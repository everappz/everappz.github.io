---
title: "Connecter vos appareils"
date: 2026-08-20
description: "Instructions etape par etape pour vous connecter a votre disque sans fil Everdisk : regardez sur un smart TV via DLNA, ouvrez vos fichiers dans n'importe quel navigateur web, montez votre appareil comme lecteur reseau dans le Finder, sous Windows ou Linux via WebDAV, connectez des applications de fichiers en FTP, et transferez par cable USB vers un Mac sans Wi-Fi."
keywords: ["se connecter a Everdisk", "diffuser vers la TV DLNA", "ouvrir des fichiers dans le navigateur", "monter un lecteur reseau Finder", "WebDAV Windows Linux", "application de fichiers FTP", "transfert par cable USB Mac", "connecter iPhone a un ordinateur", "lecteur reseau iPhone"]
tags: ["everdisk", "guide", "connect"]
readingTime: 11
---


Une fois que vous avez appuye sur **Demarrer** sur l'ecran [Partage](/docs/guide/everdisk/everdisk-guide-sharing), les autres appareils peuvent se connecter a vos fichiers de quatre facons differentes. Choisissez la methode qui correspond a l'appareil que vous voulez utiliser. Dans tous les cas, l'**adresse** exacte dont vous avez besoin est affichee dans la section **Comment se connecter** de l'ecran Partage.

> Les deux appareils doivent etre sur le **meme reseau Wi-Fi** - ou, pour un Mac, relies par un **cable USB** (voir la derniere section).

## Regarder sur une TV (DLNA)

Utilisez cette methode pour afficher des photos, videos et musiques sur un smart TV ou un lecteur multimedia.

