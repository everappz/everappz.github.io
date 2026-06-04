---
title: "Odtwarzacz multimediów"
date: 2020-02-01
lastmod: 2026-06-01
description: "Dowiedz się, jak korzystać z odtwarzacza multimediów Evervideo na iPhone, iPad i Mac. Obraz w obrazie, sprzętowo przyspieszane dekodowanie H.264 / HEVC, korektory audio i wideo, napisy główne i drugorzędne, wybór ścieżek audio i wideo, skalowanie i obrót wideo, prędkość odtwarzania, timer uśpienia, AirPlay 2, Google Chromecast, strumienie RTSP i kompaktowy odtwarzacz zawsze na ekranie."
keywords: [
  "poradnik odtwarzacza Evervideo", "ustawienia odtwarzacza wideo", "korektor Evervideo",
  "obraz w obrazie iPhone", "wideo PiP iPad", "wideo PiP Mac",
  "wideo AirPlay 2", "wideo Google Chromecast",
  "napisy wideo iPhone", "zewnętrzne napisy SRT",
  "odtwarzacz napisów ASS SSA", "libass iOS",
  "podwójne napisy nauka języka",
  "korektor wideo jasność kontrast", "korektor audio odtwarzacz wideo",
  "blokada obrotu odtwarzacza", "tryb skalowania wideo iOS",
  "sprzętowy dekoder H.264 iPhone", "sprzętowy dekoder HEVC iPad",
  "prędkość odtwarzania wideo", "odtwarzacz wideo FFmpeg iOS",
  "odtwarzacz RTSP iPhone", "kompaktowy odtwarzacz wideo",
  "odtwarzacz VR 360 wideo iPhone"
]
tags: ["poradnik", "evervideo", "odtwarzacz", "PiP", "napisy", "korektor wideo"]
readingTime: 14
---


Odtwarzacz multimediów to główny ekran aplikacji, w którym kontrolujesz odtwarzanie i większość funkcji Evervideo. Odtwarza zarówno pliki wideo, jak i audio i jest zbudowany na niestandardowym odtwarzaczu opartym na FFmpeg ze sprzętowym przyspieszeniem H.264 i HEVC, który wykonuje ciężką pracę. Poznajmy, jak go używać.

## Dostęp do odtwarzacza multimediów

Do odtwarzacza pełnoekranowego możesz dotrzeć z paska kompaktowego odtwarzacza. Na iPhone kompaktowy odtwarzacz znajduje się na górze głównego ekranu. Na iPad i Mac jest po lewej stronie (lub na górze głównego panelu). Aby zwinąć odtwarzacz pełnoekranowy z powrotem do widoku kompaktowego, dotknij przycisku zamknięcia w prawym dolnym rogu lub przesuń w dół. Aby całkowicie ukryć kompaktowy odtwarzacz, dotknij i przesuń w dół jeszcze raz.

Kompaktowy odtwarzacz pozostaje widoczny podczas przeglądania biblioteki, menedżera plików lub ustawień, dzięki czemu nigdy nie tracisz wideo podczas szukania następnego.

