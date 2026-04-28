---
title: "Sådan tilslutter du Synology NAS og lytter til musik på din iPhone eller Mac"
date: 2024-09-19
description: "Lær hvordan du tilslutter din Synology NAS ved hjælp af native API eller QuickConnect og streamer musik i høj kvalitet til din iPhone eller Mac med Evermusic og Flacbox."
keywords: ["synology nas", "stream musik", "quickconnect", "evermusic synology", "flacbox synology", "nas musikafspiller", "iphone nas musik"]
tags: ["musik", "streaming", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Resumé:** Tilslut din Synology NAS til Evermusic eller Flacbox ved hjælp af Synologys native API -- enten manuelt via IP-adresse eller automatisk via QuickConnect ID. QuickConnect lader dig streame musik eksternt uden port forwarding. Begge apps understøtter FLAC, MP3, WAV og andre hi-res formater.

Hvis du leder efter en problemfri måde at tilslutte din Synology NAS og nyde dit musikbibliotek på din iPhone eller Mac, er Evermusic og Flacbox apps de perfekte løsninger. Disse apps understøtter en bred vifte af lydformater, herunder FLAC, MP3 og WAV, hvilket gør det nemt at streame og lytte til musik i høj kvalitet direkte fra din Synology NAS.

I denne guide viser vi dig, hvordan du tilslutter din Synology NAS til Evermusic eller Flacbox appen ved hjælp af Synologys native API og QuickConnect-funktionen. Ved at udnytte Synologys direkte API kan du sikkert tilgå dit musikbibliotek uden for dit hjemmenetværk uden behov for komplicerede konfigurationer som WebDAV, SMB, DLNA. Med QuickConnect kan du streame og administrere din musik fra hvor som helst ved hjælp af din iPhone eller Mac.

## Trin 1: Konfigurer tilladelser for delt mappe (valgfrit)

1. Åbn **Kontrolpanel** og gå til sektionen **Delt mappe**.

![Delt mappe](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Vælg mappen **Musik** og klik på **Rediger**.

3. Under fanen **Tilladelser** konfigurer tilladelserne. Aktiver gæsteadgang med skrivebeskyttet, hvis du kun behøver at lytte til musik, eller læse/skrive, hvis du har brug for at ændre filer. Gem ændringerne.

![Tilladelser](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Trin 2: Find Synology NAS IP-adresse

1. Åbn **Kontrolpanel** og gå til fanen **Netværksgrænseflade**.

![Netværksgrænseflade](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Eller brug din webbrowser til at besøge [find.synology.com](http://find.synology.com).

![Find Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Noter IP-adressen for din Synology NAS (f.eks. 192.168.18.137).

## Trin 3: Find Synology NAS netværksporte

Du kan finde den officielle Synology-dokumentation for DSM standard netværksporte i denne [Synology Knowledge Center-artikel](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM bruger følgende standardporte:
- **HTTP (Webadgang):** Port **5000**
- **HTTPS (Sikker webadgang):** Port **5001**

Disse er standardportene for adgang til DSM-grænsefladen.

![Netværksporte](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Trin 4: Aktiver QuickConnect ID-funktionen

Et Synology QuickConnect ID er en unik identifikator, der giver dig adgang til din Synology NAS eksternt over internettet uden behov for at konfigurere komplicerede netværksindstillinger som port forwarding. QuickConnect forenkler fjernadgang ved at bruge Synologys servere til at etablere en forbindelse mellem din NAS og din enhed, såsom din smartphone eller computer, gennem QuickConnect ID'et.

**Sådan finder eller opretter du dit QuickConnect ID:**

1. **Log ind på DSM.**
2. Gå til **Kontrolpanel > Ekstern adgang > QuickConnect**.
3. **Aktiver QuickConnect** og opret eller se dit unikke QuickConnect ID.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Trin 5: Tilslut til Synology NAS på din iPhone/Mac ved hjælp af Evermusic eller Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) og [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) er begge musikafspiller-apps designet til iOS og macOS enheder, der hver tilbyder unikke funktioner og muligheder for at administrere og nyde dit musikbibliotek.

1. Åbn Evermusic eller Flacbox appen og gå til fanen **Forbindelser**.

![Forbindelser](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Vælg **Tilslut en cloudtjeneste** og vælg **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Du har to forbindelsesmuligheder: **manuel** ved hjælp af serverens IP-adresse og port, eller **automatisk** via QuickConnect ID.

### Manuel forbindelse

Til den manuelle metode skal du bruge den direkte IP-adresse og portnummer, som du hentede i de foregående trin.

1. Indtast server-URL'en, du fik i trin 2, i følgende format: PROTOKOL://IP_ADRESSE:PORTNUMMER
   - Brug **port 5000** til HTTP og **port 5001** til HTTPS-forbindelser.

   For eksempel:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Det faktiske portnummer kan bekræftes i trin 3 af din opsætning.
3. Indtast dit **brugernavn** og **adgangskode** til Synology NAS.
4. Tryk på **Log ind** for at etablere forbindelsen.

![Manuel forbindelse](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Automatisk forbindelse

Til den automatiske forbindelse bruger du **QuickConnect ID** fra trin 4. I stedet for manuelt at indtaste IP-adressen og portnummeret for din Synology NAS, skal du blot indtaste **QuickConnect ID**. Appen henter automatisk de nødvendige forbindelsesoplysninger.

Denne metode giver dig adgang til din NAS eksternt, selv uden for dit hjemmenetværk, så du kan administrere dine filer fra internettet uden behov for at konfigurere port forwarding eller statiske IP-adresser.

![Automatisk forbindelse](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## To-faktor-godkendelse

Fra DSM 4.2 introducerede Synology **2-trins-verifikation** for at forbedre sikkerheden. Denne funktion kræver en **engangskode (OTP)**, genereret af en godkendelses-app, ud over dine normale loginoplysninger. Hvis du har aktiveret 2-trins-verifikation, skal du efter at have indtastet dit brugernavn og adgangskode også indtaste OTP for at logge ind på din DSM-session.

Bemærk venligst, at når din session udløber, skal appen genautoriteres manuelt. For at genautoriere:

1. Gå til fanen **Forbindelser** i appen.
2. Tryk på knappen **Flere handlinger** ved siden af servernavnet.
3. Vælg **Indstillinger** fra menuen for at indtaste den nye godkendelseskode og fuldføre genautoriseringsprocessen.

Dette sikrer, at selv hvis du tilgår din NAS fra et upålideligt netværk, forbliver dine data sikre.

## Trin 6: Naviger og afspil musik

1. Når forbindelsen er oprettet, vises enheden i listen **Tilsluttede enheder**.

![Tilsluttede enheder](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Naviger til mappen **Musik** og tryk på en lydfil for at starte afspilningen.

![Afspil musik](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Trin 7: Tilføj tilsluttet cloudmappe til musikbiblioteket

1. Åbn sektionen **Musikbibliotek** i appen.
2. Vælg **Tilføj musik** og vælg **Forbindelser**.
3. Vælg din tilsluttede NAS-server og vælg mappen **Musik**. Tryk på **Færdig**.
4. Appen scanner musikmappen og tilføjer understøttede lydfiler til musikbiblioteket. Metadata indlæses, og dine numre grupperes efter album, kunstner og genre.

## Konklusion

Ved at følge disse trin kan du nemt oprette en forbindelse på din Synology NAS og streame hele dit musikbibliotek til din iPhone eller Mac ved hjælp af Evermusic eller Flacbox. Uanset om du er hjemme eller på farten, kan du nyde problemfri adgang i høj kvalitet til dine yndlingsnumre fra hvor som helst med QuickConnect. Udnyt den fleksibilitet og bekvemmelighed, som disse apps tilbyder, og begynd at administrere din musiksamling med lethed på tværs af alle dine enheder.

Med sikker fjernadgang via QuickConnect og understøttelse af en bred vifte af lydformater er du aldrig langt fra din musik. Nu er dine NAS-lagrede filer kun et tryk væk!

## Ofte stillede spørgsmål

{{% details title="Hvad er forskellen mellem manuel forbindelse og QuickConnect?" closed="true" %}}
Manuel forbindelse bruger NAS IP-adressen og porten, som fungerer på dit lokale netværk. QuickConnect bruger Synologys relay-tjeneste til at etablere en forbindelse fra hvor som helst over internettet, uden port forwarding.
{{% /details %}}

{{% details title="Kan jeg streame musik fra Synology NAS uden for mit hjemmenetværk?" closed="true" %}}
Ja. Aktiver QuickConnect på din Synology NAS og brug QuickConnect ID i Evermusic eller Flacbox til at streame musik fra hvor som helst med en internetforbindelse.
{{% /details %}}

{{% details title="Hvilke lydformater understøttes ved streaming fra Synology NAS?" closed="true" %}}
Evermusic og Flacbox understøtter FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD og mange andre formater. Alle understøttede formater fungerer ved streaming fra Synology NAS.
{{% /details %}}

{{% details title="Har jeg brug for to-faktor-godkendelse for at oprette forbindelse?" closed="true" %}}
Nej, to-faktor-godkendelse er valgfrit. Men hvis du har aktiveret 2-trins-verifikation på din Synology DSM, vil appen bede om en engangskode under login. Du skal genautoriere, når sessionen udløber.
{{% /details %}}

{{% details title="Skal jeg bruge Synology native API, WebDAV eller SMB til at oprette forbindelse?" closed="true" %}}
Synology native API med QuickConnect er det bedste valg til fjernadgang. Til brug på lokalt netværk er SMB typisk den hurtigste mulighed. WebDAV fungerer godt til både lokal og ekstern adgang. Evermusic og Flacbox understøtter alle tre protokoller.
{{% /details %}}
