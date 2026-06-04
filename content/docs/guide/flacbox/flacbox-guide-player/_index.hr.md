---
title: "Audio player"
date: 2020-02-01
description: "Naučite kako koristiti Flacbox audio player na iPhoneu, iPadu i Macu. Kontrolirajte reprodukciju, upravljajte redovima čekanja, konfigurirajte FFmpeg / sistemski audio motor, promijenite frekvenciju uzorkovanja, korekciju visine tona, trajanje IO međuspremnika, ekvilajzer, audio zabilješke, AirPlay 2, Google Cast, CarPlay, widgete i tipkovničke prečace za Mac."
keywords: [
  "vodič za Flacbox player", "postavke audio playera", "Flacbox ekvilajzer",
  "AirPlay music streaming", "Google Cast glazba", "audio zabilješke",
  "Flacbox red čekanja za reprodukciju", "Flacbox ponavljanje nasumično", "Flacbox kontrola glasnoće",
  "macOS mini player", "voiceover glazbena aplikacija",
  "Flacbox FFmpeg", "Flacbox korekcija visine tona", "Flacbox frekvencija uzorkovanja",
  "Flacbox vanjski DAC", "Flacbox surround zvuk", "Flacbox IO međuspremnik",
  "Flacbox brzina reprodukcije", "Flacbox tajmer spavanja"
]
tags: ["vodič", "flacbox", "player"]
readingTime: 14
---


Audio player je glavni zaslon aplikacije gdje kontrolirate glazbu i većinu funkcija reprodukcije. Tu i Flacboxov hi-res audio motor — izgrađen na sistemskim kodecima plus ugrađenoj **FFmpeg** biblioteci — obavlja teški posao. Istražimo kako ga koristiti.

## Pristupanje audio playeru

Playeru na cijelom zaslonu možete pristupiti s trake mini playera. Na iPhoneu, mini player se nalazi pri dnu glavnog zaslona. Na iPadu i Macu, s lijeve strane. Za skrivanje mini playera na iPhoneu, tapnite ga jednom i povucite prema dolje. Za potpuno zatvaranje playera na cijelom zaslonu, tapnite gumb za zatvaranje u donjem desnom kutu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Glavni zaslon audio playera u Flacboxu" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Podržani audio formati

Flacbox reproducira najpopularnije audio formate — kako Appleove sistemske kodeke, tako i mnoge dodatne formate koje obrađuje ugrađeni FFmpeg motor:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

To pokriva gotovo sve moderne formaty s gubitkom i bez gubitka koje vjerojatno imate u osobnoj glazbenoj kolekciji.

## Kontrole reprodukcije

Pri dnu zaslona playera vidjet ćete gumbe za Reprodukciju, Pauzu, Sljedeći zapis i Prethodni zapis. Postoje i opcionalni gumbi Sljedećih 30 sek i Prethodnih 30 sek koje možete omogućiti u postavkama aplikacije (praktično za audioknjige). Možete brzo premotati naprijed ili unatrag zadržavanjem gumba Sljedeći / Prethodni. Za skok na određeni dio zapisa, povucite klizač reprodukcije.

## Ponavljanje i nasumično

Tapnite gumb za ponavljanje za prolazak kroz načine ponavljanja:

- **Ponovi sve** — ponavlja sve zapise u redu čekanja.
- **Ponovi jedan** — ponavlja samo trenutni zapis.
- **Zaustavi ponavljanje** — pauzira kada trenutni zapis završi.
- **Bez ponavljanja** — reproducira red čekanja jednom bez ponavljanja.

Koristite gumb **Nasumično** za nasumičan redoslijed zapisa u redu čekanja.

## Kontrola glasnoće

Otvorite zaslon Audio postavki tapnutjem na ikonu zvuka ispod kontrola reprodukcije za pristup klizaču glasnoće. Ovdje ćete naći i gumbe za **Google Cast** i **AirPlay** kako biste brzo prebacili reprodukciju na drugi uređaj.

