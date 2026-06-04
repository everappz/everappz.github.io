---
title: "Pliki"
date: 2020-02-01
lastmod: 2026-06-01
description: "Dowiedz się, jak korzystać z karty Pliki w Evervideo na iPhone, iPad i Mac. Łącz usługi w chmurze, urządzenia NAS, serwery multimediów i strumienie RTSP w jednym miejscu. Zarządzaj filmami offline, kolejką transferów, pobieraniem, Wi-Fi Drive, iTunes / Finder File Sharing i dyskami USB. Obejmuje iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA i pamięć masową zgodną z S3."
keywords: [
  "pliki Evervideo", "połączenia Evervideo", "pliki lokalne Evervideo",
  "konfiguracja wideo w chmurze iPhone", "podłącz Google Drive wideo", "strumieniowanie SMB wideo",
  "odtwarzacz WebDAV iOS", "wideo DLNA iPhone", "strumieniowanie NAS wideo",
  "transfer wideo Wi-Fi Drive", "Evervideo iTunes File Sharing", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "tryb offline wideo Evervideo", "kolejka transferów Evervideo",
  "menedżer plików Evervideo", "folder Dokumenty Evervideo",
  "odtwarzacz wideo Synology", "odtwarzacz wideo QNAP",
  "odtwarzacz wideo Apple Time Capsule", "USB DAC wideo",
  "odtwarzacz wideo iXpand", "odtwarzacz wideo S3"
]
tags: ["poradnik", "evervideo", "pliki", "połączenia", "chmura", "NAS", "Plex", "RTSP"]
readingTime: 14
---

Karta Pliki to wszechstronny menedżer plików Evervideo. W przeciwieństwie do większości aplikacji wideo, które dzielą pamięć masową w chmurze od plików lokalnych na różne karty, Evervideo łączy oba w jeden, przewijalny ekran, dzięki czemu możesz przechodzić z serwera Plex do folderu w chmurze do folderu Dokumenty na iPhonie bez przeskakiwania między kartami.

Karta Pliki jest podzielona na wyraźne sekcje, które pojawiają się w tej kolejności na ekranie:

- **Szybki dostęp** — ostatnie i ulubione pliki i foldery, które ostatnio otwierałeś.
- **Pliki w tej aplikacji** — to, co znajduje się w piaskownicy folderu Dokumenty Evervideo.
- **Pliki na tym iPhone / iPad / Mac** — filmy w innych miejscach na urządzeniu, dostępne przez systemowy selektor plików.
- **Pamięć masowa w chmurze** — każde podłączone konto w chmurze, NAS i serwer multimediów.
- **Dostępne urządzenia** — serwery i dyski automatycznie wykryte przez Bonjour / mDNS w sieci lokalnej.

W prawym górnym rogu ekranu Pliki znajduje się przycisk Transfery (ikona obracających się strzałek). Dotknij go, aby otworzyć kolejkę transferów, gdzie monitorujesz każde pobranie i przesłanie z wszystkich źródeł.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — pliki w połączonych pamięciach masowych" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Podłącz do pamięci masowej w chmurze

Sekcja Pamięć masowa w chmurze na karcie Pliki to miejsce, gdzie mieszkają wszystkie podłączone konta, NAS-y, serwery multimediów i strumienie — obok siebie na jednej przewijalnej liście.

