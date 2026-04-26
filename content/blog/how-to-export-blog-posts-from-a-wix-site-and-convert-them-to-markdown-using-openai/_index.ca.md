---
title: "Exporta articles de blog de Wix a Markdown amb OpenAI"
date: 2025-06-24
description: "Automatitza l'exportació del blog de Wix amb Python, Selenium i OpenAI. Extreu contingut dinàmic, descarrega imatges i converteix HTML a Markdown net per a Hugo o Jekyll."
keywords: ["exportació blog Wix", "convertir HTML a markdown", "conversió OpenAI a markdown", "wix a markdown", "migració blog SEO", "migració wix a hugo", "scraper beautifulsoup", "renderitzar HTML amb selenium", "automatització OpenAI API", "migrar wix a lloc estàtic", "scraper blog wix python"]
tags: ["wix", "markdown", "migració de blog", "openai", "scraping", "beautifulsoup", "selenium", "automatització", "SEO", "tutorial"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Per què exportar articles de blog de Wix?

**Resum:** Aquesta guia mostra com exportar articles de blog de Wix a Markdown utilitzant tres scripts de Python: un executor de configuració, un scraper basat en Selenium i un convertidor d'HTML a Markdown amb OpenAI. El resultat són arxius Markdown nets i portables preparats per a Hugo, Jekyll o qualsevol generador de llocs estàtics.

Wix no ofereix una exportació nativa del blog a Markdown. Si estàs migrant a un generador de llocs estàtics com Hugo o Jekyll, necessites extreure les pàgines renderitzades, extreure'n el contingut i convertir-lo. Aquest tutorial automatitza tot el procés amb **Python, Selenium, BeautifulSoup** i **OpenAI GPT API**.

El pipeline utilitza tres scripts:

- `fetch_blog_posts.sh` — configura l'entorn i executa el pipeline
- `parse_blog_sitemap.py` — renderitza pàgines amb Selenium, extreu contingut, descarrega imatges
- `generate_md.py` — converteix HTML a Markdown via OpenAI

## Pas 1: Configura l'entorn

Crea `fetch_blog_posts.sh` per gestionar la verificació de Python, configuració de l'entorn virtual, instal·lació de dependències i execució del pipeline.

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

## Pas 2: Extreu el contingut del blog

`parse_blog_sitemap.py` fa la feina pesada:

1. Obté el XML del sitemap per descobrir tots els URLs dels articles
2. Renderitza cada pàgina amb **Selenium** (necessari perquè Wix carrega el contingut dinàmicament)
3. Extreu el `<div id="content-wrapper">` per aïllar el contingut de l'article
4. Descarrega totes les imatges localment i actualitza els atributs `src`
5. Desa l'HTML netejat com a `_index.html`
6. Crida el convertidor de Markdown

**Per què Selenium en lloc de requests?** Wix renderitza contingut amb JavaScript. Una petició HTTP simple retorna un esquelet buit. Selenium executa un navegador Chrome sense interfície per obtenir l'HTML completament renderitzat.

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

## Pas 3: Converteix HTML a Markdown amb OpenAI

`generate_md.py` llegeix cada arxiu `_index.html`, envia el contingut a l'API Chat d'OpenAI i escriu el Markdown resultant.

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

## Estructura de carpetes de sortida

Després d'executar el pipeline, cada article del blog obté la seva pròpia carpeta:

```
downloads/
  your-post-title/
    _index.html      # HTML extret i netejat
    _index.md         # Markdown convertit
    image1.png        # Imatges descarregades
    image2.png
```

## Configuració de la clau de l'API d'OpenAI

Desa la teva clau API en un arxiu anomenat `OPENAI_API_KEY.TXT` al directori dels scripts:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Executa el pipeline complet

```bash
bash fetch_blog_posts.sh
```

Aquesta única comanda configura l'entorn, extreu tots els articles del blog del sitemap, descarrega imatges i converteix tot a Markdown.

## Contribueix al projecte

El projecte és de codi obert. Els informes d'errors, suggeriments de funcions i pull requests són benvinguts.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Projecte a GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Preguntes freqüents

{{% details title="Per què no puc simplement usar `requests` per extreure articles de blog de Wix?" closed="true" %}}
Wix renderitza contingut dinàmicament amb JavaScript. Una petició HTTP estàndard retorna un esquelet de pàgina buit. Selenium executa un navegador sense interfície per obtenir l'HTML completament renderitzat.
{{% /details %}}

{{% details title="Funciona amb qualsevol blog de Wix?" closed="true" %}}
Sí. L'scraper llegeix el XML del sitemap i processa cada URL. Només cal actualitzar la variable `SITEMAP_URL` a `parse_blog_sitemap.py` per apuntar al sitemap del teu lloc.
{{% /details %}}

{{% details title="Quin model d'OpenAI utilitza?" closed="true" %}}
L'script utilitza GPT-4o per defecte. Pots canviar la variable `API_MODEL` a `generate_md.py` per usar un model diferent.
{{% /details %}}

{{% details title="Puc usar això per migrar de Wix a Hugo?" closed="true" %}}
Sí. La sortida és Markdown estàndard amb rutes d'imatges locals, que funciona directament amb Hugo, Jekyll, Astro i altres generadors de llocs estàtics. Afegeix front matter als arxius `_index.md` generats per completar la migració.
{{% /details %}}

{{% details title="Quant costa l'API d'OpenAI per a això?" closed="true" %}}
El cost depèn del nombre i longitud dels teus articles. Un blog típic amb 50 articles de longitud moderada costa uns quants dòlars en ús d'API amb GPT-4o.
{{% /details %}}

{{% details title="Aquesta eina és de codi obert?" closed="true" %}}
Sí. El codi font complet està disponible a [GitHub](https://github.com/everappz/wix-blog-export) sota una llicència de codi obert.
{{% /details %}}
