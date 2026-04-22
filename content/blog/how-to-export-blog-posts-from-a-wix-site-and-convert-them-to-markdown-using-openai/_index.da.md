---
title: "Eksporter Wix blogindlæg til Markdown med OpenAI"
date: 2025-06-24
description: "Automatiser Wix blog-eksport med Python, Selenium og OpenAI. Udtræk dynamisk indhold, download billeder og konverter HTML til ren Markdown til Hugo eller Jekyll."
keywords: ["Wix blog eksport", "konverter HTML til markdown", "OpenAI markdown konvertering", "wix til markdown", "SEO blog migration", "wix til hugo migration", "beautifulsoup scraper", "selenium render HTML", "OpenAI API automatisering", "migrer wix til statisk site", "wix blog scraper python"]
tags: ["wix", "markdown", "blog migration", "openai", "scraping", "beautifulsoup", "selenium", "automatisering", "SEO", "vejledning"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Hvorfor eksportere blogindlæg fra Wix?

**Resumé:** Denne guide viser, hvordan man eksporterer Wix blogindlæg til Markdown ved hjælp af tre Python-scripts: en opsætningskører, en Selenium-baseret scraper og en OpenAI-drevet HTML-til-Markdown konverter. Resultatet er rene, bærbare Markdown-filer klar til Hugo, Jekyll eller enhver statisk sitegenerator.

Wix tilbyder ikke en native blog-eksport til Markdown. Hvis du migrerer til en statisk sitegenerator som Hugo eller Jekyll, skal du scrape de renderede sider, udtrække indholdet og konvertere det. Denne vejledning automatiserer hele processen med **Python, Selenium, BeautifulSoup** og **OpenAI's GPT API**.

Pipelinen bruger tre scripts:

- `fetch_blog_posts.sh` — opsætter miljøet og kører pipelinen
- `parse_blog_sitemap.py` — renderer sider med Selenium, udtrækker indhold, downloader billeder
- `generate_md.py` — konverterer HTML til Markdown via OpenAI

## Trin 1: Opsæt miljøet

Opret `fetch_blog_posts.sh` til at håndtere Python-kontrol, opsætning af virtuelt miljø, installation af afhængigheder og kørsel af pipelinen.

```bash
#!/bin/bash
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

## Trin 2: Scrap og udtræk blogindhold

`parse_blog_sitemap.py` gør det tunge arbejde:

1. Henter sitemap XML for at opdage alle blogindlægs-URL'er
2. Renderer hver side med **Selenium** (nødvendigt fordi Wix-indhold indlæses dynamisk)
3. Udtrækker `<div id="content-wrapper">` for at isolere artikelindhold
4. Downloader alle billeder lokalt og opdaterer `src`-attributter
5. Gemmer det rensede HTML som `_index.html`
6. Kalder Markdown-konverteren

**Hvorfor Selenium i stedet for requests?** Wix renderer indhold med JavaScript. En simpel HTTP-anmodning returnerer en tom sidekonstruktion. Selenium kører en hovedløs Chrome-browser for at få det fuldt renderede HTML.

```python
#!/usr/bin/env python3
import os, re, time
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

SITEMAP_URL = "https://www.everappz.com/blog-posts-sitemap.xml"
BASE_OUTPUT_DIR = "downloads"
GPT_CONVERTER_SCRIPT = "generate_md.py"

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
        urllib.request.urlretrieve(img_url, dest_path)
        return filename
    except Exception as e:
        return None

def extract_content_wrapper(html):
    soup = BeautifulSoup(html, "html.parser")
    wrapper = soup.find("div", id="content-wrapper")
    return str(wrapper) if wrapper else ""

def update_image_sources(content_html, folder):
    soup = BeautifulSoup(content_html, "html.parser")
    for img in soup.find_all("img"):
        src = img.get("data-pin-media") or img.get("src")
        if src:
            try:
                parsed = urlparse(src)
                filename = os.path.basename(parsed.path)
                dest_path = os.path.join(folder, filename)
                urllib.request.urlretrieve(src, dest_path)
                img["src"] = filename
            except Exception as e:
                pass
    return str(soup)

def parse_sitemap_and_process():
    os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)
    sitemap_xml = urllib.request.urlopen(SITEMAP_URL).read()
    root = ET.fromstring(sitemap_xml)
    url_elems = root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url")
    for url_elem in url_elems:
        loc_elem = url_elem.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        if loc_elem is not None:
            page_url = loc_elem.text.strip()
            try:
                subpath = get_last_path_components(page_url)
                folder_path = os.path.join(BASE_OUTPUT_DIR, subpath)
                os.makedirs(folder_path, exist_ok=True)
                html = fetch_rendered_html(page_url)
                wrapper_html = extract_content_wrapper(html)
                if not wrapper_html:
                    continue
                updated_html = update_image_sources(wrapper_html, folder_path)
                index_html_path = os.path.join(folder_path, "_index.html")
                with open(index_html_path, "w", encoding="utf-8") as f:
                    f.write(updated_html)
                os.system(f"python3 {GPT_CONVERTER_SCRIPT} \"{index_html_path}\"")
            except Exception as e:
                pass

