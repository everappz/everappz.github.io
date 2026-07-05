---
title: "Evertag 4.2: nowe połączenia z chmurą, opcje edytora tagów wyjaśnione"
date: 2026-05-09
description: "Evertag 4.2 dodaje połączenia z Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP i NFS, odświeża Wi-Fi Drive i aktualizuje interfejs pod Liquid Glass. Wpis wyjaśnia także każde ustawienie edytora tagów — w tym ID3v2.4 vs ID3v2.3, skalowanie okładki, duplikowanie tagów, tryby wysyłki do chmury i właściwe opcje dla Spotify oraz innych usług streamingowych."
keywords: ["Evertag 4.2", "aktualizacja Evertag", "edytor tagów ID3 iPhone", "ID3v2.4 vs ID3v2.3", "edycja tagów FLAC iOS", "edycja tagów MP3 iPhone", "edycja okładki albumu iOS", "edytor tagów dla Spotify", "edytor tagów Plex", "edytor tagów Apple Music", "edytor tagów w chmurze Evertag", "edytor tagów Internxt", "edytor tagów Proton Drive", "edytor tagów QNAP", "edytor tagów Nextcloud", "edytor tagów Amazon S3", "edytor tagów SFTP iPhone", "edytor tagów audio FTP", "edytor tagów NFS iPhone", "Wi-Fi Drive edytor tagów", "duplikaty tagów ID3", "skalowanie okładki", "design Liquid Glass", "edytor metadanych audio iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Edytor tagów", "ID3", "ID3v2.4", "ID3v2.3", "Tagi FLAC", "Tagi MP3", "Okładka albumu", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Co nowego"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**W skrócie:** [Evertag 4.2](/products/evertag) to duża aktualizacja edytora tagów audio na iPhone'a, iPada i Maca. Wyeliminowaliśmy kluczowe błędy edycji tagów i dodaliśmy ponad 6 nowych połączeń z chmurą i serwerami — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, oraz protokoły **FTP**, **SFTP** i **NFS**. Wi-Fi Drive ma odświeżony interfejs, tryb wielokrotnego wyboru, mądrzejszą kolejkę przesyłania i szybsze transfery. Cała aplikacja została dostrojona do designu **Liquid Glass**. Wpis zagłębia się także w ustawienia edytora tagów Evertag — wyjaśniając **ID3v2.4 vs ID3v2.3**, **skalowanie okładki**, **duplikowanie tagów**, **tryby wysyłki do chmury**, **usuwanie pobranego pliku** i dokładnie, jakie opcje wybrać przy przygotowywaniu audio dla **Spotify**, **Apple Music**, **Plex**, **Jellyfin** lub dowolnej innej usługi streamingowej.

---

## Cześć wszystkim!

Pojawia się duża aktualizacja Evertag. Wyeliminowaliśmy kluczowe błędy edycji tagów i dodaliśmy **ponad 6 nowych połączeń z chmurą i serwerami**, by zarządzanie metadanymi audio było prostsze niż kiedykolwiek — niezależnie od tego, czy biblioteka mieszka w chmurze stawiającej na prywatność, na NAS-ie samodzielnie hostowanym, czy na zwykłym serwerze FTP/SFTP/NFS.

[Pobierz Evertag 4.2 z App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) albo zaktualizuj się z obecnej wersji.

## Rozszerzona obsługa chmury i serwerów

Evertag łączy się teraz natywnie z szerszym zakresem opcji chmurowych i samodzielnie hostowanych. Możesz edytować tagi ID3, MP4, FLAC, OGG i APE w plikach, gdziekolwiek się znajdują.

### Chmura skupiona na prywatności: Internxt i Proton Drive

Jeśli zależy ci na szyfrowaniu end-to-end i magazynie zero-knowledge, dwie z najbardziej szanowanych chmur stawiających na prywatność są teraz natywnie w Evertag:

- **Internxt** — hiszpańska chmura open-source, z szyfrowaniem post-kwantowym, zgodna z RODO. Dostępny darmowy plan.
- **Proton Drive** — pamięć z szyfrowaniem end-to-end od twórców Proton Mail i Proton VPN, z siedzibą w Szwajcarii. Dostępny darmowy plan i płatne plany dla większych bibliotek.

Możesz teraz edytować metadane bezpośrednio w plikach audio przechowywanych w obu serwisach — plik pozostaje zaszyfrowany w trakcie przesyłu, a do magazynu zapisywane są tylko nowe tagi.

### Rozwiązania samodzielnie hostowane: QNAP, Nextcloud, Amazon S3

Dla użytkowników prowadzących własną infrastrukturę:

- **QNAP** — natywne połączenie API z urządzeniami QNAP NAS. Edytuj tagi w plikach na QNAP-ie przez lokalne Wi-Fi lub zdalny dostęp.
- **Nextcloud** — połącz się z dowolną instancją Nextcloud, samodzielnie hostowaną lub zarządzaną.
- **Amazon S3** — wskaż Evertag dowolny bucket S3 (lub pamięć zgodną z S3 jak Backblaze B2, Wasabi, MinIO, Cloudflare R2) i edytuj metadane na miejscu.

### Nowe protokoły sieciowe: FTP, SFTP, NFS

Evertag 4.2 dodaje trzy klasyczne protokoły dla użytkowników z własnymi serwerami, homelabami lub generycznymi NAS-ami:

- **SFTP (SSH File Transfer Protocol)** — właściwa odpowiedź na **bezpieczną zdalną edycję tagów na własnym serwerze**. SFTP działa na bazie SSH, więc cały transfer (uwierzytelnianie i dane audio) jest szyfrowany. Jeśli masz VPS, serwer dedykowany lub maszynę z Linuksem w domu z dostępem SSH, możesz edytować tagi w plikach zdalnych, nie ujawniając niczego więcej. Obsługuje uwierzytelnianie hasłem i kluczem.
- **FTP** — od dawna ustanowiony standard transferu plików. Przydatne dla starszych domowych NAS-ów udostępniających FTP, ale bez natywnego API.
- **NFS (Network File System)** — de facto protokół udostępniania w Linuksie i większości urządzeń NAS. Mniejszy narzut niż SMB na tym samym sprzęcie.

> **Wskazówka:** SFTP to protokół, którego chcesz do zdalnej edycji przez otwarty internet. FTP i NFS najlepiej używać w sieci lokalnej — nie wystawiaj ich do internetu, chyba że zamkniesz w VPN.

## Ulepszenia Wi-Fi Drive

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) to wbudowana funkcja Evertag do bezprzewodowego przesyłania plików audio między komputerem a iPhone'em lub iPadem — bez iTunes, bez kabli, bez konta w chmurze. Oba urządzenia muszą być w tej samej sieci Wi-Fi.

