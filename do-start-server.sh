#!/bin/bash
set -e

PORT=${1:-1313}

echo ""
echo "🚀 Serving public/ on http://localhost:$PORT ..."
echo ""
cd public && python3 -m http.server "$PORT"
