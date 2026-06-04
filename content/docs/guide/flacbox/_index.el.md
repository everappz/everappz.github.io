---
date: 2020-01-01
title: 'Flacbox'
description: 'Μάθετε πώς να χρησιμοποιείτε το Flacbox — τον υψηλής ανάλυσης αναπαραγωγέα μουσικής FLAC, DSD, ALAC και FFmpeg για iPhone, iPad και Mac. Συνδεθείτε με iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB και DLNA. Μεταδώστε ροή και κατεβάστε υψηλής ανάλυσης ήχο, επεξεργαστείτε μεταδεδομένα, ακούστε ηχητικά βιβλία, κάντε scrobble στο Last.fm, χρησιμοποιήστε Apple CarPlay και widgets αρχικής οθόνης, και προσαρμόστε τον equalizer 10 ζωνών.'
keywords: [
  "οδηγός χρήστη Flacbox", "πώς να χρησιμοποιήσετε Flacbox", "αναπαραγωγέας μουσικής hi-res iPhone", "αναπαραγωγέας FLAC iPhone",
  "αναπαραγωγέας DSD iOS", "αναπαραγωγέας ALAC Mac", "εφαρμογή αδιάβλητης μουσικής", "αναπαραγωγέας μουσικής cloud iPhone",
  "offline αναπαραγωγέας FLAC Mac", "διαχειριστής μουσικής βιβλιοθήκης", "επεξεργαστής ετικετών ήχου",
  "CarPlay αναπαραγωγέας FLAC", "εφαρμογή Chromecast ήχου", "AirPlay 2 μουσική",
  "widgets Flacbox", "CarPlay Flacbox", "αναπαραγωγέας μουσικής FFmpeg iOS",
  "αναπαραγωγέας ηχητικών βιβλίων iPhone", "σελιδοδείκτες ήχου iOS", "διόρθωση τόνου εφαρμογή μουσικής",
  "ρυθμός δειγματοληψίας εξόδου ήχου", "εξωτερικό DAC iPhone", "USB DAC Mac",
  "εφαρμογή μουσικής Synology", "εφαρμογή μουσικής QNAP", "αναπαραγωγέας μουσικής NAS iPhone",
  "αναπαραγωγέας μουσικής WebDAV", "ροή μουσικής SMB", "αναπαραγωγέας μουσικής DLNA",
  "μουσική iCloud Drive", "FLAC Google Drive", "αναπαραγωγέας FLAC Dropbox",
  "μεταφορά μουσικής Wi-Fi Drive", "εισαγωγή playlist M3U", "scrobbling Last.fm"
]
tags: ["flacbox", "οδηγός", "hi-res", "FLAC", "FFmpeg", "cloud", "CarPlay", "widgets"]
---


### Καλώς ήρθατε στον Οδηγό Flacbox

Το Flacbox είναι ένας αναπαραγωγέας μουσικής υψηλής ανάλυσης για iPhone, iPad και Mac που σας επιτρέπει να μετατρέψετε τον αγαπημένο σας αποθηκευτικό χώρο στο cloud, NAS και διακομιστές πολυμέσων στη δική σας προσωπική υπηρεσία streaming.

Το Flacbox συνδέεται με μια εξαιρετικά ευρεία λίστα πηγών, όλα σε μία εφαρμογή:

