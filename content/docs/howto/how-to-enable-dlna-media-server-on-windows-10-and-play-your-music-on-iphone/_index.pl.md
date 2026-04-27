---
title: "Jak włączyć serwer multimediów DLNA w Windows 10 i odtwarzać muzykę na iPhonie"
date: 2019-11-26
description: "Włącz serwer DLNA w Windows 10 i strumieniuj muzykę na iPhone za pomocą aplikacji Evermusic. Zawiera przewodnik konfiguracji krok po kroku."
keywords: ["evermusic", "dlna", "windows 10", "strumieniowanie muzyki na iphone", "serwer multimediów", "sieć lokalna", "upnp"]
tags: ["evermusic", "muzyka", "chmura", "iphone", "pamięć", "lokalny", "nas", "windows", "wifi", "słuchanie", "sieć", "zdalny", "dom", "online", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**W skrócie:** Windows 10 ma wbudowany serwer DLNA. Włącz go w ustawieniach Sieci i udostępniania, a następnie użyj darmowej aplikacji **Evermusic** na iPhonie, aby strumieniować całą bibliotekę muzyczną przez Wi-Fi. Nie jest potrzebne oprogramowanie serwera firm trzecich.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Okładka" caption="Strumieniowanie muzyki DLNA na iPhone za pomocą Windows 10 i Evermusic" width="800" >}}

DLNA (Digital Living Network Alliance) to potężne narzędzie, które umożliwia łatwe strumieniowanie różnych treści multimedialnych, w tym muzyki, między urządzeniami obsługującymi DLNA w Twojej sieci. Dobra wiadomość jest taka, że Windows 10 i wcześniejsze wersje mają wbudowaną funkcję DLNA, eliminując potrzebę serwerów multimediów firm trzecich. Oto jak włączyć serwer multimediów DLNA w Windows 10 i cieszyć się strumieniowaniem muzyki na iPhonie.

## Jak włączyć serwer multimediów DLNA w Windows 10

1. Kliknij przycisk 'Start'.  
2. Wybierz ikonę 'Ustawienia'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Konfiguracja serwera" caption="Otwórz Ustawienia Windows" width="500" >}}

3. Na ekranie 'Ustawienia Windows' wybierz 'Sieć i Internet'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Ustawienia Windows" caption="Wybierz Sieć i Internet" width="500" >}}

4. W sekcji 'Sieć' wybierz 'Centrum sieci i udostępniania'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Centrum udostępniania" caption="Otwórz Centrum sieci i udostępniania" width="500" >}}

5. Na ekranie 'Centrum sieci i udostępniania' kliknij 'Zmień zaawansowane ustawienia udostępniania' w menu po lewej.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Zaawansowane ustawienia udostępniania" caption="Zmień zaawansowane ustawienia udostępniania" width="500" >}}

6. Na ekranie 'Zaawansowane ustawienia udostępniania' przewiń w dół do sekcji 'Wszystkie sieci' i rozwiń ją, klikając strzałkę.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Włącz wykrywanie" caption="Rozwiń ustawienia wszystkich sieci" width="500" >}}

7. Kliknij 'Włącz strumieniowanie multimediów', aby aktywować serwer DLNA.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Włącz serwer" caption="Włącz serwer strumieniowania multimediów" width="500" >}}

8. Nadaj nazwę bibliotece multimediów i wybierz urządzenia, które mogą mieć do niej dostęp.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Nazwa biblioteki multimediów" caption="Nazwij swoją bibliotekę multimediów DLNA" width="500" >}}

9. Kliknij 'OK', aby potwierdzić. Teraz Twoje foldery osobiste jak Muzyka, Obrazy i Wideo będą widoczne dla każdego urządzenia strumieniującego z obsługą UPnP.

## Jak wyłączyć serwer multimediów DLNA w Windows 10

1. Kliknij 'Start' i wpisz 'services' w polu wyszukiwania.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Usługi Windows" caption="Otwórz Usługi Windows" width="500" >}}

2. Na ekranie 'Usługi' przewiń w dół, aby znaleźć 'Windows Media Player Network Sharing Service'.  
3. Kliknij dwukrotnie i ustaw 'Typ uruchomienia' na 'Ręczny'.  
4. Zatrzymaj usługę, klikając przycisk 'Zatrzymaj'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="Zatrzymaj usługę DLNA" caption="Wyłącz usługę udostępniania sieciowego DLNA" width="500" >}}

