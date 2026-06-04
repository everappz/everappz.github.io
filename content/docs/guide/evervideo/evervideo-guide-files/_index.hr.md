---
title: "Datoteke"
date: 2020-02-01
lastmod: 2026-06-01
description: "Naučite kako koristiti karticu Datoteke u Evervideu na iPhone, iPad i Mac. Povežite cloud usluge, NAS uređaje, medijske servere i RTSP streamove na jednom mjestu. Upravljajte offline videozapisima, redom prijenosa, preuzimanjima, Wi-Fi Drive, iTunes / Finder File Sharing i USB diskovima. Uključuje iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA i S3-kompatibilnu pohranu."
keywords: [
  "datoteke Evervideo", "veze Evervideo", "lokalne datoteke Evervideo",
  "postavljanje cloud videa iPhone", "spajanje Google Drive videa", "SMB video streaming",
  "WebDAV video player iOS", "DLNA video iPhone", "NAS video streaming",
  "Wi-Fi Drive video prijenos", "Evervideo iTunes File Sharing", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "Evervideo offline video", "Evervideo red prijenosa",
  "Evervideo upravitelj datoteka", "Evervideo mapa Documents",
  "Synology video player", "QNAP video player",
  "Apple Time Capsule video player", "USB DAC video",
  "iXpand video player", "S3 video player"
]
tags: ["vodič", "evervideo", "datoteke", "veze", "cloud", "NAS", "Plex", "RTSP"]
readingTime: 14
---

Kartica Datoteke je sveobuhvatni upravitelj datoteka Evervideo. Za razliku od većine video aplikacija koje odvajaju pohranu u oblaku od lokalnih datoteka u različite kartice, Evervideo ih spaja u jedan pomični zaslon tako da možete prijeći s Plex servera na mapu u oblaku do mape Documents na vašem iPhoneu bez skakanja između kartica.

Kartica Datoteke podijeljena je na jasne odjeljke koji se prikazuju ovim redoslijedom na vašem zaslonu:

- **Brzi pristup** — nedavni i omiljeni za datoteke i mape koje ste nedavno otvorili.
- **Datoteke u ovoj aplikaciji** — što se nalazi u sandboxiranoj mapi Documents Evervideo.
- **Datoteke na ovom iPhone / iPad / Mac** — videozapisi drugdje na vašem uređaju, prikazani kroz sistemski birač datoteka.
- **Pohrana u oblaku** — svaki cloud račun, NAS i medijski server koji ste povezali.
- **Dostupni uređaji** — serveri i diskovi automatski otkriveni putem Bonjour / mDNS na vašoj lokalnoj mreži.

U gornjem desnom kutu zaslona Datoteke nalazi se gumb Prijenosi (ikona strelica u vrtnji). Dodirnite ga za otvaranje Reda prijenosa gdje pratite svako preuzimanje i prijenose na svim vašim izvorima.

