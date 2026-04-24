---
title: "Reprodueix la teva música des de Mac o PC a l'iPhone amb SMB"
description: "Aprèn com reproduir la teva col·lecció de música des de Mac o Windows PC al teu iPhone o iPad amb Evermusic i el protocol SMB. Una guia senzilla pas a pas per connectar i gaudir de l'àudio sense sincronitzar."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["reproduir música de Mac a iPhone", "streaming àudio SMB iOS", "configuració Evermusic SMB", "connectar música PC iPhone", "compartir música Mac iOS", "streaming fitxers SMB Windows", "accés Evermusic carpetes PC"]
---

{{< author-byline >}}


**Resum:** Utilitza l'aplicació Evermusic per a iPhone o iPad per reproduir música des del teu Mac o Windows PC a través de la teva xarxa local amb SMB. Sense sincronització, sense còpies -- simplement activa la compartició de fitxers al teu ordinador, connecta't a l'aplicació i reprodueix. La configuració triga menys de 5 minuts.

T'estàs ofegant en un mar de música al teu MAC o PC i vols gaudir-ne sense complicacions al teu iPhone o iPad? No busquis més que Evermusic. Amb Evermusic, és increïblement senzill connectar el teu ordinador utilitzant el protocol SMB i reproduir les teves melodies preferides sense preocupar-te per ocupar espai addicional al dispositiu o lidiar amb problemes de sincronització. Aquí tens una guia pas a pas per començar:

## Pas 1: Activa el protocol SMB al teu ordinador

