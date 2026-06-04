---
title: "Forbindelser"
date: 2020-02-01
description: "Lær hvordan du forbinder cloudlager, NAS og din computer til Evertag. Få adgang til og rediger lydfiler direkte fra cloudlager, personlig NAS eller Mac/PC."
keywords: [
  "Evertag cloudopsætning", "forbind iCloud til Evertag", "SMB filadgang iOS",
  "WebDAV lydtageditor", "NAS metadataredigering", "Wi-Fi Drive Evertag",
  "overfør lydfiler til iPhone", "Evertag iTunes File Sharing", "rediger FLAC-tags fra cloud"
]
tags: ["vejledning", "evertag", "forbindelser"]
readingTime: 11
---


På denne skærm kan du forbinde forskellige kilder, der indeholder dine lydfiler. Du kan integrere populære cloudtjenester som Google Drive, Dropbox, OneDrive, iCloud og andre samt forbinde din Mac eller PC. Derudover har du mulighed for at redigere lydfiler placeret i Apple Time Capsule, WD Cloud Home eller enhver NAS, der taler SMB eller WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Forbindelsesskærm" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Hurtig adgang

Øverst på Forbindelsesskærmen finder du en liste med **Hurtig adgang**. Enhver cloudmappe, du tilføjer til favoritter — selv en der er begravet flere niveauer dybt — vises her, så du kan hoppe til den uden at navigere gennem overordnede mapper hver gang.

## Forbind til cloudlager

- Åbn fanen 'Forbindelser'  
- Vælg 'Forbind til cloudlager' fra menuen  
- Vælg en cloudlagringstjeneste fra listen  
- Indtast dine legitimationsoplysninger, og tryk på 'Færdig.'

Hvis du støder på problemer, skal du kontrollere din internetforbindelse og login/adgangskode.  
I Premium-versionen af appen kan du tilføje et ubegrænset antal tjenester.

## Understøttede cloudlagringstjenester

I øjeblikket understøtter programmet de mest populære cloudlagringstjenester: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘) samt enhver SMB- eller WebDAV-server.

## Sikkerhed og privatliv

Vi bruger kun officielle SDK'er og sikre forbindelser til at interagere med tilsluttede cloudtjenester. Dit login og din adgangskode er ikke tilgængelige for programmet. Alle anmodninger fra programmet til cloudtjenesten er krypterede.

Når du indtaster dit login og din adgangskode, viser programmet dig den officielle autorisationsside leveret af cloudtjenesteudbyderen, og hele autorisationsprocessen foregår uden for programmet. Cloudtjenesteudbyderen sender et auth-token til programmet efter vellykket autorisering, og dette token bruges til at foretage API-kald.

Et auth-token er en digital nøgle, der giver tredjepartsprogrammer mulighed for at interagere med cloudlager. Auth-tokenet gemmes på din enhed i et sikkert systemlager kaldet Keychain. Du kan downloade dine filer fra den tilsluttede cloudtjeneste til enheden, og disse filer placeres i appens "Dokumenter"-mappe. Du kan fjerne disse filer til enhver tid ved hjælp af den indbyggede filhåndtering.

Programmet deler ingen oplysninger fra den tilsluttede cloudkonto. Du kan tilbagekalde adgangen til din cloudkonto til enhver tid ved at åbne kontoindstillingssiden i din webbrowser.

## Afvis auth-token

