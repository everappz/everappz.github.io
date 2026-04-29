---
title: "Com exportar la col·lecció de pistes a M3U, CSV i TXT a Evermusic i Flacbox"
date: 2024-01-31
description: "Aprèn a exportar els teus recents, favorits, llistes de reproducció i àlbums d'Evermusic i Flacbox a formats M3U, CSV o TXT. Perfecte per fer scrobbling a Last.fm i reproduir en altres dispositius."
keywords: ["exportar evermusic", "exportar flacbox", "exportar a m3u", "exportar llista de reproducció a csv", "m3u txt csv llista de reproducció", "exportar música"]
tags: ["evermusic", "recents", "favorits", "exportar", "m3u", "llista de reproducció", "csv", "txt", "àlbum"]
---

{{< author-byline >}}


**Resum:** Evermusic i Flacbox et permeten exportar qualsevol col·lecció de pistes (recents, favorits, llistes de reproducció, àlbums) a fitxers CSV, TXT o M3U. Utilitza aquestes exportacions per fer scrobbling a Last.fm, fer còpies de seguretat de la teva biblioteca o reproduir les teves llistes de reproducció en altres dispositius.

## Introducció

Exportar els teus recents, favorits, àlbums i llistes de reproducció de l'aplicació a un fitxer extern pot ser increïblement útil. Pots utilitzar aquests fitxers per actualitzar el teu historial d'escolta en serveis de scrobbling com [Last.fm](http://Last.fm) o escoltar les teves llistes de reproducció en dispositius externs. Amb Evermusic i Flacbox, aquest procés és fàcil. Aquí, et mostrarem com exportar els teus recents a CSV/TXT i les teves llistes de reproducció a M3U. No obstant això, aquesta funcionalitat està disponible per a qualsevol col·lecció de pistes dins de l'aplicació.

## Triar format

Per exportar els teus recents, obre la secció 'Biblioteca de música' i selecciona l'element del menú 'Recents'.

![biblioteca de música](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

A la pantalla següent, toca el botó 'Més accions' a la cantonada superior dreta i tria 'Exportar llista de cançons'.

![exportar recents](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

A la pantalla 'Seleccionar format de fitxer' tens diverses opcions - CSV, TXT, M3U.

- CSV

Això significa Valors Separats per Comes, perfecte per organitzar les teves dades en un format de taula ordenat. Al fitxer de destinació, trobaràs paràmetres com Nom de l'Artista, Nom de l'Àlbum, Nom de la Pista, Marca de temps (l'hora en què vas escoltar les pistes), Nom de l'Artista de l'Àlbum i Durada de la Pista. Pots utilitzar aquest fitxer més tard per actualitzar el teu historial d'escolta en serveis de scrobbling com [Last.fm](http://Last.fm) tal com es descriu [aquí](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Aquí, parlem d'un fitxer de text pla. És senzill i directe, amb paràmetres que inclouen Nom de l'Artista, Nom de l'Àlbum, Nom de la Pista i Durada. Útil si només necessites una llista de pistes en presentació de text.

- M3U

Aquest format és essencialment l'opció preferida per crear llistes de reproducció. És genial perquè pots exportar la teva llista de cançons i gaudir de les teves pistes en qualsevol dispositiu, fins i tot si no tens els fitxers originals (si selecciones l'opció d'URL absolut per a l'exportació de fitxers multimèdia). Al fitxer de sortida, trobaràs paràmetres com Durada, Nom de l'Artista, Nom de la Pista i Ubicació del Fitxer Multimèdia.

## Format CSV

Ara, seleccionem CSV i vegem què rebrem. Simplement tria CSV i prem el botó 'Exportar'.

![seleccionar format de fitxer](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Un cop completada l'exportació, veuràs una alerta amb dues opcions. Tocar 'Mostrar fitxer' revelarà el fitxer resultant al teu directori de documents.

![exportació completada](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Ara pots enviar aquest fitxer, obrir-lo en un editor de text extern o utilitzar-lo per actualitzar el teu progrés d'escolta a [Last.fm](http://Last.fm).

![carpeta d'exportació amb fitxers de resultats](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

El fitxer CSV de sortida contindrà camps en el format següent:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Per exemple:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![fitxer csv exportat](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## Format TXT

El fitxer TXT de sortida contindrà camps en el format següent:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Per exemple:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![fitxer txt exportat](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## Format M3U

A continuació, et guiarem a través de l'exportació de la teva llista de reproducció a format M3U, que és l'estàndard de facto per a fitxers de llistes de reproducció. La condició prèvia principal per a una exportació exitosa de la llista de reproducció és que tots els fitxers de la llista de reproducció han d'estar ubicats al mateix emmagatzematge, ja sigui en un servei al núvol com Google Drive, fitxers locals o fitxers al teu dispositiu. Per començar el procés d'exportació, obre qualsevol llista de reproducció i toca el botó 'Més accions' a la cantonada superior dreta, després tria l'element del menú 'Exportar llista de cançons'.

![pantalla de llista de reproducció](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

A la pantalla següent, selecciona el format de fitxer 'M3U', on trobaràs dues opcions per a 'Tipus d'ubicació del fitxer multimèdia':

![pantalla de selecció de format de fitxer d'exportació](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Si tries 'Camí relatiu', la llista de reproducció es crearà amb les ubicacions dels fitxers multimèdia escrites de forma relativa al fitxer de la llista de reproducció. Per exemple:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   En aquest cas, evita canviar la ubicació del fitxer M3U després de completar l'exportació, ja que fer-ho trencarà els camins dels fitxers multimèdia. Per començar la reproducció de la teva llista de reproducció, simplement toca el fitxer de la llista de reproducció exportat i l'aplicació localitzarà automàticament els fitxers multimèdia al teu emmagatzematge i iniciarà la reproducció. O fins i tot pots exportar les teves llistes de reproducció a l'emmagatzematge i després importar-les de nou al teu nou dispositiu.

2. Si tries 'URL absolut', l'aplicació generarà URLs directes per als teus fitxers multimèdia. Això et permet reproduir la llista de reproducció en qualsevol dispositiu/aplicació sense necessitat que tots els fitxers multimèdia estiguin ubicats al mateix emmagatzematge que el fitxer de la llista de reproducció. Aquesta opció només és compatible amb l'emmagatzematge al núvol capaç de generar URLs directes de fitxers. No obstant això, tingues en compte que en alguns casos, les URLs generades poden tenir una vida útil limitada i poden caducar després d'un temps. Aquí tens la llista de serveis al núvol compatibles: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (si és en mode convidat)  

L'URL del fitxer multimèdia de sortida serà alguna cosa com:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Un cop hagis seleccionat el 'Tipus d'ubicació del fitxer multimèdia', toca 'Exportar'. L'aplicació et demanarà que triïs una carpeta de destinació per exportar el fitxer M3U. Toca 'Fet' per confirmar la teva selecció.

![seleccionar una carpeta](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

L'aplicació generarà un fitxer M3U i el pujarà/mourà a la carpeta de destinació.

![pujant fitxer m3u](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Un cop completada l'exportació, apareixerà una alerta del sistema amb l'opció de 'Mostrar fitxer'.

![alerta d'exportació completada](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Tocar això revelarà el fitxer exportat a l'aplicació.

![fitxer m3u exportat a la llista de fitxers](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Si has seleccionat 'Camí relatiu' com a 'Tipus d'ubicació del fitxer multimèdia' al pas anterior, el fitxer de sortida serà en el format següent:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![exemple m3u amb camins relatius](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Per a l'opció 'URL absolut', l'aplicació generarà un fitxer M3U en el format:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![exemple m3u amb URLs absolutes de fitxers](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Pots obrir aquest fitxer en qualsevol dispositiu/aplicació que admeti llistes de reproducció M3U.

![llista de reproducció m3u oberta en una aplicació externa](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Reflexions finals

Exportar les teves pistes d'Evermusic i Flacbox et dona un control complet sobre les teves dades musicals. Tant si fas còpies de seguretat del teu historial d'escolta, scrobbling a Last.fm o gaudeixes de llistes de reproducció en dispositius externs, aquestes opcions d'exportació: M3U, CSV i TXT - són eines potents dissenyades per a la flexibilitat i la compatibilitat. Aprofita aquestes funcions per millorar la manera com organitzes, comparteixes i tornes a visitar la teva col·lecció de música a través de les plataformes.

## Preguntes freqüents

{{% details title="Quin format d'exportació hauria d'utilitzar per al scrobbling de Last.fm?" closed="true" %}}
Utilitza CSV. Inclou marques de temps i metadades completes requerides per eines de scrobbling com Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Puc exportar qualsevol col·lecció de pistes, no només llistes de reproducció?" closed="true" %}}
Sí. Pots exportar recents, favorits, àlbums, llistes de reproducció i qualsevol altra col·lecció de pistes a l'aplicació utilitzant els mateixos passos.
{{% /details %}}

{{% details title="Funcionarà la meva llista de reproducció M3U en altres dispositius?" closed="true" %}}
Si tries l'opció d'URL absolut durant l'exportació, el fitxer M3U es pot reproduir en qualsevol dispositiu que admeti llistes de reproducció M3U. Tingues en compte que algunes URLs al núvol poden caducar amb el temps.
{{% /details %}}

{{% details title="La funció d'exportació és gratuïta?" closed="true" %}}
Sí. L'exportació de col·leccions de pistes a M3U, CSV i TXT està disponible tant a les versions gratuïtes com premium d'Evermusic i Flacbox.
{{% /details %}}

{{% details title="Quins serveis al núvol admeten l'exportació d'URL absolut?" closed="true" %}}
L'exportació d'URL absolut és compatible amb iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive i WebDAV (mode convidat).
{{% /details %}}
