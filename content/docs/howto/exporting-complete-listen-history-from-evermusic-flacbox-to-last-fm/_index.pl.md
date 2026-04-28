---
title: "Eksportuj pełną historię słuchania z Evermusic i Flacbox do Last.fm"
date: 2024-01-30
description: "Dowiedz się, jak wyeksportować historię muzyki z Evermusic i Flacbox i przesłać ją do Last.fm za pomocą plików CSV i narzędzia Last.fm Scrubbler dla Windows."
keywords: ["evermusic", "flacbox", "lastfm", "historia muzyki", "scrobbling", "eksport utworów", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "ostatnie", "lastfm", "eksport", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Podsumowanie:** Wyeksportuj historię słuchania z Evermusic lub Flacbox jako plik CSV, a następnie prześlij ją do Last.fm za pomocą bezpłatnego narzędzia Last.fm-Scrubbler-WPF na Windows. Automatyczne scrobblowanie jest również dostępne natywnie w obu aplikacjach.

**Aktualizacja:** Automatyczne scrobblowanie jest teraz dostępne! Dowiedz się więcej tutaj: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobblowanie to prosty sposób na automatyczne zapisywanie podstawowych informacji, takich jak tytuł i wykonawca aktualnie odtwarzanego utworu, w usłudze online. Później możesz przejrzeć swoją historię słuchania.

[Last.fm](https://www.last.fm/home), zasilany przez system rekomendacji muzycznych o nazwie Audioscrobbler, oferuje tę usługę za darmo. Tworzy szczegółowy profil Twoich gustów muzycznych, rejestrując utwory, których słuchasz, niezależnie od tego, czy pochodzą z internetowych stacji radiowych, komputera czy różnych przenośnych odtwarzaczy muzyki. Możesz później odwiedzić stronę internetową, aby otrzymać rekomendacje nowych artystów lub albumów pasujących do Twoich gustów muzycznych.

Możesz przesłać swoją historię słuchania do [Last.fm](http://Last.fm) z aplikacji Evermusic i Flacbox za pomocą bezpłatnego narzędzia, a my pokażemy Ci, jak to zrobić.

Otwórz sekcję 'Biblioteka muzyki' w aplikacji i przewiń do sekcji 'Szybki dostęp'. Dotknij elementu menu 'Ostatnie'.

![ekran biblioteki muzyki](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

Na ekranie 'Ostatnie' dotknij przycisku 'Więcej' w prawym górnym rogu, aby aktywować menu 'Więcej akcji'. Dotknij elementu menu 'Eksportuj listę utworów'.

![ekran ostatnich](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

Na ekranie 'Wybierz format pliku' masz możliwość wyboru formatu pliku docelowego. Dostępne opcje - CSV, TXT, M3U.

![ekran wyboru formatu pliku](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: To skrót od Comma-Separated Values, idealny do organizowania danych w przejrzystym formacie tabelarycznym. W pliku docelowym znajdziesz parametry takie jak Nazwa artysty, Nazwa albumu, Nazwa utworu, Znacznik czasu (czas, kiedy słuchałeś utworów), Nazwa wykonawcy albumu i Czas trwania utworu.

TXT: Tutaj mówimy o zwykłym pliku tekstowym. Jest prosty i bezpośredni, z parametrami obejmującymi Nazwę artysty, Nazwę albumu, Nazwę utworu i Czas trwania.

M3U: Ten format jest zasadniczo głównym wyborem do tworzenia list odtwarzania. Jest świetny, ponieważ możesz wyeksportować listę utworów i cieszyć się nimi na dowolnym urządzeniu, nawet jeśli nie masz oryginalnych plików (pod warunkiem, że wybierzesz opcję bezwzględnego adresu URL dla plików multimedialnych). W pliku wyjściowym znajdziesz parametry takie jak Czas trwania, Nazwa artysty, Nazwa utworu i Lokalizacja pliku multimedialnego.

Dla naszego zadania wybór CSV jest właściwą drogą. Będziemy używać tego pliku z bezpłatnym oprogramowaniem Last.fm-Scrubbler-WPF, aby przesłać naszą historię słuchania do usługi [Last.fm](http://Last.fm). Po prostu wybierz CSV i naciśnij przycisk 'Eksportuj'.

![ekran zakończenia eksportu](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Po zakończeniu eksportu po prostu dotknij przycisku 'Pokaż plik', a aplikacja wyświetli utworzony plik w folderze dokumentów. Następnie dotknij przycisku 'Więcej akcji' obok nazwy pliku i wybierz opcję 'Otwórz w' z menu. Naszym następnym krokiem jest skopiowanie wyeksportowanego pliku na komputer stacjonarny. Możesz to łatwo zrobić, wybierając opcję AirDrop z menu 'Otwórz w'.

![więcej akcji dla wyeksportowanego pliku](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Następnie będziemy używać bezpłatnego klienta open-source [Last.FM](http://Last.FM), który jest dostępny tylko na platformie Windows. Ten klient pozwala efektywnie aktualizować historię słuchania na [Last.FM](http://Last.FM) przy użyciu pliku CSV, który właśnie wyeksportowaliśmy.

Jeśli nie korzystasz obecnie z komputera z Windows, nie martw się. Nadal możesz uzyskać dostęp do tego klienta, instalując VirtualBox na swoim Mac i używając oficjalnego obrazu środowiska programistycznego Windows.

Oto, co musisz zrobić:

- Zainstaluj VirtualBox z następującego linku: [Pobierz VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Pobierz i zainstaluj środowisko programistyczne Windows z tego linku: [Środowisko programistyczne Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Na komputerze z Windows (lub w aplikacji VirtualBox z obrazem Windows Development) pobierz i zainstaluj [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - bezpłatne oprogramowanie open-source dostępne na GitHub. Testowaliśmy na wersji 1.28, którą możesz pobrać tutaj: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Strona pobierania Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

W sekcji 'Assets' kliknij na [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip), aby pobrać archiwum instalacyjne. Rozpakuj pobrany plik i otwórz rozpakowany folder.

- WAŻNE

Ta aplikacja jest wciąż w wersji beta. Twórcy aplikacji nie przeprowadzili wielu testów. Zalecają najpierw spróbować scrobblować do konta testowego i sprawdzić, czy rzeczy, które chcesz scrobblować, działają prawidłowo. Szczególnie jeśli scrobblujesz wiele utworów naraz. Proszę, bądź ostrożny ze swoimi kontami.

Uruchom Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Na głównym ekranie aplikacji po prostu kliknij 'Nie zalogowano' w lewym dolnym rogu, aby aktywować ekran 'Dodaj konto'.

![Ekran dodawania konta](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Wprowadź swoje dane logowania.

![ekran wprowadzania danych logowania](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Kliknij przycisk 'Login', aby dodać swoje konto.

![Kliknij przycisk Login, aby dodać swoje konto.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Otwórz kartę 'File Parse Scrobbler', aby rozpocząć importowanie pliku CSV z aplikacji Evermusic.

![Otwórz kartę File Parse Scrobbler, aby rozpocząć importowanie pliku CSV z aplikacji Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Wybierz 'Parser: CSV' i kliknij przycisk 'Settings'.

Na następnym ekranie możesz wybrać kolejność parametrów w pliku CSV.

Poszczególne pola mogą być ujęte w cudzysłowy i MUSZĄ być ujęte w cudzysłowy, jeśli pole zawiera którykolwiek z ustawionych ograniczników. Na przykład:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Zostaw więc wszystkie ustawienia domyślne; jedyne, co musisz zmienić, to zaznaczenie pola wyboru w polu 'Has Fields Enclosed In Quotes'.

Kliknij 'Save & Close', aby zastosować zmiany.

![wybierz kolejność parametrów w pliku CSV.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Scrobblowanie z parsowania pliku ma dwa tryby. Można je zmienić za pomocą ComboBox 'Scrobbling Mode'.

Tryb normalny: W tym trybie utwory będą scrobblowane ze znacznikiem czasu z przeanalizowanego scrobble'a. Tylko scrobble'e nowsze niż 14 dni mogą być scrobblowane.

Tryb importu: W tym trybie utwory będą scrobblowane ze znacznikiem czasu obliczonym na podstawie 'Finish Time' i wybranego czasu trwania między każdym utworem. Pozwala to na scrobblowanie utworów nawet jeśli znacznik czasu przeanalizowanego scrobble'a jest starszy niż 14 dni. Dlatego pierwszy (najwyższy) utwór w pliku CSV będzie scrobblowany z 'Finish Time'.

Wybierz wcześniej wygenerowany plik CSV z aplikacji Evermusic w polu 'File:' i kliknij 'Parse'. W niektórych przypadkach możesz zobaczyć alert o błędzie informujący, że niektóre scrobble'e nie mogły zostać przeanalizowane. To normalne, jeśli masz utwory bez pełnych metadanych, takich jak Nazwa artysty.

![niektóre scrobble'e nie mogły zostać przeanalizowane](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Kliknij przycisk 'Check All', aby wybrać wszystkie przeanalizowane utwory.

![Kliknij przycisk Check All, aby wybrać wszystkie przeanalizowane utwory.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Kliknij przycisk 'Preview', aby sprawdzić wszystkie zmiany, które zostaną wysłane na serwer.

![Kliknij przycisk Preview, aby sprawdzić wszystkie zmiany, które zostaną wysłane na serwer.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Kliknij przycisk 'Scrobble', aby przesłać wszystkie zmiany na serwer.

![Kliknij przycisk Scrobble, aby przesłać wszystkie zmiany na serwer.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Wcześniej Last.fm-Scrubbler-WPF nie miał dziennego limitu scrobble'i. To się teraz zmieniło, ponieważ niektórzy ludzie używali Scrubblera do scrobblowania tak wielu utworów, że powodowało to problemy na stronie Last.fm. Limit scrobble'i wynosi obecnie 2800 scrobble'i dziennie. Gdy spróbujesz scrobblować więcej, otrzymasz komunikat o błędzie. Planowane jest dodanie 'kolejki scrobble'i', więc jeśli musisz scrobblować więcej niż 2800 utworów, zostaną one dodane do kolejki i automatycznie scrobblowane po pewnym czasie. Możesz sprawdzić, ile scrobble'i Ci pozostało, w widoku wyboru użytkownika.

Po pomyślnym przesłaniu wszystkich rekordów na serwer, zobaczysz komunikat na dole okna aplikacji potwierdzający: 'Successfully scrobbled selected tracks.'

![Successfully scrobbled selected tracks.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Teraz możesz otworzyć swój profil na stronie [Last.fm](http://Last.fm) i sprawdzić wszystkie zmiany.

![Twój profil na stronie Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Najczęściej zadawane pytania

{{% details title="Czy mogę scrobblować automatycznie bez eksportowania plików CSV?" closed="true" %}}
Tak. Zarówno Evermusic, jak i Flacbox obsługują teraz automatyczne scrobblowanie do Last.fm. Zobacz przewodnik: [Jak scrobblować do Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Co jeśli mój CSV ma utwory starsze niż 14 dni?" closed="true" %}}
Użyj trybu importu w Last.fm-Scrubbler-WPF. Przelicza on znaczniki czasu na podstawie Finish Time, umożliwiając scrobblowanie utworów niezależnie od ich oryginalnej daty.
{{% /details %}}

{{% details title="Nie mam komputera z Windows. Czy nadal mogę używać Last.fm-Scrubbler?" closed="true" %}}
Tak. Zainstaluj VirtualBox na swoim Mac i pobierz bezpłatny obraz środowiska programistycznego Windows od Microsoft. Uruchom Last.fm-Scrubbler-WPF wewnątrz maszyny wirtualnej.
{{% /details %}}

{{% details title="Dlaczego niektóre scrobble nie zostały przeanalizowane?" closed="true" %}}
Utwory bez istotnych metadanych (takich jak nazwa artysty) nie mogą zostać przeanalizowane. Jest to oczekiwane i nie wpływa na inne utwory w pliku.
{{% /details %}}

{{% details title="Czy istnieje dzienny limit scrobble'i?" closed="true" %}}
Tak. Last.fm-Scrubbler-WPF pozwala na maksymalnie 2800 scrobble'i dziennie. Jeśli musisz scrobblować więcej, rozłóż proces na kilka dni.
{{% /details %}}
