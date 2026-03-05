# Enterprise Support Copilot (RAG)

An employee self service style Copilot that answers IT and HR questions using retrieval augmented generation (RAG).

Provide internal style documentation in `./docs`. This project embeds those docs into a local FAISS vector store and uses an LLM to answer questions grounded in retrieved context.

## Demo

Grounded answers with sources from the underlying knowledge base documents.

### PTO request workflow
![PTO demo](assets/demo-pto.png)

### VPN password reset
![VPN demo](assets/demo-vpn.png)

### Outlook setup on a new device
![Email setup demo](assets/demo-email.png)

## Reproducible setup

Build the local FAISS vector store from docs:

![Ingestion pipeline](assets/ingest-run.png)

## Summary
- Retrieval augmented generation architecture
- Embeddings and vector similarity search (FAISS)
- AI assistant behavior grounded on enterprise documentation
- Basic safety practices (local secrets via `.env`, generated artifacts ignored)

## Tech stack
- Python
- Streamlit UI
- LangChain (retrieval and vector store wrapper)
- OpenAI embeddings and chat completion
- FAISS local vector database

## Requirements
- Python 3.11 or 3.12 recommended  
  Python 3.14 is not supported due to LangChain and Pydantic typing compatibility.
- OpenAI API key with billing enabled  
  Set a low monthly limit for safety.

## Project structure
- `docs/` put support documentation here as `.txt` files
- `ingest.py` builds the local vector store at `vector_db/`
- `app.py` Streamlit app for querying the knowledge base
- `vector_db/` generated locally, do not commit

## Setup

### 1 Create a virtual environment and install dependencies
Using Make (recommended)