---
title: "Partage"
date: 2026-08-20
description: "Decouvrez comment fonctionne le partage dans Everdisk : appuyez sur Demarrer pour transformer votre iPhone ou iPad en disque sans fil, choisissez ce que vous partagez (fichiers, dossiers, photos et musique), lancez les quatre serveurs (DLNA, HTTP, WebDAV, FTP), lisez les adresses de connexion, voyez qui est connecte, et gardez le partage actif via Wi-Fi ou cable USB."
keywords: ["partage Everdisk", "disque sans fil iPhone", "demarrer le partage", "partager des fichiers iPhone", "partager des photos sur le reseau", "DLNA HTTP WebDAV FTP", "quoi partager", "comment se connecter", "garder l'application ouverte", "partage Wi-Fi ou cable USB"]
tags: ["everdisk", "guide", "sharing"]
readingTime: 9
---


L'onglet **Partage** est le coeur d'Everdisk. C'est ici que vous transformez votre iPhone ou iPad en disque sans fil, que vous choisissez exactement ce que vous voulez partager, et que vous obtenez les adresses que les autres appareils utilisent pour se connecter. C'est le premier onglet que vous voyez a l'ouverture de l'application.

## Demarrer et arreter le partage

Au centre de l'ecran Partage se trouve un grand bouton rond.

- Appuyez sur **Demarrer** pour mettre en ligne tous vos serveurs actives d'un seul coup. Le bouton affiche **Demarrage...**, puis **Arreter** une fois le partage actif.
- Appuyez sur **Arreter** pour tout remettre hors ligne. Les appareils connectes sont deconnectes.

Tant que le partage est actif, les fichiers, photos et musiques que vous avez choisis sont accessibles a tout appareil du meme reseau qui se connecte via l'une des quatre methodes ci-dessous.

> Le partage ne fonctionne que lorsque l'application est ouverte. Voir **Gardez l'application ouverte** vers la fin de cette page pour comprendre pourquoi, et comment maintenir les gros transferts en cours.

## Choisir ce que vous partagez

Avant de demarrer, appuyez sur l'en-tete **Quoi partager** pour ouvrir trois groupes. Vous pouvez partager n'importe quelle combinaison, et vous devez choisir au moins un element pour pouvoir demarrer le partage.

**Fichiers et dossiers**

- Le dossier **Documents** de l'application est partage par defaut. Vous pouvez arreter de le partager si vous le preferez.
- Appuyez sur **Ajouter un dossier** pour partager un dossier situe n'importe ou sur votre appareil, ou sur **Ajouter un fichier** pour partager des fichiers individuels.
- Chaque element partage dispose d'un bouton **Infos** et d'un bouton **Arreter le partage**.

**Photos et videos**

- Activez **Autoriser l'acces a toute la photothèque** pour partager l'ensemble de vos photos et videos, ou
- Appuyez sur **Ajouter des photos** pour selectionner uniquement les photos et videos que vous souhaitez partager.

**Musique**

- Activez **Autoriser l'acces a toute la bibliothèque musicale** pour partager toute votre musique, ou
- Appuyez sur **Ajouter des morceaux** pour ne partager que certains titres.
- Les morceaux proteges (DRM) ou stockes uniquement dans le cloud ne peuvent pas etre partages.

Si vous essayez de demarrer sans rien avoir selectionne, Everdisk affiche une note **Rien a partager**. Si vous modifiez ce qui est partage pendant que le partage est actif, **arretez puis redemarrez** pour appliquer le changement.

## Les quatre serveurs

Everdisk partage le meme contenu de quatre facons a la fois. Chacune est concue pour un type d'appareil different, et chacune peut etre activee ou desactivee dans **Paramètres → Partage → Connexions**. Par defaut, les quatre sont actives.

- **TV et centre multimedia (DLNA)** - pour les smart TV et lecteurs multimedias. Ils detectent votre appareil tout seuls et affichent vos photos, videos et musiques, avec des miniatures d'apercu.
- **Navigateur (HTTP)** - pour n'importe quel telephone, tablette ou ordinateur. L'autre personne ouvre un lien dans un navigateur web pour parcourir et telecharger vos fichiers. Rien a installer.
- **Ordinateur (WebDAV)** - pour un Mac, un PC Windows ou une machine Linux. Votre appareil apparait comme un lecteur reseau classique, ce qui vous permet de glisser des fichiers dans les deux sens.
- **Autres applications et appareils (FTP)** - pour les applications de fichiers et les utilisateurs avances qui parlent FTP.

