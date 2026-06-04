---
title: "Configuració"
date: 2020-02-01
lastmod: 2026-06-01
description: "Explora cada configuració d'Evervideo — Reproductor multimèdia (Picture-in-Picture, descodificació per maquinari H.264/HEVC, equalitzador de vídeo, escalat, rotació, vista VR), Àudio (equalitzador, freqüència de mostreig, canals, buffer IO, mode mixt), Subtítols (primari/secundari, font, fitxer extern, libass), Biblioteca multimèdia, Gestor de fitxers, Wi-Fi Drive, Ginys, Personalització, Idioma, Codi d'accés, Còpia de seguretat i restauració — per a iPhone, iPad i Mac."
keywords: [
  "configuració Evervideo", "configuració reproductor de vídeo", "actualització premium Evervideo",
  "configuració Picture-in-Picture", "configuració equalitzador de vídeo",
  "mode d'escalat de vídeo", "rotació de vídeo", "descodificador per maquinari iPhone",
  "configuració subtítols", "subtítol secundari iOS", "configuració libass",
  "fitxer de subtítols extern", "font de subtítols",
  "configuració equalitzador d'àudio", "freqüència de mostreig de sortida d'àudio",
  "canals de sortida d'àudio", "durada del buffer IO", "mode mixt d'àudio",
  "Wi-Fi Drive vídeo", "ginys Evervideo",
  "còpia de seguretat i restauració Evervideo", "codi d'accés Evervideo",
  "idioma Evervideo", "personalització Evervideo"
]
tags: ["guia", "evervideo", "configuració"]
readingTime: 16
---


La pantalla de configuració és el centre de control d'Evervideo. Des d'aquí pots actualitzar a Premium, configurar els motors de vídeo i àudio (còdecs del sistema o FFmpeg), gestionar Picture-in-Picture, configurar subtítols (primaris, secundaris, libass, fitxers externs, fonts), organitzar la biblioteca multimèdia, configurar el gestor de fitxers, activar ginys de pantalla d'inici, fer còpies de seguretat de les dades i accedir a l'ajuda i informació legal. Les seccions s'agrupen sota encapçalaments: Compres i actualitzacions, Preferències de l'app, Ajuda, Legal i privadesa.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla principal de Configuració d'Evervideo" image="/docs/guide/evervideo/img/evervideo-settings.webp" >}}
{{< /cards >}}

## Actualitzar a Premium

Actualitza l'aplicació a la versió Premium per eliminar tots els límits. La versió gratuïta de l'aplicació ofereix una compra única per vida i dues opcions de subscripció (1 mes i 1 any) per eliminar totes les restriccions i actualitzar a Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Actualitzar a Premium a Evervideo" image="/docs/guide/evervideo/img/evervideo-upgrade-to-premium.webp" >}}
{{< /cards >}}

**Family Sharing** s'activa per a totes les compres i plans, de manera que pots compartir la versió Premium amb fins a cinc membres de la família sense cost addicional.

{{< cards cols="1">}}
  {{< card title="" subtitle="Seleccionar un pla Premium a Evervideo" image="/docs/guide/evervideo/img/evervideo-select-premium-plan.webp" >}}
{{< /cards >}}

## Compartir compres entre iOS i Mac

Les compres per vida i les subscripcions es comparteixen entre iOS i Mac usant **iCloud** per sincronitzar aquesta informació. Si tens Premium al dispositiu iOS, assegura't que tens instal·lada la versió més recent i que iCloud està activat. Inicia l'app a iOS i espera un minut perquè la informació de la compra es pugi a iCloud, i després llança la versió Mac — Premium hauria d'activar-se automàticament.

També pots tocar el botó **Restaurar compres** a la configuració de l'app. Assegura't de tenir connexió a Internet i d'haver iniciat sessió amb el mateix compte d'iCloud i App Store a tots dos dispositius.

## Restaurar compres en un dispositiu nou

Per restaurar la compra en un dispositiu nou, usa el menú **Compres → Restaurar compres**. Veuràs la llista de les compres. Si no veus totes les compres, confirma que el dispositiu està connectat al mateix Apple ID que es va usar per fer les compres, i assegura't que iCloud està activat.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menú de compres a la configuració d'Evervideo" image="/docs/guide/evervideo/img/evervideo-purhases-menu-in-settings.webp" >}}
{{< /cards >}}

## Prova Premium gratuïtament

Pots actualitzar a la versió Premium gratuïtament, durant un temps limitat, usant aquest menú. Simplement mira un anunci o explica als teus amics sobre l'app.

## Actualització de programari

Toca **Actualització de programari** per comprovar si hi ha una versió més nova d'Evervideo disponible a l'App Store.

## Novetats

Aquest menú és disponible després que es publica una nova versió. Mostra un resum dels canvis i les noves funcions de l'actualització més recent.

