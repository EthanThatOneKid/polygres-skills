import json
import os
from dataclasses import dataclass, field
from typing import Any

from polygres import Polygres
from polygres.models import Page, VectorResult, GraphResult

_CHUNK_INDEX_PATH = os.path.join(os.path.dirname(__file__), "chunk_index.json")
_CHUNK_INDEX: dict[str, str] = {}
if os.path.exists(_CHUNK_INDEX_PATH):
    with open(_CHUNK_INDEX_PATH, encoding="utf-8") as _f:
        _CHUNK_INDEX = json.load(_f)


@dataclass
class SearchConfig:
    api_key: str = field(default_factory=lambda: os.environ["POLYGRES_API_KEY"])
    runtime_url: str = field(default_factory=lambda: os.environ["POLYGRES_RUNTIME_URL"])


_client: Polygres | None = None
_project: Any | None = None


def get_client(cfg: SearchConfig | None = None) -> Polygres:
    global _client
    if _client is None:
        c = cfg or SearchConfig()
        _client = Polygres(api_key=c.api_key, runtime_url=c.runtime_url)
    return _client


def get_project(cfg: SearchConfig | None = None) -> Any:
    global _project
    if _project is None:
        _project = get_client(cfg).project()
    return _project


def vector_search(
    embedding: list[float],
    config_name: str | None = None,
    filters: dict[str, str] | None = None,
    min_similarity: float | None = None,
    limit: int = 10,
) -> Page[VectorResult]:
    project = get_project()
    return project.vector.search(
        embedding,
        config=config_name,
        filters=filters,
        min_similarity=min_similarity,
        limit=limit,
    )


def graph_search(
    source_id: str,
    config_name: str | None = None,
    limit: int = 20,
) -> list[dict[str, Any]]:
    project = get_project()
    try:
        page = project.graph.search(
            source_id,
            config=config_name,
            limit=limit,
        )
        return [
            {
                "id": r.id,
                "score": r.score,
                "properties": r.properties,
            }
            for r in page.results
        ]
    except AttributeError:
        return []


def format_chunk_results(page: Page[VectorResult]) -> list[dict[str, Any]]:
    return [
        {
            "chunk_id": result.id,
            "doc_id": result.properties.get("doc_id", result.id.split("_", 2)[1] if "_" in result.id else result.id),
            "content": _CHUNK_INDEX.get(result.id, result.properties.get("content", "")),
            "score": result.score,
        }
        for result in page.results
    ]


def format_results(page: Page[VectorResult]) -> list[dict[str, Any]]:
    return [
        {
            "id": result.id,
            "score": result.score,
            "properties": result.properties,
        }
        for result in page.results
    ]
