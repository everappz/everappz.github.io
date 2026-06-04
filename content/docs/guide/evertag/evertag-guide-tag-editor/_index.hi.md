---
title: "टैग एडिटर"
date: 2020-02-01
description: "Evertag टैग एडिटर का उपयोग करके म्यूज़िक मेटाडेटा अपडेट करना, एल्बम कवर संपादित करना, कई फ़ाइलें batch edit करना और MusicBrainz से टैग प्रबंधित करना सीखें। iOS और Mac पर अपनी म्यूज़िक लाइब्रेरी व्यवस्थित करने के लिए आदर्श।"
keywords: [
  "Evertag टैग एडिटर", "ऑडियो मेटाडेटा एडिटर", "म्यूज़िक टैग एडिटर",
  "iPhone पर ऑडियो टैग संपादित करें", "एल्बम कवर एडिटर", "ऑडियो टैग batch edit",
  "MusicBrainz मेटाडेटा", "म्यूज़िक ऑर्गनाइज़र ऐप", "Evertag गाइड", "ID3 टैग एडिटर"
]
tags: ["गाइड", "evertag", "टैग एडिटर"]
readingTime: 5
---


**टैग एडिटर** Evertag ऐप की मुख्य स्क्रीन है जहाँ आप ऑडियो फ़ाइल मेटाडेटा देख और संपादित कर सकते हैं। **स्थानीय फ़ाइलें** अनुभाग से या किसी भी कनेक्टेड **cloud storage** account से फ़ाइल टैप करके यह स्क्रीन खोलें।

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag टैग एडिटर स्क्रीन" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## संपादन मोड

Evertag दो संपादन मोड प्रदान करता है:

- **Single-file मोड**
  - artwork carousel पर बाएँ या दाएँ swipe करके फ़ाइलों के बीच नेविगेट करें।

- **Batch मोड**
  - एक साथ कई फ़ाइलें संपादित करें और साझा मेटाडेटा लागू करें।
  - सक्रिय करने के लिए, नीचे scroll करें और **एक साथ कई फ़ाइलें संपादित करें** टैप करें।

## Single-File मोड

डिफ़ॉल्ट रूप से, ऐप single-file mode में केवल मुख्य संपादन विकल्प सक्षम करके टैग एडिटर खोलता है। इस मोड में, आप सबसे सामान्य metadata fields संपादित कर सकते हैं, जैसे:

**Track Title, Subtitle, Album Artist, Album, Artist, Composer, Performer, Genre, Comment, Beats Per Minute, Podcast, Compilation, Disc Number, Track Number, Track Total, Rating, Year**

सभी उपलब्ध टैग एक्सेस करने के लिए, स्क्रीन के नीचे scroll करें और **Show Extended Tags** विकल्प टैप करें। यह एडिटर को extended mode में switch करेगा, जिससे आप **120 से अधिक metadata fields** संपादित कर सकते हैं, जिसमें **MusicBrainz Tags**, **Lyrics**, **Advisory Ratings**, replay-gain values, sort orders, podcast metadata और अधिक शामिल हैं। **सेटिंग्स → ऑडियो टैग एडिटर → मुख्य स्क्रीन पर बटन** का उपयोग करके Show Extended Tags को permanently toggle करें ताकि यह हमेशा on रहे।

