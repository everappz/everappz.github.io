---
title: "So verwenden Sie Klangeffekte und DSP in Flacbox: Compressor, Freeverb, Crossfeed, Echo, Lautstärkenormalisierung und mehr"
date: 2026-07-24
description: "Der vollständige Leitfaden zum Flacbox-Audio auf iPhone, iPad und Mac. Erfahren Sie, wie die BASS-Engine funktioniert, welche zusätzlichen Formate sie abspielt (einschließlich MOD- und Tracker-Musik sowie DSD) und was genau jeder Effekt, jeder Regler und jedes Preset mit Ihrem Klang macht, dazu der 10-Band-Equalizer und die eigene DSP-Kette."
keywords: ["Flacbox Audioeffekte", "Flacbox Presets erklärt", "Flacbox BASS-Engine", "BASS Audio-Bibliothek iOS", "MOD-Musikplayer iPhone", "Tracker-Musikplayer iOS", "MOD XM IT S3M abspielen iPhone", "DSD-Player iOS", "FLAC-Player iPhone", "verlustfreier Musikplayer iOS", "Flacbox Equalizer-Presets", "10-Band-Equalizer iPhone", "Lautstärkenormalisierung iPhone", "EBU R128 iOS", "Lautheitsnormalisierung Musikplayer", "Crossfeed Kopfhörer iOS", "bs2b Crossfeed", "Compressor-Presets Musikplayer", "Freeverb Hall iOS", "Echo Delay Musikplayer", "DSP-Kette Musikplayer", "Bass-Boost iPhone", "wie füge ich Effekte zu Musik hinzu Flacbox", "beste Equalizer-Einstellungen iPhone"]
tags: ["Flacbox", "Audioeffekte", "Anleitung", "BASS", "Equalizer", "Bass-Boost", "Compressor", "Freeverb", "Crossfeed", "Echo", "Lautstärkenormalisierung", "EBU R128", "MOD-Musik", "Tracker-Musik", "DSD", "FLAC", "DSP", "Kopfhörer", "Presets"]
readingTime: 30
---

{{< author-byline >}}

**Kurze Antwort:** In Flacbox wählen Sie eine **Wiedergabe-Engine** unter **Einstellungen > Audio-Player**: **Standard** (Apples System-Engine), **Universal** (die FFmpeg-Engine) oder **Sound FX** (die **BASS™-Engine**). Die gewählte Engine bestimmt, welche Dateiformate abgespielt werden, die Wahl ist also wichtig. Die **Sound FX**-Engine spielt zusätzliche Formate, die die meisten iPhone-Apps auslassen (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus und alte **MOD- und Tracker-Musik** wie MOD, XM, IT und S3M), und sie ist die einzige Engine, die die Klangwerkzeuge antreibt: einen **10-Band-Equalizer**, **Lautstärkenormalisierung**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed** und eine selbst zusammengestellte **DSP-Kette**. Um also die Effekte in diesem Leitfaden zu nutzen, stellen Sie Ihre Wiedergabe-Engine zuerst auf **Sound FX**. Jedes Werkzeug hat fertige **Presets**. Öffnen Sie sie unter **Einstellungen > Audio-Player** (Audioeffekte, Audio-Equalizer, Signalverarbeitung) oder tippen Sie im Player auf die Schaltfläche **⋯ (Weitere Aktionen)** und wählen Sie **Audioeffekte**. Nichts, was Sie hier tun, verändert jemals Ihre Dateien.

> Die Erklärungen zu Reglern und Presets unten sind dieselben kurzen Beschreibungen, die Flacbox Ihnen in der App zeigt, angereichert mit etwas zusätzlichem Hintergrund, damit Sie das Gesamtbild haben, bevor Sie tippen.

## So lesen Sie diesen Leitfaden

Jedes Werkzeug funktioniert auf die gleiche Weise:

1. **Einschalten.** Jeder Effekt hat seinen eigenen Ein/Aus-Schalter. Zu Beginn sind alle aus. Sie können so viele gleichzeitig einschalten, wie Sie möchten.
2. **Preset wählen.** Ein Preset ist eine fertige Einstellung. Tippen Sie eines an, und der Klang ändert sich sofort. Dieser Leitfaden listet auf, was **jedes** Preset bewirkt.
3. **Feinabstimmung (optional).** Öffnen Sie die Regler, um von Hand anzupassen. Sobald Sie einen Regler bewegen, zeigt der Effekt **Manuell** an, damit Sie wissen, dass Sie das Preset verlassen haben. Jeder Regler hat eine Zurücksetzen-Schaltfläche.

Nichts wird in Ihre Dateien gespeichert. Dies sind Live-Effekte. Schalten Sie einen Effekt aus, und Ihr Originalklang kehrt sofort zurück.

## Wählen Sie Ihre Wiedergabe-Engine (Sound FX hat die Effekte)

Flacbox mischt keine Engines miteinander. Sie wählen **eine** unter **Einstellungen > Audio-Player > Wiedergabe-Engine**, und die gewählte Engine bestimmt, welche Dateiformate Sie abspielen können und ob die Effekte verfügbar sind. Es gibt drei Möglichkeiten, in der App unter diesen genauen Namen angezeigt:

1. **Standard.** Apples eingebaute System-Engine. Nutzt Hardware-Decodierung für geringeren Batterieverbrauch.
2. **Universal.** Die FFmpeg-Engine, die eine sehr breite Palette an Formaten öffnet.
3. **Sound FX.** Die **BASS™-Engine**. Sie spielt verlustfreie und hochauflösende Dateien mit voller Genauigkeit ab, fügt Modul- (Tracker-)Musik hinzu und treibt jeden Effekt, den 10-Band-Equalizer und die DSP-Kette in diesem Leitfaden an.

Da jede Engine ihren eigenen Satz an Formaten unterstützt, ändern sich die Dateien, die Sie abspielen können, mit der gewählten Engine. Noch wichtiger: Die Effekte, der Equalizer und die DSP-Kette funktionieren **nur** mit der **Sound FX**-Engine, wählen Sie sie also zuerst, wenn Sie sie nutzen möchten.

