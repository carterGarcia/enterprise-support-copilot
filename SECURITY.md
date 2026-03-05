# Security

## API keys
- Do not commit `.env` or any `.env.*` files.
- Store secrets in environment variables or a local `.env` file.
- If a key is exposed, revoke it immediately and create a new one.

## Generated artifacts
- `vector_db/` is generated locally by `ingest.py` and should not be committed.

## Recommended safeguards
- Set a low monthly usage limit in your OpenAI billing settings.
- Use least-privilege keys and rotate regularly.

### Two quick checks for consistency
- Make sure the repo actually contains **`.env.example`** (it was missing in your earlier zip).
- Ensure your Makefile supports `PYTHON=...` override (it should if you used `PYTHON?=`).

If you paste your `Makefile` and confirm whether `.env.example` exists, I’ll tell you if any README commands won’t work as written.