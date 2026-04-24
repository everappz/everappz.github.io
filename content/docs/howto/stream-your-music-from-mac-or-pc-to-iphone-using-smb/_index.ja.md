---
title: "SMBを使用してMacまたはPCからiPhoneに音楽をストリーミング"
description: "EvermusicとSMBプロトコルを使用して、MacまたはWindows PCからiPhoneまたはiPadに音楽コレクションをストリーミングする方法を学びましょう。同期なしで接続してオーディオを楽しむためのシンプルなステップバイステップガイド。"
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["MacからiPhoneに音楽をストリーミング", "SMBオーディオストリーミングiOS", "Evermusic SMB設定", "PC音楽をiPhoneに接続", "Mac音楽共有iOS", "SMB Windowsファイルストリーミング", "Evermusic PCフォルダアクセス"]
aliases:
  - /post/stream-your-music-from-mac-or-pc-to-iphone-using-smb/
  - /single-post/Stream-your-music-from-MAC-or-PC-to-iPhone-using-SMB/
---

{{< author-byline >}}


**要約：** iPhone または iPad 用の Evermusic アプリを使用して、SMB 経由でローカルネットワーク上の Mac または Windows PC から音楽をストリーミングします。同期不要、コピー不要 -- コンピュータでファイル共有を有効にし、アプリで接続して再生するだけです。セットアップは5分以内で完了します。

MAC や PC に大量の音楽があり、iPhone や iPad で手軽に楽しみたいですか？Evermusic がその答えです。Evermusic を使えば、SMB プロトコルでコンピュータに接続し、デバイスの容量を気にしたり同期の手間を心配したりすることなく、お気に入りの曲をストリーミングするのが驚くほど簡単です。始めるためのステップバイステップガイドはこちらです：

## ステップ1：コンピュータでSMBプロトコルを有効にする

