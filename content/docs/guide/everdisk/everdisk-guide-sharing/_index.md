---
title: "Sharing"
date: 2025-09-03
description: "Learn how sharing works in Everdisk: tap Start to turn your iPhone or iPad into a wireless drive, choose what to share (files, folders, photos and music), run the four servers (DLNA, HTTP, WebDAV, FTP), read the connection addresses, see who is connected, and keep sharing running over Wi-Fi or a USB cable."
keywords: [
  "Everdisk sharing", "wireless drive iPhone", "start sharing", "share files iPhone",
  "share photos over network", "DLNA HTTP WebDAV FTP", "what to share",
  "how to connect", "keep app open", "Wi-Fi or USB cable sharing"
]
tags: ["everdisk", "guide", "sharing"]
readingTime: 9
aliases:
  - /guide-everdisk-sharing/
---


The **Sharing** tab is the heart of Everdisk. It is where you turn your iPhone or iPad into a wireless drive, choose exactly what you want to share, and get the addresses other devices use to connect. This is the first tab you see when you open the app.

## Start and stop sharing

In the middle of the Sharing screen is a large round button.

- Tap **Start** to bring all of your enabled servers online at once. The button shows **Starting...**, then **Stop** once sharing is live.
- Tap **Stop** to take everything offline again. Connected devices are disconnected.

While sharing is running, your chosen files, photos and music are available to any device on the same network that connects using one of the four methods below.

> Sharing runs only while the app is open. See **Keep the app open** near the end of this page for why, and how to keep large transfers going.

## Choose what to share

Before you start, tap the **What to Share** header to open three groups. You can share any mix of them, and you must choose at least one thing before sharing can start.

**Files and Folders**

- Your app's own **Documents** folder is shared by default. You can stop sharing it if you prefer.
- Tap **Add Folder** to share a folder from anywhere on your device, or **Add File** to share individual files.
- Each shared item has an **Info** button and a **Stop Sharing** button.

**Photos and Videos**

- Turn on **Allow access to all Photos Library** to share your whole photo and video library, or
- Tap **Add Photos** to hand-pick only the photos and videos you want to share.

**Music**

- Turn on **Allow access to all Music Library** to share your whole music library, or
- Tap **Add Tracks** to share only selected songs.
- Tracks that are protected (DRM) or stored only in the cloud can't be shared.

If you try to start with nothing selected, Everdisk shows a **Nothing to Share** note. If you change what is shared while sharing is running, **Stop and Start again** to apply the change.

## The four servers

Everdisk shares the same content four ways at once. Each one is designed for a different kind of device, and each can be turned on or off in **Settings → Sharing → Connections**. By default all four are on.

- **TV & Media Center (DLNA)** - for smart TVs and media players. They discover your device by itself and show your photos, videos and music, with preview thumbnails.
- **Browser (HTTP)** - for any phone, tablet or computer. The other person opens a link in a web browser to browse and download your files. Nothing to install.
- **Computer (WebDAV)** - for a Mac, Windows PC or Linux machine. Your device appears as a normal network drive so you can drag files in both directions.
- **Other Apps & Devices (FTP)** - for file apps and power users that speak FTP.

For step-by-step connection instructions for each type, see [Connect Your Devices](/docs/guide/everdisk/everdisk-guide-connect).

## How to Connect and connection addresses

After you tap Start, the **How to Connect** section shows a card for each active server with the exact **address** to type on the other device. Each address is easy to copy - tap it to copy, use the **Share** button to send it, or tap the **info (ⓘ)** button for detailed, per-protocol instructions.

- The DLNA card shows a device-description address that ends in `/device-desc.xml` for players that ask for one.
- When your device is plugged into a Mac with a cable, an extra address appears with a **Cable Connection** badge that uses your device's `.local` name.

You can also open the address as a **QR code** so another device's camera can jump straight to it.

## Who is connected

The **Who is Connected** section lists the devices currently connected to you in real time. Tap the more-actions button next to any device to **Block this device** if you don't recognize it. Blocked devices are managed in [Access & Privacy](/docs/guide/everdisk/everdisk-guide-access).

## Your device name and avatar

Every device has a friendly name (like "Speedy-Hare") and a colored avatar. This is the name a TV, computer or other app shows for your device on the network, so it is easy to pick out. You can regenerate the name and avatar for free, or set a custom name, icon or photo avatar with Premium. See [Settings](/docs/guide/everdisk/everdisk-guide-settings).

## Sharing over Wi-Fi or a USB cable

Sharing can run in two situations:

- **Over Wi-Fi** - your device and the other devices are on the same Wi-Fi network.
- **Over a USB cable** - your device is plugged into a **Mac** with a cable, even when there is no Wi-Fi at all. This is faster than Wi-Fi and keeps working on a plane, in a hotel, or on a locked network.

If neither Wi-Fi nor a cable is available, the **Start** button is disabled and a **No Wi-Fi Connection** note appears. If the connection drops while sharing, Everdisk stops sharing automatically and lets you know. Tap the info button on any of these notes for a full explanation.

## Keep the app open

Because your iPhone or iPad is acting as the server, **sharing works only while Everdisk is open on screen**. If you close the app or lock the device for a long time, the system can pause the app and sharing stops.

For large transfers:

- Keep Everdisk open and in the foreground.
- Plug your device into power.
- Set **Auto-Lock** to **Never** in the iOS Settings app while you transfer.

You can turn on **Notify before disconnecting** (in Settings → Sharing) so Everdisk reminds you to reopen the app before the system suspends it. Tap the info button on the **Keep the app open** banner for more detail.

## Next steps

- [Connect Your Devices](/docs/guide/everdisk/everdisk-guide-connect) - connect a TV, computer, browser, phone, or USB cable.
- [Access & Privacy](/docs/guide/everdisk/everdisk-guide-access) - add a password and control editing.
- [Settings](/docs/guide/everdisk/everdisk-guide-settings) - turn servers on or off and tune quality.
