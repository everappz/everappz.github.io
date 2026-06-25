---
title: "Jak pobrać metadane, ikony i zrzuty ekranu z App Store za darmo"
date: 2026-06-13
description: "Przewodnik krok po kroku, jak pobrać metadane, ikonę, zrzuty ekranu i zlokalizowane szczegóły App Store dowolnej aplikacji iOS przy użyciu AppLookup.pro, darmowego narzędzia przeglądarkowego opartego na oficjalnym iTunes Search API."
keywords: [
  "metadane app store", "pobierz dane app store", "pobierz ikonę app store",
  "pobierz zrzuty ekranu app store", "narzędzie wyszukiwania app store", "itunes search api",
  "ekstraktor metadanych aplikacji", "metadane aplikacji iOS", "darmowe narzędzie api app store",
  "pobierz ikonę aplikacji w wysokiej rozdzielczości", "analiza konkurencji app store",
  "zlokalizowane dane app store", "wyszukiwanie kraju app store", "darmowe narzędzie aso"
]
tags: [
  "Metadane App Store", "Wyszukiwanie aplikacji", "iTunes Search API",
  "Pobieranie ikony aplikacji", "Zrzuty ekranu aplikacji", "Analiza ASO"
]
sidebar:
  exclude: true
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

## Pobierz dane App Store w sekundach

