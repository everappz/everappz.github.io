---
title: "Ustawienia"
date: 2020-02-01
description: "Poznaj każde ustawienie Flacbox — od preferencji odtwarzania, silnika audio FFmpeg / systemowego, wyjścia Hi-Res, regulacji korektora, korekcji tonu, czasu buforowania IO, synchronizacji metadanych, zarządzania playlists, transferu plików, widżetów ekranu głównego, Apple CarPlay, personalizacji interfejsu, języka, kodu dostępu, kopii zapasowej i przywracania, oraz aktualizacji do Premium."
keywords: [
  "Flacbox ustawienia", "konfiguracja odtwarzacza audio", "aktualizacja Premium Flacbox",
  "WiFi Drive", "synchronizacja metadanych", "korektor", "prędkość odtwarzania",
  "duplikaty na liście odtwarzania", "ustawienia menedżera plików", "synchronizacja muzyki offline",
  "edytor tagów audio", "tryb ciemny", "przywracanie zakupów", "kopie zapasowe ustawień",
  "ustawienia widżetów Flacbox", "ustawienia CarPlay Flacbox",
  "Flacbox FFmpeg ustawienia", "Flacbox ustawienia częstotliwości próbkowania",
  "Flacbox korekcja tonu ustawienia", "Flacbox bufor IO",
  "Flacbox kod dostępu", "język Flacbox", "personalizacja Flacbox",
  "Flacbox analityka"
]
tags: ["przewodnik", "flacbox", "ustawienia"]
readingTime: 16
---


Ekran Ustawień to centrum sterowania Flacbox. Stąd możesz uaktualnić do Premium, skonfigurować silnik audio (systemowe kodeki lub FFmpeg), zarządzać biblioteką muzyczną, skonfigurować menedżer plików, dostosować edytor tagów audio, włączyć widżety ekranu głównego i Apple CarPlay, tworzyć kopie zapasowe danych i uzyskać dostęp do pomocy oraz informacji prawnych. Sekcje są zgrupowane pod nagłówkami: Zakupy i aktualizacje, Preferencje aplikacji, Pomoc oraz Prawne i prywatność.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Settings Main Screen" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Aktualizacja do Premium

Uaktualnij aplikację do wersji Premium, aby usunąć wszystkie ograniczenia. Bezpłatna wersja oferuje jednorazowy zakup na całe życie w aplikacji i dwie opcje subskrypcji (1 miesiąc i 1 rok), aby usunąć wszystkie ograniczenia i zaktualizować do Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Upgrade to Premium" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

**Udostępnianie rodzinne** jest włączone dla wszystkich zakupów i planów, dzięki czemu możesz udostępniać wersję Premium maksymalnie pięciu członkom rodziny bez dodatkowych kosztów.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Select a Premium Plan" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Możesz dowiedzieć się więcej o zakupach i wersji Premium tutaj: [Jaka jest różnica między Flacbox a Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Udostępnianie Zakupów między iOS a Mac

Zakupy na całe życie i subskrypcje są współdzielone między iOS i Mac przy użyciu iCloud do synchronizacji tych informacji. Jeśli masz wersję Premium na urządzeniu iOS, upewnij się, że masz zainstalowaną najnowszą wersję i że iCloud jest włączony. Uruchom aplikację na iOS i zaczekaj minutę na przesłanie informacji o zakupach do iCloud.

Możesz również spróbować stuknąć przycisk Przywróć zakupy w ustawieniach aplikacji. Następnie zainstaluj najnowszą wersję aplikacji z App Store na swoim Mac i uruchom aplikację. Upewnij się, że masz połączenie z internetem i używasz tego samego konta iCloud i App Store na Mac, którego używałeś na iOS. Poczekaj minutę, aż aplikacja pobierze informacje o zakupach z iCloud — wersja Premium powinna aktywować się na Twoim Macu automatycznie.

## Przywracanie Zakupów na Nowym Urządzeniu

Aby przywrócić zakup na nowym urządzeniu, użyj menu Zakupy → Przywróć zakupy. Zobaczysz listę swoich zakupów. Jeśli nie widzisz ich wszystkich, potwierdź, że urządzenie jest połączone z tym samym Apple ID, które zostało użyte do dokonania zakupów, i upewnij się, że iCloud jest włączony.

## Wypróbuj Premium za Darmo

