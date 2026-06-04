---
title: "Popisi pjesama"
date: 2020-02-01
description: "Naučite kako stvarati, uvoziti, upravljati i prilagođavati popise pjesama u Flacboxu na iPhoneu, iPadu i Macu. Gradite popise pjesama iz cloud i lokalnih datoteka, uvezite M3U / M3U8 / CUE, prerasporedite pjesme, uredite omot, arhivirajte u ZIP, izvezite u M3U / CSV / TXT i koristite offline način rada."
keywords: [
  "Flacbox popisi pjesama", "uvoz M3U popisa", "upravitelj popisa pjesama",
  "stvori popis pjesama iPhone", "audio popisi pjesama Flacbox",
  "prilagođena slika popisa pjesama", "brisanje pjesama iz popisa pjesama",
  "sortiranje popisa pjesama Flacbox", "VoiceOver preraspoređivanje popisa pjesama",
  "Flacbox M3U izvoz", "Flacbox CSV izvoz", "arhiva popisa pjesama Flacbox",
  "Flacbox offline način rada popisa pjesama", "Flacbox CUE uvoz", "Flacbox duplikati pjesama"
]
tags: ["vodič", "flacbox", "popisi pjesama"]
readingTime: 7
---


U odjeljku Popisi pjesama naći ćete korisne alate za upravljanje glazbenim kolekcijama. Ovo područje prikazuje sve popise pjesama na jednom mjestu. Na vrhu se nalazi gumb **"..."** u navigacijskoj traci koji otvara izbornik s različitim opcijama popisa pjesama, plus alatna traka s brzim radnjama poput Pretraži, Pusti sve i Reproduciraj sve nasumično. Svaki popis pjesama ima i vlastiti gumb **"..."** pored naslova, dajući više opcija samo za taj popis.

Popisi pjesama u Flacboxu mogu sadržavati mješavinu online cloud zapisa, offline preuzetih datoteka i lokalnih datoteka s vašeg uređaja — sve u jednom popisu — i besprijekorno se reproduciraju zajedno.

{{< cards cols="1">}}
  {{< card title="" subtitle="Glavni zaslon Popisa pjesama u Flacboxu" image="/docs/guide/flacbox/img/playlists-main.webp" >}}
{{< /cards >}}

## Stvaranje popisa pjesama

Stvaranje novog popisa pjesama je jednostavno. Imate dvije opcije: tapnite gumb **+**, ili tapnite gumb **"..."** smješten u gornjem desnom kutu navigacijske trake i odaberite Novi popis pjesama. Dajte popisu pjesama smisleno ime, zatim tapnite Spremi.

Time se pokreće dijaloški okvir Dodaj pjesme, gdje možete ručno odabrati zapise koje želite uključiti u novi popis. Zapisi su praktično kategorizirani prema vrsti izvora:

- **Biblioteka** — zapisi koji su već u glazbenoj biblioteci.
- **Datoteke u ovoj aplikaciji** — audio datoteke u mapi Dokumenti aplikacije (preuzete iz cloud pohrane, uvezene putem Wi-Fi Drive-a ili dodane putem Finder File Sharinga).
- **Datoteke na ovom uređaju** — audio datoteke smještene na drugom mjestu na uređaju, ne u ovoj aplikaciji.
- **Povezivanja** — online datoteke smještene unutar vaših spojenih cloud usluga pohrane.

Prema zadanoj postavci, svaki zapis možete dodati u popis pjesama samo jednom. Ako želite dopustiti duplikate, omogućite ovu funkciju u Postavke → Glazbena biblioteka → Popisi pjesama → Duplikati u popisu → Omogući.

## Uvoz popisa

U Flacboxu smo dodali uvoz M3U / M3U8 / CUE datoteka kako ne biste morali ručno recreirati popise pjesama nakon prelaska s drugog playera.

Prvo idite na odjeljak Popisi. Zatim tapnite gumb Više u gornjem desnom kutu. Iz izbornika odaberite Uvezi popis.

Na sljedećem zaslonu odaberite lokaciju datoteke. Podržane opcije uključuju:

- Spojene cloud usluge pohrane
- Datoteke u aplikaciji
- Datoteke na uređaju

Odaberite spojenu cloud pohranu i otvorite mapu koja sadrži datoteku popisa. Podržani formati datoteka popisa su M3U, M3U8 i CUE. Odaberite datoteku popisa i tapnite Završeno za potvrdu odabira.

Aplikacija parsira datoteku popisa, stvara popis zapisa i locira te datoteke na pohrani za sastavljanje finalnog popisa, koji se zatim uvozi u glazbenu biblioteku. Važno: M3U / CUE datoteka mora sadržavati ispravne putanje do medijskih datoteka, a datoteke trebaju stvarno postojati na tim putanjama u pohrani. Pročitajte više o uvozu popisa [ovdje](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox).

## Zaslon detalja popisa

