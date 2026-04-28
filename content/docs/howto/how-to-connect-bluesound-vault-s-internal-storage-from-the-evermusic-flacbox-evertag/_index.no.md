---
title: "Slik kobler du til Bluesound VAULTs interne lagring fra Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Lær hvordan du får tilgang til Bluesound VAULTs interne harddisk fra Evermusic, Flacbox og Evertag ved hjelp av SMB-protokollen for å administrere, redigere og spille av lydfiler."
keywords: ["bluesound vault", "koble til smb-lagring", "evermusic smb", "flacbox vault", "evertag smb", "nas-lagring musikk", "vault intern stasjon"]
tags: ["evermusic", "koble til", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Sammendrag:** Koble til den interne lagringen til Bluesound VAULT via SMB ved hjelp av Evermusic, Flacbox eller Evertag. Finn VAULTs IP-adresse i BluOS-appen, skriv den inn som en SMB-tilkobling med gjestetilgang, og begynn å spille av eller administrere musikkfilene dine.

Bluesound VAULT har en intern harddisk og fungerer som en nettverkstilkoblet lagring (NAS). Tilgang til VAULTs interne harddisk lar deg legge til/slette filer, redigere metadata-tagger fra appene våre Evermusic, Flacbox, Evertag.

**Følgende er trinnene for å få tilgang til VAULTs interne harddisk:**

1. I BluOS-appen velger du **Hjelp > Diagnostikk**.

2. Fra **Diagnostikk**-siden henter du **IP-adressen** til VAULT. Denne **IP-adressen** brukes i de neste trinnene.

3. Åpne Evermusic, Flacbox eller Evertag.

   ![Everappz-applikasjoner](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Åpne skjermen "Tilkoblinger" og velg menyelementet "Koble til en skytjeneste".

   ![Evermusic Tilkoblinger-skjerm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Velg "SMB"-skytjenesten.

   ![Evermusic Koble til en skytjeneste-skjerm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. På "SMB-konfigurasjonsskjermen" skriver du inn URL i følgende format:

   ```
   SMB://<<VAULT-IP>>
   ```

   Erstatt `<<VAULT-IP>>` med **IP-adressen** fra Trinn 2.

   **Merk:** La feltene Pålogging og Passord stå tomme fordi VAULT-lagringen støtter GJEST-modus.

   ![Evermusic SMB-tilkoblingsskjerm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Trykk på "Logg inn"-knappen for å lagre konfigurasjonen.

8. Åpne den tilkoblede skylagringen, naviger til mappen med lydfiler og trykk på en hvilken som helst fil for å starte lydavspilleren.

   ![Evermusic Åpnet SMB-server-skjerm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Du kan også redigere filer ved hjelp av den innebygde filbehandleren.

   ![Evermusic Filbehandler-skjerm](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Med disse enkle trinnene kan du enkelt få tilgang til den interne harddisken til Bluesound VAULT og ta kontroll over musikkbiblioteket ditt med Evermusic, Flacbox eller Evertag.

## Vanlige spørsmål

{{% details title="Trenger jeg brukernavn og passord for å koble til Bluesound VAULT?" closed="true" %}}
Nei. Bluesound VAULT støtter gjestetilgang (anonym) via SMB. La feltene Pålogging og Passord stå tomme når du konfigurerer tilkoblingen.
{{% /details %}}

{{% details title="Kan jeg redigere musikktagger på Bluesound VAULT?" closed="true" %}}
Ja. Ved hjelp av Evertag kan du redigere metadata-tagger (tittel, artist, album osv.) for lydfiler lagret direkte på VAULTs interne harddisk.
{{% /details %}}

{{% details title="Hvilke protokoller støtter Bluesound VAULT?" closed="true" %}}
Bluesound VAULT eksponerer sin interne lagring via SMB (Server Message Block). Evermusic, Flacbox og Evertag støtter alle SMB-tilkoblinger, noe som gjør det enkelt å koble til.
{{% /details %}}

{{% details title="Kan jeg strømme musikk fra VAULT uten å kopiere filer til iPhonen min?" closed="true" %}}
Ja. Når du er koblet til via SMB, kan du strømme lydfiler direkte fra VAULTs interne stasjon uten å kopiere dem til enheten din.
{{% /details %}}
