---
title: "Com activar el servidor multimèdia DLNA a Windows 10 i reproduir la teva música a l'iPhone"
date: 2019-11-26
description: "Activa el servidor DLNA a Windows 10 i transmet la teva música a l'iPhone amb l'aplicació Evermusic. Guia de configuració pas a pas inclosa."
keywords: ["evermusic", "dlna", "windows 10", "transmissió de música a iphone", "servidor multimèdia", "xarxa local", "upnp"]
tags: ["evermusic", "música", "núvol", "iphone", "emmagatzematge", "local", "nas", "windows", "wifi", "escoltar", "xarxa", "remot", "llar", "en línia", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**Resum:** Windows 10 té un servidor DLNA integrat. Activa'l a la configuració de Xarxa i ús compartit, després utilitza l'aplicació gratuïta **Evermusic** al teu iPhone per transmetre tota la teva biblioteca musical per Wi-Fi. No cal cap programari de servidor de tercers.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Portada" caption="Transmissió de música per DLNA a l'iPhone amb Windows 10 i Evermusic" width="800" >}}

DLNA (Digital Living Network Alliance) és una eina potent que et permet transmetre fàcilment diversos continguts multimèdia, inclosa la música, entre dispositius compatibles amb DLNA a la teva xarxa. La bona notícia és que Windows 10, i versions anteriors, inclouen una funció DLNA integrada, eliminant la necessitat de servidors multimèdia de tercers. Aquí t'expliquem com activar el servidor multimèdia DLNA a Windows 10 i gaudir de la transmissió de música al teu iPhone.

## Com activar el servidor multimèdia DLNA a Windows 10

1. Fes clic al botó 'Inici'.  
2. Selecciona la icona 'Configuració'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Configurar servidor" caption="Obre la configuració de Windows" width="500" >}}

3. A la pantalla 'Configuració de Windows', tria 'Xarxa i Internet'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Configuració de Windows" caption="Selecciona Xarxa i Internet" width="500" >}}

4. Sota 'Xarxa', selecciona 'Centre de xarxes i ús compartit'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Centre d'ús compartit" caption="Obre el Centre de xarxes i ús compartit" width="500" >}}

5. A la pantalla 'Centre de xarxes i ús compartit', fes clic a 'Canvia la configuració d'ús compartit avançat' al menú esquerre.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Configuració d'ús compartit avançat" caption="Canvia la configuració d'ús compartit avançat" width="500" >}}

6. A la pantalla 'Configuració d'ús compartit avançat', desplaça't fins a la secció 'Totes les xarxes' i expandeix-la fent clic a la fletxa.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Activar descobriment" caption="Expandeix la configuració de totes les xarxes" width="500" >}}

7. Fes clic a 'Activa la transmissió multimèdia' per activar el servidor DLNA.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Activar servidor" caption="Activa el servidor de transmissió multimèdia" width="500" >}}

8. Dona un nom a la teva biblioteca multimèdia i selecciona els dispositius autoritzats per accedir-hi.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Nom de la biblioteca multimèdia" caption="Posa nom a la teva biblioteca multimèdia DLNA" width="500" >}}

9. Fes clic a 'D'acord' per confirmar l'operació. Ara, les teves carpetes personals com Música, Imatges i Vídeos seran visibles per a qualsevol dispositiu de transmissió compatible amb UPnP.

## Com desactivar el servidor multimèdia DLNA a Windows 10

1. Fes clic a 'Inici' i escriu 'services' al camp de cerca.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Serveis de Windows" caption="Obre els Serveis de Windows" width="500" >}}

2. A la pantalla 'Serveis', desplaça't per trobar 'Windows Media Player Network Sharing Service'.  
3. Fes-hi doble clic i estableix el 'Tipus d'inici' a 'Manual'.  
4. Atura el servei fent clic al botó 'Atura'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="Aturar servei DLNA" caption="Desactiva el servei de compartició de xarxa DLNA" width="500" >}}

## Com reproduir música des del servidor DLNA a l'iPhone

1. Instal·la l'aplicació gratuïta **Evermusic** des de l'App Store:  
   [Aplicació Evermusic](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Obre la pestanya 'Connexions' i toca l'element 'Dispositius disponibles' a la secció 'Xarxa local'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Connexions Evermusic" caption="Evermusic: pantalla de Connexions" width="500" >}}

3. Espera uns segons mentre es carrega la llista de dispositius i toca el servidor Windows Media Player DLNA (p. ex., 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Dispositius disponibles" caption="Servidors DLNA disponibles a Evermusic" width="500" >}}

4. Veuràs una llista de carpetes disponibles al servidor multimèdia.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Carpetes Evermusic" caption="Navega per les carpetes compartides del servidor DLNA" width="500" >}}

5. Obre qualsevol carpeta que contingui fitxers d'àudio.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Contingut de la carpeta" caption="Mostra el contingut de les carpetes DLNA compartides" width="500" >}}

6. Toca qualsevol fitxer per iniciar el reproductor d'àudio.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Reproductor d'àudio" caption="Reprodueix fitxer d'àudio des de DLNA a Evermusic" width="500" >}}

7. Per millorar la teva experiència d'àudio, toca la icona 'Equalitzador' a prop de l'indicador de volum a la part inferior de la pantalla per activar l'equalitzador estil iPod amb un preamplificador.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Equalitzador" caption="Utilitza l'equalitzador integrat per a una reproducció millorada" width="500" >}}

## Conclusió

Amb el servidor multimèdia DLNA a Windows 10 i Evermusic al teu iPhone, pots gaudir d'una transmissió de música fluida des del teu ordinador al teu dispositiu mòbil. Adéu a les limitacions d'emmagatzematge i benvinguda la música sota demanda!

## Preguntes freqüents

{{% details title="Necessito instal·lar algun programari de servidor a Windows 10?" closed="true" %}}
No. Windows 10 inclou un servidor multimèdia DLNA integrat. Només cal activar la transmissió multimèdia a la configuració del Centre de xarxes i ús compartit. No cal cap programari de tercers.
{{% /details %}}

{{% details title="El meu iPhone ha d'estar a la mateixa xarxa Wi-Fi?" closed="true" %}}
Sí. La transmissió DLNA funciona a través de la teva xarxa local. Tant el teu PC amb Windows 10 com el teu iPhone han d'estar connectats a la mateixa xarxa Wi-Fi perquè Evermusic pugui descobrir el servidor DLNA.
{{% /details %}}

{{% details title="Quins formats d'àudio puc transmetre via DLNA?" closed="true" %}}
El servidor Windows DLNA comparteix fitxers de la carpeta Música independentment del format. Evermusic admet MP3, FLAC, AAC, WAV, OGG, AIFF i molts altres formats, de manera que pots reproduir pràcticament qualsevol fitxer d'àudio del servidor.
{{% /details %}}

{{% details title="Puc utilitzar Flacbox en lloc d'Evermusic?" closed="true" %}}
Sí. Flacbox també admet la navegació i reproducció DLNA/UPnP. Pots utilitzar qualsevol de les dues aplicacions per descobrir i reproduir música des del teu servidor Windows DLNA.
{{% /details %}}

{{% details title="La transmissió DLNA utilitza dades mòbils?" closed="true" %}}
No. DLNA funciona completament a la teva xarxa Wi-Fi local. No utilitza cap dada mòbil. No obstant això, ambdós dispositius han de romandre connectats a la mateixa xarxa durant la reproducció.
{{% /details %}}
