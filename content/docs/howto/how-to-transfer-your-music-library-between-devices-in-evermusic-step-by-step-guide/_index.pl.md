---
title: "Jak przenieść bibliotekę muzyczną między urządzeniami w Evermusic: przewodnik krok po kroku"
description: "Łatwo przenieś bibliotekę muzyczną Evermusic, listy odtwarzania, okładki albumów i ustawienia z jednego iPhone'a, iPada lub Maca na inny za pomocą Wi-Fi Drive i narzędzi kopii zapasowej."
date: 2024-12-29
tags: ["bibliotekamuzyczna", "transfer", "wifi", "kopiazapasowa", "webdav", "przywracanie"]
keywords: ["przenoszenie biblioteki muzycznej Evermusic", "kopia zapasowa i przywracanie list odtwarzania Evermusic", "Evermusic WiFi Drive", "synchronizacja Evermusic między urządzeniami", "przenoszenie bazy danych Evermusic", "transfer plików Evermusic", "przywracanie ustawień odtwarzacza audio", "WebDAV transfer muzyki iOS"]
readingTime: 3
---

{{< author-byline >}}


**Podsumowanie:** Aby przenieść bibliotekę Evermusic na nowe urządzenie, utwórz kopię zapasową na urządzeniu źródłowym, uruchom Wi-Fi Drive, podłącz drugie urządzenie przez tę samą sieć, pobierz kopię zapasową i pliki muzyczne, a następnie przywróć z kopii zapasowej. Cały proces zajmuje około 10 minut w zależności od rozmiaru biblioteki.

W tym przewodniku przeprowadzimy cię przez przenoszenie całej biblioteki muzycznej — w tym bazy danych, okładek albumów i ustawień — z jednego urządzenia (iPhone lub Mac) na drugie. Automatyczna synchronizacja biblioteki muzycznej i list odtwarzania jest funkcją planowaną na przyszłość, ale obecnie ten proces musi być wykonywany ręcznie.

## Krok 1: Utwórz kopię zapasową na pierwszym urządzeniu

1. **Otwórz aplikację na pierwszym urządzeniu** (tym z biblioteką muzyczną, listami odtwarzania i połączonymi usługami w chmurze).
2. **Przejdź do Ustawienia** i wybierz opcję **Kopia zapasowa i Przywracanie**.

