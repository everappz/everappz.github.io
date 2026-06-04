---
date: 2020-01-01
title: 'Flacbox'
description: 'Flacboxの使い方を学びましょう — iPhone、iPad、Mac向けのhi-res FLAC、DSD、ALAC、FFmpeg対応クラウド音楽プレーヤー。iCloud Drive、Google Drive、Dropbox、OneDrive、MEGA、Box、pCloud、Synology、QNAP、NAS、WebDAV、SMB、DLNAを接続できます。高解像度オーディオのストリーミングとダウンロード、メタデータの編集、オーディオブックの再生、Last.fmへのスクロブル、Apple CarPlayとホーム画面ウィジェットの使用、10バンドイコライザーのカスタマイズが可能です。'
keywords: [
  "Flacboxユーザーガイド", "Flacboxの使い方", "hi-res音楽プレーヤーiPhone", "FLACプレーヤーiPhone",
  "DSDプレーヤーiOS", "ALACプレーヤーMac", "ロスレス音楽アプリ", "クラウド音楽プレーヤーiPhone",
  "オフラインFLACプレーヤーMac", "音楽ライブラリ管理", "オーディオタグエディタ",
  "CarPlay FLACプレーヤー", "Chromecastオーディオアプリ", "AirPlay 2音楽",
  "Flacboxウィジェット", "Flacbox CarPlay", "FFmpeg音楽プレーヤーiOS",
  "オーディオブックプレーヤーiPhone", "オーディオブックマークiOS", "ピッチ補正音楽アプリ",
  "オーディオ出力サンプルレート", "外部DACiPhone", "USB DAC Mac",
  "Synology音楽アプリ", "QNAP音楽アプリ", "NAS音楽プレーヤーiPhone",
  "WebDAV音楽プレーヤー", "SMB音楽ストリーミング", "DLNA音楽プレーヤー",
  "iCloud Drive音楽", "Google Drive FLAC", "Dropbox FLACプレーヤー",
  "Wi-Fi Drive音楽転送", "M3Uプレイリストインポート", "Last.fmスクロブリング"
]
tags: ["flacbox", "ガイド", "hi-res", "FLAC", "FFmpeg", "クラウド", "CarPlay", "ウィジェット"]
---


### Flacboxガイドへようこそ

Flacboxは、iPhone、iPad、Mac向けの高解像度音楽プレーヤーで、お気に入りのクラウドストレージ、NAS、メディアサーバーを個人のストリーミングサービスに変えることができます。

Flacboxは驚くほど幅広いソースに接続します。すべて1つのアプリで：

- **個人用クラウドストレージ：** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **セルフホストサーバー：** Plex · Jellyfin · Emby · Subsonic（およびすべてのSubsonic互換サーバー — Airsonic、Funkwhale、Gonic、Logitech Media Server、Ampache）· Navidrome · Nextcloud（共有APIを介したownCloudを含む）· Synology Drive · QNAP.
- **NASおよびファイル共有プロトコル：** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP（パスワードまたは公開鍵認証）· NFS · DLNA / UPnP（再生とダウンロード）。Apple Time Capsule、Synology、QNAP、WD My Cloud、任意のLinux Samba / NFS / SSHホスト、またはMacやWindows PCの共有フォルダーで動作します。
- **S3互換オブジェクトストレージ：** AWS S3、Backblaze B2、Wasabi、Cloudflare R2、MinIO、DigitalOcean Spaces、およびその他のS3 APIエンドポイント。
- **ローカルネットワーク検出：** 利用可能なデバイスセクションは、Wi-Fi上のすべてのBonjour / mDNSサービスを自動的にリストします — Plex、Jellyfin、Embyサーバー、Synology、QNAP、ドライブが接続されたAirPortルーター、Time Capsule — IPアドレスを入力せずにタップして接続できます。

ほとんどの音楽アプリがAppleの組み込みオーディオエンジンを使用しているのに対し、FlacboxはシステムコーデックとともにFFmpegをバンドルしているため、iOSがネイティブでサポートしていない形式を再生できます — WMA、OGG、OPUS、APE、DSD、DSF、DFF、TTA、MPC、WV、および通常のMP3 / AAC / M4A / WAV / AIFF / ALAC / FLACファミリー。設定可能なオーディオ出力サンプルレート（44.1 / 48 / 64 / 88.2 / 96 kHz）、マルチチャンネル出力（Mono → 5.1 → SDDS → ITU BS.775-1）、IOバッファーの調整、ピッチ補正と組み合わせることで、Flacboxはほとんどのコンシューマー向け音楽アプリでは提供されないコントロールをオーディオファイルに提供します。

### スムーズなストリーミングとオフライン再生を楽しむ

Flacboxはスムーズなストリーミングのためのスマートバッファリングと、プレイリスト、アーティスト、アルバム、フォルダー、または個々のトラックをデバイスにダウンロードしてオフラインで使用できる組み込みダウンロードマネージャーを備えています。ストレージが少なくなったら、1タップでキャッシュされたファイルを削除してクラウドからのストリーミングを続けることができます。フォルダー、プレイリスト、アルバム、アーティストのオフラインモードは、クラウドに新しいトラックが追加されると自動的に同期するため、オフラインコレクションは常に最新の状態に保たれます。

### 自動的に整理された音楽ライブラリ

