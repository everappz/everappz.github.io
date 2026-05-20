---
title: "Flacbox 7.4: 刷新されたCarPlay、Plex、Jellyfin、Subsonic、SFTPでHi-Resオーディオ"
date: 2026-05-20
description: "Flacbox 7.4はゼロから作り直したCarPlay体験を搭載し、ロスレスライブラリを再生する10以上の新しい方法 — Plex、Subsonic、Navidrome、Jellyfin、Emby、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、加えてFTP、SFTP、NFS — を追加します。刷新されたホーム画面ウィジェット、Liquid Glassデザイン、iPhoneとMacでのFLAC、DSD、ALAC、APE再生のための強化されたネットワークライブラリを含みます。"
keywords: ["Flacbox 7.4", "Flacboxアップデート", "CarPlay hi-resオーディオプレーヤー", "CarPlay FLACプレーヤー iPhone", "Plex hi-res音楽 iPhone", "Plex ロスレスストリーミング", "Jellyfin FLACプレーヤー iOS", "Emby ロスレス音楽 iOS", "Subsonic FLAC iPhone", "Navidrome ロスレス iOSクライアント", "Internxt FLACストリーミング", "Proton Drive ロスレス音楽", "QNAP hi-res音楽プレーヤー", "Nextcloud FLACストリーミング iOS", "Amazon S3 ロスレスオーディオ iPhone", "SFTP FLACプレーヤー iPhone", "FTP hi-resオーディオ iOS", "NFS ロスレスストリーミング iPhone", "NASからDSDストリーム iPhone", "DSDプレーヤー iPhone 2026", "ALACプレーヤー iOS", "ロスレス音楽プレーヤー iPhone", "Liquid Glassオーディオアプリ", "hi-resオーディオプレーヤー iOS 2026"]
tags: ["Flacbox", "Flacbox 7.4", "CarPlay", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "ホーム画面ウィジェット", "Liquid Glass", "Hi-Resオーディオ", "FLAC", "DSD", "ALAC", "新機能"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**要点:** [Flacbox 7.4](/products/flacbox) はiPhoneとMacのhi-resオーディオプレーヤーの大型アップデートです。CarPlayをゼロから作り直し、クイックソート、複数のカラーテーマ、新しいNow Playing画面、再生キューを一目で確認、巨大なライブラリ向けの頭文字インデックスを搭載。このアップデートで音楽にアクセスする10以上の新しい方法を追加 — プライバシー重視のクラウド **Internxt** と **Proton Drive**、個人サーバー **QNAP**、**Nextcloud**、**Amazon S3**、ストリーミングサーバー **Plex**、**Subsonic**、**Navidrome**、**Jellyfin**、**Emby**、加えてネットワークプロトコル **FTP**、**SFTP**、**NFS** に対応。インターフェースはAppleの新しい **Liquid Glass** マテリアルに合わせて調整され、基盤となるネットワークライブラリは強化され、ホーム画面ウィジェットはより信頼性高くリフレッシュされます。

---

## 皆さん、こんにちは!

Flacboxの大型アップデートが到着しました。CarPlayをゼロから作り直し、ロスレスライブラリへの接続方法を十以上追加しました — プライバシー重視のクラウドストレージから人気のセルフホスト型メディアサーバー、定番のネットワークプロトコルまで。

[App StoreからFlacbox 7.4をダウンロード](https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8) するか、既存のバージョンからアップデートしてください。Macユーザーは [デスクトップ版をこちら](https://apps.apple.com/app/apple-store/id1594027432?pt=95781850&ct=everappzcom&mt=8) から入手できます。

## CarPlay、ゼロから作り直し

**Apple CarPlay** をFlacbox向けにゼロから再設計し、運転中のリスニングがより安全で簡単に感じられるようにしました。曲の見つけ方から再生コントロールまで、あらゆる細部が車内体験に合わせて再調整されています。

- **クイックソート** — アルバム、アーティスト、プレイリスト、フォルダにわたり、エンドレスなスクロールなしでどんな曲にも一瞬で到達できます。
- **車に合うカラーテーマ** — ダッシュボードや車内のイルミネーションに合うテーマを、昼でも夜でも選べます。
- **新しいNow Playing画面** — 大きなアートワーク、より明確なコントロール、ワンタップで使える新しい再生アクション。
- **再生キューが一目で確認可能** — 現在の画面から離れずに次の曲を確認できます。
- **大きなライブラリ向けの頭文字インデックス** — 1タッチで数万曲のFLAC、DSD、ALAC、APEトラックを移動できます。
- **読み込みが高速化、停止はもうありません** — 大きなフォルダ、クラウドディレクトリ、メディアサーバーライブラリの開く動作が瞬時に感じられます。

運転中にロスレスオーディオをストリーミングしているなら — Dropbox、Google Drive、OneDrive、iCloud Drive、[Plex](#media-servers)、[Jellyfin](#media-servers)、Subsonic、その他のソースから — 再構築されたCarPlay体験は、全体のフローを車にネイティブに感じさせます。

## 音楽を接続する10以上の新しい方法

Flacbox 7.4は「音楽ライブラリ」の定義を広げます。hi-resファイルが信頼するクラウド、自宅のNAS、セルフホスト型ストリーミングサーバーにある場合、Flacboxは今や直接そこから再生できます — 同期、エクスポート、フォーマット変換は不要です。

### プライベートクラウド: InternxtとProton Drive

エンドツーエンド暗号化やゼロ知識ストレージが重要であれば、プライバシー重視のクラウドの中で最も評価されている2つがFlacboxでネイティブ対応しました。

- **Internxt** — オープンソース、ポスト量子暗号、GDPR準拠のスペイン発クラウド。無料プランあり。
- **Proton Drive** — Proton MailとProton VPNの開発元によるエンドツーエンド暗号化ストレージ。スイス拠点。無料枠と、より大きなライブラリ向けの有料プランがあります。

一度接続すれば、FLAC、DSD、ALACファイルは暗号化されたトンネルを通じてストリーミングされます — Flacboxがあなたのデータを平文で見ることはなく、プロバイダーのサーバーからも見えません。

### 個人サーバー: QNAP、Nextcloud、Amazon S3

自分でインフラを運用するリスナー向け:

- **QNAP** — QNAP NASへのネイティブAPI接続。ローカルWi-Fiやリモートで高速かつ安定した再生が可能です。再エンコードなしで高ビットレートのFLACとDSDを直接ストリーミング。
- **Nextcloud** — セルフホストまたはマネージドを問わず、任意のNextcloudインスタンスに接続できます。プライバシー上の理由でGoogle DriveやDropboxから移行済みの方に最適。
- **Amazon S3** — 任意のS3バケット(Backblaze B2、Wasabi、MinIO、Cloudflare R2などのS3互換ストレージも可)にFlacboxを接続して、コレクションを直接ストリーミングできます。

### <a id="media-servers"></a>ストリーミングサーバー: Plex、Subsonic、Navidrome、Jellyfin、Emby

セルフホスト型音楽ファンにとって最大の目玉です。Flacbox 7.4は、人気のあるオープンソースとフリーミアム系メディアサーバー向けの一級hi-resクライアントとして、iPhoneやMacを生まれ変わらせます。

- **Plex** — Plex Media Serverのダウンロードと運用は **無料** です。**Plex Pass** サブスクリプションはオプションで、モバイル同期、ハードウェアトランスコード、その他のエクストラを解放します。Flacboxは無料ライブラリでもPlex Passライブラリでも動作します。
- **Subsonic** — セルフホスト型音楽ストリーミングサーバーの元祖。公式Subsonicサーバーは **有料** (30日間の試用後に月額1ドル)ですが、FlacboxはSubsonic APIに対応する数十のサーバーとも会話できます。
- **Navidrome** — モダンで軽量、**完全に無料かつオープンソース** な音楽サーバーで、Goで書かれています。Subsonic APIを実装。Raspberry Pi、NAS、任意のLinuxマシンで動作します。数十万曲規模までのロスレスコレクションに強くおすすめ。
- **Jellyfin** — **完全に無料かつオープンソース** のメディアサーバー(Embyのコミュニティフォーク)。音楽、映画、テレビ、オーディオブックを扱えます。アカウント不要、テレメトリーなし、サブスクなし。
- **Emby** — **フリーミアム** のメディアサーバー。コアサーバーは無料で、**Emby Premiere** は買い切りまたは年額の有料プランで、モバイルアプリ、オフライン同期などを解放します。Flacboxは無料・Premiere両方のライブラリに接続できます。

どのサーバーを使っていても、Flacboxはコレクション全体 — アルバム、アーティスト、プレイリスト、ジャンル、埋め込みアートワーク — をストリーミングします。USB DACへのbit-perfect出力、10バンドイコライザー、クロスフェードとギャップレス再生、AirPlay、Chromecast、そして再構築された **CarPlay** 体験に対応。サーバーが管理する再生履歴も尊重します。

### 新しい転送方法: FTP、SFTP、NFS

カスタムサーバー、ホームラボ、洗練されたモバイルアプリのない汎用NASを使うリスナーのために、Flacbox 7.4は3つの定番ネットワークプロトコルを追加しました。

- **SFTP (SSH File Transfer Protocol)** — **自分のサーバーから安全にリモートストリーミングする** のに最適な答え。SFTPはSSH上で動作するため、転送全体(認証もオーディオデータも)が暗号化されます。SSHアクセスがあるVPS、専用サーバー、自宅のLinuxマシンがあれば、FLACやDSDのフォルダを置いて他には何も公開せずに公衆インターネット越しにストリーミングできます。パスワード認証と鍵認証に対応。
- **FTP** — 長年使われてきたファイル転送の標準。**自宅のNAS** (古いSynology、ASUS、D-Link、TerraMaster、汎用ボックス)がFTPサーバーを公開していてネイティブAPI連携がない場合に有用。ローカルネットワーク内での利用が最適です。
- **NFS (Network File System)** — LinuxやほとんどのNASデバイスで事実上の共有プロトコル。NFS共有はホームラボや小規模オフィスのネットワークでよく使われており、Flacboxは現在マウントしてbit-perfectオーディオを直接ストリーミングできます。同等のハードウェア上でSMBよりオーバーヘッドが少なくなります。

> **ヒント:** 公衆インターネット越しのストリーミングにはSFTPがおすすめです。FTPとNFSはローカルネットワーク内での利用が最適 — VPNでラップしない限り、これらを公衆インターネットに公開しないでください。

## その他の改善

### Liquid Glassに合う新しい見た目

Flacbox 7.4のインターフェースは、アプリ全体でAppleの新しい **Liquid Glass** マテリアルに合わせて更新されました — 半透明の表面、よりスムーズなアニメーション、iOS 26とmacOS 26に自然に溶け込む洗練されたコントロール。ライブラリ、Now Playing、イコライザー、設定画面はすべて新しいシステム美学に合わせて再調整されました。

### より強力なネットワークライブラリ

Flacboxが **WebDAV**、**SMB**、**DLNA**、**Dropbox**、**Google Drive**、**OneDrive**、**iCloud Drive**、**MEGA** などのサービスとやり取りするための基盤ライブラリを更新しました。つまり、エッジケースの接続失敗が減少し、新しいサーバーバージョンへの対応が改善され、遅いまたは地理的に離れた接続での高ビットレートオーディオストリーミングの信頼性が向上しています。

### 一部のサーバーでの再生を修正

特定のセルフホストサーバーでの再生問題のいくつかを追跡して修正しました — 大きなFLACおよびDSDファイルでのシーク後のスタックや、非常に長いファイルリストを持つライブラリでの遅い起動時間を含みます。ストリーミングがエンドツーエンドでよりクリーンに感じられるはずです。

### より良いリフレッシュを備えた新しいホーム画面ウィジェット

ホーム画面ウィジェット — Now Playing、再生キュー、最近再生 — は、よりすっきりしたレイアウトとよりスマートなリフレッシュポリシーで再設計されました。アプリと同期した状態を保ちつつ余計なバッテリーを消費せず、いくつかの新しいウィジェットサイズによって、一目で見えるものをよりコントロールできます。

### 翻訳の修正

ユーザーからの直接のフィードバックに基づく、複数言語にわたる多くの小さなローカライズ修正。小さなボタンや長いヨーロッパ言語(ドイツ語、オランダ語、フランス語、スペイン語)でテキストがよりよく収まります。

### あなたのメッセージにインスパイアされた小さな仕上げ

App Storeのレビューやsupport@everappz.com宛のメールを基にした、数えきれないほどの小さな改善。すべてのメッセージに目を通しています。

## このアップデートが意味するところ

Flacbox 7.4は2つの考えに沿って作られています。

1. **どこに保存していても、あなたのhi-res音楽。** ロスレスライブラリがiCloud Driveでも、Proton DriveやInternxtのようなプライバシー重視クラウドでも、PlexやJellyfinのメディアサーバーでも、自宅のNASでも、Navidromeを動かすRaspberry Piでも構いません。Flacboxはそれらすべてにネイティブ接続し、どこでも同じbit-perfectの再生体験を提供します。
2. **車内でより快適に。** CarPlayは多くのリスナーが最もよく見る画面であり、再構築された体験はそれを反映しています — より速く、より安全に、本物のドライバーが音楽にたどり着く方法を中心に作られています。

## Flacbox 7.4を入手する

[**App StoreでFlacboxをダウンロード**](https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8) するか、App Store内からアップデートしてください。[Mac版](https://apps.apple.com/app/apple-store/id1594027432?pt=95781850&ct=everappzcom&mt=8) はユニバーサルMacアプリとして別途利用可能です。Flacboxは無料ダウンロードで、高度な機能向けにオプションのアプリ内アップグレードを提供します。再構築されたCarPlay、すべての新しいクラウドとサーバー接続、刷新されたホーム画面ウィジェット、Liquid Glass UIはベースアップデートに含まれます。

アプリが一日をより良くしてくれたなら、App Storeでの評価が本当に助かります。質問や問題があれば、**support@everappz.com** までメールしてください。本物の人間が返信します。

## よくある質問

{{% details title="Flacbox 7.4の新機能は?" closed="true" %}}
Flacbox 7.4は完全に再構築されたCarPlay体験を搭載し、10以上の新しい接続 — Plex、Jellyfin、Emby、Subsonic、Navidrome、Internxt、Proton Drive、QNAP、Nextcloud、Amazon S3、FTP、SFTP、NFS — を追加します。このリリースはLiquid Glassデザインのリフレッシュ、より強力なネットワークライブラリ、よりスマートなリフレッシュを備えた再設計されたホーム画面ウィジェット、一部のサーバーでの再生修正、翻訳改善、多くの小さな仕上げ項目も含みます。
{{% /details %}}

{{% details title="FlacboxはFLACおよびロスレスオーディオでPlexと動作しますか?" closed="true" %}}
はい。Flacbox 7.4からPlex Media Serverに接続して、hi-resライブラリ全体 — FLAC、ALAC、WAV、AIFF、OGG、OPUS、その他のロスレスフォーマット — をストリーミングできます。Plex Media Serverの実行は無料で、Plex Passはオプションです。Flacboxは無料設定でもPlex Pass設定でもサポートします。
{{% /details %}}

{{% details title="JellyfinまたはNavidromeはFlacboxでサポートされますか?" closed="true" %}}
はい。両方ともFlacbox 7.4で完全にサポートされています。Jellyfinは無料のオープンソースメディアサーバーです。NavidromeはSubsonic APIを実装した無料のオープンソース音楽サーバーです。Flacboxは両方にネイティブ接続し、ロスレスライブラリを完全なメタデータとアートワーク付きでストリーミングします。
{{% /details %}}

{{% details title="Plex、Jellyfin、Emby、Navidrome、Subsonicは無料ですか?" closed="true" %}}
- **Plex** — サーバーは無料。Plex Passはオプションの有料アップグレード。
- **Jellyfin** — 完全に無料でオープンソース。
- **Emby** — サーバーは無料。Emby Premiereは有料で、モバイル同期とオフラインを解放。
- **Navidrome** — 完全に無料でオープンソース。
- **Subsonic** — 公式サーバーは30日間の試用後に月額1ドル。ただしAPIはオープンで、多くの無料サーバー(Navidromeを含む)がそれを実装しています。
{{% /details %}}

{{% details title="自宅のNASからSFTP、FTP、NFS経由でFLACとDSDをストリーミングできますか?" closed="true" %}}
はい。Flacbox 7.4はSFTP、FTP、NFSをネイティブ接続タイプとして追加します。SSH越しにすべてのトラフィックが暗号化されるため、公衆インターネット越しに自分のサーバーからストリーミングするにはSFTPがおすすめです。FTPとNFSはローカルネットワーク内またはVPN経由での利用が最適です。
{{% /details %}}

{{% details title="SFTPでFlacboxをカスタムサーバーに接続するには?" closed="true" %}}
Flacboxを開き、Connectionsタブに移動してSFTPを選択し、サーバーのホスト名またはIP、ポート(通常22)、ユーザー名、パスワードまたはSSH秘密鍵を入力します。Flacboxがリモートフォルダを表示し、エンドツーエンド暗号化でオーディオファイルを直接ストリーミングします。
{{% /details %}}

{{% details title="FlacboxはInternxtとProton Driveをサポートしますか?" closed="true" %}}
はい。Flacbox 7.4から両方のプライバシー重視クラウドをサポートします。アプリで既に利用できるMEGAなどのプライバシーファーストサービスに加わる形です。
{{% /details %}}

{{% details title="FlacboxはPlex、Jellyfin、NASからDSDファイルを再生しますか?" closed="true" %}}
はい。FlacboxはPlex、Jellyfin、Emby、Subsonic互換サーバー、QNAP、Nextcloud、Amazon S3、そしてSFTP、FTP、NFS経由でストリーミングされるDSD64、DSD128、DSD256ファイル(DSFおよびDFFコンテナ)を再生します。USB DACへのbit-perfect出力はiPhone、iPad、Macでサポートされています。
{{% /details %}}

{{% details title="再設計されたCarPlay画面はどう動作しますか?" closed="true" %}}
FlacboxのCarPlayインターフェースは、アルバム、アーティスト、プレイリスト、フォルダにわたるクイックソート;さまざまな車の内装に合う複数のカラーテーマ;新しいコントロールを備えた新しいNow Playing画面;一目で確認できる再生キュー;大きなライブラリ間を移動する頭文字インデックス;大きなフォルダとクラウドディレクトリでの高速読み込みで再構築されました。
{{% /details %}}

{{% details title="Flacbox 7.4へのアップデートは無料ですか?" closed="true" %}}
はい。FlacboxはApp Storeから無料でダウンロードでき、7.4は既存のすべてのユーザー向けの無料アップデートです。再構築されたCarPlay、すべての新しいクラウドとサーバー接続、刷新されたホーム画面ウィジェット、Liquid Glass UIはベースアップデートに含まれます。
{{% /details %}}

{{% details title="Flacbox 7.4が利用できるデバイスは?" closed="true" %}}
Flacbox 7.4はiPhone、iPad、Macで動作します。CarPlayサポートにはCarPlay対応の車両またはアフターマーケットヘッドユニットが必要です。AirPlayとChromecastを使ってより大きなシステムに再生をキャストでき;USB DACはbit-perfectロスレス出力に対応しています。
{{% /details %}}
