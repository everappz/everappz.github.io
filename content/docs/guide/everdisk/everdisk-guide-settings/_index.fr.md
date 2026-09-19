---
title: "Paramètres"
date: 2026-08-20
description: "Un tour complet des paramètres d'Everdisk : profil de l'appareil (nom et avatar), les cinq serveurs de connexion, les controles d'acces, le chiffrement SMB (SMB3/AES), la qualite photo et video, les ports personnalises, les miniatures DLNA, les options de reseau et de transfert, les options du gestionnaire de fichiers, et Premium."
keywords: ["paramètres Everdisk", "nom avatar de l'appareil", "serveurs de connexion", "qualite photo video", "ports personnalises HTTP WebDAV FTP", "miniatures DLNA", "transferts parallèles", "supprimer definitivement des fichiers", "cache des miniatures", "Everdisk Premium"]
tags: ["everdisk", "guide", "settings"]
readingTime: 12
---


L'onglet **Paramètres** regroupe tout en trois grandes zones - **Partage**, **Reseau** et **Gestionnaire de fichiers** - plus Premium, les commentaires et les liens legaux. Cette page explique chaque reglage et sa valeur par defaut.

## Premium

En haut des Paramètres, vous voyez votre statut Premium, ou un bouton **Debloquer toutes les fonctionnalites**. Everdisk est gratuit avec quelques limites ; un achat unique **Premium a vie** les supprime. Voir [Premium](#premium-lifetime) a la fin de cette page.

## Paramètres de partage

### Général

- **Demarrer le partage de l'appareil automatiquement** - lance le partage des l'ouverture de l'application. *(Premium.)*
- **Partager le dossier Documents** - partage le dossier Documents de l'application. Active par defaut.
- **Prevenir avant la deconnexion** - vous rappelle de rouvrir l'application avant que le systeme ne la suspende en arriere-plan. Desactive par defaut ; demande l'autorisation de notification la première fois.

### Profil de l'appareil

- **Nom de l'appareil** - le nom que les autres appareils voient pour vous sur le reseau. Appuyez pour le modifier. *(Premium.)*
- **Avatar de l'appareil** - l'icone et la couleur de fond de votre appareil. Vous pouvez choisir une icone, un degrade de fond, ou **choisir un avatar depuis Photos**. *(Premium.)*
- **Regenerer le nom et l'avatar** et **Regenerer l'avatar** - obtenez un nouveau nom et/ou avatar aleatoire. *(Gratuit.)*

### Acces

- **Identifiant** et **Mot de passe** - exigez une connexion pour les connexions Navigateur, Ordinateur et Autres applications.
- **Modification des fichiers** - laissez les appareils connectes televerser, renommer et supprimer. Active par defaut.
- **Appareils bloques** - gerez les appareils que vous avez bloques.

Voir [Acces et confidentialite](/docs/guide/everdisk/everdisk-guide-access) pour plus de details.

### Connexions

Activez ou desactivez chaque serveur. Les cinq sont actives par defaut, et chacun dispose d'un bouton infos (ⓘ) avec des instructions de connexion :

- **TV et centre multimedia** (DLNA)
- **Navigateur** (HTTP)
- **Ordinateur** (WebDAV)
- **Ordinateur (avance)** (SMB) - un lecteur reseau pour Mac, Windows et Linux ; sur un Mac il apparait tout seul dans la barre laterale du Finder. La seule connexion qui peut etre chiffree.
- **Autres applications et appareils** (FTP)

### Photos

- **Format** - Original ou Le plus compatible (JPEG).
- **Qualite** - Original, Elevee, Moyenne ou Basse.

Tout autre choix qu'Original convertit les photos au moment du partage, ce qui est plus lent. La conversion est une fonctionnalite Premium.

### Videos

- **Format** - Original ou Le plus compatible (H.264 MP4).
- **Qualite** - Original, Elevee, Moyenne ou Basse.

Meme principe que pour les Photos : Original est le plus rapide, et la conversion est Premium. Baissez la qualite si une TV ancienne ne parvient pas a lire une video.

### Avancé

- **Port HTTP** (par defaut 80), **Port WebDAV** (par defaut 8080), **Port SMB** (par defaut 4455), **Port FTP** (par defaut 2121). Le DLNA choisit son port automatiquement. *(La modification des ports est Premium ; les utilisateurs gratuits peuvent voir les valeurs.)*

### Chiffrement SMB

- **Exiger le chiffrement SMB** - chiffre chaque transfert SMB avec le **chiffrement SMB3 (AES)** pour que personne d'autre sur le reseau ne puisse lire vos fichiers. Desactive par defaut. Cela necessite un **identifiant et un mot de passe** definis ci-dessus (les connexions chiffrees ne peuvent pas etre anonymes) et un client qui prend en charge SMB3, comme le Finder sur un Mac recent ou Windows 10 et versions ulterieures. Les modifications prennent effet au prochain demarrage du partage. *(Premium.)*

### Miniatures DLNA

- **Afficher les miniatures** - publie des images d'apercu pour les TV. Active par defaut (gratuit).
- Choisissez les tailles a publier : **Petite (160px)**, **Moyenne (640px)**, **Grande (1024px)**, **Très grande (4096px)**.

## Paramètres reseau

- **Transferts de fichiers** - utilisez le **Wi-Fi** uniquement, ou le **Wi-Fi et les donnees cellulaires**, pour les telechargements et televersements. Par defaut Wi-Fi.
- **Limite de transferts parallèles** - combien de transferts s'executent en meme temps. Par defaut 5.
- **Transferts en arriere-plan** - maintient les transferts en cours pendant que vous utilisez d'autres ecrans. Active par defaut.
- **Miniatures des fichiers** - indique s'il faut recuperer les miniatures des fichiers sur les autres appareils en Wi-Fi uniquement ou aussi en cellulaire. Par defaut Wi-Fi.

## Paramètres du gestionnaire de fichiers

- **Supprimer definitivement les fichiers** - supprime immediatement, sans corbeille. Desactive par defaut. Voir [Acces et confidentialite](/docs/guide/everdisk/everdisk-guide-access).
- **Reinitialiser tous les messages d'information** - fait revenir les bannières de conseils que vous avez fermees.
- **Cache des miniatures** - voyez l'espace occupe par les miniatures en cache, et **Vider le cache des miniatures**.

## Commentaires et mentions legales

En bas, vous pouvez **Noter cette application**, **Envoyer un commentaire**, **Obtenir plus d'applications**, et ouvrir les **Conditions generales** et la **Politique de confidentialite**.

## Premium Lifetime

Everdisk est gratuit. Un unique achat **Premium a vie** - un paiement unique, pas un abonnement - debloque :

- **Dossiers illimites** - partagez plus de 5 dossiers.
- **Connexions illimitees** - enregistrez plus de 10 serveurs dans l'onglet Appareils.
- **Conversion photo et video** - partagez dans n'importe quelle qualite autre qu'Original.
- **Chiffrement SMB** - protegez les transferts SMB avec le chiffrement SMB3 (AES).
- **Ports personnalises** - definissez vos propres ports HTTP, WebDAV, SMB et FTP.
- **Demarrage automatique du partage** - lancez le partage automatiquement a l'ouverture de l'application.
- **Personnalisation de l'appareil** - un nom d'appareil, une icone d'avatar, un degrade de fond ou un avatar photo personnalises.

Premium est lie a votre Apple ID. Utilisez **Restaurer les achats** pour le debloquer sur vos autres appareils connectes avec le meme Apple ID.

## Etapes suivantes

- [Partage](/docs/guide/everdisk/everdisk-guide-sharing) - l'ecran Partage en detail.
- [Acces et confidentialite](/docs/guide/everdisk/everdisk-guide-access) - mots de passe, modification et blocage.
- [FAQ](/docs/faq/everdisk) - des reponses rapides aux questions frequentes.