{{< cards cols="1">}}
  {{< card title="" subtitle="Datoteke Evervideo na povezanim pohranama" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Spajanje na pohranu u oblaku

Odjeljak Pohrana u oblaku kartice Datoteke je mjesto gdje živi svaki povezani račun, NAS, medijski server i stream — jedan pokraj drugog, u jednom pomičnom popisu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Odjeljak pohrane u oblaku Evervideo u kartici Datoteke" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Otvorite karticu **Datoteke**.
- Pomaknite se do odjeljka **Pohrana u oblaku**.
- Dodirnite **Povezati na cloud pohranu** iz izbornika.
- Odaberite uslugu pohrane u oblaku s popisa.
- Unesite svoje vjerodajnice na službenoj stranici za autorizaciju koju je pružio cloud pružatelj, zatim dodirnite **Završeno**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Spajanje usluge pohrane u oblaku" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Ako naiđete na probleme, provjerite svoju internetsku vezu i lozinku. U Premium verziji aplikacije možete dodati neograničen broj usluga; besplatna verzija podržava do tri.

## Podržane usluge pohrane u oblaku, medijski serveri i protokoli

Evervideo podržava iznimno širok raspon izvora za vaše videozapise. Sve u nastavku radi iz jednog toka spajanja na pohranu u oblaku.

**Osobna pohrana u oblaku:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Samostalno hostovani medijski serveri:** Plex · Jellyfin · Emby · Subsonic (i svaki Subsonic-kompatibilni server — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (i ownCloud putem zajedničkog API-ja) · Synology Drive · QNAP.

**NAS i protokoli dijeljenja datoteka:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, lozinka ili autentifikacija javnim ključem) · NFS · DLNA / UPnP (reprodukcija i preuzimanje).

**Live streamovi i IP kamere:** RTSP — usmjerite Evervideo na bilo koji URL `rtsp://` i odmah reproducira. Odlično za sigurnosne kamere, IPTV streamove, kamere na zvoncu, monitore za bebe i slične live izvore.

**S3-kompatibilna pohrana objekata:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i bilo koji drugi S3-API endpoint.

**Biblioteke na uređaju:** biblioteka Photos (svi videozapisi, snimke zaslona, foto albumi) i biblioteka aplikacije Music (Albumi, Žanrovi, Popisi za reproduciju) — obje se prikazuju unutar Medijske biblioteke tako da ne morate ništa kopirati.

**Otkrivanje lokalne mreže:** odjeljak Dostupni uređaji automatski navodi svaku Bonjour / mDNS uslugu na vašoj Wi-Fi mreži — serveri Plex, Jellyfin, Emby, Synology, QNAP, AirPort ruteri s priključenim diskovima, Apple Time Capsule — tako da možete dodirnuti za spajanje bez unošenja IP adrese.

## Sigurnost i privatnost

Evervideo koristi samo službene SDK-ove i sigurne veze za interakciju s povezanim cloud uslugama. Vaše korisničko ime i lozinka nisu dostupni aplikaciji — svi prijenosi su TLS-šifrirani.

Kada unosite korisničko ime i lozinku, aplikacija vam pokazuje službenu stranicu za autorizaciju koju je pružio cloud pružatelj usluga, a cijeli proces autorizacije odvija se izvan aplikacije. Cloud pružatelj usluga zatim šalje auth-token aplikaciji nakon uspješne autorizacije, a taj token se koristi za API pozive.

auth-token je digitalni ključ koji trećim aplikacijama omogućuje interakciju s pohranom u oblaku u vaše ime. Token se pohranjuje na vašem uređaju u Appleovoj sigurnoj sistemskoj pohrani (Keychain), koja je šifrirana u mirovanju i zaštićena vašom lozinkom uređaja ili biometrijskim zaključavanjem. Možete preuzimati datoteke s povezanih cloud usluga na uređaj; te datoteke se smještaju u aplikacijsku mapu Documents i mogu se ukloniti u bilo koje vrijeme pomoću ugrađenog upravitelja datoteka.

Aplikacija ne dijeli nikakve informacije s vaših povezanih cloud računa s Everappz, oglašivačima ili trećim stranama. Pristup svom cloud računu možete opozvati u bilo koje vrijeme otvaranjem stranice postavki računa u svom web pregledniku.

## Opoziv auth-tokena

Za opoziv auth-tokena, prijavite se u cloud račun u web pregledniku i idite na stranicu sigurnosti ili povezanih aplikacija. Tamo možete pronaći svaku aplikaciju treće strane koja je povezana s vašim cloud računom i ukloniti bilo koju od njih ako je više ne želite koristiti. Detaljne upute za Google račune dostupne su [ovdje](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Možete i odspojiti cloud račun unutar same aplikacije — kada to učinite, auth-token se odmah briše s vašeg uređaja. Ako deinstalirate aplikaciju s uređaja, svi preuzeti podaci i pristupni tokeni automatski se uklanjaju zajedno s njom.

## Odspajanje pohrane u oblaku ili promjena konfiguracije

- **Pristup opcijama pohrane u oblaku** — pronađite povezanu uslugu u odjeljku **Pohrana u oblaku** kartice Datoteke.
- **Dodirnite gumb "..."** pored naslova usluge za otvaranje dodatnih opcija:
  - **Preimenovati** — promijenite naziv cloud usluge kako se prikazuje na vašem popisu.
  - **Postavke** — izmijenite konfiguraciju ili podatke za autentifikaciju. Ponekad ćete morati ponovno autorizirati povezanu cloud uslugu ako je autorizacijski token istekao.
  - **Odspojiti** — potpuno prekinite vezu između aplikacije i cloud usluge. Time se uklanjaju svi videozapisi povezani s tom uslugom iz vaše medijske biblioteke, ali ostaju netaknuti na serveru.

## Spajanje na računalo ili NAS

Možete spojiti svoje računalo, osobni NAS ili drugi mrežni uređaj koristeći protokol SMB, WebDAV, FTP / FTPS, SFTP, NFS ili DLNA. To je najlakši način za unošenje postojeće kućne medijske biblioteke — bila ona na Macu, Windows PC-u, Synologyu, QNAP-u, Apple Time Capsule ili WD My Cloud Home — u Evervideo bez kopiranja bilo čega.

### Spajanje na računalo pomoću SMB

- Dodirnite **Povezati na cloud pohranu → SMB**.
- Unesite IP adresu računala i naziv dijeljene mape koristeći format `smb://ip-adresa-racunala/naziv-dijeljene-mape`.
- Odaberite verziju protokola: **Auto**, **SMB1** ili **SMB2**.
- Unesite korisničko ime i lozinku (ako se traži).
- Dodirnite **Završeno**.

Ako je spajanje uspješno, dijeljeni disk pojavljuje se u odjeljku Pohrana u oblaku. Potpuni vodič o spajanju Mac-a ili PC-a pomoću SMB dostupan je [ovdje](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Spajanje na NAS pomoću WebDAV

Svi koraci su isti kao za SMB, osim polja URL-a. Koristite `http://naziv-servera` ili `https://naziv-servera` ako server podržava SSL. WebDAV radi sa Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home i bilo kojim drugim serverom s WebDAV endpointom.

Potpuni vodič o WebDAV-u dostupan je [ovdje](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Spajanje putem DLNA / UPnP

Dijelite medijsku biblioteku koja se nalazi na vašem Windows PC-u ili NAS-u pomoću DLNA / UPnP protokola i pristupite joj unutar Evervideo kako je opisano [ovdje](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA je široko podržan, ali omogućuje samo reprodukciju ili preuzimanje videozapisa — ne možete učitavati datoteke ili stvarati nove mape na DLNA serveru.

### Spajanje pomoću FTP, FTPS ili SFTP

Evervideo podržava i klasične protokole za prijenos datoteka. Za spajanje servera putem FTP ili FTPS, dodirnite Povezati na cloud pohranu → FTP, unesite URL hosta u obliku `ftp://naziv-servera` (ili `ftps://naziv-servera` za šifriranu vezu), unesite korisničko ime i lozinku, zatim dodirnite Završeno. Za SFTP (SSH File Transfer Protocol), odaberite SFTP umjesto toga i navedite lozinku ili par SSH ključeva.

### Spajanje na NFS dijeljeni disk

Evervideo uključuje NFS (Network File System) podršku — korisno za Linux hostove, BSD servere i NAS uređaje koji preferiraju izlaganje video biblioteka putem NFS-a umjesto SMB-a. Odaberite NFS u izborniku Povezati na cloud pohranu, unesite adresu servera i izvezenu putanju i dodirnite Završeno.

## Spajanje na Plex Media Server

Evervideo se može izravno spojiti na Plex Media Server i pregledavati vaše biblioteke Movies, TV Shows i Home Videos. Dodirnite Povezati na cloud pohranu → Plex, prijavite se s Plex računom, odaberite server, i biblioteka se pojavljuje uz vaše cloud usluge. Plex serveri na istoj lokalnoj mreži automatski se otkrivaju i u odjeljku Dostupni uređaji.

## Spajanje na Jellyfin ili Emby Server

I Jellyfin (open-source) i Emby (komercijalni) medijski serveri rade nativno u Evervideu. Dodirnite Povezati na cloud pohranu → Jellyfin ili Emby, unesite URL servera (obično nešto poput `http://ip-servera:8096`) i vjerodajnice, i vaša biblioteka je spremna za streaming.

## Spajanje na Subsonic ili Navidrome Server

Evervideo govori Subsonic API, što znači da radi sa Subsonicm, Navidromeom i svakim drugim Subsonic-kompatibilnim serverom — uključujući Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) i Ampache. Dodirnite Povezati na cloud pohranu → Subsonic, unesite URL servera i vjerodajnice, i biblioteka se pojavljuje u odjeljku Pohrana u oblaku.

## Spajanje RTSP streama (IP kamere, Live TV, IPTV)

Evervideo ima nativnu RTSP podršku, tako da ga možete usmjeriti na bilo koji RTSP izvor — sigurnosne kamere, kamere na zvoncu, IPTV pružatelje, monitore za bebe, emitiranja — i Evervideo će povući i dekodirati stream uživo. Dodirnite Online veze → Dodaj vezu, zalijepite puni URL (`rtsp://ip-kamere:port/put-streama`), navedite korisničko ime i lozinku ako se traži, i dodirnite Završeno.

## Spajanje na S3-kompatibilnu pohranu objekata

Za samostalne hostere i napredne korisnike koji koriste cloud pohranu objekata, Evervideo uključuje S3-kompatibilni konektor. Dodirnite Povezati na cloud pohranu → S3 pohrana, zatim unesite URL endpointa, regiju, pristupni ključ, tajni ključ i naziv bucketa. Ovo radi s AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i bilo kojim drugim S3-API endpointom.

## Dostupni uređaji

Ovaj odjeljak prikazuje svaki uređaj na vašoj lokalnoj mreži na koji se možete spojiti iz Evervideo putem Bonjour / mDNS otkrivanja — serveri Plex, Jellyfin, Emby, Synology, QNAP, AirPort ruteri s priključenim diskovima, Apple Time Capsule, i tako dalje. Za uspostavljanje veze:

- Pomaknite se do odjeljka Dostupni uređaji u kartici Datoteke.
- Dodirnite uređaj na koji se želite spojiti.
- Ako je potrebno, unesite podatke za prijavu za dovršetak veze.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dostupni uređaji Evervideo na lokalnoj mreži" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive omogućuje bežični prijenos datoteka s računala na vaš iOS uređaj putem bilo kojeg desktop preglednika, Findera ili File Explorera. Uređaj i računalo moraju biti na istoj Wi-Fi mreži.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Omogućavanje Wi-Fi Drive

- U kartici Datoteke, pomaknite se do Pohrana u oblaku → Spoji se putem Wi-Fi za otvaranje glavnog zaslona Wi-Fi Drive.
- (Neobavezno) Postavite korisničko ime i lozinku za ugrađeni web server.
- Dodirnite Pokreni Wi-Fi Drive.

### Pristup Wi-Fi Drive na računalu

- Otvorite web preglednik na računalu (Chrome, Firefox, Safari, itd.).
- Unesite URL koji prikazuje aplikacija.
- Povucite i ispustite datoteke s računala na web stranicu — počet će se prenositi na vaš iOS uređaj.

Wi-Fi Drive možete i montirati izravno u **Finderu** na macOS (Idi → Spoji se na server…) ili File Exploreru na Windows (Mapiraj mrežni disk…) i tretirati iPhone ili iPad kao obični mrežni disk.

Detaljne upute dostupne su [ovdje](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (sada Finder File Sharing na macOS Catalina i novijima) omogućuje prijenos datoteka pomoću Lightning ili USB-C kabela. Spojite uređaj, otvorite Finder na Macu (ili iTunes na Windowsima), pronađite Evervideo na popisu aplikacija i kopirajte datoteke u njegovu dijeljenu mapu.

## Spajanje USB flash diska ili SD kartice

Umetnite USB disk ili SD karticu u iPhone, iPad ili Mac putem Lightning-to-USB / USB-C adaptera ili čitača kartica. Otvorite Datoteke → Datoteke na ovom iPhone → Otvori mapu, idite do diska i odaberite video datoteku ili mapu. Evervideo reproducira datoteke izravno s diska bez kopiranja u internu pohranu — korisno za vrlo velike 4K biblioteke.

## Pregledavanje mapa u povezanim pohranama

Dodirnite bilo koju povezanu cloud uslugu za otvaranje njezina preglednika datoteka. Mape prikazuju video minijature kada su dostupne, a dodirivanje videozapisa odmah pokreće reprodukciju dok nastavlja streamati ostatak datoteke u pozadini.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Pregledavanje mapa u povezanim pohranama" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Brzi pristup

Odjeljak Brzi pristup nalazi se na vrhu kartice Datoteke. Daje vam brzi pristup omiljenim i nedavno otvorenim datotekama i mapama — i iz cloud usluga i iz pohrane na uređaju. Kad god otvorite datoteku ili mapu iz oblaka, dodaje se na popis Nedavno otvoreno. Možete označiti duboko ugniježđene mape kao Omiljene za brzi pristup bez kopanja kroz strukturu direktorija.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo online veze i brzi pristup" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Datoteke u ovoj aplikaciji

Ovaj odjeljak prikazuje datoteke i mape pohranjene u sandboxiranom direktoriju Documents Evervideo — sve što ste preuzeli iz oblaka, prenijeli putem Wi-Fi Drive, kopirali kroz Finder File Sharing ili uvezli iz druge aplikacije.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Datoteke u ovoj aplikaciji" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Mapa Documents

Mapa Documents je korijen svega unutar Datoteka u ovoj aplikaciji. Možete stvarati podmape, preimenovati datoteke, premještati ih i grupirati kako želite.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo lokalne datoteke — Mapa Documents" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Datoteke na ovom iPhone / iPad / Mac

Ovaj odjeljak prikazuje videozapise smještene na vašem uređaju, ali u različitim aplikacijama. Možete ih uvesti u Evervideo pomoću sistemskog birača datoteka:

- Dodirnite Otvori datoteke… za odabir određenih datoteka.
- Dodirnite Otvori mapu… za odabir cijele mape.

Možete koristiti i Spoji mapu za stvaranje veze na mapu na vašem uređaju s pristupom za čitanje / pisanje — savršeno za rad s mapom na iCloud Driveu ili priključenim USB diskom bez kopiranja bilo čega.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Datoteke na ovom uređaju" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Posebne mape

Unutar kartice Datoteke vidjet ćete nekoliko posebnih mapa koje Evervideo automatski stvara i koristi:

- **Preuzimanja** — svaka datoteka preuzeta iz oblaka pojavljuje se ovdje prema zadanim postavkama. Prilagodite u Postavke → Upravitelj datoteka → Spremi preuzete datoteke u.
- **Predmemorija playera** — predmemorija medijskog playera. Prema zadanim postavkama player preuzima nadolazeće videozapise za glatku reprodukciju. Predmemoriju možete onemogućiti u postavkama aplikacije ili jednostavno obrisati ovu mapu.
- **iCloud** — datoteke u ovoj mapi sinkroniziraju se na svim vašim uređajima spojenim na isti iCloud račun.
- **Offline mape** — kada označite mapu, popis za reproduciju, album ili žanr kao dostupan offline, datoteke se preuzimaju u ovu mapu.

## Gornja alatna traka

Gornja alatna traka, smještena ispod navigacijske trake, nudi nekoliko radnji koje možete prikazati ili sakriti gestom povlačenja prema dolje:

- **Pretraživanje** — izvršite pretraživanje unutar trenutne mape ili odjeljka.
- **Nastavi reproduciranje** — ako je omogućeno u postavkama, obnovite red playera i zadnji položaj videa za trenutnu mapu.
- **Reproduciraj sve** — skenirajte trenutnu mapu i njene podmape i dodajte datoteke u red playera.
- **Nasumično sve** — kao Reproduciraj sve, ali miješa prije dodavanja.

## Opcije mape

Kada otvorite mapu, dodirnite gumb **"..."** u gornjem desnom kutu za ove radnje:

- **Odabrati** — aktivirajte način odabira datoteka.
- **Nova mapa** — stvorite novu mapu unutar trenutne mape.
- **Omogućiti offline način rada** — uključite offline sinkronizaciju za trenutnu mapu. Nove datoteke dodane online automatski se preuzimaju.
- **Učitaj datoteke** — učitajte datoteke s uređaja u online mapu.
- **Pretraživanje** — pretražujte unutar mape.
- **Sortiraj** — sortirajte datoteke po nazivu, veličini, datumu izmjene ili metapodacima.
- **Prikaz mreže / popisa** — prebacujte između prikaza tablice i prikaza minijatura. Prikaz minijatura prikazuje velike preglede video postera.

## Način odabira

Dodirnite **"..."** u gornjem desnom kutu i odaberite **Odabrati** za ulazak u način odabira. Potvrdni okviri pojavljuju se pored svake datoteke i mape. Dodirnite za odabir jedne ili više stavki, zatim izvršite skupne radnje: Reproduciraj sljedeće, Reproduciraj kasnije, Dodaj u medijsku biblioteku, Dodaj u popis za reproduciju, Kopiraj, Prenesi, Premjesti, Preimenuj ili Izbriši.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Način odabira u upravitelju datoteka" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Ako radije tretirate povezanu cloud pohranu kao read-only (za sprječavanje slučajnih brisanja), omogućite Postavke → Upravitelj datoteka → Uredi online datoteke → Isključeno za skrivanje svih destruktivnih operacija iz korisničkog sučelja.

## Radnje na datotekama

Dodirnite ikonu **"..."** pored naslova datoteke za prikaz izbornika radnji:

- **Reproduciraj sljedeće** — umetnite datoteku na vrh reda playera.
- **Reproduciraj kasnije** — dodajte datoteku na dno reda playera.
- **Dodaj u medijsku biblioteku** — uključite datoteku u svoju medijsku biblioteku, organiziranu po Albumu i Žanru.
- **Dodaj u popis za reproduciju** — dodajte datoteku u postojeći popis za reproduciju ili stvorite novi.
- **Urediti audio oznake** — otvorite ugrađeni uređivač oznaka za izmjenu metapodataka. Za online datoteke, datoteka se privremeno preuzima, uređuje, a zatim ponovo učitava nakon što potvrdite.
- **Dodaj u omiljene** — dodajte datoteku na popis omiljenih za brzi pristup.
- **Preuzeti** — preuzmite datoteku ili mapu na uređaj za offline korištenje.
- **Preimenovati** — preimenujte datoteku izravno na udaljenoj pohrani.
- **Premjesti** — premjestite datoteku u drugu mapu unutar cloud pohrane.
- **Dodaj u arhivu** — spakujte datoteku u jednu ZIP datoteku (Premium značajka).
- **Otvori u** — izvezite datoteku u drugu kompatibilnu aplikaciju putem sistemskog lista za dijeljenje.
- **Izbrisati** — trajno uklonite datoteku. **Ova radnja se ne može poništiti.**

## Radnje na mapama

Za svaku mapu u vašoj cloud pohrani dostupne su mnoge radnje dodirivanjem ikone **"..."** pored naslova mape.

- **Reproduciraj sve** — zamijenite trenutni red playera svakim videozapisom u mapi.
- **Reproduciraj sljedeće / Reproduciraj kasnije** — dodajte cijelu mapu u red.
- **Dodaj u medijsku biblioteku** — uključite sadržaj mape u svoju medijsku biblioteku.
- **Dodaj u popis za reproduciju** — dodajte cijelu mapu u popis za reproduciju.
- **Dodaj u omiljene** — dodajte mapu u omiljene.
- **Omogućiti offline način rada** — osim jednostavnog preuzimanja, ovo kontinuirano prati mapu za nove datoteke i automatski ih preuzima kako se pojavljuju online.
- **Preuzeti** — preuzmite sve sadržaje mape na uređaj za offline pristup.
- **Preimenovati / Premjesti** — preimenujte ili premjestite mapu na udaljenoj pohrani.
- **Dodaj u arhivu** — spakujte sadržaj mape u ZIP datoteku (Premium značajka).
- **Izbrisati** — trajno uklonite mapu i njezin sadržaj. **Ova radnja se ne može poništiti.**

## Red prijenosa

U gornjem desnom kutu kartice Datoteke nalazi se gumb **Prijenosi** (ikona strelica u vrtnji). Dodirnite ga za otvaranje Reda prijenosa — popis svakog aktivnog preuzimanja i prijenosa na svim izvorima, s napretkom u stvarnom vremenu, brzinom i procijenjenim vremenom dolaska po datoteci.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo red prijenosa datoteka" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Možete pauzirati, nastaviti, ponoviti neuspjele prijenose, preurediti stavke za prioritiziranje određenih preuzimanja ili ih pojednačno otkazati. Možete i podesiti brzinu reda prijenosa (maksimalan broj paralelnih zadataka), vrstu mreže (samo Wi-Fi ili Wi-Fi + Mobilna) i pozadinske prijenose u Postavke → Upravitelj datoteka.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo radnje na redu prijenosa datoteka" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Offline način rada i sinkronizirane offline mape

Offline način rada je praktična značajka koja vam omogućuje gledanje omiljenih videozapisa čak i kada niste spojeni na internet. Kada omogućite offline način rada za bilo koju mapu, popis za reproduciju, album ili žanr, sve datoteke u toj kolekciji automatski se preuzimaju na uređaj za offline reprodukciju. Pojavljuju se u odjeljku Offline mape.

Kada dodajete nove datoteke na udaljeni server, automatski se preuzimaju — tako vaša offline kolekcija ostaje aktualna bez vašeg angažmana. Za ručnu ponovnu sinkronizaciju, dodirnite tri točkice u gornjem desnom kutu offline mape i odaberite Sinkronizirati.

Možete podesiti vremenski interval sinkronizacije u Postavke → Upravitelj datoteka → Sinkronizirani offline mape → Vremenski interval.

Detaljne upute dostupne su [ovdje](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personalizacija

U Postavke → Personalizacija možete konfigurirati kako se kartica Datoteke prikazuje:

- **Stil zaslona datoteka** — Obični izbornik (prikazuje popis mapa izravno) ili Grupirani izbornik (grupira sadržaj po kategoriji — Brzi pristup, Posebne mape, Pohrana u oblaku, itd.).
