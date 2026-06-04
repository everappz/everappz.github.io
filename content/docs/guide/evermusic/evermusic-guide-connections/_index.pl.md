---
title: "Połączenia"
date: 2020-01-01
description: "Dowiedz się, jak łączyć usługi w chmurze, komputery, urządzenia NAS i zarządzać plikami muzycznymi za pomocą Evermusic. Przewodnik krok po kroku dotyczący Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes File Sharing i nie tylko."
keywords: [
  "Evermusic", "odtwarzacz muzyki z chmury", "strumieniowanie NAS", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes File Sharing",
  "podłącz pamięć w chmurze", "transfer muzyki iPhone", "menedżer plików iOS"
]
tags: ["evermusic", "przewodnik", "połączenia"]
readingTime: 11
---


Na ekranie Połączenia możesz połączyć każde źródło, w którym przechowujesz muzykę — popularne usługi w chmurze, serwery multimedialne, komputer Mac lub PC, osobisty NAS, Apple Time Capsule, WD My Cloud Home, a nawet pendrive USB — i korzystać ze wszystkich z jednego ujednoliconego interfejsu. W Połączeniach możesz też konfigurować Szybki Dostęp do głęboko zagnieżdżonych folderów w chmurze oraz uwierzytelniać Last.fm do scrobblingu.

