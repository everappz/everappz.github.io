---
title: "Acces și confidențialitate"
date: 2026-08-20
description: "Menține partajarea Everdisk în siguranță: protejează accesul cu un utilizator și o parolă, criptează conexiunea SMB cu SMB3 (AES), controlează dacă dispozitivele conectate pot încărca, redenumi și șterge prin Editarea fișierelor, blochează dispozitivele necunoscute, alege între coș de gunoi și ștergere permanentă și înțelege de ce totul rămâne în rețeaua ta locală."
keywords: ["protejare cu parolă Everdisk", "criptare SMB", "criptare SMB3 AES", "comutator editare fișiere", "blocare dispozitiv", "dispozitive blocate", "ștergere permanentă fișiere", "doar rețea locală", "partajare privată de fișiere", "DLNA fără parolă", "siguranță în rețea"]
tags: ["everdisk", "ghid", "acces", "confidențialitate", "securitate"]
readingTime: 8
---


Everdisk îți păstrează fișierele în propria ta rețea și îți oferă controale simple asupra a cine le poate accesa și ce poate face. Găsești aceste controale în **Setări → Partajare → Acces**, plus câteva setări conexe în Managerul de fișiere.

## Protejează accesul cu un utilizator și o parolă

În mod implicit, oricine se află în aceeași rețea și îți are adresa poate deschide fișierele tale partajate. Ca să impui o autentificare:

1. Mergi la **Setări → Partajare → Acces**.
2. Introdu un **Utilizator** și o **Parolă**.
3. Acum conexiunile **Browser (HTTP)**, **Computer (WebDAV)**, **Computer (avansat) (SMB)** și **Alte aplicații și dispozitive (FTP)** cer toate acele detalii înainte de a-ți afișa fișierele.

Lasă ambele câmpuri goale pentru acces deschis. Parola ta este stocată în siguranță în Keychain-ul dispozitivului.

> **DLNA este întotdeauna deschis.** Conexiunea TV și Media Center (DLNA) nu poate fi protejată cu parolă, așa că odată ce este activată, orice dispozitiv din aceeași rețea Wi-Fi îți poate răsfoi conținutul media partajat. Dezactiveaz-o dacă vrei doar conexiuni protejate și partajează doar în rețele în care ai încredere.

## Criptează conexiunea SMB (SMB3 / AES)

Un utilizator și o parolă controlează **cine** se poate conecta, dar datele în sine circulă totuși necriptate pe majoritatea conexiunilor. **SMB este singura conexiune pe care Everdisk o poate cripta**, ceea ce codifică fiecare transfer, astfel încât nimeni altcineva din aceeași rețea să nu-l poată citi.

Ca să o activezi:

1. Setează un **Utilizator** și o **Parolă** ca mai sus - conexiunile criptate nu pot fi anonime.
2. Mergi la **Setări → Partajare** și activează **Solicită criptare SMB**.
3. **Oprește și pornește** din nou partajarea, ca modificarea să intre în vigoare.

Fiecare transfer SMB este apoi protejat cu **criptare SMB3 (AES)**. Dispozitivul care se conectează trebuie să accepte SMB3 - Finder-ul de pe un Mac modern sau **Windows 10 și versiunile ulterioare**. Este o alegere excelentă pe un Wi-Fi în care nu ai deplină încredere. Criptarea SMB este o funcție Premium.

## Permite sau blochează editarea (Editarea fișierelor)

Comutatorul **Editarea fișierelor** controlează dacă dispozitivele conectate pot doar să îți vadă fișierele sau le pot și modifica.

- **Activat** (varianta implicită): dispozitivele conectate pot **încărca, redenumi și șterge** fișierele tale partajate - așa că dispozitivul tău funcționează ca o unitate de rețea reală, bidirecțională.
- **Dezactivat**: fișierele tale partajate sunt **doar pentru citire**. Ceilalți le pot vedea și descărca, dar nu pot adăuga sau modifica nimic.

Activarea lui afișează un scurt avertisment, pentru că le permite altor persoane să îți modifice fișierele. Poartă o insignă **Important** cât timp este activat.

## Blochează un dispozitiv

Dacă vezi un dispozitiv pe care nu îl recunoști:

1. Pe ecranul de Partajare, găsește-l la **Cine este conectat**.
2. Apasă butonul lui de mai multe acțiuni și alege **Blochează acest dispozitiv**.

Dispozitivele blocate sunt listate în **Setări → Partajare → Acces → Dispozitive blocate**, unde poți **debloca** unul sau poți alege **Deblochează tot**. Blocarea urmărește dispozitivul chiar dacă adresa lui din rețea se schimbă (pentru conexiunile Browser, Computer și TV).

## Coș de gunoi vs. ștergere permanentă

Când un fișier este șters - de tine în managerul de fișiere sau de un dispozitiv conectat - el ajunge în mod normal într-un **coș de gunoi** recuperabil, ca să îl poți aduce înapoi.

Dacă preferi ca fișierele să fie eliminate imediat, fără posibilitatea de recuperare, activează **Șterge permanent fișierele** în **Setări → Manager de fișiere → Ștergerea fișierelor**. Această opțiune este dezactivată în mod implicit. **Afectează managerul de fișiere de pe dispozitiv** și **ștergerile făcute în rețea**; nu schimbă felul în care biblioteca foto sau biblioteca muzicală a sistemului gestionează ștergerea.

## Totul rămâne local

Everdisk partajează doar în **rețeaua ta locală** - nimic nu este încărcat pe internet și nu există niciun cont cloud la mijloc. Câteva lucruri de care merită să știi:

- Everdisk are nevoie de permisiunea iOS **Rețea locală**, ca dispozitivele din apropiere să îl poată găsi. Dacă acea permisiune este dezactivată, o notă îți explică cum să o reactivezi în aplicația Setări din iOS.
- Pentru cea mai mare confidențialitate, partajează doar cât timp ești într-o rețea Wi-Fi **de acasă sau privată** în care ai încredere și fii atent în rețelele Wi-Fi publice. Un utilizator și o parolă ajută, dar nu înlocuiesc o rețea de încredere.
- **Cea mai privată opțiune dintre toate este un cablu USB către un Mac** - datele trec direct prin cablu și nu ajung niciodată la router sau pe internet. Vezi [Conectează-ți dispozitivele](/docs/guide/everdisk/everdisk-guide-connect).

## Pașii următori

- [Partajare](/docs/guide/everdisk/everdisk-guide-sharing) - alege ce vrei să partajezi și pornește partajarea.
- [Setări](/docs/guide/everdisk/everdisk-guide-settings) - toate setările de Acces și Manager de fișiere într-un singur loc.