## Google Cast (Chromecast)

Za korisnike Google Casta, ikona **Cast** pojavljuje se pri dnu playera. Tapnite je za odabir uređaja i početak streamanja. Osigurajte da su vaš uređaj i Google Cast prijemnik na istoj Wi-Fi mreži. Napomena: nije svaki audio format kompatibilan s Google Castom — neki hi-res formati možda trebaju biti transkodirani.

## AirPlay

Za AirPlay, potražite gumb **AirPlay** pri dnu playera. Tapnite ga i odaberite uređaj za streaming. Flacbox podržava **AirPlay 2**, pa možete reproducirati na više HomePodova, Apple TV-ova ili AirPlay-2-kompatibilnih zvučnika istovremeno.

## Audio ekvilajzer

Flacbox uključuje **10-pojasni ekvilajzer** s iPod-style presetsima. Tapnite Ekvilajzer na prikazu glasnoće, zatim ga uključite u gornjem desnom kutu. Možete koristiti presetse poput Acoustic i Bass Booster, ili prilagoditi svaki frekvencijski pojas klizačima. Napravite vlastite presetse, spremite ih pod bilo kojim nazivom i pojačajte ukupnu glasnoću predpojačalom. Imamo detaljnije upute o tome kako koristiti audio ekvilajzer [ovdje](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Ekvilajzer audio playera u Flacboxu" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Alatna traka načina rada playera

Za neke stilove playera postoji namjenska alatna traka na vrhu playera na cijelom zaslonu. Ova alatna traka sadrži tri korisna gumba:

- **Pretraži** — brzo pronađite određeni zapis u redu čekanja playera.
- **Kontrola brzine reprodukcije** — podesite brzinu reprodukcije od 0,02× do 3,00×. Savršeno za audioknjige, podcastove i predavanja. Tapnite Normalno za povratak na zadanu brzinu.
- **Audio zabilješke** — stvarajte više zabilješki po zapisu. Imamo potpune upute o tome kako koristiti zabilješke [ovdje](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Red čekanja playera

Za pregled reda čekanja playera, tapnite gumb reda čekanja na desnoj strani trenutne pjesme. Svaka pjesma u redu čekanja ima više radnji — tapnite tri točkice za njihov prikaz. Za preraspoređivanje pjesme u redu čekanja, koristite indikator preraspoređivanja pokraj naslova i povucite ga na novu poziciju.

{{< cards cols="1">}}
  {{< card title="" subtitle="Red čekanja reprodukcije u Flacboxu" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Komentari / Tekstovi

Za pregled komentara zapisa i ugrađenih tekstova, kao i LRC datoteka, slijedite ove korake:

1. Otvorite **Postavke**.
2. Idite na **Audio player**.
3. Odaberite **Personalizacija**.
4. Tapnite **Gumbi na glavnom zaslonu**.
5. Omogućite **Komentari**.

Nakon toga, tapnite gumb reda čekanja playera pri dnu zaslona nekoliko puta za prebacivanje iz prikaza omota / reda čekanja na prikaz komentara. Na zaslonu Komentara, povucite desno za prebacivanje između **Komentara**, **Ugrađenih tekstova** i **LRC datoteke**. Potpune upute dostupne su [ovdje](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Zaslon tekstova i komentara u Flacboxu" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Izbornik opcija

Svaka pjesma u redu čekanja audio playera ima izbornik s više radnji, kojima se pristupa tapnutjem na gumb s tri točkice pokraj naslova pjesme.

- **Pusti sljedeće** — dodaje pjesmu na vrh reda čekanja playera.
- **Dodaj u popis pjesama** — uključuje pjesmu u popis pjesama, s opcijom stvaranja novog.
- **Dodaj u omiljene** — označava pjesmu kao omiljenu za brzi pristup.
- **Preuzmi** — sprema pjesmu u lokalne datoteke, pojavljujući se na kartici **Lokalne datoteke** i u odjeljku **Offline glazba**.
- **Uredi audio oznake** — otvara ugrađeni editor audio oznaka za ispravljanje nedostajućih metapodataka, modificirajući pjesmu na vašem serveru.
- **Prikaži u mapi** — otkriva mapu u kojoj je pohranjena audio datoteka.
- **Prikaži u Finderu** — za datoteke uvezene s Maca, ovo otkriva mapu u kojoj se audio datoteka nalazi na Macu.
- **Otvori u** — izvozi audio datoteku u drugu aplikaciju.
- **Izbriši iz reda čekanja** — uklanja odabranu pjesmu iz reda čekanja audio playera.
- **Izbriši iz cloud usluge** — briše pjesmu i iz glazbene biblioteke i iz cloud pohrane. **Ova radnja je nepovratna.**
- **Izbriši iz lokalnih datoteka** — briše pjesmu i iz glazbene biblioteke i iz lokalne pohrane. **Ova radnja je nepovratna.**
- **Izbriši iz glazbene biblioteke** — briše pjesmu iz glazbene biblioteke, dok datoteka ostaje u pohrani.

Iste opcije dostupne su za trenutno puštanu stavku u redu čekanja audio playera, kojima možete pristupiti tapnutjem na ikonu **Više radnji** pokraj naslova zapisa.

{{< cards cols="1">}}
  {{< card title="" subtitle="Opcije za stavku u redu čekanja reprodukcije u Flacboxu" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Dodatne radnje playera

Tapnite gumb **Više radnji** "..." na lijevoj strani naslova trenutno puštane pjesme za prikaz dodatnih radnji.

- **Nastavi reprodukciju** — nastavite od mjesta gdje ste stali, uključujući red čekanja i poziciju medija. Posebno korisno za audioknjige. Aktivira se u postavkama aplikacije.
- **Pretraži** — brzo pronađite određeni zapis u redu čekanja audio playera.
- **Zabilješke** — pregledajte popis stvorenih audio zabilješki.
- **Komentari** — pregledajte komentare zapisa i ugrađene tekstove, kao i LRC datoteke. Potpune upute [ovdje](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Brzina** — podesite brzinu reprodukcije prema vašem ukusu.
- **Nedavne** — pristupite popisu nedavno puštenih pjesama.
- **Omiljeni** — pogledajte vašu kolekciju omiljenih pjesama.
- **Audio ekvilajzer** — aktivirajte audio ekvilajzer.
- **Tajmer spavanja** — postavite tajmer za zaustavljanje reprodukcije nakon određenog intervala. Odlično za trenutke kada se želite odmići uz glazbu.
- **Spremi red čekanja u popis pjesama** — spremite trenutni red čekanja audio playera kao novi popis pjesama.
- **Izbriši red čekanja** — obrišite red čekanja playera i zaustavite reprodukciju.
- **Postavke** — pristupite postavkama audio playera.
- **Pomoć** — pronađite pomoć i smjernice.

{{< cards cols="1">}}
  {{< card title="" subtitle="Zaslon više radnji audio playera u Flacboxu" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Audio zabilješke

Ova funkcija omogućuje stvaranje više zabilješki za zapise u glazbenoj biblioteci — savršeno za audioknjige, predavanja, duge DJ mješavine ili označavanje refrena omiljenog zapisa.

Za stvaranje nove zabilješke:

- Počnite reproducirati željenu pjesmu.
- Otvorite zaslon playera.
- Tapnite gumb **Zabilješke** na alatnoj traci načina rada playera.
- Odaberite **Dodaj zabilješku**.
- Odaberite vrijeme zabilješke i tapnite **Završeno** u gornjem desnom kutu.

Uređivanje zabilješki za trenutni zapis je lako: tapnite Uredi u gornjem desnom kutu za ulazak u način uređivanja. U ovom načinu rada možete prerasporediti zabilješke, brisati ih, prilagoditi vrijeme zabilješke i promijeniti naslove zabilješki. Detaljnije upute za audio zabilješke dostupne su [ovdje](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Zaslon audio zabilješki u Flacboxu" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Nedavne i omiljene

Na zaslonu playera, tapnite tri točkice za pristup Nedavnima i Omiljenima. U oba odjeljka možete pretraživati pjesme, pustiti sve, reproducirati sve nasumično, izvesti popis i obrisati popis. Imamo detaljne upute o tome kako izvesti popise pjesama [ovdje](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Spojite iPhone na auto putem USB-a ili bežičnog Apple CarPlaya i Flacbox se pojavljuje na početnom zaslonu CarPlaya, spreman za sigurno puštanje glazbe tijekom vožnje. CarPlay sučelje uključuje namjenske kartice za Biblioteku, Povezivanja, Lokalne datoteke i Postavke, s kontrolama reprodukcije, nasumičnim odabirom, ponavljanjem, upravljanjem redom čekanja i audio ekvilajzerom, sve bez uzimanja telefona. Dalje konfigurirajte CarPlay iskustvo u Postavke → CarPlay — opcije sortiranja, paginacija, boja gradijenta ikona izbornika, učitavaju li se slike i opcija automatskog pauziranja reprodukcije pri spajanju CarPlaya.

[Pročitajte potpuni CarPlay vodič](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox na Apple CarPlayu" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Widgeti početnog zaslona (iPhone i iPad)

Flacbox podržava iOS widgete početnog zaslona i zaslona zaključavanja kako biste mogli jednim pogledom vidjeti i kontrolirati reprodukciju. Provjerite jesu li Widgeti omogućeni u Postavke → Widgeti → Omogući widgete, zatim dugo pritisnite Početni zaslon ili Zaslon zaključavanja, tapnite **+**, potražite **Flacbox** i dodajte widget. Widget se osvježava tijekom reprodukcije za prikaz omota, naslova i izvođača trenutno puštanog zapisa.

## Prozor mini playera (isključivo za Mac)

Korisnici Maca mogu koristiti kompaktan, uvijek na vrhu mini player. Premjestite kursor na donji desni rub prozora Flacboxa, smanjite ga na najmanju veličinu i tapnite gumb skupljanja. Zadržite ga iznad svakog drugog prozora odabirom Prozor → Prikaži prozor uvijek na vrhu u traci izbornika — savršeno za vidljivost kontrola glazbe dok radite u drugoj aplikaciji.

## Tipkovnički prečaci (isključivo za Mac)

Za korisnike Maca, sistemski izbornik reprodukcije dostupan je u statusnoj traci s tipkovničkim prečacima. Na primjer, pritisnite razmaknicom za Reprodukciju / Pauzu. Prečaci za Zaustavljanje, Sljedeću pjesmu, Prethodnu pjesmu, Preskočiti Vrijeme, Ponavljanje, Nasumično i Brzinu reprodukcije su također dostupni.

## Postavke audio playera

Za pristup postavkama, tapnite gumb Više na zaslonu playera i odaberite Postavke. Ovdje ćete naći nekoliko odjeljaka, navedenih u nastavku.

### Općenito

Ove postavke pokrivaju temeljne aspekte audio playera, uključujući red čekanja za reprodukciju, audio izlaz i spremanje stanja playera.

- **Način ponavljanja** — odaberite kako se audio player ponaša kada zapis završi:
  - **Ponovi sve** — reproducira sve zapise u redu čekanja iznova.
  - **Ponovi jedan** — ponavlja samo trenutni zapis.
  - **Zaustavi ponavljanje** — pauzira reprodukciju kada trenutni zapis završi.
  - **Bez ponavljanja** — dopušta redu čekanja da se reproducira jednom bez ponavljanja.
- **Način nasumičnog odabira** — nasumičan redoslijed zapisa u redu čekanja. Možete ga postaviti na **Isključi nasumično** ili **Uključi nasumično**.
- **Audio kodek** — odaberite audio motor za reprodukciju:
  - **Sistemski kodek + FFmpeg** — daje prednost sistemskom audio kodeku gdje je moguće, poboljšavajući kompatibilnost i stabilnost. Korekcija visine tona i prilagodbe frekvencije uzorkovanja audio izlaza mogu biti ograničene u ovom načinu rada.
  - **FFmpeg** — forsira FFmpeg kodek za sve audio datoteke, dopuštajući podešavanje korekcije visine tona i frekvencije uzorkovanja audio izlaza.
- **Frekvencija uzorkovanja audio izlaza** — podesite frekvenciju uzorkovanja audio izlaza za optimizaciju kvalitete zvuka, posebno korisno s vanjskim DAC-om. Dostupne vrijednosti: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** i **96 kHz**.
- **Broj kanala audio izlaza** — za višekanalne audio sustave s vanjskim DAC-om, navedite broj kanala: **Mono, Stereo, Centar / Lijevo / Desno, Centar / Lijevo / Desno / Surround, ITU BS.775-1, 5.1 Surround** i **SDDS**.
- **Preferirano trajanje IO međuspremnika audio izlaza** — konfigurirajte trajanje međuspremnika ulaza / izlaza za audio reprodukciju. Tipična vrijednost za minimiziranje latencije pri reprodukciji visokokvalitetnog audija je oko **5 milisekundi (0,005 sekundi)**. Prihvatljiva veličina međuspremnika ovisi o vašem hardveru i softverskom okruženju, pa testirajte različita trajanja na ciljnom uređaju i odaberite ono koje best balansira nisku latenciju i reprodukciju bez smetnji.
- **Način rada audio izlaza (samo iOS)** — konfigurirajte mješoviti način audio izlaza tako da se audio iz Flacboxa miješa s drugim aplikacijama. Detaljne upute su [ovdje](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Spremi poziciju reprodukcije** — osigurava da aplikacija sprema i obnavlja poziciju reprodukcije za pjesme u glazbenoj biblioteci.
- **Spremi stanje audio playera** — čuva stanje audio playera prije zatvaranja aplikacije. Za nastavak reprodukcije, tapnite **Nastavi reprodukciju** na vrhu bilo koje mape, albuma, izvođača ili žanra kada ponovo otvorite aplikaciju. Reprodukciju za pojedinačne datoteke možete nastaviti i tapnutjem na određeni zapis.

Nakon što ste omogućili i **Spremi poziciju reprodukcije** i **Spremi stanje audio playera**, otvorite bilo koju mapu, album, izvođača ili žanr i vidjet ćete gumb **Nastavi reprodukciju** na vrhu zaslona zajedno s posljednjim spremljenim zapisom i pozicijom. Tapnite ga za nastavak točno tamo gdje ste stali.

### Personalizacija

Personalizacija vam omogućuje prilagodbu izgleda zaslona audio playera, promjenu dostupnih kontrola na glavnom zaslonu, zaslonu zaključavanja i statusnoj traci, te konfiguraciju kontrola za preskakanje.

- **Stil zaslona audio playera** — konfigurirajte pozicioniranje elemenata na zaslonu audio playera.
- **Stil pomicanja omova albuma** — konfigurirajte preferirani stil pomicanja za omove albuma.
- **Dodatni elementi** — omogućite dodatne elemente na zaslonu audio playera. **Informacije o audio formatu** prikazuje audio informacije trenutno puštanog zapisa iznad omota; **Klizač audio glasnoće** prikazuje klizač audio izlaza ispod kontrola reprodukcije.
- **Radnje na glavnom zaslonu** — konfigurirajte koji gumbi trebaju biti vidljivi na glavnom zaslonu audio playera prema zadanoj postavci: **Ponavljanje i nasumični način rada, Sljedeća i prethodna pjesma, Preskočiti Vrijeme, Tajmer spavanja, Google Chromecast, AirPlay i Bluetooth, Audio ekvilajzer, Pretraži, Zabilješke, Brzina, Dodaj zabilješku, Dodaj u omiljene, Komentari** i još mnogo toga.
- **Kontrole reprodukcije na zaslonu zaključavanja** — odaberite koje se kontrole pojavljuju na zaslonu zaključavanja. Moguće vrijednosti: **Preskočiti Vrijeme, Dodaj zabilješku, Dodaj u omiljene**.
- **Gumbi za preskakanje** — odaberite vremenski interval za gumbe **Preskočiti Vrijeme**.

### Učitavanje datoteka

Tijekom procesa učitavanja datoteka, možete promijeniti vrstu mreže koja se koristi za učitavanje pjesama. Dostupne opcije: **Wi-Fi**, **Wi-Fi i mobilni podaci**.

- **Vrijeme predučitavanja** — postavite vremenski interval buferizacije. Povećajte ovo ako imate lošu mrežnu vezu.
- **Koristi izravni URL** — kada je omogućeno, koristi se izravni URL za učitavanje pjesme ako poslužitelj to podržava. To može ubrzati učitavanje pjesme, ali može utjecati na stabilnost reprodukcije.

### Audio ekvilajzer

Prilagodite postavke audio ekvilajzera. Više o konfiguriranju audio ekvilajzera možete pročitati [ovdje](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Brzina reprodukcije

Podesite brzinu reprodukcije audio playera od **0,02× do 3,00×**. Tapnite ikonu konfiguracije u gornjem desnom kutu za prebacivanje na **precizni način rada** za finije prilagodbe.

{{< cards cols="1">}}
  {{< card title="" subtitle="Zaslon brzine reprodukcije u Flacboxu" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Korekcija visine tona

Promijenite postavke korekcije visine tona koristeći unaprijed definirane vrijednosti. Možete i prebaciti između unaprijed definiranih vrijednosti i preciznog načina rada tapnutjem na gumb u gornjem desnom kutu. Korekcija visine tona dostupna je na FFmpeg putu kodeka, s rasponom od **-1000 do +1000**.

### Predmemorija reprodukcije

Pjesme u redu čekanja audio playera automatski se preuzimaju za osiguranje glatke reprodukcije. Ako ručno preuzimate audio datoteke, možete onemogućiti ovu opciju za izbjegavanje duplikata. Ovdje možete i konfigurirati veličinu predmemorije audio playera.

### Tajmer spavanja

Aktivirajte tajmer za automatsko zaustavljanje reprodukcije nakon određenog perioda — praktično kada se želite odmići uz glazbu. Tapnite ikonu konfiguracije u gornjem desnom kutu za **precizni način rada** s granularnosti od minute do minute.

## Pristupačnost

Flacbox je u potpunosti pristupačan s **VoiceOver**. Svaka komponenta ima dobro dizajniranu oznaku i opis. Kada je VoiceOver aktivan, aplikacija prelazi u **Tekstualni način rada** kako bi se prikazali samo smisleni elementi — poboljšavajući brzinu navigacije i jasnoću. Tekstualni način rada možete aktivirati i u **Postavke → Pristupačnost → Tekstualni način rada**.

### Podešavanje klizača s VoiceOver-om

1. **Odaberite klizač** — povucite lijevo ili desno dok VoiceOver ne objavi klizač.
2. **Podesite vrijednost** — dvaput tapnite i zadržite klizač, zatim povucite gore ili dolje za brzu promjenu vrijednosti. VoiceOver objavljuje novu vrijednost dok napredujete.

### Podešavanje položaja zapisa u popisu s VoiceOver-om

1. Tapnite ikonu indikatora preraspoređivanja pokraj naslova zapisa kako biste je fokusirali.
2. Brzo dvaput tapnite indikator preraspoređivanja. Na drugom tapnutju ne otpuštajte prst — zadržite dok ne čujete zvuk koji označava da je ćelija spremna za premještanje.
3. Premjestite ćeliju na novu poziciju.

Ostale komponente rade prema očekivanjima, koristeći VoiceOver uzorke koje pruža sustav.
