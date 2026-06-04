---
title: "Povezivanja"
date: 2020-02-01
description: "Naučite kako povezati pohranu u oblaku, NAS i računalo s Evertagom. Pristupajte i uređujte audio datoteke izravno iz pohrane u oblaku, osobnog NAS-a ili Mac/PC računala."
keywords: [
  "Evertag postavljanje oblaka", "povezivanje iClouda s Evertagom", "SMB pristup datotekama iOS",
  "WebDAV uređivač audio oznaka", "uređivanje metapodataka NAS", "Wi-Fi Drive Evertag",
  "prijenos audio datoteka na iPhone", "Evertag iTunes File Sharing", "uređivanje FLAC oznaka iz oblaka"
]
tags: ["vodič", "evertag", "povezivanja"]
readingTime: 11
---


Na ovom zaslonu možete povezati razne izvore koji sadrže vaše audio datoteke. Možete integrirati popularne usluge oblaka kao što su Google Drive, Dropbox, OneDrive, iCloud i druge, kao i povezati Mac ili PC. Osim toga, imate mogućnost uređivanja audio datoteka smještenih u Apple Time Capsule, WD Cloud Home ili bilo koji NAS koji govori SMB ili WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Zaslon Povezivanja u Evertagu" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Brzi pristup

Na vrhu zaslona Povezivanja naći ćete popis **Brzi pristup**. Svaka mapa u oblaku koju dodate u omiljene — čak i ona zakopana nekoliko razina duboko — pojavljuje se ovdje kako biste do nje mogli skočiti bez navigiranja kroz nadređene mape svaki put.

## Povezivanje s pohranom u oblaku

- Otvorite karticu 'Povezivanja'
- Odaberite 'Poveži s pohranom u oblaku' iz izbornika
- Odaberite uslugu pohrane u oblaku s popisa
- Unesite svoje vjerodajnice i tapnite 'Gotovo.'

Ako naiđete na probleme, svakako provjerite internetsku vezu i korisničko ime/lozinku.
U Premium verziji aplikacije možete dodati neograničen broj usluga.

## Podržane usluge pohrane u oblaku

Trenutno aplikacija podržava najpopularnije usluge pohrane u oblaku: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), kao i bilo koji SMB ili WebDAV poslužitelj.

## Sigurnost i privatnost

Koristimo samo službene SDK-ove i sigurne veze za interakciju s povezanim uslugama oblaka. Vaše korisničko ime i lozinka nisu dostupni aplikaciji. Svi zahtjevi iz aplikacije prema usluzi oblaka su šifrirani.

Kada unesete korisničko ime i lozinku, aplikacija vam prikazuje službenu stranicu autorizacije koju pruža davatelj usluge oblaka, a cijeli proces autorizacije odvija se izvan aplikacije. Davatelj usluge oblaka šalje auth token aplikaciji nakon uspješne autorizacije, i taj token se koristi za API pozive.

Auth token je digitalni ključ koji omogućuje aplikacijama trećih strana interakciju s pohranom u oblaku. Auth token se pohranjuje na vašem uređaju u sigurnoj sistemskoj pohrani zvanoj Keychain. Možete preuzeti datoteke s povezane usluge oblaka na uređaj, i te datoteke će biti smještene u direktorij "Documents" aplikacije. Možete ukloniti te datoteke u bilo kojem trenutku koristeći ugrađeni upravitelj datoteka.

Aplikacija ne dijeli nikakve informacije s povezanog računa u oblaku. Možete opozvati pristup svom računu u oblaku u bilo koje vrijeme otvaranjem stranice postavki računa u web pregledniku.

## Opoziv auth tokena

