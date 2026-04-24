---
title: "Bestanden overzetten van computer naar iPhone met het SMB-protocol"
description: "Leer hoe u grote bestanden kunt overzetten en openen van uw Mac of Windows PC naar uw iPhone of iPad met Evermusic en het SMB-protocol. Een stapsgewijze handleiding voor naadloze streaming en bestandsbeheer."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["bestanden overzetten naar iPhone SMB", "PC-muziek streamen op iPhone", "Mac verbinden met iPhone SMB", "Evermusic SMB-instelling", "computerbestanden openen iPhone", "Windows muziek delen iOS", "SMB-bestandsoverdracht Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Samenvatting:** Gebruik Evermusic op uw iPhone of iPad om bestanden te openen die zijn opgeslagen op uw Mac of Windows PC via uw lokale netwerk met SMB. Geen kabels, geen iTunes, geen cloud-upload nodig. Schakel bestandsdeling in op uw computer, maak verbinding in de app en blader of speel uw bestanden draadloos af.

Heeft u een uitgebreide verzameling grote bestanden op uw MAC of PC en wilt u deze moeiteloos openen vanaf uw iPhone of iPad? Onze apps bieden een eenvoudige oplossing.

Volg deze stappen om naadloze toegang mogelijk te maken tussen uw computer en iOS-apparaat met het SMB-protocol:

## Stap 1: SMB-protocol inschakelen op uw computer

**Voor MAC:**

1. Open "Systeemvoorkeuren" op uw MAC.
2. Klik op "Delen".
3. Schakel de service "Bestandsdeling" in.
4. Voeg uw muziekmap toe aan het gedeelte "Gedeelde mappen". Voeg een gebruiker toe en kies het machtigingsniveau (Lezen en schrijven of Alleen lezen). U kunt kiezen voor "Iedereen: Alleen lezen" voor de toegevoegde muziekmap.

   ![Mac-instellingenscherm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Onthoud de computer-URL (smb://192.168.xx.xx), want u zult deze in de volgende stappen gebruiken.
6. Klik op "Opties" en activeer "Bestanden en mappen delen via SMB".

   ![Mac-bestandsdeelscherm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Schakel "Windows-bestandsdeling" in voor beschikbare accounts.

   ![Mac SMB-deelscherm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Voor Windows PC:**

1. Klik met de rechtermuisknop op uw muziekmap.
2. Selecteer "Eigenschappen".
3. Ga naar het tabblad "Delen".
4. Klik op "Delen..."
5. Kies de personen met wie u de map wilt delen en geef het machtigingsniveau op. U kunt "Iedereen: Lezen" selecteren voor de gekozen muziekmap.

   ![Windows SMB-deelscherm](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Klik op "Voltooid".
7. Klik op "Voltooid" in het venster "Bestandsdeling" en onthoud het mappad.

   ![Windows SMB gedeelde map](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Stap 2: Uw iOS-apparaat verbinden

1. Open de app op uw iPhone of iPad.
2. Ga naar het tabblad "Verbindingen".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Evermusic Verbindingen-scherm"
  caption="Evermusic Verbindingen-scherm"
  width="400"
>}}

*Als uw computer verschijnt in het gedeelte "Beschikbare apparaten":*

Als uw computer zichtbaar is in het gedeelte "Beschikbare apparaten" en u "Iedereen: Alleen lezen" hebt geselecteerd in de vorige stap, tik dan gewoon op uw computer en deze wordt automatisch verbonden.

*Als uw computer niet automatisch verschijnt:*

1. Tik op "Verbind een cloudservice".
2. Selecteer "SMB" in het scherm "Verbind een cloudservice".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Evermusic Verbind een cloudservice-scherm"
  caption="Evermusic Verbind een cloudservice-scherm"
  width="400"
>}}

3. Voer in het scherm "SMB-verbinding" de server-URL in met het pad van de gedeelde map. U kunt de servernaam of het server-IP gebruiken:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Voer uw gebruikersnaam en wachtwoord in of laat deze velden leeg als u "Iedereen: Alleen lezen" hebt geselecteerd in de vorige stap.
5. Het veld "WORKGROUP" is optioneel en moet worden gebruikt als u een Active Directory Domain hebt.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Evermusic SMB-connectorscherm"
  caption="Evermusic SMB-connectorscherm"
  width="400"
>}}

6. Nadat u uw computer hebt verbonden via het SMB-protocol, verschijnt deze in het gedeelte "Cloudservices" van het scherm "Verbindingen".
7. Open de verbonden service en navigeer naar de gewenste map.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Geopende SMB-map in Evermusic"
  caption="Geopende SMB-map in Evermusic"
  width="400"
>}}

