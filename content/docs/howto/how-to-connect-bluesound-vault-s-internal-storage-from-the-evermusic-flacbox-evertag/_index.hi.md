---
title: "Evermusic, Flacbox, Evertag से Bluesound VAULT के आंतरिक स्टोरेज को कैसे कनेक्ट करें"
date: 2022-03-10
description: "जानें कि SMB प्रोटोकॉल का उपयोग करके Evermusic, Flacbox और Evertag से Bluesound VAULT की आंतरिक हार्ड ड्राइव तक कैसे पहुंचें, ऑडियो फाइलों को प्रबंधित, संपादित और चलाने के लिए।"
keywords: ["bluesound vault", "smb स्टोरेज कनेक्ट करें", "evermusic smb", "flacbox vault", "evertag smb", "nas स्टोरेज संगीत", "vault आंतरिक ड्राइव"]
tags: ["evermusic", "कनेक्ट", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**सारांश:** Evermusic, Flacbox या Evertag का उपयोग करके SMB के माध्यम से अपने Bluesound VAULT के आंतरिक स्टोरेज से कनेक्ट करें। BluOS ऐप में VAULT का IP पता खोजें, इसे अतिथि पहुंच के साथ SMB कनेक्शन के रूप में दर्ज करें, और अपनी संगीत फाइलों को चलाना या प्रबंधित करना शुरू करें।

Bluesound VAULT में एक आंतरिक हार्ड ड्राइव है और यह नेटवर्क अटैच्ड स्टोरेज (NAS) के रूप में काम करता है। VAULT की आंतरिक हार्ड ड्राइव तक पहुंचने से आप हमारे ऐप्स Evermusic, Flacbox, Evertag से फाइलें जोड़/हटा सकते हैं, मेटाडेटा टैग संपादित कर सकते हैं।

**आपके VAULT की आंतरिक हार्ड ड्राइव तक पहुंचने के चरण निम्नलिखित हैं:**

1. BluOS ऐप में, **सहायता > निदान** चुनें।

2. **निदान** पृष्ठ से, VAULT का **IP पता** प्राप्त करें। इस **IP पते** का उपयोग अगले चरणों में किया जाएगा।

3. Evermusic, Flacbox या Evertag खोलें।

   ![Everappz एप्लिकेशन](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. "संपर्क" स्क्रीन खोलें और "क्लाउड सेवा कनेक्ट करें" मेनू आइटम चुनें।

   ![Evermusic संपर्क स्क्रीन](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. "SMB" क्लाउड सेवा चुनें।

   ![Evermusic क्लाउड सेवा कनेक्ट करें स्क्रीन](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. "SMB कॉन्फ़िगरेशन स्क्रीन" पर निम्नलिखित प्रारूप में URL दर्ज करें:

   ```
   SMB://<<VAULT-IP>>
   ```

   `<<VAULT-IP>>` को चरण 2 में प्राप्त **IP पते** से बदलें।

   **नोट:** लॉगिन और पासवर्ड फ़ील्ड खाली छोड़ दें क्योंकि VAULT स्टोरेज अतिथि (GUEST) मोड का समर्थन करता है।

   ![Evermusic SMB कनेक्शन स्क्रीन](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. कॉन्फ़िगरेशन सहेजने के लिए "साइन इन" बटन टैप करें।

8. कनेक्टेड क्लाउड स्टोरेज खोलें और ऑडियो फाइलों वाले फ़ोल्डर में नेविगेट करें और ऑडियो प्लेयर शुरू करने के लिए किसी भी फाइल पर टैप करें।

   ![Evermusic खुला SMB सर्वर स्क्रीन](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. आप बिल्ट-इन फ़ाइल मैनेजर का उपयोग करके भी फाइलें संपादित कर सकते हैं।

   ![Evermusic फ़ाइल मैनेजर स्क्रीन](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

इन सरल चरणों के साथ, आप आसानी से अपने Bluesound VAULT की आंतरिक हार्ड ड्राइव तक पहुंच सकते हैं और Evermusic, Flacbox या Evertag का उपयोग करके अपनी संगीत लाइब्रेरी को नियंत्रित कर सकते हैं।

## अक्सर पूछे जाने वाले प्रश्न

{{% details title="क्या मुझे Bluesound VAULT से कनेक्ट करने के लिए उपयोगकर्ता नाम और पासवर्ड की आवश्यकता है?" closed="true" %}}
नहीं। Bluesound VAULT SMB के माध्यम से अतिथि (अनाम) पहुंच का समर्थन करता है। कनेक्शन कॉन्फ़िगर करते समय लॉगिन और पासवर्ड फ़ील्ड खाली छोड़ दें।
{{% /details %}}

{{% details title="क्या मैं Bluesound VAULT पर संगीत टैग संपादित कर सकता हूं?" closed="true" %}}
हां। Evertag का उपयोग करके, आप VAULT की आंतरिक हार्ड ड्राइव पर सीधे संग्रहीत ऑडियो फाइलों के लिए मेटाडेटा टैग (शीर्षक, कलाकार, एल्बम, आदि) संपादित कर सकते हैं।
{{% /details %}}

{{% details title="Bluesound VAULT कौन से प्रोटोकॉल का समर्थन करता है?" closed="true" %}}
Bluesound VAULT अपने आंतरिक स्टोरेज को SMB (Server Message Block) के माध्यम से उपलब्ध कराता है। Evermusic, Flacbox और Evertag सभी SMB कनेक्शन का समर्थन करते हैं, जिससे कनेक्ट करना आसान हो जाता है।
{{% /details %}}

{{% details title="क्या मैं अपने iPhone में फाइलें कॉपी किए बिना VAULT से संगीत स्ट्रीम कर सकता हूं?" closed="true" %}}
हां। SMB के माध्यम से कनेक्ट होने के बाद, आप VAULT की आंतरिक ड्राइव से सीधे ऑडियो फाइलें स्ट्रीम कर सकते हैं बिना उन्हें अपने डिवाइस में कॉपी किए।
{{% /details %}}
