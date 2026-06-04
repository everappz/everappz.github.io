---
title: "संपर्क"
date: 2020-01-01
description: "Evermusic का उपयोग करके क्लाउड सेवाएं, कंप्यूटर, NAS डिवाइस कनेक्ट करना और अपनी म्यूजिक फाइलें मैनेज करना सीखें। Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes File Sharing और अधिक के लिए step-by-step गाइड।"
keywords: [
  "Evermusic", "cloud music player", "NAS streaming", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes File Sharing",
  "connect cloud storage", "music transfer iPhone", "file manager iOS"
]
tags: ["evermusic", "guide", "connections"]
readingTime: 11
---


संपर्क स्क्रीन पर आप हर उस सोर्स को कनेक्ट कर सकते हैं जिसमें आपका संगीत है — लोकप्रिय क्लाउड सेवाएं, self-hosted media servers, आपका Mac या PC, एक personal NAS, Apple Time Capsule, WD My Cloud Home, यहां तक कि एक USB flash drive — और इन सभी को एक unified interface से उपयोग करें। संपर्क वह जगह भी है जहां आप deeply nested cloud folders तक Quick Access सेट करते हैं और जहां आप scrobbling के लिए Last.fm authenticate करते हैं।

स्क्रीन को स्पष्ट रूप से labeled sections में विभाजित किया गया है ताकि यह एकल iCloud Drive अकाउंट से लेकर कई clouds और NAS डिवाइस में फैली लाइब्रेरी तक scale कर सके: सबसे ऊपर Quick Access (आपके पसंदीदा क्लाउड फोल्डर), Cloud storage (आपके जोड़े गए अकाउंट), Local network (Bonjour-discovered devices), Computer (Wi-Fi Drive, iTunes File Sharing, SMB), External accessories (connected USB flash drives), और Other services (Last.fm और समान)।

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic संपर्क स्क्रीन" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## क्लाउड स्टोरेज से कनेक्ट करें

- संपर्क टैब खोलें।
- मेनू से क्लाउड स्टोरेज से कनेक्ट करें चुनें।
- लिस्ट से एक क्लाउड स्टोरेज सेवा चुनें।
- provider के official authorization page पर साइन इन करें (Evermusic आपका पासवर्ड कभी नहीं देखता)।
- Done टैप करें।

