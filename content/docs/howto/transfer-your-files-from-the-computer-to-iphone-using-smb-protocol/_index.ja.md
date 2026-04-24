---
title: "SMBプロトコルを使用してコンピュータからiPhoneにファイルを転送する"
description: "EvermusicとSMBプロトコルを使用して、MacまたはWindows PCからiPhoneまたはiPadに大容量ファイルを転送してアクセスする方法を学びましょう。シームレスなストリーミングとファイル管理のためのステップバイステップガイド。"
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["iPhoneにファイル転送 SMB", "PCの音楽をiPhoneでストリーミング", "MacをiPhoneに接続 SMB", "Evermusic SMB設定", "コンピュータのファイルにiPhoneからアクセス", "Windows音楽共有 iOS", "SMBファイル転送 Evermusic"]
---

{{< author-byline >}}


**要約:** iPhoneまたはiPadでEvermusicを使用して、SMB経由でローカルネットワーク上のMacまたはWindows PCに保存されたファイルにアクセスできます。ケーブル不要、iTunes不要、クラウドアップロード不要。コンピュータでファイル共有を有効にし、アプリで接続して、ワイヤレスでファイルを閲覧または再生できます。

MACやPCに大容量ファイルの膨大なコレクションがあり、iPhoneやiPadから簡単にアクセスしたいですか？当社のアプリがシンプルなソリューションを提供します。

SMBプロトコルを使用して、コンピュータとiOSデバイス間のシームレスなアクセスを有効にするために、以下の手順に従ってください：

## ステップ1：コンピュータでSMBプロトコルを有効にする

**MACの場合：**

1. MACで「システム環境設定」を開きます。
2. 「共有」をクリックします。
3. 「ファイル共有」サービスを有効にします。
4. 「共有フォルダ」セクションに音楽フォルダを追加します。ユーザーを追加し、アクセス権限レベル（読み書きまたは読み取りのみ）を選択します。追加した音楽フォルダに「全員：読み取りのみ」を選択できます。

   ![Mac設定画面](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. コンピュータのURL（smb://192.168.xx.xx）を覚えておいてください。次のステップで使用します。
6. 「オプション」をクリックし、「SMBを使用してファイルとフォルダを共有」を有効にします。

   ![Macファイル共有画面](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. 利用可能なアカウントの「Windowsファイル共有」を有効にします。

   ![Mac SMB共有画面](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Windows PCの場合：**

1. 音楽フォルダを右クリックします。
2. 「プロパティ」を選択します。
3. 「共有」タブに移動します。
4. 「共有...」をクリックします。
5. フォルダを共有する相手を選択し、アクセス権限レベルを指定します。選択した音楽フォルダに「全員：読み取り」を選択できます。

   ![Windows SMB共有画面](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. 「完了」をクリックします。
7. 「ファイル共有」ウィンドウで「完了」をクリックし、フォルダパスを覚えておきます。

   ![Windows SMB共有フォルダ](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## ステップ2：iOSデバイスを接続する

1. iPhoneまたはiPadでアプリを開きます。
2. 「接続」タブに移動します。

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Evermusic 接続画面"
  caption="Evermusic 接続画面"
  width="400"
>}}

*「利用可能なデバイス」セクションにコンピュータが表示される場合：*

コンピュータが「利用可能なデバイス」セクションに表示され、前のステップで「全員：読み取りのみ」を選択した場合は、コンピュータをタップするだけで自動的に接続されます。

*コンピュータが自動的に表示されない場合：*

1. 「クラウドサービスに接続」をタップします。
2. 「クラウドサービスに接続」画面で「SMB」を選択します。

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Evermusic クラウドサービスに接続画面"
  caption="Evermusic クラウドサービスに接続画面"
  width="400"
>}}

3. 「SMB接続」画面で、共有フォルダのパスを含むサーバーURLを入力します。サーバー名またはサーバーIPを使用できます：

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. ログインとパスワードを入力するか、前のステップで「全員：読み取りのみ」を選択した場合はこれらのフィールドを空白のままにします。
5. 「WORKGROUP」フィールドはオプションで、Active Directory Domainがある場合に使用します。

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Evermusic SMBコネクタ画面"
  caption="Evermusic SMBコネクタ画面"
  width="400"
>}}

