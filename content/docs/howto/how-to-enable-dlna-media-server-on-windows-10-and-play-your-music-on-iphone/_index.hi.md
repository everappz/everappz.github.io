---
title: "Windows 10 पर DLNA मीडिया सर्वर कैसे सक्षम करें और iPhone पर अपना संगीत कैसे चलाएं"
date: 2019-11-26
description: "Windows 10 पर DLNA सर्वर सक्षम करें और Evermusic ऐप के साथ अपना संगीत iPhone पर स्ट्रीम करें। चरण-दर-चरण सेटअप गाइड शामिल।"
keywords: ["evermusic", "dlna", "windows 10", "iphone संगीत स्ट्रीमिंग", "मीडिया सर्वर", "स्थानीय नेटवर्क", "upnp"]
tags: ["evermusic", "संगीत", "क्लाउड", "iphone", "भंडारण", "स्थानीय", "nas", "windows", "wifi", "सुनना", "नेटवर्क", "रिमोट", "घर", "ऑनलाइन", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**संक्षेप में:** Windows 10 में एक अंतर्निहित DLNA सर्वर है। इसे नेटवर्क और शेयरिंग सेटिंग्स में सक्षम करें, फिर अपने iPhone पर मुफ्त **Evermusic** ऐप का उपयोग करके Wi-Fi पर अपनी पूरी संगीत लाइब्रेरी स्ट्रीम करें। किसी तृतीय-पक्ष सर्वर सॉफ्टवेयर की आवश्यकता नहीं।

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: फ्रंट कवर" caption="Windows 10 और Evermusic का उपयोग करके iPhone पर DLNA संगीत स्ट्रीमिंग" width="800" >}}

DLNA (Digital Living Network Alliance) एक शक्तिशाली उपकरण है जो आपको अपने नेटवर्क पर DLNA-समर्थित उपकरणों के बीच संगीत सहित विभिन्न मीडिया सामग्री को आसानी से स्ट्रीम करने में सक्षम बनाता है। अच्छी खबर यह है कि Windows 10, और पिछले संस्करणों में, एक अंतर्निहित DLNA सुविधा है, जो तृतीय-पक्ष मीडिया सर्वर की आवश्यकता को समाप्त करती है। यहां बताया गया है कि Windows 10 पर DLNA मीडिया सर्वर कैसे सक्षम करें और अपने iPhone पर संगीत स्ट्रीमिंग का आनंद कैसे लें।

## Windows 10 पर DLNA मीडिया सर्वर कैसे सक्षम करें

1. 'स्टार्ट' बटन पर क्लिक करें।  
2. 'सेटिंग्स' आइकन चुनें।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="सर्वर सेटअप" caption="Windows सेटिंग्स खोलें" width="500" >}}

3. 'Windows सेटिंग्स' स्क्रीन पर, 'नेटवर्क और इंटरनेट' चुनें।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Windows सेटिंग्स" caption="नेटवर्क और इंटरनेट चुनें" width="500" >}}

4. 'नेटवर्क' के अंतर्गत, 'नेटवर्क और शेयरिंग सेंटर' चुनें।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="शेयरिंग सेंटर" caption="नेटवर्क और शेयरिंग सेंटर खोलें" width="500" >}}

5. 'नेटवर्क और शेयरिंग सेंटर' स्क्रीन पर, बाएं मेनू में 'उन्नत शेयरिंग सेटिंग्स बदलें' पर क्लिक करें।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="उन्नत शेयरिंग सेटिंग्स" caption="उन्नत शेयरिंग सेटिंग्स बदलें" width="500" >}}

6. 'उन्नत शेयरिंग सेटिंग्स' स्क्रीन पर, 'सभी नेटवर्क' अनुभाग तक नीचे स्क्रॉल करें और तीर पर क्लिक करके इसे विस्तारित करें।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="खोज चालू करें" caption="सभी नेटवर्क सेटिंग्स विस्तारित करें" width="500" >}}

7. DLNA सर्वर सक्रिय करने के लिए 'मीडिया स्ट्रीमिंग चालू करें' पर क्लिक करें।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="सर्वर चालू करें" caption="मीडिया स्ट्रीमिंग सर्वर सक्षम करें" width="500" >}}

8. अपनी मीडिया लाइब्रेरी को एक नाम दें और उन उपकरणों का चयन करें जिन्हें इसे एक्सेस करने की अनुमति है।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="मीडिया लाइब्रेरी नाम" caption="अपनी DLNA मीडिया लाइब्रेरी का नाम रखें" width="500" >}}

9. ऑपरेशन की पुष्टि करने के लिए 'OK' पर क्लिक करें। अब, आपके व्यक्तिगत फोल्डर जैसे संगीत, चित्र और वीडियो UPnP समर्थन वाले किसी भी स्ट्रीमिंग डिवाइस को दिखाई देंगे।

## Windows 10 पर DLNA मीडिया सर्वर कैसे अक्षम करें

1. 'स्टार्ट' पर क्लिक करें और खोज फ़ील्ड में 'services' टाइप करें।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Windows सेवाएं" caption="Windows सेवाएं खोलें" width="500" >}}

