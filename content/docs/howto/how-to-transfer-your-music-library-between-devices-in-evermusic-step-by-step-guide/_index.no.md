---
title: "Slik overfører du musikkbiblioteket mellom enheter i Evermusic: trinn-for-trinn-guide"
description: "Overfør enkelt Evermusic-musikkbiblioteket, spillelister, albumkunst og innstillinger fra en iPhone, iPad eller Mac til en annen ved hjelp av Wi-Fi Drive og sikkerhetskopieringsverktøy."
date: 2024-12-29
tags: ["musikkbibliotek", "overføring", "wifi", "sikkerhetskopi", "webdav", "gjenoppretting"]
keywords: ["overføre musikkbibliotek Evermusic", "sikkerhetskopiere og gjenopprette spillelister Evermusic", "Evermusic WiFi Drive", "synkronisere Evermusic mellom enheter", "flytte Evermusic-database", "Evermusic filoverføring", "gjenopprette lydspillerinnstillinger", "WebDAV musikkoverføring iOS"]
readingTime: 3
---

{{< author-byline >}}


**Kort oppsummert:** For å overføre Evermusic-biblioteket til en ny enhet, opprett en sikkerhetskopi på kildeenheten, start Wi-Fi Drive, koble til den andre enheten over samme nettverk, last ned sikkerhetskopien og musikkfilene, og gjenopprett deretter fra sikkerhetskopien. Hele prosessen tar omtrent 10 minutter avhengig av bibliotekets størrelse.

I denne guiden veileder vi deg gjennom overføring av hele musikkbiblioteket ditt — inkludert database, albumomslag og innstillinger — fra en enhet (iPhone eller Mac) til en annen. Mens automatisk synkronisering av musikkbibliotek og spillelister er en funksjon planlagt for fremtiden, må denne prosessen for øyeblikket gjøres manuelt.

## Trinn 1: Opprett en sikkerhetskopi på den første enheten

1. **Åpne appen på den første enheten** (den med musikkbiblioteket, spillelistene og tilkoblede skytjenester).
2. **Naviger til Innstillinger** og velg alternativet **Sikkerhetskopi og Gjenoppretting**.

