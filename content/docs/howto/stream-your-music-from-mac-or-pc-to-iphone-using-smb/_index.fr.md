---
title: "Diffusez votre musique depuis Mac ou PC vers iPhone via SMB"
description: "Apprenez à diffuser votre collection musicale depuis Mac ou Windows PC vers votre iPhone ou iPad en utilisant Evermusic et le protocole SMB. Un guide simple étape par étape pour vous connecter et profiter de l'audio sans synchronisation."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["diffuser musique de Mac vers iPhone", "streaming audio SMB iOS", "configuration Evermusic SMB", "connecter musique PC iPhone", "partage musique Mac iOS", "streaming fichiers SMB Windows", "accès Evermusic dossiers PC"]
---

{{< author-byline >}}


**En bref :** Utilisez l'application Evermusic pour iPhone ou iPad pour diffuser de la musique depuis votre Mac ou Windows PC via votre réseau local en utilisant SMB. Pas de synchronisation, pas de copie -- activez simplement le partage de fichiers sur votre ordinateur, connectez-vous dans l'application et lisez. La configuration prend moins de 5 minutes.

Vous vous noyez dans un océan de musique sur votre MAC ou PC et voulez en profiter sans tracas sur votre iPhone ou iPad ? Ne cherchez pas plus loin qu'Evermusic. Avec Evermusic, il est incroyablement simple de connecter votre ordinateur en utilisant le protocole SMB et de diffuser vos mélodies préférées sans vous soucier d'occuper de l'espace supplémentaire sur l'appareil ou de gérer les problèmes de synchronisation. Voici un guide étape par étape pour commencer :

## Étape 1 : Activez le protocole SMB sur votre ordinateur

