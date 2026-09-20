---
title: "Jak skonfigurować serwer SMB na iPhone i iPad do udostępniania plików"
description: "Zamień iPhone lub iPad w serwer plików SMB z Everdisk i otwieraj go jak dysk sieciowy z Maca, innego iPhone'a, Linux lub Androida przez Wi-Fi. Pełna konfiguracja, adres i port smb, opcjonalne szyfrowanie SMB3 oraz krok po kroku łączenie dla każdego urządzenia."
date: 2026-09-19
tags: ["everdisk", "smb", "udostepnianie plikow", "dysk sieciowy", "iphone", "ipad", "mac", "finder", "szyfrowanie", "wifi"]
keywords: ["serwer SMB iPhone", "serwer SMB iPad", "jak skonfigurowac SMB na iPhone", "udostepnianie SMB iPhone", "polaczenie iPhone SMB Mac Finder", "smb iphone do iphone", "aplikacja Pliki iOS polaczenie z serwerem SMB", "udostepnianie plikow iPhone SMB", "dysk sieciowy iPhone Finder", "szyfrowanie SMB3 iOS", "udostepnianie smb iPhone Android", "polaczenie z SMB z Linux", "iPhone jako dysk sieciowy", "udostepnianie plikow miedzy iPhone wifi", "mapowanie iPhone jako dysk sieciowy"]
readingTime: 10
---

{{< author-byline >}}

SMB to udostępnianie plików wbudowane w macOS, Windows i Linux oraz w niemal każdy dysk sieciowy (NAS). Gdy łączysz się z folderem udostępnionym na innym komputerze i otwiera się on jak zwykły dysk w Finderze lub Eksploratorze plików, to właśnie robota SMB. Dzięki [Everdisk](/products/everdisk) możesz umieścić udział SMB na swoim iPhone lub iPad, tak że sam telefon pojawia się jako dysk sieciowy, który inne urządzenia przeglądają, kopiują z niego i kopiują na niego.

To opcja, po którą sięgasz, gdy chcesz, aby Twój iPhone zachowywał się jak prawdziwy dysk, a nie strona internetowa. Jest szybka, przeciąga i upuszcza w obie strony i jest jedynym typem połączenia w Everdisk, który potrafi szyfrować każdy transfer. Ten przewodnik obejmuje konfigurację oraz łączenie z Maca, innego iPhone'a lub iPada, Linux, Androida i Windows.

## Czego potrzebujesz

