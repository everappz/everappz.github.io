---
title: "Postavke"
date: 2020-02-01
lastmod: 2026-06-01
description: "Istražite svaku postavku u Evervideo — Media Player (Picture-in-Picture, hardversko H.264/HEVC dekodiranje, video ekvalizator, skaliranje, rotacija, VR pregled), Audio (ekvalizator, frekvencija uzorkovanja, kanali, IO međuspremnik, mješoviti način), Titlovi (primarni/sekundarni, font, vanjska datoteka, libass), Medijska biblioteka, Upravitelj datoteka, Wi-Fi Drive, Widgeti, Personalizacija, Jezik, Kod za pristup, Sigurnosna kopija i vraćanje — za iPhone, iPad i Mac."
keywords: [
  "postavke Evervideo", "konfiguracija video playera", "Premium nadogradnja Evervideo",
  "postavke Picture-in-Picture", "postavke video ekvalizatora",
  "način skaliranja videa", "rotacija videa", "hardverski dekoder iPhone",
  "postavke titlova", "sekundarni titl iOS", "postavke libass",
  "vanjska datoteka titla", "font titla",
  "postavke audio ekvalizatora", "frekvencija uzorkovanja audio izlaza",
  "kanali audio izlaza", "trajanje IO međuspremnika", "mješoviti način audio",
  "Wi-Fi Drive video", "widgeti Evervideo",
  "sigurnosna kopija vraćanje Evervideo", "kod za pristup Evervideo",
  "jezik Evervideo", "personalizacija Evervideo"
]
tags: ["guide", "evervideo", "settings"]
readingTime: 16
---


Zaslon **Postavke** je kontrolni centar Evervideo. Odavde možete nadograditi na Premium, konfigurirati video i audio motore (sistemske kodeke ili FFmpeg), upravljati Picture-in-Picture, postaviti titlove (primarni, sekundarni, libass, vanjske datoteke, fontovi), organizirati medijsku biblioteku, postaviti upravitelja datoteka, omogućiti widgete početnog zaslona, napraviti sigurnosnu kopiju podataka i pristupiti pomoći i pravnim informacijama. Odjeljci su grupirani pod naslovima: Kupnje i ažuriranja, Postavke aplikacije, Pomoć, Pravne napomene i privatnost.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Glavni zaslon postavki" image="/docs/guide/evervideo/img/evervideo-settings.webp" >}}
{{< /cards >}}

## Nadogradnja na Premium

Nadogradite aplikaciju na Premium verziju kako biste uklonili sva ograničenja. Besplatna verzija aplikacije nudi jednokratnu doživotnu kupnju unutar aplikacije i dvije opcije pretplate (1 mjesec i 1 godina) za uklanjanje svih ograničenja i nadogradnju na Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Nadogradnja na Premium" image="/docs/guide/evervideo/img/evervideo-upgrade-to-premium.webp" >}}
{{< /cards >}}

**Family Sharing** je omogućen za sve kupnje i planove, tako da možete podijeliti Premium verziju s do pet članova obitelji bez dodatnih troškova.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Odabir Premium plana" image="/docs/guide/evervideo/img/evervideo-select-premium-plan.webp" >}}
{{< /cards >}}

## Dijeljenje kupnji između iOS-a i Maca

Doživotne kupnje i pretplate dijele se između iOS-a i Maca putem **iCloud** za sinkronizaciju ovih informacija. Ako imate Premium na iOS uređaju, provjerite imate li instaliranu najnoviju verziju i da je iCloud omogućen. Pokrenite aplikaciju na iOS-u i pričekajte minutu da se informacije o kupnji prenesu na iCloud, zatim pokrenite Mac verziju — Premium bi se trebao aktivirati automatski.

Možete i dodirnuti gumb **Vrati kupnje** u postavkama aplikacije. Osigurajte da imate internetsku vezu i da ste prijavljeni na isti iCloud i App Store račun na oba uređaja.

## Vraćanje kupnji na novom uređaju

