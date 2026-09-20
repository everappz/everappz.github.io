---
title: "Com configurar un servidor SMB a l'iPhone i l'iPad per compartir arxius"
description: "Converteix el teu iPhone o iPad en un servidor d'arxius SMB amb Everdisk i obre'l com una unitat de xarxa des d'un Mac, un altre iPhone, Linux o Android per Wi-Fi. Configuració completa, l'adreça i el port smb, xifratge SMB3 opcional i connexió pas a pas per a cada dispositiu."
date: 2026-09-19
tags: ["everdisk", "smb", "compartir arxius", "unitat de xarxa", "iphone", "ipad", "mac", "finder", "xifratge", "wifi"]
keywords: ["servidor SMB iPhone", "servidor SMB iPad", "com configurar SMB a l'iPhone", "compartició SMB iPhone", "connectar iPhone SMB Mac Finder", "smb iphone a iphone", "app Arxius iOS connectar a servidor SMB", "compartir arxius iPhone SMB", "unitat de xarxa iphone Finder", "xifratge SMB3 iOS", "compartició smb iPhone Android", "connectar a SMB des de Linux", "iphone com a unitat de xarxa", "compartir arxius entre iphones wifi", "assignar iphone com a unitat de xarxa"]
readingTime: 10
---

{{< author-byline >}}

SMB és la compartició d'arxius integrada a macOS, Windows i Linux, i a gairebé totes les unitats de xarxa (NAS). Quan et connectes a una carpeta compartida d'un altre ordinador i s'obre com un disc normal al Finder o a l'Explorador d'arxius, això és SMB fent la feina. Amb [Everdisk](/products/everdisk) pots posar una compartició SMB al teu iPhone o iPad, de manera que el mateix telèfon apareix com una unitat de xarxa que altres dispositius exploren, de la qual copien i a la qual copien.

Aquesta és l'opció que has de triar quan vols que el teu iPhone es comporti com una unitat de debò, no com una pàgina web. És ràpid, arrossega i deixa anar en totes dues direccions, i és l'únic tipus de connexió d'Everdisk que pot xifrar cada transferència. Aquesta guia cobreix la configuració i com connectar-te des d'un Mac, un altre iPhone o iPad, Linux, Android i Windows.

## Què necessites

- Un iPhone o iPad amb [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) instal·lat.
- Un altre dispositiu a la **mateixa xarxa Wi-Fi**.
- Els arxius que vols compartir, a la carpeta Documents d'Everdisk o a carpetes que afegeixis.

## Configura el servidor SMB a Everdisk

### Pas 1: Tria què compartir i qui pot escriure

Obre Everdisk, ves a la pestanya **Compartició** i toca **Què compartir**. La carpeta Documents es comparteix per defecte. Afegeix-ne més amb **Afegeix una carpeta** i **Afegeix un fitxer**, i activa la teva biblioteca de Fotos o Música si també les vols disponibles.

Decideix si els altres dispositius només poden llegir els teus arxius, o també canviar-los. Obre **Configuració**, després **Compartició** i després **Accés**, i configura **Edició de fitxers**. Amb això activat, els dispositius connectats poden copiar arxius al teu telèfon i canviar-los de nom o eliminar-los. Amb això desactivat, la compartició és de només lectura.

Si vols un inici de sessió, defineix un **Inici de sessió** i una **Contrasenya** a la mateixa pantalla d'Accés. Deixa'ls tots dos buits per permetre l'accés de convidats.

### Pas 2: Activa el servidor SMB

