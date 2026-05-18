---
title: "Evervideo 1.7: New Plex, Jellyfin, Cloud Streaming, Playback Gestures"
date: 2026-05-18
description: "Evervideo 1.7 adds 10+ new connections — Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS — plus new playback gestures (double tap to seek, tap and hold for 2x speed), a refreshed Wi-Fi Drive with batch upload, and Liquid Glass UI updates for iPhone, iPad, and Mac."
keywords: ["Evervideo 1.7", "Evervideo update", "HD video player iPhone", "Plex video player iOS", "Jellyfin iPhone video", "Emby video player iOS", "Subsonic video iOS", "Navidrome video iOS", "Internxt video streaming", "Proton Drive video player", "QNAP video player iPhone", "Nextcloud video player iOS", "Amazon S3 video streaming", "SFTP video player iPhone", "FTP video player iOS", "NFS video streaming iPhone", "stream video from NAS iPhone", "MKV player iPhone", "video player gestures iOS", "double tap to seek video", "Wi-Fi Drive video transfer iPhone", "Liquid Glass design", "cloud video player iOS 2026", "stream movies from cloud iPhone"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Playback Gestures", "Liquid Glass", "What's New"]
aliases:
  - /post/evervideo-1-7-new-cloud-media-servers-playback-gestures-wifi-drive/
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**TL;DR:** [Evervideo 1.7](/products/evervideo) is a major update for the iPhone, iPad, and Mac HD video player. The release adds 10+ new cloud, NAS, and media-server connections — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, plus the most popular media servers **Plex**, **Subsonic**, **Navidrome**, **Jellyfin**, and **Emby**, and three network protocols: **FTP**, **SFTP**, and **NFS**. New **playback gestures** let you double tap to jump forward or backward, tap and hold to run at 2x, and single tap to toggle controls — all without leaving full-screen. Wi-Fi Drive gets a refreshed UI with selection mode and a smarter upload queue. The entire app is tuned for Apple's new **Liquid Glass** design.

---

## Hello everyone!

A big Evervideo update is here. This is one of the biggest releases we've shipped: **10+ new cloud, server, and network connections**, brand-new **playback gestures** for faster control in full-screen, a refreshed **Wi-Fi Drive** experience, and a UI tuned for **Liquid Glass** across iPhone, iPad, and Mac.

[Download Evervideo 1.7 from the App Store](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) or update from your existing version. Mac users can grab the [desktop version here](https://apps.apple.com/app/evervideo/id6743504109).

## 10+ New Cloud, NAS, and Media-Server Connections

Evervideo 1.7 expands what counts as your "video library." If your movies, shows, or recordings live on a cloud you trust, a NAS at home, or a self-hosted media server, Evervideo can now stream from it directly — no downloads, no conversions, no re-encoding.

### Privacy-Focused Cloud Storage: Internxt and Proton Drive

If you care about end-to-end encryption and zero-knowledge storage, two of the most respected privacy-first clouds are now native in Evervideo:

- **Internxt** — open-source, post-quantum encrypted, GDPR-compliant Spanish cloud. Free tier available.
- **Proton Drive** — end-to-end encrypted storage from the makers of Proton Mail and Proton VPN, based in Switzerland. Free tier available with paid plans for larger libraries.

Connect once and your videos stream through the encrypted tunnel — Evervideo never sees your data in the clear, and neither does the provider's server.

### Self-Hosted Storage: QNAP, Nextcloud, Amazon S3

For users running their own infrastructure:

- **QNAP** — native API connection to QNAP NAS devices for fast, reliable video playback over local Wi-Fi or remote access. Stream 4K MKV files directly without re-encoding.
- **Nextcloud** — connect to any self-hosted or managed Nextcloud instance. Great if you've already migrated off Google Drive or Dropbox for privacy reasons.
- **Amazon S3** — point Evervideo at any S3 bucket (or S3-compatible storage like Backblaze B2, Wasabi, MinIO, Cloudflare R2) and stream your collection directly.

### <a id="media-servers"></a>Media Servers: Plex, Subsonic, Navidrome, Jellyfin, Emby

This is the big one for self-hosted video fans. Evervideo 1.7 turns your iPhone, iPad, or Mac into a first-class client for the most popular open-source and freemium media servers:

- **Plex** — Plex Media Server is **free** to download and run, with optional **Plex Pass** subscription for features like mobile sync, hardware transcoding, and live TV. Evervideo works with both free and Plex Pass libraries — stream your full movie and TV collection.
- **Subsonic** — the original self-hosted streaming server. The official Subsonic server is **paid** ($1/month after a 30-day trial), and Evervideo also speaks the Subsonic API to compatible video servers.
- **Navidrome** — modern, lightweight, **completely free and open-source** server. Implements the Subsonic API. Runs on a Raspberry Pi, NAS, or any Linux box.
- **Jellyfin** — **completely free and open-source** media server (a community fork of Emby). Handles movies, TV, music, books, and home video. No accounts, no telemetry, no subscriptions. The go-to choice for users who want self-hosted streaming without commercial strings attached.
- **Emby** — **freemium** media server. The core server is free; **Emby Premiere** is a one-time or yearly purchase that unlocks mobile apps, offline sync, Cinema Mode, and more. Evervideo connects to both free and Premiere libraries.

Whichever server you run, Evervideo streams your full library — movies, shows, home videos, and embedded subtitle tracks — with the video equalizer, 360° support, Picture-in-Picture, AirPlay, and Chromecast.

### New Network Protocols: FTP, SFTP, NFS

For users with custom servers, home labs, or generic NAS boxes that don't ship with a polished mobile app, Evervideo 1.7 adds three classic protocols:

- **SFTP (SSH File Transfer Protocol)** — the right answer for **secure remote video streaming from your own server**. SFTP rides on top of SSH, so the entire transfer (authentication and video data) is encrypted. If you have a VPS, dedicated server, or a Linux box at home with SSH access, you can drop a folder of videos on it and stream over the public internet without exposing anything else. Supports password and key-based authentication.
- **FTP** — the long-standing standard for file transfer. Useful if your **home NAS** (older Synology, ASUS, D-Link, TerraMaster, or generic boxes) exposes an FTP server but doesn't have a native API integration. Best used inside your local network.
- **NFS (Network File System)** — the de-facto sharing protocol on Linux and most NAS devices. NFS shares are common on home labs and small business networks; Evervideo now mounts them and streams 4K and HD video with low overhead.

> **Tip:** SFTP is the protocol you want for streaming over the open internet. FTP and NFS are best inside your local network — keep them off the public internet unless you wrap them in a VPN.

## New Playback Gestures

Watching videos in full-screen should feel effortless. Evervideo 1.7 introduces a clean set of tap gestures that let you control playback without exposing the on-screen controls — perfect for movies, lectures, or anything you want to watch uninterrupted.

### Double Tap — Jump Forward or Backward

Double tap the **right side** of the screen to **skip forward** by a configurable number of seconds. Double tap the **left side** to **jump back**. You can change the interval (default: 10 seconds) in **Settings → Playback → Gesture Skip Interval** — pick anything from 5 seconds (for fine seeking) to 60 seconds (for skipping intros).

This is the gesture YouTube and Netflix users will recognize instantly, and it's now native in Evervideo for any video, on any source.

### Tap and Hold — Temporary 2x Speed

Press and hold anywhere on the screen to **temporarily speed up playback to 2x**. Release to return to normal speed. Perfect for:

- Skipping through slow scenes without committing to a permanent speed change.
- Quickly scanning through lectures, tutorials, or podcasts to find the relevant section.
- Sampling movies before you commit to watching the full version.

The hold gesture doesn't change your saved playback speed — let go and you're back where you started.

### Single Tap — Show / Hide Controls

A single tap on the screen toggles the playback controls (play, pause, seek bar, subtitles, equalizer). Tap once to bring them up, tap again to hide them. Combined with double tap and hold, this means you can spend almost an entire movie in clean full-screen mode and still seek, pause, and speed-scan whenever you need to.

## Wi-Fi Drive: New UI and Faster Uploads

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) is Evervideo's built-in feature for **transferring videos wirelessly from your computer to your iPhone or iPad — no iTunes, no cables, no cloud account required**. Both devices need to be on the same Wi-Fi network. You start the server on the iOS app and either:

- Open the URL in any desktop browser (Safari, Chrome, Firefox, Edge), drag your video files into the page, and they upload directly to the device, or
- Mount the device as a network share via **Mac Finder** ("Connect to Server…") or **Windows File Explorer** (Map Network Drive) using WebDAV.

It's the fastest way to move a large local video collection onto your phone or tablet without any third-party service. See the [step-by-step guide here](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).

In Evervideo 1.7, Wi-Fi Drive gets:

- **Redesigned user interface** — cleaner, easier to read at a glance, and updated for Liquid Glass.
- **New selection mode for batch actions** — pick multiple files or folders and act on them in bulk (delete, move, copy).
- **Improved file upload queue** — better progress feedback and resilience to network hiccups so a flaky Wi-Fi connection no longer ruins a 30 GB transfer.
- **Better overall transfer performance** — measurably faster uploads for large libraries, especially for 4K MKV files and movie collections.

## Other Improvements

### Liquid Glass Design Updates

Evervideo 1.7's interface is updated for Apple's new **Liquid Glass** material across the app — translucent surfaces, smoother animations, and refined controls that fit naturally into iOS 26, iPadOS 26, and macOS 26. Now Playing, the file browser, and the settings screens have all been retuned to match the new system aesthetic.

### Updated Connection Libraries

We refreshed the underlying libraries Evervideo uses to talk to **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, **iCloud Drive**, **MEGA**, and other services. The result: fewer edge-case connection failures, better support for newer server versions, and improved reliability when streaming video on slower or geographically distant connections.

### Playback Bug Fixes

- Fixed playback issues on certain self-hosted servers where streams would stall after seeking on large MKV files.
- Better resume behavior when the network briefly drops mid-playback.
- Smoother subtitle synchronization on long-form content.

### Localization Fixes

Translation fixes across multiple languages based on direct user feedback. Better text fitting on smaller buttons and longer European languages (German, Dutch, French).

### Smaller Refinements Inspired by Your Feedback

Many smaller improvements based on App Store reviews and emails to support@everappz.com. We read every message.

## Why This Update Matters

Evervideo 1.7 is built around three ideas:

1. **Your videos, wherever you keep them.** Whether your library lives on iCloud Drive, a privacy-first cloud like Proton Drive or Internxt, a media server like Plex or Jellyfin, a NAS at home, or a Raspberry Pi running Navidrome — Evervideo now connects to it natively, with the same playback experience everywhere.
2. **Full-screen video that feels effortless.** The new tap gestures (double tap, tap and hold, single tap) bring the kind of fluid control that streaming apps like YouTube and Netflix have trained users to expect, applied to *your* video collection.
3. **Faster transfers from your computer.** A refreshed Wi-Fi Drive with batch selection and a smarter upload queue makes moving large 4K movie collections onto your iPhone or iPad genuinely fast — no cables, no iTunes, no compression.

## Get Evervideo 1.7

[**Download Evervideo from the App Store**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) or update from inside the App Store. The [Mac version](https://apps.apple.com/app/evervideo/id6743504109) is available separately as a universal Mac app. Evervideo is a free download with optional in-app upgrades for advanced features. The new cloud connections, media-server support, playback gestures, Wi-Fi Drive improvements, and Liquid Glass UI are part of the base update.

If you enjoy the app, please leave a rating on the App Store — it genuinely helps. Have feedback or run into an issue? Email us at **support@everappz.com**. We read every message.

## Frequently Asked Questions

{{% details title="What's new in Evervideo 1.7?" closed="true" %}}
Evervideo 1.7 introduces support for 10+ new connections (Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), new playback gestures (double tap to seek, tap and hold for 2x speed, single tap to toggle controls), a redesigned Wi-Fi Drive with selection mode and a smarter upload queue, Liquid Glass design updates, updated connection libraries, and many bug fixes.
{{% /details %}}

{{% details title="Does Evervideo work with Plex?" closed="true" %}}
Yes. Starting with Evervideo 1.7, you can connect to a Plex Media Server and stream your full video library — movies, TV shows, and home videos. Plex Media Server is free to run; Plex Pass is optional. Evervideo supports both free and Plex Pass setups, including direct play of MKV, MP4, AVI, MOV, and other formats without re-encoding.
{{% /details %}}

{{% details title="Is Jellyfin or Navidrome supported in Evervideo?" closed="true" %}}
Yes. Both Jellyfin and Navidrome are fully supported in Evervideo 1.7. Jellyfin is a free, open-source media server that handles video and audio. Navidrome is a free, open-source server that implements the Subsonic API. Evervideo connects to both natively.
{{% /details %}}

{{% details title="Are Plex, Jellyfin, Emby, Navidrome, and Subsonic free?" closed="true" %}}
- **Plex** — server is free; Plex Pass is an optional paid upgrade.
- **Jellyfin** — completely free and open-source.
- **Emby** — server is free; Emby Premiere is paid and unlocks mobile sync and offline.
- **Navidrome** — completely free and open-source.
- **Subsonic** — official server costs $1/month after a 30-day trial, but its API is open and many free servers (including Navidrome) implement it.
{{% /details %}}

{{% details title="Can I stream from my home NAS over SFTP, FTP, or NFS?" closed="true" %}}
Yes. Evervideo 1.7 adds SFTP, FTP, and NFS as native connection types. SFTP is the recommended choice for streaming from your own server over the public internet because all traffic is encrypted via SSH. FTP and NFS are best used inside your local network or behind a VPN.
{{% /details %}}

{{% details title="How do I connect Evervideo to a custom server using SFTP?" closed="true" %}}
Open Evervideo, go to the Connections tab, choose SFTP, and enter your server's hostname or IP, port (usually 22), username, and either a password or an SSH private key. Evervideo will browse your remote folders and stream video files directly with end-to-end encryption.
{{% /details %}}

{{% details title="Does Evervideo support Internxt and Proton Drive?" closed="true" %}}
Yes. Both privacy-focused clouds are supported as of Evervideo 1.7. They join MEGA and other privacy-first services already available in the app.
{{% /details %}}

{{% details title="How do the new playback gestures work?" closed="true" %}}
In full-screen video playback, **double tap the right side** to jump forward and **double tap the left side** to jump back by a configurable interval (default 10 seconds — change it in Settings). **Tap and hold** anywhere on the screen to temporarily speed up to 2x; release to return to normal. **Single tap** anywhere to toggle the playback controls (show or hide).
{{% /details %}}

{{% details title="Can I change the double-tap skip interval?" closed="true" %}}
Yes. Go to **Settings → Playback → Gesture Skip Interval** and pick a value between 5 and 60 seconds. Most users keep it at 10 or 15 seconds.
{{% /details %}}

{{% details title="What is Wi-Fi Drive in Evervideo?" closed="true" %}}
Wi-Fi Drive is Evervideo's built-in wireless file transfer feature. It lets you upload videos from your computer to your iPhone or iPad over your local Wi-Fi network — no iTunes, no cables, no cloud account. You can use any desktop browser or a WebDAV client like Mac Finder or Windows File Explorer. See the [full Wi-Fi Drive guide](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).
{{% /details %}}

{{% details title="Does Evervideo play MKV, AVI, and other formats from Plex or Jellyfin?" closed="true" %}}
Yes. Evervideo plays virtually every video format — MKV, AVI, MP4, MOV, FLV, WMV, WEBM, M4V, TS, 3GP — and streams them directly from Plex, Jellyfin, Emby, and other media servers without requiring transcoding for most codecs. This means lower CPU load on your server and faster start times.
{{% /details %}}

{{% details title="Is Evervideo 1.7 free to update?" closed="true" %}}
Yes. Evervideo is a free download from the App Store, and 1.7 is a free update for all existing users. The new cloud integrations, media-server support, playback gestures, Wi-Fi Drive improvements, and Liquid Glass UI are part of the base update.
{{% /details %}}

{{% details title="Which devices is Evervideo 1.7 available on?" closed="true" %}}
Evervideo 1.7 runs on iPhone, iPad, and Mac. AirPlay and Chromecast let you cast playback to a bigger screen. iCloud Drive sync keeps your library and settings consistent across devices.
{{% /details %}}
