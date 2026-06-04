---
title: "Povezivanja"
date: 2020-01-01
description: "Naučite kako spojiti oblak usluge, računala, NAS uređaje i upravljati glazbenim datotekama koristeći Evermusic. Vodič korak po korak za Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes File Sharing i više."
keywords: [
  "Evermusic", "cloud music player", "NAS streaming", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes File Sharing",
  "connect cloud storage", "music transfer iPhone", "file manager iOS"
]
tags: ["evermusic", "guide", "connections"]
readingTime: 11
---


Na zaslonu Povezivanja možete spojiti svaki izvor koji drži vašu glazbu — popularne oblak usluge, samohostane medijske poslužitelje, vaš Mac ili PC, osobni NAS, Apple Time Capsule, WD My Cloud Home, pa čak i USB flash pogon — i koristiti ih sve iz jednog jedinstvenog sučelja. Povezivanja su i mjesto gdje postavljate Brzi pristup do duboko ugniježđenih oblak mapa i gdje autentificirate Last.fm za scrobbling.

Zaslon je podijeljen na jasno označene odjeljke tako da skalira od jednog iCloud Drive računa do biblioteke raširene na više oblaka i NAS uređaja: Brzi pristup na vrhu (vaše omiljene oblak mape), Pohrana u oblaku (dodani računi), Lokalna mreža (Bonjour-otkriveni uređaji), Računalo (Wi-Fi Drive, iTunes File Sharing, SMB), Vanjski dodaci (spojeni USB flash pogoni) i Ostale usluge (Last.fm i slično).

