---
title: "AVAssetResourceLoader के साथ iOS ऑडियो स्ट्रीमिंग"
date: 2015-06-20
description: "कस्टम URL स्कीम और डिस्क कैशिंग के साथ AVAssetResourceLoaderDelegate और AVPlayer का उपयोग करके iOS पर ऑडियो स्ट्रीम और कैश करना सीखें।"
keywords: ["iOS ऑडियो स्ट्रीमिंग", "AVAssetResourceLoaderDelegate", "AVURLAsset", "AVPlayer ट्यूटोरियल", "AVFoundation ऑडियो", "AVAssetResourceLoadingRequest", "कस्टम ऑडियो प्लेयर iOS", "क्लाउड ऑडियो स्ट्रीमिंग iOS", "ऑडियो कैशिंग iOS", "Swift AVPlayer कस्टम स्कीम"]
tags: ["streaming", "AVPlayer", "AVFoundation", "iOS", "AVAssetResourceLoader", "tutorial", "Objective-C", "audio caching"]
draft: false
aliases:
  - /post/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/
  - /amp/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/
  - /single-post/Audio-Streaming-and-Caching-in-iOS-using-AVAssetResourceLoader-and-AVPlayer/
  - /index.php/2015/02/10/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

![](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/diagram.png)

**संक्षेप में:** AVPlayer के रिसोर्स लोडिंग को इंटरसेप्ट करने के लिए कस्टम URL स्कीम के साथ `AVAssetResourceLoaderDelegate` का उपयोग करें। इससे आप क्लाउड सेवाओं के लिए कस्टम ऑथराइज़ेशन हेडर जोड़ सकते हैं, ऑडियो को डिस्क पर कैश कर सकते हैं, और स्ट्रीमिंग व्यवहार को नियंत्रित कर सकते हैं -- बिना लोकल HTTP प्रॉक्सी लिखे। पूरा सोर्स कोड [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader) पर उपलब्ध है।

---

## AVPlayer को कस्टम रिसोर्स लोडर की आवश्यकता क्यों है

`AVPlayer` लोकल फ़ाइलों और रिमोट URL से ऑडियो चलाता है। अधिकांश क्लाउड सेवाओं (Dropbox, Google Drive, Box) के लिए, आप एक सीधा डाउनलोड URL पास कर सकते हैं और प्लेबैक तुरंत काम करता है।

हालाँकि, **Yandex.Disk** और **WebDAV** जैसी कुछ सेवाओं के लिए GET अनुरोधों पर कस्टम ऑथराइज़ेशन हेडर की आवश्यकता होती है। `AVPlayer` इन हेडर को इंजेक्ट करने का कोई अंतर्निहित तरीका नहीं देता।

समाधान: `AVURLAsset` की `resourceLoader` प्रॉपर्टी का उपयोग करें। यह API रिसोर्स लोडिंग अनुरोधों को इंटरसेप्ट करता है, जटिलता के बिना एक लोकल HTTP प्रॉक्सी की तरह काम करता है।

### यह कैसे काम करता है

`AVPlayer` तब `resourceLoader` का उपयोग करता है जब वह URL स्कीम को नहीं पहचानता। `https://` को कस्टम स्कीम (जैसे `customscheme://`) से बदलकर, आप AVPlayer को सारी लोडिंग आपके ऐप को सौंपने के लिए मजबूर करते हैं।

आपको `AVAssetResourceLoaderDelegate` के दो मेथड लागू करने होंगे:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- जब AVPlayer को डेटा चाहिए तब कॉल किया जाता है। `AVAssetResourceLoadingRequest` को सेव करें और अपना डेटा लोडिंग ऑपरेशन शुरू करें।
2. **`resourceLoader:didCancelLoadingRequest:`** -- जब कोई अनुरोध रद्द या प्रतिस्थापित हो जाता है तब कॉल किया जाता है।

## कस्टम AVPlayer कैसे बनाएं

कस्टम URL स्कीम के साथ AVPlayer सेट करें:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

यह कोड:
- आपकी कस्टम स्कीम के साथ एक URL परिभाषित करता है
- मुख्य कतार पर डेलीगेट के साथ `AVURLAsset` बनाता है
- asset से `AVPlayerItem` बनाता है
- `AVPlayer` इनिशियलाइज़ करता है

## रिसोर्स लोडर डेलीगेट लागू करना

सर्वर से डेटा लाने और उसे `AVURLAsset` को वापस पास करने के लिए `LSFilePlayerResourceLoader` नाम की क्लास बनाएं। रिसोर्स URL द्वारा कुंजीबद्ध डिक्शनरी में लोडर इंस्टेंस संग्रहीत करें।

```objc
- (BOOL)resourceLoader:(AVAssetResourceLoader *)resourceLoader shouldWaitForLoadingOfRequestedResource:(AVAssetResourceLoadingRequest *)loadingRequest {
    NSURL *resourceURL = [loadingRequest.request URL];
    if ([resourceURL.scheme isEqualToString:@"customscheme"]) {
        LSFilePlayerResourceLoader *loader = [self resourceLoaderForRequest:loadingRequest];
        if (!loader) {
            loader = [[LSFilePlayerResourceLoader alloc] initWithResourceURL:resourceURL session:self.session];
            loader.delegate = self;
            [self.resourceLoaders setObject:loader forKey:[self keyForResourceLoaderWithURL:resourceURL]];
        }
        [loader addRequest:loadingRequest];
        return YES;
    }
    return NO;
}

- (void)resourceLoader:(AVAssetResourceLoader *)resourceLoader didCancelLoadingRequest:(AVAssetResourceLoadingRequest *)loadingRequest {
    LSFilePlayerResourceLoader *loader = [self resourceLoaderForRequest:loadingRequest];
    [loader removeRequest:loadingRequest];
}
```

