---
title: "Cum să conectați stocarea internă a Bluesound VAULT din Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Aflați cum să accesați hard disk-ul intern al Bluesound VAULT din Evermusic, Flacbox și Evertag utilizând protocolul SMB pentru a gestiona, edita și reda fișiere audio."
keywords: ["bluesound vault", "conectare stocare smb", "evermusic smb", "flacbox vault", "evertag smb", "stocare nas muzică", "unitate internă vault"]
tags: ["evermusic", "conectare", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Rezumat:** Conectați-vă la stocarea internă a Bluesound VAULT prin SMB folosind Evermusic, Flacbox sau Evertag. Găsiți adresa IP a VAULT în aplicația BluOS, introduceți-o ca o conexiune SMB cu acces pentru oaspeți și începeți să redați sau să gestionați fișierele muzicale.

Bluesound VAULT are un hard disk intern și funcționează ca un dispozitiv de stocare atașat la rețea (NAS). Accesarea hard disk-ului intern al VAULT vă permite să adăugați/ștergeți fișiere, să editați etichetele de metadate din aplicațiile noastre Evermusic, Flacbox, Evertag.

**Următorii sunt pașii pentru a accesa hard disk-ul intern al VAULT:**

1. În aplicația BluOS, selectați **Ajutor > Diagnosticare**.

2. Din pagina **Diagnosticare**, obțineți **Adresa IP** a VAULT. Această **Adresă IP** va fi utilizată în pașii următori.

3. Deschideți Evermusic, Flacbox sau Evertag.

   ![Aplicații Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Deschideți ecranul "Conexiuni" și selectați elementul de meniu "Conectare serviciu cloud".

   ![Ecranul Conexiuni Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Selectați serviciul cloud "SMB".

   ![Ecranul Conectare Serviciu Cloud Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Pe "Ecranul de configurare SMB" introduceți URL-ul în următorul format:

   ```
   SMB://<<VAULT-IP>>
   ```

   Înlocuiți `<<VAULT-IP>>` cu **Adresa IP** obținută la Pasul 2.

   **Notă:** Lăsați câmpurile Autentificare și Parolă goale deoarece stocarea VAULT suportă modul OASPETE.

   ![Ecranul conexiune SMB Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Atingeți butonul "Autentificare" pentru a salva configurația.

8. Deschideți stocarea cloud conectată, navigați în folderul cu fișiere audio și atingeți orice fișier pentru a porni playerul audio.

   ![Ecranul Server SMB Deschis Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. De asemenea, puteți edita fișiere folosind managerul de fișiere integrat.

   ![Ecranul Manager Fișiere Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Cu acești pași simpli, puteți accesa cu ușurință hard disk-ul intern al Bluesound VAULT și puteți prelua controlul asupra bibliotecii muzicale folosind Evermusic, Flacbox sau Evertag.

## Întrebări frecvente

{{% details title="Am nevoie de un nume de utilizator și o parolă pentru a mă conecta la Bluesound VAULT?" closed="true" %}}
Nu. Bluesound VAULT suportă acces pentru oaspeți (anonim) prin SMB. Lăsați câmpurile Autentificare și Parolă goale la configurarea conexiunii.
{{% /details %}}

{{% details title="Pot edita etichetele muzicale pe Bluesound VAULT?" closed="true" %}}
Da. Folosind Evertag, puteți edita etichetele de metadate (titlu, artist, album etc.) pentru fișierele audio stocate direct pe hard disk-ul intern al VAULT.
{{% /details %}}

{{% details title="Ce protocoale suportă Bluesound VAULT?" closed="true" %}}
Bluesound VAULT expune stocarea internă prin SMB (Server Message Block). Evermusic, Flacbox și Evertag suportă toate conexiunile SMB, făcând conectarea simplă.
{{% /details %}}

{{% details title="Pot reda muzică în streaming de pe VAULT fără a copia fișiere pe iPhone-ul meu?" closed="true" %}}
Da. Odată conectat prin SMB, puteți reda în streaming fișiere audio direct de pe unitatea internă a VAULT fără a le copia pe dispozitivul dvs.
{{% /details %}}
