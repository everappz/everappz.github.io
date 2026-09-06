---
title: "Conectează-te la servere"
date: 2026-08-20
description: "Folosește fila Dispozitive din Everdisk ca să te conectezi la alte servere din rețeaua ta. Adaugă și răsfoiește servere DLNA, WebDAV, FTP și SFTP și unități NAS, redă în flux audio și video, descarcă fișiere și creează, încarcă, redenumește, mută sau șterge pe serverele care permit acest lucru."
keywords: ["fila Dispozitive Everdisk", "conectare la NAS", "client DLNA iPhone", "client WebDAV iPhone", "client FTP iPhone", "client SFTP iPhone", "răsfoire server de rețea", "streaming de pe NAS", "descărcare de pe server", "conectare cloud WebDAV"]
tags: ["everdisk", "ghid", "dispozitive", "conexiuni"]
readingTime: 9
---


Everdisk nu este doar un disc wireless - este și un client pentru celelalte dispozitive din rețeaua ta. Fila **Dispozitive** îți permite să te conectezi la servere **DLNA**, **WebDAV**, **FTP** și **SFTP**, inclusiv la unități NAS și servere media, iar apoi să le răsfoiești, să le redai în flux și să le descarci fișierele.

## Ecranul Dispozitive

Fila Dispozitive are două părți:

- **Conexiuni** - serverele pe care le-ai salvat deja.
- **Dispozitive disponibile** - serverele pe care Everdisk le găsește automat în rețeaua ta locală.

Ca să te conectezi la ceva ce Everdisk a găsit deja, apasă pur și simplu pe el în **Dispozitive disponibile**. Ca să adaugi manual un server, apasă butonul **plus (+)** sau **Conexiune nouă**.

## Adaugă o conexiune nouă

Apasă **Conexiune nouă** și alege tipul de server la care vrei să ajungi:

- **DLNA / UPnP** - cel mai potrivit pentru servere media. Redă în flux video, muzică și fotografii din biblioteci media, unități de stocare în rețea și televizoare și computere compatibile DLNA. DLNA este doar pentru citire: poți răsfoi, reda în flux și descărca, dar nu poți încărca sau modifica fișiere.
- **WebDAV** - conectează-te la servere de fișiere, unități de stocare în rețea și drive-uri cloud care acceptă WebDAV. Citește și scrie atunci când serverul permite acest lucru.
- **FTP** - frecvent pe routere, unități de stocare în rețea și găzduire web. Portul implicit este 21 (990 pentru FTPS securizat); poți seta un port personalizat în adresă, de exemplu `ftp://host:2121`. Lasă utilizatorul și parola goale pentru acces anonim.
- **SFTP** - conectează-te securizat prin SSH. Portul implicit este 22; folosește un port personalizat în adresă dacă este nevoie, de exemplu `sftp://host:2222`.

> Everdisk se conectează doar la aceste protocoale din rețeaua locală și adresate direct. Nu se autentifică la conturi cloud precum Google Drive sau Dropbox. Un drive cloud este accesibil doar dacă acel serviciu oferă o adresă **WebDAV** pe care o poți tasta.

## Introdu adresa și autentifică-te

În editorul de conexiuni, completează:

- **Titlu** - un nume prietenos pentru conexiune.
- **URL / adresă** - adresa serverului (sunt afișate exemple pentru fiecare tip).
- **Utilizator** și **Parolă** - lasă ambele goale dacă serverul permite acces anonim.

Pentru WebDAV poți permite certificate nevalide dacă serverul tău folosește unul autosemnat. Dacă identitatea unui server securizat nu poate fi verificată, Everdisk îți cere confirmarea înainte de a avea încredere în el.

Utilizatorii versiunii gratuite pot salva până la **10** conexiuni. Premium elimină această limită.

## Răsfoiește, redă în flux și descarcă

Odată conectat, apasă pe server ca să îl deschizi:

- **Răsfoiește** folderele în listă sau grilă, sortează-le și vezi miniaturi. Serverele DLNA afișează și detalii muzicale și coperte.
- **Redă în flux** audio și video. Audio ajunge în coada mini playerului; videoclipul se redă pe tot ecranul. Derularea funcționează în timp ce un fișier este redat în flux.
- **Descarcă** fișiere pe dispozitivul tău. Selectează mai multe deodată pentru o descărcare în lot. Descărcările apar în **Transferuri de fișiere** și ajung în folderul tău **Documente**.
- **Info** pe orice element îi arată tipul, dimensiunea, data, calea și detaliile media.

## Modifică fișiere pe un server

Pe serverele care permit scrierea - **WebDAV, FTP și SFTP** - poți și gestiona fișiere:

- **Folder nou**
- **Încarcă fișiere** de pe dispozitivul tău
- **Redenumește**, **Mută** și **Șterge** (un element sau mai multe deodată)

Serverele **DLNA** sunt doar pentru citire, așa că aceste acțiuni nu sunt disponibile acolo.

## Urmărește transferurile

Descărcările și încărcările rulează în fundal și apar în **Transferuri de fișiere**, pe care le deschizi din colțul din stânga sus al filei **Documente**. Acolo poți urmări progresul și poți pune în pauză, relua, reîncerca, anula sau șterge sarcini. Poți regla transferurile și în [Setări → Rețea](/docs/guide/everdisk/everdisk-guide-settings) (doar Wi-Fi vs. Wi-Fi și date mobile, câte rulează deodată și dacă acestea continuă în fundal).

## Pașii următori

- [Fișiere și documente](/docs/guide/everdisk/everdisk-guide-files) - gestionează tot ce descarci.
- [Fotografii, muzică și video](/docs/guide/everdisk/everdisk-guide-media) - redă ce redai în flux.
- [Setări](/docs/guide/everdisk/everdisk-guide-settings) - limite de conexiuni și opțiuni de transfer.