Log ind på din konto i en webbrowser, og naviger til indstillingssiden. Der kan du finde alle tredjepartsprogrammer, der er forbundet til din cloudkonto, og fjerne dem, hvis du ikke længere vil bruge det pågældende program. Detaljerede instruktioner er tilgængelige [her](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Du kan også frakoble de tilsluttede cloudkonti i programmet, og auth-tokenet fjernes også fra din enhed. Hvis du fjerner programmet fra din enhed, fjernes alle downloadede data og adgangstokens også.

## Frakobl et cloudlager eller skift konfiguration

- Få adgang til cloudlagringsindstillinger: Find først det cloudlager, du ønsker at administrere, i appens grænseflade.  
- Tryk på knappen '...': Ved siden af tjenesteoverskriften ser du en '...'-knap. Tryk på den for at få adgang til yderligere indstillinger.  
  - **Omdøb**: Hvis du vil ændre navnet på cloudtjenesten, som det vises på din liste, skal du vælge 'Omdøb.'  
  - **Indstillinger**: For at ændre konfigurationen eller godkendelsesdataene for cloudtjenesten skal du vælge 'Indstillinger.' Nogle gange skal du muligvis genautoritere den tilsluttede cloudtjeneste, hvis autorisationstokenet er udløbet.  
  - **Frakobl**: Hvis du ønsker at afbryde forbindelsen helt mellem appen og cloudtjenesten, skal du vælge 'Frakobl.' Vær opmærksom på, at denne mulighed fjerner alle sange tilknyttet denne cloudtjeneste fra appens musikbibliotek, men de forbliver på serveren.

## Forbind til computer eller NAS

Du kan også forbinde din computer, personlige NAS eller andre netværksenheder ved hjælp af SMB-, DLNA- eller WebDAV-protokollen.

## Forbind til computer ved hjælp af SMB

- Tryk på "Forbind til cloudlager" → SMB.  
- Indtast computerens IP-adresse og delt mappenavn i URL-feltet ved hjælp af formatet smb://computer-ip-adresse/delt-mappenavn  
- Vælg protokolversion: Auto, SMB1, SMB2  
- Indtast login og adgangskode (hvis påkrævet)  
- Tryk på "Færdig."

Hvis din forbindelse lykkes, vil du se det tilsluttede lager i sektionen "Cloudlager".  
En komplet vejledning til, hvordan du forbinder din Mac eller PC ved hjælp af SMB, er tilgængelig [her](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Forbind til NAS ved hjælp af WebDAV

Alle trin er de samme undtagen URL-feltet.  
URL'en skal være i formatet http://servernavn eller https://servernavn, hvis serveren understøtter SSL.  
En komplet vejledning til, hvordan du forbinder NAS ved hjælp af WebDAV-protokollen, er tilgængelig [her](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Tilgængelige enheder

Denne sektion viser alle enheder i dit lokale netværk, som du kan forbinde til via programmet.  
For at etablere en forbindelse til en enhed skal du følge disse trin:

- Åbn appen, og gå til sektionen "Tilgængelige enheder".  
- Tryk på den enhed, du vil forbinde til, fra listen.  
- Hvis nødvendigt, indtast dine loginoplysninger for at fuldføre forbindelsen.

## Wi-Fi Drive 

Wi-Fi Drive er en praktisk teknologi, der muliggør trådløs filoverførsel fra din computer til din iOS-enhed via en skrivebordswebbrowser.  
For at bruge denne funktion effektivt skal du sikre, at din enhed og computer er forbundet til det samme Wi-Fi-netværk.  
Her er en trinvis vejledning til, hvordan du bruger Wi-Fi Drive.

## Aktivér Wi-Fi Drive

- Åbn programmet, og gå til fanen "Forbindelser".  
- Vælg "Forbind via Wi-Fi" for at få adgang til Wi-Fi Drive-hovedskærmen.  
- Tryk på "Start Wi-Fi Drive" for at aktivere Wi-Fi Drive.

## Få adgang til Wi-Fi Drive på din computer

- På din computer (stationær eller bærbar) skal du åbne en webbrowser (såsom Chrome, Firefox eller Safari).  
- I browserens adresselinje skal du indtaste den URL, som programmet angiver.

## Overfør filer trådløst

Når websiden svarende til din iOS-enhed åbnes i browseren, kan du nemt trække og slippe filer fra din computer til websiden.  
De filer, du trækker og slipper, begynder at overføre til din iOS-enhed og er tilgængelige i programmet.

Detaljerede instruktioner til, hvordan du overfører filer trådløst ved hjælp af Wi-Fi Drive, er tilgængelige [her](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing er en anden teknologi, der giver dig mulighed for at overføre filer fra en computer til en enhed ved hjælp af Finder-appen på din Mac og et Lightning-kabel.  
- Forbind blot enheden til computeren ved hjælp af et kabel, og kør Finder-appen på din Mac.  
- Åbn "Placeringer" → "Din tilsluttede enhed" → "Filer" → og find den aktuelle app.  
- Tryk på app-ikonet for at se alle delte mapper.  
- Kopier filer fra computeren til den delte mappe på enheden ved hjælp af træk og slip.

Detaljerede instruktioner til, hvordan du bruger iTunes File Sharing, er tilgængelige [her](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Forbind et USB-flashkort

Hvis du har et SD-kort eller USB-stik, kan du forbinde det ved hjælp af en Lightning- eller USB-C-kortlæser på iPhone/iPad, eller tilslutte det direkte til en Mac. Appen understøtter i øjeblikket Apple Certified kortlæsere. Vi har detaljerede instruktioner til, hvordan du forbinder et USB-flashkort til din iPhone eller iPad og administrerer filer på det, tilgængelige [her](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Tilsluttede drev vises i sektionen **Eksterne tilbehør** på Forbindelsesskærmen.

## Filhåndtering

Når du har forbundet en cloudlagringstjeneste, skal du trykke på dens ikon for at se alle tilgængelige filer og mapper. Du kan bruge den indbyggede filhåndtering til at arbejde med disse filer — download, omdøb, flyt og mere. Når du starter et download, vises filen i overførselskøen. For at se overførselskøen skal du gå til fanen "Lokale filer" og trykke på de roterende pile øverst til venstre. Alle downloadede filer og mapper er tilgængelige i sektionen "Lokale filer".

## Øverste værktøjslinje

Den øverste værktøjslinje, bekvemt placeret under navigationsbjælken, tilbyder flere nyttige handlinger for nem adgang. Du kan vise eller skjule denne værktøjslinje ved hjælp af en simpel swipe ned-bevægelse. Her er de tilgængelige handlinger:

- **Søg**: Denne mulighed giver dig mulighed for at udføre en hurtig søgning i den aktuelle mappe, hvilket gør det nemt at finde specifikke filer eller mapper.  

## Mappeindstillinger

Når du åbner en mappe i appen, finder du et praktisk sæt handlinger tilgængeligt ved at trykke på knappen "..." øverst til højre på skærmen.  
Her er en oversigt over disse handlinger:

- **Vælg**: Aktivér filtilstandstilstand. Denne tilstand giver dig mulighed for at vælge en eller flere filer i mappen, hvilket gør det nemt at udføre handlinger på valgte elementer.  
- **Ny mappe**: Opret en ny mappe inden for den aktuelle mappe. Denne funktion giver dig mulighed for at organisere dine filer og holde dit bibliotek velstruktureret.   
- **Upload filer**: Upload filer fra din enhed til onlinemappen. Denne handling lader dig overføre filer til skyen eller serveren, så de er tilgængelige fra overalt.  
- **Søg**: Søg efter specifikke filer i den aktuelle mappe. Dette er særligt nyttigt til hurtigt at finde specifikke elementer i en stor samling.  
- **Sorter**: Sorter filer i mappen efter kriterier som navn, størrelse eller redigeringsdato. Standardsorteringstilstanden afspejler normalt sorteringsrækkefølgen på serveren, men du kan ændre den efter dine præferencer.  
- **Gitter/Listevisning**: Skift mellem to visningstilstande: tabelvisning og miniaturevisning. Tabelvisningen præsenterer filer i en liste, mens miniaturevisningen viser visuelle repræsentationer af filerne, hvilket gør det lettere at identificere indhold ved første øjekast.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Cloudmappe Sorter" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Rediger onlinefiler

Når du har brug for at administrere flere filer i dit cloudlager i denne app, kan du bruge markeringstilstand til at strømline dine handlinger. Følg disse trin for effektiv filhåndtering:

- **Aktivér markeringstilstand**: Åbn appen på din enhed, og naviger til sektionen, der indeholder dit cloudlager. Kig øverst til højre, hvor du finder knappen "..." (ellipse). Tryk på den, og vælg menupunktet "Vælg" for at aktivere markeringstilstand.  
- **Vælg filer**: Du vil bemærke, at der vises afkrydsningsfelter ved siden af hver fil eller mappe på listen. Vælg en eller flere filer eller mapper ved blot at trykke på afkrydsningsfelterne ved siden af dem.  
- **Udfør forskellige handlinger**: Når du har valgt de filer eller mapper, du vil administrere, har du adgang til flere handlinger skræddersyet til dine behov:

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Filvælg" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Filhandlinger

Nær titlen på filen vil du bemærke et ellipsesymbol "..." (tre prikker) — dette fungerer som handlingsmenuen.  
Tryk på det for at afsløre en liste over tilgængelige handlinger:

- **Rediger lydtags**: Ved at vælge denne mulighed kan du få adgang til den indbyggede tageditor, der giver dig mulighed for at ændre lydtags for den valgte fil. Filen downloades midlertidigt til en midlertidig mappe og uploades derefter til lageret, efter du har bekræftet ændringerne.  
- **Tilføj til favoritter**: Denne handling tilføjer filen til din liste over foretrukne filer for hurtig og bekvem adgang.  
- **Download**: Vælg denne handling for at downloade filen eller mappen til din enhed, så den er tilgængelig til offlinebrug.  
- **Omdøb**: Denne mulighed giver dig mulighed for at omdøbe filen direkte på fjernlageret, hvilket muliggør tilpasset filnavngivning.  
- **Flyt**: Vælg denne handling for at flytte filen til en anden mappe i dit cloudlager, hvilket hjælper med at opretholde en organiseret filstruktur.  
- **Åbn i**: Brug denne handling til at eksportere filen til en anden kompatibel app. Filen downloades til din enhed, og derefter vises deling-dialogen til yderligere deling eller interaktion.  
- **Slet**: Vær forsigtig med denne handling, da den permanent fjerner filen fra dit cloudlager. **Denne sletning kan ikke fortrydes**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Filindstillinger" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Hvis listen over handlinger overskrider den tilgængelige skærmsplads, skal du blot scrolle ned i handlingsmenuen for at få adgang til yderligere indstillinger.

## Mappehandlinger

For hver mappe i dit cloudlager har du forskellige handlinger tilgængelige. For at få adgang til disse muligheder skal du blot trykke på ellipseikonet "..." placeret ved siden af mappetitlen. Hvis du ikke ser alle handlinger, skal du scrolle ned for at afsløre flere valg. Her er de tilgængelige handlinger:

- **Tilføj til favoritter**: Brug denne handling til at tilføje mappen til din liste over foretrukne filer for hurtig og bekvem adgang.  
- **Download**: Download alt indholdet i mappen til din enhed til offlineadgang.  
- **Omdøb**: Omdøb mappen direkte på fjernlageret.  
- **Flyt**: Flyt mappen til en anden placering i dit cloudlager.  
- **Slet**: Vær forsigtig med denne handling, da den permanent fjerner mappen og dens indhold fra dit cloudlager. **Denne handling kan ikke fortrydes**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Mappeindstillinger" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