## Reproductor

Tot el relacionat amb la reproducció es troba aquí — àudio, vídeo, subtítols, dispositius, personalització, memòria cau i el temporitzador de son.

### General

Aquesta configuració cobreix els aspectes fonamentals del reproductor.

- **Mode de repetició** — tria com es comporta el reproductor quan acaba un vídeo:
  - **Repetir-ho tot** — reprodueix tots els vídeos de la cua.
  - **Repetir un** — repeteix només el vídeo actual.
  - **Aturar en acabar** — pausa quan el vídeo actual acaba.
  - **Sense repetició** — reprodueix la cua una vegada sense repetir.
- **Mode aleatori** — aleatoritza l'ordre dels vídeos a la cua (**Activat** o **Desactivat**).
- **Desar posició de reproducció** — desa i restaura la posició de reproducció per als vídeos de la biblioteca.
- **Desar estat del reproductor** — preserva l'estat del reproductor quan tanques l'app, perquè puguis reprendre des d'on ho vas deixar.

### Vídeo

Configura com Evervideo descodifica i renderitza el vídeo.

- **Descodificació per maquinari H.264** — activa/desactiva la descodificació AVC accelerada per maquinari. Usa quan l'rendiment de la bateria i tèrmic és important; desactiva per a compatibilitat amb perfils exòtics.
- **Descodificació per maquinari H.265 (HEVC)** — el mateix per a HEVC. Els iPhones, iPads i Macs moderns descodifiquen HEVC eficientment.
- **Format de píxel preferit** — tria el format de píxel que el reproductor presenta al renderitzador (els valors predeterminats estan ajustats per al dispositiu).
- **FPS preferit** — estableix un FPS de reproducció objectiu. Útil per coincidir amb una freqüència d'actualització de monitor específica.
- **Mode d'escalat de vídeo** — Ajustar/Omplir/Estirar/Original. Determina com la imatge omple l'àrea de visualització.
- **Mode de visualització de vídeo** (iOS/iPadOS) — com es presenta el vídeo a la vista del reproductor.
- **Rotació de vídeo** — gira manualment la imatge 0°/90°/180°/270° (útil per a vídeos gravats amb l'orientació incorrecta).
- **Equalitzador de vídeo** — ajusta la brillantor, el contrast, la saturació i el to amb una previsualització en temps real. Els presets personalitzats es poden **exportar i importar**.
- **Vista VR** (iOS/iPadOS) — per a vídeos esfèrics de 360°. Arrossega per mirar al voltant, apropa els dits per fer zoom.
- **Picture-in-Picture (PiP)** (iOS/iPadOS) — activa el suport PiP; l'app canviarà a una finestra de reproductor flotant quan posis l'app al segon pla o toquis el botó PiP.

### Àudio

Configura la reproducció i sortida d'àudio.

- **Pista d'àudio** — tria el flux d'àudio quan un vídeo en té múltiples (comentari, doblatge, etc.).
- **Equalitzador d'àudio** — EQ de 10 bandes amb presets i un preamplificador. Els presets personalitzats es poden exportar/importar.
- **Freqüència de mostreig de sortida d'àudio** — 44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz, 96 kHz. Útil amb DACs externs.
- **Nombre de canals de sortida d'àudio** — Mono, Estèreo, 5.1, ITU BS.775-1, SDDS i més.
- **Durada preferida del buffer IO de sortida d'àudio** — el valor típic per a reproducció d'alta resolució i baixa latència és d'uns 5 ms (0,005 s). Ajusta per al maquinari.
- **Mode de sortida d'àudio** (només iOS) — el mode mixt permet que l'àudio d'Evervideo es barregi amb altres apps.

### Subtítols

Evervideo inclou suport integral de subtítols.

- **Pista de subtítols** — tria de les pistes de subtítols incrustades al fitxer.
- **Fitxer de subtítols extern** — carrega un fitxer `.srt`, `.vtt`, `.ass` o `.ssa` extern del dispositiu o qualsevol servei al núvol connectat.
- **Font** — tria una font per a la pista de subtítols primaris.

### Dispositius (només iOS/iPadOS)

Tria un dispositiu **AirPlay** o **Google Chromecast** per a la sortida de vídeo.

### Personalització

- **Estil de disseny del reproductor** — Mínim (per defecte per a Evervideo), Inferior, Antic, Clàssic i més.
- **Accions de pantalla principal** — tria quins botons apareixen a la pantalla principal del reproductor.
- **Controls de pantalla de bloqueig** — Saltar temps, Afegir marcador, Afegir als preferits.
- **Intervals de temps de salt** — tria l'interval de temps per als botons de salt (5 s, 10 s, 15 s, 30 s, etc.).
- **Estil de desplaçament de portades d'àlbums** — estil de desplaçament preferit per a la imatge de portada.
- **Elements addicionals** — informació de format d'àudio, control lliscant de volum.

### Càrrega de fitxers

Configura com es transmet les dades de vídeo des de la xarxa.

- **Tipus de xarxa** — només Wi-Fi, o Wi-Fi + Dades mòbils.
- **Temps de precàrrega** — longitud del buffer per a una reproducció més fluida en xarxes lentes.
- **Usar URL directa** — quan s'admet, usa una URL directa per a una càrrega més ràpida.

### Memòria cau de reproducció

Els vídeos a la cua del reproductor es descarreguen automàticament per garantir una reproducció fluida. Pots desactivar aquesta opció o configurar la mida de la memòria cau aquí.

### Temporitzador de son

Activa un temporitzador per aturar automàticament la reproducció després d'un període especificat. Toca la icona de configuració per al **mode precís** amb granularitat minut a minut.

## Biblioteca multimèdia

Gestiona la sincronització automàtica, les metadades, les portades d'àlbums, les llistes de reproducció, els recents i els preferits.

### Lectura de metadades

Quan afegeixes vídeos a la biblioteca, el lector de metadades els escaneja en segon pla i els organitza per àlbum i gènere. Pots ajustar la velocitat d'escaneig, desactivar el lector o activar un escaneig complet nou amb **Tornar a carregar metadades**. **Normalitzar codificació de metadades** corregeix automàticament les codificacions de caràcters trencades (comú amb fitxers de PC amb Windows).

### Sincronització en línia

Afegeix automàticament vídeos dels serveis al núvol connectats i els servidors multimèdia a la biblioteca. Tria quines carpetes escanejar, configura amb quina freqüència l'app hauria de sincronitzar i inicia/atura manualment la sincronització. La sincronització en línia només s'executa mentre l'app és activa — per a biblioteques grans, usa la versió d'escriptori i transfereix la biblioteca sincronitzada amb **Còpia de seguretat i restauració**.

### Sincronització fora de línia

Quan marques una carpeta al núvol com a disponible fora de línia, apareix a **Fitxers → Carpetes fora de línia** i es descarrega automàticament. Els fitxers nous afegits en línia també es descarreguen. Configura l'interval de temps i inicia sincronitzacions manuals des d'aquesta pantalla.

### Personalització

- **Estil de pantalla de biblioteca multimèdia** — Menú pla, Menú agrupat, Menú amb pestanyes.
- Alterna si cal mostrar portades d'àlbums grans a les pantalles de detalls.

### Portades d'àlbums

- **Tipus de xarxa** — Wi-Fi o Wi-Fi + Dades mòbils.
- **Carregar portades d'àlbums per a fitxers en línia** — extreu l'art integrat dels fitxers al núvol (usa dades addicionals).
- **Cercar a la carpeta** — usa imatges JPEG/PNG de la mateixa carpeta quan un vídeo no té portada integrada.
- **Qualitat de portada** — ajusta la resolució a la qual es guarden les portades a la memòria cau.
- **Mostrar a la carpeta** / **Eliminar totes** — gestiona la memòria cau de les portades.

### Llistes de reproducció

Activa l'afegiment del mateix vídeo a una llista de reproducció dues vegades (desactivat per defecte).

### Recents

Gestiona la llista de vídeos reproduïts recentment — canvia la mida, elimina o exporta com a M3U/CSV/TXT.

### Preferits

- **Edició simultània** — reflecteix els preferits entre la biblioteca multimèdia i la secció de fitxers.
- **Eliminar llista** — neteja la llista de preferits.
- **Exportar llista de cançons** — exporta els preferits com a M3U/CSV/TXT.

### Eliminar biblioteca multimèdia

Esborra la base de dades de la biblioteca multimèdia. Els fitxers de vídeo i àudio a l'emmagatzematge no s'eliminen.

## Codi d'accés

Protegeix Evervideo amb un **codi d'accés numèric de 4 dígits**. Quan s'activa, se't demanarà que introdueixis el codi d'accés cada vegada que l'app s'inicia. Combina'l amb Face ID/Touch ID d'iOS al dispositiu per a una protecció addicional.

## Gestor de fitxers

Controla com es transfereixen, emmagatzemen i previsualitzen els fitxers.

- **Transferències de fitxers** — preferència de xarxa (només Wi-Fi o Wi-Fi + Dades mòbils).
- **Nombre màxim de tasques en paral·lel** — estableix el nombre de fils de descàrrega en paral·lel.
- **Tasques de transferència de fitxers** — mostra les càrregues i descàrregues actives.
- **Transferències en segon pla** — permet descàrregues mentre l'app és en segon pla.
- **Desar fitxers descarregats a** — directori de descàrregues per defecte.
- **Carpetes offline sincronitzades** — gestiona les carpetes en mode fora de línia.
- **Interval de temps** — amb quina freqüència es comproven les carpetes fora de línia per si hi ha canvis.
- **Mostrar noms de fitxers complets** — mostra extensions al gestor de fitxers.
- **Editar fitxers en línia** — desactiva per canviar al mode de només lectura per als serveis al núvol connectats.
- **Copiar fitxers en obrir** — com gestionar els fitxers importats d'altres apps.
- **Miniatures per als fitxers** — gestiona les miniatures de fitxers generades.
- **Eliminar fitxers temporals** — neteja la carpeta de memòria cau de l'aplicació.

## Wi-Fi Drive

Activa Wi-Fi Drive per transferir fitxers d'un ordinador al dispositiu usant un navegador web d'escriptori, Finder o Explorador de fitxers. Les instruccions detallades estan disponibles [aquí](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Ginys

Activa els ginys perquè l'app actualitzi les dades dels ginys durant la reproducció. Les actualitzacions de ginys requereixen energia addicional, de manera que el commutador està desactivat per defecte — activa'l només si realment uses ginys a la pantalla d'inici o de bloqueig.

Pots afegir ginys d'Evervideo mantenint premuda la pantalla d'inici o de bloqueig, tocant **+**, cercant **Evervideo** i triant una mida de giny. Els ginys mostren el vídeo que s'està reproduint i es dirigeixen directament al reproductor a pantalla completa. Els ginys també funcionen a macOS al Centre de notificacions.

## Personalització

Personalitza la interfície d'usuari segons les teves preferències.

- **Icona de l'aplicació** — icona alternativa de la pantalla d'inici (Premium).
- **Esquema de colors** — Fosc, Clar o Per defecte (segueix l'aparença del sistema).
- **Estil de fons** — portada d'àlbum difuminada o color sòlid.
- **Aparença dels elements de la llista** — ajusta automàticament l'alçada de la fila; mostra miniatures més petites.
- **Límit de càrrega de contingut** — activa/desactiva la paginació.
- **Estil de pantalla de fitxers** — Menú pla o Menú agrupat.
- **Estil de pantalla de biblioteca multimèdia** — Menú pla/agrupat/amb pestanyes.
- **Estil de pantalla del reproductor** — Mínim/Inferior/Antic/Clàssic.
- **Estil de menú contextual** — menú del sistema o estil de full inferior.

## Finestra

Disponible al Mac i Catalyst. Configura les preferències relacionades amb la finestra com la mida per defecte i el comportament en iniciar.

## Pantalla

Tria si la pantalla ha de romandre activa mentre uses l'aplicació.

## Accessibilitat

Activa el **Mode de text** per amagar les imatges a la interfície d'usuari. El Mode de text s'activa automàticament quan VoiceOver és actiu.

## Idioma

Canvia l'idioma de l'aplicació i substitueix el valor predeterminat del sistema. El canvi s'aplica després de tancar completament i tornar a obrir Evervideo. S'admeten més de 120 idiomes.

## Còpia de seguretat i restauració

Fes una còpia de seguretat de totes les dades de l'aplicació o migra-les a un altre dispositiu. Tria el que vols incloure:

- **Base de dades** — entrades de la biblioteca multimèdia, llistes de reproducció, valoracions, preferits, historial de visualitzacions. Els fitxers fora de línia no s'inclouen per mantenir la mida del fitxer manejable.
- **Portades d'àlbums** — l'art de portada emmagatzemat a la memòria cau.
- **Configuració** — la configuració de l'aplicació.

Toca **Fer còpia de seguretat de les dades de l'aplicació** per iniciar la còpia de seguretat. Per restaurar en un dispositiu nou, mou el fitxer de còpia de seguretat via iCloud Drive, AirDrop o qualsevol servei al núvol connectat i obre'l al nou dispositiu.

## Ajuda

Accedeix a la guia de l'aplicació per obtenir assistència i orientació sobre l'ús efectiu de l'app.

## Preguntes freqüents

Troba respostes a les preguntes habituals a la secció de Preguntes freqüents.

## Enviar comentaris

Envia els teus comentaris a l'equip de suport directament des de l'app, amb informació de diagnòstic adjunta automàticament.

## Compartir aquesta app

Comparteix Evervideo amb els teus amics per fer-la conèixer.

## Descobrir més apps

Explora altres apps d'Everappz.

## Termes i condicions

Llegeix els termes i condicions abans d'usar l'aplicació.

## Política de privadesa

Llegeix la política de privadesa per entendre les nostres pràctiques de gestió de dades.

## Analítiques i recollida de dades

Comprova quins serveis estan activats per a l'analítica i la recollida de dades i desactiva'n qualsevol que no vulguis.

## Avisos legals

Informació sobre cada biblioteca usada a l'aplicació juntament amb el número de versió de l'app i la informació de construcció.
