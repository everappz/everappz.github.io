---
title: "Settings"
date: 2020-01-01
description: "Explore all settings in Evermusic including audio configuration, music library sync, offline folders, metadata, personalization, accessibility, widgets, CarPlay, and backup options."
keywords: [
  "Evermusic", "settings", "audio settings", "music library sync",
  "offline folders", "equalizer", "crossfade", "gapless playback",
  "audio processor", "playlist settings", "premium upgrade",
  "restore purchases", "file manager", "tags editor", "WiFi drive",
  "voiceover", "app backup", "accessibility", "localization",
  "widgets", "CarPlay", "spatial audio", "audio pitch"
]
tags: ["evermusic", "guide", "settings"]
readingTime: 16
aliases:
  - /post/evermusic-guide-settings/
  - /guide-evermusic-settings/
---


The Settings screen is the control center of Evermusic. From here you can upgrade to Premium, configure the audio player, manage your music library, set up the file manager, customize the interface, enable widgets and CarPlay, back up your data, and access help and legal information. Sections are grouped under headers: **Purchases & updates**, app preferences, **Help**, and **Legal & privacy**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic Settings Screen" image="/docs/guide/evermusic/evermusic-guide-settings/img/settings-main-screen.webp" >}}
{{< /cards >}}

## Purchases & Updates

### Upgrade to Premium

Upgrade the application to the Premium version to remove all limits. The free version offers one lifetime in-app purchase and two subscription options that unlock the full feature set.

Family Sharing is enabled for all purchases and plans, so you can share the Premium version with members of your family.

You can read more about purchases and the Premium version here: [What is the difference between Evermusic and Evermusic Premium](/docs/faq/evermusic/what-is-the-difference-between-evermusic-and-evermusic-premium/).

#### Evermusic Free (Blue Icon) vs Evermusic Pro (Red Icon)

Evermusic is published on the App Store under two different icons / colors:

- **Evermusic Free (blue icon)** is split into **two separate App Store apps with different bundle IDs** — one for **iOS / iPadOS** and a dedicated one for **macOS** (Universal binary that runs on both **Apple Silicon and Intel Macs**). Premium in-app purchases are **shared between the iOS and Mac blue apps via iCloud** — buy Premium on iPhone and it automatically activates on the Mac (and vice versa), as long as both devices use the same Apple ID with iCloud enabled.
- **Evermusic Pro (red icon)** is a **single App Store app** with a **single bundle ID** that runs on **iPhone, iPad, and Apple Silicon Macs (M1 and later)**. It has the **same functionality as Evermusic Free with an activated Premium plan**. The red app **does not support Intel Macs**, which is why its price is slightly lower than the equivalent Premium purchase in the blue app. Evermusic Pro also **does not collect any user diagnostics or analytics at all** — analytics are completely disabled in the build, with no opt-in option.

Because the bundle IDs differ between blue and red, a Premium in-app purchase activated in the blue app does not unlock the red app for free, and vice versa. If you already use the blue app with Premium activated, there is no need to install the red app — you already have everything Pro offers.

### Sharing Purchases Between iOS and Mac

Lifetime purchases and subscriptions are shared between iOS and Mac using iCloud. If you already own Premium on iOS, make sure you have the latest version installed and that iCloud is enabled. Start the app on iOS and wait one minute for your purchase information to upload to iCloud.

You can also tap **Restore Purchases** in app settings. Afterwards, install the latest app version from the App Store on your Mac and start the app. Ensure you have an internet connection and are signed in with the same iCloud and App Store account on both devices. Wait one minute for the app to download purchase information from iCloud. The Premium version should activate on your Mac automatically.

### Restore Purchases on a New Device

To restore your purchase on a new device, use **Purchases → Restore Purchases**. You will see the list of your purchases. If anything is missing, verify that the device is connected to the same iTunes account that was used to make the purchases and that iCloud is enabled.

### Try Premium for Free

