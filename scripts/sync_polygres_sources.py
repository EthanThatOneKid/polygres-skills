#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path

DEFAULT_BASE_URL = "https://docs.evokoa.com/polygres"
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parents[1] / "references" / "upstream" / "pages"
DEFAULT_MANIFEST = Path(__file__).resolve().parents[1] / "references" / "upstream" / "manifest.json"
USER_AGENT = "Mozilla/5.0 (compatible; polygres-skills-sync/1.0)"


@dataclass(frozen=True)
class Page:
    url: str
    title: str
    body: str
    source_hash: str
    discovered_from: str


@dataclass(frozen=True)
class Skip:
    url: str
    reason: str


def fetch(url: str, timeout: int = 60) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = response.read()
        charset = response.headers.get_content_charset() or "utf-8"
        return data.decode(charset, errors="replace")


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def source_to_relative_path(source_url: str) -> Path:
    parsed = urllib.parse.urlparse(source_url)
    path = parsed.path.strip("/")
    if not path:
        path = "polygres/index"
    elif path == "polygres":
        path = "polygres/index"
    elif path.endswith("/"):
        path = f"{path}index"
    if path.endswith(".html"):
        path = path[:-5]
    if path.endswith(".md"):
        path = path[:-3]
    return Path(f"{path}.md")


def extract_urls_from_html(html_text: str, page_url: str) -> list[str]:
    urls: list[str] = []
    for candidate in re.findall(r'''(?:href|data-href)=['\"]([^'\"]+)['\"]''', html_text, flags=re.IGNORECASE):
        absolute = urllib.parse.urljoin(page_url, candidate)
        absolute = urllib.parse.urldefrag(absolute).url
        parsed = urllib.parse.urlparse(absolute)
        if parsed.netloc not in {"docs.evokoa.com", "evokoa.com"}:
            continue
        if not parsed.path.startswith("/polygres"):
            continue
        if parsed.path.startswith("/polygres/_next/") or parsed.path.startswith("/polygres/images/"):
            continue
        if Path(parsed.path).suffix:
            continue
        urls.append(absolute)
    deduped: list[str] = []
    for url in urls:
        if url not in deduped:
            deduped.append(url)
    return deduped


def extract_urls_from_sitemap(xml_text: str) -> list[str]:
    urls = re.findall(r"<loc>(.*?)</loc>", xml_text, flags=re.IGNORECASE | re.DOTALL)
    return [html.unescape(url.strip()) for url in urls if url.strip()]


def extract_urls_from_llms(text: str) -> list[str]:
    urls: list[str] = []
    for match in re.findall(r"\((https?://[^)]+)\)", text):
        urls.append(match.strip())
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("http://") or line.startswith("https://"):
            urls.append(line)
    deduped: list[str] = []
    for url in urls:
        if url not in deduped:
            deduped.append(url)
    return deduped


def html_to_text(html_text: str) -> tuple[str, str]:
    title_match = re.search(r"<title>(.*?)</title>", html_text, flags=re.IGNORECASE | re.DOTALL)
    title = normalize_whitespace(html.unescape(title_match.group(1))) if title_match else ""

    body_match = re.search(r"<main[^>]*>(.*?)</main>", html_text, flags=re.IGNORECASE | re.DOTALL)
    body = body_match.group(1) if body_match else html_text
    body = re.sub(r"(?is)<(script|style|noscript|svg|iframe|canvas|meta|link)[^>]*>.*?</\1>", " ", body)
    body = re.sub(r"(?is)<br\s*/?>", "\n", body)
    body = re.sub(r"(?is)</(p|div|section|article|main|header|footer|li|h[1-6]|tr|table|ul|ol|aside|nav)>", "\n", body)
    body = re.sub(r"(?is)<[^>]+>", " ", body)
    body = html.unescape(body)

    blocks: list[str] = []
    for line in body.splitlines():
        line = normalize_whitespace(line)
        if line:
            blocks.append(line)

    return title, "\n\n".join(blocks)


