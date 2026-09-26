---
title: "Sådan afspiller du FLAC-musik (tabsfri) på min iPhone"
date: 2024-01-29
lastmod: 2026-09-26
description: "Sådan afspiller du FLAC på iPhone og iPad i 2026 med Flacbox, en hi-res-afspiller med over 120 formater, output op til 384 kHz, understøttelse af USB DAC, en 10-bånds equalizer, BASS-lydmotoren, effekter i realtid som rumklang og forsinkelse, en DSP-processor og en musikvisualizer med 500 forudindstillinger. Stream fra skyen eller NAS og afspil offline."
keywords: ["sådan afspiller du flac på iphone", "flac-afspiller iphone", "flac", "iphone", "tabsfri", "hi-res-lyd", "dsd-afspiller ios", "usb dac iphone", "384khz", "musik", "flacbox", "stream", "offline", "equalizer", "dsp", "musikvisualizer", "bass-motor"]
tags: ["musik", "sky", "afspiller", "downloader", "equalizer", "tabsfri", "hi-res", "offline", "FLAC", "DSD", "DAC", "streamer", "visualizer", "DSP"]
readingTime: 8
---

{{< author-byline >}}


**Kort sagt:** For at afspille FLAC på en iPhone har du brug for en tredjepartsafspiller, fordi Apples Musik-app ikke understøtter FLAC. Installer [Flacbox](/products/flacbox) (det er gratis), og overfør derefter enten dine filer via Wi-Fi Drive eller USB, eller tilslut dit skylager eller NAS. Dit FLAC-bibliotek afspilles i fuld kvalitet, op til 384 kHz og 32-bit via en USB DAC. Flacbox afspiller også mere end 120 formater, herunder FLAC, DSD, ALAC, APE, WAV, OGG og OPUS, og den tilføjer en 10-bånds equalizer, den professionelle BASS-lydmotor med effekter i realtid, en DSP-processor og en musikvisualizer i fuld skærm.

[{{< figure src="/docs/howto/how-to-play-flac-music-on-iphone/Flacbox_Icon-App-1024x1024.webp" alt="Flacbox Icon - FLAC music player and downloader" width="160" >}}](/products/flacbox)

## Hvorfor afspiller min iPhone ikke FLAC indbygget?

Apple har sit eget tabsfrie format kaldet ALAC (Apple Lossless), og Musik-appen er bygget op omkring det i stedet for FLAC. Siden iOS 11 kan Filer-appen forhåndsvise en enkelt FLAC-fil, men den har intet musikbibliotek, ingen playlister, ingen kø, ingen equalizer og ingen skystreaming. Det er en filviser, ikke en musikafspiller.

Så du har to reelle muligheder:

1. Afspil FLAC med en afspiller-app, så dine filer forbliver præcis som de er. Det er den, vi anbefaler.
2. Konverter FLAC til ALAC, hvilket er tabsfrit til tabsfrit, og synkroniser derefter med Musik-appen.

Hvis du har en rigtig FLAC-samling, er den første mulighed bedre. Du undgår et duplikeret bibliotek, du sparer konverteringstiden, og dine mapper og hi-res-kvalitet forbliver urørte. Flacbox er bygget netop til dette.

## Mulighed 1: Afspil FLAC med Flacbox

Flacbox er en hi-res-musikafspiller til iPhone, iPad og Mac. Den forvandler dit skylager, NAS eller din computer til dit eget private musikbibliotek, uden konvertering og uden abonnement.

### Trin 1. Installer Flacbox

Flacbox er en gratis download og kører på iPhone, iPad og Mac.

{{< app-details product="flacbox" >}}

### Trin 2. Få dine FLAC-filer ind

Vælg den måde, der er nemmest for dig:

- **Wi-Fi Drive** — åbn Forbindelser, derefter Computer, derefter Connect using Wi-Fi, og træk filer ind fra en hvilken som helst desktopbrowser. Se [Wi-Fi Drive-guiden](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).
- **Skylager** — tilslut iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, pCloud, Proton Drive og 20 flere, og stream derefter direkte fra skyen.
- **NAS eller computer** — opret forbindelse via SMB, WebDAV, DLNA, FTP, SFTP eller NFS (Synology, QNAP, WD My Cloud, Time Capsule eller enhver Samba-deling). Den fulde liste findes i [Forbindelser-guiden](/docs/guide/flacbox/flacbox-guide-connections).
- **USB-flashdrev** — tilslut en SanDisk iXpand eller en hvilken som helst ekstern læser og afspil [direkte fra drevet](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it), uden at importere.
- **Fildeling via iTunes eller Finder** — via et Lightning- eller USB-C-kabel.

