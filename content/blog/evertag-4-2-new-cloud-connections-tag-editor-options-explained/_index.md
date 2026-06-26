---
title: "Evertag 4.2: New Cloud Connections, Tag Editor Settings Explained"
date: 2026-05-09
description: "Evertag 4.2 adds Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP and NFS connections, refreshes Wi-Fi Drive, and updates the UI for Liquid Glass. This post also explains every tag editor setting — including ID3v2.4 vs ID3v2.3, album cover scaling, duplicate tags, cloud upload modes, and the right options for Spotify and other streaming services."
keywords: ["Evertag 4.2", "Evertag update", "ID3 tag editor iPhone", "ID3v2.4 vs ID3v2.3", "edit FLAC tags iOS", "edit MP3 tags iPhone", "edit album artwork iOS", "tag editor for Spotify", "tag editor Plex", "tag editor Apple Music", "Evertag cloud tag editor", "Internxt tag editor", "Proton Drive tag editor", "QNAP tag editor", "Nextcloud tag editor", "Amazon S3 tag editor", "SFTP tag editor iPhone", "FTP audio tag editor", "NFS tag editor iPhone", "Wi-Fi Drive tag editor", "duplicate ID3 tags", "album cover scaling", "Liquid Glass design", "audio metadata editor iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Tag Editor", "ID3", "ID3v2.4", "ID3v2.3", "FLAC tags", "MP3 tags", "Album Artwork", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "What's New"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**TL;DR:** [Evertag 4.2](/products/evertag) is a major update for the iPhone, iPad, and Mac audio tag editor. We squashed key tag editing bugs and added 6+ new cloud and server connections — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, plus **FTP**, **SFTP** and **NFS** protocols. Wi-Fi Drive got a refreshed UI, multi-select mode, smarter upload queue, and faster transfers. The whole app is tuned for **Liquid Glass** design. This post also goes deep into Evertag's tag editor settings — explaining **ID3v2.4 vs ID3v2.3**, **album cover scaling**, **duplicate tags**, **cloud upload modes**, **delete downloaded file**, and exactly which options to pick if you're preparing audio for **Spotify**, **Apple Music**, **Plex**, **Jellyfin**, or any other streaming service.

---

## Hey everyone!

A big Evertag update is here. We've squashed key tag editing bugs and added **6+ new cloud and server connections** to make managing your audio metadata easier than ever — whether your library lives on a privacy-first cloud, a self-hosted NAS, or a generic FTP/SFTP/NFS server.

[Download Evertag 4.2 from the App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) or update from your existing version.

## Expanded Cloud and Server Support

Evertag now connects natively to a wider range of cloud and self-hosted storage options. You can edit ID3, MP4, FLAC, OGG, and APE tags on files that live anywhere.

### Privacy-First Cloud Storage: Internxt and Proton Drive

If you care about end-to-end encryption and zero-knowledge storage, two of the most respected privacy-first clouds are now native in Evertag:

- **Internxt** — open-source, post-quantum encrypted, GDPR-compliant Spanish cloud. Free tier available.
- **Proton Drive** — end-to-end encrypted storage from the makers of Proton Mail and Proton VPN, based in Switzerland. Free tier available with paid plans for larger libraries.

You can now edit metadata on audio files stored in either service directly — the file stays encrypted in transit, and only the new tags get written back.

### Self-Hosted Solutions: QNAP, Nextcloud, Amazon S3

For users running their own infrastructure:

- **QNAP** — native API connection to QNAP NAS devices. Edit tags on files stored on your QNAP via local Wi-Fi or remote access.
- **Nextcloud** — connect to any self-hosted or managed Nextcloud instance.
- **Amazon S3** — point Evertag at any S3 bucket (or S3-compatible storage like Backblaze B2, Wasabi, MinIO, Cloudflare R2) and edit metadata in place.

### New Network Protocols: FTP, SFTP, NFS

Evertag 4.2 adds three classic protocols for users with custom servers, home labs, or generic NAS boxes:

- **SFTP (SSH File Transfer Protocol)** — the right answer for **secure remote tag editing on your own server**. SFTP rides on top of SSH, so the entire transfer (authentication and audio data) is encrypted. If you have a VPS, dedicated server, or a Linux box at home with SSH access, you can edit tags on remote files without exposing anything else. Supports password and key-based authentication.
- **FTP** — the long-standing standard for file transfer. Useful for older home NAS devices that expose FTP but don't have a native API.
- **NFS (Network File System)** — the de-facto sharing protocol on Linux and most NAS devices. Lower overhead than SMB on the same hardware.

> **Tip:** SFTP is the protocol you want for remote editing over the open internet. FTP and NFS are best inside your local network — keep them off the public internet unless you wrap them in a VPN.

## Wi-Fi Drive Upgrades

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) is Evertag's built-in feature for transferring audio files wirelessly between your computer and your iPhone or iPad — no iTunes, no cables, no cloud account required. Both devices need to be on the same Wi-Fi network.

