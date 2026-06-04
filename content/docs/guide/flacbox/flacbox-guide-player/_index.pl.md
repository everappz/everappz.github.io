---
title: "Odtwarzacz Audio"
date: 2020-02-01
description: "Dowiedz się, jak używać odtwarzacza audio Flacbox na iPhone, iPad i Mac. Steruj odtwarzaniem, zarządzaj kolejkami, konfiguruj silnik audio FFmpeg / systemowy, zmieniaj częstotliwość próbkowania, korekcję wysokości tonu, czas buforowania IO, korektor, zakładki audio, AirPlay 2, Google Cast, CarPlay, widżety i skróty klawiszowe na Mac."
keywords: [
  "przewodnik Flacbox odtwarzacz", "ustawienia odtwarzacza audio", "korektor Flacbox",
  "AirPlay strumieniowanie muzyki", "Google Cast muzyka", "zakładki audio",
  "kolejka odtwarzania Flacbox", "powtarzanie losowanie Flacbox", "regulacja głośności Flacbox",
  "mini odtwarzacz macOS", "aplikacja muzyczna VoiceOver",
  "Flacbox FFmpeg", "korekcja wysokości tonu Flacbox", "częstotliwość próbkowania Flacbox",
  "zewnętrzny DAC Flacbox", "dźwięk przestrzenny Flacbox", "bufor IO Flacbox",
  "prędkość odtwarzania Flacbox", "timer snu Flacbox"
]
tags: ["przewodnik", "flacbox", "odtwarzacz"]
readingTime: 14
---


Odtwarzacz Audio to główny ekran aplikacji, w którym sterujesz muzyką i większością funkcji odtwarzania. Tutaj również silnik audio hi-res Flacbox — zbudowany na systemowych kodeków oraz dołączonej bibliotece **FFmpeg** — wykonuje całą ciężką pracę. Przyjrzyjmy się, jak go używać.

## Dostęp do Odtwarzacza Audio

Do odtwarzacza pełnoekranowego można przejść z paska mini odtwarzacza. Na iPhone mini odtwarzacz znajduje się na dole ekranu głównego. Na iPad i Mac jest po lewej stronie. Aby ukryć mini odtwarzacz na iPhone, stuknij go raz i przesuń palcem w dół. Aby całkowicie zamknąć odtwarzacz pełnoekranowy, stuknij przycisk zamykania w prawym dolnym rogu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio Player Main Screen" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Obsługiwane Formaty Audio

Flacbox odtwarza najpopularniejsze formaty audio — zarówno systemowe kodeki Apple, jak i wiele dodatkowych formatów obsługiwanych przez dołączony silnik FFmpeg:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

Obejmuje to niemal każdy nowoczesny stratny i bezstratny format, jaki możesz mieć w swojej osobistej kolekcji muzycznej.

## Elementy Sterowania Odtwarzaniem

Na dole ekranu odtwarzacza znajdziesz przyciski Odtwórz, Pauza, Następny utwór i Poprzedni utwór. Dostępne są również opcjonalne przyciski Następne 30 sek. i Poprzednie 30 sek., które możesz włączyć w ustawieniach aplikacji (przydatne do audiobooków). Możesz przewijać do przodu lub do tyłu, przytrzymując przyciski Następny / Poprzedni. Aby przejść do określonej części utworu, przeciągnij suwak odtwarzania.

## Powtarzanie i Losowanie

Stuknij przycisk powtarzania, aby przełączać między trybami:

- **Powtórz wszystko** — zapętla wszystkie utwory w kolejce.
- **Powtórz jeden** — powtarza tylko bieżący utwór.
- **Zatrzymaj po utworze** — wstrzymuje po zakończeniu bieżącego utworu.
- **Nie powtarzaj** — odtwarza kolejkę jeden raz bez powtarzania.

Użyj przycisku **Losuj**, aby losować kolejność utworów w kolejce.

## Regulacja Głośności

Otwórz ekran Ustawień audio, stukając ikonę dźwięku pod elementami sterowania odtwarzaniem, aby uzyskać dostęp do suwaka głośności. Znajdziesz tu również przyciski **Google Cast** i **AirPlay**, dzięki którym możesz szybko przełączyć odtwarzanie na inne urządzenie.

