---
title: "Comment exporter une collection de pistes en M3U, CSV et TXT dans Evermusic et Flacbox"
date: 2024-01-31
description: "Découvrez comment exporter vos récents, favoris, playlists et albums depuis Evermusic et Flacbox aux formats M3U, CSV ou TXT. Idéal pour le scrobbling Last.fm et la lecture sur d'autres appareils."
keywords: ["exportation evermusic", "exportation flacbox", "exporter en m3u", "exporter playlist en csv", "m3u txt csv playlist", "exportation musique"]
tags: ["evermusic", "récents", "favoris", "exportation", "m3u", "playlist", "csv", "txt", "album"]
---

{{< author-byline >}}


**En bref :** Evermusic et Flacbox vous permettent d'exporter n'importe quelle collection de pistes (Récents, Favoris, playlists, albums) en fichiers CSV, TXT ou M3U. Utilisez ces exports pour scrobbler sur Last.fm, sauvegarder votre bibliothèque ou lire vos playlists sur d'autres appareils.

## Introduction

Exporter vos récents, favoris, albums et playlists depuis l'application vers un fichier externe peut être extrêmement utile. Vous pouvez utiliser ces fichiers pour mettre à jour votre historique d'écoute sur des services de scrobbling comme [Last.fm](http://Last.fm) ou écouter vos playlists sur des appareils externes. Avec Evermusic et Flacbox, ce processus est simple. Nous allons vous montrer ici comment exporter vos récents en CSV/TXT et vos playlists en M3U. Cependant, cette fonctionnalité est disponible pour toute collection de pistes dans l'application.

## Choisir le format

Pour exporter vos récents, ouvrez la section 'Bibliothèque musicale' et sélectionnez l'élément de menu 'Récents'.

![bibliothèque musicale](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Sur l'écran suivant, appuyez sur le bouton 'Plus' dans le coin supérieur droit et choisissez 'Exporter la liste de morceaux'.

![exporter les récents](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

Sur l'écran 'Sélectionner le format de fichier', vous avez plusieurs options - CSV, TXT, M3U.

- CSV

Cela signifie Comma-Separated Values (valeurs séparées par des virgules), parfait pour organiser vos données dans un format de tableau ordonné. Dans le fichier de destination, vous trouverez des paramètres comme le nom de l'artiste, le nom de l'album, le nom de la piste, l'horodatage (le moment où vous avez écouté les pistes), le nom de l'artiste de l'album et la durée de la piste. Vous pouvez utiliser ce fichier ultérieurement pour mettre à jour votre historique d'écoute sur des services de scrobbling comme [Last.fm](http://Last.fm), comme décrit [ici](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Ici, nous parlons d'un fichier texte brut. C'est simple et direct, avec des paramètres incluant le nom de l'artiste, le nom de l'album, le nom de la piste et la durée. Utile si vous avez simplement besoin d'une liste de pistes en format texte.

- M3U

Ce format est essentiellement le choix par défaut pour créer des playlists. Il est excellent car vous pouvez exporter votre liste de morceaux et profiter de vos pistes sur n'importe quel appareil, même si vous n'avez pas les fichiers originaux (si vous sélectionnez l'option URL absolue pour l'exportation des fichiers média). Dans le fichier de sortie, vous trouverez des paramètres tels que la durée, le nom de l'artiste, le nom de la piste et l'emplacement du fichier média.

## Format CSV

Maintenant, sélectionnons CSV et voyons ce que nous obtenons. Choisissez simplement CSV et appuyez sur le bouton 'Exporter'.

![sélectionner le format de fichier](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Une fois l'exportation terminée, vous verrez une alerte avec deux options. Appuyer sur 'Afficher le fichier' révélera le fichier résultant dans votre répertoire de documents.

![exportation terminée](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Vous pouvez maintenant envoyer ce fichier, l'ouvrir dans un éditeur de texte externe ou l'utiliser pour mettre à jour votre progression d'écoute sur [Last.fm](http://Last.fm).

![dossier d'exportation avec les fichiers résultants](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

Le fichier CSV de sortie contiendra des champs dans le format suivant :

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Par exemple :

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![fichier csv exporté](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## Format TXT

Le fichier TXT de sortie contiendra des champs dans le format suivant :

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Par exemple :

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![fichier txt exporté](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## Format M3U

Ensuite, nous vous guiderons dans l'exportation de votre playlist au format M3U, qui est le standard de facto pour les fichiers de playlist. La condition principale pour une exportation de playlist réussie est que tous les fichiers de la playlist doivent être situés sur le même stockage, qu'il s'agisse d'un service cloud comme Google Drive, de fichiers locaux ou de fichiers sur votre appareil. Pour commencer le processus d'exportation, ouvrez n'importe quelle playlist et appuyez sur le bouton 'Plus' dans le coin supérieur droit, puis choisissez l'élément de menu 'Exporter la liste de morceaux'.

![écran de playlist](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Sur l'écran suivant, sélectionnez le format de fichier 'M3U', où vous rencontrerez deux options pour le 'Type d'emplacement du fichier média' :

![écran de sélection du format d'exportation](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Si vous choisissez 'Chemin relatif', la playlist sera créée avec les emplacements des fichiers média écrits relativement au fichier de playlist. Par exemple :

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   Dans ce cas, évitez de changer l'emplacement du fichier M3U après la fin de l'exportation, car cela cassera les chemins des fichiers média. Pour commencer la lecture de votre playlist, appuyez simplement sur le fichier de playlist exporté, et l'application localisera automatiquement les fichiers média sur votre stockage et lancera la lecture. Vous pouvez même exporter vos playlists vers le stockage puis les importer à nouveau sur votre nouvel appareil.

2. Si vous choisissez 'URL absolue', l'application générera des URL directes pour vos fichiers média. Cela vous permet de lire la playlist sur n'importe quel appareil/application sans avoir besoin que tous les fichiers média soient situés sur le même stockage que le fichier de playlist. Cette option n'est prise en charge que pour les stockages cloud capables de générer des URL directes de fichiers. Cependant, gardez à l'esprit que dans certains cas, les URL générées peuvent avoir une durée de vie limitée et expirer après un certain temps. Voici la liste des services cloud pris en charge : iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (en mode invité)  

L'URL du fichier média de sortie ressemblera à quelque chose comme :

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Une fois que vous avez sélectionné le 'Type d'emplacement du fichier média', appuyez sur 'Exporter'. L'application vous demandera de choisir un dossier de destination pour l'exportation du fichier M3U. Appuyez sur 'Fait' pour confirmer votre sélection.

![sélectionner un dossier](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

L'application générera un fichier M3U et le téléchargera/déplacera vers le dossier de destination.

![téléchargement du fichier m3u](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Une fois l'exportation terminée, une alerte système apparaîtra avec l'option 'Afficher le fichier'.

![alerte exportation terminée](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Appuyer dessus révélera le fichier exporté dans l'application.

![fichier m3u exporté dans la liste des fichiers](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Si vous avez sélectionné 'Chemin relatif' comme 'Type d'emplacement du fichier média' à l'étape précédente, le fichier de sortie sera dans le format suivant :

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![exemple m3u avec chemins relatifs](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Pour l'option 'URL absolue', l'application générera un fichier M3U dans le format :

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![exemple m3u avec URL absolues de fichiers](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Vous pouvez ouvrir ce fichier sur n'importe quel appareil/application prenant en charge les playlists M3U.

![playlist m3u ouverte dans une application externe](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Réflexions finales

Exporter vos pistes depuis Evermusic et Flacbox vous donne un contrôle total sur vos données musicales. Que vous sauvegardiez votre historique d'écoute, scrobbliez sur Last.fm ou profitiez de playlists sur des appareils externes, ces options d'exportation : M3U, CSV et TXT - sont des outils puissants conçus pour la flexibilité et la compatibilité. Profitez de ces fonctionnalités pour améliorer la façon dont vous organisez, partagez et retrouvez votre collection musicale sur toutes les plateformes.

## FAQ

{{% details title="Quel format d'exportation dois-je utiliser pour le scrobbling Last.fm ?" closed="true" %}}
Utilisez CSV. Il inclut les horodatages et les métadonnées complètes requises par les outils de scrobbling comme Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Puis-je exporter n'importe quelle collection de pistes, pas seulement les playlists ?" closed="true" %}}
Oui. Vous pouvez exporter les récents, les favoris, les albums, les playlists et toute autre collection de pistes dans l'application en suivant les mêmes étapes.
{{% /details %}}

{{% details title="Ma playlist M3U fonctionnera-t-elle sur d'autres appareils ?" closed="true" %}}
Si vous choisissez l'option URL absolue lors de l'exportation, le fichier M3U peut être lu sur n'importe quel appareil prenant en charge les playlists M3U. Notez que certaines URL cloud peuvent expirer avec le temps.
{{% /details %}}

{{% details title="La fonctionnalité d'exportation est-elle gratuite ?" closed="true" %}}
Oui. L'exportation des collections de pistes en M3U, CSV et TXT est disponible dans les versions gratuites et premium d'Evermusic et Flacbox.
{{% /details %}}

{{% details title="Quels services cloud prennent en charge l'exportation en URL absolue ?" closed="true" %}}
L'exportation en URL absolue est prise en charge pour iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive et WebDAV (mode invité).
{{% /details %}}
