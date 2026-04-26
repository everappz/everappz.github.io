---
title: "Jak zaimportować listę odtwarzania M3U do Evermusic i Flacbox"
date: 2024-01-31
description: "Dowiedz się, jak importować pliki list odtwarzania M3U, M3U8 i CUE z chmury, pamięci lokalnej lub urządzenia do Evermusic i Flacbox."
keywords: ["evermusic", "flacbox", "lista odtwarzania", "m3u", "m3u8", "cue", "import", "aplikacja muzyczna"]
tags: ["evermusic", "import", "listy odtwarzania", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Podsumowanie:** Evermusic i Flacbox obsługują import plików list odtwarzania M3U, M3U8 i CUE z pamięci w chmurze, lokalnych plików aplikacji lub urządzenia. Przejdź do Listy odtwarzania > Więcej > Importuj listę odtwarzania, wybierz źródło, wybierz plik, a aplikacja automatycznie utworzy listę odtwarzania.

M3U, co oznacza MP3 URL lub Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, to format pliku komputerowego używany do multimedialnych list odtwarzania. Jednym z jego głównych zastosowań jest tworzenie plików list odtwarzania z pojedynczym wpisem wskazujących na strumienie w Internecie. Pliki te oferują wygodny dostęp do treści strumieniowych i są powszechnie używane do pobierania, wysyłania e-maili i słuchania radia internetowego.

Pomimo szerokiego zastosowania nie istnieje formalna specyfikacja formatu M3U; stał się on standardem de facto. Plik M3U to zasadniczo zwykły plik tekstowy określający lokalizacje jednego lub więcej plików multimedialnych. W zależności od kodowania jest zapisywany z rozszerzeniem "m3u" lub "m3u8". Każdy wpis w pliku określa lokalizację pliku multimedialnego, która może być bezwzględną ścieżką lokalną, ścieżką lokalną względem lokalizacji pliku M3U lub adresem URL. Wpisy są oddzielone znakami nowego wiersza, a niektóre urządzenia wymagają znaków nowego wiersza reprezentowanych jako CR LF.

Ponadto pliki M3U mogą zawierać komentarze poprzedzone znakiem "#". W rozszerzonym M3U "#" wprowadza rozszerzone dyrektywy M3U, które mogą obsługiwać parametry zakończone dwukropkiem ":".

W naszych aplikacjach Evermusic i Flacbox zaimplementowaliśmy funkcjonalność importu plików M3U, eliminując potrzebę ręcznego tworzenia list odtwarzania. Ten przewodnik przeprowadzi Cię przez import list odtwarzania z pamięci w chmurze, plików lokalnych lub plików na urządzeniu bezpośrednio do aplikacji.

Najpierw przejdź do sekcji 'Listy odtwarzania'. Następnie dotknij przycisku 'Więcej' w prawym górnym rogu. Z menu, które się pojawi, wybierz opcję 'Importuj listę odtwarzania'.

![akcja importu listy odtwarzania](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Na następnym ekranie wybierz lokalizację pliku. Obsługiwane opcje to:

- Połączona pamięć w chmurze;
- Pliki w aplikacji;
- Pliki na urządzeniu;

![wybierz lokalizację pliku](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Wybierzmy połączoną pamięć w chmurze i otwórzmy folder zawierający plik listy odtwarzania. Obsługiwane rozszerzenia plików list odtwarzania to M3U, M3U8 i CUE. Wybierz plik listy odtwarzania i dotknij 'Zrobione', aby potwierdzić wybór.

![wybierz plik M3U](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Aplikacja przeanalizuje plik listy odtwarzania i utworzy listę utworów. Następnie zlokalizuje te pliki w pamięci i skompiluje ostateczną listę odtwarzania, która zostanie zaimportowana do biblioteki muzycznej. Kluczowe jest, aby plik M3U/CUE zawierał prawidłowe ścieżki do plików multimedialnych, a pliki powinny znajdować się w tych ścieżkach w pamięci.

![zaimportowana lista odtwarzania](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Aplikacja obsługuje zarówno ścieżki względne, jak i bezwzględne adresy URL plików.

Na przykład:

Lista odtwarzania ze ścieżkami względnymi:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Lista odtwarzania z bezwzględnymi adresami URL:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Jeśli importujesz plik listy odtwarzania znajdujący się w aplikacji (sekcja Pliki lokalne), nie są wymagane dodatkowe kroki.

Jeśli jednak chcesz zaimportować listę odtwarzania znajdującą się na urządzeniu za pomocą systemowego selektora plików, jest ważna kwestia do zapamiętania.

Ze względu na polityki bezpieczeństwa aplikacja może uzyskać dostęp tylko do pliku wybranego za pomocą systemowego selektora plików. Jednak plik listy odtwarzania może zawierać linki do innych plików multimedialnych na urządzeniu. Aby zaimportować listę odtwarzania z urządzenia, musisz wybrać folder zawierający zarówno plik listy odtwarzania, jak i wszystkie powiązane pliki multimedialne. W takim przypadku aplikacja przeskanuje wybrany folder, znajdzie plik listy odtwarzania, zbuduje listę utworów i zaimportuje ją do biblioteki muzycznej.

Dodatkowo możesz zaimportować wiele list odtwarzania jednocześnie, dotykając przycisku "Więcej akcji" i wybierając "Importuj listy odtwarzania z folderu". Aplikacja przeskanuje zawartość folderu, znajdzie obsługiwane pliki list odtwarzania i zaimportuje je do biblioteki.

## Najczęściej zadawane pytania

{{% details title="Jakie formaty list odtwarzania obsługują Evermusic i Flacbox?" closed="true" %}}
Obie aplikacje obsługują formaty plików list odtwarzania M3U, M3U8 i CUE. Obejmują one najczęściej używane standardy list odtwarzania stosowane przez odtwarzacze muzyki i oprogramowanie multimedialne.
{{% /details %}}

{{% details title="Czy mogę importować listy odtwarzania z pamięci w chmurze?" closed="true" %}}
Tak. Możesz importować pliki list odtwarzania z dowolnej połączonej usługi pamięci w chmurze, w tym Google Drive, Dropbox, OneDrive i serwerów WebDAV.
{{% /details %}}

{{% details title="Dlaczego po imporcie brakuje niektórych utworów?" closed="true" %}}
Plik listy odtwarzania musi zawierać prawidłowe ścieżki do plików multimedialnych, a pliki te muszą istnieć w określonych lokalizacjach w pamięci. Sprawdź, czy ścieżki plików w pliku M3U lub CUE odpowiadają rzeczywistym lokalizacjom plików.
{{% /details %}}

{{% details title="Czy mogę zaimportować wiele list odtwarzania jednocześnie?" closed="true" %}}
Tak. Użyj przycisku Więcej akcji i wybierz "Importuj listy odtwarzania z folderu". Aplikacja przeskanuje folder w poszukiwaniu wszystkich obsługiwanych plików list odtwarzania i zaimportuje je w jednym kroku.
{{% /details %}}

{{% details title="Czy muszę ręcznie tworzyć listy odtwarzania?" closed="true" %}}
Nie. Funkcja importu eliminuje ręczne tworzenie list odtwarzania. Po prostu wskaż aplikacji istniejący plik M3U, M3U8 lub CUE, a automatycznie utworzy listę odtwarzania.
{{% /details %}}
