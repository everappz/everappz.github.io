---
title: "Biblioteca musical"
date: 2020-02-01
description: "Aprèn a construir, organitzar i sincronitzar la teva biblioteca musical a Flacbox a iPhone, iPad i Mac. Afegeix pistes manualment o sincronitza des de serveis al núvol, gestiona metadades, portades d'àlbum, llistes de reproducció, favorits, recents i marcadors. Inclou suport d'àudio Hi-Res, editor d'etiquetes MusicBrainz, sincronització en línia i offline, i opcions de personalització."
keywords: [
  "biblioteca musical Flacbox", "sincronitzar música des del núvol", "organitzar metadades de música",
  "editar etiquetes d'àudio Flacbox", "sincronització de música offline", "importar música local",
  "gestió de llistes de reproducció Flacbox", "cerca de portades d'àlbum Flacbox",
  "metadades de música iPhone", "guia de l'app Flacbox",
  "Flacbox MusicBrainz", "normalitzar etiquetes Flacbox",
  "biblioteca de música hi-res Flacbox", "biblioteca FFmpeg Flacbox",
  "àlbums en solitari Flacbox", "vista de compositor Flacbox"
]
tags: ["música", "guia", "flacbox", "biblioteca"]
readingTime: 11
---


Gestionar la teva biblioteca musical és molt fàcil amb Flacbox, on pots organitzar sense esforç totes les teves pistes — FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE locals i desenes d'altres formats — en una sola col·lecció cercable. Tens dues opcions per construir la teva biblioteca musical: addició manual (tries exactament el que s'afegeix) o sincronització automàtica (Flacbox escaneja carpetes al núvol designades i afegeix nous fitxers automàticament quan apareixen).

