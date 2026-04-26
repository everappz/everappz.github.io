---
title: "Flacbox 1.6：自動同期、イコライザー、OPUSサポート"
date: 2017-01-25
description: "Flacbox 1.6 for iOSに自動クラウド同期、10バンドイコライザー、OPUSフォーマットサポート、iPhone・iPad向け外部フラッシュドライブ再生が追加されました。"
keywords: ["Flacboxアップデート", "FLACプレーヤーiOS", "10バンドイコライザーiPhone", "自動音楽同期", "iPhoneでOPUS再生", "外部フラッシュドライブ音楽", "FLACストリーミングiOS", "Hi-Res音楽アプリiPhone", "Flacboxイコライザー", "SDカード音楽プレーヤーiOS"]
tags: ["Flacbox", "イコライザー", "音楽ライブラリ", "OPUS", "FLAC", "外部ストレージ", "同期", "オーディオプレーヤー", "iOSアプリ", "アップデート"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**Flacbox 1.6**はiPhone・iPad向けFLAC音楽プレーヤーに主要な新機能をもたらします。

**要約：** このアップデートでは、自動クラウドライブラリ同期、カスタムプリセット付き10バンドイコライザー、OPUSフォーマットサポート、外部SDカードからの音楽再生機能が追加されました。FLAC再生のバグも修正されています。

## Flacbox 1.6の新機能

### 自動クラウド音楽ライブラリ同期

ライブラリを手動でリフレッシュする必要はもうありません。新しい同期エンジンが選択したクラウドフォルダを自動的にスキャンし、音楽ライブラリをリアルタイムで更新します。

- 有効化：**Settings → Music Library → Automatic Sync**
- フォルダ選択：**Sync Folder → Change Settings**
- 同期モードの選択：Wi-Fiのみ、またはWi-Fi + セルラー
- プレーヤーがアクティブな間の自動更新には**Background Sync**を有効化（バッテリー消費が増加します）

手動操作なしでクラウド音楽コレクションが最新の状態に保たれます。

### カスタムサウンドのための10バンドイコライザー

プレーヤー画面または設定からアクセスできる内蔵**10バンドイコライザー**でオーディオを調整します。

- **-12 dB**から**+12 dB**の間で周波数を調整
- 内蔵プリセットを使用するか、独自のプリセットを作成
- プリアンプパワーの微調整（聴力保護のため注意して使用）

iPhone・iPadでスタジオレベルのオーディオコントロールが可能です。

### OPUSファイルフォーマットサポート

FlacboxでFLAC、ALAC、MP3などのフォーマットに加え、**OPUS**ファイルの再生が可能になりました。OPUSは音声と音楽に広く使用される高効率コーデックです。OPUS再生にはイコライザーの完全サポートが含まれています。

### 外部SDカードからの音楽再生

iPhone・iPadに接続したSDまたはmicroSDカードから直接音楽を再生：

- **Lightning to SD Card Camera Readerアダプタ**を使用
- カードを挿入してデバイスに接続
- Flacboxを開く -- カードを自動的に認識
- **Services → PowerDrive**セクションからファイルを閲覧・再生

デバイスのストレージを使用せずに音楽ライブラリを拡張するのに最適です。

### FLAC再生バグの修正

**FLACファイルの末尾での2秒スキップ**が完全に解決されました。トラックが最初から最後までシームレスに再生されるようになりました。

## Flacboxをダウンロード

Flacbox 1.6はApp Storeで利用可能です。[Flacboxをダウンロード](https://itunes.apple.com/us/app/flacbox-flac-player-music/id1097564256?mt=8)して、これらの機能を今すぐお試しください。

フィードバックや機能リクエストはありますか？ご連絡ください -- ユーザーのニーズに基づいてFlacboxを開発しています。

## よくある質問

{{% details title="Flacboxはどのオーディオフォーマットに対応していますか？" closed="true" %}}
FlacboxはFLAC、ALAC、MP3、AAC、OGG、OPUS、WAV、AIFF、DSDなどの人気オーディオフォーマットに対応しています。すべてのフォーマットが内蔵イコライザーで動作します。
{{% /details %}}

{{% details title="iPhoneでSDカードから音楽を再生できますか？" closed="true" %}}
はい。Lightning to SD Card Camera Readerアダプタを使用してSDまたはmicroSDカードを接続します。Flacboxはカードを自動的に検出し、外部ストレージから直接ファイルを閲覧・再生できます。
{{% /details %}}

{{% details title="Flacboxはクラウドストレージと自動的に同期しますか？" closed="true" %}}
はい。バージョン1.6から、Flacboxはクラウドフォルダから音楽ライブラリを自動的に同期できます。設定で自動同期を有効にし、監視するフォルダを選択してください。
{{% /details %}}

{{% details title="Flacboxのイコライザーはカスタマイズできますか？" closed="true" %}}
はい。10バンドイコライザーでは、-12 dBから+12 dBの間で個別の周波数レベルを調整できます。内蔵プリセットを使用するか、独自のカスタム設定を保存できます。
{{% /details %}}
