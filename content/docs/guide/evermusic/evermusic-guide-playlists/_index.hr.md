---
title: "Popisi pjesama"
date: 2020-01-01
description: "Naučite kreirati, uvoziti, prilagođavati i upravljati popisima pjesama u Evermusicu. Uključuje detaljne korake za uređivanje, sortiranje, offline način rada i pristupačnost."
keywords: [
  "Evermusic", "playlists", "playlist management", "import M3U playlist",
  "edit playlist", "offline playlist", "change playlist order", "playlist cover",
  "playlist accessibility", "audio player"
]
tags: ["evermusic", "guide", "playlists"]
readingTime: 6
---


## Pregled

Odjeljak Popisi pjesama pruža vam alate za organiziranje pjesama u popise. Uključuje prikaz sadržaja koji prikazuje sve kreirane popise pjesama, gumb "..." u navigacijskoj traci koji nudi različite radnje vezane uz popise pjesama i navigacijsku alatnu traku s gumbima "Pretraži", "Reproduciraj sve" i "Izmiješaj sve". Nadalje, svaki pojedinačni popis pjesama ima gumb "..." pored naslova popisa, koji nudi niz radnji specifičnih za taj popis.

{{< cards cols="1">}}
  {{< card title="" subtitle="Zaslon Evermusic Popisa pjesama" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-main.webp" >}}
{{< /cards >}}

## Kreiranje popisa pjesama

Za kreiranje novog popisa pjesama, dodirnite gumb "+" ili gumb "..." u gornjem desnom kutu navigacijske trake, odaberite "Novi popis pjesama" i dodijelite naziv popisu. Nakon imenovanja, dodirnite "Spremi".

{{< cards cols="1">}}
  {{< card title="" subtitle="Kreiranje novog popisa pjesama" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-add-new.webp" >}}
{{< /cards >}}

Time se otvara dijaloški okvir "Dodaj pjesme", gdje možete odabrati koje pjesme dodati na novi popis. Pjesme su kategorizirane prema vrsti izvora i imate nekoliko opcija:

- **Biblioteka**: Pjesme iz glazbene biblioteke.
- **Datoteke u ovoj aplikaciji**: Audio datoteke pohranjene u direktoriju Documents aplikacije.
- **Datoteke na ovom iPhoneu/iPadu/Macu**: Audio datoteke smještene u drugim mapama na uređaju, izvan aplikacije.
- **Povezivanja**: Online datoteke pohranjene u spojenim uslugama pohrane u oblaku.

Prema zadanim postavkama, možete dodati pjesmu na popis samo jednom. Za dopuštanje duplikata na popisu, omogućite ovu značajku u Postavke aplikacije - Glazbena biblioteka - Popisi pjesama - Duplikati na popisu - Omogući.

## Uvoz popisa pjesama

U Evermusicu smo dodali funkcionalnost uvoza M3U datoteka kako ne biste morali ručno kreirati popise.

{{< cards cols="1">}}
  {{< card title="" subtitle="Uvoz popisa pjesama iz izvora datoteke" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-import-from-files.webp" >}}
{{< /cards >}}

Prvo idite na odjeljak 'Popisi pjesama'. Zatim dodirnite gumb 'Više' u gornjem desnom kutu. Iz izbornika koji se pojavljuje, odaberite opciju 'Uvezi popis pjesama'.

Na sljedećem zaslonu odaberite lokaciju datoteke. Podržane opcije uključuju:

- Spojena pohrana u oblaku
- Datoteke u aplikaciji
- Datoteke na uređaju

Odaberimo spojenu pohranu u oblaku i otvorimo mapu koja sadrži datoteku popisa. Podržane ekstenzije datoteka popisa uključuju M3U, M3U8 i CUE. Odaberite datoteku popisa i dodirnite 'Završeno' za potvrdu odabira.

Aplikacija će analizirati datoteku popisa, kreirati popis pjesama i locirati te datoteke na pohrani za kompajliranje konačnog popisa, koji će biti uvezen u glazbenu biblioteku. Ključno je da vaša M3U/CUE datoteka sadrži ispravne putanje do medijskih datoteka i da se datoteke nalaze na tim putanjama na pohrani. Više o uvozu popisa možete pročitati [ovdje](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox).

## Zaslon detalja popisa

Kada otvorite popis pjesama, pojavljuje se "Zaslon detalja popisa". Na ovom zaslonu pronaći ćete gumb "..." u gornjem desnom kutu s opcijama popisa i tri gumba ispod slike artwork: "Pretraži", "Nastavi reprodukciju", "Reproduciraj sve" i "Izmiješaj sve". Uz to, postoji potvrdni okvir "Offline način rada".

{{< cards cols="1">}}
  {{< card title="" subtitle="Zaslon detalja popisa" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-detail-screen.webp" >}}
{{< /cards >}}

- **Nastavi reprodukciju**: Vraća poziciju reprodukcije za ovaj popis.
- **Pretraži**: Izvodi pretraživanje unutar trenutnog popisa.
- **Reproduciraj sve**: Dodaje sve pjesme s trenutnog popisa u red reproduktora.
- **Izmiješaj sve**: Slično "Reproduciraj sve", ali miješa pjesme prije dodavanja u red audio reproduktora.
- **Offline način rada**: Preuzima sve pjesme s ovog popisa u lokalne datoteke. Sve nove stavke dodane na popis automatski će biti preuzete.

## Više radnji za popis na zaslonu Popisa pjesama

Radnjama za popis možete pristupiti dodirivanjem gumba "..." pored naslova popisa. Evo dostupnih radnji:

- **Reproduciraj sve:** Dodaje pjesme popisa u novi red reproduktora.
- **Reproduciraj sljedeće:** Dodaje pjesme popisa na vrh postojećeg reda reproduktora.
- **Reproduciraj kasnije:** Dodaje pjesme popisa na dno postojećeg reda reproduktora.
- **Uredi sliku:** Uredite artwork sliku popisa.
- **Omogući offline način rada:** Omogućuje offline način rada za popis. U ovom scenariju, i postojeće i nove pjesme automatski će biti preuzete. Pročitajte više o offline načinu [ovdje](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).
- **Izvezi popis pjesama:** Ovaj popis možete izvesti u različitim formatima kao što je opisano [ovdje](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Dodaj u arhivu:** Ovaj popis možete arhivirati uključujući m3u datoteku, omot albuma i sve pjesme kao što je opisano [ovdje](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Dodaj pjesme:** Dodajte više pjesama u trenutni popis.
- **Preimenuj:** Preimenujte popis.
- **Izbriši popis:** Obrišite popis iz glazbene biblioteke. Napominjemo da se ova radnja ne može poništiti.

{{< cards cols="1">}}
  {{< card title="" subtitle="Izbornik više radnji za popis" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-more-actions-for-separate-playlist.webp" >}}
{{< /cards >}}

## Više radnji za popis na zaslonu detalja popisa

Radnjama za popis možete pristupiti dodirivanjem gumba "..." u gornjem desnom kutu. Evo dostupnih radnji:

- **Odabrati:** Aktivira način odabira pjesama, koristan za brisanje više pjesama s popisa ili promjenu redosljeda.
- **Reproduciraj sljedeće:** Dodaje pjesme popisa na vrh postojećeg reda reproduktora.
- **Reproduciraj kasnije:** Dodaje pjesme popisa na dno postojećeg reda reproduktora.
- **Dodaj pjesme:** Dodajte nove pjesme na popis.
- **Preuredi pjesme:** Ručno promijenite redosljed pjesama na popisu koristeći povuci i ispusti.
- **Preimenuj:** Preimenujte trenutni popis.
- **Uredi sliku:** Uredite artwork albuma za trenutni popis.
- **Izvezi popis pjesama:** Izvezite ovaj popis u različite formate. Više možete pročitati [ovdje](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Dodaj u arhivu:** Zipajte trenutni popis uključujući sve pjesme i m3u datoteku. Više možete pročitati [ovdje](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Sortiraj:** Promijenite redosljed pjesama na popisu. Opcije sortiranja uključuju "Naslov pjesme", "Broj pjesme", "Album", "Izvođač", "Album izvođač", "Žanr", "Skladatelj", "Ocjena", "Godina", "Otkucaji u minuti", "Trajanje", "Naziv datoteke", "Datum izmjene datoteke", "Datum kreiranja datoteke" i "Ručno". Opcija "Ručno" sortiranje omogućuje ručno preuređivanje pjesama koristeći povuci i ispusti.
- **Pretraži:** Pretražite određenu pjesmu unutar trenutnog popisa.
- **Mreža/popis:** Promijenite prezentaciju rasporeda zaslona.
- **Izbriši popis:** Obrišite popis iz glazbene biblioteke. Važno je napomenuti da ova radnja ne briše pjesme s pohrane i ne može se poništiti.

## Promjena redosljeda pjesama na popisu

Za promjenu redosljeda pjesama na popisu, dodirnite gumb "..." u gornjem desnom kutu i odaberite "Odaberi" za ulazak u način odabira. Koristite kontrolu za preuređivanje i geste povuci i ispusti pored svake pjesme za premještanje gore ili dolje. Dodirivanjem kontrole za preuređivanje premještate pjesmu na vrh popisa. Za izlazak iz načina odabira i primjenu promjena, dodirnite "Završeno".

{{< cards cols="1">}}
  {{< card title="" subtitle="Promjena redosljeda pjesama na popisu" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-change-songs-order.webp" >}}
{{< /cards >}}

## Promjena naslovne slike popisa

Za promjenu naslovne slike popisa, dodirnite gumb "..." u gornjem desnom kutu i odaberite "Uredi sliku". Odaberite sliku iz dostupnih izvora i potvrdite promjene dodirivanjem "Završeno".

## Dodavanje pjesama na popis

Otvorite popis i dodirnite gumb "..." u gornjem desnom kutu, zatim odaberite "Dodaj pjesme" za otvaranje dijaloškog okvira. Odaberite pjesme koje želite dodati i potvrdite promjene dodirivanjem "Završeno".

## Brisanje više pjesama s popisa

Otvorite popis, dodirnite gumb "..." u gornjem desnom kutu i odaberite "Odaberi" za ulazak u način odabira. Odaberite pjesme koje želite obrisati i dodirnite gumb "Izbriši s popisa" na dnu zaslona. Potvrdite promjene dodirivanjem "Završeno".

{{< cards cols="1">}}
  {{< card title="" subtitle="Način odabira unutar popisa" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-selection-mode-in-playlist-details-screen.webp" >}}
{{< /cards >}}

## Opcije pjesme

Svaka pjesma na popisu ima popis radnji, dostupnih dodirivanjem gumba "...". Ako ne vidite sve radnje, pomaknite se prema dolje za prikaz. Možete obrisati pjesmu s popisa, preuzeti je, urediti audio oznake i više.

{{< cards cols="1">}}
  {{< card title="" subtitle="Izbornik opcija pjesme na popisu" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-track-options.webp" >}}
{{< /cards >}}

- **Reproduciraj sljedeće:** Dodaje pjesmu na vrh reda reproduktora.
- **Reproduciraj kasnije:** Dodaje pjesmu na dno reda reproduktora.
- **Dodaj na popis pjesama:** Dodaje pjesmu na popis.
- **Dodaj u omiljene:** Označava pjesmu kao omiljenu za brz pristup.
- **Preuzeti:** Čini pjesmu dostupnom offline. Pojavit će se u redu prijenosa i kartici "Lokalne datoteke" u odjeljku "Preuzeta glazba" glazbene biblioteke.
- **Urediti audio oznake:** Otvara ugrađeni uređivač oznaka za promjenu metapodataka pjesme.
- **Otvori u:** Izvozi pjesmu i otvara je u drugoj aplikaciji.
- **Prikaži u mapi:** Otkriva mapu gdje se nalazi audio datoteka.
- **Prikaži u Finderu:** Za datoteke uvezene s Maca, ova radnja otkriva mapu gdje se audio datoteka nalazi na Mac računalu.
- **Izbriši s popisa:** Briše pjesmu s popisa.
- **Izbriši s oblak usluge:** Briše pjesmu s popisa i pridružene oblak usluge. Napominjemo da se ova radnja ne može poništiti.
- **Izbriši iz glazbene biblioteke:** Briše pjesmu iz glazbene biblioteke, ostavljajući datoteku u pohrani netaknutom.

## Pristupačnost

Naša aplikacija potpuno je dostupna s VoiceOver tehnologijom, osiguravajući da svaka komponenta ima dobro dizajniranu oznaku i opis. Kada je VoiceOver aktivan, aplikacija prevodi korisničko sučelje u tekstualni način, prikazujući samo dostupne i korisne elemente za poboljšanje brzine navigacije i udobnosti. Tekstualni način možete aktivirati i u Postavke > Pristupačnost > Tekstualni način.

Za podešavanje pozicije pjesme na popisu s VoiceOver:

1. Otvorite popis pjesama i dodirnite gumb "Više".
2. Odaberite "Promijeni redosljed pjesama". Prikaz će se prebaciti u način uređivanja.
3. Dodirnite ikonu indikatora za preuređivanje pored naslova pjesme za fokusiranje.
4. Brzo dvaput dodirnite ikonu indikatora za preuređivanje. Na drugi dodir, nemojte pustiti prst — držite dok ne čujete zvuk koji označava da je ćelija sprema za premještanje.
5. Sada možete premjestiti ćeliju na novu poziciju.

Ostale komponente rade prema očekivanjima, koristeći VoiceOver uzorke koje pruža sustav.
