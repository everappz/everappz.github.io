---
title: "كيفية توصيل تخزين NAS باستخدام WebDAV والاستماع إلى الموسيقى على iPhone أو Mac"
date: 2024-07-28
description: "تعرّف على كيفية تكوين WebDAV على Synology NAS وبث الموسيقى إلى iPhone أو Mac باستخدام Evermusic أو Flacbox. اتبع دليلنا خطوة بخطوة."
keywords: ["توصيل nas", "webdav synology", "بث الموسيقى nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["موسيقى", "بث", "تخزين", "nas", "توصيل", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**ملخص:** قم بتثبيت وتفعيل WebDAV على Synology NAS، وتكوين أذونات المجلد المشترك، ثم الاتصال من Evermusic أو Flacbox باستخدام عنوان IP الخاص بـ NAS ومنفذ WebDAV (الافتراضي 5005/5006). يمكنك بث وإدارة مكتبة الموسيقى بالكامل دون نسخ الملفات إلى جهازك.

اكتشف كيفية توصيل تخزين NAS الخاص بك باستخدام WebDAV وبث مكتبة الموسيقى بسهولة إلى iPhone أو Mac. WebDAV (التأليف والإصدار الموزع عبر الويب) هو بروتوكول يتيح لك إدارة ومشاركة الملفات عبر الإنترنت. من خلال إعداد WebDAV على NAS الخاص بك، يمكنك الوصول إلى مجموعة الموسيقى وبثها، مما يضمن أن تكون أغانيك المفضلة في متناول يدك دائمًا.

في هذا الدليل، سنوضح لك كيفية إعداد اتصال WebDAV على أحد أكثر خوادم NAS شيوعًا، Synology NAS. اتبع خطواتنا البسيطة لتكوين WebDAV على Synology NAS الخاص بك، وستتمكن من تصفح وبث وإدارة مكتبة الموسيقى مباشرة من iPhone أو Mac.

## الخطوة 1: تثبيت WebDAV على Synology NAS

1. قم بتسجيل الدخول إلى Synology NAS وافتح **مركز الحزم**.
2. ابحث عن "webdav" وقم بتثبيت حزمة WebDAV إذا لم تكن مثبتة بالفعل. افتح خادم WebDAV لتكوينه.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="تثبيت WebDAV على Synology" width="600" >}}

## الخطوة 2: تكوين خادم WebDAV

1. في صفحة إعدادات WebDAV، حدد مربعات **تفعيل HTTP** و**تفعيل HTTPS** و**تفعيل WebDAV المجهول** و**تفعيل DavDepthInfinity**.
2. انقر على **تطبيق** لحفظ التغييرات. لاحظ أرقام المنافذ لاتصالات HTTP وHTTPS، وهي 5005 و5006 بشكل افتراضي.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="تكوين إعدادات WebDAV" width="600" >}}

## الخطوة 3: تكوين أذونات المجلد المشترك

1. افتح **لوحة التحكم** وانتقل إلى قسم **المجلد المشترك**.
2. حدد مجلد **الموسيقى** وانقر على **تعديل**.
3. في علامة تبويب **الأذونات**، قم بتكوين الأذونات. قم بتفعيل وصول الضيف مع القراءة فقط إذا كنت تحتاج فقط للاستماع إلى الموسيقى، أو القراءة/الكتابة إذا كنت تحتاج لتعديل الملفات. احفظ التغييرات.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="أذونات المجلد المشترك" width="600" >}}

## الخطوة 4: العثور على عنوان IP لـ Synology NAS

1. افتح **لوحة التحكم** وانتقل إلى علامة تبويب **واجهة الشبكة**، أو استخدم متصفح الويب لزيارة [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="العثور على عنوان IP لـ NAS" width="600" >}}

2. لاحظ عنوان IP الخاص بـ Synology NAS (مثال: 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="عنوان IP لـ Synology NAS" width="600" >}}

## الخطوة 5: الاتصال بـ Synology NAS باستخدام Evermusic/Flacbox

1. افتح تطبيق Evermusic أو Flacbox وانتقل إلى علامة تبويب **الاتصالات**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="علامة تبويب الاتصالات في Evermusic" width="600" >}}