ये मेथड URL स्कीम जाँचते हैं, एक लोडर बनाते या प्राप्त करते हैं, और अनुरोध को लोडर की कतार में जोड़ते हैं। अपरिचित स्कीम `NO` लौटाती हैं।

## LSFilePlayerResourceLoader इंटरफ़ेस

```objc
@interface LSFilePlayerResourceLoader : NSObject
@property (nonatomic, readonly, strong) NSURL *resourceURL;
@property (nonatomic, readonly) NSArray *requests;
@property (nonatomic, readonly, strong) YDSession *session;
@property (nonatomic, readonly, assign) BOOL isCancelled;
@property (nonatomic, weak) id<LSFilePlayerResourceLoaderDelegate> delegate;
- (instancetype)initWithResourceURL:(NSURL *)url session:(YDSession *)session;
- (void)addRequest:(AVAssetResourceLoadingRequest *)loadingRequest;
- (void)removeRequest:(AVAssetResourceLoadingRequest *)loadingRequest;
- (void)cancel;
@end

@protocol LSFilePlayerResourceLoaderDelegate <NSObject>
@optional
- (void)filePlayerResourceLoader:(LSFilePlayerResourceLoader *)resourceLoader didFailWithError:(NSError *)error;
- (void)filePlayerResourceLoader:(LSFilePlayerResourceLoader *)resourceLoader didLoadResource:(NSURL *)resourceURL;
@end
```

## डेटा लोडिंग: दो-चरणीय प्रक्रिया

जब एक लोडिंग अनुरोध कतार में प्रवेश करता है, तो दो ऑपरेशन क्रम में निष्पादित होते हैं:

- **contentInfoOperation** -- कंटेंट की लंबाई, MIME टाइप और बाइट-रेंज सपोर्ट की क्वेरी करता है
- **dataOperation** -- `requestedOffset` से शुरू होकर फ़ाइल डेटा लाता है

## डिस्क कैशिंग रणनीति

डाउनलोड किया गया डेटा डिस्क पर एक अस्थायी फ़ाइल में लिखा जाता है। उसी कंटेंट के लिए बाद के अनुरोध इस कैश से सर्व किए जाते हैं, जिससे अनावश्यक नेटवर्क कॉल से बचा जा सकता है। यह दृष्टिकोण:

- बैंडविड्थ उपयोग को कम करता है
- लगभग तत्काल रिप्ले सक्षम बनाता है
- कैश किए गए रेंज के भीतर सीक ऑपरेशन का समर्थन करता है

## लंबित अनुरोधों को प्रोसेस करना

`processPendingRequests` मेथड प्रत्येक अनुरोध के `contentInformationRequest` को मेटाडेटा से भरता है और कैश किए गए बाइट रेंज डिलीवर करता है। पूर्ण हुए अनुरोध कतार से हटा दिए जाते हैं।

## सोर्स कोड और अगले चरण

यह ट्यूटोरियल कस्टम ऑथराइज़ेशन हेडर के साथ क्लाउड ऑडियो स्ट्रीमिंग के लिए `AVAssetResourceLoaderDelegate` लागू करने का उच्च-स्तरीय अवलोकन प्रदान करता है। पूरा सोर्स कोड [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader) पर उपलब्ध है।

यह दृष्टिकोण [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) में ऑडियो स्ट्रीमिंग इंजन को शक्ति देता है, जो iOS और macOS पर Dropbox, Google Drive, OneDrive, Yandex.Disk और अन्य क्लाउड सेवाओं से संगीत स्ट्रीम करता है।

## अक्सर पूछे जाने वाले प्रश्न

{{% details title="सीधे URL की बजाय AVAssetResourceLoaderDelegate कब उपयोग करें?" closed="true" %}}
इसका उपयोग तब करें जब क्लाउड सेवा को कस्टम ऑथराइज़ेशन हेडर की आवश्यकता हो, जब आपको स्ट्रीम किए गए ऑडियो के लिए डिस्क कैशिंग चाहिए, या जब आप डेटा लोड और बफर होने के तरीके पर बारीक नियंत्रण चाहते हों।
{{% /details %}}

{{% details title="क्या यह दृष्टिकोण Swift के साथ काम करता है?" closed="true" %}}
हाँ। `AVAssetResourceLoaderDelegate` प्रोटोकॉल Swift में भी उसी तरह काम करता है। यहाँ दिए गए Objective-C उदाहरण सीधे अनुवादित होते हैं।
{{% /details %}}

{{% details title="क्या मैं इसे वीडियो स्ट्रीमिंग के लिए भी उपयोग कर सकता हूँ?" closed="true" %}}
हाँ। `AVAssetResourceLoaderDelegate` AVPlayer द्वारा समर्थित किसी भी मीडिया टाइप के साथ काम करता है, जिसमें वीडियो भी शामिल है। वही कस्टम-स्कीम दृष्टिकोण लागू होता है।
{{% /details %}}

{{% details title="क्या यह बैकग्राउंड ऑडियो प्लेबैक का समर्थन करता है?" closed="true" %}}
हाँ, जब तक आप अपने ऐप की क्षमताओं में "Audio, AirPlay, and Picture in Picture" बैकग्राउंड मोड सक्षम करते हैं और अपने `AVAudioSession` को सही तरीके से कॉन्फ़िगर करते हैं।
{{% /details %}}
