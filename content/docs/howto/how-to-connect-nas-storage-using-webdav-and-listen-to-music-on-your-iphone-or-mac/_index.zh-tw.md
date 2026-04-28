---
title: "如何使用 WebDAV 連接 NAS 儲存並在 iPhone 或 Mac 上聽音樂"
date: 2024-07-28
description: "了解如何在 Synology NAS 上設定 WebDAV，並使用 Evermusic 或 Flacbox 將音樂串流到 iPhone 或 Mac。按照我們的逐步指南操作。"
keywords: ["連接 nas", "webdav synology", "串流音樂 nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["音樂", "串流", "儲存", "nas", "連接", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**摘要：**在 Synology NAS 上安裝並啟用 WebDAV，設定共用資料夾權限，然後使用 NAS IP 位址和 WebDAV 連接埠（預設 5005/5006）從 Evermusic 或 Flacbox 連接。您可以串流和管理整個音樂庫，無需將檔案複製到裝置。

了解如何使用 WebDAV 連接您的 NAS 儲存，並輕鬆將音樂庫串流到 iPhone 或 Mac。WebDAV（Web-based Distributed Authoring and Versioning）是一種允許您透過網際網路管理和共用檔案的通訊協定。透過在 NAS 上設定 WebDAV，您可以存取和串流音樂收藏，確保您最喜愛的歌曲隨時觸手可及。

在本指南中，我們將向您展示如何在最受歡迎的 NAS 伺服器之一 Synology NAS 上設定 WebDAV 連接。按照我們簡單的步驟在 Synology NAS 上設定 WebDAV，您將能夠直接從 iPhone 或 Mac 瀏覽、串流和管理音樂庫。

## 步驟 1：在 Synology NAS 上安裝 WebDAV

1. 登入 Synology NAS 並開啟**套件中心**。
2. 搜尋「webdav」並安裝 WebDAV 套件（如果尚未安裝）。開啟 WebDAV 伺服器進行設定。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="在 Synology 上安裝 WebDAV" width="600" >}}

## 步驟 2：設定 WebDAV 伺服器

1. 在 WebDAV 設定頁面，勾選**啟用 HTTP**、**啟用 HTTPS**、**啟用匿名 WebDAV** 和**啟用 DavDepthInfinity** 的核取方塊。
2. 按一下**套用**儲存變更。記下 HTTP 和 HTTPS 連接的連接埠號，預設為 5005 和 5006。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="設定 WebDAV 參數" width="600" >}}

## 步驟 3：設定共用資料夾權限

1. 開啟**控制台**並前往**共用資料夾**區段。
2. 選擇**音樂**資料夾並按一下**編輯**。
3. 在**權限**標籤頁中，設定權限。如果只需聽音樂，啟用唯讀的訪客存取；如果需要修改檔案，啟用讀取/寫入權限。儲存變更。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="共用資料夾權限" width="600" >}}

## 步驟 4：尋找 Synology NAS IP 位址

1. 開啟**控制台**並前往**網路介面**標籤頁，或使用瀏覽器造訪 [find.synology.com](http://find.synology.com)。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="尋找 NAS IP 位址" width="600" >}}

2. 記下 Synology NAS 的 IP 位址（例如 192.168.18.137）。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Synology NAS IP 位址" width="600" >}}

## 步驟 5：使用 Evermusic/Flacbox 連接 Synology NAS

1. 開啟 Evermusic 或 Flacbox 應用程式並前往**連接**標籤頁。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Evermusic 中的連接標籤頁" width="600" >}}

2. 要自動連接，在**可用設備**區段找到 Synology NAS 並點擊連接。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="可用設備列表" width="600" >}}

3. 要手動連接，選擇**連接雲端服務**並選擇 **WebDAV**。按以下格式輸入伺服器位址：PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER（例如 [https://192.168.18.137:5006](https://192.168.18.137:5006)）。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="手動設定 WebDAV" width="600" >}}

4. 訪客存取時將登入名稱和密碼欄位留空，或輸入 Synology 憑證。點擊**登入**。

## 步驟 6：瀏覽和播放音樂

1. 連接後，裝置將出現在**連接的配件**列表中。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Evermusic 中的已連接裝置" width="600" >}}

2. 導覽到**音樂**資料夾並點擊任意音訊檔案開始播放。

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="瀏覽音樂資料夾" width="600" >}}

## 步驟 7：將已連接的雲端資料夾新增到音樂庫

1. 在應用程式中開啟**音樂庫**區段。
2. 選擇**新增音樂**並選擇**連接**。
3. 選擇已連接的 NAS 伺服器並選擇**音樂**資料夾。點擊**完成**。
4. 應用程式將掃描音樂資料夾並將支援的音訊檔案新增到音樂庫。中繼資料將被載入，您的曲目將按專輯、藝人和類型分組。

## 總結

按照這些步驟，您可以輕鬆地在 Synology NAS 上設定 WebDAV 連接，並使用 Evermusic 或 Flacbox 將音樂庫串流到 iPhone 或 Mac。隨時享受對您最喜愛曲目的無縫存取。

## 常見問題

{{% details title="哪些 NAS 裝置支援 WebDAV？" closed="true" %}}
大多數熱門的 NAS 品牌都支援 WebDAV，包括 Synology、QNAP、TrueNAS 和 Western Digital。請查閱您的 NAS 製造商文件以取得 WebDAV 設定說明。
{{% /details %}}

{{% details title="WebDAV 和 SMB 在 NAS 音樂串流方面有什麼區別？" closed="true" %}}
WebDAV 透過 HTTP/HTTPS 運作，更適合透過網際網路進行遠端存取。SMB 在區域網路中通常更快。Evermusic 和 Flacbox 支援這兩種通訊協定，因此根據您需要本地還是遠端存取來選擇。
{{% /details %}}

{{% details title="在 Synology 上使用 WebDAV 需要使用者名稱和密碼嗎？" closed="true" %}}
不需要，如果您啟用了匿名 WebDAV 存取並在共用資料夾上設定了訪客權限。為了更好的安全性，您可以使用 Synology 憑證。
{{% /details %}}

{{% details title="我可以透過 WebDAV 從 NAS 串流 FLAC 和其他高解析度格式嗎？" closed="true" %}}
可以。Evermusic 和 Flacbox 在透過 WebDAV 從 NAS 儲存串流時都支援 FLAC、ALAC、WAV、DSD 和其他高解析度格式。
{{% /details %}}

{{% details title="為什麼應用程式在可用設備中找不到我的 NAS？" closed="true" %}}
確保您的 iPhone/Mac 和 NAS 在同一個 Wi-Fi 網路上。如果自動探索不起作用，請使用手動連接選項並直接輸入 NAS IP 位址和 WebDAV 連接埠。
{{% /details %}}
