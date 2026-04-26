---
title: "Vie Wix-blogijulkaisut Markdowniksi OpenAI:lla"
date: 2025-06-24
description: "Automatisoi Wix-blogin vienti Pythonilla, Seleniumilla ja OpenAI:lla. Poimi dynaaminen sisältö, lataa kuvat ja muunna HTML puhtaaksi Markdowniksi Hugolle tai Jekyllille."
keywords: ["Wix blogin vienti", "muunna HTML markdowniksi", "OpenAI markdown-muunnos", "wix markdowniksi", "SEO blogin migraatio", "wix hugo migraatio", "beautifulsoup scraper", "selenium HTML-renderöinti", "OpenAI API automatisointi", "wix staattiseksi sivustoksi", "wix blogi scraper python"]
tags: ["wix", "markdown", "blogin migraatio", "openai", "scraping", "beautifulsoup", "selenium", "automatisointi", "SEO", "opas"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Miksi viedä blogijulkaisuja Wixistä?

**Yhteenveto:** Tämä opas näyttää, miten Wix-blogijulkaisut viedään Markdowniksi kolmella Python-skriptillä: asetustenvalmistelija, Selenium-pohjainen scraper ja OpenAI-käyttöinen HTML-Markdown-muunnin. Tuloksena on puhtaat, siirrettävät Markdown-tiedostot valmiina Hugolle, Jekyllille tai mille tahansa staattisten sivujen generaattorille.

Wix ei tarjoa natiivia blogin vientiä Markdowniksi. Jos siirryt staattiseen sivugeneraattoriin kuten Hugo tai Jekyll, sinun täytyy raapia renderöidyt sivut, poimia sisältö ja muuntaa se. Tämä opas automatisoi koko prosessin käyttäen **Pythonia, Seleniumia, BeautifulSoupia** ja **OpenAI:n GPT API:a**.

Pipeline käyttää kolmea skriptiä:

- `fetch_blog_posts.sh` — valmistelee ympäristön ja ajaa pipelinen
- `parse_blog_sitemap.py` — renderöi sivut Seleniumilla, poimii sisällön, lataa kuvat
- `generate_md.py` — muuntaa HTML:n Markdowniksi OpenAI:lla

## Vaihe 1: Ympäristön asennus

Luo `fetch_blog_posts.sh` Python-tarkistukseen, virtuaaliympäristön asettamiseen, riippuvuuksien asentamiseen ja pipelinen ajamiseen.

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
    python3 -m venv "$VENV_DIR"
fi
source "$VENV_DIR/bin/activate"
pip install --upgrade pip
pip install beautifulsoup4 lxml selenium webdriver-manager
python3 parse_blog_sitemap.py
deactivate
```

## Vaihe 2: Blogin sisällön poiminta

`parse_blog_sitemap.py` tekee raskaan työn:

1. Hakee sitemap-XML:n kaikkien blogijulkaisujen URL-osoitteiden löytämiseksi
2. Renderöi jokaisen sivun **Seleniumilla** (tarpeen koska Wix lataa sisällön dynaamisesti)
3. Poimii `<div id="content-wrapper">` artikkelin sisällön eristämiseksi
4. Lataa kaikki kuvat paikallisesti ja päivittää `src`-attribuutit
5. Tallentaa puhdistetun HTML:n muodossa `_index.html`
6. Kutsuu Markdown-muuntimen

**Miksi Selenium eikä requests?** Wix renderöi sisällön JavaScriptillä. Yksinkertainen HTTP-pyyntö palauttaa tyhjän sivurungon. Selenium ajaa headless Chrome-selaimen täysin renderöidyn HTML:n saamiseksi.

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

def get_last_path_components(url, levels=2):
    parts = urlparse(url).path.strip("/").split("/")
    return os.path.join(*parts[-levels:])

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
                urllib.request.urlretrieve(src, os.path.join(folder, filename))
                img["src"] = filename
            except: pass
    return str(soup)

def parse_sitemap_and_process():
    os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)
    sitemap_xml = urllib.request.urlopen(SITEMAP_URL).read()
    root = ET.fromstring(sitemap_xml)
    for url_elem in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
        loc_elem = url_elem.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        if loc_elem is not None:
            page_url = loc_elem.text.strip()
            try:
                subpath = get_last_path_components(page_url)
                folder_path = os.path.join(BASE_OUTPUT_DIR, subpath)
                os.makedirs(folder_path, exist_ok=True)
                html = fetch_rendered_html(page_url)
                wrapper_html = extract_content_wrapper(html)
                if not wrapper_html: continue
                updated_html = update_image_sources(wrapper_html, folder_path)
                index_html_path = os.path.join(folder_path, "_index.html")
                with open(index_html_path, "w", encoding="utf-8") as f:
                    f.write(updated_html)
                os.system(f"python3 {GPT_CONVERTER_SCRIPT} \"{index_html_path}\"")
            except: pass

if __name__ == "__main__":
    parse_sitemap_and_process()
```

## Vaihe 3: Muunna HTML Markdowniksi OpenAI:lla

`generate_md.py` lukee jokaisen `_index.html`-tiedoston, lähettää sisällön OpenAI:n Chat API:lle ja kirjoittaa tuloksena syntyvän Markdownin.

```python
#!/usr/bin/env python3
import os, sys, json, time, random
import urllib.request, urllib.error
from bs4 import BeautifulSoup

API_MODEL = "gpt-4o"
API_KEY_FILE = "OPENAI_API_KEY.TXT"

def call_openai_to_convert_to_markdown(html_content, api_key=None):
    if api_key is None:
        with open(API_KEY_FILE, "r") as f: api_key = f.read().strip()
    time.sleep(round(random.uniform(1.0, 2.0), 2))
    system_prompt = ("You are a tool that converts HTML content from blog posts into well-structured Markdown (.md) format. "
        "Convert all visible text content and replace all <img> tags with Markdown image syntax using their local filenames.")
    data = {"model": API_MODEL, "temperature": 0.3,
        "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": html_content}]}
    request = urllib.request.Request("https://api.openai.com/v1/chat/completions",
        data=json.dumps(data).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request) as response:
            return json.load(response)["choices"][0]["message"]["content"].strip()
    except: return ""

def main():
    if len(sys.argv) != 2: return
    html_file = sys.argv[1]
    if not os.path.exists(html_file): return
    with open(html_file, "r", encoding="utf-8") as f: html = f.read()
    markdown = call_openai_to_convert_to_markdown(BeautifulSoup(html, "html.parser").prettify())
    if markdown:
        with open(os.path.join(os.path.dirname(html_file), "_index.md"), "w", encoding="utf-8") as f:
            f.write(markdown)

if __name__ == "__main__":
    main()

```

## Tulostiedostorakenne

Pipelinen suorittamisen jälkeen jokainen blogijulkaisu saa oman kansionsa:

```
downloads/
  your-post-title/
    _index.html      # Poimittu ja puhdistettu HTML
    _index.md         # Muunnettu Markdown
    image1.png        # Ladatut kuvat
    image2.png
```

## OpenAI API -avaimen asetus

Tallenna API-avaimesi tiedostoon `OPENAI_API_KEY.TXT` skriptihakemistossa:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Aja koko pipeline

```bash
bash fetch_blog_posts.sh
```

Tämä yksittäinen komento valmistelee ympäristön, poimii kaikki blogijulkaisut sitemapista, lataa kuvat ja muuntaa kaiken Markdowniksi.

## Osallistu projektiin

Projekti on avoimen lähdekoodin. Virheraportteja, ominaisuusehdotuksia ja pull requesteja otetaan vastaan.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Projekti GitHubissa" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Usein kysytyt kysymykset

{{% details title="Miksi en voi vain käyttää `requests`-kirjastoa Wix-blogijulkaisujen poimimiseen?" closed="true" %}}
Wix renderöi sisällön dynaamisesti JavaScriptillä. Tavallinen HTTP-pyyntö palauttaa tyhjän sivurungon. Selenium ajaa headless-selaimen täysin renderöidyn HTML:n saamiseksi.
{{% /details %}}

{{% details title="Toimiiko tämä minkä tahansa Wix-blogin kanssa?" closed="true" %}}
Kyllä. Scraper lukee blogin sitemap-XML:n ja käsittelee jokaisen URL:n. Sinun tarvitsee vain päivittää `SITEMAP_URL`-muuttuja `parse_blog_sitemap.py`-tiedostossa osoittamaan sivustosi sitemapiin.
{{% /details %}}

{{% details title="Mitä OpenAI-mallia tämä käyttää?" closed="true" %}}
Skripti käyttää oletuksena GPT-4o. Voit muuttaa `API_MODEL`-muuttujaa `generate_md.py`-tiedostossa käyttääksesi eri mallia.
{{% /details %}}

{{% details title="Voinko käyttää tätä siirtymiseen Wixistä Hugoon?" closed="true" %}}
Kyllä. Tuloste on standardia Markdownia paikallisilla kuvapolulla, joka toimii suoraan Hugon, Jekyllin, Astron ja muiden staattisten sivugeneraattoreiden kanssa.
{{% /details %}}

{{% details title="Paljonko OpenAI API maksaa tähän?" closed="true" %}}
Kustannus riippuu julkaisujesi määrästä ja pituudesta. Tyypillinen 50 artikkelin blogi maksaa muutaman dollarin API-käytössä GPT-4o:lla.
{{% /details %}}

{{% details title="Onko tämä työkalu avointa lähdekoodia?" closed="true" %}}
Kyllä. Täysi lähdekoodi on saatavilla [GitHubissa](https://github.com/everappz/wix-blog-export) avoimen lähdekoodin lisenssillä.
{{% /details %}}
