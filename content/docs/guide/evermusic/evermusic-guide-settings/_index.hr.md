---
title: "Postavke"
date: 2020-01-01
description: "Istražite sve postavke u Evermusicu uključujući konfiguraciju zvuka, sinkronizaciju glazbene biblioteke, offline mape, metapodatke, personalizaciju, pristupačnost, widgete, CarPlay i opcije sigurnosnog kopiranja."
keywords: [
  "Evermusic", "settings", "audio settings", "music library sync",
  "offline folders", "equalizer", "crossfade", "gapless playback",
  "audio processor", "playlist settings", "premium upgrade",
  "restore purchases", "file manager", "tags editor", "WiFi drive",
  "voiceover", "app backup", "accessibility", "localization",
  "widgets", "CarPlay", "spatial audio", "audio pitch"
]
tags: ["evermusic", "guide", "settings"]
readingTime: 16
---


Zaslon Postavki je upravljački centar Evermusicа. Odavde možete nadograditi na Premium, konfigurirati audio reproduktor, upravljati glazbenom bibliotekom, postaviti upravitelja datoteka, prilagoditi sučelje, omogućiti widgete i CarPlay, sigurnosno kopirati podatke i pristupiti pomoći i pravnim informacijama. Odjeljci su grupirani pod zaglavljima: **Kupnje i ažuriranja**, preferencije aplikacije, **Pomoć** i **Pravo i privatnost**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Zaslon postavki Evermusicа" image="/docs/guide/evermusic/evermusic-guide-settings/img/settings-main-screen.webp" >}}
{{< /cards >}}

## Kupnje i ažuriranja

### Nadogradi na Premium

Nadogradite aplikaciju na Premium verziju za uklanjanje svih ograničenja. Besplatna verzija nudi jednu doživotnu kupnju unutar aplikacije i dvije opcije pretplate koje otključavaju puni set značajki.

Obiteljsko dijeljenje je omogućeno za sve kupnje i planove, tako da možete dijeliti Premium verziju s članovima obitelji.

Više o kupnjama i Premium verziji možete pročitati ovdje: [Koja je razlika između Evermusicа i Evermusic Premiuma](/docs/faq/evermusic/what-is-the-difference-between-evermusic-and-evermusic-premium/).

#### Evermusic Free (Plava ikona) nasuprot Evermusic Pro (Crvena ikona)

Evermusic je objavljen na App Storeu pod dvije različite ikone / boje:

- **Evermusic Free (plava ikona)** podijeljen je u **dvije zasebne App Store aplikacije s različitim bundle ID-jevima** — jedna za **iOS / iPadOS** i jedna namjenska za **macOS** (Univerzalni binarni koji radi na **Apple Siliconу i Intel Macovima**). Premium kupnje unutar aplikacije **dijele se između iOS i Mac plavih aplikacija putem iClouda** — kupite Premium na iPhoneu i automatski se aktivira na Macu (i obrnuto), sve dok oba uređaja koriste isti Apple ID s omogućenim iCloudom.
- **Evermusic Pro (crvena ikona)** je **jedna App Store aplikacija** s **jednim bundle ID-jem** koja radi na **iPhoneu, iPadu i Apple Silicon Macovima (M1 i noviji)**. Ima **iste funkcionalnosti kao Evermusic Free s aktiviranim Premium planom**. Crvena aplikacija **ne podržava Intel Macove**, zbog čega je njezina cijena nešto niža od ekvivalentne Premium kupnje u plavoj aplikaciji. Evermusic Pro također **uopće ne prikuplja dijagnostiku ili analitiku korisnika** — analitika je potpuno onemogućena u izgradnji, bez opcije uključivanja.

Budući da se bundle ID-jevi razlikuju između plave i crvene, Premium kupnja aktivirana u plavoj aplikaciji ne otključava crvenu aplikaciju besplatno, i obrnuto. Ako već koristite plavu aplikaciju s aktiviranim Premiumom, nema potrebe instalirati crvenu aplikaciju — već imate sve što Pro nudi.

### Dijeljenje kupnji između iOS-a i Maca