### Trin 3. Tryk på Afspil

Dine numre vises i biblioteket med tags og albumcovers læst fra selve filerne, grupperet efter Album, Kunstner, Genre og Komponist. Hvert nummer viser sit præcise codec og opløsning, for eksempel FLAC, 96 kHz, 24-bit.

## Hi-res-output, USB DAC og flerkanals

Flacbox er bygget til folk, der går op i lydkvalitet, ikke bare afslappet afspilning:

- **Samplingsfrekvens** — afspiller fra 8 kHz op til 384 kHz, med flerkanals output fra 1 til 7 kanaler (op til 5.1 og ITU BS.775-1).
- **Understøttelse af USB DAC** — alt over 48 kHz afspilles i sin sande opløsning via en USB DAC. Via iPhones eget output resampler iOS lyden, som det gør for alle apps, så en DAC er måden at få bit-perfekt hi-res.
- **Justerbart output** — indstil samplingsfrekvens, kanalantal og IO-buffervarighed (omkring 5 ms for hi-res med lav latenstid) i Indstillinger, derefter Audio Player.
- **Toneleje og hastighed** — fin tonelejekorrektion, plus afspilningshastighed fra 0.02× til 3.00×.

## Afspiller mere end 120 formater, ikke kun FLAC

Ved siden af FLAC medfølger FFmpeg i Flacbox, så den kan afspille formater, som iOS ikke kan åbne på egen hånd. Du behøver ikke først at konvertere eller rydde op i et blandet bibliotek:

- **Tabsfrit og hi-res** — FLAC, ALAC, WAV, AIFF, APE, WV (WavPack) og DSD (DSF og DFF, herunder DSD64, DSD128 og DSD256).
- **Tabsbehæftet** — MP3, AAC, M4A, OGG, OPUS, WMA, MPC og mere.
- **Tracker- og MOD-musik** — klassiske chiptune- og demoscene-filer som MOD, XM, IT, S3M, MTM, UMX og MO3, som de fleste afspillere ikke kan åbne.

Det er mere end 120 formater i alt, hvilket dækker stort set alt i en moderne musiksamling.

## Tre lydmotorer, herunder BASS-motoren

Du kan vælge afspilningsmotoren i Indstillinger, derefter Audio Player, derefter Audio Codec:

- **System Codec + FFmpeg** — maksimal kompatibilitet og stabilitet.
- **FFmpeg** — tvinger FFmpeg-stien, hvilket låser op for tonelejekorrektion og en tilpasset output-samplingsfrekvens.
- **BASS™-motoren** — den professionelle afspilningskerne, der blev tilføjet i [Flacbox 7.6](/blog/flacbox-7-6-bass-audio-engine-effects-dsp-music-visualizer). Den låser op for lydeffekter i realtid, DSP-processoren, musikvisualizeren, tracker- og MOD-afspilning og resampling af høj kvalitet. Den tilføjer også uafhængig tonelejekontrol (±60 semitones) og tempokontrol (0.1× til 4×).

## 10-bånds equalizer, basforstærkning og forforstærker

