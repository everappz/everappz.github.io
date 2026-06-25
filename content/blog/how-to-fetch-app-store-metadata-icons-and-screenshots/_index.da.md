---
title: "Sådan henter du App Store-metadata, ikoner og skærmbilleder gratis"
date: 2026-06-13
description: "Trin for trin-guide til at hente metadata, ikon, skærmbilleder og lokaliserede App Store-detaljer for enhver iOS-app med AppLookup.pro, et gratis browserværktøj baseret på det officielle iTunes Search API."
keywords: [
  "app store metadata", "hent app store data", "download app store ikon",
  "download app store skærmbilleder", "app store opslagsværktøj", "itunes search api",
  "app metadata extractor", "iOS app metadata", "gratis app store api værktøj",
  "download app ikon høj opløsning", "app store konkurrentanalyse",
  "lokaliserede app store data", "app store land opslag", "gratis aso værktøj"
]
tags: [
  "App Store-metadata", "App-opslag", "iTunes Search API",
  "App-ikon download", "App-skærmbilleder", "ASO-research"
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

## Få App Store-data på få sekunder

**Kort version:** [AppLookup.pro](https://applookup.pro) er et gratis værktøj, der trækker offentlige data for enhver iOS-, iPadOS-, macOS- eller tvOS-app. Du får titel, beskrivning, hvad der er nyt, version, pris, anmeldelser, app-ikon, skærmbilleder, understøttede enheder og det rå svar fra iTunes API. Hvert felt har en kopiér-knap med et tryk. Åbn siden, indsæt et App Store-link eller skriv appens navn, og du har dataene.

Brug det til:

- **ASO-research.** Se hvordan de bedste apps skriver deres titler, underoverskrifter, beskrivelser og søgeord.
- **Konkurrentovervågning.** Tjek versionsopdateringer, anmeldelser og priser på tværs af markeder.
- **Asset-download.** Gem det officielle app-ikon og skærmbilleder i fuld størrelse i én ZIP.
- **Lokaliseringstjek.** Sammenlign beskrivelse, hvad der er nyt og skærmbilleder i over 40 App Store-lande.
- **API-test.** Kopiér det rå JSON-svar fra iTunes Search API direkte ind i din kode eller i Postman.

## Hvad er AppLookup.pro?

[AppLookup.pro](https://applookup.pro) er et gratis, browserbaseret App Store-opslagsværktøj. Det kører helt på din enhed. Hvert resultat kommer direkte fra Apples officielle [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html). Ingen scraping. Ingen tilmelding. Ingen sporing.

### Hvad du får

- **Søg efter appnavn eller App Store-URL.** Autofuldførelse viser live-resultater, mens du skriver.
- **Over 40 lande-butikker.** Skift mellem US, UK, JP, DE, FR, BR med flere.
- **Komplet metadata.** Titel, underoverskrift, udvikler, bundle ID, version, pris, filstørrelse, anmeldelser, udgivelsesdato, indholdsklassificering, sprog og understøttede enheder.
- **Højopløselige assets.** App-ikoner og skærmbilleder til iPhone, iPad, macOS og Apple TV.
- **Bulk ZIP-download.** Hent alle ikoner eller alle skærmbilleder i ét arkiv.
- **Rå iTunes API JSON.** Det præcise svar fra Apple, klar til at kopiere.
- **Kopiér-knapper på hvert felt.** Et tryk lægger værdien i din udklipsholder.

## Sådan bruger du AppLookup.pro trin for trin

### Trin 1. Indtast appens navn eller indsæt en App Store-URL

Åbn [applookup.pro](https://applookup.pro) og begynd at skrive appens navn. Autofuldførelse viser live App Store-resultater, mens du skriver.

Du kan også indsætte et direkte App Store-link som `https://apps.apple.com/us/app/instagram/id389801252` eller bare app-ID'et. Værktøjet trækker ID'et ud for dig. Det håndterer også Google omdirigerings-URL'er.

![Indtast et appnavn eller en App Store-URL i AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Trin 2. Hent appens info og download ikonet

Klik på **Lookup** eller tryk Enter. Værktøjet kalder det officielle iTunes Search API og viser app-ikonet, udviklerens navn, vurdering, version og pris på under et sekund.

Scroll til sektionen **App Icon**. Hver ikonstørrelse, som Apple returnerer, vises som et kort. Hvert kort har:

- **Direct Link.** Åbner billedet i fuld størrelse i en ny fane.
- **Download.** Gemmer filen på din computer.

Brug **Download All Icons (ZIP)** for at hente alle ikonstørrelser i ét arkiv. Det samme gælder skærmbilleder: hver platformssektion har sin egen **Download All (ZIP)**-knap.

![Download app-ikoner og skærmbilleder fra AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Trin 3. Læs appdetaljerne og kopiér ethvert felt

Scroll til **App Details**. Du vil se bundle ID, version, pris, filstørrelse, mindste OS, udgivelsesdato, sidste opdateringsdato, indholdsklassificering, genrer, genre-ID'er, sprog, sælger, artist-ID og track-ID.

Tryk på knappen **Copy** på et hvilket som helst kort. Værdien lander i din udklipsholder, og knappen viser et grønt 'Copied'-flueben.

Det samme virker for **Description**, **What's New** og **Supported Devices**. Disse sektioner kan scrolles, så du kan læse hele teksten uden at miste din placering, og Copy-knappen lægger hele feltet i din udklipsholder.

![Se fulde App Store-detaljer og kopiér ethvert felt med et tryk](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Trin 4. Se det rå API-svar fra App Store

Har du brug for den præcise JSON, som Apple returnerer? Scroll til **Raw API Response**. Hele payloaden fra iTunes Search API vises i en scrollbar viewer med en **Copy**-knap øverst. Et tryk kopierer hele JSON-objektet.

**iTunes Lookup URL** vises lige over. Indsæt den i Postman, curl eller din browser for at gentage samme anmodning.

![Se og kopiér det rå JSON-svar fra iTunes Search API](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Trin 5. Skift land for at se den lokaliserede version

App Store-metadata ændrer sig efter land. Den samme app har ofte en anden titel, underoverskrift, beskrivelse, skærmbilleder og pris på hvert marked.

Vælg et land i rullemenuen øverst. URL'en i inputfeltet opdateres automatisk. Klik på **Lookup** igen for at hente appen i det marked på ny.

Det er den hurtigste måde at tjekke, hvordan en konkurrent præsenterer sin app i Japan, Tyskland, Brasilien eller et af de over 40 understøttede lande.

![Skift mellem lande-butikker for at se lokaliseret App Store-metadata](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Trin 6. Kopiér de lokaliserede metadata

Når landeresultatet er indlæst, virker hvert felt på samme måde. Tryk på **Copy** på beskrivelsen, hvad der er nyt, appnavn, udvikler, bundle ID eller et hvilket som helst detaljekort for at fange den lokaliserede tekst.

Det gør det nemt at bygge sammenlignings-regneark side om side eller sende lokaliseret tekst videre til oversættelsesgennemgang.

![Kopiér lokaliseret App Store-beskrivning og metadata med et tryk](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Hvem bruger AppLookup.pro

- **Indie-udviklere**, der laver ASO-research før en lancering.
- **ASO- og marketingteams**, der følger konkurrenters opdateringer og priser.
- **Designere**, der henter det officielle højopløselige app-ikon og skærmbilleder til pressekits og cases.
- **Lokaliseringsteams**, der auditerer hvilke markeder, der er dækket, og hvor den engelske standardtekst stadig vises.
- **Backend- og QA-ingeniører**, der tester iTunes Search API-integrationer uden at skrive en scraper.
- **Skribenter og bloggere**, der har brug for det officielle app-ikon og nogle få skærmbilleder til et indlæg.

## Privatliv og ansvarsfraskrivelse

AppLookup.pro kører i din browser. Der er intet login. Der er ingen sporing. Der er ingen serverlogning af de apps, du slår op. Anmodninger går direkte fra din browser til Apples [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html).

Dette værktøj er **kun til uddannelses- og researchformål**. Alle data hentes fra Apples officielle offentlige API og forbliver ejendom for Apple Inc. og de anførte app-udgivere. Brug af værktøjet er underlagt [Apple Media Services Vilkår og Betingelser](https://www.apple.com/legal/internet-services/terms/site.html). Respekter Apples hastighedsgrænser, og videredistribuér ikke ophavsretligt beskyttede assets.

## Prøv det nu

Du behøver ikke en API-nøgle, en udviklerkonto eller et betalt abonnement for at undersøge App Store-data. Åbn [applookup.pro](https://applookup.pro), indsæt en hvilken som helst App Store-URL, og du har metadata, ikoner og rå JSON på få sekunder.

## Open source

AppLookup.pro er open source. Fejlrapporter, nye lande og pull requests er velkomne.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro på GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Ofte stillede spørgsmål

{{% details title="Er AppLookup.pro virkelig gratis?" closed="true" %}}
Ja. AppLookup.pro er 100 procent gratis og open source. Det kører i din browser. Der er ingen tilmelding, intet betalt niveau og intet brugsloft ud over Apples egne grænser for iTunes Search API.
{{% /details %}}

{{% details title="Hvor kommer dataene fra?" closed="true" %}}
Hvert resultat hentes i realtid fra Apples officielle [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html). Værktøjet scraper ikke App Store-sider og cacher ikke svar på nogen server.
{{% /details %}}

{{% details title="Kan jeg downloade app-ikonet i høj opløsning?" closed="true" %}}
Ja. Sektionen **App Icon** viser hver ikon-URL, som Apple returnerer. Hvert kort har et Direct Link og en Download-knap, og en Download All Icons ZIP-knap pakker dem alle ind i ét arkiv.
{{% /details %}}

{{% details title="Kan jeg downloade alle App Store-skærmbilleder på én gang?" closed="true" %}}
Ja. Hver skærmbillede-sektion (iPhone, iPad, macOS og Apple TV) har en **Download All (ZIP)**-knap, der samler alle skærmbilleder i fuld opløsning.
{{% /details %}}

{{% details title="Hvordan ser jeg, hvordan en app ser ud i et andet land?" closed="true" %}}
Vælg et land i rullemenuen øverst på siden. Over 40 butikker er understøttet. Klik på **Lookup** igen, og værktøjet henter appen for det land og viser den lokaliserede titel, beskrivelse, skærmbilleder, hvad der er nyt og pris.
{{% /details %}}

{{% details title="Kan jeg kopiere enkelte felter som bundle ID eller udgivelsesdato?" closed="true" %}}
Ja. Hvert tekstfelt i resultatet har sin egen Copy-knap: appnavn, udvikler, beskrivelse, hvad der er nyt, bundle ID, version, pris, filstørrelse, mindste OS, udgivelsesdato, indholdsklassificering, sprog, understøttede enheder og rå JSON.
{{% /details %}}

{{% details title="Virker AppLookup.pro for enhver iOS-app?" closed="true" %}}
Det virker for enhver app, der er offentligt anført i mindst ét App Store-land og returneres af iTunes Search API. Ikke-anførte, fjernede eller enterprise-distribuerede apps vises ikke.
{{% /details %}}

{{% details title="Understøtter det macOS- og Apple TV-apps?" closed="true" %}}
Ja. Hvis appen har macOS- eller Apple TV-skærmbilleder i svaret fra iTunes Search API, viser AppLookup.pro dem i deres eget scrollbare panel med downloadknapper.
{{% /details %}}

{{% details title="Kan jeg bruge den rå JSON i min egen kode?" closed="true" %}}
Ja. Sektionen Raw API Response viser den præcise JSON, som Apple returnerer. Kopiér den ind i Postman, en enhedstest eller en backend-pipeline. Respekter Apples API-vilkår og rimelige hastighedsgrænser.
{{% /details %}}

{{% details title="Er det sikkert at indsætte App Store-URL'er i værktøjet?" closed="true" %}}
Ja. URL'en parses i din browser. Det eneste udgående netværkskald er opslaget mod Apples iTunes Search API.
{{% /details %}}

{{% details title="Hvad er forskellen mellem AppLookup.pro og AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) er til at læse App Store-metadata fra en hvilken som helst udgivet app: konkurrentanalyse, asset-download, lokaliseringstjek. [AppKeywords.pro](https://appkeywords.pro) er til at skrive App Store-metadata for din egen app: optimering af titel, underoverskrift og søgeord med Fastlane-understøttelse. De to værktøjer fungerer godt sammen.
{{% /details %}}
