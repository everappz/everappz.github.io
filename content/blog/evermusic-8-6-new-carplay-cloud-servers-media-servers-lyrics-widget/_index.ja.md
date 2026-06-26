---
title: "Evermusic 8.6: 新しいCarPlay、Plex、Jellyfin、SFTP、歌詞ウィジェット"
date: 2026-05-08
description: "Evermusic 8.6は、CarPlay体験を全面刷新し、Plex、Jellyfin、Emby、Subsonic、Navidrome、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、FTP、SFTP、NFSをサポート。ホーム画面に同期歌詞ウィジェット、Wi-Fi Drive改善、Liquid GlassデザインのUI更新を追加。"
keywords: ["Evermusic 8.6", "Evermusicアップデート", "CarPlay 音楽プレーヤー iPhone", "Plex プレーヤー iOS", "Jellyfin iPhone 音楽", "Emby プレーヤー iOS", "Subsonic iOS アプリ", "Navidrome iOS クライアント", "Internxt 音楽ストリーミング", "Proton Drive プレーヤー", "QNAP 音楽プレーヤー iPhone", "Nextcloud プレーヤー iOS", "Amazon S3 音楽ストリーミング", "SFTP プレーヤー iPhone", "FTP オーディオプレーヤー iOS", "NFS 音楽ストリーミング iPhone", "同期歌詞 ウィジェット iPhone", "ホーム画面 歌詞 ウィジェット iOS", "Wi-Fi Drive iPhone", "Baidu Netdisk プレーヤー", "Aliyun Drive プレーヤー", "Liquid Glass デザイン", "クラウド音楽プレーヤー iOS 2026"]
tags: ["Evermusic", "Evermusic 8.6", "CarPlay", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "歌詞ウィジェット", "ホーム画面ウィジェット", "Liquid Glass", "新機能"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**要点:** [Evermusic 8.6](/products/evermusic) はiPhone、iPad、Mac向けの大型アップデートです。CarPlayをゼロから作り直し、クイックソート、複数のカラースキーム、再設計された再生中画面、再生キューのフルビュー、頭文字インデックスでの高速スクロールを実装。**Plex**、**Jellyfin**、**Emby**、**Subsonic**、**Navidrome**、**Internxt**、**Proton Drive**、**QNAP**、**Nextcloud**、**Amazon S3** に加え、**FTP**、**SFTP**、**NFS** プロトコルなど10以上の新規接続を追加しました。新しい**同期歌詞ホーム画面ウィジェット**は、再生中の楽曲の歌詞をタイミングに合わせて表示します。Wi-Fi Driveは新UI、選択モード、より速いアップロードキューを搭載。アプリ全体が**Liquid Glass**デザインに対応し、**Baidu Netdisk(百度网盘)**や**Aliyun Drive(阿里云盘)**などの中国系サーバーからのストリーミングも安定しました。

---

## 皆さん、こんにちは!

Evermusic 8.6をダウンロードできるようになりました。私たちがリリースした中でも最大級のアップデートです。CarPlay体験の全面刷新、10件以上の新しいクラウド/サーバー連携、ホーム画面向けの新しい同期歌詞ウィジェット、そしてアプリ全体のLiquid Glassインターフェース刷新。

[App StoreからEvermusic 8.6をダウンロード](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) するか、現在のバージョンからアップデートしてください。

## 全く新しいCarPlay体験

**Apple CarPlay** 向けにEvermusicをゼロから作り直しました。より速く、よりスムーズで、ハンドルを握ったまま圧倒的に使いやすくなっています。

- **クイックソート** — アルバム、アーティスト、プレイリスト、フォルダにわたり、どんな曲も数秒で見つけられます。
- **複数のカラースキーム** — ダッシュボードや車内のイルミネーションに合うテーマを選べます。
- **再設計された再生中画面** — 大きなアートワーク、見やすいコントロール、ワンタップで使える新しい再生アクション。
- **再生キューがひと目で確認可能** — 現在の画面から離れずに次の曲を確認できます。
- **頭文字インデックスでの高速スクロール** — 1万曲以上の巨大なライブラリも、終わりのないスクロールなしで移動できます。
- **コンテンツ読み込みの高速化** — 大きなフォルダ、クラウドのディレクトリ、メディアサーバーのライブラリを開く際のフリーズはもうありません。

運転中にDropbox、Google Drive、OneDrive、iCloud Drive、[Plex](#media-servers)、[Jellyfin](#media-servers)などのクラウドから音楽をストリーミングしている方には、新しいCarPlay体験が車内に最初から組み込まれているかのように感じられるはずです。

## 10件以上の新しいクラウド/NAS/サーバー連携

Evermusic 8.6は「あなたのミュージックライブラリ」の定義を広げます。信頼できるクラウド、自宅のNAS、自前ホストのメディアサーバーのいずれであっても、Evermusicはそこから直接ストリーミングできます。同期もエクスポートも不要です。

### プライバシー重視のクラウド: InternxtとProton Drive

エンドツーエンド暗号化やゼロ知識ストレージを重視するなら、プライバシーファーストクラウドの中で最も評価されている2つのサービスがEvermusicでネイティブ対応しました。

- **Internxt** — オープンソース、ポスト量子暗号、GDPR準拠のスペイン発クラウド。無料プランあり。
- **Proton Drive** — Proton Mail / Proton VPNの開発元によるエンドツーエンド暗号化ストレージ。スイス拠点。無料枠と、より大きなライブラリ向けの有料プランがあります。

一度接続すれば、音楽は暗号化されたトンネルを通じてストリーミングされます。Evermusicがあなたのデータを平文で見ることはなく、プロバイダーのサーバーからも見えません。

### セルフホストストレージ: QNAP、Nextcloud、Amazon S3

自分でインフラを運用しているユーザー向け。

- **QNAP** — QNAP NASにネイティブAPI接続。ローカルWi-Fiやリモートで高速かつ安定した再生が可能です。
- **Nextcloud** — セルフホスト/マネージドを問わず、任意のNextcloudインスタンスに接続できます。プライバシー上の理由でGoogle DriveやDropboxから移行済みの方に最適。
- **Amazon S3** — 任意のS3バケット(Backblaze B2、Wasabi、MinIO、Cloudflare R2などのS3互換ストレージも可)をEvermusicに接続して、コレクションを直接ストリーミングできます。

### <a id="media-servers"></a>メディアサーバー: Plex、Subsonic、Navidrome、Jellyfin、Emby

セルフホスト派にとって最大の目玉です。Evermusic 8.6は、人気のオープンソースおよびフリーミアム系メディアサーバーの一級クライアントとして、iPhone、iPad、Macを生まれ変わらせます。

- **Plex** — Plex Media Serverのダウンロードと運用は **無料** です。**Plex Pass** はオプションの有料プランで、モバイル同期、ハードウェアトランスコード、ライブTVなどを解放します。Evermusicは無料ライブラリでもPlex Passライブラリでも動作します。
- **Subsonic** — セルフホスト型音楽ストリーミングサーバーの元祖。公式Subsonicサーバーは **有料** (30日間の試用後に月額1ドル)ですが、EvermusicはSubsonic APIに対応する数十のサーバーとも会話できます。
- **Navidrome** — モダンで軽量、**完全に無料かつオープンソース** な音楽サーバーで、Goで書かれています。Subsonic APIを実装。Raspberry Pi、NAS、任意のLinuxマシンで動作します。数十万曲規模までのライブラリに強くおすすめ。
- **Jellyfin** — **完全に無料かつオープンソース** のメディアサーバー(Embyのコミュニティフォーク)。音楽、映画、テレビ、書籍、オーディオブックを扱えます。アカウント不要、テレメトリーなし、サブスクなし。
- **Emby** — **フリーミアム** のメディアサーバー。コアサーバーは無料で、**Emby Premiere** は買い切りまたは年額の有料プランで、モバイルアプリ、オフライン同期、Cinemaモードなどを解放します。Evermusicは無料・Premiereの両方のライブラリに接続できます。

どのサーバーを使っていても、Evermusicはアルバム、アーティスト、プレイリスト、ジャンル、埋め込みアートワークを含むあなたのライブラリ全体をストリーミングします。オフラインキャッシュ、ギャップレス・クロスフェード再生、10バンドイコライザー、AirPlay、Chromecast、そして **CarPlay** に対応。サーバーが管理する再生履歴も尊重します。

### 新しいネットワークプロトコル: FTP、SFTP、NFS

カスタムサーバー、ホームラボ、洗練されたモバイルアプリのない汎用NASを使うユーザーのために、Evermusic 8.6は3つの定番プロトコルを追加しました。

- **SFTP (SSH File Transfer Protocol)** — **自分のサーバーから安全にリモートストリーミングする** のに最適な答え。SFTPはSSH上で動作するため、転送(認証もオーディオデータも)はすべて暗号化されます。SSHアクセスがあるVPS、専用サーバー、自宅のLinuxマシンがあれば、音楽フォルダを置いて他には何も公開せずに公衆インターネット越しにストリーミングできます。パスワード認証と鍵認証に対応。
- **FTP** — 長年使われてきたファイル転送の標準。**自宅のNAS** (古いSynology、ASUS、D-Link、TerraMaster、汎用ボックス)がFTPサーバーを公開していてネイティブAPI連携がない場合に有用。ローカルネットワーク内での利用が最適です。
- **NFS (Network File System)** — Linuxやほとんどのデバイスで事実上の共有プロトコル。NFS共有はホームラボや小規模オフィスのネットワークでよく使われており、Evermusicは現在マウントして直接ストリーミングできます。同等のハードウェア上でSMBよりオーバーヘッドが少なくなります。

> **ヒント:** 公衆インターネット越しのストリーミングにはSFTPがおすすめです。FTPとNFSはローカルネットワーク内での利用が最適。VPNでラップしない限り、これらをインターネットに直接公開しないでください。

## Wi-Fi Drive: 新UIと高速アップロード

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) は、**iTunesもケーブルもクラウドアカウントも不要で、コンピュータからiPhoneやiPadへ音楽をワイヤレス転送するEvermusic組み込み機能** です。両方のデバイスが同じWi-Fiネットワークに接続されている必要があります。iOSアプリでサーバーを起動したら、次のいずれかを行います。

- 任意のデスクトップブラウザ(Safari、Chrome、Firefox、Edge)でURLを開き、ページに音楽ファイルをドラッグするとデバイスへ直接アップロードされます。
- WebDAVを使って **Mac Finder**(「サーバへ接続…」)や **Windows File Explorer** (ネットワークドライブの割り当て)からデバイスをネットワーク共有としてマウントします。

サードパーティサービスを使わずに、大容量のローカル音楽ライブラリを電話に移す最速の方法です。[ステップバイステップガイドはこちら](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/)。

Evermusic 8.6のWi-Fi Driveでは、

- **新しいユーザーインターフェース** — すっきりして見やすくなりました。
- **選択モード** — 複数のファイルやフォルダを選んでまとめて操作できます。
- **アップロードキューの改善** — 進捗のフィードバックがより明確になり、ネットワーク不調にも強くなりました。
- **全体的なパフォーマンス向上** — 大きなライブラリの転送がより高速に。

## ホーム画面の新しい同期歌詞ウィジェット

最も多くリクエストされていた機能の一つがついに登場: **iPhone、iPad、Macのホーム画面に固定できる同期歌詞ウィジェット**。

時刻同期歌詞のある楽曲を再生すると、ウィジェットは曲の **現在の行** をリアルタイムで表示し、行は音楽に合わせて進みます。ウィジェットをタップすると、Evermusicがフル歌詞ビューで開きます。

主な機能:

- 再生中の楽曲の **同期されたタイムスタンプ付き歌詞** を表示。
- 曲の進行に合わせて自動更新 — 手動更新やスクロールは不要。
- 音声ファイルに埋め込まれたLRC形式の歌詞や、アプリ内で取得した歌詞に対応。
- **複数のウィジェットサイズ** に対応 — ホーム画面に表示する文字量を選べます。
- **iPhone**、**iPad**、**Mac** で動作(対応する場合は通知センターでも)。

長時間のリスニング中にデスクの上、スタンド、またはロック画面で電話を置いて歌詞を追いかけたい方に最適です。読みながら理解を深めたいオーディオブックやポッドキャスト系コンテンツとも特に相性が良いウィジェットです。

有効化するには、ホーム画面を長押しして **編集 > ウィジェットを追加** をタップし、**Evermusic** を検索して、お好みのサイズの **歌詞** ウィジェットを選んでください。

## その他の改善

### Liquid Glassデザインのアップデート

Evermusic 8.6のインターフェースは、アプリ全体でAppleの新しい **Liquid Glass** マテリアルに合わせて更新されました。半透明の表面、よりスムーズなアニメーション、洗練されたコントロールが、iOS、iPadOS、macOSに自然に溶け込みます。

### 中国系サーバーの安定性向上

このリリースでは、**Baidu Netdisk(百度网盘)** と **Aliyun Drive(阿里云盘)** の再生安定性に多くの労力を割きました。Evermusicでこれらのサービスを使ったことがある方は、次のような変化に気づくはずです。

- 数千ファイルのライブラリでもディレクトリ一覧表示が高速化。
- 低速または地理的に距離のある接続でもストリーミングがより安定。
- 長時間の再生セッションでの接続切れが減少。
- ネットワークが一時的に切れた際のリトライと再開ロジックが改善。

これら2つのクラウドは中国でもっとも人気のある一般消費者向けストレージで、Evermusicは両方をネイティブで一級サポートする数少ないiOS音楽プレーヤーの一つです。

### 接続ライブラリの更新

Evermusicが **WebDAV**、**SMB**、**DLNA**、**Dropbox**、**Google Drive**、**OneDrive** などのサービスとやり取りするための内部ライブラリを更新しました。つまり、エッジケースの接続失敗が減少し、新しいサーバーバージョンへの対応が改善され、全体のパフォーマンスが向上しています。

### 新しいホーム画面ウィジェットとよりスマートな更新

新しい歌詞ウィジェットに加えて、既存のホーム画面ウィジェット — 再生中、再生キュー、最近再生 — も **更新ロジックを改善** し、余計な電力を使わずに同期を保つようになりました。ひと目で見える情報をより細かくコントロールしたい方向けに、新しいウィジェットレイアウトも用意されています。

### バグ修正と仕上げ

- 一部のメディアサーバーやセルフホスト構成での再生問題を修正。
- 複数言語のローカライズ修正。
- App Storeのレビューやsupport@everappz.com宛のメールでいただいたフィードバックを基にした多くの細かな改善。

## このアップデートが意味するところ

Evermusic 8.6は次の3つの考えに沿って作られています。

1. **どこに保存していても、あなたの音楽。** ライブラリがiCloud Driveでも、Proton DriveやInternxtのようなプライバシー重視クラウドでも、PlexやJellyfinのメディアサーバーでも、自宅のNASでも、Navidromeを動かすRaspberry Piでも構いません。Evermusicはそれらすべてにネイティブ接続し、どこでも同じ再生体験を提供します。
2. **車内でより快適に。** CarPlayは多くのユーザーが最もよく見る画面であり、再構築した体験はそれを反映しています。
3. **ホーム画面に歌詞を。** 新しい同期歌詞ウィジェットは、誰もまだ十分にうまくできていないものを、あなたのメインの一目で見える領域に届けます。

## Evermusic 8.6を入手する

[**App StoreでEvermusicをダウンロード**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) するか、App Storeからアップデートしてください。Evermusicは無料ダウンロードで、高度な機能向けにオプションのアプリ内アップグレードを提供します。新しいCarPlay、歌詞ウィジェット、新しいすべてのサーバー連携はベースアップデートに含まれます。

アプリを気に入っていただけたら、App Storeでの評価をお願いします。本当に助かります。フィードバックや問題があれば、**support@everappz.com** までメールしてください。すべてのメッセージに目を通しています。

## よくある質問

{{% details title="Evermusic 8.6の新機能は?" closed="true" %}}
Evermusic 8.6は、CarPlay体験の全面刷新、10件以上の新規接続(Plex、Jellyfin、Emby、Subsonic、Navidrome、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、FTP、SFTP、NFS)、ホーム画面向けの新しい同期歌詞ウィジェット、選択モードを備えたWi-Fi DriveのUI改善、Liquid Glassデザインの更新、Baidu NetdiskおよびAliyun Driveの安定性向上、多数のバグ修正を導入しています。
{{% /details %}}

{{% details title="EvermusicはPlexで動作しますか?" closed="true" %}}
はい。Evermusic 8.6からPlex Media Serverに接続して、ライブラリ全体をストリーミングできます。Plex Media Serverの実行は無料で、Plex Passはオプションです。Evermusicは無料セットアップでもPlex Passセットアップでも動作します。
{{% /details %}}

{{% details title="EvermusicでJellyfinやNavidromeはサポートされますか?" closed="true" %}}
はい。JellyfinとNavidromeの両方がEvermusic 8.6で完全サポートされます。Jellyfinは無料のオープンソースメディアサーバー、NavidromeはSubsonic APIを実装した無料のオープンソース音楽サーバーです。Evermusicは両方にネイティブ接続します。
{{% /details %}}

{{% details title="Plex、Jellyfin、Emby、Navidrome、Subsonicは無料ですか?" closed="true" %}}
- **Plex** — サーバーは無料。Plex Passはオプションの有料アップグレード。
- **Jellyfin** — 完全に無料でオープンソース。
- **Emby** — サーバーは無料。Emby Premiereは有料で、モバイル同期とオフラインを解放。
- **Navidrome** — 完全に無料でオープンソース。
- **Subsonic** — 公式サーバーは30日間の試用後に月額1ドル。ただしAPIはオープンで、多くの無料サーバー(Navidromeを含む)がそれを実装しています。
{{% /details %}}

{{% details title="自宅のNASからSFTP、FTP、NFS経由でストリーミングできますか?" closed="true" %}}
はい。Evermusic 8.6はSFTP、FTP、NFSをネイティブ接続タイプとして追加しました。SSH越しにすべてのトラフィックが暗号化されるため、公衆インターネット越しに自分のサーバーからストリーミングするにはSFTPがおすすめです。FTPとNFSはローカルネットワーク内またはVPN経由での利用が最適です。
{{% /details %}}

{{% details title="SFTPでEvermusicをカスタムサーバーに接続するには?" closed="true" %}}
Evermusicを開き、「接続」タブに移動してSFTPを選択し、サーバーのホスト名またはIP、ポート(通常22)、ユーザー名、そしてパスワードまたはSSH秘密鍵を入力します。Evermusicがリモートフォルダを表示し、エンドツーエンド暗号化でオーディオファイルを直接ストリーミングします。
{{% /details %}}

{{% details title="EvermusicはInternxtとProton Driveをサポートしますか?" closed="true" %}}
はい。Evermusic 8.6から、両方のプライバシー重視クラウドをサポートします。アプリで既に利用できるMegaなどのプライバシーファーストサービスに加わる形です。
{{% /details %}}

{{% details title="EvermusicのWi-Fi Driveとは?" closed="true" %}}
Wi-Fi Driveは、Evermusicに組み込まれているワイヤレスファイル転送機能です。iTunesもケーブルもクラウドアカウントも不要で、ローカルWi-Fiネットワーク経由でコンピュータからiPhoneまたはiPadに音楽をアップロードできます。任意のデスクトップブラウザや、Mac Finder、Windows File ExplorerのようなWebDAVクライアントを使えます。[Wi-Fi Driveの完全ガイド](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/)を参照してください。
{{% /details %}}

{{% details title="新しい歌詞ウィジェットはどう動作しますか?" closed="true" %}}
歌詞ウィジェットは、再生中の楽曲のタイミング同期歌詞をiPhone、iPad、Macのホーム画面に表示します。表示される行は曲の進行に合わせて自動的に進みます。ホーム画面を長押しして「編集 > ウィジェットを追加」をタップし、Evermusicを検索して歌詞ウィジェットを選んで追加します。
{{% /details %}}

{{% details title="Evermusic 8.6はBaidu NetdiskとAliyun Driveの再生問題を修正しますか?" closed="true" %}}
はい。百度网盘(Baidu Netdisk)と阿里云盘(Aliyun Drive)で大きな安定性改善を行いました。ディレクトリ一覧の高速化、弱い接続でのよりスマートなリトライ、長時間再生セッション時の再開動作の改善などを含みます。
{{% /details %}}

{{% details title="Evermusic 8.6への更新は無料ですか?" closed="true" %}}
はい。EvermusicはApp Storeから無料でダウンロードでき、8.6は既存のすべてのユーザー向けの無料アップデートです。新しいCarPlay、歌詞ウィジェット、新しいすべてのサーバー連携はベースアップデートに含まれます。
{{% /details %}}

{{% details title="Evermusic 8.6が利用できる端末は?" closed="true" %}}
Evermusic 8.6はiPhone、iPad、Macで動作します。CarPlayサポートにはCarPlay対応の車両またはアフターマーケットヘッドユニットが必要です。
{{% /details %}}
