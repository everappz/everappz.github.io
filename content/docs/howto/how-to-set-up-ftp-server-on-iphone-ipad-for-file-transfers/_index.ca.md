---
title: "Com configurar un servidor FTP a l'iPhone i l'iPad per transferir arxius"
description: "Converteix el teu iPhone o iPad en un servidor FTP amb Everdisk i transfereix arxius des d'un Mac, un PC amb Windows, Linux, Android, una app FTP com FileZilla o un altre iPhone per Wi-Fi. Configuració completa, l'adreça i el port ftp, accés de convidats i connexió pas a pas per a cada dispositiu."
date: 2026-09-19
tags: ["everdisk", "ftp", "transferència d'arxius", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["servidor FTP iPhone", "servidor FTP iPad", "com configurar FTP a l'iPhone", "app servidor ftp iphone", "connectar FileZilla a l'iPhone", "Cyberduck iPhone FTP", "transferir arxius iPhone FTP", "ftp iphone a ordinador", "ftp iphone a iphone", "connectar a FTP de l'iPhone des de Windows", "adreça port ftp iphone", "ftp anònim iphone", "compartir arxius iphone ftp", "ftp iphone per a càmera nas"]
readingTime: 9
---

{{< author-byline >}}

FTP és el vell fiable de la transferència d'arxius. Fa dècades que existeix, que és exactament per què és tan útil: gairebé tot el que pot parlar amb un servidor l'entén. Càmeres, televisors intel·ligents, routers, unitats de xarxa, eines d'automatització i totes les apps FTP d'escriptori parlen FTP. Amb [Everdisk](/products/everdisk) pots fer funcionar un servidor FTP al teu iPhone o iPad, de manera que el telèfon esdevé un lloc al qual aquests dispositius i apps es poden connectar i moure arxius.

Recorre a l'FTP quan les altres opcions no encaixen, per exemple un dispositiu més antic o una app que només sap connectar-se per FTP. Aquesta guia cobreix la configuració i com connectar-te des d'un Mac, Windows, una app FTP, Linux, Android i un segon iPhone.

## Què necessites

- Un iPhone o iPad amb [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) instal·lat.
- Un ordinador, app o dispositiu a la **mateixa xarxa Wi-Fi**.
- Els arxius que vols compartir, a la carpeta Documents d'Everdisk o a carpetes que afegeixis.

## Configura el servidor FTP a Everdisk

### Pas 1: Tria què compartir i defineix l'accés

Obre Everdisk, ves a la pestanya **Compartició** i toca **Què compartir**. La carpeta Documents es comparteix per defecte. Afegeix-ne més amb **Afegeix una carpeta** i **Afegeix un fitxer**.

Obre **Configuració**, després **Compartició** i després **Accés**. Activa **Edició de fitxers** si vols que la gent pugi, canviï de nom i elimini, o desactiva-la per permetre només baixades. Defineix un **Inici de sessió** i una **Contrasenya** si vols un inici de sessió, o deixa'ls buits perquè qualsevol es pugui connectar com a convidat.

### Pas 2: Activa el servidor FTP

Ves a **Configuració**, després a **Compartició** i després a **Connexions**, i activa **Altres aplicacions i dispositius**. Aquest és el servidor FTP (porta l'etiqueta FTP).

### Pas 3: Comença a compartir i anota l'adreça

Torna a la pestanya **Compartició** i toca **Iniciar**. La secció **Com connectar-se** mostra l'adreça FTP. Té aquest aspecte:

```
ftp://192.168.1.20:2121
```

El número després dels dos punts és el **port**, que és **2121** per defecte. La primera part és l'adreça del teu iPhone a la Wi-Fi, així que la teva serà diferent. Mantén Everdisk obert a la pantalla mentre hi hagi un dispositiu connectat.

## Connecta't des d'un Mac

1. Obre el **Finder**, tria **Anar**, després **Connectar al servidor** (o prem **Command i K**).
2. Escriu l'adreça FTP que es mostra a Everdisk, per exemple `ftp://192.168.1.20:2121`.
3. Fes clic a **Connectar**, després tria **Convidat** o introdueix el teu **Inici de sessió** i **Contrasenya**.

El Finder munta la compartició FTP perquè puguis explorar i copiar arxius al teu Mac. Tingues en compte que el Finder obre l'FTP com a només lectura. Quan vulguis pujar des d'un Mac, fes servir una app FTP com es descriu més avall.

## Connecta't des de Windows

1. Obre l'**Explorador d'arxius** i fes clic a la barra d'adreces de dalt.
2. Escriu l'adreça FTP d'Everdisk, per exemple `ftp://192.168.1.20:2121`, i prem **Retorn**.
3. Introdueix el teu **Inici de sessió** i **Contrasenya** si n'has definit un, o continua com a convidat.

Els arxius compartits apareixen a la finestra i els pots copiar al teu PC.

## Connecta't amb una app FTP (FileZilla, Cyberduck)

Per a pujades i control total, una app FTP és la millor eina. **FileZilla** i **Cyberduck** són gratuïtes i funcionen a Windows, Mac i Linux.

1. Obre l'app i crea una connexió nova.
2. Configura l'**Host** amb l'adreça Wi-Fi del teu iPhone, i el **Port** amb **2121**.
3. Per a l'inici de sessió, introdueix el teu **Inici de sessió** i **Contrasenya**, o tria **Anonymous** si no n'has definit cap.
4. Connecta't, i arrossega arxius en totes dues direccions (les pujades necessiten Edició de fitxers activada).

## Connecta't des de Linux

1. Obre el teu gestor d'arxius i tria **Connectar al servidor** o **Altres ubicacions**.
2. Introdueix l'adreça, per exemple `ftp://192.168.1.20:2121`.
3. Connecta't com a convidat o amb el teu inici de sessió.

També pots fer servir qualsevol client FTP de Linux des del terminal, apuntant-lo al mateix host i port 2121.

## Connecta't des d'Android

Android no té un explorador FTP del sistema, així que fes servir una app:

1. Instal·la un client FTP com ara **AndFTP**, **FTPCafe**, o un gestor d'arxius amb suport FTP com **Solid Explorer**.
2. Afegeix una connexió amb l'host, el **port 2121** i el teu inici de sessió o Anonymous.
3. Explora i transfereix.

## Connecta't des d'un altre iPhone o iPad

L'app Arxius d'iOS no inclou un client FTP, així que fes servir una d'aquestes al segon dispositiu:

- **La mateixa pestanya Dispositius d'Everdisk.** Obre Everdisk, ves a **Dispositius**, toca **Connexió nova**, tria **FTP** i introdueix l'adreça, per exemple `ftp://192.168.1.20:2121`. Aquesta és la ruta més senzilla.
- **Una app FTP dedicada** per a iOS, amb el mateix host, port 2121 i inici de sessió.

## Connecta altre maquinari: càmeres, televisors, routers i NAS

Aquí és on l'FTP brilla. Molts dispositius tenen un client FTP integrat que pot enviar o recuperar arxius:

- **Les càmeres** que pugen fotos per FTP poden enviar-les directament al teu iPhone.
- **Els televisors intel·ligents, routers, caixes NAS i eines d'automatització** compatibles amb FTP es poden connectar de la mateixa manera.

Apunta'ls a l'adreça Wi-Fi del teu iPhone, al port **2121** i al teu inici de sessió (o Anonymous), amb l'adreça que es mostra a Everdisk.

## Només lectura o lectura i escriptura

L'interruptor **Edició de fitxers** a Configuració, Compartició, Accés controla això. Activat deixa que la gent pugi, canviï de nom i elimini. Desactivat vol dir que només poden baixar. Tria només lectura quan lliures arxius i no vols que es canviï res al teu telèfon.

## Maneres reals com la gent fa servir això

- **Connectar FileZilla al teu iPhone** i pujar un lot d'arxius al telèfon d'una sola vegada.
- **Deixar que una app o dispositiu antic que només parla FTP** arribi als teus arxius quan res més es connecta.
- **Rebre fotos d'una càmera** que puja per FTP.
- **Moure arxius entre un iPhone i un iPad** amb la pestanya Dispositius d'Everdisk al dispositiu que rep.

## Uns quants consells

- Mantén Everdisk obert mentre hi hagi un dispositiu connectat, ja que iOS posa en pausa les apps en segon pla al cap d'una estona.
- Per pujar des d'un Mac, fes servir FileZilla o Cyberduck en lloc del Finder, perquè el Finder obre l'FTP com a només lectura.
- Deixa l'inici de sessió buit per a la compatibilitat més àmplia, i després connecta't com a Anonymous, cosa que la majoria de clients FTP ofereixen.
- L'FTP no xifra el seu trànsit. En una xarxa en què no confies, fes servir el [servidor SMB amb xifratge](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/).

## Preguntes freqüents

{{% details title="Quina és l'adreça i el port FTP del meu iPhone?" closed="true" %}}
Després que comencis a compartir, Everdisk mostra l'adreça a la pantalla Compartició. Té l'aspecte ftp://192.168.1.20:2121. El 2121 és el port que Everdisk fa servir per a FTP, i la primera part és l'adreça del teu iPhone a la Wi-Fi, així que la teva serà diferent.
{{% /details %}}

{{% details title="Com connecto FileZilla o Cyberduck al meu iPhone?" closed="true" %}}
Obre l'app i crea una connexió nova. Configura l'Host amb l'adreça Wi-Fi del teu iPhone i el Port amb 2121. Introdueix el teu Inici de sessió i Contrasenya, o tria Anonymous si no n'has definit cap a Everdisk. Connecta't, i pots arrossegar arxius en totes dues direccions quan Edició de fitxers està activada.
{{% /details %}}

{{% details title="Puc connectar-me a l'FTP del meu iPhone des de Windows?" closed="true" %}}
Sí. Obre l'Explorador d'arxius, fes clic a la barra d'adreces, escriu l'adreça FTP d'Everdisk (per exemple ftp://192.168.1.20:2121) i prem Retorn. Introdueix el teu inici de sessió si n'has definit un, o continua com a convidat. Per a pujades i més control, fes servir una app FTP com FileZilla.
{{% /details %}}

{{% details title="Necessito un inici de sessió per a l'FTP?" closed="true" %}}
No, un inici de sessió és opcional. Deixa l'Inici de sessió i la Contrasenya buits a Configuració, Compartició, Accés, i connecta't com a Anonymous, cosa que la majoria de clients FTP ofereixen. Defineix un inici de sessió si vols que les connexions iniciïn sessió primer.
{{% /details %}}

{{% details title="Per què només puc baixar i no pujar per FTP?" closed="true" %}}
Dues raons són habituals. Primera, l'interruptor Edició de fitxers a Configuració, Compartició, Accés ha d'estar activat per permetre pujades, canvis de nom i eliminacions. Segona, el Finder del Mac obre l'FTP com a només lectura, així que fes servir una app FTP com FileZilla o Cyberduck quan vulguis pujar.
{{% /details %}}

{{% details title="Puc fer servir FTP entre dos iPhones?" closed="true" %}}
Sí. Inicia el servidor FTP al primer iPhone. Al segon, obre Everdisk, ves a la pestanya Dispositius, toca Connexió nova, tria FTP, i introdueix l'adreça que es mostra al primer telèfon. Una app FTP dedicada per a iOS també funciona, ja que l'app Arxius d'iOS no inclou un client FTP.
{{% /details %}}

{{% details title="L'FTP és segur?" closed="true" %}}
L'FTP simple no xifra el seu trànsit, així que tracta'l com una eina per a xarxes en què confies, com la teva Wi-Fi de casa. En una xarxa que no controles, fes servir el servidor SMB amb Requereix xifratge SMB activat, que protegeix cada transferència.
{{% /details %}}

{{% details title="Quins dispositius es poden connectar per FTP?" closed="true" %}}
Gairebé qualsevol cosa amb un client FTP. Això inclou ordinadors Mac, Windows i Linux, apps FTP com FileZilla i Cyberduck, gestors d'arxius d'Android, i maquinari com càmeres, televisors intel·ligents, routers, caixes NAS i eines d'automatització. Aquest abast ampli és la raó principal per triar FTP.
{{% /details %}}

{{% details title="Per què s'ha tallat la meva connexió FTP?" closed="true" %}}
El teu iPhone és el servidor, i iOS posa en pausa les apps que estan massa estona en segon pla. Mantén Everdisk obert a la pantalla mentre hi hagi un dispositiu connectat, i connecta'l a l'electricitat durant les transferències llargues. També assegura't que tots dos dispositius encara són a la mateixa Wi-Fi.
{{% /details %}}

{{% details title="Everdisk és gratis?" closed="true" %}}
Sí, Everdisk es baixa gratis i el servidor FTP hi està inclòs. Una compra opcional única Premium afegeix extres com ports personalitzats i la conversió de fotos i vídeos. Pots configurar FTP i transferir arxius sense pagar.
{{% /details %}}

Vols provar-ho? [Baixa Everdisk de l'App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) i connecta el teu primer client FTP en un parell de minuts. Preguntes o comentaris? Escriu-nos a **support@everappz.com**.