![Evermusic - Support SMB - Écran de partage Mac](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Si vous utilisez MAC

- Ouvrez Préférences Système -> Partage.
- Activez le service de Partage de fichiers.
- Dans la section "Dossiers partagés", ajoutez votre dossier de musique, sélectionnez un utilisateur et définissez les niveaux d'autorisation (Lecture et écriture ou Lecture seule).
- Pour plus de commodité, vous pouvez sélectionner "Tout le monde : Lecture seule" pour le dossier de musique, le rendant facilement accessible dans Evermusic.
- N'oubliez pas de retenir l'URL de votre ordinateur (smb://192.168.xx.xx) pour les étapes suivantes.

![Evermusic - Support SMB - Écran de partage de fichiers](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Touchez "Options" et activez "Partager les fichiers et dossiers via SMB."
- Activez "Partage de fichiers Windows" pour les comptes disponibles.

![Evermusic - Support SMB - Écran de partage de fichiers et dossiers](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Si vous utilisez un Windows PC

![Evermusic - Support SMB - Partager des fichiers sur Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Faites un clic droit sur votre dossier de musique.
- Sélectionnez "Propriétés."
- Ouvrez l'onglet "Partage."
- Cliquez sur "Partager..."
- Choisissez les personnes avec qui partager et définissez leurs niveaux d'autorisation.
- Comme avec MAC, vous pouvez opter pour "Tout le monde : Lecture" pour le dossier de musique sélectionné.
- Cliquez sur "Fait" pour enregistrer vos paramètres.

![Evermusic - Support SMB - Dossier partagé sur Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Étape 2 : Ajoutez votre ordinateur automatiquement

- Maintenant, ouvrez Evermusic et allez dans l'onglet "Connexions" ("Réseau" si vous utilisez une ancienne version de l'application).
- Si vous voyez votre ordinateur dans la section "Appareils disponibles" ("Partages disponibles" si vous utilisez une ancienne version de l'application) et avez sélectionné "Tout le monde : Lecture seule" à l'étape précédente, touchez simplement votre ordinateur et il se connectera automatiquement.
- Si cela ne se produit pas, vous pouvez ajouter votre ordinateur manuellement.

![Evermusic - Support SMB - Écran de connexion de compte](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Étape 3 : Ajoutez votre ordinateur manuellement

- Touchez "Connecter un service cloud" ("Ajouter un compte" si vous utilisez une ancienne version de l'application)
- Sélectionnez "SMB" dans la liste des serveurs disponibles sur l'écran suivant.
- Sur l'écran des paramètres "SMB" :
  - Entrez l'URL du serveur avec le chemin du dossier partagé. Vous pouvez entrer le nom du serveur ou l'IP du serveur. Par exemple :
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Entrez votre identifiant et mot de passe ou laissez ces champs vides si vous avez sélectionné "Tout le monde : Lecture seule" à l'étape précédente.
  - Le champ "WORKGROUP" est facultatif et doit être utilisé si vous avez un domaine Active Directory.

![Evermusic - Support SMB - Écran de saisie des identifiants](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Une fois votre compte SMB connecté, il apparaîtra dans la section "Services cloud" ("Comptes"). Ouvrez le compte connecté en le touchant, naviguez vers le dossier de musique et touchez n'importe quel fichier audio pour démarrer le lecteur.

![Evermusic - Support SMB - Écran d'ouverture du dossier connecté](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Profitez de votre collection musicale en toute fluidité sur votre iPhone ou iPad avec Evermusic.

![Evermusic - Support SMB - Écran du lecteur audio](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Étape 4 : Solution de contournement SMB2

Si vous rencontrez des problèmes pour parcourir les dossiers ou lire des fichiers contenant des caractères spéciaux (comme ü, ö, é), cela peut être lié au protocole SMB2. Nous travaillons activement à la résolution de ce problème.

Comme solution temporaire, essayez d'activer SMB 1 sur votre serveur et dans les paramètres de l'application. Alternativement, vous pouvez vous connecter à votre serveur SMB en utilisant le menu d'ouverture de fichiers du système. Voici comment :

1. Naviguez vers "Fichiers locaux."
2. Faites défiler vers le bas jusqu'à la section "Fichiers sur cet appareil" et touchez "Ouvrir des fichiers..." ou "Ouvrir des dossiers..."
3. Localisez votre serveur et sélectionnez les fichiers ou dossiers dont vous avez besoin.
4. Touchez "Ouvrir" pour confirmer votre sélection.

## Étape 5 : Solution de contournement WebDAV

De plus, vous pouvez essayer de vous connecter à votre NAS en utilisant les protocoles WebDAV ou DLNA s'ils sont pris en charge.

En suivant ces étapes, vous pouvez contourner les problèmes liés aux caractères spéciaux dans les noms de fichiers et continuer à profiter de vos fichiers multimédias.

P.S. Vous pouvez également transférer des fichiers audio de votre MAC/PC vers votre iPhone en utilisant le Partage de fichiers iTunes et lire des fichiers audio locaux. En savoir plus sur cette fonctionnalité dans notre guide : [Comment lire les fichiers iTunes sur iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Questions fréquemment posées

{{% details title="Puis-je diffuser de la musique de mon PC vers mon iPhone sans iTunes ?" closed="true" %}}
Oui. Evermusic se connecte à votre PC via SMB sur votre réseau Wi-Fi local. iTunes n'est pas nécessaire. Activez simplement le partage de fichiers sur votre PC et connectez-vous dans l'application.
{{% /details %}}

{{% details title="Le streaming SMB utilise-t-il des données mobiles ?" closed="true" %}}
Non. SMB fonctionne sur votre réseau Wi-Fi local. Aucune connexion Internet ni données mobiles ne sont nécessaires.
{{% /details %}}

{{% details title="Quels formats audio Evermusic prend-il en charge via SMB ?" closed="true" %}}
Evermusic prend en charge MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC et d'autres formats audio courants. Les fichiers sont lus directement depuis le partage SMB.
{{% /details %}}

{{% details title="Puis-je diffuser de la musique depuis un NAS vers mon iPhone ?" closed="true" %}}
Oui. Si votre NAS prend en charge SMB (la plupart le font, y compris Synology, QNAP et WD My Cloud), vous pouvez vous y connecter en utilisant les mêmes étapes de ce guide.
{{% /details %}}

{{% details title="Dois-je garder mon ordinateur allumé pendant la diffusion ?" closed="true" %}}
Oui. Comme Evermusic diffuse les fichiers directement depuis votre ordinateur, celui-ci doit être allumé et connecté au même réseau que votre iPhone.
{{% /details %}}

{{% details title="Y a-t-il une limite de taille de fichier pour le streaming SMB ?" closed="true" %}}
Non. Evermusic diffuse des fichiers de toute taille via SMB. Les gros fichiers sans perte (FLAC, WAV) fonctionnent sans problème.
{{% /details %}}
