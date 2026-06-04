---
title: "Edytor tagów"
date: 2020-02-01
description: "Dowiedz się, jak używać Edytora tagów Evertag do aktualizacji metadanych muzyki, edycji okładek albumów, wsadowej edycji wielu plików i zarządzania tagami z MusicBrainz. Idealny do organizowania biblioteki muzycznej na iOS i Mac."
keywords: [
  "Evertag edytor tagów", "edytor metadanych audio", "edytor tagów muzycznych",
  "edytuj tagi audio iPhone", "edytor okładek albumów", "wsadowa edycja tagów audio",
  "metadane MusicBrainz", "aplikacja do organizacji muzyki", "poradnik Evertag", "edytor tagów ID3"
]
tags: ["poradnik", "evertag", "edytor tagów"]
readingTime: 5
---


**Edytor tagów** to główny ekran aplikacji Evertag, gdzie możesz przeglądać i edytować metadane plików audio. Otwórz ten ekran, naciskając plik z sekcji **Pliki lokalne** lub z dowolnego podłączonego konta **chmury**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Tag Editor Screen" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Tryby edycji

Evertag oferuje dwa tryby edycji:

- **Tryb pojedynczego pliku**  
  - Poruszaj się między plikami, przesuwając w lewo lub w prawo na karuzeli okładek.  

- **Tryb wsadowy**  
  - Edytuj wiele plików jednocześnie i stosuj wspólne metadane.  
  - Aby aktywować, przewiń na dół i naciśnij **Edytuj pliki jednocześnie**.

## Tryb pojedynczego pliku

Domyślnie aplikacja otwiera edytor tagów w trybie pojedynczego pliku z włączonymi tylko głównymi opcjami edycji. W tym trybie możesz edytować najczęstsze pola metadanych, takie jak:

**Tytuł utworu, Podtytuł, Artysta albumu, Album, Artysta, Kompozytor, Wykonawca, Gatunek, Komentarz, Liczba uderzeń na minutę, Podcast, Kompilacja, Numer dysku, Numer ścieżki, Łączna liczba ścieżek, Ocena, Rok**

Aby uzyskać dostęp do wszystkich dostępnych tagów, przewiń na dół ekranu i naciśnij opcję **Pokaż rozszerzone tagi**. Przełączy to edytor do trybu rozszerzonego, umożliwiając edycję ponad **120 pól metadanych**, w tym **Tagów MusicBrainz**, **Tekstów piosenek**, **Klasyfikacji doradczych**, wartości replay-gain, porządku sortowania, metadanych podcastów i nie tylko. Użyj **Ustawienia → Edytor tagów audio → Przyciski na ekranie głównym**, aby trwale włączyć Pokaż rozszerzone tagi, tak aby był zawsze widoczny.

