---
title: "OpenAI के साथ Wix ब्लॉग पोस्ट को Markdown में एक्सपोर्ट करें"
date: 2025-06-24
description: "Python, Selenium और OpenAI का उपयोग करके Wix ब्लॉग एक्सपोर्ट को ऑटोमेट करें। डायनामिक कंटेंट एक्सट्रैक्ट करें, इमेज डाउनलोड करें और HTML को Hugo या Jekyll के लिए क्लीन Markdown में कन्वर्ट करें।"
keywords: ["Wix ब्लॉग एक्सपोर्ट", "HTML को markdown में कन्वर्ट", "OpenAI markdown कन्वर्शन", "wix से markdown", "SEO ब्लॉग माइग्रेशन", "wix से hugo माइग्रेशन", "beautifulsoup scraper", "selenium HTML रेंडर", "OpenAI API ऑटोमेशन", "wix से स्टैटिक साइट माइग्रेट", "wix ब्लॉग scraper python"]
tags: ["wix", "markdown", "ब्लॉग माइग्रेशन", "openai", "scraping", "beautifulsoup", "selenium", "ऑटोमेशन", "SEO", "ट्यूटोरियल"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Wix से ब्लॉग पोस्ट क्यों एक्सपोर्ट करें?

**संक्षेप में:** यह गाइड दिखाती है कि तीन Python स्क्रिप्ट का उपयोग करके Wix ब्लॉग पोस्ट को Markdown में कैसे एक्सपोर्ट करें: एक सेटअप रनर, एक Selenium-आधारित scraper, और एक OpenAI-संचालित HTML-से-Markdown कन्वर्टर। परिणाम क्लीन, पोर्टेबल Markdown फाइलें हैं जो Hugo, Jekyll या किसी भी स्टैटिक साइट जनरेटर के लिए तैयार हैं।

Wix Markdown में नेटिव ब्लॉग एक्सपोर्ट प्रदान नहीं करता। यदि आप Hugo या Jekyll जैसे स्टैटिक साइट जनरेटर पर माइग्रेट कर रहे हैं, तो आपको रेंडर किए गए पेजों को स्क्रैप करना, कंटेंट निकालना और कन्वर्ट करना होगा। यह ट्यूटोरियल **Python, Selenium, BeautifulSoup** और **OpenAI के GPT API** का उपयोग करके पूरी प्रक्रिया को ऑटोमेट करता है।

पाइपलाइन तीन स्क्रिप्ट का उपयोग करती है:

- `fetch_blog_posts.sh` — एनवायरनमेंट सेटअप करता है और पाइपलाइन चलाता है
- `parse_blog_sitemap.py` — Selenium से पेज रेंडर करता है, कंटेंट एक्सट्रैक्ट करता है, इमेज डाउनलोड करता है
- `generate_md.py` — OpenAI के माध्यम से HTML को Markdown में कन्वर्ट करता है

## स्टेप 1: एनवायरनमेंट सेटअप करें

Python चेक, वर्चुअल एनवायरनमेंट सेटअप, डिपेंडेंसी इंस्टॉलेशन और पाइपलाइन एक्सीक्यूशन को हैंडल करने के लिए `fetch_blog_posts.sh` बनाएं।

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

## स्टेप 2: ब्लॉग कंटेंट स्क्रैप और एक्सट्रैक्ट करें

`parse_blog_sitemap.py` मुख्य काम करता है:

1. सभी ब्लॉग पोस्ट URLs खोजने के लिए sitemap XML फेच करता है
2. प्रत्येक पेज को **Selenium** से रेंडर करता है (आवश्यक क्योंकि Wix कंटेंट डायनामिकली लोड करता है)
3. आर्टिकल कंटेंट को अलग करने के लिए `<div id="content-wrapper">` एक्सट्रैक्ट करता है
4. सभी इमेज लोकली डाउनलोड करता है और `src` एट्रिब्यूट अपडेट करता है
5. क्लीन HTML को `_index.html` के रूप में सेव करता है
6. Markdown कन्वर्टर को कॉल करता है

**Selenium क्यों, requests नहीं?** Wix JavaScript से कंटेंट रेंडर करता है। एक साधारण HTTP रिक्वेस्ट खाली पेज शेल रिटर्न करती है। Selenium पूरी तरह रेंडर किया हुआ HTML प्राप्त करने के लिए headless Chrome ब्राउज़र चलाता है।

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

## स्टेप 3: OpenAI के साथ HTML को Markdown में कन्वर्ट करें

`generate_md.py` प्रत्येक `_index.html` फाइल पढ़ता है, कंटेंट को OpenAI के Chat API को भेजता है और रिजल्ट Markdown लिखता है।

```python
#!/usr/bin/env python3
import os, sys, json, time, random, urllib.request, urllib.error
from bs4 import BeautifulSoup

API_MODEL = "gpt-4o"
API_KEY_FILE = "OPENAI_API_KEY.TXT"
DISABLE_API_REQUESTS = False

def read_openai_api_key():
    with open(API_KEY_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()

def call_openai_to_convert_to_markdown(html_content, api_key=None):
    if DISABLE_API_REQUESTS: return html_content
    if api_key is None: api_key = read_openai_api_key()
    time.sleep(round(random.uniform(1.0, 2.0), 2))
    system_prompt = (
        "You are a tool that converts HTML content from blog posts into well-structured Markdown (.md) format. "
        "Convert all visible text content and replace all <img> tags with Markdown image syntax using their local filenames. "
        "Retain the content hierarchy using proper markdown headers, and preserve paragraph structure. "
        "Make sure image alt attributes (if any) are preserved as the alt text in the markdown image syntax."
    )
    data = {"model": API_MODEL, "temperature": 0.3, "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": html_content}]}
    request = urllib.request.Request("https://api.openai.com/v1/chat/completions", data=json.dumps(data).encode("utf-8"), headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request) as response:
            result = json.load(response)
            return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"❌ OpenAI API request failed: {e}")
        return ""

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 generate_md.py path/to/_index.html")
        return
    html_file = sys.argv[1]
    if not os.path.exists(html_file):
        print(f"❌ File not found: {html_file}")
        return
    print(f"🔍 Converting HTML to Markdown: {html_file}")
    with open(html_file, "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    markdown = call_openai_to_convert_to_markdown(soup.prettify())
    if markdown:
        md_path = os.path.join(os.path.dirname(html_file), "_index.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"✅ Markdown saved to {md_path}")

if __name__ == "__main__":
    main()
```

## आउटपुट फ़ोल्डर स्ट्रक्चर

```
downloads/
  your-post-title/
    _index.html      # एक्सट्रैक्ट और क्लीन किया हुआ HTML
    _index.md         # कन्वर्टेड Markdown
    image1.png        # डाउनलोड की गई इमेज
    image2.png
```

## OpenAI API कुंजी सेटअप

अपनी API कुंजी को स्क्रिप्ट डायरेक्टरी में `OPENAI_API_KEY.TXT` नामक फ़ाइल में सेव करें:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## पूरी पाइपलाइन चलाएं

```bash
bash fetch_blog_posts.sh
```

यह एक कमांड एनवायरनमेंट सेटअप करती है, sitemap से सभी ब्लॉग पोस्ट स्क्रैप करती है, इमेज डाउनलोड करती है और सब कुछ Markdown में कन्वर्ट करती है।

## प्रोजेक्ट में योगदान करें

प्रोजेक्ट ओपन सोर्स है।

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="GitHub पर प्रोजेक्ट" icon="github" tag="open source" >}}
{{< /cards >}}

