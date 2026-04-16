#!/bin/bash
cd "$(dirname "$0")"

# Ensure Python 3 is installed
if ! command -v python3 &>/dev/null; then
  echo "Python 3 not found, installing..."
  if command -v brew &>/dev/null; then
    brew install python3
  elif command -v apt-get &>/dev/null; then
    sudo apt-get update && sudo apt-get install -y python3
  elif command -v yum &>/dev/null; then
    sudo yum install -y python3
  else
    echo "Error: Cannot install Python 3 automatically. Please install it manually."
    exit 1
  fi
fi

rm -rf data
mkdir -p data
python3 fetch_reviews.py
python3 sort_reviews.py