W Evertag 4.2 Wi-Fi Drive otrzymuje:

- **Odświeżony, nowoczesny interfejs** — czystszy, łatwiejszy do odczytu na pierwszy rzut oka, zaktualizowany dla Liquid Glass.
- **Tryb wielokrotnego wyboru** — wybierz kilka plików lub folderów i działaj na nich hurtowo.
- **Mądrzejsza kolejka przesyłania** — lepsze informacje o postępie i większa odporność na zakłócenia sieci.
- **Lepsza prędkość i ogólna niezawodność** — szybsze transfery dla dużych bibliotek.

To najszybszy sposób, by przenieść partię plików audio z komputera do telefonu, edytować ich tagi i odesłać je z powrotem — bez żadnej usługi zewnętrznej.

## Ustawienia edytora tagów: szczegółowo

To część, której większość użytkowników nigdy nie czyta — i to ona decyduje, czy twoje tagi działają wszędzie, czy tylko w niektórych aplikacjach. Otwórz Evertag i przejdź do sekcji **ustawień edytora tagów audio**. Oto, co naprawdę robi każda opcja i którą wybrać w zależności od celu.

### Skalowanie okładki

Gdy zapisujesz okładkę albumu wewnątrz pliku audio, Evertag może przeskalować obraz przed osadzeniem. Dostępne opcje:

- **Mała** — najmniejszy wpływ na rozmiar pliku, niższa jakość obrazu.
- **Średnia** — wyważony wybór dla większości użytkowników.
- **Duża** — wysoka jakość, odpowiednia dla odtwarzaczy z dużymi ekranami i CarPlay.
- **Ekstra duża** — bardzo wysoka jakość, zauważalny wzrost rozmiaru pliku.
- **Oryginalna (Wyłączone)** — osadza okładkę w oryginalnej rozdzielczości. **Brak skalowania.**

**Dlaczego to ma znaczenie:**

- **Wyższa jakość = większy plik.** Okładka 3000 × 3000 pikseli może dodać kilka MB do każdego utworu. Pomnożone przez cały album sumuje się szybko.
- **Niektóre odtwarzacze źle radzą sobie z bardzo dużymi osadzonymi obrazami.** Starsze urządzenia, niektóre samochodowe panele i część odtwarzaczy desktopowych może zacinać się na okładkach powyżej ~1500 px lub odmówić ich wyświetlenia.
- **Dla większości przepływów chmurowych i streamingowych** **Średnia** lub **Duża** to złoty środek. **Oryginalna** używaj tylko, gdy potrzebujesz jakości archiwalnej lub przygotowujesz pliki dla odtwarzacza, któremu ufasz.

> Opcja **Oryginalna** jest częścią ulepszenia premium personalizacji w Evertag. Standardowe rozmiary (Mała/Średnia/Duża/Ekstra duża) są darmowe.

### Opcje zapisu tagów: ID3v2.4 vs ID3v2.3

To pojedyncze najważniejsze ustawienie kompatybilności. ID3v2 to format metadanych w plikach MP3. Są dwie szeroko używane wersje, różnią się subtelnymi, ale ważnymi szczegółami.

#### ID3v2.4

- Nowsze, obsługuje **kodowanie tekstu UTF-8** — poprawna obsługa pism niełacińskich (chiński, rosyjski, japoński, arabski, hebrajski itd.).
- Więcej typów ramek (głośność względna, presety korektora itd.).
- **Polecane dla nowoczesnych odtwarzaczy**, które je wspierają.

#### ID3v2.3

- Starsze, ale **najbardziej powszechnie wspierana wersja ID3**.
- Nie obsługuje UTF-8 bezpośrednio (używa UTF-16 dla tekstu Unicode).
- **Polecane, gdy potrzebujesz maksymalnej kompatybilności** ze starszymi odtwarzaczami, zestawami samochodowymi i niektórymi aplikacjami desktopowymi.

#### Kiedy włączyć ID3v2.4 w Evertag

- Używasz **nowoczesnych odtwarzaczy audio** jak Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (aktualne wersje) lub nowoczesne odtwarzacze Android. ✅ **Włącz ID3v2.4.**
- Twoja biblioteka zawiera **znaki niełacińskie** (chiński, koreański, japoński, rosyjski, arabski, grecki, hebrajski). ✅ **Włącz ID3v2.4** — UTF-8 obsługuje je znacznie czyściej.

#### Kiedy wyłączyć ID3v2.4 w Evertag (użyj ID3v2.3)

- Przygotowujesz pliki dla **starszego radia samochodowego lub jednostki głównej**, która nie czyta tagów v2.4.
- Widzisz **uszkodzony tekst lub brakujące tagi** w niektórych aplikacjach po edycji — to mocny sygnał, że tam nie wspierane jest v2.4. Wróć do v2.3.
- Celujesz w **starsze odtwarzacze desktopowe** lub starsze odtwarzacze przenośne (wczesne iPody, niektóre odtwarzacze MP3 z lat 2000–2010).

