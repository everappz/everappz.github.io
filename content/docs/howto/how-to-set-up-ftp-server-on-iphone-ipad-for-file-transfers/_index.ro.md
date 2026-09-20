---
title: "Cum configurezi un server FTP pe iPhone și iPad pentru transferuri de fișiere"
description: "Transformă-ți iPhone-ul sau iPad-ul într-un server FTP cu Everdisk și transferă fișiere de pe un Mac, un PC cu Windows, Linux, Android, o aplicație FTP precum FileZilla sau un alt iPhone prin Wi-Fi. Configurare completă, adresa și portul ftp, acces ca invitat și conectare pas cu pas pentru fiecare dispozitiv."
date: 2026-09-19
tags: ["everdisk", "ftp", "transfer fisiere", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["server FTP iPhone", "server FTP iPad", "cum configurez FTP pe iPhone", "aplicatie server ftp iphone", "conectare FileZilla la iPhone", "Cyberduck iPhone FTP", "transfer fisiere iPhone FTP", "ftp iphone la computer", "ftp iphone la iphone", "conectare la iPhone FTP de pe Windows", "adresa port ftp iphone", "ftp anonim iphone", "partajare fisiere iphone ftp", "iphone ftp pentru camera nas"]
readingTime: 9
---

{{< author-byline >}}

FTP este soluția veche și de încredere pentru transferul de fișiere. Există de zeci de ani, ceea ce este exact motivul pentru care este atât de utilă: aproape orice poate comunica cu un server îl înțelege. Camerele, televizoarele smart, routerele, discurile de rețea, instrumentele de automatizare și fiecare aplicație FTP de desktop vorbesc FTP. Cu [Everdisk](/products/everdisk) poți rula un server FTP pe iPhone-ul sau iPad-ul tău, astfel încât telefonul devine un loc la care acele dispozitive și aplicații se pot conecta și pot muta fișiere.

Apelează la FTP când celelalte opțiuni nu se potrivesc, de exemplu un dispozitiv mai vechi sau o aplicație care știe să se conecteze doar prin FTP. Acest ghid acoperă configurarea și cum te conectezi de pe un Mac, Windows, o aplicație FTP, Linux, Android și un al doilea iPhone.

## De ce ai nevoie

- Un iPhone sau iPad cu [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) instalat.
- Un computer, o aplicație sau un dispozitiv în **aceeași rețea Wi-Fi**.
- Fișierele pe care vrei să le partajezi, în folderul Documente al Everdisk sau în foldere pe care le adaugi.

## Configurează serverul FTP în Everdisk

### Pasul 1: Alege ce partajezi și setează accesul

Deschide Everdisk, mergi la fila **Partajare** și apasă **Ce partajezi**. Folderul Documente este partajat implicit. Adaugă mai multe cu **Adaugă folder** și **Adaugă fișier**.

Deschide **Setări**, apoi **Partajare**, apoi **Acces**. Activează **Editarea fișierelor** dacă vrei ca oamenii să încarce, redenumească și șteargă sau dezactiveaz-o pentru a permite doar descărcări. Setează un **Utilizator** și o **Parolă** dacă vrei o autentificare sau lasă-le goale, astfel încât oricine să se poată conecta ca invitat.

### Pasul 2: Activează serverul FTP

Mergi la **Setări**, apoi **Partajare**, apoi **Conexiuni** și activează **Alte aplicații și dispozitive**. Acesta este serverul FTP (poartă eticheta FTP).

### Pasul 3: Începe partajarea și notează adresa

Întoarce-te la fila **Partajare** și apasă **Start**. Secțiunea **Cum te conectezi** afișează adresa FTP. Arată așa:

```
ftp://192.168.1.20:2121
```

Numărul de după două puncte este **portul**, care este **2121** implicit. Prima parte este adresa iPhone-ului tău în rețeaua Wi-Fi, așa că a ta va fi diferită. Ține Everdisk deschis pe ecran cât timp un dispozitiv este conectat.

## Conectează-te de pe un Mac

1. Deschide **Finder**, alege **Go**, apoi **Connect to Server** (sau apasă **Command și K**).
2. Tastează adresa FTP afișată în Everdisk, de exemplu `ftp://192.168.1.20:2121`.
3. Apasă **Connect**, apoi alege **Guest** sau introdu **Utilizator** și **Parolă**.

Finder montează partajarea FTP, așa că poți răsfoi și copia fișiere pe Mac-ul tău. Reține că Finder deschide FTP doar pentru citire. Când vrei să încarci de pe un Mac, folosește o aplicație FTP așa cum este descris mai jos.

## Conectează-te de pe Windows

1. Deschide **File Explorer** și fă clic pe bara de adrese din partea de sus.
2. Tastează adresa FTP din Everdisk, de exemplu `ftp://192.168.1.20:2121`, și apasă **Enter**.
3. Introdu **Utilizator** și **Parolă** dacă ai setat sau continuă ca invitat.

Fișierele partajate apar în fereastră și le poți copia pe PC-ul tău.

## Conectează-te cu o aplicație FTP (FileZilla, Cyberduck)

Pentru încărcări și control complet, o aplicație FTP este cel mai bun instrument. **FileZilla** și **Cyberduck** sunt gratuite și rulează pe Windows, Mac și Linux.

1. Deschide aplicația și creează o nouă conexiune.
2. Setează **Host**-ul la adresa Wi-Fi a iPhone-ului tău și **Port**-ul la **2121**.
3. Pentru autentificare, introdu **Utilizator** și **Parolă** sau alege **Anonymous** dacă nu ai setat una.
4. Conectează-te și trage fișiere în ambele direcții (încărcările au nevoie de Editarea fișierelor activată).

## Conectează-te de pe Linux

1. Deschide managerul tău de fișiere și alege **Connect to Server** sau **Other Locations**.
2. Introdu adresa, de exemplu `ftp://192.168.1.20:2121`.
3. Conectează-te ca invitat sau cu autentificarea ta.

Poți folosi și orice client FTP Linux din terminal, îndreptându-l către aceeași gazdă și portul 2121.

## Conectează-te de pe Android

Android nu are un navigator FTP de sistem, așa că folosește o aplicație:

1. Instalează un client FTP precum **AndFTP**, **FTPCafe** sau un manager de fișiere cu suport FTP precum **Solid Explorer**.
2. Adaugă o conexiune cu gazda, **portul 2121** și autentificarea ta sau Anonymous.
3. Răsfoiește și transferă.

## Conectează-te de pe un alt iPhone sau iPad

Aplicația Files din iOS nu include un client FTP, așa că folosește una dintre acestea pe al doilea dispozitiv:

- **Fila proprie Dispozitive din Everdisk.** Deschide Everdisk, mergi la **Dispozitive**, apasă **Conexiune nouă**, alege **FTP** și introdu adresa, de exemplu `ftp://192.168.1.20:2121`. Aceasta este cea mai simplă cale.
- **O aplicație FTP dedicată** pentru iOS, folosind aceeași gazdă, portul 2121 și autentificarea.

## Conectează alte echipamente: camere, televizoare, routere și NAS

Aici strălucește FTP. Multe dispozitive au un client FTP integrat care poate trimite sau prelua fișiere:

- **Camerele** care încarcă fotografii prin FTP le pot trimite direct pe iPhone-ul tău.
- **Televizoarele smart, routerele, casetele NAS și instrumentele de automatizare** care acceptă FTP se pot conecta în același fel.

Îndreaptă-le către adresa Wi-Fi a iPhone-ului tău, portul **2121** și autentificarea ta (sau Anonymous), folosind adresa afișată în Everdisk.

## Doar citire sau citire și scriere

Comutatorul **Editarea fișierelor** din Setări, Partajare, Acces controlează acest lucru. Activat le permite oamenilor să încarce, redenumească și șteargă. Dezactivat înseamnă că pot doar să descarce. Alege doar citire când oferi fișiere și nu vrei să se modifice nimic pe telefonul tău.

## Moduri reale în care oamenii folosesc asta

- **Conectează FileZilla la iPhone-ul tău** și împinge un lot de fișiere pe telefon dintr-o singură mișcare.
- **Lasă o aplicație sau un dispozitiv vechi care vorbește doar FTP** să ajungă la fișierele tale când nimic altceva nu se conectează.
- **Primește fotografii de la o cameră** care încarcă prin FTP.
- **Mută fișiere între un iPhone și un iPad** folosind fila Dispozitive din Everdisk de pe dispozitivul care primește.

## Câteva sfaturi

- Ține Everdisk deschis cât timp un dispozitiv este conectat, întrucât iOS pune pe pauză aplicațiile din fundal după o vreme.
- Pentru a încărca de pe un Mac, folosește FileZilla sau Cyberduck în loc de Finder, pentru că Finder deschide FTP doar pentru citire.
- Lasă autentificarea goală pentru cea mai largă compatibilitate, apoi conectează-te ca Anonymous, ceea ce majoritatea clienților FTP oferă.
- FTP nu își criptează traficul. Într-o rețea în care nu ai încredere, folosește în schimb [serverul SMB cu criptare](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/).

## Întrebări frecvente

{{% details title="Care este adresa și portul FTP pentru iPhone-ul meu?" closed="true" %}}
După ce începi partajarea, Everdisk afișează adresa pe ecranul Partajare. Arată ca ftp://192.168.1.20:2121. 2121 este portul pe care Everdisk îl folosește pentru FTP, iar prima parte este adresa iPhone-ului tău în rețeaua Wi-Fi, așa că a ta va fi diferită.
{{% /details %}}

{{% details title="Cum conectez FileZilla sau Cyberduck la iPhone-ul meu?" closed="true" %}}
Deschide aplicația și creează o nouă conexiune. Setează Host-ul la adresa Wi-Fi a iPhone-ului tău și Port-ul la 2121. Introdu Utilizator și Parolă sau alege Anonymous dacă nu ai setat una în Everdisk. Conectează-te și poți trage fișiere în ambele direcții când Editarea fișierelor este activată.
{{% /details %}}

{{% details title="Mă pot conecta la iPhone-ul meu FTP de pe Windows?" closed="true" %}}
Da. Deschide File Explorer, fă clic pe bara de adrese, tastează adresa FTP din Everdisk (de exemplu ftp://192.168.1.20:2121) și apasă Enter. Introdu autentificarea ta dacă ai setat una sau continuă ca invitat. Pentru încărcări și mai mult control, folosește în schimb o aplicație FTP precum FileZilla.
{{% /details %}}

{{% details title="Am nevoie de o autentificare pentru FTP?" closed="true" %}}
Nu, autentificarea este opțională. Lasă Utilizator și Parolă goale în Setări, Partajare, Acces și conectează-te ca Anonymous, ceea ce majoritatea clienților FTP oferă. Setează o autentificare dacă vrei ca conexiunile să se autentifice mai întâi.
{{% /details %}}

{{% details title="De ce pot doar să descarc și nu să încarc prin FTP?" closed="true" %}}
Două motive sunt frecvente. Primul, comutatorul Editarea fișierelor din Setări, Partajare, Acces trebuie să fie activat pentru a permite încărcări, redenumiri și ștergeri. Al doilea, Mac Finder deschide FTP doar pentru citire, așa că folosește o aplicație FTP precum FileZilla sau Cyberduck când vrei să încarci.
{{% /details %}}

{{% details title="Pot folosi FTP între două iPhone-uri?" closed="true" %}}
Da. Pornește serverul FTP pe primul iPhone. Pe al doilea, deschide Everdisk, mergi la fila Dispozitive, apasă Conexiune nouă, alege FTP și introdu adresa afișată pe primul telefon. Funcționează și o aplicație FTP dedicată pentru iOS, întrucât aplicația Files din iOS nu include un client FTP.
{{% /details %}}

{{% details title="FTP este sigur?" closed="true" %}}
FTP simplu nu își criptează traficul, așa că tratează-l ca pe un instrument pentru rețele în care ai încredere, precum Wi-Fi-ul de acasă. Într-o rețea pe care nu o controlezi, folosește serverul SMB cu Solicită criptare SMB activat, care protejează fiecare transfer.
{{% /details %}}

{{% details title="Ce dispozitive se pot conecta prin FTP?" closed="true" %}}
Aproape orice cu un client FTP. Asta include computere Mac, Windows și Linux, aplicații FTP precum FileZilla și Cyberduck, manageri de fișiere Android și echipamente precum camere, televizoare smart, routere, casete NAS și instrumente de automatizare. Această acoperire largă este principalul motiv pentru a alege FTP.
{{% /details %}}

{{% details title="De ce s-a întrerupt conexiunea mea FTP?" closed="true" %}}
iPhone-ul tău este serverul, iar iOS pune pe pauză aplicațiile care stau prea mult în fundal. Ține Everdisk deschis pe ecran cât timp un dispozitiv este conectat și conectează-l la sursa de alimentare pentru transferuri lungi. De asemenea, asigură-te că ambele dispozitive sunt încă în aceeași rețea Wi-Fi.
{{% /details %}}

{{% details title="Everdisk este gratuit?" closed="true" %}}
Da, Everdisk se descarcă gratuit, iar serverul FTP este inclus. O achiziție opțională unică Premium adaugă suplimente precum porturi personalizate și conversia fotografiilor și videoclipurilor. Poți configura FTP și transfera fișiere fără să plătești.
{{% /details %}}

Gata să încerci? [Descarcă Everdisk din App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) și conectează primul tău client FTP în câteva minute. Întrebări sau feedback? Scrie-ne la **support@everappz.com**.
