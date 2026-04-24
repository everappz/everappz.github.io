---
title: "Fájlok átvitele számítógépről iPhone-ra az SMB protokoll használatával"
description: "Ismerje meg, hogyan vihet át és érhet el nagy fájlokat Mac vagy Windows PC-ről iPhone-ra vagy iPadre az Evermusic és az SMB protokoll segítségével. Lépésről lépésre útmutató a zökkenőmentes streameléshez és fájlkezeléshez."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["fájlok átvitele iPhone-ra SMB", "PC zene streamelése iPhone-on", "Mac csatlakoztatása iPhone-hoz SMB", "Evermusic SMB beállítás", "számítógépes fájlok elérése iPhone", "Windows zene megosztás iOS", "SMB fájlátvitel Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Összefoglaló:** Használja az Evermusic-ot iPhone-ján vagy iPadjén a Mac-en vagy Windows PC-n tárolt fájlok eléréséhez a helyi hálózaton keresztül SMB-vel. Nincs szükség kábelekre, iTunes-ra vagy felhőbe feltöltésre. Engedélyezze a fájlmegosztást a számítógépén, csatlakozzon az alkalmazásban, és böngéssze vagy játssza le fájljait vezeték nélkül.

Van egy kiterjedt nagy fájlokból álló gyűjteménye a MAC-én vagy PC-jén, és könnyedén szeretné elérni azokat iPhone-járól vagy iPadjéről? Alkalmazásaink egyszerű megoldást kínálnak.

Kövesse ezeket a lépéseket a zökkenőmentes hozzáférés engedélyezéséhez számítógépe és iOS eszköze között az SMB protokoll használatával:

## 1. lépés: Az SMB protokoll engedélyezése a számítógépén

**MAC esetén:**

1. Nyissa meg a "Rendszerbeállítások"-at a MAC-én.
2. Kattintson a "Megosztás"-ra.
3. Engedélyezze a "Fájlmegosztás" szolgáltatást.
4. Adja hozzá zenei mappáját a "Megosztott mappák" szakaszhoz. Adjon hozzá egy felhasználót, és válassza ki a jogosultsági szintet (Olvasás és írás vagy Csak olvasás). Választhatja a "Mindenki: Csak olvasás" opciót a hozzáadott zenei mappához.

   ![Mac beállítások képernyő](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Jegyezze meg a számítógép URL-jét (smb://192.168.xx.xx), mivel a következő lépésekben fogja használni.
6. Kattintson az "Opciók"-ra, és aktiválja a "Fájlok és mappák megosztása SMB-n keresztül" opciót.

   ![Mac fájlmegosztás képernyő](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Engedélyezze a "Windows fájlmegosztás"-t az elérhető fiókokhoz.

   ![Mac SMB megosztás képernyő](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Windows PC esetén:**

1. Kattintson jobb gombbal a zenei mappájára.
2. Válassza a "Tulajdonságok"-at.
3. Navigáljon a "Megosztás" fülre.
4. Kattintson a "Megosztás..."-ra.
5. Válassza ki azokat a személyeket, akikkel meg szeretné osztani a mappát, és adja meg a jogosultsági szintet. Választhatja a "Mindenki: Olvasás" opciót a kiválasztott zenei mappához.

   ![Windows SMB megosztás képernyő](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Kattintson a "Kész"-re.
7. Kattintson a "Kész"-re a "Fájlmegosztás" ablakban, és jegyezze meg a mappa elérési útját.

   ![Windows SMB megosztott mappa](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## 2. lépés: iOS eszköz csatlakoztatása

1. Nyissa meg az alkalmazást iPhone-ján vagy iPadjén.
2. Lépjen a "Kapcsolatok" fülre.

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Evermusic Kapcsolatok képernyő"
  caption="Evermusic Kapcsolatok képernyő"
  width="400"
>}}

*Ha a számítógépe megjelenik az "Elérhető eszközök" szakaszban:*

Ha a számítógépe látható az "Elérhető eszközök" szakaszban, és az előző lépésben a "Mindenki: Csak olvasás" opciót választotta, egyszerűen koppintson a számítógépére, és automatikusan csatlakozik.

*Ha a számítógépe nem jelenik meg automatikusan:*

1. Koppintson a "Felhőszolgáltatás csatlakoztatása" lehetőségre.
2. Válassza az "SMB"-t a "Felhőszolgáltatás csatlakoztatása" képernyőn.

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Evermusic Felhőszolgáltatás csatlakoztatása képernyő"
  caption="Evermusic Felhőszolgáltatás csatlakoztatása képernyő"
  width="400"
>}}

3. Az "SMB csatlakozás" képernyőn adja meg a szerver URL-jét a megosztott mappa elérési útjával. Használhatja a szerver nevét vagy a szerver IP-címét:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Adja meg felhasználónevét és jelszavát, vagy hagyja üresen ezeket a mezőket, ha az előző lépésben a "Mindenki: Csak olvasás" opciót választotta.
5. A "WORKGROUP" mező opcionális, és akkor kell használni, ha Active Directory Domain-nel rendelkezik.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Evermusic SMB csatlakozó képernyő"
  caption="Evermusic SMB csatlakozó képernyő"
  width="400"
>}}

6. Miután csatlakoztatta számítógépét az SMB protokoll segítségével, megjelenik a "Felhőszolgáltatások" szakaszban a "Kapcsolatok" képernyőn.
7. Nyissa meg a csatlakoztatott szolgáltatást, és navigáljon a kívánt mappához.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Megnyitott SMB mappa az Evermusic-ban"
  caption="Megnyitott SMB mappa az Evermusic-ban"
  width="400"
>}}

