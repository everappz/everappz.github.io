---
title: "Evertag 4.2: noves connexions al núvol, opcions de l'editor d'etiquetes explicades"
date: 2026-05-09
description: "Evertag 4.2 afegeix connexions a Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP i NFS, refresca Wi-Fi Drive i actualitza la interfície per a Liquid Glass. Aquesta entrada també explica totes les opcions de l'editor d'etiquetes — incloses ID3v2.4 vs ID3v2.3, escalat de la coberta, etiquetes duplicades, modes de pujada al núvol i les opcions correctes per a Spotify i altres serveis de streaming."
keywords: ["Evertag 4.2", "actualització Evertag", "editor d'etiquetes ID3 iPhone", "ID3v2.4 vs ID3v2.3", "editar etiquetes FLAC iOS", "editar etiquetes MP3 iPhone", "editar coberta àlbum iOS", "editor d'etiquetes per a Spotify", "editor d'etiquetes Plex", "editor d'etiquetes Apple Music", "editor d'etiquetes al núvol Evertag", "editor d'etiquetes Internxt", "editor d'etiquetes Proton Drive", "editor d'etiquetes QNAP", "editor d'etiquetes Nextcloud", "editor d'etiquetes Amazon S3", "editor d'etiquetes SFTP iPhone", "editor d'etiquetes àudio FTP", "editor d'etiquetes NFS iPhone", "Wi-Fi Drive editor d'etiquetes", "duplicar etiquetes ID3", "escalat de coberta", "disseny Liquid Glass", "editor de metadades d'àudio iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Editor d'etiquetes", "ID3", "ID3v2.4", "ID3v2.3", "Etiquetes FLAC", "Etiquetes MP3", "Coberta d'àlbum", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Novetats"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**TL;DR:** [Evertag 4.2](/products/evertag) és una actualització important de l'editor d'etiquetes d'àudio per a iPhone, iPad i Mac. Hem eliminat errors clau d'edició d'etiquetes i hem afegit més de 6 noves connexions al núvol i a servidors — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, a més dels protocols **FTP**, **SFTP** i **NFS**. Wi-Fi Drive estrena interfície renovada, mode de selecció múltiple, una cua de pujada més intel·ligent i transferències més ràpides. Tota l'app s'ajusta al disseny **Liquid Glass**. Aquesta entrada també aprofundeix en les opcions de l'editor d'etiquetes d'Evertag — explicant **ID3v2.4 vs ID3v2.3**, **escalat de la coberta**, **etiquetes duplicades**, **modes de pujada al núvol**, **eliminació del fitxer baixat** i exactament quines opcions triar si prepares àudio per a **Spotify**, **Apple Music**, **Plex**, **Jellyfin** o qualsevol altre servei de streaming.

---

## Hola a tothom!

Una gran actualització d'Evertag és aquí. Hem eliminat errors clau d'edició d'etiquetes i hem afegit **més de 6 noves connexions al núvol i a servidors** perquè gestionar les metadades d'àudio sigui més fàcil que mai — tant si la teva biblioteca viu en un núvol amb foco en privacitat, en un NAS autoallotjat o en un servidor genèric FTP/SFTP/NFS.

[Descarrega Evertag 4.2 a l'App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) o actualitza des de la teva versió actual.

## Suport ampliat de núvol i servidors

Evertag es connecta ara nativament a una gamma més àmplia d'opcions de núvol i emmagatzematge autoallotjat. Pots editar etiquetes ID3, MP4, FLAC, OGG i APE en fitxers visquin on visquin.

### Emmagatzematge al núvol amb foco en privacitat: Internxt i Proton Drive

Si t'importen el xifratge d'extrem a extrem i l'emmagatzematge sense coneixement, dos dels noms més respectats en núvol privacy-first ja són natius a Evertag:

- **Internxt** — núvol espanyol de codi obert, amb xifratge post-quàntic i conforme amb el RGPD. Pla gratuït disponible.
- **Proton Drive** — emmagatzematge xifrat d'extrem a extrem dels creadors de Proton Mail i Proton VPN, amb seu a Suïssa. Pla gratuït disponible i plans de pagament per a biblioteques més grans.

Ara pots editar metadades directament sobre fitxers d'àudio guardats en qualsevol dels dos serveis — el fitxer es manté xifrat en trànsit i només les noves etiquetes es tornen a escriure.

### Solucions autoallotjades: QNAP, Nextcloud, Amazon S3

Per a usuaris que gestionen la seva pròpia infraestructura:

- **QNAP** — connexió API nativa als dispositius NAS de QNAP. Edita etiquetes en fitxers del teu QNAP via Wi-Fi local o accés remot.
- **Nextcloud** — connecta amb qualsevol instància de Nextcloud autoallotjada o gestionada.
- **Amazon S3** — apunta Evertag a qualsevol cubell S3 (o emmagatzematge compatible amb S3 com Backblaze B2, Wasabi, MinIO, Cloudflare R2) i edita metadades al lloc.

### Nous protocols de xarxa: FTP, SFTP, NFS

Evertag 4.2 afegeix tres protocols clàssics per a usuaris amb servidors propis, homelabs o NAS genèrics:

- **SFTP (SSH File Transfer Protocol)** — la resposta correcta per a **edició remota i segura d'etiquetes des del teu propi servidor**. SFTP funciona sobre SSH, així que tota la transferència (autenticació i dades d'àudio) està xifrada. Si tens un VPS, un servidor dedicat o una màquina Linux a casa amb accés SSH, pots editar etiquetes en fitxers remots sense exposar res més. Admet autenticació amb contrasenya i amb clau.
- **FTP** — l'estàndard històric de transferència d'arxius. Útil per a NAS domèstics antics que exposen FTP però no tenen integració nativa per API.
- **NFS (Network File System)** — el protocol de compartició de facto a Linux i a la majoria de NAS. Menys sobrecàrrega que SMB amb el mateix maquinari.

> **Consell:** SFTP és el protocol que vols per editar a distància per Internet obert. FTP i NFS són millors a la xarxa local — no els exposis a Internet excepte que els emboliquis amb una VPN.

## Millores de Wi-Fi Drive

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) és la funció integrada d'Evertag per **transferir fitxers d'àudio sense fils entre el teu ordinador i el teu iPhone o iPad — sense iTunes, sense cables i sense compte al núvol**. Ambdós dispositius han d'estar a la mateixa xarxa Wi-Fi.

