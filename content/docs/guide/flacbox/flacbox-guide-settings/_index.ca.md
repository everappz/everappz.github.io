---
title: "Configuració"
date: 2020-02-01
description: "Explora cada paràmetre de Flacbox — des de preferències de reproducció, el motor d'àudio FFmpeg / del sistema, sortida d'àudio d'alta resolució, ajustos de l'equalitzador, correcció del to, durada del búfer IO, sincronització de metadades, control de llistes de reproducció, transferències de fitxers, widgets de la pantalla d'inici, Apple CarPlay, personalització de la interfície d'usuari, idioma, codi d'accés, còpia de seguretat i restauració, i actualització Premium."
keywords: [
  "configuració Flacbox", "configuració del reproductor d'àudio", "actualització Premium Flacbox",
  "WiFi Drive", "sincronització de metadades", "equalitzador", "velocitat de reproducció",
  "duplicats de llista de reproducció", "configuració del gestor de fitxers", "sincronització de música sense connexió",
  "editor d'etiquetes d'àudio", "mode fosc", "restaurar compres", "configuració de còpia de seguretat",
  "configuració de widgets Flacbox", "configuració de CarPlay Flacbox",
  "configuració de FFmpeg Flacbox", "configuració de freqüència de mostreig Flacbox",
  "configuració de correcció del to Flacbox", "búfer IO Flacbox",
  "codi d'accés Flacbox", "idioma Flacbox", "personalització Flacbox",
  "analítiques Flacbox"
]
tags: ["guia", "flacbox", "configuració"]
readingTime: 16
---


La pantalla de Configuració és el centre de control de Flacbox. Des d'aquí pots actualitzar a Premium, configurar el motor d'àudio (còdecs del sistema o FFmpeg), gestionar la teva biblioteca de música, configurar el gestor de fitxers, personalitzar l'editor d'etiquetes d'àudio, activar widgets de la pantalla d'inici i Apple CarPlay, fer còpies de seguretat de les teves dades i accedir a l'ajuda i informació legal. Les seccions s'agrupen sota encapçalaments: Compres i actualitzacions, Preferències de l'app, Ajuda, i Legal i privadesa.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla principal de configuració de Flacbox" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Actualització a Premium

Actualitza l'aplicació a la versió Premium per eliminar tots els límits. La versió gratuïta de l'aplicació ofereix una compra d'una sola vegada per tota la vida i dues opcions de subscripció (1 mes i 1 any) per eliminar totes les restriccions i actualitzar a Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Actualització a Premium de Flacbox" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

La **Compartició familiar** està activada per a totes les compres i plans, de manera que pots compartir la versió Premium amb fins a cinc membres de la teva família sense cap cost addicional.

