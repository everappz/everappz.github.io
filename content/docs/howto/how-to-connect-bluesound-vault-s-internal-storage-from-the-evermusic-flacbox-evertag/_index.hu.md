---
title: "Hogyan csatlakoztassuk a Bluesound VAULT belső tárhelyét az Evermusic, Flacbox, Evertag alkalmazásokból"
date: 2022-03-10
description: "Ismerje meg, hogyan érheti el a Bluesound VAULT belső merevlemezét az Evermusic, Flacbox és Evertag alkalmazásokból az SMB protokoll használatával hangfájlok kezeléséhez, szerkesztéséhez és lejátszásához."
keywords: ["bluesound vault", "smb tárhely csatlakoztatása", "evermusic smb", "flacbox vault", "evertag smb", "nas tárhely zene", "vault belső meghajtó"]
tags: ["evermusic", "csatlakoztatás", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Összefoglaló:** Csatlakozzon a Bluesound VAULT belső tárhelyéhez SMB-n keresztül az Evermusic, Flacbox vagy Evertag használatával. Keresse meg a VAULT IP-címét a BluOS alkalmazásban, adja meg SMB-kapcsolatként vendég hozzáféréssel, és kezdje el lejátszani vagy kezelni zenefájljait.

A Bluesound VAULT belső merevlemezzel rendelkezik és hálózati csatlakozású tárhelyként (NAS) működik. A VAULT belső merevlemezéhez való hozzáférés lehetővé teszi fájlok hozzáadását/törlését, metaadat-címkék szerkesztését az Evermusic, Flacbox, Evertag alkalmazásainkból.

**A következő lépésekkel férhet hozzá a VAULT belső merevlemezéhez:**

1. A BluOS alkalmazásban válassza a **Súgó > Diagnosztika** menüpontot.

2. A **Diagnosztika** oldalon szerezze be a VAULT **IP-címét**. Ezt az **IP-címet** a következő lépésekben fogja használni.

3. Nyissa meg az Evermusic, Flacbox vagy Evertag alkalmazást.

   ![Everappz alkalmazások](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Nyissa meg a "Kapcsolatok" képernyőt és válassza a "Felhőszolgáltatás csatlakoztatása" menüpontot.

   ![Evermusic Kapcsolatok képernyő](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Válassza az "SMB" felhőszolgáltatást.

   ![Evermusic Felhőszolgáltatás csatlakoztatása képernyő](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Az "SMB konfigurációs képernyőn" adja meg az URL-t a következő formátumban:

   ```
   SMB://<<VAULT-IP>>
   ```

   Cserélje le a `<<VAULT-IP>>` részt a 2. lépésben kapott **IP-címre**.

   **Megjegyzés:** Hagyja üresen a Bejelentkezés és Jelszó mezőket, mert a VAULT tárhely támogatja a VENDÉG módot.

   ![Evermusic SMB kapcsolat képernyő](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Koppintson a "Bejelentkezés" gombra a konfiguráció mentéséhez.

8. Nyissa meg a csatlakoztatott felhőtárhelyet, navigáljon a hangfájlokat tartalmazó mappába, és koppintson bármely fájlra a lejátszó indításához.

   ![Evermusic Megnyitott SMB szerver képernyő](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. A beépített fájlkezelővel is szerkesztheti a fájlokat.

   ![Evermusic Fájlkezelő képernyő](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Ezekkel az egyszerű lépésekkel könnyedén hozzáférhet a Bluesound VAULT belső merevlemezéhez, és átveheti az irányítást zenei könyvtára felett az Evermusic, Flacbox vagy Evertag használatával.

## GYIK

{{% details title="Szükségem van felhasználónévre és jelszóra a Bluesound VAULT-hoz való csatlakozáshoz?" closed="true" %}}
Nem. A Bluesound VAULT támogatja a vendég (anonim) hozzáférést SMB-n keresztül. Hagyja üresen a Bejelentkezés és Jelszó mezőket a kapcsolat konfigurálásánál.
{{% /details %}}

{{% details title="Szerkeszthetem a zenei címkéket a Bluesound VAULT-on?" closed="true" %}}
Igen. Az Evertag használatával szerkesztheti a metaadat-címkéket (cím, előadó, album stb.) a VAULT belső merevlemezén közvetlenül tárolt hangfájlokhoz.
{{% /details %}}

{{% details title="Milyen protokollokat támogat a Bluesound VAULT?" closed="true" %}}
A Bluesound VAULT SMB-n (Server Message Block) keresztül teszi elérhetővé belső tárhelyét. Az Evermusic, Flacbox és Evertag mind támogatja az SMB-kapcsolatokat, ami egyszerűvé teszi a csatlakozást.
{{% /details %}}

{{% details title="Streamelhetek zenét a VAULT-ról anélkül, hogy fájlokat másolnék az iPhone-omra?" closed="true" %}}
Igen. Az SMB-n keresztüli csatlakozás után közvetlenül a VAULT belső meghajtójáról streamelhet hangfájlokat anélkül, hogy azokat az eszközére másolná.
{{% /details %}}
