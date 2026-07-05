---
title: "Evermusic 8.7: prawdziwe odtwarzanie bez przerw, efekty audio, normalizacja głośności, przeprojektowany korektor"
date: 2026-07-05
description: "Evermusic 8.7 dla iPhone, iPad i Mac dodaje prawdziwe odtwarzanie bez przerw, pięć studyjnych efektów audio (pogłos, opóźnienie, przester, kompresor, crossfeed), normalizację głośności EBU R128, przeprojektowany 10-pasmowy korektor z importem/eksportem presetów, przebudowany silnik strumieniowania AVAudioEngine z obsługą FLAC i Ogg Vorbis oraz szybsze i dokładniejsze CarPlay i Teraz odtwarzane."
keywords: ["Evermusic 8.7", "aktualizacja Evermusic", "prawdziwe odtwarzanie bez przerw iPhone", "odtwarzacz muzyki bez przerw iOS", "odtwarzanie bez przerw CarPlay", "efekty audio odtwarzacz muzyki iPhone", "pogłos opóźnienie przester kompresor crossfeed iOS", "crossfeed słuchawki iOS", "normalizacja głośności iPhone", "normalizacja głośności odtwarzacz muzyki", "normalizacja EBU R128 iOS", "alternatywa dla replay gain iPhone", "10-pasmowy korektor iPhone", "korektor graficzny aplikacja iOS", "import eksport presetów korektora", "odtwarzacz FLAC iPhone", "odtwarzacz Ogg Vorbis iOS", "odtwarzacz muzyki bezstratnej iPhone 2026", "odtwarzacz muzyki AVAudioEngine", "odtwarzacz muzyki CarPlay iPhone", "dokładność Teraz odtwarzane ekran blokady", "odtwarzacz muzyki w chmurze iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Odtwarzanie bez przerw", "Efekty audio", "Pogłos", "Opóźnienie", "Przester", "Kompresor", "Crossfeed", "Normalizacja głośności", "EBU R128", "Korektor", "FLAC", "Ogg Vorbis", "CarPlay", "Teraz odtwarzane", "Liquid Glass", "Nowości"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**W skrócie:** [Evermusic 8.7](/products/evermusic) to wydanie skupione na jakości dźwięku dla iPhone, iPad i Mac. Zawiera **prawdziwe odtwarzanie bez przerw** (bez pauz, kliknięć czy trzasków między utworami), pełny zestaw **studyjnych efektów audio** — pogłos, opóźnienie, przester, kompresor i crossfeed — oraz **normalizację głośności EBU R128**, która utrzymuje spójną głośność od utworu do utworu bez znaczników ReplayGain. **10-pasmowy korektor** został przeprojektowany z nowymi suwakami, szybszym przełączaniem presetów, własnymi presetami, które można importować i eksportować, oraz lepszym układem w orientacji poziomej i na iPad. Od środka **przebudowany silnik strumieniowania AVAudioEngine** poprawia niezawodność i obsługę formatów, w tym **FLAC** i **Ogg Vorbis**. **CarPlay** i **Teraz odtwarzane** są szybsze i dokładniejsze na ekranie blokady, w samochodzie i z pilotów w słuchawkach.

---

## Witajcie wszyscy!

Evermusic 8.7 jest dostępny do pobrania. Ta aktualizacja dotyczy tego, jak *brzmi* Twoja muzyka. Przebudowaliśmy silnik odtwarzania dla prawdziwego odtwarzania bez przerw, dodaliśmy zestaw studyjnych efektów audio, wprowadziliśmy normalizację głośności i przeprojektowaliśmy korektor od suwaków w górę. Wszystko jest ubrane w nowy design **Liquid Glass** firmy Apple.

[Pobierz Evermusic 8.7 z App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) lub zaktualizuj z istniejącej wersji. Evermusic jest darmowy do pobrania z opcjonalnymi ulepszeniami w aplikacji.

## Prawdziwe odtwarzanie bez przerw

Odtwarzanie bez przerw oznacza, że ciszy między dwoma utworami już nie ma. Bez pauzy, bez kliknięcia, bez trzasku — bieżący utwór przechodzi prosto w następny. Ma to największe znaczenie w przypadku muzyki zaprojektowanej tak, by słuchać jej jako całości: **nagrań koncertowych, miksów DJ, utworów klasycznych i albumów koncepcyjnych**, w których jeden utwór wycisza się bezpośrednio w drugi.

Oto, co zmieniło się od strony technicznej. Silnik audio Evermusic utrzymuje dwa utwory w grze jednocześnie: ten, którego słuchasz, i następny w kolejce. Gdy bieżący utwór gra, następny jest już **pobierany, dekodowany i wstępnie buforowany** w tle. Gdy bieżący utwór dociera do końca, silnik przełącza się na następny utwór **wewnątrz odtwarzacza, a nie wewnątrz strumienia audio**. Pętla renderująca wyjście nieustannie pobiera próbki audio z ciągłego bufora pierścieniowego, nigdy się nie zatrzymując, więc słuchacz nigdy nie słyszy granicy. Przełączenie następuje między próbkami, i właśnie dlatego nie ma słyszalnej przerwy.

Działa to tak samo, niezależnie od tego, czy plik jest na Twoim urządzeniu, w chmurze czy na serwerze multimediów — wstępne buforowanie po prostu zaczyna się nieco wcześniej dla źródeł zdalnych.

## Studyjne efekty audio

Evermusic 8.7 dodaje pięć efektów audio działających w czasie rzeczywistym, które możesz nałożyć na swoją muzykę. Każdy z nich działa jako natywny węzeł przetwarzania audio w silniku odtwarzania, więc stosuje się do wszystkiego, co odtwarzasz — plików lokalnych, strumieni z chmury i radia internetowego — bez ponownego kodowania.

Każdy efekt jest dostarczany z **wyselekcjonowaną biblioteką presetów**, aby zapewnić świetne brzmienie jednym dotknięciem, a Evermusic **zapamiętuje Twoje dokładne ustawienia** między sesjami. Dostosuj dowolne sterowanie, a efekt przełącza się w stan **Ręczny**, więc zawsze wiesz, kiedy odszedłeś od presetu.

### Pogłos

Dodaje poczucie przestrzeni, od ciasnego pokoju po katedrę. Zbudowany na `AVAudioUnitReverb` firmy Apple, oferuje **13 presetów pomieszczeń** (Mały pokój, Średnia sala, Płyta, Katedra i inne) plus sterowanie **miksem wet/dry** od 0 do 100%, więc to Ty decydujesz, ile przestrzeni dodać.

### Opóźnienie (echo)

Klasyczne echo z **10 presetami** — Slapback, Echo taśmowe, Dub, Ambient i inne. Możesz ustawić **czas opóźnienia** (do 2 sekund), **sprzężenie zwrotne** (ile powtórzeń), **filtr dolnoprzepustowy** do ocieplenia powtórzeń oraz **miks wet/dry**.

### Przester

Od subtelnej chropowatości po pełne zniszczenie lo-fi, napędzany przez `AVAudioUnitDistortion` z **22 presetami charakterystycznymi** (Bit Brush, Cellphone Concert, Radio Tower i inne), sterowaniem napędem **wzmocnienia wstępnego** i miksem wet/dry, dzięki czemu możesz wmieszać efekt z powrotem w czysty sygnał.

### Kompresor

Procesor dynamiki (`AUDynamicsProcessor` firmy Apple), który wyrównuje głośne i ciche fragmenty. Udostępnia pełny profesjonalny zestaw sterowań — **próg, współczynnik/zapas, atak, zwolnienie, ekspansję i wzmocnienie wyrównawcze** — z **10 presetami** dostrojonymi do prawdziwych sytuacji: Głos / Podcast, Późna noc, Dialog filmowy, Dopasowanie do strumieniowania i Maksymalna głośność między innymi.

### Crossfeed

Crossfeed sprawia, że słuchanie w słuchawkach brzmi bardziej naturalnie, mieszając trochę lewego kanału z prawym i odwrotnie, tak jak Twoje uszy słyszą prawdziwe głośniki. Zbudowany jest na znanym algorytmie **Bauer stereophonic-to-binaural (bs2b)**, ze sterowaniem **poziomem crossfeedu** i **częstotliwością odcięcia** oraz **6 presetami**, w tym ulubionymi przez audiofilów ustawieniami *Chu Moy* i *Jan Meier*. Jest szczególnie dobry przy starszych, mocno rozpanoramowanych miksach stereo z lat 60. i 70.

## Normalizacja głośności

Zdarzyło Ci się kiedyś zbudować playlistę, w której jeden utwór grzmi, a następny to szept? Normalizacja głośności to naprawia. Evermusic 8.7 wykorzystuje **pomiar głośności EBU R128** (ten sam standard ITU-R BS.1770 używany w radiofonii i przez serwisy strumieniowe) do mierzenia rzeczywistej postrzeganej głośności każdego utworu i delikatnego kierowania jej do spójnego celu.

W przeciwieństwie do ReplayGain **nie** wymaga żadnych znaczników w plikach i **nie** modyfikuje Twojego dźwięku. Działa w czasie rzeczywistym na wszystkim, co odtwarzasz, w tym strumieniach z chmury i radiu na żywo, i resetuje się czysto, gdy przewijasz lub zmieniasz utwory.

Cztery presety pokrywają najczęstsze przypadki:

- **Lekki** — delikatne wyrównywanie (cel −20 LUFS).
- **Standardowy** — domyślny, głośność w stylu strumieniowania (cel −16 LUFS, do +12 dB podbicia dla cichych utworów).
- **Mocny** — agresywne dopasowanie dla bardzo mieszanych bibliotek (cel −14 LUFS).
- **Nocny** — cichszy i spójny do słuchania wieczorem przy niskiej głośności (cel −23 LUFS).

Nie musisz już sięgać po regulację głośności między utworami.

## Przeprojektowany korektor

**10-pasmowy korektor graficzny** Evermusic został w pełni przeprojektowany. Pasma pokrywają **od 32 Hz do 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), każde regulowane od **−12 dB do +12 dB** w drobnych krokach 0,1 dB, z **przedwzmacniaczem** od −24 dB do +24 dB, aby zapobiec przesterowaniu przy wzmacnianiu.

