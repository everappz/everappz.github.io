---
title: "Reproductor multimèdia"
date: 2020-02-01
lastmod: 2026-06-01
description: "Aprèn a usar el reproductor multimèdia d'Evervideo a iPhone, iPad i Mac. Picture-in-Picture, descodificació H.264/HEVC accelerada per maquinari, equalitzadors d'àudio i vídeo, subtítols primaris i secundaris, selecció de pistes d'àudio i vídeo, escalat i rotació de vídeo, velocitat de reproducció, temporitzador de son, AirPlay 2, Google Chromecast, transmissions RTSP i el reproductor compacte sempre visible."
keywords: [
  "guia reproductor Evervideo", "configuració reproductor de vídeo", "equalitzador Evervideo",
  "Picture-in-Picture iPhone", "PiP vídeo iPad", "PiP vídeo Mac",
  "AirPlay 2 vídeo", "Google Chromecast vídeo",
  "subtítols vídeo iPhone", "subtítols SRT externs",
  "reproductor subtítols ASS SSA", "libass iOS",
  "subtítols dobles aprenentatge d'idiomes",
  "equalitzador vídeo brillantor contrast", "equalitzador àudio reproductor vídeo",
  "bloqueig rotació reproductor vídeo", "mode escalat vídeo iOS",
  "descodificador H.264 per maquinari iPhone", "descodificador HEVC per maquinari iPad",
  "velocitat reproducció vídeo", "reproductor vídeo FFmpeg iOS",
  "reproductor RTSP iPhone", "reproductor vídeo compacte",
  "reproductor vídeo VR 360 iPhone"
]
tags: ["guia", "evervideo", "reproductor", "PiP", "subtítols", "equalitzador de vídeo"]
readingTime: 14
---


El reproductor multimèdia és la pantalla principal de l'app on controles la reproducció i la majoria de funcions d'Evervideo. Reprodueix fitxers de vídeo i àudio i està construït sobre un reproductor personalitzat basat en FFmpeg amb descodificació H.264 i HEVC accelerada per maquinari que fa el treball pesat. Explorem com usar-lo.

## Accedir al reproductor multimèdia

Pots arribar al reproductor a pantalla completa des de la barra del reproductor compacte. A l'iPhone, el reproductor compacte es troba a la part superior de la pantalla principal. A l'iPad i al Mac, es troba al costat esquerre (o a la part superior del panell principal). Per plegar el reproductor a pantalla completa de nou a la vista compacta, toca el botó de tancament a la cantonada inferior dreta o llisca cap avall. Per amagar completament el reproductor compacte, toca i llisca cap avall una vegada més.

El reproductor compacte es manté visible mentre navegues per la biblioteca, el gestor de fitxers o la configuració, de manera que mai perds el vídeo mentre busques el pròxim.

