---
title: "Reproductor d'àudio"
date: 2020-02-01
description: "Aprèn a usar el reproductor d'àudio de Flacbox a l'iPhone, l'iPad i el Mac. Controla la reproducció, gestiona les cues, configura el motor d'àudio FFmpeg / del sistema, canvia la freqüència de mostreig, la correcció del to, la durada del búfer IO, l'equalitzador, els marcadors d'àudio, AirPlay 2, Google Cast, CarPlay, els widgets i les dreceres de teclat del Mac."
keywords: [
  "guia del reproductor Flacbox", "configuració del reproductor d'àudio", "equalitzador Flacbox",
  "transmissió de música AirPlay", "música Google Cast", "marcadors d'àudio",
  "cua de reproducció Flacbox", "repetició i aleatori Flacbox", "control de volum Flacbox",
  "mini reproductor macOS", "app de música VoiceOver",
  "FFmpeg Flacbox", "correcció del to Flacbox", "freqüència de mostreig Flacbox",
  "DAC extern Flacbox", "so envoltant Flacbox", "búfer IO Flacbox",
  "velocitat de reproducció Flacbox", "temporitzador de son Flacbox"
]
tags: ["guia", "flacbox", "reproductor"]
readingTime: 14
---


El reproductor d'àudio és la pantalla principal de l'app on controles la música i la majoria de les funcions de reproducció. També és aquí on el motor d'àudio d'alta resolució de Flacbox — construït sobre els còdecs del sistema més la biblioteca **FFmpeg** inclosa — fa la feina pesada. Explorem com usar-lo.

## Accés al reproductor d'àudio

Pots arribar al reproductor de pantalla completa des de la barra del mini reproductor. A l'iPhone, el mini reproductor es troba a la part inferior de la pantalla principal. A l'iPad i al Mac, és al costat esquerre. Per ocultar el mini reproductor a l'iPhone, toca'l una vegada i llisca cap avall. Per tancar completament el reproductor de pantalla completa, toca el botó de tancament a la cantonada inferior dreta.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla principal del reproductor d'àudio de Flacbox" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Formats d'àudio compatibles

Flacbox reprodueix els formats d'àudio més populars — tant els còdecs del sistema d'Apple com molts formats addicionals gestionats pel motor FFmpeg inclòs:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

Això cobreix pràcticament tots els formats moderns amb pèrdua i sense pèrdua que probablement tens en una col·lecció de música personal.

## Controls de reproducció

A la part inferior de la pantalla del reproductor, veuràs botons per a Reproduir, Pausar, Pista següent i Pista anterior. També hi ha botons opcionals com Avançar 30 seg i Retrocedir 30 seg que pots activar a la configuració de l'app (pràctics per als audiollibres). Pots avançar ràpidament o rebobinar mantenint premuts els botons Següent / Anterior. Per saltar a una part específica d'una pista, arrossega el control lliscant de reproducció.

## Repetició i aleatori

Toca el botó de repetició per alternar entre els modes de repetició:

- **Repetir tot** — repeteix totes les pistes de la teva cua.
- **Repetir una** — repeteix només la pista actual.
- **Aturar repetició** — fa una pausa quan acaba la pista actual.
- **Sense repetició** — reprodueix la cua una vegada sense repetir.

Usa el botó **Aleatori** per aleatoritzar l'ordre de les pistes de la cua.

## Control de volum

Obre la pantalla de configuració d'àudio tocant la icona de so sota els controls de reproducció per accedir al control lliscant de volum. També trobaràs aquí botons per a **Google Cast** i **AirPlay** perquè puguis canviar ràpidament la reproducció a un altre dispositiu.

## Google Cast (Chromecast)

Per als usuaris de Google Cast, la icona **Cast** apareix a la part inferior del reproductor. Toca-la per triar un dispositiu i iniciar la transmissió. Assegura't que el teu dispositiu i el receptor de Google Cast estan a la mateixa xarxa Wi-Fi. Nota: no tots els formats d'àudio són compatibles amb Google Cast — alguns formats d'alta resolució poden necessitar transcodificació.

## AirPlay

Per a AirPlay, busca el botó **AirPlay** a la part inferior del reproductor. Toca'l i selecciona un dispositiu per a la transmissió. Flacbox és compatible amb **AirPlay 2**, de manera que pots reproduir a múltiples HomePods, Apple TV o altaveus compatibles amb AirPlay 2 al mateix temps.

