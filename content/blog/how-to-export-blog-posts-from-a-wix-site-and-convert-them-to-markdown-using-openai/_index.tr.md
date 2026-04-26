---
title: "Wix Blog Yazılarını OpenAI ile Markdown'a Aktarma"
date: 2025-06-24
description: "Python, Selenium ve OpenAI kullanarak Wix blog aktarımını otomatikleştirin. Dinamik içeriği çıkarın, görselleri indirin ve HTML'yi Hugo veya Jekyll için temiz Markdown'a dönüştürün."
keywords: ["Wix blog aktarımı", "HTML'yi markdown'a dönüştürme", "OpenAI markdown dönüşümü", "wix'ten markdown'a", "SEO blog taşıma", "wix'ten hugo'ya taşıma", "beautifulsoup scraper", "selenium HTML işleme", "OpenAI API otomasyonu", "wix'ten statik siteye taşıma", "wix blog scraper python"]
tags: ["wix", "markdown", "blog taşıma", "openai", "scraping", "beautifulsoup", "selenium", "otomasyon", "SEO", "rehber"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Neden Wix'ten Blog Yazılarını Dışa Aktarmalısınız?

**Özet:** Bu rehber, üç Python betiği kullanarak Wix blog yazılarını Markdown'a nasıl aktaracağınızı gösterir: bir kurulum çalıştırıcı, Selenium tabanlı bir scraper ve OpenAI destekli bir HTML-Markdown dönüştürücü. Sonuç, Hugo, Jekyll veya herhangi bir statik site oluşturucu için hazır temiz, taşınabilir Markdown dosyalarıdır.

Wix, Markdown'a yerel blog dışa aktarımı sunmaz. Hugo veya Jekyll gibi bir statik site oluşturucuya geçiyorsanız, işlenmiş sayfaları scrape etmeniz, içeriği çıkarmanız ve dönüştürmeniz gerekir. Bu rehber, **Python, Selenium, BeautifulSoup** ve **OpenAI GPT API** kullanarak tüm süreci otomatikleştirir.

Pipeline üç betik kullanır:

- `fetch_blog_posts.sh` — ortamı kurar ve pipeline'ı çalıştırır
- `parse_blog_sitemap.py` — Selenium ile sayfaları işler, içeriği çıkarır, görselleri indirir
- `generate_md.py` — OpenAI aracılığıyla HTML'yi Markdown'a dönüştürür

## Adım 1: Ortamı Kurma

Python kontrolleri, sanal ortam kurulumu, bağımlılık yüklemesi ve pipeline yürütmesi için `fetch_blog_posts.sh` oluşturun.

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

## Adım 2: Blog İçeriğini Scrape Etme ve Çıkarma

`parse_blog_sitemap.py` ağır işi yapar:

1. Tüm blog yazısı URL'lerini keşfetmek için sitemap XML'ini alır
2. Her sayfayı **Selenium** ile işler (Wix içeriği dinamik olarak yüklendiği için gereklidir)
3. Makale içeriğini izole etmek için `<div id="content-wrapper">`'ı çıkarır
4. Tüm görselleri yerel olarak indirir ve `src` niteliklerini günceller
5. Temizlenmiş HTML'yi `_index.html` olarak kaydeder
6. Markdown dönüştürücüyü çağırır

**Neden requests yerine Selenium?** Wix, içeriği JavaScript ile işler. Basit bir HTTP isteği boş bir sayfa kabuğu döndürür. Selenium, tam olarak işlenmiş HTML'yi almak için bir headless Chrome tarayıcısı çalıştırır.

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

## Adım 3: OpenAI ile HTML'yi Markdown'a Dönüştürme

`generate_md.py` her `_index.html` dosyasını okur, içeriği OpenAI Chat API'sine gönderir ve sonuç Markdown'ı yazar.

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

## Çıktı Klasör Yapısı

Pipeline çalıştırıldıktan sonra her blog yazısı kendi klasörünü alır:

```
downloads/
  your-post-title/
    _index.html      # Çıkarılmış ve temizlenmiş HTML
    _index.md         # Dönüştürülmüş Markdown
    image1.png        # İndirilen görseller
    image2.png
```

## OpenAI API Anahtarı Kurulumu

API anahtarınızı betik dizininde `OPENAI_API_KEY.TXT` adlı bir dosyaya kaydedin:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Tam Pipeline'ı Çalıştırma

```bash
bash fetch_blog_posts.sh
```

Bu tek komut ortamı kurar, sitemap'teki tüm blog yazılarını scrape eder, görselleri indirir ve her şeyi Markdown'a dönüştürür.

## Projeye Katkıda Bulunun

Proje açık kaynaklıdır. Hata raporları, özellik önerileri ve pull request'ler hoş karşılanır.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="GitHub'da Proje" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Sık Sorulan Sorular

{{% details title="Wix blog yazılarını scrape etmek için neden sadece `requests` kullanamıyorum?" closed="true" %}}
Wix içeriği JavaScript ile dinamik olarak işler. Standart bir HTTP isteği boş bir sayfa kabuğu döndürür. Selenium, tam olarak işlenmiş HTML'yi almak için bir headless tarayıcı çalıştırır.
{{% /details %}}

{{% details title="Bu herhangi bir Wix bloguyla çalışır mı?" closed="true" %}}
Evet. Scraper blog sitemap XML'ini okur ve her URL'yi işler. Sadece `parse_blog_sitemap.py`'deki `SITEMAP_URL` değişkenini sitenizin sitemap'ine yönlendirmek yeterlidir.
{{% /details %}}

{{% details title="Hangi OpenAI modelini kullanıyor?" closed="true" %}}
Betik varsayılan olarak GPT-4o kullanır. Farklı bir model kullanmak için `generate_md.py`'deki `API_MODEL` değişkenini değiştirebilirsiniz.
{{% /details %}}

{{% details title="Bunu Wix'ten Hugo'ya geçiş için kullanabilir miyim?" closed="true" %}}
Evet. Çıktı, yerel görsel yollarıyla standart Markdown'dır ve doğrudan Hugo, Jekyll, Astro ve diğer statik site oluşturucularla çalışır. Geçişi tamamlamak için oluşturulan `_index.md` dosyalarına front matter ekleyin.
{{% /details %}}

{{% details title="OpenAI API bunun için ne kadar tutar?" closed="true" %}}
Maliyet, blog yazılarınızın sayısına ve uzunluğuna bağlıdır. Orta uzunlukta 50 yazılı tipik bir blog, GPT-4o ile birkaç dolarlık API kullanımına mal olur.
{{% /details %}}

{{% details title="Bu araç açık kaynak mı?" closed="true" %}}
Evet. Tam kaynak kodu [GitHub](https://github.com/everappz/wix-blog-export)'da açık kaynak lisansı altında mevcuttur.
{{% /details %}}
