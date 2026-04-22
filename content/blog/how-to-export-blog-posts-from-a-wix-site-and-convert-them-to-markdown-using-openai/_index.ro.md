---
title: "Exportă Postări de Blog Wix în Markdown cu OpenAI"
date: 2025-06-24
description: "Automatizează exportul blogului Wix folosind Python, Selenium și OpenAI. Extrage conținut dinamic, descarcă imagini și convertește HTML în Markdown curat pentru Hugo sau Jekyll."
keywords: ["export blog Wix", "convertire HTML în markdown", "conversie markdown OpenAI", "wix în markdown", "migrare blog SEO", "migrare wix în hugo", "scraper beautifulsoup", "randare HTML selenium", "automatizare API OpenAI", "migrare wix la site static", "scraper blog wix python"]
tags: ["wix", "markdown", "migrare blog", "openai", "scraping", "beautifulsoup", "selenium", "automatizare", "SEO", "tutorial"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## De Ce Să Exportați Postările de Blog din Wix?

**Rezumat:** Acest ghid arată cum să exportați postările de blog Wix în Markdown folosind trei scripturi Python: un executor de configurare, un scraper bazat pe Selenium și un convertor HTML-în-Markdown alimentat de OpenAI. Rezultatul sunt fișiere Markdown curate și portabile, gata pentru Hugo, Jekyll sau orice generator de site-uri statice.

Wix nu oferă export nativ de blog în Markdown. Dacă migrați la un generator de site-uri statice precum Hugo sau Jekyll, trebuie să extrageți paginile randate, să extrageți conținutul și să îl convertiți. Acest tutorial automatizează întregul proces folosind **Python, Selenium, BeautifulSoup** și **API-ul GPT al OpenAI**.

Pipeline-ul folosește trei scripturi:

- `fetch_blog_posts.sh` — configurează mediul și rulează pipeline-ul
- `parse_blog_sitemap.py` — randează paginile cu Selenium, extrage conținut, descarcă imagini
- `generate_md.py` — convertește HTML în Markdown prin OpenAI

## Pasul 1: Configurarea Mediului

Creați `fetch_blog_posts.sh` pentru a gestiona verificările Python, configurarea mediului virtual, instalarea dependențelor și execuția pipeline-ului.

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

## Pasul 2: Extragerea Conținutului Blogului

`parse_blog_sitemap.py` face munca grea:

1. Preia XML-ul sitemap-ului pentru a descoperi toate URL-urile postărilor de blog
2. Randează fiecare pagină cu **Selenium** (necesar deoarece conținutul Wix este încărcat dinamic)
3. Extrage `<div id="content-wrapper">` pentru a izola conținutul articolului
4. Descarcă toate imaginile local și actualizează atributele `src`
5. Salvează HTML-ul curățat ca `_index.html`
6. Apelează convertorul Markdown

**De ce Selenium în loc de requests?** Wix randează conținutul cu JavaScript. O simplă cerere HTTP returnează o coajă de pagină goală. Selenium rulează un browser Chrome headless pentru a obține HTML-ul complet randat.

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

## Pasul 3: Convertiți HTML în Markdown cu OpenAI

`generate_md.py` citește fiecare fișier `_index.html`, trimite conținutul la API-ul Chat al OpenAI și scrie Markdown-ul rezultat.

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

## Structura Folderelor de Ieșire

După rularea pipeline-ului, fiecare postare de blog primește propriul folder:

```
downloads/
  your-post-title/
    _index.html      # HTML extras și curățat
    _index.md         # Markdown convertit
    image1.png        # Imagini descărcate
    image2.png
```

## Configurarea Cheii API OpenAI

Salvați cheia API într-un fișier numit `OPENAI_API_KEY.TXT` în directorul scriptului:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Rulați Pipeline-ul Complet

```bash
bash fetch_blog_posts.sh
```

Această singură comandă configurează mediul, extrage toate postările de blog din sitemap, descarcă imaginile și convertește totul în Markdown.

## Contribuiți la Proiect

Proiectul este open source. Rapoartele de erori, sugestiile de funcții și pull request-urile sunt binevenite.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Proiect pe GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Întrebări Frecvente

{{% details title="De ce nu pot folosi pur și simplu `requests` pentru a extrage postările de blog Wix?" closed="true" %}}
Wix randează conținutul dinamic cu JavaScript. O cerere HTTP standard returnează o coajă de pagină goală. Selenium rulează un browser headless pentru a obține HTML-ul complet randat.
{{% /details %}}

{{% details title="Funcționează cu orice blog Wix?" closed="true" %}}
Da. Scraper-ul citește XML-ul sitemap-ului blogului și procesează fiecare URL. Trebuie doar să actualizați variabila `SITEMAP_URL` din `parse_blog_sitemap.py` pentru a indica către sitemap-ul site-ului dvs.
{{% /details %}}

{{% details title="Ce model OpenAI folosește?" closed="true" %}}
Scriptul folosește GPT-4o implicit. Puteți schimba variabila `API_MODEL` din `generate_md.py` pentru a folosi un alt model.
{{% /details %}}

{{% details title="Pot folosi asta pentru a migra de la Wix la Hugo?" closed="true" %}}
Da. Ieșirea este Markdown standard cu căi locale de imagini, care funcționează direct cu Hugo, Jekyll, Astro și alți generatoare de site-uri statice. Adăugați front matter la fișierele `_index.md` generate pentru a finaliza migrarea.
{{% /details %}}

{{% details title="Cât costă API-ul OpenAI pentru asta?" closed="true" %}}
Costul depinde de numărul și lungimea postărilor de blog. Un blog tipic cu 50 de postări de lungime moderată costă câțiva dolari în utilizarea API cu GPT-4o.
{{% /details %}}

{{% details title="Acest instrument este open source?" closed="true" %}}
Da. Codul sursă complet este disponibil pe [GitHub](https://github.com/everappz/wix-blog-export) sub o licență open source.
{{% /details %}}
