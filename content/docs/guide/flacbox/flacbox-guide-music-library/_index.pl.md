---
title: "Biblioteka muzyczna"
date: 2020-02-01
description: "Dowiedz się, jak budować, organizować i synchronizować bibliotekę muzyczną w Flacbox na iPhone, iPad i Mac. Dodawaj utwory ręcznie lub synchronizuj z usług chmurowych, zarządzaj metadanymi, okładkami albumów, playlistami, ulubionymi, ostatnimi i zakładkami. Obejmuje obsługę audio Hi-Res, edytor tagów MusicBrainz, synchronizację online i offline oraz opcje personalizacji."
keywords: [
  "biblioteka muzyczna Flacbox", "synchronizacja muzyki z chmury", "organizacja metadanych muzyki",
  "edytuj tagi audio Flacbox", "synchronizacja muzyki offline", "importuj lokalną muzykę",
  "zarządzanie playlistami Flacbox", "wyszukiwanie okładek albumów Flacbox",
  "metadane muzyki iPhone", "przewodnik po aplikacji Flacbox",
  "Flacbox MusicBrainz", "Flacbox normalizacja tagów",
  "biblioteka muzyki hi-res Flacbox", "biblioteka FFmpeg Flacbox",
  "albumy solo Flacbox", "widok kompozytorów Flacbox"
]
tags: ["muzyka", "przewodnik", "flacbox", "biblioteka"]
readingTime: 11
---


Zarządzanie biblioteką muzyczną jest dziecinnie proste w Flacbox, gdzie możesz bez wysiłku organizować wszystkie swoje utwory — lokalne FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE i dziesiątki innych formatów — w jedną, przeszukiwalną kolekcję. Masz dwie opcje budowania biblioteki muzycznej: ręczne dodawanie (sam decydujesz, co jest dodawane) lub automatyczna synchronizacja (Flacbox skanuje wyznaczone foldery chmurowe i automatycznie dodaje nowe pliki w miarę ich pojawiania się).

