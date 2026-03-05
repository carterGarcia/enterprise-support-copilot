# Security

## API keys
- Do not commit `.env` or any `.env.*` files.
- Store secrets in environment variables or a local `.env` file (dotenv).
- If a key is exposed (for example committed to git history), revoke it immediately and create a new one.
- `.env.example` is safe to commit and is provided as a template.

## Generated artifacts
- `vector_db/` is generated locally by `ingest.py` and should not be committed.
- If you need to rebuild the index, delete `vector_db/` and rerun ingestion.

## Recommended safeguards
- Set a low monthly usage limit in your OpenAI billing settings.
- Use least privilege keys and rotate regularly.
- Avoid running this project against sensitive proprietary documents unless you have permission and appropriate controls.