> **Praktyczna zasada:** jeśli twoje tagi wyświetlają się poprawnie wszędzie z v2.4, zostaw włączone. Jeśli choćby jeden ważny odtwarzacz pokazuje błędne znaki, puste pola lub nie czyta tagów, wyłącz v2.4 i zapisz ponownie.

#### Duplikaty tagów

Gdy włączasz **Duplikaty tagów**, Evertag zapisuje wspólne pola metadanych (tytuł, wykonawca, album itd.) w **obu sekcjach ID3v1 i ID3v2** pliku. Poprawia kompatybilność z bardzo starymi odtwarzaczami, które czytają tylko ID3v1 (oryginalny tag 128 bajtów na końcu pliku).

- **Większość użytkowników tego nie potrzebuje.** Nowoczesne odtwarzacze najpierw czytają ID3v2.
- **Włącz tylko, jeśli** masz do czynienia ze sprzętem vintage lub specyficznym oprogramowaniem ignorującym ID3v2.

### Aktualizacja plików online: jak Evertag obsługuje edycje w chmurze

Gdy edytujesz tagi w pliku przechowywanym w podłączonej chmurze (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP itd.), Evertag musi wysłać zmodyfikowany plik z powrotem. Ty kontrolujesz, jak:

- **Pokaż komunikat potwierdzenia** *(domyślne, zalecane)* — Evertag pyta przed wysłaniem. Najlepsze dla ostrożnych użytkowników i bibliotek współdzielonych.
- **Automatycznie aktualizuj metadane pliku** — wysyła po cichu po każdej edycji. Najlepsze dla samodzielnych użytkowników z szybkimi, niezawodnymi łączami, którzy dużo edytują.
- **Nie aktualizuj metadanych pliku** — Evertag edytuje tylko kopię lokalną. Przydatne, by podejrzeć zmiany bez wysyłania ich do chmury.

### Edycja plików online: czyszczenie pliku lokalnego

By edytować zdalny plik, Evertag najpierw pobiera go na urządzenie. Po edycji wybierasz, co dzieje się z tą lokalną kopią:

- **Zawsze usuń pobrany plik** — Evertag usuwa plik tymczasowy po edycji. **Zalecane**, jeśli masz mało miejsca lub pracujesz na cudzych plikach.
- **Nie usuwaj pobranego pliku** — zachowuje edytowany plik na urządzeniu. Przydatne, gdy chcesz mieć kopię offline i zaktualizowaną kopię w chmurze.

### Przyciski na ekranie głównym

Ekran główny edytora tagów Evertag może pokazywać lub ukrywać przyciski poszczególnych operacji. Włącz tylko te, których naprawdę używasz, by interfejs był skupiony:

- **Automatyczne wyszukiwanie tagów audio** — znajduje brakujące metadane online na podstawie odcisku audio pliku.
- **Ręczne wyszukiwanie tagów audio** — szukaj po tytule/wykonawcy, gdy auto-wyszukiwanie zawodzi.
- **Szukaj okładki albumu** — znajduje i osadza wysokiej jakości okładki.
- **Zapisz okładkę albumu** — eksportuje osadzoną okładkę do biblioteki zdjęć lub plików.
- **Normalizuj kodowanie** — naprawia uszkodzony tekst niełaciński spowodowany starymi kodowaniami (bardzo przydatne dla cyrylicy, chińskiego i japońskiego z plików zgranych starym oprogramowaniem).
- **Usuń tagi audio** — usuwa wszystkie tagi z pliku. Przydatne przed świeżym tagowaniem.

### Pokaż rozszerzone tagi

Włącz to, by wyświetlić pełen zestaw pól metadanych poza podstawowym tytuł/wykonawca/album/rok — w tym BPM, dyrygent, oryginalny wykonawca, nastrój, prawa autorskie, koder, komentarze, teksty i więcej. Funkcja dla zaawansowanych; większość zwykłych użytkowników jej nie potrzebuje.

### Edytuj pliki jednocześnie