2. 'सेवाएं' स्क्रीन पर, 'Windows Media Player Network Sharing Service' खोजने के लिए नीचे स्क्रॉल करें।  
3. इस पर डबल-क्लिक करें और 'स्टार्टअप प्रकार' को 'मैनुअल' पर सेट करें।  
4. 'रोकें' बटन पर क्लिक करके सेवा बंद करें।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="DLNA सेवा रोकें" caption="DLNA नेटवर्क शेयरिंग सेवा अक्षम करें" width="500" >}}

## iPhone पर DLNA सर्वर से संगीत कैसे चलाएं

1. App Store से मुफ्त **Evermusic** ऐप इंस्टॉल करें:  
   [Evermusic ऐप](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. 'कनेक्शन' टैब खोलें और 'स्थानीय नेटवर्क' अनुभाग में 'उपलब्ध डिवाइस' पर टैप करें।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Evermusic कनेक्शन" caption="Evermusic: कनेक्शन स्क्रीन" width="500" >}}

3. डिवाइस सूची लोड होने तक कुछ सेकंड प्रतीक्षा करें और Windows Media Player DLNA सर्वर पर टैप करें (उदा., 'MSEDGEWIN10: My Windows Library')।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="उपलब्ध डिवाइस" caption="Evermusic में उपलब्ध DLNA सर्वर" width="500" >}}

4. आप मीडिया सर्वर पर उपलब्ध फोल्डरों की सूची देखेंगे।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Evermusic फोल्डर" caption="DLNA सर्वर से साझा फोल्डर ब्राउज़ करें" width="500" >}}

5. ऑडियो फ़ाइलों वाला कोई भी फोल्डर खोलें।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="फोल्डर सामग्री" caption="साझा DLNA फोल्डरों की सामग्री देखें" width="500" >}}

6. ऑडियो प्लेयर शुरू करने के लिए किसी भी फ़ाइल पर टैप करें।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="ऑडियो प्लेयर" caption="Evermusic में DLNA से ऑडियो फ़ाइल चलाएं" width="500" >}}

7. अपने ऑडियो अनुभव को बेहतर बनाने के लिए, स्क्रीन के नीचे वॉल्यूम इंडिकेटर के पास 'इक्वलाइज़र' आइकन पर टैप करें ताकि प्रीएम्पलीफायर के साथ iPod-स्टाइल इक्वलाइज़र सक्षम हो।

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="इक्वलाइज़र" caption="बेहतर प्लेबैक के लिए अंतर्निहित इक्वलाइज़र का उपयोग करें" width="500" >}}

## निष्कर्ष

Windows 10 पर DLNA मीडिया सर्वर और आपके iPhone पर Evermusic के साथ, आप अपने कंप्यूटर से अपने मोबाइल डिवाइस पर निर्बाध संगीत स्ट्रीमिंग का आनंद ले सकते हैं। भंडारण सीमाओं को अलविदा कहें और ऑन-डिमांड संगीत का स्वागत करें!

## अक्सर पूछे जाने वाले प्रश्न

{{% details title="क्या मुझे Windows 10 पर कोई सर्वर सॉफ्टवेयर इंस्टॉल करना होगा?" closed="true" %}}
नहीं। Windows 10 में एक अंतर्निहित DLNA मीडिया सर्वर शामिल है। आपको केवल नेटवर्क और शेयरिंग सेंटर सेटिंग्स में मीडिया स्ट्रीमिंग सक्षम करनी होगी। किसी तृतीय-पक्ष सॉफ्टवेयर की आवश्यकता नहीं है।
{{% /details %}}

{{% details title="क्या मेरे iPhone को एक ही Wi-Fi नेटवर्क पर होना चाहिए?" closed="true" %}}
हां। DLNA स्ट्रीमिंग आपके स्थानीय नेटवर्क पर काम करती है। Evermusic को DLNA सर्वर खोजने के लिए आपके Windows 10 PC और iPhone दोनों को एक ही Wi-Fi नेटवर्क से कनेक्ट होना चाहिए।
{{% /details %}}

{{% details title="DLNA के माध्यम से मैं कौन से ऑडियो प्रारूप स्ट्रीम कर सकता हूं?" closed="true" %}}
Windows DLNA सर्वर आपके संगीत फोल्डर से प्रारूप की परवाह किए बिना फ़ाइलें साझा करता है। Evermusic MP3, FLAC, AAC, WAV, OGG, AIFF और कई अन्य प्रारूपों का समर्थन करता है, इसलिए आप सर्वर से लगभग कोई भी ऑडियो फ़ाइल चला सकते हैं।
{{% /details %}}

{{% details title="क्या मैं Evermusic की जगह Flacbox का उपयोग कर सकता हूं?" closed="true" %}}
हां। Flacbox भी DLNA/UPnP ब्राउज़िंग और प्लेबैक का समर्थन करता है। आप अपने Windows DLNA सर्वर से संगीत खोजने और चलाने के लिए किसी भी ऐप का उपयोग कर सकते हैं।
{{% /details %}}

{{% details title="क्या DLNA स्ट्रीमिंग मोबाइल डेटा का उपयोग करेगी?" closed="true" %}}
नहीं। DLNA पूरी तरह से आपके स्थानीय Wi-Fi नेटवर्क पर काम करता है। यह किसी भी मोबाइल डेटा का उपयोग नहीं करता है। हालांकि, प्लेबैक के दौरान दोनों डिवाइसों को एक ही नेटवर्क से कनेक्ट रहना चाहिए।
{{% /details %}}
