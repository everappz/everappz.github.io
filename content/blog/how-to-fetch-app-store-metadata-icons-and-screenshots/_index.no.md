---
title: "Slik henter du App Store-metadata, ikoner og skjermbilder gratis"
date: 2026-06-13
description: "Trinnvis guide for å hente metadata, ikon, skjermbilder og lokaliserte App Store-detaljer for enhver iOS-app ved hjelp av AppLookup.pro, et gratis nettleserverktøy basert på det offisielle iTunes Search API."
keywords: [
  "app store metadata", "hente app store data", "last ned app store ikon",
  "last ned app store skjermbilder", "app store oppslagsverktøy", "itunes search api",
  "app metadata uttrekker", "iOS app metadata", "gratis app store api verktøy",
  "last ned app ikon i høy oppløsning", "konkurrentanalyse app store",
  "lokaliserte app store data", "app store landoppslag", "gratis aso analyseverktøy"
]
tags: [
  "App Store-metadata", "App-oppslag", "iTunes Search API",
  "App-ikon nedlasting", "App-skjermbilder", "ASO-analyse"
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

## Hent App Store-data på sekunder

**Kort versjon:** [AppLookup.pro](https://applookup.pro) er et gratis verktøy som henter offentlige data for enhver iOS-, iPadOS-, macOS- eller tvOS-app. Du får tittelen, beskrivelsen, nyheter, versjon, pris, vurderinger, app-ikon, skjermbilder, støttede enheter og det rå iTunes API-svaret. Hvert felt har en kopieringsknapp med ett trykk. Åpne siden, lim inn en App Store-lenke eller skriv inn appnavnet, så har du dataene.

Bruk det til:

- **ASO-analyse.** Se hvordan toppappene skriver titler, undertitler, beskrivelser og nøkkelord.
- **Konkurrentsporing.** Sjekk versjonsoppdateringer, vurderinger og priser på tvers av markeder.
- **Nedlasting av ressurser.** Lagre det offisielle app-ikonet og skjermbilder i full størrelse i én ZIP.
- **Lokaliseringssjekk.** Sammenlign beskrivelse, nyheter og skjermbilder på tvers av over 40 App Store-land.
- **API-testing.** Kopier den rå iTunes Search API JSON-en rett inn i koden din eller Postman.

## Hva er AppLookup.pro?

[AppLookup.pro](https://applookup.pro) er et gratis, nettleserbasert App Store-oppslagsverktøy. Det kjører helt på enheten din. Hvert resultat kommer rett fra Apples offisielle [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html). Ingen skraping. Ingen registrering. Ingen sporing.

### Hva du får

- **Søk etter appnavn eller App Store-URL.** Autofullføring viser live resultater mens du skriver.
- **Over 40 land-butikker.** Bytt mellom US, UK, JP, DE, FR, BR og flere.
- **Full metadata.** Tittel, undertittel, utvikler, bundle-ID, versjon, pris, filstørrelse, vurderinger, utgivelsesdato, innholdsklassifisering, språk og støttede enheter.
- **Ressurser i høy oppløsning.** App-ikoner og skjermbilder for iPhone, iPad, macOS og Apple TV.
- **ZIP-nedlasting i bulk.** Få alle ikoner eller alle skjermbilder i ett arkiv.
- **Rå iTunes API JSON.** Det nøyaktige svaret fra Apple, klart til å kopieres.
- **Kopieringsknapper på hvert felt.** Ett trykk legger verdien i utklippstavlen.

## Slik bruker du AppLookup.pro trinn for trinn

### Trinn 1. Skriv inn appnavnet eller lim inn en App Store-URL

Åpne [applookup.pro](https://applookup.pro) og begynn å skrive inn appnavnet. Autofullføring viser live App Store-resultater mens du skriver.

Du kan også lime inn en direkte App Store-lenke som `https://apps.apple.com/us/app/instagram/id389801252` eller bare app-ID-en. Verktøyet henter ut ID-en for deg. Det håndterer også Google-omdirigerings-URL-er.

![Skriv inn et appnavn eller App Store-URL i AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Trinn 2. Hent app-informasjonen og last ned ikonet

Klikk **Lookup** eller trykk Enter. Verktøyet kaller det offisielle iTunes Search API og viser app-ikonet, utviklernavnet, vurderingen, versjonen og prisen på under et sekund.

Bla til **App Icon**-seksjonen. Hver ikonstørrelse Apple returnerer vises som et kort. Hvert kort har:

- **Direct Link.** Åpner bildet i full størrelse i en ny fane.
- **Download.** Lagrer filen på datamaskinen din.

Bruk **Download All Icons (ZIP)** for å hente alle ikonstørrelser i ett arkiv. Det samme gjelder skjermbilder: hver plattformseksjon har sin egen **Download All (ZIP)**-knapp.

![Last ned app-ikoner og skjermbilder fra AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Trinn 3. Les app-detaljene og kopier et hvilket som helst felt

Bla til **App Details**. Du vil se bundle-ID, versjon, pris, filstørrelse, minimum OS, utgivelsesdato, dato for siste oppdatering, innholdsklassifisering, sjangre, sjanger-ID-er, språk, selger, artist-ID og spor-ID.

Trykk på **Copy**-knappen på et hvilket som helst kort. Verdien legges i utklippstavlen og knappen viser en grønn «Copied»-hake.

Det samme fungerer for **Description**, **What's New** og **Supported Devices**. Disse seksjonene er rullbare slik at du kan lese hele teksten uten å miste plassen, og Copy-knappen legger hele feltet på utklippstavlen.

![Se fullstendige App Store-detaljer og kopier et hvilket som helst felt med ett trykk](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Trinn 4. Se det rå App Store API-svaret

Trenger du den nøyaktige JSON-en Apple returnerer? Bla til **Raw API Response**. Hele iTunes Search API-nyttelasten vises i en rullbar visning med en **Copy**-knapp øverst. Ett trykk kopierer hele JSON-objektet.

**iTunes Lookup URL** vises rett over. Lim den inn i Postman, curl eller nettleseren din for å gjenta samme forespørsel.

![Se og kopier det rå iTunes Search API JSON-svaret](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Trinn 5. Endre land for å se den lokaliserte versjonen

App Store-metadata endres etter land. Den samme appen har ofte en annen tittel, undertittel, beskrivelse, skjermbilder og pris i hvert marked.

Velg et land fra rullegardinmenyen øverst. URL-en i inntastingsfeltet oppdateres automatisk. Klikk **Lookup** igjen for å hente appen på nytt i det markedet.

Dette er den raskeste måten å sjekke hvordan en konkurrent presenterer appen sin i Japan, Tyskland, Brasil eller noen av de over 40 støttede landene.

![Bytt land-butikker for å se lokalisert App Store-metadata](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Trinn 6. Kopier den lokaliserte metadataen

Når landresultatet er lastet inn, fungerer hvert felt på samme måte. Trykk på **Copy** på beskrivelsen, nyheter, appnavnet, utvikleren, bundle-ID-en eller et hvilket som helst detaljkort for å hente den lokaliserte teksten.

Dette gjør det enkelt å bygge sammenligningsregneark side ved side eller mate lokalisert tekst inn i oversettelsesgjennomgang.

![Kopier lokalisert App Store-beskrivelse og metadata med ett trykk](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Hvem bruker AppLookup.pro

- **Indie-utviklere** som gjør ASO-analyse før en lansering.
- **ASO- og markedsføringsteam** som sporer konkurrenters oppdateringer og priser.
- **Designere** som henter det offisielle app-ikonet i høy oppløsning og skjermbilder til pressepakker og casestudier.
- **Lokaliseringsteam** som reviderer hvilke markeder som dekkes og hvor den engelske standardteksten fortsatt brukes.
- **Backend- og QA-ingeniører** som tester iTunes Search API-integrasjoner uten å skrive en skraper.
- **Skribenter og bloggere** som trenger det offisielle app-ikonet og noen skjermbilder til et innlegg.

## Personvern og ansvarsfraskrivelse

AppLookup.pro kjører i nettleseren din. Det er ingen pålogging. Det er ingen sporing. Det er ingen serverlogging av appene du slår opp. Forespørsler går direkte fra nettleseren din til Apples [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html).

Dette verktøyet er kun for **utdannings- og forskningsformål**. Alle data hentes fra Apples offisielle offentlige API og forblir eiendommen til Apple Inc. og de oppførte app-utgiverne. Bruk av verktøyet er underlagt [Apple Media Services Terms and Conditions](https://www.apple.com/legal/internet-services/terms/site.html). Vennligst respekter Apples ratebegrensninger og ikke distribuer opphavsrettsbeskyttede ressurser på nytt.

## Prøv det nå

Du trenger ingen API-nøkkel, utviklerkonto eller betalt plan for å inspisere App Store-data. Åpne [applookup.pro](https://applookup.pro), lim inn en hvilken som helst App Store-URL, og du vil ha metadataen, ikonene og rå JSON på sekunder.

## Åpen kildekode

AppLookup.pro er åpen kildekode. Feilrapporter, tillegg av land og pull requests er velkomne.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro på GitHub" icon="github" tag="åpen kildekode" >}}
{{< /cards >}}

---

## Ofte stilte spørsmål

{{% details title="Er AppLookup.pro virkelig gratis?" closed="true" %}}
Ja. AppLookup.pro er 100 prosent gratis og åpen kildekode. Det kjører i nettleseren din. Det er ingen registrering, ingen betalt nivå og ingen brukstak utover Apples egne iTunes Search API-grenser.
{{% /details %}}

{{% details title="Hvor kommer dataene fra?" closed="true" %}}
Hvert resultat hentes i sanntid fra Apples offisielle [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html). Verktøyet skraper ikke App Store-sider og bufrer ikke svar på noen server.
{{% /details %}}

{{% details title="Kan jeg laste ned app-ikonet i høy oppløsning?" closed="true" %}}
Ja. **App Icon**-seksjonen viser hver ikon-URL Apple returnerer. Hvert kort har en Direct Link og en Download-knapp, og en Download All Icons ZIP-knapp pakker dem i ett arkiv.
{{% /details %}}

{{% details title="Kan jeg laste ned alle App Store-skjermbilder samtidig?" closed="true" %}}
Ja. Hver skjermbildeseksjon (iPhone, iPad, macOS og Apple TV) har en **Download All (ZIP)**-knapp som samler hvert skjermbilde i full oppløsning.
{{% /details %}}

{{% details title="Hvordan ser jeg hvordan en app ser ut i et annet land?" closed="true" %}}
Velg et land i rullegardinmenyen øverst på siden. Over 40 butikker er støttet. Klikk **Lookup** igjen og verktøyet henter appen på nytt for det landet, og viser den lokaliserte tittelen, beskrivelsen, skjermbildene, nyhetene og prisen.
{{% /details %}}

{{% details title="Kan jeg kopiere enkeltfelter som bundle-ID eller utgivelsesdato?" closed="true" %}}
Ja. Hvert tekstfelt i resultatet har sin egen Copy-knapp: appnavn, utvikler, beskrivelse, nyheter, bundle-ID, versjon, pris, filstørrelse, minimum OS, utgivelsesdato, innholdsklassifisering, språk, støttede enheter og rå JSON.
{{% /details %}}

{{% details title="Fungerer AppLookup.pro for enhver iOS-app?" closed="true" %}}
Det fungerer for enhver app som er offentlig oppført i minst ett App Store-land og returnert av iTunes Search API. Apper som ikke er oppført, fjernet eller distribuert til bedrifter vil ikke vises.
{{% /details %}}

{{% details title="Støtter det macOS- og Apple TV-apper?" closed="true" %}}
Ja. Hvis appen har macOS- eller Apple TV-skjermbilder i iTunes Search API-svaret, viser AppLookup.pro dem i sitt eget rullbare panel med nedlastingsknapper.
{{% /details %}}

{{% details title="Kan jeg bruke den rå JSON-en i min egen kode?" closed="true" %}}
Ja. Raw API Response-seksjonen viser den nøyaktige JSON-en Apple returnerer. Kopier den inn i Postman, en enhetstest eller en backend-pipeline. Vennligst respekter Apples API-vilkår og rimelige ratebegrensninger.
{{% /details %}}

{{% details title="Er det trygt å lime inn App Store-URL-er i verktøyet?" closed="true" %}}
Ja. URL-en analyseres i nettleseren din. Det eneste utgående nettverkskallet er oppslaget til Apples iTunes Search API.
{{% /details %}}

{{% details title="Hva er forskjellen mellom AppLookup.pro og AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) er for å lese App Store-metadata fra enhver publisert app: konkurrentanalyse, nedlasting av ressurser, lokaliseringssjekker. [AppKeywords.pro](https://appkeywords.pro) er for å skrive App Store-metadata for din egen app: tittel, undertittel og nøkkelordoptimalisering med Fastlane-støtte. De to verktøyene fungerer godt sammen.
{{% /details %}}
