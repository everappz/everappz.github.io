---
title: "Kako izvesti kolekciju pjesama u M3U, CSV i TXT u Evermusic i Flacbox"
date: 2024-01-31
description: "Naučite kako izvesti nedavne, omiljene, popise za reprodukciju i albume iz Evermusic i Flacbox u M3U, CSV ili TXT formate. Savršeno za Last.fm scrobblanje i reprodukciju na drugim uređajima."
keywords: ["evermusic izvoz", "flacbox izvoz", "izvoz u m3u", "izvoz popisa za reprodukciju u csv", "m3u txt csv popis za reprodukciju", "izvoz glazbe"]
tags: ["evermusic", "nedavne", "omiljeni", "izvoz", "m3u", "popis za reprodukciju", "csv", "txt", "album"]
---

{{< author-byline >}}


**Ukratko:** Evermusic i Flacbox omogućuju vam izvoz bilo koje kolekcije pjesama (nedavne, omiljeni, popisi za reprodukciju, albumi) u CSV, TXT ili M3U datoteke. Koristite ove izvoze za scrobblanje na Last.fm, sigurnosno kopiranje vaše biblioteke ili reprodukciju popisa za reprodukciju na drugim uređajima.

## Uvod

Izvoz vaših nedavnih, omiljenih, albuma i popisa za reprodukciju iz aplikacije u vanjsku datoteku može biti nevjerojatno koristan. Ove datoteke možete koristiti za ažuriranje povijesti slušanja na scrobbler servisima poput [Last.fm](http://Last.fm) ili slušanje popisa za reprodukciju na vanjskim uređajima. S Evermusic i Flacbox, ovaj je proces jednostavan. Ovdje ćemo vam pokazati kako izvesti vaše nedavne u CSV/TXT i popise za reprodukciju u M3U. Međutim, ova funkcionalnost je dostupna za bilo koju kolekciju pjesama unutar aplikacije.

## Odaberite format

Za izvoz vaših nedavnih otvorite odjeljak 'Glazbena biblioteka' i odaberite stavku izbornika 'Nedavne'.

![glazbena biblioteka](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Na sljedećem ekranu dodirnite gumb 'Više' u gornjem desnom kutu i odaberite 'Izvezi popis pjesama'.

![izvoz nedavnih](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

Na ekranu 'Odaberi format datoteke' imate nekoliko opcija - CSV, TXT, M3U.

- CSV

Ovo je skraćenica za Comma-Separated Values, savršeno za organiziranje vaših podataka u uredan tablični format. U odredišnoj datoteci pronaći ćete parametre poput Ime izvođača, Ime albuma, Ime pjesme, Vremenska oznaka (vrijeme kada ste slušali pjesme), Ime izvođača albuma i Trajanje pjesme. Tu datoteku možete kasnije koristiti za ažuriranje povijesti slušanja na scrobbler servisima poput [Last.fm](http://Last.fm) kako je opisano [ovdje](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Ovdje govorimo o običnoj tekstualnoj datoteci. Jednostavna je i jasna, s parametrima uključujući Ime izvođača, Ime albuma, Ime pjesme i Trajanje. Korisno ako vam samo treba popis pjesama u tekstualnom obliku.

- M3U

Ovaj format je u osnovi standard za stvaranje popisa za reprodukciju. Sjajan je jer možete izvesti svoj popis pjesama i uživati u svojim pjesmama na bilo kojem uređaju, čak i ako nemate originalne datoteke (ako odaberete opciju izvoza s apsolutnim URL-om za medijske datoteke). U izlaznoj datoteci pronaći ćete parametre poput Trajanje, Ime izvođača, Ime pjesme i Lokacija medijske datoteke.

## CSV format

Sada odaberimo CSV i pogledajmo što ćemo dobiti. Jednostavno odaberite CSV i pritisnite gumb 'Izvezi'.

![odabir formata datoteke](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Kada je izvoz završen, vidjet ćete obavijest s dvije opcije. Dodirom na 'Prikaži datoteku' prikazat će se rezultirajuća datoteka u vašem direktoriju dokumenata.

![izvoz završen](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Sada možete poslati tu datoteku, otvoriti je u vanjskom uređivaču teksta ili je koristiti za ažuriranje napretka slušanja na [Last.fm](http://Last.fm).

![mapa izvoza s rezultatima](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

Izlazna CSV datoteka sadržavat će polja u sljedećem formatu:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Na primjer:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![izvezena csv datoteka](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## TXT format

Izlazna TXT datoteka sadržavat će polja u sljedećem formatu:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Na primjer:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![izvezena txt datoteka](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## M3U format

Sljedeće ćemo vas provesti kroz izvoz vašeg popisa za reprodukciju u M3U format, koji je de facto standard za datoteke popisa za reprodukciju. Glavni preduvjet za uspješan izvoz popisa za reprodukciju je da se sve datoteke u popisu moraju nalaziti na istom skladištu, bilo da se radi o usluzi u oblaku poput vašeg Google Drivea, lokalnim datotekama ili datotekama na vašem uređaju. Za početak procesa izvoza otvorite bilo koji popis za reprodukciju i dodirnite gumb 'Više' u gornjem desnom kutu, zatim odaberite stavku izbornika 'Izvezi popis pjesama'.

![ekran popisa za reprodukciju](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Na sljedećem ekranu odaberite format datoteke 'M3U', gdje ćete naići na dvije opcije za 'Vrstu lokacije medijske datoteke':

![ekran odabira formata izvoza](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Ako odaberete 'Relativna putanja', popis za reprodukciju bit će kreiran s lokacijama medijskih datoteka zapisanim relativno u odnosu na datoteku popisa. Na primjer:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   U ovom slučaju izbjegavajte mijenjanje lokacije M3U datoteke nakon završetka izvoza, jer će to pokvariti putanje za medijske datoteke. Za početak reprodukcije vašeg popisa jednostavno dodirnite izvezenu datoteku popisa, a aplikacija će automatski pronaći medijske datoteke na vašem skladištu i pokrenuti reprodukciju. Možete čak izvesti svoje popise na skladište i zatim ih ponovno uvesti na svoj novi uređaj.

2. Ako odaberete 'Apsolutni URL', aplikacija će generirati izravne URL-ove za vaše medijske datoteke. To vam omogućuje reprodukciju popisa na bilo kojem uređaju/aplikaciji bez potrebe da se sve medijske datoteke nalaze na istom skladištu kao datoteka popisa. Ova opcija je podržana samo za usluge pohrane u oblaku koje mogu generirati izravne URL-ove datoteka. Međutim, imajte na umu da u nekim slučajevima generirani URL-ovi mogu imati ograničeno trajanje i mogu isteći nakon nekog vremena. Evo popisa podržanih usluga u oblaku: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (ako je u gostujućem načinu)  

Izlazni URL medijske datoteke bit će nešto poput:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Nakon što odaberete 'Vrstu lokacije medijske datoteke', dodirnite 'Izvezi'. Aplikacija će vas zatražiti da odaberete odredišnu mapu za izvoz M3U datoteke. Dodirnite 'Završeno' za potvrdu odabira.

![odabir mape](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Aplikacija će generirati M3U datoteku i prenijeti/premjestiti je u odredišnu mapu.

![prijenos m3u datoteke](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Kada je izvoz završen, pojavit će se obavijest sustava s opcijom 'Prikaži datoteku'.

![obavijest o završenom izvozu](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Dodirom na ovo prikazat će se izvezena datoteka u aplikaciji.

![izvezena m3u datoteka u popisu datoteka](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Ako ste odabrali 'Relativna putanja' kao 'Vrstu lokacije medijske datoteke' u prethodnom koraku, izlazna datoteka bit će u sljedećem formatu:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![m3u primjer s relativnim putanjama](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Za opciju 'Apsolutni URL' aplikacija će generirati M3U datoteku u formatu:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![m3u primjer s apsolutnim URL-ovima datoteka](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Tu datoteku možete otvoriti na bilo kojem uređaju/aplikaciji koja podržava M3U popise za reprodukciju.

![m3u popis za reprodukciju otvoren u vanjskoj aplikaciji](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Završne misli

Izvoz vaših pjesama iz Evermusic i Flacbox daje vam potpunu kontrolu nad vašim glazbenim podacima. Bilo da radite sigurnosnu kopiju povijesti slušanja, scrobblate na Last.fm ili uživate u popisima za reprodukciju na vanjskim uređajima, ove opcije izvoza: M3U, CSV i TXT - moćni su alati prilagođeni za fleksibilnost i kompatibilnost. Iskoristite ove značajke za poboljšanje načina na koji organizirate, dijelite i ponovno posjećujete svoju glazbenu kolekciju na različitim platformama.

## Često postavljana pitanja

{{% details title="Koji format izvoza trebam koristiti za Last.fm scrobblanje?" closed="true" %}}
Koristite CSV. Uključuje vremenske oznake i potpune metapodatke potrebne alatima za scrobblanje poput Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Mogu li izvesti bilo koju kolekciju pjesama, ne samo popise za reprodukciju?" closed="true" %}}
Da. Možete izvesti nedavne, omiljene, albume, popise za reprodukciju i bilo koju drugu kolekciju pjesama u aplikaciji koristeći iste korake.
{{% /details %}}

{{% details title="Hoće li moj M3U popis za reprodukciju raditi na drugim uređajima?" closed="true" %}}
Ako odaberete opciju Apsolutni URL tijekom izvoza, M3U datoteka se može reproducirati na bilo kojem uređaju koji podržava M3U popise za reprodukciju. Imajte na umu da neki URL-ovi oblaka mogu isteći s vremenom.
{{% /details %}}

{{% details title="Je li značajka izvoza besplatna?" closed="true" %}}
Da. Izvoz kolekcija pjesama u M3U, CSV i TXT dostupan je i u besplatnoj i u premium verziji Evermusic i Flacbox.
{{% /details %}}

{{% details title="Koje usluge u oblaku podržavaju izvoz Apsolutnog URL-a?" closed="true" %}}
Izvoz Apsolutnog URL-a podržan je za iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive i WebDAV (gostujući način).
{{% /details %}}
