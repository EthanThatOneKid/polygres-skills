import json
import os
import re
import sys
import threading
import time
from collections import defaultdict
from pathlib import Path, PurePath

import requests
import streamlit as st

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_PROJECT_ROOT))

_API_PORT = 8543
API_BASE = os.getenv("POLYGRES_DOCS_API", f"http://127.0.0.1:{_API_PORT}")

if API_BASE.startswith("http://127.0.0.1"):
    import uvicorn
    from api.search_api import app as _fastapi_app

    def _start_api():
        uvicorn.run(_fastapi_app, host="127.0.0.1", port=_API_PORT, log_level="warning")

    t = threading.Thread(target=_start_api, daemon=True)
    t.start()
    for _ in range(20):
        try:
            requests.get(f"{API_BASE}/health", timeout=1)
            break
        except requests.RequestException:
            time.sleep(0.5)


def _load_manifest():
    path = _PROJECT_ROOT / "references" / "upstream" / "manifest.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}, {}, {}

    urls, names, cats = {}, {}, {}
    for item in data.get("items", []):
        p = PurePath(item["path"])
        doc_id = p.stem
        urls[doc_id] = item["url"]
        names[doc_id] = item["title"].replace(" | Polygres", "").strip()
        try:
            rel = p.relative_to("polygres")
        except ValueError:
            rel = p
        parent = rel.parent
        if parent == PurePath("."):
            cats[doc_id] = "home" if doc_id == "index" else doc_id
        else:
            cats[doc_id] = parent.name
    return urls, names, cats


def _load_links():
    path = _PROJECT_ROOT / "import_doc_links.sql"
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return {}

    links = defaultdict(list)
    for match in re.finditer(r"\('([^']+)',\s*'([^']+)',\s*'[^']*'\)", text):
        src, tgt = match.group(1), match.group(2)
        if src != tgt:
            links[src].append(tgt)
    return dict(links)


DOC_URLS, DOC_DISPLAY_NAMES, DOC_CATEGORIES = _load_manifest()
KNOWN_LINKS = _load_links()
ALL_DOC_IDS = list(DOC_DISPLAY_NAMES.keys())

st.set_page_config(
    page_title="Polygres Docs Search",
    page_icon="",
    layout="wide",
)

st.title(" Polygres Docs Search Demo")
st.markdown("Search the Polygres documentation corpus using **vector** and **graph** retrieval.")

tab_vec, tab_graph, tab_health = st.tabs([
    " Vector Search",
    " Graph Explorer",
    " Health",
])

