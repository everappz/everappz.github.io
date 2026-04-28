---
title: "Comment connecter un Synology NAS et écouter de la musique sur votre iPhone ou Mac"
date: 2024-09-19
description: "Apprenez à connecter votre Synology NAS en utilisant l'API native ou QuickConnect et à diffuser de la musique de haute qualité sur votre iPhone ou Mac avec Evermusic et Flacbox."
keywords: ["synology nas", "diffuser musique", "quickconnect", "evermusic synology", "flacbox synology", "lecteur musique nas", "musique iphone nas"]
tags: ["musique", "diffusion", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Résumé :** Connectez votre Synology NAS à Evermusic ou Flacbox en utilisant l'API native de Synology -- soit manuellement via l'adresse IP, soit automatiquement via l'identifiant QuickConnect. QuickConnect vous permet de diffuser de la musique à distance sans redirection de ports. Les deux applications prennent en charge FLAC, MP3, WAV et d'autres formats haute résolution.

Si vous cherchez un moyen simple de connecter votre Synology NAS et de profiter de votre bibliothèque musicale sur votre iPhone ou Mac, les applications Evermusic et Flacbox sont les solutions parfaites. Ces applications prennent en charge une large gamme de formats audio, notamment FLAC, MP3 et WAV, facilitant la diffusion et l'écoute de musique de haute qualité directement depuis votre Synology NAS.

Dans ce guide, nous vous montrerons comment connecter votre Synology NAS à l'application Evermusic ou Flacbox en utilisant l'API native de Synology et la fonctionnalité QuickConnect. En exploitant l'API directe de Synology, vous pouvez accéder en toute sécurité à votre bibliothèque musicale en dehors de votre réseau domestique sans avoir besoin de configurations compliquées comme WebDAV, SMB, DLNA. Avec QuickConnect, vous pourrez diffuser et gérer votre musique depuis n'importe où, en utilisant votre iPhone ou Mac.

## Étape 1 : Configurer les permissions du dossier partagé (Optionnel)

1. Ouvrez le **Panneau de configuration** et allez dans la section **Dossier partagé**.

![Dossier partagé](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Sélectionnez le dossier **Musique** et cliquez sur **Modifier**.

3. Dans l'onglet **Permissions**, configurez les autorisations. Activez l'accès invité en lecture seule si vous avez juste besoin d'écouter de la musique, ou en lecture/écriture si vous devez modifier des fichiers. Enregistrez les modifications.

![Permissions](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Étape 2 : Trouver l'adresse IP du Synology NAS

1. Ouvrez le **Panneau de configuration** et allez dans l'onglet **Interface réseau**.

![Interface réseau](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Ou utilisez votre navigateur web pour visiter [find.synology.com](http://find.synology.com).

![Trouver Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Notez l'adresse IP de votre Synology NAS (par ex., 192.168.18.137).

## Étape 3 : Trouver les ports réseau du Synology NAS

Vous pouvez trouver la documentation officielle de Synology pour les ports réseau par défaut de DSM dans cet [article du Centre de connaissances Synology](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM utilise les ports par défaut suivants :
- **HTTP (Accès web) :** Port **5000**
- **HTTPS (Accès web sécurisé) :** Port **5001**

Ce sont les ports par défaut pour accéder à l'interface DSM.

![Ports réseau](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Étape 4 : Activer la fonctionnalité QuickConnect ID

Un identifiant QuickConnect Synology est un identifiant unique qui vous permet d'accéder à votre Synology NAS à distance via Internet sans avoir à configurer des paramètres réseau compliqués comme la redirection de ports. QuickConnect simplifie l'accès à distance en utilisant les serveurs de Synology pour établir une connexion entre votre NAS et votre appareil, comme votre smartphone ou ordinateur, via l'identifiant QuickConnect.

**Comment trouver ou configurer votre identifiant QuickConnect :**

1. **Connectez-vous à DSM.**
2. Allez dans **Panneau de configuration > Accès externe > QuickConnect**.
3. **Activez QuickConnect** et créez ou consultez votre identifiant QuickConnect unique.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Étape 5 : Se connecter au Synology NAS sur votre iPhone/Mac avec Evermusic ou Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) et [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) sont des applications de lecteur de musique conçues pour les appareils iOS et macOS, chacune offrant des fonctionnalités et capacités uniques pour gérer et profiter de votre bibliothèque musicale.

1. Ouvrez l'application Evermusic ou Flacbox et allez dans l'onglet **Connexions**.

![Connexions](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Choisissez **Connecter un service cloud** et sélectionnez **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Vous avez deux options de connexion : **manuelle** en utilisant l'adresse IP et le port du serveur, ou **automatique** via l'identifiant QuickConnect.

### Connexion manuelle

Pour la méthode manuelle, vous aurez besoin de l'adresse IP directe et du numéro de port que vous avez récupérés dans les étapes précédentes.

1. Entrez l'URL du serveur que vous avez obtenue à l'étape 2, en utilisant le format suivant : PROTOCOLE://ADRESSE_IP:NUMÉRO_PORT
   - Utilisez le **port 5000** pour HTTP et le **port 5001** pour les connexions HTTPS.

   Par exemple :
   - HTTP : [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS : [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Le numéro de port réel peut être confirmé à l'étape 3 de votre configuration.
3. Entrez votre **identifiant** et **mot de passe** pour le Synology NAS.
4. Appuyez sur **Se connecter** pour établir la connexion.

![Connexion manuelle](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Connexion automatique

Pour la connexion automatique, vous utiliserez l'**identifiant QuickConnect** de l'étape 4. Au lieu d'entrer manuellement l'adresse IP et le numéro de port de votre Synology NAS, saisissez simplement l'**identifiant QuickConnect**. L'application récupérera automatiquement les informations de connexion nécessaires.

Cette méthode vous permet d'accéder à votre NAS à distance, même en dehors de votre réseau domestique, afin de gérer vos fichiers depuis Internet sans avoir à configurer la redirection de ports ou les adresses IP statiques.

![Connexion automatique](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Authentification à deux facteurs

À partir de DSM 4.2, Synology a introduit la **vérification en 2 étapes** pour renforcer la sécurité. Cette fonctionnalité nécessite un code de **mot de passe à usage unique (OTP)**, généré par une application d'authentification, en plus de vos identifiants de connexion habituels. Si vous avez activé la vérification en 2 étapes, après avoir entré votre nom d'utilisateur et votre mot de passe, vous devrez également saisir l'OTP pour vous connecter à votre session DSM.

Veuillez noter qu'une fois votre session expirée, l'application devra être réautorisée manuellement. Pour réautoriser :

1. Allez dans l'onglet **Connexions** de l'application.
2. Appuyez sur le bouton **Plus d'actions** à côté du nom du serveur.
3. Sélectionnez **Paramètres** dans le menu pour entrer le nouveau code d'authentification et terminer le processus de réautorisation.

Cela garantit que même si vous accédez à votre NAS depuis un réseau non fiable, vos données restent sécurisées.

## Étape 6 : Naviguer et lire la musique

1. Une fois connecté, l'appareil apparaîtra dans la liste des **Appareils connectés**.

![Appareils connectés](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Naviguez jusqu'au dossier **Musique** et appuyez sur n'importe quel fichier audio pour démarrer la lecture.

![Lire la musique](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Étape 7 : Ajouter le dossier cloud connecté à la bibliothèque musicale

1. Ouvrez la section **Bibliothèque musicale** dans l'application.
2. Choisissez **Ajouter de la musique** et sélectionnez **Connexions**.
3. Choisissez votre serveur NAS connecté et sélectionnez le dossier **Musique**. Appuyez sur **Fait**.
4. L'application analysera le dossier de musique et ajoutera les fichiers audio pris en charge à la bibliothèque musicale. Les métadonnées seront chargées et vos pistes seront regroupées par album, artiste et genre.

## Conclusion

En suivant ces étapes, vous pouvez facilement configurer une connexion sur votre Synology NAS et diffuser toute votre bibliothèque musicale sur votre iPhone ou Mac en utilisant Evermusic ou Flacbox. Que vous soyez chez vous ou en déplacement, profitez d'un accès fluide et de haute qualité à vos morceaux préférés depuis n'importe où grâce à QuickConnect. Profitez de la flexibilité et de la commodité que ces applications offrent et commencez à gérer votre collection musicale en toute simplicité sur tous vos appareils.

Avec un accès distant sécurisé via QuickConnect et la prise en charge d'une large gamme de formats audio, vous ne serez jamais loin de votre musique. Maintenant, vos fichiers stockés sur le NAS sont à portée de main !

## FAQ

{{% details title="Quelle est la différence entre la connexion manuelle et QuickConnect ?" closed="true" %}}
La connexion manuelle utilise l'adresse IP et le port du NAS, ce qui fonctionne sur votre réseau local. QuickConnect utilise le service de relais de Synology pour établir une connexion depuis n'importe où via Internet, sans redirection de ports.
{{% /details %}}

{{% details title="Puis-je diffuser de la musique depuis le Synology NAS en dehors de mon réseau domestique ?" closed="true" %}}
Oui. Activez QuickConnect sur votre Synology NAS et utilisez l'identifiant QuickConnect dans Evermusic ou Flacbox pour diffuser de la musique depuis n'importe où avec une connexion Internet.
{{% /details %}}

{{% details title="Quels formats audio sont pris en charge lors de la diffusion depuis le Synology NAS ?" closed="true" %}}
Evermusic et Flacbox prennent en charge FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD et bien d'autres formats. Tous les formats pris en charge fonctionnent lors de la diffusion depuis le Synology NAS.
{{% /details %}}

{{% details title="Ai-je besoin de l'authentification à deux facteurs pour me connecter ?" closed="true" %}}
Non, l'authentification à deux facteurs est optionnelle. Cependant, si vous avez activé la vérification en 2 étapes sur votre Synology DSM, l'application vous demandera un mot de passe à usage unique lors de la connexion. Vous devrez réautoriser lorsque la session expire.
{{% /details %}}

{{% details title="Dois-je utiliser l'API native Synology, WebDAV ou SMB pour me connecter ?" closed="true" %}}
L'API native Synology avec QuickConnect est le meilleur choix pour l'accès distant. Pour l'utilisation sur réseau local, SMB est généralement l'option la plus rapide. WebDAV fonctionne bien pour l'accès local et distant. Evermusic et Flacbox prennent en charge les trois protocoles.
{{% /details %}}
