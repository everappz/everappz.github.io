---
title: "How to Set Up an SMB Server on iPhone & iPad for File Sharing"
description: "Turn your iPhone or iPad into an SMB file server with Everdisk and open it like a network drive from a Mac, another iPhone, Linux or Android over Wi-Fi. Full setup, the smb address and port, optional SMB3 encryption, and step-by-step connection for every device."
date: 2026-09-19
tags: ["everdisk", "smb", "file sharing", "network drive", "iphone", "ipad", "mac", "finder", "encryption", "wifi"]
keywords: ["SMB server iPhone", "SMB server iPad", "how to set up SMB on iPhone", "iPhone SMB share", "connect iPhone SMB Mac Finder", "smb iphone to iphone", "iOS Files app connect to server SMB", "share files iPhone SMB", "iphone network drive Finder", "SMB3 encryption iOS", "smb share iPhone Android", "connect to SMB from Linux", "iphone as network drive", "share files between iphones wifi", "map iphone as network drive"]
readingTime: 10
aliases:
  - /post/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/
---

{{< author-byline >}}

SMB is the file sharing built into macOS, Windows and Linux, and into almost every network drive (NAS). When you connect to a shared folder on another computer and it opens like a normal disk in Finder or File Explorer, that is SMB doing the work. With [Everdisk](/products/everdisk) you can put an SMB share on your iPhone or iPad, so the phone itself shows up as a network drive that other devices browse, copy from, and copy to.

This is the option to reach for when you want your iPhone to behave like a proper drive, not a web page. It is fast, it drags and drops both ways, and it is the only connection type in Everdisk that can encrypt every transfer. This guide covers the setup and how to connect from a Mac, another iPhone or iPad, Linux, Android, and Windows.

## What you need

