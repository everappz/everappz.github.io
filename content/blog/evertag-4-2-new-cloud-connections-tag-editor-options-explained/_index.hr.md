---
title: "Evertag 4.2: nove veze s oblakom, postavke uređivača oznaka objašnjene"
date: 2026-05-09
description: "Evertag 4.2 dodaje veze prema Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP i NFS, osvježuje Wi-Fi Drive i prilagođava sučelje za Liquid Glass. Ovaj članak također objašnjava svaku postavku uređivača oznaka — uključujući ID3v2.4 vs ID3v2.3, skaliranje omota albuma, dupliciranje oznaka, načine učitavanja u oblak i prave opcije za Spotify i druge usluge streaminga."
keywords: ["Evertag 4.2", "ažuriranje Evertag", "ID3 uređivač oznaka iPhone", "ID3v2.4 vs ID3v2.3", "uređivanje FLAC oznaka iOS", "uređivanje MP3 oznaka iPhone", "uređivanje omota albuma iOS", "uređivač oznaka za Spotify", "uređivač oznaka Plex", "uređivač oznaka Apple Music", "Evertag uređivač oznaka u oblaku", "uređivač oznaka Internxt", "uređivač oznaka Proton Drive", "uređivač oznaka QNAP", "uređivač oznaka Nextcloud", "uređivač oznaka Amazon S3", "SFTP uređivač oznaka iPhone", "FTP audio uređivač oznaka", "NFS uređivač oznaka iPhone", "Wi-Fi Drive uređivač oznaka", "dupliciranje ID3 oznaka", "skaliranje omota", "dizajn Liquid Glass", "uređivač audio metapodataka iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Uređivač oznaka", "ID3", "ID3v2.4", "ID3v2.3", "FLAC oznake", "MP3 oznake", "Omot albuma", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Što je novo"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**Ukratko:** [Evertag 4.2](/products/evertag) je veliko ažuriranje uređivača audio oznaka za iPhone, iPad i Mac. Riješili smo ključne pogreške u uređivanju oznaka i dodali više od 6 novih veza s oblakom i poslužiteljima — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3** plus protokoli **FTP**, **SFTP** i **NFS**. Wi-Fi Drive je dobio osvježeno sučelje, način višestrukog odabira, pametniji red prijenosa i brže prijenose. Cijela aplikacija prilagođena je dizajnu **Liquid Glass**. Ovaj članak također ulazi duboko u postavke uređivača oznaka u Evertagu — objašnjavajući **ID3v2.4 vs ID3v2.3**, **skaliranje omota albuma**, **dupliciranje oznaka**, **načine učitavanja u oblak**, **brisanje preuzete datoteke** i točno koje opcije odabrati ako pripremate audio za **Spotify**, **Apple Music**, **Plex**, **Jellyfin** ili bilo koju drugu uslugu streaminga.

---

## Pozdrav svima!

Veliko ažuriranje Evertaga je tu. Riješili smo ključne pogreške u uređivanju oznaka i dodali **više od 6 novih veza s oblakom i poslužiteljima** kako bi upravljanje vašim audio metapodacima bilo lakše nego ikad — bilo da vaša biblioteka živi u oblaku usmjerenom na privatnost, na NAS-u koji sami hostate ili na generičkom FTP/SFTP/NFS poslužitelju.

[Preuzmite Evertag 4.2 s App Storea](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) ili ažurirajte sa svoje trenutne verzije.

## Proširena podrška za oblak i poslužitelje

Evertag se sada povezuje izvorno s širim rasponom mogućnosti oblaka i samohostiranog skladištenja. Možete uređivati ID3, MP4, FLAC, OGG i APE oznake na datotekama gdje god se nalazile.

### Pohrana u oblaku usmjerena na privatnost: Internxt i Proton Drive

Ako vam je važna end-to-end enkripcija i pohrana s nultim znanjem, dva najuglednija imena u oblacima usmjerenima na privatnost sada su izvorna u Evertagu:

- **Internxt** — španjolski cloud otvorenog koda, post-kvantno enkriptiran i u skladu s GDPR-om. Dostupna besplatna razina.
- **Proton Drive** — end-to-end enkriptirana pohrana od tvoraca Proton Maila i Proton VPN-a, sa sjedištem u Švicarskoj. Dostupna besplatna razina, plaćeni planovi za veće biblioteke.

Sada možete uređivati metapodatke izravno na audio datotekama pohranjenim u jednoj od tih usluga — datoteka ostaje enkriptirana tijekom prijenosa, a samo nove oznake zapisuju se natrag.

### Samohostirana rješenja: QNAP, Nextcloud, Amazon S3

Za korisnike koji vode vlastitu infrastrukturu:

- **QNAP** — izravna API veza s QNAP NAS uređajima. Uređujte oznake na datotekama na svom QNAP-u preko lokalnog Wi-Fi-ja ili udaljenog pristupa.
- **Nextcloud** — povežite se s bilo kojom Nextcloud instancom, samohostiranom ili upravljanom.
- **Amazon S3** — usmjerite Evertag na bilo koji S3 bucket (ili pohranu kompatibilnu s S3 poput Backblaze B2, Wasabi, MinIO, Cloudflare R2) i uređujte metapodatke na licu mjesta.

### Novi mrežni protokoli: FTP, SFTP, NFS

Evertag 4.2 dodaje tri klasična protokola za korisnike s prilagođenim poslužiteljima, homelabovima ili generičkim NAS uređajima:

- **SFTP (SSH File Transfer Protocol)** — pravi odgovor za **siguran udaljeni rad s oznakama na vlastitom poslužitelju**. SFTP radi povrh SSH-a, pa je cijeli prijenos (autentifikacija i audio podaci) enkriptiran. Ako imate VPS, namjenski poslužitelj ili Linux računalo kod kuće s SSH pristupom, možete uređivati oznake na udaljenim datotekama bez izlaganja ičega drugog. Podržava autentifikaciju lozinkom i ključem.
- **FTP** — dugogodišnji standard prijenosa datoteka. Korisno za starije kućne NAS uređaje koji izlažu FTP, ali nemaju nativnu API integraciju.
- **NFS (mrežni datotečni sustav)** — de facto protokol dijeljenja na Linuxu i većini NAS uređaja. Manji troškovi od SMB-a na istom hardveru.

> **Savjet:** SFTP je protokol koji želite za udaljeno uređivanje preko otvorenog interneta. FTP i NFS najbolje koristiti unutar lokalne mreže — ne izlažite ih internetu osim ako ih ne umotate u VPN.

## Nadogradnje Wi-Fi Drivea

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) je ugrađena značajka Evertaga za **bežični prijenos audio datoteka između računala i iPhonea ili iPada — bez iTunesa, bez kabela i bez računa za oblak**. Oba uređaja moraju biti na istoj Wi-Fi mreži.

