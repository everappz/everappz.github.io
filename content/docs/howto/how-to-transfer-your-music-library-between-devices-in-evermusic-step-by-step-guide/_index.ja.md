---
title: "Evermusicでデバイス間の音楽ライブラリを転送する方法：ステップバイステップガイド"
description: "Wi-Fi Driveとバックアップツールを使用して、Evermusicの音楽ライブラリ、プレイリスト、アルバムアートワーク、設定をiPhone、iPad、またはMac間で簡単に転送できます。"
date: 2024-12-29
tags: ["音楽ライブラリ", "転送", "WiFi", "バックアップ", "webdav", "復元"]
keywords: ["Evermusic音楽ライブラリ転送", "Evermusicプレイリストバックアップと復元", "Evermusic WiFi Drive", "デバイス間Evermusic同期", "Evermusicデータベース移動", "Evermusicファイル転送", "オーディオプレーヤー設定復元", "WebDAV音楽転送iOS"]
readingTime: 3
---

{{< author-byline >}}


**概要：** Evermusicライブラリを新しいデバイスに転送するには、ソースデバイスでバックアップを作成し、Wi-Fi Driveを起動し、同じネットワーク上で2台目のデバイスを接続し、バックアップと音楽ファイルをダウンロードしてから、バックアップから復元します。プロセス全体はライブラリのサイズに応じて約10分かかります。

このガイドでは、データベース、アルバムカバー、設定を含む音楽ライブラリ全体を1つのデバイス（iPhoneまたはMac）から別のデバイスに転送する方法を説明します。音楽ライブラリとプレイリストの自動同期は将来予定されている機能ですが、現在このプロセスは手動で行う必要があります。

## ステップ1：最初のデバイスでバックアップを作成する

1. **最初のデバイスでアプリを開きます**（音楽ライブラリ、プレイリスト、接続されたクラウドサービスがあるデバイス）。
2. **設定に移動**し、**バックアップと復元**オプションを選択します。

