---
title: "Transferir fitxers de l'ordinador a l'iPhone mitjançant el protocol SMB"
description: "Apreneu a transferir i accedir a fitxers grans des del vostre Mac o Windows PC al vostre iPhone o iPad mitjançant Evermusic i el protocol SMB. Una guia pas a pas per a la transmissió i gestió de fitxers sense problemes."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["transferir fitxers a iPhone SMB", "transmetre música del PC a l'iPhone", "connectar Mac a iPhone SMB", "configuració Evermusic SMB", "accedir a fitxers de l'ordinador iPhone", "compartir música de Windows iOS", "transferència de fitxers SMB Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Resum:** Utilitzeu Evermusic al vostre iPhone o iPad per accedir a fitxers emmagatzemats al vostre Mac o Windows PC a través de la vostra xarxa local via SMB. Sense cables, sense iTunes, sense necessitat de pujar al núvol. Activeu la compartició de fitxers al vostre ordinador, connecteu-vos des de l'aplicació i navegueu o reproduïu els vostres fitxers sense fils.

Teniu una extensa col·lecció de fitxers grans al vostre MAC o PC i voleu accedir-hi fàcilment des del vostre iPhone o iPad? Les nostres aplicacions ofereixen una solució senzilla.

Seguiu aquests passos per habilitar l'accés fluid entre el vostre ordinador i el dispositiu iOS mitjançant el protocol SMB:

## Pas 1: Activar el protocol SMB al vostre ordinador

**Per a MAC:**

1. Obriu "Preferències del Sistema" al vostre MAC.
2. Feu clic a "Compartir".
3. Activeu el servei "Compartició de fitxers".
4. Afegiu la vostra carpeta de música a la secció "Carpetes compartides". Afegiu un usuari i trieu el nivell de permisos (Lectura i escriptura o Només lectura). Podeu optar per "Tothom: Només lectura" per a la carpeta de música afegida.

   ![Pantalla de configuració del Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Recordeu l'URL de l'ordinador (smb://192.168.xx.xx), ja que el fareu servir en els passos següents.
6. Feu clic a "Opcions" i activeu "Compartir fitxers i carpetes mitjançant SMB".

   ![Pantalla de compartició de fitxers del Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Activeu "Compartició de fitxers de Windows" per als comptes disponibles.

   ![Pantalla de compartició SMB del Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Per a Windows PC:**

1. Feu clic dret a la vostra carpeta de música.
2. Seleccioneu "Propietats".
3. Aneu a la pestanya "Compartir".
4. Feu clic a "Compartir..."
5. Trieu les persones amb qui voleu compartir la carpeta i especifiqueu el nivell de permisos. Podeu seleccionar "Tothom: Lectura" per a la carpeta de música triada.

   ![Pantalla de compartició SMB de Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Feu clic a "Fet".
7. Feu clic a "Fet" a la finestra de "Compartició de fitxers" i recordeu la ruta de la carpeta.

   ![Carpeta compartida SMB de Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Pas 2: Connectar el vostre dispositiu iOS

1. Obriu l'aplicació al vostre iPhone o iPad.
2. Aneu a la pestanya "Connexions".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Pantalla de Connexions d'Evermusic"
  caption="Pantalla de Connexions d'Evermusic"
  width="400"
>}}

*Si el vostre ordinador apareix a la secció "Dispositius disponibles":*

Si el vostre ordinador és visible a la secció "Dispositius disponibles" i heu seleccionat "Tothom: Només lectura" al pas anterior, simplement toqueu el vostre ordinador i es connectarà automàticament.

*Si el vostre ordinador no apareix automàticament:*

1. Toqueu "Connectar un servei al núvol".
2. Seleccioneu "SMB" a la pantalla "Connectar un servei al núvol".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Pantalla de Connectar un servei al núvol d'Evermusic"
  caption="Pantalla de Connectar un servei al núvol d'Evermusic"
  width="400"
>}}

3. A la pantalla "Connexió SMB", introduïu l'URL del servidor amb la ruta de la carpeta compartida. Podeu utilitzar el nom del servidor o la IP del servidor:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Introduïu el vostre nom d'usuari i contrasenya o deixeu aquests camps en blanc si heu seleccionat "Tothom: Només lectura" al pas anterior.
5. El camp "WORKGROUP" és opcional i s'ha d'utilitzar si teniu un Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Pantalla del connector SMB d'Evermusic"
  caption="Pantalla del connector SMB d'Evermusic"
  width="400"
>}}

6. Un cop hàgiu connectat el vostre ordinador mitjançant el protocol SMB, apareixerà a la secció "Serveis al núvol" de la pantalla "Connexions".
7. Obriu el servei connectat i navegueu fins a la carpeta desitjada.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Carpeta SMB oberta a Evermusic"
  caption="Carpeta SMB oberta a Evermusic"
  width="400"
>}}

