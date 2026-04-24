---
title: "Strøm musikken din fra Mac eller PC til iPhone med SMB"
description: "Lær hvordan du strømmer musikksamlingen din fra Mac eller Windows PC til iPhone eller iPad ved hjelp av Evermusic og SMB-protokollen. En enkel steg-for-steg-guide for å koble til og nyte lyd uten synkronisering."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["strømme musikk fra Mac til iPhone", "SMB lydstrømming iOS", "Evermusic SMB oppsett", "koble PC musikk iPhone", "Mac musikkdeling iOS", "SMB Windows filstrømming", "Evermusic PC mappetilgang"]
---

{{< author-byline >}}


**Kort fortalt:** Bruk Evermusic-appen for iPhone eller iPad til å strømme musikk fra Mac eller Windows PC over det lokale nettverket ditt ved hjelp av SMB. Ingen synkronisering, ingen kopiering -- bare aktiver fildeling på datamaskinen din, koble til i appen og spill av. Oppsettet tar under 5 minutter.

Drukner du i et hav av musikk på MAC-en eller PC-en din og vil nyte den problemfritt på iPhone eller iPad? Se ikke lenger enn Evermusic. Med Evermusic er det utrolig enkelt å koble til datamaskinen din ved hjelp av SMB-protokollen og strømme favorittmelodiene dine uten å bekymre deg for å ta opp ekstra lagringsplass eller håndtere synkroniseringsproblemer. Her er en steg-for-steg-guide for å komme i gang:

## Steg 1: Aktiver SMB-protokollen på datamaskinen din

