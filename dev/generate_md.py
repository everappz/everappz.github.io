#!/usr/bin/env python3
import os
import re
import time
import shutil
import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# === CONFIG ===
SITEMAP_URL = "https://www.everappz.com/blog-posts-sitemap.xml"
BASE_OUTPUT_DIR = "downloads"
GPT_CONVERTER_SCRIPT = "generate_md.py"  # External script that converts _index.html to _index.md

# === UTILITIES ===

def fetch_url(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def get_last_path_components(url, levels=2):
    parts = urlparse(url).path.strip("/").split("/")
    return os.path.join(*parts[-levels:])

def download_image(img_url, dest_folder):
    try:
        parsed = urlparse(img_url)
        filename = os.path.basename(parsed.path)
        dest_path = os.path.join(dest_folder, filename)
        print(f"📥 Downloading image: {img_url}")
        urllib.request.urlretrieve(img_url, dest_path)
        return filename
    except Exception as e:
        print(f"⚠️ Failed to download image: {img_url} - {e}")
        return None

def extract_content_wrapper(html):
    soup = BeautifulSoup(html, "html.parser")
    wrapper = soup.find("div", id="content-wrapper")
    return str(wrapper) if wrapper else ""

def update_image_sources(content_html, folder):
    soup = BeautifulSoup(content_html, "html.parser")
    for img in soup.find_all("img"):
        src = img.get("src")
        if src:
            filename = download_image(src, folder)
            if filename:
                img["src"] = filename
    return str(soup)

def parse_sitemap_and_process():
    os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)
    sitemap_xml = fetch_url(SITEMAP_URL)
    root = ET.fromstring(sitemap_xml)
    ns = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    for url_elem in root.findall("ns:url", ns):
        loc_elem = url_elem.find("ns:loc", ns)
        if loc_elem is not None:
            page_url = loc_elem.text.strip()
            print(f"\n🔗 Processing: {page_url}")

            try:
                # Build output folder
                subpath = get_last_path_components(page_url)
                folder_path = os.path.join(BASE_OUTPUT_DIR, subpath)
                os.makedirs(folder_path, exist_ok=True)

                # Download and extract content
                page_html = fetch_url(page_url).decode("utf-8")
                wrapper_html = extract_content_wrapper(page_html)

                if not wrapper_html:
                    print(f"❌ No <div id='content-wrapper'> found in {page_url}")
                    continue

                updated_html = update_image_sources(wrapper_html, folder_path)

                # Write to _index.html
                index_html_path = os.path.join(folder_path, "_index.html")
                with open(index_html_path, "w", encoding="utf-8") as f:
                    f.write(updated_html)
                print(f"✅ Saved: {index_html_path}")

                # Call external GPT Markdown converter
                print(f"⚙️  Converting to markdown using: {GPT_CONVERTER_SCRIPT}")
                os.system(f"python3 {GPT_CONVERTER_SCRIPT} \"{index_html_path}\"")

            except Exception as e:
                print(f"❌ Failed to process {page_url}: {e}")

if __name__ == "__main__":
    parse_sitemap_and_process()