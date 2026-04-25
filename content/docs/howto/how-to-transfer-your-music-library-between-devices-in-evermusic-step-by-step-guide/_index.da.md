---
title: "Sådan overfører du dit musikbibliotek mellem enheder i Evermusic: trin-for-trin guide"
description: "Overfør nemt dit Evermusic musikbibliotek, afspilningslister, albumcovers og indstillinger fra en iPhone, iPad eller Mac til en anden ved hjælp af Wi-Fi Drive og backup-værktøjer."
date: 2024-12-29
tags: ["musikbibliotek", "overførsel", "wifi", "backup", "webdav", "gendannelse"]
keywords: ["overfør musikbibliotek Evermusic", "backup og gendannelse af afspilningslister Evermusic", "Evermusic WiFi Drive", "synkroniser Evermusic mellem enheder", "flyt Evermusic database", "Evermusic filoverførsel", "gendan lydafspiller indstillinger", "WebDAV musikoverførsel iOS"]
readingTime: 3
---

{{< author-byline >}}


**Kort sagt:** For at overføre dit Evermusic-bibliotek til en ny enhed skal du oprette en backup på kildeenheden, starte Wi-Fi Drive, forbinde den anden enhed over det samme netværk, downloade backuppen og musikfilerne og derefter gendanne fra backup. Hele processen tager omkring 10 minutter afhængigt af bibliotekets størrelse.

I denne guide gennemgår vi overførslen af hele dit musikbibliotek — inklusive database, albumcovers og indstillinger — fra en enhed (iPhone eller Mac) til en anden. Mens automatisk synkronisering af musikbibliotek og afspilningslister er en funktion, der er planlagt til fremtiden, skal denne proces i øjeblikket udføres manuelt.

## Trin 1: Opret en backup på den første enhed

1. **Åbn appen på din første enhed** (den med dit musikbibliotek, afspilningslister og tilsluttede cloudtjenester).
2. **Gå til Indstillinger** og vælg muligheden **Backup og gendannelse**.