8. A beépített fájlkezelővel szükség szerint szerkesztheti fájljait.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Evermusic fájlkezelő"
  caption="Evermusic fájlkezelő"
  width="400"
>}}

## 3. lépés: SMB2 mappák speciális karakterekkel - megoldás

Néha problémákba ütközhet speciális karaktereket tartalmazó mappákkal az SMB2 protokoll használatakor. Íme néhány lépés a probléma megoldásához:

1. **SMB 1 engedélyezése:**  
   • Átmeneti megoldásként próbálja meg engedélyezni az SMB 1-et a szerverén és az alkalmazás beállításaiban. Ez segíthet megkerülni a speciális karakterekkel kapcsolatos problémákat a mappanevekben.

2. **Rendszer fájlmegnyitó menü használata:**  
   • Navigáljon a "Helyi fájlok"-hoz.  
   • Görgessen le a "Fájlok ezen az eszközön" szakaszhoz.  
   • Koppintson a "Fájlok megnyitása..." vagy "Mappák megnyitása..." lehetőségre.  
   • Keresse meg a szerverét, és válassza ki a szükséges fájlokat vagy mappákat.  
   • Koppintson a "Megnyitás"-ra a választás megerősítéséhez.

3. **Alternatív protokollok:**  
   • Ha a probléma továbbra is fennáll, fontolja meg a NAS-hoz való csatlakozást WebDAV vagy DLNA protokollok használatával, ha a NAS-a támogatja ezeket az opciókat. Ezek a protokollok elegánsabban kezelhetik a speciális karaktereket.

Ezen lépések követésével enyhítheti a speciális karakterekkel kapcsolatos problémákat a mappanevekben az SMB2 protokoll használatakor.

## Összegzés

Ezekkel a lépésekkel könnyedén elérheti kiterjedt fájlgyűjteményét MAC-éről vagy PC-jéről iPhone-ján vagy iPadjén alkalmazásaink segítségével.

## Gyakran ismételt kérdések

{{% details title="Elérhetek fájlokat a PC-men az iPhone-omról iTunes nélkül?" closed="true" %}}
Igen. Az Evermusic SMB-n keresztül csatlakozik a számítógépéhez a helyi Wi-Fi hálózaton. Nincs szükség iTunes vagy Finder szinkronizálásra. Engedélyezze a fájlmegosztást a PC-jén, és csatlakozzon közvetlenül az alkalmazásból.
{{% /details %}}

{{% details title="Működik az SMB fájl-hozzáférés az interneten keresztül?" closed="true" %}}
Nem. Az SMB helyi hálózati protokoll. Az iPhone-jának és számítógépének ugyanazon a Wi-Fi hálózaton kell lennie. Távoli hozzáféréshez töltse fel fájljait egy felhőszolgáltatásba, mint a Google Drive vagy Dropbox, és csatlakozzon hozzá az Evermusic-ban.
{{% /details %}}

{{% details title="Milyen fájltípusokat érhetek el SMB-n keresztül?" closed="true" %}}
Az Evermusic támogatja az MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC és más hangformátumokat. A beépített fájlkezelővel nem hang fájlokat is böngészhet és kezelhet.
{{% /details %}}

{{% details title="Átvihetek fájlokat NAS-ról iPhone-ra SMB-vel?" closed="true" %}}
Igen. A legtöbb NAS eszköz (Synology, QNAP, WD My Cloud és mások) támogatja az SMB-t. Csatlakozzon NAS-ához ugyanazokkal a lépésekkel ebben az útmutatóban.
{{% /details %}}

{{% details title="Át kell másolnom a fájlokat az iPhone-ra a lejátszáshoz?" closed="true" %}}
Nem. Az Evermusic közvetlenül a számítógépéről vagy NAS-áról streameli a fájlokat a hálózaton keresztül. A fájlok nem másolódnak az iPhone-ra, hacsak nem választja a letöltésüket offline lejátszáshoz.
{{% /details %}}

{{% details title="Biztonságos az SMB fájlmegosztás?" closed="true" %}}
Az SMB fájlmegosztás csak a helyi hálózatán működik. Más hálózatokon lévő eszközök nem férhetnek hozzá a megosztott mappáihoz. További biztonság érdekében használjon felhasználónevet és jelszót az anonim (Mindenki) hozzáférés helyett.
{{% /details %}}
