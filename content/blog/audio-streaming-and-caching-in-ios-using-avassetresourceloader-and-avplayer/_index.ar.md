---
title: "بث الصوت في iOS باستخدام AVAssetResourceLoader"
date: 2015-06-20
description: "تعرّف على كيفية بث الصوت وتخزينه مؤقتًا في iOS باستخدام AVAssetResourceLoaderDelegate وAVPlayer مع مخططات URL مخصصة والتخزين المؤقت على القرص."
keywords: ["بث الصوت في iOS", "AVAssetResourceLoaderDelegate", "AVURLAsset", "شرح AVPlayer", "AVFoundation صوت", "AVAssetResourceLoadingRequest", "مشغل صوت مخصص iOS", "بث الصوت السحابي iOS", "تخزين الصوت مؤقتًا iOS", "Swift AVPlayer مخطط مخصص"]
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

**ملخص سريع:** استخدم `AVAssetResourceLoaderDelegate` مع مخطط URL مخصص لاعتراض تحميل الموارد في AVPlayer. يتيح لك هذا إضافة رؤوس تفويض مخصصة لخدمات السحابة، وتخزين الصوت مؤقتًا على القرص، والتحكم في سلوك البث -- وكل ذلك دون الحاجة إلى كتابة وكيل HTTP محلي. الكود المصدري الكامل متاح على [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## لماذا يحتاج AVPlayer إلى محمّل موارد مخصص

يشغّل `AVPlayer` الصوت من الملفات المحلية وعناوين URL البعيدة. بالنسبة لمعظم الخدمات السحابية (Dropbox وGoogle Drive وBox)، يمكنك تمرير رابط تنزيل مباشر وستعمل إمكانية التشغيل فورًا.

غير أن بعض الخدمات مثل **Yandex.Disk** و**WebDAV** تتطلب رؤوس تفويض مخصصة في طلبات GET. لا يوفر `AVPlayer` أي طريقة مدمجة لحقن هذه الرؤوس.

الحل: استخدم خاصية `resourceLoader` في `AVURLAsset`. تعترض هذه الواجهة البرمجية طلبات تحميل الموارد، وتعمل كوكيل HTTP محلي دون التعقيد المعتاد.

### كيف يعمل

يستخدم `AVPlayer` خاصية `resourceLoader` عندما لا يتعرف على مخطط URL. باستبدال `https://` بمخطط مخصص (مثل `customscheme://`)، تجبر AVPlayer على تفويض جميع عمليات التحميل إلى تطبيقك.

تحتاج إلى تطبيق طريقتين من `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- تُستدعى عندما يحتاج AVPlayer إلى بيانات. احفظ `AVAssetResourceLoadingRequest` وابدأ عملية تحميل البيانات الخاصة بك.
2. **`resourceLoader:didCancelLoadingRequest:`** -- تُستدعى عند إلغاء طلب أو استبداله.

## كيفية إنشاء AVPlayer مخصص

أنشئ AVPlayer بمخطط URL مخصص:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

هذا الكود:
- يعرّف URL بمخططك المخصص
- ينشئ `AVURLAsset` مع مفوَّض على قائمة الانتظار الرئيسية
- يبني `AVPlayerItem` من الأصل
- يهيئ `AVPlayer`

## تطبيق مفوَّض محمّل الموارد

أنشئ فئة تسمى `LSFilePlayerResourceLoader` للتعامل مع جلب البيانات من الخادم وإعادتها إلى `AVURLAsset`. خزّن نسخ المحمّل في قاموس مفهرس بعنوان URL للمورد.

```objc
- (BOOL)resourceLoader:(AVAssetResourceLoader *)resourceLoader shouldWaitForLoadingOfRequestedResource:(AVAssetResourceLoadingRequest *)loadingRequest {
    NSURL *resourceURL = [loadingRequest.request URL];
    if ([resourceURL.scheme isEqualToString:@"customscheme"]) {
        LSFilePlayerResourceLoader *loader = 
        [self resourceLoaderForRequest:loadingRequest];
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

تتحقق هذه الطرق من مخطط URL، وتنشئ محمّلًا أو تسترجعه، وتضيف الطلب إلى قائمة انتظار المحمّل. تُعيد المخططات غير المعروفة `NO`.

## واجهة LSFilePlayerResourceLoader

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

## تحميل البيانات: عملية من خطوتين

عند دخول طلب تحميل إلى قائمة الانتظار، تُنفَّذ عمليتان بالتسلسل:

- **contentInfoOperation** -- تستعلم عن طول المحتوى ونوع MIME ودعم النطاق البايتي
- **dataOperation** -- تجلب بيانات الملف بدءًا من `requestedOffset`

## استراتيجية التخزين المؤقت على القرص

تُكتب البيانات المنزّلة إلى ملف مؤقت على القرص. تُخدَّم الطلبات اللاحقة لنفس المحتوى من هذه الذاكرة المؤقتة، مما يتجنب استدعاءات الشبكة الزائدة. يوفر هذا النهج:

- تقليل استهلاك النطاق الترددي
- إعادة تشغيل شبه فوري
- دعم عمليات البحث ضمن النطاقات المخزنة مؤقتًا

## معالجة الطلبات المعلّقة

تملأ طريقة `processPendingRequests` خاصية `contentInformationRequest` لكل طلب بالبيانات الوصفية وتسلّم نطاقات البايتات المخزنة مؤقتًا. تُحذف الطلبات المكتملة من قائمة الانتظار.

## الكود المصدري والخطوات التالية

يقدم هذا الشرح نظرة عامة عالية المستوى لتطبيق `AVAssetResourceLoaderDelegate` لبث الصوت السحابي مع رؤوس تفويض مخصصة. الكود المصدري الكامل متاح على [GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

يشغّل هذا النهج محرك بث الصوت في [Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198)، الذي يبث الموسيقى من Dropbox وGoogle Drive وOneDrive وYandex.Disk وخدمات سحابية أخرى على iOS وmacOS.

## الأسئلة الشائعة

{{% details title="متى يجب استخدام AVAssetResourceLoaderDelegate بدلًا من URL مباشر؟" closed="true" %}}
استخدمه عندما تتطلب الخدمة السحابية رؤوس تفويض مخصصة، أو عندما تحتاج إلى تخزين الصوت المبثوث مؤقتًا على القرص، أو عندما تريد تحكمًا دقيقًا في كيفية تحميل البيانات وتخزينها في المخزن المؤقت.
{{% /details %}}

{{% details title="هل يعمل هذا النهج مع Swift؟" closed="true" %}}
نعم. يعمل بروتوكول `AVAssetResourceLoaderDelegate` بنفس الطريقة في Swift. الأمثلة المكتوبة بـ Objective-C هنا تترجم مباشرةً.
{{% /details %}}

{{% details title="هل يمكن استخدام هذا لبث الفيديو أيضًا؟" closed="true" %}}
نعم. يعمل `AVAssetResourceLoaderDelegate` مع أي نوع وسائط يدعمه AVPlayer، بما في ذلك الفيديو. ينطبق نفس نهج المخطط المخصص.
{{% /details %}}

{{% details title="هل يدعم هذا تشغيل الصوت في الخلفية؟" closed="true" %}}
نعم، طالما تفعّل وضع الخلفية "Audio, AirPlay, and Picture in Picture" في إمكانيات تطبيقك وتضبط `AVAudioSession` بشكل صحيح.
{{% /details %}}
