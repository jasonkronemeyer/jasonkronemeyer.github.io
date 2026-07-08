from pathlib import Path

root = Path(__file__).resolve().parent

files = sorted(
    p.name
    for p in root.iterdir()
    if p.is_file() and p.name not in {"build_index.py", "index.html"}
)

html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Notes Index</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 2rem; line-height: 1.5; }
    ul { padding-left: 1.2rem; }
    li { margin: 0.3rem 0; }
  </style>
</head>
<body>
  <h1>Notes Index</h1>
  <p>Auto-generated list of files in this folder.</p>
  <ul>
"""

for name in files:
    href = name
    if href.endswith(".md"):
        href = href[:-3] + ".html"
    html += f'    <li><a href="{href}">{name}</a></li>\n'

html += """  </ul>
</body>
</html>
"""

Path("index.html").write_text(html, encoding="utf-8")
print("Generated index.html")