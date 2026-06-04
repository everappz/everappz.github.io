---
title: "Paramètres"
date: 2020-02-01
description: "Explorez tous les paramètres de Flacbox — des préférences de lecture, du moteur audio FFmpeg / système, de la sortie audio haute résolution, des réglages d'égaliseur, de la correction de hauteur tonale, de la durée du tampon d'E/S, de la synchronisation des métadonnées, du contrôle des listes de lecture, des transferts de fichiers, des widgets de l'écran d'accueil, d'Apple CarPlay, de la personnalisation de l'interface, de la langue, du code d'accès, de la sauvegarde et restauration, et de la mise à niveau Premium."
keywords: [
  "paramètres Flacbox", "configuration audio player", "mise à niveau Premium Flacbox",
  "Wi-Fi Drive", "synchronisation des métadonnées", "égaliseur", "vitesse de lecture",
  "doublons dans liste de lecture", "paramètres gestionnaire de fichiers", "synchronisation musique hors ligne",
  "éditeur de balises audio", "mode sombre", "restaurer achats", "paramètres sauvegarde",
  "paramètres widgets Flacbox", "paramètres CarPlay Flacbox",
  "paramètres FFmpeg Flacbox", "paramètres taux d'échantillonnage Flacbox",
  "paramètres correction hauteur tonale Flacbox", "tampon E/S Flacbox",
  "code d'accès Flacbox", "langue Flacbox", "personnalisation Flacbox",
  "analytics Flacbox"
]
tags: ["guide", "flacbox", "paramètres"]
readingTime: 16
---


L'écran Paramètres est le centre de contrôle de Flacbox. Depuis cet écran, vous pouvez passer à Premium, configurer le moteur audio (codecs système ou FFmpeg), gérer votre bibliothèque musicale, configurer le gestionnaire de fichiers, personnaliser l'éditeur de balises audio, activer les widgets de l'écran d'accueil et Apple CarPlay, sauvegarder vos données, et accéder à l'aide et aux informations légales. Les sections sont regroupées sous des en-têtes : Achats et mises à jour, Préférences de l'application, Aide, et Légal et confidentialité.

