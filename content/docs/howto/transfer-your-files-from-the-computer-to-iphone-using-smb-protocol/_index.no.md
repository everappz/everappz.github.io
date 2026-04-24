---
title: "Overfør filer fra datamaskinen til iPhone med SMB-protokollen"
description: "Lær hvordan du overfører og får tilgang til store filer fra Mac eller Windows PC til iPhone eller iPad ved hjelp av Evermusic og SMB-protokollen. En trinn-for-trinn-guide for sømløs strømming og filbehandling."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["overføre filer til iPhone SMB", "strømme PC-musikk på iPhone", "koble Mac til iPhone SMB", "Evermusic SMB-oppsett", "tilgang til datafiler iPhone", "Windows musikkdeling iOS", "SMB filoverføring Evermusic"]
---

{{< author-byline >}}


**Sammendrag:** Bruk Evermusic på iPhone eller iPad for å få tilgang til filer lagret på Mac eller Windows PC over det lokale nettverket via SMB. Ingen kabler, ingen iTunes, ingen skyopplasting nødvendig. Aktiver fildeling på datamaskinen, koble til i appen, og bla gjennom eller spill av filene dine trådløst.

Har du en omfattende samling av store filer på MAC-en eller PC-en din og ønsker å få tilgang til dem enkelt fra iPhone eller iPad? Appene våre gir en enkel løsning.

Følg disse trinnene for å aktivere sømløs tilgang mellom datamaskinen og iOS-enheten din ved hjelp av SMB-protokollen:

## Trinn 1: Aktiver SMB-protokollen på datamaskinen

**For MAC:**

1. Åpne "Systeminnstillinger" på MAC-en din.
2. Klikk på "Deling".
3. Aktiver tjenesten "Fildeling".
4. Legg til musikkmappen din i seksjonen "Delte mapper". Legg til en bruker og velg tillatelsesnivå (Les og skriv eller Kun les). Du kan velge "Alle: Kun les" for den tillagte musikkmappen.

   ![Mac-innstillingsskjerm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Husk datamaskinens URL (smb://192.168.xx.xx), da du vil bruke den i de neste trinnene.
6. Klikk på "Alternativer" og aktiver "Del filer og mapper via SMB".

   ![Mac-fildelingsskjerm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Aktiver "Windows-fildeling" for tilgjengelige kontoer.

   ![Mac SMB-delingsskjerm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**For Windows PC:**

1. Høyreklikk på musikkmappen din.
2. Velg "Egenskaper".
3. Gå til fanen "Deling".
4. Klikk på "Del..."
5. Velg personene du vil dele mappen med og spesifiser tillatelsesnivået. Du kan velge "Alle: Les" for den valgte musikkmappen.

   ![Windows SMB-delingsskjerm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Klikk "Ferdig".
7. Klikk "Ferdig" i vinduet "Fildeling", og husk mappestien.

   ![Windows SMB delt mappe](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Trinn 2: Koble til iOS-enheten din

1. Åpne appen på iPhone eller iPad.
2. Gå til fanen "Tilkoblinger".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Evermusic Tilkoblinger-skjerm"
  caption="Evermusic Tilkoblinger-skjerm"
  width="400"
>}}

*Hvis datamaskinen din vises i seksjonen "Tilgjengelige enheter":*

Hvis datamaskinen din er synlig i seksjonen "Tilgjengelige enheter" og du valgte "Alle: Kun les" i forrige trinn, trykk ganske enkelt på datamaskinen din, og den vil koble til automatisk.

*Hvis datamaskinen din ikke vises automatisk:*

1. Trykk "Koble til en skytjeneste".
2. Velg "SMB" på skjermen "Koble til en skytjeneste".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Evermusic Koble til en skytjeneste-skjerm"
  caption="Evermusic Koble til en skytjeneste-skjerm"
  width="400"
>}}

3. På skjermen "SMB-tilkobling" skriver du inn serverens URL med stien til den delte mappen. Du kan bruke servernavnet eller serverens IP:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Skriv inn brukernavn og passord, eller la disse feltene stå tomme hvis du valgte "Alle: Kun les" i forrige trinn.
5. Feltet "WORKGROUP" er valgfritt og bør brukes hvis du har et Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Evermusic SMB-tilkoblingsskjerm"
  caption="Evermusic SMB-tilkoblingsskjerm"
  width="400"
>}}

