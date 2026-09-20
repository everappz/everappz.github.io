---
title: "Com configurar un servidor multimèdia DLNA/UPnP a l'iPhone i l'iPad per fer streaming"
description: "Converteix el teu iPhone o iPad en un servidor multimèdia DLNA/UPnP amb Everdisk i fes streaming de fotos, vídeos i música a un televisor intel·ligent, una consola de jocs, VLC o Kodi per Wi-Fi. Configuració completa i com connectar-te des de televisors Samsung, LG i Sony, Windows, Mac, Linux, Android i un altre iPhone."
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "servidor multimèdia", "streaming", "televisor intel·ligent", "iphone", "ipad", "wifi"]
keywords: ["servidor DLNA iPhone", "servidor UPnP iPad", "com configurar DLNA a l'iPhone", "streaming a televisor intel·ligent des de l'iPhone", "servidor multimèdia DLNA iOS", "streaming de vídeos al televisor sense cable", "reproduir fotos de l'iPhone al televisor", "DLNA televisor Samsung iPhone", "DLNA televisor LG iPhone", "DLNA Sony Bravia iPhone", "VLC DLNA iPhone", "servidor multimèdia Kodi DLNA", "servidor multimèdia UPnP AV iOS", "streaming de música al televisor des de l'iPhone", "app servidor multimèdia iPhone"]
readingTime: 9
---

{{< author-byline >}}

DLNA (també anomenat UPnP AV) és el treballador discret que hi ha darrere de la majoria de televisors intel·ligents. És un llenguatge compartit que permet que un televisor o un reproductor multimèdia trobi una biblioteca de mitjans a la mateixa Wi-Fi i hi reprodueixi, sense res a instal·lar al televisor. Si el teu iPhone o iPad pot fer de biblioteca, les teves fotos, vídeos i música apareixen soles a la gran pantalla.

Aquesta guia mostra com convertir el teu iPhone o iPad en un servidor multimèdia DLNA/UPnP amb [Everdisk](/products/everdisk), i com obrir aquesta biblioteca des d'un televisor intel·ligent, una consola de jocs, VLC, Kodi, un ordinador, un telèfon Android i, fins i tot, un segon iPhone. Tot funciona per la teva Wi-Fi local, així que no es puja res enlloc.

## Què necessites