- **Προσωπικός αποθηκευτικός χώρος cloud:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Αυτο-φιλοξενούμενοι διακομιστές:** Plex · Jellyfin · Emby · Subsonic (και κάθε διακομιστής συμβατός με Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (και ownCloud μέσω του κοινού API) · Synology Drive · QNAP.
- **Πρωτόκολλα NAS και κοινής χρήσης αρχείων:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (κωδικός πρόσβασης ή έλεγχος ταυτότητας δημόσιου κλειδιού) · NFS · DLNA / UPnP (αναπαραγωγή και λήψη).
- **Αποθηκευτικός χώρος αντικειμένων συμβατός με S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces και οποιοδήποτε άλλο τελικό σημείο S3-API.
- **Ανακάλυψη τοπικού δικτύου:** Η ενότητα «Διαθέσιμες συσκευές» παραθέτει αυτόματα κάθε υπηρεσία Bonjour / mDNS στο Wi-Fi σας.

Ενώ οι περισσότερες εφαρμογές μουσικής περιορίζονται στην ενσωματωμένη μηχανή ήχου της Apple, το Flacbox συμπεριλαμβάνει το **FFmpeg** μαζί με τους κωδικοποιητές συστήματος για να μπορείτε να αναπαράγετε μορφές που το iOS δεν υποστηρίζει εκ των προτέρων — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV καθώς και την κανονική οικογένεια MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC.

### Απολαύστε Ομαλή Ροή και Αναπαραγωγή Εκτός Σύνδεσης

Το Flacbox διαθέτει έξυπνο buffering για ομαλή ροή και ενσωματωμένο διαχειριστή λήψεων ώστε να μπορείτε να κατεβάσετε ολόκληρες λίστες αναπαραγωγής, καλλιτέχνες, άλμπουμ, φακέλους ή μεμονωμένα κομμάτια.

### Αυτόματα Οργανωμένη Μουσική Βιβλιοθήκη

Όταν εισάγετε κομμάτια ήχου, το Flacbox σαρώνει τα μεταδεδομένα τους και τα οργανώνει σε μια καθαρή μουσική βιβλιοθήκη — ομαδοποιημένα κατά Τραγούδια, Μη αναπαραχθέντα Τραγούδια, Άλμπουμ, Καλλιτέχνες Άλμπουμ, Καλλιτέχνες, Είδη και Συνθέτες.

### Διορθώστε Μεταδεδομένα και Βάλτε Ετικέτες στη Μουσική σας

Ο ενσωματωμένος Επεξεργαστής Ετικετών ID3 μπορεί να καθαρίσει κατεστραμμένες ετικέτες — χειροκίνητα ή με αυτόματες αναζητήσεις MusicBrainz.

### Εύκολες Μεταφορές από Mac, PC ή NAS

Μεταφέρετε μουσική μεταξύ του υπολογιστή σας και του iPhone ή iPad με οποιοδήποτε από αυτά τα εργαλεία: SMB, WebDAV, DLNA, Wi-Fi Drive, iTunes / Finder File Sharing μέσω καλωδίου Lightning ή USB-C, USB flash drives ή iXpand Flash Drives.

### Προσαρμόστε τον Ήχο σας με τον Equalizer

Το Flacbox περιλαμβάνει equalizer 10 ζωνών με presets τύπου iPod, προενισχυτή και δυνατότητα αποθήκευσης των δικών σας presets.

### Φιλικό προς τα Ηχητικά Βιβλία

Το Flacbox αποτελεί εξαιρετικό αναπαραγωγέα ηχητικών βιβλίων — πολλαπλοί σελιδοδείκτες ανά κομμάτι, λεπτομερής ταχύτητα αναπαραγωγής (0,02× έως 3,00×), συνέχιση αναπαραγωγής ακριβώς από εκεί που σταματήσατε και χρονοδιακόπτης ύπνου. Τα κεφαλαιακά σημεία M4B υποστηρίζονται πλήρως.

### Μεταδώστε Ροή Οπουδήποτε — Ακόμα και στο Αυτοκίνητο και στην Αρχική Οθόνη

Μεταδώστε μουσική μέσω AirPlay 2 σε Apple TV / HomePod, στείλτε την σε ηχεία Google Chromecast και τηλεοράσεις Cast-enabled, και πάρτε τα πάντα μαζί σας με Apple CarPlay.

### Απόρρητο και Ασφάλεια

Το Flacbox χρησιμοποιεί μόνο επίσημα SDK και συνδέσεις βασισμένες σε OAuth από κάθε πάροχο cloud — ο κωδικός πρόσβασής σας δεν φτάνει ποτέ στην εφαρμογή.

### Ξεκινώντας με το Flacbox

Αυτός ο οδηγός σας καθοδηγεί σε κάθε μέρος του Flacbox σε iPhone, iPad και Mac.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Πλοήγηση" subtitle="Tab Bar στο iPhone, αριστερό μενού σε iPad και Mac, mini player, widgets, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Συνδέσεις" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Μουσική Βιβλιοθήκη" subtitle="Τραγούδια, Άλμπουμ, Καλλιτέχνες, Είδη, Συνθέτες — συγχρονισμός, αναζήτηση, επεξεργασία μεταδεδομένων." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Λίστες αναπαραγωγής" subtitle="Δημιουργία, εισαγωγή M3U / M3U8 / CUE, αναδιάταξη και εξαγωγή σε M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Τοπικά Αρχεία" subtitle="Offline μουσική, USB drives, Wi-Fi Drive, διαχειριστής αρχείων, offline φάκελοι." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Audio Player" subtitle="Έξοδος hi-res, equalizer, τόνος, σελιδοδείκτες, AirPlay, Chromecast, ταχύτητα, χρονοδιακόπτης ύπνου." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Ρυθμίσεις" subtitle="Μηχανή ήχου, βιβλιοθήκη, διαχειριστής αρχείων, CarPlay, widgets, εξατομίκευση, γλώσσα, backup." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="FAQ" subtitle="Βρείτε απαντήσεις στις 50 πιο συνηθισμένες ερωτήσεις για το Flacbox." >}}

{{< /cards >}}
