---
title: "Uređivač oznaka"
date: 2020-02-01
description: "Naučite kako koristiti Evertag Uređivač oznaka za ažuriranje glazbenih metapodataka, uređivanje naslovnica albuma, grupno uređivanje više datoteka i upravljanje oznakama iz MusicBrainza. Idealno za organiziranje glazbene biblioteke na iOS-u i Macu."
keywords: [
  "Evertag uređivač oznaka", "uređivač audio metapodataka", "uređivač glazbenih oznaka",
  "uređivanje audio oznaka iPhone", "uređivač naslovnice albuma", "grupno uređivanje audio oznaka",
  "MusicBrainz metapodaci", "aplikacija za organiziranje glazbe", "Evertag vodič", "ID3 uređivač oznaka"
]
tags: ["vodič", "evertag", "uređivač oznaka"]
readingTime: 5
---


**Uređivač oznaka** je glavni zaslon aplikacije Evertag gdje možete pregledavati i uređivati metapodatke audio datoteka. Otvorite ovaj zaslon tapkanjem datoteke iz odjeljka **Lokalne datoteke** ili s bilo kojeg povezanog računa **pohrane u oblaku**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Zaslon Uređivača oznaka u Evertagu" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Načini uređivanja

Evertag pruža dva načina uređivanja:

- **Način rada s jednom datotekom**
  - Navigirajte između datoteka prelazeći prstom lijevo ili desno po karuselu grafike.

- **Grupni način rada**
  - Uređujte više datoteka odjednom i primijenite zajedničke metapodatke.
  - Za aktivaciju, pomaknite se do dna i tapnite **Uredi nekoliko datoteka istovremeno**.

## Način rada s jednom datotekom

Prema zadanim postavkama, aplikacija otvara uređivač oznaka u načinu rada s jednom datotekom s omogućenim samo glavnim opcijama uređivanja. U ovom načinu možete uređivati najuobičajenija polja metapodataka, kao što su:

**Track Title, Subtitle, Album Artist, Album, Artist, Composer, Performer, Genre, Comment, Beats Per Minute, Podcast, Compilation, Disc Number, Track Number, Track Total, Rating, Year**

Za pristup svim dostupnim oznakama, pomaknite se do dna zaslona i tapnite opciju **Prikaži proširene oznake**. To će prebaciti uređivač u prošireni način rada, omogućujući vam uređivanje više od **120 polja metapodataka**, uključujući **MusicBrainz oznake**, **Tekst pjesme**, **Savjetodavne ocjene**, replay-gain vrijednosti, redoslijede sortiranja, metapodatke podcastova i još mnogo toga. Koristite **Postavke → Uređivač audio oznaka → Gumbi na glavnom zaslonu** za trajno uključivanje opcije Prikaži proširene oznake tako da uvijek bude uključena.

