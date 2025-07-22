---
date: '2025-06-12T17:00:00+00:00'
draft: false
title: 'Frequently Asked Questions'
description: 'Find answers to common questions about Evermusic, Flacbox, Evervideo, and Evertag. Explore features like cloud streaming, file management, playback options, metadata editing, and more.'
keywords: [
  "Evermusic FAQ", "Flacbox support", "Evervideo help", "Evertag questions",
  "how to use Evermusic", "cloud music player troubleshooting", "offline playback guide",
  "audio tags editor support", "video streaming issues", "file transfer tutorial"
]
tags: [
  "FAQ", "help", "support", "evermusic", "flacbox", "evervideo", "evertag",
  "cloud setup", "playback issues", "file management", "metadata editing",
  "troubleshooting", "offline mode", "music player", "video player"
]
aliases:
  - /blog/categories/how-to/
---

{{< lottie src="/images/juicy-json/juicy-woman-focused-on-online-learning.json" width="85%" >}}

## Learn How to Use Our Apps

Looking for answers or help using one of our apps? You’re in the right place.

Our FAQ pages will help you connect cloud storage, manage music and video files, set up offline playback, adjust equalizer settings, fix metadata, and more.

Explore the FAQ for your app below to get started, or browse common questions and answers we've received from user emails.

## Choose Your App

{{< cards cols="2">}}

{{< card 
  link="/docs/faq/evervideo" 
  title="Evervideo" 
  subtitle="Play 360° videos, stream from iCloud, watch with subtitles, apply a video equalizer, organize content with playlists, and download videos for offline viewing."
  image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< card 
  link="/docs/faq/evermusic"
  title="Evermusic" 
  subtitle="Cloud music player with offline mode, audio equalizer, crossfade, gapless playback, playlist management, full music library, and built-in file manager."
  image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/flacbox"
  title="Flacbox" 
  subtitle="High-resolution audio player for iPhone and Mac. Listen to lossless formats like FLAC, ALAC, APE, and DSD. Fine-tune output with advanced audio settings."
  image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/evertag"
  title="Evertag" 
  subtitle="Smart music tag editor with batch editing. Fix missing metadata, album covers, and more. Edit ID3, FLAC, APE tags — over 120 fields supported." 
  image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< /cards >}}

## Common Issues and Answers

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{% details title="Why can't I log in to pCloud on an older iOS version (15.8.4)?" closed="true" %}}
pCloud’s web login page may not display correctly on older iOS versions such as 15.8.4, which prevents entering your email and password inside cloud connection screen.<br><br>

As a workaround, you can use the **WebDAV** protocol, which is supported by pCloud and works reliably across all iOS versions.

**WebDAV Setup:**<br>
- **US Servers:** `https://webdav.pcloud.com`  
- **European Servers:** `https://ewebdav.pcloud.com`  
- **Username:** Your pCloud email address  
- **Password:** Your pCloud account password  

Open App → Connections → Connect to Cloud Storage → Choose **WebDAV** → Enter your credentials and server URL.

This method will let you connect to your pCloud storage and have access to your files without issues on older devices.
{{% /details %}}

{{% details title="How to play music on AirPlay from Mac (macOS)?" closed="true" %}}
The macOS version of the app doesn’t include built-in AirPlay, Chromecast, or Bluetooth connection buttons like on iOS.<br><br>

To use **AirPlay** on your MacBook Pro, follow these steps:

1. Go to the **top-right corner** of your screen and open the **Control Center** (near the clock).  
2. Click the **Sound/Volume** icon.  
3. In the next screen, click **AirPlay** to view a list of all available AirPlay devices.  
4. Select the desired device to begin streaming your music.  

This will route all system audio (including from Evermusic or Flacbox) to your chosen AirPlay device.
{{% /details %}}

{{% details title="Why isn’t my Premium purchase activated on Mac if I bought it on iPhone?" closed="true" %}}
Lifetime purchases and subscriptions are synced between iOS and Mac via **iCloud**.<br><br>

