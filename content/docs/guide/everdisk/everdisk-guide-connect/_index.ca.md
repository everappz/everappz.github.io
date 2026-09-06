---
title: "Connecta els teus dispositius"
date: 2026-08-20
description: "Instruccions pas a pas per connectar-te a la teva unitat sense fil Everdisk: mira contingut en un televisor intel·ligent per DLNA, obre els teus arxius en qualsevol navegador, munta el teu dispositiu com a unitat de xarxa al Finder, a Windows o a Linux per WebDAV, connecta apps d'arxius per FTP i transfereix per cable USB a un Mac sense Wi-Fi."
keywords: ["connectar a Everdisk", "reproduir a la TV DLNA", "obrir arxius al navegador", "muntar unitat de xarxa Finder", "WebDAV Windows Linux", "app d'arxius FTP", "transferir per cable USB Mac", "connectar iPhone a l'ordinador", "unitat de xarxa iPhone"]
tags: ["everdisk", "guia", "connectar"]
readingTime: 11
---


Un cop prems **Iniciar** a la pantalla de [Compartir](/docs/guide/everdisk/everdisk-guide-sharing), els altres dispositius es poden connectar als teus arxius de quatre maneres diferents. Tria el mètode que s'adapti al dispositiu que vols fer servir. En tots els casos, l'**adreça** exacta que necessites es mostra a la secció **Com connectar** de la pantalla de Compartir.

> Tots dos dispositius han de ser a la **mateixa xarxa Wi-Fi**, o bé, per a un Mac, connectats amb un **cable USB** (consulta l'última secció).

## Mira contingut en un televisor (DLNA)

Fes-ho servir per mostrar fotos, vídeos i música en un televisor o reproductor intel·ligent.

1. A **Configuració → Compartir → Connexions**, assegura't que **TV i Centre multimèdia** estigui activat (ho està per defecte).
2. A la pantalla de Compartir, prem **Iniciar**.
3. Al teu televisor, obre el reproductor multimèdia integrat o l'app de servidor multimèdia (pot dir-se Media Player, SmartShare, AllShare o similar).
4. El teu dispositiu apareix a la llista de servidors multimèdia pel seu nom (per exemple "Speedy-Hare"). Selecciona'l.
5. Explora les fotos, vídeos i música compartits i comença a reproduir-los. Les miniatures de previsualització apareixen automàticament.

Notes:

- El DLNA no es pot protegir amb contrasenya, així que aquesta connexió és oberta a qualsevol persona de la mateixa Wi-Fi mentre estigui activada.
- Si un vídeo no es reprodueix en un televisor antic, baixa la qualitat de vídeo a **Configuració → Compartir → Vídeos** perquè Everdisk el converteixi a un format més compatible.

## Obre en un navegador web (HTTP)

Fes-ho servir per passar arxius a qualsevol persona amb un navegador web, sense cap app per instal·lar.

1. A **Configuració → Compartir → Connexions**, assegura't que **Navegador** estigui activat.
2. Prem **Iniciar**.
3. A la pantalla de Compartir, copia l'adreça del **Navegador** (o mostra'n el codi QR).
4. A l'altre telèfon, tauleta o ordinador, obre qualsevol navegador (Safari, Chrome, Edge, Firefox) i escriu aquesta adreça.
5. La pàgina s'obre amb els teus arxius compartits.

Al navegador l'altra persona pot:

- Canviar entre la vista de **llista** i la de **quadrícula** i ordenar per nom, data o mida.
- Veure **miniatures** reals de fotos, vídeos, PDF i caràtules de música.
- Obrir una foto en una **galeria** a pantalla completa amb lliscament, pessic per fer zoom i presentació de diapositives.
- Reproduir música en un **reproductor** integrat amb cua, reproducció aleatòria i repetició.
- **Descarregar** qualsevol arxiu, o descarregar una carpeta sencera (o diversos elements seleccionats) com un únic **Archive.zip**.
- **Pujar** arxius de tornada al teu dispositiu, però només si has activat l'**Edició d'arxius** (consulta [Accés i privadesa](/docs/guide/everdisk/everdisk-guide-access)).

## Fes-lo servir com a unitat de xarxa (WebDAV)

