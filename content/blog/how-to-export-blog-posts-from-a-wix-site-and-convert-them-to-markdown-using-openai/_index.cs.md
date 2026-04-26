---
title: "Export příspěvků blogu z Wix do Markdown pomocí OpenAI"
date: 2025-06-24
description: "Automatizujte export blogu z Wix pomocí Pythonu, Selenia a OpenAI. Extrahujte dynamický obsah, stáhněte obrázky a převeďte HTML na čistý Markdown pro Hugo nebo Jekyll."
keywords: ["export blogu Wix", "převod HTML na markdown", "převod OpenAI na markdown", "wix na markdown", "migrace blogu SEO", "migrace wix na hugo", "scraper beautifulsoup", "renderování HTML selenium", "automatizace OpenAI API", "migrace wix na statický web", "scraper blogu wix python"]
tags: ["wix", "markdown", "migrace blogu", "openai", "scraping", "beautifulsoup", "selenium", "automatizace", "SEO", "návod"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Proč exportovat příspěvky blogu z Wix?

**Shrnutí:** Tento průvodce ukazuje, jak exportovat příspěvky blogu z Wix do Markdown pomocí tří Python skriptů: spouštěče nastavení, scraperu na bázi Selenia a převodníku HTML na Markdown poháněného OpenAI. Výsledkem jsou čisté, přenositelné soubory Markdown připravené pro Hugo, Jekyll nebo jakýkoli generátor statických stránek.

Wix nenabízí nativní export blogu do Markdown. Pokud migrujete na generátor statických stránek jako Hugo nebo Jekyll, potřebujete vytáhnout vykreslené stránky, extrahovat obsah a převést ho. Tento návod automatizuje celý proces pomocí **Pythonu, Selenia, BeautifulSoup** a **OpenAI GPT API**.

Pipeline používá tři skripty:

- `fetch_blog_posts.sh` — nastaví prostředí a spustí pipeline
- `parse_blog_sitemap.py` — vykreslí stránky pomocí Selenia, extrahuje obsah, stáhne obrázky
- `generate_md.py` — převede HTML na Markdown přes OpenAI

## Krok 1: Nastavení prostředí

Vytvořte `fetch_blog_posts.sh` pro správu kontroly Pythonu, nastavení virtuálního prostředí, instalaci závislostí a spuštění pipeline.

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

## Krok 2: Extrakce obsahu blogu

`parse_blog_sitemap.py` dělá hlavní práci:

1. Načte XML sitemapu pro zjištění všech URL příspěvků
2. Vykreslí každou stránku pomocí **Selenia** (nutné, protože Wix načítá obsah dynamicky)
3. Extrahuje `<div id="content-wrapper">` pro izolaci obsahu článku
4. Stáhne všechny obrázky lokálně a aktualizuje atributy `src`
5. Uloží vyčištěné HTML jako `_index.html`
6. Zavolá převodník Markdown

**Proč Selenium místo requests?** Wix vykresluje obsah JavaScriptem. Jednoduchý HTTP požadavek vrátí prázdný rámec stránky. Selenium spouští prohlížeč Chrome bez grafického rozhraní pro získání plně vykresleného HTML.

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
                img["src"] = filename
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

                os.system(f"python3 {GPT_CONVERTER_SCRIPT} \"{index_html_path}\"")

            except Exception as e:
                print(f"❌ Failed to process {page_url}: {e}")

if __name__ == "__main__":
    parse_sitemap_and_process()
```

## Krok 3: Převod HTML na Markdown pomocí OpenAI

`generate_md.py` čte každý soubor `_index.html`, odesílá obsah do Chat API OpenAI a zapisuje výsledný Markdown.

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

## Struktura výstupních složek

Po spuštění pipeline získá každý příspěvek vlastní složku:

```
downloads/
  your-post-title/
    _index.html      # Extrahované a vyčištěné HTML
    _index.md         # Převedený Markdown
    image1.png        # Stažené obrázky
    image2.png
```

## Nastavení klíče OpenAI API

Uložte svůj API klíč do souboru `OPENAI_API_KEY.TXT` v adresáři skriptů:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Spuštění celého pipeline

```bash
bash fetch_blog_posts.sh
```

Tento jediný příkaz nastaví prostředí, extrahuje všechny příspěvky blogu ze sitemapy, stáhne obrázky a převede vše do Markdown.

## Přispějte do projektu

Projekt je open source. Hlášení chyb, návrhy funkcí a pull requesty jsou vítány.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Projekt na GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Často kladené otázky

{{% details title="Proč nemohu jednoduše použít `requests` k extrakci příspěvků blogu Wix?" closed="true" %}}
Wix vykresluje obsah dynamicky pomocí JavaScriptu. Standardní HTTP požadavek vrátí prázdný rámec stránky. Selenium spouští prohlížeč bez grafického rozhraní pro získání plně vykresleného HTML.
{{% /details %}}

{{% details title="Funguje to s jakýmkoli blogem na Wix?" closed="true" %}}
Ano. Scraper čte XML sitemapu a zpracovává každé URL. Stačí aktualizovat proměnnou `SITEMAP_URL` v `parse_blog_sitemap.py` tak, aby ukazovala na sitemapu vašeho webu.
{{% /details %}}

{{% details title="Jaký model OpenAI to používá?" closed="true" %}}
Skript používá GPT-4o ve výchozím nastavení. Můžete změnit proměnnou `API_MODEL` v `generate_md.py` pro použití jiného modelu.
{{% /details %}}

{{% details title="Mohu to použít pro migraci z Wix na Hugo?" closed="true" %}}
Ano. Výstupem je standardní Markdown s lokálními cestami k obrázkům, který funguje přímo s Hugo, Jekyll, Astro a dalšími generátory statických stránek. Přidejte front matter do vygenerovaných souborů `_index.md` pro dokončení migrace.
{{% /details %}}

{{% details title="Kolik stojí OpenAI API za toto použití?" closed="true" %}}
Cena závisí na počtu a délce vašich příspěvků. Typický blog s 50 příspěvky střední délky stojí několik dolarů za využití API s GPT-4o.
{{% /details %}}

{{% details title="Je tento nástroj open source?" closed="true" %}}
Ano. Kompletní zdrojový kód je dostupný na [GitHub](https://github.com/everappz/wix-blog-export) pod open-source licencí.
{{% /details %}}
