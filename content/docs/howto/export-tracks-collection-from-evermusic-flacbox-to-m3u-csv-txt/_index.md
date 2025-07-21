---
title: "How to Export Tracks Collection to M3U, CSV, and TXT in Evermusic & Flacbox"
date: 2024-01-31
description: "Learn how to export your recents, favorites, playlists, and albums from Evermusic and Flacbox to M3U, CSV, or TXT formats. Perfect for Last.fm scrobbling and playback on other devices."
keywords: ["evermusic export", "flacbox export", "export to m3u", "export playlist to csv", "m3u txt csv playlist", "music export"]
tags: ["evermusic", "recents", "favorites", "export", "m3u", "playlist", "csv", "txt", "album"]
draft: false
aliases:
  - /post/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/
  - /amp/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/
---

## Intro

Exporting your recents, favorites, albums, and playlists from the app to an external file can be incredibly useful. You can use these files to update your listening history on scrobbler services such as [Last.fm](http://Last.fm) or listen to your playlists on external devices. With Evermusic and Flacbox, this process is easy. Here, we'll show you how to export your recents to CSV/TXT and your playlists to M3U. However, this functionality is available for any tracks collection within the app.

## Choose Format

To export your recents open the 'Music library' section and select 'Recents' menu item.

![music library](21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

On the next screen tap 'More' button in the top right corner and choose 'Export songs list'.

![export recents](21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

On the 'Select file format' screen you have several options - CSV, TXT, M3U.

- CSV

This stands for Comma-Separated Values, perfect for organizing your data into a neat table format. In the destination file, you'll find parameters like Artist Name, Album Name, Track Name, Timestamp (the time you listened to the tracks), Album Artist Name, and Track Duration. You can use that file later to update your listening history on scrobbler services such as [Last.fm](http://Last.fm) as described [here](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Here, we're talking about a plain text file. It's simple and straightforward, with parameters including Artist Name, Album Name, Track Name, and Duration. Useful if you just need a list of tracks in a text presentation.

- M3U

This format is essentially the go-to for creating playlists. It's great because you can export your song list and enjoy your tracks on any device, even if you don't have the original files (if you select the absolute URL for the media files option export). In the output file, you'll find parameters such as Duration, Artist Name, Track Name, and Media File Location.

## CSV Format

Now, let's select CSV and see what we'll receive. Simply choose CSV and hit the 'Export' button.

![select file format](21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Once the export is completed, you will see an alert with two options. Tapping 'Show file' will reveal the resulting file in your documents directory.

![export completed](21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Now you can send that file, open it in an external text editor, or use it to update your listening progress on [Last.fm](http://Last.fm).

![export folder with result files](21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

The output CSV file will contain fields in the following format:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

For example:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![exported csv file](21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## TXT Format

The output TXT file will contain fields in the following format:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

For example:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![exported txt file](21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## M3U Format

Next, we'll guide you through exporting your playlist to M3U format, which is the de facto standard for playlist files. The main precondition for successful playlist export is that all files in the playlist must be located on the same storage, whether it's in a cloud service like your Google Drive, local files, or files on your device. To begin the export process, open any playlist and tap the 'More' button in the top right corner, then choose the 'Export songs list' menu item.

![playlist screen](21260c_1371229150d54151ba525addf7e59448~mv2.png)

On the next screen, select the 'M3U' file format, where you'll encounter two options for 'Media file location type':

![select export file format screen](21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. If you choose 'Relative path', the playlist will be created with media file locations written relative to the playlist file. For example:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   In this case, avoid changing the M3U file location after export completion, as doing so will break the paths for media files. To begin playback of your playlist, simply tap on the exported playlist file, and the app will automatically locate the media files on your storage and initiate playback. Or even you can export your playlists to the storage and then import them again on your new device.

2. If you choose 'Absolute URL', the app will generate direct URLs for your media files. This allows you to play the playlist on any device/application without needing all media files to be located on the same storage as the playlist file. This option is supported only for cloud storage capable of generating direct file URLs. However, keep in mind that in some cases, the generated URLs may have a limited lifetime and can expire after some time. Here's the list of supported cloud services: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (if in guest mode)  

The output media file URL will be something like:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Once you've selected the 'Media file location type', tap 'Export'. The app will prompt you to choose a destination folder for exporting the M3U file. Tap 'Done' to confirm your selection.

![select a folder](21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

The app will generate an M3U file and upload/move it to the destination folder.

![uploading m3u file](21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Once the export is completed, a system alert will appear with the option to 'Show file'.

![export completed alert](21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Tapping on this will reveal the exported file in the app.

![exported m3u file in files list](21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

If you selected 'Relative path' as the 'Media file location type' in the previous step, the output file will be in the following format:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![m3u example with relative paths](21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

For the 'Absolute URL' option the app will generate an M3U file in the format:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![m3u example with absolute files urls](21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

You can open that file on any device/application that supports M3U playlists.

![m3u playlist opened in external app](21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Final Thoughts

Exporting your tracks from Evermusic and Flacbox gives you complete control over your music data. Whether you’re backing up your listening history, scrobbling to Last.fm, or enjoying playlists on external devices, these export options: M3U, CSV, and TXT - are powerful tools tailored for flexibility and compatibility. Take advantage of these features to enhance how you organize, share, and revisit your music collection across platforms.