A Evertag 4.2, Wi-Fi Drive estrena:

- **Interfície moderna i renovada** — més neta, més fàcil de llegir d'un cop d'ull i actualitzada per a Liquid Glass.
- **Mode de selecció múltiple** — tria diversos arxius o carpetes i actua-hi en bloc.
- **Cua de pujada més intel·ligent** — millor informació de progrés i resistència a errors de xarxa.
- **Velocitat i fiabilitat globals millorades** — transferències més ràpides per a biblioteques grans.

És la manera més ràpida de moure un lot d'arxius d'àudio de l'ordinador al telèfon, editar-ne les etiquetes i tornar-los — sense cap servei de tercers.

## Opcions de l'editor d'etiquetes: anàlisi a fons

Aquesta és la part que la majoria d'usuaris no llegeixen mai — i la part que decideix si les teves etiquetes funcionen a tot arreu o només en algunes apps. Obre Evertag i entra a la secció de **opcions de l'editor d'etiquetes d'àudio**. Aquí tens què fa cada opció i quina triar segons el que vulguis aconseguir.

### Escalat de la coberta

Quan guardes la coberta de l'àlbum dins d'un fitxer d'àudio, Evertag pot redimensionar la imatge abans d'incrustar-la. Les opcions són:

- **Petit** — menor impacte en la mida del fitxer, qualitat d'imatge més baixa.
- **Mitjà** — opció equilibrada per a la majoria d'usuaris.
- **Gran** — alta qualitat, ideal per a reproductors amb pantalles grans i CarPlay.
- **Extra gran** — qualitat molt alta, augment notable de la mida del fitxer.
- **Original (Desactivat)** — incrusta la coberta a la resolució original. **Sense escalat.**

**Per què importa:**

