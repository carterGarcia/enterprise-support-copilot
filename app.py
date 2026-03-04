import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

st.title("Enterprise Support Copilot")

embeddings = OpenAIEmbeddings()

vectorstore = FAISS.load_local("vector_db", embeddings)

retriever = vectorstore.as_retriever()

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=retriever
)

query = st.text_input("Ask a question about company IT or HR systems")

if query:
    response = qa.run(query)
    st.write(response)