In Evertag 4.2, Wi-Fi Drive gets:

- **Refreshed, modern interface** — cleaner, easier to read at a glance, and updated for Liquid Glass.
- **Multi-select mode** — pick multiple files or folders and act on them in bulk.
- **Smarter file upload queue** — better progress feedback and resilience to network hiccups.
- **Improved speed and overall reliability** — faster transfers for large libraries.

This is the fastest way to move a batch of audio files from your computer onto your phone, edit their tags, and move them back — all without any third-party service.

## Tag Editor Settings: A Deep Dive

This is the part most users never read — and the part that decides whether your tags work everywhere or only in some apps. Open Evertag, then go to the **audio tags editor settings** section. Here's what each option actually does, and which option to pick depending on what you're trying to achieve.

### Album Cover Scaling

When you save album artwork into an audio file, Evertag can scale the image down before embedding it. The available options are:

- **Small** — smallest file size impact, lower image quality.
- **Medium** — balanced choice for most users.
- **Large** — high quality, suitable for big-screen players and CarPlay.
- **Extra Large** — very high quality, noticeable file size increase.
- **Original (Deactivated)** — embed the artwork at its original resolution. **No scaling at all.**

**Why this matters:**

- **Higher quality = larger file size.** A 3,000 × 3,000 pixel cover can easily add several MB to every track. Multiply that across an album and the disk-space hit adds up fast.
- **Some audio players don't handle very large embedded images well.** Older devices, certain car head units, and some legacy desktop players can choke on covers above ~1,500 px or refuse to display them.
- **For most cloud and streaming workflows**, **Medium** or **Large** is the sweet spot. Use **Original** only when you specifically need archival quality or are preparing files for a player you trust to handle it.

> The **Original** size option is part of Evertag's premium personalization upgrade. Standard sizes (Small/Medium/Large/Extra Large) are free.

### Tag Saving Options: ID3v2.4 vs ID3v2.3

This is the single most important setting for compatibility. ID3v2 is the metadata format used inside MP3 files. There are two widely-used versions, and they differ in subtle but important ways.

#### ID3v2.4

- Newer, supports **UTF-8 text encoding** — proper handling of non-Latin scripts (Chinese, Russian, Japanese, Arabic, Hebrew, etc.).
- More frame types (relative volume, equalizer presets, etc.).
- **Recommended for modern players** that support it.

#### ID3v2.3

- Older but **the most universally supported** ID3 version.
- Doesn't support UTF-8 directly (uses UTF-16 for Unicode text).
- **Recommended when you need maximum compatibility** with legacy players, car stereos, and certain desktop apps.

#### When to enable ID3v2.4 in Evertag

- You're using **modern audio players** like Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (current versions), or modern Android players. ✅ **Turn ID3v2.4 ON.**
- Your library contains **non-Latin characters** (Chinese, Korean, Japanese, Russian, Arabic, Greek, Hebrew). ✅ **Turn ID3v2.4 ON** — UTF-8 handles these much more cleanly.

#### When to disable ID3v2.4 in Evertag (use ID3v2.3 instead)

- You're preparing files for an **older car stereo or in-dash unit** that doesn't read v2.4 tags.
- You see **garbled text or missing tags** in some apps after editing — that's a strong signal v2.4 isn't supported there. Switch back to v2.3.
- You're targeting **legacy desktop players** or older portable players (early iPods, certain MP3 players from the 2000s–2010s).

> **Rule of thumb:** if your tags display correctly everywhere with v2.4, leave it on. If even one important player shows wrong characters, blanks, or fails to read your tags, turn v2.4 off and re-save.

#### Duplicate Tags

When you enable **Duplicate tags**, Evertag writes common metadata fields (title, artist, album, etc.) into **both ID3v1 and ID3v2 sections** of the file. This improves compatibility with very old players that only read ID3v1 (the original 128-byte tag at the end of the file).

- **Most users don't need this.** Modern players read ID3v2 first.
- **Enable it only if** you're dealing with vintage hardware or some specific software that ignores ID3v2.

### Update Online Files: How Evertag Handles Cloud Edits

When you edit tags on a file stored on a connected cloud (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP, etc.), Evertag has to upload the modified file back. You control how that happens:

- **Show confirmation message** *(default, recommended)* — Evertag asks you before uploading. Best for cautious users and shared libraries.
- **Automatically update file's metadata** — uploads silently after each edit. Best for solo users with fast, reliable connections who edit a lot.
- **Do not update file's metadata** — Evertag edits the local copy only. Useful when you want to preview tag changes without committing them to the cloud.

