---
title: "Glazbena biblioteka"
date: 2020-02-01
description: "Naučite kako izgraditi, organizirati i sinkronizirati glazbenu biblioteku u Flacboxu na iPhoneu, iPadu i Macu. Dodajte zapise ručno ili sinkronizirajte iz cloud usluga, upravljajte metapodacima, omovima albuma, popisima pjesama, omiljenima, nedavnima i zabilješkama. Uključuje podršku za Hi-Res audio, MusicBrainz editor oznaka, online i offline sinkronizaciju te opcije personalizacije."
keywords: [
  "Flacbox glazbena biblioteka", "sinkronizacija glazbe iz clouda", "organizacija glazbenih metapodataka",
  "uređivanje audio oznaka Flacbox", "offline sinkronizacija glazbe", "uvoz lokalne glazbe",
  "upravljanje popisima pjesama Flacbox", "pretraga omova albuma Flacbox",
  "iPhone glazbeni metapodaci", "vodič za Flacbox aplikaciju",
  "Flacbox MusicBrainz", "Flacbox normalizacija oznaka",
  "Flacbox hi-res glazbena biblioteka", "Flacbox FFmpeg biblioteka",
  "Flacbox solo albumi", "prikaz skladatelja Flacbox"
]
tags: ["glazba", "vodič", "flacbox", "biblioteka"]
readingTime: 11
---


Upravljanje glazbenom bibliotekom s Flacboxom je lako — možete bez napora organizirati sve svoje zapise — lokalne FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE i desetke drugih formata — u jednu pretraživu kolekciju. Imate dvije opcije za izgradnju glazbene biblioteke: ručno dodavanje (vi birate što se dodaje) ili automatska sinkronizacija (Flacbox skenira određene cloud mape i automatski dodaje nove datoteke čim se pojave).

