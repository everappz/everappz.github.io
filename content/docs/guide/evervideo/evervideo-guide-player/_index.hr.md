---
title: "Medijski player"
date: 2020-02-01
lastmod: 2026-06-01
description: "Naučite kako koristiti medijski player Evervideo na iPhone, iPad i Mac. Picture-in-Picture, hardverski ubrzano H.264 / HEVC dekodiranje, audio i video ekvalizatori, primarni i sekundarni titlovi, odabir audio i video zapisa, skaliranje i rotacija videa, brzina reprodukcije, tajmer za spavanje, AirPlay 2, Google Chromecast, RTSP streamovi i kompaktni uvijek vidljivi player."
keywords: [
  "vodič za player Evervideo", "postavke video playera", "ekvalizator Evervideo",
  "Picture-in-Picture iPhone", "PiP video iPad", "PiP video Mac",
  "AirPlay 2 video", "Google Chromecast video",
  "titlovi videa iPhone", "vanjski SRT titlovi",
  "player titlova ASS SSA", "libass iOS",
  "dvostruki titlovi učenje jezika",
  "video ekvalizator svjetlina kontrast", "audio ekvalizator video player",
  "zaključavanje rotacije video playera", "način skaliranja videa iOS",
  "hardverski H.264 dekoder iPhone", "hardverski HEVC dekoder iPad",
  "brzina reprodukcije videa", "FFmpeg video player iOS",
  "RTSP iPhone player", "kompaktni video player",
  "VR 360 video player iPhone"
]
tags: ["vodič", "evervideo", "player", "PiP", "titlovi", "video ekvalizator"]
readingTime: 14
---


Medijski player je glavni zaslon aplikacije gdje upravljate reprodukcijom i većinom Evervideo značajki. Reproducira i video i audio datoteke i izgrađen je na prilagođenom FFmpeg-baziranom playeru s hardverski ubrzanim H.264 i HEVC dekodiranjem koji obavlja teški posao. Istražimo kako ga koristiti.

## Pristup medijskom playeru

Do playera na cijelom zaslonu možete doći s kompaktne trake playera. Na iPhoneu, kompaktni player se nalazi na vrhu glavnog zaslona. Na iPadu i Macu, nalazi se na lijevoj strani (ili na vrhu glavnog panela). Za skupljanje playera na cijelom zaslonu natrag u kompaktni prikaz, dodirnite gumb za zatvaranje u donjem desnom kutu ili povucite prema dolje. Za potpuno skrivanje kompaktnog playera, dodirnite i povucite prema dolje još jednom.

Kompaktni player ostaje vidljiv dok pregledavate svoju biblioteku, upravitelj datoteka ili postavke, tako da nikada ne gubite video dok tražite sljedeći.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo medijski player na cijelom zaslonu" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Podržani video i audio formati

Evervideo reproducira gotovo svaki moderni kontejner i kodek kroz ugrađeni FFmpeg motor, s hardverski ubrzanim H.264 i HEVC dekodiranjem na podržanim uređajima.

- **Video kontejneri:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — i mnogi drugi.
- **Video kodeci:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — plus gotovo svaki drugi kodek koji FFmpeg podržava.
- **Audio kodeci:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — i mnogi drugi.
- **Formati titlova:** SRT, VTT (WebVTT), ASS / SSA i ugrađene tekstualne ili slikovne staze titlova.
- **Streaming protokoli:** HTTP / HTTPS, HLS (m3u8), RTSP (IP kamere i IPTV), i direktni streaming datoteka putem SMB / WebDAV / FTP / SFTP / NFS / DLNA.

To pokriva gotovo svaku video datoteku s kojom ćete se vjerojatno susresti — uključujući MKV rip-ove, sigurnosno-kamera RTSP streamove i AV1 webm web preuzimanja.

## Kontrole reprodukcije

Na dnu zaslona playera vidjet ćete gumbe za Reprodukciju, Pauzu, Sljedeće i Prethodno. Postoje i opcionalni gumbi poput Preskakanje naprijed i Preskakanje unatrag (zadano 10 sekundi) koje možete omogućiti u postavkama aplikacije. Držite gumbe Sljedeće / Prethodno za brzo premotavanje naprijed ili unatrag. Povucite klizač reprodukcije za skok na bilo koji položaj.

