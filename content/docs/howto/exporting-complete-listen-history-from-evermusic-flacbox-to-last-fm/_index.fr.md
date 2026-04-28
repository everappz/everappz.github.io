---
title: "Exportez votre historique d'écoute complet d'Evermusic et Flacbox vers Last.fm"
date: 2024-01-30
description: "Apprenez à exporter votre historique musical d'Evermusic et Flacbox et à le télécharger sur Last.fm à l'aide de fichiers CSV et de l'outil Last.fm Scrubbler pour Windows."
keywords: ["evermusic", "flacbox", "lastfm", "historique musical", "scrobbling", "exporter des pistes", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "récents", "lastfm", "export", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Résumé:** Exportez votre historique d'écoute d'Evermusic ou Flacbox sous forme de fichier CSV, puis téléchargez-le sur Last.fm à l'aide de l'outil gratuit Last.fm-Scrubbler-WPF sous Windows. Le scrobbling automatique est également disponible nativement dans les deux applications.

**Mise à jour:** Le scrobbling automatique est maintenant disponible ! En savoir plus ici : [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Le scrobbling est un moyen simple d'enregistrer automatiquement des détails de base comme le titre et l'artiste de la chanson que vous écoutez dans un service en ligne. Plus tard, vous pouvez consulter votre historique d'écoute.

[Last.fm](https://www.last.fm/home), alimenté par un système de recommandation musicale appelé Audioscrobbler, propose ce service gratuitement. Il crée un profil détaillé de vos goûts musicaux en enregistrant les morceaux que vous écoutez, que ce soit depuis des stations de radio internet, votre ordinateur ou divers appareils musicaux portables. Vous pouvez visiter le site web plus tard pour recevoir des recommandations de nouveaux artistes ou albums correspondant à vos goûts musicaux.

Vous pouvez télécharger votre historique d'écoute sur [Last.fm](http://Last.fm) depuis les applications Evermusic et Flacbox à l'aide d'un outil gratuit, et nous allons vous guider dans ce processus.

Ouvrez la section 'Bibliothèque musicale' de l'application et faites défiler jusqu'à la section 'Accès rapide'. Appuyez sur l'élément de menu 'Récents'.

![écran de la bibliothèque musicale](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

Sur l'écran 'Récents', appuyez sur le bouton 'Plus' dans le coin supérieur droit pour activer le menu 'Plus d'actions'. Appuyez sur l'élément de menu 'Exporter la liste des chansons'.

![écran des récents](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

Sur l'écran 'Sélectionner le format de fichier', vous avez la possibilité de sélectionner le format du fichier de destination. Options disponibles - CSV, TXT, M3U.

![écran de sélection du format de fichier](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV : Cela signifie Valeurs Séparées par des Virgules, parfait pour organiser vos données dans un format de tableau soigné. Dans le fichier de destination, vous trouverez des paramètres comme le Nom de l'Artiste, le Nom de l'Album, le Nom du Morceau, l'Horodatage (l'heure à laquelle vous avez écouté les morceaux), le Nom de l'Artiste de l'Album et la Durée du Morceau.

TXT : Ici, nous parlons d'un fichier texte brut. C'est simple et direct, avec des paramètres incluant le Nom de l'Artiste, le Nom de l'Album, le Nom du Morceau et la Durée.

M3U : Ce format est essentiellement la référence pour la création de listes de lecture. C'est formidable car vous pouvez exporter votre liste de chansons et profiter de vos morceaux sur n'importe quel appareil, même si vous n'avez pas les fichiers originaux (à condition de sélectionner l'option URL absolue pour les fichiers multimédias). Dans le fichier de sortie, vous trouverez des paramètres tels que la Durée, le Nom de l'Artiste, le Nom du Morceau et l'Emplacement du Fichier Multimédia.

Pour notre tâche, sélectionner CSV est la bonne approche. Nous utiliserons ce fichier avec le logiciel gratuit Last.fm-Scrubbler-WPF pour télécharger notre historique d'écoute sur le service [Last.fm](http://Last.fm). Choisissez simplement CSV et appuyez sur le bouton 'Exporter'.

![écran d'exportation terminée](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Une fois l'exportation terminée, appuyez simplement sur le bouton 'Afficher le fichier', et l'application révélera le fichier créé dans votre dossier de documents. Ensuite, appuyez sur le bouton 'Plus d'actions' à côté du nom du fichier et sélectionnez l'option 'Ouvrir dans' du menu. Notre prochaine étape est de copier le fichier exporté sur votre ordinateur de bureau. Vous pouvez facilement le faire en sélectionnant l'option AirDrop du menu 'Ouvrir dans'.

![plus d'actions pour le fichier exporté](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Ensuite, nous utiliserons un client [Last.FM](http://Last.FM) gratuit open source qui n'est disponible que sur la plateforme Windows. Ce client vous permet de mettre à jour efficacement votre historique d'écoute sur [Last.FM](http://Last.FM) en utilisant le fichier CSV que nous venons d'exporter.

Si vous n'utilisez pas actuellement un ordinateur Windows, ne vous inquiétez pas. Vous pouvez accéder à ce client en installant VirtualBox sur votre Mac et en utilisant le fichier image officiel de l'environnement de développement Windows.

Voici ce que vous devez faire :

- Installez VirtualBox depuis le lien suivant : [Télécharger VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Téléchargez et installez l'environnement de développement Windows depuis ce lien : [Environnement de développement Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Sur votre ordinateur Windows (ou l'application VirtualBox avec l'image de développement Windows), téléchargez et installez [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - logiciel gratuit open source disponible sur GitHub. Nous avons testé la version 1.28 que vous pouvez télécharger ici : [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![page de téléchargement de Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

Dans la section 'Assets', appuyez sur [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) pour télécharger l'archive d'installation. Décompressez le fichier téléchargé et ouvrez le dossier décompressé.

- IMPORTANT

Cette application est encore en version bêta. Les créateurs de l'application n'ont pas fait beaucoup de tests. Ils recommandent d'essayer de scrobbler sur un compte test d'abord et de vérifier si les éléments que vous souhaitez scrobbler fonctionnent correctement. Surtout si vous scrobblez beaucoup de morceaux à la fois. Veuillez être prudent avec vos comptes.

Exécutez Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Sur l'écran principal de l'application, appuyez simplement sur 'Non connecté', situé dans le coin inférieur gauche, pour activer l'écran 'Ajouter un compte'.

![écran d'ajout de compte](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Saisissez vos identifiants de connexion.

![écran de saisie des identifiants](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Appuyez sur le bouton 'Connexion' pour ajouter votre compte.

![Appuyez sur le bouton Connexion pour ajouter votre compte.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Ouvrez l'onglet 'File Parse Scrobbler' pour commencer l'importation du fichier CSV depuis l'application Evermusic.

![Ouvrez l'onglet File Parse Scrobbler pour commencer l'importation du fichier CSV depuis l'application Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Choisissez 'Parser: CSV' et appuyez sur le bouton 'Paramètres'.

Sur l'écran suivant, vous pouvez choisir l'ordre des paramètres de votre fichier CSV.

Les champs individuels peuvent être entourés de guillemets et DOIVENT être entourés de guillemets si le champ contient l'un des délimiteurs définis. Par exemple :

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Laissez donc tous les paramètres par défaut, la seule chose que vous devez changer est d'activer la case à cocher dans le champ 'Has Fields Enclosed In Quotes'.

Appuyez sur 'Enregistrer et fermer' pour appliquer les modifications.

![choisir l'ordre des paramètres de votre fichier CSV.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Le scrobbling par analyse de fichier a deux modes. Ils peuvent être changés avec la liste déroulante 'Scrobbling Mode'.

Mode Normal : Dans ce mode, les morceaux seront scrobblés avec l'horodatage du scrobble analysé. Seuls les scrobbles de moins de 14 jours peuvent être scrobblés.

Mode Importation : Dans ce mode, les morceaux seront scrobblés avec l'horodatage calculé à partir du 'Temps de fin' et de la durée sélectionnée entre chaque morceau. Cela permet le scrobbling des morceaux même si l'horodatage du scrobble analysé est antérieur à 14 jours. Par conséquent, le premier morceau (le plus haut) dans le fichier CSV sera scrobblé avec le 'Temps de fin'.

Choisissez un fichier CSV précédemment généré depuis l'application Evermusic dans le champ 'File:' et appuyez sur 'Parse'. Dans certains cas, vous pourriez voir une alerte d'erreur indiquant que certains scrobbles n'ont pas pu être analysés. C'est normal si vous avez des morceaux sans métadonnées complètes comme le Nom de l'Artiste.

![certains scrobbles n'ont pas pu être analysés](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Appuyez sur le bouton 'Tout sélectionner' pour sélectionner tous les morceaux analysés.

![Appuyez sur le bouton Tout sélectionner pour sélectionner tous les morceaux analysés.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Appuyez sur le bouton 'Aperçu' pour vérifier toutes les modifications qui seront envoyées au serveur.

![Appuyez sur le bouton Aperçu pour vérifier toutes les modifications qui seront envoyées au serveur.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Appuyez sur le bouton 'Scrobble' pour télécharger toutes les modifications sur le serveur.

![Appuyez sur le bouton Scrobble pour télécharger toutes les modifications sur le serveur.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Auparavant, Last.fm-Scrubbler-WPF n'avait pas de limite de scrobbles par jour. Cela a changé car certaines personnes ont utilisé Scrubbler pour scrobbler tellement de morceaux que cela a causé des problèmes sur la page Last.fm. La limite de scrobbling est actuellement de 2800 scrobbles par jour. Si vous essayez de scrobbler plus, vous recevrez un message d'erreur. Il est prévu d'ajouter une 'file d'attente de scrobbling', donc si vous devez scrobbler plus de 2800 morceaux, ils seront ajoutés à une file d'attente et scrobblés automatiquement après un certain temps. Vous pouvez vérifier combien de scrobbles il vous reste dans la vue de sélection d'utilisateur.

Une fois tous les enregistrements téléchargés avec succès sur le serveur, vous verrez un message en bas de la fenêtre de l'application confirmant : 'Morceaux sélectionnés scrobblés avec succès.'

![Morceaux sélectionnés scrobblés avec succès.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Vous pouvez maintenant ouvrir votre profil sur la page [Last.fm](http://Last.fm) et vérifier toutes les modifications.

![votre profil sur la page Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Foire aux questions

{{% details title="Puis-je scrobbler automatiquement sans exporter de fichiers CSV ?" closed="true" %}}
Oui. Evermusic et Flacbox prennent désormais en charge le scrobbling automatique vers Last.fm. Consultez le guide : [Comment scrobbler vers Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Et si mon CSV contient des morceaux de plus de 14 jours ?" closed="true" %}}
Utilisez le Mode Importation dans Last.fm-Scrubbler-WPF. Il recalcule les horodatages à partir du Temps de fin, vous permettant de scrobbler des morceaux indépendamment de leur date d'origine.
{{% /details %}}

{{% details title="Je n'ai pas d'ordinateur Windows. Puis-je quand même utiliser Last.fm-Scrubbler ?" closed="true" %}}
Oui. Installez VirtualBox sur votre Mac et téléchargez l'image gratuite de l'environnement de développement Windows de Microsoft. Exécutez Last.fm-Scrubbler-WPF dans la machine virtuelle.
{{% /details %}}

{{% details title="Pourquoi certains scrobbles ne sont-ils pas analysés ?" closed="true" %}}
Les morceaux manquant de métadonnées essentielles (comme le nom de l'artiste) ne peuvent pas être analysés. C'est attendu et n'affecte pas les autres morceaux du fichier.
{{% /details %}}

{{% details title="Y a-t-il une limite quotidienne de scrobbling ?" closed="true" %}}
Oui. Last.fm-Scrubbler-WPF permet jusqu'à 2 800 scrobbles par jour. Si vous devez en scrobbler davantage, répartissez le processus sur plusieurs jours.
{{% /details %}}