To activate Premium on your Mac:<br>
- Ensure you have the latest app version installed on both devices<br>
- Enable **iCloud** on both devices<br>
- Launch the app on your iOS device and wait 1 minute for purchase info to upload<br>
- On your Mac, install the app from the App Store using the **same Apple ID**<br>
- Launch the app and wait a few seconds for the info to sync<br>
- Alternatively, tap **Restore Purchases** in the app’s settings on both devices<br><br>

Your Premium features should then activate on Mac automatically.
{{% /details %}}

{{% details title="How can I sync playlists automatically between devices?" closed="true" %}}
There is currently **no automatic sync** for playlists.<br><br>

You can use one of the following options:<br>
- **Backup and Restore** from App Settings [How to Transfer Your Music Library Between Devices in Evermusic: Step-by-Step Guide](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/)<br>
- **Export playlist to M3U**, then import on another device:<br>
  - [How To Export Playlists](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/)<br>
  - [How To Import Playlists](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/)<br>
- **Archive playlist or albums** and transfer via ZIP:<br>
  - [Playlist Archive Guide](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to/)
{{% /details %}}

{{% details title="Is it safe to use your apps? Can I disable analytics?" closed="true" %}}
Yes, your privacy is our top priority.<br><br>

- All data—music files, settings, cloud logins—stay on your device<br>
- Login credentials are securely stored in **iOS Keychain**<br>
- We only collect anonymous crash and usage reports<br>
- You can opt out in **App Settings → Analytics**<br><br>

More info:<br>
- [Privacy Policy](/legal/privacy-policy/)<br>
- [Apple Keychain Security](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web)<br><br>

If using personalized ads, Google Mobile Ads requires consent settings to be shown.<br>
Premium users see no ads and the ad SDK is completely disabled.
{{% /details %}}

{{% details title="Do your apps support Family Sharing?" closed="true" %}}
Yes, Family Sharing is supported.<br><br>

To share in-app purchases:<br>
- Make sure the purchase is set to be shared with your family group<br>
- On the family member’s device, go to **Settings > Purchases > Restore Purchases**<br>
- This will request purchase data from Apple’s servers and activate it on their device
{{% /details %}}

{{% details title="How to speed up metadata and cloud sync?" closed="true" %}}
To improve sync speed, enable background tasks:<br><br>

- **Settings → Music Library → Metadata Reading → Metadata Reading in Background**<br>
- **Settings → Music Library → Online Music Sync → Background Sync**<br><br>

Also, on macOS, increase metadata read speed via **Settings → Music Library**.<br>
If the player is active (audio playing), iOS won’t suspend the app, enabling continuous sync.
{{% /details %}}