U Evertagu 4.2 Wi-Fi Drive dobiva:

- **Osvježeno, moderno sučelje** — čišće, lakše čitljivo na prvi pogled i ažurirano za Liquid Glass.
- **Način višestrukog odabira** — odaberite više datoteka ili mapa i izvedite skupne radnje.
- **Pametniji red učitavanja** — bolja povratna informacija o napretku i otpornost na smetnje u mreži.
- **Poboljšana brzina i ukupna pouzdanost** — brži prijenosi za velike biblioteke.

To je najbrži način premještanja serije audio datoteka s računala na telefon, uređivanja njihovih oznaka i slanja natrag — bez ikakve usluge treće strane.

## Postavke uređivača oznaka: dubinski pregled

Ovo je dio koji većina korisnika nikada ne pročita — i dio koji odlučuje rade li vaše oznake svugdje ili samo u nekim aplikacijama. Otvorite Evertag i idite u dio **postavke uređivača audio oznaka**. Evo što svaka opcija zaista čini i koju odabrati ovisno o vašem cilju.

### Skaliranje omota albuma

Kada spremate omot albuma u audio datoteku, Evertag može skalirati sliku prije ugradnje. Dostupne opcije:

- **Mali** — najmanji utjecaj na veličinu datoteke, niža kvaliteta slike.
- **Srednji** — uravnotežen izbor za većinu korisnika.
- **Veliki** — visoka kvaliteta, prikladno za uređaje s velikim ekranima i CarPlay.
- **Vrlo veliki** — vrlo visoka kvaliteta, primjetan porast veličine datoteke.
- **Izvorni (Onemogućeno)** — ugrađuje omot u izvornoj rezoluciji. **Bez skaliranja.**

**Zašto to važi:**

- **Veća kvaliteta = veća datoteka.** Omot 3.000 × 3.000 piksela može dodati nekoliko MB svakom zapisu. Pomnoženo s cijelim albumom, opterećenje diska brzo se gomila.
- **Neki uređaji ne podnose dobro vrlo velike ugrađene slike.** Stariji uređaji, neki autoradijski sustavi i neki naslijeđeni desktop reproduktori mogu zapeti na omotima iznad ~1.500 px ili ih odbiti prikazati.
- **Za većinu tijekova rada u oblaku i streamingu**, **Srednji** ili **Veliki** je optimalna točka. Koristite **Izvorni** samo kad zaista trebate kvalitetu za arhivu ili pripremate datoteke za uređaj kojem vjerujete.

