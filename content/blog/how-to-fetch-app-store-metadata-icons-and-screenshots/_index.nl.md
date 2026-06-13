---
title: "Hoe je gratis App Store metadata, iconen en screenshots ophaalt"
date: 2026-06-13
description: "Stap voor stap gids om metadata, het icoon, screenshots en gelokaliseerde App Store details van elke iOS app op te halen met AppLookup.pro, een gratis browsertool op basis van de officiële iTunes Search API."
keywords: [
  "app store metadata", "app store data ophalen", "app store icoon downloaden",
  "app store screenshots downloaden", "app store lookup tool", "itunes search api",
  "app metadata extractor", "iOS app metadata", "gratis app store api tool",
  "app icoon hoge resolutie downloaden", "app store concurrentieonderzoek",
  "gelokaliseerde app store data", "app store landenzoeker", "gratis aso tool"
]
tags: [
  "App Store Metadata", "App Lookup", "iTunes Search API",
  "App Icoon Download", "App Screenshots", "ASO Onderzoek"
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

## Haal App Store data binnen seconden op

**Korte versie:** [AppLookup.pro](https://applookup.pro) is een gratis tool die publieke data ophaalt van elke iOS, iPadOS, macOS of tvOS app. Je krijgt de titel, beschrijving, wat nieuw is, versie, prijs, beoordelingen, app icoon, screenshots, ondersteunde apparaten en de ruwe iTunes API respons. Elk veld heeft een kopieerknop met één tik. Open de site, plak een App Store link of typ de naam van de app en je hebt de data.

Gebruik het voor:

- **ASO onderzoek.** Bekijk hoe topapps hun titels, ondertitels, beschrijvingen en zoekwoorden schrijven.
- **Concurrentie volgen.** Controleer versie updates, beoordelingen en prijzen per markt.
- **Assets downloaden.** Bewaar het officiële app icoon en screenshots op volledige grootte in één ZIP.
- **Lokalisatie checks.** Vergelijk beschrijving, wat nieuw is en screenshots in meer dan 40 App Store landen.
- **API testen.** Kopieer de ruwe iTunes Search API JSON direct in je code of in Postman.

## Wat is AppLookup.pro?

[AppLookup.pro](https://applookup.pro) is een gratis App Store lookup tool die in de browser werkt. Hij draait volledig op je apparaat. Elk resultaat komt rechtstreeks van Apples officiële [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html). Geen scraping. Geen aanmelding. Geen tracking.

### Wat je krijgt

- **Zoeken op appnaam of App Store URL.** Autocomplete toont live resultaten terwijl je typt.
- **Meer dan 40 land storefronts.** Wissel tussen US, UK, JP, DE, FR, BR en meer.
- **Volledige metadata.** Titel, ondertitel, ontwikkelaar, bundle ID, versie, prijs, bestandsgrootte, beoordelingen, releasedatum, leeftijdsclassificatie, talen en ondersteunde apparaten.
- **Assets in hoge resolutie.** App iconen en screenshots voor iPhone, iPad, macOS en Apple TV.
- **Bulk ZIP download.** Pak alle iconen of alle screenshots in één archief.
- **Ruwe iTunes API JSON.** De exacte respons van Apple, klaar om te kopiëren.
- **Kopieerknoppen op elk veld.** Eén tik en de waarde staat op je klembord.

## Hoe gebruik je AppLookup.pro stap voor stap

### Stap 1. Voer de appnaam in of plak een App Store URL

Open [applookup.pro](https://applookup.pro) en begin de naam van de app te typen. Autocomplete toont live App Store resultaten terwijl je typt.

Je kunt ook een directe App Store link plakken zoals `https://apps.apple.com/us/app/instagram/id389801252` of alleen de app ID. De tool haalt de ID er voor je uit. Hij verwerkt ook Google redirect URLs.

![Voer een appnaam of App Store URL in op AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Stap 2. Haal de app info op en download het icoon

Klik op **Lookup** of druk op Enter. De tool roept de officiële iTunes Search API aan en toont het app icoon, de naam van de ontwikkelaar, de beoordeling, de versie en de prijs in minder dan een seconde.

Scroll naar de sectie **App Icon**. Elke icoon grootte die Apple teruggeeft verschijnt als een kaart. Elke kaart heeft:

- **Direct Link.** Opent de afbeelding op volledige grootte in een nieuw tabblad.
- **Download.** Bewaart het bestand op je computer.

Gebruik **Download All Icons (ZIP)** om alle icoongroottes in één archief te pakken. Hetzelfde geldt voor screenshots: elke platformsectie heeft een eigen **Download All (ZIP)** knop.

![Download app iconen en screenshots van AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Stap 3. Lees de app details en kopieer elk veld

Scroll naar **App Details**. Je ziet bundle ID, versie, prijs, bestandsgrootte, minimaal OS, releasedatum, datum van laatste update, leeftijdsclassificatie, genres, genre IDs, talen, verkoper, artist ID en track ID.

Tik op de **Copy** knop op een kaart. De waarde gaat naar je klembord en de knop toont een groen vinkje 'Copied'.

Hetzelfde werkt voor **Description**, **What's New** en **Supported Devices**. Deze secties zijn scrollbaar zodat je de hele tekst kunt lezen zonder je plek te verliezen, en de Copy knop zet het hele veld op je klembord.

![Bekijk volledige App Store details en kopieer elk veld met één tik](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Stap 4. Bekijk de ruwe App Store API respons

Heb je de exacte JSON nodig die Apple teruggeeft? Scroll naar **Raw API Response**. De volledige iTunes Search API payload wordt getoond in een scrollbare viewer met een **Copy** knop bovenaan. Eén tik kopieert het hele JSON object.

De **iTunes Lookup URL** staat er net boven. Plak hem in Postman, curl of je browser om dezelfde aanvraag opnieuw uit te voeren.

![Bekijk en kopieer de ruwe JSON respons van de iTunes Search API](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Stap 5. Wijzig het land om de gelokaliseerde versie te zien

App Store metadata verandert per land. Dezelfde app heeft vaak een andere titel, ondertitel, beschrijving, screenshots en prijs in elke markt.

Kies een land in het dropdown menu bovenaan. De URL in het invoerveld werkt automatisch bij. Klik nogmaals op **Lookup** om de app in die markt opnieuw op te halen.

Dit is de snelste manier om te zien hoe een concurrent zijn app presenteert in Japan, Duitsland, Brazilië of een van de meer dan 40 ondersteunde landen.

![Wissel van land storefront om gelokaliseerde App Store metadata te zien](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Stap 6. Kopieer de gelokaliseerde metadata

Zodra het landresultaat is geladen, werkt elk veld op dezelfde manier. Tik op **Copy** bij beschrijving, wat nieuw is, appnaam, ontwikkelaar, bundle ID of een willekeurige detailkaart om de gelokaliseerde tekst vast te leggen.

Hierdoor wordt het makkelijk om vergelijkingsspreadsheets naast elkaar te maken of gelokaliseerde teksten in een vertaalreview te zetten.

![Kopieer gelokaliseerde App Store beschrijving en metadata met één tik](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Wie gebruikt AppLookup.pro

- **Indie ontwikkelaars** die ASO onderzoek doen voor een launch.
- **ASO en marketing teams** die updates en prijzen van concurrenten volgen.
- **Designers** die het officiële hoge resolutie app icoon en screenshots pakken voor presskits en case studies.
- **Lokalisatie teams** die controleren welke markten gedekt zijn en waar de standaard Engelse tekst nog wordt uitgeleverd.
- **Backend en QA engineers** die iTunes Search API integraties testen zonder een scraper te schrijven.
- **Schrijvers en bloggers** die het officiële app icoon en een paar screenshots nodig hebben voor een artikel.

## Privacy en disclaimer

AppLookup.pro draait in je browser. Er is geen login. Er is geen tracking. Er is geen server side logging van de apps die je opzoekt. Verzoeken gaan rechtstreeks van je browser naar Apples [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html).

Deze tool is alleen bedoeld voor **educatieve en onderzoeksdoeleinden**. Alle data wordt opgehaald via Apples officiële publieke API en blijft eigendom van Apple Inc. en de vermelde app uitgevers. Het gebruik van de tool valt onder de [Apple Media Services Algemene Voorwaarden](https://www.apple.com/legal/internet-services/terms/site.html). Respecteer Apples rate limits en verspreid geen auteursrechtelijk beschermde assets.

## Probeer het nu

Je hebt geen API sleutel, ontwikkelaarsaccount of betaald abonnement nodig om App Store data te bekijken. Open [applookup.pro](https://applookup.pro), plak een willekeurige App Store URL en je hebt de metadata, iconen en ruwe JSON in seconden.

## Open source

AppLookup.pro is open source. Bug reports, nieuwe landen en pull requests zijn welkom.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro op GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Veelgestelde vragen

{{% details title="Is AppLookup.pro echt gratis?" closed="true" %}}
Ja. AppLookup.pro is 100 procent gratis en open source. Het draait in je browser. Er is geen aanmelding, geen betaalde laag en geen gebruikslimiet buiten Apples eigen iTunes Search API limieten.
{{% /details %}}

{{% details title="Waar komt de data vandaan?" closed="true" %}}
Elk resultaat wordt in realtime opgehaald via Apples officiële [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html). De tool scrapt geen App Store pagina's en cachet geen antwoorden op een server.
{{% /details %}}

{{% details title="Kan ik het app icoon in hoge resolutie downloaden?" closed="true" %}}
Ja. De sectie **App Icon** toont elke icoon URL die Apple teruggeeft. Elke kaart heeft een Direct Link en een Download knop, en een Download All Icons ZIP knop bundelt ze in één archief.
{{% /details %}}

{{% details title="Kan ik alle App Store screenshots in één keer downloaden?" closed="true" %}}
Ja. Elke screenshot sectie (iPhone, iPad, macOS en Apple TV) heeft een **Download All (ZIP)** knop die alle screenshots op volledige resolutie bundelt.
{{% /details %}}

{{% details title="Hoe zie ik hoe een app eruitziet in een ander land?" closed="true" %}}
Kies een land in het dropdown menu bovenaan de pagina. Meer dan 40 storefronts worden ondersteund. Klik nogmaals op **Lookup** en de tool haalt de app voor dat land opnieuw op en toont de gelokaliseerde titel, beschrijving, screenshots, wat nieuw is en prijs.
{{% /details %}}

{{% details title="Kan ik losse velden zoals bundle ID of releasedatum kopiëren?" closed="true" %}}
Ja. Elk tekstveld in het resultaat heeft zijn eigen Copy knop: appnaam, ontwikkelaar, beschrijving, wat nieuw is, bundle ID, versie, prijs, bestandsgrootte, minimaal OS, releasedatum, leeftijdsclassificatie, talen, ondersteunde apparaten en ruwe JSON.
{{% /details %}}

{{% details title="Werkt AppLookup.pro voor elke iOS app?" closed="true" %}}
Het werkt voor elke app die publiek vermeld staat in ten minste één App Store land en wordt teruggegeven door de iTunes Search API. Niet vermelde, verwijderde of enterprise gedistribueerde apps verschijnen niet.
{{% /details %}}

{{% details title="Ondersteunt het macOS en Apple TV apps?" closed="true" %}}
Ja. Als de app macOS of Apple TV screenshots heeft in de respons van de iTunes Search API, toont AppLookup.pro deze in een eigen scrollbaar paneel met downloadknoppen.
{{% /details %}}

{{% details title="Kan ik de ruwe JSON in mijn eigen code gebruiken?" closed="true" %}}
Ja. De sectie Raw API Response toont de exacte JSON die Apple teruggeeft. Kopieer het in Postman, een unit test of een backend pipeline. Respecteer de API voorwaarden van Apple en redelijke rate limits.
{{% /details %}}

{{% details title="Is het veilig om App Store URLs in de tool te plakken?" closed="true" %}}
Ja. De URL wordt in je browser geparset. De enige uitgaande netwerkaanroep is de lookup naar Apples iTunes Search API.
{{% /details %}}

{{% details title="Wat is het verschil tussen AppLookup.pro en AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) is voor het lezen van App Store metadata van elke gepubliceerde app: concurrentieonderzoek, asset download, lokalisatie checks. [AppKeywords.pro](https://appkeywords.pro) is voor het schrijven van App Store metadata voor je eigen app: optimalisatie van titel, ondertitel en zoekwoorden met Fastlane ondersteuning. De twee tools werken goed samen.
{{% /details %}}
