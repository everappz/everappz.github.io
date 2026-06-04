---
title: "Éditeur de tags"
date: 2020-02-01
description: "Apprenez à utiliser l'éditeur de tags Evertag pour mettre à jour les métadonnées musicales, modifier les pochettes d'album, modifier plusieurs fichiers en lot et gérer les tags depuis MusicBrainz. Idéal pour organiser votre bibliothèque musicale sur iOS et Mac."
keywords: [
  "éditeur de tags Evertag", "éditeur de métadonnées audio", "éditeur de tags musicaux",
  "modifier les tags audio iPhone", "éditeur de pochettes d'album", "modifier les tags audio en lot",
  "métadonnées MusicBrainz", "application organisatrice de musique", "guide Evertag", "éditeur de tags ID3"
]
tags: ["guide", "evertag", "éditeur de tags"]
readingTime: 5
---


L'**Éditeur de tags** est l'écran principal de l'application Evertag où vous pouvez afficher et modifier les métadonnées des fichiers audio. Ouvrez cet écran en appuyant sur un fichier dans la section **Fichiers locaux** ou depuis n'importe quel compte de **stockage cloud** connecté.

{{< cards cols="1">}}
  {{< card title="" subtitle="Écran de l'éditeur de tags Evertag" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Modes d'édition

Evertag fournit deux modes d'édition :

- **Mode fichier unique**
  - Naviguez entre les fichiers en faisant glisser vers la gauche ou la droite sur le carrousel d'illustrations.

- **Mode lot**
  - Modifiez plusieurs fichiers à la fois et appliquez des métadonnées partagées.
  - Pour l'activer, faites défiler vers le bas et appuyez sur **Modifier plusieurs fichiers simultanément**.

## Mode fichier unique

Par défaut, l'application ouvre l'éditeur de tags en mode fichier unique avec uniquement les options d'édition principales activées. Dans ce mode, vous pouvez modifier les champs de métadonnées les plus courants, tels que :

**Titre de la piste, Sous-titre, Artiste de l'album, Album, Artiste, Compositeur, Interprète, Genre, Commentaire, Battements par minute, Podcast, Compilation, Numéro de disque, Numéro de piste, Total de pistes, Évaluation, Année**

Pour accéder à tous les tags disponibles, faites défiler vers le bas de l'écran et appuyez sur l'option **Afficher les tags étendus**. Cela basculera l'éditeur en mode étendu, vous permettant de modifier plus de **120 champs de métadonnées**, y compris les **Tags MusicBrainz**, les **Paroles**, les **Évaluations de contenu**, les valeurs de replay-gain, les ordres de tri, les métadonnées de podcast, etc. Utilisez **Paramètres → Éditeur de tags audio → Boutons sur l'écran principal** pour activer définitivement Afficher les tags étendus de sorte qu'il soit toujours activé.

{{< cards cols="1">}}
{{< card title="" subtitle="Panneau d'actions bas" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Mode lot

Vous pouvez entrer en édition par lot de deux façons :

1. **Depuis le gestionnaire de fichiers**
   - Appuyez sur **Plus d'actions** (•••) en haut à droite.
   - Appuyez sur **Sélectionner**, choisissez plusieurs fichiers, puis appuyez sur **Modifier les balises audio**.

2. **Depuis l'éditeur de tags**
   - Ouvrez n'importe quel fichier, faites défiler vers le bas et appuyez sur **Modifier les fichiers simultanément** pour charger tous les fichiers du même dossier.

{{< cards cols="1">}}
{{< card title="" subtitle="Mode d'édition par lot" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Après l'édition, appuyez sur **Enregistrer** pour appliquer les modifications.

## Modifier les paroles

L'éditeur étendu expose le champ **Paroles**. Appuyez dessus pour ouvrir la liste des paroles — chaque entrée de paroles a sa propre langue et description, donc une seule piste peut stocker plusieurs traductions.

Vous n'avez pas à taper les paroles depuis le début. L'éditeur inclut des raccourcis de recherche en un tap vers les bases de données de paroles les plus populaires sur le web, pré-remplis avec l'artiste et le titre de la piste actuelle :

- **Lrclib** — la base de données publique de référence pour les **paroles synchronisées (style LRC)**. Utilisez-la lorsque vous voulez des paroles synchronisées qui défilent ligne par ligne dans les lecteurs qui les prennent en charge.
- **Genius** — grand catalogue avec annotations et paroles en texte simple précises.
- **Lyricsify** — base de données communautaire avec paroles simples et horodatées.
- **Google** — une recherche web générale comme solution de secours lorsque les bases de données dédiées n'ont pas de correspondance.

Chaque raccourci n'apparaît que lorsque le service correspondant est accessible depuis votre appareil. Appuyez sur un service, copiez les paroles (ou les horodatages LRC) que vous souhaitez, revenez à Evertag et collez-les dans le champ de texte — puis **Enregistrer** pour écrire les paroles dans les tags du fichier audio.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pages de paroles" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Sélectionnez une langue depuis le sélecteur :

{{< cards cols="1">}}
  {{< card title="" subtitle="Sélecteur de langue des paroles" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Ensuite collez ou tapez le texte des paroles. Evertag prend en charge à la fois le texte brut et les paroles horodatées (synchronisées) — le texte indicatif montre un exemple du format de style LRC, qui est exactement ce que Lrclib et Lyricsify retournent pour les résultats synchronisés.

{{< cards cols="1">}}
  {{< card title="" subtitle="Éditeur de texte des paroles" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Définir une évaluation et une évaluation de contenu

L'éditeur étendu offre un contrôle d'**Évaluation** par étoiles ainsi qu'un contrôle segmenté d'**Évaluation de contenu**.

### Évaluation par étoiles

Utilisez le champ **Évaluation** pour donner à une piste un score personnel d'une à cinq étoiles. La valeur est écrite dans le tag d'évaluation standard du fichier (POPM pour ID3, `rate` pour MP4, `RATING` pour Vorbis/APE, etc.), de sorte que les autres applications qui lisent ce tag — y compris l'application Musique, Plex, Roon et la plupart des éditeurs de tags de bureau — récupèreront immédiatement vos scores.

{{< cards cols="1">}}
  {{< card title="" subtitle="Évaluation" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Évaluation de contenu

L'**Évaluation de contenu** marque le contenu d'une piste en utilisant l'une des valeurs de la norme de contrôle parental utilisée par l'iTunes Store et la plupart des plateformes musicales :

- **Inoffensif** — la valeur par défaut pour les pistes sans informations de contrôle parental. Le fichier est traité comme adapté à tous les auditeurs et n'affichera aucune étiquette d'avertissement dans les lecteurs qui respectent le tag.
- **Explicite** — la piste contient un langage ou un contenu explicite. Les lecteurs qui respectent les contrôles parentaux (l'application Musique, l'application Apple TV, les exportations Spotify, Plex, etc.) afficheront un badge **E** à côté du titre et, lorsque des restrictions sont activées sur l'appareil ou le compte, peuvent masquer la piste des profils pour enfants ou refuser de la lire.
- **Propre** — une version censurée ou modifiée d'une piste autrement explicite. Les lecteurs affichent un badge **C** afin que les auditeurs puissent distinguer une version propre de la version explicite originale, ce qui est utile lorsque les deux versions vivent dans la même bibliothèque.

Vous voudrez définir ou corriger ce champ lorsque :

- Un fichier a la mauvaise étiquette (par exemple une version radio propre qui a été incorrectement taguée comme Explicite, ou vice versa).
- Les pistes ont été extraites ou téléchargées sans le tag et apparaissent maintenant comme Inoffensives même si elles contiennent du contenu explicite — nécessaire pour que les contrôles parentaux et les bibliothèques partagées en famille fonctionnent correctement.
- Vous préparez un album pour soumission ou partage et avez besoin que chaque piste porte des métadonnées cohérentes.
- Vous voulez que CarPlay, l'écran de verrouillage, les lecteurs de style Apple Music ou les logiciels DJ affichent le badge **E** / **C** correct à côté du titre de la piste.

La valeur est stockée dans le champ d'évaluation de contenu standard pour le format de fichier (`rtng` pour MP4, `TXXX:ITUNESADVISORY` pour ID3, `ITUNESADVISORY` pour Vorbis), de sorte que tout lecteur qui lit les métadonnées de contrôle parental verra votre mise à jour.

{{< cards cols="1">}}
  {{< card title="" subtitle="Évaluation de contenu des paroles" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Modifier la pochette d'album

Pour changer une pochette d'album :

1. Appuyez sur l'**icône Appareil photo** dans le carrousel d'illustrations.
2. Choisissez l'emplacement de l'image : Fichiers locaux, Cloud, Téléchargements ou Bibliothèque de photos.
3. Sélectionnez une image à appliquer comme illustration de couverture.

{{< cards cols="1">}}
  {{< card title="" subtitle="Sélectionner une image" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Plus d'actions dans l'éditeur de tags

Des options d'édition supplémentaires sont disponibles via la barre d'outils sous la vue des illustrations.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Plus d'actions" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Recherche automatique des tags audio

Cette action active le moteur de recherche de tags intelligent, qui trouve et remplit les métadonnées complètes de votre fichier audio en fonction des informations existantes.
L'application utilise la base de données MusicBrainz — l'une des bases de données de tags les plus complètes — avec plus de **50 millions** de pistes.

### Rechercher la pochette d'album

Utilisez les métadonnées pour rechercher la pochette d'album correcte sur le web.

{{< cards cols="1">}}
  {{< card title="" subtitle="Rechercher la pochette d'album" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Une fois trouvée, enregistrez l'image dans vos **Photos** à l'aide du menu contextuel système.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ajouter une image aux photos" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Ensuite, revenez à l'éditeur de tags, appuyez sur l'icône Appareil photo, allez dans **Bibliothèque de photos** et sélectionnez l'image enregistrée. L'application la définira comme la couverture de votre fichier audio.

Vous pouvez ajuster la façon dont les images de couverture sont mises à l'échelle dans les paramètres de l'application.

### Enregistrer la pochette d'album

Cette action enregistre la pochette d'album actuelle dans le dossier **Documents**, afin que vous puissiez la réutiliser plus tard.

### Normaliser l'encodage

Cette action normalisera l'encodage du texte de tous les tags dans les métadonnées du fichier audio. C'est particulièrement utile si vous migrez depuis un PC Windows, où les fichiers peuvent utiliser des encodages différents qui apparaissent comme des caractères illisibles ou corrompus sur un Mac.

### Recherche manuelle des tags

Recherchez les métadonnées d'album manuellement à l'aide de la base de données MusicBrainz.

- Sélectionnez l'album

{{< cards cols="1">}}
  {{< card title="" subtitle="Sélectionner un album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Choisissez la bonne chanson

{{< cards cols="1">}}
  {{< card title="" subtitle="Sélectionner une chanson" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Choisissez les tags à appliquer

{{< cards cols="1">}}
  {{< card title="" subtitle="Sélectionner les tags audio" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Appuyez sur **Terminer** pour appliquer les métadonnées sélectionnées à votre piste.

### Supprimer les tags audio

Effacez tous les champs de métadonnées d'un fichier. Utile pour repartir de zéro. Appuyez sur **Enregistrer** pour confirmer.

## Paramètres de l'éditeur de tags

Accédez à **Paramètres → Éditeur de tags audio** pour personnaliser le comportement.

### Mise à l'échelle des pochettes d'album

Sélectionnez la façon dont les pochettes d'album doivent être mises à l'échelle lors de leur enregistrement dans les fichiers audio. Vous pouvez désactiver la mise à l'échelle pour conserver la taille d'image originale, mais sachez que certains lecteurs peuvent ne pas prendre en charge les fichiers d'illustration volumineux. L'option «taille originale» fait partie des fonctionnalités de personnalisation Premium.

### Options d'enregistrement des tags

- **ID3v2.4** — Lorsque cette option est activée, l'application enregistre les tags au format ID3v2.4 lorsque possible. Désactivez pour revenir à l'ID3v2.3 plus largement pris en charge si vos tags audio ne s'affichent pas correctement sur les anciens lecteurs ou appareils.
- **Tags dupliqués** — Lorsque cette option est activée, les champs de métadonnées communs sont dupliqués dans les deux sections de tags du fichier. Cela améliore la compatibilité avec les anciens lecteurs audio, mais dans la plupart des cas n'est pas nécessaire.

### Options de mise à jour des métadonnées des fichiers cloud

Vous pouvez contrôler la façon dont l'application met à jour les métadonnées pour les fichiers audio stockés dans les services cloud :

- **Afficher le message de confirmation**
  Demander avant d'appliquer les modifications de métadonnées aux fichiers cloud.

- **Mettre à jour automatiquement les métadonnées du fichier**
  Enregistrer les modifications de métadonnées dans le fichier cloud automatiquement après l'édition.

- **Ne pas mettre à jour les métadonnées du fichier**
  Ignorer la mise à jour des fichiers cloud — les modifications s'appliqueront uniquement localement.

### Modifier les fichiers en ligne

Choisissez ce qui arrive aux copies téléchargées localement des fichiers cloud après l'édition :

- **Toujours supprimer le fichier téléchargé**
  Supprimer la copie locale après avoir sauvegardé les modifications.

- **Ne pas supprimer le fichier téléchargé**
  Conserver le fichier téléchargé sur votre appareil après l'édition.

### Boutons de l'écran principal

Personnalisez les actions qui apparaissent sur l'écran principal de l'éditeur de tags (Recherche automatique des tags audio, Recherche manuelle des tags audio, Rechercher la pochette d'album, Enregistrer la pochette d'album, Normaliser l'encodage, Supprimer les tags audio). Vous pouvez également activer **Afficher les tags étendus** et **Modifier les fichiers simultanément** pour que l'éditeur s'ouvre toujours dans votre mode préféré.
