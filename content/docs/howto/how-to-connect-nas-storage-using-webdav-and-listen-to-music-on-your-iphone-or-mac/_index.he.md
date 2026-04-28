---
title: "כיצד לחבר אחסון NAS באמצעות WebDAV ולהאזין למוזיקה ב-iPhone או Mac"
date: 2024-07-28
description: "למדו כיצד להגדיר WebDAV ב-Synology NAS ולהזרים מוזיקה ל-iPhone או Mac באמצעות Evermusic או Flacbox. עקבו אחר המדריך שלנו צעד אחר צעד."
keywords: ["חיבור nas", "webdav synology", "הזרמת מוזיקה nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["מוזיקה", "הזרמה", "אחסון", "nas", "חיבור", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**בקצרה:** התקינו והפעילו WebDAV ב-Synology NAS, הגדירו הרשאות תיקייה משותפת, ואז התחברו מ-Evermusic או Flacbox באמצעות כתובת ה-IP של ה-NAS ופורט WebDAV (ברירת מחדל 5005/5006). תוכלו להזרים ולנהל את כל ספריית המוזיקה שלכם מבלי להעתיק קבצים למכשיר.

גלו כיצד לחבר את אחסון ה-NAS שלכם באמצעות WebDAV ולהזרים בקלות את ספריית המוזיקה שלכם ל-iPhone או Mac. WebDAV (Web-based Distributed Authoring and Versioning) הוא פרוטוקול המאפשר לכם לנהל ולשתף קבצים דרך האינטרנט. על ידי הגדרת WebDAV ב-NAS שלכם, תוכלו לגשת לאוסף המוזיקה שלכם ולהזרים אותו, ולהבטיח שהשירים האהובים עליכם תמיד בהישג יד.

במדריך זה, נראה לכם כיצד להגדיר חיבור WebDAV באחד משרתי ה-NAS הפופולריים ביותר, Synology NAS. עקבו אחר הצעדים הפשוטים שלנו להגדרת WebDAV ב-Synology NAS, ותוכלו לעיין, להזרים ולנהל את ספריית המוזיקה שלכם ישירות מה-iPhone או Mac.

## שלב 1: התקנת WebDAV ב-Synology NAS

1. התחברו ל-Synology NAS ופתחו את **מרכז החבילות**.
2. חפשו "webdav" והתקינו את חבילת WebDAV אם היא עדיין לא מותקנת. פתחו את שרת WebDAV כדי להגדיר אותו.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="התקנת WebDAV ב-Synology" width="600" >}}

## שלב 2: הגדרת שרת WebDAV

1. בדף הגדרות WebDAV, סמנו את התיבות עבור **הפעלת HTTP**, **הפעלת HTTPS**, **הפעלת WebDAV אנונימי** ו-**הפעלת DavDepthInfinity**.
2. לחצו על **החל** כדי לשמור את השינויים. שימו לב למספרי הפורטים לחיבורי HTTP ו-HTTPS, שהם 5005 ו-5006 כברירת מחדל.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="הגדרת פרמטרי WebDAV" width="600" >}}

## שלב 3: הגדרת הרשאות תיקייה משותפת

1. פתחו את **לוח הבקרה** ועברו לסעיף **תיקייה משותפת**.
2. בחרו את תיקיית **מוזיקה** ולחצו על **עריכה**.
3. בלשונית **הרשאות**, הגדירו את ההרשאות. הפעילו גישת אורח עם קריאה בלבד אם אתם צריכים רק להאזין למוזיקה, או קריאה/כתיבה אם אתם צריכים לשנות קבצים. שמרו את השינויים.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="הרשאות תיקייה משותפת" width="600" >}}

## שלב 4: מציאת כתובת IP של Synology NAS

1. פתחו את **לוח הבקרה** ועברו ללשונית **ממשק רשת**, או השתמשו בדפדפן כדי לבקר ב-[find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="מציאת כתובת IP של NAS" width="600" >}}

2. רשמו את כתובת ה-IP של Synology NAS (לדוגמה, 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="כתובת IP של Synology NAS" width="600" >}}

## שלב 5: התחברות ל-Synology NAS באמצעות Evermusic/Flacbox

