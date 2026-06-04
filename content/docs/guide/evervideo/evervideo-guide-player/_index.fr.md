---
title: "Lecteur multimédia"
date: 2020-02-01
lastmod: 2026-06-01
description: "Apprenez à utiliser le lecteur multimédia Evervideo sur iPhone, iPad et Mac. Picture-in-Picture, décodage matériel accéléré H.264 / HEVC, égaliseurs audio et vidéo, sous-titres primaires et secondaires, sélection de pistes audio et vidéo, mise à l'échelle et rotation vidéo, vitesse de lecture, minuterie de sommeil, AirPlay 2, Google Chromecast, flux RTSP et le lecteur compact toujours visible."
keywords: [
  "guide lecteur Evervideo", "paramètres lecteur vidéo", "égaliseur Evervideo",
  "Picture-in-Picture iPhone", "PiP vidéo iPad", "PiP vidéo Mac",
  "AirPlay 2 vidéo", "Google Chromecast vidéo",
  "sous-titres vidéo iPhone", "sous-titres SRT externes",
  "lecteur de sous-titres ASS SSA", "libass iOS",
  "double sous-titres apprentissage des langues",
  "égaliseur vidéo luminosité contraste", "égaliseur audio lecteur vidéo",
  "verrouillage rotation lecteur vidéo", "mode mise à l'échelle vidéo iOS",
  "décodeur H.264 matériel iPhone", "décodeur HEVC matériel iPad",
  "vitesse lecture vidéo", "lecteur vidéo FFmpeg iOS",
  "lecteur RTSP iPhone", "lecteur vidéo compact",
  "lecteur vidéo VR 360 iPhone"
]
tags: ["guide", "evervideo", "lecteur", "PiP", "sous-titres", "égaliseur vidéo"]
readingTime: 14
---


Le lecteur multimédia est l'écran principal de l'application où vous contrôlez la lecture et la plupart des fonctionnalités d'Evervideo. Il lit à la fois les fichiers vidéo et audio et est construit sur un lecteur personnalisé basé sur FFmpeg avec décodage matériel accéléré H.264 et HEVC qui fait le gros du travail. Voyons comment l'utiliser.

## Accéder au lecteur multimédia

Vous pouvez accéder au lecteur plein écran depuis la barre du lecteur compact. Sur iPhone, le lecteur compact se trouve en haut de l'écran principal. Sur iPad et Mac, il se trouve sur le côté gauche (ou en haut du panneau principal). Pour réduire le lecteur plein écran en vue compacte, appuyez sur le bouton de fermeture dans le coin inférieur droit ou faites glisser vers le bas. Pour masquer complètement le lecteur compact, appuyez et faites glisser une fois de plus vers le bas.

Le lecteur compact reste visible pendant que vous parcourez votre bibliothèque, votre gestionnaire de fichiers ou vos paramètres, afin que vous ne perdiez jamais votre vidéo tout en cherchant la suivante.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lecteur multimédia plein écran Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Formats vidéo et audio pris en charge

Evervideo lit pratiquement tous les conteneurs et codecs modernes grâce au moteur FFmpeg intégré, avec décodage matériel accéléré H.264 et HEVC sur les appareils pris en charge.

- **Conteneurs vidéo :** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — et bien d'autres.
- **Codecs vidéo :** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — plus pratiquement tous les autres codecs que FFmpeg prend en charge.
- **Codecs audio :** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — et bien d'autres.
- **Formats de sous-titres :** SRT, VTT (WebVTT), ASS / SSA, et pistes de sous-titres texte ou image intégrées.
- **Protocoles de streaming :** HTTP / HTTPS, HLS (m3u8), RTSP (caméras IP et IPTV), et streaming direct de fichiers via SMB / WebDAV / FTP / SFTP / NFS / DLNA.

Cela couvre pratiquement tous les fichiers vidéo que vous êtes susceptible de rencontrer — y compris les rips MKV, les flux RTSP de caméras de sécurité et les téléchargements web AV1 webm.

## Contrôles de lecture

En bas de l'écran du lecteur, vous verrez des boutons pour Lecture, Pause, Suivant et Précédent. Il y a également des boutons optionnels comme Avancer et Reculer (10 secondes par défaut) que vous pouvez activer dans les paramètres de l'application. Maintenez les boutons Suivant / Précédent pour avancer rapidement ou reculer. Faites glisser le curseur de lecture pour accéder à n'importe quelle position.

