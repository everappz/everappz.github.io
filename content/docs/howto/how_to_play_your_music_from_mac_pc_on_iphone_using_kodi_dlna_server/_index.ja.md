---
title: "Kodi DLNAサーバーを使用してMac / PC / Linux / NASの音楽をiPhoneで再生する方法"
date: 2025-07-25
description: "Kodi DLNAとEvermusicアプリを使用して、Wi-Fi経由でコンピューターやNASからiPhoneに音楽をストリーミングします。"
keywords: ["kodi dlnaサーバー", "iphoneに音楽をストリーミング", "nasから音楽を再生", "evermusic dlna", "macからiphoneへ音楽", "windowsからiphoneへ音楽", "kodi dlna iphone", "dlnaオーディオストリーミング"]
tags: ["dlna", "kodi", "evermusic", "iphone", "音楽ストリーミング", "mac", "nas", "linux", "ローカルネットワーク"]
readingTime: 5
---

{{< author-byline >}}


**概要：** Mac、PC、Linux、またはNASにKodiをインストールし、DLNA/UPnPサーバーを有効にして、無料のEvermusicまたはFlacboxアプリを使用してWi-Fi経由で音楽ライブラリ全体をiPhoneまたはiPadにストリーミングします。サブスクリプションは不要です。

## はじめに

