---
title: "Kako omogućiti DLNA Media Server na Windows 10 i reproducirati glazbu na iPhoneu"
date: 2019-11-26
description: "Omogućite DLNA poslužitelj na Windows 10 i streamajte glazbu na iPhone s aplikacijom Evermusic. Uključen je vodič za postavljanje korak po korak."
keywords: ["evermusic", "dlna", "windows 10", "streaming glazbe na iphone", "medijski poslužitelj", "lokalna mreža", "upnp"]
tags: ["evermusic", "glazba", "oblak", "iphone", "pohrana", "lokalno", "nas", "windows", "wifi", "slušanje", "mreža", "udaljeno", "dom", "online", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**Ukratko:** Windows 10 ima ugrađeni DLNA poslužitelj. Omogućite ga u postavkama Mreže i dijeljenja, zatim koristite besplatnu aplikaciju **Evermusic** na svom iPhoneu za streaming cijele glazbene biblioteke putem Wi-Fi. Nije potreban softver poslužitelja treće strane.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Naslovnica" caption="DLNA streaming glazbe na iPhone koristeći Windows 10 i Evermusic" width="800" >}}

DLNA (Digital Living Network Alliance) je moćan alat koji vam omogućuje jednostavno streamanje raznog medijskog sadržaja, uključujući glazbu, između uređaja s podrškom za DLNA na vašoj mreži. Dobra vijest je da Windows 10, kao i prethodne verzije, dolaze s ugrađenom DLNA značajkom, eliminirajući potrebu za medijskim poslužiteljima treće strane. Evo kako omogućiti DLNA Media Server na Windows 10 i uživati u streamanju glazbe na svom iPhoneu.

## Kako omogućiti DLNA Media Server na Windows 10

1. Kliknite gumb 'Start'.  
2. Odaberite ikonu 'Postavke'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Postavljanje poslužitelja" caption="Otvorite Windows postavke" width="500" >}}

3. Na zaslonu 'Windows postavke', odaberite 'Mreža i internet'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Windows postavke" caption="Odaberite Mreža i internet" width="500" >}}

4. Pod 'Mreža', odaberite 'Centar za mrežu i dijeljenje'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Centar za dijeljenje" caption="Otvorite Centar za mrežu i dijeljenje" width="500" >}}

5. Na zaslonu 'Centar za mrežu i dijeljenje', kliknite 'Promijeni napredne postavke dijeljenja' u lijevom izborniku.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Napredne postavke dijeljenja" caption="Promijeni napredne postavke dijeljenja" width="500" >}}

6. Na zaslonu 'Napredne postavke dijeljenja', pomaknite se do odjeljka 'Sve mreže' i proširite ga klikom na strelicu.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Uključi otkrivanje" caption="Proširite postavke svih mreža" width="500" >}}

7. Kliknite 'Uključi streaming medija' za aktiviranje DLNA poslužitelja.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Uključi poslužitelj" caption="Omogućite poslužitelj za streaming medija" width="500" >}}

8. Dajte svojoj medijskoj biblioteci ime i odaberite uređaje kojima je dopušten pristup.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Ime medijske biblioteke" caption="Imenujte svoju DLNA medijsku biblioteku" width="500" >}}

9. Kliknite 'U redu' za potvrdu. Sada će vaše osobne mape poput Glazba, Slike i Videozapisi biti vidljive svim streaming uređajima s UPnP podrškom.

## Kako onemogućiti DLNA Media Server na Windows 10

1. Kliknite 'Start' i upišite 'services' u polje za pretraživanje.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Windows usluge" caption="Otvorite Windows usluge" width="500" >}}

2. Na zaslonu 'Usluge', pomaknite se kako biste pronašli 'Windows Media Player Network Sharing Service'.  
3. Dvaput kliknite na nju i postavite 'Vrsta pokretanja' na 'Ručno'.  
4. Zaustavite uslugu klikom na gumb 'Zaustavi'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="Zaustavi DLNA uslugu" caption="Onemogućite DLNA uslugu mrežnog dijeljenja" width="500" >}}