## Répétition et lecture aléatoire

Appuyez sur le bouton de répétition pour parcourir les modes de répétition :

- **Répéter tout** — répète toutes les vidéos de votre file.
- **Répéter un** — répète uniquement la vidéo actuelle.
- **Arrêter à la fin** — met en pause quand la vidéo actuelle se termine.
- **Pas de répétition** — lit la file une seule fois sans répétition.

Utilisez le bouton **Lecture aléatoire** pour randomiser l'ordre des vidéos dans la file.

## Picture-in-Picture (PiP)

Sur iPhone et iPad, Evervideo prend entièrement en charge Picture-in-Picture (PiP). Appuyez sur l'icône PiP sur l'écran du lecteur ou faites simplement basculer Evervideo en arrière-plan — la vidéo continue de se lire dans une fenêtre flottante au-dessus de toutes les autres applications. Faites glisser la fenêtre flottante dans n'importe quel coin ; pincez pour redimensionner ; appuyez une fois pour afficher les contrôles de base lecture / pause / saut ; appuyez sur le petit bouton d'agrandissement pour revenir à Evervideo complet.

PiP fonctionne avec tous les formats vidéo qu'Evervideo lit, y compris les fichiers diffusés depuis le cloud et les flux RTSP. PiP continue également de fonctionner pendant que votre téléphone est verrouillé (selon votre paramètre de verrouillage automatique).

## Lecteur compact

Le lecteur compact est un mini-lecteur persistant qui reste visible en haut de chaque écran de l'application pendant que vous parcourez la bibliothèque, le gestionnaire de fichiers ou les paramètres. Appuyez dessus pour agrandir en lecteur plein écran ; faites glisser vers le bas pour le réduire à nouveau.

