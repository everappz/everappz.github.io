---
title: "How to Set Up an FTP Server on iPhone & iPad for File Transfers"
description: "Turn your iPhone or iPad into an FTP server with Everdisk and transfer files from a Mac, Windows PC, Linux, Android, an FTP app like FileZilla, or another iPhone over Wi-Fi. Full setup, the ftp address and port, guest access, and step-by-step connection for every device."
date: 2026-09-19
tags: ["everdisk", "ftp", "file transfer", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["FTP server iPhone", "FTP server iPad", "how to set up FTP on iPhone", "iphone ftp server app", "connect FileZilla to iPhone", "Cyberduck iPhone FTP", "transfer files iPhone FTP", "ftp iphone to computer", "ftp iphone to iphone", "connect to iPhone FTP from Windows", "ftp address port iphone", "anonymous ftp iphone", "share files iphone ftp", "iphone ftp for camera nas"]
readingTime: 9
aliases:
  - /post/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/
---

{{< author-byline >}}

FTP is the old reliable of file transfer. It has been around for decades, which is exactly why it is so useful: almost anything that can talk to a server understands it. Cameras, smart TVs, routers, network drives, automation tools and every desktop FTP app speak FTP. With [Everdisk](/products/everdisk) you can run an FTP server on your iPhone or iPad, so the phone becomes a place those devices and apps can connect to and move files.

Reach for FTP when the other options do not fit, for example an older device or an app that only knows how to connect over FTP. This guide covers the setup and how to connect from a Mac, Windows, an FTP app, Linux, Android and a second iPhone.

## What you need

- An iPhone or iPad with [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installed.
- A computer, app or device on the **same Wi-Fi network**.
- The files you want to share, in the Everdisk Documents folder or in folders you add.

## Set up the FTP server in Everdisk

### Step 1: Choose what to share and set access

Open Everdisk, go to the **Sharing** tab, and tap **What to Share**. The Documents folder is shared by default. Add more with **Add Folder** and **Add File**.

Open **Settings**, then **Sharing**, then **Access**. Turn **Files Editing** on if you want people to upload, rename and delete, or off to allow downloads only. Set a **Login** and **Password** if you want a sign in, or leave them empty so anyone can connect as a guest.

### Step 2: Turn on the FTP server

Go to **Settings**, then **Sharing**, then **Connections**, and turn on **Other Apps & Devices**. That is the FTP server (it carries the FTP tag).

### Step 3: Start sharing and note the address

Return to the **Sharing** tab and tap **Start**. The **How to Connect** section shows the FTP address. It looks like this:

```
ftp://192.168.1.20:2121
```

The number after the colon is the **port**, which is **2121** by default. The first part is your iPhone's address on the Wi-Fi, so yours will be different. Keep Everdisk open on screen while a device is connected.

## Connect from a Mac

1. Open **Finder**, choose **Go**, then **Connect to Server** (or press **Command and K**).
2. Type the FTP address shown in Everdisk, for example `ftp://192.168.1.20:2121`.
3. Click **Connect**, then choose **Guest** or enter your **Login** and **Password**.

Finder mounts the FTP share so you can browse and copy files to your Mac. Note that Finder opens FTP as read only. When you want to upload from a Mac, use an FTP app as described below.

## Connect from Windows

1. Open **File Explorer** and click the address bar at the top.
2. Type the FTP address from Everdisk, for example `ftp://192.168.1.20:2121`, and press **Enter**.
3. Enter your **Login** and **Password** if you set one, or continue as a guest.

The shared files appear in the window and you can copy them to your PC.

## Connect with an FTP app (FileZilla, Cyberduck)

For uploads and full control, an FTP app is the best tool. **FileZilla** and **Cyberduck** are free and run on Windows, Mac and Linux.

1. Open the app and create a new connection.
2. Set the **Host** to your iPhone's Wi-Fi address, and the **Port** to **2121**.
3. For the login, enter your **Login** and **Password**, or choose **Anonymous** if you did not set one.
4. Connect, and drag files in both directions (uploads need Files Editing on).

## Connect from Linux

1. Open your file manager and choose **Connect to Server** or **Other Locations**.
2. Enter the address, for example `ftp://192.168.1.20:2121`.
3. Connect as a guest or with your login.

You can also use any Linux FTP client from the terminal, pointing it at the same host and port 2121.

## Connect from Android

Android has no system FTP browser, so use an app:

1. Install an FTP client such as **AndFTP**, **FTPCafe**, or a file manager with FTP support like **Solid Explorer**.
2. Add a connection with the host, **port 2121**, and your login or Anonymous.
3. Browse and transfer.

## Connect from another iPhone or iPad

The iOS Files app does not include an FTP client, so use one of these on the second device:

- **Everdisk's own Devices tab.** Open Everdisk, go to **Devices**, tap **New Connection**, choose **FTP**, and enter the address, for example `ftp://192.168.1.20:2121`. This is the simplest route.
- **A dedicated FTP app** for iOS, using the same host, port 2121 and login.

## Connect other gear: cameras, TVs, routers and NAS

This is where FTP shines. Many devices have a built-in FTP client that can send or fetch files:

- **Cameras** that upload photos over FTP can send them straight to your iPhone.
- **Smart TVs, routers, NAS boxes and automation tools** that support FTP can connect the same way.

Point them at your iPhone's Wi-Fi address, port **2121**, and your login (or Anonymous), using the address shown in Everdisk.

## Read only or read and write

The **Files Editing** switch in Settings, Sharing, Access controls this. On lets people upload, rename and delete. Off means they can only download. Choose read only when you are handing files out and do not want anything changed on your phone.

## Real-life ways people use this

- **Connect FileZilla to your iPhone** and push a batch of files onto the phone in one go.
- **Let an old app or device that only speaks FTP** reach your files when nothing else will connect.
- **Receive photos from a camera** that uploads over FTP.
- **Move files between an iPhone and an iPad** using Everdisk's Devices tab on the receiving device.

## A few tips

- Keep Everdisk open while a device is connected, since iOS pauses background apps after a while.
- To upload from a Mac, use FileZilla or Cyberduck rather than Finder, because Finder opens FTP as read only.
- Leave the login empty for the widest compatibility, then connect as Anonymous, which most FTP clients offer.
- FTP does not encrypt its traffic. On a network you do not trust, use the [SMB server with encryption](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) instead.

## Frequently Asked Questions

{{% details title="What is the FTP address and port for my iPhone?" closed="true" %}}
After you start sharing, Everdisk shows the address on the Sharing screen. It looks like ftp://192.168.1.20:2121. The 2121 is the port Everdisk uses for FTP, and the first part is your iPhone's address on the Wi-Fi, so yours will be different.
{{% /details %}}

{{% details title="How do I connect FileZilla or Cyberduck to my iPhone?" closed="true" %}}
Open the app and create a new connection. Set the Host to your iPhone's Wi-Fi address and the Port to 2121. Enter your Login and Password, or choose Anonymous if you did not set one in Everdisk. Connect, and you can drag files in both directions when Files Editing is on.
{{% /details %}}

{{% details title="Can I connect to my iPhone FTP from Windows?" closed="true" %}}
Yes. Open File Explorer, click the address bar, type the FTP address from Everdisk (for example ftp://192.168.1.20:2121), and press Enter. Enter your login if you set one, or continue as a guest. For uploads and more control, use an FTP app like FileZilla instead.
{{% /details %}}

{{% details title="Do I need a login for FTP?" closed="true" %}}
No, a login is optional. Leave the Login and Password empty in Settings, Sharing, Access, and connect as Anonymous, which most FTP clients offer. Set a login if you want connections to sign in first.
{{% /details %}}

{{% details title="Why can I only download and not upload over FTP?" closed="true" %}}
Two reasons are common. First, the Files Editing switch in Settings, Sharing, Access must be on to allow uploads, renames and deletes. Second, Mac Finder opens FTP as read only, so use an FTP app like FileZilla or Cyberduck when you want to upload.
{{% /details %}}

{{% details title="Can I use FTP between two iPhones?" closed="true" %}}
Yes. Start the FTP server on the first iPhone. On the second, open Everdisk, go to the Devices tab, tap New Connection, choose FTP, and enter the address shown on the first phone. A dedicated FTP app for iOS works too, since the iOS Files app does not include an FTP client.
{{% /details %}}

{{% details title="Is FTP secure?" closed="true" %}}
Plain FTP does not encrypt its traffic, so treat it as a tool for networks you trust, like your home Wi-Fi. On a network you do not control, use the SMB server with Require SMB Encryption turned on, which protects every transfer.
{{% /details %}}

{{% details title="Which devices can connect over FTP?" closed="true" %}}
Almost anything with an FTP client. That includes Mac, Windows and Linux computers, FTP apps like FileZilla and Cyberduck, Android file managers, and hardware such as cameras, smart TVs, routers, NAS boxes and automation tools. That wide reach is the main reason to choose FTP.
{{% /details %}}

{{% details title="Why did my FTP connection drop?" closed="true" %}}
Your iPhone is the server, and iOS pauses apps that stay in the background too long. Keep Everdisk open on screen while a device is connected, and plug into power for long transfers. Also make sure both devices are still on the same Wi-Fi.
{{% /details %}}

{{% details title="Is Everdisk free?" closed="true" %}}
Yes, Everdisk is free to download and the FTP server is included. An optional one-time Premium purchase adds extras like custom ports and photo and video conversion. You can set up FTP and transfer files without paying.
{{% /details %}}

Ready to try it? [Download Everdisk from the App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) and connect your first FTP client in a couple of minutes. Questions or feedback? Email us at **support@everappz.com**.
