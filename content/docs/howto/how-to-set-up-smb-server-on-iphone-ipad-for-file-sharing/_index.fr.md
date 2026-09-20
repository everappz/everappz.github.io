---
title: "Comment configurer un serveur SMB sur iPhone et iPad pour le partage de fichiers"
description: "Transformez votre iPhone ou iPad en serveur de fichiers SMB avec Everdisk et ouvrez-le comme un lecteur réseau depuis un Mac, un autre iPhone, Linux ou Android via le Wi-Fi. Configuration complète, l'adresse et le port smb, le chiffrement SMB3 en option, et la connexion pas à pas pour chaque appareil."
date: 2026-09-19
tags: ["everdisk", "smb", "partage de fichiers", "lecteur réseau", "iphone", "ipad", "mac", "finder", "chiffrement", "wifi"]
keywords: ["serveur SMB iPhone", "serveur SMB iPad", "comment configurer SMB sur iPhone", "partage SMB iPhone", "connecter iPhone SMB Mac Finder", "smb iphone vers iphone", "app Fichiers iOS se connecter à un serveur SMB", "partager des fichiers iPhone SMB", "iphone lecteur réseau Finder", "chiffrement SMB3 iOS", "partage smb iPhone Android", "se connecter à SMB depuis Linux", "iphone comme lecteur réseau", "partager des fichiers entre iphones wifi", "monter l'iphone comme lecteur réseau"]
readingTime: 10
---

{{< author-byline >}}

SMB est le partage de fichiers intégré à macOS, Windows et Linux, et à presque tous les lecteurs réseau (NAS). Quand vous vous connectez à un dossier partagé sur un autre ordinateur et qu'il s'ouvre comme un disque normal dans Finder ou l'Explorateur de fichiers, c'est SMB qui travaille. Avec [Everdisk](/products/everdisk) vous pouvez placer un partage SMB sur votre iPhone ou iPad, pour que le téléphone lui-même apparaisse comme un lecteur réseau que d'autres appareils parcourent, depuis lequel ils copient, et vers lequel ils copient.

C'est l'option à privilégier quand vous voulez que votre iPhone se comporte comme un vrai disque, pas comme une page web. C'est rapide, ça glisse-dépose dans les deux sens, et c'est le seul type de connexion d'Everdisk qui peut chiffrer chaque transfert. Ce guide couvre la configuration et la connexion depuis un Mac, un autre iPhone ou iPad, Linux, Android et Windows.

## Ce dont vous avez besoin

- Un iPhone ou iPad avec [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installé.
- Un autre appareil sur le **même réseau Wi-Fi**.
- Les fichiers que vous voulez partager, dans le dossier Documents d'Everdisk ou dans des dossiers que vous ajoutez.

## Configurer le serveur SMB dans Everdisk

### Étape 1 : choisissez ce qu'il faut partager et qui peut écrire

Ouvrez Everdisk, allez dans l'onglet **Partage**, et touchez **Ce qu'il faut partager**. Le dossier Documents est partagé par défaut. Ajoutez-en davantage avec **Ajouter un dossier** et **Ajouter un fichier**, et activez votre photothèque ou votre bibliothèque musicale si vous voulez aussi les rendre disponibles.

Décidez si les autres appareils peuvent seulement lire vos fichiers, ou aussi les modifier. Ouvrez **Réglages**, puis **Partage**, puis **Accès**, et réglez **Modification des fichiers**. Activé, les appareils connectés peuvent copier des fichiers sur votre téléphone et les renommer ou les supprimer. Désactivé, le partage est en lecture seule.

Si vous voulez une connexion, définissez un **Identifiant** et un **Mot de passe** sur le même écran Accès. Laissez les deux vides pour autoriser l'accès invité.

### Étape 2 : activez le serveur SMB

Allez dans **Réglages**, puis **Partage**, puis **Connexions**, et activez **Ordinateur (avancé)**. C'est le serveur SMB (il porte l'étiquette SMB).

### Étape 3 : démarrez le partage et notez l'adresse

Retournez dans l'onglet **Partage** et touchez **Démarrer**. La section **Comment se connecter** affiche maintenant l'adresse SMB. Elle ressemble à ceci :

```
smb://192.168.1.20:4455/Share
```

Trois choses à savoir sur cette adresse :