8. U kunt de ingebouwde bestandsbeheerder gebruiken om uw bestanden naar behoefte te bewerken.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Evermusic bestandsbeheerder"
  caption="Evermusic bestandsbeheerder"
  width="400"
>}}

## Stap 3: Oplossing voor SMB2-mappen met speciale tekens

Soms kunt u problemen ondervinden met mappen die speciale tekens bevatten bij gebruik van het SMB2-protocol. Hier zijn enkele stappen om dit probleem op te lossen:

1. **SMB 1 inschakelen:**  
   • Als tijdelijke oplossing kunt u SMB 1 inschakelen op uw server en in de app-instellingen. Dit kan helpen om de problemen met speciale tekens in mapnamen te omzeilen.

2. **Systeembestand openen-menu gebruiken:**  
   • Navigeer naar "Lokale bestanden".  
   • Scroll naar beneden naar het gedeelte "Bestanden op dit apparaat".  
   • Tik op "Bestanden openen..." of "Mappen openen...".  
   • Zoek uw server en selecteer de bestanden of mappen die u nodig hebt.  
   • Tik op "Openen" om uw selectie te bevestigen.

3. **Alternatieve protocollen:**  
   • Als het probleem aanhoudt, overweeg dan om verbinding te maken met uw NAS via WebDAV- of DLNA-protocollen als uw NAS deze opties ondersteunt. Deze protocollen kunnen beter omgaan met speciale tekens.

Door deze stappen te volgen, kunt u de problemen met speciale tekens in mapnamen bij gebruik van het SMB2-protocol verminderen.

## Conclusie

Met deze stappen kunt u moeiteloos uw uitgebreide verzameling bestanden van uw MAC of PC openen op uw iPhone of iPad met onze apps.

## Veelgestelde vragen

{{% details title="Kan ik bestanden op mijn PC openen vanaf mijn iPhone zonder iTunes?" closed="true" %}}
Ja. Evermusic maakt verbinding met uw computer via SMB op uw lokale Wi-Fi-netwerk. Geen iTunes- of Finder-synchronisatie nodig. Schakel bestandsdeling in op uw PC en maak rechtstreeks verbinding vanuit de app.
{{% /details %}}

{{% details title="Werkt SMB-bestandstoegang via internet?" closed="true" %}}
Nee. SMB is een lokaal netwerkprotocol. Uw iPhone en computer moeten op hetzelfde Wi-Fi-netwerk zijn. Voor externe toegang uploadt u bestanden naar een cloudservice zoals Google Drive of Dropbox en maakt u er verbinding mee in Evermusic.
{{% /details %}}

{{% details title="Welke bestandstypen kan ik openen via SMB?" closed="true" %}}
Evermusic ondersteunt MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC en andere audioformaten. U kunt ook niet-audiobestanden bladeren en beheren met de ingebouwde bestandsbeheerder.
{{% /details %}}

{{% details title="Kan ik bestanden van een NAS naar mijn iPhone overzetten via SMB?" closed="true" %}}
Ja. De meeste NAS-apparaten (Synology, QNAP, WD My Cloud en andere) ondersteunen SMB. Maak verbinding met uw NAS met dezelfde stappen in deze handleiding.
{{% /details %}}

{{% details title="Moet ik bestanden naar mijn iPhone kopiëren om ze af te spelen?" closed="true" %}}
Nee. Evermusic streamt bestanden rechtstreeks van uw computer of NAS via het netwerk. Bestanden worden niet naar uw iPhone gekopieerd tenzij u ervoor kiest ze te downloaden voor offline afspelen.
{{% /details %}}

{{% details title="Is SMB-bestandsdeling veilig?" closed="true" %}}
SMB-bestandsdeling werkt alleen op uw lokale netwerk. Andere apparaten op andere netwerken hebben geen toegang tot uw gedeelde mappen. Voor extra beveiliging gebruikt u een gebruikersnaam en wachtwoord in plaats van anonieme (Iedereen) toegang.
{{% /details %}}
