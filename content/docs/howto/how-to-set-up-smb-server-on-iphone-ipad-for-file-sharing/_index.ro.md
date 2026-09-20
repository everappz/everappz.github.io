---
title: "Cum configurezi un server SMB pe iPhone și iPad pentru partajarea fișierelor"
description: "Transformă-ți iPhone-ul sau iPad-ul într-un server de fișiere SMB cu Everdisk și deschide-l ca un disc de rețea de pe un Mac, un alt iPhone, Linux sau Android prin Wi-Fi. Configurare completă, adresa și portul smb, criptare SMB3 opțională și conectare pas cu pas pentru fiecare dispozitiv."
date: 2026-09-19
tags: ["everdisk", "smb", "partajare fisiere", "disc de retea", "iphone", "ipad", "mac", "finder", "criptare", "wifi"]
keywords: ["server SMB iPhone", "server SMB iPad", "cum configurez SMB pe iPhone", "partajare SMB iPhone", "conectare iPhone SMB Mac Finder", "smb iphone la iphone", "aplicatie Files iOS conectare la server SMB", "partajare fisiere iPhone SMB", "disc de retea iphone Finder", "criptare SMB3 iOS", "partajare smb iPhone Android", "conectare la SMB de pe Linux", "iphone ca disc de retea", "partajare fisiere intre iphone-uri wifi", "mapare iphone ca disc de retea"]
readingTime: 10
---

{{< author-byline >}}

SMB este sistemul de partajare a fișierelor integrat în macOS, Windows și Linux și în aproape orice disc de rețea (NAS). Când te conectezi la un folder partajat de pe un alt computer și acesta se deschide ca un disc obișnuit în Finder sau File Explorer, SMB este cel care face treaba. Cu [Everdisk](/products/everdisk) poți pune o partajare SMB pe iPhone-ul sau iPad-ul tău, astfel încât telefonul însuși apare ca un disc de rețea pe care alte dispozitive îl răsfoiesc, din care copiază și în care copiază.

Aceasta este opțiunea de ales când vrei ca iPhone-ul tău să se comporte ca un disc adevărat, nu ca o pagină web. Este rapidă, trage și plasează în ambele sensuri și este singurul tip de conexiune din Everdisk care poate cripta fiecare transfer. Acest ghid acoperă configurarea și cum te conectezi de pe un Mac, un alt iPhone sau iPad, Linux, Android și Windows.

## De ce ai nevoie

- Un iPhone sau iPad cu [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) instalat.
- Un alt dispozitiv în **aceeași rețea Wi-Fi**.
- Fișierele pe care vrei să le partajezi, în folderul Documente al Everdisk sau în foldere pe care le adaugi.

## Configurează serverul SMB în Everdisk

### Pasul 1: Alege ce partajezi și cine poate scrie

Deschide Everdisk, mergi la fila **Partajare** și apasă **Ce partajezi**. Folderul Documente este partajat implicit. Adaugă mai multe cu **Adaugă folder** și **Adaugă fișier** și activează-ți biblioteca Photos sau Music dacă vrei să fie disponibile și acestea.

Decide dacă alte dispozitive pot doar să-ți citească fișierele sau și să le modifice. Deschide **Setări**, apoi **Partajare**, apoi **Acces** și setează **Editarea fișierelor**. Cu ea activată, dispozitivele conectate pot copia fișiere pe telefonul tău și le pot redenumi sau șterge. Cu ea dezactivată, partajarea este doar pentru citire.

Dacă vrei o autentificare, setează un **Utilizator** și o **Parolă** pe același ecran Acces. Lasă-le pe ambele goale pentru a permite accesul ca invitat.

### Pasul 2: Activează serverul SMB

Mergi la **Setări**, apoi **Partajare**, apoi **Conexiuni** și activează **Computer (avansat)**. Acesta este serverul SMB (poartă eticheta SMB).

### Pasul 3: Începe partajarea și notează adresa

Mergi înapoi la fila **Partajare** și apasă **Start**. Secțiunea **Cum te conectezi** afișează acum adresa SMB. Arată așa:

```
smb://192.168.1.20:4455/Share
```

Trei lucruri de știut despre acea adresă:

