---
title: "Sådan opsætter du en DLNA/UPnP-medieserver på iPhone og iPad til streaming"
description: "Gør din iPhone eller iPad til en DLNA/UPnP-medieserver med Everdisk, og stream billeder, videoer og musik til et smart-TV, en spillekonsol, VLC eller Kodi over Wi-Fi. Fuld opsætning plus hvordan du forbinder fra Samsung-, LG- og Sony-TV, Windows, Mac, Linux, Android og en anden iPhone."
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "medieserver", "streaming", "smart-tv", "iphone", "ipad", "wifi"]
keywords: ["DLNA-server iPhone", "UPnP-server iPad", "sådan opsætter du DLNA på iPhone", "stream til smart-TV fra iPhone", "DLNA-medieserver iOS", "stream videoer til TV uden kabel", "afspil iPhone-billeder på TV", "Samsung TV DLNA iPhone", "LG TV DLNA iPhone", "Sony Bravia DLNA iPhone", "VLC DLNA iPhone", "Kodi DLNA-medieserver", "UPnP AV-medieserver iOS", "stream musik til TV fra iPhone", "iPhone-medieserverapp"]
readingTime: 9
---

{{< author-byline >}}

DLNA (også kaldet UPnP AV) er den stille arbejdshest bag de fleste smart-TV. Det er et fælles sprog, der lader et TV eller en medieafspiller finde et mediebibliotek på det samme Wi-Fi og afspille fra det, uden noget at installere på TV'et. Hvis din iPhone eller iPad kan fungere som det bibliotek, dukker dine billeder, videoer og musik op på den store skærm af sig selv.

Denne vejledning viser, hvordan du gør din iPhone eller iPad til en DLNA/UPnP-medieserver med [Everdisk](/products/everdisk), og hvordan du åbner det bibliotek fra et smart-TV, en spillekonsol, VLC, Kodi, en computer, en Android-telefon og endda en anden iPhone. Alt kører over dit lokale Wi-Fi, så intet uploades nogen steder.

## Det skal du bruge