1. פתחו את אפליקציית Evermusic או Flacbox ועברו ללשונית **חיבורים**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="לשונית חיבורים ב-Evermusic" width="600" >}}

2. לחיבור אוטומטי, מצאו את Synology NAS בסעיף **מכשירים זמינים** והקישו עליו כדי להתחבר.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="רשימת מכשירים זמינים" width="600" >}}

3. לחיבור ידני, בחרו **התחברות לשירות ענן** ובחרו **WebDAV**. הזינו את כתובת השרת בפורמט: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (לדוגמה, [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="הגדרת WebDAV ידנית" width="600" >}}

4. השאירו את שדות שם המשתמש והסיסמה ריקים לגישת אורח, או הזינו את פרטי ההתחברות של Synology. הקישו על **התחברות**.

## שלב 6: ניווט והשמעת מוזיקה

1. לאחר ההתחברות, המכשיר יופיע ברשימת **אביזרים מחוברים**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="מכשירים מחוברים ב-Evermusic" width="600" >}}

2. נווטו לתיקיית **מוזיקה** והקישו על כל קובץ שמע כדי להתחיל בהשמעה.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="עיון בתיקיית מוזיקה" width="600" >}}

## שלב 7: הוספת תיקיית ענן מחוברת לספריית המוזיקה

1. פתחו את סעיף **ספריית המוזיקה** באפליקציה.
2. בחרו **הוספת מוזיקה** ובחרו **חיבורים**.
3. בחרו את שרת ה-NAS המחובר ובחרו את תיקיית **מוזיקה**. הקישו על **בוצע**.
4. האפליקציה תסרוק את תיקיית המוזיקה ותוסיף קבצי שמע נתמכים לספריית המוזיקה. המטאדאטה ייטענו, והרצועות שלכם יקובצו לפי אלבום, אמן וז'אנר.

## סיכום

על ידי ביצוע צעדים אלה, תוכלו בקלות להגדיר חיבור WebDAV ב-Synology NAS ולהזרים את ספריית המוזיקה שלכם ל-iPhone או Mac באמצעות Evermusic או Flacbox. תהנו מגישה חלקה לשירים האהובים עליכם בכל עת.

## שאלות נפוצות

{{% details title="אילו מכשירי NAS תומכים ב-WebDAV?" closed="true" %}}
רוב מותגי ה-NAS הפופולריים תומכים ב-WebDAV, כולל Synology, QNAP, TrueNAS ו-Western Digital. בדקו את התיעוד של יצרן ה-NAS שלכם להוראות הגדרת WebDAV.
{{% /details %}}

{{% details title="מה ההבדל בין WebDAV ל-SMB להזרמת מוזיקה מ-NAS?" closed="true" %}}
WebDAV פועל דרך HTTP/HTTPS ומתאים יותר לגישה מרחוק דרך האינטרנט. SMB בדרך כלל מהיר יותר ברשתות מקומיות. Evermusic ו-Flacbox תומכים בשני הפרוטוקולים, אז בחרו בהתאם לצורך בגישה מקומית או מרחוק.
{{% /details %}}

{{% details title="האם אני צריך שם משתמש וסיסמה ל-WebDAV ב-Synology?" closed="true" %}}
לא, אם תפעילו גישת WebDAV אנונימית ותגדירו הרשאות אורח בתיקייה המשותפת. לאבטחה טובה יותר, תוכלו להשתמש בפרטי ההתחברות של Synology במקום.
{{% /details %}}

{{% details title="האם אפשר להזרים FLAC ופורמטים באיכות גבוהה אחרים מ-NAS דרך WebDAV?" closed="true" %}}
כן. גם Evermusic וגם Flacbox תומכים ב-FLAC, ALAC, WAV, DSD ופורמטים באיכות גבוהה אחרים בעת הזרמה מאחסון NAS דרך WebDAV.
{{% /details %}}

{{% details title="למה האפליקציה לא מוצאת את ה-NAS שלי במכשירים זמינים?" closed="true" %}}
ודאו שה-iPhone/Mac וה-NAS נמצאים באותה רשת Wi-Fi. אם הגילוי האוטומטי לא עובד, השתמשו באפשרות החיבור הידני והזינו את כתובת ה-IP של ה-NAS ופורט WebDAV ישירות.
{{% /details %}}
