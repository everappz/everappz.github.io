---
date: 2020-01-01
title: 'Flacbox'
description: "למדו כיצד להשתמש ב-Flacbox — נגן המוזיקה בענן ל-iPhone, iPad ו-Mac עם תמיכה ב-FLAC ברזולוציה גבוהה, DSD, ALAC ו-FFmpeg. חברו iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB ו-DLNA. הזרימו והורידו אודיו ברזולוציה גבוהה, ערכו מטאדטה, האזינו לספרי שמע, בצעו scrobble ל-Last.fm, השתמשו ב-Apple CarPlay ובווידג'טים של מסך הבית, והתאימו אישית את האיקולייזר ב-10 פסים."
keywords: [
  "מדריך משתמש Flacbox", "איך להשתמש ב-Flacbox", "נגן מוזיקה ברזולוציה גבוהה iPhone", "נגן FLAC iPhone",
  "נגן DSD iOS", "נגן ALAC Mac", "אפליקציית מוזיקה ללא אובדן", "נגן מוזיקה ענן iPhone",
  "נגן FLAC אופלין Mac", "מנהל ספריית מוזיקה", "עורך תגיות אודיו",
  "נגן FLAC CarPlay", "אפליקציית אודיו Chromecast", "מוזיקת AirPlay 2",
  "ווידג'טים Flacbox", "Flacbox CarPlay", "נגן מוזיקה FFmpeg iOS",
  "נגן ספרי שמע iPhone", "סימניות אודיו iOS", "אפליקציית תיקון גובה צליל",
  "קצב דגימת פלט אודיו", "DAC חיצוני iPhone", "DAC USB Mac",
  "אפליקציית Synology מוזיקה", "אפליקציית QNAP מוזיקה", "נגן מוזיקה NAS iPhone",
  "נגן מוזיקה WebDAV", "הזרמת מוזיקה SMB", "נגן מוזיקה DLNA",
  "מוזיקת iCloud Drive", "FLAC ב-Google Drive", "נגן FLAC Dropbox",
  "העברת מוזיקה Wi-Fi Drive", "יבוא רשימת השמעה M3U", "scrobbling Last.fm"
]
tags: ["flacbox", "מדריך", "רזולוציה גבוהה", "FLAC", "FFmpeg", "ענן", "CarPlay", "ווידג'טים"]
---


### ברוכים הבאים למדריך Flacbox

Flacbox הוא נגן מוזיקה ברזולוציה גבוהה ל-iPhone, iPad ו-Mac שמאפשר לכם להפוך את אחסון הענן האהוב עליכם, שרתי NAS ושרתי מדיה לשירות הסטרימינג האישי שלכם.

Flacbox מתחבר למגוון רחב במיוחד של מקורות, הכול באפליקציה אחת:

- **אחסון ענן אישי:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **שרתים מאורחים עצמאית:** Plex · Jellyfin · Emby · Subsonic (וכל שרת תואם Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (ו-ownCloud דרך ה-API המשותף) · Synology Drive · QNAP.
- **פרוטוקולי NAS ושיתוף קבצים:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (אימות בסיסמה או מפתח ציבורי) · NFS · DLNA / UPnP (השמעה והורדה). עובד עם Apple Time Capsule, Synology, QNAP, WD My Cloud, כל מארח Linux Samba / NFS / SSH, או תיקייה משותפת ב-Mac או PC Windows.
- **אחסון אובייקטים תואם S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, וכל נקודת קצה S3-API אחרת.
- **גילוי ברשת מקומית:** החלק מכשירים זמינים מפרט אוטומטית כל שירות Bonjour / mDNS ב-Wi-Fi שלכם — שרתי Plex, Jellyfin, Emby, Synology, QNAP, נתבי AirPort עם כוננים מחוברים, Time Capsule — כדי שתוכלו להתחבר בלי להקליד כתובת IP.

בעוד שרוב אפליקציות המוזיקה מסתפקות במנוע האודיו המובנה של Apple, Flacbox כולל **FFmpeg** לצד קודקים המערכת כדי שתוכלו להשמיע פורמטים שאינם נתמכים כברירת מחדל ב-iOS — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, בנוסף לפמיליה הרגילה של MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC. בשילוב עם קצב דגימת פלט אודיו שניתן להגדרה (44.1 / 48 / 64 / 88.2 / 96 kHz), פלט רב-ערוצי (Mono → 5.1 → SDDS → ITU BS.775-1), כיוון חיץ קלט/פלט ותיקון גובה צליל, Flacbox מעניק לאוהבי אודיו שליטה שרוב אפליקציות המוזיקה הצרכניות פשוט אינן מציעות.

### הנאה מסטרימינג חלק והשמעה אופלין

Flacbox מציע אגירת חיץ חכמה לסטרימינג חלק ומנהל הורדות מובנה כדי שתוכלו להוריד רשימות השמעה, אמנים, אלבומים, תיקיות או רצועות בודדות למכשיר שלכם לשימוש אופלין. כאשר האחסון מתמלא, מחקו קבצים שנשמרו במטמון בהקשה אחת והמשיכו להזרים מהענן. מצב אופלין לתיקיות, רשימות השמעה, אלבומים ואמנים גם מסנכרן אוטומטית רצועות חדשות ברגע שהן מופיעות בענן, כך שהאוסף האופלין שלכם תמיד נשאר עדכני.

### ספריית מוזיקה מאורגנת אוטומטית

כאשר אתם מייבאים רצועות אודיו, Flacbox סורק את המטאדטה שלהן ומארגן אותן לספריית מוזיקה נקייה — מקובצות לפי שירים, שירים שלא נושמעו, אלבומים, אמנים של אלבומים, אמנים, ז'אנרים ומלחינים. השתמשו בחיפוש המובנה למציאת כל דבר תוך שניות, סננו לפי מקור (ענן מקוון / אופלין / מכשיר) ובחרו בין פריסות ספרייה פשוטה / מקובצת / בלשוניות. עבור ספריות עם קומפילציות של 'אמנים שונים', Flacbox מספק תצוגות ייעודיות של כל האלבומים / אלבומים בלעדיים / אלבומים סולו כדי להציג את התוצאות הנכונות ללא רעש.

### תקנו מטאדטה ותייגו את המוזיקה שלכם

אם אתם נתקלים בתגיות פגומות או קידודים מבולגנים (בעיה נפוצה בקבצים שרופים או ישנים), עורך תגיות ה-ID3 המובנה יכול לתקן אותם — ידנית או עם חיפושים אוטומטיים של MusicBrainz. ניתן גם לנרמל קידודי תווים שבורים (מצוין לתגיות קיריליות, יפניות או סיניות שהגיעו ממחשבי Windows), לחפש עטיפת אלבום חסרה ולכתוב שינויים בחזרה לקובץ המקורי בענן אוטומטית. לעריכת אצווה מעמיקה יותר, התקינו את אפליקציית הנלווה שלנו Evertag.

### העברות קלות מ-Mac, PC או NAS

העבירו מוזיקה בין המחשב שלכם לאייפון או לאייפד באמצעות אחד מהכלים הבאים: SMB, WebDAV, DLNA, Wi-Fi Drive (גרירה ושחרור בכל דפדפן שולחן עבודה), iTunes / Finder File Sharing דרך כבל Lightning או USB-C, כוננים USB מהירים או כוננים iXpand Flash Drive. יש לכם Apple Time Capsule, WD My Cloud, Synology, QNAP או כל NAS אחר שחושף SMB / WebDAV / DLNA / FTP / SFTP? חברו אותו פעם אחת והזרימו את כל הספרייה שלכם מבלי לתפוס אחסון במכשיר.

### התאימו את הצליל שלכם עם האיקולייזר

Flacbox כולל איקולייזר 10 פסים עם פריסטים בסגנון iPod (אקוסטי, מגבר בסים, קלאסי, ריקוד, רוק, פופ, ג'אז ועוד רבים), פריאמפליפייר ואפשרות לשמור פריסטים משלכם. בין אם אתם מכוונים לזוג אוזניות IEM של שמענים, HomePod mini או סטריאו לרכב, תוכלו לעצב את הצליל בדיוק כפי שאתם רוצים.

### ידידותי לספרי שמע

Flacbox הוא נגן ספרי שמע מצוין — מספר סימניות לרצועה, מהירות השמעה עדינה (0.02× עד 3.00×), המשך השמעה לחידוש בדיוק במקום שהפסקתם, כפתורי דילוג הניתנים להתאמה אישית ומעצר שינה שמתמוסס בעדינות בשעת השינה. סמני פרקים M4B וקבצים ארוכים נתמכים באופן מלא.

### הזרימו בכל מקום — כולל ברכב ועל מסך הבית

הזרימו מוזיקה ל-Apple TV / HomePod דרך AirPlay 2, שלחו אותה לרמקולי Google Chromecast ולטלוויזיות עם Cast, וקחו הכול לדרך עם Apple CarPlay. השתמשו בווידג'טים של מסך הבית ב-iPhone וב-iPad כדי לראות את הרצועה המושמעת כעת במבט חטוף, ו-scrobbling של Last.fm כדי לשמור את היסטוריית ההאזנה שלכם בין אפליקציות.

### פרטיות ואבטחה

Flacbox משתמש אך ורק ב-SDK רשמיים ובהתחברויות מבוססות OAuth מכל ספק ענן — הסיסמה שלכם לעולם אינה מגיעה לאפליקציה. אסימוני גישה מאוחסנים מוצפנים ב-Keychain של iOS, כל ההעברות מוגנות ב-TLS, וביטול הגישה בחשבון הענן שלכם או הסרת Flacbox מהמכשיר מוחק הכל מיידית. הגנו על הספרייה שלכם עם קוד גישה אופציונלי לשכבת פרטיות נוספת.

### תחילת עבודה עם Flacbox

מדריך זה מלווה אתכם דרך כל חלק של Flacbox ב-iPhone, iPad ו-Mac — החל מחיבור שירותי ענן, ארגון הספרייה, העברת קבצים וניהול רשימות השמעה, ועד לכיוון עדין של האיקולייזר והגדרת מנוע האודיו. השתמשו בכרטיסים למטה כדי לעבור ישירות לחלק הרלוונטי.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="ניווט" subtitle="סרגל לשוניות ב-iPhone, תפריט שמאלי ב-iPad וב-Mac, מיני נגן, ווידג'טים, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="חיבורים" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="ספריית מוזיקה" subtitle="שירים, אלבומים, אמנים, ז'אנרים, מלחינים — סנכרון, חיפוש, עריכת מטאדטה." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="רשימות השמעה" subtitle="בנו, ייבאו M3U / M3U8 / CUE, סדרו מחדש וייצאו ל-M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="קבצים מקומיים" subtitle="מוזיקה אופלין, כוננים USB, Wi-Fi Drive, מנהל קבצים, תיקיות אופלין." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="נגן אודיו" subtitle="פלט ברזולוציה גבוהה, איקולייזר, גובה צליל, סימניות, AirPlay, Chromecast, מהירות, מעצר שינה." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="הגדרות" subtitle="מנוע אודיו, ספרייה, מנהל קבצים, CarPlay, ווידג'טים, התאמה אישית, שפה, גיבוי." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="שאלות נפוצות" subtitle="מצאו תשובות ל-50 השאלות הנפוצות ביותר על Flacbox." >}}

{{< /cards >}}
