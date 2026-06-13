---
title: "كيفية الحصول على بيانات وأيقونات ولقطات شاشة تطبيقات App Store مجاناً"
date: 2026-06-13
description: "دليل خطوة بخطوة للحصول على البيانات الوصفية والأيقونة ولقطات الشاشة وتفاصيل App Store المحلية لأي تطبيق iOS باستخدام AppLookup.pro، أداة مجانية تعمل في المتصفح وتعتمد على واجهة iTunes Search API الرسمية."
keywords: [
  "بيانات app store", "جلب بيانات app store", "تنزيل أيقونة app store",
  "تنزيل لقطات شاشة app store", "أداة بحث app store", "itunes search api",
  "مستخرج بيانات التطبيق", "بيانات تطبيقات iOS", "أداة مجانية app store api",
  "تنزيل أيقونة تطبيق بدقة عالية", "بحث المنافسين app store",
  "بيانات app store المحلية", "بحث app store حسب الدولة", "أداة مجانية لبحث aso"
]
tags: [
  "بيانات App Store", "بحث التطبيقات", "iTunes Search API",
  "تنزيل أيقونة التطبيق", "لقطات شاشة التطبيق", "بحث ASO"
]
sidebar:
  exclude: true
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## احصل على بيانات App Store في ثوانٍ

