---
title: "Postavke"
date: 2020-02-01
description: "Istražite svaku postavku u Flacboxu — od preferencija reprodukcije, FFmpeg / sistemskog audio motora, Hi-Res audio izlaza, podešavanja ekvilajzera, korekcije visine tona, trajanja IO međuspremnika, sinkronizacije metapodataka, kontrole popisa, prijenosa datoteka, widgeta početnog zaslona, Apple CarPlaya, personalizacije sučelja, jezika, lozinke, sigurnosne kopije i obnove te nadogradnje na Premium."
keywords: [
  "Flacbox postavke", "konfiguracija audio playera", "nadogradnja na Premium Flacbox",
  "WiFi Drive", "sinkronizacija metapodataka", "ekvilajzer", "brzina reprodukcije",
  "duplikati u popisu", "postavke upravitelja datoteka", "offline sinkronizacija glazbe",
  "editor audio oznaka", "tamni način rada", "obnova kupnji", "sigurnosna kopija postavki",
  "Flacbox postavke widgeta", "Flacbox postavke CarPlaya",
  "Flacbox FFmpeg postavke", "Flacbox postavke frekvencije uzorkovanja",
  "Flacbox postavke korekcije visine tona", "Flacbox IO međuspremnik",
  "Flacbox lozinka", "Flacbox jezik", "Flacbox personalizacija",
  "Flacbox analitika"
]
tags: ["vodič", "flacbox", "postavke"]
readingTime: 16
---


Zaslon Postavki je kontrolni centar Flacboxa. Odavde možete nadograditi na Premium, konfigurirati audio motor (sistemski kodeci ili FFmpeg), upravljati glazbenom bibliotekom, postaviti upravitelja datoteka, prilagoditi editor audio oznaka, omogućiti widgete početnog zaslona i Apple CarPlay, sigurnosno kopirati podatke te pristupiti pomoći i pravnim informacijama. Odjeljci su grupirani pod zaglavlja: Kupnje i ažuriranja, Preferencije aplikacije, Pomoć i Pravno i privatnost.

