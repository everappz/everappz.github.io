---
title: "Izvezite Wix blog postove u Markdown s OpenAI"
date: 2025-06-24
description: "Automatizirajte izvoz Wix bloga koristeći Python, Selenium i OpenAI. Izvucite dinamički sadržaj, preuzmite slike i pretvorite HTML u čisti Markdown za Hugo ili Jekyll."
keywords: ["izvoz Wix bloga", "pretvorba HTML u markdown", "OpenAI pretvorba u markdown", "wix u markdown", "SEO migracija bloga", "wix u hugo migracija", "beautifulsoup scraper", "selenium renderiranje HTML", "OpenAI API automatizacija", "migracija wix na statičku stranicu", "wix blog scraper python"]
tags: ["wix", "markdown", "migracija bloga", "openai", "scraping", "beautifulsoup", "selenium", "automatizacija", "SEO", "vodič"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Zašto izvoziti blog postove s Wixa?

**Ukratko:** Ovaj vodič pokazuje kako izvesti Wix blog postove u Markdown koristeći tri Python skripte: pokretač za postavljanje, Selenium-bazirani scraper i OpenAI-pokretan pretvarač HTML-u-Markdown. Rezultat su čiste, prenosive Markdown datoteke spremne za Hugo, Jekyll ili bilo koji generator statičkih stranica.

Wix ne nudi izvorni izvoz bloga u Markdown. Ako migrirate na generator statičkih stranica poput Huga ili Jekyla, trebate scrapati renderirane stranice, izvući sadržaj i pretvoriti ga. Ovaj vodič automatizira cijeli proces koristeći **Python, Selenium, BeautifulSoup** i **OpenAI GPT API**.

Pipeline koristi tri skripte:

- `fetch_blog_posts.sh` — postavlja okruženje i pokreće pipeline
- `parse_blog_sitemap.py` — renderira stranice sa Seleniumom, izvlači sadržaj, preuzima slike
- `generate_md.py` — pretvara HTML u Markdown putem OpenAI

## Korak 1: Postavite okruženje

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

## Korak 2: Scrapajte i izvucite sadržaj bloga

`parse_blog_sitemap.py` obavlja glavni posao: dohvaća sitemap XML, renderira stranice sa **Selenium**, izvlači `<div id="content-wrapper">`, preuzima slike i sprema očišćeni HTML.

**Zašto Selenium umjesto requests?** Wix renderira sadržaj JavaScriptom. Standardni HTTP zahtjev vraća praznu stranicu. Selenium pokreće headless Chrome preglednik.

## Korak 3: Pretvorite HTML u Markdown s OpenAI

`generate_md.py` čita svaku `_index.html` datoteku, šalje sadržaj OpenAI Chat API-ju i zapisuje rezultirajući Markdown.

## Struktura izlaznih mapa

```
downloads/
  your-post-title/
    _index.html      # Izvučeni i očišćeni HTML
    _index.md         # Pretvoreni Markdown
    image1.png        # Preuzete slike
```

## Pokrenite cijeli pipeline

```bash
bash fetch_blog_posts.sh
```

## Doprinesite projektu

Projekt je otvorenog koda.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Projekt na GitHubu" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Često postavljana pitanja

{{% details title="Zašto ne mogu jednostavno koristiti `requests` za scrapanje Wix blog postova?" closed="true" %}}
Wix renderira sadržaj dinamički JavaScriptom. Standardni HTTP zahtjev vraća praznu stranicu. Selenium pokreće headless preglednik za potpuno renderirani HTML.
{{% /details %}}

{{% details title="Radi li ovo s bilo kojim Wix blogom?" closed="true" %}}
Da. Scraper čita XML sitemapa bloga i obrađuje svaki URL. Samo ažurirajte varijablu `SITEMAP_URL` u `parse_blog_sitemap.py`.
{{% /details %}}

{{% details title="Koji OpenAI model se koristi?" closed="true" %}}
Skripta koristi GPT-4o prema zadanim postavkama. Možete promijeniti varijablu `API_MODEL` u `generate_md.py`.
{{% /details %}}

{{% details title="Mogu li ovo koristiti za migraciju s Wixa na Hugo?" closed="true" %}}
Da. Izlaz je standardni Markdown s lokalnim putanjama slika, koji radi izravno s Hugom, Jekyllom, Astrom i drugim generatorima statičkih stranica.
{{% /details %}}

{{% details title="Koliko košta OpenAI API za ovo?" closed="true" %}}
Cijena ovisi o broju i duljini vaših blog postova. Tipičan blog s 50 postova umjerene duljine košta nekoliko dolara korištenja API-ja s GPT-4o.
{{% /details %}}

{{% details title="Je li ovaj alat otvorenog koda?" closed="true" %}}
Da. Potpuni izvorni kod dostupan je na [GitHubu](https://github.com/everappz/wix-blog-export) pod licencom otvorenog koda.
{{% /details %}}
