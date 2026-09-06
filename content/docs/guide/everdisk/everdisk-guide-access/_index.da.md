---
title: "Adgang og privatliv"
date: 2026-08-20
description: "Hold din deling i Everdisk sikker: beskyt adgangen med login og adgangskode, styr om forbundne enheder kan uploade, omdøbe og slette med Redigering af filer, bloker ukendte enheder, vælg papirkurv vs. permanent sletning, og forstå hvorfor alt bliver på dit lokale netværk."
keywords: ["Everdisk adgangskodebeskyttelse", "redigering af filer kontakt", "bloker enhed", "blokerede enheder", "slet filer permanent", "kun lokalt netværk", "privat fildeling", "DLNA ingen adgangskode", "netværkssikkerhed"]
tags: ["everdisk", "vejledning", "adgang", "privatliv", "sikkerhed"]
readingTime: 8
---


Everdisk holder dine filer på dit eget netværk og giver dig enkle kontroller over, hvem der kan nå dem, og hvad de kan gøre. Du finder disse kontroller under **Indstillinger → Deling → Adgang** samt et par relaterede indstillinger i Filhåndtering.

## Beskyt adgangen med login og adgangskode

Som standard kan alle på det samme netværk, der har din adresse, åbne dine delte filer. For at kræve et login:

1. Gå til **Indstillinger → Deling → Adgang**.
2. Indtast et **Login** og en **Adgangskode**.
3. Nu beder forbindelserne **Browser (HTTP)**, **Computer (WebDAV)** og **Andre apps og enheder (FTP)** alle om de oplysninger, før de viser dine filer.

Lad begge felter stå tomme for åben adgang. Din adgangskode gemmes sikkert i enhedens Keychain.

> **DLNA er altid åben.** Forbindelsen TV og Media Center (DLNA) kan ikke beskyttes med adgangskode, så når den er slået til, kan enhver enhed på det samme Wi-Fi gennemse dine delte medier. Slå den fra, hvis du kun vil have beskyttede forbindelser, og del kun på netværk, du stoler på.

## Tillad eller bloker redigering (Redigering af filer)

Kontakten **Redigering af filer** styrer, om forbundne enheder kun kan se dine filer eller også ændre dem.

- **Til** (standard): forbundne enheder kan **uploade, omdøbe og slette** dine delte filer - så din enhed fungerer som et rigtigt netværksdrev, der virker begge veje.
- **Fra**: dine delte filer er **skrivebeskyttede**. Andre kan se og downloade, men kan ikke tilføje eller ændre noget.

Når du slår den til, vises en kort advarsel, fordi den lader andre ændre dine filer. Den bærer et **Vigtigt**-mærke, mens den er slået til.

## Bloker en enhed

Hvis du ser en enhed, du ikke genkender:

1. På Deling-skærmen finder du den under **Hvem er forbundet**.
2. Tryk på dens knap med flere handlinger, og vælg **Bloker denne enhed**.

Blokerede enheder er listet under **Indstillinger → Deling → Adgang → Blokerede enheder**, hvor du kan **ophæve blokeringen** af en eller **Ophæv blokering af alle**. Blokeringen følger enheden, selv om dens netværksadresse ændres (for forbindelserne Browser, Computer og TV).

## Papirkurv vs. permanent sletning

Når en fil slettes - af dig i filhåndteringen eller af en forbundet enhed - havner den normalt i en **papirkurv**, hvorfra den kan gendannes, så du kan få den tilbage.

Hvis du foretrækker, at filer fjernes med det samme uden mulighed for gendannelse, kan du slå **Slet filer permanent** til under **Indstillinger → Filhåndtering → Sletning af filer**. Den er slået fra som standard. **Den påvirker filhåndteringen på enheden** og **sletninger foretaget over netværket**; den ændrer ikke, hvordan systemets fotobibliotek eller musikbibliotek håndterer sletning.

## Alt bliver lokalt

Everdisk deler kun over dit **lokale netværk** - intet uploades til internettet, og der er ingen cloud-konto i midten. Et par ting er værd at vide:

- Everdisk har brug for iOS-tilladelsen **Lokalt netværk**, så enheder i nærheden kan finde den. Hvis den tilladelse er slået fra, forklarer en note, hvordan du slår den til igen i iOS Indstillinger.
- For størst mulig privatliv bør du kun dele, mens du er på et **hjemme- eller privat Wi-Fi**-netværk, du stoler på, og være forsigtig på offentligt Wi-Fi. Et login og en adgangskode hjælper, men det er ikke en erstatning for et betroet netværk.
- **Den mest private mulighed af alle er et USB-kabel til en Mac** - dataene går direkte over kablet og rører aldrig routeren eller internettet. Se [Forbind dine enheder](/docs/guide/everdisk/everdisk-guide-connect).

## Næste skridt

- [Deling](/docs/guide/everdisk/everdisk-guide-sharing) - vælg hvad du vil dele, og start delingen.
- [Indstillinger](/docs/guide/everdisk/everdisk-guide-settings) - alle indstillinger for Adgang og Filhåndtering samlet ét sted.
