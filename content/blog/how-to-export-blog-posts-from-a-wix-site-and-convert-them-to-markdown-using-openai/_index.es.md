---
title: "Exportar artículos de blog de Wix a Markdown con OpenAI"
date: 2025-06-24
description: "Automatiza la exportación del blog de Wix con Python, Selenium y OpenAI. Extrae contenido dinámico, descarga imágenes y convierte HTML a Markdown limpio para Hugo o Jekyll."
keywords: ["exportación blog Wix", "convertir HTML a markdown", "conversión OpenAI a markdown", "wix a markdown", "migración blog SEO", "migración wix a hugo", "scraper beautifulsoup", "renderizar HTML con selenium", "automatización OpenAI API", "migrar wix a sitio estático", "scraper blog wix python"]
tags: ["wix", "markdown", "migración de blog", "openai", "scraping", "beautifulsoup", "selenium", "automatización", "SEO", "tutorial"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## ¿Por qué exportar artículos de blog de Wix?

**Resumen:** Esta guía muestra cómo exportar artículos de blog de Wix a Markdown usando tres scripts de Python: un ejecutor de configuración, un scraper basado en Selenium y un conversor de HTML a Markdown con OpenAI. El resultado son archivos Markdown limpios y portables listos para Hugo, Jekyll o cualquier generador de sitios estáticos.

Wix no ofrece una exportación nativa del blog a Markdown. Si estás migrando a un generador de sitios estáticos como Hugo o Jekyll, necesitas extraer las páginas renderizadas, extraer el contenido y convertirlo. Este tutorial automatiza todo el proceso usando **Python, Selenium, BeautifulSoup** y **OpenAI GPT API**.

El pipeline usa tres scripts:

- `fetch_blog_posts.sh` — configura el entorno y ejecuta el pipeline
- `parse_blog_sitemap.py` — renderiza páginas con Selenium, extrae contenido, descarga imágenes
- `generate_md.py` — convierte HTML a Markdown vía OpenAI

## Paso 1: Configurar el entorno

Crea `fetch_blog_posts.sh` para gestionar la verificación de Python, configuración del entorno virtual, instalación de dependencias y ejecución del pipeline.

```bash
#!/bin/bash
echo "🔍 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi
echo "✅ Python 3 found: $(python3 --version)"
VENV_DIR=".venv"
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
fi
source "$VENV_DIR/bin/activate"
pip install --upgrade pip
pip install beautifulsoup4 lxml selenium webdriver-manager
python3 parse_blog_sitemap.py
deactivate
```

## Paso 2: Extraer contenido del blog

`parse_blog_sitemap.py` hace el trabajo pesado:

1. Obtiene el XML del sitemap para descubrir todas las URLs de artículos
2. Renderiza cada página con **Selenium** (necesario porque Wix carga contenido dinámicamente)
3. Extrae el `<div id="content-wrapper">` para aislar el contenido del artículo
4. Descarga todas las imágenes localmente y actualiza los atributos `src`
5. Guarda el HTML limpio como `_index.html`
6. Llama al conversor de Markdown

**¿Por qué Selenium en lugar de requests?** Wix renderiza contenido con JavaScript. Una solicitud HTTP simple devuelve un esqueleto de página vacío. Selenium ejecuta un navegador Chrome sin interfaz para obtener el HTML completamente renderizado.

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
                urllib.request.urlretrieve(src, os.path.join(folder, filename))
                img["src"] = filename
            except: pass
    return str(soup)

def parse_sitemap_and_process():
    os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)
    sitemap_xml = urllib.request.urlopen(SITEMAP_URL).read()
    root = ET.fromstring(sitemap_xml)
    for url_elem in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
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
            except: pass

if __name__ == "__main__":
    parse_sitemap_and_process()
```

## Paso 3: Convertir HTML a Markdown con OpenAI

`generate_md.py` lee cada archivo `_index.html`, envía el contenido a la API Chat de OpenAI y escribe el Markdown resultante.

```python
#!/usr/bin/env python3
import os, sys, json, time, random
import urllib.request, urllib.error
from bs4 import BeautifulSoup

