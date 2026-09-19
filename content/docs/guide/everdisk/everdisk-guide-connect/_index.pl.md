---
title: "Podłącz swoje urządzenia"
date: 2026-08-20
description: "Instrukcje krok po kroku dotyczące łączenia się z bezprzewodowym dyskiem Everdisk: oglądaj na smart TV przez DLNA, otwieraj pliki w dowolnej przeglądarce, montuj urządzenie jako dysk sieciowy w Finderze, systemie Windows lub Linux przez WebDAV lub SMB (z opcjonalnym szyfrowaniem SMB3/AES), łącz aplikacje do plików przez FTP i przesyłaj przez kabel USB do Maca bez Wi-Fi."
keywords: ["połączenie z Everdisk", "streaming na telewizor DLNA", "otwieranie plików w przeglądarce", "montowanie dysku sieciowego Finder", "WebDAV Windows Linux", "aplikacja do plików FTP", "przesyłanie kablem USB Mac", "podłączenie iPhone do komputera", "dysk sieciowy iPhone"]
tags: ["everdisk", "guide", "connect"]
readingTime: 11
---


Gdy dotkniesz **Start** na ekranie [Udostępnianie](/docs/guide/everdisk/everdisk-guide-sharing), inne urządzenia mogą połączyć się z Twoimi plikami na pięć różnych sposobów. Wybierz metodę pasującą do urządzenia, którego chcesz użyć. W każdym przypadku dokładny **adres**, którego potrzebujesz, jest widoczny w sekcji **Jak się połączyć** na ekranie Udostępniania.

> Oba urządzenia muszą być w **tej samej sieci Wi-Fi** - albo, w przypadku Maca, połączone **kablem USB** (zobacz ostatnią sekcję).

## Oglądanie na telewizorze (DLNA)

Użyj tej metody, aby pokazać zdjęcia, filmy i muzykę na smart TV lub odtwarzaczu multimedialnym.

1. W **Ustawienia → Udostępnianie → Połączenia** upewnij się, że **TV i centrum multimedialne** jest włączone (domyślnie tak jest).
2. Na ekranie Udostępniania dotknij **Start**.
3. Na telewizorze otwórz wbudowany odtwarzacz multimedialny lub aplikację serwera multimediów (może nazywać się Media Player, SmartShare, AllShare lub podobnie).
4. Twoje urządzenie pojawi się na liście serwerów multimediów pod swoją nazwą (na przykład "Speedy-Hare"). Wybierz je.
5. Przeglądaj udostępnione zdjęcia, filmy i muzykę i rozpocznij odtwarzanie. Miniatury podglądu pojawiają się automatycznie.

Uwagi:

- DLNA nie można zabezpieczyć hasłem, więc to połączenie jest otwarte dla każdego w tej samej sieci Wi-Fi, dopóki jest włączone.
- Jeśli film nie chce się odtworzyć na starszym telewizorze, obniż jakość wideo w **Ustawienia → Udostępnianie → Filmy**, aby Everdisk przekonwertował go na bardziej zgodny format.

## Otwieranie w przeglądarce (HTTP)

Użyj tej metody, aby przekazać pliki każdemu, kto ma przeglądarkę - bez instalowania aplikacji.

1. W **Ustawienia → Udostępnianie → Połączenia** upewnij się, że **Przeglądarka** jest włączona.
2. Dotknij **Start**.
3. Na ekranie Udostępniania skopiuj adres **Przeglądarki** (lub pokaż jego kod QR).
4. Na drugim telefonie, tablecie lub komputerze otwórz dowolną przeglądarkę (Safari, Chrome, Edge, Firefox) i wpisz ten adres.
5. Otworzy się strona z Twoimi udostępnionymi plikami.

W przeglądarce druga osoba może:

