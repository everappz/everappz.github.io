---
title: "تصدير سجل الاستماع الكامل من Evermusic و Flacbox إلى Last.fm"
date: 2024-01-30
description: "تعرف على كيفية تصدير سجل الموسيقى من Evermusic و Flacbox ورفعه إلى Last.fm باستخدام ملفات CSV وأداة Last.fm Scrubbler على Windows."
keywords: ["evermusic", "flacbox", "lastfm", "سجل الموسيقى", "سكروبلينغ", "تصدير المسارات", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "الأخيرة", "lastfm", "تصدير", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**ملخص سريع:** قم بتصدير سجل الاستماع من Evermusic أو Flacbox كملف CSV، ثم ارفعه إلى Last.fm باستخدام أداة Last.fm-Scrubbler-WPF المجانية على Windows. يتوفر أيضًا السكروبلينغ التلقائي بشكل أصلي في كلا التطبيقين.

**تحديث:** السكروبلينغ التلقائي متاح الآن! تعرف على المزيد هنا: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

السكروبلينغ هو طريقة بسيطة لحفظ التفاصيل الأساسية تلقائيًا مثل عنوان الأغنية واسم الفنان للأغنية التي تستمع إليها حاليًا في خدمة عبر الإنترنت. لاحقًا، يمكنك مراجعة سجل الاستماع الخاص بك.

[Last.fm](https://www.last.fm/home)، المدعوم بنظام توصيات موسيقية يسمى Audioscrobbler، يقدم هذه الخدمة مجانًا. يقوم بإنشاء ملف تعريف مفصل لذوقك الموسيقي من خلال تسجيل المسارات التي تستمع إليها، سواء من محطات الراديو عبر الإنترنت أو جهاز الكمبيوتر الخاص بك أو أجهزة الموسيقى المحمولة المختلفة. يمكنك زيارة الموقع لاحقًا للحصول على توصيات لفنانين أو ألبومات جديدة تتناسب مع ذوقك الموسيقي.

يمكنك رفع سجل الاستماع إلى [Last.fm](http://Last.fm) من تطبيقات Evermusic و Flacbox باستخدام أداة مجانية، وسنرشدك خلال كيفية القيام بذلك.

افتح قسم 'مكتبة الموسيقى' في التطبيق وانتقل إلى قسم 'الوصول السريع'. اضغط على عنصر القائمة 'الأخيرة'.

![شاشة مكتبة الموسيقى](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

في شاشة 'الأخيرة' اضغط على زر 'المزيد' في الزاوية العلوية اليمنى لتفعيل قائمة 'المزيد من الإجراءات'. اضغط على عنصر القائمة 'تصدير قائمة الأغاني'.

![شاشة الأخيرة](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

في شاشة 'اختيار تنسيق الملف' لديك إمكانية اختيار تنسيق الملف الناتج. الخيارات المتاحة - CSV، TXT، M3U.

![شاشة اختيار تنسيق الملف](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: يرمز إلى القيم المفصولة بفواصل، وهو مثالي لتنظيم بياناتك في تنسيق جدول منظم. في الملف الناتج، ستجد معلمات مثل اسم الفنان واسم الألبوم واسم المسار والطابع الزمني (وقت استماعك للمسارات) واسم فنان الألبوم ومدة المسار.

TXT: هنا نتحدث عن ملف نصي عادي. إنه بسيط ومباشر، مع معلمات تشمل اسم الفنان واسم الألبوم واسم المسار والمدة.

M3U: هذا التنسيق هو الأساس لإنشاء قوائم التشغيل. إنه رائع لأنه يمكنك تصدير قائمة أغانيك والاستمتاع بمساراتك على أي جهاز، حتى لو لم تكن لديك الملفات الأصلية (بشرط أن تختار خيار عنوان URL المطلق لملفات الوسائط). في الملف الناتج، ستجد معلمات مثل المدة واسم الفنان واسم المسار وموقع ملف الوسائط.

لمهمتنا، اختيار CSV هو الطريقة الصحيحة. سنستخدم هذا الملف مع البرنامج المجاني Last.fm-Scrubbler-WPF لرفع سجل الاستماع إلى خدمة [Last.fm](http://Last.fm). ما عليك سوى اختيار CSV والضغط على زر 'تصدير'.

![شاشة اكتمال التصدير](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

بعد اكتمال التصدير، ما عليك سوى الضغط على زر 'عرض الملف'، وسيكشف التطبيق عن الملف الذي تم إنشاؤه في مجلد المستندات. ثم اضغط على زر 'المزيد من الإجراءات' بجانب اسم الملف واختر خيار 'فتح في' من القائمة. خطوتنا التالية هي نسخ الملف المصدّر إلى جهاز الكمبيوتر المكتبي. يمكنك القيام بذلك بسهولة عن طريق اختيار خيار AirDrop من قائمة 'فتح في'.

![المزيد من الإجراءات للملف المصدّر](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

بعد ذلك، سنستخدم عميل [Last.FM](http://Last.FM) مجاني ومفتوح المصدر وهو متاح على منصة Windows فقط. يتيح لك هذا العميل تحديث سجل الاستماع بكفاءة على [Last.FM](http://Last.FM) باستخدام ملف CSV الذي صدّرناه للتو.

الآن، إذا كنت لا تستخدم حاليًا جهاز كمبيوتر يعمل بنظام Windows، فلا تقلق. يمكنك الوصول إلى هذا العميل عن طريق تثبيت VirtualBox على جهاز Mac واستخدام ملف صورة بيئة تطوير Windows الرسمية.

إليك ما تحتاج إلى القيام به:

- قم بتثبيت VirtualBox من الرابط التالي: [تحميل VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- قم بتنزيل وتثبيت بيئة تطوير Windows من هذا الرابط: [بيئة تطوير Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

على جهاز الكمبيوتر الذي يعمل بنظام Windows (أو تطبيق VirtualBox مع صورة تطوير Windows) قم بتنزيل وتثبيت [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - برنامج مجاني ومفتوح المصدر متاح على GitHub. قمنا بالاختبار على الإصدار 1.28 الذي يمكنك تنزيله من هنا: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![صفحة تنزيل Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

ضمن قسم 'الأصول' اضغط على [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) لتنزيل أرشيف التثبيت. قم بفك ضغط الملف المحمّل وافتح المجلد الذي تم فك ضغطه.

- مهم

هذا التطبيق لا يزال في مرحلة تجريبية. لم يقم مطورو التطبيق بإجراء الكثير من الاختبارات. يوصون بمحاولة السكروبلينغ إلى حساب تجريبي أولاً والتحقق مما إذا كانت الأشياء التي تريد سكروبلينغها تعمل بشكل صحيح. خاصة إذا كنت تقوم بسكروبلينغ الكثير من المسارات دفعة واحدة. يرجى توخي الحذر مع حساباتك.

شغّل Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

في الشاشة الرئيسية للتطبيق، ما عليك سوى الضغط على 'غير مسجل الدخول'، الموجود في الزاوية السفلية اليسرى، لتفعيل شاشة 'إضافة حساب'.

![شاشة إضافة حساب](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

أدخل بيانات تسجيل الدخول الخاصة بك.

![شاشة إدخال بيانات تسجيل الدخول](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

اضغط على زر 'تسجيل الدخول' لإضافة حسابك.

![اضغط على زر تسجيل الدخول لإضافة حسابك.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

افتح علامة تبويب 'File Parse Scrobbler' لبدء استيراد ملف CSV من تطبيق Evermusic.

![افتح علامة تبويب File Parse Scrobbler لبدء استيراد ملف CSV من تطبيق Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

اختر 'Parser: CSV' واضغط على زر 'الإعدادات'.

في الشاشة التالية، يمكنك اختيار ترتيب المعلمات في ملف CSV الخاص بك.

يمكن أن تكون الحقول الفردية محاطة بعلامات اقتباس ويجب أن تكون محاطة بعلامات اقتباس إذا كان الحقل يحتوي على أي من المحددات المعيّنة. على سبيل المثال:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

لذا اترك جميع الإعدادات كما هي، الشيء الوحيد الذي تحتاج إلى تغييره هو تفعيل مربع الاختيار في حقل 'Has Fields Enclosed In Quotes'.

اضغط 'حفظ وإغلاق' لتطبيق التغييرات.

![اختيار ترتيب المعلمات في ملف CSV الخاص بك.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

يحتوي سكروبلينغ تحليل الملفات على وضعين. يمكن تغييرهما باستخدام مربع القائمة المنسدلة 'Scrobbling Mode'.

الوضع العادي: في هذا الوضع، سيتم سكروبلينغ المسارات بالطابع الزمني من السكروبل المحلل. يمكن فقط سكروبلينغ السكروبلات الأحدث من 14 يومًا.

وضع الاستيراد: في هذا الوضع، سيتم سكروبلينغ المسارات بالطابع الزمني المحسوب من 'وقت الانتهاء' والمدة المحددة بين كل مسار. هذا يسمح بسكروبلينغ المسارات حتى لو كان الطابع الزمني للسكروبل المحلل أقدم من 14 يومًا. لذلك سيتم سكروبلينغ المسار الأول (الأعلى) في ملف CSV بـ 'وقت الانتهاء'.

اختر ملف CSV الذي تم إنشاؤه مسبقًا من تطبيق Evermusic في حقل 'File:' واضغط 'Parse'. في بعض الحالات، قد ترى تنبيه خطأ يقول إن بعض السكروبلات لا يمكن تحليلها. لا بأس إذا كان لديك بعض المسارات بدون بيانات وصفية كاملة مثل اسم الفنان.

![لا يمكن تحليل بعض السكروبلات](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

اضغط على زر 'تحديد الكل' لتحديد جميع المسارات المحللة.

![اضغط على زر تحديد الكل لتحديد جميع المسارات المحللة.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

اضغط على زر 'معاينة' للتحقق من جميع التغييرات التي سيتم نشرها على الخادم.

![اضغط على زر معاينة للتحقق من جميع التغييرات التي سيتم نشرها على الخادم.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

اضغط على زر 'سكروبل' لرفع جميع التغييرات إلى الخادم.

![اضغط على زر سكروبل لرفع جميع التغييرات إلى الخادم.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

سابقًا لم يكن لدى Last.fm-Scrubbler-WPF حد يومي للسكروبلات. لقد تغير هذا الآن لأن بعض الأشخاص استخدموا Scrubbler لسكروبلينغ الكثير من المسارات، مما تسبب في مشاكل لصفحة Last.fm. حد السكروبلينغ حاليًا هو 2800 سكروبل في اليوم. عندما تحاول سكروبلينغ أكثر من ذلك ستحصل على رسالة خطأ. هناك خطط لإضافة 'قائمة انتظار السكروبلينغ'، لذا إذا كنت بحاجة إلى سكروبلينغ أكثر من 2800 مسار، فسيتم إضافتها إلى قائمة انتظار وسيتم سكروبلينغها تلقائيًا بعد بعض الوقت. يمكنك التحقق من عدد السكروبلات المتبقية لديك في عرض اختيار المستخدم.

بمجرد رفع جميع السجلات بنجاح إلى الخادم، سترى رسالة في أسفل نافذة التطبيق تؤكد: 'تم سكروبلينغ المسارات المحددة بنجاح.'

![تم سكروبلينغ المسارات المحددة بنجاح.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

الآن يمكنك فتح ملفك الشخصي على صفحة [Last.fm](http://Last.fm) والتحقق من جميع التغييرات.

![ملفك الشخصي على صفحة Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## الأسئلة الشائعة

{{% details title="هل يمكنني السكروبلينغ تلقائيًا بدون تصدير ملفات CSV؟" closed="true" %}}
نعم. يدعم كل من Evermusic و Flacbox الآن السكروبلينغ التلقائي إلى Last.fm. راجع الدليل: [كيفية السكروبلينغ إلى Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="ماذا لو كان ملف CSV يحتوي على مسارات أقدم من 14 يومًا؟" closed="true" %}}
استخدم وضع الاستيراد في Last.fm-Scrubbler-WPF. يقوم بإعادة حساب الطوابع الزمنية من وقت الانتهاء، مما يسمح لك بسكروبلينغ المسارات بغض النظر عن تاريخها الأصلي.
{{% /details %}}

{{% details title="لا أملك جهاز كمبيوتر يعمل بنظام Windows. هل يمكنني استخدام Last.fm-Scrubbler؟" closed="true" %}}
نعم. قم بتثبيت VirtualBox على جهاز Mac وتنزيل صورة بيئة تطوير Windows المجانية من Microsoft. شغّل Last.fm-Scrubbler-WPF داخل الجهاز الافتراضي.
{{% /details %}}

{{% details title="لماذا لا يتم تحليل بعض السكروبلات؟" closed="true" %}}
لا يمكن تحليل المسارات التي تفتقر إلى البيانات الوصفية الأساسية (مثل اسم الفنان). هذا متوقع ولا يؤثر على المسارات الأخرى في الملف.
{{% /details %}}

{{% details title="هل هناك حد يومي للسكروبلينغ؟" closed="true" %}}
نعم. يسمح Last.fm-Scrubbler-WPF بما يصل إلى 2800 سكروبل في اليوم. إذا كنت بحاجة إلى سكروبلينغ المزيد، قسّم العملية على عدة أيام.
{{% /details %}}
