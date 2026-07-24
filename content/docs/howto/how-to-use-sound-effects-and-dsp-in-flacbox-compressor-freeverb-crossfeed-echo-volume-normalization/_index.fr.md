---
title: "Comment utiliser les effets sonores et le DSP dans Flacbox : Compressor, Freeverb, Crossfeed, Echo, normalisation du volume et plus encore"
date: 2026-07-24
description: "Le guide complet de l'audio Flacbox sur iPhone, iPad et Mac. Découvrez comment fonctionne le moteur BASS, quels formats supplémentaires il lit (y compris la musique MOD et tracker et le DSD), et ce que fait exactement chaque effet, chaque curseur et chaque préréglage à votre son, ainsi que l'égaliseur 10 bandes et la chaîne DSP personnalisée."
keywords: ["effets audio Flacbox", "préréglages Flacbox expliqués", "moteur BASS Flacbox", "bibliothèque audio BASS iOS", "lecteur de musique MOD iPhone", "lecteur de musique tracker iOS", "lire MOD XM IT S3M iPhone", "lecteur DSD iOS", "lecteur FLAC iPhone", "lecteur de musique sans perte iOS", "préréglages égaliseur Flacbox", "égaliseur 10 bandes iPhone", "normalisation du volume iPhone", "EBU R128 iOS", "normalisation du volume sonore lecteur de musique", "crossfeed casque iOS", "crossfeed bs2b", "préréglages compresseur lecteur de musique", "réverbération freeverb iOS", "delay écho lecteur de musique", "chaîne DSP lecteur de musique", "amplification des basses iPhone", "comment ajouter des effets à la musique Flacbox", "meilleurs réglages égaliseur iPhone"]
tags: ["Flacbox", "Effets audio", "Guide pratique", "BASS", "Égaliseur", "Amplification des basses", "Compressor", "Freeverb", "Crossfeed", "Echo", "Normalisation du volume", "EBU R128", "Musique MOD", "Musique tracker", "DSD", "FLAC", "DSP", "Casque", "Préréglages"]
readingTime: 30
---

{{< author-byline >}}

{{< full-width-tables >}}

**Réponse courte :** Dans Flacbox, vous choisissez un **Moteur de lecture** dans **Paramètres > Lecteur audio** : **Standard** (le moteur système d'Apple), **Universal** (le moteur FFmpeg) ou **Sound FX** (le **moteur BASS™**). Le moteur que vous choisissez décide quels formats de fichiers se lisent, donc ce choix compte. Le moteur **Sound FX** lit des formats supplémentaires que la plupart des applications iPhone ignorent (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, ainsi que l'ancienne **musique MOD et tracker** comme MOD, XM, IT et S3M), et c'est le seul moteur qui alimente les outils sonores : un **égaliseur 10 bandes**, la **Normalisation du volume**, le **Compressor**, le **Freeverb**, l'**Auto Wah**, le **Phaser**, le **Flanger**, l'**Echo**, le **Chorus**, la **Distortion**, le **Rotate**, le **Crossfeed** et une **chaîne DSP** que vous construisez vous-même. Donc, pour utiliser les effets de ce guide, réglez d'abord votre Moteur de lecture sur **Sound FX**. Chaque outil a des **préréglages** prêts à l'emploi. Ouvrez-les dans **Paramètres > Lecteur audio** (Effets audio, Égaliseur audio, Traitement du signal), ou touchez le bouton **⋯ (Plus)** sur le lecteur et choisissez **Effets audio**. Rien de ce que vous faites ici ne modifie jamais vos fichiers.

> Les explications des curseurs et des préréglages ci-dessous sont les mêmes descriptions courtes que Flacbox vous montre dans l'application, agrémentées d'un peu de contexte supplémentaire pour que vous ayez une vue d'ensemble avant de toucher.

## Comment lire ce guide

Chaque outil fonctionne de la même manière :

1. **Activez-le.** Chaque effet a son propre interrupteur marche/arrêt. Ils sont tous désactivés au départ. Vous pouvez en activer autant que vous le souhaitez en même temps.
2. **Choisissez un préréglage.** Un préréglage est un réglage prêt à l'emploi. Touchez-en un et le son change aussitôt. Ce guide indique ce que fait **chaque** préréglage.
3. **Ajustez finement (facultatif).** Ouvrez les curseurs pour régler à la main. Dès que vous déplacez un curseur, l'effet affiche **Manuel**, ainsi vous savez que vous avez quitté le préréglage. Chaque curseur a un bouton de réinitialisation.

Rien n'est enregistré dans vos fichiers. Ce sont des effets en direct. Désactivez un effet et votre son d'origine revient aussitôt.

## Choisissez votre moteur de lecture (Sound FX possède les effets)

Flacbox ne mélange pas les moteurs entre eux. Vous en choisissez **un** dans **Paramètres > Lecteur audio > Moteur de lecture**, et le moteur que vous choisissez décide quels formats de fichiers vous pouvez lire et si les effets sont disponibles. Il y a trois choix, affichés dans l'application sous ces noms exacts :

1. **Standard.** Le moteur système intégré d'Apple. Utilise le décodage matériel pour une consommation de batterie réduite.
2. **Universal.** Le moteur FFmpeg, qui ouvre une très large gamme de formats.
3. **Sound FX.** Le **moteur BASS™**. Il lit les fichiers sans perte et haute résolution avec une précision totale, ajoute la musique de modules (tracker) et alimente chaque effet, l'égaliseur 10 bandes et la chaîne DSP de ce guide.

Comme chaque moteur prend en charge son propre ensemble de formats, les fichiers que vous pouvez lire changent selon le moteur que vous sélectionnez. Plus important encore, les effets, l'égaliseur et la chaîne DSP fonctionnent **uniquement** avec le moteur **Sound FX**, donc choisissez-le en premier si vous voulez les utiliser.

