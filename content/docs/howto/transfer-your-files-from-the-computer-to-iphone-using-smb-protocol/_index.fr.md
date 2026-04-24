---
title: "Transférer des fichiers de l'ordinateur vers l'iPhone en utilisant le protocole SMB"
description: "Apprenez à transférer et accéder à de gros fichiers depuis votre Mac ou PC Windows vers votre iPhone ou iPad en utilisant Evermusic et le protocole SMB. Un guide étape par étape pour un streaming et une gestion de fichiers sans interruption."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["transférer fichiers vers iPhone SMB", "streamer musique PC sur iPhone", "connecter Mac à iPhone SMB", "configuration Evermusic SMB", "accéder aux fichiers ordinateur iPhone", "partage musique Windows iOS", "transfert fichiers SMB Evermusic"]
---

{{< author-byline >}}


**Résumé:** Utilisez Evermusic sur votre iPhone ou iPad pour accéder aux fichiers stockés sur votre Mac ou PC Windows via votre réseau local avec SMB. Pas de câbles, pas d'iTunes, pas de téléchargement cloud nécessaire. Activez le partage de fichiers sur votre ordinateur, connectez-vous dans l'application et parcourez ou lisez vos fichiers sans fil.

Avez-vous une vaste collection de gros fichiers sur votre MAC ou PC et souhaitez-vous y accéder facilement depuis votre iPhone ou iPad ? Nos applications fournissent une solution simple.

Suivez ces étapes pour activer l'accès fluide entre votre ordinateur et votre appareil iOS en utilisant le protocole SMB :

## Étape 1 : Activer le protocole SMB sur votre ordinateur

**Pour MAC :**

1. Ouvrez les "Préférences Système" sur votre MAC.
2. Cliquez sur "Partage".
3. Activez le service "Partage de fichiers".
4. Ajoutez votre dossier de musique à la section "Dossiers partagés". Ajoutez un utilisateur et choisissez le niveau d'autorisation (Lecture et écriture ou Lecture seule). Vous pouvez opter pour "Tout le monde : Lecture seule" pour le dossier de musique ajouté.

   ![Écran des paramètres Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Notez l'URL de l'ordinateur (smb://192.168.xx.xx), car vous l'utiliserez dans les prochaines étapes.
6. Cliquez sur "Options" et activez "Partager les fichiers et dossiers via SMB".

   ![Écran de partage de fichiers Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Activez le "Partage de fichiers Windows" pour les comptes disponibles.

   ![Écran de partage SMB Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Pour PC Windows :**

1. Faites un clic droit sur votre dossier de musique.
2. Sélectionnez "Propriétés".
3. Allez dans l'onglet "Partage".
4. Cliquez sur "Partager..."
5. Choisissez les personnes avec qui vous souhaitez partager le dossier et spécifiez le niveau d'autorisation. Vous pouvez sélectionner "Tout le monde : Lecture" pour le dossier de musique choisi.

   ![Écran de partage SMB Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Cliquez sur "Fait".
7. Cliquez sur "Fait" dans la fenêtre "Partage de fichiers" et notez le chemin du dossier.

   ![Dossier partagé SMB Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Étape 2 : Connecter votre appareil iOS

1. Ouvrez l'application sur votre iPhone ou iPad.
2. Allez dans l'onglet "Connexions".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Écran Connexions d'Evermusic"
  caption="Écran Connexions d'Evermusic"
  width="400"
>}}

*Si votre ordinateur apparaît dans la section "Appareils disponibles" :*

Si votre ordinateur est visible dans la section "Appareils disponibles" et que vous avez sélectionné "Tout le monde : Lecture seule" à l'étape précédente, appuyez simplement sur votre ordinateur et il se connectera automatiquement.

*Si votre ordinateur n'apparaît pas automatiquement :*

1. Appuyez sur "Se connecter à un service cloud".
2. Sélectionnez "SMB" sur l'écran "Se connecter à un service cloud".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Écran Se connecter à un service cloud d'Evermusic"
  caption="Écran Se connecter à un service cloud d'Evermusic"
  width="400"
>}}

3. Sur l'écran "Connexion SMB", entrez l'URL du serveur avec le chemin du dossier partagé. Vous pouvez utiliser le nom du serveur ou l'adresse IP du serveur :

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Entrez votre identifiant et votre mot de passe ou laissez ces champs vides si vous avez sélectionné "Tout le monde : Lecture seule" à l'étape précédente.
5. Le champ "WORKGROUP" est facultatif et doit être utilisé si vous avez un Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Écran du connecteur SMB d'Evermusic"
  caption="Écran du connecteur SMB d'Evermusic"
  width="400"
>}}

