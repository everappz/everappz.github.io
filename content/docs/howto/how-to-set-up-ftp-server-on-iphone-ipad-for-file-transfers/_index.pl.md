---
title: "Jak skonfigurować serwer FTP na iPhone i iPad do przesyłania plików"
description: "Zamień iPhone lub iPad w serwer FTP z Everdisk i przesyłaj pliki z Maca, komputera z Windows, Linux, Androida, aplikacji FTP takiej jak FileZilla lub z innego iPhone przez Wi-Fi. Pełna konfiguracja, adres i port ftp, dostęp gościa oraz krok po kroku łączenie dla każdego urządzenia."
date: 2026-09-19
tags: ["everdisk", "ftp", "przesylanie plikow", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["serwer FTP iPhone", "serwer FTP iPad", "jak skonfigurowac FTP na iPhone", "aplikacja serwer ftp iPhone", "polaczenie FileZilla z iPhone", "Cyberduck iPhone FTP", "przesylanie plikow iPhone FTP", "ftp iphone do komputera", "ftp iphone do iphone", "polaczenie z FTP iPhone z Windows", "adres port ftp iphone", "anonimowy ftp iphone", "udostepnianie plikow iphone ftp", "iphone ftp dla aparatu nas"]
readingTime: 9
---

{{< author-byline >}}

FTP to stary, niezawodny sposób przesyłania plików. Istnieje od dziesięcioleci, i właśnie dlatego jest tak przydatny: niemal wszystko, co potrafi rozmawiać z serwerem, go rozumie. Aparaty, smart TV, routery, dyski sieciowe, narzędzia automatyzacji i każda stacjonarna aplikacja FTP mówią po FTP. Dzięki [Everdisk](/products/everdisk) możesz uruchomić serwer FTP na swoim iPhone lub iPad, tak że telefon staje się miejscem, z którym te urządzenia i aplikacje mogą się łączyć i przenosić pliki.

Sięgaj po FTP, gdy inne opcje nie pasują, na przykład starsze urządzenie lub aplikacja, która potrafi łączyć się tylko przez FTP. Ten przewodnik obejmuje konfigurację oraz łączenie z Maca, Windows, aplikacji FTP, Linux, Androida i drugiego iPhone.

## Czego potrzebujesz

- iPhone lub iPad z zainstalowanym [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Komputer, aplikacja lub urządzenie w **tej samej sieci Wi-Fi**.
- Pliki, które chcesz udostępnić, w folderze Dokumenty w Everdisk lub w dodanych przez Ciebie folderach.

## Skonfiguruj serwer FTP w Everdisk

### Krok 1: Wybierz, co udostępnić i ustaw dostęp

Otwórz Everdisk, przejdź na kartę **Udostępnianie** i dotknij **Co udostępnić**. Folder Dokumenty jest udostępniany domyślnie. Dodaj więcej za pomocą **Dodaj folder** i **Dodaj plik**.

Otwórz **Ustawienia**, następnie **Udostępnianie**, następnie **Dostęp**. Włącz **Edycja plików**, jeśli chcesz, aby ludzie mogli przesyłać, zmieniać nazwy i usuwać, albo wyłącz, aby zezwolić tylko na pobieranie. Ustaw **Login** i **Hasło**, jeśli chcesz mieć logowanie, albo pozostaw je puste, aby każdy mógł połączyć się jako gość.

### Krok 2: Włącz serwer FTP

Przejdź do **Ustawienia**, następnie **Udostępnianie**, następnie **Połączenia** i włącz **Inne aplikacje i urządzenia**. To serwer FTP (ma etykietę FTP).

### Krok 3: Rozpocznij udostępnianie i zanotuj adres

Wróć na kartę **Udostępnianie** i dotknij **Start**. Sekcja **Jak się połączyć** pokazuje adres FTP. Wygląda tak:

```
ftp://192.168.1.20:2121
```

Liczba po dwukropku to **port**, którym domyślnie jest **2121**. Pierwsza część to adres Twojego iPhone w sieci Wi-Fi, więc Twój będzie inny. Trzymaj Everdisk otwarty na ekranie, gdy urządzenie jest połączone.

## Łączenie z Maca

1. Otwórz **Finder**, wybierz **Idź**, następnie **Połącz z serwerem** (lub naciśnij **Command i K**).
2. Wpisz adres FTP pokazany w Everdisk, na przykład `ftp://192.168.1.20:2121`.
3. Kliknij **Połącz**, następnie wybierz **Gość** albo wpisz swój **Login** i **Hasło**.

Finder montuje udział FTP, więc możesz przeglądać i kopiować pliki na swój Mac. Zwróć uwagę, że Finder otwiera FTP tylko do odczytu. Gdy chcesz wysyłać z Maca, użyj aplikacji FTP, jak opisano poniżej.

## Łączenie z Windows

1. Otwórz **Eksplorator plików** i kliknij pasek adresu u góry.
2. Wpisz adres FTP z Everdisk, na przykład `ftp://192.168.1.20:2121`, i naciśnij **Enter**.
3. Wpisz swój **Login** i **Hasło**, jeśli je ustawiłeś, albo kontynuuj jako gość.

Udostępnione pliki pojawią się w oknie i możesz je skopiować na swój komputer.

## Łączenie za pomocą aplikacji FTP (FileZilla, Cyberduck)

Do wysyłania i pełnej kontroli aplikacja FTP jest najlepszym narzędziem. **FileZilla** i **Cyberduck** są bezpłatne i działają na Windows, Mac i Linux.

1. Otwórz aplikację i utwórz nowe połączenie.
2. Ustaw **Host** na adres Wi-Fi Twojego iPhone, a **Port** na **2121**.
3. Do logowania wpisz swój **Login** i **Hasło**, albo wybierz **Anonymous**, jeśli go nie ustawiłeś.
4. Połącz się i przeciągaj pliki w obie strony (wysyłanie wymaga włączonej Edycji plików).

## Łączenie z Linux

1. Otwórz swój menedżer plików i wybierz **Połącz z serwerem** lub **Inne lokalizacje**.
2. Wpisz adres, na przykład `ftp://192.168.1.20:2121`.
3. Połącz się jako gość albo ze swoim loginem.

Możesz też użyć dowolnego klienta FTP w Linux z terminala, kierując go na tego samego hosta i port 2121.

## Łączenie z Androida

Android nie ma systemowej przeglądarki FTP, więc użyj aplikacji:

1. Zainstaluj klienta FTP takiego jak **AndFTP**, **FTPCafe**, albo menedżer plików z obsługą FTP jak **Solid Explorer**.
2. Dodaj połączenie z hostem, **portem 2121** i swoim loginem lub Anonymous.
3. Przeglądaj i przesyłaj.

## Łączenie z innego iPhone lub iPad

Aplikacja Pliki na iOS nie zawiera klienta FTP, więc użyj jednej z poniższych opcji na drugim urządzeniu:

- **Własna karta Urządzenia w Everdisk.** Otwórz Everdisk, przejdź do **Urządzenia**, dotknij **Nowe połączenie**, wybierz **FTP** i wpisz adres, na przykład `ftp://192.168.1.20:2121`. To najprostsza droga.
- **Dedykowana aplikacja FTP** dla iOS, używająca tego samego hosta, portu 2121 i loginu.

## Łączenie innego sprzętu: aparaty, telewizory, routery i NAS

To tutaj FTP błyszczy. Wiele urządzeń ma wbudowanego klienta FTP, który potrafi wysyłać lub pobierać pliki:

- **Aparaty**, które przesyłają zdjęcia przez FTP, mogą wysyłać je prosto na Twój iPhone.
- **Smart TV, routery, urządzenia NAS i narzędzia automatyzacji**, które obsługują FTP, mogą łączyć się w ten sam sposób.

Skieruj je na adres Wi-Fi Twojego iPhone, port **2121** i swój login (lub Anonymous), używając adresu pokazanego w Everdisk.

## Tylko do odczytu albo do odczytu i zapisu

Steruje tym przełącznik **Edycja plików** w Ustawienia, Udostępnianie, Dostęp. Włączony pozwala ludziom przesyłać, zmieniać nazwy i usuwać. Wyłączony oznacza, że mogą tylko pobierać. Wybierz tryb tylko do odczytu, gdy przekazujesz pliki i nie chcesz, aby cokolwiek zostało zmienione na Twoim telefonie.

## Jak ludzie korzystają z tego w praktyce

- **Połącz FileZilla ze swoim iPhone** i wypchnij partię plików na telefon za jednym razem.
- **Pozwól starej aplikacji lub urządzeniu, które mówi tylko po FTP**, dotrzeć do Twoich plików, gdy nic innego się nie połączy.
- **Odbieraj zdjęcia z aparatu**, który przesyła przez FTP.
- **Przenieś pliki między iPhone a iPad**, używając karty Urządzenia w Everdisk na urządzeniu odbierającym.

## Kilka wskazówek

- Trzymaj Everdisk otwarty, gdy urządzenie jest połączone, ponieważ iOS po chwili wstrzymuje aplikacje w tle.
- Aby wysyłać z Maca, użyj FileZilla lub Cyberduck zamiast Findera, ponieważ Finder otwiera FTP tylko do odczytu.
- Pozostaw login pusty dla najszerszej zgodności, następnie połącz się jako Anonymous, którą to opcję oferuje większość klientów FTP.
- FTP nie szyfruje swojego ruchu. W sieci, której nie ufasz, użyj zamiast tego [serwera SMB z szyfrowaniem](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/).

## Najczęściej zadawane pytania

{{% details title="Jaki jest adres i port FTP dla mojego iPhone?" closed="true" %}}
Po rozpoczęciu udostępniania Everdisk pokazuje adres na ekranie Udostępnianie. Wygląda jak ftp://192.168.1.20:2121. 2121 to port, którego Everdisk używa dla FTP, a pierwsza część to adres Twojego iPhone w sieci Wi-Fi, więc Twój będzie inny.
{{% /details %}}

{{% details title="Jak połączyć FileZilla lub Cyberduck z moim iPhone?" closed="true" %}}
Otwórz aplikację i utwórz nowe połączenie. Ustaw Host na adres Wi-Fi Twojego iPhone, a Port na 2121. Wpisz swój Login i Hasło, albo wybierz Anonymous, jeśli go nie ustawiłeś w Everdisk. Połącz się i możesz przeciągać pliki w obie strony, gdy Edycja plików jest włączona.
{{% /details %}}

{{% details title="Czy mogę połączyć się z FTP mojego iPhone z Windows?" closed="true" %}}
Tak. Otwórz Eksplorator plików, kliknij pasek adresu, wpisz adres FTP z Everdisk (na przykład ftp://192.168.1.20:2121) i naciśnij Enter. Wpisz swój login, jeśli go ustawiłeś, albo kontynuuj jako gość. Do wysyłania i większej kontroli użyj zamiast tego aplikacji FTP jak FileZilla.
{{% /details %}}

{{% details title="Czy potrzebuję loginu do FTP?" closed="true" %}}
Nie, login jest opcjonalny. Pozostaw Login i Hasło puste w Ustawienia, Udostępnianie, Dostęp i połącz się jako Anonymous, którą to opcję oferuje większość klientów FTP. Ustaw login, jeśli chcesz, aby połączenia najpierw się logowały.
{{% /details %}}

{{% details title="Dlaczego mogę tylko pobierać, a nie wysyłać przez FTP?" closed="true" %}}
Dwie przyczyny są częste. Po pierwsze, przełącznik Edycja plików w Ustawienia, Udostępnianie, Dostęp musi być włączony, aby zezwolić na wysyłanie, zmianę nazw i usuwanie. Po drugie, Finder na Macu otwiera FTP tylko do odczytu, więc użyj aplikacji FTP jak FileZilla lub Cyberduck, gdy chcesz wysyłać.
{{% /details %}}

{{% details title="Czy mogę używać FTP między dwoma iPhone'ami?" closed="true" %}}
Tak. Uruchom serwer FTP na pierwszym iPhone. Na drugim otwórz Everdisk, przejdź na kartę Urządzenia, dotknij Nowe połączenie, wybierz FTP i wpisz adres pokazany na pierwszym telefonie. Dedykowana aplikacja FTP dla iOS też działa, ponieważ aplikacja Pliki na iOS nie zawiera klienta FTP.
{{% /details %}}

{{% details title="Czy FTP jest bezpieczny?" closed="true" %}}
Zwykły FTP nie szyfruje swojego ruchu, więc traktuj go jako narzędzie do sieci, którym ufasz, jak domowa sieć Wi-Fi. W sieci, której nie kontrolujesz, użyj serwera SMB z włączonym Wymagaj szyfrowania SMB, który chroni każdy transfer.
{{% /details %}}

{{% details title="Które urządzenia mogą łączyć się przez FTP?" closed="true" %}}
Niemal wszystko, co ma klienta FTP. To obejmuje komputery Mac, Windows i Linux, aplikacje FTP jak FileZilla i Cyberduck, menedżery plików na Androida oraz sprzęt taki jak aparaty, smart TV, routery, urządzenia NAS i narzędzia automatyzacji. Ten szeroki zasięg to główny powód, aby wybrać FTP.
{{% /details %}}

{{% details title="Dlaczego moje połączenie FTP się zerwało?" closed="true" %}}
Twój iPhone jest serwerem, a iOS wstrzymuje aplikacje, które zbyt długo pozostają w tle. Trzymaj Everdisk otwarty na ekranie, gdy urządzenie jest połączone, i podłączaj do zasilania podczas długich transferów. Upewnij się też, że oba urządzenia są nadal w tej samej sieci Wi-Fi.
{{% /details %}}

{{% details title="Czy Everdisk jest bezpłatny?" closed="true" %}}
Tak, Everdisk można pobrać bezpłatnie, a serwer FTP jest w zestawie. Opcjonalny jednorazowy zakup Premium dodaje dodatki, takie jak własne porty oraz konwersja zdjęć i wideo. Możesz skonfigurować FTP i przesyłać pliki bez płacenia.
{{% /details %}}

Chcesz spróbować? [Pobierz Everdisk z App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) i połącz swojego pierwszego klienta FTP w kilka minut. Pytania lub opinie? Napisz do nas na **support@everappz.com**.
