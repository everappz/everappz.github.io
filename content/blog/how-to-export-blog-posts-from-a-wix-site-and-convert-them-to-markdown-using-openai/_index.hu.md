---
title: "Wix blogbejegyzések exportálása Markdownba OpenAI-val"
date: 2025-06-24
description: "Automatizáld a Wix blog exportálását Python, Selenium és OpenAI segítségével. Dinamikus tartalom kinyerése, képek letöltése és HTML konvertálása tiszta Markdownba Hugo vagy Jekyll számára."
keywords: ["Wix blog export", "HTML markdown konvertálás", "OpenAI markdown konverzió", "wix markdownba", "SEO blog migráció", "wix hugo migráció", "beautifulsoup scraper", "selenium HTML renderelés", "OpenAI API automatizálás", "wix statikus oldalra migrálás", "wix blog scraper python"]
tags: ["wix", "markdown", "blog migráció", "openai", "scraping", "beautifulsoup", "selenium", "automatizálás", "SEO", "útmutató"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Miért exportáljunk blogbejegyzéseket a Wixből?

**Összefoglalva:** Ez az útmutató bemutatja, hogyan exportálhatod a Wix blogbejegyzéseket Markdownba három Python szkript segítségével: egy beállítási futó, egy Selenium-alapú scraper és egy OpenAI-hajtotta HTML-Markdown konverter. Az eredmény tiszta, hordozható Markdown fájlok, amelyek készen állnak Hugo, Jekyll vagy bármely statikus oldalgenerátor számára.

A Wix nem kínál natív blog exportálást Markdownba. Ha statikus oldalgenerátorra, mint a Hugo vagy Jekyll, migrálsz, scrapelned kell a renderelt oldalakat, ki kell nyerned a tartalmat és konvertálnod. Ez az útmutató automatizálja az egész folyamatot **Python, Selenium, BeautifulSoup** és **OpenAI GPT API** használatával.

A pipeline három szkriptet használ:

- `fetch_blog_posts.sh` — beállítja a környezetet és futtatja a pipeline-t
- `parse_blog_sitemap.py` — oldalakat renderel Seleniummal, tartalmat nyer ki, képeket tölt le
- `generate_md.py` — HTML-t konvertál Markdownba OpenAI-n keresztül

## 1. lépés: Környezet beállítása

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

## 2. lépés: Blog tartalom scrape-elése és kinyerése

`parse_blog_sitemap.py` végzi a nehéz munkát: lekéri a sitemap XML-t, rendereli az oldalakat **Selenium**-mal, kinyeri a `<div id="content-wrapper">`-t, letölti a képeket és elmenti a tisztított HTML-t.

**Miért Selenium és nem requests?** A Wix JavaScripttel rendereli a tartalmat. Egy egyszerű HTTP kérés üres oldalhéjat ad vissza.

## 3. lépés: HTML konvertálása Markdownba OpenAI-val

`generate_md.py` beolvassa az `_index.html` fájlokat, elküldi a tartalmat az OpenAI Chat API-nak és kiírja az eredményül kapott Markdownt.

## Kimeneti mappastruktúra

```
downloads/
  your-post-title/
    _index.html      # Kinyert és tisztított HTML
    _index.md         # Konvertált Markdown
    image1.png        # Letöltött képek
```

## Teljes pipeline futtatása

```bash
bash fetch_blog_posts.sh
```

## Hozzájárulás a projekthez

A projekt nyílt forráskódú.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Projekt a GitHubon" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Gyakran ismételt kérdések

{{% details title="Miért nem használhatok egyszerűen `requests`-et a Wix blogbejegyzések scrape-eléséhez?" closed="true" %}}
A Wix dinamikusan rendereli a tartalmat JavaScripttel. Egy standard HTTP kérés üres oldalhéjat ad vissza. A Selenium headless böngészőt futtat a teljesen renderelt HTML-ért.
{{% /details %}}

{{% details title="Működik ez bármely Wix bloggal?" closed="true" %}}
Igen. A scraper beolvassa a blog sitemap XML-jét és feldolgozza az összes URL-t. Csak frissítsd a `SITEMAP_URL` változót a `parse_blog_sitemap.py`-ban.
{{% /details %}}

{{% details title="Melyik OpenAI modellt használja?" closed="true" %}}
A szkript alapértelmezetten GPT-4o-t használ. Változtasd meg az `API_MODEL` változót a `generate_md.py`-ban más modell használatához.
{{% /details %}}

{{% details title="Használhatom ezt Wixről Hugóra való migrációhoz?" closed="true" %}}
Igen. A kimenet standard Markdown helyi képútvonalakkal, amely közvetlenül működik Hugóval, Jekyllel, Astroval és más statikus oldalgenerátorokkal.
{{% /details %}}

{{% details title="Mennyibe kerül ehhez az OpenAI API?" closed="true" %}}
A költség a blogbejegyzéseid számától és hosszától függ. Egy tipikus blog 50 közepes hosszúságú bejegyzéssel néhány dollárba kerül API használattal GPT-4o-val.
{{% /details %}}

{{% details title="Nyílt forráskódú ez az eszköz?" closed="true" %}}
Igen. A teljes forráskód elérhető a [GitHubon](https://github.com/everappz/wix-blog-export) nyílt forráskódú licenc alatt.
{{% /details %}}
