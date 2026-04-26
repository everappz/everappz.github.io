---
title: "Comment importer une liste de lecture M3U dans Evermusic et Flacbox"
date: 2024-01-31
description: "Découvrez comment importer des fichiers de listes de lecture M3U, M3U8 et CUE depuis le cloud, le stockage local ou votre appareil dans Evermusic et Flacbox."
keywords: ["evermusic", "flacbox", "liste de lecture", "m3u", "m3u8", "cue", "importer", "application musique"]
tags: ["evermusic", "importer", "listes de lecture", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Résumé :** Evermusic et Flacbox prennent en charge l'importation de fichiers de listes de lecture M3U, M3U8 et CUE depuis le stockage cloud, les fichiers locaux de l'application ou votre appareil. Allez dans Listes de lecture > Plus > Importer une liste de lecture, sélectionnez une source, choisissez votre fichier, et l'application crée votre liste de lecture automatiquement.

M3U, qui signifie MP3 URL ou Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, est un format de fichier informatique utilisé pour les listes de lecture multimédia. L'une de ses utilisations principales est la création de fichiers de listes de lecture à entrée unique pointant vers des flux sur Internet. Ces fichiers offrent un accès pratique au contenu en streaming et sont couramment utilisés pour les téléchargements, les e-mails et l'écoute de la radio Internet.

Malgré son utilisation répandue, il n'existe pas de spécification formelle pour le format M3U ; il est devenu un standard de facto. Un fichier M3U est essentiellement un fichier texte brut qui spécifie les emplacements d'un ou plusieurs fichiers multimédia. Selon l'encodage, il est enregistré avec l'extension "m3u" ou "m3u8". Chaque entrée du fichier spécifie l'emplacement d'un fichier multimédia, qui peut être un chemin local absolu, un chemin local relatif à l'emplacement du fichier M3U ou une URL. Les entrées sont séparées par des sauts de ligne, certains appareils nécessitant des sauts de ligne représentés par CR LF.

De plus, les fichiers M3U peuvent inclure des commentaires préfixés par le caractère "#". Dans le M3U étendu, "#" introduit des directives M3U étendues, qui peuvent prendre en charge des paramètres terminés par deux-points ":".

Dans nos applications Evermusic et Flacbox, nous avons implémenté la fonctionnalité d'importation de fichiers M3U, éliminant le besoin de création manuelle de listes de lecture. Ce guide vous accompagnera dans l'importation de vos listes de lecture depuis le stockage cloud, les fichiers locaux ou les fichiers de votre appareil directement dans l'application.

Tout d'abord, accédez à la section 'Listes de lecture'. Ensuite, appuyez sur le bouton 'Plus' situé dans le coin supérieur droit. Dans le menu qui apparaît, sélectionnez l'option 'Importer une liste de lecture'.

![action d'importation de liste de lecture](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Sur l'écran suivant, choisissez l'emplacement du fichier. Les options prises en charge comprennent :

- Stockage cloud connecté ;
- Fichiers dans l'application ;
- Fichiers sur votre appareil ;

![sélectionner l'emplacement du fichier](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Sélectionnons le stockage cloud connecté et ouvrons le dossier contenant le fichier de liste de lecture. Les extensions de fichiers de listes de lecture prises en charge comprennent M3U, M3U8 et CUE. Sélectionnez le fichier de liste de lecture et appuyez sur 'Fait' pour confirmer votre sélection.

![sélectionner le fichier M3U](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

L'application analysera le fichier de liste de lecture et créera une liste de pistes. Elle localisera ensuite ces fichiers dans le stockage et compilera une liste de lecture finale qui sera importée dans la bibliothèque musicale. Il est crucial que votre fichier M3U/CUE contienne les chemins corrects vers les fichiers multimédia, et les fichiers doivent se trouver à ces chemins dans votre stockage.

![liste de lecture importée](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

L'application prend en charge les chemins relatifs et les URL de fichiers absolues.

Par exemple :

Liste de lecture avec des chemins relatifs :

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Liste de lecture avec des URL absolues :

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Si vous importez un fichier de liste de lecture situé dans l'application (section Fichiers locaux), aucune étape supplémentaire n'est nécessaire.

Cependant, si vous souhaitez importer une liste de lecture située sur votre appareil en utilisant le sélecteur de fichiers système, il y a une considération importante à garder à l'esprit.

En raison des politiques de sécurité, l'application ne peut accéder qu'au fichier que vous sélectionnez via le sélecteur de fichiers système. Cependant, le fichier de liste de lecture peut inclure des liens vers d'autres fichiers multimédia sur votre appareil. Pour importer une liste de lecture depuis votre appareil, vous devez sélectionner un dossier contenant à la fois le fichier de liste de lecture et tous les fichiers multimédia liés. Dans ce cas, l'application scannera le dossier sélectionné, trouvera le fichier de liste de lecture, construira la liste des pistes et l'importera dans la bibliothèque musicale.

De plus, vous pouvez importer plusieurs listes de lecture à la fois en appuyant sur le bouton "Plus d'actions" et en sélectionnant "Importer des listes de lecture depuis un dossier". L'application scannera alors le contenu du dossier, trouvera les fichiers de listes de lecture pris en charge et les importera dans la bibliothèque.

## Questions fréquemment posées

{{% details title="Quels formats de listes de lecture Evermusic et Flacbox prennent-ils en charge ?" closed="true" %}}
Les deux applications prennent en charge les formats de fichiers de listes de lecture M3U, M3U8 et CUE. Ceux-ci couvrent les standards de listes de lecture les plus courants utilisés par les lecteurs de musique et les logiciels multimédia.
{{% /details %}}

{{% details title="Puis-je importer des listes de lecture depuis le stockage cloud ?" closed="true" %}}
Oui. Vous pouvez importer des fichiers de listes de lecture depuis n'importe quel service de stockage cloud connecté, y compris Google Drive, Dropbox, OneDrive et les serveurs WebDAV.
{{% /details %}}

{{% details title="Pourquoi certaines pistes manquent-elles après l'importation ?" closed="true" %}}
Le fichier de liste de lecture doit contenir des chemins corrects vers vos fichiers multimédia, et ces fichiers doivent exister aux emplacements spécifiés dans votre stockage. Vérifiez que les chemins de fichiers dans votre fichier M3U ou CUE correspondent aux emplacements réels des fichiers.
{{% /details %}}

{{% details title="Puis-je importer plusieurs listes de lecture à la fois ?" closed="true" %}}
Oui. Utilisez le bouton Plus d'actions et sélectionnez "Importer des listes de lecture depuis un dossier". L'application scanne le dossier pour tous les fichiers de listes de lecture pris en charge et les importe en une seule étape.
{{% /details %}}

{{% details title="Dois-je créer les listes de lecture manuellement ?" closed="true" %}}
Non. La fonction d'importation élimine la création manuelle de listes de lecture. Pointez simplement l'application vers votre fichier M3U, M3U8 ou CUE existant et elle crée la liste de lecture automatiquement.
{{% /details %}}
