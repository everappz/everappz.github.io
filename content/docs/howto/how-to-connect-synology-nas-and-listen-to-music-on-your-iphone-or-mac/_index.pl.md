---
title: "Jak podłączyć Synology NAS i słuchać muzyki na iPhonie lub Macu"
date: 2024-09-19
description: "Dowiedz się, jak podłączyć Synology NAS za pomocą natywnego API lub QuickConnect i strumieniować muzykę wysokiej jakości na iPhone lub Mac za pomocą Evermusic i Flacbox."
keywords: ["synology nas", "strumieniowanie muzyki", "quickconnect", "evermusic synology", "flacbox synology", "odtwarzacz muzyki nas", "muzyka nas iphone"]
tags: ["muzyka", "strumieniowanie", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Podsumowanie:** Podłącz swój Synology NAS do Evermusic lub Flacbox za pomocą natywnego API Synology -- ręcznie przez adres IP lub automatycznie przez QuickConnect ID. QuickConnect pozwala strumieniować muzykę zdalnie bez przekierowania portów. Obie aplikacje obsługują FLAC, MP3, WAV i inne formaty hi-res.

Jeśli szukasz bezproblemowego sposobu na podłączenie Synology NAS i cieszenie się biblioteką muzyczną na iPhonie lub Macu, aplikacje Evermusic i Flacbox są idealnym rozwiązaniem. Aplikacje te obsługują szeroką gamę formatów audio, w tym FLAC, MP3 i WAV, co ułatwia strumieniowanie i słuchanie muzyki wysokiej jakości bezpośrednio z Synology NAS.

W tym przewodniku pokażemy, jak podłączyć Synology NAS do aplikacji Evermusic lub Flacbox za pomocą natywnego API Synology i funkcji QuickConnect. Wykorzystując bezpośrednie API Synology, możesz bezpiecznie uzyskać dostęp do swojej biblioteki muzycznej poza siecią domową bez potrzeby skomplikowanych konfiguracji, takich jak WebDAV, SMB, DLNA. Dzięki QuickConnect będziesz mógł strumieniować i zarządzać swoją muzyką z dowolnego miejsca, używając iPhone'a lub Maca.

## Krok 1: Skonfiguruj uprawnienia folderów udostępnionych (opcjonalnie)

1. Otwórz **Panel sterowania** i przejdź do sekcji **Folder udostępniony**.

![Folder udostępniony](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Wybierz folder **Music** i kliknij **Edytuj**.

3. W zakładce **Uprawnienia** skonfiguruj uprawnienia. Włącz dostęp gościnny z uprawnieniami Tylko do odczytu, jeśli chcesz tylko słuchać muzyki, lub Odczyt/Zapis, jeśli musisz modyfikować pliki. Zapisz zmiany.

![Uprawnienia](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Krok 2: Znajdź adres IP Synology NAS

1. Otwórz **Panel sterowania** i przejdź do zakładki **Interfejs sieciowy**.

![Interfejs sieciowy](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Lub użyj przeglądarki internetowej, aby odwiedzić [find.synology.com](http://find.synology.com).

![Znajdź Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Zanotuj adres IP Synology NAS (np. 192.168.18.137).

## Krok 3: Znajdź porty sieciowe Synology NAS

Oficjalną dokumentację Synology dotyczącą domyślnych portów sieciowych DSM znajdziesz w tym [artykule Centrum Wiedzy Synology](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM używa następujących domyślnych portów:
- **HTTP (Dostęp webowy):** Port **5000**
- **HTTPS (Bezpieczny dostęp webowy):** Port **5001**

Są to domyślne porty dostępu do interfejsu DSM.

![Porty sieciowe](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Krok 4: Włącz funkcję QuickConnect ID

Synology QuickConnect ID to unikalny identyfikator, który pozwala na zdalny dostęp do Synology NAS przez internet bez konieczności konfigurowania skomplikowanych ustawień sieciowych, takich jak przekierowanie portów. QuickConnect upraszcza zdalny dostęp, używając serwerów Synology do nawiązania połączenia między NAS a urządzeniem, takim jak smartfon lub komputer, za pośrednictwem QuickConnect ID.

**Jak znaleźć lub skonfigurować QuickConnect ID:**

1. **Zaloguj się do DSM.**
2. Przejdź do **Panel sterowania > Dostęp zewnętrzny > QuickConnect**.
3. **Włącz QuickConnect** i utwórz lub wyświetl swój unikalny QuickConnect ID.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Krok 5: Połącz się z Synology NAS na iPhonie/Macu za pomocą Evermusic lub Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) i [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) to aplikacje odtwarzaczy muzycznych zaprojektowane dla urządzeń iOS i macOS, z których każda oferuje unikalne funkcje i możliwości zarządzania i cieszenia się biblioteką muzyczną.

1. Otwórz aplikację Evermusic lub Flacbox i przejdź do zakładki **Połączenia**.

![Połączenia](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Wybierz **Połącz usługę chmurową** i wybierz **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Masz dwie opcje połączenia: **ręczne** przy użyciu adresu IP i portu serwera, lub **automatyczne** przez QuickConnect ID.

### Połączenie ręczne

W przypadku metody ręcznej potrzebny jest bezpośredni adres IP i numer portu uzyskany w poprzednich krokach.

1. Wprowadź URL serwera uzyskany w kroku 2, używając następującego formatu: PROTOKÓŁ://ADRES_IP:NUMER_PORTU
   - Użyj **portu 5000** dla HTTP i **portu 5001** dla połączeń HTTPS.

   Na przykład:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Rzeczywisty numer portu można potwierdzić w kroku 3 konfiguracji.
3. Wprowadź swój **login** i **hasło** do Synology NAS.
4. Stuknij **Zaloguj się**, aby nawiązać połączenie.

![Połączenie ręczne](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Połączenie automatyczne

W przypadku połączenia automatycznego użyjesz **QuickConnect ID** z kroku 4. Zamiast ręcznie wprowadzać adres IP i numer portu Synology NAS, wystarczy wpisać **QuickConnect ID**. Aplikacja automatycznie pobierze niezbędne informacje o połączeniu.

Ta metoda pozwala na zdalny dostęp do NAS, nawet poza siecią domową, dzięki czemu możesz zarządzać plikami z internetu bez konieczności konfigurowania przekierowania portów lub statycznych adresów IP.

![Połączenie automatyczne](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Uwierzytelnianie dwuskładnikowe

Począwszy od DSM 4.2, Synology wprowadziło **weryfikację dwuetapową** w celu zwiększenia bezpieczeństwa. Ta funkcja wymaga kodu **jednorazowego hasła (OTP)**, generowanego przez aplikację uwierzytelniającą, oprócz zwykłych danych logowania. Jeśli włączyłeś weryfikację dwuetapową, po wprowadzeniu nazwy użytkownika i hasła musisz również podać OTP, aby zalogować się do sesji DSM.

Pamiętaj, że po wygaśnięciu sesji aplikacja będzie musiała zostać ręcznie ponownie autoryzowana. Aby ponownie autoryzować:

1. Przejdź do zakładki **Połączenia** w aplikacji.
2. Stuknij przycisk **Więcej akcji** obok nazwy serwera.
3. Wybierz **Ustawienia** z menu, aby wprowadzić nowy kod uwierzytelniający i zakończyć proces ponownej autoryzacji.

Zapewnia to bezpieczeństwo danych nawet w przypadku dostępu do NAS z niezaufanej sieci.

## Krok 6: Przeglądaj i odtwarzaj muzykę

1. Po połączeniu urządzenie pojawi się na liście **Podłączone urządzenia**.

![Podłączone urządzenia](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Przejdź do folderu **Music** i stuknij dowolny plik audio, aby rozpocząć odtwarzanie.

![Odtwarzaj muzykę](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Krok 7: Dodaj połączony folder chmurowy do biblioteki muzycznej

1. Otwórz sekcję **Biblioteka muzyczna** w aplikacji.
2. Wybierz **Dodaj muzykę** i wybierz **Połączenia**.
3. Wybierz połączony serwer NAS i wybierz folder **Music**. Stuknij **Zrobione**.
4. Aplikacja przeskanuje folder muzyczny i doda obsługiwane pliki audio do biblioteki muzycznej. Metadane zostaną załadowane, a utwory zostaną pogrupowane według albumu, artysty i gatunku.

## Podsumowanie

Postępując zgodnie z tymi krokami, możesz łatwo skonfigurować połączenie na Synology NAS i strumieniować całą bibliotekę muzyczną na iPhone lub Mac za pomocą Evermusic lub Flacbox. Niezależnie od tego, czy jesteś w domu, czy w podróży, ciesz się bezproblemowym dostępem do ulubionych utworów w wysokiej jakości z dowolnego miejsca dzięki QuickConnect. Skorzystaj z elastyczności i wygody oferowanej przez te aplikacje i zacznij łatwo zarządzać kolekcją muzyczną na wszystkich swoich urządzeniach.

Dzięki bezpiecznemu zdalnemu dostępowi przez QuickConnect i obsłudze szerokiej gamy formatów audio, nigdy nie będziesz daleko od swojej muzyki. Teraz pliki przechowywane na NAS są na wyciągnięcie ręki!

## FAQ

{{% details title="Jaka jest różnica między połączeniem ręcznym a QuickConnect?" closed="true" %}}
Połączenie ręczne wykorzystuje adres IP i port NAS, co działa w sieci lokalnej. QuickConnect używa usługi przekaźnikowej Synology do nawiązania połączenia z dowolnego miejsca przez internet, bez przekierowania portów.
{{% /details %}}

{{% details title="Czy mogę strumieniować muzykę z Synology NAS poza siecią domową?" closed="true" %}}
Tak. Włącz QuickConnect na Synology NAS i użyj QuickConnect ID w Evermusic lub Flacbox, aby strumieniować muzykę z dowolnego miejsca z połączeniem internetowym.
{{% /details %}}

{{% details title="Jakie formaty audio są obsługiwane podczas strumieniowania z Synology NAS?" closed="true" %}}
Evermusic i Flacbox obsługują FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD i wiele innych formatów. Wszystkie obsługiwane formaty działają podczas strumieniowania z Synology NAS.
{{% /details %}}

{{% details title="Czy potrzebuję uwierzytelniania dwuskładnikowego, aby się połączyć?" closed="true" %}}
Nie, 2FA jest opcjonalne. Jednak jeśli włączyłeś weryfikację dwuetapową na Synology DSM, aplikacja poprosi o jednorazowe hasło podczas logowania. Będziesz musiał ponownie autoryzować po wygaśnięciu sesji.
{{% /details %}}

{{% details title="Czy powinienem użyć natywnego API Synology, WebDAV czy SMB do połączenia?" closed="true" %}}
Natywne API Synology z QuickConnect to najlepszy wybór do zdalnego dostępu. Do użytku w sieci lokalnej SMB jest zazwyczaj najszybszą opcją. WebDAV dobrze sprawdza się zarówno w dostępie lokalnym, jak i zdalnym. Evermusic i Flacbox obsługują wszystkie trzy protokoły.
{{% /details %}}