- Le nombre après les deux-points est le **port**. Everdisk utilise **4455** par défaut.
- Le partage s'appelle **Share**.
- La première partie est l'adresse de votre iPhone sur le Wi-Fi, elle sera donc différente sur votre réseau.

Gardez Everdisk ouvert pendant que des appareils sont connectés, car iOS met en pause les applications qui restent trop longtemps en arrière-plan.

## Se connecter depuis un Mac

C'est le cas le plus fluide, car macOS parle SMB nativement.

Le moyen le plus rapide : ouvrez le **Finder** et regardez dans la barre latérale sous **Emplacements** ou **Réseau**. Everdisk se signale sur le Wi-Fi, votre iPhone y apparaît donc souvent tout seul. Cliquez dessus, puis cliquez sur **Se connecter comme** et choisissez **Invité**, ou saisissez votre identifiant.

Pour vous connecter à la main :

1. Dans le Finder, choisissez **Aller**, puis **Se connecter au serveur** (ou appuyez sur **Command et K**).
2. Tapez l'adresse SMB affichée dans Everdisk, par exemple `smb://192.168.1.20:4455/Share`.
3. Cliquez sur **Se connecter**, puis choisissez **Invité** ou saisissez votre **Identifiant** et votre **Mot de passe**.

Votre iPhone s'ouvre dans une fenêtre du Finder. Copiez des fichiers dans un sens ou dans l'autre en les glissant, exactement comme n'importe quel autre disque (si Modification des fichiers est activé).

## Se connecter depuis un autre iPhone ou iPad

iOS et iPadOS peuvent ouvrir les partages SMB dans l'app **Fichiers** intégrée, ce qui rend les transferts de téléphone à téléphone propres et rapides.

Sur le second appareil :

1. Ouvrez l'app **Fichiers**.
2. Touchez le bouton **plus** (les trois points, en haut à droite sur iPhone) et choisissez **Se connecter au serveur**.
3. Saisissez l'adresse SMB depuis Everdisk, par exemple `smb://192.168.1.20:4455/Share`.
4. Choisissez **Invité**, ou **Utilisateur enregistré** et saisissez votre identifiant.
5. Le partage apparaît sous Emplacements dans Fichiers. Parcourez et copiez dans un sens ou dans l'autre.

Vous pouvez aussi utiliser l'onglet **Appareils** d'Everdisk sur le second appareil, qui inclut un client SMB. Ouvrez Everdisk, allez dans **Appareils**, touchez **Nouvelle connexion**, choisissez **SMB**, et saisissez l'adresse.

## Se connecter depuis Linux

1. Ouvrez votre gestionnaire de fichiers (Files/Nautilus sur GNOME, Dolphin sur KDE).
2. Choisissez **Autres emplacements** ou **Se connecter au serveur**.
3. Saisissez l'adresse, par exemple `smb://192.168.1.20:4455/Share`.
4. Connectez-vous en tant qu'invité, ou saisissez votre identifiant.

Depuis un terminal, vous pouvez aussi lancer `smbclient //192.168.1.20/Share -p 4455` et saisir votre identifiant quand il est demandé.

## Se connecter depuis Android

Android n'a pas de navigateur SMB système, utilisez donc un gestionnaire de fichiers qui prend en charge SMB :

1. Installez une application comme **CX File Explorer**, **Solid Explorer** ou **X-plore File Manager**.
2. Ajoutez une nouvelle connexion **SMB** ou **LAN**.
3. Saisissez l'hôte (l'adresse Wi-Fi de votre iPhone), réglez le **port sur 4455**, et le nom de partage **Share**.
4. Connectez-vous en tant qu'invité ou avec votre identifiant, puis parcourez et copiez.

## Se connecter depuis Windows

Windows peut lire les partages SMB, avec une réserve à connaître d'emblée. L'Explorateur de fichiers intégré ne parle SMB que sur le port standard et ne permet pas de taper un port personnalisé dans le chemin, or Everdisk utilise le port 4455. Le simple **Connecter un lecteur réseau** n'y parvient donc souvent pas.

Vous avez deux bonnes options sous Windows :

- Utilisez un gestionnaire de fichiers ou un client SMB qui permet de définir un port personnalisé, et pointez-le vers l'adresse de votre iPhone avec le port **4455** et le nom de partage **Share**.
- Ou connectez-vous depuis Windows via l'un des autres serveurs d'Everdisk. La [configuration WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) et la [configuration FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) fonctionnent toutes deux bien depuis l'Explorateur de fichiers Windows, et le lien de navigateur marche dans n'importe quel navigateur.