{{< cards cols="1">}}
  {{< card title="" subtitle="क्लाउड स्टोरेज प्रोवाइडर पिकर कनेक्ट करें" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

अगर कोई समस्या आए, तो अपना इंटरनेट कनेक्शन और login credentials दोबारा जांचें, और सुनिश्चित करें कि उस सेवा के लिए two-factor authentication सही तरीके से configure है।
Premium version में आप unlimited services जोड़ सकते हैं। मुफ्त users एक बार में एक ही क्लाउड अकाउंट कनेक्ट कर सकते हैं।

## समर्थित क्लाउड स्टोरेज सेवाएं

Evermusic लोकप्रिय क्लाउड और self-hosted सेवाओं की पूरी लाइनअप सपोर्ट करता है। मुफ्त users को एक ही provider catalog मिलता है लेकिन one-account limit के साथ; Premium unlimited accounts अनलॉक करता है और अधिकांश अन्य limits हटाता है।

- **व्यक्तिगत क्लाउड अकाउंट:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **सेल्फ-होस्टेड सर्वर और मीडिया लाइब्रेरी:** Plex · Jellyfin · Emby · Subsonic (और हर Subsonic-compatible सर्वर — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (और Owncloud, shared API के माध्यम से) · Synology Drive · QNAP.
- **NAS और फाइल-शेयर प्रोटोकॉल:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (password or public-key authentication), NFS, और DLNA (read-only — playback and download).
- **S3-compatible object storage:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage, या कोई भी S3-API endpoint.
- **लोकल-नेटवर्क डिस्कवरी:** उपलब्ध उपकरण सेक्शन आपके Wi-Fi पर हर उस डिवाइस को automatically list करता है जो Bonjour / mDNS के माध्यम से खुद को advertise करता है — Plex, Jellyfin, Emby सर्वर, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, attached drives वाले AirPort राउटर, इत्यादि।

## सुरक्षा और गोपनीयता

हम connected cloud services के साथ interact करने के लिए केवल official SDK और secure connection का उपयोग करते हैं। आपका login और password application के लिए उपलब्ध नहीं है। application से cloud service तक सभी requests encrypted हैं।

जब आप अपना login और password दर्ज करते हैं तो application आपको cloud service provider द्वारा प्रदान किया गया official authorization page दिखाता है और सभी authorization process application के बाहर होती है। Cloud service provider successful authorization के बाद application को एक auth token भेजता है और उस token का उपयोग API calls करने के लिए किया जाता है।

Auth-token एक digital key है जो third-party applications को cloud storage के साथ interact करने देती है। Auth-token आपके डिवाइस पर Keychain नामक एक secure system storage में stored है। आप connected cloud service से files डिवाइस पर डाउनलोड कर सकते हैं और वे files ऐप की "Documents" directory में placed होंगी। आप built-in file manager का उपयोग करके उन files को कभी भी हटा सकते हैं।

Application connected cloud account से कोई information share नहीं करता। आप अपने web browser पर account settings page खोलकर अपने cloud account तक access किसी भी समय revoke कर सकते हैं।

## auth-token reject करें

अपने web browser पर account में login करें और settings page पर navigate करें। वहां आप सभी third-party apps देख सकते हैं जो आपके cloud account से connected हैं और अगर आप उस application का उपयोग नहीं करना चाहते तो उनमें से किसी को भी हटा सकते हैं। विस्तृत निर्देश [यहां](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account) उपलब्ध हैं।

आप application में connected cloud accounts को भी disconnect कर सकते हैं और auth token आपके डिवाइस से भी हटा दिया जाएगा। अगर आप application को अपने डिवाइस से हटाते हैं तो सभी downloaded data और access tokens भी हटा दिए जाएंगे।

## क्लाउड स्टोरेज disconnect करें या configuration बदलें

- Cloud Storage Options Access करें: पहले, ऐप के interface में उस cloud storage को locate करें जिसे manage करना है।
- '...' Button टैप करें: service title के बगल में, आपको एक '...' button दिखेगा। अतिरिक्त options access करने के लिए उस पर टैप करें।
  - **Rename**: अगर आप cloud service का वह नाम बदलना चाहते हैं जैसा आपकी list में दिखता है, तो 'Rename' चुनें।
  - **सेटिंग्स**: cloud service के लिए configuration या authentication data modify करने के लिए, 'सेटिंग्स' चुनें। कभी-कभी, आपको connected cloud service को reauthorize करने की आवश्यकता हो सकती है अगर authorization token expire हो गया हो।
  - **Disconnect**: अगर आप app और cloud service के बीच connection पूरी तरह तोड़ना चाहते हैं, तो 'Disconnect' चुनें। ध्यान रखें कि यह option चुनने से इस cloud service से जुड़े सभी songs आपकी app की music library से हटा दिए जाएंगे, लेकिन वे server पर रहेंगे।

{{< cards cols="1">}}
  {{< card title="" subtitle="Connected Cloud Storage अधिक क्रियाएँ मेनू" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Computer या NAS से कनेक्ट करें

आप SMB, DLNA, या WebDAV protocol का उपयोग करके अपना computer, personal NAS, या अन्य network devices भी कनेक्ट कर सकते हैं।

## SMB का उपयोग करके computer से कनेक्ट करें

- "क्लाउड स्टोरेज से कनेक्ट करें" → SMB टैप करें।
- URL field में computer IP address और shared folder name इस format में दर्ज करें: smb://computer-ip-address/shared-folder-name
- protocol version चुनें: Auto, SMB1, SMB2
- login और password दर्ज करें (अगर आवश्यक हो)
- "Done" टैप करें।

अगर आपका connection successful है तो आप "Cloud storage" section में connected storage देखेंगे।
SMB का उपयोग करके अपना MAC या PC कनेक्ट करने के बारे में पूरा tutorial [यहां](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/) उपलब्ध है।

{{< cards cols="1">}}
  {{< card title="" subtitle="SMB Connection सेटिंग्स" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## WebDAV का उपयोग करके NAS से कनेक्ट करें

सभी steps same हैं सिवाय URL field के।
URL इस format में होना चाहिए: http://server-name, या https://server-name अगर server SSL सपोर्ट करता है।
WebDAV protocol का उपयोग करके NAS connect करने के बारे में पूरा tutorial [यहां](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac) उपलब्ध है।

{{< cards cols="1">}}
  {{< card title="" subtitle="WebDAV Connection सेटिंग्स" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## DLNA का उपयोग करके Computer या NAS से कनेक्ट करें

आप अपने Windows PC या personal NAS पर DLNA protocol का उपयोग करके एक music library share भी कर सकते हैं और उस library को app में [यहां](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone) वर्णित अनुसार access कर सकते हैं। DLNA एक popular और widely used protocol है, लेकिन यह केवल आपको music play या download करने देता है। आप server पर files upload नहीं कर सकते या नए folders नहीं बना सकते।

{{< cards cols="1">}}
  {{< card title="" subtitle="DLNA Connection सेटिंग्स" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## उपलब्ध उपकरण

यह section आपके local network के उन सभी devices को display करता है जिनसे आप application के माध्यम से connect कर सकते हैं।
किसी device के साथ connection establish करने के लिए, इन steps का पालन करें:

- App खोलें और "उपलब्ध उपकरण" section पर जाएं।
- list से उस device पर टैप करें जिससे आप connect करना चाहते हैं।
- अगर आवश्यक हो, connection complete करने के लिए अपना login details दर्ज करें।

{{< cards cols="1">}}
  {{< card title="" subtitle="लोकल नेटवर्क पर उपलब्ध उपकरण" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive एक convenient technology है जो desktop browser के माध्यम से आपके computer से आपके iOS device पर wireless file transfers enable करती है।
इस feature का प्रभावी ढंग से उपयोग करने के लिए, सुनिश्चित करें कि आपका device और computer एक ही Wi-Fi network से connected हैं।
Wi-Fi Drive का उपयोग करने के बारे में step-by-step गाइड यहां है।

## Wi-Fi Drive Enable करें

- Application खोलें और "संपर्क" टैब पर जाएं।
- Wi-Fi Drive main screen access करने के लिए "Wi-Fi के माध्यम से कनेक्ट करें" चुनें।
- Wi-Fi Drive enable करने के लिए "Start Wi-Fi Drive" टैप करें।

## अपने Computer पर Wi-Fi Drive Access करें

- अपने computer (desktop या laptop) पर, एक web browser (जैसे Chrome, Firefox, या Safari) खोलें।
- browser के address bar में, application द्वारा प्रदान किया गया URL दर्ज करें।

## Files Wirelessly Transfer करें

एक बार जब browser में आपके iOS device से corresponding web page खुल जाए, तो आप अपने computer से web page पर files आसानी से drag और drop कर सकते हैं।
जो files आप drag और drop करते हैं वे आपके iOS device पर transfer होना शुरू हो जाएंगी और application के भीतर accessible होंगी।

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive Server सेटिंग्स" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

WiFi-Drive का उपयोग करके files wirelessly transfer करने के बारे में विस्तृत निर्देश [यहां](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) उपलब्ध हैं।

## iTunes File Sharing

iTunes File Sharing एक अन्य technology है जो आपको Finder app और lightning cable का उपयोग करके computer से device पर files transfer करने देती है।
- बस एक cable का उपयोग करके device को computer से connect करें और अपने Mac पर Finder app run करें।
- "Locations" → "Your Connected Device" → "Files" → खोलें और Evermusic app ढूंढें।
- सभी shared folders देखने के लिए app icon पर टैप करें।
- drag-and-drop का उपयोग करके computer से device पर shared folder में files copy करें।

iTunes file sharing का उपयोग करने के बारे में विस्तृत निर्देश [यहां](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/) उपलब्ध हैं।

{{< cards cols="1">}}
  {{< card title="" subtitle="Mac पर iTunes / Finder File Sharing" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## USB flashcard कनेक्ट करें

अगर आपके पास SD card है, तो आप इसे lightning card reader का उपयोग करके connect कर सकते हैं। App currently Apple Certified card readers और iXpand Flash Drives सपोर्ट करता है। अगर आपके पास iXpand Flash Drive है - इसे lightning port में insert करें और application खोलें। आपको एक 'External device connected' message और device information दिखेगी। music folder access करने के लिए बस flash drive icon पर टैप करें और playback शुरू करने के लिए किसी भी audio file पर टैप करें। iPhone पर USB flashcard कनेक्ट करने और उस पर located music सुनने या files manage करने के बारे में विस्तृत निर्देश [यहां](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it) उपलब्ध हैं।

## File Manager

एक बार जब आप क्लाउड स्टोरेज service connect कर लें, तो सभी available files और folders देखने के लिए उसके icon पर टैप करें। आप इन files के साथ काम करने के लिए built-in file manager का उपयोग कर सकते हैं — download, rename, move, और अधिक। जब आप download शुरू करते हैं, तो file transfer queue में दिखाई देगी। transfer queue देखने के लिए, "Local Files" टैब पर जाएं और top left corner में spinning arrows पर टैप करें। सभी downloaded files और folders "Local Files" section में उपलब्ध हैं।

## Top Toolbar

Top toolbar, navigation bar के नीचे conveniently located, आसान access के लिए कई useful actions प्रदान करता है। आप इस toolbar को एक simple swipe-down gesture का उपयोग करके दिखा या छिपा सकते हैं। यहां available actions हैं:

- **खोजें**: यह option आपको current directory के भीतर quick search perform करने देता है, जिससे specific files या folders locate करना effortless हो जाता है।
- **Continue Playback**: अगर application settings में enabled है, तो यह feature current folder के लिए audio player queue और last media position restore करता है। यह आपकी music library में जहां छोड़ा था वहां से pick up करने का एक handy तरीका है।
- **सभी चलाएं**: यह action select करके, app current folder और उसके subfolders को scan करेगा, सभी मिले audio files को एक new player queue में जोड़ेगा। यह तब useful है जब आप किसी particular directory के भीतर सभी music play करना चाहते हैं।
- **सभी फेरबदल करें**: "सभी चलाएं" के समान, यह action current folder और उसके subfolders को scan करता है लेकिन audio player queue में जोड़ने से पहले files को shuffle करता है। यह थोड़ी variety के लिए random order में अपना music enjoy करने का एक बढ़िया तरीका है।

{{< cards cols="1">}}
  {{< card title="" subtitle="क्लाउड फोल्डर के अंदर Top Toolbar" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Folder Options

जब आप app के भीतर कोई folder खोलते हैं, तो आपको screen के top right corner में "..." button टैप करके एक handy set of actions मिलती हैं।
यहां इन actions का breakdown है:

- **चुनें**: file selection mode activate करें। यह mode आपको folder के भीतर एक या अधिक files choose करने enable करता है, जिससे selected items पर actions perform करना आसान हो जाता है।
- **New Folder**: current folder के भीतर एक new folder create करें। यह feature आपको अपनी files organize करने और library well-structured रखने देता है।
- **Offline Mode Enable करें**: current folder के लिए offline mode toggle करें। Offline mode simple downloading से परे जाता है; यह changes के लिए folder को actively monitor करता है। अगर आप online folder में new files add करते हैं, तो app automatically इन files को आपके device पर download कर देगा। यह सुनिश्चित करता है कि आपकी local library server पर changes के साथ up-to-date रहे।
- **Files Upload करें**: अपने device से online folder में files upload करें। यह action आपको cloud या server पर files transfer करने देता है, जिससे वे कहीं से भी accessible हो जाती हैं।
- **खोजें**: current folder के भीतर specific files खोजें। यह large collection में specific items quickly locate करने के लिए especially useful है।
- **Sort**: name, size, या date edited जैसे criteria के अनुसार folder के भीतर files sort करें। Default sort mode typically server पर sorting order mirror करता है, लेकिन आप इसे अपनी preferences के अनुसार बदल सकते हैं।
- **Grid/List View**: दो viewing modes के बीच switch करें: table view और thumbnail view। Table view files को list में present करता है, जबकि thumbnail view files के visual representations display करता है, जिससे content glance में identify करना आसान हो जाता है।

{{< cards cols="1">}}
  {{< card title="" subtitle="Current Folder अधिक क्रियाएँ मेनू" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Online Files Edit करें

जब आपको Evermusic पर अपने cloud storage के भीतर multiple files manage करने की आवश्यकता हो, तो आप अपने actions streamline करने के लिए select mode का उपयोग कर सकते हैं। प्रभावी file management के लिए इन steps का पालन करें:

- **Selection Mode Activate करें**: अपने device पर app खोलें और अपने cloud storage वाले section पर navigate करें। Top right corner में "..." (ellipsis) button ढूंढें। उस पर टैप करें और selection mode activate करने के लिए "चुनें" menu item choose करें।
- **Files Choose करें**: आपको हर file या folder के बगल में checkboxes दिखेंगे। उनके बगल में checkboxes पर simply टैप करके एक या multiple files या folders choose करें।
- **विभिन्न Actions Perform करें**: एक बार जब आप वे files या folders select कर लें जिन्हें manage करना है, तो आपकी needs के अनुसार customized कई actions accessible होंगी:

{{< cards cols="1">}}
  {{< card title="" subtitle="Online Files के लिए Selection Mode" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## File actions

File के title के पास, आपको एक ellipsis symbol "..." (three dots) दिखेगा – यह actions menu का काम करता है।
उपलब्ध actions की list देखने के लिए उस पर टैप करें:

- **Play Next**: chosen file को आपके player queue के top पर insert करने के लिए यह action opt करें, यह सुनिश्चित करते हुए कि यह currently playing item के immediately बाद चले।
- **Play Later**: यह option select करने से file आपके player queue के bottom में add होती है, यह सुनिश्चित करते हुए कि यह existing queue के बाद चले।
- **Music Library में जोड़ें**: यह action आपको file को अपनी music library में incorporate करने देता है, जिससे यह artist, album, genre, या composer के अनुसार easily accessible और neatly organized हो जाती है।
- **Playlist में जोड़ें**: file को existing playlist में add करने या नई बनाने के लिए इस action का उपयोग करें।
- **ऑडियो टैग संपादित करें**: यह option select करके, आप Evermusic के built-in tags editor access कर सकते हैं, जो आपको chosen file के audio tags modify करने देता है। File temporarily एक temporary directory में download की जाएगी और फिर आपके changes confirm करने के बाद storage पर upload की जाएगी।
- **पसंदीदा में जोड़ें**: यह action quick और convenient access के लिए file को आपकी favorite files की list में add करता है।
- **डाउनलोड करें**: file या folder को offline use के लिए accessible बनाने के लिए इसे अपने device पर download करने के लिए यह action choose करें।
- **Rename**: यह option remote storage पर directly file rename करने की अनुमति देता है, customized file naming के लिए।
- **Move**: file को आपके cloud storage के भीतर किसी different folder में relocate करने के लिए यह action opt करें, organized file structure maintain करने में मदद करते हुए।
- **Open In**: file को किसी अन्य compatible app में export करने के लिए इस action का उपयोग करें। File आपके device पर download की जाएगी, और फिर further sharing या interaction के लिए Share dialog appear होगा।
- **हटाना**: इस action के साथ सावधानी बरतें, क्योंकि यह file को आपके cloud storage से permanently remove करता है। यह deletion undone नहीं की जा सकती।

{{< cards cols="1">}}
  {{< card title="" subtitle="Single File के लिए अधिक क्रियाएँ मेनू" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

अगर actions की list available screen space से अधिक हो, तो additional options access करने के लिए actions menu के भीतर simply scroll down करें।

## Folder actions

आपके cloud storage के प्रत्येक folder के लिए, विभिन्न actions available हैं। इन options access करने के लिए, folder title के बगल में ellipsis icon "..." पर simply टैप करें। अगर आपको सभी actions नहीं दिखते, तो more choices reveal करने के लिए scroll down करें। यहां available actions हैं:

- **सभी चलाएं**: current player queue को selected folder के सभी items से replace करें।
- **Play Next**: entire folder को player queue के top पर, currently playing item के right बाद add करें।
- **Play Later**: folder contents को player queue के bottom पर append करें।
- **Music Library में जोड़ें**: यह action folder के content को आपकी music library में seamlessly incorporate करता है, artist, album, genre, या composer के अनुसार easily accessible और neatly organized बनाता है।
- **Playlist में जोड़ें**: आप entire folder को playlist में include कर सकते हैं। आपके पास new playlist create करने का भी option है, और folder का नाम automatically assigned किया जाएगा।
- **पसंदीदा में जोड़ें**: quick और convenient access के लिए folder को आपकी favorite files की list में add करने के लिए इस action का उपयोग करें।
- **Offline Mode Enable करें**: selected folder के लिए offline mode enable करके, application simple downloading से परे जाता है। यह continuously changes के लिए scan करता है, और अगर online folder में new files add होती हैं, तो वे automatically app में download की जाएंगी।
- **डाउनलोड करें**: offline access के लिए folder की सभी contents को अपने device पर download करें।
- **Rename**: remote storage पर directly folder rename करें।
- **Move**: folder को आपके cloud storage के भीतर किसी different location पर relocate करें।
- **हटाना**: इस action के साथ सावधान रहें क्योंकि यह folder और उसकी contents को आपके cloud storage से permanently remove करता है। यह action undone नहीं की जा सकती।


## Quick Access

Quick Access section screen के top पर located है। यह connected cloud services से आपकी favorite और recently opened files तक fast access देता है।
जब भी आप cloud से कोई file या folder खोलते हैं, यह "Recently Opened" list में add हो जाता है। इस list को clear करने के लिए, "हाल के" खोलें, "अधिक क्रियाएँ" button टैप करें, और "Delete List" choose करें। आप deeply nested folders को Favorites के रूप में भी mark कर सकते हैं ताकि directory structure में खोजे बिना उन्हें quickly access कर सकें।

## अन्य सेवाएं

यह section extra features display करता है जो आपके experience को enhance करती हैं। Currently, app Last.fm scrobbling support करता है। Connected होने पर, आपके playback stats automatically आपके Last.fm account पर send होते हैं। आप बाद में listening analytics देखने और personalized music recommendations पाने के लिए अपना Last.fm profile visit कर सकते हैं। विस्तृत setup instructions [यहां](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm) उपलब्ध हैं।
