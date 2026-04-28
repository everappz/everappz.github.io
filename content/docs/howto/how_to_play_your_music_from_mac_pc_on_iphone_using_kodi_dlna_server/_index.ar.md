---
title: "كيفية تشغيل الموسيقى من Mac / PC / Linux / NAS على iPhone باستخدام خادم Kodi DLNA"
date: 2025-07-25
description: "بث الموسيقى من الكمبيوتر أو NAS إلى iPhone عبر Wi-Fi باستخدام Kodi DLNA وتطبيق Evermusic."
keywords: ["خادم kodi dlna", "بث الموسيقى إلى iphone", "تشغيل الموسيقى من nas", "evermusic dlna", "الموسيقى من mac إلى iphone", "الموسيقى من windows إلى iphone", "kodi dlna iphone", "بث الصوت عبر dlna"]
tags: ["dlna", "kodi", "evermusic", "iphone", "بث الموسيقى", "mac", "nas", "linux", "الشبكة المحلية"]
readingTime: 5
---

{{< author-byline >}}


**ملخص:** قم بتثبيت Kodi على Mac أو PC أو Linux أو NAS، وقم بتفعيل خادم DLNA/UPnP، وقم ببث مكتبتك الموسيقية بالكامل إلى iPhone أو iPad باستخدام تطبيق Evermusic أو Flacbox المجاني عبر Wi-Fi. لا حاجة لاشتراكات.

## مقدمة

