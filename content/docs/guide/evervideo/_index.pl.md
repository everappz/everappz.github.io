---
date: 2020-01-01
lastmod: 2026-06-01
title: 'Evervideo'
description: 'Dowiedz się, jak korzystać z Evervideo — kompleksowego odtwarzacza wideo w chmurze dla iPhone, iPad i Mac. Strumieniuj i pobieraj filmy z iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, NFS, FTP / SFTP, DLNA i S3 — a także Plex, Jellyfin, Emby, Subsonic i Navidrome. Obraz w obrazie, napisy główne i drugorzędne, korektor audio i wideo, strumienie kamer RTSP, Chromecast, AirPlay 2, sprzętowe dekodowanie H.264 / HEVC, integracja z Zdjęciami i Apple Music oraz kompaktowy odtwarzacz zawsze na ekranie.'
keywords: [
  "poradnik Evervideo", "jak używać Evervideo", "odtwarzacz wideo w chmurze iPhone", "odtwarzacz wideo Mac",
  "odtwarzacz MKV iOS", "odtwarzacz wideo FFmpeg", "odtwarzacz HEVC iPhone",
  "obraz w obrazie iPhone", "odtwarzacz PiP iPad",
  "odtwarzacz RTSP iPhone", "przeglądarka kamer IP", "odtwarzacz DLNA wideo",
  "klient Plex iPhone", "klient Jellyfin iOS", "klient Emby iPad",
  "odtwarzacz napisów iOS", "napisy SRT VTT ASS", "drugorzędne napisy iPhone",
  "korektor wideo iOS", "korektor audio do wideo", "zewnętrzny DAC wideo",
  "strumieniowanie wideo z Google Drive", "strumieniowanie wideo z Dropbox",
  "strumieniowanie wideo z OneDrive", "strumieniowanie wideo z iCloud Drive",
  "strumieniowanie wideo z MEGA", "strumieniowanie wideo z NAS",
  "Chromecast wideo iPhone", "AirPlay 2 wideo", "odtwarzacz wideo iCloud",
  "odtwarzacz wideo biblioteka Zdjęć", "odtwarzacz wideo Apple Music",
  "transfer wideo Wi-Fi Drive", "lista odtwarzania M3U",
  "Evervideo Premium", "aplikacja wideo Family Sharing"
]
tags: ["evervideo", "poradnik", "odtwarzacz wideo", "PiP", "napisy", "RTSP", "chmura", "FFmpeg"]
---


### Witamy w Poradniku Evervideo

Evervideo to w pełni funkcjonalny odtwarzacz multimediów w chmurze dla iPhone, iPad i Mac, który przekształca dowolne konto w chmurze, NAS lub serwer multimediów w Twoją osobistą bibliotekę multimediów — bez konieczności ponownego przesyłania czegokolwiek i z pełną kontrolą nad plikami.

Zbudowany na własnym silniku odtwarzacza opartym na FFmpeg ze sprzętowo przyspieszonym dekodowaniem H.264 i HEVC, Evervideo odtwarza praktycznie każdy nowoczesny kontener i kodek — MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS i wiele innych formatów FFmpeg — w pełnej jakości, z inteligentnym buforowaniem zapewniającym płynne strumieniowanie przez Wi-Fi lub sieć komórkową. Obraz w obrazie utrzymuje wideo na wierzchu każdej innej aplikacji, kompaktowy odtwarzacz zawsze na ekranie pozwala oglądać podczas przeglądania biblioteki, a Chromecast i AirPlay 2 przesyłają odtwarzanie do telewizora, HomePod lub zestawu głośnikowego jednym dotknięciem.

Evervideo łączy się z wyjątkowo szeroką listą źródeł — wszystkich z jednej aplikacji:

- **Osobista pamięć masowa w chmurze:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Własne serwery multimediów:** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud (i ownCloud przez wspólne API) · Synology Drive · QNAP.
- **Protokoły NAS i udostępniania plików:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (hasło lub uwierzytelnianie kluczem publicznym) · NFS · DLNA · UPnP.
- **Strumienie na żywo i kamery IP:** RTSP — wpisz w Evervideo dowolny adres URL RTSP (`rtsp://adres-kamery/strumień`) i po prostu odtwarza.
- **Pamięć obiektowa zgodna z S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i każdy inny punkt końcowy S3-API.
- **Źródła na urządzeniu:** biblioteka Zdjęć (Wszystkie filmy, Krótkie / Średnie / Długie, Nagrania ekranu oraz Albumy ze zdjęciami), biblioteka aplikacji Muzyka (Albumy, Gatunki, Listy odtwarzania), dyski USB / karty SD i Pliki lokalne.

### Jeden odtwarzacz dla każdego formatu i kodeka