オーディオトラックをインポートすると、Flacboxはそのメタデータをスキャンし、整理された音楽ライブラリに組み込みます — 曲、未再生の曲、アルバム、アルバムアーティスト、アーティスト、ジャンル、作曲家でグループ化されます。組み込み検索を使用して数秒で何でも見つけ、ソース（オンラインクラウド / オフライン / デバイス）でフィルタリングし、プレーン / グループ / タブ付きライブラリレイアウトを選択できます。混合の「様々なアーティスト」コンピレーションを含むライブラリには、Flacboxがすべてのアルバム / 専用アルバム / ソロアルバムビューを提供します。

### メタデータを修正して音楽にタグを付ける

破損したタグや乱雑なエンコーディングに遭遇した場合（リップされたファイルや古いファイルでよくある問題）、組み込みのID3 Tagsエディターで修正できます — 手動またはMusicBrainzの自動検索で。壊れた文字エンコーディングを正規化したり（Windows PCから来たキリル文字、日本語、中国語のタグに最適）、欠けているアルバムアートを検索したり、変更をクラウドの元のファイルに自動的に書き戻したりすることもできます。より深いバッチ編集には、コンパニオンアプリのEvertagをインストールしてください。

### Mac、PC、またはNASからの簡単な転送

これらのツールのいずれかを使用してコンピューターとiPhoneまたはiPadの間で音楽を移動できます：SMB、WebDAV、DLNA、Wi-Fi Drive（任意のデスクトップブラウザーでドラッグアンドドロップ）、LightningまたはUSB-CケーブルでのiTunes / Finderファイル共有、USBフラッシュドライブ、またはiXpand Flash Drive。Apple Time Capsule、WD My Cloud、Synology、QNAP、またはSMB / WebDAV / DLNA / FTP / SFTPを公開するその他のNASをお持ちですか？一度接続するだけで、デバイスのストレージを使わずにライブラリ全体をストリーミングできます。

### イコライザーでサウンドをカスタマイズ

Flacboxには、iPodスタイルのプリセット（アコースティック、バスブースター、クラシック、ダンス、ロック、ポップ、ジャズなど）を備えた10バンドイコライザー、プリアンプ、独自のプリセットを保存する機能が含まれています。オーディオファイルIEM、HomePod mini、またはカーステレオ向けに調整する場合でも、好みのサウンドを正確に形成できます。

### オーディオブック対応

Flacboxは優れたオーディオブックプレーヤーです — トラックごとに複数のブックマーク、細かく調整可能な再生速度（0.02×〜3.00×）、停止した正確な位置から再生を続ける機能、カスタマイズ可能なスキップ時間ボタン、就寝前にゆっくりフェードアウトするスリープタイマー。M4Bチャプターマーカーと長いファイルは完全にサポートされています。

### どこでもストリーミング — 車内とホーム画面でも

AirPlay 2を介してApple TV / HomePodに音楽をストリーミングし、Google Chromecastスピーカーおよびキャスト対応TVに送信し、Apple CarPlayで外出先でもすべてを楽しみましょう。iPhoneとiPadのホーム画面ウィジェットを使用して再生中のトラックをひと目で確認し、Last.fmスクロブリングでアプリをまたいで試聴履歴を保持できます。

### プライバシーとセキュリティ

Flacboxは各クラウドプロバイダーの公式SDKとOAuthベースのログインのみを使用しています — パスワードがアプリに届くことはありません。アクセストークンはiOS Keychainで暗号化して保存され、すべての転送はTLSで保護されており、クラウドアカウントでのアクセス取り消しやデバイスからのFlacboxの削除により、すべてが即座に削除されます。プライバシーの追加レイヤーとしてオプションのパスコードでライブラリを保護できます。

### Flacboxを始める

このガイドでは、iPhone、iPad、MacでのFlacboxのすべての部分を説明します — クラウドサービスの接続、ライブラリの整理、ファイルの転送、プレイリストの管理から、イコライザーの微調整とオーディオエンジンの設定まで。以下のカードを使用して必要なセクションに直接ジャンプしてください。

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="ナビゲーション" subtitle="iPhoneのタブバー、iPadとMacの左メニュー、ミニプレーヤー、ウィジェット、CarPlay。" >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="接続" subtitle="iCloud、Google Drive、Dropbox、OneDrive、NAS、WebDAV、SMB、DLNA。" >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="音楽ライブラリ" subtitle="曲、アルバム、アーティスト、ジャンル、作曲家 — 同期、検索、メタデータ編集。" >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="プレイリスト" subtitle="M3U / M3U8 / CUEの作成、インポート、並べ替え、M3U / CSV / TXTへのエクスポート。" >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="ローカルファイル" subtitle="オフライン音楽、USBドライブ、Wi-Fi Drive、ファイルマネージャー、オフラインフォルダー。" >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="オーディオプレーヤー" subtitle="Hi-res出力、イコライザー、ピッチ、ブックマーク、AirPlay、Chromecast、速度、スリープタイマー。" >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="設定" subtitle="オーディオエンジン、ライブラリ、ファイルマネージャー、CarPlay、ウィジェット、パーソナライズ、言語、バックアップ。" >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="よくある質問" subtitle="Flacboxに関する最もよくある50の質問への回答を見つけましょう。" >}}

{{< /cards >}}
