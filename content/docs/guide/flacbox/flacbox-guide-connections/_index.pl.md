---
title: "Połączenia"
date: 2020-02-01
description: "Dowiedz się, jak połączyć usługi chmurowe i urządzenia NAS z Flacbox. Streamuj muzykę wysokiej rozdzielczości z iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk i innych. Używaj SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, Udostępniania plików iTunes / Finder i dysków USB flash."
keywords: [
  "konfiguracja chmury Flacbox", "połącz Google Drive z Flacbox", "streaming SMB",
  "odtwarzacz WebDAV iOS", "aplikacja DLNA", "streaming audio NAS", "Wi-Fi Drive iPhone",
  "transfer plików na iPhone", "Flacbox Udostępnianie plików iTunes", "połącz NAS z iPhone",
  "aplikacja muzyczna Synology Drive", "aplikacja muzyczna QNAP", "aplikacja muzyczna Bluesound",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "aplikacja muzyczna scrobblowanie Last.fm",
  "muzyka iXpand Flash Drive", "USB DAC iPhone"
]
tags: ["przewodnik", "flacbox", "połączenia", "chmura", "NAS"]
readingTime: 12
---


Na tym ekranie możesz połączyć każde źródło, które przechowuje Twoją muzykę. Możesz zintegrować popularne usługi chmurowe, takie jak Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive i wiele innych, a także Twój Mac, PC lub NAS za pomocą standardowych protokołów. Niezależnie od tego, czy Twoja kolekcja znajduje się w usłudze przyjaznej streamingowi, takiej jak Dropbox, czy na osobistym NAS-ie, takim jak Synology, QNAP, Buffalo, Apple Time Capsule lub WD My Cloud Home, Flacbox łączy się ze wszystkimi z jednego ekranu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ekran Połączeń Flacbox" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Połącz z Pamięcią Chmurową

- Otwórz kartę **Połączenia**.
- Wybierz **Połącz z pamięcią chmurową** z menu.
- Wybierz usługę przechowywania w chmurze z listy.
- Wprowadź swoje dane uwierzytelniające na oficjalnej stronie autoryzacji udostępnionej przez dostawcę chmury, a następnie dotknij **Zrobione**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Dodaj Usługę Pamięci Chmurowej" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Jeśli napotkasz problemy, sprawdź połączenie internetowe oraz login / hasło. W wersji Premium aplikacji możesz dodać nieograniczoną liczbę usług; wersja bezpłatna obsługuje do trzech.

## Obsługiwane Usługi Przechowywania w Chmurze, Serwery Multimediów i Protokoły

Flacbox obsługuje wyjątkowo szeroki zakres źródeł muzyki. Wszystko poniżej działa z jednego ekranu **Połącz z pamięcią chmurową**.

**Osobista pamięć chmurowa:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Serwery lokalne:** Plex · Jellyfin · Emby · Subsonic (i każdy serwer kompatybilny z Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (i ownCloud przez wspólne API) · Synology Drive · QNAP.

**Protokoły NAS i udostępniania plików:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, hasło lub klucz publiczny) · NFS · DLNA / UPnP (odtwarzanie i pobieranie).

**Kompatybilna pamięć obiektowa S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i każdy inny punkt końcowy S3-API.

**Wykrywanie w sieci lokalnej:** Sekcja Dostępne urządzenia automatycznie wyświetla każdą usługę Bonjour / mDNS w sieci Wi-Fi, dzięki czemu możesz nawiązać połączenie bez wpisywania adresu IP.

Każde połączenie używa **oficjalnego SDK lub otwartego protokołu** danej usługi, z autoryzacją opartą na OAuth tam, gdzie jest obsługiwana. Możesz połączyć wiele kont tej samej usługi (na przykład dwa konta Google Drive, osobiste Dropbox obok służbowego lub zarówno serwer Plex, jak i Jellyfin) i przeglądać je obok siebie na ekranie Połączeń.

## Bezpieczeństwo i Prywatność

Używamy wyłącznie oficjalnych SDK i bezpiecznych połączeń do interakcji z podłączonymi usługami chmurowymi. Twój login i hasło nie są dostępne dla aplikacji — wszystkie transfery są zaszyfrowane TLS.

Po wprowadzeniu loginu i hasła aplikacja pokazuje oficjalną stronę autoryzacji udostępnioną przez dostawcę usług chmurowych, a cały proces autoryzacji odbywa się poza aplikacją. Dostawca usług chmurowych następnie wysyła token autoryzacyjny do aplikacji po pomyślnej autoryzacji, a ten token jest używany do wykonywania wywołań API.

