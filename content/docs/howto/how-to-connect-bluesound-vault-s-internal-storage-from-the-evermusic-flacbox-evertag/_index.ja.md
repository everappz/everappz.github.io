---
title: "Evermusic、Flacbox、EvertagからBluesound VAULTの内部ストレージに接続する方法"
date: 2022-03-10
description: "SMBプロトコルを使用して、Evermusic、Flacbox、EvertagからBluesound VAULTの内蔵ハードドライブにアクセスし、オーディオファイルの管理、編集、再生を行う方法を学びましょう。"
keywords: ["bluesound vault", "smbストレージ接続", "evermusic smb", "flacbox vault", "evertag smb", "nasストレージ音楽", "vault内蔵ドライブ"]
tags: ["evermusic", "接続", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**概要：** Evermusic、Flacbox、またはEvertagを使用して、SMB経由でBluesound VAULTの内部ストレージに接続します。BluOSアプリでVAULTのIPアドレスを確認し、ゲストアクセスでSMB接続として入力し、音楽ファイルの再生や管理を開始しましょう。

Bluesound VAULTには内蔵ハードドライブがあり、ネットワーク接続ストレージ（NAS）として機能します。VAULTの内蔵ハードドライブにアクセスすることで、Evermusic、Flacbox、Evertagからファイルの追加/削除やメタデータタグの編集が可能になります。

**VAULTの内蔵ハードドライブにアクセスする手順は以下の通りです：**

1. BluOSアプリで、**ヘルプ > 診断**を選択します。

2. **診断**ページからVAULTの**IPアドレス**を取得します。この**IPアドレス**は次の手順で使用します。

3. Evermusic、Flacbox、またはEvertagを開きます。

   ![Everappzアプリケーション](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. 「接続」画面を開き、「クラウドサービスに接続」メニュー項目を選択します。

   ![Evermusic 接続画面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. 「SMB」クラウドサービスを選択します。

   ![Evermusic クラウドサービスに接続画面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. 「SMB設定画面」で以下の形式でURLを入力します：

   ```
   SMB://<<VAULT-IP>>
   ```

   `<<VAULT-IP>>`を手順2で取得した**IPアドレス**に置き換えます。

   **注意：** VAULTストレージはゲスト（GUEST）モードをサポートしているため、ログインとパスワードのフィールドは空白のままにしてください。

   ![Evermusic SMB接続画面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. 「サインイン」ボタンをタップして設定を保存します。

8. 接続されたクラウドストレージを開き、オーディオファイルが入っているフォルダに移動して、任意のファイルをタップしてオーディオプレーヤーを起動します。

   ![Evermusic 開いたSMBサーバー画面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. 内蔵のファイルマネージャーを使用してファイルを編集することもできます。

   ![Evermusic ファイルマネージャー画面](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

これらの簡単な手順で、Bluesound VAULTの内蔵ハードドライブに簡単にアクセスし、Evermusic、Flacbox、またはEvertagを使用して音楽ライブラリを管理できます。

## よくある質問

{{% details title="Bluesound VAULTに接続するためにユーザー名とパスワードが必要ですか？" closed="true" %}}
いいえ。Bluesound VAULTはSMB経由でゲスト（匿名）アクセスをサポートしています。接続の設定時にログインとパスワードのフィールドは空白のままにしてください。
{{% /details %}}

{{% details title="Bluesound VAULTで音楽タグを編集できますか？" closed="true" %}}
はい。Evertagを使用して、VAULTの内蔵ハードドライブに直接保存されているオーディオファイルのメタデータタグ（タイトル、アーティスト、アルバムなど）を編集できます。
{{% /details %}}

{{% details title="Bluesound VAULTはどのプロトコルをサポートしていますか？" closed="true" %}}
Bluesound VAULTはSMB（Server Message Block）を介して内部ストレージを公開しています。Evermusic、Flacbox、EvertagはすべてSMB接続をサポートしており、簡単に接続できます。
{{% /details %}}

{{% details title="iPhoneにファイルをコピーせずにVAULTから音楽をストリーミングできますか？" closed="true" %}}
はい。SMB経由で接続すると、VAULTの内蔵ドライブからデバイスにコピーすることなく、直接オーディオファイルをストリーミングできます。
{{% /details %}}