Sound FX est bâti sur **BASS™**, une bibliothèque audio professionnelle d'Un4seen Developments. Vous pouvez en savoir plus sur sa page d'accueil sur [un4seen.com](https://www.un4seen.com/).

## Formats de musique : ce que le moteur Sound FX (BASS™) ajoute (y compris la musique MOD et tracker)

Avec le moteur **Sound FX (BASS™)** sélectionné, Flacbox lit les formats spécialisés ci-dessous, en plus des formats courants. Le plus spécial est la **musique de modules**, aussi appelée **musique tracker**. Un fichier de module n'est pas un enregistrement normal. Il contient de petits sons d'instruments plus une « partition » qui indique comment les jouer, et Flacbox reconstruit le morceau en direct à partir de cette partition, comme ces fichiers étaient censés être lus. Les lecteurs normaux ne peuvent pas faire cela.

| Type de musique | Formats | Bon à savoir |
|---|---|---|
| **Musique de modules / tracker** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Reconstruite en direct par le lecteur de modules BASS™. Idéale pour les chiptunes et les anciens morceaux demoscene ou Amiga. |
| **Sans perte moderne** | FLAC | Qualité complète, plus petit que WAV. |
| **Autres sans perte** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Types sans perte moins courants, tous pris en charge. |
| **DSD haute résolution** | DSF, DFF | Se lit sur du matériel normal en utilisant le DSD sur PCM. |
| **Avec perte moderne** | Opus, Ogg Vorbis, MP3 | Les types de streaming et de téléchargement habituels. |

Le moteur Sound FX lit aussi les formats grand public d'Apple (AAC, ALAC, M4A, WAV, AIFF) et les flux en direct, donc les effets et l'égaliseur fonctionnent aussi sur ceux-ci.

**Pourquoi cela vous aide :** si vous avez un mélange d'albums FLAC, de fichiers DSD haute résolution et un dossier d'anciens morceaux tracker MOD ou XM, Flacbox les lit tous, et l'égaliseur et les effets fonctionnent sur chacun d'eux.

## Les trois menus que vous utiliserez

Flacbox garde ses outils sonores à trois endroits, tous dans les paramètres du lecteur audio. Assurez-vous d'abord que votre **Moteur de lecture** est réglé sur **Sound FX** (Paramètres > Lecteur audio > Moteur de lecture), car les effets, l'égaliseur et la chaîne DSP ne sont disponibles qu'avec ce moteur.

- **Effets audio** (le rack d'effets) : ouvrez le lecteur, touchez **⋯ (Plus)**, touchez **Effets audio**. Ou allez dans **Paramètres > Lecteur audio > Effets audio**.
- **Égaliseur audio** (10 bandes et préréglages) : **Paramètres > Lecteur audio > Égaliseur audio**.
- **Traitement du signal** (votre propre chaîne DSP) : **Paramètres > Lecteur audio > Traitement du signal**.

Vous pouvez aussi régler la **fréquence d'échantillonnage de sortie**, les **canaux** et la **taille du tampon** sous **Paramètres > Lecteur audio**.

## L'égaliseur 10 bandes

**Ce qu'il fait :** Change la tonalité de la musique, des basses profondes aux aigus brillants. C'est le meilleur outil pour une **amplification des basses** propre ou un haut du spectre plus brillant et plus clair. Voyez-le comme dix boutons de volume, chacun pour une tranche différente du son. Montez une bande pour mettre cette partie en avant, baissez-la pour la reculer. De petits changements de quelques dB sonnent généralement le mieux, et cela fonctionne sur tout ce que vous lisez.

**Comment il fonctionne :** Dix curseurs à **32, 64, 125, 250, 500 Hz et 1, 2, 4, 8, 16 kHz**. Chacun va de **-12 dB (coupe)** à **+12 dB (amplification)**. Il y a aussi un **Préamplificateur** de **-24 à +24 dB** pour le niveau global. Vous pouvez enregistrer vos propres préréglages et les **exporter ou importer** entre appareils.

**Ce que fait chaque préréglage intégré (22 préréglages) :**

| Préréglage | Ce qu'il fait à votre son |
|---|---|
| **Flat** | Aucun changement. Toutes les bandes à zéro. Un point de départ propre. |
| **Acoustic** | Basses chaudes et aigus nets et présents. Rend les guitares acoustiques et les voix naturelles et vivantes. |
| **Bass Booster** | Forte élévation dans les graves, médiums et aigus intacts. Plus de punch et de poids. |
| **Bass Reducer** | Coupe les graves. Pratique pour les pièces résonnantes, les écouteurs bon marché ou les morceaux lourds. |
| **Treble Booster** | Élève uniquement les aigus. Ajoute de l'éclat et de l'air, plus de détail. |
| **Treble Reducer** | Adoucit les aigus. Apprivoise les enregistrements durs ou tranchants. |
| **Classical** | Graves pleins et aigus doux avec un léger creux dans les médiums. Doux et spacieux pour la musique orchestrale. |
| **Dance** | Graves puissants et aigus brillants avec des médiums creusés. Punchy et énergique pour les morceaux de club. |
| **Deep** | Graves chauds et épais avec des aigus plus doux. Un son douillet et décontracté. |
| **Electronic** | Basses puissantes et aigus brillants pour les synthés et les beats. Large et moderne. |
| **Hip-Hop** | Basses lourdes et aigus clairs avec des médiums maîtrisés. Pesant et punchy. |
| **Jazz** | Chaud et doux, avec un petit creux dans les médiums. Facile et naturel pour le jazz acoustique. |
| **Latin** | Graves et aigus rehaussés avec des médiums propres. Brillant et vivant. |
| **Loudness** | Amplifie fortement les basses et les aigus (une courbe en « sourire »). Sonne plus plein à faible volume. |
| **Lounge** | Médiums en avant avec des contours doux. Détendu et convivial pour les voix. |
| **Piano** | Médiums et aigus clairs pour que les notes de piano résonnent proprement. |
| **Pop** | Médiums rehaussés pour les voix, avec les graves et les aigus reculés. Les voix passent au premier plan. |
| **R&B** | Chaleur des bas-médiums très forte et aigus clairs. Doux et riche. |
| **Rock** | Graves et aigus rehaussés pour les guitares et la batterie. Énergique et plein. |
| **Small Speakers** | Amplifie les graves et coupe les aigus pour aider les petits haut-parleurs à sonner plus plein. |
| **Spoken Word** | Élève la plage vocale et coupe les basses profondes. Rend la parole claire. |
| **Vocal Booster** | Pousse le médium où vivent les voix, coupe autour. Les voix ressortent. |

**Astuce pour les basses :** Commencez par **Bass Booster**, puis, si cela sonne boueux, baissez le Préamplificateur de 1 à 2 dB pour que rien ne distorde.

## Normalisation du volume (volume uniforme)

**Ce qu'elle fait :** Certaines chansons se lisent plus fort que d'autres, donc vous changez constamment le volume. Ceci fait que chaque chanson se lit à peu près au même volume d'elle-même, donc vous n'avez pas à le faire. C'est parfait pour les listes de lecture en aléatoire qui mélangent d'anciens et de nouveaux enregistrements, différents albums ou différentes sources, où un morceau peut être beaucoup plus fort que le suivant.

**Comment elle fonctionne :** Elle écoute le volume réel de chaque morceau à l'aide de la norme **EBU R128** (mesuré en **LUFS**, la même idée qu'utilisent les services de streaming), puis ajuste chaque morceau vers votre cible. Elle n'a besoin d'aucune balise dans vos fichiers et ne modifie jamais l'audio. EBU R128 mesure le volume que vos oreilles ressentent réellement sur toute la chanson, pas seulement le pic le plus élevé, ce qui explique pourquoi elle correspond au volume réellement perçu des morceaux. Flacbox calcule cela en direct pendant que la musique joue (et vérifie le volume à l'avance quand elle le peut), puis applique un seul changement de volume stable au morceau. La limite de **Gain max** empêche les enregistrements très faibles d'être poussés si fort qu'ils distordent. Comme elle lit le son lui-même, elle fonctionne sur n'importe quelle source, y compris les fichiers cloud, les flux en direct et la musique de modules, même quand les fichiers n'ont aucune balise de volume.

**Curseurs :**

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Volume cible** | Définit le volume vers lequel chaque morceau est nivelé. Des valeurs plus élevées font tout jouer plus fort au global. | -30 à -6 LUFS (-16) |
| **Gain max** | Limite l'amplification des morceaux faibles. Des valeurs plus élevées rapprochent les enregistrements doux de la cible. | 0 à 24 dB (12) |

**Préréglages :**

| Préréglage | Ce qu'il fait |
|---|---|
| **Light** | Nivellement doux pour une écoute décontractée. Égalise les sauts de volume évidents sans trop pousser les morceaux faibles. |
| **Standard** | Le réglage par défaut polyvalent. Une cible de volume de type streaming qui convient à la plupart des musiques. Commencez ici. |
| **Strong** | Correspondance agressive qui pousse fermement les morceaux faibles vers le haut. Idéal pour les bibliothèques mixtes avec de grandes différences de niveau. |
| **Night** | Une cible globale plus calme qui élève quand même les passages doux, pour que l'écoute nocturne reste cohérente et basse. |

## Compressor (égaliser les parties fortes et faibles)

**Ce qu'il fait :** Dans une même chanson, les parties calmes peuvent être trop douces et les parties fortes trop fortes. Ceci les rapproche, pour que toute la chanson soit facile à entendre, même dans la voiture ou dans un endroit bruyant. Il baisse doucement les moments les plus forts et élève les plus doux, pour que vous cessiez de chercher le volume au cours d'un même morceau. C'est différent de la Normalisation du volume : le Compressor égalise les choses **à l'intérieur** d'une chanson, tandis que la Normalisation du volume fait correspondre le volume **entre** les chansons. Les deux fonctionnent bien ensemble. Commencez par un préréglage, et n'ouvrez les curseurs que si vous voulez plus de contrôle.

**Curseurs :**

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Seuil** | Le niveau où la compression commence. Des valeurs plus basses écrasent davantage le son, rapprochant les parties faibles et fortes. | -60 à 0 dB (-20) |
| **Ratio** | À quel point les parties fortes sont retenues une fois qu'elles dépassent le seuil. Des valeurs plus élevées compressent plus fort, gardant le son plus uniforme. | 1:1 à 30:1 (4:1) |
| **Attaque** | À quelle vitesse l'effet réagit à un pic fort soudain. Des valeurs courtes attrapent les transitoires ; des valeurs plus longues les laissent passer. | 0,1 à 1000 ms (10 ms) |
| **Relâchement** | À quelle vitesse l'effet lâche après le passage de la partie forte. Des valeurs courtes peuvent pomper ; des valeurs plus longues sonnent plus lisses. | 10 ms à 5 s (100 ms) |
| **Gain master** | Amplification finale de sortie appliquée après traitement. Montez-le pour élever le volume global une fois la dynamique égalisée. | -30 à +30 dB (0) |

**Préréglages :**

