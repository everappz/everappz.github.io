---
title: "Eksportuj wpisy blogowe Wix do Markdown za pomocą OpenAI"
date: 2025-06-24
description: "Zautomatyzuj eksport bloga Wix za pomocą Python, Selenium i OpenAI. Wyodrębnij dynamiczną zawartość, pobierz obrazy i konwertuj HTML na czysty Markdown dla Hugo lub Jekyll."
keywords: ["eksport bloga Wix", "konwersja HTML na markdown", "konwersja markdown OpenAI", "wix na markdown", "migracja bloga SEO", "migracja wix na hugo", "skrobak beautifulsoup", "renderowanie HTML selenium", "automatyzacja API OpenAI", "migracja wix na stronę statyczną", "skrobak bloga wix python"]
tags: ["wix", "markdown", "migracja bloga", "openai", "skrobanie", "beautifulsoup", "selenium", "automatyzacja", "SEO", "poradnik"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Dlaczego warto eksportować wpisy blogowe z Wix?

**Podsumowanie:** Ten przewodnik pokazuje, jak eksportować wpisy blogowe Wix do Markdown za pomocą trzech skryptów Python: programu uruchomieniowego, skrobaka opartego na Selenium i konwertera HTML-na-Markdown opartego na OpenAI. Rezultatem są czyste, przenośne pliki Markdown gotowe do Hugo, Jekyll lub dowolnego generatora stron statycznych.

Wix nie oferuje natywnego eksportu bloga do Markdown. Jeśli migrujesz do generatora stron statycznych jak Hugo lub Jekyll, musisz skrobać wyrenderowane strony, wyodrębnić zawartość i ją skonwertować. Ten poradnik automatyzuje cały proces za pomocą **Python, Selenium, BeautifulSoup** i **API GPT OpenAI**.

Pipeline używa trzech skryptów:

- `fetch_blog_posts.sh` — konfiguruje środowisko i uruchamia pipeline
- `parse_blog_sitemap.py` — renderuje strony za pomocą Selenium, wyodrębnia zawartość, pobiera obrazy
- `generate_md.py` — konwertuje HTML na Markdown przez OpenAI

## Krok 1: Skonfiguruj Środowisko

Utwórz `fetch_blog_posts.sh` do obsługi sprawdzania Python, konfiguracji środowiska wirtualnego, instalacji zależności i wykonania pipeline.

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

## Krok 2: Skrobanie i Wyodrębnianie Zawartości Bloga

`parse_blog_sitemap.py` wykonuje ciężką pracę:

1. Pobiera XML mapy witryny, aby odkryć wszystkie adresy URL wpisów blogowych
2. Renderuje każdą stronę za pomocą **Selenium** (wymagane, ponieważ zawartość Wix jest ładowana dynamicznie)
3. Wyodrębnia `<div id="content-wrapper">` aby wyizolować zawartość artykułu
4. Pobiera wszystkie obrazy lokalnie i aktualizuje atrybuty `src`
5. Zapisuje oczyszczony HTML jako `_index.html`
6. Wywołuje konwerter Markdown

**Dlaczego Selenium zamiast requests?** Wix renderuje zawartość za pomocą JavaScript. Proste żądanie HTTP zwraca pustą powłokę strony. Selenium uruchamia bezgłową przeglądarkę Chrome, aby uzyskać w pełni wyrenderowany HTML.

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

## Krok 3: Konwertuj HTML na Markdown za pomocą OpenAI

`generate_md.py` czyta każdy plik `_index.html`, wysyła zawartość do API Chat OpenAI i zapisuje wynikowy Markdown.

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

## Struktura folderów wyjściowych

Po uruchomieniu pipeline każdy wpis blogowy otrzymuje własny folder:

```
downloads/
  your-post-title/
    _index.html      # Wyodrębniony i oczyszczony HTML
    _index.md         # Skonwertowany Markdown
    image1.png        # Pobrane obrazy
    image2.png
```

## Konfiguracja klucza API OpenAI

Zapisz swój klucz API w pliku o nazwie `OPENAI_API_KEY.TXT` w katalogu skryptu:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Uruchom pełny pipeline

```bash
bash fetch_blog_posts.sh
```

To pojedyncze polecenie konfiguruje środowisko, skrobie wszystkie wpisy blogowe z mapy witryny, pobiera obrazy i konwertuje wszystko na Markdown.

## Współtwórz projekt

Projekt jest open source. Raporty o błędach, sugestie funkcji i pull requesty są mile widziane.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Projekt na GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Często Zadawane Pytania

{{% details title="Dlaczego nie mogę po prostu użyć `requests` do skrobania wpisów blogowych Wix?" closed="true" %}}
Wix renderuje zawartość dynamicznie za pomocą JavaScript. Standardowe żądanie HTTP zwraca pustą powłokę strony. Selenium uruchamia bezgłową przeglądarkę, aby uzyskać w pełni wyrenderowany HTML.
{{% /details %}}

{{% details title="Czy to działa z dowolnym blogiem Wix?" closed="true" %}}
Tak. Skrobak odczytuje XML mapy witryny bloga i przetwarza każdy URL. Wystarczy zaktualizować zmienną `SITEMAP_URL` w `parse_blog_sitemap.py`, aby wskazywała na mapę witryny Twojej strony.
{{% /details %}}

{{% details title="Jakiego modelu OpenAI to używa?" closed="true" %}}
Skrypt domyślnie używa GPT-4o. Możesz zmienić zmienną `API_MODEL` w `generate_md.py`, aby użyć innego modelu.
{{% /details %}}

{{% details title="Czy mogę użyć tego do migracji z Wix do Hugo?" closed="true" %}}
Tak. Wynik to standardowy Markdown z lokalnymi ścieżkami obrazów, który działa bezpośrednio z Hugo, Jekyll, Astro i innymi generatorami stron statycznych. Dodaj front matter do wygenerowanych plików `_index.md`, aby zakończyć migrację.
{{% /details %}}

{{% details title="Ile kosztuje API OpenAI za to?" closed="true" %}}
Koszt zależy od liczby i długości wpisów blogowych. Typowy blog z 50 wpisami o umiarkowanej długości kosztuje kilka dolarów za użycie API z GPT-4o.
{{% /details %}}

{{% details title="Czy to narzędzie jest open source?" closed="true" %}}
Tak. Pełny kod źródłowy jest dostępny na [GitHub](https://github.com/everappz/wix-blog-export) na licencji open source.
{{% /details %}}
