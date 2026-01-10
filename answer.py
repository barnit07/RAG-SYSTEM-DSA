from chromadb.api.types import D
from dotenv import load_dotenv
from pathlib import Path
from typing import List
from langchain_core.language_models import LLM
from tenacity import retry, wait_exponential
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain



load_dotenv(override=True)
MODEL= "gpt-4.1-nano"
db_name= str(Path(__file__).parent/"database")
collection_name="docs"

embedding_model= OpenAIEmbeddings(model="text-embedding-3-large")
wait= wait_exponential(multiplier=1, min=10, max=240)
RETRIEVAL_K=20
FINAL_K=10

vectorstore=Chroma(
    persist_directory=db_name,
    collection_name=collection_name,
    embedding_function=embedding_model,
)
# print("Chroma document count:", vectorstore._collection.count())


retriever= vectorstore.as_retriever(search_kwargs={"k":RETRIEVAL_K})

rewrite_prompt = ChatPromptTemplate.from_template("""
You are in a conversation with a user, answering questions about the Subject Data Structures and Algorithms.
You are about to look up information in a Knowledge Base to answer the user's question.

This is the history of your conversation so far with the user:
{history}

And this is the user's current question:
{question}

Respond only with a short, refined question that you will use to search the Knowledge Base.
It should be a VERY short specific question most likely to surface content.
IMPORTANT: Respond ONLY with the precise knowledgebase query, nothing else.
Do not use question words like what, how, why.
""")

rewrite_llm= ChatOpenAI(model= MODEL)
rewrite_chain = rewrite_prompt | rewrite_llm

@retry(wait=wait)
def rewrite_query(question, history=""):
    response = rewrite_chain.invoke({
        "question": question,
        "history": history
    })
    return response.content.strip()


def fetch_context_unranked(question):
    return retriever.invoke(question)

def merge_chunks(chunk1, chunk2):
    seen={doc.page_content for doc in chunk1}
    merged= chunk1[:]
    for doc in chunk2:
        if doc.page_content not in seen:
            merged.append(doc)
    
    return merged

rerank_prompt = ChatPromptTemplate.from_template("""
You are a document re-ranker.
You are provided with a question and a list of relevant chunks of text from a query of a knowledge base.
The chunks are provided in the order they were retrieved.

You must rank order the provided chunks by relevance to the question, with the most relevant chunk first.
Reply only with the list of ranked chunk ids, nothing else.

Question:
{question}

Chunks:
{chunks}
""")

rerank_llm= ChatOpenAI(model=MODEL)
rerank_chain= rerank_prompt | rerank_llm

import re

def rerank(question, chunks):
    formatted_chunks = ""
    for i, chunk in enumerate(chunks):
        formatted_chunks += f"#Chunk ID: {i+1}\n{chunk.page_content}\n\n"

    response = rerank_chain.invoke({
        "question": question,
        "chunks": formatted_chunks
    })

    response_text = response.content
    order = list(map(int, re.findall(r"\d+", response_text)))

    return [chunks[i-1] for i in order if 1 <= i <= len(chunks)]


def fetch_context(question):
    rewritten= rewrite_query(question)
    chunk1= fetch_context_unranked(question)
    chunk2= fetch_context_unranked(rewritten)
    merged= merge_chunks(chunk1,chunk2)
    reranked= rerank(question,merged)
    return reranked[:FINAL_K]

SYSTEM_PROMPT = """
You are a knowledgeable, friendly assistant representing the the company called BlinkNow which helps to answer the questions related to Data Structures and Algorithms.
You are chatting with a user about contents of the Subject Data Structures and Algorithms.
Your answer will be evaluated for accuracy, relevance and completeness, so make sure it only answers the question and fully answers it.
If you don't know the answer, say so.
For context, here are specific extracts from the Knowledge Base that might be directly relevant to the user's question:
{context}

With this context, please answer the user's question. Be accurate, relevant and complete.
"""

answer_prompt= ChatPromptTemplate.from_messages([
    ("system",SYSTEM_PROMPT),
    ("human","{question}")
])

answer_llm=ChatOpenAI(model=MODEL)
answer_chain=answer_prompt | answer_llm

@retry(wait=wait)
def answer_question(question,history):
    chunks= fetch_context(question)
    context = "\n\n".join(
        f"Extract from {doc.metadata.get('source', 'unknown')}:\n{doc.page_content}"
        for doc in chunks
    )
    response = answer_chain.invoke({
    "question": question,
    "context": context
    })
    answer = response.content
    return answer,chunks



# TEST_QUESTION = "How to delete an element from an array?"
# TEST_HISTORY = "User previously asked about stack and queue"

# print("\n[TEST] answer_question")
# answer, used_chunks = answer_question(TEST_QUESTION, TEST_HISTORY)

# print("\nANSWER:\n", answer)
# print("\nChunks used:", len(used_chunks))




