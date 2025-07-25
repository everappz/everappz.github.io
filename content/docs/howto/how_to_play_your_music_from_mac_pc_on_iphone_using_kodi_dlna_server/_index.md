---
title: "How to play your music from Mac / PC / Linux / NAS on iPhone using Kodi DLNA server"
date: 2025-07-25
description: "Stream music from your computer or NAS to your iPhone over Wi-Fi using Kodi DLNA and the Evermusic app."
keywords: ["kodi dlna server", "stream music to iphone", "play music from nas", "evermusic dlna", "mac to iphone music", "windows to iphone music", "kodi dlna iphone", "dlna audio streaming"]
tags: ["dlna", "kodi", "evermusic", "iphone", "music streaming", "mac", "nas", "linux", "local network"]
readingTime: 5
draft: false
---

## Introduction

If you have a **Mac, Windows PC, Linux machine, or NAS device**, you can easily transform it into a **personal music server** at home using [Kodi](https://kodi.tv/), a free and open-source media platform. With Kodi's built-in **DLNA/UPnP server**, you can stream your entire music library to any DLNA-compatible client — including your iPhone or iPad.

In this guide, we’ll show you step-by-step how to:

- Install Kodi on your Mac or PC  
- Set up your music folders for sharing  
- Enable the DLNA music server  
- Access that music using the **Evermusic** or **Flacbox** iOS app

This setup is 100% free — no subscriptions, just your own music streamed over your Wi-Fi network. Whether you're trying to organize your large MP3 collection, listen to FLAC over Wi-Fi, or just enjoy your local music without syncing via iTunes, this setup is perfect for you.

## Download and Install Kodi on Your Mac / PC / Linux / NAS

First, visit the official Kodi website:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Kodi main website" image="/1_kodi_main_page.webp" >}}
{{< /cards >}}

Click on **Downloads** and scroll to find the version for your computer.
Choose your operating system. In this example, we'll use **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Kodi Downloads page" image="/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Click **Intel (x86/64)** if you have Intel Mac or **Apple Silicon** for M1, M2, M3 Mac to start download.

{{< cards cols="1">}}
{{< card subtitle="Choose macOS installer" image="/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Please wait a moment while the installer downloads.

{{< cards cols="1">}}
{{< card subtitle="Kodi downloaded" image="/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Once downloaded, locate the `.dmg` file in your **Downloads** folder.

{{< cards cols="1">}}
{{< card subtitle="Install Kodi" image="/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Double-click the downloaded file to launch the installer.
Drag Kodi into your **Applications** folder to install.

{{< cards cols="1">}}
{{< card title="" subtitle="Install Kodi by dragging it to Applications" image="/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Launch Kodi. You might need to allow it in **System Preferences → Security & Privacy → Open Anyway**.

{{< cards cols="1">}}
{{< card subtitle="Kodi main screen" image="/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Add Music to Kodi Library

Click the **gear icon** (Settings) from the home screen.

{{< cards cols="1">}}
{{< card subtitle="Kodi settings" image="/8_kodi_settings.webp" >}}
{{< /cards >}}

Navigate to **Media Settings → Library**. Enable **Update library on startup** for Video library and Music library for automatic indexing.

{{< cards cols="1">}}
{{< card subtitle="Library settings" image="/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Then go to the **Music** section and click **Add Music**.

{{< cards cols="1">}}
{{< card subtitle="Add Music Folder" image="/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Browse and select the folder where your music is stored.

{{< cards cols="1">}}
{{< card subtitle="Choose music source" image="/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Add music source to Kodi.

{{< cards cols="1">}}
{{< card subtitle="Add music source" image="/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Confirm and let Kodi scan your music library.

{{< cards cols="1">}}
{{< card subtitle="Confirm music sources" image="/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Wait a moment while your library is being scanned and fully built.

{{< cards cols="1">}}
{{< card subtitle="Scanning music library" image="/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Enable Kodi’s DLNA Server

Go to **Settings → Services → UPnP/DLNA**.

Enable the option: **Share my libraries**.

Kodi now acts as a DLNA server on your local Wi-Fi network.

{{< cards cols="1">}}
{{< card subtitle="Kodi enable DLNA" image="/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Open Kodi Library

Right-click to close the settings window and open the Kodi main library.

{{< cards cols="1">}}
{{< card title="" subtitle="Right-click to access Kodi library" image="/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Download Music Streaming App for iOS

Get a free iOS DLNA client app that lets you stream music from a wide range of cloud storage services and DLNA servers.

- Use **Evermusic** if your collection is mostly MP3 and other standard audio formats.
- Choose **Flacbox** if you have a hi-res music library in formats like FLAC, ALAC, or DSD.

Both apps are available for **iOS** and **macOS**, and free to use.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Download Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Download Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Add DLNA Source

Once you’ve downloaded the iOS app, open the **All Connections** section.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic app main sidebar" image="/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Scroll down and tap **Local Network - Available Devices** to discover DLNA servers.
In this section, you’ll see all available devices on your local network. Your **Kodi DLNA server** should appear here. Tap the Kodi server to connect. 

{{< cards cols="1">}}
{{< card title="" subtitle="Available DLNA devices in Evermusic" image="/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic will display the library folders shared through Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Kodi music library on Evermusic" image="/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Navigate to the **Songs** folder to view all available audio files on your DLNA server.

{{< cards cols="1">}}
{{< card title="" subtitle="Songs listed from remote folder" image="/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Tap any audio file to start streaming instantly.

{{< cards cols="1">}}
{{< card title="" subtitle="MP3 file playing in Evermusic" image="/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Return to the **Connections** section. The added DLNA server will now appear here. Tap its icon to reconnect anytime. You can also connect other cloud services from this screen using the same steps.

You can enable **Last.fm scrobbling** here as well. Playback statistics will be saved to your Last.fm account, providing personalized music recommendations later.

{{< cards cols="1">}}
{{< card title="" subtitle="Connections in Evermusic" image="/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Build Music Library

Both **Evermusic** and **Flacbox** let you add music to your library and organize it by **metadata tags** such as artists, albums, genres, and composers.

To start, open the **Music Library** section. Scroll down to **Tools and Preferences** and tap **Add Music**.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic music library" image="/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Select the music source — in this case, choose **Connections**.

{{< cards cols="1">}}
{{< card title="" subtitle="Add new music in Evermusic" image="/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Find the **Kodi DLNA server** in the Connections and tap to view folders and files.

{{< cards cols="1">}}
{{< card title="" subtitle="Choose DLNA server to import music" image="/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Choose the folders or files you want to add and tap **Done**.

{{< cards cols="1">}}
{{< card title="" subtitle="Select music folder to add" image="/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

The app will scan your selected files and organize them using metadata into sections like Artists, Albums, Genres, and Composers.

{{< cards cols="1">}}
{{< card title="" subtitle="Music library with categories" image="/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Create Playlists

You can also create your own playlists.

First, open the **Playlists** tab.

{{< cards cols="1">}}
{{< card title="" subtitle="Playlists tab in Evermusic" image="/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Tap the **plus (+)** button and choose **New Playlist**.

{{< cards cols="1">}}
{{< card title="" subtitle="Create a new playlist" image="/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Enter a name for your playlist and tap **Save**.

{{< cards cols="1">}}
{{< card title="" subtitle="Enter playlist name" image="/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Next, choose a source to add songs from — here, we select the **Library**.

{{< cards cols="1">}}
{{< card title="" subtitle="Add songs to new playlist" image="/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Select the songs you want and tap **Done** to add them.

{{< cards cols="1">}}
{{< card title="" subtitle="Add music from library to playlist" image="/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Your selected tracks will now appear in the created playlist.

{{< cards cols="1">}}
{{< card title="" subtitle="Created playlist shown in list" image="/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

By default, songs are available for streaming. To listen offline, enable **Offline Mode** — the app will download all playlist tracks.

{{< cards cols="1">}}
{{< card title="" subtitle="Offline mode enabled for playlist" image="/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Tap the **More Actions** button to explore additional options. You can:

- Archive the playlist  
- Change the album cover  
- Reorder tracks  
- And more helpful features

{{< cards cols="1">}}
{{< card title="" subtitle="More playlist actions available" image="/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Conclusion

With **Evermusic** and **Flacbox**, turning your iPhone, iPad, or Mac into a powerful DLNA music player is easy. Whether you store your music in the cloud, on a NAS, or on a home media server like **Kodi**, these apps let you stream, organize, and enjoy your collection without limits.

- Stream MP3 or hi-res FLAC directly from your **Kodi DLNA server**  
- Build a personal music library grouped by metadata (albums, genres, composers)  
- Create and manage **custom playlists**  
- Enable **offline mode** for on-the-go listening  
- Connect to **multiple cloud services** and **local network devices**  
- Track your listening habits with **Last.fm integration**

Whether you're an audiophile or a casual listener, Evermusic and Flacbox offer everything you need for seamless music streaming and organization.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Download Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Download Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Start building your personal music experience today.