{{< cards cols="1">}}
  {{< card title="" subtitle="Sekcja Pamięć masowa w chmurze na karcie Pliki w Evervideo" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Otwórz kartę **Pliki**.
- Przewiń do sekcji **Pamięć masowa w chmurze**.
- Dotknij **Połącz z pamięcią masową w chmurze** z menu.
- Wybierz usługę pamięci masowej w chmurze z listy.
- Wprowadź swoje dane uwierzytelniające na oficjalnej stronie autoryzacji dostarczonej przez dostawcę chmury, a następnie dotknij **Gotowe**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — podłącz usługę pamięci masowej w chmurze" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Jeśli napotkasz problemy, sprawdź połączenie internetowe oraz login / hasło. W wersji Premium aplikacji możesz dodać nieograniczoną liczbę usług; wersja bezpłatna obsługuje do trzech.

## Obsługiwane usługi pamięci masowej w chmurze, serwery multimediów i protokoły

Evervideo obsługuje wyjątkowo szeroki zakres źródeł dla Twoich filmów. Wszystko poniżej działa z jednego przepływu Połącz z pamięcią masową w chmurze.

**Osobista pamięć masowa w chmurze:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Własne serwery multimediów:** Plex · Jellyfin · Emby · Subsonic (i każdy serwer kompatybilny z Subsonic — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (i ownCloud przez wspólne API) · Synology Drive · QNAP.

**Protokoły NAS i udostępniania plików:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, hasło lub uwierzytelnianie kluczem publicznym) · NFS · DLNA / UPnP (odtwarzanie i pobieranie).

**Strumienie na żywo i kamery IP:** RTSP — wskaż Evervideo dowolny adres URL `rtsp://` i po prostu odtwarza. Świetne do kamer bezpieczeństwa, strumieni IPTV, kamer wideo-domofonu, niań elektronicznych i podobnych źródeł na żywo.

**Pamięć obiektowa zgodna z S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i każdy inny punkt końcowy API S3.

**Biblioteki na urządzeniu:** biblioteka Zdjęć (wszystkie filmy, nagrania ekranu, albumy zdjęć) i biblioteka aplikacji Muzyka (Albumy, Gatunki, Listy odtwarzania) — obie dostępne z wnętrza Biblioteki multimediów, bez konieczności kopiowania czegokolwiek.

**Odkrywanie sieci lokalnej:** sekcja Dostępne urządzenia automatycznie wyświetla wszystkie usługi Bonjour / mDNS w sieci Wi-Fi — Plex, Jellyfin, Emby, Synology, QNAP, routery AirPort z podłączonymi dyskami, Apple Time Capsule — dzięki czemu możesz dotknąć, aby połączyć bez wpisywania adresu IP.

Każde połączenie używa oficjalnego SDK lub otwartego protokołu usługi, z autoryzacją OAuth tam, gdzie jest obsługiwana. Możesz połączyć wiele kont tej samej usługi (na przykład dwa konta Google Drive lub zarówno serwer Plex, jak i Jellyfin) i przeglądać je obok siebie w sekcji Pamięć masowa w chmurze.

## Bezpieczeństwo i prywatność

Evervideo używa wyłącznie oficjalnych SDK i bezpiecznych połączeń do interakcji z podłączonymi usługami w chmurze. Login i hasło nie są dostępne dla aplikacji — wszystkie transfery są szyfrowane TLS.

Gdy wprowadzasz login i hasło, aplikacja pokazuje Ci oficjalną stronę autoryzacji dostarczoną przez dostawcę usług w chmurze, a cały proces autoryzacji odbywa się poza aplikacją. Dostawca usług w chmurze następnie wysyła token autoryzacyjny do aplikacji po pomyślnej autoryzacji, a ten token jest używany do wykonywania wywołań API.

Token autoryzacyjny to cyfrowy klucz, który pozwala aplikacjom innych firm na interakcję z pamięcią masową w chmurze w Twoim imieniu. Token jest przechowywany na urządzeniu w bezpiecznym systemowym magazynie Apple (Keychain), który jest szyfrowany w spoczynku i chroniony kodem dostępu urządzenia lub biometryczną blokadą. Możesz pobierać pliki z podłączonych usług w chmurze na urządzenie; te pliki są umieszczane w katalogu Dokumenty aplikacji i można je usunąć w dowolnym momencie za pomocą wbudowanego menedżera plików.

Aplikacja nie udostępnia żadnych informacji z Twoich podłączonych kont w chmurze Everappz, reklamodawcom ani żadnym osobom trzecim. Możesz w dowolnym momencie odwołać dostęp do swojego konta w chmurze, otwierając stronę ustawień konta w przeglądarce internetowej.

## Odwołanie tokenu autoryzacyjnego

Aby odwołać token autoryzacyjny, zaloguj się do swojego konta w chmurze w przeglądarce internetowej i przejdź do strony zabezpieczeń lub podłączonych aplikacji. Tam możesz znaleźć każdą aplikację innej firmy podłączoną do Twojego konta w chmurze i usunąć dowolną z nich, jeśli nie chcesz jej już używać. Szczegółowe instrukcje dla kont Google są dostępne [tutaj](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Możesz również odłączyć konto w chmurze wewnątrz samej aplikacji — gdy to zrobisz, token autoryzacyjny jest natychmiast usuwany z urządzenia. Jeśli odinstalowujesz aplikację z urządzenia, wszystkie pobrane dane i tokeny dostępu są automatycznie usuwane wraz z nią.

## Odłącz pamięć masową w chmurze lub zmień konfigurację

- **Dostęp do opcji pamięci masowej w chmurze** — zlokalizuj podłączoną usługę w sekcji **Pamięć masowa w chmurze** na karcie Pliki.
- **Dotknij przycisku „..."** obok tytułu usługi, aby otworzyć dodatkowe opcje:
  - **Zmień nazwę** — zmień nazwę usługi w chmurze, jak pojawia się na Twojej liście.
  - **Ustawienia** — zmodyfikuj konfigurację lub dane uwierzytelniające. Czasami może być konieczna ponowna autoryzacja podłączonej usługi w chmurze, jeśli token autoryzacyjny wygasł.
  - **Rozłącz** — całkowicie zerwij połączenie między aplikacją a usługą w chmurze. Usuwa wszystkie filmy powiązane z tą usługą z biblioteki multimediów, ale pozostawia je nietkniętymi na serwerze.

## Podłącz do komputera lub NAS

Możesz podłączyć komputer, osobisty NAS lub inne urządzenie sieciowe używając protokołu SMB, WebDAV, FTP / FTPS, SFTP, NFS lub DLNA. To najłatwiejszy sposób na przeniesienie istniejącej domowej biblioteki multimediów — niezależnie od tego, czy jest ona na Mac, Windows PC, Synology, QNAP, Apple Time Capsule, czy WD My Cloud Home — do Evervideo bez kopiowania czegokolwiek.

### Podłącz do komputera przy użyciu SMB

- Dotknij **Połącz z pamięcią masową w chmurze → SMB**.
- Wprowadź adres IP komputera i nazwę folderu współdzielonego w formacie `smb://adres-ip-komputera/nazwa-folderu-wspoldzielonego`.
- Wybierz wersję protokołu: **Auto**, **SMB1** lub **SMB2**.
- Wprowadź login i hasło (jeśli wymagane).
- Dotknij **Gotowe**.

Jeśli połączenie powiedzie się, udział pojawi się w sekcji Pamięć masowa w chmurze. Pełny samouczek dotyczący łączenia Mac lub PC za pomocą SMB jest dostępny [tutaj](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Podłącz do NAS za pomocą WebDAV

Wszystkie kroki są takie same jak w SMB, z wyjątkiem pola URL. Użyj `http://nazwa-serwera` lub `https://nazwa-serwera`, jeśli serwer obsługuje SSL. WebDAV działa z Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home i każdym innym serwerem z punktem końcowym WebDAV.

Pełny samouczek dotyczący WebDAV jest dostępny [tutaj](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Podłącz przez DLNA / UPnP

Udostępnij bibliotekę multimediów znajdującą się na komputerze z systemem Windows lub NAS przy użyciu protokołu DLNA / UPnP i uzyskaj do niej dostęp z Evervideo zgodnie z opisem [tutaj](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA jest szeroko obsługiwany, ale pozwala tylko na odtwarzanie lub pobieranie filmów — nie możesz przesyłać plików ani tworzyć nowych folderów na serwerze DLNA.

### Podłącz przy użyciu FTP, FTPS lub SFTP

Evervideo obsługuje również klasyczne protokoły transferu plików. Aby połączyć serwer przez FTP lub FTPS, dotknij Połącz z pamięcią masową w chmurze → FTP, wprowadź adres URL hosta w postaci `ftp://nazwa-serwera` (lub `ftps://nazwa-serwera` dla szyfrowanego połączenia), podaj login i hasło, a następnie dotknij Gotowe. W przypadku SFTP (SSH File Transfer Protocol) wybierz SFTP i podaj hasło lub parę kluczy SSH.

### Podłącz do udziału NFS

Evervideo zawiera obsługę NFS (Network File System) — przydatną dla hostów Linux, serwerów BSD i urządzeń NAS, które preferują udostępnianie bibliotek wideo przez NFS zamiast SMB. Wybierz NFS w menu Połącz z pamięcią masową w chmurze, wprowadź adres serwera i eksportowaną ścieżkę, a następnie dotknij Gotowe.

## Podłącz serwer Plex Media Server

Evervideo może połączyć się bezpośrednio z Plex Media Server i przeglądać biblioteki Filmy, Seriale TV i Domowe filmy. Dotknij Połącz z pamięcią masową w chmurze → Plex, zaloguj się na swoje konto Plex, wybierz serwer, a biblioteka pojawi się obok usług w chmurze. Serwery Plex w tej samej sieci lokalnej są również automatycznie wykrywane w sekcji Dostępne urządzenia.

## Podłącz serwer Jellyfin lub Emby

Zarówno Jellyfin (open-source), jak i Emby (komercyjny) serwery multimediów działają natywnie w Evervideo. Dotknij Połącz z pamięcią masową w chmurze → Jellyfin lub Emby, wprowadź adres URL serwera (zazwyczaj coś w stylu `http://ip-serwera:8096`) i dane uwierzytelniające, a Twoja biblioteka jest gotowa do strumieniowania.

## Podłącz serwer Subsonic lub Navidrome

Evervideo obsługuje API Subsonic, co oznacza, że działa z samym Subsoniciem, Navidrome i każdym innym serwerem kompatybilnym z Subsoniciem — w tym Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) i Ampache. Dotknij Połącz z pamięcią masową w chmurze → Subsonic, wprowadź adres URL serwera i dane uwierzytelniające, a biblioteka pojawi się w sekcji Pamięć masowa w chmurze.

## Podłącz strumień RTSP (kamery IP, Live TV, IPTV)

Evervideo ma natywną obsługę RTSP, dzięki czemu możesz skierować go na dowolne źródło RTSP — kamery bezpieczeństwa, kamery wideo-domofonu, dostawców IPTV, nianie elektroniczne, sygnały nadawcze — a Evervideo pobierze i zdekoduje strumień na żywo. Dotknij Łącza online → Dodaj link, wklej pełny adres URL (`rtsp://adres-kamery:port/ścieżka-strumienia`), podaj login i hasło jeśli wymagane, i dotknij Gotowe.

## Podłącz do pamięci obiektowej zgodnej z S3

Dla osób z własnym hostingiem i zaawansowanych użytkowników korzystających z obiektowej pamięci masowej w chmurze, Evervideo zawiera konektor zgodny z S3. Dotknij Połącz z pamięcią masową w chmurze → Pamięć S3, a następnie wprowadź adres URL punktu końcowego, region, klucz dostępu, tajny klucz i nazwę bucketa. Działa z AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i każdym innym punktem końcowym API S3.

## Dostępne urządzenia

Ta sekcja wyświetla wszystkie urządzenia w sieci lokalnej, z którymi możesz połączyć się z Evervideo przez wykrywanie Bonjour / mDNS — serwery Plex, Jellyfin, Emby, Synology, QNAP, routery AirPort z podłączonymi dyskami, Apple Time Capsule i tym podobne. Aby nawiązać połączenie:

- Przewiń do sekcji Dostępne urządzenia na karcie Pliki.
- Dotknij urządzenia, z którym chcesz się połączyć.
- W razie potrzeby wprowadź dane logowania, aby zakończyć połączenie.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — dostępne urządzenia w sieci lokalnej" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive pozwala bezprzewodowo transferować pliki z komputera do urządzenia iOS przez dowolną przeglądarkę desktopową, Finder lub Eksplorator plików. Twoje urządzenie i komputer muszą być w tej samej sieci Wi-Fi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Włącz Wi-Fi Drive

- Na karcie Pliki przewiń do Pamięć masowa w chmurze → Połącz przez Wi-Fi, aby otworzyć główny ekran Wi-Fi Drive.
- (Opcjonalnie) Ustaw nazwę użytkownika i hasło dla wbudowanego serwera WWW.
- Dotknij Uruchom Wi-Fi Drive.

### Dostęp do Wi-Fi Drive na komputerze

- Otwórz przeglądarkę internetową na komputerze (Chrome, Firefox, Safari itp.).
- Wprowadź adres URL wyświetlany przez aplikację.
- Przeciągnij i upuść pliki z komputera na stronę internetową — rozpoczną się transfery do urządzenia iOS.

Możesz również zamontować Wi-Fi Drive bezpośrednio w **Finderze** na macOS (Idź → Połącz z serwerem…) lub Eksploratorze plików na Windows (Mapuj dysk sieciowy…) i traktować iPhone lub iPad jak zwykły dysk sieciowy.

Szczegółowe instrukcje są dostępne [tutaj](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (teraz Finder File Sharing na macOS Catalina i nowszych) pozwala transferować pliki za pomocą kabla Lightning lub USB-C. Podłącz urządzenie, otwórz Finder na Mac (lub iTunes na Windows), znajdź Evervideo na liście aplikacji i skopiuj pliki do jego folderu współdzielonego.

## Podłącz pendrive USB lub kartę SD

Podłącz pendrive USB lub kartę SD do iPhone, iPad lub Mac przez adapter Lightning-do-USB / USB-C lub czytnik kart. Otwórz Pliki → Pliki na tym iPhone → Otwórz folder, przejdź do dysku i wybierz plik wideo lub folder. Evervideo odtwarza pliki bezpośrednio z dysku bez kopiowania ich do pamięci wewnętrznej — przydatne w przypadku bardzo dużych bibliotek 4K.

## Przeglądanie folderów w podłączonych pamięciach masowych

Dotknij dowolnej podłączonej usługi w chmurze, aby otworzyć jej przeglądarkę plików. Foldery pokazują miniatury wideo, gdy są dostępne, a dotknięcie wideo natychmiast rozpoczyna odtwarzanie, kontynuując jednocześnie strumieniowanie reszty pliku w tle.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — przeglądanie folderów w podłączonych pamięciach masowych" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Szybki dostęp

Sekcja Szybki dostęp znajduje się na górze karty Pliki. Daje szybki dostęp do ulubionych i ostatnio otwartych plików i folderów — zarówno z usług w chmurze, jak i z pamięci na urządzeniu. Gdy otwierasz plik lub folder z chmury, jest on dodawany do listy Ostatnio otwarte. Możesz oznaczyć głęboko zagnieżdżone foldery jako Ulubione, aby uzyskać do nich szybki dostęp bez przeszukiwania struktury katalogów.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — łącza online i szybki dostęp" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Pliki w tej aplikacji

Ta sekcja pokazuje pliki i foldery przechowywane w piaskownicy katalogu Dokumenty Evervideo — wszystko, co pobrałeś z chmury, przetransferowałeś przez Wi-Fi Drive, skopiowałeś przez Finder File Sharing lub zaimportowałeś z innej aplikacji.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — pliki w tej aplikacji" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Folder Dokumenty

Folder Dokumenty jest korzeniem wszystkiego wewnątrz Pliki w tej aplikacji. Możesz tworzyć podfoldery, zmieniać nazwy plików, przenosić je i grupować je dowolnie.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — pliki lokalne — folder Dokumenty" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Pliki na tym iPhone / iPad / Mac

Ta sekcja pokazuje filmy znajdujące się na urządzeniu, ale w innych aplikacjach. Możesz je importować do Evervideo za pomocą systemowego selektora plików:

- Dotknij Otwórz pliki…, aby wybrać konkretne pliki.
- Dotknij Otwórz folder…, aby wybrać cały folder.

Możesz też użyć Podłącz folder, aby utworzyć łącze do folderu na urządzeniu z dostępem do odczytu / zapisu — idealne do pracy z folderem na iCloud Drive lub podłączonym dysku USB bez kopiowania czegokolwiek.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — pliki na tym urządzeniu" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Foldery specjalne

Na karcie Pliki zobaczysz kilka folderów specjalnych, które Evervideo tworzy i używa automatycznie:

- **Pobrania** — każdy plik pobrany z chmury pojawia się tutaj domyślnie. Dostosuj w Ustawienia → Menedżer plików → Zapisz pobrane pliki do.
- **Pamięć podręczna odtwarzacza** — pamięć podręczna odtwarzacza multimediów. Domyślnie odtwarzacz pobiera nadchodzące filmy dla płynnego odtwarzania. Możesz wyłączyć pamięć podręczną w ustawieniach aplikacji lub po prostu usunąć ten folder.
- **iCloud** — pliki w tym folderze synchronizują się na wszystkich urządzeniach podłączonych do tego samego konta iCloud.
- **Foldery offline** — gdy oznaczasz folder, listę odtwarzania, album lub gatunek jako dostępny offline, pliki są pobierane do tego folderu.

## Górny pasek narzędzi

Górny pasek narzędzi, umieszczony pod paskiem nawigacji, oferuje kilka akcji, które możesz pokazać lub ukryć gestem przesunięcia w dół:

- **Szukaj** — przeszukaj bieżący folder lub sekcję.
- **Kontynuuj odtwarzanie** — jeśli włączone w ustawieniach, przywróć kolejkę odtwarzacza i ostatnią pozycję wideo dla bieżącego folderu.
- **Odtwórz wszystkie** — skanuj bieżący folder i jego podfoldery i dodaj pliki do kolejki odtwarzacza.
- **Losuj wszystkie** — jak Odtwórz wszystkie, ale losuje przed dodaniem.

## Opcje folderu

Gdy otwierasz folder, dotknij przycisku **„..."** w prawym górnym rogu, aby uzyskać dostęp do tych akcji:

- **Wybrać** — aktywuj tryb wyboru plików.
- **Nowy folder** — utwórz nowy folder w bieżącym folderze.
- **Włączyć tryb offline** — włącz synchronizację offline dla bieżącego folderu. Nowe pliki dodane online są pobierane automatycznie.
- **Prześlij pliki** — prześlij pliki z urządzenia do folderu online.
- **Szukaj** — szukaj w folderze.
- **Sortuj** — sortuj pliki według nazwy, rozmiaru, daty modyfikacji lub metadanych.
- **Widok siatki / listy** — przełącz między widokiem tabeli a widokiem miniatur. Widok miniatur pokazuje duże podglądy okładek filmów.

## Tryb wyboru

Dotknij **„..."** w prawym górnym rogu i wybierz **Wybrać**, aby wejść w tryb wyboru. Przy każdym pliku i folderze pojawiają się pola wyboru. Dotknij, aby wybrać jeden lub kilka elementów, a następnie wykonaj działania zbiorcze: Odtwórz następny, Odtwórz później, Dodaj do biblioteki multimediów, Dodaj do listy odtwarzania, Kopiuj, Prześlij, Przenieś, Zmień nazwę lub Usuń.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — tryb wyboru w menedżerze plików" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Jeśli wolisz traktować podłączoną pamięć masową w chmurze jako tylko do odczytu (aby zapobiec przypadkowemu usuwaniu), włącz Ustawienia → Menedżer plików → Edytuj pliki online → Wył., aby ukryć wszystkie destrukcyjne operacje z interfejsu użytkownika.

## Akcje pliku

Dotknij ikony **„..."** obok tytułu pliku, aby wyświetlić menu akcji:

- **Odtwórz następny** — wstaw plik na górę kolejki odtwarzacza.
- **Odtwórz później** — dołącz plik na dole kolejki odtwarzacza.
- **Dodaj do biblioteki multimediów** — włącz plik do biblioteki multimediów, zorganizowanej według Albumu i Gatunku.
- **Dodaj do listy odtwarzania** — dodaj plik do istniejącej listy odtwarzania lub utwórz nową.
- **Edytuj tagi** — otwórz wbudowany edytor tagów do modyfikacji metadanych. W przypadku plików online plik jest tymczasowo pobierany, edytowany, a następnie ponownie przesyłany po potwierdzeniu.
- **Dodaj do ulubionych** — dodaj plik do listy ulubionych dla szybkiego dostępu.
- **Pobierz** — pobierz plik lub folder na urządzenie do użytku offline.
- **Zmień nazwę** — zmień nazwę pliku bezpośrednio w zdalnej pamięci masowej.
- **Przenieś** — przenieś plik do innego folderu w pamięci masowej w chmurze.
- **Dodaj do archiwum** — spakuj plik do jednego pliku ZIP (funkcja Premium).
- **Otwórz w** — wyeksportuj plik do innej kompatybilnej aplikacji przez systemowy arkusz udostępniania.
- **Usuń** — trwale usuń plik. **Tej akcji nie można cofnąć.**

## Akcje folderu

Dla każdego folderu w pamięci masowej w chmurze masz wiele dostępnych akcji, dotykając ikony **„..."** obok tytułu folderu.

- **Odtwórz wszystkie** — zastąp bieżącą kolejkę odtwarzacza każdym filmem w folderze.
- **Odtwórz następny / Odtwórz później** — dodaj cały folder do kolejki.
- **Dodaj do biblioteki multimediów** — włącz zawartość folderu do biblioteki multimediów.
- **Dodaj do listy odtwarzania** — dodaj cały folder do listy odtwarzania.
- **Dodaj do ulubionych** — dodaj folder do ulubionych.
- **Włącz tryb offline** — poza prostym pobieraniem, ta opcja stale monitoruje folder pod kątem nowych plików i automatycznie je pobiera, gdy pojawią się online.
- **Pobierz** — pobierz całą zawartość folderu na urządzenie do dostępu offline.
- **Zmień nazwę / Przenieś** — zmień nazwę lub przenieś folder w zdalnej pamięci masowej.
- **Dodaj do archiwum** — spakuj zawartość folderu do pliku ZIP (funkcja Premium).
- **Usuń** — trwale usuń folder i jego zawartość. **Tej akcji nie można cofnąć.**

## Kolejka transferów

W prawym górnym rogu karty Pliki znajduje się przycisk **Transfery** (ikona obracających się strzałek). Dotknij go, aby otworzyć Kolejkę transferów — listę każdego aktywnego pobierania i przesyłania ze wszystkich źródeł, z postępem w czasie rzeczywistym, prędkością i szacowanym czasem ukończenia na plik.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — kolejka transferów plików" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Możesz wstrzymywać, wznawiać, ponawiać nieudane transfery, zmieniać kolejność elementów, aby nadać priorytet konkretnym pobieraniom, lub anulować je indywidualnie. Możesz również dostosować prędkość kolejki transferów (maksymalna liczba równoległych zadań), typ sieci (tylko Wi-Fi lub Wi-Fi + sieć komórkowa) i transfery w tle w Ustawienia → Menedżer plików.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — akcje w kolejce transferów plików" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Tryb offline i zsynchronizowane foldery offline

Tryb offline to przydatna funkcja, która pozwala oglądać ulubione filmy nawet wtedy, gdy nie jesteś podłączony do Internetu. Gdy włączysz tryb offline dla dowolnego folderu, listy odtwarzania, albumu lub gatunku, wszystkie pliki w tej kolekcji są automatycznie pobierane na urządzenie do odtwarzania offline. Pojawiają się w sekcji Foldery offline.

Gdy dodajesz nowe pliki do zdalnego serwera, są one również automatycznie pobierane — dzięki czemu kolekcja offline pozostaje aktualna bez żadnego działania z Twojej strony. Aby ręcznie zsynchronizować, dotknij trzech kropek w prawym górnym rogu folderu offline i wybierz Synchronizować.

Możesz dostosować limit czasu synchronizacji w Ustawienia → Menedżer plików → Zsynchronizowane foldery offline → Interwał czasowy.

Szczegółowe instrukcje są dostępne [tutaj](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personalizacja

W Ustawienia → Personalizacja możesz skonfigurować sposób prezentowania karty Pliki:

- **Styl ekranu Pliki** — Zwykłe menu (pokazuje listę folderów bezpośrednio) lub Grupowane menu (grupuje zawartość według kategorii — Szybki dostęp, Foldery specjalne, Pamięć masowa w chmurze itp.).
