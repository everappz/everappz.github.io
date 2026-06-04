---
title: "Paramètres"
date: 2020-02-01
lastmod: 2026-06-01
description: "Explorez chaque paramètre d'Evervideo — Lecteur multimédia (Picture-in-Picture, décodage matériel H.264/HEVC, égaliseur vidéo, mise à l'échelle, rotation, vue VR), Audio (égaliseur, fréquence d'échantillonnage, canaux, tampon IO, mode mixte), Sous-titres (principal/secondaire, police, fichier externe, libass), Médiathèque, Gestionnaire de fichiers, Wi-Fi Drive, Widgets, Personnalisation, Langue, Code d'accès, Sauvegarde et restauration — pour iPhone, iPad et Mac."
keywords: [
  "paramètres Evervideo", "configuration lecteur vidéo", "mise à niveau Premium Evervideo",
  "paramètres Picture-in-Picture", "paramètres égaliseur vidéo",
  "mode de mise à l'échelle vidéo", "rotation vidéo", "décodeur matériel iPhone",
  "paramètres sous-titres", "sous-titre secondaire iOS", "paramètres libass",
  "fichier sous-titre externe", "police sous-titre",
  "paramètres égaliseur audio", "fréquence d'échantillonnage sortie audio",
  "canaux de sortie audio", "durée tampon IO", "mode mixte audio",
  "Wi-Fi Drive vidéo", "widgets Evervideo",
  "sauvegarde restauration Evervideo", "code d'accès Evervideo",
  "langue Evervideo", "personnalisation Evervideo"
]
tags: ["guide", "evervideo", "settings"]
readingTime: 16
---


L'écran **Paramètres** est le centre de contrôle d'Evervideo. Depuis cet écran, vous pouvez passer à Premium, configurer les moteurs vidéo et audio (codecs système ou FFmpeg), gérer le Picture-in-Picture, configurer les sous-titres (principal, secondaire, libass, fichiers externes, polices), organiser la médiathèque, configurer le gestionnaire de fichiers, activer les widgets de l'écran d'accueil, sauvegarder vos données et accéder à l'aide et aux informations légales. Les sections sont regroupées sous des en-têtes : Achats et mises à jour, Préférences de l'application, Aide, Mentions légales et confidentialité.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Écran principal des paramètres" image="/docs/guide/evervideo/img/evervideo-settings.webp" >}}
{{< /cards >}}

## Passer à Premium

Mettez à niveau l'application vers la version Premium pour supprimer toutes les limites. La version gratuite de l'application propose un achat unique à vie et deux options d'abonnement (1 mois et 1 an) pour supprimer toutes les restrictions et passer à Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Passer à Premium" image="/docs/guide/evervideo/img/evervideo-upgrade-to-premium.webp" >}}
{{< /cards >}}

**Family Sharing** est activé pour tous les achats et abonnements, vous pouvez donc partager la version Premium avec jusqu'à cinq membres de votre famille sans frais supplémentaires.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Sélectionner un plan Premium" image="/docs/guide/evervideo/img/evervideo-select-premium-plan.webp" >}}
{{< /cards >}}

## Partage des achats entre iOS et Mac

Les achats à vie et les abonnements sont partagés entre iOS et Mac via **iCloud** pour synchroniser ces informations. Si vous avez Premium sur votre appareil iOS, assurez-vous d'avoir la dernière version installée et qu'iCloud est activé. Démarrez l'application sur iOS et attendez une minute pour que les informations d'achat soient téléchargées sur iCloud, puis lancez la version Mac — Premium devrait s'activer automatiquement.

Vous pouvez également appuyer sur le bouton **Restaurer les achats** dans les paramètres de l'application. Assurez-vous d'avoir une connexion Internet et d'être connecté au même compte iCloud et App Store sur les deux appareils.

## Restaurer les achats sur un nouvel appareil

