#!/usr/bin/env bash
#
# build-units.sh — build static/units/data.json with total download units per app.
#
# Step 1: pull the full app catalog for an App Store artist (developer) — apps
#         only, no in-app purchases.
# Step 2: sum the "Units" column from every CSV in itns_csv/ for those app IDs
#         and write the totals to static/units/data.json.
#
# Usage: ./build-units.sh [ARTIST_ID]   (default artist: EVERAPPZ SL)
#
set -euo pipefail

ARTIST_ID="${1:-1719367008}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CSV_DIR="$SCRIPT_DIR/itns_csv"
OUT_FILE="$SCRIPT_DIR/../../static/units/data.json"
CATALOG_URL="https://itunes.apple.com/lookup?id=${ARTIST_ID}&entity=software,macSoftware&limit=200&country=us"

# Step 1 — fetch the developer catalog.
CATALOG_JSON="$(mktemp)"
trap 'rm -f "$CATALOG_JSON"' EXIT
echo "Fetching catalog for artist ${ARTIST_ID}..."
curl -fsSL "$CATALOG_URL" -o "$CATALOG_JSON"

# Step 2 — sum units per catalog app ID and write the output JSON.
python3 - "$CATALOG_JSON" "$CSV_DIR" "$OUT_FILE" <<'PY'
import csv, glob, json, os, sys

catalog_path, csv_dir, out_file = sys.argv[1], sys.argv[2], sys.argv[3]

# Catalog app IDs (apps only — skip the artist record and in-app purchases).
with open(catalog_path, encoding="utf-8") as fh:
    results = json.load(fh).get("results", [])
app_ids = [
    str(r["trackId"]) for r in results
    if r.get("wrapperType") == "software" and r.get("kind") in ("software", "mac-software")
]
if not app_ids:
    sys.exit("No apps found in the developer catalog.")

# Sum units per app ID from every CSV.
totals = {aid: 0 for aid in app_ids}
allowed = set(app_ids)
files = sorted(glob.glob(os.path.join(csv_dir, "*.csv")))
if not files:
    sys.exit(f"No CSV files found in {csv_dir}")

for path in files:
    with open(path, encoding="utf-8-sig", newline="") as fh:  # utf-8-sig strips the BOM
        reader = csv.reader(fh)
        id_idx = units_idx = None
        for row in reader:
            if id_idx is None:
                if "Apple ID" in row and "Units" in row:
                    id_idx, units_idx = row.index("Apple ID"), row.index("Units")
                continue
            if len(row) <= max(id_idx, units_idx):
                continue
            aid = row[id_idx].strip()
            units = row[units_idx].replace(",", "").strip()
            if aid in allowed and units.lstrip("-").isdigit():
                totals[aid] += int(units)

ordered = dict(sorted(totals.items(), key=lambda kv: (-kv[1], kv[0])))

os.makedirs(os.path.dirname(out_file), exist_ok=True)
with open(out_file, "w", encoding="utf-8") as fh:
    json.dump(ordered, fh, indent=2)
    fh.write("\n")

print(f"Catalog apps: {len(app_ids)} | CSV files: {len(files)} | wrote {out_file}")
PY
