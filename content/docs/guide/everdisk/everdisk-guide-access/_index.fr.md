---
title: "Acces et confidentialite"
date: 2026-08-20
description: "Gardez votre partage Everdisk en securite : protegez l'acces avec un identifiant et un mot de passe, chiffrez la connexion SMB avec SMB3 (AES), controlez si les appareils connectes peuvent televerser, renommer et supprimer grace a la Modification des fichiers, bloquez les appareils inconnus, choisissez entre corbeille et suppression definitive, et comprenez pourquoi tout reste sur votre reseau local."
keywords: ["protection par mot de passe Everdisk", "chiffrement SMB", "chiffrement SMB3 AES", "bouton modification des fichiers", "bloquer un appareil", "appareils bloques", "supprimer definitivement des fichiers", "reseau local uniquement", "partage de fichiers prive", "DLNA sans mot de passe", "securite reseau"]
tags: ["everdisk", "guide", "access", "privacy", "security"]
readingTime: 8
---


Everdisk garde vos fichiers sur votre propre reseau et vous donne des controles simples sur qui peut y acceder et ce qu'ils peuvent faire. Vous trouvez ces controles dans **Paramètres → Partage → Acces**, ainsi que quelques reglages connexes dans le Gestionnaire de fichiers.

## Proteger l'acces avec un identifiant et un mot de passe

Par defaut, toute personne du meme reseau disposant de votre adresse peut ouvrir vos fichiers partages. Pour exiger une connexion :

1. Allez dans **Paramètres → Partage → Acces**.
2. Saisissez un **Identifiant** et un **Mot de passe**.
3. Desormais, les connexions **Navigateur (HTTP)**, **Ordinateur (WebDAV)**, **Ordinateur (avance) (SMB)** et **Autres applications et appareils (FTP)** demandent toutes ces informations avant d'afficher vos fichiers.

Laissez les deux champs vides pour un acces ouvert. Votre mot de passe est stocke de maniere securisee dans le Trousseau de l'appareil.

> **Le DLNA est toujours ouvert.** La connexion TV et centre multimedia (DLNA) ne peut pas etre protegee par mot de passe : une fois activee, tout appareil sur le meme Wi-Fi peut parcourir vos medias partages. Desactivez-la si vous ne voulez que des connexions protegees, et ne partagez que sur des reseaux de confiance.

## Chiffrer la connexion SMB (SMB3 / AES)

Un identifiant et un mot de passe controlent **qui** peut se connecter, mais les donnees elles-memes circulent encore en clair sur la plupart des connexions. **SMB est la seule connexion qu'Everdisk peut chiffrer**, ce qui brouille chaque transfert pour que personne d'autre sur le meme reseau ne puisse le lire.

Pour l'activer :

1. Definissez un **Identifiant** et un **Mot de passe** comme ci-dessus - les connexions chiffrees ne peuvent pas etre anonymes.
2. Allez dans **Paramètres → Partage** et activez **Exiger le chiffrement SMB**.
3. **Arretez et redemarrez** le partage pour que la modification prenne effet.

Chaque transfert SMB est alors protege par le **chiffrement SMB3 (AES)**. L'appareil qui se connecte doit prendre en charge SMB3 - le Finder sur un Mac recent, ou **Windows 10 et versions ulterieures**. C'est un excellent choix sur un Wi-Fi auquel vous ne faites pas totalement confiance. Le chiffrement SMB est une fonction Premium.

## Autoriser ou bloquer la modification (Modification des fichiers)

Le bouton **Modification des fichiers** determine si les appareils connectes peuvent seulement consulter vos fichiers, ou aussi les modifier.

- **Active** (par defaut) : les appareils connectes peuvent **televerser, renommer et supprimer** vos fichiers partages - votre appareil fonctionne alors comme un vrai lecteur reseau bidirectionnel.
- **Desactive** : vos fichiers partages sont en **lecture seule**. Les autres peuvent consulter et telecharger, mais ne peuvent rien ajouter ni modifier.

L'activer affiche un bref avertissement, car cela permet a d'autres personnes de modifier vos fichiers. Il porte un badge **Important** tant qu'il est active.

## Bloquer un appareil

Si vous voyez un appareil que vous ne reconnaissez pas :

1. Sur l'ecran Partage, reperez-le sous **Qui est connecte**.
2. Appuyez sur son bouton d'actions supplementaires et choisissez **Bloquer cet appareil**.

Les appareils bloques sont listes dans **Paramètres → Partage → Acces → Appareils bloques**, ou vous pouvez en **debloquer** un ou **Tout debloquer**. Le blocage suit l'appareil meme si son adresse reseau change (pour les connexions Navigateur, Ordinateur et TV).

## Corbeille ou suppression definitive

Lorsqu'un fichier est supprime - par vous dans le gestionnaire de fichiers, ou par un appareil connecte - il va normalement dans une **corbeille** recuperable pour que vous puissiez le recuperer.

Si vous preferez que les fichiers soient supprimes immediatement sans recuperation possible, activez **Supprimer definitivement les fichiers** dans **Paramètres → Gestionnaire de fichiers → Suppression des fichiers**. C'est desactive par defaut. **Cela concerne le gestionnaire de fichiers de l'appareil** et **les suppressions effectuees sur le reseau** ; cela ne change pas la facon dont la photothèque ou la bibliothèque musicale du systeme gèrent la suppression.

## Tout reste local

Everdisk ne partage que sur votre **reseau local** - rien n'est televerse sur Internet et il n'y a pas de compte cloud entre les deux. Quelques points a connaitre :

- Everdisk a besoin de l'autorisation iOS **Reseau local** pour que les appareils a proximite puissent le trouver. Si cette autorisation est desactivee, une note explique comment la reactiver dans l'application Reglages d'iOS.
- Pour une confidentialite maximale, ne partagez que lorsque vous etes sur un reseau Wi-Fi **domestique ou prive** de confiance, et soyez prudent sur les Wi-Fi publics. Un identifiant et un mot de passe aident, mais ne remplacent pas un reseau de confiance.
- L'**option la plus privee de toutes est un cable USB vers un Mac** - les donnees passent directement par le cable et ne touchent jamais le routeur ni Internet. Voir [Connecter vos appareils](/docs/guide/everdisk/everdisk-guide-connect).

## Etapes suivantes

- [Partage](/docs/guide/everdisk/everdisk-guide-sharing) - choisissez ce que vous partagez et lancez le partage.
- [Paramètres](/docs/guide/everdisk/everdisk-guide-settings) - tous les reglages Acces et Gestionnaire de fichiers au meme endroit.
