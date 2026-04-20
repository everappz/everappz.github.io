---
date: '2025-06-12T17:00:00+00:00'
draft: false
title: 'Często zadawane pytania'
description: 'Znajdź odpowiedzi na często zadawane pytania dotyczące Evermusic, Flacbox, Evervideo i Evertag. Poznaj funkcje takie jak streaming w chmurze, zarządzanie plikami, opcje odtwarzania, edycja metadanych i więcej.'
keywords: [
  "Evermusic FAQ", "wsparcie Flacbox", "pomoc Evervideo", "pytania Evertag",
  "jak używać Evermusic", "rozwiązywanie problemów z odtwarzaczem muzyki w chmurze", "przewodnik po odtwarzaniu offline",
  "wsparcie edytora tagów audio", "problemy ze strumieniowaniem wideo", "samouczek transferu plików"
]
tags: [
  "FAQ", "pomoc", "wsparcie", "evermusic", "flacbox", "evervideo", "evertag",
  "konfiguracja chmury", "problemy z odtwarzaniem", "zarządzanie plikami", "edycja metadanych",
  "rozwiązywanie problemów", "tryb offline", "odtwarzacz muzyki", "odtwarzacz wideo"
]
aliases:
  - /blog/categories/how-to/
---


{{< lottie src="/images/juicy-json/juicy-woman-focused-on-online-learning.json" width="85%" >}}

## Dowiedz się, jak korzystać z naszych aplikacji

Szukasz odpowiedzi lub pomocy przy korzystaniu z jednej z naszych aplikacji? Jesteś we właściwym miejscu.

Nasze strony FAQ pomogą Ci połączyć przechowywanie w chmurze, zarządzać plikami muzycznymi i wideo, skonfigurować odtwarzanie offline, dostosować ustawienia equalizera, naprawić metadane i nie tylko.

Przeglądaj FAQ dla swojej aplikacji poniżej, aby zacząć, lub przejrzyj typowe pytania i odpowiedzi, które otrzymaliśmy od użytkowników.

## Wybierz swoją aplikację

{{< cards cols="2">}}

{{< card 
  link="/docs/faq/evervideo" 
  title="Evervideo" 
  subtitle="Odtwarzaj filmy 360°, streamuj z iCloud, oglądaj z napisami, używaj equalizera wideo, organizuj zawartość za pomocą list odtwarzania i pobieraj filmy do oglądania offline."
  image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< card 
  link="/docs/faq/evermusic"
  title="Evermusic" 
  subtitle="Odtwarzacz muzyki w chmurze z trybem offline, equalizerem audio, crossfade, bezszwowym odtwarzaniem, zarządzaniem listami odtwarzania, pełną biblioteką muzyczną i wbudowanym menedżerem plików."
  image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/flacbox"
  title="Flacbox" 
  subtitle="Odtwarzacz audio wysokiej rozdzielczości dla iPhone i Mac. Słuchaj bezstratnych formatów takich jak FLAC, ALAC, APE i DSD. Doprecyzuj wyjście za pomocą zaawansowanych ustawień audio."
  image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/evertag"
  title="Evertag" 
  subtitle="Inteligentny edytor tagów muzycznych z edycją wsadową. Napraw brakujące metadane, okładki albumów i więcej. Edytuj tagi ID3, FLAC, APE — obsługiwanych ponad 120 pól." 
  image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< /cards >}}

## Typowe problemy i odpowiedzi

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{% details title="Dlaczego nie mogę zalogować się do pCloud na starszej wersji iOS (15.8.4)?" closed="true" %}}
Strona logowania pCloud może nie wyświetlać się poprawnie na starszych wersjach iOS, takich jak 15.8.4, co uniemożliwia wpisanie adresu e-mail i hasła w ekranie połączenia z chmurą.<br><br>

Jako obejście możesz użyć protokołu **WebDAV**, który jest obsługiwany przez pCloud i działa niezawodnie we wszystkich wersjach iOS.

**Konfiguracja WebDAV:**<br>
- **Serwery USA:** `https://webdav.pcloud.com`  
- **Serwery europejskie:** `https://ewebdav.pcloud.com`  
- **Nazwa użytkownika:** Twój adres e-mail pCloud  
- **Hasło:** Hasło do konta pCloud  

Otwórz aplikację → Połączenia → Połącz z przechowywaniem w chmurze → Wybierz **WebDAV** → Wpisz swoje dane i adres URL serwera.

Ta metoda pozwoli Ci połączyć się z pamięcią pCloud i mieć dostęp do swoich plików bez problemów na starszych urządzeniach.
{{% /details %}}