| Préréglage | Ce qu'il fait |
|---|---|
| **Transparent** | Filet de sécurité à peine présent. Préserve la dynamique presque entièrement et n'attrape que les pics les plus forts. |
| **Soft** | Nivellement léger pour l'écoute hi-fi à la maison. Lissage subtil sans écraser la musique. |
| **Standard** | Réglage par défaut raisonnable pour la lecture de musique au quotidien. Le premier préréglage à essayer. |
| **Heavy** | Égalisation agressive pour les environnements bruyants. Voiture, pièce bondée, écoute à faible volume. |
| **Voice / Podcast** | Réglé pour la parole. Une attaque plus lente laisse passer les sifflantes, un gain de compensation généreux remonte les voix. |
| **Old Recordings** | Albums vintage et vinyles restaurés, où le niveau moyen est inférieur aux sorties modernes. |
| **Late Night** | Forte compression plus grande amplification pour une écoute calme quand les voisins ou la famille endormie comptent. |
| **Movie Dialog** | Remonte la parole face à la musique et aux effets sonores dans une bande-son variée. |
| **Streaming Match** | Vise approximativement la normalisation du volume des services de streaming modernes, autour de -14 LUFS. |
| **Maximum Loudness** | Tout à fond. Atteint le limiteur ; attendez-vous à un signal écrasé et très uniforme. Le préréglage littéral de volume maximal. |

## Freeverb (réverbération, une sensation d'espace)

**Ce qu'il fait :** Ajoute une sensation d'espace à la musique, d'une petite pièce jusqu'à une grande salle. Choisissez un préréglage, ou ajustez finement vous-même le mélange sec et humide, la taille de la pièce, l'amortissement et la largeur. La réverbération est l'écho naturel que vous entendez dans tout espace réel, et Freeverb la recrée en logiciel. Un peu rend les enregistrements plats ou pris de près plus ouverts et vivants. Beaucoup place la musique dans un espace grand et lointain. C'est un effet créatif, donc gardez le mélange humide modeste pour des résultats naturels.

**Curseurs :**

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Mélange sec** | Quelle quantité du son original, intact, est conservée. Des valeurs plus élevées laissent plus de signal sec dans le mélange. | 0 à 1 (0.0) |
| **Mélange humide** | Quelle quantité du son réverbéré est ajoutée. Des valeurs plus élevées rendent la réverbération plus forte et plus évidente. | 0 à 3 (1.0) |
| **Taille de la pièce** | La taille de l'espace imaginé. Des valeurs plus élevées donnent une queue de réverbération plus longue et plus grande, d'une petite pièce jusqu'à une cathédrale. | 0 à 1 (0.5) |
| **Amortissement** | À quelle vitesse les hautes fréquences s'estompent dans la queue. Des valeurs plus élevées rendent la réverbération plus sombre et plus chaude. | 0 à 1 (0.5) |
| **Largeur** | L'étalement stéréo de la réverbération. Des valeurs plus élevées font ressentir l'espace plus large entre les canaux gauche et droit. | 0 à 1 (1.0) |

**Préréglages :**

| Préréglage | Ce qu'il fait |
|---|---|
| **Room** | Un petit espace serré. Une ambiance subtile qui ajoute une sensation de lieu sans noyer le son. |
| **Studio** | Une salle d'enregistrement sèche et maîtrisée. Juste assez de réflexion pour sonner naturel. |
| **Hall** | Une grande salle de concert. Une queue longue et luxuriante qui convient à la musique orchestrale et acoustique. |
| **Cathedral** | Un immense espace de pierre résonnant. La queue de réverbération la plus longue et la plus dramatique. |
| **Plate** | Une réverbération à plaque de studio brillante et dense. Classique pour les voix et la batterie. |
| **Ambience** | Une ambiance courte et aérée. Ajoute une légère sensation d'espace tout en restant surtout sec. |

## Auto Wah (balayage de filtre funky)

**Ce qu'il fait :** Un filtre qui balaie de haut en bas tout seul pour un son wah funky, semblable à une voix. Choisissez un préréglage, ou réglez vous-même le mélange humide, le feedback, la vitesse, la plage et la fréquence. C'est le même balayage « wah » que fait une pédale wah de guitare, mais ici il bouge tout seul au rythme de la musique. Il sonne très bien sur le funk, le disco et les morceaux électroniques. C'est un effet audacieux et évident, donc un peu suffit largement pour une écoute au quotidien.

**Curseurs :**

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Mélange humide** | À quel point l'effet wah est fort dans le mélange. Des valeurs plus élevées rendent le filtre balayeur plus évident. | -2 à +2 (1.5) |
| **Feedback** | Quelle quantité de la sortie est réinjectée dans l'effet. Des valeurs plus élevées rendent le wah plus résonnant et prononcé. | -1 à +1 (0.5) |
| **Vitesse** | À quelle vitesse le filtre balaie de haut en bas. Des valeurs plus élevées donnent un wah plus rapide et plus rythmé. | 0,1 à 9 Hz (2.0) |
| **Plage** | Jusqu'où le filtre balaie, en octaves. Des valeurs plus élevées donnent un balayage plus large et plus dramatique. | 0,1 à 9 octaves (4.3) |
| **Fréquence** | La fréquence de base autour de laquelle le filtre balaie. Des valeurs plus basses sonnent plus profondes ; des valeurs plus élevées sonnent plus brillantes. | 1 à 1000 Hz (50) |

**Préréglages :**

| Préréglage | Ce qu'il fait |
|---|---|
| **Classic** | Un balayage wah équilibré et classique. Un bon point de départ pour le funk et le rock. |
| **Slow** | Un balayage lent et large qui dérive doucement de haut en bas. Idéal pour les nappes et les notes longues. |
| **Funky** | Un balayage rapide et punchy avec beaucoup de mouvement. Ajoute du mordant rythmique aux guitares et aux synthés. |
| **Deep** | Un balayage profond et large partant d'une basse fréquence. Grand et dramatique. |
| **Subtle** | Un mouvement doux et discret. Ajoute du caractère sans dominer le son. |
| **Resonant** | Un wah net et résonnant avec un feedback élevé. Semblable à une voix et expressif. |

## Phaser (souffle tourbillonnant)

**Ce qu'il fait :** Un filtre balayeur qui ajoute un mouvement tourbillonnant et soufflant au son. Choisissez un préréglage, ou réglez vous-même le feedback, la vitesse, la plage et la fréquence. Il ajoute un mouvement doux et un chatoiement sans changer les notes. Il est subtil sur les voix et les nappes, et dramatique sur les synthés et les guitares. Essayez Slow pour une sensation rêveuse ou Jet pour un fort tourbillon.

**Curseurs :**

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Feedback** | Quelle quantité de la sortie est réinjectée dans l'effet. Des valeurs plus élevées rendent le phaser plus résonnant et prononcé. | -1 à +1 (0.0) |
| **Vitesse** | À quelle vitesse le filtre balaie de haut en bas. Des valeurs plus élevées donnent un phasing plus rapide et plus rythmé. | 0,1 à 9 Hz (1.0) |
| **Plage** | Jusqu'où le filtre balaie, en octaves. Des valeurs plus élevées donnent un balayage plus large et plus dramatique. | 0,1 à 9 octaves (4.0) |
| **Fréquence** | La fréquence de base autour de laquelle le filtre balaie. Des valeurs plus basses sonnent plus profondes ; des valeurs plus élevées sonnent plus brillantes. | 1 à 1000 Hz (100) |

**Préréglages :**

| Préréglage | Ce qu'il fait |
|---|---|
| **Classic** | Un balayage de phaser équilibré et classique. Un bon point de départ pour les guitares et les claviers. |
| **Slow** | Un balayage lent et large qui dérive doucement de haut en bas. Idéal pour les nappes et les notes longues. |
| **Fast** | Un balayage rapide et chatoyant avec beaucoup de mouvement. Ajoute du mouvement et de l'énergie. |
| **Deep** | Un balayage profond et large partant d'une basse fréquence. Grand et dramatique. |
| **Subtle** | Un mouvement doux et discret. Ajoute du caractère sans dominer le son. |
| **Jet** | Un balayage intense et résonnant avec un feedback élevé, le souffle classique d'avion à réaction. |

## Flanger (balayage d'avion à réaction)

**Ce qu'il fait :** Un délai court et mouvant qui donne au son un souffle balayeur de type jet. Choisissez un préréglage, ou réglez vous-même la profondeur, le feedback, la vitesse et le délai. C'est un cousin plus fort et plus métallique du phaser, célèbre pour le balayage soufflant du rock classique et de la musique électronique. Les réglages subtils ajoutent un mouvement doux, tandis que les réglages profonds sont dramatiques et évidents. À utiliser avec parcimonie, pour l'effet.