Kada otvorite popis pjesama, pojavljuje se zaslon Detalja popisa. U gornjem desnom kutu naći ćete gumb **"..."** s opcijama popisa, i tri gumba ispod omota: Pretraži, Nastavi reprodukciju, Pusti sve i Reproduciraj sve nasumično. Tu je i potvrdni okvir za Offline način rada za uključivanje offline sinkronizacije cijelog popisa.

- **Nastavi reprodukciju** — obnovite zadnju spremljenu poziciju reprodukcije za ovaj popis.
- **Pretraži** — izvršite pretragu unutar trenutnog popisa.
- **Pusti sve** — dodajte sve zapise iz trenutnog popisa u red čekanja playera.
- **Reproduciraj sve nasumično** — kao **Pusti sve**, ali miješa zapise prije dodavanja u red čekanja audio playera.
- **Offline način rada** — preuzmite sve zapise iz ovog popisa u lokalne datoteke. Sve nove stavke dodane u popis automatski se preuzimaju.

{{< cards cols="1">}}
  {{< card title="" subtitle="Zaslon detalja popisa u Flacboxu" image="/docs/guide/flacbox/img/playlist-details-screen.webp" >}}
{{< /cards >}}

## Više radnji za popis na zaslonu Popisi

Radnjama za popis možete pristupiti tapnutjem na gumb **"..."** pored naslova popisa. Dostupne radnje:

- **Pusti sve** — dodaje zapise popisa u svježi red čekanja playera.
- **Pusti sljedeće** — dodaje zapise popisa na vrh postojećeg reda čekanja playera.
- **Pusti poslije** — dodaje zapise popisa na dno postojećeg reda čekanja playera.
- **Uredi sliku** — promijenite omot popisa.
- **Omogući offline način rada** — uključite offline način rada za popis. I postojeći i novi zapisi preuzimaju se automatski. Pročitajte više o offline načinu rada [ovdje](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).
- **Izvezi popis pjesama** — izvezite ovaj popis u **M3U / M3U8 / CSV / TXT** kao što je opisano [ovdje](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Dodaj u arhivu** — arhivirajte ovaj popis (uključujući m3u datoteku, omot albuma i sve zapise) u jednu ZIP datoteku kao što je opisano [ovdje](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to). Premium funkcija.
- **Dodaj pjesme** — dodajte više pjesama u trenutni popis.
- **Preimenuj** — preimenujte popis.
- **Izbriši popis** — izbriši popis iz glazbene biblioteke. **Ova radnja se ne može poništiti.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Više radnji za popis na glavnom zaslonu Popisa u Flacboxu" image="/docs/guide/flacbox/img/more-actions-for-playlist-in-playlists-main-screen.webp" >}}
{{< /cards >}}

## Više radnji za popis na zaslonu Detalja popisa

Radnjama za popis možete pristupiti tapnutjem na gumb **"..."** u gornjem desnom kutu. Dostupne radnje:

- **Odaberi** — aktivirajte način odabira zapisa, koristan za brisanje više zapisa iz popisa ili promjenu redosljeda.
- **Pusti sljedeće** — dodajte zapise popisa na vrh postojećeg reda čekanja playera.
- **Pusti poslije** — dodajte zapise popisa na dno postojećeg reda čekanja playera.
- **Dodaj pjesme** — dodajte nove pjesme u popis.
- **Prerasporedi pjesme** — ručno promijenite redosljed pjesama u popisu koristeći povuci i ispusti.
- **Preimenuj** — preimenujte trenutni popis.
- **Uredi sliku** — promijenite omot albuma za trenutni popis.
- **Izvezi popis pjesama** — izvezite ovaj popis u **M3U / M3U8 / CSV / TXT**. Pročitajte više [ovdje](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Dodaj u arhivu** — ZIPajte trenutni popis uključujući sve zapise i m3u datoteku. Pročitajte više [ovdje](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Sortiraj** — promijenite redosljed zapisa u popisu. Opcije sortiranja uključuju **Naslov pjesme, Broj pjesme, Album, Izvođač, Izvođač albuma, Žanr, Skladatelj, Ocjena, Godina, Ritmovi u minuti, Trajanje, Naziv datoteke, Datum izmjene datoteke, Datum stvaranja datoteke** i **Ručno**. Opcija sortiranja **Ručno** dopušta ručno preraspoređivanje pjesama koristeći povuci i ispusti.
- **Pretraži** — potražite određenu pjesmu unutar trenutnog popisa.
- **Mreža / Popis** — promijenite prezentaciju izgleda zaslona.
- **Izbriši popis** — izbriši popis iz glazbene biblioteke. Ova radnja ne briše zapise iz pohrane, ali **ne može se poništiti**.

## Promjena redosljeda pjesama u popisu

Za promjenu redosljeda pjesama u popisu, tapnite gumb **"..."** u gornjem desnom kutu i odaberite **Odaberi** za ulazak u način odabira. Koristite kontrolu za preraspoređivanje i geste povuci i ispusti pokraj svakog zapisa za njegovo pomicanje gore ili dolje. Tapnutjem kontrole za preraspoređivanje premještate zapis na vrh popisa. Za izlazak iz načina odabira i primjenu promjena, tapnite **Završeno**.

Za još jednostavniji radni tijek s dugim popisima, odaberite Više radnji → Prerasporedi pjesme za ulazak u namjenski način preraspoređivanja povuci i ispusti.

{{< cards cols="1">}}
  {{< card title="" subtitle="Preraspoređivanje pjesama u popisu u Flacboxu" image="/docs/guide/flacbox/img/playlist-details-rearange-songs.webp" >}}
{{< /cards >}}

## Promjena omota popisa

Za promjenu omota popisa, tapnite gumb **"..."** u gornjem desnom kutu i odaberite **Uredi sliku**. Odaberite sliku iz dostupnih izvora (Fotografije, Datoteke, cloud pohrana ili generiran omot iz zapisa u popisu), zatim potvrdite tapnutjem **Završeno**.

## Dodavanje pjesama u popis

Otvorite popis i tapnite gumb **"..."** u gornjem desnom kutu, zatim odaberite **Dodaj pjesme** za otvaranje dijaloškog okvira. Odaberite zapise koje želite dodati i potvrdite tapnutjem **Završeno**.

## Brisanje više pjesama iz popisa

Otvorite popis, tapnite gumb **"..."** u gornjem desnom kutu i odaberite **Odaberi** za ulazak u način odabira. Odaberite zapise koje želite izbrisati i tapnite **Izbriši iz popisa** pri dnu zaslona. Potvrdite tapnutjem **Završeno**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Način odabira na zaslonu detalja popisa u Flacboxu" image="/docs/guide/flacbox/img/selection-mode-playlist-details-screen.webp" >}}
{{< /cards >}}

## Opcije zapisa

Svaki zapis u popisu ima popis radnji, kojima se pristupa tapnutjem na gumb **"..."**. Ako ne možete vidjeti sve radnje, pomaknite se prema dolje za njihov prikaz. Možete izbrisati zapis iz popisa, preuzeti ga, urediti audio oznake i još mnogo toga.

- **Pusti sljedeće** — dodaje zapis na vrh reda čekanja playera.
- **Pusti poslije** — dodaje zapis na dno reda čekanja playera.
- **Dodaj u popis** — dodaje zapis u drugi popis.
- **Dodaj u omiljene** — označava zapis kao omiljeni za brzi pristup.
- **Preuzmi** — čini zapis dostupnim offline. Pojavljuje se u redu čekanja za prijenose i na kartici **Lokalne datoteke** u odjeljku **Preuzeta glazba** glazbene biblioteke.
- **Uredi audio oznake** — otvara ugrađeni editor oznaka za promjenu metapodataka zapisa.
- **Otvori u** — izvozi zapis i otvara ga u drugoj aplikaciji.
- **Prikaži u mapi** — otkriva mapu u kojoj se audio datoteka nalazi.
- **Prikaži u Finderu** — za datoteke uvezene s Maca, ovo otkriva mapu u kojoj se audio datoteka nalazi na Macu.
- **Izbriši iz popisa** — briše zapis iz popisa.
- **Izbriši iz cloud usluge** — briše zapis iz popisa i s pridružene cloud usluge. **Ova radnja se ne može poništiti.**
- **Izbriši iz glazbene biblioteke** — briše zapis iz glazbene biblioteke, ostavljajući datoteku u pohrani netaknutom.

## Pristupačnost

Flacbox je u potpunosti pristupačan s VoiceOver tehnologijom, osiguravajući da svaka komponenta ima dobro dizajniranu oznaku i opis. Kada je VoiceOver aktivan, aplikacija prevodi korisničko sučelje u **Tekstualni način rada**, prikazujući samo pristupačne i korisne elemente za poboljšanje brzine navigacije i praktičnosti. Tekstualni način rada možete aktivirati i u Postavke → Pristupačnost → Tekstualni način rada.

### Podešavanje položaja zapisa u popisu s VoiceOver-om

1. Otvorite popis i tapnite gumb **Više**.
2. Odaberite **Promijeni redosljed pjesama**. Prikaz prelazi u način uređivanja.
3. Tapnite ikonu indikatora preraspoređivanja pokraj naslova zapisa kako biste je fokusirali.
4. **Dvaput tapnite** ikonu indikatora preraspoređivanja brzo. Na drugom tapnutju ne otpuštajte prst — zadržite dok ne čujete zvuk koji označava da je ćelija spremna za premještanje.
5. Sada možete premjestiti ćeliju na novu poziciju.

Ostale komponente rade prema očekivanjima, koristeći VoiceOver uzorke koje pruža sustav.
