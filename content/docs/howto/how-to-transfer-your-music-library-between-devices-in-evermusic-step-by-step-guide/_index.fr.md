---
title: "Comment transférer votre bibliothèque musicale entre appareils dans Evermusic : guide étape par étape"
description: "Transférez facilement votre bibliothèque musicale Evermusic, listes de lecture, pochettes d'albums et paramètres d'un iPhone, iPad ou Mac à un autre en utilisant Wi-Fi Drive et les outils de sauvegarde."
date: 2024-12-29
tags: ["bibliothèque musicale", "transfert", "wifi", "sauvegarde", "webdav", "restauration"]
keywords: ["transférer bibliothèque musicale Evermusic", "sauvegarde et restauration listes de lecture Evermusic", "Evermusic WiFi Drive", "synchroniser Evermusic entre appareils", "déplacer base de données Evermusic", "transfert de fichiers Evermusic", "restaurer paramètres lecteur audio", "transfert musique WebDAV iOS"]
readingTime: 3
---

{{< author-byline >}}


**En bref :** Pour transférer votre bibliothèque Evermusic vers un nouvel appareil, créez une sauvegarde sur l'appareil source, démarrez Wi-Fi Drive, connectez le deuxième appareil via le même réseau, téléchargez la sauvegarde et les fichiers musicaux, puis restaurez à partir de la sauvegarde. L'ensemble du processus prend environ 10 minutes selon la taille de la bibliothèque.

Dans ce guide, nous vous accompagnerons dans le transfert de toute votre bibliothèque musicale — y compris la base de données, les pochettes d'albums et les paramètres — d'un appareil (iPhone ou Mac) à un autre. Bien que la synchronisation automatique de la bibliothèque musicale et des listes de lecture soit une fonctionnalité prévue pour l'avenir, ce processus doit actuellement être effectué manuellement.

## Étape 1 : Créer une sauvegarde sur le premier appareil

1. **Ouvrez l'application sur votre premier appareil** (celui avec votre bibliothèque musicale, listes de lecture et services cloud connectés).
2. **Accédez aux Paramètres** et sélectionnez l'option **Sauvegarde et restauration**.