Za vraćanje kupnje na novom uređaju koristite izbornik **Kupnje → Vrati kupnje**. Vidjet ćete popis svojih kupnji. Ako ne vidite sve, provjerite je li uređaj povezan s istim Apple ID-jem koji je korišten za kupnju i je li iCloud omogućen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Izbornik kupnji u postavkama" image="/docs/guide/evervideo/img/evervideo-purhases-menu-in-settings.webp" >}}
{{< /cards >}}

## Isprobajte Premium besplatno

Možete nadograditi na Premium verziju besplatno, na ograničeno vrijeme, koristeći ovaj izbornik. Samo pogledajte oglas ili recite prijateljima o aplikaciji.

## Ažuriranje softvera

Dodirnite **Ažuriranje softvera** kako biste provjerili je li novija verzija Evervideo dostupna u App Storeu.

## Što je novo

Ovaj izbornik dostupan je nakon objave nove verzije. Prikazuje sažetak promjena i novih značajki u najnovijem ažuriranju.

## Player

Sve što se odnosi na reprodukciju nalazi se ovdje — audio, video, titlovi, uređaji, personalizacija, predmemorija i tajmer za spavanje.

### Općenito

Ove postavke pokrivaju temeljne aspekte playera.

- **Način ponavljanja** — odaberite kako se player ponaša kada video završi:
  - **Ponovi sve** — ponovo reproducira svaki video u redu čekanja.
  - **Ponovi jedan** — ponavlja samo trenutni video.
  - **Zaustavi ponavljanje** — pauzira kada trenutni video završi.
  - **Bez ponavljanja** — reproducira red čekanja jednom bez ponavljanja.
- **Način miješanja** — randomizira redoslijed videa u redu čekanja (**Uključeno** ili **Isključeno**).
- **Spremi poziciju reprodukcije** — sprema i vraća poziciju reprodukcije za videa u biblioteci.
- **Spremi stanje playera** — čuva stanje playera prije zatvaranja aplikacije kako biste mogli nastaviti od mjesta gdje ste stali.

### Video

Konfigurirajte kako Evervideo dekodira i prikazuje video.

- **Hardversko dekodiranje H.264** — uključi/isključi hardverski ubrzano AVC dekodiranje. Koristite kada su važni performanse baterije i temperatura; isključite za kompatibilnost s egzotičnim profilima.
- **Hardversko dekodiranje H.265 (HEVC)** — isto za HEVC. Moderni iPhoneovi, iPadovi i Macovi učinkovito dekodiraju HEVC.
- **Preferirani format piksela** — odaberite format piksela koji player prezentira rendereru (zadane vrijednosti su podešene za uređaj).
- **Preferirani FPS** — postavite ciljni FPS reprodukcije. Korisno za usklađivanje s određenom stopom osvježavanja monitora.
- **Način skaliranja videa** — Prilagodi / Ispuni / Rastegni / Originalno. Određuje kako slika ispunjava područje prikaza.
- **Način prikaza videa** (iOS / iPadOS) — kako se video prikazuje u prikazu playera.
- **Rotacija videa** — ručno rotirajte sliku za 0° / 90° / 180° / 270° (korisno za videa snimljena u pogrešnoj orijentaciji).
- **Video ekvalizator** — podešavajte svjetlinu, kontrast, zasićenost i nijansu s pregledom u stvarnom vremenu. Prilagođene unaprijed postavke mogu se **izvesti i uvesti**.
- **VR pregled** (iOS / iPadOS) — za 360° sferične videa. Povucite za gledanje okolo, pritisnite za zumiranje.
- **Picture-in-Picture (PiP)** (iOS / iPadOS) — omogući PiP podršku; aplikacija će se prebaciti na plutajući prozor playera kada stavite aplikaciju u pozadinu ili dodirnete gumb PiP.

### Audio

Konfigurirajte audio reprodukciju i izlaz.

