---
date: 2020-01-01
title: 'Flacbox'
description: 'Learn how to use Flacbox — the hi-res FLAC, DSD, ALAC, and FFmpeg-powered cloud music player for iPhone, iPad, and Mac. Connect iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, and DLNA. Stream and download high-resolution audio, edit metadata, listen to audiobooks, scrobble to Last.fm, use Apple CarPlay and Home Screen widgets, and customize the 10-band equalizer.'
keywords: [
  "Flacbox user guide", "Flacbox how to", "hi-res music player iPhone", "FLAC player iPhone",
  "DSD player iOS", "ALAC player Mac", "lossless music app", "cloud music player iPhone",
  "offline FLAC player Mac", "music library manager", "audio tag editor",
  "CarPlay FLAC player", "Chromecast audio app", "AirPlay 2 music",
  "Flacbox widgets", "Flacbox CarPlay", "FFmpeg music player iOS",
  "audiobook player iPhone", "audio bookmarks iOS", "pitch correction music app",
  "audio output sample rate", "external DAC iPhone", "USB DAC Mac",
  "Synology music app", "QNAP music app", "NAS music player iPhone",
  "WebDAV music player", "SMB music streaming", "DLNA music player",
  "iCloud Drive music", "Google Drive FLAC", "Dropbox FLAC player",
  "Wi-Fi Drive music transfer", "M3U playlist import", "Last.fm scrobbling"
]
tags: ["flacbox", "guide", "hi-res", "FLAC", "FFmpeg", "cloud", "CarPlay", "widgets"]
aliases:
  - /post/flacbox-guide/
  - /support-flacbox/
  - /docs/guide/flacbox/flacbox-guide/
  - /post/flacbox-guideüberprüfen/
---


### Welcome to the Flacbox Guide

**Flacbox is a high-resolution music player for iPhone, iPad, and Mac** that lets you turn your favorite cloud storage, NAS, and media servers into your own personal streaming service — without limits and without subscriptions.<br><br>

Flacbox connects to a remarkably wide list of sources, all in one app:

- **Personal cloud storage:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Self-hosted servers and music-server APIs:** **Plex** · **Jellyfin** · **Emby** · **Subsonic** (and every Subsonic-compatible server — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · **Navidrome** · Nextcloud (and ownCloud via the shared API) · **Synology Drive** · **QNAP**.
- **NAS and file-share protocols:** **SMB** (SMB1, SMB2, Auto) · **WebDAV** (HTTP / HTTPS) · **FTP / FTPS** · **SFTP** (password or public-key auth) · **NFS** · **DLNA / UPnP** (playback and download). Works with Apple Time Capsule, Synology, QNAP, WD My Cloud Home, Buffalo, any Linux Samba / NFS / SSH host, or a shared folder on your Mac or Windows PC.
- **S3-compatible object storage:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, and any other S3-API endpoint.
- **Local-network discovery:** the **Available Devices** section auto-lists every Bonjour / mDNS service on your Wi-Fi — Plex, Jellyfin, Emby servers, Synology, QNAP, AirPort routers with attached drives, Time Capsule — so you can tap to connect without typing an IP address.

Where most music apps stick to Apple’s built-in audio engine, Flacbox bundles **FFmpeg** alongside the system codecs so you can play formats iOS doesn’t support out of the box — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, plus the regular MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC family. Combined with a configurable **audio output sample rate (44.1 / 48 / 64 / 88.2 / 96 kHz)**, multi-channel output (Mono → 5.1 → SDDS → ITU BS.775-1), **IO buffer tuning**, and **pitch correction**, Flacbox gives audiophiles control that most consumer music apps simply do not offer.

### Enjoy Smooth Streaming and Offline Playback

Flacbox features smart buffering for smooth streaming and a built-in **download manager** so you can pull entire Playlists, Artists, Albums, Folders, or individual tracks down to your device for offline use. When you run low on storage, clear cached files in one tap and keep streaming from the cloud. **Offline Mode** for folders, playlists, albums, and artists also auto-syncs new tracks the moment they appear in the cloud, so your offline collection always stays current.

### Automatically Organized Music Library

When you import audio tracks, Flacbox scans their metadata and organizes them into a clean Music Library — grouped by **Songs, Unplayed Songs, Albums, Album Artists, Artists, Genres, and Composers**. Use the built-in search to find anything in seconds, filter by source (online cloud / offline / device), and choose between Plain / Grouped / Tabbed library layouts. For libraries with mixed “various artists” compilations, Flacbox provides dedicated **All Albums / Exclusive Albums / Solo Albums** views to surface the right results without noise.

### Fix Metadata and Tag Your Music

If you come across corrupted tags or messy encodings (a common headache for ripped or older files), the built-in **ID3 Tags Editor** can clean them up — manually or with automatic MusicBrainz lookups. You can also normalize broken character encodings (great for Cyrillic, Japanese, or Chinese tags that came in from Windows PCs), search for missing album art, and write changes back to the original file in the cloud automatically. For deeper batch editing, install our companion app **Evertag**.

### Easy Transfers from Mac, PC, or NAS

Move music between your computer and your iPhone or iPad with any of these tools: **SMB**, **WebDAV**, **DLNA**, **Wi-Fi Drive** (drag-and-drop in any desktop browser), **iTunes / Finder File Sharing** over a Lightning or USB-C cable, **USB flash drives**, or **iXpand Flash Drives**. Have an **Apple Time Capsule, WD My Cloud Home, Synology, QNAP, Buffalo**, or any other NAS that exposes SMB / WebDAV / DLNA / FTP / SFTP? Connect it once and stream your entire library without taking up any device storage.

### Customize Your Sound with the Equalizer

Flacbox includes a **10-band equalizer** with iPod-style presets (Acoustic, Bass Booster, Classical, Dance, Rock, Pop, Jazz, and many more), a **preamplifier**, and the ability to save your own presets. Whether you’re tuning for a pair of audiophile IEMs, a HomePod mini, or a car stereo, you can shape the sound exactly the way you like it.

### Audiobook Friendly

Flacbox makes a great **audiobook player** — multiple per-track **bookmarks**, fine-grained playback speed (0.02× to 3.00×), **continue playback** to resume exactly where you stopped, customizable **skip-time buttons**, and a **sleep timer** that gently fades out at bedtime. M4B chapter markers and long files are fully supported.

### Stream Anywhere — Including Your Car and Home Screen

Stream music to **Apple TV / HomePod via AirPlay 2**, send it to **Google Chromecast** speakers and Cast-enabled TVs, and take everything on the road with **Apple CarPlay**. Use **Home Screen widgets** on iPhone and iPad to see the now-playing track at a glance, and **Last.fm scrobbling** to keep your listening history with you across apps.

### Privacy and Security

Flacbox uses only **official SDKs and OAuth-based logins** from each cloud provider — your password never reaches the app. Access tokens live encrypted in the iOS Keychain, all transfers are TLS-protected, and revoking access in your cloud account or removing Flacbox from the device deletes everything instantly. Protect your library with an optional **passcode** for an extra layer of privacy.

### Getting Started with Flacbox

This guide walks you through every part of Flacbox on iPhone, iPad, and Mac — from connecting cloud services, organizing your library, transferring files, and managing playlists, to fine-tuning the equalizer and configuring the audio engine. Use the cards below to jump straight to the section you need.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navigation" subtitle="Tab Bar on iPhone, Left Menu on iPad and Mac, mini player, widgets, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Connections" subtitle="iCloud, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Music Library" subtitle="Songs, Albums, Artists, Genres, Composers — sync, search, edit metadata." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Playlists" subtitle="Build, import M3U / M3U8 / CUE, reorder, and export to M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Local Files" subtitle="Offline music, USB drives, Wi-Fi Drive, file manager, offline folders." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Audio Player" subtitle="Hi-res output, equalizer, pitch, bookmarks, AirPlay, Chromecast, speed, sleep timer." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Settings" subtitle="Audio engine, library, file manager, CarPlay, widgets, personalization, language, backup." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="FAQ" subtitle="Find answers to the 50 most common questions about Flacbox." >}}

{{< /cards >}}