Prijavite se na račun u web pregledniku i idite na stranicu postavki. Tamo možete pronaći sve aplikacije trećih strana koje su povezane s vašim računom u oblaku i ukloniti bilo koju od njih ako je više ne želite koristiti. Detaljne upute dostupne su [ovdje](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Također možete odspojiti povezane račune u oblaku u aplikaciji, i auth token će također biti uklonjen s vašeg uređaja. Ako uklonite aplikaciju s uređaja, svi preuzeti podaci i access tokeni će također biti uklonjeni.

## Odspajanje pohrane u oblaku ili promjena konfiguracije

- Pristup opcijama pohrane u oblaku: Prvo pronađite pohranu u oblaku kojom želite upravljati unutar sučelja aplikacije.
- Tapnite gumb '...': Pored naziva usluge vidjet ćete gumb '...'. Tapnite ga za pristup dodatnim opcijama.
  - **Preimenovanje**: Ako želite promijeniti naziv usluge oblaka kako se prikazuje na vašem popisu, odaberite 'Preimenuj.'
  - **Postavke**: Za izmjenu konfiguracije ili podataka za autentifikaciju usluge oblaka, odaberite 'Postavke.' Ponekad ćete morati ponovo autorizirati povezanu uslugu oblaka ako je autorizacijski token istekao.
  - **Odspoji**: Ako želite u potpunosti prekinuti vezu između aplikacije i usluge oblaka, odaberite 'Odspoji.' Imajte na umu da će odabirom ove opcije biti uklonjene sve pjesme povezane s ovom uslugom oblaka iz glazbene biblioteke aplikacije, ali će ostati na poslužitelju.

## Povezivanje s računalom ili NAS-om

Možete također povezati računalo, osobni NAS ili druge mrežne uređaje koristeći SMB, DLNA ili WebDAV protokol.

## Povezivanje s računalom putem SMB-a

- Tapnite "Poveži s pohranom u oblaku" → SMB.
- Unesite IP adresu računala i naziv dijeljene mape u polje URL koristeći format smb://computer-ip-address/shared-folder-name
- Odaberite verziju protokola: Auto, SMB1, SMB2
- Unesite korisničko ime i lozinku (ako je potrebno)
- Tapnite "Gotovo."

Ako je veza uspješna, vidjet ćete povezanu pohranu u odjeljku "Pohrana u oblaku."
Puni vodič za povezivanje Mac-a ili PC-a putem SMB-a dostupan je [ovdje](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Povezivanje s NAS-om putem WebDAV-a

Svi koraci su isti osim polja URL.
URL bi trebao biti u formatu http://server-name, ili https://server-name ako poslužitelj podržava SSL.
Puni vodič za povezivanje NAS-a koristeći WebDAV protokol dostupan je [ovdje](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Dostupni uređaji

Ovaj odjeljak prikazuje sve uređaje unutar vaše lokalne mreže s kojima se možete povezati putem aplikacije.
Za uspostavljanje veze s uređajem, slijedite ove korake:

- Otvorite aplikaciju i idite na odjeljak "Dostupni uređaji."
- Tapnite uređaj s kojim se želite povezati s popisa.
- Ako je potrebno, unesite podatke za prijavu za dovršetak veze.

## Wi-Fi Drive

Wi-Fi Drive je zgodna tehnologija koja omogućuje bežični prijenos datoteka s računala na iOS uređaj putem desktop preglednika.
Za učinkovito korištenje ove funkcije, osigurajte da su vaš uređaj i računalo spojeni na istu Wi-Fi mrežu.
Evo vodiča korak po korak za korištenje Wi-Fi Drive-a.

## Omogući Wi-Fi Drive

- Otvorite aplikaciju i idite na karticu "Povezivanja."
- Odaberite "Poveži putem Wi-Fi-ja" za pristup glavnom zaslonu Wi-Fi Drive-a.
- Tapnite "Pokreni Wi-Fi Drive" za omogućavanje Wi-Fi Drive-a.

## Pristup Wi-Fi Drive-u na računalu

- Na računalu (desktop ili prijenosnom), otvorite web preglednik (kao što su Chrome, Firefox ili Safari).
- U adresnoj traci preglednika, unesite URL koji pruža aplikacija.

## Bežični prijenos datoteka

Kada se web stranica odgovarajuća vašem iOS uređaju otvori u pregledniku, možete lako povući i ispustiti datoteke s računala na web stranicu.
Datoteke koje povučete i ispustite počet će se prenositi na vaš iOS uređaj i bit će dostupne unutar aplikacije.

Detaljne upute za bežični prijenos datoteka koristeći Wi-Fi Drive dostupne su [ovdje](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing je još jedna tehnologija koja vam omogućuje prijenos datoteka s računala na uređaj koristeći aplikaciju Finder na Macu i Lightning kabel.
- Samo spojite uređaj na računalo kabelom i pokrenite aplikaciju Finder na Macu.
- Otvorite "Lokacije" → "Vaš spojeni uređaj" → "Datoteke" → i pronađite trenutnu aplikaciju.
- Tapnite ikonu aplikacije da vidite sve dijeljene mape.
- Kopirajte datoteke s računala u dijeljenu mapu na uređaju koristeći povuci i ispusti.

Detaljne upute za korištenje iTunes File Sharing dostupne su [ovdje](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Spajanje USB flash kartice

Ako imate SD karticu ili USB stick, možete je spojiti koristeći Lightning ili USB-C čitač kartica na iPhoneu/iPadu, ili je izravno priključiti na Mac. Aplikacija trenutno podržava Apple certificirane čitače kartica. Imamo detaljne upute za spajanje USB flash kartice na iPhone ili iPad i upravljanje datotekama na njoj, dostupne [ovdje](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Spojeni diskovi pojavljuju se u odjeljku **Vanjski pribor** zaslona Povezivanja.

## Upravitelj datoteka

Kada povežete uslugu pohrane u oblaku, tapnite njenu ikonu za pregled svih dostupnih datoteka i mapa. Možete koristiti ugrađeni upravitelj datoteka za rad s ovim datotekama — preuzimanje, preimenovanje, premještanje i još mnogo toga. Kada pokrenete preuzimanje, datoteka će se pojaviti u redu za prijenos. Za pregled reda za prijenos, idite na karticu "Lokalne datoteke" i tapnite rotirajuće strelice u gornjem lijevom kutu. Sve preuzete datoteke i mape dostupne su u odjeljku "Lokalne datoteke."

## Gornja alatna traka

Gornja alatna traka, zgodno smještena ispod navigacijske trake, nudi nekoliko korisnih akcija za jednostavan pristup. Možete prikazati ili sakriti ovu alatnu traku jednostavnim potezom prema dolje. Evo dostupnih akcija:

- **Pretraži**: Ova opcija vam omogućuje brzo pretraživanje unutar trenutnog direktorija, čineći pronalazak određenih datoteka ili mapa bez napora.

## Opcije mape

Kada otvorite mapu unutar aplikacije, naći ćete praktičan skup akcija dostupnih tapkanjem gumba "..." u gornjem desnom kutu zaslona.
Evo pregleda ovih akcija:

- **Odaberi**: Aktivirajte način odabira datoteka. Ovaj način vam omogućuje odabir jedne ili više datoteka unutar mape, olakšavajući izvođenje akcija na odabranim stavkama.
- **Nova mapa**: Stvorite novu mapu unutar trenutne mape. Ova funkcija vam omogućuje organiziranje datoteka i održavanje dobro strukturirane biblioteke.
- **Prenesi datoteke**: Prenesite datoteke s uređaja u online mapu. Ova akcija vam omogućuje prijenos datoteka u oblak ili na poslužitelj, čineći ih dostupnima s bilo kojeg mjesta.
- **Pretraži**: Pretražite određene datoteke unutar trenutne mape. Ovo je posebno korisno za brzo pronalaženje određenih stavki u velikoj kolekciji.
- **Sortiraj**: Sortirajte datoteke unutar mape prema kriterijima kao što su naziv, veličina ili datum izmjene. Zadani način sortiranja obično odražava redoslijed sortiranja na poslužitelju, ali ga možete promijeniti prema vlastitim preferencijama.
- **Rešetkasti/Listovni prikaz**: Prebacite između dva načina prikaza: tabličnog prikaza i prikaza s minijaturama. Tablični prikaz prikazuje datoteke u listi, dok prikaz s minijaturama prikazuje vizualne reprezentacije datoteka, olakšavajući prepoznavanje sadržaja na prvi pogled.

{{< cards cols="1">}}
  {{< card title="" subtitle="Sortiranje mape u oblaku u Evertagu" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Uređivanje online datoteka

Kada trebate upravljati više datotekama unutar pohrane u oblaku u ovoj aplikaciji, možete koristiti način odabira za pojednostavljivanje akcija. Slijedite ove korake za učinkovito upravljanje datotekama:

- **Aktivirajte način odabira**: Otvorite aplikaciju na uređaju i idite u odjeljak koji sadrži pohranu u oblaku. Potražite gornji desni kut gdje ćete naći gumb "..." (tri točke). Tapnite ga i odaberite stavku izbornika "Odaberi" za aktiviranje načina odabira.
- **Odaberite datoteke**: Primijetit ćete pojavu potvrdnih okvira pored svake datoteke ili mape navedene na popisu. Odaberite jednu ili više datoteka ili mapa jednostavnim tapkanjem potvrdnih okvira pored njih.
- **Izvršite razne akcije**: Kada odaberete datoteke ili mape kojima želite upravljati, imat ćete pristup nekoliko akcija prilagođenih vašim potrebama:

{{< cards cols="1">}}
  {{< card title="" subtitle="Odabir datoteka u Evertagu" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Akcije s datotekama

Pored naziva datoteke, primijetit ćete simbol tri točke "..." — ovo služi kao izbornik akcija.
Tapnite ga za prikaz liste dostupnih akcija:

- **Uredi audio oznake**: Odabirom ove opcije možete pristupiti ugrađenom uređivaču oznaka, što vam omogućuje izmjenu audio oznaka za odabranu datoteku. Datoteka će biti privremeno preuzeta u privremeni direktorij, a zatim prenesena na pohranu nakon što potvrdite promjene.
- **Dodaj u omiljene**: Ova akcija dodaje datoteku na popis omiljenih datoteka za brz i praktičan pristup.
- **Preuzmi**: Odaberite ovu akciju za preuzimanje datoteke ili mape na uređaj, čineći je dostupnom za korištenje bez interneta.
- **Preimenuj**: Ova opcija vam omogućuje preimenovanje datoteke izravno na udaljenoj pohrani, dopuštajući prilagođeno imenovanje datoteka.
- **Premjesti**: Odaberite ovu akciju za premještanje datoteke u drugu mapu unutar pohrane u oblaku, pomažući u održavanju organizirane strukture datoteka.
- **Otvori u**: Koristite ovu akciju za izvoz datoteke u drugu kompatibilnu aplikaciju. Datoteka će biti preuzeta na uređaj, a zatim će se pojaviti dijaloški okvir za dijeljenje za daljnje dijeljenje ili interakciju.
- **Izbriši**: Budite oprezni s ovom akcijom, jer trajno uklanja datoteku iz pohrane u oblaku. **Ovo brisanje se ne može poništiti**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Opcije datoteke u Evertagu" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Ako lista akcija prelazi dostupni prostor zaslona, jednostavno se pomaknite prema dolje unutar izbornika akcija za pristup dodatnim opcijama.

## Akcije s mapama

Za svaku mapu u pohrani u oblaku, imate različite dostupne akcije. Za pristup tim opcijama, jednostavno tapnite ikonu tri točke "..." smještenu pored naziva mape. Ako ne vidite sve akcije, pomaknite se prema dolje za prikaz više opcija. Evo dostupnih akcija:

- **Dodaj u omiljene**: Koristite ovu akciju za dodavanje mape na popis omiljenih datoteka za brz i praktičan pristup.
- **Preuzmi**: Preuzmite sav sadržaj mape na uređaj za pristup bez interneta.
- **Preimenuj**: Preimenujte mapu izravno na udaljenoj pohrani.
- **Premjesti**: Premjestite mapu na drugu lokaciju unutar pohrane u oblaku.
- **Izbriši**: Budite oprezni s ovom akcijom, jer trajno uklanja mapu i njezin sadržaj iz pohrane u oblaku. **Ova akcija se ne može poništiti**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Opcije mape u Evertagu" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
