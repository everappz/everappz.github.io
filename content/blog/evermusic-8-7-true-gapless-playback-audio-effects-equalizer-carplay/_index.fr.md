---
title: "Evermusic 8.7 : vraie lecture sans blanc, effets audio, normalisation du volume, égaliseur redessiné"
date: 2026-07-05
description: "Evermusic 8.7 pour iPhone, iPad et Mac ajoute une vraie lecture sans blanc, cinq effets audio de studio (réverbération, delay, distorsion, compresseur, crossfeed), la normalisation du volume EBU R128, un égaliseur à 10 bandes redessiné avec import/export de préréglages, un moteur de streaming AVAudioEngine reconstruit avec prise en charge de FLAC et Ogg Vorbis, ainsi qu'un CarPlay et un Lecture en cours plus rapides et plus précis."
keywords: ["Evermusic 8.7", "mise à jour Evermusic", "vraie lecture sans blanc iPhone", "lecteur de musique gapless iOS", "lecture gapless CarPlay", "effets audio lecteur de musique iPhone", "réverbération delay distorsion compresseur crossfeed iOS", "crossfeed casque iOS", "normalisation du volume iPhone", "normalisation du volume lecteur de musique", "normalisation EBU R128 iOS", "alternative à ReplayGain iPhone", "égaliseur 10 bandes iPhone", "égaliseur graphique application iOS", "import export préréglages égaliseur", "lecteur FLAC iPhone", "lecteur Ogg Vorbis iOS", "lecteur de musique sans perte iPhone 2026", "lecteur de musique AVAudioEngine", "lecteur de musique CarPlay iPhone", "précision Lecture en cours écran verrouillé", "lecteur de musique cloud iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Lecture sans blanc", "Effets audio", "Réverbération", "Delay", "Distorsion", "Compresseur", "Crossfeed", "Normalisation du volume", "EBU R128", "Égaliseur", "FLAC", "Ogg Vorbis", "CarPlay", "Lecture en cours", "Liquid Glass", "Nouveautés"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**En bref :** [Evermusic 8.7](/products/evermusic) est une mise à jour axée sur la qualité sonore pour iPhone, iPad et Mac. Elle apporte une **vraie lecture sans blanc** (aucune pause, aucun clic ni craquement entre les morceaux), un ensemble complet d'**effets audio de studio** — réverbération, delay, distorsion, compresseur et crossfeed — et la **normalisation du volume EBU R128** qui maintient un niveau sonore constant d'un morceau à l'autre sans tags ReplayGain. L'**égaliseur à 10 bandes** est redessiné avec de nouveaux curseurs, un changement de préréglage plus rapide, des préréglages personnalisés que vous pouvez importer et exporter, et une meilleure disposition en mode paysage et sur iPad. En coulisses, un **moteur de streaming AVAudioEngine reconstruit** améliore la fiabilité et la prise en charge des formats, notamment **FLAC** et **Ogg Vorbis**. **CarPlay** et **Lecture en cours** sont plus rapides et plus précis sur l'écran verrouillé, en voiture et depuis les télécommandes des écouteurs.

---

## Bonjour à toutes et à tous !

Evermusic 8.7 est disponible au téléchargement. Cette mise à jour est entièrement consacrée à la façon dont votre musique *sonne*. Nous avons reconstruit le moteur de lecture pour une vraie lecture sans blanc, ajouté une suite d'effets audio de qualité studio, introduit la normalisation du volume et redessiné l'égaliseur des curseurs jusqu'au moindre détail. Le tout est enveloppé dans le nouveau design **Liquid Glass** d'Apple.

[Téléchargez Evermusic 8.7 sur l'App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) ou mettez à jour depuis votre version existante. Evermusic est en téléchargement gratuit avec des améliorations facultatives via des achats intégrés.

## Vraie lecture sans blanc

La lecture sans blanc signifie que le silence entre deux morceaux disparaît. Aucune pause, aucun clic, aucun craquement — le morceau en cours s'enchaîne directement avec le suivant. Cela compte surtout pour la musique conçue pour être écoutée d'un seul tenant : **enregistrements live, mix DJ, œuvres classiques et albums concepts** où un morceau se fond directement dans un autre.

Voici ce qui a changé techniquement. Le moteur audio d'Evermusic garde deux morceaux en jeu à la fois : celui que vous entendez et le suivant dans la file d'attente. Pendant que le morceau en cours joue, le suivant est déjà en train d'être **récupéré, décodé et mis en mémoire tampon à l'avance** en arrière-plan. Lorsque le morceau en cours atteint sa fin, le moteur effectue le relais vers le suivant **à l'intérieur du lecteur, et non à l'intérieur du flux audio**. La boucle de rendu de la sortie continue de puiser les échantillons audio dans un tampon circulaire continu sans jamais s'arrêter, si bien que l'auditeur n'entend jamais de frontière. Le basculement se produit entre les échantillons, ce qui explique précisément l'absence de tout blanc audible.

Cela fonctionne de la même façon que le fichier soit sur votre appareil, dans le cloud ou sur un serveur multimédia — la mise en mémoire tampon anticipée commence simplement un peu plus tôt pour les sources distantes.

## Effets audio de studio

Evermusic 8.7 ajoute cinq effets audio en temps réel que vous pouvez superposer à votre musique. Chacun s'exécute comme un nœud de traitement audio natif dans le moteur de lecture, il s'applique donc à tout ce que vous lisez — fichiers locaux, flux cloud et radio Internet — sans réencodage.

Chaque effet est livré avec une **bibliothèque de préréglages soignée** pour obtenir un excellent son en une touche, et Evermusic **mémorise vos réglages exacts** d'une session à l'autre. Ajustez une commande et l'effet passe à l'état **Manuel**, vous savez donc toujours quand vous vous êtes éloigné d'un préréglage.

### Réverbération

Ajoute une sensation d'espace, d'une pièce exiguë à une cathédrale. Construite sur le `AVAudioUnitReverb` d'Apple, elle propose **13 préréglages de pièce** (Petite pièce, Salle moyenne, Plate, Cathédrale, et plus) plus une commande de **mix wet/dry** de 0 à 100 % pour que vous décidiez de la quantité d'espace à ajouter.

### Delay (écho)

Un écho classique avec **10 préréglages** — Slapback, Écho à bande, Dub, Ambiant, et d'autres. Vous pouvez régler le **temps de delay** (jusqu'à 2 secondes), le **feedback** (le nombre de répétitions), une **fréquence de coupure passe-bas** pour réchauffer les répétitions, et le **mix wet/dry**.

### Distorsion

D'un grain subtil à une destruction lo-fi totale, pilotée par `AVAudioUnitDistortion` avec **22 préréglages de caractère** (Bit Brush, Cellphone Concert, Radio Tower, et plus), une commande de drive de **pré-gain** et un mix wet/dry pour réintégrer l'effet dans le signal propre.

### Compresseur

Un processeur de dynamique (le `AUDynamicsProcessor` d'Apple) qui équilibre les passages forts et faibles. Il expose l'ensemble complet des commandes professionnelles — **seuil, ratio/marge, attaque, relâchement, expansion et gain de compensation** — avec **10 préréglages** ajustés pour des situations réelles : Voix / Podcast, Tard le soir, Dialogue de film, Correspondance streaming et Volume maximal, parmi d'autres.

### Crossfeed

Le Crossfeed rend l'écoute au casque plus naturelle en mélangeant un peu du canal gauche dans le droit et inversement, comme vos oreilles entendent de vrais haut-parleurs. Il est construit sur le célèbre algorithme **Bauer stereophonic-to-binaural (bs2b)**, avec un contrôle du **niveau de crossfeed** et de la **fréquence de coupure**, et **6 préréglages** dont les réglages *Chu Moy* et *Jan Meier*, favoris des audiophiles. Il est particulièrement efficace sur les vieux mixages stéréo fortement panoramiqués des années 1960 et 1970.

## Normalisation du volume

Vous avez déjà créé une liste de lecture où un morceau explose et le suivant est un murmure ? La normalisation du volume corrige cela. Evermusic 8.7 utilise la **mesure de niveau sonore EBU R128** (le même standard ITU-R BS.1770 utilisé en broadcast et par les services de streaming) pour mesurer le niveau sonore réel perçu de chaque morceau et l'orienter doucement vers une cible constante.

Contrairement à ReplayGain, elle ne nécessite **aucun** tag dans vos fichiers et ne modifie **pas** votre audio. Elle fonctionne en temps réel sur tout ce que vous lisez, y compris les flux cloud et la radio en direct, et se réinitialise proprement lorsque vous vous déplacez dans un morceau ou changez de piste.

Quatre préréglages couvrent les cas courants :

- **Léger** — nivellement doux (cible −20 LUFS).
- **Standard** — la valeur par défaut, niveau sonore de type streaming (cible −16 LUFS, jusqu'à +12 dB de gain pour les morceaux faibles).
- **Fort** — correspondance agressive pour les bibliothèques très hétérogènes (cible −14 LUFS).
- **Nuit** — plus calme et constant pour une écoute du soir à faible volume (cible −23 LUFS).

Vous n'avez plus besoin de toucher au volume entre les morceaux.

## Égaliseur redessiné

L'**égaliseur graphique à 10 bandes** d'Evermusic a été entièrement redessiné. Les bandes couvrent **32 Hz à 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), chacune réglable de **−12 dB à +12 dB** par pas fins de 0,1 dB, avec un **préampli** de −24 dB à +24 dB pour éviter l'écrêtage lorsque vous amplifiez.

Ce qui est nouveau dans la 8.7 :

- **Nouveaux curseurs** — des commandes précises et réactives qui adoptent l'apparence du curseur système natif d'iOS 26 et le matériau **Liquid Glass**.
- **Changement de préréglage plus rapide et plus fluide** — passez d'un préréglage à l'autre instantanément, avec une barre de préréglages horizontale redessinée en mode portrait et une colonne de préréglages verticale en mode paysage.
- **Meilleure disposition en mode paysage et sur iPad** — les curseurs et le sélecteur de préréglages se réorganisent pour exploiter la largeur supplémentaire au lieu de se tasser dans une colonne à la taille d'un téléphone.
- **Préréglages personnalisés** — créez et enregistrez vos propres courbes, réorganisez-les, et **importez et exportez** des préréglages sous forme de fichiers `.eqp` pour les déplacer entre appareils ou les partager.

L'égaliseur s'exécute nativement dans le moteur (`AVAudioUnitEQ`), il s'applique donc à toutes les sources, et il fonctionne aussi via AirPlay, Chromecast et CarPlay là où c'est pris en charge.

## Moteur de lecture reconstruit

En coulisses, Evermusic 8.7 tourne sur un **moteur de streaming reconstruit** basé sur le `AVAudioEngine` d'Apple avec un pipeline de rendu personnalisé. C'est ce qui rend possibles le relais gapless, la chaîne d'effets et l'égaliseur, et cela rend aussi la lecture quotidienne plus fiable.

- **Prise en charge des formats améliorée** — notamment **FLAC** (via Core Audio) et **Ogg Vorbis** (via `libvorbisfile`), aux côtés de MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF et plus encore.
- **Mise en mémoire tampon plus intelligente** — un tampon anticipé adaptatif qui s'ajuste à votre connexion, avec un tampon circulaire continu alimentant la sortie pour que de brefs à-coups réseau ne se transforment pas en coupures.
- **Récupération automatique** — une machine à états de remise en mémoire tampon et une logique de nouvelle tentative avec temporisation reprennent la lecture proprement après un moment de signal faible, au lieu d'arrêter le morceau.
- **Moins d'interruptions** — le même moteur pilote les fichiers locaux, les flux cloud, les serveurs multimédias et la radio Internet, le comportement est donc cohérent partout.

## Lecture en cours et CarPlay

Les écrans que vous regardez réellement en écoutant — l'**écran verrouillé**, **CarPlay** et les boutons de télécommande de votre voiture ou de vos écouteurs — sont plus précis et plus rapides dans la 8.7.

- **Infos Lecture en cours plus précises.** Evermusic capture l'état du lecteur sous un verrou avant de le publier, de sorte que le titre, le temps écoulé, la durée et l'état lecture/pause ne peuvent jamais se contredire sur l'écran verrouillé ou en voiture. Les états de mise en mémoire tampon et de chargement sont désormais correctement signalés au lieu d'afficher « lecture » alors qu'un morceau est encore en cours de récupération.
- **Télécommandes fiables.** Lecture, pause, suivant, précédent, avance, saut, aléatoire, répétition et vitesse de lecture répondent tous de manière cohérente depuis les boutons des écouteurs, les commandes de la voiture et l'écran verrouillé, pilotés par `MPRemoteCommandCenter`.
- **Pochettes CarPlay plus rapides.** Les pochettes d'album se chargent désormais plusieurs fois plus vite sur les longues listes (cadence de traitement par lots réduite de 1,0 s à 0,25 s, le premier écran visible se chargeant immédiatement), et elles apparaissent maintenant dans les lignes de liste compactes de CarPlay sous iOS 26 qui n'affichaient auparavant aucune pochette.
- **Corrections de tri et de stabilité pour CarPlay.** Tri plus rapide sur les grandes bibliothèques et renforcement contre des plantages dans des cas limites lors du défilement de longues listes.
- **Mises à jour de métadonnées limitées.** Les mises à jour de Lecture en cours et des télécommandes sont désormais limitées pour que des changements rapides n'inondent plus le système, ce qui garde les commandes de l'écran verrouillé et de CarPlay réactives.

## Autres améliorations

- **Design Liquid Glass** affiné dans toute l'application — surfaces translucides, animations plus douces et commandes raffinées sur iOS, iPadOS et macOS.
- **Nouveaux widgets d'écran d'accueil** avec une logique de mise à jour améliorée qui les garde synchronisés sans vider davantage la batterie.
- Corrections pour les versions récentes d'iOS.
- Corrections de localisation dans plusieurs langues.
- De nombreuses améliorations plus petites basées sur vos e-mails et vos avis sur l'App Store.

## Pourquoi cette mise à jour compte

Evermusic 8.7 est construit autour d'une seule idée : **votre musique doit sonner au mieux, sur n'importe quelle source.**

1. **Des albums entiers, comme prévu.** La vraie lecture sans blanc signifie que les sets live, les mix DJ et les albums concepts se lisent enfin comme l'artiste les a masterisés.
2. **Un studio dans votre poche.** Réverbération, delay, distorsion, compresseur, crossfeed, un égaliseur redessiné et la normalisation du volume vous donnent un vrai contrôle sur votre son, et pas seulement un interrupteur marche/arrêt.
3. **La même expérience partout.** Fichiers locaux, espaces cloud, serveurs multimédias et radio Internet passent tous par le même moteur reconstruit, avec un Lecture en cours précis et un CarPlay plus rapide par-dessus.

## Obtenir Evermusic 8.7

[**Téléchargez Evermusic sur l'App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) ou mettez à jour depuis l'App Store. Evermusic est en téléchargement gratuit avec des améliorations facultatives via des achats intégrés pour les fonctions avancées.

Si vous appréciez l'application, laissez une note sur l'App Store — cela aide vraiment. Vous avez un retour ou vous rencontrez un problème ? Écrivez-nous à **support@everappz.com**. Nous lisons chaque message.

## Foire aux questions

{{% details title="Quoi de neuf dans Evermusic 8.7 ?" closed="true" %}}
Evermusic 8.7 ajoute une vraie lecture sans blanc, cinq effets audio de studio (réverbération, delay, distorsion, compresseur et crossfeed), la normalisation du volume EBU R128, un égaliseur à 10 bandes redessiné avec préréglages personnalisés et import/export, un moteur de streaming AVAudioEngine reconstruit avec une prise en charge des formats améliorée (dont FLAC et Ogg Vorbis), un CarPlay et un Lecture en cours plus rapides et plus précis, des mises à jour de design Liquid Glass, des widgets d'écran d'accueil rafraîchis, ainsi que des corrections de bugs et de localisation.
{{% /details %}}

{{% details title="Evermusic propose-t-il une vraie lecture sans blanc ?" closed="true" %}}
Oui. À partir d'Evermusic 8.7, la lecture est vraiment sans blanc : il n'y a aucune pause, aucun clic ni craquement entre les morceaux. Le moteur met en mémoire tampon et décode à l'avance le morceau suivant pendant que le morceau en cours joue et effectue le relais entre les échantillons audio sur un tampon circulaire continu, de sorte que la transition est inaudible. Cela fonctionne pour les fichiers locaux, les flux cloud et les serveurs multimédias, et c'est idéal pour les albums live, les mix DJ et les albums concepts.
{{% /details %}}

{{% details title="Quels effets audio Evermusic 8.7 inclut-il ?" closed="true" %}}
Cinq effets en temps réel : **Réverbération** (13 préréglages de pièce, mix wet/dry), **Delay/Écho** (10 préréglages avec temps de delay, feedback, passe-bas et mix), **Distorsion** (22 préréglages de caractère avec pré-gain et mix), **Compresseur** (un processeur de dynamique complet avec seuil, ratio, attaque, relâchement, expansion et gain de compensation, plus 10 préréglages) et **Crossfeed** (crossfeed pour casque Bauer bs2b avec commandes de niveau et de coupure et 6 préréglages). Chaque effet est livré avec des préréglages soignés, et vos réglages personnalisés sont mémorisés d'une session à l'autre.
{{% /details %}}

{{% details title="Qu'est-ce que le Crossfeed et pourquoi l'utiliser ?" closed="true" %}}
Le Crossfeed mélange une petite quantité filtrée de chaque canal stéréo dans l'autre, comme vos oreilles entendent naturellement de vrais haut-parleurs dans une pièce. Au casque, cela réduit la séparation exagérée, « dans la tête », des enregistrements fortement panoramiqués et rend les longues écoutes plus confortables. Evermusic utilise le célèbre algorithme Bauer stereophonic-to-binaural (bs2b) et inclut des préréglages comme Chu Moy et Jan Meier. Il est particulièrement efficace sur les vieux mixages stéréo des années 1960 et 1970.
{{% /details %}}

{{% details title="Comment fonctionne la normalisation du volume dans Evermusic ?" closed="true" %}}
Evermusic 8.7 mesure le niveau sonore perçu de chaque morceau à l'aide du standard EBU R128 (ITU-R BS.1770) en temps réel et ajuste doucement le niveau vers une cible constante pour que les morceaux ne sautent pas en volume. Il ne nécessite pas de tags ReplayGain et n'altère pas vos fichiers. Quatre préréglages sont disponibles — Léger (−20 LUFS), Standard (−16 LUFS), Fort (−14 LUFS) et Nuit (−23 LUFS) — et la normalisation se réinitialise proprement lorsque vous vous déplacez dans un morceau ou changez de piste.
{{% /details %}}

{{% details title="La normalisation du volume d'Evermusic est-elle la même chose que ReplayGain ?" closed="true" %}}
Elle atteint le même objectif — un niveau sonore constant entre les morceaux — mais fonctionne différemment. ReplayGain s'appuie sur des tags de niveau sonore stockés dans vos fichiers. Le normaliseur d'Evermusic mesure le niveau sonore en direct avec EBU R128, il fonctionne donc sur n'importe quelle source, y compris les flux cloud et la radio Internet, même lorsque les fichiers n'ont aucun tag.
{{% /details %}}

{{% details title="Combien de bandes l'égaliseur d'Evermusic a-t-il, et puis-je créer mes propres préréglages ?" closed="true" %}}
L'égaliseur d'Evermusic est un égaliseur graphique à 10 bandes couvrant 32 Hz à 16 kHz, chaque bande étant réglable de −12 dB à +12 dB par pas de 0,1 dB et avec un préampli de −24 dB à +24 dB. Il comprend des préréglages intégrés, vous permet de créer et d'enregistrer des préréglages personnalisés, et prend en charge l'import et l'export de préréglages sous forme de fichiers .eqp pour les déplacer ou les partager entre appareils.
{{% /details %}}

{{% details title="Qu'est-ce qui a changé dans l'égaliseur d'Evermusic 8.7 ?" closed="true" %}}
L'égaliseur a été redessiné avec de nouveaux curseurs plus précis qui adoptent l'apparence du curseur système d'iOS 26 et le look Liquid Glass, un changement de préréglage plus rapide et plus fluide, et une meilleure disposition en mode paysage et sur iPad (une barre de préréglages horizontale en portrait et une colonne de préréglages verticale en paysage). Les préréglages personnalisés et l'import/export .eqp sont pris en charge.
{{% /details %}}

{{% details title="Evermusic 8.7 prend-il en charge FLAC et Ogg Vorbis ?" closed="true" %}}
Oui. Le moteur reconstruit lit FLAC (via Core Audio) et Ogg Vorbis (via libvorbisfile), ainsi que MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF et plus encore, depuis les fichiers locaux, les espaces cloud et les serveurs multimédias.
{{% /details %}}

{{% details title="Qu'est-ce qui a été amélioré dans CarPlay et sur l'écran verrouillé ?" closed="true" %}}
Les pochettes d'album CarPlay se chargent plusieurs fois plus vite sur les longues listes et apparaissent désormais dans les lignes de liste compactes d'iOS 26 qui n'en affichaient aucune. Les infos Lecture en cours sur l'écran verrouillé et dans CarPlay sont plus précises — le titre, le temps écoulé, la durée et l'état lecture/pause sont capturés ensemble pour qu'ils ne puissent pas se contredire, et les états de mise en mémoire tampon sont correctement signalés. Les télécommandes (lecture, pause, suivant, précédent, avance, aléatoire, répétition, vitesse) répondent de manière fiable depuis les écouteurs et la voiture, et le tri CarPlay sur les grandes bibliothèques est plus rapide.
{{% /details %}}

{{% details title="Les effets audio et l'égaliseur fonctionnent-ils avec le streaming cloud et CarPlay ?" closed="true" %}}
Oui. Les effets, l'égaliseur et la normalisation du volume s'exécutent nativement dans le moteur de lecture, ils s'appliquent donc à tout ce qu'Evermusic lit — fichiers locaux, espaces cloud, serveurs multimédias et radio Internet — et continuent de fonctionner pendant la lecture avec CarPlay et, là où c'est pris en charge, via AirPlay et Chromecast.
{{% /details %}}

{{% details title="Evermusic 8.7 est-il gratuit à mettre à jour, et quels appareils prend-il en charge ?" closed="true" %}}
Oui. Evermusic est en téléchargement gratuit sur l'App Store, et la 8.7 est une mise à jour gratuite pour les utilisateurs existants, avec des améliorations facultatives via des achats intégrés pour les fonctions avancées. Elle fonctionne sur iPhone, iPad et Mac. CarPlay nécessite un véhicule ou un autoradio compatible CarPlay.
{{% /details %}}
