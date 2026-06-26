---
title: "Evertag 4.2 : nouvelles connexions cloud et options de l'éditeur de tags"
date: 2026-05-09
description: "Evertag 4.2 ajoute des connexions Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP et NFS, rafraîchit Wi-Fi Drive et met à jour l'interface pour Liquid Glass. Cet article explique aussi tous les réglages de l'éditeur de tags — y compris ID3v2.4 vs ID3v2.3, mise à l'échelle de la pochette, tags dupliqués, modes d'envoi cloud et les bons réglages pour Spotify et les autres services de streaming."
keywords: ["Evertag 4.2", "mise à jour Evertag", "éditeur de tags ID3 iPhone", "ID3v2.4 vs ID3v2.3", "modifier tags FLAC iOS", "modifier tags MP3 iPhone", "modifier pochette album iOS", "éditeur de tags pour Spotify", "éditeur de tags Plex", "éditeur de tags Apple Music", "éditeur de tags cloud Evertag", "éditeur de tags Internxt", "éditeur de tags Proton Drive", "éditeur de tags QNAP", "éditeur de tags Nextcloud", "éditeur de tags Amazon S3", "éditeur de tags SFTP iPhone", "éditeur de tags FTP audio", "éditeur de tags NFS iPhone", "Wi-Fi Drive éditeur de tags", "tags ID3 dupliqués", "mise à l'échelle pochette", "design Liquid Glass", "éditeur de métadonnées audio iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Éditeur de tags", "ID3", "ID3v2.4", "ID3v2.3", "Tags FLAC", "Tags MP3", "Pochette d'album", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Nouveautés"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**TL;DR :** [Evertag 4.2](/products/evertag) est une mise à jour majeure de l'éditeur de tags audio pour iPhone, iPad et Mac. Nous avons écrasé les principaux bugs d'édition de tags et ajouté plus de 6 nouvelles connexions cloud et serveur — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, ainsi que les protocoles **FTP**, **SFTP** et **NFS**. Wi-Fi Drive a une interface rafraîchie, un mode multi-sélection, une file d'envoi plus intelligente et des transferts plus rapides. Toute l'app est ajustée au design **Liquid Glass**. Cet article plonge aussi en détail dans les réglages de l'éditeur de tags d'Evertag — en expliquant **ID3v2.4 vs ID3v2.3**, la **mise à l'échelle de la pochette**, les **tags dupliqués**, les **modes d'envoi cloud**, la **suppression du fichier téléchargé** et exactement quels réglages choisir si vous préparez de l'audio pour **Spotify**, **Apple Music**, **Plex**, **Jellyfin** ou tout autre service de streaming.

---

## Bonjour à toutes et à tous !

Une grosse mise à jour Evertag est là. Nous avons écrasé des bugs clés d'édition de tags et ajouté **plus de 6 nouvelles connexions cloud et serveur** pour rendre la gestion de vos métadonnées audio plus simple que jamais — que votre bibliothèque vive sur un cloud orienté confidentialité, sur un NAS auto-hébergé, ou sur un serveur générique FTP/SFTP/NFS.

[Téléchargez Evertag 4.2 sur l'App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) ou mettez à jour depuis votre version actuelle.

## Prise en charge cloud et serveur étendue

Evertag se connecte désormais nativement à un éventail plus large d'options cloud et auto-hébergées. Vous pouvez modifier les tags ID3, MP4, FLAC, OGG et APE sur des fichiers où qu'ils soient.

### Stockage cloud orienté confidentialité : Internxt et Proton Drive

Si le chiffrement de bout en bout et le stockage à zéro connaissance comptent pour vous, deux des noms les plus respectés du cloud privé sont désormais natifs dans Evertag :

- **Internxt** — cloud espagnol open source, chiffré post-quantique et conforme au RGPD. Niveau gratuit disponible.
- **Proton Drive** — stockage chiffré de bout en bout des créateurs de Proton Mail et Proton VPN, basé en Suisse. Niveau gratuit disponible avec des forfaits payants pour les bibliothèques plus grandes.

Vous pouvez désormais modifier les métadonnées directement sur les fichiers audio stockés dans l'un ou l'autre service — le fichier reste chiffré en transit, et seuls les nouveaux tags sont réécrits.

### Solutions auto-hébergées : QNAP, Nextcloud, Amazon S3

Pour les utilisateurs qui gèrent leur propre infrastructure :

- **QNAP** — connexion API native aux NAS QNAP. Modifiez les tags des fichiers stockés sur votre QNAP via Wi-Fi local ou accès distant.
- **Nextcloud** — connectez-vous à n'importe quelle instance Nextcloud auto-hébergée ou managée.
- **Amazon S3** — pointez Evertag vers n'importe quel bucket S3 (ou un stockage compatible S3 comme Backblaze B2, Wasabi, MinIO, Cloudflare R2) et modifiez les métadonnées sur place.

### Nouveaux protocoles réseau : FTP, SFTP, NFS

Evertag 4.2 ajoute trois protocoles classiques pour les utilisateurs avec des serveurs sur mesure, des homelabs ou des NAS génériques :

- **SFTP (SSH File Transfer Protocol)** — la bonne réponse pour **modifier des tags à distance, en toute sécurité, sur votre propre serveur**. SFTP fonctionne sur SSH : tout le transfert (authentification et données audio) est chiffré. Si vous avez un VPS, un serveur dédié ou une machine Linux à la maison avec accès SSH, vous pouvez modifier les tags de fichiers distants sans rien exposer d'autre. Authentification par mot de passe ou clé.
- **FTP** — la norme historique de transfert de fichiers. Utile pour les NAS domestiques anciens qui exposent du FTP mais n'ont pas d'API native.
- **NFS (Network File System)** — le protocole de partage de facto sous Linux et la plupart des NAS. Moins de surcoût que SMB sur le même matériel.

> **Astuce :** SFTP est le protocole à privilégier pour l'édition à distance via Internet ouvert. FTP et NFS s'utilisent mieux sur le réseau local — ne les exposez pas sur Internet sans VPN.

## Améliorations de Wi-Fi Drive

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) est la fonction intégrée d'Evertag pour transférer des fichiers audio sans fil entre votre ordinateur et votre iPhone ou iPad — sans iTunes, sans câbles, sans compte cloud. Les deux appareils doivent être sur le même réseau Wi-Fi.

Dans Evertag 4.2, Wi-Fi Drive bénéficie de :

- **Interface modernisée et rafraîchie** — plus claire, plus lisible d'un coup d'œil et mise à jour pour Liquid Glass.
- **Mode multi-sélection** — choisissez plusieurs fichiers ou dossiers et agissez en lot.
- **File d'envoi plus intelligente** — meilleure information de progression et meilleure résistance aux coupures réseau.
- **Vitesse et fiabilité globales améliorées** — transferts plus rapides pour les grosses bibliothèques.

C'est la façon la plus rapide de déplacer un lot de fichiers audio de l'ordinateur vers le téléphone, d'en modifier les tags, puis de les renvoyer — sans aucun service tiers.

## Réglages de l'éditeur de tags : analyse approfondie

C'est la partie que la plupart des utilisateurs ne lisent jamais — et celle qui décide si vos tags fonctionnent partout ou seulement dans quelques apps. Ouvrez Evertag puis allez dans la section **réglages de l'éditeur de tags audio**. Voici ce que fait chaque option et laquelle choisir selon votre objectif.

### Mise à l'échelle de la pochette

Quand vous enregistrez la pochette dans un fichier audio, Evertag peut redimensionner l'image avant de l'incorporer. Les options sont :

- **Petite** — impact minimal sur la taille du fichier, qualité d'image plus faible.
- **Moyenne** — choix équilibré pour la plupart des utilisateurs.
- **Grande** — haute qualité, adaptée aux lecteurs grand écran et à CarPlay.
- **Très grande** — très haute qualité, augmentation notable de la taille du fichier.
- **Originale (Désactivée)** — incorpore la pochette à sa résolution d'origine. **Aucune mise à l'échelle.**

**Pourquoi c'est important :**

- **Plus de qualité = fichier plus lourd.** Une pochette 3 000 × 3 000 pixels peut ajouter plusieurs Mo à chaque morceau. Multipliez par un album entier et l'impact disque s'accumule vite.
- **Certains lecteurs gèrent mal les images intégrées très grandes.** Vieux appareils, certains autoradios et quelques lecteurs de bureau anciens peuvent buter sur des pochettes au-dessus de ~1 500 px ou refuser de les afficher.
- **Pour la plupart des flux cloud et streaming**, **Moyenne** ou **Grande** est le bon compromis. Utilisez **Originale** uniquement quand vous avez besoin d'une qualité d'archive ou que vous préparez des fichiers pour un lecteur capable de la gérer.

> L'option **Originale** fait partie de la mise à niveau « personnalisation premium » d'Evertag. Les tailles standard (Petite/Moyenne/Grande/Très grande) sont gratuites.

### Options d'enregistrement des tags : ID3v2.4 vs ID3v2.3

C'est le réglage de compatibilité le plus important. ID3v2 est le format de métadonnées utilisé dans les fichiers MP3. Deux versions sont largement utilisées et diffèrent sur des points subtils mais déterminants.

#### ID3v2.4

- Plus récent, prend en charge l'**encodage UTF-8** — manipulation correcte des écritures non latines (chinois, russe, japonais, arabe, hébreu, etc.).
- Plus de types de frames (volume relatif, presets d'égaliseur, etc.).
- **Recommandé pour les lecteurs modernes** qui le supportent.

#### ID3v2.3

- Plus ancien mais **la version d'ID3 la plus universellement supportée**.
- Ne supporte pas UTF-8 directement (utilise UTF-16 pour le texte Unicode).
- **Recommandé quand vous avez besoin d'une compatibilité maximale** avec lecteurs anciens, autoradios et certaines apps de bureau.

#### Quand activer ID3v2.4 dans Evertag

- Vous utilisez des **lecteurs audio modernes** comme Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (versions actuelles) ou des lecteurs Android modernes. ✅ **Activez ID3v2.4.**
- Votre bibliothèque contient des **caractères non latins** (chinois, coréen, japonais, russe, arabe, grec, hébreu). ✅ **Activez ID3v2.4** — UTF-8 les gère bien plus proprement.

#### Quand désactiver ID3v2.4 dans Evertag (utiliser ID3v2.3)

- Vous préparez des fichiers pour un **vieux autoradio ou unité de tableau de bord** qui ne lit pas les tags v2.4.
- Vous voyez du **texte illisible ou des tags manquants** dans certaines apps après édition — c'est un signal fort que v2.4 n'y est pas pris en charge. Repassez en v2.3.
- Vous visez des **lecteurs de bureau anciens** ou de vieux baladeurs (premiers iPods, certains lecteurs MP3 des années 2000–2010).

> **Règle pratique :** si vos tags s'affichent correctement partout en v2.4, laissez activé. Si même un seul lecteur important affiche des caractères erronés, du vide ou ne lit pas les tags, désactivez v2.4 et réenregistrez.

#### Tags dupliqués

Quand vous activez **Tags dupliqués**, Evertag écrit les champs de métadonnées courants (titre, artiste, album, etc.) dans **les sections ID3v1 et ID3v2** du fichier. Cela améliore la compatibilité avec les très vieux lecteurs qui ne lisent qu'ID3v1 (le tag d'origine de 128 octets en fin de fichier).

- **La plupart des utilisateurs n'en ont pas besoin.** Les lecteurs modernes lisent ID3v2 en premier.
- **Activez-le seulement si** vous travaillez avec du matériel vintage ou un logiciel spécifique qui ignore ID3v2.

### Mise à jour des fichiers en ligne : comment Evertag gère les éditions cloud

Quand vous modifiez les tags d'un fichier stocké sur un cloud connecté (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP, etc.), Evertag doit renvoyer le fichier modifié. Vous contrôlez comment :

- **Afficher un message de confirmation** *(par défaut, recommandé)* — Evertag demande avant l'envoi. Idéal pour les utilisateurs prudents et les bibliothèques partagées.
- **Mettre à jour automatiquement les métadonnées du fichier** — envoie en silence après chaque édition. Idéal pour les utilisateurs solo avec des connexions rapides et fiables qui modifient beaucoup.
- **Ne pas mettre à jour les métadonnées du fichier** — Evertag édite seulement la copie locale. Pratique pour prévisualiser sans propager au cloud.

### Modifier des fichiers en ligne : nettoyage du fichier local

Pour modifier un fichier distant, Evertag le télécharge d'abord sur l'appareil. Après édition, vous choisissez ce qu'il advient de cette copie locale :

- **Toujours supprimer le fichier téléchargé** — Evertag retire le fichier temporaire après l'édition. **Recommandé** si vous manquez de stockage ou travaillez sur les fichiers d'autrui.
- **Ne pas supprimer le fichier téléchargé** — conserve le fichier modifié sur votre appareil. Pratique pour avoir à la fois une copie hors ligne et une copie cloud à jour.

### Boutons de l'écran principal

L'écran d'accueil de l'éditeur de tags d'Evertag peut afficher ou masquer des boutons pour des opérations spécifiques. Activez seulement ceux que vous utilisez réellement pour garder l'interface concentrée :

- **Recherche automatique des tags audio** — trouve les métadonnées manquantes en ligne via l'empreinte audio du fichier.
- **Recherche manuelle des tags audio** — recherchez par titre/artiste quand l'auto-recherche échoue.
- **Rechercher la pochette** — trouve et incorpore une pochette de haute qualité.
- **Enregistrer la pochette** — exporte la pochette intégrée vers la photothèque ou les fichiers.
- **Normaliser l'encodage** — corrige le texte non latin illisible causé par d'anciens encodages (très utile pour les pistes en cyrillique, chinois et japonais rippées avec un logiciel ancien).
- **Supprimer les tags audio** — retire tous les tags d'un fichier. Utile avant un re-tagging propre.

### Afficher les tags étendus

Activez ceci pour afficher l'ensemble complet des champs de métadonnées au-delà du basique titre/artiste/album/année — y compris BPM, chef d'orchestre, artiste original, ambiance, copyright, encodeur, commentaires, paroles, et plus encore. Fonction pour utilisateurs avancés ; la plupart des utilisateurs occasionnels n'en ont pas besoin.

### Modifier des fichiers simultanément

Activé, Evertag vous permet d'éditer les métadonnées sur **plusieurs fichiers sélectionnés en même temps** — appliquez le même artiste de l'album, année ou genre à un album entier en une seule opération. C'est la façon la plus rapide de remettre de l'ordre dans une grosse bibliothèque.

## Modifier les tags pour Spotify, Apple Music et les plateformes de streaming

Une question fréquente : « j'ai modifié mes tags dans Evertag, j'ai uploadé les fichiers, et le service de streaming affiche de mauvaises métadonnées. Que se passe-t-il ? »

Réponse courte : **les services de streaming n'honorent pas toujours vos tags locaux**. Apple Music et Spotify ont leurs propres bases de données — quand ils reconnaissent un morceau, ils écrasent les métadonnées affichées avec les leurs. Mais pour les **fichiers téléversés**, vos fichiers locaux (la fonction « Bibliothèque » d'Apple Music, les Fichiers locaux de Spotify) et les **uploads de distributeur vers les plateformes de streaming**, vos tags comptent absolument. Voici comment régler Evertag dans chaque cas :

