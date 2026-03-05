# Enterprise Support Copilot (RAG)

An employee self service style Copilot that answers IT and HR questions using retrieval augmented generation (RAG).

Provide internal style documentation in ./docs. This project embeds those docs into a local FAISS vector store and uses an LLM to answer questions grounded in retrieved context.

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
- Basic safety practices (local secrets via .env, generated artifacts ignored)

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
- docs/ put support documentation here as .txt files
- ingest.py builds the local vector store at vector_db/
- app.py Streamlit app for querying the knowledge base
- vector_db/ generated locally, do not commit

## Setup

### 1) Create a virtual environment and install dependencies
Using Make (recommended):

make setup

If your Python is installed differently:

make setup PYTHON=python3

### 2) Configure your API key
Create a local .env file from the template:

cp .env.example .env

Edit .env and set:

OPENAI_API_KEY=your_openai_key_here

### 3) Build the vector store
make ingest

### 4) Run the app
make run

## Usage
In the Streamlit UI, ask questions like:
- How do I request PTO?
- How do I reset my VPN password?
- How do I set up Outlook on a new device?

If the documentation does not contain the answer, the assistant should respond that it does not know.

## Updating documentation
If you add or change files in docs/, rebuild the vector store:

rm -rf vector_db
make ingest

## Security
- Keep secrets in .env locally. Never commit .env or .env.*
- If you accidentally expose a key, revoke it immediately and create a new one.
- vector_db/ is generated locally and should not be pushed to GitHub.

## License
MIT