Flacbox indeholder en 10-bånds grafisk equalizer med forudindstillinger i iPod-stil som Acoustic, Bass Booster, Rock, Pop, Jazz, Classical og Dance. Der er en forforstærker til at løfte stille numre uden clipping, og du kan gemme dine egne forudindstillinger. Tilpas den til in-ear-monitorer, en HomePod eller et bilstereoanlæg. For en fuld gennemgang, se [equalizer-guiden](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audio Player equalizer" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Lydeffekter i realtid

Når BASS-motoren er slået til, får du elleve effekter i realtid, som du kan stable og justere, mens musikken spiller. Intet genkodes, og at slå en effekt fra bringer den oprindelige lyd tilbage med det samme:

- **Rumklang (Reverb)** — fra et lille rum til en katedral.
- **Forsinkelse og multi-tap-ekko** — fra et stramt slapback til en lang ambient hale.
- **Crossfeed** — blander stereokanalerne, så hovedtelefoner lyder mere som rigtige højttalere på hårdt panorerede mix.
- **Kompressor** — udjævner høje og stille dele, hvilket er godt til bilen eller fitnesscenteret.
- **Chorus, Flanger, Phaser, Auto-Wah, Distortion og Stereo Rotation** — kreative modulations- og karaktereffekter.

Flacbox har også automatisk lydstyrkeudjævning baseret på broadcast-standarden EBU R128 for lydstyrke. Albums og shufflede playlister afspilles på et jævnt niveau, så du ikke hele tiden skal justere lydstyrken. Den kommer med forudindstillingerne Light, Standard, Strong og Night.

## Byg din egen DSP-processor

Ud over effekterne giver Flacbox dig en 14-filter DSP-processor i realtid, som du selv konfigurerer. Du kan tilføje professionelle filtre og parametriske EQ-bånd, saturation og en bit crusher, og kreative processorer som tremolo, ring modulator og stereo width. Det hele kører live på alt, hvad du afspiller, fra en lokal FLAC til en skystream, og DSP-indstillingerne er endda tilgængelige i CarPlay.

## Musikvisualizer i fuld skærm

Flacbox har en indbygget musikvisualizer, der maler bevægelige, farverige visuals i takt med din musik. Den bruger den velkendte Milkdrop-motor (projectM) med 500 forudindstillinger, tegnet med OpenGL på iPhone, iPad og Mac. Åbn den fra afspilleren ved at trykke på knappen Flere handlinger og derefter Personalisering. Vælg en forudindstilling, eller brug Auto-tilstand til at skifte imellem dem hvert 30 sekunder med en jævn crossfade. For trinvis hjælp, se guiden om [hvordan man tænder musikvisualizeren](/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox musikvisualizer (Milkdrop and projectM)" image="/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac/music-visualizer-starfield-sectors-preset.webp" >}}
{{< /cards >}}

## Sky, NAS og offline afspilning

Stream direkte fra mere end 30 skytjenester, herunder iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, pCloud, Proton Drive og Internxt. Du kan også tilslutte selv-hostede servere som Plex, Jellyfin, Emby, Subsonic og Navidrome, og enhver NAS via SMB, WebDAV, DLNA, FTP, SFTP eller NFS.

Når du vil have din musik med dig, gemmer den indbyggede downloadmanager hele playlister, kunstnere, albums eller mapper til offline lytning. Offline-tilstand synkroniserer derefter automatisk nye numre, efterhånden som de dukker op i skyen. Er du ved at løbe tør for plads? Ryd cachen med ét tryk og fortsæt med at streame.

## Alt andet, som seriøse lyttere ønsker

- **Organiseret bibliotek** — grupperet efter Sange, Albums, Albumkunstnere, Kunstnere, Genrer og Komponister, med hurtig søgning, der virker offline.
- **ID3-tag-editor** — ret rodede metadata og ødelagte kodninger (kyrillisk, japansk, kinesisk) og skriv ændringerne tilbage til filen.
- **Playlister** — byg, omarranger, importer og eksporter M3U, M3U8 og CUE, og gør dem tilgængelige offline.
- **Apple CarPlay** — en dedikeret skærm i bilen til bibliotek, sky, lokal og offline musik, med equalizeren om bord.
- **AirPlay 2 og Chromecast** — cast til HomePods, Apple TV og Cast-aktiverede højttalere.
- **Lydbogsværktøjer** — flere bogmærker, justerbar hastighed, en sleep-timer og genoptagelse fra hvor du stoppede.
- **Widgets og mere** — widgets til hjemmeskærm og låseskærm, Last.fm-scrobbling, tidsindstillede sangtekster og LRC, og fuld VoiceOver-tilgængelighed.

Flacbox er gratis at downloade. Premium fjerner gratisversionens begrænsninger på skykonti, playlister og offline-mapper, og den fås som et engangskøb for livet eller et månedligt eller årligt abonnement, med Deling i familie.

{{< app-details product="flacbox" >}}

## Mulighed 2: Konverter FLAC til ALAC til Musik-appen

Hvis du virkelig vil have dine rips inde i Apples Musik-app, kan du konvertere dem. FLAC til ALAC er tabsfrit til tabsfrit, så du mister ingen kvalitet:

1. På din computer skal du batch-konvertere med et gratis værktøj som XLD på Mac eller foobar2000 på Windows. Begge bevarer dine tags.
2. Tilføj ALAC-filerne til dit Musik- eller iTunes-bibliotek.
3. Synkroniser til iPhonen med Finder på Mac eller Apple Devices-appen på Windows.

Afvejningerne er reelle. Du beholder nu to kopier af dit bibliotek, hver metadataredigering betyder endnu en synkronisering, og Musik-appens layout forbliver fast, uden regelbaserede playlister, uden equalizer, uden DSP og uden sky- eller NAS-streaming på enheden. Derfor vælger de fleste med seriøse FLAC-samlinger den første mulighed.

## Ofte stillede spørgsmål

{{% details title="Kan iPhone afspille FLAC-filer indbygget?" closed="true" %}}
Kun på en begrænset måde. Filer-appen kan forhåndsvise en enkelt FLAC-fil siden iOS 11, men der er intet bibliotek, playlister, kø, equalizer eller skystreaming. Til rigtig lytning skal du bruge en afspiller-app som Flacbox.
{{% /details %}}

{{% details title="Kan jeg afspille 24-bit eller 96kHz (eller højere) FLAC på iPhone?" closed="true" %}}
Ja. Flacbox understøtter hi-res-output op til 384 kHz. For at afspille over 48 kHz i sand opløsning skal du tilslutte en ekstern USB DAC, fordi iPhones indbyggede output resampler lyden for hver app.
{{% /details %}}

{{% details title="Konverterer Flacbox FLAC til et andet format?" closed="true" %}}
Nej. Flacbox afspiller FLAC i dens oprindelige tabsfrie kvalitet uden konvertering. Effekter og DSP anvendes kun live under afspilning, og de ændrer aldrig dine filer.
{{% /details %}}

{{% details title="Mister jeg kvalitet ved at konvertere FLAC til ALAC?" closed="true" %}}
Nej. FLAC og ALAC er begge tabsfri, så konverteringen er bit-perfekt. Du bruger kun tid og giver afkald på bekvemmelighed, da du ender med to biblioteker at vedligeholde og skal synkronisere igen efter redigeringer.
{{% /details %}}

{{% details title="Hvilke lydformater understøtter Flacbox?" closed="true" %}}
Mere end 120 formater, herunder FLAC, DSD (DSF og DFF), ALAC, APE, WAV, AIFF, WV, OGG, OPUS, MP3, AAC, M4A, WMA, og endda tracker- og MOD-musik som MOD, XM, IT og S3M.
{{% /details %}}

{{% details title="Har Flacbox en equalizer, effekter og en visualizer?" closed="true" %}}
Ja. Den har en 10-bånds equalizer med forudindstillinger og en forforstærker. Den har også en professionel BASS-motor med elleve effekter i realtid (reverb, delay, multi-tap-ekko, crossfeed, compressor, chorus, flanger, phaser, auto-wah, distortion og stereo rotation), plus EBU R128-lydstyrkeudjævning, en 14-filter DSP-processor og en Milkdrop-visualizer i fuld skærm med 500 forudindstillinger.
{{% /details %}}

{{% details title="Kan jeg streame FLAC fra min NAS eller sky?" closed="true" %}}
Ja. Flacbox opretter forbindelse til mere end 30 skytjenester og til en NAS eller computer via SMB, WebDAV, DLNA, FTP, SFTP og NFS. Hele dit bibliotek er tilgængeligt uden at kopiere filer til din iPhone, og du kan downloade numre til offline afspilning når som helst.
{{% /details %}}

{{% details title="Er Flacbox virkelig gratis?" closed="true" %}}
Flacbox er gratis at downloade, med kernefunktioner som equalizeren, skystreaming og offline afspilning. Premium fjerner gratisversionens begrænsninger på skykonti, playlister og offline-mapper, og den kommer som et engangskøb for livet eller et månedligt eller årligt abonnement, med Deling i familie.
{{% /details %}}