Gdy włączone, Evertag pozwala edytować metadane na **wielu wybranych plikach naraz** — ustaw ten sam album artist, rok lub gatunek dla całego albumu w jednej operacji. To najszybszy sposób, by uporządkować dużą, nieuporządkowaną bibliotekę.

## Edycja tagów dla Spotify, Apple Music i platform streamingowych

Częste pytanie: «edytowałem tagi w Evertag, wgrałem pliki, a serwis streamingowy pokazuje błędne metadane. O co chodzi?»

Krótka odpowiedź: **serwisy streamingowe nie zawsze respektują twoje lokalne tagi**. Apple Music i Spotify mają własne wewnętrzne bazy danych — gdy rozpoznają utwór, nadpisują wyświetlane metadane swoimi. Ale dla **wgranych plików**, twoich plików lokalnych (funkcja «Biblioteka» Apple Music, Pliki lokalne Spotify) i **wgrań przez dystrybutora na platformy streamingowe**, twoje tagi mają znaczenie. Oto jak ustawić Evertag w każdym scenariuszu:

### Przygotowanie plików dla Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: WŁ.** — Apple Music dobrze obsługuje UTF-8.
- **Okładka albumu: Duża** — aplikacje Apple dobrze pokazują duże okładki; Oryginalna jest przesadą.
- **Duplikaty tagów: WYŁ.** — niepotrzebne.
- Upewnij się, że **Album artist** jest wypełniony poprawnie — Apple Music używa go do grupowania.

### Przygotowanie plików dla Plików lokalnych Spotify

Pliki lokalne Spotify pokazują tylko dobrze otagowane pliki. Tagi czytane przez Spotify są ograniczone.

- **ID3v2.4: WŁ.** w większości przypadków. Jeśli utwór nie wyświetla się poprawnie w Spotify po edycji, **spróbuj zapisać z ID3v2.4 WYŁ.** (czyli jako ID3v2.3) — parser Spotify był historycznie zachowawczy wobec v2.4.
- **Okładka albumu: Średnia lub Duża** — Spotify i tak ją skaluje.
- Wypełnij co najmniej **Tytuł**, **Wykonawca**, **Album** i **Numer utworu**.

### Przygotowanie plików dla wgrań dystrybutora (DistroKid, TuneCore, CD Baby itd.)

Jeśli jesteś artystą wgrywającym własne dzieła do platform streamingowych, twój dystrybutor zwykle czyta tagi, ale prosi też o metadane w swoim UI. Tak czy inaczej:

- **ID3v2.3** to często bezpieczniejsza domyślna opcja — wiele potoków dystrybutorów zbudowano lata temu i preferują starszy format.
- Osadź **Dużą** okładkę (większość dystrybutorów wymaga ≥ 1400 × 1400 px — sprawdź ich wytyczne).
- Nie polegaj na rozszerzonych tagach — dystrybutorzy czytają tylko podstawowe pola.

### Przygotowanie plików dla Plex, Jellyfin, Navidrome, Subsonic, Emby

Te samodzielnie hostowane serwery multimedialne są bardzo tolerancyjne. Czytają zarówno v2.3, jak i v2.4 czysto i dobrze obsługują UTF-8.

- **ID3v2.4: WŁ.** jest w porządku.
- **Okładka albumu: Duża** lub **Ekstra duża** — te serwery serwują okładki klientom mobilnym i ekranom CarPlay, więc jakość ma znaczenie.
- **Album artist** mocno zalecane — to po nim Plex/Jellyfin grupują albumy według artysty.

### Przygotowanie plików dla samochodowych zestawów audio i starszego sprzętu

- **ID3v2.4: WYŁ.** (użyj ID3v2.3) — starsze jednostki główne często nie obsługują v2.4.
- **Okładka albumu: Średnia** — wiele wyświetlaczy samochodowych ma problem z dużymi osadzonymi okładkami.
- **Duplikaty tagów: WŁ.** — starsze radia samochodowe czasami czytają tylko fallback ID3v1.

## Inne ulepszenia

