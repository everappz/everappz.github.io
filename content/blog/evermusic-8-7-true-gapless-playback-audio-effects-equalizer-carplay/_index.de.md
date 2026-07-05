---
title: "Evermusic 8.7: Echte lückenlose Wiedergabe, Audioeffekte, Lautstärkenormalisierung, neu gestalteter Equalizer"
date: 2026-07-05
description: "Evermusic 8.7 für iPhone, iPad und Mac bringt echte lückenlose Wiedergabe, fünf Studio-Audioeffekte (Hall, Delay, Verzerrung, Kompressor, Crossfeed), EBU-R128-Lautstärkenormalisierung, einen neu gestalteten 10-Band-Equalizer mit Import/Export von Presets, eine neu entwickelte AVAudioEngine-Streaming-Engine mit FLAC- und Ogg-Vorbis-Unterstützung sowie ein schnelleres, genaueres CarPlay und Aktuelle Wiedergabe."
keywords: ["Evermusic 8.7", "Evermusic Update", "echte lückenlose Wiedergabe iPhone", "lückenloser Musikplayer iOS", "lückenlose Wiedergabe CarPlay", "Musikplayer Audioeffekte iPhone", "Hall Delay Verzerrung Kompressor Crossfeed iOS", "Crossfeed Kopfhörer iOS", "Lautstärkenormalisierung iPhone", "Lautheitsnormalisierung Musikplayer", "EBU R128 Normalisierung iOS", "ReplayGain-Alternative iPhone", "10-Band-Equalizer iPhone", "grafischer Equalizer iOS-App", "Equalizer-Presets Import Export", "FLAC-Player iPhone", "Ogg-Vorbis-Player iOS", "verlustfreier Musikplayer iPhone 2026", "AVAudioEngine Musikplayer", "CarPlay Musikplayer iPhone", "Aktuelle Wiedergabe Sperrbildschirm Genauigkeit", "Cloud-Musikplayer iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Lückenlose Wiedergabe", "Audioeffekte", "Hall", "Delay", "Verzerrung", "Kompressor", "Crossfeed", "Lautstärkenormalisierung", "EBU R128", "Equalizer", "FLAC", "Ogg Vorbis", "CarPlay", "Aktuelle Wiedergabe", "Liquid Glass", "Neuheiten"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**Kurzfassung:** [Evermusic 8.7](/products/evermusic) ist ein Release für Klangqualität für iPhone, iPad und Mac. Es bringt **echte lückenlose Wiedergabe** (keine Pausen, kein Klicken oder Knacken zwischen den Titeln), ein komplettes Set an **Studio-Audioeffekten** – Hall, Delay, Verzerrung, Kompressor und Crossfeed – sowie eine **EBU-R128-Lautstärkenormalisierung**, die die Lautheit von Song zu Song ohne ReplayGain-Tags gleichbleibend hält. Der **10-Band-Equalizer** wurde neu gestaltet, mit neuen Reglern, schnellerem Preset-Wechsel, eigenen Presets zum Importieren und Exportieren sowie einem besseren Layout im Querformat und auf dem iPad. Im Inneren verbessert eine **neu entwickelte AVAudioEngine-Streaming-Engine** die Zuverlässigkeit und Formatunterstützung, darunter **FLAC** und **Ogg Vorbis**. **CarPlay** und **Aktuelle Wiedergabe** sind schneller und genauer auf dem Sperrbildschirm, im Auto und über Fernbedienungen an Kopfhörern.

---

## Hallo zusammen!

Evermusic 8.7 steht zum Download bereit. Bei diesem Update dreht sich alles darum, wie Ihre Musik *klingt*. Wir haben die Wiedergabe-Engine für eine echte lückenlose Wiedergabe neu aufgebaut, eine Reihe von Audioeffekten in Studioqualität hinzugefügt, eine Lautheitsnormalisierung eingeführt und den Equalizer von den Reglern an neu gestaltet. Alles ist in Apples neues Design **Liquid Glass** gehüllt.

[Laden Sie Evermusic 8.7 aus dem App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) oder aktualisieren Sie von Ihrer bestehenden Version. Evermusic ist ein kostenloser Download mit optionalen In-App-Upgrades.

## Echte lückenlose Wiedergabe

Lückenlose Wiedergabe bedeutet, dass die Stille zwischen zwei Titeln verschwunden ist. Keine Pause, kein Klicken, kein Knacken – der aktuelle Song geht direkt in den nächsten über. Am wichtigsten ist das für Musik, die als Ganzes gehört werden sollte: **Live-Aufnahmen, DJ-Mixe, klassische Werke und Konzeptalben**, bei denen ein Titel direkt in einen anderen übergeht.

Hier ist, was sich technisch geändert hat. Die Audio-Engine von Evermusic hält zwei Titel gleichzeitig in Bereitschaft: den, den Sie hören, und den nächsten in der Warteschlange. Während der aktuelle Titel läuft, wird der nächste bereits im Hintergrund **abgerufen, dekodiert und vorgepuffert**. Wenn der aktuelle Titel sein Ende erreicht, übergibt die Engine **innerhalb des Players, nicht innerhalb des Audiostreams**, an den nächsten Titel. Die Ausgabe-Render-Schleife zieht kontinuierlich Audiosamples aus einem durchgehenden Ringpuffer, ohne jemals zu stoppen, sodass der Hörer nie eine Grenze wahrnimmt. Der Wechsel erfolgt zwischen den Samples, und genau deshalb gibt es keine hörbare Lücke.

Das funktioniert gleich, egal ob die Datei auf Ihrem Gerät, in der Cloud oder auf einem Medienserver liegt – bei entfernten Quellen beginnt das Vorpuffern nur etwas früher.

## Studio-Audioeffekte

Evermusic 8.7 fügt fünf Echtzeit-Audioeffekte hinzu, die Sie über Ihre Musik legen können. Jeder läuft als nativer Audio-Verarbeitungsknoten in der Wiedergabe-Engine, sodass er auf alles angewendet wird, was Sie abspielen – lokale Dateien, Cloud-Streams und Internetradio gleichermaßen – ohne erneute Kodierung.

Jeder Effekt wird mit einer **kuratierten Bibliothek von Presets** ausgeliefert, damit Sie mit einem Tipp einen großartigen Klang erhalten, und Evermusic **merkt sich Ihre genauen Einstellungen** zwischen den Sitzungen. Passen Sie ein beliebiges Bedienelement an, und der Effekt wechselt in einen **Manuell**-Zustand, sodass Sie immer wissen, wann Sie sich von einem Preset entfernt haben.

### Hall

Verleiht ein Raumgefühl, von einem knackigen Zimmer bis zu einer Kathedrale. Basiert auf Apples `AVAudioUnitReverb` und bietet **13 Raum-Presets** (Kleiner Raum, Mittlerer Saal, Plate, Kathedrale und mehr) sowie einen **Wet/Dry-Mix**-Regler von 0 bis 100 %, sodass Sie entscheiden, wie viel Raum Sie hinzufügen.

### Delay (Echo)

Ein klassisches Echo mit **10 Presets** – Slapback, Tape Echo, Dub, Ambient und andere. Sie können die **Delay-Zeit** (bis zu 2 Sekunden), das **Feedback** (Anzahl der Wiederholungen), einen **Tiefpass-Cutoff** zum Anwärmen der Wiederholungen und den **Wet/Dry-Mix** einstellen.

### Verzerrung

Von dezentem Grit bis zur vollständigen Lo-Fi-Zerstörung, angetrieben von `AVAudioUnitDistortion` mit **22 Charakter-Presets** (Bit Brush, Cellphone Concert, Radio Tower und mehr), einem **Pre-Gain**-Antriebsregler und einem Wet/Dry-Mix, sodass Sie den Effekt wieder in das saubere Signal einmischen können.

### Kompressor

Ein Dynamikprozessor (Apples `AUDynamicsProcessor`), der laute und leise Passagen ausgleicht. Er bietet den vollen professionellen Regelsatz – **Schwellenwert, Verhältnis/Headroom, Attack, Release, Expansion und Makeup-Gain** – mit **10 Presets**, die auf reale Situationen abgestimmt sind: darunter Sprache / Podcast, Späte Nacht, Filmdialog, Streaming-Angleichung und Maximale Lautheit.

### Crossfeed

Crossfeed lässt das Hören über Kopfhörer natürlicher klingen, indem es ein wenig des linken Kanals in den rechten mischt und umgekehrt, so wie Ihre Ohren echte Lautsprecher hören. Es basiert auf dem bekannten Algorithmus **Bauer stereophonic-to-binaural (bs2b)**, mit Kontrolle über den **Crossfeed-Pegel** und die **Cutoff-Frequenz** sowie **6 Presets**, darunter die unter Audiophilen beliebten Einstellungen *Chu Moy* und *Jan Meier*. Besonders gut ist es bei älteren, hart gepannten Stereo-Mischungen aus den 1960er- und 1970er-Jahren.

## Lautstärkenormalisierung

Haben Sie jemals eine Wiedergabeliste zusammengestellt, bei der ein Titel dröhnt und der nächste ein Flüstern ist? Die Lautstärkenormalisierung behebt das. Evermusic 8.7 verwendet die **EBU-R128-Lautheitsmessung** (denselben ITU-R-BS.1770-Standard, der im Rundfunk und bei Streaming-Diensten verwendet wird), um die tatsächliche wahrgenommene Lautheit jedes Titels zu messen und sie behutsam auf ein gleichbleibendes Ziel zu lenken.

Anders als ReplayGain benötigt sie **keine** Tags in Ihren Dateien und **verändert** Ihr Audiomaterial **nicht**. Sie arbeitet in Echtzeit auf allem, was Sie abspielen, einschließlich Cloud-Streams und Live-Radio, und setzt sich sauber zurück, wenn Sie spulen oder den Titel wechseln.

Vier Presets decken die häufigen Fälle ab:

- **Leicht** – sanfte Nivellierung (Ziel −20 LUFS).
- **Standard** – die Voreinstellung, streaming-typische Lautheit (Ziel −16 LUFS, bis zu +12 dB Anhebung für leise Titel).
- **Stark** – aggressive Angleichung für sehr gemischte Bibliotheken (Ziel −14 LUFS).
- **Nacht** – leiser und gleichmäßig für das Hören bei geringer Lautstärke am Abend (Ziel −23 LUFS).

Sie müssen zwischen den Songs nicht mehr zur Lautstärke greifen.

## Neu gestalteter Equalizer

Evermusics **grafischer 10-Band-Equalizer** hat eine komplette Neugestaltung erhalten. Die Bänder decken **32 Hz bis 16 kHz** ab (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), jedes einstellbar von **−12 dB bis +12 dB** in feinen 0,1-dB-Schritten, mit einem **Vorverstärker** von −24 dB bis +24 dB, um Clipping beim Anheben zu verhindern.

Das ist neu in 8.7:

- **Neue Regler** – präzise, reaktionsschnelle Bedienelemente, die das native iOS-26-System-Slider-Aussehen und das **Liquid Glass**-Material übernehmen.
- **Schnellerer, geschmeidigerer Preset-Wechsel** – springen Sie sofort zwischen Presets, mit einer neu gestalteten horizontalen Preset-Leiste im Hochformat und einer vertikalen Preset-Spalte im Querformat.
- **Besseres Layout im Querformat und auf dem iPad** – die Regler und die Preset-Auswahl ordnen sich neu an, um die zusätzliche Breite zu nutzen, statt sich in eine telefongroße Spalte zu quetschen.
- **Eigene Presets** – erstellen und speichern Sie Ihre eigenen Kurven, ordnen Sie sie neu und **importieren und exportieren** Sie Presets als `.eqp`-Dateien, um sie zwischen Geräten zu übertragen oder zu teilen.

Der Equalizer läuft nativ in der Engine (`AVAudioUnitEQ`), sodass er auf jede Quelle angewendet wird, und er funktioniert auch über AirPlay, Chromecast und CarPlay, wo dies unterstützt wird.

## Neu entwickelte Wiedergabe-Engine

Im Inneren läuft Evermusic 8.7 auf einer **neu entwickelten Streaming-Engine**, die auf Apples `AVAudioEngine` mit einer eigenen Render-Pipeline aufbaut. Das ist es, was die lückenlose Übergabe, die Effektkette und den Equalizer möglich macht, und es macht auch die alltägliche Wiedergabe zuverlässiger.

- **Verbesserte Formatunterstützung** – darunter **FLAC** (über Core Audio) und **Ogg Vorbis** (über `libvorbisfile`), neben MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF und mehr.
- **Intelligenteres Puffern** – ein adaptiver Vorpuffer skaliert mit Ihrer Verbindung, wobei ein durchgehender Ringpuffer die Ausgabe speist, sodass kurze Netzwerkaussetzer nicht zu Aussetzern werden.
- **Automatische Wiederherstellung** – ein Zustandsautomat für das Neupuffern sowie eine Wiederholungslogik mit Backoff nehmen die Wiedergabe nach einem Moment mit schwachem Signal sauber wieder auf, statt den Titel zu stoppen.
- **Weniger Unterbrechungen** – dieselbe Engine treibt lokale Dateien, Cloud-Streams, Medienserver und Internetradio an, sodass das Verhalten überall einheitlich ist.

## Aktuelle Wiedergabe und CarPlay

Die Bildschirme, auf die Sie beim Hören tatsächlich schauen – der **Sperrbildschirm**, **CarPlay** und die Fernbedienungstasten Ihres Autos oder Ihrer Kopfhörer – sind in 8.7 genauer und schneller.

- **Genauere Informationen bei Aktuelle Wiedergabe.** Evermusic erfasst den Zustand des Players unter einer Sperre, bevor es ihn veröffentlicht, sodass Titel, verstrichene Zeit, Dauer und Wiedergabe-/Pausenzustand auf dem Sperrbildschirm oder im Auto niemals widersprüchlich sein können. Puffer- und Ladezustände werden jetzt korrekt gemeldet, statt "Wiedergabe" anzuzeigen, während ein Titel noch abgerufen wird.
- **Zuverlässige Fernbedienungen.** Wiedergabe, Pause, Weiter, Zurück, Spulen, Überspringen, Zufall, Wiederholen und Wiedergabegeschwindigkeit reagieren alle einheitlich über Kopfhörertasten, Autobedienelemente und den Sperrbildschirm, angetrieben von `MPRemoteCommandCenter`.
- **Schnelleres CarPlay-Artwork.** Albumcover werden auf langen Listen jetzt mehrfach schneller geladen (Batch-Taktung von 1,0 s auf 0,25 s reduziert, wobei der erste sichtbare Bildschirm sofort lädt), und es erscheint nun in den kompakten iOS-26-CarPlay-Listenzeilen, die zuvor kein Artwork zeigten.
- **Korrekturen bei CarPlay-Sortierung und -Stabilität.** Schnelleres Sortieren bei großen Bibliotheken und Härtung gegen Abstürze in Randfällen beim Scrollen langer Listen.
- **Gedrosselte Metadaten-Updates.** Aktualisierungen von Aktuelle Wiedergabe und Fernbedienungsbefehlen werden gedrosselt, sodass schnelle Änderungen das System nicht mehr überschwemmen, was die Bedienelemente auf dem Sperrbildschirm und in CarPlay reaktionsschnell hält.

## Weitere Verbesserungen

- **Liquid-Glass-Design**-Verfeinerungen in der gesamten App – transluzente Oberflächen, geschmeidigere Animationen und überarbeitete Bedienelemente auf iOS, iPadOS und macOS.
- **Neue Home-Bildschirm-Widgets** mit verbesserter Aktualisierungslogik, die sie synchron hält, ohne zusätzlichen Akku zu verbrauchen.
- Korrekturen für aktuelle iOS-Versionen.
- Lokalisierungskorrekturen in mehreren Sprachen.
- Viele kleinere Verbesserungen auf Grundlage Ihrer E-Mails und App-Store-Bewertungen.

## Warum dieses Update wichtig ist

Evermusic 8.7 ist um eine Idee herum aufgebaut: **Ihre Musik sollte auf jeder Quelle bestmöglich klingen.**

1. **Ganze Alben, wie beabsichtigt.** Echte lückenlose Wiedergabe bedeutet, dass Live-Sets, DJ-Mixe und Konzeptalben endlich so abgespielt werden, wie der Künstler sie gemastert hat.
2. **Ein Studio in Ihrer Hosentasche.** Hall, Delay, Verzerrung, Kompressor, Crossfeed, ein neu gestalteter Equalizer und die Lautheitsnormalisierung geben Ihnen echte Kontrolle über Ihren Klang, nicht nur einen Ein/Aus-Schalter.
3. **Dasselbe Erlebnis überall.** Lokale Dateien, Cloud-Laufwerke, Medienserver und Internetradio laufen alle durch dieselbe neu entwickelte Engine, mit genauer Aktueller Wiedergabe und einem schnelleren CarPlay obendrauf.

## Holen Sie sich Evermusic 8.7

[**Laden Sie Evermusic aus dem App Store herunter**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) oder aktualisieren Sie direkt im App Store. Evermusic ist ein kostenloser Download mit optionalen In-App-Upgrades für erweiterte Funktionen.

Wenn Ihnen die App gefällt, hinterlassen Sie bitte eine Bewertung im App Store – das hilft wirklich. Haben Sie Feedback oder ein Problem festgestellt? Schreiben Sie uns an **support@everappz.com**. Wir lesen jede Nachricht.

## Häufig gestellte Fragen

{{% details title="Was ist neu in Evermusic 8.7?" closed="true" %}}
Evermusic 8.7 bringt echte lückenlose Wiedergabe, fünf Studio-Audioeffekte (Hall, Delay, Verzerrung, Kompressor und Crossfeed), EBU-R128-Lautstärkenormalisierung, einen neu gestalteten 10-Band-Equalizer mit eigenen Presets und Import/Export, eine neu entwickelte AVAudioEngine-Streaming-Engine mit verbesserter Formatunterstützung (darunter FLAC und Ogg Vorbis), ein schnelleres und genaueres CarPlay und Aktuelle Wiedergabe, Liquid-Glass-Design-Updates, aufgefrischte Home-Bildschirm-Widgets sowie Fehler- und Lokalisierungskorrekturen.
{{% /details %}}

{{% details title="Hat Evermusic echte lückenlose Wiedergabe?" closed="true" %}}
Ja. Ab Evermusic 8.7 ist die Wiedergabe wirklich lückenlos: Es gibt keine Pause, kein Klicken und kein Knacken zwischen den Titeln. Die Engine puffert und dekodiert den nächsten Titel vor, während der aktuelle läuft, und übergibt zwischen den Audiosamples auf einem durchgehenden Ringpuffer, sodass der Übergang unhörbar ist. Es funktioniert für lokale Dateien, Cloud-Streams und Medienserver und ist ideal für Live-Alben, DJ-Mixe und Konzeptalben.
{{% /details %}}

{{% details title="Welche Audioeffekte enthält Evermusic 8.7?" closed="true" %}}
Fünf Echtzeiteffekte: **Hall** (13 Raum-Presets, Wet/Dry-Mix), **Delay/Echo** (10 Presets mit Delay-Zeit, Feedback, Tiefpass und Mix), **Verzerrung** (22 Charakter-Presets mit Pre-Gain und Mix), **Kompressor** (ein vollwertiger Dynamikprozessor mit Schwellenwert, Verhältnis, Attack, Release, Expansion und Makeup-Gain sowie 10 Presets) und **Crossfeed** (Bauer-bs2b-Kopfhörer-Crossfeed mit Pegel- und Cutoff-Reglern und 6 Presets). Jeder Effekt wird mit kuratierten Presets ausgeliefert, und Ihre eigenen Einstellungen werden zwischen den Sitzungen gemerkt.
{{% /details %}}

{{% details title="Was ist Crossfeed und warum sollte ich es verwenden?" closed="true" %}}
Crossfeed mischt einen kleinen, gefilterten Anteil jedes Stereokanals in den anderen, so wie Ihre Ohren echte Lautsprecher in einem Raum von Natur aus hören. Über Kopfhörer reduziert das die übertriebene, "im-Kopf"-Trennung hart gepannter Aufnahmen und macht langes Hören angenehmer. Evermusic verwendet den bekannten Algorithmus Bauer stereophonic-to-binaural (bs2b) und enthält Presets wie Chu Moy und Jan Meier. Besonders wirkungsvoll ist es bei älteren Stereo-Mischungen aus den 1960er- und 1970er-Jahren.
{{% /details %}}

{{% details title="Wie funktioniert die Lautstärkenormalisierung in Evermusic?" closed="true" %}}
Evermusic 8.7 misst die wahrgenommene Lautheit jedes Titels in Echtzeit mit dem Standard EBU R128 (ITU-R BS.1770) und passt den Pegel behutsam an ein gleichbleibendes Ziel an, sodass Titel nicht in der Lautstärke springen. Es benötigt keine ReplayGain-Tags und verändert Ihre Dateien nicht. Vier Presets sind verfügbar – Leicht (−20 LUFS), Standard (−16 LUFS), Stark (−14 LUFS) und Nacht (−23 LUFS) – und die Normalisierung setzt sich sauber zurück, wenn Sie spulen oder den Titel wechseln.
{{% /details %}}

{{% details title="Ist die Lautstärkenormalisierung von Evermusic dasselbe wie ReplayGain?" closed="true" %}}
Sie verfolgt dasselbe Ziel – eine gleichbleibende Lautheit zwischen den Titeln – funktioniert aber anders. ReplayGain stützt sich auf Lautheits-Tags, die in Ihren Dateien gespeichert sind. Der Normalisierer von Evermusic misst die Lautheit live mit EBU R128, sodass er auf jeder Quelle funktioniert, einschließlich Cloud-Streams und Internetradio, selbst wenn die Dateien überhaupt keine Tags haben.
{{% /details %}}

{{% details title="Wie viele Bänder hat der Evermusic-Equalizer, und kann ich eigene Presets erstellen?" closed="true" %}}
Der Evermusic-Equalizer ist ein grafischer 10-Band-Equalizer, der 32 Hz bis 16 kHz abdeckt, wobei jedes Band von −12 dB bis +12 dB in 0,1-dB-Schritten einstellbar ist und ein Vorverstärker von −24 dB bis +24 dB zur Verfügung steht. Er enthält integrierte Presets, lässt Sie eigene Presets erstellen und speichern und unterstützt den Import und Export von Presets als .eqp-Dateien, sodass Sie sie zwischen Geräten übertragen oder teilen können.
{{% /details %}}

{{% details title="Was hat sich am Equalizer von Evermusic 8.7 geändert?" closed="true" %}}
Der Equalizer wurde mit neuen, präziseren Reglern neu gestaltet, die das iOS-26-System-Slider- und Liquid-Glass-Aussehen übernehmen, mit schnellerem und geschmeidigerem Preset-Wechsel sowie einem besseren Layout im Querformat und auf dem iPad (eine horizontale Preset-Leiste im Hochformat und eine vertikale Preset-Spalte im Querformat). Eigene Presets und der .eqp-Import/-Export werden unterstützt.
{{% /details %}}

{{% details title="Unterstützt Evermusic 8.7 FLAC und Ogg Vorbis?" closed="true" %}}
Ja. Die neu entwickelte Engine spielt FLAC (über Core Audio) und Ogg Vorbis (über libvorbisfile), zusammen mit MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF und mehr, von lokalen Dateien, Cloud-Laufwerken und Medienservern.
{{% /details %}}

{{% details title="Was wurde in CarPlay und auf dem Sperrbildschirm verbessert?" closed="true" %}}
CarPlay-Albumcover werden auf langen Listen mehrfach schneller geladen und erscheinen jetzt in den kompakten iOS-26-Listenzeilen, die zuvor keine zeigten. Die Informationen bei Aktuelle Wiedergabe auf dem Sperrbildschirm und in CarPlay sind genauer – Titel, verstrichene Zeit, Dauer und Wiedergabe-/Pausenzustand werden gemeinsam erfasst, sodass sie nicht widersprüchlich sein können, und Pufferzustände werden korrekt gemeldet. Fernbedienungen (Wiedergabe, Pause, Weiter, Zurück, Spulen, Zufall, Wiederholen, Geschwindigkeit) reagieren zuverlässig über Kopfhörer und im Auto, und die CarPlay-Sortierung bei großen Bibliotheken ist schneller.
{{% /details %}}

{{% details title="Funktionieren die Audioeffekte und der Equalizer mit Cloud-Streaming und CarPlay?" closed="true" %}}
Ja. Die Effekte, der Equalizer und die Lautstärkenormalisierung laufen nativ innerhalb der Wiedergabe-Engine, sodass sie auf alles angewendet werden, was Evermusic abspielt – lokale Dateien, Cloud-Laufwerke, Medienserver und Internetradio – und sie funktionieren während der CarPlay-Wiedergabe sowie, wo unterstützt, über AirPlay und Chromecast weiter.
{{% /details %}}

{{% details title="Ist das Update auf Evermusic 8.7 kostenlos, und welche Geräte werden unterstützt?" closed="true" %}}
Ja. Evermusic ist ein kostenloser Download aus dem App Store, und 8.7 ist ein kostenloses Update für bestehende Nutzer, mit optionalen In-App-Upgrades für erweiterte Funktionen. Es läuft auf iPhone, iPad und Mac. CarPlay erfordert ein CarPlay-kompatibles Fahrzeug oder Head-Unit.
{{% /details %}}
