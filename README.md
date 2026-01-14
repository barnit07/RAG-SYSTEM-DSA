# 📘 BlinkNow – Data Structures & Algorithms RAG Assistant

BlinkNow is a **production-style Retrieval-Augmented Generation (RAG) system** built to answer **Data Structures & Algorithms (DSA)** questions accurately and transparently.

Unlike a basic chatbot, this project:
- Retrieves answers from a **vector database**
- Supports **history-aware follow-up questions**
- Clearly shows the **knowledge chunks** used to generate answers
- Separates **ingestion** from **inference**, like real-world systems

---

## 🚀 Features

- Retrieval-Augmented Generation (RAG)
- History-aware multi-turn conversations
- Query rewriting + re-ranking
- Transparent chunk retrieval display
- Gradio-based interactive UI
- Clean, reproducible setup

---

## 🧠 Architecture Overview

User Question
↓
Conversation History (bounded)
↓
Query Rewriting
↓
Vector Retrieval (Chroma)
↓
Chunk Merging + Re-ranking
↓
LLM Answer Generation
↓
Answer + Retrieved Context


Meta or conversational questions (e.g., *“What can you answer?”*) intentionally skip retrieval.

---

## 🛠️ Tech Stack

- **Python**: 3.11.9
- **LLM**: OpenAI (via LangChain)
- **Embeddings**: text-embedding-3-large
- **Vector Database**: Chroma
- **Frameworks**: LangChain, Gradio

---

## 📋 Prerequisites

- Python **3.11.9**
  ```bash
  python --version

OpenAI API key stored in .env
  OPENAI_API_KEY=your_api_key_here



⚙️ Step-by-Step Setup

⚠️ The vector database is not committed to GitHub by design.
You must run the ingestion step after cloning.


1️⃣ Clone the repository
git clone https://github.com/barnit07/RAG-SYSTEM-DSA.git
cd RAG-SYSTEM-DSA

2️⃣ Create and activate a virtual environment
python -m venv venv

Windows- venv\Scripts\activate
macOS / Linux- source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Build the vector database (MANDATORY)
python ingest.py

Expected output: Ingestion Complete

5️⃣ Run the application
python app.py

The Gradio UI will open in your browser.



🧪 How to Test

Try the following:

What is a stack?
Give an example
Compare it with a queue


You should observe:

1)Retrieved chunks for factual questions

2)Correct handling of follow-up questions

3)History-aware responses


📂 Project Structure
RAG-SYSTEM-DSA/
│
├── app.py              # Gradio UI
├── answer.py           # RAG pipeline logic
├── ingest.py           # Knowledge base ingestion
├── requirements.txt    # Dependencies
├── knowledge-base/     # DSA source documents
├── database/           # (Generated) Chroma vector DB
├── .env                # API keys (not committed)
└── README.md


⚠️ Important Notes

The database/ directory is generated locally and ignored by Git.
This mirrors real-world RAG deployments.
On a fresh clone, ingest.py must be run once before starting the app.


🎯 Design Decisions

Bounded history prevents context drift
Conditional retrieval avoids unnecessary vector searches
Re-ranking improves answer relevance
Clear separation of ingestion and inference


👤 Author
Barnit Khatiwada
Aspiring AI / LLM Engineer
Focused on building robust, production-ready RAG systems.

