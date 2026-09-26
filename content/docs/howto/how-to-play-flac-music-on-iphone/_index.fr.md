---
title: "Comment lire de la musique FLAC (sans perte) sur mon iPhone"
date: 2024-01-29
lastmod: 2026-09-26
description: "Comment lire du FLAC sur iPhone et iPad en 2026 avec Flacbox, un lecteur haute résolution prenant en charge plus de 120 formats, une sortie jusqu'à 384 kHz, les DAC USB, un égaliseur 10 bandes, le moteur audio BASS, des effets en temps réel comme la réverbération et le delay, un processeur DSP et un visualiseur musical avec 500 presets. Diffusez depuis le cloud ou un NAS et écoutez hors ligne."
keywords: ["comment lire du flac sur iphone", "lecteur flac iphone", "flac", "iphone", "sans perte", "audio haute résolution", "lecteur dsd ios", "dac usb iphone", "384khz", "musique", "flacbox", "diffusion", "hors ligne", "égaliseur", "dsp", "visualiseur musical", "moteur bass"]
tags: ["musique", "cloud", "lecteur", "téléchargeur", "égaliseur", "sans perte", "haute résolution", "hors ligne", "FLAC", "DSD", "DAC", "streamer", "visualiseur", "DSP"]
readingTime: 8
---

{{< author-byline >}}


**En bref :** Pour lire du FLAC sur un iPhone, vous avez besoin d'un lecteur tiers, car l'application Musique d'Apple ne prend pas en charge le FLAC. Installez [Flacbox](/products/flacbox) (c'est gratuit), puis transférez vos fichiers via Wi-Fi Drive ou USB, ou connectez votre stockage cloud ou votre NAS. Votre bibliothèque FLAC est lue en pleine qualité, jusqu'à 384 kHz et 32 bits via un DAC USB. Flacbox lit également plus de 120 formats, dont FLAC, DSD, ALAC, APE, WAV, OGG et OPUS, et il ajoute un égaliseur 10 bandes, le moteur audio professionnel BASS avec des effets en temps réel, un processeur DSP et un visualiseur musical en plein écran.

[{{< figure src="/docs/howto/how-to-play-flac-music-on-iphone/Flacbox_Icon-App-1024x1024.webp" alt="Flacbox Icon - FLAC music player and downloader" width="160" >}}](/products/flacbox)

## Pourquoi mon iPhone ne lit-il pas le FLAC nativement ?

Apple possède son propre format sans perte appelé ALAC (Apple Lossless), et l'application Musique est conçue autour de celui-ci plutôt que du FLAC. Depuis iOS 11, l'application Fichiers peut prévisualiser un seul fichier FLAC, mais elle n'a pas de bibliothèque musicale, pas de playlists, pas de file d'attente, pas d'égaliseur et pas de diffusion depuis le cloud. C'est un visualiseur de fichiers, pas un lecteur de musique.

Vous avez donc deux vraies options :

1. Lire le FLAC avec une application de lecture, afin que vos fichiers restent exactement tels quels. C'est celle que nous recommandons.
2. Convertir le FLAC en ALAC, ce qui est du sans perte vers du sans perte, puis synchroniser avec l'application Musique.

Si vous avez une véritable collection FLAC, la première option est meilleure. Vous évitez une bibliothèque en double, vous économisez le temps de conversion, et vos dossiers et votre qualité haute résolution restent intacts. Flacbox est conçu exactement pour cela.

## Option 1 : lire le FLAC avec Flacbox

Flacbox est un lecteur de musique haute résolution pour iPhone, iPad et Mac. Il transforme votre stockage cloud, votre NAS ou votre ordinateur en votre propre bibliothèque musicale privée, sans conversion et sans abonnement.

### Étape 1. Installer Flacbox

Flacbox se télécharge gratuitement et fonctionne sur iPhone, iPad et Mac.

{{< app-details product="flacbox" >}}

### Étape 2. Importer vos fichiers FLAC

Choisissez la méthode la plus simple pour vous :

- **Wi-Fi Drive** — ouvrez Connexions, puis Ordinateur, puis Se connecter en Wi-Fi, et glissez-déposez vos fichiers depuis n'importe quel navigateur de bureau. Consultez le [guide Wi-Fi Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).
- **Stockage cloud** — connectez iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, pCloud, Proton Drive et 20 autres, puis diffusez directement depuis le cloud.
- **NAS ou ordinateur** — connectez-vous via SMB, WebDAV, DLNA, FTP, SFTP ou NFS (Synology, QNAP, WD My Cloud, Time Capsule ou tout partage Samba). La liste complète se trouve dans le [guide des Connexions](/docs/guide/flacbox/flacbox-guide-connections).
- **Clé USB** — branchez une SanDisk iXpand ou tout lecteur externe et écoutez [directement depuis le lecteur](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it), sans importation.
- **Partage de fichiers iTunes ou Finder** — via un câble Lightning ou USB-C.

