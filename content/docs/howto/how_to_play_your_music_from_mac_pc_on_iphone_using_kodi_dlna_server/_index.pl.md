---
title: "Jak odtwarzać muzykę z Mac / PC / Linux / NAS na iPhonie za pomocą serwera Kodi DLNA"
date: 2025-07-25
description: "Strumieniuj muzykę z komputera lub NAS na iPhone przez Wi-Fi za pomocą Kodi DLNA i aplikacji Evermusic."
keywords: ["serwer kodi dlna", "strumieniowanie muzyki na iphone", "odtwarzanie muzyki z nas", "evermusic dlna", "muzyka z mac na iphone", "muzyka z windows na iphone", "kodi dlna iphone", "strumieniowanie audio dlna"]
tags: ["dlna", "kodi", "evermusic", "iphone", "strumieniowanie muzyki", "mac", "nas", "linux", "sieć lokalna"]
readingTime: 5
---

{{< author-byline >}}

**TL;DR:** Zainstaluj Kodi na Mac, PC, Linux lub NAS, włącz serwer DLNA/UPnP i strumieniuj całą bibliotekę muzyczną na iPhone lub iPad za pomocą darmowej aplikacji Evermusic lub Flacbox przez Wi-Fi. Bez subskrypcji.

## Wprowadzenie

