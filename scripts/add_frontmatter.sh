#!/bin/bash

# Script to add minimal front matter to all .md files that don't have it
# This ensures Jekyll will process and convert all markdown files to HTML

echo "Adding front matter to markdown files without it..."

# Find all .md files (excluding _site, .git, and vendor directories)
find . \
  -type f \
  -name "*.md" \
  -not -path "./_site/*" \
  -not -path "./.git/*" \
  -not -path "./vendor/*" \
  -not -path "./node_modules/*" | while read -r file; do
  
  # Check if file starts with front matter (---)
  if ! head -c 3 "$file" | grep -q "^---"; then
    echo "Adding front matter to: $file"
    
    # Create temporary file with front matter prepended
    tmp_file="$(mktemp)"
    {
      printf -- "---\n---\n"
      cat "$file"
    } > "$tmp_file"

    # Replace original file
    mv "$tmp_file" "$file"
  else
    echo "Skipping $file (already has front matter)"
  fi
done

echo "Done!"
