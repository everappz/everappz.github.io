---
title: "Jak podłączyć pamięć NAS za pomocą WebDAV i słuchać muzyki na iPhonie lub Macu"
date: 2024-07-28
description: "Dowiedz się, jak skonfigurować WebDAV na serwerze Synology NAS i strumieniować muzykę na iPhone lub Mac za pomocą Evermusic lub Flacbox. Postępuj zgodnie z naszym przewodnikiem krok po kroku."
keywords: ["podłączyć nas", "webdav synology", "strumieniowanie muzyki nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["muzyka", "strumieniowanie", "pamięć", "nas", "połączenie", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**W skrócie:** Zainstaluj i włącz WebDAV na swoim Synology NAS, skonfiguruj uprawnienia folderu współdzielonego, a następnie połącz się z Evermusic lub Flacbox używając adresu IP NAS i portu WebDAV (domyślnie 5005/5006). Możesz strumieniować i zarządzać całą biblioteką muzyczną bez kopiowania plików na urządzenie.

Odkryj, jak podłączyć pamięć NAS za pomocą WebDAV i bez wysiłku strumieniować bibliotekę muzyczną na iPhone lub Mac. WebDAV (Web-based Distributed Authoring and Versioning) to protokół umożliwiający zarządzanie i udostępnianie plików przez Internet. Konfigurując WebDAV na NAS, możesz uzyskać dostęp do kolekcji muzycznej i strumieniować ją, mając zawsze ulubione utwory na wyciągnięcie ręki.

W tym przewodniku pokażemy, jak skonfigurować połączenie WebDAV na jednym z najpopularniejszych serwerów NAS, Synology NAS. Postępuj zgodnie z naszymi prostymi krokami, aby skonfigurować WebDAV na Synology NAS, a będziesz mógł przeglądać, strumieniować i zarządzać biblioteką muzyczną bezpośrednio z iPhone lub Mac.

## Krok 1: Zainstaluj WebDAV na Synology NAS

1. Zaloguj się do Synology NAS i otwórz **Centrum pakietów**.
2. Wyszukaj "webdav" i zainstaluj pakiet WebDAV, jeśli nie jest jeszcze zainstalowany. Otwórz serwer WebDAV, aby go skonfigurować.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Instalacja WebDAV na Synology" width="600" >}}

## Krok 2: Skonfiguruj serwer WebDAV

1. Na stronie ustawień WebDAV zaznacz pola **Włącz HTTP**, **Włącz HTTPS**, **Włącz anonimowy WebDAV** i **Włącz DavDepthInfinity**.
2. Kliknij **Zastosuj**, aby zapisać zmiany. Zanotuj numery portów dla połączeń HTTP i HTTPS, które domyślnie wynoszą 5005 i 5006.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Konfiguracja ustawień WebDAV" width="600" >}}

## Krok 3: Skonfiguruj uprawnienia folderu współdzielonego

1. Otwórz **Panel sterowania** i przejdź do sekcji **Folder współdzielony**.
2. Wybierz folder **Muzyka** i kliknij **Edytuj**.
3. Na karcie **Uprawnienia** skonfiguruj uprawnienia. Włącz dostęp dla gości z uprawnieniem Tylko do odczytu, jeśli chcesz tylko słuchać muzyki, lub Odczyt/Zapis, jeśli musisz modyfikować pliki. Zapisz zmiany.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Uprawnienia folderu współdzielonego" width="600" >}}

## Krok 4: Znajdź adres IP Synology NAS

1. Otwórz **Panel sterowania** i przejdź do karty **Interfejs sieciowy** lub użyj przeglądarki, aby odwiedzić [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Znajdź adres IP NAS" width="600" >}}

2. Zanotuj adres IP swojego Synology NAS (np. 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Adres IP Synology NAS" width="600" >}}

## Krok 5: Połącz się z Synology NAS za pomocą Evermusic/Flacbox

1. Otwórz aplikację Evermusic lub Flacbox i przejdź do karty **Połączenia**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Karta Połączenia w Evermusic" width="600" >}}

2. Aby połączyć się automatycznie, znajdź Synology NAS w sekcji **Dostępne urządzenia** i dotknij, aby się połączyć.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Lista dostępnych urządzeń" width="600" >}}

3. Aby połączyć się ręcznie, wybierz **Połącz z usługą chmurową** i wybierz **WebDAV**. Wpisz adres serwera w formacie: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (np. [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Ręczna konfiguracja WebDAV" width="600" >}}

4. Pozostaw pola loginu i hasła puste dla dostępu gościa lub wprowadź dane logowania Synology. Dotknij **Zaloguj się**.

## Krok 6: Przeglądaj i odtwarzaj muzykę

1. Po połączeniu urządzenie pojawi się na liście **Podłączone akcesoria**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Podłączone urządzenia w Evermusic" width="600" >}}

2. Przejdź do folderu **Muzyka** i dotknij dowolnego pliku audio, aby rozpocząć odtwarzanie.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Przeglądanie folderu z muzyką" width="600" >}}

## Krok 7: Dodaj podłączony folder chmurowy do biblioteki muzycznej

1. Otwórz sekcję **Biblioteka muzyczna** w aplikacji.
2. Wybierz **Dodaj muzykę** i wybierz **Połączenia**.
3. Wybierz podłączony serwer NAS i wybierz folder **Muzyka**. Dotknij **Zrobione**.
4. Aplikacja przeskanuje folder z muzyką i doda obsługiwane pliki audio do biblioteki muzycznej. Metadane zostaną załadowane, a utwory zostaną pogrupowane według albumu, wykonawcy i gatunku.

## Podsumowanie

Wykonując te kroki, możesz łatwo skonfigurować połączenie WebDAV na Synology NAS i strumieniować bibliotekę muzyczną na iPhone lub Mac za pomocą Evermusic lub Flacbox. Ciesz się bezproblemowym dostępem do ulubionych utworów w dowolnym momencie.

## Najczęściej zadawane pytania

{{% details title="Które urządzenia NAS obsługują WebDAV?" closed="true" %}}
Większość popularnych marek NAS obsługuje WebDAV, w tym Synology, QNAP, TrueNAS i Western Digital. Sprawdź dokumentację producenta NAS, aby uzyskać instrukcje konfiguracji WebDAV.
{{% /details %}}

{{% details title="Jaka jest różnica między WebDAV a SMB do strumieniowania muzyki z NAS?" closed="true" %}}
WebDAV działa przez HTTP/HTTPS i lepiej nadaje się do zdalnego dostępu przez Internet. SMB jest zazwyczaj szybszy w sieciach lokalnych. Evermusic i Flacbox obsługują oba protokoły, więc wybierz w zależności od tego, czy potrzebujesz dostępu lokalnego czy zdalnego.
{{% /details %}}

{{% details title="Czy potrzebuję nazwy użytkownika i hasła do WebDAV na Synology?" closed="true" %}}
Nie, jeśli włączysz anonimowy dostęp WebDAV i skonfigurujesz uprawnienia gościa w folderze współdzielonym. Dla lepszego bezpieczeństwa możesz użyć danych logowania Synology.
{{% /details %}}

{{% details title="Czy mogę strumieniować FLAC i inne formaty hi-res z NAS przez WebDAV?" closed="true" %}}
Tak. Zarówno Evermusic, jak i Flacbox obsługują FLAC, ALAC, WAV, DSD i inne formaty wysokiej rozdzielczości podczas strumieniowania z pamięci NAS przez WebDAV.
{{% /details %}}

{{% details title="Dlaczego aplikacja nie może znaleźć mojego NAS w Dostępnych urządzeniach?" closed="true" %}}
Upewnij się, że iPhone/Mac i NAS są w tej samej sieci Wi-Fi. Jeśli automatyczne wykrywanie nie działa, użyj opcji połączenia ręcznego i wpisz adres IP NAS i port WebDAV bezpośrednio.
{{% /details %}}
