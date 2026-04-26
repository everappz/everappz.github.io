---
title: "Export blogových príspevkov z Wix do Markdown pomocou OpenAI"
date: 2025-06-24
description: "Automatizujte export blogu z Wix pomocou Python, Selenium a OpenAI. Extrahujte dynamický obsah, stiahnite obrázky a konvertujte HTML na čistý Markdown pre Hugo alebo Jekyll."
keywords: ["export blogu Wix", "konverzia HTML na markdown", "OpenAI konverzia markdown", "wix do markdown", "migrácia SEO blogu", "migrácia wix do hugo", "beautifulsoup scraper", "selenium render HTML", "OpenAI API automatizácia", "migrácia wix na statickú stránku", "wix blog scraper python"]
tags: ["wix", "markdown", "migrácia blogu", "openai", "scraping", "beautifulsoup", "selenium", "automatizácia", "SEO", "návod"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Prečo exportovať blogové príspevky z Wix?

**Zhrnutie:** Tento návod ukazuje, ako exportovať blogové príspevky z Wix do Markdown pomocou troch Python skriptov: spúšťač nastavenia, scraper založený na Selenium a konvertor HTML na Markdown poháňaný OpenAI. Výsledkom sú čisté, prenosné Markdown súbory pripravené pre Hugo, Jekyll alebo akýkoľvek generátor statických stránok.

Wix neponúka natívny export blogu do Markdown. Ak migrujete na generátor statických stránok ako Hugo alebo Jekyll, musíte scrapovať vykreslené stránky, extrahovať obsah a konvertovať ho. Tento návod automatizuje celý proces pomocou **Python, Selenium, BeautifulSoup** a **OpenAI GPT API**.

Pipeline používa tri skripty:

- `fetch_blog_posts.sh` — nastaví prostredie a spustí pipeline
- `parse_blog_sitemap.py` — vykreslí stránky pomocou Selenium, extrahuje obsah, stiahne obrázky
- `generate_md.py` — konvertuje HTML na Markdown cez OpenAI

## Krok 1: Nastavenie prostredia

Vytvorte `fetch_blog_posts.sh` na spracovanie kontroly Python, nastavenie virtuálneho prostredia, inštaláciu závislostí a spustenie pipeline.

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

## Krok 2: Scrapovanie a extrakcia obsahu blogu

`parse_blog_sitemap.py` vykonáva ťažkú prácu:

1. Získa sitemap XML na objavenie všetkých URL blogových príspevkov
2. Vykreslí každú stránku pomocou **Selenium** (potrebné, pretože Wix obsah sa načítava dynamicky)
3. Extrahuje `<div id="content-wrapper">` na izoláciu obsahu článku
4. Stiahne všetky obrázky lokálne a aktualizuje atribúty `src`
5. Uloží vyčistené HTML ako `_index.html`
6. Zavolá konvertor Markdown

**Prečo Selenium namiesto requests?** Wix vykresluje obsah pomocou JavaScript. Jednoduchý HTTP request vráti prázdnu kostru stránky. Selenium spustí headless Chrome prehliadač na získanie plne vykresleného HTML.

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

## Krok 3: Konverzia HTML na Markdown pomocou OpenAI

`generate_md.py` načíta každý súbor `_index.html`, odošle obsah do OpenAI Chat API a zapíše výsledný Markdown.

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

## Štruktúra výstupných priečinkov

Po spustení pipeline každý blogový príspevok dostane vlastný priečinok:

```
downloads/
  your-post-title/
    _index.html      # Extrahované a vyčistené HTML
    _index.md         # Konvertovaný Markdown
    image1.png        # Stiahnuté obrázky
    image2.png
```

## Nastavenie OpenAI API kľúča

Uložte svoj API kľúč do súboru s názvom `OPENAI_API_KEY.TXT` v adresári skriptov:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Spustenie celého pipeline

```bash
bash fetch_blog_posts.sh
```

Tento jediný príkaz nastaví prostredie, scrapuje všetky blogové príspevky zo sitemapy, stiahne obrázky a konvertuje všetko na Markdown.

## Prispejte do projektu

Projekt je open source. Hlásenia chýb, návrhy funkcií a pull requesty sú vítané.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Projekt na GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Často kladené otázky

{{% details title="Prečo nemôžem použiť len `requests` na scrapovanie blogových príspevkov z Wix?" closed="true" %}}
Wix vykresluje obsah dynamicky pomocou JavaScript. Štandardný HTTP request vráti prázdnu kostru stránky. Selenium spustí headless prehliadač na získanie plne vykresleného HTML.
{{% /details %}}

{{% details title="Funguje to s akýmkoľvek blogom na Wix?" closed="true" %}}
Áno. Scraper číta sitemap XML blogu a spracováva každú URL. Stačí aktualizovať premennú `SITEMAP_URL` v `parse_blog_sitemap.py` tak, aby ukazovala na sitemapu vašej stránky.
{{% /details %}}

{{% details title="Aký model OpenAI to používa?" closed="true" %}}
Skript štandardne používa GPT-4o. Môžete zmeniť premennú `API_MODEL` v `generate_md.py` na použitie iného modelu.
{{% /details %}}

{{% details title="Môžem to použiť na migráciu z Wix do Hugo?" closed="true" %}}
Áno. Výstupom je štandardný Markdown s lokálnymi cestami k obrázkom, ktorý funguje priamo s Hugo, Jekyll, Astro a ďalšími generátormi statických stránok. Pridajte front matter do vygenerovaných súborov `_index.md` na dokončenie migrácie.
{{% /details %}}

{{% details title="Koľko stojí OpenAI API na toto?" closed="true" %}}
Náklady závisia od počtu a dĺžky vašich blogových príspevkov. Typický blog s 50 príspevkami strednej dĺžky stojí niekoľko dolárov za API využitie s GPT-4o.
{{% /details %}}

{{% details title="Je tento nástroj open source?" closed="true" %}}
Áno. Úplný zdrojový kód je dostupný na [GitHub](https://github.com/everappz/wix-blog-export) pod open-source licenciou.
{{% /details %}}
