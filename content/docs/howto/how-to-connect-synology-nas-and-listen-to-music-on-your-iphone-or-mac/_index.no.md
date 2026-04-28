---
title: "Slik kobler du til Synology NAS og lytter til musikk på din iPhone eller Mac"
date: 2024-09-19
description: "Lær hvordan du kobler til Synology NAS ved hjelp av native API eller QuickConnect og strømmer musikk av høy kvalitet til din iPhone eller Mac med Evermusic og Flacbox."
keywords: ["synology nas", "strømme musikk", "quickconnect", "evermusic synology", "flacbox synology", "nas musikkspiller", "iphone nas musikk"]
tags: ["musikk", "strømming", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Sammendrag:** Koble Synology NAS til Evermusic eller Flacbox ved hjelp av Synologys native API -- enten manuelt via IP-adresse eller automatisk via QuickConnect ID. QuickConnect lar deg strømme musikk eksternt uten portvideresending. Begge appene støtter FLAC, MP3, WAV og andre hi-res formater.

Hvis du leter etter en sømløs måte å koble til Synology NAS og nyte musikkbiblioteket ditt på din iPhone eller Mac, er Evermusic og Flacbox-appene de perfekte løsningene. Disse appene støtter et bredt spekter av lydformater, inkludert FLAC, MP3 og WAV, noe som gjør det enkelt å strømme og lytte til musikk av høy kvalitet direkte fra din Synology NAS.

I denne guiden viser vi deg hvordan du kobler Synology NAS til Evermusic eller Flacbox-appen ved hjelp av Synologys native API og QuickConnect-funksjon. Ved å utnytte Synologys direkte API kan du sikkert få tilgang til musikkbiblioteket ditt utenfor hjemmenettverket uten å trenge kompliserte konfigurasjoner som WebDAV, SMB, DLNA. Med QuickConnect kan du strømme og administrere musikken din fra hvor som helst, ved hjelp av din iPhone eller Mac.

## Trinn 1: Konfigurer tillatelser for delt mappe (valgfritt)

1. Åpne **Kontrollpanel** og gå til seksjonen **Delt mappe**.

![Delt mappe](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Velg mappen **Music** og klikk **Rediger**.

3. I fanen **Tillatelser** konfigurerer du tillatelsene. Aktiver gjestetilgang med Kun lesing hvis du bare trenger å lytte til musikk, eller Lese/Skrive hvis du trenger å endre filer. Lagre endringene.

![Tillatelser](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Trinn 2: Finn Synology NAS IP-adresse

1. Åpne **Kontrollpanel** og gå til fanen **Nettverksgrensesnitt**.

![Nettverksgrensesnitt](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Eller bruk nettleseren din for å besøke [find.synology.com](http://find.synology.com).

![Finn Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Noter IP-adressen til Synology NAS (f.eks. 192.168.18.137).

## Trinn 3: Finn Synology NAS nettverksporter

Du finner den offisielle Synology-dokumentasjonen for standard DSM-nettverksporter i denne [Synology Knowledge Center-artikkelen](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM bruker følgende standardporter:
- **HTTP (Webtilgang):** Port **5000**
- **HTTPS (Sikker webtilgang):** Port **5001**

Dette er standardportene for tilgang til DSM-grensesnittet.

![Nettverksporter](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Trinn 4: Aktiver QuickConnect ID-funksjonen

En Synology QuickConnect ID er en unik identifikator som lar deg få tilgang til Synology NAS eksternt over internett uten å konfigurere kompliserte nettverksinnstillinger som portvideresending. QuickConnect forenkler ekstern tilgang ved å bruke Synologys servere for å opprette en forbindelse mellom NAS og enheten din, som smarttelefon eller datamaskin, via QuickConnect ID.

**Slik finner eller setter du opp QuickConnect ID:**

1. **Logg inn på DSM.**
2. Gå til **Kontrollpanel > Ekstern tilgang > QuickConnect**.
3. **Aktiver QuickConnect** og opprett eller vis din unike QuickConnect ID.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Trinn 5: Koble til Synology NAS på din iPhone/Mac med Evermusic eller Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) og [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) er begge musikkspiller-apper designet for iOS- og macOS-enheter, som hver tilbyr unike funksjoner og muligheter for å administrere og nyte musikkbiblioteket ditt.

1. Åpne Evermusic eller Flacbox-appen og gå til fanen **Tilkoblinger**.

![Tilkoblinger](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Velg **Koble til en skytjeneste** og velg **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Du har to tilkoblingsalternativer: **manuell** med serverens IP-adresse og port, eller **automatisk** via QuickConnect ID.

### Manuell tilkobling

For den manuelle metoden trenger du den direkte IP-adressen og portnummeret du hentet i tidligere trinn.

1. Skriv inn server-URLen du fikk i trinn 2, i følgende format: PROTOKOLL://IP_ADRESSE:PORTNUMMER
   - Bruk **port 5000** for HTTP og **port 5001** for HTTPS-tilkoblinger.

   For eksempel:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Det faktiske portnummeret kan bekreftes i trinn 3 i oppsettet ditt.
3. Skriv inn **brukernavn** og **passord** for Synology NAS.
4. Trykk **Logg inn** for å opprette tilkoblingen.

![Manuell tilkobling](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Automatisk tilkobling

For automatisk tilkobling bruker du **QuickConnect ID** fra trinn 4. I stedet for å manuelt skrive inn IP-adressen og portnummeret for Synology NAS, skriver du bare inn **QuickConnect ID**. Appen henter automatisk nødvendig tilkoblingsinformasjon.

Denne metoden lar deg få tilgang til NAS eksternt, selv utenfor hjemmenettverket, slik at du kan administrere filene dine fra internett uten å konfigurere portvideresending eller statiske IP-adresser.

![Automatisk tilkobling](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Tofaktorautentisering

Fra og med DSM 4.2 introduserte Synology **totrinnsverifisering** for å forbedre sikkerheten. Denne funksjonen krever en **engangspassord (OTP)**-kode, generert av en autentiseringsapp, i tillegg til dine vanlige innloggingsopplysninger. Hvis du har aktivert totrinnsverifisering, må du etter å ha skrevet inn brukernavn og passord også oppgi OTP for å logge inn på DSM-økten din.

Vær oppmerksom på at når økten din utløper, må appen autoriseres på nytt manuelt. For å autorisere på nytt:

1. Gå til fanen **Tilkoblinger** i appen.
2. Trykk på knappen **Flere handlinger** ved siden av servernavnet.
3. Velg **Innstillinger** fra menyen for å skrive inn den nye autentiseringskoden og fullføre reautorisasjonsprosessen.

Dette sikrer at selv om du får tilgang til NAS fra et upålitelig nettverk, forblir dataene dine sikre.

## Trinn 6: Naviger og spill musikk

1. Når du er tilkoblet, vises enheten i listen **Tilkoblede enheter**.

![Tilkoblede enheter](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Naviger til mappen **Music** og trykk på en lydfil for å starte avspilling.

![Spill musikk](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Trinn 7: Legg til tilkoblet skymappe i musikkbiblioteket

1. Åpne seksjonen **Musikkbibliotek** i appen.
2. Velg **Legg til musikk** og velg **Tilkoblinger**.
3. Velg din tilkoblede NAS-server og velg mappen **Music**. Trykk **Ferdig**.
4. Appen skanner musikkmappen og legger til støttede lydfiler i musikkbiblioteket. Metadata lastes inn, og sporene dine grupperes etter album, artist og sjanger.

## Konklusjon

Ved å følge disse trinnene kan du enkelt sette opp en tilkobling på Synology NAS og strømme hele musikkbiblioteket til din iPhone eller Mac med Evermusic eller Flacbox. Enten du er hjemme eller på farten, nyt sømløs tilgang av høy kvalitet til favorittlåtene dine fra hvor som helst med QuickConnect. Dra nytte av fleksibiliteten og bekvemmeligheten disse appene tilbyr, og begynn å administrere musikksamlingen din enkelt på alle enhetene dine.

Med sikker ekstern tilgang gjennom QuickConnect og støtte for et bredt spekter av lydformater, vil du aldri være langt fra musikken din. Nå er NAS-lagrede filer bare et trykk unna!

## FAQ

{{% details title="Hva er forskjellen mellom manuell tilkobling og QuickConnect?" closed="true" %}}
Manuell tilkobling bruker NAS IP-adresse og port, som fungerer på ditt lokale nettverk. QuickConnect bruker Synologys relétjeneste for å opprette en tilkobling fra hvor som helst over internett, uten portvideresending.
{{% /details %}}

{{% details title="Kan jeg strømme musikk fra Synology NAS utenfor hjemmenettverket mitt?" closed="true" %}}
Ja. Aktiver QuickConnect på Synology NAS og bruk QuickConnect ID i Evermusic eller Flacbox for å strømme musikk fra hvor som helst med internettforbindelse.
{{% /details %}}

{{% details title="Hvilke lydformater støttes ved strømming fra Synology NAS?" closed="true" %}}
Evermusic og Flacbox støtter FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD og mange andre formater. Alle støttede formater fungerer ved strømming fra Synology NAS.
{{% /details %}}

{{% details title="Trenger jeg tofaktorautentisering for å koble til?" closed="true" %}}
Nei, 2FA er valgfritt. Hvis du har aktivert totrinnsverifisering på Synology DSM, vil appen be om et engangspassord under innlogging. Du må autorisere på nytt når økten utløper.
{{% /details %}}

{{% details title="Bør jeg bruke Synology native API, WebDAV eller SMB for å koble til?" closed="true" %}}
Synology native API med QuickConnect er det beste valget for ekstern tilgang. For bruk på lokalt nettverk er SMB vanligvis det raskeste alternativet. WebDAV fungerer bra for både lokal og ekstern tilgang. Evermusic og Flacbox støtter alle tre protokollene.
{{% /details %}}