with tab_vec:
    st.subheader("Semantic Vector Search")
    st.markdown("Ask a question in plain text — the API embeds your query with **all-MiniLM-L6-v2** (384d, ONNX on-device) and returns ranked results from Polygres.")

    query = st.text_input(
        "Search query",
        value="How do I configure vector search?",
        placeholder="e.g. How do I set up retrieval?",
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        limit = st.slider("Max results", 1, 20, 5)
    with col2:
        min_sim = st.slider("Min similarity", 0.0, 1.0, 0.0, 0.01)

    if st.button("Search", type="primary", key="vec_search"):
        with st.spinner("Embedding query & searching..."):
            try:
                r = requests.post(
                    f"{API_BASE}/search/chunks",
                    json={"query": query, "limit": limit, "min_similarity": min_sim},
                    timeout=30,
                )
                r.raise_for_status()
                data = r.json()
            except requests.RequestException as e:
                st.error(f"API call failed: {e}")
                st.stop()

        items = data.get("results", [])
        if not items:
            st.info("No results found.")
        else:
            grouped = defaultdict(list)
            for item in items:
                grouped[item["doc_id"]].append(item)

            st.success(f"Found {len(items)} chunk(s) across {len(grouped)} page(s)")

            rank = 0
            for doc_id, chunks in grouped.items():
                title = DOC_DISPLAY_NAMES.get(doc_id, doc_id)
                cat = DOC_CATEGORIES.get(doc_id, "?")
                url = DOC_URLS.get(doc_id, "")

                with st.container(border=True):
                    rank += 1
                    link = f"[**{rank}. {title}**]({url})" if url else f"**{rank}. {title}**"
                    st.markdown(f"{link}  `{cat}`  —  {len(chunks)} matching chunk(s)")

                    for chunk in chunks:
                        snippet = chunk.get("content", "")[:200]
                        if len(chunk.get("content", "")) > 200:
                            snippet += "..."
                        cols = st.columns([5, 1])
                        with cols[0]:
                            st.markdown(f"```\n{snippet}\n```")
                        with cols[1]:
                            st.markdown(f"`{chunk['score']:.4f}`")

            result_ids = set(grouped.keys())
            edges = []
            for src in result_ids:
                for tgt in KNOWN_LINKS.get(src, []):
                    if tgt in result_ids:
                        edges.append((src, tgt))

            with st.expander(" Graph View — Result Interconnections"):
                if not edges:
                    st.caption("No interconnections between these results")
                else:
                    def _safe(id_: str) -> str:
                        return id_.replace("-", "_")

                    seen = set()
                    for src, tgt in edges:
                        seen.add(src)
                        seen.add(tgt)

                    lines = ["flowchart LR"]
                    for n in seen:
                        label = DOC_DISPLAY_NAMES.get(n, n)
                        lines.append(f'  {_safe(n)}["{label}"]')
                    for src, tgt in edges:
                        lines.append(f"  {_safe(src)} --> {_safe(tgt)}")
                    for n in seen:
                        url = DOC_URLS.get(n, "")
                        if url:
                            lines.append(f'  click {_safe(n)} href "{url}" _blank')
                    st.markdown("```mermaid\n" + "\n".join(lines) + "\n```")

with tab_graph:
    st.subheader("Document Graph Explorer")
    st.markdown("Select a doc page to see which other pages it references (outbound links) and which pages reference it (inbound links).")

    selected = st.selectbox(
        "Choose a document",
        options=ALL_DOC_IDS,
        format_func=lambda x: f"{DOC_DISPLAY_NAMES.get(x, x)}  ({DOC_CATEGORIES.get(x, '?')})",
        index=ALL_DOC_IDS.index("key-concepts") if "key-concepts" in ALL_DOC_IDS else 0,
    )

    outbound = KNOWN_LINKS.get(selected, [])
    inbound = []
    for src, tgts in KNOWN_LINKS.items():
        if src != selected and selected in tgts:
            inbound.append(src)

    def _doc_link(doc_id: str) -> str:
        name = DOC_DISPLAY_NAMES.get(doc_id, doc_id)
        url = DOC_URLS.get(doc_id, "")
        cat = DOC_CATEGORIES.get(doc_id, "?")
        if url:
            return f"- [{name}]({url}) `{cat}`"
        return f"- **{name}** `{cat}`"

    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("####  Outbound Links")
        if outbound:
            for target in outbound:
                st.markdown(_doc_link(target))
        else:
            st.caption("No outbound links")

    with col_r:
        st.markdown("####  Inbound Links")
        if inbound:
            for source in inbound:
                st.markdown(_doc_link(source))
        else:
            st.caption("No inbound links")

    st.divider()
    st.markdown("#### Graph search via API")
    if st.button("Fetch from API", key="graph_fetch"):
        with st.spinner("Querying graph search endpoint..."):
            try:
                r = requests.get(
                    f"{API_BASE}/graph/neighbors/{selected}",
                    timeout=10,
                )
                r.raise_for_status()
                data = r.json()
                st.json(data)
            except requests.RequestException as e:
                st.info(f"Graph API not available (expected if graph search isn't configured in Polygres): {e}")

with tab_health:
    st.subheader("API Health")

    if st.button("Check Health", type="primary"):
        with st.spinner("Pinging API..."):
            try:
                r = requests.get(f"{API_BASE}/health", timeout=5)
                r.raise_for_status()
                data = r.json()
            except requests.RequestException as e:
                st.error(f"API unreachable: {e}")
                st.stop()

        status = data.get("status", "unknown")
        readiness = data.get("readiness", {})

        st.metric("Status", status.upper())

        cols = st.columns(3)
        readiness_icons = {
            "vector": (" Vector", "inactive"),
            "graph": (" Graph", "inactive"),
            "hybrid": (" Hybrid", "inactive"),
        }
        for key, (label, _) in readiness_icons.items():
            ready = readiness.get(key, False)
            readiness_icons[key] = (
                f"✅ {label}" if ready else f"⬜ {label}"
            )

        for i, (key, display) in enumerate(readiness_icons.items()):
            cols[i].metric(display, "Ready" if readiness.get(key) else "Not configured")

        if readiness.get("vector"):
            st.success("Vector search is configured and ready to serve queries.")
        if readiness.get("graph"):
            st.success("Graph search is configured and ready to query document relationships.")
        if readiness.get("hybrid"):
            st.success("Hybrid search is available (combined vector + graph).")

st.divider()
st.caption(
    f"API: `{API_BASE}`  ·  "
    "[Polygres Docs](https://docs.evokoa.com/polygres)  ·  "
    "`{query}` embedded via all-MiniLM-L6-v2 (ONNX)"
)
