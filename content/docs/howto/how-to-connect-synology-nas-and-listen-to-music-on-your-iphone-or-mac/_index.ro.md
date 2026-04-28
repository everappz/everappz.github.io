---
title: "Cum să conectezi Synology NAS și să asculți muzică pe iPhone sau Mac"
date: 2024-09-19
description: "Află cum să conectezi Synology NAS folosind API-ul nativ sau QuickConnect și să transmiți muzică de înaltă calitate pe iPhone sau Mac cu Evermusic și Flacbox."
keywords: ["synology nas", "transmitere muzică", "quickconnect", "evermusic synology", "flacbox synology", "player muzică nas", "muzică nas iphone"]
tags: ["muzică", "transmitere", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Rezumat:** Conectează-ți Synology NAS la Evermusic sau Flacbox folosind API-ul nativ Synology -- fie manual prin adresa IP, fie automat prin QuickConnect ID. QuickConnect îți permite să transmiți muzică de la distanță fără redirecționarea porturilor. Ambele aplicații suportă FLAC, MP3, WAV și alte formate hi-res.

Dacă cauți o modalitate simplă de a-ți conecta Synology NAS și de a te bucura de biblioteca ta de muzică pe iPhone sau Mac, aplicațiile Evermusic și Flacbox sunt soluțiile perfecte. Aceste aplicații suportă o gamă largă de formate audio, inclusiv FLAC, MP3 și WAV, facilitând transmiterea și ascultarea muzicii de înaltă calitate direct de pe Synology NAS.

În acest ghid, îți vom arăta cum să-ți conectezi Synology NAS la aplicația Evermusic sau Flacbox folosind API-ul nativ Synology și funcția QuickConnect. Prin utilizarea API-ului direct Synology, poți accesa în siguranță biblioteca ta de muzică în afara rețelei de acasă fără a avea nevoie de configurații complicate precum WebDAV, SMB, DLNA. Cu QuickConnect, vei putea transmite și gestiona muzica ta de oriunde, folosind iPhone-ul sau Mac-ul tău.

## Pasul 1: Configurează permisiunile folderului partajat (opțional)

1. Deschide **Panoul de control** și mergi la secțiunea **Folder partajat**.

![Folder partajat](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Selectează folderul **Music** și apasă **Editare**.

3. În fila **Permisiuni**, configurează permisiunile. Activează accesul pentru oaspeți cu Doar citire dacă trebuie doar să asculți muzică, sau Citire/Scriere dacă trebuie să modifici fișiere. Salvează modificările.

![Permisiuni](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Pasul 2: Găsește adresa IP a Synology NAS

1. Deschide **Panoul de control** și mergi la fila **Interfață de rețea**.

![Interfață de rețea](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Sau folosește browserul web pentru a vizita [find.synology.com](http://find.synology.com).

![Găsește Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Notează adresa IP a Synology NAS (de ex., 192.168.18.137).

## Pasul 3: Găsește porturile de rețea ale Synology NAS

Poți găsi documentația oficială Synology pentru porturile de rețea implicite DSM în acest [articol din Centrul de cunoștințe Synology](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM folosește următoarele porturi implicite:
- **HTTP (Acces web):** Portul **5000**
- **HTTPS (Acces web securizat):** Portul **5001**

Acestea sunt porturile implicite pentru accesarea interfeței DSM.

![Porturi de rețea](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Pasul 4: Activează funcția QuickConnect ID

Un Synology QuickConnect ID este un identificator unic care îți permite să accesezi Synology NAS de la distanță prin internet fără a fi nevoie să configurezi setări de rețea complicate precum redirecționarea porturilor. QuickConnect simplifică accesul de la distanță prin utilizarea serverelor Synology pentru a stabili o conexiune între NAS și dispozitivul tău, cum ar fi smartphone-ul sau computerul, prin QuickConnect ID.

**Cum să găsești sau să configurezi QuickConnect ID:**

1. **Conectează-te la DSM.**
2. Mergi la **Panou de control > Acces extern > QuickConnect**.
3. **Activează QuickConnect** și creează sau vizualizează QuickConnect ID-ul tău unic.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Pasul 5: Conectează-te la Synology NAS pe iPhone/Mac folosind Evermusic sau Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) și [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) sunt ambele aplicații player de muzică proiectate pentru dispozitive iOS și macOS, fiecare oferind caracteristici și capabilități unice pentru gestionarea și bucuria bibliotecii tale de muzică.

1. Deschide aplicația Evermusic sau Flacbox și mergi la fila **Conexiuni**.

![Conexiuni](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Alege **Conectează un serviciu cloud** și selectează **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Ai două opțiuni de conectare: **manuală** folosind adresa IP și portul serverului, sau **automată** prin QuickConnect ID.

### Conexiune manuală

Pentru metoda manuală, vei avea nevoie de adresa IP directă și numărul portului obținute în pașii anteriori.

1. Introdu URL-ul serverului obținut la pasul 2, folosind următorul format: PROTOCOL://ADRESĂ_IP:NUMĂR_PORT
   - Folosește **portul 5000** pentru HTTP și **portul 5001** pentru conexiuni HTTPS.

   De exemplu:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Numărul real al portului poate fi confirmat la pasul 3 al configurării.
3. Introdu **numele de utilizator** și **parola** pentru Synology NAS.
4. Apasă **Conectare** pentru a stabili conexiunea.

![Conexiune manuală](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Conexiune automată

Pentru conexiunea automată, vei folosi **QuickConnect ID** de la pasul 4. În loc să introduci manual adresa IP și numărul portului pentru Synology NAS, pur și simplu introdu **QuickConnect ID**. Aplicația va prelua automat informațiile de conexiune necesare.

Această metodă îți permite să accesezi NAS de la distanță, chiar și în afara rețelei de acasă, astfel încât să poți gestiona fișierele de pe internet fără a configura redirecționarea porturilor sau adresele IP statice.

![Conexiune automată](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Autentificare cu doi factori

Începând cu DSM 4.2, Synology a introdus **verificarea în doi pași** pentru a îmbunătăți securitatea. Această funcție necesită un cod de **parolă unică (OTP)**, generat de o aplicație de autentificare, pe lângă datele tale obișnuite de conectare. Dacă ai activat verificarea în doi pași, după introducerea numelui de utilizator și a parolei, va trebui să introduci și OTP-ul pentru a te conecta la sesiunea DSM.

Te rugăm să reții că, odată ce sesiunea expiră, aplicația va trebui reautorizată manual. Pentru a reautoriza:

1. Mergi la fila **Conexiuni** din aplicație.
2. Apasă butonul **Mai multe acțiuni** de lângă numele serverului.
3. Selectează **Setări** din meniu pentru a introduce noul cod de autentificare și a finaliza procesul de reautorizare.

Aceasta asigură că, chiar dacă accesezi NAS dintr-o rețea nesigură, datele tale rămân în siguranță.

## Pasul 6: Navighează și redă muzică

1. Odată conectat, dispozitivul va apărea în lista **Dispozitive conectate**.

![Dispozitive conectate](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Navighează la folderul **Music** și apasă pe orice fișier audio pentru a începe redarea.

![Redă muzică](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Pasul 7: Adaugă folderul cloud conectat la biblioteca de muzică

1. Deschide secțiunea **Bibliotecă de muzică** din aplicație.
2. Alege **Adaugă muzică** și selectează **Conexiuni**.
3. Alege serverul NAS conectat și selectează folderul **Music**. Apasă **Finalizat**.
4. Aplicația va scana folderul de muzică și va adăuga fișierele audio suportate în biblioteca de muzică. Metadatele vor fi încărcate, iar piesele tale vor fi grupate după album, artist și gen.

## Concluzie

Urmând acești pași, poți configura cu ușurință o conexiune pe Synology NAS și transmite întreaga ta bibliotecă de muzică pe iPhone sau Mac folosind Evermusic sau Flacbox. Fie că ești acasă sau în mișcare, bucură-te de acces fără întreruperi și de înaltă calitate la piesele tale preferate de oriunde folosind QuickConnect. Profită de flexibilitatea și comoditatea pe care aceste aplicații le oferă și începe să-ți gestionezi colecția de muzică cu ușurință pe toate dispozitivele tale.

Cu acces securizat de la distanță prin QuickConnect și suport pentru o gamă largă de formate audio, nu vei fi niciodată departe de muzica ta. Acum, fișierele stocate pe NAS sunt la doar o apăsare distanță!

## FAQ

{{% details title="Care este diferența dintre conexiunea manuală și QuickConnect?" closed="true" %}}
Conexiunea manuală folosește adresa IP și portul NAS, care funcționează în rețeaua ta locală. QuickConnect folosește serviciul de releu Synology pentru a stabili o conexiune de oriunde prin internet, fără redirecționarea porturilor.
{{% /details %}}

{{% details title="Pot transmite muzică de pe Synology NAS în afara rețelei de acasă?" closed="true" %}}
Da. Activează QuickConnect pe Synology NAS și folosește QuickConnect ID în Evermusic sau Flacbox pentru a transmite muzică de oriunde cu o conexiune la internet.
{{% /details %}}

{{% details title="Ce formate audio sunt suportate la transmiterea de pe Synology NAS?" closed="true" %}}
Evermusic și Flacbox suportă FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD și multe alte formate. Toate formatele suportate funcționează la transmiterea de pe Synology NAS.
{{% /details %}}

{{% details title="Am nevoie de autentificare cu doi factori pentru a mă conecta?" closed="true" %}}
Nu, 2FA este opțional. Totuși, dacă ai activat verificarea în doi pași pe Synology DSM, aplicația va cere o parolă unică în timpul conectării. Va trebui să reautorizezi când sesiunea expiră.
{{% /details %}}

{{% details title="Ar trebui să folosesc API-ul nativ Synology, WebDAV sau SMB pentru conectare?" closed="true" %}}
API-ul nativ Synology cu QuickConnect este cea mai bună alegere pentru accesul de la distanță. Pentru utilizarea în rețeaua locală, SMB este de obicei cea mai rapidă opțiune. WebDAV funcționează bine atât pentru accesul local, cât și pentru cel de la distanță. Evermusic și Flacbox suportă toate cele trei protocoale.
{{% /details %}}