> Opcija veličine **Izvorni** dio je premium personalizacijske nadogradnje Evertaga. Standardne veličine (Mali/Srednji/Veliki/Vrlo veliki) su besplatne.

### Opcije spremanja oznaka: ID3v2.4 vs ID3v2.3

Ovo je najvažnija pojedinačna postavka za kompatibilnost. ID3v2 je format metapodataka koji se koristi unutar MP3 datoteka. Postoje dvije široko korištene verzije i razlikuju se u suptilnim, ali važnim detaljima.

#### ID3v2.4

- Noviji, podržava **UTF-8 tekstualno kodiranje** — pravilno rukovanje nelatiničnim pismima (kineski, ruski, japanski, arapski, hebrejski itd.).
- Više vrsta okvira (relativna glasnoća, postavke ekvalizatora itd.).
- **Preporučuje se za moderne uređaje** koji ga podržavaju.

#### ID3v2.3

- Stariji ali **najuniverzalnije podržana** verzija ID3-a.
- Ne podržava UTF-8 izravno (koristi UTF-16 za Unicode tekst).
- **Preporučuje se kada trebate maksimalnu kompatibilnost** sa starijim uređajima, autoradijima i nekim desktop aplikacijama.

#### Kada uključiti ID3v2.4 u Evertagu

- Koristite **moderne audio uređaje** poput Evermusica, Plexa, Jellyfina, Navidromea, foobar2000, VLC-a, Apple Musica (trenutne verzije) ili modernih Android uređaja. ✅ **Uključite ID3v2.4.**
- Vaša biblioteka sadrži **nelatinične znakove** (kineski, korejski, japanski, ruski, arapski, grčki, hebrejski). ✅ **Uključite ID3v2.4** — UTF-8 ih obrađuje mnogo čišće.

#### Kada isključiti ID3v2.4 u Evertagu (umjesto toga koristite ID3v2.3)

- Pripremate datoteke za **stariji autoradio ili in-dash jedinicu** koja ne čita oznake v2.4.
- Vidite **iskrivljeni tekst ili nedostajuće oznake** u nekim aplikacijama nakon uređivanja — to je snažan signal da v2.4 tamo nije podržan. Vratite se na v2.3.
- Ciljate na **naslijeđene desktop uređaje** ili starije prijenosne uređaje (rani iPodi, neki MP3 uređaji iz 2000–2010-ih).

> **Pravilo palca:** ako vaše oznake ispravno prikazuju svugdje s v2.4, ostavite je uključenom. Ako čak i jedan važan reproduktor pokazuje pogrešne znakove, prazne ili ne čita oznake, isključite v2.4 i ponovno spremite.

#### Dupliciranje oznaka

Kada uključite **Dupliciranje oznaka**, Evertag piše uobičajena polja metapodataka (naslov, izvođač, album itd.) u **oba odjeljka ID3v1 i ID3v2** datoteke. Ovo poboljšava kompatibilnost s vrlo starim uređajima koji čitaju samo ID3v1 (izvorna oznaka od 128 bajtova na kraju datoteke).

- **Većini korisnika ovo nije potrebno.** Moderni uređaji prvo čitaju ID3v2.
- **Uključite samo ako** se bavite vintage hardverom ili specifičnim softverom koji ignorira ID3v2.

### Ažuriranje online datoteka: kako Evertag rukuje uređivanjima u oblaku

Kada uređujete oznake na datoteci pohranjenoj na povezanom oblaku (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP itd.), Evertag mora prenijeti izmijenjenu datoteku natrag. Vi kontrolirate kako:

- **Prikaži poruku potvrde** *(zadano, preporučeno)* — Evertag pita prije prijenosa. Najbolje za oprezne korisnike i dijeljene biblioteke.
- **Automatski ažuriraj metapodatke datoteke** — tiho prenosi nakon svakog uređivanja. Najbolje za samostalne korisnike s brzim, pouzdanim vezama koji puno uređuju.
- **Ne ažuriraj metapodatke datoteke** — Evertag uređuje samo lokalnu kopiju. Korisno za pregled promjena bez slanja u oblak.

