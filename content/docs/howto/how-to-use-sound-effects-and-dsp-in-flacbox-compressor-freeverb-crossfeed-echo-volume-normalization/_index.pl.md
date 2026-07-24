---
title: "Jak korzystać z efektów dźwiękowych i DSP w Flacbox: Kompresor, Freeverb, Crossfeed, Echo, Normalizacja głośności i więcej"
date: 2026-07-24
description: "Kompletny przewodnik po dźwięku w Flacbox na iPhone, iPad i Mac. Dowiedz się, jak działa silnik BASS, jakie dodatkowe formaty odtwarza (w tym muzykę MOD i trackerową oraz DSD) i dokładnie co robi każdy efekt, każdy suwak i każdy preset z Twoim dźwiękiem, plus 10-pasmowy korektor i własny łańcuch DSP."
keywords: ["efekty dźwiękowe Flacbox", "presety Flacbox wyjaśnione", "silnik BASS Flacbox", "biblioteka audio BASS iOS", "odtwarzacz muzyki MOD iPhone", "odtwarzacz muzyki trackerowej iOS", "odtwarzanie MOD XM IT S3M iPhone", "odtwarzacz DSD iOS", "odtwarzacz FLAC iPhone", "bezstratny odtwarzacz muzyki iOS", "presety korektora Flacbox", "10-pasmowy korektor iPhone", "normalizacja głośności iPhone", "EBU R128 iOS", "normalizacja głośności odtwarzacz muzyki", "crossfeed słuchawki iOS", "bs2b crossfeed", "presety kompresora odtwarzacz muzyki", "pogłos freeverb iOS", "echo opóźnienie odtwarzacz muzyki", "łańcuch DSP odtwarzacz muzyki", "podbicie basów iPhone", "jak dodać efekty do muzyki Flacbox", "najlepsze ustawienia korektora iPhone"]
tags: ["Flacbox", "Efekty dźwiękowe", "Poradnik", "BASS", "Korektor", "Podbicie basów", "Kompresor", "Freeverb", "Crossfeed", "Echo", "Normalizacja głośności", "EBU R128", "Muzyka MOD", "Muzyka trackerowa", "DSD", "FLAC", "DSP", "Słuchawki", "Presety"]
readingTime: 30
---

{{< author-byline >}}

{{< full-width-tables >}}

**Krótka odpowiedź:** W Flacbox wybierasz jeden **Silnik odtwarzania** w **Ustawienia > Odtwarzacz audio**: **Standard** (systemowy silnik Apple), **Universal** (silnik FFmpeg) lub **Sound FX** (**silnik BASS™**). Wybrany silnik decyduje, które formaty plików się odtwarzają, więc wybór ma znaczenie. Silnik **Sound FX** odtwarza dodatkowe formaty, które większość aplikacji na iPhone pomija (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus oraz starą **muzykę MOD i trackerową** jak MOD, XM, IT i S3M) i jest jedynym silnikiem, który zasila narzędzia dźwiękowe: **10-pasmowy korektor**, **Normalizację głośności**, **Kompresor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed** oraz własny **łańcuch DSP**. Aby więc korzystać z efektów w tym przewodniku, najpierw ustaw silnik odtwarzania na **Sound FX**. Każde narzędzie ma gotowe **presety**. Otwórz je w **Ustawienia > Odtwarzacz audio** (Efekty audio, Korektor audio, Przetwarzanie sygnału) lub dotknij przycisku **⋯ (Więcej)** na odtwarzaczu i wybierz **Efekty audio**. Nic, co tu robisz, nigdy nie zmienia Twoich plików.

> Wyjaśnienia suwaków i presetów poniżej to te same krótkie opisy, które Flacbox pokazuje Ci wewnątrz aplikacji, wzbogacone o odrobinę dodatkowego tła, abyś miał pełny obraz, zanim dotkniesz.

## Jak czytać ten przewodnik

Każde narzędzie działa tak samo:

1. **Włącz je.** Każdy efekt ma własny przełącznik włącz/wyłącz. Wszystkie są początkowo wyłączone. Możesz włączyć jednocześnie tyle, ile chcesz.
2. **Wybierz preset.** Preset to gotowe ustawienie. Dotknij go, a dźwięk zmieni się od razu. Ten przewodnik wymienia, co robi **każdy** preset.
3. **Dostrój (opcjonalnie).** Otwórz suwaki, aby regulować ręcznie. W momencie, gdy poruszysz suwak, efekt pokazuje **Ręczny**, więc wiesz, że opuściłeś preset. Każdy suwak ma przycisk resetowania.

Nic nie jest zapisywane w Twoich plikach. To są efekty na żywo. Wyłącz efekt, a Twój oryginalny dźwięk natychmiast wraca.

## Wybierz swój silnik odtwarzania (Sound FX ma efekty)

Flacbox nie miesza silników ze sobą. Wybierasz **jeden** w **Ustawienia > Odtwarzacz audio > Silnik odtwarzania**, a wybrany silnik decyduje, które formaty plików możesz odtwarzać i czy efekty są dostępne. Są trzy opcje, pokazane w aplikacji pod tymi dokładnymi nazwami:

1. **Standard.** Wbudowany silnik systemowy Apple. Używa dekodowania sprzętowego dla mniejszego zużycia baterii.
2. **Universal.** Silnik FFmpeg, który otwiera bardzo szeroki zakres formatów.
3. **Sound FX.** **Silnik BASS™**. Odtwarza pliki bezstratne i wysokiej rozdzielczości z pełną dokładnością, dodaje muzykę modułową (trackerową) i zasila każdy efekt, 10-pasmowy korektor oraz łańcuch DSP w tym przewodniku.

Ponieważ każdy silnik obsługuje własny zestaw formatów, pliki, które możesz odtwarzać, zmieniają się wraz z wybranym silnikiem. Co ważniejsze, efekty, korektor i łańcuch DSP działają **tylko** z silnikiem **Sound FX**, więc wybierz go najpierw, jeśli chcesz z nich korzystać.

