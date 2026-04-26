---
title: "Hoe M3U-afspeellijst importeren in Evermusic en Flacbox"
date: 2024-01-31
description: "Leer hoe u M3U-, M3U8- en CUE-afspeellijstbestanden importeert vanuit de cloud, lokale opslag of uw apparaat in Evermusic en Flacbox."
keywords: ["evermusic", "flacbox", "afspeellijst", "m3u", "m3u8", "cue", "importeren", "muziek app"]
tags: ["evermusic", "importeren", "afspeellijsten", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Samenvatting:** Evermusic en Flacbox ondersteunen het importeren van M3U-, M3U8- en CUE-afspeellijstbestanden vanuit cloudopslag, lokale app-bestanden of uw apparaat. Ga naar Afspeellijsten > Meer > Afspeellijst importeren, selecteer een bron, kies uw bestand en de app bouwt automatisch uw afspeellijst.

M3U, wat staat voor MP3 URL of Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, is een computerbestandsformaat dat wordt gebruikt voor multimedia-afspeellijsten. Een van de belangrijkste toepassingen is het maken van afspeellijstbestanden met één vermelding die verwijzen naar streams op internet. Deze bestanden bieden gemakkelijke toegang tot streamingcontent en worden vaak gebruikt voor downloads, e-mail en het luisteren naar internetradio.

Ondanks het wijdverbreide gebruik is er geen formele specificatie voor het M3U-formaat; het is een de facto standaard geworden. Een M3U-bestand is in wezen een platte-tekstbestand dat de locaties van een of meer mediabestanden specificeert. Afhankelijk van de codering wordt het opgeslagen met de bestandsextensie "m3u" of "m3u8". Elke vermelding in het bestand specificeert de locatie van een mediabestand, die een absoluut lokaal pad, een lokaal pad relatief ten opzichte van de M3U-bestandslocatie of een URL kan zijn. Vermeldingen worden gescheiden door regelafbrekingen, waarbij sommige apparaten regelafbrekingen vereisen die worden weergegeven als CR LF.

Daarnaast kunnen M3U-bestanden opmerkingen bevatten die worden voorafgegaan door het "#"-teken. In uitgebreid M3U introduceert "#" uitgebreide M3U-richtlijnen, die parameters kunnen ondersteunen die worden afgesloten met een dubbele punt ":".

In onze apps Evermusic en Flacbox hebben we M3U-bestandsimportfunctionaliteit geïmplementeerd, waardoor handmatig afspeellijsten aanmaken niet meer nodig is. Deze handleiding begeleidt u bij het importeren van uw afspeellijsten vanuit cloudopslag, lokale bestanden of bestanden op uw apparaat rechtstreeks in de app.

Navigeer eerst naar het gedeelte 'Afspeellijsten'. Tik vervolgens op de knop 'Meer' in de rechterbovenhoek. Selecteer in het menu dat verschijnt de optie 'Afspeellijst importeren'.

![afspeellijst importeren actie](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Kies op het volgende scherm de bestandslocatie. Ondersteunde opties zijn:

- Verbonden cloudopslag;
- Bestanden in de applicatie;
- Bestanden op uw apparaat;

![bestandslocatie selecteren](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Laten we verbonden cloudopslag selecteren en de map openen die het afspeellijstbestand bevat. Ondersteunde afspeellijstbestandsextensies zijn M3U, M3U8 en CUE. Selecteer het afspeellijstbestand en tik op 'Voltooid' om uw selectie te bevestigen.

![M3U-bestand selecteren](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

De app zal het afspeellijstbestand verwerken en een lijst met nummers maken. Vervolgens worden die bestanden op de opslag gevonden en wordt een definitieve afspeellijst samengesteld die in de muziekbibliotheek wordt geïmporteerd. Het is cruciaal dat uw M3U/CUE-bestand de juiste paden voor mediabestanden bevat en dat de bestanden zich op die paden op uw opslag bevinden.

![geïmporteerde afspeellijst](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

De app ondersteunt zowel relatieve paden als absolute bestands-URL's.

Bijvoorbeeld:

Afspeellijst met relatieve paden:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Afspeellijst met absolute URL's:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Als u een afspeellijstbestand importeert dat zich in de app bevindt (sectie Lokale bestanden), zijn er geen extra stappen nodig.

Als u echter een afspeellijst wilt importeren die zich op uw apparaat bevindt met de systeembestandskiezer, is er een belangrijk aandachtspunt.

Vanwege beveiligingsbeleid kan de applicatie alleen toegang krijgen tot het bestand dat u selecteert met de systeembestandskiezer. Het afspeellijstbestand kan echter links bevatten naar andere mediabestanden op uw apparaat. Om een afspeellijst van uw apparaat te importeren, moet u een map selecteren die zowel het afspeellijstbestand als alle gekoppelde mediabestanden bevat. In dit geval zal de app de geselecteerde map scannen, het afspeellijstbestand vinden, de tracklist opbouwen en deze in de muziekbibliotheek importeren.

Daarnaast kunt u meerdere afspeellijsten tegelijk importeren door op de knop "Meer acties" te tikken en "Afspeellijsten importeren vanuit een map" te selecteren. De app scant vervolgens de inhoud van de map, vindt ondersteunde afspeellijstbestanden en importeert ze in de bibliotheek.

## Veelgestelde vragen

{{% details title="Welke afspeellijstformaten ondersteunen Evermusic en Flacbox?" closed="true" %}}
Beide apps ondersteunen M3U-, M3U8- en CUE-afspeellijstbestandsformaten. Deze dekken de meest voorkomende afspeellijststandaarden die worden gebruikt door muziekspelers en mediasoftware.
{{% /details %}}

{{% details title="Kan ik afspeellijsten importeren vanuit cloudopslag?" closed="true" %}}
Ja. U kunt afspeellijstbestanden importeren vanuit elke verbonden cloudopslagdienst, waaronder Google Drive, Dropbox, OneDrive en WebDAV-servers.
{{% /details %}}

{{% details title="Waarom ontbreken er nummers na het importeren?" closed="true" %}}
Het afspeellijstbestand moet correcte paden naar uw mediabestanden bevatten en die bestanden moeten bestaan op de opgegeven locaties op uw opslag. Controleer nogmaals of de bestandspaden in uw M3U- of CUE-bestand overeenkomen met de werkelijke bestandslocaties.
{{% /details %}}

{{% details title="Kan ik meerdere afspeellijsten tegelijk importeren?" closed="true" %}}
Ja. Gebruik de knop Meer acties en selecteer "Afspeellijsten importeren vanuit een map." De app scant de map op alle ondersteunde afspeellijstbestanden en importeert ze in één stap.
{{% /details %}}

{{% details title="Moet ik handmatig afspeellijsten aanmaken?" closed="true" %}}
Nee. De importfunctie maakt handmatig afspeellijsten aanmaken overbodig. Wijs de app gewoon naar uw bestaande M3U-, M3U8- of CUE-bestand en de afspeellijst wordt automatisch opgebouwd.
{{% /details %}}
