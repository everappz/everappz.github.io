---
title: "Hur du överför ditt musikbibliotek mellan enheter i Evermusic: steg-för-steg-guide"
description: "Överför enkelt ditt Evermusic-musikbibliotek, spellistor, albumomslag och inställningar från en iPhone, iPad eller Mac till en annan med Wi-Fi Drive och säkerhetskopieringsverktyg."
date: 2024-12-29
tags: ["musikbibliotek", "överföring", "wifi", "säkerhetskopia", "webdav", "återställning"]
keywords: ["överföra musikbibliotek Evermusic", "säkerhetskopiera och återställa spellistor Evermusic", "Evermusic WiFi Drive", "synkronisera Evermusic mellan enheter", "flytta Evermusic-databas", "Evermusic filöverföring", "återställa ljudspelarinställningar", "WebDAV musiköverföring iOS"]
readingTime: 3
---

{{< author-byline >}}


**Sammanfattning:** För att överföra ditt Evermusic-bibliotek till en ny enhet, skapa en säkerhetskopia på källenheten, starta Wi-Fi Drive, anslut den andra enheten via samma nätverk, ladda ner säkerhetskopian och musikfilerna och återställ sedan från säkerhetskopian. Hela processen tar cirka 10 minuter beroende på bibliotekets storlek.

I denna guide vägleder vi dig genom överföringen av hela ditt musikbibliotek — inklusive databas, albumomslag och inställningar — från en enhet (iPhone eller Mac) till en annan. Även om automatisk synkronisering av musikbibliotek och spellistor är en funktion som planeras för framtiden, måste denna process för närvarande göras manuellt.

## Steg 1: Skapa en säkerhetskopia på den första enheten

1. **Öppna appen på din första enhet** (den med ditt musikbibliotek, spellistor och anslutna molntjänster).
2. **Navigera till Inställningar** och välj alternativet **Säkerhetskopiering och Återställning**.

