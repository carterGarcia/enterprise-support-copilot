import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY", "").strip()

# Common placeholder patterns from .env.example
if not api_key or "replace" in api_key.lower() or api_key.lower().startswith("your_"):
    raise RuntimeError(
        "OPENAI_API_KEY is not set or still a placeholder.\n"
        "Fix: copy .env.example to .env, then edit .env and set:\n"
        "OPENAI_API_KEY=sk-...your real key...\n"
        "Do not commit .env to git."
    )

if not api_key.startswith("sk-"):
    raise RuntimeError(
        "OPENAI_API_KEY does not look like a valid OpenAI key.\n"
        "It should usually start with 'sk-'. Check your .env value."
    )

docs = []
for file in os.listdir("docs"):
    path = os.path.join("docs", file)
    if not os.path.isfile(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    docs.append(Document(page_content=text, metadata={"source": file}))

if not docs:
    raise RuntimeError("No documents found in ./docs. Add .txt files and retry.")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = FAISS.from_documents(docs, embeddings)
vectorstore.save_local("vector_db")

print("Saved vectorstore to vector_db")