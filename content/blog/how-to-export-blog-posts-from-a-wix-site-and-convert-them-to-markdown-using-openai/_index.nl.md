---
title: "Wix Blogberichten Exporteren naar Markdown met OpenAI"
date: 2025-06-24
description: "Automatiseer Wix blogexport met Python, Selenium en OpenAI. Extraheer dynamische inhoud, download afbeeldingen en converteer HTML naar schone Markdown voor Hugo of Jekyll."
keywords: ["Wix blog export", "HTML naar markdown converteren", "OpenAI markdown conversie", "wix naar markdown", "SEO blogmigratie", "wix naar hugo migratie", "beautifulsoup scraper", "selenium HTML renderen", "OpenAI API automatisering", "wix naar statische site migreren", "wix blog scraper python"]
tags: ["wix", "markdown", "blogmigratie", "openai", "scraping", "beautifulsoup", "selenium", "automatisering", "SEO", "tutorial"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Waarom Blogberichten Exporteren vanuit Wix?

**Samenvatting:** Deze gids laat zien hoe u Wix blogberichten exporteert naar Markdown met drie Python-scripts: een setup-runner, een op Selenium gebaseerde scraper en een OpenAI-aangedreven HTML-naar-Markdown converter. Het resultaat zijn schone, draagbare Markdown-bestanden klaar voor Hugo, Jekyll of elke andere statische sitegenerator.

Wix biedt geen native blogexport naar Markdown. Als u migreert naar een statische sitegenerator zoals Hugo of Jekyll, moet u de gerenderde pagina's scrapen, de inhoud extraheren en converteren. Deze tutorial automatiseert het hele proces met **Python, Selenium, BeautifulSoup** en **OpenAI's GPT API**.

De pipeline gebruikt drie scripts:

- `fetch_blog_posts.sh` — stelt de omgeving in en voert de pipeline uit
- `parse_blog_sitemap.py` — rendert pagina's met Selenium, extraheert inhoud, downloadt afbeeldingen
- `generate_md.py` — converteert HTML naar Markdown via OpenAI

## Stap 1: De Omgeving Opzetten

Maak `fetch_blog_posts.sh` aan om Python-controles, virtuele omgeving setup, afhankelijkheden installatie en pipeline-uitvoering af te handelen.

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

## Stap 2: Bloginhoud Scrapen en Extraheren

`parse_blog_sitemap.py` doet het zware werk:

1. Haalt de sitemap XML op om alle blogpost-URL's te ontdekken
2. Rendert elke pagina met **Selenium** (nodig omdat Wix-inhoud dynamisch geladen wordt)
3. Extraheert de `<div id="content-wrapper">` om artikelinhoud te isoleren
4. Downloadt alle afbeeldingen lokaal en werkt `src`-attributen bij
5. Slaat de opgeschoonde HTML op als `_index.html`
6. Roept de Markdown-converter aan

**Waarom Selenium in plaats van requests?** Wix rendert inhoud met JavaScript. Een eenvoudige HTTP-aanvraag geeft een lege paginahuls terug. Selenium draait een headless Chrome-browser om de volledig gerenderde HTML te krijgen.

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

## Stap 3: HTML naar Markdown Converteren met OpenAI

`generate_md.py` leest elk `_index.html`-bestand, stuurt de inhoud naar OpenAI's Chat API en schrijft de resulterende Markdown.

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

## Uitvoermapstructuur

Na het uitvoeren van de pipeline krijgt elk blogbericht zijn eigen map:

```
downloads/
  your-post-title/
    _index.html      # Geëxtraheerde en opgeschoonde HTML
    _index.md         # Geconverteerde Markdown
    image1.png        # Gedownloade afbeeldingen
    image2.png
```

## OpenAI API-sleutel Instellen

Sla uw API-sleutel op in een bestand genaamd `OPENAI_API_KEY.TXT` in de scriptmap:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## De Volledige Pipeline Uitvoeren

```bash
bash fetch_blog_posts.sh
```

Dit enkele commando stelt de omgeving in, scrapt alle blogberichten van de sitemap, downloadt afbeeldingen en converteert alles naar Markdown.

## Bijdragen aan het Project

Het project is open source. Bugrapporten, functiesuggesties en pull requests zijn welkom.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Project op GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Veelgestelde Vragen

{{% details title="Waarom kan ik niet gewoon `requests` gebruiken om Wix blogberichten te scrapen?" closed="true" %}}
Wix rendert inhoud dynamisch met JavaScript. Een standaard HTTP-aanvraag geeft een lege paginahuls terug. Selenium draait een headless browser om de volledig gerenderde HTML te krijgen.
{{% /details %}}

{{% details title="Werkt dit met elke Wix blog?" closed="true" %}}
Ja. De scraper leest de blog sitemap XML en verwerkt elke URL. U hoeft alleen de `SITEMAP_URL`-variabele in `parse_blog_sitemap.py` bij te werken om naar de sitemap van uw site te verwijzen.
{{% /details %}}

{{% details title="Welk OpenAI-model gebruikt dit?" closed="true" %}}
Het script gebruikt standaard GPT-4o. U kunt de `API_MODEL`-variabele in `generate_md.py` wijzigen om een ander model te gebruiken.
{{% /details %}}

{{% details title="Kan ik dit gebruiken om van Wix naar Hugo te migreren?" closed="true" %}}
Ja. De uitvoer is standaard Markdown met lokale afbeeldingspaden, wat direct werkt met Hugo, Jekyll, Astro en andere statische sitegeneratoren. Voeg front matter toe aan de gegenereerde `_index.md`-bestanden om de migratie te voltooien.
{{% /details %}}

{{% details title="Hoeveel kost de OpenAI API hiervoor?" closed="true" %}}
De kosten hangen af van het aantal en de lengte van uw blogberichten. Een typische blog met 50 berichten van gemiddelde lengte kost een paar dollar aan API-gebruik met GPT-4o.
{{% /details %}}

{{% details title="Is deze tool open source?" closed="true" %}}
Ja. De volledige broncode is beschikbaar op [GitHub](https://github.com/everappz/wix-blog-export) onder een open-source licentie.
{{% /details %}}
