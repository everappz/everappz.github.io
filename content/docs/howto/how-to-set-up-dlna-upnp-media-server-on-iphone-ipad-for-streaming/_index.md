---
title: "How to Set Up a DLNA/UPnP Media Server on iPhone & iPad for Streaming"
description: "Turn your iPhone or iPad into a DLNA/UPnP media server with Everdisk and stream photos, videos and music to a smart TV, game console, VLC or Kodi over Wi-Fi. Full setup plus how to connect from Samsung, LG and Sony TVs, Windows, Mac, Linux, Android and another iPhone."
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "media server", "streaming", "smart tv", "iphone", "ipad", "wifi"]
keywords: ["DLNA server iPhone", "UPnP server iPad", "how to set up DLNA on iPhone", "stream to smart TV from iPhone", "DLNA media server iOS", "stream videos to TV without cable", "play iPhone photos on TV", "Samsung TV DLNA iPhone", "LG TV DLNA iPhone", "Sony Bravia DLNA iPhone", "VLC DLNA iPhone", "Kodi DLNA media server", "UPnP AV media server iOS", "stream music to TV from iPhone", "iPhone media server app"]
readingTime: 9
aliases:
  - /post/how-to-set-up-dlna-upnp-media-server-on-iphone-ipad-for-streaming/
---

{{< author-byline >}}

DLNA (also called UPnP AV) is the quiet workhorse behind most smart TVs. It is a shared language that lets a TV or media player find a media library on the same Wi-Fi and play from it, with nothing to install on the TV. If your iPhone or iPad can act as that library, your photos, videos and music show up on the big screen on their own.

This guide shows how to turn your iPhone or iPad into a DLNA/UPnP media server using [Everdisk](/products/everdisk), and how to open that library from a smart TV, a game console, VLC, Kodi, a computer, an Android phone, and even a second iPhone. Everything runs over your local Wi-Fi, so nothing is uploaded anywhere.

## What you need