### Design Liquid Glass

Interfejs Evertag 4.2 jest dostrojony do nowego materiału **Liquid Glass** od Apple w całej aplikacji — przezroczyste powierzchnie, płynniejsze animacje i dopracowane elementy sterowania, które naturalnie wpisują się w iOS, iPadOS i macOS.

### Zaktualizowane biblioteki połączeń

Odświeżyliśmy wewnętrzne biblioteki, których Evertag używa do komunikacji z **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** i innymi serwisami. Efekt: mniej awarii połączeń w przypadkach brzegowych, lepsze wsparcie nowszych wersji serwerów i większa niezawodność edycji tagów na plikach zdalnych.

### Poprawki tłumaczeń i lokalizacji

Wiele poprawek językowych w UI w oparciu o bezpośrednie opinie użytkowników. Lepsze dopasowanie tekstu na mniejszych przyciskach w kilku językach.

### Mniejsze szlify zainspirowane waszą opinią

Wiele drobnych usprawnień na podstawie opinii w App Store i e-maili na support@everappz.com. Czytamy każdą wiadomość.

## Pobierz Evertag 4.2

[**Pobierz Evertag z App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) lub zaktualizuj się przez App Store. Evertag to bezpłatne pobranie z opcjonalnymi ulepszeniami w aplikacji dla zaawansowanych funkcji. Nowe połączenia z chmurą, protokoły sieciowe, ulepszenia Wi-Fi Drive i interfejs Liquid Glass są częścią aktualizacji bazowej.

Jeśli aplikacja ci się podoba, zostaw ocenę w App Store — to naprawdę pomaga. Masz uwagi albo trafiłeś na problem? Napisz do nas na **support@everappz.com**. Czytamy każdą wiadomość.

## Najczęściej zadawane pytania

{{% details title="Co nowego w Evertag 4.2?" closed="true" %}}
Evertag 4.2 dodaje ponad 6 nowych połączeń z chmurą i serwerami (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), odświeżony Wi-Fi Drive z wielokrotnym wyborem i mądrzejszą kolejką przesyłania, aktualizacje UI Liquid Glass, zaktualizowane biblioteki połączeń, kluczowe poprawki edycji tagów oraz usprawnienia tłumaczenia.
{{% /details %}}

{{% details title="Czy używać ID3v2.4 czy ID3v2.3 w Evertag?" closed="true" %}}
Używaj **ID3v2.4** dla nowoczesnych odtwarzaczy (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, nowoczesne aplikacje Android) i bibliotek z znakami niełacińskimi — wsparcie UTF-8 oznacza czystsze tagi po chińsku, koreańsku, japońsku, rosyjsku, arabsku i hebrajsku. Używaj **ID3v2.3**, jeśli twoje tagi wyświetlają się błędnie w niektórych aplikacjach, jeśli celujesz w starsze radia samochodowe lub jeśli potok dystrybutora streamingowego odrzuca v2.4. Zawsze możesz przełączyć i zapisać ponownie.
{{% /details %}}

{{% details title="Dlaczego moje tagi są błędne w Spotify po edycji?" closed="true" %}}
Spotify w większości pokazuje metadane z własnego katalogu — twoje lokalne tagi są używane tylko dla «Plików lokalnych» lub treści wgranych przez ciebie jako artystę. Jeśli tagujesz pliki dla Plików lokalnych Spotify i nie wyświetlają się poprawnie, spróbuj wyłączyć ID3v2.4 w Evertag i zapisać jako ID3v2.3 — parser Spotify był historycznie zachowawczy wobec v2.4.
{{% /details %}}