- En iPhone eller iPad med [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installeret.
- Et TV, en afspiller eller en computer på **det samme Wi-Fi-netværk** som din enhed.
- De billeder, videoer eller den musik, du vil afspille, allerede på din iPhone (i Billeder-appen, Musik-appen eller Everdisks Dokumenter-mappe).

## Opsæt DLNA-serveren i Everdisk

### Trin 1: Vælg, hvad der skal deles

Åbn Everdisk og gå til fanen **Deling**. Tryk på **Hvad skal deles**, og vælg dit indhold:

- Slå **Tillad adgang til hele billedbiblioteket** til for at dele hvert album, eller tryk på **Tilføj billeder** for at vælge nogle få.
- Slå **Tillad adgang til hele musikbiblioteket** til for at dele dine sange, eller tryk på **Tilføj numre** for et udvalg.
- Tilføj mapper eller filer med **Tilføj mappe** og **Tilføj fil**. Appens egen Dokumenter-mappe deles som standard.

Du skal have mindst ét element valgt, før deling kan starte.

### Trin 2: Slå Tv og mediecenter (DLNA) til

Gå til **Indstillinger**, derefter **Deling**, derefter **Forbindelser**. Sørg for, at **Tv og mediecenter** er slået til. Det er slået til som standard og bærer DLNA-mærket. Det er den server, TV og afspillere leder efter.

### Trin 3: Start deling

Tilbage på fanen **Deling** trykker du på den store **Start**-knap. Din enhed er nu en medieserver på dit Wi-Fi. Den vises for andre enheder under sit venlige navn, det der vises som dit enhedsnavn i appen (noget i retning af "Speedy-Hare", indtil du ændrer det).

DLNA-streaming er altid åben, så der er ingen adgangskode at indtaste på TV'et. Hold Everdisk åben på skærmen, mens du ser med, fordi iOS sætter apps på pause, der skubbes helt i baggrunden.

## Afspil på et smart-TV

Dette er det mest almindelige tilfælde, og det tager som regel omkring tredive sekunder.

1. Sæt TV'et på **det samme Wi-Fi** som din iPhone.
2. Åbn TV'ets indbyggede medieafspiller. Navnet afhænger af mærket: **Media Player**, **Gallery**, **SmartShare** (LG), **AllShare** eller **SmartThings** (Samsung), **Content Share** eller **SimplyShare**.
3. Find listen over medieservere eller kilder. Din enhed vises der med sit navn.
4. Vælg den, gå ind i dine billeder, videoer eller din musik, og tryk på afspil.

Forhåndsvisningsminiaturer vises automatisk, så du kan finde det rigtige feriealbum eller den rigtige film uden at gætte.

### Hvilke TV virker

De fleste TV fra **Samsung, LG, Sony BRAVIA, Panasonic (VIERA-firmware), Philips og Hisense** har DLNA indbygget og virker med det samme. Det gør **PlayStation- og Xbox-konsoller og de fleste AV-receivere** også.

Nogle få platforme udelader det: **Roku-TV, Amazon Fire TV, Vizio SmartCast og almindelig Google TV** uden en producents medieapp. Hvis dit TV er et af disse og ikke kan finde din enhed, er det som regel grunden. På de TV kan du installere en DLNA-afspillerapp som VLC eller Kodi eller i stedet nå dine filer gennem en webbrowser ved hjælp af [vejledningen til WebDAV-opsætning](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/).

Nogle mærker beholdt DLNA i funktion, selv efter at det officielle DLNA-logo blev fjernet, så hvis det ser ud til at mangle, så led efter et af medieafspillernavnene ovenfor.

## Afspil i VLC eller Kodi på Windows, Mac og Linux

VLC og Kodi er gratis, kører på alle stationære systemer og taler DLNA godt. De er den pålidelige måde at åbne dit Everdisk-bibliotek på en computer.

**VLC (Windows, Mac, Linux):**

1. Åbn VLC.
2. Vis afspilningslisten (på Windows og Linux tryk på **Ctrl+L**, på Mac åbn **Playlist** fra menuen View).
3. I sidebjælken åbner du **Universal Plug'n'Play** under Local Network.
4. Din enhed vises på listen. Klik ind i den, og vælg en fil.

**Kodi (Windows, Mac, Linux):**

1. Gå til **Videos**, **Music** eller **Pictures**, derefter **Files**, derefter **Add source** (eller **Browse**).
2. Vælg **UPnP devices**.
3. Vælg din enhed, og gennemse dit bibliotek.

På Windows kan du også åbne **Windows Media Player**, udvide **Other Libraries** i sidebjælken, og din enhed dukker op der.

## Afspil på Android

Android-telefoner og -tablets har ikke en system-DLNA-browser, så brug en app:

- **VLC for Android**: åbn sidemenuen, tryk på **Local Network**, og din enhed vises under UPnP-servere.
- **BubbleUPnP** eller en lignende UPnP-app: din enhed dukker op på serverlisten, og disse apps kan også skubbe afspilningen til et TV.

## Afspil på en anden iPhone eller iPad

To enheder, ét bibliotek. Sig, at billederne er på din iPhone, og du vil se dem på din iPad.

- Den enkleste vej er Everdisks egen fane **Enheder** på den anden enhed. Den fungerer både som DLNA-klient og server. Åbn Everdisk på iPad'en, gå til **Enheder**, og din iPhone vises under **Tilgængelige enheder**. Tryk på den for at gennemse og afspille.
- Enhver DLNA-afspillerapp til iOS virker også, såsom VLC eller en UPnP-browser. Åbn dens visning af det lokale netværk, og vælg din iPhone.

## Afspil på en spillekonsol

- **PlayStation 5 og 4**: åbn appen **Media** (Media Gallery), og din enhed dukker op som en medieserver, du kan gennemse.
- **Xbox**: brug en medieafspillerapp, der understøtter DLNA, og vælg derefter din enhed fra serverlisten.

## Hvis din enhed ikke vises på listen

Nogle afspillere lader dig tilføje en medieserver efter adresse i stedet for at vente på, at den bliver fundet. På Everdisks skærm **Deling** viser DLNA-kortet en enhedsbeskrivelsesadresse, der ender på `/device-desc.xml`. Indtast den adresse i afspillerens felt til tilføjelse af server.

Hvis den stadig ikke dukker op, så tjek tre ting: at begge enheder er på det samme Wi-Fi (ikke et gæstenetværk, der blokerer trafik mellem enheder), at Everdisk er åben, og deling er startet, og at **Tv og mediecenter** er slået til i Indstillinger.

## Hvis en video ikke vil afspilles

DLNA rækker filen til TV'et, som den er, og TV'et skal kunne afkode den. Hvis et klip nægter at afspille, understøtter det pågældende TV sandsynligvis ikke dets format. To løsninger:

- Åbn **Indstillinger**, derefter **Deling**, derefter **Videoer**, og sænk **Kvalitet**. Everdisk konverterer så videoen til et mere kompatibelt format, mens den streamer. (Konvertering er en Premium-funktion.)
- Eller åbn den samme fil i en webbrowser ved hjælp af Everdisks browserlink, som er mere tilgivende med hensyn til formater.

## Sådan bruger folk det i praksis

- **Filmaften med familien.** Videoer optaget på din telefon afspilles på stue-TV'et uden et kabel eller et Apple TV.
- **Feriebilleder på den store skærm.** Åbn dit Billeder-bibliotek på TV'et, og swipe gennem turen med alle i rummet.
- **Baggrundsmusik til en fest.** Peg en DLNA-højttaler eller en AV-receiver mod dit Musik-bibliotek, og lad det køre.
- **Se med på et hotel-TV**, der har en medieafspiller, når først begge enheder er på værelsets Wi-Fi.

## Et par tips

- Hold Everdisk åben, mens du streamer. Hvis du låser telefonen i lang tid, kan iOS sætte appen på pause, og afspilningen stopper.
- Sæt telefonen til strøm ved lange filmsessioner.
- For den hurtigste streaming holder du **Format** og **Kvalitet** på **Original** i Indstillinger og sænker dem kun, hvis et bestemt TV har problemer med en fil.
- DLNA er kun streaming. Ingen på TV-siden kan ændre eller slette dine filer. Til tovejsfiloverførsel bruger du i stedet [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)-, [WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/)- eller [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/)-serveren.

## Ofte stillede spørgsmål

{{% details title="Hvad er forskellen på DLNA og UPnP?" closed="true" %}}
De er nært beslægtede. UPnP er den underliggende netværksstandard, og DLNA er den medieprofil, der er bygget ovenpå, og som TV og afspillere bruger til at dele og afspille billeder, videoer og musik. I daglig brug er ordene indbyrdes udskiftelige. Når du slår Tv og mediecenter til i Everdisk, bliver din enhed til en DLNA/UPnP-medieserver, som enhver DLNA-klient kan gennemse.
{{% /details %}}

{{% details title="Skal jeg installere noget på mit TV?" closed="true" %}}
Nej. Hvis dit TV understøtter DLNA, har det allerede en medieafspiller, der kan finde din enhed på Wi-Fi. Du installerer kun Everdisk på den iPhone eller iPad, der indeholder indholdet. Hvis dit TV ikke understøtter DLNA, installerer du en afspiller som VLC eller Kodi på en enhed, der er tilsluttet det.
{{% /details %}}

{{% details title="Hvorfor dukker min iPhone ikke op på TV'et?" closed="true" %}}
Tjek, at begge enheder er på det samme Wi-Fi-netværk. Gæstenetværk og nogle kontor- eller hotelnetværk blokerer, at enheder kan se hinanden, hvilket stopper DLNA. Bekræft derefter, at Everdisk er åben, og deling er startet, og at Tv og mediecenter er slået til i Indstillinger, Deling, Forbindelser. Hvis TV'et stadig ikke kan finde den, så tilføj serveren manuelt ved hjælp af enhedsbeskrivelsesadressen, der ender på /device-desc.xml.
{{% /details %}}

{{% details title="Kræver DLNA-streaming en adgangskode?" closed="true" %}}
Nej. DLNA er altid åben for alle på det samme Wi-Fi, mens det er slået til, hvilket er grunden til, at der ikke er noget login på TV-siden. Det er fint på et hjemmenetværk, du har tillid til. På et netværk, du ikke har tillid til, slår du Tv og mediecenter fra, når du er færdig, eller bruger i stedet SMB-serveren med kryptering.
{{% /details %}}

{{% details title="Kan jeg streame til en Chromecast eller Roku?" closed="true" %}}
Chromecast og Roku fungerer ikke som DLNA-afspillere fra starten, så de finder ikke din enhed direkte. Løsningen er at installere en DLNA-app, der kan caste, såsom VLC eller BubbleUPnP på en telefon, og skubbe afspilningen til Chromecast eller Roku derfra. På de fleste andre smart-TV virker DLNA uden noget af dette.
{{% /details %}}

{{% details title="En video afspilles uden lyd eller vil ikke åbne. Hvad kan jeg gøre?" closed="true" %}}
Det er et format, TV'et ikke kan afkode. Åbn Indstillinger, Deling, Videoer i Everdisk, og sænk Kvalitet, så appen konverterer videoen til et mere kompatibelt format, mens den streamer. Du kan også åbne den samme fil gennem browserlinket, som håndterer flere formater.
{{% /details %}}

{{% details title="Kan jeg streame musik og ikke kun video?" closed="true" %}}
Ja. Slå Tillad adgang til hele musikbiblioteket til, eller tilføj bestemte numre, og start derefter deling. Dine sange vises på enhver DLNA-højttaler, AV-receiver eller ethvert TV med albumbilleder og nummeroplysninger. Musik deles altid i original kvalitet.
{{% /details %}}

{{% details title="Skal appen forblive åben, mens jeg ser med?" closed="true" %}}
Ja. Din iPhone fungerer som server, og iOS sætter apps på pause, der skubbes helt i baggrunden i lang tid. Hold Everdisk på skærmen, mens du streamer, og sæt til strøm ved lange sessioner.
{{% /details %}}

{{% details title="Hvordan streamer jeg fra én iPhone til en anden iPad?" closed="true" %}}
Start deling på iPhonen, åbn derefter Everdisk på iPad'en, og gå til fanen Enheder. iPhonen vises under Tilgængelige enheder som en medieserver. Tryk på den for at gennemse og afspille. Everdisk fungerer som DLNA-klient og server, så du behøver ikke en anden app.
{{% /details %}}

{{% details title="Er Everdisk gratis?" closed="true" %}}
Ja, Everdisk er gratis at downloade, og DLNA-medieserveren er inkluderet. Et valgfrit engangskøb af Premium Lifetime tilføjer ekstra funktioner som billed- og videokonvertering til ældre TV, brugerdefinerede porte og mere. Du kan opsætte og bruge DLNA-streaming uden at betale.
{{% /details %}}

Klar til at prøve det? [Download Everdisk fra App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8), og stream dit første album til TV'et på et par minutter. Spørgsmål eller feedback? Skriv til os på **support@everappz.com**.
