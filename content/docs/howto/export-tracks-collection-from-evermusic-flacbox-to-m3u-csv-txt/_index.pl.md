---
title: "Jak eksportować kolekcję utworów do M3U, CSV i TXT w Evermusic i Flacbox"
date: 2024-01-31
description: "Dowiedz się, jak eksportować ostatnie, ulubione, playlisty i albumy z Evermusic i Flacbox do formatów M3U, CSV lub TXT. Idealne do scrobblowania na Last.fm i odtwarzania na innych urządzeniach."
keywords: ["evermusic eksport", "flacbox eksport", "eksport do m3u", "eksport playlisty do csv", "m3u txt csv playlista", "eksport muzyki"]
tags: ["evermusic", "recents", "favorites", "export", "m3u", "playlist", "csv", "txt", "album"]
---

{{< author-byline >}}


**W skrócie:** Evermusic i Flacbox pozwalają eksportować dowolną kolekcję utworów (ostatnie, ulubione, playlisty, albumy) do plików CSV, TXT lub M3U. Używaj tych eksportów do scrobblowania na Last.fm, tworzenia kopii zapasowej biblioteki lub odtwarzania playlist na innych urządzeniach.

## Wprowadzenie

Eksportowanie ostatnich, ulubionych, albumów i playlist z aplikacji do pliku zewnętrznego może być niezwykle przydatne. Możesz używać tych plików do aktualizacji historii odsłuchów w serwisach scrobblerowych, takich jak [Last.fm](http://Last.fm), lub do słuchania swoich playlist na zewnętrznych urządzeniach. W Evermusic i Flacbox ten proces jest prosty. Tutaj pokażemy, jak eksportować ostatnie do CSV/TXT i playlisty do M3U. Funkcjonalność ta jest jednak dostępna dla każdej kolekcji utworów w aplikacji.

## Wybierz format

Aby eksportować ostatnie, otwórz sekcję «Biblioteka muzyczna» i wybierz element menu «Ostatnie».

![biblioteka muzyczna](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Na następnym ekranie naciśnij przycisk «Więcej» w prawym górnym rogu i wybierz «Eksportuj listę utworów».

![eksportuj ostatnie](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

Na ekranie «Wybierz format pliku» masz kilka opcji – CSV, TXT, M3U.

- CSV

To skrót od Comma-Separated Values, idealny do organizowania danych w schludnym formacie tabelarycznym. W pliku docelowym znajdziesz takie parametry jak nazwa artysty, nazwa albumu, nazwa utworu, znacznik czasu (czas odsłuchu utworów), nazwa artysty albumu i czas trwania utworu. Możesz później użyć tego pliku do aktualizacji historii odsłuchów w serwisach scrobblerowych, takich jak [Last.fm](http://Last.fm), jak opisano [tutaj](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Tutaj mówimy o zwykłym pliku tekstowym. Jest prosty i przejrzysty, z parametrami takimi jak nazwa artysty, nazwa albumu, nazwa utworu i czas trwania. Przydatny, jeśli potrzebujesz jedynie listy utworów w formie tekstowej.

- M3U

Ten format jest w zasadzie standardem tworzenia playlist. Jest świetny, ponieważ możesz wyeksportować listę utworów i cieszyć się nimi na dowolnym urządzeniu, nawet jeśli nie masz oryginalnych plików (jeśli wybierzesz opcję eksportu z bezwzględnym URL plików multimedialnych). W pliku wyjściowym znajdziesz parametry takie jak czas trwania, nazwa artysty, nazwa utworu i lokalizacja pliku multimedialnego.

## Format CSV

Teraz wybierzmy CSV i zobaczmy, co otrzymamy. Po prostu wybierz CSV i naciśnij przycisk «Eksportuj».

![wybierz format pliku](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Po zakończeniu eksportu zobaczysz alert z dwiema opcjami. Naciśnięcie «Pokaż plik» wyświetli wynikowy plik w katalogu dokumentów.

![eksport zakończony](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Teraz możesz wysłać ten plik, otworzyć go w zewnętrznym edytorze tekstu lub użyć do aktualizacji postępów odsłuchów na [Last.fm](http://Last.fm).

![folder eksportu z plikami wynikowymi](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

Wyjściowy plik CSV będzie zawierał pola w następującym formacie:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Na przykład:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![wyeksportowany plik csv](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## Format TXT

Wyjściowy plik TXT będzie zawierał pola w następującym formacie:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Na przykład:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![wyeksportowany plik txt](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## Format M3U

Teraz przeprowadzimy Cię przez eksport playlisty do formatu M3U, który jest de facto standardem plików playlist. Głównym warunkiem pomyślnego eksportu playlisty jest to, że wszystkie pliki w playliście muszą znajdować się na tym samym nośniku, niezależnie od tego, czy jest to usługa chmurowa, taka jak Google Drive, pliki lokalne czy pliki na urządzeniu. Aby rozpocząć proces eksportu, otwórz dowolną playlistę i naciśnij przycisk «Więcej» w prawym górnym rogu, a następnie wybierz element menu «Eksportuj listę utworów».

![ekran playlisty](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Na następnym ekranie wybierz format pliku «M3U», gdzie napotkasz dwie opcje «Typ lokalizacji pliku multimedialnego»:

![ekran wyboru formatu eksportu](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Jeśli wybierzesz «Ścieżka względna», playlista zostanie utworzona z lokalizacjami plików multimedialnych zapisanymi względem pliku playlisty. Na przykład:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   W tym przypadku unikaj zmiany lokalizacji pliku M3U po zakończeniu eksportu, ponieważ spowoduje to uszkodzenie ścieżek do plików multimedialnych. Aby rozpocząć odtwarzanie playlisty, po prostu naciśnij wyeksportowany plik playlisty, a aplikacja automatycznie zlokalizuje pliki multimedialne na Twoim nośniku i rozpocznie odtwarzanie. Możesz nawet wyeksportować playlisty do chmury, a następnie zaimportować je ponownie na nowym urządzeniu.

2. Jeśli wybierzesz «Bezwzględny URL», aplikacja wygeneruje bezpośrednie adresy URL plików multimedialnych. Pozwala to na odtwarzanie playlisty na dowolnym urządzeniu/aplikacji bez konieczności umieszczania wszystkich plików multimedialnych na tym samym nośniku co plik playlisty. Ta opcja jest obsługiwana tylko dla chmury zdolnej do generowania bezpośrednich adresów URL plików. Należy jednak pamiętać, że w niektórych przypadkach wygenerowane adresy URL mogą mieć ograniczony czas życia i mogą wygasnąć po pewnym czasie. Oto lista obsługiwanych usług chmurowych: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (w trybie gościa)  

Wynikowy adres URL pliku multimedialnego będzie wyglądał mniej więcej tak:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Po wybraniu «Typu lokalizacji pliku multimedialnego» naciśnij «Eksportuj». Aplikacja poprosi o wybranie folderu docelowego do eksportu pliku M3U. Naciśnij «Zrobione», aby potwierdzić wybór.

![wybierz folder](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Aplikacja wygeneruje plik M3U i prześle/przeniesie go do folderu docelowego.

![przesyłanie pliku m3u](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Po zakończeniu eksportu pojawi się alert systemowy z opcją «Pokaż plik».

![alert eksport zakończony](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Naciśnięcie go wyświetli wyeksportowany plik w aplikacji.

![wyeksportowany plik m3u na liście plików](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Jeśli w poprzednim kroku wybrałeś «Ścieżka względna» jako «Typ lokalizacji pliku multimedialnego», plik wyjściowy będzie w następującym formacie:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![przykład m3u ze ścieżkami względnymi](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Dla opcji «Bezwzględny URL» aplikacja wygeneruje plik M3U w formacie:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![przykład m3u z bezwzględnymi URL plików](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Możesz otworzyć ten plik na dowolnym urządzeniu/aplikacji obsługującej playlisty M3U.

![playlista m3u otwarta w zewnętrznej aplikacji](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Podsumowanie

Eksportowanie utworów z Evermusic i Flacbox daje Ci pełną kontrolę nad danymi muzycznymi. Niezależnie od tego, czy tworzysz kopię zapasową historii odsłuchów, scroblujesz na Last.fm, czy cieszysz się playlistami na zewnętrznych urządzeniach, te opcje eksportu – M3U, CSV i TXT – to potężne narzędzia dostosowane do elastyczności i kompatybilności. Skorzystaj z tych funkcji, aby usprawnić sposób organizowania, udostępniania i ponownego odkrywania kolekcji muzycznej na różnych platformach.

## FAQ

{{% details title="Jakiego formatu eksportu powinienem użyć do scrobblowania na Last.fm?" closed="true" %}}
Użyj CSV. Zawiera znaczniki czasu i pełne metadane wymagane przez narzędzia scrobblerowe, takie jak Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Czy mogę eksportować dowolną kolekcję utworów, nie tylko playlisty?" closed="true" %}}
Tak. Możesz eksportować ostatnie, ulubione, albumy, playlisty i każdą inną kolekcję utworów w aplikacji, korzystając z tych samych kroków.
{{% /details %}}

{{% details title="Czy moja playlista M3U będzie działać na innych urządzeniach?" closed="true" %}}
Jeśli podczas eksportu wybierzesz opcję Bezwzględny URL, plik M3U można odtwarzać na dowolnym urządzeniu obsługującym playlisty M3U. Pamiętaj, że niektóre adresy URL chmury mogą wygasnąć z czasem.
{{% /details %}}

{{% details title="Czy funkcja eksportu jest bezpłatna?" closed="true" %}}
Tak. Eksport kolekcji utworów do M3U, CSV i TXT jest dostępny zarówno w wersji bezpłatnej, jak i premium Evermusic i Flacbox.
{{% /details %}}

{{% details title="Jakie usługi chmurowe obsługują eksport z bezwzględnym URL?" closed="true" %}}
Eksport z bezwzględnym URL jest obsługiwany dla iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive i WebDAV (tryb gościa).
{{% /details %}}
