---
title: "Ako preniesť hudobnú knižnicu medzi zariadeniami v Evermusic: sprievodca krok za krokom"
description: "Jednoducho preneste svoju hudobnú knižnicu Evermusic, prehrávače, obaly albumov a nastavenia z jedného iPhonu, iPadu alebo Macu na iný pomocou Wi-Fi Drive a nástrojov zálohovania."
date: 2024-12-29
tags: ["hudobnakniznica", "prenos", "wifi", "zaloha", "webdav", "obnovenie"]
keywords: ["prenos hudobnej knižnice Evermusic", "zálohovanie a obnovenie prehrávačov Evermusic", "Evermusic WiFi Drive", "synchronizácia Evermusic medzi zariadeniami", "presun databázy Evermusic", "prenos súborov Evermusic", "obnovenie nastavení audio prehrávača", "WebDAV prenos hudby iOS"]
readingTime: 3
---

{{< author-byline >}}


**Zhrnutie:** Na prenos knižnice Evermusic na nové zariadenie vytvorte zálohu na zdrojovom zariadení, spustite Wi-Fi Drive, pripojte druhé zariadenie cez rovnakú sieť, stiahnite zálohu a hudobné súbory a potom obnovte zo zálohy. Celý proces trvá približne 10 minút v závislosti od veľkosti knižnice.

V tomto sprievodcovi vás prevedieme prenosom celej hudobnej knižnice — vrátane databázy, obalov albumov a nastavení — z jedného zariadenia (iPhone alebo Mac) na druhé. Automatická synchronizácia hudobnej knižnice a prehrávačov je funkcia plánovaná do budúcnosti, ale v súčasnosti sa tento proces musí vykonávať manuálne.

## Krok 1: Vytvorte zálohu na prvom zariadení

1. **Otvorte aplikáciu na prvom zariadení** (to s hudobnou knižnicou, prehrávačmi a pripojenými cloudovými službami).
2. **Prejdite do Nastavenia** a vyberte možnosť **Zálohovanie a Obnovenie**.