Doživotne kupnje i pretplate dijele se između iOS-a i Maca koristeći iCloud. Ako već posjedujete Premium na iOS-u, provjerite imate li instaliranu najnoviju verziju i je li iCloud omogućen. Pokrenite aplikaciju na iOS-u i pričekajte minutu da se podaci o kupnji uploadaju na iCloud.

U postavkama aplikacije možete i dodirnuti **Obnovi kupnje**. Potom instalirajte najnoviju verziju aplikacije s App Storea na Macu i pokrenite aplikaciju. Provjerite imate li internetsku vezu i jeste li prijavljeni s istim iCloud i App Store računom na oba uređaja. Pričekajte minutu da aplikacija preuzme podatke o kupnji s iClouda. Premium verzija trebala bi se automatski aktivirati na Macu.

### Obnova kupnji na novom uređaju

Za obnovu kupnje na novom uređaju, koristite **Kupnje → Obnovi kupnje**. Vidjet ćete popis kupnji. Ako nešto nedostaje, provjerite je li uređaj spojen na isti iTunes račun koji je korišten za obavljanje kupnji i je li iCloud omogućen.

### Isprobajte Premium besplatno

Putem ovog izbornika možete nadograditi na Premium verziju besplatno na ograničeno vrijeme. Pogledajte kratki oglas ili podijelite aplikaciju s prijateljima za privremeno otključavanje Premiuma.

### Kupnje

Obnovite prethodne kupnje iz ovog izbornika. Ako naiđete na greške aktivacije, pokušajte omogućiti opciju **Obnovi kupnje pri pokretanju aplikacije**.

### Ažuriranje softvera

Dodirnite **Ažuriranje softvera** za provjeru je li dostupna novija verzija Evermusicа. Aplikacija će usporediti instaliranu verziju s najnovijom verzijom na App Storeu i obavijestiti vas preporučuje li se ažuriranje.

### Što je novo

Ovaj izbornik postaje dostupan nakon objavljivanja nove verzije. Prikazuje sažetak promjena i novih značajki uključenih u najnovije ažuriranje.

## Postavke audio reproduktora

Sve postavke audio reproduktora grupirane su ovdje: ekvilajzer, crossfade reprodukcija, predmemorija audio reproduktora, učitavanje pjesama i više. Postavke su organizirane u logičke pododjeljke.

### Općenito

Ovaj pododjeljak sadrži opće postavke reda reprodukcije, audio izlaza i spremanja stanja.

#### Način ponavljanja

Specificira ponašanje audio reproduktora kada završi reprodukcija pjesme:

- **Repeat All** – ponavlja sve pjesme u redu reproduktora.
- **Repeat One** – ponavlja samo trenutnu pjesmu.
- **Repeat Stop** – pauzira reprodukciju kada završi trenutna pjesma.
- **Repeat None** – pušta red da se reproducira bez ponavljanja.

#### Način miješanja

Reproducira pjesme nasumičnim redoslijedom. Ovo zapravo miješa red i reproducira pjesme jednu po jednu novim redoslijedom. Dostupne vrijednosti: **Shuffle off** i **Shuffle on**.

#### Audio procesor

Moguće vrijednosti: **AVFoundation** i **CoreAudio**. Prema zadanim postavkama, koristi se AVFoundation. Zbog poznatog problema s AVFoundation na iOS 17.0–17.6, crossfade reprodukcija i audio ekvilajzer ne mogu se koristiti istovremeno. Za uživanje u crossfadeu i ekvilajzeru na tim iOS verzijama, prebacite se na CoreAudio audio procesor.

Ako imate problema s gapless reprodukcijom koristeći AVFoundation, isprobajte i CoreAudio. Jedina ograničenja CoreAudio su internetsko strujanje nekih radio stanica i određeni audio formati, jer ne podržava svaki sistemski audio format (kao M4A i nekoliko ostalih).

#### Brzina uzorkovanja audio izlaza

Postavite brzinu uzorkovanja audio izlaza od 8 KHz do 384 KHz. Ova je opcija dostupna samo kada je odabran CoreAudio procesor.

#### Broj kanala audio izlaza

Postavite broj kanala audio izlaza — **MONO** ili **STEREO**. Ova je opcija dostupna samo kada je odabran CoreAudio procesor.

#### Algoritam visine tona