{{< cards cols="1">}}
  {{< card title="" subtitle="Odtwarzacz multimediów pełnoekranowy Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Obsługiwane formaty wideo i audio

Evervideo odtwarza praktycznie każdy nowoczesny kontener i kodek przez dołączony silnik FFmpeg, ze sprzętowo przyspieszonym dekodowaniem H.264 i HEVC na obsługiwanych urządzeniach.

- **Kontenery wideo:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — i wiele więcej.
- **Kodeki wideo:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — oraz praktycznie każdy inny kodek obsługiwany przez FFmpeg.
- **Kodeki audio:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — i wiele więcej.
- **Formaty napisów:** SRT, VTT (WebVTT), ASS / SSA i osadzone tekstowe lub graficzne ścieżki napisów.
- **Protokoły strumieniowania:** HTTP / HTTPS, HLS (m3u8), RTSP (kamery IP i IPTV) i bezpośrednie strumieniowanie plików przez SMB / WebDAV / FTP / SFTP / NFS / DLNA.

Obejmuje to praktycznie każdy plik wideo, z jakim możesz się spotkać — w tym ripy MKV, strumienie RTSP z kamer bezpieczeństwa i pliki webm z AV1.

## Sterowanie odtwarzaniem

Na dole ekranu odtwarzacza zobaczysz przyciski Odtwórz, Pauza, Następny i Poprzedni. Dostępne są również opcjonalne przyciski Pomiń do przodu i Pomiń do tyłu (domyślnie 10 sekund), które możesz włączyć w ustawieniach aplikacji. Przytrzymaj przyciski Następny / Poprzedni, aby przewijać do przodu lub do tyłu. Przeciągnij suwak odtwarzania, aby przejść do dowolnej pozycji.

## Powtarzanie i losowanie

Dotknij przycisku powtarzania, aby przechodzić między trybami:

- **Powtarzaj wszystkie** — zapętla każde wideo w kolejce.
- **Powtarzaj jedno** — powtarza tylko bieżące wideo.
- **Zatrzymaj po zakończeniu** — wstrzymuje, gdy bieżące wideo się kończy.
- **Nie powtarzaj** — odtwarza kolejkę raz bez powtarzania.

Użyj przycisku **Losuj**, aby losowo zmienić kolejność filmów w kolejce.

## Obraz w obrazie (PiP)

Na iPhone i iPad Evervideo w pełni obsługuje Obraz w obrazie (PiP). Dotknij ikony PiP na ekranie odtwarzacza lub po prostu przesuń Evervideo w tło — wideo nadal odtwarza się w pływającym oknie ponad każdą inną aplikacją. Przeciągnij pływające okno do dowolnego rogu; zsuń, aby zmienić rozmiar; dotknij raz, aby wyświetlić podstawowe przyciski odtwarzania / pauzy / pomijania; dotknij małego przycisku rozwijania, aby wrócić do pełnej Evervideo.

PiP działa ze wszystkimi formatami wideo odtwarzanymi przez Evervideo, w tym z plikami strumieniowanymi z chmury i strumieniami RTSP. PiP działa też, gdy telefon jest zablokowany (w zależności od ustawień automatycznej blokady).

## Kompaktowy odtwarzacz

Kompaktowy odtwarzacz to trwały mini-odtwarzacz, który pozostaje widoczny na górze każdego ekranu w aplikacji podczas przeglądania biblioteki, menedżera plików lub ustawień. Dotknij, aby rozwinąć do odtwarzacza pełnoekranowego; przesuń w dół, aby go ponownie zwinąć.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ustawienia wideo z widoku kompaktowego odtwarzacza na głównym ekranie Evervideo" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

W przypadku AirPlay dotknij przycisku AirPlay na odtwarzaczu. Evervideo obsługuje AirPlay 2, dzięki czemu możesz przesyłać wideo do Apple TV, HomePod lub dowolnego głośnika lub inteligentnego telewizora zgodnego z AirPlay 2. W konfiguracji z wieloma urządzeniami AirPlay możesz jednocześnie kierować audio do wielu odbiorników.

## Google Chromecast

Dla użytkowników Google Cast ikona Cast pojawia się na odtwarzaczu. Dotknij, aby wybrać urządzenie i rozpocząć przesyłanie. Upewnij się, że telefon i odbiornik Cast są w tej samej sieci Wi-Fi. Nie każdy kodek jest obsługiwany przez sprzęt Chromecast — niektóre pliki mogą wymagać transkodowania.

## Strumienie RTSP na żywo

Evervideo może bezpośrednio odtwarzać źródła RTSP — kamery IP, kamery wideo-domofonu, strumienie IPTV, sygnały nadawcze i każdy inny adres URL `rtsp://`. Dodaj strumień jako połączenie RTSP w Pliki → Łącza online → Dodaj link, a następnie dotknij, aby rozpocząć oglądanie. Strumienie RTSP działają w Obrazie w obrazie, kompaktowym odtwarzaczu i przesyłają przez AirPlay 2 i Chromecast tak samo jak zwykłe wideo.

## Wybór ścieżki audio

W przypadku filmów z wieloma ścieżkami audio (komentarz, alternatywny dubbing, ścieżka reżysera) dotknij przycisku Więcej akcji na odtwarzaczu i wybierz Ścieżka audio — następnie wybierz żądaną ścieżkę. Jest to niezbędne dla filmów obcojęzycznych, plików BDMV / MKV z wieloma dubbingami i materiałów instruktażowych ze ścieżkami komentarzy.

## Wybór ścieżki wideo

Niektóre pliki wideo zawierają wiele strumieni wideo (Blu-ray wielokątowe, alternatywne wersje). Wybierz Ścieżka wideo z menu Więcej akcji, aby przełączać się między nimi podczas odtwarzania.

## Napisy — wewnętrzne i zewnętrzne

Evervideo daje precyzyjną kontrolę nad napisami:

- **Ścieżka napisów** — wybierz spośród ścieżek osadzonych w pliku.
- **Zewnętrzne pliki napisów** — załaduj pliki `.srt`, `.vtt`, `.ass` lub `.ssa` z urządzenia, iCloud Drive lub dowolnej podłączonej usługi w chmurze.
- **Renderowanie Libass** — zaawansowane stylizacje ASS / SSA (czcionki, kolory, pozycje, efekty karaoke) są renderowane poprawnie dzięki dołączonej bibliotece libass.
- **Wybór czcionki** — wybierz niestandardową czcionkę dla głównych napisów i osobną czcionkę dla drugorzędnych. Dostępne są dołączone czcionki oraz każda czcionka zainstalowana na urządzeniu.

Wszystko to możesz skonfigurować w Ustawienia → Napisy przed odtwarzaniem lub użyć Więcej akcji → Napisy z odtwarzacza, aby zmienić w locie.

## Korektor audio

Evervideo zawiera pełny korektor audio do dostrojenia ścieżek dźwiękowych wideo dla słuchawek, głośników lub systemu hi-fi. Dotknij ikony korektora na głośności (lub akcji Korektor audio w menu Więcej akcji odtwarzacza), włącz korektor przełącznikiem w prawym górnym rogu i wybierz preset lub przeciągnij suwaki pasm, aby zbudować własny preset. Niestandardowe presety można eksportować i importować, aby udostępniać je między urządzeniami lub tworzyć kopie zapasowe.

## Korektor wideo

Do dostrajania obrazu Evervideo udostępnia dedykowany korektor wideo — reguluj jasność, kontrast, nasycenie i odcień w czasie rzeczywistym podczas odtwarzania. Podobnie jak korektor audio, niestandardowe presety wideo można eksportować i importować do udostępniania lub kopii zapasowych. Użyj go, aby rozjaśnić ciemną scenę w słoneczny dzień, zwiększyć nasycenie wyblakłych treści lub ocieplić zimny odcień koloru.

{{< cards cols="1">}}
  {{< card title="" subtitle="Korektor wideo Evervideo" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Tryb skalowania wideo

Wybierz sposób wypełniania ekranu przez wideo:

- **Dopasuj** — zachowaj oryginalny współczynnik proporcji; czarne paski tam, gdzie potrzeba.
- **Wypełnij** — wypełnij cały ekran, przycinając wideo w razie potrzeby.
- **Rozciągnij** — rozciągnij wideo, aby wypełnić ekran, zniekształcając w razie potrzeby.
- **Oryginalny** — zachowaj natywną rozdzielczość 1:1.

## Obrót wideo

W przypadku filmów nagranych w złej orientacji wybierz **Więcej akcji → Obrót** i wybierz **0°**, **90°**, **180°** lub **270°**, aby obrócić obraz bez opuszczania odtwarzacza.

## Dekodowanie sprzętowe (H.264 i HEVC)

W Ustawienia → Odtwarzacz → Wideo możesz niezależnie włączyć / wyłączyć Sprzętowe dekodowanie H.264 i Sprzętowe dekodowanie H.265 (HEVC). Dekodowanie sprzętowe jest szybsze, zużywa mniej baterii i działa chłodniej — ale w rzadkich przypadkach (uszkodzone pliki, egzotyczne profile) może być konieczne wyłączenie sprzętowego dekodowania i przełączenie na programowe dekodowanie FFmpeg. Evervideo pozwala to zrobić dla każdego pliku z menu Więcej akcji odtwarzacza.

## Viewport VR 360°

Evervideo zawiera viewport VR / 360° do sferycznych plików wideo. Podczas odtwarzania wideo 360°, możesz przeciągać, aby rozglądać się, szczypać, aby powiększyć, a Evervideo wyrenderuje obraz w czasie rzeczywistym.

## Prędkość odtwarzania

Dotknij kontrolki Prędkość na pasku narzędzi odtwarzacza, aby zmienić prędkość odtwarzania — zwolnij do analizy (0,25× lub 0,5×) lub przyspiesz do tutoriali i wykładów (1,25×, 1,5×, 2× i do 3×). Dotknij ikony konfiguracji w prawym górnym rogu ekranu Prędkości, aby przełączyć się na tryb precyzyjny z dokładniejszymi regulacjami. Dostępna jest również korekcja tonacji na ścieżkę.

{{< cards cols="1">}}
  {{< card title="" subtitle="Prędkość odtwarzania na głównym pasku narzędzi Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Kolejka odtwarzacza

Aby zobaczyć kolejkę odtwarzacza, dotknij przycisku kolejki na odtwarzaczu. Każde wideo w kolejce ma więcej akcji — dotknij trzy kropki, aby je zobaczyć. Aby zmienić kolejność wideo w kolejce, użyj wskaźnika zmiany kolejności obok tytułu i przeciągnij go na nową pozycję.

{{< cards cols="1">}}
  {{< card title="" subtitle="Kolejka odtwarzania Evervideo" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Timer uśpienia

Otwórz Ustawienia → Odtwarzacz → Timer uśpienia, włącz go i wybierz, jak długo ma trwać odtwarzanie przed automatycznym zatrzymaniem. Możesz też dodać przycisk Timera uśpienia bezpośrednio do głównego ekranu odtwarzacza przez Ustawienia → Odtwarzacz → Personalizacja → Akcje głównego ekranu.

## Zakładki odtwarzacza

Zapisz swoje miejsce w długich filmach — wykładach, audiobookach-wideo, tutorialach, długich pobraniach z YouTube — dotykając Dodaj zakładkę z menu Więcej akcji. Zakładki pojawiają się w liście Więcej akcji → Zakładki wideo i utrzymują się między sesjami.

## Menu Więcej akcji

Dotknij przycisku **Więcej akcji „..."** na odtwarzaczu, aby uzyskać dostęp do dodatkowych funkcji.

- **Kontynuuj odtwarzanie** — wznów kolejkę od ostatniej pozycji.
- **Szukaj** — znajdź konkretne wideo w kolejce.
- **Zakładki** — przeglądaj i przeskakuj do zakładek.
- **Prędkość** — dostosuj prędkość odtwarzania.
- **Ostatnie** — ostatnio odtwarzane filmy.
- **Ulubione** — ulubione filmy.
- **Korektor audio** — aktywuj korektor audio.
- **Korektor wideo** — aktywuj korektor wideo.
- **Ścieżka audio** — wybierz strumień audio.
- **Ścieżka wideo** — wybierz strumień wideo.
- **Napisy** — ścieżka główna / drugorzędna, plik zewnętrzny, czcionka.
- **Obrót** — obróć obraz 0° / 90° / 180° / 270°.
- **Tryb skalowania** — Dopasuj / Wypełnij / Rozciągnij / Oryginalny.
- **Obraz w obrazie** — wejdź w tryb PiP.
- **AirPlay** / **Chromecast** — wyślij na urządzenie.
- **Timer uśpienia** — ustaw timer do zatrzymania odtwarzania.
- **Zapisz kolejkę jako listę odtwarzania** — zapisz bieżącą kolejkę jako nową listę odtwarzania.
- **Usuń kolejkę** — wyczyść kolejkę i zatrzymaj odtwarzanie.
- **Ustawienia** — przejdź bezpośrednio do ustawień odtwarzacza.
- **Pomoc** — otwórz wskazówki.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ekran Więcej akcji odtwarzacza Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Ustawienia odtwarzacza

Pełne drzewo ustawień odtwarzacza jest udokumentowane w [poradniku Ustawień](/docs/guide/evervideo/evervideo-guide-settings/). Najczęściej używane sekcje:

- **Ogólne** — tryb powtarzania, tryb losowania, Zapisz stan odtwarzacza, Zapisz pozycję odtwarzania, interwały pomijania.
- **Wideo** — sprzętowe dekodowanie H.264 / HEVC, korektor wideo, tryb skalowania, obrót, tryb wyświetlania, preferowana liczba klatek, preferowany format pikseli, viewport VR.
- **Audio** — korektor audio, częstotliwość próbkowania, kanały, czas trwania bufora IO, tryb mieszany.
- **Napisy** — ścieżka główna / drugorzędna, wybór pliku zewnętrznego, czcionka, drugorzędna czcionka.
- **Urządzenia** (iOS) — AirPlay / Chromecast.
- **Personalizacja** — styl układu odtwarzacza (Minimalny / Dolny / Antyczny / Klasyczny), akcje głównego ekranu, sterowanie ekranem blokady.
- **Pamięć podręczna odtwarzania** — pamięć podręczna dysku do płynniejszego strumieniowania.
- **Timer uśpienia** — automatyczne zatrzymanie.

## Dostępność

Evervideo jest w pełni dostępna z VoiceOver. Każdy komponent ma dobrze zaprojektowaną etykietę i opis. Gdy VoiceOver jest aktywny, aplikacja przełącza się w Tryb tekstowy, dzięki czemu wyświetlane są tylko znaczące elementy — poprawiając szybkość nawigacji i przejrzystość. Możesz też aktywować Tryb tekstowy w Ustawienia → Dostępność → Tryb tekstowy.

### Dostosowywanie suwaków za pomocą VoiceOver

1. **Zaznacz suwak** — przesuń w lewo lub w prawo, aż VoiceOver go ogłosi.
2. **Dostosuj wartość** — dwukrotnie dotknij i przytrzymaj suwak, a następnie przeciągnij w górę lub w dół, aby szybko zmienić wartość. VoiceOver ogłasza nową wartość podczas przesuwania.

Inne elementy działają zgodnie z oczekiwaniami, korzystając ze wzorców VoiceOver dostarczanych przez system.
