---
title: "Εξαγωγή άρθρων blog από Wix σε Markdown με OpenAI"
date: 2025-06-24
description: "Αυτοματοποιήστε την εξαγωγή blog Wix με Python, Selenium και OpenAI. Εξαγάγετε δυναμικό περιεχόμενο, κατεβάστε εικόνες και μετατρέψτε HTML σε καθαρό Markdown για Hugo ή Jekyll."
keywords: ["εξαγωγή blog Wix", "μετατροπή HTML σε markdown", "μετατροπή OpenAI σε markdown", "wix σε markdown", "μετάβαση blog SEO", "μετάβαση wix σε hugo", "scraper beautifulsoup", "απόδοση HTML με selenium", "αυτοματοποίηση OpenAI API", "μετάβαση wix σε στατικό site", "scraper blog wix python"]
tags: ["wix", "markdown", "μετάβαση blog", "openai", "scraping", "beautifulsoup", "selenium", "αυτοματοποίηση", "SEO", "οδηγός"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Γιατί να εξαγάγετε άρθρα blog από το Wix;

**Περίληψη:** Αυτός ο οδηγός δείχνει πώς να εξάγετε άρθρα blog Wix σε Markdown χρησιμοποιώντας τρία scripts Python: ένα πρόγραμμα εκτέλεσης εγκατάστασης, ένα scraper βασισμένο σε Selenium και έναν μετατροπέα HTML σε Markdown με OpenAI. Το αποτέλεσμα είναι καθαρά, φορητά αρχεία Markdown έτοιμα για Hugo, Jekyll ή οποιονδήποτε γεννήτρια στατικών σελίδων.

Το Wix δεν προσφέρει εγγενή εξαγωγή blog σε Markdown. Αν μεταβαίνετε σε γεννήτρια στατικών σελίδων όπως Hugo ή Jekyll, χρειάζεται να εξαγάγετε τις αποδιδόμενες σελίδες, να εξάγετε το περιεχόμενο και να το μετατρέψετε. Αυτός ο οδηγός αυτοματοποιεί ολόκληρη τη διαδικασία χρησιμοποιώντας **Python, Selenium, BeautifulSoup** και **OpenAI GPT API**.

Η pipeline χρησιμοποιεί τρία scripts:

- `fetch_blog_posts.sh` — ρυθμίζει το περιβάλλον και εκτελεί την pipeline
- `parse_blog_sitemap.py` — αποδίδει σελίδες με Selenium, εξάγει περιεχόμενο, κατεβάζει εικόνες
- `generate_md.py` — μετατρέπει HTML σε Markdown μέσω OpenAI

## Βήμα 1: Ρύθμιση περιβάλλοντος

Δημιουργήστε `fetch_blog_posts.sh` για τη διαχείριση ελέγχου Python, ρύθμιση εικονικού περιβάλλοντος, εγκατάσταση εξαρτήσεων και εκτέλεση pipeline.

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

## Βήμα 2: Εξαγωγή περιεχομένου blog

Το `parse_blog_sitemap.py` κάνει τη βαριά δουλειά:

1. Ανακτά το XML του sitemap για να ανακαλύψει όλα τα URL άρθρων
2. Αποδίδει κάθε σελίδα με **Selenium** (απαιτείται γιατί το Wix φορτώνει περιεχόμενο δυναμικά)
3. Εξάγει το `<div id="content-wrapper">` για απομόνωση του περιεχομένου
4. Κατεβάζει όλες τις εικόνες τοπικά και ενημερώνει τα χαρακτηριστικά `src`
5. Αποθηκεύει το καθαρισμένο HTML ως `_index.html`
6. Καλεί τον μετατροπέα Markdown

**Γιατί Selenium αντί για requests;** Το Wix αποδίδει περιεχόμενο με JavaScript. Ένα απλό HTTP αίτημα επιστρέφει ένα κενό σκελετό σελίδας. Το Selenium εκτελεί ένα headless πρόγραμμα περιήγησης Chrome για να λάβει το πλήρως αποδοθέν HTML.

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

## Βήμα 3: Μετατροπή HTML σε Markdown με OpenAI

Το `generate_md.py` διαβάζει κάθε αρχείο `_index.html`, στέλνει το περιεχόμενο στο Chat API της OpenAI και γράφει το Markdown αποτέλεσμα.

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

## Δομή φακέλων εξόδου

Μετά την εκτέλεση της pipeline, κάθε άρθρο blog αποκτά τον δικό του φάκελο:

```
downloads/
  your-post-title/
    _index.html      # Εξαγμένο και καθαρισμένο HTML
    _index.md         # Μετατραπέν Markdown
    image1.png        # Λήψη εικόνων
    image2.png
```

## Ρύθμιση κλειδιού OpenAI API

Αποθηκεύστε το κλειδί API σας σε αρχείο `OPENAI_API_KEY.TXT` στον κατάλογο scripts:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Εκτέλεση πλήρους pipeline

```bash
bash fetch_blog_posts.sh
```

Αυτή η μοναδική εντολή ρυθμίζει το περιβάλλον, εξάγει όλα τα άρθρα blog από το sitemap, κατεβάζει εικόνες και μετατρέπει τα πάντα σε Markdown.

## Συμβάλετε στο έργο

Το έργο είναι ανοιχτού κώδικα. Αναφορές σφαλμάτων, προτάσεις χαρακτηριστικών και pull requests είναι ευπρόσδεκτα.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Έργο στο GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Συχνές ερωτήσεις

{{% details title="Γιατί δεν μπορώ απλά να χρησιμοποιήσω `requests` για scraping άρθρων Wix;" closed="true" %}}
Το Wix αποδίδει περιεχόμενο δυναμικά με JavaScript. Ένα τυπικό HTTP αίτημα επιστρέφει κενό σκελετό σελίδας. Το Selenium εκτελεί headless browser για πλήρως αποδοθέν HTML.
{{% /details %}}

{{% details title="Λειτουργεί με οποιοδήποτε blog Wix;" closed="true" %}}
Ναι. Ο scraper διαβάζει το XML sitemap και επεξεργάζεται κάθε URL. Χρειάζεται μόνο να ενημερώσετε τη μεταβλητή `SITEMAP_URL` στο `parse_blog_sitemap.py`.
{{% /details %}}

{{% details title="Ποιο μοντέλο OpenAI χρησιμοποιεί;" closed="true" %}}
Το script χρησιμοποιεί GPT-4o ως προεπιλογή. Μπορείτε να αλλάξετε τη μεταβλητή `API_MODEL` στο `generate_md.py`.
{{% /details %}}

{{% details title="Μπορώ να το χρησιμοποιήσω για μετάβαση από Wix σε Hugo;" closed="true" %}}
Ναι. Η έξοδος είναι τυπικό Markdown με τοπικές διαδρομές εικόνων, που λειτουργεί απευθείας με Hugo, Jekyll, Astro και άλλες γεννήτριες στατικών σελίδων.
{{% /details %}}

{{% details title="Πόσο κοστίζει το OpenAI API;" closed="true" %}}
Το κόστος εξαρτάται από τον αριθμό και το μέγεθος των άρθρων σας. Ένα τυπικό blog με 50 άρθρα κοστίζει λίγα δολάρια με GPT-4o.
{{% /details %}}

{{% details title="Είναι αυτό το εργαλείο ανοιχτού κώδικα;" closed="true" %}}
Ναι. Ο πλήρης πηγαίος κώδικας είναι διαθέσιμος στο [GitHub](https://github.com/everappz/wix-blog-export).
{{% /details %}}
