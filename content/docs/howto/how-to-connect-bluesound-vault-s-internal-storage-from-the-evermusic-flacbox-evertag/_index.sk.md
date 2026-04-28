---
title: "Ako pripojiť interné úložisko Bluesound VAULT z aplikácií Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Naučte sa, ako pristupovať k internému pevnému disku Bluesound VAULT z aplikácií Evermusic, Flacbox a Evertag pomocou protokolu SMB na správu, úpravu a prehrávanie zvukových súborov."
keywords: ["bluesound vault", "pripojenie smb úložiska", "evermusic smb", "flacbox vault", "evertag smb", "nas úložisko hudba", "interný disk vault"]
tags: ["evermusic", "pripojenie", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Zhrnutie:** Pripojte sa k internému úložisku Bluesound VAULT cez SMB pomocou Evermusic, Flacbox alebo Evertag. Nájdite IP adresu VAULT v aplikácii BluOS, zadajte ju ako SMB pripojenie s hosťovským prístupom a začnite prehrávať alebo spravovať svoje hudobné súbory.

Bluesound VAULT má interný pevný disk a funguje ako sieťové úložisko (NAS). Prístup k internému pevnému disku VAULT vám umožňuje pridávať/mazať súbory, upravovať tagy metadát z našich aplikácií Evermusic, Flacbox, Evertag.

**Nasledujú kroky na prístup k internému pevnému disku VAULT:**

1. V aplikácii BluOS vyberte **Pomoc > Diagnostika**.

2. Na stránke **Diagnostika** získajte **IP adresu** VAULT. Táto **IP adresa** sa použije v ďalších krokoch.

3. Otvorte Evermusic, Flacbox alebo Evertag.

   ![Aplikácie Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Otvorte obrazovku "Pripojenia" a vyberte položku ponuky "Pripojiť cloudovú službu".

   ![Obrazovka Pripojenia v Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Vyberte cloudovú službu "SMB".

   ![Obrazovka Pripojiť cloudovú službu v Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Na "Obrazovke konfigurácie SMB" zadajte URL v nasledujúcom formáte:

   ```
   SMB://<<VAULT-IP>>
   ```

   Nahraďte `<<VAULT-IP>>` **IP adresou** získanou v kroku 2.

   **Poznámka:** Ponechajte polia Prihlásenie a Heslo prázdne, pretože úložisko VAULT podporuje režim HOSŤA.

   ![Obrazovka SMB pripojenia v Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Ťuknite na tlačidlo "Prihlásiť sa" pre uloženie konfigurácie.

8. Otvorte pripojené cloudové úložisko, prejdite do priečinka so zvukovými súbormi a ťuknite na ľubovoľný súbor pre spustenie prehrávača zvuku.

   ![Obrazovka otvoreného SMB servera v Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Súbory môžete tiež upravovať pomocou vstavaného správcu súborov.

   ![Obrazovka správcu súborov v Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Pomocou týchto jednoduchých krokov môžete ľahko pristupovať k internému pevnému disku Bluesound VAULT a spravovať svoju hudobnú knižnicu pomocou Evermusic, Flacbox alebo Evertag.

## Často kladené otázky

{{% details title="Potrebujem používateľské meno a heslo na pripojenie k Bluesound VAULT?" closed="true" %}}
Nie. Bluesound VAULT podporuje hosťovský (anonymný) prístup cez SMB. Pri konfigurácii pripojenia ponechajte polia Prihlásenie a Heslo prázdne.
{{% /details %}}

{{% details title="Môžem upravovať hudobné tagy na Bluesound VAULT?" closed="true" %}}
Áno. Pomocou Evertag môžete upravovať tagy metadát (názov, interpret, album atď.) zvukových súborov uložených priamo na internom pevnom disku VAULT.
{{% /details %}}

{{% details title="Aké protokoly Bluesound VAULT podporuje?" closed="true" %}}
Bluesound VAULT sprístupňuje svoje interné úložisko cez SMB (Server Message Block). Evermusic, Flacbox a Evertag všetky podporujú SMB pripojenia, čo uľahčuje pripojenie.
{{% /details %}}

{{% details title="Môžem streamovať hudbu z VAULT bez kopírovania súborov do iPhonu?" closed="true" %}}
Áno. Po pripojení cez SMB môžete streamovať zvukové súbory priamo z interného disku VAULT bez ich kopírovania do vášho zariadenia.
{{% /details %}}