**Mac、Windows PC、Linuxマシン、またはNASデバイス**をお持ちであれば、無料でオープンソースのメディアプラットフォームである[Kodi](https://kodi.tv/)を使用して、自宅で簡単に**パーソナル音楽サーバー**に変えることができます。Kodiの内蔵**DLNA/UPnPサーバー**を使えば、音楽ライブラリ全体をDLNA対応のクライアント（iPhoneやiPadを含む）にストリーミングできます。

このガイドでは、以下の手順をステップバイステップで説明します：

- MacまたはPCにKodiをインストールする  
- 音楽フォルダを共有用に設定する  
- DLNA音楽サーバーを有効にする  
- **Evermusic**または**Flacbox** iOSアプリを使用して音楽にアクセスする

このセットアップは100%無料です。サブスクリプションなし、Wi-Fiネットワーク上で自分の音楽をストリーミングするだけです。大きなMP3コレクションを整理したい場合、Wi-Fi経由でFLACを聴きたい場合、またはiTunesで同期せずにローカル音楽を楽しみたい場合、このセットアップは最適です。

## Mac / PC / Linux / NASにKodiをダウンロードしてインストールする

まず、Kodiの公式ウェブサイトにアクセスします：

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Kodiメインページ" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

**ダウンロード**をクリックし、お使いのコンピューター用のバージョンを見つけるためにスクロールします。オペレーティングシステムを選択してください。この例では**macOS**を使用します。

{{< cards cols="1">}}
{{< card subtitle="Kodiダウンロードページ" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Intel Macの場合は**Intel (x86/64)**を、M1、M2、M3 Macの場合は**Apple Silicon**をクリックしてダウンロードを開始します。

{{< cards cols="1">}}
{{< card subtitle="macOSインストーラーを選択" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

インストーラーのダウンロード中、少々お待ちください。

{{< cards cols="1">}}
{{< card subtitle="Kodiダウンロード完了" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

ダウンロード後、**ダウンロード**フォルダで`.dmg`ファイルを見つけてください。

{{< cards cols="1">}}
{{< card subtitle="Kodiをインストール" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

ダウンロードしたファイルをダブルクリックしてインストーラーを起動します。Kodiを**アプリケーション**フォルダにドラッグしてインストールします。

{{< cards cols="1">}}
{{< card title="" subtitle="Kodiをアプリケーションにドラッグしてインストール" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Kodiを起動します。**システム環境設定 → セキュリティとプライバシー → このまま開く**で許可が必要な場合があります。

{{< cards cols="1">}}
{{< card subtitle="Kodiメイン画面" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Kodiライブラリに音楽を追加する

ホーム画面から**歯車アイコン**（設定）をクリックします。

{{< cards cols="1">}}
{{< card subtitle="Kodi設定" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

**メディア設定 → ライブラリ**に移動します。自動インデックス作成のために、ビデオライブラリと音楽ライブラリの**起動時にライブラリを更新**を有効にします。

{{< cards cols="1">}}
{{< card subtitle="ライブラリ設定" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

次に**音楽**セクションに移動し、**音楽を追加**をクリックします。

{{< cards cols="1">}}
{{< card subtitle="音楽フォルダを追加" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

音楽が保存されているフォルダを参照して選択します。

{{< cards cols="1">}}
{{< card subtitle="音楽ソースを選択" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

音楽ソースをKodiに追加します。

{{< cards cols="1">}}
{{< card subtitle="音楽ソースを追加" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

確認し、Kodiに音楽ライブラリをスキャンさせます。

{{< cards cols="1">}}
{{< card subtitle="音楽ソースを確認" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

ライブラリのスキャンと構築が完了するまで少々お待ちください。

{{< cards cols="1">}}
{{< card subtitle="音楽ライブラリをスキャン中" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## KodiのDLNAサーバーを有効にする

**設定 → サービス → UPnP/DLNA**に移動します。

オプションを有効にします：**ライブラリを共有する**。

Kodiはローカルのwi-Fiネットワーク上でDLNAサーバーとして機能するようになりました。

{{< cards cols="1">}}
{{< card subtitle="KodiでDLNAを有効にする" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Kodiライブラリを開く

右クリックして設定ウィンドウを閉じ、Kodiメインライブラリを開きます。

{{< cards cols="1">}}
{{< card title="" subtitle="右クリックでKodiライブラリにアクセス" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## iOS用音楽ストリーミングアプリをダウンロード

さまざまなクラウドストレージサービスやDLNAサーバーから音楽をストリーミングできる無料のiOS DLNAクライアントアプリを入手してください。

- コレクションが主にMP3やその他の標準オーディオ形式の場合は**Evermusic**を使用してください。
- FLAC、ALAC、DSDなどの形式のハイレゾ音楽ライブラリがある場合は**Flacbox**を選択してください。

両アプリとも**iOS**と**macOS**で利用可能で、無料で使用できます。

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Evermusicをダウンロード" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Flacboxをダウンロード" icon="download" tag="Free" >}}
{{< /cards >}}

## DLNAソースを追加

iOSアプリをダウンロードしたら、**すべての接続**セクションを開きます。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusicアプリのメインサイドバー" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

下にスクロールして**ローカルネットワーク - 利用可能なデバイス**をタップしてDLNAサーバーを検出します。このセクションでは、ローカルネットワーク上のすべての利用可能なデバイスが表示されます。**Kodi DLNAサーバー**がここに表示されるはずです。Kodiサーバーをタップして接続します。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusicで利用可能なDLNAデバイス" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

EvermusicはKodiを通じて共有されたライブラリフォルダを表示します。

{{< cards cols="1">}}
{{< card title="" subtitle="EvermusicのKodi音楽ライブラリ" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

**曲**フォルダに移動して、DLNAサーバー上のすべての利用可能なオーディオファイルを表示します。

{{< cards cols="1">}}
{{< card title="" subtitle="リモートフォルダからリストされた曲" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

任意のオーディオファイルをタップして、即座にストリーミングを開始します。

{{< cards cols="1">}}
{{< card title="" subtitle="EvermusicでMP3ファイルを再生" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

**接続**セクションに戻ります。追加されたDLNAサーバーがここに表示されます。いつでもそのアイコンをタップして再接続できます。同じ手順でこの画面から他のクラウドサービスも接続できます。

ここで**Last.fmスクロブリング**も有効にできます。再生統計がLast.fmアカウントに保存され、後でパーソナライズされた音楽のおすすめを提供します。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusicの接続" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## 音楽ライブラリを構築

**Evermusic**と**Flacbox**の両方で、音楽をライブラリに追加し、アーティスト、アルバム、ジャンル、作曲家などの**メタデータタグ**で整理できます。

まず、**音楽ライブラリ**セクションを開きます。**ツールと設定**まで下にスクロールし、**音楽を追加**をタップします。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic音楽ライブラリ" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

音楽ソースを選択します — この場合、**接続**を選択します。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusicで新しい音楽を追加" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

接続で**Kodi DLNAサーバー**を見つけ、タップしてフォルダとファイルを表示します。

{{< cards cols="1">}}
{{< card title="" subtitle="音楽インポート用のDLNAサーバーを選択" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

追加したいフォルダまたはファイルを選択し、**完了**をタップします。

{{< cards cols="1">}}
{{< card title="" subtitle="追加する音楽フォルダを選択" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

アプリが選択したファイルをスキャンし、メタデータを使用してアーティスト、アルバム、ジャンル、作曲家などのセクションに整理します。

{{< cards cols="1">}}
{{< card title="" subtitle="カテゴリ付き音楽ライブラリ" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## プレイリストを作成

独自のプレイリストも作成できます。

まず、**プレイリスト**タブを開きます。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusicのプレイリストタブ" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

**プラス（+）**ボタンをタップし、**新しいプレイリスト**を選択します。

{{< cards cols="1">}}
{{< card title="" subtitle="新しいプレイリストを作成" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

プレイリストの名前を入力し、**保存する**をタップします。

{{< cards cols="1">}}
{{< card title="" subtitle="プレイリスト名を入力" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

次に、曲を追加するソースを選択します — ここでは**ライブラリ**を選択します。

{{< cards cols="1">}}
{{< card title="" subtitle="新しいプレイリストに曲を追加" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

希望の曲を選択し、**完了**をタップして追加します。

{{< cards cols="1">}}
{{< card title="" subtitle="ライブラリからプレイリストに音楽を追加" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

選択したトラックが作成されたプレイリストに表示されます。

{{< cards cols="1">}}
{{< card title="" subtitle="作成されたプレイリストがリストに表示" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

デフォルトでは、曲はストリーミングで利用可能です。オフラインで聴くには、**オフラインモード**を有効にしてください — アプリがすべてのプレイリストトラックをダウンロードします。

{{< cards cols="1">}}
{{< card title="" subtitle="プレイリストのオフラインモードが有効" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

**その他のアクション**ボタンをタップして、追加オプションを確認します。以下のことができます：

- プレイリストをアーカイブする  
- アルバムカバーを変更する  
- トラックを並べ替える  
- その他の便利な機能

{{< cards cols="1">}}
{{< card title="" subtitle="プレイリストのその他のアクション" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## まとめ

**Evermusic**と**Flacbox**を使えば、iPhone、iPad、またはMacを強力なDLNA音楽プレーヤーに変えるのは簡単です。クラウド、NAS、または**Kodi**のようなホームメディアサーバーに音楽を保存していても、これらのアプリでコレクションを制限なくストリーミング、整理、楽しむことができます。

- **Kodi DLNAサーバー**からMP3やハイレゾFLACを直接ストリーミング  
- メタデータ（アルバム、ジャンル、作曲家）でグループ化されたパーソナル音楽ライブラリを構築  
- **カスタムプレイリスト**を作成・管理  
- 移動中の視聴に**オフラインモード**を有効化  
- **複数のクラウドサービス**や**ローカルネットワークデバイス**に接続  
- **Last.fm連携**でリスニング習慣を追跡

オーディオファイルでもカジュアルリスナーでも、EvermusicとFlacboxはシームレスな音楽ストリーミングと整理に必要なすべてを提供します。

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Evermusicをダウンロード" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Flacboxをダウンロード" icon="download" tag="Free" >}}
{{< /cards >}}

今日からあなたのパーソナル音楽体験を構築しましょう。

## よくある質問

{{% details title="KodiはDLNAサーバーとして無料ですか？" closed="true" %}}
はい。Kodiは完全に無料でオープンソースです。macOS、Windows、Linux、多くのNASデバイスで動作します。
{{% /details %}}

{{% details title="EvermusicとFlacboxはDLNA経由のFLACストリーミングに対応していますか？" closed="true" %}}
はい。FlacboxはFLAC、ALAC、DSDなどのハイレゾフォーマットに最適化されています。EvermusicもMP3やその他の標準フォーマットとともにFLAC再生をサポートしています。
{{% /details %}}

{{% details title="Kodiからストリーミングした後、オフラインで聴けますか？" closed="true" %}}
はい。任意のプレイリストでオフラインモードを有効にすると、アプリがすべてのトラックをデバイスにダウンロードし、ネットワーク接続なしで聴けます。
{{% /details %}}

{{% details title="DLNAを使用するにはプレミアムサブスクリプションが必要ですか？" closed="true" %}}
無料版は最大3つのクラウドまたはネットワーク接続をサポートします。プレミアムはこの制限を解除し、無制限のサービスとDLNAサーバーに接続できます。
{{% /details %}}

{{% details title="iPhoneはKodiと同じWi-Fiネットワークにある必要がありますか？" closed="true" %}}
はい。DLNAストリーミングはローカルネットワーク上で動作します。KodiサーバーとiOSデバイスの両方が同じWi-Fiネットワークに接続されている必要があります。
{{% /details %}}

{{% details title="MacやPCの代わりにNASでこのセットアップを使用できますか？" closed="true" %}}
はい。多くのNASデバイス（Synology、QNAPなど）はKodiをサポートしているか、独自の内蔵DLNAサーバーを持っています。EvermusicとFlacboxは、任意の標準DLNA/UPnPサーバーに接続できます。
{{% /details %}}