### Uređivanje online datoteka: čišćenje lokalne datoteke

Kako bi uređivao udaljenu datoteku, Evertag je prvo preuzima na vaš uređaj. Nakon uređivanja birate što će se dogoditi s tom lokalnom kopijom:

- **Uvijek izbriši preuzetu datoteku** — Evertag uklanja privremenu datoteku nakon uređivanja. **Preporučeno** ako imate malo prostora ili radite na tuđim datotekama.
- **Ne briši preuzetu datoteku** — zadržava uređenu datoteku na vašem uređaju. Korisno kad želite i offline kopiju i ažuriranu kopiju u oblaku.

### Gumbi na glavnom zaslonu

Glavni zaslon uređivača oznaka u Evertagu može prikazati ili sakriti gumbe za pojedinačne radnje. Aktivirajte samo one koje stvarno koristite kako biste sučelje držali fokusiranim:

- **Automatski potraži audio oznake** — pronalazi metapodatke koji nedostaju online na temelju audio otiska datoteke.
- **Ručno potraži audio oznake** — tražite po naslovu/izvođaču kada automatska pretraga promaši.
- **Pretraži omot albuma** — pronalazi i ugrađuje omote visoke kvalitete.
- **Spremi omot albuma** — izvozi ugrađeni omot u vašu foto biblioteku ili datoteke.
- **Normaliziraj kodiranje** — ispravlja oštećeni nelatinični tekst uzrokovan starim kodiranjima (vrlo korisno za ćirilične, kineske i japanske pjesme ripane starim softverom).
- **Izbriši audio oznake** — uklanja sve oznake iz datoteke. Korisno prije čistog ponovnog tagiranja.

### Prikaži proširene oznake

Aktivirajte ovo za prikaz cijelog skupa polja metapodataka iznad osnovnog naslov/izvođač/album/godina — uključujući BPM, dirigenta, izvornog izvođača, raspoloženje, autorska prava, koder, komentare, tekstove i još mnogo toga. Značajka za napredne korisnike; većini običnih korisnika nije potrebna.

### Uređivanje datoteka istovremeno

Kad je omogućeno, Evertag vam omogućuje uređivanje metapodataka na **više odabranih datoteka odjednom** — postavite isti album artist, godinu ili žanr za cijeli album u jednoj operaciji. Ovo je najbrži način čišćenja velike, neorganizirane biblioteke.

## Uređivanje oznaka za Spotify, Apple Music i streaming platforme

Često postavljano pitanje: «uredio sam svoje oznake u Evertagu, učitao datoteke i streaming usluga prikazuje krive metapodatke. O čemu se radi?»

Kratak odgovor: **streaming usluge ne poštuju uvijek vaše lokalne oznake.** Apple Music i Spotify imaju vlastite interne baze podataka — kad prepoznaju pjesmu, prepisuju prikazane metapodatke svojima. No za **prenesene datoteke**, vaše lokalne datoteke (značajka «Library» Apple Musica, Spotify Local Files) i **prijenose distributera na streaming platforme**, vaše oznake apsolutno su važne. Evo kako postaviti Evertag za svaki scenarij:

### Priprema datoteka za Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music ispravno rukuje UTF-8.
- **Omot albuma: Veliki** — Appleove aplikacije dobro prikazuju velike omote; Izvorni je previše.
- **Dupliciranje oznaka: OFF** — nije potrebno.
- Provjerite je li **Album Artist** ispravno popunjen — Apple Music ga koristi za grupiranje.

### Priprema datoteka za Spotify Local Files

Spotify Local Files prikazuje samo dobro označene datoteke. Oznake koje Spotify čita su ograničene.

- **ID3v2.4: ON** u većini slučajeva. Ako se pjesma ne prikazuje ispravno u Spotifyju nakon uređivanja, **pokušajte spremiti s ID3v2.4: OFF** (tj. kao ID3v2.3) — Spotifyjev parser je povijesno bio konzervativan prema v2.4.
- **Omot albuma: Srednji ili Veliki** — Spotify ga svejedno smanjuje.
- Popunite najmanje **Naslov**, **Izvođač**, **Album** i **Broj pjesme**.

### Priprema datoteka za prijenos preko distributera (DistroKid, TuneCore, CD Baby itd.)

Ako ste izvođač koji svoja djela prenosi na streaming platforme, distributer obično čita oznake, ali traži i metapodatke u svom sučelju. Bilo kako bilo:

- **ID3v2.3** je često sigurnija zadana opcija — mnogi cjevovodi distributera napravljeni su prije godina i preferiraju stariji format.
- Ugradite **Veliki** omot (većina distributera traži omote ≥ 1.400 × 1.400 px — provjerite njihove smjernice).
- Ne oslanjajte se na proširene oznake — distributeri čitaju samo glavna polja.

### Priprema datoteka za Plex, Jellyfin, Navidrome, Subsonic, Emby

Ovi samohostirani medijski poslužitelji su vrlo tolerantni. Čitaju i v2.3 i v2.4 čisto i dobro rukuju UTF-8.

- **ID3v2.4: ON** je u redu.
- **Omot albuma: Veliki** ili **Vrlo veliki** — ovi poslužitelji poslužuju omote mobilnim klijentima i CarPlay zaslonima, pa kvaliteta važi.
- **Album Artist** se snažno preporučuje — to je ono što Plex/Jellyfin koriste za ispravno grupiranje albuma po izvođaču.

### Priprema datoteka za autoradije i stariji hardver

- **ID3v2.4: OFF** (koristite ID3v2.3) — starije glavne jedinice često ne podržavaju v2.4.
- **Omot albuma: Srednji** — mnogi automobilski zasloni zapinju na velikim ugrađenim omotima.
- **Dupliciranje oznaka: ON** — stariji autoradiji ponekad čitaju samo ID3v1 fallback.

## Ostala poboljšanja

### Dizajn Liquid Glass

Sučelje Evertaga 4.2 prilagođeno je novom Appleovom materijalu **Liquid Glass** u cijeloj aplikaciji — prozirne površine, glađe animacije i ugođene kontrole koje se prirodno uklapaju u iOS, iPadOS i macOS.

### Ažurirane biblioteke veza

Osvježili smo interne biblioteke kojima Evertag komunicira s **WebDAV-om**, **SMB-om**, **DLNA-om**, **Dropboxom**, **Google Driveom**, **OneDriveom** i drugim uslugama. Rezultat: manje neuspjelih spajanja u rubnim slučajevima, bolja podrška za novije verzije poslužitelja i veća pouzdanost prilikom uređivanja oznaka na udaljenim datotekama.

### Ispravci prijevoda i lokalizacije

Više ispravaka jezika u sučelju na temelju izravnih povratnih informacija korisnika. Bolje uklapanje teksta na manjim gumbima u nekoliko jezika.

### Manja poboljšanja inspirirana vašim povratnim informacijama

Mnogo manjih poboljšanja na temelju recenzija na App Storeu i e-poruka na support@everappz.com. Čitamo svaku poruku.

## Preuzmite Evertag 4.2

[**Preuzmite Evertag s App Storea**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) ili ažurirajte putem App Storea. Evertag je besplatno preuzimanje uz neobavezne nadogradnje unutar aplikacije za napredne značajke. Nove veze s oblakom, mrežni protokoli, poboljšanja Wi-Fi Drivea i Liquid Glass UI dio su osnovnog ažuriranja.

Ako uživate u aplikaciji, ostavite recenziju na App Storeu — to stvarno pomaže. Imate povratne informacije ili ste naišli na problem? Pošaljite nam mail na **support@everappz.com**. Čitamo svaku poruku.

## Često postavljana pitanja

{{% details title="Što je novo u Evertagu 4.2?" closed="true" %}}
Evertag 4.2 dodaje više od 6 novih veza s oblakom i poslužiteljima (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), osvježeni Wi-Fi Drive s višestrukim odabirom i pametnijim redom prijenosa, ažuriranja Liquid Glass UI-a, ažurirane biblioteke veza, ključne ispravke pogrešaka u uređivanju oznaka i poboljšanja prijevoda.
{{% /details %}}

{{% details title="Trebam li koristiti ID3v2.4 ili ID3v2.3 u Evertagu?" closed="true" %}}
Koristite **ID3v2.4** za moderne uređaje (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, moderne Android aplikacije) i za biblioteke s nelatiničnim znakovima — UTF-8 podrška znači čišće oznake na kineskom, korejskom, japanskom, ruskom, arapskom i hebrejskom. Koristite **ID3v2.3** ako se vaše oznake netočno prikazuju u nekim aplikacijama, ako ciljate na starije autoradije ili ako cjevovod streaming distributera odbija v2.4. Uvijek možete prebaciti i ponovno spremiti.
{{% /details %}}

