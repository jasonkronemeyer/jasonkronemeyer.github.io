#!/usr/bin/env python3
"""Write dir.html (never index.html) into each folder given on the command line.

Usage (from anywhere): python scripts/build_dir.py research notes papers
Folders are resolved relative to the repo root, not the working directory.
"""
import html
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKIP = {"index.md", "index.html", "dir.html"}
EXTENSIONS = {".md", ".html", ".pdf"}


def href_and_title(path: Path):
    # Jekyll converts .md to .html; other files are served as-is.
    if path.suffix == ".md":
        return path.stem + ".html", path.stem
    return path.name, path.stem


def build(folder: Path) -> str:
    files = sorted(
        p for p in folder.iterdir()
        if p.is_file() and p.suffix in EXTENSIONS and p.name not in SKIP
    )
    items = ""
    for p in files:
        href, stem = href_and_title(p)
        title = html.escape(stem.replace("-", " ").replace("_", " ").title())
        items += f'    <li><a href="{html.escape(href)}">{title}</a></li>\n'
    name = html.escape(folder.name.replace("-", " ").title())
    return f"""---
layout: null
---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{name} Index</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 2rem; line-height: 1.5; }}
    ul {{ padding-left: 1.2rem; }}
    li {{ margin: 0.3rem 0; }}
  </style>
</head>
<body>
  <h1>{name}</h1>
  <p>Auto-generated index.</p>
  <ul>
{items}  </ul>
</body>
</html>
"""


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    for arg in sys.argv[1:]:
        folder = (REPO / arg).resolve()
        if not folder.is_dir() or REPO not in folder.parents:
            print(f"Skipping {arg}: not a folder inside the repo")
            continue
        out = folder / "dir.html"
        out.write_text(build(folder), encoding="utf-8")
        print(f"Wrote {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
