---
title: "Connections"
date: 2020-02-01
aliases:
  - /post/flacbox-guide-connections/
  - /guide-flacbox-connect/
description: "Learn how to connect cloud services and NAS devices to Flacbox. Stream high-resolution music from iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk, and more. Use SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder File Sharing, and USB flash drives."
keywords: [
  "Flacbox cloud setup", "connect Google Drive to Flacbox", "SMB music streaming",
  "WebDAV iOS player", "DLNA music app", "NAS audio streaming", "Wi-Fi Drive iPhone",
  "transfer files to iPhone", "Flacbox iTunes File Sharing", "connect NAS to iPhone",
  "Synology Drive music app", "QNAP music app", "Bluesound music app",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "Last.fm scrobbling music app",
  "iXpand Flash Drive music", "USB DAC iPhone"
]
tags: ["guide", "flacbox", "connections", "cloud", "NAS"]
readingTime: 12
---


On this screen, you can connect every source that holds your music. You can integrate popular cloud services like **Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive,** and many more, as well as your **Mac, PC, or NAS** over standard protocols. Whether your collection lives on a streaming-friendly service like Dropbox or on a personal NAS like a Synology, QNAP, Buffalo, **Apple Time Capsule**, or **WD My Cloud Home**, Flacbox connects to them all from a single screen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Connections Screen" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Connect to Cloud Storage

- Open the **Connections** tab.
- Select **Connect to cloud storage** from the menu.
- Choose a cloud storage service from the list.
- Enter your credentials on the official authorization page provided by the cloud provider, then tap **Done**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Add a Cloud Storage Service" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

If you encounter any issues, check your internet connection and your login / password. In the **Premium** version of the app, you can add an unlimited number of services; the free version supports up to three.

## Supported Cloud Storage Services, Media Servers, and Protocols

Flacbox supports an exceptionally wide range of sources for your music. Everything below works from a single **Connect to cloud storage** screen.

