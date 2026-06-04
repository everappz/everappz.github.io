---
title: "Povezivanja"
date: 2020-02-01
description: "Naučite kako povezati cloud usluge i NAS uređaje s Flacboxom. Streamajte visokokvalitetnu glazbu s iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk i još mnogo toga. Koristite SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder File Sharing i USB flash diskove."
keywords: [
  "Flacbox postavljanje cloud-a", "povežite Google Drive s Flacboxom", "SMB music streaming",
  "WebDAV iOS player", "DLNA glazbena aplikacija", "NAS audio streaming", "Wi-Fi Drive iPhone",
  "prijenos datoteka na iPhone", "Flacbox iTunes File Sharing", "povežite NAS s iPhoneom",
  "Synology Drive glazbena aplikacija", "QNAP glazbena aplikacija", "Bluesound glazbena aplikacija",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "Last.fm scrobbling glazbena aplikacija",
  "iXpand Flash Drive glazba", "USB DAC iPhone"
]
tags: ["vodič", "flacbox", "povezivanja", "cloud", "NAS"]
readingTime: 12
---


Na ovom zaslonu možete povezati svaki izvor koji sadrži vašu glazbu. Možete integrirati popularne cloud usluge poput Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive i još mnogo toga, kao i vaše Mac, PC ili NAS uređaje putem standardnih protokola. Bez obzira nalazi li se vaša kolekcija na streaming-prijatelskoj usluzi poput Dropboxa ili na osobnom NAS-u poput Synologyja, QNAP-a, Buffaloa, Apple Time Capsule ili WD My Cloud Home, Flacbox se povezuje sa svima njima s jednog zaslona.

