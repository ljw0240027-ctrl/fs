from __future__ import annotations

from pathlib import Path


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_text_utf8(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")
