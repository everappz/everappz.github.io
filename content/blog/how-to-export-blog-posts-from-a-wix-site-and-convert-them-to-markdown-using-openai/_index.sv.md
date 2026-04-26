---
title: "Exportera Wix-blogginlägg till Markdown med OpenAI"
date: 2025-06-24
description: "Automatisera Wix-bloggexport med Python, Selenium och OpenAI. Extrahera dynamiskt innehåll, ladda ner bilder och konvertera HTML till ren Markdown för Hugo eller Jekyll."
keywords: ["Wix bloggexport", "konvertera HTML till markdown", "OpenAI markdown-konvertering", "wix till markdown", "SEO bloggmigrering", "wix till hugo-migrering", "beautifulsoup scraper", "selenium rendera HTML", "OpenAI API automatisering", "migrera wix till statisk sajt", "wix blogg scraper python"]
tags: ["wix", "markdown", "bloggmigrering", "openai", "scraping", "beautifulsoup", "selenium", "automatisering", "SEO", "handledning"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Varfor exportera blogginlagg fran Wix?

**Sammanfattning:** Denna guide visar hur du exporterar Wix-blogginlagg till Markdown med tre Python-skript: en installationskorare, en Selenium-baserad scraper och en OpenAI-driven HTML-till-Markdown-konverterare. Resultatet ar rena, portabla Markdown-filer redo for Hugo, Jekyll eller nagon annan statisk sajtgenerator.

Wix erbjuder ingen inbyggd bloggexport till Markdown. Om du migrerar till en statisk sajtgenerator som Hugo eller Jekyll behover du scrapa de renderade sidorna, extrahera innehallet och konvertera det. Denna handledning automatiserar hela processen med **Python, Selenium, BeautifulSoup** och **OpenAI:s GPT API**.

Pipelinen använder tre skript:

- `fetch_blog_posts.sh` — konfigurerar miljön och kör pipelinen
- `parse_blog_sitemap.py` — renderar sidor med Selenium, extraherar innehåll, laddar ner bilder
- `generate_md.py` — konverterar HTML till Markdown via OpenAI

## Steg 1: Konfigurera miljön

Skapa `fetch_blog_posts.sh` för att hantera Python-kontroller, virtuell miljö-konfiguration, beroendeinstallation och pipelinekörning.

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

## Steg 2: Scrapa och extrahera blogginnehåll

`parse_blog_sitemap.py` gör det tunga arbetet:

1. Hämtar sitemap-XML för att hitta alla blogginläggens URL:er
2. Renderar varje sida med **Selenium** (nödvändigt eftersom Wix-innehåll laddas dynamiskt)
3. Extraherar `<div id="content-wrapper">` för att isolera artikelinnehållet
4. Laddar ner alla bilder lokalt och uppdaterar `src`-attribut
5. Sparar den rensade HTML:en som `_index.html`
6. Anropar Markdown-konverteraren

**Varför Selenium istället för requests?** Wix renderar innehåll med JavaScript. En enkel HTTP-begäran returnerar en tom sidmall. Selenium kör en headless Chrome-webbläsare för att få den fullständigt renderade HTML:en.

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

## Steg 3: Konvertera HTML till Markdown med OpenAI

`generate_md.py` läser varje `_index.html`-fil, skickar innehållet till OpenAI:s Chat API och skriver den resulterande Markdown-filen.

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

## Utdatamappstruktur

Efter att ha kört pipelinen får varje blogginlägg sin egen mapp:

```
downloads/
  your-post-title/
    _index.html      # Extraherad och rensad HTML
    _index.md         # Konverterad Markdown
    image1.png        # Nedladdade bilder
    image2.png
```

## Konfiguration av OpenAI API-nyckel

Spara din API-nyckel i en fil som heter `OPENAI_API_KEY.TXT` i skriptkatalogen:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Kör hela pipelinen

```bash
bash fetch_blog_posts.sh
```

Detta enda kommando konfigurerar miljön, scrapar alla blogginlägg från sitemap:en, laddar ner bilder och konverterar allt till Markdown.

## Bidra till projektet

Projektet är öppen källkod. Felrapporter, funktionsförslag och pull requests är välkomna.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Projekt på GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Vanliga frågor

{{% details title="Varför kan jag inte bara använda `requests` för att scrapa Wix-blogginlägg?" closed="true" %}}
Wix renderar innehåll dynamiskt med JavaScript. En standard HTTP-begäran returnerar en tom sidmall. Selenium kör en headless webbläsare för att få den fullständigt renderade HTML:en.
{{% /details %}}

{{% details title="Fungerar detta med vilken Wix-blogg som helst?" closed="true" %}}
Ja. Scrapern läser bloggens sitemap-XML och bearbetar varje URL. Du behöver bara uppdatera variabeln `SITEMAP_URL` i `parse_blog_sitemap.py` så att den pekar på din sajts sitemap.
{{% /details %}}

{{% details title="Vilken OpenAI-modell använder detta?" closed="true" %}}
Skriptet använder GPT-4o som standard. Du kan ändra variabeln `API_MODEL` i `generate_md.py` för att använda en annan modell.
{{% /details %}}

{{% details title="Kan jag använda detta för att migrera från Wix till Hugo?" closed="true" %}}
Ja. Utdata är standard Markdown med lokala bildsökvägar, vilket fungerar direkt med Hugo, Jekyll, Astro och andra statiska sajtgeneratorer. Lägg till front matter till de genererade `_index.md`-filerna för att slutföra migreringen.
{{% /details %}}

{{% details title="Hur mycket kostar OpenAI API för detta?" closed="true" %}}
Kostnaden beror på antalet och längden på dina blogginlägg. En typisk blogg med 50 inlägg av måttlig längd kostar några dollar i API-användning med GPT-4o.
{{% /details %}}

{{% details title="Är detta verktyg öppen källkod?" closed="true" %}}
Ja. Den fullständiga källkoden finns tillgänglig på [GitHub](https://github.com/everappz/wix-blog-export) under en öppen källkodslicens.
{{% /details %}}
