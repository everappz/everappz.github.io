#!/bin/bash
# convert_to_webp.sh
# Usage: ./convert_to_webp.sh [WIDTH] [QUALITY]
# Example: ./convert_to_webp.sh 800 90

set -euo pipefail

WIDTH=${1:-1600}   # Max width in pixels
QUALITY=${2:-90}   # WebP quality %

OUTDIR="webp_output"
mkdir -p "$OUTDIR"

EXTENSIONS="jpg jpeg png"

echo "Converting images to WebP ..."
echo "- Max width      : $WIDTH px"
echo "- Quality        : $QUALITY%"
echo "- Output folder  : $OUTDIR"
echo

for ext in $EXTENSIONS; do
  find . -type f -iname "*.$ext" ! -path "./$OUTDIR/*" | while read -r file; do
    # Strip leading "./"
    relpath="${file#./}"
    outpath="$OUTDIR/${relpath%.*}.webp"

    # Create output directory if needed
    mkdir -p "$(dirname "$outpath")"

    # Get original pixel width
    orig_w=$(identify -format "%w" "$file" 2>/dev/null || echo 0)

    if [[ "$orig_w" -gt "$WIDTH" ]]; then
      # Resize because original width is larger than target
      cwebp -q "$QUALITY" -resize "$WIDTH" 0 "$file" -o "$outpath"
      echo "Resized & converted: $file  (${orig_w}px → ${WIDTH}px)"
    else
      # Keep original size (no -resize flag)
      cwebp -q "$QUALITY" "$file" -o "$outpath"
      echo "Converted (kept size): $file  (${orig_w}px)"
    fi
  done
done

echo
echo "Done."