Co nowego w 8.7:

- **Nowe suwaki** — precyzyjne, responsywne sterowanie, które przyjmuje natywny wygląd systemowego suwaka iOS 26 i materiał **Liquid Glass**.
- **Szybsze, płynniejsze przełączanie presetów** — przeskakuj między presetami natychmiast, z przeprojektowanym poziomym paskiem presetów w orientacji pionowej i pionową kolumną presetów w poziomej.
- **Lepszy układ w orientacji poziomej i na iPad** — suwaki i wybór presetów układają się tak, by wykorzystać dodatkową szerokość zamiast tłoczyć się w kolumnie wielkości telefonu.
- **Własne presety** — twórz i zapisuj własne krzywe, zmieniaj ich kolejność oraz **importuj i eksportuj** presety jako pliki `.eqp`, aby przenosić je między urządzeniami lub udostępniać.

Korektor działa natywnie w silniku (`AVAudioUnitEQ`), więc stosuje się do każdego źródła, a także działa przez AirPlay, Chromecast i CarPlay tam, gdzie są obsługiwane.

## Przebudowany silnik odtwarzania

Od środka Evermusic 8.7 działa na **przebudowanym silniku strumieniowania** opartym na `AVAudioEngine` firmy Apple z niestandardowym potokiem renderowania. To właśnie umożliwia przełączanie bez przerw, łańcuch efektów i korektor, a także sprawia, że codzienne odtwarzanie jest bardziej niezawodne.

