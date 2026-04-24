---
title: "Strumieniuj muzykę z Maca lub PC na iPhone za pomocą SMB"
description: "Dowiedz się, jak strumieniować swoją kolekcję muzyki z Maca lub Windows PC na iPhone lub iPad za pomocą Evermusic i protokołu SMB. Prosty przewodnik krok po kroku do połączenia i cieszenia się dźwiękiem bez synchronizacji."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["strumieniowanie muzyki z Mac na iPhone", "SMB audio streaming iOS", "konfiguracja Evermusic SMB", "połączenie muzyki PC iPhone", "udostępnianie muzyki Mac iOS", "SMB Windows strumieniowanie plików", "dostęp Evermusic do folderów PC"]
aliases:
  - /post/stream-your-music-from-mac-or-pc-to-iphone-using-smb/
  - /single-post/Stream-your-music-from-MAC-or-PC-to-iPhone-using-SMB/
---

{{< author-byline >}}


**W skrócie:** Użyj aplikacji Evermusic na iPhone lub iPad, aby strumieniować muzykę z Maca lub Windows PC przez sieć lokalną za pomocą SMB. Bez synchronizacji, bez kopiowania -- po prostu włącz udostępnianie plików na komputerze, połącz się w aplikacji i odtwarzaj. Konfiguracja zajmuje mniej niż 5 minut.

Toniesz w morzu muzyki na swoim MAC lub PC i chcesz cieszyć się nią bezproblemowo na iPhonie lub iPadzie? Nie szukaj dalej niż Evermusic. Z Evermusic jest niewiarygodnie proste połączyć komputer za pomocą protokołu SMB i strumieniować ulubione utwory bez martwienia się o zajmowanie dodatkowej przestrzeni na urządzeniu lub radzenie sobie z problemami synchronizacji. Oto przewodnik krok po kroku, aby zacząć:

## Krok 1: Włącz protokół SMB na swoim komputerze

