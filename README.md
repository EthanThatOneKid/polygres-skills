# polygres-skills

Nightly-mirrored Polygres docs, a companion `polygres` agent skill, and a search UI with **vector** + **graph** retrieval over the full documentation corpus.

## What lives here

- `skills/polygres/SKILL.md` — master skill entry point
- `references/upstream/pages/` — mirrored Polygres docs pages (22 pages, ~119 chunks)
- `api/` — FastAPI search server with vector (chunk-level) and graph search
- `ui/streamlit_app.py` — Streamlit dashboard that embeds the API and provides a search UI
- `scripts/sync_polygres_sources.py` — nightly mirror job

## Prerequisites

- Python 3.11+
- A [Polygres](https://docs.evokoa.com/polygres) account with a project
- A [Gemini API key](https://aistudio.google.com/apikey)

## Setup

1. Clone the repo:

```bash
git clone https://github.com/EthanThatOneKid/polygres-skills.git
cd polygres-skills
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file:

```env
POLYGRES_RUNTIME_URL=https://{project_id}.api.db.polygres.com/v1
POLYGRES_API_KEY=poly_live_{key}
GEMINI_API_KEY=your_gemini_api_key
```

4. Import the database schema:

Open the [Polygres SQL Editor](https://docs.evokoa.com/polygres) and run:
   - `import_docs_pages.sql` — creates the `docs_pages` table (page metadata + doc-level embeddings)
   - `import_doc_links.sql` — creates the `doc_links` table (cross-reference graph edges)
   - `import_doc_chunks.sql` — creates the `doc_chunks` table (paragraph-level chunked content)

5. Generate chunk embeddings:

```bash
python api/enrich_docs.py --direct
```

This reads the mirrored markdown files, strips frontmatter, chunks by section, generates Gemini embeddings for all ~119 chunks, and writes them to your Polygres project.

6. Configure vector search in the Polygres dashboard:

   - Create a Vector Search config on `doc_chunks.embedding`
   - (Optional) Create a config on `docs_pages.embedding` for backward compat

## Run locally

```bash
streamlit run ui/streamlit_app.py
```

Opens at `http://localhost:8501`. The FastAPI server starts automatically on port 8543 as a background thread embedded in the Streamlit process.

## Deploy (free — Streamlit Community Cloud)

1. Push the repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and deploy.
3. Set these **secrets** (Streamlit Cloud > Settings > Secrets):

```toml
POLYGRES_RUNTIME_URL = "https://{project_id}.api.db.polygres.com/v1"
POLYGRES_API_KEY = "poly_live_{key}"
GEMINI_API_KEY = "your_gemini_api_key"
```

4. Set the **App location** to `ui/streamlit_app.py`.

The FastAPI server is embedded as a daemon thread — no separate hosting needed. Both processes share the Streamlit Cloud instance (1 GB RAM, sufficient for this corpus).

## Search API

The embedded API exposes three endpoints:

| Endpoint | Description |
|---|---|
| `POST /search` | Vector search on `docs_pages` (raw embedding, backward compat) |
| `POST /search/text` | Text search on `doc_chunks` (default, embeds via Gemini) |
| `POST /search/chunks` | Explicit chunk-level text search |
| `GET /graph/neighbors/{doc_id}` | Graph neighbors from `doc_links` |
| `GET /health` | Polygres readiness (graph / vector / hybrid) |

## Skill

The `polygres` skill is routed from the mirrored docs:

- `start` — product overview and onboarding
- `workspace` — organization, projects, data, and dashboard operations
- `sdk` — application integration and client setup
- `retrieve` — retrieval configuration and query patterns
- `reference` — guardrails, permissions, limits, and troubleshooting

### Install the skill

```bash
npx skills add https://github.com/EthanThatOneKid/polygres-skills --skill polygres
```

## Sync docs mirror

```bash
python scripts/sync_polygres_sources.py
```

Re-downloads all docs pages, updates `manifest.json`, and prunes stale files. Run overnight (or manually) to keep the corpus current.
