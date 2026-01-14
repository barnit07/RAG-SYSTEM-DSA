BlinkNow – Data Structures & Algorithms RAG Assistant
====================================================

BlinkNow is a production-style Retrieval-Augmented Generation (RAG) system built
to answer Data Structures & Algorithms (DSA) questions accurately and transparently.

Unlike a basic chatbot, this project:
- Retrieves answers from a vector database
- Supports history-aware follow-up questions
- Clearly shows the knowledge chunks used to generate answers
- Separates ingestion from inference, similar to real-world systems


FEATURES
--------
- Retrieval-Augmented Generation (RAG)
- History-aware multi-turn conversations
- Query rewriting and re-ranking
- Transparent chunk retrieval display
- Gradio-based interactive UI
- Clean and reproducible setup


ARCHITECTURE OVERVIEW
---------------------
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

Note:
Meta or conversational questions (e.g., "What can you answer?")
intentionally skip retrieval.


TECH STACK
----------
- Python: 3.11.9
- LLM: OpenAI (via LangChain)
- Embeddings: text-embedding-3-large
- Vector Database: Chroma
- Frameworks: LangChain, Gradio


PREREQUISITES
-------------
1. Python 3.11.9
   Check with:
   python --version

2. OpenAI API Key
   Create a .env file in the project root with:
   OPENAI_API_KEY=your_api_key_here


STEP-BY-STEP SETUP
------------------
IMPORTANT:
The vector database is NOT committed to GitHub by design.
You must run the ingestion step once after cloning.

1) Clone the repository
   git clone https://github.com/barnit07/RAG-SYSTEM-DSA.git
   cd RAG-SYSTEM-DSA

2) Create and activate a virtual environment
   python -m venv venv

   Windows:
   venv\Scripts\activate

   macOS / Linux:
   source venv/bin/activate

3) Install dependencies
   pip install -r requirements.txt

4) Build the vector database (MANDATORY)
   python ingest.py

   Expected output:
   Ingestion Complete

5) Run the application
   python app.py

   The Gradio UI will open in your browser.


HOW TO TEST
-----------
Try the following sequence in the UI:

- What is a stack?
- Give an example
- Compare it with a queue

Expected behavior:
1) Retrieved chunks shown for factual questions
2) Correct handling of follow-up questions
3) History-aware responses


PROJECT STRUCTURE
-----------------
RAG-SYSTEM-DSA/
│
├── app.py              # Gradio UI
├── answer.py           # RAG pipeline logic
├── ingest.py           # Knowledge base ingestion
├── requirements.txt    # Dependencies
├── knowledge-base/     # DSA source documents
├── database/           # (Generated) Chroma vector DB
├── .env                # API keys (not committed)
└── README.txt


IMPORTANT NOTES
---------------
- The database/ directory is generated locally and ignored by Git.
- This mirrors real-world RAG deployments where embeddings
  are environment-specific.
- On a fresh clone, ingest.py must be run once before starting the app.


DESIGN DECISIONS
----------------
- Bounded conversation history prevents context drift
- Conditional retrieval avoids unnecessary vector searches
- Re-ranking improves answer relevance
- Clear separation of ingestion and inference improves reproducibility


AUTHOR
------
Barnit Khatiwada
Aspiring AI / LLM Engineer
Focused on building robust, production-ready RAG systems
