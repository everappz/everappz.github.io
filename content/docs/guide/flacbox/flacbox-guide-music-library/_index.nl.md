---
title: "Muziekbibliotheek"
date: 2020-02-01
description: "Leer hoe je de muziekbibliotheek in Flacbox bouwt, organiseert en synchroniseert op iPhone, iPad en Mac. Voeg tracks handmatig toe of synchroniseer vanuit cloudservices, beheer metadata, albumhoezen, afspeellijsten, favorieten, recente items en bladwijzers. Inclusief hi-res audioondersteuning, MusicBrainz-tageditor, online en offline synchronisatie en personalisatie-opties."
keywords: [
  "Flacbox muziekbibliotheek", "muziek synchroniseren van cloud", "muziekmetadata organiseren",
  "audiotags bewerken Flacbox", "offline muziek synchroniseren", "lokale muziek importeren",
  "Flacbox afspeellijstbeheer", "albumhoes zoeken Flacbox",
  "iPhone muziekmetadata", "Flacbox app gids",
  "Flacbox MusicBrainz", "Flacbox tags normaliseren",
  "Flacbox hi-res muziekbibliotheek", "Flacbox FFmpeg bibliotheek",
  "Flacbox soloalbums", "Flacbox componistenweergave"
]
tags: ["muziek", "gids", "flacbox", "bibliotheek"]
readingTime: 11
---


Je muziekbibliotheek beheren is een fluitje van een cent met Flacbox, waar je moeiteloos al je tracks — lokale FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE en tientallen andere formaten — kunt organiseren in één doorzoekbare collectie. Je hebt twee opties voor het opbouwen van je muziekbibliotheek: handmatige toevoeging (je kiest precies wat er wordt toegevoegd) of automatische synchronisatie (Flacbox scant aangewezen cloudmappen en voegt nieuwe bestanden automatisch toe zodra ze verschijnen).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Muziekbibliotheek Albumweergave" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Handmatige Toevoeging

Om tracks handmatig toe te voegen, tik op het pictogram **Muziek toevoegen** in de linkerbovenhoek en kies mappen of bestanden van een verbonden cloudopslagservice of bestanden op je apparaat. Wanneer je tracks aan de bibliotheek toevoegt, worden er alleen koppelingen naar die tracks gemaakt — de eigenlijke bestanden blijven op hun oorspronkelijke locaties om kostbare schijfruimte te besparen. Als je tracks offline beschikbaar wilt maken, kun je de actie Downloaden gebruiken in het optiesmenu of de offline modus inschakelen voor afspeellijsten en trackcollecties.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Nummers Toevoegen aan de Muziekbibliotheek" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

Je kunt ook bestanden naar de bibliotheek slepen en neerzetten in de Mac-versie, of **Bestanden openen…** / **Map openen…** gebruiken via de systeembestandselecteur op iPhone en iPad.

## Afspelen Hervatten

Herstel de audiospelerwachtrij vanaf de laatst opgeslagen positie als deze functie is ingeschakeld in de applicatie-instellingen. Schakel zowel **Audiospelerstatus opslaan** als **Afspeelpositie opslaan** in via Instellingen → Audiospeler → Algemeen voor de beste ervaring. Eenmaal ingeschakeld verschijnt er bovenaan elk map-, album-, artiest-, genre- en afspeellijstscherm een knop **Afspelen hervatten**.

## Locaties

Alle tracks in je bibliotheek zijn zorgvuldig gegroepeerd per brontype en muziektagbepaling. Je kunt nummers filteren op locatie via de knop **Meer acties** rechtsboven en **Filteren** te selecteren.

### Online Muziek

Deze sectie toont muziek van je verbonden cloudopslagservices. De tracks hier worden op aanvraag gestreamd; niets neemt lokale opslag in beslag tenzij je expliciet downloadt of de offline modus inschakelt.

### Bestanden in Deze Applicatie

Hier vind je muziek die beschikbaar is voor offline afspelen, afkomstig van je lokale bestanden. Dit omvat bestanden in de Documents-map van de app.

### Bestanden op Deze iPhone / iPad / Mac

