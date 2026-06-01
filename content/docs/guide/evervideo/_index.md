---
date: 2020-01-01
lastmod: 2026-06-01
title: 'Evervideo'
description: 'Learn how to use Evervideo — the all-in-one cloud video player for iPhone, iPad, and Mac. Stream and download videos from iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, NFS, FTP / SFTP, DLNA, and S3 — plus Plex, Jellyfin, Emby, Subsonic, and Navidrome. Picture-in-Picture, primary and secondary subtitles, audio and video equalizers, RTSP IP camera streams, Chromecast, AirPlay 2, hardware H.264 / HEVC decoding, Photos and Apple Music library integration, and a compact always-on-top player.'
keywords: [
  "Evervideo guide", "Evervideo how to", "cloud video player iPhone", "video player Mac",
  "MKV player iOS", "FFmpeg video player", "HEVC video player iPhone",
  "Picture-in-Picture video iPhone", "PiP video player iPad",
  "RTSP player iPhone", "IP camera viewer", "DLNA video player",
  "Plex client iPhone", "Jellyfin client iOS", "Emby client iPad",
  "subtitle player iOS", "SRT VTT ASS subtitles", "secondary subtitles iPhone",
  "video equalizer iOS", "audio equalizer video player", "external DAC video",
  "stream video from Google Drive", "stream video from Dropbox",
  "stream video from OneDrive", "stream video from iCloud Drive",
  "stream video from MEGA", "stream video from NAS",
  "Chromecast video iPhone", "AirPlay 2 video", "iCloud video player",
  "Photos library video player", "Apple Music video player",
  "Wi-Fi Drive video transfer", "M3U video playlist",
  "Evervideo Premium", "Family Sharing video app"
]
tags: ["evervideo", "guide", "video player", "PiP", "subtitles", "RTSP", "cloud", "FFmpeg"]
aliases:
  - /post/evervideo-guide/
  - /support-evervideo/
  - /docs/guide/evervideo/evervideo-guide/
---


### Welcome to the Evervideo Guide

**Evervideo is a full-featured cloud media player for iPhone, iPad, and Mac** that turns any cloud storage account, NAS, or media server into your personal media library — without subscription fees, without re-uploading anything, and without giving up control of your files.<br><br>

Built on a custom **FFmpeg-based player engine** with **hardware-accelerated H.264 and HEVC decoding**, Evervideo plays virtually any modern container and codec — MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS, and the long tail of FFmpeg formats — at full quality, with smart buffering for smooth streaming over Wi-Fi or cellular. **Picture-in-Picture** keeps your video on top of every other app, the **compact always-on-screen player** lets you keep watching while browsing your library, and **Chromecast and AirPlay 2** send playback to your TV, HomePod, or speaker setup with one tap.

Evervideo connects to a remarkably wide list of sources, all from one app:

- **Personal cloud storage:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Self-hosted media servers and content-server APIs:** **Plex** · **Jellyfin** · **Emby** · **Subsonic** · **Navidrome** · Nextcloud (and ownCloud via the shared API) · **Synology Drive** · **QNAP**.
- **NAS and file-share protocols:** **SMB** (SMB1, SMB2, Auto) · **WebDAV** (HTTP / HTTPS) · **FTP / FTPS** · **SFTP** (password or public-key auth) · **NFS** · **DLNA / UPnP**.
- **Live and IP-camera streams:** **RTSP** — point Evervideo at any RTSP URL (`rtsp://camera-ip/stream`) and it just plays.
- **S3-compatible object storage:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, and any other S3-API endpoint.
- **On-device sources:** the iOS **Photos library** (All Videos, Short / Medium / Long, Screen Recordings, plus your Photo Albums), the iOS **Music app library** (Albums, Genres, Playlists), USB / SD card drives, and Local Files.

### One Player for Every Format and Codec

Where most iOS apps stop at H.264 / H.265 inside MP4 / MOV, Evervideo bundles **FFmpeg** alongside Apple's system codecs so you can play formats the system doesn't recognize — MKV containers, VP9, AV1, MPEG-2, OGG, Vorbis, and many more — and switches between **hardware H.264 / HEVC decoding** and software decoding automatically based on the file and the device.<br><br>

You can pick the **video track** (multi-stream Blu-ray rips), the **audio track** (commentary tracks, alternate dubs), and **two subtitle tracks at once** (great for language learners). External **SRT, VTT, and ASS / SSA** subtitle files load with one tap; advanced ASS / SSA styling is rendered correctly thanks to bundled **libass**.

### Smart Subtitles and Multi-Track Support

- **Primary and secondary subtitle tracks** rendered simultaneously — perfect for language learning.
- **External subtitle files** (`.srt`, `.vtt`, `.ass`, `.ssa`) loaded from anywhere on your device or from the cloud.
- **libass** for fully styled ASS / SSA rendering.
- **Per-track and global font selection** for both primary and secondary subtitles.
- **Audio track selection** — pick the dub, commentary, or director's track.
- **Video track selection** — for multi-angle or multi-version files.

### Dial in the Picture and the Sound

Two equalizers, side by side: an **audio equalizer** for tuning bass and treble (with import / export of custom presets), and a **video equalizer** for tweaking brightness, contrast, saturation, and hue (again with import / export). Both engines also expose audiophile-grade controls — **audio output sample rate, channel count, IO buffer duration,** and **mixed mode** — for users with external DACs and home-theater receivers.

### Cast, AirPlay, and Picture-in-Picture

- **Picture-in-Picture (PiP)** on iPhone and iPad — keep watching while you use other apps.
- **AirPlay 2** — send video to Apple TV, HomePod, or any AirPlay 2 speaker / TV.
- **Google Chromecast** — cast directly to a Chromecast or Cast-enabled TV.
- **Compact player** — a persistent mini player on top of every screen so you can browse your library without losing the video.

### Privacy and Security

Evervideo uses **official SDKs and OAuth-based logins** from every cloud provider — your password never reaches the app. Access tokens live encrypted in the iOS **Keychain**, every transfer is TLS-protected, and revoking access from your cloud account (or removing Evervideo from the device) deletes everything instantly. Protect your library with an optional **4-digit passcode** for an extra layer of privacy.

### Getting Started with Evervideo

This guide walks you through every part of Evervideo on iPhone, iPad, and Mac — from connecting cloud services, browsing your library, downloading and transferring files, managing playlists, to fine-tuning the media player, equalizers, subtitles, and Picture-in-Picture. Use the cards below to jump straight to the section you need.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="Navigation" subtitle="Tab Bar on iPhone, Left Menu on iPad and Mac, compact always-on-screen media player, Recents-first launch." >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="Files" subtitle="One unified tab for cloud (iCloud, Google Drive, Dropbox, OneDrive, MEGA, Synology, QNAP, Plex, Jellyfin, Emby), NAS (SMB, WebDAV, NFS, FTP, SFTP, DLNA), RTSP streams, local files, USB drives, and the transfers queue." >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="Media Library" subtitle="Browse by Albums, Genres, Recents, Favorites — plus the iOS Photos library and Apple Music library." >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="Playlists" subtitle="Build playlists from cloud, local, Photos, or Music library — import M3U / M3U8 / CUE." >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="Media Player" subtitle="Picture-in-Picture, audio and video tracks, primary and secondary subtitles, audio + video equalizers, AirPlay, Chromecast." >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="Settings" subtitle="Audio engine, video decoder, subtitles, library, file manager, widgets, personalization, language, backup." >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="FAQ" subtitle="Find answers to the most common questions about Evervideo." >}}

{{< /cards >}}