6. Når du har koblet til datamaskinen via SMB-protokollen, vil den vises i seksjonen "Skytjenester" på skjermen "Tilkoblinger".
7. Åpne den tilkoblede tjenesten og naviger til ønsket mappe.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Åpnet SMB-mappe i Evermusic"
  caption="Åpnet SMB-mappe i Evermusic"
  width="400"
>}}

8. Du kan bruke den innebygde filbehandleren til å redigere filene dine etter behov.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Evermusic filbehandler"
  caption="Evermusic filbehandler"
  width="400"
>}}

## Trinn 3: Løsning for SMB2-mapper med spesialtegn

Noen ganger kan du oppleve problemer med mapper som inneholder spesialtegn når du bruker SMB2-protokollen. Her er noen trinn for å løse dette problemet:

1. **Aktiver SMB 1:**  
   • Som en midlertidig løsning kan du prøve å aktivere SMB 1 på serveren din og i appinnstillingene. Dette kan hjelpe med å omgå problemene knyttet til spesialtegn i mappenavn.

2. **Bruk systemets filåpningsmeny:**  
   • Naviger til "Lokale filer".  
   • Rull ned til seksjonen "Filer på denne enheten".  
   • Trykk "Åpne filer..." eller "Åpne mapper...".  
   • Finn serveren din og velg filene eller mappene du trenger.  
   • Trykk "Åpne" for å bekrefte valget ditt.

3. **Alternative protokoller:**  
   • Hvis problemet vedvarer, vurder å koble til NAS-en din via WebDAV- eller DLNA-protokoller hvis NAS-en din støtter disse alternativene. Disse protokollene kan håndtere spesialtegn mer elegant.

Ved å følge disse trinnene kan du redusere problemene med spesialtegn i mappenavn når du bruker SMB2-protokollen.

## Konklusjon

Med disse trinnene kan du enkelt få tilgang til din store samling av filer fra MAC-en eller PC-en din på iPhone eller iPad ved hjelp av appene våre.

## Ofte stilte spørsmål

{{% details title="Kan jeg få tilgang til filer på PC-en min fra iPhone uten iTunes?" closed="true" %}}
Ja. Evermusic kobler til datamaskinen din via SMB på det lokale Wi-Fi-nettverket. Ingen iTunes- eller Finder-synkronisering er nødvendig. Aktiver fildeling på PC-en og koble til direkte fra appen.
{{% /details %}}

{{% details title="Fungerer SMB-filtilgang over internett?" closed="true" %}}
Nei. SMB er en lokal nettverksprotokoll. iPhone og datamaskinen din må være på samme Wi-Fi-nettverk. For ekstern tilgang kan du laste opp filer til en skytjeneste som Google Drive eller Dropbox og koble til den i Evermusic.
{{% /details %}}

{{% details title="Hvilke filtyper kan jeg få tilgang til via SMB?" closed="true" %}}
Evermusic støtter MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC og andre lydformater. Du kan også bla gjennom og administrere ikke-lydfiler ved hjelp av den innebygde filbehandleren.
{{% /details %}}

{{% details title="Kan jeg overføre filer fra en NAS til iPhone med SMB?" closed="true" %}}
Ja. De fleste NAS-enheter (Synology, QNAP, WD My Cloud og andre) støtter SMB. Koble til NAS-en din med de samme trinnene i denne guiden.
{{% /details %}}

{{% details title="Må jeg kopiere filer til iPhone for å spille dem?" closed="true" %}}
Nei. Evermusic strømmer filer direkte fra datamaskinen eller NAS-en din over nettverket. Filer kopieres ikke til iPhone med mindre du velger å laste dem ned for frakoblet avspilling.
{{% /details %}}

{{% details title="Er SMB-fildeling sikkert?" closed="true" %}}
SMB-fildeling fungerer bare på det lokale nettverket ditt. Andre enheter på forskjellige nettverk kan ikke få tilgang til de delte mappene dine. For ekstra sikkerhet kan du bruke brukernavn og passord i stedet for anonym (Alle) tilgang.
{{% /details %}}
