---
title: "Eksport Catatan Blog Wix ke Markdown dengan OpenAI"
date: 2025-06-24
description: "Automatikkan eksport blog Wix menggunakan Python, Selenium dan OpenAI. Ekstrak kandungan dinamik, muat turun imej, dan tukar HTML kepada Markdown bersih untuk Hugo atau Jekyll."
keywords: ["eksport blog Wix", "tukar HTML ke markdown", "penukaran markdown OpenAI", "wix ke markdown", "migrasi blog SEO", "migrasi wix ke hugo", "pengikis beautifulsoup", "render HTML selenium", "automasi API OpenAI", "migrasi wix ke laman statik", "pengikis blog wix python"]
tags: ["wix", "markdown", "migrasi blog", "openai", "pengikisan", "beautifulsoup", "selenium", "automasi", "SEO", "tutorial"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Mengapa Mengeksport Catatan Blog dari Wix?

**Ringkasan:** Panduan ini menunjukkan cara mengeksport catatan blog Wix ke Markdown menggunakan tiga skrip Python: pelari persediaan, pengikis berasaskan Selenium, dan penukar HTML-ke-Markdown berkuasa OpenAI. Hasilnya ialah fail Markdown yang bersih dan mudah alih, sedia untuk Hugo, Jekyll, atau mana-mana penjana laman statik.

Wix tidak menawarkan eksport blog natif ke Markdown. Jika anda berhijrah ke penjana laman statik seperti Hugo atau Jekyll, anda perlu mengikis halaman yang dirender, mengekstrak kandungan, dan menukarkannya. Tutorial ini mengautomatikkan keseluruhan proses menggunakan **Python, Selenium, BeautifulSoup**, dan **API GPT OpenAI**.

Saluran paip menggunakan tiga skrip:

- `fetch_blog_posts.sh` — menyediakan persekitaran dan menjalankan saluran paip
- `parse_blog_sitemap.py` — merender halaman dengan Selenium, mengekstrak kandungan, memuat turun imej
- `generate_md.py` — menukar HTML ke Markdown melalui OpenAI

## Langkah 1: Sediakan Persekitaran

Cipta `fetch_blog_posts.sh` untuk mengendalikan pemeriksaan Python, persediaan persekitaran maya, pemasangan kebergantungan, dan pelaksanaan saluran paip.

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

## Langkah 2: Kikis dan Ekstrak Kandungan Blog

`parse_blog_sitemap.py` melakukan kerja berat:

1. Mengambil XML peta laman untuk menemui semua URL catatan blog
2. Merender setiap halaman dengan **Selenium** (diperlukan kerana kandungan Wix dimuat secara dinamik)
3. Mengekstrak `<div id="content-wrapper">` untuk mengasingkan kandungan artikel
4. Memuat turun semua imej secara tempatan dan mengemas kini atribut `src`
5. Menyimpan HTML yang dibersihkan sebagai `_index.html`
6. Memanggil penukar Markdown

**Mengapa Selenium dan bukannya requests?** Wix merender kandungan dengan JavaScript. Permintaan HTTP mudah mengembalikan cangkerang halaman kosong. Selenium menjalankan pelayar Chrome tanpa kepala untuk mendapatkan HTML yang dirender sepenuhnya.

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

## Langkah 3: Tukar HTML ke Markdown dengan OpenAI

`generate_md.py` membaca setiap fail `_index.html`, menghantar kandungan ke API Chat OpenAI, dan menulis Markdown yang dihasilkan.

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

## 출력 폴더 구조

파이프라인 실행 후 각 블로그 게시물은 자체 폴더를 갖습니다:

```
downloads/
  your-post-title/
    _index.html      # 추출 및 정리된 HTML
    _index.md         # 변환된 Markdown
    image1.png        # 다운로드된 이미지
    image2.png
```

## OpenAI API 키 설정

스크립트 디렉토리에 `OPENAI_API_KEY.TXT`라는 파일에 API 키를 저장하세요:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## 전체 파이프라인 실행

```bash
bash fetch_blog_posts.sh
```

Perintah tunggal ini menyediakan persekitaran, mengikis semua catatan blog dari peta laman, memuat turun imej, dan menukar semuanya kepada Markdown.

## Sumbang kepada Projek

Projek ini adalah sumber terbuka. Laporan pepijat, cadangan ciri, dan pull request dialu-alukan.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Projek di GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Soalan Lazim

{{% details title="Mengapa saya tidak boleh menggunakan `requests` untuk mengikis catatan blog Wix?" closed="true" %}}
Wix merender kandungan secara dinamik dengan JavaScript. Permintaan HTTP standard mengembalikan cangkerang halaman kosong. Selenium menjalankan pelayar tanpa kepala untuk mendapatkan HTML yang dirender sepenuhnya.
{{% /details %}}

{{% details title="Adakah ini berfungsi dengan mana-mana blog Wix?" closed="true" %}}
Ya. Pengikis membaca XML peta laman blog dan memproses setiap URL. Anda hanya perlu mengemas kini pembolehubah `SITEMAP_URL` dalam `parse_blog_sitemap.py` untuk menunjuk ke peta laman tapak anda.
{{% /details %}}

{{% details title="Model OpenAI mana yang digunakan?" closed="true" %}}
Skrip menggunakan GPT-4o secara lalai. Anda boleh menukar pembolehubah `API_MODEL` dalam `generate_md.py` untuk menggunakan model lain.
{{% /details %}}

{{% details title="Bolehkah saya menggunakan ini untuk berhijrah dari Wix ke Hugo?" closed="true" %}}
Ya. Output adalah Markdown standard dengan laluan imej tempatan, yang berfungsi terus dengan Hugo, Jekyll, Astro, dan penjana laman statik lain. Tambahkan front matter pada fail `_index.md` yang dijana untuk melengkapkan migrasi.
{{% /details %}}

{{% details title="Berapakah kos API OpenAI untuk ini?" closed="true" %}}
Kos bergantung pada bilangan dan panjang catatan blog anda. Blog biasa dengan 50 catatan panjang sederhana berharga beberapa dolar dalam penggunaan API dengan GPT-4o.
{{% /details %}}

{{% details title="Adakah alat ini sumber terbuka?" closed="true" %}}
Ya. Kod sumber penuh tersedia di [GitHub](https://github.com/everappz/wix-blog-export) di bawah lesen sumber terbuka.
{{% /details %}}
