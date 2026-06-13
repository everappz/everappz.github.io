---
title: "Comment récupérer gratuitement les métadonnées, icônes et captures d'écran de l'App Store"
date: 2026-06-13
description: "Guide pas à pas pour récupérer les métadonnées, l'icône, les captures d'écran et les détails localisés App Store de n'importe quelle app iOS avec AppLookup.pro, un outil de navigateur gratuit basé sur l'API officielle iTunes Search."
keywords: [
  "métadonnées app store", "récupérer données app store", "télécharger icône app store",
  "télécharger captures app store", "outil de recherche app store", "itunes search api",
  "extracteur métadonnées app", "métadonnées app iOS", "outil gratuit api app store",
  "télécharger icône app haute résolution", "recherche concurrent app store",
  "données localisées app store", "recherche app store par pays", "outil aso gratuit"
]
tags: [
  "Métadonnées App Store", "Recherche d'App", "API iTunes Search",
  "Téléchargement d'icônes d'app", "Captures d'écran d'app", "Recherche ASO"
]
sidebar:
  exclude: true
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Obtenez les données de l'App Store en quelques secondes

**Version courte :** [AppLookup.pro](https://applookup.pro) est un outil gratuit qui récupère les données publiques de toute app iOS, iPadOS, macOS ou tvOS. Vous obtenez le titre, la description, les nouveautés, la version, le prix, les notes, l'icône de l'app, les captures d'écran, les appareils pris en charge et la réponse brute de l'API iTunes. Chaque champ a un bouton de copie en un tap. Ouvrez le site, collez un lien App Store ou tapez le nom de l'app, et vous avez les données.

À utiliser pour :

- **Recherche ASO.** Voyez comment les top apps écrivent leurs titres, sous-titres, descriptions et mots-clés.
- **Suivi des concurrents.** Consultez les mises à jour de version, les notes et les prix selon les marchés.
- **Téléchargement de ressources.** Enregistrez l'icône officielle et les captures en taille réelle dans un seul ZIP.
- **Vérifications de localisation.** Comparez description, nouveautés et captures dans plus de 40 pays de l'App Store.
- **Tests d'API.** Copiez le JSON brut de l'API iTunes Search directement dans votre code ou dans Postman.

## Qu'est-ce qu'AppLookup.pro ?

[AppLookup.pro](https://applookup.pro) est un outil gratuit de recherche App Store qui fonctionne dans le navigateur. Il s'exécute entièrement sur votre appareil. Chaque résultat vient directement de l'[API officielle iTunes Search](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) d'Apple. Pas de scraping. Pas d'inscription. Pas de tracking.

### Ce que vous obtenez

- **Recherche par nom d'app ou URL App Store.** L'autocomplétion affiche des résultats en direct au fur et à mesure de votre saisie.
- **Plus de 40 boutiques par pays.** Passez entre US, UK, JP, DE, FR, BR et bien d'autres.
- **Métadonnées complètes.** Titre, sous-titre, développeur, bundle ID, version, prix, taille du fichier, notes, date de sortie, classification, langues et appareils pris en charge.
- **Ressources en haute résolution.** Icônes d'app et captures pour iPhone, iPad, macOS et Apple TV.
- **Téléchargement groupé en ZIP.** Récupérez toutes les icônes ou toutes les captures dans une seule archive.
- **JSON brut de l'API iTunes.** La réponse exacte d'Apple, prête à copier.
- **Boutons de copie sur chaque champ.** Un tap met la valeur dans votre presse-papiers.

## Comment utiliser AppLookup.pro étape par étape

### Étape 1. Entrez le nom de l'app ou collez une URL App Store

Ouvrez [applookup.pro](https://applookup.pro) et commencez à taper le nom de l'app. L'autocomplétion affiche les résultats App Store en direct pendant que vous tapez.

Vous pouvez aussi coller un lien App Store direct comme `https://apps.apple.com/us/app/instagram/id389801252` ou simplement l'ID de l'app. L'outil extrait l'ID pour vous. Il gère aussi les URLs de redirection Google.

![Saisissez un nom d'app ou une URL App Store dans AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Étape 2. Récupérez les infos de l'app et téléchargez l'icône

Cliquez sur **Lookup** ou appuyez sur Entrée. L'outil appelle l'API officielle iTunes Search et affiche l'icône de l'app, le nom du développeur, la note, la version et le prix en moins d'une seconde.

Faites défiler jusqu'à la section **App Icon**. Chaque taille d'icône qu'Apple renvoie apparaît sous forme de carte. Chaque carte a :

- **Direct Link.** Ouvre l'image en taille réelle dans un nouvel onglet.
- **Download.** Enregistre le fichier sur votre ordinateur.

Utilisez **Download All Icons (ZIP)** pour récupérer toutes les tailles d'icône dans une archive. Pareil pour les captures : chaque section de plateforme a son propre bouton **Download All (ZIP)**.

![Téléchargez les icônes et captures d'apps depuis AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Étape 3. Lisez les détails de l'app et copiez n'importe quel champ

Faites défiler jusqu'à **App Details**. Vous verrez bundle ID, version, prix, taille du fichier, OS minimum, date de sortie, date de la dernière mise à jour, classification du contenu, genres, IDs de genres, langues, vendeur, ID artiste et ID track.

Tapez le bouton **Copy** sur n'importe quelle carte. La valeur va dans votre presse-papiers et le bouton affiche une coche verte 'Copied'.

Pareil pour **Description**, **What's New** et **Supported Devices**. Ces sections sont défilables, ce qui vous permet de lire le texte complet sans perdre votre place, et le bouton Copy met tout le champ dans votre presse-papiers.

![Consultez tous les détails App Store et copiez n'importe quel champ en un tap](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Étape 4. Affichez la réponse brute de l'API App Store

Besoin du JSON exact qu'Apple renvoie ? Faites défiler jusqu'à **Raw API Response**. La charge utile complète de l'API iTunes Search est affichée dans une visionneuse défilable avec un bouton **Copy** en haut. Un tap copie tout l'objet JSON.

L'**iTunes Lookup URL** s'affiche juste au-dessus. Collez-la dans Postman, curl ou votre navigateur pour rejouer la même requête.

![Affichez et copiez la réponse JSON brute de l'API iTunes Search](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Étape 5. Changez de pays pour voir la version localisée

Les métadonnées de l'App Store changent selon le pays. La même app a souvent un titre, un sous-titre, une description, des captures et un prix différents sur chaque marché.

Choisissez un pays dans le menu déroulant en haut. L'URL dans la zone de saisie se met à jour automatiquement. Cliquez à nouveau sur **Lookup** pour récupérer l'app sur ce marché.

C'est le moyen le plus rapide de vérifier comment un concurrent présente son app au Japon, en Allemagne, au Brésil ou dans l'un des plus de 40 pays pris en charge.

![Changez de boutique pays pour voir les métadonnées App Store localisées](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Étape 6. Copiez les métadonnées localisées

Une fois le résultat du pays chargé, chaque champ fonctionne de la même façon. Tapez **Copy** sur la description, les nouveautés, le nom de l'app, le développeur, le bundle ID ou n'importe quelle carte de détail pour capturer le texte localisé.

C'est pratique pour construire des tableurs de comparaison côte à côte ou pour injecter du contenu localisé dans une revue de traduction.

![Copiez la description et les métadonnées App Store localisées en un tap](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Qui utilise AppLookup.pro

- **Développeurs indépendants** qui font de la recherche ASO avant un lancement.
- **Équipes ASO et marketing** qui suivent les mises à jour et les prix des concurrents.
- **Designers** qui récupèrent l'icône officielle haute résolution et les captures pour des kits presse et des études de cas.
- **Équipes de localisation** qui auditent les marchés couverts et identifient où le texte anglais par défaut est encore livré.
- **Ingénieurs backend et QA** qui testent des intégrations à l'API iTunes Search sans écrire de scraper.
- **Rédacteurs et blogueurs** qui ont besoin de l'icône officielle et de quelques captures pour un article.

## Confidentialité et avertissement

AppLookup.pro fonctionne dans votre navigateur. Pas de connexion. Pas de tracking. Aucun log côté serveur des apps que vous consultez. Les requêtes vont directement de votre navigateur à l'[API iTunes Search](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) d'Apple.

Cet outil est destiné **uniquement à des fins éducatives et de recherche**. Toutes les données proviennent de l'API publique officielle d'Apple et restent la propriété d'Apple Inc. et des éditeurs des apps listées. L'utilisation de l'outil est soumise aux [Conditions générales des services médias Apple](https://www.apple.com/legal/internet-services/terms/site.html). Veuillez respecter les limites de taux d'Apple et ne pas redistribuer les ressources protégées par le droit d'auteur.

## Essayez maintenant

Vous n'avez pas besoin de clé d'API, de compte développeur ni d'abonnement payant pour inspecter les données de l'App Store. Ouvrez [applookup.pro](https://applookup.pro), collez n'importe quelle URL App Store, et vous aurez les métadonnées, les icônes et le JSON brut en quelques secondes.

## Open source

AppLookup.pro est open source. Les rapports de bugs, les ajouts de pays et les pull requests sont les bienvenus.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro sur GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Foire aux questions

{{% details title="AppLookup.pro est-il vraiment gratuit ?" closed="true" %}}
Oui. AppLookup.pro est 100 pour cent gratuit et open source. Il fonctionne dans votre navigateur. Pas d'inscription, pas de palier payant et pas de plafond d'utilisation au-delà des propres limites de l'API iTunes Search d'Apple.
{{% /details %}}

{{% details title="D'où viennent les données ?" closed="true" %}}
Chaque résultat est récupéré en temps réel depuis l'[API officielle iTunes Search](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) d'Apple. L'outil ne fait pas de scraping des pages App Store et ne met aucune réponse en cache sur un serveur.
{{% /details %}}

{{% details title="Puis-je télécharger l'icône de l'app en haute résolution ?" closed="true" %}}
Oui. La section **App Icon** affiche toutes les URLs d'icône qu'Apple renvoie. Chaque carte a un Direct Link et un bouton Download, et un bouton Download All Icons ZIP les regroupe dans une seule archive.
{{% /details %}}

{{% details title="Puis-je télécharger toutes les captures App Store d'un coup ?" closed="true" %}}
Oui. Chaque section de captures (iPhone, iPad, macOS et Apple TV) a un bouton **Download All (ZIP)** qui regroupe toutes les captures en pleine résolution.
{{% /details %}}

{{% details title="Comment voir à quoi une app ressemble dans un autre pays ?" closed="true" %}}
Choisissez un pays dans le menu déroulant en haut de la page. Plus de 40 boutiques sont prises en charge. Cliquez à nouveau sur **Lookup** et l'outil récupère l'app pour ce pays, en affichant le titre, la description, les captures, les nouveautés et le prix localisés.
{{% /details %}}

{{% details title="Puis-je copier des champs individuels comme le bundle ID ou la date de sortie ?" closed="true" %}}
Oui. Chaque champ de texte dans le résultat a son propre bouton Copy : nom de l'app, développeur, description, nouveautés, bundle ID, version, prix, taille du fichier, OS minimum, date de sortie, classification, langues, appareils pris en charge et JSON brut.
{{% /details %}}

{{% details title="AppLookup.pro fonctionne-t-il pour n'importe quelle app iOS ?" closed="true" %}}
Il fonctionne pour toute app qui est listée publiquement dans au moins un pays de l'App Store et renvoyée par l'API iTunes Search. Les apps non listées, retirées ou distribuées en entreprise n'apparaîtront pas.
{{% /details %}}

{{% details title="Prend-il en charge les apps macOS et Apple TV ?" closed="true" %}}
Oui. Si l'app a des captures macOS ou Apple TV dans la réponse de l'API iTunes Search, AppLookup.pro les affiche dans leur propre panneau défilable avec des boutons de téléchargement.
{{% /details %}}

{{% details title="Puis-je utiliser le JSON brut dans mon propre code ?" closed="true" %}}
Oui. La section Raw API Response affiche le JSON exact qu'Apple renvoie. Copiez-le dans Postman, dans un test unitaire ou dans un pipeline backend. Veuillez respecter les conditions d'utilisation de l'API d'Apple et des limites de taux raisonnables.
{{% /details %}}

{{% details title="Est-il sûr de coller des URLs App Store dans l'outil ?" closed="true" %}}
Oui. L'URL est analysée dans votre navigateur. Le seul appel réseau sortant est la requête vers l'API iTunes Search d'Apple.
{{% /details %}}

{{% details title="Quelle est la différence entre AppLookup.pro et AppKeywords.pro ?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) sert à lire les métadonnées App Store de toute app publiée : recherche concurrentielle, téléchargement de ressources, vérifications de localisation. [AppKeywords.pro](https://appkeywords.pro) sert à écrire les métadonnées App Store de votre propre app : optimisation du titre, du sous-titre et des mots-clés avec prise en charge de Fastlane. Les deux outils fonctionnent très bien ensemble.
{{% /details %}}