- Przełączać się między widokiem **listy** i **siatki** oraz sortować według nazwy, daty lub rozmiaru.
- Zobaczyć prawdziwe **miniatury** zdjęć, filmów, plików PDF i okładek muzyki.
- Otworzyć zdjęcie w pełnoekranowej **galerii** z przesuwaniem, przybliżaniem szczypnięciem i pokazem slajdów.
- Odtwarzać muzykę we wbudowanym **odtwarzaczu** z kolejką, odtwarzaniem losowym i powtarzaniem.
- **Pobrać** dowolny plik lub pobrać cały folder (bądź kilka wybranych elementów) jako jeden **Archive.zip**.
- **Wysłać** pliki z powrotem na Twoje urządzenie - tylko jeśli włączysz **Edycję plików** (zobacz [Dostęp i prywatność](/docs/guide/everdisk/everdisk-guide-access)).

## Używanie jako dysku sieciowego (WebDAV)

Użyj tej metody, aby Twoje urządzenie pojawiło się jako zwykły dysk na Macu, komputerze z systemem Windows lub Linux, dzięki czemu możesz przeciągać pliki w obie strony.

**Na Macu (Finder)**

1. W **Ustawienia → Udostępnianie → Połączenia** upewnij się, że **Komputer** jest włączony.
2. Dotknij **Start** i zapisz adres **Komputer (WebDAV)**.
3. W Finderze wybierz **Idź → Połącz z serwerem** (lub naciśnij **⌘K**).
4. Wpisz adres WebDAV dokładnie tak, jak jest wyświetlany, i kliknij **Połącz**.
5. Wprowadź login i hasło, jeśli je ustawiłeś, w przeciwnym razie połącz się jako gość.
6. Twoje urządzenie otworzy się jak każdy inny dysk sieciowy. Przeciągaj pliki do niego lub z niego.

**W systemie Windows**

1. Otwórz **Eksplorator plików**, kliknij prawym przyciskiem myszy **Ten komputer** i wybierz **Dodaj lokalizację sieciową** (lub zmapuj dysk sieciowy).
2. Wprowadź adres WebDAV wyświetlany w Everdisk.
3. Wprowadź login i hasło, jeśli je ustawiłeś.

**W systemie Linux**

1. Otwórz menedżer plików i wybierz **Połącz z serwerem** (lub użyj `davs://` / `dav://`).
2. Wprowadź adres WebDAV wyświetlany w Everdisk.

To, czy połączenie jest tylko do odczytu, czy dwukierunkowe, zależy od ustawienia **Edycja plików**. Gdy jest włączone, możesz kopiować pliki na urządzenie oraz zmieniać ich nazwy i je usuwać; gdy jest wyłączone, dysk jest tylko do odczytu.

## Połączenie przez SMB (szyfrowany dysk sieciowy)

SMB to dysk sieciowy dla Maca, Windows i Linux, oparty na udostępnianiu plików już obecnym w tych systemach, więc Twoje urządzenie pojawia się jako zwykły dysk sieciowy - i jest to jedyne połączenie, które możesz zaszyfrować.

1. W **Ustawienia → Udostępnianie → Połączenia** upewnij się, że **Komputer (zaawansowane)** (połączenie SMB) jest włączone.
2. Dotknij **Start** i zapisz adres **SMB**, który wygląda jak `smb://192.168.1.20:4455/Share`.
3. Połącz się z komputera:
   - **Mac:** Twoje urządzenie pojawia się samo na **pasku bocznym Findera** w sekcji **Lokalizacje** (Sieć) - wystarczy je kliknąć i zalogować się. Aby połączyć się ręcznie, wybierz **Idź → Połącz z serwerem** (**⌘K**) i wpisz adres.
   - **Windows:** otwórz **Eksplorator plików**, kliknij prawym przyciskiem myszy **Ten komputer** i wybierz **Mapuj dysk sieciowy**, a następnie wpisz `\\<address>\Share`, używając hosta i nazwy udziału z ekranu Udostępniania (albo wpisz adres `smb://` na pasku adresu).
   - **Linux:** w swoim menedżerze plików wybierz **Połącz z serwerem** i wpisz adres.
