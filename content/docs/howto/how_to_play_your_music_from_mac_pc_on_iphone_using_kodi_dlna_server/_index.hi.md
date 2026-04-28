---
title: "Kodi DLNA सर्वर का उपयोग करके Mac / PC / Linux / NAS से iPhone पर अपना संगीत कैसे चलाएं"
date: 2025-07-25
description: "Kodi DLNA और Evermusic ऐप का उपयोग करके Wi-Fi के माध्यम से अपने कंप्यूटर या NAS से iPhone पर संगीत स्ट्रीम करें।"
keywords: ["kodi dlna सर्वर", "iphone पर संगीत स्ट्रीम करें", "nas से संगीत चलाएं", "evermusic dlna", "mac से iphone संगीत", "windows से iphone संगीत", "kodi dlna iphone", "dlna ऑडियो स्ट्रीमिंग"]
tags: ["dlna", "kodi", "evermusic", "iphone", "संगीत स्ट्रीमिंग", "mac", "nas", "linux", "लोकल नेटवर्क"]
readingTime: 5
---

{{< author-byline >}}


**सारांश:** अपने Mac, PC, Linux या NAS पर Kodi इंस्टॉल करें, इसका DLNA/UPnP सर्वर सक्षम करें, और मुफ्त Evermusic या Flacbox ऐप का उपयोग करके Wi-Fi के माध्यम से अपनी पूरी संगीत लाइब्रेरी को iPhone या iPad पर स्ट्रीम करें। कोई सब्सक्रिप्शन की आवश्यकता नहीं।

## परिचय

