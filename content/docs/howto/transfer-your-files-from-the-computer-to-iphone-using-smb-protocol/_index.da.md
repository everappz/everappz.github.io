---
title: "Overfør filer fra computeren til iPhone ved hjælp af SMB-protokollen"
description: "Lær hvordan du overfører og får adgang til store filer fra din Mac eller Windows PC til din iPhone eller iPad ved hjælp af Evermusic og SMB-protokollen. En trin-for-trin guide til problemfri streaming og filhåndtering."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["overfør filer til iPhone SMB", "stream PC-musik på iPhone", "tilslut Mac til iPhone SMB", "Evermusic SMB opsætning", "adgang til computerfiler iPhone", "Windows musikdeling iOS", "SMB filoverførsel Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Resumé:** Brug Evermusic på din iPhone eller iPad til at få adgang til filer gemt på din Mac eller Windows PC over dit lokale netværk via SMB. Ingen kabler, ingen iTunes, ingen cloud-upload nødvendig. Aktivér fildeling på din computer, opret forbindelse i appen, og gennemse eller afspil dine filer trådløst.

Har du en omfattende samling af store filer på din MAC eller PC og ønsker at få adgang til dem nemt fra din iPhone eller iPad? Vores apps giver en simpel løsning.

Følg disse trin for at aktivere problemfri adgang mellem din computer og iOS-enhed ved hjælp af SMB-protokollen:

## Trin 1: Aktivér SMB-protokollen på din computer

**For MAC:**

1. Åbn "Systemindstillinger" på din MAC.
2. Klik på "Deling".
3. Aktivér tjenesten "Fildeling".
4. Tilføj din musikmappe til sektionen "Delte mapper". Tilføj en bruger og vælg tilladelsesniveauet (Læs og skriv eller Kun læsning). Du kan vælge "Alle: Kun læsning" for den tilføjede musikmappe.

   ![Mac indstillingsskærm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Husk computerens URL (smb://192.168.xx.xx), da du skal bruge den i de næste trin.
6. Klik på "Indstillinger" og aktivér "Del filer og mapper via SMB".

   ![Mac fildelingsskærm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Aktivér "Windows fildeling" for tilgængelige konti.

   ![Mac SMB-delingsskærm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**For Windows PC:**

1. Højreklik på din musikmappe.
2. Vælg "Egenskaber".
3. Gå til fanen "Deling".
4. Klik på "Del..."
5. Vælg de personer, du vil dele mappen med, og angiv tilladelsesniveauet. Du kan vælge "Alle: Læs" for den valgte musikmappe.

   ![Windows SMB-delingsskærm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Klik på "Færdig".
7. Klik på "Færdig" i vinduet "Fildeling", og husk mappestien.

   ![Windows SMB delt mappe](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Trin 2: Tilslut din iOS-enhed

1. Åbn appen på din iPhone eller iPad.
2. Gå til fanen "Forbindelser".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Evermusic Forbindelser-skærm"
  caption="Evermusic Forbindelser-skærm"
  width="400"
>}}

*Hvis din computer vises i sektionen "Tilgængelige enheder":*

Hvis din computer er synlig i sektionen "Tilgængelige enheder", og du valgte "Alle: Kun læsning" i det foregående trin, skal du blot trykke på din computer, og den vil forbinde automatisk.

*Hvis din computer ikke vises automatisk:*

1. Tryk på "Tilslut en cloudtjeneste".
2. Vælg "SMB" på skærmen "Tilslut en cloudtjeneste".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Evermusic Tilslut en cloudtjeneste-skærm"
  caption="Evermusic Tilslut en cloudtjeneste-skærm"
  width="400"
>}}

3. På skærmen "SMB-forbindelse" skal du indtaste serverens URL med stien til den delte mappe. Du kan bruge servernavnet eller serverens IP:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Indtast dit brugernavn og adgangskode, eller lad disse felter stå tomme, hvis du valgte "Alle: Kun læsning" i det foregående trin.
5. Feltet "WORKGROUP" er valgfrit og bør bruges, hvis du har et Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Evermusic SMB-forbindelsesskærm"
  caption="Evermusic SMB-forbindelsesskærm"
  width="400"
>}}

6. Når du har tilsluttet din computer ved hjælp af SMB-protokollen, vises den i sektionen "Cloudtjenester" på skærmen "Forbindelser".
7. Åbn den tilsluttede tjeneste og naviger til den ønskede mappe.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Evermusic åbnet SMB-mappe"
  caption="Evermusic åbnet SMB-mappe"
  width="400"
>}}

