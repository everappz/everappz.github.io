---
title: "How to Set Up a WebDAV Server on iPhone & iPad for File Access & Sharing"
description: "Turn your iPhone or iPad into a WebDAV server with Everdisk and mount it as a network drive on Mac Finder, Windows File Explorer, Linux, Android or another iPhone over Wi-Fi. Full setup, the WebDAV address and port, and step-by-step connection for every device."
date: 2026-09-19
tags: ["everdisk", "webdav", "network drive", "file sharing", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["WebDAV server iPhone", "WebDAV server iPad", "how to set up WebDAV on iPhone", "mount iPhone as network drive", "connect iPhone WebDAV Mac Finder", "WebDAV Windows File Explorer iPhone", "iphone network drive Windows", "WebDAV Linux iPhone", "access iPhone files from computer", "webdav iphone to iphone", "share files iPhone WebDAV", "map network drive iphone", "transfer files iphone webdav", "webdav address port iphone"]
readingTime: 9
aliases:
  - /post/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/
---

{{< author-byline >}}

WebDAV turns a folder into a network drive that a computer can open in its normal file manager. It runs over the same web protocol your browser uses, which is why it travels well across Mac, Windows and Linux without special drivers. With [Everdisk](/products/everdisk) you can run a WebDAV server on your iPhone or iPad, so the phone shows up as a drive you can browse, copy from, and copy to from almost any computer.

WebDAV is the best pick when Windows is in the picture, because Windows File Explorer connects to it cleanly. This guide covers the setup and how to connect from a Mac, Windows, Linux, Android and a second iPhone.

## What you need

- An iPhone or iPad with [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installed.
- A computer or another device on the **same Wi-Fi network**.
- The files you want to share, in the Everdisk Documents folder or in folders you add.

## Set up the WebDAV server in Everdisk

### Step 1: Choose what to share and set access

Open Everdisk, go to the **Sharing** tab, and tap **What to Share**. The Documents folder is shared by default. Add more with **Add Folder** and **Add File**.

Open **Settings**, then **Sharing**, then **Access**. Set **Files Editing** on if you want connected computers to copy files onto your phone and rename or delete them, or off for a read only drive. Set a **Login** and **Password** here if you want a sign in, or leave them empty for guest access.

### Step 2: Turn on the WebDAV server

Go to **Settings**, then **Sharing**, then **Connections**, and turn on **Computer**. That is the WebDAV server (it carries the WebDAV tag).

### Step 3: Start sharing and note the address

Return to the **Sharing** tab and tap **Start**. The **How to Connect** section shows the WebDAV address. It looks like this:

```
http://192.168.1.20:8080
```

The number after the colon is the **port**, which is **8080** by default. The first part is your iPhone's address on the Wi-Fi, so yours will differ. Keep Everdisk open on screen while a device is connected.

## Connect from a Mac

1. Open **Finder**, choose **Go**, then **Connect to Server** (or press **Command and K**).
2. Type the WebDAV address shown in Everdisk, for example `http://192.168.1.20:8080`.
3. Click **Connect**, then choose **Guest** or enter your **Login** and **Password**.

Your iPhone opens in a Finder window and behaves like a normal folder. Copy files in either direction if Files Editing is on.

## Connect from Windows

Windows has a built-in WebDAV client, so this works from File Explorer.

1. Open **File Explorer**, right-click **This PC** in the sidebar, and choose **Add a network location** (you can also use **Map network drive**).
2. When asked for the address, type the same WebDAV address from Everdisk, for example `http://192.168.1.20:8080`, then click **Next**.
3. Enter your **Login** and **Password** if you set one.

The device then appears under This PC as a network location you can open and copy files from. If Windows refuses to connect the first time, make sure the **WebClient** service is running (search Services in the Start menu, find WebClient, and set it to start), then try again.

## Connect from Linux

1. Open your file manager and choose **Connect to Server** or **Other Locations**.
2. Enter the address with a WebDAV prefix, for example `dav://192.168.1.20:8080` (use `davs://` only if you set up TLS).
3. Connect as a guest or enter your login.

## Connect from Android

Android has no system WebDAV browser, so use a file manager that supports it:

1. Install an app such as **Solid Explorer** or **CX File Explorer**.
2. Add a new **WebDAV** connection.
3. Enter the host and **port 8080**, choose the `http` scheme, and add your login if you set one.

## Connect from another iPhone or iPad

The iOS Files app does not include a WebDAV client, so use one of these:

- **Everdisk's own Devices tab.** On the second device, open Everdisk, go to **Devices**, tap **New Connection**, choose **WebDAV**, and enter the address, for example `http://192.168.1.20:8080`. This is the simplest route and needs nothing extra.
- **A WebDAV app** such as Documents by Readdle, which can add a WebDAV connection with the same address and login.

## Prefer a quick link instead of a drive?

If you only need to grab a file fast and do not want to mount a drive at all, turn on the **Browser** connection in Settings, Sharing, Connections. Everdisk then gives you a web address you can open in any browser on any device to browse and download your files. It is the fastest way to hand a file to a Windows PC, a Chromebook or a friend's phone.

## Read only or read and write

The **Files Editing** switch in Settings, Sharing, Access decides this. On means connected computers can upload, rename and delete. Off means the drive is read only, so others can view and copy your files but cannot change them.

## Real-life ways people use this

- **Copy files onto your iPhone from a Windows PC** by mapping it as a network location and dragging them across.
- **Offload photos and documents to a laptop** using the file manager you already know, with no cable and no iTunes.
- **Edit a document in place** from your Mac, opening it straight from the phone and saving back.
- **Move a folder between an iPhone and an iPad** using Everdisk's Devices tab on the receiving device.

## A few tips

- Keep Everdisk open while a device is connected. Locking the phone for a long time can pause the app.
- On Windows, if the connection fails, start the WebClient service and try the address again.
- WebDAV and SMB both mount as network drives. Use WebDAV when Windows is involved, and [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) when you want Finder speed and encryption.
- For the fastest transfers, keep photo and video quality on Original in Settings.

## Frequently Asked Questions

{{% details title="What is the WebDAV address and port for my iPhone?" closed="true" %}}
After you start sharing, Everdisk shows the address on the Sharing screen. It looks like http://192.168.1.20:8080. The 8080 is the port Everdisk uses for WebDAV, and the first part is your iPhone's address on the Wi-Fi, so yours will be different.
{{% /details %}}

{{% details title="How do I connect to my iPhone WebDAV from Windows?" closed="true" %}}
Open File Explorer, right-click This PC, and choose Add a network location or Map network drive. Enter the WebDAV address from Everdisk, for example http://192.168.1.20:8080, then enter your login if you set one. If Windows will not connect, make sure the WebClient service is running (search Services, find WebClient, start it) and try again.
{{% /details %}}

{{% details title="Can I use WebDAV between two iPhones?" closed="true" %}}
Yes, but the iOS Files app has no WebDAV client, so use Everdisk on the second device. Open the Devices tab, tap New Connection, choose WebDAV, and enter the address shown on the first phone. A WebDAV app such as Documents by Readdle works too.
{{% /details %}}

{{% details title="Does WebDAV need a password?" closed="true" %}}
No, a login is optional. Leave the Login and Password empty in Settings, Sharing, Access for guest access, or set them if you want connections to sign in.
{{% /details %}}

{{% details title="Can other people change my files over WebDAV?" closed="true" %}}
Only if you allow it. The Files Editing switch in Settings, Sharing, Access controls this. On lets connected devices upload, rename and delete. Off makes the drive read only, so others can view and copy but not change anything.
{{% /details %}}

{{% details title="WebDAV or SMB, what is the difference?" closed="true" %}}
Both mount your iPhone as a network drive. WebDAV runs over the web protocol and connects cleanly from Windows File Explorer, which is its main strength. SMB is the native file sharing on Mac, Linux and NAS devices, is usually faster on a Mac, and is the only Everdisk connection that can encrypt transfers. Everdisk can run both at once.
{{% /details %}}

{{% details title="Why does my WebDAV drive disconnect?" closed="true" %}}
Your iPhone is the server, and iOS pauses apps that stay in the background too long. Keep Everdisk open on screen while a device is connected, and plug into power for long transfers. Also confirm both devices are still on the same Wi-Fi.
{{% /details %}}

{{% details title="Can I connect over WebDAV without Wi-Fi?" closed="true" %}}
Yes, if you plug your iPhone into a Mac with a cable. Everdisk then shows an extra cable connection address that the connected Mac can open in Finder, which works even with no Wi-Fi at all. On the cable, only that Mac can reach the device.
{{% /details %}}

{{% details title="Is Everdisk free?" closed="true" %}}
Yes, Everdisk is free to download and the WebDAV server is included. An optional one-time Premium purchase adds extras like custom ports and photo and video conversion. You can set up WebDAV and share files without paying.
{{% /details %}}

Ready to try it? [Download Everdisk from the App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) and mount your iPhone as a drive in a couple of minutes. Questions or feedback? Email us at **support@everappz.com**.