Pour les instructions de connexion detaillees, etape par etape, pour chaque type, consultez [Connecter vos appareils](/docs/guide/everdisk/everdisk-guide-connect).

## Comment se connecter et adresses de connexion

Apres avoir appuye sur Demarrer, la section **Comment se connecter** affiche une carte pour chaque serveur actif, avec l'**adresse** exacte a saisir sur l'autre appareil. Chaque adresse est facile a copier : appuyez dessus pour la copier, utilisez le bouton **Partager** pour l'envoyer, ou appuyez sur le bouton **infos (ⓘ)** pour des instructions detaillees, protocole par protocole.

- La carte DLNA affiche une adresse de description d'appareil se terminant par `/device-desc.xml` pour les lecteurs qui en demandent une.
- Lorsque votre appareil est branche a un Mac avec un cable, une adresse supplementaire apparait avec un badge **Connexion par cable** qui utilise le nom `.local` de votre appareil.

Vous pouvez aussi ouvrir l'adresse sous forme de **QR code** pour que la camera d'un autre appareil accede directement a la connexion.

## Qui est connecte

La section **Qui est connecte** liste en temps reel les appareils actuellement connectes a vous. Appuyez sur le bouton d'actions supplementaires a cote de n'importe quel appareil pour **Bloquer cet appareil** si vous ne le reconnaissez pas. Les appareils bloques se gerent dans [Acces et confidentialite](/docs/guide/everdisk/everdisk-guide-access).

## Le nom et l'avatar de votre appareil

Chaque appareil possede un nom convivial (comme « Speedy-Hare ») et un avatar colore. C'est le nom qu'une TV, un ordinateur ou une autre application affiche pour votre appareil sur le reseau, afin de le reperer facilement. Vous pouvez regenerer gratuitement le nom et l'avatar, ou definir un nom, une icone ou un avatar photo personnalises avec Premium. Voir [Paramètres](/docs/guide/everdisk/everdisk-guide-settings).

## Partager en Wi-Fi ou par cable USB

Le partage peut fonctionner dans deux situations :

- **En Wi-Fi** - votre appareil et les autres appareils sont sur le meme reseau Wi-Fi.
- **Par cable USB** - votre appareil est branche a un **Mac** avec un cable, meme en l'absence totale de Wi-Fi. C'est plus rapide que le Wi-Fi et cela continue de fonctionner dans un avion, dans un hotel ou sur un reseau verrouille.

Si ni le Wi-Fi ni un cable ne sont disponibles, le bouton **Demarrer** est desactive et une note **Aucune connexion Wi-Fi** apparait. Si la connexion est perdue pendant le partage, Everdisk arrete automatiquement le partage et vous en informe. Appuyez sur le bouton infos de l'une de ces notes pour une explication complete.

## Gardez l'application ouverte

Comme votre iPhone ou iPad joue le role de serveur, **le partage ne fonctionne que lorsque Everdisk est ouvert a l'ecran**. Si vous fermez l'application ou verrouillez l'appareil pendant longtemps, le systeme peut suspendre l'application et le partage s'arrete.

Pour les gros transferts :

- Gardez Everdisk ouvert et au premier plan.
- Branchez votre appareil sur une source d'alimentation.
- Reglez le **Verrouillage auto.** sur **Jamais** dans l'application Reglages d'iOS pendant le transfert.

Vous pouvez activer **Prevenir avant la deconnexion** (dans Paramètres → Partage) pour qu'Everdisk vous rappelle de rouvrir l'application avant que le systeme ne la suspende. Appuyez sur le bouton infos de la banniere **Gardez l'application ouverte** pour plus de details.

## Etapes suivantes

- [Connecter vos appareils](/docs/guide/everdisk/everdisk-guide-connect) - connectez une TV, un ordinateur, un navigateur, un telephone ou un cable USB.
- [Acces et confidentialite](/docs/guide/everdisk/everdisk-guide-access) - ajoutez un mot de passe et controlez la modification.
- [Paramètres](/docs/guide/everdisk/everdisk-guide-settings) - activez ou desactivez les serveurs et ajustez la qualite.
