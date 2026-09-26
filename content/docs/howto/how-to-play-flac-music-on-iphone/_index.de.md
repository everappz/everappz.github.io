---
title: "FLAC-Musik (verlustfrei) auf dem iPhone abspielen"
date: 2024-01-29
lastmod: 2026-09-26
description: "So spielen Sie FLAC 2026 auf iPhone und iPad mit Flacbox ab, einem Hi-Res-Player mit über 120 Formaten, Ausgabe bis 384 kHz, USB-DAC-Unterstützung, einem 10-Band-Equalizer, der BASS-Audio-Engine, Echtzeiteffekten wie Hall und Delay, einem DSP-Prozessor und einem Musikvisualizer mit 500 Presets. Streamen Sie aus der Cloud oder vom NAS und hören Sie offline."
keywords: ["flac auf iphone abspielen", "flac player iphone", "flac", "iphone", "verlustfrei", "hi-res audio", "dsd player ios", "usb dac iphone", "384khz", "musik", "flacbox", "streamen", "offline", "equalizer", "dsp", "musikvisualizer", "bass engine"]
tags: ["musik", "cloud", "player", "downloader", "equalizer", "verlustfrei", "hi-res", "offline", "FLAC", "DSD", "DAC", "streamer", "visualizer", "DSP"]
readingTime: 8
---

{{< author-byline >}}


**Kurzfassung:** Um FLAC auf einem iPhone abzuspielen, brauchen Sie einen Player eines Drittanbieters, denn Apples Musik-App unterstützt kein FLAC. Installieren Sie [Flacbox](/products/flacbox) (kostenlos), übertragen Sie Ihre Dateien dann entweder per Wi-Fi Drive oder USB, oder verbinden Sie Ihren Cloud-Speicher oder Ihr NAS. Ihre FLAC-Bibliothek läuft in voller Qualität, bis zu 384 kHz und 32-bit über einen USB DAC. Flacbox spielt außerdem mehr als 120 Formate ab, darunter FLAC, DSD, ALAC, APE, WAV, OGG und OPUS, und bietet einen 10-Band-Equalizer, die professionelle BASS-Audio-Engine mit Echtzeiteffekten, einen DSP-Prozessor und einen Vollbild-Musikvisualizer.

[{{< figure src="/docs/howto/how-to-play-flac-music-on-iphone/Flacbox_Icon-App-1024x1024.webp" alt="Flacbox Icon - FLAC music player and downloader" width="160" >}}](/products/flacbox)

## Warum spielt mein iPhone FLAC nicht nativ ab?

Apple hat ein eigenes verlustfreies Format namens ALAC (Apple Lossless), und die Musik-App ist darauf ausgelegt statt auf FLAC. Seit iOS 11 kann die Dateien-App eine einzelne FLAC-Datei in der Vorschau anzeigen, aber sie hat keine Musikbibliothek, keine Wiedergabelisten, keine Warteschlange, keinen Equalizer und kein Cloud-Streaming. Sie ist ein Dateibetrachter, kein Musikplayer.

Sie haben also zwei echte Optionen:

1. FLAC mit einer Player-App abspielen, sodass Ihre Dateien genau so bleiben, wie sie sind. Das ist die Variante, die wir empfehlen.
2. FLAC in ALAC umwandeln, was verlustfrei zu verlustfrei ist, und dann mit der Musik-App synchronisieren.

Wenn Sie eine echte FLAC-Sammlung haben, ist die erste Option besser. Sie vermeiden eine doppelte Bibliothek, sparen sich die Umwandlungszeit, und Ihre Ordner sowie die Hi-Res-Qualität bleiben unberührt. Flacbox ist genau dafür gemacht.

## Option 1: FLAC mit Flacbox abspielen

Flacbox ist ein Hi-Res-Musikplayer für iPhone, iPad und Mac. Er verwandelt Ihren Cloud-Speicher, Ihr NAS oder Ihren Computer in Ihre eigene private Musikbibliothek, ohne Umwandlung und ohne Abonnement.

