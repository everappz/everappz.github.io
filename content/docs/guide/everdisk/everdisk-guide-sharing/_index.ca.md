---
title: "Compartir"
date: 2026-08-20
description: "Aprèn com funciona la compartició a Everdisk: prem Iniciar per convertir el teu iPhone o iPad en una unitat sense fil, tria què compartir (arxius, carpetes, fotos i música), fes funcionar els quatre servidors (DLNA, HTTP, WebDAV, FTP), consulta les adreces de connexió, mira qui està connectat i mantén la compartició activa per Wi-Fi o per cable USB."
keywords: ["compartir Everdisk", "unitat sense fil iPhone", "iniciar compartició", "compartir arxius iPhone", "compartir fotos per xarxa", "DLNA HTTP WebDAV FTP", "què compartir", "com connectar", "mantenir l'app oberta", "compartir per Wi-Fi o cable USB"]
tags: ["everdisk", "guia", "compartir"]
readingTime: 9
---


La pestanya **Compartir** és el cor d'Everdisk. És on converteixes el teu iPhone o iPad en una unitat sense fil, tries exactament què vols compartir i obtens les adreces que fan servir els altres dispositius per connectar-s'hi. És la primera pestanya que veus quan obres l'app.

## Iniciar i aturar la compartició

Al centre de la pantalla de Compartir hi ha un botó rodó gran.

- Prem **Iniciar** per posar en línia tots els servidors que tinguis activats alhora. El botó mostra **Iniciant...** i després **Aturar** un cop la compartició és activa.
- Prem **Aturar** per tornar-ho a posar tot fora de línia. Els dispositius connectats es desconnecten.

Mentre la compartició està en marxa, els arxius, fotos i música que has triat estan disponibles per a qualsevol dispositiu de la mateixa xarxa que es connecti amb un dels quatre mètodes de sota.

> La compartició només funciona mentre l'app està oberta. Consulta **Mantén l'app oberta** al final d'aquesta pàgina per saber-ne el motiu i com mantenir en marxa les transferències grans.

## Tria què compartir

Abans de començar, prem la capçalera **Què compartir** per obrir tres grups. Pots compartir qualsevol combinació d'aquests i has de triar com a mínim una cosa abans que la compartició pugui començar.

**Arxius i carpetes**

- La carpeta **Documents** pròpia de l'app es comparteix per defecte. La pots deixar de compartir si ho prefereixes.
- Prem **Afegir carpeta** per compartir una carpeta de qualsevol lloc del teu dispositiu, o **Afegir arxiu** per compartir arxius individuals.
- Cada element compartit té un botó **Informació** i un botó **Deixar de compartir**.

**Fotos i vídeos**

- Activa **Permetre l'accés a tota la Fototeca** per compartir tota la teva biblioteca de fotos i vídeos, o bé
- Prem **Afegir fotos** per triar a mà només les fotos i vídeos que vols compartir.

**Música**

- Activa **Permetre l'accés a tota la Biblioteca de música** per compartir tota la teva biblioteca de música, o bé
- Prem **Afegir pistes** per compartir només cançons concretes.
- Les pistes protegides (DRM) o desades només al núvol no es poden compartir.

Si intentes iniciar sense res seleccionat, Everdisk mostra un avís de **Res per compartir**. Si canvies què es comparteix mentre la compartició està en marxa, **atura-la i torna a iniciar-la** per aplicar el canvi.

## Els quatre servidors

Everdisk comparteix el mateix contingut de quatre maneres alhora. Cadascuna està pensada per a un tipus de dispositiu diferent i cadascuna es pot activar o desactivar a **Configuració → Compartir → Connexions**. Per defecte les quatre estan activades.

- **TV i Centre multimèdia (DLNA)**: per a televisors i reproductors intel·ligents. Descobreixen el teu dispositiu ells sols i mostren les teves fotos, vídeos i música, amb miniatures de previsualització.
- **Navegador (HTTP)**: per a qualsevol telèfon, tauleta o ordinador. L'altra persona obre un enllaç al navegador per explorar i descarregar els teus arxius. No cal instal·lar res.
- **Ordinador (WebDAV)**: per a un Mac, un PC amb Windows o una màquina Linux. El teu dispositiu apareix com una unitat de xarxa normal, de manera que pots arrossegar arxius en totes dues direccions.
- **Altres apps i dispositius (FTP)**: per a apps d'arxius i usuaris avançats que utilitzen FTP.

