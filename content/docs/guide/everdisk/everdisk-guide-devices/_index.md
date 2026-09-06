---
title: "Connect to Servers"
date: 2026-08-20
description: "Use the Devices tab in Everdisk to connect to other servers on your network. Add and browse DLNA, WebDAV, FTP and SFTP servers and NAS drives, stream audio and video, download files, and create, upload, rename, move or delete on servers that allow it."
keywords: [
  "Everdisk Devices tab", "connect to NAS", "DLNA client iPhone", "WebDAV client iPhone",
  "FTP client iPhone", "SFTP client iPhone", "browse network server", "stream from NAS",
  "download from server", "connect cloud WebDAV"
]
tags: ["everdisk", "guide", "devices", "connections"]
readingTime: 9
aliases:
  - /guide-everdisk-devices/
---


Everdisk is not only a wireless drive - it is also a client for the other devices on your network. The **Devices** tab lets you connect to **DLNA**, **WebDAV**, **FTP** and **SFTP** servers, including NAS drives and media servers, then browse, stream and download their files.

## The Devices screen

The Devices tab has two parts:

- **Connections** - the servers you have already saved.
- **Available Devices** - servers Everdisk finds automatically on your local network.

To connect to something Everdisk already found, just tap it in **Available Devices**. To add a server by hand, tap the **plus (+)** button or **New Connection**.

## Add a new connection

Tap **New Connection** and choose the type of server you want to reach:

- **DLNA / UPnP** - best for media servers. Stream video, music and photos from media libraries, network storage drives and DLNA-enabled TVs and computers. DLNA is read-only: you can browse, stream and download, but you can't upload or change files.
- **WebDAV** - connect to file servers, network storage drives, and cloud drives that support WebDAV. Read and write when the server allows it.
- **FTP** - common on routers, network storage drives and web hosting. The default port is 21 (990 for secure FTPS); you can set a custom port in the address, for example `ftp://host:2121`. Leave the login and password empty for anonymous access.
- **SFTP** - connect securely over SSH. The default port is 22; use a custom port in the address if needed, for example `sftp://host:2222`.

> Everdisk connects only to these local-network and directly-addressed protocols. It does not sign in to cloud accounts like Google Drive or Dropbox. A cloud drive is reachable only if that service offers a **WebDAV** address you can type in.

## Enter the address and sign in

On the connection editor, fill in:

- **Title** - a friendly name for the connection.
- **URL / address** - the server address (examples are shown for each type).
- **Login** and **Password** - leave both empty if the server allows anonymous access.

For WebDAV you can allow invalid certificates if your server uses a self-signed one. If a secure server's identity can't be verified, Everdisk asks you to confirm before trusting it.

Free users can save up to **10** connections. Premium removes the limit.

## Browse, stream and download

Once connected, tap the server to open it:

- **Browse** the folders in list or grid, sort them, and see thumbnails. DLNA servers also show music details and artwork.
- **Stream** audio and video. Audio goes to the mini player queue; video plays full screen. Seeking works while a file streams.
- **Download** files to your device. Select several at once for a batch download. Downloads appear in **File Transfers** and land in your **Documents** folder.
- **Info** on any item shows its kind, size, date, path and media details.

## Change files on a server

On servers that allow writing - **WebDAV, FTP and SFTP** - you can also manage files:

- **New Folder**
- **Upload Files** from your device
- **Rename**, **Move** and **Delete** (one item or several at once)

**DLNA** servers are read-only, so these actions are not available there.

## Track your transfers

Downloads and uploads run in the background and show up in **File Transfers**, which you open from the top-left of the **Documents** tab. There you can watch progress, and pause, resume, retry, cancel or clear tasks. You can also tune transfers in [Settings → Network](/docs/guide/everdisk/everdisk-guide-settings) (Wi-Fi only vs. Wi-Fi and cellular, how many run at once, and whether they continue in the background).

## Next steps

- [Files & Documents](/docs/guide/everdisk/everdisk-guide-files) - manage everything you download.
- [Photos, Music & Video](/docs/guide/everdisk/everdisk-guide-media) - play what you stream.
- [Settings](/docs/guide/everdisk/everdisk-guide-settings) - connection limits and transfer options.
