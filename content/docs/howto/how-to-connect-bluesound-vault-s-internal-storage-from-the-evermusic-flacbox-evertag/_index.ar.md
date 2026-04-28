---
title: "كيفية الاتصال بوحدة التخزين الداخلية لجهاز Bluesound VAULT من Evermusic وFlacbox وEvertag"
date: 2022-03-10
description: "تعرف على كيفية الوصول إلى القرص الصلب الداخلي لجهاز Bluesound VAULT من Evermusic وFlacbox وEvertag باستخدام بروتوكول SMB لإدارة ملفات الصوت وتحريرها وتشغيلها."
keywords: ["bluesound vault", "توصيل تخزين smb", "evermusic smb", "flacbox vault", "evertag smb", "تخزين nas للموسيقى", "محرك vault الداخلي"]
tags: ["evermusic", "الاتصال", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**ملخص:** اتصل بوحدة التخزين الداخلية لجهاز Bluesound VAULT عبر SMB باستخدام Evermusic أو Flacbox أو Evertag. ابحث عن عنوان IP الخاص بجهاز VAULT في تطبيق BluOS، وأدخله كاتصال SMB مع وصول الضيف، وابدأ تشغيل ملفات الموسيقى أو إدارتها.

يحتوي جهاز Bluesound VAULT على قرص صلب داخلي ويعمل كوحدة تخزين متصلة بالشبكة (NAS). يتيح لك الوصول إلى القرص الصلب الداخلي لجهاز VAULT إضافة/حذف الملفات وتحرير علامات البيانات الوصفية من تطبيقاتنا Evermusic وFlacbox وEvertag.

**فيما يلي خطوات الوصول إلى القرص الصلب الداخلي لجهاز VAULT:**

1. في تطبيق BluOS، اختر **المساعدة > التشخيصات**.

2. من صفحة **التشخيصات**، احصل على **عنوان IP** الخاص بجهاز VAULT. سيتم استخدام **عنوان IP** هذا في الخطوات التالية.

3. افتح Evermusic أو Flacbox أو Evertag.

   ![تطبيقات Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. افتح شاشة "الاتصالات" واختر عنصر القائمة "توصيل خدمة سحابية".

   ![شاشة اتصالات Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. اختر خدمة "SMB" السحابية.

   ![شاشة توصيل خدمة سحابية في Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. في "شاشة إعداد SMB" أدخل عنوان URL بالتنسيق التالي:

   ```
   SMB://<<VAULT-IP>>
   ```

   استبدل `<<VAULT-IP>>` بـ**عنوان IP** الذي حصلت عليه في الخطوة 2.

   **ملاحظة:** اترك حقلي تسجيل الدخول وكلمة المرور فارغين لأن تخزين VAULT يدعم وضع الضيف (GUEST).

   ![شاشة اتصال SMB في Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. اضغط على زر "تسجيل الدخول" لحفظ الإعدادات.

8. افتح التخزين السحابي المتصل وانتقل داخل المجلد الذي يحتوي على ملفات الصوت واضغط على أي ملف لبدء مشغل الصوت.

   ![شاشة خادم SMB المفتوح في Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. يمكنك أيضًا تحرير الملفات باستخدام مدير الملفات المدمج.

   ![شاشة مدير الملفات في Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

باتباع هذه الخطوات البسيطة، يمكنك الوصول بسهولة إلى القرص الصلب الداخلي لجهاز Bluesound VAULT والتحكم في مكتبة الموسيقى الخاصة بك باستخدام Evermusic أو Flacbox أو Evertag.

## الأسئلة الشائعة

{{% details title="هل أحتاج إلى اسم مستخدم وكلمة مرور للاتصال بجهاز Bluesound VAULT؟" closed="true" %}}
لا. يدعم Bluesound VAULT الوصول كضيف (مجهول) عبر SMB. اترك حقلي تسجيل الدخول وكلمة المرور فارغين عند إعداد الاتصال.
{{% /details %}}

{{% details title="هل يمكنني تحرير علامات الموسيقى على Bluesound VAULT؟" closed="true" %}}
نعم. باستخدام Evertag، يمكنك تحرير علامات البيانات الوصفية (العنوان، الفنان، الألبوم، إلخ) لملفات الصوت المخزنة مباشرة على القرص الصلب الداخلي لجهاز VAULT.
{{% /details %}}

{{% details title="ما البروتوكولات التي يدعمها Bluesound VAULT؟" closed="true" %}}
يكشف Bluesound VAULT عن تخزينه الداخلي عبر SMB (Server Message Block). تدعم Evermusic وFlacbox وEvertag جميعها اتصالات SMB، مما يجعل الاتصال سهلاً.
{{% /details %}}

{{% details title="هل يمكنني بث الموسيقى من VAULT دون نسخ الملفات إلى iPhone؟" closed="true" %}}
نعم. بمجرد الاتصال عبر SMB، يمكنك بث ملفات الصوت مباشرة من محرك الأقراص الداخلي لجهاز VAULT دون نسخها إلى جهازك.
{{% /details %}}