{{< cards cols="1">}}
{{< card title="" subtitle="Panel akcija na dnu" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Grupni način rada

Grupno uređivanje možete pokrenuti na dva načina:

1. **Iz Upravitelja datoteka**
   - Tapnite **Više radnji** (•••) u gornjem desnom kutu.
   - Tapnite **Odaberi**, odaberite više datoteka, a zatim tapnite **Uredi audio oznake**.

2. **Iz Uređivača oznaka**
   - Otvorite bilo koju datoteku, pomaknite se do dna i tapnite **Uredi datoteke istovremeno** za učitavanje svih datoteka iz iste mape.

{{< cards cols="1">}}
{{< card title="" subtitle="Grupni način uređivanja" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Nakon uređivanja, tapnite **Spremi** za primjenu promjena.

## Uređivanje teksta pjesme

Prošireni uređivač otkriva polje **Tekst pjesme**. Tapnite ga za otvaranje liste tekstova — svaki unos teksta pjesme ima vlastiti jezik i opis, pa jedan track može pohraniti nekoliko prijevoda.

Ne morate sami tipkati tekst pjesme. Uređivač uključuje prečace za pretraživanje jednim tapkanjem prema najpopularnijim bazama podataka tekstova na webu, unaprijed ispunjene s izvođačem i naslovom trenutnog tracka:

- **Lrclib** — glavna javna baza podataka za **sinhronizirane (LRC-style) tekstove**. Koristite ga kada želite sinhronizirane tekstove koji se pomiču redak po redak u playerima koji ih podržavaju.
- **Genius** — velika katalog s anotacijama i točnim plain-text tekstovima.
- **Lyricsify** — baza podataka vođena zajednicom s plain i vremenski označenim tekstovima.
- **Google** — opće web pretraživanje kao rezervna opcija kada namjenske baze podataka nemaju podudaranje.

Svaki prečac se pojavljuje samo kada je odgovarajuća usluga dostupna s vašeg uređaja. Tapnite uslugu, kopirajte tekst (ili LRC vremenske oznake) koji želite, vratite se na Evertag i zalijepite ih u tekstualno polje — zatim **Spremi** za pisanje teksta natrag u oznake audio datoteke.

{{< cards cols="1">}}
  {{< card title="" subtitle="Stranice teksta pjesme" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Odaberite jezik iz birača:

{{< cards cols="1">}}
  {{< card title="" subtitle="Birač jezika teksta pjesme" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Zatim zalijepite ili utipkajte tekst pjesme. Evertag podržava i plain tekst i vremenski označene (sinhronizirane) tekstove — rezervirano mjesto prikazuje primjer LRC-style formata, što je točno ono što Lrclib i Lyricsify vraćaju za sinhronizirane rezultate.

{{< cards cols="1">}}
  {{< card title="" subtitle="Uređivač teksta pjesme" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Postavljanje ocjene i savjetodavne ocjene

Prošireni uređivač nudi kontrolu zvjezdice **Ocjena** uz segmentiranu kontrolu **Savjetodavna ocjena**.

### Ocjena zvjezdicama

Koristite polje **Ocjena** za davanje osobnog rezultata od jedne do pet zvjezdica tracku. Vrijednost se upisuje u standardnu oznaku ocjene datoteke (POPM za ID3, `rate` za MP4, `RATING` za Vorbis/APE, itd.), tako da će druge aplikacije koje čitaju ovu oznaku — uključujući Music app, Plex, Roon i većinu desktop uređivača oznaka — odmah preuzeti vaše ocjene.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ocjena" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Savjetodavna ocjena

**Savjetodavna ocjena** označava sadržaj tracka koristeći jednu od vrijednosti iz Parental Advisory standarda koji koristi iTunes Store i većina glazbenih platformi:

- **Neuvredljivo** — zadano za trackove bez informacija o roditeljskom nadzoru. Datoteka se tretira kao prikladna za sve slušatelje i neće prikazivati nikakvu savjetodavnu oznaku u playerima koji poštuju oznaku.
- **Eksplicitno** — track sadrži eksplicitan jezik ili sadržaj. Playeri koji poštuju roditeljski nadzor (Music app, Apple TV app, Spotify izvozi, Plex, itd.) prikazivat će oznaku **E** pored naslova i, kada su ograničenja omogućena na uređaju ili računu, mogu sakriti track iz profila djece ili odbiti reproducirati ga.
- **Čisto** — cenzurirana ili uređena verzija inače eksplicitnog tracka. Playeri prikazuju oznaku **C** kako bi slušatelji mogli razlikovati čistu verziju od originalnog eksplicitnog mastera, što je korisno kada obje verzije žive u istoj biblioteci.

Postat ćete svjesni potrebe za postavljanjem ili ispravljanjem ovog polja kada:

- Datoteka ima pogrešnu oznaku (na primjer čista radio verzija koja je pogrešno označena kao Eksplicitna, ili obrnuto).
- Trackovi su rippani ili preuzeti bez oznake i sada se prikazuju kao Neuvredljivi čak i ako sadrže eksplicitni sadržaj — potrebno da roditeljski nadzor i obiteljski dijeljene biblioteke rade ispravno.
- Pripremate album za predaju ili dijeljenje i trebate svaki track nositi dosljedne metapodatke.
- Želite da CarPlay, Lock Screen, Apple Music–style playeri ili DJ softver prikazuju ispravnu oznaku **E** / **C** pored naslova tracka.

Vrijednost se pohranjuje u standardno polje savjetodavne ocjene za format datoteke (`rtng` za MP4, `TXXX:ITUNESADVISORY` za ID3, `ITUNESADVISORY` za Vorbis), tako da će svaki player koji čita metapodatke roditeljskog nadzora vidjeti vaše ažuriranje.

{{< cards cols="1">}}
  {{< card title="" subtitle="Savjetodavna ocjena teksta pjesme" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Uređivanje naslovnice albuma

Za promjenu naslovnice albuma:

1. Tapnite **ikonu Kamere** u karuselu grafike.
2. Odaberite lokaciju slike: Lokalne datoteke, Oblak, Preuzimanja ili Biblioteka fotografija.
3. Odaberite sliku za primjenu kao naslovnica albuma.

{{< cards cols="1">}}
  {{< card title="" subtitle="Odabir slike" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Više radnji u Uređivaču oznaka

Dodatne opcije uređivanja dostupne su putem alatne trake ispod prikaza grafike.

{{< cards cols="1">}}
  {{< card title="" subtitle="Izbornik Više radnji" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Auto-pretraži audio oznake

Ova akcija aktivira pametni motor pretraživanja oznaka, koji pronalazi i ispunjava potpune metapodatke za vašu audio datoteku na temelju postojećih informacija.
Aplikacija koristi MusicBrainz bazu podataka — jednu od najsveobuhvatnijih baza podataka oznaka — s više od **50 milijuna** trackova.

### Pretraži naslovnicu albuma

Koristite metapodatke za pretraživanje weba za ispravnu grafiku albuma.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pretraži naslovnicu albuma" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Nakon pronalaska, sačuvajte sliku u **Fotografijama** koristeći sistemski kontekstni izbornik.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dodaj sliku u Fotografije" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Nakon toga, vratite se na uređivač oznaka, tapnite ikonu Kamere, idite na **Biblioteku fotografija** i odaberite spremljenu sliku. Aplikacija će je postaviti kao naslovnicu vaše audio datoteke.

Možete prilagoditi način skaliranja naslovnica u postavkama aplikacije.

### Spremi naslovnicu albuma

Ova akcija sprema trenutnu naslovnicu albuma u mapu **Documents**, tako da je možete ponovo koristiti kasnije.

### Normaliziraj kodiranje

Ova akcija će normalizirati tekstualno kodiranje svih oznaka u metapodacima audio datoteke. Posebno je korisna ako prelazite s Windows PC-ja, gdje datoteke mogu koristiti različita kodiranja koja se pojavljuju kao nečitljivi ili iskrivljeni znakovi na Macu.

### Ručno pretraži oznake

Ručno pretražujte metapodatke albuma koristeći MusicBrainz bazu podataka.

- Odaberite album

{{< cards cols="1">}}
  {{< card title="" subtitle="Odabir albuma" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Odaberite ispravnu pjesmu

{{< cards cols="1">}}
  {{< card title="" subtitle="Odabir pjesme" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Odaberite koje oznake primijeniti

{{< cards cols="1">}}
  {{< card title="" subtitle="Odabir audio oznaka" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Tapnite **Gotovo** za primjenu odabranih metapodataka na track.

### Izbriši audio oznake

Obrišite sva polja metapodataka za datoteku. Korisno pri početku od nule. Tapnite **Spremi** za potvrdu.

## Postavke Uređivača oznaka

Navigirajte do **Postavke → Uređivač audio oznaka** za prilagodbu ponašanja.

### Skaliranje naslovnice albuma

Odaberite kako naslovnice albuma trebaju biti skalirane pri pohrani u audio datoteke. Možete onemogućiti skaliranje za zadržavanje originalne veličine slike, ali budite svjesni da neki playeri možda neće podržavati velike datoteke grafike. Opcija "originalna veličina" dio je Premium funkcija personalizacije.

### Opcije pohrane oznaka

- **ID3v2.4** — Kada je omogućeno, aplikacija pohranjuje oznake u formatu ID3v2.4 kada je to moguće. Onemogućite za povratak na šire podržani ID3v2.3 ako vaše audio oznake nisu ispravno prikazane na starijim playerima ili uređajima.
- **Duplicate oznake** — Kada je omogućeno, uobičajena polja metapodataka duplicirana su u oba odjeljka oznaka datoteke. To poboljšava kompatibilnost sa starijim audio playerima, ali u većini slučajeva nije potrebno.

### Opcije ažuriranja metapodataka datoteka u oblaku

Možete kontrolirati kako aplikacija ažurira metapodatke za audio datoteke pohranjene u uslugama oblaka:

- **Prikaži poruku za potvrdu**
  Pitajte prije primjene promjena metapodataka na datoteke u oblaku.

- **Automatski ažuriraj metapodatke datoteke**
  Pohranite promjene metapodataka u datoteku u oblaku automatski nakon uređivanja.

- **Ne ažuriraj metapodatke datoteke**
  Preskočite ažuriranje datoteka u oblaku — promjene će se primjenjivati samo lokalno.

### Uredi online datoteke

Odaberite što se događa s lokalno preuzetim kopijama datoteka iz oblaka nakon uređivanja:

- **Uvijek izbriši preuzetu datoteku**
  Uklonite lokalnu kopiju nakon pohrane promjena.

- **Ne briši preuzetu datoteku**
  Zadržite preuzetu datoteku na uređaju nakon uređivanja.

### Gumbi na glavnom zaslonu

Prilagodite koje akcije se pojavljuju na glavnom zaslonu uređivača oznaka (Auto-pretraži audio oznake, Ručno pretraži audio oznake, Pretraži naslovnicu albuma, Spremi naslovnicu albuma, Normaliziraj kodiranje, Izbriši audio oznake). Možete i uključiti **Prikaži proširene oznake** i **Uredi datoteke istovremeno** tako da se uređivač uvijek otvara u preferiranom načinu rada.
