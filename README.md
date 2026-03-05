# Enterprise Support Copilot

An employee self service style Copilot that answers IT and HR questions using retrieval augmented generation (RAG).

You provide internal style documentation in `./docs`. The project embeds those docs into a local FAISS vector store and uses an LLM to answer questions grounded in retrieved context.

## What this demonstrates
- RAG architecture (retrieve relevant context then generate an answer)
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
- `docs/`  
  Put your support documentation here as `.txt` files.
- `ingest.py`  
  Builds the local vector store at `vector_db/`.
- `app.py`  
  Streamlit app for querying the knowledge base.
- `vector_db/`  
  Generated locally. Do not commit this folder.

## Setup

### 1 Create a virtual environment and install dependencies
Using Make (recommended):

```bash
make setup