- An iPhone or iPad with [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installed.
- A TV, player or computer on the **same Wi-Fi network** as your device.
- The photos, videos or music you want to play, already on your iPhone (in the Photos app, the Music app, or the Everdisk Documents folder).

## Set up the DLNA server in Everdisk

### Step 1: Choose what to share

Open Everdisk and go to the **Sharing** tab. Tap **What to Share** and pick your content:

- Turn on **Allow access to all Photos Library** to share every album, or tap **Add Photos** to pick a few.
- Turn on **Allow access to all Music Library** to share your songs, or tap **Add Tracks** for a selection.
- Add any folders or files with **Add Folder** and **Add File**. The app's own Documents folder is shared by default.

You need at least one item selected before sharing can start.

### Step 2: Turn on TV & Media Center (DLNA)

Go to **Settings**, then **Sharing**, then **Connections**. Make sure **TV & Media Center** is on. It is on by default and carries the DLNA tag. This is the server that TVs and players look for.

### Step 3: Start sharing

Back on the **Sharing** tab, tap the big **Start** button. Your device is now a media server on your Wi-Fi. It appears to other devices under its friendly name, the one shown as your device name in the app (something like "Speedy-Hare" until you change it).

DLNA streaming is always open, so there is no password to enter on the TV. Keep Everdisk open on screen while you watch, because iOS pauses apps that are pushed fully into the background.

## Play on a smart TV

This is the most common case, and it usually takes about thirty seconds.

1. Put the TV on the **same Wi-Fi** as your iPhone.
2. Open the TV's built-in media player. The name depends on the brand: **Media Player**, **Gallery**, **SmartShare** (LG), **AllShare** or **SmartThings** (Samsung), **Content Share**, or **SimplyShare**.
3. Look for the list of media servers or sources. Your device appears there by its name.
4. Select it, browse into your photos, videos or music, and press play.

Preview thumbnails show up automatically, so you can find the right holiday album or movie without guessing.

### Which TVs work

Most TVs from **Samsung, LG, Sony BRAVIA, Panasonic (VIERA firmware), Philips and Hisense** have DLNA built in and work right away. **PlayStation and Xbox consoles and most AV receivers** do too.

A few platforms leave it out: **Roku TVs, Amazon Fire TV, Vizio SmartCast, and plain Google TV** without a maker's media app. If your TV is one of these and cannot find your device, that is usually the reason. On those TVs, install a DLNA player app such as VLC or Kodi, or reach your files through a web browser instead using the [WebDAV setup guide](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/).

Some brands kept DLNA working even after removing the official DLNA logo, so if it looks missing, hunt for one of the media player names above.

## Play in VLC or Kodi on Windows, Mac and Linux

VLC and Kodi are free, run on every desktop system, and speak DLNA well. They are the reliable way to open your Everdisk library on a computer.

**VLC (Windows, Mac, Linux):**

1. Open VLC.
2. Show the playlist (on Windows and Linux press **Ctrl+L**, on Mac open the **Playlist** from the View menu).
3. In the sidebar, open **Universal Plug'n'Play** under Local Network.
4. Your device appears in the list. Click into it and pick a file.

**Kodi (Windows, Mac, Linux):**

1. Go to **Videos**, **Music** or **Pictures**, then **Files**, then **Add source** (or **Browse**).
2. Choose **UPnP devices**.
3. Select your device and browse your library.

On Windows you can also open **Windows Media Player**, expand **Other Libraries** in the sidebar, and your device shows up there.

## Play on Android

Android phones and tablets do not have a system DLNA browser, so use an app:

- **VLC for Android**: open the side menu, tap **Local Network**, and your device appears under UPnP servers.
- **BubbleUPnP** or a similar UPnP app: your device shows up in the server list, and these apps can also push playback to a TV.

## Play on another iPhone or iPad

Two devices, one library. Say the photos are on your iPhone and you want to watch them on your iPad.

- The simplest route is Everdisk's own **Devices** tab on the second device. It works as a DLNA client as well as a server. Open Everdisk on the iPad, go to **Devices**, and your iPhone appears under **Available Devices**. Tap it to browse and play.
- Any DLNA player app for iOS works too, such as VLC or a UPnP browser. Open its local network view and pick your iPhone.

## Play on a game console

- **PlayStation 5 and 4**: open the **Media** app (Media Gallery), and your device shows up as a media server you can browse.
- **Xbox**: use a media player app that supports DLNA, then pick your device from the server list.

## If your device does not appear in the list

Some players let you add a media server by address instead of waiting for it to be discovered. On the Everdisk **Sharing** screen, the DLNA card shows a device description address that ends in `/device-desc.xml`. Enter that address in the player's add server field.

If it still does not show up, check three things: both devices are on the same Wi-Fi (not a guest network that blocks device to device traffic), Everdisk is open and sharing is started, and **TV & Media Center** is on in Settings.

## If a video will not play

DLNA hands the file to the TV as it is, and the TV has to be able to decode it. If a clip refuses to play, its format is probably not supported by that TV. Two fixes:

- Open **Settings**, then **Sharing**, then **Videos**, and lower the **Quality**. Everdisk then converts the video to a more compatible format as it streams. (Conversion is a Premium feature.)
- Or open the same file in a web browser using Everdisk's browser link, which is more forgiving about formats.

## Real-life ways people use this

- **Family movie night.** Videos shot on your phone play on the living room TV without a cable or an Apple TV.
- **Holiday photos on the big screen.** Open your Photos library on the TV and swipe through the trip with everyone in the room.
- **Background music at a party.** Point a DLNA speaker or AV receiver at your Music library and let it run.
- **Watching on a hotel TV** that has a media player, once both devices are on the room's Wi-Fi.

## A few tips

- Keep Everdisk open while you stream. If you lock the phone for a long time, iOS may pause the app and playback stops.
- Plug the phone into power for long movie sessions.
- For the fastest streaming, keep **Format** and **Quality** on **Original** in Settings, and only lower them if a specific TV struggles with a file.
- DLNA is streaming only. Nobody on the TV side can change or delete your files. For two-way file transfer, use the [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/), [WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) or [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) server instead.

## Frequently Asked Questions

{{% details title="What is the difference between DLNA and UPnP?" closed="true" %}}
They are closely related. UPnP is the underlying networking standard, and DLNA is the media profile built on top of it that TVs and players use to share and play photos, videos and music. In everyday use the words are interchangeable. When you turn on TV & Media Center in Everdisk, your device becomes a DLNA/UPnP media server that any DLNA client can browse.
{{% /details %}}

{{% details title="Do I need to install anything on my TV?" closed="true" %}}
No. If your TV supports DLNA, it already has a media player that can find your device on the Wi-Fi. You only install Everdisk on the iPhone or iPad that holds the content. If your TV does not support DLNA, install a player like VLC or Kodi on a device connected to it.
{{% /details %}}

{{% details title="Why does my iPhone not show up on the TV?" closed="true" %}}
Check that both devices are on the same Wi-Fi network. Guest networks and some office or hotel networks block devices from seeing each other, which stops DLNA. Then confirm Everdisk is open with sharing started, and that TV & Media Center is on in Settings, Sharing, Connections. If the TV still cannot find it, add the server by hand using the device description address that ends in /device-desc.xml.
{{% /details %}}

{{% details title="Does DLNA streaming need a password?" closed="true" %}}
No. DLNA is always open to anyone on the same Wi-Fi while it is on, which is why there is no login on the TV side. That is fine on a home network you trust. On a network you do not trust, turn TV & Media Center off when you are done, or use the SMB server with encryption instead.
{{% /details %}}

{{% details title="Can I stream to a Chromecast or Roku?" closed="true" %}}
Chromecast and Roku do not act as DLNA players out of the box, so they will not find your device directly. The workaround is to install a DLNA app that can cast, such as VLC or BubbleUPnP on a phone, and push playback to the Chromecast or Roku from there. On most other smart TVs, DLNA works without any of this.
{{% /details %}}

{{% details title="A video plays with no sound or will not open. What can I do?" closed="true" %}}
That is a format the TV cannot decode. Open Settings, Sharing, Videos in Everdisk and lower the Quality so the app converts the video to a more compatible format as it streams. You can also open the same file through the browser link, which handles more formats.
{{% /details %}}

{{% details title="Can I stream music, not just video?" closed="true" %}}
Yes. Turn on Allow access to all Music Library, or add specific tracks, then start sharing. Your songs appear on any DLNA speaker, AV receiver or TV, with artwork and track details. Music is always shared in its original quality.
{{% /details %}}

{{% details title="Does the app have to stay open while I watch?" closed="true" %}}
Yes. Your iPhone is acting as the server, and iOS pauses apps that are pushed fully into the background for a long time. Keep Everdisk on screen while you stream, and plug into power for long sessions.
{{% /details %}}

{{% details title="How do I stream from one iPhone to another iPad?" closed="true" %}}
Start sharing on the iPhone, then open Everdisk on the iPad and go to the Devices tab. The iPhone appears under Available Devices as a media server. Tap it to browse and play. Everdisk works as a DLNA client and a server, so you do not need another app.
{{% /details %}}

{{% details title="Is Everdisk free?" closed="true" %}}
Yes, Everdisk is free to download and the DLNA media server is included. An optional one-time Premium Lifetime purchase adds extras like photo and video conversion for older TVs, custom ports and more. You can set up and use DLNA streaming without paying.
{{% /details %}}

Ready to try it? [Download Everdisk from the App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) and stream your first album to the TV in a couple of minutes. Questions or feedback? Email us at **support@everappz.com**.
