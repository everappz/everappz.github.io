#!/bin/bash
set -e

echo "🧹 Cleaning public folder..."
rm -rf public

echo ""
echo "🚀 Starting Hugo server (writes to public/ automatically)..."
echo "   Build will take 30s–2min for 22k files."
echo ""

# Start Hugo server in background (it writes to public/ by default)
hugo server --buildDrafts --disableFastRender --logLevel warn &
SERVER_PID=$!

# Wait for index.html to appear (signals build is done)
echo "⏳ Waiting for initial build..."
while [ ! -f "public/index.html" ]; do
  sleep 1
  if ! kill -0 $SERVER_PID 2>/dev/null; then
    echo "❌ Hugo server died. Check errors above."
    exit 1
  fi
done

# Give Hugo a few more seconds to finish writing everything
sleep 5

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