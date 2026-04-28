---
title: "Sådan tilslutter du Bluesound VAULTs interne lager fra Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Lær hvordan du får adgang til Bluesound VAULTs interne harddisk fra Evermusic, Flacbox og Evertag ved hjælp af SMB-protokollen til at administrere, redigere og afspille lydfiler."
keywords: ["bluesound vault", "tilslut smb-lager", "evermusic smb", "flacbox vault", "evertag smb", "nas-lager musik", "vault internt drev"]
tags: ["evermusic", "tilslut", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Resumé:** Tilslut dit Bluesound VAULTs interne lager via SMB ved hjælp af Evermusic, Flacbox eller Evertag. Find VAULTs IP-adresse i BluOS-appen, indtast den som en SMB-forbindelse med gæsteadgang, og begynd at afspille eller administrere dine musikfiler.

Bluesound VAULT har en intern harddisk og fungerer som et netværkstilsluttet lager (NAS). Adgang til VAULTs interne harddisk giver dig mulighed for at tilføje/slette filer, redigere metadata-tags fra vores apps Evermusic, Flacbox, Evertag.

**Følgende er trinene for at få adgang til dit VAULTs interne harddisk:**

1. I BluOS-appen skal du vælge **Hjælp > Diagnostik**.

2. Fra siden **Diagnostik** skal du finde **IP-adressen** på VAULT. Denne **IP-adresse** vil blive brugt i de næste trin.

3. Åbn Evermusic, Flacbox eller Evertag.

   ![Everappz-applikationer](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Åbn skærmen "Forbindelser" og vælg menupunktet "Tilslut en cloud-tjeneste".

   ![Evermusic Forbindelser-skærm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Vælg cloud-tjenesten "SMB".

   ![Evermusic Tilslut en Cloud-tjeneste-skærm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. På "SMB-konfigurationsskærmen" skal du indtaste URL i følgende format:

   ```
   SMB://<<VAULT-IP>>
   ```

   Erstat `<<VAULT-IP>>` med **IP-adressen** fra Trin 2.

   **Bemærk:** Lad felterne Login og Adgangskode stå tomme, fordi VAULT-lageret understøtter GÆST-tilstand.

   ![Evermusic SMB-forbindelsesskærm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Tryk på knappen "Log ind" for at gemme konfigurationen.

8. Åbn det tilsluttede cloud-lager, naviger ind i mappen med lydfiler og tryk på en vilkårlig fil for at starte lydafspilleren.

   ![Evermusic Åbnet SMB-server-skærm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Du kan også redigere filer ved hjælp af den indbyggede filhåndtering.

   ![Evermusic Filhåndteringsskærm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Med disse enkle trin kan du nemt få adgang til din Bluesound VAULTs interne harddisk og tage kontrol over dit musikbibliotek ved hjælp af Evermusic, Flacbox eller Evertag.

## FAQ

{{% details title="Har jeg brug for et brugernavn og en adgangskode for at oprette forbindelse til Bluesound VAULT?" closed="true" %}}
Nej. Bluesound VAULT understøtter gæste- (anonym) adgang via SMB. Lad felterne Login og Adgangskode stå tomme, når du konfigurerer forbindelsen.
{{% /details %}}

{{% details title="Kan jeg redigere musik-tags på Bluesound VAULT?" closed="true" %}}
Ja. Ved hjælp af Evertag kan du redigere metadata-tags (titel, kunstner, album osv.) for lydfiler gemt direkte på VAULTs interne harddisk.
{{% /details %}}

{{% details title="Hvilke protokoller understøtter Bluesound VAULT?" closed="true" %}}
Bluesound VAULT eksponerer sit interne lager via SMB (Server Message Block). Evermusic, Flacbox og Evertag understøtter alle SMB-forbindelser, hvilket gør det nemt at oprette forbindelse.
{{% /details %}}

{{% details title="Kan jeg streame musik fra VAULT uden at kopiere filer til min iPhone?" closed="true" %}}
Ja. Når du er tilsluttet via SMB, kan du streame lydfiler direkte fra VAULTs interne drev uden at kopiere dem til din enhed.
{{% /details %}}