Jeśli masz **Mac, PC z Windows, maszynę Linux lub urządzenie NAS**, możesz łatwo przekształcić go w **osobisty serwer muzyczny** w domu za pomocą [Kodi](https://kodi.tv/), darmowej i otwartoźródłowej platformy multimedialnej. Dzięki wbudowanemu serwerowi **DLNA/UPnP** Kodi możesz strumieniować całą bibliotekę muzyczną na dowolnego klienta kompatybilnego z DLNA — w tym iPhone lub iPad.

W tym przewodniku pokażemy Ci krok po kroku, jak:

- Zainstalować Kodi na Mac lub PC
- Skonfigurować foldery muzyczne do udostępniania
- Włączyć serwer muzyczny DLNA
- Uzyskać dostęp do muzyki za pomocą aplikacji **Evermusic** lub **Flacbox** na iOS

Ta konfiguracja jest w 100% darmowa — bez subskrypcji, tylko Twoja własna muzyka strumieniowana przez sieć Wi-Fi. Czy próbujesz uporządkować dużą kolekcję MP3, słuchać FLAC przez Wi-Fi, czy po prostu cieszyć się lokalną muzyką bez synchronizacji przez iTunes, ta konfiguracja jest idealna.

## Pobierz i zainstaluj Kodi na Mac / PC / Linux / NAS

Najpierw odwiedź oficjalną stronę Kodi:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Strona główna Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Kliknij **Pobierz** i przewiń, aby znaleźć wersję dla swojego komputera.
Wybierz swój system operacyjny. W tym przykładzie użyjemy **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Strona pobierania Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Kliknij **Intel (x86/64)**, jeśli masz Mac z Intel, lub **Apple Silicon** dla M1, M2, M3 Mac, aby rozpocząć pobieranie.

{{< cards cols="1">}}
{{< card subtitle="Wybierz instalator macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Poczekaj chwilę, aż instalator się pobierze.

{{< cards cols="1">}}
{{< card subtitle="Kodi pobrane" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Po pobraniu znajdź plik `.dmg` w folderze **Pobrane**.

{{< cards cols="1">}}
{{< card subtitle="Zainstaluj Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Kliknij dwukrotnie pobrany plik, aby uruchomić instalator.
Przeciągnij Kodi do folderu **Aplikacje**, aby zainstalować.

{{< cards cols="1">}}
{{< card title="" subtitle="Zainstaluj Kodi, przeciągając do Aplikacji" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Uruchom Kodi. Być może będziesz musiał zezwolić na to w **Preferencje systemowe → Bezpieczeństwo i prywatność → Otwórz mimo to**.

{{< cards cols="1">}}
{{< card subtitle="Ekran główny Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Dodaj muzykę do biblioteki Kodi

Kliknij **ikonę koła zębatego** (Ustawienia) z ekranu głównego.

{{< cards cols="1">}}
{{< card subtitle="Ustawienia Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Przejdź do **Ustawienia mediów → Biblioteka**. Włącz **Aktualizuj bibliotekę przy uruchamianiu** dla biblioteki wideo i muzycznej do automatycznego indeksowania.

{{< cards cols="1">}}
{{< card subtitle="Ustawienia biblioteki" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Następnie przejdź do sekcji **Muzyka** i kliknij **Dodaj muzykę**.

{{< cards cols="1">}}
{{< card subtitle="Dodaj folder muzyczny" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Przeglądaj i wybierz folder, w którym przechowywana jest Twoja muzyka.

{{< cards cols="1">}}
{{< card subtitle="Wybierz źródło muzyki" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Dodaj źródło muzyki do Kodi.

{{< cards cols="1">}}
{{< card subtitle="Dodaj źródło muzyki" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Potwierdź i pozwól Kodi przeskanować bibliotekę muzyczną.

{{< cards cols="1">}}
{{< card subtitle="Potwierdź źródła muzyki" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Poczekaj chwilę, aż biblioteka zostanie przeskanowana i w pełni zbudowana.

{{< cards cols="1">}}
{{< card subtitle="Skanowanie biblioteki muzycznej" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Włącz serwer DLNA Kodi

Przejdź do **Ustawienia → Usługi → UPnP/DLNA**.

Włącz opcję: **Udostępnij moje biblioteki**.

Kodi działa teraz jako serwer DLNA w Twojej lokalnej sieci Wi-Fi.

{{< cards cols="1">}}
{{< card subtitle="Włącz DLNA w Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Otwórz bibliotekę Kodi

Kliknij prawym przyciskiem myszy, aby zamknąć okno ustawień i otworzyć główną bibliotekę Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Kliknij prawym przyciskiem, aby uzyskać dostęp do biblioteki Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Pobierz aplikację do strumieniowania muzyki na iOS

Pobierz darmową aplikację klienta DLNA na iOS, która pozwala strumieniować muzykę z wielu usług przechowywania w chmurze i serwerów DLNA.

- Użyj **Evermusic**, jeśli Twoja kolekcja to głównie MP3 i inne standardowe formaty audio.
- Wybierz **Flacbox**, jeśli masz bibliotekę muzyczną hi-res w formatach takich jak FLAC, ALAC lub DSD.

Obie aplikacje są dostępne na **iOS** i **macOS**, i są darmowe.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Pobierz Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Pobierz Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Dodaj źródło DLNA

Po pobraniu aplikacji iOS otwórz sekcję **Wszystkie Połączenia**.

{{< cards cols="1">}}
{{< card title="" subtitle="Główny pasek boczny aplikacji Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Przewiń w dół i dotknij **Sieć lokalna - Dostępne urządzenia**, aby odkryć serwery DLNA.
W tej sekcji zobaczysz wszystkie dostępne urządzenia w sieci lokalnej. Twój **serwer Kodi DLNA** powinien się tu pojawić. Dotknij serwera Kodi, aby się połączyć.

{{< cards cols="1">}}
{{< card title="" subtitle="Dostępne urządzenia DLNA w Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic wyświetli foldery biblioteki udostępniane przez Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Biblioteka muzyczna Kodi w Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Przejdź do folderu **Utwory**, aby wyświetlić wszystkie dostępne pliki audio na serwerze DLNA.

{{< cards cols="1">}}
{{< card title="" subtitle="Utwory z folderu zdalnego" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Dotknij dowolnego pliku audio, aby natychmiast rozpocząć strumieniowanie.

{{< cards cols="1">}}
{{< card title="" subtitle="Plik MP3 odtwarzany w Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Wróć do sekcji **Połączenia**. Dodany serwer DLNA pojawi się teraz tutaj. Dotknij jego ikony, aby ponownie się połączyć w dowolnym momencie. Możesz także połączyć inne usługi chmurowe z tego ekranu, używając tych samych kroków.

Możesz także włączyć **śledzenie Last.fm** tutaj. Statystyki odtwarzania zostaną zapisane na koncie Last.fm, zapewniając spersonalizowane rekomendacje muzyczne później.

{{< cards cols="1">}}
{{< card title="" subtitle="Połączenia w Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Zbuduj bibliotekę muzyczną

Zarówno **Evermusic**, jak i **Flacbox** pozwalają dodawać muzykę do biblioteki i organizować ją według **tagów metadanych**, takich jak artyści, albumy, gatunki i kompozytorzy.

Aby rozpocząć, otwórz sekcję **Biblioteka muzyczna**. Przewiń w dół do **Narzędzia i ustawienia** i dotknij **Dodaj muzykę**.

{{< cards cols="1">}}
{{< card title="" subtitle="Biblioteka muzyczna Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Wybierz źródło muzyki — w tym przypadku wybierz **Połączenia**.

{{< cards cols="1">}}
{{< card title="" subtitle="Dodaj nową muzykę w Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Znajdź **serwer Kodi DLNA** w Połączeniach i dotknij, aby wyświetlić foldery i pliki.

{{< cards cols="1">}}
{{< card title="" subtitle="Wybierz serwer DLNA do importu muzyki" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Wybierz foldery lub pliki, które chcesz dodać, i dotknij **Zrobione**.

{{< cards cols="1">}}
{{< card title="" subtitle="Wybierz folder muzyczny do dodania" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Aplikacja przeskanuje wybrane pliki i uporządkuje je za pomocą metadanych w sekcje, takie jak Artyści, Albumy, Gatunki i Kompozytorzy.

{{< cards cols="1">}}
{{< card title="" subtitle="Biblioteka muzyczna z kategoriami" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Tworzenie list odtwarzania

Możesz także tworzyć własne listy odtwarzania.

Najpierw otwórz kartę **Listy odtwarzania**.

{{< cards cols="1">}}
{{< card title="" subtitle="Karta List odtwarzania w Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Dotknij przycisku **plus (+)** i wybierz **Nowa lista odtwarzania**.

{{< cards cols="1">}}
{{< card title="" subtitle="Utwórz nową listę odtwarzania" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Wprowadź nazwę listy odtwarzania i dotknij **Zapisz**.

{{< cards cols="1">}}
{{< card title="" subtitle="Wprowadź nazwę listy odtwarzania" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Następnie wybierz źródło do dodania utworów — tutaj wybieramy **Bibliotekę**.

{{< cards cols="1">}}
{{< card title="" subtitle="Dodaj utwory do nowej listy odtwarzania" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Wybierz żądane utwory i dotknij **Zrobione**, aby je dodać.

{{< cards cols="1">}}
{{< card title="" subtitle="Dodaj muzykę z biblioteki do listy odtwarzania" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Wybrane utwory pojawią się teraz na utworzonej liście odtwarzania.

{{< cards cols="1">}}
{{< card title="" subtitle="Utworzona lista odtwarzania na liście" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Domyślnie utwory są dostępne do strumieniowania. Aby słuchać offline, włącz **Tryb offline** — aplikacja pobierze wszystkie utwory z listy.

{{< cards cols="1">}}
{{< card title="" subtitle="Tryb offline włączony dla listy odtwarzania" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Dotknij przycisku **Więcej akcji**, aby poznać dodatkowe opcje. Możesz:

- Zarchiwizować listę odtwarzania
- Zmienić okładkę albumu
- Zmienić kolejność utworów
- I więcej przydatnych funkcji

{{< cards cols="1">}}
{{< card title="" subtitle="Więcej akcji listy odtwarzania dostępnych" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Podsumowanie

Z **Evermusic** i **Flacbox** zamiana iPhone, iPad lub Mac w potężny odtwarzacz muzyki DLNA jest łatwa. Niezależnie od tego, czy przechowujesz muzykę w chmurze, na NAS, czy na domowym serwerze multimedialnym, takim jak **Kodi**, te aplikacje pozwalają strumieniować, organizować i cieszyć się kolekcją bez ograniczeń.

- Strumieniuj MP3 lub hi-res FLAC bezpośrednio z **serwera Kodi DLNA**
- Zbuduj osobistą bibliotekę muzyczną pogrupowaną według metadanych (albumy, gatunki, kompozytorzy)
- Twórz i zarządzaj **niestandardowymi listami odtwarzania**
- Włącz **tryb offline** do słuchania w podróży
- Łącz się z **wieloma usługami chmurowymi** i **urządzeniami sieci lokalnej**
- Śledź nawyki słuchania z **integracją Last.fm**

Niezależnie od tego, czy jesteś audiofilem, czy przypadkowym słuchaczem, Evermusic i Flacbox oferują wszystko, czego potrzebujesz do płynnego strumieniowania i organizacji muzyki.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Pobierz Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Pobierz Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Zacznij budować swoje osobiste doświadczenie muzyczne już dziś.

## Najczęściej zadawane pytania

{{% details title="Czy Kodi jest darmowy jako serwer DLNA?" closed="true" %}}
Tak. Kodi jest całkowicie darmowy i open-source. Działa na macOS, Windows, Linux i wielu urządzeniach NAS.
{{% /details %}}

{{% details title="Czy Evermusic i Flacbox obsługują strumieniowanie FLAC przez DLNA?" closed="true" %}}
Tak. Flacbox jest zoptymalizowany pod kątem formatów hi-res, takich jak FLAC, ALAC i DSD. Evermusic również obsługuje odtwarzanie FLAC obok MP3 i innych standardowych formatów.
{{% /details %}}

{{% details title="Czy mogę słuchać offline po strumieniowaniu z Kodi?" closed="true" %}}
Tak. Włącz Tryb offline na dowolnej liście odtwarzania, a aplikacja pobierze wszystkie utwory na urządzenie do słuchania bez połączenia sieciowego.
{{% /details %}}

{{% details title="Czy potrzebuję subskrypcji premium, aby korzystać z DLNA?" closed="true" %}}
Wersja darmowa obsługuje do 3 połączeń chmurowych lub sieciowych. Premium usuwa ten limit i pozwala na nieograniczone połączenia z usługami i serwerami DLNA.
{{% /details %}}

{{% details title="Czy mój iPhone musi być w tej samej sieci Wi-Fi co Kodi?" closed="true" %}}
Tak. Strumieniowanie DLNA działa przez sieć lokalną. Zarówno serwer Kodi, jak i urządzenie iOS muszą być podłączone do tej samej sieci Wi-Fi.
{{% /details %}}

{{% details title="Czy mogę użyć tej konfiguracji z NAS zamiast Mac lub PC?" closed="true" %}}
Tak. Wiele urządzeń NAS (Synology, QNAP itp.) obsługuje Kodi lub ma własny wbudowany serwer DLNA. Evermusic i Flacbox mogą łączyć się z dowolnym standardowym serwerem DLNA/UPnP.
{{% /details %}}
