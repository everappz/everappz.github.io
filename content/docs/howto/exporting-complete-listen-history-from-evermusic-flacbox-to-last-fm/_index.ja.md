---
title: "Evermusic & FlacboxからLast.fmへ完全なリスニング履歴をエクスポート"
date: 2024-01-30
description: "EvermusciとFlacboxから音楽履歴をエクスポートし、CSVファイルとWindows用Last.fm Scrubblerツールを使用してLast.fmにアップロードする方法を学びましょう。"
keywords: ["evermusic", "flacbox", "lastfm", "音楽履歴", "スクロブリング", "トラックエクスポート", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "最近の項目", "lastfm", "エクスポート", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**要約:** EvermusciまたはFlacboxからリスニング履歴をCSVファイルとしてエクスポートし、Windows上の無料ツールLast.fm-Scrubbler-WPFを使用してLast.fmにアップロードします。自動スクロブリングも両方のアプリでネイティブに利用できます。

**更新:** 自動スクロブリングが利用可能になりました！詳しくはこちら： [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

スクロブリングは、現在再生中の曲のタイトルやアーティストなどの基本情報を自動的にオンラインサービスに保存するシンプルな方法です。後でリスニング履歴を確認できます。

[Last.fm](https://www.last.fm/home)は、Audioscrobblerと呼ばれる音楽レコメンデーションシステムを搭載し、このサービスを無料で提供しています。インターネットラジオ局、コンピューター、またはさまざまなポータブル音楽デバイスから聴いた曲を記録することで、音楽の好みの詳細なプロファイルを作成します。後でウェブサイトを訪問して、音楽の好みに合った新しいアーティストやアルバムの推薦を受けることができます。

無料ツールを使用して、EvermusciおよびFlacboxアプリから[Last.fm](http://Last.fm)にリスニング履歴をアップロードでき、その方法をご案内します。

アプリケーションの「ミュージックライブラリ」セクションを開き、「クイックアクセス」セクションまでスクロールします。「最近の項目」メニュー項目をタップします。

![ミュージックライブラリ画面](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

「最近の項目」画面で右上隅の「その他」ボタンをタップして「その他のアクション」メニューを有効にします。「曲リストをエクスポート」メニュー項目をタップします。

![最近の項目画面](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

「ファイル形式を選択」画面で、出力ファイルの形式を選択できます。利用可能なオプション - CSV、TXT、M3U。

![ファイル形式選択画面](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV：カンマ区切り値の略で、データを整然としたテーブル形式に整理するのに最適です。出力ファイルには、アーティスト名、アルバム名、トラック名、タイムスタンプ（トラックを聴いた時間）、アルバムアーティスト名、トラック再生時間などのパラメータがあります。

TXT：プレーンテキストファイルです。シンプルで簡単で、アーティスト名、アルバム名、トラック名、再生時間などのパラメータが含まれます。

M3U：この形式はプレイリスト作成の標準です。元のファイルがなくても（メディアファイルの絶対URLオプションを選択した場合）、曲リストをエクスポートして任意のデバイスでトラックを楽しめます。出力ファイルには、再生時間、アーティスト名、トラック名、メディアファイルの場所などのパラメータがあります。

私たちのタスクには、CSVを選択するのが正しい方法です。このファイルを無料ソフトウェアLast.fm-Scrubbler-WPFと共に使用して、リスニング履歴を[Last.fm](http://Last.fm)サービスにアップロードします。CSVを選択して「エクスポート」ボタンを押してください。

![エクスポート完了画面](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

エクスポートが完了したら、「ファイルを表示」ボタンをタップすると、アプリがドキュメントフォルダに作成されたファイルを表示します。次に、ファイル名の横にある「その他のアクション」ボタンをタップし、メニューから「で開く」オプションを選択します。次のステップは、エクスポートしたファイルをデスクトップコンピューターにコピーすることです。「で開く」メニューからAirDropオプションを選択することで簡単に行えます。

![エクスポートされたファイルのその他のアクション](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

次に、Windowsプラットフォームでのみ利用可能な無料のオープンソース[Last.FM](http://Last.FM)クライアントを使用します。このクライアントを使用すると、エクスポートしたCSVファイルを使って[Last.FM](http://Last.FM)のリスニング履歴を効率的に更新できます。

現在Windowsコンピューターを使用していなくても心配ありません。MacにVirtualBoxをインストールし、公式のWindows開発環境イメージファイルを使用することでこのクライアントにアクセスできます。

以下が必要な手順です：

- 次のリンクからVirtualBoxをインストールします：[VirtualBoxダウンロード](https://www.virtualbox.org/wiki/Downloads)

- このリンクからWindows開発環境をダウンロードしてインストールします：[Windows開発環境](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

WindowsコンピューターまたはWindows Developmentイメージを使用したVirtualBoxアプリで、[Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF)をダウンロードしてインストールします。GitHubで利用可能な無料のオープンソースソフトウェアです。バージョン1.28でテストしました。こちらからダウンロードできます：[https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Last.fm-Scrubbler-WPFダウンロードページ](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

「Assets」セクションで[Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip)をタップしてインストールアーカイブをダウンロードします。ダウンロードしたファイルを解凍し、解凍したフォルダを開きます。

- 重要

このアプリはまだベータ版です。アプリの作成者はあまりテストを行っていません。まずテストアカウントにスクロブルを試して、正しく動作するか確認することを推奨しています。特に一度に多くのトラックをスクロブルする場合は注意してください。アカウントには十分注意してください。

Last.fm-Scrubbler-WPF.exeを実行します

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

アプリケーションのメイン画面で、左下隅にある「ログインしていません」をタップして、「アカウント追加」画面を有効にします。

![アカウント追加画面](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

ログイン資格情報を入力します。

![ログイン資格情報入力画面](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

「ログイン」ボタンをタップしてアカウントを追加します。

![ログインボタンをタップしてアカウントを追加します。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

「File Parse Scrobbler」タブを開いて、EvermusciアプリからのCSVファイルのインポートを開始します。

![File Parse Scrobblerタブを開いてEvermusciアプリからCSVファイルのインポートを開始します。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

「Parser: CSV」を選択し、「設定」ボタンをタップします。

次の画面で、CSVファイルのパラメータの順序を選択できます。

個々のフィールドは引用符で囲むことができ、フィールドに設定された区切り文字が含まれている場合は引用符で囲む必要があります。例えば：

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

すべての設定をデフォルトのままにし、変更する必要があるのは「Has Fields Enclosed In Quotes」フィールドのチェックボックスを有効にすることだけです。

「保存して閉じる」をタップして変更を適用します。

![CSVファイルのパラメータの順序を選択します。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

ファイル解析スクロブリングには2つのモードがあります。「Scrobbling Mode」コンボボックスで変更できます。

通常モード：このモードでは、トラックは解析されたスクロブルのタイムスタンプでスクロブルされます。14日以内のスクロブルのみスクロブルできます。

インポートモード：このモードでは、トラックは「終了時間」と各トラック間の選択された期間から計算されたタイムスタンプでスクロブルされます。これにより、解析されたスクロブルのタイムスタンプが14日以上前であってもトラックのスクロブルが可能になります。したがって、CSVファイルの最初（最上部）のトラックは「終了時間」でスクロブルされます。

Evermusciアプリから以前に生成されたCSVファイルを「File:」フィールドで選択し、「Parse」をタップします。場合によっては、一部のスクロブルを解析できなかったというエラーアラートが表示される場合があります。アーティスト名などの完全なメタデータがない一部のトラックがある場合は問題ありません。

![一部のスクロブルを解析できませんでした](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

「すべて選択」ボタンをタップして、すべての解析されたトラックを選択します。

![すべて選択ボタンをタップしてすべての解析されたトラックを選択します。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

「プレビュー」ボタンをタップして、サーバーに投稿されるすべての変更を確認します。

![プレビューボタンをタップしてサーバーに投稿されるすべての変更を確認します。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

「Scrobble」ボタンをタップして、すべての変更をサーバーにアップロードします。

![Scrobbleボタンをタップしてすべての変更をサーバーにアップロードします。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

以前はLast.fm-Scrubbler-WPFには1日あたりのスクロブル制限がありませんでした。一部のユーザーがScrubblerを使用して非常に多くのトラックをスクロブルし、Last.fmページに問題を引き起こしたため、これは変更されました。スクロブル制限は現在1日あたり2800スクロブルです。それ以上スクロブルしようとすると、エラーメッセージが表示されます。「スクロブルキュー」を追加する計画があり、2800以上のトラックをスクロブルする必要がある場合、キューに追加され、しばらくしてから自動的にスクロブルされます。ユーザー選択ビューで残りのスクロブル数を確認できます。

すべてのレコードがサーバーに正常にアップロードされると、アプリウィンドウの下部に確認メッセージが表示されます：「選択したトラックが正常にスクロブルされました。」

![選択したトラックが正常にスクロブルされました。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

[Last.fm](http://Last.fm)ページでプロファイルを開き、すべての変更を確認できます。

![Last.fmページのプロファイル](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## よくある質問

{{% details title="CSVファイルをエクスポートせずに自動的にスクロブルできますか？" closed="true" %}}
はい。EvermusciとFlacboxの両方が、Last.fmへの自動スクロブリングをサポートしています。ガイドをご覧ください：[Last.fmへのスクロブル方法](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)。
{{% /details %}}

{{% details title="CSVに14日以上前のトラックがある場合はどうなりますか？" closed="true" %}}
Last.fm-Scrubbler-WPFのインポートモードを使用してください。終了時間からタイムスタンプを再計算し、元の日付に関係なくトラックをスクロブルできます。
{{% /details %}}

{{% details title="Windowsコンピューターを持っていません。Last.fm-Scrubblerを使用できますか？" closed="true" %}}
はい。MacにVirtualBoxをインストールし、Microsoftから無料のWindows開発環境イメージをダウンロードしてください。仮想マシン内でLast.fm-Scrubbler-WPFを実行してください。
{{% /details %}}

{{% details title="一部のスクロブルが解析されないのはなぜですか？" closed="true" %}}
アーティスト名などの重要なメタデータが不足しているトラックは解析できません。これは想定内であり、ファイル内の他のトラックには影響しません。
{{% /details %}}

{{% details title="1日のスクロブル制限はありますか？" closed="true" %}}
はい。Last.fm-Scrubbler-WPFは1日あたり最大2,800スクロブルを許可しています。それ以上必要な場合は、プロセスを複数日に分けてください。
{{% /details %}}