Si vous voulez tout de même essayer Connecter un lecteur réseau : ouvrez l'**Explorateur de fichiers**, faites un clic droit sur **Ce PC**, choisissez **Connecter un lecteur réseau**, et saisissez l'hôte et le nom de partage affichés dans Everdisk. Si la connexion échoue, c'est la limitation de port ci-dessus, passez donc à WebDAV ou FTP.

## Activer le chiffrement pour un Wi-Fi non fiable

SMB est la seule connexion Everdisk qui peut chiffrer chaque transfert, ce qui compte sur un Wi-Fi que vous ne contrôlez pas entièrement, comme un café ou un réseau de bureau.

1. Dans **Réglages**, **Partage**, **Accès**, définissez un **Identifiant** et un **Mot de passe**. Les connexions chiffrées ne peuvent pas être anonymes, cette étape est donc obligatoire.
2. Dans **Réglages**, **Partage**, activez **Exiger le chiffrement SMB**.
3. Arrêtez puis redémarrez le partage pour que la modification prenne effet.

Chaque transfert SMB est alors protégé par le **chiffrement SMB3 (AES)**. L'appareil qui se connecte doit prendre en charge SMB3, ce que font le Finder sur un Mac récent ainsi que Windows 10 et versions ultérieures. Le chiffrement SMB fait partie de l'achat Premium unique.

## Lecture seule ou lecture et écriture

Le commutateur **Modification des fichiers** dans Réglages, Partage, Accès contrôle cela pour chaque serveur, y compris SMB. Activez-le et les appareils connectés peuvent envoyer, renommer et supprimer. Désactivez-le et ils peuvent seulement parcourir et copier des fichiers depuis votre téléphone. Choisissez la lecture seule quand vous transmettez des fichiers à quelqu'un à qui vous ne voulez rien laisser modifier.

## Des usages concrets

- **Déplacez un gros dossier sur votre iPhone depuis un Mac** en le glissant dans la fenêtre du Finder, plus vite qu'un envoi web.
- **Récupérez une journée de photos et de vidéos de votre téléphone** vers un ordinateur portable, sans iTunes ni câble.
- **Envoyez des fichiers entre deux iPhone** via l'app Fichiers, sans troisième application d'un côté ni de l'autre.
- **Travaillez sur un fichier sur place**, en ouvrant un document directement depuis le téléphone dans une app sur votre Mac et en l'enregistrant.

## Quelques conseils

- Gardez Everdisk ouvert pendant qu'un appareil est connecté. Verrouiller le téléphone longtemps peut mettre l'app en pause et couper la connexion.
- Si un Mac ne voit pas le téléphone dans la barre latérale du Finder, connectez-vous à la main avec Se connecter au serveur et l'adresse smb complète.
- Pour la meilleure vitesse sur les gros transferts, laissez la qualité photo et vidéo sur Original dans les Réglages.
- Sur un réseau non fiable, activez Exiger le chiffrement SMB et désactivez les autres serveurs pendant que vous travaillez.

## Questions fréquentes

{{% details title="Quelle est l'adresse et le port SMB de mon iPhone ?" closed="true" %}}
Après le démarrage du partage, Everdisk affiche l'adresse sur l'écran Partage. Elle ressemble à smb://192.168.1.20:4455/Share. Le 4455 est le port qu'Everdisk utilise pour SMB, et Share est le nom du dossier partagé. La première partie est l'adresse de votre iPhone sur le Wi-Fi, la vôtre sera donc différente.
{{% /details %}}

{{% details title="Puis-je me connecter au partage SMB de mon iPhone depuis Windows ?" closed="true" %}}
L'Explorateur de fichiers Windows ne se connecte à SMB que sur le port standard et n'accepte pas de port personnalisé dans le chemin, alors qu'Everdisk utilise le port 4455. Le simple Connecter un lecteur réseau n'y parvient donc souvent pas. Utilisez un gestionnaire de fichiers qui permet de définir un port personnalisé, ou connectez-vous depuis Windows avec WebDAV, FTP ou le lien de navigateur. Tous fonctionnent depuis Windows sans souci de port.
{{% /details %}}