{{< cards cols="1">}}
  {{< card title="" subtitle="Écran principal des paramètres Flacbox" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Passer à Premium

Passez à la version Premium pour supprimer toutes les limites. La version gratuite de l'application propose un achat unique à vie et deux options d'abonnement (1 mois et 1 an) pour supprimer toutes les restrictions et passer à Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — Passer à Premium" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

Le **Partage familial** est activé pour tous les achats et abonnements, vous permettant de partager la version Premium avec jusqu'à cinq membres de votre famille sans frais supplémentaires.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — Choisir un abonnement Premium" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Vous pouvez en savoir plus sur les achats et la version Premium ici : [Quelle est la différence entre Flacbox et Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Partager les achats entre iOS et Mac

Les achats à vie et les abonnements sont partagés entre iOS et Mac, en utilisant iCloud pour synchroniser ces informations. Si vous avez la version Premium sur votre appareil iOS, assurez-vous d'avoir installé la dernière version et qu'iCloud est activé. Démarrez l'application sur iOS et attendez une minute pour que vos informations d'achat soient téléversées vers iCloud.

Vous pouvez également essayer d'appuyer sur le bouton Restaurer les achats dans les paramètres de l'application. Ensuite, installez la dernière version de l'application depuis l'App Store sur votre Mac et démarrez l'application. Assurez-vous d'avoir une connexion internet et d'utiliser le même compte iCloud et App Store sur Mac que celui utilisé sur iOS. Attendez une minute pour que l'application télécharge les informations d'achat depuis iCloud — la version Premium devrait s'activer automatiquement sur votre Mac.

## Restaurer les achats sur un nouvel appareil

Pour restaurer votre achat sur un nouvel appareil, utilisez le menu Achats → Restaurer les achats. Vous verrez la liste de vos achats. Si vous ne les voyez pas tous, confirmez que l'appareil est connecté au même Apple ID utilisé pour effectuer les achats et assurez-vous qu'iCloud est activé.

## Essayer Premium gratuitement

Vous pouvez passer à la version Premium gratuitement, pour une durée limitée, en utilisant ce menu. Regardez simplement une publicité ou parlez de l'application à vos amis pour obtenir Premium gratuitement.

## Achats

Vous pouvez restaurer les achats précédents depuis ce menu. Si vous rencontrez des erreurs d'activation, essayez d'activer l'option Restaurer les achats au lancement de l'application.

## Mise à jour du logiciel

Appuyez sur Mise à jour du logiciel pour vérifier si une version plus récente de Flacbox est disponible. L'application comparera votre version installée avec la dernière version sur l'App Store et vous informera si une mise à jour est recommandée.

## Nouveautés

Ce menu est disponible après la sortie d'une nouvelle version. Il affiche un résumé des modifications et des nouvelles fonctionnalités de la mise à jour la plus récente.

## Audio Player

Cette section configure l'audio player et le moteur audio sous-jacent, y compris le choix du codec FFmpeg / système et les options de sortie audio haute résolution.

### Général

Ces paramètres couvrent les aspects fondamentaux de l'audio player — file de lecture, sortie audio et enregistrement de l'état du lecteur.

- **Mode de répétition** — choisissez comment l'audio player se comporte lorsqu'une piste se termine :
  - **Répéter tout** — rejoue toutes les pistes de votre file.
  - **Répéter une** — répète uniquement la piste actuelle.
  - **Répéter arrêt** — met en pause la lecture lorsque la piste actuelle se termine.
  - **Pas de répétition** — permet à votre file de se lire sans répétition.
- **Mode mélange** — aléatoiriser l'ordre des pistes dans votre file. Vous pouvez activer **Mélange désactivé** ou **Mélange activé**.
- **Codec audio** — choisissez le moteur audio utilisé pour la lecture :
  - **Codec système + FFmpeg** — donne la priorité au codec audio du système autant que possible, améliorant la compatibilité et la stabilité. La correction de hauteur tonale et le taux d'échantillonnage de sortie audio peuvent être limités.
  - **FFmpeg** — force le codec FFmpeg pour tous les fichiers audio, débloquant la correction de hauteur tonale et le taux d'échantillonnage de sortie audio.
- **Taux d'échantillonnage de sortie audio** — ajuster le taux d'échantillonnage de sortie audio pour optimiser la qualité sonore, particulièrement utile avec un DAC externe. Valeurs disponibles : **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** et **96 kHz**.
- **Nombre de canaux de sortie audio** — pour les systèmes audio multicanaux avec un DAC externe, spécifiez le nombre de canaux : Mono, Stéréo, Centre / Gauche / Droite, Centre / Gauche / Droite / Surround, ITU BS.775-1, 5.1 Surround et SDDS.
- **Durée préférée du tampon d'E/S de sortie audio** — configurer la durée du tampon d'entrée / sortie. Une valeur typique pour minimiser la latence lors de la lecture audio haute résolution est d'environ **5 millisecondes (0,005 secondes)**. Testez différentes durées sur votre appareil cible pour trouver le meilleur équilibre entre faible latence et lecture sans accroc.
- **Mode de sortie audio (iOS uniquement)** — configurer la sortie audio mixte pour que l'audio de Flacbox se mélange avec d'autres applications. Des instructions détaillées sont disponibles [ici](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Enregistrer la position de lecture** — enregistre et restaure la position de lecture pour les chansons de votre bibliothèque musicale.
- **Enregistrer l'état de l'audio player** — préserve l'état de l'audio player avant que vous fermiez l'application, facilitant la reprise là où vous vous étiez arrêté.

Une fois que vous avez activé **Enregistrer la position de lecture** et **Enregistrer l'état de l'audio player**, ouvrez n'importe quel dossier, album, artiste ou genre et vous verrez un bouton **Reprendre la lecture** en haut de l'écran.

### Personnalisation

La personnalisation vous permet de personnaliser l'apparence de l'écran de l'audio player, de modifier les commandes disponibles sur l'écran principal, l'écran de verrouillage et la barre d'état, et de configurer les contrôles de saut de temps.

- **Style de l'écran de l'audio player** — configurer le positionnement des éléments sur l'écran de l'audio player.
- **Style de défilement des pochettes d'album** — configurer le style de défilement préféré pour les pochettes d'album.
- **Éléments supplémentaires** — activer des éléments supplémentaires sur l'écran de l'audio player. Informations sur le format audio affiche les informations audio de la piste en cours au-dessus de l'illustration ; Curseur de volume audio affiche le curseur de sortie audio sous les commandes de lecture.
- **Actions de l'écran principal** — configurer quels boutons doivent être visibles par défaut sur l'écran principal de l'audio player : Mode de répétition et de mélange, Chanson suivante et précédente, Sauter dans le temps, Minuteur de sommeil, Google Chromecast, AirPlay et Bluetooth, Égaliseur audio, Rechercher, Signets, Vitesse, Ajouter un signet, Ajouter aux favoris, Commentaires et plus encore.
- **Commandes de lecture sur l'écran de verrouillage** — choisir quelles commandes apparaissent sur l'écran de verrouillage. Valeurs possibles : Sauter dans le temps, Ajouter un signet, Ajouter aux favoris.
- **Boutons de saut de temps** — choisir l'intervalle de temps pour les boutons de saut de temps.

### Chargement des fichiers

Pendant le chargement des fichiers, vous pouvez modifier le type de réseau utilisé pour charger les chansons. Options disponibles : **Wi-Fi**, **Wi-Fi et données cellulaires**.

- **Temps de préchargement** — définir l'intervalle de mise en mémoire tampon. Augmentez cette valeur si vous avez une connexion réseau médiocre.
- **Utiliser l'URL directe** — lorsque cette option est activée, une URL directe est utilisée pour charger la chanson si le serveur la prend en charge. Cela peut accélérer le chargement des chansons mais peut affecter la stabilité de la lecture.

### Égaliseur audio

Configurez l'égaliseur audio à 10 bandes, les préréglages et le préamplificateur. Vous pouvez en savoir plus sur la configuration de l'égaliseur audio [ici](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Vitesse de lecture

Ajustez la vitesse de lecture de l'audio player de **0,02× à 3,00×**. Appuyez sur l'icône de configuration dans le coin supérieur droit pour passer en **mode précis** pour des ajustements plus fins.

### Correction de hauteur tonale

Modifiez les paramètres de correction de hauteur tonale à l'aide des valeurs prédéfinies, ou passez en **mode précis** en appuyant sur le bouton dans le coin supérieur droit. La correction de hauteur tonale est disponible dans le chemin du codec FFmpeg, avec une plage de **-1000 à +1000**.

### Cache de lecture

Les chansons dans la file de l'audio player sont automatiquement téléchargées pour garantir une lecture fluide. Si vous téléchargez manuellement des fichiers audio, vous pouvez désactiver cette option pour éviter les doublons. Vous pouvez également configurer la taille du cache de l'audio player ici.

### Minuteur de sommeil

Activez un minuteur pour arrêter automatiquement la lecture après une période spécifiée. Appuyez sur l'icône de configuration dans le coin supérieur droit pour le **mode précis** avec une granularité minute par minute.

## Bibliothèque

Vos paramètres de bibliothèque musicale — synchronisation automatique, lecture des métadonnées, chargement des pochettes, listes de lecture, récents et favoris — se trouvent ici.

### Lecture des métadonnées

Lorsque vous ajoutez des pistes à la bibliothèque, le **lecteur de métadonnées** se met au travail. Ce processus en arrière-plan lit toutes les métadonnées de vos pistes et les organise par Artiste, Album, Genre et Compositeur. Vous pouvez ajuster la vitesse de lecture des métadonnées pour charger les données plus rapidement (au détriment de la batterie). Vous pouvez également désactiver le lecteur de métadonnées et afficher les noms de fichiers à la place des informations de balise.

Le lecteur de métadonnées **met uniquement à jour les métadonnées dans votre bibliothèque musicale** et ne modifie pas les fichiers stockés dans votre compte cloud ou dans le stockage local. Pour modifier les métadonnées dans les fichiers audio eux-mêmes, utilisez l'**éditeur de balises** intégré via l'action correspondante dans le menu options.

Lorsque **Lecture des métadonnées en arrière-plan** est activé, le lecteur continue de fonctionner en mode arrière-plan. Si l'application utilise trop d'énergie pendant la lecture audio, iOS peut la suspendre.

Si vous avez une grande collection de musique, effectuez la synchronisation des métadonnées sur la version de bureau de l'application et transférez la bibliothèque musicale synchronisée vers iOS à l'aide de **Sauvegarde et restauration**.

Lorsque **Normaliser l'encodage des métadonnées** est activé, l'application normalise automatiquement l'encodage des métadonnées pour toutes les chansons. Cela corrige les encodages de balises cassés (par exemple après avoir modifié des fichiers sur un PC Windows) et empêche l'affichage de caractères incorrects dans les informations de piste.

**Recharger les métadonnées** marque chaque fichier de votre bibliothèque musicale comme ayant des métadonnées manquantes, ce qui pousse le lecteur de métadonnées à actualiser chaque enregistrement.

**Démarrer la lecture des métadonnées** déclenche manuellement le lecteur de métadonnées. La progression est affichée sous l'action.

### Synchronisation en ligne

La synchronisation automatique de musique en ligne ajoute des pistes depuis les services cloud connectés à la bibliothèque musicale automatiquement. Pour l'activer, ouvrez les paramètres de la bibliothèque musicale et sélectionnez les dossiers de synchronisation.

Avec cette option activée, l'application analyse les dossiers sélectionnés, identifie les fichiers audio pris en charge et les ajoute à votre bibliothèque. Démarrez ou arrêtez la synchronisation avec l'action de menu correspondante.

La synchronisation en ligne ne fonctionne que lorsque l'application est au premier plan, donc la synchronisation d'une grande bibliothèque peut prendre du temps. Pour accélérer les choses, gardez Flacbox ouvert, branchez votre appareil sur secteur et activez **Paramètres → Écran → Toujours actif**.

Vous pouvez également effectuer la synchronisation en ligne sur la version de bureau de l'application et transférer le résultat vers iOS à l'aide de **Sauvegarde et restauration**.

Vous pouvez également choisir la fréquence d'exécution de la synchronisation en ligne. En définissant l'intervalle sur **Immédiatement**, une synchronisation est déclenchée chaque fois que vous ouvrez l'application.

### Synchronisation hors ligne

Configurez la synchronisation de musique hors ligne.

#### Dossiers hors ligne synchronisés

Lorsque vous marquez un dossier en ligne sur votre serveur cloud comme disponible hors ligne (en utilisant le menu **Plus d'actions**), il apparaît ici. Le contenu du dossier est téléchargé dans **Fichiers locaux → Dossiers hors ligne**. Lorsque le dossier en ligne change (fichiers ajoutés, supprimés ou mis à jour), l'application vérifie les modifications et met à jour la copie locale sur votre appareil.

Sur cet écran, vous pouvez démarrer manuellement la synchronisation des dossiers hors ligne, révéler le dossier hors ligne dans son dossier parent et désactiver le mode hors ligne pour le dossier. La désactivation du mode hors ligne supprime toutes les copies locales des fichiers de votre appareil.

#### Intervalle de temps

Choisissez la fréquence à laquelle l'application vérifie les modifications dans les dossiers hors ligne.

#### Démarrer l'analyse des dossiers locaux

Analysez tous les dossiers locaux dans le répertoire **Documents** de l'application pour trouver les fichiers audio pris en charge. Les fichiers trouvés sont ajoutés automatiquement à la bibliothèque musicale. Les fichiers situés sur votre appareil mais en dehors du répertoire Documents de l'application doivent être ajoutés manuellement à la bibliothèque musicale, car l'application ne peut pas y accéder en raison des restrictions de sécurité iOS / macOS.

**Important :** Il est conseillé de lancer périodiquement la synchronisation de musique hors ligne pour maintenir votre bibliothèque musicale à jour avec vos fichiers locaux.

### Personnalisation

Configurez le style de l'écran de la bibliothèque musicale. Trois options sont disponibles : **Menu simple, Menu groupé, Menu à onglets**. Vous pouvez également activer ou désactiver les pochettes d'album dans l'écran de détail d'album.

### Pochettes d'album

Configurez la façon dont l'application charge et stocke les illustrations d'album.

- **Type de réseau** — choisissez **Wi-Fi** ou **Wi-Fi et données cellulaires** pour les téléchargements de pochettes.
- **Charger les pochettes pour les fichiers en ligne** — lorsque cette option est activée, les pochettes d'album intégrées sont chargées pour les fichiers stockés dans le stockage cloud. Cela peut utiliser des données réseau supplémentaires.
- **Rechercher dans le dossier** — lorsque cette option est activée, si une piste n'a pas de pochette intégrée, l'application recherche des images JPEG ou PNG dans le même dossier et les utilise comme illustration d'album.
- **Qualité des pochettes** — sélectionner la qualité des pochettes d'album stockées sur votre appareil.
- **Afficher dans le dossier** — ouvrir le dossier où les pochettes d'album sont mises en cache.
- **Tout supprimer** — supprimer les pochettes d'album mises en cache pour libérer de l'espace de stockage et forcer l'application à les recharger à la demande.

### Listes de lecture

Activez l'option d'ajout de la même chanson à une liste de lecture deux fois. Par défaut, cette option est désactivée.

### Récents

Gérez votre liste de chansons récemment lues.

- **Supprimer la liste** — supprimer toute la liste des chansons récemment lues.
- **Modifier la taille de la liste** — définir le nombre d'éléments qui apparaissent dans la liste.
- **Exporter la liste des chansons** — exporter votre liste de chansons récemment lues en M3U, CSV ou TXT. Des instructions détaillées sont disponibles [ici](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoris

Gérez la liste de vos chansons favorites.

- **Modification simultanée** — lorsque cette option est activée, l'ajout d'une chanson aux favoris l'ajoute à la fois dans la bibliothèque musicale et dans la section fichiers simultanément.
- **Supprimer la liste** — supprimer toute la liste des chansons favorites.
- **Exporter la liste des chansons** — comme pour les Récents, exporter les favoris en M3U, CSV ou TXT.

### Supprimer la bibliothèque musicale

Effacer la base de données de la bibliothèque musicale. Vos fichiers musicaux dans le stockage restent intacts.

## Code d'accès

Activez l'écran du code d'accès pour protéger les données de votre application avec un code numérique à 4 chiffres. Lorsqu'il est activé, vous serez invité à saisir le code d'accès à chaque lancement de l'application. Combinez-le avec Face ID / Touch ID iOS sur l'appareil pour une protection supplémentaire.

## Gestionnaire de fichiers

La section Gestionnaire de fichiers contrôle la façon dont les fichiers sont transférés, stockés et prévisualisés.

### Transferts de fichiers

Choisissez votre préférence réseau pour le téléchargement de fichiers sur votre appareil.

### Nombre maximum de tâches parallèles

Définissez le nombre de fils de téléchargement parallèles. Un nombre plus élevé accélère les téléchargements mais utilise plus de batterie.

### Tâches de transfert de fichiers

Affiche les tâches de téléversement et téléchargement actuellement actives.

### Transferts en arrière-plan

Autorisez les téléchargements pendant que l'application est en arrière-plan. Si les transferts en arrière-plan consomment beaucoup d'énergie, iOS peut suspendre l'application.

### Enregistrer les fichiers téléchargés dans

Choisissez le répertoire de téléchargements par défaut, ou faites en sorte que l'application vous demande à chaque fois.

### Dossiers hors ligne synchronisés

Gérez la synchronisation hors ligne pour les dossiers sélectionnés. Pour activer la synchronisation hors ligne, appuyez sur le bouton à trois points à côté d'un dossier et sélectionnez **Mode hors ligne disponible**. Les nouveaux fichiers ajoutés au dossier cloud sont téléchargés automatiquement sur votre appareil. En savoir plus sur les modes hors ligne [ici](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Intervalle de temps

Choisissez la fréquence de synchronisation des dossiers hors ligne. **Immédiatement** déclenche une synchronisation à chaque ouverture de l'application.

### Afficher les noms de fichiers complets

Afficher les noms de fichiers complets, y compris les extensions, dans le gestionnaire de fichiers.

### Modifier les fichiers en ligne

Désactivez la modification des fichiers en ligne pour passer en mode lecture seule pour les services cloud connectés et éviter les suppressions accidentelles. Cette action supprime les opérations de modification de fichiers de l'interface utilisateur.

### Copier les fichiers à l'ouverture

Spécifiez comment l'application gère les fichiers importés depuis d'autres applications.

### Miniatures pour les fichiers

Gérez et supprimez les miniatures de fichiers générées pour libérer de l'espace de stockage.

### Supprimer les fichiers temporaires

Videz le dossier de cache de l'application pour récupérer de l'espace de stockage.

## Éditeur de balises audio

Configurez l'éditeur de balises audio intégré — pratique pour corriger en lot les problèmes d'artiste / album / année / genre / pochette dans les fichiers cloud et locaux.

### Mise à l'échelle de la pochette

Choisissez la méthode de mise à l'échelle utilisée lorsqu'une pochette est enregistrée dans les balises audio.

### Mettre à jour les fichiers en ligne

Lorsque cette option est activée, l'application met automatiquement à jour les métadonnées d'un fichier sur le serveur cloud après que vous ayez terminé de le modifier.

### Supprimer le fichier après modification en ligne

Choisissez si l'application doit supprimer la copie téléchargée après avoir terminé la modification d'un fichier en ligne sur un serveur cloud.

### Boutons de l'écran principal

Choisissez quels boutons sont visibles sur l'écran principal de l'éditeur de balises audio.

Pour une édition en lot plus poussée sur de nombreux fichiers à la fois, installez notre application complémentaire **Evertag**.

## Widgets

Activez les widgets pour que l'application mette à jour les données des widgets pendant la lecture. Les mises à jour des widgets nécessitent de l'énergie supplémentaire, donc le commutateur est désactivé par défaut — activez-le uniquement si vous utilisez réellement des widgets sur votre écran d'accueil ou de verrouillage.

Vous pouvez ajouter des widgets Flacbox en maintenant appuyé votre écran d'accueil ou de verrouillage, en appuyant sur **+**, en recherchant **Flacbox** et en choisissant une taille de widget. Les widgets affichent l'illustration actuelle, le titre de la piste et l'artiste, et permettent d'accéder directement au lecteur plein écran en appuyant. Les widgets fonctionnent également sur macOS dans le Centre de notifications.

## CarPlay

Modifiez les paramètres CarPlay ici. Ce menu est également disponible dans l'interface CarPlay pour que vous puissiez ajuster l'expérience pendant la conduite.

### Trier

Configurez les options de tri pour tous les écrans CarPlay.

### Limite de chargement du contenu

Choisissez si l'application utilise la pagination sur l'écran CarPlay. La pagination maintient les menus réactifs sur les grandes bibliothèques.

### Couleur de dégradé des icônes de menu

Sélectionnez le schéma de couleurs pour l'écran d'accueil CarPlay.

### Afficher les images

Désactivez les images sur l'écran CarPlay pour optimiser la vitesse de chargement et réduire l'utilisation de la mémoire sur les grandes bibliothèques.

### Mettre en pause la lecture à la connexion

Activez cette option pour éviter un son soudain et fort lorsque vous connectez votre appareil à CarPlay.

## Wi-Fi Drive

Activez **Wi-Fi Drive** pour transférer des fichiers depuis un ordinateur vers votre appareil à l'aide d'un navigateur web de bureau, du Finder ou de l'Explorateur de fichiers. Des instructions détaillées sur l'utilisation de Wi-Fi Drive sont disponibles [ici](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personnalisation

Personnalisez l'interface utilisateur selon vos préférences.

### Icône de l'application

Choisissez une icône d'application alternative pour votre écran d'accueil (Premium).

### Schéma de couleurs

Choisissez le thème de l'interface utilisateur et activez le mode sombre. Lorsque **Par défaut** est sélectionné, l'application suit les paramètres d'apparence à l'échelle de l'appareil.

### Style d'arrière-plan

Modifiez le style d'arrière-plan de l'application. Actuellement, la seule option est **Pochette d'album floutée**, qui utilise l'illustration de la piste en cours de lecture comme arrière-plan flou de l'application.

### Apparence des éléments dans la liste

Ajustez la façon dont les éléments sont affichés dans les listes. Utile sur les petits écrans — vous pouvez laisser l'application ajuster automatiquement la hauteur des lignes en fonction du contenu, ou afficher des icônes plus petites dans les cellules de liste pour donner plus d'espace au texte.

### Limite de chargement du contenu

Par défaut, l'application utilise la pagination pour accélérer le chargement du contenu. Vous pouvez désactiver la pagination pour tout charger en une seule fois.

### Style de l'écran Fichiers locaux

Modifier le style de présentation de la section **Fichiers locaux**.

### Style de l'écran Bibliothèque musicale

Personnaliser l'apparence de l'écran **Bibliothèque musicale**.

### Style de l'écran Audio Player

Configurer l'apparence de l'écran **Audio Player**.

### Style du menu contextuel

Choisissez le style du menu contextuel affiché lorsque vous appuyez sur le bouton **Plus d'actions**.

## Fenêtre

Disponible sur Mac et Catalyst. Configurez les préférences liées à la fenêtre, telles que la taille par défaut et le comportement au lancement.

## Écran

Choisissez si l'écran doit rester actif pendant que vous utilisez l'application. Utile lors de l'analyse de grandes bibliothèques ou de travaux d'édition de balises prolongés.

## Accessibilité

Activez le **Mode texte** pour masquer toutes les images dans l'interface utilisateur. Le Mode texte est activé automatiquement lorsque VoiceOver est actif et est également utile pour les configurations très petites ou uniquement textuelles.

## Langue

Modifiez la langue de l'application et remplacez le paramètre système par défaut. Le changement s'applique après avoir complètement fermé et rouvert Flacbox. Les localisations actuellement prises en charge incluent : Afrikaans, Akan, Albanais, Amharique, Arabe, Arménien, Assamais, Aymara, Azerbaïdjanais, Bambara, Bengali, Basque, Biélorusse, Bosnien, Bulgare, Birman, Catalan, Cebuano, Chinois (simplifié), Chinois (traditionnel), Corse, Croate, Tchèque, Danois, Maldivien, Dogri, Néerlandais, Anglais, Espéranto, Estonien, Ewe, Filipino, Finnois, Français, Galicien, Ganda, Géorgien, Allemand, Grec, Guarani, Gujarati, Créole haïtien, Haoussa, Hawaïen, Hébreu, Hindi, Hmong, Hongrois, Islandais, Igbo, Iloko, Indonésien, Irlandais, Italien, Japonais, Javanais, Kannada, Kazakh, Khmer, Kinyarwanda, Coréen, Krio, Kurde, Kurde sorani, Kirghiz, Laotien, Latin, Letton, Lingala, Lituanien, Luxembourgeois, Macédonien, Maithili, Malgache, Malais, Malayalam, Maltais, Māori, Marathi, Mizo, Mongol, Népalais, Sotho du Nord, Norvégien Bokmål, Nyanja, Odia, Oromo, Pachto, Persan, Polonais, Portugais, Pendjabi, Roumain, Russe, Samoan, Sanskrit, Gaélique écossais, Serbe, Shona, Sindhi, Cingalais, Slovaque, Slovène, Somali, Sotho du Sud, Espagnol, Soundanais, Swahili, Suédois, Tadjik, Tamoul, Tatar, Télougou, Thaï, Tsonga, Turc, Turkmène, Ukrainien, Ourdou, Ouïghour, Ouzbek, Vietnamien, Gallois, Xhosa, Yiddish, Yoruba, Zoulou.

## Sauvegarde et restauration

Utilisez cette fonctionnalité pour sauvegarder toutes les données de votre application ou les migrer vers un autre appareil. Vous pouvez choisir ce qui est inclus :

- **Base de données** — toutes vos pistes dans la bibliothèque musicale, y compris les listes de lecture. Les pistes hors ligne ne sont pas incluses pour que la taille du fichier de sauvegarde reste gérable.
- **Pochettes d'album** — toutes vos pochettes d'album mises en cache.
- **Paramètres** — tous les paramètres de votre application.

Appuyez sur **Sauvegarder les données de l'application** pour démarrer la sauvegarde. Les données de l'application sont écrites dans un seul fichier que vous pouvez utiliser ultérieurement pour restaurer l'état de l'application sur un nouvel appareil ou après avoir réinstallé l'application.

Pour restaurer les données de l'application sur un nouvel appareil, déplacez le fichier de sauvegarde vers le nouvel appareil à l'aide d'un service cloud connecté ou iCloud et ouvrez-le sur le nouvel appareil.

Instructions détaillées étape par étape : [Comment transférer votre bibliothèque musicale entre appareils : guide étape par étape](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Aide

Accédez au guide de l'application pour obtenir de l'aide et des conseils sur l'utilisation efficace de l'application.

## Foire aux questions

Trouvez des réponses aux questions courantes dans la section FAQ.

## Envoyer des commentaires

Vous avez des commentaires ou besoin d'aide ? Envoyez vos commentaires directement à notre équipe d'assistance depuis l'application.

## Partager cette application

Partagez l'application avec vos amis pour faire connaître l'application.

## Découvrir d'autres applications

Explorez d'autres applications d'Everappz.

## Conditions générales d'utilisation

Décrit les conditions générales d'utilisation de l'application. Veuillez les lire avant d'utiliser l'application.

## Politique de confidentialité

Visitez la page de politique de confidentialité pour comprendre nos pratiques de traitement des données. Veuillez la lire avant d'utiliser l'application.

## Analytics et collecte de données

Vérifiez quels services sont activés pour les analytics et la collecte de données et désactivez ceux que vous ne souhaitez pas.

## Mentions légales

Contient des informations sur chaque bibliothèque utilisée dans l'application ainsi que le numéro de version et les informations de build.
