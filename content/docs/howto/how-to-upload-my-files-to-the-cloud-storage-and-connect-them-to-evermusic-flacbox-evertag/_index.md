---
title: "How to Upload Files to Cloud Storage and Connect to Evermusic, Flacbox, or Evertag"
description: "Learn how to upload files to cloud services like Google Drive, Dropbox, and OneDrive, and connect them to Evermusic, Flacbox, or Evertag for easy file access."
date: 2022-03-17
readingTime: 2
tags: ["evermusic", "flacbox", "cloud", "file", "account", "manager", "connect", "network", "service"]
keywords: ["connect cloud service to Evermusic", "upload files to Google Drive", "Flacbox cloud integration", "use OneDrive with Evermusic", "Evertag cloud file access", "connect Dropbox to iOS music player", "file manager for cloud services"]
aliases:
  - /post/how-to-upload-my-files-to-the-cloud-storage-and-connect-them-to-evermusic-flacbox-evertag/
---

{{< author-byline >}}


**TL;DR:** Upload your music or media files to any supported cloud service (Google Drive, Dropbox, OneDrive, and more), then connect that service inside Evermusic, Flacbox, or Evertag to stream or download your files directly on iPhone, iPad, or Mac.

## Step 1: Sign Up for a Cloud Storage Account

If you haven’t already, sign up for a cloud service like Google Drive, Dropbox, OneDrive, etc.

{{< figure src="21260c_09c03b8445784d23b632534939b328dd~mv2.png" alt="Evermusic: Create your Google Account" width="400" >}}

You can connect any of the supported accounts: Dropbox, Box, Google Drive, OneDrive, MediaFire, Yandex.Disk, MEGA, MyDrive, pCloud, and others.

{{< figure src="21260c_3433be90b41f4fe7988383929751b5ec~mv2.png" alt="Evermusic: Go to Google Drive" width="400" >}}

## Step 2: Download the Cloud App for Your Computer

Download the official application for Mac or PC from your cloud provider.

{{< figure src="21260c_0e710dbbbb1f47328015575bb25deee0~mv2.png" alt="Evermusic: Download Google Drive for MAC" width="400" >}}

## Step 3: Upload Your Files to the Cloud

Use the desktop app or web interface to move files into your cloud account.

{{< figure src="21260c_0d0f8accee4642debdaa5e88e104b875~mv2.png" alt="Evermusic: Change Google Drive Sync Settings" width="400" >}}

## Step 4: Connect Cloud Storage to the App

Once your upload is complete, open Evermusic, Flacbox, or Evertag on your iPhone, iPad, or Mac.

### Step 4.1: Open Connections

Open the **Connections** tab and tap **Connect a cloud service**.

{{< figure src="21260c_7fcd5b0dbe954ad19a922b64df9f40b2~mv2.png" alt="Evermusic: Connect a cloud service" width="400" >}}

### Step 4.2: Choose a Service

Select your cloud service from the list of supported services.

{{< figure src="21260c_f6a38f1159a44c788f015481581ab25e~mv2.png" alt="Evermusic: Select a cloud service" width="400" >}}

### Step 4.3: Login

Enter your login credentials.

{{< figure src="21260c_8839d4994ef742bea1b88cb366fa3da9~mv2.png" alt="Evermusic: Enter Login Password for a Cloud Service" width="400" >}}

### Step 4.4: Authorize Access

Allow the app to access files in your cloud storage.

{{< figure src="21260c_32b765b63fb24c149c1cf0c3d6b538a3~mv2.png" alt="Evermusic: Allow Permissions for Cloud Service" width="400" >}}

## Step 5: Manage Your Files in the App

Once connected, browse your cloud files and manage them using the in-app file manager. You can move, rename, delete, or download files by tapping the **More actions** button `...`.

{{< figure src="21260c_ff782076be304029a555f38bd4517788~mv2.png" alt="Evermusic: List Of Files" width="400" >}}

## Conclusion

Connecting your cloud service to our apps streamlines file access and management, making it easier than ever to enjoy your files across different devices.

Say goodbye to storage limitations and hello to convenience!

## Frequently Asked Questions

{{% details title="Which cloud services are supported?" closed="true" %}}
Evermusic, Flacbox, and Evertag support Google Drive, Dropbox, OneDrive, Box, MediaFire, Yandex.Disk, MEGA, MyDrive, pCloud, and other cloud providers. You can also connect custom WebDAV, SMB, and FTP servers.
{{% /details %}}

{{% details title="Can I stream music directly from the cloud without downloading?" closed="true" %}}
Yes. All three apps support streaming audio files directly from your connected cloud storage. You can also download files for offline playback when you do not have internet access.
{{% /details %}}

{{% details title="Is there a file size or storage limit in the app?" closed="true" %}}
The apps do not impose their own file size or storage limits. Your available storage depends on your cloud service plan and your device's local storage for downloaded files.
{{% /details %}}

{{% details title="Can I connect multiple cloud accounts at the same time?" closed="true" %}}
Yes. You can connect multiple cloud services and multiple accounts from the same provider simultaneously. All connected accounts appear in the Connections tab for easy switching.
{{% /details %}}

{{% details title="Do I need to re-upload files if I switch to a different app?" closed="true" %}}
No. Since your files are stored in the cloud, you can connect the same cloud account to Evermusic, Flacbox, or Evertag without re-uploading anything. Each app accesses the same files from your cloud storage.
{{% /details %}}

{{% details title="Is my cloud account data secure?" closed="true" %}}
Yes. The app uses only official SDKs and encrypted connections to interact with cloud services. Your login and password are never stored by the app. When you sign in, the app displays the official authorization page provided by the cloud service. After successful authorization, the cloud provider sends an auth token to the app, which is stored securely in the device Keychain. This token is used for all API requests.<br><br>
The app does not share any information from your cloud account. You can revoke access at any time from your cloud account settings page in a web browser, or disconnect the account inside the app.
{{% /details %}}

{{% details title="How do I disconnect a cloud service or change its configuration?" closed="true" %}}
Locate the cloud storage in the app's Connections tab and tap the **...** button next to it. You will see these options:<br>
- **Rename** -- change the display name of the cloud service<br>
- **Settings** -- modify configuration or re-authorize if the token has expired<br>
- **Disconnect** -- remove the connection entirely. This removes all songs from this cloud service from the app's music library, but files remain on the server
{{% /details %}}

{{% details title="How do I revoke the app's access to my cloud account?" closed="true" %}}
Log in to your cloud account in a web browser and open the account settings or security page. Find the list of connected third-party apps and remove the app you no longer want to authorize. You can also disconnect the cloud account inside the app -- this removes the auth token from your device. If you delete the app entirely, all downloaded data and access tokens are removed automatically.
{{% /details %}}
