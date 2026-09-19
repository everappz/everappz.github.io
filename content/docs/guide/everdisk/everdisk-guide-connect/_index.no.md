---
title: "Koble til enhetene dine"
date: 2026-08-20
description: "Trinnvise instruksjoner for å koble til den trådløse Everdisk-disken din: se på en smart-TV over DLNA, åpne filene dine i en hvilken som helst nettleser, koble enheten din opp som en nettverksdisk i Finder, Windows eller Linux over WebDAV eller SMB (med valgfri SMB3/AES-kryptering), koble til filapper over FTP, og overfør over en USB-kabel til en Mac helt uten Wi-Fi."
keywords: ["koble til Everdisk", "streame til TV DLNA", "åpne filer i nettleser", "koble til nettverksdisk Finder", "WebDAV Windows Linux", "FTP-filapp", "USB-kabeloverføring Mac", "koble iPhone til datamaskin", "nettverksdisk iPhone"]
tags: ["everdisk", "veiledning", "koble til"]
readingTime: 11
---


Så snart du trykker **Start** på [Deling](/docs/guide/everdisk/everdisk-guide-sharing)-skjermen, kan andre enheter koble til filene dine på fem forskjellige måter. Velg metoden som passer enheten du vil bruke. I alle tilfeller vises den nøyaktige **adressen** du trenger i seksjonen **Slik kobler du til** på Deling-skjermen.

> Begge enhetene må være på **samme Wi-Fi-nettverk** - eller, for en Mac, koblet til med en **USB-kabel** (se den siste seksjonen).

## Se på en TV (DLNA)

Bruk dette for å vise bilder, videoer og musikk på en smart-TV eller mediespiller.

1. I **Innstillinger → Deling → Tilkoblinger**, sørg for at **TV og mediesenter** er på (det er på som standard).
2. På Deling-skjermen, trykk **Start**.
3. På TV-en åpner du den innebygde mediespilleren eller medieserver-appen (den kan hete Media Player, SmartShare, AllShare eller lignende).
4. Enheten din dukker opp i listen over medieservere med navnet sitt (for eksempel Speedy-Hare). Velg den.
5. Bla i de delte bildene, videoene og musikken din og start avspilling. Forhåndsvisningsminiatyrer vises automatisk.

Merk:

- DLNA kan ikke passordbeskyttes, så denne tilkoblingen er åpen for alle på samme Wi-Fi mens den er slått på.
- Hvis en video ikke vil spilles av på en eldre TV, senk videokvaliteten i **Innstillinger → Deling → Videoer** slik at Everdisk konverterer den til et mer kompatibelt format.

## Åpne i en nettleser (HTTP)

Bruk dette for å gi filer til hvem som helst med en nettleser - ingen app å installere.

1. I **Innstillinger → Deling → Tilkoblinger**, sørg for at **Nettleser** er på.
2. Trykk **Start**.
3. På Deling-skjermen kopierer du **Nettleser**-adressen (eller viser QR-koden dens).
4. På den andre telefonen, nettbrettet eller datamaskinen åpner du en hvilken som helst nettleser (Safari, Chrome, Edge, Firefox) og skriver inn den adressen.
5. Siden åpnes med de delte filene dine.

I nettleseren kan den andre personen:

- Bytte mellom **liste**- og **rutenett**-visning og sortere etter navn, dato eller størrelse.
- Se ekte **miniatyrer** for bilder, videoer, PDF-er og musikkomslag.
- Åpne et bilde til et **galleri** i fullskjerm med sveiping, knip for å zoome og en lysbildefremvisning.
- Spille musikk i en innebygd **spiller** med kø, tilfeldig rekkefølge og gjentakelse.
- **Laste ned** en hvilken som helst fil, eller laste ned en hel mappe (eller flere valgte elementer) som en enkelt **Archive.zip**.
- **Laste opp** filer tilbake til enheten din - bare hvis du slo på **Filredigering** (se [Tilgang og personvern](/docs/guide/everdisk/everdisk-guide-access)).

## Bruk den som en nettverksdisk (WebDAV)

Bruk dette for å få enheten din til å dukke opp som en vanlig disk på en Mac, Windows-PC eller Linux-maskin, slik at du kan dra filer begge veier.

**På en Mac (Finder)**

1. I **Innstillinger → Deling → Tilkoblinger**, sørg for at **Datamaskin** er på.
2. Trykk **Start** og noter **Datamaskin (WebDAV)**-adressen.
3. I Finder velger du **Gå → Koble til tjener** (eller trykk **⌘K**).
4. Skriv inn WebDAV-adressen nøyaktig slik den vises og klikk **Koble til**.
5. Skriv inn brukernavnet og passordet hvis du har angitt noe, ellers kobler du til som gjest.
6. Enheten din åpnes som en hvilken som helst annen nettverksdisk. Dra filer inn eller ut.

**På Windows**

1. Åpne **Filutforsker**, høyreklikk på **Denne PC-en** og velg **Legg til en nettverksplassering** (eller koble til en nettverksstasjon).
2. Skriv inn WebDAV-adressen som vises i Everdisk.
3. Skriv inn brukernavnet og passordet hvis du har angitt noe.

