import os
import glob
from pathlib import Path
from unittest import loader
from langchain_community.document_loaders import TextLoader,DirectoryLoader
from langchain_core import document_loaders
from openai import OpenAI
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from openai.types import embedding, vector_store

model="gpt-5-nano"
load_dotenv(override=True)

db_name= str(Path(__file__).parent/"database")
knowledge_base= str(Path(__file__).parent/"knowledge-base")

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

def fetch_documents():
    documents=[]
    folders= glob.glob(str(Path(knowledge_base)/'*'))
    for folder in folders:
            doc_type= os.path.basename(folder)
            loader= DirectoryLoader(
                folder, glob="**/*.md",loader_cls=TextLoader,loader_kwargs={"encoding": "utf-8"}
            )
            folder_docs= loader.load()

            for doc in folder_docs:
                doc.metadata["doc_type"]=doc_type
                documents.append(doc)
    return documents

def create_chunks(documents):
    text_splitter= RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
    chunks=text_splitter.split_documents(documents)
    return chunks


def create_embeddings(chunks):
    if os.path.exists(db_name):
        Chroma(persist_directory=db_name, embedding_function=embeddings).delete_collection()
    
    vectorstore= Chroma.from_documents(
        documents=chunks, embedding=embeddings, persist_directory=db_name,collection_name="docs",
    )

    return vectorstore

if __name__=="__main__":
    documents = fetch_documents()
    print("Loaded documents:", len(documents))

    chunks= create_chunks(documents)
    print("Chunks created:", len(chunks))

    vectorstore = create_embeddings(chunks)
    print("Stored in Chroma:", vectorstore._collection.count())


    print("Ingestion complete")





