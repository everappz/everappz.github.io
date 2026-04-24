---
title: "Stream din musik fra Mac eller PC til iPhone via SMB"
description: "Lær hvordan du streamer din musiksamling fra Mac eller Windows PC til din iPhone eller iPad med Evermusic og SMB-protokollen. En enkel trin-for-trin guide til at forbinde og nyde lyd uden synkronisering."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["stream musik fra Mac til iPhone", "SMB audio streaming iOS", "Evermusic SMB opsætning", "forbind PC musik iPhone", "Mac musikdeling iOS", "SMB Windows fil streaming", "Evermusic PC mappe adgang"]
aliases:
  - /post/stream-your-music-from-mac-or-pc-to-iphone-using-smb/
  - /single-post/Stream-your-music-from-MAC-or-PC-to-iPhone-using-SMB/
---

{{< author-byline >}}


**Kort fortalt:** Brug Evermusic-appen til iPhone eller iPad til at streame musik fra din Mac eller Windows PC over dit lokale netværk via SMB. Ingen synkronisering, ingen kopiering -- aktiver blot fildeling på din computer, forbind i appen og afspil. Opsætningen tager under 5 minutter.

Drukner du i et hav af musik på din MAC eller PC og vil nyde den ubesværet på din iPhone eller iPad? Led ikke længere end Evermusic. Med Evermusic er det utroligt nemt at forbinde din computer ved hjælp af SMB-protokollen og streame dine yndlingsmelodier uden at bekymre dig om at optage ekstra plads på enheden eller håndtere synkroniseringsproblemer. Her er en trin-for-trin guide til at komme i gang:

## Trin 1: Aktiver SMB-protokollen på din computer

