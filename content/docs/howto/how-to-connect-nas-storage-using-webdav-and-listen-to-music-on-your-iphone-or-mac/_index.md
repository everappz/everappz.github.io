---
title: "How to Connect NAS Storage Using WebDAV and Listen to Music on Your iPhone or Mac"
date: 2024-07-28
description: "Learn how to configure WebDAV on your Synology NAS and stream music to your iPhone or Mac using Evermusic or Flacbox. Follow our step-by-step guide."
keywords: ["connect nas", "webdav synology", "stream music nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["music", "streaming", "storage", "nas", "connect", "webdav"]
readingTime: 2
draft: false
aliases:
  - /post/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/
---

Discover how to connect your NAS storage using WebDAV and effortlessly stream your music library to your iPhone or Mac. WebDAV (Web-based Distributed Authoring and Versioning) is a protocol that allows you to manage and share files over the Internet. By setting up WebDAV on your NAS, you can access and stream your music collection, ensuring you always have your favorite tunes at your fingertips.

In this guide, we will show you how to set up a WebDAV connection on one of the most popular NAS servers, Synology NAS. Follow our simple steps to configure WebDAV on your Synology NAS, and you’ll be able to browse, stream, and manage your music library directly from your iPhone or Mac.

## Step 1: Install WebDAV on Synology NAS

1. Log in to your Synology NAS and open **Package Center**.
2. Search for “webdav” and install the WebDAV package if it’s not already installed. Open the WebDAV server to configure it.

{{< figure src="/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Install WebDAV on Synology" width="600" >}}

## Step 2: Configure WebDAV Server

1. On the WebDAV settings page, check the boxes for **Enable HTTP**, **Enable HTTPS**, **Enable Anonymous WebDAV**, and **Enable DavDepthInfinity**.
2. Click **Apply** to save changes. Note the port numbers for HTTP and HTTPS connections, which are 5005 and 5006 by default.

{{< figure src="/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Configure WebDAV settings" width="600" >}}

## Step 3: Configure Shared Folder Permissions

1. Open the **Control Panel** and go to the **Shared Folder** section.
2. Select the **Music** folder and click **Edit**.
3. In the **Permissions** tab, configure the permissions. Enable guest access with Read-only if you just need to listen to music, or Read/Write if you need to modify files. Save the changes.

{{< figure src="/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Shared Folder Permissions" width="600" >}}

## Step 4: Find Synology NAS IP Address

1. Open the **Control Panel** and go to the **Network Interface** tab, or use your web browser to visit [find.synology.com](http://find.synology.com).

{{< figure src="/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Find NAS IP Address" width="600" >}}

2. Note the IP address of your Synology NAS (e.g., 192.168.18.137).

{{< figure src="/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Synology NAS IP address" width="600" >}}

## Step 5: Connect to Synology NAS Using Evermusic/Flacbox

1. Open the Evermusic or Flacbox app and go to the **Connections** tab.

{{< figure src="/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Connections Tab in Evermusic" width="600" >}}

2. For automatic connection, find your Synology NAS in the **Available Devices** section and tap it to connect.

{{< figure src="/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Available Devices List" width="600" >}}

3. For manual connection, choose **Connect a cloud service** and select **WebDAV**. Enter the server address in the format: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (e.g., [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Manual WebDAV Configuration" width="600" >}}

4. Leave the login and password fields empty for guest access, or enter your Synology credentials. Tap **Sign In**.

## Step 6: Navigate and Play Music

1. Once connected, the device will appear in the **Connected Devices** list.

{{< figure src="/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Connected Devices in Evermusic" width="600" >}}

2. Navigate to the **Music** folder and tap any audio file to start playback.

{{< figure src="/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Browsing Music Folder" width="600" >}}

## Step 7: Add Connected Cloud Folder to Music Library

1. Open the **Music Library** section in the app.
2. Choose **Add Music** and select **Connections**.
3. Choose your connected NAS server and select the **Music** folder. Tap **Done**.
4. The app will scan the music folder and add supported audio files to the music library. Metadata will be loaded, and your tracks will be grouped by album, artist, and genre.

## Conclusion

By following these steps, you can easily set up a WebDAV connection on your Synology NAS and stream your music library to your iPhone or Mac using Evermusic or Flacbox. Enjoy seamless access to your favorite tracks anytime.