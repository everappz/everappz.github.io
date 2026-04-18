---
title: "Export Wix Blog Posts to Markdown with OpenAI"
date: 2025-06-24
description: "Automate Wix blog export using Python, Selenium, and OpenAI. Extract dynamic content, download images, and convert HTML to clean Markdown for Hugo or Jekyll."
keywords: ["Wix blog export", "convert HTML to markdown", "OpenAI markdown conversion", "wix to markdown", "seo blog migration", "wix to hugo migration", "beautifulsoup scraper", "selenium render HTML", "OpenAI API automation", "migrate wix to static site", "wix blog scraper python"]
tags: ["wix", "markdown", "blog migration", "openai", "scraping", "beautifulsoup", "selenium", "automation", "SEO", "tutorial"]
draft: false
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Why Export Blog Posts from Wix?

**TL;DR:** This guide shows how to export Wix blog posts to Markdown using three Python scripts: a setup runner, a Selenium-based scraper, and an OpenAI-powered HTML-to-Markdown converter. The result is clean, portable Markdown files ready for Hugo, Jekyll, or any static site generator.

Wix does not offer a native blog export to Markdown. If you are migrating to a static site generator like Hugo or Jekyll, you need to scrape the rendered pages, extract the content, and convert it. This tutorial automates the entire process using **Python, Selenium, BeautifulSoup**, and **OpenAI's GPT API**.

The pipeline uses three scripts:

- `fetch_blog_posts.sh` — sets up the environment and runs the pipeline
- `parse_blog_sitemap.py` — renders pages with Selenium, extracts content, downloads images
- `generate_md.py` — converts HTML to Markdown via OpenAI

## Step 1: Set Up the Environment

Create `fetch_blog_posts.sh` to handle Python checks, virtual environment setup, dependency installation, and pipeline execution.

```bash
#!/bin/bash

# setup_blog_scraper.sh
# Usage: bash setup_blog_scraper.sh

echo "🔍 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

VENV_DIR=".venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "📁 Creating virtual environment in $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
else
    echo "✅ Virtual environment already exists."
fi

echo "⚙️ Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install beautifulsoup4 lxml selenium webdriver-manager

echo "🚀 Running blog sitemap parser..."
python3 parse_blog_sitemap.py

deactivate
```

## Step 2: Scrape and Extract Blog Content

`parse_blog_sitemap.py` does the heavy lifting:

1. Fetches the sitemap XML to discover all blog post URLs
2. Renders each page with **Selenium** (required because Wix content is dynamically loaded)
3. Extracts the `<div id="content-wrapper">` to isolate article content
4. Downloads all images locally and updates `src` attributes
5. Saves the cleaned HTML as `_index.html`
6. Calls the Markdown converter

**Why Selenium instead of requests?** Wix renders content with JavaScript. A simple HTTP request returns an empty shell. Selenium runs a headless Chrome browser to get the fully rendered HTML.

```python
#!/usr/bin/env python3
import os
import re
import time
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# === CONFIG ===
SITEMAP_URL = "https://www.everappz.com/blog-posts-sitemap.xml"
BASE_OUTPUT_DIR = "downloads"
GPT_CONVERTER_SCRIPT = "generate_md.py"

# === UTILITIES ===

def fetch_rendered_html(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    try:
        driver.get(url)
        time.sleep(3)
        return driver.page_source
    finally:
        driver.quit()

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\\\|?*]', '_', filename)

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
    from urllib.parse import urlparse
    soup = BeautifulSoup(content_html, "html.parser")

    for img in soup.find_all("img"):
        src = img.get("data-pin-media") or img.get("src")
        if src:
            try:
                parsed = urlparse(src)
                filename = os.path.basename(parsed.path)
                dest_path = os.path.join(folder, filename)
                print(f"📥 Downloading image: {src}")
                urllib.request.urlretrieve(src, dest_path)
                img["src"] = filename  # Update src to local path
            except Exception as e:
                print(f"⚠️ Failed to download image: {src} - {e}")
    return str(soup)
    
def parse_sitemap_and_process():
    os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)
    sitemap_xml = urllib.request.urlopen(SITEMAP_URL).read()
    root = ET.fromstring(sitemap_xml)

    url_elems = root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url")
    print(f"🔎 Total URLs found: {len(url_elems)}")

    for url_elem in url_elems:
        loc_elem = url_elem.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        if loc_elem is not None:
            page_url = loc_elem.text.strip()
            print(f"\n🔗 Processing: {page_url}")
            try:
                subpath = get_last_path_components(page_url)
                folder_path = os.path.join(BASE_OUTPUT_DIR, subpath)
                os.makedirs(folder_path, exist_ok=True)

                html = fetch_rendered_html(page_url)
                wrapper_html = extract_content_wrapper(html)

                if not wrapper_html:
                    print(f"❌ No <div id='content-wrapper'> found in {page_url}")
                    continue

                updated_html = update_image_sources(wrapper_html, folder_path)

                index_html_path = os.path.join(folder_path, "_index.html")
                with open(index_html_path, "w", encoding="utf-8") as f:
                    f.write(updated_html)
                print(f"✅ Saved: {index_html_path}")

                # Optional: call markdown converter
                os.system(f"python3 {GPT_CONVERTER_SCRIPT} \"{index_html_path}\"")

            except Exception as e:
                print(f"❌ Failed to process {page_url}: {e}")

if __name__ == "__main__":
    parse_sitemap_and_process()
```

