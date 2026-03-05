import os
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY not set. Create a .env file with OPENAI_API_KEY=...")

import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

st.title("Enterprise Support Copilot")

embeddings = OpenAIEmbeddings()

if not os.path.exists("vector_db"):
    st.warning("Vector store not found. Run: make ingest or python3 ingest.py")
    st.stop()

vectorstore = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever()

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=retriever
)

query = st.text_input("Ask a question about company IT or HR systems")

if query:
    response = qa.run(query)
    st.write(response)