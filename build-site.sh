#!/bin/bash
set -e

# Kill all existing Hugo processes
if pgrep -f hugo > /dev/null 2>&1; then
  echo "🛑 Killing all Hugo processes..."
  pkill -9 -f hugo 2>/dev/null
  sleep 1
fi

# echo "🧹 Clearing Hugo caches..."
# rm -rf resources/_gen
# hugo --gc > /dev/null 2>&1 || true

echo ""
echo "🔍 Checking for aliases in localized pages..."
BAD_FILES=()
while IFS= read -r f; do
  # Match localized pages: any .XX.md or .xx-xx.md (2-letter or 2-letter-2-letter lang code before .md)
  [[ "$f" =~ \.[a-z]{2}(-[a-z]{2})?\.md$ ]] || continue
  if grep -q '^aliases:' "$f" 2>/dev/null; then
    BAD_FILES+=("$f")
  fi
done < <(find content -name '*.md' -type f)

if [ ${#BAD_FILES[@]} -gt 0 ]; then
  echo "❌ Found aliases in localized pages (aliases must be removed from translations):"
  for bf in "${BAD_FILES[@]}"; do
    echo "   $bf"
  done
  exit 1
fi
echo "   ✓ No aliases found in localized pages"

echo ""
echo "🧹 Cleaning public folder..."
rm -rf public

echo ""
echo "🔨 Building site..."
hugo --buildDrafts --logLevel warn

echo ""
echo "📊 Build Stats"
echo "─────────────────────────────"
echo "Total files: $(find public -type f | wc -l | tr -d ' ')"
echo "Total size:  $(du -sh public | cut -f1)"
echo ""
echo "Files by top-level folder:"
for dir in public/*/; do
  count=$(find "$dir" -type f 2>/dev/null | wc -l | tr -d ' ')
  printf "  %-30s %s\n" "$(basename "$dir")" "$count"
done