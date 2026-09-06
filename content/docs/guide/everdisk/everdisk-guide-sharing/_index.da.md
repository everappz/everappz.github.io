---
title: "Deling"
date: 2026-08-20
description: "Lær hvordan deling fungerer i Everdisk: tryk på Start for at forvandle din iPhone eller iPad til et trådløst drev, vælg hvad du vil dele (filer, mapper, fotos og musik), kør de fire servere (DLNA, HTTP, WebDAV, FTP), læs forbindelsesadresserne, se hvem der er forbundet, og hold delingen kørende over Wi-Fi eller et USB-kabel."
keywords: ["Everdisk deling", "trådløst drev iPhone", "start deling", "del filer iPhone", "del fotos over netværk", "DLNA HTTP WebDAV FTP", "hvad man skal dele", "sådan opretter du forbindelse", "hold appen åben", "deling over Wi-Fi eller USB-kabel"]
tags: ["everdisk", "vejledning", "deling"]
readingTime: 9
---


Fanen **Deling** er hjertet i Everdisk. Det er her, du forvandler din iPhone eller iPad til et trådløst drev, vælger præcis hvad du vil dele, og får de adresser, andre enheder bruger til at oprette forbindelse. Det er den første fane, du ser, når du åbner appen.

## Start og stop deling

Midt på Deling-skærmen er der en stor rund knap.

- Tryk på **Start** for at bringe alle dine aktiverede servere online på én gang. Knappen viser **Starter...** og derefter **Stop**, når delingen er i gang.
- Tryk på **Stop** for at tage alt offline igen. Forbundne enheder bliver koblet fra.

Mens delingen kører, er dine valgte filer, fotos og din musik tilgængelige for enhver enhed på det samme netværk, der forbinder med en af de fire metoder nedenfor.

> Deling kører kun, mens appen er åben. Se **Hold appen åben** nær slutningen af denne side for at forstå hvorfor, og hvordan du holder store overførsler kørende.

## Vælg hvad du vil dele

Inden du starter, skal du trykke på overskriften **Hvad skal deles** for at åbne tre grupper. Du kan dele en hvilken som helst kombination af dem, og du skal vælge mindst én ting, før delingen kan starte.

**Filer og mapper**

- Appens egen mappe **Dokumenter** deles som standard. Du kan stoppe med at dele den, hvis du foretrækker det.
- Tryk på **Tilføj mappe** for at dele en mappe fra hvor som helst på din enhed, eller **Tilføj fil** for at dele enkelte filer.
- Hvert delt element har en **Info**-knap og en **Stop deling**-knap.

**Fotos og videoer**

- Slå **Tillad adgang til hele fotobiblioteket** til for at dele hele dit foto- og videobibliotek, eller
- tryk på **Tilføj fotos** for at håndplukke kun de fotos og videoer, du vil dele.

**Musik**

- Slå **Tillad adgang til hele musikbiblioteket** til for at dele hele dit musikbibliotek, eller
- tryk på **Tilføj numre** for kun at dele udvalgte sange.
- Numre, der er beskyttede (DRM) eller kun gemt i skyen, kan ikke deles.

Hvis du forsøger at starte uden at have valgt noget, viser Everdisk en note om **Intet at dele**. Hvis du ændrer hvad der deles, mens delingen kører, skal du **stoppe og starte igen** for at anvende ændringen.

## De fire servere

Everdisk deler det samme indhold på fire måder samtidig. Hver metode er lavet til en bestemt slags enhed, og hver kan slås til eller fra under **Indstillinger → Deling → Forbindelser**. Som standard er alle fire slået til.

- **TV og Media Center (DLNA)** - til smart-TV og medieafspillere. De finder selv din enhed og viser dine fotos, videoer og din musik med miniaturer til forhåndsvisning.
- **Browser (HTTP)** - til enhver telefon, tablet eller computer. Den anden person åbner et link i en webbrowser for at gennemse og downloade dine filer. Der er intet at installere.
- **Computer (WebDAV)** - til en Mac, Windows-PC eller Linux-maskine. Din enhed vises som et almindeligt netværksdrev, så du kan trække filer begge veje.
- **Andre apps og enheder (FTP)** - til filapps og avancerede brugere, der taler FTP.

