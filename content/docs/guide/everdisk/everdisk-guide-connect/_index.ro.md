---
title: "Conectează-ți dispozitivele"
date: 2026-08-20
description: "Instrucțiuni pas cu pas pentru conectarea la discul tău wireless Everdisk: urmărește pe un smart TV prin DLNA, deschide-ți fișierele în orice browser web, montează dispozitivul ca unitate de rețea în Finder, Windows sau Linux prin WebDAV sau SMB (cu criptare SMB3/AES opțională), conectează aplicații de fișiere prin FTP și transferă printr-un cablu USB la un Mac, fără Wi-Fi."
keywords: ["conectare la Everdisk", "streaming la TV DLNA", "deschidere fișiere în browser", "montare unitate de rețea Finder", "WebDAV Windows Linux", "aplicație de fișiere FTP", "transfer prin cablu USB Mac", "conectare iPhone la computer", "unitate de rețea iPhone"]
tags: ["everdisk", "ghid", "conectare"]
readingTime: 11
---


După ce apeși **Start** pe ecranul de [Partajare](/docs/guide/everdisk/everdisk-guide-sharing), celelalte dispozitive se pot conecta la fișierele tale în cinci moduri diferite. Alege metoda care se potrivește dispozitivului pe care vrei să îl folosești. În fiecare caz, **adresa** exactă de care ai nevoie este afișată în secțiunea **Cum să te conectezi** de pe ecranul de Partajare.

> Ambele dispozitive trebuie să fie în **aceeași rețea Wi-Fi** - sau, în cazul unui Mac, conectate cu un **cablu USB** (vezi ultima secțiune).

## Urmărește pe un TV (DLNA)

Folosește această metodă ca să afișezi fotografii, videoclipuri și muzică pe un smart TV sau pe un player media.

1. În **Setări → Partajare → Conexiuni**, asigură-te că **TV și Media Center** este activat (este activat în mod implicit).
2. Pe ecranul de Partajare, apasă **Start**.
3. Pe televizorul tău, deschide playerul media integrat sau aplicația de server media (s-ar putea numi Media Player, SmartShare, AllShare sau ceva similar).
4. Dispozitivul tău apare în lista de servere media după numele lui (de exemplu "Speedy-Hare"). Selectează-l.
5. Răsfoiește fotografiile, videoclipurile și muzica partajate și începe redarea. Miniaturile de previzualizare apar automat.

Note:

- DLNA nu poate fi protejat cu parolă, așa că această conexiune este deschisă oricui se află în aceeași rețea Wi-Fi cât timp este activată.
- Dacă un videoclip nu se redă pe un TV mai vechi, scade calitatea video în **Setări → Partajare → Videoclipuri**, ca Everdisk să îl convertească într-un format mai compatibil.

## Deschide într-un browser web (HTTP)

Folosește această metodă ca să dai fișiere oricui are un browser web - nu trebuie instalată nicio aplicație.

1. În **Setări → Partajare → Conexiuni**, asigură-te că **Browser** este activat.
2. Apasă **Start**.
3. Pe ecranul de Partajare, copiază adresa **Browser** (sau afișează-i codul QR).
4. Pe celălalt telefon, tabletă sau computer, deschide orice browser web (Safari, Chrome, Edge, Firefox) și tastează acea adresă.
5. Pagina se deschide cu fișierele tale partajate.

În browser, cealaltă persoană poate:

- Comuta între vizualizarea **listă** și **grilă** și sorta după nume, dată sau dimensiune.
- Vedea **miniaturi** reale pentru fotografii, videoclipuri, PDF-uri și coperte muzicale.
- Deschide o fotografie într-o **galerie** pe tot ecranul, cu glisare, ciupire pentru zoom și prezentare de diapozitive.
- Reda muzică într-un **player** integrat, cu coadă de redare, redare aleatorie și repetare.
- **Descărca** orice fișier sau descărca un folder întreg (ori mai multe elemente selectate) sub forma unui singur fișier **Archive.zip**.
- **Încărca** fișiere înapoi pe dispozitivul tău - numai dacă ai activat **Editarea fișierelor** (vezi [Acces și confidențialitate](/docs/guide/everdisk/everdisk-guide-access)).

## Folosește-l ca unitate de rețea (WebDAV)

Folosește această metodă ca să faci dispozitivul tău să apară ca un disc obișnuit pe un Mac, un PC cu Windows sau o mașină Linux, ca să poți trage fișiere în ambele sensuri.

**Pe un Mac (Finder)**

1. În **Setări → Partajare → Conexiuni**, asigură-te că **Computer** este activat.
2. Apasă **Start** și reține adresa **Computer (WebDAV)**.
3. În Finder, alege **Go → Connect to Server** (sau apasă **⌘K**).
4. Tastează adresa WebDAV exact așa cum este afișată și dă clic pe **Connect**.
5. Introdu utilizatorul și parola dacă ai setat una, altfel conectează-te ca invitat.
6. Dispozitivul tău se deschide ca orice altă unitate de rețea. Trage fișiere în interior sau în exterior.

**Pe Windows**

1. Deschide **File Explorer**, dă clic dreapta pe **This PC** și alege **Add a network location** (sau mapează o unitate de rețea).
2. Introdu adresa WebDAV afișată în Everdisk.
3. Introdu utilizatorul și parola dacă ai setat una.

