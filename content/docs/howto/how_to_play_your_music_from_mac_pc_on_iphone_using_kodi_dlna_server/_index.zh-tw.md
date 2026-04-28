---
title: "如何使用 Kodi DLNA 伺服器在 iPhone 上播放 Mac / PC / Linux / NAS 中的音樂"
date: 2025-07-25
description: "使用 Kodi DLNA 和 Evermusic 應用程式透過 Wi-Fi 將電腦或 NAS 中的音樂串流到 iPhone。"
keywords: ["kodi dlna 伺服器", "將音樂串流到 iphone", "從 nas 播放音樂", "evermusic dlna", "mac 到 iphone 音樂", "windows 到 iphone 音樂", "kodi dlna iphone", "dlna 音訊串流"]
tags: ["dlna", "kodi", "evermusic", "iphone", "音樂串流", "mac", "nas", "linux", "本地網路"]
readingTime: 5
---

{{< author-byline >}}

**TL;DR:** 在 Mac、PC、Linux 或 NAS 上安裝 Kodi，啟用 DLNA/UPnP 伺服器，使用免費的 Evermusic 或 Flacbox 應用程式透過 Wi-Fi 將整個音樂庫串流到 iPhone 或 iPad。無需訂閱。

## 簡介

如果您有 **Mac、Windows PC、Linux 電腦或 NAS 裝置**，您可以使用 [Kodi](https://kodi.tv/)（一個免費的開源媒體平台）輕鬆將其轉變為家中的**個人音樂伺服器**。藉助 Kodi 內建的 **DLNA/UPnP 伺服器**，您可以將整個音樂庫串流到任何相容 DLNA 的用戶端——包括您的 iPhone 或 iPad。

在本指南中，我們將逐步向您展示如何：

- 在 Mac 或 PC 上安裝 Kodi
- 設定音樂資料夾以進行共享
- 啟用 DLNA 音樂伺服器
- 使用 **Evermusic** 或 **Flacbox** iOS 應用程式存取音樂

此設定 100% 免費——無需訂閱，只需透過 Wi-Fi 網路串流您自己的音樂。

## 在 Mac / PC / Linux / NAS 上下載並安裝 Kodi

首先，造訪 Kodi 官方網站：

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Kodi 首頁" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

點選**下載**並向下捲動找到適合您電腦的版本。
選擇您的作業系統。在此範例中，我們將使用 **macOS**。

{{< cards cols="1">}}
{{< card subtitle="Kodi 下載頁面" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

如果您有 Intel Mac，請點選 **Intel (x86/64)**，或為 M1、M2、M3 Mac 點選 **Apple Silicon** 開始下載。

{{< cards cols="1">}}
{{< card subtitle="選擇 macOS 安裝程式" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

請稍候，安裝程式正在下載。

{{< cards cols="1">}}
{{< card subtitle="Kodi 已下載" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

下載後，在**下載**資料夾中找到 `.dmg` 檔案。

{{< cards cols="1">}}
{{< card subtitle="安裝 Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

雙擊下載的檔案以啟動安裝程式。
將 Kodi 拖到**應用程式**資料夾中進行安裝。

{{< cards cols="1">}}
{{< card title="" subtitle="將 Kodi 拖到應用程式中安裝" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

啟動 Kodi。您可能需要在**系統偏好設定 → 安全性與隱私權 → 仍然開啟**中允許它。

{{< cards cols="1">}}
{{< card subtitle="Kodi 主畫面" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## 將音樂加入 Kodi 媒體庫

從主畫面點選**齒輪圖示**（設定）。

{{< cards cols="1">}}
{{< card subtitle="Kodi 設定" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

導覽至**媒體設定 → 媒體庫**。啟用影片庫和音樂庫的**啟動時更新媒體庫**以進行自動索引。

{{< cards cols="1">}}
{{< card subtitle="媒體庫設定" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

然後前往**音樂**部分並點選**新增音樂**。

{{< cards cols="1">}}
{{< card subtitle="新增音樂資料夾" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

瀏覽並選擇儲存音樂的資料夾。

{{< cards cols="1">}}
{{< card subtitle="選擇音樂來源" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

將音樂來源新增到 Kodi。

{{< cards cols="1">}}
{{< card subtitle="新增音樂來源" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

確認並讓 Kodi 掃描您的音樂庫。

{{< cards cols="1">}}
{{< card subtitle="確認音樂來源" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

請稍候，媒體庫正在掃描和完全建立。

{{< cards cols="1">}}
{{< card subtitle="正在掃描音樂庫" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## 啟用 Kodi 的 DLNA 伺服器

前往**設定 → 服務 → UPnP/DLNA**。

啟用選項：**共享我的媒體庫**。

Kodi 現在作為 DLNA 伺服器在您的本地 Wi-Fi 網路上運行。

{{< cards cols="1">}}
{{< card subtitle="在 Kodi 中啟用 DLNA" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## 開啟 Kodi 媒體庫

按右鍵關閉設定視窗並開啟 Kodi 主媒體庫。

{{< cards cols="1">}}
{{< card title="" subtitle="按右鍵存取 Kodi 媒體庫" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## 下載 iOS 音樂串流應用程式

取得一個免費的 iOS DLNA 用戶端應用程式，讓您從各種雲端儲存服務和 DLNA 伺服器串流音樂。

- 如果您的收藏主要是 MP3 和其他標準音訊格式，請使用 **Evermusic**。
- 如果您有 FLAC、ALAC 或 DSD 等格式的高解析度音樂庫，請選擇 **Flacbox**。

兩個應用程式都可在 **iOS** 和 **macOS** 上使用，且免費。

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="下載 Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="下載 Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## 新增 DLNA 來源

下載 iOS 應用程式後，開啟**所有連接**部分。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic 應用程式主側邊欄" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

向下捲動並點選**本地網路 - 可用設備**以發現 DLNA 伺服器。
在此部分中，您將看到本地網路上所有可用的裝置。您的 **Kodi DLNA 伺服器**應該出現在這裡。點選 Kodi 伺服器進行連線。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic 中的可用 DLNA 裝置" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic 將顯示透過 Kodi 共享的媒體庫資料夾。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic 中的 Kodi 音樂庫" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

導覽至**歌曲**資料夾以檢視 DLNA 伺服器上所有可用的音訊檔案。

{{< cards cols="1">}}
{{< card title="" subtitle="來自遠端資料夾的歌曲" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

點選任何音訊檔案即可立即開始串流播放。

{{< cards cols="1">}}
{{< card title="" subtitle="在 Evermusic 中播放 MP3 檔案" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

返回**連接**部分。新增的 DLNA 伺服器現在將顯示在這裡。隨時點選其圖示重新連線。

您還可以在這裡啟用 **Last.fm 記錄**。播放統計資料將儲存到您的 Last.fm 帳戶中。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic 中的連接" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## 建立音樂庫

**Evermusic** 和 **Flacbox** 都允許您將音樂加入媒體庫，並按**中繼資料標籤**（如藝人、專輯、類型和作曲家）進行組織。

首先，開啟**音樂庫**部分。向下捲動到**工具和偏好設定**，然後點選**新增音樂**。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic 音樂庫" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

選擇音樂來源——在此選擇**連接**。

{{< cards cols="1">}}
{{< card title="" subtitle="在 Evermusic 中新增新音樂" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

在連接中找到 **Kodi DLNA 伺服器**並點選檢視資料夾和檔案。

{{< cards cols="1">}}
{{< card title="" subtitle="選擇 DLNA 伺服器匯入音樂" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

選擇要新增的資料夾或檔案，然後點選**完成**。

{{< cards cols="1">}}
{{< card title="" subtitle="選擇要新增的音樂資料夾" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

應用程式將掃描您選擇的檔案，並使用中繼資料將其組織到藝人、專輯、類型和作曲家等部分。

{{< cards cols="1">}}
{{< card title="" subtitle="帶分類的音樂庫" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## 建立播放列表

您還可以建立自己的播放列表。

首先，開啟**播放列表**標籤頁。

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic 中的播放列表標籤頁" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

點選**加號 (+)** 按鈕並選擇**新建播放列表**。

{{< cards cols="1">}}
{{< card title="" subtitle="建立新播放列表" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

輸入播放列表名稱並點選**儲存**。

{{< cards cols="1">}}
{{< card title="" subtitle="輸入播放列表名稱" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

接下來，選擇新增歌曲的來源——這裡我們選擇**媒體庫**。

{{< cards cols="1">}}
{{< card title="" subtitle="向新播放列表新增歌曲" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

選擇想要的歌曲並點選**完成**新增。

{{< cards cols="1">}}
{{< card title="" subtitle="從媒體庫新增音樂到播放列表" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

選定的曲目現在將出現在建立的播放列表中。

{{< cards cols="1">}}
{{< card title="" subtitle="建立的播放列表顯示在列表中" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

預設情況下，歌曲可用於串流播放。要離線收聽，請啟用**離線模式**——應用程式將下載所有播放列表曲目。

{{< cards cols="1">}}
{{< card title="" subtitle="播放列表已啟用離線模式" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

點選**更多操作**按鈕探索其他選項。您可以：

- 封存播放列表
- 變更專輯封面
- 重新排列曲目
- 以及更多實用功能

{{< cards cols="1">}}
{{< card title="" subtitle="更多播放列表操作可用" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## 總結

使用 **Evermusic** 和 **Flacbox**，將您的 iPhone、iPad 或 Mac 變成強大的 DLNA 音樂播放器非常簡單。

- 直接從您的 **Kodi DLNA 伺服器**串流 MP3 或高解析度 FLAC
- 建立按中繼資料分組的個人音樂庫（專輯、類型、作曲家）
- 建立和管理**自訂播放列表**
- 啟用**離線模式**以便隨時隨地收聽
- 連線到**多個雲端服務**和**本地網路裝置**
- 使用 **Last.fm 整合**追蹤您的收聽習慣

無論您是發燒友還是普通聽眾，Evermusic 和 Flacbox 都能為您提供無縫音樂串流和組織所需的一切。

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="下載 Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="下載 Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

立即開始建立您的個人音樂體驗。

## 常見問題

{{% details title="Kodi 作為 DLNA 伺服器是免費的嗎？" closed="true" %}}
是的。Kodi 完全免費且開源。可在 macOS、Windows、Linux 和許多 NAS 裝置上執行。
{{% /details %}}

{{% details title="Evermusic 和 Flacbox 是否支援透過 DLNA 串流 FLAC？" closed="true" %}}
是的。Flacbox 針對 FLAC、ALAC 和 DSD 等高解析度格式進行了最佳化。Evermusic 也支援 FLAC 播放以及 MP3 和其他標準格式。
{{% /details %}}

{{% details title="從 Kodi 串流後可以離線收聽嗎？" closed="true" %}}
可以。在任何播放列表上啟用離線模式，應用程式將把所有曲目下載到您的裝置上。
{{% /details %}}

{{% details title="使用 DLNA 需要進階訂閱嗎？" closed="true" %}}
免費版本支援最多 3 個雲端或網路連線。進階版取消此限制。
{{% /details %}}

{{% details title="我的 iPhone 需要與 Kodi 在同一個 Wi-Fi 網路上嗎？" closed="true" %}}
是的。DLNA 串流透過您的本地網路運作。Kodi 伺服器和 iOS 裝置都必須連線到同一個 Wi-Fi 網路。
{{% /details %}}

{{% details title="我可以用 NAS 代替 Mac 或 PC 使用此設定嗎？" closed="true" %}}
可以。許多 NAS 裝置（Synology、QNAP 等）支援 Kodi 或有自己內建的 DLNA 伺服器。Evermusic 和 Flacbox 可以連線到任何標準 DLNA/UPnP 伺服器。
{{% /details %}}