![Evermusic - SMBサポート - Mac共有画面](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### MACを使用している場合

- システム環境設定 -> 共有を開きます。
- ファイル共有サービスを有効にします。
- 「共有フォルダ」セクションで、音楽フォルダを追加し、ユーザーを選択して、権限レベル（読み書きまたは読み取り専用）を設定します。
- さらに便利にするために、音楽フォルダに「全員：読み取り専用」を選択すると、Evermusic で簡単にアクセスできます。
- 次のステップのために、コンピュータの URL（smb://192.168.xx.xx）を覚えておいてください。

![Evermusic - SMBサポート - ファイル共有画面](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- 「オプション」をタップし、「SMBを使用してファイルとフォルダを共有」を有効にします。
- 利用可能なアカウントの「Windows ファイル共有」を有効にします。

![Evermusic - SMBサポート - ファイルとフォルダの共有画面](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Windows PCを使用している場合

![Evermusic - SMBサポート - Windowsでのファイル共有](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- 音楽フォルダを右クリックします。
- 「プロパティ」を選択します。
- 「共有」タブを開きます。
- 「共有...」をクリックします。
- 共有する相手を選び、権限レベルを設定します。
- MACと同様に、選択した音楽フォルダに「全員：読み取り」を選択できます。
- 「完了」をクリックして設定を保存します。

![Evermusic - SMBサポート - Windowsでの共有フォルダ](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## ステップ2：コンピュータを自動的に追加する

- Evermusic を開き、「接続」タブ（古いアプリバージョンを使用している場合は「ネットワーク」）に移動します。
- 「利用可能なデバイス」（古いアプリバージョンを使用している場合は「利用可能な共有」）セクションにコンピュータが表示され、前のステップで「全員：読み取り専用」を選択した場合は、コンピュータをタップするだけで自動的に接続されます。
- これが機能しない場合は、手動でコンピュータを追加できます。

![Evermusic - SMBサポート - アカウント接続画面](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## ステップ3：コンピュータを手動で追加する

- 「クラウドサービスに接続」（古いアプリバージョンを使用している場合は「アカウントを追加」）をタップします。
- 次の画面で利用可能なサーバーのリストから「SMB」を選択します。
- 「SMB」設定画面で：
  - 共有フォルダのパスを含むサーバーURLを入力します。サーバー名またはサーバーIPを入力できます。例：
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - ログイン名とパスワードを入力するか、前のステップで「全員：読み取り専用」を選択した場合はこれらのフィールドを空白のままにします。
  - 「WORKGROUP」フィールドはオプションで、Active Directory ドメインがある場合に使用します。

![Evermusic - SMBサポート - 資格情報入力画面](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

SMBアカウントを接続すると、「クラウドサービス」（「アカウント」）セクションに表示されます。接続されたアカウントをタップして開き、音楽フォルダに移動して、任意のオーディオファイルをタップしてプレーヤーを起動します。

![Evermusic - SMBサポート - 接続フォルダを開く画面](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Evermusic で iPhone または iPad で音楽コレクションをシームレスにお楽しみください。

![Evermusic - SMBサポート - オーディオプレーヤー画面](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## ステップ4：SMB2の回避策

フォルダの閲覧や特殊文字（ü、ö、éなど）を含むファイルの再生に問題が発生した場合、SMB2プロトコルに関連している可能性があります。この問題の解決に積極的に取り組んでいます。

一時的な解決策として、サーバーとアプリの設定でSMB 1を有効にしてみてください。または、システムのファイルオープンメニューを使用してSMBサーバーに接続できます。方法は以下の通りです：

1. 「ローカルファイル」に移動します。
2. 「このデバイス上のファイル」セクションまでスクロールし、「ファイルを開く...」または「フォルダを開く...」をタップします。
3. サーバーを見つけ、必要なファイルまたはフォルダを選択します。
4. 「開く」をタップして選択を確認します。

## ステップ5：WebDAVの回避策

さらに、サポートされている場合は、WebDAVまたはDLNAプロトコルを使用してNASに接続することもできます。

これらの手順に従うことで、ファイル名の特殊文字に関連する問題を回避し、メディアファイルを引き続き楽しむことができます。

追記：iTunes ファイル共有を使用して MAC/PC から iPhone にオーディオファイルを転送し、ローカルオーディオファイルを再生することもできます。この機能の詳細については、ガイドをご覧ください：[iPhoneでiTunesファイルを再生する方法](/docs/howto/how-to-play-local-itunes-files-on-my-iphone)。

## よくある質問

{{% details title="iTunesなしでPCからiPhoneに音楽をストリーミングできますか？" closed="true" %}}
はい。Evermusic はローカル Wi-Fi ネットワーク上で SMB を介して PC に接続します。iTunes は不要です。PC でファイル共有を有効にし、アプリで接続するだけです。
{{% /details %}}

{{% details title="SMBストリーミングはモバイルデータを使用しますか？" closed="true" %}}
いいえ。SMB はローカル Wi-Fi ネットワーク上で動作します。インターネット接続やモバイルデータは不要です。
{{% /details %}}

{{% details title="EvermusicはSMB経由でどのオーディオフォーマットをサポートしていますか？" closed="true" %}}
Evermusic は MP3、FLAC、AAC、WAV、AIFF、OGG、WMA、ALAC、その他の一般的なオーディオフォーマットをサポートしています。ファイルは SMB 共有から直接再生されます。
{{% /details %}}

{{% details title="NASからiPhoneに音楽をストリーミングできますか？" closed="true" %}}
はい。NAS が SMB をサポートしている場合（Synology、QNAP、WD My Cloud を含むほとんどがサポートしています）、このガイドと同じ手順で接続できます。
{{% /details %}}

{{% details title="ストリーミング中はコンピュータの電源を入れておく必要がありますか？" closed="true" %}}
はい。Evermusic はコンピュータから直接ファイルをストリーミングするため、電源が入っていて iPhone と同じネットワークに接続されている必要があります。
{{% /details %}}

{{% details title="SMBストリーミングにファイルサイズの制限はありますか？" closed="true" %}}
いいえ。Evermusic は SMB 経由で任意のサイズのファイルをストリーミングします。大きなロスレスファイル（FLAC、WAV）も問題なく動作します。
{{% /details %}}