### Préparer des fichiers pour Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4 : ON** — Apple Music gère UTF-8 correctement.
- **Pochette : Grande** — les apps Apple rendent bien les grandes pochettes ; Originale est excessif.
- **Tags dupliqués : OFF** — pas nécessaire.
- Vérifiez que **Artiste de l'album** est bien rempli — Apple Music s'en sert pour le regroupement.

### Préparer des fichiers pour les Fichiers locaux de Spotify

Les Fichiers locaux de Spotify n'affichent que les fichiers bien tagués. Les tags lus par Spotify sont limités.

- **ID3v2.4 : ON** dans la plupart des cas. Si une piste refuse de s'afficher correctement dans Spotify après édition, **essayez de sauvegarder avec ID3v2.4 OFF** (donc en ID3v2.3) — le parser de Spotify a historiquement été conservateur avec v2.4.
- **Pochette : Moyenne ou Grande** — Spotify la redimensionne de toute façon.
- Remplissez au minimum **Titre**, **Artiste**, **Album** et **Numéro de piste**.

### Préparer des fichiers pour un upload de distributeur (DistroKid, TuneCore, CD Baby, etc.)

Si vous êtes artiste et téléversez vos propres œuvres sur les plateformes de streaming, votre distributeur lit généralement les tags mais demande aussi les métadonnées dans son interface. Dans tous les cas :

