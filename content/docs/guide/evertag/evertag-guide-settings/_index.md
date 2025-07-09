---
title: "Settings"
date: 2020-02-01
draft: false
description: "Explore every setting in Flacbox, from playback preferences and equalizer tweaks to metadata sync, playlist control, file transfers, UI customization, and Premium upgrade steps."
keywords: [
  "Flacbox settings", "audio player configuration", "premium upgrade Flacbox",
  "WiFi drive", "metadata synchronization", "equalizer", "playback speed", 
  "playlist duplicates", "file manager settings", "offline music sync", 
  "audio tags editor", "dark mode", "restore purchases", "backup settings"
]
tags: ["guide", "flacbox", "settings"]
readingTime: 14
aliases:
  - /guide-evertag-settings/
---

On this screen, you can access the application settings and upgrade it to the Premium version.

![flacbox settings screen](21260c_9cc76041f09447d0b809e8d36f64fd95~mv2.png)

## Upgrade to Premium

Upgrade the application to the Premium version to remove all limits. The free version of the application offers one-lifetime in-app purchase and two subscription options that allow you to remove all restrictions and upgrade to the Premium version.  

Also, please keep in mind that **Family Sharing** is enabled for all purchases and plans, so you can share the Premium version with members of your family.  

You can read more about purchases and Premium version here: [What is the difference between Flacbox and Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Sharing Purchases Between iOS and Mac

Please keep in mind that lifetime purchases and subscriptions are shared between iOS and Mac, using iCloud to sync this information. If you have the premium version on your iOS device, please ensure you have the latest version installed and that iCloud is enabled. Start the app on iOS and wait one minute for your purchase information to upload to iCloud.

You can also try pressing the "Restore Purchases" button in the app settings. Afterward, install the latest app version from the App Store on your Mac and start the app. Ensure you have an internet connection and are using the same iCloud and App Store account on your Mac that you used on your iOS device. Wait one minute for the app to download purchase info from iCloud. The premium version should activate on your Mac automatically.

## Restore purchases on a New Device

To restore your purchase on the new device just use the **Purchases -> Restore purchases** menu. You will see the list of your purchases. If you don't see all your purchases please check if the device is connected to the same iTunes account that was used to make purchases, and make sure iCloud is enabled.

## Try Premium for Free 

You can upgrade to the Premium version for free but for a limited time only using this menu. Just watch an advertisement or tell your friends about this app to get the Premium version for free.

## Purchases 

You can restore previous purchases from this menu. If you encounter activation errors, try enabling the “Restore Purchases at App Launch” option.

## What’s new 

This menu is available after new version released. You can see what is new in the updated application.

## Audio Player

To access settings, tap the "more" button on the player screen and choose "Settings." Here, you'll find various sections:

![audio player settings menu](21260c_5287929e77cb4f9b9c962b99df5f9f30~mv2.png)

### General

These settings cover the fundamental aspects of the audio player, including the playback queue, audio output, and saving the player's state. Available options:

- **Repeat Mode:** This setting lets you choose how the audio player behaves when a track finishes playing. You can select from various options:
  - "Repeat all" – This replays all the tracks in your queue.
  - "Repeat one" – It repeats only the current track.
  - "Repeat Stop" – This pauses playback when the current track ends.
  - "Repeat None" – It allows your queue to play through without repeating.

- **Shuffle Mode:** This option randomizes the order of tracks in your queue, creating a new sequence for playback. You can turn it "Shuffle off" or "Shuffle on."

- **Audio Codec:** You can change the audio codec used for playing tracks in the application. Your choices include:
  - "System codec + FFMPEG" – This prioritizes the system's audio codec where possible, enhancing compatibility and stability during playback. Note that pitch correction and audio output sample rate adjustments may not be available.
  - "FFMPEG" – This forces the use of the FFMPEG codec for all audio files, allowing you to tweak pitch correction and audio output sample rate.

![general player settings screen](21260c_af5ca9a962bb4133a2155286f32fca00~mv2.png)

- **Audio Output Sample Rate:** Adjust the audio output sample rate to optimize sound quality. This feature is useful if you have an external DAC (Digital-to-Analog Converter) connected to your device. You can pick values like "44.1 KHz," "48 KHz," "64 KHz," "88.2 KHz," or "96 KHz."

- **Audio Output Number of Channels:** If you're using a multichannel audio system with an external DAC, this setting allows you to specify the number of channels. Options include "Mono," "Stereo," "Center, Left, Right," "Center, Left, Right, Surround," "ITU BS.775-1," "5.1 Surround," and "SDDS."

- **Audio Output Preferred IO Buffer Duration:** This option allows you to configure the input/output buffer duration for audio playback on your device. A typical value for input/output buffer duration to minimize latency while playing high-resolution audio is around 5 milliseconds (0.005 seconds). Keep in mind that the actual acceptable buffer size may vary depending on the specific hardware and software environment. It's essential to test different buffer durations on your target device and choose the one that provides the best compromise between low latency and stable audio playback without glitches.

- **Audio Output Mode (iOS Only):** This feature is exclusive to iOS and enables you to configure an audio output mixed mode. It allows audio from the app to blend seamlessly with other applications. Detailed instructions can be found [here](/docs/howto/how-to-record-video-while-playing-music-on-iphone).

- **Save Playback Position:** This option ensures that the application saves and restores the playback position for songs in your music library.

- **Save Audio Player State:** When enabled, this feature preserves your audio player's state before you close the app. This makes it easy to pick up where you left off. To continue playback, tap the "Continue Playback" button located at the top of the screen when you re-open the app. You can also restore playback for individual files by tapping on the specific track.

Once you’ve enabled both of these features, open any folder, album, artist, or genre within the app. You’ll notice a ‘Continue Playback’ button at the top of the screen, along with the last saved song playback position. To restore the playback progress, simply tap on the ‘Continue Playback’ button. If you want to restore playback for an individual file, tap on that specific file.

### Personalization

Personalization allows you to customize the look of the audio player screen, change the available controls on the main screen of the audio player, lock screen, and status bar during audio playback, and configure skip time controls.

![personalization settings screen](21260c_e1dee3c68a554c5f9a46ab1c6c713e4e~mv2.png)

- **Audio Player Screen Style:** You can configure the positioning of elements on the audio player screen.
  
- **Album Covers Scrolling Style:** You can configure the preferred album covers scrolling style on the audio player screen.

- **Additional Elements:** This allows you to enable additional elements on the audio player screen. Enabling ‘Audio Format Info’ will show the now-playing track’s audio info above the artwork picture. Enabling the ‘Audio Volume Slider’ will show the audio output slider below the playback controls on the main screen of the audio player.

- **Main Screen Actions:** This allows you to configure which buttons should be visible on the main audio player screen by default. Possible values include Repeat and Shuffle Mode, Next and Previous Song, Skip Time, Sleep Timer, Google Chromecast, AirPlay and Bluetooth, Audio Equalizer, Search, Bookmarks, Speed, Add Bookmark, Add to Favorites, Comments, and others.

- **Playback Controls on the Lock Screen:** You can set which controls should be enabled on the lock screen. Possible values are Skip Time, Add Bookmark, and Add to Favorites.

- **Skip Time Buttons:** You can select the time interval for the ‘Skip Time’ buttons here.

### File Loading

During the file loading process, you can change the network type that app uses to load songs. Available options - "Wi-Fi", "Wi-Fi and Cellular data".

- **Preloading time:** Set buffering time interval. You may increase this value if you have a bad network connection.

- **Use direct URL:** when this option is enabled a direct URL will be used to load the song if the server supports it. This can speed up song loading but may affect playback stability.

### Audio Equalizer

This section is where you can customize the audio equalizer settings. You can read more about configuring audio equalizer [here](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

![audio equalizer settings screen](21260c_107b9a57dca44551b1b7bbb0f4a9bc9c~mv2.png)

### Playback Speed

Adjust the playback speed of the audio player to your liking.

![playback speed screen](21260c_7d20cdc138e7492d88b0646f20fd5378~mv2.png)

### Pitch Correction

Change pitch correction settings using the predefined values. You can also switch between predefined values and precise mode by tapping the button in the top right corner.

![pitch correction screen](21260c_8b278d6d7fd54104b1655fdaf66b2a16~mv2.png)

### Playback Cache

Songs in the audio player queue are automatically downloaded to ensure smooth playback. If you manually download audio files, you can disable this option to avoid duplicates. You can also configure the audio player cache size here.

![audio player cache settings screen](21260c_d1430e6328994723916c9dead4d05b20~mv2.png)

### Sleep Timer

Activate a timer to automatically stop playback after a specified period. This feature can be handy when you want to listen to music as you fall asleep. If you need more precise adjustments, activate the precise mode by tapping the configuration icon in the top right corner.

![sleep timer settings screen](21260c_0e84493d6c6f4a0fa7ac62c33e4727db~mv2.png)

## Library

Your music library settings like automatic sync, metadata reading, loading of album artworks, playlists are located here.

![Music library settings screen](21260c_32a25b477f5249909a7b4e33047144f5~mv2.png)

### Metadata Reading

When you add tracks to the library, the metadata reader gets to work. This background process reads all metadata from your tracks and organizes them by Artist, Album, Genre, and Composer. You have the flexibility to adjust the speed of metadata reading to load data faster, but be aware that this may use more energy. You can also disable the metadata reader and display file names instead of tag information.

![Metadata Synchronization screen](21260c_9d22c93f1e574ffc9e2b9f189fedac62~mv2.png)

Importantly, the metadata reader only updates metadata in your music library and does not alter the files stored in your cloud account or local storage. If you wish to edit metadata for audio files, you can do so using the built-in tags editor, which you can activate from the corresponding action in the options menu.

When the **Metadata reading in the background** switch is on, the metadata reader works in background mode. However, please note that if the app consumes a lot of energy during audio playback, the iOS operating system may suspend it.

So, if you have a large music collection, it's advisable to use the desktop version of the application for metadata synchronization. You can then use the data backup and restore feature to transfer the synchronized music library from the desktop, which is available in app settings.

When the **Normalize metadata encoding** is enabled, the app will automatically normalize metadata encoding for all songs in the music library. This fixes issues where audio tags’ encoding is broken (such as after editing files on a Windows PC) and prevents incorrect information from displaying while a track is playing or added to the library.

The **Reload metadata** action will flag all files in your music library as having missing metadata, triggering the metadata reader to refresh the metadata for every file in your music library.

Tap the **Start Metadata Reading** action to start the metadata reader. The operation progress will be displayed below.

### Online Synchronization

Automatic online music sync allows you to add tracks from connected cloud services to the music library automatically. To activate this feature, head to music library settings and select sync folders.

![Online Music Synchronization screen](21260c_ac7c155c66ba48ca972c80f3c0d66950~mv2.png)

With this option enabled, the application scans all selected folders, identifies supported audio files, and seamlessly integrates them into your library. You can start or stop synchronization by tapping on the corresponding menu action.

![Synchronized online folders selection screen](21260c_cd8c111c7ab640e5be6f15e775f7259c~mv2.png)

Online music synchronization operates exclusively when the app is in the foreground, which means synchronization may take some time. To speed up the process, leave your app open, connect it to a power source, and enable **'Screen' -> 'Always active'** option in application settings.

Alternatively, you can perform online music synchronization on the desktop version of the app and transfer the music library to the iOS version using the data backup restore feature.

You can also set how often you want to synchronize your online music library. If you set it to **"Immediately"**, online sync will start every time you open the application.

![Online synchronization time interval screen](21260c_30f554b0d0a3473ba7628539ce26ace8~mv2.png)

### Offline Synchronizationh

Here you can configure offline music synchronization.

![Offline Music Synchronization screen](21260c_f6b45dbcf5cc4dd282857d348d946003~mv2.png)

#### Synchronized Offline Folders

When you make an online folder on your cloud server available offline (using the **More Actions** menu), this folder will appear here. The folder content will be downloaded to the **Local Files -> Offline Folders** section. When you change the online folder on the cloud server (adding, removing, or updating files), the app will check for changes and update the local copy of this folder on your device.

On this screen, you can manually start offline folder synchronization, show the offline folder in its enclosing folder, and disable offline mode for this folder. Disabling offline mode will remove all local copies of files from your device.

![Synchronized Offline Folders screen](21260c_d4e0b5f422894598a3ab2f1eaafe7657~mv2.png)

#### Time Interval

You can set the time interval for how often the app should check offline folders for modifications.

#### Start Local Folders Scanning

This option scans all local folders located in the application’s **Documents** directory to find supported audio files. All these local files are seamlessly added to your music library. Local files located on your device but outside of this application must be added to the music library manually, as the app does not have access to files outside the application Documents directory due to iOS/MacOS security restrictions.

**Important:** It is advisable to periodically initiate offline music synchronization to keep your music library updated with your local files.

### Personalization

In this section, you can configure the music library screen style to suit your preferences. Three options are available: Plain menu, Grouped menu, Tabbed menu. Also you can enable or disable showing album covers in album details screen.

![Personalization screen](21260c_468417e440b846a59af908d5101901b6~mv2.png)

### Album Covers

Here, you can enable the search for album covers within your music folders. You can also choose the quality of album covers stored on your device and manage your cached album covers. By default, the app will check for embedded album covers in your tracks and display them if available. If there are no embedded album artworks and the ‘Search in the folder’ option is enabled, the app will check the enclosing folder for JPEG or PNG images and use them as album artwork for all tracks in that folder.

![Album Covers Settings Screen](21260c_bafa8d6fb0a4465ba696af582c0074aa~mv2.png)

### Playlists

You can enable the option to add the same song to a playlist twice. By default, this option is disabled.

![Playlists Settings](21260c_8f67546ed47245169983fcea35d5af3f~mv2.png)

### Recents

You can manage your recently played songs list.

![Recents screen](21260c_0a400318ca3c45dfb10659b151430bb9~mv2.png)

- **Delete List:** You can delete the entire list of recently played songs.
- **Change List Size:** You can set the number of items that should appear in the list.
- **Export Songs List:** Use this action to export your recently played songs list in different formats: M3U, CSV, or TXT. Detailed instructions are available on our website [here](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

![Export Songs List screen](21260c_eace98a1cc344e7299377aba42f18512~mv2.png)

### Favorites

You can manage the list of your favorite songs.

- **Simultaneous Editing:** Enable this option to add a song to the favorites list in both the music library and the files section simultaneously.
- **Delete List:** You can delete the entire list of favorite songs.
- **Export Songs List:** Similar to the Recents section, you can export the list of your favorite tracks in different formats: M3U, CSV, or TXT.

![Favorites screen](21260c_64e95955fadf4605930ac98e9bafa0f3~mv2.png)

### Delete music library

This action will erase the music library database, but it will leave your music files untouched.

## Passcode

Activates the password protection screen if you want to protect your application data.

![Passcode screen](21260c_9c328f0298394b549003f899602704e3~mv2.png)

## File manager

![File manager screen](21260c_c2881a78d2c94d53b977c577fd0fc459~mv2.png)

### File transfers

Choose your network preference when downloading files to your device.

#### Maximum number of parallel tasks

Set the number of parallel download threads. Choosing a higher number will speed up file downloads but may require extra battery power.

#### File transfer tasks

Displays currently active upload/download tasks.

#### Background transfers

You can enable downloads even when the app is running in the background. Please be aware that if this operation consumes a significant amount of energy, the operating system may suspend the app.

#### Save downloaded files to

Define your default downloads directory or opt to be prompted every time to choose where to save files.

#### Synchronized offline folders

Manage synchronization of selected offline folders. If you want to synchronize a folder for offline playback, tap the three dots button near the folder name and select ‘Available Offline Mode.’ All new files added to the cloud folder will be downloaded to your device automatically. You can read more about offline modes [here](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

#### Time interval

Select the time interval for synchronizing offline folders. If you choose "Immediately," offline folders will be synchronized every time you open the application.

#### Show full filenames

Activate this option if you need to view complete filenames, including extensions, in the file manager.

#### Edit online files

You can disable online file editing and switch to a read-only mode for connected cloud services to prevent accidental file deletions. This action removes file editing operations from the user interface.

#### Copy files when opening

Specify how the app should handle imported files from other applications.

#### Thumbnails for files

Delete and manage generated file thumbnails to free up storage space.

#### Delete temporary files

Clear the application's cache folder to reclaim storage space.

## Audio tags editor

![Audio tags editor screen](21260c_1bac9f60647347c5b1f3f493bd3a546b~mv2.png)

In this section, you can configure the built-in audio tags editor.

### Album cover scaling

Here you can select the scaling method for the album cover when saving it to audio tags.

### Update online files

You can enable this option, and the application will automatically update the file's metadata on a cloud server after you've finished editing it.

### Edit online files

You can choose whether the application should delete the downloaded file after you've finished editing the online file on a cloud server.

### Main screen buttons

You can choose which buttons should be available on the main screen of the audio tags editor.

## CarPlay

You can change CarPlay settings here. This menu also abailable in CarPlay interface allowing you to optimize it.

### Sort

You can change sort options here for all CarPlay screens.

### Content loading limit

You can select if the app should use pagination in CarPlay screen.

### Show images

You can disable images on CarPlay screen to optimize loading speed.

### Pause playback when connected

You can enable this to avoid sudden loud audio when you connect to CarPlay interface.

## WiFi-Drive

In this section, you can activate the WiFi Drive feature, which allows you to transfer files from your computer to this device using a desktop web browser. We have detailed instructions on how to use WiFi Drive [here](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

![WiFi-Drive screen](21260c_47d7e22d7d7542119123cee8d3ae24b8~mv2.png)

## Personalization

In this section, you can customize the user interface settings to suit your preferences.

### Application icon

Select an application icon for your home screen, whether you want a fresh new look or something that matches your style.

### Color scheme

Customize the user interface theme and enable dark mode here. When the default option is selected, the application will adapt its color scheme based on your device's appearance settings.

### Background style

Modify the background style of the application. Currently, the only available option is "Blurred album cover." When enabled, a blurred album cover image will serve as the application's background.

### Appearance of items in the list

Here you can customize how items in the list are displayed, which is especially useful for devices with smaller screens. You can choose whether the app should automatically adjust the height based on the content or show smaller icons in list cells to provide more space for text.

### Content loading limit

By default, the application uses pagination to speed up content loading. However, you can opt to disable this feature, allowing the application to load all available data at once.

### Local files screen style

Change the presentation style for the "Local files" section to your preference.

### Music library screen style

Customize the style of the "Music library" screen to suit your taste.

### Audio player screen style

Configure the style of the "Audio player" screen to match your preferences.

### Context menu style

Select a style for the context menu that appears when you tap the 'More Actions' button.

## Screen

In this section, you have the option to customize whether the screen should stay active while you're using the application.

## Accessibility

In this section, you can activate text mode for the application, which hides all images. This feature is automatically enabled when VoiceOver is active.

## Language

![Language screen](21260c_d18ffeafea86496a9bbd5d2629aa3c28~mv2.png)

In this section, you can change the application language and override the default system settings. Currently, the app supports following localizations: Afrikaans, Akan, Albanian, Amharic, Arabic, Armenian, Assamese, Aymara, Azerbaijani, Bambara, Bangla, Basque, Belarusian, Bosnian, Bulgarian, Burmese, Catalan, Cebuano, Chinese, Simplified, Chinese, Traditional, Corsican, Croatian, Czech, Danish, Dhivehi, Dogri, Dutch, English, Esperanto, Estonian, Ewe, Filipino, Finnish, French, Galician, Ganda, Georgian, German, Greek, Guarani, Gujarati, Haitian Creole, Hausa, Hawaiian, Hebrew, Hindi, Hmong, Hungarian, Icelandic, Igbo, Iloko, Indonesian, Irish, Italian, Japanese, Javanese, Kannada, Kazakh, Khmer, Kinyarwanda, Korean, Krio, Kurdish, Kurdish, Sorani, Kyrgyz, Lao, Latin, Latvian, Lingala, Lithuanian, Luxembourgish, Macedonian, Maithili, Malagasy, Malay, Malayalam, Maltese, Māori, Marathi, Mizo, Mongolian, Nepali, Northern Sotho, Norwegian Bokmål, Nyanja, Odia, Oromo, Pashto, Persian, Polish, Portuguese, Punjabi, Romanian, Russian, Samoan, Sanskrit, Scottish Gaelic, Serbian, Shona, Sindhi, Sinhala, Slovak, Slovenian, Somali, Southern Sotho, Spanish, Sundanese, Swahili, Swedish, Tajik, Tamil, Tatar, Telugu, Thai, Tsonga, Turkish, Turkmen, Ukrainian, Urdu, Uyghur, Uzbek, Vietnamese, Welsh, Xhosa, Yiddish, Yoruba, Zulu

## Backup & Restore

![Backup & Restore screen](21260c_07a50c600fae45d7b9964475a6eb28da~mv2.png)

Use this feature to backup all your application data or migrate it to another device.

You can choose which data you want to migrate:

- **Database:** All your tracks in the music library, including playlists. Offline tracks will not backup to optimize backup file size.
- **Album Covers:** All your cached album covers.
- **Settings:** All your application settings.

To start the backup operation, just tap the **Backup Application Data** button. Application data will be backed up to a file, and you can use it in the future to restore the application state on a new device or after reinstalling the application.

If you need to restore application data on a new device, move the backup file from this device to the new device using a connected cloud service or iCloud and open it on the new device.

We have detailed instruction about how to use data backup and restore feature here: [How to Transfer Your Music Library Between Devices: Step-by-Step Guide](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Help

Access the application guide for assistance and guidance on using the app effectively.

## Frequently Asked Questions

Find answers to common questions in the FAQ section.

## Send Feedback

Have feedback or need assistance? Send your feedback to our support team.

## Share This App

Share this application with your friends and spread the word.

## Discover More Apps

Explore our other apps and discover more from our collection.

## Terms and Conditions

This section outlines the terms and conditions for using the application. Please read it before using the application.

## Privacy Policy

Visit the privacy policy page to understand our data handling practices. Please read it before using the application.

## Analytics and Data Collection

Here you can check what services are enabled for analytics and data collection and deactivate them if you need.

## Legal Notices

This section contains information about all the libraries and app version details used in the application.