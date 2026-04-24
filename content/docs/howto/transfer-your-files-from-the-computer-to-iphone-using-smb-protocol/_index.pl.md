---
title: "Przesyłanie plików z komputera na iPhone za pomocą protokołu SMB"
description: "Dowiedz się, jak przesyłać i uzyskiwać dostęp do dużych plików z Maca lub PC z Windowsem na iPhone'a lub iPada za pomocą Evermusic i protokołu SMB. Przewodnik krok po kroku do płynnego streamingu i zarządzania plikami."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["przesyłanie plików na iPhone SMB", "streamowanie muzyki z PC na iPhone", "połączenie Maca z iPhonem SMB", "konfiguracja Evermusic SMB", "dostęp do plików komputera iPhone", "udostępnianie muzyki Windows iOS", "transfer plików SMB Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Podsumowanie:** Użyj Evermusic na swoim iPhonie lub iPadzie, aby uzyskać dostęp do plików przechowywanych na Macu lub PC z Windowsem przez sieć lokalną za pomocą SMB. Bez kabli, bez iTunes, bez konieczności przesyłania do chmury. Włącz udostępnianie plików na komputerze, połącz się w aplikacji i przeglądaj lub odtwarzaj pliki bezprzewodowo.

Czy masz obszerną kolekcję dużych plików na swoim MAC lub PC i chcesz uzyskać do nich łatwy dostęp z iPhone'a lub iPada? Nasze aplikacje zapewniają proste rozwiązanie.

Wykonaj te kroki, aby umożliwić płynny dostęp między komputerem a urządzeniem iOS za pomocą protokołu SMB:

## Krok 1: Włącz protokół SMB na swoim komputerze

**Dla MAC:**

1. Otwórz "Preferencje systemowe" na swoim MAC.
2. Kliknij "Udostępnianie".
3. Włącz usługę "Udostępnianie plików".
4. Dodaj folder z muzyką do sekcji "Foldery udostępnione". Dodaj użytkownika i wybierz poziom uprawnień (Odczyt i zapis lub Tylko odczyt). Możesz wybrać "Wszyscy: Tylko odczyt" dla dodanego folderu z muzyką.

   ![Ekran ustawień Maca](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Zapamiętaj URL komputera (smb://192.168.xx.xx), ponieważ użyjesz go w następnych krokach.
6. Kliknij "Opcje" i aktywuj "Udostępniaj pliki i foldery za pomocą SMB".

   ![Ekran udostępniania plików Maca](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Włącz "Udostępnianie plików Windows" dla dostępnych kont.

   ![Ekran udostępniania SMB Maca](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Dla Windows PC:**

1. Kliknij prawym przyciskiem myszy na folderze z muzyką.
2. Wybierz "Właściwości".
3. Przejdź do zakładki "Udostępnianie".
4. Kliknij "Udostępnij..."
5. Wybierz osoby, którym chcesz udostępnić folder i określ poziom uprawnień. Możesz wybrać "Wszyscy: Odczyt" dla wybranego folderu z muzyką.

   ![Ekran udostępniania SMB Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Kliknij "Zrobione".
7. Kliknij "Zrobione" w oknie "Udostępnianie plików" i zapamiętaj ścieżkę folderu.

   ![Udostępniony folder SMB Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Krok 2: Podłącz swoje urządzenie iOS

1. Otwórz aplikację na iPhonie lub iPadzie.
2. Przejdź do zakładki "Połączenia".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Ekran Połączenia w Evermusic"
  caption="Ekran Połączenia w Evermusic"
  width="400"
>}}

*Jeśli Twój komputer pojawia się w sekcji "Dostępne urządzenia":*

Jeśli Twój komputer jest widoczny w sekcji "Dostępne urządzenia" i wybrałeś "Wszyscy: Tylko odczyt" w poprzednim kroku, po prostu dotknij swojego komputera, a połączy się automatycznie.

*Jeśli Twój komputer nie pojawia się automatycznie:*

1. Dotknij "Połącz usługę w chmurze".
2. Wybierz "SMB" na ekranie "Połącz usługę w chmurze".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Ekran Połącz usługę w chmurze w Evermusic"
  caption="Ekran Połącz usługę w chmurze w Evermusic"
  width="400"
>}}

3. Na ekranie "Połączenie SMB" wpisz URL serwera ze ścieżką do udostępnionego folderu. Możesz użyć nazwy serwera lub adresu IP serwera:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Wpisz swój login i hasło lub pozostaw te pola puste, jeśli wybrałeś "Wszyscy: Tylko odczyt" w poprzednim kroku.
5. Pole "WORKGROUP" jest opcjonalne i powinno być używane, jeśli masz Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Ekran konektora SMB w Evermusic"
  caption="Ekran konektora SMB w Evermusic"
  width="400"
>}}

6. Po podłączeniu komputera za pomocą protokołu SMB pojawi się on w sekcji "Usługi w chmurze" na ekranie "Połączenia".
7. Otwórz podłączoną usługę i przejdź do żądanego folderu.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Otwarty folder SMB w Evermusic"
  caption="Otwarty folder SMB w Evermusic"
  width="400"
>}}

