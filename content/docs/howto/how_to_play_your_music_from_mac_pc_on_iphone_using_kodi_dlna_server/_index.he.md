---
title: "כיצד להשמיע מוזיקה מ-Mac / PC / Linux / NAS באייפון באמצעות שרת Kodi DLNA"
date: 2025-07-25
description: "הזרמת מוזיקה מהמחשב או NAS לאייפון שלך דרך Wi-Fi באמצעות Kodi DLNA ואפליקציית Evermusic."
keywords: ["שרת kodi dlna", "הזרמת מוזיקה לאייפון", "השמעת מוזיקה מ-nas", "evermusic dlna", "מוזיקה ממק לאייפון", "מוזיקה מ-windows לאייפון", "kodi dlna iphone", "הזרמת אודיו dlna"]
tags: ["dlna", "kodi", "evermusic", "iphone", "הזרמת מוזיקה", "mac", "nas", "linux", "רשת מקומית"]
readingTime: 5
---

{{< author-byline >}}


**תקציר:** התקן Kodi על Mac, PC, Linux או NAS, הפעל את שרת DLNA/UPnP שלו, והזרם את כל ספריית המוזיקה שלך לאייפון או אייפד באמצעות אפליקציית Evermusic או Flacbox החינמית דרך Wi-Fi. ללא מנויים.

## מבוא