- **ID3v2.3** est souvent le choix le plus sûr — beaucoup de pipelines de distributeurs ont été construits il y a des années et préfèrent l'ancien format.
- Incorporez une pochette **Grande** (la plupart des distributeurs exigent ≥ 1 400 × 1 400 px — vérifiez leurs consignes).
- Ne comptez pas sur les tags étendus — les distributeurs ne lisent que les champs de base.

### Préparer des fichiers pour Plex, Jellyfin, Navidrome, Subsonic, Emby

Ces serveurs multimédias auto-hébergés sont très tolérants. Ils lisent v2.3 et v2.4 proprement et gèrent bien UTF-8.

- **ID3v2.4 : ON** convient.
- **Pochette : Grande** ou **Très grande** — ces serveurs servent la pochette aux clients mobiles et aux écrans CarPlay, donc la qualité compte.
- **Artiste de l'album** vivement recommandé — c'est ce que Plex/Jellyfin utilisent pour regrouper les albums par artiste correctement.

### Préparer des fichiers pour autoradios et matériel ancien

- **ID3v2.4 : OFF** (utilisez ID3v2.3) — les vieilles unités ne supportent souvent pas v2.4.
- **Pochette : Moyenne** — beaucoup d'écrans de voiture buttent sur les grandes pochettes intégrées.
- **Tags dupliqués : ON** — les vieux autoradios ne lisent parfois que le repli ID3v1.

