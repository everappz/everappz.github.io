---
title: "Sådan aktiverer og bruger du gapless-afspilning i Evermusic (og hvorfor det er ægte gapless)"
date: 2026-07-05
description: "Slå ægte gapless-afspilning til i Evermusic til iPhone, iPad og Mac. Lær, hvordan du aktiverer det i Indstillinger, hvordan du bruger det med album og playlister, hvordan det fungerer under motorhjelmen, og hvorfor det er ægte gapless-afspilning med sample-nøjagtighed, ikke crossfade."
keywords: ["gapless-afspilning iPhone", "sådan aktiverer du gapless-afspilning Evermusic", "ægte gapless-afspilning iOS", "gapless musikafspiller iPhone", "gapless-afspilning vs crossfade", "ingen pause mellem sange iPhone", "gapless FLAC-afspiller iOS", "afspilning af livealbum iPhone", "konceptalbum gapless", "DJ-mix gapless iOS", "Evermusic gapless", "problemfri overgang mellem numre musikafspiller"]
tags: ["Evermusic", "Gapless-afspilning", "Sådan gør du", "Lyd", "Afspilning", "Crossfade", "FLAC", "Album", "Playlister"]
readingTime: 4
---

{{< author-byline >}}

**Kort fortalt:** Åbn **Indstillinger > Lydafspiller > Gapless-afspilning**, og sæt kontakten på **TIL**. Fra da af afspilles sange uden pause, klik eller tik imellem dem. Evermusic forbuffrer og afkoder det næste nummer, mens det aktuelle stadig spiller, og overdrager derefter mellem lydsamples på en sammenhængende buffer, så overgangen er helt problemfri. Det er ægte gapless-afspilning med sample-nøjagtighed, ikke crossfade.

## Hvad er gapless-afspilning?

Gapless-afspilning fjerner den korte stilhed, der normalt opstår mellem to numre. Når det er slået til, flyder den sidste tone i én sang direkte over i den første tone i den næste, **uden pause, uden klik og uden tik**.

Det betyder mest for musik, der er blevet masteret til at høres som ét sammenhængende stykke:

- **Liveoptagelser og koncerter**, hvor bifald og publikumsstøj bæres videre mellem sange.
- **DJ-mix og sammenhængende sæt**, hvor ét nummer er beat-matchet ind i det næste.
- **Klassiske værker**, hvor satser er tænkt til at løbe sammen.
- **Konceptalbum**, hvor numre fader eller crossfader direkte ind i hinanden by design (for eksempel *The Dark Side of the Moon* eller *Abbey Road*).

Uden gapless-afspilning bliver disse album afbrudt af et lille hul ved hver nummerovergang, hvilket bryder det flow, kunstneren havde tænkt.

## Sådan aktiverer du gapless-afspilning i Evermusic

Gapless-afspilning er **slået fra som standard**, så du slår det til én gang, og det bliver slået til.

1. Åbn **Evermusic**.
2. Gå til fanen **Indstillinger**.
3. Tryk på **Lydafspiller**.
4. Tryk på **Gapless-afspilning**.
5. Sæt kontakten **Gapless-afspilning** på **TIL**.

Så er det gjort. Ændringen gemmes med det samme og gælder for alt, du afspiller herefter.

> **Bemærk:** Når gapless-afspilning er slået til, **slås crossfade automatisk fra**. De to funktioner gør modsatte ting. Crossfade overlapper og blander slutningen af ét nummer med starten af det næste, mens gapless bevarer den nøjagtige lyd og blot fjerner hullet imellem dem. Du bruger den ene eller den anden, ikke begge.

## Sådan bruger du gapless-afspilning

Når det først er aktiveret, er der ikke mere at gøre – det virker bare. For den bedste oplevelse:

- **Afspil et helt album eller en sammenhængende playliste** i rækkefølge. Sæt hele albummet i kø, tryk på afspil, og lad det køre fra ende til anden.
- **Behold numrene i den tiltænkte rækkefølge.** Gapless betyder noget mellem tilstødende numre, så bland er mindre relevant for et konceptalbum eller et livesæt.
- **Det virker ens for lokale filer og skyfiler.** Uanset om din musik er gemt på enheden, på et skydrev eller på en medieserver, begynder Evermusic at forberede det næste nummer tidligt, så overdragelsen bliver problemfri. For fjernkilder begynder den blot at buffre lidt tidligere.
- **Det virker med tabsfrie og tabsbehæftede formater**, herunder FLAC, Apple Lossless (ALAC), MP3, AAC og mere.

## Sådan fungerer gapless-afspilning i Evermusic

Her er, hvad der sker under motorhjelmen, forklaret enkelt.

Evermusics afspilningsmotor holder **to numre i spil samtidig**: det, du hører (den *aktuelle* post), og det, der er sat i kø efter det (den *næste* post).

1. **Det næste nummer forberedes tidligt.** Mens det aktuelle nummer stadig spiller, henter, afkoder og **forbuffrer** Evermusic det næste nummer i baggrunden. Når det aktuelle nummer slutter, er det næste allerede afkodet og klar til at spille – der er ingen "indlæsnings"-pause.
2. **Udgangen stopper aldrig.** Motorens renderingsløkke trækker løbende lydsamples fra en delt buffer og sender dem til højttalerne eller hovedtelefonerne. Denne løkke stopper ikke ved en nummerovergang.
3. **Overdragelsen sker mellem samples.** Når det aktuelle nummer når sit sidste sample, skifter Evermusic kilden til det næste nummer **inde i afspilleren**, ikke inde i lydstrømmen. Udgangsbufferen bliver ved med at flyde uden afbrydelse, så skiftet sker i rummet mellem to lydsamples – alt for lille til, at øret kan opfange det.