**Personal cloud storage:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Self-hosted servers and music-server APIs:** **Plex** · **Jellyfin** · **Emby** · **Subsonic** (and every Subsonic-compatible server — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · **Navidrome** · Nextcloud (and ownCloud via the shared API) · **Synology Drive** · **QNAP**.

**NAS and file-share protocols:** **SMB** (SMB1, SMB2, Auto) · **WebDAV** (HTTP / HTTPS) · **FTP / FTPS** · **SFTP** (SSH File Transfer Protocol, password or public-key auth) · **NFS** · **DLNA / UPnP** (playback and download).

**S3-compatible object storage:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, and any other S3-API endpoint.

**Local-network discovery:** the **Available Devices** section auto-lists every Bonjour / mDNS service on your Wi-Fi network so you can tap to connect without typing an IP address.

Each connection uses the **official SDK or open protocol** of the service, with OAuth-based authorization where supported. You can connect multiple accounts of the same service (for example, two Google Drive accounts, a personal Dropbox alongside a work one, or both a Plex and a Jellyfin server) and browse them side-by-side in the Connections screen.

## Security and Privacy

We use only **official SDKs and secure connections** to interact with connected cloud services. Your login and password are not accessible to the application — all transfers are TLS-encrypted.

When you enter your login and password, the application shows you the **official authorization page provided by the cloud service provider**, and the entire authorization process takes place outside the application. The cloud service provider then sends an **auth-token** to the application after successful authorization, and that token is used to make API calls.

An auth-token is a digital key that allows third-party applications to interact with cloud storage on your behalf. The token is stored on your device in **Apple’s secure system storage (Keychain)**, which is encrypted at rest and protected by your device passcode or biometric lock. You can download files from connected cloud services to your device; those files are placed in the app’s **Documents** directory and can be removed at any time using the built-in file manager.

The application **does not share any information** from your connected cloud accounts with Everappz, advertisers, or any third party. You can revoke access to your cloud account at any time by opening the account-settings page in your web browser.

## Reject Auth-Token

To revoke an auth-token, log in to your cloud account in a web browser and navigate to the security or connected-apps page. There you can find every third-party app that is connected to your cloud account and remove any of them if you no longer want to use it. Detailed instructions for Google accounts are available [here](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

You can also disconnect the cloud account inside the application itself — when you do, the auth-token is immediately deleted from your device. If you uninstall the application from your device, all downloaded data and access tokens are removed automatically along with it.

## Disconnect a Cloud Storage or Change Configuration

- **Access cloud-storage options** — locate the connected service in the **Connections** screen.
- **Tap the "..." button** next to the service title to open additional options:
  - **Rename** — change the name of the cloud service as it appears in your list.
  - **Settings** — modify the configuration or authentication data. Sometimes you may need to re-authorize the connected cloud service if the authorization token has expired.
  - **Disconnect** — completely sever the connection between the app and the cloud service. This removes all songs associated with that service from your app’s music library, but it leaves them untouched on the server.

## Connect to a Computer or NAS

You can also connect your computer, personal NAS, or other network devices using the **SMB**, **DLNA**, or **WebDAV** protocols. This is the easiest way to bring an existing home music library — whether it lives on a Mac, a Windows PC, a Synology box, or a NAS — into Flacbox without copying anything.

## Connect to a Computer Using SMB

- Tap **Connect to cloud storage → SMB**.
- Enter the computer’s IP address and shared folder name in the URL field using the format `smb://computer-ip-address/shared-folder-name`.
- Choose the protocol version: **Auto**, **SMB1**, or **SMB2**.
- Enter your login and password (if required).
- Tap **Done**.

If the connection is successful, you will see the connected storage in the **Cloud Storage** section. A full tutorial on how to connect your Mac or PC using SMB is available [here](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Connect to a NAS Using WebDAV

All steps are the same as SMB, except for the URL field. The URL should be in the format `http://server-name` or `https://server-name` if the server supports SSL. WebDAV works with **Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home, Buffalo,** and many other servers — anywhere a WebDAV endpoint is available.

A full tutorial on how to connect a NAS using WebDAV is available [here](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Connect to a Computer or NAS Using DLNA

You can also share a music library located on your Windows PC or personal NAS using the **DLNA / UPnP** protocol and access that library in the app as described [here](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA is a popular, widely supported protocol, but it only allows you to play or download music — you cannot upload files or create new folders on a DLNA server.

## Connect to a NAS or Server Using FTP, FTPS, or SFTP

Flacbox also supports the classic file-transfer protocols. To connect a server over **FTP** or **FTPS**, tap **Connect to cloud storage → FTP**, enter the host URL in the form `ftp://server-name` (or `ftps://server-name` for an encrypted connection), provide your login and password, then tap **Done**. For **SFTP (SSH File Transfer Protocol)**, choose **SFTP** instead and supply either a password or an SSH key pair. Both work with NAS devices, Linux hosts, and any server that has an FTP / FTPS / SSH daemon.

## Connect to an NFS Share

Flacbox includes **NFS (Network File System)** support — handy for Linux hosts, BSD servers, and NAS devices that prefer to expose music libraries over NFS instead of SMB. Pick **NFS** in the **Connect to cloud storage** menu, enter the server address and exported path, and tap **Done**.

## Connect a Plex Media Server

Flacbox can connect directly to a **Plex Media Server** and browse your music library by Artists, Albums, Genres, and Playlists. Tap **Connect to cloud storage → Plex**, sign in with your Plex account, pick a server, and the library appears alongside your cloud services. Plex servers on the same local network are also discovered automatically in the **Available Devices** section.

## Connect a Jellyfin or Emby Server

Both **Jellyfin** (open-source) and **Emby** (commercial) media servers work natively in Flacbox. Tap **Connect to cloud storage → Jellyfin** or **Emby**, enter your server URL (something like `http://server-ip:8096`) and credentials, and your music library is ready to stream. As with Plex, libraries on the local network are listed automatically in **Available Devices**.

## Connect a Subsonic or Navidrome Server

Flacbox speaks the **Subsonic API**, which means it works with **Subsonic** itself, **Navidrome**, and every other Subsonic-compatible server — including **Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS),** and **Ampache**. Tap **Connect to cloud storage → Subsonic**, enter the server URL and credentials, and the library appears in the Connections screen. This is the easiest way to give Flacbox access to a self-hosted music collection without exposing the underlying file share.

## Connect to S3-Compatible Object Storage

For self-hosters and audiophiles using cloud object storage, Flacbox includes an **S3-compatible** connector. Tap **Connect to cloud storage → S3 storage**, then enter the endpoint URL, region, access key, secret key, and bucket name. This works with **AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces,** and any other service that exposes an S3-API endpoint.

## Available Devices

This section displays every device on your local network that you can connect to from Flacbox via Bonjour discovery. To establish a connection, follow these steps:

- Open the app and go to the **Available Devices** section under Connections.
- Tap the device you want to connect to.
- If needed, enter your login details to complete the connection.

This is the fastest way to discover an SMB, WebDAV, DLNA, or **Bluesound Vault** share on your home network without typing IP addresses manually.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Available Devices on the Local Network" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

**Wi-Fi Drive** is a convenient technology that enables wireless file transfers from your computer to your iOS device via any desktop browser. To use this feature effectively, ensure that your device and computer are connected to the same Wi-Fi network. Here is a step-by-step guide on how to use Wi-Fi Drive.

### Enable Wi-Fi Drive

- Open the application and go to the **Connections** tab.
- Select **Connect via Wi-Fi** to access the Wi-Fi Drive main screen.
- (Optional) Set a username and password for the embedded web server to protect access.
- Tap **Start Wi-Fi Drive** to enable Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Access Wi-Fi Drive on Your Computer

- On your computer (desktop or laptop), open a web browser (such as Chrome, Firefox, or Safari).
- In the browser’s address bar, enter the URL provided by the application.

### Transfer Files Wirelessly

Once the web page corresponding to your iOS device opens in the browser, you can easily **drag and drop** files from your computer onto the web page. The files you drop will begin transferring to your iOS device and will be accessible inside Flacbox.

You can also mount Wi-Fi Drive directly in **Finder** on macOS (Go → Connect to Server…) or **File Explorer** on Windows (Map Network Drive…) and treat your iPhone or iPad as a regular network drive.

Detailed instructions on how to transfer files wirelessly using Wi-Fi Drive are available [here](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

**iTunes File Sharing** (now **Finder File Sharing** on macOS Catalina and later) is another way to transfer files from a computer to a device using a Lightning or USB-C cable.

- Connect the device to the computer using a cable and run **Finder** on Mac (or **iTunes** on Windows).
- Open **Locations → Your Connected Device → Files** and find the Flacbox app.
- Tap on the app icon to see all shared folders.
- Copy files from the computer to the shared folder on the device using drag-and-drop.

Detailed instructions on how to use Finder File Sharing are available [here](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Connect a USB Flash Drive

If you have an SD card or USB drive, you can connect it using a **Lightning to USB / SD Card Reader** or a USB-C drive (on iPad and iPhone 15 / 16 / 17 / Pro). The app supports **Apple Certified card readers** and **iXpand Flash Drives**. With an iXpand Flash Drive, insert it into the Lightning port and open the application — you’ll see an **External Device Connected** message and the device information. Tap the flash drive icon to access the music folder and tap any audio file to start playing.

We have detailed instructions on how to connect a USB flash drive to your iPhone and listen to music or manage files located on it [here](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## File Manager

Once you’ve connected a cloud storage service, tap its icon to view all available files and folders. You can use the built-in file manager to work with these files — download, rename, move, upload, delete, and more. When you start a download, the file appears in the **transfer queue**. To open the transfer queue, go to the **Local Files** tab and tap the spinning-arrows icon in the top-left corner. All downloaded files and folders are available in the **Local Files** section.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Browsing Folders on a Connected Cloud Service" image="/docs/guide/flacbox/img/connected-device-folders.webp" >}}
{{< /cards >}}

## Top Toolbar

The top toolbar, conveniently located under the navigation bar, offers several useful actions for easy access. You can show or hide it with a simple swipe-down gesture.

- **Search** — perform a quick search within the current directory, making it effortless to locate specific files or folders.
- **Continue Playback** — if enabled in the application settings, this restores the audio player queue and the last media position for the current folder. A handy way to pick up where you left off.
- **Play All** — scans the current folder and its subfolders, then adds all found audio files to a new player queue. Useful when you want to play every track in a directory.
- **Shuffle All** — like **Play All**, but shuffles the files before adding them to the audio player queue. Great for rediscovering an old folder of music.

## Folder Options

When you open a folder, you’ll find a handy set of actions available by tapping the **"..."** button in the top right corner.

- **Select** — activate file-selection mode. This lets you choose one or more files within the folder and perform actions on the whole selection.
- **New Folder** — create a new folder in the current folder. Great for keeping your library well-structured.
- **Enable Offline Mode** — toggle on offline mode for the current folder. Offline mode goes beyond simple downloading: it actively monitors the folder for changes. If you add new files online, they’ll automatically appear on your device.
- **Upload Files** — upload files from your device to the online folder. This makes them accessible from anywhere via the same cloud service.
- **Search** — search for specific files within the current folder.
- **Sort** — sort files by name, size, date modified, or by metadata. The default sort mode mirrors the sort order on the server, but you can change it to suit your preferences.
- **Grid / List View** — switch between table view and thumbnail view. Table view shows a compact list; thumbnail view shows large artwork previews for quick visual identification.

## Edit Online Files

When you need to manage multiple files in your cloud storage, use **Selection Mode** to streamline your actions:

- **Activate Selection Mode** — tap the **"..."** button in the top-right corner and choose **Select**.
- **Choose Files** — checkboxes appear next to every file and folder. Tap to select one or several items.
- **Perform Actions** — once you’ve selected the files or folders, you’ll have access to **Play Next, Play Later, Add to Music Library, Add to a Playlist, Copy, Upload, Move, Rename,** and **Delete**.

If you’d rather treat connected cloud storage as read-only (to prevent accidental deletions), enable **Settings → File Manager → Edit Online Files → Off** to hide all destructive operations from the UI.

## File Actions

Tap the **"..."** icon near a file’s title to reveal its actions menu:

- **Play Next** — insert the file at the top of the player queue, so it plays right after the current track.
- **Play Later** — append the file to the bottom of the player queue.
- **Add to Music Library** — incorporate the file into your music library, organized by artist, album, genre, or composer.
- **Add to a Playlist** — add the file to an existing playlist or create a new one.
- **Edit Audio Tags** — open the built-in tag editor to modify metadata. For online files, the track is temporarily downloaded, edited, and then re-uploaded after you confirm.
- **Add to Favorites** — add the file to your favorites list for quick access.
- **Download** — download the file or folder to your device for offline use.
- **Rename** — rename the file directly on the remote storage.
- **Move** — relocate the file to a different folder within your cloud storage.
- **Open In** — export the file to another compatible app. The file is downloaded to your device, then the system Share sheet appears.
- **Delete** — permanently remove the file from your cloud storage. **This action cannot be undone.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox More Actions for a File in Connected Cloud Storage" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

If the list of actions exceeds the available screen space, simply scroll down within the actions menu to access additional options.

## Folder Actions

For each folder in your cloud storage, you have a wide variety of actions available by tapping the **"..."** icon next to the folder title. If you don’t see all the actions, scroll down to reveal more.

- **Play All** — replace the current player queue with every item in the selected folder.
- **Play Next** — add the entire folder to the top of the player queue.
- **Play Later** — append the folder contents to the bottom of the player queue.
- **Add to Music Library** — incorporate the folder’s content into your music library.
- **Add to Playlist** — add the entire folder to a playlist. You also have the option to create a new playlist; its name is auto-populated from the folder name.
- **Add to Favorites** — add the folder to your favorites for quick access.
- **Enable Offline Mode** — beyond a simple download, this continuously monitors the folder for new files and auto-downloads them as they appear online.
- **Download** — download all contents of the folder to your device for offline access.
- **Rename** — rename the folder directly on the remote storage.
- **Move** — relocate the folder to a different location within your cloud storage.
- **Archive (ZIP)** — bundle the folder contents into a single ZIP file (Premium feature).
- **Delete** — permanently remove the folder and its contents from your cloud storage. **This action cannot be undone.**

## Quick Access

The **Quick Access** section is located at the top of the screen. It gives you fast access to your favorite and recently opened files from connected cloud services. Whenever you open a file or folder from the cloud, it’s added to the **Recently Opened** list. To clear this list, open **Recents**, tap the **More Actions** button, and choose **Delete List**. You can also mark deeply nested folders as **Favorites** to access them quickly without digging through the directory structure.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Online Links and Quick Access" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Other Services

This section displays extra features that enhance your experience. Currently, the app supports **Last.fm scrobbling** — when connected, your playback statistics are automatically sent to your Last.fm account. You can later visit your Last.fm profile to view listening analytics and get personalized music recommendations. Detailed setup instructions are available [here](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Last.fm Connect" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