4. Wprowadź login i hasło, jeśli je ustawiłeś, w przeciwnym razie połącz się jako gość.
5. Udział nazywa się **Share**. Z włączoną **Edycją plików** możesz kopiować pliki w obie strony; z wyłączoną jest tylko do odczytu.

**Włącz szyfrowanie (zalecane w niezaufanej sieci Wi-Fi)**

SMB to jedyne połączenie Everdisk, które można zaszyfrować. Aby chronić każdy transfer **szyfrowaniem SMB3 (AES)**:

1. W **Ustawienia → Udostępnianie → Dostęp** ustaw **Login** i **Hasło** - szyfrowane połączenia nie mogą być anonimowe.
2. W **Ustawienia → Udostępnianie** włącz **Wymagaj szyfrowania SMB**.
3. **Zatrzymaj i ponownie rozpocznij** udostępnianie, aby zmiana zaczęła obowiązywać.

Twój klient musi obsługiwać SMB3 - Finder na nowoczesnym Macu albo **Windows 10 i nowszy**. Szyfrowanie SMB to funkcja Premium.

## Łączenie aplikacji do plików (FTP)

Użyj tej metody w aplikacjach do zarządzania plikami i przesyłania, które posługują się FTP (na przykład FileZilla lub Cyberduck na komputerze).

1. W **Ustawienia → Udostępnianie → Połączenia** upewnij się, że **Inne aplikacje i urządzenia** jest włączone.
2. Dotknij **Start** i zapisz adres **FTP**.
3. W aplikacji FTP dodaj nowe połączenie, używając tego adresu.
4. Wprowadź login i hasło, jeśli je ustawiłeś, lub pozostaw je puste dla dostępu anonimowego.

## Przesyłanie przez kabel USB (Mac, bez potrzeby Wi-Fi)

Użyj tej metody, gdy nie ma Wi-Fi lub gdy chcesz uzyskać najszybszy i najbardziej prywatny transfer. Działa tylko z **Makiem**.

1. Podłącz iPhone'a lub iPada do Maca zwykłym kablem do ładowania.
2. Jeśli urządzenie o to poprosi, dotknij **Zaufaj temu komputerowi**.
3. W Everdisk dotknij **Start**. Pojawi się komunikat **Dostępne szybkie połączenie**, a na ekranie Udostępniania pokaże się dodatkowy adres z plakietką **Połączenie kablowe** zakończony `.local`.
4. Na Macu otwórz Finder → **Idź → Połącz z serwerem** (**⌘K**) i wprowadź ten adres `.local` (działa zarówno dla połączenia Przeglądarki, jak i Komputera).
5. Twoje urządzenie otworzy się przez kabel - szybciej niż przez Wi-Fi, a dane nigdy nie przechodzą przez router ani internet.

Uwagi:

- Używaj **nazwy `.local`**, a nie adresu IP (adresy IP działają tylko przez Wi-Fi), i nigdy `localhost`.
- Ścieżka kablowa działa **tylko z Makiem**. Komputery z systemem Windows i urządzenia z Androidem muszą używać Wi-Fi.
- Możesz również przeciągać pliki do folderu Everdisk za pomocą Findera na Macu lub aplikacji Apple Devices (albo iTunes) w systemie Windows, przez standardowe udostępnianie plików iOS.

## Następne kroki

- [Dostęp i prywatność](/docs/guide/everdisk/everdisk-guide-access) - dodaj hasło, zezwól na przesyłanie, zablokuj urządzenie.
- [Zdjęcia, muzyka i wideo](/docs/guide/everdisk/everdisk-guide-media) - udostępnij całą bibliotekę i ustaw jakość.
- [Połącz z serwerami](/docs/guide/everdisk/everdisk-guide-devices) - sięgnij po inne urządzenia z poziomu Everdisk.
