---
title: "Połączenia"
date: 2020-02-01
description: "Dowiedz się, jak połączyć chmurę, NAS i komputer z Evertag. Uzyskaj dostęp i edytuj pliki audio bezpośrednio z chmury, osobistego NAS lub Mac/PC."
keywords: [
  "konfiguracja chmury Evertag", "połącz iCloud z Evertag", "dostęp do plików SMB iOS",
  "edytor tagów audio WebDAV", "edycja metadanych NAS", "Wi-Fi Drive Evertag",
  "transfer plików audio na iPhone", "Evertag iTunes File Sharing", "edycja tagów FLAC z chmury"
]
tags: ["poradnik", "evertag", "połączenia"]
readingTime: 11
---


Na tym ekranie możesz połączyć różne źródła zawierające Twoje pliki audio. Możesz integrować popularne usługi chmurowe, takie jak Google Drive, Dropbox, OneDrive, iCloud i inne, a także połączyć komputer Mac lub PC. Dodatkowo masz możliwość edytowania plików audio znajdujących się w Apple Time Capsule, WD Cloud Home lub dowolnym NAS obsługującym SMB lub WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Connections Screen" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Szybki dostęp

Na górze ekranu Połączenia znajdziesz listę **Szybkiego dostępu**. Dowolny folder w chmurze dodany do ulubionych — nawet zagnieżdżony kilka poziomów głębiej — pojawia się tutaj, dzięki czemu możesz przejść do niego bez nawigowania przez nadrzędne foldery za każdym razem.

## Połącz z chmurą

- Otwórz zakładkę „Połączenia"  
- Wybierz „Połącz z chmurą" z menu  
- Wybierz usługę chmurową z listy  
- Wprowadź dane uwierzytelniające i naciśnij „Zrobione."

Jeśli napotkasz problemy, sprawdź połączenie internetowe oraz login/hasło.  
W wersji Premium aplikacji możesz dodać nieograniczoną liczbę usług.

## Obsługiwane usługi chmurowe

Obecnie aplikacja obsługuje najpopularniejsze usługi chmurowe: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), a także dowolny serwer SMB lub WebDAV.

## Bezpieczeństwo i prywatność

Używamy wyłącznie oficjalnych SDK i bezpiecznych połączeń do interakcji z podłączonymi usługami chmurowymi. Twój login i hasło nie są dostępne dla aplikacji. Wszystkie żądania aplikacji do usługi chmurowej są szyfrowane.

Gdy wprowadzasz login i hasło, aplikacja wyświetla oficjalną stronę autoryzacji dostarczoną przez dostawcę usługi chmurowej, a cały proces autoryzacji odbywa się poza aplikacją. Po pomyślnej autoryzacji dostawca usługi chmurowej wysyła token uwierzytelniający do aplikacji, który jest używany do wywołań API.

Token uwierzytelniający to cyfrowy klucz umożliwiający aplikacjom innych firm interakcję z chmurą. Token jest przechowywany na urządzeniu w bezpiecznym systemowym magazynie o nazwie Keychain. Możesz pobierać pliki z połączonej usługi chmurowej na urządzenie — trafią do katalogu „Dokumenty" aplikacji. Możesz usunąć te pliki w dowolnym momencie za pomocą wbudowanego menedżera plików.

Aplikacja nie udostępnia żadnych informacji z połączonego konta w chmurze. Możesz cofnąć dostęp do konta w chmurze w dowolnym momencie, otwierając stronę ustawień konta w przeglądarce internetowej.

## Odwoływanie tokenu autoryzacji