- Numărul de după două puncte este **portul**. Everdisk folosește implicit **4455**.
- Partajarea se numește **Share**.
- Prima parte este adresa iPhone-ului tău în rețeaua Wi-Fi, așa că va fi diferită în rețeaua ta.

Ține Everdisk deschis cât timp dispozitivele sunt conectate, pentru că iOS pune pe pauză aplicațiile care stau prea mult în fundal.

## Conectează-te de pe un Mac

Acesta este cazul cel mai fluent, pentru că macOS vorbește SMB nativ.

Cea mai rapidă cale: deschide **Finder** și caută în bara laterală sub **Locations** sau **Network**. Everdisk se anunță în rețeaua Wi-Fi, așa că iPhone-ul tău apare adesea acolo de la sine. Fă clic pe el, apoi apasă **Connect As** și alege **Guest** sau introdu autentificarea ta.

Pentru a te conecta manual:

1. În Finder, alege **Go**, apoi **Connect to Server** (sau apasă **Command și K**).
2. Tastează adresa SMB afișată în Everdisk, de exemplu `smb://192.168.1.20:4455/Share`.
3. Apasă **Connect**, apoi alege **Guest** sau introdu **Utilizator** și **Parolă**.

iPhone-ul tău se deschide într-o fereastră Finder. Copiază fișiere înăuntru sau afară prin tragere, exact ca la orice alt disc (dacă Editarea fișierelor este activată).

## Conectează-te de pe un alt iPhone sau iPad

iOS și iPadOS pot deschide partajări SMB în aplicația integrată **Files**, ceea ce face transferurile de la telefon la telefon curate și rapide.

Pe al doilea dispozitiv:

1. Deschide aplicația **Files**.
2. Apasă butonul **more** (cele trei puncte, dreapta sus pe iPhone) și alege **Connect to Server**.
3. Introdu adresa SMB din Everdisk, de exemplu `smb://192.168.1.20:4455/Share`.
4. Alege **Guest** sau **Registered User** și introdu autentificarea ta.
5. Partajarea apare sub Locations în Files. Răsfoiește și copiază în oricare direcție.

Poți folosi și fila proprie **Dispozitive** din Everdisk de pe al doilea dispozitiv, care include un client SMB. Deschide Everdisk, mergi la **Dispozitive**, apasă **Conexiune nouă**, alege **SMB** și introdu adresa.

## Conectează-te de pe Linux

1. Deschide managerul tău de fișiere (Files/Nautilus pe GNOME, Dolphin pe KDE).
2. Alege **Other Locations** sau **Connect to Server**.
3. Introdu adresa, de exemplu `smb://192.168.1.20:4455/Share`.
4. Conectează-te ca invitat sau introdu autentificarea ta.

Dintr-un terminal poți rula și `smbclient //192.168.1.20/Share -p 4455` și introduce autentificarea ta când ți se cere.

## Conectează-te de pe Android

Android nu are un navigator SMB de sistem, așa că folosește un manager de fișiere care acceptă SMB:

1. Instalează o aplicație precum **CX File Explorer**, **Solid Explorer** sau **X-plore File Manager**.
2. Adaugă o nouă conexiune **SMB** sau **LAN**.
3. Introdu gazda (adresa Wi-Fi a iPhone-ului tău), setează **portul la 4455** și numele partajării **Share**.
4. Conectează-te ca invitat sau cu autentificarea ta, apoi răsfoiește și copiază.

## Conectează-te de pe Windows

Windows poate citi partajări SMB, cu o singură captură pe care merită să o știi din start. File Explorer integrat comunică cu SMB doar pe portul standard și nu îți permite să tastezi un port personalizat în cale, iar Everdisk folosește portul 4455. Așa că ruta simplă **Map network drive** adesea nu îl va ajunge.

Ai două opțiuni bune pe Windows:

- Folosește un manager de fișiere sau un client SMB care îți permite să setezi un port personalizat și îndreaptă-l către adresa iPhone-ului tău cu portul **4455** și numele partajării **Share**.
- Sau conectează-te de pe Windows folosind în schimb unul dintre celelalte servere ale Everdisk. [Configurarea WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) și [configurarea FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) funcționează amândouă bine din Windows File Explorer, iar link-ul de browser funcționează în orice browser.