- Un iPhone o iPad amb [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) instal·lat.
- Un televisor, reproductor o ordinador a la **mateixa xarxa Wi-Fi** que el teu dispositiu.
- Les fotos, vídeos o música que vols reproduir, ja al teu iPhone (a l'app Fotos, a l'app Música o a la carpeta Documents d'Everdisk).

## Configura el servidor DLNA a Everdisk

### Pas 1: Tria què vols compartir

Obre Everdisk i ves a la pestanya **Compartició**. Toca **Què compartir** i tria el teu contingut:

- Activa **Permet l'accés a tota la biblioteca de fotos** per compartir cada àlbum, o toca **Afegeix fotos** per triar-ne alguns.
- Activa **Permet l'accés a tota la biblioteca de música** per compartir les teves cançons, o toca **Afegeix cançons** per fer-ne una selecció.
- Afegeix qualsevol carpeta o arxiu amb **Afegeix una carpeta** i **Afegeix un fitxer**. La carpeta Documents de l'app es comparteix per defecte.

Cal que tinguis com a mínim un element seleccionat abans que la compartició pugui començar.

### Pas 2: Activa Televisor i centre multimèdia (DLNA)

Ves a **Configuració**, després a **Compartició** i després a **Connexions**. Assegura't que **Televisor i centre multimèdia** està activat. Ho està per defecte i porta l'etiqueta DLNA. Aquest és el servidor que busquen els televisors i reproductors.

### Pas 3: Comença a compartir

Torna a la pestanya **Compartició** i toca el botó gran **Iniciar**. El teu dispositiu ara és un servidor multimèdia a la teva Wi-Fi. Apareix als altres dispositius amb el seu nom amable, el que es mostra com a nom del teu dispositiu a l'app (una cosa com «Speedy-Hare» fins que el canviïs).

El streaming DLNA sempre està obert, així que no cal introduir cap contrasenya al televisor. Mantén Everdisk obert a la pantalla mentre mires, perquè iOS posa en pausa les apps que passen completament a segon pla.

## Reprodueix en un televisor intel·ligent

Aquest és el cas més habitual i normalment triga uns trenta segons.

1. Posa el televisor a la **mateixa Wi-Fi** que el teu iPhone.
2. Obre el reproductor multimèdia integrat del televisor. El nom depèn de la marca: **Media Player**, **Gallery**, **SmartShare** (LG), **AllShare** o **SmartThings** (Samsung), **Content Share** o **SimplyShare**.
3. Busca la llista de servidors multimèdia o fonts. El teu dispositiu hi apareix pel seu nom.
4. Selecciona'l, explora les teves fotos, vídeos o música, i prem reproduir.

Les miniatures de previsualització apareixen automàticament, així que pots trobar l'àlbum de vacances o la pel·lícula que vols sense endevinar-ho.

### Quins televisors funcionen

La majoria de televisors de **Samsung, LG, Sony BRAVIA, Panasonic (firmware VIERA), Philips i Hisense** porten DLNA integrat i funcionen de seguida. **Les consoles PlayStation i Xbox i la majoria de receptors AV** també.

Algunes plataformes no l'inclouen: **els televisors Roku, Amazon Fire TV, Vizio SmartCast i el Google TV senzill** sense una app multimèdia del fabricant. Si el teu televisor és un d'aquests i no pot trobar el teu dispositiu, normalment aquesta n'és la raó. En aquests televisors, instal·la una app reproductora de DLNA com ara VLC o Kodi, o arriba als teus arxius a través d'un navegador web amb la [guia de configuració de WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/).

Algunes marques van mantenir el DLNA en funcionament fins i tot després de treure el logotip oficial de DLNA, així que si sembla que falta, busca un dels noms de reproductor multimèdia d'abans.

## Reprodueix a VLC o Kodi a Windows, Mac i Linux

VLC i Kodi són gratuïts, funcionen en tots els sistemes d'escriptori i parlen bé el DLNA. Són la manera fiable d'obrir la teva biblioteca d'Everdisk en un ordinador.

**VLC (Windows, Mac, Linux):**

1. Obre VLC.
2. Mostra la llista de reproducció (a Windows i Linux prem **Ctrl+L**, a Mac obre la **Playlist** des del menú Visualització).
3. A la barra lateral, obre **Universal Plug'n'Play** a Xarxa local.
4. El teu dispositiu apareix a la llista. Fes-hi clic i tria un arxiu.

**Kodi (Windows, Mac, Linux):**

1. Ves a **Videos**, **Music** o **Pictures**, després a **Files** i després a **Add source** (o **Browse**).
2. Tria **UPnP devices**.
3. Selecciona el teu dispositiu i explora la teva biblioteca.

A Windows també pots obrir **Windows Media Player**, desplegar **Other Libraries** a la barra lateral, i el teu dispositiu hi apareixerà.

## Reprodueix a Android

Els telèfons i tauletes Android no tenen un explorador de DLNA del sistema, així que fes servir una app:

- **VLC per a Android**: obre el menú lateral, toca **Local Network** i el teu dispositiu apareix sota els servidors UPnP.
- **BubbleUPnP** o una app UPnP similar: el teu dispositiu apareix a la llista de servidors, i aquestes apps també poden enviar la reproducció a un televisor.

## Reprodueix en un altre iPhone o iPad

Dos dispositius, una biblioteca. Suposem que les fotos són al teu iPhone i les vols mirar al teu iPad.

- La ruta més senzilla és la mateixa pestanya **Dispositius** d'Everdisk al segon dispositiu. Funciona com a client DLNA i també com a servidor. Obre Everdisk a l'iPad, ves a **Dispositius** i el teu iPhone apareix sota **Dispositius disponibles**. Toca'l per explorar i reproduir.
- Qualsevol app reproductora de DLNA per a iOS també funciona, com ara VLC o un explorador UPnP. Obre la seva vista de xarxa local i tria el teu iPhone.

## Reprodueix en una consola de jocs

- **PlayStation 5 i 4**: obre l'app **Media** (Media Gallery), i el teu dispositiu apareix com un servidor multimèdia que pots explorar.
- **Xbox**: fes servir una app reproductora de mitjans compatible amb DLNA, i després tria el teu dispositiu de la llista de servidors.

## Si el teu dispositiu no apareix a la llista

Alguns reproductors et permeten afegir un servidor multimèdia per adreça en lloc d'esperar que sigui descobert. A la pantalla **Compartició** d'Everdisk, la targeta DLNA mostra una adreça de descripció del dispositiu que acaba en `/device-desc.xml`. Introdueix aquesta adreça al camp per afegir un servidor del reproductor.

Si encara no apareix, comprova tres coses: que tots dos dispositius són a la mateixa Wi-Fi (no una xarxa de convidats que bloqueja el trànsit entre dispositius), que Everdisk està obert i la compartició està iniciada, i que **Televisor i centre multimèdia** està activat a Configuració.

## Si un vídeo no es reprodueix

DLNA lliura l'arxiu al televisor tal com és, i el televisor l'ha de poder descodificar. Si un clip es nega a reproduir-se, el seu format probablement no és compatible amb aquell televisor. Dues solucions:

- Obre **Configuració**, després **Compartició** i després **Vídeos**, i abaixa la **Qualitat**. Everdisk aleshores converteix el vídeo a un format més compatible mentre fa streaming. (La conversió és una funció Premium.)
- O obre el mateix arxiu en un navegador web amb l'enllaç del navegador d'Everdisk, que és més tolerant amb els formats.

## Maneres reals com la gent fa servir això

- **Nit de pel·lícula en família.** Els vídeos gravats amb el teu telèfon es reprodueixen al televisor del menjador sense cap cable ni Apple TV.
- **Fotos de vacances a la gran pantalla.** Obre la teva biblioteca de Fotos al televisor i llisca pel viatge amb tothom a la sala.
- **Música de fons en una festa.** Apunta un altaveu DLNA o un receptor AV a la teva biblioteca de Música i deixa que soni.
- **Mirar en un televisor d'hotel** que té un reproductor multimèdia, un cop tots dos dispositius siguin a la Wi-Fi de l'habitació.

## Uns quants consells

- Mantén Everdisk obert mentre fas streaming. Si bloqueges el telèfon durant molta estona, iOS pot posar en pausa l'app i la reproducció s'atura.
- Connecta el telèfon a l'electricitat per a sessions llargues de pel·lícula.
- Per al streaming més ràpid, mantén el **Format** i la **Qualitat** en **Original** a Configuració, i abaixa'ls només si un televisor concret té problemes amb un arxiu.
- DLNA només és streaming. Ningú del costat del televisor pot canviar ni eliminar els teus arxius. Per a la transferència d'arxius en totes dues direccions, fes servir el servidor [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/), [WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) o [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/).

## Preguntes freqüents

{{% details title="Quina diferència hi ha entre DLNA i UPnP?" closed="true" %}}
Estan estretament relacionats. UPnP és l'estàndard de xarxa subjacent, i DLNA és el perfil multimèdia construït al damunt que els televisors i reproductors fan servir per compartir i reproduir fotos, vídeos i música. En l'ús diari les paraules són intercanviables. Quan actives Televisor i centre multimèdia a Everdisk, el teu dispositiu es converteix en un servidor multimèdia DLNA/UPnP que qualsevol client DLNA pot explorar.
{{% /details %}}

{{% details title="Cal instal·lar res al meu televisor?" closed="true" %}}
No. Si el teu televisor admet DLNA, ja té un reproductor multimèdia que pot trobar el teu dispositiu a la Wi-Fi. Només instal·les Everdisk a l'iPhone o iPad que conté el contingut. Si el teu televisor no admet DLNA, instal·la un reproductor com VLC o Kodi en un dispositiu que hi estigui connectat.
{{% /details %}}

{{% details title="Per què el meu iPhone no apareix al televisor?" closed="true" %}}
Comprova que tots dos dispositius són a la mateixa xarxa Wi-Fi. Les xarxes de convidats i algunes xarxes d'oficina o d'hotel impedeixen que els dispositius es vegin entre ells, cosa que atura el DLNA. Després confirma que Everdisk està obert amb la compartició iniciada, i que Televisor i centre multimèdia està activat a Configuració, Compartició, Connexions. Si el televisor encara no el troba, afegeix el servidor a mà amb l'adreça de descripció del dispositiu que acaba en /device-desc.xml.
{{% /details %}}

{{% details title="El streaming DLNA necessita contrasenya?" closed="true" %}}
No. DLNA sempre està obert a qualsevol persona de la mateixa Wi-Fi mentre està activat, i per això no hi ha inici de sessió al costat del televisor. Això va bé en una xarxa domèstica en què confies. En una xarxa en què no confies, desactiva Televisor i centre multimèdia quan acabis, o fes servir el servidor SMB amb xifratge.
{{% /details %}}

{{% details title="Puc fer streaming a un Chromecast o Roku?" closed="true" %}}
Chromecast i Roku no fan de reproductors DLNA de sèrie, així que no trobaran el teu dispositiu directament. La solució és instal·lar una app DLNA que pugui fer casting, com ara VLC o BubbleUPnP en un telèfon, i enviar la reproducció al Chromecast o al Roku des d'allà. A la majoria dels altres televisors intel·ligents, el DLNA funciona sense res d'això.
{{% /details %}}

{{% details title="Un vídeo es reprodueix sense so o no s'obre. Què puc fer?" closed="true" %}}
Aquest és un format que el televisor no pot descodificar. Obre Configuració, Compartició, Vídeos a Everdisk i abaixa la Qualitat perquè l'app converteixi el vídeo a un format més compatible mentre fa streaming. També pots obrir el mateix arxiu a través de l'enllaç del navegador, que gestiona més formats.
{{% /details %}}

{{% details title="Puc fer streaming de música, no només de vídeo?" closed="true" %}}
Sí. Activa Permet l'accés a tota la biblioteca de música, o afegeix cançons concretes, i després comença a compartir. Les teves cançons apareixen a qualsevol altaveu DLNA, receptor AV o televisor, amb caràtula i detalls de la cançó. La música sempre es comparteix amb la seva qualitat original.
{{% /details %}}

{{% details title="L'app ha de quedar oberta mentre miro?" closed="true" %}}
Sí. El teu iPhone fa de servidor, i iOS posa en pausa les apps que passen completament a segon pla durant molta estona. Mantén Everdisk a la pantalla mentre fas streaming, i connecta'l a l'electricitat per a sessions llargues.
{{% /details %}}

{{% details title="Com faig streaming d'un iPhone a un altre iPad?" closed="true" %}}
Comença a compartir a l'iPhone, després obre Everdisk a l'iPad i ves a la pestanya Dispositius. L'iPhone apareix sota Dispositius disponibles com a servidor multimèdia. Toca'l per explorar i reproduir. Everdisk funciona com a client DLNA i com a servidor, així que no necessites cap altra app.
{{% /details %}}

{{% details title="Everdisk és gratis?" closed="true" %}}
Sí, Everdisk es baixa gratis i el servidor multimèdia DLNA hi està inclòs. Una compra opcional única Premium de per vida afegeix extres com la conversió de fotos i vídeos per a televisors antics, ports personalitzats i més. Pots configurar i fer servir el streaming DLNA sense pagar.
{{% /details %}}

Vols provar-ho? [Baixa Everdisk de l'App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) i fes streaming del teu primer àlbum al televisor en un parell de minuts. Preguntes o comentaris? Escriu-nos a **support@everappz.com**.
