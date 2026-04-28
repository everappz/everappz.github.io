---
title: "Jak připojit interní úložiště Bluesound VAULT z aplikací Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Naučte se, jak přistupovat k internímu pevnému disku Bluesound VAULT z aplikací Evermusic, Flacbox a Evertag pomocí protokolu SMB pro správu, úpravu a přehrávání zvukových souborů."
keywords: ["bluesound vault", "připojení smb úložiště", "evermusic smb", "flacbox vault", "evertag smb", "nas úložiště hudba", "interní disk vault"]
tags: ["evermusic", "připojení", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Shrnutí:** Připojte se k internímu úložišti Bluesound VAULT přes SMB pomocí Evermusic, Flacbox nebo Evertag. Najděte IP adresu VAULT v aplikaci BluOS, zadejte ji jako SMB připojení s přístupem hosta a začněte přehrávat nebo spravovat své hudební soubory.

Bluesound VAULT má interní pevný disk a funguje jako síťové úložiště (NAS). Přístup k internímu pevnému disku VAULT vám umožňuje přidávat/mazat soubory, upravovat tagy metadat z našich aplikací Evermusic, Flacbox, Evertag.

**Následují kroky pro přístup k internímu pevnému disku VAULT:**

1. V aplikaci BluOS vyberte **Nápověda > Diagnostika**.

2. Na stránce **Diagnostika** získejte **IP adresu** VAULT. Tato **IP adresa** bude použita v dalších krocích.

3. Otevřete Evermusic, Flacbox nebo Evertag.

   ![Aplikace Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Otevřete obrazovku "Připojení" a vyberte položku nabídky "Připojit cloudovou službu".

   ![Obrazovka Připojení v Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Vyberte cloudovou službu "SMB".

   ![Obrazovka Připojit cloudovou službu v Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Na "obrazovce konfigurace SMB" zadejte URL v následujícím formátu:

   ```
   SMB://<<VAULT-IP>>
   ```

   Nahraďte `<<VAULT-IP>>` **IP adresou** získanou v kroku 2.

   **Poznámka:** Ponechte pole Přihlášení a Heslo prázdná, protože úložiště VAULT podporuje režim HOST.

   ![Obrazovka SMB připojení v Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Klepněte na tlačítko "Přihlásit se" pro uložení konfigurace.

8. Otevřete připojené cloudové úložiště, přejděte do složky se zvukovými soubory a klepněte na libovolný soubor pro spuštění přehrávače zvuku.

   ![Obrazovka otevřeného SMB serveru v Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Soubory můžete také upravovat pomocí vestavěného správce souborů.

   ![Obrazovka správce souborů v Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Pomocí těchto jednoduchých kroků můžete snadno přistupovat k internímu pevnému disku Bluesound VAULT a spravovat svou hudební knihovnu pomocí Evermusic, Flacbox nebo Evertag.

## Často kladené dotazy

{{% details title="Potřebuji uživatelské jméno a heslo pro připojení k Bluesound VAULT?" closed="true" %}}
Ne. Bluesound VAULT podporuje přístup hosta (anonymní) přes SMB. Při konfiguraci připojení ponechte pole Přihlášení a Heslo prázdná.
{{% /details %}}

{{% details title="Mohu upravovat hudební tagy na Bluesound VAULT?" closed="true" %}}
Ano. Pomocí Evertag můžete upravovat tagy metadat (název, interpret, album atd.) zvukových souborů uložených přímo na interním pevném disku VAULT.
{{% /details %}}

{{% details title="Jaké protokoly Bluesound VAULT podporuje?" closed="true" %}}
Bluesound VAULT zpřístupňuje své interní úložiště přes SMB (Server Message Block). Evermusic, Flacbox a Evertag všechny podporují SMB připojení, takže připojení je jednoduché.
{{% /details %}}

{{% details title="Mohu streamovat hudbu z VAULT bez kopírování souborů do iPhonu?" closed="true" %}}
Ano. Po připojení přes SMB můžete streamovat zvukové soubory přímo z interního disku VAULT bez jejich kopírování do vašeho zařízení.
{{% /details %}}
