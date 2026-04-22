---
title: "Xuất bài viết blog Wix sang Markdown với OpenAI"
date: 2025-06-24
description: "Tự động hóa xuất blog Wix bằng Python, Selenium và OpenAI. Trích xuất nội dung động, tải ảnh và chuyển đổi HTML thành Markdown cho Hugo hoặc Jekyll."
keywords: ["xuất blog Wix", "chuyển đổi HTML sang markdown", "OpenAI chuyển đổi markdown", "wix sang markdown", "di chuyển blog SEO", "di chuyển wix sang hugo", "beautifulsoup scraper", "selenium render HTML", "OpenAI API tự động hóa", "di chuyển wix sang trang tĩnh", "wix blog scraper python"]
tags: ["wix", "markdown", "di chuyển blog", "openai", "scraping", "beautifulsoup", "selenium", "tự động hóa", "SEO", "hướng dẫn"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Tại sao cần xuất bài viết blog từ Wix?

**Tóm tắt:** Hướng dẫn này trình bày cách xuất bài viết blog Wix sang Markdown bằng ba script Python: trình chạy thiết lập, scraper dựa trên Selenium và trình chuyển đổi HTML sang Markdown sử dụng OpenAI. Kết quả là các tệp Markdown sạch, di động, sẵn sàng cho Hugo, Jekyll hoặc bất kỳ trình tạo trang tĩnh nào.

Wix không cung cấp tính năng xuất blog sang Markdown. Nếu bạn đang di chuyển sang trình tạo trang tĩnh như Hugo hoặc Jekyll, bạn cần scrape các trang đã render, trích xuất nội dung và chuyển đổi. Hướng dẫn này tự động hóa toàn bộ quy trình bằng **Python, Selenium, BeautifulSoup** và **OpenAI GPT API**.

Pipeline sử dụng ba script:

- `fetch_blog_posts.sh` — thiết lập môi trường và chạy pipeline
- `parse_blog_sitemap.py` — render trang bằng Selenium, trích xuất nội dung, tải ảnh
- `generate_md.py` — chuyển đổi HTML sang Markdown qua OpenAI

## Bước 1: Thiết lập môi trường

Tạo `fetch_blog_posts.sh` để xử lý kiểm tra Python, thiết lập môi trường ảo, cài đặt phụ thuộc và thực thi pipeline.

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

## Bước 2: Scrape và trích xuất nội dung blog

`parse_blog_sitemap.py` thực hiện công việc nặng:

1. Lấy sitemap XML để tìm tất cả URL bài viết
2. Render mỗi trang bằng **Selenium** (cần thiết vì nội dung Wix được tải động)
3. Trích xuất `<div id="content-wrapper">` để tách nội dung bài viết
4. Tải tất cả ảnh về máy và cập nhật thuộc tính `src`
5. Lưu HTML đã làm sạch thành `_index.html`
6. Gọi trình chuyển đổi Markdown

**Tại sao Selenium thay vì requests?** Wix render nội dung bằng JavaScript. Yêu cầu HTTP đơn giản trả về trang trống. Selenium chạy trình duyệt Chrome headless để lấy HTML đã render đầy đủ.

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

def download_image(img_url, dest_folder):
    try:
        parsed = urlparse(img_url)
        filename = os.path.basename(parsed.path)
        dest_path = os.path.join(dest_folder, filename)
        urllib.request.urlretrieve(img_url, dest_path)
        return filename
    except Exception as e:
        return None

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
            except Exception as e:
                pass
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
                print(f"❌ Failed to process {page_url}: {e}")

if __name__ == "__main__":
    parse_sitemap_and_process()
```

## Bước 3: Chuyển đổi HTML sang Markdown với OpenAI

`generate_md.py` đọc mỗi tệp `_index.html`, gửi nội dung đến OpenAI Chat API và ghi Markdown kết quả.

```python
#!/usr/bin/env python3
import os, sys, json, time, random
import urllib.request, urllib.error
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
    except Exception as e:
        return ""

def main():
    if len(sys.argv) != 2: return
    html_file = sys.argv[1]
    if not os.path.exists(html_file): return
    with open(html_file, "r", encoding="utf-8") as f:
        html = f.read()
    html_content = BeautifulSoup(html, "html.parser").prettify()
    markdown = call_openai_to_convert_to_markdown(html_content)
    if markdown:
        md_path = os.path.join(os.path.dirname(html_file), "_index.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(markdown)

if __name__ == "__main__":
    main()
```

## Cấu trúc thư mục đầu ra

Sau khi chạy pipeline, mỗi bài viết blog có thư mục riêng:

```
downloads/
  your-post-title/
    _index.html      # HTML đã trích xuất và làm sạch
    _index.md         # Markdown đã chuyển đổi
    image1.png        # Ảnh đã tải
    image2.png
```

## Thiết lập OpenAI API Key

Lưu API key vào tệp `OPENAI_API_KEY.TXT` trong thư mục script:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Chạy toàn bộ Pipeline

```bash
bash fetch_blog_posts.sh
```

Lệnh duy nhất này thiết lập môi trường, scrape tất cả bài viết từ sitemap, tải ảnh và chuyển đổi mọi thứ sang Markdown.

## Đóng góp cho dự án

Dự án là mã nguồn mở. Báo cáo lỗi, đề xuất tính năng và pull request đều được hoan nghênh.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Dự án trên GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Câu hỏi thường gặp

{{% details title="Tại sao tôi không thể dùng `requests` để scrape bài viết blog Wix?" closed="true" %}}
Wix render nội dung động bằng JavaScript. Yêu cầu HTTP tiêu chuẩn trả về trang trống. Selenium chạy trình duyệt headless để lấy HTML đã render đầy đủ.
{{% /details %}}

{{% details title="Điều này có hoạt động với bất kỳ blog Wix nào không?" closed="true" %}}
Có. Scraper đọc sitemap XML của blog và xử lý từng URL. Bạn chỉ cần cập nhật biến `SITEMAP_URL` trong `parse_blog_sitemap.py` trỏ đến sitemap của trang web bạn.
{{% /details %}}

{{% details title="Sử dụng mô hình OpenAI nào?" closed="true" %}}
Script mặc định dùng GPT-4o. Bạn có thể thay đổi biến `API_MODEL` trong `generate_md.py` để dùng mô hình khác.
{{% /details %}}

{{% details title="Tôi có thể dùng để di chuyển từ Wix sang Hugo không?" closed="true" %}}
Có. Đầu ra là Markdown chuẩn với đường dẫn ảnh cục bộ, hoạt động trực tiếp với Hugo, Jekyll, Astro và các trình tạo trang tĩnh khác. Thêm front matter vào các tệp `_index.md` được tạo để hoàn tất di chuyển.
{{% /details %}}

{{% details title="OpenAI API tốn bao nhiêu cho việc này?" closed="true" %}}
Chi phí phụ thuộc vào số lượng và độ dài bài viết. Blog điển hình với 50 bài viết độ dài trung bình tốn vài đô la sử dụng API với GPT-4o.
{{% /details %}}

{{% details title="Công cụ này có phải mã nguồn mở không?" closed="true" %}}
Có. Toàn bộ mã nguồn có sẵn trên [GitHub](https://github.com/everappz/wix-blog-export) theo giấy phép mã nguồn mở.
{{% /details %}}