Dacă totuși vrei să încerci Map network drive: deschide **File Explorer**, fă clic dreapta pe **This PC**, alege **Map network drive** și introdu gazda și numele partajării afișate în Everdisk. Dacă nu se poate conecta, este limitarea de port de mai sus, așa că treci la WebDAV sau FTP.

## Activează criptarea pentru Wi-Fi în care nu ai încredere

SMB este singura conexiune Everdisk care poate cripta fiecare transfer, ceea ce contează pe un Wi-Fi pe care nu îl controlezi complet, precum o cafenea sau o rețea de birou.

1. În **Setări**, **Partajare**, **Acces**, setează un **Utilizator** și o **Parolă**. Conexiunile criptate nu pot fi anonime, așa că acest pas este obligatoriu.
2. În **Setări**, **Partajare**, activează **Solicită criptare SMB**.
3. Oprește și repornește partajarea, astfel încât modificarea să aibă efect.

Fiecare transfer SMB este apoi protejat cu **criptare SMB3 (AES)**. Dispozitivul care se conectează trebuie să accepte SMB3, ceea ce Finder-ul de pe un Mac modern și Windows 10 sau versiunile ulterioare fac amândouă. Criptarea SMB face parte din achiziția unică Premium.

## Doar citire sau citire și scriere

Comutatorul **Editarea fișierelor** din Setări, Partajare, Acces controlează acest lucru pentru fiecare server, inclusiv SMB. Activează-l și dispozitivele conectate pot încărca, redenumi și șterge. Dezactivează-l și pot doar să răsfoiască și să copieze fișiere de pe telefonul tău. Alege doar citire când oferi fișiere cuiva pe care nu vrei să modifice nimic.

## Moduri reale în care oamenii folosesc asta

- **Mută un folder mare pe iPhone de pe un Mac** trăgându-l în fereastra Finder, mai rapid decât o încărcare web.
- **Extrage o zi de fotografii și videoclipuri de pe telefonul tău** pe un laptop fără iTunes sau un cablu.
- **Trimite fișiere între două iPhone-uri** prin aplicația Files, fără o a treia aplicație pe vreo parte.
- **Lucrează cu un fișier pe loc**, deschizând un document direct de pe telefon într-o aplicație de pe Mac-ul tău și salvându-l înapoi.

## Câteva sfaturi

- Ține Everdisk deschis cât timp un dispozitiv este conectat. Blocarea telefonului mult timp poate pune aplicația pe pauză și poate întrerupe conexiunea.
- Dacă un Mac nu poate vedea telefonul în bara laterală Finder, conectează-te manual cu Connect to Server și adresa smb completă.
- Pentru cea mai bună viteză la transferuri mari, ține calitatea fotografiilor și videoclipurilor pe Original în Setări.
- Într-o rețea în care nu ai încredere, activează Solicită criptare SMB și dezactivează celelalte servere cât timp lucrezi.

## Întrebări frecvente

{{% details title="Care este adresa și portul SMB pentru iPhone-ul meu?" closed="true" %}}
După ce începi partajarea, Everdisk afișează adresa pe ecranul Partajare. Arată ca smb://192.168.1.20:4455/Share. 4455 este portul pe care Everdisk îl folosește pentru SMB, iar Share este numele folderului partajat. Prima parte este adresa iPhone-ului tău în rețeaua Wi-Fi, așa că a ta va fi diferită.
{{% /details %}}

{{% details title="Mă pot conecta la partajarea SMB a iPhone-ului meu de pe Windows?" closed="true" %}}
Windows File Explorer se conectează la SMB doar pe portul standard și nu acceptă un port personalizat în cale, în timp ce Everdisk folosește portul 4455. Așa că ruta simplă Map network drive adesea nu îl va ajunge. Folosește un manager de fișiere care îți permite să setezi un port personalizat sau conectează-te de pe Windows cu WebDAV, FTP sau link-ul de browser. Toate acestea funcționează de pe Windows fără nicio problemă de port.
{{% /details %}}