{{% details title="How can I cancel my subscription?" closed="true" %}}
You can cancel your subscription from Apple’s official instructions:<br>
👉 [How to cancel a subscription](https://support.apple.com/en-us/118428)
{{% /details %}}

{{% details title="How can I connect and stream audio from WD MyCloud EX2 Ultra?" closed="true" %}}

When you add a connection in the app via **Connections > Connect to Cloud Storage > My Cloud Home**, it’s officially designed to support **WD MyCloud Home** devices.<br>
WD MyCloud EX2 Ultra uses restricted access for apps.<br><br>

However, if you’ve successfully connected to a **WD MyCloud EX2 Ultra**, **WD MyCloud Mirror**, or another **WD MyCloud** storage model, you can still use it with the following workaround:<br><br>

1. Open **Connections → Connect to Cloud Storage → My Cloud Home**<br>
2. Create a folder using built-in file manager<br>
3. Upload music files into this folder<br>
4. These will be stored in a "sandbox" accessible only by the app<br>
5. You can now stream or download them directly<br><br>

⚠️ Only folders created via the app will be accessible from the NAS.
{{% /details %}}

{{% details title="How do I connect to Koofr.eu?" closed="true" %}}
You can connect Koofr using **WebDAV**.<br><br>

- Koofr WebDAV setup guide: [koofr.eu blog](https://koofr.eu/blog/posts/3-ways-to-map-koofr-as-a-network-drive-explained)<br>
- Evermusic/Flacbox WebDAV guide: [How to Connect NAS Storage Using WebDAV and Listen to Music on Your iPhone or Mac](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)
{{% /details %}}

{{% details title="What are the app URL schemes?" closed="true" %}}
Here are the supported schemes:<br><br>

**Evermusic**<br>
- iOS (blue icon): `lsevermusic://`<br>
- macOS: `lsevermusicmac://`<br>
- iOS (red icon): `lsevermusicpro://`<br><br>

**Flacbox**<br>
- iOS: `lsflap://`<br>
- macOS: `lsflapmac://`<br><br>

**Evertag**<br>
- iOS: `lsevertag://`<br>
- macOS: `lsevertagmac://`<br><br>

**Evervideo**<br>
- iOS: `lsevervideo://`<br>
- macOS: `lsevervideomac://`
{{% /details %}}

{{% details title="Music stops playing when app is in background — how to fix?" closed="true" %}}
If the app crashes or pauses in background:<br>
- Go to **Settings > Music Library > Online Music Sync > Background Sync → Disable**<br>
- **Settings > Music Library > Metadata Reading > Metadata Reading in the Background → Disable**<br>
- **Settings > File Manager > Background Transfers → Disable**
{{% /details %}}

{{% details title="Gapless playback not working — how to fix?" closed="true" %}}
Gapless playback depends on iOS version and audio engine.<br>
Try switching the audio engine:<br>
- Go to **Settings → Audio Player → General → Audio Processor**<br>
- Select **Core Audio** for better gapless support
{{% /details %}}

{{% details title="Why does the app only show 100 items in a list?" closed="true" %}}
The app uses pagination for performance.<br>
To disable it:<br>
- Go to **Settings → Personalization → Content Loading Limit → Deactivated**<br>
Now all items will load at once.
{{% /details %}}

{{% details title="Why are there strange characters in metadata?" closed="true" %}}
Try enabling metadata normalization:<br>
- **Settings → Music Library → Metadata Reading → Normalize Metadata Encoding**
{{% /details %}}

{{% details title="Why can’t the app read folder names with special characters?" closed="true" %}}
This is a known issue with **SMB2 protocol**.<br><br>

Try the following solutions:<br>
- Enable **SMB1** on your server and in app settings<br>
- Use the **system file picker**:<br>
  - Go to **Local Files > Files on this Device > Open Files...**<br>
  - Select folders/files using Apple’s native menu<br><br>

Alternatively, connect using **WebDAV** or **DLNA** if your NAS supports them.
{{% /details %}}

{{% details title="How do I upload and manage music in iCloud?" closed="true" %}}
– **How do I upload music to iCloud?**  <br>
Go to [https://www.icloud.com](https://www.icloud.com) in your browser, create a folder, and upload your music files directly from your Mac or PC.<br>

– **How do I manage iCloud storage?**  <br>
You have two options:  <br>
1. Use [https://www.icloud.com](https://www.icloud.com) in your browser to organize, upload, or delete files.<br>  
2. In the app, after connecting to iCloud via **Connections → Connect to Cloud Storage → iCloud Drive**, use the built-in file manager to upload, download, rename folders, or delete files directly in your iCloud storage — without saving them to your device.<br>

⚠️ Be careful when deleting files. The app permanently deletes them (they won’t go to the trash and can’t be recovered).<br>

Learn more here: [How to Stream Music from iCloud Drive on My iPhone or Mac](/docs/howto/how-to-listen-to-music-from-icloud-drive-on-your-iphone-or-mac/)

{{% /details %}}

</div>