![Sauvegarde et restauration](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. Sur l'écran **Sauvegarde et restauration**, choisissez les éléments à inclure dans votre fichier de sauvegarde :
   - **Base de données** (comprend votre bibliothèque musicale et listes de lecture)
   - **Pochettes d'albums**
   - **Paramètres**

Ces options sont activées par défaut.

![Options de sauvegarde](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Appuyez sur **Sauvegarder les données de l'application** pour commencer le processus.

![Sauvegarder les données de l'application](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Une fois la sauvegarde terminée, une alerte d'information apparaîtra.

![Sauvegarde terminée](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Appuyez sur **Afficher le fichier** pour révéler le fichier de sauvegarde dans le répertoire **Documents**. Les fichiers de sauvegarde sont généralement enregistrés dans le dossier **Backup**.

![Afficher le fichier de sauvegarde](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Étape 2 : Démarrer le serveur Wi-Fi Drive

1. Allez dans la section **Connexions** de l'application.
2. Faites défiler vers le bas jusqu'à **Se connecter via Wi-Fi** et appuyez dessus.

![Se connecter via Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. Sur l'écran suivant, appuyez sur **Démarrer Wi-Fi Drive**.

- Optionnellement, vous pouvez définir un identifiant et un mot de passe pour la sécurité, mais ce n'est pas nécessaire pour les réseaux domestiques.

4. Une fois démarré, vous verrez les adresses de serveur disponibles. Cela peut être utilisé pour les navigateurs de bureau ou les applications WebDAV, mais dans ce guide, nous passerons directement aux étapes suivantes.

![Wi-Fi Drive démarré](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Étape 3 : Connecter votre deuxième appareil au premier

1. Ouvrez l'application sur votre deuxième appareil (où vous souhaitez transférer la bibliothèque).
2. Assurez-vous que les deux appareils sont connectés au même réseau Wi-Fi.
3. Sur le deuxième appareil, ouvrez l'onglet **Connexions** et sélectionnez **Appareils disponibles**.

![Appareils disponibles](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Vous devriez voir une connexion WebDAV nommée **Evermusic** (le serveur que nous avons démarré sur le premier appareil). Appuyez dessus pour vous connecter.

5. Une fois connecté, vous verrez tous les dossiers du premier appareil.

![Connecté au premier appareil](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Étape 4 : Préparer les transferts de fichiers

1. Sur le deuxième appareil, allez dans **Paramètres > Gestionnaire de fichiers** et activez **Enregistrer les fichiers téléchargés dans - Demander à chaque fois**.

- Cela garantit que vous pouvez sélectionner le dossier de destination pour chaque téléchargement.

2. Retournez à l'onglet **Connexions** et naviguez vers le serveur WebDAV connecté.

![Préparer les transferts de fichiers](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Étape 5 : Transférer la sauvegarde et les fichiers musicaux

1. Ouvrez le dossier **Backup** sur le serveur WebDAV connecté.

![Dossier de sauvegarde](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Appuyez sur le bouton **Plus d'actions** (trois points) à côté du fichier de sauvegarde et sélectionnez **Télécharger**.

3. Créez un dossier **Backup** sur le deuxième appareil pour stocker les fichiers téléchargés. Confirmez votre sélection en appuyant sur **Fait**.

![Télécharger la sauvegarde](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Transférez tout fichier musical supplémentaire :
   - Vérifiez le dossier **Téléchargements** ou d'autres dossiers pertinents sur le serveur WebDAV.

![Transférer les fichiers musicaux](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Utilisez l'option **Sélectionner** pour choisir des fichiers, puis appuyez sur **Plus d'actions > Télécharger**. Enregistrez-les dans le dossier correspondant sur le deuxième appareil pour maintenir la même structure de répertoires.

L'objectif est de transférer tous les fichiers de votre premier appareil vers votre appareil actuel, en veillant à ce que la structure des dossiers reste identique. De cette façon, les liens dans votre bibliothèque musicale et vos listes de lecture restent intacts. Notez que les fichiers locaux stockés en dehors du répertoire Documents de l'application sur votre premier appareil doivent être transférés séparément. Comme l'application ne peut pas accéder à ces fichiers en mode Wi-Fi Drive, vous devrez utiliser l'application Fichiers du système pour leur transfert.

![Transfert terminé](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Étape 6 : Surveiller la progression du transfert

1. Sur le deuxième appareil, allez dans la section **Fichiers locaux** (ou l'onglet **Téléchargements** sur iPad/Mac).

2. Appuyez sur le bouton **Activité de transfert** dans le coin supérieur gauche pour surveiller la file d'attente de transfert.

![Surveiller le transfert](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Étape 7 : Restaurer les données à partir de la sauvegarde

1. Une fois le fichier de sauvegarde et tous les fichiers audio nécessaires téléchargés sur le deuxième appareil, ouvrez le dossier **Backup**.

2. Appuyez sur le fichier de sauvegarde, et un message de confirmation apparaîtra.

![Restaurer la sauvegarde](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Remarque :** La restauration remplacera toutes les données actuelles de la bibliothèque musicale, les listes de lecture, les paramètres et les pochettes d'albums par les données de la sauvegarde.

3. Appuyez sur **Restaurer** pour commencer le processus.

![Processus de restauration](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Une fois la restauration terminée, une alerte confirmera le succès.

![Restauration terminée](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Vérifiez les sections **Listes de lecture** ou **Bibliothèque musicale** pour confirmer la restauration.

![Vérifier la restauration](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Étape 8 : Réindexer la bibliothèque musicale

1. Pour de meilleurs résultats, réindexez votre bibliothèque pour vous assurer que tous les fichiers sont détectés avec succès.

2. Allez dans **Paramètres > Bibliothèque musicale > Synchronisation de musique hors ligne** et sélectionnez **Démarrer l'analyse des dossiers locaux**.

En suivant ces étapes, vous transférerez avec succès votre bibliothèque musicale, vos listes de lecture et vos paramètres vers un autre appareil. Si vous rencontrez des problèmes, n'hésitez pas à contacter le support.

## Questions fréquemment posées

{{% details title="Puis-je transférer ma bibliothèque Evermusic sans Wi-Fi ?" closed="true" %}}
Wi-Fi Drive nécessite que les deux appareils soient sur le même réseau Wi-Fi. Il n'existe actuellement aucune option de transfert par Bluetooth ou réseau cellulaire. Vous pouvez alternativement utiliser AirDrop ou l'application Fichiers pour déplacer manuellement le fichier de sauvegarde et les dossiers musicaux entre les appareils.
{{% /details %}}

{{% details title="Les connexions aux services cloud seront-elles transférées avec la sauvegarde ?" closed="true" %}}
La sauvegarde comprend votre base de données, listes de lecture, pochettes d'albums et paramètres. Les identifiants de connexion aux services cloud ne sont pas inclus pour des raisons de sécurité. Vous devrez reconnecter vos comptes cloud sur le nouvel appareil après la restauration.
{{% /details %}}

{{% details title="Qu'arrive-t-il à ma bibliothèque existante sur le deuxième appareil ?" closed="true" %}}
La restauration d'une sauvegarde remplace toutes les données existantes de la bibliothèque musicale, les listes de lecture, les paramètres et les pochettes d'albums sur le deuxième appareil. Faites une sauvegarde séparée du deuxième appareil d'abord si vous souhaitez conserver ses données.
{{% /details %}}

{{% details title="Ce processus fonctionne-t-il entre iPhone et Mac ?" closed="true" %}}
Oui. Evermusic prend en charge le transfert Wi-Fi Drive entre toute combinaison d'iPhone, iPad et Mac. Les deux appareils doivent simplement être sur le même réseau Wi-Fi.
{{% /details %}}

{{% details title="Combien de temps dure le transfert ?" closed="true" %}}
Le temps de transfert dépend de la taille de votre bibliothèque musicale et de votre vitesse Wi-Fi. Une bibliothèque typique de quelques gigaoctets se transfère en 5 à 15 minutes via un réseau domestique standard.
{{% /details %}}