![Backup and Restore](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. Na ekranie **Kopia zapasowa i Przywracanie** wybierz elementy do uwzględnienia w pliku kopii zapasowej:
   - **Baza danych** (zawiera bibliotekę muzyczną i listy odtwarzania)
   - **Okładki albumów**
   - **Ustawienia**

Te opcje są domyślnie włączone.

![Backup Options](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Dotknij **Kopia zapasowa danych aplikacji**, aby rozpocząć proces.

![Backup Application Data](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Po zakończeniu tworzenia kopii zapasowej pojawi się alert informacyjny.

![Backup Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Dotknij **Pokaż plik**, aby wyświetlić plik kopii zapasowej w katalogu **Dokumenty**. Pliki kopii zapasowych są zazwyczaj zapisywane w folderze **Backup**.

![Show Backup File](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Krok 2: Uruchom serwer Wi-Fi Drive

1. Przejdź do sekcji **Połączenia** w aplikacji.
2. Przewiń w dół do **Połącz przez Wi-Fi** i dotknij.

![Connect Using Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. Na następnym ekranie dotknij **Uruchom Wi-Fi Drive**.

- Opcjonalnie możesz ustawić login i hasło dla bezpieczeństwa, ale nie jest to konieczne w sieciach domowych.

4. Po uruchomieniu zobaczysz dostępne adresy serwera. Można je wykorzystać w przeglądarkach na komputerze lub aplikacjach WebDAV, ale w tym przewodniku przejdziemy bezpośrednio do następnych kroków.

![Wi-Fi Drive Started](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Krok 3: Połącz drugie urządzenie z pierwszym

1. Otwórz aplikację na drugim urządzeniu (tym, na które chcesz przenieść bibliotekę).
2. Upewnij się, że oba urządzenia są połączone z tą samą siecią Wi-Fi.
3. Na drugim urządzeniu otwórz kartę **Połączenia** i wybierz **Dostępne urządzenia**.

![Available Devices](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Powinieneś zobaczyć połączenie WebDAV o nazwie **Evermusic** (serwer uruchomiony na pierwszym urządzeniu). Dotknij, aby się połączyć.

5. Po połączeniu zobaczysz wszystkie foldery z pierwszego urządzenia.

![Connected to First Device](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Krok 4: Przygotuj się do transferu plików

1. Na drugim urządzeniu przejdź do **Ustawienia > Menedżer plików** i włącz **Zapisz pobrane pliki do - Pytaj za każdym razem**.

- Dzięki temu możesz wybrać folder docelowy dla każdego pobierania.

2. Wróć do karty **Połączenia** i przejdź do połączonego serwera WebDAV.

![Prepare for File Transfers](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Krok 5: Przenieś kopię zapasową i pliki muzyczne

1. Otwórz folder **Backup** na połączonym serwerze WebDAV.

![Backup Folder](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Dotknij przycisku **Więcej akcji** (trzy kropki) obok pliku kopii zapasowej i wybierz **Pobierz**.

3. Utwórz folder **Backup** na drugim urządzeniu, aby przechowywać pobrane pliki. Potwierdź wybór, dotykając **Zrobione**.

![Download Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Przenieś dodatkowe pliki muzyczne:
   - Sprawdź folder **Pobrania** lub inne odpowiednie foldery na serwerze WebDAV.

![Transfer Music Files](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Użyj opcji **Wybrać**, aby zaznaczyć pliki, a następnie dotknij **Więcej akcji > Pobierz**. Zapisz je w odpowiednim folderze na drugim urządzeniu, aby zachować tę samą strukturę katalogów.

Celem jest przeniesienie wszystkich plików z pierwszego urządzenia na bieżące urządzenie, zapewniając identyczną strukturę folderów. W ten sposób linki w bibliotece muzycznej i listach odtwarzania pozostaną nienaruszone. Zauważ, że pliki lokalne przechowywane poza katalogiem Dokumenty aplikacji na pierwszym urządzeniu muszą zostać przeniesione osobno. Ponieważ aplikacja nie może uzyskać dostępu do tych plików w trybie Wi-Fi Drive, musisz użyć aplikacji Pliki systemowe do ich transferu.

![Transfer Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Krok 6: Monitoruj postęp transferu

1. Na drugim urządzeniu przejdź do sekcji **Pliki lokalne** (lub karty **Pobrania** na iPadzie/Macu).

2. Dotknij przycisku **Aktywność transferu** w lewym górnym rogu, aby monitorować kolejkę transferu.

![Monitor Transfer](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Krok 7: Przywróć dane z kopii zapasowej

1. Po pobraniu pliku kopii zapasowej i wszystkich potrzebnych plików audio na drugie urządzenie otwórz folder **Backup**.

2. Dotknij pliku kopii zapasowej — pojawi się komunikat potwierdzenia.

![Restore Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Uwaga:** Przywracanie zastąpi wszystkie bieżące dane biblioteki muzycznej, listy odtwarzania, ustawienia i okładki albumów danymi z kopii zapasowej.

3. Dotknij **Przywróć**, aby rozpocząć proces.

![Restore Process](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Po zakończeniu przywracania alert potwierdzi sukces.

![Restoration Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Sprawdź sekcje **Listy odtwarzania** lub **Biblioteka muzyczna**, aby zweryfikować przywracanie.

![Verify Restoration](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Krok 8: Ponowne indeksowanie biblioteki muzycznej

1. Aby uzyskać najlepsze rezultaty, ponownie zindeksuj bibliotekę, aby upewnić się, że wszystkie pliki zostały pomyślnie wykryte.

2. Przejdź do **Ustawienia > Biblioteka muzyczna > Synchronizacja muzyki offline** i wybierz **Rozpocznij skanowanie folderów lokalnych**.

Wykonując te kroki, pomyślnie przeniesiesz bibliotekę muzyczną, listy odtwarzania i ustawienia na inne urządzenie. Jeśli napotkasz jakiekolwiek problemy, nie wahaj się skontaktować z pomocą techniczną.

## Często zadawane pytania

{{% details title="Czy mogę przenieść bibliotekę Evermusic bez Wi-Fi?" closed="true" %}}
Wi-Fi Drive wymaga, aby oba urządzenia były w tej samej sieci Wi-Fi. Obecnie nie ma opcji transferu przez Bluetooth ani sieć komórkową. Alternatywnie możesz użyć AirDrop lub aplikacji Pliki, aby ręcznie przenieść plik kopii zapasowej i foldery muzyczne między urządzeniami.
{{% /details %}}

{{% details title="Czy połączenia z usługami w chmurze zostaną przeniesione z kopią zapasową?" closed="true" %}}
Kopia zapasowa zawiera bazę danych, listy odtwarzania, okładki albumów i ustawienia. Dane logowania do usług w chmurze nie są uwzględniane ze względów bezpieczeństwa. Po przywróceniu musisz ponownie połączyć konta chmurowe na nowym urządzeniu.
{{% /details %}}

{{% details title="Co stanie się z istniejącą biblioteką na drugim urządzeniu?" closed="true" %}}
Przywracanie kopii zapasowej zastępuje wszystkie istniejące dane biblioteki muzycznej, listy odtwarzania, ustawienia i okładki albumów na drugim urządzeniu. Najpierw utwórz osobną kopię zapasową drugiego urządzenia, jeśli chcesz zachować jego dane.
{{% /details %}}

{{% details title="Czy ten proces działa między iPhone a Mac?" closed="true" %}}
Tak. Evermusic obsługuje transfer Wi-Fi Drive między dowolną kombinacją iPhone, iPad i Mac. Oba urządzenia muszą po prostu znajdować się w tej samej sieci Wi-Fi.
{{% /details %}}

{{% details title="Jak długo trwa transfer?" closed="true" %}}
Czas transferu zależy od rozmiaru biblioteki muzycznej i prędkości Wi-Fi. Typowa biblioteka o rozmiarze kilku gigabajtów jest przenoszona w ciągu 5-15 minut przez standardową sieć domową.
{{% /details %}}