6. SMBプロトコルを使用してコンピュータを接続すると、「接続」画面の「クラウドサービス」セクションに表示されます。
7. 接続されたサービスを開き、目的のフォルダに移動します。

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Evermusicで開いたSMBフォルダ"
  caption="Evermusicで開いたSMBフォルダ"
  width="400"
>}}

8. 内蔵のファイルマネージャーを使用して、必要に応じてファイルを編集できます。

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Evermusic ファイルマネージャー"
  caption="Evermusic ファイルマネージャー"
  width="400"
>}}

## ステップ3：特殊文字を含むSMB2フォルダの回避策

SMB2プロトコルを使用する際、特殊文字を含むフォルダで問題が発生することがあります。この問題を解決するためのいくつかの手順を以下に示します：

1. **SMB 1を有効にする：**  
   • 一時的な解決策として、サーバーとアプリの設定でSMB 1を有効にしてみてください。これにより、フォルダ名の特殊文字に関連する問題を回避できる場合があります。

2. **システムのファイルオープンメニューを使用する：**  
   • 「ローカルファイル」に移動します。  
   • 「このデバイスのファイル」セクションまで下にスクロールします。  
   • 「ファイルを開く...」または「フォルダを開く...」をタップします。  
   • サーバーを見つけて、必要なファイルまたはフォルダを選択します。  
   • 「開く」をタップして選択を確認します。

3. **代替プロトコル：**  
   • 問題が解決しない場合は、NASがこれらのオプションをサポートしている場合、WebDAVまたはDLNAプロトコルを使用してNASに接続することを検討してください。これらのプロトコルは特殊文字をより適切に処理できる場合があります。

これらの手順に従うことで、SMB2プロトコルを使用する際のフォルダ名の特殊文字に関する問題を軽減できます。

## まとめ

これらの手順により、当社のアプリを使用して、MACやPCからiPhoneやiPadで膨大なファイルコレクションに簡単にアクセスできます。

## よくある質問

{{% details title="iTunesなしでiPhoneからPCのファイルにアクセスできますか？" closed="true" %}}
はい。Evermusicはローカルの Wi-Fiネットワーク上でSMBを通じてコンピュータに接続します。iTunesやFinderの同期は不要です。PCでファイル共有を有効にし、アプリから直接接続してください。
{{% /details %}}

{{% details title="SMBファイルアクセスはインターネット経由で動作しますか？" closed="true" %}}
いいえ。SMBはローカルネットワークプロトコルです。iPhoneとコンピュータは同じWi-Fiネットワーク上にある必要があります。リモートアクセスの場合は、ファイルをGoogle DriveやDropboxなどのクラウドサービスにアップロードし、Evermusicで接続してください。
{{% /details %}}

{{% details title="SMBでどのようなファイルタイプにアクセスできますか？" closed="true" %}}
EvermusicはMP3、FLAC、AAC、WAV、AIFF、OGG、WMA、ALACおよびその他のオーディオ形式をサポートしています。内蔵のファイルマネージャーを使用して、非オーディオファイルも閲覧・管理できます。
{{% /details %}}

{{% details title="SMBを使用してNASからiPhoneにファイルを転送できますか？" closed="true" %}}
はい。ほとんどのNASデバイス（Synology、QNAP、WD My Cloudなど）はSMBをサポートしています。このガイドの同じ手順を使用してNASに接続してください。
{{% /details %}}

{{% details title="ファイルを再生するためにiPhoneにコピーする必要がありますか？" closed="true" %}}
いいえ。Evermusicはネットワーク経由でコンピュータやNASから直接ファイルをストリーミングします。オフライン再生のためにダウンロードすることを選択しない限り、ファイルはiPhoneにコピーされません。
{{% /details %}}

{{% details title="SMBファイル共有は安全ですか？" closed="true" %}}
SMBファイル共有はローカルネットワーク上でのみ動作します。異なるネットワーク上の他のデバイスは共有フォルダにアクセスできません。セキュリティを強化するには、匿名（全員）アクセスの代わりにログインとパスワードを使用してください。
{{% /details %}}
