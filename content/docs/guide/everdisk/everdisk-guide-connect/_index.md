---
title: "Connect Your Devices"
date: 2025-09-03
description: "Step-by-step instructions for connecting to your Everdisk wireless drive: watch on a smart TV over DLNA, open your files in any web browser, mount your device as a network drive in Finder, Windows or Linux over WebDAV, connect file apps over FTP, and transfer over a USB cable to a Mac with no Wi-Fi."
keywords: [
  "connect to Everdisk", "stream to TV DLNA", "open files in browser",
  "mount network drive Finder", "WebDAV Windows Linux", "FTP file app",
  "USB cable transfer Mac", "connect iPhone to computer", "network drive iPhone"
]
tags: ["everdisk", "guide", "connect"]
readingTime: 11
aliases:
  - /guide-everdisk-connect/
---


Once you tap **Start** on the [Sharing](/docs/guide/everdisk/everdisk-guide-sharing) screen, other devices can connect to your files four different ways. Pick the method that matches the device you want to use. In every case, the exact **address** you need is shown in the **How to Connect** section of the Sharing screen.

> Both devices must be on the **same Wi-Fi network** — or, for a Mac, connected with a **USB cable** (see the last section).

## Watch on a TV (DLNA)

Use this to show photos, videos and music on a smart TV or media player.

1. In **Settings → Sharing → Connections**, make sure **TV & Media Center** is on (it is on by default).
2. On the Sharing screen, tap **Start**.
3. On your TV, open its built-in media player or media-server app (it may be called Media Player, SmartShare, AllShare, or similar).
4. Your device appears in the list of media servers by its name (for example "Speedy-Hare"). Select it.
5. Browse your shared photos, videos and music and start playing. Preview thumbnails appear automatically.

Notes:

- DLNA can't be password protected, so this connection is open to anyone on the same Wi-Fi while it is turned on.
- If a video won't play on an older TV, lower the video quality in **Settings → Sharing → Videos** so Everdisk converts it to a more compatible format.

## Open in a web browser (HTTP)

Use this to hand files to anyone with a web browser — no app to install.

1. In **Settings → Sharing → Connections**, make sure **Browser** is on.
2. Tap **Start**.
3. On the Sharing screen, copy the **Browser** address (or show its QR code).
4. On the other phone, tablet or computer, open any web browser (Safari, Chrome, Edge, Firefox) and type that address.
5. The page opens with your shared files.

In the browser the other person can:

- Switch between **list** and **grid** views and sort by name, date or size.
- See real **thumbnails** for photos, videos, PDFs and music artwork.
- Open a photo to a full-screen **gallery** with swipe, pinch-to-zoom and a slideshow.
- Play music in a built-in **player** with a queue, shuffle and repeat.
- **Download** any file, or download a whole folder (or several selected items) as a single **Archive.zip**.
- **Upload** files back to your device — only if you turned on **Files Editing** (see [Access & Privacy](/docs/guide/everdisk/everdisk-guide-access)).

## Use it as a network drive (WebDAV)

Use this to make your device appear as a normal disk on a Mac, Windows PC or Linux machine, so you can drag files both ways.

**On a Mac (Finder)**

1. In **Settings → Sharing → Connections**, make sure **Computer** is on.
2. Tap **Start** and note the **Computer (WebDAV)** address.
3. In Finder, choose **Go → Connect to Server** (or press **⌘K**).
4. Type the WebDAV address exactly as shown and click **Connect**.
5. Enter the login and password if you set one, otherwise connect as a guest.
6. Your device opens like any other network drive. Drag files in or out.

**On Windows**

1. Open **File Explorer**, right-click **This PC**, and choose **Add a network location** (or map a network drive).
2. Enter the WebDAV address shown in Everdisk.
3. Enter the login and password if you set one.

**On Linux**

1. Open your file manager and choose **Connect to Server** (or use `davs://` / `dav://`).
2. Enter the WebDAV address shown in Everdisk.

Whether the connection is read-only or two-way depends on the **Files Editing** setting. With it on, you can copy files onto your device and rename or delete them; with it off, the drive is read-only.

## Connect a file app (FTP)

Use this for file-manager and transfer apps that speak FTP (for example FileZilla or Cyberduck on a computer).

1. In **Settings → Sharing → Connections**, make sure **Other Apps & Devices** is on.
2. Tap **Start** and note the **FTP** address.
3. In your FTP app, add a new connection using that address.
4. Enter the login and password if you set one, or leave them empty for anonymous access.

## Transfer over a USB cable (Mac, no Wi-Fi needed)

Use this when there is no Wi-Fi, or when you want the fastest and most private transfer. It works with a **Mac** only.

1. Plug your iPhone or iPad into the Mac with the normal charging cable.
2. If asked on the device, tap **Trust This Computer**.
3. In Everdisk, tap **Start**. A **Fast Connection Available** note appears and the Sharing screen shows an extra address with a **Cable Connection** badge that ends in `.local`.
4. On the Mac, open Finder → **Go → Connect to Server** (**⌘K**) and enter that `.local` address (it works for both the Browser and Computer connections).
5. Your device opens over the cable — faster than Wi-Fi, and the data never touches the router or the internet.

Notes:

- Use the **`.local` name**, not an IP address (IP addresses only work over Wi-Fi), and never `localhost`.
- The cable path is **Mac only**. Windows PCs and Android devices must use Wi-Fi.
- You can also drag files into the Everdisk folder using Finder on a Mac, or the Apple Devices app (or iTunes) on Windows, through standard iOS file sharing.

## Next steps

- [Access & Privacy](/docs/guide/everdisk/everdisk-guide-access) — add a password, allow uploads, block a device.
- [Photos, Music & Video](/docs/guide/everdisk/everdisk-guide-media) — share your whole library and set quality.
- [Connect to Servers](/docs/guide/everdisk/everdisk-guide-devices) — reach other devices from Everdisk.
