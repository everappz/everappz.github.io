---
title: "如何在 Windows 10 上啟用 DLNA 媒體伺服器並在 iPhone 上播放音樂"
date: 2019-11-26
description: "在 Windows 10 上啟用 DLNA 伺服器，並使用 Evermusic 應用程式將音樂串流到 iPhone。包含逐步設定指南。"
keywords: ["evermusic", "dlna", "windows 10", "iphone 音樂串流", "媒體伺服器", "本地網路", "upnp"]
tags: ["evermusic", "音樂", "雲端", "iphone", "儲存", "本地", "nas", "windows", "wifi", "聆聽", "網路", "遠端", "家庭", "線上", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**摘要：** Windows 10 內建了 DLNA 伺服器。在網路和共用設定中啟用它，然後使用 iPhone 上的免費 **Evermusic** 應用程式透過 Wi-Fi 串流整個音樂庫。無需第三方伺服器軟體。

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA：封面" caption="使用 Windows 10 和 Evermusic 將音樂透過 DLNA 串流到 iPhone" width="800" >}}

DLNA（數位生活網路聯盟）是一個強大的工具，可讓您輕鬆地在網路上的 DLNA 支援裝置之間串流各種媒體內容，包括音樂。好消息是，Windows 10 及之前的版本都內建了 DLNA 功能，無需第三方媒體伺服器。以下是如何在 Windows 10 上啟用 DLNA 媒體伺服器並在 iPhone 上享受音樂串流。

## 如何在 Windows 10 上啟用 DLNA 媒體伺服器

1. 點擊「開始」按鈕。  
2. 選擇「設定」圖示。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="伺服器設定" caption="開啟 Windows 設定" width="500" >}}

3. 在「Windows 設定」畫面上，選擇「網路和網際網路」。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Windows 設定" caption="選擇網路和網際網路" width="500" >}}

4. 在「網路」下，選擇「網路和共用中心」。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="共用中心" caption="開啟網路和共用中心" width="500" >}}

5. 在「網路和共用中心」畫面上，點擊左側選單中的「變更進階共用設定」。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="進階共用設定" caption="變更進階共用設定" width="500" >}}

6. 在「進階共用設定」畫面上，向下捲動到「所有網路」區段，點擊箭頭展開。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="開啟探索" caption="展開所有網路設定" width="500" >}}

7. 點擊「開啟媒體串流」以啟動 DLNA 伺服器。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="開啟伺服器" caption="啟用媒體串流伺服器" width="500" >}}

8. 為媒體庫命名並選擇允許存取的裝置。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="媒體庫名稱" caption="命名您的 DLNA 媒體庫" width="500" >}}

9. 點擊「確定」確認操作。現在，您的個人資料夾（如音樂、圖片和影片）將對任何支援 UPnP 的串流裝置可見。

## 如何在 Windows 10 上停用 DLNA 媒體伺服器

1. 點擊「開始」並在搜尋欄中輸入「services」。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Windows 服務" caption="開啟 Windows 服務" width="500" >}}

2. 在「服務」畫面上，向下捲動找到「Windows Media Player Network Sharing Service」。  
3. 雙擊它並將「啟動類型」設定為「手動」。  
4. 點擊「停止」按鈕停止服務。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="停止 DLNA 服務" caption="停用 DLNA 網路共用服務" width="500" >}}

## 如何在 iPhone 上從 DLNA 伺服器播放音樂

1. 從 App Store 安裝免費的 **Evermusic** 應用程式：  
   [Evermusic 應用程式](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. 開啟「連線」標籤頁，點擊「本地網路」區段中的「可用裝置」。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Evermusic 連線" caption="Evermusic：連線畫面" width="500" >}}

3. 等待幾秒鐘裝置清單載入，然後點擊 Windows Media Player DLNA 伺服器（例如「MSEDGEWIN10: My Windows Library」）。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="可用裝置" caption="Evermusic 中可用的 DLNA 伺服器" width="500" >}}

4. 您將看到媒體伺服器上可用資料夾的清單。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Evermusic 資料夾" caption="瀏覽 DLNA 伺服器的共用資料夾" width="500" >}}

5. 開啟任何包含音訊檔案的資料夾。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="資料夾內容" caption="檢視共用 DLNA 資料夾的內容" width="500" >}}

6. 點擊任何檔案啟動音訊播放器。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="音訊播放器" caption="在 Evermusic 中播放 DLNA 的音訊檔案" width="500" >}}

7. 要增強音訊體驗，點擊畫面底部音量指示器旁的「等化器」圖示，啟用帶前級放大器的 iPod 風格等化器。

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="等化器" caption="使用內建等化器增強播放效果" width="500" >}}

## 結論

透過 Windows 10 上的 DLNA 媒體伺服器和 iPhone 上的 Evermusic，您可以享受從電腦到行動裝置的無縫音樂串流。告別儲存限制，擁抱隨選音樂！

## 常見問題

{{% details title="我需要在 Windows 10 上安裝伺服器軟體嗎？" closed="true" %}}
不需要。Windows 10 包含內建的 DLNA 媒體伺服器。您只需在網路和共用中心設定中啟用媒體串流即可。無需第三方軟體。
{{% /details %}}

{{% details title="我的 iPhone 需要在同一個 Wi-Fi 網路上嗎？" closed="true" %}}
是的。DLNA 串流透過本地網路工作。您的 Windows 10 電腦和 iPhone 都必須連接到同一個 Wi-Fi 網路，Evermusic 才能發現 DLNA 伺服器。
{{% /details %}}

{{% details title="我可以透過 DLNA 串流哪些音訊格式？" closed="true" %}}
Windows DLNA 伺服器會共用音樂資料夾中的檔案，不受格式限制。Evermusic 支援 MP3、FLAC、AAC、WAV、OGG、AIFF 等多種格式，因此您幾乎可以播放伺服器上的任何音訊檔案。
{{% /details %}}

{{% details title="我可以使用 Flacbox 代替 Evermusic 嗎？" closed="true" %}}
可以。Flacbox 也支援 DLNA/UPnP 瀏覽和播放。您可以使用任一應用程式來發現和播放 Windows DLNA 伺服器上的音樂。
{{% /details %}}

{{% details title="DLNA 串流會使用行動數據嗎？" closed="true" %}}
不會。DLNA 完全在本地 Wi-Fi 網路上運作。不使用任何行動數據。但是，播放期間兩台裝置都必須保持連接到同一網路。
{{% /details %}}