You can upgrade to the Premium version for free for a limited time using this menu. Watch a short advertisement or share the app with friends to unlock Premium temporarily.

### Purchases

Restore previous purchases from this menu. If you encounter activation errors, try enabling the **Restore Purchases at App Launch** option.

### Software Update

Tap **Software Update** to check whether a newer version of Evermusic is available. The app will compare your installed version with the latest version on the App Store and let you know if an update is recommended.

### What’s New

This menu becomes available after a new version is released. It shows a summary of the changes and new features included in the most recent update.

## Audio Player Settings

All audio player settings are grouped here: equalizer, crossfade playback, audio player cache, song loading, and more. Settings are organized into logical sub-sections.

### General

This sub-section contains general playback queue, audio output, and state-saving settings.

#### Repeat Mode

Specifies the audio player’s behavior when a track finishes playback:

- **Repeat all** – loops all tracks in your player queue.
- **Repeat one** – repeats only the current track.
- **Repeat stop** – pauses playback when the current track ends.
- **Repeat none** – lets your queue play through without repeating.

#### Shuffle Mode

Plays the tracks in a randomized order. This actually shuffles the queue and plays tracks one by one in the new order. Available values: **Shuffle off** and **Shuffle on**.

#### Audio Processor

Possible values: **AVFoundation** and **CoreAudio**. By default, AVFoundation is used. Due to a known issue with AVFoundation on iOS 17.0–17.6, crossfade playback and the audio equalizer cannot be used at the same time. To enjoy both crossfade and the equalizer on those iOS versions, switch to the CoreAudio audio processor.

If you experience issues with gapless playback using AVFoundation, try CoreAudio as well. The only limitations of CoreAudio are internet streaming of some radio stations and certain audio formats, since it does not support every system audio format (such as M4A and a few others).

#### Audio Output Sample Rate

Set the audio output sample rate from 8 KHz to 384 KHz. This option is available only when the CoreAudio processor is selected.

#### Audio Output Number of Channels

Set the audio output number of channels — **MONO** or **STEREO**. This option is available only when the CoreAudio processor is selected.

#### Audio Pitch Algorithm

Choose the algorithm used for pitch correction. Available values are **Time Domain**, **Spectral**, and **Varispeed**. Useful if you adjust playback speed and want to control the resulting audio quality.

#### Spatial Audio

Spatial audio uses psychoacoustic methods to create a more immersive audio experience on supported headphones and speaker arrangements. Possible values: **Deactivated**, **Mono and Stereo**, **Multichannel**, **Mono Stereo Multichannel**.

#### Audio Output Mode

Available on iOS only. Lets you enable mixed mode so audio from this application blends with other applications. You can find instructions on how to use mixed mode [here](/docs/howto/how-to-record-video-while-playing-music-on-iphone).

#### Save Playback Position

Ensures the application saves and restores the playback position for songs in your music library.

#### Save Audio Player State

Saves the audio player state before closing the application, making it easy to resume from where you left off.

Once both of these features are enabled, open any folder, album, artist, or genre. You will see a **Continue Playback** action at the top of the screen, along with the last saved song and playback position. Tap **Continue Playback** to restore. To resume playback for an individual file, simply tap that file.

### Personalization

Customize the look of the audio player screen, choose which controls are visible on the player, lock screen, and status bar, and configure the skip-time buttons.

#### Audio Player Screen Style

Configure the positioning of toolbars and main controls on the audio player.

#### Album Covers Scrolling Style

Choose the scrolling style for album covers on the audio player screen.

#### Additional Elements

Enable extra elements on the audio player screen. **Audio Format Info** displays the now-playing track’s technical info above the artwork; **Audio Volume Slider** shows the audio output slider below the playback controls.

#### Main Screen Actions

Configure which buttons are visible on the main audio player screen. Available options include Repeat and Shuffle Mode, Next and Previous Song, Skip Time, Sleep Timer, Google Chromecast, AirPlay and Bluetooth, Audio Equalizer, Search, Bookmarks, Speed, Add Bookmark, Add to Favorites, Comments, and more.