![Backup og gendannelse](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. På skærmen **Backup og gendannelse** skal du vælge de elementer, der skal inkluderes i din backupfil:
   - **Database** (inkluderer dit musikbibliotek og afspilningslister)
   - **Albumcovers**
   - **Indstillinger**

Disse muligheder er aktiveret som standard.

![Backup-muligheder](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Tryk på **Backup applikationsdata** for at starte processen.

![Backup applikationsdata](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Når backuppen er færdig, vises en informationsalarm.

![Backup fuldført](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Tryk på **Vis fil** for at afsløre backupfilen i mappen **Dokumenter**. Backupfiler gemmes typisk i mappen **Backup**.

![Vis backupfil](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Trin 2: Start Wi-Fi Drive-serveren

1. Gå til sektionen **Forbindelser** i appen.
2. Rul ned til **Forbind via Wi-Fi** og tryk på den.

![Forbind via Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. På næste skærm skal du trykke på **Start Wi-Fi Drive**.

- Valgfrit kan du indstille et login og en adgangskode for sikkerhed, men dette er unødvendigt for hjemmenetværk.

4. Når den er startet, vil du se de tilgængelige serveradresser. Dette kan bruges til desktop-browsere eller WebDAV-apps, men i denne guide fortsætter vi direkte til de næste trin.

![Wi-Fi Drive startet](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Trin 3: Forbind din anden enhed til den første

1. Åbn appen på din anden enhed (hvor du vil overføre biblioteket til).
2. Sørg for, at begge enheder er forbundet til det samme Wi-Fi-netværk.
3. På den anden enhed skal du åbne fanen **Forbindelser** og vælge **Tilgængelige enheder**.

![Tilgængelige enheder](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Du bør se en WebDAV-forbindelse med navnet **Evermusic** (serveren vi startede på den første enhed). Tryk på den for at forbinde.

5. Når du er forbundet, vil du se alle mapper fra den første enhed.

![Forbundet til første enhed](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Trin 4: Forbered filoverførsler

1. På den anden enhed skal du gå til **Indstillinger > Filhåndtering** og aktivere **Gem downloadede filer til - Spørg hver gang**.

- Dette sikrer, at du kan vælge destinationsmappen for hver download.

2. Vend tilbage til fanen **Forbindelser** og naviger til den tilsluttede WebDAV-server.

![Forbered filoverførsler](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Trin 5: Overfør backup og musikfiler

1. Åbn mappen **Backup** på den tilsluttede WebDAV-server.

![Backup-mappe](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Tryk på knappen **Flere handlinger** (tre prikker) ved backupfilen og vælg **Downloade**.

3. Opret en **Backup**-mappe på den anden enhed til at gemme de downloadede filer. Bekræft dit valg ved at trykke på **Færdig**.

![Download backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Overfør eventuelle yderligere musikfiler:
   - Tjek mappen **Hente** eller andre relevante mapper på WebDAV-serveren.

![Overfør musikfiler](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Brug muligheden **Vælg** til at vælge filer, og tryk derefter på **Flere handlinger > Downloade**. Gem dem i den tilsvarende mappe på den anden enhed for at bevare den samme mappestruktur.

Målet er at overføre alle filer fra din første enhed til din aktuelle enhed og sikre, at mappestrukturen forbliver identisk. På denne måde forbliver links i dit musikbibliotek og afspilningslister intakte. Bemærk, at lokale filer gemt uden for appens Dokumenter-mappe på din første enhed skal overføres separat. Da appen ikke kan få adgang til disse filer i Wi-Fi Drive-tilstand, skal du bruge systemets Filer-app til deres overførsel.

![Overførsel fuldført](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Trin 6: Overvåg overførselsforløbet

1. På den anden enhed skal du gå til sektionen **Lokale filer** (eller fanen **Hente** på iPad/Mac).

2. Tryk på knappen **Overførselsaktivitet** i øverste venstre hjørne for at overvåge overførselskøen.

![Overvåg overførsel](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Trin 7: Gendan data fra backup

1. Når backupfilen og alle nødvendige lydfiler er downloadet til den anden enhed, skal du åbne mappen **Backup**.

2. Tryk på backupfilen, og en bekræftelsesmeddelelse vises.

![Gendan backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Bemærk:** Gendannelse vil erstatte alle aktuelle musikbiblioteksdata, afspilningslister, indstillinger og albumcovers med backupdataene.

3. Tryk på **Gendan** for at starte processen.

![Gendannelsesproces](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Når gendannelsen er fuldført, bekræfter en alarm succesen.

![Gendannelse fuldført](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Tjek sektionerne **Afspilningslister** eller **Musikbibliotek** for at verificere gendannelsen.

![Verificer gendannelse](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Trin 8: Genindekser musikbiblioteket

1. For de bedste resultater skal du genindeksere dit bibliotek for at sikre, at alle filer registreres korrekt.

2. Gå til **Indstillinger > Musikbibliotek > Offline musiksynkronisering** og vælg **Start scanning af lokale mapper**.

Ved at følge disse trin vil du med succes overføre dit musikbibliotek, afspilningslister og indstillinger til en anden enhed. Hvis du støder på problemer, tøv ikke med at kontakte support.

## Ofte stillede spørgsmål

{{% details title="Kan jeg overføre mit Evermusic-bibliotek uden Wi-Fi?" closed="true" %}}
Wi-Fi Drive kræver, at begge enheder er på det samme Wi-Fi-netværk. Der er i øjeblikket ingen Bluetooth- eller mobildata-overførselsmulighed. Du kan alternativt bruge AirDrop eller Filer-appen til manuelt at flytte backupfilen og musikmapper mellem enheder.
{{% /details %}}

{{% details title="Overføres mine cloudtjenesteforbindelser med backuppen?" closed="true" %}}
Backuppen inkluderer din database, afspilningslister, albumcovers og indstillinger. Loginoplysninger til cloudtjenester er ikke inkluderet af sikkerhedsmæssige årsager. Du skal tilslutte dine cloudkonti igen på den nye enhed efter gendannelse.
{{% /details %}}

{{% details title="Hvad sker der med mit eksisterende bibliotek på den anden enhed?" closed="true" %}}
Gendannelse af en backup erstatter alle eksisterende musikbiblioteksdata, afspilningslister, indstillinger og albumcovers på den anden enhed. Lav en separat backup af den anden enhed først, hvis du vil bevare dens data.
{{% /details %}}

{{% details title="Fungerer denne proces mellem iPhone og Mac?" closed="true" %}}
Ja. Evermusic understøtter Wi-Fi Drive-overførsel mellem enhver kombination af iPhone, iPad og Mac. Begge enheder skal bare være på det samme Wi-Fi-netværk.
{{% /details %}}

{{% details title="Hvor lang tid tager overførslen?" closed="true" %}}
Overførselstiden afhænger af størrelsen på dit musikbibliotek og din Wi-Fi-hastighed. Et typisk bibliotek på et par gigabyte overføres på 5-15 minutter over et standard hjemmenetværk.
{{% /details %}}