- **Audio zapis** — odaberite audio stream kada video ima više (komentar, sinkronizacija, itd.).
- **Audio ekvalizator** — 10-pojasni EQ s unaprijed postavkama i pojačalom. Prilagođene unaprijed postavke mogu se izvesti / uvesti.
- **Frekvencija uzorkovanja audio izlaza** — 44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz, 96 kHz. Korisno s vanjskim DAC-ovima.
- **Broj kanala audio izlaza** — Mono, Stereo, 5.1, ITU BS.775-1, SDDS i više.
- **Preferirano trajanje IO međuspremnika audio izlaza** — tipična vrijednost za reprodukciju visoke razlučivosti s niskim kašnjenjem je oko 5 ms (0,005 s). Podešavajte za svoj hardver.
- **Način audio izlaza** (samo iOS) — mješoviti način omogućuje miješanje Evervideo zvuka s drugim aplikacijama.

### Titlovi

Evervideo uključuje sveobuhvatnu podršku za titlove.

- **Zapis titla** — odaberite iz ugrađenih zapisa titlova u datoteci.
- **Vanjska datoteka titla** — učitajte vanjsku `.srt`, `.vtt`, `.ass` ili `.ssa` datoteku s vašeg uređaja ili bilo koje povezane usluge u oblaku.
- **Font** — odaberite font za primarni zapis titla.

### Uređaji (samo iOS/iPadOS)

Odaberite **AirPlay** ili **Google Chromecast** uređaj za video izlaz.

### Personalizacija

- **Stil izgleda playera** — Minimalan (zadano za Evervideo), Dno, Antički, Klasični i više.
- **Radnje glavnog zaslona** — odaberite koje se gumbe prikazuju na glavnom zaslonu playera.
- **Upravljanje zaslona zaključavanja** — Preskoči vrijeme, Dodaj oznaku, Dodaj u omiljene.
- **Intervali preskakanja** — odaberite vremenski interval za gumbe preskakanja (5 s, 10 s, 15 s, 30 s, itd.).
- **Stil pomicanja omota albuma** — preferirani stil pomicanja za naslovne slike.
- **Dodatni elementi** — Informacije o audio formatu, Klizač glasnoće.

### Učitavanje datoteka

Konfigurirajte kako se video podaci prenose s mreže.

- **Vrsta mreže** — samo Wi-Fi ili Wi-Fi + mobilna mreža.
- **Vrijeme predučitavanja** — duljina međuspremnika za glatkiju reprodukciju na sporim mrežama.
- **Koristi direktni URL** — kada je podržano, koristi direktni URL za brže učitavanje.

### Predmemorija reprodukcije

Videa u redu čekanja playera automatski se preuzimaju radi osiguravanja glatke reprodukcije. Ovdje možete onemogućiti ovu opciju ili konfigurirati veličinu predmemorije.

### Tajmer za spavanje

Aktivirajte tajmer za automatsko zaustavljanje reprodukcije nakon određenog vremena. Dodirnite ikonu konfiguracije za **precizni način** s granularnošću po minuti.

## Medijska biblioteka

Upravljajte automatskom sinkronizacijom, metapodacima, omotima albuma, popisima pjesama, nedavnim i omiljenima.

### Čitanje metapodataka

Kada dodajete videa u biblioteku, čitač metapodataka ih skenira u pozadini i organizira po Albumu i Žanru. Možete podesiti brzinu skeniranja, onemogućiti čitač ili pokrenuti potpuno ponovsko skeniranje s **Ponovno učitati metapodatke**. **Normalizacija kodiranja metapodataka** automatski popravlja pokvarena kodiranja znakova (uobičajeno s datotekama s Windows računala).

### Online sinkronizacija

Automatski dodajte videa s povezanih usluga u oblaku i medijskih poslužitelja u svoju biblioteku. Odaberite koje mape skenirati, konfigurirajte koliko često aplikacija treba sinkronizirati i ručno pokrenite/zaustavite sinkronizaciju. Online sinkronizacija se izvodi samo dok je aplikacija aktivna — za velike biblioteke koristite verziju za stolno računalo i zatim prenesite sinkroniziranu biblioteku s **Sigurnosna kopija i vraćanje**.

