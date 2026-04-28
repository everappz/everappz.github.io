---
title: "WebDAVを使用してNASストレージに接続し、iPhoneまたはMacで音楽を聴く方法"
date: 2024-07-28
description: "Synology NASでWebDAVを設定し、EvermusicまたはFlacboxを使用してiPhoneやMacに音楽をストリーミングする方法を学びましょう。ステップバイステップガイドに従ってください。"
keywords: ["nas接続", "webdav synology", "音楽ストリーミング nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["音楽", "ストリーミング", "ストレージ", "nas", "接続", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**要約：** Synology NASにWebDAVをインストールして有効にし、共有フォルダのアクセス権を設定し、NASのIPアドレスとWebDAVポート（デフォルト5005/5006）を使用してEvermusicまたはFlacboxから接続します。デバイスにファイルをコピーすることなく、音楽ライブラリ全体をストリーミングして管理できます。

WebDAVを使用してNASストレージに接続し、音楽ライブラリをiPhoneまたはMacに簡単にストリーミングする方法をご紹介します。WebDAV（Web-based Distributed Authoring and Versioning）は、インターネット経由でファイルを管理・共有できるプロトコルです。NASにWebDAVを設定することで、音楽コレクションにアクセスしてストリーミングでき、お気に入りの曲をいつでも手元に置くことができます。

このガイドでは、最も人気のあるNASサーバーの1つであるSynology NASでWebDAV接続を設定する方法をお見せします。Synology NASでWebDAVを設定するための簡単な手順に従えば、iPhoneまたはMacから直接音楽ライブラリを閲覧、ストリーミング、管理できるようになります。

## ステップ1：Synology NASにWebDAVをインストール

1. Synology NASにログインし、**パッケージセンター**を開きます。
2. "webdav"を検索し、まだインストールされていない場合はWebDAVパッケージをインストールします。WebDAVサーバーを開いて設定します。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="SynologyにWebDAVをインストール" width="600" >}}

## ステップ2：WebDAVサーバーの設定

1. WebDAV設定ページで、**HTTPを有効にする**、**HTTPSを有効にする**、**匿名WebDAVを有効にする**、**DavDepthInfinityを有効にする**のチェックボックスをオンにします。
2. **適用**をクリックして変更を保存します。HTTPとHTTPS接続のポート番号を確認してください。デフォルトでは5005と5006です。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="WebDAV設定の構成" width="600" >}}

## ステップ3：共有フォルダのアクセス権設定

1. **コントロールパネル**を開き、**共有フォルダ**セクションに移動します。
2. **ミュージック**フォルダを選択し、**編集**をクリックします。
3. **アクセス権**タブで、アクセス権を設定します。音楽を聴くだけの場合は読み取り専用でゲストアクセスを有効にし、ファイルを変更する必要がある場合は読み取り/書き込みで有効にします。変更を保存します。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="共有フォルダのアクセス権" width="600" >}}

## ステップ4：Synology NASのIPアドレスを確認

1. **コントロールパネル**を開き、**ネットワークインターフェース**タブに移動するか、Webブラウザで[find.synology.com](http://find.synology.com)にアクセスします。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="NASのIPアドレスを確認" width="600" >}}

2. Synology NASのIPアドレスをメモします（例：192.168.18.137）。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Synology NASのIPアドレス" width="600" >}}

## ステップ5：Evermusic/FlacboxでSynology NASに接続

1. EvermusicまたはFlacboxアプリを開き、**接続**タブに移動します。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Evermusicの接続タブ" width="600" >}}

2. 自動接続の場合、**利用可能なデバイス**セクションでSynology NASを見つけ、タップして接続します。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="利用可能なデバイスリスト" width="600" >}}

3. 手動接続の場合、**クラウドサービスに接続**を選択し、**WebDAV**を選びます。サーバーアドレスを次の形式で入力します：PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER（例：[https://192.168.18.137:5006](https://192.168.18.137:5006)）。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="手動WebDAV設定" width="600" >}}

4. ゲストアクセスの場合はログインとパスワードのフィールドを空のままにするか、Synologyの認証情報を入力します。**サインイン**をタップします。

## ステップ6：音楽をナビゲートして再生

1. 接続すると、デバイスが**接続されたアクセサリー**リストに表示されます。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Evermusicの接続済みデバイス" width="600" >}}

2. **ミュージック**フォルダに移動し、任意のオーディオファイルをタップして再生を開始します。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="ミュージックフォルダの閲覧" width="600" >}}

## ステップ7：接続したクラウドフォルダを音楽ライブラリに追加

1. アプリの**音楽ライブラリ**セクションを開きます。
2. **音楽を追加**を選択し、**接続**を選びます。
3. 接続したNASサーバーを選択し、**ミュージック**フォルダを選びます。**完了**をタップします。
4. アプリが音楽フォルダをスキャンし、サポートされているオーディオファイルを音楽ライブラリに追加します。メタデータが読み込まれ、トラックがアルバム、アーティスト、ジャンルごとにグループ化されます。

## まとめ

これらの手順に従えば、Synology NASにWebDAV接続を簡単に設定し、EvermusicまたはFlacboxを使用してiPhoneやMacに音楽ライブラリをストリーミングできます。いつでもお気に入りの曲にシームレスにアクセスしましょう。

## よくある質問

{{% details title="どのNASデバイスがWebDAVをサポートしていますか？" closed="true" %}}
Synology、QNAP、TrueNAS、Western Digitalなど、ほとんどの人気NASブランドがWebDAVをサポートしています。WebDAVのセットアップ手順については、NASメーカーのドキュメントを確認してください。
{{% /details %}}

{{% details title="NAS音楽ストリーミングにおけるWebDAVとSMBの違いは何ですか？" closed="true" %}}
WebDAVはHTTP/HTTPSで動作し、インターネット経由のリモートアクセスに適しています。SMBはローカルネットワークでは通常より高速です。EvermusicとFlacboxは両方のプロトコルをサポートしているので、ローカルアクセスかリモートアクセスかに基づいて選択してください。
{{% /details %}}

{{% details title="SynologyのWebDAVにユーザー名とパスワードは必要ですか？" closed="true" %}}
匿名WebDAVアクセスを有効にし、共有フォルダのゲスト権限を設定すれば不要です。セキュリティを強化するには、Synologyの認証情報を使用できます。
{{% /details %}}

{{% details title="WebDAV経由でNASからFLACやその他のハイレゾフォーマットをストリーミングできますか？" closed="true" %}}
はい。EvermusicとFlacboxは、WebDAV経由でNASストレージからストリーミングする際に、FLAC、ALAC、WAV、DSD、その他のハイレゾフォーマットをサポートしています。
{{% /details %}}

{{% details title="利用可能なデバイスにNASが表示されないのはなぜですか？" closed="true" %}}
iPhone/MacとNASが同じWi-Fiネットワーク上にあることを確認してください。自動検出が機能しない場合は、手動接続オプションを使用して、NASのIPアドレスとWebDAVポートを直接入力してください。
{{% /details %}}
