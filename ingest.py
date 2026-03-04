from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os

documents = []

for file in os.listdir("docs"):
    loader = TextLoader(f"docs/{file}")
    documents.extend(loader.load())

embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(documents, embeddings)

vectorstore.save_local("vector_db")

print("Documents embedded successfully")