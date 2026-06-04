---
title: "Lecteur audio"
date: 2020-02-01
description: "Apprenez à utiliser le lecteur audio Flacbox sur iPhone, iPad et Mac. Contrôlez la lecture, gérez les files d'attente, configurez le moteur audio FFmpeg / système, modifiez le taux d'échantillonnage, la correction de hauteur tonale, la durée du tampon d'E/S, l'égaliseur, les signets audio, AirPlay 2, Google Cast, CarPlay, les widgets et les raccourcis clavier Mac."
keywords: [
  "guide lecteur Flacbox", "paramètres audio player", "égaliseur Flacbox",
  "streaming musique AirPlay", "musique Google Cast", "signets audio",
  "file de lecture Flacbox", "répétition mélange Flacbox", "contrôle volume Flacbox",
  "mini lecteur macOS", "application musique VoiceOver",
  "Flacbox FFmpeg", "correction hauteur tonale Flacbox", "taux d'échantillonnage Flacbox",
  "DAC externe Flacbox", "son surround Flacbox", "tampon E/S Flacbox",
  "vitesse de lecture Flacbox", "minuteur de sommeil Flacbox"
]
tags: ["guide", "flacbox", "lecteur"]
readingTime: 14
---


Le lecteur audio est l'écran principal de l'application où vous contrôlez la musique et la plupart des fonctionnalités de lecture. C'est également là que le moteur audio haute résolution de Flacbox — basé sur les codecs système et la bibliothèque **FFmpeg** intégrée — fait le gros du travail. Voyons comment l'utiliser.

## Accéder au lecteur audio

Vous pouvez accéder au lecteur plein écran depuis la barre du mini lecteur. Sur iPhone, le mini lecteur se trouve au bas de l'écran principal. Sur iPad et Mac, il est sur le côté gauche. Pour masquer le mini lecteur sur iPhone, appuyez dessus une fois et balayez vers le bas. Pour fermer complètement le lecteur plein écran, appuyez sur le bouton de fermeture dans le coin inférieur droit.