1. Dans **Paramètres → Partage → Connexions**, assurez-vous que **TV et centre multimedia** est active (il l'est par defaut).
2. Sur l'ecran Partage, appuyez sur **Demarrer**.
3. Sur votre TV, ouvrez son lecteur multimedia integre ou son application de serveur multimedia (elle peut s'appeler Media Player, SmartShare, AllShare ou quelque chose de similaire).
4. Votre appareil apparait dans la liste des serveurs multimedias sous son nom (par exemple « Speedy-Hare »). Selectionnez-le.
5. Parcourez vos photos, videos et musiques partagees et lancez la lecture. Les miniatures d'apercu apparaissent automatiquement.

Remarques :

- Le DLNA ne peut pas etre protege par mot de passe : cette connexion est donc ouverte a toute personne sur le meme Wi-Fi tant qu'elle est activee.
- Si une video refuse de se lire sur une TV ancienne, baissez la qualite video dans **Paramètres → Partage → Videos** pour qu'Everdisk la convertisse dans un format plus compatible.

## Ouvrir dans un navigateur web (HTTP)

Utilisez cette methode pour transmettre des fichiers a quiconque dispose d'un navigateur web - aucune application a installer.

1. Dans **Paramètres → Partage → Connexions**, assurez-vous que **Navigateur** est active.
2. Appuyez sur **Demarrer**.
3. Sur l'ecran Partage, copiez l'adresse **Navigateur** (ou affichez son QR code).
4. Sur l'autre telephone, tablette ou ordinateur, ouvrez n'importe quel navigateur web (Safari, Chrome, Edge, Firefox) et saisissez cette adresse.
5. La page s'ouvre avec vos fichiers partages.

Dans le navigateur, l'autre personne peut :

- Basculer entre l'affichage en **liste** et en **grille** et trier par nom, date ou taille.
- Voir de vraies **miniatures** pour les photos, videos, PDF et pochettes musicales.
- Ouvrir une photo dans une **galerie** plein ecran avec balayage, zoom par pincement et diaporama.
- Ecouter la musique dans un **lecteur** integre avec file d'attente, lecture aleatoire et repetition.
- **Telecharger** n'importe quel fichier, ou telecharger un dossier entier (ou plusieurs elements selectionnes) sous forme d'un unique **Archive.zip**.
- **Televerser** des fichiers vers votre appareil - uniquement si vous avez active la **Modification des fichiers** (voir [Acces et confidentialite](/docs/guide/everdisk/everdisk-guide-access)).

## L'utiliser comme lecteur reseau (WebDAV)

Utilisez cette methode pour que votre appareil apparaisse comme un disque classique sur un Mac, un PC Windows ou une machine Linux, afin de glisser des fichiers dans les deux sens.

**Sur un Mac (Finder)**

1. Dans **Paramètres → Partage → Connexions**, assurez-vous que **Ordinateur** est active.
2. Appuyez sur **Demarrer** et notez l'adresse **Ordinateur (WebDAV)**.
3. Dans le Finder, choisissez **Aller → Se connecter au serveur** (ou appuyez sur **⌘K**).
4. Saisissez l'adresse WebDAV exactement telle qu'elle est affichee et cliquez sur **Se connecter**.
5. Saisissez l'identifiant et le mot de passe si vous en avez defini un, sinon connectez-vous en tant qu'invite.
6. Votre appareil s'ouvre comme n'importe quel autre lecteur reseau. Glissez des fichiers dans un sens ou dans l'autre.

**Sous Windows**

1. Ouvrez l'**Explorateur de fichiers**, faites un clic droit sur **Ce PC** et choisissez **Ajouter un emplacement reseau** (ou connectez un lecteur reseau).
2. Saisissez l'adresse WebDAV affichee dans Everdisk.
3. Saisissez l'identifiant et le mot de passe si vous en avez defini un.

**Sous Linux**

1. Ouvrez votre gestionnaire de fichiers et choisissez **Se connecter au serveur** (ou utilisez `davs://` / `dav://`).
2. Saisissez l'adresse WebDAV affichee dans Everdisk.

Le fait que la connexion soit en lecture seule ou bidirectionnelle depend du reglage **Modification des fichiers**. Lorsqu'il est active, vous pouvez copier des fichiers sur votre appareil et les renommer ou les supprimer ; lorsqu'il est desactive, le lecteur est en lecture seule.

## Connecter une application de fichiers (FTP)

Utilisez cette methode pour les applications de gestion et de transfert de fichiers qui parlent FTP (par exemple FileZilla ou Cyberduck sur un ordinateur).

1. Dans **Paramètres → Partage → Connexions**, assurez-vous que **Autres applications et appareils** est active.
2. Appuyez sur **Demarrer** et notez l'adresse **FTP**.
3. Dans votre application FTP, ajoutez une nouvelle connexion en utilisant cette adresse.
4. Saisissez l'identifiant et le mot de passe si vous en avez defini un, ou laissez-les vides pour un acces anonyme.

## Transferer par cable USB (Mac, sans Wi-Fi)

Utilisez cette methode lorsqu'il n'y a pas de Wi-Fi, ou lorsque vous voulez le transfert le plus rapide et le plus prive. Elle fonctionne uniquement avec un **Mac**.

1. Branchez votre iPhone ou iPad au Mac avec le cable de charge habituel.
2. Si l'appareil vous le demande, appuyez sur **Se fier a cet ordinateur**.
3. Dans Everdisk, appuyez sur **Demarrer**. Une note **Connexion rapide disponible** apparait et l'ecran Partage affiche une adresse supplementaire avec un badge **Connexion par cable** qui se termine par `.local`.
4. Sur le Mac, ouvrez le Finder → **Aller → Se connecter au serveur** (**⌘K**) et saisissez cette adresse `.local` (elle fonctionne aussi bien pour les connexions Navigateur qu'Ordinateur).
5. Votre appareil s'ouvre via le cable - plus rapide que le Wi-Fi, et les donnees ne touchent jamais le routeur ni Internet.

Remarques :

- Utilisez le **nom `.local`**, pas une adresse IP (les adresses IP ne fonctionnent qu'en Wi-Fi), et jamais `localhost`.
- La connexion par cable fonctionne **uniquement sur Mac**. Les PC Windows et les appareils Android doivent utiliser le Wi-Fi.
- Vous pouvez aussi glisser des fichiers dans le dossier Everdisk en utilisant le Finder sur un Mac, ou l'application Appareils Apple (ou iTunes) sous Windows, via le partage de fichiers iOS standard.

## Etapes suivantes

- [Acces et confidentialite](/docs/guide/everdisk/everdisk-guide-access) - ajoutez un mot de passe, autorisez les televersements, bloquez un appareil.
- [Photos, musique et video](/docs/guide/everdisk/everdisk-guide-media) - partagez toute votre bibliothèque et reglez la qualite.
- [Se connecter a des serveurs](/docs/guide/everdisk/everdisk-guide-devices) - atteignez d'autres appareils depuis Everdisk.