{{% details title="Comment partager des fichiers entre deux iPhone avec SMB ?" closed="true" %}}
Démarrez le serveur SMB sur le premier iPhone dans Everdisk. Sur le second iPhone, ouvrez l'app Fichiers, touchez le bouton plus, choisissez Se connecter au serveur, et saisissez l'adresse smb affichée dans Everdisk (par exemple smb://192.168.1.20:4455/Share). Connectez-vous en tant qu'Invité ou avec votre identifiant, et le partage apparaît dans Fichiers. Vous pouvez aussi utiliser l'onglet Appareils d'Everdisk sur le second téléphone.
{{% /details %}}

{{% details title="Mon iPhone apparaît-il automatiquement dans la barre latérale du Finder du Mac ?" closed="true" %}}
Généralement oui. Everdisk signale le partage SMB sur votre Wi-Fi, votre iPhone apparaît donc souvent sous Emplacements ou Réseau dans la barre latérale du Finder. Cliquez dessus et choisissez Se connecter comme, puis Invité ou votre identifiant. S'il n'apparaît pas, connectez-vous à la main avec Aller, Se connecter au serveur et l'adresse smb complète.
{{% /details %}}

{{% details title="Ai-je besoin d'un mot de passe pour utiliser SMB ?" closed="true" %}}
Non, une connexion est facultative. Laissez l'Identifiant et le Mot de passe vides dans Réglages, Partage, Accès pour autoriser l'accès invité. Définissez-les si vous voulez que les connexions s'identifient. Un identifiant et un mot de passe ne sont requis que si vous activez Exiger le chiffrement SMB, car les connexions chiffrées ne peuvent pas être anonymes.
{{% /details %}}

{{% details title="La connexion SMB est-elle chiffrée ?" closed="true" %}}
Elle peut l'être. SMB est la seule connexion Everdisk qui prend en charge le chiffrement. Définissez un identifiant et un mot de passe, puis activez Exiger le chiffrement SMB dans Réglages, Partage. Chaque transfert est alors protégé par SMB3 (AES). L'autre appareil doit prendre en charge SMB3, ce que font les Mac récents et Windows 10 ou version ultérieure. Le chiffrement est une fonction Premium.
{{% /details %}}

{{% details title="Les autres personnes peuvent-elles modifier ou supprimer mes fichiers via SMB ?" closed="true" %}}
Seulement si vous l'autorisez. Le commutateur Modification des fichiers dans Réglages, Partage, Accès contrôle cela. Activé, les appareils connectés peuvent envoyer, renommer et supprimer. Désactivé, le partage est en lecture seule et les autres peuvent parcourir et copier des fichiers depuis votre téléphone mais ne peuvent rien modifier.
{{% /details %}}

{{% details title="Pourquoi ma connexion SMB s'est-elle coupée ?" closed="true" %}}
Votre iPhone est le serveur, et iOS met en pause les applications qui restent trop longtemps en arrière-plan. Gardez Everdisk ouvert à l'écran pendant qu'un appareil est connecté, et branchez le téléphone sur secteur pendant les longs transferts. Vérifiez aussi que les deux appareils sont restés sur le même Wi-Fi.
{{% /details %}}

{{% details title="SMB, WebDAV ou FTP, lequel choisir ?" closed="true" %}}
Utilisez SMB quand vous voulez que le téléphone se comporte comme un vrai lecteur réseau sur un Mac, un autre iPhone, Linux ou un NAS, et quand vous voulez du chiffrement. Utilisez WebDAV quand vous voulez un lecteur réseau qui fonctionne aussi bien depuis Windows. Utilisez FTP pour la plus large compatibilité avec les appareils et applications plus anciens. Everdisk peut tous les faire tourner en même temps, vous n'êtes donc pas enfermé dans un seul.
{{% /details %}}

{{% details title="Everdisk est-il gratuit ?" closed="true" %}}
Oui, Everdisk se télécharge gratuitement et le serveur SMB est inclus. L'achat Premium unique et facultatif ajoute le chiffrement SMB, les ports personnalisés et quelques autres extras. Vous pouvez configurer SMB et partager des fichiers sans payer.
{{% /details %}}

Envie d'essayer ? [Téléchargez Everdisk sur l'App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) et ouvrez votre iPhone dans le Finder en une minute environ. Des questions ou des retours ? Écrivez-nous à **support@everappz.com**.
