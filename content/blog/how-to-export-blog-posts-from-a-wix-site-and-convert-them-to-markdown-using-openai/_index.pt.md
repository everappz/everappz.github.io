---
title: "Exportar Posts do Blog Wix para Markdown com OpenAI"
date: 2025-06-24
description: "Automatize a exportação do blog Wix usando Python, Selenium e OpenAI. Extraia conteúdo dinâmico, baixe imagens e converta HTML para Markdown limpo para Hugo ou Jekyll."
keywords: ["exportação blog Wix", "converter HTML para markdown", "conversão markdown OpenAI", "wix para markdown", "migração blog SEO", "migração wix para hugo", "scraper beautifulsoup", "renderização HTML selenium", "automação API OpenAI", "migrar wix para site estático", "scraper blog wix python"]
tags: ["wix", "markdown", "migração de blog", "openai", "scraping", "beautifulsoup", "selenium", "automação", "SEO", "tutorial"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Por Que Exportar Posts do Blog do Wix?

**Resumo:** Este guia mostra como exportar posts do blog Wix para Markdown usando três scripts Python: um executor de configuração, um scraper baseado em Selenium e um conversor HTML-para-Markdown alimentado por OpenAI. O resultado são arquivos Markdown limpos e portáveis prontos para Hugo, Jekyll ou qualquer gerador de sites estáticos.

Wix não oferece exportação nativa de blog para Markdown. Se você está migrando para um gerador de sites estáticos como Hugo ou Jekyll, precisa raspar as páginas renderizadas, extrair o conteúdo e convertê-lo. Este tutorial automatiza todo o processo usando **Python, Selenium, BeautifulSoup** e **API GPT da OpenAI**.

O pipeline usa três scripts:

- `fetch_blog_posts.sh` — configura o ambiente e executa o pipeline
- `parse_blog_sitemap.py` — renderiza páginas com Selenium, extrai conteúdo, baixa imagens
- `generate_md.py` — converte HTML para Markdown via OpenAI

## Passo 1: Configurar o Ambiente

Crie `fetch_blog_posts.sh` para lidar com verificações do Python, configuração do ambiente virtual, instalação de dependências e execução do pipeline.

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

## Passo 2: Raspar e Extrair Conteúdo do Blog

`parse_blog_sitemap.py` faz o trabalho pesado:

1. Busca o XML do sitemap para descobrir todas as URLs dos posts do blog
2. Renderiza cada página com **Selenium** (necessário porque o conteúdo do Wix é carregado dinamicamente)
3. Extrai o `<div id="content-wrapper">` para isolar o conteúdo do artigo
4. Baixa todas as imagens localmente e atualiza os atributos `src`
5. Salva o HTML limpo como `_index.html`
6. Chama o conversor Markdown

**Por que Selenium em vez de requests?** Wix renderiza conteúdo com JavaScript. Uma simples requisição HTTP retorna uma casca de página vazia. Selenium executa um navegador Chrome headless para obter o HTML completamente renderizado.

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

## Passo 3: Converter HTML para Markdown com OpenAI

`generate_md.py` lê cada arquivo `_index.html`, envia o conteúdo para a API Chat da OpenAI e escreve o Markdown resultante.

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

## Estrutura de Pastas de Saída

Após executar o pipeline, cada post do blog recebe sua própria pasta:

```
downloads/
  your-post-title/
    _index.html      # HTML extraído e limpo
    _index.md         # Markdown convertido
    image1.png        # Imagens baixadas
    image2.png
```

## Configuração da Chave API OpenAI

Salve sua chave API em um arquivo chamado `OPENAI_API_KEY.TXT` no diretório do script:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Execute o Pipeline Completo

```bash
bash fetch_blog_posts.sh
```

Este único comando configura o ambiente, raspa todos os posts do blog do sitemap, baixa imagens e converte tudo para Markdown.

## Contribua para o Projeto

O projeto é open source. Relatórios de bugs, sugestões de recursos e pull requests são bem-vindos.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Projeto no GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Perguntas Frequentes

{{% details title="Por que não posso usar `requests` para raspar posts do blog Wix?" closed="true" %}}
Wix renderiza conteúdo dinamicamente com JavaScript. Uma requisição HTTP padrão retorna uma casca de página vazia. Selenium executa um navegador headless para obter o HTML completamente renderizado.
{{% /details %}}

{{% details title="Isso funciona com qualquer blog Wix?" closed="true" %}}
Sim. O scraper lê o XML do sitemap do blog e processa cada URL. Você só precisa atualizar a variável `SITEMAP_URL` em `parse_blog_sitemap.py` para apontar para o sitemap do seu site.
{{% /details %}}

{{% details title="Qual modelo OpenAI isso usa?" closed="true" %}}
O script usa GPT-4o por padrão. Você pode alterar a variável `API_MODEL` em `generate_md.py` para usar um modelo diferente.
{{% /details %}}

{{% details title="Posso usar isso para migrar do Wix para Hugo?" closed="true" %}}
Sim. A saída é Markdown padrão com caminhos de imagem locais, que funciona diretamente com Hugo, Jekyll, Astro e outros geradores de sites estáticos. Adicione front matter aos arquivos `_index.md` gerados para completar a migração.
{{% /details %}}

{{% details title="Quanto custa a API OpenAI para isso?" closed="true" %}}
O custo depende do número e comprimento dos seus posts do blog. Um blog típico com 50 posts de comprimento moderado custa alguns dólares em uso da API com GPT-4o.
{{% /details %}}

{{% details title="Esta ferramenta é open source?" closed="true" %}}
Sim. O código-fonte completo está disponível no [GitHub](https://github.com/everappz/wix-blog-export) sob uma licença open source.
{{% /details %}}