## Kako reproducirati glazbu s DLNA poslužitelja na iPhoneu

1. Instalirajte besplatnu aplikaciju **Evermusic** iz App Storea:  
   [Aplikacija Evermusic](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Otvorite karticu 'Veze' i dodirnite 'Dostupni uređaji' u odjeljku 'Lokalna mreža'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Evermusic veze" caption="Evermusic: zaslon Veze" width="500" >}}

3. Pričekajte nekoliko sekundi dok se lista uređaja učitava i dodirnite Windows Media Player DLNA poslužitelj (npr. 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Dostupni uređaji" caption="Dostupni DLNA poslužitelji u Evermusicу" width="500" >}}

4. Vidjet ćete popis mapa dostupnih na medijskom poslužitelju.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Evermusic mape" caption="Pregledajte dijeljene mape s DLNA poslužitelja" width="500" >}}

5. Otvorite bilo koju mapu koja sadrži audio datoteke.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Sadržaj mape" caption="Prikažite sadržaj dijeljenih DLNA mapa" width="500" >}}

6. Dodirnite bilo koju datoteku za pokretanje audio playera.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Audio player" caption="Reproducirajte audio datoteku s DLNA u Evermusicу" width="500" >}}

7. Za poboljšanje audio iskustva, dodirnite ikonu 'Ekvilajzer' blizu indikatora glasnoće na dnu zaslona za aktiviranje ekvilajzera u stilu iPod s predpojačalom.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Ekvilajzer" caption="Koristite ugrađeni ekvilajzer za poboljšanu reprodukciju" width="500" >}}

## Zaključak

S DLNA Media Serverom na Windows 10 i Evermusicom na vašem iPhoneu, možete uživati u besprijekornom streamanju glazbe s računala na mobilni uređaj. Recite zbogom ograničenjima pohrane i pozdravite glazbu na zahtjev!

## Često postavljana pitanja

{{% details title="Trebam li instalirati softver poslužitelja na Windows 10?" closed="true" %}}
Ne. Windows 10 uključuje ugrađeni DLNA medijski poslužitelj. Trebate samo omogućiti streaming medija u postavkama Centra za mrežu i dijeljenje. Nije potreban softver treće strane.
{{% /details %}}

{{% details title="Mora li moj iPhone biti na istoj Wi-Fi mreži?" closed="true" %}}
Da. DLNA streaming radi preko vaše lokalne mreže. I vaše Windows 10 računalo i iPhone moraju biti povezani na istu Wi-Fi mrežu kako bi Evermusic mogao otkriti DLNA poslužitelj.
{{% /details %}}

{{% details title="Koje audio formate mogu streamati putem DLNA?" closed="true" %}}
Windows DLNA poslužitelj dijeli datoteke iz vaše mape Glazba bez obzira na format. Evermusic podržava MP3, FLAC, AAC, WAV, OGG, AIFF i mnoge druge formate, tako da možete reproducirati praktički bilo koju audio datoteku s poslužitelja.
{{% /details %}}

{{% details title="Mogu li koristiti Flacbox umjesto Evermusica?" closed="true" %}}
Da. Flacbox također podržava DLNA/UPnP pregledavanje i reprodukciju. Možete koristiti bilo koju od dvije aplikacije za otkrivanje i reprodukciju glazbe s vašeg Windows DLNA poslužitelja.
{{% /details %}}

{{% details title="Hoće li DLNA streaming koristiti mobilne podatke?" closed="true" %}}
Ne. DLNA radi isključivo na vašoj lokalnoj Wi-Fi mreži. Ne koristi nikakve mobilne podatke. Međutim, oba uređaja moraju ostati povezana na istu mrežu tijekom reprodukcije.
{{% /details %}}
