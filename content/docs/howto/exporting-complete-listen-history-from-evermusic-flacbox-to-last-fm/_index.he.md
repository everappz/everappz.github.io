---
title: "ייצוא היסטוריית ההאזנה המלאה מ-Evermusic ו-Flacbox ל-Last.fm"
date: 2024-01-30
description: "למדו כיצד לייצא את היסטוריית המוזיקה שלכם מ-Evermusic ו-Flacbox ולהעלות אותה ל-Last.fm באמצעות קבצי CSV וכלי Last.fm Scrubbler עבור Windows."
keywords: ["evermusic", "flacbox", "lastfm", "היסטוריית מוזיקה", "scrobbling", "ייצוא שירים", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "עדכונים אחרונים", "lastfm", "ייצוא", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**תקציר:** ייצאו את היסטוריית ההאזנה שלכם מ-Evermusic או Flacbox כקובץ CSV, ואז העלו אותו ל-Last.fm באמצעות הכלי החינמי Last.fm-Scrubbler-WPF ב-Windows. Scrobbling אוטומטי זמין גם באופן מובנה בשתי האפליקציות.

**עדכון:** Scrobbling אוטומטי זמין כעת! למידע נוסף כאן: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling הוא דרך פשוטה לשמור אוטומטית פרטים בסיסיים כמו שם השיר והאמן של השיר שאתם מנגנים כרגע בשירות מקוון. מאוחר יותר, תוכלו לעיין בהיסטוריית ההאזנה שלכם.

[Last.fm](https://www.last.fm/home), המופעל על ידי מערכת המלצות מוזיקה בשם Audioscrobbler, מציע שירות זה בחינם. הוא יוצר פרופיל מפורט של הטעם המוזיקלי שלכם על ידי רישום השירים שאתם מאזינים להם, בין אם מתחנות רדיו באינטרנט, המחשב שלכם או מכשירי מוזיקה ניידים שונים. תוכלו לבקר באתר מאוחר יותר כדי לקבל המלצות לאמנים או אלבומים חדשים שמתאימים לטעם המוזיקלי שלכם.

תוכלו להעלות את היסטוריית ההאזנה שלכם ל-[Last.fm](http://Last.fm) מאפליקציות Evermusic ו-Flacbox באמצעות כלי חינמי, ואנחנו נדריך אתכם כיצד לעשות זאת.

פתחו את הקטע 'ספריית מוזיקה' באפליקציה וגללו לקטע 'גישה מהירה'. הקישו על פריט התפריט 'עדכונים אחרונים'.

![מסך ספריית המוזיקה](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

במסך 'עדכונים אחרונים' הקישו על כפתור 'עוד' בפינה הימנית העליונה כדי להפעיל את תפריט 'עוד פעולות'. הקישו על פריט התפריט 'ייצוא רשימת שירים'.

![מסך עדכונים אחרונים](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

במסך 'בחירת פורמט קובץ' יש לכם אפשרות לבחור את פורמט קובץ היעד. אפשרויות זמינות - CSV, TXT, M3U.

![מסך בחירת פורמט קובץ](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: ראשי תיבות של ערכים מופרדים בפסיקים, מושלם לארגון הנתונים שלכם בפורמט טבלה מסודר. בקובץ היעד, תמצאו פרמטרים כמו שם האמן, שם האלבום, שם השיר, חותמת זמן (הזמן שבו האזנתם לשירים), שם אמן האלבום ומשך השיר.

TXT: כאן אנחנו מדברים על קובץ טקסט פשוט. הוא פשוט וישיר, עם פרמטרים הכוללים שם האמן, שם האלבום, שם השיר ומשך.

M3U: פורמט זה הוא למעשה הבחירה המובילה ליצירת רשימות השמעה. הוא נהדר כי אתם יכולים לייצא את רשימת השירים שלכם וליהנות מהשירים בכל מכשיר, גם אם אין לכם את הקבצים המקוריים (בתנאי שתבחרו באפשרות URL מוחלט לקבצי המדיה). בקובץ הפלט, תמצאו פרמטרים כמו משך, שם האמן, שם השיר ומיקום קובץ המדיה.

למשימה שלנו, בחירת CSV היא הדרך הנכונה. נשתמש בקובץ זה עם התוכנה החינמית Last.fm-Scrubbler-WPF כדי להעלות את היסטוריית ההאזנה שלנו לשירות [Last.fm](http://Last.fm). פשוט בחרו CSV ולחצו על כפתור 'ייצוא'.

![מסך ייצוא הושלם](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

לאחר השלמת הייצוא, פשוט הקישו על כפתור 'הצג קובץ', והאפליקציה תחשוף את הקובץ שנוצר בתיקיית המסמכים שלכם. לאחר מכן, הקישו על כפתור 'עוד פעולות' ליד שם הקובץ ובחרו באפשרות 'פתח ב' מהתפריט. הצעד הבא שלנו הוא להעתיק את הקובץ המיוצא למחשב השולחני שלכם. תוכלו לעשות זאת בקלות על ידי בחירת אפשרות AirDrop מתפריט 'פתח ב'.

![עוד פעולות לקובץ המיוצא](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

בהמשך, נשתמש בלקוח [Last.FM](http://Last.FM) חינמי בקוד פתוח שזמין רק בפלטפורמת Windows. לקוח זה מאפשר לכם לעדכן ביעילות את היסטוריית ההאזנה שלכם ב-[Last.FM](http://Last.FM) באמצעות קובץ ה-CSV שזה עתה ייצאנו.

כעת, אם אינכם משתמשים כרגע במחשב Windows, אל דאגה. תוכלו לגשת ללקוח זה על ידי התקנת VirtualBox ב-Mac שלכם ושימוש בקובץ התמונה הרשמי של סביבת הפיתוח של Windows.

הנה מה שעליכם לעשות:

- התקינו VirtualBox מהקישור הבא: [הורדת VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- הורידו והתקינו את סביבת הפיתוח של Windows מקישור זה: [סביבת פיתוח Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

במחשב Windows שלכם (או באפליקציית VirtualBox עם תמונת פיתוח Windows) הורידו והתקינו את [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - תוכנה חינמית בקוד פתוח הזמינה ב-GitHub. בדקנו את גרסה 1.28 שתוכלו להוריד כאן: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![דף הורדת Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

תחת הקטע 'Assets' הקישו על [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) כדי להוריד את ארכיון ההתקנה. חלצו את הקובץ שהורד ופתחו את התיקייה שחולצה.

- חשוב

אפליקציה זו עדיין בגרסת בטא. יוצרי האפליקציה לא ביצעו הרבה בדיקות. הם ממליצים לנסות לעשות scrobble לחשבון בדיקה קודם ולראות אם הדברים שאתם רוצים לעשות להם scrobble עובדים כראוי. במיוחד אם אתם עושים scrobble להרבה שירים בבת אחת. אנא היזהרו עם החשבונות שלכם.

הפעילו Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

במסך הראשי של האפליקציה, פשוט הקישו על 'לא מחובר', הממוקם בפינה השמאלית התחתונה, כדי להפעיל את מסך 'הוסף חשבון'.

![מסך הוספת חשבון](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

הזינו את פרטי ההתחברות שלכם.

![מסך הזנת פרטי התחברות](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

הקישו על כפתור 'התחברות' כדי להוסיף את חשבונכם.

![הקישו על כפתור ההתחברות כדי להוסיף את חשבונכם.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

פתחו את לשונית 'File Parse Scrobbler' כדי להתחיל לייבא קובץ CSV מאפליקציית Evermusic.

![פתחו את לשונית File Parse Scrobbler כדי להתחיל לייבא קובץ CSV מאפליקציית Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

בחרו 'Parser: CSV' והקישו על כפתור 'הגדרות'.

במסך הבא, תוכלו לבחור את סדר הפרמטרים בקובץ ה-CSV שלכם.

שדות בודדים יכולים להיות מוקפים במרכאות וחייבים להיות מוקפים במרכאות אם השדה מכיל אחד מהמפרידים שהוגדרו. לדוגמה:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

אז השאירו את כל ההגדרות בברירת מחדל, הדבר היחיד שצריך לשנות הוא להפעיל את תיבת הסימון בשדה 'Has Fields Enclosed In Quotes'.

הקישו על 'שמור וסגור' כדי להחיל שינויים.

![בחרו את סדר הפרמטרים בקובץ ה-CSV שלכם.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

ל-Scrobbling ניתוח קבצים יש שני מצבים. ניתן לשנות אותם עם תיבת הרשימה הנפתחת 'Scrobbling Mode'.

מצב רגיל: במצב זה, השירים יעברו scrobble עם חותמת הזמן מה-scrobble שנותח. רק scrobbles חדשים מ-14 יום ניתנים ל-scrobble.

מצב ייבוא: במצב זה, השירים יעברו scrobble עם חותמת זמן מחושבת מ'זמן הסיום' והמשך שנבחר בין כל שיר. זה מאפשר scrobbling של השירים גם אם חותמת הזמן של ה-scrobble שנותח ישנה מ-14 יום. לכן השיר הראשון (העליון) בקובץ ה-CSV יעבור scrobble עם 'זמן הסיום'.

בחרו קובץ CSV שנוצר קודם לכן מאפליקציית Evermusic בשדה 'File:' והקישו על 'Parse'. במקרים מסוימים, ייתכן שתראו התראת שגיאה שאומרת שחלק מה-scrobbles לא ניתנים לניתוח. זה בסדר אם יש לכם כמה שירים ללא מטא-נתונים מלאים כמו שם האמן.

![חלק מה-scrobbles לא ניתנים לניתוח](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

הקישו על כפתור 'בחר הכל' כדי לבחור את כל השירים שנותחו.

![הקישו על כפתור בחר הכל כדי לבחור את כל השירים שנותחו.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

הקישו על כפתור 'תצוגה מקדימה' כדי לבדוק את כל השינויים שיפורסמו לשרת.

![הקישו על כפתור תצוגה מקדימה כדי לבדוק את כל השינויים שיפורסמו לשרת.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

הקישו על כפתור 'Scrobble' כדי להעלות את כל השינויים לשרת.

![הקישו על כפתור Scrobble כדי להעלות את כל השינויים לשרת.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

בעבר ל-Last.fm-Scrubbler-WPF לא היה מגבלת scrobbles יומית. זה השתנה כעת מכיוון שחלק מהאנשים השתמשו ב-Scrubbler כדי לעשות scrobble לכל כך הרבה שירים שזה גרם לבעיות בדף Last.fm. מגבלת ה-scrobbling היא כרגע 2800 scrobbles ביום. כשתנסו לעשות scrobble ליותר מזה תקבלו הודעת שגיאה. ישנן תוכניות להוסיף 'תור scrobbling', כך שאם אתם צריכים לעשות scrobble ליותר מ-2800 שירים, הם יתווספו לתור ויעברו scrobble אוטומטית לאחר זמן מה. תוכלו לבדוק כמה scrobbles נותרו לכם בתצוגת בחירת המשתמש.

לאחר שכל הרשומות הועלו בהצלחה לשרת, תראו הודעה בתחתית חלון האפליקציה המאשרת: 'השירים שנבחרו עברו scrobble בהצלחה.'

![השירים שנבחרו עברו scrobble בהצלחה.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

כעת תוכלו לפתוח את הפרופיל שלכם בדף [Last.fm](http://Last.fm) ולבדוק את כל השינויים.

![הפרופיל שלכם בדף Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## שאלות נפוצות

{{% details title="האם אני יכול לעשות scrobble אוטומטית ללא ייצוא קבצי CSV?" closed="true" %}}
כן. גם Evermusic וגם Flacbox תומכים כעת ב-scrobbling אוטומטי ל-Last.fm. ראו את המדריך: [כיצד לעשות scrobble ל-Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="מה אם ה-CSV שלי מכיל שירים ישנים מ-14 יום?" closed="true" %}}
השתמשו במצב ייבוא ב-Last.fm-Scrubbler-WPF. הוא מחשב מחדש חותמות זמן מזמן הסיום, ומאפשר לכם לעשות scrobble לשירים ללא קשר לתאריך המקורי שלהם.
{{% /details %}}

{{% details title="אין לי מחשב Windows. האם אני עדיין יכול להשתמש ב-Last.fm-Scrubbler?" closed="true" %}}
כן. התקינו VirtualBox ב-Mac שלכם והורידו את תמונת סביבת הפיתוח החינמית של Windows מ-Microsoft. הפעילו את Last.fm-Scrubbler-WPF בתוך המכונה הווירטואלית.
{{% /details %}}

{{% details title="למה חלק מה-scrobbles לא מנותחים?" closed="true" %}}
שירים שחסרים להם מטא-נתונים חיוניים (כמו שם האמן) לא ניתנים לניתוח. זה צפוי ואינו משפיע על שירים אחרים בקובץ.
{{% /details %}}

{{% details title="האם יש מגבלת scrobbling יומית?" closed="true" %}}
כן. Last.fm-Scrubbler-WPF מאפשר עד 2,800 scrobbles ביום. אם אתם צריכים לעשות scrobble ליותר, חלקו את התהליך על פני מספר ימים.
{{% /details %}}