API_MODEL = "gpt-4o"
API_KEY_FILE = "OPENAI_API_KEY.TXT"

def call_openai_to_convert_to_markdown(html_content, api_key=None):
    if api_key is None:
        with open(API_KEY_FILE, "r") as f: api_key = f.read().strip()
    time.sleep(round(random.uniform(1.0, 2.0), 2))
    system_prompt = ("You are a tool that converts HTML content from blog posts into well-structured Markdown (.md) format. "
        "Convert all visible text content and replace all <img> tags with Markdown image syntax using their local filenames.")
    data = {"model": API_MODEL, "temperature": 0.3,
        "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": html_content}]}
    request = urllib.request.Request("https://api.openai.com/v1/chat/completions",
        data=json.dumps(data).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request) as response:
            return json.load(response)["choices"][0]["message"]["content"].strip()
    except: return ""

def main():
    if len(sys.argv) != 2: return
    html_file = sys.argv[1]
    if not os.path.exists(html_file): return
    with open(html_file, "r", encoding="utf-8") as f: html = f.read()
    markdown = call_openai_to_convert_to_markdown(BeautifulSoup(html, "html.parser").prettify())
    if markdown:
        with open(os.path.join(os.path.dirname(html_file), "_index.md"), "w", encoding="utf-8") as f:
            f.write(markdown)

if __name__ == "__main__":
    main()

```

## Estructura de carpetas de salida

Después de ejecutar el pipeline, cada artículo obtiene su propia carpeta:

```
downloads/
  your-post-title/
    _index.html      # HTML extraído y limpio
    _index.md         # Markdown convertido
    image1.png        # Imágenes descargadas
    image2.png
```

## Configuración de la clave de la API de OpenAI

Guarda tu clave API en un archivo llamado `OPENAI_API_KEY.TXT` en el directorio de scripts:

```text
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Ejecutar el pipeline completo

```bash
bash fetch_blog_posts.sh
```

Este único comando configura el entorno, extrae todos los artículos del sitemap, descarga imágenes y convierte todo a Markdown.

## Contribuye al proyecto

El proyecto es de código abierto. Los informes de errores, sugerencias de funciones y pull requests son bienvenidos.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Proyecto en GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Preguntas frecuentes

{{% details title="¿Por qué no puedo usar simplemente `requests` para extraer artículos de Wix?" closed="true" %}}
Wix renderiza contenido dinámicamente con JavaScript. Una solicitud HTTP estándar devuelve un esqueleto de página vacío. Selenium ejecuta un navegador sin interfaz para obtener el HTML completamente renderizado.
{{% /details %}}

{{% details title="¿Funciona con cualquier blog de Wix?" closed="true" %}}
Sí. El scraper lee el XML del sitemap y procesa cada URL. Solo necesitas actualizar la variable `SITEMAP_URL` en `parse_blog_sitemap.py`.
{{% /details %}}

{{% details title="¿Qué modelo de OpenAI utiliza?" closed="true" %}}
El script usa GPT-4o por defecto. Puedes cambiar la variable `API_MODEL` en `generate_md.py` para usar otro modelo.
{{% /details %}}

{{% details title="¿Puedo usar esto para migrar de Wix a Hugo?" closed="true" %}}
Sí. La salida es Markdown estándar con rutas de imágenes locales, que funciona directamente con Hugo, Jekyll, Astro y otros generadores de sitios estáticos.
{{% /details %}}

{{% details title="¿Cuánto cuesta la API de OpenAI para esto?" closed="true" %}}
El coste depende del número y longitud de tus artículos. Un blog típico con 50 artículos cuesta unos pocos dólares con GPT-4o.
{{% /details %}}

{{% details title="¿Es esta herramienta de código abierto?" closed="true" %}}
Sí. El código fuente completo está disponible en [GitHub](https://github.com/everappz/wix-blog-export).
{{% /details %}}