{{% details title="Jak odtwarzać muzykę przez AirPlay z Mac (macOS)?" closed="true" %}}
Wersja macOS aplikacji nie zawiera wbudowanych przycisków połączenia AirPlay, Chromecast ani Bluetooth jak w iOS.<br><br>

Aby używać **AirPlay** na MacBook Pro, wykonaj następujące kroki:

1. Przejdź do **prawego górnego rogu** ekranu i otwórz **Centrum sterowania** (przy zegarze).  
2. Kliknij ikonę **Dźwięk/Głośność**.  
3. Na następnym ekranie kliknij **AirPlay**, aby wyświetlić listę wszystkich dostępnych urządzeń AirPlay.  
4. Wybierz żądane urządzenie, aby rozpocząć strumieniowanie muzyki.  

Spowoduje to przekierowanie całego dźwięku systemowego (w tym z Evermusic lub Flacbox) do wybranego urządzenia AirPlay.
{{% /details %}}

{{% details title="Dlaczego mój zakup Premium nie jest aktywowany na Mac, jeśli kupiłem go na iPhone?" closed="true" %}}
Zakupy dożywotnie i subskrypcje są synchronizowane między iOS i Mac za pośrednictwem **iCloud**.<br><br>

Aby aktywować Premium na Mac:<br>
- Upewnij się, że masz najnowszą wersję aplikacji zainstalowaną na obu urządzeniach<br>
- Włącz **iCloud** na obu urządzeniach<br>
- Uruchom aplikację na urządzeniu iOS i poczekaj 1 minutę na przesłanie informacji o zakupie<br>
- Na Macu zainstaluj aplikację z App Store używając tego samego **Apple ID**<br>
- Uruchom aplikację i poczekaj kilka sekund na synchronizację informacji<br>
- Możesz też dotknąć **Przywróć zakupy** w ustawieniach aplikacji na obu urządzeniach<br><br>

Funkcje Premium powinny wtedy automatycznie aktywować się na Mac.
{{% /details %}}

{{% details title="Jak mogę automatycznie synchronizować listy odtwarzania między urządzeniami?" closed="true" %}}
Obecnie **nie ma automatycznej synchronizacji** list odtwarzania.<br><br>

Możesz użyć jednej z następujących opcji:<br>
- **Kopia zapasowa i przywracanie** z ustawień aplikacji [Jak przenieść bibliotekę muzyczną między urządzeniami w Evermusic: Przewodnik krok po kroku](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/)<br>
- **Eksportuj listę odtwarzania do M3U**, a następnie zaimportuj na innym urządzeniu:<br>
  - [Jak eksportować listy odtwarzania](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/)<br>
  - [Jak importować listy odtwarzania](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/)<br>
- **Archiwizuj listę odtwarzania lub albumy** i przenieś przez ZIP:<br>
  - [Przewodnik archiwizacji listy odtwarzania](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to/)
{{% /details %}}

{{% details title="Czy korzystanie z waszych aplikacji jest bezpieczne? Czy mogę wyłączyć analitykę?" closed="true" %}}
Tak, Twoja prywatność jest naszym najwyższym priorytetem.<br><br>

- Wszystkie dane — pliki muzyczne, ustawienia, loginy do chmury — pozostają na Twoim urządzeniu<br>
- Dane logowania są bezpiecznie przechowywane w **iOS Keychain**<br>
- Zbieramy tylko anonimowe raporty awarii i użytkowania<br>
- Możesz zrezygnować w **Ustawieniach aplikacji → Analityka**<br><br>

Więcej informacji:<br>
- [Polityka prywatności](/legal/privacy-policy/)<br>
- [Bezpieczeństwo Apple Keychain](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web)<br><br>

Jeśli używasz spersonalizowanych reklam, Google Mobile Ads wymaga wyświetlenia ustawień zgody.<br>
Użytkownicy Premium nie widzą reklam, a SDK reklam jest całkowicie wyłączony.
{{% /details %}}

{{% details title="Czy wasze aplikacje obsługują Udostępnianie rodzinne?" closed="true" %}}
Tak, Udostępnianie rodzinne jest obsługiwane.<br><br>

Aby udostępniać zakupy w aplikacji:<br>
- Upewnij się, że zakup jest ustawiony do udostępnienia grupie rodzinnej<br>
- Na urządzeniu członka rodziny przejdź do **Ustawienia > Zakupy > Przywróć zakupy**<br>
- Spowoduje to pobranie danych zakupu z serwerów Apple i aktywację na ich urządzeniu
{{% /details %}}

{{% details title="Jak przyspieszyć metadane i synchronizację z chmurą?" closed="true" %}}
Aby poprawić szybkość synchronizacji, włącz zadania w tle:<br><br>

