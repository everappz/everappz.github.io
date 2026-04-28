---
title: "Comment lire votre musique depuis Mac / PC / Linux / NAS sur iPhone avec le serveur Kodi DLNA"
date: 2025-07-25
description: "Diffusez de la musique depuis votre ordinateur ou NAS vers votre iPhone via Wi-Fi en utilisant Kodi DLNA et l'application Evermusic."
keywords: ["serveur kodi dlna", "diffuser musique vers iphone", "lire musique depuis nas", "evermusic dlna", "musique mac vers iphone", "musique windows vers iphone", "kodi dlna iphone", "diffusion audio dlna"]
tags: ["dlna", "kodi", "evermusic", "iphone", "diffusion de musique", "mac", "nas", "linux", "réseau local"]
readingTime: 5
---

{{< author-byline >}}


**Résumé :** Installez Kodi sur votre Mac, PC, Linux ou NAS, activez son serveur DLNA/UPnP et diffusez toute votre bibliothèque musicale vers iPhone ou iPad avec l'application gratuite Evermusic ou Flacbox via Wi-Fi. Aucun abonnement requis.

## Introduction

Si vous avez un **Mac, PC Windows, machine Linux ou appareil NAS**, vous pouvez facilement le transformer en **serveur de musique personnel** à la maison en utilisant [Kodi](https://kodi.tv/), une plateforme multimédia gratuite et open source. Avec le serveur **DLNA/UPnP** intégré de Kodi, vous pouvez diffuser toute votre bibliothèque musicale vers n'importe quel client compatible DLNA — y compris votre iPhone ou iPad.

Dans ce guide, nous vous montrerons étape par étape comment :

- Installer Kodi sur votre Mac ou PC  
- Configurer vos dossiers de musique pour le partage  
- Activer le serveur de musique DLNA  
- Accéder à cette musique avec l'application **Evermusic** ou **Flacbox** pour iOS

Cette configuration est 100% gratuite — pas d'abonnement, juste votre propre musique diffusée sur votre réseau Wi-Fi. Que vous essayiez d'organiser votre grande collection de MP3, d'écouter du FLAC via Wi-Fi, ou simplement de profiter de votre musique locale sans synchroniser via iTunes, cette configuration est parfaite pour vous.

## Télécharger et installer Kodi sur votre Mac / PC / Linux / NAS

Visitez d'abord le site officiel de Kodi :

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Page principale de Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Cliquez sur **Téléchargements** et faites défiler pour trouver la version pour votre ordinateur.
Choisissez votre système d'exploitation. Dans cet exemple, nous utiliserons **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Page de téléchargements de Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Cliquez sur **Intel (x86/64)** si vous avez un Mac Intel ou **Apple Silicon** pour M1, M2, M3 Mac pour lancer le téléchargement.

{{< cards cols="1">}}
{{< card subtitle="Choisir l'installateur macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Veuillez patienter un instant pendant le téléchargement de l'installateur.

{{< cards cols="1">}}
{{< card subtitle="Kodi téléchargé" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Une fois téléchargé, localisez le fichier `.dmg` dans votre dossier **Téléchargements**.

{{< cards cols="1">}}
{{< card subtitle="Installer Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Double-cliquez sur le fichier téléchargé pour lancer l'installateur.
Glissez Kodi dans votre dossier **Applications** pour l'installer.

{{< cards cols="1">}}
{{< card title="" subtitle="Installez Kodi en le glissant dans Applications" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Lancez Kodi. Vous devrez peut-être l'autoriser dans **Préférences Système → Sécurité et confidentialité → Ouvrir quand même**.

{{< cards cols="1">}}
{{< card subtitle="Écran principal de Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Ajouter de la musique à la bibliothèque Kodi

Cliquez sur l'**icône d'engrenage** (Paramètres) depuis l'écran d'accueil.

{{< cards cols="1">}}
{{< card subtitle="Paramètres de Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Naviguez vers **Paramètres des médias → Bibliothèque**. Activez **Mettre à jour la bibliothèque au démarrage** pour la bibliothèque vidéo et musicale pour l'indexation automatique.

{{< cards cols="1">}}
{{< card subtitle="Paramètres de la bibliothèque" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Allez ensuite dans la section **Musique** et cliquez sur **Ajouter de la musique**.

{{< cards cols="1">}}
{{< card subtitle="Ajouter un dossier de musique" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Parcourez et sélectionnez le dossier où votre musique est stockée.

{{< cards cols="1">}}
{{< card subtitle="Choisir la source de musique" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Ajoutez la source de musique à Kodi.

{{< cards cols="1">}}
{{< card subtitle="Ajouter la source de musique" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Confirmez et laissez Kodi scanner votre bibliothèque musicale.

{{< cards cols="1">}}
{{< card subtitle="Confirmer les sources de musique" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Attendez un moment pendant que votre bibliothèque est scannée et entièrement construite.

{{< cards cols="1">}}
{{< card subtitle="Scan de la bibliothèque musicale" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Activer le serveur DLNA de Kodi

Allez dans **Paramètres → Services → UPnP/DLNA**.

Activez l'option : **Partager mes bibliothèques**.

Kodi fonctionne maintenant comme serveur DLNA sur votre réseau Wi-Fi local.

{{< cards cols="1">}}
{{< card subtitle="Activer DLNA dans Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Ouvrir la bibliothèque Kodi

Faites un clic droit pour fermer la fenêtre des paramètres et ouvrir la bibliothèque principale de Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Clic droit pour accéder à la bibliothèque Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Télécharger l'application de diffusion de musique pour iOS

Obtenez une application client DLNA gratuite pour iOS qui vous permet de diffuser de la musique depuis de nombreux services de stockage cloud et serveurs DLNA.

- Utilisez **Evermusic** si votre collection est principalement en MP3 et autres formats audio standard.
- Choisissez **Flacbox** si vous avez une bibliothèque musicale haute résolution dans des formats comme FLAC, ALAC ou DSD.

Les deux applications sont disponibles pour **iOS** et **macOS**, et sont gratuites.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Télécharger Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Télécharger Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Ajouter une source DLNA

Une fois l'application iOS téléchargée, ouvrez la section **Toutes les Connexions**.

{{< cards cols="1">}}
{{< card title="" subtitle="Barre latérale principale de l'application Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Faites défiler vers le bas et appuyez sur **Réseau local - Appareils disponibles** pour découvrir les serveurs DLNA.
Dans cette section, vous verrez tous les appareils disponibles sur votre réseau local. Votre **serveur Kodi DLNA** devrait apparaître ici. Appuyez sur le serveur Kodi pour vous connecter.

{{< cards cols="1">}}
{{< card title="" subtitle="Appareils DLNA disponibles dans Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic affichera les dossiers de la bibliothèque partagés via Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Bibliothèque musicale Kodi dans Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Naviguez vers le dossier **Chansons** pour voir tous les fichiers audio disponibles sur votre serveur DLNA.

{{< cards cols="1">}}
{{< card title="" subtitle="Chansons listées depuis le dossier distant" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Appuyez sur n'importe quel fichier audio pour commencer la diffusion instantanément.

{{< cards cols="1">}}
{{< card title="" subtitle="Fichier MP3 en lecture dans Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Retournez dans la section **Connexions**. Le serveur DLNA ajouté apparaîtra maintenant ici. Appuyez sur son icône pour vous reconnecter à tout moment. Vous pouvez également connecter d'autres services cloud depuis cet écran en suivant les mêmes étapes.

Vous pouvez également activer le **scrobbling Last.fm** ici. Les statistiques de lecture seront sauvegardées dans votre compte Last.fm, fournissant des recommandations musicales personnalisées ultérieurement.

{{< cards cols="1">}}
{{< card title="" subtitle="Connexions dans Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Construire la bibliothèque musicale

**Evermusic** et **Flacbox** vous permettent d'ajouter de la musique à votre bibliothèque et de l'organiser par **balises de métadonnées** comme les artistes, albums, genres et compositeurs.

Pour commencer, ouvrez la section **Bibliothèque musicale**. Faites défiler vers le bas jusqu'à **Outils et préférences** et appuyez sur **Ajouter de la musique**.

{{< cards cols="1">}}
{{< card title="" subtitle="Bibliothèque musicale Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Sélectionnez la source de musique — dans ce cas, choisissez **Connexions**.

{{< cards cols="1">}}
{{< card title="" subtitle="Ajouter de la nouvelle musique dans Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Trouvez le **serveur Kodi DLNA** dans les Connexions et appuyez pour voir les dossiers et fichiers.

{{< cards cols="1">}}
{{< card title="" subtitle="Choisir le serveur DLNA pour importer la musique" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Choisissez les dossiers ou fichiers que vous souhaitez ajouter et appuyez sur **Fait**.

{{< cards cols="1">}}
{{< card title="" subtitle="Sélectionner le dossier de musique à ajouter" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

L'application scannera vos fichiers sélectionnés et les organisera à l'aide des métadonnées en sections comme Artistes, Albums, Genres et Compositeurs.

{{< cards cols="1">}}
{{< card title="" subtitle="Bibliothèque musicale avec catégories" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Créer des listes de lecture

Vous pouvez également créer vos propres listes de lecture.

D'abord, ouvrez l'onglet **Listes de lecture**.

{{< cards cols="1">}}
{{< card title="" subtitle="Onglet Listes de lecture dans Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Appuyez sur le bouton **plus (+)** et choisissez **Nouvelle liste de lecture**.

{{< cards cols="1">}}
{{< card title="" subtitle="Créer une nouvelle liste de lecture" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Entrez un nom pour votre liste de lecture et appuyez sur **Enregistrer**.

{{< cards cols="1">}}
{{< card title="" subtitle="Entrer le nom de la liste de lecture" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Ensuite, choisissez une source pour ajouter des chansons — ici, nous sélectionnons la **Bibliothèque**.

{{< cards cols="1">}}
{{< card title="" subtitle="Ajouter des chansons à la nouvelle liste de lecture" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Sélectionnez les chansons souhaitées et appuyez sur **Fait** pour les ajouter.

{{< cards cols="1">}}
{{< card title="" subtitle="Ajouter de la musique de la bibliothèque à la liste de lecture" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Vos morceaux sélectionnés apparaîtront maintenant dans la liste de lecture créée.

{{< cards cols="1">}}
{{< card title="" subtitle="Liste de lecture créée affichée dans la liste" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Par défaut, les chansons sont disponibles en streaming. Pour écouter hors ligne, activez le **Mode hors ligne** — l'application téléchargera tous les morceaux de la liste de lecture.

{{< cards cols="1">}}
{{< card title="" subtitle="Mode hors ligne activé pour la liste de lecture" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Appuyez sur le bouton **Plus d'actions** pour explorer des options supplémentaires. Vous pouvez :

- Archiver la liste de lecture  
- Changer la pochette de l'album  
- Réorganiser les morceaux  
- Et d'autres fonctionnalités utiles

{{< cards cols="1">}}
{{< card title="" subtitle="Plus d'actions de liste de lecture disponibles" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Conclusion

Avec **Evermusic** et **Flacbox**, transformer votre iPhone, iPad ou Mac en un puissant lecteur de musique DLNA est facile. Que vous stockiez votre musique dans le cloud, sur un NAS ou sur un serveur multimédia domestique comme **Kodi**, ces applications vous permettent de diffuser, organiser et profiter de votre collection sans limites.

- Diffusez des MP3 ou du FLAC haute résolution directement depuis votre **serveur Kodi DLNA**  
- Construisez une bibliothèque musicale personnelle regroupée par métadonnées (albums, genres, compositeurs)  
- Créez et gérez des **listes de lecture personnalisées**  
- Activez le **mode hors ligne** pour écouter en déplacement  
- Connectez-vous à **plusieurs services cloud** et **appareils réseau locaux**  
- Suivez vos habitudes d'écoute avec l'**intégration Last.fm**

Que vous soyez audiophile ou auditeur occasionnel, Evermusic et Flacbox offrent tout ce dont vous avez besoin pour une diffusion et une organisation musicale fluides.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Télécharger Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Télécharger Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Commencez à construire votre expérience musicale personnelle dès aujourd'hui.

## FAQ

{{% details title="Kodi est-il gratuit comme serveur DLNA ?" closed="true" %}}
Oui. Kodi est entièrement gratuit et open source. Il fonctionne sur macOS, Windows, Linux et de nombreux appareils NAS.
{{% /details %}}

{{% details title="Evermusic et Flacbox supportent-ils la diffusion FLAC via DLNA ?" closed="true" %}}
Oui. Flacbox est optimisé pour les formats haute résolution comme FLAC, ALAC et DSD. Evermusic supporte également la lecture FLAC en plus de MP3 et d'autres formats standard.
{{% /details %}}

{{% details title="Puis-je écouter hors ligne après avoir diffusé depuis Kodi ?" closed="true" %}}
Oui. Activez le Mode hors ligne sur n'importe quelle liste de lecture, et l'application téléchargera tous les morceaux sur votre appareil pour une écoute sans connexion réseau.
{{% /details %}}

{{% details title="Ai-je besoin d'un abonnement premium pour utiliser DLNA ?" closed="true" %}}
La version gratuite supporte jusqu'à 3 connexions cloud ou réseau. Premium supprime cette limite et vous permet de connecter des services et serveurs DLNA illimités.
{{% /details %}}

{{% details title="Mon iPhone doit-il être sur le même réseau Wi-Fi que Kodi ?" closed="true" %}}
Oui. La diffusion DLNA fonctionne sur votre réseau local. Le serveur Kodi et votre appareil iOS doivent être connectés au même réseau Wi-Fi.
{{% /details %}}

{{% details title="Puis-je utiliser cette configuration avec un NAS au lieu d'un Mac ou PC ?" closed="true" %}}
Oui. De nombreux appareils NAS (Synology, QNAP, etc.) supportent Kodi ou disposent de leur propre serveur DLNA intégré. Evermusic et Flacbox peuvent se connecter à n'importe quel serveur DLNA/UPnP standard.
{{% /details %}}