Zaloguj się na konto w przeglądarce internetowej i przejdź do strony ustawień. Tam możesz znaleźć wszystkie aplikacje innych firm połączone z kontem w chmurze i usunąć dowolną z nich, jeśli nie chcesz już korzystać z tej aplikacji. Szczegółowe instrukcje są dostępne [tutaj](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Możesz również rozłączyć połączone konta w chmurze w aplikacji — token uwierzytelniający zostanie wtedy usunięty z urządzenia. Jeśli usuniesz aplikację z urządzenia, wszystkie pobrane dane i tokeny dostępu zostaną również usunięte.

## Odłącz chmurę lub zmień konfigurację

- Uzyskaj dostęp do opcji chmury: najpierw zlokalizuj chmurę, którą chcesz zarządzać w interfejsie aplikacji.  
- Naciśnij przycisk „...": obok tytułu usługi zobaczysz przycisk „...". Naciśnij go, aby uzyskać dostęp do dodatkowych opcji.  
  - **Zmień nazwę**: jeśli chcesz zmienić nazwę usługi chmurowej wyświetlanej na liście, wybierz „Zmień nazwę."  
  - **Ustawienia**: aby zmodyfikować konfigurację lub dane uwierzytelniające usługi chmurowej, wybierz „Ustawienia." Czasem może być konieczna ponowna autoryzacja połączonej usługi chmurowej, jeśli token wygasł.  
  - **Rozłącz**: jeśli chcesz całkowicie zerwać połączenie między aplikacją a usługą chmurową, wybierz „Rozłącz." Pamiętaj, że wybranie tej opcji usunie wszystkie utwory powiązane z tą usługą z biblioteki muzycznej aplikacji, ale pozostaną one na serwerze.

## Połącz z komputerem lub NAS

Możesz również połączyć komputer, osobisty NAS lub inne urządzenia sieciowe za pomocą protokołu SMB, DLNA lub WebDAV.

## Połącz z komputerem przez SMB

- Naciśnij „Połącz z chmurą" → SMB.  
- Wpisz adres IP komputera i nazwę udostępnionego folderu w polu URL w formacie smb://adres-ip-komputera/nazwa-folderu  
- Wybierz wersję protokołu: Auto, SMB1, SMB2  
- Wpisz login i hasło (jeśli wymagane)  
- Naciśnij „Zrobione."

Jeśli połączenie zakończy się powodzeniem, zobaczysz podłączoną chmurę w sekcji „Chmura."  
Pełny samouczek dotyczący łączenia Mac lub PC przez SMB jest dostępny [tutaj](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Połącz z NAS przez WebDAV

Wszystkie kroki są takie same, z wyjątkiem pola URL.  
URL powinien mieć format http://nazwa-serwera lub https://nazwa-serwera, jeśli serwer obsługuje SSL.  
Pełny samouczek dotyczący łączenia NAS przez protokół WebDAV jest dostępny [tutaj](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Dostępne urządzenia

Ta sekcja wyświetla wszystkie urządzenia w sieci lokalnej, z którymi możesz się połączyć przez aplikację.  
Aby nawiązać połączenie z urządzeniem, wykonaj następujące kroki:

- Otwórz aplikację i przejdź do sekcji „Dostępne urządzenia."  
- Naciśnij urządzenie, z którym chcesz się połączyć.  
- Jeśli to konieczne, wpisz dane logowania, aby zakończyć połączenie.

## Wi-Fi Drive

Wi-Fi Drive to wygodna technologia umożliwiająca bezprzewodowe przesyłanie plików z komputera na urządzenie iOS za pomocą przeglądarki desktopowej.  
Aby efektywnie korzystać z tej funkcji, upewnij się, że urządzenie i komputer są podłączone do tej samej sieci Wi-Fi.  
Oto przewodnik krok po kroku dotyczący korzystania z Wi-Fi Drive.

## Włącz Wi-Fi Drive

- Otwórz aplikację i przejdź do zakładki „Połączenia."  
- Wybierz „Połącz przez Wi-Fi", aby wejść na główny ekran Wi-Fi Drive.  
- Naciśnij „Uruchom Wi-Fi Drive", aby włączyć Wi-Fi Drive.

## Uzyskaj dostęp do Wi-Fi Drive na komputerze

- Na komputerze (stacjonarnym lub laptopie) otwórz przeglądarkę internetową (np. Chrome, Firefox lub Safari).  
- W pasku adresu przeglądarki wpisz URL podany przez aplikację.

## Przesyłaj pliki bezprzewodowo

Po otwarciu strony internetowej odpowiadającej urządzeniu iOS w przeglądarce możesz łatwo przeciągać i upuszczać pliki z komputera na stronę internetową.  
Pliki przeciągnięte i upuszczone zaczną się przesyłać na urządzenie iOS i będą dostępne w aplikacji.

Szczegółowe instrukcje dotyczące bezprzewodowego przesyłania plików za pomocą Wi-Fi Drive są dostępne [tutaj](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing to kolejna technologia umożliwiająca przesyłanie plików z komputera na urządzenie za pomocą aplikacji Finder na Mac i kabla Lightning.  
- Po prostu podłącz urządzenie do komputera kablem i uruchom aplikację Finder na Mac.  
- Otwórz „Lokalizacje" → „Twoje podłączone urządzenie" → „Pliki" → i znajdź bieżącą aplikację.  
- Naciśnij ikonę aplikacji, aby zobaczyć wszystkie udostępnione foldery.  
- Skopiuj pliki z komputera do udostępnionego folderu na urządzeniu metodą przeciągnij i upuść.

Szczegółowe instrukcje dotyczące korzystania z iTunes File Sharing są dostępne [tutaj](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Podłącz pamięć USB

Jeśli masz kartę SD lub pamięć USB, możesz ją podłączyć za pomocą czytnika kart Lightning lub USB-C na iPhone/iPad lub bezpośrednio do Mac. Aplikacja obsługuje certyfikowane przez Apple czytniki kart. Mamy szczegółowe instrukcje dotyczące podłączania pamięci USB do iPhone lub iPad i zarządzania znajdującymi się na niej plikami, dostępne [tutaj](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Podłączone dyski pojawiają się w sekcji **Podłączone akcesoria** ekranu Połączenia.

## Menedżer plików

Po połączeniu z usługą chmurową naciśnij jej ikonę, aby wyświetlić wszystkie dostępne pliki i foldery. Możesz używać wbudowanego menedżera plików do pracy z tymi plikami — pobierania, zmiany nazw, przenoszenia i nie tylko. Po rozpoczęciu pobierania plik pojawi się w kolejce transferów. Aby wyświetlić kolejkę transferów, przejdź do zakładki „Pliki lokalne" i naciśnij obracające się strzałki w lewym górnym rogu. Wszystkie pobrane pliki i foldery są dostępne w sekcji „Pliki lokalne."

## Górny pasek narzędzi

Górny pasek narzędzi, wygodnie umieszczony pod paskiem nawigacji, oferuje kilka przydatnych akcji. Możesz pokazać lub ukryć ten pasek za pomocą prostego gestu przesunięcia w dół. Dostępne akcje:

- **Wyszukaj**: ta opcja pozwala na szybkie wyszukiwanie w bieżącym katalogu, ułatwiając zlokalizowanie konkretnych plików lub folderów.  

## Opcje folderu

Po otwarciu folderu w aplikacji znajdziesz zestaw akcji dostępnych po naciśnięciu przycisku „..." w prawym górnym rogu ekranu.  
Oto zestawienie tych akcji:

- **Wybrać**: włącz tryb wyboru plików. Ten tryb umożliwia wybranie jednego lub więcej plików w folderze, ułatwiając wykonywanie akcji na wybranych elementach.  
- **Nowy folder**: utwórz nowy folder w bieżącym folderze. Ta funkcja pozwala organizować pliki i utrzymywać bibliotekę w porządku.   
- **Prześlij pliki**: prześlij pliki z urządzenia do folderu online. Ta akcja umożliwia transfer plików do chmury lub serwera, czyniąc je dostępnymi z dowolnego miejsca.  
- **Wyszukaj**: wyszukaj konkretne pliki w bieżącym folderze. Jest to szczególnie przydatne do szybkiego wyszukiwania konkretnych elementów w dużej kolekcji.  
- **Sortuj**: sortuj pliki w folderze według kryteriów takich jak nazwa, rozmiar lub data edycji. Domyślny tryb sortowania zazwyczaj odzwierciedla kolejność sortowania na serwerze, ale możesz ją zmienić według własnych preferencji.  
- **Widok siatki/listy**: przełączaj między dwoma trybami wyświetlania: widok tabeli i widok miniatur. Widok tabeli prezentuje pliki w postaci listy, a widok miniatur wyświetla wizualne reprezentacje plików, ułatwiając identyfikację zawartości.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Cloud Folder Sort" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Edytuj pliki online

Gdy chcesz zarządzać wieloma plikami w chmurze w tej aplikacji, możesz użyć trybu wyboru, aby usprawnić działania. Wykonaj następujące kroki, aby efektywnie zarządzać plikami:

- **Aktywuj tryb wyboru**: otwórz aplikację na urządzeniu i przejdź do sekcji zawierającej chmurę. Poszukaj prawego górnego rogu, gdzie znajdziesz przycisk „..." (wielokropek). Naciśnij go i wybierz element menu „Wybrać", aby aktywować tryb wyboru.  
- **Wybierz pliki**: zauważysz pola wyboru pojawiające się obok każdego pliku lub folderu. Wybierz jeden lub wiele plików lub folderów, po prostu naciskając pola wyboru obok nich.  
- **Wykonaj różne akcje**: po wybraniu plików lub folderów, którymi chcesz zarządzać, będziesz mieć dostęp do kilku akcji dostosowanych do Twoich potrzeb:

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Select" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Akcje pliku

Obok tytułu pliku zobaczysz symbol wielokropka „..." (trzy kropki) — służy on jako menu akcji.  
Naciśnij go, aby wyświetlić listę dostępnych akcji:

- **Edytować tagi audio**: wybierając tę opcję, uzyskasz dostęp do wbudowanego edytora tagów, który pozwala modyfikować tagi audio wybranego pliku. Plik zostanie tymczasowo pobrany do katalogu tymczasowego, a następnie przesłany z powrotem do pamięci po potwierdzeniu zmian.  
- **Dodaj do ulubionych**: ta akcja dodaje plik do listy ulubionych plików dla szybkiego i wygodnego dostępu.  
- **Pobierz**: wybierz tę akcję, aby pobrać plik lub folder na urządzenie, umożliwiając korzystanie z niego w trybie offline.  
- **Zmień nazwę**: ta opcja pozwala zmienić nazwę pliku bezpośrednio w zdalnej pamięci, umożliwiając niestandardowe nazewnictwo plików.  
- **Przenieś**: użyj tej akcji, aby przenieść plik do innego folderu w chmurze, pomagając utrzymać zorganizowaną strukturę plików.  
- **Otwórz w**: użyj tej akcji, aby wyeksportować plik do innej kompatybilnej aplikacji. Plik zostanie pobrany na urządzenie, a następnie pojawi się okno dialogowe Udostępnij.  
- **Usuń**: zachowaj ostrożność przy tej akcji, ponieważ trwale usuwa plik z chmury. **Tego usunięcia nie można cofnąć**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Options" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Jeśli lista akcji przekracza dostępne miejsce na ekranie, po prostu przewiń w dół w menu akcji, aby uzyskać dostęp do dodatkowych opcji.

## Akcje folderu

Dla każdego folderu w chmurze dostępne są różne akcje. Aby uzyskać dostęp do tych opcji, naciśnij ikonę wielokropka „..." obok tytułu folderu. Jeśli nie widzisz wszystkich akcji, przewiń w dół, aby wyświetlić więcej opcji. Dostępne akcje:

- **Dodaj do ulubionych**: użyj tej akcji, aby dodać folder do listy ulubionych plików dla szybkiego i wygodnego dostępu.  
- **Pobierz**: pobierz całą zawartość folderu na urządzenie w celu dostępu offline.  
- **Zmień nazwę**: zmień nazwę folderu bezpośrednio w zdalnej pamięci.  
- **Przenieś**: przenieś folder do innej lokalizacji w chmurze.  
- **Usuń**: zachowaj ostrożność przy tej akcji, ponieważ trwale usuwa folder i jego zawartość z chmury. **Tej akcji nie można cofnąć**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Folder Options" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
