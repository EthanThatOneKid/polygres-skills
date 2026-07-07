import os
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from api.embed import embed_text
from api.search_helper import get_project, vector_search, graph_search, format_results, format_chunk_results

app = FastAPI(
    title="Polygres Docs Search API",
    description="Vector search over the Polygres documentation corpus using the Polygres SDK + ONNX on-device embeddings (all-MiniLM-L6-v2).",
    version="0.3.0",
)


class RawSearchRequest(BaseModel):
    embedding: list[float] = Field(
        ...,
        description="Dense vector embedding. Must match the dimension of your Polygres vector index (384 for all-MiniLM-L6-v2).",
        examples=[[0.01, 0.02, 0.03]],
    )
    config: str | None = Field(
        default=None,
        description="Polygres Vector Search config name. Omit to use the project default.",
    )
    limit: int = Field(default=10, ge=1, le=100)
    min_similarity: float | None = Field(default=None, ge=0.0, le=1.0)


class TextSearchRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=1,
        description="Plain-text search query. Embedded server-side via all-MiniLM-L6-v2 (ONNX, on-device).",
        examples=["How do I configure vector search?"],
    )
    config: str | None = Field(
        default=None,
        description="Polygres Vector Search config name. Omit to use the project default.",
    )
    limit: int = Field(default=10, ge=1, le=100)
    min_similarity: float | None = Field(default=None, ge=0.0, le=1.0)


class SearchResultItem(BaseModel):
    id: str
    score: float
    properties: dict[str, Any]


class SearchResponse(BaseModel):
    results: list[SearchResultItem]
    request_id: str | None = None


class ChunkSearchResultItem(BaseModel):
    chunk_id: str
    doc_id: str
    content: str
    score: float


class ChunkSearchResponse(BaseModel):
    results: list[ChunkSearchResultItem]
    request_id: str | None = None


@app.post("/search", response_model=SearchResponse)
def search_raw(body: RawSearchRequest):
    """
    Vector search with a pre-computed embedding (searches docs_pages).

    Use this when you already have an embedding from your own client-side model.
    """
    return _run_search(body.embedding, body.config, body.limit, body.min_similarity)


@app.post("/search/text", response_model=ChunkSearchResponse)
def search_text(body: TextSearchRequest):
    """
    Vector search from plain text against chunked doc content.

    Embeds the query server-side using all-MiniLM-L6-v2 (384d, ONNX),
    then searches doc_chunks with the resulting vector.
    """
    embedding = embed_text(body.query)
    return _run_chunk_search(embedding, body.config, body.limit, body.min_similarity)


@app.post("/search/chunks", response_model=ChunkSearchResponse)
def search_chunks(body: TextSearchRequest):
    """
    Explicit chunk-level vector search from plain text.
    """
    embedding = embed_text(body.query)
    return _run_chunk_search(embedding, body.config, body.limit, body.min_similarity)


def _run_search(
    embedding: list[float],
    config: str | None,
    limit: int,
    min_similarity: float | None,
) -> SearchResponse:
    try:
        page = vector_search(
            embedding=embedding,
            config_name=config,
            limit=limit,
            min_similarity=min_similarity,
        )
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))

    return SearchResponse(
        results=format_results(page),
        request_id=getattr(page, "request_id", None),
    )


def _run_chunk_search(
    embedding: list[float],
    config: str | None,
    limit: int,
    min_similarity: float | None,
) -> ChunkSearchResponse:
    if config is None:
        config = os.getenv("POLYGRES_CHUNK_CONFIG", "doc_chunks_embedding")
    try:
        page = vector_search(
            embedding=embedding,
            config_name=config,
            limit=limit,
            min_similarity=min_similarity,
        )
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))

    return ChunkSearchResponse(
        results=format_chunk_results(page),
        request_id=getattr(page, "request_id", None),
    )


@app.get("/graph/neighbors/{doc_id}")
def graph_neighbors(doc_id: str, limit: int = 20):
    """
    Graph search: find pages connected to the given doc via doc_links.
    """
    try:
        results = graph_search(doc_id, limit=limit)
        return {"results": results}
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))


@app.get("/health")
def health() -> dict[str, Any]:
    try:
        readiness = get_project().readiness()
        return {
            "status": "ok",
            "readiness": {
                "graph": readiness.graph,
                "vector": readiness.vector,
                "hybrid": readiness.hybrid,
            },
        }
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))
