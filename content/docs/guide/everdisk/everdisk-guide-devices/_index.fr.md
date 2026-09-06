---
title: "Se connecter a des serveurs"
date: 2026-08-20
description: "Utilisez l'onglet Appareils d'Everdisk pour vous connecter a d'autres serveurs de votre reseau. Ajoutez et parcourez des serveurs DLNA, WebDAV, FTP et SFTP et des NAS, diffusez de l'audio et de la video, telechargez des fichiers, et creez, televersez, renommez, deplacez ou supprimez sur les serveurs qui l'autorisent."
keywords: ["onglet Appareils Everdisk", "se connecter a un NAS", "client DLNA iPhone", "client WebDAV iPhone", "client FTP iPhone", "client SFTP iPhone", "parcourir un serveur reseau", "diffuser depuis un NAS", "telecharger depuis un serveur", "connexion cloud WebDAV"]
tags: ["everdisk", "guide", "devices", "connections"]
readingTime: 9
---


Everdisk n'est pas seulement un disque sans fil - c'est aussi un client pour les autres appareils de votre reseau. L'onglet **Appareils** vous permet de vous connecter a des serveurs **DLNA**, **WebDAV**, **FTP** et **SFTP**, y compris des NAS et des serveurs multimedias, puis de parcourir, diffuser et telecharger leurs fichiers.

## L'ecran Appareils

L'onglet Appareils comporte deux parties :

- **Connexions** - les serveurs que vous avez deja enregistres.
- **Appareils disponibles** - les serveurs qu'Everdisk detecte automatiquement sur votre reseau local.

Pour vous connecter a un serveur qu'Everdisk a deja trouve, il suffit d'appuyer dessus dans **Appareils disponibles**. Pour ajouter un serveur manuellement, appuyez sur le bouton **plus (+)** ou sur **Nouvelle connexion**.

## Ajouter une nouvelle connexion

Appuyez sur **Nouvelle connexion** et choisissez le type de serveur que vous voulez atteindre :

- **DLNA / UPnP** - ideal pour les serveurs multimedias. Diffusez video, musique et photos depuis des mediathèques, des unites de stockage reseau et des TV et ordinateurs compatibles DLNA. Le DLNA est en lecture seule : vous pouvez parcourir, diffuser et telecharger, mais vous ne pouvez pas televerser ni modifier de fichiers.
- **WebDAV** - connectez-vous a des serveurs de fichiers, des unites de stockage reseau et des lecteurs cloud qui prennent en charge WebDAV. Lecture et ecriture lorsque le serveur l'autorise.
- **FTP** - courant sur les routeurs, les unites de stockage reseau et l'hebergement web. Le port par defaut est 21 (990 pour le FTPS securise) ; vous pouvez definir un port personnalise dans l'adresse, par exemple `ftp://host:2121`. Laissez l'identifiant et le mot de passe vides pour un acces anonyme.
- **SFTP** - connectez-vous de maniere securisee via SSH. Le port par defaut est 22 ; utilisez un port personnalise dans l'adresse si besoin, par exemple `sftp://host:2222`.

> Everdisk se connecte uniquement a ces protocoles reseau local et directement adressables. Il ne se connecte pas a des comptes cloud comme Google Drive ou Dropbox. Un lecteur cloud n'est accessible que si ce service propose une adresse **WebDAV** que vous pouvez saisir.

## Saisir l'adresse et se connecter

Dans l'editeur de connexion, renseignez :

- **Titre** - un nom convivial pour la connexion.
- **URL / adresse** - l'adresse du serveur (des exemples sont affiches pour chaque type).
- **Identifiant** et **Mot de passe** - laissez les deux vides si le serveur autorise l'acces anonyme.

Pour le WebDAV, vous pouvez autoriser les certificats non valides si votre serveur en utilise un auto-signe. Si l'identite d'un serveur securise ne peut pas etre verifiee, Everdisk vous demande de confirmer avant de lui faire confiance.

Les utilisateurs gratuits peuvent enregistrer jusqu'a **10** connexions. Premium supprime cette limite.

## Parcourir, diffuser et telecharger

Une fois connecte, appuyez sur le serveur pour l'ouvrir :

- **Parcourez** les dossiers en liste ou en grille, triez-les et voyez les miniatures. Les serveurs DLNA affichent aussi les details musicaux et les pochettes.
- **Diffusez** de l'audio et de la video. L'audio rejoint la file d'attente du mini-lecteur ; la video se lit en plein ecran. La navigation dans le fichier fonctionne pendant la diffusion.
- **Telechargez** des fichiers sur votre appareil. Selectionnez-en plusieurs a la fois pour un telechargement groupe. Les telechargements apparaissent dans **Transferts de fichiers** et arrivent dans votre dossier **Documents**.
- Les **Infos** de n'importe quel element affichent son type, sa taille, sa date, son chemin et ses details multimedias.

## Modifier des fichiers sur un serveur

Sur les serveurs qui autorisent l'ecriture - **WebDAV, FTP et SFTP** - vous pouvez aussi gerer les fichiers :

- **Nouveau dossier**
- **Televerser des fichiers** depuis votre appareil
- **Renommer**, **Deplacer** et **Supprimer** (un element ou plusieurs a la fois)

Les serveurs **DLNA** sont en lecture seule : ces actions n'y sont donc pas disponibles.

## Suivre vos transferts

Les telechargements et les televersements s'executent en arriere-plan et apparaissent dans **Transferts de fichiers**, que vous ouvrez depuis le coin superieur gauche de l'onglet **Documents**. Vous pouvez y suivre la progression, et mettre en pause, reprendre, relancer, annuler ou effacer les taches. Vous pouvez aussi ajuster les transferts dans [Paramètres → Reseau](/docs/guide/everdisk/everdisk-guide-settings) (Wi-Fi uniquement ou Wi-Fi et donnees cellulaires, combien s'executent en meme temps, et s'ils continuent en arriere-plan).

## Etapes suivantes

- [Fichiers et documents](/docs/guide/everdisk/everdisk-guide-files) - gerez tout ce que vous telechargez.
- [Photos, musique et video](/docs/guide/everdisk/everdisk-guide-media) - lisez ce que vous diffusez.
- [Paramètres](/docs/guide/everdisk/everdisk-guide-settings) - limites de connexion et options de transfert.
