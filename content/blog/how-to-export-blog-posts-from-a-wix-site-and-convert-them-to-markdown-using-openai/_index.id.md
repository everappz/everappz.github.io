---
title: "Ekspor Postingan Blog Wix ke Markdown dengan OpenAI"
date: 2025-06-24
description: "Otomasi ekspor blog Wix menggunakan Python, Selenium, dan OpenAI. Ekstrak konten dinamis, unduh gambar, dan konversi HTML ke Markdown bersih untuk Hugo atau Jekyll."
keywords: ["ekspor blog Wix", "konversi HTML ke markdown", "konversi markdown OpenAI", "wix ke markdown", "migrasi blog SEO", "migrasi wix ke hugo", "scraper beautifulsoup", "render HTML selenium", "otomasi API OpenAI", "migrasi wix ke situs statis", "scraper blog wix python"]
tags: ["wix", "markdown", "migrasi blog", "openai", "scraping", "beautifulsoup", "selenium", "otomasi", "SEO", "tutorial"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Mengapa Mengekspor Postingan Blog dari Wix?

**Ringkasan:** Panduan ini menunjukkan cara mengekspor postingan blog Wix ke Markdown menggunakan tiga skrip Python: runner setup, scraper berbasis Selenium, dan konverter HTML-ke-Markdown yang didukung OpenAI. Hasilnya adalah file Markdown bersih dan portabel yang siap untuk Hugo, Jekyll, atau generator situs statis apa pun.

Wix tidak menawarkan ekspor blog native ke Markdown. Jika Anda bermigrasi ke generator situs statis seperti Hugo atau Jekyll, Anda perlu meng-scrape halaman yang dirender, mengekstrak konten, dan mengonversinya. Tutorial ini mengotomasi seluruh proses menggunakan **Python, Selenium, BeautifulSoup**, dan **API GPT OpenAI**.

Pipeline menggunakan tiga skrip:

- `fetch_blog_posts.sh` — menyiapkan lingkungan dan menjalankan pipeline
- `parse_blog_sitemap.py` — merender halaman dengan Selenium, mengekstrak konten, mengunduh gambar
- `generate_md.py` — mengonversi HTML ke Markdown melalui OpenAI

## Langkah 1: Siapkan Lingkungan

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

## Langkah 2: Scrape dan Ekstrak Konten Blog

`parse_blog_sitemap.py` melakukan pekerjaan berat: mengambil XML sitemap, merender halaman dengan **Selenium**, mengekstrak `<div id="content-wrapper">`, mengunduh gambar, dan menyimpan HTML bersih.

**Mengapa Selenium bukan requests?** Wix merender konten dengan JavaScript. Permintaan HTTP standar mengembalikan shell halaman kosong.

## Langkah 3: Konversi HTML ke Markdown dengan OpenAI

`generate_md.py` membaca setiap file `_index.html`, mengirim konten ke API Chat OpenAI, dan menulis Markdown yang dihasilkan.

## Struktur Folder Output

```
downloads/
  your-post-title/
    _index.html      # HTML yang diekstrak dan dibersihkan
    _index.md         # Markdown yang dikonversi
    image1.png        # Gambar yang diunduh
```

## Jalankan Pipeline Lengkap

```bash
bash fetch_blog_posts.sh
```

## Kontribusi ke Proyek

Proyek ini open source.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="Proyek di GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Pertanyaan yang Sering Diajukan

{{% details title="Mengapa tidak bisa menggunakan `requests` untuk meng-scrape postingan blog Wix?" closed="true" %}}
Wix merender konten secara dinamis dengan JavaScript. Permintaan HTTP standar mengembalikan shell halaman kosong. Selenium menjalankan browser headless untuk mendapatkan HTML yang sepenuhnya dirender.
{{% /details %}}

{{% details title="Apakah ini berfungsi dengan blog Wix mana pun?" closed="true" %}}
Ya. Scraper membaca XML sitemap blog dan memproses setiap URL. Cukup perbarui variabel `SITEMAP_URL` di `parse_blog_sitemap.py`.
{{% /details %}}

{{% details title="Model OpenAI mana yang digunakan?" closed="true" %}}
Skrip menggunakan GPT-4o secara default. Ubah variabel `API_MODEL` di `generate_md.py` untuk model berbeda.
{{% /details %}}

{{% details title="Bisakah menggunakan ini untuk migrasi dari Wix ke Hugo?" closed="true" %}}
Ya. Output-nya adalah Markdown standar dengan path gambar lokal, yang berfungsi langsung dengan Hugo, Jekyll, Astro, dan generator situs statis lainnya.
{{% /details %}}

{{% details title="Berapa biaya API OpenAI untuk ini?" closed="true" %}}
Biaya tergantung pada jumlah dan panjang postingan blog Anda. Blog khas dengan 50 postingan panjang sedang menghabiskan beberapa dolar penggunaan API dengan GPT-4o.
{{% /details %}}

{{% details title="Apakah alat ini open source?" closed="true" %}}
Ya. Kode sumber lengkap tersedia di [GitHub](https://github.com/everappz/wix-blog-export) di bawah lisensi open source.
{{% /details %}}