{{< cards cols="1">}}
  {{< card title="" subtitle="Reproductor multimèdia a pantalla completa d'Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Formats de vídeo i àudio compatibles

Evervideo reprodueix pràcticament tots els contenidors i còdecs moderns a través del motor FFmpeg inclòs, amb descodificació H.264 i HEVC accelerada per maquinari als dispositius compatibles.

- **Contenidors de vídeo:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — i molts més.
- **Còdecs de vídeo:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — a més de pràcticament qualsevol altre còdec que FFmpeg admet.
- **Còdecs d'àudio:** AAC, MP3, FLAC, ALAC, OGG/Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — i molts més.
- **Formats de subtítols:** SRT, VTT (WebVTT), ASS/SSA i pistes de subtítols de text o imatge incrustades.
- **Protocols de transmissió:** HTTP/HTTPS, HLS (m3u8), RTSP (càmeres IP i IPTV) i transmissió directa de fitxers via SMB/WebDAV/FTP/SFTP/NFS/DLNA.

Això cobreix pràcticament qualsevol fitxer de vídeo que puguis trobar — incloent còpies MKV, transmissions RTSP de càmeres de seguretat i descàrregues web AV1 webm.

## Controls de reproducció

A la part inferior de la pantalla del reproductor, veuràs botons de Reproduir, Pausar, Següent i Anterior. També hi ha botons opcionals com Saltar endavant i Saltar enrere (10 segons per defecte) que pots activar a la configuració de l'app. Mantén premuts els botons Següent/Anterior per avançar o retrocedir ràpidament. Arrossega el lliscador de reproducció per saltar a qualsevol posició.

## Repetició i aleatori

Toca el botó de repetició per ciclar pels modes de repetició:

- **Repetir-ho tot** — repeteix tots els vídeos de la cua.
- **Repetir un** — repeteix només el vídeo actual.
- **Aturar en acabar** — pausa quan el vídeo actual acaba.
- **Sense repetició** — reprodueix la cua una vegada sense repetir.

Usa el botó **Aleatori** per aleatoritzar l'ordre dels vídeos a la cua.

## Picture-in-Picture (PiP)

A iPhone i iPad, Evervideo és compatible amb Picture-in-Picture (PiP). Toca la icona PiP a la pantalla del reproductor o simplement envia Evervideo al segon pla — el vídeo continua reproduint-se en una finestra flotant per sobre de qualsevol altra app. Arrossega la finestra flotant a qualsevol cantonada; apropa els dits per canviar la mida; toca una vegada per mostrar els controls bàsics de reproduir/pausar/saltar; toca el petit botó d'expandir per tornar a Evervideo complet.

PiP funciona amb tots els formats de vídeo que reprodueix Evervideo, incloent fitxers transmesos des del núvol i transmissions RTSP. PiP també continua funcionant mentre el telèfon està bloquejat (depenent de la configuració de bloqueig automàtic).

## Reproductor compacte

El reproductor compacte és un mini reproductor persistent que es manté visible a la part superior de cada pantalla de l'app mentre navegues per la biblioteca, el gestor de fitxers o la configuració. Toca'l per expandir-lo al reproductor a pantalla completa; llisca cap avall per plegar-lo de nou.

{{< cards cols="1">}}
  {{< card title="" subtitle="Configuració de vídeo des del reproductor compacte a la pantalla principal d'Evervideo" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

Per a AirPlay, toca el botó AirPlay al reproductor. Evervideo admet AirPlay 2, de manera que pots transmetre vídeo a Apple TV, HomePod o qualsevol altaveu o televisió intel·ligent compatible amb AirPlay 2. En una configuració amb múltiples dispositius AirPlay, pots enviar l'àudio a múltiples receptors simultàniament.

## Google Chromecast

Per als usuaris de Google Cast, la icona Cast apareix al reproductor. Toca-la per triar un dispositiu i iniciar la retransmissió. Assegura't que el telèfon i el receptor Cast estiguin a la mateixa xarxa Wi-Fi. No tots els còdecs estan suportats pel maquinari Chromecast — alguns fitxers poden necessitar transcodificació.

## Transmissions RTSP en directe

Evervideo pot reproduir fonts RTSP directament — càmeres IP, càmeres de timbre, transmissions IPTV, feeds de difusió i qualsevol URL `rtsp://`. Afegeix la transmissió com una connexió RTSP a Fitxers → Enllaços en línia → Afegir enllaç i toca-la per començar a veure. Les transmissions RTSP funcionen en Picture-in-Picture, el reproductor compacte, i es retransmeten via AirPlay 2 i Chromecast com un vídeo normal.

## Selecció de pista d'àudio

Per a vídeos amb múltiples pistes d'àudio (comentaris, doblatges en idiomes alternatius, pistes del director), toca el botó Més accions al reproductor i tria Pista d'àudio — i tria la pista que vols. Essencial per a pel·lícules en idiomes estrangers, fitxers BDMV/MKV amb múltiples doblatges i contingut d'instrucció amb pistes de comentaris.

## Selecció de pista de vídeo

Alguns fitxers de vídeo inclouen múltiples fluxos de vídeo (Blu-rays de múltiples angles, talls alternatius). Tria Pista de vídeo del menú Més accions per canviar entre ells durant la reproducció.

## Subtítols — interns i externs

Evervideo et dóna un control precís sobre els subtítols:

- **Pista de subtítols** — tria de les pistes incrustades al fitxer.
- **Fitxers de subtítols externs** — carrega fitxers `.srt`, `.vtt`, `.ass` o `.ssa` del dispositiu, iCloud Drive o qualsevol servei al núvol connectat.
- **Renderització Libass** — l'estil avançat ASS/SSA (fonts, colors, posicions, efectes de karaoke) es renderitza correctament gràcies a la biblioteca libass inclosa.
- **Selecció de font** — tria una font personalitzada per a la pista de subtítols primaris i una font independent per als subtítols secundaris. Les fonts incloses més qualsevol font instal·lada al dispositiu estan disponibles.

Pots configurar tot això a Configuració → Subtítols abans de la reproducció, o usar Més accions → Subtítols des del reproductor per canviar sobre la marxa.

## Equalitzador d'àudio

Evervideo inclou un equalitzador d'àudio complet per ajustar les bandes sonores de vídeo per als teus auriculars, altaveus o equip de so. Toca la icona de l'equalitzador a la vista de volum (o l'acció Equalitzador d'àudio al menú Més accions del reproductor), activa l'equalitzador amb el commutador a la cantonada superior dreta, i tria un preset o arrossega els lliscadors de banda per crear el teu propi preset. Els presets personalitzats es poden exportar i importar per compartir-los entre dispositius o fer-ne una còpia de seguretat.

## Equalitzador de vídeo

Per ajustar la imatge, Evervideo proporciona un equalitzador de vídeo dedicat — ajusta la brillantor, el contrast, la saturació i el to en temps real durant la reproducció. Com l'equalitzador d'àudio, els presets de vídeo personalitzats es poden exportar i importar per a compartir o fer còpia de seguretat. Usa'l per aclarir una escena fosca en un dia assolellat, potenciar la saturació de contingut esblaimat o escalfar una dominanta de color freda.

{{< cards cols="1">}}
  {{< card title="" subtitle="Equalitzador de vídeo d'Evervideo" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Mode d'escalat de vídeo

Tria com el vídeo omple la pantalla:

- **Ajustar** — conserva la relació d'aspecte original; barres negres on calgui.
- **Omplir** — omple tota la pantalla, retallant el vídeo si cal.
- **Estirar** — estira el vídeo per omplir la pantalla, distorsionant si cal.
- **Original** — manté la resolució nativa a 1:1.

## Rotació de vídeo

Per a vídeos gravats amb l'orientació incorrecta, tria **Més accions → Rotació** i selecciona **0°**, **90°**, **180°** o **270°** per girar la imatge sense sortir del reproductor.

## Descodificació per maquinari (H.264 i HEVC)

A Configuració → Reproductor → Vídeo, pots activar/desactivar la descodificació per maquinari H.264 i la descodificació per maquinari H.265 (HEVC) de manera independent. La descodificació per maquinari és més ràpida, usa menys bateria i funciona més fresca — però en casos rars (fitxers corruptes, perfils exòtics) pot ser necessari desactivar la descodificació per maquinari i recórrer a la descodificació per programari FFmpeg. Evervideo et permet fer-ho fitxer per fitxer des del menú Més accions del reproductor.

## Vista VR 360°

Evervideo inclou una vista VR/360° per a fitxers de vídeo esfèrics. En reproduir un vídeo de 360°, pots arrossegar per mirar al voltant, apropar els dits per fer zoom, i Evervideo deformarà la renderització en temps real.

## Velocitat de reproducció

Toca el control de Velocitat a la barra d'eines del reproductor per canviar la velocitat de reproducció — alenteix per a anàlisi (0,25× o 0,5×) o accelera per a tutorials i classes (1,25×, 1,5×, 2× i fins a 3×). Toca la icona de configuració a la cantonada superior dreta de la pantalla de Velocitat per canviar al mode precís amb ajustos més fins. La correcció de to per pista també és disponible.

{{< cards cols="1">}}
  {{< card title="" subtitle="Velocitat de reproducció d'Evervideo a la barra d'eines principal" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Cua del reproductor

Per veure la cua del reproductor, toca el botó de cua al reproductor. Cada vídeo a la cua té més accions — toca els tres punts per veure'ls. Per reordenar un vídeo a la cua, usa l'indicador de reordenació a prop del títol i arrossega'l a una nova posició.

{{< cards cols="1">}}
  {{< card title="" subtitle="Cua de reproducció d'Evervideo" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Temporitzador de son

Obre Configuració → Reproductor → Temporitzador de son, activa'l i tria quant de temps vols que continuï la reproducció abans d'aturar-se automàticament. També pots afegir el botó del Temporitzador de son directament a la pantalla principal del reproductor via Configuració → Reproductor → Personalització → Accions de pantalla principal.

## Marcadors del reproductor

Desa el lloc en vídeos llargs — classes, audiolibres en vídeo, tutorials, descàrregues de YouTube d'una hora — tocant Afegir marcador al menú Més accions. Els marcadors apareixen a la llista Més accions → Marcadors del vídeo i persisteixen entre sessions.

## Menú Més accions

Toca el botó **Més accions "..."** al reproductor per accedir a funcions addicionals.

- **Continuar reproducció** — reprèn la cua des de l'última posició.
- **Cerca** — troba un vídeo específic a la cua.
- **Marcadors** — mostra i salta als marcadors.
- **Velocitat** — ajusta la velocitat de reproducció.
- **Recents** — vídeos reproduïts recentment.
- **Preferits** — vídeos preferits.
- **Equalitzador d'àudio** — activa l'equalitzador d'àudio.
- **Equalitzador de vídeo** — activa l'equalitzador de vídeo.
- **Pista d'àudio** — tria el flux d'àudio.
- **Pista de vídeo** — tria el flux de vídeo.
- **Subtítols** — pista primària/secundària, fitxer extern, font.
- **Rotació** — gira la imatge 0°/90°/180°/270°.
- **Mode d'escalat** — Ajustar/Omplir/Estirar/Original.
- **Picture-in-Picture** — entra al mode PiP.
- **AirPlay** / **Chromecast** — envia a un dispositiu.
- **Temporitzador de son** — estableix un temporitzador per aturar la reproducció.
- **Desar la cua com a llista de reproducció** — desa la cua actual com una nova llista de reproducció.
- **Eliminar la cua** — neteja la cua i atura la reproducció.
- **Configuració** — salta directament a la configuració del reproductor.
- **Ajuda** — obre l'orientació.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla Més accions del reproductor d'Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Configuració del reproductor

L'arbre complet de configuració del reproductor està documentat a la [guia de Configuració](/docs/guide/evervideo/evervideo-guide-settings/). Les seccions més usades:

- **General** — mode de repetició, mode aleatori, desar estat del reproductor, desar posició de reproducció, intervals de salt.
- **Vídeo** — descodificació per maquinari H.264/HEVC, equalitzador de vídeo, mode d'escalat, rotació, mode de visualització, FPS preferit, format de píxel preferit, vista VR.
- **Àudio** — equalitzador d'àudio, freqüència de mostreig, canals, durada del buffer IO, mode mixt.
- **Subtítols** — pista primària/secundària, selecció de fitxer extern, font, font secundària.
- **Dispositius** (iOS) — AirPlay/Chromecast.
- **Personalització** — estil de disseny del reproductor (Mínim/Inferior/Antic/Clàssic), accions de pantalla principal, controls de pantalla de bloqueig.
- **Memòria cau de reproducció** — memòria cau de disc per a una transmissió més fluida.
- **Temporitzador de son** — aturada automàtica.

## Accessibilitat

Evervideo és totalment accessible amb VoiceOver. Cada component té una etiqueta i descripció ben dissenyades. Quan VoiceOver està actiu, l'app canvia al Mode de text perquè només es mostrin els elements significatius — millorant la velocitat de navegació i la claredat. També pots activar el Mode de text a Configuració → Accessibilitat → Mode de text.

### Ajustar lliscadors amb VoiceOver

1. **Selecciona el lliscador** — llisca a l'esquerra o dreta fins que VoiceOver l'anunciï.
2. **Ajusta el valor** — toca dues vegades i mantén el lliscador, i després arrossega amunt o avall per canviar el valor ràpidament. VoiceOver anuncia el nou valor mentre vas ajustant.

Els altres components funcionen com s'espera, usant els patrons VoiceOver proporcionats pel sistema.
