---
title: "Exporter les articles de blog Wix en Markdown avec OpenAI"
date: 2025-06-24
description: "Automatisez l'export de blog Wix avec Python, Selenium et OpenAI. Extrayez le contenu dynamique, téléchargez les images et convertissez le HTML en Markdown propre pour Hugo ou Jekyll."
keywords: ["export blog Wix", "convertir HTML en markdown", "conversion markdown OpenAI", "wix vers markdown", "migration blog SEO", "migration wix vers hugo", "scraper beautifulsoup", "rendu HTML selenium", "automatisation API OpenAI", "migrer wix vers site statique", "scraper blog wix python"]
tags: ["wix", "markdown", "migration de blog", "openai", "scraping", "beautifulsoup", "selenium", "automatisation", "SEO", "tutoriel"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Pourquoi exporter les articles de blog depuis Wix ?

**En bref :** Ce guide montre comment exporter les articles de blog Wix en Markdown à l'aide de trois scripts Python : un lanceur de configuration, un scraper basé sur Selenium et un convertisseur HTML-vers-Markdown alimenté par OpenAI. Le résultat est des fichiers Markdown propres et portables, prêts pour Hugo, Jekyll ou tout générateur de site statique.

Wix ne propose pas d'export natif de blog en Markdown. Si vous migrez vers un générateur de site statique comme Hugo ou Jekyll, vous devez scraper les pages rendues, extraire le contenu et le convertir. Ce tutoriel automatise l'ensemble du processus en utilisant **Python, Selenium, BeautifulSoup** et l'**API GPT d'OpenAI**.

Le pipeline utilise trois scripts :

- `fetch_blog_posts.sh` — configure l'environnement et lance le pipeline
- `parse_blog_sitemap.py` — rend les pages avec Selenium, extrait le contenu, télécharge les images
- `generate_md.py` — convertit le HTML en Markdown via OpenAI

## Étape 1 : Configurer l'environnement

Créez `fetch_blog_posts.sh` pour gérer les vérifications Python, la configuration de l'environnement virtuel, l'installation des dépendances et l'exécution du pipeline.

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

## Étape 2 : Scraper et extraire le contenu du blog

`parse_blog_sitemap.py` fait le gros du travail :

1. Récupère le XML du sitemap pour découvrir toutes les URL des articles de blog
2. Rend chaque page avec **Selenium** (nécessaire car Wix charge le contenu dynamiquement)
3. Extrait le `<div id="content-wrapper">` pour isoler le contenu de l'article
4. Télécharge toutes les images localement et met à jour les attributs `src`
5. Sauvegarde le HTML nettoyé en tant que `_index.html`
6. Appelle le convertisseur Markdown

**Pourquoi Selenium plutôt que requests ?** Wix rend le contenu avec JavaScript. Une simple requête HTTP renvoie une coquille vide. Selenium exécute un navigateur Chrome headless pour obtenir le HTML entièrement rendu.

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

## Étape 3 : Convertir le HTML en Markdown avec OpenAI

`generate_md.py` lit chaque fichier `_index.html`, envoie le contenu à l'API Chat d'OpenAI et écrit le Markdown résultant.

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

## Structure des dossiers de sortie

Après l'exécution du pipeline, chaque article de blog obtient son propre dossier :

```
downloads/
  your-post-title/
    _index.html      # HTML extrait et nettoyé
    _index.md         # Markdown converti
    image1.png        # Images téléchargées
    image2.png
```

## Configuration de la clé API OpenAI

Sauvegardez votre clé API dans un fichier appelé `OPENAI_API_KEY.TXT` dans le répertoire du script :

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Lancer le pipeline complet

```bash
bash fetch_blog_posts.sh
```

Cette seule commande configure l'environnement, scrape tous les articles du sitemap, télécharge les images et convertit tout en Markdown.

## Contribuer au projet

Le projet est open source. Les rapports de bugs, suggestions de fonctionnalités et pull requests sont les bienvenus.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Projet sur GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Questions fréquemment posées

{{% details title="Pourquoi ne puis-je pas simplement utiliser `requests` pour scraper les articles Wix ?" closed="true" %}}
Wix rend le contenu dynamiquement avec JavaScript. Une requête HTTP standard renvoie une coquille de page vide. Selenium exécute un navigateur headless pour obtenir le HTML entièrement rendu.
{{% /details %}}

{{% details title="Cela fonctionne-t-il avec n'importe quel blog Wix ?" closed="true" %}}
Oui. Le scraper lit le XML du sitemap du blog et traite chaque URL. Il suffit de mettre à jour la variable `SITEMAP_URL` dans `parse_blog_sitemap.py` pour pointer vers le sitemap de votre site.
{{% /details %}}

{{% details title="Quel modèle OpenAI est utilisé ?" closed="true" %}}
Le script utilise GPT-4o par défaut. Vous pouvez changer la variable `API_MODEL` dans `generate_md.py` pour utiliser un modèle différent.
{{% /details %}}

{{% details title="Puis-je utiliser ceci pour migrer de Wix vers Hugo ?" closed="true" %}}
Oui. La sortie est du Markdown standard avec des chemins d'images locaux, qui fonctionne directement avec Hugo, Jekyll, Astro et d'autres générateurs de sites statiques. Ajoutez le front matter aux fichiers `_index.md` générés pour compléter la migration.
{{% /details %}}

{{% details title="Combien coûte l'API OpenAI pour cela ?" closed="true" %}}
Le coût dépend du nombre et de la longueur de vos articles de blog. Un blog typique avec 50 articles de longueur moyenne coûte quelques dollars en utilisation de l'API avec GPT-4o.
{{% /details %}}

{{% details title="Cet outil est-il open source ?" closed="true" %}}
Oui. Le code source complet est disponible sur [GitHub](https://github.com/everappz/wix-blog-export) sous une licence open source.
{{% /details %}}
