---
title: "प्लेलिस्ट्स"
date: 2020-01-01
description: "Evermusic में playlists create, import, customize, और manage करना सीखें। Editing, sorting, offline mode, और accessibility के लिए detailed steps शामिल हैं।"
keywords: [
  "Evermusic", "playlists", "playlist management", "import M3U playlist",
  "edit playlist", "offline playlist", "change playlist order", "playlist cover",
  "playlist accessibility", "audio player"
]
tags: ["evermusic", "guide", "playlists"]
readingTime: 6
---


## Overview

Playlists section आपको अपने tracks को lists में organize करने के tools प्रदान करता है। इसमें आपके सभी created playlists showcase करने वाला एक content view, navigation bar में एक "..." button जो विभिन्न playlist-related actions offer करता है, और "खोजें," "सभी चलाएं," और "सभी फेरबदल करें" buttons के साथ एक navigation toolbar शामिल है। इसके अलावा, हर individual playlist में playlist title के पास एक "..." button है जो उस playlist के specific actions की range offer करता है।

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic Playlists स्क्रीन" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-main.webp" >}}
{{< /cards >}}

## Playlist बनाना

New playlist create करने के लिए, navigation bar के top right corner में "+" button या "..." button टैप करें, "New playlist" select करें और अपनी playlist को एक name assign करें। Name देने के बाद, "Save" टैप करें।