Fordi overgangen sker på sample-niveau på en buffer, der aldrig standser, er der ingen stilhed at indsætte og ingen afkoder at genstarte ved overgangen. Det er dét, der fjerner klikket, tikket og hullet.

## Hvorfor det er ægte gapless-afspilning

Nogle apps *simulerer* kun gapless-afspilning. Evermusics er ægte vare, og her er forskellen:

- **Det er sample-nøjagtigt, ikke en crossfade.** Crossfade skjuler hullet ved at overlappe og fade to numre sammen, hvilket ændrer den lyd, du hører ved overgangen. Gapless bevarer hvert sample af begge numre nøjagtigt som masteret og fjerner blot stilheden imellem dem.
- **Der er intet hul fra afkoder-genstart.** Mange "gapless"-implementeringer holder stadig en kort pause for at åbne og afkode den næste fil. Evermusic afkoder det næste nummer *på forhånd*, så der er intet at vente på ved overgangen.
- **Der indsættes ingen stilhed.** Nogle encodere og afspillere tilføjer nogle få millisekunder padding mellem numre. Evermusics overdragelse via sammenhængende buffer betyder, at der ikke tilføjes padding ved afspilning.
- **Intet genkodes.** Din lyd er urørt. Gapless opnås gennem *hvordan* numrene planlægges og buffres, ikke ved at behandle eller genkomprimere lyden.
- **Det virker overalt.** Fordi det er indbygget i selve afspilningsmotorens kerne, virker gapless med lokale filer, skydrev, medieservere, tabsfrie og tabsbehæftede formater – med det samme problemfrie resultat på tværs af alle.

Resultatet er, at et livealbum, et beat-matchet DJ-sæt eller en konceptplade afspilles nøjagtigt, som det var tænkt: som ét sammenhængende stykke musik.

## Ofte stillede spørgsmål

{{% details title="Hvordan slår jeg gapless-afspilning til i Evermusic?" closed="true" %}}
Åbn Evermusic, gå til Indstillinger > Lydafspiller > Gapless-afspilning, og sæt kontakten på TIL. Det er slået fra som standard. Når det er aktiveret, gælder det for alt, du afspiller, og bliver slået til, indtil du slår det fra.
{{% /details %}}

{{% details title="Er Evermusics gapless-afspilning ægte gapless eller bare crossfade?" closed="true" %}}
Det er ægte gapless-afspilning med sample-nøjagtighed. Evermusic afkoder og forbuffrer det næste nummer, mens det aktuelle spiller, og overdrager derefter mellem lydsamples på en sammenhængende buffer, så der indsættes ingen stilhed, klik eller padding, og der opstår intet hul fra afkoder-genstart. Crossfade er en separat, anden funktion, der overlapper og blander numre; gapless bevarer lyden nøjagtigt som masteret og fjerner kun hullet.
{{% /details %}}

{{% details title="Hvorfor hører jeg stadig et hul mellem nogle numre?" closed="true" %}}
Sørg for, at gapless-afspilning er slået TIL under Indstillinger > Lydafspiller > Gapless-afspilning. Hvis der stadig er et hul, kan det være indbygget i selve optagelsen (nogle filer indeholder nogle få sekunders ægte stilhed i starten eller slutningen af et nummer). Gapless fjerner det hul, afspilleren normalt ville tilføje mellem numre; det kan ikke fjerne stilhed, der er en del af lydfilen.
{{% /details %}}

{{% details title="Virker gapless-afspilning med FLAC og andre tabsfrie filer?" closed="true" %}}
Ja. Gapless-afspilning virker med FLAC, Apple Lossless (ALAC) og tabsbehæftede formater som MP3 og AAC, uanset om filerne er gemt lokalt, i skyen eller på en medieserver.
{{% /details %}}

{{% details title="Kan jeg bruge gapless-afspilning og crossfade samtidig?" closed="true" %}}
Nej. De gør modsatte ting, så når du aktiverer gapless-afspilning, deaktiveres crossfade automatisk. Brug gapless til livealbum, DJ-mix og konceptplader, hvor lyden skal bevares nøjagtigt; brug crossfade, hvis du vil have sange til at fade over i hinanden.
{{% /details %}}

{{% details title="Virker gapless-afspilning ved streaming fra skyen?" closed="true" %}}
Ja. Evermusic begynder at buffre og afkode det næste nummer tidligt, også for skydrev og medieservere, så overdragelsen forbliver problemfri. På langsommere forbindelser begynder den blot at forberede det næste nummer lidt tidligere.
{{% /details %}}

{{% details title="Forringer gapless-afspilning lydkvaliteten?" closed="true" %}}
Nej. Gapless-afspilning genkoder eller behandler ikke din lyd. Det ændrer kun, hvordan numrene planlægges og buffres, så der ikke er noget hul imellem dem. Hvert sample afspilles nøjagtigt, som det er i filen.
{{% /details %}}
