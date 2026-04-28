---
title: "כיצד לחבר את האחסון הפנימי של Bluesound VAULT מ-Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "למדו כיצד לגשת לכונן הקשיח הפנימי של Bluesound VAULT מ-Evermusic, Flacbox ו-Evertag באמצעות פרוטוקול SMB לניהול, עריכה והשמעת קבצי אודיו."
keywords: ["bluesound vault", "חיבור אחסון smb", "evermusic smb", "flacbox vault", "evertag smb", "אחסון nas מוזיקה", "כונן פנימי vault"]
tags: ["evermusic", "חיבור", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**תקציר:** התחברו לאחסון הפנימי של Bluesound VAULT דרך SMB באמצעות Evermusic, Flacbox או Evertag. מצאו את כתובת ה-IP של ה-VAULT באפליקציית BluOS, הזינו אותה כחיבור SMB עם גישת אורח, והתחילו להשמיע או לנהל את קבצי המוזיקה שלכם.

ל-Bluesound VAULT יש כונן קשיח פנימי והוא פועל כאחסון מחובר לרשת (NAS). גישה לכונן הקשיח הפנימי של ה-VAULT מאפשרת לכם להוסיף/למחוק קבצים, לערוך תגי מטאדטה מהאפליקציות שלנו Evermusic, Flacbox, Evertag.

**להלן השלבים לגישה לכונן הקשיח הפנימי של ה-VAULT:**

1. באפליקציית BluOS, בחרו **עזרה > אבחון**.

2. מדף **האבחון**, השיגו את **כתובת ה-IP** של ה-VAULT. **כתובת IP** זו תשמש בשלבים הבאים.

3. פתחו את Evermusic, Flacbox או Evertag.

   ![אפליקציות Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. פתחו את מסך "חיבורים" ובחרו בפריט התפריט "חבר שירות ענן".

   ![מסך חיבורים של Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. בחרו בשירות הענן "SMB".

   ![מסך חיבור שירות ענן של Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. ב"מסך הגדרת SMB" הזינו את ה-URL בפורמט הבא:

   ```
   SMB://<<VAULT-IP>>
   ```

   החליפו את `<<VAULT-IP>>` ב**כתובת ה-IP** שהושגה בשלב 2.

   **הערה:** השאירו את שדות שם המשתמש והסיסמה ריקים כי אחסון ה-VAULT תומך במצב אורח (GUEST).

   ![מסך חיבור SMB של Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. הקישו על כפתור "התחבר" כדי לשמור את ההגדרות.

8. פתחו את אחסון הענן המחובר, נווטו לתיקייה עם קבצי אודיו והקישו על כל קובץ כדי להפעיל את נגן האודיו.

   ![מסך שרת SMB פתוח של Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. ניתן גם לערוך קבצים באמצעות מנהל הקבצים המובנה.

   ![מסך מנהל הקבצים של Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

בעזרת שלבים פשוטים אלה, תוכלו לגשת בקלות לכונן הקשיח הפנימי של Bluesound VAULT ולשלוט בספריית המוזיקה שלכם באמצעות Evermusic, Flacbox או Evertag.

## שאלות נפוצות

{{% details title="האם אני צריך שם משתמש וסיסמה כדי להתחבר ל-Bluesound VAULT?" closed="true" %}}
לא. Bluesound VAULT תומך בגישת אורח (אנונימית) דרך SMB. השאירו את שדות שם המשתמש והסיסמה ריקים בעת הגדרת החיבור.
{{% /details %}}

{{% details title="האם אני יכול לערוך תגי מוזיקה ב-Bluesound VAULT?" closed="true" %}}
כן. באמצעות Evertag, תוכלו לערוך תגי מטאדטה (כותרת, אמן, אלבום וכו') עבור קבצי אודיו המאוחסנים ישירות בכונן הקשיח הפנימי של ה-VAULT.
{{% /details %}}

{{% details title="אילו פרוטוקולים תומך Bluesound VAULT?" closed="true" %}}
Bluesound VAULT חושף את האחסון הפנימי שלו דרך SMB (Server Message Block). Evermusic, Flacbox ו-Evertag כולם תומכים בחיבורי SMB, מה שהופך את החיבור לפשוט.
{{% /details %}}

{{% details title="האם אני יכול להזרים מוזיקה מה-VAULT מבלי להעתיק קבצים ל-iPhone שלי?" closed="true" %}}
כן. לאחר החיבור דרך SMB, תוכלו להזרים קבצי אודיו ישירות מהכונן הפנימי של ה-VAULT מבלי להעתיק אותם למכשיר שלכם.
{{% /details %}}
