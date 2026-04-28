---
title: "Com connectar Synology NAS i escoltar música al teu iPhone o Mac"
date: 2024-09-19
description: "Aprèn a connectar el teu Synology NAS utilitzant l'API nativa o QuickConnect i reproduir música d'alta qualitat al teu iPhone o Mac amb Evermusic i Flacbox."
keywords: ["synology nas", "reproduir música", "quickconnect", "evermusic synology", "flacbox synology", "reproductor de música nas", "música iphone nas"]
tags: ["música", "reproducció", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Resum:** Connecta el teu Synology NAS a Evermusic o Flacbox utilitzant l'API nativa de Synology -- ja sigui manualment mitjançant l'adreça IP o automàticament mitjançant l'ID de QuickConnect. QuickConnect et permet reproduir música de forma remota sense redirecció de ports. Ambdues aplicacions admeten FLAC, MP3, WAV i altres formats d'alta resolució.

Si busques una manera senzilla de connectar el teu Synology NAS i gaudir de la teva biblioteca musical al teu iPhone o Mac, les aplicacions Evermusic i Flacbox són les solucions perfectes. Aquestes aplicacions admeten una àmplia gamma de formats d'àudio, incloent FLAC, MP3 i WAV, facilitant la reproducció i l'escolta de música d'alta qualitat directament des del teu Synology NAS.

En aquesta guia, et mostrarem com connectar el teu Synology NAS a l'aplicació Evermusic o Flacbox utilitzant l'API nativa de Synology i la funció QuickConnect. Aprofitant l'API directa de Synology, pots accedir de manera segura a la teva biblioteca musical fora de la teva xarxa domèstica sense necessitat de configuracions complicades com WebDAV, SMB, DLNA. Amb QuickConnect, podràs reproduir i gestionar la teva música des de qualsevol lloc, utilitzant el teu iPhone o Mac.

## Pas 1: Configurar els permisos de la carpeta compartida (Opcional)

1. Obre el **Tauler de control** i ves a la secció **Carpeta compartida**.

![Carpeta compartida](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Selecciona la carpeta **Música** i fes clic a **Editar**.

3. A la pestanya **Permisos**, configura els permisos. Activa l'accés de convidats amb només lectura si només necessites escoltar música, o lectura/escriptura si necessites modificar fitxers. Desa els canvis.

![Permisos](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Pas 2: Trobar l'adreça IP del Synology NAS

1. Obre el **Tauler de control** i ves a la pestanya **Interfície de xarxa**.

![Interfície de xarxa](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. O utilitza el teu navegador web per visitar [find.synology.com](http://find.synology.com).

![Trobar Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Anota l'adreça IP del teu Synology NAS (p. ex., 192.168.18.137).

## Pas 3: Trobar els ports de xarxa del Synology NAS

Pots trobar la documentació oficial de Synology per als ports de xarxa predeterminats del DSM en aquest [article del Centre de coneixement de Synology](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM utilitza els ports predeterminats següents:
- **HTTP (Accés web):** Port **5000**
- **HTTPS (Accés web segur):** Port **5001**

Aquests són els ports predeterminats per accedir a la interfície del DSM.

![Ports de xarxa](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Pas 4: Activar la funció d'ID de QuickConnect

Un ID de QuickConnect de Synology és un identificador únic que et permet accedir al teu Synology NAS de forma remota per internet sense necessitat de configurar paràmetres de xarxa complicats com la redirecció de ports. QuickConnect simplifica l'accés remot utilitzant els servidors de Synology per establir una connexió entre el teu NAS i el teu dispositiu, com el teu telèfon intel·ligent o ordinador, a través de l'ID de QuickConnect.

**Com trobar o configurar el teu ID de QuickConnect:**

1. **Inicia sessió al DSM.**
2. Ves a **Tauler de control > Accés extern > QuickConnect**.
3. **Activa QuickConnect** i crea o visualitza el teu ID de QuickConnect únic.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Pas 5: Connectar-se al Synology NAS al teu iPhone/Mac utilitzant Evermusic o Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) i [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) són aplicacions de reproducció de música dissenyades per a dispositius iOS i macOS, cadascuna oferint funcions i capacitats úniques per gestionar i gaudir de la teva biblioteca musical.

1. Obre l'aplicació Evermusic o Flacbox i ves a la pestanya **Connexions**.

![Connexions](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Tria **Connectar un servei al núvol** i selecciona **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Tens dues opcions de connexió: **manual** utilitzant l'adreça IP del servidor i el port, o **automàtica** mitjançant l'ID de QuickConnect.

### Connexió manual

Per al mètode manual, necessitaràs l'adreça IP directa i el número de port que has obtingut en els passos anteriors.

1. Introdueix l'URL del servidor que has obtingut al pas 2, utilitzant el format següent: PROTOCOL://ADREÇA_IP:NÚMERO_PORT
   - Utilitza el **port 5000** per a HTTP i el **port 5001** per a connexions HTTPS.

   Per exemple:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. El número de port real es pot confirmar al pas 3 de la configuració.
3. Introdueix el teu **nom d'usuari** i **contrasenya** per al Synology NAS.
4. Toca **Iniciar sessió** per establir la connexió.

![Connexió manual](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Connexió automàtica

Per a la connexió automàtica, utilitzaràs l'**ID de QuickConnect** del pas 4. En lloc d'introduir manualment l'adreça IP i el número de port del teu Synology NAS, simplement introdueix l'**ID de QuickConnect**. L'aplicació recuperarà automàticament la informació de connexió necessària.

Aquest mètode et permet accedir al teu NAS de forma remota, fins i tot fora de la teva xarxa domèstica, perquè puguis gestionar els teus fitxers des d'internet sense necessitat de configurar la redirecció de ports o adreces IP estàtiques.

![Connexió automàtica](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Autenticació de dos factors

A partir del DSM 4.2, Synology va introduir la **verificació en dos passos** per millorar la seguretat. Aquesta funció requereix un codi de **contrasenya d'un sol ús (OTP)**, generat per una aplicació d'autenticació, a més de les credencials habituals d'inici de sessió. Si has activat la verificació en dos passos, després d'introduir el teu nom d'usuari i contrasenya, també hauràs d'introduir l'OTP per iniciar sessió a la teva sessió DSM.

Tingues en compte que, un cop la sessió expiri, l'aplicació haurà de ser reautoritzada manualment. Per reautoritzar:

1. Ves a la pestanya **Connexions** de l'aplicació.
2. Toca el botó **Més accions** al costat del nom del servidor.
3. Selecciona **Configuració** del menú per introduir el nou codi d'autenticació i completar el procés de reautorització.

Això garanteix que, fins i tot si accedeixes al teu NAS des d'una xarxa no fiable, les teves dades romandran segures.

## Pas 6: Navegar i reproduir música

1. Un cop connectat, el dispositiu apareixerà a la llista de **Dispositius connectats**.

![Dispositius connectats](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Navega fins a la carpeta **Música** i toca qualsevol fitxer d'àudio per començar la reproducció.

![Reproduir música](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Pas 7: Afegir la carpeta al núvol connectada a la biblioteca musical

1. Obre la secció **Biblioteca musical** de l'aplicació.
2. Tria **Afegir música** i selecciona **Connexions**.
3. Tria el servidor NAS connectat i selecciona la carpeta **Música**. Toca **Fet**.
4. L'aplicació escanejarà la carpeta de música i afegirà els fitxers d'àudio compatibles a la biblioteca musical. Es carregaran les metadades i les teves pistes es gruparan per àlbum, artista i gènere.

## Conclusió

Seguint aquests passos, pots configurar fàcilment una connexió al teu Synology NAS i reproduir tota la teva biblioteca musical al teu iPhone o Mac utilitzant Evermusic o Flacbox. Tant si ets a casa com en moviment, gaudeix d'un accés fluid i d'alta qualitat a les teves pistes preferides des de qualsevol lloc amb QuickConnect. Aprofita la flexibilitat i la comoditat que ofereixen aquestes aplicacions i comença a gestionar la teva col·lecció musical amb facilitat a tots els teus dispositius.

Amb accés remot segur a través de QuickConnect i compatibilitat amb una àmplia gamma de formats d'àudio, mai estaràs lluny de la teva música. Ara, els teus fitxers emmagatzemats al NAS estan a un sol toc de distància!

## Preguntes freqüents

{{% details title="Quina diferència hi ha entre la connexió manual i QuickConnect?" closed="true" %}}
La connexió manual utilitza l'adreça IP del NAS i el port, que funciona a la teva xarxa local. QuickConnect utilitza el servei de retransmissió de Synology per establir una connexió des de qualsevol lloc per internet, sense redirecció de ports.
{{% /details %}}

{{% details title="Puc reproduir música des del Synology NAS fora de la meva xarxa domèstica?" closed="true" %}}
Sí. Activa QuickConnect al teu Synology NAS i utilitza l'ID de QuickConnect a Evermusic o Flacbox per reproduir música des de qualsevol lloc amb connexió a internet.
{{% /details %}}

{{% details title="Quins formats d'àudio es poden utilitzar quan es reprodueix des del Synology NAS?" closed="true" %}}
Evermusic i Flacbox admeten FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD i molts altres formats. Tots els formats compatibles funcionen quan es reprodueix des del Synology NAS.
{{% /details %}}

{{% details title="Necessito autenticació de dos factors per connectar-me?" closed="true" %}}
No, l'autenticació de dos factors és opcional. No obstant això, si has activat la verificació en dos passos al teu Synology DSM, l'aplicació et demanarà una contrasenya d'un sol ús durant l'inici de sessió. Hauràs de reautoritzar quan la sessió expiri.
{{% /details %}}

{{% details title="Hauria d'utilitzar l'API nativa de Synology, WebDAV o SMB per connectar-me?" closed="true" %}}
L'API nativa de Synology amb QuickConnect és la millor opció per a l'accés remot. Per a l'ús a la xarxa local, SMB sol ser l'opció més ràpida. WebDAV funciona bé tant per a l'accés local com remot. Evermusic i Flacbox admeten els tres protocols.
{{% /details %}}
