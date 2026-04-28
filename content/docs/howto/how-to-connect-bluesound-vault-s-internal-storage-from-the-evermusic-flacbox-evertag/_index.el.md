---
title: "Πώς να συνδέσετε τον εσωτερικό αποθηκευτικό χώρο του Bluesound VAULT από το Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Μάθετε πώς να αποκτήσετε πρόσβαση στον εσωτερικό σκληρό δίσκο του Bluesound VAULT από το Evermusic, Flacbox και Evertag χρησιμοποιώντας το πρωτόκολλο SMB για διαχείριση, επεξεργασία και αναπαραγωγή αρχείων ήχου."
keywords: ["bluesound vault", "σύνδεση αποθηκευτικού χώρου smb", "evermusic smb", "flacbox vault", "evertag smb", "αποθήκευση nas μουσική", "εσωτερικός δίσκος vault"]
tags: ["evermusic", "σύνδεση", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Περίληψη:** Συνδεθείτε στον εσωτερικό αποθηκευτικό χώρο του Bluesound VAULT μέσω SMB χρησιμοποιώντας Evermusic, Flacbox ή Evertag. Βρείτε τη διεύθυνση IP του VAULT στην εφαρμογή BluOS, εισαγάγετε την ως σύνδεση SMB με πρόσβαση επισκέπτη και ξεκινήστε την αναπαραγωγή ή τη διαχείριση των αρχείων μουσικής σας.

Το Bluesound VAULT διαθέτει εσωτερικό σκληρό δίσκο και λειτουργεί ως αποθηκευτικός χώρος συνδεδεμένος στο δίκτυο (NAS). Η πρόσβαση στον εσωτερικό σκληρό δίσκο του VAULT σας επιτρέπει να προσθέτετε/διαγράφετε αρχεία, να επεξεργάζεστε ετικέτες μεταδεδομένων από τις εφαρμογές μας Evermusic, Flacbox, Evertag.

**Ακολουθούν τα βήματα για πρόσβαση στον εσωτερικό σκληρό δίσκο του VAULT:**

1. Στην εφαρμογή BluOS, επιλέξτε **Βοήθεια > Διαγνωστικά**.

2. Από τη σελίδα **Διαγνωστικά**, αποκτήστε τη **Διεύθυνση IP** του VAULT. Αυτή η **Διεύθυνση IP** θα χρησιμοποιηθεί στα επόμενα βήματα.

3. Ανοίξτε το Evermusic, Flacbox ή Evertag.

   ![Εφαρμογές Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Ανοίξτε την οθόνη "Συνδέσεις" και επιλέξτε το στοιχείο μενού "Σύνδεση υπηρεσίας cloud".

   ![Οθόνη Συνδέσεων Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Επιλέξτε την υπηρεσία cloud "SMB".

   ![Οθόνη Σύνδεσης Υπηρεσίας Cloud Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Στην "Οθόνη διαμόρφωσης SMB" εισαγάγετε το URL στην ακόλουθη μορφή:

   ```
   SMB://<<VAULT-IP>>
   ```

   Αντικαταστήστε το `<<VAULT-IP>>` με τη **Διεύθυνση IP** που αποκτήθηκε στο Βήμα 2.

   **Σημείωση:** Αφήστε τα πεδία Σύνδεση και Κωδικός πρόσβασης κενά επειδή ο αποθηκευτικός χώρος VAULT υποστηρίζει λειτουργία ΕΠΙΣΚΕΠΤΗ.

   ![Οθόνη σύνδεσης SMB Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Πατήστε το κουμπί "Είσοδος" για να αποθηκεύσετε τη διαμόρφωση.

8. Ανοίξτε τον συνδεδεμένο αποθηκευτικό χώρο cloud και πλοηγηθείτε μέσα στον φάκελο με αρχεία ήχου και πατήστε οποιοδήποτε αρχείο για να ξεκινήσετε τον αναπαραγωγέα ήχου.

   ![Οθόνη ανοιγμένου διακομιστή SMB Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Μπορείτε επίσης να επεξεργαστείτε αρχεία χρησιμοποιώντας τον ενσωματωμένο διαχειριστή αρχείων.

   ![Οθόνη Διαχειριστή Αρχείων Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Με αυτά τα απλά βήματα, μπορείτε εύκολα να αποκτήσετε πρόσβαση στον εσωτερικό σκληρό δίσκο του Bluesound VAULT και να ελέγξετε τη μουσική βιβλιοθήκη σας χρησιμοποιώντας Evermusic, Flacbox ή Evertag.

## Συχνές Ερωτήσεις

{{% details title="Χρειάζομαι όνομα χρήστη και κωδικό πρόσβασης για να συνδεθώ στο Bluesound VAULT;" closed="true" %}}
Όχι. Το Bluesound VAULT υποστηρίζει πρόσβαση επισκέπτη (ανώνυμη) μέσω SMB. Αφήστε τα πεδία Σύνδεση και Κωδικός πρόσβασης κενά κατά τη διαμόρφωση της σύνδεσης.
{{% /details %}}

{{% details title="Μπορώ να επεξεργαστώ ετικέτες μουσικής στο Bluesound VAULT;" closed="true" %}}
Ναι. Χρησιμοποιώντας το Evertag, μπορείτε να επεξεργαστείτε ετικέτες μεταδεδομένων (τίτλος, καλλιτέχνης, άλμπουμ κ.λπ.) για αρχεία ήχου που είναι αποθηκευμένα απευθείας στον εσωτερικό σκληρό δίσκο του VAULT.
{{% /details %}}

{{% details title="Ποια πρωτόκολλα υποστηρίζει το Bluesound VAULT;" closed="true" %}}
Το Bluesound VAULT εκθέτει τον εσωτερικό του αποθηκευτικό χώρο μέσω SMB (Server Message Block). Τα Evermusic, Flacbox και Evertag υποστηρίζουν όλα συνδέσεις SMB, καθιστώντας τη σύνδεση απλή.
{{% /details %}}

{{% details title="Μπορώ να κάνω streaming μουσικής από το VAULT χωρίς να αντιγράψω αρχεία στο iPhone μου;" closed="true" %}}
Ναι. Μόλις συνδεθείτε μέσω SMB, μπορείτε να κάνετε streaming αρχείων ήχου απευθείας από τον εσωτερικό δίσκο του VAULT χωρίς να τα αντιγράψετε στη συσκευή σας.
{{% /details %}}
