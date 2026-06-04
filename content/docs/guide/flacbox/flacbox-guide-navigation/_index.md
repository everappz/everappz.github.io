---
title: "Navigation"
date: 2020-02-01
aliases:
  - /post/flacbox-guide-navigation/
  - /guide-flacbox-navigation/
description: "Learn how to navigate the Flacbox interface on iPhone, iPad, and Mac. Covers the Music Library, Playlists, Local Files, Connections, Settings, the mini player and full-screen player, the top toolbar, context menu, Home Screen widgets, Apple CarPlay, and VoiceOver accessibility."
keywords: [
  "Flacbox navigation", "Flacbox interface", "music player UI", "mini player iOS Mac",
  "file manager music app", "cloud music folders", "audio library tabs",
  "continue playback Flacbox", "VoiceOver music app", "Flacbox accessibility",
  "Flacbox widgets iPhone", "Flacbox widgets iPad", "Flacbox lock screen widget",
  "Flacbox CarPlay", "Apple CarPlay music app", "wireless CarPlay FLAC",
  "Flacbox mini player Mac"
]
tags: ["guide", "flacbox", "navigation", "widgets", "CarPlay"]
readingTime: 5
---


Flacbox offers an intuitive user interface that closely resembles the native Music app, but adds a true built-in file manager so you can edit audio files, organize them into folders, and seamlessly move them to and from cloud storage and your device — without leaving the app.

Flacbox’s functionality is thoughtfully split into two logical halves: the Music Library, surfaced through the Music Library and Playlists tabs, and the Files section, surfaced through the Connections and Local Files tabs. The Music Library treats tracks as metadata-aware media items (with artist / album / genre / composer hierarchies), while the Files section gives you full file-and-folder control over the raw audio files behind those items.

## Sections

Whether you’re using an iPhone, iPad, or the compact window mode on a Mac, all app features are reachable from the tab bar at the bottom of the screen. On iPad and Mac, the same menu is available on the left sidebar so you can keep more of the screen for content. This thoughtful organization categorizes every feature into clearly named sections, ensuring a user-friendly experience whether you’re browsing a 50-track library or a 50,000-track one.

- **Connections** — connect cloud storage services such as Google Drive, MEGA, OneDrive, Dropbox, Box, pCloud, Yandex Disk, Synology Drive, and many more, plus your own computer or NAS over SMB, WebDAV, or DLNA.
- **Music Library** — neatly displays every track in your library, grouped by Artist, Album Artist, Album, Genre, Composer, Songs, and Unplayed Songs, plus dedicated sections for Recents, Favorites, and Bookmarks. You can add songs manually or have them appear automatically via online sync.
- **Playlists** — manage all of your playlists in one place: create, rename, edit cover art, reorder songs, enable offline mode, import M3U / M3U8 / CUE files, export to M3U / CSV / TXT, and add songs to the player queue.
- **Local Files** — find and manage downloaded files, with full control over the transfer queue. To open the transfer queue, tap the spinning-arrows icon in the top-left corner of the Local Files screen. The Local Files screen is split into Files in This Application (the app’s sandboxed Documents directory) and Files on This iPhone / iPad / Mac (other folders on your device, accessed via Apple’s system file picker).
- **Settings** — modify application settings, including audio engine and codecs, equalizer, music library sync, file transfers, album artwork cache, Home Screen widgets, CarPlay, user interface, language, passcode, and backup & restore.
- **Quick Access** — jump to your favorite and recently played tracks and files. On Mac and iPad, Quick Access has its own dedicated section; on iPhone, you’ll find it at the top of the Local Files, Connections, and Music Library screens.

## Mini Player on iPhone

Tap the mini player bar at the bottom of the iPhone screen to expand it into the full-screen player, and swipe down to collapse it again. On iPad and Mac the mini player lives at the top of the window and can be hidden when you open the full-screen player from the main menu. The mini player shows the current artwork, title, artist, and basic transport controls, so you never have to leave whatever you’re browsing just to pause or skip a track.

## Mini Player Window (Mac Exclusive)

On macOS, you can shrink Flacbox into a compact always-on-top mini player that floats above your other apps — perfect for keeping the now-playing track visible while you work.

