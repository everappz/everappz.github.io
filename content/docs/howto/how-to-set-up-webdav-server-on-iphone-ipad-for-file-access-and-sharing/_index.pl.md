---
title: "Jak skonfigurować serwer WebDAV na iPhone i iPad do dostępu i udostępniania plików"
description: "Zamień iPhone lub iPad w serwer WebDAV z Everdisk i zamontuj go jako dysk sieciowy w Finderze na Macu, Eksploratorze plików Windows, Linux, Androidzie lub na innym iPhone przez Wi-Fi. Pełna konfiguracja, adres i port WebDAV oraz krok po kroku łączenie dla każdego urządzenia."
date: 2026-09-19
tags: ["everdisk", "webdav", "dysk sieciowy", "udostepnianie plikow", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["serwer WebDAV iPhone", "serwer WebDAV iPad", "jak skonfigurowac WebDAV na iPhone", "zamontuj iPhone jako dysk sieciowy", "polaczenie iPhone WebDAV Mac Finder", "WebDAV Eksplorator plikow Windows iPhone", "iPhone dysk sieciowy Windows", "WebDAV Linux iPhone", "dostep do plikow iPhone z komputera", "webdav iphone do iphone", "udostepnianie plikow iPhone WebDAV", "mapowanie dysku sieciowego iPhone", "przesylanie plikow iPhone webdav", "adres port webdav iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV zamienia folder w dysk sieciowy, który komputer może otworzyć w swoim zwykłym menedżerze plików. Działa na tym samym protokole internetowym, którego używa Twoja przeglądarka, dlatego dobrze przenosi się między Mac, Windows i Linux bez specjalnych sterowników. Dzięki [Everdisk](/products/everdisk) możesz uruchomić serwer WebDAV na swoim iPhone lub iPad, tak że telefon pojawia się jako dysk, który możesz przeglądać, kopiować z niego i kopiować na niego z niemal każdego komputera.

WebDAV to najlepszy wybór, gdy w grę wchodzi Windows, ponieważ Eksplorator plików Windows łączy się z nim bez problemu. Ten przewodnik obejmuje konfigurację oraz łączenie z Maca, Windows, Linux, Androida i drugiego iPhone.

## Czego potrzebujesz

- iPhone lub iPad z zainstalowanym [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Komputer lub inne urządzenie w **tej samej sieci Wi-Fi**.
- Pliki, które chcesz udostępnić, w folderze Dokumenty w Everdisk lub w dodanych przez Ciebie folderach.

## Skonfiguruj serwer WebDAV w Everdisk

### Krok 1: Wybierz, co udostępnić i ustaw dostęp

Otwórz Everdisk, przejdź na kartę **Udostępnianie** i dotknij **Co udostępnić**. Folder Dokumenty jest udostępniany domyślnie. Dodaj więcej za pomocą **Dodaj folder** i **Dodaj plik**.

Otwórz **Ustawienia**, następnie **Udostępnianie**, następnie **Dostęp**. Włącz **Edycja plików**, jeśli chcesz, aby podłączone komputery mogły kopiować pliki na Twój telefon oraz zmieniać ich nazwy i usuwać je, albo wyłącz dla dysku tylko do odczytu. Ustaw tu **Login** i **Hasło**, jeśli chcesz mieć logowanie, albo pozostaw je puste, aby zezwolić na dostęp gościa.

### Krok 2: Włącz serwer WebDAV

Przejdź do **Ustawienia**, następnie **Udostępnianie**, następnie **Połączenia** i włącz **Komputer**. To serwer WebDAV (ma etykietę WebDAV).

### Krok 3: Rozpocznij udostępnianie i zanotuj adres

Wróć na kartę **Udostępnianie** i dotknij **Start**. Sekcja **Jak się połączyć** pokazuje adres WebDAV. Wygląda tak:

```
http://192.168.1.20:8080
```

Liczba po dwukropku to **port**, którym domyślnie jest **8080**. Pierwsza część to adres Twojego iPhone w sieci Wi-Fi, więc Twój będzie inny. Trzymaj Everdisk otwarty na ekranie, gdy urządzenie jest połączone.

## Łączenie z Maca

1. Otwórz **Finder**, wybierz **Idź**, następnie **Połącz z serwerem** (lub naciśnij **Command i K**).
2. Wpisz adres WebDAV pokazany w Everdisk, na przykład `http://192.168.1.20:8080`.
3. Kliknij **Połącz**, następnie wybierz **Gość** albo wpisz swój **Login** i **Hasło**.

Twój iPhone otwiera się w oknie Findera i zachowuje się jak zwykły folder. Kopiuj pliki w obu kierunkach, jeśli Edycja plików jest włączona.

## Łączenie z Windows

Windows ma wbudowanego klienta WebDAV, więc to działa z Eksploratora plików.

1. Otwórz **Eksplorator plików**, kliknij prawym przyciskiem **Ten komputer** na pasku bocznym i wybierz **Dodaj lokalizację sieciową** (możesz też użyć **Mapuj dysk sieciowy**).
2. Gdy zostaniesz zapytany o adres, wpisz ten sam adres WebDAV z Everdisk, na przykład `http://192.168.1.20:8080`, następnie kliknij **Dalej**.
3. Wpisz swój **Login** i **Hasło**, jeśli je ustawiłeś.

Urządzenie pojawi się wtedy w sekcji Ten komputer jako lokalizacja sieciowa, którą możesz otworzyć i kopiować z niej pliki. Jeśli Windows za pierwszym razem odmawia połączenia, upewnij się, że usługa **WebClient** jest uruchomiona (wyszukaj Usługi w menu Start, znajdź WebClient i ustaw ją do uruchomienia), a następnie spróbuj ponownie.

## Łączenie z Linux

1. Otwórz swój menedżer plików i wybierz **Połącz z serwerem** lub **Inne lokalizacje**.
2. Wpisz adres z prefiksem WebDAV, na przykład `dav://192.168.1.20:8080` (użyj `davs://` tylko wtedy, gdy skonfigurowałeś TLS).
3. Połącz się jako gość albo wpisz swój login.

## Łączenie z Androida

Android nie ma systemowej przeglądarki WebDAV, więc użyj menedżera plików, który go obsługuje:

1. Zainstaluj aplikację taką jak **Solid Explorer** lub **CX File Explorer**.
2. Dodaj nowe połączenie **WebDAV**.
3. Wpisz hosta i **port 8080**, wybierz schemat `http` i dodaj swój login, jeśli go ustawiłeś.

## Łączenie z innego iPhone lub iPad

Aplikacja Pliki na iOS nie zawiera klienta WebDAV, więc użyj jednej z poniższych opcji:

- **Własna karta Urządzenia w Everdisk.** Na drugim urządzeniu otwórz Everdisk, przejdź do **Urządzenia**, dotknij **Nowe połączenie**, wybierz **WebDAV** i wpisz adres, na przykład `http://192.168.1.20:8080`. To najprostsza droga i nie wymaga niczego dodatkowego.
- **Aplikacja WebDAV** taka jak Documents by Readdle, która może dodać połączenie WebDAV z tym samym adresem i loginem.

## Wolisz szybki link zamiast dysku?

Jeśli potrzebujesz tylko szybko pobrać plik i w ogóle nie chcesz montować dysku, włącz połączenie **Przeglądarka** w Ustawienia, Udostępnianie, Połączenia. Everdisk poda Ci wtedy adres internetowy, który możesz otworzyć w dowolnej przeglądarce na dowolnym urządzeniu, aby przeglądać i pobierać swoje pliki. To najszybszy sposób na przekazanie pliku komputerowi z Windows, Chromebookowi lub telefonowi znajomego.

## Tylko do odczytu albo do odczytu i zapisu

Decyduje o tym przełącznik **Edycja plików** w Ustawienia, Udostępnianie, Dostęp. Włączony oznacza, że podłączone komputery mogą przesyłać, zmieniać nazwy i usuwać. Wyłączony oznacza, że dysk jest tylko do odczytu, więc inni mogą oglądać i kopiować Twoje pliki, ale nie mogą ich zmieniać.

## Jak ludzie korzystają z tego w praktyce

- **Kopiuj pliki na iPhone z komputera z Windows**, mapując go jako lokalizację sieciową i przeciągając je do środka.
- **Zgraj zdjęcia i dokumenty na laptop**, używając menedżera plików, który już znasz, bez kabla i bez iTunes.
- **Edytuj dokument na miejscu** z Maca, otwierając go prosto z telefonu i zapisując z powrotem.
- **Przenieś folder między iPhone a iPad**, używając karty Urządzenia w Everdisk na urządzeniu odbierającym.

## Kilka wskazówek

- Trzymaj Everdisk otwarty, gdy urządzenie jest połączone. Zablokowanie telefonu na dłużej może wstrzymać aplikację.
- Na Windows, jeśli połączenie się nie powiedzie, uruchom usługę WebClient i spróbuj adresu ponownie.
- WebDAV i SMB oba montują się jako dyski sieciowe. Użyj WebDAV, gdy w grę wchodzi Windows, i [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/), gdy chcesz szybkości Findera i szyfrowania.
- Dla najszybszych transferów trzymaj jakość zdjęć i wideo na Oryginał w Ustawieniach.

## Najczęściej zadawane pytania

{{% details title="Jaki jest adres i port WebDAV dla mojego iPhone?" closed="true" %}}
Po rozpoczęciu udostępniania Everdisk pokazuje adres na ekranie Udostępnianie. Wygląda jak http://192.168.1.20:8080. 8080 to port, którego Everdisk używa dla WebDAV, a pierwsza część to adres Twojego iPhone w sieci Wi-Fi, więc Twój będzie inny.
{{% /details %}}

{{% details title="Jak połączyć się z WebDAV mojego iPhone z Windows?" closed="true" %}}
Otwórz Eksplorator plików, kliknij prawym przyciskiem Ten komputer i wybierz Dodaj lokalizację sieciową lub Mapuj dysk sieciowy. Wpisz adres WebDAV z Everdisk, na przykład http://192.168.1.20:8080, następnie wpisz swój login, jeśli go ustawiłeś. Jeśli Windows nie chce się połączyć, upewnij się, że usługa WebClient jest uruchomiona (wyszukaj Usługi, znajdź WebClient, uruchom ją) i spróbuj ponownie.
{{% /details %}}

{{% details title="Czy mogę używać WebDAV między dwoma iPhone'ami?" closed="true" %}}
Tak, ale aplikacja Pliki na iOS nie ma klienta WebDAV, więc użyj Everdisk na drugim urządzeniu. Otwórz kartę Urządzenia, dotknij Nowe połączenie, wybierz WebDAV i wpisz adres pokazany na pierwszym telefonie. Aplikacja WebDAV taka jak Documents by Readdle też działa.
{{% /details %}}

{{% details title="Czy WebDAV wymaga hasła?" closed="true" %}}
Nie, login jest opcjonalny. Pozostaw Login i Hasło puste w Ustawienia, Udostępnianie, Dostęp dla dostępu gościa, albo ustaw je, jeśli chcesz, aby połączenia się logowały.
{{% /details %}}

{{% details title="Czy inni ludzie mogą zmieniać moje pliki przez WebDAV?" closed="true" %}}
Tylko jeśli na to pozwolisz. Steruje tym przełącznik Edycja plików w Ustawienia, Udostępnianie, Dostęp. Włączony pozwala podłączonym urządzeniom przesyłać, zmieniać nazwy i usuwać. Wyłączony sprawia, że dysk jest tylko do odczytu, więc inni mogą oglądać i kopiować, ale nie mogą niczego zmieniać.
{{% /details %}}

{{% details title="WebDAV czy SMB, jaka jest różnica?" closed="true" %}}
Oba montują Twój iPhone jako dysk sieciowy. WebDAV działa na protokole internetowym i łączy się bez problemu z Eksploratora plików Windows, co jest jego główną siłą. SMB to natywne udostępnianie plików na Mac, Linux i urządzeniach NAS, jest zwykle szybsze na Macu i jest jedynym połączeniem Everdisk, które potrafi szyfrować transfery. Everdisk może uruchomić oba naraz.
{{% /details %}}

{{% details title="Dlaczego mój dysk WebDAV się rozłącza?" closed="true" %}}
Twój iPhone jest serwerem, a iOS wstrzymuje aplikacje, które zbyt długo pozostają w tle. Trzymaj Everdisk otwarty na ekranie, gdy urządzenie jest połączone, i podłączaj do zasilania podczas długich transferów. Potwierdź też, że oba urządzenia są nadal w tej samej sieci Wi-Fi.
{{% /details %}}

{{% details title="Czy mogę połączyć się przez WebDAV bez Wi-Fi?" closed="true" %}}
Tak, jeśli podłączysz iPhone do Maca kablem. Everdisk pokazuje wtedy dodatkowy adres połączenia kablowego, który podłączony Mac może otworzyć w Finderze, co działa nawet zupełnie bez Wi-Fi. Przez kabel tylko ten Mac może dotrzeć do urządzenia.
{{% /details %}}

{{% details title="Czy Everdisk jest bezpłatny?" closed="true" %}}
Tak, Everdisk można pobrać bezpłatnie, a serwer WebDAV jest w zestawie. Opcjonalny jednorazowy zakup Premium dodaje dodatki, takie jak własne porty oraz konwersja zdjęć i wideo. Możesz skonfigurować WebDAV i udostępniać pliki bez płacenia.
{{% /details %}}

Chcesz spróbować? [Pobierz Everdisk z App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) i zamontuj swój iPhone jako dysk w kilka minut. Pytania lub opinie? Napisz do nas na **support@everappz.com**.