Odaberite algoritam koji se koristi za korekciju visine tona. Dostupne vrijednosti su **Time Domain**, **Spectral** i **Varispeed**. Korisno ako prilagođavate brzinu reprodukcije i želite kontrolirati rezultirajuću kvalitetu zvuka.

#### Prostorni zvuk

Prostorni zvuk koristi psihoakustičke metode za stvaranje iskusnog audio iskustva na podržanim slušalicama i rasporedima zvučnika. Moguće vrijednosti: **Deactivated**, **Mono and Stereo**, **Multichannel**, **Mono Stereo Multichannel**.

#### Način audio izlaza

Dostupno samo na iOS-u. Omogućuje vam aktiviranje miješanog načina rada kako bi se audio iz ove aplikacije miješao s drugim aplikacijama. Upute o korištenju miješanog načina možete pronaći [ovdje](/docs/howto/how-to-record-video-while-playing-music-on-iphone).

#### Spremi poziciju reprodukcije

Osigurava da aplikacija sprema i vraća poziciju reprodukcije za pjesme u glazbenoj biblioteci.

#### Spremi stanje audio reproduktora

Sprema stanje audio reproduktora prije zatvaranja aplikacije, čineći lakim nastavak od mjesta gdje ste stali.

Nakon što su obje ove značajke omogućene, otvorite bilo koju mapu, album, izvođača ili žanr. Vidjet ćete radnju **Nastavi reprodukciju** na vrhu zaslona, zajedno s posljednjom pohranjenom pjesmom i pozicijom reprodukcije. Dodirnite **Nastavi reprodukciju** za vraćanje. Za nastavak reprodukcije pojedinačne datoteke, jednostavno dodirnite tu datoteku.

### Personalizacija

Prilagodite izgled zaslona audio reproduktora, odaberite koje su kontrole vidljive na reproduktoru, zaključanom zaslonu i statusnoj traci i konfigurirajte gumbe za preskakivanje vremena.

#### Stil zaslona audio reproduktora

Konfigurirajte pozicioniranje alatnih traka i glavnih kontrola na audio reproduktoru.

#### Stil pomicanja omota albuma

Odaberite stil pomicanja za omote albuma na zaslonu audio reproduktora.

#### Dodatni elementi

Omogućite dodatne elemente na zaslonu audio reproduktora. **Informacije o audio formatu** prikazuje tehničke informacije trenutno reproducirajuće pjesme iznad artwork; **Klizač audio glasnoće** prikazuje klizač audio izlaza ispod kontrola reprodukcije.

#### Radnje glavnog zaslona

Konfigurirajte koji su gumbi vidljivi na glavnom zaslonu audio reproduktora. Dostupne opcije uključuju Repeat i Shuffle način, sljedeću i prethodnu pjesmu, Skip Time, Sleep Timer, Google Chromecast, AirPlay i Bluetooth, Audio Equalizer, Pretraži, Bookmarks, Speed, Add Bookmark, Add to Favorites, Comments i više.

#### Kontrole reprodukcije na zaključanom zaslonu

Odaberite koje su dodatne kontrole omogućene na zaključanom zaslonu. Moguće vrijednosti: **Skip Time**, **Add Bookmark** i **Add to Favorites**.

#### Intervali preskakivanja vremena

Odaberite vremenske intervale koje koriste gumbi za preskakivanje naprijed i natrag.

### Učitavanje datoteka

Odaberite vrstu mreže koja se koristi za strujanje pjesama. Dostupne opcije: **Wi-Fi** i **Wi-Fi i mobilni podaci**.

#### Vrijeme prethodnog učitavanja

Postavite vremenski interval međuspremnika. Povećajte ovu vrijednost ako imate lošu mrežnu vezu.

#### Koristi direktni URL

Kada je omogućeno, direktni URL se koristi za učitavanje pjesme ako ga poslužitelj podržava. To može ubrzati učitavanje pjesama, ali može neznatno utjecati na stabilnost reprodukcije.

#### Optimizacija učitavanja datoteka

Kada je omogućeno, sustav optimizira učitavanje pjesama za AVFoundation audio procesor, što može poboljšati stabilnost reprodukcije. Aplikacija koristi tehnologiju opisanu [ovdje](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/).

### Audio ekvilajzer