Per veure instruccions de connexió pas a pas per a cada tipus, consulta [Connecta els teus dispositius](/docs/guide/everdisk/everdisk-guide-connect).

## Com connectar i adreces de connexió

Després de prémer Iniciar, la secció **Com connectar** mostra una targeta per a cada servidor actiu amb l'**adreça** exacta que has d'escriure a l'altre dispositiu. Cada adreça és fàcil de copiar: prem-la per copiar-la, fes servir el botó **Compartir** per enviar-la, o prem el botó **d'informació (ⓘ)** per veure instruccions detallades específiques de cada protocol.

- La targeta DLNA mostra una adreça de descripció del dispositiu que acaba en `/device-desc.xml` per als reproductors que en demanen una.
- Quan el teu dispositiu està connectat a un Mac amb un cable, apareix una adreça addicional amb una etiqueta **Connexió per cable** que fa servir el nom `.local` del teu dispositiu.

També pots obrir l'adreça com a **codi QR** perquè la càmera d'un altre dispositiu hi arribi directament.

## Qui està connectat

La secció **Qui està connectat** llista els dispositius connectats a tu en temps real. Prem el botó de més accions al costat de qualsevol dispositiu per **Bloquejar aquest dispositiu** si no el reconeixes. Els dispositius bloquejats es gestionen a [Accés i privadesa](/docs/guide/everdisk/everdisk-guide-access).

## El nom i l'avatar del teu dispositiu

Cada dispositiu té un nom amable (com ara "Speedy-Hare") i un avatar de color. Aquest és el nom que un televisor, un ordinador o una altra app mostra per al teu dispositiu a la xarxa, de manera que és fàcil de reconèixer. Pots regenerar el nom i l'avatar gratuïtament, o definir un nom, una icona o un avatar amb foto personalitzats amb Premium. Consulta [Configuració](/docs/guide/everdisk/everdisk-guide-settings).

## Compartir per Wi-Fi o per cable USB

La compartició pot funcionar en dues situacions:

- **Per Wi-Fi**: el teu dispositiu i els altres dispositius són a la mateixa xarxa Wi-Fi.
- **Per cable USB**: el teu dispositiu està connectat a un **Mac** amb un cable, encara que no hi hagi gens de Wi-Fi. Això és més ràpid que el Wi-Fi i continua funcionant en un avió, en un hotel o en una xarxa bloquejada.

Si no hi ha ni Wi-Fi ni cable disponible, el botó **Iniciar** queda desactivat i apareix un avís de **Sense connexió Wi-Fi**. Si la connexió es talla mentre comparteixes, Everdisk atura la compartició automàticament i t'ho fa saber. Prem el botó d'informació de qualsevol d'aquests avisos per veure'n l'explicació completa.

## Mantén l'app oberta

Com que el teu iPhone o iPad fa de servidor, **la compartició només funciona mentre Everdisk està obert a la pantalla**. Si tanques l'app o bloqueges el dispositiu durant molta estona, el sistema pot pausar l'app i la compartició s'atura.

Per a transferències grans:

- Mantén Everdisk obert i en primer pla.
- Connecta el dispositiu al corrent.
- Posa el **Bloqueig automàtic** a **Mai** a l'app Configuració d'iOS mentre transfereixes.

Pots activar **Avisar abans de desconnectar** (a Configuració → Compartir) perquè Everdisk et recordi que has de tornar a obrir l'app abans que el sistema la suspengui. Prem el botó d'informació al bàner **Mantén l'app oberta** per veure'n més detalls.

## Passes següents

- [Connecta els teus dispositius](/docs/guide/everdisk/everdisk-guide-connect): connecta un televisor, un ordinador, un navegador, un telèfon o un cable USB.
- [Accés i privadesa](/docs/guide/everdisk/everdisk-guide-access): afegeix una contrasenya i controla l'edició.
- [Configuració](/docs/guide/everdisk/everdisk-guide-settings): activa o desactiva servidors i ajusta la qualitat.
