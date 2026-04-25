#!/bin/bash
set -e

echo "🧹 Cleaning public folder..."
rm -rf public

echo ""
echo "🚀 Starting Hugo server (writes to public/ automatically)..."
echo ""

# Start Hugo server in background (it writes to public/ by default)
hugo server --buildDrafts --disableFastRender --logLevel warn &
SERVER_PID=$!

# Progress indicator while waiting for build
echo -n "⏳ Building"
while [ ! -f "public/index.html" ]; do
  sleep 2
  if ! kill -0 $SERVER_PID 2>/dev/null; then
    echo ""
    echo "❌ Hugo server died. Check errors above."
    exit 1
  fi
  # Show file count as progress
  if [ -d "public" ]; then
    COUNT=$(find public -type f 2>/dev/null | wc -l | tr -d ' ')
    echo -ne "\r⏳ Building... ${COUNT} files generated"
  else
    echo -n "."
  fi
done

# Keep showing progress for a few more seconds while Hugo finishes writing
for i in 1 2 3 4 5; do
  sleep 2
  COUNT=$(find public -type f 2>/dev/null | wc -l | tr -d ' ')
  echo -ne "\r⏳ Building... ${COUNT} files generated"
done

echo ""
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

echo ""
echo "✅ Server running at http://localhost:1313/"
echo "   Press Ctrl+C to stop."
wait $SERVER_PID
