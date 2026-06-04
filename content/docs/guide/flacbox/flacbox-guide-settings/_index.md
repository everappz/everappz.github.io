---
title: "Settings"
date: 2020-02-01
description: "Explore every setting in Flacbox — from playback preferences, the FFmpeg / system audio engine, Hi-Res audio output, equalizer tweaks, pitch correction, IO buffer duration, metadata sync, playlist control, file transfers, Home Screen widgets, Apple CarPlay, UI personalization, language, passcode, backup & restore, and Premium upgrade."
keywords: [
  "Flacbox settings", "audio player configuration", "premium upgrade Flacbox",
  "WiFi Drive", "metadata synchronization", "equalizer", "playback speed",
  "playlist duplicates", "file manager settings", "offline music sync",
  "audio tags editor", "dark mode", "restore purchases", "backup settings",
  "Flacbox widgets settings", "Flacbox CarPlay settings",
  "Flacbox FFmpeg settings", "Flacbox sample rate settings",
  "Flacbox pitch correction settings", "Flacbox IO buffer",
  "Flacbox passcode", "Flacbox language", "Flacbox personalization",
  "Flacbox analytics"
]
tags: ["guide", "flacbox", "settings"]
readingTime: 16
aliases:
  - /post/flacbox-guide-settings/
  - /guide-flacbox-settings/
---


The Settings screen is the control center of Flacbox. From here you can upgrade to Premium, configure the audio engine (system codecs or FFmpeg), manage your music library, set up the file manager, customize the audio tags editor, enable Home Screen widgets and Apple CarPlay, back up your data, and access help and legal information. Sections are grouped under headers: Purchases & Updates, App Preferences, Help, and Legal & Privacy.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Settings Main Screen" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Upgrade to Premium

Upgrade the application to the Premium version to remove all limits. The free version of the application offers a one-time lifetime in-app purchase and two subscription options (1 month and 1 year) to remove all restrictions and upgrade to Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Upgrade to Premium" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

**Family Sharing** is enabled for all purchases and plans, so you can share the Premium version with up to five members of your family at no extra cost.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Select a Premium Plan" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