**Curseurs :**

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Profondeur** | À quel point l'effet de balayage est fort. Des valeurs plus élevées rendent le flanging plus évident. | 0 à 100 % (25) |
| **Feedback** | Quelle quantité de la sortie est réinjectée dans l'effet. Des valeurs plus élevées rendent le flanger plus résonnant et métallique. | -99 à +99 % (-50) |
| **Vitesse** | À quelle vitesse le balayage se déplace de haut en bas. Des valeurs plus élevées donnent un mouvement plus rapide et plus chatoyant. | 0 à 10 Hz (0.25) |
| **Délai** | Le temps de délai de base sur lequel le balayage est construit. Des valeurs plus élevées donnent un caractère plus profond et plus creux. | 0 à 4 ms (2.0) |

**Préréglages :**

| Préréglage | Ce qu'il fait |
|---|---|
| **Classic** | Un flanger équilibré et classique. Un bon point de départ pour les guitares et les claviers. |
| **Subtle** | Un balayage doux et discret. Ajoute du mouvement sans dominer le son. |
| **Deep** | Un balayage profond et lourd avec un feedback fort. Grand et dramatique. |
| **Jet** | Un balayage intense avec un feedback positif, le souffle classique d'avion à réaction. |
| **Fast** | Un balayage rapide et chatoyant avec beaucoup de mouvement et d'énergie. |
| **Wide** | Un balayage lent et large avec un long délai. Luxuriant et spacieux. |

## Echo (répétitions)

**Ce qu'il fait :** Répète le son en échos qui s'estompent pour une sensation d'espace et de profondeur. Choisissez un préréglage, ou réglez vous-même le mélange humide, le feedback et le délai. C'est comme crier dans un canyon : le son revient une ou plusieurs fois après un court intervalle. Une seule répétition courte ajoute du corps et une sensation rétro, tandis que des répétitions plus longues avec plus de feedback créent des queues spacieuses et traînantes. Le préréglage Ping Pong fait rebondir les répétitions entre vos oreilles gauche et droite, ce qui est amusant au casque. Gardez le mélange humide modeste pour que les échos soutiennent la musique plutôt que de la couvrir.

**Curseurs :**

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Mélange humide** | À quel point les échos sont forts par rapport au son original. Des valeurs plus élevées font davantage ressortir les répétitions. | -2 à +2 (0.6) |
| **Feedback** | Combien de fois l'écho se répète. Des valeurs plus élevées donnent plus de répétitions qui mettent plus de temps à s'estomper. | -1 à +1 (0.5) |
| **Délai** | Le temps entre les échos. Des valeurs plus courtes donnent un slap-back serré ; des valeurs plus longues donnent des répétitions espacées. | 0,01 à 2 s (0.4) |

**Préréglages :**

| Préréglage | Ce qu'il fait |
|---|---|
| **Slapback** | Une seule répétition serrée juste derrière le son. Le slap-back rockabilly classique. |
| **Room** | Un écho court et naturel, comme une petite pièce. Ajoute de l'espace sans étaler le son. |
| **Tape** | Des répétitions chaudes et moyennes qui s'estompent progressivement, comme un ancien delay à bande. |
| **Dub** | Des répétitions longues et lourdes avec un feedback fort. Grand, dubby et spacieux. |
| **Ping Pong** | Les échos rebondissent entre les haut-parleurs gauche et droit pour un large effet stéréo. |
| **Long** | Des répétitions lentes et largement espacées qui traînent loin derrière le son. |

## Chorus (son plus épais et plus large)

**Ce qu'il fait :** Épaissit et élargit le son en superposant une copie décalée sur l'original. Choisissez un préréglage, ou réglez vous-même le mélange humide/sec, la profondeur, la vitesse et le feedback. Il fait sonner un instrument ou une voix comme plusieurs jouant ensemble, en ajoutant des copies mouvantes légèrement désaccordées. Cela ajoute de la richesse et un chatoiement doux. Les réglages subtils réchauffent les choses, tandis que les réglages forts sonnent luxuriants et rêveurs. Il est populaire sur les guitares, les claviers et les voix.

**Curseurs :**

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Humide/Sec** | Quelle quantité du chorus vous entendez par rapport au son original. Des valeurs plus élevées rendent l'effet plus évident. | 0 à 100 % (50) |
| **Profondeur** | Jusqu'où la hauteur oscille de haut en bas. Des valeurs plus élevées donnent un son plus épais et plus chatoyant. | 0 à 100 % (25) |
| **Vitesse** | À quelle vitesse le chatoiement se déplace. Les vitesses plus lentes sonnent douces et luxuriantes ; les plus rapides sonnent plus comme un vibrato. | 0 à 10 Hz (1.1) |
| **Feedback** | Quelle quantité de l'effet est réinjectée en lui-même. Des valeurs plus élevées rendent le chorus plus résonnant et intense. | -99 à +99 % (25) |

**Préréglages :**

| Préréglage | Ce qu'il fait |
|---|---|
| **Subtle** | Un épaississement doux qui ajoute de la chaleur sans attirer l'attention sur lui-même. |
| **Lush** | Un chorus riche et classique. Un excellent réglage polyvalent pour les guitares et les claviers. |
| **Ensemble** | Un chatoiement plein et en couches qui fait sonner un seul instrument comme plusieurs. |
| **Vibrato** | Entièrement humide avec une vitesse rapide, pour un vibrato oscillant au lieu d'un chorus subtil. |
| **Wide** | Un chatoiement lent et large qui ouvre l'image stéréo. Spacieux et rêveur. |
| **Twelve-String** | Un chatoiement brillant et résonnant rappelant une guitare à douze cordes. |

## Distortion (grain et mordant)

**Ce qu'elle fait :** Ajoute du grain et du mordant en surchargeant le son. Choisissez un préréglage, ou réglez vous-même le drive, la sortie et la tonalité. Elle rend délibérément le son plus rugueux, d'un mordant chaud et graveleux à un son cassé et fuzzy. C'est un effet créatif et pour le plaisir plutôt qu'un moyen d'améliorer la qualité, donc utilisez-le en petites quantités. Il est amusant sur les morceaux électroniques, rock et expérimentaux. Baissez la Sortie si un préréglage lourd devient trop fort.

**Curseurs :**

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Drive** | À quel point le son est distordu. Des valeurs plus élevées sont plus graveleuses et plus agressives. | 0 à 100 % (15) |
| **Sortie** | Le niveau de sortie après la distortion. Baissez-le si un réglage lourd devient trop fort. | -60 à 0 dB (-18) |
| **Tonalité** | Atténue les aigus avant la distortion. Des valeurs plus basses sonnent plus sombres et plus chaudes. | 100 à 8000 Hz (8000) |
| **Centre** | Sur quelle fréquence la distortion est concentrée. Décale le caractère vers le plus brillant ou le plus sombre. | 100 à 8000 Hz (2400) |
| **Largeur** | À quel point cette concentration est large. Étroit sonne net et nasillard ; large sonne plein et ouvert. | 100 à 8000 Hz (2400) |

**Préréglages :**

| Préréglage | Ce qu'il fait |
|---|---|
| **Warm Drive** | Un grain léger et chaud qui ajoute du mordant sans changer beaucoup le caractère. |
| **Crunch** | Un overdrive croustillant classique, punchy et rythmé. |
| **Overdrive** | Un son brillant et poussé avec beaucoup de mordant. Idéal pour les sons de lead. |
| **Fuzz** | Un fuzz épais et saturé. Lourd et plein d'harmoniques. |
| **Metal** | Un son à fort gain, serré et centré sur les médiums pour des sons agressifs et lourds. |
| **Screamer** | Un overdrive à médiums rehaussés qui perce, comme un tube screamer. |
| **LoFi** | Une distortion écrasée à bande étroite pour un caractère lo-fi graveleux. |

## Rotate (stéréo tournoyante)

**Ce qu'il fait :** Fait tourner le son autour du champ stéréo pour un effet rotatif et tourbillonnant. Choisissez un préréglage, ou réglez vous-même la vitesse. Il déplace lentement le son autour de vos canaux gauche et droit, un peu comme un haut-parleur tournant, ce qui ajoute une sensation tourbillonnante et hypnotique. Les réglages lents sont doux et larges, tandis que les réglages rapides sont vertigineux et évidents. C'est un effet stéréo, donc il est le plus perceptible au casque ou sur des haut-parleurs bien placés.

**Curseur :**

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Vitesse** | À quelle vitesse le son tourne autour du champ stéréo. Les valeurs négatives tournent dans l'autre sens ; zéro le maintient immobile. | -5 à +5 Hz (1.0) |

**Préréglages :**

| Préréglage | Ce qu'il fait |
|---|---|
| **Slow Pan** | Une dérive lente et douce d'un côté à l'autre. Subtil et large. |
| **Sway** | Un balancement gauche-droite régulier. Ajoute un mouvement doux à l'image stéréo. |
| **Rotary** | Une rotation moyenne rappelant un haut-parleur rotatif. |
| **Fast Spin** | Une rotation rapide autour du champ stéréo pour un effet vertigineux et tourbillonnant. |
| **Reverse** | Une rotation moyenne dans le sens opposé. |
| **Whirl** | Un tourbillon très rapide. Intense et désorientant. |