- **Ulepszona obsługa formatów** — w tym **FLAC** (przez Core Audio) i **Ogg Vorbis** (przez `libvorbisfile`), obok MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF i innych.
- **Inteligentniejsze buforowanie** — adaptacyjny bufor wstępny skaluje się z Twoim połączeniem, a ciągły bufor pierścieniowy zasila wyjście, aby krótkie zakłócenia sieci nie zamieniały się w przerwy.
- **Automatyczne odzyskiwanie** — maszyna stanów ponownego buforowania oraz logika ponawiania z odczekaniem czysto wznawiają odtwarzanie po chwili słabego sygnału, zamiast zatrzymywać utwór.
- **Mniej przerw** — ten sam silnik napędza pliki lokalne, strumienie z chmury, serwery multimediów i radio internetowe, więc zachowanie jest wszędzie spójne.

## Teraz odtwarzane i CarPlay

Ekrany, na które faktycznie patrzysz podczas słuchania — **ekran blokady**, **CarPlay** oraz przyciski pilota w samochodzie lub słuchawkach — są dokładniejsze i szybsze w 8.7.

- **Dokładniejsze informacje Teraz odtwarzane.** Evermusic przechwytuje stan odtwarzacza pod blokadą, zanim go opublikuje, więc tytuł, czas, który upłynął, czas trwania oraz stan odtwarzania/pauzy nigdy nie mogą być ze sobą sprzeczne na ekranie blokady czy w samochodzie. Stany buforowania i ładowania są teraz raportowane poprawnie, zamiast pokazywać „odtwarzanie", gdy utwór jest jeszcze pobierany.
- **Niezawodne sterowanie zdalne.** Odtwarzanie, pauza, następny, poprzedni, przewijanie, pomijanie, tryb losowy, powtarzanie i tempo odtwarzania reagują spójnie z przycisków słuchawek, sterowania w samochodzie i ekranu blokady, napędzane przez `MPRemoteCommandCenter`.
- **Szybsze okładki w CarPlay.** Okładki albumów ładują się teraz kilka razy szybciej na długich listach (tempo wsadowe skrócone z 1,0 s do 0,25 s, przy czym pierwszy widoczny ekran ładuje się natychmiast) i pojawiają się teraz w kompaktowych wierszach listy CarPlay iOS 26, które wcześniej nie pokazywały żadnej okładki.
- **Poprawki sortowania i stabilności CarPlay.** Szybsze sortowanie na dużych bibliotekach oraz zabezpieczenie przed awariami w przypadkach brzegowych podczas przewijania długich list.
- **Ograniczone aktualizacje metadanych.** Aktualizacje Teraz odtwarzane i poleceń zdalnych są ograniczane, aby szybkie zmiany nie zalewały systemu, co utrzymuje responsywność sterowania na ekranie blokady i w CarPlay.

