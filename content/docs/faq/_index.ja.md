---
date: '2025-06-12T17:00:00+00:00'
title: 'よくある質問'
description: 'Evermusic、Flacbox、Evervideo、Evertag に関するよくある質問への回答を見つけましょう。クラウドストリーミング、ファイル管理、再生オプション、メタデータ編集などの機能を探索できます。'
keywords: [
  "Evermusic FAQ", "Flacbox サポート", "Evervideo ヘルプ", "Evertag 質問",
  "Evermusic の使い方", "クラウド音楽プレーヤーのトラブルシューティング", "オフライン再生ガイド",
  "オーディオタグエディタサポート", "ビデオストリーミングの問題", "ファイル転送チュートリアル"
]
tags: [
  "FAQ", "ヘルプ", "サポート", "evermusic", "flacbox", "evervideo", "evertag",
  "クラウド設定", "再生の問題", "ファイル管理", "メタデータ編集",
  "トラブルシューティング", "オフラインモード", "音楽プレーヤー", "ビデオプレーヤー"
]
---


{{< lottie src="/images/juicy-json/juicy-woman-focused-on-online-learning.json" width="85%" >}}

## アプリの使い方を学びましょう

アプリの使用方法についての回答やサポートをお探しですか？ここが正しい場所です。

FAQ ページでは、クラウドストレージの接続、音楽やビデオファイルの管理、オフライン再生の設定、イコライザー設定の調整、メタデータの修正などをサポートしています。

始めるには以下のアプリの FAQ をご覧ください。または、ユーザーから受け取ったメールからよくある質問と回答も参照できます。

## アプリを選択してください

{{< cards cols="2">}}

{{< card 
  link="/docs/faq/evervideo" 
  title="Evervideo" 
  subtitle="360° ビデオを再生し、iCloud からストリーミングし、字幕付きで視聴し、ビデオイコライザーを適用し、プレイリストでコンテンツを整理し、オフライン視聴のためにビデオをダウンロードできます。"
  image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< card 
  link="/docs/faq/evermusic"
  title="Evermusic" 
  subtitle="オフラインモード、オーディオイコライザー、クロスフェード、ギャップレス再生、プレイリスト管理、完全な音楽ライブラリ、組み込みファイルマネージャーを備えたクラウド音楽プレーヤー。"
  image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/flacbox"
  title="Flacbox" 
  subtitle="iPhone と Mac 向けの高解像度オーディオプレーヤー。FLAC、ALAC、APE、DSD などのロスレス形式を再生できます。高度なオーディオ設定で出力を細かく調整できます。"
  image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/evertag"
  title="Evertag" 
  subtitle="一括編集機能付きのスマートな音楽タグエディタ。欠落したメタデータ、アルバムカバーなどを修正できます。ID3、FLAC、APE タグを編集 — 120 以上のフィールドに対応。" 
  image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< /cards >}}

## よくある問題と回答

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{% details title="古い iOS バージョン (15.8.4) で pCloud にログインできないのはなぜですか？" closed="true" %}}
pCloud のウェブログインページは、15.8.4 などの古い iOS バージョンでは正しく表示されないことがあり、クラウド接続画面でメールアドレスとパスワードを入力できない場合があります。<br><br>

回避策として、pCloud でサポートされており、すべての iOS バージョンで確実に動作する **WebDAV** プロトコルを使用できます。

**WebDAV の設定:**<br>
- **US サーバー:** `https://webdav.pcloud.com`  
- **ヨーロッパサーバー:** `https://ewebdav.pcloud.com`  
- **ユーザー名:** pCloud のメールアドレス  
- **パスワード:** pCloud アカウントのパスワード  

アプリを開く → 接続 → クラウドストレージに接続 → **WebDAV** を選択 → 認証情報とサーバー URL を入力。

この方法を使用すると、古いデバイスでも問題なく pCloud ストレージに接続してファイルにアクセスできます。
{{% /details %}}

{{% details title="Mac (macOS) から AirPlay で音楽を再生するには？" closed="true" %}}
アプリの macOS 版には、iOS のような AirPlay、Chromecast、Bluetooth の接続ボタンが内蔵されていません。<br><br>