2. للاتصال التلقائي، ابحث عن Synology NAS في قسم **الأجهزة المتاحة** واضغط عليه للاتصال.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="قائمة الأجهزة المتاحة" width="600" >}}

3. للاتصال اليدوي، اختر **الاتصال بخدمة سحابية** وحدد **WebDAV**. أدخل عنوان الخادم بالصيغة: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (مثال: [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="تكوين WebDAV يدوياً" width="600" >}}

4. اترك حقول اسم المستخدم وكلمة المرور فارغة لوصول الضيف، أو أدخل بيانات اعتماد Synology الخاصة بك. اضغط على **تسجيل الدخول**.

## الخطوة 6: التنقل وتشغيل الموسيقى

1. بمجرد الاتصال، سيظهر الجهاز في قائمة **الإكسسوارات المتصلة**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="الأجهزة المتصلة في Evermusic" width="600" >}}

2. انتقل إلى مجلد **الموسيقى** واضغط على أي ملف صوتي لبدء التشغيل.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="تصفح مجلد الموسيقى" width="600" >}}

## الخطوة 7: إضافة مجلد السحابة المتصل إلى مكتبة الموسيقى

1. افتح قسم **مكتبة الموسيقى** في التطبيق.
2. اختر **إضافة موسيقى** وحدد **الاتصالات**.
3. اختر خادم NAS المتصل وحدد مجلد **الموسيقى**. اضغط على **تم**.
4. سيقوم التطبيق بمسح مجلد الموسيقى وإضافة ملفات الصوت المدعومة إلى مكتبة الموسيقى. سيتم تحميل البيانات الوصفية، وسيتم تجميع مساراتك حسب الألبوم والفنان والنوع.

## الخلاصة

باتباع هذه الخطوات، يمكنك بسهولة إعداد اتصال WebDAV على Synology NAS وبث مكتبة الموسيقى إلى iPhone أو Mac باستخدام Evermusic أو Flacbox. استمتع بالوصول السلس إلى أغانيك المفضلة في أي وقت.

## الأسئلة الشائعة

{{% details title="ما هي أجهزة NAS التي تدعم WebDAV؟" closed="true" %}}
تدعم معظم علامات NAS الشائعة WebDAV، بما في ذلك Synology وQNAP وTrueNAS وWestern Digital. تحقق من وثائق الشركة المصنعة لـ NAS للحصول على تعليمات إعداد WebDAV.
{{% /details %}}

{{% details title="ما الفرق بين WebDAV وSMB لبث الموسيقى من NAS؟" closed="true" %}}
يعمل WebDAV عبر HTTP/HTTPS وهو أكثر ملاءمة للوصول عن بُعد عبر الإنترنت. عادةً ما يكون SMB أسرع على الشبكات المحلية. يدعم كل من Evermusic وFlacbox كلا البروتوكولين، لذا اختر بناءً على ما إذا كنت تحتاج إلى وصول محلي أو عن بُعد.
{{% /details %}}

{{% details title="هل أحتاج إلى اسم مستخدم وكلمة مرور لـ WebDAV على Synology؟" closed="true" %}}
لا، إذا قمت بتفعيل وصول WebDAV المجهول وتكوين أذونات الضيف على المجلد المشترك. لمزيد من الأمان، يمكنك استخدام بيانات اعتماد Synology بدلاً من ذلك.
{{% /details %}}

{{% details title="هل يمكنني بث FLAC وتنسيقات عالية الدقة الأخرى من NAS عبر WebDAV؟" closed="true" %}}
نعم. يدعم كل من Evermusic وFlacbox تنسيقات FLAC وALAC وWAV وDSD وغيرها من التنسيقات عالية الدقة عند البث من تخزين NAS عبر WebDAV.
{{% /details %}}

{{% details title="لماذا لا يمكن للتطبيق العثور على NAS في الأجهزة المتاحة؟" closed="true" %}}
تأكد من أن iPhone/Mac وNAS على نفس شبكة Wi-Fi. إذا لم يعمل الاكتشاف التلقائي، استخدم خيار الاتصال اليدوي وأدخل عنوان IP لـ NAS ومنفذ WebDAV مباشرة.
{{% /details %}}