## Crossfeed (son naturel au casque)

Sur des haut-parleurs, chacune de vos oreilles entend à la fois le haut-parleur gauche et le droit, juste à des moments et des volumes légèrement différents. Au casque, ce mélange naturel disparaît : votre oreille gauche n'entend que le canal gauche et votre oreille droite uniquement le droit. Cette « super stéréo » peut donner l'impression que la musique est fractionnée à l'intérieur de votre tête, et les enregistrements très pannés, où un instrument se trouve entièrement d'un côté, peuvent sembler peu naturels ou fatigants lors de longues écoutes.

Crossfeed corrige cela en mélangeant une petite quantité filtrée de chaque canal dans l'autre, avec un tout petit délai et une atténuation douce des hautes fréquences. Cela se rapproche de la façon dont le son de vrais haut-parleurs atteint vos deux oreilles, y compris la manière dont votre tête ombre légèrement l'oreille éloignée. Le résultat est une image plus naturelle, semblable à des haut-parleurs, qui se situe un peu devant vous au lieu d'être dans votre tête, et cela réduit la fatigue d'écoute lors de longues sessions. Flacbox utilise la célèbre méthode **bs2b (Bauer stereophonic-to-binaural)**, un crossfeed open-source respecté et utilisé par de nombreux lecteurs audiophiles. Vous pouvez en savoir plus sur l'algorithme sur la [page du projet bs2b](https://bs2b.sourceforge.net/).

Le **Cutoff** contrôle à quel point le mélange sonne chaud, et le **Niveau de feed** contrôle à quel point il est fort. Les préréglages couvrent les niveaux bs2b classiques, d'une touche à peine présente jusqu'à un mélange ferme, semblable à des haut-parleurs. Crossfeed est un effet pour casque, donc laissez-le désactivé quand vous écoutez sur des haut-parleurs.

**Curseurs :**

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Cutoff** | Définit où le mélange entre les canaux commence à s'atténuer. Des valeurs plus basses donnent un effet plus chaud et plus prononcé. | 300 à 2000 Hz (700) |
| **Niveau de feed** | Contrôle quelle quantité d'un canal se mélange dans l'autre. Des valeurs plus élevées produisent un son plus semblable à des haut-parleurs. | 1 à 15 dB (4.5) |

**Préréglages :**

| Préréglage | Ce qu'il fait |
|---|---|
| **Subtle** | Crossfeed à peine présent pour une écoute décontractée. Adoucit la stéréo très pannée sans changer l'équilibre tonal. |
| **Chu Moy** | Le réglage par défaut polyvalent classique. Équilibré et légèrement chaud, il fonctionne sur presque n'importe quel matériel. Commencez ici. |
| **Strong** | Mélange plus fort pour les mixages plus pannés. Rétrécissement stéréo plus évident. |
| **Jan Meier** | Populaire chez les passionnés de casques. Feed plus large, présentation plus semblable à des haut-parleurs, légère élévation des basses. |
| **Speaker-like** | Réglé pour la reproduction la plus naturelle de type haut-parleur au casque. |
| **Vintage Stereo** | Crossfeed agressif réglé pour les mixages des années 1960 et 1970 avec batterie et voix très pannées. |

## Traitement du signal : construisez votre propre chaîne DSP

Au-delà des effets prêts à l'emploi, Flacbox vous laisse construire votre propre chaîne dans **Paramètres > Lecteur audio > Traitement du signal**. Comme l'explique l'application quand la chaîne est vide : *« Touchez + pour ajouter un effet. Activez ou désactivez chacun avec son interrupteur, glissez pour réorganiser, touchez pour modifier ses paramètres, et appuyez longuement pour dupliquer ou supprimer. »*

L'**ordre compte** : un filtre avant une distortion sonne différemment du même filtre après elle. Vous pouvez aussi diriger toute la chaîne vers **Tous les canaux**, le **Canal gauche** ou le **Canal droit**.

Ci-dessous se trouve chaque bloc, avec le propre texte de l'application pour chaque curseur et chaque préréglage.

### Gain (ajustement de niveau)

Monte ou baisse le niveau à un point de la chaîne.

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Gain** | Amplifie ou coupe le niveau à ce point de la chaîne. Utilisez-le pour compenser le niveau après d'autres effets, ou pour pousser ceux qui suivent. | -24 à +24 dB (0) |

| Préréglage | Ce qu'il fait |
|---|---|
| **Unity** | Aucun changement de niveau. Un point de départ neutre. |
| **Cut** | Une grande coupe. Apprivoise une source forte, ou fait de la place avant les effets qui suivent. |
| **Trim** | Une coupe douce pour reculer un peu le niveau. |
| **Lift** | Une amplification modeste pour remonter une source faible. |
| **Boost** | Une forte amplification pour du matériel faible, ou pour pousser plus fort les effets suivants. |
| **Max** | Amplification maximale. Fort, attention au clipping plus loin dans la chaîne. |

### Low Pass (supprime les aigus)

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Cutoff** | Définit où le filtre commence à atténuer les aigus. Baissez-le pour assombrir et adoucir le son ; montez-le vers le haut pour ouvrir pleinement. | 20 Hz à 20 kHz (20 kHz) |
| **Résonance** | Met en valeur les fréquences juste au niveau du cutoff. Gardez-la basse pour une atténuation propre ; montez-la pour un bord pointu et sifflant. | 0,1 à 10 (0.707) |

| Préréglage | Ce qu'il fait |
|---|---|
| **Air** | Rogne seulement le tout haut. Enlève un peu de mordant sans ternir le son. |
| **Warm** | Une atténuation douce des aigus pour une tonalité plus chaude et plus arrondie. |
| **Mellow** | Nettement adouci. Recule la brillance pour une sensation décontractée. |
| **Muffled** | Sombre et étouffé, comme entendu à travers un mur. |
| **Telephone** | Un pic étroit et résonnant bas dans la plage. Une voix fine, de type téléphone. |

### High Pass (supprime les graves)

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Cutoff** | Définit où le filtre commence à atténuer les graves. Montez-le pour amincir les graves et supprimer le grondement ; baissez-le vers le bas pour ouvrir pleinement. | 20 Hz à 20 kHz (20 Hz) |
| **Résonance** | Met en valeur les fréquences juste au niveau du cutoff. Gardez-la basse pour une atténuation propre ; montez-la pour un bord pointu et sifflant. | 0,1 à 10 (0.707) |

| Préréglage | Ce qu'il fait |
|---|---|
| **Rumble Cut** | Supprime le grondement subsonique et le décalage DC sans toucher aux graves audibles. |
| **Tighten** | Rogne les basses fréquences résonnantes pour des basses plus serrées et plus propres. |
| **Thin** | Coupe la chaleur et le corps, laissant un son plus léger et plus fin. |
| **Radio** | Seuls les médiums et les aigus restent, comme un petit haut-parleur de radio. |
| **Telephone** | Un pic étroit et résonnant haut dans la plage. Une voix fine, de type téléphone. |

### Band Pass (garde une bande médiane)

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Centre** | Définit la fréquence que le filtre laisse passer. Tout au-dessus et en dessous est atténué. Balayez-le pour isoler les graves, les médiums ou les aigus. | 20 Hz à 20 kHz (1 kHz) |
| **Résonance** | Contrôle la largeur de la bande. Des valeurs basses laissent passer une large plage ; montez-la pour resserrer autour du centre pour un son net et résonnant. | 0,1 à 10 (0.707) |

| Préréglage | Ce qu'il fait |
|---|---|
| **Voice** | Une large bande autour des médiums où se trouvent la plupart des voix. Un point de départ neutre. |
| **Bass** | Isole les graves, ne laissant que la basse et la grosse caisse. |
| **Body** | Se concentre sur les bas-médiums pour un corps chaud et boxy. |
| **Presence** | Élève les hauts-médiums pour la clarté et la présence. |
| **Telephone** | Une bande médium étroite. Un son fin, de type téléphone. |
| **Wah** | Un pic très étroit et résonnant. Balayez le centre pour un effet wah. |

### Notch (supprime une bande étroite)

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Fréquence** | Définit la fréquence que le filtre supprime. Tout au-dessus et en dessous passe. Accordez-le sur un ronflement ou une résonance pour l'éliminer. | 20 Hz à 20 kHz (60 Hz) |
| **Résonance** | Contrôle la largeur de la coupe. Des valeurs basses creusent une large plage ; montez-la pour ne supprimer qu'une bande ponctuelle et laisser le reste intact. | 0,1 à 10 (8.0) |