---

## अक्सर पूछे जाने वाले प्रश्न

{{% details title="Wix ब्लॉग पोस्ट स्क्रैप करने के लिए `requests` का उपयोग क्यों नहीं कर सकते?" closed="true" %}}
Wix JavaScript से डायनामिकली कंटेंट रेंडर करता है। स्टैंडर्ड HTTP रिक्वेस्ट खाली पेज शेल रिटर्न करती है। Selenium पूरी तरह रेंडर किया हुआ HTML प्राप्त करने के लिए headless ब्राउज़र चलाता है।
{{% /details %}}

{{% details title="क्या यह किसी भी Wix ब्लॉग के साथ काम करता है?" closed="true" %}}
हाँ। Scraper ब्लॉग sitemap XML पढ़ता है और प्रत्येक URL प्रोसेस करता है। बस `parse_blog_sitemap.py` में `SITEMAP_URL` वेरिएबल अपडेट करें।
{{% /details %}}

{{% details title="कौन सा OpenAI मॉडल उपयोग होता है?" closed="true" %}}
स्क्रिप्ट डिफ़ॉल्ट रूप से GPT-4o उपयोग करती है। `generate_md.py` में `API_MODEL` वेरिएबल बदलें।
{{% /details %}}

{{% details title="क्या इसे Wix से Hugo माइग्रेशन के लिए उपयोग कर सकते हैं?" closed="true" %}}
हाँ। आउटपुट लोकल इमेज पाथ के साथ स्टैंडर्ड Markdown है, जो Hugo, Jekyll, Astro के साथ सीधे काम करता है।
{{% /details %}}

{{% details title="OpenAI API की लागत कितनी है?" closed="true" %}}
लागत आपके ब्लॉग पोस्ट की संख्या और लंबाई पर निर्भर करती है। 50 मध्यम लंबाई के पोस्ट वाला ब्लॉग GPT-4o के साथ कुछ डॉलर खर्च करता है।
{{% /details %}}

{{% details title="क्या यह टूल ओपन सोर्स है?" closed="true" %}}
हाँ। पूरा सोर्स कोड [GitHub](https://github.com/everappz/wix-blog-export) पर ओपन-सोर्स लाइसेंस के तहत उपलब्ध है।
{{% /details %}}