**Krótka wersja:** [AppLookup.pro](https://applookup.pro) to darmowe narzędzie, które pobiera publiczne dane dowolnej aplikacji iOS, iPadOS, macOS lub tvOS. Otrzymujesz tytuł, opis, nowości, wersję, cenę, oceny, ikonę aplikacji, zrzuty ekranu, obsługiwane urządzenia oraz surową odpowiedź iTunes API. Każde pole ma przycisk kopiowania jednym dotknięciem. Otwórz stronę, wklej link do App Store lub wpisz nazwę aplikacji, a otrzymasz dane.

Użyj go do:

- **Analizy ASO.** Zobacz, jak topowe aplikacje piszą swoje tytuły, podtytuły, opisy i słowa kluczowe.
- **Śledzenia konkurencji.** Sprawdź aktualizacje wersji, oceny i ceny na różnych rynkach.
- **Pobierania zasobów.** Zapisz oficjalną ikonę aplikacji i pełnowymiarowe zrzuty ekranu w jednym pliku ZIP.
- **Sprawdzania lokalizacji.** Porównaj opis, nowości i zrzuty ekranu w ponad 40 krajach App Store.
- **Testowania API.** Skopiuj surowy JSON iTunes Search API bezpośrednio do swojego kodu lub Postmana.

## Czym jest AppLookup.pro?

[AppLookup.pro](https://applookup.pro) to darmowe narzędzie do wyszukiwania w App Store oparte na przeglądarce. Działa w całości na twoim urządzeniu. Każdy wynik pochodzi bezpośrednio z oficjalnego [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) firmy Apple. Bez scrapowania. Bez rejestracji. Bez śledzenia.

### Co otrzymujesz

- **Wyszukiwanie po nazwie aplikacji lub URL App Store.** Autouzupełnianie pokazuje wyniki na żywo podczas pisania.
- **Ponad 40 sklepów krajowych.** Przełączaj się między US, UK, JP, DE, FR, BR i innymi.
- **Pełne metadane.** Tytuł, podtytuł, deweloper, identyfikator pakietu, wersja, cena, rozmiar pliku, oceny, data wydania, klasyfikacja treści, języki i obsługiwane urządzenia.
- **Zasoby w wysokiej rozdzielczości.** Ikony aplikacji i zrzuty ekranu dla iPhone, iPad, macOS i Apple TV.
- **Pobieranie ZIP zbiorczo.** Pobierz wszystkie ikony lub wszystkie zrzuty ekranu w jednym archiwum.
- **Surowy JSON iTunes API.** Dokładna odpowiedź od Apple, gotowa do skopiowania.
- **Przyciski kopiowania w każdym polu.** Jedno dotknięcie umieszcza wartość w schowku.

## Jak używać AppLookup.pro krok po kroku

### Krok 1. Wprowadź nazwę aplikacji lub wklej URL App Store

Otwórz [applookup.pro](https://applookup.pro) i zacznij wpisywać nazwę aplikacji. Autouzupełnianie pokazuje wyniki App Store na żywo podczas pisania.

Możesz także wkleić bezpośredni link App Store, taki jak `https://apps.apple.com/us/app/instagram/id389801252`, lub po prostu identyfikator aplikacji. Narzędzie wyodrębni identyfikator za ciebie. Obsługuje również URL-e przekierowań Google.

![Wprowadź nazwę aplikacji lub URL App Store do AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Krok 2. Pobierz informacje o aplikacji i pobierz ikonę

Kliknij **Lookup** lub naciśnij Enter. Narzędzie wywołuje oficjalne iTunes Search API i pokazuje ikonę aplikacji, nazwę dewelopera, ocenę, wersję i cenę w czasie poniżej sekundy.

Przewiń do sekcji **App Icon**. Każdy rozmiar ikony, który zwraca Apple, pojawia się jako karta. Każda karta ma:

- **Direct Link.** Otwiera obraz w pełnym rozmiarze w nowej karcie.
- **Download.** Zapisuje plik na twoim komputerze.

Użyj **Download All Icons (ZIP)**, aby pobrać wszystkie rozmiary ikon w jednym archiwum. To samo dotyczy zrzutów ekranu: każda sekcja platformy ma własny przycisk **Download All (ZIP)**.

![Pobierz ikony aplikacji i zrzuty ekranu z AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Krok 3. Przeczytaj szczegóły aplikacji i skopiuj dowolne pole

Przewiń do **App Details**. Zobaczysz identyfikator pakietu, wersję, cenę, rozmiar pliku, minimalny OS, datę wydania, datę ostatniej aktualizacji, klasyfikację treści, gatunki, identyfikatory gatunków, języki, sprzedawcę, identyfikator artysty i identyfikator utworu.

Dotknij przycisku **Copy** na dowolnej karcie. Wartość trafia do twojego schowka, a przycisk pokazuje zielony znacznik «Copied».

To samo działa dla **Description**, **What's New** i **Supported Devices**. Te sekcje są przewijane, więc możesz przeczytać cały tekst bez utraty miejsca, a przycisk Copy umieszcza całe pole w schowku.

![Wyświetl pełne szczegóły App Store i skopiuj dowolne pole jednym dotknięciem](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Krok 4. Wyświetl surową odpowiedź API App Store

Potrzebujesz dokładnego JSON, który zwraca Apple? Przewiń do **Raw API Response**. Pełny ładunek iTunes Search API jest pokazany w przewijanym podglądzie z przyciskiem **Copy** u góry. Jedno dotknięcie kopiuje cały obiekt JSON.

**iTunes Lookup URL** jest pokazany tuż nad nim. Wklej go do Postmana, curl lub przeglądarki, aby powtórzyć to samo żądanie.

![Wyświetl i skopiuj surową odpowiedź JSON iTunes Search API](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Krok 5. Zmień kraj, aby zobaczyć zlokalizowaną wersję

Metadane App Store zmieniają się w zależności od kraju. Ta sama aplikacja często ma inny tytuł, podtytuł, opis, zrzuty ekranu i cenę na każdym rynku.

Wybierz kraj z rozwijanego menu u góry. URL w polu wprowadzania aktualizuje się automatycznie. Kliknij **Lookup** ponownie, aby ponownie pobrać aplikację na tym rynku.

To najszybszy sposób, aby sprawdzić, jak konkurent przedstawia swoją aplikację w Japonii, Niemczech, Brazylii lub w którymkolwiek z ponad 40 obsługiwanych krajów.

![Przełącz sklepy krajowe, aby zobaczyć zlokalizowane metadane App Store](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Krok 6. Skopiuj zlokalizowane metadane

Gdy wynik kraju się załaduje, każde pole działa tak samo. Dotknij **Copy** w opisie, nowościach, nazwie aplikacji, deweloperze, identyfikatorze pakietu lub dowolnej karcie szczegółów, aby przechwycić zlokalizowany tekst.

Ułatwia to budowanie arkuszy porównawczych obok siebie lub przekazywanie zlokalizowanej treści do przeglądu tłumaczeń.

![Skopiuj zlokalizowany opis i metadane App Store jednym dotknięciem](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Kto używa AppLookup.pro

- **Niezależni deweloperzy** prowadzący analizę ASO przed premierą.
- **Zespoły ASO i marketingu** śledzące aktualizacje i ceny konkurencji.
- **Projektanci** pobierający oficjalną ikonę aplikacji w wysokiej rozdzielczości i zrzuty ekranu do zestawów prasowych i studiów przypadków.
- **Zespoły lokalizacyjne** audytujące, które rynki są pokryte i gdzie nadal dostarczany jest domyślny angielski tekst.
- **Inżynierowie backend i QA** testujący integracje iTunes Search API bez pisania scrapera.
- **Pisarze i blogerzy** potrzebujący oficjalnej ikony aplikacji i kilku zrzutów ekranu do wpisu.

## Prywatność i zastrzeżenie

AppLookup.pro działa w twojej przeglądarce. Nie ma logowania. Nie ma śledzenia. Nie ma rejestrowania na serwerze aplikacji, które wyszukujesz. Żądania idą bezpośrednio z twojej przeglądarki do [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) firmy Apple.

To narzędzie służy wyłącznie do **celów edukacyjnych i badawczych**. Wszystkie dane są pobierane z oficjalnego publicznego API firmy Apple i pozostają własnością Apple Inc. oraz wymienionych wydawców aplikacji. Korzystanie z narzędzia podlega [Apple Media Services Terms and Conditions](https://www.apple.com/legal/internet-services/terms/site.html). Prosimy o przestrzeganie limitów Apple i nierozpowszechnianie zasobów chronionych prawem autorskim.

## Wypróbuj teraz

Nie potrzebujesz klucza API, konta dewelopera ani płatnego planu, aby sprawdzić dane App Store. Otwórz [applookup.pro](https://applookup.pro), wklej dowolny URL App Store, a otrzymasz metadane, ikony i surowy JSON w sekundach.

## Open Source

AppLookup.pro to oprogramowanie open source. Zgłoszenia błędów, dodawanie krajów i pull requesty są mile widziane.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro na GitHubie" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Najczęściej zadawane pytania

{{% details title="Czy AppLookup.pro jest naprawdę darmowy?" closed="true" %}}
Tak. AppLookup.pro jest w 100 procentach darmowy i open source. Działa w twojej przeglądarce. Nie ma rejestracji, nie ma płatnego planu i nie ma limitu użytkowania poza limitami własnego iTunes Search API firmy Apple.
{{% /details %}}

{{% details title="Skąd pochodzą dane?" closed="true" %}}
Każdy wynik jest pobierany w czasie rzeczywistym z oficjalnego [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) firmy Apple. Narzędzie nie scrapuje stron App Store i nie buforuje odpowiedzi na żadnym serwerze.
{{% /details %}}

{{% details title="Czy mogę pobrać ikonę aplikacji w wysokiej rozdzielczości?" closed="true" %}}
Tak. Sekcja **App Icon** pokazuje każdy URL ikony, który zwraca Apple. Każda karta ma Direct Link i przycisk Download, a przycisk Download All Icons ZIP pakuje je w jedno archiwum.
{{% /details %}}

{{% details title="Czy mogę pobrać wszystkie zrzuty ekranu App Store naraz?" closed="true" %}}
Tak. Każda sekcja zrzutów ekranu (iPhone, iPad, macOS i Apple TV) ma przycisk **Download All (ZIP)**, który grupuje każdy zrzut ekranu w pełnej rozdzielczości.
{{% /details %}}

{{% details title="Jak zobaczyć, jak aplikacja wygląda w innym kraju?" closed="true" %}}
Wybierz kraj z rozwijanego menu u góry strony. Obsługiwanych jest ponad 40 sklepów. Kliknij **Lookup** ponownie, a narzędzie pobierze aplikację dla tego kraju, pokazując zlokalizowany tytuł, opis, zrzuty ekranu, nowości i cenę.
{{% /details %}}

{{% details title="Czy mogę kopiować pojedyncze pola, takie jak identyfikator pakietu lub data wydania?" closed="true" %}}
Tak. Każde pole tekstowe w wyniku ma własny przycisk Copy: nazwa aplikacji, deweloper, opis, nowości, identyfikator pakietu, wersja, cena, rozmiar pliku, minimalny OS, data wydania, klasyfikacja treści, języki, obsługiwane urządzenia i surowy JSON.
{{% /details %}}

{{% details title="Czy AppLookup.pro działa dla dowolnej aplikacji iOS?" closed="true" %}}
Działa dla każdej aplikacji, która jest publicznie wyświetlana w co najmniej jednym kraju App Store i zwracana przez iTunes Search API. Aplikacje niewyświetlane, usunięte lub dystrybuowane w przedsiębiorstwie nie pojawią się.
{{% /details %}}

{{% details title="Czy obsługuje aplikacje macOS i Apple TV?" closed="true" %}}
Tak. Jeśli aplikacja ma zrzuty ekranu macOS lub Apple TV w odpowiedzi iTunes Search API, AppLookup.pro pokazuje je we własnym przewijanym panelu z przyciskami pobierania.
{{% /details %}}

{{% details title="Czy mogę użyć surowego JSON we własnym kodzie?" closed="true" %}}
Tak. Sekcja Raw API Response pokazuje dokładny JSON, który zwraca Apple. Skopiuj go do Postmana, testu jednostkowego lub pipeline'u backend. Prosimy o przestrzeganie warunków API firmy Apple i rozsądnych limitów.
{{% /details %}}

{{% details title="Czy bezpiecznie jest wkleić URL-e App Store do narzędzia?" closed="true" %}}
Tak. URL jest parsowany w twojej przeglądarce. Jedyne wychodzące wywołanie sieciowe to wyszukiwanie w iTunes Search API firmy Apple.
{{% /details %}}

{{% details title="Jaka jest różnica między AppLookup.pro a AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) służy do odczytywania metadanych App Store z dowolnej opublikowanej aplikacji: analiza konkurencji, pobieranie zasobów, sprawdzanie lokalizacji. [AppKeywords.pro](https://appkeywords.pro) służy do pisania metadanych App Store dla twojej własnej aplikacji: optymalizacja tytułu, podtytułu i słów kluczowych ze wsparciem Fastlane. Te dwa narzędzia dobrze ze sobą współpracują.
{{% /details %}}
