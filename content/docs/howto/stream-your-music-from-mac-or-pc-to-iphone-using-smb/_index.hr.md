---
title: "Streamajte glazbu s Maca ili PC-a na iPhone koristeći SMB"
description: "Naučite kako streamati svoju glazbenu kolekciju s Maca ili Windows PC-a na iPhone ili iPad koristeći Evermusic i SMB protokol. Jednostavan vodič korak po korak za povezivanje i uživanje u zvuku bez sinkronizacije."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["streamanje glazbe s Mac na iPhone", "SMB audio streaming iOS", "Evermusic SMB postavljanje", "povezivanje PC glazbe iPhone", "Mac dijeljenje glazbe iOS", "SMB Windows streaming datoteka", "Evermusic pristup PC mapama"]
---

{{< author-byline >}}


**Ukratko:** Koristite aplikaciju Evermusic za iPhone ili iPad za streamanje glazbe s vašeg Maca ili Windows PC-a putem lokalne mreže koristeći SMB. Bez sinkronizacije, bez kopiranja -- samo omogućite dijeljenje datoteka na računalu, povežite se u aplikaciji i reproducirajte. Postavljanje traje manje od 5 minuta.

Utapate li se u moru glazbe na svom MAC-u ili PC-u i želite je uživati bez problema na svom iPhoneu ili iPadu? Ne tražite dalje od Evermusic. S Evermusic je nevjerojatno jednostavno povezati svoje računalo koristeći SMB protokol i streamati svoje omiljene melodije bez brige o zauzimanju dodatnog prostora na uređaju ili problemima sa sinkronizacijom. Evo vodiča korak po korak za početak:

## Korak 1: Omogućite SMB protokol na svom računalu