Możesz uaktualnić do wersji Premium za darmo, na ograniczony czas, używając tego menu. Wystarczy obejrzeć reklamę lub powiedzieć przyjaciołom o aplikacji, aby otrzymać Premium za darmo.

## Zakupy

Możesz przywrócić poprzednie zakupy z tego menu. Jeśli napotkasz błędy aktywacji, spróbuj włączyć opcję Przywróć zakupy przy uruchomieniu aplikacji.

## Aktualizacja Oprogramowania

Stuknij Aktualizacja oprogramowania, aby sprawdzić, czy dostępna jest nowsza wersja Flacbox. Aplikacja porówna zainstalowaną wersję z najnowszą wersją w App Store i poinformuje, czy zalecana jest aktualizacja.

## Co Nowego

To menu jest dostępne po wydaniu nowej wersji. Pokazuje podsumowanie zmian i nowych funkcji w najnowszej aktualizacji.

## Odtwarzacz Audio

Ta sekcja konfiguruje odtwarzacz audio i bazowy silnik audio, w tym wybór FFmpeg / systemowego kodeka i opcje wyjścia audio Hi-Res.

### Ogólne

Te ustawienia dotyczą podstawowych aspektów odtwarzacza audio — kolejki odtwarzania, wyjścia audio i zapisywania stanu odtwarzacza.

- **Tryb powtarzania** — wybierz zachowanie odtwarzacza audio po zakończeniu utworu:
  - **Powtórz wszystko** — powtarza wszystkie utwory w kolejce.
  - **Powtórz jeden** — powtarza tylko bieżący utwór.
  - **Zatrzymaj po utworze** — wstrzymuje odtwarzanie po zakończeniu bieżącego utworu.
  - **Nie powtarzaj** — pozwala odtworzyć kolejkę bez powtarzania.
- **Tryb losowania** — losuje kolejność utworów w kolejce. Możesz go **wyłączyć** lub **włączyć**.
- **Koder audio** — wybierz silnik audio używany do odtwarzania:
  - **System Codec + FFmpeg** — priorytetowo używa systemowego kodeka audio tam gdzie to możliwe, zwiększając kompatybilność i stabilność. Korekcja wysokości tonu i częstotliwość próbkowania wyjścia audio mogą być ograniczone.
  - **FFmpeg** — wymusza użycie kodeka FFmpeg dla wszystkich plików audio, umożliwiając korekcję tonu i regulację częstotliwości próbkowania wyjścia audio.