{{< cards cols="1">}}
  {{< card title="" subtitle="Widok albumów biblioteki muzycznej Flacbox" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Ręczne Dodawanie

Aby ręcznie dodać utwory, dotknij ikony **Dodaj muzykę** w lewym górnym rogu i wybierz foldery lub pliki z podłączonej usługi chmurowej lub pliki na urządzeniu. Gdy dodajesz utwory do biblioteki, tworzone są tylko linki do tych utworów — rzeczywiste pliki pozostają w oryginalnych lokalizacjach, aby zaoszczędzić cenne miejsce na dysku. Jeśli chcesz udostępnić utwory offline, możesz użyć akcji Pobierz z menu opcji lub włączyć Tryb offline dla playlist i kolekcji utworów.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Dodawanie utworów do biblioteki muzycznej" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

Możesz również przeciągać i upuszczać pliki do biblioteki w wersji Mac lub używać **Otwórz pliki…** / **Otwórz folder…** z systemowego okna wyboru pliku na iPhone i iPad.

## Kontynuuj Odtwarzanie

Przywróć kolejkę odtwarzacza audio z ostatniej zapisanej pozycji, jeśli ta funkcja jest włączona w ustawieniach aplikacji. Włącz zarówno **Zapisz stan odtwarzacza audio**, jak i **Zapisz pozycję odtwarzania** w Ustawienia → Odtwarzacz audio → Ogólne, aby uzyskać najlepsze wrażenia. Po włączeniu przycisk **Kontynuuj odtwarzanie** pojawia się na górze każdego ekranu folderu, albumu, artysty, gatunku i playlisty — dotknij go, aby powrócić dokładnie do utworu i pozycji, w której skończyłeś.

## Lokalizacje

Wszystkie utwory w bibliotece są przemyślanie pogrupowane według typu źródła i tagów muzycznych. Możesz filtrować utwory według lokalizacji, używając przycisku **Więcej akcji** w prawym górnym rogu i wybierając **Filtr**.

### Muzyka Online

Ta sekcja prezentuje muzykę z podłączonych usług chmurowych. Utwory tutaj są transmitowane na żądanie; nic nie zajmuje miejsca na urządzeniu, dopóki wyraźnie nie pobierzesz lub nie włączysz trybu offline.

### Pliki w Tej Aplikacji

Tutaj znajdziesz muzykę dostępną do odtwarzania offline, pobraną z lokalnych plików. Obejmuje pliki w katalogu Dokumenty aplikacji — wszystko, co pobrałeś, przetransferowałeś przez Wi-Fi Drive lub zaimportowałeś przez Udostępnianie plików Finder.

### Pliki na Tym iPhone / iPad / Mac

Ta kategoria obejmuje muzykę zaimportowaną do aplikacji z urządzenia, dodaną przez okno dialogowe **Otwórz pliki…**. Oryginalne pliki pozostają w oryginalnej lokalizacji; Flacbox zachowuje do nich tylko link.

## Kategorie

Gdy dodajesz utwory do biblioteki muzycznej, aplikacja automatycznie odczytuje ich tagi audio i organizuje je w kategorie, takie jak Utwory, Nieodtwarzane utwory, Albumy, Artyści albumów, Artyści, Gatunki i Kompozytorzy.

## Grupowanie Tagów

Te kategorie pomagają organizować utwory według tagów muzycznych. Gdy dodajesz utwory do biblioteki muzycznej, aplikacja odczytuje ich metadane i grupuje je według tych kategorii. Jeśli nie widzisz wszystkich albumów, upewnij się, że aplikacja przeskanowała każdy utwór. Możesz sprawdzić postęp skanowania w Ustawienia → Biblioteka muzyczna → Odczyt metadanych → Liczba przetworzonych plików w bibliotece muzycznej. W przypadku plików lokalnych możesz również ponownie skanować foldery offline w Ustawienia → Biblioteka muzyczna → Synchronizacja folderów offline → Uruchom skanowanie folderów lokalnych. Po zakończeniu wszystkich operacji przez czytnik metadanych zobaczysz następujące kategorie w bibliotece muzycznej:

- **Utwory** — wszystkie utwory pogrupowane według tagu TRACK_TITLE. Możesz sprawdzić kolejność sortowania za pomocą menu Więcej akcji w prawym górnym rogu.
- **Nieodtwarzane utwory** — wszystkie utwory, które nigdy nie były odtwarzane.
- **Albumy** — utwory pogrupowane według tagu ALBUM_NAME, ignorując tagi artysty, artysty albumów i kompozytora. Jeśli masz kilka albumów o tej samej nazwie, ale różnych artystach, rozważ użycie sortowania Wyłączne albumy opisanego poniżej.
- **Artyści albumów** — utwory pogrupowane tylko według ALBUM_ARTIST_TAG. Przydatne do utrzymania kompilacji i współpracy w porządku z dala od pracy solo.
- **Artyści** — utwory pogrupowane tylko według ARTIST_TAG.
- **Gatunki** — utwory pogrupowane według tagu GENRE.
- **Kompozytorzy** — utwory pogrupowane według tagu COMPOSER — nieocenione dla bibliotek muzyki klasycznej, gdzie „kompozytor" jest podstawową osią nawigacji.

## Ulubione

Możesz oznaczać utwory jako ulubione na ekranie odtwarzacza audio lub za pomocą menu opcji. Ulubione pojawiają się we własnej sekcji, dzięki czemu możesz je znaleźć jednym dotknięciem.

## Ostatnie

Ta sekcja wyświetla wszystkie ostatnio odtwarzane utwory. Możesz dostosować, ile elementów przechowuje lista ostatnich w Ustawienia → Biblioteka → Ostatnie → Zmień rozmiar listy, i eksportować listę do M3U / CSV / TXT, aby zachować historię słuchania.

## Zakładki

Możesz tworzyć zakładki audio podczas odtwarzania utworu i zarządzać nimi na tym ekranie — idealne do audiobooków, długich miksów, wykładów lub zaznaczania refrenu ulubionego utworu. Szczegółowe instrukcje dotyczące pracy z zakładkami audio są dostępne [tutaj](/docs/guide/evermusic/evermusic-guide-music-library).

## Górny Pasek Narzędzi

Znajdujący się tuż pod paskiem nawigacji górny pasek narzędzi oferuje kilka wygodnych akcji: Szukaj, Odtwórz wszystko, Odtwarzaj losowo i Kontynuuj odtwarzanie. Możesz odsłonić lub ukryć ten pasek narzędzi prostym gestem przeciągnięcia w dół.

## Wyszukiwanie

Funkcja wyszukiwania umożliwia znalezienie konkretnego utworu, artysty, albumu lub gatunku w bibliotece muzycznej. Na ekranie Szukaj masz dostęp do akcji Sortuj, Filtruj i Siatka / Lista. Wyszukiwanie działa lokalnie na bazie danych biblioteki muzycznej, więc działa w pełni offline i zwraca wyniki podczas pisania.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wyszukiwanie w bibliotece muzycznej" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Menu Opcji

Każdy utwór w bibliotece muzycznej ma menu z większą liczbą akcji, dostępne przez dotknięcie przycisku z trzema kropkami obok tytułu utworu. Te akcje różnią się w zależności od tego, czy jest to pojedynczy utwór, czy część kolekcji.

### Dla Pojedynczych Utworów

- **Odtwórz następny** — dodaje utwór na górę kolejki odtwarzacza.
- **Odtwórz później** — dołącza utwór na dół kolejki odtwarzacza.
- **Dodaj do playlisty** — dodaje utwór do playlisty.
- **Dodaj do Ulubionych** — oznacza utwór jako ulubiony dla szybkiego dostępu.
- **Pobierz** — zapisuje utwór do plików lokalnych. Pojawia się w karcie **Pliki lokalne** i sekcji **Muzyka offline**.
- **Edytować tagi audio** — otwiera wbudowany edytor tagów audio, aby naprawić brakujące metadane; należy pamiętać, że zmieni to utwór w magazynie.
- **Pokaż w folderze** — pokazuje folder, w którym przechowywany jest plik audio.
- **Pokaż w Finderze** — dla plików zaimportowanych z Maca, ta akcja pokazuje folder, w którym plik audio jest zlokalizowany na Macu.
- **Otwórz w** — eksportuje plik audio do innej aplikacji.
- **Usuń z usługi chmurowej** — usuwa plik zarówno z biblioteki muzycznej, jak i z chmury. **Ta akcja jest nieodwracalna.**
- **Usuń z biblioteki muzycznej** — usuwa utwór z biblioteki muzycznej, ale plik pozostaje w magazynie. Jeśli włączona jest automatyczna synchronizacja i plik istnieje w zdalnym magazynie, pojawi się ponownie w bibliotece po operacji synchronizacji.

### Dla Kolekcji Utworów

Dla kolekcji utworów, takich jak Albumy, Artyści, Gatunki lub Kompozytorzy, menu opcji zawiera następujące akcje.

- **Odtwórz wszystko** — zastępuje kolejkę odtwarzacza utworami z wybranej kolekcji.
- **Odtwórz następny** — dodaje utwory z tej kolekcji na górę kolejki odtwarzacza.
- **Odtwórz później** — dołącza utwory z tej kolekcji na dół kolejki odtwarzacza.
- **Dodaj do playlisty** — dołącza utwory z tej kolekcji do playlisty, z opcją tworzenia nowej.
- **Włącz tryb offline** — pobiera utwory z tej kolekcji do plików lokalnych. Pliki pojawiają się w karcie **Pliki lokalne** i sekcji **Muzyka offline**. Jeśli na serwerze zostaną dodane nowe elementy do kolekcji, zostaną automatycznie pobrane.
- **Edytuj obraz** — zmień okładkę albumu dla kolekcji utworów.
- **Dodaj do archiwum** — spakuj całą kolekcję do jednego pliku ZIP dla łatwego tworzenia kopii zapasowej lub transferu (funkcja Premium).
- **Eksportuj listę utworów** — eksportuj kolekcję do M3U, CSV lub TXT do użytku w innych odtwarzaczach lub do archiwizacji.
- **Usuń z biblioteki muzycznej** — usuwa kolekcję utworów z biblioteki muzycznej. Ta akcja nie usuwa rzeczywistych plików z magazynu. Jeśli włączona jest automatyczna synchronizacja i pliki istnieją w zdalnym magazynie, pojawią się ponownie w bibliotece po operacji synchronizacji.

## Tryb Wyboru

Możesz aktywować tryb wyboru za pomocą przycisku Więcej akcji w prawym górnym rogu. W tym trybie możesz wybrać wiele utworów jednocześnie i wykonywać akcje wsadowe — dodawanie do playlisty, oznaczanie jako ulubione, usuwanie z biblioteki, pobieranie i nie tylko.

## Szczegóły Albumu

Gdy otworzysz sekcje Artysta, Artysta albumu lub Kompozytor, możesz zobaczyć przełącznik Utwory / Wszystkie albumy / Wyłączne albumy / Albumy solo.

- **Utwory** — wyświetla wszystkie utwory, w których ten Artysta / Artysta albumu / Kompozytor pojawia się w tagach audio.
- **Wszystkie albumy** — pokazuje albumy kompilacyjne i wszystkie albumy, w których artysta w ogóle jest obecny.
- **Wyłączne albumy** — pokazuje albumy, gdzie określony artysta jest jedynym artystą o tej nazwie albumu.
- **Albumy solo** — pokazuje albumy, gdzie pojawiają się tylko utwory określonego artysty, nawet jeśli inni artyści mają albumy o tej samej nazwie.

Jest to szczególnie przydatne do czyszczenia zaśmieconych kompilacji „Various Artists" w dużych bibliotekach.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Ekran szczegółów albumu" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Ustawienia

Dotknij Więcej akcji → Ustawienia, aby skonfigurować preferencje biblioteki muzycznej.

### Odczyt Metadanych

Gdy dodajesz utwory do biblioteki, czytnik metadanych przystępuje do pracy. Ten proces w tle odczytuje wszystkie metadane z Twoich utworów i organizuje je według Artysty, Albumu, Gatunku i Kompozytora. Możesz dostosować prędkość odczytu metadanych, aby szybciej ładować dane — pamiętaj, że szybszy odczyt zużywa więcej energii. Możesz również całkowicie wyłączyć czytnik metadanych i wyświetlać nazwy plików zamiast informacji z tagów.

Co ważne, czytnik metadanych aktualizuje tylko metadane w bibliotece muzycznej i nie zmienia plików przechowywanych na koncie chmurowym ani w pamięci lokalnej. Jeśli chcesz edytować metadane plików audio, możesz to zrobić za pomocą wbudowanego edytora tagów, który możesz aktywować z odpowiedniej akcji w menu opcji.

### Dostępne Tryby Czytnika Metadanych

- **Dezaktywowany** — czytnik metadanych jest wyłączony i zamiast danych z tagów audio wyświetlane są nazwy plików.
- **Bieżący utwór** — aplikacja odczytuje metadane tylko dla aktualnie odtwarzanego utworu. Użyj tej opcji, jeśli masz wolne połączenie sieciowe, aby zapobiec wysyłaniu wielu żądań do serwera chmury przez czytnik metadanych, co może powodować przerwy w odtwarzaniu.
- **Kolejka odtwarzania** — aplikacja odczytuje metadane dla wszystkich utworów w kolejce odtwarzacza audio.
- **Biblioteka** — aplikacja odczytuje metadane dla wszystkich utworów w bibliotece muzycznej.

Gdy włączony jest przełącznik **Odczyt metadanych w tle**, czytnik metadanych kontynuuje pracę w trybie tła. Należy pamiętać, że jeśli aplikacja zużywa dużo energii podczas odtwarzania audio, system operacyjny iOS może ją zawiesić.

Dlatego, jeśli masz dużą kolekcję muzyczną, zaleca się korzystanie z wersji desktopowej aplikacji do synchronizacji metadanych. Następnie możesz użyć funkcji Kopia zapasowa i przywracanie w ustawieniach aplikacji, aby przesłać zsynchronizowaną bibliotekę z komputera na urządzenie mobilne.

Gdy włączona jest opcja **Normalizuj kodowanie metadanych**, aplikacja automatycznie normalizuje kodowanie metadanych dla wszystkich utworów w bibliotece muzycznej. Naprawia to problemy, gdy kodowanie tagów audio jest uszkodzone (np. po edycji plików na PC z Windows) i zapobiega wyświetlaniu nieprawidłowych znaków w informacjach o utworze.

Akcja **Przeładować metadane** oznacza każdy plik w bibliotece muzycznej jako mający brakujące metadane, powodując odświeżenie każdego rekordu przez czytnik metadanych.

Dotknij **Uruchom odczyt metadanych**, aby ręcznie uruchomić czytnik. Postęp operacji jest wyświetlany poniżej.

### Synchronizacja Online

Automatyczna synchronizacja muzyki online pozwala automatycznie dodawać utwory z podłączonych usług chmurowych do biblioteki muzycznej. Aby aktywować tę funkcję, przejdź do Ustawień biblioteki muzycznej i wybierz foldery synchronizacji.

Po włączeniu tej opcji aplikacja skanuje wszystkie wybrane foldery, identyfikuje obsługiwane pliki audio i bezproblemowo integruje je z biblioteką. Możesz uruchamiać lub zatrzymywać synchronizację, dotykając odpowiedniej akcji w menu.

Synchronizacja muzyki online działa wyłącznie gdy aplikacja jest na pierwszym planie, co oznacza, że synchronizacja dużej biblioteki może zająć trochę czasu. Aby przyspieszyć ten proces, pozostaw aplikację otwartą, podłącz ją do źródła zasilania i włącz Ekran → Zawsze aktywny w ustawieniach aplikacji.

Alternatywnie możesz przeprowadzić synchronizację muzyki online w wersji desktopowej aplikacji i przenieść bibliotekę muzyczną do wersji iOS za pomocą funkcji Kopia zapasowa i przywracanie.

Możesz również ustawić, jak często chcesz synchronizować bibliotekę muzyki online. Jeśli ustawisz interwał na Natychmiast, synchronizacja online będzie uruchamiana za każdym razem, gdy otworzysz aplikację.

### Synchronizacja Offline

Tutaj możesz konfigurować synchronizację muzyki offline.

#### Zsynchronizowane Foldery Offline

Gdy udostępniasz folder chmurowy offline (przez menu Więcej akcji), pojawia się on w sekcji Pliki lokalne → Foldery offline. Aplikacja pobiera jego zawartość na urządzenie. Jeśli dokonasz zmian w folderze w chmurze — jak dodawanie, usuwanie lub aktualizowanie plików — aplikacja wykrywa te zmiany i automatycznie aktualizuje lokalną kopię.

Na tym ekranie możesz ręcznie uruchamiać synchronizację folderu offline, pokazywać folder offline w jego folderze nadrzędnym i wyłączać tryb offline dla folderu. Wyłączenie trybu offline usuwa wszystkie lokalne kopie plików z urządzenia.

#### Interwał Czasu

Możesz ustawić interwał czasu określający, jak często aplikacja powinna sprawdzać foldery offline pod kątem modyfikacji.

#### Uruchom Skanowanie Folderów Lokalnych

Ta opcja skanuje wszystkie lokalne foldery znajdujące się w katalogu Dokumenty aplikacji, aby znaleźć obsługiwane pliki audio. Wszystkie te pliki lokalne są bezproblemowo dodawane do biblioteki muzycznej. Pliki lokalne na urządzeniu, ale poza tą aplikacją, muszą być dodane do biblioteki muzycznej ręcznie, ponieważ aplikacja nie ma dostępu do plików poza katalogiem Dokumenty aplikacji ze względu na ograniczenia bezpieczeństwa iOS / macOS.

#### Ważne

Zaleca się okresowe inicjowanie synchronizacji muzyki offline, aby biblioteka muzyczna była aktualna z plikami lokalnymi.

### Personalizacja

W tej sekcji możesz skonfigurować styl ekranu biblioteki muzycznej zgodnie ze swoimi preferencjami. Dostępne są trzy opcje: Zwykłe menu, Pogrupowane menu, Menu z kartami. Możesz również włączyć lub wyłączyć wyświetlanie okładek albumów na ekranach szczegółów albumów.

### Okładki Albumów

Tutaj możesz skonfigurować, jak aplikacja ładuje i przechowuje okładki albumów.

- **Typ sieci** — wybierz Wi-Fi lub Wi-Fi i dane komórkowe do pobierania okładek.
- **Ładuj okładki albumów dla plików online** — gdy włączone, wbudowane okładki albumów są ładowane dla plików przechowywanych w chmurze. Może to zużywać dodatkowe dane sieciowe.
- **Szukaj w folderze** — gdy włączone, jeśli utwór nie ma wbudowanej okładki, aplikacja szuka obrazów JPEG lub PNG w tym samym folderze i używa ich jako okładki albumu.
- **Jakość okładki** — wybierz jakość okładek albumów przechowywanych na urządzeniu.
- **Pokaż w folderze** — otwórz folder, w którym okładki albumów są buforowane, abyś mógł nimi zarządzać lub wykonać kopię zapasową.
- **Usuń wszystkie** — usuń buforowane okładki albumów, aby zwolnić miejsce na dysku i wymuś na aplikacji ich ponowne ładowanie na żądanie.

Domyślnie aplikacja sprawdza wbudowane okładki albumów w Twoich utworach i wyświetla je, jeśli są dostępne. Jeśli nie ma wbudowanych okładek albumów i włączona jest opcja **Szukaj w folderze**, aplikacja sprawdza folder nadrzędny pod kątem obrazów JPEG lub PNG i używa ich jako okładek albumów dla wszystkich utworów w tym folderze.

### Listy Odtwarzania

Możesz włączyć opcję dodawania tego samego utworu do playlisty dwukrotnie. Domyślnie ta opcja jest wyłączona.

### Ostatnie

Możesz zarządzać listą ostatnio odtwarzanych utworów.

- **Usuń listę** — usuń całą listę ostatnio odtwarzanych utworów.
- **Zmień rozmiar listy** — ustaw liczbę elementów wyświetlanych na liście.
- **Eksportuj listę utworów** — eksportuj listę ostatnio odtwarzanych utworów do M3U, CSV lub TXT. Szczegółowe instrukcje są dostępne [tutaj](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Ulubione

Możesz zarządzać listą ulubionych utworów.

- **Jednoczesna edycja** — gdy włączone, dodanie utworu do ulubionych dodaje go jednocześnie w bibliotece muzycznej i sekcji plików.
- **Usuń listę** — usuń całą listę ulubionych utworów.
- **Eksportuj listę utworów** — podobnie jak Ostatnie, eksportuj listę ulubionych do M3U, CSV lub TXT.

### Usuń Bibliotekę

Ta akcja wymaże bazę danych biblioteki muzycznej, ale pozostawi pliki muzyczne nienaruszone w magazynie.

### Limit Ładowania Zawartości

Domyślnie aplikacja używa paginacji, aby skrócić czas ładowania zawartości i utrzymać responsywność dużych bibliotek. Możesz jednak wyłączyć tę opcję i pozwolić aplikacji ładować wszystkie dostępne dane naraz. Aby to zrobić, otwórz ustawienia aplikacji, przewiń w dół do Personalizacja → Limit ładowania zawartości i wybierz Dezaktywowany.
