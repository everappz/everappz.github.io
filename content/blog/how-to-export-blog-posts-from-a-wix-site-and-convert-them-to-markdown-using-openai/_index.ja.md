---
title: "OpenAIでWixブログ記事をMarkdownにエクスポート"
date: 2025-06-24
description: "Python、Selenium、OpenAIを使用してWixブログのエクスポートを自動化。動的コンテンツの抽出、画像のダウンロード、HTMLからHugoやJekyll用のクリーンなMarkdownへの変換。"
keywords: ["Wixブログエクスポート", "HTMLをmarkdownに変換", "OpenAI markdown変換", "wixからmarkdown", "SEOブログ移行", "wixからhugo移行", "beautifulsoupスクレイパー", "selenium HTMLレンダリング", "OpenAI API自動化", "wixから静的サイトに移行", "wixブログスクレイパーpython"]
tags: ["wix", "markdown", "ブログ移行", "openai", "スクレイピング", "beautifulsoup", "selenium", "自動化", "SEO", "チュートリアル"]
draft: false
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## なぜWixからブログ記事をエクスポートするのか？

**要約：** このガイドでは、3つのPythonスクリプトを使用してWixブログ記事をMarkdownにエクスポートする方法を説明します：セットアップランナー、Seleniumベースのスクレイパー、OpenAI搭載のHTML-Markdownコンバーター。結果は、Hugo、Jekyll、その他の静的サイトジェネレーター用のクリーンでポータブルなMarkdownファイルです。

WixにはMarkdownへのネイティブブログエクスポート機能がありません。HugoやJekyllのような静的サイトジェネレーターに移行する場合、レンダリングされたページをスクレイプし、コンテンツを抽出して変換する必要があります。このチュートリアルは**Python、Selenium、BeautifulSoup**、**OpenAIのGPT API**を使用してプロセス全体を自動化します。

パイプラインは3つのスクリプトを使用：

- `fetch_blog_posts.sh` — 環境をセットアップしパイプラインを実行
- `parse_blog_sitemap.py` — Seleniumでページをレンダリング、コンテンツを抽出、画像をダウンロード
- `generate_md.py` — OpenAI経由でHTMLをMarkdownに変換

## ステップ1：環境のセットアップ

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

## ステップ2：ブログコンテンツのスクレイプと抽出

`parse_blog_sitemap.py`が重い処理を担当：サイトマップXMLを取得、**Selenium**でページをレンダリング、`<div id="content-wrapper">`を抽出、画像をダウンロード、クリーンなHTMLを保存。

**なぜrequestsではなくSelenium？** WixはJavaScriptでコンテンツをレンダリングします。通常のHTTPリクエストでは空のページシェルが返されます。

## ステップ3：OpenAIでHTMLをMarkdownに変換

`generate_md.py`は各`_index.html`ファイルを読み込み、OpenAIのChat APIにコンテンツを送信し、結果のMarkdownを書き込みます。

## 出力フォルダ構造

```
downloads/
  your-post-title/
    _index.html      # 抽出・クリーニング済みHTML
    _index.md         # 変換済みMarkdown
    image1.png        # ダウンロード済み画像
```

## パイプライン全体の実行

```bash
bash fetch_blog_posts.sh
```

## プロジェクトへの貢献

プロジェクトはオープンソースです。

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/wix-blog-export" title="GitHubのプロジェクト" icon="github" tag="open source" >}}
{{< /cards >}}

---

## よくある質問

{{% details title="Wixブログ記事のスクレイプに`requests`を使えないのはなぜ？" closed="true" %}}
WixはJavaScriptで動的にコンテンツをレンダリングします。標準的なHTTPリクエストでは空のページシェルが返されます。Seleniumはヘッドレスブラウザを実行して完全にレンダリングされたHTMLを取得します。
{{% /details %}}

{{% details title="どのWixブログでも動作しますか？" closed="true" %}}
はい。スクレイパーはブログのサイトマップXMLを読み取り、各URLを処理します。`parse_blog_sitemap.py`の`SITEMAP_URL`変数を更新するだけです。
{{% /details %}}

{{% details title="どのOpenAIモデルを使用していますか？" closed="true" %}}
スクリプトはデフォルトでGPT-4oを使用します。`generate_md.py`の`API_MODEL`変数を変更して別のモデルを使用できます。
{{% /details %}}

{{% details title="WixからHugoへの移行に使えますか？" closed="true" %}}
はい。出力はローカル画像パス付きの標準Markdownで、Hugo、Jekyll、Astroなどの静的サイトジェネレーターで直接動作します。
{{% /details %}}

{{% details title="OpenAI APIの費用はいくらですか？" closed="true" %}}
費用はブログ記事の数と長さによります。中程度の長さの記事50件の一般的なブログで、GPT-4oのAPI使用料は数ドルです。
{{% /details %}}

{{% details title="このツールはオープンソースですか？" closed="true" %}}
はい。完全なソースコードは[GitHub](https://github.com/everappz/wix-blog-export)でオープンソースライセンスの下で利用可能です。
{{% /details %}}
