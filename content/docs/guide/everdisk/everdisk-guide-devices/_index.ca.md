---
title: "Connectar a servidors"
date: 2026-08-20
description: "Fes servir la pestanya Dispositius d'Everdisk per connectar-te a altres servidors de la teva xarxa. Afegeix i explora servidors DLNA, WebDAV, FTP, SFTP i SMB i unitats NAS, reprodueix àudio i vídeo, descarrega arxius i crea, puja, canvia el nom, mou o elimina als servidors que ho permetin."
keywords: ["pestanya Dispositius Everdisk", "connectar a NAS", "client DLNA iPhone", "client WebDAV iPhone", "client FTP iPhone", "client SFTP iPhone", "client SMB iPhone", "connectar a recurs compartit SMB", "explorar servidor de xarxa", "reproduir des de NAS", "descarregar des de servidor", "connectar núvol WebDAV"]
tags: ["everdisk", "guia", "dispositius", "connexions"]
readingTime: 9
---


Everdisk no és només una unitat sense fil: també és un client per als altres dispositius de la teva xarxa. La pestanya **Dispositius** et permet connectar-te a servidors **DLNA**, **WebDAV**, **FTP**, **SFTP** i **SMB**, inclosos Macs, PC amb Windows, màquines Linux, unitats NAS i servidors multimèdia, i després explorar, reproduir i descarregar els seus arxius.

## La pantalla de Dispositius

La pestanya Dispositius té dues parts:

- **Connexions**: els servidors que ja has desat.
- **Dispositius disponibles**: servidors que Everdisk troba automàticament a la teva xarxa local.

Per connectar-te a alguna cosa que Everdisk ja ha trobat, només has de prémer-la a **Dispositius disponibles**. Per afegir un servidor manualment, prem el botó **més (+)** o **Nova connexió**.

## Afegir una connexió nova

Prem **Nova connexió** i tria el tipus de servidor al qual vols arribar:

- **DLNA / UPnP**: la millor opció per a servidors multimèdia. Reprodueix vídeo, música i fotos des de biblioteques multimèdia, unitats d'emmagatzematge de xarxa i televisors i ordinadors amb DLNA. El DLNA és de només lectura: pots explorar, reproduir i descarregar, però no pots pujar ni canviar arxius.
- **WebDAV**: connecta't a servidors d'arxius, unitats d'emmagatzematge de xarxa i unitats al núvol compatibles amb WebDAV. Llegeix i escriu quan el servidor ho permet.
- **FTP**: habitual en routers, unitats d'emmagatzematge de xarxa i allotjament web. El port per defecte és el 21 (990 per a FTPS segur); pots definir un port personalitzat a l'adreça, per exemple `ftp://host:2121`. Deixa l'inici de sessió i la contrasenya buits per a l'accés anònim.
- **SFTP**: connecta't de manera segura per SSH. El port per defecte és el 22; fes servir un port personalitzat a l'adreça si cal, per exemple `sftp://host:2222`.
- **SMB**: connecta't a Macs, PC amb Windows, servidors Linux i emmagatzematge en xarxa (NAS) que comparteixen carpetes mitjançant **SMB / CIFS**. Introdueix una adreça com `smb://server-address/share-name/` (exemples: `smb://local-server-name/share-name/folder-path`, `smb://192.168.1.105/share-name/folder-path`, `smb://remote-server.com`). SMB afegeix dos camps opcionals: un nom de **Grup de treball** i una **Versió del protocol** que pots deixar en **Automàtica** o forçar a **SMB1** o **SMB2**. Si els arxius o carpetes amb caràcters especials no s'obren, prova de canviar la versió a **SMB1**.

> Everdisk només es connecta a aquests protocols de xarxa local i d'adreçament directe. No inicia sessió en comptes al núvol com Google Drive o Dropbox. Una unitat al núvol només és accessible si aquell servei ofereix una adreça **WebDAV** que puguis escriure.

## Introduir l'adreça i iniciar sessió

A l'editor de connexions, emplena:

- **Títol**: un nom amable per a la connexió.
- **URL / adreça**: l'adreça del servidor (es mostren exemples per a cada tipus).
- **Inici de sessió** i **Contrasenya**: deixa'ls buits tots dos si el servidor permet l'accés anònim.

Per a WebDAV pots permetre certificats no vàlids si el teu servidor en fa servir un d'autosignat. Si no es pot verificar la identitat d'un servidor segur, Everdisk et demana que ho confirmis abans de confiar-hi.

Els usuaris gratuïts poden desar fins a **10** connexions. Premium elimina el límit.

## Explorar, reproduir i descarregar

Un cop connectat, prem el servidor per obrir-lo:

- **Explora** les carpetes en llista o quadrícula, ordena-les i mira'n les miniatures. Els servidors DLNA també mostren els detalls i les caràtules de la música.
- **Reprodueix** àudio i vídeo. L'àudio va a la cua del minireproductor; el vídeo es reprodueix a pantalla completa. La cerca funciona mentre un arxiu es reprodueix en temps real.
- **Descarrega** arxius al teu dispositiu. Selecciona'n diversos alhora per a una descàrrega en lot. Les descàrregues apareixen a **Transferències d'arxius** i van a parar a la teva carpeta **Documents**.
- **Informació** de qualsevol element mostra el seu tipus, mida, data, ruta i detalls multimèdia.

## Canviar arxius en un servidor

Als servidors que permeten l'escriptura (**WebDAV, FTP, SFTP i SMB**) també pots gestionar arxius:

- **Nova carpeta**
- **Pujar arxius** des del teu dispositiu
- **Canviar el nom**, **Moure** i **Eliminar** (un element o diversos alhora)

Els servidors **DLNA** són de només lectura, així que aquestes accions no hi estan disponibles.

## Fes el seguiment de les teves transferències

Les descàrregues i pujades s'executen en segon pla i apareixen a **Transferències d'arxius**, que obres des de la part superior esquerra de la pestanya **Documents**. Allà pots veure el progrés i pausar, reprendre, reintentar, cancel·lar o esborrar tasques. També pots ajustar les transferències a [Configuració → Xarxa](/docs/guide/everdisk/everdisk-guide-settings) (només Wi-Fi o Wi-Fi i dades mòbils, quantes s'executen alhora i si continuen en segon pla).

## Passes següents

- [Arxius i documents](/docs/guide/everdisk/everdisk-guide-files): gestiona tot el que descarreguis.
- [Fotos, música i vídeo](/docs/guide/everdisk/everdisk-guide-media): reprodueix el que emetis.
- [Configuració](/docs/guide/everdisk/everdisk-guide-settings): límits de connexió i opcions de transferència.
