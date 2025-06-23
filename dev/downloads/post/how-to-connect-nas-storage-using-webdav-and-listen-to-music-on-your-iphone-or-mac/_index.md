# How to Connect NAS Storage Using WebDAV and Listen to Music on Your iPhone or Mac

**Writer:** admin  
**Date:** Jul 28, 2024  
**Updated:** Dec 6, 2024  
**Reading Time:** 2 min read

Discover how to connect your NAS storage using WebDAV and effortlessly stream your music library to your iPhone or Mac. WebDAV (Web-based Distributed Authoring and Versioning) is a protocol that allows you to manage and share files over the Internet. By setting up WebDAV on your NAS, you can access and stream your music collection, ensuring you always have your favorite tunes at your fingertips.

In this guide, we will show you how to set up a WebDAV connection on one of the most popular NAS servers, Synology NAS. Follow our simple steps to configure WebDAV on your Synology NAS, and you’ll be able to browse, stream, and manage your music library directly from your iPhone or Mac.

## Step 1: Install WebDAV on Synology NAS

1. Log in to your Synology NAS and open **Package Center**.
2. Search for “webdav” and install the WebDAV package if it’s not already installed. Open the WebDAV server to configure it.

![21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png]()

## Step 2: Configure WebDAV Server

1. On the WebDAV settings page, check the boxes for **Enable HTTP**, **Enable HTTPS**, **Enable Anonymous WebDAV**, and **Enable DavDepthInfinity**.
2. Click **Apply** to save changes. Note the port numbers for HTTP and HTTPS connections, which are 5005 and 5006 by default.

![21260c_61268a79aab046fdb50bf0e24495958b~mv2.png]()

## Step 3: Configure Shared Folder Permissions

1. Open the **Control Panel** and go to the **Shared Folder** section.
2. Select the **Music** folder and click **Edit**.
3. In the **Permissions** tab, configure the permissions. Enable guest access with Read-only if you just need to listen to music, or Read/Write if you need to modify files. Save the changes.

![21260c_599ebfa896164704ba4497524286ea58~mv2.png]()

## Step 4: Find Synology NAS IP Address

1. Open the **Control Panel** and go to the **Network Interface** tab, or use your web browser to visit [find.synology.com](http://find.synology.com).

![21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png]()

2. Note the IP address of your Synology NAS (e.g., 192.168.18.137).

![21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png]()

## Step 5: Connect to Synology NAS Using Evermusic/Flacbox

1. Open the Evermusic or Flacbox app and go to the **Connections** tab.

![21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png]()

2. For automatic connection, find your Synology NAS in the **Available Devices** section and tap it to connect.

![21260c_7536b0b169674a9199784da275b1cf6b~mv2.png]()

3. For manual connection, choose **Connect a cloud service** and select **WebDAV**. Enter the server address in the format: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (e.g., [https://192.168.18.137:5006](https://192.168.18.137:5006)).

![21260c_45ecc52850874ca18d7be50d086365fc~mv2.png]()

4. Leave the login and password fields empty for guest access, or enter your Synology credentials. Tap **Sign In**.

## Step 6: Navigate and Play Music

1. Once connected, the device will appear in the **Connected Devices** list.

![21260c_2cadbe057eed4e0eba098b767014de29~mv2.png]()

2. Navigate to the **Music** folder and tap any audio file to start playback.

![21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png]()

## Step 7: Add Connected Cloud Folder to Music Library

1. Open the **Music Library** section in the app.
2. Choose **Add Music** and select **Connections**.
3. Choose your connected NAS server and select the **Music** folder. Tap **Done**.
4. The app will scan the music folder and add supported audio files to the music library. Metadata will be loaded, and your tracks will be grouped by album, artist, and genre.

By following these steps, you can easily set up a WebDAV connection on your Synology NAS and stream your music library to your iPhone or Mac using Evermusic or Flacbox. Enjoy seamless access to your favorite tracks anytime.

---

**Tags:** [music](https://www.everappz.com/blog/tags/music), [streaming](https://www.everappz.com/blog/tags/streaming), [storage](https://www.everappz.com/blog/tags/storage), [nas](https://www.everappz.com/blog/tags/nas), [connect](https://www.everappz.com/blog/tags/connect), [webdav](https://www.everappz.com/blog/tags/webdav)

**Category:** [How To](https://www.everappz.com/blog/categories/how-to)