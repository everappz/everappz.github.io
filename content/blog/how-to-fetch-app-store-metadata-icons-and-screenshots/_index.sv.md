---
title: "Så hämtar du App Store-metadata, ikoner och skärmbilder gratis"
date: 2026-06-13
description: "Steg för steg-guide för att hämta metadata, ikon, skärmbilder och lokaliserade App Store-detaljer för vilken iOS-app som helst med AppLookup.pro, ett gratis webbläsarverktyg som bygger på det officiella iTunes Search API."
keywords: [
  "app store metadata", "hämta app store-data", "ladda ner app store-ikon",
  "ladda ner app store-skärmbilder", "app store sökverktyg", "itunes search api",
  "app metadata-extraktor", "iOS app metadata", "gratis app store api verktyg",
  "ladda ner app-ikon hög upplösning", "app store konkurrentanalys",
  "lokaliserade app store-data", "app store land sökning", "gratis aso verktyg"
]
tags: [
  "App Store-metadata", "App-sökning", "iTunes Search API",
  "Nedladdning av app-ikoner", "App-skärmbilder", "ASO-research"
]
sidebar:
  exclude: true
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Få App Store-data på sekunder

**Kortversion:** [AppLookup.pro](https://applookup.pro) är ett gratis verktyg som hämtar offentlig data för alla iOS-, iPadOS-, macOS- eller tvOS-appar. Du får titel, beskrivning, vad som är nytt, version, pris, betyg, appikon, skärmbilder, enheter som stöds och det råa svaret från iTunes API. Varje fält har en kopieringsknapp med ett tryck. Öppna sajten, klistra in en App Store-länk eller skriv appnamnet, så har du datan.

Använd det för:

- **ASO-research.** Se hur topp-apparna skriver sina titlar, underrubriker, beskrivningar och sökord.
- **Bevaka konkurrenter.** Kolla versionsuppdateringar, betyg och priser mellan marknader.
- **Ladda ner tillgångar.** Spara den officiella appikonen och skärmbilder i full storlek i en ZIP.
- **Lokaliseringskontroller.** Jämför beskrivning, vad som är nytt och skärmbilder i över 40 App Store-länder.
- **API-testning.** Kopiera det råa JSON-svaret från iTunes Search API direkt in i din kod eller Postman.

## Vad är AppLookup.pro?

[AppLookup.pro](https://applookup.pro) är ett gratis, webbläsarbaserat verktyg för App Store-sökning. Det körs helt på din enhet. Varje resultat kommer direkt från Apples officiella [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html). Ingen scraping. Ingen registrering. Ingen spårning.

### Vad du får

- **Sök efter appnamn eller App Store-URL.** Autoifyllning visar live-resultat medan du skriver.
- **Över 40 landsbutiker.** Växla mellan US, UK, JP, DE, FR, BR med flera.
- **Fullständig metadata.** Titel, underrubrik, utvecklare, bundle ID, version, pris, filstorlek, betyg, släppdatum, innehållsklassificering, språk och enheter som stöds.
- **Tillgångar i hög upplösning.** Appikoner och skärmbilder för iPhone, iPad, macOS och Apple TV.
- **Massnedladdning som ZIP.** Hämta alla ikoner eller alla skärmbilder i ett arkiv.
- **Råt JSON från iTunes API.** Det exakta svaret från Apple, redo att kopiera.
- **Kopieringsknappar på varje fält.** Ett tryck lägger värdet i ditt urklipp.

## Så använder du AppLookup.pro steg för steg

### Steg 1. Ange appnamnet eller klistra in en App Store-URL

Öppna [applookup.pro](https://applookup.pro) och börja skriva appnamnet. Autoifyllning visar live-resultat från App Store medan du skriver.

Du kan också klistra in en direkt App Store-länk som `https://apps.apple.com/us/app/instagram/id389801252` eller bara app-ID:t. Verktyget plockar ut ID:t åt dig. Det hanterar även Google-omdirigerings-URL:er.

![Ange ett appnamn eller en App Store-URL i AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Steg 2. Hämta appinfon och ladda ner ikonen

Klicka på **Lookup** eller tryck Enter. Verktyget anropar det officiella iTunes Search API och visar appikonen, utvecklarens namn, betyg, version och pris på under en sekund.

Scrolla till sektionen **App Icon**. Varje ikonstorlek som Apple returnerar visas som ett kort. Varje kort har:

- **Direct Link.** Öppnar bilden i full storlek i en ny flik.
- **Download.** Sparar filen till din dator.

Använd **Download All Icons (ZIP)** för att hämta alla ikonstorlekar i ett arkiv. Detsamma gäller skärmbilder: varje plattformssektion har en egen **Download All (ZIP)**-knapp.

![Ladda ner appikoner och skärmbilder från AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Steg 3. Läs appdetaljerna och kopiera vilket fält som helst

Scrolla till **App Details**. Du ser bundle ID, version, pris, filstorlek, lägsta OS, släppdatum, datum för senaste uppdatering, innehållsklassificering, genrer, genre-ID:n, språk, säljare, artist-ID och track-ID.

Tryck på knappen **Copy** på ett kort. Värdet hamnar i ditt urklipp och knappen visar en grön 'Copied'-bock.

Samma sak fungerar för **Description**, **What's New** och **Supported Devices**. Dessa sektioner är scrollbara så du kan läsa hela texten utan att tappa platsen, och Copy-knappen lägger hela fältet i ditt urklipp.

![Visa fullständiga App Store-detaljer och kopiera vilket fält som helst med ett tryck](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Steg 4. Visa det råa svaret från App Store API

Behöver du den exakta JSON som Apple returnerar? Scrolla till **Raw API Response**. Hela payloaden från iTunes Search API visas i en scrollbar vy med en **Copy**-knapp högst upp. Ett tryck kopierar hela JSON-objektet.

**iTunes Lookup URL** visas precis ovanför. Klistra in den i Postman, curl eller din webbläsare för att spela upp samma begäran igen.

![Visa och kopiera det råa JSON-svaret från iTunes Search API](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Steg 5. Byt land för att se den lokaliserade versionen

App Store-metadata varierar mellan länder. Samma app har ofta olika titel, underrubrik, beskrivning, skärmbilder och pris på varje marknad.

Välj ett land i rullgardinsmenyn högst upp. URL:en i inmatningsfältet uppdateras automatiskt. Klicka på **Lookup** igen för att hämta appen i den marknaden på nytt.

Det är det snabbaste sättet att se hur en konkurrent presenterar sin app i Japan, Tyskland, Brasilien eller någon av de över 40 länder som stöds.

![Byt landsbutik för att se lokaliserad App Store-metadata](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Steg 6. Kopiera den lokaliserade metadatan

När landsresultatet har laddats fungerar varje fält på samma sätt. Tryck på **Copy** på beskrivningen, vad som är nytt, appnamnet, utvecklaren, bundle ID eller något detaljkort för att fånga den lokaliserade texten.

Det gör det enkelt att bygga jämförelsetabeller sida vid sida eller att skicka in lokaliserad text för översättningsgranskning.

![Kopiera lokaliserad App Store-beskrivning och metadata med ett tryck](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Vem använder AppLookup.pro

- **Indieutvecklare** som gör ASO-research inför en lansering.
- **ASO- och marknadsteam** som följer konkurrenters uppdateringar och priser.
- **Designers** som hämtar den officiella högupplösta appikonen och skärmbilder för presskit och fallstudier.
- **Lokaliseringsteam** som granskar vilka marknader som täcks och var den engelska standardtexten fortfarande används.
- **Backend- och QA-ingenjörer** som testar iTunes Search API-integrationer utan att skriva en scraper.
- **Skribenter och bloggare** som behöver den officiella appikonen och några skärmbilder för ett inlägg.

## Integritet och ansvarsfriskrivning

AppLookup.pro körs i din webbläsare. Det finns ingen inloggning. Det finns ingen spårning. Det finns ingen serverloggning av apparna du slår upp. Begäranden går direkt från din webbläsare till Apples [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html).

Det här verktyget är **endast avsett för utbildnings- och researchsyfte**. All data hämtas från Apples officiella publika API och förblir egendom hos Apple Inc. och de listade apputgivarna. Användning av verktyget omfattas av [Apple Media Services Villkor](https://www.apple.com/legal/internet-services/terms/site.html). Respektera Apples hastighetsgränser och distribuera inte vidare upphovsrättsskyddade tillgångar.

## Testa nu

Du behöver ingen API-nyckel, inget utvecklarkonto och ingen betald plan för att inspektera App Store-data. Öppna [applookup.pro](https://applookup.pro), klistra in en valfri App Store-URL och du har metadata, ikoner och rå JSON på sekunder.

## Öppen källkod

AppLookup.pro är öppen källkod. Buggrapporter, nya länder och pull requests välkomnas.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro på GitHub" icon="github" tag="öppen källkod" >}}
{{< /cards >}}

---

## Vanliga frågor

{{% details title="Är AppLookup.pro verkligen gratis?" closed="true" %}}
Ja. AppLookup.pro är 100 procent gratis och öppen källkod. Det körs i din webbläsare. Det finns ingen registrering, ingen betald nivå och ingen användningsgräns utöver Apples egna gränser för iTunes Search API.
{{% /details %}}

{{% details title="Varifrån kommer datan?" closed="true" %}}
Varje resultat hämtas i realtid från Apples officiella [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html). Verktyget scrapar inte App Store-sidor och cachar inga svar på någon server.
{{% /details %}}

{{% details title="Kan jag ladda ner appikonen i hög upplösning?" closed="true" %}}
Ja. Sektionen **App Icon** visar varje ikon-URL som Apple returnerar. Varje kort har en Direct Link och en Download-knapp, och en Download All Icons ZIP-knapp packar ihop dem i ett arkiv.
{{% /details %}}

{{% details title="Kan jag ladda ner alla App Store-skärmbilder på en gång?" closed="true" %}}
Ja. Varje skärmbildsektion (iPhone, iPad, macOS och Apple TV) har en **Download All (ZIP)**-knapp som buntar ihop alla skärmbilder i full upplösning.
{{% /details %}}

{{% details title="Hur ser jag hur en app ser ut i ett annat land?" closed="true" %}}
Välj ett land i rullgardinsmenyn högst upp på sidan. Över 40 butiker stöds. Klicka på **Lookup** igen så hämtar verktyget appen för det landet och visar lokaliserad titel, beskrivning, skärmbilder, vad som är nytt och pris.
{{% /details %}}

{{% details title="Kan jag kopiera enskilda fält som bundle ID eller släppdatum?" closed="true" %}}
Ja. Varje textfält i resultatet har en egen Copy-knapp: appnamn, utvecklare, beskrivning, vad som är nytt, bundle ID, version, pris, filstorlek, lägsta OS, släppdatum, innehållsklassificering, språk, enheter som stöds och rå JSON.
{{% /details %}}

{{% details title="Fungerar AppLookup.pro för vilken iOS-app som helst?" closed="true" %}}
Det fungerar för alla appar som är publikt listade i minst ett App Store-land och returneras av iTunes Search API. Olistade, borttagna eller enterprise-distribuerade appar dyker inte upp.
{{% /details %}}

{{% details title="Stödjer det appar för macOS och Apple TV?" closed="true" %}}
Ja. Om appen har macOS- eller Apple TV-skärmbilder i svaret från iTunes Search API visar AppLookup.pro dem i en egen scrollbar panel med nedladdningsknappar.
{{% /details %}}

{{% details title="Kan jag använda den råa JSON i min egen kod?" closed="true" %}}
Ja. Sektionen Raw API Response visar den exakta JSON som Apple returnerar. Kopiera den till Postman, ett enhetstest eller en backend-pipeline. Respektera Apples API-villkor och rimliga hastighetsgränser.
{{% /details %}}

{{% details title="Är det säkert att klistra in App Store-URL:er i verktyget?" closed="true" %}}
Ja. URL:en tolkas i din webbläsare. Det enda utgående nätverksanropet är uppslagningen mot Apples iTunes Search API.
{{% /details %}}

{{% details title="Vad är skillnaden mellan AppLookup.pro och AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) är till för att läsa App Store-metadata för en publicerad app: konkurrentanalys, nedladdning av tillgångar, lokaliseringskontroller. [AppKeywords.pro](https://appkeywords.pro) är till för att skriva App Store-metadata för din egen app: optimering av titel, underrubrik och sökord med stöd för Fastlane. De två verktygen funkar bra ihop.
{{% /details %}}
