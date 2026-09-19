---
title: "Accés i privadesa"
date: 2026-08-20
description: "Mantén segura la teva compartició d'Everdisk: protegeix l'accés amb un inici de sessió i una contrasenya, xifra la connexió SMB amb SMB3 (AES), controla si els dispositius connectats poden pujar, canviar el nom i eliminar amb l'Edició d'arxius, bloqueja dispositius desconeguts, tria entre paperera i eliminació permanent i entén per què tot es queda a la teva xarxa local."
keywords: ["protecció amb contrasenya Everdisk", "xifratge SMB", "xifratge SMB3 AES", "commutador edició d'arxius", "bloquejar dispositiu", "dispositius bloquejats", "eliminar arxius permanentment", "només xarxa local", "compartició d'arxius privada", "DLNA sense contrasenya", "seguretat de xarxa"]
tags: ["everdisk", "guia", "acces", "privadesa", "seguretat"]
readingTime: 8
---


Everdisk manté els teus arxius a la teva pròpia xarxa i et dona controls senzills sobre qui hi pot arribar i què hi pot fer. Aquests controls els trobes a **Configuració → Compartir → Accés**, més uns quants ajustos relacionats al Gestor d'arxius.

## Protegeix l'accés amb un inici de sessió i una contrasenya

Per defecte, qualsevol persona de la mateixa xarxa que tingui la teva adreça pot obrir els teus arxius compartits. Per exigir un inici de sessió:

1. Ves a **Configuració → Compartir → Accés**.
2. Introdueix un **Inici de sessió** i una **Contrasenya**.
3. Ara les connexions del **Navegador (HTTP)**, l'**Ordinador (WebDAV)**, l'**Ordinador (avançat) (SMB)** i les **Altres apps i dispositius (FTP)** demanen totes aquestes dades abans de mostrar els teus arxius.

Deixa tots dos camps buits per a l'accés obert. La teva contrasenya es desa de manera segura al Keychain del dispositiu.

> **El DLNA sempre és obert.** La connexió TV i Centre multimèdia (DLNA) no es pot protegir amb contrasenya, així que un cop està activada, qualsevol dispositiu de la mateixa Wi-Fi pot explorar el teu contingut multimèdia compartit. Desactiva-la si només vols connexions protegides, i comparteix només en xarxes en les quals confiïs.

## Xifra la connexió SMB (SMB3 / AES)

Un inici de sessió i una contrasenya controlen **qui** es pot connectar, però les dades en si encara viatgen sense xifrar a la majoria de connexions. **SMB és l'única connexió que Everdisk pot xifrar**, cosa que codifica cada transferència perquè ningú més de la mateixa xarxa no la pugui llegir.

Per activar-ho:

1. Defineix un **Inici de sessió** i una **Contrasenya** com més amunt - les connexions xifrades no poden ser anònimes.
2. Ves a **Configuració → Compartir** i activa **Requereix xifratge SMB**.
3. **Atura i Inicia** la compartició de nou perquè el canvi tingui efecte.

Cada transferència SMB queda llavors protegida amb **xifratge SMB3 (AES)**. El dispositiu que es connecta ha de ser compatible amb SMB3 - el Finder d'un Mac modern, o **Windows 10 i posteriors**. És una opció excel·lent en un Wi-Fi en què no confiïs del tot. El Xifratge SMB és una funció Premium.

## Permet o bloqueja l'edició (Edició d'arxius)

El commutador **Edició d'arxius** controla si els dispositius connectats només poden mirar els teus arxius, o també poden canviar-los.

- **Activat** (per defecte): els dispositius connectats poden **pujar, canviar el nom i eliminar** els teus arxius compartits, de manera que el teu dispositiu funciona com una unitat de xarxa bidireccional real.
- **Desactivat**: els teus arxius compartits són de **només lectura**. Els altres poden veure'ls i descarregar-los, però no poden afegir ni canviar res.

Activar-lo mostra un avís breu perquè permet que altres persones modifiquin els teus arxius. Duu una etiqueta **Important** mentre està activat.

## Bloqueja un dispositiu

Si veus un dispositiu que no reconeixes:

1. A la pantalla de Compartir, troba'l a **Qui està connectat**.
2. Prem el seu botó de més accions i tria **Bloquejar aquest dispositiu**.

Els dispositius bloquejats es llisten a **Configuració → Compartir → Accés → Dispositius bloquejats**, on pots **desbloquejar-ne** un o **Desbloquejar-los tots**. El bloqueig segueix el dispositiu encara que la seva adreça de xarxa canviï (per a les connexions del Navegador, l'Ordinador i el televisor).

## Paperera vs. eliminació permanent

Quan s'elimina un arxiu (per tu al gestor d'arxius, o per un dispositiu connectat) normalment va a una **paperera** recuperable perquè el puguis recuperar.

Si prefereixes que els arxius s'eliminin immediatament sense recuperació, activa **Eliminar arxius permanentment** a **Configuració → Gestor d'arxius → Eliminació d'arxius**. Això està desactivat per defecte. **Afecta el gestor d'arxius del dispositiu** i les **eliminacions fetes per la xarxa**; no canvia com gestionen l'eliminació la Fototeca ni la Biblioteca de música del sistema.

## Tot es queda en local

Everdisk comparteix només per la teva **xarxa local**: no es puja res a internet i no hi ha cap compte al núvol pel mig. Val la pena saber unes quantes coses:

- Everdisk necessita el permís de **Xarxa local** d'iOS perquè els dispositius propers el puguin trobar. Si aquest permís està desactivat, un avís explica com tornar-lo a activar a l'app Configuració d'iOS.
- Per obtenir la màxima privadesa, comparteix només mentre siguis en una xarxa Wi-Fi **domèstica o privada** en la qual confiïs, i vés amb compte amb les Wi-Fi públiques. Un inici de sessió i una contrasenya ajuden, però no substitueixen una xarxa de confiança.
- L'**opció més privada de totes és un cable USB a un Mac**: les dades van directament pel cable i mai no toquen el router ni internet. Consulta [Connecta els teus dispositius](/docs/guide/everdisk/everdisk-guide-connect).

## Passes següents

- [Compartir](/docs/guide/everdisk/everdisk-guide-sharing): tria què compartir i inicia la compartició.
- [Configuració](/docs/guide/everdisk/everdisk-guide-settings): tots els ajustos d'Accés i del Gestor d'arxius en un sol lloc.