{{< cards cols="1">}}
{{< card title="" subtitle="Bottom Actions Panel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Tryb wsadowy

Możesz wejść w tryb wsadowy na dwa sposoby:

1. **Z menedżera plików**  
   - Naciśnij **Więcej akcji** (•••) w prawym górnym rogu.  
   - Naciśnij **Wybrać**, wybierz wiele plików, a następnie naciśnij **Edytuj tagi audio**.

2. **Z edytora tagów**  
   - Otwórz dowolny plik, przewiń na dół i naciśnij **Edytuj pliki jednocześnie**, aby załadować wszystkie pliki z tego samego folderu.

{{< cards cols="1">}}
{{< card title="" subtitle="Batch Editing Mode" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Po edycji naciśnij **Zapisz**, aby zastosować zmiany.

## Edytuj teksty piosenek

Rozszerzony edytor udostępnia pole **Teksty piosenek**. Naciśnij je, aby otworzyć listę tekstów — każdy wpis ma własny język i opis, więc jeden utwór może przechowywać kilka tłumaczeń.

Nie musisz wpisywać tekstów od zera. Edytor zawiera skróty do wyszukiwania jednym dotknięciem do najpopularniejszych baz tekstów piosenek, wstępnie wypełnionych artystą i tytułem bieżącego utworu:

- **Lrclib** — główna publiczna baza danych dla **zsynchronizowanych tekstów (w stylu LRC)**. Używaj jej, gdy chcesz zsynchronizowane teksty przewijane linia po linii w odtwarzaczach, które je obsługują.
- **Genius** — duży katalog z adnotacjami i dokładnymi tekstami w formacie zwykłego tekstu.
- **Lyricsify** — baza danych prowadzona przez społeczność z tekstami zwykłymi i z sygnaturami czasowymi.
- **Google** — ogólne wyszukiwanie internetowe jako alternatywa, gdy dedykowane bazy danych nie mają dopasowania.

Każdy skrót pojawia się tylko wtedy, gdy odpowiednia usługa jest dostępna z urządzenia. Naciśnij usługę, skopiuj żądane teksty (lub sygnatury czasowe LRC), wróć do Evertag i wklej je w pole tekstowe — następnie naciśnij **Zapisz**, aby zapisać teksty z powrotem w tagach pliku audio.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Pages" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Wybierz język z selektora:

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Language Selector" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Następnie wklej lub wpisz tekst piosenek. Evertag obsługuje zarówno zwykły tekst, jak i zsynchronizowane teksty — pole placeholder pokazuje przykład formatu LRC, który jest dokładnie tym, co Lrclib i Lyricsify zwracają dla zsynchronizowanych wyników.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Text Editor" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Ustaw Ocenę i Klasyfikację doradczą

Rozszerzony edytor oferuje gwiazdkową kontrolę **Oceny** wraz z segmentowaną kontrolą **Klasyfikacji doradczej**.

### Ocena gwiazdkowa

Użyj pola **Ocena**, aby przyznać utworowi osobisty wynik od jednej do pięciu gwiazdek. Wartość jest zapisywana w standardowym polu oceny pliku (POPM dla ID3, `rate` dla MP4, `RATING` dla Vorbis/APE itd.), więc inne aplikacje odczytujące ten tag — w tym aplikacja Music, Plex, Roon i większość desktopowych edytorów tagów — od razu zobaczą twoje oceny.

{{< cards cols="1">}}
  {{< card title="" subtitle="Rating" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Klasyfikacja doradcza

**Klasyfikacja doradcza** oznacza zawartość utworu za pomocą jednej z wartości ze standardu Parental Advisory, używanego przez iTunes Store i większość platform muzycznych:

- **Bez zastrzeżeń** — wartość domyślna dla utworów bez informacji o poradach rodzicielskich. Plik jest traktowany jako odpowiedni dla wszystkich słuchaczy i nie będzie wyświetlać żadnej etykiety doradczej w odtwarzaczach, które respektują ten tag.
- **Explicit** — utwór zawiera wulgarny język lub treść. Odtwarzacze respektujące kontrolę rodzicielską (aplikacja Music, aplikacja Apple TV, eksport Spotify, Plex itp.) wyświetlą oznaczenie **E** obok tytułu i, gdy ograniczenia są włączone na urządzeniu lub koncie, mogą ukryć utwór w profilach dzieci lub odmówić jego odtwarzania.
- **Czyste** — ocenzurowana lub zredagowana wersja inaczej wyraźnego utworu. Odtwarzacze wyświetlają oznaczenie **C**, aby słuchacze mogli odróżnić czystą wersję od oryginalnego wyraźnego mastera, co jest przydatne, gdy obie wersje żyją w tej samej bibliotece.

Powinieneś ustawić lub poprawić to pole, gdy:

- Plik ma błędną etykietę (na przykład czyste wydanie radiowe, które zostało błędnie oznaczone jako Explicit, lub odwrotnie).
- Utwory zostały zripowane lub pobrane bez tagu i teraz są wyświetlane jako Bez zastrzeżeń, mimo że zawierają wyraźną treść — niezbędne do prawidłowego działania kontroli rodzicielskiej i bibliotek udostępnianych rodzinie.
- Przygotowujesz album do przesłania lub udostępnienia i potrzebujesz, aby każdy utwór miał spójne metadane.
- Chcesz, aby CarPlay, ekran blokady, odtwarzacze w stylu Apple Music lub oprogramowanie DJ wyświetlały prawidłowe oznaczenie **E** / **C** obok tytułu.

Wartość jest przechowywana w standardowym polu klasyfikacji doradczej dla formatu pliku (`rtng` dla MP4, `TXXX:ITUNESADVISORY` dla ID3, `ITUNESADVISORY` dla Vorbis), więc każdy odtwarzacz, który odczytuje metadane porad rodzicielskich, zobaczy twoją aktualizację.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Advisory Rating" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Edytuj okładkę albumu

Aby zmienić okładkę albumu:

1. Naciśnij ikonę **Aparatu** w karuzeli okładek.  
2. Wybierz lokalizację obrazu: Pliki lokalne, Chmura, Pobrania lub Biblioteka zdjęć.  
3. Wybierz obraz, który ma być zastosowany jako okładka.

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Image" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Więcej akcji w edytorze tagów

Dodatkowe opcje edycji są dostępne przez pasek narzędzi pod widokiem okładek.

{{< cards cols="1">}}
  {{< card title="" subtitle="More Actions Menu" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Automatyczne wyszukiwanie tagów audio

Ta akcja aktywuje inteligentny silnik wyszukiwania tagów, który na podstawie istniejących informacji znajduje i wypełnia kompletne metadane dla pliku audio.  
Aplikacja korzysta z bazy danych MusicBrainz — jednej z najbardziej kompleksowych baz tagów — z ponad **50 milionami** utworów.

### Wyszukaj okładkę albumu

Użyj metadanych do wyszukania w internecie właściwej okładki albumu.  

{{< cards cols="1">}}
  {{< card title="" subtitle="Search Album Cover" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Po znalezieniu zapisz obraz do **Zdjęć** za pomocą systemowego menu kontekstowego.

{{< cards cols="1">}}
  {{< card title="" subtitle="Add Image to Photos" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Następnie wróć do edytora tagów, naciśnij ikonę Aparatu, przejdź do **Biblioteki zdjęć** i wybierz zapisany obraz. Aplikacja ustawi go jako okładkę pliku audio.

Możesz dostosować sposób skalowania okładek w ustawieniach aplikacji.

### Zapisz okładkę albumu

Ta akcja zapisuje bieżącą okładkę albumu do folderu **Dokumenty**, dzięki czemu możesz ją później ponownie wykorzystać.

### Normalizuj kodowanie

Ta akcja normalizuje kodowanie tekstu wszystkich tagów w metadanych pliku audio. Jest szczególnie pomocna, jeśli przechodzisz z komputera z systemem Windows, gdzie pliki mogą używać różnych kodowań wyświetlanych jako nieczytelne lub zniekształcone znaki na Mac.

### Ręczne wyszukiwanie tagów

Ręczne wyszukiwanie metadanych albumu za pomocą bazy danych MusicBrainz.  

- Wybierz album  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Wybierz właściwy utwór  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Song" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Wybierz, które tagi zastosować  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Audio Tags" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Naciśnij **Zrobione**, aby zastosować wybrane metadane do swojego utworu.

### Usuń tagi audio

Wyczyść wszystkie pola metadanych dla pliku. Przydatne przy zaczynaniu od zera. Naciśnij **Zapisz**, aby potwierdzić.

## Ustawienia edytora tagów

Przejdź do **Ustawienia → Edytor tagów audio**, aby dostosować zachowanie.

### Skalowanie okładki albumu

Wybierz sposób skalowania okładek albumów podczas zapisywania w plikach audio. Możesz wyłączyć skalowanie, aby zachować oryginalny rozmiar obrazu, ale pamiętaj, że niektóre odtwarzacze mogą nie obsługiwać dużych plików okładek. Opcja „oryginalny rozmiar" jest częścią funkcji Premium personalizacji.

### Opcje zapisywania tagów

- **ID3v2.4** — gdy włączone, aplikacja zapisuje tagi w formacie ID3v2.4, gdy to możliwe. Wyłącz, aby wrócić do szerzej obsługiwanego ID3v2.3, jeśli tagi audio nie są poprawnie wyświetlane na starszych odtwarzaczach lub urządzeniach.
- **Duplikaty tagów** — gdy włączone, typowe pola metadanych są duplikowane do obu sekcji tagów pliku. Poprawia to zgodność ze starszymi odtwarzaczami audio, ale w większości przypadków nie jest wymagane.

### Opcje aktualizacji metadanych pliku w chmurze

Możesz kontrolować, jak aplikacja aktualizuje metadane dla plików audio przechowywanych w usługach chmurowych:

- **Pokaż komunikat potwierdzenia**  
  Zapytaj przed zastosowaniem zmian metadanych do plików w chmurze.

- **Automatycznie aktualizuj metadane pliku**  
  Zapisz zmiany metadanych do pliku w chmurze automatycznie po edycji.

- **Nie aktualizuj metadanych pliku**  
  Pomiń aktualizację plików w chmurze — zmiany będą stosowane tylko lokalnie.

### Edytuj pliki online

Wybierz, co się dzieje z lokalnymi pobranymi kopiami plików w chmurze po edycji:

- **Zawsze usuwaj pobrany plik**  
  Usuń lokalną kopię po zapisaniu zmian.

- **Nie usuwaj pobranego pliku**  
  Zachowaj pobrany plik na urządzeniu po edycji.

### Przyciski ekranu głównego

Dostosuj, jakie akcje pojawiają się na ekranie głównym edytora tagów (Automatyczne wyszukiwanie tagów, Ręczne wyszukiwanie tagów, Wyszukaj okładkę albumu, Zapisz okładkę albumu, Normalizuj kodowanie, Usuń tagi audio). Możesz również przełączyć **Pokaż rozszerzone tagi** i **Edytuj pliki jednocześnie**, tak aby edytor zawsze otwierał się w preferowanym trybie.
