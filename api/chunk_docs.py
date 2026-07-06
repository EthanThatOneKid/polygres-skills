import re


def _is_heading(line: str) -> bool:
    line = line.strip()
    if not line:
        return False
    if re.match(r"^\d+[\.\)]\s+[A-Z]", line):
        return True
    if len(line) < 80 and re.match(r"^[A-Z][a-z]+(\s+[A-Z][a-z]+){0,4}$", line):
        return True
    return False


def _split_oversized(text: str, max_size: int = 1800) -> list[str]:
    if len(text) <= max_size:
        return [text]
    lines = text.split("\n")
    mid = len(lines) // 2
    left = "\n".join(lines[:mid])
    right = "\n".join(lines[mid:])
    result: list[str] = []
    result.extend(_split_oversized(left, max_size))
    result.extend(_split_oversized(right, max_size))
    return result


def chunk_text(text: str, chunk_size: int = 800) -> list[str]:
    lines = [l for l in text.strip().split("\n") if l.strip()]
    if not lines:
        return []

    chunks: list[str] = []
    start = 0

    for i, line in enumerate(lines):
        current_size = sum(len(l) + 1 for l in lines[start : i + 1])
        if current_size >= chunk_size and _is_heading(line):
            chunks.append("\n".join(lines[start:i]))
            start = i

    if start < len(lines):
        remaining = "\n".join(lines[start:])
        if chunks and len(remaining) < chunk_size // 3:
            chunks[-1] += "\n" + remaining
        else:
            chunks.append(remaining)

    result: list[str] = []
    for c in chunks:
        result.extend(_split_oversized(c))
    return result
