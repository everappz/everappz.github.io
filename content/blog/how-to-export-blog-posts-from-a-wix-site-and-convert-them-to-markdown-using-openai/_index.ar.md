---
title: "تصدير مقالات مدونة Wix إلى Markdown باستخدام OpenAI"
date: 2025-06-24
description: "أتمتة تصدير مدونة Wix باستخدام Python وSelenium وOpenAI. استخراج المحتوى الديناميكي، تحميل الصور، وتحويل HTML إلى Markdown نظيف لـ Hugo أو Jekyll."
keywords: ["تصدير مدونة Wix", "تحويل HTML إلى markdown", "تحويل OpenAI إلى markdown", "wix إلى markdown", "ترحيل مدونة SEO", "ترحيل wix إلى hugo", "أداة beautifulsoup", "عرض HTML بـ selenium", "أتمتة OpenAI API", "ترحيل wix إلى موقع ثابت", "أداة استخراج مدونة wix بـ python"]
tags: ["wix", "markdown", "ترحيل مدونة", "openai", "استخراج البيانات", "beautifulsoup", "selenium", "أتمتة", "SEO", "دليل تعليمي"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## لماذا تصدير مقالات المدونة من Wix؟

**ملخص:** يوضح هذا الدليل كيفية تصدير مقالات مدونة Wix إلى Markdown باستخدام ثلاثة نصوص Python: منفذ إعداد، أداة استخراج بـ Selenium، ومحول HTML إلى Markdown بواسطة OpenAI. النتيجة هي ملفات Markdown نظيفة وقابلة للنقل جاهزة لـ Hugo أو Jekyll أو أي منشئ مواقع ثابتة.

لا يوفر Wix تصديراً أصلياً للمدونة إلى Markdown. إذا كنت تنتقل إلى منشئ مواقع ثابتة مثل Hugo أو Jekyll، تحتاج إلى استخراج الصفحات المعروضة، واستخلاص المحتوى، وتحويله. يؤتمت هذا الدليل العملية بأكملها باستخدام **Python وSelenium وBeautifulSoup** و**OpenAI GPT API**.

يستخدم خط الأنابيب ثلاثة نصوص:

- `fetch_blog_posts.sh` — يُعد البيئة وينفذ خط الأنابيب
- `parse_blog_sitemap.py` — يعرض الصفحات بـ Selenium، يستخرج المحتوى، يحمّل الصور
- `generate_md.py` — يحول HTML إلى Markdown عبر OpenAI

## الخطوة 1: إعداد البيئة

أنشئ `fetch_blog_posts.sh` للتعامل مع فحص Python، إعداد البيئة الافتراضية، تثبيت التبعيات، وتنفيذ خط الأنابيب.

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

## الخطوة 2: استخراج محتوى المدونة

يقوم `parse_blog_sitemap.py` بالعمل الثقيل:

1. يجلب XML خريطة الموقع لاكتشاف جميع عناوين URL لمقالات المدونة
2. يعرض كل صفحة بـ **Selenium** (مطلوب لأن محتوى Wix يُحمّل ديناميكياً)
3. يستخرج `<div id="content-wrapper">` لعزل محتوى المقالة
4. يحمّل جميع الصور محلياً ويحدّث سمات `src`
5. يحفظ HTML المنظف كـ `_index.html`
6. يستدعي محول Markdown

**لماذا Selenium بدلاً من requests؟** يعرض Wix المحتوى بـ JavaScript. طلب HTTP بسيط يُرجع هيكل صفحة فارغاً. يشغل Selenium متصفح Chrome بدون واجهة للحصول على HTML المعروض بالكامل.

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

## الخطوة 3: تحويل HTML إلى Markdown بـ OpenAI

يقرأ `generate_md.py` كل ملف `_index.html`، يرسل المحتوى إلى Chat API الخاص بـ OpenAI، ويكتب Markdown الناتج.

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

## هيكل مجلد الإخراج

بعد تشغيل خط الأنابيب، يحصل كل مقال مدونة على مجلده الخاص:

```
downloads/
  your-post-title/
    _index.html      # HTML مستخرج ومنظف
    _index.md         # Markdown محول
    image1.png        # صور محملة
    image2.png
```

## إعداد مفتاح OpenAI API

احفظ مفتاح API الخاص بك في ملف يسمى `OPENAI_API_KEY.TXT` في مجلد النصوص:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## تشغيل خط الأنابيب الكامل

```bash
bash fetch_blog_posts.sh
```

هذا الأمر الواحد يُعد البيئة، يستخرج جميع مقالات المدونة من خريطة الموقع، يحمّل الصور، ويحول كل شيء إلى Markdown.

## المساهمة في المشروع

المشروع مفتوح المصدر. تقارير الأخطاء واقتراحات الميزات وطلبات السحب مرحب بها.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="المشروع على GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## الأسئلة الشائعة

{{% details title="لماذا لا يمكنني استخدام `requests` لاستخراج مقالات مدونة Wix؟" closed="true" %}}
يعرض Wix المحتوى ديناميكياً بـ JavaScript. طلب HTTP عادي يُرجع هيكل صفحة فارغاً. يشغل Selenium متصفحاً بدون واجهة للحصول على HTML المعروض بالكامل.
{{% /details %}}

{{% details title="هل يعمل هذا مع أي مدونة Wix؟" closed="true" %}}
نعم. يقرأ المستخرج XML خريطة الموقع ويعالج كل عنوان URL. تحتاج فقط إلى تحديث متغير `SITEMAP_URL` في `parse_blog_sitemap.py` للإشارة إلى خريطة موقعك.
{{% /details %}}

{{% details title="أي نموذج OpenAI يستخدمه هذا؟" closed="true" %}}
يستخدم النص GPT-4o افتراضياً. يمكنك تغيير متغير `API_MODEL` في `generate_md.py` لاستخدام نموذج مختلف.
{{% /details %}}

{{% details title="هل يمكنني استخدام هذا للانتقال من Wix إلى Hugo؟" closed="true" %}}
نعم. الإخراج هو Markdown قياسي مع مسارات صور محلية، يعمل مباشرة مع Hugo وJekyll وAstro ومنشئات المواقع الثابتة الأخرى. أضف front matter إلى ملفات `_index.md` المولدة لإكمال الترحيل.
{{% /details %}}

{{% details title="كم يكلف استخدام OpenAI API لهذا؟" closed="true" %}}
تعتمد التكلفة على عدد وطول مقالات مدونتك. مدونة نموذجية تحتوي على 50 مقالاً بطول معتدل تكلف بضعة دولارات في استخدام API مع GPT-4o.
{{% /details %}}

{{% details title="هل هذه الأداة مفتوحة المصدر؟" closed="true" %}}
نعم. الكود المصدري الكامل متاح على [GitHub](https://github.com/everappz/wix-blog-export) بموجب ترخيص مفتوح المصدر.
{{% /details %}}
