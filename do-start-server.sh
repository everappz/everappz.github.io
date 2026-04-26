#!/bin/bash
set -e

PORT=${1:-1313}

echo ""
echo "🚀 Serving public/ on http://localhost:$PORT ..."
echo ""

# Open browser after a short delay to let the server start
(sleep 1 && open "http://localhost:$PORT") &

cd public && python3 -m http.server "$PORT"