{{< cards cols="1">}}
  {{< card title="" subtitle="Paramètres vidéo Evervideo depuis le lecteur compact sur l'écran principal" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

Pour AirPlay, appuyez sur le bouton AirPlay sur le lecteur. Evervideo prend en charge AirPlay 2, vous pouvez donc diffuser de la vidéo vers Apple TV, HomePod ou tout haut-parleur ou smart TV compatible AirPlay 2. Sur une configuration avec plusieurs appareils AirPlay, vous pouvez acheminer l'audio vers plusieurs récepteurs simultanément.

## Google Chromecast

Pour les utilisateurs de Google Cast, l'icône Cast apparaît sur le lecteur. Appuyez dessus pour choisir un appareil et commencer à diffuser. Assurez-vous que votre téléphone et le récepteur Cast sont sur le même réseau Wi-Fi. Tous les codecs ne sont pas pris en charge par le matériel Chromecast — certains fichiers peuvent nécessiter un transcodage.

## Flux RTSP en direct

Evervideo peut lire des sources RTSP directement — caméras IP, caméras de sonnette, flux IPTV, flux de diffusion et tout autre URL `rtsp://`. Ajoutez le flux comme connexion RTSP dans Fichiers → Liens en ligne → Ajouter un lien, puis appuyez dessus pour commencer à regarder. Les flux RTSP fonctionnent en Picture-in-Picture, dans le lecteur compact, et se diffusent via AirPlay 2 et Chromecast comme une vidéo ordinaire.

## Sélection de piste audio

Pour les vidéos avec plusieurs pistes audio (commentaire, doublages en langues alternatives, pistes du réalisateur), appuyez sur le bouton Plus d'actions sur le lecteur et choisissez Piste audio — puis choisissez la piste souhaitée. Essentiel pour les films en langue étrangère, les fichiers BDMV / MKV avec plusieurs doublages, et le contenu pédagogique avec des pistes de commentaires.

## Sélection de piste vidéo

Certains fichiers vidéo incluent plusieurs flux vidéo (Blu-rays multi-angles, montages alternatifs). Choisissez Piste vidéo dans le menu Plus d'actions pour basculer entre eux en cours de lecture.

## Sous-titres — internes et externes

Evervideo vous offre un contrôle précis des sous-titres :

- **Piste de sous-titres** — choisissez parmi les pistes intégrées dans le fichier.
- **Fichiers de sous-titres externes** — chargez des fichiers `.srt`, `.vtt`, `.ass` ou `.ssa` depuis votre appareil, iCloud Drive ou tout service cloud connecté.
- **Rendu Libass** — le style ASS / SSA avancé (polices, couleurs, positions, effets karaoké) est rendu correctement grâce à libass intégré.
- **Sélection de police** — choisissez une police personnalisée pour les sous-titres primaires et une police séparée pour les sous-titres secondaires. Les polices intégrées ainsi que toute police installée sur votre appareil sont disponibles.

Vous pouvez configurer tout cela dans Paramètres → Sous-titres avant la lecture, ou utiliser Plus d'actions → Sous-titres depuis le lecteur pour changer à la volée.

## Égaliseur audio

Evervideo inclut un égaliseur audio complet pour régler les bandes sonores vidéo pour vos écouteurs, haut-parleurs ou système hi-fi. Appuyez sur l'icône de l'égaliseur sur la vue du volume (ou l'action Égaliseur audio sur le menu Plus d'actions du lecteur), activez l'égaliseur avec le commutateur dans le coin supérieur droit, et choisissez un préréglage ou faites glisser les curseurs de bande pour créer le vôtre. Les préréglages personnalisés peuvent être exportés et importés pour les partager entre appareils ou les sauvegarder.

## Égaliseur vidéo

Pour régler l'image, Evervideo fournit un égaliseur vidéo dédié — ajustez la luminosité, le contraste, la saturation et la teinte en temps réel pendant la lecture. Comme l'égaliseur audio, les préréglages vidéo personnalisés peuvent être exportés et importés pour le partage ou la sauvegarde. Utilisez-le pour éclaircir une scène sombre par une journée ensoleillée, booster la saturation sur du contenu délavé, ou réchauffer une dominante froide.

{{< cards cols="1">}}
  {{< card title="" subtitle="Égaliseur vidéo Evervideo" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Mode de mise à l'échelle vidéo

Choisissez comment la vidéo remplit l'écran :

- **Ajuster** — préserver le rapport d'aspect original ; barres noires si nécessaire.
- **Remplir** — remplir tout l'écran, en recadrant la vidéo si nécessaire.
- **Étirer** — étirer la vidéo pour remplir l'écran, en déformant si nécessaire.
- **Original** — conserver la résolution native à 1:1.

## Rotation vidéo

Pour les vidéos enregistrées dans la mauvaise orientation, choisissez **Plus d'actions → Rotation** et sélectionnez **0°**, **90°**, **180°** ou **270°** pour faire pivoter l'image sans quitter le lecteur.

## Décodage matériel (H.264 et HEVC)

Dans Paramètres → Lecteur → Vidéo, vous pouvez activer / désactiver le décodage matériel H.264 et le décodage matériel H.265 (HEVC) indépendamment. Le décodage matériel est plus rapide, utilise moins de batterie et chauffe moins — mais dans de rares cas (fichiers corrompus, profils exotiques), vous devrez peut-être désactiver le décodage matériel et revenir au décodage logiciel FFmpeg. Evervideo vous permet de le faire fichier par fichier depuis le menu Plus d'actions du lecteur.

## Viewport VR 360°

Evervideo inclut un viewport VR / 360° pour les fichiers vidéo sphériques. Lors de la lecture d'une vidéo à 360°, vous pouvez faire glisser pour regarder autour, pincer pour zoomer, et Evervideo déformera le rendu en temps réel.

## Vitesse de lecture

Appuyez sur le contrôle de vitesse sur la barre d'outils du lecteur pour modifier la vitesse de lecture — ralentissez pour l'analyse (0,25× ou 0,5×) ou accélérez pour les tutoriels et les conférences (1,25×, 1,5×, 2×, et jusqu'à 3×). Appuyez sur l'icône de configuration dans le coin supérieur droit de l'écran Vitesse pour passer en mode précis avec des ajustements plus fins. La correction de hauteur par piste est également disponible.

{{< cards cols="1">}}
  {{< card title="" subtitle="Vitesse de lecture Evervideo sur la barre d'outils principale" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## File du lecteur

Pour voir votre file du lecteur, appuyez sur le bouton de file sur le lecteur. Chaque vidéo dans la file a des actions supplémentaires — appuyez sur les trois points pour les voir. Pour réorganiser une vidéo dans la file, utilisez l'indicateur de réorganisation près du titre et faites-le glisser vers une nouvelle position.

{{< cards cols="1">}}
  {{< card title="" subtitle="File de lecture Evervideo" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Minuterie de sommeil

Ouvrez Paramètres → Lecteur → Minuterie de sommeil, activez-la et choisissez combien de temps vous souhaitez que la lecture se poursuive avant de s'arrêter automatiquement. Vous pouvez également ajouter le bouton Minuterie de sommeil directement sur l'écran principal du lecteur via Paramètres → Lecteur → Personnalisation → Actions de l'écran principal.

## Signets du lecteur

Sauvegardez votre position dans les longues vidéos — conférences, livres audio en vidéo, tutoriels, téléchargements YouTube d'une heure — en appuyant sur Ajouter un signet dans le menu Plus d'actions. Les signets apparaissent dans la liste Plus d'actions → Signets de la vidéo et persistent entre les sessions.

## Menu Plus d'actions

Appuyez sur le bouton **Plus d'actions « ... »** sur le lecteur pour accéder à des fonctions supplémentaires.

- **Continuer la lecture** — reprendre la file depuis la dernière position.
- **Rechercher** — trouver une vidéo spécifique dans votre file.
- **Signets** — afficher et accéder aux signets.
- **Vitesse** — ajuster la vitesse de lecture.
- **Récents** — vidéos récemment lues.
- **Favoris** — vidéos en favoris.
- **Égaliseur audio** — activer l'égaliseur audio.
- **Égaliseur vidéo** — activer l'égaliseur vidéo.
- **Piste audio** — choisir le flux audio.
- **Piste vidéo** — choisir le flux vidéo.
- **Sous-titres** — piste primaire / secondaire, fichier externe, police.
- **Rotation** — faire pivoter l'image 0° / 90° / 180° / 270°.
- **Mode de mise à l'échelle** — Ajuster / Remplir / Étirer / Original.
- **Picture-in-Picture** — entrer en mode PiP.
- **AirPlay** / **Chromecast** — envoyer vers un appareil.
- **Minuterie de sommeil** — définir un minuteur pour arrêter la lecture.
- **Enregistrer la file en liste de lecture** — sauvegarder la file actuelle comme nouvelle liste de lecture.
- **Supprimer la file** — vider la file et arrêter la lecture.
- **Paramètres** — accéder directement aux paramètres du lecteur.
- **Aide** — ouvrir les conseils.

{{< cards cols="1">}}
  {{< card title="" subtitle="Écran Plus d'actions du lecteur Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Paramètres du lecteur

L'arborescence complète des paramètres du lecteur est documentée dans le [guide Paramètres](/docs/guide/evervideo/evervideo-guide-settings/). Les sections les plus utilisées :

- **Général** — Mode de répétition, mode lecture aléatoire, enregistrer l'état du lecteur, enregistrer la position de lecture, intervalles de saut.
- **Vidéo** — Décodage matériel H.264 / HEVC, égaliseur vidéo, mode de mise à l'échelle, rotation, mode d'affichage, FPS préféré, format de pixel préféré, viewport VR.
- **Audio** — Égaliseur audio, taux d'échantillonnage, canaux, durée du tampon IO, mode mixte.
- **Sous-titres** — Piste primaire / secondaire, sélection de fichier externe, police, police secondaire.
- **Appareils** (iOS) — AirPlay / Chromecast.
- **Personnalisation** — Style de disposition du lecteur (Minimal / Bas / Antique / Classique), actions de l'écran principal, contrôles de l'écran de verrouillage.
- **Cache de lecture** — cache disque pour un streaming plus fluide.
- **Minuterie de sommeil** — arrêt automatique.

## Accessibilité

Evervideo est entièrement accessible avec VoiceOver. Chaque composant a une étiquette et une description bien conçues. Lorsque VoiceOver est actif, l'application passe en Mode texte de sorte que seuls les éléments significatifs sont affichés — améliorant la vitesse de navigation et la clarté. Vous pouvez également activer le Mode texte dans Paramètres → Accessibilité → Mode texte.

### Ajuster les curseurs avec VoiceOver

1. **Sélectionnez le curseur** — balayez vers la gauche ou la droite jusqu'à ce que VoiceOver l'annonce.
2. **Ajustez la valeur** — double-appuyez et maintenez le curseur, puis faites glisser vers le haut ou le bas pour modifier rapidement la valeur. VoiceOver annonce la nouvelle valeur au fur et à mesure.

Les autres composants fonctionnent comme prévu, en utilisant les modèles VoiceOver fournis par le système.