![Evermusic - Obsługa SMB - Ekran udostępniania Mac](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Jeśli używasz MAC

- Otwórz Preferencje systemowe -> Udostępnianie.
- Włącz usługę Udostępniania plików.
- W sekcji "Udostępnione foldery" dodaj folder z muzyką, wybierz użytkownika i ustaw poziomy uprawnień (Odczyt i zapis lub Tylko odczyt).
- Dla dodatkowej wygody możesz wybrać "Wszyscy: Tylko odczyt" dla folderu z muzyką, co ułatwi dostęp w Evermusic.
- Nie zapomnij zapamiętać URL swojego komputera (smb://192.168.xx.xx) na potrzeby kolejnych kroków.

![Evermusic - Obsługa SMB - Ekran udostępniania plików](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Dotknij "Opcje" i włącz "Udostępniaj pliki i foldery za pomocą SMB."
- Włącz "Udostępnianie plików Windows" dla dostępnych kont.

![Evermusic - Obsługa SMB - Ekran udostępniania plików i folderów](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Jeśli używasz Windows PC

![Evermusic - Obsługa SMB - Udostępnianie plików w Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Kliknij prawym przyciskiem myszy na folder z muzyką.
- Wybierz "Właściwości."
- Otwórz kartę "Udostępnianie."
- Kliknij "Udostępnij..."
- Wybierz osoby, którym chcesz udostępnić, i ustaw ich poziomy uprawnień.
- Podobnie jak na MAC, możesz wybrać "Wszyscy: Odczyt" dla wybranego folderu z muzyką.
- Kliknij "Zrobione", aby zapisać ustawienia.

![Evermusic - Obsługa SMB - Udostępniony folder w Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Krok 2: Dodaj swój komputer automatycznie

- Teraz otwórz Evermusic i przejdź do karty "Połączenia" ("Sieć" jeśli używasz starszej wersji aplikacji).
- Jeśli widzisz swój komputer w sekcji "Dostępne urządzenia" ("Dostępne udziały" jeśli używasz starszej wersji aplikacji) i wybrałeś "Wszyscy: Tylko odczyt" w poprzednim kroku, po prostu dotknij swojego komputera, a połączy się automatycznie.
- Jeśli to nie nastąpi, możesz dodać swój komputer ręcznie.

![Evermusic - Obsługa SMB - Ekran łączenia konta](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Krok 3: Dodaj swój komputer ręcznie

- Dotknij "Połącz usługę chmurową" ("Dodaj konto" jeśli używasz starszej wersji aplikacji)
- Wybierz "SMB" z listy dostępnych serwerów na następnym ekranie.
- Na ekranie ustawień "SMB":
  - Wprowadź URL serwera ze ścieżką do udostępnionego folderu. Możesz wprowadzić nazwę serwera lub IP serwera. Na przykład:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Wprowadź swoją nazwę użytkownika i hasło lub pozostaw te pola puste, jeśli wybrałeś "Wszyscy: Tylko odczyt" w poprzednim kroku.
  - Pole "WORKGROUP" jest opcjonalne i powinno być używane, jeśli masz domenę Active Directory.

![Evermusic - Obsługa SMB - Ekran wprowadzania danych logowania](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Po połączeniu konta SMB pojawi się ono w sekcji "Usługi chmurowe" ("Konta"). Otwórz połączone konto, dotykając go, przejdź do folderu z muzyką i dotknij dowolnego pliku audio, aby uruchomić odtwarzacz.

![Evermusic - Obsługa SMB - Ekran otwierania połączonego folderu](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Ciesz się swoją kolekcją muzyki bezproblemowo na iPhonie lub iPadzie z Evermusic.

![Evermusic - Obsługa SMB - Ekran odtwarzacza audio](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Krok 4: Obejście SMB2

Jeśli napotkasz problemy z przeglądaniem folderów lub odtwarzaniem plików zawierających znaki specjalne (takie jak ü, ö, é), może to być związane z protokołem SMB2. Aktywnie pracujemy nad rozwiązaniem tego problemu.

Jako tymczasowe rozwiązanie spróbuj włączyć SMB 1 na serwerze i w ustawieniach aplikacji. Alternatywnie możesz połączyć się z serwerem SMB za pomocą systemowego menu otwierania plików. Oto jak:

1. Przejdź do "Pliki lokalne."
2. Przewiń w dół do sekcji "Pliki na tym urządzeniu" i dotknij "Otwórz pliki..." lub "Otwórz foldery..."
3. Znajdź swój serwer i wybierz potrzebne pliki lub foldery.
4. Dotknij "Otwórz", aby potwierdzić wybór.

## Krok 5: Obejście WebDAV

Ponadto możesz spróbować połączyć się z NAS za pomocą protokołów WebDAV lub DLNA, jeśli są obsługiwane.

Postępując zgodnie z tymi krokami, możesz ominąć problemy związane ze znakami specjalnymi w nazwach plików i nadal cieszyć się plikami multimedialnymi.

P.S. Możesz również przesyłać pliki audio z MAC/PC na iPhone za pomocą udostępniania plików iTunes i odtwarzać lokalne pliki audio. Dowiedz się więcej o tej funkcji w naszym przewodniku: [Jak odtwarzać pliki iTunes na iPhonie](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Często zadawane pytania

{{% details title="Czy mogę strumieniować muzykę z PC na iPhone bez iTunes?" closed="true" %}}
Tak. Evermusic łączy się z PC przez SMB w lokalnej sieci Wi-Fi. iTunes nie jest wymagany. Po prostu włącz udostępnianie plików na PC i połącz się w aplikacji.
{{% /details %}}

{{% details title="Czy strumieniowanie SMB zużywa dane mobilne?" closed="true" %}}
Nie. SMB działa przez lokalną sieć Wi-Fi. Nie jest potrzebne połączenie internetowe ani dane mobilne.
{{% /details %}}

{{% details title="Jakie formaty audio obsługuje Evermusic przez SMB?" closed="true" %}}
Evermusic obsługuje MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC i inne popularne formaty audio. Pliki odtwarzane są bezpośrednio z udziału SMB.
{{% /details %}}

{{% details title="Czy mogę strumieniować muzykę z NAS na iPhone?" closed="true" %}}
Tak. Jeśli twój NAS obsługuje SMB (większość tak, w tym Synology, QNAP i WD My Cloud), możesz się z nim połączyć, korzystając z tych samych kroków w tym przewodniku.
{{% /details %}}

{{% details title="Czy muszę trzymać komputer włączony podczas strumieniowania?" closed="true" %}}
Tak. Ponieważ Evermusic strumieniuje pliki bezpośrednio z komputera, musi on być włączony i podłączony do tej samej sieci co iPhone.
{{% /details %}}

{{% details title="Czy istnieje limit rozmiaru pliku dla strumieniowania SMB?" closed="true" %}}
Nie. Evermusic strumieniuje pliki dowolnego rozmiaru przez SMB. Duże pliki bezstratne (FLAC, WAV) działają bez problemów.
{{% /details %}}
