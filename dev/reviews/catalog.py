#!/usr/bin/env python3
"""
Load the developer's App Store catalog (apps only — no in-app purchases) from
the iTunes Lookup API, so review scripts don't need a hardcoded apps.json.

Usage:
    from catalog import load_apps
    apps = load_apps()            # {app_id: app_name}
"""
import json
import sys
import urllib.request

# EVERAPPZ SL. Override by passing an artist id to load_apps().
ARTIST_ID = "1719367008"


def load_apps(artist_id=ARTIST_ID):
    """Return {app_id (str): app_name} for every app in the developer catalog."""
    url = (f"https://itunes.apple.com/lookup?id={artist_id}"
           f"&entity=software,macSoftware&limit=200&country=us")
    with urllib.request.urlopen(url, timeout=30) as resp:
        results = json.loads(resp.read()).get("results", [])
    apps = {}
    for r in results:
        if r.get("wrapperType") == "software" and r.get("kind") in ("software", "mac-software"):
            apps[str(r["trackId"])] = r.get("trackName", str(r["trackId"]))
    if not apps:
        sys.exit(f"No apps found for artist {artist_id}")
    return apps


if __name__ == "__main__":
    for app_id, name in load_apps(*sys.argv[1:2]).items():
        print(f"{app_id}\t{name}")
