---
title: "Music Library"
date: 2020-01-01
description: "Learn how to manage your Evermusic library: add tracks, sync cloud and offline music, edit metadata, group songs by tags, and personalize your music experience."
keywords: [
  "Evermusic", "music library", "audio tags", "metadata reader", 
  "offline music", "cloud sync", "album covers", 
  "playlists", "favorites", "iTunes library"
]
tags: ["evermusic", "guide", "music", "library"]
readingTime: 11
draft: false
aliases:
  - /post/evermusic-guide-music-library/
---

## Intro

Managing your music library is a breeze with Evermusic, where you can effortlessly organize all your tracks. You have two options for building your music library: manual addition or automatic synchronization.

![Music library screen](21260c_324233656df74f219cd303f3bea91228~mv2.png)

## Manual Addition

To manually add tracks, tap on the "Add music" menu item and select folders/files from the connected cloud storage service or files located on your device. When you add tracks to the library, only links to those tracks are created, preserving the actual files in their original locations to save valuable disk space. If you want to make tracks available offline, you can use the download action from the options menu or enable offline mode for playlists and track collections.

![Add music](21260c_c716bca4d7304a1fb98f94b57f362950~mv2.png)

## Quick Access

At the top of the music library menu, you'll find a quick access section providing convenient links to your favorites, recents, and audio bookmarks.

### Favorites

You can mark songs as favorites on the audio player screen or using the options menu.

### Recents

This section displays all recently played tracks.

### Bookmarks

