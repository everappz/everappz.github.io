---
title: "Comment connecter le stockage interne du Bluesound VAULT depuis Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Apprenez comment accéder au disque dur interne du Bluesound VAULT depuis Evermusic, Flacbox et Evertag en utilisant le protocole SMB pour gérer, modifier et lire des fichiers audio."
keywords: ["bluesound vault", "connecter stockage smb", "evermusic smb", "flacbox vault", "evertag smb", "stockage nas musique", "disque interne vault"]
tags: ["evermusic", "connecter", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Résumé :** Connectez-vous au stockage interne de votre Bluesound VAULT via SMB en utilisant Evermusic, Flacbox ou Evertag. Trouvez l'adresse IP du VAULT dans l'application BluOS, saisissez-la comme connexion SMB avec accès invité et commencez à lire ou gérer vos fichiers musicaux.

Le Bluesound VAULT dispose d'un disque dur interne et fonctionne comme un stockage connecté au réseau (NAS). L'accès au disque dur interne du VAULT vous permet d'ajouter/supprimer des fichiers, de modifier les balises de métadonnées depuis nos applications Evermusic, Flacbox, Evertag.

**Voici les étapes pour accéder au disque dur interne de votre VAULT :**

1. Dans l'application BluOS, sélectionnez **Aide > Diagnostics**.

2. Depuis la page **Diagnostics**, obtenez l'**Adresse IP** du VAULT. Cette **Adresse IP** sera utilisée dans les étapes suivantes.

3. Ouvrez Evermusic, Flacbox ou Evertag.

   ![Applications Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Ouvrez l'écran "Connexions" et sélectionnez l'élément de menu "Connecter un service cloud".

   ![Écran Connexions d'Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Sélectionnez le service cloud "SMB".

   ![Écran Connecter un Service Cloud d'Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Sur l'"écran de configuration SMB", saisissez l'URL dans le format suivant :

   ```
   SMB://<<VAULT-IP>>
   ```

   Remplacez `<<VAULT-IP>>` par l'**Adresse IP** obtenue à l'étape 2.

   **Remarque :** Laissez les champs Identifiant et Mot de passe vides car le stockage VAULT prend en charge le mode INVITÉ.

   ![Écran de connexion SMB d'Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Appuyez sur le bouton "Se connecter" pour enregistrer la configuration.

8. Ouvrez le stockage cloud connecté, naviguez dans le dossier contenant les fichiers audio et appuyez sur n'importe quel fichier pour démarrer le lecteur audio.

   ![Écran du serveur SMB ouvert d'Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Vous pouvez également modifier des fichiers à l'aide du gestionnaire de fichiers intégré.

   ![Écran du Gestionnaire de Fichiers d'Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Grâce à ces étapes simples, vous pouvez facilement accéder au disque dur interne de votre Bluesound VAULT et prendre le contrôle de votre bibliothèque musicale en utilisant Evermusic, Flacbox ou Evertag.

## FAQ

{{% details title="Ai-je besoin d'un nom d'utilisateur et d'un mot de passe pour me connecter au Bluesound VAULT ?" closed="true" %}}
Non. Le Bluesound VAULT prend en charge l'accès invité (anonyme) via SMB. Laissez les champs Identifiant et Mot de passe vides lors de la configuration de la connexion.
{{% /details %}}

{{% details title="Puis-je modifier les balises musicales sur le Bluesound VAULT ?" closed="true" %}}
Oui. En utilisant Evertag, vous pouvez modifier les balises de métadonnées (titre, artiste, album, etc.) des fichiers audio stockés directement sur le disque dur interne du VAULT.
{{% /details %}}

{{% details title="Quels protocoles le Bluesound VAULT prend-il en charge ?" closed="true" %}}
Le Bluesound VAULT expose son stockage interne via SMB (Server Message Block). Evermusic, Flacbox et Evertag prennent tous en charge les connexions SMB, ce qui rend la connexion simple.
{{% /details %}}

{{% details title="Puis-je diffuser de la musique depuis le VAULT sans copier de fichiers sur mon iPhone ?" closed="true" %}}
Oui. Une fois connecté via SMB, vous pouvez diffuser des fichiers audio directement depuis le disque interne du VAULT sans les copier sur votre appareil.
{{% /details %}}
