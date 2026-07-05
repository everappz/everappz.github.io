---
title: "Naadloos afspelen inschakelen en gebruiken in Evermusic (en waarom het echt naadloos is)"
date: 2026-07-05
description: "Schakel echt naadloos afspelen in Evermusic in voor iPhone, iPad en Mac. Leer hoe je het inschakelt in Instellingen, hoe je het gebruikt met albums en afspeellijsten, hoe het onder de motorkap werkt, en waarom het echt naadloos afspelen op sample-niveau is, geen crossfade."
keywords: ["naadloos afspelen iPhone", "naadloos afspelen inschakelen Evermusic", "echt naadloos afspelen iOS", "naadloze muziekspeler iPhone", "naadloos afspelen versus crossfade", "geen pauze tussen nummers iPhone", "naadloze FLAC-speler iOS", "livealbum afspelen iPhone", "conceptalbum naadloos", "DJ-mix naadloos iOS", "Evermusic naadloos", "naadloze nummerovergang muziekspeler"]
tags: ["Evermusic", "Naadloos afspelen", "Handleiding", "Audio", "Afspelen", "Crossfade", "FLAC", "Albums", "Afspeellijsten"]
readingTime: 4
---

{{< author-byline >}}

**Kort samengevat:** Open **Instellingen > Audiospeler > Naadloos afspelen** en zet de schakelaar **AAN**. Vanaf dat moment worden nummers afgespeeld zonder pauze, klik of tik ertussen. Evermusic buffert en decodeert het volgende nummer alvast terwijl het huidige nog speelt, en draagt de overdracht dan over tussen audiosamples op een doorlopende buffer, zodat de overgang echt naadloos is. Het is echt naadloos afspelen op sample-niveau, geen crossfade.

## Wat is naadloos afspelen?

Naadloos afspelen verwijdert de korte stilte die normaal gesproken tussen twee nummers verschijnt. Wanneer het aanstaat, stroomt de laatste noot van het ene nummer rechtstreeks over in de eerste noot van het volgende, **zonder pauze, zonder klik en zonder tik**.

Het is het belangrijkst voor muziek die is gemasterd om als één doorlopend geheel te worden gehoord:

- **Live-opnames en concerten**, waar applaus en publieksgeluid tussen de nummers doorlopen.
- **DJ-mixen en doorlopende sets**, waar het ene nummer beatgematcht overgaat in het volgende.
- **Klassieke werken**, waar delen bedoeld zijn om in elkaar over te lopen.
- **Conceptalbums**, waar nummers bewust rechtstreeks in elkaar overvloeien of crossfaden (bijvoorbeeld *The Dark Side of the Moon* of *Abbey Road*).

Zonder naadloos afspelen worden deze albums bij elke nummergrens onderbroken door een klein gaatje, wat de flow die de artiest bedoelde doorbreekt.

## Naadloos afspelen inschakelen in Evermusic

Naadloos afspelen staat **standaard uit**, dus je zet het één keer aan en het blijft aan.

1. Open **Evermusic**.
2. Ga naar het tabblad **Instellingen**.
3. Tik op **Audiospeler**.
4. Tik op **Naadloos afspelen**.
5. Zet de schakelaar **Naadloos afspelen** op **AAN**.

Dat is alles. De wijziging wordt meteen opgeslagen en geldt voor alles wat je hierna afspeelt.

> **Let op:** Wanneer naadloos afspelen aanstaat, wordt **crossfade automatisch uitgeschakeld**. De twee functies doen het tegenovergestelde — crossfade laat het einde van het ene nummer overlappen en versmelten met het begin van het volgende, terwijl naadloos afspelen de exacte audio behoudt en simpelweg de tussenruimte weghaalt. Je gebruikt het een of het ander, niet allebei.

## Naadloos afspelen gebruiken

Zodra het is ingeschakeld, hoef je verder niets te doen — het werkt gewoon. Voor de beste ervaring:

- **Speel een volledig album of een doorlopende afspeellijst** op volgorde af. Zet het hele album in de wachtrij, druk op afspelen en laat het van begin tot eind lopen.
- **Houd de nummers in de bedoelde volgorde.** Naadloos afspelen telt tussen aangrenzende nummers, dus shuffle is minder relevant voor een conceptalbum of een liveset.
- **Het werkt voor lokale en cloudbestanden gelijk.** Of je muziek nu op het apparaat, op een cloudschijf of op een mediaserver staat, Evermusic begint het volgende nummer vroeg voor te bereiden zodat de overdracht naadloos is. Voor externe bronnen begint het gewoon iets eerder met bufferen.
- **Het werkt met lossless- en lossy-formaten**, waaronder FLAC, Apple Lossless (ALAC), MP3, AAC en meer.

## Hoe naadloos afspelen werkt in Evermusic

Dit is wat er onder de motorkap gebeurt, in gewone taal.

De afspeelengine van Evermusic houdt **twee nummers tegelijk in afspeelstatus**: het nummer dat je hoort (het *huidige* item) en het nummer dat erna in de wachtrij staat (het *volgende* item).

1. **Het volgende nummer wordt vroeg voorbereid.** Terwijl het huidige nummer nog speelt, haalt Evermusic het volgende nummer op de achtergrond op, decodeert het en **buffert het alvast**. Tegen de tijd dat het huidige nummer eindigt, is het volgende al gedecodeerd en klaar om af te spelen — er is geen "laad"-pauze.
2. **De uitvoer stopt nooit.** De renderlus van de engine trekt continu audiosamples uit een gedeelde buffer en stuurt ze naar de luidsprekers of koptelefoon. Deze lus stopt niet bij een nummergrens.
3. **De overdracht gebeurt tussen samples.** Wanneer het huidige nummer zijn laatste sample bereikt, schakelt Evermusic de bron over naar het volgende nummer **binnen de speler**, niet binnen de audiostroom. De uitvoerbuffer blijft zonder onderbreking stromen, dus de overschakeling gebeurt in de ruimte tussen twee audiosamples — veel te klein voor het oor om waar te nemen.