You can create audio bookmarks while a song is playing and manage them on this screen. Detailed instructions on working with audio bookmarks can be found [here](https://www.everappz.com/post/evermusic-guide-music-library).

## Continue Playback

Restore the audio player queue from the last saved position if this feature is enabled in application settings.

## Locations

All the tracks in your library are thoughtfully grouped by source types and music tags.

### Online music

This section showcases music from your cloud storage services.

### Files in this application

Here you can find music available for offline playback, sourced from your local files. This includes files in the app’s documents directory.

### Files on this iPhone/iPad/Mac

This category includes music imported into the application from your device added through the ‘Open files…’ system dialog.

### iTunes music

This section shows music imported into your device's iPod library. Please note that tracks from Apple Music are not available here.

## Categories

When you add tracks to your music library, the app automatically reads their audio tags and organizes them into categories such as Songs, Unplayed Songs, Albums, Album Artists, Artists, Genres, and Composers.

## Top Toolbar

Located just beneath the navigation bar, the top toolbar offers several convenient actions: "Search," "Play all," "Shuffle all," and "Continue playback." You can reveal or hide this toolbar with a simple swipe-down gesture.

![Top Toolbar](21260c_a73c980c1b0f4117991be100f4dd6193~mv2.png)

## Search

The search feature empowers you to locate a specific track, artist, album, or genre within your music library. Within the "Search screen," you have access to the following actions: "Sort," "Filter," "Grid/List."

![Music Library Search](21260c_959385148fd9449aa4f4ee9e973cd9a0~mv2.png)

## Options Menu

Each song in your music library boasts a menu with more actions, accessed by tapping the three dots button near the song title. These actions vary depending on whether it's a single song or part of a collection.

![Song Options Menu](21260c_1b50588d732248858fda0d957353df1b~mv2.png)

### For Individual Songs

- **Play next**: Adds the song to the top of the player queue.
- **Play later**: Appends the song to the bottom of the player queue.
- **Add to playlist**: Adds the song in a playlist.
- **Add to favorites**: Marks the song as a favorite for quick access.
- **Download**: Saves the song to local files. It appears in the "Local Files" tab and the "Offline music" section.
- **Edit audio tags**: Opens the built-in audio tags editor to fix missing metadata; note that this will alter the song on your storage.
- **Show in folder**: Reveals the folder where the audio file is stored.
- **Show in Finder**: For files imported from your Mac, this action reveals the folder where the audio file is located on your Mac.
- **Open in**: Exports the audio file to another app.
- **Delete from cloud service**: Removes the file from both the music library and cloud storage, and please note that this action is irreversible.
- **Delete from music library**: Deletes the song from your music library, but the file remains in storage. If automatic sync is enabled and the file exists on remote storage, it will reappear in your library after a sync operation.

### For Song Collections

For song collections like Albums, Artists, Genres, or Composers, the options menu includes the following actions.

![Songs Collection Options Menu](21260c_0ca8e39089b249a0a5e39d4b25f27a47~mv2.png)

- **Play all**: Replaces the player queue with songs from the selected collection.
- **Play next**: Adds the songs from this collection to the top of the player queue.
- **Play later**: Appends the songs from this collection to the bottom of the player queue.
- **Add to playlist**: Includes songs from this collection in a playlist, with the option to create a new playlist.
- **Enable offline mode**: Downloads songs from this collection to local files. These downloaded songs will appear in the "Local Files" tab and the "Offline music" section of your Music Library. If new items are added to the collection on the server, they will be downloaded automatically to "Local Files."
- **Edit image**: Allows you to change the album cover for the song collection.
- **Delete from music library**: Removes the song collection from your music library. However, this action does not delete the actual files from storage. If automatic sync is enabled and the files exist on remote storage, they will reappear in your library after a sync operation.

## Selection mode

You can activate selection mode using the More Actions button in the top right corner. In this mode, you can select multiple tracks and perform various actions.

![Selection mode](21260c_f821a01a30844a4799157a01d9896d41~mv2.png)

## Tags Grouping

These categories help you organize your tracks by music tags: Songs, Albums, Album Artists, Artists, Genres, Composers. When you add tracks to the music library, the app reads the tracks’ metadata and groups them by these categories. If you don’t see all your albums, ensure the app has scanned all tracks. You can check the scanning progress in **Settings -> Music Library -> Metadata Reading -> Number of Processed Files in Music Library**. For local files, you can also rescan offline folders in **Settings -> Music Library -> Offline Folders Sync -> Start Local Folders Scanning**. After the metadata reader completes all operations, you can see the following categories in your music library.

- **Songs**: All songs are grouped by the TRACK_TITLE tag. You can check the sort order using the More Actions menu in the top right corner.
- **Unplayed songs**: All songs are grouped by the TRACK_TITLE tag and not played.
- **Albums**: Songs are grouped by the ALBUM_NAME tag, while artist, album artist, and composer tags are skipped. If you have several albums with the same name but different artists, consider using the Exclusive Albums sorting described below.
- **Album Artists**: Songs are grouped by the ALBUM_ARTIST_TAG only.
- **Artists**: Songs are grouped by the ARTIST_TAG only.
- **Genres**: Songs are grouped by the GENRE tag.
- **Composers**: Songs are grouped by the COMPOSER tag.

## Album Detail

When you open the Artist, Album Artist, or Composer sections, you can see a switcher for Songs/All Albums/Exclusive Albums/Solo Albums.

![Tags Grouping](21260c_259f3120ee8646f3a8e963cf25bfe21e~mv2.png)

- **Songs**: Displays all songs where this Artist/Album Artist/Composer is set in the audio tags.
- **All Albums**: Shows compilation albums and all albums where the artist is present.
- **Exclusive Albums**: Shows albums where the specified artist is the only artist with that album name.
- **Solo Albums**: Shows albums where only the specified artist’s tracks are displayed, even if other artists have albums with the same name.

## Tools and preferences

This section shows actions which allows you to manage your library and find content quickly.

### Search

You can use this feature to quickly find any song, artist, album, or genre in your music library.

### Settings

Tap the "Settings" menu item to configure your music library preferences.

![music library settings](21260c_32a25b477f5249909a7b4e33047144f5~mv2.png)

#### Metadata Reading

When you add tracks to the library, the metadata reader gets to work. This background process reads all metadata from your tracks and organizes them by Artist, Album, Genre, and Composer. You have the flexibility to adjust the speed of metadata reading to load data faster, but be aware that this may use more energy. You can also disable the metadata reader and display file names instead of tag information.

![Metadata Synchronization](21260c_9d22c93f1e574ffc9e2b9f189fedac62~mv2.png)

Importantly, the metadata reader only updates metadata in your music library and does not alter the files stored in your cloud account or local storage. If you wish to edit metadata for audio files, you can do so using the built-in tags editor, which you can activate from the corresponding action in the options menu.

#### Available Modes for Metadata Reader

- **Deactivated**: The metadata reader will be deactivated, and file names will be shown instead of data from audio tags.
- **Current Song**: The application will read metadata only for the currently playing song. Use this option if you have a slow network connection to prevent the metadata reader from sending many requests to the cloud server, which may cause playback interruptions.
- **Playback Queue**: The app will read metadata for all songs in the audio player queue.
- **Library**: The app will read metadata for all songs in the music library.

When the **Metadata reading in the background** switch is on, the metadata reader works in background mode. However, please note that if the app consumes a lot of energy during audio playback, the iOS operating system may suspend it.

So, if you have a large music collection, it's advisable to use the desktop version of the application for metadata synchronization. You can then use the data backup and restore feature to transfer the synchronized music library from the desktop, which is available in app settings.

When the **Normalize metadata encoding** is enabled, the app will automatically normalize metadata encoding for all songs in the music library. This fixes issues where audio tags’ encoding is broken (such as after editing files on a Windows PC) and prevents incorrect information from displaying while a track is playing or added to the library.

The **Reload metadata** action will flag all files in your music library as having missing metadata, triggering the metadata reader to refresh the metadata for every file in your music library.

Tap the **Start Metadata Reading** action to start the metadata reader. The operation progress will be displayed below.

#### Online Synchronization

Automatic online music sync allows you to add tracks from connected cloud services to the music library automatically. To activate this feature, head to music library settings and select sync folders.

![Online Music Synchronization](21260c_ac7c155c66ba48ca972c80f3c0d66950~mv2.png)

With this option enabled, the application scans all selected folders, identifies supported audio files, and seamlessly integrates them into your library. You can start or stop synchronization by tapping on the corresponding menu action.

![synchronized online filders selection screen](21260c_cd8c111c7ab640e5be6f15e775f7259c~mv2.png)

Online music synchronization operates exclusively when the app is in the foreground, which means synchronization may take some time. To speed up the process, leave your app open, connect it to a power source, and enable **Screen -> Always active** option in application settings.

Alternatively, you can perform online music synchronization on the desktop version of the app and transfer the music library to the iOS version using the data backup restore feature.

You can also set how often you want to synchronize your online music library. If you set it to "Immediately," online sync will start every time you open the application.

![online synchronization time interval](21260c_30f554b0d0a3473ba7628539ce26ace8~mv2.png)

#### Offline Synchronization

Here you can configure offline music synchronization.

![Offline Music Synchronization](21260c_f6b45dbcf5cc4dd282857d348d946003~mv2.png)

##### Synchronized Offline Folders

When you make a cloud folder available offline (via the More Actions menu), it will appear in the **Local Files → Offline Folders** section. The app will download its contents to your device. If you make changes to the folder in the cloud—like adding, removing, or updating files—the app will detect those changes and update the local copy automatically.

![Synchronized Offline Folders](21260c_d4e0b5f422894598a3ab2f1eaafe7657~mv2.png)

On this screen, you can manually start offline folder synchronization, show the offline folder in its enclosing folder, and disable offline mode for this folder. Disabling offline mode will remove all local copies of files from your device.

##### Time Interval

You can set the time interval for how often the app should check offline folders for modifications.

##### Start Local Folders Scanning

This option scans all local folders located in the application’s Documents directory to find supported audio files. All these local files are seamlessly added to your music library. Local files located on your device but outside of this application must be added to the music library manually, as the app does not have access to files outside the application Documents directory due to iOS/MacOS security restrictions.

##### Important

It is advisable to periodically initiate offline music synchronization to keep your music library updated with your local files.

#### Personalization

In this section, you can configure the music library screen style to suit your preferences. Three options are available: Plain menu, Grouped menu, Tabbed menu.

![Personalization](21260c_468417e440b846a59af908d5101901b6~mv2.png)

#### Album Covers

Here, you can choose the quality of album covers stored on your device and manage your cached album covers. By default, the app will check for embedded album covers in your tracks and display them if available. If there are no embedded album artworks and the ‘Search in the folder’ option is enabled, the app will check the enclosing folder for JPEG or PNG images and use them as album artwork for all tracks in that folder.

![Album Covers Settings Screen](21260c_bafa8d6fb0a4465ba696af582c0074aa~mv2.png)

#### Playlists

You can enable the option to add the same song to a playlist twice. By default, this option is disabled.

![Playlists Settings](21260c_8f67546ed47245169983fcea35d5af3f~mv2.png)

#### Recents

You can manage your recently played songs list.

![Recents](21260c_0a400318ca3c45dfb10659b151430bb9~mv2.png)

- **Delete List**: You can delete the entire list of recently played songs.
- **Change List Size**: You can set the number of items that should appear in the list.
- **Export Songs List**: Use this action to export your recently played songs list in different formats: M3U, CSV, or TXT. Detailed instructions are available on our website [here](https://www.everappz.com/post/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt).

![Export Songs List](21260c_eace98a1cc344e7299377aba42f18512~mv2.png)

#### Favorites

You can manage the list of your favorite songs.

- **Simultaneous Editing**: Enable this option to add a song to the favorites list in both the music library and the files section simultaneously.
- **Delete List**: You can delete the entire list of favorite songs.
- **Export Songs List**: Similar to the Recents section, you can export the list of your favorite tracks in different formats: M3U, CSV, or TXT.

![Favorites](21260c_64e95955fadf4605930ac98e9bafa0f3~mv2.png)

#### Delete music library

This action will erase the music library database, but it will leave your music files untouched.

#### Content loading limit

By default, the application uses pagination to reduce content loading time. However, you can disable this option and allow the application to load all available data at once. To do so, open application settings, scroll down to "Personalization" -> "Content loading limit" and choose "Deactivated".

#### Main Menu Style

You can configure the Media Library menu style. Available options are Plain Menu and Grouped Menu. To change this, open Settings, then go to Personalization, and select Main Menu Style.

![Main Menu Style](21260c_77c203b0361e41eb86d7694959cb2852~mv2.png)