- **Częstotliwość próbkowania wyjścia audio** — dostosuj częstotliwość próbkowania wyjścia audio. Dostępne wartości: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** i **96 kHz**.
- **Liczba kanałów wyjścia audio** — dla wielokanałowych systemów audio z zewnętrznym DAC: Mono, Stereo, Center / Left / Right, Center / Left / Right / Surround, ITU BS.775-1, 5.1 Surround i SDDS.
- **Preferowany czas buforowania IO wyjścia audio** — skonfiguruj czas trwania bufora. Typowa wartość minimalizująca opóźnienie to około **5 milisekund (0,005 sekundy)**. Przetestuj różne czasy trwania na docelowym urządzeniu.
- **Tryb wyjścia audio (tylko iOS)** — skonfiguruj mieszany tryb wyjścia audio. Szczegółowe instrukcje [tutaj](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Zapisz pozycję odtwarzania** — zapisuje i przywraca pozycję odtwarzania dla piosenek w bibliotece muzycznej.
- **Zapisz stan odtwarzacza audio** — zachowuje stan odtwarzacza audio przed zamknięciem aplikacji, ułatwiając wznowienie od miejsca, w którym skończyłeś.

Po włączeniu zarówno **Zapisz pozycję odtwarzania**, jak i **Zapisz stan odtwarzacza audio**, otwórz dowolny folder, album, wykonawcę lub gatunek, a na górze ekranu zobaczysz przycisk **Kontynuuj odtwarzanie**.

### Personalizacja

Personalizacja pozwala dostosować wygląd ekranu odtwarzacza audio, zmienić dostępne elementy sterowania na ekranie głównym, ekranie blokady i pasku statusu oraz skonfigurować elementy sterowania pomijaniem czasu.

- **Styl ekranu odtwarzacza audio** — skonfiguruj rozmieszczenie elementów na ekranie odtwarzacza audio.
- **Styl przewijania okładek albumów** — skonfiguruj preferowany styl przewijania dla okładek albumów.
- **Dodatkowe elementy** — włącz dodatkowe elementy na ekranie odtwarzacza audio. Informacje o formacie audio wyświetlają informacje audio bieżącego utworu nad okładką; Suwak głośności audio wyświetla suwak wyjścia audio pod elementami sterowania odtwarzaniem.
- **Akcje ekranu głównego** — skonfiguruj, które przyciski powinny być domyślnie widoczne: Tryb powtarzania i losowania, Następna i poprzednia piosenka, Pomiń czas, Timer snu, Google Chromecast, AirPlay i Bluetooth, Korektor audio, Szukaj, Zakładki, Prędkość, Dodaj zakładkę, Dodaj do ulubionych, Komentarze i inne.
- **Elementy sterowania odtwarzaniem na ekranie blokady** — wybierz, które elementy sterowania pojawiają się na ekranie blokady. Możliwe wartości: Pomiń czas, Dodaj zakładkę, Dodaj do ulubionych.
- **Przyciski pomijania czasu** — wybierz interwał czasu dla przycisków Pomiń czas.

### Ładowanie Plików

Podczas ładowania pliku możesz zmienić typ sieci. Dostępne opcje: **Wi-Fi**, **Wi-Fi i dane komórkowe**.

- **Czas wstępnego ładowania** — ustaw interwał czasu buforowania. Zwiększ przy słabym połączeniu.
- **Użyj bezpośredniego URL** — gdy włączone, bezpośredni URL jest używany do ładowania piosenki. Może przyspieszyć ładowanie, ale może wpłynąć na stabilność.

### Korektor Audio

Skonfiguruj 10-pasmowy korektor audio, presety i wzmacniacz wstępny. Więcej informacji [tutaj](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Prędkość Odtwarzania

Dostosuj prędkość odtwarzania od **0,02× do 3,00×**. Stuknij ikonę konfiguracji w prawym górnym rogu, aby przełączyć się do **trybu precyzyjnego**.

### Korekcja Wysokości Tonu

Zmień ustawienia korekcji tonu lub przełącz do **trybu precyzyjnego**, stukając przycisk w prawym górnym rogu. Dostępne w ścieżce FFmpeg, zakres od **-1000 do +1000**.

### Pamięć Podręczna Odtwarzania

Piosenki w kolejce są automatycznie pobierane. Jeśli ręcznie pobierasz pliki, możesz wyłączyć tę opcję. Możesz tu również skonfigurować rozmiar pamięci podręcznej.

### Timer Snu

Aktywuj timer, aby automatycznie zatrzymać odtwarzanie. Stuknij ikonę konfiguracji dla **trybu precyzyjnego** z granularnością minutową.

## Biblioteka

Ustawienia biblioteki muzycznej — automatyczna synchronizacja, odczyt metadanych, ładowanie okładek, playlists, ostatnie i ulubione — znajdują się tutaj.

### Odczyt Metadanych

Po dodaniu ścieżek do biblioteki **czytnik metadanych** rozpoczyna pracę. Ten proces w tle odczytuje wszystkie metadane z ścieżek i organizuje je według Wykonawcy, Albumu, Gatunku i Kompozytora. Możesz dostosować prędkość odczytu metadanych (koszt: więcej baterii). Możesz też wyłączyć czytnik metadanych i wyświetlać nazwy plików zamiast informacji z tagów.

Czytnik metadanych **aktualizuje tylko metadane w bibliotece muzycznej** i nie zmienia plików w chmurze ani w lokalnej pamięci. Aby edytować metadane w samych plikach, użyj wbudowanego **edytora tagów** poprzez odpowiednie działanie w menu opcji.

Gdy **Odczyt metadanych w tle** jest włączony, czytnik kontynuuje pracę w trybie tła. Jeśli aplikacja zużywa zbyt dużo energii podczas odtwarzania, iOS może ją zawiesić.

W przypadku dużej kolekcji muzycznej wykonaj synchronizację metadanych na wersji desktopowej i przenieś zsynchronizowaną bibliotekę na iOS za pomocą funkcji **Backup & Restore**.

Gdy **Normalizuj kodowanie metadanych** jest włączone, aplikacja automatycznie normalizuje kodowanie metadanych wszystkich piosenek. Naprawia to uszkodzone kodowania tagów (np. po edycji plików na Windows) i zapobiega wyświetlaniu niepoprawnych znaków.

**Przeładuj metadane** oznacza każdy plik w bibliotece muzycznej jako mający brakujące metadane, powodując odświeżenie każdego rekordu przez czytnik.

**Uruchom odczyt metadanych** ręcznie uruchamia czytnik metadanych. Postęp jest pokazywany poniżej akcji.

### Synchronizacja Online

Automatyczna synchronizacja muzyki online dodaje ścieżki z podłączonych usług w chmurze do biblioteki muzycznej automatycznie. Aby ją włączyć, otwórz ustawienia biblioteki muzycznej i wybierz foldery do synchronizacji.

Przy tej opcji włączonej aplikacja skanuje wybrane foldery, identyfikuje obsługiwane pliki audio i dodaje je do biblioteki. Uruchom lub zatrzymaj synchronizację odpowiednim działaniem menu.

Synchronizacja online działa tylko gdy aplikacja jest na pierwszym planie, więc synchronizacja dużej biblioteki może trochę potrwać. Aby przyspieszyć, trzymaj Flacbox otwarty, podłącz urządzenie do zasilania i włącz **Ustawienia → Ekran → Zawsze aktywny**.

Możesz też wybrać, jak często uruchamia się synchronizacja online. Ustawienie interwału na **Natychmiast** uruchamia synchronizację przy każdym otwarciu aplikacji.

### Synchronizacja Offline

Skonfiguruj synchronizację muzyki offline.

#### Zsynchronizowane Foldery Offline

Po oznaczeniu folderu online na serwerze w chmurze jako dostępnego offline (za pomocą menu **Więcej akcji**), pojawia się tutaj. Zawartość folderu jest pobierana do **Pliki lokalne → Foldery offline**. Gdy zawartość folderu online zmienia się (pliki dodane, usunięte lub zaktualizowane), aplikacja sprawdza zmiany i aktualizuje lokalną kopię na urządzeniu.

Na tym ekranie możesz ręcznie uruchomić synchronizację folderu offline, wyświetlić folder offline w folderze nadrzędnym i wyłączyć tryb offline dla folderu. Wyłączenie trybu offline usuwa wszystkie lokalne kopie plików z urządzenia.

#### Interwał Czasowy

Wybierz, jak często aplikacja sprawdza foldery offline pod kątem modyfikacji.

#### Uruchom Skanowanie Lokalnych Folderów

Skanuje wszystkie lokalne foldery w katalogu **Dokumenty** aplikacji w poszukiwaniu obsługiwanych plików audio. Znalezione pliki są automatycznie dodawane do biblioteki muzycznej. Pliki zlokalizowane na urządzeniu poza katalogiem Dokumenty aplikacji muszą być dodawane do biblioteki muzycznej ręcznie, ponieważ aplikacja nie ma do nich dostępu z powodu ograniczeń bezpieczeństwa iOS / macOS.

**Ważne:** Zalecane jest okresowe inicjowanie synchronizacji muzyki offline, aby biblioteka muzyczna była aktualna z lokalnymi plikami.

### Personalizacja

Skonfiguruj styl ekranu biblioteki muzycznej. Dostępne trzy opcje: **Proste menu, Grupowane menu, Menu z kartami**. Możesz też włączyć lub wyłączyć okładki albumów na ekranie szczegółów albumu.

### Okładki Albumów

Skonfiguruj sposób ładowania i przechowywania okładek albumów.

- **Typ sieci** — wybierz **Wi-Fi** lub **Wi-Fi i dane komórkowe** do pobierania okładek.
- **Ładuj okładki albumów dla plików online** — gdy włączone, osadzone okładki są ładowane dla plików w chmurze. Może to zużywać dodatkowe dane sieciowe.
- **Szukaj w folderze** — gdy włączone, jeśli utwór nie ma osadzonej okładki, aplikacja szuka obrazów JPEG lub PNG w tym samym folderze.
- **Jakość okładki** — wybierz jakość okładek albumów przechowywanych na urządzeniu.
- **Pokaż w folderze** — otwórz folder, w którym są zbuforowane okładki albumów.
- **Usuń wszystkie** — usuń zbuforowane okładki albumów, aby zwolnić miejsce i wymusić ponowne ładowanie.

### Listy Odtwarzania

Włącz opcję dodania tej samej piosenki do listy odtwarzania dwukrotnie. Domyślnie ta opcja jest wyłączona.

### Ostatnie

Zarządzaj listą ostatnio odtwarzanych piosenek.

- **Usuń listę** — usuń całą listę ostatnio odtwarzanych piosenek.
- **Zmień rozmiar listy** — ustaw liczbę elementów wyświetlanych na liście.
- **Eksportuj listę piosenek** — eksportuj listę ostatnio odtwarzanych piosenek jako M3U, CSV lub TXT. Szczegółowe instrukcje [tutaj](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Ulubione

Zarządzaj listą ulubionych piosenek.

- **Jednoczesna edycja** — gdy włączone, dodanie piosenki do ulubionych dodaje ją zarówno w bibliotece muzycznej, jak i w sekcji plików jednocześnie.
- **Usuń listę** — usuń całą listę ulubionych piosenek.
- **Eksportuj listę piosenek** — jak Ostatnie, eksportuj ulubione jako M3U, CSV lub TXT.

### Usuń Bibliotekę Muzyczną

Wymaż bazę danych biblioteki muzycznej. Twoje pliki muzyczne w pamięci pozostają niezmienione.

## Kod Dostępu

Aktywuj ekran kodu dostępu, aby chronić dane aplikacji 4-cyfrowym numerycznym kodem dostępu. Gdy jest włączony, przy każdym uruchomieniu aplikacji będziesz proszony o podanie kodu dostępu. Połącz z iOS Face ID / Touch ID na urządzeniu dla dodatkowej ochrony.

## Menedżer Plików

Sekcja Menedżera plików kontroluje sposób transferowania, przechowywania i podglądu plików.

### Transfery Plików

Wybierz preferencje sieciowe do pobierania plików na urządzenie.

### Maksymalna Liczba Równoległych Zadań

Ustaw liczbę równoległych wątków pobierania. Wyższa liczba przyspiesza pobieranie, ale zużywa więcej baterii.

### Zadania Transferu Plików

Wyświetla aktualnie aktywne zadania przesyłania i pobierania.

### Transfery w Tle

Pozwól na pobieranie gdy aplikacja jest w tle. Jeśli transfery w tle zużywają dużo energii, iOS może zawiesić aplikację.

### Zapisz Pobrane Pliki Do

Wybierz domyślny katalog pobierania lub zezwól aplikacji na pytanie przy każdym pobraniu.

### Zsynchronizowane Foldery Offline

Zarządzaj synchronizacją offline dla wybranych folderów. Aby włączyć synchronizację offline, stuknij przycisk z trzema kropkami obok folderu i wybierz **Tryb dostępny offline**. Nowe pliki dodane do folderu w chmurze są automatycznie pobierane na urządzenie. Więcej o trybach offline [tutaj](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Interwał Czasowy

Wybierz, jak często foldery offline są synchronizowane. **Natychmiast** uruchamia synchronizację przy każdym otwarciu aplikacji.

### Pokaż Pełne Nazwy Plików

Pokaż kompletne nazwy plików, włącznie z rozszerzeniami, w menedżerze plików.

### Edytuj Pliki Online

Wyłącz edycję plików online, aby przełączyć się do trybu tylko do odczytu dla podłączonych usług w chmurze i zapobiec przypadkowym usunięciom. To działanie usuwa operacje edycji plików z interfejsu użytkownika.

### Kopiuj Pliki przy Otwieraniu

Określ, jak aplikacja obsługuje importowane pliki z innych aplikacji.

### Miniatury Plików

Zarządzaj i usuwaj wygenerowane miniatury plików, aby zwolnić miejsce.

### Usuń Pliki Tymczasowe

Wyczyść folder pamięci podręcznej aplikacji, aby odzyskać miejsce.

## Edytor Tagów Audio

Skonfiguruj wbudowany edytor tagów audio — przydatny do wsadowego naprawiania problemów z wykonawcą / albumem / rokiem / gatunkiem / okładką albumów.

### Skalowanie Okładki Albumu

Wybierz metodę skalowania używaną przy zapisywaniu okładki albumu do tagów audio.

### Aktualizuj Pliki Online

Gdy włączone, aplikacja automatycznie aktualizuje metadane pliku na serwerze w chmurze po zakończeniu edycji.

### Usuń Plik Po Edycji Online

Wybierz, czy aplikacja powinna usuwać pobraną kopię po zakończeniu edycji pliku online na serwerze w chmurze.

### Przyciski Ekranu Głównego

Wybierz, które przyciski są widoczne na głównym ekranie edytora tagów audio.

W celu głębszej edycji wsadowej wielu plików naraz zainstaluj naszą towarzyszącą aplikację **Evertag**.

## Widżety

Włącz widżety, aby aplikacja aktualizowała dane widżetów podczas odtwarzania. Aktualizacje widżetów wymagają dodatkowej energii, więc przełącznik jest domyślnie wyłączony — włącz go tylko jeśli faktycznie używasz widżetów na ekranie głównym lub ekranie blokady.

Możesz dodać widżety Flacbox, przytrzymując naciśnięty ekran główny lub ekran blokady, stukając **+**, wyszukując **Flacbox** i wybierając rozmiar widżetu. Widżety wyświetlają aktualną okładkę, tytuł ścieżki i wykonawcę, i stukają bezpośrednio do odtwarzacza pełnoekranowego. Widżety działają również na macOS w Centrum powiadomień.

## CarPlay

Zmień ustawienia CarPlay tutaj. To menu jest również dostępne w interfejsie CarPlay, abyś mógł dostosować doświadczenie podczas jazdy.

### Sortowanie

Skonfiguruj opcje sortowania dla wszystkich ekranów CarPlay.

### Limit Ładowania Treści

Wybierz, czy aplikacja używa paginacji na ekranie CarPlay. Paginacja utrzymuje responsywność menu w dużych bibliotekach.

### Kolor Gradientu Ikon Menu

Wybierz schemat kolorów dla ekranu głównego CarPlay.

### Pokaż Obrazy

Wyłącz obrazy na ekranie CarPlay, aby zoptymalizować prędkość ładowania i zmniejszyć zużycie pamięci w dużych bibliotekach.

### Wstrzymaj Odtwarzanie Po Połączeniu

Włącz to, aby uniknąć nagłego głośnego dźwięku po podłączeniu urządzenia do CarPlay.

## Wi-Fi Drive

Aktywuj **Wi-Fi Drive**, aby przenosić pliki z komputera na urządzenie za pomocą desktopu przeglądarki internetowej, Finder lub Eksploratora plików. Szczegółowe instrukcje dotyczące Wi-Fi Drive dostępne [tutaj](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalizacja

Dostosuj interfejs użytkownika do swoich preferencji.

### Ikona Aplikacji

Wybierz alternatywną ikonę aplikacji dla ekranu głównego (Premium).

### Schemat Kolorów

Wybierz motyw interfejsu użytkownika i włącz tryb ciemny. Gdy wybrane jest **Domyślne**, aplikacja stosuje się do ustawień wyglądu urządzenia.

### Styl Tła

Zmodyfikuj styl tła aplikacji. Obecnie jedyną opcją jest **Rozmyta okładka albumów**, która używa okładki aktualnie odtwarzanego utworu jako rozmytego tła aplikacji.

### Wygląd Elementów na Liście

Dostosuj sposób wyświetlania elementów na listach. Przydatne na małych ekranach — możesz pozwolić aplikacji automatycznie dostosować wysokość wiersza lub wyświetlać mniejsze ikony w komórkach listy.

### Limit Ładowania Treści

Domyślnie aplikacja używa paginacji do przyspieszenia ładowania treści. Możesz wyłączyć paginację, aby ładować wszystko naraz.

### Styl Ekranu Pliki Lokalne

Zmień styl prezentacji sekcji **Pliki lokalne**.

### Styl Ekranu Biblioteka Muzyczna

Dostosuj wygląd ekranu **Biblioteka muzyczna**.

### Styl Ekranu Odtwarzacza Audio

Skonfiguruj wygląd ekranu **Odtwarzacza audio**.

### Styl Menu Kontekstowego

Wybierz styl menu kontekstowego wyświetlanego po stuknięciu przycisku **Więcej akcji**.

## Okno

Dostępne na Mac i Catalyst. Skonfiguruj preferencje związane z oknem, takie jak domyślny rozmiar i zachowanie przy uruchomieniu.

## Ekran

Wybierz, czy ekran powinien pozostać aktywny podczas używania aplikacji. Przydatne podczas skanowania dużych bibliotek lub długotrwałej pracy z tagami.

## Dostępność

Aktywuj **Tryb tekstu**, aby ukryć wszystkie obrazy w interfejsie użytkownika. Tryb tekstu jest włączany automatycznie gdy VoiceOver jest aktywny i jest również przydatny dla bardzo małych lub tylko tekstowych konfiguracji.

## Język

Zmień język aplikacji i nadpisz domyślny systemowy. Zmiana wchodzi w życie po całkowitym zamknięciu i ponownym otwarciu Flacbox. Aktualnie obsługiwane lokalizacje obejmują: afrykanerski, akan, albański, amharski, arabski, armeński, asamski, ajmara, azerbejdżański, bambara, bengalski, baskijski, białoruski, bośniacki, bułgarski, birmański, kataloński, cebuano, chiński (uproszczony), chiński (tradycyjny), korsykański, chorwacki, czeski, duński, dhivehi, dogri, holenderski, angielski, esperanto, estoński, ewe, filipiński, fiński, francuski, galicyjski, ganda, gruziński, niemiecki, grecki, guarani, gudżarati, haitański kreolski, hausa, hawajski, hebrajski, hindi, hmong, węgierski, islandzki, igbo, iloko, indonezyjski, irlandzki, włoski, japoński, jawajski, kannada, kazachski, khmerski, kinyarwanda, koreański, krio, kurdyjski, sorani kurdyjski, kirgiski, laotański, łaciński, łotewski, lingala, litewski, luksemburski, macedoński, maithili, malgaski, malajski, malajalam, maltański, maoryski, marathi, mizo, mongolski, nepalski, sotho północny, norweski bokmål, nyanja, odia, oromo, pasztuński, perski, polski, portugalski, pendżabski, rumuński, rosyjski, samoański, sanskryt, szkocki gaelicki, serbski, shona, sindhi, syngaleski, słowacki, słoweński, somalijski, sotho południowy, hiszpański, sundajski, suahili, szwedzki, tadżycki, tamilski, tatarski, telugu, tajski, tsonga, turecki, turkmeński, ukraiński, urdu, ujgurski, uzbecki, wietnamski, walijski, xhosa, jidysz, joruba, zulu.

## Kopia Zapasowa i Przywracanie

Użyj tej funkcji, aby wykonać kopię zapasową wszystkich danych aplikacji lub przenieść je na inne urządzenie. Możesz wybrać, co dołączyć:

- **Baza danych** — wszystkie ścieżki w bibliotece muzycznej, w tym listy odtwarzania. Ścieżki offline nie są dołączone, aby rozmiar pliku kopii zapasowej był zarządzalny.
- **Okładki albumów** — wszystkie zbuforowane okładki albumów.
- **Ustawienia** — wszystkie ustawienia aplikacji.

Stuknij **Utwórz kopię zapasową danych aplikacji**, aby rozpocząć tworzenie kopii zapasowej. Dane aplikacji są zapisywane do jednego pliku, który możesz później użyć do przywrócenia stanu aplikacji na nowym urządzeniu lub po ponownej instalacji.

Aby przywrócić dane aplikacji na nowym urządzeniu, przenieś plik kopii zapasowej na nowe urządzenie za pomocą podłączonej usługi w chmurze lub iCloud i otwórz go na nowym urządzeniu.

Szczegółowe instrukcje krok po kroku: [Jak przenosić bibliotekę muzyczną między urządzeniami: Przewodnik krok po kroku](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Pomoc

Uzyskaj dostęp do przewodnika po aplikacji, aby uzyskać pomoc i wskazówki dotyczące efektywnego używania aplikacji.

## Często Zadawane Pytania

Znajdź odpowiedzi na najczęstsze pytania w sekcji FAQ.

## Wyślij Opinię

Masz opinię lub potrzebujesz pomocy? Wyślij opinię bezpośrednio z aplikacji do naszego zespołu wsparcia.

## Udostępnij Tę Aplikację

Udostępnij aplikację przyjaciołom, aby promować jej używanie.

## Odkryj Więcej Aplikacji

Poznaj inne aplikacje od Everappz.

## Warunki i Postanowienia

Określa warunki i postanowienia korzystania z aplikacji. Prosimy przeczytać je przed użyciem aplikacji.

## Polityka Prywatności

Odwiedź stronę polityki prywatności, aby zrozumieć nasze praktyki obsługi danych. Prosimy przeczytać ją przed użyciem aplikacji.

## Analityka i Zbieranie Danych

Sprawdź, które usługi są włączone do analityki i zbierania danych, i dezaktywuj te, których nie chcesz.

## Informacje Prawne

Zawiera informacje o każdej bibliotece używanej w aplikacji wraz z numerem wersji aplikacji i informacjami o buildzie.