![Evermusic - SMB podrška - Mac zaslon za dijeljenje](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Ako koristite MAC

- Otvorite Postavke sustava -> Dijeljenje.
- Omogućite uslugu Dijeljenja datoteka.
- U odjeljku "Dijeljene mape" dodajte svoju glazbenu mapu, odaberite korisnika i postavite razine dozvola (Čitanje i pisanje ili Samo čitanje).
- Za dodatnu pogodnost, možete odabrati "Svi: Samo čitanje" za glazbenu mapu, čineći je lako dostupnom u Evermusic.
- Ne zaboravite zapamtiti URL svog računala (smb://192.168.xx.xx) za sljedeće korake.

![Evermusic - SMB podrška - Zaslon dijeljenja datoteka](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Dodirnite "Opcije" i omogućite "Dijeli datoteke i mape koristeći SMB."
- Omogućite "Windows dijeljenje datoteka" za dostupne račune.

![Evermusic - SMB podrška - Zaslon dijeljenja datoteka i mapa](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Ako koristite Windows PC

![Evermusic - SMB podrška - Dijeljenje datoteka na Windowsu](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Desnom tipkom miša kliknite na svoju glazbenu mapu.
- Odaberite "Svojstva."
- Otvorite karticu "Dijeljenje."
- Kliknite "Dijeli..."
- Odaberite ljude s kojima želite dijeliti i postavite njihove razine dozvola.
- Kao i s MAC-om, možete odabrati "Svi: Čitanje" za odabranu glazbenu mapu.
- Kliknite "Završeno" za spremanje postavki.

![Evermusic - SMB podrška - Dijeljena mapa na Windowsu](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Korak 2: Dodajte svoje računalo automatski

- Sada otvorite Evermusic i idite na karticu "Povezivanja" ("Mreža" ako koristite stariju verziju aplikacije).
- Ako vidite svoje računalo u odjeljku "Dostupni uređaji" ("Dostupna dijeljenja" ako koristite stariju verziju aplikacije) i odabrali ste "Svi: Samo čitanje" u prethodnom koraku, jednostavno dodirnite svoje računalo i automatski će se povezati.
- Ako se to ne dogodi, možete dodati svoje računalo ručno.

![Evermusic - SMB podrška - Zaslon povezivanja računa](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Korak 3: Dodajte svoje računalo ručno

- Dodirnite "Poveži cloud uslugu" ("Dodaj račun" ako koristite stariju verziju aplikacije)
- Odaberite "SMB" s popisa dostupnih poslužitelja na sljedećem zaslonu.
- Na zaslonu postavki "SMB":
  - Unesite URL poslužitelja s putanjom dijeljene mape. Možete unijeti ime poslužitelja ili IP poslužitelja. Na primjer:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Unesite svoje korisničko ime i lozinku ili ostavite ova polja prazna ako ste odabrali "Svi: Samo čitanje" u prethodnom koraku.
  - Polje "WORKGROUP" je neobavezno i treba ga koristiti ako imate Active Directory domenu.

![Evermusic - SMB podrška - Zaslon unosa vjerodajnica](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Nakon što povežete svoj SMB račun, pojavit će se u odjeljku "Cloud usluge" ("Računi"). Otvorite povezani račun dodirom na njega, navigirajte do glazbene mape i dodirnite bilo koju audio datoteku za pokretanje playera.

![Evermusic - SMB podrška - Zaslon otvaranja povezane mape](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Uživajte u svojoj glazbenoj kolekciji besprijekorno na svom iPhoneu ili iPadu s Evermusic.

![Evermusic - SMB podrška - Zaslon audio playera](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Korak 4: SMB2 zaobilazno rješenje

Ako naiđete na probleme s pregledavanjem mapa ili reprodukcijom datoteka koje sadrže posebne znakove (poput ü, ö, é), to može biti povezano s SMB2 protokolom. Aktivno radimo na rješavanju ovog problema.

Kao privremeno rješenje, pokušajte omogućiti SMB 1 na svom poslužitelju i u postavkama aplikacije. Alternativno, možete se povezati na svoj SMB poslužitelj koristeći izbornik za otvaranje datoteka sustava. Evo kako:

1. Navigirajte do "Lokalne datoteke."
2. Pomaknite se prema dolje do odjeljka "Datoteke na ovom uređaju" i dodirnite "Otvori datoteke..." ili "Otvori mape..."
3. Pronađite svoj poslužitelj i odaberite datoteke ili mape koje trebate.
4. Dodirnite "Otvori" za potvrdu odabira.

## Korak 5: WebDAV zaobilazno rješenje

Dodatno, možete pokušati povezati se na svoj NAS koristeći WebDAV ili DLNA protokole ako su podržani.

Slijedeći ove korake, možete zaobići probleme povezane s posebnim znakovima u imenima datoteka i nastaviti uživati u svojim medijskim datotekama.

P.S. Također možete prenijeti audio datoteke s MAC/PC-a na iPhone koristeći iTunes dijeljenje datoteka i reproducirati lokalne audio datoteke. Saznajte više o ovoj značajci u našem vodiču: [Kako reproducirati iTunes datoteke na iPhoneu](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Često postavljana pitanja

{{% details title="Mogu li streamati glazbu s PC-a na iPhone bez iTunesa?" closed="true" %}}
Da. Evermusic se povezuje na vaš PC putem SMB na vašoj lokalnoj Wi-Fi mreži. iTunes nije potreban. Samo omogućite dijeljenje datoteka na PC-u i povežite se u aplikaciji.
{{% /details %}}

{{% details title="Koristi li SMB streaming mobilne podatke?" closed="true" %}}
Ne. SMB radi putem vaše lokalne Wi-Fi mreže. Nije potrebna internetska veza niti mobilni podaci.
{{% /details %}}

{{% details title="Koje audio formate Evermusic podržava putem SMB-a?" closed="true" %}}
Evermusic podržava MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC i druge uobičajene audio formate. Datoteke se reproduciraju izravno s SMB dijeljenja.
{{% /details %}}

{{% details title="Mogu li streamati glazbu s NAS-a na iPhone?" closed="true" %}}
Da. Ako vaš NAS podržava SMB (većina ga podržava, uključujući Synology, QNAP i WD My Cloud), možete se povezati na njega koristeći iste korake u ovom vodiču.
{{% /details %}}

{{% details title="Trebam li držati računalo uključeno dok streamam?" closed="true" %}}
Da. Budući da Evermusic streama datoteke izravno s vašeg računala, ono mora biti uključeno i povezano na istu mrežu kao vaš iPhone.
{{% /details %}}

{{% details title="Postoji li ograničenje veličine datoteke za SMB streaming?" closed="true" %}}
Ne. Evermusic streama datoteke bilo koje veličine putem SMB-a. Velike lossless datoteke (FLAC, WAV) rade bez problema.
{{% /details %}}
