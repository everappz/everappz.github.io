---
title: "WebDAV का उपयोग करके NAS स्टोरेज कनेक्ट करें और अपने iPhone या Mac पर संगीत सुनें"
date: 2024-07-28
description: "जानें कि अपने Synology NAS पर WebDAV कैसे कॉन्फ़िगर करें और Evermusic या Flacbox का उपयोग करके अपने iPhone या Mac पर संगीत स्ट्रीम करें। हमारी चरण-दर-चरण मार्गदर्शिका का पालन करें।"
keywords: ["nas कनेक्ट करें", "webdav synology", "संगीत स्ट्रीम nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["संगीत", "स्ट्रीमिंग", "स्टोरेज", "nas", "कनेक्ट", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**संक्षेप में:** अपने Synology NAS पर WebDAV इंस्टॉल और सक्षम करें, साझा फ़ोल्डर अनुमतियाँ कॉन्फ़िगर करें, फिर NAS IP पते और WebDAV पोर्ट (डिफ़ॉल्ट 5005/5006) का उपयोग करके Evermusic या Flacbox से कनेक्ट करें। आप अपने डिवाइस पर फ़ाइलें कॉपी किए बिना अपनी पूरी संगीत लाइब्रेरी स्ट्रीम और प्रबंधित कर सकते हैं।

जानें कि WebDAV का उपयोग करके अपने NAS स्टोरेज को कैसे कनेक्ट करें और अपनी संगीत लाइब्रेरी को आसानी से अपने iPhone या Mac पर स्ट्रीम करें। WebDAV (Web-based Distributed Authoring and Versioning) एक प्रोटोकॉल है जो आपको इंटरनेट पर फ़ाइलों को प्रबंधित और साझा करने की अनुमति देता है। अपने NAS पर WebDAV सेट करके, आप अपने संगीत संग्रह तक पहुँच सकते हैं और उसे स्ट्रीम कर सकते हैं, जिससे आपके पसंदीदा गाने हमेशा आपकी उंगलियों पर रहें।

इस मार्गदर्शिका में, हम आपको दिखाएंगे कि सबसे लोकप्रिय NAS सर्वरों में से एक, Synology NAS पर WebDAV कनेक्शन कैसे सेट करें। अपने Synology NAS पर WebDAV कॉन्फ़िगर करने के लिए हमारे सरल चरणों का पालन करें, और आप अपने iPhone या Mac से सीधे अपनी संगीत लाइब्रेरी ब्राउज़, स्ट्रीम और प्रबंधित कर पाएंगे।

## चरण 1: Synology NAS पर WebDAV इंस्टॉल करें

1. अपने Synology NAS में लॉग इन करें और **पैकेज सेंटर** खोलें।
2. "webdav" खोजें और अगर यह पहले से इंस्टॉल नहीं है तो WebDAV पैकेज इंस्टॉल करें। इसे कॉन्फ़िगर करने के लिए WebDAV सर्वर खोलें।

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Synology पर WebDAV इंस्टॉल करें" width="600" >}}

## चरण 2: WebDAV सर्वर कॉन्फ़िगर करें

1. WebDAV सेटिंग्स पेज पर, **HTTP सक्षम करें**, **HTTPS सक्षम करें**, **अनाम WebDAV सक्षम करें**, और **DavDepthInfinity सक्षम करें** के बॉक्स चेक करें।
2. परिवर्तन सहेजने के लिए **लागू करें** पर क्लिक करें। HTTP और HTTPS कनेक्शन के लिए पोर्ट नंबर नोट करें, जो डिफ़ॉल्ट रूप से 5005 और 5006 हैं।

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="WebDAV सेटिंग्स कॉन्फ़िगर करें" width="600" >}}

## चरण 3: साझा फ़ोल्डर अनुमतियाँ कॉन्फ़िगर करें

1. **नियंत्रण कक्ष** खोलें और **साझा फ़ोल्डर** अनुभाग पर जाएं।
2. **संगीत** फ़ोल्डर चुनें और **संपादित करें** पर क्लिक करें।
3. **अनुमतियाँ** टैब में, अनुमतियाँ कॉन्फ़िगर करें। अगर आपको केवल संगीत सुनना है तो केवल-पढ़ने के साथ अतिथि पहुँच सक्षम करें, या अगर आपको फ़ाइलें संशोधित करनी हैं तो पढ़ने/लिखने के साथ। परिवर्तन सहेजें।

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="साझा फ़ोल्डर अनुमतियाँ" width="600" >}}

## चरण 4: Synology NAS का IP पता खोजें

1. **नियंत्रण कक्ष** खोलें और **नेटवर्क इंटरफ़ेस** टैब पर जाएं, या अपने वेब ब्राउज़र का उपयोग करके [find.synology.com](http://find.synology.com) पर जाएं।

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="NAS IP पता खोजें" width="600" >}}

2. अपने Synology NAS का IP पता नोट करें (उदा., 192.168.18.137)।

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Synology NAS IP पता" width="600" >}}

## चरण 5: Evermusic/Flacbox का उपयोग करके Synology NAS से कनेक्ट करें

1. Evermusic या Flacbox ऐप खोलें और **संपर्क** टैब पर जाएं।

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Evermusic में संपर्क टैब" width="600" >}}