## Ponavljanje i nasumično

Dodirnite gumb za ponavljanje za cikliranje kroz načine ponavljanja:

- **Ponovi sve** — petlja svakog videozapisa u redu.
- **Ponovi jedan** — ponavlja samo trenutni videozapis.
- **Stani na kraju** — pauzira kada trenutni videozapis završi.
- **Bez ponavljanja** — reproducira red jednom bez ponavljanja.

Koristite gumb **Nasumično** za nasumičan redoslijed videozapisa u redu.

## Picture-in-Picture (PiP)

Na iPhoneu i iPadu, Evervideo u potpunosti podržava Picture-in-Picture (PiP). Dodirnite PiP ikonu na zaslonu playera ili jednostavno stavite Evervideo u pozadinu — videozapis nastavlja se reproducirati u plutajućem prozoru iznad svake druge aplikacije. Povucite plutajući prozor u bilo koji kut; prikvačite za promjenu veličine; dodirnite jednom za prikaz osnovnih kontrola reprodukcije / pauze / preskakanja; dodirnite mali gumb za proširenje za povratak u puni Evervideo.

PiP radi sa svakim video formatom koji Evervideo reproducira, uključujući datoteke koje se streamaju s clouda i RTSP streamove. PiP nastavlja raditi i dok je telefon zaključan (ovisno o postavci automatskog zaključavanja).

## Kompaktni player

Kompaktni player je stalni mini player koji ostaje vidljiv na vrhu svakog zaslona u aplikaciji dok pregledavate biblioteku, upravitelj datoteka ili postavke. Dodirnite ga za proširenje u player na cijelom zaslonu; povucite prema dolje da ga skupite opet.

