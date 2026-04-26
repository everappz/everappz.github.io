---
title: "ส่งออกบล็อกโพสต์ Wix เป็น Markdown ด้วย OpenAI"
date: 2025-06-24
description: "อัตโนมัติการส่งออกบล็อก Wix โดยใช้ Python, Selenium และ OpenAI แยกเนื้อหาแบบไดนามิก ดาวน์โหลดรูปภาพ และแปลง HTML เป็น Markdown สำหรับ Hugo หรือ Jekyll"
keywords: ["ส่งออกบล็อก Wix", "แปลง HTML เป็น markdown", "OpenAI แปลง markdown", "wix เป็น markdown", "ย้ายบล็อก SEO", "ย้าย wix เป็น hugo", "beautifulsoup scraper", "selenium เรนเดอร์ HTML", "OpenAI API อัตโนมัติ", "ย้าย wix เป็นเว็บไซต์แบบสถิต", "wix blog scraper python"]
tags: ["wix", "markdown", "ย้ายบล็อก", "openai", "scraping", "beautifulsoup", "selenium", "อัตโนมัติ", "SEO", "บทเรียน"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## ทำไมต้องส่งออกบล็อกโพสต์จาก Wix?

**สรุป:** คู่มือนี้แสดงวิธีส่งออกบล็อกโพสต์ Wix เป็น Markdown โดยใช้สคริปต์ Python สามตัว: ตัวเรียกใช้การตั้งค่า, scraper ที่ใช้ Selenium และตัวแปลง HTML เป็น Markdown ที่ขับเคลื่อนด้วย OpenAI ผลลัพธ์คือไฟล์ Markdown ที่สะอาดและพกพาได้ พร้อมสำหรับ Hugo, Jekyll หรือตัวสร้างเว็บไซต์แบบสถิตใดๆ

Wix ไม่มีการส่งออกบล็อกเป็น Markdown แบบดั้งเดิม หากคุณกำลังย้ายไปยังตัวสร้างเว็บไซต์แบบสถิตเช่น Hugo หรือ Jekyll คุณต้อง scrape หน้าที่เรนเดอร์แล้ว แยกเนื้อหา และแปลงมัน บทเรียนนี้ทำให้กระบวนการทั้งหมดเป็นอัตโนมัติโดยใช้ **Python, Selenium, BeautifulSoup** และ **OpenAI GPT API**

Pipeline ใช้สคริปต์สามตัว:

- `fetch_blog_posts.sh` — ตั้งค่าสภาพแวดล้อมและเรียกใช้ pipeline
- `parse_blog_sitemap.py` — เรนเดอร์หน้าด้วย Selenium, แยกเนื้อหา, ดาวน์โหลดรูปภาพ
- `generate_md.py` — แปลง HTML เป็น Markdown ผ่าน OpenAI

## ขั้นตอนที่ 1: ตั้งค่าสภาพแวดล้อม

สร้าง `fetch_blog_posts.sh` เพื่อจัดการการตรวจสอบ Python, การตั้งค่า virtual environment, การติดตั้ง dependencies และการเรียกใช้ pipeline

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

## ขั้นตอนที่ 2: Scrape และแยกเนื้อหาบล็อก

`parse_blog_sitemap.py` ทำงานหนัก:

1. ดึง sitemap XML เพื่อค้นหา URL ของบล็อกโพสต์ทั้งหมด
2. เรนเดอร์แต่ละหน้าด้วย **Selenium** (จำเป็นเพราะเนื้อหา Wix โหลดแบบไดนามิก)
3. แยก `<div id="content-wrapper">` เพื่อแยกเนื้อหาบทความ
4. ดาวน์โหลดรูปภาพทั้งหมดไว้ในเครื่องและอัปเดตแอตทริบิวต์ `src`
5. บันทึก HTML ที่ทำความสะอาดแล้วเป็น `_index.html`
6. เรียกตัวแปลง Markdown

**ทำไมต้อง Selenium แทน requests?** Wix เรนเดอร์เนื้อหาด้วย JavaScript คำขอ HTTP แบบง่ายจะส่งคืนหน้าเปล่า Selenium เรียกใช้เบราว์เซอร์ Chrome แบบ headless เพื่อให้ได้ HTML ที่เรนเดอร์สมบูรณ์

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

## ขั้นตอนที่ 3: แปลง HTML เป็น Markdown ด้วย OpenAI

`generate_md.py` อ่านไฟล์ `_index.html` แต่ละไฟล์ ส่งเนื้อหาไปยัง OpenAI Chat API และเขียน Markdown ที่ได้

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

## โครงสร้างโฟลเดอร์ผลลัพธ์

หลังจากเรียกใช้ pipeline บล็อกโพสต์แต่ละรายการจะได้โฟลเดอร์ของตัวเอง:

```
downloads/
  your-post-title/
    _index.html      # HTML ที่แยกและทำความสะอาดแล้ว
    _index.md         # Markdown ที่แปลงแล้ว
    image1.png        # รูปภาพที่ดาวน์โหลด
    image2.png
```

## การตั้งค่า OpenAI API Key

บันทึก API key ของคุณในไฟล์ชื่อ `OPENAI_API_KEY.TXT` ในไดเรกทอรีสคริปต์:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## เรียกใช้ Pipeline ทั้งหมด

```bash
bash fetch_blog_posts.sh
```

คำสั่งเดียวนี้ตั้งค่าสภาพแวดล้อม scrape บล็อกโพสต์ทั้งหมดจาก sitemap ดาวน์โหลดรูปภาพ และแปลงทุกอย่างเป็น Markdown

## มีส่วนร่วมกับโปรเจกต์

โปรเจกต์นี้เป็น open source ยินดีรับรายงานข้อบกพร่อง ข้อเสนอแนะฟีเจอร์ และ pull request

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="โปรเจกต์บน GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## คำถามที่พบบ่อย

{{% details title="ทำไมฉันไม่สามารถใช้ `requests` เพื่อ scrape บล็อกโพสต์ Wix ได้?" closed="true" %}}
Wix เรนเดอร์เนื้อหาแบบไดนามิกด้วย JavaScript คำขอ HTTP มาตรฐานจะส่งคืนหน้าเปล่า Selenium เรียกใช้เบราว์เซอร์แบบ headless เพื่อให้ได้ HTML ที่เรนเดอร์สมบูรณ์
{{% /details %}}

{{% details title="ใช้ได้กับบล็อก Wix ทุกบล็อกหรือไม่?" closed="true" %}}
ใช่ Scraper อ่าน sitemap XML ของบล็อกและประมวลผลแต่ละ URL คุณเพียงแค่ต้องอัปเดตตัวแปร `SITEMAP_URL` ใน `parse_blog_sitemap.py` ให้ชี้ไปยัง sitemap ของเว็บไซต์คุณ
{{% /details %}}

{{% details title="ใช้โมเดล OpenAI ตัวไหน?" closed="true" %}}
สคริปต์ใช้ GPT-4o เป็นค่าเริ่มต้น คุณสามารถเปลี่ยนตัวแปร `API_MODEL` ใน `generate_md.py` เพื่อใช้โมเดลอื่น
{{% /details %}}

{{% details title="ฉันสามารถใช้สิ่งนี้เพื่อย้ายจาก Wix ไป Hugo ได้หรือไม่?" closed="true" %}}
ได้ ผลลัพธ์เป็น Markdown มาตรฐานพร้อมเส้นทางรูปภาพในเครื่อง ซึ่งใช้ได้โดยตรงกับ Hugo, Jekyll, Astro และตัวสร้างเว็บไซต์แบบสถิตอื่นๆ เพิ่ม front matter ให้ไฟล์ `_index.md` ที่สร้างขึ้นเพื่อทำการย้ายให้เสร็จสมบูรณ์
{{% /details %}}

{{% details title="OpenAI API สำหรับสิ่งนี้มีค่าใช้จ่ายเท่าไหร่?" closed="true" %}}
ค่าใช้จ่ายขึ้นอยู่กับจำนวนและความยาวของบล็อกโพสต์ บล็อกทั่วไปที่มี 50 โพสต์ความยาวปานกลางจะมีค่าใช้จ่ายไม่กี่ดอลลาร์ในการใช้ API กับ GPT-4o
{{% /details %}}

{{% details title="เครื่องมือนี้เป็น open source หรือไม่?" closed="true" %}}
ใช่ ซอร์สโค้ดทั้งหมดมีอยู่บน [GitHub](https://github.com/everappz/wix-blog-export) ภายใต้สัญญาอนุญาต open source
{{% /details %}}
