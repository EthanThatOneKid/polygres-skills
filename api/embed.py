import os

import diskcache
from google import genai
from google.genai import types

_GEMINI_MODEL = "gemini-embedding-2"
_CACHE = diskcache.Cache(os.path.join(os.path.dirname(__file__), "..", "embedding_cache"))


def get_client() -> genai.Client:
    return genai.Client(api_key=os.environ["GEMINI_API_KEY"])


_EMBED_DIM = 768


def embed_text(text: str) -> list[float]:
    cached = _CACHE.get(text)
    if cached is not None:
        return cached
    client = get_client()
    result = client.models.embed_content(
        model=_GEMINI_MODEL,
        contents=text,
        config=types.EmbedContentConfig(output_dimensionality=_EMBED_DIM),
    )
    embedding = result.embeddings[0].values
    _CACHE.set(text, embedding, expire=86400 * 30)
    return embedding


def embed_many(texts: list[str]) -> list[list[float]]:
    client = get_client()
    result = client.models.embed_content(
        model=_GEMINI_MODEL,
        contents=[
            types.Content(parts=[types.Part(text=t)])
            for t in texts
        ],
        config=types.EmbedContentConfig(output_dimensionality=_EMBED_DIM),
    )
    return [e.values for e in result.embeddings]