## Autres améliorations

### Design Liquid Glass

L'interface d'Evertag 4.2 est ajustée au nouveau matériau **Liquid Glass** d'Apple dans toute l'app — surfaces translucides, animations plus fluides, contrôles affinés qui s'intègrent naturellement à iOS, iPadOS et macOS.

### Bibliothèques de connexion mises à jour

Nous avons rafraîchi les bibliothèques internes utilisées par Evertag pour parler à **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** et d'autres services. Résultat : moins de pannes de connexion sur des cas limites, meilleure compatibilité avec les versions de serveur récentes, et meilleure fiabilité lors de l'édition de tags sur des fichiers distants.

### Corrections de traduction et de localisation

Plusieurs corrections linguistiques dans l'UI à partir des retours directs des utilisateurs. Meilleur ajustement du texte sur les petits boutons dans plusieurs langues.

### Petites améliorations inspirées par vos retours

Beaucoup d'améliorations mineures basées sur les avis App Store et les e-mails à support@everappz.com. Nous lisons chaque message.

## Obtenez Evertag 4.2

[**Téléchargez Evertag sur l'App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) ou mettez à jour depuis l'App Store. Evertag est un téléchargement gratuit avec des achats intégrés optionnels pour les fonctions avancées. Les nouvelles connexions cloud, les protocoles réseau, les améliorations Wi-Fi Drive et l'UI Liquid Glass font partie de la mise à jour de base.

Si vous aimez l'app, laissez-lui une note sur l'App Store — ça aide vraiment. Une remarque ou un souci ? Écrivez-nous à **support@everappz.com**. Nous lisons chaque message.

## Foire aux questions

{{% details title="Quoi de neuf dans Evertag 4.2 ?" closed="true" %}}
Evertag 4.2 ajoute plus de 6 nouvelles connexions cloud et serveur (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), un Wi-Fi Drive rafraîchi avec multi-sélection et une file d'envoi plus intelligente, des mises à jour de l'UI Liquid Glass, des bibliothèques de connexion à jour, des corrections clés d'édition de tags et des améliorations de traduction.
{{% /details %}}

{{% details title="Faut-il utiliser ID3v2.4 ou ID3v2.3 dans Evertag ?" closed="true" %}}
Utilisez **ID3v2.4** pour les lecteurs modernes (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, apps Android modernes) et pour les bibliothèques avec des caractères non latins — le support UTF-8 donne des tags plus propres en chinois, coréen, japonais, russe, arabe et hébreu. Utilisez **ID3v2.3** si vos tags s'affichent mal dans certaines apps, si vous visez de vieux autoradios, ou si un pipeline de distributeur de streaming refuse v2.4. Vous pouvez toujours basculer et réenregistrer.
{{% /details %}}

{{% details title="Pourquoi mes tags sont-ils faux dans Spotify après édition ?" closed="true" %}}
Spotify affiche surtout les métadonnées de son propre catalogue — vos tags locaux ne servent que pour les « Fichiers locaux » ou pour le contenu que vous avez téléversé en tant qu'artiste. Si vous taguez des fichiers pour les Fichiers locaux de Spotify et qu'ils ne s'affichent pas correctement, essayez de désactiver ID3v2.4 dans Evertag et de sauvegarder en ID3v2.3 — le parser de Spotify a été historiquement conservateur avec v2.4.
{{% /details %}}

{{% details title="Quelle taille de pochette choisir dans Evertag ?" closed="true" %}}
Pour la plupart des utilisateurs : **Grande**. Elle rend très bien sur téléphones, iPads, Macs et écrans de voiture modernes sans gonfler trop les fichiers. Utilisez **Moyenne** si vous avez une énorme bibliothèque et voulez économiser du disque. Utilisez **Originale** (sans mise à l'échelle) seulement pour des masters d'archive ou si vous avez vraiment besoin d'une qualité maximale — sachant que certains vieux lecteurs galèrent avec les pochettes intégrées très grandes. **Originale** fait partie de la mise à niveau « personnalisation premium » d'Evertag.
{{% /details %}}

{{% details title="Les pochettes plus grandes vont-elles alourdir mes fichiers ?" closed="true" %}}
Oui. Intégrer une pochette 3 000 × 3 000 px peut ajouter plusieurs mégaoctets à un fichier audio. Sur une bibliothèque de 1 000 morceaux, cela monte vite à plusieurs gigaoctets. Si l'espace est limité, utilisez Moyenne ou Grande ; si vous diffusez depuis un NAS où la taille n'a pas d'importance, Très grande ou Originale conviennent.
{{% /details %}}

{{% details title="Qu'est-ce que les tags dupliqués et faut-il les activer ?" closed="true" %}}
Les tags dupliqués écrivent les métadonnées de base dans les sections ID3v1 (legacy 128 octets) et ID3v2 (moderne) du fichier. Activez-les uniquement si vous visez de très vieux lecteurs ou du matériel qui lit ID3v1. Pour tout ce qui est moderne (smartphones, ordinateurs, autoradios récents), laissez-les désactivés.
{{% /details %}}

{{% details title="Evertag modifie-t-il les tags directement sur les fichiers cloud ?" closed="true" %}}
Oui. Connectez-vous à votre cloud (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, etc.) ou via FTP/SFTP/NFS, ouvrez un fichier et modifiez les tags comme s'il était local. Evertag télécharge le fichier, applique vos modifications et renvoie la version mise à jour. Vous pouvez choisir entre les modes « Toujours demander », « Auto-upload » ou « Ne pas uploader » dans les réglages.
{{% /details %}}

{{% details title="Puis-je modifier les tags FLAC sur iPhone avec Evertag ?" closed="true" %}}
Oui. Evertag prend en charge FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE et d'autres formats majeurs avec un support complet de lecture/écriture des tags, y compris la pochette intégrée.
{{% /details %}}

{{% details title="Comment éditer en toute sécurité les tags sur mon serveur domestique avec SFTP ?" closed="true" %}}
Ouvrez Evertag, allez dans Connexions, choisissez SFTP et saisissez le nom d'hôte ou l'IP de votre serveur, le port (généralement 22), le nom d'utilisateur et soit un mot de passe, soit une clé SSH privée. Evertag parcourra vos dossiers distants et modifiera les tags directement avec un chiffrement de bout en bout sur SSH.
{{% /details %}}

{{% details title="Puis-je modifier les tags de plusieurs fichiers à la fois ?" closed="true" %}}
Oui. Activez **Modifier les fichiers simultanément** dans les réglages. Sélectionnez plusieurs fichiers, ouvrez l'éditeur de tags, et tout champ que vous changez s'applique à tous les fichiers sélectionnés. C'est la façon la plus rapide d'appliquer le même artiste de l'album, année ou genre sur tout un album.
{{% /details %}}

{{% details title="La mise à jour Evertag 4.2 est-elle gratuite ?" closed="true" %}}
Oui. Evertag est un téléchargement gratuit sur l'App Store, et la 4.2 est une mise à jour gratuite pour tous les utilisateurs actuels. Les nouvelles intégrations cloud, les améliorations Wi-Fi Drive et l'UI Liquid Glass font partie de la mise à jour de base.
{{% /details %}}

{{% details title="Sur quels appareils Evertag 4.2 est-il disponible ?" closed="true" %}}
Evertag 4.2 fonctionne sur iPhone, iPad et Mac. La synchronisation iCloud Drive maintient vos réglages d'édition de tags cohérents entre appareils.
{{% /details %}}