- **Més qualitat = arxiu més gran.** Una coberta de 3.000 × 3.000 píxels pot afegir diversos MB a cada pista. Multiplicat per tot un àlbum, el cost en disc s'acumula ràpid.
- **Alguns reproductors no manegen bé imatges incrustades molt grans.** Dispositius més antics, certs sistemes de cotxe i alguns reproductors d'escriptori heretats poden encallar-se amb cobertes superiors a ~1.500 px o no mostrar-les.
- **Per a la majoria de fluxos al núvol i streaming**, **Mitjà** o **Gran** és el punt òptim. Usa **Original** només quan necessites qualitat d'arxiu o prepares fitxers per a un reproductor en què confies.

> L'opció **Original** forma part de la millora de personalització premium d'Evertag. Les mides estàndard (Petit/Mitjà/Gran/Extra gran) són gratuïtes.

### Opcions de desat d'etiquetes: ID3v2.4 vs ID3v2.3

És l'ajustament més important per a la compatibilitat. ID3v2 és el format de metadades dins els fitxers MP3. Hi ha dues versions molt utilitzades, i es diferencien en detalls subtils però importants.

#### ID3v2.4

- Més recent, admet **codificació de text UTF-8** — manipulació correcta d'escriptures no llatines (xinès, rus, japonès, àrab, hebreu, etc.).
- Més tipus de marc (volum relatiu, presets d'equalitzador, etc.).
- **Recomanada per a reproductors moderns** que la suporten.

#### ID3v2.3

- Més antiga però **la versió d'ID3 amb major compatibilitat universal**.
- No admet UTF-8 directament (utilitza UTF-16 per a text Unicode).
- **Recomanada quan necessites màxima compatibilitat** amb reproductors antics, equips de cotxe i certes apps d'escriptori.

#### Quan activar ID3v2.4 a Evertag

- Utilitzes **reproductors d'àudio moderns** com Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (versions actuals) o reproductors Android moderns. ✅ **Activa ID3v2.4.**
- La teva biblioteca conté **caràcters no llatins** (xinès, coreà, japonès, rus, àrab, grec, hebreu). ✅ **Activa ID3v2.4** — UTF-8 els maneja amb molta més neteja.

#### Quan desactivar ID3v2.4 a Evertag (utilitza ID3v2.3)

- Prepares fitxers per a un **equip de cotxe o capçal antic** que no llegeix etiquetes v2.4.
- Veus **text il·legible o etiquetes buides** en algunes apps després d'editar — això és un senyal clar que allà no s'admet v2.4. Torna a v2.3.
- Apuntes a **reproductors d'escriptori heretats** o reproductors portàtils antics (primers iPods, certs reproductors MP3 de 2000–2010).

> **Regla pràctica:** si les teves etiquetes es veuen correctament a tot arreu amb v2.4, deixa-la activada. Si fins i tot un reproductor important mostra caràcters erronis, espais en blanc o no llegeix les etiquetes, desactiva v2.4 i torna a desar.

#### Etiquetes duplicades

Quan actives **Etiquetes duplicades**, Evertag escriu els camps de metadades comuns (títol, artista, àlbum, etc.) a **les seccions ID3v1 i ID3v2** del fitxer. Això millora la compatibilitat amb reproductors molt antics que només llegeixen ID3v1 (l'etiqueta original de 128 bytes al final del fitxer).

- **La majoria d'usuaris no la necessiten.** Els reproductors moderns llegeixen ID3v2 primer.
- **Activa-la només si** treballes amb maquinari vintage o programari específic que ignora ID3v2.

### Actualitzar fitxers en línia: com gestiona Evertag les edicions al núvol

Quan edites etiquetes en un fitxer guardat en un núvol connectat (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP, etc.), Evertag ha de tornar a pujar el fitxer modificat. Tu controles com:

- **Mostrar missatge de confirmació** *(predeterminat, recomanat)* — Evertag pregunta abans de pujar. Millor per a usuaris cautelosos i biblioteques compartides.
- **Actualitzar automàticament les metadades del fitxer** — puja en silenci després de cada edició. Millor per a usuaris sols amb connexions ràpides i fiables que editen molt.
- **No actualitzar les metadades del fitxer** — Evertag edita només la còpia local. Útil per previsualitzar canvis sense enviar-los al núvol.

### Editar fitxers en línia: neteja del fitxer local

Per editar un fitxer remot, Evertag el descarrega primer al dispositiu. Després d'editar, tries què passa amb aquesta còpia local:

- **Eliminar sempre el fitxer baixat** — Evertag esborra el fitxer temporal després d'editar. **Recomanat** si vas just d'emmagatzematge o treballes amb fitxers d'altri.
- **No eliminar el fitxer baixat** — conserva el fitxer editat al teu dispositiu. Útil si vols una còpia offline i una còpia al núvol actualitzada.

### Botons a la pantalla principal

La pantalla principal de l'editor d'etiquetes d'Evertag pot mostrar o amagar botons per a operacions individuals. Activa només els que realment utilitzes per mantenir la interfície enfocada:

- **Cercar etiquetes d'àudio automàticament** — troba metadades que faltin en línia a partir de l'empremta d'àudio del fitxer.
- **Cercar etiquetes d'àudio manualment** — cerca per títol/artista quan la cerca automàtica falla.
- **Cercar coberta de l'àlbum** — troba i incrusta cobertes d'alta qualitat.
- **Desar coberta de l'àlbum** — exporta la coberta incrustada a la teva fototeca o arxius.
- **Normalitzar codificació** — corregeix text no llatí mal codificat per encodings antics (molt útil per a pistes en ciríl·lic, xinès i japonès ripades amb programari heretat).
- **Eliminar etiquetes d'àudio** — esborra totes les etiquetes del fitxer. Útil abans d'una nova etiqueta neta.

### Mostra etiquetes ampliades

Activa això per mostrar tot el conjunt de camps de metadades més enllà del bàsic títol/artista/àlbum/any — incloent BPM, director, artista original, estat d'ànim, copyright, codificador, comentaris, lletres i més. Funció per a usuaris avançats; la majoria dels casuals no la necessita.

### Editar fitxers simultàniament

Activat, Evertag et permet editar metadades a **múltiples fitxers seleccionats alhora** — establir el mateix album artist, any o gènere per a tot un àlbum en una sola operació. És la manera més ràpida de posar ordre en una biblioteca gran i desordenada.

## Editar etiquetes per a Spotify, Apple Music i plataformes de streaming

Una pregunta habitual: «vaig editar les meves etiquetes a Evertag, vaig pujar els fitxers i el servei de streaming mostra metadades equivocades. Què passa?».

Resposta curta: **els serveis de streaming no sempre respecten les teves etiquetes locals**. Apple Music i Spotify tenen les seves pròpies bases de dades internes — quan reconeixen una pista, sobreescriuen les metadades mostrades amb les seves. Però per a **fitxers pujats**, els teus fitxers locals (la funció «Biblioteca» d'Apple Music, els Fitxers locals de Spotify) i les **pujades de distribuïdor a plataformes de streaming**, les teves etiquetes sí que importen. Aquí tens com configurar Evertag en cada cas:

### Preparar fitxers per a Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music maneja UTF-8 correctament.
- **Coberta de l'àlbum: Gran** — les apps d'Apple mostren bé les cobertes grans; Original és excessiu.
- **Etiquetes duplicades: OFF** — no són necessàries.
- Assegura't que **Album Artist** estigui ben omplert — Apple Music l'usa per a l'agrupació.

### Preparar fitxers per als Fitxers locals de Spotify

Els Fitxers locals de Spotify només mostren fitxers ben etiquetats. Les etiquetes que Spotify llegeix són limitades.

- **ID3v2.4: ON** en la majoria dels casos. Si una pista no apareix correctament a Spotify després d'editar, **prova a desar amb ID3v2.4: OFF** (és a dir, com a ID3v2.3) — l'analitzador de Spotify ha estat històricament conservador amb v2.4.
- **Coberta de l'àlbum: Mitjana o Gran** — Spotify la redimensiona de totes maneres.
- Omple com a mínim **Títol**, **Artista**, **Àlbum** i **Número de pista**.

### Preparar fitxers per a pujada per distribuïdor (DistroKid, TuneCore, CD Baby, etc.)

Si ets artista i pugis el teu propi treball a plataformes de streaming, el teu distribuïdor sol llegir les etiquetes però també demana metadades a la seva interfície. En qualsevol cas:

- **ID3v2.3** sol ser l'opció més segura — moltes canonades de distribuïdor es van construir fa anys i prefereixen el format antic.
- Incrusta coberta **Gran** (la majoria de distribuïdors exigeixen ≥ 1.400 × 1.400 px — consulta les seves directrius).
- No t'apoyis en etiquetes ampliades — els distribuïdors només llegeixen els camps principals.

### Preparar fitxers per a Plex, Jellyfin, Navidrome, Subsonic, Emby

Aquests servidors multimèdia autoallotjats són molt tolerants. Llegeixen tant v2.3 com v2.4 sense problemes i manegen UTF-8 bé.

- **ID3v2.4: ON** està bé.
- **Coberta de l'àlbum: Gran** o **Extra gran** — aquests servidors envien la coberta a clients mòbils i pantalles CarPlay, així que la qualitat importa.
- **Album Artist** molt recomanat — és el que Plex/Jellyfin usen per agrupar àlbums per artista correctament.

### Preparar fitxers per a equips de cotxe i maquinari antic

- **ID3v2.4: OFF** (utilitza ID3v2.3) — els capçals antics sovint no admeten v2.4.
- **Coberta de l'àlbum: Mitjana** — moltes pantalles de cotxe s'encalmen amb cobertes grans incrustades.
- **Etiquetes duplicades: ON** — alguns equips de cotxe antics només llegeixen el reserva ID3v1.

## Altres millores

### Disseny Liquid Glass

La interfície d'Evertag 4.2 s'ajusta al nou material **Liquid Glass** d'Apple a tota l'app — superfícies translúcides, animacions més suaus i controls refinats que encaixen de manera natural amb iOS, iPadOS i macOS.

### Biblioteques de connexió actualitzades

Hem refrescat les biblioteques internes que Evertag utilitza per parlar amb **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** i altres serveis. Resultat: menys errors de connexió en casos límit, millor compatibilitat amb versions noves de servidor i major fiabilitat en editar etiquetes en fitxers remots.

### Correccions de traducció i localització

Múltiples correccions d'idioma a la interfície a partir del feedback directe dels usuaris. Millor encaix del text en botons petits en diversos idiomes.

### Petites millores inspirades en els teus comentaris

Moltes millories menors basades en ressenyes de l'App Store i correus a support@everappz.com. Llegim cada missatge.

## Aconsegueix Evertag 4.2

[**Descarrega Evertag a l'App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) o actualitza des de l'App Store. Evertag és una descàrrega gratuïta amb millores opcionals dins de l'app per a funcions avançades. Les noves connexions al núvol, els protocols de xarxa, les millores de Wi-Fi Drive i la interfície Liquid Glass formen part de l'actualització base.

Si t'agrada l'app, deixa una valoració a l'App Store — ens ajuda molt. Tens comentaris o un problema? Escriu-nos a **support@everappz.com**. Llegim cada missatge.

## Preguntes freqüents

{{% details title="Què hi ha de nou a Evertag 4.2?" closed="true" %}}
Evertag 4.2 afegeix més de 6 noves connexions al núvol i a servidors (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), un Wi-Fi Drive renovat amb selecció múltiple i cua de pujada més intel·ligent, actualitzacions de la interfície Liquid Glass, biblioteques de connexió actualitzades, correccions clau en l'edició d'etiquetes i millores en la traducció.
{{% /details %}}

{{% details title="He d'usar ID3v2.4 o ID3v2.3 a Evertag?" closed="true" %}}
Utilitza **ID3v2.4** per a reproductors moderns (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, apps Android modernes) i per a biblioteques amb caràcters no llatins — el suport UTF-8 implica etiquetes més netes en xinès, coreà, japonès, rus, àrab i hebreu. Utilitza **ID3v2.3** si les teves etiquetes es veuen incorrectament en algunes apps, si apuntes a equips de cotxe antics o si una canonada de distribuïdor de streaming rebutja v2.4. Sempre pots canviar i tornar a desar.
{{% /details %}}

{{% details title="Per què les meves etiquetes són incorrectes a Spotify després d'editar?" closed="true" %}}
Spotify mostra principalment metadades del seu propi catàleg — les teves etiquetes locals només s'usen per a «Local Files» o per a contingut que has pujat com a artista. Si etiquetes fitxers per a Fitxers locals de Spotify i no apareixen correctament, prova a desactivar ID3v2.4 a Evertag i desar com a ID3v2.3 — l'analitzador de Spotify ha estat històricament conservador amb v2.4.
{{% /details %}}

{{% details title="Quina mida de coberta hauria de triar a Evertag?" closed="true" %}}
Per a la majoria d'usuaris: **Gran**. Es veu fantàstic en telèfons, iPads, Macs i pantalles de cotxe modernes sense inflar massa els fitxers. Utilitza **Mitjana** si tens una biblioteca enorme i vols estalviar disc. Utilitza **Original** (sense escalat) només per a màsters d'arxiu o quan necessites màxima qualitat — però tingues en compte que alguns reproductors antics tenen problemes amb cobertes incrustades molt grans. **Original** forma part de la millora de personalització premium d'Evertag.
{{% /details %}}

{{% details title="Les cobertes més grans faran els meus fitxers més grans?" closed="true" %}}
Sí. Incrustar una coberta de 3.000 × 3.000 px pot afegir diversos megabytes a un sol fitxer d'àudio. Sobre una biblioteca de 1.000 pistes, això suma gigabytes. Si vas just d'emmagatzematge, utilitza Mitjana o Gran; si reprodueixes des d'un NAS on la mida no importa, Extra gran o Original van bé.
{{% /details %}}

{{% details title="Què són les etiquetes duplicades i hauria d'activar-les?" closed="true" %}}
Les etiquetes duplicades escriuen les metadades centrals a les seccions ID3v1 (llegat de 128 bytes) i ID3v2 (moderna) del fitxer. Activa-les només si apuntes a reproductors molt antics o maquinari que llegeix ID3v1. Per a tot allò modern (smartphones, ordinadors, equips de cotxe recents), deixa-les desactivades.
{{% /details %}}

{{% details title="Evertag edita les etiquetes directament en fitxers al núvol?" closed="true" %}}
Sí. Connecta't al teu núvol (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, etc.) o via FTP/SFTP/NFS, obre un fitxer i edita les etiquetes com si fos local. Evertag descarrega el fitxer, aplica els teus canvis i torna a pujar la versió actualitzada. Pots triar entre els modes «Preguntar sempre», «Pujar automàticament» o «No pujar» a la configuració.
{{% /details %}}

{{% details title="Puc editar etiquetes FLAC a iPhone amb Evertag?" closed="true" %}}
Sí. Evertag admet FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE i altres formats importants amb suport complet de lectura/escriptura d'etiquetes, incloent coberta incrustada.
{{% /details %}}

{{% details title="Com edito etiquetes de manera segura al meu servidor domèstic amb SFTP?" closed="true" %}}
Obre Evertag, ves a Connexions, tria SFTP i introdueix el nom d'amfitrió o IP del servidor, el port (normalment 22), el nom d'usuari i, o bé una contrasenya, o una clau SSH privada. Evertag mostrarà les teves carpetes remotes i editarà les etiquetes directament amb xifratge d'extrem a extrem sobre SSH.
{{% /details %}}

{{% details title="Puc editar etiquetes en diversos fitxers alhora?" closed="true" %}}
Sí. Activa **Editar fitxers simultàniament** a la configuració. Selecciona diversos fitxers, obre l'editor d'etiquetes i qualsevol camp que canviïs s'aplicarà a tots els fitxers seleccionats. És la manera més ràpida de fixar el mateix album artist, any o gènere en tot un àlbum.
{{% /details %}}

{{% details title="L'actualització a Evertag 4.2 és gratuïta?" closed="true" %}}
Sí. Evertag és una descàrrega gratuïta a l'App Store i la 4.2 és una actualització gratis per a tots els usuaris actuals. Les noves integracions al núvol, les millores de Wi-Fi Drive i la interfície Liquid Glass formen part de l'actualització base.
{{% /details %}}

{{% details title="En quins dispositius està disponible Evertag 4.2?" closed="true" %}}
Evertag 4.2 funciona a iPhone, iPad i Mac. La sincronització amb iCloud Drive manté els teus ajustaments d'edició d'etiquetes consistents entre dispositius.
{{% /details %}}
