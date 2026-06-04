---
title: "Connexions"
date: 2020-02-01
description: "Apprenez à connecter le stockage cloud, un NAS et votre ordinateur à Evertag. Accédez et modifiez les fichiers audio directement depuis le stockage cloud, un NAS personnel ou un Mac/PC."
keywords: [
  "configuration cloud Evertag", "connecter iCloud à Evertag", "accès aux fichiers SMB iOS",
  "éditeur de tags audio WebDAV", "modification des métadonnées NAS", "Wi-Fi Drive Evertag",
  "transférer des fichiers audio vers iPhone", "Evertag iTunes File Sharing", "modifier les tags FLAC depuis le cloud"
]
tags: ["guide", "evertag", "connexions"]
readingTime: 11
---


Sur cet écran, vous pouvez connecter diverses sources contenant vos fichiers audio. Vous pouvez intégrer des services cloud populaires comme Google Drive, Dropbox, OneDrive, iCloud et d'autres, ainsi que connecter votre Mac ou PC. De plus, vous avez la possibilité de modifier les fichiers audio situés dans Apple Time Capsule, WD Cloud Home ou tout NAS compatible SMB ou WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Écran des connexions Evertag" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Accès rapide

En haut de l'écran Connexions, vous trouverez une liste d'**Accès rapide**. Tout dossier cloud que vous ajoutez aux favoris — même enfoui plusieurs niveaux dans l'arborescence — apparaît ici afin que vous puissiez y accéder directement sans naviguer à travers les dossiers parents à chaque fois.

## Se connecter au stockage cloud

- Ouvrez l'onglet **Connexions**
- Sélectionnez «Connexion au stockage cloud» dans le menu
- Choisissez un service de stockage cloud dans la liste
- Entrez vos identifiants et appuyez sur «Terminer».

Si vous rencontrez des problèmes, vérifiez votre connexion Internet et votre identifiant/mot de passe.
Dans la version Premium de l'application, vous pouvez ajouter un nombre illimité de services.

## Services de stockage cloud pris en charge

Actuellement, l'application prend en charge les services de stockage cloud les plus populaires : iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), ainsi que tout serveur SMB ou WebDAV.

## Sécurité et confidentialité

Nous utilisons uniquement des SDK officiels et des connexions sécurisées pour interagir avec les services cloud connectés. Votre identifiant et votre mot de passe ne sont pas accessibles à l'application. Toutes les requêtes de l'application vers le service cloud sont chiffrées.

Lorsque vous entrez votre identifiant et votre mot de passe, l'application vous affiche la page d'autorisation officielle fournie par le fournisseur de service cloud, et l'ensemble du processus d'autorisation se déroule en dehors de l'application. Le fournisseur de service cloud envoie un token d'authentification à l'application après une autorisation réussie, et ce token est utilisé pour effectuer des appels API.

Un token d'authentification est une clé numérique qui permet aux applications tierces d'interagir avec le stockage cloud. Le token d'authentification est stocké sur votre appareil dans un stockage système sécurisé appelé Keychain. Vous pouvez télécharger vos fichiers depuis le service cloud connecté vers l'appareil, et ces fichiers seront placés dans le répertoire «Documents» de l'application. Vous pouvez supprimer ces fichiers à tout moment à l'aide du gestionnaire de fichiers intégré.

L'application ne partage aucune information provenant du compte cloud connecté. Vous pouvez révoquer l'accès à votre compte cloud à tout moment en ouvrant la page des paramètres du compte dans votre navigateur web.

## Révoquer le token d'authentification