| Préréglage | Ce qu'il fait |
|---|---|
| **Mains Hum 60** | Supprime le ronflement électrique de 60 Hz (secteur nord-américain). Un point de départ neutre. |
| **Mains Hum 50** | Supprime le ronflement électrique de 50 Hz (secteur européen et autres). |
| **Rumble** | Coupe un grondement ou une résonance basse fréquence sans amincir tout le bas du spectre. |
| **Mud** | Creuse la boue des bas-médiums pour un son plus propre et plus clair. |
| **Boxy** | Supprime une résonance boxy des médiums. |
| **Harsh** | Apprivoise un pic dur et perçant dans les hauts-médiums. |

### Peaking (bande d'EQ paramétrique)

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Fréquence** | Le centre de la bande à amplifier ou couper. Balayez-le pour trouver la fréquence que vous voulez façonner. | 20 Hz à 20 kHz (1 kHz) |
| **Gain** | Quelle quantité amplifier ou couper au centre. Positif élève la bande ; négatif la creuse. | -15 à +15 dB (0) |
| **Facteur Q** | Définit la largeur de la bande. Des valeurs basses façonnent une large zone ; des valeurs élevées resserrent pour des changements chirurgicaux et ponctuels. | 0,1 à 10 (1.0) |

| Préréglage | Ce qu'il fait |
|---|---|
| **Presence** | Une large élévation des hauts-médiums pour la clarté et la présence. Un point de départ neutre. |
| **Warmth** | Une large amplification des bas-médiums qui ajoute du corps et de la chaleur. |
| **Vocal Boost** | Élève le cœur de la plage vocale pour amener les voix en avant. |
| **Cut Mud** | Creuse la boue boxy des bas-médiums pour un son plus propre. |
| **Tame Harsh** | Une coupe étroite pour apprivoiser un pic dur et perçant. |
| **Punch** | Une amplification des graves qui ajoute du punch et de l'impact au bas du spectre. |
| **Sub Boost** | Une amplification profonde tout en bas pour un poids sub-grave supplémentaire. |
| **Air** | Une large élévation en haut pour un éclat ouvert et aéré. |
| **Clarity** | Élève les hauts-médiums pour ajouter de la définition et du mordant. |
| **De-Ess** | Une coupe étroite dans la plage des sifflantes pour apprivoiser les S durs. |
| **De-Boom** | Coupe une accumulation basse fréquence résonnante pour un bas du spectre plus serré. |
| **Scoop** | Un large creux dans les médiums pour un son creusé et moderne. |

### Low Shelf (contrôle des basses et amplification des basses)

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Fréquence** | Définit le coin en dessous duquel le shelf prend effet. Tout en dessous est amplifié ou coupé ensemble. | 20 à 2000 Hz (200) |
| **Gain** | Quelle quantité élever ou baisser les graves. Positif ajoute du poids et de la chaleur ; négatif les amincit. | -15 à +15 dB (0) |

| Préréglage | Ce qu'il fait |
|---|---|
| **Warmth** | Une élévation douce des graves pour la chaleur et le corps. Un point de départ neutre. |
| **Bass Boost** | Une amplification solide des basses pour le poids et le punch. |
| **Fullness** | Remplit les bas-médiums pour un son plus plein et plus arrondi. |
| **Trim Bass** | Une coupe modeste pour alléger un mixage riche en basses. |
| **Cut Lows** | Une forte coupe pour amincir ou dé-résonner les graves. |
| **Big Bottom** | Une grande amplification des graves pour un poids et un grondement maximaux. |

### High Shelf (contrôle des aigus)

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Fréquence** | Définit le coin au-dessus duquel le shelf prend effet. Tout au-dessus est amplifié ou coupé ensemble. | 1 à 20 kHz (8 kHz) |
| **Gain** | Quelle quantité élever ou baisser les aigus. Positif ajoute de la brillance et de l'air ; négatif lisse et assombrit. | -15 à +15 dB (0) |

| Préréglage | Ce qu'il fait |
|---|---|
| **Presence** | Une élévation douce des aigus pour la clarté et le détail. Un point de départ neutre. |
| **Air** | Ouvre le tout haut pour un son aéré et ouvert. |
| **Bright** | Une forte amplification pour une tonalité nette, brillante et en avant. |
| **Soften** | Une coupe modeste pour enlever le mordant des aigus durs. |
| **Tame Highs** | Une forte coupe pour assombrir et lisser un son trop brillant. |
| **Sparkle** | Une grande amplification du haut du spectre pour un chatoiement et un éclat maximaux. |

### Soft Clip (saturation chaude)

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Drive** | Pousse le signal plus fort dans le waveshaper. De faibles quantités ajoutent une chaleur douce ; de fortes quantités arrondissent les pics en une saturation épaisse et graveleuse. | 0 à 40 dB (0) |

| Préréglage | Ce qu'il fait |
|---|---|
| **Warm** | Une touche de drive pour une chaleur douce, de style analogique. |
| **Drive** | Une saturation notable qui épaissit et colore le son. |
| **Crunch** | Un drive lourd avec un bord croustillant audible. |
| **Fuzz** | Une distortion épaisse et fuzzy. Les pics sont écrasés fort. |
| **Destroy** | Drive maximal. Grain agressif et entièrement saturé. |

### Bit Crusher (rétro lo-fi)

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Profondeur de bits** | Définit combien de bits décrivent chaque échantillon. Moins de bits signifie des paliers plus grossiers et plus de bruit de quantification, pour un son numérique croustillant et graveleux. | 1 à 16 bits (16) |
| **Fréquence d'échantillonnage** | Sous-échantillonne l'audio. À cent pour cent la fréquence est intacte ; baissez-la pour tenir chaque échantillon plus longtemps, ternissant les aigus et ajoutant un bord dur et aliasé. | 1 % à 100 % (100 %) |

| Préréglage | Ce qu'il fait |
|---|---|
| **Vintage** | Une légère baisse de qualité, comme un ancien échantillonneur numérique. |
| **LoFi** | Le lo-fi 8 bits classique, à demi-fréquence. Grainé et rétro. |
| **Crunch** | Un écrasement plus lourd avec un bord croustillant audible. |
| **Gritty** | Grossier et graveleux. Les paliers entre les niveaux sont évidents. |
| **Destroy** | Réduction extrême. Dur, cassé, à peine reconnaissable. |

### Ring Modulator (sons métalliques et robotiques)

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Porteuse** | Définit la fréquence du son par lequel le signal est multiplié. Quelques hertz donnent un tremolo oscillant ; des fréquences plus élevées ajoutent des harmoniques métalliques, cristallines et robotiques. | 1 à 4000 Hz (440) |
| **Mix** | Mélange le son modulé avec l'original. À zéro pour cent vous n'entendez que le signal sec ; à cent pour cent seulement le son entièrement modulé. | 0 % à 100 % (0 %) |

| Préréglage | Ce qu'il fait |
|---|---|
| **Tremolo** | Une porteuse très basse le transforme en tremolo d'amplitude, faisant osciller le volume. |
| **Robot** | Une porteuse médium ajoute des harmoniques métalliques pour un effet classique de voix de robot. |
| **Metallic** | Des harmoniques denses et inharmoniques pour un son dur et métallique. |
| **Bell** | Une porteuse plus haute donne un tintement brillant, de type cloche. |
| **Alien** | Entièrement humide avec une porteuse haute. Extrême, extraterrestre, à peine reconnaissable. |

### Tremolo (oscillation du volume)

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Vitesse** | Définit à quelle vitesse le volume pulse. Les vitesses plus lentes donnent un balancement doux ; les plus rapides donnent un staccato rapide. | 0,1 à 20 Hz (5) |
| **Profondeur** | Définit de combien le volume baisse à chaque pulsation. À zéro pour cent le niveau est stable ; à cent pour cent il descend jusqu'au silence. | 0 % à 100 % (0 %) |

| Préréglage | Ce qu'il fait |
|---|---|
| **Gentle** | Un balancement lent et peu profond. Mouvement subtil sans attirer l'attention. |
| **Classic** | Le tremolo d'ampli classique : une vitesse moyenne et une profondeur modérée. |
| **Deep** | Une pulsation forte et profonde qui descend presque au silence à chaque cycle. |
| **Fast** | Un flottement rapide pour une sensation chatoyante et nerveuse. |
| **Chop** | Rapide et à pleine profondeur. Un hachage dur et saccadé. |