Pour restaurer votre achat sur un nouvel appareil, utilisez le menu **Achats → Restaurer les achats**. Vous verrez la liste de vos achats. Si vous ne les voyez pas tous, confirmez que l'appareil est connecté au même identifiant Apple que celui utilisé pour effectuer les achats, et assurez-vous qu'iCloud est activé.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Menu Achats dans les paramètres" image="/docs/guide/evervideo/img/evervideo-purhases-menu-in-settings.webp" >}}
{{< /cards >}}

## Essayer Premium gratuitement

Vous pouvez passer à la version Premium gratuitement, pour une durée limitée, en utilisant ce menu. Regardez simplement une publicité ou parlez de l'application à vos amis.

## Mise à jour logicielle

Appuyez sur **Mise à jour logicielle** pour vérifier si une version plus récente d'Evervideo est disponible sur l'App Store.

## Nouveautés

Ce menu est disponible après la sortie d'une nouvelle version. Il affiche un résumé des modifications et des nouvelles fonctionnalités de la mise à jour la plus récente.

## Lecteur

Tout ce qui concerne la lecture se trouve ici — audio, vidéo, sous-titres, appareils, personnalisation, cache et minuterie de veille.

### Général

Ces paramètres couvrent les aspects fondamentaux du lecteur.

- **Mode de répétition** — choisissez comment le lecteur se comporte lorsqu'une vidéo se termine :
  - **Répéter tout** — rejoue toutes les vidéos de votre file d'attente.
  - **Répéter un** — répète uniquement la vidéo en cours.
  - **Arrêt répétition** — met en pause lorsque la vidéo en cours se termine.
  - **Pas de répétition** — lit la file d'attente une seule fois sans répétition.
- **Mode aléatoire** — randomisez l'ordre des vidéos dans votre file d'attente (**Activé** ou **Désactivé**).
- **Enregistrer la position de lecture** — enregistre et restaure la position de lecture pour les vidéos de votre bibliothèque.
- **Enregistrer l'état du lecteur** — préserve l'état du lecteur avant de fermer l'application, afin de reprendre là où vous vous étiez arrêté.

### Vidéo

Configurez la façon dont Evervideo décode et affiche la vidéo.

