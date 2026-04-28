---
title: "Synology NASを接続してiPhoneやMacで音楽を聴く方法"
date: 2024-09-19
description: "ネイティブAPIまたはQuickConnectを使用してSynology NASを接続し、EvermusicとFlacboxでiPhoneやMacに高品質な音楽をストリーミングする方法を学びましょう。"
keywords: ["synology nas", "音楽ストリーミング", "quickconnect", "evermusic synology", "flacbox synology", "nasミュージックプレーヤー", "iphone nas音楽"]
tags: ["音楽", "ストリーミング", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**概要：** SynologyのネイティブAPIを使用して、IPアドレスによる手動接続またはQuickConnect IDによる自動接続で、Synology NASをEvermusicまたはFlacboxに接続します。QuickConnectを使用すると、ポート転送なしでリモートから音楽をストリーミングできます。両方のアプリはFLAC、MP3、WAV、その他のハイレゾフォーマットをサポートしています。

Synology NASを接続してiPhoneやMacで音楽ライブラリを楽しむシームレスな方法をお探しなら、EvermusicとFlacboxアプリが最適なソリューションです。これらのアプリはFLAC、MP3、WAVを含む幅広いオーディオフォーマットをサポートしており、Synology NASから直接高品質な音楽をストリーミングして聴くことが簡単にできます。

このガイドでは、SynologyのネイティブAPIとQuickConnect機能を使用して、Synology NASをEvermusicまたはFlacboxアプリに接続する方法を説明します。Synologyの直接APIを活用することで、WebDAV、SMB、DLNAなどの複雑な設定を必要とせずに、ホームネットワーク外から安全に音楽ライブラリにアクセスできます。QuickConnectを使用すれば、iPhoneやMacを使ってどこからでも音楽をストリーミングして管理できます。

## ステップ1：共有フォルダのアクセス権を設定する（オプション）

1. **コントロールパネル**を開き、**共有フォルダ**セクションに移動します。

![共有フォルダ](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. **ミュージック**フォルダを選択し、**編集**をクリックします。

3. **アクセス権**タブでアクセス権を設定します。音楽を聴くだけなら読み取り専用でゲストアクセスを有効にし、ファイルを変更する必要がある場合は読み取り/書き込みを有効にします。変更を保存します。

![アクセス権](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## ステップ2：Synology NASのIPアドレスを確認する

1. **コントロールパネル**を開き、**ネットワークインターフェース**タブに移動します。

![ネットワークインターフェース](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. または、Webブラウザを使用して[find.synology.com](http://find.synology.com)にアクセスします。

![Synologyを検索](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Synology NASのIPアドレスをメモします（例：192.168.18.137）。

## ステップ3：Synology NASのネットワークポートを確認する

DSMのデフォルトネットワークポートに関するSynologyの公式ドキュメントは、この[Synologyナレッジセンターの記事](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services)で確認できます。

Synology DSMは以下のデフォルトポートを使用します：
- **HTTP（Webアクセス）：** ポート**5000**
- **HTTPS（セキュアWebアクセス）：** ポート**5001**

これらはDSMインターフェースにアクセスするためのデフォルトポートです。

![ネットワークポート](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## ステップ4：QuickConnect ID機能を有効にする

Synology QuickConnect IDは、ポート転送などの複雑なネットワーク設定を構成することなく、インターネット経由でSynology NASにリモートアクセスできる一意の識別子です。QuickConnectは、QuickConnect IDを通じてNASとスマートフォンやコンピュータなどのデバイス間の接続を確立するためにSynologyのサーバーを使用し、リモートアクセスを簡素化します。

**QuickConnect IDの確認または設定方法：**

1. **DSMにログインします。**
2. **コントロールパネル > 外部アクセス > QuickConnect**に移動します。
3. **QuickConnectを有効にし**、一意のQuickConnect IDを作成または確認します。

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## ステップ5：EvermusicまたはFlacboxを使用してiPhone/MacでSynology NASに接続する

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198)と[Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256)は、iOSおよびmacOSデバイス向けに設計された音楽プレーヤーアプリで、それぞれが音楽ライブラリの管理と楽しみのための独自の機能と能力を提供します。

1. EvermusicまたはFlacboxアプリを開き、**接続**タブに移動します。

![接続](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. **クラウドサービスを接続**を選択し、**Synology Drive**を選択します。

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

2つの接続オプションがあります：サーバーのIPアドレスとポートを使用する**手動**接続、またはQuickConnect IDによる**自動**接続です。

### 手動接続

手動方法では、前のステップで取得した直接IPアドレスとポート番号が必要です。

1. ステップ2で取得したサーバーURLを次の形式で入力します：プロトコル://IPアドレス:ポート番号
   - HTTPには**ポート5000**、HTTPS接続には**ポート5001**を使用します。

   例：
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. 実際のポート番号はセットアップのステップ3で確認できます。
3. Synology NASの**ログイン名**と**パスワード**を入力します。
4. **サインイン**をタップして接続を確立します。

![手動接続](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### 自動接続

自動接続では、ステップ4の**QuickConnect ID**を使用します。Synology NASのIPアドレスとポート番号を手動で入力する代わりに、**QuickConnect ID**を入力するだけです。アプリが自動的に必要な接続情報を取得します。

この方法により、ホームネットワーク外からでもリモートでNASにアクセスでき、ポート転送や静的IPアドレスの設定なしにインターネットからファイルを管理できます。

![自動接続](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## 二要素認証

DSM 4.2から、Synologyはセキュリティを強化するために**2段階認証**を導入しました。この機能では、通常のログイン資格情報に加えて、認証アプリによって生成された**ワンタイムパスワード（OTP）**コードが必要です。2段階認証を有効にしている場合、ユーザー名とパスワードを入力した後、DSMセッションにログインするためにOTPも入力する必要があります。

セッションが期限切れになると、アプリを手動で再認証する必要があることにご注意ください。再認証するには：

1. アプリの**接続**タブに移動します。
2. サーバー名の横にある**その他のアクション**ボタンをタップします。
3. メニューから**設定**を選択して新しい認証コードを入力し、再認証プロセスを完了します。

これにより、信頼されていないネットワークからNASにアクセスしても、データの安全が保たれます。

## ステップ6：音楽を閲覧して再生する

1. 接続すると、デバイスが**接続済みデバイス**リストに表示されます。

![接続済みデバイス](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. **ミュージック**フォルダに移動し、任意のオーディオファイルをタップして再生を開始します。

![音楽を再生](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## ステップ7：接続済みクラウドフォルダを音楽ライブラリに追加する

1. アプリの**音楽ライブラリ**セクションを開きます。
2. **音楽を追加**を選択し、**接続**を選択します。
3. 接続済みのNASサーバーを選択し、**ミュージック**フォルダを選択します。**完了**をタップします。
4. アプリが音楽フォルダをスキャンし、サポートされているオーディオファイルを音楽ライブラリに追加します。メタデータが読み込まれ、トラックがアルバム、アーティスト、ジャンルごとにグループ化されます。

## まとめ

これらのステップに従うことで、Synology NASに簡単に接続を設定し、EvermusicまたはFlacboxを使用してiPhoneやMacに音楽ライブラリ全体をストリーミングできます。自宅でも外出先でも、QuickConnectを使用してどこからでもお気に入りの曲にシームレスで高品質なアクセスを楽しめます。これらのアプリが提供する柔軟性と利便性を活用して、すべてのデバイスで音楽コレクションを簡単に管理し始めましょう。

QuickConnectによる安全なリモートアクセスと幅広いオーディオフォーマットのサポートにより、音楽から離れることはありません。NASに保存されたファイルは、今やタップ一つで手の届くところにあります！

## よくある質問

{{% details title="手動接続とQuickConnectの違いは何ですか？" closed="true" %}}
手動接続はNASのIPアドレスとポートを使用し、ローカルネットワークで動作します。QuickConnectはSynologyのリレーサービスを使用して、ポート転送なしにインターネット経由でどこからでも接続を確立します。
{{% /details %}}

{{% details title="ホームネットワーク外からSynology NASの音楽をストリーミングできますか？" closed="true" %}}
はい。Synology NASでQuickConnectを有効にし、EvermusicまたはFlacboxでQuickConnect IDを使用して、インターネット接続のある場所からどこでも音楽をストリーミングできます。
{{% /details %}}

{{% details title="Synology NASからストリーミングする際にサポートされるオーディオフォーマットは？" closed="true" %}}
EvermusicとFlacboxはFLAC、MP3、AAC、WAV、ALAC、OGG、WMA、DSD、その他多くのフォーマットをサポートしています。すべてのサポートされたフォーマットはSynology NASからのストリーミング時に動作します。
{{% /details %}}

{{% details title="接続に二要素認証は必要ですか？" closed="true" %}}
いいえ、二要素認証はオプションです。ただし、Synology DSMで2段階認証を有効にしている場合、アプリはログイン時にワンタイムパスワードを要求します。セッションが期限切れになった場合は再認証が必要です。
{{% /details %}}

{{% details title="SynologyネイティブAPI、WebDAV、SMBのどれを使って接続すべきですか？" closed="true" %}}
QuickConnectを使用したSynologyネイティブAPIは、リモートアクセスに最適な選択肢です。ローカルネットワーク使用には、SMBが通常最も高速なオプションです。WebDAVはローカルとリモートの両方のアクセスに適しています。EvermusicとFlacboxは3つのプロトコルすべてをサポートしています。
{{% /details %}}
