---
title: "Access & Privacy"
date: 2026-08-20
description: "Keep your Everdisk sharing safe: protect access with a login and password, encrypt the SMB connection with SMB3 (AES), control whether connected devices can upload, rename and delete with Files Editing, block unknown devices, choose trash vs. permanent delete, and understand why everything stays on your local network."
keywords: [
  "Everdisk password protection", "SMB encryption", "SMB3 AES encryption", "files editing toggle", "block device",
  "blocked devices", "permanently delete files", "local network only",
  "private file sharing", "DLNA no password", "network safety"
]
tags: ["everdisk", "guide", "access", "privacy", "security"]
readingTime: 8
aliases:
  - /guide-everdisk-access/
---


Everdisk keeps your files on your own network and gives you simple controls over who can reach them and what they can do. You find these controls in **Settings → Sharing → Access**, plus a few related settings in File Manager.

## Protect access with a login and password

By default, anyone on the same network who has your address can open your shared files. To require a sign-in:

1. Go to **Settings → Sharing → Access**.
2. Enter a **Login** and a **Password**.
3. Now the **Browser (HTTP)**, **Computer (WebDAV)**, **Computer (Advanced) (SMB)** and **Other Apps & Devices (FTP)** connections all ask for those details before they show your files.

Leave both fields empty for open access. Your password is stored securely in the device Keychain.

> **DLNA is always open.** The TV & Media Center (DLNA) connection can't be password protected, so once it is on, any device on the same Wi-Fi can browse your shared media. Turn it off if you only want protected connections, and only share on networks you trust.

## Encrypt the SMB connection (SMB3 / AES)

A login and password control **who** can connect, but the data itself still travels in the clear on most connections. **SMB is the only connection Everdisk can encrypt**, which scrambles every transfer so no one else on the same network can read it.

To turn it on:

1. Set a **Login** and **Password** as above - encrypted connections can't be anonymous.
2. Go to **Settings → Sharing** and turn on **Require SMB Encryption**.
3. **Stop and Start** sharing again so the change takes effect.

Every SMB transfer is then protected with **SMB3 encryption (AES)**. The connecting device must support SMB3 - the Finder on a modern Mac, or **Windows 10 and later**. This is a great choice on Wi-Fi you don't fully trust. SMB Encryption is a Premium feature.

## Allow or block editing (Files Editing)

The **Files Editing** toggle controls whether connected devices can only look at your files, or also change them.

- **On** (the default): connected devices can **upload, rename and delete** your shared files - so your device works like a real two-way network drive.
- **Off**: your shared files are **read-only**. Others can view and download, but can't add or change anything.

Turning it on shows a short warning because it lets other people modify your files. It carries an **Important** badge while it is on.

## Block a device

If you see a device you don't recognize:

1. On the Sharing screen, find it under **Who is Connected**.
2. Tap its more-actions button and choose **Block this device**.

Blocked devices are listed in **Settings → Sharing → Access → Blocked Devices**, where you can **unblock** one or **Unblock All**. Blocking follows the device even if its network address changes (for the Browser, Computer and TV connections).

## Trash vs. permanent delete

When a file is deleted - by you in the file manager, or by a connected device - it normally goes to a recoverable **trash** so you can get it back.

If you prefer files to be removed immediately with no recovery, turn on **Permanently Delete Files** in **Settings → File Manager → Deleting Files**. This is off by default. **It affects the on-device file manager** and **deletes made over the network**; it does not change how the system Photos library or Music library handle deletion.

## Everything stays local

Everdisk shares only over your **local network** - nothing is uploaded to the internet and there is no cloud account in the middle. A few things worth knowing:

- Everdisk needs the iOS **Local Network** permission so nearby devices can find it. If that permission is off, a note explains how to turn it back on in the iOS Settings app.
- For the most privacy, share only while you are on a **home or private Wi-Fi** network you trust, and be careful on public Wi-Fi. A login and password helps, but it is not a substitute for a trusted network.
- The **most private option of all is a USB cable to a Mac** - the data goes straight over the cable and never touches the router or the internet. See [Connect Your Devices](/docs/guide/everdisk/everdisk-guide-connect).

## Next steps

- [Sharing](/docs/guide/everdisk/everdisk-guide-sharing) - choose what to share and start sharing.
- [Settings](/docs/guide/everdisk/everdisk-guide-settings) - all Access and File Manager settings in one place.