Sound FX jest zbudowany na **BASS™**, profesjonalnej bibliotece audio od Un4seen Developments. Możesz przeczytać o niej więcej na jej stronie głównej pod adresem [un4seen.com](https://www.un4seen.com/).

## Formaty muzyki: co dodaje silnik Sound FX (BASS™) (w tym muzyka MOD i trackerowa)

Z wybranym silnikiem **Sound FX (BASS™)** Flacbox odtwarza poniższe specjalistyczne formaty, oprócz tych codziennych. Najbardziej wyjątkowa jest **muzyka modułowa**, nazywana także **muzyką trackerową**. Plik modułowy nie jest normalnym nagraniem. Zawiera małe brzmienia instrumentów plus „partyturę”, która mówi, jak je odtwarzać, a Flacbox odbudowuje utwór na żywo z tej partytury, w sposób, w jaki te pliki miały być odtwarzane. Normalne odtwarzacze nie potrafią tego zrobić.

| Rodzaj muzyki | Formaty | Warto wiedzieć |
|---|---|---|
| **Muzyka modułowa / trackerowa** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Odbudowywana na żywo przez odtwarzacz modułów BASS™. Świetna do chiptune'ów oraz starych utworów demosceny lub Amigi. |
| **Nowoczesna bezstratna** | FLAC | Pełna jakość, mniejszy niż WAV. |
| **Inna bezstratna** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Mniej popularne typy bezstratne, wszystkie obsługiwane. |
| **DSD wysokiej rozdzielczości** | DSF, DFF | Odtwarzane na normalnym sprzęcie z użyciem DSD over PCM. |
| **Nowoczesna stratna** | Opus, Ogg Vorbis, MP3 | Zwykłe typy do strumieniowania i pobierania. |

Silnik Sound FX odtwarza również popularne formaty Apple (AAC, ALAC, M4A, WAV, AIFF) oraz transmisje na żywo, więc efekty i korektor działają także na nich.

**Dlaczego to Ci pomaga:** jeśli masz mieszankę albumów FLAC, plików DSD wysokiej rozdzielczości i folder starych utworów trackerowych MOD lub XM, Flacbox odtwarza je wszystkie, a korektor i efekty działają na każdym z nich.

## Trzy menu, których będziesz używać

Flacbox trzyma swoje narzędzia dźwiękowe w trzech miejscach, wszystkie wewnątrz ustawień odtwarzacza audio. Najpierw upewnij się, że Twój **Silnik odtwarzania** jest ustawiony na **Sound FX** (Ustawienia > Odtwarzacz audio > Silnik odtwarzania), ponieważ efekty, korektor i łańcuch DSP są dostępne tylko z tym silnikiem.

- **Efekty audio** (zestaw efektów): otwórz odtwarzacz, dotknij **⋯ (Więcej)**, dotknij **Efekty audio**. Lub przejdź do **Ustawienia > Odtwarzacz audio > Efekty audio**.
- **Korektor audio** (10 pasm i presety): **Ustawienia > Odtwarzacz audio > Korektor audio**.
- **Przetwarzanie sygnału** (Twój własny łańcuch DSP): **Ustawienia > Odtwarzacz audio > Przetwarzanie sygnału**.

Możesz również ustawić **wyjściową częstotliwość próbkowania**, **kanały** i **rozmiar bufora** w **Ustawienia > Odtwarzacz audio**.

## 10-pasmowy korektor

**Co robi:** Zmienia barwę muzyki, od głębokiego basu po jasne soprany. To najlepsze narzędzie do czystego **podbicia basów** lub jaśniejszego, wyraźniejszego górnego zakresu. Pomyśl o nim jak o dziesięciu gałkach głośności, każda dla innego wycinka dźwięku. Podnieś pasmo, aby wysunąć tę część do przodu, obniż je, aby ją cofnąć. Małe zmiany o kilka dB zwykle brzmią najlepiej, i działa to na wszystkim, co odtwarzasz.

**Jak działa:** Dziesięć suwaków przy **32, 64, 125, 250, 500 Hz oraz 1, 2, 4, 8, 16 kHz**. Każdy sięga od **-12 dB (cięcie)** do **+12 dB (podbicie)**. Jest też **Przedwzmacniacz** od **-24 do +24 dB** dla ogólnego poziomu. Możesz zapisywać własne presety oraz **eksportować lub importować** je między urządzeniami.

**Co robi każdy wbudowany preset (22 presety):**

| Preset | Co robi z Twoim dźwiękiem |
|---|---|
| **Flat** | Bez zmian. Wszystkie pasma na zerze. Czysty punkt wyjścia. |
| **Acoustic** | Ciepły bas i wyraziste, obecne soprany. Sprawia, że gitary akustyczne i głosy brzmią naturalnie i żywo. |
| **Bass Booster** | Mocne podniesienie dolnego zakresu, średnie i wysokie nietknięte. Więcej uderzenia i ciężaru. |
| **Bass Reducer** | Tnie dolny zakres. Przydatny w dudniących pomieszczeniach, tanich słuchawkach dousznych lub ciężkich utworach. |
| **Treble Booster** | Podnosi tylko soprany. Dodaje blasku i powietrza, więcej szczegółów. |
| **Treble Reducer** | Zmiękcza soprany. Poskramia ostre lub kłujące nagrania. |
| **Classical** | Pełny dół i łagodne soprany z lekkim obniżeniem średnicy. Gładki i przestrzenny dla muzyki orkiestrowej. |
| **Dance** | Duży dół i jasne soprany z wyciętą średnicą. Uderzeniowy i energetyczny dla utworów klubowych. |
| **Deep** | Ciepły, gruby dolny zakres z łagodniejszymi sopranami. Przytulne, wyluzowane brzmienie. |
| **Electronic** | Mocny bas i jasne soprany dla syntezatorów i bitów. Szerokie i nowoczesne. |
| **Hip-Hop** | Ciężki bas i wyraźne soprany z kontrolowaną średnicą. Ciężkie i uderzeniowe. |
| **Jazz** | Ciepłe i gładkie, z niewielkim obniżeniem średnicy. Łatwe i naturalne dla akustycznego jazzu. |
| **Latin** | Podbite dół i góra z czystą średnicą. Jasne i żywe. |
| **Loudness** | Mocno podbija bas i soprany (krzywa „uśmiechu”). Brzmi pełniej przy niskiej głośności. |
| **Lounge** | Wysunięta średnica z miękkimi krawędziami. Zrelaksowane i przyjazne wokalom. |
| **Piano** | Wyraźna średnica i soprany, aby nuty fortepianu wybrzmiewały czysto. |
| **Pop** | Podniesiona średnica dla wokali, z cofniętym dołem i górą. Głosy stoją z przodu. |
| **R&B** | Bardzo mocne ciepło dolnej średnicy i wyraźne soprany. Gładkie i bogate. |
| **Rock** | Podbite dół i góra dla gitar i perkusji. Energetyczne i pełne. |
| **Small Speakers** | Podbija dół i tnie górę, aby pomóc małym głośnikom brzmieć pełniej. |
| **Spoken Word** | Podnosi zakres głosu i tnie głęboki bas. Sprawia, że mowa jest wyraźna. |
| **Vocal Booster** | Wypycha środek, gdzie żyją głosy, tnie wokół nich. Wokale się wyróżniają. |

**Wskazówka dla basów:** Zacznij od **Bass Booster**, a następnie, jeśli brzmi mętnie, ściągnij Przedwzmacniacz o 1 do 2 dB, aby nic się nie zniekształcało.

## Normalizacja głośności (równa głośność)

**Co robi:** Niektóre utwory grają głośniej niż inne, więc ciągle zmieniasz głośność. To sprawia, że każdy utwór gra na mniej więcej tej samej głośności sam z siebie, więc nie musisz tego robić. Idealne do losowych playlist mieszających stare i nowe nagrania, różne albumy lub różne źródła, gdzie jeden utwór może być znacznie głośniejszy od następnego.

**Jak działa:** Nasłuchuje rzeczywistej głośności każdego utworu przy użyciu standardu **EBU R128** (mierzonej w **LUFS**, tej samej idei, której używają serwisy streamingowe), a następnie dostosowuje każdy utwór w kierunku Twojego celu. Nie potrzebuje żadnych tagów w plikach i nigdy nie zmienia dźwięku. EBU R128 mierzy głośność, którą Twoje uszy faktycznie odczuwają w całym utworze, a nie tylko najwyższy szczyt, dlatego odpowiada temu, jak głośno utwory naprawdę Ci się wydają. Flacbox oblicza to na żywo, gdy muzyka gra (i sprawdza głośność z wyprzedzeniem, gdy może), a następnie stosuje pojedynczą, stałą zmianę głośności do utworu. Limit **Maksymalne podbicie** powstrzymuje bardzo ciche nagrania przed wypchnięciem tak mocno, że się zniekształcą. Ponieważ odczytuje sam dźwięk, działa na dowolnym źródle, w tym plikach w chmurze, transmisjach na żywo i muzyce modułowej, nawet gdy pliki w ogóle nie mają tagów głośności.

**Suwaki:**

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Docelowa głośność** | Ustawia głośność, do której wyrównywany jest każdy utwór. Wyższe wartości sprawiają, że wszystko gra ogólnie głośniej. | -30 do -6 LUFS (-16) |
| **Maksymalne podbicie** | Ogranicza, o ile ciche utwory mogą zostać wzmocnione. Wyższe wartości przybliżają ciche nagrania do celu. | 0 do 24 dB (12) |

**Presety:**

| Preset | Co robi |
|---|---|
| **Light** | Delikatne wyrównanie do swobodnego słuchania. Wyrównuje oczywiste skoki głośności bez mocnego wypychania cichych utworów. |
| **Standard** | Uniwersalne ustawienie domyślne. Cel głośności w stylu streamingu, który pasuje do większości muzyki. Zacznij tutaj. |
| **Strong** | Agresywne dopasowanie, które zdecydowanie wypycha ciche utwory w górę. Najlepsze do mieszanych bibliotek z dużymi różnicami poziomu. |
| **Night** | Cichszy ogólny cel, który wciąż podnosi ciche fragmenty, aby nocne słuchanie pozostało spójne i ciche. |

## Kompresor (wyrównaj głośne i ciche fragmenty)

**Co robi:** W jednym utworze ciche fragmenty mogą być zbyt ciche, a głośne zbyt głośne. To zbliża je do siebie, więc cały utwór jest łatwy do usłyszenia, nawet w samochodzie lub głośnym miejscu. Delikatnie ścisza najgłośniejsze momenty i podnosi cichsze, więc przestajesz sięgać po głośność podczas jednego utworu. To różni się od Normalizacji głośności: Kompresor wyrównuje rzeczy **wewnątrz** jednego utworu, podczas gdy Normalizacja głośności dopasowuje głośność **między** utworami. Oba dobrze ze sobą współpracują. Zacznij od presetu i otwieraj suwaki tylko, jeśli chcesz większej kontroli.

**Suwaki:**

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Próg** | Poziom, przy którym rozpoczyna się kompresja. Niższe wartości ściskają więcej dźwięku, utrzymując ciche i głośne fragmenty bliżej siebie. | -60 do 0 dB (-20) |
| **Współczynnik** | Jak mocno głośne fragmenty są wstrzymywane, gdy przekroczą próg. Wyższe wartości kompresują mocniej, utrzymując dźwięk bardziej równym. | 1:1 do 30:1 (4:1) |
| **Atak** | Jak szybko efekt reaguje na nagły głośny szczyt. Krótkie wartości łapią transjenty; dłuższe je przepuszczają. | 0.1 do 1000 ms (10 ms) |
| **Zwolnienie** | Jak szybko efekt puszcza po tym, jak minie głośny fragment. Krótkie wartości mogą pompować; dłuższe brzmią gładziej. | 10 ms do 5 s (100 ms) |
| **Wzmocnienie główne** | Końcowe podbicie wyjścia stosowane po przetwarzaniu. Podnieś je, aby zwiększyć ogólną głośność po wyrównaniu dynamiki. | -30 do +30 dB (0) |

**Presety:**

| Preset | Co robi |
|---|---|
| **Transparent** | Ledwie obecna siatka bezpieczeństwa. Zachowuje dynamikę niemal w całości i łapie tylko najgłośniejsze szczyty. |
| **Soft** | Lekkie wyrównanie do słuchania hi-fi w domu. Subtelne wygładzenie bez ściskania muzyki. |
| **Standard** | Rozsądne ustawienie domyślne do codziennego odtwarzania muzyki. Pierwszy preset do wypróbowania. |
| **Heavy** | Agresywne wyrównanie do głośnych otoczeń. Samochód, zatłoczone pomieszczenie, słuchanie na niskiej głośności. |
| **Voice / Podcast** | Dostrojony do mowy. Wolniejszy atak przepuszcza syczące dźwięki, hojne wzmocnienie makijażowe podnosi wokale. |
| **Old Recordings** | Zabytkowe albumy i odrestaurowany winyl, gdzie średni poziom jest poniżej nowoczesnych wydań. |
| **Late Night** | Ciężka kompresja plus duże podbicie do cichego słuchania, gdy sąsiedzi lub śpiąca rodzina mają znaczenie. |
| **Movie Dialog** | Podnosi mowę względem muzyki i efektów dźwiękowych w zróżnicowanej ścieżce dźwiękowej. |
| **Streaming Match** | Celuje w przybliżeniu w normalizację głośności nowoczesnych serwisów streamingowych, około -14 LUFS. |
| **Maximum Loudness** | Na maksa. Uderza w limiter; spodziewaj się ściśniętego, bardzo równego sygnału. Dosłownie preset maksymalnej głośności. |

## Freeverb (pogłos, poczucie przestrzeni)

**Co robi:** Dodaje poczucie przestrzeni do muzyki, od małego pokoju po dużą salę. Wybierz preset lub sam dostrój miks suchy i mokry, rozmiar pomieszczenia, tłumienie i szerokość. Pogłos to naturalne echo, które słyszysz w każdej rzeczywistej przestrzeni, a Freeverb odtwarza je programowo. Odrobina sprawia, że płaskie lub nagrywane z bliska nagrania stają się bardziej otwarte i żywe. Dużo umieszcza muzykę w dużej, odległej przestrzeni. To efekt kreatywny, więc utrzymuj miks mokry skromny dla naturalnych rezultatów.

**Suwaki:**

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Miks suchy** | Ile oryginalnego, nietkniętego dźwięku jest zachowywane. Wyższe wartości pozostawiają więcej suchego sygnału w miksie. | 0 do 1 (0.0) |
| **Miks mokry** | Ile dodawanego jest dźwięku z pogłosem. Wyższe wartości sprawiają, że pogłos jest głośniejszy i bardziej oczywisty. | 0 do 3 (1.0) |
| **Rozmiar pomieszczenia** | Rozmiar wyobrażonej przestrzeni. Wyższe wartości dają dłuższy, większy ogon pogłosu, od małego pokoju po katedrę. | 0 do 1 (0.5) |
| **Tłumienie** | Jak szybko wysokie częstotliwości zanikają w ogonie. Wyższe wartości sprawiają, że pogłos jest ciemniejszy i cieplejszy. | 0 do 1 (0.5) |
| **Szerokość** | Rozpiętość stereo pogłosu. Wyższe wartości sprawiają, że przestrzeń wydaje się szersza między kanałem lewym a prawym. | 0 do 1 (1.0) |

**Presety:**

| Preset | Co robi |
|---|---|
| **Room** | Mała, ciasna przestrzeń. Subtelna atmosfera, która dodaje poczucie miejsca bez zamywania dźwięku. |
| **Studio** | Suche, kontrolowane pomieszczenie nagraniowe. Akurat tyle odbicia, aby brzmiało naturalnie. |
| **Hall** | Duża sala koncertowa. Długi, bujny ogon pasujący do muzyki orkiestrowej i akustycznej. |
| **Cathedral** | Ogromna, echowa kamienna przestrzeń. Najdłuższy, najbardziej dramatyczny ogon pogłosu. |
| **Plate** | Jasny, gęsty studyjny pogłos płytowy. Klasyczny dla wokali i perkusji. |
| **Ambience** | Krótka, przewiewna atmosfera. Dodaje lekkie poczucie przestrzeni, pozostając głównie suchym. |

## Auto Wah (funkowy przemiatający filtr)

**Co robi:** Filtr, który sam przemiata w górę i w dół, dla funkowego, wokalnego brzmienia wah. Wybierz preset lub sam ustaw miks mokry, sprzężenie, tempo, zakres i częstotliwość. To ten sam przemiatający dźwięk „wah”, który wydaje gitarowy pedał wah, ale tutaj porusza się sam w rytm muzyki. Świetnie brzmi na utworach funkowych, disco i elektronicznych. To śmiały, oczywisty efekt, więc odrobina wystarcza na długo przy codziennym słuchaniu.

**Suwaki:**

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Miks mokry** | Jak silny jest efekt wah w miksie. Wyższe wartości sprawiają, że przemiatający filtr jest bardziej oczywisty. | -2 do +2 (1.5) |
| **Sprzężenie** | Ile wyjścia jest podawane z powrotem do efektu. Wyższe wartości sprawiają, że wah jest bardziej rezonansowy i wyrazisty. | -1 do +1 (0.5) |
| **Tempo** | Jak szybko filtr przemiata w górę i w dół. Wyższe wartości dają szybsze, bardziej rytmiczne wah. | 0.1 do 9 Hz (2.0) |
| **Zakres** | Jak daleko filtr przemiata, w oktawach. Wyższe wartości dają szersze, bardziej dramatyczne przemiatanie. | 0.1 do 9 oktaw (4.3) |
| **Częstotliwość** | Bazowa częstotliwość, wokół której filtr przemiata. Niższe wartości brzmią głębiej; wyższe brzmią jaśniej. | 1 do 1000 Hz (50) |

**Presety:**

| Preset | Co robi |
|---|---|
| **Classic** | Zrównoważone, klasyczne przemiatanie wah. Dobry punkt wyjścia dla funku i rocka. |
| **Slow** | Wolne, szerokie przemiatanie, które delikatnie dryfuje w górę i w dół. Świetne do padów i długich nut. |
| **Funky** | Szybkie, uderzeniowe przemiatanie z mnóstwem ruchu. Dodaje rytmicznego zgryzu gitarom i syntezatorom. |
| **Deep** | Głębokie, szerokie przemiatanie zaczynające się od niskiej częstotliwości. Duże i dramatyczne. |
| **Subtle** | Delikatny, powściągliwy ruch. Dodaje charakteru bez dominowania nad dźwiękiem. |
| **Resonant** | Ostre, rezonansowe wah z wysokim sprzężeniem. Wokalne i ekspresyjne. |

## Phaser (wirujący świst)

**Co robi:** Przemiatający filtr, który dodaje wirujący, świszczący ruch do dźwięku. Wybierz preset lub sam ustaw sprzężenie, tempo, zakres i częstotliwość. Dodaje delikatny ruch i migotanie bez zmiany nut. Jest subtelny na wokalach i padach, a dramatyczny na syntezatorach i gitarach. Wypróbuj Slow dla marzycielskiego klimatu lub Jet dla mocnego wirowania.

**Suwaki:**

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Sprzężenie** | Ile wyjścia jest podawane z powrotem do efektu. Wyższe wartości sprawiają, że phaser jest bardziej rezonansowy i wyrazisty. | -1 do +1 (0.0) |
| **Tempo** | Jak szybko filtr przemiata w górę i w dół. Wyższe wartości dają szybsze, bardziej rytmiczne fazowanie. | 0.1 do 9 Hz (1.0) |
| **Zakres** | Jak daleko filtr przemiata, w oktawach. Wyższe wartości dają szersze, bardziej dramatyczne przemiatanie. | 0.1 do 9 oktaw (4.0) |
| **Częstotliwość** | Bazowa częstotliwość, wokół której filtr przemiata. Niższe wartości brzmią głębiej; wyższe brzmią jaśniej. | 1 do 1000 Hz (100) |

**Presety:**

| Preset | Co robi |
|---|---|
| **Classic** | Zrównoważone, klasyczne przemiatanie phasera. Dobry punkt wyjścia dla gitar i klawiszy. |
| **Slow** | Wolne, szerokie przemiatanie, które delikatnie dryfuje w górę i w dół. Świetne do padów i długich nut. |
| **Fast** | Szybkie, migoczące przemiatanie z mnóstwem ruchu. Dodaje ruchu i energii. |
| **Deep** | Głębokie, szerokie przemiatanie zaczynające się od niskiej częstotliwości. Duże i dramatyczne. |
| **Subtle** | Delikatny, powściągliwy ruch. Dodaje charakteru bez dominowania nad dźwiękiem. |
| **Jet** | Intensywne, rezonansowe przemiatanie z wysokim sprzężeniem, klasyczny świst odrzutowca. |

## Flanger (przemiatanie odrzutowca)

**Co robi:** Krótkie, poruszające się opóźnienie, które nadaje dźwiękowi odrzutowy, przemiatający świst. Wybierz preset lub sam ustaw głębię, sprzężenie, tempo i opóźnienie. To silniejszy, bardziej metaliczny kuzyn phasera, słynny z przemiatającego świstu w klasycznym rocku i muzyce elektronicznej. Subtelne ustawienia dodają delikatnego ruchu, podczas gdy głębokie ustawienia są dramatyczne i oczywiste. Najlepiej używać oszczędnie, dla efektu.

**Suwaki:**

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Głębia** | Jak silny jest efekt przemiatania. Wyższe wartości sprawiają, że flangowanie jest bardziej oczywiste. | 0 do 100% (25) |
| **Sprzężenie** | Ile wyjścia jest podawane z powrotem do efektu. Wyższe wartości sprawiają, że flanger jest bardziej rezonansowy i metaliczny. | -99 do +99% (-50) |
| **Tempo** | Jak szybko przemiatanie porusza się w górę i w dół. Wyższe wartości dają szybszy, bardziej migoczący ruch. | 0 do 10 Hz (0.25) |
| **Opóźnienie** | Bazowy czas opóźnienia, na którym budowane jest przemiatanie. Wyższe wartości dają głębszy, bardziej pusty charakter. | 0 do 4 ms (2.0) |

**Presety:**

| Preset | Co robi |
|---|---|
| **Classic** | Zrównoważony, klasyczny flanger. Dobry punkt wyjścia dla gitar i klawiszy. |
| **Subtle** | Delikatne, powściągliwe przemiatanie. Dodaje ruchu bez dominowania nad dźwiękiem. |
| **Deep** | Głębokie, ciężkie przemiatanie z mocnym sprzężeniem. Duże i dramatyczne. |
| **Jet** | Intensywne przemiatanie z dodatnim sprzężeniem, klasyczny świst odrzutowca. |
| **Fast** | Szybkie, migoczące przemiatanie z mnóstwem ruchu i energii. |
| **Wide** | Wolne, szerokie przemiatanie z długim opóźnieniem. Bujne i przestronne. |

## Echo (powtórzenia)

**Co robi:** Powtarza dźwięk jako zanikające echa dla poczucia przestrzeni i głębi. Wybierz preset lub sam ustaw miks mokry, sprzężenie i opóźnienie. To jak wołanie w kanionie: dźwięk wraca raz lub więcej razy po krótkiej przerwie. Pojedyncze krótkie powtórzenie dodaje ciała i retro klimatu, podczas gdy dłuższe powtórzenia z większym sprzężeniem tworzą przestronne, ciągnące się ogony. Preset Ping Pong odbija powtórzenia między lewym a prawym uchem, co jest zabawne na słuchawkach. Utrzymuj miks mokry skromny, aby echa wspierały muzykę, a nie ją zakrywały.

**Suwaki:**

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Miks mokry** | Jak głośne są echa w porównaniu z oryginalnym dźwiękiem. Wyższe wartości sprawiają, że powtórzenia bardziej się wyróżniają. | -2 do +2 (0.6) |
| **Sprzężenie** | Ile razy echo się powtarza. Wyższe wartości dają więcej powtórzeń, które dłużej zanikają. | -1 do +1 (0.5) |
| **Opóźnienie** | Czas między echami. Krótsze wartości dają ciasny slap-back; dłuższe dają rozstawione powtórzenia. | 0.01 do 2 s (0.4) |

**Presety:**

| Preset | Co robi |
|---|---|
| **Slapback** | Pojedyncze, ciasne powtórzenie tuż za dźwiękiem. Klasyczny rockabilly slap-back. |
| **Room** | Krótkie, naturalne echo, jak mały pokój. Dodaje przestrzeni bez rozmazywania dźwięku. |
| **Tape** | Ciepłe, średnie powtórzenia, które zanikają stopniowo, jak stare taśmowe opóźnienie. |
| **Dub** | Długie, ciężkie powtórzenia z mocnym sprzężeniem. Duże, dubowe i przestronne. |
| **Ping Pong** | Echa odbijają się między lewym a prawym głośnikiem dla szerokiego efektu stereo. |
| **Long** | Wolne, szeroko rozstawione powtórzenia, które ciągną się daleko za dźwiękiem. |

## Chorus (grubszy, szerszy dźwięk)

**Co robi:** Pogrubia i poszerza dźwięk, nakładając przesuniętą kopię na oryginał. Wybierz preset lub sam ustaw miks mokry/suchy, głębię, tempo i sprzężenie. Sprawia, że jeden instrument lub głos brzmi jak kilka grających razem, dodając lekko rozstrojone, poruszające się kopie. To dodaje bogactwa i delikatnego migotania. Subtelne ustawienia ocieplają brzmienie, podczas gdy mocne ustawienia brzmią bujnie i marzycielsko. Popularny na gitarach, klawiszach i wokalach.

**Suwaki:**

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Mokry/Suchy** | Ile chorusu słyszysz w porównaniu z oryginalnym dźwiękiem. Wyższe wartości sprawiają, że efekt jest bardziej oczywisty. | 0 do 100% (50) |
| **Głębia** | Jak daleko wysokość drży w górę i w dół. Wyższe wartości dają grubszy, bardziej migoczący dźwięk. | 0 do 100% (25) |
| **Tempo** | Jak szybko porusza się migotanie. Wolniejsze tempa brzmią delikatnie i bujnie; szybsze brzmią bardziej jak vibrato. | 0 do 10 Hz (1.1) |
| **Sprzężenie** | Ile efektu jest podawane z powrotem do siebie. Wyższe wartości sprawiają, że chorus jest bardziej rezonansowy i intensywny. | -99 do +99% (25) |

**Presety:**

| Preset | Co robi |
|---|---|
| **Subtle** | Delikatne pogrubienie, które dodaje ciepła bez zwracania na siebie uwagi. |
| **Lush** | Bogaty, klasyczny chorus. Świetne wszechstronne ustawienie dla gitar i klawiszy. |
| **Ensemble** | Pełne, warstwowe migotanie, które sprawia, że pojedynczy instrument brzmi jak kilka. |
| **Vibrato** | W pełni mokry z szybkim tempem, dla drżącego vibrato zamiast subtelnego chorusu. |
| **Wide** | Wolne, szerokie migotanie, które otwiera obraz stereo. Przestronne i marzycielskie. |
| **Twelve-String** | Jasne, rezonansowe migotanie przypominające dwunastostrunową gitarę. |

## Distortion (chropowatość i ostrość)

**Co robi:** Dodaje chropowatości i ostrości poprzez przesterowanie dźwięku. Wybierz preset lub sam ustaw drive, wyjście i barwę. Celowo szorstkuje dźwięk, od ciepłej, chropowatej krawędzi po połamany, zniekształcony ton. To efekt kreatywny, dla zabawy, a nie sposób na poprawę jakości, więc używaj go w małych ilościach. Jest zabawny na utworach elektronicznych, rockowych i eksperymentalnych. Obniż Wyjście, jeśli ciężki preset staje się zbyt głośny.

**Suwaki:**

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Drive** | Jak mocno dźwięk jest zniekształcany. Wyższe wartości są bardziej chropowate i agresywne. | 0 do 100% (15) |
| **Wyjście** | Poziom wyjścia po zniekształceniu. Obniż go, jeśli ciężkie ustawienie staje się zbyt głośne. | -60 do 0 dB (-18) |
| **Barwa** | Ścina soprany przed zniekształceniem. Niższe wartości brzmią ciemniej i cieplej. | 100 do 8000 Hz (8000) |
| **Środek** | Na której częstotliwości skupione jest zniekształcenie. Przesuwa charakter jaśniej lub ciemniej. | 100 do 8000 Hz (2400) |
| **Szerokość** | Jak szerokie jest to skupienie. Wąskie brzmi ostro i nosowo; szerokie brzmi pełnie i otwarcie. | 100 do 8000 Hz (2400) |

**Presety:**

| Preset | Co robi |
|---|---|
| **Warm Drive** | Lekka, ciepła chropowatość, która dodaje krawędzi bez większej zmiany charakteru. |
| **Crunch** | Klasyczny chrupiący overdrive, uderzeniowy i rytmiczny. |
| **Overdrive** | Jasny, napędzany ton z mnóstwem zgryzu. Świetny dla brzmień solowych. |
| **Fuzz** | Gruby, nasycony fuzz. Ciężki i pełen harmonicznych. |
| **Metal** | Ciasny, skupiony na średnicy ton o wysokim wzmocnieniu dla agresywnych, ciężkich brzmień. |
| **Screamer** | Podbity w średnicy overdrive, który się przebija, jak tube screamer. |
| **LoFi** | Zmiażdżone, wąskopasmowe zniekształcenie dla chropowatego charakteru lo-fi. |

## Rotate (wirujące stereo)

**Co robi:** Obraca dźwięk wokół pola stereo dla wirującego, obrotowego efektu. Wybierz preset lub sam ustaw tempo. Powoli przesuwa dźwięk wokół lewego i prawego kanału, trochę jak wirujący głośnik, co dodaje wirujące, hipnotyczne uczucie. Wolne ustawienia są delikatne i szerokie, podczas gdy szybkie ustawienia są zawrotne i oczywiste. To efekt stereo, więc jest najbardziej zauważalny na słuchawkach lub dobrze rozstawionych głośnikach.

**Suwak:**

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Tempo** | Jak szybko dźwięk obraca się wokół pola stereo. Wartości ujemne obracają w drugą stronę; zero trzyma go nieruchomo. | -5 do +5 Hz (1.0) |

**Presety:**

| Preset | Co robi |
|---|---|
| **Slow Pan** | Wolny, delikatny dryf z boku na bok. Subtelny i szeroki. |
| **Sway** | Miarowe kołysanie lewo-prawo. Dodaje delikatnego ruchu do obrazu stereo. |
| **Rotary** | Średni obrót przypominający wirujący głośnik. |
| **Fast Spin** | Szybki obrót wokół pola stereo dla zawrotnego, wirującego efektu. |
| **Reverse** | Średni obrót w przeciwnym kierunku. |
| **Whirl** | Bardzo szybki wir. Intensywny i dezorientujący. |

## Crossfeed (naturalny dźwięk na słuchawkach)

Na głośnikach każde z Twoich uszu słyszy zarówno lewy, jak i prawy głośnik, tylko w nieco różnych czasach i głośnościach. Na słuchawkach to naturalne mieszanie znika: Twoje lewe ucho słyszy tylko lewy kanał, a prawe ucho tylko prawy. To „super stereo” może sprawić, że muzyka wydaje się rozdzielona wewnątrz Twojej głowy, a nagrania mocno panoramowane, gdzie instrument siedzi w pełni po jednej stronie, mogą wydawać się nienaturalne lub męczące przy długim słuchaniu.

Crossfeed naprawia to, mieszając małą, filtrowaną ilość każdego kanału do drugiego, z niewielkim opóźnieniem i delikatnym ścięciem wysokich częstotliwości. To bliskie temu, jak dźwięk z prawdziwych głośników dociera do obu Twoich uszu, w tym sposobowi, w jaki Twoja głowa lekko zacienia dalsze ucho. Rezultatem jest bardziej naturalny, przypominający głośniki obraz, który siedzi trochę przed Tobą zamiast wewnątrz głowy, i zmniejsza zmęczenie słuchowe podczas długich sesji. Flacbox używa dobrze znanej metody **bs2b (Bauer stereophonic-to-binaural)**, cenionego otwartoźródłowego crossfeedu używanego przez wiele odtwarzaczy audiofilskich. Możesz przeczytać o algorytmie na [stronie projektu bs2b](https://bs2b.sourceforge.net/).

**Odcięcie** kontroluje, jak ciepło brzmi mieszanie, a **Poziom przenikania** kontroluje, jak silne ono jest. Presety obejmują klasyczne poziomy bs2b, od ledwie obecnego dotknięcia po zdecydowane, przypominające głośniki mieszanie. Crossfeed to efekt dla słuchawek, więc pozostaw go wyłączony, gdy słuchasz na głośnikach.

**Suwaki:**

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Odcięcie** | Ustawia, gdzie przenikanie między kanałami zaczyna się ścinać. Niższe wartości dają cieplejszy, bardziej wyrazisty efekt. | 300 do 2000 Hz (700) |
| **Poziom przenikania** | Kontroluje, ile jednego kanału przenika do drugiego. Wyższe wartości dają bardziej przypominający głośniki dźwięk. | 1 do 15 dB (4.5) |

**Presety:**

| Preset | Co robi |
|---|---|
| **Subtle** | Ledwie obecny crossfeed do swobodnego słuchania. Zmiękcza mocno panoramowane stereo bez zmiany balansu tonalnego. |
| **Chu Moy** | Klasyczne uniwersalne ustawienie domyślne. Zrównoważone i lekko ciepłe, działa na niemal każdym materiale. Zacznij tutaj. |
| **Strong** | Silniejsze przenikanie dla mocniej panoramowanych miksów. Bardziej oczywiste zwężenie stereo. |
| **Jan Meier** | Popularny wśród entuzjastów słuchawek. Szersze przenikanie, bardziej przypominająca głośniki prezentacja, lekkie podniesienie basów. |
| **Speaker-like** | Dostrojony do najbardziej naturalnego, głośnikowego odtwarzania przez słuchawki. |
| **Vintage Stereo** | Agresywny crossfeed dostrojony do miksów z lat 60. i 70. z mocno panoramowaną perkusją i wokalami. |

## Przetwarzanie sygnału: zbuduj własny łańcuch DSP

Poza gotowymi efektami Flacbox pozwala Ci zbudować własny łańcuch w **Ustawienia > Odtwarzacz audio > Przetwarzanie sygnału**. Jak wyjaśnia aplikacja, gdy łańcuch jest pusty: *«Dotknij +, aby dodać efekt. Włącz lub wyłącz każdy z nich jego przełącznikiem, przeciągnij, aby zmienić kolejność, dotknij, aby edytować jego parametry, i przytrzymaj, aby zduplikować lub usunąć.»*

**Kolejność ma znaczenie**: filtr przed zniekształceniem brzmi inaczej niż ten sam filtr po nim. Możesz również skierować cały łańcuch na **Wszystkie kanały**, **Lewy kanał** lub **Prawy kanał**.

Poniżej znajduje się każdy blok, z własnym tekstem aplikacji dla każdego suwaka i każdego presetu.

### Gain (regulacja poziomu)

Podnosi lub obniża poziom w jednym punkcie łańcucha.

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Gain** | Podbija lub tnie poziom w tym punkcie łańcucha. Użyj go, aby uzupełnić poziom po innych efektach lub aby napędzić te, które następują. | -24 do +24 dB (0) |

| Preset | Co robi |
|---|---|
| **Unity** | Brak zmiany poziomu. Neutralny punkt wyjścia. |
| **Cut** | Duże cięcie. Poskramia głośne źródło lub robi miejsce przed efektami, które następują. |
| **Trim** | Delikatne cięcie, aby nieco ściągnąć poziom. |
| **Lift** | Umiarkowane podbicie, aby podnieść ciche źródło. |
| **Boost** | Mocne podbicie dla cichego materiału lub aby mocniej napędzić następujące efekty. |
| **Max** | Maksymalne podbicie. Głośne, uważaj na przesterowanie później w łańcuchu. |

### Low Pass (usuwa soprany)

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Odcięcie** | Ustawia, gdzie filtr zaczyna ścinać soprany. Obniż je, aby przyciemnić i zmiękczyć dźwięk; podnieś je ku górze, aby w pełni otworzyć. | 20 Hz do 20 kHz (20 kHz) |
| **Rezonans** | Podkreśla częstotliwości tuż przy odcięciu. Trzymaj go nisko dla czystego ścięcia; podnieś dla szczytowej, gwiżdżącej krawędzi. | 0.1 do 10 (0.707) |

| Preset | Co robi |
|---|---|
| **Air** | Ścina tylko sam szczyt. Zdejmuje odrobinę krawędzi bez przytępienia dźwięku. |
| **Warm** | Delikatne ścięcie sopranów dla cieplejszego, bardziej okrągłego tonu. |
| **Mellow** | Zauważalnie zmiękczony. Ściąga jasność dla wyluzowanego klimatu. |
| **Muffled** | Ciemny i przytłumiony, jakby słyszany przez ścianę. |
| **Telephone** | Wąski, rezonansowy szczyt nisko w zakresie. Cienki, telefoniczny głos. |

### High Pass (usuwa basy)

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Odcięcie** | Ustawia, gdzie filtr zaczyna ścinać basy. Podnieś je, aby przerzedzić dolny zakres i usunąć dudnienie; obniż je ku dołowi, aby w pełni otworzyć. | 20 Hz do 20 kHz (20 Hz) |
| **Rezonans** | Podkreśla częstotliwości tuż przy odcięciu. Trzymaj go nisko dla czystego ścięcia; podnieś dla szczytowej, gwiżdżącej krawędzi. | 0.1 do 10 (0.707) |

| Preset | Co robi |
|---|---|
| **Rumble Cut** | Usuwa podakustyczne dudnienie i przesunięcie DC bez naruszania słyszalnego dolnego zakresu. |
| **Tighten** | Ścina dudniące niskie częstotliwości dla ciaśniejszego, czystszego basu. |
| **Thin** | Tnie ciepło i ciało, pozostawiając lżejszy, cieńszy dźwięk. |
| **Radio** | Pozostają tylko średnie i wysokie, jak mały głośnik radiowy. |
| **Telephone** | Wąski, rezonansowy szczyt wysoko w zakresie. Cienki, telefoniczny głos. |

### Band Pass (zachowuje środkowe pasmo)

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Środek** | Ustawia częstotliwość, którą filtr przepuszcza. Wszystko powyżej i poniżej niej jest ścinane. Przemiataj, aby wybrać basy, średnie lub soprany. | 20 Hz do 20 kHz (1 kHz) |
| **Rezonans** | Kontroluje, jak szerokie jest pasmo. Niskie wartości przepuszczają szeroki zakres; podnieś je, aby zawęzić się do środka dla ostrego, rezonansowego tonu. | 0.1 do 10 (0.707) |

| Preset | Co robi |
|---|---|
| **Voice** | Szerokie pasmo wokół średnicy, gdzie siedzi większość wokali. Neutralny punkt wyjścia. |
| **Bass** | Izoluje dolny zakres, pozostawiając tylko bas i stopę. |
| **Body** | Skupia się na niskiej średnicy dla ciepłego, pudełkowego ciała. |
| **Presence** | Podnosi wysoką średnicę dla klarowności i obecności. |
| **Telephone** | Wąskie pasmo średnicy. Cienki, telefoniczny dźwięk. |
| **Wah** | Bardzo wąski, rezonansowy szczyt. Przemiataj środek dla efektu wah. |

### Notch (usuwa jedno wąskie pasmo)

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Częstotliwość** | Ustawia częstotliwość, którą filtr usuwa. Wszystko powyżej i poniżej niej przechodzi. Dostrój ją na buczenie lub rezonans, aby je wyciąć. | 20 Hz do 20 kHz (60 Hz) |
| **Rezonans** | Kontroluje, jak szerokie jest cięcie. Niskie wartości wybierają szeroki zakres; podnieś je, aby usunąć tylko punktowe pasmo i pozostawić resztę nietkniętą. | 0.1 do 10 (8.0) |

| Preset | Co robi |
|---|---|
| **Mains Hum 60** | Usuwa buczenie elektryczne 60 Hz (sieć północnoamerykańska). Neutralny punkt wyjścia. |
| **Mains Hum 50** | Usuwa buczenie elektryczne 50 Hz (sieć europejska i inne). |
| **Rumble** | Tnie niskoczęstotliwościowe dudnienie lub rezonans bez przerzedzania całego dolnego zakresu. |
| **Mud** | Wybiera mętność niskiej średnicy dla czystszego, wyraźniejszego dźwięku. |
| **Boxy** | Usuwa pudełkowe nosowanie średnicy. |
| **Harsh** | Poskramia ostry, przeszywający szczyt w wysokiej średnicy. |

### Peaking (parametryczne pasmo EQ)

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Częstotliwość** | Środek pasma do podbicia lub cięcia. Przemiataj, aby znaleźć częstotliwość, którą chcesz ukształtować. | 20 Hz do 20 kHz (1 kHz) |
| **Gain** | O ile podbić lub ciąć w środku. Dodatnie podnosi pasmo; ujemne je wybiera. | -15 do +15 dB (0) |
| **Współczynnik Q** | Ustawia, jak szerokie jest pasmo. Niskie wartości kształtują szeroki obszar; wysokie wartości zawężają dla chirurgicznych, punktowych zmian. | 0.1 do 10 (1.0) |

| Preset | Co robi |
|---|---|
| **Presence** | Szerokie podniesienie wysokiej średnicy dla klarowności i obecności. Neutralny punkt wyjścia. |
| **Warmth** | Szerokie podbicie niskiej średnicy, które dodaje ciała i ciepła. |
| **Vocal Boost** | Podnosi rdzeń zakresu wokalnego, aby wysunąć głosy do przodu. |
| **Cut Mud** | Wybiera pudełkową mętność niskiej średnicy dla czystszego dźwięku. |
| **Tame Harsh** | Wąskie cięcie, aby poskromić ostry, przeszywający szczyt. |
| **Punch** | Niskie podbicie, które dodaje uderzenia i impaktu dolnemu zakresowi. |
| **Sub Boost** | Głębokie podbicie na samym dole dla dodatkowego ciężaru sub-basów. |
| **Air** | Szerokie podniesienie na górze dla otwartego, przewiewnego połysku. |
| **Clarity** | Podnosi wysoką średnicę, aby dodać definicji i krawędzi. |
| **De-Ess** | Wąskie cięcie w zakresie syczenia, aby poskromić ostre dźwięki S. |
| **De-Boom** | Tnie dudniące nagromadzenie niskich częstotliwości dla ciaśniejszego dolnego zakresu. |
| **Scoop** | Szerokie obniżenie średnicy dla wyciętego, nowoczesnego tonu. |

### Low Shelf (kontrola basów i podbicie basów)

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Częstotliwość** | Ustawia narożnik, poniżej którego półka działa. Wszystko pod nim jest podbijane lub cięte razem. | 20 do 2000 Hz (200) |
| **Gain** | O ile podnieść lub obniżyć dolny zakres. Dodatnie dodaje ciężaru i ciepła; ujemne go przerzedza. | -15 do +15 dB (0) |

| Preset | Co robi |
|---|---|
| **Warmth** | Delikatne podniesienie dolnego zakresu dla ciepła i ciała. Neutralny punkt wyjścia. |
| **Bass Boost** | Solidne podbicie basu dla ciężaru i uderzenia. |
| **Fullness** | Wypełnia niższą średnicę dla pełniejszego, bardziej okrągłego dźwięku. |
| **Trim Bass** | Umiarkowane cięcie, aby rozjaśnić basowo ciężki miks. |
| **Cut Lows** | Mocne cięcie, aby przerzedzić lub odbuczyć dolny zakres. |
| **Big Bottom** | Duże podbicie dolnego zakresu dla maksymalnego ciężaru i dudnienia. |

### High Shelf (kontrola sopranów)

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Częstotliwość** | Ustawia narożnik, powyżej którego półka działa. Wszystko nad nim jest podbijane lub cięte razem. | 1 do 20 kHz (8 kHz) |
| **Gain** | O ile podnieść lub obniżyć górny zakres. Dodatnie dodaje jasności i powietrza; ujemne wygładza i przyciemnia. | -15 do +15 dB (0) |

| Preset | Co robi |
|---|---|
| **Presence** | Delikatne podniesienie górnego zakresu dla klarowności i szczegółów. Neutralny punkt wyjścia. |
| **Air** | Otwiera sam szczyt dla przewiewnego, otwartego dźwięku. |
| **Bright** | Mocne podbicie dla wyrazistego, jasnego, wysuniętego tonu. |
| **Soften** | Umiarkowane cięcie, aby zdjąć krawędź z ostrych sopranów. |
| **Tame Highs** | Mocne cięcie, aby przyciemnić i wygładzić nadmiernie jasny dźwięk. |
| **Sparkle** | Duże podbicie górnego zakresu dla maksymalnego migotania i blasku. |

### Soft Clip (ciepłe nasycenie)

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Drive** | Popycha sygnał mocniej w kształtownik fali. Małe ilości dodają delikatnego ciepła; duże zaokrąglają szczyty w gęste nasycenie i chropowatość. | 0 do 40 dB (0) |

| Preset | Co robi |
|---|---|
| **Warm** | Odrobina drive'u dla delikatnego, analogowego ciepła. |
| **Drive** | Zauważalne nasycenie, które pogrubia i koloruje dźwięk. |
| **Crunch** | Ciężki drive ze słyszalną chrupiącą krawędzią. |
| **Fuzz** | Gruba, zniekształcona chropowatość. Szczyty są mocno ściśnięte. |
| **Destroy** | Maksymalny drive. Agresywna, w pełni nasycona chropowatość. |

### Bit Crusher (retro lo-fi)

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Głębia bitowa** | Ustawia, ile bitów opisuje każdą próbkę. Mniej bitów oznacza grubsze stopnie i więcej szumu kwantyzacji, dla chrupiącego, chropowatego cyfrowego dźwięku. | 1 do 16 bitów (16) |
| **Częstotliwość próbkowania** | Zmniejsza próbkowanie dźwięku. Przy stu procentach częstotliwość jest nietknięta; obniż ją, aby dłużej trzymać każdą próbkę, przytępiając soprany i dodając ostrą, aliasingową krawędź. | 1% do 100% (100%) |

| Preset | Co robi |
|---|---|
| **Vintage** | Subtelny spadek jakości, jak wczesny cyfrowy sampler. |
| **LoFi** | Klasyczne 8-bitowe, półszybkościowe lo-fi. Ziarniste i retro. |
| **Crunch** | Cięższe kruszenie ze słyszalną chrupiącą krawędzią. |
| **Gritty** | Szorstkie i chropowate. Stopnie między poziomami są oczywiste. |
| **Destroy** | Ekstremalna redukcja. Ostre, połamane, ledwie rozpoznawalne. |

### Ring Modulator (metaliczne i robotyczne tony)

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Nośna** | Ustawia częstotliwość tonu, przez który mnożony jest sygnał. Kilka herców daje drżące tremolo; wyższe częstotliwości dodają metalicznych, dzwonkowych i robotycznych alikwotów. | 1 do 4000 Hz (440) |
| **Miks** | Miesza zmodulowany dźwięk z oryginałem. Przy zero procent słyszysz tylko suchy sygnał; przy stu procentach tylko w pełni zmodulowany ton. | 0% do 100% (0%) |

| Preset | Co robi |
|---|---|
| **Tremolo** | Bardzo niska nośna zamienia go w amplitudowe tremolo, drżąc głośnością. |
| **Robot** | Średnia nośna dodaje brzęczących alikwotów dla klasycznego efektu głosu robota. |
| **Metallic** | Gęste, nieharmoniczne alikwoty dla ostrego, metalicznego tonu. |
| **Bell** | Wyższa nośna daje jasne, dzwonkowe brzmienie. |
| **Alien** | W pełni mokry z wysoką nośną. Ekstremalny, obcy, ledwie rozpoznawalny. |

### Tremolo (drżenie głośności)

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Tempo** | Ustawia, jak szybko pulsuje głośność. Wolniejsze tempa dają gładkie kołysanie; szybsze tempa dają szybkie jąkanie. | 0.1 do 20 Hz (5) |
| **Głębia** | Ustawia, o ile spada głośność przy każdym pulsie. Przy zero procent poziom jest stały; przy stu procentach opada aż do ciszy. | 0% do 100% (0%) |

| Preset | Co robi |
|---|---|
| **Gentle** | Wolne, płytkie kołysanie. Subtelny ruch bez zwracania uwagi. |
| **Classic** | Klasyczne tremolo wzmacniacza: średnie tempo i umiarkowana głębia. |
| **Deep** | Mocny, głęboki puls, który niemal opada do ciszy przy każdym cyklu. |
| **Fast** | Szybkie trzepotanie dla migoczącego, nerwowego uczucia. |
| **Chop** | Szybkie i pełnej głębi. Twarde, jąkające się siekanie. |

### Delay (echo)

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Czas** | Ustawia przerwę przed każdym echem. Krótkie czasy dają ciasny slapback; dłuższe czasy rozstawiają powtórzenia dalej od siebie. | 0.01 do 2 s (0.25) |
| **Sprzężenie** | Ustawia, ile każdego echa jest podawane z powrotem. Niskie wartości dają pojedyncze powtórzenie; wyższe wartości budują długą, ciągnącą się serię ech. | 0 do 0.95 (0.4) |
| **Miks** | Miesza echa z oryginałem. Przy zero procent słyszysz tylko suchy sygnał; przy stu procentach tylko echa. | 0% do 100% (0%) |

| Preset | Co robi |
|---|---|
| **Slapback** | Pojedyncze krótkie echo, ciasno przy oryginale. Rockabilly i dublowanie wokali. |
| **Echo** | Klasyczne echo: wyraźne powtórzenie z kilkoma ciągnącymi się ogonami. |
| **Ping** | Szybkie, odbijające się powtórzenie, które dodaje rytmicznego ruchu. |
| **Ambient** | Dłuższe, łagodniejsze powtórzenia, które rozpływają się w przestronny ogon. |
| **Dub** | Wysokie sprzężenie dla długich, dubowych kaskad echa. |
| **Cavern** | Długie, głębokie powtórzenia, jak dźwięk echem przez ogromną przestrzeń. |

### Stereo Width (zwęż lub poszerz)

| Kontrolka | Co robi | Zakres (domyślnie) |
|---|---|---|
| **Szerokość** | Zwęża lub poszerza obraz stereo. Zero procent zwija do mono, sto procent pozostawia nietknięty, a wyższe wartości pchają boki szerzej. Wpływa tylko na utwory stereo na celu Wszystkie kanały. | 0% do 200% (100%) |

| Preset | Co robi |
|---|---|
| **Wide** | Delikatne poszerzenie, które otwiera obraz stereo. Neutralny punkt wyjścia. |
| **Wider** | Mocniejsze rozłożenie dla dużego, wciągającego pola stereo. |
| **Max** | Maksymalna szerokość. Bardzo szeroko, ale uważaj na problemy z kompatybilnością mono. |
| **Narrow** | Ściąga boki do środka dla ciaśniejszego, bardziej wyśrodkowanego obrazu. |
| **Focused** | Niemal wyśrodkowany, z tylko odrobiną stereo. |
| **Mono** | W pełni zwinięty do mono. Oba głośniki grają ten sam sygnał. |

## Jak to wszystko działa pod maską (prosta wersja)

- **Silniki:** wybierasz jeden w Ustawienia > Odtwarzacz audio > Silnik odtwarzania: **Standard** (systemowy), **Universal** (FFmpeg) lub **Sound FX** (**silnik BASS™** od [Un4seen Developments](https://www.un4seen.com/)). Wybrany silnik decyduje, które formaty się odtwarzają, a efekty, korektor i łańcuch DSP działają tylko w silniku Sound FX.
- **Formaty:** silnik BASS™ dodaje FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus oraz muzykę modułową (trackerową) na wierzchu formatów systemowych i FFmpeg.
- **Efekty:** korektor, kompresor i większość efektów używają dodatków efektów BASS™. Freeverb to pogłos Freeverb. Chorus, Flanger i Distortion używają klasycznych efektów w stylu DirectX z własnymi kontrolkami.
- **Normalizacja głośności:** działający na żywo wyrównywacz głośności **EBU R128** (standard głośności używany w nadawaniu i streamingu).
- **Crossfeed:** crossfeed **bs2b (Bauer)**, uruchamiany wewnątrz silnika BASS™.
- **Łańcuch DSP:** Twoje własne bloki, stosowane w dokładnej kolejności, którą ustawisz, na wszystkich kanałach lub tylko jednej stronie.
- **Wyjście:** możesz ustawić częstotliwość próbkowania, liczbę kanałów i rozmiar bufora, aby dopasować do swojego sprzętu.

Ponieważ to wszystko działa na żywo, gdy muzyka gra, efekty:

- Działają w **czasie rzeczywistym** na wszystkim, w tym plikach w chmurze, strumieniach i muzyce modułowej.
- **Nigdy nie zmieniają ani nie zapisują ponownie** Twoich plików. Wyłącz efekt, a oryginał wraca.
- **Pamiętają Twoje ustawienia** dla każdego efektu.
- Mogą być **dowolnie mieszane i łączone**, ponieważ każdy z nich jest osobny.

## Proste przepisy do wypróbowania

**Codzienne słuchanie**

- **Więcej basu, czysto:** Korektor > Bass Booster, następnie obniż Przedwzmacniacz o 1 do 2 dB. Lub dodaj DSP Low Shelf na Bass Boost.
- **Równa głośność w mieszanej playliście:** Normalizacja głośności > Standard, plus Kompresor > Soft.
- **Delikatne ogólne dopracowanie:** Kompresor > Transparent, plus Normalizacja głośności > Light.
- **Wyraźniejsze wokale:** Korektor > Vocal Booster, lub blok DSP Peaking na Vocal Boost.
- **Pełniejszy dźwięk na małych głośnikach telefonu:** Korektor > Small Speakers.

**Słuchawki**

- **Przyjemniej, mniej męcząco na słuchawkach:** Crossfeed > Chu Moy lub Jan Meier.
- **Szerszy dźwięk na słuchawkach:** DSP Stereo Width > Wide, plus Crossfeed > Chu Moy.
- **Napraw mocno panoramowane płyty z lat 60. i 70.:** Crossfeed > Vintage Stereo.
- **Odrobina powietrza i przestrzeni:** Freeverb > Ambience, utrzymany nisko, plus Crossfeed > Subtle.

**Ciche pory i mowa**

- **Ciche słuchanie późną nocą:** Normalizacja głośności > Night, plus Kompresor > Late Night.
- **Podcasty i audiobooki:** Kompresor > Voice / Podcast, plus Korektor > Spoken Word.
- **Najgłośniejszy, najbardziej równy dźwięk w hałaśliwym samochodzie:** Normalizacja głośności > Strong, plus Kompresor > Heavy.

**Rozwiązywanie problemów**

- **Poskrom ostre, jasne nagranie:** Korektor > Treble Reducer, lub blok DSP Peaking na Tame Harsh.
- **Usuń buczenie elektryczne:** łańcuch DSP > Notch > Mains Hum 60 (lub Mains Hum 50 w Europie).
- **Ciaśniejszy, czystszy bas:** DSP High Pass > Tighten, aby wyciąć dudniący dolny zakres.
- **Mniej dudnienia w basowo ciężkim miksie:** DSP Low Shelf > Trim Bass, lub Peaking > De-Boom.

**Kreatywne i zabawne**

- **Ciepły, przestronny klimat:** Freeverb > Hall, utrzymany nisko.
- **Marzycielskie, przestronne gitary:** Chorus > Wide, plus Echo > Long.
- **Retro lo-fi:** łańcuch DSP > Bit Crusher (LoFi) do Soft Clip (Warm).
- **Funkowy ruch na utworach elektronicznych:** Auto Wah > Funky, lub Phaser > Fast.
- **Klasyczne przemiatanie odrzutowca:** Flanger > Jet.

## FAQ

{{% details title="Jakiego silnika dźwięku używa Flacbox?" closed="true" %}}
Wybierasz jeden Silnik odtwarzania w Ustawienia > Odtwarzacz audio: Standard (systemowy silnik Apple), Universal (silnik FFmpeg) lub Sound FX (silnik BASS™ od Un4seen Developments, un4seen.com). Wybrany silnik decyduje, które formaty plików się odtwarzają. Sound FX to ten, który odtwarza dodatkowe formaty jak FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus oraz muzykę MOD lub trackerową, i jest jedynym silnikiem, który zapewnia efekty na żywo, 10-pasmowy korektor i łańcuch DSP. Aby korzystać z efektów, ustaw silnik odtwarzania na Sound FX.
{{% /details %}}

{{% details title="Czy Flacbox może odtwarzać MOD, XM, IT i inną muzykę trackerową lub modułową?" closed="true" %}}
Tak. Silnik BASS™ ma wbudowany odtwarzacz modułów, który ładuje pliki MOD, XM, IT, S3M, MTM, UMX i MO3 oraz odbudowuje utwór na żywo z jego wzorców i brzmień instrumentów, w sposób, w jaki muzyka trackerowa ma być odtwarzana. Zwykłe odtwarzacze na iPhone nie potrafią tego zrobić. Efekty i korektor działają również na muzyce modułowej.
{{% /details %}}

{{% details title="Czy Flacbox obsługuje DSD i pliki wysokiej rozdzielczości?" closed="true" %}}
Tak. Flacbox odtwarza pliki DSD (DSF i DFF) przez silnik BASS™ z użyciem DSD over PCM, więc działają na normalnym sprzęcie wyjściowym, plus FLAC, WavPack, Monkey's Audio (APE), Musepack i TrueAudio do bezstratnego odtwarzania.
{{% /details %}}

{{% details title="Jakie efekty dźwiękowe ma Flacbox?" closed="true" %}}
10-pasmowy korektor, Normalizację głośności, Kompresor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate i Crossfeed, plus własny łańcuch DSP z filtrami, półkami, wzmocnieniem, soft clipem, bit crusherem, ring modulatorem, tremolo, opóźnieniem i szerokością stereo. Każdy z nich jest osobny i można go łączyć z pozostałymi.
{{% /details %}}

{{% details title="Czym jest preset?" closed="true" %}}
Preset to gotowe ustawienie dla efektu. Zamiast samemu poruszać suwakami, dotykasz presetu, a dźwięk zmienia się, aby mu odpowiadać. Każdy efekt w Flacbox ma kilka presetów, a ten przewodnik wymienia, co robi każdy z nich. Jeśli poruszysz suwak po wybraniu presetu, efekt pokazuje „Ręczny”, aby powiedzieć Ci, że korzysta teraz z Twoich własnych wartości.
{{% /details %}}

{{% details title="Jak otworzyć efekty audio w Flacbox?" closed="true" %}}
Otwórz odtwarzacz Teraz odtwarzane, dotknij przycisku ⋯ (Więcej) i wybierz Efekty audio. Lub przejdź do Ustawienia > Odtwarzacz audio > Efekty audio. Dotknij efektu, włącz jego przełącznik i wybierz preset, lub otwórz suwaki, aby dostroić.
{{% /details %}}

{{% details title="Gdzie jest korektor i jakie są najlepsze ustawienia?" closed="true" %}}
Przejdź do Ustawienia > Odtwarzacz audio > Korektor audio. Ma 10 pasm od 32 Hz do 16 kHz, każde od -12 do +12 dB, plus Przedwzmacniacz od -24 do +24 dB i 22 presety. Dla większego basu użyj Bass Booster. Dla wyraźniejszych głosów użyj Vocal Booster lub Pop. Dla jaśniejszego dźwięku użyj Treble Booster. Następnie dostosuj pojedyncze pasma do gustu.
{{% /details %}}

{{% details title="Jak podbić basy w Flacbox?" closed="true" %}}
Dwa łatwe sposoby. W Korektorze audio wybierz Bass Booster (lub podnieś pasma 32 Hz i 64 Hz o kilka dB). Lub, w Przetwarzaniu sygnału, dodaj blok Low Shelf ustawiony na Bass Boost. W obu przypadkach obniż Przedwzmacniacz lub dodaj blok Gain o 1 do 2 dB, aby bas pozostał czysty i się nie zniekształcał.
{{% /details %}}

{{% details title="Który preset korektora jest najlepszy dla mojej muzyki?" closed="true" %}}
Rock i Electronic dodają energii mocnym dołem i górą. Acoustic, Jazz i Classical pozostają ciepłe i naturalne. Pop i Vocal Booster wysuwają głosy do przodu. Bass Booster i Hip-Hop dodają ciężaru. Deep i Loudness brzmią pełniej przy niskiej głośności. Zacznij od tego, który pasuje do Twojego gatunku, a następnie dostrój.
{{% /details %}}

{{% details title="Czym jest Normalizacja głośności i czym różni się od ReplayGain?" closed="true" %}}
Sprawia, że każdy utwór gra na mniej więcej tej samej głośności. Mierzy rzeczywistą głośność przy użyciu standardu EBU R128 (w LUFS, jak serwisy streamingowe) i dostosowuje każdy utwór w kierunku Twojego celu, z limitem maksymalnego podbicia. W przeciwieństwie do ReplayGain nie potrzebuje żadnych tagów w plikach i działa na dowolnym źródle, na żywo, bez zmiany dźwięku. Presety: Light, Standard, Strong i Night.
{{% /details %}}

{{% details title="Czym jest Crossfeed i czy powinienem go używać?" closed="true" %}}
Crossfeed miesza trochę lewego i prawego kanału razem, aby słuchawki bardziej przypominały prawdziwe głośniki i mniej odczucie, że dźwięk utknął w Twojej głowie. Jest tylko dla słuchawek, więc wyłącz go dla głośników. Flacbox używa metody bs2b (Bauer), z presetami jak Chu Moy i Jan Meier.
{{% /details %}}

{{% details title="Jaka jest różnica między Kompresorem a Normalizacją głośności?" closed="true" %}}
Normalizacja głośności dopasowuje głośność między różnymi utworami. Kompresor wyrównuje głośne i ciche fragmenty wewnątrz pojedynczego utworu. Rozwiązują różne problemy i dobrze ze sobą współpracują, zwłaszcza w samochodzie lub głośnym miejscu.
{{% /details %}}

{{% details title="Czym jest łańcuch Przetwarzania sygnału (DSP)?" closed="true" %}}
To własny zestaw w Ustawienia > Odtwarzacz audio > Przetwarzanie sygnału. Dodaj bloki jak filtry, półki, wzmocnienie, soft clip, bit crusher, ring modulator, tremolo, opóźnienie i szerokość stereo, ustaw je w dowolnej kolejności, włącz lub wyłącz każdy i skieruj łańcuch na wszystkie kanały, lewy lub prawy. Ponieważ kolejność ma znaczenie, możesz zaprojektować dokładnie ten dźwięk, którego chcesz.
{{% /details %}}

{{% details title="Jaka jest różnica między Korektorem, efektami a łańcuchem DSP?" closed="true" %}}
Korektor to prosta 10-pasmowa kontrola barwy. Efekty audio to gotowe narzędzia (kompresor, pogłos, echo i tak dalej) z presetami. Łańcuch DSP to miejsce, gdzie budujesz własną kolejność efektów z pojedynczych bloków. Możesz uruchomić wszystkie trzy jednocześnie.
{{% /details %}}

{{% details title="Czy efekty zmieniają lub uszkadzają moje pliki muzyczne?" closed="true" %}}
Nie. Wszystko jest stosowane na żywo, gdy muzyka gra. Twoje pliki nigdy nie są zmieniane ani zapisywane ponownie. Wyłącz efekt, a oryginalny dźwięk wraca natychmiast.
{{% /details %}}

{{% details title="Czy mogę używać więcej niż jednego efektu jednocześnie?" closed="true" %}}
Tak. Każdy efekt ma własny przełącznik i nie ma głównego przełącznika, więc dowolna kombinacja działa. Na przykład Normalizacja głośności plus Kompresor dla równego słuchania, lub Freeverb plus Crossfeed na słuchawkach, z korektorem na wierzchu.
{{% /details %}}

{{% details title="Dlaczego kontrolki efektu są wyszarzone?" closed="true" %}}
Efekt jest wyłączony. Włącz jego przełącznik na górze edytora, aby użyć kontrolek. Każdy efekt jest domyślnie wyłączony.
{{% /details %}}

{{% details title="Co oznacza etykieta Ręczny?" closed="true" %}}
Oznacza to, że odsunąłeś suwak od presetu, więc efekt korzysta teraz z Twoich własnych niestandardowych wartości zamiast nazwanego presetu. Każdy suwak ma przycisk resetowania, a ponowne wybranie presetu zastępuje Twoje ręczne wartości.
{{% /details %}}

{{% details title="Czy mogę zapisywać i udostępniać moje presety korektora?" closed="true" %}}
Tak. Oprócz 22 wbudowanych presetów możesz tworzyć własne, zmieniać ich kolejność oraz eksportować lub importować je, aby przenieść swoje ustawienia na inne urządzenie.
{{% /details %}}

{{% details title="Czy efekty działają z CarPlay, streamingiem i odtwarzaniem w tle?" closed="true" %}}
Tak. Efekty działają wewnątrz silnika BASS™, więc stosują się do plików lokalnych, dysków w chmurze, serwerów multimediów, strumieni i muzyki modułowej, i działają nadal podczas CarPlay oraz odtwarzania w tle.
{{% /details %}}

{{% details title="Czy mogę zmienić jakość wyjścia audio?" closed="true" %}}
Tak. W Ustawienia > Odtwarzacz audio możesz ustawić wyjściową częstotliwość próbkowania, liczbę kanałów i rozmiar bufora, aby dopasować do swoich słuchawek, głośników lub DAC.
{{% /details %}}

{{% details title="Jaka jest dobra początkowa konfiguracja dla słuchawek?" closed="true" %}}
Włącz Normalizację głośności (Standard), dodaj lekki Kompresor (Soft), wybierz preset korektora, który lubisz, i włącz Crossfeed (Chu Moy lub Jan Meier). Pozostaw pogłos, echo i distortion wyłączone, chyba że chcesz kreatywnego brzmienia.
{{% /details %}}

---

*BASS jest znakiem towarowym Un4seen Developments Ltd. Zobacz [un4seen.com](https://www.un4seen.com/). Crossfeed używa algorytmu bs2b (Bauer stereophonic-to-binaural); zobacz [stronę projektu bs2b](https://bs2b.sourceforge.net/).*
