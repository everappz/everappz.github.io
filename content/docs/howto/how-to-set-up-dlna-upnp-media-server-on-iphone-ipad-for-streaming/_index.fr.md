---
title: "Comment configurer un serveur multimédia DLNA/UPnP sur iPhone et iPad pour la diffusion"
description: "Transformez votre iPhone ou iPad en serveur multimédia DLNA/UPnP avec Everdisk et diffusez photos, vidéos et musique vers une smart TV, une console de jeu, VLC ou Kodi via le Wi-Fi. Configuration complète et connexion depuis les TV Samsung, LG et Sony, Windows, Mac, Linux, Android et un autre iPhone."
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "serveur multimédia", "diffusion", "smart tv", "iphone", "ipad", "wifi"]
keywords: ["serveur DLNA iPhone", "serveur UPnP iPad", "comment configurer DLNA sur iPhone", "diffuser vers une smart TV depuis un iPhone", "serveur multimédia DLNA iOS", "diffuser des vidéos vers la TV sans câble", "lire des photos iPhone sur la TV", "TV Samsung DLNA iPhone", "TV LG DLNA iPhone", "Sony Bravia DLNA iPhone", "VLC DLNA iPhone", "serveur multimédia Kodi DLNA", "serveur multimédia UPnP AV iOS", "diffuser de la musique vers la TV depuis un iPhone", "application serveur multimédia iPhone"]
readingTime: 9
---

{{< author-byline >}}

Le DLNA (aussi appelé UPnP AV) est le discret pilier de la plupart des smart TV. C'est un langage commun qui permet à une TV ou à un lecteur multimédia de trouver une bibliothèque multimédia sur le même Wi-Fi et d'y lire du contenu, sans rien à installer sur la TV. Si votre iPhone ou iPad peut jouer le rôle de cette bibliothèque, vos photos, vidéos et musique apparaissent tout seuls sur le grand écran.

Ce guide montre comment transformer votre iPhone ou iPad en serveur multimédia DLNA/UPnP avec [Everdisk](/products/everdisk), et comment ouvrir cette bibliothèque depuis une smart TV, une console de jeu, VLC, Kodi, un ordinateur, un téléphone Android, et même un second iPhone. Tout fonctionne sur votre Wi-Fi local, donc rien n'est envoyé nulle part.

## Ce dont vous avez besoin