{{< cards cols="1">}}
  {{< card title="" subtitle="Glavni zaslon Postavki u Flacboxu" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Nadogradnja na Premium

Nadogradite aplikaciju na Premium verziju za uklanjanje svih ograničenja. Besplatna verzija aplikacije nudi jednokratnu doživotnu kupnju unutar aplikacije i dvije opcije pretplate (1 mjesec i 1 godina) za uklanjanje svih ograničenja i nadogradnju na Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Nadogradnja na Premium u Flacboxu" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

**Family Sharing** je omogućen za sve kupnje i planove, pa možete dijeliti Premium verziju s do pet članova obitelji bez dodatnih troškova.

{{< cards cols="1">}}
  {{< card title="" subtitle="Odabir Premium plana u Flacboxu" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Više o kupnjama i Premium verziji možete pročitati ovdje: [Koja je razlika između Flacboxa i Flacbox Premiuma](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Dijeljenje kupnji između iOS-a i Maca

Doživotne kupnje i pretplate dijele se između iOS-a i Maca, koristeći iCloud za sinkronizaciju tih informacija. Ako imate Premium verziju na iOS uređaju, osigurajte da imate instaliranu najnoviju verziju i da je iCloud omogućen. Pokrenite aplikaciju na iOS-u i pričekajte jednu minutu da se informacije o kupnji prevedu na iCloud.

Možete i pokušati tapnuti gumb Obnovi kupnje u postavkama aplikacije. Nakon toga instalirajte najnoviju verziju aplikacije s App Storea na Macu i pokrenite aplikaciju. Osigurajte da imate internetsku vezu i da koristite isti iCloud i App Store račun na Macu koji ste koristili na iOS-u. Pričekajte jednu minutu da aplikacija preuzme informacije o kupnji s iClouda — Premium verzija trebala bi se automatski aktivirati na Macu.

## Obnova kupnji na novom uređaju

Za obnovu kupnje na novom uređaju, koristite izbornik Kupnje → Obnovi kupnje. Vidjet ćete popis vaših kupnji. Ako ne vidite sve, potvrdite da je uređaj spojen na isti Apple ID koji je korišten za kupnje i osigurajte da je iCloud omogućen.

## Isprobajte Premium besplatno

Možete nadograditi na Premium verziju besplatno, na ograničeno vrijeme, koristeći ovaj izbornik. Samo pogledajte oglas ili recite prijateljima za aplikaciju da biste dobili Premium besplatno.

## Kupnje

Prethodne kupnje možete obnoviti iz ovog izbornika. Ako naiđete na pogreške aktivacije, pokušajte omogućiti opciju Obnovi kupnje pri pokretanju aplikacije.

## Ažuriranje softvera

Tapnite Ažuriranje softvera za provjeru je li dostupna novija verzija Flacboxa. Aplikacija će usporediti instaliranu verziju s najnovijom verzijom na App Storeu i obavijestiti vas preporučuje li se ažuriranje.

## Novosti

Ovaj izbornik dostupan je nakon puštanja nove verzije. Prikazuje sažetak promjena i novih funkcija u najnovijem ažuriranju.

## Audio player

Ovaj odjeljak konfigurira audio player i temeljni audio motor, uključujući odabir FFmpeg / sistemskog kodeka i opcije Hi-Res audio izlaza.

### Općenito

Ove postavke pokrivaju temeljne aspekte audio playera — red čekanja za reprodukciju, audio izlaz i spremanje stanja playera.

- **Način ponavljanja** — odaberite kako se audio player ponaša kada zapis završi:
  - **Ponovi sve** — reproducira sve zapise u redu čekanja iznova.
  - **Ponovi jedan** — ponavlja samo trenutni zapis.
  - **Zaustavi ponavljanje** — pauzira reprodukciju kada trenutni zapis završi.
  - **Bez ponavljanja** — dopušta redu čekanja da se reproducira jednom bez ponavljanja.
- **Način nasumičnog odabira** — nasumičan redosljed zapisa u redu čekanja. Možete ga postaviti na **Isključi nasumično** ili **Uključi nasumično**.
- **Audio kodek** — odaberite audio motor za reprodukciju:
  - **Sistemski kodek + FFmpeg** — daje prednost sistemskom audio kodeku gdje je moguće, poboljšavajući kompatibilnost i stabilnost. Korekcija visine tona i frekvencija uzorkovanja audio izlaza mogu biti ograničene.
  - **FFmpeg** — forsira FFmpeg kodek za sve audio datoteke, otključavajući korekciju visine tona i frekvenciju uzorkovanja audio izlaza.
- **Frekvencija uzorkovanja audio izlaza** — podesite frekvenciju uzorkovanja audio izlaza za optimizaciju kvalitete zvuka, posebno korisno s vanjskim DAC-om. Dostupne vrijednosti: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** i **96 kHz**.
- **Broj kanala audio izlaza** — za višekanalne audio sustave s vanjskim DAC-om, navedite broj kanala: Mono, Stereo, Centar / Lijevo / Desno, Centar / Lijevo / Desno / Surround, ITU BS.775-1, 5.1 Surround i SDDS.
- **Preferirano trajanje IO međuspremnika audio izlaza** — konfigurirajte trajanje međuspremnika ulaza / izlaza. Tipična vrijednost za minimiziranje latencije pri reprodukciji visokokvalitetnog audija je oko **5 milisekundi (0,005 sekundi)**. Testirajte različita trajanja na ciljnom uređaju za pronalaženje najboljeg balansa između niske latencije i reprodukcije bez smetnji.
- **Način rada audio izlaza (samo iOS)** — konfigurirajte mješoviti audio izlaz tako da se audio iz Flacboxa miješa s drugim aplikacijama. Detaljne upute su [ovdje](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Spremi poziciju reprodukcije** — sprema i obnavlja poziciju reprodukcije za pjesme u glazbenoj biblioteci.
- **Spremi stanje audio playera** — čuva stanje audio playera prije zatvaranja aplikacije, olakšavajući nastavak od mjesta gdje ste stali.

Nakon što ste omogućili i **Spremi poziciju reprodukcije** i **Spremi stanje audio playera**, otvorite bilo koju mapu, album, izvođača ili žanr i vidjet ćete gumb **Nastavi reprodukciju** na vrhu zaslona.

### Personalizacija

Personalizacija vam omogućuje prilagodbu izgleda zaslona audio playera, promjenu dostupnih kontrola na glavnom zaslonu, zaslonu zaključavanja i statusnoj traci, te konfiguraciju kontrola za preskakanje.

- **Stil zaslona audio playera** — konfigurirajte pozicioniranje elemenata na zaslonu audio playera.
- **Stil pomicanja omova albuma** — konfigurirajte preferirani stil pomicanja za omove albuma.
- **Dodatni elementi** — omogućite dodatne elemente na zaslonu audio playera. Informacije o audio formatu prikazuju audio informacije trenutno puštanog zapisa iznad omota; Klizač audio glasnoće prikazuje klizač audio izlaza ispod kontrola reprodukcije.
- **Radnje na glavnom zaslonu** — konfigurirajte koji gumbi trebaju biti vidljivi na glavnom zaslonu audio playera prema zadanoj postavci: Ponavljanje i nasumični način rada, Sljedeća i prethodna pjesma, Preskočiti Vrijeme, Tajmer spavanja, Google Chromecast, AirPlay i Bluetooth, Audio ekvilajzer, Pretraži, Zabilješke, Brzina, Dodaj zabilješku, Dodaj u omiljene, Komentari i još mnogo toga.
- **Kontrole reprodukcije na zaslonu zaključavanja** — odaberite koje se kontrole pojavljuju na zaslonu zaključavanja. Moguće vrijednosti: Preskočiti Vrijeme, Dodaj zabilješku, Dodaj u omiljene.
- **Gumbi za preskakanje** — odaberite vremenski interval za gumbe za Preskočiti Vrijeme.

### Učitavanje datoteka

Tijekom učitavanja datoteka, možete promijeniti vrstu mreže koja se koristi za učitavanje pjesama. Dostupne opcije: **Wi-Fi**, **Wi-Fi i mobilni podaci**.

- **Vrijeme predučitavanja** — postavite vremenski interval buferizacije. Povećajte ovo ako imate lošu mrežnu vezu.
- **Koristi izravni URL** — kada je omogućeno, koristi se izravni URL za učitavanje pjesme ako poslužitelj to podržava. To može ubrzati učitavanje, ali može utjecati na stabilnost reprodukcije.

### Audio ekvilajzer

Konfigurirajte 10-pojasni audio ekvilajzer, presetse i predpojačalo. Više o konfiguriranju audio ekvilajzera možete pročitati [ovdje](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Brzina reprodukcije

Podesite brzinu reprodukcije audio playera od **0,02× do 3,00×**. Tapnite ikonu konfiguracije u gornjem desnom kutu za prebacivanje na **precizni način rada** za finije prilagodbe.

### Korekcija visine tona

Promijenite postavke korekcije visine tona koristeći unaprijed definirane vrijednosti, ili se prebacite na **precizni način rada** tapnutjem na gumb u gornjem desnom kutu. Korekcija visine tona dostupna je na FFmpeg putu kodeka, s rasponom od **-1000 do +1000**.

### Predmemorija reprodukcije

Pjesme u redu čekanja audio playera automatski se preuzimaju za osiguranje glatke reprodukcije. Ako ručno preuzimate audio datoteke, možete onemogućiti ovo za izbjegavanje duplikata. Ovdje možete i konfigurirati veličinu predmemorije audio playera.

### Tajmer spavanja

Aktivirajte tajmer za automatsko zaustavljanje reprodukcije nakon određenog perioda. Tapnite ikonu konfiguracije u gornjem desnom kutu za **precizni način rada** s granularnosti od minute do minute.

## Biblioteka

Postavke glazbene biblioteke — automatska sinkronizacija, čitanje metapodataka, učitavanje omova albuma, popisi, nedavne i omiljene — nalaze se ovdje.

### Čitanje metapodataka

Kada dodajete zapise u biblioteku, **čitač metapodataka** se aktivira. Ovaj pozadinski proces čita sve metapodatke iz vaših zapisa i organizira ih po Izvođaču, Albumu, Žanru i Skladatelju. Možete prilagoditi brzinu čitanja metapodataka za brže učitavanje podataka (na račun baterije). Možete i onemogućiti čitač metapodataka i prikazivati nazive datoteka umjesto informacija o oznakama.

Čitač metapodataka **samo ažurira metapodatke u vašoj glazbenoj biblioteci** i ne mijenja datoteke pohranjene u vašem cloud računu ili lokalnoj pohrani. Za uređivanje metapodataka u samim audio datotekama, koristite ugrađeni **editor oznaka** putem odgovarajuće radnje u izborniku opcija.

Kada je uključeno **Čitanje metapodataka u pozadini**, čitač nastavlja raditi u pozadinskom načinu rada. Ako aplikacija troši previše energije tijekom audio reprodukcije, iOS je može suspendirati.

Ako imate veliku glazbenu kolekciju, izvršite sinkronizaciju metapodataka na desktop verziji aplikacije i prenesite sinkroniziranu glazbenu biblioteku na iOS koristeći **Sigurnosna kopija i obnova**.

Kada je omogućena **Normalizacija kodiranja metapodataka**, aplikacija automatski normalizira kodiranje metapodataka za sve pjesme. Ovo ispravlja pokvarena kodiranja oznaka (npr. nakon uređivanja datoteka na Windows PC-u) i sprječava pojavu netočnih znakova u informacijama o zapisima.

**Ponovo učitaj metapodatke** označava svaku datoteku u glazbenoj biblioteci kao datoteku s nedostajućim metapodacima, što uzrokuje osvježavanje svakog zapisa čitačem metapodataka.

**Pokreni čitanje metapodataka** ručno pokreće čitač metapodataka. Napredak je prikazan ispod radnje.

### Online sinkronizacija

Automatska online sinkronizacija glazbe automatski dodaje zapise iz spojenih cloud usluga u glazbenu biblioteku. Za njezino omogućavanje, otvorite postavke glazbene biblioteke i odaberite mape za sinkronizaciju.

S ovom opcijom omogućenom, aplikacija skenira odabrane mape, identificira podržane audio datoteke i dodaje ih u biblioteku. Pokrenite ili zaustavite sinkronizaciju odgovarajućom radnjom izbornika.

Online sinkronizacija radi samo dok je aplikacija u prvom planu, pa sinkronizacija velike biblioteke može potrajati. Za ubrzavanje, zadržite Flacbox otvorenim, prikopčajte uređaj na napajanje i omogućite **Postavke → Zaslon → Uvijek aktivan**.

Alternativno, izvršite online sinkronizaciju na desktop verziji aplikacije i prenesite rezultat na iOS koristeći **Sigurnosna kopija i obnova**.

Možete i odabrati koliko često se pokreće online sinkronizacija. Postavljanjem intervala na **Odmah** pokreće se sinkronizacija svaki put kada otvorite aplikaciju.

### Offline sinkronizacija

Konfigurirajte offline sinkronizaciju glazbe.

#### Sinkronizirane offline mape

Kada online mapu na cloud poslužitelju označite kao dostupnu offline (koristeći izbornik **Više radnji**), pojavljuje se ovdje. Sadržaj mape preuzima se u **Lokalne datoteke → Offline mape**. Kada se online mapa promijeni (datoteke dodane, uklonjene ili ažurirane), aplikacija provjerava promjene i ažurira lokalnu kopiju na uređaju.

Na ovom zaslonu možete ručno pokrenuti sinkronizaciju offline mape, otkriti offline mapu u njezinoj nadređenoj mapi i onemogućiti offline način rada za mapu. Onemogućavanje offline načina rada uklanja sve lokalne kopije datoteka s vašeg uređaja.

#### Vremenski interval

Odaberite koliko često aplikacija provjerava offline mape za izmjene.

#### Pokreni skeniranje lokalnih mapa

Skenirajte sve lokalne mape u direktoriju aplikacije **Dokumenti** za podržane audio datoteke. Pronađene datoteke automatski se dodaju u glazbenu biblioteku. Datoteke smještene na uređaju, ali izvan direktorija Dokumenti aplikacije, moraju se ručno dodati u glazbenu biblioteku, budući da aplikacija ne može njima pristupiti zbog sigurnosnih ograničenja iOS-a / macOS-a.

**Važno:** Preporučljivo je povremeno pokrenuti offline sinkronizaciju glazbe kako biste glazbenu biblioteku održavali ažuriranom s lokalnim datotekama.

### Personalizacija

Konfigurirajte stil zaslona glazbene biblioteke. Dostupne su tri opcije: **Jednostavni izbornik, Grupirani izbornik, Izbornik s karticama**. Možete i omogućiti ili onemogućiti omove albuma na zaslonu detalja albuma.

### Omovi albuma

Konfigurirajte kako aplikacija učitava i pohranjuje omove albuma.

- **Vrsta mreže** — odaberite **Wi-Fi** ili **Wi-Fi i mobilni podaci** za preuzimanje omova.
- **Učitaj omove albuma za online datoteke** — kada je omogućeno, ugrađeni omovi albuma učitavaju se za datoteke pohranjene u cloud pohrani. To može koristiti dodatne mrežne podatke.
- **Pretraži u mapi** — kada je omogućeno, ako zapis nema ugrađeni omot, aplikacija traži JPEG ili PNG slike u istoj mapi i koristi ih kao omot albuma.
- **Kvaliteta omota** — odaberite kvalitetu omova albuma pohranjenih na uređaju.
- **Prikaži u mapi** — otvorite mapu u kojoj su predmemorirani omovi albuma.
- **Izbriši sve** — izbrišite predmemorirane omove albuma za oslobađanje pohrane i prisilite aplikaciju da ih ponovo učita na zahtjev.

### Popisi

Omogućite opciju dodavanja iste pjesme u popis dva puta. Prema zadanoj postavci, ova opcija je onemogućena.

### Nedavne

Upravljajte popisom nedavno puštenih pjesama.

- **Izbriši popis** — izbrišite cijeli popis nedavno puštenih pjesama.
- **Promijeni veličinu popisa** — postavite broj stavki koji se pojavljuju na popisu.
- **Izvezi popis pjesama** — izvezite popis nedavno puštenih pjesama kao M3U, CSV ili TXT. Detaljne upute dostupne su [ovdje](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Omiljeni

Upravljajte popisom omiljenih pjesama.

- **Istovremeno uređivanje** — kada je omogućeno, dodavanje pjesme u omiljene dodaje je i u glazbenoj biblioteci i u odjeljku datoteka istovremeno.
- **Izbriši popis** — izbrišite cijeli popis omiljenih pjesama.
- **Izvezi popis pjesama** — kao i Nedavne, izvezite omiljene kao M3U, CSV ili TXT.

### Izbriši glazbenu biblioteku

Obrišite bazu podataka glazbene biblioteke. Glazbene datoteke u pohrani ostaju netaknutima.

## Lozinka

Aktivirajte zaslon lozinke za zaštitu podataka aplikacije s 4-znamenkastom numeričkom lozinkom. Kada je omogućeno, od vas će se tražiti unos lozinke svaki put kad se aplikacija pokrene. Kombinirajte s iOS Face ID / Touch ID na uređaju za dodatnu zaštitu.

## Upravitelj datoteka

Odjeljak Upravitelja datoteka kontrolira kako se datoteke prenose, pohranjuju i pregledavaju.

### Prijenosi datoteka

Odaberite mrežne preferencije za preuzimanje datoteka na uređaj.

### Maksimalni broj paralelnih zadataka

Postavite broj paralelnih niti preuzimanja. Veći broj ubrzava preuzimanja ali troši više baterije.

### Zadaci prijenosa datoteka

Prikazuje trenutno aktivne zadatke prijenosa i preuzimanja.

### Prijenosi u pozadini

Dopustite preuzimanja dok je aplikacija u pozadini. Ako prijenosi u pozadini troše puno energije, iOS može suspendirati aplikaciju.

### Spremi preuzete datoteke u

Odaberite zadani direktorij za preuzimanja, ili neka aplikacija pita svaki put.

### Sinkronizirane offline mape

Upravljajte offline sinkronizacijom za odabrane mape. Za omogućavanje offline sinkronizacije, tapnite gumb s tri točkice pored mape i odaberite **Dostupan offline način rada**. Nove datoteke dodane u cloud mapu automatski se preuzimaju na uređaj. Pročitajte više o offline načinima rada [ovdje](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Vremenski interval

Odaberite koliko često se sinkroniziraju offline mape. **Odmah** pokreće sinkronizaciju svaki put kada otvorite aplikaciju.

### Prikaži pune nazive datoteka

Prikažite potpune nazive datoteka, uključujući nastavke, u upravitelju datoteka.

### Uredi online datoteke

Onemogućite uređivanje online datoteka za prebacivanje u način rada samo za čitanje za spojene cloud usluge i sprečavanje slučajnog brisanja. Ova radnja uklanja operacije uređivanja datoteka iz korisničkog sučelja.

### Kopiraj datoteke pri otvaranju

Odredite kako aplikacija obrađuje uvezene datoteke iz drugih aplikacija.

### Minijature za datoteke

Upravljajte i brišite generirane minijature datoteka za oslobađanje prostora za pohranu.

### Izbriši privremene datoteke

Očistite predmemoriju aplikacije za povrat prostora za pohranu.

## Editor audio oznaka

Konfigurirajte ugrađeni editor audio oznaka — praktično za skupno ispravljanje problema s izvođačem / albumom / godinom / žanrom / omotom albuma na cloud i lokalnim datotekama.

### Skaliranje omota albuma

Odaberite metodu skaliranja koja se koristi kada se omot albuma sprema u audio oznake.

### Ažuriraj online datoteke

Kada je omogućeno, aplikacija automatski ažurira metapodatke datoteke na cloud poslužitelju nakon što završite uređivanje.

### Izbriši datoteku nakon uređivanja online

Odaberite treba li aplikacija izbrisati preuzetu kopiju nakon završetka uređivanja online datoteke na cloud poslužitelju.

### Gumbi na glavnom zaslonu

Odaberite koji gumbi su vidljivi na glavnom zaslonu editora audio oznaka.

Za dublje skupno uređivanje kroz mnoge datoteke odjednom, instalirajte naš prateći app **Evertag**.

## Widgeti

Omogućite widgete kako bi aplikacija ažurirala podatke widgeta tijekom reprodukcije. Ažuriranja widgeta zahtijevaju dodatnu energiju, pa je prekidač prema zadanoj postavci isključen — omogućite ga samo ako zapravo koristite widgete na Početnom zaslonu ili Zaslonu zaključavanja.

Flacbox widgete možete dodati dugim pritiskom na Početni zaslon ili Zaslon zaključavanja, tapnutjem **+**, pretraživanjem za **Flacbox** i odabirom veličine widgeta. Widgeti prikazuju trenutni omot, naslov zapisa i izvođača te izravno tapnuti do playera na cijelom zaslonu. Widgeti rade i na macOS-u u Centru obavijesti.

## CarPlay

Promijenite CarPlay postavke ovdje. Ovaj izbornik dostupan je i unutar CarPlay sučelja kako biste mogli prilagoditi iskustvo tijekom vožnje.

### Sortiraj

Konfigurirajte opcije sortiranja za sve CarPlay zaslone.

### Ograničenje učitavanja sadržaja

Odaberite koristi li aplikacija paginaciju na CarPlay zaslonu. Paginacija održava responzivnost izbornika na velikim bibliotekama.

### Boja gradijenta ikona izbornika

Odaberite shemu boja za CarPlay početni zaslon.

### Prikaži slike

Onemogućite slike na CarPlay zaslonu za optimizaciju brzine učitavanja i smanjenje upotrebe memorije na velikim bibliotekama.

### Pauziraj reprodukciju pri spajanju

Omogućite ovo za izbjegavanje iznenadnog glasnog zvuka kada spojite uređaj na CarPlay.

## Wi-Fi Drive

Aktivirajte **Wi-Fi Drive** za prijenos datoteka s računala na uređaj koristeći desktop web preglednik, Finder ili File Explorer. Detaljne upute o tome kako koristiti Wi-Fi Drive dostupne su [ovdje](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalizacija

Prilagodite korisničko sučelje prema vašim preferencijama.

### Ikona aplikacije

Odaberite alternativnu ikonu aplikacije za Početni zaslon (Premium).

### Shema boja

Odaberite temu korisničkog sučelja i omogućite tamni način rada. Kada je odabrano **Zadano**, aplikacija prati postavke izgleda cijelog uređaja.

### Stil pozadine

Izmijenite stil pozadine aplikacije. Trenutno je jedina opcija **Zamućeni omot albuma**, koji koristi omot trenutno puštanog zapisa kao zamućenu pozadinu aplikacije.

### Izgled stavki na popisu

Podesite kako se stavke prikazuju na popisima. Korisno na malim zaslonima — možete dopustiti aplikaciji da automatski prilagodi visinu redaka prema sadržaju, ili prikazati manje ikone u ćelijama popisa kako biste tekstu dali više prostora.

### Ograničenje učitavanja sadržaja

Prema zadanoj postavci, aplikacija koristi paginaciju za ubrzavanje učitavanja sadržaja. Možete onemogućiti paginaciju za učitavanje svega odjednom.

### Stil zaslona Lokalnih datoteka

Promijenite stil prezentacije odjeljka **Lokalne datoteke**.

### Stil zaslona Glazbene biblioteke

Prilagodite izgled zaslona **Glazbena biblioteka**.

### Stil zaslona Audio playera

Konfigurirajte izgled zaslona **Audio player**.

### Stil kontekstnog izbornika

Odaberite stil kontekstnog izbornika prikazanog kada tapnete gumb **Više radnji**.

## Prozor

Dostupno na Macu i Catalystu. Konfigurirajte preferencije vezane uz prozor poput zadane veličine i ponašanja pri pokretanju.

## Zaslon

Odaberite treba li zaslon ostati aktivan dok koristite aplikaciju. Korisno pri skeniranju velikih biblioteka ili dugotrajnom radu uređivanja oznaka.

## Pristupačnost

Aktivirajte **Tekstualni način rada** za skrivanje svih slika u korisničkom sučelju. Tekstualni način rada automatski se omogućuje kada je VoiceOver aktivan i koristan je i za vrlo male ili postavke samo s tekstom.

## Jezik

Promijenite jezik aplikacije i zaobiđite zadanu sistemsku postavku. Promjena se primjenjuje nakon potpunog zatvaranja i ponovnog otvaranja Flacboxa. Trenutno podržani prijevodi uključuju: afrikaans, akan, albanskki, amharski, arapski, armenski, asamski, aymara, azerbajdžanski, bambara, bengalski, baskijski, bjeloruski, bosanski, bugarski, burmanski, katalonski, cebuano, kineski (pojednostavljeni), kineski (tradicionalni), korzikanski, hrvatski, češki, danski, dhivehi, dogri, nizozemski, engleski, esperanto, estonski, ewe, filipinski, finski, francuski, galicijski, ganda, gruzijski, njemački, grčki, guarani, gujarati, haitski kreolski, hauski, havajski, hebrejski, hindski, hmong, mađarski, islandski, igbo, iloko, indonezijski, irski, talijanski, japanski, javanski, kannadski, kazahstanski, kmerski, kinyarwanda, korejski, krio, kurdski, kurdski sorani, kirgiski, laoški, latinski, latvijski, lingala, litvanski, luksemburški, makedonski, maithili, malagaški, malajski, malajalamski, malteški, maorski, marathski, mizo, mongolski, nepalski, sjeverni sotho, norveški bokmål, njanja, odiya, oromo, pašto, perzijski, poljski, portuganski, pandžabski, rumunjski, ruski, samoanski, sanskrit, škotski galski, srpski, shona, sindhi, sinhala, slovački, slovenski, somalijski, južni sotho, španjolski, sundanski, suaheli, švedski, tadžički, tamilski, tatarski, telugu, tajlandski, tsonga, turski, turkmenski, ukrajinski, urdski, ujgurski, uzbekistanski, vijetnamski, velški, xhosa, jidiš, joruba, zulu.

## Sigurnosna kopija i obnova

Koristite ovu funkciju za sigurnosno kopiranje svih podataka aplikacije ili za migraciju na drugi uređaj. Možete odabrati što uključiti:

- **Baza podataka** — svi zapisi u glazbenoj biblioteci, uključujući popise. Offline zapisi nisu uključeni kako bi se veličina datoteke sigurnosne kopije zadržala razumnom.
- **Omovi albuma** — svi predmemorirani omovi albuma.
- **Postavke** — sve postavke aplikacije.

Tapnite **Sigurnosna kopija podataka aplikacije** za pokretanje sigurnosnog kopiranja. Podaci aplikacije zapisuju se u jednu datoteku koju možete koristiti za obnovu stanja aplikacije na novom uređaju ili nakon reinstalacije aplikacije.

Za obnovu podataka aplikacije na novom uređaju, premjestite datoteku sigurnosne kopije na novi uređaj koristeći spojenu cloud uslugu ili iCloud i otvorite je na novom uređaju.

Detaljne upute korak po korak: [Kako prenijeti glazbenu biblioteku između uređaja: Vodič korak po korak](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Pomoć

Pristupite vodiču aplikacije za pomoć i smjernice za učinkovito korištenje aplikacije.

## Česta pitanja

Pronađite odgovore na uobičajena pitanja u odjeljku Česta pitanja.

## Pošalji povratne informacije

Imate povratne informacije ili trebate pomoć? Pošaljite povratne informacije izravno timu za podršku iz aplikacije.

## Podijeli ovu aplikaciju

Podijelite aplikaciju s prijateljima za širenje vijesti.

## Otkrijte više aplikacija

Istražite druge aplikacije od Everappza.

## Uvjeti i odredbe

Opisuje uvjete i odredbe za korištenje aplikacije. Molimo pročitajte ih prije korištenja aplikacije.

## Politika privatnosti

Posjetite stranicu politike privatnosti kako biste razumjeli naše prakse rukovanja podacima. Molimo pročitajte je prije korištenja aplikacije.

## Analitika i prikupljanje podataka

Provjerite koje su usluge omogućene za analitiku i prikupljanje podataka i deaktivirajte one koje ne želite.

## Pravne napomene

Sadrži informacije o svakoj biblioteci korištenoj u aplikaciji zajedno s brojem verzije aplikacije i informacijama o izgradnji.