Deze categorie omvat muziek die via het systeemdialoogvenster **Bestanden openen…** vanuit je apparaat in de applicatie is geïmporteerd. De oorspronkelijke bestanden blijven op hun oorspronkelijke locatie; Flacbox bewaart alleen een koppeling naar ze.

## Categorieën

Wanneer je tracks aan je muziekbibliotheek toevoegt, leest de app automatisch hun audiotags en organiseert ze in categorieën zoals Nummers, Niet-afgespeelde nummers, Albums, Albumartiesten, Artiesten, Genres en Componisten.

## Tags Groeperen

Deze categorieën helpen je tracks te organiseren op muziektagbepaling. Wanneer je tracks aan de muziekbibliotheek toevoegt, leest de app hun metadata en groepeert ze op deze categorieën. Als je niet al je albums ziet, controleer dan of de app elk track heeft gescand. Je kunt de voortgang van het scannen controleren in Instellingen → Muziekbibliotheek → Metadata lezen → Aantal verwerkte bestanden in de muziekbibliotheek. Nadat de metadatalezer alle bewerkingen heeft voltooid, zie je de volgende categorieën in je muziekbibliotheek:

- **Nummers** — alle nummers gegroepeerd op de TRACK_TITLE-tag. Je kunt de sorteervolgorde controleren via het menu Meer acties rechtsboven.
- **Niet-afgespeelde nummers** — alle nummers die nog nooit zijn afgespeeld.
- **Albums** — nummers gegroepeerd op de ALBUM_NAME-tag, waarbij artiesten-, albumartiest- en componistentags worden genegeerd.
- **Albumartiesten** — nummers gegroepeerd alleen op de ALBUM_ARTIST_TAG. Handig om compilaties en samenwerkingen netjes gescheiden te houden van solowerk.
- **Artiesten** — nummers gegroepeerd alleen op de ARTIST_TAG.
- **Genres** — nummers gegroepeerd op de GENRE-tag.
- **Componisten** — nummers gegroepeerd op de COMPOSER-tag — onmisbaar voor klassieke muziekbibliotheken waar 'componist' de primaire navigatieas is.

## Favorieten

Je kunt nummers als favoriet markeren op het audiospelerscherm of via het optiesmenu. Favorieten verschijnen in hun eigen sectie zodat je ze met één tik kunt vinden.

## Recenties

Deze sectie toont alle recent afgespeelde tracks. Je kunt aanpassen hoeveel items de recente lijst bijhoudt in Instellingen → Bibliotheek → Recenties → Lijstgrootte wijzigen, en de lijst exporteren naar M3U / CSV / TXT om je luistergeschiedenis te bewaren.

## Bladwijzers

Je kunt audio-bladwijzers maken terwijl een nummer wordt afgespeeld en ze beheren op dit scherm — perfect voor audioboeken, lange mixen, lezingen of het markeren van het refrein van een favoriet nummer. Gedetailleerde instructies over het werken met audio-bladwijzers zijn beschikbaar [hier](/docs/guide/evermusic/evermusic-guide-music-library).

## Bovenste Werkbalk

Vlak onder de navigatiebalk biedt de bovenste werkbalk verschillende handige acties: Zoeken, Alles afspelen, Alles shufflen en Afspelen hervatten. Je kunt deze werkbalk tonen of verbergen met een eenvoudige swipe-down-beweging.

## Zoeken

De zoekfunctie stelt je in staat een specifiek nummer, artiest, album of genre te vinden in je muziekbibliotheek. Zoeken werkt lokaal op de muziekbibliotheekdatabase, dus het werkt volledig offline en geeft resultaten terwijl je typt.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Muziekbibliotheek Zoeken" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Optiesmenu

Elk nummer in je muziekbibliotheek heeft een menu met meer acties, toegankelijk via de drie-puntjesknop bij de nummertitel.

### Voor Individuele Nummers