**باختصار:** [AppLookup.pro](https://applookup.pro) أداة مجانية تستخرج البيانات العامة لأي تطبيق iOS أو iPadOS أو macOS أو tvOS. تحصل على العنوان، الوصف، ما الجديد، الإصدار، السعر، التقييمات، أيقونة التطبيق، لقطات الشاشة، الأجهزة المدعومة، واستجابة iTunes API الخام. كل حقل به زر نسخ بنقرة واحدة. افتح الموقع، الصق رابط App Store أو اكتب اسم التطبيق، وتحصل على البيانات.

استخدمها لـ:

- **بحث ASO.** اطّلع على كيفية كتابة كبار التطبيقات لعناوينها وعناوينها الفرعية وأوصافها وكلماتها المفتاحية.
- **متابعة المنافسين.** تحقق من تحديثات الإصدار والتقييمات والأسعار عبر الأسواق.
- **تنزيل الأصول.** احفظ أيقونة التطبيق الرسمية ولقطات الشاشة بالحجم الكامل في ملف ZIP واحد.
- **فحوصات التوطين.** قارن الوصف وما الجديد ولقطات الشاشة عبر أكثر من 40 دولة من دول App Store.
- **اختبار API.** انسخ استجابة JSON الخام لـ iTunes Search API مباشرة إلى الكود الخاص بك أو إلى Postman.

## ما هو AppLookup.pro؟

[AppLookup.pro](https://applookup.pro) أداة مجانية لبحث App Store تعمل في المتصفح. تعمل بالكامل على جهازك. كل نتيجة تأتي مباشرة من واجهة [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) الرسمية من Apple. بدون scraping. بدون تسجيل. بدون تتبع.

### ما الذي تحصل عليه

- **بحث باسم التطبيق أو رابط App Store.** يعرض الإكمال التلقائي نتائج حية أثناء الكتابة.
- **أكثر من 40 متجر دولة.** بدّل بين الولايات المتحدة والمملكة المتحدة واليابان وألمانيا وفرنسا والبرازيل والمزيد.
- **بيانات وصفية كاملة.** العنوان، العنوان الفرعي، المطور، bundle ID، الإصدار، السعر، حجم الملف، التقييمات، تاريخ الإصدار، تصنيف المحتوى، اللغات والأجهزة المدعومة.
- **أصول عالية الدقة.** أيقونات التطبيقات ولقطات الشاشة لـ iPhone وiPad وmacOS وApple TV.
- **تنزيل ZIP مجمّع.** احصل على كل أيقونة أو كل لقطة شاشة في أرشيف واحد.
- **JSON خام من iTunes API.** الاستجابة الدقيقة من Apple، جاهزة للنسخ.
- **أزرار نسخ على كل حقل.** نقرة واحدة تضع القيمة في حافظتك.

## كيفية استخدام AppLookup.pro خطوة بخطوة

### الخطوة 1. أدخل اسم التطبيق أو الصق رابط App Store

افتح [applookup.pro](https://applookup.pro) وابدأ بكتابة اسم التطبيق. يعرض الإكمال التلقائي نتائج App Store حية أثناء الكتابة.

يمكنك أيضاً لصق رابط App Store مباشر مثل `https://apps.apple.com/us/app/instagram/id389801252` أو فقط معرف التطبيق. تستخرج الأداة المعرف نيابة عنك. كما تدعم روابط إعادة توجيه Google.

![أدخل اسم التطبيق أو رابط App Store في AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### الخطوة 2. اجلب معلومات التطبيق ونزّل الأيقونة

انقر على **Lookup** أو اضغط Enter. تستدعي الأداة واجهة iTunes Search API الرسمية وتعرض أيقونة التطبيق واسم المطور والتقييم والإصدار والسعر في أقل من ثانية.

مرّر إلى قسم **App Icon**. كل حجم أيقونة تعيده Apple يظهر كبطاقة. كل بطاقة بها:

- **Direct Link.** يفتح الصورة بالحجم الكامل في علامة تبويب جديدة.
- **Download.** يحفظ الملف على جهاز الكمبيوتر.

استخدم **Download All Icons (ZIP)** للحصول على كل حجم أيقونة في أرشيف واحد. الأمر نفسه ينطبق على لقطات الشاشة: كل قسم منصة له زر **Download All (ZIP)** الخاص به.

![نزّل أيقونات التطبيق ولقطات الشاشة من AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### الخطوة 3. اقرأ تفاصيل التطبيق وانسخ أي حقل

مرّر إلى **App Details**. سترى bundle ID، الإصدار، السعر، حجم الملف، الحد الأدنى لنظام التشغيل، تاريخ الإصدار، تاريخ آخر تحديث، تصنيف المحتوى، الأنواع، معرفات الأنواع، اللغات، البائع، معرف الفنان ومعرف المسار.

اضغط على زر **Copy** في أي بطاقة. تذهب القيمة إلى الحافظة ويعرض الزر علامة خضراء 'Copied'.

الأمر نفسه يعمل لأقسام **Description** و**What's New** و**Supported Devices**. هذه الأقسام قابلة للتمرير حتى تتمكن من قراءة النص الكامل دون فقدان مكانك، ويضع زر Copy الحقل بأكمله في الحافظة.

![اعرض تفاصيل App Store الكاملة وانسخ أي حقل بنقرة واحدة](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### الخطوة 4. اعرض استجابة App Store API الخام

هل تحتاج إلى JSON الدقيق الذي تعيده Apple؟ مرّر إلى **Raw API Response**. يتم عرض حمولة iTunes Search API الكاملة في عارض قابل للتمرير مع زر **Copy** في الأعلى. نقرة واحدة تنسخ كائن JSON بأكمله.

يتم عرض **iTunes Lookup URL** أعلاه مباشرة. الصقه في Postman أو curl أو متصفحك لتكرار الطلب نفسه.

![اعرض وانسخ استجابة JSON الخام لـ iTunes Search API](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### الخطوة 5. غيّر الدولة لرؤية النسخة المحلية

تتغير بيانات App Store حسب الدولة. غالباً ما يكون للتطبيق نفسه عنوان وعنوان فرعي ووصف ولقطات شاشة وسعر مختلفة في كل سوق.

اختر دولة من القائمة المنسدلة في الأعلى. يتم تحديث الرابط في مربع الإدخال تلقائياً. انقر على **Lookup** مرة أخرى لإعادة جلب التطبيق في ذلك السوق.

هذه أسرع طريقة للتحقق من كيفية تقديم منافس لتطبيقه في اليابان أو ألمانيا أو البرازيل أو أي من الدول الأكثر من 40 المدعومة.

![بدّل متاجر الدولة لرؤية بيانات App Store المحلية](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### الخطوة 6. انسخ البيانات المحلية

بمجرد تحميل نتيجة الدولة، يعمل كل حقل بالطريقة نفسها. اضغط **Copy** على الوصف أو ما الجديد أو اسم التطبيق أو المطور أو bundle ID أو أي بطاقة تفاصيل لالتقاط النص المحلي.

هذا يجعل من السهل إنشاء جداول بيانات للمقارنة جنباً إلى جنب أو إدخال نسخ محلية في مراجعة الترجمة.

![انسخ وصف وبيانات App Store المحلية بنقرة واحدة](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## من يستخدم AppLookup.pro

- **المطورون المستقلون** الذين يقومون ببحث ASO قبل الإطلاق.
- **فرق ASO والتسويق** التي تتابع تحديثات المنافسين والأسعار.
- **المصممون** الذين يلتقطون أيقونة التطبيق الرسمية عالية الدقة ولقطات الشاشة للمواد الصحفية ودراسات الحالة.
- **فرق التوطين** التي تدقق الأسواق المغطاة وأين لا يزال يتم شحن النسخة الإنجليزية الافتراضية.
- **مهندسو الواجهة الخلفية وضمان الجودة** الذين يختبرون تكاملات iTunes Search API دون كتابة scraper.
- **الكتّاب والمدوّنون** الذين يحتاجون إلى أيقونة التطبيق الرسمية وبعض لقطات الشاشة لمقال.

## الخصوصية وإخلاء المسؤولية

يعمل AppLookup.pro في متصفحك. لا يوجد تسجيل دخول. لا يوجد تتبع. لا يوجد تسجيل من جانب الخادم للتطبيقات التي تبحث عنها. تذهب الطلبات مباشرة من متصفحك إلى [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) من Apple.

هذه الأداة **للأغراض التعليمية والبحثية فقط**. يتم جلب جميع البيانات من واجهة API الرسمية العامة من Apple وتبقى ملكاً لشركة Apple Inc. وناشري التطبيقات المدرجين. يخضع استخدام الأداة لـ [شروط وأحكام Apple Media Services](https://www.apple.com/legal/internet-services/terms/site.html). يرجى احترام حدود معدل Apple وعدم إعادة توزيع الأصول المحمية بحقوق الطبع والنشر.

## جربها الآن

لست بحاجة إلى مفتاح API أو حساب مطور أو خطة مدفوعة لفحص بيانات App Store. افتح [applookup.pro](https://applookup.pro)، الصق أي رابط App Store، وستحصل على البيانات والأيقونات وJSON الخام في ثوانٍ.

## مفتوح المصدر

AppLookup.pro مفتوح المصدر. تقارير الأخطاء وإضافات الدول وطلبات السحب مرحب بها.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro على GitHub" icon="github" tag="مفتوح المصدر" >}}
{{< /cards >}}

---

## الأسئلة المتكررة

{{% details title="هل AppLookup.pro مجاني فعلاً؟" closed="true" %}}
نعم. AppLookup.pro مجاني ومفتوح المصدر بنسبة 100 بالمئة. يعمل في متصفحك. لا يوجد تسجيل ولا فئة مدفوعة ولا حد للاستخدام يتجاوز حدود iTunes Search API الخاصة بـ Apple.
{{% /details %}}

{{% details title="من أين تأتي البيانات؟" closed="true" %}}
يتم جلب كل نتيجة في الوقت الفعلي من واجهة [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) الرسمية من Apple. لا تقوم الأداة بـ scraping لصفحات App Store ولا تخزن الردود مؤقتاً على أي خادم.
{{% /details %}}

{{% details title="هل يمكنني تنزيل أيقونة التطبيق بدقة عالية؟" closed="true" %}}
نعم. يعرض قسم **App Icon** كل رابط أيقونة تعيده Apple. كل بطاقة بها Direct Link وزر Download، وزر Download All Icons ZIP يحزمها في أرشيف واحد.
{{% /details %}}

{{% details title="هل يمكنني تنزيل جميع لقطات شاشة App Store دفعة واحدة؟" closed="true" %}}
نعم. كل قسم لقطات شاشة (iPhone وiPad وmacOS وApple TV) به زر **Download All (ZIP)** يحزم كل لقطة شاشة بالدقة الكاملة.
{{% /details %}}

{{% details title="كيف أرى كيف يبدو التطبيق في دولة أخرى؟" closed="true" %}}
اختر دولة في القائمة المنسدلة في أعلى الصفحة. أكثر من 40 متجر مدعوم. انقر على **Lookup** مرة أخرى وستعيد الأداة جلب التطبيق لتلك الدولة، وتعرض العنوان والوصف ولقطات الشاشة وما الجديد والسعر المحلي.
{{% /details %}}

{{% details title="هل يمكنني نسخ حقول مفردة مثل bundle ID أو تاريخ الإصدار؟" closed="true" %}}
نعم. كل حقل نصي في النتيجة له زر Copy خاص به: اسم التطبيق، المطور، الوصف، ما الجديد، bundle ID، الإصدار، السعر، حجم الملف، الحد الأدنى لنظام التشغيل، تاريخ الإصدار، تصنيف المحتوى، اللغات، الأجهزة المدعومة وJSON الخام.
{{% /details %}}

{{% details title="هل يعمل AppLookup.pro مع أي تطبيق iOS؟" closed="true" %}}
يعمل مع أي تطبيق مدرج علنياً في دولة App Store واحدة على الأقل ويعيده iTunes Search API. التطبيقات غير المدرجة أو المحذوفة أو الموزعة كمؤسسات لن تظهر.
{{% /details %}}

{{% details title="هل يدعم تطبيقات macOS وApple TV؟" closed="true" %}}
نعم. إذا كان للتطبيق لقطات شاشة لـ macOS أو Apple TV في استجابة iTunes Search API، يعرضها AppLookup.pro في لوحة قابلة للتمرير خاصة بها مع أزرار التنزيل.
{{% /details %}}

{{% details title="هل يمكنني استخدام JSON الخام في الكود الخاص بي؟" closed="true" %}}
نعم. يعرض قسم Raw API Response JSON الدقيق الذي تعيده Apple. انسخه إلى Postman أو اختبار وحدة أو خط أنابيب backend. يرجى احترام شروط API الخاصة بـ Apple وحدود المعدل المعقولة.
{{% /details %}}

{{% details title="هل من الآمن لصق روابط App Store في الأداة؟" closed="true" %}}
نعم. يتم تحليل الرابط في متصفحك. الاتصال الشبكي الصادر الوحيد هو البحث في iTunes Search API من Apple.
{{% /details %}}

{{% details title="ما الفرق بين AppLookup.pro وAppKeywords.pro؟" closed="true" %}}
[AppLookup.pro](https://applookup.pro) مخصص لقراءة بيانات App Store من أي تطبيق منشور: بحث المنافسين، تنزيل الأصول، فحوصات التوطين. [AppKeywords.pro](https://appkeywords.pro) مخصص لكتابة بيانات App Store لتطبيقك الخاص: تحسين العنوان والعنوان الفرعي والكلمات المفتاحية بدعم Fastlane. تعمل الأداتان معاً بشكل جيد.
{{% /details %}}