إذا كان لديك **Mac أو PC يعمل بنظام Windows أو جهاز Linux أو جهاز NAS**، يمكنك بسهولة تحويله إلى **خادم موسيقى شخصي** في المنزل باستخدام [Kodi](https://kodi.tv/)، وهي منصة وسائط مجانية ومفتوحة المصدر. باستخدام خادم **DLNA/UPnP** المدمج في Kodi، يمكنك بث مكتبتك الموسيقية بالكامل إلى أي عميل متوافق مع DLNA — بما في ذلك iPhone أو iPad.

في هذا الدليل، سنوضح لك خطوة بخطوة كيفية:

- تثبيت Kodi على Mac أو PC  
- إعداد مجلدات الموسيقى للمشاركة  
- تفعيل خادم الموسيقى DLNA  
- الوصول إلى تلك الموسيقى باستخدام تطبيق **Evermusic** أو **Flacbox** لنظام iOS

هذا الإعداد مجاني بالكامل — لا اشتراكات، فقط موسيقاك الخاصة تُبث عبر شبكة Wi-Fi. سواء كنت تحاول تنظيم مجموعة MP3 الكبيرة الخاصة بك، أو الاستماع إلى FLAC عبر Wi-Fi، أو الاستمتاع بموسيقاك المحلية دون المزامنة عبر iTunes، فإن هذا الإعداد مثالي لك.

## تنزيل وتثبيت Kodi على Mac / PC / Linux / NAS

أولاً، قم بزيارة موقع Kodi الرسمي:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="الصفحة الرئيسية لموقع Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

انقر على **التنزيلات** وقم بالتمرير للعثور على الإصدار المناسب لجهازك.
اختر نظام التشغيل الخاص بك. في هذا المثال، سنستخدم **macOS**.

{{< cards cols="1">}}
{{< card subtitle="صفحة تنزيلات Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

انقر على **Intel (x86/64)** إذا كان لديك Mac بمعالج Intel أو **Apple Silicon** لأجهزة M1 أو M2 أو M3 Mac لبدء التنزيل.

{{< cards cols="1">}}
{{< card subtitle="اختر مثبت macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

يرجى الانتظار لحظة أثناء تنزيل المثبت.

{{< cards cols="1">}}
{{< card subtitle="تم تنزيل Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

بعد التنزيل، حدد موقع ملف `.dmg` في مجلد **التنزيلات**.

{{< cards cols="1">}}
{{< card subtitle="تثبيت Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

انقر مرتين على الملف الذي تم تنزيله لتشغيل المثبت.
اسحب Kodi إلى مجلد **التطبيقات** للتثبيت.

{{< cards cols="1">}}
{{< card title="" subtitle="قم بتثبيت Kodi عن طريق سحبه إلى التطبيقات" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

قم بتشغيل Kodi. قد تحتاج إلى السماح به في **تفضيلات النظام ← الأمان والخصوصية ← فتح على أي حال**.

{{< cards cols="1">}}
{{< card subtitle="الشاشة الرئيسية لـ Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## إضافة الموسيقى إلى مكتبة Kodi

انقر على **أيقونة الترس** (الإعدادات) من الشاشة الرئيسية.

{{< cards cols="1">}}
{{< card subtitle="إعدادات Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

انتقل إلى **إعدادات الوسائط ← المكتبة**. قم بتفعيل **تحديث المكتبة عند بدء التشغيل** لمكتبة الفيديو ومكتبة الموسيقى للفهرسة التلقائية.

{{< cards cols="1">}}
{{< card subtitle="إعدادات المكتبة" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

ثم انتقل إلى قسم **الموسيقى** وانقر على **إضافة موسيقى**.

{{< cards cols="1">}}
{{< card subtitle="إضافة مجلد الموسيقى" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

تصفح واختر المجلد الذي تُخزن فيه الموسيقى.

{{< cards cols="1">}}
{{< card subtitle="اختيار مصدر الموسيقى" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

أضف مصدر الموسيقى إلى Kodi.

{{< cards cols="1">}}
{{< card subtitle="إضافة مصدر الموسيقى" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

قم بالتأكيد واترك Kodi يفحص مكتبتك الموسيقية.

{{< cards cols="1">}}
{{< card subtitle="تأكيد مصادر الموسيقى" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

انتظر لحظة أثناء فحص المكتبة وبنائها بالكامل.

{{< cards cols="1">}}
{{< card subtitle="فحص مكتبة الموسيقى" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## تفعيل خادم DLNA في Kodi

انتقل إلى **الإعدادات ← الخدمات ← UPnP/DLNA**.

قم بتفعيل الخيار: **مشاركة مكتباتي**.

أصبح Kodi الآن يعمل كخادم DLNA على شبكة Wi-Fi المحلية الخاصة بك.

{{< cards cols="1">}}
{{< card subtitle="تفعيل DLNA في Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## فتح مكتبة Kodi

انقر بزر الماوس الأيمن لإغلاق نافذة الإعدادات وفتح مكتبة Kodi الرئيسية.

{{< cards cols="1">}}
{{< card title="" subtitle="انقر بزر الماوس الأيمن للوصول إلى مكتبة Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## تنزيل تطبيق بث الموسيقى لنظام iOS

احصل على تطبيق عميل DLNA مجاني لنظام iOS يتيح لك بث الموسيقى من مجموعة واسعة من خدمات التخزين السحابي وخوادم DLNA.

- استخدم **Evermusic** إذا كانت مجموعتك تتكون بشكل أساسي من MP3 وصيغ الصوت القياسية الأخرى.
- اختر **Flacbox** إذا كانت لديك مكتبة موسيقى عالية الدقة بصيغ مثل FLAC أو ALAC أو DSD.

كلا التطبيقين متاحان لنظامي **iOS** و**macOS**، ومجانيان للاستخدام.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="تحميل Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="تحميل Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## إضافة مصدر DLNA

بعد تنزيل تطبيق iOS، افتح قسم **جميع الاتصالات**.

{{< cards cols="1">}}
{{< card title="" subtitle="الشريط الجانبي الرئيسي لتطبيق Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

قم بالتمرير لأسفل وانقر على **الشبكة المحلية - الأجهزة المتاحة** لاكتشاف خوادم DLNA.
في هذا القسم، سترى جميع الأجهزة المتاحة على شبكتك المحلية. يجب أن يظهر **خادم Kodi DLNA** هنا. انقر على خادم Kodi للاتصال.

{{< cards cols="1">}}
{{< card title="" subtitle="أجهزة DLNA المتاحة في Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

سيعرض Evermusic مجلدات المكتبة المشتركة عبر Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="مكتبة موسيقى Kodi على Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

انتقل إلى مجلد **الأغاني** لعرض جميع ملفات الصوت المتاحة على خادم DLNA الخاص بك.

{{< cards cols="1">}}
{{< card title="" subtitle="الأغاني المدرجة من المجلد البعيد" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

انقر على أي ملف صوتي لبدء البث فوراً.

{{< cards cols="1">}}
{{< card title="" subtitle="تشغيل ملف MP3 في Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

ارجع إلى قسم **الاتصالات**. سيظهر خادم DLNA المضاف هنا الآن. انقر على أيقونته لإعادة الاتصال في أي وقت. يمكنك أيضاً توصيل خدمات سحابية أخرى من هذه الشاشة باستخدام نفس الخطوات.

يمكنك تفعيل **تتبع Last.fm** هنا أيضاً. سيتم حفظ إحصائيات التشغيل في حساب Last.fm الخاص بك، مما يوفر توصيات موسيقية مخصصة لاحقاً.

{{< cards cols="1">}}
{{< card title="" subtitle="الاتصالات في Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## بناء مكتبة الموسيقى

يتيح لك كل من **Evermusic** و**Flacbox** إضافة الموسيقى إلى مكتبتك وتنظيمها حسب **علامات البيانات الوصفية** مثل الفنانين والألبومات والأنواع والمؤلفين.

للبدء، افتح قسم **مكتبة الموسيقى**. قم بالتمرير لأسفل إلى **الأدوات والتفضيلات** وانقر على **إضافة موسيقى**.

{{< cards cols="1">}}
{{< card title="" subtitle="مكتبة موسيقى Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

اختر مصدر الموسيقى — في هذه الحالة، اختر **الاتصالات**.

{{< cards cols="1">}}
{{< card title="" subtitle="إضافة موسيقى جديدة في Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

ابحث عن **خادم Kodi DLNA** في الاتصالات وانقر لعرض المجلدات والملفات.

{{< cards cols="1">}}
{{< card title="" subtitle="اختيار خادم DLNA لاستيراد الموسيقى" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

اختر المجلدات أو الملفات التي تريد إضافتها وانقر على **تم**.

{{< cards cols="1">}}
{{< card title="" subtitle="اختيار مجلد الموسيقى للإضافة" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

سيقوم التطبيق بفحص ملفاتك المحددة وتنظيمها باستخدام البيانات الوصفية في أقسام مثل الفنانين والألبومات والأنواع والمؤلفين.

{{< cards cols="1">}}
{{< card title="" subtitle="مكتبة الموسيقى مع الفئات" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## إنشاء قوائم التشغيل

يمكنك أيضاً إنشاء قوائم التشغيل الخاصة بك.

أولاً، افتح علامة تبويب **قوائم التشغيل**.

{{< cards cols="1">}}
{{< card title="" subtitle="علامة تبويب قوائم التشغيل في Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

انقر على زر **الإضافة (+)** واختر **قائمة تشغيل جديدة**.

{{< cards cols="1">}}
{{< card title="" subtitle="إنشاء قائمة تشغيل جديدة" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

أدخل اسماً لقائمة التشغيل وانقر على **حفظ**.

{{< cards cols="1">}}
{{< card title="" subtitle="إدخال اسم قائمة التشغيل" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

بعد ذلك، اختر مصدراً لإضافة الأغاني منه — هنا، نختار **المكتبة**.

{{< cards cols="1">}}
{{< card title="" subtitle="إضافة أغانٍ إلى قائمة تشغيل جديدة" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

اختر الأغاني التي تريدها وانقر على **تم** لإضافتها.

{{< cards cols="1">}}
{{< card title="" subtitle="إضافة الموسيقى من المكتبة إلى قائمة التشغيل" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

ستظهر الآن المقاطع المحددة في قائمة التشغيل التي تم إنشاؤها.

{{< cards cols="1">}}
{{< card title="" subtitle="قائمة التشغيل المنشأة تظهر في القائمة" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

بشكل افتراضي، الأغاني متاحة للبث. للاستماع بدون اتصال، قم بتفعيل **وضع عدم الاتصال** — سيقوم التطبيق بتنزيل جميع مقاطع قائمة التشغيل.

{{< cards cols="1">}}
{{< card title="" subtitle="تم تفعيل وضع عدم الاتصال لقائمة التشغيل" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

انقر على زر **المزيد من الإجراءات** لاستكشاف خيارات إضافية. يمكنك:

- أرشفة قائمة التشغيل  
- تغيير غلاف الألبوم  
- إعادة ترتيب المقاطع  
- والمزيد من الميزات المفيدة

{{< cards cols="1">}}
{{< card title="" subtitle="المزيد من إجراءات قائمة التشغيل المتاحة" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## الخاتمة

مع **Evermusic** و**Flacbox**، تحويل iPhone أو iPad أو Mac إلى مشغل موسيقى DLNA قوي أمر سهل. سواء كنت تخزن موسيقاك في السحابة أو على NAS أو على خادم وسائط منزلي مثل **Kodi**، تتيح لك هذه التطبيقات البث والتنظيم والاستمتاع بمجموعتك بدون حدود.

- بث MP3 أو FLAC عالي الدقة مباشرة من **خادم Kodi DLNA**  
- بناء مكتبة موسيقى شخصية مجمعة حسب البيانات الوصفية (الألبومات، الأنواع، المؤلفين)  
- إنشاء وإدارة **قوائم تشغيل مخصصة**  
- تفعيل **وضع عدم الاتصال** للاستماع أثناء التنقل  
- الاتصال بـ **خدمات سحابية متعددة** و**أجهزة الشبكة المحلية**  
- تتبع عادات الاستماع مع **تكامل Last.fm**

سواء كنت من عشاق الصوت أو مستمعاً عادياً، يوفر Evermusic وFlacbox كل ما تحتاجه لبث الموسيقى وتنظيمها بسلاسة.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="تحميل Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="تحميل Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

ابدأ ببناء تجربتك الموسيقية الشخصية اليوم.

## الأسئلة الشائعة

{{% details title="هل Kodi مجاني للاستخدام كخادم DLNA؟" closed="true" %}}
نعم. Kodi مجاني تماماً ومفتوح المصدر. يعمل على macOS وWindows وLinux والعديد من أجهزة NAS.
{{% /details %}}

{{% details title="هل يدعم Evermusic وFlacbox بث FLAC عبر DLNA؟" closed="true" %}}
نعم. تم تحسين Flacbox لصيغ الصوت عالية الدقة مثل FLAC وALAC وDSD. يدعم Evermusic أيضاً تشغيل FLAC بالإضافة إلى MP3 والصيغ القياسية الأخرى.
{{% /details %}}

{{% details title="هل يمكنني الاستماع بدون اتصال بعد البث من Kodi؟" closed="true" %}}
نعم. قم بتفعيل وضع عدم الاتصال على أي قائمة تشغيل، وسيقوم التطبيق بتنزيل جميع المقاطع إلى جهازك للاستماع بدون اتصال بالشبكة.
{{% /details %}}

{{% details title="هل أحتاج إلى اشتراك مدفوع لاستخدام DLNA؟" closed="true" %}}
يدعم الإصدار المجاني ما يصل إلى 3 اتصالات سحابية أو شبكية. يزيل الإصدار المدفوع هذا الحد ويتيح لك توصيل خدمات وخوادم DLNA غير محدودة.
{{% /details %}}

{{% details title="هل يجب أن يكون iPhone على نفس شبكة Wi-Fi مع Kodi؟" closed="true" %}}
نعم. يعمل بث DLNA عبر شبكتك المحلية. يجب أن يكون خادم Kodi وجهاز iOS متصلين بنفس شبكة Wi-Fi.
{{% /details %}}

{{% details title="هل يمكنني استخدام هذا الإعداد مع NAS بدلاً من Mac أو PC؟" closed="true" %}}
نعم. العديد من أجهزة NAS (Synology وQNAP وغيرها) تدعم Kodi أو لديها خادم DLNA مدمج خاص بها. يمكن لـ Evermusic وFlacbox الاتصال بأي خادم DLNA/UPnP قياسي.
{{% /details %}}
