---
title: "Evervideo 1.7 : Plex, Jellyfin, streaming cloud et gestes de lecture"
date: 2026-05-18
description: "Evervideo 1.7 ajoute plus de 10 nouvelles connexions — Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS — plus de nouveaux gestes de lecture (double tap pour avancer, appui long pour 2x), un Wi-Fi Drive rafraîchi avec envoi par lots et des mises à jour Liquid Glass pour iPhone, iPad et Mac."
keywords: ["Evervideo 1.7", "mise à jour Evervideo", "lecteur vidéo HD iPhone", "lecteur vidéo Plex iOS", "vidéo Jellyfin iPhone", "lecteur vidéo Emby iOS", "vidéo Subsonic iOS", "vidéo Navidrome iOS", "streaming vidéo Internxt", "lecteur vidéo Proton Drive", "lecteur vidéo QNAP iPhone", "lecteur vidéo Nextcloud iOS", "streaming vidéo Amazon S3", "lecteur vidéo SFTP iPhone", "lecteur vidéo FTP iOS", "streaming vidéo NFS iPhone", "streaming vidéo depuis NAS iPhone", "lecteur MKV iPhone", "gestes lecteur vidéo iOS", "double tap pour avancer la vidéo", "transfert vidéo Wi-Fi Drive iPhone", "design Liquid Glass", "lecteur vidéo cloud iOS 2026", "streaming de films depuis le cloud iPhone"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Gestes de lecture", "Liquid Glass", "Nouveautés"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**TL;DR :** [Evervideo 1.7](/products/evervideo) est une mise à jour majeure du lecteur vidéo HD pour iPhone, iPad et Mac. Cette version ajoute plus de 10 nouvelles connexions cloud, NAS et serveurs multimédias — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, ainsi que les serveurs multimédias les plus populaires **Plex**, **Subsonic**, **Navidrome**, **Jellyfin** et **Emby**, et trois protocoles réseau : **FTP**, **SFTP** et **NFS**. De nouveaux **gestes de lecture** vous permettent de double-taper pour avancer ou reculer, d'appuyer longuement pour passer à 2x, et de taper une fois pour afficher ou masquer les commandes — sans jamais quitter le plein écran. Wi-Fi Drive a une interface rafraîchie avec un mode de sélection et une file d'envoi plus intelligente. Toute l'app est ajustée au nouveau design **Liquid Glass** d'Apple.

---

## Bonjour à toutes et à tous !

Une grosse mise à jour Evervideo est là. C'est l'une des plus grandes versions que nous ayons livrées : **plus de 10 nouvelles connexions cloud, serveur et réseau**, de tout nouveaux **gestes de lecture** pour un contrôle plus rapide en plein écran, une expérience **Wi-Fi Drive** rafraîchie et une interface ajustée pour **Liquid Glass** sur iPhone, iPad et Mac.

[Téléchargez Evervideo 1.7 sur l'App Store](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) ou mettez à jour depuis votre version actuelle. Les utilisateurs Mac peuvent obtenir la [version de bureau ici](https://apps.apple.com/app/evervideo/id6743504109).

## Plus de 10 nouvelles connexions cloud, NAS et serveurs multimédias

Evervideo 1.7 élargit ce qui compte comme votre « bibliothèque vidéo ». Si vos films, séries ou enregistrements vivent sur un cloud auquel vous faites confiance, un NAS à la maison ou un serveur multimédia auto-hébergé, Evervideo peut désormais y diffuser directement — sans téléchargements, sans conversions, sans réencodage.

### Stockage cloud orienté confidentialité : Internxt et Proton Drive

Si le chiffrement de bout en bout et le stockage à zéro connaissance comptent pour vous, deux des clouds privés les plus respectés sont désormais natifs dans Evervideo :

- **Internxt** — cloud espagnol open source, chiffré post-quantique et conforme au RGPD. Niveau gratuit disponible.
- **Proton Drive** — stockage chiffré de bout en bout des créateurs de Proton Mail et Proton VPN, basé en Suisse. Niveau gratuit disponible avec des forfaits payants pour les bibliothèques plus grandes.

Connectez-vous une fois et vos vidéos sont diffusées dans le tunnel chiffré — Evervideo ne voit jamais vos données en clair, et le serveur du fournisseur non plus.

### Stockage auto-hébergé : QNAP, Nextcloud, Amazon S3

Pour les utilisateurs qui gèrent leur propre infrastructure :

- **QNAP** — connexion API native aux NAS QNAP pour une lecture vidéo rapide et fiable via Wi-Fi local ou accès distant. Diffusez directement des fichiers MKV 4K sans réencodage.
- **Nextcloud** — connectez-vous à n'importe quelle instance Nextcloud auto-hébergée ou managée. Idéal si vous avez déjà migré depuis Google Drive ou Dropbox pour des raisons de confidentialité.
- **Amazon S3** — pointez Evervideo vers n'importe quel bucket S3 (ou stockage compatible S3 comme Backblaze B2, Wasabi, MinIO, Cloudflare R2) et diffusez votre collection directement.

### <a id="media-servers"></a>Serveurs multimédias : Plex, Subsonic, Navidrome, Jellyfin, Emby

C'est la grande nouveauté pour les fans de vidéo auto-hébergée. Evervideo 1.7 transforme votre iPhone, iPad ou Mac en client de premier ordre pour les serveurs multimédias open source et freemium les plus populaires :

- **Plex** — Plex Media Server est **gratuit** à télécharger et exécuter, avec un abonnement **Plex Pass** optionnel pour des fonctions comme la synchronisation mobile, le transcodage matériel et la TV en direct. Evervideo fonctionne avec les bibliothèques gratuites et Plex Pass — diffusez toute votre collection de films et séries TV.
- **Subsonic** — le serveur de streaming auto-hébergé original. Le serveur Subsonic officiel est **payant** (1 $/mois après un essai de 30 jours), et Evervideo prend aussi en charge l'API Subsonic avec les serveurs vidéo compatibles.
- **Navidrome** — serveur moderne, léger, **entièrement gratuit et open source**. Implémente l'API Subsonic. Fonctionne sur un Raspberry Pi, un NAS ou n'importe quelle machine Linux.
- **Jellyfin** — serveur multimédia **entièrement gratuit et open source** (un fork communautaire d'Emby). Gère films, séries TV, musique, livres et vidéos personnelles. Pas de comptes, pas de télémétrie, pas d'abonnements. Le choix de référence pour les utilisateurs qui veulent du streaming auto-hébergé sans contraintes commerciales.
- **Emby** — serveur multimédia **freemium**. Le serveur principal est gratuit ; **Emby Premiere** est un achat unique ou annuel qui débloque les apps mobiles, la synchronisation hors ligne, le mode Cinéma et plus encore. Evervideo se connecte aux bibliothèques gratuites et Premiere.

Quel que soit le serveur que vous utilisez, Evervideo diffuse toute votre bibliothèque — films, séries, vidéos personnelles et pistes de sous-titres intégrées — avec l'égaliseur vidéo, la prise en charge 360°, Picture-in-Picture, AirPlay et Chromecast.

### Nouveaux protocoles réseau : FTP, SFTP, NFS

Pour les utilisateurs avec des serveurs sur mesure, des homelabs ou des NAS génériques qui ne sont pas livrés avec une app mobile soignée, Evervideo 1.7 ajoute trois protocoles classiques :

- **SFTP (SSH File Transfer Protocol)** — la bonne réponse pour **diffuser des vidéos en toute sécurité depuis votre propre serveur**. SFTP fonctionne sur SSH, ce qui signifie que tout le transfert (authentification et données vidéo) est chiffré. Si vous avez un VPS, un serveur dédié ou une machine Linux à la maison avec accès SSH, vous pouvez y déposer un dossier de vidéos et diffuser sur l'Internet public sans rien exposer d'autre. Authentification par mot de passe et par clé.
- **FTP** — la norme historique de transfert de fichiers. Utile si votre **NAS domestique** (Synology, ASUS, D-Link, TerraMaster anciens ou boîtiers génériques) expose un serveur FTP mais n'a pas d'intégration API native. À utiliser de préférence sur votre réseau local.
- **NFS (Network File System)** — le protocole de partage de facto sous Linux et la plupart des NAS. Les partages NFS sont courants sur les homelabs et les petits réseaux d'entreprise ; Evervideo les monte désormais et diffuse de la vidéo 4K et HD avec peu de surcoût.

> **Astuce :** SFTP est le protocole à privilégier pour diffuser sur l'Internet ouvert. FTP et NFS s'utilisent mieux sur le réseau local — ne les exposez pas à Internet sans VPN.

## Nouveaux gestes de lecture

Regarder des vidéos en plein écran doit être sans effort. Evervideo 1.7 introduit un ensemble propre de gestes tactiles qui vous permettent de contrôler la lecture sans afficher les commandes à l'écran — parfait pour les films, les conférences ou tout ce que vous voulez regarder sans interruption.

### Double tap — Avance ou recul

Double-tapez la **partie droite** de l'écran pour **avancer** d'un nombre de secondes configurable. Double-tapez la **partie gauche** pour **reculer**. Vous pouvez modifier l'intervalle (par défaut : 10 secondes) dans **Paramètres → Lecture → Intervalle de saut par geste** — choisissez n'importe quoi entre 5 secondes (pour un calage fin) et 60 secondes (pour passer les génériques).

C'est le geste que les utilisateurs de YouTube et Netflix reconnaîtront immédiatement, et il est désormais natif dans Evervideo pour toute vidéo, sur toute source.

### Appui long — Vitesse 2x temporaire

Appuyez longuement n'importe où sur l'écran pour **accélérer temporairement la lecture à 2x**. Relâchez pour revenir à la vitesse normale. Parfait pour :

- Passer des scènes lentes sans s'engager dans un changement de vitesse permanent.
- Parcourir rapidement des cours, tutoriels ou podcasts pour trouver la section pertinente.
- Échantillonner des films avant de vous engager à voir la version complète.

Le geste d'appui long ne modifie pas votre vitesse de lecture enregistrée — relâchez et vous êtes revenu au point de départ.

### Tap simple — Afficher / masquer les commandes

Un seul tap sur l'écran bascule les commandes de lecture (lecture, pause, barre de progression, sous-titres, égaliseur). Tapez une fois pour les afficher, tapez à nouveau pour les masquer. Combiné au double tap et à l'appui long, cela signifie que vous pouvez passer presque tout un film en mode plein écran épuré tout en pouvant chercher, mettre en pause et accélérer le scan dès que nécessaire.

## Wi-Fi Drive : nouvelle interface et envois plus rapides

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) est la fonctionnalité intégrée d'Evervideo pour **transférer des vidéos sans fil de votre ordinateur vers votre iPhone ou iPad — sans iTunes, sans câbles, sans compte cloud**. Les deux appareils doivent être sur le même réseau Wi-Fi. Vous démarrez le serveur depuis l'app iOS, puis vous :

- Ouvrez l'URL dans n'importe quel navigateur de bureau (Safari, Chrome, Firefox, Edge), glissez vos fichiers vidéo dans la page, et ils sont envoyés directement sur l'appareil, ou
- Montez l'appareil comme partage réseau via **le Finder du Mac** (« Se connecter au serveur… ») ou **l'Explorateur de fichiers Windows** (Connecter un lecteur réseau) en utilisant WebDAV.

C'est le moyen le plus rapide de transférer une grande collection vidéo locale sur votre téléphone ou tablette sans aucun service tiers. Voir le [guide pas à pas ici](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).

Dans Evervideo 1.7, Wi-Fi Drive bénéficie de :

- **Interface utilisateur redessinée** — plus propre, plus lisible d'un coup d'œil et mise à jour pour Liquid Glass.
- **Nouveau mode de sélection pour les actions par lots** — choisissez plusieurs fichiers ou dossiers et agissez en masse (supprimer, déplacer, copier).
- **File d'envoi améliorée** — meilleure information de progression et meilleure résilience aux coupures réseau pour qu'une connexion Wi-Fi capricieuse ne ruine plus un transfert de 30 Go.
- **Meilleure performance globale des transferts** — envois sensiblement plus rapides pour les grosses bibliothèques, notamment pour les fichiers MKV 4K et les collections de films.

## Autres améliorations

### Mises à jour du design Liquid Glass

L'interface d'Evervideo 1.7 est mise à jour pour le nouveau matériau **Liquid Glass** d'Apple à travers toute l'app — surfaces translucides, animations plus fluides et contrôles affinés qui s'intègrent naturellement à iOS 26, iPadOS 26 et macOS 26. La fenêtre Now Playing, le navigateur de fichiers et les écrans de réglages ont tous été retravaillés pour correspondre à la nouvelle esthétique système.

### Bibliothèques de connexion mises à jour

Nous avons rafraîchi les bibliothèques internes utilisées par Evervideo pour parler à **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, **iCloud Drive**, **MEGA** et d'autres services. Résultat : moins de pannes de connexion sur des cas limites, meilleure compatibilité avec les versions de serveur récentes et meilleure fiabilité lors du streaming vidéo sur des connexions lentes ou géographiquement éloignées.

### Corrections de bugs de lecture

- Correction de problèmes de lecture sur certains serveurs auto-hébergés où les flux se bloquaient après un saut sur de gros fichiers MKV.
- Meilleur comportement de reprise quand le réseau coupe brièvement en pleine lecture.
- Synchronisation des sous-titres plus fluide sur les contenus longs.

### Corrections de localisation

Corrections de traduction dans plusieurs langues sur la base des retours directs des utilisateurs. Meilleur ajustement du texte sur les petits boutons et les langues européennes plus longues (allemand, néerlandais, français).

### Petites améliorations inspirées par vos retours

Beaucoup de petites améliorations basées sur les avis App Store et les e-mails à support@everappz.com. Nous lisons chaque message.

## Pourquoi cette mise à jour compte

Evervideo 1.7 est construite autour de trois idées :

1. **Vos vidéos, où que vous les gardiez.** Que votre bibliothèque vive sur iCloud Drive, sur un cloud orienté confidentialité comme Proton Drive ou Internxt, sur un serveur multimédia comme Plex ou Jellyfin, sur un NAS à la maison ou sur un Raspberry Pi exécutant Navidrome — Evervideo s'y connecte désormais nativement, avec la même expérience de lecture partout.
2. **Une vidéo plein écran qui paraît sans effort.** Les nouveaux gestes tactiles (double tap, appui long, tap simple) apportent le type de contrôle fluide que les apps de streaming comme YouTube et Netflix ont habitué les utilisateurs à attendre, appliqué à *votre* collection vidéo.
3. **Des transferts plus rapides depuis votre ordinateur.** Un Wi-Fi Drive rafraîchi avec sélection par lots et file d'envoi plus intelligente rend le déplacement de grosses collections de films 4K vers votre iPhone ou iPad véritablement rapide — sans câbles, sans iTunes, sans compression.

## Obtenez Evervideo 1.7

[**Téléchargez Evervideo sur l'App Store**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) ou mettez à jour depuis l'App Store. La [version Mac](https://apps.apple.com/app/evervideo/id6743504109) est disponible séparément comme app Mac universelle. Evervideo est un téléchargement gratuit avec des achats intégrés optionnels pour les fonctions avancées. Les nouvelles connexions cloud, le support des serveurs multimédias, les gestes de lecture, les améliorations Wi-Fi Drive et l'UI Liquid Glass font partie de la mise à jour de base.

Si vous aimez l'app, laissez-lui une note sur l'App Store — ça aide vraiment. Une remarque ou un souci ? Écrivez-nous à **support@everappz.com**. Nous lisons chaque message.

## Foire aux questions

{{% details title="Quoi de neuf dans Evervideo 1.7 ?" closed="true" %}}
Evervideo 1.7 introduit la prise en charge de plus de 10 nouvelles connexions (Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), de nouveaux gestes de lecture (double tap pour avancer, appui long pour 2x, tap simple pour afficher/masquer les commandes), un Wi-Fi Drive redessiné avec mode de sélection et file d'envoi plus intelligente, des mises à jour du design Liquid Glass, des bibliothèques de connexion à jour et de nombreuses corrections de bugs.
{{% /details %}}

{{% details title="Evervideo fonctionne-t-il avec Plex ?" closed="true" %}}
Oui. À partir d'Evervideo 1.7, vous pouvez vous connecter à un Plex Media Server et diffuser toute votre bibliothèque vidéo — films, séries TV et vidéos personnelles. Plex Media Server est gratuit à exécuter ; Plex Pass est optionnel. Evervideo prend en charge à la fois les configurations gratuites et Plex Pass, y compris la lecture directe des formats MKV, MP4, AVI, MOV et autres sans réencodage.
{{% /details %}}

{{% details title="Jellyfin ou Navidrome sont-ils pris en charge dans Evervideo ?" closed="true" %}}
Oui. Jellyfin et Navidrome sont tous deux entièrement pris en charge dans Evervideo 1.7. Jellyfin est un serveur multimédia gratuit et open source qui gère la vidéo et l'audio. Navidrome est un serveur gratuit et open source qui implémente l'API Subsonic. Evervideo se connecte nativement aux deux.
{{% /details %}}

{{% details title="Plex, Jellyfin, Emby, Navidrome et Subsonic sont-ils gratuits ?" closed="true" %}}
- **Plex** — le serveur est gratuit ; Plex Pass est une mise à niveau payante optionnelle.
- **Jellyfin** — entièrement gratuit et open source.
- **Emby** — le serveur est gratuit ; Emby Premiere est payant et débloque la synchronisation mobile et le mode hors ligne.
- **Navidrome** — entièrement gratuit et open source.
- **Subsonic** — le serveur officiel coûte 1 $/mois après un essai de 30 jours, mais son API est ouverte et de nombreux serveurs gratuits (dont Navidrome) l'implémentent.
{{% /details %}}

{{% details title="Puis-je diffuser depuis mon NAS domestique en SFTP, FTP ou NFS ?" closed="true" %}}
Oui. Evervideo 1.7 ajoute SFTP, FTP et NFS comme types de connexion natifs. SFTP est le choix recommandé pour diffuser depuis votre propre serveur sur l'Internet public car tout le trafic est chiffré via SSH. FTP et NFS s'utilisent mieux sur le réseau local ou derrière un VPN.
{{% /details %}}

{{% details title="Comment connecter Evervideo à un serveur personnalisé en SFTP ?" closed="true" %}}
Ouvrez Evervideo, allez dans l'onglet Connexions, choisissez SFTP, et saisissez le nom d'hôte ou l'IP de votre serveur, le port (généralement 22), le nom d'utilisateur et soit un mot de passe, soit une clé SSH privée. Evervideo parcourra vos dossiers distants et diffusera les fichiers vidéo directement avec un chiffrement de bout en bout.
{{% /details %}}

{{% details title="Evervideo prend-il en charge Internxt et Proton Drive ?" closed="true" %}}
Oui. Les deux clouds orientés confidentialité sont pris en charge à partir d'Evervideo 1.7. Ils rejoignent MEGA et d'autres services orientés confidentialité déjà disponibles dans l'app.
{{% /details %}}

{{% details title="Comment fonctionnent les nouveaux gestes de lecture ?" closed="true" %}}
En lecture vidéo plein écran, **double-tapez sur le côté droit** pour avancer et **double-tapez sur le côté gauche** pour reculer d'un intervalle configurable (par défaut 10 secondes — modifiable dans les Paramètres). **Appuyez longuement** n'importe où sur l'écran pour passer temporairement à 2x ; relâchez pour revenir au normal. **Un tap simple** n'importe où bascule l'affichage des commandes de lecture (montrer ou masquer).
{{% /details %}}

{{% details title="Puis-je modifier l'intervalle de saut du double tap ?" closed="true" %}}
Oui. Allez dans **Paramètres → Lecture → Intervalle de saut par geste** et choisissez une valeur entre 5 et 60 secondes. La plupart des utilisateurs le laissent à 10 ou 15 secondes.
{{% /details %}}

{{% details title="Qu'est-ce que Wi-Fi Drive dans Evervideo ?" closed="true" %}}
Wi-Fi Drive est la fonction intégrée de transfert de fichiers sans fil d'Evervideo. Elle vous permet d'envoyer des vidéos depuis votre ordinateur vers votre iPhone ou iPad sur votre réseau Wi-Fi local — sans iTunes, sans câbles, sans compte cloud. Vous pouvez utiliser n'importe quel navigateur de bureau ou un client WebDAV comme le Finder du Mac ou l'Explorateur de fichiers Windows. Voir le [guide complet Wi-Fi Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).
{{% /details %}}

{{% details title="Evervideo lit-il les fichiers MKV, AVI et autres formats depuis Plex ou Jellyfin ?" closed="true" %}}
Oui. Evervideo lit pratiquement tous les formats vidéo — MKV, AVI, MP4, MOV, FLV, WMV, WEBM, M4V, TS, 3GP — et les diffuse directement depuis Plex, Jellyfin, Emby et d'autres serveurs multimédias sans transcodage pour la plupart des codecs. Cela signifie moins de charge CPU sur votre serveur et des temps de démarrage plus rapides.
{{% /details %}}

{{% details title="La mise à jour vers Evervideo 1.7 est-elle gratuite ?" closed="true" %}}
Oui. Evervideo est un téléchargement gratuit sur l'App Store, et la 1.7 est une mise à jour gratuite pour tous les utilisateurs actuels. Les nouvelles intégrations cloud, le support des serveurs multimédias, les gestes de lecture, les améliorations Wi-Fi Drive et l'UI Liquid Glass font partie de la mise à jour de base.
{{% /details %}}

{{% details title="Sur quels appareils Evervideo 1.7 est-il disponible ?" closed="true" %}}
Evervideo 1.7 fonctionne sur iPhone, iPad et Mac. AirPlay et Chromecast vous permettent d'envoyer la lecture vers un écran plus grand. La synchronisation iCloud Drive maintient la cohérence de votre bibliothèque et de vos réglages entre les appareils.
{{% /details %}}
