---
title: "How to Transfer Your Music Library Between Devices in Evermusic: Step-by-Step Guide"
description: "Easily transfer your Evermusic music library, playlists, album artwork, and settings from one iPhone, iPad, or Mac to another using Wi-Fi Drive and backup tools."
date: 2024-12-29
tags: ["musiclibrary", "transfer", "wifi", "backup", "webdav", "restore"]
keywords: ["transfer music library Evermusic", "backup and restore playlists Evermusic", "Evermusic WiFi Drive", "sync Evermusic between devices", "move Evermusic database", "Evermusic file transfer", "restore audio player settings", "WebDAV music transfer iOS"]
readingTime: 3
---

In this guide, we’ll walk you through transferring your entire music library — including database, album covers, and settings — from one device (iPhone or Mac) to another. While automatic music library and playlist sync is a feature planned for the future, this process must currently be done manually.

## Step 1: Create a Backup on the First Device

1. **Open the app on your first device** (the one with your music library, playlists, and connected cloud services).
2. **Navigate to Settings** and select the **Backup and Restore** option.

![Backup and Restore](21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. On the **Backup and Restore** screen, choose the items to include in your backup file:
   - **Database** (includes your music library and playlists)
   - **Album Covers**
   - **Settings**

These options are enabled by default.

![Backup Options](21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Tap **Backup Application Data** to begin the process.

![Backup Application Data](21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Once the backup is complete, an info alert will appear.

![Backup Complete](21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Tap **Show File** to reveal the backup file in the **Documents** directory. Backup files are typically saved in the **Backup** folder.

![Show Backup File](21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Step 2: Start the Wi-Fi Drive Server

1. Go to the **Connections** section in the app.
2. Scroll down to **Connect Using Wi-Fi** and tap on it.

![Connect Using Wi-Fi](21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. On the next screen, tap **Start Wi-Fi Drive**.

- Optionally, you can set a login and password for security, but this is unnecessary for home networks.

4. Once started, you’ll see the available server addresses. This can be used for desktop browsers or WebDAV apps, but in this guide, we’ll proceed directly to the next steps.

![Wi-Fi Drive Started](21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Step 3: Connect Your Second Device to the First One

1. Open the app on your second device (where you want to transfer the library).
2. Ensure both devices are connected to the same Wi-Fi network.
3. On the second device, open the **Connections** tab and select **Available Devices**.

![Available Devices](21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. You should see a WebDAV connection named **Evermusic** (the server we started on the first device). Tap on it to connect.

5. Once connected, you’ll see all the folders from the first device.

![Connected to First Device](21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Step 4: Prepare for File Transfers

1. On the second device, go to **Settings > File Manager** and enable **Save Downloaded Files To - Ask Every Time**.

- This ensures you can select the destination folder for each download.

2. Return to the **Connections** tab and navigate to the connected WebDAV server.

![Prepare for File Transfers](21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Step 5: Transfer Backup and Music Files

1. Open the **Backup** folder on the connected WebDAV server.

![Backup Folder](21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Tap the **More Actions** button (three dots) near the backup file and select **Download**.

3. Create a **Backup** folder on the second device to store the downloaded files. Confirm your selection by tapping **Done**.

![Download Backup](21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Transfer any additional music files:
   - Check the **Downloads** folder or other relevant folders on the WebDAV server.

![Transfer Music Files](21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Use the **Select** option to choose files, then tap **More Actions > Download**. Save them in the corresponding folder on the second device to maintain the same directory structure.

The goal is to transfer all files from your first device to your current device, ensuring that the folder structure remains identical. This way, links in your music library and playlists stay intact. Note that local files stored outside the app’s Documents directory on your first device must be transferred separately. Since the app cannot access these files in Wi-Fi Drive mode, you’ll need to use the System Files app for their transfer.

![Transfer Complete](21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Step 6: Monitor the Transfer Progress

1. On the second device, go to the **Local Files** section (or **Downloads** tab on iPad/Mac).

2. Tap the **Transfer Activity** button in the top-left corner to monitor the transfer queue.

![Monitor Transfer](21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Step 7: Restore Data from Backup

1. Once the backup file and all needed audio files are downloaded to the second device, open the **Backup** folder.

2. Tap the backup file, and a confirmation message will appear.

![Restore Backup](21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Note:** Restoring will replace all current music library data, playlists, settings, and album artwork with the backup data.

3. Tap **Restore** to begin the process.

![Restore Process](21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. After the restoration is complete, an alert will confirm success.

![Restoration Complete](21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Check the **Playlists** or **Music Library** sections to verify the restoration.

![Verify Restoration](21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Step 8: Reindex the Music Library

1. For best results, reindex your library to ensure all files are successfully detected.

2. Go to **Settings > Music Library > Offline Music Sync** and select **Start Local Folders Scanning**.

By following these steps, you’ll successfully transfer your music library, playlists, and settings to another device. If you encounter any issues, don’t hesitate to reach out for support.