---
date: 2020-01-01
title: 'Flacbox'
description: 'Ismerje meg, hogyan használja a Flacboxot — a hi-res FLAC, DSD, ALAC és FFmpeg-alapú felhős zenei lejátszót iPhone-ra, iPadre és Macre. Csatlakoztassa az iCloud Drive-ot, a Google Drive-ot, a Dropboxot, az OneDrive-ot, a MEGA-t, a Boxot, a pCloudot, a Synologyt, a QNAP-ot, a NAS-t, a WebDAV-ot, az SMB-t és a DLNA-t. Streamelje és töltse le a nagy felbontású hanganyagokat, szerkessze a metaadatokat, hallgasson hangoskönyveket, scrobboljon a Last.fm-re, használja az Apple CarPlayt és a kezdőképernyő widgeteket, és személyre szabja a 10 sávos equalizert.'
keywords: [
  "Flacbox felhasználói útmutató", "Flacbox hogyan kell", "hi-res zenelejátszó iPhone", "FLAC lejátszó iPhone",
  "DSD lejátszó iOS", "ALAC lejátszó Mac", "veszteségmentes zene app", "felhős zenelejátszó iPhone",
  "offline FLAC lejátszó Mac", "zenetár-kezelő", "hangsáv-szerkesztő",
  "CarPlay FLAC lejátszó", "Chromecast audio app", "AirPlay 2 zene",
  "Flacbox widgetek", "Flacbox CarPlay", "FFmpeg zenelejátszó iOS",
  "hangoskönyv lejátszó iPhone", "hang könyvjelzők iOS", "hangmagasság-korrekció",
  "audio kimenet mintavételezési frekvencia", "külső DAC iPhone", "USB DAC Mac",
  "Synology zene app", "QNAP zene app", "NAS zenelejátszó iPhone",
  "WebDAV zenelejátszó", "SMB zene streaming", "DLNA zenelejátszó",
  "iCloud Drive zene", "Google Drive FLAC", "Dropbox FLAC lejátszó",
  "Wi-Fi Drive zenátvitel", "M3U lejátszási lista importálás", "Last.fm scrobbling"
]
tags: ["flacbox", "útmutató", "hi-res", "FLAC", "FFmpeg", "felhő", "CarPlay", "widgetek"]
---


### Üdvözöljük a Flacbox útmutatóban

A Flacbox egy nagy felbontású zenelejátszó iPhone-ra, iPadre és Macre, amely lehetővé teszi, hogy kedvenc felhőtárhely-szolgáltatásait, NAS-ét és médiaszervereit saját személyes streaming-szolgáltatássá alakítsa.

A Flacbox rengeteg forráshoz csatlakozik, mind egyetlen alkalmazásban:

