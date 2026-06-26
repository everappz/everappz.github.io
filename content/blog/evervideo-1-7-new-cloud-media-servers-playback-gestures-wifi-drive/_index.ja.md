---
title: "Evervideo 1.7: 新しいPlex、Jellyfin、クラウドストリーミング、再生ジェスチャ"
date: 2026-05-18
description: "Evervideo 1.7は10以上の新しい接続(Plex、Jellyfin、Emby、Subsonic、Navidrome、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、FTP、SFTP、NFS)を追加し、新しい再生ジェスチャ(ダブルタップでシーク、長押しで2倍速)、バッチアップロード対応の刷新されたWi-Fi Drive、iPhone/iPad/Mac向けのLiquid Glass UIアップデートを備えます。"
keywords: ["Evervideo 1.7", "Evervideoアップデート", "HD動画プレイヤー iPhone", "Plex 動画プレイヤー iOS", "Jellyfin iPhone 動画", "Emby 動画プレイヤー iOS", "Subsonic 動画 iOS", "Navidrome 動画 iOS", "Internxt 動画ストリーミング", "Proton Drive 動画プレイヤー", "QNAP 動画プレイヤー iPhone", "Nextcloud 動画プレイヤー iOS", "Amazon S3 動画ストリーミング", "SFTP 動画プレイヤー iPhone", "FTP 動画プレイヤー iOS", "NFS 動画ストリーミング iPhone", "NASからiPhoneに動画ストリーミング", "MKVプレイヤー iPhone", "動画プレイヤー ジェスチャ iOS", "ダブルタップで動画シーク", "Wi-Fi Drive 動画転送 iPhone", "Liquid Glass デザイン", "クラウド動画プレイヤー iOS 2026", "クラウドからiPhoneへ映画ストリーミング"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "再生ジェスチャ", "Liquid Glass", "新機能"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**要点:** [Evervideo 1.7](/products/evervideo) はiPhone、iPad、Mac向けHD動画プレイヤーの大型アップデートです。本リリースでは10件以上の新しいクラウド/NAS/メディアサーバー接続(**Internxt**、**Proton Drive**、**QNAP**、**Nextcloud**、**Amazon S3**)に加え、最も人気のあるメディアサーバー(**Plex**、**Subsonic**、**Navidrome**、**Jellyfin**、**Emby**)、3つのネットワークプロトコル(**FTP**、**SFTP**、**NFS**)を追加しました。新しい**再生ジェスチャ**では、ダブルタップで前後にジャンプ、長押しで2倍速再生、シングルタップでコントロールの表示/非表示を切り替えられます — すべてフルスクリーンを抜けずに行えます。Wi-Fi Driveは複数選択モードとよりスマートなアップロードキューを備えたUIに刷新されました。アプリ全体はAppleの新しい**Liquid Glass**デザインに合わせて調整されています。

---

## 皆さん、こんにちは!

Evervideoの大型アップデートが届きました。これは私たちがリリースした中でも特に大きなアップデートのひとつです:**10件以上の新しいクラウド/サーバー/ネットワーク接続**、フルスクリーンでのより素早い操作を実現する全く新しい**再生ジェスチャ**、刷新された**Wi-Fi Drive**体験、そしてiPhone/iPad/Macに渡って**Liquid Glass**に合わせて調整されたUIです。

[App StoreからEvervideo 1.7をダウンロード](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336)するか、既存のバージョンからアップデートしてください。Macユーザーは[デスクトップ版をこちら](https://apps.apple.com/app/evervideo/id6743504109)から入手できます。

## 10以上の新しいクラウド/NAS/メディアサーバー接続

Evervideo 1.7は「動画ライブラリ」として扱える範囲を拡大します。映画、ドラマ、録画が信頼するクラウド、自宅のNAS、セルフホスト型のメディアサーバーにあれば、Evervideoはダウンロード、変換、再エンコードなしで直接ストリーミングできます。

### プライバシー重視のクラウドストレージ:InternxtとProton Drive

エンドツーエンド暗号化とゼロ知識ストレージにこだわるなら、最も評価の高いプライバシーファーストのクラウド2つがEvervideoにネイティブで利用できるようになりました:

- **Internxt** — オープンソース、ポスト量子暗号、GDPR準拠のスペイン製クラウド。無料プランあり。
- **Proton Drive** — Proton MailおよびProton VPNの開発元によるエンドツーエンド暗号化ストレージ。スイス拠点。無料プランあり、大容量ライブラリには有料プランも用意。

一度接続すれば動画は暗号化トンネル経由でストリーミングされ、Evervideoがあなたのデータを平文で見ることはなく、プロバイダのサーバーも同様です。

### セルフホスト型ストレージ:QNAP、Nextcloud、Amazon S3

独自インフラを運用するユーザー向けに:

- **QNAP** — QNAP NASデバイスへのネイティブAPI接続で、ローカルWi-Fiまたはリモートアクセスでの高速かつ信頼性の高い動画再生に対応。4K MKVファイルを再エンコードなしで直接ストリーミング。
- **Nextcloud** — セルフホストまたは管理されたNextcloudインスタンスのいずれにも接続可能。プライバシーの理由でGoogle DriveやDropboxから移行済みなら最適です。
- **Amazon S3** — EvervideoをS3バケット(またはBackblaze B2、Wasabi、MinIO、Cloudflare R2などS3互換ストレージ)に向けて、コレクションを直接ストリーミング。

### <a id="media-servers"></a>メディアサーバー:Plex、Subsonic、Navidrome、Jellyfin、Emby

セルフホスト動画ファンにとっての大きな目玉です。Evervideo 1.7は、iPhone、iPad、Macを最も人気のあるオープンソース/フリーミアム型メディアサーバー向けの第一級クライアントに変えます:

- **Plex** — Plex Media Serverは**無料**でダウンロード/実行可能。モバイル同期、ハードウェアトランスコード、ライブTVなどのために**Plex Pass**(有料)を任意で追加できます。Evervideoは無料ライブラリ/Plex Passライブラリの双方で動作 — 映画/TVコレクション全体をストリーミングできます。
- **Subsonic** — セルフホスト型ストリーミングサーバーの元祖。公式Subsonicサーバーは**有料**(30日トライアル後、月額1ドル)で、EvervideoはSubsonic API互換の動画サーバーとも通信できます。
- **Navidrome** — モダンで軽量、**完全に無料でオープンソース**のサーバー。Subsonic APIを実装。Raspberry Pi、NAS、任意のLinuxマシンで動作します。
- **Jellyfin** — **完全に無料でオープンソース**のメディアサーバー(Embyのコミュニティフォーク)。映画、TV、音楽、書籍、ホームビデオを扱います。アカウント不要、テレメトリなし、サブスクリプションなし。商業的なしがらみなしでセルフホスト・ストリーミングをしたいユーザーの定番です。
- **Emby** — **フリーミアム**型メディアサーバー。コアサーバーは無料、**Emby Premiere**は買い切りまたは年額の購入でモバイルアプリ、オフライン同期、Cinema Modeなどがアンロックされます。Evervideoは無料/Premiereの双方のライブラリに接続できます。

どのサーバーを動かしていても、Evervideoは動画イコライザ、360°対応、ピクチャ・イン・ピクチャ、AirPlay、Chromecastとともに、映画/ドラマ/ホームビデオ/埋め込み字幕トラックを含むライブラリ全体をストリーミングします。

### 新しいネットワークプロトコル:FTP、SFTP、NFS

洗練されたモバイルアプリを提供しないカスタムサーバー、ホームラボ、または汎用NASを使うユーザー向けに、Evervideo 1.7は3つの定番プロトコルを追加します:

- **SFTP (SSH File Transfer Protocol)** — **自分のサーバーからの安全なリモート動画ストリーミング**に最適な答え。SFTPはSSH上で動作するため、転送全体(認証と動画データ)が暗号化されます。SSHアクセス可能なVPS、専用サーバー、自宅のLinuxマシンがあれば、動画フォルダを置いて他のものを公開することなくパブリック・インターネット経由でストリーミング可能です。パスワード認証および鍵認証に対応。
- **FTP** — 長年使われてきたファイル転送の標準。**自宅のNAS**(旧式のSynology、ASUS、D-Link、TerraMaster、汎用機器)がFTPサーバーを公開しているがネイティブAPI統合がない場合に便利。ローカルネットワーク内での使用が最適です。
- **NFS (Network File System)** — Linuxやほとんどのネットワーク機器における事実上の標準共有プロトコル。ホームラボや小規模ビジネスネットワークでNFS共有が一般的で、Evervideoはマウントして低オーバーヘッドで4K/HD動画をストリーミングします。

> **ヒント:** SFTPはオープン・インターネット越しのストリーミングに使うべきプロトコルです。FTPとNFSはローカルネットワーク内で使うのが最善 — VPNで包まない限り、パブリック・インターネットには公開しないでください。

## 新しい再生ジェスチャ

フルスクリーンでの動画視聴は手間がかからない感覚であるべきです。Evervideo 1.7は、画面上のコントロールを表示せずに再生を制御できる洗練されたタップジェスチャを導入します — 映画、講義、または中断なく視聴したい何にでも最適です。

### ダブルタップ — 前後にジャンプ

画面の**右側**をダブルタップすると、設定可能な秒数だけ**早送り**します。**左側**をダブルタップすると**巻き戻し**ます。インターバル(デフォルト:10秒)は**設定 → 再生 → ジェスチャ・スキップ間隔**で変更でき、5秒(細かなシーク用)から60秒(イントロのスキップ用)まで任意の値を選べます。

これはYouTubeやNetflixのユーザーがすぐに認識できるジェスチャで、今ではあらゆるソースのあらゆる動画でEvervideoにネイティブで搭載されました。

### 長押し — 一時的に2倍速

画面のどこでも長押しすると**一時的に再生速度が2倍**になります。指を離すと通常速度に戻ります。次のような用途に最適:

- 永続的な速度変更を伴わずに、スローなシーンを飛ばす。
- 講義、チュートリアル、ポッドキャストを素早くスキャンして該当箇所を探す。
- 本編視聴に踏み切る前に、映画をサンプリングしてみる。

長押しジェスチャは保存された再生速度を変更しません — 離せば元のところに戻ります。

### シングルタップ — コントロールの表示 / 非表示

画面上のシングルタップで、再生コントロール(再生/一時停止、シークバー、字幕、イコライザ)の表示/非表示を切り替えます。一度タップして呼び出し、もう一度タップして非表示にします。ダブルタップや長押しと組み合わせれば、映画のほとんどをすっきりしたフルスクリーンモードで過ごしつつ、必要に応じてシーク/一時停止/速度スキャンが行えます。

## Wi-Fi Drive:新しいUIとより速いアップロード

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) はEvervideoの内蔵機能で、**iTunes、ケーブル、クラウドアカウントなしで、コンピューターからiPhoneやiPadへ動画をワイヤレス転送**できます。両方のデバイスは同じWi-Fiネットワーク上にある必要があります。iOSアプリでサーバーを起動して、次のいずれかの方法を取ります:

- 任意のデスクトップブラウザ(Safari、Chrome、Firefox、Edge)でURLを開き、動画ファイルをページにドラッグすると、デバイスに直接アップロードされます。または
- **Mac Finder**(「サーバへ接続...」)や**Windowsエクスプローラー**(ネットワークドライブの割り当て)を使い、WebDAV経由でデバイスをネットワーク共有としてマウントします。

サードパーティ・サービスなしで、大きなローカル動画コレクションをスマホやタブレットへ移動する最速の方法です。[ステップバイステップガイドはこちら](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/)をご覧ください。

Evervideo 1.7では、Wi-Fi Driveに次の改良が加わります:

- **再設計されたユーザーインターフェース** — よりクリーンで一目で読みやすく、Liquid Glassに合わせて更新。
- **バッチ操作のための新しい選択モード** — 複数のファイル/フォルダを選んでまとめて操作(削除、移動、コピー)できます。
- **改良されたファイルアップロードキュー** — より良い進捗フィードバックとネットワーク不調への耐性により、不安定なWi-Fi接続でも30GBの転送が台無しになることがありません。
- **全体的な転送パフォーマンスの向上** — 大規模ライブラリ、特に4K MKVファイルや映画コレクションで体感的に高速なアップロード。

## その他の改善

### Liquid Glass デザインのアップデート

Evervideo 1.7のインターフェースは、アプリ全体でAppleの新しい**Liquid Glass**マテリアルに更新されました — 半透明のサーフェス、なめらかなアニメーション、洗練されたコントロールで、iOS 26、iPadOS 26、macOS 26に自然になじみます。Now Playing、ファイルブラウザ、設定画面のいずれも新システムの美学に合うよう再調整されました。

### 更新された接続ライブラリ

Evervideoが**WebDAV**、**SMB**、**DLNA**、**Dropbox**、**Google Drive**、**OneDrive**、**iCloud Drive**、**MEGA**などのサービスと通信するために使う基盤ライブラリを刷新しました。その結果、稀な接続失敗の減少、新しいサーバーバージョンへの対応強化、低速または地理的に離れた接続での動画ストリーミングの信頼性向上を実現しました。

### 再生バグの修正

- 大きなMKVファイルでシーク後にストリームが停止する一部のセルフホスト・サーバーでの再生問題を修正。
- 再生中にネットワークが一時的に切断された場合の再開挙動を改善。
- 長尺コンテンツでの字幕同期をよりスムーズに。

### ローカライズの修正

ユーザーからの直接の声に基づき、複数言語の翻訳を修正。小さなボタンや長めの欧州言語(ドイツ語、オランダ語、フランス語)でのテキスト収まりを改善。

### あなたのフィードバックから着想を得た細かな改良

App Storeレビューやsupport@everappz.com宛のメールから得た細かな改善を多数反映。すべてのメッセージを読んでいます。

## このアップデートが重要な理由

Evervideo 1.7は3つのアイデアを軸にしています:

1. **あなたの動画を、どこに保存していても。** ライブラリがiCloud Driveにあっても、Proton DriveやInternxtのようなプライバシー重視のクラウド、PlexやJellyfinのようなメディアサーバー、自宅のNAS、Navidromeを動かすRaspberry Piにあっても — Evervideoはどこでも同じ再生体験で、ネイティブに接続します。
2. **手間のかからないフルスクリーン動画。** 新しいタップジェスチャ(ダブルタップ、長押し、シングルタップ)は、YouTubeやNetflixなどのストリーミングアプリがユーザーに学習させた流れるような操作感を、*あなた*の動画コレクションに適用します。
3. **コンピューターからのより速い転送。** バッチ選択とよりスマートなアップロードキューを備えた刷新されたWi-Fi Driveにより、大規模な4K映画コレクションのiPhone/iPadへの移動が、ケーブル/iTunes/圧縮なしで本当に高速に行えます。

## Evervideo 1.7 を入手

[**App StoreからEvervideoをダウンロード**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336)するか、App Store内でアップデートしてください。[Mac版](https://apps.apple.com/app/evervideo/id6743504109)はユニバーサルMacアプリとして別途利用可能です。Evervideoは無料でダウンロードでき、高度な機能向けのオプションのアプリ内アップグレードがあります。新しいクラウド接続、メディアサーバー対応、再生ジェスチャ、Wi-Fi Driveの改善、Liquid Glass UIは、ベースのアップデートの一部です。

アプリが気に入ったら、App Storeにレビューを残してください — 本当に助かります。フィードバックや問題がありますか?**support@everappz.com**までメールしてください。すべてのメッセージを読んでいます。

## よくある質問

{{% details title="Evervideo 1.7の新機能は?" closed="true" %}}
Evervideo 1.7は10件以上の新しい接続(Plex、Jellyfin、Emby、Subsonic、Navidrome、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、FTP、SFTP、NFS)、新しい再生ジェスチャ(ダブルタップでシーク、長押しで2倍速、シングルタップでコントロール表示の切り替え)、選択モードとよりスマートなアップロードキューを備えた再設計されたWi-Fi Drive、Liquid Glassデザインの更新、接続ライブラリの更新、多くのバグ修正を導入します。
{{% /details %}}

{{% details title="EvervideoはPlexで動作しますか?" closed="true" %}}
はい。Evervideo 1.7からPlex Media Serverに接続して、映画、TV番組、ホームビデオを含む動画ライブラリ全体をストリーミングできます。Plex Media Serverは無料で動作し、Plex Passは任意です。EvervideoはFree版とPlex Passの双方の構成をサポートし、再エンコードなしでのMKV、MP4、AVI、MOVなどの直接再生も可能です。
{{% /details %}}

{{% details title="EvervideoはJellyfinやNavidromeをサポートしていますか?" closed="true" %}}
はい。JellyfinもNavidromeもEvervideo 1.7で完全にサポートされています。Jellyfinは動画と音声を扱う無料のオープンソース・メディアサーバーです。NavidromeはSubsonic APIを実装した無料のオープンソース・サーバーです。Evervideoはどちらにもネイティブに接続します。
{{% /details %}}

{{% details title="Plex、Jellyfin、Emby、Navidrome、Subsonicは無料ですか?" closed="true" %}}
- **Plex** — サーバーは無料、Plex Passは任意の有料アップグレード。
- **Jellyfin** — 完全に無料でオープンソース。
- **Emby** — サーバーは無料、Emby Premiereは有料でモバイル同期とオフラインをアンロック。
- **Navidrome** — 完全に無料でオープンソース。
- **Subsonic** — 公式サーバーは30日トライアル後、月額1ドル。ただしAPIはオープンで、多くの無料サーバー(Navidromeを含む)が実装。
{{% /details %}}

{{% details title="自宅のNASからSFTP、FTP、NFSでストリーミングできますか?" closed="true" %}}
はい。Evervideo 1.7はSFTP、FTP、NFSをネイティブの接続タイプとして追加します。SFTPはトラフィック全体がSSH経由で暗号化されるため、パブリック・インターネット越しに自分のサーバーからストリーミングする場合の推奨選択肢です。FTPとNFSはローカルネットワーク内、またはVPNの背後で使用するのが最適です。
{{% /details %}}

{{% details title="EvervideoをSFTPでカスタムサーバーに接続するには?" closed="true" %}}
Evervideoを開き、接続タブへ行き、SFTPを選び、サーバーのホスト名またはIP、ポート(通常は22)、ユーザー名、パスワードまたはSSH秘密鍵を入力します。Evervideoはリモートフォルダを参照し、エンドツーエンド暗号化で動画ファイルを直接ストリーミングします。
{{% /details %}}

{{% details title="EvervideoはInternxtとProton Driveをサポートしていますか?" closed="true" %}}
はい。両方のプライバシー重視クラウドはEvervideo 1.7時点でサポートされています。これらはアプリ内ですでに利用可能なMEGAなどのプライバシーファースト・サービスに加わります。
{{% /details %}}

{{% details title="新しい再生ジェスチャはどのように動作しますか?" closed="true" %}}
フルスクリーン動画再生中、**画面の右側をダブルタップ**すると早送り、**左側をダブルタップ**すると巻き戻し(設定可能な間隔、デフォルト10秒 — 設定で変更可能)になります。画面上のどこでも**長押し**すると一時的に2倍速になり、離すと通常速度に戻ります。どこでも**シングルタップ**すると再生コントロールの表示/非表示が切り替わります。
{{% /details %}}

{{% details title="ダブルタップのスキップ間隔は変更できますか?" closed="true" %}}
はい。**設定 → 再生 → ジェスチャ・スキップ間隔**で、5秒から60秒の間で値を選べます。多くのユーザーは10秒または15秒のままにしています。
{{% /details %}}

{{% details title="EvervideoのWi-Fi Driveとは何ですか?" closed="true" %}}
Wi-Fi DriveはEvervideoに内蔵されたワイヤレスファイル転送機能です。ローカルWi-Fiネットワーク経由で、iTunes、ケーブル、クラウドアカウントなしに、コンピューターからiPhoneやiPadへ動画をアップロードできます。任意のデスクトップブラウザや、Mac FinderまたはWindowsエクスプローラーのようなWebDAVクライアントを使用できます。[Wi-Fi Drive完全ガイドはこちら](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/)。
{{% /details %}}

{{% details title="EvervideoはPlexやJellyfinからMKV、AVIなどの形式を再生しますか?" closed="true" %}}
はい。Evervideoは事実上あらゆる動画形式(MKV、AVI、MP4、MOV、FLV、WMV、WEBM、M4V、TS、3GP)を再生し、ほとんどのコーデックでトランスコードを必要とせずにPlex、Jellyfin、Embyなどのメディアサーバーから直接ストリーミングします。これによりサーバー側のCPU負荷が下がり、起動時間も短縮されます。
{{% /details %}}

{{% details title="Evervideo 1.7のアップデートは無料ですか?" closed="true" %}}
はい。EvervideoはApp Storeから無料でダウンロードでき、1.7は既存ユーザー全員に対する無料アップデートです。新しいクラウド統合、メディアサーバー対応、再生ジェスチャ、Wi-Fi Driveの改善、Liquid Glass UIは、ベースのアップデートの一部です。
{{% /details %}}

{{% details title="Evervideo 1.7はどのデバイスで利用できますか?" closed="true" %}}
Evervideo 1.7はiPhone、iPad、Macで動作します。AirPlayとChromecastで大画面に再生をキャストできます。iCloud Drive同期により、デバイス間でライブラリと設定が一貫して保たれます。
{{% /details %}}