**På Linux**

1. Åpne filbehandleren og velg **Koble til tjener** (eller bruk `davs://` / `dav://`).
2. Skriv inn WebDAV-adressen som vises i Everdisk.

Om tilkoblingen er skrivebeskyttet eller toveis avhenger av innstillingen **Filredigering**. Med den på kan du kopiere filer over til enheten din og gi dem nytt navn eller slette dem; med den av er disken skrivebeskyttet.

## Koble til over SMB (kryptert nettverksdisk)

SMB er en nettverksdisk for Mac, Windows og Linux, bygget på fildelingen som allerede finnes i disse systemene, så enheten din dukker opp som en helt vanlig nettverksdisk - og det er den eneste tilkoblingen du kan kryptere.

1. I **Innstillinger → Deling → Tilkoblinger**, sørg for at **Datamaskin (avansert)** (SMB-tilkoblingen) er på.
2. Trykk **Start** og noter **SMB**-adressen, som ser ut som `smb://192.168.1.20:4455/Share`.
3. Koble til fra datamaskinen din:
   - **Mac:** enheten din dukker opp helt av seg selv i **Finder-sidefeltet** under **Steder** (Nettverk) - bare klikk på den og logg inn. For å koble til manuelt i stedet, velg **Gå → Koble til tjener** (**⌘K**) og skriv inn adressen.
   - **Windows:** åpne **Filutforsker**, høyreklikk på **Denne PC-en** og velg **Tilordne nettverksstasjon**, og skriv så inn `\\<address>\Share` med verten og delingsnavnet fra Deling-skjermen (eller skriv `smb://`-adressen i adressefeltet).
   - **Linux:** i filbehandleren velger du **Koble til tjener** og skriver inn adressen.
4. Skriv inn brukernavnet og passordet hvis du har angitt noe, ellers kobler du til som gjest.
5. Den delte mappen heter **Share**. Med **Filredigering** på kan du kopiere filer begge veier; med den av er den skrivebeskyttet.

**Slå på kryptering (anbefalt på Wi-Fi du ikke stoler på)**

SMB er den eneste Everdisk-tilkoblingen som kan krypteres. For å beskytte hver overføring med **SMB3-kryptering (AES)**:

1. I **Innstillinger → Deling → Tilgang**, sett opp et **Brukernavn** og **Passord** - krypterte tilkoblinger kan ikke være anonyme.
2. I **Innstillinger → Deling**, slå på **Krev SMB-kryptering**.
3. **Stopp og Start** deling på nytt slik at endringen trer i kraft.

Klienten din må støtte SMB3 - Finder på en moderne Mac, eller **Windows 10 og nyere**. SMB-kryptering er en Premium-funksjon.

## Koble til en filapp (FTP)

Bruk dette for filbehandler- og overføringsapper som snakker FTP (for eksempel FileZilla eller Cyberduck på en datamaskin).

1. I **Innstillinger → Deling → Tilkoblinger**, sørg for at **Andre apper og enheter** er på.
2. Trykk **Start** og noter **FTP**-adressen.
3. I FTP-appen din legger du til en ny tilkobling med den adressen.
4. Skriv inn brukernavnet og passordet hvis du har angitt noe, eller la dem stå tomme for anonym tilgang.

## Overfør over en USB-kabel (Mac, ingen Wi-Fi nødvendig)

Bruk dette når det ikke finnes noe Wi-Fi, eller når du vil ha den raskeste og mest private overføringen. Det fungerer bare med en **Mac**.

1. Koble din iPhone eller iPad til Mac-en med den vanlige ladekabelen.
2. Hvis du blir spurt på enheten, trykk **Stol på denne maskinen**.
3. I Everdisk, trykk **Start**. Et varsel om **Rask tilkobling tilgjengelig** dukker opp, og Deling-skjermen viser en ekstra adresse med et **Kabeltilkobling**-merke som slutter på `.local`.
4. På Mac-en åpner du Finder → **Gå → Koble til tjener** (**⌘K**) og skriver inn den `.local`-adressen (den fungerer for både Nettleser- og Datamaskin-tilkoblingene).
5. Enheten din åpnes over kabelen - raskere enn Wi-Fi, og dataene rører aldri ruteren eller internett.

Merk:

- Bruk **`.local`-navnet**, ikke en IP-adresse (IP-adresser fungerer bare over Wi-Fi), og aldri `localhost`.
- Kabelveien er **kun for Mac**. Windows-PC-er og Android-enheter må bruke Wi-Fi.
- Du kan også dra filer inn i Everdisk-mappen med Finder på en Mac, eller med Apple Devices-appen (eller iTunes) på Windows, gjennom standard fildeling i iOS.

## Neste steg

- [Tilgang og personvern](/docs/guide/everdisk/everdisk-guide-access) - legg til et passord, tillat opplastinger, blokker en enhet.
- [Bilder, musikk og video](/docs/guide/everdisk/everdisk-guide-media) - del hele biblioteket ditt og angi kvalitet.
- [Koble til servere](/docs/guide/everdisk/everdisk-guide-devices) - nå andre enheter fra Everdisk.