{{< cards cols="1">}}
  {{< card title="" subtitle="Zaslon Evermusic Povezivanja" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Spoji se na pohranu u oblaku

- Otvorite karticu Povezivanja.
- Odaberite Spoji se na pohranu u oblaku iz izbornika.
- Odaberite uslugu pohrane u oblaku s popisa.
- Prijavite se na službenu stranicu autorizacije pružatelja (Evermusic nikada ne vidi vašu lozinku).
- Dodirnite Završeno.

{{< cards cols="1">}}
  {{< card title="" subtitle="Odabir pružatelja pohrane u oblaku" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Ako naiđete na probleme, provjerite internetsku vezu i vjerodajnice za prijavu te provjerite je li dvofaktorska autentifikacija ispravno konfigurirana za tu uslugu.
U Premium verziji aplikacije možete dodati neograničen broj usluga. Besplatni korisnici mogu spojiti jedan oblak račun odjednom.

## Podržane usluge pohrane u oblaku

Evermusic podržava cijeli niz popularnih oblak i samohostanih usluga. Besplatni korisnici dobivaju isti katalog pružatelja, ali s ograničenjem jednog računa; Premium otključava neograničene račune i uklanja većinu ostalih ograničenja.

- **Osobni oblak računi:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Samohostani poslužitelji i medijske biblioteke:** Plex · Jellyfin · Emby · Subsonic (i svaki Subsonic-kompatibilni poslužitelj — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (i Owncloud, putem dijeljenog API-ja) · Synology Drive · QNAP.
- **NAS i protokoli za dijeljenje datoteka:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (lozinka ili autentifikacija javnim ključem), NFS i DLNA (samo za čitanje — reprodukcija i preuzimanje).
- **S3-kompatibilna pohrana objekata:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage ili bilo koja S3-API krajnja točka.
- **Otkrivanje lokalne mreže:** odjeljak Dostupni uređaji automatski popisuje svaki uređaj na vašem Wi-Fiju koji se oglašava putem Bonjour / mDNS — Plex, Jellyfin, Emby poslužitelje, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, AirPort usmjernike s pričvršćenim pogonima itd.

## Sigurnost i privatnost

Koristimo samo službeni SDK i sigurnu vezu za interakciju s povezanim oblak uslugama. Vaša prijava i lozinka nisu dostupni aplikaciji. Svi zahtjevi iz aplikacije prema oblak usluzi su šifrirani.

Kada unesete svoju prijavu i lozinku, aplikacija vam prikazuje službenu stranicu autorizacije koju pruža davatelj oblak usluge i cijeli postupak autorizacije odvija se izvan aplikacije. Davatelj oblak usluge šalje auth token aplikaciji nakon uspješne autorizacije i taj token se koristi za API pozive.

Auth-token je digitalni ključ koji trećim aplikacijama omogućuje interakciju s pohranom u oblaku. Auth-token je pohranjen na vašem uređaju u sigurnoj sustavnoj pohrani nazvanoj Keychain. Možete preuzeti datoteke s povezane oblak usluge na uređaj i te datoteke bit će smještene u direktoriju "Documents" aplikacije. Možete ukloniti te datoteke u bilo kojem trenutku koristeći ugrađeni upravitelj datoteka.

Aplikacija ne dijeli nikakve informacije s povezanog oblak računa. Pristup svom oblak računu možete opozvati u bilo kojem trenutku otvaranjem stranice postavki računa u web pregledniku.

## Odbijanje auth-tokena

Prijavite se na račun u web pregjedniku i idite na stranicu postavki. Tamo možete pronaći sve aplikacije trećih strana koje su spojene na vaš oblak račun i ukloniti bilo koju od njih ako više ne želite koristiti tu aplikaciju. Detaljne upute dostupne su [ovdje](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Možete i odspojiti spojene oblak račune u aplikaciji i auth token će biti uklonjen s vašeg uređaja. Ako uklonite aplikaciju s uređaja, svi preuzeti podaci i pristupni tokeni bit će također uklonjeni.

## Odspojite pohranu u oblaku ili promijenite konfiguraciju

- Pristupite opcijama pohrane u oblaku: prvo pronađite pohranu u oblaku koju želite upravljati unutar sučelja aplikacije.
- Dodirnite gumb '...': pored naziva usluge vidjet ćete gumb '...'. Dodirnite ga za pristup dodatnim opcijama.
  - **Preimen**: ako želite promijeniti naziv oblak usluge kako se pojavljuje na popisu, odaberite 'Preimenuj'.
  - **Postavke**: za izmjenu konfiguracije ili podataka za autentifikaciju oblak usluge, odaberite 'Postavke'. Ponekad ćete morati ponovo autorizirati spojenu oblak uslugu ako je autorizacijski token istekao.
  - **Odspojiti**: ako želite potpuno prekinuti vezu između aplikacije i oblak usluge, odaberite 'Odspoji'. Imajte na umu da će odabirom ove opcije sve pjesme vezane uz ovu oblak uslugu biti uklonjene iz glazbene biblioteke aplikacije, ali ostat će na poslužitelju.

{{< cards cols="1">}}
  {{< card title="" subtitle="Izbornik više radnji spojene pohrane u oblaku" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Spoji se na računalo ili NAS

Možete i spojiti računalo, osobni NAS ili druge mrežne uređaje koristeći SMB, DLNA ili WebDAV protokol.

## Spoji se na računalo koristeći SMB

- Dodirnite "Spoji se na pohranu u oblaku" → SMB.
- Unesite IP adresu računala i naziv dijeljene mape u polje URL u formatu smb://computer-ip-address/shared-folder-name
- Odaberite verziju protokola: Auto, SMB1, SMB2
- Unesite prijavu i lozinku (ako je potrebno)
- Dodirnite "Završeno".

Ako je veza uspješna, vidjet ćete spojenu pohranu u odjeljku "Pohrana u oblaku".
Potpuni vodič o tome kako spojiti MAC ili PC koristeći SMB dostupan je [ovdje](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Postavke SMB veze" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Spoji se na NAS koristeći WebDAV

Svi koraci su isti, osim polja URL.
URL treba biti u formatu http://server-name, ili https://server-name ako poslužitelj podržava SSL.
Potpuni vodič o tome kako spojiti NAS koristeći WebDAV protokol dostupan je [ovdje](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Postavke WebDAV veze" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Spoji se na računalo ili NAS koristeći DLNA

Možete i dijeliti glazbenu biblioteku smještenu na vašem Windows PC-u ili osobnom NAS-u koristeći DLNA protokol i pristupiti toj biblioteci u aplikaciji kao što je opisano [ovdje](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA je popularan i široko korišten protokol, ali vam omogućuje samo reprodukciju ili preuzimanje glazbe. Ne možete uploadati datoteke ili kreirati nove mape na poslužitelju.

{{< cards cols="1">}}
  {{< card title="" subtitle="Postavke DLNA veze" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Dostupni uređaji

Ovaj odjeljak prikazuje sve uređaje unutar vaše lokalne mreže s kojima se možete spojiti putem aplikacije.
Za uspostavljanje veze s uređajem, slijedite ove korake:

- Otvorite aplikaciju i idite na odjeljak "Dostupni uređaji".
- Dodirnite uređaj s kojim se želite spojiti s popisa.
- Ako je potrebno, unesite podatke za prijavu za dovršetak veze.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dostupni uređaji na lokalnoj mreži" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive je zgodna tehnologija koja omogućuje bežični prijenos datoteka s računala na vaš iOS uređaj putem desktop preglednika.
Za učinkovito korištenje ove značajke, provjerite jesu li vaš uređaj i računalo spojeni na istu Wi-Fi mrežu.
Evo vodiča korak po korak o tome kako koristiti Wi-Fi Drive.

## Omogućite Wi-Fi Drive

- Otvorite aplikaciju i idite na karticu "Povezivanja".
- Odaberite "Spoji se putem Wi-Fija" za pristup glavnom zaslonu Wi-Fi Drive.
- Dodirnite "Pokreni Wi-Fi Drive" za omogućivanje Wi-Fi Drive.

## Pristupite Wi-Fi Drive na računalu

- Na računalu (stolnom ili prijenosnom), otvorite web preglednik (kao Chrome, Firefox ili Safari).
- U adresnoj traci preglednika unesite URL koji pruža aplikacija.

## Bežično prenosite datoteke

Kada se web stranica koja odgovara vašem iOS uređaju otvori u pregledniku, možete lako povući i ispustiti datoteke s računala na web stranicu.
Datoteke koje povučete i ispustite počet će se prenositi na vaš iOS uređaj i bit će dostupne unutar aplikacije.

{{< cards cols="1">}}
  {{< card title="" subtitle="Postavke Wi-Fi Drive poslužitelja" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Detaljne upute o bežičnom prijenosu datoteka koristeći WiFi-Drive dostupne su [ovdje](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing je druga tehnologija koja vam omogućuje prijenos datoteka s računala na uređaj koristeći aplikaciju Finder na Macu i lightning kabel.
- Samo spojite uređaj na računalo koristeći kabel i pokrenite aplikaciju Finder na Macu.
- Otvorite "Locations" → "Vaš spojeni uređaj" → "Files" → i pronađite aplikaciju Evermusic.
- Dodirnite ikonu aplikacije za prikaz svih dijeljenih mapa.
- Kopirajte datoteke s računala u dijeljenu mapu na uređaju koristeći povuci i ispusti.

Detaljne upute o korištenju iTunes file sharinga dostupne su [ovdje](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder File Sharing na Macu" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Spojite USB flash karticu

Ako imate SD karticu, možete je spojiti koristeći lightning čitač kartica. Aplikacija trenutno podržava Apple Certified čitače kartica i iXpand Flash Drives. Ako imate iXpand Flash Drive - umetnite ga u lightning priključak i otvorite aplikaciju. Vidjet ćete poruku "Vanjski uređaj spojen" i informacije o uređaju. Jednostavno dodirnite ikonu flash pogona za pristup glazbenoj mapi i dodirnite bilo koju audio datoteku za pokretanje reprodukcije. Imamo detaljne upute o tome kako spojiti USB flash karticu na iPhone i slušati glazbu ili upravljati datotekama na njoj koje su dostupne [ovdje](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Upravitelj datoteka

Kada spojite uslugu pohrane u oblaku, dodirnite njenu ikonu za prikaz svih dostupnih datoteka i mapa. Možete koristiti ugrađeni upravitelj datoteka za rad s tim datotekama — preuzimanje, preimenovanje, premještanje i više. Kada pokrenete preuzimanje, datoteka će se pojaviti u redu prijenosa. Za prikaz reda prijenosa, idite na karticu "Lokalne datoteke" i dodirnite rotirajuće strelice u gornjem lijevom kutu. Sve preuzete datoteke i mape dostupne su u odjeljku "Lokalne datoteke".

## Gornja alatna traka

Gornja alatna traka, smještena ispod navigacijske trake, nudi nekoliko korisnih radnji za lak pristup. Ovu alatnu traku možete prikazati ili sakriti jednostavnim gestom povlačenja prema dolje. Evo dostupnih radnji:

- **Pretraži**: Ova opcija vam omogućuje brzo pretraživanje unutar trenutnog direktorija, što olakšava pronalaženje određenih datoteka ili mapa.
- **Nastavi reprodukciju**: Ako je omogućeno u postavkama aplikacije, ova značajka vraća red audio reproduktora i posljednju medijsku poziciju za trenutnu mapu. Zgodan je način za nastavak od mjesta gdje ste stali u glazbenoj biblioteci.
- **Reproduciraj sve**: Odabirom ove radnje, aplikacija će skenirati trenutnu mapu i njene podmape, dodajući sve pronađene audio datoteke u novi red reproduktora. Ovo je korisno kada želite reproducirati svu glazbu unutar određenog direktorija.
- **Izmiješaj sve**: Slično "Reproduciraj sve", ova radnja skenira trenutnu mapu i njene podmape ali miješa datoteke prije dodavanja u red audio reproduktora. Odličan je način za uživanje u glazbi slučajnim redoslijedom.

{{< cards cols="1">}}
  {{< card title="" subtitle="Gornja alatna traka unutar oblak mape" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Opcije mape

Kada otvorite mapu unutar aplikacije, pronaći ćete prikladni skup radnji dostupnih dodirivanjem gumba "..." u gornjem desnom kutu zaslona.
Evo pregleda tih radnji:

- **Odabrati**: Aktivirajte način odabira datoteka. Ovaj način vam omogućuje odabir jedne ili više datoteka unutar mape, što olakšava izvođenje radnji na odabranim stavkama.
- **Nova mapa**: Kreirajte novu mapu unutar trenutne mape. Ova značajka vam omogućuje organiziranje datoteka i održavanje biblioteke strukturiranom.
- **Omogućiti offline način rada**: Uključite offline način rada za trenutnu mapu. Offline način rada ide dalje od jednostavnog preuzimanja; aktivno prati mapu za promjene. Ako dodate nove datoteke u mapu online, aplikacija će automatski preuzeti te datoteke na uređaj. Time se osigurava da vaša lokalna biblioteka ostaje ažurna s promjenama na poslužitelju.
- **Uploadi datoteke**: Uploadajte datoteke s uređaja u online mapu. Ova radnja vam omogućuje prijenos datoteka u oblak ili na poslužitelj, čineći ih dostupnima s bilo kojeg mjesta.
- **Pretraži**: Pretražite određene datoteke unutar trenutne mape. Ovo je posebno korisno za brzo pronalaženje određenih stavki u velikoj kolekciji.
- **Sortiraj**: Sortirajte datoteke unutar mape prema kriterijima kao što su naziv, veličina ili datum uređivanja. Zadani način sortiranja obično odražava redosljed sortiranja na poslužitelju, ali možete ga promijeniti prema svojoj preferenciji.
- **Prikaz mreže/popisa**: Prebacujte između dva načina prikaza: tablični prikaz i prikaz minijatura. Tablični prikaz prikazuje datoteke u popisu, dok prikaz minijatura prikazuje vizualne prikaze datoteka, što olakšava prepoznavanje sadržaja na prvi pogled.

{{< cards cols="1">}}
  {{< card title="" subtitle="Izbornik više radnji trenutne mape" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Uredite online datoteke

Kada trebate upravljati više datotekama unutar pohrane u oblaku na Evermusicu, možete koristiti način odabira za pojednostavljivanje radnji. Slijedite ove korake za učinkovito upravljanje datotekama:

- **Aktivirajte način odabira**: Otvorite aplikaciju na uređaju i navigirajte do odjeljka koji sadrži pohranu u oblaku. Potražite "..." (tri točke) gumb u gornjem desnom kutu. Dodirnite ga i odaberite "Odaberi" stavku izbornika za aktiviranje načina odabira.
- **Odaberite datoteke**: Vidjet ćete potvrdne okvire koji se pojavljuju pored svake datoteke ili mape na popisu. Odaberite jednu ili više datoteka ili mapa jednostavnim dodirivanjem potvrdnih okvira pored njih.
- **Izvršite različite radnje**: Kada odaberete datoteke ili mape kojima želite upravljati, imat ćete pristup nekoliko radnji prilagođenih vašim potrebama:

{{< cards cols="1">}}
  {{< card title="" subtitle="Način odabira za online datoteke" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Radnje datoteke

Pored naslova datoteke, vidjet ćete simbol elipse "..." (tri točke) — ovo je izbornik radnji.
Dodirnite ga za prikaz popisa dostupnih radnji:

- **Reproduciraj sljedeće**: Odaberite ovu radnju za umetanje odabrane datoteke na vrh reda reproduktora, osiguravajući da se reproducira odmah nakon trenutne stavke.
- **Reproduciraj kasnije**: Odabirom ove opcije dodaje se datoteka na dno reda reproduktora, osiguravajući da se reproducira nakon postojećeg reda.
- **Dodaj u glazbenu biblioteku**: Ova radnja vam omogućuje uključivanje datoteke u glazbenu biblioteku, čineći je lako dostupnom i uredno organiziranom prema izvođaču, albumu, žanru ili skladatelju.
- **Dodaj na popis pjesama**: Koristite ovu radnju za dodavanje datoteke na postojeći popis pjesama ili kreiranje novog.
- **Urediti audio oznake**: Odabirom ove opcije možete pristupiti ugrađenom uređivaču oznaka u Evermusicu, što vam omogućuje izmjenu audio oznaka za odabranu datoteku. Datoteka će biti privremeno preuzeta u privremeni direktorij, a zatim uploadana na pohranu nakon potvrde promjena.
- **Dodaj u omiljene**: Ova radnja dodaje datoteku na popis omiljenih datoteka za brz i prikladan pristup.
- **Preuzeti**: Odaberite ovu radnju za preuzimanje datoteke ili mape na uređaj, čineći je dostupnom za offline korištenje.
- **Preimenuj**: Ova opcija vam dopušta preimenovanje datoteke izravno na udaljenoj pohrani.
- **Premjesti**: Odaberite ovu radnju za premještanje datoteke u drugu mapu unutar pohrane u oblaku, pomažući u održavanju organizirane strukture datoteka.
- **Otvori u**: Koristite ovu radnju za izvoz datoteke u drugu kompatibilnu aplikaciju. Datoteka će biti preuzeta na uređaj, a zatim će se pojaviti dijaloški okvir za dijeljenje.
- **Izbrisati**: Budite oprezni s ovom radnjom, jer trajno uklanja datoteku iz pohrane u oblaku. Ovo brisanje se ne može poništiti.

{{< cards cols="1">}}
  {{< card title="" subtitle="Izbornik više radnji za jednu datoteku" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Ako popis radnji premašuje dostupni prostor na zaslonu, jednostavno se pomaknite prema dolje unutar izbornika radnji za pristup dodatnim opcijama.

## Radnje mape

Za svaku mapu u pohrani u oblaku dostupne su različite radnje. Za pristup tim opcijama, jednostavno dodirnite ikonu elipse "..." koja se nalazi pored naslova mape. Ako ne vidite sve radnje, pomaknite se prema dolje za prikaz više izbora. Evo dostupnih radnji:

- **Reproduciraj sve**: Zamijenite trenutni red reproduktora svim stavkama iz odabrane mape.
- **Reproduciraj sljedeće**: Dodajte cijelu mapu na vrh reda reproduktora, odmah nakon trenutno reproducirane stavke.
- **Reproduciraj kasnije**: Dodajte sadržaj mape na dno reda reproduktora.
- **Dodaj u glazbenu biblioteku**: Ova radnja besprijekorno uključuje sadržaj mape u vašu glazbenu biblioteku, čineći je lako dostupnom i uredno organiziranom prema izvođaču, albumu, žanru ili skladatelju.
- **Dodaj na popis pjesama**: Možete uključiti cijelu mapu na popis pjesama. Imate i opciju kreiranja novog popisa pjesama, a naziv mape bit će automatski dodijeljen.
- **Dodaj u omiljene**: Koristite ovu radnju za dodavanje mape na popis omiljenih datoteka za brz i prikladan pristup.
- **Omogućiti offline način rada**: Omogućavanjem offline načina rada za odabranu mapu, aplikacija ide dalje od jednostavnog preuzimanja. Kontinuirano skenira promjene, i ako se dodaju nove datoteke u online mapu, automatski će biti preuzete u aplikaciju.
- **Preuzeti**: Preuzmite sav sadržaj mape na uređaj za offline pristup.
- **Preimenuj**: Preimenujte mapu izravno na udaljenoj pohrani.
- **Premjesti**: Premjestite mapu na drugo mjesto unutar pohrane u oblaku.
- **Izbrisati**: Budite oprezni s ovom radnjom jer trajno uklanja mapu i njen sadržaj iz pohrane u oblaku. Ova radnja se ne može poništiti.


## Brzi pristup

Odjeljak Brzi pristup nalazi se na vrhu zaslona. Daje vam brz pristup omiljenim i nedavno otvorenim datotekama s povezanih oblak usluga.
Kad god otvorite datoteku ili mapu iz oblaka, dodaje se na popis "Nedavno otvoreno". Za brisanje tog popisa, otvorite "Nedavne", dodirnite gumb "Više radnji" i odaberite "Izbriši popis". Možete i označiti duboko ugniježđene mape kao Omiljene za brz pristup bez kopanja kroz strukturu direktorija.

## Ostale usluge

Ovaj odjeljak prikazuje dodatne značajke koje poboljšavaju vaše iskustvo. Trenutno aplikacija podržava Last.fm scrobbling. Kada ste spojeni, vaše statistike reprodukcije automatski se šalju na vaš Last.fm račun. Možete posjetiti vaš Last.fm profil kasnije za prikaz analitike slušanja i dobivanje personaliziranih preporuka glazbe. Detaljne upute za postavljanje dostupne su [ovdje](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
