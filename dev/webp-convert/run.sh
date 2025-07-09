#!/bin/bash

# Convert all images in the current directory and subdirectories to WebP
# while skipping the output directory and preserving folder structure

# Usage:
#   ./convert_to_webp.sh [WIDTH] [QUALITY]
# Example:
#   ./convert_to_webp.sh 800 90

WIDTH=${1:-1600}      # Default width: 1600px
QUALITY=${2:-90}     # Default quality: 90%

# Output directory
OUTDIR="webp_output"
mkdir -p "$OUTDIR"

# Supported image extensions (lowercase only)
EXTENSIONS="jpg jpeg png"

echo "Converting images to WebP format..."
echo "Target width: $WIDTH px"
echo "Quality: $QUALITY%"
echo "Output directory: $OUTDIR"

# Loop through supported extensions
for ext in $EXTENSIONS; do
  find . -type f -iname "*.$ext" ! -path "./$OUTDIR/*" | while read -r file; do
    relpath="${file#./}"                       # Remove leading ./
    outpath="$OUTDIR/${relpath%.*}.webp"       # Set output path
    mkdir -p "$(dirname "$outpath")"           # Create output directory
    cwebp -q "$QUALITY" -resize "$WIDTH" 0 "$file" -o "$outpath"
    echo "Converted: $file -> $outpath"
  done
done

echo "Done."