### Offline sinkronizacija

Kada označite mapu u oblaku kao dostupnu offline, pojavljuje se u **Datoteke → Offline mape** i automatski se preuzima. Nove datoteke dodane online također se preuzimaju. Konfigurirajte vremenski interval i pokrenite ručne sinkronizacije s ovog zaslona.

### Personalizacija

- **Stil zaslona medijske biblioteke** — Običan izbornik, Grupirani izbornik, Izbornik s karticama.
- Prebacite prikaz velikih omota albuma na zaslonima s detaljima.

### Omoti albuma

- **Vrsta mreže** — Wi-Fi ili Wi-Fi + mobilna mreža.
- **Učitaj omote albuma za online datoteke** — izvuci ugrađene ilustracije iz datoteka u oblaku (koristi dodatne podatke).
- **Traži u mapi** — koristi JPEG / PNG slike u istoj mapi kada video nema ugrađeni omot.
- **Kvaliteta omota** — podesite razlučivost na kojoj se omoti pohranjuju u predmemoriju.
- **Prikaži u mapi** / **Izbriši sve** — upravljajte predmemorijom ilustracija.

### Popisi pjesama

Omogući dodavanje istog videa dva puta u popis pjesama (isključeno prema zadanim postavkama).

### Nedavne

Upravljajte popisom nedavno reproduciranih videa — promijenite veličinu, izbrišite ili izvezite kao M3U / CSV / TXT.

### Omiljeni

- **Istovremeno uređivanje** — zrcaljenje omiljenih između medijske biblioteke i odjeljka datoteka.
- **Izbriši popis** — obrišite popis omiljenih.
- **Izvezi popis pjesama** — izvezite omiljene kao M3U / CSV / TXT.

### Izbriši medijsku biblioteku

Obrišite bazu podataka medijske biblioteke. Vaše video i audio datoteke na pohrani ostaju netaknute.

## Kod za pristup

Zaštitite Evervideo s **4-znamenkastim numeričkim kodom za pristup**. Kada je omogućen, od vas će se tražiti unos koda za pristup svaki put kada se aplikacija pokrene. Kombinirajte ga s iOS Face ID / Touch ID na uređaju za dodatnu zaštitu.

## Upravitelj datoteka

Kontrolira kako se datoteke prenose, pohranjuju i pregledavaju.

- **Prijenosi datoteka** — mrežna preferencija (samo Wi-Fi ili Wi-Fi + mobilna mreža).
- **Maksimalni broj paralelnih zadataka** — postavite broj paralelnih niti za preuzimanje.
- **Zadaci prijenosa datoteka** — pogledajte trenutno aktivna prijenosa i preuzimanja.
- **Prijenosi u pozadini** — dopustite preuzimanja dok je aplikacija u pozadini.
- **Spremi preuzete datoteke u** — zadani direktorij za preuzimanja.
- **Sinkronizirani offline mape** — upravljajte mapama u offline načinu rada.
- **Vremenski interval** — koliko često se offline mape provjeravaju na promjene.
- **Prikaži puna imena datoteka** — prikazuje ekstenzije u upravitelju datoteka.
- **Uredi online datoteke** — onemogući za prebacivanje na način samo za čitanje za povezane usluge u oblaku.
- **Kopiraj datoteke pri otvaranju** — kako postupati s uvezenim datotekama iz drugih aplikacija.
- **Minijature za datoteke** — upravljajte generiranim minijaturama datoteka.
- **Izbriši privremene datoteke** — očistite mapu predmemorije aplikacije.

## Wi-Fi Drive

