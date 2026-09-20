---
title: "Com configurar un servidor WebDAV a l'iPhone i l'iPad per accedir a arxius i compartir-los"
description: "Converteix el teu iPhone o iPad en un servidor WebDAV amb Everdisk i munta'l com una unitat de xarxa al Finder del Mac, a l'Explorador d'arxius de Windows, a Linux, a Android o a un altre iPhone per Wi-Fi. Configuració completa, l'adreça i el port WebDAV, i connexió pas a pas per a cada dispositiu."
date: 2026-09-19
tags: ["everdisk", "webdav", "unitat de xarxa", "compartir arxius", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["servidor WebDAV iPhone", "servidor WebDAV iPad", "com configurar WebDAV a l'iPhone", "muntar iPhone com a unitat de xarxa", "connectar iPhone WebDAV Mac Finder", "WebDAV Explorador d'arxius Windows iPhone", "unitat de xarxa iphone Windows", "WebDAV Linux iPhone", "accedir a arxius de l'iPhone des de l'ordinador", "webdav iphone a iphone", "compartir arxius iPhone WebDAV", "assignar unitat de xarxa iphone", "transferir arxius iphone webdav", "adreça port webdav iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV converteix una carpeta en una unitat de xarxa que un ordinador pot obrir amb el seu gestor d'arxius habitual. Funciona amb el mateix protocol web que fa servir el teu navegador, i per això viatja bé entre Mac, Windows i Linux sense controladors especials. Amb [Everdisk](/products/everdisk) pots fer funcionar un servidor WebDAV al teu iPhone o iPad, de manera que el telèfon apareix com una unitat que pots explorar, de la qual copies i a la qual copies des de gairebé qualsevol ordinador.

WebDAV és la millor opció quan Windows hi és involucrat, perquè l'Explorador d'arxius de Windows s'hi connecta netament. Aquesta guia cobreix la configuració i com connectar-te des d'un Mac, Windows, Linux, Android i un segon iPhone.

## Què necessites

- Un iPhone o iPad amb [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) instal·lat.
- Un ordinador o un altre dispositiu a la **mateixa xarxa Wi-Fi**.
- Els arxius que vols compartir, a la carpeta Documents d'Everdisk o a carpetes que afegeixis.

## Configura el servidor WebDAV a Everdisk

### Pas 1: Tria què compartir i defineix l'accés

Obre Everdisk, ves a la pestanya **Compartició** i toca **Què compartir**. La carpeta Documents es comparteix per defecte. Afegeix-ne més amb **Afegeix una carpeta** i **Afegeix un fitxer**.

Obre **Configuració**, després **Compartició** i després **Accés**. Activa **Edició de fitxers** si vols que els ordinadors connectats copiïn arxius al teu telèfon i els canviïn de nom o els eliminin, o desactiva-la per a una unitat de només lectura. Defineix aquí un **Inici de sessió** i una **Contrasenya** si vols un inici de sessió, o deixa'ls buits per a l'accés de convidats.

### Pas 2: Activa el servidor WebDAV

Ves a **Configuració**, després a **Compartició** i després a **Connexions**, i activa **Ordinador**. Aquest és el servidor WebDAV (porta l'etiqueta WebDAV).

### Pas 3: Comença a compartir i anota l'adreça

Torna a la pestanya **Compartició** i toca **Iniciar**. La secció **Com connectar-se** mostra l'adreça WebDAV. Té aquest aspecte:

```
http://192.168.1.20:8080
```

El número després dels dos punts és el **port**, que és **8080** per defecte. La primera part és l'adreça del teu iPhone a la Wi-Fi, així que la teva serà diferent. Mantén Everdisk obert a la pantalla mentre hi hagi un dispositiu connectat.

## Connecta't des d'un Mac

1. Obre el **Finder**, tria **Anar**, després **Connectar al servidor** (o prem **Command i K**).
2. Escriu l'adreça WebDAV que es mostra a Everdisk, per exemple `http://192.168.1.20:8080`.
3. Fes clic a **Connectar**, després tria **Convidat** o introdueix el teu **Inici de sessió** i **Contrasenya**.

El teu iPhone s'obre en una finestra del Finder i es comporta com una carpeta normal. Copia arxius en qualsevol direcció si Edició de fitxers està activada.

## Connecta't des de Windows

Windows té un client WebDAV integrat, així que això funciona des de l'Explorador d'arxius.

1. Obre l'**Explorador d'arxius**, fes clic dret a **Aquest ordinador** a la barra lateral i tria **Afegir una ubicació de xarxa** (també pots fer servir **Assignar una unitat de xarxa**).
2. Quan et demani l'adreça, escriu la mateixa adreça WebDAV d'Everdisk, per exemple `http://192.168.1.20:8080`, i després fes clic a **Següent**.
3. Introdueix el teu **Inici de sessió** i **Contrasenya** si n'has definit un.

El dispositiu apareix aleshores sota Aquest ordinador com una ubicació de xarxa que pots obrir i de la qual copiar arxius. Si Windows es nega a connectar-se el primer cop, assegura't que el servei **WebClient** s'està executant (busca Serveis al menú Inici, troba WebClient i configura'l perquè s'iniciï), i després torna-ho a provar.

## Connecta't des de Linux

1. Obre el teu gestor d'arxius i tria **Connectar al servidor** o **Altres ubicacions**.
2. Introdueix l'adreça amb un prefix WebDAV, per exemple `dav://192.168.1.20:8080` (fes servir `davs://` només si has configurat TLS).
3. Connecta't com a convidat o introdueix el teu inici de sessió.

## Connecta't des d'Android

Android no té un explorador WebDAV del sistema, així que fes servir un gestor d'arxius compatible:

1. Instal·la una app com ara **Solid Explorer** o **CX File Explorer**.
2. Afegeix una connexió **WebDAV** nova.
3. Introdueix l'amfitrió i el **port 8080**, tria l'esquema `http`, i afegeix el teu inici de sessió si n'has definit un.

## Connecta't des d'un altre iPhone o iPad

L'app Arxius d'iOS no inclou un client WebDAV, així que fes servir una d'aquestes:

- **La mateixa pestanya Dispositius d'Everdisk.** Al segon dispositiu, obre Everdisk, ves a **Dispositius**, toca **Connexió nova**, tria **WebDAV** i introdueix l'adreça, per exemple `http://192.168.1.20:8080`. Aquesta és la ruta més senzilla i no necessita res més.
- **Una app WebDAV** com ara Documents by Readdle, que pot afegir una connexió WebDAV amb la mateixa adreça i inici de sessió.

## Prefereixes un enllaç ràpid en lloc d'una unitat?

Si només necessites agafar un arxiu de pressa i no vols muntar cap unitat, activa la connexió **Navegador** a Configuració, Compartició, Connexions. Everdisk et dona aleshores una adreça web que pots obrir a qualsevol navegador de qualsevol dispositiu per explorar i baixar els teus arxius. És la manera més ràpida de lliurar un arxiu a un PC amb Windows, un Chromebook o el telèfon d'un amic.

## Només lectura o lectura i escriptura

L'interruptor **Edició de fitxers** a Configuració, Compartició, Accés decideix això. Activat vol dir que els ordinadors connectats poden pujar, canviar de nom i eliminar. Desactivat vol dir que la unitat és de només lectura, així que els altres poden veure i copiar els teus arxius però no poden canviar-los.

## Maneres reals com la gent fa servir això

- **Copiar arxius al teu iPhone des d'un PC amb Windows** assignant-lo com una ubicació de xarxa i arrossegant-los.
- **Descarregar fotos i documents a un portàtil** amb el gestor d'arxius que ja coneixes, sense cable ni iTunes.
- **Editar un document al seu lloc** des del teu Mac, obrint-lo directament des del telèfon i desant-lo de nou.
- **Moure una carpeta entre un iPhone i un iPad** amb la pestanya Dispositius d'Everdisk al dispositiu que rep.

## Uns quants consells

- Mantén Everdisk obert mentre hi hagi un dispositiu connectat. Bloquejar el telèfon durant molta estona pot posar en pausa l'app.
- A Windows, si la connexió falla, inicia el servei WebClient i torna a provar l'adreça.
- WebDAV i SMB es munten tots dos com a unitats de xarxa. Fes servir WebDAV quan hi hagi Windows involucrat, i [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) quan vols la velocitat del Finder i el xifratge.
- Per a les transferències més ràpides, mantén la qualitat de fotos i vídeos en Original a Configuració.

## Preguntes freqüents

{{% details title="Quina és l'adreça i el port WebDAV del meu iPhone?" closed="true" %}}
Després que comencis a compartir, Everdisk mostra l'adreça a la pantalla Compartició. Té l'aspecte http://192.168.1.20:8080. El 8080 és el port que Everdisk fa servir per a WebDAV, i la primera part és l'adreça del teu iPhone a la Wi-Fi, així que la teva serà diferent.
{{% /details %}}

{{% details title="Com em connecto al WebDAV del meu iPhone des de Windows?" closed="true" %}}
Obre l'Explorador d'arxius, fes clic dret a Aquest ordinador, i tria Afegir una ubicació de xarxa o Assignar una unitat de xarxa. Introdueix l'adreça WebDAV d'Everdisk, per exemple http://192.168.1.20:8080, i després introdueix el teu inici de sessió si n'has definit un. Si Windows no es connecta, assegura't que el servei WebClient s'està executant (busca Serveis, troba WebClient, inicia'l) i torna-ho a provar.
{{% /details %}}

{{% details title="Puc fer servir WebDAV entre dos iPhones?" closed="true" %}}
Sí, però l'app Arxius d'iOS no té client WebDAV, així que fes servir Everdisk al segon dispositiu. Obre la pestanya Dispositius, toca Connexió nova, tria WebDAV, i introdueix l'adreça que es mostra al primer telèfon. Una app WebDAV com Documents by Readdle també funciona.
{{% /details %}}

{{% details title="WebDAV necessita contrasenya?" closed="true" %}}
No, un inici de sessió és opcional. Deixa l'Inici de sessió i la Contrasenya buits a Configuració, Compartició, Accés per a l'accés de convidats, o defineix-los si vols que les connexions iniciïn sessió.
{{% /details %}}

{{% details title="Altres persones poden canviar els meus arxius per WebDAV?" closed="true" %}}
Només si ho permets. L'interruptor Edició de fitxers a Configuració, Compartició, Accés controla això. Activat deixa que els dispositius connectats pugin, canviïn de nom i eliminin. Desactivat fa que la unitat sigui de només lectura, així que els altres poden veure i copiar però no canviar res.
{{% /details %}}

{{% details title="WebDAV o SMB, quina diferència hi ha?" closed="true" %}}
Tots dos munten el teu iPhone com una unitat de xarxa. WebDAV funciona amb el protocol web i es connecta netament des de l'Explorador d'arxius de Windows, cosa que és el seu punt fort principal. SMB és la compartició d'arxius nativa a Mac, Linux i dispositius NAS, sol ser més ràpid en un Mac, i és l'única connexió d'Everdisk que pot xifrar les transferències. Everdisk pot fer funcionar tots dos alhora.
{{% /details %}}

{{% details title="Per què es desconnecta la meva unitat WebDAV?" closed="true" %}}
El teu iPhone és el servidor, i iOS posa en pausa les apps que estan massa estona en segon pla. Mantén Everdisk obert a la pantalla mentre hi hagi un dispositiu connectat, i connecta'l a l'electricitat durant les transferències llargues. També confirma que tots dos dispositius encara són a la mateixa Wi-Fi.
{{% /details %}}

{{% details title="Puc connectar-me per WebDAV sense Wi-Fi?" closed="true" %}}
Sí, si connectes el teu iPhone a un Mac amb un cable. Everdisk mostra aleshores una adreça de connexió per cable addicional que el Mac connectat pot obrir al Finder, cosa que funciona fins i tot sense gens de Wi-Fi. Pel cable, només aquell Mac pot arribar al dispositiu.
{{% /details %}}

{{% details title="Everdisk és gratis?" closed="true" %}}
Sí, Everdisk es baixa gratis i el servidor WebDAV hi està inclòs. Una compra opcional única Premium afegeix extres com ports personalitzats i la conversió de fotos i vídeos. Pots configurar WebDAV i compartir arxius sense pagar.
{{% /details %}}

Vols provar-ho? [Baixa Everdisk de l'App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) i munta el teu iPhone com una unitat en un parell de minuts. Preguntes o comentaris? Escriu-nos a **support@everappz.com**.