{{% details title="Cum partajez fișiere între două iPhone-uri cu SMB?" closed="true" %}}
Pornește serverul SMB pe primul iPhone în Everdisk. Pe al doilea iPhone, deschide aplicația Files, apasă butonul more, alege Connect to Server și introdu adresa smb afișată în Everdisk (de exemplu smb://192.168.1.20:4455/Share). Conectează-te ca Guest sau cu autentificarea ta, iar partajarea apare în Files. Poți folosi și fila proprie Dispozitive din Everdisk de pe al doilea telefon.
{{% /details %}}

{{% details title="Apare iPhone-ul meu automat în bara laterală Finder de pe Mac?" closed="true" %}}
De obicei da. Everdisk anunță partajarea SMB în rețeaua ta Wi-Fi, așa că iPhone-ul tău apare adesea sub Locations sau Network în bara laterală Finder. Fă clic pe el și alege Connect As, apoi Guest sau autentificarea ta. Dacă nu apare, conectează-te manual cu Go, Connect to Server și adresa smb completă.
{{% /details %}}

{{% details title="Am nevoie de o parolă pentru a folosi SMB?" closed="true" %}}
Nu, autentificarea este opțională. Lasă Utilizator și Parolă goale în Setări, Partajare, Acces pentru a permite accesul ca invitat. Setează-le dacă vrei ca conexiunile să se autentifice. Un utilizator și o parolă sunt obligatorii doar dacă activezi Solicită criptare SMB, pentru că conexiunile criptate nu pot fi anonime.
{{% /details %}}

{{% details title="Conexiunea SMB este criptată?" closed="true" %}}
Poate fi. SMB este singura conexiune Everdisk care acceptă criptare. Setează un utilizator și o parolă, apoi activează Solicită criptare SMB în Setări, Partajare. Fiecare transfer este apoi protejat cu SMB3 (AES). Celălalt dispozitiv trebuie să accepte SMB3, ceea ce Mac-urile moderne și Windows 10 sau versiunile ulterioare fac. Criptarea este o funcție Premium.
{{% /details %}}

{{% details title="Pot oamenii să-mi modifice sau șteargă fișierele prin SMB?" closed="true" %}}
Doar dacă permiți asta. Comutatorul Editarea fișierelor din Setări, Partajare, Acces controlează acest lucru. Cu el activat, dispozitivele conectate pot încărca, redenumi și șterge. Cu el dezactivat, partajarea este doar pentru citire, iar ceilalți pot răsfoi și copia fișiere de pe telefonul tău, dar nu pot modifica nimic.
{{% /details %}}

{{% details title="De ce s-a întrerupt conexiunea mea SMB?" closed="true" %}}
iPhone-ul tău este serverul, iar iOS pune pe pauză aplicațiile care stau prea mult în fundal. Ține Everdisk deschis pe ecran cât timp un dispozitiv este conectat și conectează telefonul la sursa de alimentare în timpul transferurilor lungi. De asemenea, asigură-te că ambele dispozitive au rămas în aceeași rețea Wi-Fi.
{{% /details %}}

{{% details title="SMB, WebDAV sau FTP, pe care ar trebui să îl folosesc?" closed="true" %}}
Folosește SMB când vrei ca telefonul să se comporte ca un disc de rețea adevărat pe un Mac, un alt iPhone, Linux sau un NAS și când vrei criptare. Folosește WebDAV când vrei un disc de rețea care funcționează bine și de pe Windows. Folosește FTP pentru cea mai largă compatibilitate cu dispozitive și aplicații mai vechi. Everdisk le poate rula pe toate deodată, așa că nu ești blocat într-una singură.
{{% /details %}}

{{% details title="Everdisk este gratuit?" closed="true" %}}
Da, Everdisk se descarcă gratuit, iar serverul SMB este inclus. Achiziția opțională unică Premium adaugă criptare SMB, porturi personalizate și câteva alte suplimente. Poți configura SMB și partaja fișiere fără să plătești.
{{% /details %}}

Gata să încerci? [Descarcă Everdisk din App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) și deschide-ți iPhone-ul în Finder în aproximativ un minut. Întrebări sau feedback? Scrie-ne la **support@everappz.com**.