- Un iPhone ou iPad avec [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installé.
- Une TV, un lecteur ou un ordinateur sur le **même réseau Wi-Fi** que votre appareil.
- Les photos, vidéos ou musiques que vous voulez lire, déjà présentes sur votre iPhone (dans l'app Photos, l'app Musique ou le dossier Documents d'Everdisk).

## Configurer le serveur DLNA dans Everdisk

### Étape 1 : choisissez ce qu'il faut partager

Ouvrez Everdisk et allez dans l'onglet **Partage**. Touchez **Ce qu'il faut partager** et sélectionnez votre contenu :

- Activez **Autoriser l'accès à toute la photothèque** pour partager tous les albums, ou touchez **Ajouter des photos** pour en choisir quelques-unes.
- Activez **Autoriser l'accès à toute la bibliothèque musicale** pour partager vos morceaux, ou touchez **Ajouter des morceaux** pour une sélection.
- Ajoutez des dossiers ou des fichiers avec **Ajouter un dossier** et **Ajouter un fichier**. Le dossier Documents de l'app est partagé par défaut.

Vous devez sélectionner au moins un élément avant de pouvoir démarrer le partage.

### Étape 2 : activez TV et centre multimédia (DLNA)

Allez dans **Réglages**, puis **Partage**, puis **Connexions**. Assurez-vous que **TV et centre multimédia** est activé. Il l'est par défaut et porte l'étiquette DLNA. C'est le serveur que les TV et les lecteurs recherchent.

### Étape 3 : démarrez le partage

De retour dans l'onglet **Partage**, touchez le grand bouton **Démarrer**. Votre appareil est maintenant un serveur multimédia sur votre Wi-Fi. Il apparaît aux autres appareils sous son nom convivial, celui affiché comme nom de votre appareil dans l'app (quelque chose comme « Speedy-Hare » tant que vous ne l'avez pas changé).

La diffusion DLNA est toujours ouverte, il n'y a donc aucun mot de passe à saisir sur la TV. Gardez Everdisk ouvert à l'écran pendant que vous regardez, car iOS met en pause les applications reléguées complètement en arrière-plan.

## Lire sur une smart TV

C'est le cas le plus courant, et cela prend généralement une trentaine de secondes.

1. Mettez la TV sur le **même Wi-Fi** que votre iPhone.
2. Ouvrez le lecteur multimédia intégré de la TV. Son nom dépend de la marque : **Media Player**, **Gallery**, **SmartShare** (LG), **AllShare** ou **SmartThings** (Samsung), **Content Share** ou **SimplyShare**.
3. Cherchez la liste des serveurs multimédias ou des sources. Votre appareil y apparaît sous son nom.
4. Sélectionnez-le, parcourez vos photos, vidéos ou musiques, et lancez la lecture.

Les vignettes d'aperçu s'affichent automatiquement, vous pouvez donc trouver le bon album de vacances ou le bon film sans deviner.

### Quelles TV fonctionnent

La plupart des TV **Samsung, LG, Sony BRAVIA, Panasonic (micrologiciel VIERA), Philips et Hisense** intègrent le DLNA et fonctionnent tout de suite. **Les consoles PlayStation et Xbox et la plupart des amplis home-cinéma** aussi.

Quelques plateformes le laissent de côté : **les TV Roku, Amazon Fire TV, Vizio SmartCast et Google TV** simple sans application multimédia du fabricant. Si votre TV est l'une d'elles et ne trouve pas votre appareil, c'est généralement la raison. Sur ces TV, installez une application lecteur DLNA comme VLC ou Kodi, ou accédez plutôt à vos fichiers via un navigateur web avec le [guide de configuration WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/).

Certaines marques ont conservé le DLNA même après avoir retiré le logo DLNA officiel, donc s'il semble absent, cherchez l'un des noms de lecteur multimédia ci-dessus.

## Lire dans VLC ou Kodi sur Windows, Mac et Linux

VLC et Kodi sont gratuits, tournent sur tous les systèmes de bureau et maîtrisent bien le DLNA. Ils constituent le moyen fiable d'ouvrir votre bibliothèque Everdisk sur un ordinateur.

**VLC (Windows, Mac, Linux) :**

1. Ouvrez VLC.
2. Affichez la liste de lecture (sous Windows et Linux appuyez sur **Ctrl+L**, sous Mac ouvrez la **Playlist** depuis le menu Vue).
3. Dans la barre latérale, ouvrez **Universal Plug'n'Play** sous Réseau local.
4. Votre appareil apparaît dans la liste. Cliquez dessus et choisissez un fichier.

**Kodi (Windows, Mac, Linux) :**

1. Allez dans **Vidéos**, **Musique** ou **Images**, puis **Fichiers**, puis **Ajouter une source** (ou **Parcourir**).
2. Choisissez **Appareils UPnP**.
3. Sélectionnez votre appareil et parcourez votre bibliothèque.

Sous Windows, vous pouvez aussi ouvrir **Windows Media Player**, déplier **Autres bibliothèques** dans la barre latérale, et votre appareil y apparaît.

## Lire sur Android

Les téléphones et tablettes Android n'ont pas de navigateur DLNA système, utilisez donc une application :

- **VLC pour Android** : ouvrez le menu latéral, touchez **Réseau local**, et votre appareil apparaît sous les serveurs UPnP.
- **BubbleUPnP** ou une application UPnP similaire : votre appareil apparaît dans la liste des serveurs, et ces applications peuvent aussi renvoyer la lecture vers une TV.

## Lire sur un autre iPhone ou iPad

Deux appareils, une bibliothèque. Disons que les photos sont sur votre iPhone et que vous voulez les regarder sur votre iPad.

- Le chemin le plus simple est l'onglet **Appareils** d'Everdisk sur le second appareil. Il fonctionne comme client DLNA autant que comme serveur. Ouvrez Everdisk sur l'iPad, allez dans **Appareils**, et votre iPhone apparaît sous **Appareils disponibles**. Touchez-le pour parcourir et lire.
- N'importe quelle application lecteur DLNA pour iOS fonctionne aussi, comme VLC ou un navigateur UPnP. Ouvrez sa vue de réseau local et choisissez votre iPhone.

## Lire sur une console de jeu

- **PlayStation 5 et 4** : ouvrez l'application **Média** (Galerie multimédia), et votre appareil apparaît comme un serveur multimédia que vous pouvez parcourir.
- **Xbox** : utilisez une application lecteur multimédia qui prend en charge le DLNA, puis choisissez votre appareil dans la liste des serveurs.

## Si votre appareil n'apparaît pas dans la liste

Certains lecteurs permettent d'ajouter un serveur multimédia par adresse plutôt que d'attendre qu'il soit découvert. Sur l'écran **Partage** d'Everdisk, la carte DLNA affiche une adresse de description d'appareil qui se termine par `/device-desc.xml`. Saisissez cette adresse dans le champ d'ajout de serveur du lecteur.

Si ça n'apparaît toujours pas, vérifiez trois points : les deux appareils sont sur le même Wi-Fi (pas un réseau invité qui bloque le trafic entre appareils), Everdisk est ouvert et le partage est démarré, et **TV et centre multimédia** est activé dans les Réglages.

## Si une vidéo ne se lit pas

Le DLNA transmet le fichier tel quel à la TV, et la TV doit pouvoir le décoder. Si un extrait refuse de se lire, son format n'est probablement pas pris en charge par cette TV. Deux solutions :

- Ouvrez **Réglages**, puis **Partage**, puis **Vidéos**, et baissez la **Qualité**. Everdisk convertit alors la vidéo vers un format plus compatible pendant la diffusion. (La conversion est une fonction Premium.)
- Ou ouvrez le même fichier dans un navigateur web avec le lien de navigateur d'Everdisk, qui est plus tolérant sur les formats.

## Des usages concrets

- **Soirée cinéma en famille.** Les vidéos filmées sur votre téléphone se lisent sur la TV du salon sans câble ni Apple TV.
- **Les photos de vacances sur grand écran.** Ouvrez votre photothèque sur la TV et faites défiler le voyage avec tout le monde dans la pièce.
- **Musique d'ambiance à une fête.** Pointez une enceinte DLNA ou un ampli home-cinéma vers votre bibliothèque musicale et laissez tourner.
- **Regarder sur la TV d'un hôtel** dotée d'un lecteur multimédia, une fois les deux appareils sur le Wi-Fi de la chambre.

## Quelques conseils

- Gardez Everdisk ouvert pendant que vous diffusez. Si vous verrouillez le téléphone longtemps, iOS peut mettre l'app en pause et la lecture s'arrête.
- Branchez le téléphone sur secteur pour les longues séances de film.
- Pour la diffusion la plus rapide, laissez **Format** et **Qualité** sur **Original** dans les Réglages, et ne les baissez que si une TV précise a du mal avec un fichier.
- Le DLNA sert uniquement à la diffusion. Personne côté TV ne peut modifier ni supprimer vos fichiers. Pour un transfert de fichiers dans les deux sens, utilisez plutôt le serveur [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/), [WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) ou [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/).

## Questions fréquentes

{{% details title="Quelle est la différence entre DLNA et UPnP ?" closed="true" %}}
Ils sont étroitement liés. L'UPnP est la norme réseau sous-jacente, et le DLNA est le profil multimédia construit par-dessus, que les TV et les lecteurs utilisent pour partager et lire photos, vidéos et musique. Dans l'usage courant, les deux mots sont interchangeables. Quand vous activez TV et centre multimédia dans Everdisk, votre appareil devient un serveur multimédia DLNA/UPnP que n'importe quel client DLNA peut parcourir.
{{% /details %}}

{{% details title="Dois-je installer quelque chose sur ma TV ?" closed="true" %}}
Non. Si votre TV prend en charge le DLNA, elle possède déjà un lecteur multimédia capable de trouver votre appareil sur le Wi-Fi. Vous installez uniquement Everdisk sur l'iPhone ou l'iPad qui contient le contenu. Si votre TV ne prend pas en charge le DLNA, installez un lecteur comme VLC ou Kodi sur un appareil qui lui est connecté.
{{% /details %}}

{{% details title="Pourquoi mon iPhone n'apparaît-il pas sur la TV ?" closed="true" %}}
Vérifiez que les deux appareils sont sur le même réseau Wi-Fi. Les réseaux invités et certains réseaux de bureau ou d'hôtel empêchent les appareils de se voir, ce qui bloque le DLNA. Confirmez ensuite qu'Everdisk est ouvert avec le partage démarré, et que TV et centre multimédia est activé dans Réglages, Partage, Connexions. Si la TV ne le trouve toujours pas, ajoutez le serveur à la main avec l'adresse de description d'appareil qui se termine par /device-desc.xml.
{{% /details %}}

{{% details title="La diffusion DLNA nécessite-t-elle un mot de passe ?" closed="true" %}}
Non. Le DLNA est toujours ouvert à quiconque sur le même Wi-Fi tant qu'il est activé, c'est pourquoi il n'y a pas de connexion à saisir côté TV. C'est très bien sur un réseau domestique de confiance. Sur un réseau auquel vous ne faites pas confiance, désactivez TV et centre multimédia une fois terminé, ou utilisez plutôt le serveur SMB avec chiffrement.
{{% /details %}}

{{% details title="Puis-je diffuser vers un Chromecast ou un Roku ?" closed="true" %}}
Le Chromecast et le Roku ne fonctionnent pas comme lecteurs DLNA d'origine, ils ne trouveront donc pas directement votre appareil. La solution consiste à installer une application DLNA capable de caster, comme VLC ou BubbleUPnP sur un téléphone, et à y renvoyer la lecture vers le Chromecast ou le Roku. Sur la plupart des autres smart TV, le DLNA fonctionne sans tout cela.
{{% /details %}}

{{% details title="Une vidéo se lit sans son ou ne s'ouvre pas. Que puis-je faire ?" closed="true" %}}
C'est un format que la TV ne peut pas décoder. Ouvrez Réglages, Partage, Vidéos dans Everdisk et baissez la Qualité pour que l'app convertisse la vidéo vers un format plus compatible pendant la diffusion. Vous pouvez aussi ouvrir le même fichier via le lien de navigateur, qui gère plus de formats.
{{% /details %}}

{{% details title="Puis-je diffuser de la musique, pas seulement de la vidéo ?" closed="true" %}}
Oui. Activez Autoriser l'accès à toute la bibliothèque musicale, ou ajoutez des morceaux précis, puis démarrez le partage. Vos morceaux apparaissent sur n'importe quelle enceinte DLNA, ampli home-cinéma ou TV, avec la pochette et les détails du morceau. La musique est toujours partagée en qualité originale.
{{% /details %}}

{{% details title="L'app doit-elle rester ouverte pendant que je regarde ?" closed="true" %}}
Oui. Votre iPhone joue le rôle de serveur, et iOS met en pause les applications reléguées complètement en arrière-plan pendant longtemps. Gardez Everdisk à l'écran pendant que vous diffusez, et branchez sur secteur pour les longues séances.
{{% /details %}}

{{% details title="Comment diffuser d'un iPhone vers un autre iPad ?" closed="true" %}}
Démarrez le partage sur l'iPhone, puis ouvrez Everdisk sur l'iPad et allez dans l'onglet Appareils. L'iPhone apparaît sous Appareils disponibles comme serveur multimédia. Touchez-le pour parcourir et lire. Everdisk fonctionne comme client et comme serveur DLNA, vous n'avez donc pas besoin d'une autre application.
{{% /details %}}

{{% details title="Everdisk est-il gratuit ?" closed="true" %}}
Oui, Everdisk se télécharge gratuitement et le serveur multimédia DLNA est inclus. Un achat facultatif et unique Premium à vie ajoute des extras comme la conversion photo et vidéo pour les TV plus anciennes, les ports personnalisés et plus encore. Vous pouvez configurer et utiliser la diffusion DLNA sans payer.
{{% /details %}}

Envie d'essayer ? [Téléchargez Everdisk sur l'App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) et diffusez votre premier album vers la TV en quelques minutes. Des questions ou des retours ? Écrivez-nous à **support@everappz.com**.
