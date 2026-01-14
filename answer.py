from chromadb.api.types import D
from dotenv import load_dotenv
from pathlib import Path
from typing import List
from langchain_core.language_models import LLM
from tenacity import retry, wait_exponential
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate



MAX_HISTORY_TURNS=6
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


def fetch_context(question,history):
    rewritten= rewrite_query(question, history=history)
    chunk1= fetch_context_unranked(question)
    chunk2= fetch_context_unranked(rewritten)
    merged= merge_chunks(chunk1,chunk2)
    reranked= rerank(question,merged)
    return reranked[:FINAL_K]

SYSTEM_PROMPT = """
You are a knowledgeable, friendly assistant representing the the company called BlinkNow which helps to answer the questions related to Data Structures and Algorithms.
You are chatting with a user about contents of the Subject Data Structures and Algorithms.
Conversation so far:
{history}
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

    history_lines= history.strip().split("\n")
    history= "\n".join(history_lines[-MAX_HISTORY_TURNS*2:])
    chunks= fetch_context(question,history)
    context = "\n\n".join(
        f"Extract from {doc.metadata.get('source', 'unknown')}:\n{doc.page_content}"
        for doc in chunks
    )
    response = answer_chain.invoke({
    "question": question,
    "context": context,
    "history":history
    })
    answer = response.content
    return answer,chunks

# import os
# import re
# from pathlib import Path
# from typing import List

# from dotenv import load_dotenv
# from tenacity import retry, wait_exponential

# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langchain_chroma import Chroma
# from langchain.prompts import ChatPromptTemplate
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.document_loaders import DirectoryLoader, TextLoader


# # ---------------- ENV ----------------
# load_dotenv(override=True)

# MODEL = "gpt-4.1-nano"
# COLLECTION_NAME = "docs"

# BASE_DIR = Path(__file__).resolve().parent
# KB_DIR = BASE_DIR / "knowledge-base"
# DB_DIR = BASE_DIR / "chroma_db"

# RETRIEVAL_K = 20
# FINAL_K = 10

# wait = wait_exponential(multiplier=1, min=10, max=240)

# # ---------------- Embeddings ----------------
# embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")


# # ---------------- Build / Load Vector DB ----------------
# def load_or_create_vectorstore() -> Chroma:
#     if DB_DIR.exists():
#         vs = Chroma(
#             persist_directory=str(DB_DIR),
#             collection_name=COLLECTION_NAME,
#             embedding_function=embedding_model,
#         )
#         if vs._collection.count() > 0:
#             print(f"✅ Loaded Chroma DB ({vs._collection.count()} chunks)")
#             return vs

#     print("⚙️ Building Chroma DB from knowledge-base...")

#     loader = DirectoryLoader(
#         path=str(KB_DIR),
#         glob="**/*.md",
#         loader_cls=TextLoader,
#         loader_kwargs={"encoding": "utf-8"},
#     )
#     documents = loader.load()

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=200,
#     )
#     chunks = splitter.split_documents(documents)

#     vs = Chroma.from_documents(
#         documents=chunks,
#         embedding=embedding_model,
#         persist_directory=str(DB_DIR),
#         collection_name=COLLECTION_NAME,
#     )

#     print(f"✅ Chroma DB created ({len(chunks)} chunks)")
#     return vs


# # Build DB at startup
# vectorstore = load_or_create_vectorstore()
# retriever = vectorstore.as_retriever(search_kwargs={"k": RETRIEVAL_K})


# # ---------------- Query Rewrite ----------------
# rewrite_prompt = ChatPromptTemplate.from_template("""
# You are refining a search query for a Data Structures and Algorithms knowledge base.

# Conversation history:
# {history}

# User question:
# {question}

# Return ONLY a short, precise search query.
# Do NOT include question words.
# """)

# rewrite_llm = ChatOpenAI(model=MODEL)
# rewrite_chain = rewrite_prompt | rewrite_llm


# @retry(wait=wait)
# def rewrite_query(question, history=""):
#     return rewrite_chain.invoke({
#         "question": question,
#         "history": history
#     }).content.strip()


# # ---------------- Retrieval ----------------
# def fetch_context_unranked(query):
#     return retriever.invoke(query)


# def merge_chunks(chunks1, chunks2):
#     seen = {doc.page_content for doc in chunks1}
#     merged = list(chunks1)
#     for doc in chunks2:
#         if doc.page_content not in seen:
#             merged.append(doc)
#     return merged


# # ---------------- Reranking ----------------
# rerank_prompt = ChatPromptTemplate.from_template("""
# You are ranking document chunks by relevance.

# Question:
# {question}

# Chunks:
# {chunks}

# Return ONLY a list of chunk IDs in ranked order.
# """)

# rerank_llm = ChatOpenAI(model=MODEL)
# rerank_chain = rerank_prompt | rerank_llm


# def rerank(question, chunks):
#     formatted = ""
#     for i, chunk in enumerate(chunks, 1):
#         formatted += f"#Chunk {i}\n{chunk.page_content}\n\n"

#     response = rerank_chain.invoke({
#         "question": question,
#         "chunks": formatted
#     }).content

#     order = list(map(int, re.findall(r"\d+", response)))
#     return [chunks[i - 1] for i in order if 1 <= i <= len(chunks)]


# def fetch_context(question):
#     rewritten = rewrite_query(question)
#     c1 = fetch_context_unranked(question)
#     c2 = fetch_context_unranked(rewritten)
#     merged = merge_chunks(c1, c2)
#     ranked = rerank(question, merged)
#     return ranked[:FINAL_K]


# # ---------------- Answer Generation ----------------
# SYSTEM_PROMPT = """
# You are BlinkNow, an expert assistant for Data Structures and Algorithms.

# Use ONLY the provided context to answer.
# If the answer is not in the context, say you don't know.

# Context:
# {context}
# """

# answer_prompt = ChatPromptTemplate.from_messages([
#     ("system", SYSTEM_PROMPT),
#     ("human", "{question}")
# ])

# answer_llm = ChatOpenAI(model=MODEL)
# answer_chain = answer_prompt | answer_llm


# @retry(wait=wait)
# def answer_question(question, history=""):
#     chunks = fetch_context(question)
#     context = "\n\n".join(
#         f"{doc.page_content}"
#         for doc in chunks
#     )

#     response = answer_chain.invoke({
#         "question": question,
#         "context": context
#     })

#     return response.content, chunks