### Delay (écho)

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Temps** | Définit l'intervalle avant chaque écho. Les temps courts donnent un slapback serré ; les temps plus longs espacent davantage les répétitions. | 0,01 à 2 s (0.25) |
| **Feedback** | Définit quelle quantité de chaque écho est réinjectée. Des valeurs basses donnent une seule répétition ; des valeurs plus élevées construisent une longue série d'échos traînante. | 0 à 0,95 (0.4) |
| **Mix** | Mélange les échos avec l'original. À zéro pour cent vous n'entendez que le signal sec ; à cent pour cent seulement les échos. | 0 % à 100 % (0 %) |

| Préréglage | Ce qu'il fait |
|---|---|
| **Slapback** | Un seul écho court, serré contre l'original. Rockabilly et doublage vocal. |
| **Echo** | L'écho classique : une répétition claire avec quelques queues traînantes. |
| **Ping** | Une répétition rapide et rebondissante qui ajoute un mouvement rythmé. |
| **Ambient** | Des répétitions plus longues et plus douces qui se dissolvent en une queue spacieuse. |
| **Dub** | Un feedback élevé pour de longues cascades d'écho dubby. |
| **Cavern** | Des répétitions longues et profondes, comme un son résonnant dans un immense espace. |

### Stereo Width (rétrécir ou élargir)

| Réglage | Ce qu'il fait | Plage (par défaut) |
|---|---|---|
| **Largeur** | Rétrécit ou élargit l'image stéréo. Zéro pour cent replie en mono, cent pour cent la laisse intacte, et des valeurs plus élevées poussent les côtés plus larges. N'affecte que les pistes stéréo sur la cible Tous les canaux. | 0 % à 200 % (100 %) |

| Préréglage | Ce qu'il fait |
|---|---|
| **Wide** | Un élargissement doux qui ouvre l'image stéréo. Un point de départ neutre. |
| **Wider** | Un étalement plus fort pour un champ stéréo grand et immersif. |
| **Max** | Largeur maximale. Très large, mais attention aux problèmes de compatibilité mono. |
| **Narrow** | Rentre les côtés pour une image plus serrée et plus centrée. |
| **Focused** | Presque centré, avec juste un soupçon de stéréo. |
| **Mono** | Entièrement replié en mono. Les deux haut-parleurs jouent le même signal. |

## Comment tout cela fonctionne sous le capot (version simple)