8. Du kan bruge den indbyggede filhåndtering til at redigere dine filer efter behov.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Evermusic filhåndtering"
  caption="Evermusic filhåndtering"
  width="400"
>}}

## Trin 3: Løsning for SMB2-mapper med specialtegn

Nogle gange kan du støde på problemer med mapper, der indeholder specialtegn, når du bruger SMB2-protokollen. Her er nogle trin til at løse dette problem:

1. **Aktivér SMB 1:**  
   • Som en midlertidig løsning kan du prøve at aktivere SMB 1 på din server og i appens indstillinger. Dette kan hjælpe med at omgå problemerne relateret til specialtegn i mappenavne.

2. **Brug systemets filåbningsmenu:**  
   • Naviger til "Lokale filer".  
   • Rul ned til sektionen "Filer på denne enhed".  
   • Tryk på "Åbn filer..." eller "Åbn mapper...".  
   • Find din server og vælg de filer eller mapper, du har brug for.  
   • Tryk på "Åbn" for at bekræfte dit valg.

3. **Alternative protokoller:**  
   • Hvis problemet fortsætter, kan du overveje at oprette forbindelse til din NAS ved hjælp af WebDAV- eller DLNA-protokoller, hvis din NAS understøtter disse muligheder. Disse protokoller kan håndtere specialtegn mere elegant.

Ved at følge disse trin kan du afhjælpe problemerne med specialtegn i mappenavne, når du bruger SMB2-protokollen.

## Konklusion

Med disse trin kan du nemt få adgang til din store samling af filer fra din MAC eller PC på din iPhone eller iPad ved hjælp af vores apps.

## Ofte stillede spørgsmål

{{% details title="Kan jeg få adgang til filer på min PC fra min iPhone uden iTunes?" closed="true" %}}
Ja. Evermusic opretter forbindelse til din computer via SMB på dit lokale Wi-Fi-netværk. Ingen iTunes- eller Finder-synkronisering er nødvendig. Aktivér fildeling på din PC og opret forbindelse direkte fra appen.
{{% /details %}}

{{% details title="Fungerer SMB-filadgang over internettet?" closed="true" %}}
Nej. SMB er en lokal netværksprotokol. Din iPhone og computer skal være på det samme Wi-Fi-netværk. For fjernadgang skal du uploade filer til en cloudtjeneste som Google Drive eller Dropbox og oprette forbindelse til den i Evermusic.
{{% /details %}}

{{% details title="Hvilke filtyper kan jeg få adgang til via SMB?" closed="true" %}}
Evermusic understøtter MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC og andre lydformater. Du kan også gennemse og administrere ikke-lydfiler ved hjælp af den indbyggede filhåndtering.
{{% /details %}}

{{% details title="Kan jeg overføre filer fra en NAS til min iPhone ved hjælp af SMB?" closed="true" %}}
Ja. De fleste NAS-enheder (Synology, QNAP, WD My Cloud og andre) understøtter SMB. Opret forbindelse til din NAS ved hjælp af de samme trin i denne guide.
{{% /details %}}

{{% details title="Skal jeg kopiere filer til min iPhone for at afspille dem?" closed="true" %}}
Nej. Evermusic streamer filer direkte fra din computer eller NAS over netværket. Filer kopieres ikke til din iPhone, medmindre du vælger at downloade dem til offline afspilning.
{{% /details %}}

{{% details title="Er SMB-fildeling sikker?" closed="true" %}}
SMB-fildeling fungerer kun på dit lokale netværk. Andre enheder på forskellige netværk kan ikke få adgang til dine delte mapper. For yderligere sikkerhed skal du bruge et brugernavn og en adgangskode i stedet for anonym (Alle) adgang.
{{% /details %}}