## Equalitzador d'àudio

Flacbox inclou un **equalitzador de 10 bandes** amb presets a l'estil iPod. Toca Equalitzador a la vista de volum, i activa'l a la cantonada superior dreta. Pots usar presets com Acoustic i Bass Booster, o ajustar cada banda de freqüència amb controls lliscants. Crea els teus propis presets, desa'ls amb qualsevol nom i augmenta el volum global amb el preamplificador. Tenim instruccions més detallades sobre com usar l'equalitzador d'àudio [aquí](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Equalitzador del reproductor d'àudio de Flacbox" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Barra d'eines del mode de reproductor

Per a alguns estils de reproductor, hi ha una barra d'eines dedicada a la part superior del reproductor de pantalla completa. Aquesta barra d'eines alberga tres botons útils:

- **Cerca** — localitza ràpidament una pista específica a la cua del reproductor.
- **Control de velocitat de reproducció** — ajusta la velocitat de reproducció des de 0,02× fins a 3,00×. Perfecte per a audiollibres, podcasts i conferències. Toca Normal per tornar a la velocitat predeterminada.
- **Marcadors d'àudio** — crea múltiples marcadors per pista. Tenim instruccions completes sobre com usar els marcadors [aquí](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Cua del reproductor

Per veure la cua del reproductor, toca el botó de cua al costat dret de la cançó actual. Cada cançó de la cua té més accions — toca els tres punts per veure-les. Per reordenar una cançó a la cua, usa l'indicador de reordenació prop del títol i arrossega'l a una nova posició.

