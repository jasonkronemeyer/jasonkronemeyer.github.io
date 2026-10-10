#!/usr/bin/env python3
"""Generate dir.html for research directory."""

from pathlib import Path

root = Path(__file__).resolve().parent

# Get all markdown files (excluding index.md)
files = sorted(
    p.name
    for p in root.glob("*.md")
    if p.is_file() and p.name != "index.md"
)

# Build HTML index with links
html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Research Index</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 2rem; line-height: 1.5; }
    ul { padding-left: 1.2rem; }
    li { margin: 0.3rem 0; }
  </style>
</head>
<body>
  <h1>Research</h1>
  <p>Auto-generated index of research articles and papers.</p>
  <ul>
"""

for name in files:
    # Convert filename to title (remove extension, replace dashes with spaces, title case)
    title = name.replace(".md", "").replace("-", " ").title()
    # Link to the markdown file (or .html if it's converted)
    href = name.replace(".md", ".html")
    html += f'    <li><a href="{href}">{title}</a></li>\n'

html += """  </ul>
</body>
</html>
"""

# Write to dir.html
output_path = root / "dir.html"
output_path.write_text(html, encoding="utf-8")
print(f"Generated {output_path}")
