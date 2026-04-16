#!/usr/bin/env python3
import json
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR / "data"
SORTED_DIR = SCRIPT_DIR.parent.parent / "static" / "reviews" / "sorted"


def main():
    SORTED_DIR.mkdir(parents=True, exist_ok=True)

    # Find all app IDs from data files (pattern: {app_id}_{country}.json)
    app_ids = set()
    for f in DATA_DIR.glob("*.json"):
        match = re.match(r"^(\d+)_", f.name)
        if match:
            app_ids.add(match.group(1))

    total_files = 0
    total_reviews = 0

    for app_id in sorted(app_ids):
        all_reviews = []
        seen_ids = set()

        for f in DATA_DIR.glob(f"{app_id}_*.json"):
            reviews = json.loads(f.read_text())
            for r in reviews:
                rid = r.get("id")
                if rid and rid not in seen_ids:
                    seen_ids.add(rid)
                    all_reviews.append(r)

        all_reviews.sort(key=lambda r: r.get("date") or "", reverse=True)

        output_file = SORTED_DIR / f"{app_id}.json"
        output_file.write_text(json.dumps(all_reviews, indent=2, ensure_ascii=False))
        print(f"  {app_id} → {len(all_reviews)} reviews")
        total_files += 1
        total_reviews += len(all_reviews)

    print(f"\n=== Done ===")
    print(f"Total: {total_reviews} reviews in {total_files} files")


if __name__ == "__main__":
    main()