{{< cards cols="1">}}
  {{< card title="" subtitle="Postavke videa Evervideo iz prikaza kompaktnog playera na glavnom zaslonu" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

Za AirPlay, dodirnite gumb AirPlay na playeru. Evervideo podržava AirPlay 2, tako da možete streamati video na Apple TV, HomePod ili bilo koji AirPlay 2-kompatibilni zvučnik ili pametni TV. Na postavljanju s više AirPlay uređaja, možete usmjeriti audio na više prijemnika istovremeno.

## Google Chromecast

Za korisnike Google Casta, ikona Cast pojavljuje se na playeru. Dodirnite je za odabir uređaja i početak castanja. Pobrinite se da su telefon i Cast prijemnik na istoj Wi-Fi mreži. Chromecast hardver ne podržava sve kodece — neke datoteke možda trebaju transkodiranje.

## RTSP live streamovi

Evervideo može reproducirati RTSP izvore izravno — IP kamere, kamere na zvoncu, IPTV streamove, emitiranja i bilo koji `rtsp://` URL. Dodajte stream kao RTSP vezu u Datoteke → Online veze → Dodaj vezu, zatim ga dodirnite za početak gledanja. RTSP streamovi rade u Picture-in-Picture, kompaktnom playeru i castaju se putem AirPlay 2 i Chromecast kao i obični video.

## Odabir audio zapisa

Za videozapise s više audio zapisa (komentar, alternativni jezični sinkroni prijevodi, režiserske staze), dodirnite gumb Više radnji na playeru i odaberite Audio zapis — zatim odaberite zapis koji želite. Bitno za strane filmove, BDMV / MKV datoteke s više sinkronih prijevoda i obrazovni sadržaj s komentarskim stazama.

## Odabir video zapisa

Neke video datoteke uključuju više video streamova (multi-kut Blu-ray, alternativni rezovi). Odaberite Video zapis iz izbornika Više radnji za prebacivanje između njih tijekom reprodukcije.

## Titlovi — unutarnji i vanjski

Evervideo vam daje fino zrnatstu kontrolu nad titlovima:

- **Staza titlova** — odaberite iz staza ugrađenih u datoteku.
- **Vanjske datoteke titlova** — učitajte `.srt`, `.vtt`, `.ass` ili `.ssa` datoteke s uređaja, iCloud Drive ili bilo koje connected cloud usluge.
- **Libass renderiranje** — napredno ASS / SSA stiliziranje (fontovi, boje, pozicije, karaoke efekti) ispravno se prikazuje zahvaljujući ugrađenom libass.
- **Odabir fonta** — odaberite prilagođeni font za primarne titlove i zasebni font za sekundarne titlove. Dostupni su ugrađeni fontovi plus svaki font instaliran na vašem uređaju.

Sve ovo možete konfigurirati u Postavke → Titlovi prije reprodukcije ili koristiti Više radnji → Titlovi s playera za promjenu u hodu.

## Audio ekvalizator

Evervideo uključuje potpuni audio ekvalizator za ugađanje video zvučnih zapisa za slušalice, zvučnike ili hi-fi postavljanje. Dodirnite ikonu ekvalizatora na prikazu glasnoće (ili radnju Audio ekvalizator na izborniku Više radnji playera), uključite ekvalizator s preklopnikom u gornjem desnom kutu i odaberite predodređenu postavku ili povucite klizače pojasa za izgradnju vlastite. Prilagođene predodređene postavke mogu se izvesti i uvesti za dijeljenje između uređaja ili sigurnosno kopiranje.

## Video ekvalizator

Za ugađanje slike, Evervideo pruža namjenski video ekvalizator — podesite svjetlinu, kontrast, zasićenost i nijansu u stvarnom vremenu tijekom reprodukcije. Kao i audio ekvalizator, prilagođene video predodređene postavke mogu se izvesti i uvesti za dijeljenje ili sigurnosno kopiranje. Koristite ga za osvjetljavanje tamne scene na sunčan dan, povećanje zasićenosti na izblijedjelom sadržaju ili zagrijavanje hladnog kolor baca.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo video ekvalizator" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Način skaliranja videa

Odaberite kako video ispunjava zaslon:

- **Prilagodi** — čuvajte originalni omjer stranica; crne trake prema potrebi.
- **Ispuni** — ispunite cijeli zaslon, opisujući video ako je potrebno.
- **Rastegni** — rastegnite video za ispunjavanje zaslona, iskrivljujući ako je potrebno.
- **Originalno** — zadržite nativnu rezoluciju na 1:1.

## Rotacija videa

Za videozapise snimljene u krivoj orijentaciji, odaberite **Više radnji → Rotacija** i odaberite **0°**, **90°**, **180°** ili **270°** za rotaciju slike bez napuštanja playera.

## Hardversko dekodiranje (H.264 i HEVC)

U Postavke → Player → Video, možete neovisno omogućiti / onemogućiti Hardversko dekodiranje H.264 i Hardversko dekodiranje H.265 (HEVC). Hardversko dekodiranje je brže, koristi manje baterije i radi hladnije — ali u rijetkim slučajevima (oštećene datoteke, egzotični profili) možda ćete trebati onemogućiti hardversko dekodiranje i vratiti se na softversko FFmpeg dekodiranje. Evervideo vam omogućuje to datoteka-po-datoteka iz izbornika Više radnji playera.

## VR 360° viewport

Evervideo uključuje VR / 360° viewport za sferne video datoteke. Pri reproduciranju 360° videa, možete povući za gledanje okolo, prikvačiti za zumiranje, a Evervideo će iskriviti renderiranje u stvarnom vremenu.

## Brzina reprodukcije

Dodirnite kontrolu brzine na alatnoj traci playera za promjenu brzine reprodukcije — usporite za analizu (0.25× ili 0.5×) ili ubrzajte za vodiče i predavanja (1.25×, 1.5×, 2× i do 3×). Dodirnite ikonu konfiguracije u gornjem desnom kutu zaslona brzine za prebacivanje na precizni način s finijim podešavanjima. Dostupna je i korekcija visine tona po stazi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Brzina reprodukcije Evervideo na glavnoj alatnoj traci" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Red playera

Za prikaz reda playera, dodirnite gumb reda na playeru. Svaki videozapis u redu ima više radnji — dodirnite tri točkice za prikaz. Za preuređivanje videozapisa u redu, koristite indikator za preuređivanje pored naslova i povucite ga na novu poziciju.

{{< cards cols="1">}}
  {{< card title="" subtitle="Red reprodukcije Evervideo" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Tajmer za spavanje

Otvorite Postavke → Player → Tajmer za spavanje, uključite ga i odaberite koliko dugo želite da reprodukcija traje prije automatskog zaustavljanja. Gumb Tajmer za spavanje možete dodati i izravno na glavni zaslon playera putem Postavke → Player → Personalizacija → Radnje glavnog zaslona.

## Oznake playera

Spremite svoje mjesto u dugim videozapisima — predavanja, audioknjige na videu, vodiči, sat dugih YouTube preuzimanja — dodirivanjem Dodaj oznaku iz izbornika Više radnji. Oznake se pojavljuju na popisu Više radnji → Zabilješke videa i ostaju između sesija.

## Izbornik Više radnji

Dodirnite gumb **Više radnji "..."** na playeru za pristup dodatnim funkcijama.

- **Nastavi reproduciranje** — nastavite red od zadnjeg mjesta.
- **Pretraživanje** — pronađite određeni videozapis u redu.
- **Zabilješke** — pregledajte i skočite na oznake.
- **Brzina** — podesite brzinu reprodukcije.
- **Nedavne** — nedavno reproducirani videozapisi.
- **Omiljeni** — omiljeni videozapisi.
- **Audio ekvalizator** — aktivirajte audio ekvalizator.
- **Video ekvalizator** — aktivirajte video ekvalizator.
- **Audio zapis** — odaberite audio stream.
- **Video zapis** — odaberite video stream.
- **Titlovi** — primarna / sekundarna staza, vanjska datoteka, font.
- **Rotacija** — rotirajte sliku 0° / 90° / 180° / 270°.
- **Način skaliranja** — Prilagodi / Ispuni / Rastegni / Originalno.
- **Picture-in-Picture** — uđite u PiP način.
- **AirPlay** / **Chromecast** — pošaljite na uređaj.
- **Tajmer za spavanje** — postavite tajmer za zaustavljanje reprodukcije.
- **Spremi red kao popis za reproduciju** — spremite trenutni red kao novi popis za reproduciju.
- **Izbriši red** — očistite red i zaustavite reprodukciju.
- **Postavke** — skočite izravno na postavke playera.
- **Pomoć** — otvorite smjernice.

{{< cards cols="1">}}
  {{< card title="" subtitle="Zaslon Više radnji playera Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Postavke playera

Potpuno stablo postavki playera dokumentirano je u [vodiču za postavke](/docs/guide/evervideo/evervideo-guide-settings/). Najkorišteniji odjeljci:

- **Općenito** — Način ponavljanja, način nasumičnog, spremi stanje playera, spremi položaj reprodukcije, intervali preskakanja.
- **Video** — Hardversko dekodiranje H.264 / HEVC, video ekvalizator, način skaliranja, rotacija, način prikaza, željeni FPS, željeni format piksela, VR view-port.
- **Audio** — Audio ekvalizator, brzina uzorkovanja, kanali, trajanje IO buffera, mješoviti način.
- **Titlovi** — Primarna / sekundarna staza, odabir vanjskih datoteka, font, sekundarni font.
- **Uređaji** (iOS) — AirPlay / Chromecast.
- **Personalizacija** — Stil rasporeda playera (Minimalni / Donji / Antički / Klasični), radnje glavnog zaslona, kontrole zaslona za zaključavanje.
- **Predmemorija reprodukcije** — predmemorija diska za glatki streaming.
- **Tajmer za spavanje** — automatsko zaustavljanje.

## Pristupačnost

Evervideo je u potpunosti dostupan s VoiceOver. Svaka komponenta ima dobro dizajniranu oznaku i opis. Kada je VoiceOver aktivan, aplikacija prelazi u Tekstni način tako da se prikazuju samo smisleni elementi — poboljšavajući brzinu navigacije i jasnoću. Možete aktivirati i Tekstni način u Postavke → Pristupačnost → Tekstni način.

### Podešavanje klizača s VoiceOver

1. **Odaberite klizač** — povucite lijevo ili desno dok VoiceOver ne objavi.
2. **Podesite vrijednost** — dvaput dodirnite i zadržite klizač, zatim povucite gore ili dolje za brzu promjenu vrijednosti. VoiceOver objavljuje novu vrijednost kako idete.

Ostale komponente rade kako se očekuje, koristeći VoiceOver obrasce koje pruža sustav.