Omdat de overgang op sample-niveau plaatsvindt op een buffer die nooit pauzeert, is er geen stilte om in te voegen en geen decoder om bij de grens te herstarten. Dat is wat de klik, tik en het gaatje wegneemt.

## Waarom het echt naadloos afspelen is

Sommige apps *simuleren* naadloos afspelen alleen maar. Dat van Evermusic is het echte werk, en dit is het verschil:

- **Het is op sample-niveau nauwkeurig, geen crossfade.** Crossfade verbergt het gaatje door twee nummers te laten overlappen en samen weg te faden, wat de audio verandert die je bij de grens hoort. Naadloos afspelen behoudt elke sample van beide nummers precies zoals gemasterd en verwijdert simpelweg de stilte ertussen.
- **Er is geen decoder-herstartpauze.** Veel "naadloze" implementaties pauzeren nog steeds even om het volgende bestand te openen en te decoderen. Evermusic decodeert het volgende nummer *van tevoren*, dus er is niets om op te wachten bij de grens.
- **Er wordt geen stilte ingevoegd.** Sommige encoders en spelers voegen een paar milliseconden opvulling tussen nummers toe. De overdracht via doorlopende buffer van Evermusic betekent dat er bij het afspelen geen opvulling wordt toegevoegd.
- **Er wordt niets opnieuw gecodeerd.** Je audio blijft onaangeroerd. Naadloos afspelen wordt bereikt door *hoe* de nummers worden gepland en gebufferd, niet door het geluid te bewerken of opnieuw te comprimeren.
- **Het werkt overal.** Omdat het is ingebouwd in de kern-afspeelengine, werkt naadloos afspelen met lokale bestanden, cloudschijven, mediaservers, lossless- en lossy-formaten — hetzelfde naadloze resultaat over al deze bronnen.

Het resultaat is dat een livealbum, een beatgematchte DJ-set of een conceptplaat precies wordt afgespeeld zoals bedoeld: als één doorlopend muziekstuk.

## Veelgestelde vragen

{{% details title="Hoe zet ik naadloos afspelen aan in Evermusic?" closed="true" %}}
Open Evermusic, ga naar Instellingen > Audiospeler > Naadloos afspelen en zet de schakelaar AAN. Het staat standaard uit. Eenmaal ingeschakeld geldt het voor alles wat je afspeelt en blijft het aan totdat je het uitzet.
{{% /details %}}

{{% details title="Is het naadloos afspelen van Evermusic echt naadloos of gewoon crossfade?" closed="true" %}}
Het is echt naadloos afspelen op sample-niveau. Evermusic decodeert en buffert het volgende nummer alvast terwijl het huidige speelt, en draagt de overdracht dan over tussen audiosamples op een doorlopende buffer, zodat er geen stilte, klik of opvulling wordt ingevoegd en er geen decoder-herstartpauze optreedt. Crossfade is een aparte, andere functie die nummers laat overlappen en versmelten; naadloos afspelen behoudt de audio precies zoals gemasterd en verwijdert alleen het gaatje.
{{% /details %}}

{{% details title="Waarom hoor ik nog steeds een gaatje tussen sommige nummers?" closed="true" %}}
Zorg dat naadloos afspelen AAN staat in Instellingen > Audiospeler > Naadloos afspelen. Als er een gaatje blijft, kan het in de opname zelf zitten (sommige bestanden bevatten een paar seconden echte stilte aan het begin of einde van een nummer). Naadloos afspelen verwijdert het gaatje dat de speler normaal tussen nummers zou toevoegen; het kan geen stilte verwijderen die deel uitmaakt van het audiobestand.
{{% /details %}}

{{% details title="Werkt naadloos afspelen met FLAC en andere lossless-bestanden?" closed="true" %}}
Ja. Naadloos afspelen werkt met FLAC, Apple Lossless (ALAC) en lossy-formaten zoals MP3 en AAC, of de bestanden nu lokaal, in de cloud of op een mediaserver zijn opgeslagen.
{{% /details %}}

{{% details title="Kan ik naadloos afspelen en crossfade tegelijk gebruiken?" closed="true" %}}
Nee. Ze doen het tegenovergestelde, dus het inschakelen van naadloos afspelen schakelt crossfade automatisch uit. Gebruik naadloos afspelen voor livealbums, DJ-mixen en conceptplaten waar de audio precies bewaard moet blijven; gebruik crossfade als je wilt dat nummers in elkaar overvloeien.
{{% /details %}}

{{% details title="Werkt naadloos afspelen bij streamen vanuit de cloud?" closed="true" %}}
Ja. Evermusic begint het volgende nummer vroeg te bufferen en te decoderen, ook voor cloudschijven en mediaservers, zodat de overdracht naadloos blijft. Bij tragere verbindingen begint het simpelweg iets eerder met het voorbereiden van het volgende nummer.
{{% /details %}}

{{% details title="Vermindert naadloos afspelen de audiokwaliteit?" closed="true" %}}
Nee. Naadloos afspelen codeert of bewerkt je audio niet opnieuw. Het verandert alleen hoe nummers worden gepland en gebufferd, zodat er geen gaatje tussen zit. Elke sample wordt precies afgespeeld zoals hij in het bestand staat.
{{% /details %}}