![Evermusic - Suport SMB - Pantalla de compartició de Mac](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Si utilitzes MAC

- Obre Preferències del Sistema -> Compartició.
- Activa el servei de Compartició de Fitxers.
- A la secció "Carpetes compartides", afegeix la teva carpeta de música, selecciona un usuari i estableix els nivells de permisos (Lectura i Escriptura o Només Lectura).
- Per a més comoditat, pots seleccionar "Tothom: Només Lectura" per a la carpeta de música, fent-la fàcilment accessible a Evermusic.
- No oblidis recordar la URL del teu ordinador (smb://192.168.xx.xx) per als passos següents.

![Evermusic - Suport SMB - Pantalla de compartició de fitxers](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Toca "Opcions" i activa "Compartir fitxers i carpetes amb SMB."
- Activa "Compartició de fitxers de Windows" per als comptes disponibles.

![Evermusic - Suport SMB - Pantalla de compartició de fitxers i carpetes](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Si utilitzes un Windows PC

![Evermusic - Suport SMB - Compartir fitxers a Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Fes clic dret a la teva carpeta de música.
- Selecciona "Propietats."
- Obre la pestanya "Compartició."
- Fes clic a "Compartir..."
- Tria les persones amb qui vols compartir i estableix els seus nivells de permisos.
- Com amb MAC, pots optar per "Tothom: Lectura" per a la carpeta de música seleccionada.
- Fes clic a "Fet" per desar la configuració.

![Evermusic - Suport SMB - Carpeta compartida a Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Pas 2: Afegeix el teu ordinador automàticament

- Ara, obre Evermusic i ves a la pestanya "Connexions" ("Xarxa" si utilitzes una versió antiga de l'aplicació).
- Si veus el teu ordinador a la secció "Dispositius disponibles" ("Recursos compartits disponibles" si utilitzes una versió antiga de l'aplicació) i has seleccionat "Tothom: Només Lectura" al pas anterior, simplement toca el teu ordinador i es connectarà automàticament.
- Si això no passa, pots afegir el teu ordinador manualment.

![Evermusic - Suport SMB - Pantalla de connexió de compte](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Pas 3: Afegeix el teu ordinador manualment

- Toca "Connectar un servei al núvol" ("Afegir compte" si utilitzes una versió antiga de l'aplicació)
- Selecciona "SMB" de la llista de servidors disponibles a la pantalla següent.
- A la pantalla de configuració "SMB":
  - Introdueix la URL del servidor amb la ruta de la carpeta compartida. Pots introduir el nom del servidor o la IP del servidor. Per exemple:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Introdueix el teu Usuari i Contrasenya o deixa aquests camps en blanc si has seleccionat "Tothom: Només Lectura" al pas anterior.
  - El camp "WORKGROUP" és opcional i s'ha d'utilitzar si tens un domini Active Directory.

![Evermusic - Suport SMB - Pantalla d'introducció de credencials](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Un cop hagis connectat el teu compte SMB, apareixerà a la secció "Serveis al núvol" ("Comptes"). Obre el compte connectat tocant-lo, navega fins a la carpeta de música i toca qualsevol fitxer d'àudio per iniciar el reproductor.

![Evermusic - Suport SMB - Pantalla d'obrir carpeta connectada](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Gaudeix de la teva col·lecció de música sense problemes al teu iPhone o iPad amb Evermusic.

![Evermusic - Suport SMB - Pantalla del reproductor d'àudio](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Pas 4: Solució alternativa per a SMB2

Si trobes problemes navegant per carpetes o reproduint fitxers que contenen símbols especials (com ü, ö, é), això pot estar relacionat amb el protocol SMB2. Estem treballant activament per resoldre aquest problema.

Com a solució temporal, si us plau prova d'activar SMB 1 al teu servidor i a la configuració de l'aplicació. Alternativament, pots connectar-te al teu servidor SMB utilitzant el menú d'obertura de fitxers del sistema. Aquí tens com:

1. Navega a "Fitxers locals."
2. Desplaça't cap avall fins a la secció "Fitxers en aquest dispositiu" i toca "Obrir fitxers..." o "Obrir carpetes..."
3. Localitza el teu servidor i selecciona els fitxers o carpetes que necessites.
4. Toca "Obrir" per confirmar la teva selecció.

## Pas 5: Solució alternativa amb WebDAV

A més, pots provar de connectar-te al teu NAS utilitzant els protocols WebDAV o DLNA si són compatibles.

Seguint aquests passos, pots evitar els problemes relacionats amb símbols especials als noms de fitxers i continuar gaudint dels teus fitxers multimèdia.

P.D. També pots transferir fitxers d'àudio del teu MAC/PC al teu iPhone utilitzant la Compartició de Fitxers d'iTunes i reproduir fitxers d'àudio locals. Aprèn més sobre aquesta funció a la nostra guia: [Com reproduir fitxers d'iTunes a l'iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Preguntes freqüents

{{% details title="Puc reproduir música del meu PC al meu iPhone sense iTunes?" closed="true" %}}
Sí. Evermusic es connecta al teu PC via SMB a la teva xarxa Wi-Fi local. No cal iTunes. Simplement activa la compartició de fitxers al teu PC i connecta't a l'aplicació.
{{% /details %}}

{{% details title="El streaming SMB utilitza dades mòbils?" closed="true" %}}
No. SMB funciona a través de la teva xarxa Wi-Fi local. No cal connexió a Internet ni dades mòbils.
{{% /details %}}

{{% details title="Quins formats d'àudio suporta Evermusic via SMB?" closed="true" %}}
Evermusic suporta MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC i altres formats d'àudio comuns. Els fitxers es reprodueixen directament des del recurs compartit SMB.
{{% /details %}}

{{% details title="Puc reproduir música des d'un NAS al meu iPhone?" closed="true" %}}
Sí. Si el teu NAS suporta SMB (la majoria ho fan, incloent Synology, QNAP i WD My Cloud), pots connectar-t'hi utilitzant els mateixos passos d'aquesta guia.
{{% /details %}}

{{% details title="He de mantenir el meu ordinador encès mentre reprodueixo?" closed="true" %}}
Sí. Com que Evermusic reprodueix els fitxers directament des del teu ordinador, ha d'estar encès i connectat a la mateixa xarxa que el teu iPhone.
{{% /details %}}

{{% details title="Hi ha un límit de mida de fitxer per al streaming SMB?" closed="true" %}}
No. Evermusic reprodueix fitxers de qualsevol mida via SMB. Els fitxers grans sense pèrdua (FLAC, WAV) funcionen sense problemes.
{{% /details %}}
