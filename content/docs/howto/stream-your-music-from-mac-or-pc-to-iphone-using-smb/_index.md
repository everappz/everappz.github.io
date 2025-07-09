---
title: "Stream Your Music from Mac or PC to iPhone Using SMB"
description: "Learn how to stream your music collection from Mac or Windows PC to your iPhone or iPad using Evermusic and the SMB protocol. A simple step-by-step guide to connect and enjoy audio without syncing."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["stream music from Mac to iPhone", "SMB audio streaming iOS", "Evermusic SMB setup", "connect PC music iPhone", "Mac music share iOS", "SMB Windows file streaming", "Evermusic PC folder access"]
---

Are you drowning in a sea of music on your MAC or PC and want to enjoy it hassle-free on your iPhone or iPad? Look no further than Evermusic. With Evermusic, it's incredibly simple to connect your computer using the SMB protocol and stream your beloved tunes without worrying about taking up extra device space or dealing with synchronization hassles. Here's a step-by-step guide to get you started:

## Step 1: Enable SMB Protocol on Your Computer

![Evermusic - SMB Support - Mac Sharing Screen](21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### If you're using MAC

- Open System Preferences -> Sharing.
- Enable the File Sharing service.
- In the "Shared Folders" section, add your music folder, select a user, and set permission levels (Read & Write or Read Only).
- For added convenience, you can select "Everyone: Read Only" for the music folder, making it easily accessible in Evermusic.
- Don't forget to remember your computer's URL (smb://192.168.xx.xx) for the next steps.

![Evermusic - SMB Support - File Sharing Screen](21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Tap "Options" and enable "Share files and folders using SMB."
- Enable "Windows File Sharing" for available accounts.

![Evermusic - SMB Support - Share Files And Folders Screen](21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### If you're using a Windows PC

![Evermusic - SMB Support - Share Files On Windows](21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Right-click on your music folder.
- Select "Properties."
- Open the "Sharing" tab.
- Click "Share…"
- Choose the people to share with and set their permission levels.
- Like with MAC, you can opt for "Everyone: Read" for the selected music folder.
- Click "Done" to save your settings.

![Evermusic - SMB Support - Folder Shared on Windows](21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Step 2: Add Your Computer Automatically

- Now, open Evermusic and go to the "Connections" tab ("Network" if you are using old app version).
- If you see your computer in the "Available devices" ("Available shares" if you are using old app version) section and selected "Anyone: Read Only" in the previous step, simply tap on your computer, and it will connect automatically.
- If this doesn't happen, you can add your computer manually.

![Evermusic - SMB Support - Connect Account Screen](21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Step 3: Add Your Computer Manually

- Tap "Connect a cloud service" ("Add Account" if you are using old app version)
- Select "SMB" from the list of available servers on the next screen.
- In the "SMB" Settings screen:
  - Enter the server URL with the shared folder path. You may enter the server name or server IP. For example:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Enter your Login and Password or leave these fields blank if you selected "Anyone: Read Only" in the previous step.
  - The "WORKGROUP" field is optional and should be used if you have an Active Directory Domain.

![Evermusic - SMB Support - Enter Credentials Screen](21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Once you've connected your SMB Account, it will appear in the "Cloud services"("Accounts") section. Open the connected account by tapping on it, navigate to the music folder, and tap on any audio file to start the player.

![Evermusic - SMB Support - Open Connected Folder Screen](21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Enjoy your music collection seamlessly on your iPhone or iPad with Evermusic.

![Evermusic - SMB Support - Audio Player Screen](21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Step 4: SMB2 Workaround

If you encounter issues with browsing folders or playing files that contain special symbols (like ü, ö, é), this may be related to the SMB2 protocol. We are actively working on resolving this issue.

As a temporary solution, please try enabling SMB 1 on your server and in the app settings. Alternatively, you can connect to your SMB server using the system file open menu. Here's how:

1. Navigate to "Local files."
2. Scroll down to the "Files on this device" section and tap "Open files..." or "Open folders..."
3. Locate your server and select the files or folders you need.
4. Tap "Open" to confirm your selection.

## Step 5: WebDAV Workaround

Additionally, you can try connecting to your NAS using WebDAV or DLNA protocols if supported.

By following these steps, you can bypass the issues related to special symbols in file names and continue enjoying your media files.

P.S. You can also transfer audio files from your MAC/PC to your iPhone using iTunes File Sharing and play local audio files. Learn more about this feature in our guide: [How To Play iTunes Files on iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).