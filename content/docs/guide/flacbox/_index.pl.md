---
date: 2020-01-01
title: 'Flacbox'
description: 'Dowiedz się, jak używać Flacbox — odtwarzacza muzyki hi-res obsługującego FLAC, DSD, ALAC i FFmpeg dla iPhone, iPad i Mac. Połącz iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB i DLNA. Streamuj i pobieraj dźwięk wysokiej rozdzielczości, edytuj metadane, słuchaj audiobooków, scrobbluuj do Last.fm, używaj Apple CarPlay i widgetów na ekranie głównym oraz dostosuj 10-pasmowy equalizer.'
keywords: [
  "przewodnik Flacbox", "jak używać Flacbox", "odtwarzacz muzyki hi-res iPhone", "odtwarzacz FLAC iPhone",
  "odtwarzacz DSD iOS", "odtwarzacz ALAC Mac", "aplikacja muzyczna lossless", "odtwarzacz muzyki chmurowej iPhone",
  "odtwarzacz FLAC offline Mac", "menedżer biblioteki muzycznej", "edytor tagów audio",
  "odtwarzacz FLAC CarPlay", "aplikacja audio Chromecast", "muzyka AirPlay 2",
  "widgety Flacbox", "Flacbox CarPlay", "odtwarzacz muzyki FFmpeg iOS",
  "odtwarzacz audiobooków iPhone", "zakładki audio iOS", "aplikacja do korekcji tonu",
  "częstotliwość próbkowania wyjścia audio", "zewnętrzny DAC iPhone", "USB DAC Mac",
  "aplikacja muzyczna Synology", "aplikacja muzyczna QNAP", "odtwarzacz muzyki NAS iPhone",
  "odtwarzacz WebDAV", "streaming SMB", "odtwarzacz DLNA",
  "muzyka iCloud Drive", "Google Drive FLAC", "Dropbox odtwarzacz FLAC",
  "transfer muzyki Wi-Fi Drive", "import playlisty M3U", "scrobblowanie Last.fm"
]
tags: ["flacbox", "przewodnik", "hi-res", "FLAC", "FFmpeg", "chmura", "CarPlay", "widgety"]
---


### Witaj w przewodniku Flacbox

Flacbox to odtwarzacz muzyki wysokiej rozdzielczości dla iPhone, iPad i Mac, który pozwala przekształcić ulubione usługi chmurowe, NAS i serwery mediów we własny osobisty serwis streamingowy.

Flacbox łączy się z wyjątkowo szeroką listą źródeł — wszystko w jednej aplikacji:

- **Osobista pamięć chmurowa:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Serwery lokalne:** Plex · Jellyfin · Emby · Subsonic (i każdy serwer kompatybilny z Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (i ownCloud przez wspólne API) · Synology Drive · QNAP.
- **Protokoły NAS i udostępniania plików:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (hasło lub klucz publiczny) · NFS · DLNA / UPnP (odtwarzanie i pobieranie). Działa z Apple Time Capsule, Synology, QNAP, WD My Cloud, dowolnym hostem Linux Samba / NFS / SSH lub współdzielonym folderem na Mac lub PC z Windows.
- **Kompatybilna pamięć obiektowa S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i każdy inny punkt końcowy S3-API.
- **Wykrywanie w sieci lokalnej:** Sekcja Dostępne urządzenia automatycznie wyświetla każdą usługę Bonjour / mDNS w sieci Wi-Fi — serwery Plex, Jellyfin, Emby, Synology, QNAP, routery AirPort z podłączonymi dyskami, Time Capsule — dzięki czemu możesz nawiązać połączenie bez wpisywania adresu IP.

Podczas gdy większość aplikacji muzycznych korzysta z wbudowanego silnika audio Apple, Flacbox dołącza **FFmpeg** obok systemowych kodeków, dzięki czemu możesz odtwarzać formaty, których iOS nie obsługuje natywnie — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, a także standardową rodzinę MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC. W połączeniu z konfigurowalną częstotliwością próbkowania wyjścia audio (44,1 / 48 / 64 / 88,2 / 96 kHz), wielokanałowym wyjściem (Mono → 5.1 → SDDS → ITU BS.775-1), strojeniem bufora IO i korekcją tonu, Flacbox daje audiofilom kontrolę, której większość konsumenckich aplikacji muzycznych po prostu nie oferuje.

### Ciesz się płynnym streamingiem i odtwarzaniem offline

Flacbox oferuje inteligentne buforowanie dla płynnego streamingu i wbudowany menedżer pobierania, dzięki któremu możesz pobrać całe playlisty, artystów, albumy, foldery lub pojedyncze utwory na urządzenie do użytku offline. Gdy brakuje miejsca, wyczyść pliki w pamięci podręcznej jednym dotknięciem i kontynuuj streaming z chmury. Tryb offline dla folderów, playlist, albumów i artystów automatycznie synchronizuje nowe utwory, gdy tylko pojawią się w chmurze, dzięki czemu kolekcja offline jest zawsze aktualna.

### Automatycznie zorganizowana biblioteka muzyczna

Gdy importujesz utwory audio, Flacbox skanuje ich metadane i organizuje je w przejrzystą Bibliotekę muzyczną — pogrupowaną według Utworów, Nieodtwarzanych utworów, Albumów, Artystów albumów, Artystów, Gatunków i Kompozytorów. Używaj wbudowanego wyszukiwania, aby znaleźć cokolwiek w ciągu sekund, filtruj według źródła (online w chmurze / offline / urządzenie) i wybieraj między układami biblioteki Zwykły / Pogrupowany / Karta. W przypadku bibliotek ze mieszanymi kompilacjami „różnych artystów" Flacbox zapewnia dedykowane widoki Wszystkie albumy / Wyłączne albumy / Albumy solo, aby wyświetlić odpowiednie wyniki bez szumu.

### Napraw metadane i otaguj swoją muzykę

Jeśli natrafisz na uszkodzone tagi lub nieprawidłowe kodowania (powszechny problem w przypadku zrippowanych lub starszych plików), wbudowany edytor tagów ID3 może je wyczyścić — ręcznie lub za pomocą automatycznych wyszukiwań MusicBrainz. Możesz również znormalizować uszkodzone kodowania znaków (świetne dla tagów cyrylickich, japońskich lub chińskich z PC z Windows), wyszukiwać brakujące okładki albumów i automatycznie zapisywać zmiany z powrotem do oryginalnego pliku w chmurze. Aby uzyskać głębszą edycję wsadową, zainstaluj naszą aplikację pomocniczą Evertag.

### Łatwe transfery z Mac, PC lub NAS

Przenoś muzykę między komputerem a iPhone lub iPad za pomocą dowolnego z tych narzędzi: SMB, WebDAV, DLNA, Wi-Fi Drive (przeciągnij i upuść w dowolnej przeglądarce na komputerze), Udostępnianie plików iTunes / Finder przez kabel Lightning lub USB-C, dyski USB flash lub dyski iXpand Flash. Masz Apple Time Capsule, WD My Cloud, Synology, QNAP lub inny NAS obsługujący SMB / WebDAV / DLNA / FTP / SFTP? Połącz raz i streamuj całą bibliotekę bez zajmowania miejsca na urządzeniu.

### Dostosuj dźwięk za pomocą equalizera

Flacbox zawiera 10-pasmowy equalizer ze stylowymi presetami iPod (Acoustic, Bass Booster, Classical, Dance, Rock, Pop, Jazz i wiele innych), preamplifikator oraz możliwość zapisywania własnych presetów. Niezależnie od tego, czy strojisz do słuchawek IEM dla audiofilów, HomePod mini czy samochodowego systemu audio, możesz kształtować dźwięk dokładnie tak, jak chcesz.

### Przyjazny dla audiobooków

Flacbox to świetny odtwarzacz audiobooków — wiele zakładek na utwór, precyzyjna prędkość odtwarzania (0,02× do 3,00×), kontynuacja odtwarzania dokładnie tam, gdzie przerwałeś, konfigurowalne przyciski przewijania oraz timer snu, który płynnie wycisza dźwięk przed snem. Markery rozdziałów M4B i długie pliki są w pełni obsługiwane.

### Streamuj gdziekolwiek — w tym w samochodzie i na ekranie głównym

Streamuj muzykę do Apple TV / HomePod przez AirPlay 2, wyślij ją na głośniki Google Chromecast i telewizory z Cast, i zabierz wszystko w podróż z Apple CarPlay. Używaj widgetów na ekranie głównym na iPhone i iPad, aby zobaczyć aktualnie odtwarzany utwór jednym spojrzeniem, a scrobblowanie Last.fm zapewni, że historia słuchania będzie dostępna we wszystkich aplikacjach.

### Prywatność i bezpieczeństwo

Flacbox używa wyłącznie oficjalnych zestawów SDK i logowań opartych na OAuth od każdego dostawcy chmury — Twoje hasło nigdy nie trafia do aplikacji. Tokeny dostępu są przechowywane w zaszyfrowanym formacie w iOS Keychain, wszystkie transfery są chronione TLS, a cofnięcie dostępu na koncie chmurowym lub usunięcie Flacbox z urządzenia natychmiast usuwa wszystko. Chroń swoją bibliotekę opcjonalnym kodem dostępu dla dodatkowej warstwy prywatności.

### Pierwsze kroki z Flacbox

Ten przewodnik przeprowadzi Cię przez każdą część Flacbox na iPhone, iPad i Mac — od łączenia usług chmurowych, organizowania biblioteki, transferu plików i zarządzania playlistami, po dostrajanie equalizera i konfigurowanie silnika audio. Użyj kart poniżej, aby przejść bezpośrednio do potrzebnej sekcji.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Nawigacja" subtitle="Pasek kart na iPhone, lewe menu na iPad i Mac, mini odtwarzacz, widgety, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Połączenia" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Biblioteka muzyczna" subtitle="Utwory, albumy, artyści, gatunki, kompozytorzy — synchronizacja, wyszukiwanie, edycja metadanych." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Listy odtwarzania" subtitle="Twórz, importuj M3U / M3U8 / CUE, zmieniaj kolejność i eksportuj do M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Pliki lokalne" subtitle="Muzyka offline, dyski USB, Wi-Fi Drive, menedżer plików, foldery offline." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Odtwarzacz audio" subtitle="Wyjście hi-res, equalizer, korekcja tonu, zakładki, AirPlay, Chromecast, prędkość, timer snu." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Ustawienia" subtitle="Silnik audio, biblioteka, menedżer plików, CarPlay, widgety, personalizacja, język, kopia zapasowa." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="FAQ" subtitle="Znajdź odpowiedzi na 50 najczęstszych pytań dotyczących Flacbox." >}}

{{< /cards >}}
