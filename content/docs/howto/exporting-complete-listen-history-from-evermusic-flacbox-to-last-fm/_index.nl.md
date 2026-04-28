---
title: "Exporteer je volledige luistergeschiedenis van Evermusic & Flacbox naar Last.fm"
date: 2024-01-30
description: "Leer hoe je je muziekgeschiedenis exporteert vanuit Evermusic en Flacbox en uploadt naar Last.fm met CSV-bestanden en de Last.fm Scrubbler-tool voor Windows."
keywords: ["evermusic", "flacbox", "lastfm", "muziekgeschiedenis", "scrobbling", "nummers exporteren", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "recenties", "lastfm", "exporteren", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Samenvatting:** Exporteer je luistergeschiedenis vanuit Evermusic of Flacbox als een CSV-bestand en upload het vervolgens naar Last.fm met de gratis Last.fm-Scrubbler-WPF-tool op Windows. Automatische scrobbling is ook standaard beschikbaar in beide apps.

**Update:** Automatische scrobbling is nu beschikbaar! Meer informatie vind je hier: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling is een eenvoudige manier om automatisch basisgegevens op te slaan, zoals de titel en artiest van het nummer dat je afspeelt, bij een online dienst. Later kun je je luistergeschiedenis bekijken.

[Last.fm](https://www.last.fm/home), aangedreven door een muziekaanbevelingssysteem genaamd Audioscrobbler, biedt deze dienst gratis aan. Het creëert een gedetailleerd profiel van je muzieksmaak door de nummers die je beluistert vast te leggen, of het nu gaat om internetradiostations, je computer of diverse draagbare muziekapparaten. Je kunt de website later bezoeken om aanbevelingen te ontvangen voor nieuwe artiesten of albums die passen bij je muzieksmaak.

Je kunt je luistergeschiedenis uploaden naar [Last.fm](http://Last.fm) vanuit de Evermusic- en Flacbox-apps met een gratis tool, en we laten je zien hoe je dit doet.

Open het gedeelte 'Muziekbibliotheek' van de applicatie en scroll naar het gedeelte 'Snelle toegang'. Tik op het menu-item 'Recenties'.

![scherm muziekbibliotheek](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

Op het scherm 'Recenties' tik je op de knop 'Meer' in de rechterbovenhoek om het menu 'Meer acties' te activeren. Tik op het menu-item 'Nummerlijst exporteren'.

![scherm recenties](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

Op het scherm 'Bestandsformaat selecteren' heb je de mogelijkheid om het formaat van het doelbestand te selecteren. Beschikbare opties - CSV, TXT, M3U.

![scherm bestandsformaat selecteren](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Dit staat voor Comma-Separated Values, perfect om je gegevens in een nette tabelindeling te organiseren. In het doelbestand vind je parameters zoals Artiestnaam, Albumnaam, Tracknaam, Tijdstempel (het tijdstip waarop je de nummers hebt beluisterd), Albumartiestnaam en Trackduur.

TXT: Hier hebben we het over een platte-tekstbestand. Het is eenvoudig en overzichtelijk, met parameters waaronder Artiestnaam, Albumnaam, Tracknaam en Duur.

M3U: Dit formaat is in wezen de standaardkeuze voor het maken van afspeellijsten. Het is geweldig omdat je je nummerlijst kunt exporteren en je tracks op elk apparaat kunt beluisteren, zelfs als je de originele bestanden niet hebt (mits je de optie voor absolute URL voor mediabestanden selecteert). In het uitvoerbestand vind je parameters zoals Duur, Artiestnaam, Tracknaam en Mediabestandslocatie.

Voor onze taak is het selecteren van CSV de juiste keuze. We gebruiken dit bestand met de gratis software Last.fm-Scrubbler-WPF om onze luistergeschiedenis te uploaden naar de [Last.fm](http://Last.fm)-dienst. Kies gewoon CSV en druk op de knop 'Exporteren'.

![scherm export voltooid](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Nadat de export is voltooid, tik je eenvoudig op de knop 'Bestand tonen', en de app toont het aangemaakte bestand in je documentenmap. Tik vervolgens op de knop 'Meer acties' naast de bestandsnaam en selecteer de optie 'Openen in' uit het menu. Onze volgende stap is het geëxporteerde bestand naar je desktopcomputer kopiëren. Dit kun je eenvoudig doen door de optie AirDrop te selecteren uit het menu 'Openen in'.

![meer acties voor geëxporteerd bestand](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Vervolgens gebruiken we een gratis open-source [Last.FM](http://Last.FM)-client die alleen beschikbaar is op het Windows-platform. Met deze client kun je je luistergeschiedenis op [Last.FM](http://Last.FM) efficiënt bijwerken met het CSV-bestand dat we zojuist hebben geëxporteerd.

Als je momenteel geen Windows-computer gebruikt, maak je geen zorgen. Je kunt deze client nog steeds gebruiken door VirtualBox op je Mac te installeren en het officiële Windows-ontwikkelomgevingsimagebestand te gebruiken.

Dit is wat je moet doen:

- Installeer VirtualBox via de volgende link: [VirtualBox downloaden](https://www.virtualbox.org/wiki/Downloads)

- Download en installeer de Windows-ontwikkelomgeving via deze link: [Windows-ontwikkelomgeving](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Download en installeer op je Windows-computer (of VirtualBox-app met Windows Development-image) [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - gratis open-source software beschikbaar op GitHub. We hebben getest met versie 1.28 die je hier kunt downloaden: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Downloadpagina van Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

Klik onder het gedeelte 'Assets' op [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) om het installatiearchief te downloaden. Pak het gedownloade bestand uit en open de uitgepakte map.

- BELANGRIJK

Deze app is nog in bèta. De makers van de app hebben niet veel getest. Ze raden aan om eerst te proberen te scrobblen naar een testaccount en te kijken of de dingen die je wilt scrobblen correct werken. Vooral als je veel nummers tegelijk scrobbelt. Wees voorzichtig met je accounts.

Start Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Op het hoofdscherm van de applicatie tik je eenvoudig op 'Niet ingelogd' linksonder om het scherm 'Account toevoegen' te activeren.

![Scherm account toevoegen](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Voer je inloggegevens in.

![scherm inloggegevens invoeren](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Tik op de knop 'Login' om je account toe te voegen.

![Tik op de knop Login om je account toe te voegen.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Open het tabblad 'File Parse Scrobbler' om te beginnen met het importeren van het CSV-bestand vanuit de Evermusic-app.

![Open het tabblad File Parse Scrobbler om te beginnen met het importeren van het CSV-bestand vanuit de Evermusic-app.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Kies 'Parser: CSV' en tik op de knop 'Settings'.

Op het volgende scherm kun je de volgorde van de parameters in je CSV-bestand kiezen.

Individuele velden kunnen worden omsloten door aanhalingstekens en MOETEN worden omsloten door aanhalingstekens als het veld een van de ingestelde scheidingstekens bevat. Bijvoorbeeld:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Laat dus alle instellingen op standaard staan; het enige dat je hoeft te wijzigen is het inschakelen van het selectievakje in het veld 'Has Fields Enclosed In Quotes'.

Tik op 'Save & Close' om de wijzigingen toe te passen.

![kies de volgorde van de parameters in je CSV-bestand.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Bestandsparse-scrobbling heeft twee modi. Deze kunnen worden gewijzigd met de ComboBox 'Scrobbling Mode'.

Normale modus: In deze modus worden de nummers gescrobbeld met het tijdstempel van de geparseerde scrobble. Alleen scrobbles nieuwer dan 14 dagen kunnen worden gescrobbeld.

Importmodus: In deze modus worden de nummers gescrobbeld met het tijdstempel berekend op basis van de 'Finish Time' en de geselecteerde duur tussen elk nummer. Dit maakt het mogelijk om nummers te scrobblen, zelfs als het tijdstempel van de geparseerde scrobble ouder is dan 14 dagen. Daarom wordt het eerste (bovenste) nummer in het CSV-bestand gescrobbeld met de 'Finish Time'.

Kies een eerder gegenereerd CSV-bestand vanuit de Evermusic-app in het veld 'File:' en tik op 'Parse'. In sommige gevallen kun je een foutmelding zien die aangeeft dat sommige scrobbles niet geparseerd konden worden. Dit is normaal als je enkele nummers hebt zonder volledige metadata zoals Artiestnaam.

![sommige scrobbles konden niet worden geparseerd](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Tik op de knop 'Check All' om alle geparseerde nummers te selecteren.

![Tik op de knop Check All om alle geparseerde nummers te selecteren.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Tik op de knop 'Preview' om alle wijzigingen te controleren die naar de server worden verzonden.

![Tik op de knop Preview om alle wijzigingen te controleren die naar de server worden verzonden.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Tik op de knop 'Scrobble' om alle wijzigingen naar de server te uploaden.

![Tik op de knop Scrobble om alle wijzigingen naar de server te uploaden.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Voorheen had Last.fm-Scrubbler-WPF geen dagelijkse scrobblelimiet. Dit is nu veranderd omdat sommige mensen de Scrubbler gebruikten om zoveel nummers te scrobblen dat het problemen veroorzaakte voor de Last.fm-pagina. De scrobblelimiet is momenteel 2800 scrobbles per dag. Wanneer je probeert meer te scrobblen, krijg je een foutmelding. Er zijn plannen om een 'scrobble-wachtrij' toe te voegen, zodat als je meer dan 2800 nummers moet scrobblen, ze aan een wachtrij worden toegevoegd en na enige tijd automatisch worden gescrobbeld. Je kunt controleren hoeveel scrobbles je nog over hebt in de gebruikersselectieweergave.

Zodra alle records succesvol naar de server zijn geüpload, zie je onderaan het app-venster een bericht met de bevestiging: 'Successfully scrobbled selected tracks.'

![Successfully scrobbled selected tracks.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Nu kun je je profiel openen op de [Last.fm](http://Last.fm)-pagina en alle wijzigingen bekijken.

![je profiel op de Last.fm-pagina](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Veelgestelde vragen

{{% details title="Kan ik automatisch scrobblen zonder CSV-bestanden te exporteren?" closed="true" %}}
Ja. Zowel Evermusic als Flacbox ondersteunen nu automatische Last.fm-scrobbling. Zie de handleiding: [Hoe scrobble je naar Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Wat als mijn CSV nummers bevat die ouder zijn dan 14 dagen?" closed="true" %}}
Gebruik de Importmodus in Last.fm-Scrubbler-WPF. Het herberekent tijdstempels op basis van de Finish Time, waardoor je nummers kunt scrobblen ongeacht hun oorspronkelijke datum.
{{% /details %}}

{{% details title="Ik heb geen Windows-computer. Kan ik Last.fm-Scrubbler toch gebruiken?" closed="true" %}}
Ja. Installeer VirtualBox op je Mac en download de gratis Windows-ontwikkelomgevingsimage van Microsoft. Voer Last.fm-Scrubbler-WPF uit in de virtuele machine.
{{% /details %}}

{{% details title="Waarom worden sommige scrobbles niet geparseerd?" closed="true" %}}
Nummers zonder essentiële metadata (zoals artiestnaam) kunnen niet worden geparseerd. Dit is verwacht en heeft geen invloed op andere nummers in het bestand.
{{% /details %}}

{{% details title="Is er een dagelijkse scrobblelimiet?" closed="true" %}}
Ja. Last.fm-Scrubbler-WPF staat maximaal 2.800 scrobbles per dag toe. Als je meer moet scrobblen, verdeel het proces dan over meerdere dagen.
{{% /details %}}