Sound FX baut auf **BASS™** auf, einer professionellen Audio-Bibliothek von Un4seen Developments. Mehr dazu erfahren Sie auf der Startseite unter [un4seen.com](https://www.un4seen.com/).

## Musikformate: Was die Sound FX (BASS™)-Engine hinzufügt (einschließlich MOD- und Tracker-Musik)

Mit ausgewählter **Sound FX (BASS™)**-Engine spielt Flacbox die untenstehenden Spezialformate zusätzlich zu den alltäglichen ab. Das Besondere ist **Modulmusik**, auch **Tracker-Musik** genannt. Eine Moduldatei ist keine normale Aufnahme. Sie enthält kleine Instrumentenklänge plus eine «Partitur», die angibt, wie sie abzuspielen sind, und Flacbox baut den Song live aus dieser Partitur nach, so wie diese Dateien gedacht waren. Normale Player können das nicht.

| Musikart | Formate | Gut zu wissen |
|---|---|---|
| **Modul- / Tracker-Musik** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Live nachgebaut vom BASS™-Modulplayer. Ideal für Chiptunes und alte Demoszene- oder Amiga-Songs. |
| **Modernes verlustfreies** | FLAC | Volle Qualität, kleiner als WAV. |
| **Anderes verlustfreies** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Weniger verbreitete verlustfreie Typen, alle unterstützt. |
| **Hochauflösendes DSD** | DSF, DFF | Spielt auf normaler Hardware mittels DSD über PCM. |
| **Modernes verlustbehaftetes** | Opus, Ogg Vorbis, MP3 | Die üblichen Streaming- und Download-Typen. |

Die Sound FX-Engine spielt auch die gängigen Apple-Formate (AAC, ALAC, M4A, WAV, AIFF) und Live-Streams, sodass die Effekte und der Equalizer auch bei diesen funktionieren.

**Warum das für Sie hilfreich ist:** Wenn Sie eine Mischung aus FLAC-Alben, hochauflösenden DSD-Dateien und einem Ordner mit alten MOD- oder XM-Tracker-Songs haben, spielt Flacbox sie alle ab, und der Equalizer und die Effekte funktionieren bei jedem einzelnen davon.

## Die drei Menüs, die Sie verwenden werden

Flacbox hält seine Klangwerkzeuge an drei Orten bereit, alle innerhalb der Audio-Player-Einstellungen. Stellen Sie zunächst sicher, dass Ihre **Wiedergabe-Engine** auf **Sound FX** eingestellt ist (Einstellungen > Audio-Player > Wiedergabe-Engine), denn die Effekte, der Equalizer und die DSP-Kette sind nur mit dieser Engine verfügbar.

- **Audioeffekte** (das Effekt-Rack): Öffnen Sie den Player, tippen Sie auf **⋯ (Weitere Aktionen)**, tippen Sie auf **Audioeffekte**. Oder gehen Sie zu **Einstellungen > Audio-Player > Audioeffekte**.
- **Audio-Equalizer** (10 Bänder und Presets): **Einstellungen > Audio-Player > Audio-Equalizer**.
- **Signalverarbeitung** (Ihre eigene DSP-Kette): **Einstellungen > Audio-Player > Signalverarbeitung**.

Sie können außerdem die **Ausgabe-Abtastrate**, die **Kanäle** und die **Puffergröße** unter **Einstellungen > Audio-Player** festlegen.

## Der 10-Band-Equalizer

**Was er macht:** Verändert den Klangcharakter der Musik, von tiefem Bass bis zu hellen Höhen. Dies ist das beste Werkzeug für einen sauberen **Bass-Boost** oder ein helleres, klareres oberes Ende. Stellen Sie ihn sich als zehn Lautstärkeregler vor, jeder für einen anderen Ausschnitt des Klangs. Heben Sie ein Band an, um diesen Teil nach vorn zu holen, senken Sie es, um ihn zurückzunehmen. Kleine Änderungen von wenigen dB klingen meist am besten, und er wirkt auf alles, was Sie abspielen.

**Wie er funktioniert:** Zehn Regler bei **32, 64, 125, 250, 500 Hz und 1, 2, 4, 8, 16 kHz**. Jeder reicht von **-12 dB (Absenkung)** bis **+12 dB (Anhebung)**. Es gibt außerdem einen **Vorverstärker** von **-24 bis +24 dB** für den Gesamtpegel. Sie können eigene Presets speichern und sie zwischen Geräten **exportieren oder importieren**.

**Was jedes eingebaute Preset macht (22 Presets):**

| Preset | Was es mit Ihrem Klang macht |
|---|---|
| **Flat** | Keine Änderung. Alle Bänder auf null. Ein sauberer Ausgangspunkt. |
| **Acoustic** | Warmer Bass und knackige, präsente Höhen. Lässt Akustikgitarren und Stimmen natürlich und lebendig wirken. |
| **Bass Booster** | Starke Anhebung im Tiefton, Mitten und Höhen unberührt. Mehr Punch und Gewicht. |
| **Bass Reducer** | Senkt den Tiefton. Praktisch für dröhnende Räume, günstige Ohrhörer oder basslastige Titel. |
| **Treble Booster** | Hebt nur die Höhen an. Fügt Glanz und Luftigkeit hinzu, mehr Details. |
| **Treble Reducer** | Mildert die Höhen. Zähmt harsche oder scharfe Aufnahmen. |
| **Classical** | Volle Tiefen und sanfte Höhen mit einer leichten Mittenabsenkung. Weich und geräumig für Orchestermusik. |
| **Dance** | Große Tiefen und helle Höhen mit ausgehöhlten Mitten. Druckvoll und energiegeladen für Club-Titel. |
| **Deep** | Warmer, dicker Tiefton mit weicheren Höhen. Ein gemütlicher, entspannter Klang. |
| **Electronic** | Starker Bass und helle Höhen für Synths und Beats. Weit und modern. |
| **Hip-Hop** | Kräftiger Bass und klare Höhen mit kontrollierten Mitten. Gewichtig und druckvoll. |
| **Jazz** | Warm und weich, mit einer kleinen Mittenabsenkung. Locker und natürlich für akustischen Jazz. |
| **Latin** | Angehobene Tiefen und Höhen mit sauberen Mitten. Hell und lebendig. |
| **Loudness** | Hebt Bass und Höhen stark an (eine «Lächeln»-Kurve). Klingt bei niedriger Lautstärke voller. |
| **Lounge** | Nach vorn geholte Mitten mit weichen Kanten. Entspannt und stimmenfreundlich. |
| **Piano** | Klare Mitten und Höhen, damit Klaviernoten sauber erklingen. |
| **Pop** | Angehobene Mitten für Stimmen, mit zurückgenommenen Tiefen und Höhen. Stimmen sitzen vorn. |
| **R&B** | Sehr starke Tief-Mitten-Wärme und klare Höhen. Weich und satt. |
| **Rock** | Angehobene Tiefen und Höhen für Gitarren und Schlagzeug. Energiegeladen und voll. |
| **Small Speakers** | Hebt Tiefen an und senkt Höhen, damit winzige Lautsprecher voller klingen. |
| **Spoken Word** | Hebt den Stimmbereich an und senkt den tiefen Bass. Macht Sprache klar. |
| **Vocal Booster** | Drückt die Mitte hoch, wo Stimmen liegen, senkt drumherum. Vocals stechen heraus. |

**Tipp für Bass:** Beginnen Sie mit **Bass Booster**, und wenn es matschig klingt, ziehen Sie den Vorverstärker um 1 bis 2 dB nach unten, damit nichts verzerrt.

## Lautstärkenormalisierung (gleichmäßige Lautheit)

**Was sie macht:** Manche Songs spielen lauter als andere, sodass Sie ständig die Lautstärke ändern. Dies lässt jeden Song von selbst etwa gleich laut spielen, damit Sie es nicht tun müssen. Sie ist perfekt für gemischte Wiedergabelisten im Zufallsmodus, die alte und neue Aufnahmen, verschiedene Alben oder verschiedene Quellen mischen, bei denen ein Titel viel lauter als der nächste sein kann.

**Wie sie funktioniert:** Sie hört die tatsächliche Lautheit jedes Titels nach dem **EBU R128**-Standard ab (gemessen in **LUFS**, dieselbe Idee, die Streaming-Dienste verwenden) und passt dann jeden Titel an Ihr Ziel an. Sie benötigt keine Tags in Ihren Dateien und verändert das Audio nie. EBU R128 misst die Lautheit, die Ihre Ohren über den ganzen Song hinweg tatsächlich wahrnehmen, nicht nur die höchste Spitze, weshalb sie damit übereinstimmt, wie laut Titel Ihnen wirklich erscheinen. Flacbox ermittelt das live während der Wiedergabe (und prüft die Lautheit im Voraus, wenn es kann) und wendet dann eine einzige, gleichmäßige Lautstärkeänderung auf den Titel an. Die Grenze **Max. Anhebung** verhindert, dass sehr leise Aufnahmen so stark hochgezogen werden, dass sie verzerren. Da sie den Klang selbst liest, funktioniert sie bei jeder Quelle, einschließlich Cloud-Dateien, Live-Streams und Modulmusik, selbst wenn die Dateien überhaupt keine Lautheits-Tags haben.

**Regler:**

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Ziel-Lautheit** | Legt die Lautheit fest, auf die jeder Titel eingepegelt wird. Höhere Werte lassen alles insgesamt lauter spielen. | -30 bis -6 LUFS (-16) |
| **Max. Anhebung** | Begrenzt, wie stark leise Titel verstärkt werden können. Höhere Werte bringen leise Aufnahmen näher ans Ziel. | 0 bis 24 dB (12) |

**Presets:**

| Preset | Was es macht |
|---|---|
| **Light** | Sanftes Einpegeln für gelegentliches Hören. Gleicht offensichtliche Lautstärkesprünge aus, ohne leise Titel stark hochzudrücken. |
| **Standard** | Der Allzweck-Standard. Ein Lautheitsziel im Streaming-Stil, das zu den meisten Musikstücken passt. Beginnen Sie hier. |
| **Strong** | Aggressives Anpassen, das leise Titel kräftig hochdrückt. Am besten für gemischte Bibliotheken mit großen Pegelunterschieden. |
| **Night** | Ein insgesamt leiseres Ziel, das leise Passagen dennoch anhebt, damit spätnächtliches Hören gleichmäßig und leise bleibt. |

## Compressor (laute und leise Teile ausgleichen)

**Was er macht:** In einem Song können die leisen Teile zu leise und die lauten Teile zu laut sein. Dies bringt sie näher zusammen, sodass der ganze Song leicht zu hören ist, selbst im Auto oder an einem lauten Ort. Er dreht die lautesten Momente sanft herunter und hebt die leiseren an, damit Sie während eines einzelnen Titels nicht mehr zur Lautstärke greifen. Das unterscheidet sich von der Lautstärkenormalisierung: Der Compressor gleicht die Dinge **innerhalb** eines Songs aus, während die Lautstärkenormalisierung die Lautheit **zwischen** Songs angleicht. Beide arbeiten gut zusammen. Beginnen Sie mit einem Preset und öffnen Sie die Regler nur, wenn Sie mehr Kontrolle möchten.

**Regler:**

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Threshold** | Der Pegel, bei dem die Kompression einsetzt. Niedrigere Werte stauchen mehr vom Klang und halten leise und laute Teile näher zusammen. | -60 bis 0 dB (-20) |
| **Ratio** | Wie stark die lauten Teile zurückgehalten werden, sobald sie den Schwellenwert überschreiten. Höhere Werte komprimieren härter und halten den Klang gleichmäßiger. | 1:1 bis 30:1 (4:1) |
| **Attack** | Wie schnell der Effekt auf eine plötzliche laute Spitze reagiert. Kurze Werte fangen Transienten ab; längere lassen sie durch. | 0,1 bis 1000 ms (10 ms) |
| **Release** | Wie schnell der Effekt loslässt, nachdem der laute Teil vorbei ist. Kurze Werte können pumpen; längere klingen weicher. | 10 ms bis 5 s (100 ms) |
| **Master-Gain** | Endgültige Ausgangsanhebung nach der Verarbeitung. Erhöhen Sie diesen, um die Gesamtlautheit anzuheben, sobald die Dynamik ausgeglichen ist. | -30 bis +30 dB (0) |

**Presets:**

| Preset | Was es macht |
|---|---|
| **Transparent** | Kaum spürbares Sicherheitsnetz. Bewahrt die Dynamik nahezu vollständig und fängt nur die lautesten Spitzen ab. |
| **Soft** | Leichtes Einpegeln für Hi-Fi-Hören zu Hause. Dezente Glättung, ohne die Musik zu stauchen. |
| **Standard** | Vernünftiger Standard für die alltägliche Musikwiedergabe. Das erste Preset zum Ausprobieren. |
| **Heavy** | Aggressives Ausgleichen für laute Umgebungen. Auto, überfüllter Raum, Hören bei niedriger Lautstärke. |
| **Voice / Podcast** | Auf Sprache abgestimmt. Langsameres Attack lässt Zischlaute durch, großzügiges Makeup-Gain zieht Vocals hoch. |
| **Old Recordings** | Alte Alben und restauriertes Vinyl, deren Durchschnittspegel unter modernen Veröffentlichungen liegt. |
| **Late Night** | Starke Kompression plus große Anhebung für leises Hören, wenn Nachbarn oder schlafende Familie eine Rolle spielen. |
| **Movie Dialog** | Bringt gesprochenes Wort gegenüber Musik und Soundeffekten in einem abwechslungsreichen Soundtrack nach vorn. |
| **Streaming Match** | Zielt etwa auf die Lautheitsnormalisierung moderner Streaming-Dienste rund um -14 LUFS. |
| **Maximum Loudness** | Volles Programm. Erreicht den Limiter; erwarten Sie ein gestauchtes, sehr gleichmäßiges Signal. Das buchstäbliche Maximallautstärke-Preset. |

## Freeverb (Hall, ein Raumgefühl)

**Was er macht:** Fügt der Musik ein Raumgefühl hinzu, von einem kleinen Zimmer bis zu einer großen Halle. Wählen Sie ein Preset oder stimmen Sie das Dry- und Wet-Mischungsverhältnis, die Raumgröße, Dämpfung und Breite selbst ab. Hall ist das natürliche Echo, das Sie in jedem realen Raum hören, und Freeverb bildet es in Software nach. Ein wenig lässt flache oder nah mikrofonierte Aufnahmen offener und lebendiger wirken. Viel platziert die Musik in einem großen, entfernten Raum. Es ist ein kreativer Effekt, halten Sie die Wet-Mischung also für natürliche Ergebnisse moderat.

**Regler:**

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Dry mix** | Wie viel des ursprünglichen, unberührten Klangs erhalten bleibt. Höhere Werte belassen mehr vom trockenen Signal in der Mischung. | 0 bis 1 (0,0) |
| **Wet mix** | Wie viel des verhallten Klangs hinzugefügt wird. Höhere Werte machen den Hall lauter und deutlicher. | 0 bis 3 (1,0) |
| **Room size** | Die Größe des vorgestellten Raums. Höhere Werte ergeben eine längere, größere Hallfahne, von einem kleinen Zimmer bis zu einer Kathedrale. | 0 bis 1 (0,5) |
| **Damp** | Wie schnell die hohen Frequenzen in der Fahne verklingen. Höhere Werte machen den Hall dunkler und wärmer. | 0 bis 1 (0,5) |
| **Width** | Die Stereobreite des Halls. Höhere Werte lassen den Raum breiter zwischen dem linken und rechten Kanal wirken. | 0 bis 1 (1,0) |

**Presets:**

| Preset | Was es macht |
|---|---|
| **Room** | Ein kleiner, enger Raum. Dezente Atmosphäre, die ein Ortsgefühl hinzufügt, ohne den Klang auszuwaschen. |
| **Studio** | Ein trockener, kontrollierter Aufnahmeraum. Gerade genug Reflexion, um natürlich zu klingen. |
| **Hall** | Ein großer Konzertsaal. Eine lange, üppige Fahne, die zu Orchester- und Akustikmusik passt. |
| **Cathedral** | Ein riesiger, hallender Steinraum. Die längste, dramatischste Hallfahne. |
| **Plate** | Ein heller, dichter Studio-Plattenhall. Klassisch für Vocals und Schlagzeug. |
| **Ambience** | Eine kurze, luftige Atmosphäre. Fügt ein leichtes Raumgefühl hinzu und bleibt dabei überwiegend trocken. |

## Auto Wah (funkiger Filtersweep)

**Was er macht:** Ein Filter, der von selbst auf und ab schwingt für einen funkigen, stimmartigen Wah-Klang. Wählen Sie ein Preset oder stellen Sie Wet-Mischung, Feedback, Rate, Bereich und Frequenz selbst ein. Es ist derselbe «Wah»-Sweep, den ein Gitarren-Wah-Pedal erzeugt, aber hier bewegt er sich von selbst im Takt der Musik. Er klingt großartig bei Funk-, Disco- und Elektronik-Titeln. Es ist ein kräftiger, deutlicher Effekt, ein wenig reicht beim alltäglichen Hören also weit.

**Regler:**

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Wet mix** | Wie stark der Wah-Effekt in der Mischung ist. Höhere Werte machen den schwingenden Filter deutlicher. | -2 bis +2 (1,5) |
| **Feedback** | Wie viel des Ausgangs in den Effekt zurückgeführt wird. Höhere Werte machen das Wah resonanter und ausgeprägter. | -1 bis +1 (0,5) |
| **Rate** | Wie schnell der Filter auf und ab schwingt. Höhere Werte ergeben ein schnelleres, rhythmischeres Wah. | 0,1 bis 9 Hz (2,0) |
| **Range** | Wie weit der Filter schwingt, in Oktaven. Höhere Werte ergeben einen breiteren, dramatischeren Sweep. | 0,1 bis 9 Oktaven (4,3) |
| **Frequency** | Die Grundfrequenz, um die der Filter schwingt. Niedrigere Werte klingen tiefer; höhere klingen heller. | 1 bis 1000 Hz (50) |

**Presets:**

| Preset | Was es macht |
|---|---|
| **Classic** | Ein ausgewogener, klassischer Wah-Sweep. Ein guter Ausgangspunkt für Funk und Rock. |
| **Slow** | Ein langsamer, breiter Sweep, der sanft auf und ab treibt. Ideal für Pads und lange Noten. |
| **Funky** | Ein schneller, druckvoller Sweep mit viel Bewegung. Fügt Gitarren und Synths rhythmischen Biss hinzu. |
| **Deep** | Ein tiefer, breiter Sweep, der bei einer niedrigen Frequenz beginnt. Groß und dramatisch. |
| **Subtle** | Eine sanfte, zurückhaltende Bewegung. Fügt Charakter hinzu, ohne den Klang zu dominieren. |
| **Resonant** | Ein scharfes, resonantes Wah mit hohem Feedback. Stimmartig und ausdrucksstark. |

## Phaser (wirbelndes Rauschen)

**Was er macht:** Ein schwingender Filter, der dem Klang eine wirbelnde, rauschende Bewegung hinzufügt. Wählen Sie ein Preset oder stellen Sie Feedback, Rate, Bereich und Frequenz selbst ein. Er fügt sanfte Bewegung und Schimmer hinzu, ohne die Noten zu verändern. Er ist dezent bei Vocals und Pads und dramatisch bei Synths und Gitarren. Probieren Sie Slow für ein verträumtes Gefühl oder Jet für einen kräftigen Wirbel.

**Regler:**

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Feedback** | Wie viel des Ausgangs in den Effekt zurückgeführt wird. Höhere Werte machen den Phaser resonanter und ausgeprägter. | -1 bis +1 (0,0) |
| **Rate** | Wie schnell der Filter auf und ab schwingt. Höhere Werte ergeben ein schnelleres, rhythmischeres Phasing. | 0,1 bis 9 Hz (1,0) |
| **Range** | Wie weit der Filter schwingt, in Oktaven. Höhere Werte ergeben einen breiteren, dramatischeren Sweep. | 0,1 bis 9 Oktaven (4,0) |
| **Frequency** | Die Grundfrequenz, um die der Filter schwingt. Niedrigere Werte klingen tiefer; höhere klingen heller. | 1 bis 1000 Hz (100) |

**Presets:**

| Preset | Was es macht |
|---|---|
| **Classic** | Ein ausgewogener, klassischer Phaser-Sweep. Ein guter Ausgangspunkt für Gitarren und Keys. |
| **Slow** | Ein langsamer, breiter Sweep, der sanft auf und ab treibt. Ideal für Pads und lange Noten. |
| **Fast** | Ein schneller, schimmernder Sweep mit viel Bewegung. Fügt Bewegung und Energie hinzu. |
| **Deep** | Ein tiefer, breiter Sweep, der bei einer niedrigen Frequenz beginnt. Groß und dramatisch. |
| **Subtle** | Eine sanfte, zurückhaltende Bewegung. Fügt Charakter hinzu, ohne den Klang zu dominieren. |
| **Jet** | Ein intensiver, resonanter Sweep mit hohem Feedback, das klassische Düsenflugzeug-Rauschen. |

## Flanger (Düsenflugzeug-Sweep)

**Was er macht:** Ein kurzes, bewegtes Delay, das dem Klang ein düsenartiges, schwingendes Rauschen verleiht. Wählen Sie ein Preset oder stellen Sie Tiefe, Feedback, Rate und Delay selbst ein. Er ist ein stärkerer, metallischerer Vetter des Phasers, berühmt für den rauschenden Sweep im klassischen Rock und in der elektronischen Musik. Dezente Einstellungen fügen sanfte Bewegung hinzu, während tiefe Einstellungen dramatisch und deutlich sind. Am besten sparsam eingesetzt, als Effekt.

**Regler:**

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Depth** | Wie stark der schwingende Effekt ist. Höhere Werte machen das Flanging deutlicher. | 0 bis 100 % (25) |
| **Feedback** | Wie viel des Ausgangs in den Effekt zurückgeführt wird. Höhere Werte machen den Flanger resonanter und metallischer. | -99 bis +99 % (-50) |
| **Rate** | Wie schnell sich der Sweep auf und ab bewegt. Höhere Werte ergeben eine schnellere, schimmerndere Bewegung. | 0 bis 10 Hz (0,25) |
| **Delay** | Die Grund-Delayzeit, auf der der Sweep aufbaut. Höhere Werte ergeben einen tieferen, hohleren Charakter. | 0 bis 4 ms (2,0) |

**Presets:**

| Preset | Was es macht |
|---|---|
| **Classic** | Ein ausgewogener, klassischer Flanger. Ein guter Ausgangspunkt für Gitarren und Keys. |
| **Subtle** | Ein sanfter, zurückhaltender Sweep. Fügt Bewegung hinzu, ohne den Klang zu dominieren. |
| **Deep** | Ein tiefer, kräftiger Sweep mit starkem Feedback. Groß und dramatisch. |
| **Jet** | Ein intensiver Sweep mit positivem Feedback, das klassische Düsenflugzeug-Rauschen. |
| **Fast** | Ein schneller, schimmernder Sweep mit viel Bewegung und Energie. |
| **Wide** | Ein langsamer, breiter Sweep mit langem Delay. Üppig und geräumig. |

## Echo (Wiederholungen)

**Was es macht:** Wiederholt den Klang als verklingende Echos für ein Raum- und Tiefengefühl. Wählen Sie ein Preset oder stellen Sie Wet-Mischung, Feedback und Delay selbst ein. Es ist wie ein Ruf in einem Canyon: Der Klang kommt nach einer kurzen Pause ein- oder mehrmals zurück. Eine einzelne kurze Wiederholung fügt Körper und ein Retro-Gefühl hinzu, während längere Wiederholungen mit mehr Feedback geräumige, nachhallende Fahnen erzeugen. Das Ping-Pong-Preset lässt die Wiederholungen zwischen Ihrem linken und rechten Ohr springen, was mit Kopfhörern Spaß macht. Halten Sie die Wet-Mischung moderat, damit die Echos die Musik unterstützen, statt sie zu überdecken.

**Regler:**

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Wet mix** | Wie laut die Echos im Vergleich zum Originalklang sind. Höhere Werte lassen die Wiederholungen stärker hervortreten. | -2 bis +2 (0,6) |
| **Feedback** | Wie oft sich das Echo wiederholt. Höhere Werte ergeben mehr Wiederholungen, die länger zum Verklingen brauchen. | -1 bis +1 (0,5) |
| **Delay** | Die Zeit zwischen den Echos. Kürzere Werte ergeben ein enges Slapback; längere ergeben weit auseinanderliegende Wiederholungen. | 0,01 bis 2 s (0,4) |

**Presets:**

| Preset | Was es macht |
|---|---|
| **Slapback** | Eine einzelne, enge Wiederholung direkt hinter dem Klang. Klassisches Rockabilly-Slapback. |
| **Room** | Ein kurzes, natürliches Echo wie in einem kleinen Raum. Fügt Raum hinzu, ohne den Klang zu verwischen. |
| **Tape** | Warme, mittellange Wiederholungen, die allmählich verklingen, wie ein altes Bandecho. |
| **Dub** | Lange, kräftige Wiederholungen mit starkem Feedback. Groß, dubbig und geräumig. |
| **Ping Pong** | Echos springen zwischen dem linken und rechten Lautsprecher für einen breiten Stereoeffekt. |
| **Long** | Langsame, weit auseinanderliegende Wiederholungen, die weit hinter dem Klang ausklingen. |

## Chorus (dickerer, breiterer Klang)

**Was er macht:** Verdickt und verbreitert den Klang, indem er eine verschobene Kopie über das Original legt. Wählen Sie ein Preset oder stellen Sie das Wet/Dry-Mischungsverhältnis, die Tiefe, Rate und das Feedback selbst ein. Er lässt ein Instrument oder eine Stimme wie mehrere klingen, die zusammen spielen, indem er leicht verstimmte, bewegte Kopien hinzufügt. Das fügt Fülle und einen sanften Schimmer hinzu. Dezente Einstellungen wärmen den Klang, während starke Einstellungen üppig und verträumt klingen. Er ist beliebt bei Gitarren, Keyboards und Vocals.

**Regler:**

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Wet/Dry** | Wie viel des Chorus Sie im Vergleich zum Originalklang hören. Höhere Werte machen den Effekt deutlicher. | 0 bis 100 % (50) |
| **Depth** | Wie weit die Tonhöhe auf und ab schwankt. Höhere Werte ergeben einen dickeren, schimmernderen Klang. | 0 bis 100 % (25) |
| **Rate** | Wie schnell sich der Schimmer bewegt. Langsamere Raten klingen sanft und üppig; schnellere Raten klingen eher wie Vibrato. | 0 bis 10 Hz (1,1) |
| **Feedback** | Wie viel des Effekts in sich selbst zurückgeführt wird. Höhere Werte machen den Chorus resonanter und intensiver. | -99 bis +99 % (25) |

**Presets:**

| Preset | Was es macht |
|---|---|
| **Subtle** | Eine sanfte Verdickung, die Wärme hinzufügt, ohne die Aufmerksamkeit auf sich zu ziehen. |
| **Lush** | Ein satter, klassischer Chorus. Eine großartige Allround-Einstellung für Gitarren und Keys. |
| **Ensemble** | Ein voller, geschichteter Schimmer, der ein einzelnes Instrument wie mehrere klingen lässt. |
| **Vibrato** | Vollständig wet mit einer schnellen Rate, für ein zitterndes Vibrato statt eines dezenten Chorus. |
| **Wide** | Ein langsamer, breiter Schimmer, der das Stereobild öffnet. Geräumig und verträumt. |
| **Twelve-String** | Ein heller, resonanter Schimmer, der an eine zwölfsaitige Gitarre erinnert. |

## Distortion (Grit und Kante)

**Was sie macht:** Fügt Grit und Kante hinzu, indem sie den Klang übersteuert. Wählen Sie ein Preset oder stellen Sie Drive, Ausgang und Klangfarbe selbst ein. Sie raut den Klang bewusst auf, von einer warmen, körnigen Kante bis zu einem gebrochenen, fuzzigen Ton. Es ist ein kreativer Spaßeffekt statt eine Möglichkeit, die Qualität zu verbessern, verwenden Sie sie also in kleinen Mengen. Sie macht Spaß bei elektronischen, Rock- und experimentellen Titeln. Senken Sie den Ausgang, wenn ein kräftiges Preset zu laut wird.

**Regler:**

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Drive** | Wie stark der Klang verzerrt wird. Höhere Werte sind körniger und aggressiver. | 0 bis 100 % (15) |
| **Output** | Der Ausgangspegel nach der Verzerrung. Senken Sie ihn, wenn eine kräftige Einstellung zu laut wird. | -60 bis 0 dB (-18) |
| **Tone** | Rollt die Höhen vor der Verzerrung ab. Niedrigere Werte klingen dunkler und wärmer. | 100 bis 8000 Hz (8000) |
| **Center** | Um welche Frequenz die Verzerrung zentriert ist. Verschiebt den Charakter heller oder dunkler. | 100 bis 8000 Hz (2400) |
| **Width** | Wie breit dieser Fokus ist. Schmal klingt scharf und nasal; breit klingt voll und offen. | 100 bis 8000 Hz (2400) |

**Presets:**

| Preset | Was es macht |
|---|---|
| **Warm Drive** | Ein leichter, warmer Grit, der Kante hinzufügt, ohne den Charakter stark zu verändern. |
| **Crunch** | Ein klassischer, knackiger Overdrive, druckvoll und rhythmisch. |
| **Overdrive** | Ein heller, angetriebener Ton mit viel Biss. Ideal für Lead-Sounds. |
| **Fuzz** | Ein dicker, gesättigter Fuzz. Kräftig und voller Obertöne. |
| **Metal** | Ein enger, mittenfokussierter High-Gain-Ton für aggressive, kräftige Sounds. |
| **Screamer** | Ein mittenangehobener Overdrive, der sich durchsetzt, wie ein Tube Screamer. |
| **LoFi** | Eine zerdrückte, schmalbandige Verzerrung für einen körnigen Lo-Fi-Charakter. |

## Rotate (rotierendes Stereo)

**Was es macht:** Dreht den Klang um das Stereofeld für einen rotierenden, wirbelnden Effekt. Wählen Sie ein Preset oder stellen Sie die Rate selbst ein. Es bewegt den Klang langsam um Ihren linken und rechten Kanal, ein wenig wie ein drehender Lautsprecher, was ein wirbelndes, hypnotisches Gefühl hinzufügt. Langsame Einstellungen sind sanft und breit, während schnelle Einstellungen schwindelig und deutlich sind. Es ist ein Stereoeffekt, daher ist er am deutlichsten mit Kopfhörern oder gut platzierten Lautsprechern.

**Regler:**

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Rate** | Wie schnell sich der Klang um das Stereofeld dreht. Negative Werte drehen in die andere Richtung; null hält ihn still. | -5 bis +5 Hz (1,0) |

**Presets:**

| Preset | Was es macht |
|---|---|
| **Slow Pan** | Ein langsames, sanftes Treiben von Seite zu Seite. Dezent und breit. |
| **Sway** | Ein gleichmäßiges Links-Rechts-Schwanken. Fügt dem Stereobild sanfte Bewegung hinzu. |
| **Rotary** | Eine mittlere Drehung, die an einen Rotationslautsprecher erinnert. |
| **Fast Spin** | Eine schnelle Drehung um das Stereofeld für einen schwindeligen, wirbelnden Effekt. |
| **Reverse** | Eine mittlere Drehung in die entgegengesetzte Richtung. |
| **Whirl** | Ein sehr schneller Wirbel. Intensiv und desorientierend. |

## Crossfeed (natürlicher Klang auf Kopfhörern)

Auf Lautsprechern hört jedes Ihrer Ohren sowohl den linken als auch den rechten Lautsprecher, nur zu leicht unterschiedlichen Zeiten und Lautstärken. Auf Kopfhörern ist diese natürliche Vermischung verschwunden: Ihr linkes Ohr hört nur den linken Kanal und Ihr rechtes Ohr nur den rechten. Dieses «Super-Stereo» kann Musik so wirken lassen, als sei sie in Ihrem Kopf aufgeteilt, und hart gepannte Aufnahmen, bei denen ein Instrument vollständig auf einer Seite sitzt, können bei langem Hören unnatürlich oder ermüdend wirken.

Crossfeed behebt das, indem es eine kleine, gefilterte Menge jedes Kanals in den anderen mischt, mit einer winzigen Verzögerung und einem sanften Abfall der hohen Frequenzen. Das kommt dem nahe, wie Klang von echten Lautsprechern beide Ihrer Ohren erreicht, einschließlich der Art, wie Ihr Kopf das entfernte Ohr leicht abschattet. Das Ergebnis ist ein natürlicheres, lautsprecherähnliches Bild, das ein wenig vor Ihnen statt in Ihrem Kopf sitzt, und es reduziert die Hörermüdung bei langen Sitzungen. Flacbox verwendet die bekannte **bs2b-Methode (Bauer stereophonic-to-binaural)**, ein angesehenes Open-Source-Crossfeed, das von vielen audiophilen Playern genutzt wird. Über den Algorithmus können Sie auf der [bs2b-Projektseite](https://bs2b.sourceforge.net/) lesen.

Der **Cutoff** steuert, wie warm die Mischung klingt, und der **Feed level** steuert, wie stark sie ist. Die Presets decken die klassischen bs2b-Stufen ab, von einem kaum spürbaren Hauch bis zu einer festen, lautsprecherähnlichen Mischung. Crossfeed ist ein Kopfhörereffekt, lassen Sie ihn also aus, wenn Sie über Lautsprecher hören.

**Regler:**

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Cutoff** | Legt fest, wo das Überkoppeln zwischen den Kanälen abzufallen beginnt. Niedrigere Werte ergeben einen wärmeren, ausgeprägteren Effekt. | 300 bis 2000 Hz (700) |
| **Feed level** | Steuert, wie viel eines Kanals in den anderen überkoppelt. Höhere Werte erzeugen einen lautsprecherähnlicheren Klang. | 1 bis 15 dB (4,5) |

**Presets:**

| Preset | Was es macht |
|---|---|
| **Subtle** | Kaum spürbares Crossfeed für gelegentliches Hören. Mildert hart gepanntes Stereo, ohne die tonale Balance zu verändern. |
| **Chu Moy** | Der klassische Allzweck-Standard. Ausgewogen und leicht warm, funktioniert bei fast jedem Material. Beginnen Sie hier. |
| **Strong** | Stärkeres Überkoppeln für härter gepannte Mischungen. Deutlichere Stereo-Verengung. |
| **Jan Meier** | Beliebt bei Kopfhörer-Enthusiasten. Breiteres Feed, lautsprecherähnlichere Darstellung, leichte Bassanhebung. |
| **Speaker-like** | Abgestimmt auf die natürlichste lautsprecherartige Wiedergabe über Kopfhörer. |
| **Vintage Stereo** | Aggressives Crossfeed, abgestimmt auf Mischungen der 1960er und 1970er mit hart gepanntem Schlagzeug und Gesang. |

## Signalverarbeitung: Bauen Sie Ihre eigene DSP-Kette

Über die fertigen Effekte hinaus lässt Flacbox Sie Ihre eigene Kette unter **Einstellungen > Audio-Player > Signalverarbeitung** bauen. Wie die App erklärt, wenn die Kette leer ist: *«Tippen Sie auf +, um einen Effekt hinzuzufügen. Schalten Sie jeden mit seinem Schalter ein oder aus, ziehen Sie zum Umsortieren, tippen Sie, um seine Parameter zu bearbeiten, und halten Sie lange gedrückt, um zu duplizieren oder zu löschen.»*

Die **Reihenfolge ist wichtig**: Ein Filter vor einer Verzerrung klingt anders als derselbe Filter danach. Sie können die gesamte Kette auch auf **Alle Kanäle**, **Linker Kanal** oder **Rechter Kanal** richten.

Unten steht jeder Block, mit dem eigenen Text der App für jeden Regler und jedes Preset.

### Gain (Pegel-Trim)

Hebt oder senkt den Pegel an einem Punkt in der Kette.

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Gain** | Hebt oder senkt den Pegel an diesem Punkt in der Kette. Verwenden Sie ihn, um nach anderen Effekten Pegel auszugleichen oder die folgenden anzutreiben. | -24 bis +24 dB (0) |

| Preset | Was es macht |
|---|---|
| **Unity** | Keine Pegeländerung. Ein neutraler Ausgangspunkt. |
| **Cut** | Eine große Absenkung. Zähmt eine laute Quelle oder schafft Platz vor den folgenden Effekten. |
| **Trim** | Eine sanfte Absenkung, um den Pegel etwas zurückzunehmen. |
| **Lift** | Eine moderate Anhebung, um eine leise Quelle anzuheben. |
| **Boost** | Eine starke Anhebung für leises Material oder um die folgenden Effekte härter anzutreiben. |
| **Max** | Maximale Anhebung. Laut, achten Sie später in der Kette auf Clipping. |

### Low Pass (entfernt Höhen)

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Cutoff** | Legt fest, wo der Filter beginnt, die Höhen abzurollen. Senken Sie ihn, um den Klang zu verdunkeln und zu erweichen; heben Sie ihn nach oben, um voll zu öffnen. | 20 Hz bis 20 kHz (20 kHz) |
| **Resonance** | Betont die Frequenzen genau am Cutoff. Halten Sie sie niedrig für einen sauberen Abfall; erhöhen Sie sie für eine spitze, pfeifende Kante. | 0,1 bis 10 (0,707) |

| Preset | Was es macht |
|---|---|
| **Air** | Beschneidet nur die allerhöchsten Höhen. Nimmt etwas Kante, ohne den Klang zu dämpfen. |
| **Warm** | Ein sanftes Abrollen der Höhen für einen wärmeren, runderen Ton. |
| **Mellow** | Deutlich weicher. Nimmt die Helligkeit zurück für ein entspanntes Gefühl. |
| **Muffled** | Dunkel und gedämpft, als würde man durch eine Wand hören. |
| **Telephone** | Eine schmale, resonante Spitze im unteren Bereich. Eine dünne, telefonartige Stimme. |

### High Pass (entfernt Tiefen)

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Cutoff** | Legt fest, wo der Filter beginnt, die Tiefen abzurollen. Heben Sie ihn, um den Tiefton auszudünnen und Rumpeln zu entfernen; senken Sie ihn nach unten, um voll zu öffnen. | 20 Hz bis 20 kHz (20 Hz) |
| **Resonance** | Betont die Frequenzen genau am Cutoff. Halten Sie sie niedrig für einen sauberen Abfall; erhöhen Sie sie für eine spitze, pfeifende Kante. | 0,1 bis 10 (0,707) |

| Preset | Was es macht |
|---|---|
| **Rumble Cut** | Entfernt subsonisches Rumpeln und DC-Offset, ohne den hörbaren Tiefton anzutasten. |
| **Tighten** | Beschneidet dröhnende Tieffrequenzen für einen strafferen, saubereren Bass. |
| **Thin** | Senkt Wärme und Körper und lässt einen leichteren, dünneren Klang. |
| **Radio** | Nur die Mitten und Höhen bleiben, wie ein kleiner Radiolautsprecher. |
| **Telephone** | Eine schmale, resonante Spitze im oberen Bereich. Eine dünne, telefonartige Stimme. |

### Band Pass (behält ein mittleres Band)

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Center** | Legt die Frequenz fest, die der Filter durchlässt. Alles darüber und darunter wird abgerollt. Fahren Sie ihn durch, um Bass, Mitten oder Höhen herauszupicken. | 20 Hz bis 20 kHz (1 kHz) |
| **Resonance** | Steuert, wie breit das Band ist. Niedrige Werte lassen einen breiten Bereich durch; erhöhen Sie sie, um sich für einen scharfen, resonanten Ton auf das Zentrum zu verengen. | 0,1 bis 10 (0,707) |

| Preset | Was es macht |
|---|---|
| **Voice** | Ein breites Band um die Mitten, wo die meisten Vocals sitzen. Ein neutraler Ausgangspunkt. |
| **Bass** | Isoliert den Tiefton und lässt nur Bass und Kick. |
| **Body** | Fokussiert auf die Tief-Mitten für einen warmen, kastigen Körper. |
| **Presence** | Hebt die Ober-Mitten für Klarheit und Präsenz an. |
| **Telephone** | Ein schmales Mittenband. Ein dünner, telefonartiger Klang. |
| **Wah** | Eine sehr schmale, resonante Spitze. Fahren Sie das Zentrum durch für einen Wah-Effekt. |

### Notch (entfernt ein schmales Band)

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Frequency** | Legt die Frequenz fest, die der Filter entfernt. Alles darüber und darunter passiert. Stimmen Sie ihn auf ein Brummen oder eine Resonanz ab, um sie herauszuschneiden. | 20 Hz bis 20 kHz (60 Hz) |
| **Resonance** | Steuert, wie breit die Absenkung ist. Niedrige Werte höhlen einen breiten Bereich aus; erhöhen Sie sie, um nur ein punktgenaues Band zu entfernen und den Rest unberührt zu lassen. | 0,1 bis 10 (8,0) |

| Preset | Was es macht |
|---|---|
| **Mains Hum 60** | Entfernt 60-Hz-Netzbrummen (nordamerikanisches Netz). Ein neutraler Ausgangspunkt. |
| **Mains Hum 50** | Entfernt 50-Hz-Netzbrummen (europäisches und anderes Netz). |
| **Rumble** | Schneidet ein tieffrequentes Rumpeln oder eine Resonanz aus, ohne das ganze untere Ende auszudünnen. |
| **Mud** | Höhlt Tief-Mitten-Matsch aus für einen saubereren, klareren Klang. |
| **Boxy** | Entfernt ein kastiges Mitten-Dröhnen. |
| **Harsh** | Zähmt eine harsche, durchdringende Spitze in den Ober-Mitten. |

### Peaking (parametrisches EQ-Band)

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Frequency** | Das Zentrum des Bandes, das angehoben oder abgesenkt werden soll. Fahren Sie es durch, um die Frequenz zu finden, die Sie formen möchten. | 20 Hz bis 20 kHz (1 kHz) |
| **Gain** | Wie stark am Zentrum angehoben oder abgesenkt wird. Positiv hebt das Band an; negativ höhlt es aus. | -15 bis +15 dB (0) |
| **Q factor** | Legt fest, wie breit das Band ist. Niedrige Werte formen einen breiten Bereich; hohe Werte verengen für chirurgische, punktgenaue Änderungen. | 0,1 bis 10 (1,0) |

| Preset | Was es macht |
|---|---|
| **Presence** | Eine breite Ober-Mitten-Anhebung für Klarheit und Präsenz. Ein neutraler Ausgangspunkt. |
| **Warmth** | Eine breite Tief-Mitten-Anhebung, die Körper und Wärme hinzufügt. |
| **Vocal Boost** | Hebt den Kern-Stimmbereich an, um Stimmen nach vorn zu holen. |
| **Cut Mud** | Höhlt kastigen Tief-Mitten-Matsch für einen saubereren Klang aus. |
| **Tame Harsh** | Eine schmale Absenkung, um eine harsche, durchdringende Spitze zu zähmen. |
| **Punch** | Eine Tiefton-Anhebung, die dem unteren Ende Punch und Wucht hinzufügt. |
| **Sub Boost** | Eine tiefe Anhebung ganz unten für zusätzliches Sub-Bass-Gewicht. |
| **Air** | Eine breite Anhebung ganz oben für einen offenen, luftigen Schimmer. |
| **Clarity** | Hebt die Hoch-Mitten an, um Definition und Kante hinzuzufügen. |
| **De-Ess** | Eine schmale Absenkung im Zischlautbereich, um harsche S-Laute zu zähmen. |
| **De-Boom** | Schneidet einen dröhnenden Tieffrequenz-Aufbau für ein strafferes unteres Ende. |
| **Scoop** | Eine breite Mittenabsenkung für einen ausgehöhlten, modernen Ton. |

### Low Shelf (Bass-Steuerung und Bass-Boost)

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Frequency** | Legt die Ecke fest, unterhalb derer das Shelf wirkt. Alles darunter wird gemeinsam angehoben oder abgesenkt. | 20 bis 2000 Hz (200) |
| **Gain** | Wie stark der Tiefton angehoben oder abgesenkt wird. Positiv fügt Gewicht und Wärme hinzu; negativ dünnt ihn aus. | -15 bis +15 dB (0) |

| Preset | Was es macht |
|---|---|
| **Warmth** | Eine sanfte Tiefton-Anhebung für Wärme und Körper. Ein neutraler Ausgangspunkt. |
| **Bass Boost** | Eine solide Anhebung des Basses für Gewicht und Punch. |
| **Fullness** | Füllt die Tief-Mitten auf für einen volleren, runderen Klang. |
| **Trim Bass** | Eine moderate Absenkung, um eine basslastige Mischung aufzuhellen. |
| **Cut Lows** | Eine starke Absenkung, um das untere Ende auszudünnen oder zu entdröhnen. |
| **Big Bottom** | Eine große Tiefton-Anhebung für maximales Gewicht und Rumpeln. |

### High Shelf (Höhen-Steuerung)

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Frequency** | Legt die Ecke fest, oberhalb derer das Shelf wirkt. Alles darüber wird gemeinsam angehoben oder abgesenkt. | 1 bis 20 kHz (8 kHz) |
| **Gain** | Wie stark das obere Ende angehoben oder abgesenkt wird. Positiv fügt Helligkeit und Luftigkeit hinzu; negativ glättet und verdunkelt. | -15 bis +15 dB (0) |

| Preset | Was es macht |
|---|---|
| **Presence** | Eine sanfte Höhen-Anhebung für Klarheit und Details. Ein neutraler Ausgangspunkt. |
| **Air** | Öffnet die allerhöchsten Höhen für einen luftigen, offenen Klang. |
| **Bright** | Eine starke Anhebung für einen knackigen, hellen, nach vorn gerichteten Ton. |
| **Soften** | Eine moderate Absenkung, um harschen Höhen die Kante zu nehmen. |
| **Tame Highs** | Eine starke Absenkung, um einen übermäßig hellen Klang zu verdunkeln und zu glätten. |
| **Sparkle** | Eine große Anhebung des oberen Endes für maximalen Schimmer und Glanz. |

### Soft Clip (warme Sättigung)

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Drive** | Drückt das Signal härter in den Waveshaper. Kleine Mengen fügen sanfte Wärme hinzu; große Mengen runden die Spitzen zu dicker Sättigung und Grit. | 0 bis 40 dB (0) |

| Preset | Was es macht |
|---|---|
| **Warm** | Ein Hauch von Drive für sanfte, analogartige Wärme. |
| **Drive** | Deutliche Sättigung, die den Klang verdickt und färbt. |
| **Crunch** | Kräftiger Drive mit einer hörbaren knackigen Kante. |
| **Fuzz** | Dicke, fuzzige Verzerrung. Die Spitzen werden hart gestaucht. |
| **Destroy** | Maximaler Drive. Aggressiver, voll gesättigter Grit. |

### Bit Crusher (Retro Lo-Fi)

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Bit depth** | Legt fest, wie viele Bits jedes Sample beschreiben. Weniger Bits bedeuten gröbere Stufen und mehr Quantisierungsrauschen, für einen knackigen, körnigen digitalen Klang. | 1 bis 16 Bit (16) |
| **Sample rate** | Reduziert die Abtastrate des Audios. Bei hundert Prozent bleibt die Rate unberührt; senken Sie sie, um jedes Sample länger zu halten, was die Höhen dämpft und eine harsche, aliasbehaftete Kante hinzufügt. | 1 % bis 100 % (100 %) |

| Preset | Was es macht |
|---|---|
| **Vintage** | Ein dezenter Qualitätsabfall, wie ein früher digitaler Sampler. |
| **LoFi** | Klassisches 8-Bit-Lo-Fi mit halber Rate. Körnig und retro. |
| **Crunch** | Kräftigeres Crushing mit einer hörbaren knackigen Kante. |
| **Gritty** | Grob und körnig. Die Stufen zwischen den Pegeln sind deutlich. |
| **Destroy** | Extreme Reduktion. Harsch, gebrochen, kaum wiedererkennbar. |

### Ring Modulator (metallische und robotische Töne)

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Carrier** | Legt die Frequenz des Tons fest, mit dem das Signal multipliziert wird. Wenige Hertz ergeben ein Tremolo-Wobbeln; höhere Frequenzen fügen metallische, glockenartige und robotische Obertöne hinzu. | 1 bis 4000 Hz (440) |
| **Mix** | Mischt den modulierten Klang mit dem Original. Bei null Prozent hören Sie nur das trockene Signal; bei hundert Prozent nur den vollständig modulierten Ton. | 0 % bis 100 % (0 %) |

| Preset | Was es macht |
|---|---|
| **Tremolo** | Ein sehr niedriger Carrier verwandelt es in ein Amplituden-Tremolo, das die Lautstärke wobbelt. |
| **Robot** | Ein mittlerer Carrier fügt klirrende Obertöne für einen klassischen Roboterstimmen-Effekt hinzu. |
| **Metallic** | Dichte, inharmonische Obertöne für einen harschen, metallischen Ton. |
| **Bell** | Ein höherer Carrier ergibt ein helles, glockenartiges Klingen. |
| **Alien** | Voll wet mit einem hohen Carrier. Extrem, fremdartig, kaum wiedererkennbar. |

### Tremolo (Lautstärke-Wobbeln)

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Rate** | Legt fest, wie schnell die Lautstärke pulsiert. Langsamere Raten ergeben ein weiches Schwanken; schnellere Raten ergeben ein schnelles Stottern. | 0,1 bis 20 Hz (5) |
| **Depth** | Legt fest, wie stark die Lautstärke bei jedem Puls abfällt. Bei null Prozent bleibt der Pegel gleichmäßig; bei hundert Prozent fällt er bis zur Stille ab. | 0 % bis 100 % (0 %) |

| Preset | Was es macht |
|---|---|
| **Gentle** | Ein langsames, flaches Schwanken. Dezente Bewegung, ohne Aufmerksamkeit zu erregen. |
| **Classic** | Das klassische Amp-Tremolo: eine mittlere Rate und moderate Tiefe. |
| **Deep** | Ein starker, tiefer Puls, der jeden Zyklus fast bis zur Stille abfällt. |
| **Fast** | Ein schnelles Flattern für ein schimmerndes, nervöses Gefühl. |
| **Chop** | Schnell und volle Tiefe. Ein hartes, stotterndes Zerhacken. |

### Delay (Echo)

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Time** | Legt die Pause vor jedem Echo fest. Kurze Zeiten ergeben ein enges Slapback; längere Zeiten spreizen die Wiederholungen weiter auseinander. | 0,01 bis 2 s (0,25) |
| **Feedback** | Legt fest, wie viel von jedem Echo zurückgeführt wird. Niedrige Werte ergeben eine einzelne Wiederholung; höhere Werte bauen eine lange, nachhallende Reihe von Echos auf. | 0 bis 0,95 (0,4) |
| **Mix** | Mischt die Echos mit dem Original. Bei null Prozent hören Sie nur das trockene Signal; bei hundert Prozent nur die Echos. | 0 % bis 100 % (0 %) |

| Preset | Was es macht |
|---|---|
| **Slapback** | Ein einzelnes kurzes Echo, eng am Original. Rockabilly und Vocal-Doubling. |
| **Echo** | Das klassische Echo: eine klare Wiederholung mit einigen nachhallenden Fahnen. |
| **Ping** | Eine schnelle, springende Wiederholung, die rhythmische Bewegung hinzufügt. |
| **Ambient** | Längere, weichere Wiederholungen, die in eine geräumige Fahne auswaschen. |
| **Dub** | Hohes Feedback für lange, dubbige Kaskaden von Echo. |
| **Cavern** | Lange, tiefe Wiederholungen, wie Klang, der durch einen riesigen Raum hallt. |

### Stereo Width (verengen oder verbreitern)

| Regler | Was er macht | Bereich (Standard) |
|---|---|---|
| **Width** | Verengt oder verbreitert das Stereobild. Null Prozent kollabiert zu Mono, hundert Prozent lässt es unberührt, und höhere Werte drücken die Seiten breiter. Wirkt nur auf Stereotitel beim Ziel Alle Kanäle. | 0 % bis 200 % (100 %) |

| Preset | Was es macht |
|---|---|
| **Wide** | Eine sanfte Verbreiterung, die das Stereobild öffnet. Ein neutraler Ausgangspunkt. |
| **Wider** | Eine stärkere Spreizung für ein großes, immersives Stereofeld. |
| **Max** | Maximale Breite. Sehr breit, aber achten Sie auf Mono-Kompatibilitätsprobleme. |
| **Narrow** | Zieht die Seiten für ein strafferes, zentrierteres Bild herein. |
| **Focused** | Nahezu zentriert, mit nur einem Hauch von Stereo. |
| **Mono** | Vollständig zu Mono kollabiert. Beide Lautsprecher spielen dasselbe Signal. |

## Wie das Ganze unter der Haube funktioniert (einfache Version)

- **Engines:** Sie wählen eine unter Einstellungen > Audio-Player > Wiedergabe-Engine: **Standard** (System), **Universal** (FFmpeg) oder **Sound FX** (die **BASS™-Engine** von [Un4seen Developments](https://www.un4seen.com/)). Die gewählte Engine bestimmt, welche Formate abgespielt werden, und die Effekte, der Equalizer und die DSP-Kette laufen nur in der Sound FX-Engine.
- **Formate:** Die BASS™-Engine fügt FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus und Modul- (Tracker-)Musik zusätzlich zu den System- und FFmpeg-Formaten hinzu.
- **Effekte:** Der Equalizer, der Compressor und die meisten Effekte nutzen die BASS™-Effekt-Add-ons. Freeverb ist der Freeverb-Hall. Chorus, Flanger und Distortion nutzen klassische DirectX-artige Effekte mit ihren eigenen Reglern.
- **Lautstärkenormalisierung:** ein Live-**EBU R128**-Lautheits-Einpegeler (der Lautheitsstandard, der in Rundfunk und Streaming verwendet wird).
- **Crossfeed:** das **bs2b (Bauer)**-Crossfeed, ausgeführt innerhalb der BASS™-Engine.
- **DSP-Kette:** Ihre eigenen Blöcke, angewendet in der genauen Reihenfolge, die Sie festlegen, auf allen Kanälen oder nur einer Seite.
- **Ausgabe:** Sie können Abtastrate, Kanalanzahl und Puffergröße passend zu Ihrer Ausrüstung einstellen.

Da all dies live während der Musikwiedergabe läuft, gilt für die Effekte:

- Sie arbeiten in **Echtzeit** an allem, einschließlich Cloud-Dateien, Streams und Modulmusik.
- Sie **verändern oder speichern** Ihre Dateien **nie neu**. Schalten Sie einen Effekt aus, und das Original kehrt zurück.
- Sie **merken sich Ihre Einstellungen** für jeden Effekt.
- Sie können frei **gemischt und kombiniert** werden, da jeder einzeln ist.

## Einfache Rezepte zum Ausprobieren

**Alltägliches Hören**

- **Mehr Bass, sauber:** Equalizer > Bass Booster, dann den Vorverstärker um 1 bis 2 dB senken. Oder ein DSP-Low-Shelf auf Bass Boost hinzufügen.
- **Gleichmäßige Lautstärke über eine gemischte Wiedergabeliste:** Lautstärkenormalisierung > Standard, plus Compressor > Soft.
- **Sanfter Gesamt-Feinschliff:** Compressor > Transparent, plus Lautstärkenormalisierung > Light.
- **Klarere Vocals:** Equalizer > Vocal Booster, oder ein DSP-Peaking-Block auf Vocal Boost.
- **Vollerer Klang auf kleinen Handy-Lautsprechern:** Equalizer > Small Speakers.

**Kopfhörer**

- **Angenehmer, weniger ermüdend auf Kopfhörern:** Crossfeed > Chu Moy oder Jan Meier.
- **Breiterer Klang auf Kopfhörern:** DSP Stereo Width > Wide, plus Crossfeed > Chu Moy.
- **Hart gepannte Platten der 1960er und 1970er korrigieren:** Crossfeed > Vintage Stereo.
- **Ein wenig Luftigkeit und Raum:** Freeverb > Ambience, niedrig gehalten, plus Crossfeed > Subtle.

**Ruhige Zeiten und gesprochenes Audio**

- **Spätnächtliches leises Hören:** Lautstärkenormalisierung > Night, plus Compressor > Late Night.
- **Podcasts und Hörbücher:** Compressor > Voice / Podcast, plus Equalizer > Spoken Word.
- **Lautester, gleichmäßigster Klang in einem lauten Auto:** Lautstärkenormalisierung > Strong, plus Compressor > Heavy.

**Probleme beheben**

- **Eine harsche, helle Aufnahme zähmen:** Equalizer > Treble Reducer, oder ein DSP-Peaking-Block auf Tame Harsh.
- **Elektrisches Brummen entfernen:** DSP-Kette > Notch > Mains Hum 60 (oder Mains Hum 50 in Europa).
- **Strafferer, saubererer Bass:** DSP High Pass > Tighten, um den dröhnenden Tiefton zu beschneiden.
- **Weniger Dröhnen in einer basslastigen Mischung:** DSP Low Shelf > Trim Bass, oder Peaking > De-Boom.

**Kreativ und zum Spaß**

- **Warmes, raumiges Gefühl:** Freeverb > Hall, niedrig gehalten.
- **Verträumte, geräumige Gitarren:** Chorus > Wide, plus Echo > Long.
- **Retro Lo-Fi:** DSP-Kette > Bit Crusher (LoFi) in Soft Clip (Warm).
- **Funkige Bewegung bei elektronischen Titeln:** Auto Wah > Funky, oder Phaser > Fast.
- **Klassischer Düsenflugzeug-Sweep:** Flanger > Jet.

## FAQ

{{% details title="Welche Klang-Engine verwendet Flacbox?" closed="true" %}}
Sie wählen eine Wiedergabe-Engine unter Einstellungen > Audio-Player: Standard (Apples System-Engine), Universal (die FFmpeg-Engine) oder Sound FX (die BASS™-Engine von Un4seen Developments, un4seen.com). Die gewählte Engine bestimmt, welche Dateiformate abgespielt werden. Sound FX ist diejenige, die zusätzliche Formate wie FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus und MOD- oder Tracker-Musik abspielt, und sie ist die einzige Engine, die die Live-Effekte, den 10-Band-Equalizer und die DSP-Kette bereitstellt. Um die Effekte zu nutzen, stellen Sie die Wiedergabe-Engine auf Sound FX.
{{% /details %}}

{{% details title="Kann Flacbox MOD, XM, IT und andere Tracker- oder Modulmusik abspielen?" closed="true" %}}
Ja. Die BASS™-Engine hat einen eingebauten Modulplayer, der MOD-, XM-, IT-, S3M-, MTM-, UMX- und MO3-Dateien lädt und den Song live aus seinen Mustern und Instrumentenklängen nachbaut, so wie Tracker-Musik gedacht ist. Reguläre iPhone-Player können das nicht. Effekte und der Equalizer funktionieren auch bei Modulmusik.
{{% /details %}}

{{% details title="Unterstützt Flacbox DSD und hochauflösende Dateien?" closed="true" %}}
Ja. Flacbox spielt DSD-Dateien (DSF und DFF) über die BASS™-Engine mittels DSD über PCM ab, sodass sie auf normaler Ausgabe-Hardware funktionieren, dazu FLAC, WavPack, Monkey's Audio (APE), Musepack und TrueAudio für verlustfreie Wiedergabe.
{{% /details %}}

{{% details title="Welche Klangeffekte hat Flacbox?" closed="true" %}}
Einen 10-Band-Equalizer, Lautstärkenormalisierung, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate und Crossfeed, dazu eine selbst zusammenstellbare DSP-Kette mit Filtern, Shelves, Gain, Soft Clip, Bit Crusher, Ring Modulator, Tremolo, Delay und Stereo Width. Jeder einzelne ist separat und kann mit den anderen kombiniert werden.
{{% /details %}}

{{% details title="Was ist ein Preset?" closed="true" %}}
Ein Preset ist eine fertige Einstellung für einen Effekt. Statt selbst Regler zu bewegen, tippen Sie ein Preset an, und der Klang ändert sich entsprechend. Jeder Effekt in Flacbox hat mehrere Presets, und dieser Leitfaden listet auf, was jedes einzelne bewirkt. Wenn Sie nach der Wahl eines Presets einen Regler bewegen, zeigt der Effekt «Manuell» an, um Ihnen mitzuteilen, dass er nun Ihre eigenen Werte verwendet.
{{% /details %}}

{{% details title="Wie öffne ich die Audioeffekte in Flacbox?" closed="true" %}}
Öffnen Sie den Now-Playing-Player, tippen Sie auf die Schaltfläche ⋯ (Weitere Aktionen) und wählen Sie Audioeffekte. Oder gehen Sie zu Einstellungen > Audio-Player > Audioeffekte. Tippen Sie einen Effekt an, schalten Sie seinen Schalter ein und wählen Sie ein Preset, oder öffnen Sie die Regler zur Feinabstimmung.
{{% /details %}}

{{% details title="Wo ist der Equalizer, und was sind die besten Einstellungen?" closed="true" %}}
Gehen Sie zu Einstellungen > Audio-Player > Audio-Equalizer. Er hat 10 Bänder von 32 Hz bis 16 kHz, jedes von -12 bis +12 dB, dazu einen Vorverstärker von -24 bis +24 dB und 22 Presets. Für mehr Bass verwenden Sie Bass Booster. Für klarere Stimmen verwenden Sie Vocal Booster oder Pop. Für einen helleren Klang verwenden Sie Treble Booster. Passen Sie dann einzelne Bänder nach Geschmack an.
{{% /details %}}

{{% details title="Wie hebe ich den Bass in Flacbox an?" closed="true" %}}
Zwei einfache Wege. Wählen Sie im Audio-Equalizer Bass Booster (oder heben Sie die Bänder bei 32 Hz und 64 Hz um einige dB an). Oder fügen Sie in der Signalverarbeitung einen Low-Shelf-Block eingestellt auf Bass Boost hinzu. In beiden Fällen senken Sie den Vorverstärker oder fügen einen Gain-Block um 1 bis 2 dB hinzu, damit der Bass sauber bleibt und nicht verzerrt.
{{% /details %}}

{{% details title="Welches Equalizer-Preset ist das beste für meine Musik?" closed="true" %}}
Rock und Electronic fügen Energie mit starken Tiefen und Höhen hinzu. Acoustic, Jazz und Classical bleiben warm und natürlich. Pop und Vocal Booster holen Stimmen nach vorn. Bass Booster und Hip-Hop fügen Gewicht hinzu. Deep und Loudness klingen bei niedriger Lautstärke voller. Beginnen Sie mit dem, das zu Ihrem Genre passt, und nehmen Sie dann die Feinabstimmung vor.
{{% /details %}}

{{% details title="Was ist Lautstärkenormalisierung, und wie unterscheidet sie sich von ReplayGain?" closed="true" %}}
Sie lässt jeden Titel etwa gleich laut spielen. Sie misst die tatsächliche Lautheit nach dem EBU R128-Standard (in LUFS, wie Streaming-Dienste) und passt jeden Titel an Ihr Ziel an, mit einer Max-Anhebungs-Grenze. Anders als ReplayGain benötigt sie keine Tags in Ihren Dateien und funktioniert bei jeder Quelle, live, ohne das Audio zu verändern. Presets: Light, Standard, Strong und Night.
{{% /details %}}

{{% details title="Was ist Crossfeed, und sollte ich es verwenden?" closed="true" %}}
Crossfeed mischt ein wenig des linken und rechten Kanals zusammen, sodass sich Kopfhörer eher wie echte Lautsprecher anfühlen und weniger, als stecke der Klang im Kopf fest. Es ist nur für Kopfhörer, schalten Sie es also für Lautsprecher aus. Flacbox verwendet die bs2b (Bauer)-Methode, mit Presets wie Chu Moy und Jan Meier.
{{% /details %}}

{{% details title="Was ist der Unterschied zwischen dem Compressor und der Lautstärkenormalisierung?" closed="true" %}}
Die Lautstärkenormalisierung gleicht die Lautheit zwischen verschiedenen Songs an. Der Compressor gleicht die lauten und leisen Teile innerhalb eines einzelnen Songs aus. Sie lösen unterschiedliche Probleme und arbeiten gut zusammen, besonders in einem Auto oder an einem lauten Ort.
{{% /details %}}

{{% details title="Was ist die Signalverarbeitungs- (DSP-)Kette?" closed="true" %}}
Es ist ein selbst zusammenstellbares Rack unter Einstellungen > Audio-Player > Signalverarbeitung. Fügen Sie Blöcke wie Filter, Shelves, Gain, Soft Clip, Bit Crusher, Ring Modulator, Tremolo, Delay und Stereo Width hinzu, bringen Sie sie in beliebige Reihenfolge, schalten Sie jeden ein oder aus und richten Sie die Kette auf alle Kanäle, links oder rechts. Da die Reihenfolge wichtig ist, können Sie genau den Klang gestalten, den Sie möchten.
{{% /details %}}

{{% details title="Was ist der Unterschied zwischen dem Equalizer, den Effekten und der DSP-Kette?" closed="true" %}}
Der Equalizer ist eine einfache 10-Band-Klangregelung. Die Audioeffekte sind fertige Werkzeuge (Compressor, Hall, Echo und so weiter) mit Presets. Die DSP-Kette ist der Ort, an dem Sie Ihre eigene Effektreihenfolge aus einzelnen Blöcken bauen. Sie können alle drei gleichzeitig laufen lassen.
{{% /details %}}

{{% details title="Verändern oder beschädigen die Effekte meine Musikdateien?" closed="true" %}}
Nein. Alles wird live während der Musikwiedergabe angewendet. Ihre Dateien werden nie verändert oder neu gespeichert. Schalten Sie einen Effekt aus, und der Originalklang kehrt sofort zurück.
{{% /details %}}

{{% details title="Kann ich mehr als einen Effekt gleichzeitig verwenden?" closed="true" %}}
Ja. Jeder Effekt hat seinen eigenen Schalter, und es gibt keinen Hauptschalter, sodass jede Kombination funktioniert. Zum Beispiel Lautstärkenormalisierung plus Compressor für gleichmäßiges Hören, oder Freeverb plus Crossfeed auf Kopfhörern, mit dem Equalizer obendrauf.
{{% /details %}}

{{% details title="Warum sind die Effektregler ausgegraut?" closed="true" %}}
Der Effekt ist ausgeschaltet. Schalten Sie seinen Schalter oben im Editor ein, um die Regler zu verwenden. Jeder Effekt ist standardmäßig aus.
{{% /details %}}

{{% details title="Was bedeutet die Manuell-Kennzeichnung?" closed="true" %}}
Sie bedeutet, dass Sie einen Regler von einem Preset weg bewegt haben, sodass der Effekt nun Ihre eigenen benutzerdefinierten Werte statt eines benannten Presets verwendet. Jeder Regler hat eine Zurücksetzen-Schaltfläche, und die erneute Wahl eines Presets ersetzt Ihre manuellen Werte.
{{% /details %}}

{{% details title="Kann ich meine Equalizer-Presets speichern und teilen?" closed="true" %}}
Ja. Neben den 22 eingebauten Presets können Sie eigene erstellen, sie umsortieren und sie exportieren oder importieren, um Ihre Einstellungen auf ein anderes Gerät zu übertragen.
{{% /details %}}

{{% details title="Funktionieren die Effekte mit CarPlay, Streaming und Hintergrundwiedergabe?" closed="true" %}}
Ja. Die Effekte laufen innerhalb der BASS™-Engine, sodass sie auf lokale Dateien, Cloud-Laufwerke, Medienserver, Streams und Modulmusik angewendet werden und während CarPlay und der Hintergrundwiedergabe weiter funktionieren.
{{% /details %}}

{{% details title="Kann ich die Audio-Ausgabequalität ändern?" closed="true" %}}
Ja. Unter Einstellungen > Audio-Player können Sie die Ausgabe-Abtastrate, die Anzahl der Kanäle und die Puffergröße passend zu Ihren Kopfhörern, Lautsprechern oder Ihrem DAC einstellen.
{{% /details %}}

{{% details title="Was ist ein guter Ausgangsaufbau für Kopfhörer?" closed="true" %}}
Schalten Sie die Lautstärkenormalisierung (Standard) ein, fügen Sie einen leichten Compressor (Soft) hinzu, wählen Sie ein Equalizer-Preset, das Ihnen gefällt, und schalten Sie Crossfeed (Chu Moy oder Jan Meier) ein. Lassen Sie Hall, Echo und Distortion aus, es sei denn, Sie möchten einen kreativen Klang.
{{% /details %}}

---

*BASS ist eine Marke von Un4seen Developments Ltd. Siehe [un4seen.com](https://www.un4seen.com/). Crossfeed verwendet den bs2b-Algorithmus (Bauer stereophonic-to-binaural); siehe die [bs2b-Projektseite](https://bs2b.sourceforge.net/).*