## Step 3: Convert HTML to Markdown with OpenAI

`generate_md.py` reads each `_index.html` file, sends the content to OpenAI's Chat API, and writes the resulting Markdown.

```python
#!/usr/bin/env python3
import os
import sys
import json
import time
import random
import urllib.request
import urllib.error
from bs4 import BeautifulSoup

# === CONFIGURATION ===
API_MODEL = "gpt-4o"
API_KEY_FILE = "OPENAI_API_KEY.TXT"
DISABLE_API_REQUESTS = False

def read_openai_api_key():
    with open(API_KEY_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()

def call_openai_to_convert_to_markdown(html_content, api_key=None):
    if DISABLE_API_REQUESTS:
        return html_content

    if api_key is None:
        api_key = read_openai_api_key()

    time.sleep(round(random.uniform(1.0, 2.0), 2))

    system_prompt = (
        "You are a tool that converts HTML content from blog posts into well-structured Markdown (.md) format. "
        "Convert all visible text content and replace all <img> tags with Markdown image syntax using their local filenames. "
        "Retain the content hierarchy using proper markdown headers, and preserve paragraph structure. "
        "Make sure image alt attributes (if any) are preserved as the alt text in the markdown image syntax."
    )

    data = {
        "model": API_MODEL,
        "temperature": 0.3,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": html_content}
        ]
    }

    request = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(data).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )

    try:
        with urllib.request.urlopen(request) as response:
            result = json.load(response)
            markdown = result["choices"][0]["message"]["content"].strip()
            return markdown
    except Exception as e:
        print(f"❌ OpenAI API request failed: {e}")
        return ""

def extract_html_content(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    return soup.prettify()

def write_markdown_file(output_path, markdown_text):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_text)
    print(f"✅ Markdown saved to {output_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 generate_md.py path/to/_index.html")
        return

    html_file = sys.argv[1]
    if not os.path.exists(html_file):
        print(f"❌ File not found: {html_file}")
        return

    print(f"🔍 Converting HTML to Markdown: {html_file}")
    html_content = extract_html_content(html_file)
    markdown = call_openai_to_convert_to_markdown(html_content)
    if markdown:
        md_path = os.path.join(os.path.dirname(html_file), "_index.md")
        write_markdown_file(md_path, markdown)

if __name__ == "__main__":
    main()

```

## Output Folder Structure

After running the pipeline, each blog post gets its own folder:

```
downloads/
  your-post-title/
    _index.html      # Extracted and cleaned HTML
    _index.md         # Converted Markdown
    image1.png        # Downloaded images
    image2.png
```

## OpenAI API Key Setup

Save your API key in a file called `OPENAI_API_KEY.TXT` in the script directory:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Run the Full Pipeline

```bash
bash fetch_blog_posts.sh
```

This single command sets up the environment, scrapes all blog posts from the sitemap, downloads images, and converts everything to Markdown.

## Contribute to the Project

The project is open source. Bug reports, feature suggestions, and pull requests are welcome.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Project on GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Frequently Asked Questions

{{% details title="Why can't I just use `requests` to scrape Wix blog posts?" closed="true" %}}
Wix renders content dynamically with JavaScript. A standard HTTP request returns an empty page shell. Selenium runs a headless browser to get the fully rendered HTML.
{{% /details %}}

{{% details title="Does this work with any Wix blog?" closed="true" %}}
Yes. The scraper reads the blog sitemap XML and processes each URL. You only need to update the `SITEMAP_URL` variable in `parse_blog_sitemap.py` to point to your site's sitemap.
{{% /details %}}

{{% details title="Which OpenAI model does this use?" closed="true" %}}
The script uses GPT-4o by default. You can change the `API_MODEL` variable in `generate_md.py` to use a different model.
{{% /details %}}

{{% details title="Can I use this to migrate from Wix to Hugo?" closed="true" %}}
Yes. The output is standard Markdown with local image paths, which works directly with Hugo, Jekyll, Astro, and other static site generators. Add front matter to the generated `_index.md` files to complete the migration.
{{% /details %}}

{{% details title="How much does the OpenAI API cost for this?" closed="true" %}}
Cost depends on the number and length of your blog posts. A typical blog with 50 posts of moderate length costs a few dollars in API usage with GPT-4o.
{{% /details %}}

{{% details title="Is this tool open source?" closed="true" %}}
Yes. The full source code is available on [GitHub](https://github.com/everappz/wix-blog-export) under an open-source license.
{{% /details %}}