- **Volgende afspelen** — voegt het nummer toe aan de bovenkant van de spelerwachtrij.
- **Later afspelen** — voegt het nummer toe aan de onderkant van de spelerwachtrij.
- **Toevoegen aan afspeellijst** — voegt het nummer toe aan een afspeellijst.
- **Toevoegen aan favorieten** — markeert het nummer als favoriet voor snelle toegang.
- **Downloaden** — slaat het nummer op in lokale bestanden. Het verschijnt in het tabblad **Lokale bestanden** en de sectie **Offline muziek**.
- **Audio-tags bewerken** — opent de ingebouwde audio-tageditor om ontbrekende metadata te herstellen.
- **Tonen in map** — toont de map waar het audiobestand is opgeslagen.
- **Tonen in Finder** — voor bestanden geïmporteerd van je Mac, toont deze actie de map waar het audiobestand zich bevindt op je Mac.
- **Openen in** — exporteert het audiobestand naar een andere app.
- **Verwijderen van cloudservice** — verwijdert het bestand uit zowel de muziekbibliotheek als de cloudopslag. **Deze actie is onomkeerbaar.**
- **Verwijderen uit muziekbibliotheek** — verwijdert het nummer uit je muziekbibliotheek, maar het bestand blijft in de opslag.

### Voor Nummerscollecties

Voor nummerscollecties zoals Albums, Artiesten, Genres of Componisten bevat het optiesmenu de volgende acties.

- **Alles afspelen** — vervangt de spelerwachtrij door nummers uit de geselecteerde collectie.
- **Volgende afspelen** — voegt nummers van deze collectie toe aan de bovenkant van de spelerwachtrij.
- **Later afspelen** — voegt nummers van deze collectie toe aan de onderkant van de spelerwachtrij.
- **Toevoegen aan afspeellijst** — voegt nummers van deze collectie toe aan een afspeellijst, met de optie om een nieuwe te maken.
- **Offline-modus inschakelen** — downloadt nummers van deze collectie naar lokale bestanden. Bestanden verschijnen in het tabblad **Lokale bestanden** en de sectie **Offline muziek**.
- **Afbeelding bewerken** — verander de albumhoes voor de nummerscollectie.
- **Toevoegen aan archief** — bundel de hele collectie in een enkel ZIP-bestand voor eenvoudige back-up of overdracht (Premium-functie).
- **Nummerlijst exporteren** — exporteer de collectie naar M3U, CSV of TXT voor gebruik in andere spelers of voor archivering.
- **Verwijderen uit muziekbibliotheek** — verwijdert de nummerscollectie uit je muziekbibliotheek. Deze actie verwijdert de eigenlijke bestanden niet uit de opslag.

## Selectiemodus

Je kunt selectiemodus activeren via de knop Meer acties rechtsboven. In deze modus kun je meerdere tracks tegelijk selecteren en batchacties uitvoeren.

## Albumdetails

Wanneer je de secties Artiest, Albumartiest of Componist opent, zie je een schakelaar voor Nummers / Alle albums / Exclusieve albums / Soloalbums.

- **Nummers** — toont alle nummers waarbij deze Artiest / Albumartiest / Componist voorkomt in de audiotags.
- **Alle albums** — toont compilatiealbums en alle albums waarbij de artiest aanwezig is.
- **Exclusieve albums** — toont albums waarbij de opgegeven artiest de enige artiest is met die albumnaam.
- **Soloalbums** — toont albums waarbij alleen de tracks van de opgegeven artiest verschijnen.

Dit is bijzonder nuttig voor het opschonen van rommelige 'Verschillende artiesten'-compilaties in grote bibliotheken.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Albumdetailsscherm" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Instellingen

Tik op Meer acties → Instellingen om je muziekbibliotheekvoorkeuren te configureren.

### Metadata Lezen

Wanneer je tracks aan de bibliotheek toevoegt, gaat de **metadatalezer** aan de slag. Dit achtergrondproces leest alle metadata van je tracks en organiseert ze op Artiest, Album, Genre en Componist.

**Metadata lezen op de achtergrond** als ingeschakeld, blijft de lezer werken in de achtergrondmodus.

**Metadatacodering normaliseren** wanneer ingeschakeld, normaliseert de app automatisch de metadatacodering voor alle nummers.