- **Décodage matériel H.264** — activez/désactivez le décodage AVC accéléré par le matériel. Utilisez-le lorsque les performances de la batterie et thermiques sont importantes ; désactivez-le pour la compatibilité avec les profils exotiques.
- **Décodage matériel H.265 (HEVC)** — idem pour HEVC. Les iPhone, iPad et Mac modernes décodent efficacement HEVC.
- **Format de pixel préféré** — choisissez le format de pixel que le lecteur présente au moteur de rendu (les valeurs par défaut sont optimisées pour l'appareil).
- **FPS préféré** — définissez un FPS de lecture cible. Utile pour correspondre à un taux de rafraîchissement d'écran spécifique.
- **Mode de mise à l'échelle vidéo** — Ajuster / Remplir / Étirer / Original. Détermine comment l'image remplit la zone d'affichage.
- **Mode d'affichage vidéo** (iOS / iPadOS) — comment la vidéo est présentée dans la vue du lecteur.
- **Rotation vidéo** — faites pivoter manuellement l'image à 0° / 90° / 180° / 270° (utile pour les vidéos enregistrées avec une mauvaise orientation).
- **Égaliseur vidéo** — ajustez la luminosité, le contraste, la saturation et la teinte avec un aperçu en temps réel. Les préréglages personnalisés peuvent être **exportés et importés**.
- **Vue VR** (iOS / iPadOS) — pour les vidéos sphériques à 360°. Faites glisser pour regarder autour, pincez pour zoomer.
- **Picture-in-Picture (PiP)** (iOS / iPadOS) — activez le support PiP ; l'application basculera vers une fenêtre de lecteur flottante lorsque vous mettrez l'application en arrière-plan ou appuierez sur le bouton PiP.

### Audio

Configurez la lecture et la sortie audio.

- **Piste audio** — choisissez le flux audio lorsqu'une vidéo en a plusieurs (commentaire, doublage, etc.).
- **Égaliseur audio** — égaliseur 10 bandes avec préréglages et préamplificateur. Les préréglages personnalisés peuvent être exportés / importés.
- **Fréquence d'échantillonnage de sortie audio** — 44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz, 96 kHz. Utile avec les DAC externes.
- **Nombre de canaux de sortie audio** — Mono, Stéréo, 5.1, ITU BS.775-1, SDDS, et plus.
- **Durée du tampon IO de sortie audio préféré** — la valeur typique pour la lecture haute résolution à faible latence est d'environ 5 ms (0,005 s). Ajustez selon votre matériel.
- **Mode de sortie audio** (iOS uniquement) — le mode mixte permet à l'audio d'Evervideo de se mélanger avec d'autres applications.

### Sous-titres

Evervideo inclut une prise en charge complète des sous-titres.

- **Piste de sous-titres** — choisissez parmi les pistes de sous-titres intégrées dans le fichier.
- **Fichier de sous-titres externe** — chargez un fichier `.srt`, `.vtt`, `.ass` ou `.ssa` externe depuis votre appareil ou tout service cloud connecté.
- **Police** — choisissez une police pour la piste de sous-titres principale.

### Appareils (iOS/iPadOS uniquement)

Choisissez un appareil **AirPlay** ou **Google Chromecast** pour la sortie vidéo.

### Personnalisation

- **Style de mise en page du lecteur** — Minimal (par défaut pour Evervideo), Bas, Antique, Classique, et plus.
- **Actions de l'écran principal** — choisissez les boutons qui apparaissent sur l'écran principal du lecteur.
- **Commandes de l'écran de verrouillage** — Sauter le temps, Ajouter un signet, Ajouter aux favoris.
- **Intervalles de saut** — choisissez l'intervalle de temps pour les boutons de saut (5 s, 10 s, 15 s, 30 s, etc.).
- **Style de défilement des pochettes d'album** — style de défilement préféré pour les pochettes.
- **Éléments supplémentaires** — Infos de format audio, Curseur de volume.

### Chargement des fichiers

Configurez la façon dont les données vidéo sont diffusées depuis le réseau.

- **Type de réseau** — Wi-Fi uniquement, ou Wi-Fi + Cellulaire.
- **Temps de préchargement** — longueur du tampon pour une lecture plus fluide sur les réseaux lents.
- **Utiliser l'URL directe** — lorsque pris en charge, utilisez une URL directe pour un chargement plus rapide.

### Cache de lecture

Les vidéos dans la file d'attente du lecteur sont automatiquement téléchargées pour assurer une lecture fluide. Vous pouvez désactiver cette option ou configurer la taille du cache ici.

### Minuterie de veille

Activez une minuterie pour arrêter automatiquement la lecture après une période spécifiée. Appuyez sur l'icône de configuration pour le **mode précis** avec une granularité minute par minute.

## Médiathèque

Gérez la synchronisation automatique, les métadonnées, les pochettes d'album, les listes de lecture, les éléments récents et les favoris.

### Lecture des métadonnées

Lorsque vous ajoutez des vidéos à la bibliothèque, le lecteur de métadonnées les analyse en arrière-plan et les organise par Album et Genre. Vous pouvez ajuster la vitesse d'analyse, désactiver le lecteur ou déclencher une réanalyse complète avec **Recharger les métadonnées**. **Normaliser l'encodage des métadonnées** corrige automatiquement les encodages de caractères incorrects (fréquent avec les fichiers de PC Windows).

### Synchronisation en ligne

Ajoutez automatiquement des vidéos depuis les services cloud connectés et les serveurs multimédia à votre bibliothèque. Choisissez les dossiers à analyser, configurez la fréquence de synchronisation de l'application et démarrez/arrêtez la synchronisation manuellement. La synchronisation en ligne s'exécute uniquement pendant que l'application est active — pour les grandes bibliothèques, utilisez la version bureau puis transférez la bibliothèque synchronisée avec **Sauvegarde et restauration**.

### Synchronisation hors ligne

Lorsque vous marquez un dossier cloud comme disponible hors ligne, il apparaît dans **Fichiers → Dossiers hors ligne** et est téléchargé automatiquement. Les nouveaux fichiers ajoutés en ligne sont également téléchargés. Configurez l'intervalle de temps et déclenchez des synchronisations manuelles depuis cet écran.

### Personnalisation

- **Style de l'écran de médiathèque** — Menu simple, Menu groupé, Menu à onglets.
- Activez ou désactivez l'affichage de grandes pochettes d'album dans les écrans de détail.

### Pochettes d'album

- **Type de réseau** — Wi-Fi ou Wi-Fi + Cellulaire.
- **Charger les pochettes d'album pour les fichiers en ligne** — extraire les illustrations intégrées des fichiers cloud (utilise des données supplémentaires).
- **Rechercher dans le dossier** — utiliser des images JPEG / PNG dans le même dossier lorsqu'une vidéo n'a pas de pochette intégrée.
- **Qualité de la pochette** — ajustez la résolution à laquelle les pochettes sont mises en cache.
- **Afficher dans le dossier** / **Tout supprimer** — gérez le cache des illustrations.

### Listes de lecture

Activez l'ajout de la même vidéo deux fois dans une liste de lecture (désactivé par défaut).

### Récents

Gérez la liste des vidéos récemment lues — modifiez la taille, supprimez ou exportez en M3U / CSV / TXT.

### Favoris

- **Édition simultanée** — miroir des favoris entre la médiathèque et la section fichiers.
- **Supprimer la liste** — effacez la liste des favoris.
- **Exporter la liste** — exportez les favoris en M3U / CSV / TXT.

### Supprimer la médiathèque

Effacez la base de données de la médiathèque. Vos fichiers vidéo et audio sur le stockage restent intacts.

## Code d'accès

Protégez Evervideo avec un **code d'accès numérique à 4 chiffres**. Lorsqu'il est activé, vous serez invité à saisir le code d'accès à chaque lancement de l'application. Combinez-le avec Face ID / Touch ID iOS sur l'appareil pour une protection supplémentaire.

## Gestionnaire de fichiers

Contrôle la façon dont les fichiers sont transférés, stockés et prévisualisés.

- **Transferts de fichiers** — préférence réseau (Wi-Fi uniquement ou Wi-Fi + Cellulaire).
- **Nombre maximum de tâches parallèles** — définissez le nombre de fils de téléchargement parallèles.
- **Tâches de transfert de fichiers** — voir les téléchargements et envois actuellement actifs.
- **Transferts en arrière-plan** — autoriser les téléchargements pendant que l'application est en arrière-plan.
- **Enregistrer les fichiers téléchargés dans** — répertoire de téléchargements par défaut.
- **Dossiers hors ligne synchronisés** — gérez les dossiers en mode hors ligne.
- **Intervalle de temps** — fréquence à laquelle les dossiers hors ligne sont vérifiés pour les modifications.
- **Afficher les noms de fichiers complets** — affichez les extensions dans le gestionnaire de fichiers.
- **Modifier les fichiers en ligne** — désactivez pour passer en mode lecture seule pour les services cloud connectés.
- **Copier les fichiers à l'ouverture** — comment gérer les fichiers importés d'autres applications.
- **Miniatures pour les fichiers** — gérez les miniatures de fichiers générées.
- **Supprimer les fichiers temporaires** — videz le dossier cache de l'application.

## Wi-Fi Drive

Activez Wi-Fi Drive pour transférer des fichiers d'un ordinateur vers votre appareil via un navigateur web de bureau, Finder ou l'Explorateur de fichiers. Des instructions détaillées sont disponibles [ici](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Widgets

Activez les widgets pour que l'application mette à jour les données des widgets pendant la lecture. Les mises à jour des widgets nécessitent de l'énergie supplémentaire, donc le bouton est désactivé par défaut — activez-le uniquement si vous utilisez réellement des widgets sur votre écran d'accueil ou écran de verrouillage.

Vous pouvez ajouter des widgets Evervideo en appuyant longuement sur votre écran d'accueil ou écran de verrouillage, en appuyant sur **+**, en recherchant **Evervideo** et en choisissant une taille de widget. Les widgets affichent la vidéo en cours de lecture et ouvrent directement le lecteur plein écran. Les widgets fonctionnent également sur macOS dans le Centre de notifications.

## Personnalisation

Personnalisez l'interface utilisateur selon vos préférences.

- **Icône de l'application** — icône d'écran d'accueil alternative (Premium).
- **Schéma de couleurs** — Sombre, Clair ou Par défaut (suit l'apparence de votre système).
- **Style d'arrière-plan** — Pochette d'album floutée ou couleur unie.
- **Apparence des éléments dans la liste** — ajustement automatique de la hauteur des lignes ; afficher des miniatures plus petites.
- **Limite de chargement du contenu** — activer/désactiver la pagination.
- **Style de l'écran Fichiers** — Menu simple ou Menu groupé.
- **Style de l'écran Médiathèque** — Menu simple / Groupé / À onglets.
- **Style de l'écran Lecteur** — Minimal / Bas / Antique / Classique.
- **Style du menu contextuel** — menu système ou style feuille inférieure.

## Fenêtre

Disponible sur Mac et Catalyst. Configurez les préférences liées à la fenêtre telles que la taille par défaut et le comportement au lancement.

## Écran

Choisissez si l'écran doit rester actif pendant que vous utilisez l'application.

## Accessibilité

Activez le **Mode texte** pour masquer les images dans l'interface utilisateur. Le mode texte est activé automatiquement lorsque VoiceOver est actif.

## Langue

Changez la langue de l'application et remplacez la langue par défaut du système. Le changement s'applique après avoir complètement quitté et rouvert Evervideo. Plus de 120 langues sont prises en charge.

## Sauvegarde et restauration

Sauvegardez toutes vos données d'application ou migrez-les vers un autre appareil. Choisissez ce qu'il faut inclure :

- **Base de données** — vos entrées de médiathèque, listes de lecture, évaluations, favoris, historique de visionnage. Les fichiers hors ligne ne sont pas inclus pour garder la taille du fichier gérable.
- **Pochettes d'album** — vos illustrations en cache.
- **Paramètres** — vos paramètres d'application.

Appuyez sur **Sauvegarder les données de l'application** pour démarrer la sauvegarde. Pour restaurer sur un nouvel appareil, déplacez le fichier de sauvegarde via iCloud Drive, AirDrop ou tout service cloud connecté et ouvrez-le sur le nouvel appareil.

## Aide

Accédez au guide de l'application pour obtenir de l'aide et des conseils sur l'utilisation efficace de l'application.

## Foire aux questions

Trouvez des réponses aux questions courantes dans la section FAQ.

## Envoyer des commentaires

Envoyez vos commentaires à notre équipe d'assistance directement depuis l'application, avec des informations de diagnostic jointes automatiquement.

## Partager cette application

Partagez Evervideo avec vos amis pour faire connaître l'application.

## Découvrir d'autres applications

Explorez d'autres applications d'Everappz.

## Conditions d'utilisation

Lisez les conditions d'utilisation avant d'utiliser l'application.

## Politique de confidentialité

Lisez la politique de confidentialité pour comprendre nos pratiques de gestion des données.

## Analyses et collecte de données

Vérifiez quels services sont activés pour l'analyse et la collecte de données et désactivez ceux que vous ne souhaitez pas.

## Mentions légales

Informations sur chaque bibliothèque utilisée dans l'application ainsi que le numéro de version et les informations de build.