8. Podeu utilitzar el gestor de fitxers integrat per editar els vostres fitxers segons calgui.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Gestor de fitxers d'Evermusic"
  caption="Gestor de fitxers d'Evermusic"
  width="400"
>}}

## Pas 3: Solució alternativa per a carpetes SMB2 amb caràcters especials

De vegades podeu trobar problemes amb carpetes que contenen caràcters especials quan utilitzeu el protocol SMB2. Aquí teniu alguns passos per resoldre aquest problema:

1. **Activar SMB 1:**  
   • Com a solució temporal, proveu d'activar SMB 1 al vostre servidor i a la configuració de l'aplicació. Això pot ajudar a evitar els problemes relacionats amb caràcters especials als noms de les carpetes.

2. **Utilitzar el menú d'obertura de fitxers del sistema:**  
   • Aneu a "Fitxers locals".  
   • Desplaceu-vos cap avall fins a la secció "Fitxers en aquest dispositiu".  
   • Toqueu "Obrir fitxers..." o "Obrir carpetes...".  
   • Localitzeu el vostre servidor i seleccioneu els fitxers o carpetes que necessiteu.  
   • Toqueu "Obrir" per confirmar la vostra selecció.

3. **Protocols alternatius:**  
   • Si el problema persisteix, considereu connectar-vos al vostre NAS mitjançant protocols WebDAV o DLNA si el vostre NAS admet aquestes opcions. Aquests protocols poden gestionar els caràcters especials de manera més adequada.

Seguint aquests passos, podeu mitigar els problemes amb caràcters especials als noms de les carpetes quan utilitzeu el protocol SMB2.

## Conclusió

Amb aquests passos, podeu accedir fàcilment a la vostra gran col·lecció de fitxers del vostre MAC o PC al vostre iPhone o iPad mitjançant les nostres aplicacions.

## Preguntes freqüents

{{% details title="Puc accedir als fitxers del meu PC des del meu iPhone sense iTunes?" closed="true" %}}
Sí. Evermusic es connecta al vostre ordinador via SMB a la vostra xarxa Wi-Fi local. No cal sincronització amb iTunes o Finder. Activeu la compartició de fitxers al vostre PC i connecteu-vos directament des de l'aplicació.
{{% /details %}}

{{% details title="L'accés a fitxers SMB funciona per Internet?" closed="true" %}}
No. SMB és un protocol de xarxa local. El vostre iPhone i l'ordinador han d'estar a la mateixa xarxa Wi-Fi. Per a l'accés remot, pugeu els fitxers a un servei al núvol com Google Drive o Dropbox i connecteu-vos-hi des d'Evermusic.
{{% /details %}}

{{% details title="Quins tipus de fitxers puc accedir via SMB?" closed="true" %}}
Evermusic admet MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC i altres formats d'àudio. També podeu navegar i gestionar fitxers no d'àudio mitjançant el gestor de fitxers integrat.
{{% /details %}}

{{% details title="Puc transferir fitxers d'un NAS al meu iPhone mitjançant SMB?" closed="true" %}}
Sí. La majoria de dispositius NAS (Synology, QNAP, WD My Cloud i altres) admeten SMB. Connecteu-vos al vostre NAS seguint els mateixos passos d'aquesta guia.
{{% /details %}}

{{% details title="Necessito copiar els fitxers al meu iPhone per reproduir-los?" closed="true" %}}
No. Evermusic transmet els fitxers directament des del vostre ordinador o NAS a través de la xarxa. Els fitxers no es copien al vostre iPhone tret que trieu descarregar-los per a la reproducció sense connexió.
{{% /details %}}

{{% details title="La compartició de fitxers SMB és segura?" closed="true" %}}
La compartició de fitxers SMB funciona només a la vostra xarxa local. Altres dispositius en xarxes diferents no poden accedir a les vostres carpetes compartides. Per a una seguretat addicional, utilitzeu un nom d'usuari i contrasenya en lloc de l'accés anònim (Tothom).
{{% /details %}}