אם יש לך **Mac, PC עם Windows, מכונת Linux או התקן NAS**, תוכל בקלות להפוך אותו ל**שרת מוזיקה אישי** בבית באמצעות [Kodi](https://kodi.tv/), פלטפורמת מדיה חינמית וקוד פתוח. עם שרת **DLNA/UPnP** המובנה של Kodi, תוכל להזרים את כל ספריית המוזיקה שלך לכל לקוח תואם DLNA — כולל האייפון או האייפד שלך.

במדריך זה, נראה לך צעד אחר צעד כיצד:

- להתקין Kodi על Mac או PC  
- להגדיר תיקיות מוזיקה לשיתוף  
- להפעיל את שרת המוזיקה DLNA  
- לגשת למוזיקה באמצעות אפליקציית **Evermusic** או **Flacbox** ל-iOS

הגדרה זו היא 100% חינמית — ללא מנויים, רק המוזיקה שלך מוזרמת דרך רשת Wi-Fi. בין אם אתה מנסה לארגן את אוסף MP3 הגדול שלך, להאזין ל-FLAC דרך Wi-Fi, או פשוט ליהנות מהמוזיקה המקומית שלך ללא סנכרון דרך iTunes, הגדרה זו מושלמת עבורך.

## הורדה והתקנה של Kodi על Mac / PC / Linux / NAS

ראשית, בקר באתר הרשמי של Kodi:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="דף הבית של Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

לחץ על **הורדות** וגלול למטה כדי למצוא את הגרסה למחשב שלך.
בחר את מערכת ההפעלה שלך. בדוגמה זו, נשתמש ב-**macOS**.

{{< cards cols="1">}}
{{< card subtitle="דף ההורדות של Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

לחץ על **Intel (x86/64)** אם יש לך Mac עם Intel או **Apple Silicon** עבור M1, M2, M3 Mac כדי להתחיל בהורדה.

{{< cards cols="1">}}
{{< card subtitle="בחר מתקין macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

אנא המתן רגע בזמן שהמתקין יורד.

{{< cards cols="1">}}
{{< card subtitle="Kodi הורד" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

לאחר ההורדה, אתר את קובץ `.dmg` בתיקיית **ההורדות** שלך.

{{< cards cols="1">}}
{{< card subtitle="התקנת Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

לחץ לחיצה כפולה על הקובץ שהורד כדי להפעיל את המתקין.
גרור את Kodi לתיקיית **היישומים** שלך להתקנה.

{{< cards cols="1">}}
{{< card title="" subtitle="התקן Kodi על ידי גרירתו ליישומים" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

הפעל את Kodi. ייתכן שתצטרך לאפשר אותו ב**העדפות מערכת ← אבטחה ופרטיות ← פתח בכל זאת**.

{{< cards cols="1">}}
{{< card subtitle="מסך הבית של Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## הוספת מוזיקה לספריית Kodi

לחץ על **סמל גלגל השיניים** (הגדרות) ממסך הבית.

{{< cards cols="1">}}
{{< card subtitle="הגדרות Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

נווט אל **הגדרות מדיה ← ספרייה**. הפעל **עדכן ספרייה בהפעלה** עבור ספריית הווידאו והמוזיקה לאינדוקס אוטומטי.

{{< cards cols="1">}}
{{< card subtitle="הגדרות ספרייה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

לאחר מכן עבור לקטע **מוזיקה** ולחץ על **הוסף מוזיקה**.

{{< cards cols="1">}}
{{< card subtitle="הוסף תיקיית מוזיקה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

עיין ובחר את התיקייה בה מאוחסנת המוזיקה שלך.

{{< cards cols="1">}}
{{< card subtitle="בחר מקור מוזיקה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

הוסף מקור מוזיקה ל-Kodi.

{{< cards cols="1">}}
{{< card subtitle="הוסף מקור מוזיקה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

אשר ותן ל-Kodi לסרוק את ספריית המוזיקה שלך.

{{< cards cols="1">}}
{{< card subtitle="אשר מקורות מוזיקה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

המתן רגע בזמן שהספרייה שלך נסרקת ונבנית במלואה.

{{< cards cols="1">}}
{{< card subtitle="סריקת ספריית מוזיקה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## הפעלת שרת DLNA של Kodi

עבור אל **הגדרות ← שירותים ← UPnP/DLNA**.

הפעל את האפשרות: **שתף את הספריות שלי**.

Kodi פועל כעת כשרת DLNA ברשת Wi-Fi המקומית שלך.

{{< cards cols="1">}}
{{< card subtitle="הפעלת DLNA ב-Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## פתיחת ספריית Kodi

לחץ לחיצה ימנית כדי לסגור את חלון ההגדרות ולפתוח את ספריית Kodi הראשית.

{{< cards cols="1">}}
{{< card title="" subtitle="לחיצה ימנית לגישה לספריית Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## הורדת אפליקציית הזרמת מוזיקה ל-iOS

קבל אפליקציית לקוח DLNA חינמית ל-iOS שמאפשרת לך להזרים מוזיקה ממגוון רחב של שירותי אחסון ענן ושרתי DLNA.

- השתמש ב-**Evermusic** אם האוסף שלך הוא בעיקר MP3 ופורמטי אודיו סטנדרטיים אחרים.
- בחר ב-**Flacbox** אם יש לך ספריית מוזיקה ברזולוציה גבוהה בפורמטים כמו FLAC, ALAC או DSD.

שתי האפליקציות זמינות ל-**iOS** ו-**macOS**, וחינמיות לשימוש.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="הורד Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="הורד Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## הוספת מקור DLNA

לאחר הורדת אפליקציית iOS, פתח את קטע **כל החיבורים**.

{{< cards cols="1">}}
{{< card title="" subtitle="סרגל צד ראשי של אפליקציית Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

גלול למטה והקש על **רשת מקומית - מכשירים זמינים** כדי לגלות שרתי DLNA.
בקטע זה תראה את כל המכשירים הזמינים ברשת המקומית שלך. **שרת Kodi DLNA** שלך אמור להופיע כאן. הקש על שרת Kodi כדי להתחבר.

{{< cards cols="1">}}
{{< card title="" subtitle="מכשירי DLNA זמינים ב-Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic יציג את תיקיות הספרייה המשותפות דרך Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="ספריית מוזיקה של Kodi ב-Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

נווט לתיקיית **שירים** כדי לראות את כל קבצי האודיו הזמינים בשרת DLNA שלך.

{{< cards cols="1">}}
{{< card title="" subtitle="שירים מתיקייה מרוחקת" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

הקש על כל קובץ אודיו כדי להתחיל בהזרמה מיידית.

{{< cards cols="1">}}
{{< card title="" subtitle="קובץ MP3 מתנגן ב-Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

חזור לקטע **חיבורים**. שרת DLNA שנוסף יופיע כאן כעת. הקש על הסמל שלו כדי להתחבר מחדש בכל עת. תוכל גם לחבר שירותי ענן אחרים ממסך זה באמצעות אותם שלבים.

תוכל גם להפעיל **מעקב Last.fm** כאן. סטטיסטיקות השמעה יישמרו בחשבון Last.fm שלך, ויספקו המלצות מוזיקה מותאמות אישית מאוחר יותר.

{{< cards cols="1">}}
{{< card title="" subtitle="חיבורים ב-Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## בניית ספריית מוזיקה

**Evermusic** ו-**Flacbox** מאפשרים לך להוסיף מוזיקה לספרייה שלך ולארגן אותה לפי **תגיות מטא-נתונים** כמו אמנים, אלבומים, ז'אנרים ומלחינים.

כדי להתחיל, פתח את קטע **ספריית המוזיקה**. גלול למטה אל **כלים והעדפות** והקש על **הוסף מוזיקה**.

{{< cards cols="1">}}
{{< card title="" subtitle="ספריית מוזיקה של Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

בחר את מקור המוזיקה — במקרה זה, בחר **חיבורים**.

{{< cards cols="1">}}
{{< card title="" subtitle="הוסף מוזיקה חדשה ב-Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

מצא את **שרת Kodi DLNA** בחיבורים והקש כדי לראות תיקיות וקבצים.

{{< cards cols="1">}}
{{< card title="" subtitle="בחר שרת DLNA לייבוא מוזיקה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

בחר את התיקיות או הקבצים שברצונך להוסיף והקש על **בוצע**.

{{< cards cols="1">}}
{{< card title="" subtitle="בחר תיקיית מוזיקה להוספה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

האפליקציה תסרוק את הקבצים שבחרת ותארגן אותם באמצעות מטא-נתונים לקטגוריות כמו אמנים, אלבומים, ז'אנרים ומלחינים.

{{< cards cols="1">}}
{{< card title="" subtitle="ספריית מוזיקה עם קטגוריות" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## יצירת רשימות השמעה

תוכל גם ליצור רשימות השמעה משלך.

ראשית, פתח את לשונית **רשימות השמעה**.

{{< cards cols="1">}}
{{< card title="" subtitle="לשונית רשימות השמעה ב-Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

הקש על כפתור **הפלוס (+)** ובחר **רשימת השמעה חדשה**.

{{< cards cols="1">}}
{{< card title="" subtitle="צור רשימת השמעה חדשה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

הזן שם לרשימת ההשמעה שלך והקש על **שמור**.

{{< cards cols="1">}}
{{< card title="" subtitle="הזן שם רשימת השמעה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

לאחר מכן, בחר מקור להוספת שירים — כאן, בוחרים את **הספרייה**.

{{< cards cols="1">}}
{{< card title="" subtitle="הוסף שירים לרשימת השמעה חדשה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

בחר את השירים שאתה רוצה והקש על **בוצע** כדי להוסיף אותם.

{{< cards cols="1">}}
{{< card title="" subtitle="הוסף מוזיקה מהספרייה לרשימת השמעה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

השירים שבחרת יופיעו כעת ברשימת ההשמעה שנוצרה.

{{< cards cols="1">}}
{{< card title="" subtitle="רשימת השמעה שנוצרה מוצגת ברשימה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

כברירת מחדל, השירים זמינים להזרמה. כדי להאזין במצב לא מקוון, הפעל **מצב לא מקוון** — האפליקציה תוריד את כל שירי רשימת ההשמעה.

{{< cards cols="1">}}
{{< card title="" subtitle="מצב לא מקוון מופעל עבור רשימת השמעה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

הקש על כפתור **עוד פעולות** כדי לחקור אפשרויות נוספות. תוכל:

- לארכב את רשימת ההשמעה  
- לשנות את עטיפת האלבום  
- לסדר מחדש שירים  
- ועוד תכונות שימושיות

{{< cards cols="1">}}
{{< card title="" subtitle="עוד פעולות זמינות לרשימת השמעה" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## סיכום

עם **Evermusic** ו-**Flacbox**, הפיכת האייפון, אייפד או Mac שלך לנגן מוזיקה DLNA חזק היא קלה. בין אם אתה מאחסן את המוזיקה שלך בענן, ב-NAS או בשרת מדיה ביתי כמו **Kodi**, אפליקציות אלה מאפשרות לך להזרים, לארגן וליהנות מהאוסף שלך ללא הגבלות.

- הזרם MP3 או FLAC ברזולוציה גבוהה ישירות מ**שרת Kodi DLNA** שלך  
- בנה ספריית מוזיקה אישית מקובצת לפי מטא-נתונים (אלבומים, ז'אנרים, מלחינים)  
- צור ונהל **רשימות השמעה מותאמות אישית**  
- הפעל **מצב לא מקוון** להאזנה בדרכים  
- התחבר ל**שירותי ענן מרובים** ו**מכשירי רשת מקומית**  
- עקוב אחר הרגלי ההאזנה שלך עם **שילוב Last.fm**

בין אם אתה חובב אודיו או מאזין מזדמן, Evermusic ו-Flacbox מציעים את כל מה שצריך להזרמת מוזיקה וארגון חלקים.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="הורד Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="הורד Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

התחל לבנות את חוויית המוזיקה האישית שלך היום.

## שאלות נפוצות

{{% details title="האם Kodi חינמי לשימוש כשרת DLNA?" closed="true" %}}
כן. Kodi הוא חינמי לחלוטין וקוד פתוח. הוא פועל על macOS, Windows, Linux והרבה מכשירי NAS.
{{% /details %}}

{{% details title="האם Evermusic ו-Flacbox תומכים בהזרמת FLAC דרך DLNA?" closed="true" %}}
כן. Flacbox מותאם לפורמטים ברזולוציה גבוהה כמו FLAC, ALAC ו-DSD. Evermusic גם תומך בהשמעת FLAC לצד MP3 ופורמטים סטנדרטיים אחרים.
{{% /details %}}

{{% details title="האם אני יכול להאזין במצב לא מקוון לאחר הזרמה מ-Kodi?" closed="true" %}}
כן. הפעל מצב לא מקוון על כל רשימת השמעה, והאפליקציה תוריד את כל השירים למכשיר שלך להאזנה ללא חיבור רשת.
{{% /details %}}

{{% details title="האם אני צריך מנוי פרימיום כדי להשתמש ב-DLNA?" closed="true" %}}
הגרסה החינמית תומכת בעד 3 חיבורי ענן או רשת. פרימיום מסיר מגבלה זו ומאפשר לך לחבר שירותים ושרתי DLNA ללא הגבלה.
{{% /details %}}

{{% details title="האם האייפון שלי צריך להיות באותה רשת Wi-Fi כמו Kodi?" closed="true" %}}
כן. הזרמת DLNA פועלת דרך הרשת המקומית שלך. גם שרת Kodi וגם מכשיר iOS שלך חייבים להיות מחוברים לאותה רשת Wi-Fi.
{{% /details %}}

{{% details title="האם אני יכול להשתמש בהגדרה זו עם NAS במקום Mac או PC?" closed="true" %}}
כן. מכשירי NAS רבים (Synology, QNAP וכו') תומכים ב-Kodi או שיש להם שרת DLNA מובנה משלהם. Evermusic ו-Flacbox יכולים להתחבר לכל שרת DLNA/UPnP סטנדרטי.
{{% /details %}}