![Backup and Restore](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. På skärmen **Säkerhetskopiering och Återställning** väljer du vilka objekt som ska inkluderas i säkerhetskopian:
   - **Databas** (inkluderar ditt musikbibliotek och spellistor)
   - **Albumomslag**
   - **Inställningar**

Dessa alternativ är aktiverade som standard.

![Backup Options](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Tryck på **Säkerhetskopiera applikationsdata** för att starta processen.

![Backup Application Data](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. När säkerhetskopieringen är klar visas en informationsvarning.

![Backup Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Tryck på **Visa fil** för att visa säkerhetskopian i katalogen **Dokument**. Säkerhetskopior sparas vanligtvis i mappen **Backup**.

![Show Backup File](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Steg 2: Starta Wi-Fi Drive-servern

1. Gå till avsnittet **Anslutningar** i appen.
2. Bläddra ner till **Anslut via Wi-Fi** och tryck på den.

![Connect Using Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. På nästa skärm trycker du på **Starta Wi-Fi Drive**.

- Valfritt kan du ange ett användarnamn och lösenord för säkerhet, men detta är onödigt för hemnätverk.

4. När den har startats ser du tillgängliga serveradresser. Dessa kan användas för webbläsare på datorer eller WebDAV-appar, men i denna guide går vi direkt vidare till nästa steg.

![Wi-Fi Drive Started](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Steg 3: Anslut din andra enhet till den första

1. Öppna appen på din andra enhet (dit du vill överföra biblioteket).
2. Se till att båda enheterna är anslutna till samma Wi-Fi-nätverk.
3. På den andra enheten öppnar du fliken **Anslutningar** och väljer **Tillgängliga enheter**.

![Available Devices](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Du bör se en WebDAV-anslutning med namnet **Evermusic** (servern vi startade på den första enheten). Tryck på den för att ansluta.

5. När du är ansluten ser du alla mappar från den första enheten.

![Connected to First Device](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Steg 4: Förbered för filöverföring

1. På den andra enheten går du till **Inställningar > Filhanterare** och aktiverar **Spara nedladdade filer till - Fråga varje gång**.

- Detta säkerställer att du kan välja målmapp för varje nedladdning.

2. Gå tillbaka till fliken **Anslutningar** och navigera till den anslutna WebDAV-servern.

![Prepare for File Transfers](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Steg 5: Överför säkerhetskopia och musikfiler

1. Öppna mappen **Backup** på den anslutna WebDAV-servern.

![Backup Folder](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Tryck på knappen **Fler åtgärder** (tre prickar) bredvid säkerhetskopian och välj **Ladda ner**.

3. Skapa en **Backup**-mapp på den andra enheten för att lagra de nedladdade filerna. Bekräfta ditt val genom att trycka på **Färdig**.

![Download Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Överför eventuella ytterligare musikfiler:
   - Kontrollera mappen **Ladda ner** eller andra relevanta mappar på WebDAV-servern.

![Transfer Music Files](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Använd alternativet **Välja** för att välja filer och tryck sedan på **Fler åtgärder > Ladda ner**. Spara dem i motsvarande mapp på den andra enheten för att bibehålla samma mappstruktur.

Målet är att överföra alla filer från din första enhet till din nuvarande enhet och säkerställa att mappstrukturen förblir identisk. På så sätt förblir länkarna i ditt musikbibliotek och spellistor intakta. Observera att lokala filer som lagras utanför appens Dokument-katalog på din första enhet måste överföras separat. Eftersom appen inte kan komma åt dessa filer i Wi-Fi Drive-läge måste du använda appen Systemfiler för överföringen.

![Transfer Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Steg 6: Övervaka överföringsförloppet

1. På den andra enheten går du till avsnittet **Lokala filer** (eller fliken **Ladda ner** på iPad/Mac).

2. Tryck på knappen **Överföringsaktivitet** i det övre vänstra hörnet för att övervaka överföringskön.

![Monitor Transfer](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Steg 7: Återställ data från säkerhetskopia

1. När säkerhetskopian och alla nödvändiga ljudfiler har laddats ner till den andra enheten öppnar du mappen **Backup**.

2. Tryck på säkerhetskopian och ett bekräftelsemeddelande visas.

![Restore Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Obs:** Återställning ersätter all aktuell musikbiblioteksdata, spellistor, inställningar och albumomslag med säkerhetskopians data.

3. Tryck på **Återställ** för att starta processen.

![Restore Process](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Efter att återställningen är klar bekräftar en varning att det lyckades.

![Restoration Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Kontrollera avsnitten **Spellistor** eller **Musikbibliotek** för att verifiera återställningen.

![Verify Restoration](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Steg 8: Indexera om musikbiblioteket

1. För bästa resultat, indexera om ditt bibliotek för att säkerställa att alla filer har upptäckts framgångsrikt.

2. Gå till **Inställningar > Musikbibliotek > Offline musiksynkronisering** och välj **Starta skanning av lokala mappar**.

Genom att följa dessa steg överför du framgångsrikt ditt musikbibliotek, spellistor och inställningar till en annan enhet. Om du stöter på problem, tveka inte att kontakta supporten.

## Vanliga frågor

{{% details title="Kan jag överföra mitt Evermusic-bibliotek utan Wi-Fi?" closed="true" %}}
Wi-Fi Drive kräver att båda enheterna är på samma Wi-Fi-nätverk. Det finns för närvarande inget Bluetooth- eller mobilöverföringsalternativ. Du kan alternativt använda AirDrop eller appen Filer för att manuellt flytta säkerhetskopian och musikmapparna mellan enheter.
{{% /details %}}

{{% details title="Överförs mina molntjänstanslutningar med säkerhetskopian?" closed="true" %}}
Säkerhetskopian inkluderar din databas, spellistor, albumomslag och inställningar. Inloggningsuppgifter för molntjänster inkluderas inte av säkerhetsskäl. Du behöver återansluta dina molnkonton på den nya enheten efter återställningen.
{{% /details %}}

{{% details title="Vad händer med mitt befintliga bibliotek på den andra enheten?" closed="true" %}}
Att återställa en säkerhetskopia ersätter all befintlig musikbiblioteksdata, spellistor, inställningar och albumomslag på den andra enheten. Gör en separat säkerhetskopia av den andra enheten först om du vill bevara dess data.
{{% /details %}}

{{% details title="Fungerar denna process mellan iPhone och Mac?" closed="true" %}}
Ja. Evermusic stöder Wi-Fi Drive-överföring mellan alla kombinationer av iPhone, iPad och Mac. Båda enheterna behöver bara vara på samma Wi-Fi-nätverk.
{{% /details %}}

{{% details title="Hur lång tid tar överföringen?" closed="true" %}}
Överföringstiden beror på storleken på ditt musikbibliotek och din Wi-Fi-hastighet. Ett typiskt bibliotek på några gigabyte överförs på 5-15 minuter över ett vanligt hemnätverk.
{{% /details %}}