Konfigurirajte audio ekvilajzer. Više o postavkama i EQ konfiguracijama možete pročitati [ovdje](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Uređaji

Spojite se na AirPlay ili Google Chromecast uređaj (samo iOS).

### Brzina reprodukcije

Podesite brzinu reprodukcije audio reproduktora. Za preciznije upravljanje, omogućite precizni klizač dodirivanjem ikone konfiguracije u gornjem desnom kutu.

### Crossfade reprodukcija

Crossfade omogućuje besprijekoran tijek pjesama u kontinuiranoj mješavini — sljedeća pjesma počinje s reprodukcijom nekoliko sekundi prije nego trenutna završi. Crossfade nije dostupan za AirPlay i Google Chromecast. Na ovom zaslonu odaberite koliko dugo trenutna i sljedeća pjesma reproduciraju istovremeno. Ako imate problema s crossfadeom i audio ekvilajzerom istovremeno, prebacite audio procesor kao što je gore opisano.

### Gapless reprodukcija

Gapless reprodukcija osigurava da se pjesme reproduciraju bez ikakvih prekida ili tišine između njih. Savršena je za klasičnu glazbu, live snimke i konceptualne albume. Ako imate problema s gapless reprodukcijom, prebacite audio procesor kao što je gore opisano.

### Predmemorija reprodukcije

Pjesme u redu audio reproduktora automatski se preuzimaju za glatku reprodukciju. Ako ručno preuzimate audio datoteke, ovu opciju možete onemogućiti za izbjegavanje duplikata. Ovdje možete i konfigurirati veličinu predmemorije audio reproduktora. Pročitajte više o offline načinu i predmemoriji reprodukcije ovdje: [Reprodukcija offline glazbe u Evermusicu i Flacboxu: Preuzimanje i sinkronizacija iz oblaka u lokalne datoteke](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Tajmer za spavanje

Omogućite tajmer za zaustavljanje reprodukcije nakon određenog vremenskog ograničenja. Za preciznije upravljanje, omogućite precizni način dodirivanjem ikone konfiguracije u gornjem desnom kutu.

## Biblioteka

Postavke glazbene biblioteke — automatska sinkronizacija, čitanje metapodataka, učitavanje omota albuma, popisi pjesama, nedavne i omiljene — nalaze se ovdje.

### Čitanje metapodataka

Kada dodajete pjesme u biblioteku, čitač metapodataka ih obrađuje u pozadini i organizira prema Izvođaču, Albumu, Žanru i Skladatelju. Možete prilagoditi brzinu čitanja metapodataka za brže učitavanje podataka (na račun više baterije). Možete i potpuno onemogućiti čitač metapodataka i prikazivati nazive datoteka umjesto informacija iz oznaka.

Čitač metapodataka samo ažurira bazu podataka glazbene biblioteke; ne mijenja datoteke pohranjene u oblak računu ili lokalnoj pohrani. Ako trebate urediti metapodatke audio datoteka, koristite ugrađeni uređivač oznaka putem odgovarajuće radnje u izborniku opcija.

Kada je **Čitanje metapodataka u pozadini** uključeno, čitač nastavlja raditi u pozadinskom načinu. Ako aplikacija koristi previše energije tijekom reprodukcije, iOS je može suspendirati.

Ako imate veliku glazbenu kolekciju, preporučljivo je izvesti sinkronizaciju metapodataka na desktop verziji aplikacije. Zatim možete prenijeti sinkroniziranu glazbenu biblioteku na iOS koristeći značajku **Sigurnosno kopiranje i obnavljanje**.

Kada je **Normalizacija kodiranja metapodataka** omogućena, aplikacija automatski normalizira kodiranje metapodataka za sve pjesme. Ovo popravlja probleme gdje je kodiranje audio oznaka pokvareno (npr. nakon uređivanja datoteka na Windows PC-u) i sprječava pojavu netočnih znakova u informacijama o pjesmi.

**Ponovno učitavanje metapodataka** označava svaku datoteku u glazbenoj biblioteci kao datoteku s nedostajućim metapodacima, što uzrokuje da čitač metapodataka osvježi svaki zapis.

**Pokretanje čitanja metapodataka** ručno pokreće čitač metapodataka. Napredak je prikazan ispod radnje.

### Online sinkronizacija

Automatska online sinkronizacija glazbe dodaje pjesme iz spojenih oblak usluga u glazbenu biblioteku automatski. Za njeno omogućivanje, otvorite postavke glazbene biblioteke i odaberite mape za sinkronizaciju.

S ovom opcijom omogućenom, aplikacija skenira odabrane mape, identificira podržane audio datoteke i dodaje ih u biblioteku. Pokrenite ili zaustavite sinkronizaciju odgovarajućom radnjom izbornika.

Online sinkronizacija radi samo kada je aplikacija u prvom planu, pa sinkronizacija velike biblioteke može potrajati. Za ubrzavanje, držite aplikaciju otvorenom, spojite se na izvor napajanja i omogućite **Zaslon → Uvijek aktivno** u postavkama.

Alternativno, izvršite online sinkronizaciju na desktop verziji aplikacije i prenesite glazbenu biblioteku na iOS koristeći **Sigurnosno kopiranje i obnavljanje**.

Možete i odabrati koliko često se pokreće online sinkronizacija. Postavljanje intervala na **Odmah** pokreće sinkronizaciju svaki put kada otvorite aplikaciju.

### Offline sinkronizacija

Konfigurirajte offline sinkronizaciju glazbe.

#### Sinkronizirani offline mape

Kada označite online mapu na oblak poslužitelju kao dostupnu offline (koristeći izbornik Više radnji), pojavljuje se ovdje. Sadržaj mape preuzima se u **Lokalne datoteke → Offline mape**. Kada se online mapa promijeni (datoteke dodane, uklonjene ili ažurirane), aplikacija provjerava promjene i ažurira lokalnu kopiju na uređaju.

Na ovom zaslonu možete ručno pokrenuti sinkronizaciju offline mape, otkriti offline mapu u njenoj nadređenoj mapi i onemogućiti offline način rada za mapu. Onemogućavanje offline načina rada uklanja sve lokalne kopije datoteka s uređaja.

#### Vremenski interval

Odaberite koliko često aplikacija provjerava offline mape za izmjene.

#### Pokretanje skeniranja lokalnih mapa

Skenirajte sve lokalne mape u direktoriju Documents aplikacije za podržane audio datoteke. Pronađene datoteke automatski se dodaju u glazbenu biblioteku. Datoteke smještene na uređaju, ali izvan direktorija Documents aplikacije, moraju se ručno dodati u glazbenu biblioteku jer aplikacija im ne može pristupiti zbog iOS/macOS sigurnosnih ograničenja.

**Važno:** Preporučljivo je povremeno pokrenuti offline sinkronizaciju glazbe kako biste glazbenu biblioteku ažurirali lokalnim datotekama.

### Personalizacija

Konfigurirajte stil zaslona glazbene biblioteke. Dostupne su tri opcije: **Jednostavni izbornik**, **Grupirani izbornik** i **Izbornik s karticama**. Možete i omogućiti ili onemogućiti omote albuma na zaslonu detalja albuma.

### Omoti albuma

Odaberite kako aplikacija učitava i pohranjuje artwork albuma.

- **Vrsta mreže** — odaberite **Wi-Fi** ili **Wi-Fi i mobilni podaci** za preuzimanja omota.
- **Učitaj omote albuma za online datoteke** — kada je omogućeno, ugrađeni omoti albuma učitavaju se za datoteke pohranjene u pohrani u oblaku. To može koristiti dodatne mrežne podatke.
- **Pretraži u mapi** — kada je omogućeno, ako pjesma nema ugrađeni omot, aplikacija traži JPEG ili PNG slike u istoj mapi i koristi ih kao artwork albuma.
- **Kvaliteta omota** — odaberite kvalitetu omota albuma pohranjenih na uređaju.
- **Prikaži u mapi** — otvorite mapu gdje su predmemorirani omoti albuma kako biste ih mogli upravljati ili sigurnosno kopirati.
- **Izbriši sve** — obrišite predmemorirane omote albuma za oslobađanje pohrane i prisiljavate aplikaciju da ih ponovo učita na zahtjev.

### Popisi pjesama

Omogućite opciju dodavanja iste pjesme na popis dvaput. Prema zadanim postavkama, ova je opcija onemogućena.

### Nedavne

Upravljajte popisom nedavno reproduciranih pjesama.

- **Izbriši popis** — obrišite cijeli popis nedavno reproduciranih pjesama.
- **Promijeni veličinu popisa** — postavite broj stavki koje se pojavljuju na popisu.
- **Izvezi popis pjesama** — izvezite popis nedavno reproduciranih pjesama kao M3U, CSV ili TXT. Detaljne upute dostupne su [ovdje](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Omiljeni

Upravljajte popisom omiljenih pjesama.

- **Simultano uređivanje** — kada je omogućeno, dodavanjem pjesme u omiljene dodaje je i u glazbenoj biblioteci i u odjeljku datoteka istovremeno.
- **Izbriši popis** — obrišite cijeli popis omiljenih pjesama.
- **Izvezi popis pjesama** — kao Nedavne, izvezite omiljene kao M3U, CSV ili TXT.

### Brisanje glazbene biblioteke

Obrišite bazu podataka glazbene biblioteke. Glazbene datoteke u pohrani ostaju netaknute.

## Šifra

Aktivira zaslon zaštite lozinkom ako želite zaštititi podatke aplikacije.

## Upravitelj datoteka

Odjeljak Upravitelja datoteka kontrolira kako se datoteke prenose, pohranjuju i pregledavaju.

### Prijenosi datoteka

Odaberite preferenciju mreže za preuzimanje datoteka na uređaj.

### Maksimalni broj paralelnih zadataka

Postavite broj paralelnih niti preuzimanja. Veći broj ubrzava preuzimanja, ali zahtijeva više baterije.

### Zadaci prijenosa datoteka

Prikazuje trenutno aktivne zadatke uploada i preuzimanja.

### Pozadinski prijenosi

Dopustite preuzimanja dok je aplikacija u pozadini. Ako pozadinski prijenosi troše puno energije, iOS može suspendirati aplikaciju.

### Spremi preuzete datoteke u

Odaberite zadani direktorij preuzimanja ili neka aplikacija pita svaki put.

### Sinkronizirani offline mape

Upravljajte offline sinkronizacijom za odabrane mape. Za omogućivanje offline sinkronizacije, dodirnite gumb s tri točke pored mape i odaberite **Dostupno offline**. Nove datoteke dodane u oblak mapu automatski se preuzimaju na uređaj. Pročitajte više o offline načinima [ovdje](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Vremenski interval

Odaberite koliko često se offline mape sinkroniziraju. **Odmah** pokreće sinkronizaciju svaki put kada otvorite aplikaciju.

### Prikaži pune nazive datoteka

Prikazuje potpune nazive datoteka uključujući ekstenzije u upravitelju datoteka.

### Uredi online datoteke

Onemogućite online uređivanje datoteka za prebacivanje u način samo za čitanje za spojene oblak usluge i sprječavanje slučajnih brisanja. Ova radnja uklanja operacije uređivanja datoteka iz korisničkog sučelja.

### Kopiraj datoteke pri otvaranju

Odredite kako aplikacija rukuje uvezenim datotekama iz drugih aplikacija.

### Minijature datoteka

Upravljajte i brišite generirane minijature datoteka za oslobađanje prostora za pohranu.

### Brisanje privremenih datoteka

Ispraznite mapu predmemorije aplikacije za povrat prostora za pohranu.

## Uređivač audio oznaka

Konfigurirajte ugrađeni uređivač audio oznaka.

### Skaliranje omota albuma

Odaberite metodu skaliranja koja se koristi kada se omot albuma sprema u audio oznake.

### Ažuriraj online datoteke

Kada je omogućeno, aplikacija automatski ažurira metapodatke datoteke na oblak poslužitelju nakon što završite s uređivanjem.

### Izbriši datoteku nakon online uređivanja

Odaberite treba li aplikacija izbrisati preuzetu kopiju nakon završetka uređivanja online datoteke na oblak poslužitelju.

### Gumbi glavnog zaslona

Odaberite koji su gumbi vidljivi na glavnom zaslonu uređivača audio oznaka.

## Widgeti

Omogućite widgete kako bi aplikacija ažurirala podatke widgeta tijekom reprodukcije. Ažuriranja widgeta zahtijevaju dodatnu energiju, pa to omogućite samo ako zaista koristite widgete na početnom zaslonu ili zaključanom zaslonu.

Više o Evermusic widgetima možete pročitati u [Vodiču za navigaciju](/docs/guide/evermusic/evermusic-guide-navigation/).

## CarPlay

Ovdje promijenite CarPlay postavke. Ovaj izbornik dostupan je i unutar CarPlay sučelja kako biste mogli prilagoditi iskustvo tijekom vožnje.

### Sortiranje

Konfigurirajte opcije sortiranja za sve CarPlay zaslone.

### Ograničenje učitavanja sadržaja

Odaberite koristi li aplikacija paginaciju na CarPlay zaslonu. Paginacija održava responzivnost izbornika na uređajima s ograničenom memorijom i velikim bibliotekama.

### Boja gradijenta ikona izbornika

Odaberite shemu boja za CarPlay početni zaslon.

### Prikaži slike

Onemogućite slike na CarPlay zaslonu za optimizaciju brzine učitavanja i smanjenje korištenja memorije na velikim bibliotekama.

### Pauziraj reprodukciju pri spajanju

Omogućite ovo za izbjegavanje iznenadnog glasnog zvuka pri spajanju uređaja na CarPlay.

## Wi-Fi Drive

Aktivirajte Wi-Fi Drive za prijenos datoteka s računala na uređaj koristeći desktop web preglednik. Detaljne upute o korištenju Wi-Fi Drive dostupne su [ovdje](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalizacija

Prilagodite korisničko sučelje prema preferencijama.

### Ikona aplikacije

Odaberite alternativnu ikonu aplikacije za početni zaslon.

### Shema boja

Odaberite temu korisničkog sučelja i omogućite tamni način rada. Kada je odabrano **Zadano**, aplikacija prati postavke izgleda cijelog uređaja.

### Stil pozadine

Modificirajte stil pozadine aplikacije. Trenutno jedina opcija je **Zamagljeni omot albuma**, koji koristi artwork trenutno reproducirajuće pjesme kao zamagljenu pozadinu aplikacije.

### Izgled stavki na popisu

Prilagodite prikaz stavki na popisima. Korisno na malim zaslonima — možete pustiti aplikaciju da automatski prilagodi visinu redaka prema sadržaju ili prikazati manje ikone u ćelijama popisa za više prostora za tekst.

### Ograničenje učitavanja sadržaja

Prema zadanim postavkama aplikacija koristi paginaciju za ubrzavanje učitavanja sadržaja. Možete onemogućiti paginaciju za učitavanje svega odjednom.

### Stil zaslona lokalnih datoteka

Promijenite stil prezentacije odjeljka **Lokalne datoteke**.

### Stil zaslona glazbene biblioteke

Prilagodite izgled zaslona **Glazbena biblioteka**.

### Stil zaslona audio reproduktora

Konfigurirajte izgled zaslona **Audio reproduktor**.

### Stil kontekstualnog izbornika

Odaberite stil kontekstualnog izbornika koji se prikazuje pri dodirivanju gumba Više radnji.

## Prozor

Dostupno na Macu i Catalystu. Konfigurirajte preferencije vezane uz prozor poput zadane veličine i ponašanja pri pokretanju.

## Zaslon

Odaberite treba li zaslon ostati aktivan dok koristite aplikaciju. Korisno pri skeniranju velikih biblioteka ili dugotrajnom uređivanju oznaka.

## Pristupačnost

Aktivirajte **Tekstualni način** za skrivanje svih slika u korisničkom sučelju. Tekstualni način automatski se aktivira kada je VoiceOver aktivan i koristan je i za vrlo male ili samo-tekstualne postavke.

## Jezik

Promijenite jezik aplikacije i nadjačajte sistemske zadane postavke. Trenutno aplikacija podržava sljedeće lokalizacije: Afrikaans, Akan, Albanski, Amharski, Arapski, Armenski, Asamski, Aymara, Azerbajdžanski, Bambara, Bengalski, Baskijski, Bjeloruski, Bosanski, Bugarski, Burmanski, Katalonski, Cebuanski, Kineski (pojednostavnjeni), Kineski (tradicionalni), Korzikanski, Hrvatski, Češki, Danski, Dhivehi, Dogri, Nizozemski, Engleski, Esperanto, Estonski, Ewe, Filipinski, Finski, Francuski, Galicijski, Ganda, Gruzijski, Njemački, Grčki, Guarani, Gujarati, Haitski kreolski, Hausa, Havajski, Hebrejski, Hindi, Hmong, Mađarski, Islandski, Igbo, Iloko, Indonezijski, Irski, Talijanski, Japanski, Javanski, Kannada, Kazaški, Khmer, Kinyarwanda, Korejski, Krio, Kurdski, Kurdski sorani, Kirgiški, Laoški, Latinski, Latvijski, Lingala, Litvanski, Luksemburški, Makedonski, Maithili, Malagaški, Malajski, Malajalam, Malteški, Maorski, Marathski, Mizo, Mongolski, Nepali, Sjeverni Sotho, Norveški bokmal, Nyanja, Odiya, Oromo, Paštu, Perzijski, Poljski, Portugalski, Punjabi, Rumunjski, Ruski, Samojski, Sanskrit, Škotski gaelski, Srpski, Shona, Sindhi, Sinhala, Slovački, Slovenački, Somalski, Južni Sotho, Španjolski, Sundanski, Svahili, Švedski, Tadžički, Tamilski, Tatarski, Telugu, Tajlandski, Tsonga, Turski, Turkmenski, Ukrajinski, Urdu, Ujgurski, Uzbekistanski, Vijetnamski, Velški, Xhosa, Jidiš, Joruba, Zulu.

## Sigurnosno kopiranje i obnavljanje

Sigurnosno kopirajte sve podatke aplikacije ili ih migrirajte na drugi uređaj. Možete odabrati što uključiti:

- **Baza podataka** — sve pjesme glazbene biblioteke i popisi pjesama. Offline pjesme nisu uključene za održavanje veličine sigurnosne kopije.
- **Omoti albuma** — svi predmemorirani omoti albuma.
- **Postavke** — sve postavke aplikacije.

Dodirnite **Sigurnosno kopiraj podatke aplikacije** za pokretanje sigurnosnog kopiranja. Podaci aplikacije zapisuju se u jednu datoteku koju možete koristiti za obnavljanje stanja aplikacije na novom uređaju ili nakon ponovne instalacije.

Za obnavljanje podataka aplikacije na novom uređaju, premjestite datoteku sigurnosne kopije na novi uređaj koristeći spojenu oblak uslugu ili iCloud i otvorite je na novom uređaju.

Imamo detaljan vodič korak po korak ovdje: [Kako prenijeti glazbenu biblioteku između uređaja u Evermusicu: Vodič korak po korak](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Pomoć

Otvorite vodič aplikacije za pomoć i smjernice o učinkovitom korištenju aplikacije.

## Često postavljana pitanja

Pronađite odgovore na uobičajena pitanja u odjeljku FAQ.

## Pošalji povratne informacije

Imate povratne informacije ili trebate pomoć? Pošaljite povratne informacije timu za podršku izravno iz aplikacije.

## Podijeli ovu aplikaciju

Podijelite aplikaciju s prijateljima kako biste pomogli u širenju.

## Otkrijte više aplikacija

Istražite druge aplikacije tvrtke Everappz.

## Uvjeti i odredbe

Opisuje uvjete i odredbe za korištenje aplikacije. Molimo pročitajte prije korištenja aplikacije.

## Politika privatnosti

Posjetite stranicu politike privatnosti za razumijevanje naših praksi rukovanja podacima. Molimo pročitajte prije korištenja aplikacije.

## Analitika i prikupljanje podataka

Provjerite koje su usluge omogućene za analitiku i prikupljanje podataka i deaktivirajte one koje ne želite.

U **Evermusic Free (plava ikona)**, analitika i dijagnostika prema zadanim su postavkama omogućene kako bi nam pomogle poboljšati aplikaciju — možete ih ovdje isključiti u bilo kojem trenutku. **Evermusic Pro (crvena ikona) ne uključuje nikakvu analitiku ili dijagnostiku** — odjeljak je prazan (ili skriven) jer se ništa ne prikuplja i nema opcije uključivanja.

## Pravne napomene

Sadrži informacije o svakoj biblioteci korištenoj u aplikaciji zajedno s brojem verzije aplikacije i informacijama o izgradnji.