- **Moteurs :** vous en choisissez un dans Paramètres > Lecteur audio > Moteur de lecture : **Standard** (système), **Universal** (FFmpeg) ou **Sound FX** (le **moteur BASS™** d'[Un4seen Developments](https://www.un4seen.com/)). Le moteur que vous choisissez décide quels formats se lisent, et les effets, l'égaliseur et la chaîne DSP ne tournent que dans le moteur Sound FX.
- **Formats :** le moteur BASS™ ajoute FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus et la musique de modules (tracker) en plus des formats système et FFmpeg.
- **Effets :** l'égaliseur, le compresseur et la plupart des effets utilisent les modules d'effets BASS™. Freeverb est la réverbération Freeverb. Chorus, Flanger et Distortion utilisent des effets classiques de style DirectX avec leurs propres réglages.
- **Normalisation du volume :** un niveleur de volume **EBU R128** en direct (la norme de volume utilisée en diffusion et en streaming).
- **Crossfeed :** le crossfeed **bs2b (Bauer)**, exécuté dans le moteur BASS™.
- **Chaîne DSP :** vos blocs personnalisés, appliqués dans l'ordre exact que vous définissez, sur tous les canaux ou juste un côté.
- **Sortie :** vous pouvez régler la fréquence d'échantillonnage, le nombre de canaux et la taille du tampon pour correspondre à votre matériel.

Comme tout cela tourne en direct pendant que la musique joue, les effets :

- Fonctionnent en **temps réel** sur tout, y compris les fichiers cloud, les flux et la musique de modules.
- Ne **modifient ni ne ré-enregistrent jamais** vos fichiers. Désactivez un effet et l'original revient.
- **Mémorisent vos réglages** pour chaque effet.
- Peuvent être **mélangés et combinés** librement, puisque chacun est séparé.

## Recettes simples à essayer

**Écoute au quotidien**

- **Plus de basses, proprement :** Égaliseur > Bass Booster, puis baissez le Préamplificateur de 1 à 2 dB. Ou ajoutez un Low Shelf DSP sur Bass Boost.
- **Volume uniforme sur une liste de lecture mixte :** Normalisation du volume > Standard, plus Compressor > Soft.
- **Polissage global doux :** Compressor > Transparent, plus Normalisation du volume > Light.
- **Voix plus claires :** Égaliseur > Vocal Booster, ou un bloc Peaking DSP sur Vocal Boost.
- **Son plus plein sur les petits haut-parleurs de téléphone :** Égaliseur > Small Speakers.

**Casque**

- **Plus agréable et moins fatigant au casque :** Crossfeed > Chu Moy ou Jan Meier.
- **Son plus large au casque :** Stereo Width DSP > Wide, plus Crossfeed > Chu Moy.
- **Corriger les disques très pannés des années 1960 et 1970 :** Crossfeed > Vintage Stereo.
- **Un peu d'air et d'espace :** Freeverb > Ambience, gardé bas, plus Crossfeed > Subtle.

**Moments calmes et audio parlé**

- **Écoute calme en fin de soirée :** Normalisation du volume > Night, plus Compressor > Late Night.
- **Podcasts et livres audio :** Compressor > Voice / Podcast, plus Égaliseur > Spoken Word.
- **Son le plus fort et le plus uniforme dans une voiture bruyante :** Normalisation du volume > Strong, plus Compressor > Heavy.

**Résoudre des problèmes**

- **Apprivoiser un enregistrement dur et brillant :** Égaliseur > Treble Reducer, ou un bloc Peaking DSP sur Tame Harsh.
- **Supprimer le ronflement électrique :** Chaîne DSP > Notch > Mains Hum 60 (ou Mains Hum 50 en Europe).
- **Basses plus serrées et plus propres :** High Pass DSP > Tighten, pour couper les graves résonnants.
- **Moins de résonance dans un mixage riche en basses :** Low Shelf DSP > Trim Bass, ou Peaking > De-Boom.

**Créatif et amusant**

- **Sensation chaude et spacieuse :** Freeverb > Hall, gardé bas.
- **Guitares rêveuses et spacieuses :** Chorus > Wide, plus Echo > Long.
- **Rétro lo-fi :** Chaîne DSP > Bit Crusher (LoFi) vers Soft Clip (Warm).
- **Mouvement funky sur les morceaux électroniques :** Auto Wah > Funky, ou Phaser > Fast.
- **Balayage classique d'avion à réaction :** Flanger > Jet.

## FAQ

{{% details title="Quel moteur sonore Flacbox utilise-t-il ?" closed="true" %}}
Vous choisissez un Moteur de lecture dans Paramètres > Lecteur audio : Standard (le moteur système d'Apple), Universal (le moteur FFmpeg) ou Sound FX (le moteur BASS™ d'Un4seen Developments, un4seen.com). Le moteur que vous choisissez décide quels formats de fichiers se lisent. Sound FX est celui qui lit des formats supplémentaires comme FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, et la musique MOD ou tracker, et c'est le seul moteur qui fournit les effets en direct, l'égaliseur 10 bandes et la chaîne DSP. Pour utiliser les effets, réglez le Moteur de lecture sur Sound FX.
{{% /details %}}

{{% details title="Flacbox peut-il lire la musique MOD, XM, IT et autre musique tracker ou module ?" closed="true" %}}
Oui. Le moteur BASS™ a un lecteur de modules intégré qui charge les fichiers MOD, XM, IT, S3M, MTM, UMX et MO3 et reconstruit le morceau en direct à partir de ses motifs et sons d'instruments, comme la musique tracker est censée se lire. Les lecteurs iPhone habituels ne peuvent pas faire cela. Les effets et l'égaliseur fonctionnent aussi sur la musique de modules.
{{% /details %}}

{{% details title="Flacbox prend-il en charge le DSD et les fichiers haute résolution ?" closed="true" %}}
Oui. Flacbox lit les fichiers DSD (DSF et DFF) via le moteur BASS™ en utilisant le DSD sur PCM pour qu'ils fonctionnent sur du matériel de sortie normal, plus FLAC, WavPack, Monkey's Audio (APE), Musepack et TrueAudio pour la lecture sans perte.
{{% /details %}}

{{% details title="Quels effets sonores Flacbox possède-t-il ?" closed="true" %}}
Un égaliseur 10 bandes, la Normalisation du volume, le Compressor, le Freeverb, l'Auto Wah, le Phaser, le Flanger, l'Echo, le Chorus, la Distortion, le Rotate et le Crossfeed, plus une chaîne DSP à construire soi-même avec filtres, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay et largeur stéréo. Chacun est séparé et peut être combiné avec les autres.
{{% /details %}}

{{% details title="Qu'est-ce qu'un préréglage ?" closed="true" %}}
Un préréglage est un réglage prêt à l'emploi pour un effet. Au lieu de déplacer les curseurs vous-même, vous touchez un préréglage et le son change en conséquence. Chaque effet dans Flacbox a plusieurs préréglages, et ce guide indique ce que chacun fait. Si vous déplacez un curseur après avoir choisi un préréglage, l'effet affiche « Manuel » pour vous indiquer qu'il utilise désormais vos propres valeurs.
{{% /details %}}

{{% details title="Comment ouvrir les effets audio dans Flacbox ?" closed="true" %}}
Ouvrez le lecteur Lecture en cours, touchez le bouton ⋯ (Plus) et choisissez Effets audio. Ou allez dans Paramètres > Lecteur audio > Effets audio. Touchez un effet, activez son interrupteur, et choisissez un préréglage, ou ouvrez les curseurs pour un réglage fin.
{{% /details %}}

{{% details title="Où se trouve l'égaliseur, et quels sont les meilleurs réglages ?" closed="true" %}}
Allez dans Paramètres > Lecteur audio > Égaliseur audio. Il a 10 bandes de 32 Hz à 16 kHz, chacune de -12 à +12 dB, plus un Préamplificateur de -24 à +24 dB et 22 préréglages. Pour plus de basses, utilisez Bass Booster. Pour des voix plus claires, utilisez Vocal Booster ou Pop. Pour un son plus brillant, utilisez Treble Booster. Puis ajustez les bandes individuelles à votre goût.
{{% /details %}}

{{% details title="Comment amplifier les basses dans Flacbox ?" closed="true" %}}
Deux méthodes faciles. Dans l'Égaliseur audio, choisissez Bass Booster (ou montez les bandes 32 Hz et 64 Hz de quelques dB). Ou, dans le Traitement du signal, ajoutez un bloc Low Shelf réglé sur Bass Boost. Dans les deux cas, baissez le Préamplificateur ou ajoutez un bloc Gain de 1 à 2 dB pour que les basses restent propres et ne distordent pas.
{{% /details %}}

{{% details title="Quel préréglage d'égaliseur convient le mieux à ma musique ?" closed="true" %}}
Rock et Electronic ajoutent de l'énergie avec des graves et des aigus puissants. Acoustic, Jazz et Classical restent chauds et naturels. Pop et Vocal Booster poussent les voix en avant. Bass Booster et Hip-Hop ajoutent du poids. Deep et Loudness sonnent plus plein à faible volume. Commencez par celui qui correspond à votre genre, puis ajustez finement.
{{% /details %}}

{{% details title="Qu'est-ce que la Normalisation du volume, et en quoi diffère-t-elle de ReplayGain ?" closed="true" %}}
Elle fait jouer chaque morceau à peu près au même volume. Elle mesure le volume réel à l'aide de la norme EBU R128 (en LUFS, comme les services de streaming) et ajuste chaque morceau vers votre cible, avec une limite de gain max. Contrairement à ReplayGain, elle n'a besoin d'aucune balise dans vos fichiers et fonctionne sur n'importe quelle source, en direct, sans modifier l'audio. Préréglages : Light, Standard, Strong et Night.
{{% /details %}}

{{% details title="Qu'est-ce que le Crossfeed, et devrais-je l'utiliser ?" closed="true" %}}
Crossfeed mélange un peu des canaux gauche et droit ensemble pour que le casque ressemble davantage à de vrais haut-parleurs et moins à un son coincé dans votre tête. C'est uniquement pour le casque, donc désactivez-le pour les haut-parleurs. Flacbox utilise la méthode bs2b (Bauer), avec des préréglages comme Chu Moy et Jan Meier.
{{% /details %}}

{{% details title="Quelle est la différence entre le Compressor et la Normalisation du volume ?" closed="true" %}}
La Normalisation du volume fait correspondre le volume entre différentes chansons. Le Compressor égalise les parties fortes et faibles à l'intérieur d'une seule chanson. Ils résolvent des problèmes différents et fonctionnent bien ensemble, surtout dans une voiture ou un endroit bruyant.
{{% /details %}}

{{% details title="Qu'est-ce que la chaîne de Traitement du signal (DSP) ?" closed="true" %}}
C'est un rack à construire soi-même dans Paramètres > Lecteur audio > Traitement du signal. Ajoutez des blocs comme des filtres, des shelves, du gain, du soft clip, du bit crusher, du ring modulator, du tremolo, du delay et de la largeur stéréo, mettez-les dans n'importe quel ordre, activez ou désactivez chacun, et dirigez la chaîne vers tous les canaux, la gauche ou la droite. Comme l'ordre compte, vous pouvez concevoir exactement le son que vous voulez.
{{% /details %}}

{{% details title="Quelle est la différence entre l'Égaliseur, les effets et la chaîne DSP ?" closed="true" %}}
L'Égaliseur est un simple contrôle de tonalité à 10 bandes. Les Effets audio sont des outils prêts à l'emploi (compresseur, réverbération, écho, etc.) avec des préréglages. La chaîne DSP est l'endroit où vous construisez votre propre ordre d'effets à partir de blocs individuels. Vous pouvez exécuter les trois en même temps.
{{% /details %}}

{{% details title="Les effets modifient-ils ou endommagent-ils mes fichiers de musique ?" closed="true" %}}
Non. Tout est appliqué en direct pendant que la musique joue. Vos fichiers ne sont jamais modifiés ni ré-enregistrés. Désactivez un effet et le son original revient aussitôt.
{{% /details %}}

{{% details title="Puis-je utiliser plusieurs effets en même temps ?" closed="true" %}}
Oui. Chaque effet a son propre interrupteur et il n'y a pas d'interrupteur principal, donc n'importe quelle combinaison fonctionne. Par exemple, Normalisation du volume plus Compressor pour une écoute uniforme, ou Freeverb plus Crossfeed au casque, avec l'égaliseur par-dessus.
{{% /details %}}

{{% details title="Pourquoi les réglages de l'effet sont-ils grisés ?" closed="true" %}}
L'effet est désactivé. Activez son interrupteur en haut de l'éditeur pour utiliser les réglages. Chaque effet est désactivé par défaut.
{{% /details %}}

{{% details title="Que signifie l'étiquette Manuel ?" closed="true" %}}
Cela signifie que vous avez éloigné un curseur d'un préréglage, donc l'effet utilise désormais vos propres valeurs personnalisées au lieu d'un préréglage nommé. Chaque curseur a un bouton de réinitialisation, et choisir à nouveau un préréglage remplace vos valeurs manuelles.
{{% /details %}}

{{% details title="Puis-je enregistrer et partager mes préréglages d'égaliseur ?" closed="true" %}}
Oui. Outre les 22 préréglages intégrés, vous pouvez créer les vôtres, les réorganiser, et les exporter ou importer pour déplacer vos réglages vers un autre appareil.
{{% /details %}}

{{% details title="Les effets fonctionnent-ils avec CarPlay, le streaming et la lecture en arrière-plan ?" closed="true" %}}
Oui. Les effets tournent dans le moteur BASS™, donc ils s'appliquent aux fichiers locaux, aux disques cloud, aux serveurs multimédias, aux flux et à la musique de modules, et ils continuent de fonctionner pendant CarPlay et la lecture en arrière-plan.
{{% /details %}}

{{% details title="Puis-je changer la qualité de sortie audio ?" closed="true" %}}
Oui. Dans Paramètres > Lecteur audio, vous pouvez régler la fréquence d'échantillonnage de sortie, le nombre de canaux et la taille du tampon pour correspondre à votre casque, vos haut-parleurs ou votre DAC.
{{% /details %}}

{{% details title="Quelle est une bonne configuration de départ pour le casque ?" closed="true" %}}
Activez la Normalisation du volume (Standard), ajoutez un Compressor léger (Soft), choisissez un préréglage d'égaliseur que vous aimez, et activez le Crossfeed (Chu Moy ou Jan Meier). Laissez la réverbération, l'écho et la distortion désactivés à moins que vous ne vouliez un son créatif.
{{% /details %}}

---

*BASS est une marque déposée d'Un4seen Developments Ltd. Voir [un4seen.com](https://www.un4seen.com/). Crossfeed utilise l'algorithme bs2b (Bauer stereophonic-to-binaural) ; voir la [page du projet bs2b](https://bs2b.sourceforge.net/).*
