---
title: "How to connect Bluesound Vault's internal storage from the Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Learn how to access Bluesound VAULT's internal hard drive from Evermusic, Flacbox, and Evertag using SMB protocol to manage, edit, and play audio files."
keywords: ["bluesound vault", "connect smb storage", "evermusic smb", "flacbox vault", "evertag smb", "nas storage music", "vault internal drive"]
tags: ["evermusic", "connect", "bluesound vault"]
readingTime: 1
aliases:
  - /post/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/
---

{{< author-byline >}}


**TL;DR:** Connect to your Bluesound VAULT's internal storage via SMB using Evermusic, Flacbox, or Evertag. Find the VAULT's IP address in the BluOS app, enter it as an SMB connection with guest access, and start playing or managing your music files.

Bluesound VAULT has an internal hard drive and acts as a Network Attached Storage (NAS). Accessing the VAULT’s internal hard drive allows you to add/delete files, edit metadata tags from our apps Evermusic, Flacbox, Evertag.

**Following are the steps to access your VAULT’s internal hard drive:**

1. In the BluOS App, select **Help > Diagnostics**.

2. From the **Diagnostics** page, obtain the **IP Address** of the VAULT. This **IP Address** will be used in next steps.

3. Open Evermusic, Flacbox or Evertag.

   ![Everappz applications](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Open the "Connections" screen and select the "Connect a cloud service" menu item.

   ![Evermusic Connections Screen](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Select "SMB" cloud service.

   ![Evermusic Connect A Cloud Service Screen](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. On the "SMB Configuration screen" enter URL in the following format:

   ```
   SMB://<<VAULT-IP>>
   ```

   Replace `<<VAULT-IP>>` with the **IP Address** obtained in Step 2.

   **Note:** Leave Login and Password fields blank because VAULT Storage supports GUEST mode.

   ![Evermusic SMB Connection Screen](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Tap the "Sign in" button to save the configuration.

8. Open connected cloud storage and navigate inside the folder with audio files and tap any file to start the audio player.

   ![Evermusic Opened SMB Server Screen](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. You can also edit files using the built-in file manager.

   ![Evermusic File Manager Screen](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

With these straightforward steps, you can effortlessly access your Bluesound VAULT's internal hard drive and take control of your music library using Evermusic, Flacbox, or Evertag.

## FAQ

{{% details title="Do I need a username and password to connect to Bluesound VAULT?" closed="true" %}}
No. Bluesound VAULT supports guest (anonymous) access via SMB. Leave the Login and Password fields blank when configuring the connection.
{{% /details %}}

{{% details title="Can I edit music tags on the Bluesound VAULT?" closed="true" %}}
Yes. Using Evertag, you can edit metadata tags (title, artist, album, etc.) for audio files stored directly on the VAULT's internal hard drive.
{{% /details %}}

{{% details title="Which protocols does Bluesound VAULT support?" closed="true" %}}
Bluesound VAULT exposes its internal storage via SMB (Server Message Block). Evermusic, Flacbox, and Evertag all support SMB connections, making it straightforward to connect.
{{% /details %}}

{{% details title="Can I stream music from the VAULT without copying files to my iPhone?" closed="true" %}}
Yes. Once connected via SMB, you can stream audio files directly from the VAULT's internal drive without copying them to your device.
{{% /details %}}
