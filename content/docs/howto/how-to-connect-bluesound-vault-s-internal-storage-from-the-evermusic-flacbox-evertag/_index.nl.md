---
title: "Hoe de interne opslag van Bluesound VAULT te verbinden vanuit Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Leer hoe u toegang krijgt tot de interne harde schijf van Bluesound VAULT vanuit Evermusic, Flacbox en Evertag met het SMB-protocol om audiobestanden te beheren, bewerken en afspelen."
keywords: ["bluesound vault", "smb-opslag verbinden", "evermusic smb", "flacbox vault", "evertag smb", "nas-opslag muziek", "vault intern station"]
tags: ["evermusic", "verbinden", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Samenvatting:** Maak verbinding met de interne opslag van uw Bluesound VAULT via SMB met Evermusic, Flacbox of Evertag. Zoek het IP-adres van de VAULT in de BluOS-app, voer het in als een SMB-verbinding met gasttoegang en begin met het afspelen of beheren van uw muziekbestanden.

De Bluesound VAULT heeft een interne harde schijf en fungeert als een Network Attached Storage (NAS). Toegang tot de interne harde schijf van de VAULT stelt u in staat bestanden toe te voegen/te verwijderen en metadata-tags te bewerken vanuit onze apps Evermusic, Flacbox, Evertag.

**Hieronder volgen de stappen om toegang te krijgen tot de interne harde schijf van uw VAULT:**

1. Selecteer in de BluOS-app **Help > Diagnostiek**.

2. Verkrijg op de pagina **Diagnostiek** het **IP-adres** van de VAULT. Dit **IP-adres** wordt in de volgende stappen gebruikt.

3. Open Evermusic, Flacbox of Evertag.

   ![Everappz-applicaties](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Open het scherm "Verbindingen" en selecteer het menu-item "Een cloudservice verbinden".

   ![Evermusic Verbindingen-scherm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Selecteer de "SMB"-cloudservice.

   ![Evermusic Cloudservice Verbinden-scherm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Voer op het "SMB-configuratiescherm" de URL in het volgende formaat in:

   ```
   SMB://<<VAULT-IP>>
   ```

   Vervang `<<VAULT-IP>>` door het **IP-adres** verkregen in Stap 2.

   **Opmerking:** Laat de velden Inloggen en Wachtwoord leeg omdat de VAULT-opslag de GAST-modus ondersteunt.

   ![Evermusic SMB-verbindingsscherm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Tik op de knop "Aanmelden" om de configuratie op te slaan.

8. Open de verbonden cloudopslag, navigeer naar de map met audiobestanden en tik op een willekeurig bestand om de audiospeler te starten.

   ![Evermusic Geopende SMB-server-scherm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. U kunt ook bestanden bewerken met de ingebouwde bestandsbeheerder.

   ![Evermusic Bestandsbeheerder-scherm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Met deze eenvoudige stappen kunt u moeiteloos toegang krijgen tot de interne harde schijf van uw Bluesound VAULT en de controle over uw muziekbibliotheek overnemen met Evermusic, Flacbox of Evertag.

## Veelgestelde vragen

{{% details title="Heb ik een gebruikersnaam en wachtwoord nodig om verbinding te maken met Bluesound VAULT?" closed="true" %}}
Nee. Bluesound VAULT ondersteunt gasttoegang (anoniem) via SMB. Laat de velden Inloggen en Wachtwoord leeg bij het configureren van de verbinding.
{{% /details %}}

{{% details title="Kan ik muziektags op de Bluesound VAULT bewerken?" closed="true" %}}
Ja. Met Evertag kunt u metadata-tags (titel, artiest, album, enz.) bewerken voor audiobestanden die rechtstreeks op de interne harde schijf van de VAULT zijn opgeslagen.
{{% /details %}}

{{% details title="Welke protocollen ondersteunt de Bluesound VAULT?" closed="true" %}}
De Bluesound VAULT stelt zijn interne opslag beschikbaar via SMB (Server Message Block). Evermusic, Flacbox en Evertag ondersteunen allemaal SMB-verbindingen, waardoor het eenvoudig is om verbinding te maken.
{{% /details %}}

{{% details title="Kan ik muziek streamen vanaf de VAULT zonder bestanden naar mijn iPhone te kopiëren?" closed="true" %}}
Ja. Zodra u via SMB bent verbonden, kunt u audiobestanden rechtstreeks vanaf het interne station van de VAULT streamen zonder ze naar uw apparaat te kopiëren.
{{% /details %}}
