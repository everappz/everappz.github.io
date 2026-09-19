---
title: "Partajare"
date: 2026-08-20
description: "Află cum funcționează partajarea în Everdisk: apeși Start ca să transformi iPhone-ul sau iPad-ul într-un disc wireless, alegi ce vrei să partajezi (fișiere, foldere, fotografii și muzică), pornești cele cinci servere (DLNA, HTTP, WebDAV, SMB, FTP), criptezi conexiunea SMB cu SMB3 (AES), citești adresele de conectare, vezi cine este conectat și menții partajarea activă prin Wi-Fi sau printr-un cablu USB."
keywords: ["partajare Everdisk", "disc wireless iPhone", "pornire partajare", "partajare fișiere iPhone", "partajare fotografii în rețea", "DLNA HTTP WebDAV FTP", "ce să partajezi", "cum să te conectezi", "menține aplicația deschisă", "partajare prin Wi-Fi sau cablu USB"]
tags: ["everdisk", "ghid", "partajare"]
readingTime: 9
---


Fila **Partajare** este inima aplicației Everdisk. Aici îți transformi iPhone-ul sau iPad-ul într-un disc wireless, alegi exact ce vrei să partajezi și obții adresele pe care celelalte dispozitive le folosesc ca să se conecteze. Este prima filă pe care o vezi când deschizi aplicația.

## Pornirea și oprirea partajării

În mijlocul ecranului de Partajare se află un buton mare, rotund.

- Apasă **Start** ca să pornești toate serverele activate deodată. Butonul afișează **Se pornește...**, apoi **Stop** odată ce partajarea este activă.
- Apasă **Stop** ca să oprești din nou totul. Dispozitivele conectate sunt deconectate.

Cât timp partajarea rulează, fișierele, fotografiile și muzica alese de tine sunt disponibile pentru orice dispozitiv din aceeași rețea care se conectează folosind una dintre cele cinci metode de mai jos.

> Partajarea rulează doar cât timp aplicația este deschisă. Vezi **Menține aplicația deschisă** aproape de finalul acestei pagini pentru a înțelege de ce și cum poți menține transferurile mari în desfășurare.

## Alege ce vrei să partajezi

Înainte de a porni, apasă antetul **Ce să partajezi** ca să deschizi trei grupuri. Poți partaja orice combinație dintre ele și trebuie să alegi cel puțin un element înainte ca partajarea să poată începe.

**Fișiere și foldere**

- Folderul **Documente** propriu al aplicației este partajat în mod implicit. Poți opri partajarea lui dacă preferi.
- Apasă **Adaugă folder** ca să partajezi un folder de oriunde de pe dispozitivul tău sau **Adaugă fișier** ca să partajezi fișiere individuale.
- Fiecare element partajat are un buton **Info** și un buton **Oprește partajarea**.

**Fotografii și videoclipuri**

- Activează **Permite accesul la întreaga bibliotecă foto** ca să partajezi toată biblioteca ta de fotografii și videoclipuri sau
- apasă **Adaugă fotografii** ca să alegi manual doar fotografiile și videoclipurile pe care vrei să le partajezi.

**Muzică**

- Activează **Permite accesul la întreaga bibliotecă muzicală** ca să partajezi toată biblioteca ta muzicală sau
- apasă **Adaugă piese** ca să partajezi doar melodiile selectate.
- Piesele protejate (DRM) sau stocate doar în cloud nu pot fi partajate.

Dacă încerci să pornești fără să fi selectat nimic, Everdisk afișează o notă **Nimic de partajat**. Dacă modifici ce este partajat în timp ce partajarea rulează, apasă **Stop și Start din nou** ca să aplici schimbarea.

## Cele cinci servere

Everdisk partajează același conținut în cinci moduri deodată. Fiecare este gândit pentru un alt tip de dispozitiv și fiecare poate fi activat sau dezactivat în **Setări → Partajare → Conexiuni**. În mod implicit, toate cele cinci sunt active.

- **TV și Media Center (DLNA)** - pentru televizoare smart și playere media. Îți descoperă singure dispozitivul și îți afișează fotografiile, videoclipurile și muzica, cu miniaturi de previzualizare.
- **Browser (HTTP)** - pentru orice telefon, tabletă sau computer. Cealaltă persoană deschide un link într-un browser web ca să răsfoiască și să descarce fișierele tale. Nu trebuie instalat nimic.
- **Computer (WebDAV)** - pentru un Mac, un PC cu Windows sau o mașină Linux. Dispozitivul tău apare ca o unitate de rețea obișnuită, așa că poți trage fișiere în ambele sensuri.
- **Computer (avansat) (SMB)** - un disc de rețea pentru Mac, Windows și Linux. Pe un Mac apare de la sine în bara laterală Finder; pe Windows, îl deschizi în File Explorer cu o adresă `smb://`. Este singura conexiune pe care o poți **cripta**, cu criptare SMB3 (AES).
- **Alte aplicații și dispozitive (FTP)** - pentru aplicații de fișiere și utilizatori avansați care vorbesc FTP.

