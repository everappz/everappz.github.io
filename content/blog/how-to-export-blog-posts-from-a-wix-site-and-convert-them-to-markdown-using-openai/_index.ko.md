---
title: "OpenAI를 사용하여 Wix 블로그 게시물을 Markdown으로 내보내기"
date: 2025-06-24
description: "Python, Selenium, OpenAI를 사용하여 Wix 블로그 내보내기를 자동화합니다. 동적 콘텐츠를 추출하고 이미지를 다운로드하며 HTML을 Hugo나 Jekyll용 깔끔한 Markdown으로 변환합니다."
keywords: ["Wix 블로그 내보내기", "HTML을 markdown으로 변환", "OpenAI markdown 변환", "wix에서 markdown으로", "SEO 블로그 마이그레이션", "wix에서 hugo 마이그레이션", "beautifulsoup 스크래퍼", "selenium HTML 렌더링", "OpenAI API 자동화", "wix에서 정적 사이트로 마이그레이션", "wix 블로그 스크래퍼 python"]
tags: ["wix", "markdown", "블로그 마이그레이션", "openai", "스크래핑", "beautifulsoup", "selenium", "자동화", "SEO", "튜토리얼"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Wix에서 블로그 게시물을 내보내는 이유

**요약:** 이 가이드에서는 세 개의 Python 스크립트를 사용하여 Wix 블로그 게시물을 Markdown으로 내보내는 방법을 보여줍니다: 설정 실행기, Selenium 기반 스크래퍼, OpenAI 기반 HTML-to-Markdown 변환기. 결과물은 Hugo, Jekyll 또는 기타 정적 사이트 생성기에 바로 사용할 수 있는 깔끔하고 이식 가능한 Markdown 파일입니다.

Wix는 기본적으로 Markdown으로 블로그를 내보내는 기능을 제공하지 않습니다. Hugo나 Jekyll 같은 정적 사이트 생성기로 마이그레이션하려면 렌더링된 페이지를 스크래핑하고, 콘텐츠를 추출하고, 변환해야 합니다. 이 튜토리얼에서는 **Python, Selenium, BeautifulSoup**, **OpenAI의 GPT API**를 사용하여 전체 프로세스를 자동화합니다.

파이프라인은 세 개의 스크립트를 사용합니다:

- `fetch_blog_posts.sh` — 환경을 설정하고 파이프라인을 실행합니다
- `parse_blog_sitemap.py` — Selenium으로 페이지를 렌더링하고, 콘텐츠를 추출하고, 이미지를 다운로드합니다
- `generate_md.py` — OpenAI를 통해 HTML을 Markdown으로 변환합니다

## 1단계: 환경 설정

Python 확인, 가상 환경 설정, 의존성 설치, 파이프라인 실행을 처리하는 `fetch_blog_posts.sh`를 만듭니다.

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

## 2단계: 블로그 콘텐츠 스크래핑 및 추출

`parse_blog_sitemap.py`가 주요 작업을 수행합니다:

1. 사이트맵 XML을 가져와 모든 블로그 게시물 URL을 찾습니다
2. **Selenium**으로 각 페이지를 렌더링합니다 (Wix 콘텐츠가 동적으로 로드되기 때문에 필요)
3. `<div id="content-wrapper">`를 추출하여 기사 콘텐츠를 분리합니다
4. 모든 이미지를 로컬에 다운로드하고 `src` 속성을 업데이트합니다
5. 정리된 HTML을 `_index.html`로 저장합니다
6. Markdown 변환기를 호출합니다

**왜 requests 대신 Selenium인가?** Wix는 JavaScript로 콘텐츠를 렌더링합니다. 단순 HTTP 요청은 빈 페이지 셸을 반환합니다. Selenium은 헤드리스 Chrome 브라우저를 실행하여 완전히 렌더링된 HTML을 가져옵니다.

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

## 3단계: OpenAI로 HTML을 Markdown으로 변환

`generate_md.py`는 각 `_index.html` 파일을 읽고, 콘텐츠를 OpenAI의 Chat API로 보내고, 결과 Markdown을 작성합니다.

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

이 단일 명령으로 환경 설정, 사이트맵의 모든 블로그 게시물 스크래핑, 이미지 다운로드, 모든 것의 Markdown 변환이 이루어집니다.

## 프로젝트에 기여하기

이 프로젝트는 오픈 소스입니다. 버그 보고, 기능 제안, 풀 리퀘스트를 환영합니다.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="GitHub 프로젝트" icon="github" tag="open source" >}}
{{< /cards >}}

---

## 자주 묻는 질문

{{% details title="왜 Wix 블로그 게시물을 스크래핑하는 데 `requests`를 사용할 수 없나요?" closed="true" %}}
Wix는 JavaScript로 콘텐츠를 동적으로 렌더링합니다. 표준 HTTP 요청은 빈 페이지 셸을 반환합니다. Selenium은 헤드리스 브라우저를 실행하여 완전히 렌더링된 HTML을 가져옵니다.
{{% /details %}}

{{% details title="어떤 Wix 블로그에서도 작동하나요?" closed="true" %}}
네. 스크래퍼는 블로그 사이트맵 XML을 읽고 각 URL을 처리합니다. `parse_blog_sitemap.py`의 `SITEMAP_URL` 변수를 사이트의 사이트맵으로 업데이트하기만 하면 됩니다.
{{% /details %}}

{{% details title="어떤 OpenAI 모델을 사용하나요?" closed="true" %}}
스크립트는 기본적으로 GPT-4o를 사용합니다. `generate_md.py`의 `API_MODEL` 변수를 변경하여 다른 모델을 사용할 수 있습니다.
{{% /details %}}

{{% details title="Wix에서 Hugo로 마이그레이션하는 데 사용할 수 있나요?" closed="true" %}}
네. 출력물은 로컬 이미지 경로가 있는 표준 Markdown으로, Hugo, Jekyll, Astro 및 기타 정적 사이트 생성기에서 바로 작동합니다. 마이그레이션을 완료하려면 생성된 `_index.md` 파일에 front matter를 추가하세요.
{{% /details %}}

{{% details title="OpenAI API 비용은 얼마인가요?" closed="true" %}}
비용은 블로그 게시물의 수와 길이에 따라 다릅니다. 중간 길이의 게시물 50개가 있는 일반적인 블로그는 GPT-4o로 몇 달러의 API 사용료가 듭니다.
{{% /details %}}

{{% details title="이 도구는 오픈 소스인가요?" closed="true" %}}
네. 전체 소스 코드는 오픈 소스 라이선스로 [GitHub](https://github.com/everappz/wix-blog-export)에서 이용할 수 있습니다.
{{% /details %}}