{{< cards cols="1">}}
{{< card title="" subtitle="Bottom Actions Panel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Batch मोड

आप batch editing दो तरीकों से शुरू कर सकते हैं:

1. **फ़ाइल मैनेजर से**
   - ऊपरी दाएँ में **More actions** (•••) टैप करें।
   - **चुनें** टैप करें, कई फ़ाइलें चुनें, और फिर **ऑडियो टैग संपादित करें** टैप करें।

2. **टैग एडिटर से**
   - कोई भी फ़ाइल खोलें, नीचे scroll करें, और उसी folder की सभी फ़ाइलें load करने के लिए **एक साथ फ़ाइलें संपादित करें** टैप करें।

{{< cards cols="1">}}
{{< card title="" subtitle="Batch Editing मोड" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

संपादन के बाद, changes लागू करने के लिए **सेव करें** टैप करें।

## गीत संपादित करें

extended editor **Lyrics** field दिखाता है। गीत सूची खोलने के लिए उसे टैप करें — प्रत्येक lyrics entry की अपनी भाषा और description होती है, इसलिए एक ट्रैक कई translations संग्रहीत कर सकता है।

आपको गीत खुद टाइप नहीं करने होंगे। एडिटर में web पर सबसे लोकप्रिय lyrics databases के one-tap search shortcuts हैं, जो current track के artist और title से pre-filled हैं:

- **Lrclib** — **timed (LRC-style) lyrics** के लिए go-to public database। इसका उपयोग तब करें जब आप synced lyrics चाहते हों जो उन्हें support करने वाले players में line-by-line scroll करें।
- **Genius** — annotations और accurate plain-text lyrics के साथ बड़ा catalog।
- **Lyricsify** — plain और timestamped lyrics के साथ community-driven database।
- **Google** — जब dedicated databases में match न हो तो fallback के रूप में general web search।

प्रत्येक shortcut तभी दिखाई देता है जब corresponding service आपके डिवाइस से reachable हो। एक service टैप करें, जो lyrics (या LRC timestamps) चाहते हों copy करें, Evertag पर वापस आएँ, और उन्हें text field में paste करें — फिर lyrics को ऑडियो फ़ाइल के टैग में write करने के लिए **सेव करें**।

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Pages" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

picker से एक भाषा चुनें:

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Language Selector" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

फिर lyrics text paste करें या टाइप करें। Evertag plain text और timestamped (synced) lyrics दोनों का समर्थन करता है — placeholder LRC-style format का एक उदाहरण दिखाता है, जो कि synced results के लिए Lrclib और Lyricsify return करते हैं।

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Text Editor" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Rating और Advisory Rating सेट करें

extended editor एक star **Rating** control और एक **Advisory Rating** segmented control प्रदान करता है।

### Star Rating

किसी track को एक से पाँच stars का personal score देने के लिए **Rating** field का उपयोग करें। मान फ़ाइल के standard rating tag में लिखा जाता है (ID3 के लिए POPM, MP4 के लिए `rate`, Vorbis/APE के लिए `RATING`, आदि), इसलिए अन्य ऐप जो यह टैग पढ़ते हैं — जिसमें Music app, Plex, Roon और अधिकांश desktop tag editors शामिल हैं — आपके scores तुरंत उठाएँगे।

{{< cards cols="1">}}
  {{< card title="" subtitle="Rating" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Advisory Rating

**Advisory Rating** iTunes Store और अधिकांश music platforms द्वारा उपयोग किए जाने वाले Parental Advisory standard के मूल्यों में से एक का उपयोग करके track की content को चिह्नित करता है:

- **Inoffensive** — बिना parental-advisory जानकारी वाले tracks के लिए default। फ़ाइल को सभी श्रोताओं के लिए उपयुक्त माना जाता है और उन players में कोई advisory label नहीं दिखाएगी जो टैग का सम्मान करते हैं।
- **Explicit** — track में explicit language या content है। Players जो parental controls का सम्मान करते हैं (Music app, Apple TV app, Spotify exports, Plex, आदि) title के पास **E** badge दिखाएँगे और जब डिवाइस या account पर restrictions सक्षम हों, तो kids' profiles से track छुपा सकते हैं या उसे play करने से मना कर सकते हैं।
- **Clean** — अन्यथा explicit track का censored या edited संस्करण। Players एक **C** badge दिखाते हैं ताकि श्रोता clean edit को original explicit master से अलग कर सकें, जो तब उपयोगी है जब दोनों versions एक ही library में हों।

आप इस field को set या fix करना चाहेंगे जब:

- किसी फ़ाइल पर गलत label है (उदाहरण के लिए एक clean radio edit जो गलती से Explicit के रूप में tagged थी, या उल्टा)।
- Tracks बिना टैग के ripped या downloaded किए गए थे और अब Inoffensive के रूप में दिखाई दे रहे हैं भले ही उनमें explicit content हो — parental controls और family-shared libraries के सही ढंग से काम करने के लिए आवश्यक।
- आप submission या sharing के लिए एक album तैयार कर रहे हैं और प्रत्येक track में consistent metadata होना चाहते हैं।
- आप चाहते हैं कि CarPlay, Lock Screen, Apple Music–style players, या DJ software track title के पास सही **E** / **C** badge दिखाएँ।

मान file format के लिए standard advisory-rating field में संग्रहीत होता है (MP4 के लिए `rtng`, ID3 के लिए `TXXX:ITUNESADVISORY`, Vorbis के लिए `ITUNESADVISORY`), इसलिए कोई भी player जो parental-advisory metadata पढ़ता है आपका update देखेगा।

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Advisory Rating" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## एल्बम कवर संपादित करें

एल्बम कवर बदलने के लिए:

1. artwork carousel में **Camera icon** टैप करें।
2. image location चुनें: Local Files, Cloud, Downloads, या Photo Library।
3. cover art के रूप में लागू करने के लिए एक image चुनें।

{{< cards cols="1">}}
  {{< card title="" subtitle="Image चुनें" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## टैग एडिटर में अधिक क्रियाएँ

artwork view के नीचे toolbar के माध्यम से अतिरिक्त संपादन विकल्प उपलब्ध हैं।

{{< cards cols="1">}}
  {{< card title="" subtitle="More Actions मेनू" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### ऑडियो टैग Auto-Search

यह action smart tag search engine सक्रिय करती है, जो existing information के आधार पर आपकी ऑडियो फ़ाइल के लिए complete metadata खोजती और भरती है।
ऐप MusicBrainz database — सबसे comprehensive tag databases में से एक — का उपयोग करता है, जिसमें **50 मिलियन** से अधिक tracks हैं।

### एल्बम कवर खोजें

सही album artwork के लिए web पर खोजने के लिए metadata का उपयोग करें।

{{< cards cols="1">}}
  {{< card title="" subtitle="एल्बम कवर खोजें" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

मिलने के बाद, system context menu का उपयोग करके image अपने **Photos** में सेव करें।

{{< cards cols="1">}}
  {{< card title="" subtitle="Photos में Image जोड़ें" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

उसके बाद, टैग एडिटर पर वापस आएँ, Camera icon टैप करें, **Photos Library** पर जाएँ, और सेव की गई image चुनें। ऐप इसे आपकी ऑडियो फ़ाइल के cover के रूप में सेट करेगा।

आप ऐप की सेटिंग्स में cover images को कैसे scale किया जाए समायोजित कर सकते हैं।

### एल्बम आर्टवर्क सेव करें

यह action current album artwork को **Documents** folder में सेव करती है, ताकि आप इसे बाद में reuse कर सकें।

### एन्कोडिंग नॉर्मलाइज़ करें

यह action ऑडियो फ़ाइल के metadata में सभी टैग का text encoding normalize करेगी। यह विशेष रूप से सहायक होती है यदि आप Windows PC से switch कर रहे हैं, जहाँ फ़ाइलें different encodings का उपयोग कर सकती हैं जो Mac पर अपठनीय या garbled characters के रूप में दिखाई देती हैं।

### Manual Tags Search

MusicBrainz database का उपयोग करके album metadata मैन्युअल रूप से खोजें।

- album चुनें

{{< cards cols="1">}}
  {{< card title="" subtitle="Album चुनें" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- सही song चुनें

{{< cards cols="1">}}
  {{< card title="" subtitle="Song चुनें" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- कौन-से टैग लागू करने हैं चुनें

{{< cards cols="1">}}
  {{< card title="" subtitle="ऑडियो टैग चुनें" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

अपने track पर चुना हुआ metadata लागू करने के लिए **पूर्ण करना** टैप करें।

### ऑडियो टैग हटाएँ

किसी फ़ाइल के सभी metadata fields साफ़ करें। नए सिरे से शुरू करते समय उपयोगी। पुष्टि करने के लिए **सेव करें** टैप करें।

## टैग एडिटर सेटिंग्स

व्यवहार कस्टमाइज़ करने के लिए **सेटिंग्स → ऑडियो टैग एडिटर** पर जाएँ।

### एल्बम कवर स्केलिंग

चुनें कि ऑडियो फ़ाइलों में सेव करते समय album covers को कैसे scale किया जाए। आप original image size रखने के लिए scaling disable कर सकते हैं, लेकिन ध्यान रखें कि कुछ players बड़े artwork files का समर्थन नहीं कर सकते। "original size" विकल्प Premium personalization features का हिस्सा है।

### टैग सेविंग विकल्प

- **ID3v2.4** — सक्षम होने पर, ऐप जब संभव हो ID3v2.4 format में टैग सेव करता है। यदि आपके ऑडियो टैग पुराने players या डिवाइस पर सही ढंग से प्रदर्शित नहीं होते तो अधिक व्यापक रूप से supported ID3v2.3 पर वापस आने के लिए disable करें।
- **Duplicate tags** — सक्षम होने पर, सामान्य metadata fields फ़ाइल के दोनों tag sections में duplicate होती हैं। यह पुराने audio players के साथ compatibility बेहतर बनाता है, लेकिन अधिकांश मामलों में इसकी आवश्यकता नहीं होती।

### Cloud File Metadata Update विकल्प

आप नियंत्रित कर सकते हैं कि ऐप cloud services में संग्रहीत ऑडियो फ़ाइलों के लिए metadata कैसे अपडेट करता है:

- **पुष्टि संदेश दिखाएँ**
  cloud files पर metadata changes लागू करने से पहले पूछें।

- **फ़ाइल का metadata स्वचालित रूप से अपडेट करें**
  संपादन के बाद cloud file में metadata changes स्वचालित रूप से सेव करें।

- **फ़ाइल का metadata अपडेट न करें**
  cloud files को update करना छोड़ें — changes केवल locally लागू होंगे।

### ऑनलाइन फ़ाइलें संपादित करें

संपादन के बाद cloud files की locally downloaded copies के साथ क्या हो चुनें:

- **डाउनलोड की गई फ़ाइल हमेशा हटाएँ**
  changes सेव करने के बाद local copy हटाएँ।

- **डाउनलोड की गई फ़ाइल न हटाएँ**
  संपादन के बाद downloaded file अपने डिवाइस पर रखें।

### मुख्य स्क्रीन बटन

टैग एडिटर की मुख्य स्क्रीन पर कौन-सी actions दिखाई दें कस्टमाइज़ करें (Auto-search audio tags, Manual search audio tags, Search album artwork, Save album artwork, Normalize encoding, Delete audio tags)। आप **Show extended tags** और **Edit files simultaneously** भी toggle कर सकते हैं ताकि एडिटर हमेशा आपके preferred mode में खुले।