Pentru instrucțiuni de conectare pas cu pas pentru fiecare tip, vezi [Conectează-ți dispozitivele](/docs/guide/everdisk/everdisk-guide-connect).

## Cum să te conectezi și adresele de conectare

După ce apeși Start, secțiunea **Cum să te conectezi** afișează câte un card pentru fiecare server activ, cu **adresa** exactă pe care o tastezi pe celălalt dispozitiv. Fiecare adresă se copiază ușor - apasă pe ea ca să o copiezi, folosește butonul **Partajează** ca să o trimiți sau apasă butonul **info (ⓘ)** pentru instrucțiuni detaliate, specifice fiecărui protocol.

- Cardul DLNA afișează o adresă de descriere a dispozitivului care se termină în `/device-desc.xml`, pentru playerele care cer una.
- Când dispozitivul tău este conectat la un Mac cu un cablu, apare o adresă suplimentară cu o insignă **Conexiune prin cablu**, care folosește numele `.local` al dispozitivului tău.

Poți deschide adresa și sub forma unui **cod QR**, ca să sară camera altui dispozitiv direct la ea.

## Cine este conectat

Secțiunea **Cine este conectat** listează în timp real dispozitivele conectate la tine în acest moment. Apasă butonul de mai multe acțiuni de lângă orice dispozitiv ca să **Blochezi acest dispozitiv** dacă nu îl recunoști. Dispozitivele blocate se gestionează în [Acces și confidențialitate](/docs/guide/everdisk/everdisk-guide-access).

## Numele și avatarul dispozitivului tău

Fiecare dispozitiv are un nume prietenos (de exemplu "Speedy-Hare") și un avatar colorat. Acesta este numele pe care un TV, un computer sau o altă aplicație îl afișează pentru dispozitivul tău în rețea, așa că este ușor de recunoscut. Poți genera din nou numele și avatarul gratuit sau poți seta un nume, o pictogramă sau un avatar din fotografii personalizat cu Premium. Vezi [Setări](/docs/guide/everdisk/everdisk-guide-settings).

## Partajarea prin Wi-Fi sau printr-un cablu USB

Partajarea poate rula în două situații:

- **Prin Wi-Fi** - dispozitivul tău și celelalte dispozitive sunt în aceeași rețea Wi-Fi.
- **Printr-un cablu USB** - dispozitivul tău este conectat la un **Mac** cu un cablu, chiar și atunci când nu există deloc Wi-Fi. Este mai rapid decât Wi-Fi și continuă să funcționeze într-un avion, într-un hotel sau într-o rețea blocată.

Dacă nu ai nici Wi-Fi, nici cablu, butonul **Start** este dezactivat și apare o notă **Fără conexiune Wi-Fi**. Dacă se întrerupe conexiunea în timpul partajării, Everdisk oprește partajarea automat și te anunță. Apasă butonul info de pe oricare dintre aceste note pentru o explicație completă.

## Menține aplicația deschisă

Deoarece iPhone-ul sau iPad-ul tău funcționează ca server, **partajarea funcționează doar cât timp Everdisk este deschis pe ecran**. Dacă închizi aplicația sau blochezi dispozitivul pentru mult timp, sistemul poate pune aplicația în pauză și partajarea se oprește.

Pentru transferuri mari:

- Menține Everdisk deschis și în prim-plan.
- Conectează dispozitivul la o sursă de alimentare.
- Setează **Blocare automată** pe **Niciodată** în aplicația Setări din iOS cât timp faci transferul.

Poți activa **Notifică înainte de deconectare** (în Setări → Partajare), ca Everdisk să îți amintească să redeschizi aplicația înainte ca sistemul să o suspende. Apasă butonul info de pe bannerul **Menține aplicația deschisă** pentru mai multe detalii.

## Pașii următori

- [Conectează-ți dispozitivele](/docs/guide/everdisk/everdisk-guide-connect) - conectează un TV, un computer, un browser, un telefon sau un cablu USB.
- [Acces și confidențialitate](/docs/guide/everdisk/everdisk-guide-access) - adaugă o parolă și controlează editarea.
- [Setări](/docs/guide/everdisk/everdisk-guide-settings) - activează sau dezactivează servere și reglează calitatea.
