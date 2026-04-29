---
title: "從Evermusic和Flacbox匯出完整收聽記錄到Last.fm"
date: 2024-01-30
description: "了解如何從Evermusic和Flacbox匯出音樂記錄，並使用CSV檔案和Windows版Last.fm Scrubbler工具上傳到Last.fm。"
keywords: ["evermusic", "flacbox", "lastfm", "音樂記錄", "scrobbling", "匯出曲目", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "最近使用的", "lastfm", "匯出", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**摘要：** 將您的收聽記錄從Evermusic或Flacbox匯出為CSV檔案，然後使用Windows上的免費工具Last.fm-Scrubbler-WPF上傳到Last.fm。兩個應用程式都原生支援自動scrobble功能。

**更新：** 自動scrobble功能現已推出！在此了解更多：[/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling是一種簡單的方式，可以自動將您正在播放的歌曲的基本資訊（如標題和藝術家）儲存到線上服務中。之後，您可以檢視自己的收聽記錄。

[Last.fm](https://www.last.fm/home)由名為Audioscrobbler的音樂推薦系統驅動，免費提供此服務。它透過記錄您收聽的曲目（無論是來自網路電台、您的電腦還是各種可攜式音樂裝置）來建立您音樂品味的詳細檔案。您可以稍後造訪該網站，取得與您音樂品味相符的新藝術家或專輯推薦。

您可以使用免費工具將收聽記錄從Evermusic和Flacbox應用程式上傳到[Last.fm](http://Last.fm)，我們將向您說明具體操作方法。

開啟應用程式的「音樂資料庫」部分，捲動到「快速存取」部分。點選「最近使用的」選單項目。

![音樂資料庫畫面](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

在「最近使用的」畫面上，點選右上角的「更多」按鈕以啟動「更多操作」選單。點選「匯出歌曲清單」選單項目。

![最近使用的畫面](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

在「選擇檔案格式」畫面上，您可以選擇目標檔案的格式。可用選項 - CSV、TXT、M3U。

![選擇檔案格式畫面](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV：即逗號分隔值（Comma-Separated Values），非常適合將資料整理成整齊的表格格式。在目標檔案中，您將找到藝術家名稱、專輯名稱、曲目名稱、時間戳記（您收聽曲目的時間）、專輯藝術家名稱和曲目時長等參數。

TXT：這是一個純文字檔案。簡單直接，參數包括藝術家名稱、專輯名稱、曲目名稱和時長。

M3U：這種格式是建立播放清單的首選。它很棒，因為您可以匯出歌曲清單並在任何裝置上欣賞您的曲目，即使您沒有原始檔案（前提是您選擇媒體檔案的絕對URL選項）。在輸出檔案中，您將找到時長、藝術家名稱、曲目名稱和媒體檔案位置等參數。

對於我們的任務，選擇CSV是正確的選擇。我們將使用此檔案配合免費軟體Last.fm-Scrubbler-WPF將收聽記錄上傳到[Last.fm](http://Last.fm)服務。只需選擇CSV並點選「匯出」按鈕。

![匯出完成畫面](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

匯出完成後，只需點選「顯示檔案」按鈕，應用程式將在您的文件資料夾中顯示建立的檔案。然後，點選檔案名稱旁邊的「更多操作」按鈕，從選單中選擇「開啟方式」選項。下一步是將匯出的檔案複製到您的桌上型電腦。您可以透過從「開啟方式」選單中選擇AirDrop選項輕鬆完成此操作。

![匯出檔案的更多操作](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

接下來，我們將使用一個免費的開源[Last.FM](http://Last.FM)用戶端，該用戶端僅在Windows平台上可用。此用戶端允許您使用我們剛匯出的CSV檔案高效地更新[Last.FM](http://Last.FM)上的收聽記錄。

如果您目前沒有使用Windows電腦，不用擔心。您可以透過在Mac上安裝VirtualBox並使用官方Windows開發環境映像檔來存取此用戶端。

以下是您需要做的：

- 從以下連結安裝VirtualBox：[下載VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- 從此連結下載並安裝Windows開發環境：[Windows開發環境](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

在您的Windows電腦上（或帶有Windows Development映像的VirtualBox應用程式中）下載並安裝[Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - GitHub上可用的免費開源軟體。我們在1.28版本上進行了測試，您可以在此處下載：[https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Last.fm-Scrubbler-WPF下載頁面](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

在「Assets」部分點選[Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip)下載安裝壓縮檔。解壓縮下載的檔案並開啟解壓縮後的資料夾。

- 重要提示

此應用程式仍處於測試版。應用程式建立者沒有進行大量測試。他們建議先嘗試scrobble到測試帳戶，看看您想要scrobble的內容是否正確。特別是如果您一次scrobble大量曲目。請謹慎使用您的帳戶。

執行 Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

在應用程式的主畫面上，只需點選左下角的「未登入」以啟動「新增帳戶」畫面。

![新增帳戶畫面](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

輸入您的登入憑證。

![輸入登入憑證畫面](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

點選「Login」按鈕新增您的帳戶。

![點選Login按鈕新增您的帳戶。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

開啟「File Parse Scrobbler」標籤頁，開始從Evermusic應用程式匯入CSV檔案。

![開啟File Parse Scrobbler標籤頁，開始從Evermusic應用程式匯入CSV檔案。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

選擇「Parser: CSV」並點選「Settings」按鈕。

在下一個畫面上，您可以選擇CSV檔案中參數的順序。

各個欄位可以用引號括起來，如果欄位包含任何設定的分隔符號，則必須用引號括起來。例如：

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

因此保留所有預設設定，您唯一需要更改的是啟用「Has Fields Enclosed In Quotes」欄位中的核取方塊。

點選「Save & Close」套用變更。

![選擇CSV檔案中參數的順序。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

檔案解析scrobbling有兩種模式。可以透過「Scrobbling Mode」下拉方塊更改。

一般模式：在此模式下，曲目將使用解析的scrobble時間戳記進行scrobble。只有14天內的scrobble才能被scrobble。

匯入模式：在此模式下，曲目將使用從「Finish Time」和每個曲目之間選定的時長計算出的時間戳記進行scrobble。這允許即使解析的scrobble時間戳記超過14天也能scrobble曲目。因此，CSV檔案中的第一個（最上面的）曲目將使用「Finish Time」進行scrobble。

在「File:」欄位中選擇之前從Evermusic應用程式產生的CSV檔案，然後點選「Parse」。在某些情況下，您可能會看到錯誤提示，說某些scrobble無法解析。如果您有一些缺少完整中繼資料（如藝術家名稱）的曲目，這是正常的。

![某些scrobble無法解析](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

點選「Check All」按鈕選擇所有已解析的曲目。

![點選Check All按鈕選擇所有已解析的曲目。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

點選「Preview」按鈕檢查將要傳送到伺服器的所有變更。

![點選Preview按鈕檢查將要傳送到伺服器的所有變更。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

點選「Scrobble」按鈕將所有變更上傳到伺服器。

![點選Scrobble按鈕將所有變更上傳到伺服器。](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

之前Last.fm-Scrubbler-WPF沒有每日scrobble限制。現在已經改變了，因為一些人使用Scrubbler scrobble了太多曲目，導致Last.fm頁面出現問題。目前scrobble限制為每天2800次。當您嘗試scrobble超過此數量時，將收到錯誤訊息。計畫新增「scrobble佇列」功能，這樣如果您需要scrobble超過2800個曲目，它們將被新增到佇列中，過一段時間後自動scrobble。您可以在使用者選擇檢視中查看剩餘的scrobble次數。

當所有記錄成功上傳到伺服器後，您將在應用程式視窗底部看到確認訊息：'Successfully scrobbled selected tracks.'

![Successfully scrobbled selected tracks.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

現在您可以在[Last.fm](http://Last.fm)頁面上開啟您的個人資料並檢查所有變更。

![您在Last.fm頁面上的個人資料](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## 常見問題

{{% details title="我可以不匯出CSV檔案而自動scrobble嗎？" closed="true" %}}
可以。Evermusic和Flacbox現在都支援自動Last.fm scrobble。請參閱指南：[如何Scrobble到Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)。
{{% /details %}}

{{% details title="如果我的CSV中有超過14天的曲目怎麼辦？" closed="true" %}}
在Last.fm-Scrubbler-WPF中使用匯入模式。它從Finish Time重新計算時間戳記，允許您不受原始日期限制地scrobble曲目。
{{% /details %}}

{{% details title="我沒有Windows電腦。我還能使用Last.fm-Scrubbler嗎？" closed="true" %}}
可以。在Mac上安裝VirtualBox並從Microsoft下載免費的Windows開發環境映像。在虛擬機器中執行Last.fm-Scrubbler-WPF。
{{% /details %}}

{{% details title="為什麼某些scrobble沒有被解析？" closed="true" %}}
缺少必要中繼資料（如藝術家名稱）的曲目無法被解析。這是正常的，不會影響檔案中的其他曲目。
{{% /details %}}

{{% details title="有每日scrobble限制嗎？" closed="true" %}}
有。Last.fm-Scrubbler-WPF允許每天最多2,800次scrobble。如果您需要scrobble更多，請將過程分散到多天進行。
{{% /details %}}