You can read more about purchases and the Premium version here: [What is the difference between Flacbox and Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Sharing Purchases Between iOS and Mac

Lifetime purchases and subscriptions are shared between iOS and Mac, using iCloud to sync this information. If you have the Premium version on your iOS device, ensure you have the latest version installed and that iCloud is enabled. Start the app on iOS and wait one minute for your purchase information to upload to iCloud.

You can also try tapping the Restore Purchases button in the app settings. Afterward, install the latest app version from the App Store on your Mac and start the app. Ensure you have an internet connection and are using the same iCloud and App Store account on Mac that you used on iOS. Wait one minute for the app to download purchase info from iCloud — the Premium version should activate on your Mac automatically.

## Restore Purchases on a New Device

To restore your purchase on a new device, use the Purchases → Restore Purchases menu. You’ll see the list of your purchases. If you don’t see all of them, confirm the device is connected to the same Apple ID that was used to make the purchases, and make sure iCloud is enabled.

## Try Premium for Free

You can upgrade to the Premium version for free, for a limited time, using this menu. Just watch an advertisement or tell your friends about the app to get Premium for free.

## Purchases

You can restore previous purchases from this menu. If you encounter activation errors, try enabling the Restore Purchases at App Launch option.

## Software Update

Tap Software Update to check whether a newer version of Flacbox is available. The app will compare your installed version with the latest version on the App Store and let you know if an update is recommended.

## What’s New

This menu is available after a new version is released. It shows a summary of the changes and new features in the most recent update.

## Audio Player

This section configures the audio player and the underlying audio engine, including the FFmpeg / system codec choice and Hi-Res audio output options.

### General

These settings cover the fundamental aspects of the audio player — playback queue, audio output, and saving the player’s state.

- **Repeat Mode** — choose how the audio player behaves when a track finishes:
  - **Repeat All** — replays all the tracks in your queue.
  - **Repeat One** — repeats only the current track.
  - **Repeat Stop** — pauses playback when the current track ends.
  - **Repeat None** — allows your queue to play through without repeating.
- **Shuffle Mode** — randomize the order of tracks in your queue. You can turn it **Shuffle Off** or **Shuffle On**.
- **Audio Codec** — choose the audio engine used for playback:
  - **System Codec + FFmpeg** — prioritizes the system’s audio codec where possible, enhancing compatibility and stability. Pitch correction and audio output sample rate may be limited.
  - **FFmpeg** — forces the FFmpeg codec for all audio files, unlocking pitch correction and the audio output sample rate.
- **Audio Output Sample Rate** — adjust the audio output sample rate to optimize sound quality, especially useful with an external DAC. Available values: **44.1 kHz, 48 kHz, 64 kHz, 88.2 kHz,** and **96 kHz**.
- **Audio Output Number of Channels** — for multichannel audio systems with an external DAC, specify the number of channels: Mono, Stereo, Center / Left / Right, Center / Left / Right / Surround, ITU BS.775-1, 5.1 Surround, and SDDS.
- **Audio Output Preferred IO Buffer Duration** — configure the input / output buffer duration. A typical value for minimizing latency while playing high-resolution audio is around **5 milliseconds (0.005 seconds)**. Test different durations on your target device to find the best balance between low latency and glitch-free playback.
- **Audio Output Mode (iOS only)** — configure mixed audio output so audio from Flacbox blends with other applications. Detailed instructions are [here](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Save Playback Position** — saves and restores the playback position for songs in your music library.
- **Save Audio Player State** — preserves the audio player’s state before you close the app, making it easy to resume from where you left off.

Once you’ve enabled both **Save Playback Position** and **Save Audio Player State**, open any folder, album, artist, or genre and you’ll see a **Continue Playback** button at the top of the screen.

### Personalization

Personalization allows you to customize the look of the audio player screen, change the available controls on the main screen, lock screen, and status bar, and configure skip-time controls.

- **Audio Player Screen Style** — configure the positioning of elements on the audio player screen.
- **Album Covers Scrolling Style** — configure the preferred scrolling style for album covers.
- **Additional Elements** — enable extra elements on the audio player screen. Audio Format Info shows the now-playing track’s audio info above the artwork; Audio Volume Slider shows the audio output slider below the playback controls.
- **Main Screen Actions** — configure which buttons should be visible on the main audio player screen by default: Repeat and Shuffle Mode, Next and Previous Song, Skip Time, Sleep Timer, Google Chromecast, AirPlay and Bluetooth, Audio Equalizer, Search, Bookmarks, Speed, Add Bookmark, Add to Favorites, Comments, and more.
- **Playback Controls on the Lock Screen** — choose which controls appear on the lock screen. Possible values: Skip Time, Add Bookmark, Add to Favorites.
- **Skip Time Buttons** — pick the time interval for the Skip Time buttons.

### File Loading

During file loading, you can change the network type used to load songs. Available options: **Wi-Fi**, **Wi-Fi & Cellular Data**.

- **Preloading Time** — set the buffering time interval. Increase this if you have a poor network connection.
- **Use Direct URL** — when enabled, a direct URL is used to load the song if the server supports it. This can speed up song loading but may affect playback stability.

### Audio Equalizer

Configure the 10-band audio equalizer, presets, and preamplifier. You can read more about configuring the audio equalizer [here](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Playback Speed

Adjust the playback speed of the audio player from **0.02× to 3.00×**. Tap the configuration icon in the top-right corner to switch to **precise mode** for finer adjustments.

### Pitch Correction

Change pitch correction settings using the predefined values, or switch to **precise mode** by tapping the button in the top-right corner. Pitch correction is available in the FFmpeg codec path, with a range from **-1000 to +1000**.

### Playback Cache

Songs in the audio player queue are automatically downloaded to ensure smooth playback. If you manually download audio files, you can disable this to avoid duplicates. You can also configure the audio player cache size here.

### Sleep Timer

Activate a timer to automatically stop playback after a specified period. Tap the configuration icon in the top-right corner for **precise mode** with minute-by-minute granularity.

## Library

Your music library settings — automatic sync, metadata reading, album cover loading, playlists, recents, and favorites — live here.

### Metadata Reading

When you add tracks to the library, the **metadata reader** gets to work. This background process reads all metadata from your tracks and organizes them by Artist, Album, Genre, and Composer. You can adjust the speed of metadata reading to load data faster (at the cost of more battery). You can also disable the metadata reader and display file names instead of tag information.

The metadata reader **only updates metadata in your music library** and does not alter the files stored in your cloud account or local storage. To edit metadata in the audio files themselves, use the built-in **tag editor** via the corresponding action in the options menu.

When **Metadata Reading in the Background** is on, the reader continues working in background mode. If the app uses too much energy during audio playback, iOS may suspend it.

If you have a large music collection, perform metadata synchronization on the desktop version of the application and transfer the synchronized music library to iOS using **Backup & Restore**.

When **Normalize Metadata Encoding** is enabled, the app automatically normalizes the encoding of metadata for all songs. This fixes broken tag encodings (for example after editing files on a Windows PC) and prevents incorrect characters from appearing in track information.

**Reload Metadata** flags every file in your music library as having missing metadata, which causes the metadata reader to refresh every record.

**Start Metadata Reading** triggers the metadata reader manually. Progress is shown below the action.

### Online Synchronization

Automatic online music sync adds tracks from connected cloud services to the music library automatically. To enable it, open the music library settings and select sync folders.

With this option enabled, the application scans the selected folders, identifies supported audio files, and adds them to your library. Start or stop synchronization with the corresponding menu action.

Online sync runs only when the app is in the foreground, so syncing a large library can take a while. To speed things up, keep Flacbox open, plug your device into power, and enable **Settings → Screen → Always Active**.

Alternatively, perform online sync on the desktop version of the app and transfer the result to iOS using **Backup & Restore**.

You can also choose how often online sync runs. Setting the interval to **Immediately** triggers a sync every time you open the application.

### Offline Synchronization

Configure offline music synchronization.

#### Synchronized Offline Folders

When you mark an online folder on your cloud server as available offline (using the **More Actions** menu), it appears here. The folder content is downloaded to **Local Files → Offline Folders**. When the online folder changes (files added, removed, or updated), the app checks for changes and updates the local copy on your device.

On this screen you can manually start offline folder synchronization, reveal the offline folder in its enclosing folder, and disable offline mode for the folder. Disabling offline mode removes all local copies of files from your device.

#### Time Interval

Choose how often the app checks offline folders for modifications.

#### Start Local Folders Scanning

Scan all local folders in the application **Documents** directory for supported audio files. Found files are added to the music library automatically. Files located on your device but outside of the application Documents directory must be added to the music library manually, as the app cannot access them due to iOS / macOS security restrictions.

**Important:** It is advisable to periodically initiate offline music synchronization to keep your music library updated with your local files.

### Personalization

Configure the music library screen style. Three options are available: **Plain Menu, Grouped Menu, Tabbed Menu**. You can also enable or disable album covers in the album details screen.

### Album Covers

Configure how the application loads and stores album artwork.

- **Network Type** — pick **Wi-Fi** or **Wi-Fi & Cellular Data** for cover downloads.
- **Load Album Covers for Online Files** — when enabled, embedded album covers are loaded for files stored in cloud storage. This may use additional network data.
- **Search in the Folder** — when enabled, if a track has no embedded cover, the app looks for JPEG or PNG images in the same folder and uses them as the album artwork.
- **Cover Quality** — select the quality of album covers stored on your device.
- **Show in Folder** — open the folder where album covers are cached.
- **Delete All** — delete cached album covers to free up storage and force the app to reload them on demand.

### Playlists

Enable the option to add the same song to a playlist twice. By default, this option is disabled.

### Recents

Manage your recently played songs list.

- **Delete List** — delete the entire list of recently played songs.
- **Change List Size** — set the number of items that appear in the list.
- **Export Songs List** — export your recently played songs list as M3U, CSV, or TXT. Detailed instructions are available [here](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favorites

Manage the list of your favorite songs.

- **Simultaneous Editing** — when enabled, adding a song to favorites adds it both in the music library and the files section simultaneously.
- **Delete List** — delete the entire list of favorite songs.
- **Export Songs List** — like Recents, export favorites as M3U, CSV, or TXT.

### Delete Music Library

Erase the music library database. Your music files on storage are left untouched.

## Passcode

Activate the passcode screen to protect your application data with a 4-digit numeric passcode. When enabled, you’ll be prompted to enter the passcode every time the app launches. Combine it with iOS Face ID / Touch ID on the device for extra protection.

## File Manager

The File Manager section controls how files are transferred, stored, and previewed.

### File Transfers

Choose your network preference for downloading files to your device.

### Maximum Number of Parallel Tasks

Set the number of parallel download threads. A higher number speeds up downloads but uses more battery.

### File Transfer Tasks

Displays currently active upload and download tasks.

### Background Transfers

Allow downloads while the app is in the background. If background transfers consume a lot of energy, iOS may suspend the app.

### Save Downloaded Files To

Choose the default downloads directory, or have the app prompt you every time.

### Synchronized Offline Folders

Manage offline sync for selected folders. To enable offline sync, tap the three-dots button next to a folder and select **Available Offline Mode**. New files added to the cloud folder are downloaded to your device automatically. Read more about offline modes [here](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Time Interval

Choose how often offline folders are synchronized. **Immediately** triggers a sync every time you open the app.

### Show Full Filenames

Show complete filenames, including extensions, in the file manager.

### Edit Online Files

Disable online file editing to switch to read-only mode for connected cloud services and prevent accidental deletions. This action removes file editing operations from the user interface.

### Copy Files When Opening

Specify how the app handles imported files from other applications.

### Thumbnails for Files

Manage and delete generated file thumbnails to free up storage space.

### Delete Temporary Files

Clear the application’s cache folder to reclaim storage space.

## Audio Tags Editor

Configure the built-in audio tags editor — handy for batch-fixing artist / album / year / genre / cover-art issues across cloud and local files.

### Album Cover Scaling

Choose the scaling method used when an album cover is saved into audio tags.

### Update Online Files

When enabled, the application automatically updates a file’s metadata on the cloud server after you finish editing it.

### Delete File After Editing Online

Choose whether the application should delete the downloaded copy after finishing the edit of an online file on a cloud server.

### Main Screen Buttons

Choose which buttons are visible on the main screen of the audio tags editor.

For deeper batch editing across many files at once, install our companion app **Evertag**.

## Widgets

Enable widgets so the app updates widget data during playback. Widget updates require additional energy, so the toggle is off by default — enable it only if you actually use widgets on your Home Screen or Lock Screen.

You can add Flacbox widgets by long-pressing your Home Screen or Lock Screen, tapping **+**, searching **Flacbox**, and picking a widget size. Widgets show the current artwork, track title, and artist, and tap through directly to the full-screen player. Widgets also work on macOS in the Notification Center.

## CarPlay

Change CarPlay settings here. This menu is also available inside the CarPlay interface so you can adjust the experience while driving.

### Sort

Configure sort options for all CarPlay screens.

### Content Loading Limit

Choose whether the app uses pagination on the CarPlay screen. Pagination keeps menus responsive on large libraries.

### Menu Icons Gradient Color

Select the color scheme for the CarPlay home screen.

### Show Images

Disable images on the CarPlay screen to optimize loading speed and reduce memory usage on large libraries.

### Pause Playback When Connected

Enable this to avoid sudden loud audio when you connect your device to CarPlay.

## Wi-Fi Drive

Activate **Wi-Fi Drive** to transfer files from a computer to your device using a desktop web browser, Finder, or File Explorer. Detailed instructions on how to use Wi-Fi Drive are available [here](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalization

Customize the user interface to suit your preferences.

### Application Icon

Choose an alternate application icon for your Home Screen (Premium).

### Color Scheme

Pick the user interface theme and enable dark mode. When **Default** is selected, the application follows the device-wide appearance settings.

### Background Style

Modify the background style of the application. Currently the only option is **Blurred Album Cover**, which uses the currently playing track’s artwork as a blurred app background.

### Appearance of Items in the List

Tune how items are displayed in lists. Useful on small screens — you can let the app adjust row height automatically based on content, or show smaller icons in list cells to give text more space.

### Content Loading Limit

By default the application uses pagination to speed up content loading. You can disable pagination to load everything at once.

### Local Files Screen Style

Change the presentation style of the **Local Files** section.

### Music Library Screen Style

Customize the look of the **Music Library** screen.

### Audio Player Screen Style

Configure the look of the **Audio Player** screen.

### Context Menu Style

Choose the style of the context menu shown when you tap the **More Actions** button.

## Window

Available on Mac and Catalyst. Configure window-related preferences such as default size and behavior on launch.

## Screen

Choose whether the screen should stay active while you are using the application. Useful when scanning large libraries or doing prolonged tag-editing work.

## Accessibility

Activate **Text Mode** to hide all images in the user interface. Text Mode is enabled automatically when VoiceOver is active and is also useful for very small or text-only setups.

## Language

Change the application language and override the system default. The change applies after you fully quit and reopen Flacbox. Currently supported localizations include: Afrikaans, Akan, Albanian, Amharic, Arabic, Armenian, Assamese, Aymara, Azerbaijani, Bambara, Bangla, Basque, Belarusian, Bosnian, Bulgarian, Burmese, Catalan, Cebuano, Chinese (Simplified), Chinese (Traditional), Corsican, Croatian, Czech, Danish, Dhivehi, Dogri, Dutch, English, Esperanto, Estonian, Ewe, Filipino, Finnish, French, Galician, Ganda, Georgian, German, Greek, Guarani, Gujarati, Haitian Creole, Hausa, Hawaiian, Hebrew, Hindi, Hmong, Hungarian, Icelandic, Igbo, Iloko, Indonesian, Irish, Italian, Japanese, Javanese, Kannada, Kazakh, Khmer, Kinyarwanda, Korean, Krio, Kurdish, Kurdish Sorani, Kyrgyz, Lao, Latin, Latvian, Lingala, Lithuanian, Luxembourgish, Macedonian, Maithili, Malagasy, Malay, Malayalam, Maltese, Māori, Marathi, Mizo, Mongolian, Nepali, Northern Sotho, Norwegian Bokmål, Nyanja, Odia, Oromo, Pashto, Persian, Polish, Portuguese, Punjabi, Romanian, Russian, Samoan, Sanskrit, Scottish Gaelic, Serbian, Shona, Sindhi, Sinhala, Slovak, Slovenian, Somali, Southern Sotho, Spanish, Sundanese, Swahili, Swedish, Tajik, Tamil, Tatar, Telugu, Thai, Tsonga, Turkish, Turkmen, Ukrainian, Urdu, Uyghur, Uzbek, Vietnamese, Welsh, Xhosa, Yiddish, Yoruba, Zulu.

## Backup & Restore

Use this feature to back up all of your application data or migrate it to another device. You can choose what to include:

- **Database** — all your tracks in the music library, including playlists. Offline tracks are not included to keep the backup file size manageable.
- **Album Covers** — all your cached album covers.
- **Settings** — all your application settings.

Tap **Backup Application Data** to start the backup. Application data is written to a single file you can use later to restore the application state on a new device or after reinstalling the application.

To restore application data on a new device, move the backup file to the new device using a connected cloud service or iCloud and open it on the new device.

Detailed step-by-step instructions: [How to Transfer Your Music Library Between Devices: Step-by-Step Guide](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Help

Access the application guide for assistance and guidance on using the app effectively.

## Frequently Asked Questions

Find answers to common questions in the FAQ section.

## Send Feedback

Have feedback or need assistance? Send your feedback to our support team directly from the app.

## Share This App

Share the application with your friends to spread the word.

## Discover More Apps

Explore other apps from Everappz.

## Terms and Conditions

Outlines the terms and conditions for using the application. Please read them before using the application.

## Privacy Policy

Visit the privacy policy page to understand our data-handling practices. Please read it before using the application.

## Analytics and Data Collection

Check which services are enabled for analytics and data collection and deactivate any you do not want.

## Legal Notices

Contains information about every library used in the application along with the app version number and build information.