Fes-ho servir perquè el teu dispositiu aparegui com un disc normal en un Mac, un PC amb Windows o una màquina Linux, així pots arrossegar arxius en totes dues direccions.

**En un Mac (Finder)**

1. A **Configuració → Compartir → Connexions**, assegura't que **Ordinador** estigui activat.
2. Prem **Iniciar** i anota l'adreça d'**Ordinador (WebDAV)**.
3. Al Finder, tria **Anar → Connectar al servidor** (o prem **⌘K**).
4. Escriu l'adreça WebDAV exactament com es mostra i fes clic a **Connectar**.
5. Introdueix l'inici de sessió i la contrasenya si n'has definit una; si no, connecta't com a convidat.
6. El teu dispositiu s'obre com qualsevol altra unitat de xarxa. Arrossega-hi arxius cap a dins o cap a fora.

**A Windows**

1. Obre l'**Explorador d'arxius**, fes clic dret a **Aquest PC** i tria **Afegir una ubicació de xarxa** (o assigna una unitat de xarxa).
2. Introdueix l'adreça WebDAV que es mostra a Everdisk.
3. Introdueix l'inici de sessió i la contrasenya si n'has definit una.

**A Linux**

1. Obre el teu gestor d'arxius i tria **Connectar al servidor** (o fes servir `davs://` / `dav://`).
2. Introdueix l'adreça WebDAV que es mostra a Everdisk.

Que la connexió sigui de només lectura o bidireccional depèn de l'opció **Edició d'arxius**. Amb aquesta activada, pots copiar arxius al teu dispositiu i canviar-ne el nom o eliminar-los; amb aquesta desactivada, la unitat és de només lectura.

## Connecta una app d'arxius (FTP)

Fes-ho servir per a apps de gestió i transferència d'arxius que utilitzen FTP (per exemple FileZilla o Cyberduck en un ordinador).

1. A **Configuració → Compartir → Connexions**, assegura't que **Altres apps i dispositius** estigui activat.
2. Prem **Iniciar** i anota l'adreça **FTP**.
3. A la teva app FTP, afegeix una connexió nova amb aquesta adreça.
4. Introdueix l'inici de sessió i la contrasenya si n'has definit una, o deixa'ls buits per a l'accés anònim.

## Transfereix per cable USB (només Mac, sense Wi-Fi)

Fes-ho servir quan no hi ha Wi-Fi, o quan vols la transferència més ràpida i més privada. Només funciona amb un **Mac**.

1. Connecta el teu iPhone o iPad al Mac amb el cable de càrrega habitual.
2. Si el dispositiu t'ho demana, prem **Confia en aquest ordinador**.
3. A Everdisk, prem **Iniciar**. Apareix un avís de **Connexió ràpida disponible** i la pantalla de Compartir mostra una adreça addicional amb una etiqueta **Connexió per cable** que acaba en `.local`.
4. Al Mac, obre el Finder → **Anar → Connectar al servidor** (**⌘K**) i introdueix aquesta adreça `.local` (funciona tant per a la connexió del Navegador com per a la de l'Ordinador).
5. El teu dispositiu s'obre per cable, més ràpid que per Wi-Fi, i les dades mai no toquen el router ni internet.

Notes:

- Fes servir el **nom `.local`**, no una adreça IP (les adreces IP només funcionen per Wi-Fi), i mai `localhost`.
- El camí per cable és **només per a Mac**. Els PC amb Windows i els dispositius Android han de fer servir Wi-Fi.
- També pots arrossegar arxius a la carpeta d'Everdisk fent servir el Finder en un Mac, o l'app Apple Devices (o iTunes) a Windows, mitjançant la compartició d'arxius estàndard d'iOS.

## Passes següents

- [Accés i privadesa](/docs/guide/everdisk/everdisk-guide-access): afegeix una contrasenya, permet pujades, bloqueja un dispositiu.
- [Fotos, música i vídeo](/docs/guide/everdisk/everdisk-guide-media): comparteix tota la teva biblioteca i ajusta la qualitat.
- [Connectar a servidors](/docs/guide/everdisk/everdisk-guide-devices): arriba a altres dispositius des d'Everdisk.
