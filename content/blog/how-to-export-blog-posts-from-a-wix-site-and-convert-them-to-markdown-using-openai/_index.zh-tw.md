---
title: "使用 OpenAI 將 Wix 部落格文章匯出為 Markdown"
date: 2025-06-24
description: "使用 Python、Selenium 和 OpenAI 自動化 Wix 部落格匯出。擷取動態內容、下載圖片並將 HTML 轉換為乾淨的 Markdown，適用於 Hugo 或 Jekyll。"
keywords: ["Wix 部落格匯出", "HTML 轉 markdown", "OpenAI markdown 轉換", "wix 轉 markdown", "SEO 部落格遷移", "wix 遷移到 hugo", "beautifulsoup 爬蟲", "selenium 渲染 HTML", "OpenAI API 自動化", "wix 遷移到靜態網站", "wix 部落格爬蟲 python"]
tags: ["wix", "markdown", "部落格遷移", "openai", "爬蟲", "beautifulsoup", "selenium", "自動化", "SEO", "教學"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## 為什麼要從 Wix 匯出部落格文章？

**摘要：** 本指南展示如何使用三個 Python 腳本將 Wix 部落格文章匯出為 Markdown：一個設定執行器、一個基於 Selenium 的爬蟲和一個由 OpenAI 驅動的 HTML 到 Markdown 轉換器。結果是乾淨、可攜帶的 Markdown 檔案，適用於 Hugo、Jekyll 或任何靜態網站產生器。

Wix 不提供原生的部落格 Markdown 匯出。如果您正在遷移到 Hugo 或 Jekyll 等靜態網站產生器，您需要抓取渲染的頁面、擷取內容並轉換。本教學使用 **Python、Selenium、BeautifulSoup** 和 **OpenAI GPT API** 自動化整個過程。

Pipeline 使用三個腳本：

- `fetch_blog_posts.sh` — 設定環境並執行 pipeline
- `parse_blog_sitemap.py` — 使用 Selenium 渲染頁面、擷取內容、下載圖片
- `generate_md.py` — 透過 OpenAI 將 HTML 轉換為 Markdown

## 步驟 1：設定環境

建立 `fetch_blog_posts.sh` 來處理 Python 檢查、虛擬環境設定、相依套件安裝和 pipeline 執行。

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

## 步驟 2：抓取和擷取部落格內容

`parse_blog_sitemap.py` 負責核心工作：

1. 取得 sitemap XML 以發現所有部落格文章 URL
2. 使用 **Selenium** 渲染每個頁面（因為 Wix 內容是動態載入的）
3. 擷取 `<div id="content-wrapper">` 以隔離文章內容
4. 在本機下載所有圖片並更新 `src` 屬性
5. 將清理後的 HTML 儲存為 `_index.html`
6. 呼叫 Markdown 轉換器

**為什麼用 Selenium 而不是 requests？** Wix 使用 JavaScript 渲染內容。簡單的 HTTP 請求傳回空頁面。Selenium 執行無頭 Chrome 瀏覽器來取得完全渲染的 HTML。

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

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\\\|?*]', '_', filename)

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
                dest_path = os.path.join(folder, filename)
                urllib.request.urlretrieve(src, dest_path)
                img["src"] = filename
            except: pass
    return str(soup)

def parse_sitemap_and_process():
    os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)
    sitemap_xml = urllib.request.urlopen(SITEMAP_URL).read()
    root = ET.fromstring(sitemap_xml)
    url_elems = root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url")
    for url_elem in url_elems:
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
            except Exception as e:
                print(f"❌ Failed: {page_url}: {e}")

if __name__ == "__main__":
    parse_sitemap_and_process()
```

## 步驟 3：使用 OpenAI 將 HTML 轉換為 Markdown

`generate_md.py` 讀取每個 `_index.html` 檔案，將內容傳送到 OpenAI Chat API，並寫入產生的 Markdown。

```python
#!/usr/bin/env python3
import os, sys, json, time, random
import urllib.request, urllib.error
from bs4 import BeautifulSoup

API_MODEL = "gpt-4o"
API_KEY_FILE = "OPENAI_API_KEY.TXT"