MacBook Pro で **AirPlay** を使用するには、次の手順に従ってください：

1. 画面の**右上隅**に移動し、**コントロールセンター**を開きます（時計の近く）。  
2. **サウンド/音量**アイコンをクリックします。  
3. 次の画面で **AirPlay** をクリックして、利用可能なすべての AirPlay デバイスの一覧を表示します。  
4. 音楽のストリーミングを開始するために希望のデバイスを選択します。  

これにより、すべてのシステムオーディオ（Evermusic または Flacbox からのものを含む）が選択した AirPlay デバイスにルーティングされます。
{{% /details %}}

{{% details title="iPhone で購入した場合、Mac で Premium が有効化されないのはなぜですか？" closed="true" %}}
永続購入とサブスクリプションは **iCloud** を通じて iOS と Mac 間で同期されます。<br><br>

Mac で Premium を有効化するには：<br>
- 両方のデバイスに最新バージョンのアプリがインストールされていることを確認してください<br>
- 両方のデバイスで **iCloud** を有効にしてください<br>
- iOS デバイスでアプリを起動し、購入情報がアップロードされるまで 1 分待ってください<br>
- Mac では、**同じ Apple ID** を使用して App Store からアプリをインストールしてください<br>
- アプリを起動し、情報が同期されるまで数秒待ってください<br>
- または、両方のデバイスのアプリ設定で**購入を復元**をタップしてください<br><br>

その後、Premium 機能が Mac で自動的に有効化されます。
{{% /details %}}

{{% details title="デバイス間でプレイリストを自動同期するには？" closed="true" %}}
現在、プレイリストの**自動同期はありません**。<br><br>

次のいずれかの方法を使用できます：<br>
- アプリ設定からの**バックアップと復元** [Evermusic でデバイス間で音楽ライブラリを転送する方法：ステップバイステップガイド](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/)<br>
- **プレイリストを M3U にエクスポート**し、別のデバイスにインポートする：<br>
  - [プレイリストのエクスポート方法](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/)<br>
  - [プレイリストのインポート方法](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/)<br>
- **プレイリストやアルバムをアーカイブ**して ZIP で転送：<br>
  - [プレイリストアーカイブガイド](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to/)
{{% /details %}}

{{% details title="アプリの使用は安全ですか？分析を無効にできますか？" closed="true" %}}
はい、お客様のプライバシーが私たちの最優先事項です。<br><br>

- 音楽ファイル、設定、クラウドログインなど、すべてのデータはデバイス上に保管されます<br>
- ログイン認証情報は **iOS Keychain** に安全に保存されます<br>
- 匿名のクラッシュと使用状況レポートのみを収集します<br>
- **アプリ設定 → 分析**でオプトアウトできます<br><br>

詳細情報：<br>
- [プライバシーポリシー](/legal/privacy-policy/)<br>
- [Apple Keychain セキュリティ](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web)<br><br>

パーソナライズされた広告を使用する場合、Google Mobile Ads は同意設定の表示を必要とします。<br>
Premium ユーザーには広告が表示されず、広告 SDK は完全に無効化されています。
{{% /details %}}

{{% details title="アプリはファミリー共有をサポートしていますか？" closed="true" %}}
はい、ファミリー共有はサポートされています。<br><br>

アプリ内購入を共有するには：<br>
- 購入がファミリーグループと共有するように設定されていることを確認してください<br>
- ファミリーメンバーのデバイスで、**設定 > 購入 > 購入を復元**に移動してください<br>
- これにより Apple のサーバーから購入データが要求され、そのデバイスで有効化されます
{{% /details %}}

{{% details title="メタデータとクラウドの同期を高速化するには？" closed="true" %}}
同期速度を向上させるには、バックグラウンドタスクを有効にしてください：<br><br>

- **設定 → 音楽ライブラリ → メタデータ読み取り → バックグラウンドでのメタデータ読み取り**<br>
- **設定 → 音楽ライブラリ → オンライン音楽同期 → バックグラウンド同期**<br><br>