{{< cards cols="1">}}
  {{< card title="" subtitle="Vista d'àlbums de la biblioteca musical de Flacbox" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Addició Manual

Per afegir pistes manualment, toca la icona **Afegir música** a la cantonada superior esquerra i tria carpetes o fitxers d'un servei d'emmagatzematge al núvol connectat o fitxers del teu dispositiu. Quan afegeixes pistes a la biblioteca, només es creen enllaços a aquelles pistes — els fitxers reals romanen a les seves ubicacions originals per estalviar espai de disc valuable. Si vols tenir pistes disponibles offline, pots usar l'acció Descarregar del menú d'opcions o activar el Mode offline per a llistes de reproducció i col·leccions de pistes.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Afegir cançons a la biblioteca musical" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

També pots arrossegar i deixar anar fitxers a la biblioteca a la versió Mac, o usar **Obrir fitxers…** / **Obrir carpeta…** del selector de fitxers del sistema a iPhone i iPad.

## Continuar Reproducció

Restaura la cua del reproductor d'àudio de l'última posició guardada si aquesta funció está activada als ajustos de l'aplicació. Activa tant **Desar l'estat del reproductor d'àudio** com **Desar la posició de reproducció** a Configuració → Reproductor d'àudio → General per a la millor experiència. Un cop activat, apareix un botó **Continuar reproducció** a la part superior de cada carpeta, àlbum, artista, gènere i pantalla de llista de reproducció — toca'l per tornar directament a la pista i posició exactes on ho vas deixar.

## Ubicacions

Totes les pistes de la teva biblioteca estan agrupades de manera reflexiva per tipus de font i etiquetes de música. Pots filtrar cançons per ubicació usant el botó **Més accions** a la cantonada superior dreta i seleccionant **Filtre**.

### Música en línia

Aquesta secció mostra música dels teus serveis d'emmagatzematge al núvol connectats. Les pistes aquí es reprodueixen per demanda; res ocupa emmagatzematge local fins que descarregues o actives el mode offline explícitament.

### Fitxers en aquesta aplicació

Aquí pots trobar música disponible per a reproducció offline, provinent dels teus fitxers locals. Inclou fitxers al directori Documents de l'app — qualsevol cosa que hagis descarregat, transferit via Wi-Fi Drive o importat a través de Compartició de fitxers Finder.

### Fitxers en aquest iPhone / iPad / Mac

Aquesta categoria inclou música importada a l'aplicació des del teu dispositiu, afegida a través del diàleg del sistema **Obrir fitxers…**. Els fitxers originals romanen a la seva ubicació original; Flacbox només manté un enllaç a ells.

## Categories

Quan afegeixes pistes a la teva biblioteca musical, l'app llegeix automàticament les seves etiquetes d'àudio i les organitza en categories com Cançons, Cançons no reproduïdes, Àlbums, Artistes d'àlbum, Artistes, Gèneres i Compositors.

## Agrupació per etiquetes

Aquestes categories t'ajuden a organitzar les pistes per etiquetes de música. Quan afegeixes pistes a la biblioteca musical, l'app llegeix les seves metadades i les agrupa per aquestes categories. Si no veus tots els teus àlbums, assegura't que l'app ha escanejat cada pista. Pots comprovar el progrés de l'escaneig a Configuració → Biblioteca musical → Lectura de metadades → Nombre de fitxers processats a la biblioteca musical. Per als fitxers locals, també pots tornar a escanejar les carpetes offline a Configuració → Biblioteca musical → Sincronització de carpetes offline → Inici de l'escaneig de carpetes locals. Després que el lector de metadades completi totes les operacions, veuràs les categories següents a la teva biblioteca musical:

- **Cançons** — totes les cançons agrupades per l'etiqueta TRACK_TITLE. Pots comprovar l'ordre de classificació usant el menú Més accions a la cantonada superior dreta.
- **Cançons no reproduïdes** — totes les cançons que no s'han reproduït mai.
- **Àlbums** — cançons agrupades per l'etiqueta ALBUM_NAME, ignorant les etiquetes d'artista, artista d'àlbum i compositor. Si tens diversos àlbums amb el mateix nom però d'artistes diferents, considera usar la classificació d'Àlbums exclusius descrita a continuació.
- **Artistes d'àlbum** — cançons agrupades només per l'etiqueta ALBUM_ARTIST_TAG. Útil per mantenir les compilacions i col·laboracions netament separades del treball en solitari.
- **Artistes** — cançons agrupades només per l'etiqueta ARTIST_TAG.
- **Gèneres** — cançons agrupades per l'etiqueta GENRE.
- **Compositors** — cançons agrupades per l'etiqueta COMPOSER — imprescindible per a biblioteques de música clàssica on el 'compositor' és l'eix de navegació principal.

## Favorits

Pots marcar cançons com a favorits a la pantalla del reproductor d'àudio o usant el menú d'opcions. Els favorits apareixen a la seva pròpia secció perquè puguis trobar-los amb un sol toc.

## Recents

Aquesta secció mostra totes les pistes reproduïdes recentment. Pots personalitzar quants elements manté la llista de recents a Configuració → Biblioteca → Recents → Canviar la mida de la llista, i exportar la llista a M3U / CSV / TXT per fer una còpia de seguretat del teu historial d'escolta.

## Marcadors

Pots crear marcadors d'àudio mentre una cançó s'està reproduint i gestionar-los en aquesta pantalla — perfecte per a audiollibres, llargues mescles, conferències o només per marcar l'estribillo d'una cançó preferida. Hi ha instruccions detallades sobre el treball amb marcadors d'àudio disponibles [aquí](/docs/guide/evermusic/evermusic-guide-music-library).

## Barra d'Eines Superior

Situada just per sota de la barra de navegació, la barra d'eines superior ofereix diverses accions convenients: Cerca, Reproduir tot, Reproduir tot aleatori i Continuar reproducció. Pots revelar o ocultar aquesta barra amb un simple gest de lliscar cap avall.

## Cerca

La funció de cerca et permet localitzar una pista, artista, àlbum o gènere específics dins de la teva biblioteca musical. Dins de la pantalla de Cerca, tens accés a les accions Ordenar, Filtre i vista de Quadrícula / Llista. La cerca s'executa localment contra la base de dades de la biblioteca musical, de manera que funciona completament offline i retorna resultats mentre escrius.

{{< cards cols="1">}}
  {{< card title="" subtitle="Cerca de la biblioteca musical de Flacbox" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Menú d'Opcions

Cada cançó de la teva biblioteca musical té un menú amb més accions, accessible tocant el botó de tres punts al costat del títol de la cançó. Aquestes accions varien depenent de si és una cançó individual o part d'una col·lecció.

### Per a Cançons Individuals

- **Reproduir a continuació** — afegeix la cançó a la part superior de la cua del reproductor.
- **Reproduir més tard** — afegeix la cançó a la part inferior de la cua del reproductor.
- **Afegir a la llista de reproducció** — afegeix la cançó a una llista de reproducció.
- **Afegir als favorits** — marca la cançó com a favorita per a un accés ràpid.
- **Descarregar** — desa la cançó als fitxers locals. Apareix a la pestanya **Fitxers locals** i a la secció **Música offline**.
- **Editar etiquetes d'àudio** — obre l'editor d'etiquetes d'àudio integrat per corregir metadades que falten; tingues en compte que això alterarà la cançó al teu emmagatzematge.
- **Mostrar a la carpeta** — revela la carpeta on s'emmagatzema el fitxer d'àudio.
- **Mostrar al Finder** — per als fitxers importats des del teu Mac, aquesta acció revela la carpeta on es troba el fitxer d'àudio al Mac.
- **Obrir amb** — exporta el fitxer d'àudio a una altra app.
- **Eliminar del servei al núvol** — elimina el fitxer tant de la biblioteca musical com de l'emmagatzematge al núvol. **Aquesta acció és irreversible.**
- **Eliminar de la biblioteca musical** — elimina la cançó de la teva biblioteca musical, però el fitxer roman a l'emmagatzematge. Si la sincronització automàtica está activada i el fitxer existeix a l'emmagatzematge remot, tornarà a aparèixer a la teva biblioteca després d'una operació de sincronització.

### Per a Col·leccions de Cançons

Per a col·leccions de cançons com Àlbums, Artistes, Gèneres o Compositors, el menú d'opcions inclou les accions següents.

- **Reproduir tot** — substitueix la cua del reproductor per cançons de la col·lecció seleccionada.
- **Reproduir a continuació** — afegeix les cançons d'aquesta col·lecció a la part superior de la cua del reproductor.
- **Reproduir més tard** — afegeix les cançons d'aquesta col·lecció a la part inferior de la cua del reproductor.
- **Afegir a la llista de reproducció** — inclou les cançons d'aquesta col·lecció en una llista de reproducció, amb l'opció de crear-ne una de nova.
- **Activar el mode fora de línia** — descarrega les cançons d'aquesta col·lecció als fitxers locals. Els fitxers apareixen a la pestanya **Fitxers locals** i a la secció **Música offline**. Si s'afegeixen nous elements a la col·lecció al servidor, es descarregaran automàticament.
- **Editar imatge** — canvia la portada de l'àlbum per a la col·lecció de cançons.
- **Afegir a l'arxiu** — agrupa tota la col·lecció en un sol fitxer ZIP per a una còpia de seguretat o transferència fàcil (funció Premium).
- **Exportar llista de cançons** — exporta la col·lecció a M3U, CSV o TXT per usar-la en altres reproductors o per arxivar.
- **Eliminar de la biblioteca musical** — elimina la col·lecció de cançons de la teva biblioteca musical. Aquesta acció no elimina els fitxers reals de l'emmagatzematge. Si la sincronització automàtica está activada i els fitxers existeixen a l'emmagatzematge remot, tornaran a aparèixer a la teva biblioteca després d'una operació de sincronització.

## Mode de Selecció

Pots activar el mode de selecció usant el botó Més accions a la cantonada superior dreta. En aquest mode, pots seleccionar múltiples pistes alhora i realitzar accions per lots — afegir a la llista de reproducció, marcar com a favorit, eliminar de la biblioteca, descarregar i més.

## Detall de l'Àlbum

Quan obres les seccions Artista, Artista d'àlbum o Compositor, pots veure un commutador per a Cançons / Tots els àlbums / Àlbums exclusius / Àlbums en solitari.

- **Cançons** — mostra totes les cançons on aquest Artista / Artista d'àlbum / Compositor apareix a les etiquetes d'àudio.
- **Tots els àlbums** — mostra àlbums de recopilació i tots els àlbums on l'artista és present.
- **Àlbums exclusius** — mostra àlbums on l'artista especificat és l'únic artista amb aquell nom d'àlbum.
- **Àlbums en solitari** — mostra àlbums on només apareixen pistes de l'artista especificat, fins i tot si altres artistes tenen àlbums amb el mateix nom.

Això és especialment útil per netejar les compilacions 'Artistes diversos' desordenades en biblioteques grans.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de detall d'àlbum de Flacbox" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Configuració

Toca Més accions → Configuració per configurar les preferències de la teva biblioteca musical.

### Lectura de Metadades

Quan afegeixes pistes a la biblioteca, el lector de metadades comença a treballar. Aquest procés en segon pla llegeix totes les metadades de les teves pistes i les organitza per Artista, Àlbum, Gènere i Compositor. Pots ajustar la velocitat de lectura de metadades per carregar dades més ràpid — tingues en compte que una lectura més ràpida usa més energia. També pots desactivar el lector de metadades completament i mostrar noms de fitxers en lloc de la informació d'etiquetes.

Importantment, el lector de metadades només actualitza les metadades a la teva biblioteca musical i no altera els fitxers emmagatzemats al teu compte al núvol o emmagatzematge local. Si desitges editar metadades per a fitxers d'àudio, pots fer-ho usant l'editor d'etiquetes integrat, que pots activar des de l'acció corresponent al menú d'opcions.

### Modes Disponibles per al Lector de Metadades

- **Desactivat** — el lector de metadades está apagat i es mostren noms de fitxers en lloc de dades d'etiquetes d'àudio.
- **Cançó actual** — l'aplicació llegeix metadades només per a la cançó que s'está reproduint. Usa aquesta opció si tens una connexió de xarxa lenta per evitar que el lector de metadades enviï moltes peticions al servidor al núvol, cosa que pot causar interrupcions de la reproducció.
- **Cua de reproducció** — l'app llegeix metadades per a totes les cançons a la cua del reproductor d'àudio.
- **Biblioteca** — l'app llegeix metadades per a totes les cançons de la biblioteca musical.

Quan el commutador **Lectura de metadades en segon pla** está activat, el lector de metadades continua treballant en mode segon pla. Tingues en compte que si l'app consumeix molta energia durant la reproducció d'àudio, el sistema operatiu iOS pot suspendre-la.

Per tant, si tens una gran col·lecció de música, és aconsellable usar la versió d'escriptori de l'aplicació per a la sincronització de metadades. Pots usar la funció de Còpia de seguretat i Restauració als ajustos de l'app per transferir la biblioteca sincronitzada de l'escriptori al mòbil.

Quan l'opció **Normalitzar codificació de metadades** está activada, l'app normalitza automàticament la codificació de metadades per a totes les cançons de la biblioteca musical. Això corregeix problemes on la codificació de les etiquetes d'àudio está trencada (com ara després d'editar fitxers en un Windows PC) i evita que apareguin caràcters incorrectes a la informació de la pista.

L'acció **Tornar a carregar metadades** marca cada fitxer de la teva biblioteca musical com que li falten metadades, desencadenant que el lector de metadades actualitzi cada registre.

Toca **Inici de la lectura de metadades** per iniciar el lector manualment. El progrés de l'operació es mostra a continuació.

### Sincronització en línia

La sincronització de música en línia automàtica et permet afegir pistes dels serveis al núvol connectats a la biblioteca musical automàticament. Per activar aquesta funció, ves als Ajustos de la biblioteca musical i selecciona les carpetes de sincronització.

Amb aquesta opció activada, l'aplicació escaneja totes les carpetes seleccionades, identifica els fitxers d'àudio compatibles i els integra perfectament a la teva biblioteca. Pots iniciar o aturar la sincronització tocant l'acció de menú corresponent.

La sincronització de música en línia opera exclusivament quan l'app está en primer pla, cosa que significa que sincronitzar una biblioteca gran pot portar una mica de temps. Per accelerar el procés, deixa l'app oberta, connecta el dispositiu a una font d'alimentació i activa Pantalla → Sempre activa als ajustos de l'aplicació.

Alternativament, pots realitzar la sincronització de música en línia a la versió d'escriptori de l'app i transferir la biblioteca musical a la versió iOS usant la funció Còpia de seguretat i Restauració.

També pots configurar amb quina freqüència vols sincronitzar la teva biblioteca musical en línia. Si configures l'interval a Immediatament, la sincronització en línia s'iniciarà cada vegada que obris l'aplicació.

### Sincronització offline

Aquí pots configurar la sincronització de música offline.

#### Carpetes offline sincronitzades

Quan fas que una carpeta al núvol estigui disponible offline (via el menú Més accions), apareix a la secció Fitxers locals → Carpetes fora de línia. L'app descarrega el seu contingut al teu dispositiu. Si fas canvis a la carpeta al núvol — com afegir, eliminar o actualitzar fitxers — l'app detecta aquests canvis i actualitza la còpia local automàticament.

En aquesta pantalla, pots iniciar manualment la sincronització de la carpeta offline, revelar la carpeta offline a la seva carpeta contenidora i desactivar el mode offline per a la carpeta. Desactivar el mode offline elimina totes les còpies locals dels fitxers del teu dispositiu.

#### Interval de temps

Pots establir l'interval de temps per a quant sovint l'app ha de comprovar les modificacions de les carpetes offline.

#### Inici de l'escaneig de carpetes locals

Aquesta opció escaneja totes les carpetes locals ubicades al directori Documents de l'aplicació per trobar fitxers d'àudio compatibles. Tots aquests fitxers locals s'afegeixen perfectament a la teva biblioteca musical. Els fitxers locals ubicats al teu dispositiu però fora d'aquesta aplicació s'han d'afegir a la biblioteca musical manualment, ja que l'app no té accés als fitxers fora del directori Documents de l'aplicació a causa de les restriccions de seguretat de iOS / macOS.

#### Important

És aconsellable iniciar periòdicament la sincronització de música offline per mantenir la teva biblioteca musical actualitzada amb els teus fitxers locals.

### Personalització

En aquesta secció, pots configurar l'estil de la pantalla de la biblioteca musical per adaptar-lo a les teves preferències. Hi ha tres opcions disponibles: Menú simple, Menú agrupat, Menú amb pestanyes. També pots activar o desactivar la visualització de portades d'àlbum a les pantalles de detall d'àlbum.

### Portades d'Àlbum

Aquí pots configurar com l'aplicació carrega i emmagatzema les portades d'àlbum.

- **Tipus de xarxa** — tria Wi-Fi o Wi-Fi i dades mòbils per a les descàrregues de portades.
- **Carregar portades d'àlbum per a fitxers en línia** — quan está activat, es carreguen les portades d'àlbum incrustades per als fitxers emmagatzemats al núvol. Pot usar dades de xarxa addicionals.
- **Cercar a la carpeta** — quan está activat, si una pista no té portada incrustada, l'app busca imatges JPEG o PNG a la mateixa carpeta i les usa com a portada d'àlbum.
- **Qualitat de portada** — tria la qualitat de les portades d'àlbum emmagatzemades al teu dispositiu.
- **Mostrar a la carpeta** — obre la carpeta on s'emmagatzemen les portades d'àlbum a la memòria cau perquè puguis gestionar-les o fer-ne còpies de seguretat.
- **Eliminar tot** — elimina les portades d'àlbum de la memòria cau per alliberar espai d'emmagatzematge i forçar l'app a tornar-les a carregar per demanda.

Per defecte, l'app comprova si hi ha portades d'àlbum incrustades a les teves pistes i les mostra si estan disponibles. Si no hi ha portades incrustades i l'opció **Cercar a la carpeta** está activada, l'app comprova la carpeta contenidora per a imatges JPEG o PNG i les usa com a portada d'àlbum per a totes les pistes d'aquella carpeta.

### Llistes de reproducció

Pots activar l'opció d'afegir la mateixa cançó a una llista de reproducció dues vegades. Per defecte, aquesta opció está desactivada.

### Recents

Pots gestionar la teva llista de cançons reproduïdes recentment.

- **Eliminar llista** — elimina tota la llista de cançons reproduïdes recentment.
- **Canviar la mida de la llista** — estableix el nombre d'elements que apareixen a la llista.
- **Exportar llista de cançons** — exporta la teva llista de cançons reproduïdes recentment a M3U, CSV o TXT. Hi ha instruccions detallades disponibles [aquí](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favorits

Pots gestionar la llista de les teves cançons favorites.

- **Edició simultània** — quan está activat, afegir una cançó als favorits l'afegeix tant a la biblioteca musical com a la secció de fitxers alhora.
- **Eliminar llista** — elimina tota la llista de cançons favorites.
- **Exportar llista de cançons** — similar a Recents, exporta la llista de favorits a M3U, CSV o TXT.

### Eliminar biblioteca

Aquesta acció esborrarà la base de dades de la biblioteca musical, però deixarà els fitxers de música intactes a l'emmagatzematge.

### Límit de càrrega de contingut

Per defecte, l'aplicació usa paginació per reduir el temps de càrrega de contingut i mantenir les biblioteques grans amb resposta. No obstant això, pots desactivar aquesta opció i permetre que l'aplicació carregui totes les dades disponibles alhora. Per fer-ho, obre els ajustos de l'aplicació, desplaça't fins a Personalització → Límit de càrrega de contingut i tria Desactivat.