def read_openai_api_key():
    with open(API_KEY_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()

def call_openai_to_convert_to_markdown(html_content, api_key=None):
    if api_key is None: api_key = read_openai_api_key()
    time.sleep(round(random.uniform(1.0, 2.0), 2))
    system_prompt = (
        "You are a tool that converts HTML content from blog posts into well-structured Markdown (.md) format. "
        "Convert all visible text content and replace all <img> tags with Markdown image syntax using their local filenames. "
        "Retain the content hierarchy using proper markdown headers, and preserve paragraph structure. "
        "Make sure image alt attributes (if any) are preserved as the alt text in the markdown image syntax."
    )
    data = {"model": API_MODEL, "temperature": 0.3, "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": html_content}
    ]}
    request = urllib.request.Request("https://api.openai.com/v1/chat/completions",
        data=json.dumps(data).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request) as response:
            result = json.load(response)
            return result["choices"][0]["message"]["content"].strip()
    except: return ""

def main():
    if len(sys.argv) != 2: return
    html_file = sys.argv[1]
    if not os.path.exists(html_file): return
    with open(html_file, "r", encoding="utf-8") as f: html = f.read()
    html_content = BeautifulSoup(html, "html.parser").prettify()
    markdown = call_openai_to_convert_to_markdown(html_content)
    if markdown:
        md_path = os.path.join(os.path.dirname(html_file), "_index.md")
        with open(md_path, "w", encoding="utf-8") as f: f.write(markdown)

if __name__ == "__main__":
    main()
```

## 輸出資料夾結構

執行 pipeline 後，每篇部落格文章都有自己的資料夾：

```
downloads/
  your-post-title/
    _index.html      # 擷取並清理的 HTML
    _index.md         # 轉換後的 Markdown
    image1.png        # 下載的圖片
    image2.png
```

## OpenAI API 金鑰設定

將您的 API 金鑰儲存在腳本目錄中名為 `OPENAI_API_KEY.TXT` 的檔案中：

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## 執行完整 Pipeline

```bash
bash fetch_blog_posts.sh
```

這個單一命令設定環境、從 sitemap 抓取所有部落格文章、下載圖片並將所有內容轉換為 Markdown。

## 為專案做出貢獻

該專案是開放原始碼的。歡迎提交錯誤回報、功能建議和 pull request。

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="GitHub 上的專案" icon="github" tag="open source" >}}
{{< /cards >}}

---

## 常見問題

{{% details title="為什麼不能直接用 `requests` 抓取 Wix 部落格文章？" closed="true" %}}
Wix 使用 JavaScript 動態渲染內容。標準 HTTP 請求傳回空頁面。Selenium 執行無頭瀏覽器來取得完全渲染的 HTML。
{{% /details %}}

{{% details title="這適用於任何 Wix 部落格嗎？" closed="true" %}}
是的。爬蟲讀取部落格 sitemap XML 並處理每個 URL。您只需更新 `parse_blog_sitemap.py` 中的 `SITEMAP_URL` 變數指向您網站的 sitemap。
{{% /details %}}

{{% details title="使用哪個 OpenAI 模型？" closed="true" %}}
腳本預設使用 GPT-4o。您可以變更 `generate_md.py` 中的 `API_MODEL` 變數來使用其他模型。
{{% /details %}}

{{% details title="我可以用它從 Wix 遷移到 Hugo 嗎？" closed="true" %}}
可以。輸出是帶有本機圖片路徑的標準 Markdown，直接適用於 Hugo、Jekyll、Astro 和其他靜態網站產生器。為產生的 `_index.md` 檔案新增 front matter 即可完成遷移。
{{% /details %}}

{{% details title="OpenAI API 費用是多少？" closed="true" %}}
費用取決於部落格文章的數量和長度。包含 50 篇中等長度文章的典型部落格使用 GPT-4o 花費幾美元的 API 使用量。
{{% /details %}}

{{% details title="這個工具是開放原始碼的嗎？" closed="true" %}}
是的。完整原始碼可在 [GitHub](https://github.com/everappz/wix-blog-export) 上以開放原始碼授權取得。
{{% /details %}}
