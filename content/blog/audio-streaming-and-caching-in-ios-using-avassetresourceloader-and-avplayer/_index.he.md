---
title: "סטרימינג אודיו ב-iOS עם AVAssetResourceLoader"
date: 2015-06-20
description: "למדו כיצד לסטרם ולשמור אודיו במטמון ב-iOS באמצעות AVAssetResourceLoaderDelegate ו-AVPlayer עם סכמות URL מותאמות אישית ומטמון על הדיסק."
keywords: ["סטרימינג אודיו iOS", "AVAssetResourceLoaderDelegate", "AVURLAsset", "מדריך AVPlayer", "אודיו AVFoundation", "AVAssetResourceLoadingRequest", "נגן אודיו מותאם iOS", "סטרימינג אודיו ענן iOS", "מטמון אודיו iOS", "Swift AVPlayer סכמה מותאמת"]
tags: ["streaming", "AVPlayer", "AVFoundation", "iOS", "AVAssetResourceLoader", "tutorial", "Objective-C", "audio caching"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

![](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/diagram.png)

**סיכום קצר:** השתמשו ב-`AVAssetResourceLoaderDelegate` עם סכמת URL מותאמת אישית כדי ליירט את טעינת המשאבים של AVPlayer. זה מאפשר לכם להוסיף כותרות הרשאה מותאמות לשירותי ענן, לשמור אודיו במטמון על הדיסק ולשלוט בהתנהגות הסטרימינג -- הכל ללא כתיבת פרוקסי HTTP מקומי. קוד המקור המלא זמין ב-[GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

---

## מדוע AVPlayer זקוק לטוען משאבים מותאם

`AVPlayer` מנגן אודיו מקבצים מקומיים ו-URL מרוחקות. עבור רוב שירותי הענן (Dropbox, Google Drive, Box), ניתן להעביר URL הורדה ישיר והניגון עובד מיד.

אולם, שירותים כגון **Yandex.Disk** ו-**WebDAV** דורשים כותרות הרשאה מותאמות בבקשות GET. `AVPlayer` אינו מספק דרך מובנית להזרקת כותרות אלה.

הפתרון: השתמשו במאפיין `resourceLoader` של `AVURLAsset`. ממשק API זה מיירט בקשות טעינת משאבים ופועל כפרוקסי HTTP מקומי ללא המורכבות.

### כיצד זה עובד

`AVPlayer` משתמש ב-`resourceLoader` כאשר הוא אינו מזהה את סכמת ה-URL. על ידי החלפת `https://` בסכמה מותאמת (למשל `customscheme://`), אתם מאלצים את AVPlayer להאציל את כל הטעינה לאפליקציה שלכם.

עליכם לממש שתי שיטות של `AVAssetResourceLoaderDelegate`:

1. **`resourceLoader:shouldWaitForLoadingOfRequestedResource:`** -- נקראת כאשר AVPlayer זקוק לנתונים. שמרו את ה-`AVAssetResourceLoadingRequest` והתחילו את פעולת טעינת הנתונים שלכם.
2. **`resourceLoader:didCancelLoadingRequest:`** -- נקראת כאשר בקשה מבוטלת או מוחלפת.

## כיצד ליצור AVPlayer מותאם אישית

הגדירו AVPlayer עם סכמת URL מותאמת אישית:

```objc
NSURL *url = [NSURL URLWithString:@"customscheme://host/audio.mp3"];
AVURLAsset *asset = [AVURLAsset URLAssetWithURL:url options:nil];
[asset.resourceLoader setDelegate:self queue:dispatch_get_main_queue()];
AVPlayerItem *item = [AVPlayerItem playerItemWithAsset:asset];
[self addObserversForPlayerItem:item];
self.player = [AVPlayer playerWithPlayerItem:item];
[self addObserversForPlayer];
```

קוד זה:
- מגדיר URL עם הסכמה המותאמת שלכם
- יוצר `AVURLAsset` עם דלגט בתור הראשי
- בונה `AVPlayerItem` מה-asset
- מאתחל את `AVPlayer`

## מימוש דלגט טוען המשאבים

צרו מחלקה בשם `LSFilePlayerResourceLoader` לטיפול בשליפת הנתונים מהשרת והעברתם ל-`AVURLAsset`. אחסנו מופעי טוען במילון שמפתחותיו הם URL המשאב.

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

שיטות אלה בודקות את סכמת ה-URL, יוצרות או מאחזרות טוען, ומוסיפות את הבקשה לתור הטוען. סכמות לא מזוהות מחזירות `NO`.

## ממשק LSFilePlayerResourceLoader

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

## טעינת נתונים: תהליך דו-שלבי

כאשר בקשת טעינה נכנסת לתור, שתי פעולות מתבצעות ברצף:

- **contentInfoOperation** -- מבצעת שאילתה על אורך התוכן, סוג MIME ותמיכה בטווחי בתים
- **dataOperation** -- שולפת נתוני קובץ החל מה-`requestedOffset`

## אסטרטגיית מטמון על הדיסק

הנתונים שהורדו נכתבים לקובץ זמני על הדיסק. בקשות עוקבות לאותו תוכן מוגשות מהמטמון, תוך הימנעות מקריאות רשת מיותרות. גישה זו:

- מצמצמת שימוש ברוחב פס
- מאפשרת ניגון חוזר כמעט מיידי
- תומכת בפעולות דילוג בתוך טווחים שנשמרו במטמון

## עיבוד בקשות ממתינות

המתודה `processPendingRequests` ממלאת את ה-`contentInformationRequest` של כל בקשה במטה-נתונים ומספקת טווחי בתים שנשמרו במטמון. בקשות שהושלמו מוסרות מהתור.

## קוד מקור וצעדים הבאים

מדריך זה מספק סקירה כללית של מימוש `AVAssetResourceLoaderDelegate` לסטרימינג אודיו בענן עם כותרות הרשאה מותאמות. קוד המקור המלא זמין ב-[GitHub](http://github.com/leshkoapps/AVAssetResourceLoader).

גישה זו מניעה את מנוע הסטרימינג של האודיו ב-[Evermusic](https://apps.apple.com/app/evermusic-offline-music-player/id885367198), המסטרים מוזיקה מ-Dropbox, Google Drive, OneDrive, Yandex.Disk ושירותי ענן נוספים ב-iOS וב-macOS.

## שאלות נפוצות

{{% details title="מתי להשתמש ב-AVAssetResourceLoaderDelegate במקום URL ישיר?" closed="true" %}}
השתמשו בו כאשר שירות הענן דורש כותרות הרשאה מותאמות, כאשר אתם זקוקים למטמון דיסק לאודיו שמסטרמים, או כאשר אתם רוצים שליטה מדויקת על אופן טעינת הנתונים ואחסונם בחוצץ.
{{% /details %}}

{{% details title="האם גישה זו עובדת עם Swift?" closed="true" %}}
כן. פרוטוקול `AVAssetResourceLoaderDelegate` עובד באותו אופן ב-Swift. דוגמאות Objective-C שכאן מתורגמות ישירות.
{{% /details %}}

{{% details title="האם ניתן להשתמש בזה גם לסטרימינג וידאו?" closed="true" %}}
כן. `AVAssetResourceLoaderDelegate` עובד עם כל סוג מדיה שנתמך על ידי AVPlayer, כולל וידאו. אותה גישה עם סכמה מותאמת חלה גם כאן.
{{% /details %}}

{{% details title="האם זה תומך בניגון אודיו ברקע?" closed="true" %}}
כן, כל עוד אתם מפעילים את מצב הרקע "Audio, AirPlay, and Picture in Picture" ביכולות האפליקציה ומגדירים את ה-`AVAudioSession` שלכם כראוי.
{{% /details %}}