**Pe Linux**

1. Deschide managerul de fișiere și alege **Connect to Server** (sau folosește `davs://` / `dav://`).
2. Introdu adresa WebDAV afișată în Everdisk.

Dacă conexiunea este doar pentru citire sau bidirecțională depinde de setarea **Editarea fișierelor**. Cu ea activată, poți copia fișiere pe dispozitivul tău și le poți redenumi sau șterge; cu ea dezactivată, unitatea este doar pentru citire.

## Conectează-te prin SMB (unitate de rețea criptată)

SMB este o unitate de rețea pentru Mac, Windows și Linux, construită pe partajarea de fișiere deja existentă în aceste sisteme, așa că dispozitivul tău apare ca o unitate de rețea obișnuită - și este singura conexiune pe care o poți cripta.

1. În **Setări → Partajare → Conexiuni**, asigură-te că **Computer (avansat)** (conexiunea SMB) este activată.
2. Apasă **Start** și reține adresa **SMB**, care arată ca `smb://192.168.1.20:4455/Share`.
3. Conectează-te de pe computer:
   - **Mac:** dispozitivul tău apare de la sine în **bara laterală Finder** la **Locations** (Network) - doar dă clic pe el și autentifică-te. Pentru a te conecta manual, alege **Go → Connect to Server** (**⌘K**) și introdu adresa.
   - **Windows:** deschide **File Explorer**, dă clic dreapta pe **This PC** și alege **Map network drive**, apoi introdu `\\<address>\Share` folosind gazda și numele partajării de pe ecranul de Partajare (sau tastează adresa `smb://` în bara de adrese).
   - **Linux:** în managerul tău de fișiere alege **Connect to Server** și introdu adresa.
4. Introdu utilizatorul și parola dacă ai setat una, altfel conectează-te ca invitat.
5. Partajarea se numește **Share**. Cu **Editarea fișierelor** activată poți copia fișiere în ambele sensuri; cu ea dezactivată, este doar pentru citire.

**Activează criptarea (recomandat pe un Wi-Fi în care nu ai încredere)**

SMB este singura conexiune Everdisk care poate fi criptată. Ca să protejezi fiecare transfer cu **criptare SMB3 (AES)**:

1. În **Setări → Partajare → Acces**, setează un **Utilizator** și o **Parolă** - conexiunile criptate nu pot fi anonime.
2. În **Setări → Partajare**, activează **Solicită criptare SMB**.
3. **Oprește și pornește** din nou partajarea, ca modificarea să intre în vigoare.

Clientul tău trebuie să accepte SMB3 - Finder-ul de pe un Mac modern sau **Windows 10 și versiunile ulterioare**. Criptarea SMB este o funcție Premium.

## Conectează o aplicație de fișiere (FTP)

Folosește această metodă pentru aplicațiile de gestionare și transfer de fișiere care vorbesc FTP (de exemplu FileZilla sau Cyberduck pe un computer).

1. În **Setări → Partajare → Conexiuni**, asigură-te că **Alte aplicații și dispozitive** este activat.
2. Apasă **Start** și reține adresa **FTP**.
3. În aplicația ta FTP, adaugă o conexiune nouă folosind acea adresă.
4. Introdu utilizatorul și parola dacă ai setat una sau lasă-le goale pentru acces anonim.

## Transferă printr-un cablu USB (Mac, fără Wi-Fi)

Folosește această metodă atunci când nu ai Wi-Fi sau când vrei cel mai rapid și mai privat transfer. Funcționează doar cu un **Mac**.

1. Conectează iPhone-ul sau iPad-ul la Mac cu cablul obișnuit de încărcare.
2. Dacă ești întrebat pe dispozitiv, apasă **Trust This Computer**.
3. În Everdisk, apasă **Start**. Apare o notă **Conexiune rapidă disponibilă**, iar ecranul de Partajare afișează o adresă suplimentară cu o insignă **Conexiune prin cablu** care se termină în `.local`.
4. Pe Mac, deschide Finder → **Go → Connect to Server** (**⌘K**) și introdu acea adresă `.local` (funcționează atât pentru conexiunea Browser, cât și pentru Computer).
5. Dispozitivul tău se deschide prin cablu - mai rapid decât prin Wi-Fi, iar datele nu ajung niciodată la router sau pe internet.

Note:

- Folosește **numele `.local`**, nu o adresă IP (adresele IP funcționează doar prin Wi-Fi) și niciodată `localhost`.
- Calea prin cablu este **doar pentru Mac**. PC-urile cu Windows și dispozitivele Android trebuie să folosească Wi-Fi.
- Poți trage fișiere și în folderul Everdisk folosind Finder pe un Mac sau aplicația Apple Devices (ori iTunes) pe Windows, prin partajarea standard de fișiere din iOS.

## Pașii următori

- [Acces și confidențialitate](/docs/guide/everdisk/everdisk-guide-access) - adaugă o parolă, permite încărcări, blochează un dispozitiv.
- [Fotografii, muzică și video](/docs/guide/everdisk/everdisk-guide-media) - partajează întreaga bibliotecă și setează calitatea.
- [Conectează-te la servere](/docs/guide/everdisk/everdisk-guide-devices) - ajunge la alte dispozitive din Everdisk.