- iPhone lub iPad z zainstalowanym [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Inne urządzenie w **tej samej sieci Wi-Fi**.
- Pliki, które chcesz udostępnić, w folderze Dokumenty w Everdisk lub w dodanych przez Ciebie folderach.

## Skonfiguruj serwer SMB w Everdisk

### Krok 1: Wybierz, co udostępnić i kto może zapisywać

Otwórz Everdisk, przejdź na kartę **Udostępnianie** i dotknij **Co udostępnić**. Folder Dokumenty jest udostępniany domyślnie. Dodaj więcej za pomocą **Dodaj folder** i **Dodaj plik** oraz włącz swoją bibliotekę Zdjęć lub Muzyki, jeśli chcesz je również udostępnić.

Zdecyduj, czy inne urządzenia mogą tylko czytać Twoje pliki, czy także je zmieniać. Otwórz **Ustawienia**, następnie **Udostępnianie**, następnie **Dostęp** i ustaw **Edycja plików**. Gdy jest włączona, podłączone urządzenia mogą kopiować pliki na Twój telefon oraz zmieniać ich nazwy i usuwać je. Gdy jest wyłączona, udział jest tylko do odczytu.

Jeśli chcesz mieć logowanie, ustaw **Login** i **Hasło** na tym samym ekranie Dostęp. Pozostaw oba puste, aby zezwolić na dostęp gościa.

### Krok 2: Włącz serwer SMB

Przejdź do **Ustawienia**, następnie **Udostępnianie**, następnie **Połączenia** i włącz **Komputer (zaawansowane)**. To serwer SMB (ma etykietę SMB).

### Krok 3: Rozpocznij udostępnianie i zanotuj adres

Wróć na kartę **Udostępnianie** i dotknij **Start**. Sekcja **Jak się połączyć** pokazuje teraz adres SMB. Wygląda tak:

```
smb://192.168.1.20:4455/Share
```

Trzy rzeczy, które warto wiedzieć o tym adresie:

- Liczba po dwukropku to **port**. Everdisk używa domyślnie **4455**.
- Udział nazywa się **Share**.
- Pierwsza część to adres Twojego iPhone w sieci Wi-Fi, więc w Twojej sieci będzie inny.

Trzymaj Everdisk otwarty, gdy urządzenia są połączone, ponieważ iOS wstrzymuje aplikacje, które zbyt długo pozostają w tle.

## Łączenie z Maca

To najgładszy przypadek, ponieważ macOS mówi natywnie po SMB.

Najszybszy sposób: otwórz **Finder** i poszukaj na pasku bocznym w sekcji **Lokalizacje** lub **Sieć**. Everdisk ogłasza się w sieci Wi-Fi, więc Twój iPhone często pojawia się tam sam. Kliknij go, następnie kliknij **Połącz jako** i wybierz **Gość**, albo wpisz swój login.

Aby połączyć się ręcznie:

1. W Finderze wybierz **Idź**, następnie **Połącz z serwerem** (lub naciśnij **Command i K**).
2. Wpisz adres SMB pokazany w Everdisk, na przykład `smb://192.168.1.20:4455/Share`.
3. Kliknij **Połącz**, następnie wybierz **Gość** albo wpisz swój **Login** i **Hasło**.

Twój iPhone otwiera się w oknie Findera. Kopiuj pliki do środka lub na zewnątrz, przeciągając je, dokładnie jak każdy inny dysk (jeśli Edycja plików jest włączona).

## Łączenie z innego iPhone lub iPad

iOS i iPadOS mogą otwierać udziały SMB we wbudowanej aplikacji **Pliki**, co sprawia, że transfery telefon do telefonu są czyste i szybkie.

Na drugim urządzeniu:

1. Otwórz aplikację **Pliki**.
2. Dotknij przycisku **więcej** (trzy kropki, u góry po prawej na iPhone) i wybierz **Połącz z serwerem**.
3. Wpisz adres SMB z Everdisk, na przykład `smb://192.168.1.20:4455/Share`.
4. Wybierz **Gość** albo **Zarejestrowany użytkownik** i wpisz swój login.
5. Udział pojawia się w sekcji Lokalizacje w aplikacji Pliki. Przeglądaj i kopiuj w obu kierunkach.

Możesz też użyć własnej karty **Urządzenia** w Everdisk na drugim urządzeniu, która zawiera klienta SMB. Otwórz Everdisk, przejdź do **Urządzenia**, dotknij **Nowe połączenie**, wybierz **SMB** i wpisz adres.

## Łączenie z Linux

1. Otwórz swój menedżer plików (Files/Nautilus w GNOME, Dolphin w KDE).
2. Wybierz **Inne lokalizacje** lub **Połącz z serwerem**.
3. Wpisz adres, na przykład `smb://192.168.1.20:4455/Share`.
4. Połącz się jako gość albo wpisz swój login.

Z terminala możesz też uruchomić `smbclient //192.168.1.20/Share -p 4455` i wpisać login, gdy zostaniesz o niego poproszony.

## Łączenie z Androida

Android nie ma systemowej przeglądarki SMB, więc użyj menedżera plików obsługującego SMB:

1. Zainstaluj aplikację taką jak **CX File Explorer**, **Solid Explorer** lub **X-plore File Manager**.
2. Dodaj nowe połączenie **SMB** lub **LAN**.
3. Wpisz hosta (adres Wi-Fi Twojego iPhone), ustaw **port na 4455** i nazwę udziału **Share**.
4. Połącz się jako gość lub ze swoim loginem, następnie przeglądaj i kopiuj.

## Łączenie z Windows

Windows potrafi odczytywać udziały SMB, z jednym haczykiem, o którym warto wiedzieć na wstępie. Wbudowany Eksplorator plików rozmawia z SMB tylko na standardowym porcie i nie pozwala wpisać własnego portu w ścieżce, a Everdisk używa portu 4455. Dlatego zwykła droga przez **Mapuj dysk sieciowy** często do niego nie dotrze.

Masz dwie dobre opcje na Windows:

- Użyj menedżera plików lub klienta SMB, który pozwala ustawić własny port, i skieruj go na adres Twojego iPhone z portem **4455** i nazwą udziału **Share**.
- Albo połącz się z Windows za pomocą jednego z innych serwerów Everdisk. [Konfiguracja WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) i [konfiguracja FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) obie działają dobrze z Eksploratora plików Windows, a link przeglądarki działa w każdej przeglądarce.

Jeśli chcesz spróbować Mapuj dysk sieciowy: otwórz **Eksplorator plików**, kliknij prawym przyciskiem **Ten komputer**, wybierz **Mapuj dysk sieciowy** i wpisz hosta oraz nazwę udziału pokazane w Everdisk. Jeśli nie może się połączyć, to przez opisane wyżej ograniczenie portu, więc przełącz się na WebDAV lub FTP.

## Włącz szyfrowanie dla niezaufanej sieci Wi-Fi

SMB to jedyne połączenie Everdisk, które potrafi szyfrować każdy transfer, co ma znaczenie w sieci Wi-Fi, której nie kontrolujesz w pełni, jak kawiarnia czy sieć biurowa.

1. W **Ustawienia**, **Udostępnianie**, **Dostęp** ustaw **Login** i **Hasło**. Szyfrowane połączenia nie mogą być anonimowe, więc ten krok jest wymagany.
2. W **Ustawienia**, **Udostępnianie** włącz **Wymagaj szyfrowania SMB**.
3. Zatrzymaj i uruchom udostępnianie ponownie, aby zmiana zadziałała.

Każdy transfer SMB jest wtedy chroniony **szyfrowaniem SMB3 (AES)**. Łączące się urządzenie musi obsługiwać SMB3, co robią zarówno Finder na nowoczesnym Macu, jak i Windows 10 lub nowszy. Szyfrowanie SMB jest częścią jednorazowego zakupu Premium.

## Tylko do odczytu albo do odczytu i zapisu

Przełącznik **Edycja plików** w Ustawienia, Udostępnianie, Dostęp steruje tym dla każdego serwera, w tym SMB. Włącz go, a podłączone urządzenia mogą przesyłać, zmieniać nazwy i usuwać. Wyłącz go, a mogą tylko przeglądać i kopiować pliki z Twojego telefonu. Wybierz tryb tylko do odczytu, gdy przekazujesz pliki komuś, kto nie ma niczego zmieniać.

## Jak ludzie korzystają z tego w praktyce

- **Przenieś duży folder na iPhone z Maca**, przeciągając go do okna Findera, szybciej niż przez wysyłkę w sieci.
- **Ściągnij dzień zdjęć i filmów z telefonu** na laptop bez iTunes i bez kabla.
- **Wysyłaj pliki między dwoma iPhone'ami** przez aplikację Pliki, bez trzeciej aplikacji po żadnej ze stron.
- **Pracuj z plikiem na miejscu**, otwierając dokument prosto z telefonu w aplikacji na Macu i zapisując go z powrotem.

## Kilka wskazówek

- Trzymaj Everdisk otwarty, gdy urządzenie jest połączone. Zablokowanie telefonu na dłużej może wstrzymać aplikację i zerwać połączenie.
- Jeśli Mac nie widzi telefonu na pasku bocznym Findera, połącz się ręcznie przez Połącz z serwerem i pełny adres smb.
- Dla najlepszej prędkości przy dużych transferach trzymaj jakość zdjęć i wideo na Oryginał w Ustawieniach.
- W niezaufanej sieci włącz Wymagaj szyfrowania SMB i wyłącz pozostałe serwery na czas pracy.

## Najczęściej zadawane pytania

{{% details title="Jaki jest adres i port SMB dla mojego iPhone?" closed="true" %}}
Po rozpoczęciu udostępniania Everdisk pokazuje adres na ekranie Udostępnianie. Wygląda jak smb://192.168.1.20:4455/Share. 4455 to port, którego Everdisk używa dla SMB, a Share to nazwa udostępnionego folderu. Pierwsza część to adres Twojego iPhone w sieci Wi-Fi, więc Twój będzie inny.
{{% /details %}}

{{% details title="Czy mogę połączyć się z udziałem SMB mojego iPhone z Windows?" closed="true" %}}
Eksplorator plików Windows łączy się z SMB tylko na standardowym porcie i nie przyjmuje własnego portu w ścieżce, a Everdisk używa portu 4455. Dlatego zwykła droga przez Mapuj dysk sieciowy często do niego nie dotrze. Użyj menedżera plików, który pozwala ustawić własny port, albo połącz się z Windows przez WebDAV, FTP lub link przeglądarki. Wszystkie z nich działają z Windows bez żadnego problemu z portem.
{{% /details %}}

{{% details title="Jak udostępniać pliki między dwoma iPhone'ami przez SMB?" closed="true" %}}
Uruchom serwer SMB na pierwszym iPhone w Everdisk. Na drugim iPhone otwórz aplikację Pliki, dotknij przycisku więcej, wybierz Połącz z serwerem i wpisz adres smb pokazany w Everdisk (na przykład smb://192.168.1.20:4455/Share). Połącz się jako Gość lub ze swoim loginem, a udział pojawi się w aplikacji Pliki. Możesz też użyć własnej karty Urządzenia w Everdisk na drugim telefonie.
{{% /details %}}

{{% details title="Czy mój iPhone pojawia się automatycznie na pasku bocznym Findera na Macu?" closed="true" %}}
Zwykle tak. Everdisk ogłasza udział SMB w Twojej sieci Wi-Fi, więc Twój iPhone często pojawia się w sekcji Lokalizacje lub Sieć na pasku bocznym Findera. Kliknij go i wybierz Połącz jako, następnie Gość lub swój login. Jeśli się nie pojawia, połącz się ręcznie przez Idź, Połącz z serwerem i pełny adres smb.
{{% /details %}}

{{% details title="Czy potrzebuję hasła, aby używać SMB?" closed="true" %}}
Nie, login jest opcjonalny. Pozostaw Login i Hasło puste w Ustawienia, Udostępnianie, Dostęp, aby zezwolić na dostęp gościa. Ustaw je, jeśli chcesz, aby połączenia się logowały. Login i hasło są wymagane tylko wtedy, gdy włączysz Wymagaj szyfrowania SMB, ponieważ szyfrowane połączenia nie mogą być anonimowe.
{{% /details %}}

{{% details title="Czy połączenie SMB jest szyfrowane?" closed="true" %}}
Może być. SMB to jedyne połączenie Everdisk, które obsługuje szyfrowanie. Ustaw login i hasło, następnie włącz Wymagaj szyfrowania SMB w Ustawienia, Udostępnianie. Każdy transfer jest wtedy chroniony szyfrowaniem SMB3 (AES). Drugie urządzenie musi obsługiwać SMB3, co robią nowoczesne Maki oraz Windows 10 lub nowszy. Szyfrowanie to funkcja Premium.
{{% /details %}}

{{% details title="Czy ludzie mogą zmieniać lub usuwać moje pliki przez SMB?" closed="true" %}}
Tylko jeśli na to pozwolisz. Steruje tym przełącznik Edycja plików w Ustawienia, Udostępnianie, Dostęp. Gdy jest włączony, podłączone urządzenia mogą przesyłać, zmieniać nazwy i usuwać. Gdy jest wyłączony, udział jest tylko do odczytu, a inni mogą przeglądać i kopiować pliki z Twojego telefonu, ale nie mogą niczego zmieniać.
{{% /details %}}

{{% details title="Dlaczego moje połączenie SMB się zerwało?" closed="true" %}}
Twój iPhone jest serwerem, a iOS wstrzymuje aplikacje, które zbyt długo pozostają w tle. Trzymaj Everdisk otwarty na ekranie, gdy urządzenie jest połączone, i podłączaj telefon do zasilania podczas długich transferów. Upewnij się też, że oba urządzenia pozostały w tej samej sieci Wi-Fi.
{{% /details %}}

{{% details title="SMB, WebDAV czy FTP, którego użyć?" closed="true" %}}
Użyj SMB, gdy chcesz, aby telefon zachowywał się jak prawdziwy dysk sieciowy na Macu, innym iPhone, Linux lub NAS, i gdy chcesz szyfrowania. Użyj WebDAV, gdy chcesz dysku sieciowego, który dobrze działa też z Windows. Użyj FTP dla najszerszej zgodności ze starszymi urządzeniami i aplikacjami. Everdisk może uruchomić je wszystkie naraz, więc nie jesteś zamknięty w jednym.
{{% /details %}}

{{% details title="Czy Everdisk jest bezpłatny?" closed="true" %}}
Tak, Everdisk można pobrać bezpłatnie, a serwer SMB jest w zestawie. Opcjonalny jednorazowy zakup Premium dodaje szyfrowanie SMB, własne porty i kilka innych dodatków. Możesz skonfigurować SMB i udostępniać pliki bez płacenia.
{{% /details %}}

Chcesz spróbować? [Pobierz Everdisk z App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) i otwórz swój iPhone w Finderze w około minutę. Pytania lub opinie? Napisz do nas na **support@everappz.com**.