![Backup and Restore](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. På skjermen **Sikkerhetskopi og Gjenoppretting** velger du elementene som skal inkluderes i sikkerhetskopifilen:
   - **Database** (inkluderer musikkbiblioteket og spillelistene dine)
   - **Albumomslag**
   - **Innstillinger**

Disse alternativene er aktivert som standard.

![Backup Options](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Trykk på **Sikkerhetskopier applikasjonsdata** for å starte prosessen.

![Backup Application Data](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Når sikkerhetskopieringen er fullført, vises en informasjonsmelding.

![Backup Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Trykk på **Vis fil** for å vise sikkerhetskopifilen i **Dokumenter**-katalogen. Sikkerhetskopifiler lagres vanligvis i **Backup**-mappen.

![Show Backup File](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Trinn 2: Start Wi-Fi Drive-serveren

1. Gå til **Tilkoblinger**-seksjonen i appen.
2. Bla ned til **Koble til via Wi-Fi** og trykk på den.

![Connect Using Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. På neste skjerm trykker du på **Start Wi-Fi Drive**.

- Valgfritt kan du angi brukernavn og passord for sikkerhet, men dette er unødvendig for hjemmenettverk.

4. Når den er startet, ser du tilgjengelige serveradresser. Dette kan brukes til nettlesere på datamaskiner eller WebDAV-apper, men i denne guiden går vi direkte videre til neste trinn.

![Wi-Fi Drive Started](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Trinn 3: Koble den andre enheten til den første

1. Åpne appen på den andre enheten (der du vil overføre biblioteket).
2. Sørg for at begge enhetene er koblet til samme Wi-Fi-nettverk.
3. På den andre enheten åpner du **Tilkoblinger**-fanen og velger **Tilgjengelige enheter**.

![Available Devices](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Du bør se en WebDAV-tilkobling kalt **Evermusic** (serveren vi startet på den første enheten). Trykk på den for å koble til.

5. Når du er tilkoblet, ser du alle mappene fra den første enheten.

![Connected to First Device](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Trinn 4: Forbered filoverføring

1. På den andre enheten går du til **Innstillinger > Filbehandler** og aktiverer **Lagre nedlastede filer til - Spør hver gang**.

- Dette sikrer at du kan velge målmappe for hver nedlasting.

2. Gå tilbake til **Tilkoblinger**-fanen og naviger til den tilkoblede WebDAV-serveren.

![Prepare for File Transfers](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Trinn 5: Overfør sikkerhetskopi og musikkfiler

1. Åpne **Backup**-mappen på den tilkoblede WebDAV-serveren.

![Backup Folder](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Trykk på knappen **Flere handlinger** (tre prikker) ved siden av sikkerhetskopifilen og velg **Laste ned**.

3. Opprett en **Backup**-mappe på den andre enheten for å lagre de nedlastede filene. Bekreft valget ved å trykke **Ferdig**.

![Download Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Overfør eventuelle ekstra musikkfiler:
   - Sjekk **Nedlastinger**-mappen eller andre relevante mapper på WebDAV-serveren.

![Transfer Music Files](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Bruk **Velge**-alternativet for å velge filer, og trykk deretter **Flere handlinger > Laste ned**. Lagre dem i tilsvarende mappe på den andre enheten for å opprettholde samme mappestruktur.

Målet er å overføre alle filer fra den første enheten til den nåværende enheten, og sikre at mappestrukturen forblir identisk. På denne måten forblir koblingene i musikkbiblioteket og spillelistene intakte. Merk at lokale filer lagret utenfor appens Dokumenter-katalog på den første enheten må overføres separat. Siden appen ikke kan få tilgang til disse filene i Wi-Fi Drive-modus, må du bruke Systemfiler-appen for overføringen.

![Transfer Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Trinn 6: Overvåk overføringsfremgangen

1. På den andre enheten går du til **Lokale filer**-seksjonen (eller **Nedlastinger**-fanen på iPad/Mac).

2. Trykk på knappen **Overføringsaktivitet** øverst til venstre for å overvåke overføringskøen.

![Monitor Transfer](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Trinn 7: Gjenopprett data fra sikkerhetskopi

1. Når sikkerhetskopifilen og alle nødvendige lydfiler er lastet ned til den andre enheten, åpner du **Backup**-mappen.

2. Trykk på sikkerhetskopifilen, og en bekreftelsesmelding vises.

![Restore Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Merk:** Gjenoppretting erstatter alle gjeldende musikkbibliotekdata, spillelister, innstillinger og albumkunst med sikkerhetskopidataene.

3. Trykk på **Gjenopprett** for å starte prosessen.

![Restore Process](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Etter at gjenopprettingen er fullført, bekrefter en melding at det var vellykket.

![Restoration Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Sjekk **Spillelister** eller **Musikkbibliotek**-seksjonene for å bekrefte gjenopprettingen.

![Verify Restoration](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Trinn 8: Reindekser musikkbiblioteket

1. For best resultat, reindekser biblioteket for å sikre at alle filer er vellykket oppdaget.

2. Gå til **Innstillinger > Musikkbibliotek > Offline musikksynkronisering** og velg **Start skanning av lokale mapper**.

Ved å følge disse trinnene overfører du musikkbiblioteket, spillelistene og innstillingene til en annen enhet. Hvis du støter på problemer, ikke nøl med å ta kontakt for støtte.

## Vanlige spørsmål

{{% details title="Kan jeg overføre Evermusic-biblioteket uten Wi-Fi?" closed="true" %}}
Wi-Fi Drive krever at begge enhetene er på samme Wi-Fi-nettverk. Det finnes for øyeblikket ingen Bluetooth- eller mobiloverføringsalternativ. Du kan alternativt bruke AirDrop eller Filer-appen til å manuelt flytte sikkerhetskopifilen og musikkmappene mellom enheter.
{{% /details %}}

{{% details title="Overføres skytjenestetilkoblingene med sikkerhetskopien?" closed="true" %}}
Sikkerhetskopien inkluderer databasen, spillelistene, albumomslagene og innstillingene dine. Innloggingsinformasjon for skytjenester er ikke inkludert av sikkerhetsgrunner. Du må koble til skykontoene dine på nytt på den nye enheten etter gjenoppretting.
{{% /details %}}

{{% details title="Hva skjer med det eksisterende biblioteket på den andre enheten?" closed="true" %}}
Gjenoppretting av en sikkerhetskopi erstatter alle eksisterende musikkbibliotekdata, spillelister, innstillinger og albumkunst på den andre enheten. Ta en separat sikkerhetskopi av den andre enheten først hvis du vil bevare dataene.
{{% /details %}}

{{% details title="Fungerer denne prosessen mellom iPhone og Mac?" closed="true" %}}
Ja. Evermusic støtter Wi-Fi Drive-overføring mellom alle kombinasjoner av iPhone, iPad og Mac. Begge enhetene trenger bare å være på samme Wi-Fi-nettverk.
{{% /details %}}

{{% details title="Hvor lang tid tar overføringen?" closed="true" %}}
Overføringstiden avhenger av størrelsen på musikkbiblioteket og Wi-Fi-hastigheten din. Et typisk bibliotek på noen få gigabyte overføres på 5-15 minutter over et standard hjemmenettverk.
{{% /details %}}
