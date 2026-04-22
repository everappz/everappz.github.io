---
title: "Esportare post del blog Wix in Markdown con OpenAI"
date: 2025-06-24
description: "Automatizza l'esportazione del blog Wix con Python, Selenium e OpenAI. Estrai contenuti dinamici, scarica immagini e converti HTML in Markdown pulito per Hugo o Jekyll."
keywords: ["esportazione blog Wix", "convertire HTML in markdown", "conversione markdown OpenAI", "wix in markdown", "migrazione blog SEO", "migrazione wix a hugo", "scraper beautifulsoup", "rendering HTML selenium", "automazione API OpenAI", "migrare wix a sito statico", "scraper blog wix python"]
tags: ["wix", "markdown", "migrazione blog", "openai", "scraping", "beautifulsoup", "selenium", "automazione", "SEO", "tutorial"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Perché esportare i post del blog da Wix?

**In breve:** Questa guida mostra come esportare i post del blog Wix in Markdown usando tre script Python: un runner di setup, uno scraper basato su Selenium e un convertitore HTML-in-Markdown alimentato da OpenAI. Il risultato sono file Markdown puliti e portabili pronti per Hugo, Jekyll o qualsiasi generatore di siti statici.

Wix non offre un'esportazione nativa del blog in Markdown. Se stai migrando a un generatore di siti statici come Hugo o Jekyll, devi effettuare lo scraping delle pagine renderizzate, estrarre il contenuto e convertirlo. Questo tutorial automatizza l'intero processo usando **Python, Selenium, BeautifulSoup** e l'**API GPT di OpenAI**.

La pipeline usa tre script:

- `fetch_blog_posts.sh` — configura l'ambiente ed esegue la pipeline
- `parse_blog_sitemap.py` — renderizza le pagine con Selenium, estrae il contenuto, scarica le immagini
- `generate_md.py` — converte HTML in Markdown tramite OpenAI

## Passo 1: Configurare l'ambiente

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

## Passo 2: Scraping ed estrazione del contenuto del blog

`parse_blog_sitemap.py` fa il lavoro pesante: recupera il XML della sitemap, renderizza le pagine con **Selenium**, estrae il `<div id="content-wrapper">`, scarica le immagini e salva l'HTML pulito.

**Perché Selenium anziché requests?** Wix renderizza il contenuto con JavaScript. Una semplice richiesta HTTP restituisce una pagina vuota.

## Passo 3: Convertire HTML in Markdown con OpenAI

`generate_md.py` legge ogni file `_index.html`, invia il contenuto all'API Chat di OpenAI e scrive il Markdown risultante.

## Struttura delle cartelle di output

```
downloads/
  your-post-title/
    _index.html      # HTML estratto e pulito
    _index.md         # Markdown convertito
    image1.png        # Immagini scaricate
```

## Eseguire la pipeline completa

```bash
bash fetch_blog_posts.sh
```

## Contribuisci al progetto

Il progetto è open source.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Progetto su GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Domande frequenti

{{% details title="Perché non posso semplicemente usare `requests` per lo scraping dei post Wix?" closed="true" %}}
Wix renderizza il contenuto dinamicamente con JavaScript. Una richiesta HTTP standard restituisce una pagina vuota. Selenium esegue un browser headless per ottenere l'HTML completamente renderizzato.
{{% /details %}}

{{% details title="Funziona con qualsiasi blog Wix?" closed="true" %}}
Sì. Lo scraper legge l'XML della sitemap del blog e processa ogni URL. Basta aggiornare la variabile `SITEMAP_URL` in `parse_blog_sitemap.py`.
{{% /details %}}

{{% details title="Quale modello OpenAI viene usato?" closed="true" %}}
Lo script usa GPT-4o per impostazione predefinita. Puoi cambiare la variabile `API_MODEL` in `generate_md.py`.
{{% /details %}}

{{% details title="Posso usare questo per migrare da Wix a Hugo?" closed="true" %}}
Sì. L'output è Markdown standard con percorsi immagine locali, che funziona direttamente con Hugo, Jekyll, Astro e altri generatori di siti statici.
{{% /details %}}

{{% details title="Quanto costa l'API OpenAI per questo?" closed="true" %}}
Il costo dipende dal numero e dalla lunghezza dei tuoi post. Un blog tipico con 50 post di lunghezza media costa pochi dollari di utilizzo API con GPT-4o.
{{% /details %}}

{{% details title="Questo strumento è open source?" closed="true" %}}
Sì. Il codice sorgente completo è disponibile su [GitHub](https://github.com/everappz/wix-blog-export) con licenza open source.
{{% /details %}}