Aktivirajte Wi-Fi Drive za prijenos datoteka s računala na uređaj pomoću stolnog web preglednika, Findera ili File Explorera. Detaljne upute dostupne su [ovdje](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Widgeti

Omogućite widgete kako bi aplikacija ažurirala podatke widgeta tijekom reprodukcije. Ažuriranja widgeta zahtijevaju dodatnu energiju, stoga je prekidač prema zadanim postavkama isključen — omogućite ga samo ako stvarno koristite widgete na početnom zaslonu ili zaslonu zaključavanja.

Widgete Evervideo možete dodati dugim pritiskom na početni zaslon ili zaslon zaključavanja, dodirivanjem **+**, traženjem **Evervideo** i odabirom veličine widgeta. Widgeti prikazuju video koji se trenutno reproducira i otvaraju se izravno na player punog zaslona. Widgeti također rade na macOS-u u Centru za obavijesti.

## Personalizacija

Prilagodite korisničko sučelje prema vašim preferencijama.

- **Ikona aplikacije** — alternativna ikona početnog zaslona (Premium).
- **Shema boja** — Tamna, Svijetla ili Zadana (prati izgled sustava).
- **Stil pozadine** — Zamućeni omot albuma ili jednobojno.
- **Izgled stavki na popisu** — automatsko podešavanje visine retka; prikaz manjih minijatura.
- **Ograničenje učitavanja sadržaja** — uključi/isključi stranično prikazivanje.
- **Stil zaslona datoteka** — Običan izbornik ili Grupirani izbornik.
- **Stil zaslona medijske biblioteke** — Običan / Grupirani / Izbornik s karticama.
- **Stil zaslona playera** — Minimalan / Dno / Antički / Klasični.
- **Stil kontekstnog izbornika** — sistemski izbornik ili stil donjeg lista.

## Prozor

Dostupno na Macu i Catalyst. Konfigurirajte preference vezane uz prozor kao što su zadana veličina i ponašanje pri pokretanju.

## Zaslon

Odaberite treba li zaslon ostati aktivan dok koristite aplikaciju.

## Pristupačnost

Aktivirajte **Tekstualni način** za skrivanje slika u korisničkom sučelju. Tekstualni način automatski se aktivira kada je VoiceOver aktivan.

## Jezik

Promijenite jezik aplikacije i nadjačajte zadane postavke sustava. Promjena se primjenjuje nakon potpunog zatvaranja i ponovnog otvaranja Evervideo. Podržano je više od 120 jezika.

## Sigurnosna kopija i vraćanje

Napravite sigurnosnu kopiju svih podataka aplikacije ili ih migrirajte na drugi uređaj. Odaberite što uključiti:

- **Baza podataka** — vaši unosi medijske biblioteke, popisi pjesama, ocjene, omiljeni, povijest gledanja. Offline datoteke nisu uključene kako bi veličina datoteke ostala upravljivom.
- **Omoti albuma** — vaše predmemorirane ilustracije.
- **Postavke** — vaše postavke aplikacije.

Dodirnite **Napravi sigurnosnu kopiju podataka aplikacije** za pokretanje sigurnosnog kopiranja. Za vraćanje na novom uređaju premjestite datoteku sigurnosne kopije putem iCloud Drivea, AirDropa ili bilo koje povezane usluge u oblaku i otvorite je na novom uređaju.

## Pomoć

Pristupite vodiču aplikacije za pomoć i smjernice o učinkovitom korištenju aplikacije.

## Česta pitanja

Pronađite odgovore na uobičajena pitanja u odjeljku FAQ.

## Pošalji povratne informacije

Pošaljite povratne informacije našem timu za podršku izravno iz aplikacije, s automatski priloženim dijagnostičkim informacijama.

## Podijeli ovu aplikaciju

Podijelite Evervideo s prijateljima kako biste širili vijest.

## Otkrij više aplikacija

Istražite druge aplikacije od Everappza.

## Uvjeti i odredbe

Pročitajte uvjete i odredbe prije korištenja aplikacije.

## Pravila privatnosti

Pročitajte pravila privatnosti kako biste razumjeli naše prakse rukovanja podacima.

## Analitika i prikupljanje podataka

Provjerite koje su usluge omogućene za analitiku i prikupljanje podataka i deaktivirajte one koje ne želite.

## Pravne napomene

Informacije o svakoj biblioteci korištenoj u aplikaciji zajedno s brojem verzije aplikacije i informacijama o izgradnji.