### Edit Online Files: Local File Cleanup

To edit a remote file, Evertag downloads it to your device first. After editing, you choose what happens to that local copy:

- **Always delete downloaded file** — Evertag removes the temporary file after editing. **Recommended** if you're tight on storage or working on someone else's files.
- **Do not delete downloaded file** — keeps the edited file on your device. Useful if you want both an offline copy and an updated cloud copy.

### Buttons on the Main Screen

Evertag's tag editor home screen can show or hide buttons for individual operations. Toggle the ones you actually use to keep the UI focused:

- **Auto-search audio tags** — finds missing metadata online based on the file's audio fingerprint.
- **Manual search audio tags** — search by title/artist when auto-search misses.
- **Search album artwork** — finds and embeds high-quality cover art.
- **Save album artwork** — exports the embedded cover to your photo library or files.
- **Normalize encoding** — fixes garbled non-Latin text caused by old encodings (very useful for Cyrillic, Chinese, and Japanese tracks ripped on legacy software).
- **Delete audio tags** — strips all tags from a file. Useful before fresh tagging.

### Show Extended Tags

Toggle this to display the full set of metadata fields beyond the basic title/artist/album/year — including BPM, conductor, original artist, mood, copyright, encoder, comments, lyrics, and more. Power-user feature; most casual users don't need it.

### Edit Files Simultaneously

When enabled, Evertag lets you edit metadata across **multiple selected files at once** — set the same album artist, year, or genre for an entire album in a single operation. This is the fastest way to clean up a large unorganized library.

## Editing Tags for Spotify, Apple Music, and Streaming Platforms

A common question we get: "I edited my tags in Evertag, uploaded the files, and the streaming service shows wrong metadata. What gives?"

The short answer: **streaming services don't always honor your local tags**. Apple Music and Spotify have their own internal databases — when they recognize a track, they overwrite the displayed metadata with their own. But for **uploaded files**, your local files (Apple Music's "Library" feature, Spotify Local Files), and **distributor uploads to streaming platforms**, your tags absolutely matter. Here's how to set Evertag for each scenario:

### Preparing files for Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music handles UTF-8 correctly.
- **Album cover: Large** — Apple's apps render large artwork well; Original is overkill.
- **Duplicate tags: OFF** — not needed.
- Make sure **Album Artist** is filled correctly — Apple Music uses it for grouping.

### Preparing files for Spotify Local Files

Spotify Local Files only displays files that are well-tagged. The tags Spotify reads are limited.

- **ID3v2.4: ON** in most cases. If a track refuses to show up correctly in Spotify after editing, **try saving with ID3v2.4 OFF** (i.e., as ID3v2.3) — Spotify's parser has been historically conservative about v2.4.
- **Album cover: Medium or Large** — Spotify scales artwork down anyway.
- Fill **Title**, **Artist**, **Album**, and **Track Number** at minimum.

### Preparing files for distributor upload (DistroKid, TuneCore, CD Baby, etc.)

If you're an artist uploading your own work to streaming platforms, your distributor usually reads tags but also asks for metadata in their UI. Either way:

- **ID3v2.3** is often the safer default — many distributor pipelines were built years ago and prefer the older format.
- Embed **Large** artwork (most distributors require ≥ 1,400 × 1,400 px artwork — check their guidelines).
- Don't rely on extended tags — distributors only read core fields.

### Preparing files for Plex, Jellyfin, Navidrome, Subsonic, Emby

These self-hosted media servers are very tolerant. They read both v2.3 and v2.4 cleanly and handle UTF-8 well.

- **ID3v2.4: ON** is fine.
- **Album cover: Large** or **Extra Large** — these servers serve artwork to mobile clients and CarPlay screens, so quality matters.
- **Album Artist** is strongly recommended — that's what Plex/Jellyfin use to group albums by artist correctly.

### Preparing files for car stereos and older hardware

- **ID3v2.4: OFF** (use ID3v2.3) — older head units often don't support v2.4.
- **Album cover: Medium** — many car displays choke on large embedded art.
- **Duplicate tags: ON** — older car stereos sometimes only read the ID3v1 fallback.

## Other Improvements

### Liquid Glass Design

Evertag 4.2's interface is tuned for Apple's new **Liquid Glass** material across the app — translucent surfaces, smoother animations, and refined controls that fit naturally into iOS, iPadOS, and macOS.

### Updated Connection Libraries

We refreshed the underlying libraries Evertag uses to talk to **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, and other services. The result: fewer edge-case connection failures, better support for newer server versions, and improved reliability when editing tags on remote files.

### Translation and Localization Fixes

Multiple language fixes across the UI based on direct feedback from users. Better text fitting on smaller buttons in several languages.