## Inne ulepszenia

- **Udoskonalenia designu Liquid Glass** w całej aplikacji — półprzezroczyste powierzchnie, płynniejsze animacje i dopracowane sterowanie na iOS, iPadOS i macOS.
- **Nowe widżety na ekran główny** z ulepszoną logiką aktualizacji, która utrzymuje je w synchronizacji bez dodatkowego zużycia baterii.
- Poprawki dla najnowszych wydań iOS.
- Poprawki lokalizacji w wielu językach.
- Wiele mniejszych ulepszeń opartych na Waszych mailach i recenzjach w App Store.

## Dlaczego ta aktualizacja ma znaczenie

Evermusic 8.7 jest zbudowany wokół jednej idei: **Twoja muzyka powinna brzmieć jak najlepiej, z każdego źródła.**

1. **Całe albumy, tak jak zamierzono.** Prawdziwe odtwarzanie bez przerw sprawia, że sety koncertowe, miksy DJ i albumy koncepcyjne wreszcie grają tak, jak artysta je zmasterował.
2. **Studio w kieszeni.** Pogłos, opóźnienie, przester, kompresor, crossfeed, przeprojektowany korektor i normalizacja głośności dają Ci prawdziwą kontrolę nad brzmieniem, a nie tylko przełącznik włącz/wyłącz.
3. **To samo doświadczenie wszędzie.** Pliki lokalne, dyski w chmurze, serwery multimediów i radio internetowe działają przez ten sam przebudowany silnik, z dokładnym Teraz odtwarzane i szybszym CarPlay na dodatek.

## Pobierz Evermusic 8.7

[**Pobierz Evermusic z App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) lub zaktualizuj z poziomu App Store. Evermusic jest darmowy do pobrania z opcjonalnymi ulepszeniami w aplikacji dla zaawansowanych funkcji.