Token autoryzacyjny to cyfrowy klucz, który umożliwia aplikacjom innych firm interakcję z pamięcią chmurową w Twoim imieniu. Token jest przechowywany na Twoim urządzeniu w bezpiecznym systemowym magazynie Apple (Keychain), który jest zaszyfrowany w spoczynku i chroniony kodem dostępu do urządzenia lub blokadą biometryczną. Możesz pobierać pliki z podłączonych usług chmurowych na urządzenie; pliki te są umieszczane w katalogu Dokumenty aplikacji i można je usunąć w dowolnym momencie za pomocą wbudowanego menedżera plików.

Aplikacja nie udostępnia żadnych informacji z Twoich podłączonych kont chmurowych firmie Everappz, reklamodawcom ani żadnej osobie trzeciej. Możesz cofnąć dostęp do swojego konta chmurowego w dowolnym momencie, otwierając stronę ustawień konta w przeglądarce internetowej.

## Odrzuć Token Autoryzacyjny

Aby odwołać token autoryzacyjny, zaloguj się na konto chmurowe w przeglądarce internetowej i przejdź do strony bezpieczeństwa lub podłączonych aplikacji. Tam możesz znaleźć każdą aplikację innej firmy, która jest podłączona do Twojego konta chmurowego i usunąć dowolną z nich, jeśli nie chcesz już jej używać. Szczegółowe instrukcje dotyczące kont Google są dostępne [tutaj](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Możesz również rozłączyć konto chmurowe wewnątrz samej aplikacji — gdy to zrobisz, token autoryzacyjny jest natychmiast usuwany z urządzenia. Jeśli odinstalowujesz aplikację z urządzenia, wszystkie pobrane dane i tokeny dostępu są automatycznie usuwane wraz z nią.

## Rozłącz Pamięć Chmurową lub Zmień Konfigurację

- **Uzyskaj dostęp do opcji pamięci chmurowej** — znajdź podłączoną usługę na ekranie **Połączenia**.
- **Dotknij przycisku „..."** obok tytułu usługi, aby otworzyć dodatkowe opcje:
  - **Zmień nazwę** — zmień nazwę usługi chmurowej, która pojawia się na liście.
  - **Ustawienia** — zmodyfikuj konfigurację lub dane uwierzytelniające. Czasem może być konieczna ponowna autoryzacja podłączonej usługi chmurowej, jeśli token autoryzacji wygasł.
  - **Rozłącz** — całkowicie odetnij połączenie między aplikacją a usługą chmurową. Spowoduje to usunięcie wszystkich utworów powiązanych z tą usługą z biblioteki muzycznej aplikacji, ale pozostawi je nienaruszone na serwerze.

## Połącz z Komputerem lub NAS

Możesz również podłączyć komputer, osobisty NAS lub inne urządzenia sieciowe za pomocą protokołów SMB, DLNA lub WebDAV. To najprostszy sposób na wprowadzenie istniejącej domowej biblioteki muzycznej — niezależnie od tego, czy znajduje się na Macu, PC z Windows, urządzeniu Synology czy NAS — do Flacbox bez kopiowania czegokolwiek.

## Połącz z Komputerem za Pomocą SMB

- Dotknij **Połącz z pamięcią chmurową → SMB**.
- Wprowadź adres IP komputera i nazwę folderu współdzielonego w polu URL w formacie `smb://ip-komputera/nazwa-folderu-wspoldzielonego`.
- Wybierz wersję protokołu: **Auto**, **SMB1** lub **SMB2**.
- Wprowadź login i hasło (jeśli wymagane).
- Dotknij **Zrobione**.

Jeśli połączenie zakończy się sukcesem, zobaczysz podłączone urządzenie w sekcji **Pamięć w chmurze**. Pełny samouczek dotyczący połączenia Mac lub PC za pomocą SMB jest dostępny [tutaj](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Połącz z NAS za Pomocą WebDAV

Wszystkie kroki są takie same jak w przypadku SMB, z wyjątkiem pola URL. URL powinien być w formacie `http://nazwa-serwera` lub `https://nazwa-serwera`, jeśli serwer obsługuje SSL. WebDAV działa z **Synology, QNAP, Nextcloud, ownCloud** i wieloma innymi serwerami — wszędzie tam, gdzie dostępny jest punkt końcowy WebDAV.

Pełny samouczek dotyczący połączenia NAS za pomocą WebDAV jest dostępny [tutaj](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Połącz z Komputerem lub NAS za Pomocą DLNA

Możesz również udostępnić bibliotekę muzyczną znajdującą się na Twoim PC z Windows lub osobistym NAS za pomocą protokołu DLNA / UPnP i uzyskać dostęp do tej biblioteki w aplikacji, jak opisano [tutaj](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA to popularny, szeroko obsługiwany protokół, ale pozwala tylko na odtwarzanie lub pobieranie muzyki — nie możesz przesyłać plików ani tworzyć nowych folderów na serwerze DLNA.

## Połącz z NAS lub Serwerem za Pomocą FTP, FTPS lub SFTP

Flacbox obsługuje również klasyczne protokoły transferu plików. Aby połączyć serwer przez FTP lub FTPS, dotknij **Połącz z pamięcią chmurową → FTP**, wprowadź adres URL hosta w formie `ftp://nazwa-serwera` (lub `ftps://nazwa-serwera` dla zaszyfrowanego połączenia), podaj login i hasło, a następnie dotknij **Zrobione**. W przypadku **SFTP** (SSH File Transfer Protocol) wybierz **SFTP** zamiast tego i podaj albo hasło, albo parę kluczy SSH. Oba działają z urządzeniami NAS, hostami Linux i każdym serwerem, który ma demona FTP / FTPS / SSH.

## Połącz z Udziałem NFS

Flacbox obsługuje **NFS** (Network File System) — przydatne dla hostów Linux, serwerów BSD i urządzeń NAS, które preferują udostępnianie bibliotek muzycznych przez NFS zamiast SMB. Wybierz **NFS** w menu **Połącz z pamięcią chmurową**, wprowadź adres serwera i eksportowaną ścieżkę, a następnie dotknij **Zrobione**.

## Połącz Serwer Plex Media Server

Flacbox może połączyć się bezpośrednio z Plex Media Server i przeglądać bibliotekę muzyczną według Artystów, Albumów, Gatunków i Playlist. Dotknij **Połącz z pamięcią chmurową → Plex**, zaloguj się na konto Plex, wybierz serwer, a biblioteka pojawi się obok usług chmurowych. Serwery Plex w tej samej sieci lokalnej są również wykrywane automatycznie w sekcji **Dostępne urządzenia**.

## Połącz Serwer Jellyfin lub Emby

Zarówno **Jellyfin** (open-source), jak i **Emby** (komercyjny) serwery multimediów działają natywnie w Flacbox. Dotknij **Połącz z pamięcią chmurową → Jellyfin** lub **Emby**, wprowadź adres URL serwera (coś w stylu `http://ip-serwera:8096`) i dane uwierzytelniające, a Twoja biblioteka muzyczna jest gotowa do streamingu. Podobnie jak w przypadku Plex, biblioteki w sieci lokalnej są automatycznie wyświetlane w **Dostępne urządzenia**.

## Połącz Serwer Subsonic lub Navidrome

Flacbox obsługuje API Subsonic, co oznacza, że działa z **Subsonic**, **Navidrome** i każdym innym serwerem kompatybilnym z Subsonic — w tym Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Dotknij **Połącz z pamięcią chmurową → Subsonic**, wprowadź adres URL serwera i dane uwierzytelniające, a biblioteka pojawi się na ekranie Połączeń. To najprostszy sposób na udostępnienie Flacbox własnoręcznie hostowanej kolekcji muzycznej bez ujawniania podstawowego udziału plikowego.

## Połącz z Kompatybilną Pamięcią Obiektową S3

Dla osób samodzielnie hostujących i audiofilów korzystających z chmurowej pamięci obiektowej, Flacbox zawiera łącznik kompatybilny z S3. Dotknij **Połącz z pamięcią chmurową → Pamięć S3**, a następnie wprowadź adres URL punktu końcowego, region, klucz dostępu, klucz tajny i nazwę zasobnika. Działa z AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i każdą inną usługą, która udostępnia punkt końcowy S3-API.

## Dostępne Urządzenia

Ta sekcja wyświetla każde urządzenie w Twojej sieci lokalnej, z którym możesz się połączyć z Flacbox za pomocą wykrywania Bonjour. Aby nawiązać połączenie, wykonaj następujące kroki:

- Otwórz aplikację i przejdź do sekcji **Dostępne urządzenia** w Połączeniach.
- Dotknij urządzenia, z którym chcesz się połączyć.
- Jeśli to konieczne, wprowadź dane logowania, aby zakończyć połączenie.

To najszybszy sposób na wykrycie udziału SMB, WebDAV, DLNA w sieci domowej bez ręcznego wpisywania adresów IP.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Dostępne Urządzenia w Sieci Lokalnej" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive to wygodna technologia umożliwiająca bezprzewodowy transfer plików z komputera na urządzenie iOS za pomocą dowolnej przeglądarki na komputerze. Aby efektywnie korzystać z tej funkcji, upewnij się, że urządzenie i komputer są połączone z tą samą siecią Wi-Fi. Oto przewodnik krok po kroku dotyczący korzystania z Wi-Fi Drive.

### Włącz Wi-Fi Drive

- Otwórz aplikację i przejdź do karty **Połączenia**.
- Wybierz **Połącz przez Wi-Fi**, aby uzyskać dostęp do głównego ekranu Wi-Fi Drive.
- (Opcjonalnie) Ustaw nazwę użytkownika i hasło dla wbudowanego serwera WWW, aby chronić dostęp.
- Dotknij **Uruchom Wi-Fi Drive**, aby włączyć Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Uzyskaj Dostęp do Wi-Fi Drive na Komputerze

- Na komputerze (stacjonarnym lub laptopie) otwórz przeglądarkę internetową (np. Chrome, Firefox lub Safari).
- W pasku adresu przeglądarki wprowadź adres URL podany przez aplikację.

### Transferuj Pliki Bezprzewodowo

Gdy strona internetowa odpowiadająca Twojemu urządzeniu iOS otworzy się w przeglądarce, możesz łatwo przeciągać i upuszczać pliki z komputera na stronę internetową. Pliki, które upuścisz, zaczną przesyłać się na urządzenie iOS i będą dostępne wewnątrz Flacbox.

Możesz również zamontować Wi-Fi Drive bezpośrednio w Finderze na macOS (Idź → Połącz z serwerem…) lub Eksploratorze plików w Windows (Mapuj dysk sieciowy…) i traktować iPhone lub iPad jak zwykły dysk sieciowy.

Szczegółowe instrukcje dotyczące bezprzewodowego przesyłania plików za pomocą Wi-Fi Drive są dostępne [tutaj](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Udostępnianie Plików iTunes / Finder

Udostępnianie plików iTunes (teraz Udostępnianie plików Finder w macOS Catalina i nowszych) to inny sposób na transfer plików z komputera na urządzenie za pomocą kabla Lightning lub USB-C.

- Podłącz urządzenie do komputera za pomocą kabla i uruchom **Finder** na Mac (lub **iTunes** na Windows).
- Otwórz **Lokalizacje → Twoje Podłączone Urządzenie → Pliki** i znajdź aplikację Flacbox.
- Dotknij ikony aplikacji, aby zobaczyć wszystkie foldery współdzielone.
- Skopiuj pliki z komputera do folderu współdzielonego na urządzeniu za pomocą przeciągania i upuszczania.

Szczegółowe instrukcje dotyczące korzystania z Udostępniania plików Finder są dostępne [tutaj](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Podłącz Dysk USB Flash

Jeśli masz kartę SD lub dysk USB, możesz go podłączyć za pomocą czytnika Lightning to USB / SD Card lub dysku USB-C (na iPad i iPhone 15 / 16 / 17 / Pro). Aplikacja obsługuje certyfikowane przez Apple czytniki kart i iXpand Flash Drives. Z iXpand Flash Drive, wsuń go do portu Lightning i otwórz aplikację — zobaczysz komunikat Podłączono zewnętrzne urządzenie oraz informacje o urządzeniu. Dotknij ikony dysku flash, aby uzyskać dostęp do folderu muzyki i dotknij dowolnego pliku audio, aby rozpocząć odtwarzanie.

Mamy szczegółowe instrukcje dotyczące podłączania dysku USB flash do iPhone oraz słuchania muzyki lub zarządzania plikami na nim [tutaj](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Menedżer Plików

Po podłączeniu usługi chmurowej dotknij jej ikony, aby wyświetlić wszystkie dostępne pliki i foldery. Możesz używać wbudowanego menedżera plików do pracy z tymi plikami — pobierania, zmiany nazw, przenoszenia, przesyłania, usuwania i nie tylko. Gdy rozpoczniesz pobieranie, plik pojawia się w kolejce transferu. Aby otworzyć kolejkę transferu, przejdź do karty Pliki lokalne i dotknij ikony obracających się strzałek w lewym górnym rogu. Wszystkie pobrane pliki i foldery są dostępne w sekcji Pliki lokalne.

## Górny Pasek Narzędzi

Górny pasek narzędzi, wygodnie umieszczony pod paskiem nawigacji, oferuje kilka przydatnych akcji dla łatwego dostępu. Możesz go pokazać lub ukryć prostym gestem przeciągnięcia w dół.

- **Szukaj** — szybkie wyszukiwanie w bieżącym katalogu, ułatwiające zlokalizowanie konkretnych plików lub folderów.
- **Kontynuuj odtwarzanie** — jeśli włączone w ustawieniach aplikacji, przywraca kolejkę odtwarzacza audio i ostatnią pozycję multimediów dla bieżącego folderu. Wygodny sposób na wznowienie od miejsca, w którym skończyłeś.
- **Odtwórz wszystko** — skanuje bieżący folder i jego podfoldery, a następnie dodaje wszystkie znalezione pliki audio do nowej kolejki odtwarzacza. Przydatne gdy chcesz odtworzyć każdy utwór w katalogu.
- **Odtwarzaj losowo** — jak Odtwórz wszystko, ale tasuje pliki przed dodaniem ich do kolejki odtwarzacza audio. Świetne do ponownego odkrywania starego folderu muzyki.

## Opcje Folderu

Gdy otworzysz folder, znajdziesz poręczny zestaw akcji dostępnych przez dotknięcie przycisku **„..."** w prawym górnym rogu.

- **Wybrać** — aktywuj tryb wyboru pliku. Umożliwia to wybranie jednego lub więcej plików w folderze i wykonanie akcji na całym wyborze.
- **Nowy folder** — utwórz nowy folder w bieżącym folderze. Świetne do utrzymania dobrze zorganizowanej biblioteki.
- **Włączyć tryb offline** — włącz tryb offline dla bieżącego folderu. Tryb offline wykracza poza zwykłe pobieranie: aktywnie monitoruje folder pod kątem zmian. Jeśli dodasz nowe pliki online, automatycznie pojawią się na Twoim urządzeniu.
- **Prześlij pliki** — prześlij pliki z urządzenia do folderu online. Dzięki temu będą dostępne z dowolnego miejsca za pośrednictwem tej samej usługi chmurowej.
- **Szukaj** — wyszukaj konkretne pliki w bieżącym folderze.
- **Sortuj** — sortuj pliki według nazwy, rozmiaru, daty modyfikacji lub metadanych. Domyślny tryb sortowania odzwierciedla kolejność sortowania na serwerze, ale możesz ją zmienić zgodnie z własnymi preferencjami.
- **Siatka / Widok listy** — przełącz się między widokiem tabeli a widokiem miniatur. Widok tabeli pokazuje zwartą listę; widok miniatur pokazuje duże podglądy okładek dla szybkiej identyfikacji wizualnej.

## Edytuj Pliki Online

Gdy chcesz zarządzać wieloma plikami w swoim magazynie chmurowym, użyj **Trybu wyboru**, aby usprawnić swoje działania:

- **Aktywuj tryb wyboru** — dotknij przycisku **„..."** w prawym górnym rogu i wybierz **Wybrać**.
- **Wybierz pliki** — obok każdego pliku i folderu pojawią się pola wyboru. Dotknij, aby wybrać jeden lub kilka elementów.
- **Wykonaj akcje** — po wybraniu plików lub folderów będziesz mieć dostęp do opcji Odtwórz następny, Odtwórz później, Dodaj do biblioteki muzycznej, Dodaj do playlisty, Kopiuj, Prześlij, Przenieś, Zmień nazwę i Usuń.

Jeśli wolisz traktować podłączone pamięci chmurowe jako tylko do odczytu (aby zapobiec przypadkowemu usuwaniu), włącz Ustawienia → Menedżer plików → Edytuj pliki online → Wyłącz, aby ukryć wszystkie destrukcyjne operacje z interfejsu użytkownika.

## Akcje na Plikach

Dotknij ikony **„..."** obok tytułu pliku, aby wyświetlić jego menu akcji:

- **Odtwórz następny** — wstaw plik na górę kolejki odtwarzacza, aby odtworzył się zaraz po bieżącym utworze.
- **Odtwórz później** — dołącz plik na dół kolejki odtwarzacza.
- **Dodaj do biblioteki muzycznej** — włącz plik do biblioteki muzycznej, zorganizowanej według artysty, albumu, gatunku lub kompozytora.
- **Dodaj do playlisty** — dodaj plik do istniejącej playlisty lub utwórz nową.
- **Edytować tagi audio** — otwórz wbudowany edytor tagów, aby zmodyfikować metadane. W przypadku plików online utwór jest tymczasowo pobierany, edytowany, a następnie ponownie przesyłany po potwierdzeniu.
- **Dodaj do Ulubionych** — dodaj plik do listy ulubionych, aby uzyskać szybki dostęp.
- **Pobierz** — pobierz plik lub folder na urządzenie do użytku offline.
- **Zmień nazwę** — zmień nazwę pliku bezpośrednio na zdalnym urządzeniu.
- **Przenieś** — przenieś plik do innego folderu w chmurze.
- **Otwórz w** — wyeksportuj plik do innej zgodnej aplikacji. Plik jest pobierany na urządzenie, a następnie pojawia się systemowy arkusz udostępniania.
- **Usunąć** — trwale usuń plik z chmurowego magazynu. **Tej akcji nie można cofnąć.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Więcej Akcji dla Pliku w Podłączonej Pamięci Chmurowej" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

Jeśli lista akcji przekracza dostępne miejsce na ekranie, po prostu przewiń w dół w menu akcji, aby uzyskać dostęp do dodatkowych opcji.

## Akcje na Folderach

Dla każdego folderu w chmurze masz dostępną szeroką gamę akcji, dotykając ikony **„..."** obok tytułu folderu. Jeśli nie widzisz wszystkich akcji, przewiń w dół, aby wyświetlić więcej.

- **Odtwórz wszystko** — zastąp bieżącą kolejkę odtwarzacza każdym elementem w wybranym folderze.
- **Odtwórz następny** — dodaj cały folder na górę kolejki odtwarzacza.
- **Odtwórz później** — dołącz zawartość folderu na dół kolejki odtwarzacza.
- **Dodaj do biblioteki muzycznej** — włącz zawartość folderu do biblioteki muzycznej.
- **Dodaj do playlisty** — dodaj cały folder do playlisty. Masz też opcję utworzenia nowej playlisty; jej nazwa jest automatycznie uzupełniana na podstawie nazwy folderu.
- **Dodaj do Ulubionych** — dodaj folder do ulubionych, aby uzyskać szybki dostęp.
- **Włączyć tryb offline** — poza prostym pobieraniem, ta opcja stale monitoruje folder pod kątem nowych plików i automatycznie pobiera je po pojawieniu się online.
- **Pobierz** — pobierz całą zawartość folderu na urządzenie w celu dostępu offline.
- **Zmień nazwę** — zmień nazwę folderu bezpośrednio na zdalnym urządzeniu.
- **Przenieś** — przenieś folder do innej lokalizacji w chmurze.
- **Archiwum (ZIP)** — spakuj zawartość folderu do jednego pliku ZIP (funkcja Premium).
- **Usunąć** — trwale usuń folder i jego zawartość z chmurowego magazynu. **Tej akcji nie można cofnąć.**

## Szybki Dostęp

Sekcja Szybki Dostęp znajduje się na górze ekranu. Zapewnia szybki dostęp do ulubionych i ostatnio otwartych plików z podłączonych usług chmurowych. Za każdym razem, gdy otworzysz plik lub folder z chmury, zostanie on dodany do listy Ostatnio Otwartych. Aby wyczyścić tę listę, otwórz sekcję Ostatnie, dotknij przycisku Więcej akcji i wybierz Usuń listę. Możesz również oznaczyć głęboko zagnieżdżone foldery jako Ulubione, aby uzyskać do nich szybki dostęp bez przekopywania się przez strukturę katalogów.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Linki Online i Szybki Dostęp" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Inne Usługi

Ta sekcja wyświetla dodatkowe funkcje, które usprawniają Twoje doświadczenie. Obecnie aplikacja obsługuje scrobblowanie **Last.fm** — po połączeniu statystyki odtwarzania są automatycznie wysyłane do Twojego konta Last.fm. Możesz później odwiedzić swój profil Last.fm, aby wyświetlić analizy słuchania i otrzymać spersonalizowane rekomendacje muzyczne. Szczegółowe instrukcje konfiguracji są dostępne [tutaj](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Połącz Last.fm" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