### Smaller Refinements Inspired by Your Feedback

Many smaller improvements based on App Store reviews and emails to support@everappz.com. We read every message.

## Get Evertag 4.2

[**Download Evertag from the App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) or update from inside the App Store. Evertag is a free download with optional in-app upgrades for advanced features. The new cloud connections, network protocols, Wi-Fi Drive improvements, and Liquid Glass UI are part of the base update.

If you enjoy the app, please leave a rating on the App Store — it genuinely helps. Have feedback or run into an issue? Email us at **support@everappz.com**. We read every message.

## Frequently Asked Questions

{{% details title="What's new in Evertag 4.2?" closed="true" %}}
Evertag 4.2 adds 6+ new cloud and server connections (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), a refreshed Wi-Fi Drive with multi-select and a smarter upload queue, Liquid Glass UI updates, updated connection libraries, key tag editing bug fixes, and translation improvements.
{{% /details %}}

{{% details title="Should I use ID3v2.4 or ID3v2.3 in Evertag?" closed="true" %}}
Use **ID3v2.4** for modern players (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, modern Android apps) and for libraries with non-Latin characters — UTF-8 support means cleaner Chinese, Korean, Japanese, Russian, Arabic, and Hebrew tags. Use **ID3v2.3** if your tags display incorrectly in some apps, if you target older car stereos, or if a streaming distributor pipeline rejects v2.4. You can always switch and re-save.
{{% /details %}}

{{% details title="Why are my tags wrong in Spotify after editing?" closed="true" %}}
Spotify mostly displays metadata from its own catalog — your local tags are only used for "Local Files" or for content you've uploaded as an artist. If you're tagging files for Spotify Local Files and they don't show correctly, try disabling ID3v2.4 in Evertag and saving as ID3v2.3 — Spotify's parser has been conservative about v2.4 historically.
{{% /details %}}

{{% details title="What album cover size should I choose in Evertag?" closed="true" %}}
For most users: **Large**. It looks great on phones, iPads, Macs, and modern car displays without inflating file sizes too much. Use **Medium** if you have a huge library and want to save disk. Use **Original** (no scaling) only for archival masters or when you specifically need maximum quality — but be aware some older players struggle with very large embedded artwork. **Original** is part of Evertag's premium personalization upgrade.
{{% /details %}}

{{% details title="Will larger album covers make my files bigger?" closed="true" %}}
Yes. Embedding a 3,000 × 3,000 px artwork can add several megabytes to a single audio file. Across a 1,000-track library, that adds up to gigabytes. If storage is tight, use Medium or Large; if you stream from a NAS where size doesn't matter, Extra Large or Original is fine.
{{% /details %}}

{{% details title="What is Duplicate Tags and should I enable it?" closed="true" %}}
Duplicate Tags writes the core metadata into both ID3v1 (legacy 128-byte) and ID3v2 (modern) sections of the file. Enable it only if you're targeting very old players or hardware that reads ID3v1. For everything modern (smartphones, computers, recent car stereos), leave it off.
{{% /details %}}

{{% details title="Does Evertag edit tags on cloud files directly?" closed="true" %}}
Yes. Connect to your cloud (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, etc.) or via FTP/SFTP/NFS, then open a file and edit tags as if it were local. Evertag downloads the file, applies your edits, and uploads the updated version back. You can choose between Always ask, Auto-upload, or Don't upload modes in settings.
{{% /details %}}

{{% details title="Can I edit FLAC tags on iPhone with Evertag?" closed="true" %}}
Yes. Evertag supports FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE, and other major formats with full read/write tag support including embedded artwork.
{{% /details %}}

{{% details title="How do I securely edit tags on my home server with SFTP?" closed="true" %}}
Open Evertag, go to Connections, choose SFTP, and enter your server's hostname or IP, port (usually 22), username, and either a password or an SSH private key. Evertag will browse your remote folders and edit tags directly with end-to-end encryption over SSH.
{{% /details %}}

{{% details title="Can I edit tags on multiple files at once?" closed="true" %}}
Yes. Enable **Edit files simultaneously** in settings. Select multiple files, open the tag editor, and any field you change will apply to all selected files. This is the fastest way to set the same album artist, year, or genre across an album.
{{% /details %}}

{{% details title="Is Evertag 4.2 free to update?" closed="true" %}}
Yes. Evertag is a free download from the App Store, and 4.2 is a free update for all existing users. The new cloud integrations, Wi-Fi Drive improvements, and Liquid Glass UI are part of the base update.
{{% /details %}}

{{% details title="Which devices is Evertag 4.2 available on?" closed="true" %}}
Evertag 4.2 runs on iPhone, iPad, and Mac. iCloud Drive sync keeps your tag editing settings consistent across devices.
{{% /details %}}