8. Możesz użyć wbudowanego menedżera plików do edycji plików w razie potrzeby.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Menedżer plików Evermusic"
  caption="Menedżer plików Evermusic"
  width="400"
>}}

## Krok 3: Obejście problemu z folderami SMB2 ze znakami specjalnymi

Czasami możesz napotkać problemy z folderami zawierającymi znaki specjalne podczas korzystania z protokołu SMB2. Oto kilka kroków, aby rozwiązać ten problem:

1. **Włącz SMB 1:**  
   • Jako tymczasowe rozwiązanie spróbuj włączyć SMB 1 na serwerze i w ustawieniach aplikacji. Może to pomóc w ominięciu problemów związanych ze znakami specjalnymi w nazwach folderów.

2. **Użyj systemowego menu otwierania plików:**  
   • Przejdź do "Pliki lokalne".  
   • Przewiń w dół do sekcji "Pliki na tym urządzeniu".  
   • Dotknij "Otwórz pliki..." lub "Otwórz foldery...".  
   • Zlokalizuj swój serwer i wybierz pliki lub foldery, których potrzebujesz.  
   • Dotknij "Otwórz", aby potwierdzić wybór.

3. **Alternatywne protokoły:**  
   • Jeśli problem się utrzymuje, rozważ połączenie z NAS za pomocą protokołów WebDAV lub DLNA, jeśli Twój NAS obsługuje te opcje. Te protokoły mogą lepiej obsługiwać znaki specjalne.

Stosując te kroki, możesz złagodzić problemy ze znakami specjalnymi w nazwach folderów podczas korzystania z protokołu SMB2.

## Podsumowanie

Dzięki tym krokom możesz bez wysiłku uzyskać dostęp do swojej obszernej kolekcji plików z MAC lub PC na iPhonie lub iPadzie za pomocą naszych aplikacji.

## Najczęściej zadawane pytania

{{% details title="Czy mogę uzyskać dostęp do plików na PC z iPhone'a bez iTunes?" closed="true" %}}
Tak. Evermusic łączy się z komputerem przez SMB w lokalnej sieci Wi-Fi. Synchronizacja iTunes lub Finder nie jest potrzebna. Włącz udostępnianie plików na PC i połącz się bezpośrednio z aplikacji.
{{% /details %}}

{{% details title="Czy dostęp do plików SMB działa przez internet?" closed="true" %}}
Nie. SMB to protokół sieci lokalnej. iPhone i komputer muszą być w tej samej sieci Wi-Fi. Aby uzyskać zdalny dostęp, prześlij pliki do usługi w chmurze, takiej jak Google Drive lub Dropbox, i połącz się z nią w Evermusic.
{{% /details %}}

{{% details title="Do jakich typów plików mogę uzyskać dostęp przez SMB?" closed="true" %}}
Evermusic obsługuje MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC i inne formaty audio. Możesz także przeglądać i zarządzać plikami innymi niż audio za pomocą wbudowanego menedżera plików.
{{% /details %}}

{{% details title="Czy mogę przesłać pliki z NAS na iPhone'a za pomocą SMB?" closed="true" %}}
Tak. Większość urządzeń NAS (Synology, QNAP, WD My Cloud i inne) obsługuje SMB. Połącz się z NAS, korzystając z tych samych kroków w tym przewodniku.
{{% /details %}}

{{% details title="Czy muszę kopiować pliki na iPhone'a, aby je odtwarzać?" closed="true" %}}
Nie. Evermusic strumieniuje pliki bezpośrednio z komputera lub NAS przez sieć. Pliki nie są kopiowane na iPhone'a, chyba że zdecydujesz się je pobrać do odtwarzania offline.
{{% /details %}}

{{% details title="Czy udostępnianie plików SMB jest bezpieczne?" closed="true" %}}
Udostępnianie plików SMB działa tylko w sieci lokalnej. Inne urządzenia w innych sieciach nie mogą uzyskać dostępu do udostępnionych folderów. Dla dodatkowego bezpieczeństwa użyj loginu i hasła zamiast anonimowego (Wszyscy) dostępu.
{{% /details %}}