6. Une fois votre ordinateur connecté via le protocole SMB, il apparaîtra dans la section "Services cloud" de l'écran "Connexions".
7. Ouvrez le service connecté et naviguez vers le dossier souhaité.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Dossier SMB ouvert dans Evermusic"
  caption="Dossier SMB ouvert dans Evermusic"
  width="400"
>}}

8. Vous pouvez utiliser le gestionnaire de fichiers intégré pour modifier vos fichiers selon vos besoins.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Gestionnaire de fichiers Evermusic"
  caption="Gestionnaire de fichiers Evermusic"
  width="400"
>}}

## Étape 3 : Solution pour les dossiers SMB2 avec des caractères spéciaux

Parfois, vous pouvez rencontrer des problèmes avec des dossiers contenant des caractères spéciaux lors de l'utilisation du protocole SMB2. Voici quelques étapes pour résoudre ce problème :

1. **Activer SMB 1 :**  
   • Comme solution temporaire, essayez d'activer SMB 1 sur votre serveur et dans les paramètres de l'application. Cela peut aider à contourner les problèmes liés aux caractères spéciaux dans les noms de dossiers.

2. **Utiliser le menu d'ouverture de fichiers du système :**  
   • Naviguez vers "Fichiers locaux".  
   • Faites défiler jusqu'à la section "Fichiers sur cet appareil".  
   • Appuyez sur "Ouvrir des fichiers..." ou "Ouvrir des dossiers...".  
   • Localisez votre serveur et sélectionnez les fichiers ou dossiers dont vous avez besoin.  
   • Appuyez sur "Ouvrir" pour confirmer votre sélection.

3. **Protocoles alternatifs :**  
   • Si le problème persiste, envisagez de vous connecter à votre NAS en utilisant les protocoles WebDAV ou DLNA si votre NAS prend en charge ces options. Ces protocoles peuvent gérer les caractères spéciaux plus facilement.

En suivant ces étapes, vous pouvez atténuer les problèmes de caractères spéciaux dans les noms de dossiers lors de l'utilisation du protocole SMB2.

## Conclusion

Avec ces étapes, vous pouvez facilement accéder à votre vaste collection de fichiers depuis votre MAC ou PC sur votre iPhone ou iPad en utilisant nos applications.

## Questions fréquemment posées

{{% details title="Puis-je accéder aux fichiers de mon PC depuis mon iPhone sans iTunes ?" closed="true" %}}
Oui. Evermusic se connecte à votre ordinateur via SMB sur votre réseau Wi-Fi local. Aucune synchronisation iTunes ou Finder n'est nécessaire. Activez le partage de fichiers sur votre PC et connectez-vous directement depuis l'application.
{{% /details %}}

{{% details title="L'accès aux fichiers SMB fonctionne-t-il via Internet ?" closed="true" %}}
Non. SMB est un protocole de réseau local. Votre iPhone et votre ordinateur doivent être sur le même réseau Wi-Fi. Pour l'accès à distance, téléchargez les fichiers vers un service cloud comme Google Drive ou Dropbox et connectez-vous-y dans Evermusic.
{{% /details %}}

{{% details title="Quels types de fichiers puis-je accéder via SMB ?" closed="true" %}}
Evermusic prend en charge MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC et d'autres formats audio. Vous pouvez également parcourir et gérer des fichiers non audio à l'aide du gestionnaire de fichiers intégré.
{{% /details %}}

{{% details title="Puis-je transférer des fichiers d'un NAS vers mon iPhone en utilisant SMB ?" closed="true" %}}
Oui. La plupart des appareils NAS (Synology, QNAP, WD My Cloud et autres) prennent en charge SMB. Connectez-vous à votre NAS en suivant les mêmes étapes de ce guide.
{{% /details %}}

{{% details title="Dois-je copier les fichiers sur mon iPhone pour les lire ?" closed="true" %}}
Non. Evermusic diffuse les fichiers directement depuis votre ordinateur ou NAS via le réseau. Les fichiers ne sont pas copiés sur votre iPhone sauf si vous choisissez de les télécharger pour une lecture hors ligne.
{{% /details %}}

{{% details title="Le partage de fichiers SMB est-il sécurisé ?" closed="true" %}}
Le partage de fichiers SMB fonctionne uniquement sur votre réseau local. Les autres appareils sur des réseaux différents ne peuvent pas accéder à vos dossiers partagés. Pour une sécurité supplémentaire, utilisez un identifiant et un mot de passe au lieu de l'accès anonyme (Tout le monde).
{{% /details %}}