Connectez-vous à votre compte dans un navigateur web et accédez à la page des paramètres. Là, vous pouvez trouver toutes les applications tierces connectées à votre compte cloud et en supprimer si vous ne souhaitez plus utiliser cette application. Des instructions détaillées sont disponibles [ici](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Vous pouvez également déconnecter les comptes cloud connectés dans l'application, et le token d'authentification sera également supprimé de votre appareil. Si vous supprimez l'application de votre appareil, toutes les données téléchargées et les tokens d'accès seront également supprimés.

## Déconnecter un stockage cloud ou modifier la configuration

- Accéder aux options de stockage cloud : Localisez d'abord le stockage cloud que vous souhaitez gérer dans l'interface de l'application.
- Appuyez sur le bouton «...» : À côté du titre du service, vous verrez un bouton «...». Appuyez dessus pour accéder aux options supplémentaires.
  - **Renommer** : Si vous souhaitez modifier le nom du service cloud tel qu'il apparaît dans votre liste, sélectionnez «Renommer».
  - **Paramètres** : Pour modifier la configuration ou les données d'authentification du service cloud, choisissez «Paramètres». Vous devrez parfois réautoriser le service cloud connecté si le token d'autorisation a expiré.
  - **Se déconnecter** : Si vous souhaitez rompre complètement la connexion entre l'application et le service cloud, sélectionnez «Se déconnecter». Sachez que cette option supprimera tous les morceaux associés à ce service cloud de la bibliothèque musicale de votre application, mais ils resteront sur le serveur.

## Se connecter à un ordinateur ou un NAS

Vous pouvez également connecter votre ordinateur, votre NAS personnel ou d'autres périphériques réseau en utilisant le protocole SMB, DLNA ou WebDAV.

## Connexion à un ordinateur via SMB

- Appuyez sur «Connexion au stockage cloud» → SMB.
- Entrez l'adresse IP de l'ordinateur et le nom du dossier partagé dans le champ URL en utilisant le format smb://adresse-ip-ordinateur/nom-dossier-partagé
- Choisissez la version du protocole : Auto, SMB1, SMB2
- Entrez votre identifiant et mot de passe (si nécessaire)
- Appuyez sur «Terminer».

Si votre connexion réussit, vous verrez le stockage connecté dans la section «Stockage cloud».
Un tutoriel complet sur la façon de connecter votre Mac ou PC via SMB est disponible [ici](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Connexion à un NAS via WebDAV

Toutes les étapes sont identiques sauf pour le champ URL.
L'URL doit être au format http://nom-du-serveur, ou https://nom-du-serveur si le serveur prend en charge SSL.
Un tutoriel complet sur la façon de connecter un NAS via le protocole WebDAV est disponible [ici](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Appareils disponibles

Cette section affiche tous les appareils de votre réseau local auxquels vous pouvez vous connecter via l'application.
Pour établir une connexion avec un appareil, suivez ces étapes :

- Ouvrez l'application et accédez à la section «Appareils disponibles».
- Appuyez sur l'appareil auquel vous souhaitez vous connecter dans la liste.
- Si nécessaire, entrez vos informations de connexion pour compléter la connexion.

## Wi-Fi Drive

Wi-Fi Drive est une technologie pratique qui permet le transfert sans fil de fichiers depuis votre ordinateur vers votre appareil iOS via un navigateur de bureau.
Pour utiliser cette fonctionnalité efficacement, assurez-vous que votre appareil et votre ordinateur sont connectés au même réseau Wi-Fi.
Voici un guide étape par étape sur la façon d'utiliser Wi-Fi Drive.

## Activer Wi-Fi Drive

- Ouvrez l'application et accédez à l'onglet **Connexions**.
- Sélectionnez «Connexion via Wi-Fi» pour accéder à l'écran principal de Wi-Fi Drive.
- Appuyez sur «Démarrer Wi-Fi Drive» pour activer Wi-Fi Drive.

## Accéder à Wi-Fi Drive sur votre ordinateur

- Sur votre ordinateur (de bureau ou portable), ouvrez un navigateur web (tel que Chrome, Firefox ou Safari).
- Dans la barre d'adresse du navigateur, entrez l'URL fournie par l'application.

## Transférer des fichiers sans fil

Une fois que la page web correspondant à votre appareil iOS s'ouvre dans le navigateur, vous pouvez facilement faire glisser et déposer des fichiers depuis votre ordinateur sur la page web.
Les fichiers que vous faites glisser et déposez commenceront à se transférer vers votre appareil iOS et seront accessibles dans l'application.

Des instructions détaillées sur la façon de transférer des fichiers sans fil via Wi-Fi Drive sont disponibles [ici](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing est une autre technologie qui vous permet de transférer des fichiers d'un ordinateur vers un appareil en utilisant l'application Finder sur votre Mac et un câble Lightning.
- Connectez simplement l'appareil à l'ordinateur à l'aide d'un câble et lancez l'application Finder sur votre Mac.
- Ouvrez «Emplacements» → «Votre appareil connecté» → «Fichiers» → et trouvez l'application actuelle.
- Appuyez sur l'icône de l'application pour voir tous les dossiers partagés.
- Copiez les fichiers de l'ordinateur vers le dossier partagé sur l'appareil par glisser-déposer.

Des instructions détaillées sur l'utilisation d'iTunes File Sharing sont disponibles [ici](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Connecter une clé USB

Si vous avez une carte SD ou une clé USB, vous pouvez la connecter à l'aide d'un lecteur de carte Lightning ou USB-C sur iPhone/iPad, ou la brancher directement sur un Mac. L'application prend actuellement en charge les lecteurs de carte certifiés Apple. Nous avons des instructions détaillées sur la façon de connecter une clé USB à votre iPhone ou iPad et de gérer les fichiers qui s'y trouvent, disponibles [ici](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Les lecteurs connectés apparaissent dans la section **Accessoires externes** de l'écran Connexions.

## Gestionnaire de fichiers

Une fois que vous avez connecté un service de stockage cloud, appuyez sur son icône pour afficher tous les fichiers et dossiers disponibles. Vous pouvez utiliser le gestionnaire de fichiers intégré pour travailler avec ces fichiers — télécharger, renommer, déplacer et plus encore. Lorsque vous démarrez un téléchargement, le fichier apparaît dans la file de transfert. Pour afficher la file de transfert, accédez à l'onglet «Fichiers locaux» et appuyez sur les flèches tournantes dans le coin supérieur gauche. Tous les fichiers et dossiers téléchargés sont disponibles dans la section «Fichiers locaux».

## Barre d'outils supérieure

La barre d'outils supérieure, commodément située sous la barre de navigation, offre plusieurs actions utiles pour un accès facile. Vous pouvez afficher ou masquer cette barre d'outils en utilisant un simple geste de balayage vers le bas. Voici les actions disponibles :

- **Rechercher** : Cette option vous permet d'effectuer une recherche rapide dans le répertoire actuel, facilitant la localisation de fichiers ou dossiers spécifiques.

## Options de dossier

Lorsque vous ouvrez un dossier dans l'application, vous trouverez un ensemble pratique d'actions disponibles en appuyant sur le bouton «...» dans le coin supérieur droit de l'écran.
Voici un aperçu de ces actions :

- **Sélectionner** : Activez le mode de sélection de fichiers. Ce mode vous permet de choisir un ou plusieurs fichiers dans le dossier, facilitant ainsi l'exécution d'actions sur les éléments sélectionnés.
- **Nouveau dossier** : Créez un nouveau dossier dans le dossier actuel. Cette fonctionnalité vous permet d'organiser vos fichiers et de maintenir votre bibliothèque bien structurée.
- **Téléverser des fichiers** : Téléversez des fichiers depuis votre appareil vers le dossier en ligne. Cette action vous permet de transférer des fichiers vers le cloud ou le serveur, les rendant accessibles de n'importe où.
- **Rechercher** : Recherchez des fichiers spécifiques dans le dossier actuel. Ceci est particulièrement utile pour localiser rapidement des éléments spécifiques dans une grande collection.
- **Trier** : Triez les fichiers dans le dossier selon des critères tels que le nom, la taille ou la date de modification. Le mode de tri par défaut reflète généralement l'ordre de tri sur le serveur, mais vous pouvez le modifier selon vos préférences.
- **Vue grille/liste** : Basculez entre deux modes d'affichage : vue tableau et vue vignettes. La vue tableau présente les fichiers sous forme de liste, tandis que la vue vignettes affiche des représentations visuelles des fichiers, facilitant l'identification du contenu d'un coup d'œil.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tri du dossier cloud Evertag" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Modifier des fichiers en ligne

Lorsque vous devez gérer plusieurs fichiers dans votre stockage cloud sur cette application, vous pouvez utiliser le mode de sélection pour rationaliser vos actions. Suivez ces étapes pour une gestion efficace des fichiers :

- **Activer le mode de sélection** : Ouvrez l'application sur votre appareil et accédez à la section contenant votre stockage cloud. Cherchez le bouton «...» (points de suspension) dans le coin supérieur droit. Appuyez dessus et choisissez l'élément de menu «Sélectionner» pour activer le mode de sélection.
- **Choisir des fichiers** : Vous remarquerez des cases à cocher apparaître à côté de chaque fichier ou dossier listé. Choisissez un ou plusieurs fichiers ou dossiers en appuyant simplement sur les cases à cocher à côté d'eux.
- **Effectuer diverses actions** : Une fois que vous avez sélectionné les fichiers ou dossiers que vous souhaitez gérer, vous aurez accès à plusieurs actions adaptées à vos besoins :

{{< cards cols="1">}}
  {{< card title="" subtitle="Sélection de fichier Evertag" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Actions sur les fichiers

Près du titre du fichier, vous remarquerez un symbole de points de suspension «...» (trois points) – il sert de menu d'actions.
Appuyez dessus pour révéler une liste d'actions disponibles :

- **Modifier les balises audio** : En sélectionnant cette option, vous pouvez accéder à l'éditeur de tags intégré, vous permettant de modifier les tags audio pour le fichier choisi. Le fichier sera temporairement téléchargé dans un répertoire temporaire puis téléversé vers le stockage après que vous confirmez les modifications.
- **Ajouter aux favoris** : Cette action ajoute le fichier à votre liste de fichiers favoris pour un accès rapide et pratique.
- **Télécharger** : Choisissez cette action pour télécharger le fichier ou le dossier sur votre appareil, le rendant accessible pour une utilisation hors ligne.
- **Renommer** : Cette option vous permet de renommer le fichier directement sur le stockage distant, permettant une dénomination personnalisée.
- **Déplacer** : Optez pour cette action pour déplacer le fichier vers un autre dossier dans votre stockage cloud, aidant à maintenir une structure de fichiers organisée.
- **Ouvrir dans** : Utilisez cette action pour exporter le fichier vers une autre application compatible. Le fichier sera téléchargé sur votre appareil, puis la boîte de dialogue de partage apparaîtra pour un partage ou une interaction supplémentaire.
- **Supprimer** : Soyez prudent avec cette action, car elle supprime définitivement le fichier de votre stockage cloud. **Cette suppression ne peut pas être annulée**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Options de fichier Evertag" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Si la liste des actions dépasse l'espace disponible à l'écran, faites simplement défiler vers le bas dans le menu des actions pour accéder aux options supplémentaires.

## Actions sur les dossiers

Pour chaque dossier dans votre stockage cloud, vous disposez de diverses actions. Pour accéder à ces options, appuyez simplement sur l'icône de points de suspension «...» située à côté du titre du dossier. Si vous ne voyez pas toutes les actions, faites défiler vers le bas pour en révéler davantage. Voici les actions disponibles :

- **Ajouter aux favoris** : Utilisez cette action pour ajouter le dossier à votre liste de fichiers favoris pour un accès rapide et pratique.
- **Télécharger** : Téléchargez tout le contenu du dossier sur votre appareil pour un accès hors ligne.
- **Renommer** : Renommez le dossier directement sur le stockage distant.
- **Déplacer** : Déplacez le dossier vers un autre emplacement dans votre stockage cloud.
- **Supprimer** : Soyez prudent avec cette action, car elle supprime définitivement le dossier et son contenu de votre stockage cloud. **Cette action ne peut pas être annulée**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Options de dossier Evertag" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