Ves a **Configuració**, després a **Compartició** i després a **Connexions**, i activa **Ordinador (avançat)**. Aquest és el servidor SMB (porta l'etiqueta SMB).

### Pas 3: Comença a compartir i anota l'adreça

Torna a la pestanya **Compartició** i toca **Iniciar**. La secció **Com connectar-se** ara mostra l'adreça SMB. Té aquest aspecte:

```
smb://192.168.1.20:4455/Share
```

Tres coses que has de saber sobre aquesta adreça:

- El número després dels dos punts és el **port**. Everdisk fa servir **4455** per defecte.
- La compartició s'anomena **Share**.
- La primera part és l'adreça del teu iPhone a la Wi-Fi, així que serà diferent a la teva xarxa.

Mantén Everdisk obert mentre hi hagi dispositius connectats, perquè iOS posa en pausa les apps que estan massa estona en segon pla.

## Connecta't des d'un Mac

Aquest és el cas més fàcil, perquè macOS parla SMB de manera nativa.

La manera més ràpida: obre el **Finder** i mira a la barra lateral sota **Ubicacions** o **Xarxa**. Everdisk s'anuncia a la Wi-Fi, així que el teu iPhone sovint hi apareix sol. Fes-hi clic, després fes clic a **Connectar com a** i tria **Convidat**, o introdueix el teu inici de sessió.

Per connectar-te a mà:

1. Al Finder, tria **Anar**, després **Connectar al servidor** (o prem **Command i K**).
2. Escriu l'adreça SMB que es mostra a Everdisk, per exemple `smb://192.168.1.20:4455/Share`.
3. Fes clic a **Connectar**, després tria **Convidat** o introdueix el teu **Inici de sessió** i **Contrasenya**.

El teu iPhone s'obre en una finestra del Finder. Copia arxius cap endins o cap enfora arrossegant, exactament com qualsevol altra unitat (si Edició de fitxers està activada).

## Connecta't des d'un altre iPhone o iPad

iOS i iPadOS poden obrir comparticions SMB a l'app **Arxius** integrada, cosa que fa que les transferències de telèfon a telèfon siguin netes i ràpides.

Al segon dispositiu:

1. Obre l'app **Arxius**.
2. Toca el botó **més** (els tres punts, a dalt a la dreta a l'iPhone) i tria **Connectar al servidor**.
3. Introdueix l'adreça SMB d'Everdisk, per exemple `smb://192.168.1.20:4455/Share`.
4. Tria **Convidat**, o **Usuari registrat** i introdueix el teu inici de sessió.
5. La compartició apareix sota Ubicacions a Arxius. Explora i copia en qualsevol direcció.

També pots fer servir la mateixa pestanya **Dispositius** d'Everdisk al segon dispositiu, que inclou un client SMB. Obre Everdisk, ves a **Dispositius**, toca **Connexió nova**, tria **SMB** i introdueix l'adreça.

## Connecta't des de Linux

1. Obre el teu gestor d'arxius (Files/Nautilus a GNOME, Dolphin a KDE).
2. Tria **Altres ubicacions** o **Connectar al servidor**.
3. Introdueix l'adreça, per exemple `smb://192.168.1.20:4455/Share`.
4. Connecta't com a convidat, o introdueix el teu inici de sessió.

Des d'un terminal també pots executar `smbclient //192.168.1.20/Share -p 4455` i introduir el teu inici de sessió quan et demani.

## Connecta't des d'Android

Android no té un explorador SMB del sistema, així que fes servir un gestor d'arxius compatible amb SMB:

1. Instal·la una app com ara **CX File Explorer**, **Solid Explorer** o **X-plore File Manager**.
2. Afegeix una connexió **SMB** o **LAN** nova.
3. Introdueix l'amfitrió (l'adreça Wi-Fi del teu iPhone), configura el **port a 4455** i el nom de la compartició **Share**.
4. Connecta't com a convidat o amb el teu inici de sessió, i després explora i copia.

## Connecta't des de Windows

Windows pot llegir comparticions SMB, amb un detall que val la pena saber d'entrada. L'Explorador d'arxius integrat només parla SMB al port estàndard i no et deixa escriure un port personalitzat a la ruta, i Everdisk fa servir el port 4455. Així que la ruta senzilla d'**Assignar una unitat de xarxa** sovint no hi arribarà.

Tens dues bones opcions a Windows:

- Fes servir un gestor d'arxius o un client SMB que et permeti definir un port personalitzat, i apunta'l a l'adreça del teu iPhone amb el port **4455** i el nom de la compartició **Share**.
- O connecta't des de Windows amb un dels altres servidors d'Everdisk. La [configuració de WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) i la [configuració d'FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) funcionen bé des de l'Explorador d'arxius de Windows, i l'enllaç del navegador funciona a qualsevol navegador.

Si vols provar Assignar una unitat de xarxa: obre l'**Explorador d'arxius**, fes clic dret a **Aquest ordinador**, tria **Assignar una unitat de xarxa**, i introdueix l'amfitrió i el nom de la compartició que es mostren a Everdisk. Si no es pot connectar, és la limitació del port d'abans, així que canvia a WebDAV o FTP.

## Activa el xifratge per a una Wi-Fi de poca confiança

SMB és l'única connexió d'Everdisk que pot xifrar cada transferència, cosa que importa en una Wi-Fi que no controles del tot, com la d'una cafeteria o una xarxa d'oficina.

1. A **Configuració**, **Compartició**, **Accés**, defineix un **Inici de sessió** i una **Contrasenya**. Les connexions xifrades no poden ser anònimes, així que aquest pas és obligatori.
2. A **Configuració**, **Compartició**, activa **Requereix xifratge SMB**.
3. Atura i torna a iniciar la compartició perquè el canvi tingui efecte.

Cada transferència SMB queda aleshores protegida amb **xifratge SMB3 (AES)**. El dispositiu que es connecta ha d'admetre SMB3, cosa que el Finder d'un Mac modern i Windows 10 o posterior fan tots dos. El xifratge SMB forma part de la compra única Premium.

## Només lectura o lectura i escriptura

L'interruptor **Edició de fitxers** a Configuració, Compartició, Accés controla això per a cada servidor, inclòs SMB. Activa'l i els dispositius connectats poden pujar, canviar de nom i eliminar. Desactiva'l i només poden explorar i copiar arxius del teu telèfon. Tria només lectura quan lliures arxius a algú a qui no vols que canviï res.

## Maneres reals com la gent fa servir això

- **Moure una carpeta gran al teu iPhone des d'un Mac** arrossegant-la a la finestra del Finder, més ràpid que una pujada web.
- **Treure un dia de fotos i vídeos del teu telèfon** a un portàtil sense iTunes ni cap cable.
- **Enviar arxius entre dos iPhones** a través de l'app Arxius, sense cap tercera app a cap dels dos costats.
- **Treballar amb un arxiu al seu lloc**, obrint un document directament des del telèfon en una app del teu Mac i desant-lo de nou.

## Uns quants consells

- Mantén Everdisk obert mentre hi hagi un dispositiu connectat. Bloquejar el telèfon durant molta estona pot posar en pausa l'app i tallar la connexió.
- Si un Mac no pot veure el telèfon a la barra lateral del Finder, connecta't a mà amb Connectar al servidor i l'adreça smb completa.
- Per a la millor velocitat en transferències grans, mantén la qualitat de fotos i vídeos en Original a Configuració.
- En una xarxa de poca confiança, activa Requereix xifratge SMB i desactiva els altres servidors mentre treballes.

## Preguntes freqüents

{{% details title="Quina és l'adreça i el port SMB del meu iPhone?" closed="true" %}}
Després que comencis a compartir, Everdisk mostra l'adreça a la pantalla Compartició. Té l'aspecte smb://192.168.1.20:4455/Share. El 4455 és el port que Everdisk fa servir per a SMB, i Share és el nom de la carpeta compartida. La primera part és l'adreça del teu iPhone a la Wi-Fi, així que la teva serà diferent.
{{% /details %}}

{{% details title="Puc connectar-me a la compartició SMB del meu iPhone des de Windows?" closed="true" %}}
L'Explorador d'arxius de Windows només es connecta a SMB al port estàndard i no accepta un port personalitzat a la ruta, mentre que Everdisk fa servir el port 4455. Així que la ruta senzilla d'Assignar una unitat de xarxa sovint no hi arribarà. Fes servir un gestor d'arxius que et permeti definir un port personalitzat, o connecta't des de Windows amb WebDAV, FTP o l'enllaç del navegador. Tots aquests funcionen des de Windows sense cap problema de port.
{{% /details %}}

{{% details title="Com comparteixo arxius entre dos iPhones amb SMB?" closed="true" %}}
Inicia el servidor SMB al primer iPhone a Everdisk. Al segon iPhone, obre l'app Arxius, toca el botó més, tria Connectar al servidor, i introdueix l'adreça smb que es mostra a Everdisk (per exemple smb://192.168.1.20:4455/Share). Connecta't com a Convidat o amb el teu inici de sessió, i la compartició apareix a Arxius. També pots fer servir la mateixa pestanya Dispositius d'Everdisk al segon telèfon.
{{% /details %}}

{{% details title="El meu iPhone apareix automàticament a la barra lateral del Finder del Mac?" closed="true" %}}
Normalment sí. Everdisk anuncia la compartició SMB a la teva Wi-Fi, així que el teu iPhone sovint apareix sota Ubicacions o Xarxa a la barra lateral del Finder. Fes-hi clic i tria Connectar com a, després Convidat o el teu inici de sessió. Si no apareix, connecta't a mà amb Anar, Connectar al servidor i l'adreça smb completa.
{{% /details %}}

{{% details title="Necessito una contrasenya per fer servir SMB?" closed="true" %}}
No, un inici de sessió és opcional. Deixa l'Inici de sessió i la Contrasenya buits a Configuració, Compartició, Accés per permetre l'accés de convidats. Defineix-los si vols que les connexions iniciïn sessió. Un inici de sessió i una contrasenya només són obligatoris si actives Requereix xifratge SMB, perquè les connexions xifrades no poden ser anònimes.
{{% /details %}}

{{% details title="La connexió SMB està xifrada?" closed="true" %}}
Pot estar-ho. SMB és l'única connexió d'Everdisk que admet xifratge. Defineix un inici de sessió i una contrasenya, i després activa Requereix xifratge SMB a Configuració, Compartició. Cada transferència queda aleshores protegida amb SMB3 (AES). L'altre dispositiu ha d'admetre SMB3, cosa que els Mac moderns i Windows 10 o posterior fan. El xifratge és una funció Premium.
{{% /details %}}

{{% details title="La gent pot canviar o eliminar els meus arxius per SMB?" closed="true" %}}
Només si ho permets. L'interruptor Edició de fitxers a Configuració, Compartició, Accés controla això. Amb això activat, els dispositius connectats poden pujar, canviar de nom i eliminar. Amb això desactivat, la compartició és de només lectura i els altres poden explorar i copiar arxius del teu telèfon però no poden canviar res.
{{% /details %}}

{{% details title="Per què s'ha tallat la meva connexió SMB?" closed="true" %}}
El teu iPhone és el servidor, i iOS posa en pausa les apps que estan massa estona en segon pla. Mantén Everdisk obert a la pantalla mentre hi hagi un dispositiu connectat, i connecta el telèfon a l'electricitat durant les transferències llargues. També assegura't que tots dos dispositius s'han quedat a la mateixa Wi-Fi.
{{% /details %}}

{{% details title="SMB, WebDAV o FTP, quin hauria de fer servir?" closed="true" %}}
Fes servir SMB quan vols que el telèfon es comporti com una unitat de xarxa de debò en un Mac, un altre iPhone, Linux o un NAS, i quan vols xifratge. Fes servir WebDAV quan vols una unitat de xarxa que també funcioni bé des de Windows. Fes servir FTP per a la compatibilitat més àmplia amb dispositius i apps antics. Everdisk pot fer-los funcionar tots alhora, així que no quedes lligat a cap.
{{% /details %}}

{{% details title="Everdisk és gratis?" closed="true" %}}
Sí, Everdisk es baixa gratis i el servidor SMB hi està inclòs. La compra opcional única Premium afegeix el xifratge SMB, ports personalitzats i uns quants altres extres. Pots configurar SMB i compartir arxius sense pagar.
{{% /details %}}

Vols provar-ho? [Baixa Everdisk de l'App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) i obre el teu iPhone al Finder en aproximadament un minut. Preguntes o comentaris? Escriu-nos a **support@everappz.com**.
