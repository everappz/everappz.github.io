---
title: "Bibliothèque musicale"
date: 2020-02-01
description: "Apprenez à créer, organiser et synchroniser votre bibliothèque musicale dans Flacbox sur iPhone, iPad et Mac. Ajoutez des pistes manuellement ou synchronisez depuis des services cloud, gérez les métadonnées, les pochettes d'album, les listes de lecture, les favoris, les récents et les signets. Inclut la prise en charge audio haute résolution, l'éditeur de balises MusicBrainz, la synchronisation en ligne et hors ligne, et les options de personnalisation."
keywords: [
  "bibliothèque musicale Flacbox", "synchroniser musique depuis le nuage", "organiser les métadonnées musicales",
  "modifier les balises audio Flacbox", "synchronisation musique hors ligne", "importer musique locale",
  "gestion des listes de lecture Flacbox", "recherche pochette album Flacbox",
  "métadonnées musicales iPhone", "guide application Flacbox",
  "Flacbox MusicBrainz", "normaliser les balises Flacbox",
  "bibliothèque musicale haute résolution Flacbox", "bibliothèque Flacbox FFmpeg",
  "albums solos Flacbox", "vue compositeur Flacbox"
]
tags: ["musique", "guide", "flacbox", "bibliothèque"]
readingTime: 11
---


