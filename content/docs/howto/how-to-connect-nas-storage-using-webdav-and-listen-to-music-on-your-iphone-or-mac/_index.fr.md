---
title: "Comment connecter un stockage NAS via WebDAV et écouter de la musique sur votre iPhone ou Mac"
date: 2024-07-28
description: "Découvrez comment configurer WebDAV sur votre Synology NAS et diffuser de la musique sur votre iPhone ou Mac avec Evermusic ou Flacbox. Suivez notre guide étape par étape."
keywords: ["connecter nas", "webdav synology", "diffuser musique nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["musique", "streaming", "stockage", "nas", "connecter", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**En bref :** Installez et activez WebDAV sur votre Synology NAS, configurez les permissions du dossier partagé, puis connectez-vous depuis Evermusic ou Flacbox en utilisant l'adresse IP du NAS et le port WebDAV (par défaut 5005/5006). Vous pouvez diffuser et gérer l'intégralité de votre bibliothèque musicale sans copier de fichiers sur votre appareil.

Découvrez comment connecter votre stockage NAS via WebDAV et diffuser facilement votre bibliothèque musicale sur votre iPhone ou Mac. WebDAV (Web-based Distributed Authoring and Versioning) est un protocole qui vous permet de gérer et partager des fichiers sur Internet. En configurant WebDAV sur votre NAS, vous pouvez accéder à votre collection musicale et la diffuser en streaming, vous assurant d'avoir toujours vos morceaux préférés à portée de main.

Dans ce guide, nous vous montrerons comment configurer une connexion WebDAV sur l'un des serveurs NAS les plus populaires, Synology NAS. Suivez nos étapes simples pour configurer WebDAV sur votre Synology NAS, et vous pourrez parcourir, diffuser et gérer votre bibliothèque musicale directement depuis votre iPhone ou Mac.

## Étape 1 : Installer WebDAV sur Synology NAS

1. Connectez-vous à votre Synology NAS et ouvrez le **Centre de paquets**.
2. Recherchez "webdav" et installez le paquet WebDAV s'il n'est pas déjà installé. Ouvrez le serveur WebDAV pour le configurer.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Installer WebDAV sur Synology" width="600" >}}

## Étape 2 : Configurer le serveur WebDAV

1. Sur la page des paramètres WebDAV, cochez les cases **Activer HTTP**, **Activer HTTPS**, **Activer WebDAV anonyme** et **Activer DavDepthInfinity**.
2. Cliquez sur **Appliquer** pour enregistrer les modifications. Notez les numéros de port pour les connexions HTTP et HTTPS, qui sont 5005 et 5006 par défaut.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Configurer les paramètres WebDAV" width="600" >}}

## Étape 3 : Configurer les permissions du dossier partagé

1. Ouvrez le **Panneau de configuration** et allez dans la section **Dossier partagé**.
2. Sélectionnez le dossier **Musique** et cliquez sur **Modifier**.
3. Dans l'onglet **Permissions**, configurez les permissions. Activez l'accès invité en Lecture seule si vous avez juste besoin d'écouter de la musique, ou Lecture/Écriture si vous devez modifier des fichiers. Enregistrez les modifications.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Permissions du dossier partagé" width="600" >}}

## Étape 4 : Trouver l'adresse IP du Synology NAS

1. Ouvrez le **Panneau de configuration** et allez dans l'onglet **Interface réseau**, ou utilisez votre navigateur web pour visiter [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Trouver l'adresse IP du NAS" width="600" >}}

2. Notez l'adresse IP de votre Synology NAS (par exemple, 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Adresse IP du Synology NAS" width="600" >}}

## Étape 5 : Se connecter au Synology NAS avec Evermusic/Flacbox

1. Ouvrez l'application Evermusic ou Flacbox et allez dans l'onglet **Connexions**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Onglet Connexions dans Evermusic" width="600" >}}

2. Pour la connexion automatique, trouvez votre Synology NAS dans la section **Appareils disponibles** et appuyez dessus pour vous connecter.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Liste des appareils disponibles" width="600" >}}

3. Pour la connexion manuelle, choisissez **Connecter un service cloud** et sélectionnez **WebDAV**. Entrez l'adresse du serveur au format : PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (par exemple, [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Configuration manuelle de WebDAV" width="600" >}}

4. Laissez les champs identifiant et mot de passe vides pour l'accès invité, ou entrez vos identifiants Synology. Appuyez sur **Se connecter**.

## Étape 6 : Naviguer et lire de la musique

1. Une fois connecté, l'appareil apparaîtra dans la liste des **Accessoires connectés**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Appareils connectés dans Evermusic" width="600" >}}

2. Naviguez vers le dossier **Musique** et appuyez sur n'importe quel fichier audio pour lancer la lecture.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Parcourir le dossier Musique" width="600" >}}

## Étape 7 : Ajouter le dossier cloud connecté à la bibliothèque musicale

1. Ouvrez la section **Bibliothèque musicale** dans l'application.
2. Choisissez **Ajouter de la musique** et sélectionnez **Connexions**.
3. Choisissez votre serveur NAS connecté et sélectionnez le dossier **Musique**. Appuyez sur **Fait**.
4. L'application analysera le dossier musical et ajoutera les fichiers audio pris en charge à la bibliothèque musicale. Les métadonnées seront chargées et vos pistes seront regroupées par album, artiste et genre.

## Conclusion

En suivant ces étapes, vous pouvez facilement configurer une connexion WebDAV sur votre Synology NAS et diffuser votre bibliothèque musicale sur votre iPhone ou Mac avec Evermusic ou Flacbox. Profitez d'un accès fluide à vos morceaux préférés à tout moment.

## FAQ

{{% details title="Quels appareils NAS prennent en charge WebDAV ?" closed="true" %}}
La plupart des marques NAS populaires prennent en charge WebDAV, y compris Synology, QNAP, TrueNAS et Western Digital. Consultez la documentation du fabricant de votre NAS pour les instructions de configuration de WebDAV.
{{% /details %}}

{{% details title="Quelle est la différence entre WebDAV et SMB pour le streaming musical depuis un NAS ?" closed="true" %}}
WebDAV fonctionne via HTTP/HTTPS et est mieux adapté à l'accès distant via Internet. SMB est généralement plus rapide sur les réseaux locaux. Evermusic et Flacbox prennent en charge les deux protocoles, choisissez donc selon que vous avez besoin d'un accès local ou distant.
{{% /details %}}

{{% details title="Ai-je besoin d'un nom d'utilisateur et d'un mot de passe pour WebDAV sur Synology ?" closed="true" %}}
Non, si vous activez l'accès anonyme WebDAV et configurez les permissions invité sur votre dossier partagé. Pour une meilleure sécurité, vous pouvez utiliser vos identifiants Synology à la place.
{{% /details %}}

{{% details title="Puis-je diffuser des fichiers FLAC et d'autres formats haute résolution depuis un NAS via WebDAV ?" closed="true" %}}
Oui. Evermusic et Flacbox prennent tous deux en charge les formats FLAC, ALAC, WAV, DSD et d'autres formats haute résolution lors du streaming depuis un stockage NAS via WebDAV.
{{% /details %}}

{{% details title="Pourquoi l'application ne peut-elle pas trouver mon NAS dans les Appareils disponibles ?" closed="true" %}}
Assurez-vous que votre iPhone/Mac et le NAS sont sur le même réseau Wi-Fi. Si la découverte automatique ne fonctionne pas, utilisez l'option de connexion manuelle et entrez directement l'adresse IP du NAS et le port WebDAV.
{{% /details %}}