### Étape 3. Appuyez sur Lecture

Vos morceaux apparaissent dans la bibliothèque avec les tags et les pochettes lus directement dans les fichiers, regroupés par Album, Artiste, Genre et Compositeur. Chaque morceau affiche son codec et sa résolution exacts, par exemple FLAC, 96 kHz, 24 bits.

## Sortie haute résolution, DAC USB et multicanal

Flacbox est conçu pour les personnes soucieuses de la qualité sonore, pas seulement de l'écoute occasionnelle :

- **Fréquence d'échantillonnage** — lecture de 8 kHz jusqu'à 384 kHz, avec une sortie multicanal de 1 à 7 canaux (jusqu'à 5.1 et ITU BS.775-1).
- **Prise en charge des DAC USB** — tout ce qui dépasse 48 kHz est lu à sa véritable résolution via un DAC USB. Sur la sortie propre de l'iPhone, iOS rééchantillonne l'audio comme il le fait pour chaque application, donc un DAC est le moyen d'obtenir une haute résolution bit-perfect.
- **Sortie réglable** — définissez la fréquence d'échantillonnage, le nombre de canaux et la durée du tampon IO (autour de 5 ms pour une haute résolution à faible latence) dans Paramètres, puis Lecteur audio.
- **Hauteur et vitesse** — correction fine de la hauteur, ainsi qu'une vitesse de lecture de 0.02× à 3.00×.

## Lit plus de 120 formats, pas seulement le FLAC

En plus du FLAC, Flacbox intègre FFmpeg pour lire des formats qu'iOS ne peut pas ouvrir seul. Vous n'avez pas besoin de convertir ou de nettoyer une bibliothèque mixte au préalable :

- **Sans perte et haute résolution** — FLAC, ALAC, WAV, AIFF, APE, WV (WavPack) et DSD (DSF et DFF, y compris DSD64, DSD128 et DSD256).
- **Avec perte** — MP3, AAC, M4A, OGG, OPUS, WMA, MPC et plus encore.
- **Musique tracker et MOD** — les fichiers chiptune et demoscene classiques MOD, XM, IT, S3M, MTM, UMX et MO3 que la plupart des lecteurs ne peuvent pas ouvrir.

Cela fait plus de 120 formats au total, ce qui couvre à peu près tout ce que contient une collection musicale moderne.

## Trois moteurs audio, dont le moteur BASS

Vous pouvez choisir le moteur de lecture dans Paramètres, puis Lecteur audio, puis Codec audio :

- **System Codec + FFmpeg** — compatibilité et stabilité maximales.
- **FFmpeg** — force le chemin FFmpeg, ce qui débloque la correction de la hauteur et une fréquence d'échantillonnage de sortie personnalisée.
- **Moteur BASS™** — le cœur de lecture professionnel ajouté dans [Flacbox 7.6](/blog/flacbox-7-6-bass-audio-engine-effects-dsp-music-visualizer). Il débloque les effets audio en temps réel, le processeur DSP, le visualiseur musical, la lecture tracker et MOD, et un rééchantillonnage de haute qualité. Il ajoute aussi un contrôle indépendant de la hauteur (±60 semitones) et un contrôle du tempo (0.1× à 4×).

## Égaliseur 10 bandes, amplification des basses et préampli

Flacbox comprend un égaliseur graphique 10 bandes avec des presets à la manière de l'iPod, comme Acoustique, Amplificateur de basses, Rock, Pop, Jazz, Classique et Dance. Il y a un préamplificateur pour rehausser les morceaux trop discrets sans saturation, et vous pouvez enregistrer vos propres presets. Réglez-le pour des écouteurs intra-auriculaires, un HomePod ou un autoradio. Pour une présentation complète, consultez le [guide de l'égaliseur](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Égaliseur du lecteur audio Flacbox" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Effets audio en temps réel

Lorsque le moteur BASS est activé, vous obtenez onze effets en temps réel que vous pouvez cumuler et ajuster pendant la lecture. Rien n'est réencodé, et désactiver un effet ramène le son original immédiatement :

- **Réverbération** — d'une petite pièce à une cathédrale.
- **Delay et écho multi-tap** — d'un slapback serré à une longue traîne d'ambiance.
- **Crossfeed** — mélange les canaux stéréo pour que le casque sonne davantage comme de vraies enceintes sur les mixages fortement pannés.
- **Compresseur** — égalise les parties fortes et faibles, ce qui est idéal pour la voiture ou la salle de sport.
- **Chorus, Flanger, Phaser, Auto-Wah, Distorsion et rotation stéréo** — des effets de modulation créatifs et de caractère.

Flacbox propose aussi un nivellement automatique du volume basé sur la norme de sonie EBU R128 de qualité broadcast. Les albums et les playlists en lecture aléatoire sont diffusés à un niveau constant, pour que vous n'ayez pas toujours à toucher au volume. Il est livré avec les presets Léger, Standard, Fort et Nuit.

## Créez votre propre processeur DSP

Au-delà des effets, Flacbox vous offre un processeur DSP à 14 filtres en temps réel que vous configurez vous-même. Vous pouvez ajouter des filtres professionnels et des bandes d'EQ paramétriques, de la saturation et un bit crusher, ainsi que des processeurs créatifs comme le tremolo, le ring modulator et la largeur stéréo. Tout s'exécute en direct sur ce que vous lisez, d'un FLAC local à un flux cloud, et les réglages DSP sont même disponibles dans CarPlay.

## Visualiseur musical en plein écran

Flacbox dispose d'un visualiseur musical intégré qui peint des visuels colorés en mouvement au rythme de votre musique. Il utilise le célèbre moteur Milkdrop (projectM) avec 500 presets, rendus avec OpenGL sur iPhone, iPad et Mac. Ouvrez-le depuis le lecteur en appuyant sur le bouton Plus d'actions puis Visualisation. Choisissez un preset, ou utilisez le mode Auto pour les faire défiler toutes les 30 secondes avec un fondu enchaîné en douceur. Pour une aide pas à pas, consultez le guide sur [comment activer le visualiseur musical](/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Visualiseur musical Flacbox (Milkdrop et projectM)" image="/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac/music-visualizer-starfield-sectors-preset.webp" >}}
{{< /cards >}}

## Cloud, NAS et lecture hors ligne

Diffusez directement depuis plus de 30 services cloud, dont iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, pCloud, Proton Drive et Internxt. Vous pouvez aussi connecter des serveurs auto-hébergés comme Plex, Jellyfin, Emby, Subsonic et Navidrome, et tout NAS via SMB, WebDAV, DLNA, FTP, SFTP ou NFS.

Quand vous voulez emporter votre musique, le gestionnaire de téléchargements intégré enregistre des playlists, des artistes, des albums ou des dossiers entiers pour une écoute hors ligne. Le Mode hors ligne synchronise ensuite automatiquement les nouveaux morceaux à mesure qu'ils apparaissent dans le cloud. Vous manquez d'espace ? Videz le cache en un seul geste et continuez à diffuser.

## Tout ce que les mélomanes exigeants veulent d'autre

- **Bibliothèque organisée** — regroupée par Chansons, Albums, Artistes d'album, Artistes, Genres et Compositeurs, avec une recherche rapide qui fonctionne hors ligne.
- **Éditeur de tags ID3** — corrigez les métadonnées désordonnées et les encodages cassés (cyrillique, japonais, chinois) et réécrivez les changements dans le fichier.
- **Playlists** — créez, réorganisez, importez et exportez M3U, M3U8 et CUE, et rendez-les disponibles hors ligne.
- **Apple CarPlay** — un écran dédié en voiture pour la bibliothèque, le cloud, la musique locale et hors ligne, avec l'égaliseur à bord.
- **AirPlay 2 et Chromecast** — diffusez vers des HomePod, une Apple TV et des enceintes compatibles Cast.
- **Outils pour livres audio** — plusieurs signets, une vitesse réglable, une minuterie de veille et la reprise là où vous vous êtes arrêté.
- **Widgets et plus** — widgets pour l'écran d'accueil et l'écran de verrouillage, scrobbling Last.fm, paroles synchronisées et LRC, et une accessibilité VoiceOver complète.

Flacbox se télécharge gratuitement. Premium supprime les limites de la version gratuite sur les comptes cloud, les playlists et les dossiers hors ligne, et il est disponible sous forme d'achat unique à vie ou d'abonnement mensuel ou annuel, avec le Partage familial.

{{< app-details product="flacbox" >}}

## Option 2 : convertir le FLAC en ALAC pour l'application Musique

Si vous tenez vraiment à avoir vos rips dans l'application Musique d'Apple, vous pouvez les convertir. Du FLAC vers de l'ALAC, c'est du sans perte vers du sans perte, donc vous ne perdez aucune qualité :

1. Sur votre ordinateur, convertissez par lots avec un outil gratuit comme XLD sur Mac ou foobar2000 sur Windows. Tous deux conservent vos tags.
2. Ajoutez les fichiers ALAC à votre bibliothèque Musique ou iTunes.
3. Synchronisez vers l'iPhone avec le Finder sur Mac ou l'application Appareils Apple sur Windows.

Les compromis sont réels. Vous conservez désormais deux copies de votre bibliothèque, chaque modification de métadonnées implique une nouvelle synchronisation, et la mise en page de l'application Musique reste figée, sans playlists intelligentes, sans égaliseur, sans DSP, et sans diffusion cloud ou NAS sur l'appareil. C'est pourquoi la plupart des personnes possédant de vraies collections FLAC choisissent la première option.

## FAQ

{{% details title="L'iPhone peut-il lire les fichiers FLAC nativement ?" closed="true" %}}
Seulement de manière limitée. L'application Fichiers peut prévisualiser un seul fichier FLAC depuis iOS 11, mais il n'y a pas de bibliothèque, de playlists, de file d'attente, d'égaliseur ou de diffusion cloud. Pour une véritable écoute, utilisez une application de lecture comme Flacbox.
{{% /details %}}

{{% details title="Puis-je lire du FLAC 24 bits ou 96 kHz (ou plus) sur iPhone ?" closed="true" %}}
Oui. Flacbox prend en charge une sortie haute résolution jusqu'à 384 kHz. Pour lire au-dessus de 48 kHz à la véritable résolution, connectez un DAC USB externe, car la sortie intégrée de l'iPhone rééchantillonne l'audio pour chaque application.
{{% /details %}}

{{% details title="Flacbox convertit-il le FLAC vers un autre format ?" closed="true" %}}
Non. Flacbox lit le FLAC dans sa qualité sans perte d'origine, sans conversion. Les effets et le DSP sont appliqués en direct pendant la lecture uniquement, et ils ne modifient jamais vos fichiers.
{{% /details %}}

{{% details title="Est-ce que je perds en qualité en convertissant le FLAC en ALAC ?" closed="true" %}}
Non. FLAC et ALAC sont tous deux sans perte, donc la conversion est bit-perfect. Vous ne perdez que du temps et de la commodité, puisque vous vous retrouvez avec deux bibliothèques à entretenir et que vous devez resynchroniser après chaque modification.
{{% /details %}}

{{% details title="Quels formats audio Flacbox prend-il en charge ?" closed="true" %}}
Plus de 120 formats, dont FLAC, DSD (DSF et DFF), ALAC, APE, WAV, AIFF, WV, OGG, OPUS, MP3, AAC, M4A, WMA, et même de la musique tracker et MOD comme MOD, XM, IT et S3M.
{{% /details %}}

{{% details title="Flacbox a-t-il un égaliseur, des effets et un visualiseur ?" closed="true" %}}
Oui. Il dispose d'un égaliseur 10 bandes avec des presets et un préampli. Il possède aussi un moteur professionnel BASS avec onze effets en temps réel (réverbération, delay, écho multi-tap, crossfeed, compresseur, chorus, flanger, phaser, auto-wah, distorsion et rotation stéréo), plus le nivellement du volume EBU R128, un processeur DSP à 14 filtres et un visualiseur Milkdrop en plein écran avec 500 presets.
{{% /details %}}

{{% details title="Puis-je diffuser du FLAC depuis mon NAS ou le cloud ?" closed="true" %}}
Oui. Flacbox se connecte à plus de 30 services cloud ainsi qu'à un NAS ou un ordinateur via SMB, WebDAV, DLNA, FTP, SFTP et NFS. Toute votre bibliothèque est disponible sans copier de fichiers sur votre iPhone, et vous pouvez télécharger des morceaux pour une lecture hors ligne à tout moment.
{{% /details %}}

{{% details title="Flacbox est-il vraiment gratuit ?" closed="true" %}}
Flacbox se télécharge gratuitement, avec des fonctionnalités essentielles comme l'égaliseur, la diffusion cloud et la lecture hors ligne. Premium supprime les limites de la version gratuite sur les comptes cloud, les playlists et les dossiers hors ligne, et il est proposé sous forme d'achat unique à vie ou d'abonnement mensuel ou annuel, avec le Partage familial.
{{% /details %}}
