---
title: "Экспорт постов блога Wix в Markdown с помощью OpenAI"
date: 2025-06-24
description: "Автоматизируйте экспорт блога Wix с помощью Python, Selenium и OpenAI. Извлекайте динамический контент, загружайте изображения и конвертируйте HTML в чистый Markdown для Hugo или Jekyll."
keywords: ["экспорт блога Wix", "конвертация HTML в markdown", "конвертация markdown OpenAI", "wix в markdown", "миграция блога SEO", "миграция wix в hugo", "скрапер beautifulsoup", "рендеринг HTML selenium", "автоматизация API OpenAI", "миграция wix на статический сайт", "скрапер блога wix python"]
tags: ["wix", "markdown", "миграция блога", "openai", "скрапинг", "beautifulsoup", "selenium", "автоматизация", "SEO", "руководство"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Зачем Экспортировать Посты Блога из Wix?

**Кратко:** Это руководство показывает, как экспортировать посты блога Wix в Markdown с помощью трёх Python-скриптов: запускатель настройки, скрапер на базе Selenium и конвертер HTML-в-Markdown на базе OpenAI. Результат — чистые, портативные файлы Markdown, готовые для Hugo, Jekyll или любого генератора статических сайтов.

Wix не предлагает нативного экспорта блога в Markdown. Если вы мигрируете на генератор статических сайтов вроде Hugo или Jekyll, вам нужно скрапить отрендеренные страницы, извлечь контент и конвертировать его. Этот туториал автоматизирует весь процесс с помощью **Python, Selenium, BeautifulSoup** и **GPT API OpenAI**.

Конвейер использует три скрипта:

- `fetch_blog_posts.sh` — настраивает окружение и запускает конвейер
- `parse_blog_sitemap.py` — рендерит страницы с помощью Selenium, извлекает контент, загружает изображения
- `generate_md.py` — конвертирует HTML в Markdown через OpenAI

## Шаг 1: Настройка Окружения

Создайте `fetch_blog_posts.sh` для проверки Python, настройки виртуального окружения, установки зависимостей и запуска конвейера.

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

## Шаг 2: Скрапинг и Извлечение Контента Блога

`parse_blog_sitemap.py` выполняет основную работу:

1. Получает XML карты сайта для обнаружения всех URL постов блога
2. Рендерит каждую страницу с помощью **Selenium** (необходимо, так как контент Wix загружается динамически)
3. Извлекает `<div id="content-wrapper">` для изоляции контента статьи
4. Загружает все изображения локально и обновляет атрибуты `src`
5. Сохраняет очищенный HTML как `_index.html`
6. Вызывает конвертер Markdown

**Почему Selenium, а не requests?** Wix рендерит контент с помощью JavaScript. Простой HTTP-запрос возвращает пустую оболочку страницы. Selenium запускает безголовый браузер Chrome для получения полностью отрендеренного HTML.

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

## Шаг 3: Конвертация HTML в Markdown с OpenAI

`generate_md.py` читает каждый файл `_index.html`, отправляет контент в Chat API OpenAI и записывает результирующий Markdown.

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

## Структура Выходных Папок

После запуска конвейера каждый пост блога получает свою папку:

```
downloads/
  your-post-title/
    _index.html      # Извлечённый и очищенный HTML
    _index.md         # Конвертированный Markdown
    image1.png        # Загруженные изображения
    image2.png
```

## Настройка Ключа API OpenAI

Сохраните ваш API ключ в файле `OPENAI_API_KEY.TXT` в директории скрипта:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Запуск Полного Конвейера

```bash
bash fetch_blog_posts.sh
```

Эта единственная команда настраивает окружение, скрапит все посты блога из карты сайта, загружает изображения и конвертирует всё в Markdown.

## Внесите Вклад в Проект

Проект с открытым исходным кодом. Отчёты об ошибках, предложения функций и pull request-ы приветствуются.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Проект на GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Часто Задаваемые Вопросы

{{% details title="Почему нельзя просто использовать `requests` для скрапинга постов блога Wix?" closed="true" %}}
Wix рендерит контент динамически с помощью JavaScript. Стандартный HTTP-запрос возвращает пустую оболочку страницы. Selenium запускает безголовый браузер для получения полностью отрендеренного HTML.
{{% /details %}}

{{% details title="Это работает с любым блогом Wix?" closed="true" %}}
Да. Скрапер читает XML карты сайта блога и обрабатывает каждый URL. Вам нужно только обновить переменную `SITEMAP_URL` в `parse_blog_sitemap.py`, указав на карту сайта вашего сайта.
{{% /details %}}

{{% details title="Какую модель OpenAI это использует?" closed="true" %}}
Скрипт использует GPT-4o по умолчанию. Вы можете изменить переменную `API_MODEL` в `generate_md.py` для использования другой модели.
{{% /details %}}

{{% details title="Можно ли использовать это для миграции с Wix на Hugo?" closed="true" %}}
Да. Выходные данные — стандартный Markdown с локальными путями к изображениям, который работает напрямую с Hugo, Jekyll, Astro и другими генераторами статических сайтов. Добавьте front matter в сгенерированные файлы `_index.md` для завершения миграции.
{{% /details %}}

{{% details title="Сколько стоит API OpenAI для этого?" closed="true" %}}
Стоимость зависит от количества и длины ваших постов. Типичный блог с 50 постами средней длины обходится в несколько долларов за использование API с GPT-4o.
{{% /details %}}

{{% details title="Этот инструмент с открытым исходным кодом?" closed="true" %}}
Да. Полный исходный код доступен на [GitHub](https://github.com/everappz/wix-blog-export) под открытой лицензией.
{{% /details %}}