**Metadata opnieuw laden** markeert elk bestand in je muziekbibliotheek als ontbrekende metadata, waardoor de metadatalezer elk record vernieuwt.

**Metadata lezen starten** start de lezer handmatig.

### Online Synchronisatie

Automatische online muzieksync voegt tracks van verbonden cloudservices automatisch toe aan de muziekbibliotheek. Om het in te schakelen, open de muziekbibliotheeksinstellingen en selecteer synchronisatiemappen.

Online sync werkt alleen wanneer de app op de voorgrond is, dus het synchroniseren van een grote bibliotheek kan even duren. Om het te versnellen, houd Flacbox open, sluit je apparaat aan op stroom en schakel **Instellingen → Scherm → Altijd actief** in.

### Offline Synchronisatie

Configureer offline muzieknynchronisatie.

#### Gesynchroniseerde Offline Mappen

Wanneer je een online map op je cloudserver beschikbaar maakt voor offline gebruik (via het menu **Meer acties**), verschijnt deze hier. De mapinhoud wordt gedownload naar **Lokale bestanden → Offline mappen**.

#### Tijdsinterval

Kies hoe vaak de app offline mappen controleert op wijzigingen.

#### Lokale Mappen Scannen Starten

Scan alle lokale mappen in de applicatie **Documenten**-map op ondersteunde audiobestanden.

**Belangrijk:** Het is raadzaam periodiek offline muzieknynchronisatie te starten om je muziekbibliotheek up-to-date te houden met je lokale bestanden.

### Personalisatie

Configureer de stijl van het muziekbibliotheekscherm. Drie opties zijn beschikbaar: **Eenvoudig menu, Gegroepeerd menu, Tabbladdenmenu**.

### Albumhoezen

Configureer hoe de applicatie albumhoezen laadt en opslaat.

- **Netwerktype** — kies **Wi-Fi** of **Wi-Fi & Mobiele data** voor het downloaden van hoezen.
- **Albumhoezen laden voor online bestanden** — wanneer ingeschakeld, worden ingebedde albumhoezen geladen voor bestanden in de cloudopslag.
- **Zoeken in de map** — wanneer ingeschakeld, zoekt de app naar JPEG- of PNG-afbeeldingen in dezelfde map als de albumhoes als een track geen ingebedde hoes heeft.
- **Kwaliteit van hoezen** — selecteer de kwaliteit van albumhoezen op je apparaat.
- **Tonen in map** — open de map waar albumhoezen zijn gecached.
- **Alles verwijderen** — verwijder gecachte albumhoezen om opslagruimte vrij te maken.

### Afspeellijsten

Schakel de optie in om hetzelfde nummer twee keer aan een afspeellijst toe te voegen. Standaard is deze optie uitgeschakeld.

### Recenties

Beheer je lijst met recent afgespeelde nummers.

- **Lijst verwijderen** — verwijder de volledige lijst met recent afgespeelde nummers.
- **Lijstgrootte wijzigen** — stel het aantal items in dat in de lijst verschijnt.
- **Nummerlijst exporteren** — exporteer je lijst met recent afgespeelde nummers als M3U, CSV of TXT. Gedetailleerde instructies zijn beschikbaar [hier](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favorieten

Beheer de lijst met je favoriete nummers.

- **Gelijktijdig bewerken** — wanneer ingeschakeld, voegt het toevoegen van een nummer aan favorieten het zowel in de muziekbibliotheek als de bestandensectie tegelijk toe.
- **Lijst verwijderen** — verwijder de volledige lijst met favoriete nummers.
- **Nummerlijst exporteren** — net als Recenties, exporteer favorieten als M3U, CSV of TXT.

### Bibliotheek Verwijderen

Wis de muziekbibliotheekdatabase. Je muziekbestanden in de opslag blijven onaangeroerd.

### Inhoudslaadlimiet

Standaard gebruikt de applicatie paginering om de laadtijd van inhoud te verkorten en grote bibliotheken responsief te houden. Je kunt paginering uitschakelen om alles in één keer te laden.
