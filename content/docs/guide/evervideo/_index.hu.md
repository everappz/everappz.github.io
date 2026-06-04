---
date: 2020-01-01
lastmod: 2026-06-01
title: 'Evervideo'
description: 'Ismerje meg, hogyan használhatja az Evervideót — az iPhone-ra, iPadre és Macre készült mindent-egyben felhővideó-lejátszót. Videók streamelése és letöltése iCloud Drive-ról, Google Drive-ról, Dropboxról, OneDrive-ról, MEGÁról, Boxból, pCloudból, Synologyról, QNAP-ről, NAS-ről, WebDAV-on, SMB-n, NFS-en, FTP / SFTP-n, DLNA-n és S3-on keresztül — valamint Plex, Jellyfin, Emby, Subsonic és Navidrome támogatással. Kép-a-képben nézet, elsődleges és másodlagos feliratok, hang- és videóegyenlítők, RTSP IP-kamera streamek, Chromecast, AirPlay 2, hardveres H.264 / HEVC dekódolás, Fotók és Apple Music könyvtár integráció, valamint kompakt, mindig látható lejátszó.'
keywords: [
  "Evervideo útmutató", "Evervideo hogyan", "felhővideó-lejátszó iPhone", "videólejátszó Mac",
  "MKV lejátszó iOS", "FFmpeg videólejátszó", "HEVC videólejátszó iPhone",
  "Kép-a-képben videó iPhone", "PiP videólejátszó iPad",
  "RTSP lejátszó iPhone", "IP kamera néző", "DLNA videólejátszó",
  "Plex kliens iPhone", "Jellyfin kliens iOS", "Emby kliens iPad",
  "felirat lejátszó iOS", "SRT VTT ASS feliratok", "másodlagos feliratok iPhone",
  "videóegyenlítő iOS", "hangegyenlítő videólejátszó", "külső DAC videó",
  "videó streamelése Google Drive-ról", "videó streamelése Dropboxról",
  "videó streamelése OneDrive-ról", "videó streamelése iCloud Drive-ról",
  "videó streamelése MEGÁról", "videó streamelése NAS-ről",
  "Chromecast videó iPhone", "AirPlay 2 videó", "iCloud videólejátszó",
  "Fotók könyvtár videólejátszó", "Apple Music videólejátszó",
  "Wi-Fi Drive videóátvitel", "M3U videólejátszási lista",
  "Evervideo Premium", "Family Sharing videó alkalmazás"
]
tags: ["evervideo", "útmutató", "videólejátszó", "PiP", "feliratok", "RTSP", "felhő", "FFmpeg"]
---


### Üdvözöljük az Evervideo útmutatóban

Az Evervideo egy teljes funkcionalitású felhőmédialejátszó iPhone-ra, iPadre és Macre, amely bármely felhőtároló-fiókot, NAS-t vagy médiaszervert személyes médiakönyvtárrá alakítja — mindenféle újrafeltöltés nélkül, miközben teljes irányítást biztosít a fájlok felett.

Az egyedi FFmpeg-alapú lejátszómotor hardveres H.264 és HEVC dekódolással szinte minden modern tárolóformátumot és kodeket lejátszik — MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS és az FFmpeg-formátumok hosszú sora — teljes minőségben, intelligens pufferelés segítségével Wi-Fi-n vagy mobilhálózaton keresztül. A Kép-a-képben funkció minden más alkalmazás felett tartja a videót, a kompakt, mindig látható lejátszó lehetővé teszi, hogy tovább nézzen, miközben böngészi a könyvtárat, a Chromecast és az AirPlay 2 pedig egy érintéssel elküldi a lejátszást a tévére, HomePodra vagy hangszórókra.

Az Evervideo rendkívül széles forráslista-hoz csatlakozik, mindezt egyetlen alkalmazásból:

- **Személyes felhőtároló:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Önhostolt médiaszerverek:** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud (és ownCloud a megosztott API-n keresztül) · Synology Drive · QNAP.
- **NAS és fájlmegosztási protokollok:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (jelszavas vagy nyilvános kulcsú hitelesítés) · NFS · DLNA · UPnP.
- **Élő és IP-kamera streamek:** RTSP — irányítsa az Evervideót bármely RTSP URL-re (`rtsp://camera-ip/stream`) és azonnal lejátssza.
- **S3-kompatibilis objektumtároló:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces és bármely más S3-API végpont.
- **Eszközön lévő források:** a Fotók könyvtár (Minden videó, Rövid / Közepes / Hosszú, Képernyőfelvételek és Fotoalbumok), a Music alkalmazás könyvtára (Albumok, Műfajok, Lejátszási listák), USB / SD kártya meghajtók és Helyi fájlok.

### Egy lejátszó minden formátumhoz és kodekhez