## Jak odtwarzać muzykę z serwera DLNA na iPhonie

1. Zainstaluj darmową aplikację **Evermusic** z App Store:  
   [Aplikacja Evermusic](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Otwórz kartę 'Połączenia' i dotknij 'Dostępne urządzenia' w sekcji 'Sieć lokalna'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Połączenia Evermusic" caption="Evermusic: ekran Połączenia" width="500" >}}

3. Poczekaj kilka sekund, aż lista urządzeń się załaduje i dotknij serwera Windows Media Player DLNA (np. 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Dostępne urządzenia" caption="Dostępne serwery DLNA w Evermusic" width="500" >}}

4. Zobaczysz listę folderów dostępnych na serwerze multimediów.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Foldery Evermusic" caption="Przeglądaj udostępnione foldery z serwera DLNA" width="500" >}}

5. Otwórz dowolny folder zawierający pliki audio.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Zawartość folderu" caption="Zobacz zawartość udostępnionych folderów DLNA" width="500" >}}

6. Dotknij dowolnego pliku, aby uruchomić odtwarzacz audio.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Odtwarzacz audio" caption="Odtwórz plik audio z DLNA w Evermusic" width="500" >}}

7. Aby poprawić wrażenia dźwiękowe, dotknij ikony 'Korektor' obok wskaźnika głośności na dole ekranu, aby włączyć korektor w stylu iPod z przedwzmacniaczem.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Korektor" caption="Użyj wbudowanego korektora dla lepszego odtwarzania" width="500" >}}

## Podsumowanie

Z serwerem multimediów DLNA w Windows 10 i Evermusic na iPhonie możesz cieszyć się płynnym strumieniowaniem muzyki z komputera na urządzenie mobilne. Pożegnaj ograniczenia pamięci i przywitaj muzykę na żądanie!

## Często zadawane pytania

{{% details title="Czy muszę instalować oprogramowanie serwera w Windows 10?" closed="true" %}}
Nie. Windows 10 zawiera wbudowany serwer multimediów DLNA. Wystarczy włączyć strumieniowanie multimediów w ustawieniach Centrum sieci i udostępniania. Nie jest wymagane oprogramowanie firm trzecich.
{{% /details %}}

{{% details title="Czy mój iPhone musi być w tej samej sieci Wi-Fi?" closed="true" %}}
Tak. Strumieniowanie DLNA działa w sieci lokalnej. Zarówno komputer z Windows 10, jak i iPhone muszą być podłączone do tej samej sieci Wi-Fi, aby Evermusic mógł wykryć serwer DLNA.
{{% /details %}}

{{% details title="Jakie formaty audio mogę strumieniować przez DLNA?" closed="true" %}}
Serwer Windows DLNA udostępnia pliki z folderu Muzyka niezależnie od formatu. Evermusic obsługuje MP3, FLAC, AAC, WAV, OGG, AIFF i wiele innych formatów, więc możesz odtwarzać praktycznie każdy plik audio z serwera.
{{% /details %}}

{{% details title="Czy mogę użyć Flacbox zamiast Evermusic?" closed="true" %}}
Tak. Flacbox również obsługuje przeglądanie i odtwarzanie DLNA/UPnP. Możesz użyć dowolnej z tych aplikacji do wykrywania i odtwarzania muzyki z serwera Windows DLNA.
{{% /details %}}

{{% details title="Czy strumieniowanie DLNA zużywa dane mobilne?" closed="true" %}}
Nie. DLNA działa wyłącznie w lokalnej sieci Wi-Fi. Nie zużywa żadnych danych mobilnych. Oba urządzenia muszą jednak pozostać podłączone do tej samej sieci podczas odtwarzania.
{{% /details %}}
