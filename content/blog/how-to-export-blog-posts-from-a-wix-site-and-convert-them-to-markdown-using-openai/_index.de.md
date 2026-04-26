---
title: "Wix-Blogbeiträge zu Markdown exportieren mit OpenAI"
date: 2025-06-24
description: "Automatisieren Sie den Wix-Blog-Export mit Python, Selenium und OpenAI. Extrahieren Sie dynamische Inhalte, laden Sie Bilder herunter und konvertieren Sie HTML in sauberes Markdown für Hugo oder Jekyll."
keywords: ["Wix Blog Export", "HTML zu Markdown konvertieren", "OpenAI Markdown-Konvertierung", "Wix zu Markdown", "SEO Blog-Migration", "Wix zu Hugo Migration", "BeautifulSoup Scraper", "Selenium HTML rendern", "OpenAI API Automatisierung", "Wix zu statischer Seite migrieren", "Wix Blog Scraper Python"]
tags: ["wix", "markdown", "Blog-Migration", "openai", "Scraping", "beautifulsoup", "selenium", "Automatisierung", "SEO", "Anleitung"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Warum Blogbeiträge von Wix exportieren?

**Zusammenfassung:** Diese Anleitung zeigt, wie Sie Wix-Blogbeiträge mit drei Python-Skripten zu Markdown exportieren: einem Setup-Runner, einem Selenium-basierten Scraper und einem OpenAI-gestützten HTML-zu-Markdown-Konverter. Das Ergebnis sind saubere, portable Markdown-Dateien, die für Hugo, Jekyll oder jeden anderen statischen Seitengenerator bereit sind.

Wix bietet keinen nativen Blog-Export in Markdown. Wenn Sie zu einem statischen Seitengenerator wie Hugo oder Jekyll migrieren, müssen Sie die gerenderten Seiten scrapen, den Inhalt extrahieren und konvertieren. Dieses Tutorial automatisiert den gesamten Prozess mit **Python, Selenium, BeautifulSoup** und **OpenAIs GPT API**.

Die Pipeline verwendet drei Skripte:

- `fetch_blog_posts.sh` — richtet die Umgebung ein und führt die Pipeline aus
- `parse_blog_sitemap.py` — rendert Seiten mit Selenium, extrahiert Inhalte, lädt Bilder herunter
- `generate_md.py` — konvertiert HTML zu Markdown über OpenAI

## Schritt 1: Umgebung einrichten

Erstellen Sie `fetch_blog_posts.sh` für Python-Prüfung, Einrichtung der virtuellen Umgebung, Abhängigkeitsinstallation und Pipeline-Ausführung.

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

## Schritt 2: Blog-Inhalte scrapen und extrahieren

`parse_blog_sitemap.py` erledigt die Hauptarbeit:

1. Ruft die Sitemap-XML ab, um alle Blog-URLs zu entdecken
2. Rendert jede Seite mit **Selenium** (erforderlich, da Wix Inhalte dynamisch lädt)
3. Extrahiert das `<div id="content-wrapper">` zur Isolierung des Artikelinhalts
4. Lädt alle Bilder lokal herunter und aktualisiert `src`-Attribute
5. Speichert das bereinigte HTML als `_index.html`
6. Ruft den Markdown-Konverter auf

**Warum Selenium statt requests?** Wix rendert Inhalte mit JavaScript. Eine einfache HTTP-Anfrage liefert eine leere Seitenhülle. Selenium führt einen headless Chrome-Browser aus, um das vollständig gerenderte HTML zu erhalten.

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
            except:
                pass
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
            except:
                pass

if __name__ == "__main__":
    parse_sitemap_and_process()
```

## Schritt 3: HTML zu Markdown mit OpenAI konvertieren

`generate_md.py` liest jede `_index.html`-Datei, sendet den Inhalt an die OpenAI Chat API und schreibt das resultierende Markdown.

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
    except:
        return ""

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

## Ausgabeordnerstruktur

Nach Ausführung der Pipeline erhält jeder Blogbeitrag einen eigenen Ordner:

```
downloads/
  your-post-title/
    _index.html      # Extrahiertes und bereinigtes HTML
    _index.md         # Konvertiertes Markdown
    image1.png        # Heruntergeladene Bilder
    image2.png
```

## OpenAI API-Schlüssel einrichten

Speichern Sie Ihren API-Schlüssel in einer Datei namens `OPENAI_API_KEY.TXT` im Skriptverzeichnis:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Die vollständige Pipeline ausführen

```bash
bash fetch_blog_posts.sh
```

Dieser einzelne Befehl richtet die Umgebung ein, scrapt alle Blogbeiträge aus der Sitemap, lädt Bilder herunter und konvertiert alles in Markdown.

## Zum Projekt beitragen

Das Projekt ist Open Source. Fehlerberichte, Funktionsvorschläge und Pull Requests sind willkommen.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Projekt auf GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Häufig gestellte Fragen

{{% details title="Warum kann ich nicht einfach `requests` verwenden, um Wix-Blogbeiträge zu scrapen?" closed="true" %}}
Wix rendert Inhalte dynamisch mit JavaScript. Eine Standard-HTTP-Anfrage gibt eine leere Seitenhülle zurück. Selenium führt einen Headless-Browser aus, um das vollständig gerenderte HTML zu erhalten.
{{% /details %}}

{{% details title="Funktioniert das mit jedem Wix-Blog?" closed="true" %}}
Ja. Der Scraper liest die Blog-Sitemap-XML und verarbeitet jede URL. Sie müssen nur die Variable `SITEMAP_URL` in `parse_blog_sitemap.py` aktualisieren, damit sie auf die Sitemap Ihrer Website zeigt.
{{% /details %}}

{{% details title="Welches OpenAI-Modell wird verwendet?" closed="true" %}}
Das Skript verwendet standardmäßig GPT-4o. Sie können die Variable `API_MODEL` in `generate_md.py` ändern, um ein anderes Modell zu verwenden.
{{% /details %}}

{{% details title="Kann ich das für die Migration von Wix zu Hugo verwenden?" closed="true" %}}
Ja. Die Ausgabe ist Standard-Markdown mit lokalen Bildpfaden, das direkt mit Hugo, Jekyll, Astro und anderen statischen Seitengeneratoren funktioniert. Fügen Sie Front Matter zu den generierten `_index.md`-Dateien hinzu, um die Migration abzuschließen.
{{% /details %}}

{{% details title="Wie viel kostet die OpenAI API dafür?" closed="true" %}}
Die Kosten hängen von der Anzahl und Länge Ihrer Blogbeiträge ab. Ein typischer Blog mit 50 Beiträgen mittlerer Länge kostet einige Dollar an API-Nutzung mit GPT-4o.
{{% /details %}}

{{% details title="Ist dieses Tool Open Source?" closed="true" %}}
Ja. Der vollständige Quellcode ist auf [GitHub](https://github.com/everappz/wix-blog-export) unter einer Open-Source-Lizenz verfügbar.
{{% /details %}}
