---
title: "Comment configurer un serveur WebDAV sur iPhone et iPad pour l'accès et le partage de fichiers"
description: "Transformez votre iPhone ou iPad en serveur WebDAV avec Everdisk et montez-le comme lecteur réseau sur le Finder d'un Mac, l'Explorateur de fichiers de Windows, Linux, Android ou un autre iPhone via le Wi-Fi. Configuration complète, l'adresse et le port WebDAV, et la connexion pas à pas pour chaque appareil."
date: 2026-09-19
tags: ["everdisk", "webdav", "lecteur réseau", "partage de fichiers", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["serveur WebDAV iPhone", "serveur WebDAV iPad", "comment configurer WebDAV sur iPhone", "monter l'iPhone comme lecteur réseau", "connecter iPhone WebDAV Mac Finder", "WebDAV Explorateur de fichiers Windows iPhone", "iphone lecteur réseau Windows", "WebDAV Linux iPhone", "accéder aux fichiers iPhone depuis un ordinateur", "webdav iphone vers iphone", "partager des fichiers iPhone WebDAV", "connecter un lecteur réseau iphone", "transférer des fichiers iphone webdav", "adresse port webdav iphone"]
readingTime: 9
---

{{< author-byline >}}

Le WebDAV transforme un dossier en lecteur réseau qu'un ordinateur peut ouvrir dans son gestionnaire de fichiers habituel. Il fonctionne sur le même protocole web que votre navigateur, c'est pourquoi il voyage bien entre Mac, Windows et Linux sans pilote particulier. Avec [Everdisk](/products/everdisk) vous pouvez faire tourner un serveur WebDAV sur votre iPhone ou iPad, pour que le téléphone apparaisse comme un disque que vous pouvez parcourir, depuis lequel vous copiez, et vers lequel vous copiez depuis presque n'importe quel ordinateur.

Le WebDAV est le meilleur choix quand Windows entre en jeu, car l'Explorateur de fichiers Windows s'y connecte proprement. Ce guide couvre la configuration et la connexion depuis un Mac, Windows, Linux, Android et un second iPhone.

## Ce dont vous avez besoin

- Un iPhone ou iPad avec [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installé.
- Un ordinateur ou un autre appareil sur le **même réseau Wi-Fi**.
- Les fichiers que vous voulez partager, dans le dossier Documents d'Everdisk ou dans des dossiers que vous ajoutez.

## Configurer le serveur WebDAV dans Everdisk

### Étape 1 : choisissez ce qu'il faut partager et réglez l'accès

Ouvrez Everdisk, allez dans l'onglet **Partage**, et touchez **Ce qu'il faut partager**. Le dossier Documents est partagé par défaut. Ajoutez-en davantage avec **Ajouter un dossier** et **Ajouter un fichier**.

Ouvrez **Réglages**, puis **Partage**, puis **Accès**. Activez **Modification des fichiers** si vous voulez que les ordinateurs connectés puissent copier des fichiers sur votre téléphone et les renommer ou les supprimer, ou désactivez-le pour un disque en lecture seule. Définissez ici un **Identifiant** et un **Mot de passe** si vous voulez une connexion, ou laissez-les vides pour l'accès invité.

### Étape 2 : activez le serveur WebDAV

Allez dans **Réglages**, puis **Partage**, puis **Connexions**, et activez **Ordinateur**. C'est le serveur WebDAV (il porte l'étiquette WebDAV).

### Étape 3 : démarrez le partage et notez l'adresse

Retournez dans l'onglet **Partage** et touchez **Démarrer**. La section **Comment se connecter** affiche l'adresse WebDAV. Elle ressemble à ceci :

```
http://192.168.1.20:8080
```

Le nombre après les deux-points est le **port**, qui est **8080** par défaut. La première partie est l'adresse de votre iPhone sur le Wi-Fi, la vôtre différera donc. Gardez Everdisk ouvert à l'écran pendant qu'un appareil est connecté.

## Se connecter depuis un Mac

1. Ouvrez le **Finder**, choisissez **Aller**, puis **Se connecter au serveur** (ou appuyez sur **Command et K**).
2. Tapez l'adresse WebDAV affichée dans Everdisk, par exemple `http://192.168.1.20:8080`.
3. Cliquez sur **Se connecter**, puis choisissez **Invité** ou saisissez votre **Identifiant** et votre **Mot de passe**.

Votre iPhone s'ouvre dans une fenêtre du Finder et se comporte comme un dossier normal. Copiez des fichiers dans un sens ou dans l'autre si Modification des fichiers est activé.

## Se connecter depuis Windows

Windows possède un client WebDAV intégré, cela fonctionne donc depuis l'Explorateur de fichiers.

1. Ouvrez l'**Explorateur de fichiers**, faites un clic droit sur **Ce PC** dans la barre latérale, et choisissez **Ajouter un emplacement réseau** (vous pouvez aussi utiliser **Connecter un lecteur réseau**).
2. Quand l'adresse est demandée, tapez la même adresse WebDAV depuis Everdisk, par exemple `http://192.168.1.20:8080`, puis cliquez sur **Suivant**.
3. Saisissez votre **Identifiant** et votre **Mot de passe** si vous en avez défini un.

L'appareil apparaît alors sous Ce PC comme un emplacement réseau que vous pouvez ouvrir et depuis lequel copier des fichiers. Si Windows refuse de se connecter la première fois, assurez-vous que le service **WebClient** est en cours d'exécution (recherchez Services dans le menu Démarrer, trouvez WebClient et réglez-le pour qu'il démarre), puis réessayez.

## Se connecter depuis Linux

1. Ouvrez votre gestionnaire de fichiers et choisissez **Se connecter au serveur** ou **Autres emplacements**.
2. Saisissez l'adresse avec un préfixe WebDAV, par exemple `dav://192.168.1.20:8080` (utilisez `davs://` uniquement si vous avez configuré le TLS).
3. Connectez-vous en tant qu'invité ou saisissez votre identifiant.

## Se connecter depuis Android

Android n'a pas de navigateur WebDAV système, utilisez donc un gestionnaire de fichiers qui le prend en charge :

1. Installez une application comme **Solid Explorer** ou **CX File Explorer**.
2. Ajoutez une nouvelle connexion **WebDAV**.
3. Saisissez l'hôte et le **port 8080**, choisissez le schéma `http`, et ajoutez votre identifiant si vous en avez défini un.

## Se connecter depuis un autre iPhone ou iPad

L'app Fichiers d'iOS n'inclut pas de client WebDAV, utilisez donc l'une de ces options :

- **L'onglet Appareils d'Everdisk.** Sur le second appareil, ouvrez Everdisk, allez dans **Appareils**, touchez **Nouvelle connexion**, choisissez **WebDAV**, et saisissez l'adresse, par exemple `http://192.168.1.20:8080`. C'est le chemin le plus simple et rien d'autre n'est nécessaire.
- **Une application WebDAV** comme Documents by Readdle, qui peut ajouter une connexion WebDAV avec la même adresse et le même identifiant.

## Vous préférez un lien rapide à un lecteur ?

Si vous voulez seulement récupérer un fichier vite fait sans monter de lecteur du tout, activez la connexion **Navigateur** dans Réglages, Partage, Connexions. Everdisk vous donne alors une adresse web que vous pouvez ouvrir dans n'importe quel navigateur sur n'importe quel appareil pour parcourir et télécharger vos fichiers. C'est le moyen le plus rapide de transmettre un fichier à un PC Windows, un Chromebook ou le téléphone d'un ami.

## Lecture seule ou lecture et écriture

Le commutateur **Modification des fichiers** dans Réglages, Partage, Accès décide de cela. Activé signifie que les ordinateurs connectés peuvent envoyer, renommer et supprimer. Désactivé signifie que le disque est en lecture seule, les autres peuvent donc voir et copier vos fichiers mais ne peuvent pas les modifier.

## Des usages concrets

- **Copiez des fichiers sur votre iPhone depuis un PC Windows** en le connectant comme emplacement réseau et en les glissant dessus.
- **Déchargez photos et documents sur un ordinateur portable** avec le gestionnaire de fichiers que vous connaissez déjà, sans câble ni iTunes.
- **Modifiez un document sur place** depuis votre Mac, en l'ouvrant directement depuis le téléphone et en l'enregistrant.
- **Déplacez un dossier entre un iPhone et un iPad** avec l'onglet Appareils d'Everdisk sur l'appareil récepteur.

## Quelques conseils

- Gardez Everdisk ouvert pendant qu'un appareil est connecté. Verrouiller le téléphone longtemps peut mettre l'app en pause.
- Sous Windows, si la connexion échoue, démarrez le service WebClient et réessayez l'adresse.
- WebDAV et SMB se montent tous deux comme lecteurs réseau. Utilisez WebDAV quand Windows est impliqué, et [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) quand vous voulez la vitesse du Finder et le chiffrement.
- Pour les transferts les plus rapides, laissez la qualité photo et vidéo sur Original dans les Réglages.

## Questions fréquentes

{{% details title="Quelle est l'adresse et le port WebDAV de mon iPhone ?" closed="true" %}}
Après le démarrage du partage, Everdisk affiche l'adresse sur l'écran Partage. Elle ressemble à http://192.168.1.20:8080. Le 8080 est le port qu'Everdisk utilise pour WebDAV, et la première partie est l'adresse de votre iPhone sur le Wi-Fi, la vôtre sera donc différente.
{{% /details %}}

{{% details title="Comment me connecter à mon WebDAV iPhone depuis Windows ?" closed="true" %}}
Ouvrez l'Explorateur de fichiers, faites un clic droit sur Ce PC, et choisissez Ajouter un emplacement réseau ou Connecter un lecteur réseau. Saisissez l'adresse WebDAV depuis Everdisk, par exemple http://192.168.1.20:8080, puis saisissez votre identifiant si vous en avez défini un. Si Windows ne se connecte pas, assurez-vous que le service WebClient est en cours d'exécution (recherchez Services, trouvez WebClient, démarrez-le) et réessayez.
{{% /details %}}

{{% details title="Puis-je utiliser WebDAV entre deux iPhone ?" closed="true" %}}
Oui, mais l'app Fichiers d'iOS n'a pas de client WebDAV, utilisez donc Everdisk sur le second appareil. Ouvrez l'onglet Appareils, touchez Nouvelle connexion, choisissez WebDAV, et saisissez l'adresse affichée sur le premier téléphone. Une application WebDAV comme Documents by Readdle fonctionne aussi.
{{% /details %}}

{{% details title="WebDAV nécessite-t-il un mot de passe ?" closed="true" %}}
Non, une connexion est facultative. Laissez l'Identifiant et le Mot de passe vides dans Réglages, Partage, Accès pour l'accès invité, ou définissez-les si vous voulez que les connexions s'identifient.
{{% /details %}}

{{% details title="D'autres personnes peuvent-elles modifier mes fichiers via WebDAV ?" closed="true" %}}
Seulement si vous l'autorisez. Le commutateur Modification des fichiers dans Réglages, Partage, Accès contrôle cela. Activé, il laisse les appareils connectés envoyer, renommer et supprimer. Désactivé, il rend le disque en lecture seule, les autres peuvent donc voir et copier mais rien modifier.
{{% /details %}}

{{% details title="WebDAV ou SMB, quelle est la différence ?" closed="true" %}}
Les deux montent votre iPhone comme un lecteur réseau. WebDAV fonctionne sur le protocole web et se connecte proprement depuis l'Explorateur de fichiers Windows, ce qui est sa principale force. SMB est le partage de fichiers natif des Mac, Linux et NAS, il est généralement plus rapide sur un Mac, et c'est la seule connexion Everdisk qui peut chiffrer les transferts. Everdisk peut faire tourner les deux en même temps.
{{% /details %}}

{{% details title="Pourquoi mon lecteur WebDAV se déconnecte-t-il ?" closed="true" %}}
Votre iPhone est le serveur, et iOS met en pause les applications qui restent trop longtemps en arrière-plan. Gardez Everdisk ouvert à l'écran pendant qu'un appareil est connecté, et branchez sur secteur pour les longs transferts. Confirmez aussi que les deux appareils sont toujours sur le même Wi-Fi.
{{% /details %}}

{{% details title="Puis-je me connecter via WebDAV sans Wi-Fi ?" closed="true" %}}
Oui, si vous branchez votre iPhone sur un Mac avec un câble. Everdisk affiche alors une adresse de connexion par câble supplémentaire que le Mac connecté peut ouvrir dans le Finder, ce qui fonctionne même sans aucun Wi-Fi. Sur le câble, seul ce Mac peut atteindre l'appareil.
{{% /details %}}

{{% details title="Everdisk est-il gratuit ?" closed="true" %}}
Oui, Everdisk se télécharge gratuitement et le serveur WebDAV est inclus. Un achat Premium unique et facultatif ajoute des extras comme les ports personnalisés et la conversion photo et vidéo. Vous pouvez configurer WebDAV et partager des fichiers sans payer.
{{% /details %}}

Envie d'essayer ? [Téléchargez Everdisk sur l'App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) et montez votre iPhone comme un disque en quelques minutes. Des questions ou des retours ? Écrivez-nous à **support@everappz.com**.