1. Move your cursor to the bottom-right edge of the Flacbox window and resize it down to its smallest size.
2. Tap the **collapse button** (the downward arrow) to switch into the mini player window.
3. To keep it on top of every other app, choose Window → Show Window Always On Top from the macOS menu bar.

This is great for listening to audio lectures, podcasts, or audiobooks while you read or write — Flacbox stays out of the way but always one click from your transport controls.

## More Actions

Virtually every content item on the screen has a **More Actions** button (the “⋯” three-dots icon). Tap it to open a context-sensitive menu with every action available for that item — play next, play later, add to library or playlist, edit tags, download, share, rename, move, and so on. Long lists scroll vertically so you can reach less-common actions without crowding the main UI.

## Top Toolbar

The top toolbar, situated just beneath the navigation bar, provides quick access to the most common per-screen actions. You can show or hide it with a simple swipe-down gesture.

- **Search** — start a search within the current screen (folder, playlist, album, artist, genre, library, or queue).
- **Continue Playback** — Flacbox can restore the audio player’s state for the current directory, album, artist, or playlist from the last saved position. This option only appears if Save Audio Player State is enabled in Settings → Audio Player → General.
- **Play All** — adds every track from the current page to the player queue, preserving the current sort order.
- **Shuffle All** — adds every track from the current page to the player queue, shuffled. Great for rediscovering an old album or a huge artist catalog.

## Context Menu

The context menu provides quick access to additional options and actions for seamless interaction across devices.

### Context Menu on iOS / iPadOS

Tap and Hold on cells, the mini player, or the compact player to reveal the context menu. You can change the context menu presentation style in Settings → Personalization → Context Menu Style.

### Context Menu on macOS

Right-click on cells, the mini player, or the compact player to show the context menu. Right-click also works on the album artwork in the full-screen player.

## Home Screen Widgets (iPhone & iPad)

Flacbox supports iOS Home Screen and Lock Screen widgets so you can see the now-playing track at a glance.

1. Make sure **Widgets** are enabled in **Settings → Widgets → Enable Widgets** (widget updates use a small amount of energy, so the toggle is off by default).
2. Long-press an empty area of your **Home Screen** or **Lock Screen**.
3. Tap the **+** button in the top corner and search for **Flacbox**.
4. Pick a widget size and tap **Add Widget**.

The widget shows the current artwork, track title, and artist, and lets you tap directly through to the full-screen player. Widgets also work on **macOS** in the Notification Center.

## Apple CarPlay

Flacbox fully supports Apple CarPlay, with a streamlined interface designed for safe in-car use. Connect your iPhone over a Lightning / USB-C cable or wireless CarPlay, and the Flacbox icon will appear on your CarPlay home screen. The CarPlay UI includes dedicated tabs for Library, Connections, Local Files, and Settings, so you have full control over your entire music collection — cloud, offline, or local — without picking up your phone.

You can fine-tune the CarPlay layout in Settings → CarPlay — sort options, pagination, the menu icons gradient color, whether album art is shown, and an option to automatically pause playback the moment you connect to CarPlay (handy to avoid sudden loud audio).

## Accessibility

Flacbox is fully accessible with **VoiceOver**: every component has a descriptive label and a sensible accessibility hint. When VoiceOver is active, the app automatically switches to **Text Mode** — image-heavy decorative elements are hidden and only meaningful controls are surfaced, improving navigation speed and clarity for screen-reader users. You can also enable Text Mode manually in Settings → Accessibility → Text Mode.

### Adjusting Sliders with VoiceOver

1. **Select the slider** — swipe left or right until VoiceOver announces it.
2. **Adjust the value** — double-tap and hold the slider, then drag up or down to change the value quickly. VoiceOver will announce each new value as you go.

### Adjusting Track Position in a Playlist with VoiceOver

1. Open a playlist and tap the **More** button.
2. Select **Change Songs Order**. The list switches into editing mode.
3. Tap the reorder indicator icon near the track title to give it focus.
4. **Double-tap** the reorder indicator. On the second tap, do not release your finger — hold it until you hear a sound indicating the cell is ready to be moved.
5. You can now move the cell to its new position.

Other components work as expected, using system-provided VoiceOver patterns.
