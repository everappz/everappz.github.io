#!/usr/bin/env python3
import json
import re
import time
import urllib.request
import urllib.error
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
APPS_FILE = SCRIPT_DIR / "apps.json"
DATA_DIR = SCRIPT_DIR / "data"
MAX_REVIEWS = 50
MAX_PAGES = 10  # RSS feed supports pages 1–10 (50 reviews per page)
DELAY_BETWEEN_PAGES = 1.0
DELAY_BETWEEN_COUNTRIES = 0.5

# All App Store country codes
COUNTRIES = [
    "dz", "ao", "ai", "ag", "ar", "am", "au", "at", "az", "bh",
    "bb", "by", "be", "bz", "bj", "bm", "bt", "bo", "bw", "br",
    "vg", "bn", "bg", "bf", "kh", "cm", "ca", "cv", "ky", "td",
    "cl", "cn", "co", "cg", "cr", "ci", "hr", "cy", "cz", "dk",
    "dm", "do", "ec", "eg", "sv", "ee", "sz", "fj", "fi", "fr",
    "ga", "gm", "ge", "de", "gh", "gr", "gd", "gt", "gw", "gy",
    "hn", "hk", "hu", "is", "in", "id", "iq", "ie", "il", "it",
    "jm", "jp", "jo", "kz", "ke", "kr", "kw", "kg", "la", "lv",
    "lb", "lr", "ly", "lt", "lu", "mo", "mg", "mw", "my", "mv",
    "ml", "mt", "mr", "mu", "mx", "fm", "md", "mn", "me", "ms",
    "ma", "mz", "mm", "na", "nr", "np", "nl", "nz", "ni", "ne",
    "ng", "mk", "no", "om", "pk", "pw", "pa", "pg", "py", "pe",
    "ph", "pl", "pt", "qa", "ro", "ru", "rw", "kn", "lc", "vc",
    "st", "sa", "sn", "rs", "sc", "sl", "sg", "sk", "si", "sb",
    "za", "es", "lk", "sr", "se", "ch", "tw", "tj", "tz", "th",
    "tn", "tr", "tm", "tc", "ug", "ua", "ae", "gb", "us", "uy",
    "uz", "ve", "vn", "ye", "zm", "zw",
]

BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


# --- Method 1: RSS feed ---

def fetch_rss_page(app_id, country, page):
    url = (f"https://itunes.apple.com/{country}/rss/customerreviews"
           f"/page={page}/id={app_id}/sortby=mostrecent/json")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        entries = data.get("feed", {}).get("entry", [])
        if not isinstance(entries, list):
            entries = [entries]
        return [e for e in entries if "im:rating" in e]
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError):
        return []


def parse_rss_review(entry, country):
    try:
        return {
            "country": country,
            "id": entry.get("id", {}).get("label"),
            "author": entry.get("author", {}).get("name", {}).get("label"),
            "rating": int(entry.get("im:rating", {}).get("label", 0)),
            "title": entry.get("title", {}).get("label"),
            "content": entry.get("content", {}).get("label"),
            "date": entry.get("updated", {}).get("label"),
            "version": entry.get("im:version", {}).get("label"),
        }
    except (ValueError, AttributeError):
        return None


def fetch_rss_reviews(app_id, country, max_reviews):
    reviews = []
    for page in range(1, MAX_PAGES + 1):
        if len(reviews) >= max_reviews:
            break
        entries = fetch_rss_page(app_id, country, page)
        if not entries:
            break
        added = 0
        for entry in entries:
            review = parse_rss_review(entry, country)
            if review and review["id"]:
                reviews.append(review)
                added += 1
                if len(reviews) >= max_reviews:
                    break
        if added == 0:
            break
        time.sleep(DELAY_BETWEEN_PAGES)
    return reviews


# --- Method 2: HTML scraping (see-all=reviews page) ---

def fetch_html_reviews(app_id, country):
    url = f"https://apps.apple.com/{country}/app/id{app_id}?see-all=reviews"
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": BROWSER_UA,
            "Accept-Language": "en-US,en;q=0.9",
        })
        html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError):
        return []

    scripts = re.findall(r"<script[^>]*>(.*?)</script>", html, re.DOTALL)
    ssr_data = None
    for s in scripts:
        if len(s) < 5000:
            continue
        try:
            ssr_data = json.loads(s)
            break
        except (json.JSONDecodeError, ValueError):
            continue

    if not ssr_data:
        return []

    reviews = []
    try:
        shelf = ssr_data["data"][0]["data"]["shelfMapping"]
        for key in ("allProductReviews", "userProductReviews"):
            items = shelf.get(key, {}).get("items", [])
            for item in items:
                r = item.get("review", {})
                rid = r.get("id")
                if not rid:
                    continue
                reviews.append({
                    "country": country,
                    "id": str(rid),
                    "author": r.get("reviewerName", ""),
                    "rating": r.get("rating"),
                    "title": r.get("title", ""),
                    "content": r.get("contents", ""),
                    "date": r.get("date", ""),
                    "version": None,
                })
    except (KeyError, IndexError, TypeError):
        pass

    return reviews


# --- Merge and deduplicate ---

def fetch_all_reviews(app_id, country, max_reviews):
    rss_reviews = fetch_rss_reviews(app_id, country, max_reviews)

    time.sleep(DELAY_BETWEEN_PAGES)
    html_reviews = fetch_html_reviews(app_id, country)

    seen_ids = set()
    merged = []
    for review in rss_reviews + html_reviews:
        if review["id"] not in seen_ids:
            seen_ids.add(review["id"])
            merged.append(review)

    return merged


def main():
    apps = json.loads(APPS_FILE.read_text())
    DATA_DIR.mkdir(exist_ok=True)

    total_files = 0
    total_reviews = 0

    for app_name, app_id in apps.items():
        for country in COUNTRIES:
            print(f"  {app_name} (id={app_id}) [{country}] ", end="", flush=True)
            reviews = fetch_all_reviews(app_id, country, MAX_REVIEWS)

            if reviews:
                output_file = DATA_DIR / f"{app_id}_{country}.json"
                output_file.write_text(json.dumps(reviews, indent=2, ensure_ascii=False))
                print(f"→ {len(reviews)} reviews")
                total_files += 1
                total_reviews += len(reviews)
            else:
                print(f"→ 0, skipping")

            time.sleep(DELAY_BETWEEN_COUNTRIES)

    print(f"\n=== Done ===")
    print(f"Total: {total_reviews} reviews in {total_files} files")


if __name__ == "__main__":
    main()
