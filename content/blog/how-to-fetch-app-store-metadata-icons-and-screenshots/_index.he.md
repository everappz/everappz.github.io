---
title: "איך לשלוף נתוני App Store, אייקונים וצילומי מסך בחינם"
date: 2026-06-13
description: "מדריך שלב אחר שלב לשליפת מטא-נתונים, אייקון, צילומי מסך ופרטי App Store מקומיים של כל אפליקציית iOS באמצעות AppLookup.pro, כלי דפדפן חינמי המבוסס על iTunes Search API הרשמי."
keywords: [
  "מטא-נתונים app store", "שליפת נתוני app store", "הורדת אייקון app store",
  "הורדת צילומי מסך app store", "כלי חיפוש app store", "itunes search api",
  "מחלץ מטא-נתוני אפליקציה", "מטא-נתוני אפליקציית iOS", "כלי app store api חינמי",
  "הורדת אייקון אפליקציה ברזולוציה גבוהה", "מחקר מתחרים app store",
  "נתוני app store מקומיים", "חיפוש app store לפי מדינה", "כלי מחקר aso חינמי"
]
tags: [
  "מטא-נתוני App Store", "חיפוש אפליקציות", "iTunes Search API",
  "הורדת אייקון אפליקציה", "צילומי מסך אפליקציה", "מחקר ASO"
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

## קבלו נתוני App Store בשניות

**גרסה קצרה:** [AppLookup.pro](https://applookup.pro) הוא כלי חינמי ששולף נתונים ציבוריים עבור כל אפליקציית iOS, iPadOS, macOS או tvOS. אתם מקבלים את הכותרת, התיאור, מה חדש, גרסה, מחיר, דירוגים, אייקון אפליקציה, צילומי מסך, מכשירים נתמכים ותגובת iTunes API גולמית. לכל שדה יש כפתור העתקה בלחיצה אחת. פתחו את האתר, הדביקו קישור App Store או הקלידו את שם האפליקציה, וקיבלתם את הנתונים.

השתמשו בו עבור:

- **מחקר ASO.** ראו כיצד האפליקציות המובילות כותבות את הכותרות, כותרות המשנה, התיאורים ומילות המפתח שלהן.
- **מעקב אחר מתחרים.** בדקו עדכוני גרסה, דירוגים ומחירים בשווקים שונים.
- **הורדת נכסים.** שמרו את אייקון האפליקציה הרשמי וצילומי מסך בגודל מלא בקובץ ZIP אחד.
- **בדיקות לוקליזציה.** השוו תיאור, מה חדש וצילומי מסך ביותר מ-40 מדינות App Store.
- **בדיקת API.** העתיקו את ה-JSON הגולמי של iTunes Search API ישירות לקוד שלכם או ל-Postman.

## מה זה AppLookup.pro?

[AppLookup.pro](https://applookup.pro) הוא כלי חינמי לחיפוש App Store המבוסס על דפדפן. הוא רץ לחלוטין על המכשיר שלכם. כל תוצאה מגיעה ישירות מ-[iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) הרשמי של Apple. ללא scraping. ללא הרשמה. ללא מעקב.

### מה אתם מקבלים

- **חיפוש לפי שם אפליקציה או כתובת App Store.** השלמה אוטומטית מציגה תוצאות חיות תוך כדי הקלדה.
- **יותר מ-40 חנויות לפי מדינה.** עברו בין ארה'ב, בריטניה, יפן, גרמניה, צרפת, ברזיל ועוד.
- **מטא-נתונים מלאים.** כותרת, כותרת משנה, מפתח, bundle ID, גרסה, מחיר, גודל קובץ, דירוגים, תאריך השקה, דירוג תוכן, שפות ומכשירים נתמכים.
- **נכסים ברזולוציה גבוהה.** אייקוני אפליקציה וצילומי מסך עבור iPhone, iPad, macOS ו-Apple TV.
- **הורדת ZIP בכמות גדולה.** קבלו כל אייקון או כל צילום מסך בארכיון אחד.
- **JSON גולמי של iTunes API.** התגובה המדויקת מ-Apple, מוכנה להעתקה.
- **כפתורי העתקה בכל שדה.** לחיצה אחת מעבירה את הערך ללוח שלכם.

## כיצד להשתמש ב-AppLookup.pro שלב אחר שלב

### שלב 1. הזינו את שם האפליקציה או הדביקו כתובת App Store

פתחו את [applookup.pro](https://applookup.pro) והתחילו להקליד את שם האפליקציה. השלמה אוטומטית מציגה תוצאות App Store חיות תוך כדי הקלדה.

תוכלו גם להדביק קישור App Store ישיר כמו `https://apps.apple.com/us/app/instagram/id389801252` או רק את מזהה האפליקציה. הכלי מחלץ את המזהה עבורכם. הוא גם מטפל בכתובות הפניית Google.

![הזינו שם אפליקציה או כתובת App Store ב-AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### שלב 2. שלפו את פרטי האפליקציה והורידו את האייקון

לחצו על **Lookup** או על Enter. הכלי קורא ל-iTunes Search API הרשמי ומציג את אייקון האפליקציה, שם המפתח, הדירוג, הגרסה והמחיר בפחות משנייה.

גללו לסעיף **App Icon**. כל גודל אייקון ש-Apple מחזירה מופיע ככרטיס. לכל כרטיס יש:

- **Direct Link.** פותח את התמונה בגודל מלא בלשונית חדשה.
- **Download.** שומר את הקובץ במחשב שלכם.

השתמשו ב-**Download All Icons (ZIP)** כדי להשיג כל גודל אייקון בארכיון אחד. אותו דבר נכון לצילומי מסך: לכל סעיף פלטפורמה יש כפתור **Download All (ZIP)** משלו.

![הורידו אייקוני אפליקציה וצילומי מסך מ-AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### שלב 3. קראו את פרטי האפליקציה והעתיקו כל שדה

גללו ל-**App Details**. תראו bundle ID, גרסה, מחיר, גודל קובץ, מערכת הפעלה מינימלית, תאריך השקה, תאריך עדכון אחרון, דירוג תוכן, ז'אנרים, מזהי ז'אנר, שפות, מוכר, מזהה אמן ומזהה רצועה.

הקישו על כפתור **Copy** בכל כרטיס. הערך נכנס ללוח שלכם והכפתור מציג סימן ירוק 'Copied'.

אותו דבר עובד עבור **Description**, **What's New** ו-**Supported Devices**. סעיפים אלה ניתנים לגלילה כך שתוכלו לקרוא את הטקסט המלא בלי לאבד את המקום שלכם, וכפתור Copy שם את כל השדה בלוח.

![צפו בפרטי App Store מלאים והעתיקו כל שדה בלחיצה אחת](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### שלב 4. צפו בתגובת ה-API הגולמית של App Store

צריכים את ה-JSON המדויק ש-Apple מחזירה? גללו ל-**Raw API Response**. תוכן ה-iTunes Search API המלא מוצג בצופה הניתן לגלילה עם כפתור **Copy** למעלה. לחיצה אחת מעתיקה את כל אובייקט ה-JSON.

ה-**iTunes Lookup URL** מוצג ממש מעליו. הדביקו אותו ב-Postman, curl או בדפדפן שלכם כדי לשחזר את אותה בקשה.

![צפו והעתיקו את תגובת ה-JSON הגולמית של iTunes Search API](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### שלב 5. שנו את המדינה כדי לראות את הגרסה המקומית

מטא-נתוני App Store משתנים לפי מדינה. אותה אפליקציה בדרך כלל יש לה כותרת, כותרת משנה, תיאור, צילומי מסך ומחיר שונים בכל שוק.

בחרו מדינה מהתפריט הנפתח למעלה. הכתובת בתיבת הקלט מתעדכנת אוטומטית. לחצו שוב על **Lookup** כדי לשלוף שוב את האפליקציה בשוק זה.

זוהי הדרך המהירה ביותר לבדוק כיצד מתחרה מציג את האפליקציה שלו ביפן, גרמניה, ברזיל או כל אחת מיותר מ-40 המדינות הנתמכות.

![עברו בין חנויות מדינה כדי לראות מטא-נתוני App Store מקומיים](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### שלב 6. העתיקו את המטא-נתונים המקומיים

לאחר שתוצאת המדינה נטענה, כל שדה עובד באותה צורה. הקישו על **Copy** בתיאור, במה חדש, בשם האפליקציה, במפתח, ב-bundle ID או בכל כרטיס פרטים כדי ללכוד את הטקסט המקומי.

זה הופך את היצירה של גליונות אלקטרוניים להשוואה זה לצד זה לקלה, או הזנת טקסט מקומי לסקירת תרגום.

![העתיקו תיאור ומטא-נתוני App Store מקומיים בלחיצה אחת](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## מי משתמש ב-AppLookup.pro

- **מפתחים עצמאיים** שעושים מחקר ASO לפני השקה.
- **צוותי ASO ושיווק** שעוקבים אחרי עדכוני מתחרים ותמחור.
- **מעצבים** שלוקחים את אייקון האפליקציה הרשמי ברזולוציה גבוהה וצילומי מסך לערכות עיתונות ומקרי בוחן.
- **צוותי לוקליזציה** שבודקים אילו שווקים מכוסים והיכן עדיין נשלח הטקסט האנגלי המוגדר כברירת מחדל.
- **מהנדסי Backend ו-QA** הבודקים אינטגרציות של iTunes Search API מבלי לכתוב scraper.
- **כותבים ובלוגרים** הזקוקים לאייקון האפליקציה הרשמי וכמה צילומי מסך לפוסט.

## פרטיות וכתב ויתור

AppLookup.pro רץ בדפדפן שלכם. אין כניסה. אין מעקב. אין רישום בשרת של האפליקציות שאתם מחפשים. בקשות עוברות ישירות מהדפדפן שלכם ל-[iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) של Apple.

כלי זה מיועד **למטרות חינוכיות ומחקריות בלבד**. כל הנתונים נשלפים מה-API הציבורי הרשמי של Apple ונשארים רכושם של Apple Inc. ושל מפרסמי האפליקציות הרשומים. השימוש בכלי כפוף ל-[תנאים והגבלות של Apple Media Services](https://www.apple.com/legal/internet-services/terms/site.html). אנא כבדו את מגבלות הקצב של Apple ואל תפיצו מחדש נכסים המוגנים בזכויות יוצרים.

## נסו עכשיו

אינכם זקוקים למפתח API, חשבון מפתח או תוכנית בתשלום כדי לבדוק נתוני App Store. פתחו את [applookup.pro](https://applookup.pro), הדביקו כל כתובת App Store, ויהיו לכם המטא-נתונים, האייקונים וה-JSON הגולמי בשניות.

## קוד פתוח

AppLookup.pro הוא קוד פתוח. דוחות באגים, הוספות מדינה ו-pull requests מוזמנים.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro ב-GitHub" icon="github" tag="קוד פתוח" >}}
{{< /cards >}}

---

## שאלות נפוצות

{{% details title="האם AppLookup.pro באמת חינמי?" closed="true" %}}
כן. AppLookup.pro הוא 100 אחוז חינמי וקוד פתוח. הוא רץ בדפדפן שלכם. אין הרשמה, אין שכבה בתשלום ואין מגבלת שימוש מעבר למגבלות iTunes Search API של Apple עצמה.
{{% /details %}}

{{% details title="מאיפה הנתונים מגיעים?" closed="true" %}}
כל תוצאה נשלפת בזמן אמת מ-[iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) הרשמי של Apple. הכלי לא עושה scraping לדפי App Store ולא שומר תגובות במטמון על שום שרת.
{{% /details %}}

{{% details title="האם אפשר להוריד את אייקון האפליקציה ברזולוציה גבוהה?" closed="true" %}}
כן. סעיף **App Icon** מציג כל כתובת אייקון ש-Apple מחזירה. לכל כרטיס יש Direct Link וכפתור Download, וכפתור Download All Icons ZIP אורז אותם בארכיון אחד.
{{% /details %}}

{{% details title="האם אפשר להוריד את כל צילומי המסך של App Store בבת אחת?" closed="true" %}}
כן. לכל סעיף צילומי מסך (iPhone, iPad, macOS ו-Apple TV) יש כפתור **Download All (ZIP)** שאורז כל צילום מסך ברזולוציה מלאה.
{{% /details %}}

{{% details title="איך אני רואה איך אפליקציה נראית במדינה אחרת?" closed="true" %}}
בחרו מדינה בתפריט הנפתח בראש הדף. יותר מ-40 חנויות נתמכות. לחצו שוב על **Lookup** והכלי שולף שוב את האפליקציה עבור אותה מדינה, ומציג את הכותרת, התיאור, צילומי המסך, מה חדש והמחיר המקומיים.
{{% /details %}}

{{% details title="האם אפשר להעתיק שדות בודדים כמו bundle ID או תאריך השקה?" closed="true" %}}
כן. לכל שדה טקסט בתוצאה יש כפתור Copy משלו: שם אפליקציה, מפתח, תיאור, מה חדש, bundle ID, גרסה, מחיר, גודל קובץ, מערכת הפעלה מינימלית, תאריך השקה, דירוג תוכן, שפות, מכשירים נתמכים ו-JSON גולמי.
{{% /details %}}

{{% details title="האם AppLookup.pro עובד עבור כל אפליקציית iOS?" closed="true" %}}
הוא עובד עבור כל אפליקציה הרשומה בפומבי בלפחות מדינת App Store אחת ומוחזרת על ידי iTunes Search API. אפליקציות לא רשומות, שהוסרו או מופצות באופן ארגוני לא יופיעו.
{{% /details %}}

{{% details title="האם הוא תומך באפליקציות macOS ו-Apple TV?" closed="true" %}}
כן. אם לאפליקציה יש צילומי מסך של macOS או Apple TV בתגובת iTunes Search API, AppLookup.pro מציג אותם בפאנל ניתן לגלילה משלהם עם כפתורי הורדה.
{{% /details %}}

{{% details title="האם אפשר להשתמש ב-JSON הגולמי בקוד שלי?" closed="true" %}}
כן. סעיף Raw API Response מציג את ה-JSON המדויק ש-Apple מחזירה. העתיקו אותו ל-Postman, מבחן יחידה או צינור backend. אנא כבדו את תנאי ה-API של Apple ומגבלות קצב סבירות.
{{% /details %}}

{{% details title="האם בטוח להדביק כתובות App Store בכלי?" closed="true" %}}
כן. הכתובת מנותחת בדפדפן שלכם. השיחת הרשת היוצאת היחידה היא חיפוש ל-iTunes Search API של Apple.
{{% /details %}}

{{% details title="מה ההבדל בין AppLookup.pro ל-AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) נועד לקריאת מטא-נתוני App Store מכל אפליקציה שפורסמה: מחקר מתחרים, הורדת נכסים, בדיקות לוקליזציה. [AppKeywords.pro](https://appkeywords.pro) נועד לכתיבת מטא-נתוני App Store עבור האפליקציה שלכם: אופטימיזציה של כותרת, כותרת משנה ומילות מפתח עם תמיכה ב-Fastlane. שני הכלים עובדים היטב יחד.
{{% /details %}}
