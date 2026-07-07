import os

import diskcache
import numpy as np
import onnxruntime as ort
from huggingface_hub import hf_hub_download
from tokenizers import Tokenizer

_REPO = "Xenova/all-MiniLM-L6-v2"
_MODEL_FILE = "onnx/model_quantized.onnx"
_TOKENIZER_FILE = "tokenizer.json"
_MAX_TOKENS = 256
_EMBED_DIM = 384

_CACHE = diskcache.Cache(os.path.join(os.path.dirname(__file__), "..", "embedding_cache"))

_session: ort.InferenceSession | None = None
_tokenizer: Tokenizer | None = None


def _get_session() -> ort.InferenceSession:
    global _session
    if _session is None:
        model_path = hf_hub_download(repo_id=_REPO, filename=_MODEL_FILE)
        _session = ort.InferenceSession(model_path, providers=["CPUExecutionProvider"])
    return _session


def _get_tokenizer() -> Tokenizer:
    global _tokenizer
    if _tokenizer is None:
        tokenizer_path = hf_hub_download(repo_id=_REPO, filename=_TOKENIZER_FILE)
        _tokenizer = Tokenizer.from_file(str(tokenizer_path))
        _tokenizer.enable_truncation(_MAX_TOKENS)
        _tokenizer.enable_padding(pad_id=0, pad_token="[PAD]", length=None)
    return _tokenizer


def _mean_pooling(hidden: np.ndarray, mask: np.ndarray) -> np.ndarray:
    mask_f = mask[..., np.newaxis].astype(np.float32)
    summed = (hidden * mask_f).sum(axis=1)
    counts = mask_f.sum(axis=1).clip(min=1e-9)
    return summed / counts


def _l2_normalize(v: np.ndarray) -> np.ndarray:
    return v / np.linalg.norm(v, axis=1, keepdims=True).clip(min=1e-12)


def embed_text(text: str) -> list[float]:
    cached = _CACHE.get(text)
    if cached is not None:
        return cached
    session = _get_session()
    tokenizer = _get_tokenizer()
    encoded = tokenizer.encode(text)
    input_ids = np.array([encoded.ids], dtype=np.int64)
    mask = np.array([encoded.attention_mask], dtype=np.int64)
    token_type_ids = np.zeros_like(input_ids)
    out = session.run(
        None,
        {
            "input_ids": input_ids,
            "attention_mask": mask,
            "token_type_ids": token_type_ids,
        },
    )
    pooled = _mean_pooling(out[0], mask)
    embedding = _l2_normalize(pooled)[0].tolist()
    _CACHE.set(text, embedding, expire=86400 * 30)
    return embedding


def embed_many(texts: list[str]) -> list[list[float]]:
    session = _get_session()
    tokenizer = _get_tokenizer()
    batch = tokenizer.encode_batch(texts)
    if not batch:
        return []
    max_len = max(len(e.ids) for e in batch)
    n = len(texts)
    input_ids = np.zeros((n, max_len), dtype=np.int64)
    mask = np.zeros((n, max_len), dtype=np.int64)
    for i, e in enumerate(batch):
        ids = e.ids
        attn = e.attention_mask
        input_ids[i, : len(ids)] = ids
        mask[i, : len(attn)] = attn
    token_type_ids = np.zeros_like(input_ids)
    out = session.run(
        None,
        {
            "input_ids": input_ids,
            "attention_mask": mask,
            "token_type_ids": token_type_ids,
        },
    )
    pooled = _mean_pooling(out[0], mask)
    return _l2_normalize(pooled).tolist()
