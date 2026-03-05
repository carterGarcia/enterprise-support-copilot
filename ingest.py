import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document

# Load environment variables from a local .env file (kept out of git)
load_dotenv()

# Read API key once and validate it before making any network calls
api_key = os.getenv("OPENAI_API_KEY", "").strip()

# Fail fast if the key is missing or still a placeholder from .env.example
if not api_key or "replace" in api_key.lower() or api_key.lower().startswith("your_"):
    raise RuntimeError(
        "OPENAI_API_KEY is not set or still a placeholder.\n"
        "Fix: copy .env.example to .env, then edit .env and set:\n"
        "OPENAI_API_KEY=sk-...your real key...\n"
        "Do not commit .env to git."
    )

# Basic sanity check to catch obvious mistakes
if not api_key.startswith("sk-"):
    raise RuntimeError(
        "OPENAI_API_KEY does not look like a valid OpenAI key.\n"
        "It should usually start with 'sk-'. Check your .env value."
    )

# Load documents from ./docs and attach filenames as metadata for citations in the UI
docs = []
for file in os.listdir("docs"):
    path = os.path.join("docs", file)

    # Skip subfolders or non-file entries
    if not os.path.isfile(path):
        continue

    # Read the full document as text (UTF-8 for portability)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Store source filename so the app can display which docs were used
    docs.append(Document(page_content=text, metadata={"source": file}))

# Guard against empty knowledge bases
if not docs:
    raise RuntimeError("No documents found in ./docs. Add .txt files and retry.")

# Create embeddings for the docs (same model used at query time)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Build a FAISS vector index from documents and persist it locally
vectorstore = FAISS.from_documents(docs, embeddings)
vectorstore.save_local("vector_db")

print("Saved vectorstore to vector_db")