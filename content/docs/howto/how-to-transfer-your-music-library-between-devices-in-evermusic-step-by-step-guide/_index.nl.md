---
title: "Hoe u uw muziekbibliotheek tussen apparaten overzet in Evermusic: stapsgewijze handleiding"
description: "Zet eenvoudig uw Evermusic-muziekbibliotheek, afspeellijsten, albumhoezen en instellingen over van de ene iPhone, iPad of Mac naar een andere met Wi-Fi Drive en back-uptools."
date: 2024-12-29
tags: ["muziekbibliotheek", "overdracht", "wifi", "back-up", "webdav", "herstel"]
keywords: ["muziekbibliotheek overzetten Evermusic", "back-up en herstel afspeellijsten Evermusic", "Evermusic WiFi Drive", "Evermusic synchroniseren tussen apparaten", "Evermusic database verplaatsen", "Evermusic bestandsoverdracht", "audiospeler instellingen herstellen", "WebDAV muziekoverdracht iOS"]
readingTime: 3
---

{{< author-byline >}}


**Samenvatting:** Om uw Evermusic-bibliotheek naar een nieuw apparaat over te zetten, maakt u een back-up op het bronapparaat, start u Wi-Fi Drive, verbindt u het tweede apparaat via hetzelfde netwerk, downloadt u de back-up en muziekbestanden en herstelt u vervolgens vanuit de back-up. Het hele proces duurt ongeveer 10 minuten, afhankelijk van de grootte van de bibliotheek.

In deze handleiding begeleiden we u bij het overzetten van uw volledige muziekbibliotheek — inclusief database, albumhoezen en instellingen — van het ene apparaat (iPhone of Mac) naar het andere. Hoewel automatische synchronisatie van muziekbibliotheek en afspeellijsten een functie is die voor de toekomst gepland is, moet dit proces momenteel handmatig worden uitgevoerd.

## Stap 1: Maak een back-up op het eerste apparaat

1. **Open de app op uw eerste apparaat** (het apparaat met uw muziekbibliotheek, afspeellijsten en verbonden cloudservices).
2. **Navigeer naar Instellingen** en selecteer de optie **Back-up en Herstel**.