Ekran jest podzielony na wyraźnie oznaczone sekcje, dzięki czemu obsługuje zarówno jedno konto iCloud Drive, jak i bibliotekę rozmieszczoną na wielu chmurach i urządzeniach NAS: Szybki Dostęp u góry (ulubione foldery w chmurze), Pamięć w chmurze (dodane konta), Sieć lokalna (urządzenia wykryte przez Bonjour), Komputer (Wi-Fi Drive, iTunes File Sharing, SMB), Zewnętrzne akcesoria (podłączone pendrive'y) i Inne usługi (Last.fm i podobne).

{{< cards cols="1">}}
  {{< card title="" subtitle="Ekran Połączeń Evermusic" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Połącz z pamięcią w chmurze

- Otwórz kartę Połączenia.
- Wybierz Połącz z pamięcią w chmurze z menu.
- Wybierz usługę pamięci w chmurze z listy.
- Zaloguj się na oficjalnej stronie autoryzacji dostawcy (Evermusic nigdy nie widzi Twojego hasła).
- Dotknij Zrobione.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wybór dostawcy pamięci w chmurze" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Jeśli napotkasz problemy, sprawdź dwukrotnie połączenie internetowe i dane logowania oraz upewnij się, że uwierzytelnianie dwuskładnikowe jest poprawnie skonfigurowane dla tej usługi.  
W wersji Premium aplikacji możesz dodać nieograniczoną liczbę usług. Bezpłatni użytkownicy mogą jednocześnie połączyć jedno konto w chmurze.

## Obsługiwane usługi pamięci w chmurze

Evermusic obsługuje pełną gamę popularnych usług w chmurze i serwerów. Bezpłatni użytkownicy mają dostęp do tego samego katalogu dostawców, ale z limitem jednego konta; Premium odblokuje nieograniczoną liczbę kont i usuwa większość innych ograniczeń.

- **Osobiste konta w chmurze:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Serwery hostowane lokalnie i biblioteki mediów:** Plex · Jellyfin · Emby · Subsonic (i każdy serwer kompatybilny z Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (i Owncloud, przez wspólne API) · Synology Drive · QNAP.
- **Protokoły NAS i udostępniania plików:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (uwierzytelnianie hasłem lub kluczem publicznym), NFS i DLNA (tylko do odczytu — odtwarzanie i pobieranie).
- **Pamięć obiektowa zgodna z S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage lub dowolny punkt końcowy S3-API.
- **Wykrywanie w sieci lokalnej:** sekcja Dostępne urządzenia automatycznie wyświetla wszystkie urządzenia w sieci Wi-Fi, które reklamują się przez Bonjour / mDNS — serwery Plex, Jellyfin, Emby, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, routery AirPort z podłączonymi dyskami i tak dalej.

## Bezpieczeństwo i prywatność

Używamy wyłącznie oficjalnego SDK i bezpiecznych połączeń do interakcji z połączonymi usługami w chmurze. Twój login i hasło nie są dostępne dla aplikacji. Wszystkie żądania z aplikacji do usługi w chmurze są szyfrowane.

Gdy wpisujesz login i hasło, aplikacja wyświetla oficjalną stronę autoryzacji dostarczoną przez dostawcę usługi w chmurze, a cały proces autoryzacji odbywa się poza aplikacją. Dostawca usługi w chmurze wysyła token uwierzytelniający do aplikacji po pomyślnej autoryzacji, a ten token jest używany do wykonywania wywołań API.

Token uwierzytelniający to cyfrowy klucz, który umożliwia aplikacjom trzecim interakcję z pamięcią w chmurze. Token jest przechowywany na Twoim urządzeniu w bezpiecznym systemowym magazynie zwanym Keychain. Możesz pobierać pliki z połączonej usługi w chmurze na urządzenie, a te pliki zostaną umieszczone w katalogu „Dokumenty" aplikacji. Możesz usunąć te pliki w dowolnym momencie za pomocą wbudowanego menedżera plików.

Aplikacja nie udostępnia żadnych informacji z połączonego konta w chmurze. Możesz odwołać dostęp do swojego konta w chmurze w dowolnym momencie, otwierając stronę ustawień konta w przeglądarce internetowej.

## Odwołanie tokenu uwierzytelniającego

Zaloguj się na swoje konto w przeglądarce internetowej i przejdź do strony ustawień. Tam znajdziesz wszystkie aplikacje trzecie połączone z Twoim kontem w chmurze i możesz usunąć dowolną z nich, jeśli nie chcesz już korzystać z tej aplikacji. Szczegółowe instrukcje dostępne są [tutaj](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Możesz również rozłączyć połączone konta w chmurze w aplikacji, a token uwierzytelniający zostanie również usunięty z Twojego urządzenia. Jeśli usuniesz aplikację z urządzenia, wszystkie pobrane dane i tokeny dostępu zostaną również usunięte.

## Rozłączanie pamięci w chmurze lub zmiana konfiguracji

- Uzyskaj dostęp do opcji pamięci w chmurze: najpierw znajdź pamięć w chmurze, którą chcesz zarządzać, w interfejsie aplikacji.
- Dotknij przycisku '...': obok tytułu usługi zobaczysz przycisk '...'. Dotknij go, aby uzyskać dostęp do dodatkowych opcji.
  - **Zmień nazwę**: jeśli chcesz zmienić nazwę usługi w chmurze wyświetlaną na liście, wybierz 'Zmień nazwę'.
  - **Ustawienia**: aby zmodyfikować konfigurację lub dane uwierzytelniające dla usługi w chmurze, wybierz 'Ustawienia'. Czasami może być konieczne ponowne autoryzowanie połączonej usługi w chmurze, jeśli token autoryzacji wygasł.
  - **Rozłącz**: jeśli chcesz całkowicie zerwać połączenie między aplikacją a usługą w chmurze, wybierz 'Rozłącz'. Pamiętaj, że wybranie tej opcji usunie wszystkie utwory powiązane z tą usługą z biblioteki muzyki w aplikacji, ale pozostaną one na serwerze.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Więcej Akcji dla połączonej pamięci w chmurze" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Połącz z komputerem lub NAS

Możesz również połączyć swój komputer, osobisty NAS lub inne urządzenia sieciowe za pomocą protokołu SMB, DLNA lub WebDAV.

## Połącz z komputerem przez SMB

- Dotknij „Połącz z pamięcią w chmurze" → SMB.
- Wpisz adres IP komputera i nazwę folderu udostępnionego w polu URL, używając formatu smb://adres-ip-komputera/nazwa-folderu-udostępnionego
- Wybierz wersję protokołu: Auto, SMB1, SMB2
- Wpisz login i hasło (jeśli wymagane)
- Dotknij „Zrobione".

Jeśli połączenie się powiedzie, zobaczysz połączone zasoby w sekcji „Pamięć w chmurze".  
Pełny samouczek dotyczący łączenia komputera Mac lub PC przez SMB jest dostępny [tutaj](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Ustawienia połączenia SMB" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Połącz z NAS przez WebDAV

Wszystkie kroki są takie same, z wyjątkiem pola URL.  
URL powinien być w formacie http://nazwa-serwera lub https://nazwa-serwera, jeśli serwer obsługuje SSL.
Pełny samouczek dotyczący łączenia NAS za pomocą protokołu WebDAV jest dostępny [tutaj](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Ustawienia połączenia WebDAV" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Połącz z komputerem lub NAS przez DLNA

Możesz również udostępnić bibliotekę muzyki znajdującą się na komputerze PC z systemem Windows lub osobistym NAS za pomocą protokołu DLNA i uzyskać dostęp do tej biblioteki w aplikacji zgodnie z opisem [tutaj](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA to popularny i szeroko stosowany protokół, ale pozwala jedynie na odtwarzanie lub pobieranie muzyki. Nie można przesyłać plików ani tworzyć nowych folderów na serwerze.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ustawienia połączenia DLNA" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Dostępne urządzenia

Ta sekcja wyświetla wszystkie urządzenia w sieci lokalnej, z którymi możesz się połączyć przez aplikację.  
Aby nawiązać połączenie z urządzeniem, wykonaj następujące kroki:

- Otwórz aplikację i przejdź do sekcji „Dostępne urządzenia".
- Dotknij urządzenia, z którym chcesz się połączyć, z listy.
- Jeśli to konieczne, wpisz swoje dane logowania, aby zakończyć połączenie.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dostępne urządzenia w sieci lokalnej" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive to wygodna technologia umożliwiająca bezprzewodowy transfer plików z komputera na urządzenie iOS przez przeglądarkę na komputerze.  
Aby efektywnie korzystać z tej funkcji, upewnij się, że Twoje urządzenie i komputer są podłączone do tej samej sieci Wi-Fi.  
Oto przewodnik krok po kroku dotyczący korzystania z Wi-Fi Drive.

## Włącz Wi-Fi Drive

- Otwórz aplikację i przejdź do karty „Połączenia".
- Wybierz „Połącz przez Wi-Fi", aby przejść do ekranu głównego Wi-Fi Drive.
- Dotknij „Uruchom Wi-Fi Drive", aby włączyć Wi-Fi Drive.

## Uzyskaj dostęp do Wi-Fi Drive na komputerze

- Na komputerze (stacjonarnym lub laptopie) otwórz przeglądarkę internetową (np. Chrome, Firefox lub Safari).
- W pasku adresu przeglądarki wpisz adres URL podany przez aplikację.

## Bezprzewodowy transfer plików

Po otwarciu strony internetowej odpowiadającej Twojemu urządzeniu iOS w przeglądarce możesz łatwo przeciągać i upuszczać pliki z komputera na stronę internetową.  
Pliki, które przeciągniesz i upuścisz, zaczną się transferować na Twoje urządzenie iOS i będą dostępne w aplikacji.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ustawienia serwera Wi-Fi Drive" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Szczegółowe instrukcje dotyczące bezprzewodowego transferu plików za pomocą WiFi-Drive są dostępne [tutaj](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing to kolejna technologia umożliwiająca transfer plików z komputera na urządzenie za pomocą aplikacji Finder na Mac i kabla Lightning.  
- Wystarczy podłączyć urządzenie do komputera za pomocą kabla i uruchomić aplikację Finder na Mac.
- Otwórz „Lokalizacje" → „Twoje podłączone urządzenie" → „Pliki" → i znajdź aplikację Evermusic.
- Dotknij ikony aplikacji, aby zobaczyć wszystkie foldery udostępnione.
- Skopiuj pliki z komputera do folderu udostępnionego na urządzeniu za pomocą przeciągania i upuszczania.

Szczegółowe instrukcje dotyczące korzystania z iTunes File Sharing są dostępne [tutaj](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder File Sharing na Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Podłącz pendrive USB

Jeśli masz kartę SD, możesz ją podłączyć za pomocą czytnika kart Lightning. Aplikacja obsługuje aktualnie certyfikowane przez Apple czytniki kart oraz iXpand Flash Drives. Jeśli masz iXpand Flash Drive — włóż go do portu Lightning i otwórz aplikację. Zobaczysz komunikat 'Podłączono urządzenie zewnętrzne' i informacje o urządzeniu. Wystarczy dotknąć ikony pendrive'a, aby uzyskać dostęp do folderu muzyki, i dotknąć dowolnego pliku audio, aby rozpocząć odtwarzanie. Mamy szczegółowe instrukcje dotyczące podłączania pendrive'a USB do iPhone i słuchania muzyki lub zarządzania plikami na nim, dostępne [tutaj](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Menedżer plików

Po połączeniu usługi pamięci w chmurze dotknij jej ikony, aby zobaczyć wszystkie dostępne pliki i foldery. Możesz używać wbudowanego menedżera plików do pracy z tymi plikami — pobierać, zmieniać nazwy, przenosić i nie tylko. Gdy rozpoczniesz pobieranie, plik pojawi się w kolejce transferów. Aby wyświetlić kolejkę transferów, przejdź do karty „Pliki lokalne" i dotknij obracających się strzałek w lewym górnym rogu. Wszystkie pobrane pliki i foldery są dostępne w sekcji „Pliki lokalne".

## Górny pasek narzędzi

Górny pasek narzędzi, wygodnie umieszczony pod paskiem nawigacyjnym, oferuje kilka przydatnych akcji ułatwiających dostęp. Możesz pokazywać lub ukrywać ten pasek narzędzi za pomocą prostego gestu przesunięcia w dół. Oto dostępne akcje:

- **Szukaj**: ta opcja umożliwia szybkie wyszukiwanie w bieżącym katalogu, co ułatwia lokalizowanie określonych plików lub folderów.
- **Kontynuuj odtwarzanie**: jeśli jest włączone w ustawieniach aplikacji, ta funkcja przywraca kolejkę odtwarzacza audio i ostatnią pozycję mediów dla bieżącego folderu. To wygodny sposób na powrót do miejsca, w którym skończyłeś słuchać.
- **Odtwórz wszystko**: wybranie tej akcji spowoduje, że aplikacja przeskanuje bieżący folder i jego podfoldery, dodając wszystkie znalezione pliki audio do nowej kolejki odtwarzacza. Jest to przydatne, gdy chcesz odtwarzać całą muzykę w określonym katalogu.
- **Odtwórz losowo**: podobnie jak „Odtwórz wszystko", ta akcja skanuje bieżący folder i jego podfoldery, ale miesza pliki przed dodaniem ich do kolejki odtwarzacza audio. To świetny sposób na słuchanie muzyki w losowej kolejności.

{{< cards cols="1">}}
  {{< card title="" subtitle="Górny pasek narzędzi wewnątrz folderu w chmurze" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Opcje folderu

Po otwarciu folderu w aplikacji znajdziesz przydatny zestaw akcji dostępnych po dotknięciu przycisku „..." w prawym górnym rogu ekranu.  
Oto opis tych akcji:

- **Wybrać**: aktywuj tryb wyboru pliku. Ten tryb umożliwia wybór jednego lub więcej plików w folderze, co ułatwia wykonywanie akcji na wybranych elementach.
- **Nowy folder**: utwórz nowy folder w bieżącym folderze. Ta funkcja pozwala organizować pliki i utrzymywać bibliotekę w dobrej strukturze.
- **Włączyć tryb offline**: włącz tryb offline dla bieżącego folderu. Tryb offline wykracza poza zwykłe pobieranie — aktywnie monitoruje folder pod kątem zmian. Jeśli dodasz nowe pliki do folderu online, aplikacja automatycznie pobierze te pliki na Twoje urządzenie. Dzięki temu lokalna biblioteka jest zawsze aktualna ze zmianami na serwerze.
- **Prześlij pliki**: prześlij pliki z urządzenia do folderu online. Ta akcja pozwala przenosić pliki do chmury lub serwera, czyniąc je dostępnymi z dowolnego miejsca.
- **Szukaj**: wyszukaj określone pliki w bieżącym folderze. Jest to szczególnie przydatne do szybkiego lokalizowania określonych elementów w dużej kolekcji.
- **Sortuj**: sortuj pliki w folderze według kryteriów takich jak nazwa, rozmiar lub data edycji. Domyślny tryb sortowania zazwyczaj odzwierciedla kolejność sortowania na serwerze, ale możesz ją zmienić według własnych preferencji.
- **Siatka/Lista**: przełączaj się między dwoma trybami wyświetlania: widokiem tabeli i widokiem miniatur. Widok tabeli prezentuje pliki na liście, podczas gdy widok miniatur wyświetla wizualne reprezentacje plików, ułatwiając identyfikację zawartości na pierwszy rzut oka.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Więcej Akcji dla bieżącego folderu" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Edycja plików online

Gdy potrzebujesz zarządzać wieloma plikami w pamięci w chmurze w Evermusic, możesz skorzystać z trybu wyboru, aby usprawnić swoje działania. Wykonaj następujące kroki, aby efektywnie zarządzać plikami:

- **Aktywuj tryb wyboru**: otwórz aplikację na urządzeniu i przejdź do sekcji zawierającej pamięć w chmurze. Znajdź przycisk „..." (wielokropek) w prawym górnym rogu. Dotknij go i wybierz element menu „Wybrać", aby aktywować tryb wyboru.
- **Wybierz pliki**: zauważysz pola wyboru pojawiające się obok każdego pliku lub folderu na liście. Wybierz jeden lub wiele plików albo folderów, dotykając pól wyboru obok nich.
- **Wykonuj różne akcje**: po wybraniu plików lub folderów, którymi chcesz zarządzać, uzyskasz dostęp do kilku akcji dostosowanych do Twoich potrzeb.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tryb wyboru dla plików online" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Akcje dla pliku

Obok tytułu pliku zauważysz symbol wielokropka „..." (trzy kropki) — to menu akcji.  
Dotknij go, aby wyświetlić listę dostępnych akcji:

- **Odtwórz następnie**: wybierz tę akcję, aby wstawić wybrany plik na górę kolejki odtwarzacza, zapewniając jego odtworzenie natychmiast po bieżącym elemencie.
- **Odtwórz później**: wybranie tej opcji dodaje plik na dół kolejki odtwarzacza, zapewniając jego odtworzenie po istniejącej kolejce.
- **Dodaj do biblioteki muzyki**: ta akcja pozwala włączyć plik do biblioteki muzyki, czyniąc go łatwo dostępnym i starannie zorganizowanym według artysty, albumu, gatunku lub kompozytora.
- **Dodaj do listy odtwarzania**: użyj tej akcji, aby dodać plik do istniejącej listy odtwarzania lub utworzyć nową.
- **Edytować tagi audio**: wybranie tej opcji umożliwia dostęp do wbudowanego edytora tagów Evermusic, pozwalając modyfikować tagi audio wybranego pliku. Plik zostanie tymczasowo pobrany do tymczasowego katalogu, a następnie przesłany z powrotem do pamięci po potwierdzeniu zmian.
- **Dodaj do ulubionych**: ta akcja dodaje plik do listy ulubionych plików, zapewniając szybki i wygodny dostęp.
- **Pobierz**: wybierz tę akcję, aby pobrać plik lub folder na urządzenie, czyniąc go dostępnym do użytku offline.
- **Zmień nazwę**: ta opcja umożliwia zmianę nazwy pliku bezpośrednio na zdalnym magazynie, co pozwala na niestandardowe nazewnictwo plików.
- **Przenieś**: wybierz tę akcję, aby przenieść plik do innego folderu w pamięci w chmurze, pomagając utrzymać zorganizowaną strukturę plików.
- **Otwórz w**: użyj tej akcji, aby wyeksportować plik do innej kompatybilnej aplikacji. Plik zostanie pobrany na urządzenie, a następnie pojawi się okno dialogowe Udostępnij.
- **Usuń**: zachowaj ostrożność przy tej akcji, ponieważ trwale usuwa plik z pamięci w chmurze. Tej operacji nie można cofnąć.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Więcej Akcji dla pojedynczego pliku" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Jeśli lista akcji przekracza dostępne miejsce na ekranie, po prostu przewiń w dół w menu akcji, aby uzyskać dostęp do dodatkowych opcji.

## Akcje dla folderu

Dla każdego folderu w pamięci w chmurze dostępnych jest wiele akcji. Aby uzyskać do nich dostęp, dotknij ikony wielokropka „..." znajdującej się obok tytułu folderu. Jeśli nie widzisz wszystkich akcji, przewiń w dół, aby wyświetlić więcej opcji. Oto dostępne akcje:

- **Odtwórz wszystko**: zastąp bieżącą kolejkę odtwarzacza wszystkimi elementami z wybranego folderu.
- **Odtwórz następnie**: dodaj cały folder na górę kolejki odtwarzacza, tuż po bieżącym elemencie.
- **Odtwórz później**: dołącz zawartość folderu na dół kolejki odtwarzacza.
- **Dodaj do biblioteki muzyki**: ta akcja płynnie włącza zawartość folderu do biblioteki muzyki, czyniąc ją łatwo dostępną i starannie zorganizowaną według artysty, albumu, gatunku lub kompozytora.
- **Dodaj do listy odtwarzania**: możesz umieścić cały folder na liście odtwarzania. Masz też opcję utworzenia nowej listy odtwarzania, a nazwa folderu zostanie automatycznie przypisana.
- **Dodaj do ulubionych**: użyj tej akcji, aby dodać folder do listy ulubionych plików, zapewniając szybki i wygodny dostęp.
- **Włączyć tryb offline**: włączając tryb offline dla wybranego folderu, aplikacja wykracza poza zwykłe pobieranie. Stale skanuje w poszukiwaniu zmian, a jeśli do folderu online zostaną dodane nowe pliki, zostaną one automatycznie pobrane do aplikacji.
- **Pobierz**: pobierz całą zawartość folderu na urządzenie, aby uzyskać dostęp offline.
- **Zmień nazwę**: zmień nazwę folderu bezpośrednio na zdalnym magazynie.
- **Przenieś**: przenieś folder do innej lokalizacji w pamięci w chmurze.
- **Usuń**: zachowaj ostrożność przy tej akcji, ponieważ trwale usuwa folder i jego zawartość z pamięci w chmurze. Tej operacji nie można cofnąć.


## Szybki dostęp

Sekcja Szybki Dostęp znajduje się u góry ekranu. Zapewnia szybki dostęp do ulubionych i ostatnio otwartych plików z połączonych usług w chmurze.
Gdy otwierasz plik lub folder z chmury, jest on dodawany do listy „Ostatnio otwarte". Aby wyczyścić tę listę, otwórz „Ostatnie", dotknij przycisku „Więcej Akcji" i wybierz „Usuń listę". Możesz również oznaczać głęboko zagnieżdżone foldery jako Ulubione, aby uzyskiwać do nich szybki dostęp bez przeszukiwania struktury katalogów.

## Inne usługi

Ta sekcja wyświetla dodatkowe funkcje, które wzbogacają Twoje doświadczenie. Obecnie aplikacja obsługuje scrobbling Last.fm. Po połączeniu statystyki odtwarzania są automatycznie wysyłane na Twoje konto Last.fm. Możesz później odwiedzić swój profil Last.fm, aby przeglądać analizy słuchania i otrzymywać spersonalizowane rekomendacje muzyczne. Szczegółowe instrukcje konfiguracji są dostępne [tutaj](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