if __name__ == "__main__":
    parse_sitemap_and_process()
```

## Trin 3: Konverter HTML til Markdown med OpenAI

`generate_md.py` læser hver `_index.html`-fil, sender indholdet til OpenAI's Chat API og skriver den resulterende Markdown.

```python
#!/usr/bin/env python3
import os, sys, json, time, random
import urllib.request, urllib.error
from bs4 import BeautifulSoup

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
    data = {"model": API_MODEL, "temperature": 0.3,
        "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": html_content}]}
    request = urllib.request.Request("https://api.openai.com/v1/chat/completions",
        data=json.dumps(data).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request) as response:
            result = json.load(response)
            return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return ""

def main():
    if len(sys.argv) != 2:
        return
    html_file = sys.argv[1]
    if not os.path.exists(html_file):
        return
    with open(html_file, "r", encoding="utf-8") as f:
        html = f.read()
    html_content = BeautifulSoup(html, "html.parser").prettify()
    markdown = call_openai_to_convert_to_markdown(html_content)
    if markdown:
        md_path = os.path.join(os.path.dirname(html_file), "_index.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(markdown)

if __name__ == "__main__":
    main()

```

## Outputmappestruktur

Efter kørsel af pipelinen får hvert blogindlæg sin egen mappe:

```
downloads/
  your-post-title/
    _index.html      # Udtrukket og renset HTML
    _index.md         # Konverteret Markdown
    image1.png        # Downloadede billeder
    image2.png
```

## OpenAI API nøgleopsætning

Gem din API-nøgle i en fil kaldet `OPENAI_API_KEY.TXT` i scriptmappen:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Kør den fulde pipeline

```bash
bash fetch_blog_posts.sh
```

Denne ene kommando opsætter miljøet, scraper alle blogindlæg fra sitemappen, downloader billeder og konverterer alt til Markdown.

## Bidrag til projektet

Projektet er open source. Fejlrapporter, funktionsforslag og pull requests er velkomne.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Projekt på GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Ofte stillede spørgsmål

{{% details title="Hvorfor kan jeg ikke bare bruge `requests` til at scrape Wix blogindlæg?" closed="true" %}}
Wix renderer indhold dynamisk med JavaScript. En standard HTTP-anmodning returnerer en tom sidekonstruktion. Selenium kører en hovedløs browser for at få det fuldt renderede HTML.
{{% /details %}}

{{% details title="Fungerer dette med enhver Wix blog?" closed="true" %}}
Ja. Scraperen læser blog-sitemap XML og behandler hvert URL. Du behøver kun at opdatere `SITEMAP_URL`-variablen i `parse_blog_sitemap.py` til at pege på dit sites sitemap.
{{% /details %}}

{{% details title="Hvilken OpenAI model bruger dette?" closed="true" %}}
Scriptet bruger GPT-4o som standard. Du kan ændre `API_MODEL`-variablen i `generate_md.py` for at bruge en anden model.
{{% /details %}}

{{% details title="Kan jeg bruge dette til at migrere fra Wix til Hugo?" closed="true" %}}
Ja. Outputtet er standard Markdown med lokale billedstier, som fungerer direkte med Hugo, Jekyll, Astro og andre statiske sitegeneratorer. Tilføj front matter til de genererede `_index.md`-filer for at fuldføre migrationen.
{{% /details %}}

{{% details title="Hvad koster OpenAI API til dette?" closed="true" %}}
Prisen afhænger af antallet og længden af dine blogindlæg. En typisk blog med 50 indlæg af moderat længde koster et par dollars i API-forbrug med GPT-4o.
{{% /details %}}

{{% details title="Er dette værktøj open source?" closed="true" %}}
Ja. Den fulde kildekode er tilgængelig på [GitHub](https://github.com/everappz/wix-blog-export) under en open source-licens.
{{% /details %}}
