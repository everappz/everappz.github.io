---
title: "Com obtenir metadades, icones i captures de pantalla de l'App Store gratis"
date: 2026-06-13
description: "Guia pas a pas per obtenir les metadades, la icona, les captures de pantalla i els detalls localitzats de l'App Store de qualsevol aplicació iOS amb AppLookup.pro, una eina de navegador gratuïta basada en l'API oficial d'iTunes Search."
keywords: [
  "metadades App Store", "obtenir dades App Store", "descarregar icona App Store",
  "descarregar captures App Store", "eina de cerca App Store", "iTunes Search API",
  "extractor de metadades d'apps", "metadades d'app iOS", "eina gratuïta App Store API",
  "descarregar icona d'app alta resolució", "recerca de competidors App Store",
  "dades App Store localitzades", "cerca per país App Store", "eina ASO gratuïta"
]
tags: [
  "Metadades App Store", "App Lookup", "iTunes Search API",
  "Descàrrega d'icones d'apps", "Captures d'apps", "Recerca ASO"
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

## Obtén dades de l'App Store en segons

**Versió curta:** [AppLookup.pro](https://applookup.pro) és una eina gratuïta que extreu dades públiques de qualsevol app per a iOS, iPadOS, macOS o tvOS. Obtens el títol, la descripció, què hi ha de nou, la versió, el preu, les valoracions, la icona de l'app, les captures de pantalla, els dispositius compatibles i la resposta sense processar de l'API d'iTunes. Cada camp té un botó per copiar amb un sol toc. Obre el lloc, enganxa un enllaç de l'App Store o escriu el nom de l'app i ja tens les dades.

Utilitza-la per a:

- **Recerca ASO.** Veure com les apps més importants escriuen els seus títols, subtítols, descripcions i paraules clau.
- **Seguiment de la competència.** Comprovar actualitzacions de versió, valoracions i preus a diferents mercats.
- **Descàrrega de recursos.** Desar la icona oficial de l'app i les captures a mida completa en un sol ZIP.
- **Comprovació de localització.** Comparar la descripció, què hi ha de nou i captures de pantalla a més de 40 països de l'App Store.
- **Proves d'API.** Copiar el JSON sense processar de l'API d'iTunes Search directament al codi o a Postman.

## Què és AppLookup.pro?

[AppLookup.pro](https://applookup.pro) és una eina gratuïta de cerca a l'App Store basada en el navegador. S'executa íntegrament al teu dispositiu. Cada resultat prové directament de l'[API oficial d'iTunes Search](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) d'Apple. Sense scraping. Sense registre. Sense seguiment.

### Què obtens

- **Cerca per nom de l'app o URL de l'App Store.** L'autocompletat mostra resultats en directe mentre escrius.
- **Més de 40 botigues per país.** Canvia entre EUA, Regne Unit, Japó, Alemanya, França, Brasil i molts més.
- **Metadades completes.** Títol, subtítol, desenvolupador, Bundle ID, versió, preu, mida del fitxer, valoracions, data de llançament, classificació de contingut, idiomes i dispositius compatibles.
- **Recursos d'alta resolució.** Icones d'apps i captures de pantalla per a iPhone, iPad, macOS i Apple TV.
- **Descàrrega massiva en ZIP.** Obtén totes les icones o totes les captures en un sol arxiu.
- **JSON sense processar de l'API d'iTunes.** La resposta exacta d'Apple, llesta per copiar.
- **Botons de còpia a cada camp.** Un sol toc posa el valor al porta-retalls.

## Com utilitzar AppLookup.pro pas a pas

### Pas 1. Introdueix el nom de l'app o enganxa un URL de l'App Store

Obre [applookup.pro](https://applookup.pro) i comença a escriure el nom de l'app. L'autocompletat mostra resultats en directe de l'App Store mentre escrius.

També pots enganxar un enllaç directe de l'App Store com ara `https://apps.apple.com/us/app/instagram/id389801252` o només l'ID de l'app. L'eina n'extreu l'ID per tu. També admet URL de redirecció de Google.

![Introdueix el nom d'una app o un URL de l'App Store a AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Pas 2. Obtén la informació de l'app i descarrega la icona

Fes clic a **Lookup** o prem Enter. L'eina crida l'API oficial d'iTunes Search i mostra la icona de l'app, el nom del desenvolupador, la valoració, la versió i el preu en menys d'un segon.

Desplaça't fins a la secció **App Icon**. Cada mida d'icona que retorna Apple apareix com una targeta. Cada targeta té:

- **Direct Link.** Obre la imatge a mida completa en una pestanya nova.
- **Download.** Desa el fitxer a l'ordinador.

Fes servir **Download All Icons (ZIP)** per obtenir totes les mides d'icona en un sol arxiu. El mateix passa amb les captures de pantalla: cada secció de plataforma té el seu propi botó **Download All (ZIP)**.

![Descarrega icones i captures d'apps des d'AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Pas 3. Llegeix els detalls de l'app i copia qualsevol camp

Desplaça't fins a **App Details**. Veuràs el Bundle ID, la versió, el preu, la mida del fitxer, l'SO mínim, la data de llançament, la data de l'última actualització, la classificació de contingut, els gèneres, els IDs de gènere, els idiomes, el venedor, l'ID d'artista i l'ID de track.

Toca el botó **Copy** de qualsevol targeta. El valor passa al porta-retalls i el botó mostra una marca verda 'Copied'.

El mateix funciona per a **Description**, **What's New** i **Supported Devices**. Aquestes seccions es poden desplaçar, així que pots llegir tot el text sense perdre la posició, i el botó Copy posa tot el camp al porta-retalls.

![Visualitza tots els detalls de l'App Store i copia qualsevol camp amb un sol toc](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Pas 4. Visualitza la resposta sense processar de l'App Store API

Necessites el JSON exacte que retorna Apple? Desplaça't fins a **Raw API Response**. La càrrega útil completa de l'API d'iTunes Search es mostra en un visor desplaçable amb un botó **Copy** a la part superior. Un sol toc copia tot l'objecte JSON.

L'**iTunes Lookup URL** es mostra just a sobre. Enganxa'l a Postman, curl o al teu navegador per repetir la mateixa sol·licitud.

![Visualitza i copia la resposta JSON sense processar de l'API d'iTunes Search](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Pas 5. Canvia el país per veure la versió localitzada

Les metadades de l'App Store canvien segons el país. La mateixa app sovint té un títol, subtítol, descripció, captures i preu diferents a cada mercat.

Tria un país del menú desplegable de la part superior. L'URL del quadre d'entrada s'actualitza automàticament. Fes clic a **Lookup** una altra vegada per tornar a obtenir l'app en aquell mercat.

Aquesta és la manera més ràpida de comprovar com un competidor presenta la seva app al Japó, Alemanya, Brasil o qualsevol dels més de 40 països compatibles.

![Canvia les botigues per país per veure metadades localitzades de l'App Store](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Pas 6. Copia les metadades localitzades

Un cop carregat el resultat del país, cada camp funciona igual. Toca **Copy** a la descripció, què hi ha de nou, el nom de l'app, el desenvolupador, el Bundle ID o qualsevol targeta de detall per capturar el text localitzat.

Així és fàcil crear fulls de càlcul de comparació en paral·lel o alimentar les còpies localitzades a la revisió de traducció.

![Copia la descripció i les metadades localitzades de l'App Store amb un sol toc](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Qui utilitza AppLookup.pro

- **Desenvolupadors indie** que fan recerca ASO abans d'un llançament.
- **Equips d'ASO i màrqueting** que segueixen les actualitzacions i els preus de la competència.
- **Dissenyadors** que necessiten la icona oficial d'alta resolució i les captures per a press kits i casos d'estudi.
- **Equips de localització** que auditen quins mercats estan coberts i on encara es publica el text per defecte en anglès.
- **Enginyers de backend i QA** que proven integracions amb l'API d'iTunes Search sense escriure un scraper.
- **Redactors i blogaires** que necessiten la icona oficial de l'app i unes quantes captures per a un article.

## Privadesa i avís legal

AppLookup.pro s'executa al teu navegador. No hi ha inici de sessió. No hi ha seguiment. No hi ha registre al servidor de les apps que cerques. Les sol·licituds es fan directament des del teu navegador a l'[API d'iTunes Search](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) d'Apple.

Aquesta eina és **només per a finalitats educatives i de recerca**. Totes les dades s'obtenen de l'API pública oficial d'Apple i continuen sent propietat d'Apple Inc. i dels editors de les apps indicades. L'ús de l'eina està subjecte als [Termes i Condicions dels Serveis Multimèdia d'Apple](https://www.apple.com/legal/internet-services/terms/site.html). Respecta els límits de velocitat d'Apple i no redistribueixis recursos amb drets d'autor.

## Prova-ho ara

No necessites una clau d'API, un compte de desenvolupador ni un pla de pagament per inspeccionar dades de l'App Store. Obre [applookup.pro](https://applookup.pro), enganxa qualsevol URL de l'App Store i tindràs les metadades, les icones i el JSON sense processar en segons.

## Codi obert

AppLookup.pro és de codi obert. Els informes d'errors, les addicions de països i les pull requests són benvinguts.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro a GitHub" icon="github" tag="codi obert" >}}
{{< /cards >}}

---

## Preguntes freqüents

{{% details title="AppLookup.pro és realment gratuït?" closed="true" %}}
Sí. AppLookup.pro és 100 per cent gratuït i de codi obert. S'executa al teu navegador. No hi ha registre, ni nivell de pagament, ni cap límit d'ús més enllà dels propis límits de l'API d'iTunes Search d'Apple.
{{% /details %}}

{{% details title="D'on provenen les dades?" closed="true" %}}
Cada resultat s'obté en temps real de l'[API oficial d'iTunes Search](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) d'Apple. L'eina no fa scraping de pàgines de l'App Store i no guarda en memòria cau les respostes en cap servidor.
{{% /details %}}

{{% details title="Puc descarregar la icona de l'app en alta resolució?" closed="true" %}}
Sí. La secció **App Icon** mostra cada URL d'icona que retorna Apple. Cada targeta té un botó Direct Link i un Download, i el botó Download All Icons ZIP les empaqueta totes en un sol arxiu.
{{% /details %}}

{{% details title="Puc descarregar totes les captures de pantalla de l'App Store de cop?" closed="true" %}}
Sí. Cada secció de captures de pantalla (iPhone, iPad, macOS i Apple TV) té un botó **Download All (ZIP)** que agrupa totes les captures a resolució completa.
{{% /details %}}

{{% details title="Com puc veure com es veu una app en un altre país?" closed="true" %}}
Tria un país al menú desplegable de la part superior de la pàgina. S'admeten més de 40 botigues. Fes clic a **Lookup** una altra vegada i l'eina torna a obtenir l'app per a aquell país, mostrant el títol, descripció, captures, què hi ha de nou i preu localitzats.
{{% /details %}}

{{% details title="Puc copiar camps individuals com el Bundle ID o la data de llançament?" closed="true" %}}
Sí. Cada camp de text del resultat té el seu propi botó Copy: nom de l'app, desenvolupador, descripció, què hi ha de nou, Bundle ID, versió, preu, mida del fitxer, SO mínim, data de llançament, classificació de contingut, idiomes, dispositius compatibles i JSON sense processar.
{{% /details %}}

{{% details title="AppLookup.pro funciona amb qualsevol app iOS?" closed="true" %}}
Funciona amb qualsevol app que estigui llistada públicament a almenys un país de l'App Store i sigui retornada per l'API d'iTunes Search. Les apps no llistades, retirades o distribuïdes via empresa no apareixeran.
{{% /details %}}

{{% details title="Admet apps de macOS i Apple TV?" closed="true" %}}
Sí. Si l'app té captures de pantalla de macOS o Apple TV a la resposta de l'API d'iTunes Search, AppLookup.pro les mostra al seu propi panell desplaçable amb botons de descàrrega.
{{% /details %}}

{{% details title="Puc utilitzar el JSON sense processar al meu propi codi?" closed="true" %}}
Sí. La secció Raw API Response mostra el JSON exacte que retorna Apple. Copia'l a Postman, a un test unitari o a un pipeline de backend. Respecta els termes de l'API d'Apple i uns límits de velocitat raonables.
{{% /details %}}

{{% details title="És segur enganxar URLs de l'App Store a l'eina?" closed="true" %}}
Sí. L'URL es processa al teu navegador. L'única crida de xarxa sortint és la consulta a l'API d'iTunes Search d'Apple.
{{% /details %}}

{{% details title="Quina és la diferència entre AppLookup.pro i AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) serveix per llegir metadades de l'App Store de qualsevol app publicada: recerca de competència, descàrrega de recursos, comprovacions de localització. [AppKeywords.pro](https://appkeywords.pro) serveix per escriure metadades de l'App Store per a la teva pròpia app: optimització de títol, subtítol i paraules clau amb suport per a Fastlane. Les dues eines funcionen molt bé conjuntament.
{{% /details %}}