{{< cards cols="1">}}
  {{< card title="" subtitle="New Playlist बनाएं" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-add-new.webp" >}}
{{< /cards >}}

यह "Add songs" dialog prompt करता है, जहां आप choose कर सकते हैं कि new playlist में कौन से tracks add करने हैं। Tracks source type के अनुसार categorized हैं, और आपके पास कई options हैं:

- **Library**: आपकी music library के Tracks।
- **Files in This Application**: App के Documents directory में stored audio files।
- **Files on This iPhone/iPad/Mac**: App के बाहर, आपके device के अन्य folders में located audio files।
- **संपर्क**: Connected cloud storage services में stored online files।

Default रूप से, आप एक track को playlist में केवल एक बार add कर सकते हैं। Playlist में duplicated songs allow करने के लिए, इस feature को app सेटिंग्स - Music library - प्लेलिस्ट्स - Duplicates in a playlist - Enable में enable करें।

## Playlist Import करें

Evermusic में, हमने M3U file import functionality add की है, ताकि आपको playlists manually create न करनी पड़े।

{{< cards cols="1">}}
  {{< card title="" subtitle="File Source से Playlist Import करें" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-import-from-files.webp" >}}
{{< /cards >}}

पहले, 'प्लेलिस्ट्स' section पर जाएं। फिर, top right corner में 'More' button टैप करें। Appear होने वाले menu से, 'Import Playlist' option select करें।

Next screen पर, file location choose करें। Supported options include करते हैं:

- Connected cloud storage
- Application में files
- आपके device पर files

Connected cloud storage select करते हैं और playlist file वाला folder open करते हैं। Supported playlist file extensions में M3U, M3U8, और CUE शामिल हैं। Playlist file select करें और अपना selection confirm करने के लिए 'Done' टैप करें।

App playlist file parse करेगी, tracks की list create करेगी, और उन files को storage पर locate करेगी एक final playlist compile करने के लिए, जो music library में import होगी। यह crucial है कि आपकी M3U/CUE file में media files के correct paths हों, और files उन paths पर आपके storage पर located होनी चाहिए। Playlist import के बारे में अधिक [यहां](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox) पढ़ सकते हैं।

## Playlist Detail Screen

जब आप कोई playlist खोलते हैं, तो "Playlist detail screen" appear होती है। इस screen पर, top right corner में playlist options के साथ एक "..." button और artwork image के नीचे तीन buttons मिलेंगे: "खोजें," "Continue playback", "सभी चलाएं," और "सभी फेरबदल करें।" इसके अलावा, एक "Offline mode" checkbox है।

{{< cards cols="1">}}
  {{< card title="" subtitle="Playlist Detail Screen" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-detail-screen.webp" >}}
{{< /cards >}}

- **Continue playback**: इस playlist के लिए playback position restore करें।
- **खोजें**: Current playlist के भीतर search perform करें।
- **सभी चलाएं**: Current playlist के सभी tracks को player queue में add करें।
- **सभी फेरबदल करें**: "सभी चलाएं" के समान, लेकिन audio player queue में add करने से पहले tracks shuffle करता है।
- **Offline mode**: इस playlist के सभी tracks को local files में download करें। Playlist में add किए गए कोई भी new items automatically download होंगे।

## Playlists Screen में Playlist के लिए अधिक क्रियाएँ

आप playlist title के पास "..." button टैप करके playlist के लिए actions access कर सकते हैं। यहां available actions हैं:

- **सभी चलाएं:** New player queue में playlist tracks add करता है।
- **Play next:** Existing player queue के top पर playlist tracks add करता है।
- **Play later:** Existing player queue के bottom पर playlist tracks add करता है।
- **Edit image:** Playlist की artwork image edit करें।
- **Offline mode enable करें:** Playlist के लिए offline mode enable करता है। इस scenario में, existing और new tracks दोनों automatically download होंगे। Offline mode के बारे में अधिक [यहां](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/) पढ़ें।
- **Export songs list:** इस playlist को [यहां](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/) described अनुसार different formats में export कर सकते हैं।
- **Add to archive:** इस playlist को [यहां](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to) described अनुसार m3u file, album cover, और सभी tracks सहित archive कर सकते हैं।
- **Add songs:** Current playlist में more songs add करें।
- **Rename:** Playlist rename करें।
- **Delete playlist:** Playlist को Music library से delete करें। कृपया ध्यान दें कि यह action undone नहीं की जा सकती।

{{< cards cols="1">}}
  {{< card title="" subtitle="Playlist के लिए अधिक क्रियाएँ मेनू" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-more-actions-for-separate-playlist.webp" >}}
{{< /cards >}}

## Playlist Detail Screen में Playlist के लिए अधिक क्रियाएँ

आप top right corner में "..." button टैप करके playlist के लिए actions access कर सकते हैं। यहां available actions हैं:

- **चुनें:** Track selection mode activate करता है, playlist से multiple tracks delete करने या उनका order change करने के लिए useful।
- **Play next:** Existing player queue के top पर playlist tracks add करता है।
- **Play later:** Existing player queue के bottom पर playlist tracks add करता है।
- **Add songs:** Playlist में new songs add करें।
- **Rearrange songs:** Drag-and-drop का उपयोग करके playlist में songs का order manually change करें।
- **Rename:** Current playlist rename करें।
- **Edit image:** Current playlist के लिए album artwork edit करें।
- **Export songs list:** इस playlist को different formats में export करें। आप अधिक [यहां](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/) पढ़ सकते हैं।
- **Add to archive:** सभी tracks और m3u file सहित current playlist zip करें। आप अधिक [यहां](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to) पढ़ सकते हैं।
- **Sort:** Playlist में tracks का order change करें। Sorting options include करते हैं "Song title," "Song number," "Album," "Artist," "Album artist," "Genre," "Composer," "Rating," "Year," "Beats per minute," "Duration," "File name," "File modification date," "File creation date," और "Manual।" "Manual" sort option drag-and-drop का उपयोग करके songs का manual reordering allow करता है।
- **खोजें:** Current playlist के भीतर specific song search करें।
- **Grid/List:** Screen layout presentation change करें।
- **Delete playlist:** Playlist को Music library से delete करें। Importantly, यह action आपके storage से tracks delete नहीं करती, और यह undone नहीं की जा सकती।

## Playlist में Song Order बदलना

Playlist में songs का order change करने के लिए, top right corner में "..." button टैप करें और selection mode enter करने के लिए "चुनें" select करें। हर track के पास reorder control और drag-and-drop gestures का उपयोग करके उन्हें up या down move करें। Reorder control पर टैप करने से track list के top पर move हो जाएगा। Selection mode exit करने और changes apply करने के लिए, "Done" टैप करें।

{{< cards cols="1">}}
  {{< card title="" subtitle="Playlist में Song Order बदलें" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-change-songs-order.webp" >}}
{{< /cards >}}

## Playlist Cover Image बदलना

Playlist की cover image change करने के लिए, top right corner में "..." button टैप करें और "Edit image" select करें। Available sources से एक image choose करें और "Done" टैप करके changes confirm करें।

## Playlist में Songs जोड़ना

Playlist खोलें और top right corner में "..." button टैप करें, फिर dialog खोलने के लिए "Add songs" select करें। जो tracks add करने हैं उन्हें choose करें और "Done" टैप करके changes confirm करें।

## Playlist से Multiple Songs Delete करना

Playlist खोलें, top right corner में "..." button टैप करें, और selection mode enter करने के लिए "चुनें" select करें। जो tracks delete करने हैं उन्हें choose करें और screen के bottom पर "Delete from playlist" button टैप करें। "Done" टैप करके changes confirm करें।

{{< cards cols="1">}}
  {{< card title="" subtitle="Playlist Details Screen के अंदर Selection Mode" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-selection-mode-in-playlist-details-screen.webp" >}}
{{< /cards >}}

## Track Options

Playlist के हर track में actions की एक list है, "..." button टैप करके accessible। अगर आप सभी actions नहीं देख सकते, तो उन्हें view करने के लिए scroll down करें। आप track को playlist से delete कर सकते हैं, download कर सकते हैं, audio tags edit कर सकते हैं, और अधिक।

{{< cards cols="1">}}
  {{< card title="" subtitle="Playlist में Track Options Menu" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-track-options.webp" >}}
{{< /cards >}}

- **Play next:** Track को player queue के top पर adds करता है।
- **Play later:** Track को player queue के bottom पर appends करता है।
- **Playlist में जोड़ें:** Track को playlist में adds करता है।
- **पसंदीदा में जोड़ें:** Quick access के लिए track को favorite के रूप में marks करता है।
- **डाउनलोड करें:** Track को offline available बनाता है। यह transfer queue और Music library के "Downloaded music" section में "Local Files" tab में appear होगा।
- **ऑडियो टैग संपादित करें:** Track metadata change करने के लिए built-in tags editor खोलता है।
- **Open in:** Track को export करता है और इसे किसी दूसरे app में खोलता है।
- **Show in folder:** जहां audio file located है उस folder को reveals करता है।
- **Show in Finder:** आपके Mac से import की गई files के लिए, यह action आपके Mac computer पर audio file located folder को reveals करता है।
- **Delete from playlist:** Playlist से track deletes करता है।
- **Delete from cloud service:** Playlist और associated cloud service से track deletes करता है। कृपया ध्यान दें कि यह action undone नहीं की जा सकती।
- **Delete from music library:** Music library से track deletes करता है, storage पर file untouched रखता है।

## Accessibility

हमारा app VoiceOver technology के साथ fully accessible है, हर component में well-designed label और description ensure करते हुए। VoiceOver active होने पर, app user interface को text mode में translate करती है, navigation speed और convenience improve करने के लिए केवल accessible और useful elements display करती है। आप सेटिंग्स > Accessibility > Text Mode में text mode भी activate कर सकते हैं।

VoiceOver के साथ playlist में track position adjust करने के लिए:

1. Playlist खोलें और "More" button टैप करें।
2. "Change Songs Order" select करें। View editing mode पर switch हो जाएगी।
3. Track title के पास reorder indicator icon टैप करें उसे focus देने के लिए।
4. Reorder indicator icon quickly double-tap करें। Second tap पर, अपनी finger release न करें — hold करें जब तक आप एक sound न सुनें जो indicate करे कि cell move के लिए ready है।
5. अब, आप cell को new position पर move कर सकते हैं।

अन्य components expected रूप से काम करते हैं, system-provided VoiceOver patterns का उपयोग करते हुए।