{{% details title="Jaki rozmiar okładki wybrać w Evertag?" closed="true" %}}
Dla większości użytkowników: **Duża**. Wygląda świetnie na telefonach, iPadach, Macach i nowoczesnych wyświetlaczach samochodowych, nie zwiększając zbyt mocno rozmiaru plików. Używaj **Średniej**, jeśli masz ogromną bibliotekę i chcesz oszczędzać dysk. Używaj **Oryginalnej** (bez skalowania) tylko do masterów archiwalnych lub gdy naprawdę potrzebujesz maksymalnej jakości — pamiętaj, że niektóre starsze odtwarzacze mają trudność z bardzo dużymi osadzonymi okładkami. **Oryginalna** jest częścią ulepszenia premium personalizacji w Evertag.
{{% /details %}}

{{% details title="Czy większe okładki sprawią, że moje pliki będą większe?" closed="true" %}}
Tak. Osadzenie okładki 3000 × 3000 px może dodać kilka megabajtów do pojedynczego pliku audio. W bibliotece 1000 utworów daje gigabajty. Jeśli ciasno z miejscem, używaj Średniej lub Dużej; jeśli streamujesz z NAS-a, gdzie rozmiar nie ma znaczenia, Ekstra duża lub Oryginalna są w porządku.
{{% /details %}}

{{% details title="Czym są duplikaty tagów i czy je włączać?" closed="true" %}}
Duplikaty tagów zapisują metadane podstawowe zarówno w sekcji ID3v1 (legacy 128 bajtów), jak i ID3v2 (nowoczesna) pliku. Włącz tylko, jeśli celujesz w bardzo stare odtwarzacze lub sprzęt czytający ID3v1. Dla wszystkiego nowoczesnego (smartfony, komputery, nowsze radia samochodowe) zostaw wyłączone.
{{% /details %}}

{{% details title="Czy Evertag edytuje tagi bezpośrednio w plikach w chmurze?" closed="true" %}}
Tak. Połącz się z chmurą (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3 itd.) lub przez FTP/SFTP/NFS, otwórz plik i edytuj tagi tak, jakby był lokalny. Evertag pobiera plik, stosuje twoje zmiany i wysyła zaktualizowaną wersję z powrotem. W ustawieniach możesz wybrać między trybami «Zawsze pytaj», «Auto-wysyłka» lub «Nie wysyłaj».
{{% /details %}}

{{% details title="Czy mogę edytować tagi FLAC na iPhonie z Evertag?" closed="true" %}}
Tak. Evertag obsługuje FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE i inne ważne formaty z pełnym wsparciem odczytu/zapisu tagów, łącznie z osadzoną okładką.
{{% /details %}}

{{% details title="Jak bezpiecznie edytować tagi na domowym serwerze przez SFTP?" closed="true" %}}
Otwórz Evertag, przejdź do Połączeń, wybierz SFTP i wpisz nazwę hosta lub IP serwera, port (zwykle 22), nazwę użytkownika oraz hasło lub prywatny klucz SSH. Evertag przejdzie po twoich zdalnych folderach i będzie edytował tagi bezpośrednio z szyfrowaniem end-to-end po SSH.
{{% /details %}}

{{% details title="Czy mogę edytować tagi w wielu plikach naraz?" closed="true" %}}
Tak. Włącz **Edytuj pliki jednocześnie** w ustawieniach. Wybierz wiele plików, otwórz edytor tagów, a każde pole, które zmienisz, zostanie zastosowane do wszystkich wybranych plików. To najszybszy sposób, by ustawić ten sam album artist, rok lub gatunek na całym albumie.
{{% /details %}}

{{% details title="Czy aktualizacja Evertag 4.2 jest darmowa?" closed="true" %}}
Tak. Evertag to bezpłatne pobranie z App Store, a 4.2 to bezpłatna aktualizacja dla wszystkich istniejących użytkowników. Nowe integracje chmurowe, ulepszenia Wi-Fi Drive i UI Liquid Glass są częścią aktualizacji bazowej.
{{% /details %}}

{{% details title="Na jakich urządzeniach jest dostępny Evertag 4.2?" closed="true" %}}
Evertag 4.2 działa na iPhonie, iPadzie i Macu. Synchronizacja iCloud Drive utrzymuje twoje ustawienia edytora tagów spójne między urządzeniami.
{{% /details %}}
