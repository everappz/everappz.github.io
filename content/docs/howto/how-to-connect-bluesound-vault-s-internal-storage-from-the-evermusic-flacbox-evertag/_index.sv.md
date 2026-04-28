---
title: "Hur man ansluter Bluesound VAULTs interna lagring från Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Lär dig hur du kommer åt Bluesound VAULTs interna hårddisk från Evermusic, Flacbox och Evertag med SMB-protokollet för att hantera, redigera och spela upp ljudfiler."
keywords: ["bluesound vault", "anslut smb-lagring", "evermusic smb", "flacbox vault", "evertag smb", "nas-lagring musik", "vault intern enhet"]
tags: ["evermusic", "anslut", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Sammanfattning:** Anslut till din Bluesound VAULTs interna lagring via SMB med Evermusic, Flacbox eller Evertag. Hitta VAULTs IP-adress i BluOS-appen, ange den som en SMB-anslutning med gäståtkomst och börja spela upp eller hantera dina musikfiler.

Bluesound VAULT har en intern hårddisk och fungerar som en nätverksansluten lagring (NAS). Åtkomst till VAULTs interna hårddisk låter dig lägga till/ta bort filer, redigera metadata-taggar från våra appar Evermusic, Flacbox, Evertag.

**Följande är stegen för att komma åt din VAULTs interna hårddisk:**

1. I BluOS-appen väljer du **Hjälp > Diagnostik**.

2. Från sidan **Diagnostik** hämtar du VAULTs **IP-adress**. Denna **IP-adress** kommer att användas i nästa steg.

3. Öppna Evermusic, Flacbox eller Evertag.

   ![Everappz-applikationer](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Öppna skärmen "Anslutningar" och välj menyalternativet "Anslut en molntjänst".

   ![Evermusic Anslutningar-skärm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Välj "SMB"-molntjänsten.

   ![Evermusic Anslut en molntjänst-skärm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. På "SMB-konfigurationsskärmen" anger du URL i följande format:

   ```
   SMB://<<VAULT-IP>>
   ```

   Ersätt `<<VAULT-IP>>` med **IP-adressen** som erhölls i Steg 2.

   **Obs:** Lämna fälten Inloggning och Lösenord tomma eftersom VAULT-lagringen stöder GÄST-läge.

   ![Evermusic SMB-anslutningsskärm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Tryck på knappen "Logga in" för att spara konfigurationen.

8. Öppna den anslutna molnlagringen, navigera till mappen med ljudfiler och tryck på valfri fil för att starta ljudspelaren.

   ![Evermusic Öppnad SMB-server-skärm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Du kan också redigera filer med den inbyggda filhanteraren.

   ![Evermusic Filhanterarskärm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Med dessa enkla steg kan du enkelt komma åt din Bluesound VAULTs interna hårddisk och ta kontroll över ditt musikbibliotek med Evermusic, Flacbox eller Evertag.

## Vanliga frågor

{{% details title="Behöver jag ett användarnamn och lösenord för att ansluta till Bluesound VAULT?" closed="true" %}}
Nej. Bluesound VAULT stöder gäståtkomst (anonym) via SMB. Lämna fälten Inloggning och Lösenord tomma när du konfigurerar anslutningen.
{{% /details %}}

{{% details title="Kan jag redigera musiktaggar på Bluesound VAULT?" closed="true" %}}
Ja. Med Evertag kan du redigera metadata-taggar (titel, artist, album etc.) för ljudfiler som lagras direkt på VAULTs interna hårddisk.
{{% /details %}}

{{% details title="Vilka protokoll stöder Bluesound VAULT?" closed="true" %}}
Bluesound VAULT exponerar sin interna lagring via SMB (Server Message Block). Evermusic, Flacbox och Evertag stöder alla SMB-anslutningar, vilket gör det enkelt att ansluta.
{{% /details %}}

{{% details title="Kan jag strömma musik från VAULT utan att kopiera filer till min iPhone?" closed="true" %}}
Ja. När du är ansluten via SMB kan du strömma ljudfiler direkt från VAULTs interna enhet utan att kopiera dem till din enhet.
{{% /details %}}
