---
title: "Comment configurer un serveur FTP sur iPhone et iPad pour les transferts de fichiers"
description: "Transformez votre iPhone ou iPad en serveur FTP avec Everdisk et transférez des fichiers depuis un Mac, un PC Windows, Linux, Android, une application FTP comme FileZilla, ou un autre iPhone via le Wi-Fi. Configuration complète, l'adresse et le port ftp, l'accès invité, et la connexion pas à pas pour chaque appareil."
date: 2026-09-19
tags: ["everdisk", "ftp", "transfert de fichiers", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["serveur FTP iPhone", "serveur FTP iPad", "comment configurer FTP sur iPhone", "application serveur ftp iphone", "connecter FileZilla à un iPhone", "Cyberduck iPhone FTP", "transférer des fichiers iPhone FTP", "ftp iphone vers ordinateur", "ftp iphone vers iphone", "se connecter au FTP de l'iPhone depuis Windows", "adresse port ftp iphone", "ftp anonyme iphone", "partager des fichiers iphone ftp", "ftp iphone pour appareil photo nas"]
readingTime: 9
---

{{< author-byline >}}

FTP est la vieille valeur sûre du transfert de fichiers. Il existe depuis des décennies, et c'est justement ce qui le rend si utile : presque tout ce qui peut dialoguer avec un serveur le comprend. Appareils photo, smart TV, routeurs, lecteurs réseau, outils d'automatisation et toutes les applications FTP de bureau parlent FTP. Avec [Everdisk](/products/everdisk) vous pouvez faire tourner un serveur FTP sur votre iPhone ou iPad, pour que le téléphone devienne un endroit auquel ces appareils et applications peuvent se connecter et déplacer des fichiers.

Optez pour FTP quand les autres options ne conviennent pas, par exemple un appareil plus ancien ou une application qui ne sait se connecter qu'en FTP. Ce guide couvre la configuration et la connexion depuis un Mac, Windows, une application FTP, Linux, Android et un second iPhone.

## Ce dont vous avez besoin

- Un iPhone ou iPad avec [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installé.
- Un ordinateur, une application ou un appareil sur le **même réseau Wi-Fi**.
- Les fichiers que vous voulez partager, dans le dossier Documents d'Everdisk ou dans des dossiers que vous ajoutez.

## Configurer le serveur FTP dans Everdisk

### Étape 1 : choisissez ce qu'il faut partager et réglez l'accès

Ouvrez Everdisk, allez dans l'onglet **Partage**, et touchez **Ce qu'il faut partager**. Le dossier Documents est partagé par défaut. Ajoutez-en davantage avec **Ajouter un dossier** et **Ajouter un fichier**.

Ouvrez **Réglages**, puis **Partage**, puis **Accès**. Activez **Modification des fichiers** si vous voulez que les gens puissent envoyer, renommer et supprimer, ou désactivez-le pour n'autoriser que les téléchargements. Définissez un **Identifiant** et un **Mot de passe** si vous voulez une connexion, ou laissez-les vides pour que n'importe qui puisse se connecter en tant qu'invité.

### Étape 2 : activez le serveur FTP

Allez dans **Réglages**, puis **Partage**, puis **Connexions**, et activez **Autres apps et appareils**. C'est le serveur FTP (il porte l'étiquette FTP).

### Étape 3 : démarrez le partage et notez l'adresse

Retournez dans l'onglet **Partage** et touchez **Démarrer**. La section **Comment se connecter** affiche l'adresse FTP. Elle ressemble à ceci :

```
ftp://192.168.1.20:2121
```

Le nombre après les deux-points est le **port**, qui est **2121** par défaut. La première partie est l'adresse de votre iPhone sur le Wi-Fi, la vôtre sera donc différente. Gardez Everdisk ouvert à l'écran pendant qu'un appareil est connecté.

## Se connecter depuis un Mac

1. Ouvrez le **Finder**, choisissez **Aller**, puis **Se connecter au serveur** (ou appuyez sur **Command et K**).
2. Tapez l'adresse FTP affichée dans Everdisk, par exemple `ftp://192.168.1.20:2121`.
3. Cliquez sur **Se connecter**, puis choisissez **Invité** ou saisissez votre **Identifiant** et votre **Mot de passe**.

Le Finder monte le partage FTP pour que vous puissiez parcourir et copier des fichiers vers votre Mac. Notez que le Finder ouvre le FTP en lecture seule. Quand vous voulez envoyer depuis un Mac, utilisez une application FTP comme décrit ci-dessous.

## Se connecter depuis Windows

1. Ouvrez l'**Explorateur de fichiers** et cliquez sur la barre d'adresse en haut.
2. Tapez l'adresse FTP depuis Everdisk, par exemple `ftp://192.168.1.20:2121`, et appuyez sur **Entrée**.
3. Saisissez votre **Identifiant** et votre **Mot de passe** si vous en avez défini un, ou continuez en tant qu'invité.

Les fichiers partagés apparaissent dans la fenêtre et vous pouvez les copier sur votre PC.

## Se connecter avec une application FTP (FileZilla, Cyberduck)

Pour les envois et un contrôle complet, une application FTP est le meilleur outil. **FileZilla** et **Cyberduck** sont gratuits et tournent sous Windows, Mac et Linux.

1. Ouvrez l'application et créez une nouvelle connexion.
2. Réglez l'**Hôte** sur l'adresse Wi-Fi de votre iPhone, et le **Port** sur **2121**.
3. Pour l'identification, saisissez votre **Identifiant** et votre **Mot de passe**, ou choisissez **Anonyme** si vous n'en avez pas défini.
4. Connectez-vous, et glissez des fichiers dans les deux sens (les envois nécessitent que Modification des fichiers soit activé).

## Se connecter depuis Linux

1. Ouvrez votre gestionnaire de fichiers et choisissez **Se connecter au serveur** ou **Autres emplacements**.
2. Saisissez l'adresse, par exemple `ftp://192.168.1.20:2121`.
3. Connectez-vous en tant qu'invité ou avec votre identifiant.

Vous pouvez aussi utiliser n'importe quel client FTP Linux depuis le terminal, en le pointant vers le même hôte et le port 2121.

## Se connecter depuis Android

Android n'a pas de navigateur FTP système, utilisez donc une application :

1. Installez un client FTP comme **AndFTP**, **FTPCafe**, ou un gestionnaire de fichiers avec prise en charge FTP comme **Solid Explorer**.
2. Ajoutez une connexion avec l'hôte, le **port 2121**, et votre identifiant ou Anonyme.
3. Parcourez et transférez.

## Se connecter depuis un autre iPhone ou iPad

L'app Fichiers d'iOS n'inclut pas de client FTP, utilisez donc l'une de ces options sur le second appareil :

- **L'onglet Appareils d'Everdisk.** Ouvrez Everdisk, allez dans **Appareils**, touchez **Nouvelle connexion**, choisissez **FTP**, et saisissez l'adresse, par exemple `ftp://192.168.1.20:2121`. C'est le chemin le plus simple.
- **Une application FTP dédiée** pour iOS, avec le même hôte, le port 2121 et l'identifiant.

## Connecter d'autres appareils : appareils photo, TV, routeurs et NAS

C'est là que le FTP brille. Beaucoup d'appareils possèdent un client FTP intégré qui peut envoyer ou récupérer des fichiers :

- **Les appareils photo** qui envoient des photos par FTP peuvent les transmettre directement à votre iPhone.
- **Les smart TV, routeurs, NAS et outils d'automatisation** qui prennent en charge FTP peuvent se connecter de la même façon.

Pointez-les vers l'adresse Wi-Fi de votre iPhone, le port **2121**, et votre identifiant (ou Anonyme), en utilisant l'adresse affichée dans Everdisk.

## Lecture seule ou lecture et écriture

Le commutateur **Modification des fichiers** dans Réglages, Partage, Accès contrôle cela. Activé, il laisse les gens envoyer, renommer et supprimer. Désactivé, ils peuvent seulement télécharger. Choisissez la lecture seule quand vous distribuez des fichiers et ne voulez rien voir modifié sur votre téléphone.

## Des usages concrets

- **Connectez FileZilla à votre iPhone** et poussez un lot de fichiers sur le téléphone en une seule fois.
- **Laissez une vieille application ou un appareil qui ne parle que FTP** atteindre vos fichiers quand rien d'autre ne se connecte.
- **Recevez des photos d'un appareil photo** qui les envoie par FTP.
- **Déplacez des fichiers entre un iPhone et un iPad** avec l'onglet Appareils d'Everdisk sur l'appareil récepteur.

## Quelques conseils

- Gardez Everdisk ouvert pendant qu'un appareil est connecté, car iOS met en pause les applications en arrière-plan au bout d'un moment.
- Pour envoyer depuis un Mac, utilisez FileZilla ou Cyberduck plutôt que le Finder, car le Finder ouvre le FTP en lecture seule.
- Laissez l'identifiant vide pour la plus large compatibilité, puis connectez-vous en tant qu'Anonyme, ce que proposent la plupart des clients FTP.
- Le FTP ne chiffre pas son trafic. Sur un réseau auquel vous ne faites pas confiance, utilisez plutôt le [serveur SMB avec chiffrement](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/).

## Questions fréquentes

{{% details title="Quelle est l'adresse et le port FTP de mon iPhone ?" closed="true" %}}
Après le démarrage du partage, Everdisk affiche l'adresse sur l'écran Partage. Elle ressemble à ftp://192.168.1.20:2121. Le 2121 est le port qu'Everdisk utilise pour FTP, et la première partie est l'adresse de votre iPhone sur le Wi-Fi, la vôtre sera donc différente.
{{% /details %}}

{{% details title="Comment connecter FileZilla ou Cyberduck à mon iPhone ?" closed="true" %}}
Ouvrez l'application et créez une nouvelle connexion. Réglez l'Hôte sur l'adresse Wi-Fi de votre iPhone et le Port sur 2121. Saisissez votre Identifiant et votre Mot de passe, ou choisissez Anonyme si vous n'en avez pas défini dans Everdisk. Connectez-vous, et vous pouvez glisser des fichiers dans les deux sens quand Modification des fichiers est activé.
{{% /details %}}

{{% details title="Puis-je me connecter au FTP de mon iPhone depuis Windows ?" closed="true" %}}
Oui. Ouvrez l'Explorateur de fichiers, cliquez sur la barre d'adresse, tapez l'adresse FTP depuis Everdisk (par exemple ftp://192.168.1.20:2121), et appuyez sur Entrée. Saisissez votre identifiant si vous en avez défini un, ou continuez en tant qu'invité. Pour les envois et plus de contrôle, utilisez plutôt une application FTP comme FileZilla.
{{% /details %}}

{{% details title="Ai-je besoin d'une connexion pour FTP ?" closed="true" %}}
Non, une connexion est facultative. Laissez l'Identifiant et le Mot de passe vides dans Réglages, Partage, Accès, et connectez-vous en tant qu'Anonyme, ce que proposent la plupart des clients FTP. Définissez une connexion si vous voulez que les connexions s'identifient d'abord.
{{% /details %}}

{{% details title="Pourquoi puis-je seulement télécharger et pas envoyer via FTP ?" closed="true" %}}
Deux raisons sont fréquentes. D'abord, le commutateur Modification des fichiers dans Réglages, Partage, Accès doit être activé pour autoriser les envois, renommages et suppressions. Ensuite, le Finder du Mac ouvre le FTP en lecture seule, utilisez donc une application FTP comme FileZilla ou Cyberduck quand vous voulez envoyer.
{{% /details %}}

{{% details title="Puis-je utiliser FTP entre deux iPhone ?" closed="true" %}}
Oui. Démarrez le serveur FTP sur le premier iPhone. Sur le second, ouvrez Everdisk, allez dans l'onglet Appareils, touchez Nouvelle connexion, choisissez FTP, et saisissez l'adresse affichée sur le premier téléphone. Une application FTP dédiée pour iOS fonctionne aussi, puisque l'app Fichiers d'iOS n'inclut pas de client FTP.
{{% /details %}}

{{% details title="FTP est-il sécurisé ?" closed="true" %}}
Le FTP simple ne chiffre pas son trafic, considérez-le donc comme un outil pour les réseaux de confiance, comme votre Wi-Fi domestique. Sur un réseau que vous ne contrôlez pas, utilisez le serveur SMB avec Exiger le chiffrement SMB activé, qui protège chaque transfert.
{{% /details %}}

{{% details title="Quels appareils peuvent se connecter via FTP ?" closed="true" %}}
Presque tout ce qui possède un client FTP. Cela comprend les ordinateurs Mac, Windows et Linux, les applications FTP comme FileZilla et Cyberduck, les gestionnaires de fichiers Android, et le matériel comme les appareils photo, smart TV, routeurs, NAS et outils d'automatisation. Cette large portée est la principale raison de choisir FTP.
{{% /details %}}

{{% details title="Pourquoi ma connexion FTP s'est-elle coupée ?" closed="true" %}}
Votre iPhone est le serveur, et iOS met en pause les applications qui restent trop longtemps en arrière-plan. Gardez Everdisk ouvert à l'écran pendant qu'un appareil est connecté, et branchez sur secteur pour les longs transferts. Assurez-vous aussi que les deux appareils sont toujours sur le même Wi-Fi.
{{% /details %}}

{{% details title="Everdisk est-il gratuit ?" closed="true" %}}
Oui, Everdisk se télécharge gratuitement et le serveur FTP est inclus. Un achat Premium unique et facultatif ajoute des extras comme les ports personnalisés et la conversion photo et vidéo. Vous pouvez configurer FTP et transférer des fichiers sans payer.
{{% /details %}}

Envie d'essayer ? [Téléchargez Everdisk sur l'App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) et connectez votre premier client FTP en quelques minutes. Des questions ou des retours ? Écrivez-nous à **support@everappz.com**.