Gérer votre bibliothèque musicale est un jeu d'enfant avec Flacbox, qui vous permet d'organiser sans effort toutes vos pistes — FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE et des dizaines d'autres formats locaux — dans une collection unique et consultable. Vous avez deux options pour constituer votre bibliothèque musicale : l'ajout manuel (vous choisissez exactement ce qui est ajouté) ou la synchronisation automatique (Flacbox analyse les dossiers cloud désignés et ajoute automatiquement les nouveaux fichiers au fur et à mesure qu'ils apparaissent).

{{< cards cols="1">}}
  {{< card title="" subtitle="Vue Albums de la bibliothèque musicale Flacbox" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Ajout manuel

Pour ajouter des pistes manuellement, appuyez sur l'icône **Ajouter de la musique** située dans le coin supérieur gauche et choisissez des dossiers ou des fichiers depuis un service de stockage en nuage connecté ou des fichiers situés sur votre appareil. Lorsque vous ajoutez des pistes à la bibliothèque, seuls des liens vers ces pistes sont créés — les fichiers réels restent dans leurs emplacements d'origine pour économiser l'espace disque précieux. Si vous souhaitez rendre des pistes disponibles hors ligne, vous pouvez utiliser l'action Télécharger du menu options ou activer le mode hors ligne pour les listes de lecture et les collections de pistes.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — Ajouter des chansons à la bibliothèque musicale" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

Vous pouvez également glisser-déposer des fichiers dans la bibliothèque sur la version Mac, ou utiliser **Ouvrir des fichiers…** / **Ouvrir un dossier…** depuis le sélecteur de fichiers système sur iPhone et iPad.

## Reprendre la lecture

Restaurez la file de l'audio player depuis la dernière position enregistrée si cette fonctionnalité est activée dans les paramètres de l'application. Activez à la fois **Enregistrer l'état de l'audio player** et **Enregistrer la position de lecture** dans Paramètres → Audio Player → Général pour une expérience optimale. Une fois activé, un bouton **Reprendre la lecture** apparaît en haut de chaque écran de dossier, album, artiste, genre et liste de lecture — appuyez dessus pour revenir directement à la piste exacte et à la position où vous vous étiez arrêté.

## Emplacements

Toutes les pistes de votre bibliothèque sont regroupées par type de source et balises musicales. Vous pouvez filtrer les chansons par emplacement en utilisant le bouton **Plus d'actions** dans le coin supérieur droit et en sélectionnant **Filtrer**.

### Musique en ligne

Cette section présente la musique de vos services de stockage en nuage connectés. Les pistes ici sont diffusées à la demande ; rien n'occupe le stockage local jusqu'à ce que vous téléchargiez explicitement ou activiez le mode hors ligne.

### Fichiers dans cette application

Vous pouvez y trouver la musique disponible pour une lecture hors ligne, provenant de vos fichiers locaux. Cela inclut les fichiers dans le répertoire Documents de l'application — tout ce que vous avez téléchargé, transféré via Wi-Fi Drive ou importé via Finder File Sharing.

### Fichiers sur cet iPhone / iPad / Mac

Cette catégorie inclut la musique importée dans l'application depuis votre appareil, ajoutée via la boîte de dialogue système **Ouvrir des fichiers…**. Les fichiers originaux restent dans leur emplacement d'origine ; Flacbox conserve simplement un lien vers eux.

## Catégories

Lorsque vous ajoutez des pistes à votre bibliothèque musicale, l'application lit automatiquement leurs balises audio et les organise en catégories telles que Chansons, Chansons non lues, Albums, Artistes d'albums, Artistes, Genres et Compositeurs.

## Regroupement par balises

Ces catégories vous aident à organiser vos pistes par balises musicales. Lorsque vous ajoutez des pistes à la bibliothèque musicale, l'application lit leurs métadonnées et les regroupe par ces catégories. Si vous ne voyez pas tous vos albums, assurez-vous que l'application a analysé chaque piste. Vous pouvez vérifier la progression de l'analyse dans Paramètres → Bibliothèque musicale → Lecture des métadonnées → Nombre de fichiers traités dans la bibliothèque musicale. Pour les fichiers locaux, vous pouvez également relancer l'analyse des dossiers hors ligne dans Paramètres → Bibliothèque musicale → Synchronisation des dossiers hors ligne → Démarrer l'analyse des dossiers locaux. Une fois que le lecteur de métadonnées a terminé toutes les opérations, vous verrez les catégories suivantes dans votre bibliothèque musicale :

- **Chansons** — toutes les chansons regroupées par la balise TRACK_TITLE. Vous pouvez vérifier l'ordre de tri dans le menu Plus d'actions dans le coin supérieur droit.
- **Chansons non lues** — toutes les chansons qui n'ont jamais été lues.
- **Albums** — chansons regroupées par la balise ALBUM_NAME, en ignorant les balises d'artiste, d'artiste d'album et de compositeur. Si vous avez plusieurs albums avec le même nom mais des artistes différents, envisagez d'utiliser le tri Albums exclusifs décrit ci-dessous.
- **Artistes d'albums** — chansons regroupées uniquement par la balise ALBUM_ARTIST_TAG. Utile pour séparer clairement les compilations et collaborations du travail en solo.
- **Artistes** — chansons regroupées uniquement par la balise ARTIST_TAG.
- **Genres** — chansons regroupées par la balise GENRE.
- **Compositeurs** — chansons regroupées par la balise COMPOSER — inestimable pour les bibliothèques de musique classique où «&nbsp;compositeur&nbsp;» est le principal axe de navigation.

## Favoris

Vous pouvez marquer des chansons comme favorites sur l'écran de l'audio player ou via le menu options. Les favoris apparaissent dans leur propre section pour que vous puissiez les trouver en un seul appui.

## Récents

Cette section affiche toutes les pistes récemment lues. Vous pouvez personnaliser le nombre d'éléments conservés dans la liste des récents dans Paramètres → Bibliothèque → Récents → Modifier la taille de la liste, et exporter la liste vers M3U / CSV / TXT pour sauvegarder votre historique d'écoute.

## Signets

Vous pouvez créer des signets audio pendant qu'une chanson est en cours de lecture et les gérer sur cet écran — parfait pour les livres audio, les longs mixages, les conférences ou simplement pour marquer le refrain d'une piste préférée. Des instructions détaillées sur l'utilisation des signets audio sont disponibles [ici](/docs/guide/evermusic/evermusic-guide-music-library).

## Barre d'outils supérieure

Située juste sous la barre de navigation, la barre d'outils supérieure propose plusieurs actions pratiques : Rechercher, Tout lire, Tout mélanger et Reprendre la lecture. Vous pouvez afficher ou masquer cette barre d'outils d'un simple geste de balayage vers le bas.

## Recherche

La fonctionnalité de recherche vous permet de localiser une piste, un artiste, un album ou un genre spécifique dans votre bibliothèque musicale. Dans l'écran de recherche, vous avez accès aux actions Trier, Filtrer et vue Grille / Liste. La recherche s'effectue localement dans la base de données de la bibliothèque musicale, ce qui lui permet de fonctionner entièrement hors ligne et de renvoyer des résultats au fur et à mesure que vous tapez.

{{< cards cols="1">}}
  {{< card title="" subtitle="Recherche dans la bibliothèque musicale Flacbox" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Menu Options

Chaque chanson de votre bibliothèque musicale dispose d'un menu avec plus d'actions, accessible en appuyant sur le bouton à trois points près du titre de la chanson. Ces actions varient selon qu'il s'agit d'une chanson individuelle ou d'une collection.

### Pour les chansons individuelles

- **Lire ensuite** — ajoute la chanson en haut de la file de l'audio player.
- **Lire plus tard** — ajoute la chanson en bas de la file de l'audio player.
- **Ajouter à une liste de lecture** — ajoute la chanson à une liste de lecture.
- **Ajouter aux favoris** — marque la chanson comme favorite pour un accès rapide.
- **Télécharger** — enregistre la chanson dans les fichiers locaux. Elle apparaît dans l'onglet **Fichiers locaux** et la section **Musique hors ligne**.
- **Modifier les balises audio** — ouvre l'éditeur de balises audio intégré pour corriger les métadonnées manquantes ; notez que cela modifiera la chanson dans votre stockage.
- **Afficher dans le dossier** — révèle le dossier où le fichier audio est stocké.
- **Afficher dans le Finder** — pour les fichiers importés depuis votre Mac, cette action révèle le dossier où se trouve le fichier audio sur votre Mac.
- **Ouvrir dans** — exporte le fichier audio vers une autre application.
- **Supprimer du service cloud** — supprime le fichier de la bibliothèque musicale et du stockage cloud. **Cette action est irréversible.**
- **Supprimer de la bibliothèque musicale** — supprime la chanson de votre bibliothèque musicale, mais le fichier reste dans le stockage. Si la synchronisation automatique est activée et que le fichier existe sur le stockage distant, il réapparaîtra dans votre bibliothèque après une opération de synchronisation.

### Pour les collections de chansons

Pour les collections de chansons telles que les Albums, Artistes, Genres ou Compositeurs, le menu options inclut les actions suivantes.

- **Tout lire** — remplace la file de l'audio player par les chansons de la collection sélectionnée.
- **Lire ensuite** — ajoute les chansons de cette collection en haut de la file de l'audio player.
- **Lire plus tard** — ajoute les chansons de cette collection en bas de la file de l'audio player.
- **Ajouter à une liste de lecture** — inclut les chansons de cette collection dans une liste de lecture, avec la possibilité d'en créer une nouvelle.
- **Activer le mode hors ligne** — télécharge les chansons de cette collection dans les fichiers locaux. Les fichiers apparaissent dans l'onglet **Fichiers locaux** et la section **Musique hors ligne**. Si de nouveaux éléments sont ajoutés à la collection sur le serveur, ils seront téléchargés automatiquement.
- **Modifier l'image** — modifier la pochette d'album pour la collection de chansons.
- **Ajouter à l'archive** — regrouper toute la collection dans un seul fichier ZIP pour une sauvegarde ou un transfert facile (fonctionnalité Premium).
- **Exporter la liste des chansons** — exporter la collection vers M3U, CSV ou TXT pour une utilisation dans d'autres lecteurs ou pour l'archivage.
- **Supprimer de la bibliothèque musicale** — supprime la collection de chansons de votre bibliothèque musicale. Cette action ne supprime pas les fichiers réels du stockage. Si la synchronisation automatique est activée et que les fichiers existent sur le stockage distant, ils réapparaîtront dans votre bibliothèque après une opération de synchronisation.

## Mode de sélection

Vous pouvez activer le mode de sélection via le bouton Plus d'actions dans le coin supérieur droit. Dans ce mode, vous pouvez sélectionner plusieurs pistes à la fois et effectuer des actions par lot — ajouter à une liste de lecture, marquer comme favori, supprimer de la bibliothèque, télécharger, et plus encore.

## Détail d'un album

Lorsque vous ouvrez les sections Artiste, Artiste d'album ou Compositeur, vous pouvez voir un sélecteur pour Chansons / Tous les albums / Albums exclusifs / Albums solos.

- **Chansons** — affiche toutes les chansons où cet Artiste / Artiste d'album / Compositeur apparaît dans les balises audio.
- **Tous les albums** — affiche les albums de compilation et tous les albums où l'artiste est présent.
- **Albums exclusifs** — affiche les albums où l'artiste spécifié est le seul artiste avec ce nom d'album.
- **Albums solos** — affiche les albums où apparaissent uniquement les pistes de l'artiste spécifié, même si d'autres artistes ont des albums portant le même nom.

Cela est particulièrement utile pour nettoyer les compilations «&nbsp;Artistes divers&nbsp;» encombrées dans les grandes bibliothèques.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — Écran de détail d'un album" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Paramètres

Appuyez sur Plus d'actions → Paramètres pour configurer vos préférences de bibliothèque musicale.

### Lecture des métadonnées

Lorsque vous ajoutez des pistes à la bibliothèque, le lecteur de métadonnées se met au travail. Ce processus en arrière-plan lit toutes les métadonnées de vos pistes et les organise par Artiste, Album, Genre et Compositeur. Vous pouvez ajuster la vitesse de lecture des métadonnées pour charger les données plus rapidement — sachez que la lecture plus rapide consomme plus d'énergie. Vous pouvez également désactiver entièrement le lecteur de métadonnées et afficher les noms de fichiers à la place des informations de balise.

Il est important de noter que le lecteur de métadonnées met uniquement à jour les métadonnées dans votre bibliothèque musicale et ne modifie pas les fichiers stockés dans votre compte cloud ou dans le stockage local. Si vous souhaitez modifier les métadonnées des fichiers audio, vous pouvez le faire à l'aide de l'éditeur de balises intégré, que vous pouvez activer depuis l'action correspondante dans le menu options.

### Modes disponibles pour le lecteur de métadonnées

- **Désactivé** — le lecteur de métadonnées est désactivé et les noms de fichiers sont affichés à la place des données de balises audio.
- **Chanson actuelle** — l'application lit les métadonnées uniquement pour la chanson en cours de lecture. Utilisez cette option si vous avez une connexion réseau lente pour éviter que le lecteur de métadonnées n'envoie de nombreuses requêtes au serveur cloud, ce qui pourrait provoquer des interruptions de lecture.
- **File de lecture** — l'application lit les métadonnées pour toutes les chansons dans la file de l'audio player.
- **Bibliothèque** — l'application lit les métadonnées pour toutes les chansons de la bibliothèque musicale.

Lorsque le commutateur **Lecture des métadonnées en arrière-plan** est activé, le lecteur de métadonnées continue de fonctionner en mode arrière-plan. Notez que si l'application consomme beaucoup d'énergie pendant la lecture audio, le système d'exploitation iOS peut la suspendre.

Ainsi, si vous disposez d'une grande collection de musique, il est conseillé d'utiliser la version de bureau de l'application pour la synchronisation des métadonnées. Vous pouvez ensuite utiliser la fonctionnalité de sauvegarde et restauration des données dans les paramètres de l'application pour transférer la bibliothèque synchronisée du bureau vers le mobile.

Lorsque l'option **Normaliser l'encodage des métadonnées** est activée, l'application normalise automatiquement l'encodage des métadonnées pour toutes les chansons de la bibliothèque musicale. Cela corrige les problèmes où l'encodage des balises audio est cassé (par exemple après avoir modifié des fichiers sur un PC Windows) et empêche l'affichage de caractères incorrects dans les informations de piste.

L'action **Recharger les métadonnées** marque chaque fichier de votre bibliothèque musicale comme ayant des métadonnées manquantes, déclenchant ainsi le lecteur de métadonnées pour actualiser chaque enregistrement.

Appuyez sur **Démarrer la lecture des métadonnées** pour déclencher le lecteur manuellement. La progression de l'opération s'affiche ci-dessous.

### Synchronisation en ligne

La synchronisation automatique de musique en ligne vous permet d'ajouter automatiquement des pistes depuis les services cloud connectés à la bibliothèque musicale. Pour activer cette fonctionnalité, accédez aux Paramètres de la bibliothèque musicale et sélectionnez les dossiers de synchronisation.

Avec cette option activée, l'application analyse tous les dossiers sélectionnés, identifie les fichiers audio pris en charge et les intègre de manière transparente dans votre bibliothèque. Vous pouvez démarrer ou arrêter la synchronisation en appuyant sur l'action de menu correspondante.

La synchronisation de musique en ligne fonctionne exclusivement lorsque l'application est au premier plan, ce qui signifie que la synchronisation d'une grande bibliothèque peut prendre du temps. Pour accélérer le processus, laissez votre application ouverte, connectez-la à une source d'alimentation et activez Écran → Toujours actif dans les paramètres de l'application.

Vous pouvez également effectuer la synchronisation de musique en ligne sur la version de bureau de l'application et transférer la bibliothèque musicale vers la version iOS à l'aide de la fonctionnalité Sauvegarde et restauration.

Vous pouvez également définir la fréquence de synchronisation de votre bibliothèque musicale en ligne. Si vous définissez l'intervalle sur Immédiatement, la synchronisation en ligne démarrera chaque fois que vous ouvrirez l'application.

### Synchronisation hors ligne

Ici, vous pouvez configurer la synchronisation de musique hors ligne.

#### Dossiers hors ligne synchronisés

Lorsque vous rendez un dossier cloud disponible hors ligne (via le menu Plus d'actions), il apparaît dans la section Fichiers locaux → Dossiers hors ligne. L'application télécharge son contenu sur votre appareil. Si vous apportez des modifications au dossier dans le nuage — comme ajouter, supprimer ou mettre à jour des fichiers — l'application détecte ces changements et met à jour la copie locale automatiquement.

Sur cet écran, vous pouvez démarrer manuellement la synchronisation des dossiers hors ligne, révéler le dossier hors ligne dans son dossier parent et désactiver le mode hors ligne pour le dossier. La désactivation du mode hors ligne supprime toutes les copies locales des fichiers de votre appareil.

#### Intervalle de temps

Vous pouvez définir l'intervalle de temps pour la fréquence à laquelle l'application doit vérifier les modifications dans les dossiers hors ligne.

#### Démarrer l'analyse des dossiers locaux

Cette option analyse tous les dossiers locaux situés dans le répertoire Documents de l'application pour trouver les fichiers audio pris en charge. Tous ces fichiers locaux sont ajoutés de manière transparente à votre bibliothèque musicale. Les fichiers locaux situés sur votre appareil mais en dehors de cette application doivent être ajoutés manuellement à la bibliothèque musicale, car l'application n'a pas accès aux fichiers en dehors du répertoire Documents de l'application en raison des restrictions de sécurité iOS / macOS.

#### Important

Il est conseillé de lancer périodiquement la synchronisation de musique hors ligne pour maintenir votre bibliothèque musicale à jour avec vos fichiers locaux.

### Personnalisation

Dans cette section, vous pouvez configurer le style de l'écran de la bibliothèque musicale selon vos préférences. Trois options sont disponibles : Menu simple, Menu groupé, Menu à onglets. Vous pouvez également activer ou désactiver l'affichage des pochettes d'album dans les écrans de détail d'album.

### Pochettes d'album

Ici, vous pouvez configurer la façon dont l'application charge et stocke les illustrations d'album.

- **Type de réseau** — choisissez Wi-Fi ou Wi-Fi et données cellulaires pour les téléchargements de pochettes.
- **Charger les pochettes pour les fichiers en ligne** — lorsque cette option est activée, les pochettes d'album intégrées sont chargées pour les fichiers stockés dans le stockage cloud. Cela peut utiliser des données réseau supplémentaires.
- **Rechercher dans le dossier** — lorsque cette option est activée, si une piste n'a pas de pochette intégrée, l'application recherche des images JPEG ou PNG dans le même dossier et les utilise comme illustration d'album.
- **Qualité des pochettes** — choisissez la qualité des pochettes d'album stockées sur votre appareil.
- **Afficher dans le dossier** — ouvrir le dossier où les pochettes d'album sont mises en cache pour vous permettre de les gérer ou de les sauvegarder.
- **Tout supprimer** — supprimer les pochettes d'album mises en cache pour libérer de l'espace de stockage et forcer l'application à les recharger à la demande.

Par défaut, l'application vérifie la présence de pochettes d'album intégrées dans vos pistes et les affiche si elles sont disponibles. S'il n'y a pas d'illustrations d'album intégrées et que l'option **Rechercher dans le dossier** est activée, l'application vérifie le dossier parent pour des images JPEG ou PNG et les utilise comme illustration d'album pour toutes les pistes de ce dossier.

### Listes de lecture

Vous pouvez activer l'option d'ajout de la même chanson à une liste de lecture deux fois. Par défaut, cette option est désactivée.

### Récents

Vous pouvez gérer votre liste de chansons récemment lues.

- **Supprimer la liste** — supprimer toute la liste des chansons récemment lues.
- **Modifier la taille de la liste** — définir le nombre d'éléments qui apparaissent dans la liste.
- **Exporter la liste des chansons** — exporter votre liste de chansons récemment lues vers M3U, CSV ou TXT. Des instructions détaillées sont disponibles [ici](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoris

Vous pouvez gérer la liste de vos chansons favorites.

- **Modification simultanée** — lorsque cette option est activée, l'ajout d'une chanson aux favoris l'ajoute à la fois dans la bibliothèque musicale et dans la section fichiers en même temps.
- **Supprimer la liste** — supprimer toute la liste des chansons favorites.
- **Exporter la liste des chansons** — comme pour les Récents, exporter la liste des favoris vers M3U, CSV ou TXT.

### Supprimer la bibliothèque

Cette action effacera la base de données de la bibliothèque musicale, mais laissera vos fichiers musicaux intacts dans le stockage.

### Limite de chargement du contenu

Par défaut, l'application utilise la pagination pour réduire le temps de chargement du contenu et maintenir la réactivité des grandes bibliothèques. Cependant, vous pouvez désactiver cette option et permettre à l'application de charger toutes les données disponibles en une seule fois. Pour ce faire, ouvrez les paramètres de l'application, faites défiler jusqu'à Personnalisation → Limite de chargement du contenu et choisissez Désactivé.