Podczas gdy większość aplikacji iOS zatrzymuje się na H.264 / H.265 w MP4 / MOV, Evervideo łączy FFmpeg z systemowymi kodekami Apple, dzięki czemu możesz odtwarzać formaty nierozpoznawane przez system — kontenery MKV, VP9, AV1, MPEG-2, OGG, Vorbis i wiele innych — i automatycznie przełącza się między sprzętowym dekodowaniem H.264 / HEVC a dekodowaniem programowym na podstawie pliku i urządzenia.

Możesz wybrać ścieżkę wideo (rips z Blu-ray z wieloma strumieniami), ścieżkę audio (ścieżki komentarzy, alternatywne dubbingi) i ścieżkę napisów. Zewnętrzne pliki napisów SRT, VTT i ASS / SSA ładują się jednym dotknięciem; zaawansowane stylizacje ASS / SSA są renderowane poprawnie dzięki dołączonej bibliotece libass.

### Inteligentne napisy

- **Wybór ścieżki napisów** — idealny do nauki języków.
- **Zewnętrzne pliki napisów** (`.srt`, `.vtt`, `.ass`, `.ssa`) ładowane z dowolnego miejsca na urządzeniu lub z chmury.
- **libass** — w pełni stylizowane renderowanie ASS / SSA.
- **Wybór czcionki dla każdej ścieżki i globalny** dla napisów.
- **Wybór ścieżki audio** — wybierz dubbing, komentarz lub ścieżkę reżysera.
- **Wybór ścieżki wideo** — dla plików wielokątowych lub wielowersyjnych.

### Dopasuj obraz i dźwięk

Dwa korektory obok siebie: korektor audio do dostosowania basów i sopranów (z importem / eksportem niestandardowych presetów) oraz korektor wideo do regulacji jasności, kontrastu, nasycenia i odcienia (również z importem / eksportem). Oba silniki udostępniają też zaawansowane kontrolki audiofila: częstotliwość próbkowania wyjścia audio, liczba kanałów, czas trwania bufora IO i **Tryb mieszany** — dla użytkowników z zewnętrznymi DAC-ami i odbiornikami kina domowego.

### Cast, AirPlay i obraz w obrazie

- **Obraz w obrazie (PiP):** oglądaj podczas korzystania z innych aplikacji.
- **AirPlay 2:** przesyłaj wideo do Apple TV, HomePod lub dowolnego głośnika / telewizora AirPlay 2.
- **Google Chromecast:** przesyłaj bezpośrednio na Chromecast lub telewizor obsługujący Cast.
- **Kompaktowy odtwarzacz:** trwały mini-odtwarzacz na wierzchu każdego ekranu, dzięki któremu możesz przeglądać bibliotekę bez przerywania wideo.

### Prywatność i bezpieczeństwo

Evervideo używa oficjalnych SDK i logowań opartych na OAuth od każdego dostawcy chmury, dzięki czemu Twoje hasło nigdy nie trafia do aplikacji. Tokeny dostępu są przechowywane zaszyfrowane w iOS/MacOS Keychain, każdy transfer jest chroniony TLS, a odwołanie dostępu z konta w chmurze (lub usunięcie Evervideo z urządzenia) natychmiast usuwa wszystko. Chroń swoją bibliotekę opcjonalnym 4-cyfrowym kodem dostępu dla dodatkowej warstwy prywatności.

### Pierwsze kroki z Evervideo

Ten poradnik przeprowadza Cię przez każdą część Evervideo na iPhone, iPad i Mac — od łączenia usług w chmurze, przeglądania biblioteki, pobierania i transferu plików, zarządzania listami odtwarzania, po precyzyjne dostrojenie odtwarzacza multimediów, korektorów, napisów i obrazu w obrazie. Użyj poniższych kart, aby przejść bezpośrednio do potrzebnej sekcji.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="Nawigacja" subtitle="Pasek kart na iPhone, lewe menu na iPad i Mac, kompaktowy odtwarzacz zawsze na ekranie." >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="Pliki" subtitle="Jedna ujednolicona karta dla chmury, NAS, strumieni RTSP, plików lokalnych, dysków USB i kolejki transferów." >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="Biblioteka multimediów" subtitle="Przeglądaj według Albumów, Gatunków, Ostatnich, Ulubionych — a także biblioteki Zdjęć iOS i Apple Music." >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="Listy odtwarzania" subtitle="Twórz listy odtwarzania z chmury, plików lokalnych, Zdjęć lub biblioteki Muzyka, importuj M3U / M3U8 / CUE." >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="Odtwarzacz multimediów" subtitle="Obraz w obrazie, ścieżki audio i wideo, napisy, korektory audio i wideo, AirPlay, Chromecast." >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="Ustawienia" subtitle="Silnik audio, dekoder wideo, napisy, biblioteka, menedżer plików, widżety, personalizacja, język, kopia zapasowa." >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="FAQ" subtitle="Znajdź odpowiedzi na najczęstsze pytania dotyczące Evervideo." >}}

{{< /cards >}}