- **Ustawienia → Biblioteka muzyczna → Odczyt metadanych → Odczyt metadanych w tle**<br>
- **Ustawienia → Biblioteka muzyczna → Synchronizacja muzyki online → Synchronizacja w tle**<br><br>

Ponadto na macOS zwiększ szybkość odczytu metadanych przez **Ustawienia → Biblioteka muzyczna**.<br>
Jeśli odtwarzacz jest aktywny (odtwarzanie audio), iOS nie zawiesi aplikacji, umożliwiając ciągłą synchronizację.
{{% /details %}}

{{% details title="Jak mogę anulować subskrypcję?" closed="true" %}}
Możesz anulować subskrypcję zgodnie z oficjalnymi instrukcjami Apple:<br>
👉 [Jak anulować subskrypcję](https://support.apple.com/en-us/118428)
{{% /details %}}

{{% details title="Jak połączyć się i streamować audio z WD MyCloud EX2 Ultra?" closed="true" %}}

Gdy dodajesz połączenie w aplikacji przez **Połączenia > Połącz z przechowywaniem w chmurze > My Cloud Home**, jest ono oficjalnie zaprojektowane do obsługi urządzeń **WD MyCloud Home**.<br>
WD MyCloud EX2 Ultra używa ograniczonego dostępu dla aplikacji.<br><br>

Jeśli jednak udało Ci się połączyć z **WD MyCloud EX2 Ultra**, **WD MyCloud Mirror** lub innym modelem pamięci **WD MyCloud**, możesz nadal go używać z następującym obejściem:<br><br>

1. Otwórz **Połączenia → Połącz z przechowywaniem w chmurze → My Cloud Home**<br>
2. Utwórz folder za pomocą wbudowanego menedżera plików<br>
3. Prześlij pliki muzyczne do tego folderu<br>
4. Zostaną one przechowane w „piaskownicy" dostępnej tylko dla aplikacji<br>
5. Możesz teraz streamować lub pobierać je bezpośrednio<br><br>

⚠️ Tylko foldery utworzone przez aplikację będą dostępne z NAS.
{{% /details %}}

{{% details title="Jak połączyć się z Koofr.eu?" closed="true" %}}
Możesz połączyć się z Koofr za pomocą **WebDAV**.<br><br>

- Przewodnik konfiguracji Koofr WebDAV: [blog koofr.eu](https://koofr.eu/blog/posts/3-ways-to-map-koofr-as-a-network-drive-explained)<br>
- Przewodnik WebDAV Evermusic/Flacbox: [Jak połączyć pamięć NAS za pomocą WebDAV i słuchać muzyki na iPhone lub Mac](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)
{{% /details %}}

{{% details title="Jakie są schematy URL aplikacji?" closed="true" %}}
Oto obsługiwane schematy:<br><br>

**Evermusic**<br>
- iOS (niebieska ikona): `lsevermusic://`<br>
- macOS: `lsevermusicmac://`<br>
- iOS (czerwona ikona): `lsevermusicpro://`<br><br>

**Flacbox**<br>
- iOS: `lsflap://`<br>
- macOS: `lsflapmac://`<br><br>

**Evertag**<br>
- iOS: `lsevertag://`<br>
- macOS: `lsevertagmac://`<br><br>

**Evervideo**<br>
- iOS: `lsevervideo://`<br>
- macOS: `lsevervideomac://`
{{% /details %}}

{{% details title="Muzyka przestaje grać, gdy aplikacja jest w tle — jak naprawić?" closed="true" %}}
Jeśli aplikacja zawiesza się lub zatrzymuje w tle:<br>
- Przejdź do **Ustawienia > Biblioteka muzyczna > Synchronizacja muzyki online > Synchronizacja w tle → Wyłącz**<br>
- **Ustawienia > Biblioteka muzyczna > Odczyt metadanych > Odczyt metadanych w tle → Wyłącz**<br>
- **Ustawienia > Menedżer plików > Przesyłanie w tle → Wyłącz**
{{% /details %}}

{{% details title="Bezszwowe odtwarzanie nie działa — jak naprawić?" closed="true" %}}
Bezszwowe odtwarzanie zależy od wersji iOS i silnika audio.<br>
Spróbuj przełączyć silnik audio:<br>
- Przejdź do **Ustawienia → Odtwarzacz audio → Ogólne → Procesor audio**<br>
- Wybierz **Core Audio** dla lepszej obsługi bezszwowego odtwarzania
{{% /details %}}

{{% details title="Dlaczego aplikacja wyświetla tylko 100 elementów na liście?" closed="true" %}}
Aplikacja używa stronicowania dla wydajności.<br>
Aby to wyłączyć:<br>
- Przejdź do **Ustawienia → Personalizacja → Limit ładowania zawartości → Dezaktywowany**<br>
Teraz wszystkie elementy będą ładowane jednocześnie.
{{% /details %}}

{{% details title="Dlaczego w metadanych są dziwne znaki?" closed="true" %}}
Spróbuj włączyć normalizację metadanych:<br>
- **Ustawienia → Biblioteka muzyczna → Odczyt metadanych → Normalizuj kodowanie metadanych**
{{% /details %}}

{{% details title="Dlaczego aplikacja nie może odczytać nazw folderów ze znakami specjalnymi?" closed="true" %}}
To znany problem z **protokołem SMB2**.<br><br>

Wypróbuj następujące rozwiązania:<br>
- Włącz **SMB1** na serwerze i w ustawieniach aplikacji<br>
- Użyj **selektora plików systemowych**:<br>
  - Przejdź do **Pliki lokalne > Pliki na tym urządzeniu > Otwórz pliki...**<br>
  - Wybierz foldery/pliki za pomocą natywnego menu Apple<br><br>

Ewentualnie połącz się za pomocą **WebDAV** lub **DLNA**, jeśli Twój NAS je obsługuje.
{{% /details %}}

{{% details title="Jak przesyłać i zarządzać muzyką w iCloud?" closed="true" %}}
– **Jak przesłać muzykę do iCloud?**  <br>
Przejdź do [https://www.icloud.com](https://www.icloud.com) w przeglądarce, utwórz folder i prześlij pliki muzyczne bezpośrednio z Mac lub PC.<br>

– **Jak zarządzać pamięcią iCloud?**  <br>
Masz dwie opcje:  <br>
1. Użyj [https://www.icloud.com](https://www.icloud.com) w przeglądarce, aby organizować, przesyłać lub usuwać pliki.<br>  
2. W aplikacji, po połączeniu z iCloud przez **Połączenia → Połącz z przechowywaniem w chmurze → iCloud Drive**, użyj wbudowanego menedżera plików do przesyłania, pobierania, zmiany nazw folderów lub usuwania plików bezpośrednio w swojej pamięci iCloud — bez zapisywania ich na urządzeniu.<br>

⚠️ Zachowaj ostrożność podczas usuwania plików. Aplikacja usuwa je trwale (nie trafią do kosza i nie można ich odzyskać).<br>

Dowiedz się więcej tutaj: [Jak streamować muzykę z iCloud Drive na iPhone lub Mac](/docs/howto/how-to-listen-to-music-from-icloud-drive-on-your-iphone-or-mac/)

{{% /details %}}

{{% details title="Jak przenieść bibliotekę muzyczną 10 GB z Windows 11 na iPhone do odtwarzania offline?" closed="true" %}}

Masz kilka niezawodnych opcji przeniesienia biblioteki muzycznej z PC z Windows 11 na iPhone i korzystania z niej offline w aplikacji. Wybierz metodę, która najlepiej Ci odpowiada:

1. **Używanie połączenia kablowego (zalecane dla dużych bibliotek)**  <br>
   Użyj aplikacji **Apple Devices** na Windows 11, aby przesyłać pliki bezpośrednio na iPhone przez USB.  
   Postępuj zgodnie z przewodnikiem Apple tutaj:  
   https://support.apple.com/en-ph/120402 <br>

2. **Bezprzewodowo przez Wi-Fi Drive**  <br>
   Włącz funkcję **WiFi Drive** w aplikacji i prześlij muzykę przez przeglądarkę na komputerze.  
   Instrukcje krok po kroku tutaj:  
   [Jak przenosić pliki muzyczne z komputera na iPhone bez iTunes za pomocą WiFi-Drive](/docs/howto/how-to-transfer-music-from-computer-to-iphone-without-itunes/) <br>

3. **Bezprzewodowo za pomocą serwera DLNA**  <br>
   Włącz serwer mediów DLNA na komputerze Windows i streamuj lub przenoś bibliotekę bezpośrednio do aplikacji.  
   Przewodnik:  
   [Jak włączyć serwer mediów DLNA w Windows 10 i odtwarzać muzykę na iPhone](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/) <br>

4. **Bezprzewodowo za pomocą udostępniania plików SMB**  <br>
   Włącz **udostępnianie plików SMB** na PC i połącz się z nim w aplikacji, aby przeglądać, pobierać lub przenosić pliki folder po folderze.  
   Instrukcje:  
   [Przenoś pliki z komputera na iPhone za pomocą protokołu SMB](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/) <br>

⚠️ Podczas przenoszenia dużych bibliotek (10 GB+), przewodowy transfer USB jest zazwyczaj najszybszą i najbardziej stabilną opcją.

{{% /details %}}

</div>