{{< cards cols="1">}}
  {{< card title="" subtitle="Selecciona un pla Premium de Flacbox" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Pots llegir més sobre les compres i la versió Premium aquí: [Quina és la diferència entre Flacbox i Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Compartició de compres entre iOS i Mac

Les compres de per vida i les subscripcions es comparteixen entre iOS i Mac, usant iCloud per sincronitzar aquesta informació. Si tens la versió Premium al teu dispositiu iOS, assegura't que tens instal·lada la versió més recent i que iCloud està activat. Inicia l'app a iOS i espera un minut perquè la informació de la teva compra es carregui a iCloud.

També pots provar de tocar el botó Restaurar compres a la configuració de l'app. Després, instal·la l'última versió de l'app des de l'App Store al teu Mac i inicia l'app. Assegura't que tens connexió a Internet i que estàs usant el mateix compte d'iCloud i App Store al Mac que vas usar a iOS. Espera un minut perquè l'app descarregui la informació de compra d'iCloud — la versió Premium s'hauria d'activar al teu Mac automàticament.

## Restauració de compres en un dispositiu nou

Per restaurar la teva compra en un dispositiu nou, usa el menú Compres → Restaurar compres. Veuràs la llista de les teves compres. Si no les veus totes, confirma que el dispositiu està connectat al mateix Apple ID que es va usar per fer les compres i assegura't que iCloud està activat.

## Prova Premium gratuïtament

Pots actualitzar a la versió Premium gratuïtament, durant un temps limitat, usant aquest menú. Simplement mira un anunci o explica als teus amics sobre l'app per obtenir Premium gratuïtament.

## Compres

Pots restaurar compres anteriors des d'aquest menú. Si trobes errors d'activació, prova d'activar l'opció Restaurar compres en iniciar l'app.

## Actualització de programari

Toca Actualització de programari per comprovar si hi ha disponible una versió més nova de Flacbox. L'app compararà la teva versió instal·lada amb la darrera versió a l'App Store i t'avisarà si es recomana una actualització.

## Novetats

Aquest menú està disponible després que s'alliberi una nova versió. Mostra un resum dels canvis i les noves funcions de l'actualització més recent.

## Reproductor d'àudio

Aquesta secció configura el reproductor d'àudio i el motor d'àudio subjacent, incloent l'elecció de FFmpeg / còdec del sistema i les opcions de sortida d'àudio d'alta resolució.

### General

Aquesta configuració cobreix els aspectes fonamentals del reproductor d'àudio — la cua de reproducció, la sortida d'àudio i el desament de l'estat del reproductor.

- **Mode de repetició** — tria com es comporta el reproductor d'àudio quan acaba una pista:
  - **Repetir tot** — reprodueix de nou totes les pistes de la teva cua.
  - **Repetir una** — repeteix només la pista actual.
  - **Aturar repetició** — fa una pausa a la reproducció quan acaba la pista actual.
  - **Sense repetició** — permet que la teva cua es reprodueixi sense repetir.
- **Mode aleatori** — aleatoritza l'ordre de les pistes de la teva cua. Pots configurar-lo en **Aleatori desactivat** o **Aleatori activat**.
- **Còdec d'àudio** — tria el motor d'àudio usat per a la reproducció:
  - **Còdec del sistema + FFmpeg** — prioritza el còdec d'àudio del sistema on sigui possible, millorant la compatibilitat i l'estabilitat. La correcció del to i la freqüència de mostreig de sortida d'àudio poden ser limitats.
  - **FFmpeg** — força el còdec FFmpeg per a tots els fitxers d'àudio, desblocant la correcció del to i la freqüència de mostreig de sortida d'àudio.
- **Freqüència de mostreig de sortida d'àudio** — ajusta la freqüència de mostreig de sortida d'àudio per optimitzar la qualitat del so, especialment útil amb un DAC extern. Valors disponibles: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** i **96 kHz**.
- **Nombre de canals de sortida d'àudio** — per a sistemes d'àudio multicanal amb un DAC extern, especifica el nombre de canals: Mono, Estèreo, Centre / Esquerre / Dreta, Centre / Esquerre / Dreta / Envoltant, ITU BS.775-1, 5.1 Envoltant i SDDS.
- **Durada preferida del búfer IO de sortida d'àudio** — configura la durada del búfer d'entrada / sortida. Un valor típic per minimitzar la latència mentre reprodueixes àudio d'alta resolució és d'uns **5 mil·lisegons (0,005 segons)**. Prova diferents durades al teu dispositiu de destinació per trobar el millor equilibri entre la latència baixa i la reproducció sense errors.
- **Mode de sortida d'àudio (només iOS)** — configura el mode de sortida d'àudio barrejat perquè l'àudio de Flacbox es barreji amb altres aplicacions. Les instruccions detallades són [aquí](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Desar la posició de reproducció** — desa i restaura la posició de reproducció de les cançons de la teva biblioteca de música.
- **Desar l'estat del reproductor d'àudio** — preserva l'estat del reproductor d'àudio abans que tanquis l'app, facilitant la represa des d'on ho vas deixar.

Un cop hagis activat tant **Desar la posició de reproducció** com **Desar l'estat del reproductor d'àudio**, obre qualsevol carpeta, àlbum, artista o gènere i veuràs un botó **Continuar reproducció** a la part superior de la pantalla.

### Personalització

La personalització et permet personalitzar l'aspecte de la pantalla del reproductor d'àudio, canviar els controls disponibles a la pantalla principal, la pantalla de bloqueig i la barra d'estat, i configurar els controls de salt de temps.

- **Estil de la pantalla del reproductor d'àudio** — configura la posició dels elements a la pantalla del reproductor d'àudio.
- **Estil de desplaçament de les portades d'àlbum** — configura l'estil de desplaçament preferit per a les portades d'àlbum.
- **Elements addicionals** — activa elements addicionals a la pantalla del reproductor d'àudio. La informació del format d'àudio mostra la informació d'àudio de la pista que s'està reproduint sobre la portada; el control lliscant de volum d'àudio mostra el control lliscant de sortida d'àudio sota els controls de reproducció.
- **Accions de la pantalla principal** — configura quins botons han d'estar visibles a la pantalla principal del reproductor d'àudio per defecte: mode de repetició i aleatori, cançó següent i anterior, salt de temps, temporitzador de son, Google Chromecast, AirPlay i Bluetooth, equalitzador d'àudio, cerca, marcadors, velocitat, afegir marcador, afegir als favorits, comentaris i més.
- **Controls de reproducció a la pantalla de bloqueig** — tria quins controls apareixen a la pantalla de bloqueig. Valors possibles: salt de temps, afegir marcador, afegir als favorits.
- **Botons de salt de temps** — tria l'interval de temps per als botons de salt de temps.

### Càrrega de fitxers

Durant la càrrega de fitxers, pots canviar el tipus de xarxa usat per carregar cançons. Opcions disponibles: **Wi-Fi**, **Wi-Fi i dades mòbils**.

- **Temps de precàrrega** — estableix l'interval de temps del búfer. Augmenta'l si tens una connexió de xarxa deficient.
- **Usar URL directa** — quan s'activa, s'usa una URL directa per carregar la cançó si el servidor ho permet. Això pot accelerar la càrrega de cançons però pot afectar l'estabilitat de la reproducció.

### Equalitzador d'àudio

Configura l'equalitzador d'àudio de 10 bandes, els presets i el preamplificador. Pots llegir més sobre la configuració de l'equalitzador d'àudio [aquí](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Velocitat de reproducció

Ajusta la velocitat de reproducció del reproductor d'àudio de **0,02× a 3,00×**. Toca la icona de configuració a la cantonada superior dreta per canviar al **mode precís** per a ajustos més fins.

### Correcció del to

Canvia la configuració de correcció del to usant els valors predefinits, o canvia al **mode precís** tocant el botó a la cantonada superior dreta. La correcció del to està disponible en el camí del còdec FFmpeg, amb un rang de **-1000 a +1000**.

### Memòria cau de reproducció

Les cançons a la cua del reproductor d'àudio es descarreguen automàticament per garantir una reproducció fluida. Si descarregues fitxers d'àudio manualment, pots desactivar-ho per evitar duplicats. També pots configurar la mida de la memòria cau del reproductor d'àudio aquí.

### Temporitzador de son

Activa un temporitzador per aturar automàticament la reproducció després d'un període especificat. Toca la icona de configuració a la cantonada superior dreta per al **mode precís** amb granularitat minut per minut.

## Biblioteca

La configuració de la teva biblioteca de música — sincronització automàtica, lectura de metadades, càrrega de portades d'àlbum, llistes de reproducció, recents i favorits — es troba aquí.

### Lectura de metadades

Quan afegeixis pistes a la biblioteca, el **lector de metadades** comença a treballar. Aquest procés en segon pla llegeix totes les metadades de les teves pistes i les organitza per Artista, Àlbum, Gènere i Compositor. Pots ajustar la velocitat de lectura de metadades per carregar dades més ràpidament (a costa de més bateria). També pots desactivar el lector de metadades i mostrar noms de fitxers en lloc d'informació d'etiquetes.

El lector de metadades **només actualitza les metadades a la teva biblioteca de música** i no altera els fitxers emmagatzemats al teu compte al núvol ni a l'emmagatzematge local. Per editar metadades als mateixos fitxers d'àudio, usa l'**editor d'etiquetes** integrat a través de l'acció corresponent al menú d'opcions.

Quan la **Lectura de metadades en segon pla** està activada, el lector continua treballant en mode de segon pla. Si l'app usa massa energia durant la reproducció d'àudio, iOS podria suspendre-la.

Si tens una gran col·lecció de música, realitza la sincronització de metadades a la versió d'escriptori de l'aplicació i transfereix la biblioteca de música sincronitzada a iOS usant **Còpia de seguretat i restauració**.

Quan **Normalitzar la codificació de metadades** està activat, l'app normalitza automàticament la codificació de metadades per a totes les cançons. Això corregeix les codificacions d'etiquetes trencades (per exemple, després d'editar fitxers en un PC amb Windows) i evita que apareguin caràcters incorrectes a la informació de la pista.

**Tornar a carregar metadades** marca cada fitxer de la teva biblioteca de música com a mancat de metadades, la qual cosa fa que el lector de metadades actualitzi cada registre.

**Iniciar la lectura de metadades** activa el lector de metadades manualment. El progrés es mostra sota l'acció.

### Sincronització en línia

La sincronització automàtica de música en línia afegeix pistes de serveis al núvol connectats a la biblioteca de música automàticament. Per activar-la, obre la configuració de la biblioteca de música i selecciona les carpetes de sincronització.

Amb aquesta opció activada, l'aplicació escaneja les carpetes seleccionades, identifica els fitxers d'àudio compatibles i els afegeix a la teva biblioteca. Inicia o atura la sincronització amb l'acció del menú corresponent.

La sincronització en línia s'executa únicament quan l'app és en primer pla, de manera que sincronitzar una biblioteca gran pot trigar una estona. Per accelerar les coses, mantén Flacbox obert, endolla el dispositiu a l'alimentació i activa **Configuració → Pantalla → Sempre actiu**.

Alternativament, realitza la sincronització en línia a la versió d'escriptori de l'app i transfereix el resultat a iOS usant **Còpia de seguretat i restauració**.

També pots triar la freqüència amb la qual s'executa la sincronització en línia. Configurar l'interval en **Immediatament** activa una sincronització cada vegada que obres l'aplicació.

### Sincronització sense connexió

Configura la sincronització de música sense connexió.

#### Carpetes offline sincronitzades

Quan marques una carpeta en línia al teu servidor al núvol com a disponible sense connexió (usant el menú **Més accions**), apareix aquí. El contingut de la carpeta es descarrega a **Fitxers locals → Carpetes fora de línia**. Quan la carpeta en línia canvia (fitxers afegits, eliminats o actualitzats), l'app comprova els canvis i actualitza la còpia local al teu dispositiu.

En aquesta pantalla pots iniciar manualment la sincronització de la carpeta sense connexió, revelar la carpeta sense connexió a la seva carpeta adjacent i desactivar el mode sense connexió per a la carpeta. Desactivar el mode sense connexió elimina totes les còpies locals de fitxers del teu dispositiu.

#### Interval de temps

Tria la freqüència amb la qual l'app comprova les carpetes sense connexió per detectar modificacions.

#### Iniciar l'escaneig de carpetes locals

Escaneja totes les carpetes locals al directori **Documents** de l'aplicació per cercar fitxers d'àudio compatibles. Els fitxers trobats s'afegeixen automàticament a la biblioteca de música. Els fitxers ubicats al teu dispositiu però fora del directori Documents de l'aplicació s'han d'afegir manualment a la biblioteca de música, ja que l'app no pot accedir-hi a causa de les restriccions de seguretat d'iOS / macOS.

**Important:** Es recomana iniciar periòdicament la sincronització de música sense connexió per mantenir actualitzada la teva biblioteca de música amb els teus fitxers locals.

### Personalització

Configura l'estil de la pantalla de la biblioteca de música. Hi ha tres opcions disponibles: **Menú senzill, Menú agrupat, Menú amb pestanyes**. També pots activar o desactivar les portades d'àlbum a la pantalla de detalls de l'àlbum.

### Portades d'àlbum

Configura com l'aplicació carrega i emmagatzema les portades dels àlbums.

- **Tipus de xarxa** — tria **Wi-Fi** o **Wi-Fi i dades mòbils** per a les descàrregues de portades.
- **Carregar portades d'àlbum per a fitxers en línia** — quan s'activa, es carreguen les portades d'àlbum incrustades per als fitxers emmagatzemats a l'emmagatzematge al núvol. Això pot usar dades de xarxa addicionals.
- **Cercar a la carpeta** — quan s'activa, si una pista no té portada incrustada, l'app cerca imatges JPEG o PNG a la mateixa carpeta i les usa com a portada de l'àlbum.
- **Qualitat de la portada** — selecciona la qualitat de les portades d'àlbum emmagatzemades al teu dispositiu.
- **Mostrar a la carpeta** — obre la carpeta on s'emmagatzemen temporalment les portades d'àlbum.
- **Eliminar totes** — elimina les portades d'àlbum emmagatzemades temporalment per alliberar espai d'emmagatzematge i obligar l'app a tornar a carregar-les quan calgui.

### Llistes de reproducció

Activa l'opció per afegir la mateixa cançó a una llista de reproducció dues vegades. Per defecte, aquesta opció està desactivada.

### Recents

Gestiona la teva llista de cançons reproduïdes recentment.

- **Eliminar llista** — elimina tota la llista de cançons reproduïdes recentment.
- **Canviar la mida de la llista** — estableix el nombre d'elements que apareixen a la llista.
- **Exportar llista de cançons** — exporta la teva llista de cançons reproduïdes recentment com a M3U, CSV o TXT. Les instruccions detallades estan disponibles [aquí](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favorits

Gestiona la llista de les teves cançons preferides.

- **Edició simultània** — quan s'activa, afegir una cançó als favorits l'afegeix tant a la biblioteca de música com a la secció de fitxers simultàniament.
- **Eliminar llista** — elimina tota la llista de cançons preferides.
- **Exportar llista de cançons** — com en Recents, exporta els favorits com a M3U, CSV o TXT.

### Eliminar la biblioteca de música

Esborra la base de dades de la biblioteca de música. Els teus fitxers de música a l'emmagatzematge es deixen intactes.

## Codi d'accés

Activa la pantalla de codi d'accés per protegir les dades de la teva aplicació amb un codi d'accés numèric de 4 dígits. Quan s'activa, se't demanarà que introdueixis el codi d'accés cada vegada que l'app s'iniciï. Combina'l amb Face ID / Touch ID d'iOS al dispositiu per a una protecció addicional.

## Gestor de fitxers

La secció del Gestor de fitxers controla com es transfereixen, emmagatzemen i previsualitzen els fitxers.

### Transferències de fitxers

Tria la preferència de xarxa per descarregar fitxers al teu dispositiu.

### Nombre màxim de tasques paral·leles

Estableix el nombre de fils de descàrrega paral·lels. Un nombre més alt accelera les descàrregues però usa més bateria.

### Tasques de transferència de fitxers

Mostra les tasques de càrrega i descàrrega actives actualment.

### Transferències en segon pla

Permet les descàrregues mentre l'app és en segon pla. Si les transferències en segon pla consumeixen molta energia, iOS pot suspendre l'app.

### Desa els fitxers descarregats a

Tria el directori de descàrregues predeterminat, o fes que l'app et demani cada vegada.

### Carpetes offline sincronitzades

Gestiona la sincronització sense connexió per a les carpetes seleccionades. Per activar la sincronització sense connexió, toca el botó de tres punts al costat d'una carpeta i selecciona **Mode disponible sense connexió**. Els fitxers nous afegits a la carpeta al núvol es descarreguen al teu dispositiu automàticament. Llegeix més sobre els modes sense connexió [aquí](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Interval de temps

Tria la freqüència amb la qual es sincronitzen les carpetes sense connexió. **Immediatament** activa una sincronització cada vegada que obres l'app.

### Mostra els noms de fitxer complets

Mostra els noms de fitxer complets, incloent les extensions, al gestor de fitxers.

### Editar fitxers en línia

Desactiva l'edició de fitxers en línia per canviar al mode de només lectura per als serveis al núvol connectats i evitar eliminacions accidentals. Aquesta acció elimina les operacions d'edició de fitxers de la interfície d'usuari.

### Copiar fitxers en obrir

Especifica com l'app gestiona els fitxers importats d'altres aplicacions.

### Miniatures per a fitxers

Gestiona i elimina les miniatures de fitxers generades per alliberar espai d'emmagatzematge.

### Eliminar fitxers temporals

Neteja la carpeta de memòria cau de l'aplicació per recuperar espai d'emmagatzematge.

## Editor d'etiquetes d'àudio

Configura l'editor d'etiquetes d'àudio integrat — pràctic per corregir en massa problemes d'artista / àlbum / any / gènere / portada en fitxers al núvol i locals.

### Escala de la portada de l'àlbum

Tria el mètode d'escala usat quan es desa una portada d'àlbum a les etiquetes d'àudio.

### Actualitzar fitxers en línia

Quan s'activa, l'aplicació actualitza automàticament les metadades d'un fitxer al servidor al núvol després d'acabar d'editar-lo.

### Eliminar el fitxer després d'editar en línia

Tria si l'aplicació ha d'eliminar la còpia descarregada després d'acabar l'edició d'un fitxer en línia en un servidor al núvol.

### Botons de la pantalla principal

Tria quins botons són visibles a la pantalla principal de l'editor d'etiquetes d'àudio.

Per a una edició en massa més profunda de molts fitxers alhora, instal·la la nostra aplicació complementària **Evertag**.

## Widgets

Activa els widgets perquè l'app actualitzi les dades dels widgets durant la reproducció. Les actualitzacions dels widgets requereixen energia addicional, de manera que el commutador és inactiu per defecte — activa'l només si realment uses widgets a la teva pantalla d'inici o pantalla de bloqueig.

Pots afegir widgets de Flacbox mantenint premuda la pantalla d'inici o la pantalla de bloqueig, tocant **+**, cercant **Flacbox** i escollint una mida de widget. Els widgets mostren la portada actual, el títol de la pista i l'artista, i toquen directament al reproductor de pantalla completa. Els widgets també funcionen al macOS al Centre de notificacions.

## CarPlay

Canvia la configuració de CarPlay aquí. Aquest menú també està disponible dins de la interfície de CarPlay perquè puguis ajustar l'experiència mentre condueixes.

### Ordenar

Configura les opcions d'ordenació per a totes les pantalles de CarPlay.

### Límit de càrrega de contingut

Tria si l'app usa paginació a la pantalla de CarPlay. La paginació manté els menús responsables en biblioteques grans.

### Color del degradat de les icones del menú

Selecciona l'esquema de colors per a la pantalla d'inici de CarPlay.

### Mostrar imatges

Desactiva les imatges a la pantalla de CarPlay per optimitzar la velocitat de càrrega i reduir l'ús de memòria en biblioteques grans.

### Pausar la reproducció en connectar

Activa aixó per evitar àudio fort sobtat quan connectes el dispositiu a CarPlay.

## Wi-Fi Drive

Activa **Wi-Fi Drive** per transferir fitxers d'un ordinador al teu dispositiu usant un navegador web d'escriptori, Finder o File Explorer. Les instruccions detallades sobre com usar Wi-Fi Drive estan disponibles [aquí](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalització

Personalitza la interfície d'usuari per adaptar-la a les teves preferències.

### Icona de l'aplicació

Tria una icona d'aplicació alternativa per a la teva pantalla d'inici (Premium).

### Esquema de colors

Tria el tema de la interfície d'usuari i activa el mode fosc. Quan es selecciona **Per defecte**, l'aplicació segueix la configuració d'aparença del dispositiu.

### Estil de fons

Modifica l'estil de fons de l'aplicació. Actualment l'única opció és **Portada d'àlbum difuminada**, que usa la portada de la pista que s'està reproduint com a fons difuminat de l'app.

### Aparença dels elements a la llista

Ajusta com es mostren els elements a les llistes. Útil en pantalles petites — pots deixar que l'app ajusti l'alçada de les files automàticament segons el contingut, o mostrar icones més petites a les cel·les de la llista per donar més espai al text.

### Límit de càrrega de contingut

Per defecte l'aplicació usa paginació per accelerar la càrrega de contingut. Pots desactivar la paginació per carregar-ho tot d'un cop.

### Estil de la pantalla de fitxers locals

Canvia l'estil de presentació de la secció **Fitxers locals**.

### Estil de la pantalla de la biblioteca de música

Personalitza l'aspecte de la pantalla de **Biblioteca de música**.

### Estil de la pantalla del reproductor d'àudio

Configura l'aspecte de la pantalla del **Reproductor d'àudio**.

### Estil del menú contextual

Tria l'estil del menú contextual mostrat quan toques el botó **Més accions**.

## Finestra

Disponible al Mac i Catalyst. Configura les preferències relacionades amb la finestra com la mida predeterminada i el comportament en iniciar.

## Pantalla

Tria si la pantalla ha de romandre activa mentre uses l'aplicació. Útil quan s'escanegen biblioteques grans o es fa una feina prolongada d'edició d'etiquetes.

## Accessibilitat

Activa el **Mode de text** per amagar totes les imatges a la interfície d'usuari. El mode de text s'activa automàticament quan VoiceOver és actiu i també és útil per a configuracions molt petites o de només text.

## Idioma

Canvia l'idioma de l'aplicació i sobreescriu el valor predeterminat del sistema. El canvi s'aplica després de tancar completament i tornar a obrir Flacbox. Les localitzacions compatibles actualment inclouen: Afrikaans, Akan, Albanès, Amhàric, Àrab, Armeni, Assamès, Aimara, Azerbaidjanès, Bambara, Bengalí, Basc, Bielorús, Bosnià, Búlgar, Birmà, Català, Cebuà, Xinès (simplificat), Xinès (tradicional), Cors, Croat, Txec, Danès, Divehi, Dogri, Holandès, Anglès, Esperanto, Estonià, Ewe, Filipí, Finlandès, Francès, Gallec, Ganda, Georgià, Alemany, Grec, Guaraní, Gujarati, Crioll haitià, Haussa, Hawaià, Hebreu, Hindi, Hmong, Hongarès, Islandès, Igbo, Ilocà, Indonesi, Irlandès, Italià, Japonès, Javanès, Kannada, Kazakh, Khmer, Kinyarwanda, Coreà, Krio, Kurd, Kurd Sorani, Kirguís, Laosià, Llatí, Letó, Lingalà, Lituà, Luxemburguès, Macedoni, Maithili, Malgaix, Malai, Malayalam, Maltès, Maori, Marathi, Mizo, Mongol, Nepalès, Sotho del nord, Noruec Bokmål, Nyanja, Odia, Oromo, Paixtu, Persa, Polonès, Portuguès, Panjabi, Romanès, Rus, Samoà, Sànscrit, Gaèlic escocès, Serbi, Shona, Sindhi, Singalès, Eslovac, Eslovè, Somali, Sotho del sud, Espanyol, Sundanès, Swahili, Suec, Tadjik, Tamil, Tàtar, Telugu, Tailandès, Tsonga, Turc, Turcman, Ucraïnès, Urdu, Uigur, Uzbek, Vietnamita, Gal·lès, Xhosa, Yiddish, Ioruba, Zulu.

## Còpia de seguretat i restauració

Usa aquesta funció per fer còpies de seguretat de totes les dades de la teva aplicació o migrar-les a un altre dispositiu. Pots triar què incloure:

- **Base de dades** — totes les teves pistes a la biblioteca de música, incloent les llistes de reproducció. Les pistes sense connexió no s'inclouen per mantenir el tamany del fitxer de còpia de seguretat manejable.
- **Portades d'àlbum** — totes les teves portades d'àlbum emmagatzemades temporalment.
- **Configuració** — tota la configuració de la teva aplicació.

Toca **Còpia de seguretat de les dades de l'aplicació** per iniciar la còpia de seguretat. Les dades de l'aplicació s'escriuen en un sol fitxer que pots usar més tard per restaurar l'estat de l'aplicació en un dispositiu nou o després de reinstal·lar l'aplicació.

Per restaurar les dades de l'aplicació en un dispositiu nou, mou el fitxer de còpia de seguretat al nou dispositiu usant un servei al núvol connectat o iCloud i obre'l al nou dispositiu.

Instruccions detallades pas a pas: [Com transferir la teva biblioteca de música entre dispositius: Guia pas a pas](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Ajuda

Accedeix a la guia de l'aplicació per obtenir assistència i orientació sobre l'ús efectiu de l'app.

## Preguntes freqüents

Troba respostes a les preguntes més comunes a la secció de Preguntes freqüents.

## Enviar comentaris

Tens comentaris o necessites assistència? Envia els teus comentaris a l'equip d'assistència directament des de l'app.

## Compartir aquesta aplicació

Comparteix l'aplicació amb els teus amics per escampar la paraula.

## Descobreix més aplicacions

Explora altres aplicacions d'Everappz.

## Termes i condicions

Descriu els termes i condicions per usar l'aplicació. Si us plau, llegeix-los abans d'usar l'aplicació.

## Política de privadesa

Visita la pàgina de política de privadesa per entendre les nostres pràctiques de gestió de dades. Si us plau, llegeix-la abans d'usar l'aplicació.

## Analítiques i recopilació de dades

Comprova quins serveis estan activats per a les analítiques i la recopilació de dades i desactiva els que no vulguis.

## Avisos legals

Conté informació sobre cada biblioteca usada a l'aplicació juntament amb el número de versió de l'app i la informació de compilació.