{{% details title="Zašto su moje oznake netočne u Spotifyju nakon uređivanja?" closed="true" %}}
Spotify uglavnom prikazuje metapodatke iz vlastitog kataloga — vaše lokalne oznake koriste se samo za «Local Files» ili sadržaj koji ste prenijeli kao izvođač. Ako označavate datoteke za Spotify Local Files i ne prikazuju se ispravno, pokušajte onemogućiti ID3v2.4 u Evertagu i spremiti kao ID3v2.3 — Spotifyjev parser je povijesno bio konzervativan prema v2.4.
{{% /details %}}

{{% details title="Koju veličinu omota albuma trebam odabrati u Evertagu?" closed="true" %}}
Za većinu korisnika: **Veliki**. Izgleda sjajno na telefonima, iPadima, Macovima i modernim automobilskim zaslonima bez previše napuhivanja datoteka. Koristite **Srednji** ako imate ogromnu biblioteku i želite uštedjeti disk. Koristite **Izvorni** (bez skaliranja) samo za arhivske mastere ili kad stvarno trebate maksimalnu kvalitetu — ali svjesni budite da neki stariji uređaji imaju problema s vrlo velikim ugrađenim omotima. **Izvorni** je dio premium personalizacijske nadogradnje Evertaga.
{{% /details %}}

{{% details title="Hoće li veći omoti albuma povećati moje datoteke?" closed="true" %}}
Da. Ugrađivanje omota 3.000 × 3.000 px može dodati nekoliko megabajta jednoj audio datoteci. U biblioteci od 1.000 pjesama to se penje u gigabajte. Ako je prostor pohrane oskudan, koristite Srednji ili Veliki; ako streamate s NAS-a gdje veličina nije bitna, Vrlo veliki ili Izvorni su u redu.
{{% /details %}}

{{% details title="Što su Duplicirane oznake i trebam li ih uključiti?" closed="true" %}}
Duplicirane oznake pišu osnovne metapodatke u oba dijela ID3v1 (legacy 128 bajtova) i ID3v2 (moderni) datoteke. Uključite ih samo ako ciljate na vrlo stare uređaje ili hardver koji čita ID3v1. Za sve moderno (pametne telefone, računala, novije autoradije), ostavite isključeno.
{{% /details %}}

{{% details title="Uređuje li Evertag oznake izravno na datotekama u oblaku?" closed="true" %}}
Da. Povežite se sa svojim oblakom (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3 itd.) ili putem FTP/SFTP/NFS, otvorite datoteku i uredite oznake kao da je lokalna. Evertag preuzima datoteku, primjenjuje vaše izmjene i prenosi ažuriranu verziju natrag. U postavkama možete odabrati između načina «Uvijek pitaj», «Auto-prijenos» ili «Ne prenosi».
{{% /details %}}

{{% details title="Mogu li uređivati FLAC oznake na iPhoneu s Evertagom?" closed="true" %}}
Da. Evertag podržava FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE i druge važne formate s punom podrškom za čitanje/pisanje oznaka, uključujući ugrađeni omot.
{{% /details %}}

{{% details title="Kako sigurno uređujem oznake na svom kućnom poslužitelju s SFTP-om?" closed="true" %}}
Otvorite Evertag, idite na Veze, odaberite SFTP i unesite naziv hosta ili IP poslužitelja, port (obično 22), korisničko ime i lozinku ili privatni SSH ključ. Evertag će pregledavati vaše udaljene mape i uređivati oznake izravno s end-to-end enkripcijom preko SSH-a.
{{% /details %}}

{{% details title="Mogu li uređivati oznake na više datoteka istovremeno?" closed="true" %}}
Da. Aktivirajte **Uređivanje datoteka istovremeno** u postavkama. Odaberite više datoteka, otvorite uređivač oznaka, i bilo koje polje koje promijenite primijenit će se na sve odabrane datoteke. Ovo je najbrži način postavljanja istog album artist, godine ili žanra za cijeli album.
{{% /details %}}

{{% details title="Je li ažuriranje na Evertag 4.2 besplatno?" closed="true" %}}
Da. Evertag je besplatno preuzimanje s App Storea, a 4.2 je besplatno ažuriranje za sve postojeće korisnike. Nove integracije s oblakom, poboljšanja Wi-Fi Drivea i Liquid Glass UI dio su osnovnog ažuriranja.
{{% /details %}}

{{% details title="Na kojim uređajima je dostupan Evertag 4.2?" closed="true" %}}
Evertag 4.2 radi na iPhoneu, iPadu i Macu. Sinkronizacija putem iCloud Drivea održava postavke uređivača oznaka dosljednim između uređaja.
{{% /details %}}
