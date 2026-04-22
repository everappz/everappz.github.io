---
title: "ייצוא פוסטים מבלוג Wix ל-Markdown עם OpenAI"
date: 2025-06-24
description: "אוטומציה של ייצוא בלוג Wix באמצעות Python, Selenium ו-OpenAI. חילוץ תוכן דינמי, הורדת תמונות והמרת HTML ל-Markdown נקי עבור Hugo או Jekyll."
keywords: ["ייצוא בלוג Wix", "המרת HTML ל-markdown", "המרת markdown OpenAI", "wix ל-markdown", "הגירת בלוג SEO", "הגירת wix ל-hugo", "scraper beautifulsoup", "רינדור HTML selenium", "אוטומציית API OpenAI", "הגירת wix לאתר סטטי", "scraper בלוג wix python"]
tags: ["wix", "markdown", "הגירת בלוג", "openai", "scraping", "beautifulsoup", "selenium", "אוטומציה", "SEO", "מדריך"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## למה לייצא פוסטים מבלוג Wix?

**בקצרה:** מדריך זה מראה כיצד לייצא פוסטים מבלוג Wix ל-Markdown באמצעות שלושה סקריפטים של Python: מריץ הגדרות, scraper מבוסס Selenium וממיר HTML-ל-Markdown מופעל על ידי OpenAI. התוצאה היא קבצי Markdown נקיים וניידים מוכנים ל-Hugo, Jekyll או כל מחולל אתרים סטטי.

Wix אינו מציע ייצוא בלוג מקורי ל-Markdown. אם אתם מהגרים למחולל אתרים סטטי כמו Hugo או Jekyll, עליכם לגרד את הדפים המרונדרים, לחלץ את התוכן ולהמיר אותו. מדריך זה מאוטמט את כל התהליך באמצעות **Python, Selenium, BeautifulSoup** ו-**API GPT של OpenAI**.

הצינור משתמש בשלושה סקריפטים:

- `fetch_blog_posts.sh` — מגדיר את הסביבה ומריץ את הצינור
- `parse_blog_sitemap.py` — מרנדר דפים עם Selenium, מחלץ תוכן, מוריד תמונות
- `generate_md.py` — ממיר HTML ל-Markdown דרך OpenAI

## שלב 1: הגדרת הסביבה

צרו את `fetch_blog_posts.sh` לטיפול בבדיקות Python, הגדרת סביבה וירטואלית, התקנת תלויות והרצת הצינור.

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

## שלב 2: גרידה וחילוץ תוכן הבלוג

`parse_blog_sitemap.py` עושה את העבודה הקשה:

1. שולף את ה-XML של ה-sitemap כדי לגלות את כל כתובות URL של פוסטי הבלוג
2. מרנדר כל דף עם **Selenium** (נדרש כי Wix טוען תוכן באופן דינמי)
3. מחלץ את `<div id="content-wrapper">` כדי לבודד את תוכן המאמר
4. מוריד את כל התמונות מקומית ומעדכן את תכונות `src`
5. שומר את ה-HTML הנקי כ-`_index.html`
6. קורא לממיר ה-Markdown

**למה Selenium ולא requests?** Wix מרנדר תוכן עם JavaScript. בקשת HTTP פשוטה מחזירה מעטפת דף ריקה. Selenium מריץ דפדפן Chrome headless כדי לקבל את ה-HTML המרונדר במלואו.

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

## שלב 3: המרת HTML ל-Markdown עם OpenAI

`generate_md.py` קורא כל קובץ `_index.html`, שולח את התוכן ל-API Chat של OpenAI וכותב את ה-Markdown שנוצר.

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

## מבנה תיקיות הפלט

לאחר הרצת הצינור, כל פוסט בבלוג מקבל תיקייה משלו:

```
downloads/
  your-post-title/
    _index.html      # HTML מחולץ ונקי
    _index.md         # Markdown שהומר
    image1.png        # תמונות שהורדו
    image2.png
```

## הגדרת מפתח API של OpenAI

שמרו את מפתח ה-API שלכם בקובץ בשם `OPENAI_API_KEY.TXT` בספריית הסקריפט:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## הרצת הצינור המלא

```bash
bash fetch_blog_posts.sh
```

פקודה אחת זו מגדירה את הסביבה, גורדת את כל הפוסטים מה-sitemap, מורידה תמונות וממירה הכל ל-Markdown.

## תרומה לפרויקט

הפרויקט הוא קוד פתוח. דיווחי באגים, הצעות לתכונות ו-pull requests מתקבלים בברכה.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="פרויקט ב-GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## שאלות נפוצות

{{% details title="למה אני לא יכול פשוט להשתמש ב-`requests` כדי לגרד פוסטי בלוג Wix?" closed="true" %}}
Wix מרנדר תוכן באופן דינמי עם JavaScript. בקשת HTTP סטנדרטית מחזירה מעטפת דף ריקה. Selenium מריץ דפדפן headless כדי לקבל את ה-HTML המרונדר במלואו.
{{% /details %}}

{{% details title="האם זה עובד עם כל בלוג Wix?" closed="true" %}}
כן. ה-scraper קורא את ה-XML של ה-sitemap של הבלוג ומעבד כל URL. צריך רק לעדכן את המשתנה `SITEMAP_URL` ב-`parse_blog_sitemap.py` כדי להפנות ל-sitemap של האתר שלכם.
{{% /details %}}

{{% details title="באיזה מודל OpenAI זה משתמש?" closed="true" %}}
הסקריפט משתמש ב-GPT-4o כברירת מחדל. ניתן לשנות את המשתנה `API_MODEL` ב-`generate_md.py` כדי להשתמש במודל אחר.
{{% /details %}}

{{% details title="האם ניתן להשתמש בזה להגירה מ-Wix ל-Hugo?" closed="true" %}}
כן. הפלט הוא Markdown סטנדרטי עם נתיבי תמונות מקומיים, שעובד ישירות עם Hugo, Jekyll, Astro ומחוללי אתרים סטטיים אחרים. הוסיפו front matter לקבצי `_index.md` שנוצרו כדי להשלים את ההגירה.
{{% /details %}}

{{% details title="כמה עולה ה-API של OpenAI לזה?" closed="true" %}}
העלות תלויה במספר ובאורך הפוסטים בבלוג שלכם. בלוג טיפוסי עם 50 פוסטים באורך בינוני עולה כמה דולרים בשימוש API עם GPT-4o.
{{% /details %}}

{{% details title="האם הכלי הזה קוד פתוח?" closed="true" %}}
כן. קוד המקור המלא זמין ב-[GitHub](https://github.com/everappz/wix-blog-export) תחת רישיון קוד פתוח.
{{% /details %}}
