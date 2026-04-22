---
title: "Експорт блог-постів Wix у Markdown за допомогою OpenAI"
date: 2025-06-24
description: "Автоматизуйте експорт блогу Wix за допомогою Python, Selenium та OpenAI. Витягніть динамічний контент, завантажте зображення та конвертуйте HTML у чистий Markdown для Hugo або Jekyll."
keywords: ["експорт блогу Wix", "конвертація HTML у markdown", "OpenAI конвертація markdown", "wix у markdown", "міграція SEO блогу", "міграція wix у hugo", "beautifulsoup scraper", "selenium рендеринг HTML", "OpenAI API автоматизація", "міграція wix на статичний сайт", "wix blog scraper python"]
tags: ["wix", "markdown", "міграція блогу", "openai", "scraping", "beautifulsoup", "selenium", "автоматизація", "SEO", "посібник"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Навіщо експортувати блог-пости з Wix?

**Підсумок:** Цей посібник показує, як експортувати блог-пости Wix у Markdown за допомогою трьох Python-скриптів: запускач налаштування, scraper на базі Selenium та конвертер HTML у Markdown на базі OpenAI. Результат — чисті, портативні файли Markdown, готові для Hugo, Jekyll або будь-якого генератора статичних сайтів.

Wix не пропонує нативного експорту блогу в Markdown. Якщо ви мігруєте на генератор статичних сайтів як Hugo або Jekyll, вам потрібно зібрати відрендерені сторінки, витягнути контент і конвертувати його. Цей посібник автоматизує весь процес за допомогою **Python, Selenium, BeautifulSoup** та **OpenAI GPT API**.

Pipeline використовує три скрипти:

- `fetch_blog_posts.sh` — налаштовує середовище та запускає pipeline
- `parse_blog_sitemap.py` — рендерить сторінки за допомогою Selenium, витягує контент, завантажує зображення
- `generate_md.py` — конвертує HTML у Markdown через OpenAI

## Крок 1: Налаштування середовища

Створіть `fetch_blog_posts.sh` для обробки перевірки Python, налаштування віртуального середовища, встановлення залежностей та запуску pipeline.

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

## Крок 2: Збір та витягнення контенту блогу

`parse_blog_sitemap.py` виконує основну роботу:

1. Отримує sitemap XML для виявлення всіх URL блог-постів
2. Рендерить кожну сторінку за допомогою **Selenium** (потрібно, оскільки контент Wix завантажується динамічно)
3. Витягує `<div id="content-wrapper">` для ізоляції контенту статті
4. Завантажує всі зображення локально та оновлює атрибути `src`
5. Зберігає очищений HTML як `_index.html`
6. Викликає конвертер Markdown

**Чому Selenium замість requests?** Wix рендерить контент за допомогою JavaScript. Простий HTTP-запит повертає порожню оболонку сторінки. Selenium запускає headless браузер Chrome для отримання повністю відрендереного HTML.

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

## Крок 3: Конвертація HTML у Markdown за допомогою OpenAI

`generate_md.py` читає кожен файл `_index.html`, надсилає контент до OpenAI Chat API та записує результат у Markdown.

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

## Структура вихідних папок

Після запуску pipeline кожен блог-пост отримує власну папку:

```
downloads/
  your-post-title/
    _index.html      # Витягнутий та очищений HTML
    _index.md         # Конвертований Markdown
    image1.png        # Завантажені зображення
    image2.png
```

## Налаштування ключа OpenAI API

Збережіть ваш API ключ у файлі `OPENAI_API_KEY.TXT` у директорії скриптів:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Запуск повного pipeline

```bash
bash fetch_blog_posts.sh
```

Ця єдина команда налаштовує середовище, збирає всі блог-пости із sitemap, завантажує зображення та конвертує все в Markdown.

## Долучайтесь до проєкту

Проєкт є відкритим. Звіти про помилки, пропозиції функцій та pull request вітаються.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Проєкт на GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Часті запитання

{{% details title="Чому я не можу просто використати `requests` для збору блог-постів Wix?" closed="true" %}}
Wix рендерить контент динамічно за допомогою JavaScript. Стандартний HTTP-запит повертає порожню оболонку сторінки. Selenium запускає headless браузер для отримання повністю відрендереного HTML.
{{% /details %}}

{{% details title="Це працює з будь-яким блогом на Wix?" closed="true" %}}
Так. Scraper читає sitemap XML блогу та обробляє кожну URL. Вам потрібно лише оновити змінну `SITEMAP_URL` в `parse_blog_sitemap.py`, щоб вона вказувала на sitemap вашого сайту.
{{% /details %}}

{{% details title="Яку модель OpenAI це використовує?" closed="true" %}}
Скрипт за замовчуванням використовує GPT-4o. Ви можете змінити змінну `API_MODEL` в `generate_md.py` для використання іншої моделі.
{{% /details %}}

{{% details title="Чи можу я використати це для міграції з Wix на Hugo?" closed="true" %}}
Так. Вихідні дані — це стандартний Markdown з локальними шляхами до зображень, який працює безпосередньо з Hugo, Jekyll, Astro та іншими генераторами статичних сайтів. Додайте front matter до згенерованих файлів `_index.md` для завершення міграції.
{{% /details %}}

{{% details title="Скільки коштує OpenAI API для цього?" closed="true" %}}
Вартість залежить від кількості та довжини ваших блог-постів. Типовий блог з 50 постами середньої довжини коштує кілька доларів за використання API з GPT-4o.
{{% /details %}}

{{% details title="Цей інструмент з відкритим кодом?" closed="true" %}}
Так. Повний вихідний код доступний на [GitHub](https://github.com/everappz/wix-blog-export) під ліцензією з відкритим кодом.
{{% /details %}}