#### Playback Controls on the Lock Screen

Choose which extra controls are enabled on the lock screen. Possible values: **Skip Time**, **Add Bookmark**, and **Add to Favorites**.

#### Skip Time Intervals

Select the time intervals used by the forward and backward Skip Time buttons.

### File Loading

Choose the network type used to stream songs. Available options: **Wi-Fi** and **Wi-Fi & Cellular Data**.

#### Preloading Time

Set the buffering time interval. Increase this value if you have a poor network connection.

#### Use Direct URL

When enabled, a direct URL is used to load the song if the server supports it. This can speed up song loading but may slightly affect playback stability.

#### Optimize File Loading

When enabled, the system optimizes song loading for the AVFoundation audio processor, which can improve playback stability. The app uses the technology described [here](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/).

### Audio Equalizer

Configure the audio equalizer. You can read more about presets and EQ configurations [here](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Devices

Connect to an AirPlay or Google Chromecast device (iOS only).

### Playback Speed

Adjust the audio player playback speed. For more precise control, enable the precise slider by tapping the configuration icon in the top right corner.

### Crossfade Playback

Crossfade allows songs to flow seamlessly in a continuous mix — the next song starts playing a few seconds before the current one finishes. Crossfade is not available for AirPlay and Google Chromecast. On this screen, choose how long the current and next song play simultaneously. If you experience issues with crossfade and the audio equalizer at the same time, switch the audio processor as described above.

### Gapless Playback

Gapless playback ensures that songs play without any interruption or silence in between. It is perfect for classical music, live recordings, and concept albums. If you have issues with gapless playback, switch the audio processor as described above.

### Playback Cache

Songs in the audio player queue are downloaded automatically for smooth playback. If you download audio files manually, you can disable this option to avoid duplicates. You can also configure the audio player cache size here. Read more about offline mode and playback cache here: [Play Offline Music in Evermusic & Flacbox: Download & Sync from Cloud to Local Files](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Sleep Timer

Enable a timer to stop playback after a specified timeout. For more precise control, enable precise mode by tapping the configuration icon in the top right corner.

## Library

Music library settings — automatic sync, metadata reading, album cover loading, playlists, recents, and favorites — live here.

### Metadata Reading

When you add tracks to the library, the metadata reader processes them in the background and organizes them by Artist, Album, Genre, and Composer. You can adjust how fast metadata is read to load data faster (at the cost of more battery). You can also disable the metadata reader entirely and show file names instead of tag information.

The metadata reader only updates the music library database; it does not alter files stored in your cloud account or local storage. If you need to edit audio file metadata, use the built-in tags editor via the corresponding action in the options menu.

When **Metadata Reading in the Background** is on, the reader continues working in background mode. If the app uses too much energy during playback, iOS may suspend it.

If you have a large music collection, it is advisable to perform metadata synchronization on the desktop version of the application. You can then transfer the synchronized music library to iOS using the **Backup & Restore** feature.

When **Normalize Metadata Encoding** is enabled, the app automatically normalizes the encoding of metadata for all songs. This fixes issues where audio tag encoding is broken (for example after editing files on a Windows PC) and prevents incorrect characters from appearing in track information.

**Reload Metadata** flags every file in your music library as having missing metadata, which causes the metadata reader to refresh every record.

**Start Metadata Reading** triggers the metadata reader manually. Progress is shown below the action.

### Online Synchronization

Automatic online music sync adds tracks from connected cloud services to the music library automatically. To enable it, open the music library settings and select sync folders.

With this option enabled, the application scans the selected folders, identifies supported audio files, and adds them to your library. Start or stop synchronization with the corresponding menu action.

Online sync runs only when the app is in the foreground, so synchronizing a large library can take some time. To speed things up, keep the app open, connect to a power source, and enable **Screen → Always Active** in settings.

Alternatively, perform online sync on the desktop version of the app and transfer the music library to iOS using **Backup & Restore**.

You can also choose how often online sync runs. Setting the interval to **Immediately** triggers a sync every time you open the application.

### Offline Synchronization

Configure offline music synchronization.

#### Synchronized Offline Folders

When you mark an online folder on your cloud server as available offline (using the More Actions menu), it appears here. The folder content is downloaded to **Local Files → Offline Folders**. When the online folder changes (files added, removed, or updated), the app checks for changes and updates the local copy on your device.

On this screen you can manually start offline folder synchronization, reveal the offline folder in its enclosing folder, and disable offline mode for the folder. Disabling offline mode removes all local copies of files from your device.

#### Time Interval

Choose how often the app checks offline folders for modifications.

#### Start Local Folders Scanning

Scan all local folders in the application Documents directory for supported audio files. Found files are added to the music library automatically. Files located on your device but outside of the application Documents directory must be added to the music library manually, as the app cannot access them due to iOS/macOS security restrictions.

**Important:** It is advisable to periodically initiate offline music synchronization to keep your music library updated with your local files.

### Personalization

Configure the music library screen style. Three options are available: **Plain menu**, **Grouped menu**, and **Tabbed menu**. You can also enable or disable album covers in the album details screen.

### Album Covers

Choose how the application loads and stores album artwork.

- **Network type** — pick **Wi-Fi** or **Wi-Fi & Cellular Data** for cover downloads.
- **Load Album Covers for Online Files** — when enabled, embedded album covers are loaded for files stored in cloud storage. This may use additional network data.
- **Search in the Folder** — when enabled, if a track has no embedded cover, the app looks for JPEG or PNG images in the same folder and uses them as the album artwork.
- **Cover Quality** — select the quality of album covers stored on your device.
- **Show in Folder** — open the folder where album covers are cached so you can manage or back them up.
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

Activates the password protection screen if you want to protect your application data.

## File Manager

The File Manager section controls how files are transferred, stored, and previewed.

### File Transfers

Choose your network preference for downloading files to your device.

### Maximum Number of Parallel Tasks

Set the number of parallel download threads. A higher number speeds up downloads but requires more battery.

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

Configure the built-in audio tags editor.

### Album Cover Scaling

Choose the scaling method used when an album cover is saved into audio tags.

### Update Online Files

When enabled, the application automatically updates a file’s metadata on the cloud server after you finish editing it.

### Delete File After Editing Online

Choose whether the application should delete the downloaded copy after finishing the edit of an online file on a cloud server.

### Main Screen Buttons

Choose which buttons are visible on the main screen of the audio tags editor.

## Widgets

Enable widgets so the app updates widget data during playback. Widget updates require additional energy, so enable this only if you actually use widgets on your Home Screen or Lock Screen.

You can read more about Evermusic widgets in the [Navigation guide](/docs/guide/evermusic/evermusic-guide-navigation/).

## CarPlay

Change CarPlay settings here. This menu is also available inside the CarPlay interface so you can adjust the experience while driving.

### Sort

Configure sort options for all CarPlay screens.

### Content Loading Limit

Choose whether the app uses pagination on the CarPlay screen. Pagination keeps menus responsive on devices with limited memory and large libraries.

### Menu Icons Gradient Color

Select the color scheme for the CarPlay home screen.

### Show Images

Disable images on the CarPlay screen to optimize loading speed and reduce memory usage on large libraries.

### Pause Playback When Connected

Enable this to avoid sudden loud audio when you connect your device to CarPlay.

## Wi-Fi Drive

Activate Wi-Fi Drive to transfer files from a computer to your device using a desktop web browser. Detailed instructions on how to use Wi-Fi Drive are available [here](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalization

Customize the user interface to suit your preferences.

### Application Icon

Choose an alternate application icon for your Home Screen.

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

Choose the style of the context menu shown when you tap the More Actions button.

## Window

Available on Mac and Catalyst. Configure window-related preferences such as default size and behavior on launch.

## Screen

Choose whether the screen should stay active while you are using the application. Useful when scanning large libraries or doing prolonged tag-editing work.

## Accessibility

Activate **Text Mode** to hide all images in the user interface. Text Mode is enabled automatically when VoiceOver is active and is also useful for very small or text-only setups.

## Language

Change the application language and override the system default. Currently the app supports the following localizations: Afrikaans, Akan, Albanian, Amharic, Arabic, Armenian, Assamese, Aymara, Azerbaijani, Bambara, Bangla, Basque, Belarusian, Bosnian, Bulgarian, Burmese, Catalan, Cebuano, Chinese Simplified, Chinese Traditional, Corsican, Croatian, Czech, Danish, Dhivehi, Dogri, Dutch, English, Esperanto, Estonian, Ewe, Filipino, Finnish, French, Galician, Ganda, Georgian, German, Greek, Guarani, Gujarati, Haitian Creole, Hausa, Hawaiian, Hebrew, Hindi, Hmong, Hungarian, Icelandic, Igbo, Iloko, Indonesian, Irish, Italian, Japanese, Javanese, Kannada, Kazakh, Khmer, Kinyarwanda, Korean, Krio, Kurdish, Kurdish Sorani, Kyrgyz, Lao, Latin, Latvian, Lingala, Lithuanian, Luxembourgish, Macedonian, Maithili, Malagasy, Malay, Malayalam, Maltese, Māori, Marathi, Mizo, Mongolian, Nepali, Northern Sotho, Norwegian Bokmål, Nyanja, Odia, Oromo, Pashto, Persian, Polish, Portuguese, Punjabi, Romanian, Russian, Samoan, Sanskrit, Scottish Gaelic, Serbian, Shona, Sindhi, Sinhala, Slovak, Slovenian, Somali, Southern Sotho, Spanish, Sundanese, Swahili, Swedish, Tajik, Tamil, Tatar, Telugu, Thai, Tsonga, Turkish, Turkmen, Ukrainian, Urdu, Uyghur, Uzbek, Vietnamese, Welsh, Xhosa, Yiddish, Yoruba, Zulu.

## Backup & Restore

Back up all of your application data or migrate it to another device. You can choose what to include:

- **Database** — all of your music library tracks and playlists. Offline tracks are not included to keep the backup size manageable.
- **Album Covers** — all of your cached album covers.
- **Settings** — all of your application settings.

Tap **Backup Application Data** to start the backup operation. The application data is written to a single file that you can use later to restore the application state on a new device or after reinstalling the app.

To restore application data on a new device, move the backup file to the new device using a connected cloud service or iCloud and open it on the new device.

We have a detailed step-by-step guide here: [How to Transfer Your Music Library Between Devices in Evermusic: Step-by-Step Guide](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Help

Open the application guide for assistance and guidance on using the app effectively.

## Frequently Asked Questions

Find answers to common questions in the FAQ section.

## Send Feedback

Have feedback or need assistance? Send your feedback to our support team directly from the app.

## Share This App

Share the application with your friends to help spread the word.

## Discover More Apps

Explore other apps from Everappz.

## Terms and Conditions

Outlines the terms and conditions for using the application. Please read it before using the application.

## Privacy Policy

Visit the privacy policy page to understand our data handling practices. Please read it before using the application.

## Analytics and Data Collection

Check which services are enabled for analytics and data collection and deactivate any you do not want.

In **Evermusic Free (blue icon)**, analytics and diagnostics are enabled by default to help us improve the app — you can turn them off here at any time. **Evermusic Pro (red icon) does not include any analytics or diagnostics at all** — the section is empty (or hidden) because nothing is collected, and there is no opt-in option.

## Legal Notices

Contains information about every library used in the application along with the app version number and build information.