![Backup and Restore](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. Na obrazovke **Zálohovanie a Obnovenie** vyberte položky, ktoré chcete zahrnúť do záložného súboru:
   - **Databáza** (zahŕňa hudobnú knižnicu a prehrávače)
   - **Obaly albumov**
   - **Nastavenia**

Tieto možnosti sú predvolene zapnuté.

![Backup Options](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Ťuknite na **Zálohovať údaje aplikácie** a spustite proces.

![Backup Application Data](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Po dokončení zálohovania sa zobrazí informačné upozornenie.

![Backup Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Ťuknite na **Zobraziť súbor**, čím zobrazíte záložný súbor v adresári **Dokumenty**. Záložné súbory sa zvyčajne ukladajú do priečinka **Backup**.

![Show Backup File](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Krok 2: Spustite server Wi-Fi Drive

1. Prejdite do sekcie **Pripojenia** v aplikácii.
2. Prejdite nadol na **Pripojenie cez Wi-Fi** a ťuknite naň.

![Connect Using Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. Na ďalšej obrazovke ťuknite na **Spustiť Wi-Fi Drive**.

- Voliteľne môžete nastaviť prihlasovacie meno a heslo pre bezpečnosť, ale pre domáce siete to nie je potrebné.

4. Po spustení uvidíte dostupné adresy servera. Tie sa dajú použiť pre prehliadače na počítači alebo WebDAV aplikácie, ale v tomto sprievodcovi prejdeme priamo na ďalšie kroky.

![Wi-Fi Drive Started](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Krok 3: Pripojte druhé zariadenie k prvému

1. Otvorte aplikáciu na druhom zariadení (kam chcete preniesť knižnicu).
2. Uistite sa, že obe zariadenia sú pripojené k rovnakej Wi-Fi sieti.
3. Na druhom zariadení otvorte kartu **Pripojenia** a vyberte **Dostupné zariadenia**.

![Available Devices](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Mali by ste vidieť WebDAV pripojenie s názvom **Evermusic** (server, ktorý sme spustili na prvom zariadení). Ťuknite naň pre pripojenie.

5. Po pripojení uvidíte všetky priečinky z prvého zariadenia.

![Connected to First Device](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Krok 4: Príprava na prenos súborov

1. Na druhom zariadení prejdite do **Nastavenia > Správca súborov** a zapnite **Uložiť stiahnuté súbory do - Pýtať sa zakaždým**.

- Toto zaistí, že si môžete vybrať cieľový priečinok pre každé stiahnutie.

2. Vráťte sa na kartu **Pripojenia** a prejdite na pripojený WebDAV server.

![Prepare for File Transfers](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Krok 5: Preneste zálohu a hudobné súbory

1. Otvorte priečinok **Backup** na pripojenom WebDAV serveri.

![Backup Folder](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Ťuknite na tlačidlo **Viac akcií** (tri bodky) vedľa záložného súboru a vyberte **Stiahnuť**.

3. Vytvorte priečinok **Backup** na druhom zariadení na uloženie stiahnutých súborov. Potvrďte výber ťuknutím na **Hotovo**.

![Download Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Preneste ďalšie hudobné súbory:
   - Skontrolujte priečinok **Stiahnuť** alebo iné relevantné priečinky na WebDAV serveri.

![Transfer Music Files](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Použite možnosť **Vybrať** na výber súborov, potom ťuknite na **Viac akcií > Stiahnuť**. Uložte ich do zodpovedajúceho priečinka na druhom zariadení, aby ste zachovali rovnakú štruktúru adresárov.

Cieľom je preniesť všetky súbory z prvého zariadenia na aktuálne zariadenie, pričom sa zabezpečí, že štruktúra priečinkov zostane identická. Takto zostanú odkazy v hudobnej knižnici a prehrávačoch neporušené. Upozorňujeme, že lokálne súbory uložené mimo adresár Dokumenty aplikácie na prvom zariadení sa musia preniesť samostatne. Keďže aplikácia nemá prístup k týmto súborom v režime Wi-Fi Drive, na ich prenos budete musieť použiť aplikáciu Systémové súbory.

![Transfer Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Krok 6: Sledujte priebeh prenosu

1. Na druhom zariadení prejdite do sekcie **Lokálne súbory** (alebo karty **Stiahnuť** na iPade/Macu).

2. Ťuknite na tlačidlo **Aktivita prenosu** v ľavom hornom rohu na sledovanie fronty prenosu.

![Monitor Transfer](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Krok 7: Obnovte údaje zo zálohy

1. Po stiahnutí záložného súboru a všetkých potrebných audio súborov na druhé zariadenie otvorte priečinok **Backup**.

2. Ťuknite na záložný súbor a zobrazí sa potvrdzovacia správa.

![Restore Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Poznámka:** Obnovenie nahradí všetky aktuálne údaje hudobnej knižnice, prehrávače, nastavenia a obaly albumov údajmi zo zálohy.

3. Ťuknite na **Obnoviť** a spustite proces.

![Restore Process](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Po dokončení obnovenia upozornenie potvrdí úspech.

![Restoration Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Skontrolujte sekcie **Prehrávače** alebo **Hudobná knižnica** na overenie obnovenia.

![Verify Restoration](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Krok 8: Preindexujte hudobnú knižnicu

1. Pre najlepšie výsledky preindexujte knižnicu, aby ste sa uistili, že všetky súbory boli úspešne zistené.

2. Prejdite do **Nastavenia > Hudobná knižnica > Synchronizácia offline hudby** a vyberte **Spustiť skenovanie lokálnych priečinkov**.

Podľa týchto krokov úspešne prenesiete hudobnú knižnicu, prehrávače a nastavenia na iné zariadenie. Ak narazíte na akékoľvek problémy, neváhajte sa obrátiť na podporu.

## Často kladené otázky

{{% details title="Môžem preniesť knižnicu Evermusic bez Wi-Fi?" closed="true" %}}
Wi-Fi Drive vyžaduje, aby obe zariadenia boli na rovnakej Wi-Fi sieti. V súčasnosti nie je k dispozícii možnosť prenosu cez Bluetooth alebo mobilnú sieť. Alternatívne môžete použiť AirDrop alebo aplikáciu Súbory na manuálny prenos záložného súboru a hudobných priečinkov medzi zariadeniami.
{{% /details %}}

{{% details title="Prenesú sa pripojenia ku cloudovým službám so zálohou?" closed="true" %}}
Záloha zahŕňa databázu, prehrávače, obaly albumov a nastavenia. Prihlasovacie údaje cloudových služieb nie sú zahrnuté z bezpečnostných dôvodov. Po obnovení budete musieť znova pripojiť cloudové účty na novom zariadení.
{{% /details %}}

{{% details title="Čo sa stane s existujúcou knižnicou na druhom zariadení?" closed="true" %}}
Obnovenie zálohy nahradí všetky existujúce údaje hudobnej knižnice, prehrávače, nastavenia a obaly albumov na druhom zariadení. Ak chcete zachovať údaje druhého zariadenia, najskôr vytvorte samostatnú zálohu.
{{% /details %}}

{{% details title="Funguje tento proces medzi iPhonom a Macom?" closed="true" %}}
Áno. Evermusic podporuje prenos cez Wi-Fi Drive medzi akoukoľvek kombináciou iPhonu, iPadu a Macu. Obe zariadenia musia byť na rovnakej Wi-Fi sieti.
{{% /details %}}

{{% details title="Ako dlho trvá prenos?" closed="true" %}}
Čas prenosu závisí od veľkosti hudobnej knižnice a rýchlosti Wi-Fi. Typická knižnica s niekoľkými gigabajtmi sa prenesie za 5-15 minút cez štandardnú domácu sieť.
{{% /details %}}