Jeśli podoba Ci się aplikacja, zostaw ocenę w App Store — to naprawdę pomaga. Masz opinię lub natknąłeś się na problem? Napisz do nas na **support@everappz.com**. Czytamy każdą wiadomość.

## Najczęściej zadawane pytania

{{% details title="Co nowego w Evermusic 8.7?" closed="true" %}}
Evermusic 8.7 dodaje prawdziwe odtwarzanie bez przerw, pięć studyjnych efektów audio (pogłos, opóźnienie, przester, kompresor i crossfeed), normalizację głośności EBU R128, przeprojektowany 10-pasmowy korektor z własnymi presetami oraz importem/eksportem, przebudowany silnik strumieniowania AVAudioEngine z ulepszoną obsługą formatów (w tym FLAC i Ogg Vorbis), szybsze i dokładniejsze CarPlay oraz Teraz odtwarzane, aktualizacje designu Liquid Glass, odświeżone widżety na ekran główny oraz poprawki błędów i lokalizacji.
{{% /details %}}

{{% details title="Czy Evermusic ma prawdziwe odtwarzanie bez przerw?" closed="true" %}}
Tak. Począwszy od Evermusic 8.7 odtwarzanie jest naprawdę bez przerw: nie ma pauzy, kliknięcia ani trzasku między utworami. Silnik wstępnie buforuje i dekoduje następny utwór, gdy bieżący gra, i przełącza się między próbkami audio na ciągłym buforze pierścieniowym, więc przejście jest niesłyszalne. Działa z plikami lokalnymi, strumieniami z chmury i serwerami multimediów i jest idealne do albumów koncertowych, miksów DJ i albumów koncepcyjnych.
{{% /details %}}

{{% details title="Jakie efekty audio zawiera Evermusic 8.7?" closed="true" %}}
Pięć efektów działających w czasie rzeczywistym: **pogłos** (13 presetów pomieszczeń, miks wet/dry), **opóźnienie/echo** (10 presetów z czasem opóźnienia, sprzężeniem zwrotnym, filtrem dolnoprzepustowym i miksem), **przester** (22 presety charakterystyczne z wzmocnieniem wstępnym i miksem), **kompresor** (pełny procesor dynamiki z progiem, współczynnikiem, atakiem, zwolnieniem, ekspansją i wzmocnieniem wyrównawczym plus 10 presetów) oraz **crossfeed** (crossfeed słuchawkowy Bauer bs2b ze sterowaniem poziomem i częstotliwością odcięcia oraz 6 presetami). Każdy efekt jest dostarczany z wyselekcjonowanymi presetami, a Twoje własne ustawienia są zapamiętywane między sesjami.
{{% /details %}}

{{% details title="Czym jest crossfeed i dlaczego miałbym go używać?" closed="true" %}}
Crossfeed miesza niewielką, przefiltrowaną część każdego kanału stereo z drugim, tak jak Twoje uszy naturalnie słyszą prawdziwe głośniki w pomieszczeniu. W słuchawkach redukuje to przesadną separację „w głowie" mocno rozpanoramowanych nagrań i sprawia, że długie słuchanie jest wygodniejsze. Evermusic wykorzystuje znany algorytm Bauer stereophonic-to-binaural (bs2b) i zawiera presety takie jak Chu Moy i Jan Meier. Jest szczególnie skuteczny przy starszych miksach stereo z lat 60. i 70.
{{% /details %}}

{{% details title="Jak działa normalizacja głośności w Evermusic?" closed="true" %}}
Evermusic 8.7 mierzy postrzeganą głośność każdego utworu za pomocą standardu EBU R128 (ITU-R BS.1770) w czasie rzeczywistym i delikatnie dostosowuje poziom do spójnego celu, aby utwory nie skakały w głośności. Nie wymaga znaczników ReplayGain i nie zmienia Twoich plików. Dostępne są cztery presety — Lekki (−20 LUFS), Standardowy (−16 LUFS), Mocny (−14 LUFS) i Nocny (−23 LUFS) — a normalizacja resetuje się czysto, gdy przewijasz lub zmieniasz utwory.
{{% /details %}}