यदि आपके पास **Mac, Windows PC, Linux मशीन या NAS डिवाइस** है, तो आप [Kodi](https://kodi.tv/) का उपयोग करके इसे आसानी से घर पर **व्यक्तिगत संगीत सर्वर** में बदल सकते हैं, जो एक मुफ्त और ओपन-सोर्स मीडिया प्लेटफॉर्म है। Kodi के बिल्ट-इन **DLNA/UPnP सर्वर** के साथ, आप अपनी पूरी संगीत लाइब्रेरी को किसी भी DLNA-संगत क्लाइंट पर स्ट्रीम कर सकते हैं — जिसमें आपका iPhone या iPad भी शामिल है।

इस गाइड में, हम आपको चरण-दर-चरण दिखाएंगे कि कैसे:

- अपने Mac या PC पर Kodi इंस्टॉल करें  
- शेयरिंग के लिए अपने म्यूजिक फोल्डर सेट करें  
- DLNA म्यूजिक सर्वर सक्षम करें  
- **Evermusic** या **Flacbox** iOS ऐप का उपयोग करके उस संगीत तक पहुंचें

यह सेटअप 100% मुफ्त है — कोई सब्सक्रिप्शन नहीं, बस आपका अपना संगीत आपके Wi-Fi नेटवर्क पर स्ट्रीम किया जाता है। चाहे आप अपने बड़े MP3 कलेक्शन को व्यवस्थित करने की कोशिश कर रहे हों, Wi-Fi पर FLAC सुनना चाहते हों, या बस iTunes के माध्यम से सिंक किए बिना अपने लोकल म्यूजिक का आनंद लेना चाहते हों, यह सेटअप आपके लिए एकदम सही है।

## अपने Mac / PC / Linux / NAS पर Kodi डाउनलोड और इंस्टॉल करें

सबसे पहले, Kodi की आधिकारिक वेबसाइट पर जाएं:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Kodi का मुख्य पेज" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

**डाउनलोड** पर क्लिक करें और अपने कंप्यूटर के लिए वर्जन खोजने के लिए स्क्रॉल करें।
अपना ऑपरेटिंग सिस्टम चुनें। इस उदाहरण में, हम **macOS** का उपयोग करेंगे।

{{< cards cols="1">}}
{{< card subtitle="Kodi डाउनलोड पेज" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

यदि आपके पास Intel Mac है तो **Intel (x86/64)** पर क्लिक करें या M1, M2, M3 Mac के लिए **Apple Silicon** पर क्लिक करके डाउनलोड शुरू करें।

{{< cards cols="1">}}
{{< card subtitle="macOS इंस्टॉलर चुनें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

कृपया इंस्टॉलर डाउनलोड होने तक प्रतीक्षा करें।

{{< cards cols="1">}}
{{< card subtitle="Kodi डाउनलोड हो गया" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

डाउनलोड होने के बाद, अपने **डाउनलोड** फोल्डर में `.dmg` फाइल खोजें।

{{< cards cols="1">}}
{{< card subtitle="Kodi इंस्टॉल करें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

इंस्टॉलर लॉन्च करने के लिए डाउनलोड की गई फाइल पर डबल-क्लिक करें।
इंस्टॉल करने के लिए Kodi को अपने **एप्लिकेशन** फोल्डर में ड्रैग करें।

{{< cards cols="1">}}
{{< card title="" subtitle="Kodi को एप्लिकेशन में ड्रैग करके इंस्टॉल करें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Kodi लॉन्च करें। आपको **सिस्टम प्रेफरेंसेज ← सुरक्षा और गोपनीयता ← फिर भी खोलें** में इसे अनुमति देनी पड़ सकती है।

{{< cards cols="1">}}
{{< card subtitle="Kodi मुख्य स्क्रीन" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Kodi लाइब्रेरी में संगीत जोड़ें

होम स्क्रीन से **गियर आइकन** (सेटिंग्स) पर क्लिक करें।

{{< cards cols="1">}}
{{< card subtitle="Kodi सेटिंग्स" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

**मीडिया सेटिंग्स ← लाइब्रेरी** पर नेविगेट करें। स्वचालित इंडेक्सिंग के लिए वीडियो लाइब्रेरी और म्यूजिक लाइब्रेरी के लिए **स्टार्टअप पर लाइब्रेरी अपडेट करें** सक्षम करें।

{{< cards cols="1">}}
{{< card subtitle="लाइब्रेरी सेटिंग्स" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

फिर **म्यूजिक** सेक्शन पर जाएं और **म्यूजिक जोड़ें** पर क्लिक करें।

{{< cards cols="1">}}
{{< card subtitle="म्यूजिक फोल्डर जोड़ें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

ब्राउज़ करें और वह फोल्डर चुनें जहां आपका संगीत स्टोर है।

{{< cards cols="1">}}
{{< card subtitle="संगीत स्रोत चुनें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Kodi में संगीत स्रोत जोड़ें।

{{< cards cols="1">}}
{{< card subtitle="संगीत स्रोत जोड़ें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

पुष्टि करें और Kodi को आपकी संगीत लाइब्रेरी स्कैन करने दें।

{{< cards cols="1">}}
{{< card subtitle="संगीत स्रोतों की पुष्टि करें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

आपकी लाइब्रेरी स्कैन होने और पूरी तरह बनने तक प्रतीक्षा करें।

{{< cards cols="1">}}
{{< card subtitle="संगीत लाइब्रेरी स्कैन हो रही है" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Kodi का DLNA सर्वर सक्षम करें

**सेटिंग्स ← सर्विसेज ← UPnP/DLNA** पर जाएं।

विकल्प सक्षम करें: **मेरी लाइब्रेरी शेयर करें**।

Kodi अब आपके लोकल Wi-Fi नेटवर्क पर DLNA सर्वर के रूप में कार्य करता है।

{{< cards cols="1">}}
{{< card subtitle="Kodi में DLNA सक्षम करें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Kodi लाइब्रेरी खोलें

सेटिंग्स विंडो बंद करने और Kodi मुख्य लाइब्रेरी खोलने के लिए राइट-क्लिक करें।

{{< cards cols="1">}}
{{< card title="" subtitle="Kodi लाइब्रेरी तक पहुंचने के लिए राइट-क्लिक करें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## iOS के लिए म्यूजिक स्ट्रीमिंग ऐप डाउनलोड करें

एक मुफ्त iOS DLNA क्लाइंट ऐप प्राप्त करें जो आपको क्लाउड स्टोरेज सेवाओं और DLNA सर्वरों से संगीत स्ट्रीम करने देता है।

- यदि आपका कलेक्शन मुख्य रूप से MP3 और अन्य मानक ऑडियो फॉर्मेट में है तो **Evermusic** का उपयोग करें।
- यदि आपकी हाई-रेज म्यूजिक लाइब्रेरी FLAC, ALAC या DSD जैसे फॉर्मेट में है तो **Flacbox** चुनें।

दोनों ऐप **iOS** और **macOS** के लिए उपलब्ध हैं, और मुफ्त हैं।

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Evermusic डाउनलोड करें" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Flacbox डाउनलोड करें" icon="download" tag="Free" >}}
{{< /cards >}}

## DLNA स्रोत जोड़ें

iOS ऐप डाउनलोड करने के बाद, **सभी संपर्क** सेक्शन खोलें।

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic ऐप का मुख्य साइडबार" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

नीचे स्क्रॉल करें और DLNA सर्वर खोजने के लिए **लोकल नेटवर्क - उपलब्ध उपकरण** पर टैप करें।
इस सेक्शन में, आप अपने लोकल नेटवर्क पर सभी उपलब्ध डिवाइस देखेंगे। आपका **Kodi DLNA सर्वर** यहां दिखाई देना चाहिए। कनेक्ट करने के लिए Kodi सर्वर पर टैप करें।

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic में उपलब्ध DLNA डिवाइस" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic Kodi के माध्यम से शेयर किए गए लाइब्रेरी फोल्डर दिखाएगा।

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic में Kodi म्यूजिक लाइब्रेरी" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

अपने DLNA सर्वर पर सभी उपलब्ध ऑडियो फाइलें देखने के लिए **गाने** फोल्डर में नेविगेट करें।

{{< cards cols="1">}}
{{< card title="" subtitle="रिमोट फोल्डर से गाने सूचीबद्ध" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

तुरंत स्ट्रीमिंग शुरू करने के लिए किसी भी ऑडियो फाइल पर टैप करें।

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic में MP3 फाइल चल रही है" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

**संपर्क** सेक्शन पर वापस जाएं। जोड़ा गया DLNA सर्वर अब यहां दिखाई देगा। किसी भी समय फिर से कनेक्ट करने के लिए इसके आइकन पर टैप करें। आप इसी स्क्रीन से उन्हीं चरणों का उपयोग करके अन्य क्लाउड सेवाओं को भी कनेक्ट कर सकते हैं।

आप यहां **Last.fm स्क्रॉबलिंग** भी सक्षम कर सकते हैं। प्लेबैक सांख्यिकी आपके Last.fm खाते में सहेजी जाएंगी, जो बाद में व्यक्तिगत संगीत अनुशंसाएं प्रदान करेंगी।

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic में संपर्क" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## म्यूजिक लाइब्रेरी बनाएं

**Evermusic** और **Flacbox** दोनों आपको अपनी लाइब्रेरी में संगीत जोड़ने और इसे कलाकारों, एल्बम, शैलियों और संगीतकारों जैसे **मेटाडेटा टैग** द्वारा व्यवस्थित करने देते हैं।

शुरू करने के लिए, **म्यूजिक लाइब्रेरी** सेक्शन खोलें। **टूल्स और प्राथमिकताएं** तक नीचे स्क्रॉल करें और **म्यूजिक जोड़ें** पर टैप करें।

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic म्यूजिक लाइब्रेरी" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

संगीत स्रोत चुनें — इस मामले में, **संपर्क** चुनें।

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic में नया संगीत जोड़ें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

संपर्क में **Kodi DLNA सर्वर** खोजें और फोल्डर और फाइलें देखने के लिए टैप करें।

{{< cards cols="1">}}
{{< card title="" subtitle="संगीत आयात के लिए DLNA सर्वर चुनें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

जोड़ने के लिए फोल्डर या फाइलें चुनें और **पूर्ण करना** पर टैप करें।

{{< cards cols="1">}}
{{< card title="" subtitle="जोड़ने के लिए म्यूजिक फोल्डर चुनें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

ऐप आपकी चयनित फाइलों को स्कैन करेगा और मेटाडेटा का उपयोग करके उन्हें कलाकार, एल्बम, शैली और संगीतकार जैसे सेक्शन में व्यवस्थित करेगा।

{{< cards cols="1">}}
{{< card title="" subtitle="श्रेणियों के साथ म्यूजिक लाइब्रेरी" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## प्लेलिस्ट बनाएं

आप अपनी खुद की प्लेलिस्ट भी बना सकते हैं।

सबसे पहले, **प्लेलिस्ट्स** टैब खोलें।

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic में प्लेलिस्ट टैब" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

**प्लस (+)** बटन पर टैप करें और **नई प्लेलिस्ट** चुनें।

{{< cards cols="1">}}
{{< card title="" subtitle="नई प्लेलिस्ट बनाएं" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

अपनी प्लेलिस्ट का नाम दर्ज करें और **सहेजें** पर टैप करें।

{{< cards cols="1">}}
{{< card title="" subtitle="प्लेलिस्ट का नाम दर्ज करें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

अगला, गाने जोड़ने के लिए एक स्रोत चुनें — यहां, हम **लाइब्रेरी** चुनते हैं।

{{< cards cols="1">}}
{{< card title="" subtitle="नई प्लेलिस्ट में गाने जोड़ें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

अपने इच्छित गाने चुनें और उन्हें जोड़ने के लिए **पूर्ण करना** पर टैप करें।

{{< cards cols="1">}}
{{< card title="" subtitle="लाइब्रेरी से प्लेलिस्ट में संगीत जोड़ें" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

आपके चयनित ट्रैक अब बनाई गई प्लेलिस्ट में दिखाई देंगे।

{{< cards cols="1">}}
{{< card title="" subtitle="बनाई गई प्लेलिस्ट सूची में दिखाई गई" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

डिफ़ॉल्ट रूप से, गाने स्ट्रीमिंग के लिए उपलब्ध हैं। ऑफलाइन सुनने के लिए, **ऑफलाइन मोड** सक्षम करें — ऐप सभी प्लेलिस्ट ट्रैक डाउनलोड करेगा।

{{< cards cols="1">}}
{{< card title="" subtitle="प्लेलिस्ट के लिए ऑफलाइन मोड सक्षम" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

अतिरिक्त विकल्पों का पता लगाने के लिए **अधिक क्रियाएँ** बटन पर टैप करें। आप:

- प्लेलिस्ट को आर्काइव करें  
- एल्बम कवर बदलें  
- ट्रैक को पुनर्व्यवस्थित करें  
- और अधिक उपयोगी सुविधाएं

{{< cards cols="1">}}
{{< card title="" subtitle="प्लेलिस्ट के लिए और अधिक क्रियाएँ उपलब्ध" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## निष्कर्ष

**Evermusic** और **Flacbox** के साथ, अपने iPhone, iPad या Mac को एक शक्तिशाली DLNA म्यूजिक प्लेयर में बदलना आसान है। चाहे आप अपना संगीत क्लाउड में, NAS पर, या **Kodi** जैसे होम मीडिया सर्वर पर स्टोर करें, ये ऐप्स आपको बिना किसी सीमा के अपने कलेक्शन को स्ट्रीम, व्यवस्थित और आनंद लेने देते हैं।

- अपने **Kodi DLNA सर्वर** से सीधे MP3 या हाई-रेज FLAC स्ट्रीम करें  
- मेटाडेटा (एल्बम, शैलियां, संगीतकार) द्वारा समूहीकृत व्यक्तिगत म्यूजिक लाइब्रेरी बनाएं  
- **कस्टम प्लेलिस्ट** बनाएं और प्रबंधित करें  
- चलते-फिरते सुनने के लिए **ऑफलाइन मोड** सक्षम करें  
- **कई क्लाउड सेवाओं** और **लोकल नेटवर्क डिवाइसों** से कनेक्ट करें  
- **Last.fm इंटीग्रेशन** के साथ अपनी सुनने की आदतों को ट्रैक करें

चाहे आप ऑडियोफाइल हों या कैजुअल श्रोता, Evermusic और Flacbox निर्बाध संगीत स्ट्रीमिंग और संगठन के लिए आपको जो कुछ भी चाहिए वह प्रदान करते हैं।

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Evermusic डाउनलोड करें" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Flacbox डाउनलोड करें" icon="download" tag="Free" >}}
{{< /cards >}}

आज ही अपना व्यक्तिगत संगीत अनुभव बनाना शुरू करें।

## अक्सर पूछे जाने वाले प्रश्न

{{% details title="क्या Kodi DLNA सर्वर के रूप में मुफ्त है?" closed="true" %}}
हां। Kodi पूरी तरह से मुफ्त और ओपन-सोर्स है। यह macOS, Windows, Linux और कई NAS डिवाइसों पर चलता है।
{{% /details %}}

{{% details title="क्या Evermusic और Flacbox DLNA पर FLAC स्ट्रीमिंग का समर्थन करते हैं?" closed="true" %}}
हां। Flacbox FLAC, ALAC और DSD जैसे हाई-रेज फॉर्मेट के लिए अनुकूलित है। Evermusic भी MP3 और अन्य मानक फॉर्मेट के साथ FLAC प्लेबैक का समर्थन करता है।
{{% /details %}}

{{% details title="क्या मैं Kodi से स्ट्रीमिंग के बाद ऑफलाइन सुन सकता हूं?" closed="true" %}}
हां। किसी भी प्लेलिस्ट पर ऑफलाइन मोड सक्षम करें, और ऐप नेटवर्क कनेक्शन के बिना सुनने के लिए सभी ट्रैक आपके डिवाइस पर डाउनलोड कर देगा।
{{% /details %}}

{{% details title="क्या मुझे DLNA का उपयोग करने के लिए प्रीमियम सब्सक्रिप्शन की आवश्यकता है?" closed="true" %}}
मुफ्त संस्करण 3 क्लाउड या नेटवर्क कनेक्शन तक का समर्थन करता है। प्रीमियम इस सीमा को हटा देता है और आपको असीमित सेवाओं और DLNA सर्वरों से कनेक्ट करने देता है।
{{% /details %}}

{{% details title="क्या मेरे iPhone को Kodi के समान Wi-Fi नेटवर्क पर होना चाहिए?" closed="true" %}}
हां। DLNA स्ट्रीमिंग आपके लोकल नेटवर्क पर काम करती है। Kodi सर्वर और आपके iOS डिवाइस दोनों को एक ही Wi-Fi नेटवर्क से कनेक्ट होना चाहिए।
{{% /details %}}

{{% details title="क्या मैं Mac या PC के बजाय NAS के साथ इस सेटअप का उपयोग कर सकता हूं?" closed="true" %}}
हां। कई NAS डिवाइस (Synology, QNAP आदि) Kodi का समर्थन करते हैं या उनका अपना बिल्ट-इन DLNA सर्वर है। Evermusic और Flacbox किसी भी मानक DLNA/UPnP सर्वर से कनेक्ट हो सकते हैं।
{{% /details %}}
