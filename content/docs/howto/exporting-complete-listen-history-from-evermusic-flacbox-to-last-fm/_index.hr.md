---
title: "Izvezite svoju kompletnu povijest slušanja iz Evermusica i Flacboxa na Last.fm"
date: 2024-01-30
description: "Saznajte kako izvesti svoju povijest glazbe iz Evermusica i Flacboxa te je prenijeti na Last.fm koristeći CSV datoteke i alat Last.fm Scrubbler za Windows."
keywords: ["evermusic", "flacbox", "lastfm", "povijest glazbe", "scrobbling", "izvoz pjesama", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "nedavne", "lastfm", "izvoz", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Sažetak:** Izvezite svoju povijest slušanja iz Evermusica ili Flacboxa kao CSV datoteku, zatim je prenesite na Last.fm koristeći besplatni alat Last.fm-Scrubbler-WPF na Windowsu. Automatsko scrobblanje također je izvorno dostupno u obje aplikacije.

**Ažuriranje:** Automatsko scrobblanje je sada dostupno! Saznajte više ovdje: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobblanje je jednostavan način automatskog spremanja osnovnih detalja poput naslova i izvođača pjesme koju trenutno slušate u online uslugu. Kasnije možete pregledati svoju povijest slušanja.

[Last.fm](https://www.last.fm/home), pokretan sustavom za preporuku glazbe zvanim Audioscrobbler, nudi ovu uslugu besplatno. Stvara detaljan profil vašeg glazbenog ukusa bilježenjem pjesama koje slušate, bilo s internetskih radio stanica, vašeg računala ili raznih prijenosnih glazbenih uređaja. Možete posjetiti web stranicu kasnije kako biste primili preporuke za nove izvođače ili albume koji odgovaraju vašem glazbenom ukusu.

Možete prenijeti svoju povijest slušanja na [Last.fm](http://Last.fm) iz aplikacija Evermusic i Flacbox koristeći besplatni alat, a mi ćemo vas provesti kroz postupak.

Otvorite odjeljak 'Glazbena knjižnica' aplikacije i pomaknite se do odjeljka 'Brzi pristup'. Dodirnite stavku izbornika 'Nedavne'.

![zaslon glazbene knjižnice](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

Na zaslonu 'Nedavne' dodirnite gumb 'Više' u gornjem desnom kutu kako biste aktivirali izbornik 'Više radnji'. Dodirnite stavku izbornika 'Izvezi popis pjesama'.

![zaslon nedavnih](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

Na zaslonu 'Odaberite format datoteke' imate mogućnost odabira formata odredišne datoteke. Dostupne opcije - CSV, TXT, M3U.

![zaslon odabira formata datoteke](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Ovo označava vrijednosti odvojene zarezima, savršeno za organiziranje vaših podataka u uredan tablični format. U odredišnoj datoteci pronaći ćete parametre poput Imena izvođača, Imena albuma, Imena pjesme, Vremenskog žiga (vrijeme kada ste slušali pjesme), Imena izvođača albuma i Trajanja pjesme.

TXT: Ovdje govorimo o jednostavnoj tekstualnoj datoteci. Jednostavna je i izravna, s parametrima koji uključuju Ime izvođača, Ime albuma, Ime pjesme i Trajanje.

M3U: Ovaj format je u osnovi standard za stvaranje popisa za reprodukciju. Odličan je jer možete izvesti svoj popis pjesama i uživati u svojim pjesmama na bilo kojem uređaju, čak i ako nemate izvorne datoteke (pod uvjetom da odaberete opciju apsolutnog URL-a za medijske datoteke). U izlaznoj datoteci pronaći ćete parametre poput Trajanja, Imena izvođača, Imena pjesme i Lokacije medijske datoteke.

Za naš zadatak, odabir CSV-a je pravi put. Koristit ćemo ovu datoteku s besplatnim softverom Last.fm-Scrubbler-WPF za prijenos naše povijesti slušanja na uslugu [Last.fm](http://Last.fm). Jednostavno odaberite CSV i pritisnite gumb 'Izvezi'.

![zaslon dovršenog izvoza](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Nakon dovršetka izvoza, jednostavno dodirnite gumb 'Prikaži datoteku', i aplikacija će otkriti stvorenu datoteku u vašoj mapi dokumenata. Zatim dodirnite gumb 'Više radnji' pokraj naziva datoteke i odaberite opciju 'Otvori u' iz izbornika. Naš sljedeći korak je kopiranje izvezene datoteke na vaše stolno računalo. To možete lako učiniti odabirom opcije AirDrop iz izbornika 'Otvori u'.

![više radnji za izvezenu datoteku](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Sljedeće, koristit ćemo besplatni open-source [Last.FM](http://Last.FM) klijent koji je dostupan samo na Windows platformi. Ovaj klijent vam omogućuje učinkovito ažuriranje vaše povijesti slušanja na [Last.FM](http://Last.FM) koristeći CSV datoteku koju smo upravo izvezli.

Sada, ako trenutno ne koristite Windows računalo, ne brinite. Možete pristupiti ovom klijentu instaliranjem VirtualBoxa na vaš Mac i korištenjem službene slike Windows razvojnog okruženja.

Evo što trebate učiniti:

- Instalirajte VirtualBox s sljedećeg linka: [Preuzmi VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Preuzmite i instalirajte Windows razvojno okruženje s ovog linka: [Windows razvojno okruženje](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Na vašem Windows računalu (ili VirtualBox aplikaciji sa slikom Windows Development) preuzmite i instalirajte [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - besplatni open-source softver dostupan na GitHubu. Testirali smo verziju 1.28 koju možete preuzeti ovdje: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![stranica za preuzimanje Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

U odjeljku 'Assets' dodirnite [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) za preuzimanje instalacijskog arhiva. Raspakirajte preuzetu datoteku i otvorite raspakiranu mapu.

- VAŽNO

Ova aplikacija je još uvijek u beta fazi. Kreatori aplikacije nisu puno testirali. Preporučuju da prvo pokušate scrobblati na testni račun i vidite rade li stvari koje želite scrobblati ispravno. Posebno ako scrobblate puno pjesama odjednom. Molimo budite oprezni sa svojim računima.

Pokrenite Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Na glavnom zaslonu aplikacije, jednostavno dodirnite 'Nije prijavljen', smješten u donjem lijevom kutu, kako biste aktivirali zaslon 'Dodaj račun'.

![zaslon dodavanja računa](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Unesite svoje podatke za prijavu.

![zaslon unosa podataka za prijavu](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Dodirnite gumb 'Prijava' za dodavanje vašeg računa.

![Dodirnite gumb Prijava za dodavanje vašeg računa.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Otvorite karticu 'File Parse Scrobbler' za početak uvoza CSV datoteke iz aplikacije Evermusic.

![Otvorite karticu File Parse Scrobbler za početak uvoza CSV datoteke iz aplikacije Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Odaberite 'Parser: CSV' i dodirnite gumb 'Postavke'.

Na sljedećem zaslonu možete odabrati redoslijed parametara u vašoj CSV datoteci.

Pojedinačna polja mogu biti zatvorena u navodnike i MORAJU biti zatvorena u navodnike ako polje sadrži bilo koji od postavljenih razdjelnika. Na primjer:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Dakle ostavite sve postavke na zadanom, jedino što trebate promijeniti je omogućiti potvrdni okvir u polju 'Has Fields Enclosed In Quotes'.

Dodirnite 'Spremi i zatvori' za primjenu promjena.

![odaberite redoslijed parametara u vašoj CSV datoteci.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Scrobblanje analize datoteka ima dva načina rada. Mogu se promijeniti s padajućim izbornikom 'Scrobbling Mode'.

Normalni način: U ovom načinu, pjesme će biti scrobblane s vremenskim žigom iz analizirane scrobble. Samo scrobble novije od 14 dana mogu biti scrobblane.

Način uvoza: U ovom načinu, pjesme će biti scrobblane s vremenskim žigom izračunatim iz 'Vremena završetka' i odabranog trajanja između svake pjesme. To omogućuje scrobblanje pjesama čak i ako je vremenski žig analizirane scrobble stariji od 14 dana. Stoga će prva (najgornja) pjesma u CSV datoteci biti scrobblana s 'Vremenom završetka'.

Odaberite prethodno generiranu CSV datoteku iz aplikacije Evermusic u polju 'File:' i dodirnite 'Parse'. U nekim slučajevima možete vidjeti upozorenje o pogrešci koje kaže da neke scrobble nisu mogle biti analizirane. U redu je ako imate neke pjesme bez potpunih metapodataka poput Imena izvođača.

![neke scrobble nisu mogle biti analizirane](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Dodirnite gumb 'Odaberi sve' za odabir svih analiziranih pjesama.

![Dodirnite gumb Odaberi sve za odabir svih analiziranih pjesama.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Dodirnite gumb 'Pregled' za provjeru svih promjena koje će biti objavljene na poslužitelju.

![Dodirnite gumb Pregled za provjeru svih promjena koje će biti objavljene na poslužitelju.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Dodirnite gumb 'Scrobble' za prijenos svih promjena na poslužitelj.

![Dodirnite gumb Scrobble za prijenos svih promjena na poslužitelj.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Ranije Last.fm-Scrubbler-WPF nije imao dnevno ograničenje scrobble-ova. To se sada promijenilo jer su neki ljudi koristili Scrubbler za scrobblanje toliko mnogo pjesama da je to uzrokovalo probleme za Last.fm stranicu. Ograničenje scrobblanja trenutno je 2800 scrobble-ova dnevno. Kada pokušate scrobblati više od toga, dobit ćete poruku o pogrešci. Postoje planovi za dodavanje 'reda za scrobblanje', pa ako trebate scrobblati više od 2800 pjesama, bit će dodane u red i automatski scrobblane nakon nekog vremena. Možete provjeriti koliko vam je scrobble-ova preostalo u prikazu odabira korisnika.

Kada su svi zapisi uspješno preneseni na poslužitelj, vidjet ćete poruku na dnu prozora aplikacije koja potvrđuje: 'Odabrane pjesme uspješno scrobblane.'

![Odabrane pjesme uspješno scrobblane.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Sada možete otvoriti svoj profil na stranici [Last.fm](http://Last.fm) i provjeriti sve promjene.

![vaš profil na stranici Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Često postavljana pitanja

{{% details title="Mogu li scrobblati automatski bez izvoza CSV datoteka?" closed="true" %}}
Da. I Evermusic i Flacbox sada podržavaju automatsko Last.fm scrobblanje. Pogledajte vodič: [Kako scrobblati na Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Što ako moj CSV ima pjesme starije od 14 dana?" closed="true" %}}
Koristite Način uvoza u Last.fm-Scrubbler-WPF. Preračunava vremenske žigove iz Vremena završetka, omogućujući vam scrobblanje pjesama bez obzira na njihov izvorni datum.
{{% /details %}}

{{% details title="Nemam Windows računalo. Mogu li još uvijek koristiti Last.fm-Scrubbler?" closed="true" %}}
Da. Instalirajte VirtualBox na vaš Mac i preuzmite besplatnu sliku Windows razvojnog okruženja od Microsofta. Pokrenite Last.fm-Scrubbler-WPF unutar virtualnog stroja.
{{% /details %}}

{{% details title="Zašto neke scrobble nisu analizirane?" closed="true" %}}
Pjesme kojima nedostaju bitni metapodaci (poput imena izvođača) ne mogu biti analizirane. To je očekivano i ne utječe na ostale pjesme u datoteci.
{{% /details %}}

{{% details title="Postoji li dnevno ograničenje scrobblanja?" closed="true" %}}
Da. Last.fm-Scrubbler-WPF dopušta do 2.800 scrobble-ova dnevno. Ako trebate scrobblati više, podijelite postupak na više dana.
{{% /details %}}
