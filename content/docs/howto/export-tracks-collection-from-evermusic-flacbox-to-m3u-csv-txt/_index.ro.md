---
title: "Cum să exportați colecția de piese în M3U, CSV și TXT din Evermusic și Flacbox"
date: 2024-01-31
description: "Aflați cum să exportați recente, preferințe, playlisturi și albume din Evermusic și Flacbox în formatele M3U, CSV sau TXT. Perfect pentru scrobbling pe Last.fm și redare pe alte dispozitive."
keywords: ["evermusic export", "flacbox export", "export în m3u", "export playlist în csv", "m3u txt csv playlist", "export muzică"]
tags: ["evermusic", "recents", "favorites", "export", "m3u", "playlist", "csv", "txt", "album"]
---

{{< author-byline >}}


**Pe scurt:** Evermusic și Flacbox vă permit să exportați orice colecție de piese (recente, preferințe, playlisturi, albume) în fișiere CSV, TXT sau M3U. Folosiți aceste exporturi pentru a face scrobbling pe Last.fm, pentru a crea o copie de rezervă a bibliotecii sau pentru a reda playlisturile pe alte dispozitive.

## Introducere

Exportarea recentelor, preferințelor, albumelor și playlisturilor din aplicație într-un fișier extern poate fi incredibil de utilă. Puteți folosi aceste fișiere pentru a vă actualiza istoricul de ascultare pe servicii de scrobbling precum [Last.fm](http://Last.fm) sau pentru a asculta playlisturile pe dispozitive externe. Cu Evermusic și Flacbox, acest proces este simplu. Aici vă vom arăta cum să exportați recentele în CSV/TXT și playlisturile în M3U. Cu toate acestea, această funcționalitate este disponibilă pentru orice colecție de piese din aplicație.

## Alegeți formatul

Pentru a exporta recentele, deschideți secțiunea «Biblioteca muzicală» și selectați elementul de meniu «Recente».

![biblioteca muzicală](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Pe ecranul următor, atingeți butonul «Mai mult» din colțul din dreapta sus și alegeți «Exportă lista de melodii».

![exportă recente](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

Pe ecranul «Selectați formatul fișierului» aveți mai multe opțiuni – CSV, TXT, M3U.

- CSV

Aceasta înseamnă Comma-Separated Values, perfect pentru organizarea datelor într-un format tabelar ordonat. În fișierul de destinație, veți găsi parametri precum numele artistului, numele albumului, numele piesei, marcaj temporal (momentul în care ați ascultat piesele), numele artistului albumului și durata piesei. Puteți folosi acel fișier ulterior pentru a vă actualiza istoricul de ascultare pe servicii de scrobbling precum [Last.fm](http://Last.fm), așa cum este descris [aici](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Aici vorbim despre un fișier text simplu. Este direct și clar, cu parametri care includ numele artistului, numele albumului, numele piesei și durata. Util dacă aveți nevoie doar de o listă de piese în format text.

- M3U

Acest format este practic standardul pentru crearea playlisturilor. Este excelent deoarece puteți exporta lista de melodii și vă puteți bucura de piesele pe orice dispozitiv, chiar dacă nu aveți fișierele originale (dacă selectați opțiunea URL absolut pentru exportul fișierelor media). În fișierul de ieșire, veți găsi parametri precum durata, numele artistului, numele piesei și locația fișierului media.

## Formatul CSV

Acum, să selectăm CSV și să vedem ce vom primi. Pur și simplu alegeți CSV și atingeți butonul «Exportă».

![selectați formatul fișierului](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Odată ce exportul este finalizat, veți vedea o alertă cu două opțiuni. Atingerea «Afișează fișierul» va dezvălui fișierul rezultat în directorul de documente.

![export finalizat](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Acum puteți trimite acel fișier, îl puteți deschide într-un editor de text extern sau îl puteți folosi pentru a vă actualiza progresul de ascultare pe [Last.fm](http://Last.fm).

![folder de export cu fișiere rezultat](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

Fișierul CSV de ieșire va conține câmpuri în următorul format:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

De exemplu:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![fișier csv exportat](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## Formatul TXT

Fișierul TXT de ieșire va conține câmpuri în următorul format:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

De exemplu:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![fișier txt exportat](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## Formatul M3U

În continuare, vă vom ghida prin exportarea playlistului în formatul M3U, care este standardul de facto pentru fișierele de playlist. Condiția principală pentru un export reușit al playlistului este ca toate fișierele din playlist să fie localizate pe același spațiu de stocare, fie că este un serviciu cloud precum Google Drive, fișiere locale sau fișiere de pe dispozitiv. Pentru a începe procesul de export, deschideți orice playlist și atingeți butonul «Mai mult» din colțul din dreapta sus, apoi alegeți elementul de meniu «Exportă lista de melodii».

![ecranul playlistului](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Pe ecranul următor, selectați formatul de fișier «M3U», unde veți întâlni două opțiuni pentru «Tipul locației fișierului media»:

![ecranul de selectare a formatului de export](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Dacă alegeți «Cale relativă», playlistul va fi creat cu locațiile fișierelor media scrise relativ la fișierul playlistului. De exemplu:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   În acest caz, evitați schimbarea locației fișierului M3U după finalizarea exportului, deoarece acest lucru va strica căile către fișierele media. Pentru a începe redarea playlistului, pur și simplu atingeți fișierul de playlist exportat, iar aplicația va localiza automat fișierele media pe spațiul de stocare și va iniția redarea. Puteți chiar exporta playlisturile pe spațiul de stocare și apoi le puteți importa din nou pe dispozitivul nou.

2. Dacă alegeți «URL absolut», aplicația va genera URL-uri directe pentru fișierele media. Aceasta vă permite să redați playlistul pe orice dispozitiv/aplicație fără a fi necesar ca toate fișierele media să fie localizate pe același spațiu de stocare ca fișierul playlistului. Această opțiune este suportată doar pentru stocarea cloud capabilă să genereze URL-uri directe ale fișierelor. Cu toate acestea, rețineți că în unele cazuri, URL-urile generate pot avea o durată de viață limitată și pot expira după un timp. Iată lista serviciilor cloud suportate: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (dacă în modul oaspete)  

URL-ul fișierului media de ieșire va fi ceva de genul:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

După ce ați selectat «Tipul locației fișierului media», atingeți «Exportă». Aplicația vă va solicita să alegeți un folder de destinație pentru exportul fișierului M3U. Atingeți «Finalizat» pentru a confirma selecția.

![selectați un folder](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Aplicația va genera un fișier M3U și îl va încărca/muta în folderul de destinație.

![încărcarea fișierului m3u](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Odată ce exportul este finalizat, va apărea o alertă de sistem cu opțiunea de a «Afișa fișierul».

![alertă export finalizat](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Atingerea acesteia va dezvălui fișierul exportat în aplicație.

![fișier m3u exportat în lista de fișiere](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Dacă ați selectat «Cale relativă» ca «Tipul locației fișierului media» în pasul anterior, fișierul de ieșire va fi în următorul format:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![exemplu m3u cu căi relative](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Pentru opțiunea «URL absolut», aplicația va genera un fișier M3U în formatul:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![exemplu m3u cu URL-uri absolute ale fișierelor](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Puteți deschide acel fișier pe orice dispozitiv/aplicație care suportă playlisturi M3U.

![playlist m3u deschis în aplicație externă](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Concluzii

Exportarea pieselor din Evermusic și Flacbox vă oferă control complet asupra datelor muzicale. Fie că faceți o copie de rezervă a istoricului de ascultare, scrobbling pe Last.fm sau vă bucurați de playlisturi pe dispozitive externe, aceste opțiuni de export – M3U, CSV și TXT – sunt instrumente puternice concepute pentru flexibilitate și compatibilitate. Profitați de aceste funcții pentru a îmbunătăți modul în care organizați, partajați și revizitați colecția muzicală pe diverse platforme.

## FAQ

{{% details title="Ce format de export ar trebui să folosesc pentru scrobbling pe Last.fm?" closed="true" %}}
Folosiți CSV. Include marcaje temporale și metadate complete necesare de instrumentele de scrobbling precum Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Pot exporta orice colecție de piese, nu doar playlisturi?" closed="true" %}}
Da. Puteți exporta recente, preferințe, albume, playlisturi și orice altă colecție de piese din aplicație folosind aceiași pași.
{{% /details %}}

{{% details title="Va funcționa playlistul meu M3U pe alte dispozitive?" closed="true" %}}
Dacă alegeți opțiunea URL absolut în timpul exportului, fișierul M3U poate fi redat pe orice dispozitiv care suportă playlisturi M3U. Rețineți că unele URL-uri cloud pot expira în timp.
{{% /details %}}

{{% details title="Este funcția de export gratuită?" closed="true" %}}
Da. Exportarea colecțiilor de piese în M3U, CSV și TXT este disponibilă atât în versiunea gratuită, cât și în versiunea premium a Evermusic și Flacbox.
{{% /details %}}

{{% details title="Ce servicii cloud suportă exportul cu URL absolut?" closed="true" %}}
Exportul cu URL absolut este suportat pentru iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive și WebDAV (modul oaspete).
{{% /details %}}
