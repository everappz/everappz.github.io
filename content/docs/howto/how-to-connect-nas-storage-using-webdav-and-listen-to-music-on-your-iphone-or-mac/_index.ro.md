---
title: "Cum să conectezi stocarea NAS folosind WebDAV și să asculți muzică pe iPhone sau Mac"
date: 2024-07-28
description: "Învață cum să configurezi WebDAV pe Synology NAS și să transmiți muzică pe iPhone sau Mac folosind Evermusic sau Flacbox. Urmează ghidul nostru pas cu pas."
keywords: ["conectare nas", "webdav synology", "transmite muzică nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["muzică", "streaming", "stocare", "nas", "conectare", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Pe scurt:** Instalează și activează WebDAV pe Synology NAS, configurează permisiunile folderului partajat, apoi conectează-te din Evermusic sau Flacbox folosind adresa IP a NAS-ului și portul WebDAV (implicit 5005/5006). Poți transmite și gestiona întreaga bibliotecă muzicală fără să copiezi fișiere pe dispozitiv.

Descoperă cum să conectezi stocarea NAS folosind WebDAV și să transmiți fără efort biblioteca muzicală pe iPhone sau Mac. WebDAV (Web-based Distributed Authoring and Versioning) este un protocol care îți permite să gestionezi și să partajezi fișiere prin Internet. Configurând WebDAV pe NAS, poți accesa și transmite colecția ta muzicală, asigurându-te că melodiile tale preferate sunt mereu la îndemână.

În acest ghid, îți vom arăta cum să configurezi o conexiune WebDAV pe unul dintre cele mai populare servere NAS, Synology NAS. Urmează pașii noștri simpli pentru a configura WebDAV pe Synology NAS și vei putea naviga, transmite și gestiona biblioteca muzicală direct de pe iPhone sau Mac.

## Pasul 1: Instalează WebDAV pe Synology NAS

1. Conectează-te la Synology NAS și deschide **Centrul de pachete**.
2. Caută "webdav" și instalează pachetul WebDAV dacă nu este deja instalat. Deschide serverul WebDAV pentru a-l configura.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Instalare WebDAV pe Synology" width="600" >}}

## Pasul 2: Configurează serverul WebDAV

1. Pe pagina de setări WebDAV, bifează casetele pentru **Activare HTTP**, **Activare HTTPS**, **Activare WebDAV anonim** și **Activare DavDepthInfinity**.
2. Apasă **Aplică** pentru a salva modificările. Notează numerele de port pentru conexiunile HTTP și HTTPS, care sunt 5005 și 5006 implicit.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Configurare setări WebDAV" width="600" >}}

## Pasul 3: Configurează permisiunile folderului partajat

1. Deschide **Panoul de control** și navighează la secțiunea **Folder partajat**.
2. Selectează folderul **Muzică** și apasă **Editare**.
3. În fila **Permisiuni**, configurează permisiunile. Activează accesul pentru oaspeți cu Doar citire dacă trebuie doar să asculți muzică, sau Citire/Scriere dacă trebuie să modifici fișiere. Salvează modificările.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Permisiuni folder partajat" width="600" >}}

## Pasul 4: Găsește adresa IP a Synology NAS

1. Deschide **Panoul de control** și navighează la fila **Interfață de rețea**, sau folosește browserul web pentru a vizita [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Găsire adresă IP NAS" width="600" >}}

2. Notează adresa IP a Synology NAS (de ex., 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Adresa IP Synology NAS" width="600" >}}

## Pasul 5: Conectare la Synology NAS folosind Evermusic/Flacbox

1. Deschide aplicația Evermusic sau Flacbox și navighează la fila **Conexiuni**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Fila Conexiuni în Evermusic" width="600" >}}

2. Pentru conexiune automată, găsește Synology NAS în secțiunea **Dispozitive disponibile** și atinge-l pentru a te conecta.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Lista dispozitivelor disponibile" width="600" >}}

3. Pentru conexiune manuală, alege **Conectare serviciu cloud** și selectează **WebDAV**. Introdu adresa serverului în formatul: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (de ex., [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Configurare manuală WebDAV" width="600" >}}

4. Lasă câmpurile de autentificare și parolă goale pentru accesul ca oaspete, sau introdu credențialele Synology. Atinge **Conectare**.

## Pasul 6: Navigare și redare muzică

1. După conectare, dispozitivul va apărea în lista **Accesorii conectate**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Dispozitive conectate în Evermusic" width="600" >}}

2. Navighează la folderul **Muzică** și atinge orice fișier audio pentru a începe redarea.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Navigare în folderul de muzică" width="600" >}}

## Pasul 7: Adaugă folderul cloud conectat la biblioteca muzicală

1. Deschide secțiunea **Bibliotecă muzicală** în aplicație.
2. Alege **Adaugă muzică** și selectează **Conexiuni**.
3. Alege serverul NAS conectat și selectează folderul **Muzică**. Atinge **Finalizat**.
4. Aplicația va scana folderul de muzică și va adăuga fișierele audio compatibile în biblioteca muzicală. Metadatele vor fi încărcate, iar piesele tale vor fi grupate după album, artist și gen.

## Concluzie

Urmând acești pași, poți configura cu ușurință o conexiune WebDAV pe Synology NAS și transmite biblioteca muzicală pe iPhone sau Mac folosind Evermusic sau Flacbox. Bucură-te de acces fluid la melodiile tale preferate oricând.

## Întrebări frecvente

{{% details title="Ce dispozitive NAS suportă WebDAV?" closed="true" %}}
Majoritatea brandurilor populare de NAS suportă WebDAV, inclusiv Synology, QNAP, TrueNAS și Western Digital. Verifică documentația producătorului NAS-ului tău pentru instrucțiuni de configurare WebDAV.
{{% /details %}}

{{% details title="Care este diferența dintre WebDAV și SMB pentru streaming de muzică de pe NAS?" closed="true" %}}
WebDAV funcționează prin HTTP/HTTPS și este mai potrivit pentru acces la distanță prin internet. SMB este de obicei mai rapid pe rețelele locale. Evermusic și Flacbox suportă ambele protocoale, deci alege în funcție de necesitatea accesului local sau la distanță.
{{% /details %}}

{{% details title="Am nevoie de nume de utilizator și parolă pentru WebDAV pe Synology?" closed="true" %}}
Nu, dacă activezi accesul anonim WebDAV și configurezi permisiunile de oaspete pe folderul partajat. Pentru o securitate mai bună, poți folosi credențialele Synology.
{{% /details %}}

{{% details title="Pot transmite FLAC și alte formate de înaltă rezoluție de pe NAS prin WebDAV?" closed="true" %}}
Da. Atât Evermusic, cât și Flacbox suportă FLAC, ALAC, WAV, DSD și alte formate de înaltă rezoluție la transmiterea de pe stocarea NAS prin WebDAV.
{{% /details %}}

{{% details title="De ce aplicația nu poate găsi NAS-ul meu în Dispozitive disponibile?" closed="true" %}}
Asigură-te că iPhone-ul/Mac-ul și NAS-ul sunt pe aceeași rețea Wi-Fi. Dacă descoperirea automată nu funcționează, folosește opțiunea de conexiune manuală și introdu adresa IP a NAS-ului și portul WebDAV direct.
{{% /details %}}