## Google Cast (Chromecast)

Dla użytkowników Google Cast ikona **Cast** pojawia się na dole odtwarzacza. Stuknij ją, aby wybrać urządzenie i rozpocząć strumieniowanie. Upewnij się, że Twoje urządzenie i odbiornik Google Cast są w tej samej sieci Wi-Fi. Uwaga: nie każdy format audio jest zgodny z Google Cast — niektóre formaty hi-res mogą wymagać transkodowania.

## AirPlay

W przypadku AirPlay poszukaj przycisku **AirPlay** na dole odtwarzacza. Stuknij go i wybierz urządzenie do strumieniowania. Flacbox obsługuje **AirPlay 2**, więc możesz odtwarzać jednocześnie na wielu urządzeniach HomePod, Apple TV lub głośnikach zgodnych z AirPlay 2.

## Korektor Audio

Flacbox zawiera **10-pasmowy korektor** z presetami w stylu iPod. Stuknij Korektor w widoku głośności, a następnie włącz go w prawym górnym rogu. Możesz używać presetów takich jak Akustyczny i Wzmocnienie basów lub dostosować każde pasmo częstotliwości suwakami. Twórz własne presety, zapisuj je pod dowolną nazwą i wzmacniaj ogólną głośność za pomocą wzmacniacza wstępnego. Szczegółowe instrukcje dotyczące korektora znajdziesz [tutaj](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio Player Equalizer" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Pasek Narzędzi Trybu Odtwarzacza

W przypadku niektórych stylów odtwarzacza dostępny jest dedykowany pasek narzędzi na górze odtwarzacza pełnoekranowego. Pasek ten zawiera trzy przydatne przyciski:

- **Szukaj** — szybko znajdź konkretny utwór w kolejce odtwarzacza.
- **Kontrola prędkości odtwarzania** — dostosuj prędkość odtwarzania od 0,02× do 3,00×. Idealne do audiobooków, podcastów i wykładów. Stuknij Normalna, aby przywrócić domyślną prędkość.
- **Zakładki audio** — twórz wiele zakładek dla jednego utworu. Pełne instrukcje dotyczące zakładek znajdziesz [tutaj](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Kolejka Odtwarzacza

Aby zobaczyć kolejkę odtwarzacza, stuknij przycisk kolejki po prawej stronie bieżącej piosenki. Każda piosenka w kolejce ma więcej akcji — stuknij trzy kropki, aby je wyświetlić. Aby zmienić kolejność piosenki, użyj wskaźnika kolejności przy tytule i przeciągnij go na nową pozycję.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Playback Queue" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Komentarze / Teksty

Aby wyświetlić komentarze do utworu i osadzone teksty, a także pliki LRC, wykonaj następujące kroki:

1. Otwórz **Ustawienia**.
2. Przejdź do **Odtwarzacza audio**.
3. Wybierz **Personalizację**.
4. Stuknij **Przyciski na ekranie głównym**.
5. Włącz **Komentarze**.

Następnie stuknij przycisk kolejki odtwarzacza na dole ekranu kilka razy, aby przełączyć się z widoku okładki / kolejki na widok komentarzy. Na ekranie Komentarze przewiń w prawo, aby przełączać się między **Komentarzami**, **Osadzonymi tekstami** i **Plikiem LRC**. Pełne instrukcje znajdziesz [tutaj](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lyrics and Comments Screen" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Menu Opcji

Każda piosenka w kolejce odtwarzacza audio ma menu z dodatkowymi akcjami, dostępne przez stuknięcie przycisku z trzema kropkami przy tytule piosenki.

- **Odtwórz następny** — dodaje piosenkę na górę kolejki odtwarzacza.
- **Dodaj do listy odtwarzania** — dodaje piosenkę do listy odtwarzania z opcją tworzenia nowej.
- **Dodaj do ulubionych** — oznacza piosenkę jako ulubioną w celu szybkiego dostępu.
- **Pobierz** — zapisuje piosenkę w plikach lokalnych, wyświetlaną na karcie **Pliki lokalne** i w sekcji **Muzyka offline**.
- **Edytuj tagi audio** — otwiera wbudowany edytor tagów audio, aby naprawić brakujące metadane, modyfikując piosenkę w pamięci.
- **Pokaż w folderze** — pokazuje folder, w którym przechowywany jest plik audio.
- **Pokaż w Finderze** — w przypadku plików zaimportowanych z komputera Mac pokazuje folder, w którym plik audio jest zlokalizowany na komputerze.
- **Otwórz w** — eksportuje plik audio do innej aplikacji.
- **Usuń z kolejki** — usuwa wybraną piosenkę z kolejki odtwarzacza audio.
- **Usuń z usługi w chmurze** — usuwa piosenkę zarówno z biblioteki muzycznej, jak i z pamięci w chmurze. **Ta akcja jest nieodwracalna.**
- **Usuń z plików lokalnych** — usuwa piosenkę zarówno z biblioteki muzycznej, jak i z lokalnej pamięci. **Ta akcja jest nieodwracalna.**
- **Usuń z biblioteki muzycznej** — usuwa piosenkę z biblioteki muzycznej, zachowując plik w pamięci.

Te same opcje są dostępne dla aktualnie odtwarzanego elementu w kolejce odtwarzacza audio, do którego można uzyskać dostęp, stukając ikonę **Więcej akcji** przy tytule utworu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Options for an Item in the Playback Queue" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Dodatkowe Akcje Odtwarzacza

Stuknij przycisk **Więcej akcji** „..." po lewej stronie tytułu aktualnie odtwarzanej piosenki, aby zobaczyć dodatkowe akcje.

- **Kontynuuj odtwarzanie** — wznów od miejsca, w którym skończyłeś, łącznie z kolejką i pozycją w mediach. Szczególnie przydatne w przypadku audiobooków. Aktywowane w ustawieniach aplikacji.
- **Szukaj** — szybko znajdź konkretny utwór w kolejce odtwarzacza audio.
- **Zakładki** — wyświetl listę utworzonych zakładek audio.
- **Komentarze** — wyświetl komentarze do utworu i osadzone teksty, a także pliki LRC. Pełne instrukcje [tutaj](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Prędkość** — dostosuj prędkość odtwarzania do swoich preferencji.
- **Ostatnie** — uzyskaj dostęp do listy ostatnio odtwarzanych piosenek.
- **Ulubione** — wyświetl kolekcję ulubionych piosenek.
- **Korektor audio** — aktywuj korektor audio.
- **Timer snu** — ustaw timer, aby zatrzymać odtwarzanie po określonym czasie. Idealne dla tych chwil, gdy chcesz zasnąć przy muzyce.
- **Zapisz kolejkę jako listę odtwarzania** — zapisz bieżącą kolejkę odtwarzacza audio jako nową listę odtwarzania.
- **Usuń kolejkę** — wyczyść kolejkę odtwarzacza i zatrzymaj odtwarzanie.
- **Ustawienia** — uzyskaj dostęp do ustawień odtwarzacza audio.
- **Pomoc** — znajdź pomoc i wskazówki.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio Player More Actions Screen" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Zakładki Audio

Ta funkcja pozwala tworzyć wiele zakładek dla utworów w bibliotece muzycznej — idealne do audiobooków, wykładów, długich miksów DJ-skich lub oznaczania refrenu ulubionego utworu.

Aby utworzyć nową zakładkę:

- Rozpocznij odtwarzanie wybranej piosenki.
- Otwórz ekran odtwarzacza.
- Stuknij przycisk **Zakładki** na pasku narzędzi trybu odtwarzacza.
- Wybierz **Dodaj zakładkę**.
- Wybierz czas zakładki i stuknij **Gotowe** w prawym górnym rogu.

Edytowanie zakładek bieżącego utworu jest proste: stuknij Edytuj w prawym górnym rogu, aby wejść w tryb edycji. W tym trybie możesz zmieniać kolejność zakładek, usuwać je, dostosowywać czas zakładki i zmieniać tytuły zakładek. Szczegółowe instrukcje dotyczące zakładek audio znajdziesz [tutaj](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio Bookmarks Screen" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Ostatnie i Ulubione

Na ekranie odtwarzacza stuknij trzy kropki, aby uzyskać dostęp do Ostatnich i Ulubionych. W obu sekcjach możesz wyszukiwać piosenki, odtwarzać wszystkie, losować wszystkie, eksportować listę i czyścić listę. Szczegółowe instrukcje dotyczące eksportowania list piosenek znajdziesz [tutaj](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Podłącz iPhone do samochodu przez USB lub bezprzewodowy Apple CarPlay, a Flacbox pojawi się na ekranie głównym CarPlay, gotowy do bezpiecznego odtwarzania muzyki podczas jazdy. Interfejs CarPlay zawiera dedykowane karty dla Biblioteki, Połączeń, Plików lokalnych i Ustawień, z elementami sterowania odtwarzaniem, losowaniem, powtarzaniem, zarządzaniem kolejką i korektorem audio — wszystko dostępne bez sięgania po telefon. Skonfiguruj środowisko CarPlay dalej w Ustawienia → CarPlay — opcje sortowania, paginacja, kolor gradientu ikon menu, czy obrazy są ładowane, i opcja automatycznego wstrzymywania odtwarzania po podłączeniu do CarPlay.

[Przeczytaj pełny przewodnik CarPlay](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox on Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Widżety Ekranu Głównego (iPhone i iPad)

Flacbox obsługuje widżety ekranu głównego i ekranu blokady iOS, dzięki czemu możesz widzieć i sterować odtwarzaniem na pierwszy rzut oka. Upewnij się, że widżety są włączone w Ustawienia → Widżety → Włącz widżety, a następnie przytrzymaj naciśnięty ekran główny lub ekran blokady, stuknij **+**, wyszukaj **Flacbox** i dodaj widżet. Widżet odświeża się podczas odtwarzania, aby wyświetlać okładkę, tytuł i wykonawcę aktualnie odtwarzanego utworu.

## Okno Mini Odtwarzacza (tylko Mac)

Użytkownicy Mac mogą korzystać z kompaktowego mini odtwarzacza zawsze na górze. Przesuń kursor do prawego dolnego rogu okna Flacbox, zmień rozmiar do minimum i stuknij przycisk zwijania. Utrzymaj go na wierzchu każdego innego okna, wybierając Okno → Pokaż okno zawsze na górze na pasku menu — idealne do utrzymania widoczności elementów sterowania muzyką podczas pracy w innej aplikacji.

## Skróty Klawiszowe (tylko Mac)

Dla użytkowników Mac dostępne jest systemowe menu odtwarzania na pasku statusu ze skrótami klawiszowymi. Na przykład naciśnij spację, aby Odtwarzać / Pauzować. Dostępne są również skróty dla Zatrzymaj, Następna piosenka, Poprzednia piosenka, Pomiń czas, Powtarzaj, Losuj i Prędkość odtwarzania.

## Ustawienia Odtwarzacza Audio

Aby uzyskać dostęp do ustawień, stuknij przycisk Więcej na ekranie odtwarzacza i wybierz Ustawienia. Znajdziesz tam kilka sekcji opisanych poniżej.

### Ogólne

Te ustawienia dotyczą podstawowych aspektów odtwarzacza audio, w tym kolejki odtwarzania, wyjścia audio i zapisywania stanu odtwarzacza.

- **Tryb powtarzania** — wybierz zachowanie odtwarzacza audio po zakończeniu utworu:
  - **Powtórz wszystko** — powtarza wszystkie utwory w kolejce.
  - **Powtórz jeden** — powtarza tylko bieżący utwór.
  - **Zatrzymaj po utworze** — wstrzymuje odtwarzanie po zakończeniu bieżącego utworu.
  - **Nie powtarzaj** — pozwala odtworzyć kolejkę do końca bez powtarzania.
- **Tryb losowania** — losuje kolejność utworów w kolejce. Możesz go **wyłączyć** lub **włączyć**.
- **Koder audio** — wybierz silnik audio używany do odtwarzania:
  - **System Codec + FFmpeg** — priorytetowo używa systemowego kodeka audio tam gdzie to możliwe, zwiększając kompatybilność i stabilność. Korekcja wysokości tonu i regulacja częstotliwości próbkowania wyjścia audio mogą być ograniczone w tym trybie.
  - **FFmpeg** — wymusza użycie kodeka FFmpeg dla wszystkich plików audio, umożliwiając dostosowanie korekcji wysokości tonu i częstotliwości próbkowania wyjścia audio.
- **Częstotliwość próbkowania wyjścia audio** — dostosuj częstotliwość próbkowania wyjścia audio, aby zoptymalizować jakość dźwięku, szczególnie przydatne przy zewnętrznym DAC. Dostępne wartości: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** i **96 kHz**.
- **Liczba kanałów wyjścia audio** — dla wielokanałowych systemów audio z zewnętrznym DAC określ liczbę kanałów: **Mono, Stereo, Center / Left / Right, Center / Left / Right / Surround, ITU BS.775-1, 5.1 Surround** i **SDDS**.
- **Preferowany czas buforowania IO wyjścia audio** — skonfiguruj czas trwania bufora wejścia/wyjścia dla odtwarzania audio. Typowa wartość minimalizująca opóźnienie przy odtwarzaniu audio wysokiej rozdzielczości wynosi około **5 milisekund (0,005 sekundy)**. Dopuszczalny rozmiar bufora zależy od środowiska sprzętowego i programowego, więc przetestuj różne czasy trwania na docelowym urządzeniu i wybierz ten, który najlepiej równoważy niskie opóźnienie i bezproblemowe odtwarzanie.
- **Tryb wyjścia audio (tylko iOS)** — skonfiguruj mieszany tryb wyjścia audio, dzięki czemu dźwięk z Flacbox miesza się z innymi aplikacjami. Szczegółowe instrukcje znajdziesz [tutaj](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Zapisz pozycję odtwarzania** — zapewnia zapisywanie i przywracanie pozycji odtwarzania dla piosenek w bibliotece muzycznej.
- **Zapisz stan odtwarzacza audio** — zachowuje stan odtwarzacza audio przed zamknięciem aplikacji. Aby kontynuować odtwarzanie, stuknij **Kontynuuj odtwarzanie** na górze dowolnego folderu, albumu, wykonawcy lub gatunku po ponownym otwarciu aplikacji. Możesz również przywrócić odtwarzanie dla poszczególnych plików, stukając konkretny utwór.

Po włączeniu zarówno **Zapisz pozycję odtwarzania**, jak i **Zapisz stan odtwarzacza audio**, otwórz dowolny folder, album, wykonawcę lub gatunek, a na górze ekranu zobaczysz przycisk **Kontynuuj odtwarzanie** wraz z ostatnio zapisanym utworem i pozycją. Stuknij go, aby wznowić dokładnie tam, gdzie skończyłeś.

### Personalizacja

Personalizacja pozwala dostosować wygląd ekranu odtwarzacza audio, zmienić dostępne elementy sterowania na ekranie głównym, ekranie blokady i pasku statusu oraz skonfigurować elementy sterowania pomijaniem czasu.

- **Styl ekranu odtwarzacza audio** — skonfiguruj rozmieszczenie elementów na ekranie odtwarzacza audio.
- **Styl przewijania okładek albumów** — skonfiguruj preferowany styl przewijania dla okładek albumów.
- **Dodatkowe elementy** — włącz dodatkowe elementy na ekranie odtwarzacza audio. **Informacje o formacie audio** wyświetlają informacje audio bieżącego utworu nad okładką; **Suwak głośności audio** wyświetla suwak wyjścia audio pod elementami sterowania odtwarzaniem.
- **Akcje ekranu głównego** — skonfiguruj, które przyciski powinny być domyślnie widoczne na głównym ekranie odtwarzacza audio: **Tryb powtarzania i losowania, Następna i poprzednia piosenka, Pomiń czas, Timer snu, Google Chromecast, AirPlay i Bluetooth, Korektor audio, Szukaj, Zakładki, Prędkość, Dodaj zakładkę, Dodaj do ulubionych, Komentarze** i inne.
- **Elementy sterowania odtwarzaniem na ekranie blokady** — wybierz, które elementy sterowania pojawiają się na ekranie blokady. Możliwe wartości: **Pomiń czas, Dodaj zakładkę, Dodaj do ulubionych**.
- **Przyciski pomijania czasu** — wybierz interwał czasu dla przycisków **Pomiń czas**.

### Ładowanie Plików

Podczas procesu ładowania pliku możesz zmienić typ sieci używanej do ładowania piosenek. Dostępne opcje: **Wi-Fi**, **Wi-Fi i dane komórkowe**.

- **Czas wstępnego ładowania** — ustaw interwał czasu buforowania. Zwiększ tę wartość, jeśli masz słabe połączenie sieciowe.
- **Użyj bezpośredniego URL** — gdy włączone, bezpośredni URL jest używany do ładowania piosenki, jeśli serwer to obsługuje. Może to przyspieszyć ładowanie piosenek, ale może wpłynąć na stabilność odtwarzania.

### Korektor Audio

Dostosuj ustawienia korektora audio. Więcej informacji o konfiguracji korektora audio znajdziesz [tutaj](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Prędkość Odtwarzania

Dostosuj prędkość odtwarzania odtwarzacza audio od **0,02× do 3,00×**. Stuknij ikonę konfiguracji w prawym górnym rogu, aby przełączyć się do **trybu precyzyjnego** w celu dokładniejszych regulacji.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Playback Speed Screen" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Korekcja Wysokości Tonu

Zmień ustawienia korekcji wysokości tonu, używając predefiniowanych wartości. Możesz również przełączać się między predefiniowanymi wartościami a trybem precyzyjnym, stukając przycisk w prawym górnym rogu. Korekcja wysokości tonu jest dostępna w ścieżce kodeka FFmpeg z zakresem od **-1000 do +1000**.

### Pamięć Podręczna Odtwarzania

Piosenki w kolejce odtwarzacza audio są automatycznie pobierane, aby zapewnić płynne odtwarzanie. Jeśli ręcznie pobierasz pliki audio, możesz wyłączyć tę opcję, aby uniknąć duplikatów. Możesz tu również skonfigurować rozmiar pamięci podręcznej odtwarzacza audio.

### Timer Snu

Aktywuj timer, aby automatycznie zatrzymać odtwarzanie po określonym czasie — przydatne, gdy chcesz zasnąć przy muzyce. Stuknij ikonę konfiguracji w prawym górnym rogu, aby uzyskać **tryb precyzyjny** z granularnością minutową.

## Dostępność

Flacbox jest w pełni dostępny z **VoiceOver**. Każdy komponent ma dobrze zaprojektowaną etykietę i opis. Gdy VoiceOver jest aktywny, aplikacja przełącza się do **Trybu tekstu**, dzięki czemu wyświetlane są tylko istotne elementy — poprawa prędkości nawigacji i przejrzystości. Możesz również aktywować Tryb tekstu w **Ustawienia → Dostępność → Tryb tekstu**.

### Dostosowywanie Suwaków z VoiceOver

1. **Wybierz suwak** — przesuń palcem w lewo lub w prawo, aż VoiceOver go ogłosi.
2. **Dostosuj wartość** — dwukrotnie stuknij i przytrzymaj suwak, a następnie przeciągnij w górę lub w dół, aby szybko zmienić wartość. VoiceOver ogłasza nową wartość w miarę postępów.

### Dostosowywanie Pozycji Utworu na Liście z VoiceOver

1. Stuknij ikonę wskaźnika kolejności przy tytule utworu, aby dać jej fokus.
2. Szybko dwukrotnie stuknij wskaźnik kolejności. Przy drugim stuknięciu nie unoś palca — przytrzymaj go, aż usłyszysz dźwięk wskazujący, że komórka jest gotowa do przeniesienia.
3. Przenieś komórkę na nową pozycję.

Pozostałe komponenty działają zgodnie z oczekiwaniami, używając systemowych wzorców VoiceOver.