### Schritt 1. Flacbox installieren

Flacbox ist ein kostenloser Download und läuft auf iPhone, iPad und Mac.

{{< app-details product="flacbox" >}}

### Schritt 2. Ihre FLAC-Dateien hineinbekommen

Wählen Sie den für Sie einfachsten Weg:

- **Wi-Fi Drive** — öffnen Sie Verbindungen, dann Computer, dann Über WLAN verbinden, und ziehen Sie Dateien aus einem beliebigen Desktop-Browser hinein. Siehe die [Anleitung zu Wi-Fi Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).
- **Cloud-Speicher** — verbinden Sie iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, pCloud, Proton Drive und 20 weitere, und streamen Sie dann direkt aus der Cloud.
- **NAS oder Computer** — verbinden Sie sich über SMB, WebDAV, DLNA, FTP, SFTP oder NFS (Synology, QNAP, WD My Cloud, Time Capsule oder jede Samba-Freigabe). Die vollständige Liste finden Sie in der [Anleitung zu Verbindungen](/docs/guide/flacbox/flacbox-guide-connections).
- **USB-Stick** — stecken Sie einen SanDisk iXpand oder einen beliebigen externen Leser ein und spielen Sie [direkt vom Laufwerk](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it), ganz ohne Import.
- **iTunes- oder Finder-Dateifreigabe** — über ein Lightning- oder USB-C-Kabel.

### Schritt 3. Auf Play drücken

Ihre Titel erscheinen in der Bibliothek mit Tags und Cover-Art, die aus den Dateien selbst gelesen werden, gruppiert nach Album, Künstler, Genre und Komponist. Jeder Titel zeigt seinen genauen Codec und seine Auflösung an, zum Beispiel FLAC, 96 kHz, 24-bit.

## Hi-Res-Ausgabe, USB DAC und Mehrkanal

Flacbox ist für Menschen gemacht, denen Klangqualität wichtig ist, nicht nur für die beiläufige Wiedergabe:

- **Abtastrate** — spielt von 8 kHz bis 384 kHz, mit Mehrkanalausgabe von 1 bis 7 Kanälen (bis zu 5.1 und ITU BS.775-1).
- **USB-DAC-Unterstützung** — alles über 48 kHz wird in seiner echten Auflösung über einen USB DAC abgespielt. Über die eigene Ausgabe des iPhones rechnet iOS das Audiosignal wie bei jeder App neu ab, daher ist ein DAC der Weg zu bit-perfektem Hi-Res.
- **Einstellbare Ausgabe** — legen Sie Abtastrate, Kanalanzahl und IO-Puffer-Dauer (etwa 5 ms für Hi-Res mit geringer Latenz) unter Einstellungen und dann Audioplayer fest.
- **Tonhöhe und Geschwindigkeit** — feine Tonhöhenkorrektur, plus Wiedergabegeschwindigkeit von 0.02× bis 3.00×.

## Spielt mehr als 120 Formate, nicht nur FLAC

Neben FLAC bringt Flacbox FFmpeg mit, sodass es Formate abspielen kann, die iOS von sich aus nicht öffnen kann. Sie müssen eine gemischte Bibliothek nicht erst umwandeln oder bereinigen:

- **Verlustfrei und Hi-Res** — FLAC, ALAC, WAV, AIFF, APE, WV (WavPack) und DSD (DSF und DFF, einschließlich DSD64, DSD128 und DSD256).
- **Verlustbehaftet** — MP3, AAC, M4A, OGG, OPUS, WMA, MPC und mehr.
- **Tracker- und MOD-Musik** — klassische MOD-, XM-, IT-, S3M-, MTM-, UMX- und MO3-Chiptune- und Demoscene-Dateien, die die meisten Player nicht öffnen können.

Das sind insgesamt mehr als 120 Formate, was so gut wie alles in einer modernen Musiksammlung abdeckt.

## Drei Audio-Engines, einschließlich der BASS-Engine

Sie können die Wiedergabe-Engine unter Einstellungen, dann Audioplayer, dann Audio-Codec auswählen:

- **System Codec + FFmpeg** — maximale Kompatibilität und Stabilität.
- **FFmpeg** — erzwingt den FFmpeg-Pfad, der die Tonhöhenkorrektur und eine benutzerdefinierte Ausgabe-Abtastrate freischaltet.
- **BASS™-Engine** — der professionelle Wiedergabekern, der in [Flacbox 7.6](/blog/flacbox-7-6-bass-audio-engine-effects-dsp-music-visualizer) hinzugefügt wurde. Er schaltet die Echtzeit-Audioeffekte, den DSP-Prozessor, den Musikvisualizer, die Tracker- und MOD-Wiedergabe sowie hochwertiges Resampling frei. Außerdem bietet er eine unabhängige Tonhöhensteuerung (±60 semitones) und Temposteuerung (0.1× bis 4×).

## 10-Band-Equalizer, Bass-Boost und Vorverstärker

Flacbox enthält einen grafischen 10-Band-Equalizer mit Presets im iPod-Stil wie Acoustic, Bass Booster, Rock, Pop, Jazz, Classical und Dance. Es gibt einen Vorverstärker, um leise Titel ohne Clipping anzuheben, und Sie können Ihre eigenen Presets speichern. Stellen Sie ihn für In-Ear-Monitore, einen HomePod oder ein Autoradio ein. Eine vollständige Anleitung finden Sie in der [Equalizer-Anleitung](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Audioplayer-Equalizer" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Echtzeit-Audioeffekte

Wenn die BASS-Engine aktiv ist, erhalten Sie elf Echtzeiteffekte, die Sie während der Musikwiedergabe stapeln und anpassen können. Nichts wird neu codiert, und wenn Sie einen Effekt ausschalten, kehrt der Originalklang sofort zurück:

- **Reverb** — von einem kleinen Raum bis zu einer Kathedrale.
- **Delay und Multi-Tap-Echo** — von einem knappen Slapback bis zu einer langen ambienten Fahne.
- **Crossfeed** — mischt die Stereokanäle, sodass Kopfhörer bei stark gepannten Mixes eher wie echte Lautsprecher klingen.
- **Compressor** — gleicht laute und leise Passagen aus, was fürs Auto oder das Fitnessstudio ideal ist.
- **Chorus, Flanger, Phaser, Auto-Wah, Distortion und Stereo Rotation** — kreative Modulations- und Charaktereffekte.

Flacbox verfügt außerdem über eine automatische Lautstärkeanpassung auf Basis des rundfunktauglichen EBU R128 Lautheitsstandards. Alben und zufällig abgespielte Wiedergabelisten laufen mit gleichmäßigem Pegel, sodass Sie nicht ständig zur Lautstärke greifen müssen. Es gibt die Presets Light, Standard, Strong und Night.

## Bauen Sie Ihren eigenen DSP-Prozessor

Über die Effekte hinaus bietet Ihnen Flacbox einen Echtzeit-DSP-Prozessor mit 14 Filtern, den Sie selbst einrichten. Sie können professionelle Filter und parametrische EQ-Bänder, Sättigung und einen Bit-Crusher sowie kreative Prozessoren wie Tremolo, Ringmodulator und Stereobreite hinzufügen. Alles läuft live auf allem, was Sie abspielen, von einer lokalen FLAC bis zu einem Cloud-Stream, und die DSP-Einstellungen sind sogar in CarPlay verfügbar.

## Vollbild-Musikvisualizer

Flacbox hat einen integrierten Musikvisualizer, der bewegte, farbenfrohe Visuals im Takt Ihrer Musik zeichnet. Er nutzt die bekannte Milkdrop-Engine (projectM) mit 500 presets, gezeichnet mit OpenGL auf iPhone, iPad und Mac. Öffnen Sie ihn im Player, indem Sie auf die Schaltfläche Weitere Aktionen und dann Visualisierung tippen. Wählen Sie ein Preset, oder nutzen Sie den Auto-Modus, um alle 30 Sekunden mit einer sanften Überblendung durch sie zu wechseln. Eine Schritt-für-Schritt-Hilfe finden Sie in der Anleitung dazu, [wie man den Musikvisualizer aktiviert](/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Musikvisualizer (Milkdrop und projectM)" image="/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac/music-visualizer-starfield-sectors-preset.webp" >}}
{{< /cards >}}

## Cloud, NAS und Offline-Wiedergabe

Streamen Sie direkt von mehr als 30 Cloud-Diensten, darunter iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, pCloud, Proton Drive und Internxt. Sie können auch selbst gehostete Server wie Plex, Jellyfin, Emby, Subsonic und Navidrome verbinden, sowie jedes NAS über SMB, WebDAV, DLNA, FTP, SFTP oder NFS.

Wenn Sie Ihre Musik dabeihaben möchten, speichert der integrierte Download-Manager ganze Wiedergabelisten, Künstler, Alben oder Ordner zum Offline-Hören. Der Offline-Modus synchronisiert dann automatisch neue Titel, sobald sie in der Cloud auftauchen. Wenig Speicherplatz? Leeren Sie den Cache mit einem Tippen und streamen Sie weiter.

## Alles Weitere, was anspruchsvolle Hörer wollen

- **Organisierte Bibliothek** — gruppiert nach Songs, Alben, Album-Künstlern, Künstlern, Genres und Komponisten, mit schneller Suche, die offline funktioniert.
- **ID3-Tag-Editor** — beheben Sie unordentliche Metadaten und defekte Kodierungen (Kyrillisch, Japanisch, Chinesisch) und schreiben Sie die Änderungen zurück in die Datei.
- **Wiedergabelisten** — erstellen, umsortieren, M3U, M3U8 und CUE importieren und exportieren und offline verfügbar machen.
- **Apple CarPlay** — ein eigener Bildschirm im Auto für Bibliothek, Cloud, lokale und Offline-Musik, mit dem Equalizer an Bord.
- **AirPlay 2 und Chromecast** — auf HomePods, Apple TV und Cast-fähige Lautsprecher übertragen.
- **Hörbuch-Werkzeuge** — mehrere Lesezeichen, einstellbare Geschwindigkeit, ein Sleep-Timer und Fortsetzung dort, wo Sie aufgehört haben.
- **Widgets und mehr** — Widgets für Home- und Sperrbildschirm, Last.fm-Scrobbling, zeitgesteuerte Liedtexte und LRC sowie volle VoiceOver-Barrierefreiheit.

Flacbox ist ein kostenloser Download. Premium hebt die Grenzen der kostenlosen Version für Cloud-Konten, Wiedergabelisten und Offline-Ordner auf und ist als einmaliger lebenslanger Kauf oder als monatliches oder jährliches Abonnement mit Familienfreigabe erhältlich.

{{< app-details product="flacbox" >}}

## Option 2: FLAC für die Musik-App in ALAC umwandeln

Wenn Sie Ihre Rips unbedingt in Apples Musik-App haben möchten, können Sie sie umwandeln. FLAC zu ALAC ist verlustfrei zu verlustfrei, sodass Sie keine Qualität verlieren:

1. Wandeln Sie auf Ihrem Computer stapelweise mit einem kostenlosen Tool wie XLD auf Mac oder foobar2000 auf Windows um. Beide behalten Ihre Tags bei.
2. Fügen Sie die ALAC-Dateien zu Ihrer Musik- oder iTunes-Bibliothek hinzu.
3. Synchronisieren Sie mit dem iPhone über Finder auf Mac oder die Apple-Geräte-App auf Windows.

Die Nachteile sind real. Sie behalten nun zwei Kopien Ihrer Bibliothek, jede Metadaten-Änderung bedeutet eine weitere Synchronisierung, und das Layout der Musik-App bleibt fest, ohne regelbasierte Wiedergabelisten, ohne Equalizer, ohne DSP und ohne Cloud- oder NAS-Streaming auf dem Gerät. Deshalb entscheiden sich die meisten Menschen mit ernsthaften FLAC-Sammlungen für die erste Option.

## FAQ

{{% details title="Kann das iPhone FLAC-Dateien nativ abspielen?" closed="true" %}}
Nur eingeschränkt. Die Dateien-App kann seit iOS 11 eine einzelne FLAC-Datei in der Vorschau anzeigen, aber es gibt keine Bibliothek, keine Wiedergabelisten, keine Warteschlange, keinen Equalizer und kein Cloud-Streaming. Für echtes Hören nutzen Sie eine Player-App wie Flacbox.
{{% /details %}}

{{% details title="Kann ich 24-bit- oder 96kHz-FLAC (oder höher) auf dem iPhone abspielen?" closed="true" %}}
Ja. Flacbox unterstützt Hi-Res-Ausgabe bis zu 384 kHz. Um oberhalb von 48 kHz in echter Auflösung abzuspielen, schließen Sie einen externen USB DAC an, denn die eingebaute Ausgabe des iPhones rechnet das Audiosignal für jede App neu ab.
{{% /details %}}

{{% details title="Wandelt Flacbox FLAC in ein anderes Format um?" closed="true" %}}
Nein. Flacbox spielt FLAC in seiner ursprünglichen verlustfreien Qualität ohne Umwandlung ab. Effekte und DSP werden nur live während der Wiedergabe angewendet und ändern niemals Ihre Dateien.
{{% /details %}}

{{% details title="Verliere ich Qualität, wenn ich FLAC in ALAC umwandle?" closed="true" %}}
Nein. FLAC und ALAC sind beide verlustfrei, sodass die Umwandlung bit-perfekt ist. Sie investieren nur Zeit und geben Komfort auf, denn Sie enden mit zwei Bibliotheken, die Sie pflegen müssen, und Sie müssen nach Änderungen erneut synchronisieren.
{{% /details %}}

{{% details title="Welche Audioformate unterstützt Flacbox?" closed="true" %}}
Mehr als 120 Formate, darunter FLAC, DSD (DSF und DFF), ALAC, APE, WAV, AIFF, WV, OGG, OPUS, MP3, AAC, M4A, WMA und sogar Tracker- und MOD-Musik wie MOD, XM, IT und S3M.
{{% /details %}}

{{% details title="Hat Flacbox einen Equalizer, Effekte und einen Visualizer?" closed="true" %}}
Ja. Es hat einen 10-Band-Equalizer mit Presets und einem Vorverstärker. Es hat außerdem eine professionelle BASS-Engine mit elf Echtzeiteffekten (Reverb, Delay, Multi-Tap-Echo, Crossfeed, Compressor, Chorus, Flanger, Phaser, Auto-Wah, Distortion und Stereo Rotation), plus EBU R128 Lautstärkeanpassung, einen DSP-Prozessor mit 14 Filtern und einen Vollbild-Milkdrop-Visualizer mit 500 presets.
{{% /details %}}

{{% details title="Kann ich FLAC von meinem NAS oder aus der Cloud streamen?" closed="true" %}}
Ja. Flacbox verbindet sich mit mehr als 30 Cloud-Diensten und mit einem NAS oder Computer über SMB, WebDAV, DLNA, FTP, SFTP und NFS. Ihre gesamte Bibliothek ist verfügbar, ohne Dateien auf Ihr iPhone zu kopieren, und Sie können Titel jederzeit für die Offline-Wiedergabe herunterladen.
{{% /details %}}

{{% details title="Ist Flacbox wirklich kostenlos?" closed="true" %}}
Flacbox ist ein kostenloser Download mit Kernfunktionen wie dem Equalizer, Cloud-Streaming und Offline-Wiedergabe. Premium hebt die Grenzen der kostenlosen Version für Cloud-Konten, Wiedergabelisten und Offline-Ordner auf und kommt als einmaliger lebenslanger Kauf oder als monatliches oder jährliches Abonnement mit Familienfreigabe.
{{% /details %}}