また、macOS では **設定 → 音楽ライブラリ**からメタデータの読み取り速度を上げることができます。<br>
プレーヤーがアクティブな場合（オーディオ再生中）、iOS はアプリをサスペンドしないため、継続的な同期が可能です。
{{% /details %}}

{{% details title="サブスクリプションをキャンセルするには？" closed="true" %}}
Apple の公式手順に従ってサブスクリプションをキャンセルできます：<br>
👉 [サブスクリプションのキャンセル方法](https://support.apple.com/en-us/118428)
{{% /details %}}

{{% details title="WD MyCloud EX2 Ultra から音声を接続してストリーミングするには？" closed="true" %}}

アプリで **接続 > クラウドストレージに接続 > My Cloud Home** を通じて接続を追加すると、これは公式に **WD MyCloud Home** デバイスをサポートするように設計されています。<br>
WD MyCloud EX2 Ultra はアプリに対して制限されたアクセスを使用します。<br><br>

ただし、**WD MyCloud EX2 Ultra**、**WD MyCloud Mirror**、または別の **WD MyCloud** ストレージモデルへの接続に成功した場合は、次の回避策で引き続き使用できます：<br><br>

1. **接続 → クラウドストレージに接続 → My Cloud Home** を開く<br>
2. 内蔵ファイルマネージャーを使用してフォルダを作成する<br>
3. このフォルダに音楽ファイルをアップロードする<br>
4. これらはアプリのみがアクセスできる「サンドボックス」に保存されます<br>
5. 直接ストリーミングまたはダウンロードできるようになります<br><br>

⚠️ アプリを通じて作成されたフォルダのみが NAS からアクセス可能です。
{{% /details %}}

{{% details title="Koofr.eu に接続するには？" closed="true" %}}
**WebDAV** を使用して Koofr を接続できます。<br><br>

- Koofr WebDAV 設定ガイド: [koofr.eu blog](https://koofr.eu/blog/posts/3-ways-to-map-koofr-as-a-network-drive-explained)<br>
- Evermusic/Flacbox WebDAV ガイド: [WebDAV を使用して NAS ストレージに接続し iPhone または Mac で音楽を聴く方法](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)
{{% /details %}}

{{% details title="アプリの URL スキームは何ですか？" closed="true" %}}
サポートされているスキームは次のとおりです：<br><br>

**Evermusic**<br>
- iOS (青いアイコン): `lsevermusic://`<br>
- macOS: `lsevermusicmac://`<br>
- iOS (赤いアイコン): `lsevermusicpro://`<br><br>

**Flacbox**<br>
- iOS: `lsflap://`<br>
- macOS: `lsflapmac://`<br><br>

**Evertag**<br>
- iOS: `lsevertag://`<br>
- macOS: `lsevertagmac://`<br><br>

**Evervideo**<br>
- iOS: `lsevervideo://`<br>
- macOS: `lsevervideomac://`
{{% /details %}}

{{% details title="アプリがバックグラウンドにあるとき音楽が止まる — 修正方法は？" closed="true" %}}
アプリがバックグラウンドでクラッシュまたは一時停止する場合：<br>
- **設定 > 音楽ライブラリ > オンライン音楽同期 > バックグラウンド同期 → 無効**に移動する<br>
- **設定 > 音楽ライブラリ > メタデータ読み取り > バックグラウンドでのメタデータ読み取り → 無効**<br>
- **設定 > ファイルマネージャー > バックグラウンド転送 → 無効**
{{% /details %}}

{{% details title="ギャップレス再生が機能しない — 修正方法は？" closed="true" %}}
ギャップレス再生は iOS バージョンとオーディオエンジンによって異なります。<br>
オーディオエンジンを切り替えてみてください：<br>
- **設定 → オーディオプレーヤー → 一般 → オーディオプロセッサ**に移動する<br>
- より良いギャップレスサポートのために **Core Audio** を選択する
{{% /details %}}

{{% details title="アプリがリストに 100 個しか表示されないのはなぜですか？" closed="true" %}}
アプリはパフォーマンスのためにページネーションを使用しています。<br>
無効にするには：<br>
- **設定 → カスタマイズ → コンテンツ読み込み制限 → 無効**に移動する<br>
これですべてのアイテムが一度に読み込まれます。
{{% /details %}}

{{% details title="メタデータに奇妙な文字があるのはなぜですか？" closed="true" %}}
メタデータの正規化を有効にしてみてください：<br>
- **設定 → 音楽ライブラリ → メタデータ読み取り → メタデータエンコーディングの正規化**
{{% /details %}}

{{% details title="アプリが特殊文字を含むフォルダ名を読み取れないのはなぜですか？" closed="true" %}}
これは **SMB2 プロトコル**の既知の問題です。<br><br>

次の解決策を試してください：<br>
- サーバーとアプリの設定で **SMB1** を有効にする<br>
- **システムファイルピッカー**を使用する：<br>
  - **ローカルファイル > このデバイスのファイル > ファイルを開く...**に移動する<br>
  - Apple のネイティブメニューを使用してフォルダ/ファイルを選択する<br><br>

または、NAS がサポートしている場合は **WebDAV** または **DLNA** を使用して接続してください。
{{% /details %}}

{{% details title="iCloud で音楽をアップロードして管理するには？" closed="true" %}}
– **iCloud に音楽をアップロードするには？**  <br>
ブラウザで [https://www.icloud.com](https://www.icloud.com) にアクセスし、フォルダを作成して、Mac または PC から直接音楽ファイルをアップロードします。<br>

– **iCloud ストレージを管理するには？**  <br>
2 つのオプションがあります：  <br>
1. ブラウザで [https://www.icloud.com](https://www.icloud.com) を使用してファイルを整理、アップロード、または削除する。<br>  
2. アプリで、**接続 → クラウドストレージに接続 → iCloud Drive** を通じて iCloud に接続した後、内蔵ファイルマネージャーを使用して、デバイスに保存することなく iCloud ストレージ内のファイルを直接アップロード、ダウンロード、フォルダの名前変更、またはファイルの削除ができます。<br>

⚠️ ファイルを削除するときは注意してください。アプリは永久に削除します（ゴミ箱に入らず、復元できません）。<br>

詳細はこちら: [iPhone または Mac で iCloud Drive から音楽をストリーミングする方法](/docs/howto/how-to-listen-to-music-from-icloud-drive-on-your-iphone-or-mac/)

{{% /details %}}

{{% details title="Windows 11 から iPhone に 10GB の音楽ライブラリをオフライン再生のために転送するには？" closed="true" %}}

Windows 11 PC から iPhone に音楽ライブラリを移動し、アプリでオフラインで使用するための信頼性の高いいくつかのオプションがあります。最適な方法を選択してください：

1. **ケーブル接続を使用する（大きなライブラリに推奨）**  <br>
   Windows 11 の **Apple Devices** アプリを使用して、USB 経由で iPhone に直接ファイルを転送します。  
   こちらの Apple のガイドに従ってください：  
   https://support.apple.com/en-ph/120402 <br>

2. **Wi-Fi Drive を使用してワイヤレスで**  <br>
   アプリ内の **WiFi Drive** 機能を有効にして、コンピューターのブラウザから音楽をアップロードします。  
   ステップバイステップの手順はこちら：  
   [WiFi-Drive を使用して iTunes なしでコンピューターから iPhone に音楽ファイルを転送する方法](/docs/howto/how-to-transfer-music-from-computer-to-iphone-without-itunes/) <br>

3. **DLNA サーバーを使用してワイヤレスで**  <br>
   Windows コンピューターで DLNA メディアサーバーをオンにして、ライブラリを直接アプリにストリーミングまたは転送します。  
   ガイド：  
   [Windows 10 で DLNA メディアサーバーを有効にして iPhone で音楽を再生する方法](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/) <br>

4. **SMB ファイル共有を使用してワイヤレスで**  <br>
   PC で **SMB ファイル共有**を有効にして、アプリで接続してファイルをフォルダごとに参照、ダウンロード、または転送します。  
   手順：  
   [SMB プロトコルを使用してコンピューターから iPhone にファイルを転送する](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/) <br>

⚠️ 大きなライブラリ（10GB 以上）を転送する場合、有線 USB 転送が通常最も速く安定したオプションです。

{{% /details %}}

</div>
