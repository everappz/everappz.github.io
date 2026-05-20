---
title: "Flacbox 7.4: Rebuilt CarPlay, Plex, Jellyfin, Subsonic, SFTP for Hi-Res Audio"
date: 2026-05-20
description: "Flacbox 7.4 ships a CarPlay experience rebuilt from scratch and adds 10+ new ways to play your lossless library — Plex, Subsonic, Navidrome, Jellyfin, Emby, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, plus FTP, SFTP, and NFS. Includes refreshed Home Screen widgets, Liquid Glass design, and stronger network libraries for FLAC, DSD, ALAC, and APE playback on iPhone and Mac."
keywords: ["Flacbox 7.4", "Flacbox update", "CarPlay hi-res audio player", "CarPlay FLAC player iPhone", "Plex hi-res music iPhone", "Plex lossless streaming", "Jellyfin FLAC player iOS", "Emby lossless music iOS", "Subsonic FLAC iPhone", "Navidrome lossless iOS client", "Internxt FLAC streaming", "Proton Drive lossless music", "QNAP hi-res music player", "Nextcloud FLAC streaming iOS", "Amazon S3 lossless audio iPhone", "SFTP FLAC player iPhone", "FTP hi-res audio iOS", "NFS lossless streaming iPhone", "stream DSD from NAS iPhone", "DSD player iPhone 2026", "ALAC player iOS", "lossless music player iPhone", "Liquid Glass audio app", "hi-res audio player iOS 2026"]
tags: ["Flacbox", "Flacbox 7.4", "CarPlay", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Home Screen Widgets", "Liquid Glass", "Hi-Res Audio", "FLAC", "DSD", "ALAC", "What's New"]
aliases:
  - /post/flacbox-7-4-new-carplay-cloud-media-servers-hi-res/
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**TL;DR:** [Flacbox 7.4](/products/flacbox) is a major release for the iPhone and Mac hi-res audio player. CarPlay has been rebuilt from the ground up — fast sorting, multiple color themes, a fresh Now Playing screen, a full play queue at a glance, and a letter index for huge libraries. The update adds 10+ new ways to reach your music — privacy-first clouds **Internxt** and **Proton Drive**, personal servers **QNAP**, **Nextcloud**, and **Amazon S3**, the streaming servers **Plex**, **Subsonic**, **Navidrome**, **Jellyfin**, and **Emby**, plus the network protocols **FTP**, **SFTP**, and **NFS**. The interface is tuned for Apple's new **Liquid Glass** material, the underlying network libraries are stronger, and Home Screen widgets refresh more reliably.

---

## Hi everyone!

A big Flacbox update is here. We rebuilt CarPlay from scratch and added more than ten new ways to connect to your lossless library — from privacy-first cloud storage to popular self-hosted media servers and classic network protocols.

[Download Flacbox 7.4 from the App Store](https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8) or update from your existing version. Mac users can grab the [desktop version here](https://apps.apple.com/app/apple-store/id1594027432?pt=95781850&ct=everappzcom&mt=8).

## CarPlay, Rebuilt from Scratch

We redesigned **Apple CarPlay** for Flacbox from the ground up so listening on the road feels safer and easier. Every detail — from how a song is found to how playback is controlled — has been retuned for the in-car experience.

- **Fast sorting** — reach any song in moments across albums, artists, playlists, and folders without endless scrolling.
- **Color themes that fit your car** — pick a theme that matches your dashboard or your interior lighting, day or night.
- **A fresh Now Playing screen** — bigger artwork, clearer controls, and new playback actions one tap away.
- **Your full play queue at a glance** — see what is coming next without leaving the current screen.
- **Letter index for large libraries** — jump through tens of thousands of FLAC, DSD, ALAC, and APE tracks with a single touch.
- **Faster loading, no more pauses** — opening big folders, cloud directories, or media-server libraries feels instant.

If you stream lossless audio while driving — from Dropbox, Google Drive, OneDrive, iCloud Drive, [Plex](#media-servers), [Jellyfin](#media-servers), Subsonic, or any other source — the rebuilt CarPlay experience makes the whole flow feel native to the car.

## 10+ New Ways to Connect Your Music

Flacbox 7.4 expands what counts as your "music library." If your hi-res files live on a cloud you trust, a NAS at home, or a self-hosted streaming server, Flacbox now plays from it directly — no syncing, no exporting, no format conversion.

### Private Clouds: Internxt and Proton Drive

If end-to-end encryption and zero-knowledge storage matter to you, two of the most respected privacy-first clouds are now native in Flacbox:

- **Internxt** — open-source, post-quantum encrypted, GDPR-compliant Spanish cloud. Free tier available.
- **Proton Drive** — end-to-end encrypted storage from the makers of Proton Mail and Proton VPN, based in Switzerland. Free tier available with paid plans for larger libraries.

Connect once and your FLAC, DSD, or ALAC files stream through the encrypted tunnel — Flacbox never sees your data in the clear, and neither does the provider's server.

### Personal Servers: QNAP, Nextcloud, Amazon S3

For listeners running their own infrastructure:

- **QNAP** — native API connection to QNAP NAS devices for fast, reliable playback over local Wi-Fi or remote access. Stream high-bitrate FLAC and DSD directly without re-encoding.
- **Nextcloud** — connect to any self-hosted or managed Nextcloud instance. A great option if you have already moved off Google Drive or Dropbox for privacy reasons.
- **Amazon S3** — point Flacbox at any S3 bucket (or S3-compatible storage like Backblaze B2, Wasabi, MinIO, Cloudflare R2) and stream your collection directly.

### <a id="media-servers"></a>Streaming Servers: Plex, Subsonic, Navidrome, Jellyfin, Emby

This is the big one for self-hosted music fans. Flacbox 7.4 turns your iPhone or Mac into a first-class hi-res client for the most popular open-source and freemium media servers:

- **Plex** — Plex Media Server is **free** to download and run. A **Plex Pass** subscription is optional and unlocks mobile sync, hardware transcoding, and other extras. Flacbox works with both free and Plex Pass libraries.
- **Subsonic** — the original self-hosted music streaming server. The official Subsonic server is **paid** ($1/month after a 30-day trial), and Flacbox also speaks the Subsonic API to dozens of compatible servers.
- **Navidrome** — modern, lightweight, **completely free and open-source** music server written in Go. Implements the Subsonic API. Runs on a Raspberry Pi, NAS, or any Linux box. Highly recommended for lossless collections up to a few hundred thousand tracks.
- **Jellyfin** — **completely free and open-source** media server (a community fork of Emby). Handles music, movies, TV, and audiobooks. No accounts, no telemetry, no subscriptions.
- **Emby** — **freemium** media server. The core server is free; **Emby Premiere** is a one-time or yearly purchase that unlocks mobile apps, offline sync, and more. Flacbox connects to both free and Premiere libraries.

Whichever server you run, Flacbox streams your full collection — albums, artists, playlists, genres, and embedded artwork — with bit-perfect output to USB DACs, the 10-band equalizer, crossfade and gapless playback, AirPlay, Chromecast, and the rebuilt **CarPlay** experience. Your server keeps listening history; Flacbox respects it.

### New Transfer Methods: FTP, SFTP, NFS

For listeners with custom servers, home labs, or generic NAS boxes that don't ship with a polished mobile app, Flacbox 7.4 adds three classic network protocols:

- **SFTP (SSH File Transfer Protocol)** — the right answer for **secure remote streaming from your own server**. SFTP rides on top of SSH, so the entire transfer (authentication and audio data) is encrypted. If you have a VPS, dedicated server, or a Linux box at home with SSH access, you can drop a folder of FLAC or DSD on it and stream over the public internet without exposing anything else. Supports password and key-based authentication.
- **FTP** — the long-standing standard for file transfer. Useful if your **home NAS** (older Synology, ASUS, D-Link, TerraMaster, or generic boxes) exposes an FTP server but does not have a native API integration. Best used inside your local network.
- **NFS (Network File System)** — the de-facto sharing protocol on Linux and most NAS devices. NFS shares are common on home labs and small business networks; Flacbox now mounts them and streams bit-perfect audio directly. Lower overhead than SMB on the same hardware.

> **Tip:** SFTP is the protocol you want for streaming from the open internet. FTP and NFS are best inside your local network — keep them off the public internet unless you wrap them in a VPN.

## Other Improvements

### A New Look That Matches Liquid Glass

Flacbox 7.4's interface is updated for Apple's new **Liquid Glass** material across the app — translucent surfaces, smoother animations, and refined controls that fit naturally into iOS 26 and macOS 26. The library, Now Playing, equalizer, and settings screens have all been retuned for the new system aesthetic.

### Stronger Network Libraries

We refreshed the underlying libraries Flacbox uses to talk to **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, **iCloud Drive**, **MEGA**, and other services. Translation: fewer edge-case connection failures, better support for newer server versions, and improved reliability when streaming high-bitrate audio on slower or geographically distant connections.

### Fixed Playback on Some Servers

We tracked down and fixed a handful of playback issues on certain self-hosted servers — including stalls after seeking on large FLAC and DSD files, and slow start times on libraries with very long file lists. Streaming should feel cleaner end-to-end.

### New Home Screen Widgets with Better Refresh

The Home Screen widgets — Now Playing, Playback Queue, Recently Played — have been redesigned with cleaner layouts and a smarter refresh policy. They stay in sync with the app without burning extra battery, and a few new widget sizes give you more control over what is visible at a glance.

### Translation Fixes

Many small localization fixes across multiple languages based on direct user feedback. Text fits better on smaller buttons and in longer European languages (German, Dutch, French, Spanish).

### Small Polish Inspired by Your Messages

Countless small improvements based on App Store reviews and emails to support@everappz.com. We read every message.

## Why This Update Matters

Flacbox 7.4 is built around two ideas:

1. **Your hi-res music, wherever you keep it.** Whether your lossless library lives on iCloud Drive, a privacy-first cloud like Proton Drive or Internxt, a media server like Plex or Jellyfin, a NAS at home, or a Raspberry Pi running Navidrome — Flacbox now connects to it natively, with the same bit-perfect playback experience everywhere.
2. **Better in the car.** CarPlay is the screen many listeners see most, and the rebuilt experience reflects that — faster, safer, and built around the way real drivers reach for their music.

## Get Flacbox 7.4

[**Download Flacbox from the App Store**](https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8) or update from inside the App Store. The [Mac version](https://apps.apple.com/app/apple-store/id1594027432?pt=95781850&ct=everappzcom&mt=8) is available separately as a universal Mac app. Flacbox is a free download with optional in-app upgrades for advanced features. The rebuilt CarPlay, all new cloud and server connections, the refreshed Home Screen widgets, and the Liquid Glass UI are part of the base update.

If the app makes your day better, a rating on the App Store really helps. Questions or problems? Write to **support@everappz.com** and a real person will reply.

## Frequently Asked Questions

{{% details title="What's new in Flacbox 7.4?" closed="true" %}}
Flacbox 7.4 ships a fully rebuilt CarPlay experience and adds 10+ new connections — Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS. The release also brings a Liquid Glass design refresh, stronger network libraries, redesigned Home Screen widgets with smarter refresh, playback fixes on some servers, translation improvements, and many small polish items.
{{% /details %}}

{{% details title="Does Flacbox work with Plex for FLAC and lossless audio?" closed="true" %}}
Yes. Starting with Flacbox 7.4 you can connect to a Plex Media Server and stream your full hi-res library — FLAC, ALAC, WAV, AIFF, OGG, OPUS, and other lossless formats. Plex Media Server is free to run; Plex Pass is optional. Flacbox supports both free and Plex Pass setups.
{{% /details %}}

{{% details title="Is Jellyfin or Navidrome supported in Flacbox?" closed="true" %}}
Yes. Both are fully supported in Flacbox 7.4. Jellyfin is a free, open-source media server. Navidrome is a free, open-source music server that implements the Subsonic API. Flacbox connects to both natively and streams your lossless library with full metadata and artwork.
{{% /details %}}

{{% details title="Are Plex, Jellyfin, Emby, Navidrome, and Subsonic free?" closed="true" %}}
- **Plex** — server is free; Plex Pass is an optional paid upgrade.
- **Jellyfin** — completely free and open-source.
- **Emby** — server is free; Emby Premiere is paid and unlocks mobile sync and offline.
- **Navidrome** — completely free and open-source.
- **Subsonic** — official server costs $1/month after a 30-day trial, but its API is open and many free servers (including Navidrome) implement it.
{{% /details %}}

{{% details title="Can I stream FLAC and DSD from my home NAS over SFTP, FTP, or NFS?" closed="true" %}}
Yes. Flacbox 7.4 adds SFTP, FTP, and NFS as native connection types. SFTP is the recommended choice for streaming from your own server over the public internet because all traffic is encrypted via SSH. FTP and NFS are best used inside your local network or behind a VPN.
{{% /details %}}

{{% details title="How do I connect Flacbox to a custom server using SFTP?" closed="true" %}}
Open Flacbox, go to the Connections tab, choose SFTP, and enter your server's hostname or IP, port (usually 22), username, and either a password or an SSH private key. Flacbox will browse your remote folders and stream audio files directly with end-to-end encryption.
{{% /details %}}

{{% details title="Does Flacbox support Internxt and Proton Drive?" closed="true" %}}
Yes. Both privacy-focused clouds are supported as of Flacbox 7.4. They join MEGA and other privacy-first services already available in the app.
{{% /details %}}

{{% details title="Does Flacbox play DSD files from Plex, Jellyfin, or a NAS?" closed="true" %}}
Yes. Flacbox plays DSD64, DSD128, and DSD256 files (DSF and DFF containers) streamed from Plex, Jellyfin, Emby, Subsonic-compatible servers, QNAP, Nextcloud, Amazon S3, and over SFTP, FTP, and NFS. Bit-perfect output to USB DACs is supported on iPhone, iPad, and Mac.
{{% /details %}}

{{% details title="How do the redesigned CarPlay screens work?" closed="true" %}}
Flacbox's CarPlay interface has been rebuilt with fast sorting across albums, artists, playlists, and folders; multiple color themes that match different car interiors; a fresh Now Playing screen with new controls; the full play queue at a glance; a letter index for jumping through large libraries; and faster loading on big folders and cloud directories.
{{% /details %}}

{{% details title="Is Flacbox 7.4 free to update?" closed="true" %}}
Yes. Flacbox is a free download from the App Store, and 7.4 is a free update for all existing users. The rebuilt CarPlay, all new cloud and server connections, refreshed Home Screen widgets, and Liquid Glass UI are part of the base update.
{{% /details %}}

{{% details title="Which devices is Flacbox 7.4 available on?" closed="true" %}}
Flacbox 7.4 runs on iPhone, iPad, and Mac. CarPlay support requires a CarPlay-compatible vehicle or aftermarket head unit. AirPlay and Chromecast let you cast playback to a bigger system; USB DACs are supported for bit-perfect lossless output.
{{% /details %}}