Se trinvise forbindelsesanvisninger for hver type i [Forbind dine enheder](/docs/guide/everdisk/everdisk-guide-connect).

## Sådan opretter du forbindelse, og forbindelsesadresser

Når du har trykket på Start, viser afsnittet **Sådan opretter du forbindelse** et kort for hver aktiv server med den præcise **adresse**, du skal indtaste på den anden enhed. Hver adresse er nem at kopiere - tryk på den for at kopiere, brug knappen **Del** for at sende den, eller tryk på **info (ⓘ)**-knappen for at få detaljerede anvisninger for hver protokol.

- DLNA-kortet viser en adresse til enhedsbeskrivelse, der ender på `/device-desc.xml`, til afspillere, der beder om en.
- Når din enhed er tilsluttet en Mac med et kabel, dukker der en ekstra adresse op med et **Kabelforbindelse**-mærke, som bruger din enheds `.local`-navn.

Du kan også åbne adressen som en **QR-kode**, så en anden enheds kamera kan hoppe direkte til den.

## Hvem er forbundet

Afsnittet **Hvem er forbundet** viser de enheder, der er forbundet til dig lige nu, i realtid. Tryk på knappen med flere handlinger ved siden af en enhed for at **Bloker denne enhed**, hvis du ikke genkender den. Blokerede enheder håndteres i [Adgang og privatliv](/docs/guide/everdisk/everdisk-guide-access).

## Dit enhedsnavn og din avatar

Hver enhed har et venligt navn (som "Speedy-Hare") og en farvet avatar. Det er det navn, et TV, en computer eller en anden app viser for din enhed på netværket, så den er nem at finde frem. Du kan generere navnet og avataren på ny gratis eller sætte et brugerdefineret navn, et ikon eller en fotoavatar med Premium. Se [Indstillinger](/docs/guide/everdisk/everdisk-guide-settings).

## Deling over Wi-Fi eller et USB-kabel

Deling kan køre i to situationer:

- **Over Wi-Fi** - din enhed og de andre enheder er på det samme Wi-Fi-netværk.
- **Over et USB-kabel** - din enhed er tilsluttet en **Mac** med et kabel, selv når der slet ikke er noget Wi-Fi. Det er hurtigere end Wi-Fi og bliver ved med at virke i et fly, på et hotel eller på et låst netværk.

Hvis hverken Wi-Fi eller et kabel er tilgængeligt, er **Start**-knappen deaktiveret, og der vises en note om **Ingen Wi-Fi-forbindelse**. Hvis forbindelsen falder ud, mens du deler, stopper Everdisk delingen automatisk og giver dig besked. Tryk på info-knappen på en af disse noter for at få en fuld forklaring.

## Hold appen åben

Fordi din iPhone eller iPad fungerer som server, **virker deling kun, mens Everdisk er åben på skærmen**. Hvis du lukker appen eller låser enheden i lang tid, kan systemet sætte appen på pause, og så stopper delingen.

Til store overførsler:

- Hold Everdisk åben og i forgrunden.
- Sæt din enhed til opladning.
- Sæt **Automatisk lås** til **Aldrig** i iOS Indstillinger, mens du overfører.

Du kan slå **Giv besked før frakobling** til (under Indstillinger → Deling), så Everdisk minder dig om at åbne appen igen, før systemet suspenderer den. Tryk på info-knappen på banneret **Hold appen åben** for at få flere detaljer.

## Næste skridt

- [Forbind dine enheder](/docs/guide/everdisk/everdisk-guide-connect) - forbind et TV, en computer, en browser, en telefon eller et USB-kabel.
- [Adgang og privatliv](/docs/guide/everdisk/everdisk-guide-access) - tilføj en adgangskode og styr redigering.
- [Indstillinger](/docs/guide/everdisk/everdisk-guide-settings) - slå servere til eller fra, og justér kvaliteten.