2. स्वचालित कनेक्शन के लिए, **उपलब्ध उपकरण** अनुभाग में अपना Synology NAS खोजें और कनेक्ट करने के लिए टैप करें।

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="उपलब्ध उपकरणों की सूची" width="600" >}}

3. मैन्युअल कनेक्शन के लिए, **क्लाउड सेवा से कनेक्ट करें** चुनें और **WebDAV** चुनें। सर्वर पता इस प्रारूप में दर्ज करें: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (उदा., [https://192.168.18.137:5006](https://192.168.18.137:5006))।

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="मैन्युअल WebDAV कॉन्फ़िगरेशन" width="600" >}}

4. अतिथि पहुँच के लिए लॉगिन और पासवर्ड फ़ील्ड खाली छोड़ें, या अपने Synology क्रेडेंशियल दर्ज करें। **साइन इन** पर टैप करें।

## चरण 6: नेविगेट करें और संगीत चलाएं

1. कनेक्ट होने के बाद, डिवाइस **जुड़े हुए उपकरण** सूची में दिखाई देगा।

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Evermusic में कनेक्टेड डिवाइस" width="600" >}}

2. **संगीत** फ़ोल्डर पर नेविगेट करें और प्लेबैक शुरू करने के लिए किसी भी ऑडियो फ़ाइल पर टैप करें।

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="संगीत फ़ोल्डर ब्राउज़ करना" width="600" >}}

## चरण 7: कनेक्टेड क्लाउड फ़ोल्डर को संगीत लाइब्रेरी में जोड़ें

1. ऐप में **संगीत लाइब्रेरी** अनुभाग खोलें।
2. **संगीत जोड़ें** चुनें और **संपर्क** चुनें।
3. अपना कनेक्टेड NAS सर्वर चुनें और **संगीत** फ़ोल्डर चुनें। **पूर्ण करना** पर टैप करें।
4. ऐप संगीत फ़ोल्डर को स्कैन करेगा और समर्थित ऑडियो फ़ाइलों को संगीत लाइब्रेरी में जोड़ेगा। मेटाडेटा लोड होगा, और आपके ट्रैक एल्बम, कलाकार और शैली के अनुसार समूहित होंगे।

## निष्कर्ष

इन चरणों का पालन करके, आप आसानी से अपने Synology NAS पर WebDAV कनेक्शन सेट कर सकते हैं और Evermusic या Flacbox का उपयोग करके अपनी संगीत लाइब्रेरी को अपने iPhone या Mac पर स्ट्रीम कर सकते हैं। किसी भी समय अपने पसंदीदा गानों तक निर्बाध पहुँच का आनंद लें।

## अक्सर पूछे जाने वाले प्रश्न

{{% details title="कौन से NAS डिवाइस WebDAV का समर्थन करते हैं?" closed="true" %}}
अधिकांश लोकप्रिय NAS ब्रांड WebDAV का समर्थन करते हैं, जिनमें Synology, QNAP, TrueNAS और Western Digital शामिल हैं। WebDAV सेटअप निर्देशों के लिए अपने NAS निर्माता के दस्तावेज़ देखें।
{{% /details %}}

{{% details title="NAS संगीत स्ट्रीमिंग के लिए WebDAV और SMB में क्या अंतर है?" closed="true" %}}
WebDAV HTTP/HTTPS पर काम करता है और इंटरनेट पर रिमोट एक्सेस के लिए बेहतर है। SMB आमतौर पर स्थानीय नेटवर्क पर तेज़ होता है। Evermusic और Flacbox दोनों प्रोटोकॉल का समर्थन करते हैं, इसलिए चुनें कि आपको स्थानीय या रिमोट एक्सेस की आवश्यकता है।
{{% /details %}}

{{% details title="क्या मुझे Synology पर WebDAV के लिए उपयोगकर्ता नाम और पासवर्ड की आवश्यकता है?" closed="true" %}}
नहीं, अगर आप अनाम WebDAV एक्सेस सक्षम करते हैं और अपने साझा फ़ोल्डर पर अतिथि अनुमतियाँ कॉन्फ़िगर करते हैं। बेहतर सुरक्षा के लिए, आप इसके बजाय अपने Synology क्रेडेंशियल का उपयोग कर सकते हैं।
{{% /details %}}

{{% details title="क्या मैं WebDAV के माध्यम से NAS से FLAC और अन्य हाई-रेज़ फ़ॉर्मेट स्ट्रीम कर सकता हूँ?" closed="true" %}}
हाँ। Evermusic और Flacbox दोनों WebDAV के माध्यम से NAS स्टोरेज से स्ट्रीमिंग करते समय FLAC, ALAC, WAV, DSD और अन्य उच्च-रिज़ॉल्यूशन फ़ॉर्मेट का समर्थन करते हैं।
{{% /details %}}

{{% details title="ऐप उपलब्ध उपकरणों में मेरा NAS क्यों नहीं ढूंढ पा रहा है?" closed="true" %}}
सुनिश्चित करें कि आपका iPhone/Mac और NAS एक ही Wi-Fi नेटवर्क पर हैं। अगर स्वचालित खोज काम नहीं करती है, तो मैन्युअल कनेक्शन विकल्प का उपयोग करें और NAS IP पता और WebDAV पोर्ट सीधे दर्ज करें।
{{% /details %}}