- **Személyes felhőtárhely:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Saját hosztolt szerverek:** Plex · Jellyfin · Emby · Subsonic (és minden Subsonic-kompatibilis szerver — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (és ownCloud a közös API-n keresztül) · Synology Drive · QNAP.
- **NAS és fájlmegosztási protokollok:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (jelszavas vagy nyilvános kulcsos hitelesítés) · NFS · DLNA / UPnP (lejátszás és letöltés). Működik Apple Time Capsule-lel, Synologyval, QNAP-pal, WD My Clouddal, bármilyen Linux Samba / NFS / SSH-gazdával, vagy a Mac vagy Windows PC megosztott mappájával.
- **S3-kompatibilis objektumtárhely:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces és bármilyen más S3 API-végpont.
- **Helyi hálózat felfedezése:** Az Elérhető eszközök szakasz automatikusan listázza az összes Bonjour / mDNS-szolgáltatást a Wi-Fi hálózaton — Plex, Jellyfin, Emby szerverek, Synology, QNAP, AirPort útválasztók csatlakoztatott meghajtókkal, Time Capsule — így IP-cím beírása nélkül csatlakozhat.

Ahol a legtöbb zenealkalmazás az Apple beépített hangmotorjára támaszkodik, a Flacbox **FFmpeg**-et kínál a rendszerkodekek mellett, így olyan formátumokat is lejátszhat, amelyeket az iOS alapból nem támogat — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, plusz a szokásos MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC család. Konfigurálható audio kimenet mintavételezési frekvenciával (44,1 / 48 / 64 / 88,2 / 96 kHz), többcsatornás kimenettel (Mono → 5.1 → SDDS → ITU BS.775-1), IO puffer hangolással és hangmagasság-korrekcióval a Flacbox olyan vezérlést ad audiophileknek, amit a legtöbb fogyasztói zenealkalmazás egyszerűen nem kínál.

### Élvezze a gördülékeny streamelést és offline lejátszást

A Flacbox intelligens pufferelést kínál a gördülékeny streameléshez és beépített letöltéskezelőt, így teljes lejátszási listákat, előadókat, albumokat, mappákat vagy egyedi számokat tölthet le az eszközére offline használatra. Ha kevés a tárhely, egy koppintással törölheti a gyorsítótárazott fájlokat, és folytathatja a streamelést a felhőből. Az offline mód mappákhoz, lejátszási listákhoz, albumokhoz és előadókhoz automatikusan szinkronizálja az új számokat, amint megjelennek a felhőben, így az offline gyűjtemény mindig naprakész marad.

### Automatikusan rendszerezett zenetár

Amikor hangfájlokat importál, a Flacbox beolvassa a metaadataikat és rendezett Zenetárba rendezi őket — Dalok, Lejátszatlan dalok, Albumok, Album előadók, Előadók, Műfajok és Szerzők szerint csoportosítva. A beépített kereséssel másodpercek alatt megtalálhat bármit, szűrhet forrás szerint (online felhő / offline / eszköz), és választhat Sima / Csoportosított / Füles könyvtárelrendezések közül. A vegyes "különböző előadók" összeállításokat tartalmazó könyvtárak esetén a Flacbox dedikált Összes album / Exkluzív albumok / Szóló albumok nézeteket biztosít.

### Javítsa a metaadatokat és tagelje a zenéjét

Ha sérült tagekkel vagy rendezetlen kódolásokkal találkozik (ez gyakori gond a ripelt vagy régebbi fájloknál), a beépített ID3 Tags Editor megoldhatja ezeket — manuálisan vagy automatikus MusicBrainz-keresésekkel. Normalizálhatja a törött karakterkódolásokat (kiváló a cirill, japán vagy kínai tagekhez, amelyek Windows PC-kről kerültek be), kereshet hiányzó borítókat, és automatikusan visszaírhatja a változtatásokat az eredeti felhőbeli fájlba. A mélyebb kötegelt szerkesztéshez telepítse a kísérő Evertag alkalmazásunkat.

### Egyszerű átvitel Mac-ről, PC-ről vagy NAS-ról

Vigyen át zenét a számítógépe és iPhone-ja vagy iPadje között az alábbi eszközök bármelyikével: SMB, WebDAV, DLNA, Wi-Fi Drive (drag-and-drop bármilyen asztali böngészőben), iTunes / Finder fájlmegosztás Lightning vagy USB-C kábelen keresztül, USB flash meghajtók vagy iXpand Flash Drive-ok. Van Apple Time Capsule-je, WD My Clouda, Synologyja, QNAP-ja vagy bármilyen más NAS-a, amely SMB / WebDAV / DLNA / FTP / SFTP-t biztosít? Csatlakozzon egyszer, és streamelje az egész könyvtárát anélkül, hogy helyet foglalna az eszközön.

### Személyre szabhatja a hangzást az equalizerrel

A Flacbox tartalmaz egy 10 sávos equalizert iPod-stílusú előbeállításokkal (Akusztikus, Basszus erősítő, Klasszikus, Dance, Rock, Pop, Jazz és még sok más), egy preamplifikátorral és a saját előbeállítások mentési lehetőségével. Akár audiophile IEM-ekre, HomePod minire vagy autósztereóra hangol, pontosan olyan hangzást alakíthat ki, amilyet szeretne.

### Hangoskönyv-barát

A Flacbox kiváló hangoskönyv-lejátszó — többszörös sávonkénti könyvjelzők, finoman hangolható lejátszási sebesség (0,02×-tól 3,00×-ig), lejátszás folytatása pontosan onnan, ahol abbahagyta, testreszabható ugrás-idő gombok és alvásidőzítő, amely lefekvés előtt halkan elhal. Az M4B fejezet jelölők és a hosszú fájlok teljes mértékben támogatottak.

### Streameljen bárhol — beleértve az autóját és a kezdőképernyőt

Streameljen zenét az Apple TV-re / HomePodra AirPlay 2-n keresztül, küldje Google Chromecast hangszórókra és Cast-kompatibilis TV-kre, és vigyen mindent magával az Apple CarPlayon. Használjon kezdőképernyő widgeteket iPhone-on és iPaden az éppen lejátszott szám megtekintéséhez egy pillantásra, és a Last.fm scrobbling segítségével tartsa meg a hallgatási előzményeit az alkalmazások között.

### Adatvédelem és biztonság

A Flacbox csak hivatalos SDK-kat és OAuth-alapú bejelentkezéseket használ minden felhőszolgáltatótól — a jelszava soha nem jut el az alkalmazáshoz. A hozzáférési tokenek titkosítva vannak az iOS Keychain-ben, minden átvitel TLS-védett, és a felhőfiókjából való visszavonás vagy a Flacbox eltávolítása az eszközről azonnal mindent töröl. Védje könyvtárát opcionális jelszókóddal a magánélet extra védelme érdekében.

### Első lépések a Flacboxszal

Ez az útmutató végigvezeti Önt a Flacbox minden részén iPhone-on, iPaden és Macon — a felhőszolgáltatások csatlakoztatásától, a könyvtár rendszerezésétől, a fájlok átvitelétől és a lejátszási listák kezelésétől az equalizer finomhangolásáig és a hangmotor konfigurálásáig. Az alábbi kártyák segítségével közvetlenül a szükséges szakaszra ugorhat.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navigáció" subtitle="Tab sor iPhone-on, bal oldali menü iPaden és Macon, mini lejátszó, widgetek, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Kapcsolatok" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Zenetár" subtitle="Dalok, Albumok, Előadók, Műfajok, Szerzők — szinkronizálás, keresés, metaadatok szerkesztése." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Lejátszási listák" subtitle="Hozzon létre, importáljon M3U / M3U8 / CUE-t, rendezze át és exportálja M3U / CSV / TXT formátumba." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Helyi fájlok" subtitle="Offline zene, USB meghajtók, Wi-Fi Drive, fájlkezelő, offline mappák." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Audiojátszó" subtitle="Hi-res kimenet, equalizer, hangmagasság, könyvjelzők, AirPlay, Chromecast, sebesség, alvásidőzítő." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Beállítások" subtitle="Hangmotor, könyvtár, fájlkezelő, CarPlay, widgetek, személyre szabás, nyelv, biztonsági mentés." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="GYIK" subtitle="Találja meg a Flacboxra vonatkozó 50 leggyakoribb kérdésre adott választ." >}}

{{< /cards >}}
