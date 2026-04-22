---
title: "Eksporter Wix-blogginnlegg til Markdown med OpenAI"
date: 2025-06-24
description: "Automatiser Wix-bloggeksport med Python, Selenium og OpenAI. Ekstraher dynamisk innhold, last ned bilder og konverter HTML til ren Markdown for Hugo eller Jekyll."
keywords: ["Wix blogg eksport", "konverter HTML til markdown", "OpenAI markdown konvertering", "wix til markdown", "SEO bloggmigrering", "wix til hugo migrering", "beautifulsoup scraper", "selenium render HTML", "OpenAI API automatisering", "migrer wix til statisk side", "wix blogg scraper python"]
tags: ["wix", "markdown", "bloggmigrering", "openai", "scraping", "beautifulsoup", "selenium", "automatisering", "SEO", "veiledning"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Hvorfor Eksportere Blogginnlegg fra Wix?

**Sammendrag:** Denne guiden viser hvordan du eksporterer Wix-blogginnlegg til Markdown ved hjelp av tre Python-skript: en oppsettskjører, en Selenium-basert scraper og en OpenAI-drevet HTML-til-Markdown-konverterer. Resultatet er rene, bærbare Markdown-filer klare for Hugo, Jekyll eller hvilken som helst statisk sidegenerator.

Wix tilbyr ikke en native bloggeksport til Markdown. Hvis du migrerer til en statisk sidegenerator som Hugo eller Jekyll, må du scrape de rendrede sidene, ekstrahere innholdet og konvertere det. Denne veiledningen automatiserer hele prosessen med **Python, Selenium, BeautifulSoup** og **OpenAIs GPT API**.

Pipelinen bruker tre skript:

- `fetch_blog_posts.sh` — setter opp miljøet og kjører pipelinen
- `parse_blog_sitemap.py` — rendrer sider med Selenium, ekstraherer innhold, laster ned bilder
- `generate_md.py` — konverterer HTML til Markdown via OpenAI

## Trinn 1: Sett Opp Miljøet

Opprett `fetch_blog_posts.sh` for å håndtere Python-sjekker, oppsett av virtuelt miljø, installasjon av avhengigheter og kjøring av pipelinen.

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

## Trinn 2: Scrap og Ekstraher Blogginnhold

`parse_blog_sitemap.py` gjør det tunge arbeidet:

1. Henter sitemap-XML for å oppdage alle bloggpost-URL-er
2. Rendrer hver side med **Selenium** (nødvendig fordi Wix-innhold lastes dynamisk)
3. Ekstraherer `<div id="content-wrapper">` for å isolere artikkelinnhold
4. Laster ned alle bilder lokalt og oppdaterer `src`-attributter
5. Lagrer den rensede HTML-en som `_index.html`
6. Kaller Markdown-konvertereren

**Hvorfor Selenium i stedet for requests?** Wix rendrer innhold med JavaScript. En enkel HTTP-forespørsel returnerer et tomt sideskall. Selenium kjører en headless Chrome-nettleser for å få den fullstendig rendrede HTML-en.

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

## Trinn 3: Konverter HTML til Markdown med OpenAI

`generate_md.py` leser hver `_index.html`-fil, sender innholdet til OpenAIs Chat API og skriver den resulterende Markdown-en.

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

## Utdatamappestruktur

Etter å ha kjørt pipelinen får hvert blogginnlegg sin egen mappe:

```
downloads/
  your-post-title/
    _index.html      # Ekstrahert og renset HTML
    _index.md         # Konvertert Markdown
    image1.png        # Nedlastede bilder
    image2.png
```

## OpenAI API-nøkkel Oppsett

Lagre API-nøkkelen din i en fil kalt `OPENAI_API_KEY.TXT` i skriptmappen:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Kjør den Fullstendige Pipelinen

```bash
bash fetch_blog_posts.sh
```

Denne enkle kommandoen setter opp miljøet, scraper alle blogginnlegg fra sitemappen, laster ned bilder og konverterer alt til Markdown.

## Bidra til Prosjektet

Prosjektet er åpen kildekode. Feilrapporter, funksjonsforslag og pull requests er velkomne.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Prosjekt på GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Ofte Stilte Spørsmål

{{% details title="Hvorfor kan jeg ikke bare bruke `requests` til å scrape Wix-blogginnlegg?" closed="true" %}}
Wix rendrer innhold dynamisk med JavaScript. En standard HTTP-forespørsel returnerer et tomt sideskall. Selenium kjører en headless nettleser for å få den fullstendig rendrede HTML-en.
{{% /details %}}

{{% details title="Fungerer dette med hvilken som helst Wix-blogg?" closed="true" %}}
Ja. Scraperen leser blogg-sitemap-XML-en og behandler hver URL. Du trenger bare å oppdatere `SITEMAP_URL`-variabelen i `parse_blog_sitemap.py` til å peke på nettstedets sitemap.
{{% /details %}}

{{% details title="Hvilken OpenAI-modell bruker dette?" closed="true" %}}
Skriptet bruker GPT-4o som standard. Du kan endre `API_MODEL`-variabelen i `generate_md.py` for å bruke en annen modell.
{{% /details %}}

{{% details title="Kan jeg bruke dette til å migrere fra Wix til Hugo?" closed="true" %}}
Ja. Utdataen er standard Markdown med lokale bildestier, som fungerer direkte med Hugo, Jekyll, Astro og andre statiske sidegeneratorer. Legg til front matter i de genererte `_index.md`-filene for å fullføre migreringen.
{{% /details %}}

{{% details title="Hvor mye koster OpenAI API for dette?" closed="true" %}}
Kostnaden avhenger av antallet og lengden på blogginnleggene dine. En typisk blogg med 50 innlegg av moderat lengde koster noen få dollar i API-bruk med GPT-4o.
{{% /details %}}

{{% details title="Er dette verktøyet åpen kildekode?" closed="true" %}}
Ja. Den fullstendige kildekoden er tilgjengelig på [GitHub](https://github.com/everappz/wix-blog-export) under en åpen kildekode-lisens.
{{% /details %}}
