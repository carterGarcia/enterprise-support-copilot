# enterprise-support-copilot
Setup

Create environment
make setup

Set API key
cp .env.example .env
Edit .env and set OPENAI_API_KEY

Add documents
Put .txt files in docs/

Build vector store
make ingest

Run
make run

Notes
Recommended Python 3.11 or 3.12
Tested on MacOS
Do not commit .env
Delete vector_db and rerun ingest if you change docs