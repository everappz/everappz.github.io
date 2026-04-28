---
title: "כיצד לחבר Synology NAS ולהאזין למוזיקה ב-iPhone או Mac"
date: 2024-09-19
description: "למד כיצד לחבר את ה-Synology NAS שלך באמצעות API מקורי או QuickConnect ולהזרים מוזיקה באיכות גבוהה ל-iPhone או Mac עם Evermusic ו-Flacbox."
keywords: ["synology nas", "הזרמת מוזיקה", "quickconnect", "evermusic synology", "flacbox synology", "נגן מוזיקה nas", "מוזיקה iphone nas"]
tags: ["מוזיקה", "הזרמה", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**תקציר:** חבר את ה-Synology NAS שלך ל-Evermusic או Flacbox באמצעות ה-API המקורי של Synology -- באופן ידני דרך כתובת IP או באופן אוטומטי דרך מזהה QuickConnect. QuickConnect מאפשר לך להזרים מוזיקה מרחוק ללא העברת פורטים. שתי האפליקציות תומכות ב-FLAC, MP3, WAV ופורמטים נוספים באיכות גבוהה.

אם אתה מחפש דרך חלקה לחבר את ה-Synology NAS שלך וליהנות מספריית המוזיקה שלך ב-iPhone או Mac, אפליקציות Evermusic ו-Flacbox הן הפתרונות המושלמים. אפליקציות אלו תומכות במגוון רחב של פורמטי שמע, כולל FLAC, MP3 ו-WAV, מה שמקל על הזרמה והאזנה למוזיקה באיכות גבוהה ישירות מה-Synology NAS שלך.

במדריך זה, נראה לך כיצד לחבר את ה-Synology NAS שלך לאפליקציית Evermusic או Flacbox באמצעות ה-API המקורי של Synology ותכונת QuickConnect. על ידי ניצול ה-API הישיר של Synology, תוכל לגשת בבטחה לספריית המוזיקה שלך מחוץ לרשת הביתית שלך ללא צורך בהגדרות מסובכות כמו WebDAV, SMB, DLNA. עם QuickConnect, תוכל להזרים ולנהל את המוזיקה שלך מכל מקום, באמצעות ה-iPhone או Mac שלך.

## שלב 1: הגדרת הרשאות תיקייה משותפת (אופציונלי)

1. פתח את **לוח הבקרה** ועבור לקטע **תיקייה משותפת**.

![תיקייה משותפת](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. בחר את תיקיית **המוזיקה** ולחץ על **עריכה**.

3. בלשונית **הרשאות**, הגדר את ההרשאות. אפשר גישת אורח עם קריאה בלבד אם אתה רק צריך להאזין למוזיקה, או קריאה/כתיבה אם אתה צריך לשנות קבצים. שמור את השינויים.

![הרשאות](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## שלב 2: מציאת כתובת ה-IP של Synology NAS

1. פתח את **לוח הבקרה** ועבור ללשונית **ממשק רשת**.

![ממשק רשת](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. או השתמש בדפדפן האינטרנט שלך כדי לבקר ב-[find.synology.com](http://find.synology.com).

![מצא Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. רשום את כתובת ה-IP של ה-Synology NAS שלך (לדוגמה, 192.168.18.137).

## שלב 3: מציאת פורטי הרשת של Synology NAS

תוכל למצוא את התיעוד הרשמי של Synology עבור פורטי הרשת המוגדרים כברירת מחדל של DSM ב[מאמר זה ממרכז הידע של Synology](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM משתמש בפורטים המוגדרים כברירת מחדל הבאים:
- **HTTP (גישה לאינטרנט):** פורט **5000**
- **HTTPS (גישה מאובטחת לאינטרנט):** פורט **5001**

אלו הם הפורטים המוגדרים כברירת מחדל לגישה לממשק DSM.

![פורטי רשת](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## שלב 4: הפעלת תכונת מזהה QuickConnect

מזהה QuickConnect של Synology הוא מזהה ייחודי המאפשר לך לגשת ל-Synology NAS שלך מרחוק דרך האינטרנט ללא צורך בהגדרת הגדרות רשת מסובכות כמו העברת פורטים. QuickConnect מפשט גישה מרחוק על ידי שימוש בשרתי Synology ליצירת חיבור בין ה-NAS שלך למכשיר שלך, כמו הטלפון החכם או המחשב, דרך מזהה QuickConnect.

**כיצד למצוא או להגדיר את מזהה ה-QuickConnect שלך:**

1. **התחבר ל-DSM.**
2. עבור אל **לוח הבקרה > גישה חיצונית > QuickConnect**.
3. **הפעל QuickConnect** וצור או צפה במזהה ה-QuickConnect הייחודי שלך.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## שלב 5: התחברות ל-Synology NAS ב-iPhone/Mac באמצעות Evermusic או Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) ו-[Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) הן אפליקציות נגן מוזיקה המיועדות למכשירי iOS ו-macOS, כל אחת מציעה תכונות ויכולות ייחודיות לניהול וליהנות מספריית המוזיקה שלך.

1. פתח את אפליקציית Evermusic או Flacbox ועבור ללשונית **חיבורים**.

![חיבורים](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. בחר **חבר שירות ענן** ובחר **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

יש לך שתי אפשרויות חיבור: **ידני** באמצעות כתובת ה-IP והפורט של השרת, או **אוטומטי** דרך מזהה QuickConnect.

### חיבור ידני

לשיטה הידנית, תצטרך את כתובת ה-IP הישירה ומספר הפורט שקיבלת בשלבים הקודמים.

1. הזן את כתובת ה-URL של השרת שקיבלת בשלב 2, בפורמט הבא: PROTOCOL://IP_ADDRESS:PORT_NUMBER
   - השתמש ב-**פורט 5000** עבור HTTP ו-**פורט 5001** עבור חיבורי HTTPS.

   לדוגמה:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. ניתן לאשר את מספר הפורט בפועל בשלב 3 של ההגדרה.
3. הזן את **שם המשתמש** ו**סיסמה** שלך ל-Synology NAS.
4. הקש על **התחבר** ליצירת החיבור.

![חיבור ידני](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### חיבור אוטומטי

לחיבור האוטומטי, תשתמש ב-**מזהה QuickConnect** משלב 4. במקום להזין ידנית את כתובת ה-IP ומספר הפורט של ה-Synology NAS שלך, פשוט הזן את **מזהה QuickConnect**. האפליקציה תאחזר אוטומטית את מידע החיבור הנדרש.

שיטה זו מאפשרת לך לגשת ל-NAS שלך מרחוק, אפילו מחוץ לרשת הביתית שלך, כך שתוכל לנהל את הקבצים שלך מהאינטרנט ללא צורך בהגדרת העברת פורטים או כתובות IP סטטיות.

![חיבור אוטומטי](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## אימות דו-שלבי

החל מ-DSM 4.2, Synology הציגה **אימות דו-שלבי** לשיפור האבטחה. תכונה זו דורשת קוד **סיסמה חד-פעמית (OTP)**, שנוצר על ידי אפליקציית אימות, בנוסף לפרטי ההתחברות הרגילים שלך. אם הפעלת אימות דו-שלבי, לאחר הזנת שם המשתמש והסיסמה, תצטרך גם להזין את ה-OTP כדי להתחבר להפעלת ה-DSM שלך.

שים לב, ברגע שההפעלה שלך פגה, יהיה צורך לאשר מחדש את האפליקציה באופן ידני. לאישור מחדש:

1. עבור ללשונית **חיבורים** באפליקציה.
2. הקש על כפתור **עוד פעולות** ליד שם השרת.
3. בחר **הגדרות** מהתפריט כדי להזין את קוד האימות החדש ולהשלים את תהליך האישור מחדש.

זה מבטיח שגם אם אתה ניגש ל-NAS שלך מרשת לא מהימנה, הנתונים שלך נשארים מאובטחים.

## שלב 6: ניווט והשמעת מוזיקה

1. לאחר החיבור, המכשיר יופיע ברשימת **המכשירים המחוברים**.

![מכשירים מחוברים](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. נווט לתיקיית **המוזיקה** והקש על כל קובץ שמע כדי להתחיל בהשמעה.

![השמעת מוזיקה](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## שלב 7: הוספת תיקיית ענן מחוברת לספריית המוזיקה

1. פתח את קטע **ספריית המוזיקה** באפליקציה.
2. בחר **הוסף מוזיקה** ובחר **חיבורים**.
3. בחר את שרת ה-NAS המחובר ובחר את תיקיית **המוזיקה**. הקש **בוצע**.
4. האפליקציה תסרוק את תיקיית המוזיקה ותוסיף קבצי שמע נתמכים לספריית המוזיקה. מטאדאטה ייטען והרצועות שלך ייקובצו לפי אלבום, אמן וז'אנר.

## סיכום

על ידי ביצוע שלבים אלו, תוכל בקלות להגדיר חיבור ב-Synology NAS שלך ולהזרים את כל ספריית המוזיקה שלך ל-iPhone או Mac באמצעות Evermusic או Flacbox. בין אם אתה בבית או בדרכים, תהנה מגישה חלקה ואיכותית לרצועות האהובות עליך מכל מקום באמצעות QuickConnect. נצל את הגמישות והנוחות שאפליקציות אלו מציעות, והתחל לנהל את אוסף המוזיקה שלך בקלות בכל המכשירים שלך.

עם גישה מרחוק מאובטחת דרך QuickConnect ותמיכה במגוון רחב של פורמטי שמע, לעולם לא תהיה רחוק מהמוזיקה שלך. כעת, הקבצים המאוחסנים ב-NAS שלך נמצאים במרחק הקשה אחת!

## שאלות נפוצות

{{% details title="מה ההבדל בין חיבור ידני ל-QuickConnect?" closed="true" %}}
חיבור ידני משתמש בכתובת ה-IP והפורט של ה-NAS, שעובד ברשת המקומית שלך. QuickConnect משתמש בשירות הממסר של Synology ליצירת חיבור מכל מקום דרך האינטרנט, ללא העברת פורטים.
{{% /details %}}

{{% details title="האם אוכל להזרים מוזיקה מ-Synology NAS מחוץ לרשת הביתית שלי?" closed="true" %}}
כן. הפעל QuickConnect ב-Synology NAS שלך והשתמש במזהה QuickConnect ב-Evermusic או Flacbox כדי להזרים מוזיקה מכל מקום עם חיבור לאינטרנט.
{{% /details %}}

{{% details title="אילו פורמטי שמע נתמכים בהזרמה מ-Synology NAS?" closed="true" %}}
Evermusic ו-Flacbox תומכים ב-FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD ופורמטים רבים נוספים. כל הפורמטים הנתמכים עובדים בהזרמה מ-Synology NAS.
{{% /details %}}

{{% details title="האם אני צריך אימות דו-שלבי כדי להתחבר?" closed="true" %}}
לא, אימות דו-שלבי הוא אופציונלי. עם זאת, אם הפעלת אימות דו-שלבי ב-Synology DSM שלך, האפליקציה תבקש סיסמה חד-פעמית בעת ההתחברות. תצטרך לאשר מחדש כאשר ההפעלה פגה.
{{% /details %}}

{{% details title="האם עלי להשתמש ב-API המקורי של Synology, WebDAV או SMB כדי להתחבר?" closed="true" %}}
ה-API המקורי של Synology עם QuickConnect הוא הבחירה הטובה ביותר לגישה מרחוק. לשימוש ברשת מקומית, SMB הוא בדרך כלל האפשרות המהירה ביותר. WebDAV עובד היטב לגישה מקומית ומרחוק. Evermusic ו-Flacbox תומכים בשלושת הפרוטוקולים.
{{% /details %}}