{{< cards cols="1">}}
  {{< card title="" subtitle="Cua de reproducció de Flacbox" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Comentaris / Lletra

Per veure els comentaris de la pista i la lletra incrustada, així com els fitxers LRC, segueix aquests passos:

1. Obre **Configuració**.
2. Vés a **Reproductor d'àudio**.
3. Selecciona **Personalització**.
4. Toca **Botons a la pantalla principal**.
5. Activa **Comentaris**.

Després d'això, toca el botó de cua del reproductor a la part inferior de la pantalla diverses vegades per canviar de la vista de portada / cua a la vista de comentaris. A la pantalla de comentaris, llisca a la dreta per canviar entre **Comentaris**, **Lletra incrustada** i el **Fitxer LRC**. Les instruccions completes estan disponibles [aquí](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de lletra i comentaris de Flacbox" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Menú d'opcions

Cada cançó a la cua del reproductor d'àudio té un menú amb més accions, al qual s'accedeix tocant el botó de tres punts prop del títol de la cançó.

- **Reproduir a continuació** — afegeix la cançó a la part superior de la cua del reproductor.
- **Afegir a la llista de reproducció** — inclou la cançó en una llista de reproducció, amb l'opció de crear-ne una de nova.
- **Afegir als favorits** — marca la cançó com a preferida per a un accés ràpid.
- **Descarregar** — desa la cançó als fitxers locals, apareixent a la pestanya **Fitxers locals** i a la secció **Música sense connexió**.
- **Editar etiquetes d'àudio** — obre l'editor d'etiquetes d'àudio integrat per corregir metadades que falten, modificant la cançó al teu emmagatzematge.
- **Mostrar a la carpeta** — revela la carpeta on s'emmagatzema el fitxer d'àudio.
- **Mostrar al Finder** — per als fitxers importats des del Mac, revela la carpeta on es troba el fitxer d'àudio al teu Mac.
- **Obrir a** — exporta el fitxer d'àudio a una altra app.
- **Eliminar de la cua** — elimina la cançó seleccionada de la cua del reproductor d'àudio.
- **Eliminar del servei al núvol** — elimina la cançó tant de la biblioteca de música com de l'emmagatzematge al núvol. **Aquesta acció és irreversible.**
- **Eliminar dels fitxers locals** — elimina la cançó tant de la biblioteca de música com de l'emmagatzematge local. **Aquesta acció és irreversible.**
- **Eliminar de la biblioteca de música** — elimina la cançó de la teva biblioteca de música, mantenint el fitxer a l'emmagatzematge.

Les mateixes opcions estan disponibles per a l'element que s'està reproduint actualment a la cua del reproductor d'àudio, al qual pots accedir tocant la icona de **Més accions** prop del títol de la pista.

{{< cards cols="1">}}
  {{< card title="" subtitle="Opcions de Flacbox per a un element a la cua de reproducció" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Accions addicionals del reproductor

Toca el botó de **Més accions** "..." al costat esquerre del títol de la cançó que s'està reproduint actualment per veure accions addicionals.

- **Continuar reproducció** — reprèn des d'on ho vas deixar, incloent la cua i la posició del mèdia. Especialment útil per als audiollibres. S'activa a la configuració de l'app.
- **Cerca** — troba ràpidament una pista específica a la cua del reproductor d'àudio.
- **Marcadors** — veu la teva llista de marcadors d'àudio creats.
- **Comentaris** — veu els comentaris de la pista i la lletra incrustada, així com els fitxers LRC. Instruccions completes [aquí](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Velocitat** — ajusta la velocitat de reproducció al teu gust.
- **Recents** — accedeix a una llista de cançons reproduïdes recentment.
- **Favorits** — veu la teva col·lecció de cançons preferides.
- **Equalitzador d'àudio** — activa l'equalitzador d'àudio.
- **Temporitzador de son** — estableix un temporitzador per aturar la reproducció després d'un interval especificat. Ideal per a aquells moments en què vols adormir-te amb la teva música.
- **Desar cua com a llista de reproducció** — desa la cua actual del reproductor d'àudio com a nova llista de reproducció.
- **Eliminar cua** — buida la cua del reproductor i atura la reproducció.
- **Configuració** — accedeix a la configuració del reproductor d'àudio.
- **Ajuda** — troba assistència i orientació.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de més accions del reproductor d'àudio de Flacbox" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Marcadors d'àudio

Aquesta funció et permet crear múltiples marcadors per a les pistes de la teva biblioteca de música — perfecta per a audiollibres, conferències, llargues sessions de DJ o per marcar el cor d'una pista favorita.

Per crear un nou marcador:

- Comença a reproduir la cançó desitjada.
- Obre la pantalla del reproductor.
- Toca el botó **Marcadors** a la barra d'eines del mode de reproductor.
- Selecciona **Afegir marcador**.
- Tria el temps del marcador i toca **Fet** a la cantonada superior dreta.

Editar els marcadors de la pista actual és fàcil: toca Edita a la cantonada superior dreta per entrar al mode d'edició. En aquest mode, pots reordenar els marcadors, eliminar-los, ajustar el temps del marcador i canviar els títols dels marcadors. Hi ha instruccions més detallades sobre els marcadors d'àudio disponibles [aquí](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de marcadors d'àudio de Flacbox" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Recents i favorits

A la pantalla del reproductor, toca els tres punts per accedir als Recents i als Favorits. En tots dos apartats, pots cercar cançons, reproduir-les totes, barrejar-les totes, exportar la llista i esborrar-la. Tenim instruccions detallades sobre com exportar llistes de cançons [aquí](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Connecta el teu iPhone al cotxe via USB o Apple CarPlay sense fils i Flacbox apareix a la pantalla d'inici del teu CarPlay, llest per reproduir música de forma segura mentre condueixes. La interfície de CarPlay inclou pestanyes dedicades per a Biblioteca, Connexions, Fitxers locals i Configuració, amb controls de reproducció, aleatori, repetició, gestió de la cua i l'equalitzador d'àudio — tot disponible sense agafar el telèfon. Configura l'experiència de CarPlay a Configuració → CarPlay — opcions d'ordenació, paginació, color del degradat de les icones del menú, si es carreguen imatges i una opció per pausar la reproducció automàticament quan CarPlay es connecta.

[Llegeix la guia completa de CarPlay](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox a Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Widgets de la pantalla d'inici (iPhone i iPad)

Flacbox admet widgets de la pantalla d'inici i de la pantalla de bloqueig d'iOS perquè puguis veure i controlar la reproducció d'un cop d'ull. Assegura't que els Widgets estan activats a Configuració → Widgets → Activa els widgets, després mantén premuda la pantalla d'inici o la pantalla de bloqueig, toca **+**, cerca **Flacbox** i afegeix un widget. El widget s'actualitza durant la reproducció per mostrar la portada de la pista que s'està reproduint, el títol i l'artista.

## Finestra del mini reproductor (exclusiu de Mac)

Els usuaris de Mac poden usar un mini reproductor compacte sempre a dalt. Mou el cursor cap a la cantonada inferior dreta de la finestra de Flacbox, redueix-la fins a la seva mida més petita i toca el botó de plegar. Mantén-la a sobre de totes les altres finestres seleccionant Finestra → Mostra sempre la finestra a sobre a la barra de menús — perfecta per mantenir els controls de música visibles mentre treballes en una altra app.

## Dreceres de teclat (exclusiu de Mac)

Per als usuaris de Mac, hi ha disponible un menú de reproducció del sistema a la barra d'estat amb dreceres de teclat. Per exemple, prem la barra d'espai per Reproduir / Pausar. També estan disponibles dreceres per a Aturar, Cançó següent, Cançó anterior, Saltar temps, Repetir, Aleatori i Velocitat de reproducció.

## Configuració del reproductor d'àudio

Per accedir a la configuració, toca el botó Més a la pantalla del reproductor i tria Configuració. Aquí trobaràs diverses seccions, que s'enumeren a continuació.

### General

Aquesta configuració cobreix els aspectes fonamentals del reproductor d'àudio, incloent la cua de reproducció, la sortida d'àudio i el desament de l'estat del reproductor.

- **Mode de repetició** — tria com es comporta el reproductor d'àudio quan acaba una pista:
  - **Repetir tot** — reprodueix de nou totes les pistes de la teva cua.
  - **Repetir una** — repeteix només la pista actual.
  - **Aturar repetició** — fa una pausa a la reproducció quan acaba la pista actual.
  - **Sense repetició** — permet que la teva cua es reprodueixi sense repetir.
- **Mode aleatori** — aleatoritza l'ordre de les pistes de la teva cua. Pots configurar-lo en **Aleatori desactivat** o **Aleatori activat**.
- **Còdec d'àudio** — tria el motor d'àudio usat per a la reproducció:
  - **Còdec del sistema + FFmpeg** — prioritza el còdec d'àudio del sistema on sigui possible, millorant la compatibilitat i l'estabilitat. La correcció del to i els ajustos de la freqüència de mostreig de sortida d'àudio poden ser limitats en aquest mode.
  - **FFmpeg** — força el còdec FFmpeg per a tots els fitxers d'àudio, permetent-te ajustar la correcció del to i la freqüència de mostreig de sortida d'àudio.
- **Freqüència de mostreig de sortida d'àudio** — ajusta la freqüència de mostreig de sortida d'àudio per optimitzar la qualitat del so, especialment útil amb un DAC extern. Valors disponibles: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** i **96 kHz**.
- **Nombre de canals de sortida d'àudio** — per a sistemes d'àudio multicanal amb un DAC extern, especifica el nombre de canals: **Mono, Estèreo, Centre / Esquerre / Dreta, Centre / Esquerre / Dreta / Envoltant, ITU BS.775-1, 5.1 Envoltant** i **SDDS**.
- **Durada preferida del búfer IO de sortida d'àudio** — configura la durada del búfer d'entrada / sortida per a la reproducció d'àudio. Un valor típic per minimitzar la latència mentre reprodueixes àudio d'alta resolució és d'uns **5 mil·lisegons (0,005 segons)**. La mida de búfer acceptable depèn del teu entorn de maquinari i programari, de manera que prova diferents durades al teu dispositiu de destinació i tria la que millor equilibri la latència baixa i la reproducció sense errors.
- **Mode de sortida d'àudio (només iOS)** — configura el mode de sortida d'àudio barrejat perquè l'àudio de Flacbox es barreji amb altres aplicacions. Les instruccions detallades són [aquí](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Desar la posició de reproducció** — garanteix que l'aplicació desa i restaura la posició de reproducció de les cançons de la teva biblioteca de música.
- **Desar l'estat del reproductor d'àudio** — preserva l'estat del teu reproductor d'àudio abans que tanquis l'app. Per continuar la reproducció, toca **Continuar reproducció** a la part superior de qualsevol carpeta, àlbum, artista o gènere quan tornis a obrir l'app. També pots restaurar la reproducció de fitxers individuals tocant la pista específica.

Un cop hagis activat tant **Desar la posició de reproducció** com **Desar l'estat del reproductor d'àudio**, obre qualsevol carpeta, àlbum, artista o gènere i veuràs un botó **Continuar reproducció** a la part superior de la pantalla juntament amb l'última pista i posició desada. Toca'l per reprendre exactament on ho vas deixar.

### Personalització

La personalització et permet personalitzar l'aspecte de la pantalla del reproductor d'àudio, canviar els controls disponibles a la pantalla principal, la pantalla de bloqueig i la barra d'estat, i configurar els controls de salt de temps.

- **Estil de la pantalla del reproductor d'àudio** — configura la posició dels elements a la pantalla del reproductor d'àudio.
- **Estil de desplaçament de les portades d'àlbum** — configura l'estil de desplaçament preferit per a les portades d'àlbum.
- **Elements addicionals** — activa elements addicionals a la pantalla del reproductor d'àudio. **Informació del format d'àudio** mostra la informació d'àudio de la pista que s'està reproduint sobre la portada; **Control lliscant de volum d'àudio** mostra el control lliscant de sortida d'àudio sota els controls de reproducció.
- **Accions de la pantalla principal** — configura quins botons han d'estar visibles a la pantalla principal del reproductor d'àudio per defecte: **Mode de repetició i aleatori, Cançó següent i anterior, Salt de temps, Temporitzador de son, Google Chromecast, AirPlay i Bluetooth, Equalitzador d'àudio, Cerca, Marcadors, Velocitat, Afegir marcador, Afegir als favorits, Comentaris** i més.
- **Controls de reproducció a la pantalla de bloqueig** — tria quins controls apareixen a la pantalla de bloqueig. Valors possibles: **Salt de temps, Afegir marcador, Afegir als favorits**.
- **Botons de salt de temps** — tria l'interval de temps per als botons de **Salt de temps**.

### Càrrega de fitxers

Durant el procés de càrrega de fitxers, pots canviar el tipus de xarxa usat per carregar cançons. Opcions disponibles: **Wi-Fi**, **Wi-Fi i dades mòbils**.

- **Temps de precàrrega** — estableix l'interval de temps del búfer. Augmenta'l si tens una connexió de xarxa deficient.
- **Usar URL directa** — quan s'activa, s'usa una URL directa per carregar la cançó si el servidor ho permet. Això pot accelerar la càrrega de cançons però pot afectar l'estabilitat de la reproducció.

### Equalitzador d'àudio

Personalitza la configuració de l'equalitzador d'àudio. Pots llegir més sobre la configuració de l'equalitzador d'àudio [aquí](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Velocitat de reproducció

Ajusta la velocitat de reproducció del reproductor d'àudio de **0,02× a 3,00×**. Toca la icona de configuració a la cantonada superior dreta per canviar al **mode precís** per a ajustos més fins.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de velocitat de reproducció de Flacbox" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Correcció del to

Canvia la configuració de correcció del to usant els valors predefinits. També pots canviar entre valors predefinits i mode precís tocant el botó a la cantonada superior dreta. La correcció del to està disponible en el camí del còdec FFmpeg, amb un rang de **-1000 a +1000**.

### Memòria cau de reproducció

Les cançons a la cua del reproductor d'àudio es descarreguen automàticament per garantir una reproducció fluida. Si descarregues fitxers d'àudio manualment, pots desactivar aquesta opció per evitar duplicats. També pots configurar la mida de la memòria cau del reproductor d'àudio aquí.

### Temporitzador de son

Activa un temporitzador per aturar automàticament la reproducció després d'un període especificat — pràctic quan vols adormir-te amb música. Toca la icona de configuració a la cantonada superior dreta per al **mode precís** amb granularitat minut per minut.

## Accessibilitat

Flacbox és totalment accessible amb **VoiceOver**. Cada component té una etiqueta i una descripció ben dissenyades. Quan VoiceOver està actiu, l'app canvia al **Mode de text** perquè només es mostrin els elements significatius — millorant la velocitat de navegació i la claredat. També pots activar el Mode de text a **Configuració → Accessibilitat → Mode de text**.

### Ajust de lliscadors amb VoiceOver

1. **Selecciona el lliscador** — llisca cap a l'esquerra o la dreta fins que VoiceOver l'anunciï.
2. **Ajusta el valor** — toca dues vegades i mantén el lliscador premut, després arrossega cap amunt o cap avall per canviar el valor ràpidament. VoiceOver anuncia el nou valor a mesura que avances.

### Ajust de la posició d'una pista en una llista amb VoiceOver

1. Toca la icona de l'indicador de reordenació prop del títol de la pista per donar-li el focus.
2. Toca dues vegades ràpidament l'indicador de reordenació. Al segon toc, no alliberis el dit — mantén-lo premut fins que sentis un so que indica que la cel·la està llesta per ser moguda.
3. Mou la cel·la a la seva nova posició.

Els altres components funcionen com s'espera, utilitzant els patrons de VoiceOver proporcionats pel sistema.