![バックアップと復元](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. **バックアップと復元**画面で、バックアップファイルに含める項目を選択します：
   - **データベース**（音楽ライブラリとプレイリストを含む）
   - **アルバムカバー**
   - **設定**

これらのオプションはデフォルトで有効になっています。

![バックアップオプション](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. **アプリケーションデータのバックアップ**をタップしてプロセスを開始します。

![アプリケーションデータのバックアップ](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. バックアップが完了すると、情報アラートが表示されます。

![バックアップ完了](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

**ファイルを表示**をタップして、**ドキュメント**ディレクトリ内のバックアップファイルを表示します。バックアップファイルは通常、**Backup**フォルダに保存されます。

![バックアップファイルを表示](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## ステップ2：Wi-Fi Driveサーバーを起動する

1. アプリの**接続**セクションに移動します。
2. **Wi-Fiで接続**まで下にスクロールしてタップします。

![Wi-Fiで接続](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. 次の画面で、**Wi-Fi Driveを開始**をタップします。

- オプションで、セキュリティのためにログインとパスワードを設定できますが、ホームネットワークでは不要です。

4. 起動すると、利用可能なサーバーアドレスが表示されます。これはデスクトップブラウザやWebDAVアプリで使用できますが、このガイドでは直接次のステップに進みます。

![Wi-Fi Drive起動済み](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## ステップ3：2台目のデバイスを1台目に接続する

1. 2台目のデバイスでアプリを開きます（ライブラリを転送したいデバイス）。
2. 両方のデバイスが同じWi-Fiネットワークに接続されていることを確認します。
3. 2台目のデバイスで**接続**タブを開き、**利用可能なデバイス**を選択します。

![利用可能なデバイス](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. **Evermusic**という名前のWebDAV接続が表示されるはずです（1台目のデバイスで起動したサーバー）。タップして接続します。

5. 接続すると、1台目のデバイスのすべてのフォルダが表示されます。

![1台目のデバイスに接続](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## ステップ4：ファイル転送の準備

1. 2台目のデバイスで、**設定 > ファイルマネージャー**に移動し、**ダウンロードしたファイルの保存先 - 毎回確認**を有効にします。

- これにより、各ダウンロードの保存先フォルダを選択できます。

2. **接続**タブに戻り、接続されたWebDAVサーバーに移動します。

![ファイル転送の準備](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## ステップ5：バックアップと音楽ファイルを転送する

1. 接続されたWebDAVサーバーの**Backup**フォルダを開きます。

![バックアップフォルダ](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. バックアップファイルの横にある**その他のアクション**ボタン（3つの点）をタップし、**ダウンロード**を選択します。

3. ダウンロードしたファイルを保存するために、2台目のデバイスに**Backup**フォルダを作成します。**完了**をタップして選択を確認します。

![バックアップをダウンロード](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. 追加の音楽ファイルを転送します：
   - WebDAVサーバーの**ダウンロード**フォルダまたはその他の関連フォルダを確認します。

![音楽ファイルを転送](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- **選択する**オプションを使用してファイルを選び、**その他のアクション > ダウンロード**をタップします。同じディレクトリ構造を維持するために、2台目のデバイスの対応するフォルダに保存します。

目標は、フォルダ構造が同一のまま、1台目のデバイスから現在のデバイスにすべてのファイルを転送することです。こうすることで、音楽ライブラリとプレイリストのリンクが維持されます。1台目のデバイスのアプリのドキュメントディレクトリ外に保存されたローカルファイルは、別途転送する必要があります。アプリはWi-Fi Driveモードではこれらのファイルにアクセスできないため、システムのファイルアプリを使用して転送する必要があります。

![転送完了](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## ステップ6：転送の進行状況を監視する

1. 2台目のデバイスで、**ローカルファイル**セクション（またはiPad/Macの**ダウンロード**タブ）に移動します。

2. 左上隅の**転送アクティビティ**ボタンをタップして、転送キューを監視します。

![転送を監視](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## ステップ7：バックアップからデータを復元する

1. バックアップファイルと必要なすべてのオーディオファイルが2台目のデバイスにダウンロードされたら、**Backup**フォルダを開きます。

2. バックアップファイルをタップすると、確認メッセージが表示されます。

![バックアップを復元](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **注意：** 復元すると、現在のすべての音楽ライブラリデータ、プレイリスト、設定、アルバムアートワークがバックアップデータに置き換えられます。

3. **復元**をタップしてプロセスを開始します。

![復元プロセス](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. 復元が完了すると、アラートが成功を確認します。

![復元完了](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

**プレイリスト**または**音楽ライブラリ**セクションを確認して復元を検証します。

![復元を検証](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## ステップ8：音楽ライブラリを再インデックスする

1. 最良の結果を得るために、ライブラリを再インデックスしてすべてのファイルが正常に検出されたことを確認します。

2. **設定 > 音楽ライブラリ > オフライン音楽同期**に移動し、**ローカルフォルダスキャンを開始**を選択します。

これらのステップに従うことで、音楽ライブラリ、プレイリスト、設定を別のデバイスに正常に転送できます。問題が発生した場合は、遠慮なくサポートにお問い合わせください。

## よくある質問

{{% details title="Wi-Fiなしでevermusicライブラリを転送できますか？" closed="true" %}}
Wi-Fi Driveは、両方のデバイスが同じWi-Fiネットワーク上にある必要があります。現在、BluetoothまたはセルラーTransferオプションはありません。代わりに、AirDropまたはファイルアプリを使用して、バックアップファイルと音楽フォルダをデバイス間で手動で移動できます。
{{% /details %}}

{{% details title="クラウドサービスの接続はバックアップと一緒に転送されますか？" closed="true" %}}
バックアップには、データベース、プレイリスト、アルバムカバー、設定が含まれます。セキュリティ上の理由から、クラウドサービスのログイン資格情報は含まれていません。復元後、新しいデバイスでクラウドアカウントを再接続する必要があります。
{{% /details %}}

{{% details title="2台目のデバイスの既存のライブラリはどうなりますか？" closed="true" %}}
バックアップの復元により、2台目のデバイスの既存の音楽ライブラリデータ、プレイリスト、設定、アルバムアートワークがすべて置き換えられます。データを保持したい場合は、最初に2台目のデバイスの個別のバックアップを作成してください。
{{% /details %}}

{{% details title="このプロセスはiPhoneとMac間で機能しますか？" closed="true" %}}
はい。Evermusicは、iPhone、iPad、Macの任意の組み合わせ間のWi-Fi Drive転送をサポートしています。両方のデバイスが同じWi-Fiネットワーク上にあるだけで大丈夫です。
{{% /details %}}

{{% details title="転送にはどのくらい時間がかかりますか？" closed="true" %}}
転送時間は、音楽ライブラリのサイズとWi-Fi速度によって異なります。数ギガバイトの一般的なライブラリは、標準的なホームネットワークで5〜15分で転送されます。
{{% /details %}}
