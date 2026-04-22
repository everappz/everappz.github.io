---
title: "使用 OpenAI 将 Wix 博客文章导出为 Markdown"
date: 2025-06-24
description: "使用 Python、Selenium 和 OpenAI 自动化 Wix 博客导出。提取动态内容、下载图片并将 HTML 转换为干净的 Markdown，适用于 Hugo 或 Jekyll。"
keywords: ["Wix 博客导出", "HTML 转 markdown", "OpenAI markdown 转换", "wix 转 markdown", "SEO 博客迁移", "wix 迁移到 hugo", "beautifulsoup 爬虫", "selenium 渲染 HTML", "OpenAI API 自动化", "wix 迁移到静态网站", "wix 博客爬虫 python"]
tags: ["wix", "markdown", "博客迁移", "openai", "爬虫", "beautifulsoup", "selenium", "自动化", "SEO", "教程"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## 为什么要从 Wix 导出博客文章？

**摘要：** 本指南展示如何使用三个 Python 脚本将 Wix 博客文章导出为 Markdown：一个设置运行器、一个基于 Selenium 的爬虫和一个由 OpenAI 驱动的 HTML 到 Markdown 转换器。结果是干净、可移植的 Markdown 文件，适用于 Hugo、Jekyll 或任何静态站点生成器。

Wix 不提供原生的博客 Markdown 导出。如果您正在迁移到 Hugo 或 Jekyll 等静态站点生成器，您需要抓取渲染的页面、提取内容并转换。本教程使用 **Python、Selenium、BeautifulSoup** 和 **OpenAI GPT API** 自动化整个过程。

Pipeline 使用三个脚本：

- `fetch_blog_posts.sh` — 设置环境并运行 pipeline
- `parse_blog_sitemap.py` — 使用 Selenium 渲染页面、提取内容、下载图片
- `generate_md.py` — 通过 OpenAI 将 HTML 转换为 Markdown

## 步骤 1：设置环境

创建 `fetch_blog_posts.sh` 来处理 Python 检查、虚拟环境设置、依赖安装和 pipeline 执行。

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

## 步骤 2：抓取和提取博客内容

`parse_blog_sitemap.py` 负责核心工作：

1. 获取 sitemap XML 以发现所有博客文章 URL
2. 使用 **Selenium** 渲染每个页面（因为 Wix 内容是动态加载的）
3. 提取 `<div id="content-wrapper">` 以隔离文章内容
4. 在本地下载所有图片并更新 `src` 属性
5. 将清理后的 HTML 保存为 `_index.html`
6. 调用 Markdown 转换器

**为什么用 Selenium 而不是 requests？** Wix 使用 JavaScript 渲染内容。简单的 HTTP 请求返回空页面。Selenium 运行无头 Chrome 浏览器来获取完全渲染的 HTML。

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

## 步骤 3：使用 OpenAI 将 HTML 转换为 Markdown

`generate_md.py` 读取每个 `_index.html` 文件，将内容发送到 OpenAI Chat API，并写入生成的 Markdown。

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

## 输出文件夹结构

运行 pipeline 后，每篇博客文章都有自己的文件夹：

```
downloads/
  your-post-title/
    _index.html      # 提取并清理的 HTML
    _index.md         # 转换后的 Markdown
    image1.png        # 下载的图片
    image2.png
```

## OpenAI API 密钥设置

将您的 API 密钥保存在脚本目录中名为 `OPENAI_API_KEY.TXT` 的文件中：

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## 运行完整 Pipeline

```bash
bash fetch_blog_posts.sh
```

这个单一命令设置环境、从 sitemap 抓取所有博客文章、下载图片并将所有内容转换为 Markdown。

## 为项目做贡献

该项目是开源的。欢迎提交错误报告、功能建议和 pull request。

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="GitHub 上的项目" icon="github" tag="open source" >}}
{{< /cards >}}

---

## 常见问题

{{% details title="为什么不能直接用 `requests` 抓取 Wix 博客文章？" closed="true" %}}
Wix 使用 JavaScript 动态渲染内容。标准 HTTP 请求返回空页面。Selenium 运行无头浏览器来获取完全渲染的 HTML。
{{% /details %}}

{{% details title="这适用于任何 Wix 博客吗？" closed="true" %}}
是的。爬虫读取博客 sitemap XML 并处理每个 URL。您只需更新 `parse_blog_sitemap.py` 中的 `SITEMAP_URL` 变量指向您网站的 sitemap。
{{% /details %}}

{{% details title="使用哪个 OpenAI 模型？" closed="true" %}}
脚本默认使用 GPT-4o。您可以更改 `generate_md.py` 中的 `API_MODEL` 变量来使用其他模型。
{{% /details %}}

{{% details title="我可以用它从 Wix 迁移到 Hugo 吗？" closed="true" %}}
可以。输出是带有本地图片路径的标准 Markdown，直接适用于 Hugo、Jekyll、Astro 和其他静态站点生成器。为生成的 `_index.md` 文件添加 front matter 即可完成迁移。
{{% /details %}}

{{% details title="OpenAI API 费用是多少？" closed="true" %}}
费用取决于博客文章的数量和长度。包含 50 篇中等长度文章的典型博客使用 GPT-4o 花费几美元的 API 使用量。
{{% /details %}}

{{% details title="这个工具是开源的吗？" closed="true" %}}
是的。完整源代码可在 [GitHub](https://github.com/everappz/wix-blog-export) 上以开源许可证获取。
{{% /details %}}