def try_fetch_discovery_urls(base_url: str) -> list[str]:
    discovered: list[str] = []
    for suffix in ("/sitemap.xml", "/llms.txt", "/llms-full.txt"):
        candidate = f"{base_url}{suffix}"
        try:
            text = fetch(candidate)
        except urllib.error.HTTPError:
            continue
        except Exception:
            continue

        if suffix.endswith("sitemap.xml"):
            discovered.extend(extract_urls_from_sitemap(text))
        else:
            discovered.extend(extract_urls_from_llms(text))

    deduped: list[str] = []
    for url in discovered:
        if url not in deduped:
            deduped.append(url)
    return deduped


def crawl(base_url: str) -> tuple[list[Page], list[Skip]]:
    queue: list[tuple[str, str]] = [(base_url, base_url)]
    queue.extend((url, base_url) for url in try_fetch_discovery_urls(base_url))

    seen: set[str] = set()
    pages: list[Page] = []
    skips: list[Skip] = []

    while queue:
        url, discovered_from = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)

        try:
            html_text = fetch(url)
        except urllib.error.HTTPError as exc:
            skips.append(Skip(url, f"http {exc.code}"))
            continue
        except Exception as exc:  # noqa: BLE001
            skips.append(Skip(url, f"fetch failed: {exc}"))
            continue

        title, body = html_to_text(html_text)
        if not body:
            skips.append(Skip(url, "empty text"))
            continue

        source_hash = content_hash(html_text)
        pages.append(
            Page(
                url=url,
                title=title or url,
                body=body,
                source_hash=source_hash,
                discovered_from=discovered_from,
            )
        )

        for next_url in extract_urls_from_html(html_text, url):
            if next_url not in seen:
                queue.append((next_url, url))

    return pages, skips


def write_page(output_dir: Path, page: Page) -> Path:
    relative_path = source_to_relative_path(page.url)
    output_path = output_dir / relative_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    content = [
        f"source: {page.url}",
        f"title: {page.title}",
        f"source_hash: {page.source_hash}",
        f"discovered_from: {page.discovered_from}",
        "",
        f"# {page.title}",
        "",
        page.body,
        "",
    ]
    output_path.write_text("\n".join(content), encoding="utf-8")
    return relative_path


def prune_stale_files(output_dir: Path, active_paths: set[Path], manifest_path: Path) -> list[Path]:
    removed: list[Path] = []
    if not output_dir.exists():
        return removed

    manifest_resolved = manifest_path.resolve()
    for path in sorted(output_dir.rglob("*.md")):
        if path.relative_to(output_dir) not in active_paths and path.resolve() != manifest_resolved:
            path.unlink()
            removed.append(path)

    for directory in sorted((path for path in output_dir.rglob("*") if path.is_dir()), reverse=True):
        if not any(directory.iterdir()):
            directory.rmdir()

    return removed


def build_manifest(base_url: str, pages: list[Page], skips: list[Skip], output_dir: Path) -> dict:
    items = []
    for page in pages:
        relative_path = source_to_relative_path(page.url)
        items.append(
            {
                "url": page.url,
                "title": page.title,
                "path": str(relative_path).replace("\\", "/"),
                "sha256": page.source_hash,
                "discovered_from": page.discovered_from,
            }
        )

    return {
        "source": {"base_url": base_url},
        "output_dir": str(output_dir).replace("\\", "/"),
        "count": len(items),
        "skip_count": len(skips),
        "items": items,
        "skips": [{"url": skip.url, "reason": skip.reason} for skip in skips],
    }


def sync(args: argparse.Namespace) -> int:
    output_dir = Path(args.output_dir)
    manifest_path = Path(args.manifest)

    pages, skips = crawl(args.base_url)
    if not pages:
        print("No pages collected.", file=sys.stderr)
        return 1

    manifest = build_manifest(args.base_url, pages, skips, output_dir)

    if args.dry_run:
        print(json.dumps(manifest, indent=2))
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)
    written_paths: set[Path] = set()
    for page in pages:
        written_paths.add(write_page(output_dir, page))

    removed = prune_stale_files(output_dir, written_paths, manifest_path)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {len(written_paths)} markdown files to {output_dir}")
    if removed:
        print(f"Removed {len(removed)} stale markdown files")
    if skips:
        print(f"Skipped {len(skips)} pages", file=sys.stderr)
    print(f"Manifest: {manifest_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Polygres public markdown sources.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    return sync(args)


if __name__ == "__main__":
    raise SystemExit(main())
