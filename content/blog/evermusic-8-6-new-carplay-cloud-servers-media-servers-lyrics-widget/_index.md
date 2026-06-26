---
title: "Evermusic 8.6: New CarPlay, Plex, Jellyfin, SFTP, Lyrics Widget"
date: 2026-05-08
description: "Evermusic 8.6 ships a fully redesigned CarPlay experience, support for Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS, a synced lyrics Home Screen widget, Wi-Fi Drive improvements, and Liquid Glass UI updates."
keywords: ["Evermusic 8.6", "Evermusic update", "CarPlay music player iPhone", "Plex music player iOS", "Jellyfin iPhone music", "Emby music player iOS", "Subsonic iOS app", "Navidrome iOS client", "Internxt music streaming", "Proton Drive music player", "QNAP music player iPhone", "Nextcloud music player iOS", "Amazon S3 music streaming", "SFTP music player iPhone", "FTP audio player iOS", "NFS music streaming iPhone", "synced lyrics widget iPhone", "Home Screen lyrics widget iOS", "Wi-Fi Drive iPhone", "Baidu Netdisk music player", "Aliyun Drive music player", "Liquid Glass design", "cloud music player iOS 2026"]
tags: ["Evermusic", "Evermusic 8.6", "CarPlay", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Lyrics Widget", "Home Screen Widgets", "Liquid Glass", "What's New"]
aliases:
  - /post/evermusic-8-6-new-carplay-cloud-servers-media-servers-lyrics-widget/
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-administrator-everappz.webp"
---

{{< author-byline >}}

**TL;DR:** [Evermusic 8.6](/products/evermusic) is a major update for iPhone, iPad, and Mac. CarPlay is rebuilt from the ground up with quick sorting, multiple color schemes, a redesigned Now Playing screen, full queue view, and a fast-scroll letter index. The release adds 10+ new connections — **Plex**, **Jellyfin**, **Emby**, **Subsonic**, **Navidrome**, **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, plus **FTP**, **SFTP**, and **NFS** protocols. A new synced **lyrics Home Screen widget** displays time-aligned lyrics while you listen. Wi-Fi Drive gets a new UI, selection mode, and a faster upload queue. The whole app is updated for **Liquid Glass** design, and streaming from Chinese servers like **Baidu Netdisk (百度网盘)** and **Aliyun Drive (阿里云盘)** is more reliable.

---

## Hello everyone!

Evermusic 8.6 is available to download. This is one of the biggest updates we've shipped: a fully redesigned CarPlay experience, more than ten new cloud and server integrations, a brand-new synced lyrics widget for the Home Screen, and a refreshed Liquid Glass interface across the app.

[Download Evermusic 8.6 from the App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) or update from your existing version.

## A Brand-New CarPlay Experience

We rebuilt Evermusic for **Apple CarPlay** from the ground up. The result is faster, smoother, and far easier to use behind the wheel.

- **Quick sorting** — find any track in seconds across albums, artists, playlists, and folders.
- **Multiple color schemes** — pick a theme that matches your dashboard or your car's interior lighting.
- **Redesigned Now Playing screen** — bigger artwork, clearer controls, and new playback actions you can trigger with one tap.
- **Full playback queue at a glance** — see what's next without leaving the current screen.
- **Fast-scroll letter index** — jump through huge libraries (10,000+ tracks) without endless scrolling.
- **Smoother content loading** — no more freezes when opening big folders, cloud directories, or media-server libraries.

If you stream music from the cloud while driving — Dropbox, Google Drive, OneDrive, iCloud Drive, [Plex](#media-servers), [Jellyfin](#media-servers), and others — the new CarPlay experience makes the whole flow feel native to the car.

## 10+ New Cloud, NAS, and Server Integrations

Evermusic 8.6 expands what counts as your "music library." If your audio lives on a cloud you trust, a NAS at home, or a self-hosted media server, Evermusic can stream from it directly — no syncing, no exporting.

### Privacy-Focused Clouds: Internxt and Proton Drive

If you care about end-to-end encryption and zero-knowledge storage, two of the most respected names in privacy-first cloud are now native in Evermusic:

- **Internxt** — open-source, post-quantum encrypted, GDPR-compliant Spanish cloud. Free tier available.
- **Proton Drive** — end-to-end encrypted storage from the makers of Proton Mail and Proton VPN, based in Switzerland. Free tier available with paid plans for larger libraries.

Connect once and your music streams through the encrypted tunnel — Evermusic never sees your data in the clear, and neither does the provider's server.

### Self-Hosted Storage: QNAP, Nextcloud, Amazon S3

For users running their own infrastructure:

- **QNAP** — native API connection to QNAP NAS devices for fast, reliable playback over local Wi-Fi or remote access.
- **Nextcloud** — connect to any self-hosted or managed Nextcloud instance. Great if you've already migrated off Google Drive or Dropbox for privacy reasons.
- **Amazon S3** — point Evermusic at any S3 bucket (or S3-compatible storage like Backblaze B2, Wasabi, MinIO, Cloudflare R2) and stream your collection directly.

### <a id="media-servers"></a>Media Servers: Plex, Subsonic, Navidrome, Jellyfin, Emby

This is the big one for self-hosted music fans. Evermusic 8.6 turns your iPhone, iPad, or Mac into a first-class client for the most popular open-source and freemium media servers:

- **Plex** — Plex Media Server is **free** to download and run. A **Plex Pass** subscription is optional and unlocks features like mobile sync, hardware transcoding, and live TV. Evermusic works with both free and Plex Pass libraries.
- **Subsonic** — the original self-hosted music streaming server. The official Subsonic server is **paid** ($1/month after a 30-day trial), but Evermusic also speaks the Subsonic API to dozens of compatible servers.
- **Navidrome** — modern, lightweight, **completely free and open-source** music server written in Go. Implements the Subsonic API. Runs on a Raspberry Pi, NAS, or any Linux box. Highly recommended for music libraries up to a few hundred thousand tracks.
- **Jellyfin** — **completely free and open-source** media server (a community fork of Emby). Handles music, movies, TV, books, and audiobooks. No accounts, no telemetry, no subscriptions.
- **Emby** — **freemium** media server. The core server is free; **Emby Premiere** is a one-time or yearly purchase that unlocks mobile apps, offline sync, Cinema Mode, and more. Evermusic connects to both free and Premiere libraries.

Whichever server you run, Evermusic streams your full library — albums, artists, playlists, genres, and embedded artwork — with offline caching, gapless and crossfade playback, the 10-band equalizer, AirPlay, Chromecast, and **CarPlay**. Your server tracks listening history; Evermusic respects it.

### New Network Protocols: FTP, SFTP, NFS

For users with custom servers, home labs, or generic NAS boxes that don't ship with a polished mobile app, Evermusic 8.6 adds three classic protocols:

- **SFTP (SSH File Transfer Protocol)** — the right answer for **secure remote streaming from your own server**. SFTP rides on top of SSH, so the entire transfer (authentication and audio data) is encrypted. If you have a VPS, dedicated server, or a Linux box at home with SSH access, you can drop a folder of music on it and stream over the public internet without exposing anything else. Supports password and key-based authentication.
- **FTP** — the long-standing standard for file transfer. Useful if your **home NAS** (older Synology, ASUS, D-Link, TerraMaster, or generic boxes) exposes an FTP server but doesn't have a native API integration. Best used inside your local network.
- **NFS (Network File System)** — the de-facto sharing protocol on Linux and most NAS devices. NFS shares are common on home labs and small business networks; Evermusic now mounts them and streams directly. Lower overhead than SMB on the same hardware.

> **Tip:** SFTP is the protocol you want for streaming from the open internet. FTP and NFS are best inside your local network — keep them off the public internet unless you wrap them in a VPN.

## Wi-Fi Drive: New UI and Faster Uploads

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) is Evermusic's built-in feature for **transferring music wirelessly from your computer to your iPhone or iPad — no iTunes, no cables, no cloud account required**. Both devices need to be on the same Wi-Fi network. You start the server on the iOS app and either:

- Open the URL in any desktop browser (Safari, Chrome, Firefox, Edge), drag your music files into the page, and they upload directly to the device, or
- Mount the device as a network share via **Mac Finder** ("Connect to Server…") or **Windows File Explorer** (Map Network Drive) using WebDAV.

It's the fastest way to move a large local music library onto your phone without any third-party service. See the [step-by-step guide here](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).

In Evermusic 8.6, Wi-Fi Drive gets:

- **A new user interface** — cleaner, easier to read at a glance.
- **Selection mode** — pick multiple files or folders and act on them in bulk.
- **Improved file upload queue** — better progress feedback and resilience to network hiccups.
- **Better overall performance** — faster transfers for large libraries.

## New Synced Lyrics Home Screen Widget

One of the most-requested features is finally here: **a synced lyrics widget you can pin to your iPhone, iPad, or Mac Home Screen**.

When you play a track that has time-aligned lyrics, the widget displays the **current line** of the song in real time — and the line advances as the music plays. Tap the widget to open Evermusic in full lyrics view.

What it does:

- Shows **synced, time-stamped lyrics** for the currently playing track.
- Updates as the song progresses — no manual refresh, no scrolling.
- Works with embedded LRC-style lyrics in your audio files and with lyrics fetched in-app.
- Available in **multiple widget sizes** so you can pick how much text fits on the Home Screen.
- Works on **iPhone**, **iPad**, and **Mac** (Home Screen and Notification Center where supported).

The widget is perfect for users who like to follow along with songs while their phone is on the desk, on a stand, or on a lock screen during a long listen. It pairs especially well with audiobooks and podcast-style content where reading along helps comprehension.

To enable it, long-press your Home Screen, tap **Edit > Add Widget**, search for **Evermusic**, and pick the **Lyrics** widget in the size you want.

## Other Improvements

### Liquid Glass Design Updates

Evermusic 8.6's interface is updated for Apple's new **Liquid Glass** material across the app — translucent surfaces, smoother animations, and refined controls that fit naturally into iOS, iPadOS, and macOS.

### Better Reliability for Chinese Servers

We invested significant work this release in playback stability for **Baidu Netdisk (百度网盘)** and **Aliyun Drive (阿里云盘)**. If you've used these services with Evermusic before, you'll notice:

- Faster directory listing on libraries with thousands of files.
- More reliable streaming on slower or geographically distant connections.
- Fewer dropped connections during long playback sessions.
- Improved retry and resume logic when the network briefly drops.

These two clouds are the most popular consumer storage services in China, and Evermusic is one of the few iOS music players with first-class native support for both.

### Updated Connection Libraries

We updated the underlying libraries Evermusic uses to talk to **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, and other services. Translation: fewer edge-case connection failures, better support for newer server versions, and improved performance overall.

### New Home Screen Widgets and Smarter Updates

Beyond the new lyrics widget, the existing Home Screen widgets — Now Playing, Playback Queue, Recently Played — have been refined with **better update logic**, so they stay in sync without burning extra battery. There are also new widget layouts for users who want more control over what's visible at a glance.

### Bug Fixes and Polish

- Fixed playback issues on certain media servers and self-hosted setups.
- Localization fixes across multiple languages.
- Many smaller improvements based on direct feedback from App Store reviews and emails to support@everappz.com.

## Why This Update Matters

Evermusic 8.6 is built around three ideas:

1. **Your music, wherever you keep it.** Whether your library lives on iCloud Drive, a privacy-first cloud like Proton Drive or Internxt, a media server like Plex or Jellyfin, a NAS at home, or a Raspberry Pi running Navidrome — Evermusic now connects to it natively, with the same playback experience everywhere.
2. **Better in the car.** CarPlay is the screen many users see most, and the rebuilt experience reflects that.
3. **Lyrics on your Home Screen.** The new synced lyrics widget brings something nobody else does well into your main glanceable surface.

## Get Evermusic 8.6

[**Download Evermusic from the App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) or update from inside the App Store. Evermusic is a free download with optional in-app upgrades for advanced features. The new CarPlay, lyrics widget, and all new server integrations are part of the base update.

If you enjoy the app, please leave a rating on the App Store — it genuinely helps. Have feedback or run into an issue? Email us at **support@everappz.com**. We read every message.

## Frequently Asked Questions

{{% details title="What's new in Evermusic 8.6?" closed="true" %}}
Evermusic 8.6 introduces a fully redesigned CarPlay experience, support for 10+ new connections (Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), a new synced lyrics Home Screen widget, Wi-Fi Drive UI improvements with selection mode, Liquid Glass design updates, better reliability for Baidu Netdisk and Aliyun Drive, and many bug fixes.
{{% /details %}}

{{% details title="Does Evermusic work with Plex?" closed="true" %}}
Yes. Starting with Evermusic 8.6, you can connect to a Plex Media Server and stream your full music library. Plex Media Server is free to run; Plex Pass is optional. Evermusic supports both free and Plex Pass setups.
{{% /details %}}

{{% details title="Is Jellyfin or Navidrome supported in Evermusic?" closed="true" %}}
Yes. Both Jellyfin and Navidrome are fully supported in Evermusic 8.6. Jellyfin is a free, open-source media server. Navidrome is a free, open-source music server that implements the Subsonic API. Evermusic connects to both natively.
{{% /details %}}

{{% details title="Are Plex, Jellyfin, Emby, Navidrome, and Subsonic free?" closed="true" %}}
- **Plex** — server is free; Plex Pass is an optional paid upgrade.
- **Jellyfin** — completely free and open-source.
- **Emby** — server is free; Emby Premiere is paid and unlocks mobile sync and offline.
- **Navidrome** — completely free and open-source.
- **Subsonic** — official server costs $1/month after a 30-day trial, but its API is open and many free servers (including Navidrome) implement it.
{{% /details %}}

{{% details title="Can I stream from my home NAS over SFTP, FTP, or NFS?" closed="true" %}}
Yes. Evermusic 8.6 adds SFTP, FTP, and NFS as native connection types. SFTP is the recommended choice for streaming from your own server over the public internet because all traffic is encrypted via SSH. FTP and NFS are best used inside your local network or behind a VPN.
{{% /details %}}

{{% details title="How do I connect Evermusic to a custom server using SFTP?" closed="true" %}}
Open Evermusic, go to the Connections tab, choose SFTP, and enter your server's hostname or IP, port (usually 22), username, and either a password or an SSH private key. Evermusic will browse your remote folders and stream audio files directly with end-to-end encryption.
{{% /details %}}

{{% details title="Does Evermusic support Internxt and Proton Drive?" closed="true" %}}
Yes. Both privacy-focused clouds are supported as of Evermusic 8.6. They join Mega and other privacy-first services already available in the app.
{{% /details %}}

{{% details title="What is Wi-Fi Drive in Evermusic?" closed="true" %}}
Wi-Fi Drive is Evermusic's built-in wireless file transfer feature. It lets you upload music from your computer to your iPhone or iPad over your local Wi-Fi network — no iTunes, no cables, no cloud account. You can use any desktop browser or a WebDAV client like Mac Finder or Windows File Explorer. See the [full Wi-Fi Drive guide](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).
{{% /details %}}

{{% details title="How does the new lyrics widget work?" closed="true" %}}
The lyrics widget shows time-synced lyrics on your iPhone, iPad, or Mac Home Screen for the currently playing track. The displayed line advances automatically as the song plays. Add it by long-pressing the Home Screen, tapping Edit > Add Widget, searching for Evermusic, and choosing the Lyrics widget.
{{% /details %}}

{{% details title="Does Evermusic 8.6 fix Baidu Netdisk and Aliyun Drive playback issues?" closed="true" %}}
Yes. We made significant reliability improvements for both 百度网盘 (Baidu Netdisk) and 阿里云盘 (Aliyun Drive), including faster directory listing, smarter retries on weak connections, and better resume behavior during long playback sessions.
{{% /details %}}

{{% details title="Is Evermusic 8.6 free to update?" closed="true" %}}
Yes. Evermusic is a free download from the App Store, and 8.6 is a free update for all existing users. The new CarPlay experience, lyrics widget, and all new server integrations are part of the base update.
{{% /details %}}

{{% details title="Which devices is Evermusic 8.6 available on?" closed="true" %}}
Evermusic 8.6 runs on iPhone, iPad, and Mac. CarPlay support requires a CarPlay-compatible vehicle or aftermarket head unit.
{{% /details %}}
