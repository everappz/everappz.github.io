---
title: "Evervideo 1.7: Plex, Jellyfin noi, streaming din cloud, gesturi de redare"
date: 2026-05-18
description: "Evervideo 1.7 adaugă peste 10 conexiuni noi — Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS — plus gesturi noi de redare (dublu tap pentru derulare, atinge și ține pentru viteză 2x), un Wi-Fi Drive reîmprospătat cu încărcare în loturi și actualizări de UI Liquid Glass pentru iPhone, iPad și Mac."
keywords: ["Evervideo 1.7", "actualizare Evervideo", "player video HD iPhone", "player video Plex iOS", "Jellyfin iPhone video", "player video Emby iOS", "Subsonic video iOS", "Navidrome video iOS", "streaming video Internxt", "player video Proton Drive", "player video QNAP iPhone", "player video Nextcloud iOS", "streaming video Amazon S3", "player video SFTP iPhone", "player video FTP iOS", "streaming video NFS iPhone", "transmite video de pe NAS iPhone", "player MKV iPhone", "gesturi player video iOS", "dublu tap pentru derulare video", "transfer video Wi-Fi Drive iPhone", "design Liquid Glass", "player video în cloud iOS 2026", "transmite filme din cloud iPhone"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Gesturi de redare", "Liquid Glass", "Noutăți"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**Pe scurt:** [Evervideo 1.7](/products/evervideo) este o actualizare majoră pentru playerul video HD pentru iPhone, iPad și Mac. Versiunea adaugă peste 10 conexiuni noi de cloud, NAS și servere media — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, plus cele mai populare servere media **Plex**, **Subsonic**, **Navidrome**, **Jellyfin** și **Emby**, și trei protocoale de rețea: **FTP**, **SFTP** și **NFS**. Noile **gesturi de redare** vă permit să atingeți de două ori pentru a sări înainte sau înapoi, să atingeți și să țineți pentru a rula la 2x și să atingeți o dată pentru a comuta controalele — totul fără a părăsi modul ecran complet. Wi-Fi Drive primește o UI reîmprospătată cu mod de selecție și o coadă de încărcare mai inteligentă. Întreaga aplicație este ajustată pentru noul design **Liquid Glass** de la Apple.

---

## Salutare tuturor!

A sosit o actualizare mare pentru Evervideo. Este una dintre cele mai mari versiuni pe care le-am lansat: **peste 10 conexiuni noi de cloud, server și rețea**, **gesturi de redare** complet noi pentru control mai rapid în ecran complet, o experiență **Wi-Fi Drive** reîmprospătată și o UI ajustată pentru **Liquid Glass** pe iPhone, iPad și Mac.

[Descarcă Evervideo 1.7 din App Store](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) sau actualizează din versiunea ta existentă. Utilizatorii de Mac pot obține [versiunea desktop aici](https://apps.apple.com/app/evervideo/id6743504109).

## Peste 10 conexiuni noi de cloud, NAS și servere media

Evervideo 1.7 extinde ce înseamnă «biblioteca ta video». Dacă filmele, serialele sau înregistrările tale stau într-un cloud în care ai încredere, pe un NAS acasă sau pe un server media auto-găzduit, Evervideo poate acum transmite direct de la ele — fără descărcări, fără conversii, fără re-codificare.

### Cloud axat pe confidențialitate: Internxt și Proton Drive

Dacă îți pasă de criptarea end-to-end și de stocarea zero-knowledge, două dintre cele mai respectate cloud-uri axate pe confidențialitate sunt acum native în Evervideo:

- **Internxt** — cloud spaniol open-source, cu criptare post-cuantică, conform GDPR. Plan gratuit disponibil.
- **Proton Drive** — stocare cu criptare end-to-end de la creatorii Proton Mail și Proton VPN, cu sediul în Elveția. Plan gratuit disponibil cu planuri plătite pentru biblioteci mai mari.

Conectează-te o dată, iar videoclipurile tale sunt transmise prin tunelul criptat — Evervideo nu îți vede niciodată datele în clar, și nici serverul furnizorului.

### Stocare auto-găzduită: QNAP, Nextcloud, Amazon S3

Pentru utilizatorii care își rulează propria infrastructură:

- **QNAP** — conexiune API nativă la dispozitivele QNAP NAS pentru redare video rapidă și fiabilă prin Wi-Fi local sau acces de la distanță. Transmite fișiere MKV 4K direct, fără re-codificare.
- **Nextcloud** — conectează-te la orice instanță Nextcloud, auto-găzduită sau gestionată. Excelent dacă ai migrat deja de la Google Drive sau Dropbox din motive de confidențialitate.
- **Amazon S3** — îndreaptă Evervideo către orice bucket S3 (sau stocare compatibilă S3, precum Backblaze B2, Wasabi, MinIO, Cloudflare R2) și transmite colecția ta direct.

### <a id="media-servers"></a>Servere media: Plex, Subsonic, Navidrome, Jellyfin, Emby

Aceasta e marea știre pentru fanii video-ului auto-găzduit. Evervideo 1.7 transformă iPhone-ul, iPad-ul sau Mac-ul tău într-un client de primă clasă pentru cele mai populare servere media open-source și freemium:

- **Plex** — Plex Media Server este **gratuit** de descărcat și rulat, cu abonament **Plex Pass** opțional pentru funcții precum sincronizare mobilă, transcodare hardware și TV live. Evervideo funcționează atât cu biblioteci gratuite, cât și Plex Pass — transmite întreaga ta colecție de filme și seriale.
- **Subsonic** — serverul original de streaming auto-găzduit. Serverul oficial Subsonic este **plătit** (1 USD/lună după o perioadă de încercare de 30 de zile), iar Evervideo vorbește și API-ul Subsonic cu servere video compatibile.
- **Navidrome** — server modern, ușor, **complet gratuit și open-source**. Implementează API-ul Subsonic. Rulează pe Raspberry Pi, NAS sau orice mașină Linux.
- **Jellyfin** — server media **complet gratuit și open-source** (un fork comunitar al Emby). Gestionează filme, seriale, muzică, cărți și video-uri de acasă. Fără conturi, fără telemetrie, fără abonamente. Alegerea preferată pentru utilizatorii care doresc streaming auto-găzduit fără atașări comerciale.
- **Emby** — server media **freemium**. Serverul de bază este gratuit; **Emby Premiere** este o achiziție unică sau anuală care deblochează aplicații mobile, sincronizare offline, Modul Cinema și multe altele. Evervideo se conectează atât la biblioteci gratuite, cât și Premiere.

Indiferent de serverul pe care îl rulezi, Evervideo transmite întreaga ta bibliotecă — filme, seriale, video-uri de acasă și piste de subtitrări încorporate — cu egalizator video, suport 360°, Picture-in-Picture, AirPlay și Chromecast.

### Protocoale de rețea noi: FTP, SFTP, NFS

Pentru utilizatorii cu servere personalizate, homelab-uri sau cutii NAS generice care nu vin cu o aplicație mobilă elegantă, Evervideo 1.7 adaugă trei protocoale clasice:

- **SFTP (SSH File Transfer Protocol)** — răspunsul potrivit pentru **streaming video sigur de la distanță de pe propriul server**. SFTP funcționează deasupra SSH, deci întregul transfer (autentificare și date video) este criptat. Dacă ai un VPS, server dedicat sau o mașină Linux acasă cu acces SSH, poți pune un folder cu video-uri pe el și să transmiți prin internetul public fără a expune nimic altceva. Suportă autentificare cu parolă și pe bază de cheie.
- **FTP** — standardul de lungă durată pentru transferul de fișiere. Util dacă **NAS-ul tău de acasă** (Synology mai vechi, ASUS, D-Link, TerraMaster sau cutii generice) expune un server FTP, dar nu are integrare API nativă. Cel mai bine folosit în interiorul rețelei tale locale.
- **NFS (Network File System)** — protocolul de partajare de facto pe Linux și pe majoritatea dispozitivelor NAS. Partajările NFS sunt comune în homelab-uri și rețele de afaceri mici; Evervideo le montează acum și transmite video 4K și HD cu suprasarcină scăzută.

> **Sfat:** SFTP este protocolul pe care îl vrei pentru streaming prin internetul deschis. FTP și NFS sunt cele mai bune în interiorul rețelei tale locale — ține-le departe de internetul public, cu excepția cazului în care le înfășori într-un VPN.

## Gesturi noi de redare

Vizionarea video-urilor în ecran complet ar trebui să fie fără efort. Evervideo 1.7 introduce un set curat de gesturi tactile care îți permit să controlezi redarea fără a expune controalele de pe ecran — perfect pentru filme, prelegeri sau orice vrei să urmărești neîntrerupt.

### Dublu tap — sari înainte sau înapoi

Atinge de două ori **partea dreaptă** a ecranului pentru a **sări înainte** cu un număr configurabil de secunde. Atinge de două ori **partea stângă** pentru a **sări înapoi**. Poți schimba intervalul (implicit: 10 secunde) în **Setări → Redare → Interval de salt prin gest** — alege orice valoare între 5 secunde (pentru căutare fină) și 60 de secunde (pentru a sări peste introduceri).

Acesta este gestul pe care utilizatorii YouTube și Netflix îl recunosc instantaneu, iar acum este nativ în Evervideo pentru orice video, din orice sursă.

### Atinge și ține — viteză 2x temporară

Apasă și ține oriunde pe ecran pentru a **accelera temporar redarea la 2x**. Eliberează pentru a reveni la viteza normală. Perfect pentru:

- Sărirea peste scene lente fără a te angaja la o modificare permanentă a vitezei.
- Scanarea rapidă a prelegerilor, tutorialelor sau podcasturilor pentru a găsi secțiunea relevantă.
- Eșantionarea filmelor înainte de a te angaja să urmărești versiunea completă.

Gestul de ținere nu modifică viteza ta de redare salvată — eliberează și ești înapoi de unde ai pornit.

### Tap unic — afișează / ascunde controalele

Un singur tap pe ecran comută controalele de redare (redare, pauză, bara de derulare, subtitrări, egalizator). Atinge o dată pentru a le aduce sus, atinge din nou pentru a le ascunde. Combinat cu dublu tap și ținere, asta înseamnă că poți petrece aproape un film întreg în mod ecran complet curat și totuși să cauți, să pui pauză și să scanezi la viteză oricând ai nevoie.

## Wi-Fi Drive: UI nouă și încărcări mai rapide

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) este funcția integrată a Evervideo pentru **transferul de video-uri fără fir de pe computerul tău pe iPhone sau iPad — fără iTunes, fără cabluri, fără cont în cloud**. Ambele dispozitive trebuie să fie în aceeași rețea Wi-Fi. Pornești serverul în aplicația iOS și apoi fie:

- Deschizi URL-ul în orice browser desktop (Safari, Chrome, Firefox, Edge), tragi fișierele video în pagină și ele se încarcă direct pe dispozitiv, fie
- Montezi dispozitivul ca o partajare de rețea prin **Mac Finder** («Conectare la server…») sau **Explorator de fișiere Windows** (Mapare unitate de rețea) folosind WebDAV.

Este cel mai rapid mod de a muta o colecție mare locală de video pe telefon sau tabletă fără niciun serviciu terț. Vezi [ghidul pas cu pas aici](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).

În Evervideo 1.7, Wi-Fi Drive primește:

- **Interfață utilizator reproiectată** — mai curată, mai ușor de citit la prima vedere și actualizată pentru Liquid Glass.
- **Mod nou de selecție pentru acțiuni în loturi** — alege mai multe fișiere sau foldere și acționează asupra lor în bloc (șterge, mută, copiază).
- **Coadă îmbunătățită de încărcare a fișierelor** — feedback mai bun al progresului și rezistență la sughițuri de rețea, astfel încât o conexiune Wi-Fi instabilă nu mai strică un transfer de 30 GB.
- **Performanță generală de transfer mai bună** — încărcări măsurabil mai rapide pentru biblioteci mari, în special pentru fișiere MKV 4K și colecții de filme.

## Alte îmbunătățiri

### Actualizări de design Liquid Glass

Interfața Evervideo 1.7 este actualizată pentru noul material **Liquid Glass** de la Apple în întreaga aplicație — suprafețe translucide, animații mai fluide și controale rafinate care se potrivesc natural în iOS 26, iPadOS 26 și macOS 26. Now Playing, exploratorul de fișiere și ecranele de setări au fost toate reajustate pentru a se potrivi cu noua estetică a sistemului.

### Biblioteci de conexiune actualizate

Am împrospătat bibliotecile subiacente pe care Evervideo le folosește pentru a comunica cu **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, **iCloud Drive**, **MEGA** și alte servicii. Rezultatul: mai puține eșecuri de conexiune în cazurile limită, suport mai bun pentru versiunile mai noi de servere și fiabilitate îmbunătățită la transmiterea video-ului pe conexiuni mai lente sau distante geografic.

### Remedieri ale erorilor de redare

- Remediate problemele de redare pe anumite servere auto-găzduite unde fluxurile se opreau după derulare pe fișiere MKV mari.
- Comportament îmbunătățit de reluare când rețeaua cade scurt în timpul redării.
- Sincronizare mai lină a subtitrărilor pe conținut de format lung.

### Remedieri de localizare

Remedieri de traducere în mai multe limbi pe baza feedback-ului direct al utilizatorilor. Adaptare mai bună a textului pe butoanele mai mici și în limbi europene mai lungi (germană, olandeză, franceză).

### Rafinări mai mici inspirate de feedback-ul tău

Multe îmbunătățiri mai mici pe baza recenziilor din App Store și e-mailurilor la support@everappz.com. Citim fiecare mesaj.

## De ce contează această actualizare

Evervideo 1.7 este construit în jurul a trei idei:

1. **Video-urile tale, oriunde le ții.** Fie că biblioteca ta trăiește pe iCloud Drive, într-un cloud axat pe confidențialitate precum Proton Drive sau Internxt, pe un server media precum Plex sau Jellyfin, pe un NAS acasă sau pe un Raspberry Pi care rulează Navidrome — Evervideo se conectează acum la el nativ, cu aceeași experiență de redare peste tot.
2. **Video în ecran complet care pare fără efort.** Noile gesturi tactile (dublu tap, atinge și ține, tap unic) aduc tipul de control fluid pe care aplicațiile de streaming precum YouTube și Netflix i-au învățat pe utilizatori să-l aștepte, aplicat colecției *tale* de video.
3. **Transferuri mai rapide de pe computer.** Un Wi-Fi Drive reîmprospătat cu selecție în loturi și o coadă de încărcare mai inteligentă face ca mutarea colecțiilor mari de filme 4K pe iPhone-ul sau iPad-ul tău să fie cu adevărat rapidă — fără cabluri, fără iTunes, fără compresie.

## Obține Evervideo 1.7

[**Descarcă Evervideo din App Store**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) sau actualizează din interiorul App Store. [Versiunea Mac](https://apps.apple.com/app/evervideo/id6743504109) este disponibilă separat ca aplicație Mac universală. Evervideo este o descărcare gratuită cu upgrade-uri opționale în aplicație pentru funcții avansate. Noile conexiuni de cloud, suportul pentru server media, gesturile de redare, îmbunătățirile Wi-Fi Drive și UI-ul Liquid Glass fac parte din actualizarea de bază.

Dacă îți place aplicația, te rugăm să lași o evaluare în App Store — ajută cu adevărat. Ai feedback sau ai dat de o problemă? Trimite-ne un e-mail la **support@everappz.com**. Citim fiecare mesaj.

## Întrebări frecvente

{{% details title="Ce este nou în Evervideo 1.7?" closed="true" %}}
Evervideo 1.7 introduce suport pentru peste 10 conexiuni noi (Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), gesturi noi de redare (dublu tap pentru derulare, atinge și ține pentru viteză 2x, tap unic pentru comutarea controalelor), un Wi-Fi Drive reproiectat cu mod de selecție și o coadă de încărcare mai inteligentă, actualizări de design Liquid Glass, biblioteci de conexiune actualizate și multe remedieri de erori.
{{% /details %}}

{{% details title="Evervideo funcționează cu Plex?" closed="true" %}}
Da. Începând cu Evervideo 1.7, te poți conecta la un Plex Media Server și transmite întreaga ta bibliotecă video — filme, seriale TV și video-uri de acasă. Plex Media Server este gratuit de rulat; Plex Pass este opțional. Evervideo suportă atât configurări gratuite, cât și Plex Pass, inclusiv redare directă a MKV, MP4, AVI, MOV și a altor formate fără re-codificare.
{{% /details %}}

{{% details title="Jellyfin sau Navidrome sunt suportate în Evervideo?" closed="true" %}}
Da. Atât Jellyfin, cât și Navidrome sunt complet suportate în Evervideo 1.7. Jellyfin este un server media gratuit, open-source, care gestionează video și audio. Navidrome este un server gratuit, open-source, care implementează API-ul Subsonic. Evervideo se conectează la ambele nativ.
{{% /details %}}

{{% details title="Plex, Jellyfin, Emby, Navidrome și Subsonic sunt gratuite?" closed="true" %}}
- **Plex** — serverul este gratuit; Plex Pass este un upgrade plătit opțional.
- **Jellyfin** — complet gratuit și open-source.
- **Emby** — serverul este gratuit; Emby Premiere este plătit și deblochează sincronizarea mobilă și offline.
- **Navidrome** — complet gratuit și open-source.
- **Subsonic** — serverul oficial costă 1 USD/lună după o perioadă de încercare de 30 de zile, dar API-ul său este deschis și multe servere gratuite (inclusiv Navidrome) îl implementează.
{{% /details %}}

{{% details title="Pot transmite de pe NAS-ul meu de acasă prin SFTP, FTP sau NFS?" closed="true" %}}
Da. Evervideo 1.7 adaugă SFTP, FTP și NFS ca tipuri de conexiune native. SFTP este alegerea recomandată pentru streaming de pe propriul server prin internetul public, deoarece tot traficul este criptat prin SSH. FTP și NFS sunt cel mai bine folosite în interiorul rețelei tale locale sau în spatele unui VPN.
{{% /details %}}

{{% details title="Cum conectez Evervideo la un server personalizat folosind SFTP?" closed="true" %}}
Deschide Evervideo, mergi la fila Conexiuni, alege SFTP și introdu numele de gazdă sau IP-ul serverului tău, portul (de obicei 22), numele de utilizator și fie o parolă, fie o cheie privată SSH. Evervideo va naviga prin folderele tale de la distanță și va transmite fișiere video direct cu criptare end-to-end.
{{% /details %}}

{{% details title="Evervideo suportă Internxt și Proton Drive?" closed="true" %}}
Da. Ambele cloud-uri axate pe confidențialitate sunt suportate începând cu Evervideo 1.7. Se alătură MEGA și altor servicii axate pe confidențialitate deja disponibile în aplicație.
{{% /details %}}

{{% details title="Cum funcționează noile gesturi de redare?" closed="true" %}}
În redarea video în ecran complet, **atinge de două ori partea dreaptă** pentru a sări înainte și **atinge de două ori partea stângă** pentru a sări înapoi cu un interval configurabil (implicit 10 secunde — schimbă-l în Setări). **Atinge și ține** oriunde pe ecran pentru a accelera temporar la 2x; eliberează pentru a reveni la normal. **Tap unic** oriunde pentru a comuta controalele de redare (afișează sau ascunde).
{{% /details %}}

{{% details title="Pot schimba intervalul de salt al dublului tap?" closed="true" %}}
Da. Mergi la **Setări → Redare → Interval de salt prin gest** și alege o valoare între 5 și 60 de secunde. Majoritatea utilizatorilor o țin la 10 sau 15 secunde.
{{% /details %}}

{{% details title="Ce este Wi-Fi Drive în Evervideo?" closed="true" %}}
Wi-Fi Drive este funcția integrată de transfer wireless de fișiere a Evervideo. Îți permite să încarci video-uri de pe computerul tău pe iPhone sau iPad prin rețeaua ta Wi-Fi locală — fără iTunes, fără cabluri, fără cont în cloud. Poți folosi orice browser desktop sau un client WebDAV precum Mac Finder sau Explorator de fișiere Windows. Vezi [ghidul complet Wi-Fi Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).
{{% /details %}}

{{% details title="Evervideo redă MKV, AVI și alte formate din Plex sau Jellyfin?" closed="true" %}}
Da. Evervideo redă practic orice format video — MKV, AVI, MP4, MOV, FLV, WMV, WEBM, M4V, TS, 3GP — și le transmite direct din Plex, Jellyfin, Emby și alte servere media fără a necesita transcodare pentru majoritatea codecurilor. Acest lucru înseamnă o sarcină de CPU mai mică pe serverul tău și timpi de pornire mai rapizi.
{{% /details %}}

{{% details title="Evervideo 1.7 este gratuit pentru actualizare?" closed="true" %}}
Da. Evervideo este o descărcare gratuită din App Store, iar 1.7 este o actualizare gratuită pentru toți utilizatorii existenți. Noile integrări cloud, suportul pentru server media, gesturile de redare, îmbunătățirile Wi-Fi Drive și UI-ul Liquid Glass fac parte din actualizarea de bază.
{{% /details %}}

{{% details title="Pe ce dispozitive este disponibil Evervideo 1.7?" closed="true" %}}
Evervideo 1.7 rulează pe iPhone, iPad și Mac. AirPlay și Chromecast îți permit să transmiți redarea pe un ecran mai mare. Sincronizarea iCloud Drive menține biblioteca și setările tale consistente între dispozitive.
{{% /details %}}