{{< cards cols="1">}}
  {{< card title="" subtitle="Prikaz albuma glazbene biblioteke u Flacboxu" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Ručno dodavanje

Za ručno dodavanje zapisa, tapnite ikonu **Dodaj glazbu** smještenu u gornjem lijevom kutu i odaberite mape ili datoteke iz spojene usluge cloud pohrane ili datoteke smještene na vašem uređaju. Kada dodajete zapise u biblioteku, stvaraju se samo veze na te zapise — stvarne datoteke ostaju na originalnim lokacijama kako bi se sačuvao dragocjeni prostor na disku. Ako želite zapise učiniti dostupnima offline, možete koristiti radnju Preuzmi iz izbornika opcija ili omogućiti Offline način rada za popise pjesama i kolekcije zapisa.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dodavanje pjesama u glazbenu biblioteku u Flacboxu" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

Na Mac verziji možete i povlačiti i ispuštati datoteke u biblioteku, ili koristiti **Otvori datoteke…** / **Otvori mapu…** iz sistemskog birača datoteka na iPhoneu i iPadu.

## Nastavi reprodukciju

Obnovite red čekanja audio playera od posljednje spremljene pozicije ako je ova funkcija omogućena u postavkama aplikacije. Omogućite i **Spremi stanje audio playera** i **Spremi poziciju reprodukcije** u Postavke → Audio player → Općenito za najbolje iskustvo. Jednom kada je omogućeno, gumb **Nastavi reprodukciju** pojavljuje se na vrhu svakog zaslona mape, albuma, izvođača, žanra i popisa pjesama — tapnite ga za skok ravno na točan zapis i poziciju na kojoj ste zadnje bili.

## Lokacije

Svi zapisi u vašoj biblioteci su promišljeno grupirani prema vrsti izvora i glazbenim oznakama. Možete filtrirati pjesme prema lokaciji koristeći gumb **Više radnji** u gornjem desnom kutu i odabirom **Filtriraj**.

### Online glazba

Ovaj odjeljak prikazuje glazbu iz vaših spojenih cloud usluga pohrane. Zapisi ovdje se streamaju na zahtjev; ništa ne zauzima lokalnu pohranu dok je eksplicitno ne preuzmete ili ne omogućite offline način rada.

### Datoteke u ovoj aplikaciji

Ovdje možete pronaći glazbu dostupnu za offline reprodukciju, s izvorom iz lokalnih datoteka. To uključuje datoteke u direktoriju Dokumenti aplikacije — sve što ste preuzeli, prenijeli putem Wi-Fi Drive-a ili uvezli putem Finder File Sharinga.

### Datoteke na ovom iPhoneu / iPadu / Macu

Ova kategorija uključuje glazbu uvezenu u aplikaciju s vašeg uređaja, dodanu putem sistemskog dijaloga **Otvori datoteke…**. Originalne datoteke ostaju na originalnoj lokaciji; Flacbox samo čuva vezu na njih.

## Kategorije

Kada dodajete zapise u glazbenu biblioteku, aplikacija automatski čita njihove audio oznake i organizira ih u kategorije poput Pjesama, Nepuštenih pjesama, Albuma, Izvođača albuma, Izvođača, Žanrova i Skladatelja.

## Grupiranje oznaka

Te kategorije pomažu organizirati zapise prema glazbenim oznakama. Kada dodajete zapise u glazbenu biblioteku, aplikacija čita njihove metapodatke i grupira ih po tim kategorijama. Ako ne vidite sve albumei, provjerite je li aplikacija skenirala svaki zapis. Možete provjeriti napredak skeniranja u Postavke → Glazbena biblioteka → Čitanje metapodataka → Broj obrađenih datoteka u glazbenoj biblioteci. Za lokalne datoteke možete i ponovo skenirati offline mape u Postavke → Glazbena biblioteka → Sinkronizacija offline mapa → Pokreni skeniranje lokalnih mapa. Nakon što čitač metapodataka dovrši sve operacije, vidjet ćete sljedeće kategorije u glazbenoj biblioteci:

- **Pjesme** — sve pjesme grupirane po oznaci TRACK_TITLE. Redoslijed sortiranja možete provjeriti koristeći izbornik Više radnji u gornjem desnom kutu.
- **Nepuštene pjesme** — sve pjesme koje nikada nisu puštene.
- **Albumi** — pjesme grupirane po oznaci ALBUM_NAME, ignorirajući oznake izvođača, izvođača albuma i skladatelja. Ako imate nekoliko albuma s istim nazivom ali različitim izvođačima, razmotrite korištenje sortiranja Ekskluzivni albumi opisanog u nastavku.
- **Izvođači albuma** — pjesme grupirane samo po ALBUM_ARTIST_TAG. Korisno za uredno odvajanje kompilacija i suradnji od solo radova.
- **Izvođači** — pjesme grupirane samo po ARTIST_TAG.
- **Žanrovi** — pjesme grupirane po oznaci GENRE.
- **Skladatelji** — pjesme grupirane po oznaci COMPOSER — neprocjenjivo za biblioteke klasične glazbe gdje je "skladatelj" primarni navigacijski osi.

## Omiljeni

Možete označiti pjesme kao omiljene na zaslonu audio playera ili koristeći izbornik opcija. Omiljeni se pojavljuju u svom odjeljku tako da ih možete pronaći jednim tapnutjem.

## Nedavne

Ovaj odjeljak prikazuje sve nedavno puštene zapise. Možete prilagoditi koliko stavki popis nedavnih čuva u Postavke → Biblioteka → Nedavne → Promijeni veličinu popisa, te izvesti popis u M3U / CSV / TXT za sigurnosno kopiranje povijesti slušanja.

## Zabilješke

Možete stvarati audio zabilješke dok se pjesma reproducira i upravljati njima na ovom zaslonu — savršeno za audioknjige, duge mješavine, predavanja ili samo označavanje refrena omiljenog zapisa. Detaljne upute za rad s audio zabilješkama dostupne su [ovdje](/docs/guide/evermusic/evermusic-guide-music-library).

## Gornja alatna traka

Smještena neposredno ispod navigacijske trake, gornja alatna traka nudi nekoliko praktičnih radnji: Pretraži, Pusti sve, Reproduciraj sve nasumično i Nastavi reprodukciju. Ovu alatnu traku možete otkriti ili sakriti jednostavnim gestom povlačenja prema dolje.

## Pretraži

Funkcija pretraživanja omogućuje vam lociranje određenog zapisa, izvođača, albuma ili žanra unutar vaše glazbene biblioteke. Na zaslonu Pretraži imate pristup radnjama Sortiraj, Filtriraj i Mreža / Popis. Pretraga se izvodi lokalno u bazi podataka glazbene biblioteke, pa radi u potpunosti offline i vraća rezultate dok tipkate.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pretraga glazbene biblioteke u Flacboxu" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Izbornik opcija

Svaka pjesma u glazbenoj biblioteci ima izbornik s više radnji, kojima se pristupa tapnutjem na gumb s tri točkice pored naslova pjesme. Te radnje variraju ovisno o tome radi li se o pojedinačnoj pjesmi ili dijelu kolekcije.

### Za pojedinačne pjesme

- **Pusti sljedeće** — dodaje pjesmu na vrh reda čekanja playera.
- **Pusti poslije** — dodaje pjesmu na dno reda čekanja playera.
- **Dodaj u popis pjesama** — dodaje pjesmu u popis pjesama.
- **Dodaj u omiljene** — označava pjesmu kao omiljenu za brzi pristup.
- **Preuzmi** — sprema pjesmu u lokalne datoteke. Pojavljuje se na kartici **Lokalne datoteke** i u odjeljku **Offline glazba**.
- **Uredi audio oznake** — otvara ugrađeni editor audio oznaka za ispravljanje nedostajućih metapodataka; imajte na umu da će to promijeniti pjesmu na vašem serveru.
- **Prikaži u mapi** — otkriva mapu u kojoj je pohranjena audio datoteka.
- **Prikaži u Finderu** — za datoteke uvezene s Maca, ova radnja otkriva mapu u kojoj se audio datoteka nalazi na Macu.
- **Otvori u** — izvozi audio datoteku u drugu aplikaciju.
- **Izbriši iz cloud usluge** — uklanja datoteku i iz glazbene biblioteke i iz cloud pohrane. **Ova radnja je nepovratna.**
- **Izbriši iz glazbene biblioteke** — briše pjesmu iz glazbene biblioteke, ali datoteka ostaje u pohrani. Ako je automatska sinkronizacija omogućena i datoteka postoji na udaljenoj pohrani, ponovo će se pojaviti u biblioteci nakon operacije sinkronizacije.

### Za kolekcije pjesama

Za kolekcije pjesama poput Albuma, Izvođača, Žanrova ili Skladatelja, izbornik opcija uključuje sljedeće radnje.

- **Pusti sve** — zamjenjuje red čekanja playera pjesmama iz odabrane kolekcije.
- **Pusti sljedeće** — dodaje pjesme iz ove kolekcije na vrh reda čekanja playera.
- **Pusti poslije** — dodaje pjesme iz ove kolekcije na dno reda čekanja playera.
- **Dodaj u popis pjesama** — uključuje pjesme iz ove kolekcije u popis pjesama, s opcijom stvaranja novog.
- **Omogući offline način rada** — preuzima pjesme iz ove kolekcije u lokalne datoteke. Datoteke se pojavljuju na kartici **Lokalne datoteke** i u odjeljku **Offline glazba**. Ako se nove stavke dodaju u kolekciju na poslužitelju, automatski će se preuzeti.
- **Uredi sliku** — promijenite omot albuma za kolekciju pjesama.
- **Dodaj u arhivu** — spakirajte cijelu kolekciju u jednu ZIP datoteku za lako sigurnosno kopiranje ili prijenos (Premium funkcija).
- **Izvezi popis pjesama** — izvezite kolekciju u M3U, CSV ili TXT za korištenje u drugim playerima ili za arhiviranje.
- **Izbriši iz glazbene biblioteke** — uklanja kolekciju pjesama iz glazbene biblioteke. Ova radnja ne briše stvarne datoteke iz pohrane. Ako je automatska sinkronizacija omogućena i datoteke postoje na udaljenoj pohrani, ponovo će se pojaviti u biblioteci nakon operacije sinkronizacije.

## Način odabira

Možete aktivirati način odabira koristeći gumb Više radnji u gornjem desnom kutu. U ovom načinu rada možete odabrati više zapisa odjednom i izvoditi skupne radnje — dodati u popis pjesama, označiti kao omiljene, izbrisati iz biblioteke, preuzeti i još mnogo toga.

## Detalji albuma

Kada otvorite odjeljke Izvođač, Izvođač albuma ili Skladatelj, možete vidjeti prebacivač za Pjesme / Svi albumi / Ekskluzivni albumi / Solo albumi.

- **Pjesme** — prikazuje sve pjesme u kojima se ovaj Izvođač / Izvođač albuma / Skladatelj pojavljuje u audio oznakama.
- **Svi albumi** — prikazuje kompilacijske albume i sve albume u kojima je izvođač prisutan.
- **Ekskluzivni albumi** — prikazuje albume na kojima je navedeni izvođač jedini izvođač s tim nazivom albuma.
- **Solo albumi** — prikazuje albume na kojima se pojavljuju samo zapisi navedenog izvođača, čak i ako drugi izvođači imaju albume s istim nazivom.

Ovo je posebno korisno za čišćenje zakrčenih kompilacija "Raznih izvođača" u velikim bibliotekama.

{{< cards cols="1">}}
  {{< card title="" subtitle="Zaslon detalja albuma u Flacboxu" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Postavke

Tapnite Više radnji → Postavke za konfiguraciju preferencija glazbene biblioteke.

### Čitanje metapodataka

Kada dodajete zapise u biblioteku, čitač metapodataka se aktivira. Ovaj pozadinski proces čita sve metapodatke iz vaših zapisa i organizira ih po Izvođaču, Albumu, Žanru i Skladatelju. Možete prilagoditi brzinu čitanja metapodataka za brže učitavanje podataka — imajte na umu da brže čitanje troši više energije. Možete i potpuno onemogućiti čitač metapodataka i prikazivati nazive datoteka umjesto informacija o oznakama.

Važno je napomenuti da čitač metapodataka samo ažurira metapodatke u vašoj glazbenoj biblioteci i ne mijenja datoteke pohranjene u vašem cloud računu ili lokalnoj pohrani. Ako želite urediti metapodatke za audio datoteke, to možete učiniti koristeći ugrađeni editor oznaka, koji možete aktivirati odgovarajućom radnjom u izborniku opcija.

### Dostupni načini rada za čitač metapodataka

- **Deaktivirano** — čitač metapodataka je isključen i prikazuju se nazivi datoteka umjesto podataka audio oznaka.
- **Trenutna pjesma** — aplikacija čita metapodatke samo za trenutno puštenu pjesmu. Koristite ovu opciju ako imate sporu mrežnu vezu kako biste spriječili da čitač metapodataka šalje mnoge zahtjeve na cloud poslužitelj, što može uzrokovati prekide reprodukcije.
- **Red čekanja reprodukcije** — aplikacija čita metapodatke za sve pjesme u redu čekanja audio playera.
- **Biblioteka** — aplikacija čita metapodatke za sve pjesme u glazbenoj biblioteci.

Kada je uključen prekidač **Čitanje metapodataka u pozadini**, čitač metapodataka nastavlja raditi u pozadinskom načinu rada. Imajte na umu da ako aplikacija troši puno energije tijekom audio reprodukcije, iOS operativni sustav može je suspendirati.

Dakle, ako imate veliku glazbenu kolekciju, preporučljivo je koristiti desktop verziju aplikacije za sinkronizaciju metapodataka. Zatim možete koristiti funkciju Sigurnosna kopija i obnova podataka u postavkama aplikacije za prijenos sinkronizirane biblioteke s deskopa na mobitel.

Kada je omogućena opcija **Normalizacija kodiranja metapodataka**, aplikacija automatski normalizira kodiranje metapodataka za sve pjesme u glazbenoj biblioteci. Ovo ispravlja probleme gdje je kodiranje audio oznaka pokvareno (npr. nakon uređivanja datoteka na Windows PC-u) i sprječava pojavu netočnih znakova u informacijama o zapisima.

Radnja **Ponovo učitaj metapodatke** označava svaku datoteku u glazbenoj biblioteci kao datoteku s nedostajućim metapodacima, što pokreće čitač metapodataka za osvježavanje svakog zapisa.

Tapnite **Pokreni čitanje metapodataka** za ručno pokretanje čitača. Napredak operacije prikazan je ispod.

### Online sinkronizacija

Automatska online sinkronizacija glazbe omogućuje automatsko dodavanje zapisa iz spojenih cloud usluga u glazbenu biblioteku. Za aktiviranje ove funkcije, idite na Postavke glazbene biblioteke i odaberite mape za sinkronizaciju.

S ovom opcijom omogućenom, aplikacija skenira sve odabrane mape, identificira podržane audio datoteke i besprijekorno ih integrira u vašu biblioteku. Možete pokrenuti ili zaustaviti sinkronizaciju tapnutjem na odgovarajuću radnju izbornika.

Online sinkronizacija glazbe radi isključivo kada je aplikacija u prvom planu, što znači da sinkronizacija velike biblioteke može potrajati. Za ubrzavanje procesa, ostavite aplikaciju otvorenom, spojite je na izvor napajanja i omogućite Zaslon → Uvijek aktivan u postavkama aplikacije.

Alternativno, možete provesti online sinkronizaciju glazbe na desktop verziji aplikacije i prenijeti glazbenu biblioteku na iOS verziju koristeći funkciju Sigurnosna kopija i obnova.

Možete i postaviti koliko često želite sinkronizirati online glazbenu biblioteku. Ako postavite interval na Odmah, online sinkronizacija će se pokrenuti svaki put kad otvorite aplikaciju.

### Offline sinkronizacija

Ovdje možete konfigurirati offline sinkronizaciju glazbe.

#### Sinkronizirane offline mape

Kada cloud mapu učinite dostupnom offline (putem izbornika Više radnji), ona se pojavljuje u odjeljku Lokalne datoteke → Offline mape. Aplikacija preuzima njezin sadržaj na vaš uređaj. Ako napravite promjene u mapi na cloudu — poput dodavanja, uklanjanja ili ažuriranja datoteka — aplikacija otkriva te promjene i automatski ažurira lokalnu kopiju.

Na ovom zaslonu možete ručno pokrenuti sinkronizaciju offline mape, otkriti offline mapu u njezinoj nadređenoj mapi i onemogućiti offline način rada za mapu. Onemogućavanje offline načina rada uklanja sve lokalne kopije datoteka s vašeg uređaja.

#### Vremenski interval

Možete postaviti vremenski interval za to koliko često aplikacija treba provjeravati offline mape za izmjene.

#### Pokreni skeniranje lokalnih mapa

Ova opcija skenira sve lokalne mape smještene u direktoriju Dokumenti aplikacije za pronalaženje podržanih audio datoteka. Sve te lokalne datoteke besprijekorno se dodaju u glazbenu biblioteku. Lokalne datoteke smještene na vašem uređaju, ali izvan ove aplikacije, moraju se ručno dodati u glazbenu biblioteku, budući da aplikacija nema pristup datotekama izvan direktorija Dokumenti aplikacije zbog sigurnosnih ograničenja iOS-a / macOS-a.

#### Važno

Preporučljivo je povremeno pokrenuti offline sinkronizaciju glazbe kako biste svoju glazbenu biblioteku održavali ažuriranom s lokalnim datotekama.

### Personalizacija

U ovom odjeljku možete konfigurirati stil zaslona glazbene biblioteke prema vašim preferencijama. Dostupne su tri opcije: Jednostavni izbornik, Grupirani izbornik, Izbornik s karticama. Možete i omogućiti ili onemogućiti prikazivanje omova albuma na zaslonima detalja albuma.

### Omovi albuma

Ovdje možete konfigurirati kako aplikacija učitava i pohranjuje omove albuma.

- **Vrsta mreže** — odaberite Wi-Fi ili Wi-Fi i mobilni podaci za preuzimanje omova.
- **Učitaj omove albuma za online datoteke** — kada je omogućeno, ugrađeni omovi albuma učitavaju se za datoteke pohranjene u cloud pohrani. To može koristiti dodatne mrežne podatke.
- **Pretraži u mapi** — kada je omogućeno, ako zapis nema ugrađeni omot, aplikacija traži JPEG ili PNG slike u istoj mapi i koristi ih kao omot albuma.
- **Kvaliteta omota** — odaberite kvalitetu omova albuma pohranjenih na vašem uređaju.
- **Prikaži u mapi** — otvorite mapu u kojoj su predmemorirani omovi albuma kako biste njima upravljali ili ih sigurnosno kopirali.
- **Izbriši sve** — izbrišite predmemorirane omove albuma za oslobađanje prostora i prisilite aplikaciju da ih ponovo učita na zahtjev.

Prema zadanoj postavci, aplikacija provjerava ugrađene omove albuma u vašim zapisima i prikazuje ih ako su dostupni. Ako nema ugrađenih omova albuma i opcija **Pretraži u mapi** je omogućena, aplikacija provjerava nadređenu mapu za JPEG ili PNG slike i koristi ih kao omot albuma za sve zapise u toj mapi.

### Popisi pjesama

Možete omogućiti opciju dodavanja iste pjesme u popis pjesama dva puta. Prema zadanoj postavci, ova opcija je onemogućena.

### Nedavne

Možete upravljati popisom nedavno puštenih pjesama.

- **Izbriši popis** — izbrišite cijeli popis nedavno puštenih pjesama.
- **Promijeni veličinu popisa** — postavite broj stavki koje se pojavljuju na popisu.
- **Izvezi popis pjesama** — izvezite popis nedavno puštenih pjesama u M3U, CSV ili TXT. Detaljne upute dostupne su [ovdje](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Omiljeni

Možete upravljati popisom omiljenih pjesama.

- **Istovremeno uređivanje** — kada je omogućeno, dodavanje pjesme u omiljene dodaje je i u glazbenoj biblioteci i u odjeljku datoteka istovremeno.
- **Izbriši popis** — izbrišite cijeli popis omiljenih pjesama.
- **Izvezi popis pjesama** — slično kao Nedavne, izvezite popis omiljenih u M3U, CSV ili TXT.

### Izbriši biblioteku

Ova radnja će obrisati bazu podataka glazbene biblioteke, ali će ostaviti vaše glazbene datoteke netaknutima u pohrani.

### Ograničenje učitavanja sadržaja

Prema zadanoj postavci, aplikacija koristi paginaciju za smanjenje vremena učitavanja sadržaja i održavanje responzivnosti velikih biblioteka. Međutim, možete onemogućiti ovu opciju i dozvoliti aplikaciji da odjednom učita sve dostupne podatke. Za to otvorite postavke aplikacije, pomaknite se prema dolje na Personalizacija → Ograničenje učitavanja sadržaja i odaberite Deaktivirano.
