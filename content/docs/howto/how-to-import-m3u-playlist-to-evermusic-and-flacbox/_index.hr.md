---
title: "Kako uvesti M3U popis pjesama u Evermusic i Flacbox"
date: 2024-01-31
description: "Saznajte kako uvesti M3U, M3U8 i CUE datoteke popisa pjesama iz oblaka, lokalnog prostora ili uređaja u Evermusic i Flacbox."
keywords: ["evermusic", "flacbox", "popis pjesama", "m3u", "m3u8", "cue", "uvoz", "glazbena aplikacija"]
tags: ["evermusic", "uvoz", "popisi pjesama", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Sažetak:** Evermusic i Flacbox podržavaju uvoz M3U, M3U8 i CUE datoteka popisa pjesama iz pohrane u oblaku, lokalnih datoteka aplikacije ili vašeg uređaja. Idite na Popisi pjesama > Više > Uvezi popis pjesama, odaberite izvor, odaberite datoteku i aplikacija automatski stvara vaš popis pjesama.

M3U, što znači MP3 URL ili Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, je format računalne datoteke koji se koristi za multimedijske popise pjesama. Jedna od njegovih primarnih upotreba je stvaranje datoteka popisa pjesama s jednim unosom koje upućuju na streamove na internetu. Ove datoteke nude praktičan pristup streaming sadržaju i obično se koriste za preuzimanja, e-poštu i slušanje internetskog radija.

Unatoč širokoj upotrebi, ne postoji formalna specifikacija za M3U format; postao je de facto standard. M3U datoteka je u osnovi obična tekstualna datoteka koja navodi lokacije jedne ili više medijskih datoteka. Ovisno o kodiranju, sprema se s ekstenzijom "m3u" ili "m3u8". Svaki unos u datoteci navodi lokaciju medijske datoteke, koja može biti apsolutni lokalni put, lokalni put relativan u odnosu na lokaciju M3U datoteke ili URL. Unosi su odvojeni prijelomima redaka, pri čemu neki uređaji zahtijevaju prijelome redaka predstavljene kao CR LF.

Dodatno, M3U datoteke mogu sadržavati komentare s prefiksom znaka "#". U proširenom M3U, "#" uvodi proširene M3U direktive, koje mogu podržavati parametre završene dvotočkom ":".

U našim aplikacijama Evermusic i Flacbox implementirali smo funkcionalnost uvoza M3U datoteka, eliminirajući potrebu za ručnim stvaranjem popisa pjesama. Ovaj vodič će vas provesti kroz uvoz vaših popisa pjesama iz pohrane u oblaku, lokalnih datoteka ili datoteka na vašem uređaju izravno u aplikaciju.

Prvo, navigirajte do odjeljka 'Popisi pjesama'. Zatim dodirnite gumb 'Više' koji se nalazi u gornjem desnom kutu. Iz izbornika koji se pojavi, odaberite opciju 'Uvezi popis pjesama'.

![radnja uvoza popisa pjesama](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Na sljedećem zaslonu odaberite lokaciju datoteke. Podržane opcije uključuju:

- Povezanu pohranu u oblaku;
- Datoteke u aplikaciji;
- Datoteke na vašem uređaju;

![odabir lokacije datoteke](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Odaberimo povezanu pohranu u oblaku i otvorimo mapu koja sadrži datoteku popisa pjesama. Podržane ekstenzije datoteka popisa pjesama uključuju M3U, M3U8 i CUE. Odaberite datoteku popisa pjesama i dodirnite 'Završeno' za potvrdu odabira.

![odabir M3U datoteke](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Aplikacija će analizirati datoteku popisa pjesama i stvoriti popis pjesama. Zatim će locirati te datoteke na pohrani i sastaviti konačni popis pjesama koji će biti uvezen u glazbenu knjižnicu. Ključno je da vaša M3U/CUE datoteka sadrži ispravne putove za medijske datoteke, a datoteke bi se trebale nalaziti na tim putovima na vašoj pohrani.

![uvezeni popis pjesama](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Aplikacija podržava i relativne putove i apsolutne URL-ove datoteka.

Na primjer:

Popis pjesama s relativnim putovima:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Popis pjesama s apsolutnim URL-ovima:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Ako uvozite datoteku popisa pjesama koja se nalazi unutar aplikacije (odjeljak Lokalne datoteke), nisu potrebni dodatni koraci.

Međutim, ako želite uvesti popis pjesama koji se nalazi na vašem uređaju koristeći birač datoteka sustava, postoji važna napomena koju treba imati na umu.

Zbog sigurnosnih politika, aplikacija može pristupiti samo datoteci koju odaberete pomoću birača datoteka sustava. Međutim, datoteka popisa pjesama može sadržavati veze na druge medijske datoteke na vašem uređaju. Za uvoz popisa pjesama s vašeg uređaja morate odabrati mapu koja sadrži i datoteku popisa pjesama i sve medijske datoteke povezane s njom. U tom slučaju, aplikacija će skenirati odabranu mapu, pronaći datoteku popisa pjesama, izgraditi popis pjesama i uvesti ga u glazbenu knjižnicu.

Dodatno, možete uvesti više popisa pjesama odjednom dodirom na gumb "Više radnji" i odabirom "Uvezi popise pjesama iz mape". Aplikacija će zatim skenirati sadržaj mape, pronaći podržane datoteke popisa pjesama i uvesti ih u knjižnicu.

## Često postavljana pitanja

{{% details title="Koje formate popisa pjesama podržavaju Evermusic i Flacbox?" closed="true" %}}
Obje aplikacije podržavaju M3U, M3U8 i CUE formate datoteka popisa pjesama. Oni pokrivaju najčešće standarde popisa pjesama koje koriste glazbeni playeri i medijski softver.
{{% /details %}}

{{% details title="Mogu li uvesti popise pjesama iz pohrane u oblaku?" closed="true" %}}
Da. Možete uvesti datoteke popisa pjesama iz bilo koje povezane usluge pohrane u oblaku, uključujući Google Drive, Dropbox, OneDrive i WebDAV poslužitelje.
{{% /details %}}

{{% details title="Zašto nedostaju neke pjesme nakon uvoza?" closed="true" %}}
Datoteka popisa pjesama mora sadržavati ispravne putove do vaših medijskih datoteka, a te datoteke moraju postojati na navedenim lokacijama na vašoj pohrani. Provjerite da putovi datoteka u vašoj M3U ili CUE datoteci odgovaraju stvarnim lokacijama datoteka.
{{% /details %}}

{{% details title="Mogu li uvesti više popisa pjesama odjednom?" closed="true" %}}
Da. Koristite gumb Više radnji i odaberite "Uvezi popise pjesama iz mape". Aplikacija skenira mapu za sve podržane datoteke popisa pjesama i uvozi ih u jednom koraku.
{{% /details %}}

{{% details title="Moram li ručno stvarati popise pjesama?" closed="true" %}}
Ne. Funkcija uvoza eliminira ručno stvaranje popisa pjesama. Samo usmjerite aplikaciju na svoju postojeću M3U, M3U8 ili CUE datoteku i ona automatski stvara popis pjesama.
{{% /details %}}