{{< cards cols="1">}}
  {{< card title="" subtitle="Zaslon Povezivanja u Flacboxu" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Povezivanje s cloud pohranom

- Otvorite karticu **Povezivanja**.
- Odaberite **Poveži se s cloud pohranom** iz izbornika.
- Odaberite uslugu cloud pohrane s popisa.
- Unesite svoje vjerodajnice na službenoj stranici za autorizaciju koju pruža davatelj cloud usluge, zatim tapnite **Završeno**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dodavanje cloud pohrane u Flacboxu" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Ako naiđete na probleme, provjerite internetsku vezu i svoje korisničko ime / lozinku. U Premium verziji aplikacije možete dodati neograničen broj usluga; besplatna verzija podržava do tri.

## Podržane usluge cloud pohrane, medijski poslužitelji i protokoli

Flacbox podržava iznimno širok raspon izvora za vašu glazbu. Sve u nastavku funkcionira s jednog zaslona **Poveži se s cloud pohranom**.

**Osobna cloud pohrana:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Samostalno hostirani poslužitelji:** Plex · Jellyfin · Emby · Subsonic (i svaki Subsonic-kompatibilni poslužitelj — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (i ownCloud putem zajedničkog API-ja) · Synology Drive · QNAP.

**NAS i protokoli za dijeljenje datoteka:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, autentifikacija lozinkom ili javnim ključem) · NFS · DLNA / UPnP (reprodukcija i preuzimanje).

**S3-kompatibilna pohrana objekata:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i bilo koja druga S3-API krajnja točka.

**Otkrivanje na lokalnoj mreži:** Odjeljak Dostupni uređaji automatski navodi svaku Bonjour / mDNS uslugu na vašoj Wi-Fi mreži, tako da možete tapnuti za povezivanje bez unošenja IP adrese.

Svaka veza koristi **službeni SDK ili otvoreni protokol** usluge, s OAuth-temeljenom autorizacijom gdje je podržana. Možete povezati više računa iste usluge (na primjer, dva Google Drive računa, osobni Dropbox uz poslovni ili i Plex i Jellyfin poslužitelj) i pregledavati ih usporedo na zaslonu Povezivanja.

## Sigurnost i privatnost

Koristimo samo službene SDK-ove i sigurne veze za interakciju s povezanim cloud uslugama. Vaše korisničko ime i lozinka nisu dostupni aplikaciji — svi prijenosi su zaštićeni TLS-om.

Kada unesete korisničko ime i lozinku, aplikacija vam prikazuje službenu stranicu za autorizaciju koju pruža davatelj cloud usluge, a cjelokupni proces autorizacije odvija se izvan aplikacije. Davatelj cloud usluge tada šalje auth-token aplikaciji nakon uspješne autorizacije, a taj token se koristi za API pozive.

Auth-token je digitalni ključ koji omogućuje aplikacijama trećih strana interakciju s cloud pohranom u vaše ime. Token je pohranjen na vašem uređaju u Appleovoj sigurnoj pohrani sustava (Keychain), koja je šifrirana i zaštićena lozinkom uređaja ili biometrijskim zaključavanjem. Možete preuzeti datoteke s povezanih cloud usluga na uređaj; te datoteke se smještaju u direktorij Dokumenti aplikacije i mogu se ukloniti u bilo koje vrijeme pomoću ugrađenog upravitelja datoteka.

Aplikacija ne dijeli nikakve informacije s vaših povezanih cloud računa s Everappzom, oglašivačima niti trećim stranama. Pristup svom cloud računu možete opozvati u bilo koje vrijeme otvaranjem stranice s postavkama računa u web pregledniku.

## Opoziv auth-tokena

Za opoziv auth-tokena, prijavite se u svoji cloud račun u web pregledniku i idite na stranicu sigurnosti ili povezanih aplikacija. Tamo možete pronaći svaku aplikaciju treće strane koja je povezana s vašim cloud računom i ukloniti je ako je više ne želite koristiti. Detaljne upute za Google račune dostupne su [ovdje](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Možete i prekinuti vezu s cloud računom unutar same aplikacije — kada to učinite, auth-token se odmah briše s vašeg uređaja. Ako deinstalirate aplikaciju s uređaja, svi preuzeti podaci i pristupni tokeni automatski se uklanjaju zajedno s njom.

## Prekid veze s cloud pohranom ili promjena konfiguracije

- **Pristupite opcijama cloud pohrane** — pronađite povezanu uslugu na zaslonu **Povezivanja**.
- **Tapnite gumb "..."** pored naziva usluge za otvaranje dodatnih opcija:
  - **Preimenuj** — promijenite naziv cloud usluge kako se prikazuje na vašem popisu.
  - **Postavke** — izmijenite konfiguraciju ili podatke za autentifikaciju. Ponekad ćete možda trebati ponovo autorizirati povezanu cloud uslugu ako je autorizacijski token istekao.
  - **Odspoji** — potpuno prekinite vezu između aplikacije i cloud usluge. To uklanja sve pjesme povezane s tom uslugom iz glazbene biblioteke aplikacije, ali ih ostavlja netaknutima na poslužitelju.

## Povezivanje s računalom ili NAS-om

Možete povezati i svoje računalo, osobni NAS ili druge mrežne uređaje koristeći SMB, DLNA ili WebDAV protokole. Ovo je najlakši način da unesete postojeću kućnu glazbenu biblioteku — bilo da se nalazi na Macu, Windows PC-u, Synology boxu ili NAS-u — u Flacbox bez kopiranja ičega.

## Povezivanje s računalom pomoću SMB-a

- Tapnite **Poveži se s cloud pohranom → SMB**.
- Unesite IP adresu računala i naziv dijeljene mape u polje URL-a koristeći format `smb://ip-adresa-računala/naziv-dijeljene-mape`.
- Odaberite verziju protokola: **Auto**, **SMB1** ili **SMB2**.
- Unesite korisničko ime i lozinku (ako su potrebni).
- Tapnite **Završeno**.

Ako je veza uspješna, vidjet ćete povezanu pohranu u odjeljku **Cloud pohrana**. Potpuni vodič o tome kako povezati Mac ili PC putem SMB-a dostupan je [ovdje](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Povezivanje s NAS-om pomoću WebDAV-a

Svi koraci su isti kao za SMB, osim polja URL-a. URL bi trebao biti u formatu `http://naziv-poslužitelja` ili `https://naziv-poslužitelja` ako poslužitelj podržava SSL. WebDAV radi sa **Synology, QNAP, Nextcloud, ownCloud** i mnogim drugim poslužiteljima — svugdje gdje je dostupna WebDAV krajnja točka.

Potpuni vodič o tome kako povezati NAS pomoću WebDAV-a dostupan je [ovdje](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Povezivanje s računalom ili NAS-om pomoću DLNA-e

Također možete dijeliti glazbenu biblioteku smještenu na Windows PC-u ili osobnom NAS-u koristeći DLNA / UPnP protokol i pristupati toj biblioteci u aplikaciji kao što je opisano [ovdje](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA je popularan, široko podržan protokol, ali omogućuje samo reprodukciju ili preuzimanje glazbe — ne možete prenijeti datoteke niti stvoriti nove mape na DLNA poslužitelju.

## Povezivanje s NAS-om ili poslužiteljem koristeći FTP, FTPS ili SFTP

Flacbox podržava i klasične protokole za prijenos datoteka. Za povezivanje poslužitelja putem FTP-a ili FTPS-a, tapnite **Poveži se s cloud pohranom → FTP**, unesite URL hosta u obliku `ftp://naziv-poslužitelja` (ili `ftps://naziv-poslužitelja` za šifriranu vezu), navedite korisničko ime i lozinku, zatim tapnite **Završeno**. Za **SFTP** (SSH File Transfer Protocol), odaberite **SFTP** i navedite lozinku ili par SSH ključeva. Oboje rade s NAS uređajima, Linux hostovima i bilo kojim poslužiteljem koji ima FTP / FTPS / SSH daemon.

## Povezivanje NFS dijeljenja

Flacbox uključuje podršku za **NFS** (Network File System) — praktično za Linux hostove, BSD poslužitelje i NAS uređaje koji preferiraju izlaganje glazbenih biblioteka putem NFS-a umjesto SMB-a. Odaberite **NFS** u izborniku **Poveži se s cloud pohranom**, unesite adresu poslužitelja i izvezenu putanju, zatim tapnite **Završeno**.

## Povezivanje Plex Media Servera

Flacbox se može izravno povezati s Plex Media Serverom i pregledavati vašu glazbenu biblioteku po Izvođačima, Albumima, Žanrovima i Popisima pjesama. Tapnite **Poveži se s cloud pohranom → Plex**, prijavite se Plex računom, odaberite poslužitelj i biblioteka se pojavljuje uz vaše cloud usluge. Plex poslužitelji na istoj lokalnoj mreži također se automatski otkrivaju u odjeljku **Dostupni uređaji**.

## Povezivanje Jellyfin ili Emby poslužitelja

I **Jellyfin** (open-source) i **Emby** (komercijalni) medijski poslužitelji rade nativno u Flacboxu. Tapnite **Poveži se s cloud pohranom → Jellyfin** ili **Emby**, unesite URL poslužitelja (nešto poput `http://ip-poslužitelja:8096`) i vjerodajnice, te je vaša glazbena biblioteka spremna za streaming. Kao i s Plexom, biblioteke na lokalnoj mreži automatski su navedene u **Dostupnim uređajima**.

## Povezivanje Subsonic ili Navidrome poslužitelja

Flacbox govori Subsonic API, što znači da radi sa samim **Subsonicvom**, **Navidromevom** i svakim drugim Subsonic-kompatibilnim poslužiteljem — uključujući Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Tapnite **Poveži se s cloud pohranom → Subsonic**, unesite URL poslužitelja i vjerodajnice, te se biblioteka pojavljuje na zaslonu Povezivanja. Ovo je najlakši način da Flacboxu date pristup osobno hostiranoj glazbenoj kolekciji bez izlaganja temeljnog dijeljenja datoteka.

## Povezivanje s S3-kompatibilnom pohranom objekata

Za osobne hostere i audiofane koji koriste cloud pohranu objekata, Flacbox uključuje S3-kompatibilni konektor. Tapnite **Poveži se s cloud pohranom → S3 pohrana**, zatim unesite URL krajnje točke, regiju, ključ pristupa, tajni ključ i naziv bucketa. Ovo radi s AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i bilo kojom drugom uslugom koja izlaže S3-API krajnju točku.

## Dostupni uređaji

Ovaj odjeljak prikazuje svaki uređaj na vašoj lokalnoj mreži na koji se možete spojiti iz Flacboxa putem Bonjour otkrivanja. Za uspostavljanje veze slijedite ove korake:

- Otvorite aplikaciju i idite na odjeljak **Dostupni uređaji** u Povezivanjima.
- Tapnite uređaj s kojim se želite spojiti.
- Ako je potrebno, unesite podatke za prijavu kako biste dovršili vezu.

Ovo je najbrži način za otkrivanje SMB, WebDAV, DLNA dijeljenja na kućnoj mreži bez ručnog unošenja IP adresa.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dostupni uređaji na lokalnoj mreži u Flacboxu" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive je praktična tehnologija koja omogućuje bežični prijenos datoteka s vašeg računala na iOS uređaj putem bilo kojeg desktop preglednika. Za učinkovito korištenje ove funkcije, osigurajte da su vaš uređaj i računalo spojeni na istu Wi-Fi mrežu. Evo vodiča korak po korak za korištenje Wi-Fi Drive.

### Omogućivanje Wi-Fi Drive-a

- Otvorite aplikaciju i idite na karticu **Povezivanja**.
- Odaberite **Poveži se putem Wi-Fi-ja** za pristup glavnom zaslonu Wi-Fi Drive-a.
- (Neobavezno) Postavite korisničko ime i lozinku za ugrađeni web poslužitelj radi zaštite pristupa.
- Tapnite **Pokreni Wi-Fi Drive** za omogućivanje Wi-Fi Drive-a.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive u Flacboxu" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Pristup Wi-Fi Drive-u na računalu

- Na računalu (desktop ili laptop), otvorite web preglednik (poput Chromea, Firefoxa ili Safarija).
- U adresnoj traci preglednika unesite URL koji pruža aplikacija.

### Bežični prijenos datoteka

Kada se web stranica odgovarajuća vašem iOS uređaju otvori u pregledniku, možete lako povući i ispustiti datoteke s računala na web stranicu. Datoteke koje ispustite počet će se prenositi na vaš iOS uređaj i bit će dostupne unutar Flacboxa.

Wi-Fi Drive možete i montirati izravno u Finderu na macOS-u (Idi → Poveži se s poslužiteljem…) ili File Exploreru na Windowsima (Mapiraj mrežni pogon…) i tretirati iPhone ili iPad kao redovni mrežni pogon.

Detaljne upute o tome kako bežično prenositi datoteke koristeći Wi-Fi Drive dostupne su [ovdje](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (sada Finder File Sharing na macOS Catalina i novijim verzijama) je još jedan način prijenosa datoteka s računala na uređaj koristeći Lightning ili USB-C kabel.

- Spojite uređaj na računalo kabelom i pokrenite **Finder** na Macu (ili **iTunes** na Windowsima).
- Otvorite **Lokacije → Vaš spojeni uređaj → Datoteke** i pronađite Flacbox aplikaciju.
- Tapnite na ikonu aplikacije da biste vidjeli sve dijeljene mape.
- Kopirajte datoteke s računala u dijeljenu mapu na uređaju koristeći povuci i ispusti.

Detaljne upute o tome kako koristiti Finder File Sharing dostupne su [ovdje](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Povezivanje USB flash diska

Ako imate SD karticu ili USB pogon, možete ga spojiti koristeći Lightning na USB / SD Card Reader ili USB-C pogon (na iPadu i iPhoneu 15 / 16 / 17 / Pro). Aplikacija podržava Apple Certified čitače kartica i iXpand Flash Diskove. S iXpand Flash Diskom, umetnite ga u Lightning priključak i otvorite aplikaciju — vidjet ćete poruku Eksterni uređaj spojen i informacije o uređaju. Tapnite ikonu flash diska za pristup mapi s glazbom i tapnite bilo koju audio datoteku za početak reprodukcije.

Imamo detaljne upute o tome kako spojiti USB flash disk na iPhone i slušati glazbu ili upravljati datotekama koje se nalaze na njemu [ovdje](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Upravitelj datoteka

Nakon što ste spojili uslugu cloud pohrane, tapnite njezinu ikonu za pregled svih dostupnih datoteka i mapa. Možete koristiti ugrađeni upravitelj datoteka za rad s tim datotekama — preuzimanje, preimenovanje, premještanje, prijenos, brisanje i još mnogo toga. Kada pokrenete preuzimanje, datoteka se pojavljuje u redu čekanja za prijenos. Za otvaranje reda čekanja za prijenos, idite na karticu Lokalne datoteke i tapnite ikonu s rotirajućim strelicama u gornjem lijevom kutu. Sve preuzete datoteke i mape dostupne su u odjeljku Lokalne datoteke.

## Gornja alatna traka

Gornja alatna traka, prikladna za smještaj ispod navigacijske trake, nudi nekoliko korisnih radnji za lak pristup. Možete je prikazati ili sakriti jednostavnim gestom povlačenja prema dolje.

- **Pretraži** — brzo pretražite unutar trenutnog direktorija, što olakšava pronalaženje određenih datoteka ili mapa.
- **Nastavi reprodukciju** — ako je omogućeno u postavkama aplikacije, ovo obnavlja red čekanja audio playera i posljednju medijsku poziciju za trenutnu mapu. Praktičan način za nastavak tamo gdje ste stali.
- **Pusti sve** — skenira trenutnu mapu i njene podmape, zatim dodaje sve pronađene audio datoteke u novi red čekanja playera. Korisno kada želite pustiti svaki zapis u direktoriju.
- **Reproduciraj sve nasumično** — kao Pusti sve, ali miješa datoteke prije dodavanja u red čekanja audio playera. Odlično za ponovnog otkrivanje stare mape s glazbom.

## Opcije mape

Kada otvorite mapu, naći ćete praktičan skup radnji dostupnih tapnutjem na gumb **"..."** u gornjem desnom kutu.

- **Odaberi** — aktivirajte način odabira datoteka. To vam omogućuje odabir jedne ili više datoteka unutar mape i izvođenje radnji nad cijelim odabirom.
- **Nova mapa** — stvorite novu mapu unutar trenutne mape. Odlično za dobro strukturiranje biblioteke.
- **Omogući offline način rada** — uključite offline način rada za trenutnu mapu. Offline način rada nadilazi jednostavno preuzimanje: aktivno prati mapu za promjenama. Ako dodate nove datoteke online, automatski će se pojaviti na vašem uređaju.
- **Prenesi datoteke** — prenesite datoteke s vašeg uređaja u online mapu. To ih čini dostupnima s bilo kojeg mjesta putem iste cloud usluge.
- **Pretraži** — pretražite određene datoteke unutar trenutne mape.
- **Sortiraj** — sortirajte datoteke po imenu, veličini, datumu izmjene ili prema metapodacima. Zadani način sortiranja odražava redoslijed sortiranja na poslužitelju, ali ga možete promijeniti prema svojim preferencijama.
- **Prikaz mreže / popisa** — prebacite se između prikaza tablice i prikaza minijatura. Prikaz tablice prikazuje kompaktan popis; prikaz minijatura prikazuje velike preglede ilustracija za brzu vizualnu identifikaciju.

## Uređivanje online datoteka

Kada trebate upravljati s više datoteka u cloud pohrani, koristite **Način odabira** za pojednostavljivanje radnji:

- **Aktivirajte način odabira** — tapnite gumb **"..."** u gornjem desnom kutu i odaberite **Odaberi**.
- **Odaberite datoteke** — pojavit će se potvrdni okviri pokraj svake datoteke i mape. Tapnite za odabir jedne ili više stavki.
- **Izvedite radnje** — nakon odabira datoteka ili mapa, imat ćete pristup radnjama Pusti sljedeće, Pusti poslije, Dodaj u glazbenu biblioteku, Dodaj u popis pjesama, Kopiraj, Prenesi, Premjesti, Preimenuj i Izbriši.

Ako želite tretirati povezanu cloud pohranu samo za čitanje (kako biste spriječili slučajno brisanje), omogućite Postavke → Upravitelj datoteka → Uredi online datoteke → Isključeno za skrivanje svih destruktivnih operacija iz sučelja.

## Radnje s datotekama

Tapnite ikonu **"..."** pored naslova datoteke za prikaz izbornika radnji:

- **Pusti sljedeće** — umetnite datoteku na vrh reda čekanja playera, tako da se reproducira odmah nakon trenutnog zapisa.
- **Pusti poslije** — dodajte datoteku na dno reda čekanja playera.
- **Dodaj u glazbenu biblioteku** — uključite datoteku u glazbenu biblioteku, organiziranu po izvođaču, albumu, žanru ili skladatelju.
- **Dodaj u popis pjesama** — dodajte datoteku u postojeći popis pjesama ili stvorite novi.
- **Uredi audio oznake** — otvorite ugrađeni editor oznaka za izmjenu metapodataka. Za online datoteke, zapis se privremeno preuzima, uređuje, a zatim ponovo prenosi nakon potvrde.
- **Dodaj u omiljene** — dodajte datoteku na popis omiljenih za brzi pristup.
- **Preuzmi** — preuzmite datoteku ili mapu na uređaj za offline korištenje.
- **Preimenuj** — preimenujte datoteku izravno na udaljenom serveru.
- **Premjesti** — premjestite datoteku u drugu mapu unutar cloud pohrane.
- **Otvori u** — izvezite datoteku u drugu kompatibilnu aplikaciju. Datoteka se preuzima na uređaj, zatim se pojavljuje sistemski dijaloški okvir za dijeljenje.
- **Izbriši** — trajno uklonite datoteku iz cloud pohrane. **Ova radnja se ne može poništiti.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Više radnji za datoteku u povezanoj cloud pohrani u Flacboxu" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

Ako popis radnji prekoračuje dostupni prostor na zaslonu, jednostavno se pomaknite prema dolje unutar izbornika radnji za pristup dodatnim opcijama.

## Radnje s mapama

Za svaku mapu u cloud pohrani, imate širok raspon dostupnih radnji tapnutjem na ikonu **"..."** pored naslova mape. Ako ne vidite sve radnje, pomaknite se prema dolje za prikaz više.

- **Pusti sve** — zamijenite trenutni red čekanja playera svim stavkama iz odabrane mape.
- **Pusti sljedeće** — dodajte cijelu mapu na vrh reda čekanja playera.
- **Pusti poslije** — dodajte sadržaj mape na dno reda čekanja playera.
- **Dodaj u glazbenu biblioteku** — uključite sadržaj mape u glazbenu biblioteku.
- **Dodaj u popis pjesama** — dodajte cijelu mapu u popis pjesama. Imate mogućnost i stvaranja novog popisa pjesama; naziv se automatski dodjeljuje od naziva mape.
- **Dodaj u omiljene** — dodajte mapu u omiljene za brzi pristup.
- **Omogući offline način rada** — osim jednostavnog preuzimanja, kontinuirano prati mapu za novim datotekama i automatski ih preuzima čim se pojave online.
- **Preuzmi** — preuzmite sav sadržaj mape na uređaj za offline pristup.
- **Preimenuj** — preimenujte mapu izravno na udaljenom serveru.
- **Premjesti** — premjestite mapu na drugu lokaciju unutar cloud pohrane.
- **Arhiviraj (ZIP)** — spakirajte sadržaj mape u jednu ZIP datoteku (Premium funkcija).
- **Izbriši** — trajno uklonite mapu i njezin sadržaj iz cloud pohrane. **Ova radnja se ne može poništiti.**

## Brzi pristup

Odjeljak Brzi pristup nalazi se na vrhu zaslona. Daje vam brzi pristup vašim omiljenim i nedavno otvorenim datotekama iz povezanih cloud usluga. Kad god otvorite datoteku ili mapu iz clouda, dodaje se na popis Nedavno otvoreno. Za brisanje ovog popisa, otvorite Nedavne, tapnite gumb Više radnji i odaberite Izbriši popis. Također možete označiti duboko ugniježđene mape kao Omiljene za brzi pristup bez kopanja kroz strukturu direktorija.

{{< cards cols="1">}}
  {{< card title="" subtitle="Online poveznice i brzi pristup u Flacboxu" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Ostale usluge

Ovaj odjeljak prikazuje dodatne funkcije koje poboljšavaju vaše iskustvo. Trenutno aplikacija podržava **Last.fm** scrobbling — kada je spojen, vaše statistike reprodukcije automatski se šalju na vaš Last.fm račun. Kasnije možete posjetiti svoj Last.fm profil za pregled analitike slušanja i dobivanje personaliziranih preporuka za glazbu. Detaljne upute za postavljanje dostupne su [ovdje](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Last.fm Connect" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
