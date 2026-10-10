#!/usr/bin/env python3
"""Generate index.md for research directory."""

from pathlib import Path
import re

root = Path(__file__).resolve().parent

# Get all markdown files (excluding index.md)
files = sorted(
    p.name
    for p in root.glob("*.md")
    if p.is_file() and p.name != "index.md"
)

# Build markdown index with links
markdown = """# Research

Auto-generated index of research articles and papers.

"""

for name in files:
    # Convert filename to title (remove dashes, capitalize words)
    title = name.replace(".md", "").replace("-", " ").title()
    markdown += f"- [{title}]({name})\n"

# Write to index.md
index_path = root / "index.md"
index_path.write_text(markdown, encoding="utf-8")
print(f"Generated {index_path}")
