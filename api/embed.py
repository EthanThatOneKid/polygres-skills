import os

from google import genai
from google.genai import types

_GEMINI_MODEL = "gemini-embedding-2"


def get_client() -> genai.Client:
    return genai.Client(api_key=os.environ["GEMINI_API_KEY"])


_EMBED_DIM = 768


def embed_text(text: str) -> list[float]:
    client = get_client()
    result = client.models.embed_content(
        model=_GEMINI_MODEL,
        contents=text,
        config=types.EmbedContentConfig(output_dimensionality=_EMBED_DIM),
    )
    return result.embeddings[0].values


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