![Backup and Restore](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. Op het scherm **Back-up en Herstel** kiest u de items die in uw back-upbestand moeten worden opgenomen:
   - **Database** (bevat uw muziekbibliotheek en afspeellijsten)
   - **Albumhoezen**
   - **Instellingen**

Deze opties zijn standaard ingeschakeld.

![Backup Options](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Tik op **Back-up applicatiegegevens** om het proces te starten.

![Backup Application Data](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Zodra de back-up voltooid is, verschijnt er een informatiemelding.

![Backup Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Tik op **Bestand tonen** om het back-upbestand in de map **Documenten** te onthullen. Back-upbestanden worden doorgaans opgeslagen in de map **Backup**.

![Show Backup File](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Stap 2: Start de Wi-Fi Drive-server

1. Ga naar het gedeelte **Verbindingen** in de app.
2. Scroll naar beneden naar **Verbinden via Wi-Fi** en tik erop.

![Connect Using Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. Tik op het volgende scherm op **Wi-Fi Drive starten**.

- Optioneel kunt u een gebruikersnaam en wachtwoord instellen voor beveiliging, maar dit is niet nodig voor thuisnetwerken.

4. Eenmaal gestart, ziet u de beschikbare serveradressen. Dit kan worden gebruikt voor desktopbrowsers of WebDAV-apps, maar in deze handleiding gaan we direct door naar de volgende stappen.

![Wi-Fi Drive Started](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Stap 3: Verbind uw tweede apparaat met het eerste

1. Open de app op uw tweede apparaat (waar u de bibliotheek naartoe wilt overzetten).
2. Zorg ervoor dat beide apparaten verbonden zijn met hetzelfde Wi-Fi-netwerk.
3. Open op het tweede apparaat het tabblad **Verbindingen** en selecteer **Beschikbare apparaten**.

![Available Devices](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. U zou een WebDAV-verbinding moeten zien met de naam **Evermusic** (de server die we op het eerste apparaat hebben gestart). Tik erop om te verbinden.

5. Eenmaal verbonden, ziet u alle mappen van het eerste apparaat.

![Connected to First Device](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Stap 4: Voorbereiden op bestandsoverdracht

1. Ga op het tweede apparaat naar **Instellingen > Bestandsbeheer** en schakel **Gedownloade bestanden opslaan naar - Elke keer vragen** in.

- Dit zorgt ervoor dat u de doelmap voor elke download kunt selecteren.

2. Ga terug naar het tabblad **Verbindingen** en navigeer naar de verbonden WebDAV-server.

![Prepare for File Transfers](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Stap 5: Back-up en muziekbestanden overzetten

1. Open de map **Backup** op de verbonden WebDAV-server.

![Backup Folder](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Tik op de knop **Meer acties** (drie puntjes) naast het back-upbestand en selecteer **Downloaden**.

3. Maak een map **Backup** aan op het tweede apparaat om de gedownloade bestanden op te slaan. Bevestig uw selectie door op **Voltooid** te tikken.

![Download Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Zet eventuele extra muziekbestanden over:
   - Controleer de map **Downloads** of andere relevante mappen op de WebDAV-server.

![Transfer Music Files](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Gebruik de optie **Selecteren** om bestanden te kiezen en tik vervolgens op **Meer acties > Downloaden**. Sla ze op in de overeenkomstige map op het tweede apparaat om dezelfde mapstructuur te behouden.

Het doel is om alle bestanden van uw eerste apparaat naar uw huidige apparaat over te zetten, waarbij de mapstructuur identiek blijft. Op deze manier blijven de koppelingen in uw muziekbibliotheek en afspeellijsten intact. Let op: lokale bestanden die buiten de Documenten-map van de app op uw eerste apparaat zijn opgeslagen, moeten apart worden overgezet. Aangezien de app deze bestanden niet kan benaderen in Wi-Fi Drive-modus, moet u de Systeem Bestanden-app gebruiken voor de overdracht.

![Transfer Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Stap 6: Bewaak de voortgang van de overdracht

1. Ga op het tweede apparaat naar het gedeelte **Lokale bestanden** (of het tabblad **Downloads** op iPad/Mac).

2. Tik op de knop **Overdrachtsactiviteit** in de linkerbovenhoek om de overdrachtswachtrij te bewaken.

![Monitor Transfer](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Stap 7: Gegevens herstellen vanuit back-up

1. Zodra het back-upbestand en alle benodigde audiobestanden naar het tweede apparaat zijn gedownload, opent u de map **Backup**.

2. Tik op het back-upbestand en er verschijnt een bevestigingsbericht.

![Restore Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Let op:** Herstellen vervangt alle huidige muziekbibliotheekgegevens, afspeellijsten, instellingen en albumhoezen door de back-upgegevens.

3. Tik op **Herstellen** om het proces te starten.

![Restore Process](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Nadat het herstel is voltooid, bevestigt een melding het succes.

![Restoration Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Controleer de secties **Afspeellijsten** of **Muziekbibliotheek** om het herstel te verifiëren.

![Verify Restoration](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Stap 8: Herindexeer de muziekbibliotheek

1. Voor de beste resultaten herindexeert u uw bibliotheek om ervoor te zorgen dat alle bestanden succesvol worden gedetecteerd.

2. Ga naar **Instellingen > Muziekbibliotheek > Offline muziek synchronisatie** en selecteer **Lokale mappen scannen starten**.

Door deze stappen te volgen, zet u met succes uw muziekbibliotheek, afspeellijsten en instellingen over naar een ander apparaat. Als u problemen ondervindt, aarzel dan niet om contact op te nemen met de ondersteuning.

## Veelgestelde vragen

{{% details title="Kan ik mijn Evermusic-bibliotheek overzetten zonder Wi-Fi?" closed="true" %}}
Wi-Fi Drive vereist dat beide apparaten op hetzelfde Wi-Fi-netwerk zitten. Er is momenteel geen Bluetooth- of mobiele overdrachtsoptie. U kunt als alternatief AirDrop of de Bestanden-app gebruiken om het back-upbestand en de muziekmappen handmatig tussen apparaten te verplaatsen.
{{% /details %}}

{{% details title="Worden mijn cloudserviceverbindingen mee overgezet met de back-up?" closed="true" %}}
De back-up bevat uw database, afspeellijsten, albumhoezen en instellingen. Inloggegevens voor cloudservices worden om veiligheidsredenen niet meegenomen. U moet uw cloudaccounts opnieuw verbinden op het nieuwe apparaat na het herstellen.
{{% /details %}}

{{% details title="Wat gebeurt er met mijn bestaande bibliotheek op het tweede apparaat?" closed="true" %}}
Het herstellen van een back-up vervangt alle bestaande muziekbibliotheekgegevens, afspeellijsten, instellingen en albumhoezen op het tweede apparaat. Maak eerst een aparte back-up van het tweede apparaat als u de gegevens wilt bewaren.
{{% /details %}}

{{% details title="Werkt dit proces tussen iPhone en Mac?" closed="true" %}}
Ja. Evermusic ondersteunt Wi-Fi Drive-overdracht tussen elke combinatie van iPhone, iPad en Mac. Beide apparaten hoeven alleen op hetzelfde Wi-Fi-netwerk te zitten.
{{% /details %}}

{{% details title="Hoe lang duurt de overdracht?" closed="true" %}}
De overdrachtstijd hangt af van de grootte van uw muziekbibliotheek en uw Wi-Fi-snelheid. Een typische bibliotheek van enkele gigabytes wordt in 5-15 minuten overgezet via een standaard thuisnetwerk.
{{% /details %}}