{{< cards cols="1">}}
  {{< card title="" subtitle="Écran principal du lecteur audio Flacbox" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Formats audio pris en charge

Flacbox lit les formats audio les plus populaires — à la fois les codecs système d'Apple et de nombreux formats supplémentaires gérés par le moteur FFmpeg intégré :

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

Cela couvre pratiquement tous les formats modernes avec et sans perte que vous êtes susceptible d'avoir dans une collection musicale personnelle.

## Commandes de lecture

Au bas de l'écran du lecteur, vous verrez des boutons pour Lire, Pause, Piste suivante et Piste précédente. Il y a également des boutons optionnels comme Avancer de 30 secondes et Reculer de 30 secondes que vous pouvez activer dans les paramètres de l'application (pratique pour les livres audio). Vous pouvez avancer ou reculer rapidement en maintenant les boutons Suivant / Précédent enfoncés. Pour accéder à une partie spécifique d'une piste, faites glisser le curseur de lecture.

## Répétition et mélange

Appuyez sur le bouton de répétition pour faire défiler les modes de répétition :

- **Répéter tout** — boucle sur toutes les pistes de votre file.
- **Répéter une** — répète uniquement la piste actuelle.
- **Répéter arrêt** — met en pause lorsque la piste actuelle se termine.
- **Pas de répétition** — lit la file une seule fois sans répétition.

Utilisez le bouton **Mélanger** pour aléatoiriser l'ordre des pistes dans la file.

## Contrôle du volume

Ouvrez l'écran Paramètres audio en appuyant sur l'icône de son sous les commandes de lecture pour accéder au curseur de volume. Vous y trouverez également des boutons pour **Google Cast** et **AirPlay** pour basculer rapidement la lecture vers un autre appareil.

## Google Cast (Chromecast)

Pour les utilisateurs de Google Cast, l'icône **Cast** apparaît au bas du lecteur. Appuyez dessus pour choisir un appareil et commencer la diffusion. Assurez-vous que votre appareil et le récepteur Google Cast sont sur le même réseau Wi-Fi. Remarque : tous les formats audio ne sont pas compatibles avec Google Cast — certains formats haute résolution peuvent nécessiter un transcodage.

## AirPlay

Pour AirPlay, recherchez le bouton **AirPlay** au bas du lecteur. Appuyez dessus et sélectionnez un appareil pour la diffusion. Flacbox prend en charge **AirPlay 2**, ce qui vous permet de lire sur plusieurs HomePods, Apple TV ou enceintes compatibles AirPlay 2 simultanément.

## Égaliseur audio

Flacbox inclut un **égaliseur à 10 bandes** avec des préréglages de style iPod. Appuyez sur Égaliseur dans la vue du volume, puis activez-le dans le coin supérieur droit. Vous pouvez utiliser des préréglages comme Acoustique et Renforcement des basses, ou ajuster chaque bande de fréquence avec des curseurs. Créez vos propres préréglages, enregistrez-les sous n'importe quel nom et augmentez le volume global avec le préamplificateur. Nous avons des instructions plus détaillées sur l'utilisation de l'égaliseur [ici](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Égaliseur du lecteur audio Flacbox" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Barre d'outils du mode lecteur

Pour certains styles de lecteur, il y a une barre d'outils dédiée en haut du lecteur plein écran. Cette barre d'outils contient trois boutons utiles :

- **Rechercher** — localiser rapidement une piste spécifique dans votre file de lecture.
- **Contrôle de la vitesse de lecture** — ajuster la vitesse de lecture de 0,02× à 3,00×. Parfait pour les livres audio, les podcasts et les conférences. Appuyez sur Normal pour revenir à la vitesse par défaut.
- **Signets audio** — créer plusieurs signets par piste. Nous avons des instructions complètes sur l'utilisation des signets [ici](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## File de lecture

Pour voir votre file de lecture, appuyez sur le bouton de file sur le côté droit de la chanson actuelle. Chaque chanson dans la file dispose de plus d'actions — appuyez sur les trois points pour les afficher. Pour réorganiser une chanson dans la file, utilisez l'indicateur de réorganisation près du titre et faites-le glisser vers une nouvelle position.

{{< cards cols="1">}}
  {{< card title="" subtitle="File de lecture Flacbox" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Commentaires / Paroles

Pour afficher les commentaires de piste et les paroles intégrées, ainsi que les fichiers LRC, suivez ces étapes :

1. Ouvrez **Paramètres**.
2. Accédez à **Audio Player**.
3. Sélectionnez **Personnalisation**.
4. Appuyez sur **Boutons sur l'écran principal**.
5. Activez **Commentaires**.

Après cela, appuyez plusieurs fois sur le bouton de file de l'audio player en bas de l'écran pour passer de la vue illustration / file à la vue commentaires. Sur l'écran Commentaires, faites défiler vers la droite pour basculer entre **Commentaires**, **Paroles intégrées** et le **Fichier LRC**. Des instructions complètes sont disponibles [ici](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Écran paroles et commentaires Flacbox" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Menu Options

Chaque chanson dans la file de l'audio player dispose d'un menu avec plus d'actions, accessible en appuyant sur le bouton à trois points près du titre de la chanson.

- **Lire ensuite** — ajoute la chanson en haut de la file de l'audio player.
- **Ajouter à une liste de lecture** — inclut la chanson dans une liste de lecture, avec la possibilité d'en créer une nouvelle.
- **Ajouter aux favoris** — marque la chanson comme favorite pour un accès rapide.
- **Télécharger** — enregistre la chanson dans les fichiers locaux, apparaissant dans l'onglet **Fichiers locaux** et la section **Musique hors ligne**.
- **Modifier les balises audio** — ouvre l'éditeur de balises audio intégré pour corriger les métadonnées manquantes, modifiant la chanson dans votre stockage.
- **Afficher dans le dossier** — révèle le dossier où le fichier audio est stocké.
- **Afficher dans le Finder** — pour les fichiers importés depuis votre Mac, cette action révèle le dossier où se trouve le fichier audio sur votre Mac.
- **Ouvrir dans** — exporte le fichier audio vers une autre application.
- **Supprimer de la file** — supprime la chanson sélectionnée de la file de l'audio player.
- **Supprimer du service cloud** — supprime la chanson de la bibliothèque musicale et du stockage cloud. **Cette action est irréversible.**
- **Supprimer des fichiers locaux** — supprime la chanson de la bibliothèque musicale et du stockage local. **Cette action est irréversible.**
- **Supprimer de la bibliothèque musicale** — supprime la chanson de votre bibliothèque musicale, tout en conservant le fichier dans le stockage.

Les mêmes options sont disponibles pour l'élément en cours de lecture dans la file de l'audio player, auquel vous pouvez accéder en appuyant sur l'icône **Plus d'actions** près du titre de la piste.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — Options pour un élément dans la file de lecture" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Actions supplémentaires du lecteur

Appuyez sur le bouton **Plus d'actions** «&nbsp;...&nbsp;» sur le côté gauche du titre de la chanson en cours de lecture pour voir les actions supplémentaires.

- **Reprendre la lecture** — reprendre là où vous vous étiez arrêté, y compris la file et la position média. Particulièrement utile pour les livres audio. Activé dans les paramètres de l'application.
- **Rechercher** — trouver rapidement une piste spécifique dans votre file de l'audio player.
- **Signets** — afficher votre liste de signets audio créés.
- **Commentaires** — afficher les commentaires de piste et les paroles intégrées, ainsi que les fichiers LRC. Instructions complètes [ici](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Vitesse** — ajuster la vitesse de lecture à votre convenance.
- **Récents** — accéder à une liste des chansons récemment lues.
- **Favoris** — voir votre collection de chansons favorites.
- **Égaliseur audio** — activer l'égaliseur audio.
- **Minuteur de sommeil** — définir un minuteur pour arrêter la lecture après un intervalle spécifié. Idéal pour ceux qui veulent s'endormir au son de leur musique.
- **Enregistrer la file dans une liste de lecture** — enregistrer la file actuelle de l'audio player comme une nouvelle liste de lecture.
- **Supprimer la file** — effacer votre file de l'audio player et arrêter la lecture.
- **Paramètres** — accéder aux paramètres de l'audio player.
- **Aide** — trouver de l'assistance et des conseils.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — Écran Plus d'actions de l'audio player" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Signets audio

Cette fonctionnalité vous permet de créer plusieurs signets pour les pistes de votre bibliothèque musicale — idéal pour les livres audio, les conférences, les longs mixages DJ ou pour marquer le refrain d'une piste préférée.

Pour créer un nouveau signet :

- Commencez à lire la chanson souhaitée.
- Ouvrez l'écran du lecteur.
- Appuyez sur le bouton **Signets** dans la barre d'outils du mode lecteur.
- Sélectionnez **Ajouter un signet**.
- Choisissez l'heure du signet et appuyez sur **Fait** dans le coin supérieur droit.

La modification des signets pour la piste actuelle est facile : appuyez sur Modifier dans le coin supérieur droit pour entrer en mode d'édition. Dans ce mode, vous pouvez réorganiser les signets, les supprimer, ajuster l'heure du signet et modifier les titres des signets. Des instructions plus détaillées sur les signets audio sont disponibles [ici](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Écran Signets audio Flacbox" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Récents et favoris

Sur l'écran du lecteur, appuyez sur les trois points pour accéder aux Récents et aux Favoris. Dans les deux sections, vous pouvez rechercher des chansons, tout lire, tout mélanger, exporter la liste et effacer la liste. Nous avons des instructions détaillées sur l'exportation de listes de chansons [ici](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Connectez votre iPhone à votre voiture via USB ou Apple CarPlay sans fil et Flacbox apparaît sur votre écran d'accueil CarPlay, prêt à lire de la musique en toute sécurité pendant la conduite. L'interface CarPlay inclut des onglets dédiés pour Bibliothèque, Connexions, Fichiers locaux et Paramètres, avec des commandes de lecture, le mélange, la répétition, la gestion de la file et l'égaliseur audio — tous disponibles sans prendre votre téléphone en main. Configurez davantage l'expérience CarPlay dans Paramètres → CarPlay — options de tri, pagination, couleur de dégradé des icônes de menu, chargement des images, et une option pour mettre en pause la lecture automatiquement lorsque CarPlay se connecte.

[Lire le guide complet CarPlay](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox sur Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Widgets de l'écran d'accueil (iPhone et iPad)

Flacbox prend en charge les widgets de l'écran d'accueil et de l'écran de verrouillage iOS pour vous permettre de voir et de contrôler la lecture d'un coup d'œil. Assurez-vous que les Widgets sont activés dans Paramètres → Widgets → Activer les widgets, puis maintenez appuyé votre écran d'accueil ou de verrouillage, appuyez sur **+**, recherchez **Flacbox** et ajoutez un widget. Le widget se rafraîchit pendant la lecture pour afficher l'illustration, le titre et l'artiste de la piste en cours.

## Fenêtre mini lecteur (Mac exclusif)

Les utilisateurs Mac peuvent utiliser un mini lecteur compact toujours au premier plan. Déplacez votre curseur vers le bord inférieur droit de la fenêtre Flacbox, redimensionnez-la à sa taille minimale et appuyez sur le bouton de réduction. Gardez-le au-dessus de toutes les autres fenêtres en sélectionnant Fenêtre → Afficher la fenêtre toujours au premier plan dans la barre de menus — idéal pour garder les commandes musicales visibles pendant que vous travaillez dans une autre application.

## Raccourcis clavier (Mac exclusif)

Pour les utilisateurs Mac, un menu de lecture système est disponible dans la barre d'état avec des raccourcis clavier. Par exemple, appuyez sur la barre d'espace pour Lire / Pause. Des raccourcis pour Arrêt, Chanson suivante, Chanson précédente, Sauter dans le temps, Répétition, Mélange et Vitesse de lecture sont également disponibles.

## Paramètres de l'audio player

Pour accéder aux paramètres, appuyez sur le bouton Plus sur l'écran du lecteur et choisissez Paramètres. Vous y trouverez plusieurs sections, listées ci-dessous.

### Général

Ces paramètres couvrent les aspects fondamentaux de l'audio player, notamment la file de lecture, la sortie audio et l'enregistrement de l'état du lecteur.

- **Mode de répétition** — choisissez comment l'audio player se comporte lorsqu'une piste se termine :
  - **Répéter tout** — rejoue toutes les pistes de votre file.
  - **Répéter une** — répète uniquement la piste actuelle.
  - **Répéter arrêt** — met en pause la lecture lorsque la piste actuelle se termine.
  - **Pas de répétition** — permet à votre file de se lire sans répétition.
- **Mode mélange** — aléatoiriser l'ordre des pistes dans votre file. Vous pouvez activer **Mélange désactivé** ou **Mélange activé**.
- **Codec audio** — choisissez le moteur audio utilisé pour la lecture :
  - **Codec système + FFmpeg** — donne la priorité au codec audio du système autant que possible, améliorant la compatibilité et la stabilité. La correction de hauteur tonale et les ajustements du taux d'échantillonnage de sortie audio peuvent être limités dans ce mode.
  - **FFmpeg** — force le codec FFmpeg pour tous les fichiers audio, vous permettant d'ajuster la correction de hauteur tonale et le taux d'échantillonnage de sortie audio.
- **Taux d'échantillonnage de sortie audio** — ajuster le taux d'échantillonnage de sortie audio pour optimiser la qualité sonore, particulièrement utile avec un DAC externe. Valeurs disponibles : **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** et **96 kHz**.
- **Nombre de canaux de sortie audio** — pour les systèmes audio multicanaux avec un DAC externe, spécifiez le nombre de canaux : **Mono, Stéréo, Centre / Gauche / Droite, Centre / Gauche / Droite / Surround, ITU BS.775-1, 5.1 Surround** et **SDDS**.
- **Durée préférée du tampon d'E/S de sortie audio** — configurer la durée du tampon d'entrée / sortie pour la lecture audio. Une valeur typique pour minimiser la latence lors de la lecture audio haute résolution est d'environ **5 millisecondes (0,005 secondes)**. La taille de tampon acceptable dépend de votre environnement matériel et logiciel, alors testez différentes durées sur votre appareil cible et choisissez celle qui offre le meilleur équilibre entre faible latence et lecture sans accroc.
- **Mode de sortie audio (iOS uniquement)** — configurer le mode de sortie audio mixte pour que l'audio de Flacbox se mélange avec d'autres applications. Des instructions détaillées sont disponibles [ici](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Enregistrer la position de lecture** — garantit que l'application enregistre et restaure la position de lecture pour les chansons de votre bibliothèque musicale.
- **Enregistrer l'état de l'audio player** — préserve l'état de votre audio player avant que vous fermiez l'application. Pour reprendre la lecture, appuyez sur **Reprendre la lecture** en haut de n'importe quel dossier, album, artiste ou genre lorsque vous rouvrez l'application. Vous pouvez également reprendre la lecture de fichiers individuels en appuyant sur la piste spécifique.

Une fois que vous avez activé **Enregistrer la position de lecture** et **Enregistrer l'état de l'audio player**, ouvrez n'importe quel dossier, album, artiste ou genre et vous verrez un bouton **Reprendre la lecture** en haut de l'écran avec la dernière piste et position enregistrées. Appuyez dessus pour reprendre exactement là où vous vous étiez arrêté.

### Personnalisation

La personnalisation vous permet de personnaliser l'apparence de l'écran de l'audio player, de modifier les commandes disponibles sur l'écran principal, l'écran de verrouillage et la barre d'état, et de configurer les contrôles de saut de temps.

- **Style de l'écran de l'audio player** — configurer le positionnement des éléments sur l'écran de l'audio player.
- **Style de défilement des pochettes d'album** — configurer le style de défilement préféré pour les pochettes d'album.
- **Éléments supplémentaires** — activer des éléments supplémentaires sur l'écran de l'audio player. **Informations sur le format audio** affiche les informations audio de la piste en cours au-dessus de l'illustration ; **Curseur de volume audio** affiche le curseur de sortie audio sous les commandes de lecture.
- **Actions de l'écran principal** — configurer quels boutons doivent être visibles par défaut sur l'écran principal de l'audio player : **Mode de répétition et de mélange, Chanson suivante et précédente, Sauter dans le temps, Minuteur de sommeil, Google Chromecast, AirPlay et Bluetooth, Égaliseur audio, Rechercher, Signets, Vitesse, Ajouter un signet, Ajouter aux favoris, Commentaires** et plus encore.
- **Commandes de lecture sur l'écran de verrouillage** — choisir quelles commandes apparaissent sur l'écran de verrouillage. Valeurs possibles : **Sauter dans le temps, Ajouter un signet, Ajouter aux favoris**.
- **Boutons de saut de temps** — choisir l'intervalle de temps pour les boutons **Sauter dans le temps**.

### Chargement des fichiers

Pendant le processus de chargement des fichiers, vous pouvez modifier le type de réseau utilisé pour charger les chansons. Options disponibles : **Wi-Fi**, **Wi-Fi et données cellulaires**.

- **Temps de préchargement** — définir l'intervalle de mise en mémoire tampon. Augmentez cette valeur si vous avez une connexion réseau médiocre.
- **Utiliser l'URL directe** — lorsque cette option est activée, une URL directe est utilisée pour charger la chanson si le serveur la prend en charge. Cela peut accélérer le chargement des chansons mais peut affecter la stabilité de la lecture.

### Égaliseur audio

Personnalisez les paramètres de l'égaliseur audio. Vous pouvez en savoir plus sur la configuration de l'égaliseur audio [ici](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Vitesse de lecture

Ajustez la vitesse de lecture de l'audio player de **0,02× à 3,00×**. Appuyez sur l'icône de configuration dans le coin supérieur droit pour passer en **mode précis** pour des ajustements plus fins.

{{< cards cols="1">}}
  {{< card title="" subtitle="Écran Vitesse de lecture Flacbox" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Correction de hauteur tonale

Modifiez les paramètres de correction de hauteur tonale à l'aide des valeurs prédéfinies. Vous pouvez également basculer entre les valeurs prédéfinies et le mode précis en appuyant sur le bouton dans le coin supérieur droit. La correction de hauteur tonale est disponible dans le chemin du codec FFmpeg, avec une plage de **-1000 à +1000**.

### Cache de lecture

Les chansons dans la file de l'audio player sont automatiquement téléchargées pour garantir une lecture fluide. Si vous téléchargez manuellement des fichiers audio, vous pouvez désactiver cette option pour éviter les doublons. Vous pouvez également configurer la taille du cache de l'audio player ici.

### Minuteur de sommeil

Activez un minuteur pour arrêter automatiquement la lecture après une période spécifiée — pratique quand vous voulez vous endormir au son de votre musique. Appuyez sur l'icône de configuration dans le coin supérieur droit pour le **mode précis** avec une granularité minute par minute.

## Accessibilité

Flacbox est entièrement accessible avec **VoiceOver**. Chaque composant dispose d'une étiquette et d'une description bien conçues. Lorsque VoiceOver est actif, l'application passe en **Mode texte** pour que seuls les éléments significatifs soient présentés — améliorant la vitesse de navigation et la clarté. Vous pouvez également activer le Mode texte dans **Paramètres → Accessibilité → Mode texte**.

### Ajuster les curseurs avec VoiceOver

1. **Sélectionner le curseur** — balayez vers la gauche ou la droite jusqu'à ce que VoiceOver l'annonce.
2. **Ajuster la valeur** — appuyez deux fois et maintenez le curseur, puis faites glisser vers le haut ou le bas pour modifier la valeur rapidement. VoiceOver annonce la nouvelle valeur au fur et à mesure.

### Ajuster la position d'une piste dans une liste avec VoiceOver

1. Appuyez sur l'icône de l'indicateur de réorganisation près du titre de la piste pour lui donner le focus.
2. Appuyez deux fois rapidement sur l'indicateur de réorganisation. Au deuxième appui, ne relâchez pas votre doigt — maintenez-le jusqu'à entendre un son indiquant que la cellule est prête à être déplacée.
3. Déplacez la cellule vers sa nouvelle position.

Les autres composants fonctionnent comme prévu, en utilisant les schémas VoiceOver fournis par le système.