{{% details title="Czy normalizacja głośności w Evermusic to to samo co ReplayGain?" closed="true" %}}
Osiąga ten sam cel — spójną głośność między utworami — ale działa inaczej. ReplayGain polega na znacznikach głośności zapisanych w plikach. Normalizator Evermusic mierzy głośność na żywo za pomocą EBU R128, więc działa na dowolnym źródle, w tym strumieniach z chmury i radiu internetowym, nawet gdy pliki w ogóle nie mają znaczników.
{{% /details %}}

{{% details title="Ile pasm ma korektor Evermusic i czy mogę tworzyć własne presety?" closed="true" %}}
Korektor Evermusic to 10-pasmowy korektor graficzny pokrywający od 32 Hz do 16 kHz, z każdym pasmem regulowanym od −12 dB do +12 dB w krokach 0,1 dB i przedwzmacniaczem od −24 dB do +24 dB. Zawiera wbudowane presety, pozwala tworzyć i zapisywać własne presety oraz obsługuje importowanie i eksportowanie presetów jako plików .eqp, dzięki czemu możesz je przenosić lub udostępniać między urządzeniami.
{{% /details %}}

{{% details title="Co się zmieniło w korektorze Evermusic 8.7?" closed="true" %}}
Korektor został przeprojektowany z nowymi, bardziej precyzyjnymi suwakami, które przyjmują wygląd systemowego suwaka iOS 26 i Liquid Glass, szybszym i płynniejszym przełączaniem presetów oraz lepszym układem w orientacji poziomej i na iPad (poziomy pasek presetów w orientacji pionowej i pionowa kolumna presetów w poziomej). Obsługiwane są własne presety oraz import/eksport .eqp.
{{% /details %}}

{{% details title="Czy Evermusic 8.7 obsługuje FLAC i Ogg Vorbis?" closed="true" %}}
Tak. Przebudowany silnik odtwarza FLAC (przez Core Audio) i Ogg Vorbis (przez libvorbisfile), wraz z MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF i innymi, z plików lokalnych, dysków w chmurze i serwerów multimediów.
{{% /details %}}

{{% details title="Co poprawiono w CarPlay i na ekranie blokady?" closed="true" %}}
Okładki albumów CarPlay ładują się kilka razy szybciej na długich listach i pojawiają się teraz w kompaktowych wierszach listy iOS 26, które wcześniej ich nie pokazywały. Informacje Teraz odtwarzane na ekranie blokady i w CarPlay są dokładniejsze — tytuł, czas, który upłynął, czas trwania oraz stan odtwarzania/pauzy są przechwytywane razem, więc nie mogą być sprzeczne, a stany buforowania są raportowane poprawnie. Sterowanie zdalne (odtwarzanie, pauza, następny, poprzedni, przewijanie, tryb losowy, powtarzanie, tempo) reaguje niezawodnie ze słuchawek i z samochodu, a sortowanie CarPlay na dużych bibliotekach jest szybsze.
{{% /details %}}

{{% details title="Czy efekty audio i korektor działają ze strumieniowaniem z chmury i CarPlay?" closed="true" %}}
Tak. Efekty, korektor i normalizacja głośności działają natywnie wewnątrz silnika odtwarzania, więc stosują się do wszystkiego, co Evermusic odtwarza — plików lokalnych, dysków w chmurze, serwerów multimediów i radia internetowego — i działają dalej podczas odtwarzania przez CarPlay oraz, tam gdzie jest to obsługiwane, przez AirPlay i Chromecast.
{{% /details %}}

{{% details title="Czy aktualizacja Evermusic 8.7 jest darmowa i które urządzenia obsługuje?" closed="true" %}}
Tak. Evermusic jest darmowy do pobrania z App Store, a 8.7 to darmowa aktualizacja dla istniejących użytkowników, z opcjonalnymi ulepszeniami w aplikacji dla zaawansowanych funkcji. Działa na iPhone, iPad i Mac. CarPlay wymaga pojazdu lub zestawu głównego zgodnego z CarPlay.
{{% /details %}}
