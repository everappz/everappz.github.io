---
title: "Exporta el teu historial d'escolta complet d'Evermusic i Flacbox a Last.fm"
date: 2024-01-30
description: "Aprèn a exportar el teu historial de música d'Evermusic i Flacbox i pujar-lo a Last.fm utilitzant fitxers CSV i l'eina Last.fm Scrubbler per a Windows."
keywords: ["evermusic", "flacbox", "lastfm", "historial de música", "scrobbling", "exportar pistes", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "recents", "lastfm", "exportar", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Resum:** Exporta el teu historial d'escolta d'Evermusic o Flacbox com a fitxer CSV, després puja'l a Last.fm utilitzant l'eina gratuïta Last.fm-Scrubbler-WPF a Windows. L'scrobbling automàtic també està disponible de forma nativa a ambdues aplicacions.

**Actualització:** L'scrobbling automàtic ja està disponible! Més informació aquí: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

L'scrobbling és una manera senzilla de desar automàticament detalls bàsics com el títol i l'artista de la cançó que estàs reproduint en un servei en línia. Més tard, pots revisar el teu historial d'escolta.

[Last.fm](https://www.last.fm/home), impulsat per un sistema de recomanació musical anomenat Audioscrobbler, ofereix aquest servei de forma gratuïta. Crea un perfil detallat del teu gust musical enregistrant les pistes que escoltes, ja siguin d'estacions de ràdio per internet, del teu ordinador o de diversos dispositius de música portàtils. Pots visitar el lloc web més tard per rebre recomanacions de nous artistes o àlbums que s'adaptin al teu gust musical.

Pots pujar el teu historial d'escolta a [Last.fm](http://Last.fm) des de les aplicacions Evermusic i Flacbox utilitzant una eina gratuïta, i et guiarem a través de com fer-ho.

Obre la secció 'Biblioteca de música' de l'aplicació i desplaça't fins a la secció 'Accés ràpid'. Toca l'element del menú 'Recents'.

![pantalla de la biblioteca de música](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

A la pantalla 'Recents' toca el botó 'Més' a la cantonada superior dreta per activar el menú 'Més accions'. Toca l'element del menú 'Exportar llista de cançons'.

![pantalla de recents](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

A la pantalla 'Selecciona el format del fitxer' tens la possibilitat de seleccionar el format del fitxer de destinació. Opcions disponibles - CSV, TXT, M3U.

![pantalla de selecció de format de fitxer](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Significa Valors Separats per Comes, perfecte per organitzar les teves dades en un format de taula ordenat. Al fitxer de destinació, trobaràs paràmetres com Nom de l'Artista, Nom de l'Àlbum, Nom de la Pista, Marca de Temps (l'hora en què vas escoltar les pistes), Nom de l'Artista de l'Àlbum i Durada de la Pista.

TXT: Aquí parlem d'un fitxer de text pla. És simple i directe, amb paràmetres que inclouen Nom de l'Artista, Nom de l'Àlbum, Nom de la Pista i Durada.

M3U: Aquest format és essencialment el referent per crear llistes de reproducció. És genial perquè pots exportar la teva llista de cançons i gaudir de les teves pistes en qualsevol dispositiu, fins i tot si no tens els fitxers originals (sempre que seleccionis l'opció d'URL absolut per als fitxers multimèdia). Al fitxer de sortida, trobaràs paràmetres com Durada, Nom de l'Artista, Nom de la Pista i Ubicació del Fitxer Multimèdia.

Per a la nostra tasca, seleccionar CSV és el camí a seguir. Utilitzarem aquest fitxer amb el programari gratuït Last.fm-Scrubbler-WPF per pujar el nostre historial d'escolta al servei [Last.fm](http://Last.fm). Simplement tria CSV i prem el botó 'Exportar'.

![pantalla d'exportació completada](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Després de completar l'exportació, simplement toca el botó 'Mostrar fitxer', i l'aplicació revelarà el fitxer creat a la teva carpeta de documents. Després, toca el botó 'Més accions' al costat del nom del fitxer i selecciona l'opció 'Obrir amb' del menú. El nostre següent pas és copiar el fitxer exportat al teu ordinador d'escriptori. Pots fer-ho fàcilment seleccionant l'opció AirDrop del menú 'Obrir amb'.

![més accions per al fitxer exportat](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

A continuació, utilitzarem un client [Last.FM](http://Last.FM) gratuït de codi obert que només està disponible a la plataforma Windows. Aquest client et permet actualitzar eficientment el teu historial d'escolta a [Last.FM](http://Last.FM) utilitzant el fitxer CSV que acabem d'exportar.

Ara, si no estàs utilitzant un ordinador amb Windows, no et preocupis. Pots accedir a aquest client instal·lant VirtualBox al teu Mac i utilitzant el fitxer d'imatge oficial de l'entorn de desenvolupament de Windows.

Aquí tens el que has de fer:

- Instal·la VirtualBox des del següent enllaç: [Descarregar VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Descarrega i instal·la l'entorn de desenvolupament de Windows des d'aquest enllaç: [Entorn de desenvolupament de Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Al teu ordinador amb Windows (o l'aplicació VirtualBox amb la imatge de desenvolupament de Windows) descarrega i instal·la [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - programari gratuït de codi obert disponible a GitHub. Hem provat la versió 1.28 que pots descarregar aquí: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![pàgina de descàrrega de Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

A la secció 'Assets' toca [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) per descarregar l'arxiu d'instal·lació. Descomprimeix el fitxer descarregat i obre la carpeta descomprimida.

- IMPORTANT

Aquesta aplicació encara està en fase beta. Els creadors de l'aplicació no han fet moltes proves. Recomanen provar l'scrobbling a un compte de prova primer i veure si les coses que vols fer scrobble funcionen correctament. Especialment si fas scrobble de moltes pistes alhora. Si us plau, tingues cura amb els teus comptes.

Executa Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

A la pantalla principal de l'aplicació, simplement toca 'No connectat', situat a la cantonada inferior esquerra, per activar la pantalla 'Afegir compte'.

![pantalla d'afegir compte](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Introdueix les teves credencials d'inici de sessió.

![pantalla d'introducció de credencials](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Toca el botó 'Iniciar sessió' per afegir el teu compte.

![Toca el botó Iniciar sessió per afegir el teu compte.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Obre la pestanya 'File Parse Scrobbler' per començar a importar el fitxer CSV des de l'aplicació Evermusic.

![Obre la pestanya File Parse Scrobbler per començar a importar el fitxer CSV des de l'aplicació Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Tria 'Parser: CSV' i toca el botó 'Configuració'.

A la següent pantalla, pots triar l'ordre dels paràmetres del teu fitxer CSV.

Els camps individuals poden estar tancats entre cometes i HAN d'estar tancats entre cometes si el camp conté qualsevol dels delimitadors establerts. Per exemple:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Així que deixa totes les configuracions per defecte, l'únic que has de canviar és activar la casella de selecció al camp 'Has Fields Enclosed In Quotes'.

Toca 'Desar i tancar' per aplicar els canvis.

![triar l'ordre dels paràmetres del teu fitxer CSV.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

L'scrobbling d'anàlisi de fitxers té dos modes. Es poden canviar amb el ComboBox 'Scrobbling Mode'.

Mode Normal: En aquest mode, les pistes es faran scrobble amb la marca de temps de l'scrobble analitzat. Només els scrobbles més recents de 14 dies es poden fer scrobble.

Mode d'Importació: En aquest mode, les pistes es faran scrobble amb la marca de temps calculada a partir del 'Temps de Finalització' i la durada seleccionada entre cada pista. Això permet fer scrobble de les pistes fins i tot si la marca de temps de l'scrobble analitzat és més antiga de 14 dies. Per tant, la primera pista (la de dalt) del fitxer CSV es farà scrobble amb el 'Temps de Finalització'.

Tria un fitxer CSV prèviament generat des de l'aplicació Evermusic al camp 'File:' i toca 'Parse'. En alguns casos, pots veure una alerta d'error dient que alguns scrobbles no s'han pogut analitzar. Està bé si tens algunes pistes sense metadades completes com el Nom de l'Artista.

![alguns scrobbles no s'han pogut analitzar](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Toca el botó 'Seleccionar tot' per seleccionar totes les pistes analitzades.

![Toca el botó Seleccionar tot per seleccionar totes les pistes analitzades.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Toca el botó 'Previsualitzar' per comprovar tots els canvis que es publicaran al servidor.

![Toca el botó Previsualitzar per comprovar tots els canvis que es publicaran al servidor.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Toca el botó 'Scrobble' per pujar tots els canvis al servidor.

![Toca el botó Scrobble per pujar tots els canvis al servidor.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Anteriorment, Last.fm-Scrubbler-WPF no tenia un límit d'scrobbles per dia. Això ha canviat ja que algunes persones van utilitzar Scrubbler per fer scrobble de tantes pistes que va causar problemes a la pàgina de Last.fm. El límit d'scrobbling és actualment de 2800 scrobbles per dia. Quan intentes fer scrobble de més, rebràs un missatge d'error. Hi ha plans per afegir una 'cua d'scrobbling', de manera que si necessites fer scrobble de més de 2800 pistes, s'afegiran a una cua i es faran scrobble automàticament després d'un temps. Pots comprovar quants scrobbles et queden a la vista de selecció d'usuari.

Un cop tots els registres s'han pujat amb èxit al servidor, veuràs un missatge a la part inferior de la finestra de l'aplicació confirmant: 'Scrobble de les pistes seleccionades completat amb èxit.'

![Scrobble de les pistes seleccionades completat amb èxit.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Ara pots obrir el teu perfil a la pàgina de [Last.fm](http://Last.fm) i comprovar tots els canvis.

![el teu perfil a la pàgina de Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Preguntes freqüents

{{% details title="Puc fer scrobbling automàticament sense exportar fitxers CSV?" closed="true" %}}
Sí. Tant Evermusic com Flacbox ara admeten l'scrobbling automàtic a Last.fm. Consulta la guia: [Com fer scrobble a Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Què passa si el meu CSV té pistes de més de 14 dies?" closed="true" %}}
Utilitza el Mode d'Importació a Last.fm-Scrubbler-WPF. Recalcula les marques de temps a partir del Temps de Finalització, permetent-te fer scrobble de les pistes independentment de la seva data original.
{{% /details %}}

{{% details title="No tinc un ordinador amb Windows. Puc utilitzar Last.fm-Scrubbler?" closed="true" %}}
Sí. Instal·la VirtualBox al teu Mac i descarrega la imatge gratuïta de l'entorn de desenvolupament de Windows de Microsoft. Executa Last.fm-Scrubbler-WPF dins de la màquina virtual.
{{% /details %}}

{{% details title="Per què no s'analitzen alguns scrobbles?" closed="true" %}}
Les pistes que no tenen metadades essencials (com el nom de l'artista) no es poden analitzar. Això és esperat i no afecta les altres pistes del fitxer.
{{% /details %}}

{{% details title="Hi ha un límit diari d'scrobbling?" closed="true" %}}
Sí. Last.fm-Scrubbler-WPF permet fins a 2.800 scrobbles per dia. Si necessites fer-ne més, divideix el procés en diversos dies.
{{% /details %}}