![Evermusic - SMB-understøttelse - Mac delingsskærm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Hvis du bruger MAC

- Åbn Systemindstillinger -> Deling.
- Aktiver Fildeling-tjenesten.
- I sektionen "Delte mapper" tilføjer du din musikmappe, vælger en bruger og indstiller tilladelsesniveauer (Læs og skriv eller Kun læsning).
- For ekstra bekvemmelighed kan du vælge "Alle: Kun læsning" for musikmappen, hvilket gør den let tilgængelig i Evermusic.
- Glem ikke at huske din computers URL (smb://192.168.xx.xx) til de næste trin.

![Evermusic - SMB-understøttelse - Fildelingsskærm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Tryk på "Indstillinger" og aktiver "Del filer og mapper via SMB."
- Aktiver "Windows fildeling" for tilgængelige konti.

![Evermusic - SMB-understøttelse - Del filer og mapper skærm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Hvis du bruger en Windows PC

![Evermusic - SMB-understøttelse - Del filer på Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Højreklik på din musikmappe.
- Vælg "Egenskaber."
- Åbn fanen "Deling."
- Klik på "Del..."
- Vælg de personer, du vil dele med, og indstil deres tilladelsesniveauer.
- Ligesom med MAC kan du vælge "Alle: Læs" for den valgte musikmappe.
- Klik på "Færdig" for at gemme dine indstillinger.

![Evermusic - SMB-understøttelse - Delt mappe på Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Trin 2: Tilføj din computer automatisk

- Åbn nu Evermusic og gå til fanen "Forbindelser" ("Netværk" hvis du bruger en ældre version af appen).
- Hvis du ser din computer i sektionen "Tilgængelige enheder" ("Tilgængelige delinger" hvis du bruger en ældre version af appen) og valgte "Alle: Kun læsning" i det forrige trin, skal du blot trykke på din computer, og den vil forbinde automatisk.
- Hvis dette ikke sker, kan du tilføje din computer manuelt.

![Evermusic - SMB-understøttelse - Forbind konto skærm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Trin 3: Tilføj din computer manuelt

- Tryk på "Forbind en cloudtjeneste" ("Tilføj konto" hvis du bruger en ældre version af appen)
- Vælg "SMB" fra listen over tilgængelige servere på næste skærm.
- På "SMB" indstillingsskærmen:
  - Indtast serverens URL med stien til den delte mappe. Du kan indtaste servernavnet eller serverens IP. For eksempel:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Indtast dit brugernavn og adgangskode eller lad disse felter stå tomme, hvis du valgte "Alle: Kun læsning" i det forrige trin.
  - Feltet "WORKGROUP" er valgfrit og bør bruges, hvis du har et Active Directory-domæne.

![Evermusic - SMB-understøttelse - Indtast legitimationsoplysninger skærm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Når du har forbundet din SMB-konto, vises den i sektionen "Cloudtjenester" ("Konti"). Åbn den forbundne konto ved at trykke på den, naviger til musikmappen og tryk på en lydfil for at starte afspilleren.

![Evermusic - SMB-understøttelse - Åbn forbundet mappe skærm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Nyd din musiksamling problemfrit på din iPhone eller iPad med Evermusic.

![Evermusic - SMB-understøttelse - Lydafspiller skærm](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Trin 4: SMB2-løsning

Hvis du oplever problemer med at gennemse mapper eller afspille filer, der indeholder specialtegn (som ü, ö, é), kan dette være relateret til SMB2-protokollen. Vi arbejder aktivt på at løse dette problem.

Som en midlertidig løsning kan du prøve at aktivere SMB 1 på din server og i app-indstillingerne. Alternativt kan du forbinde til din SMB-server ved hjælp af systemets filåbningsmenuen. Sådan gør du:

1. Naviger til "Lokale filer."
2. Rul ned til sektionen "Filer på denne enhed" og tryk på "Åbn filer..." eller "Åbn mapper..."
3. Find din server og vælg de filer eller mapper, du har brug for.
4. Tryk på "Åbn" for at bekræfte dit valg.

## Trin 5: WebDAV-løsning

Derudover kan du prøve at forbinde til din NAS ved hjælp af WebDAV- eller DLNA-protokoller, hvis de understøttes.

Ved at følge disse trin kan du omgå problemerne relateret til specialtegn i filnavne og fortsætte med at nyde dine mediefiler.

P.S. Du kan også overføre lydfiler fra din MAC/PC til din iPhone ved hjælp af iTunes Fildeling og afspille lokale lydfiler. Lær mere om denne funktion i vores guide: [Sådan afspiller du iTunes-filer på iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Ofte stillede spørgsmål

{{% details title="Kan jeg streame musik fra min PC til min iPhone uden iTunes?" closed="true" %}}
Ja. Evermusic forbinder til din PC via SMB på dit lokale Wi-Fi-netværk. iTunes er ikke påkrævet. Aktiver blot fildeling på din PC og forbind i appen.
{{% /details %}}

{{% details title="Bruger SMB-streaming mobildata?" closed="true" %}}
Nej. SMB fungerer over dit lokale Wi-Fi-netværk. Ingen internetforbindelse eller mobildata er nødvendig.
{{% /details %}}

{{% details title="Hvilke lydformater understøtter Evermusic via SMB?" closed="true" %}}
Evermusic understøtter MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC og andre almindelige lydformater. Filer afspilles direkte fra SMB-delingen.
{{% /details %}}

{{% details title="Kan jeg streame musik fra en NAS til min iPhone?" closed="true" %}}
Ja. Hvis din NAS understøtter SMB (de fleste gør, herunder Synology, QNAP og WD My Cloud), kan du forbinde til den ved hjælp af de samme trin i denne guide.
{{% /details %}}

{{% details title="Skal jeg holde min computer tændt under streaming?" closed="true" %}}
Ja. Da Evermusic streamer filer direkte fra din computer, skal den være tændt og forbundet til det samme netværk som din iPhone.
{{% /details %}}

{{% details title="Er der en filstørrelsesgrænse for SMB-streaming?" closed="true" %}}
Nej. Evermusic streamer filer af enhver størrelse via SMB. Store tabsfrie filer (FLAC, WAV) fungerer uden problemer.
{{% /details %}}