- An iPhone or iPad with [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installed.
- Another device on the **same Wi-Fi network**.
- The files you want to share, in the Everdisk Documents folder or in folders you add.

## Set up the SMB server in Everdisk

### Step 1: Pick what to share and who can write

Open Everdisk, go to the **Sharing** tab, and tap **What to Share**. The Documents folder is shared by default. Add more with **Add Folder** and **Add File**, and turn on your Photos or Music library if you want those available too.

Decide whether other devices can only read your files, or also change them. Open **Settings**, then **Sharing**, then **Access**, and set **Files Editing**. With it on, connected devices can copy files onto your phone and rename or delete them. With it off, the share is read only.

If you want a login, set a **Login** and **Password** on the same Access screen. Leave both empty to allow guest access.

### Step 2: Turn on the SMB server

Go to **Settings**, then **Sharing**, then **Connections**, and turn on **Computer (Advanced)**. That is the SMB server (it carries the SMB tag).

### Step 3: Start sharing and note the address

Go back to the **Sharing** tab and tap **Start**. The **How to Connect** section now shows the SMB address. It looks like this:

```
smb://192.168.1.20:4455/Share
```

Three things to know about that address:

- The number after the colon is the **port**. Everdisk uses **4455** by default.
- The share is named **Share**.
- The first part is your iPhone's address on the Wi-Fi, so it will be different on your network.

Keep Everdisk open while devices are connected, because iOS pauses apps that sit in the background too long.

## Connect from a Mac

This is the smoothest case, because macOS speaks SMB natively.

The quickest way: open **Finder** and look in the sidebar under **Locations** or **Network**. Everdisk announces itself on the Wi-Fi, so your iPhone often appears there on its own. Click it, then click **Connect As** and choose **Guest**, or enter your login.

To connect by hand:

1. In Finder, choose **Go**, then **Connect to Server** (or press **Command and K**).
2. Type the SMB address shown in Everdisk, for example `smb://192.168.1.20:4455/Share`.
3. Click **Connect**, then pick **Guest** or enter your **Login** and **Password**.

Your iPhone opens in a Finder window. Copy files in or out by dragging, exactly like any other drive (if Files Editing is on).

## Connect from another iPhone or iPad

iOS and iPadOS can open SMB shares in the built-in **Files** app, which makes phone to phone transfers clean and quick.

On the second device:

1. Open the **Files** app.
2. Tap the **more** button (the three dots, top right on iPhone) and choose **Connect to Server**.
3. Enter the SMB address from Everdisk, for example `smb://192.168.1.20:4455/Share`.
4. Choose **Guest**, or **Registered User** and enter your login.
5. The share appears under Locations in Files. Browse and copy in either direction.

You can also use Everdisk's own **Devices** tab on the second device, which includes an SMB client. Open Everdisk, go to **Devices**, tap **New Connection**, choose **SMB**, and enter the address.

## Connect from Linux

1. Open your file manager (Files/Nautilus on GNOME, Dolphin on KDE).
2. Choose **Other Locations** or **Connect to Server**.
3. Enter the address, for example `smb://192.168.1.20:4455/Share`.
4. Connect as a guest, or enter your login.

From a terminal you can also run `smbclient //192.168.1.20/Share -p 4455` and enter your login when asked.

## Connect from Android

Android does not have a system SMB browser, so use a file manager that supports SMB:

1. Install an app such as **CX File Explorer**, **Solid Explorer**, or **X-plore File Manager**.
2. Add a new **SMB** or **LAN** connection.
3. Enter the host (your iPhone's Wi-Fi address), set the **port to 4455**, and the share name **Share**.
4. Connect as a guest or with your login, then browse and copy.

## Connect from Windows

Windows can read SMB shares, with one catch worth knowing up front. The built-in File Explorer only talks to SMB on the standard port and does not let you type a custom port in the path, and Everdisk uses port 4455. So the plain **Map network drive** route often will not reach it.

You have two good options on Windows:

- Use a file manager or SMB client that lets you set a custom port, and point it at your iPhone's address with port **4455** and the share name **Share**.
- Or connect from Windows using one of Everdisk's other servers instead. The [WebDAV setup](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) and [FTP setup](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) both work well from Windows File Explorer, and the browser link works in any browser.

If you do want to try Map network drive: open **File Explorer**, right-click **This PC**, choose **Map network drive**, and enter the host and share name shown in Everdisk. If it cannot connect, that is the port limitation above, so switch to WebDAV or FTP.

## Turn on encryption for untrusted Wi-Fi

SMB is the only Everdisk connection that can encrypt every transfer, which matters on Wi-Fi you do not fully control, like a cafe or an office network.

1. In **Settings**, **Sharing**, **Access**, set a **Login** and **Password**. Encrypted connections cannot be anonymous, so this step is required.
2. In **Settings**, **Sharing**, turn on **Require SMB Encryption**.
3. Stop and start sharing again so the change takes effect.

Every SMB transfer is then protected with **SMB3 encryption (AES)**. The connecting device needs to support SMB3, which the Finder on a modern Mac and Windows 10 or later both do. SMB Encryption is part of the one-time Premium purchase.

## Read only or read and write

The **Files Editing** switch in Settings, Sharing, Access controls this for every server, including SMB. Turn it on and connected devices can upload, rename and delete. Turn it off and they can only browse and copy files off your phone. Choose read only when you are handing files to someone you do not want changing anything.

## Real-life ways people use this

- **Move a big folder onto your iPhone from a Mac** by dragging it into the Finder window, faster than a web upload.
- **Pull a day of photos and videos off your phone** onto a laptop without iTunes or a cable.
- **Send files between two iPhones** through the Files app, with no third app on either side.
- **Work with a file in place**, opening a document straight from the phone in an app on your Mac and saving it back.

## A few tips

- Keep Everdisk open while a device is connected. Locking the phone for a long time can pause the app and drop the connection.
- If a Mac cannot see the phone in the Finder sidebar, connect by hand with Connect to Server and the full smb address.
- For the best speed on large transfers, keep photo and video quality on Original in Settings.
- On an untrusted network, turn on Require SMB Encryption and turn the other servers off while you work.

## Frequently Asked Questions

{{% details title="What is the SMB address and port for my iPhone?" closed="true" %}}
After you start sharing, Everdisk shows the address on the Sharing screen. It looks like smb://192.168.1.20:4455/Share. The 4455 is the port Everdisk uses for SMB, and Share is the name of the shared folder. The first part is your iPhone's address on the Wi-Fi, so yours will be different.
{{% /details %}}

{{% details title="Can I connect to my iPhone SMB share from Windows?" closed="true" %}}
Windows File Explorer only connects to SMB on the standard port and does not accept a custom port in the path, while Everdisk uses port 4455. So the plain Map network drive route often will not reach it. Use a file manager that lets you set a custom port, or connect from Windows with WebDAV, FTP or the browser link instead. All of those work from Windows without any port trouble.
{{% /details %}}

{{% details title="How do I share files between two iPhones with SMB?" closed="true" %}}
Start the SMB server on the first iPhone in Everdisk. On the second iPhone, open the Files app, tap the more button, choose Connect to Server, and enter the smb address shown in Everdisk (for example smb://192.168.1.20:4455/Share). Connect as Guest or with your login, and the share appears in Files. You can also use Everdisk's own Devices tab on the second phone.
{{% /details %}}

{{% details title="Does my iPhone show up in the Mac Finder sidebar automatically?" closed="true" %}}
Usually yes. Everdisk announces the SMB share on your Wi-Fi, so your iPhone often appears under Locations or Network in the Finder sidebar. Click it and choose Connect As, then Guest or your login. If it does not appear, connect by hand with Go, Connect to Server and the full smb address.
{{% /details %}}

{{% details title="Do I need a password to use SMB?" closed="true" %}}
No, a login is optional. Leave the Login and Password empty in Settings, Sharing, Access to allow guest access. Set them if you want connections to sign in. A login and password are required only if you turn on Require SMB Encryption, because encrypted connections cannot be anonymous.
{{% /details %}}

{{% details title="Is the SMB connection encrypted?" closed="true" %}}
It can be. SMB is the only Everdisk connection that supports encryption. Set a login and password, then turn on Require SMB Encryption in Settings, Sharing. Every transfer is then protected with SMB3 (AES). The other device needs to support SMB3, which modern Macs and Windows 10 or later do. Encryption is a Premium feature.
{{% /details %}}

{{% details title="Can people change or delete my files over SMB?" closed="true" %}}
Only if you allow it. The Files Editing switch in Settings, Sharing, Access controls this. With it on, connected devices can upload, rename and delete. With it off, the share is read only and others can browse and copy files off your phone but cannot change anything.
{{% /details %}}

{{% details title="Why did my SMB connection drop?" closed="true" %}}
Your iPhone is the server, and iOS pauses apps that stay in the background too long. Keep Everdisk open on screen while a device is connected, and plug the phone into power during long transfers. Also make sure both devices stayed on the same Wi-Fi.
{{% /details %}}

{{% details title="SMB, WebDAV or FTP, which should I use?" closed="true" %}}
Use SMB when you want the phone to behave like a real network drive on a Mac, another iPhone, Linux or a NAS, and when you want encryption. Use WebDAV when you want a network drive that also works well from Windows. Use FTP for the widest compatibility with older devices and apps. Everdisk can run all of them at once, so you are not locked into one.
{{% /details %}}

{{% details title="Is Everdisk free?" closed="true" %}}
Yes, Everdisk is free to download and the SMB server is included. The optional one-time Premium purchase adds SMB encryption, custom ports and a few other extras. You can set up SMB and share files without paying.
{{% /details %}}

Ready to try it? [Download Everdisk from the App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) and open your iPhone in Finder in about a minute. Questions or feedback? Email us at **support@everappz.com**.
