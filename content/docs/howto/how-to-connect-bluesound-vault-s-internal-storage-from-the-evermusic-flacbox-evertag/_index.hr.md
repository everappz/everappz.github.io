---
title: "Kako povezati internu pohranu Bluesound VAULT-a iz aplikacija Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Naučite kako pristupiti unutarnjem tvrdom disku Bluesound VAULT-a iz Evermusic, Flacbox i Evertag koristeći SMB protokol za upravljanje, uređivanje i reprodukciju audio datoteka."
keywords: ["bluesound vault", "povezati smb pohranu", "evermusic smb", "flacbox vault", "evertag smb", "nas pohrana glazba", "vault interni pogon"]
tags: ["evermusic", "povezati", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Sažetak:** Povežite se s internom pohranom vašeg Bluesound VAULT-a putem SMB-a koristeći Evermusic, Flacbox ili Evertag. Pronađite IP adresu VAULT-a u BluOS aplikaciji, unesite je kao SMB vezu s pristupom gosta i počnite reproducirati ili upravljati svojim glazbenim datotekama.

Bluesound VAULT ima unutarnji tvrdi disk i djeluje kao mrežna pohrana (NAS). Pristup unutarnjem tvrdom disku VAULT-a omogućuje vam dodavanje/brisanje datoteka, uređivanje oznaka metapodataka iz naših aplikacija Evermusic, Flacbox, Evertag.

**Sljedeći su koraci za pristup unutarnjem tvrdom disku vašeg VAULT-a:**

1. U BluOS aplikaciji odaberite **Pomoć > Dijagnostika**.

2. Na stranici **Dijagnostika** pronađite **IP adresu** VAULT-a. Ova **IP adresa** koristit će se u sljedećim koracima.

3. Otvorite Evermusic, Flacbox ili Evertag.

   ![Everappz aplikacije](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Otvorite zaslon "Povezivanja" i odaberite stavku izbornika "Poveži oblak uslugu".

   ![Zaslon Povezivanja u Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Odaberite "SMB" oblak uslugu.

   ![Zaslon Poveži oblak uslugu u Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Na "zaslonu za konfiguraciju SMB-a" unesite URL u sljedećem formatu:

   ```
   SMB://<<VAULT-IP>>
   ```

   Zamijenite `<<VAULT-IP>>` s **IP adresom** dobivenom u koraku 2.

   **Napomena:** Ostavite polja za prijavu i lozinku prazna jer VAULT pohrana podržava GOST način rada.

   ![Zaslon SMB veze u Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Dodirnite gumb "Prijavi se" za spremanje konfiguracije.

8. Otvorite povezanu oblak pohranu, navigirajte unutar mape s audio datotekama i dodirnite bilo koju datoteku za pokretanje audio playera.

   ![Zaslon otvorenog SMB servera u Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Također možete uređivati datoteke koristeći ugrađeni upravitelj datoteka.

   ![Zaslon upravitelja datoteka u Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Ovim jednostavnim koracima možete lako pristupiti unutarnjem tvrdom disku vašeg Bluesound VAULT-a i preuzeti kontrolu nad svojom glazbenom knjižnicom koristeći Evermusic, Flacbox ili Evertag.

## Često postavljana pitanja

{{% details title="Trebam li korisničko ime i lozinku za povezivanje s Bluesound VAULT-om?" closed="true" %}}
Ne. Bluesound VAULT podržava pristup gosta (anonimni) putem SMB-a. Ostavite polja za prijavu i lozinku prazna prilikom konfiguriranja veze.
{{% /details %}}

{{% details title="Mogu li uređivati glazbene oznake na Bluesound VAULT-u?" closed="true" %}}
Da. Koristeći Evertag, možete uređivati oznake metapodataka (naslov, umjetnik, album itd.) za audio datoteke pohranjene izravno na unutarnjem tvrdom disku VAULT-a.
{{% /details %}}

{{% details title="Koje protokole Bluesound VAULT podržava?" closed="true" %}}
Bluesound VAULT izlaže svoju internu pohranu putem SMB-a (Server Message Block). Evermusic, Flacbox i Evertag svi podržavaju SMB veze, što čini povezivanje jednostavnim.
{{% /details %}}

{{% details title="Mogu li streamati glazbu s VAULT-a bez kopiranja datoteka na svoj iPhone?" closed="true" %}}
Da. Nakon što se povežete putem SMB-a, možete streamati audio datoteke izravno s unutarnjeg pogona VAULT-a bez kopiranja na vaš uređaj.
{{% /details %}}