Miközben a legtöbb iOS-alkalmazás megáll a H.264 / H.265-nél MP4 / MOV formátumon belül, az Evervideo az Apple rendszerkodekei mellé becsomagolja az FFmpeg-et, így olyan formátumokat is lejátszhat, amelyeket a rendszer nem ismer fel — MKV-tárolók, VP9, AV1, MPEG-2, OGG, Vorbis és sok más — és automatikusan vált a hardveres H.264 / HEVC dekódolás és a szoftveres dekódolás között a fájl és az eszköz alapján.

Kiválaszthatja a videósávot (többsávos Blu-ray másolatok), a hangsávot (kommentársávok, alternatív szinkronizálások) és a felirat sávot. A külső SRT, VTT és ASS / SSA feliratfájlok egy érintéssel betölthetők; a fejlett ASS / SSA stílus helyes renderelést biztosít a beépített libass köszönhetően.

### Intelligens feliratok

- **Felirat sávválasztás** — tökéletes nyelvtanuláshoz.
- **Külső feliratfájlok** (`.srt`, `.vtt`, `.ass`, `.ssa`) betölthetők az eszköz bármely helyéről vagy a felhőből.
- **libass** a teljes mértékben stílusos ASS / SSA rendereléshez.
- **Sávonkénti és globális betűtípus-kiválasztás** feliratokhoz.
- **Hangsáv-kiválasztás** — válassza a szinkronizálást, a kommentárt vagy a rendező sávját.
- **Videósáv-kiválasztás** — többszögű vagy többverziós fájlokhoz.

### Finomhangolja a képet és a hangot

Két egyenlítő egymás mellett: egy hangegyenlítő a mély- és magashangok beállításához (egyéni előbeállítások importálása / exportálása), és egy videóegyenlítő a fényerő, kontraszt, telítettség és árnyalat beállításához (szintén importálással / exportálással). Mindkét motor audiofil vezérlőket is kínál: kimeneti mintavételezési frekvencia, csatornaszám, IO puffer időtartama és vegyes mód — külső DAC-okkal és otthoni mozgófilmrendszerekkel rendelkező felhasználók számára.

### Cast, AirPlay és Kép-a-képben

- **Kép-a-képben (PiP):** nézzen tovább, miközben más alkalmazásokat használ.
- **AirPlay 2:** videó küldése Apple TV-re, HomePodra vagy bármely AirPlay 2 hangszóróra / tévére.
- **Google Chromecast:** leadás közvetlenül Chromecastra vagy Cast-kompatibilis tévére.
- **Kompakt lejátszó:** állandó mini lejátszó minden képernyő tetején, így böngészheti a könyvtárat a videó elvesztése nélkül.

### Adatvédelem és biztonság

Az Evervideo hivatalos SDK-kat és OAuth-alapú bejelentkezéseket használ minden felhőszolgáltatótól, így jelszava soha nem jut el az alkalmazáshoz. A hozzáférési tokenek titkosítva tárolódnak az iOS/MacOS Keychain-ben, minden átvitel TLS-védelemmel rendelkezik, és a felhőfiókból (vagy az Evervideo eszközről való eltávolítása után) a hozzáférés visszavonása azonnal mindent töröl. Védje könyvtárát opcionális 4 számjegyű jelszóval a további adatvédelem érdekében.

### Az Evervideo használatának megkezdése

Ez az útmutató végigvezeti az Evervideo minden részén iPhone-on, iPaden és Macon — a felhőszolgáltatások csatlakoztatásától, a könyvtár böngészésétől, a fájlok letöltésétől és átvitelétől, a lejátszási listák kezelésétől a médialejátszó, egyenlítők, feliratok és Kép-a-képben finomhangolásáig. Az alábbi kártyák segítségével ugorjon közvetlenül a szükséges szakaszhoz.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="Navigáció" subtitle="Tab sáv iPhone-on, Bal menü iPaden és Macon, kompakt, mindig látható médialejátszó." >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="Fájlok" subtitle="Egységes lap a felhőhöz, NAS-hoz, RTSP streamekhez, helyi fájlokhoz, USB meghajtókhoz és az átviteli sorhoz." >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="Médiakönyvtár" subtitle="Böngészés albumok, műfajok, legutóbbi, kedvencek szerint — valamint az iOS Fotók könyvtár és az Apple Music könyvtár." >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="Lejátszási listák" subtitle="Lejátszási listák készítése felhőből, helyi, Fotók vagy Music könyvtárból, M3U / M3U8 / CUE importálása." >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="Médialejátszó" subtitle="Kép-a-képben, hang- és videósávok, feliratok, hang- és videóegyenlítők, AirPlay, Chromecast." >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="Beállítások" subtitle="Hangmotor, videódekóder, feliratok, könyvtár, fájlkezelő, widgetek, személyre szabás, nyelv, biztonsági mentés." >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="GYIK" subtitle="Találja meg a leggyakoribb Evervideóval kapcsolatos kérdések válaszait." >}}

{{< /cards >}}