![Evermusic - SMB-støtte - Mac delingsskjerm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Hvis du bruker MAC

- Åpne Systeminnstillinger -> Deling.
- Aktiver Fildeling-tjenesten.
- I seksjonen "Delte mapper" legger du til musikkmappen din, velger en bruker og setter tilgangsnivåer (Les og skriv eller Kun lesing).
- For ekstra bekvemmelighet kan du velge "Alle: Kun lesing" for musikkmappen, noe som gjør den lett tilgjengelig i Evermusic.
- Ikke glem å huske datamaskinens URL (smb://192.168.xx.xx) for de neste stegene.

![Evermusic - SMB-støtte - Fildelingsskjerm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Trykk på "Alternativer" og aktiver "Del filer og mapper ved hjelp av SMB."
- Aktiver "Windows fildeling" for tilgjengelige kontoer.

![Evermusic - SMB-støtte - Del filer og mapper skjerm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Hvis du bruker en Windows PC

![Evermusic - SMB-støtte - Del filer på Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Høyreklikk på musikkmappen din.
- Velg "Egenskaper."
- Åpne fanen "Deling."
- Klikk "Del..."
- Velg personene du vil dele med og sett deres tilgangsnivåer.
- Som med MAC kan du velge "Alle: Les" for den valgte musikkmappen.
- Klikk "Ferdig" for å lagre innstillingene dine.

![Evermusic - SMB-støtte - Delt mappe på Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Steg 2: Legg til datamaskinen din automatisk

- Åpne nå Evermusic og gå til fanen "Tilkoblinger" ("Nettverk" hvis du bruker en eldre versjon av appen).
- Hvis du ser datamaskinen din i seksjonen "Tilgjengelige enheter" ("Tilgjengelige delinger" hvis du bruker en eldre versjon av appen) og valgte "Alle: Kun lesing" i forrige steg, trykk bare på datamaskinen din, og den kobles til automatisk.
- Hvis dette ikke skjer, kan du legge til datamaskinen din manuelt.

![Evermusic - SMB-støtte - Koble til konto skjerm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Steg 3: Legg til datamaskinen din manuelt

- Trykk på "Koble til en skytjeneste" ("Legg til konto" hvis du bruker en eldre versjon av appen)
- Velg "SMB" fra listen over tilgjengelige servere på neste skjerm.
- På "SMB"-innstillingsskjermen:
  - Skriv inn serverens URL med banen til den delte mappen. Du kan skrive inn servernavnet eller serverens IP. For eksempel:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Skriv inn brukernavnet og passordet ditt eller la disse feltene stå tomme hvis du valgte "Alle: Kun lesing" i forrige steg.
  - "WORKGROUP"-feltet er valgfritt og bør brukes hvis du har et Active Directory-domene.

![Evermusic - SMB-støtte - Skriv inn påloggingsinformasjon skjerm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Når du har koblet til SMB-kontoen din, vises den i seksjonen "Skytjenester" ("Kontoer"). Åpne den tilkoblede kontoen ved å trykke på den, naviger til musikkmappen og trykk på en lydfil for å starte avspilleren.

![Evermusic - SMB-støtte - Åpne tilkoblet mappe skjerm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Nyt musikksamlingen din sømløst på iPhone eller iPad med Evermusic.

![Evermusic - SMB-støtte - Lydavspiller skjerm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Steg 4: SMB2-løsning

Hvis du opplever problemer med å bla gjennom mapper eller spille av filer som inneholder spesialtegn (som ü, ö, é), kan dette være relatert til SMB2-protokollen. Vi jobber aktivt med å løse dette problemet.

Som en midlertidig løsning kan du prøve å aktivere SMB 1 på serveren din og i appinnstillingene. Alternativt kan du koble til SMB-serveren din via systemets filåpningsmeny. Slik gjør du det:

1. Naviger til "Lokale filer."
2. Rull ned til seksjonen "Filer på denne enheten" og trykk "Åpne filer..." eller "Åpne mapper..."
3. Finn serveren din og velg filene eller mappene du trenger.
4. Trykk "Åpne" for å bekrefte valget ditt.

## Steg 5: WebDAV-løsning

I tillegg kan du prøve å koble til NAS-en din ved hjelp av WebDAV- eller DLNA-protokoller hvis de støttes.

Ved å følge disse stegene kan du omgå problemene relatert til spesialtegn i filnavn og fortsette å nyte mediefilene dine.

P.S. Du kan også overføre lydfiler fra MAC/PC-en din til iPhone ved hjelp av iTunes Fildeling og spille av lokale lydfiler. Lær mer om denne funksjonen i guiden vår: [Hvordan spille iTunes-filer på iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Ofte stilte spørsmål

{{% details title="Kan jeg strømme musikk fra PC-en min til iPhone uten iTunes?" closed="true" %}}
Ja. Evermusic kobler til PC-en din via SMB på det lokale Wi-Fi-nettverket ditt. iTunes er ikke nødvendig. Bare aktiver fildeling på PC-en din og koble til i appen.
{{% /details %}}

{{% details title="Bruker SMB-strømming mobildata?" closed="true" %}}
Nei. SMB fungerer over det lokale Wi-Fi-nettverket ditt. Ingen internettforbindelse eller mobildata er nødvendig.
{{% /details %}}

{{% details title="Hvilke lydformater støtter Evermusic via SMB?" closed="true" %}}
Evermusic støtter MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC og andre vanlige lydformater. Filer spilles av direkte fra SMB-delingen.
{{% /details %}}

{{% details title="Kan jeg strømme musikk fra en NAS til iPhone?" closed="true" %}}
Ja. Hvis NAS-en din støtter SMB (de fleste gjør det, inkludert Synology, QNAP og WD My Cloud), kan du koble til den med de samme stegene i denne guiden.
{{% /details %}}

{{% details title="Må jeg holde datamaskinen min påslått under strømming?" closed="true" %}}
Ja. Siden Evermusic strømmer filer direkte fra datamaskinen din, må den være påslått og koblet til det samme nettverket som iPhone.
{{% /details %}}

{{% details title="Er det en filstørrelsesgrense for SMB-strømming?" closed="true" %}}
Nei. Evermusic strømmer filer av enhver størrelse via SMB. Store tapsfrie filer (FLAC, WAV) fungerer uten problemer.
{{% /details %}}
