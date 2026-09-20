---
title: "Slik setter du opp en DLNA/UPnP-medieserver på iPhone og iPad for streaming"
description: "Gjør iPhone eller iPad om til en DLNA/UPnP-medieserver med Everdisk og stream bilder, videoer og musikk til en smart-TV, spillkonsoll, VLC eller Kodi over Wi-Fi. Komplett oppsett pluss hvordan du kobler til fra Samsung-, LG- og Sony-TV-er, Windows, Mac, Linux, Android og en annen iPhone."
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "medieserver", "streaming", "smart-tv", "iphone", "ipad", "wifi"]
keywords: ["DLNA-server iPhone", "UPnP-server iPad", "hvordan sette opp DLNA på iPhone", "stream til smart-TV fra iPhone", "DLNA-medieserver iOS", "stream videoer til TV uten kabel", "spill iPhone-bilder på TV", "Samsung TV DLNA iPhone", "LG TV DLNA iPhone", "Sony Bravia DLNA iPhone", "VLC DLNA iPhone", "Kodi DLNA-medieserver", "UPnP AV-medieserver iOS", "stream musikk til TV fra iPhone", "iPhone-medieserverapp"]
readingTime: 9
---

{{< author-byline >}}

DLNA (også kalt UPnP AV) er den stille arbeidshesten bak de fleste smart-TV-er. Det er et felles språk som lar en TV eller mediespiller finne et mediebibliotek på samme Wi-Fi og spille av fra det, uten noe å installere på TV-en. Hvis iPhone eller iPad kan opptre som det biblioteket, dukker bildene, videoene og musikken din opp på storskjermen av seg selv.

Denne veiledningen viser hvordan du gjør iPhone eller iPad om til en DLNA/UPnP-medieserver med [Everdisk](/products/everdisk), og hvordan du åpner det biblioteket fra en smart-TV, en spillkonsoll, VLC, Kodi, en datamaskin, en Android-telefon og til og med en annen iPhone. Alt kjører over det lokale Wi-Fi-nettverket ditt, så ingenting lastes opp noe sted.

## Hva du trenger

- En iPhone eller iPad med [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installert.
- En TV, spiller eller datamaskin på **samme Wi-Fi-nettverk** som enheten din.
- Bildene, videoene eller musikken du vil spille av, allerede på iPhone (i Bilder-appen, Musikk-appen eller Everdisks Dokumenter-mappe).

## Sett opp DLNA-serveren i Everdisk

### Steg 1: Velg hva du vil dele

Åpne Everdisk og gå til **Deling**-fanen. Trykk på **Hva du skal dele** og velg innholdet ditt:

- Slå på **Gi tilgang til hele bildebiblioteket** for å dele alle albumene, eller trykk **Legg til bilder** for å velge noen få.
- Slå på **Gi tilgang til hele musikkbiblioteket** for å dele sangene dine, eller trykk **Legg til spor** for et utvalg.
- Legg til mapper eller filer med **Legg til mappe** og **Legg til fil**. Appens egen Dokumenter-mappe deles som standard.

Du må ha minst ett element valgt før deling kan starte.

### Steg 2: Slå på TV og mediesenter (DLNA)

Gå til **Innstillinger**, så **Deling**, så **Tilkoblinger**. Sørg for at **TV og mediesenter** er på. Det er på som standard og bærer DLNA-merket. Dette er serveren som TV-er og spillere leter etter.

### Steg 3: Start delingen

Tilbake på **Deling**-fanen trykker du på den store **Start**-knappen. Enheten din er nå en medieserver på Wi-Fi-nettverket ditt. Den vises for andre enheter under sitt vennlige navn, det som vises som enhetsnavnet ditt i appen (noe sånt som «Speedy-Hare» helt til du endrer det).

DLNA-streaming er alltid åpen, så det er ingen passord å taste inn på TV-en. Hold Everdisk åpen på skjermen mens du ser på, for iOS setter apper som skyves helt i bakgrunnen på pause.

## Spill av på en smart-TV

Dette er det vanligste tilfellet, og det tar som regel omtrent tretti sekunder.

1. Sett TV-en på **samme Wi-Fi** som iPhone.
2. Åpne TV-ens innebygde mediespiller. Navnet avhenger av merket: **Media Player**, **Gallery**, **SmartShare** (LG), **AllShare** eller **SmartThings** (Samsung), **Content Share** eller **SimplyShare**.
3. Se etter listen over medieservere eller kilder. Enheten din vises der ved navnet sitt.
4. Velg den, bla inn i bildene, videoene eller musikken din, og trykk på spill av.

Forhåndsvisningsbilder dukker opp automatisk, så du kan finne riktig ferialbum eller film uten å gjette.

### Hvilke TV-er fungerer

De fleste TV-er fra **Samsung, LG, Sony BRAVIA, Panasonic (VIERA-fastvare), Philips og Hisense** har DLNA innebygd og fungerer med en gang. **PlayStation- og Xbox-konsoller og de fleste AV-mottakere** gjør det også.

Noen få plattformer utelater det: **Roku-TV-er, Amazon Fire TV, Vizio SmartCast og vanlig Google TV** uten en produsents medieapp. Hvis TV-en din er en av disse og ikke finner enheten din, er det som regel grunnen. På slike TV-er kan du installere en DLNA-spillerapp som VLC eller Kodi, eller nå filene dine gjennom en nettleser i stedet med [WebDAV-oppsettveiledningen](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/).

Noen merker beholdt DLNA-funksjonen selv etter at de fjernet den offisielle DLNA-logoen, så hvis det ser ut til å mangle, let etter et av mediespillernavnene over.

## Spill av i VLC eller Kodi på Windows, Mac og Linux

VLC og Kodi er gratis, kjører på alle skrivebordssystemer og snakker DLNA godt. De er den pålitelige måten å åpne Everdisk-biblioteket på en datamaskin.

**VLC (Windows, Mac, Linux):**

1. Åpne VLC.
2. Vis spillelisten (på Windows og Linux trykker du **Ctrl+L**, på Mac åpner du **Playlist** fra Vis-menyen).
3. I sidefeltet åpner du **Universal Plug'n'Play** under Lokalt nettverk.
4. Enheten din vises i listen. Klikk deg inn på den og velg en fil.

**Kodi (Windows, Mac, Linux):**

1. Gå til **Videos**, **Music** eller **Pictures**, så **Files**, så **Add source** (eller **Browse**).
2. Velg **UPnP devices**.
3. Velg enheten din og bla i biblioteket ditt.

På Windows kan du også åpne **Windows Media Player**, utvide **Other Libraries** i sidefeltet, og enheten din dukker opp der.

## Spill av på Android

Android-telefoner og -nettbrett har ingen DLNA-blaerer i systemet, så bruk en app:

- **VLC for Android**: åpne sidemenyen, trykk **Local Network**, og enheten din vises under UPnP-servere.
- **BubbleUPnP** eller en lignende UPnP-app: enheten din dukker opp i serverlisten, og disse appene kan også sende avspilling til en TV.

## Spill av på en annen iPhone eller iPad

To enheter, ett bibliotek. La oss si at bildene er på iPhone og du vil se dem på iPad.

- Den enkleste veien er Everdisks egen **Enheter**-fane på den andre enheten. Den fungerer både som DLNA-klient og server. Åpne Everdisk på iPad, gå til **Enheter**, og iPhone dukker opp under **Tilgjengelige enheter**. Trykk på den for å bla og spille av.
- Hvilken som helst DLNA-spillerapp for iOS fungerer også, som VLC eller en UPnP-blaerer. Åpne dens visning av det lokale nettverket og velg iPhone.

## Spill av på en spillkonsoll

- **PlayStation 5 og 4**: åpne **Media**-appen (Media Gallery), og enheten din dukker opp som en medieserver du kan bla i.
- **Xbox**: bruk en mediespillerapp som støtter DLNA, og velg så enheten din fra serverlisten.

## Hvis enheten din ikke vises i listen

Noen spillere lar deg legge til en medieserver etter adresse i stedet for å vente på at den blir oppdaget. På Everdisks **Deling**-skjerm viser DLNA-kortet en enhetsbeskrivelsesadresse som slutter på `/device-desc.xml`. Skriv inn den adressen i spillerens felt for å legge til server.

Hvis den fortsatt ikke dukker opp, sjekk tre ting: at begge enhetene er på samme Wi-Fi (ikke et gjestenettverk som blokkerer trafikk mellom enheter), at Everdisk er åpen og delingen er startet, og at **TV og mediesenter** er på i Innstillinger.

## Hvis en video ikke vil spilles av

DLNA gir filen til TV-en slik den er, og TV-en må kunne dekode den. Hvis et klipp nekter å spille, støttes formatet sannsynligvis ikke av den TV-en. To løsninger:

- Åpne **Innstillinger**, så **Deling**, så **Videoer**, og senk **Kvalitet**. Everdisk konverterer da videoen til et mer kompatibelt format mens den streamer. (Konvertering er en Premium-funksjon.)
- Eller åpne den samme filen i en nettleser med Everdisks nettleserlenke, som er mer tolerant med formater.

## Måter folk bruker dette i hverdagen

- **Familiefilmkveld.** Videoer filmet på telefonen spilles av på stue-TV-en uten kabel eller Apple TV.
- **Feriebilder på storskjerm.** Åpne bildebiblioteket ditt på TV-en og bla gjennom turen med alle i rommet.
- **Bakgrunnsmusikk i et selskap.** Rett en DLNA-høyttaler eller AV-mottaker mot Musikk-biblioteket ditt og la det gå.
- **Se på en hotell-TV** som har en mediespiller, når begge enhetene er på romets Wi-Fi.

## Noen tips

- Hold Everdisk åpen mens du streamer. Hvis du låser telefonen lenge, kan iOS sette appen på pause og avspillingen stopper.
- Koble telefonen til strøm ved lange filmøkter.
- For raskest streaming holder du **Format** og **Kvalitet** på **Original** i Innstillinger, og senker dem bare hvis en bestemt TV strever med en fil.
- DLNA er kun streaming. Ingen på TV-siden kan endre eller slette filene dine. For toveis filoverføring bruker du [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)-, [WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/)- eller [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/)-serveren i stedet.

## Ofte stilte spørsmål

{{% details title="Hva er forskjellen mellom DLNA og UPnP?" closed="true" %}}
De er nært beslektet. UPnP er den underliggende nettverksstandarden, og DLNA er medieprofilen bygget oppå den som TV-er og spillere bruker for å dele og spille av bilder, videoer og musikk. I dagligtale er ordene utbyttbare. Når du slår på TV og mediesenter i Everdisk, blir enheten din en DLNA/UPnP-medieserver som enhver DLNA-klient kan bla i.
{{% /details %}}

{{% details title="Må jeg installere noe på TV-en?" closed="true" %}}
Nei. Hvis TV-en din støtter DLNA, har den allerede en mediespiller som kan finne enheten din på Wi-Fi. Du installerer bare Everdisk på iPhone eller iPad som inneholder innholdet. Hvis TV-en ikke støtter DLNA, installerer du en spiller som VLC eller Kodi på en enhet som er koblet til den.
{{% /details %}}

{{% details title="Hvorfor dukker ikke iPhone opp på TV-en?" closed="true" %}}
Sjekk at begge enhetene er på samme Wi-Fi-nettverk. Gjestenettverk og noen kontor- eller hotellnettverk blokkerer enheter fra å se hverandre, noe som stopper DLNA. Bekreft så at Everdisk er åpen med delingen startet, og at TV og mediesenter er på i Innstillinger, Deling, Tilkoblinger. Hvis TV-en fortsatt ikke finner den, legg til serveren manuelt med enhetsbeskrivelsesadressen som slutter på /device-desc.xml.
{{% /details %}}

{{% details title="Trenger DLNA-streaming et passord?" closed="true" %}}
Nei. DLNA er alltid åpen for alle på samme Wi-Fi mens den er på, og derfor er det ingen innlogging på TV-siden. Det er greit på et hjemmenettverk du stoler på. På et nettverk du ikke stoler på, slår du av TV og mediesenter når du er ferdig, eller bruker SMB-serveren med kryptering i stedet.
{{% /details %}}

{{% details title="Kan jeg streame til en Chromecast eller Roku?" closed="true" %}}
Chromecast og Roku fungerer ikke som DLNA-spillere rett ut av esken, så de finner ikke enheten din direkte. Løsningen er å installere en DLNA-app som kan caste, som VLC eller BubbleUPnP på en telefon, og sende avspilling til Chromecast eller Roku derfra. På de fleste andre smart-TV-er fungerer DLNA uten noe av dette.
{{% /details %}}

{{% details title="En video spilles av uten lyd eller vil ikke åpnes. Hva kan jeg gjøre?" closed="true" %}}
Det er et format TV-en ikke kan dekode. Åpne Innstillinger, Deling, Videoer i Everdisk og senk Kvalitet slik at appen konverterer videoen til et mer kompatibelt format mens den streamer. Du kan også åpne den samme filen gjennom nettleserlenken, som håndterer flere formater.
{{% /details %}}

{{% details title="Kan jeg streame musikk, ikke bare video?" closed="true" %}}
Ja. Slå på Gi tilgang til hele musikkbiblioteket, eller legg til bestemte spor, og start så delingen. Sangene dine vises på enhver DLNA-høyttaler, AV-mottaker eller TV, med albumbilder og spordetaljer. Musikk deles alltid i original kvalitet.
{{% /details %}}

{{% details title="Må appen holdes åpen mens jeg ser på?" closed="true" %}}
Ja. iPhone opptrer som serveren, og iOS setter apper som skyves helt i bakgrunnen lenge på pause. Hold Everdisk på skjermen mens du streamer, og koble til strøm ved lange økter.
{{% /details %}}

{{% details title="Hvordan streamer jeg fra én iPhone til en annen iPad?" closed="true" %}}
Start delingen på iPhone, åpne så Everdisk på iPad og gå til Enheter-fanen. iPhone dukker opp under Tilgjengelige enheter som en medieserver. Trykk på den for å bla og spille av. Everdisk fungerer både som DLNA-klient og server, så du trenger ingen annen app.
{{% /details %}}

{{% details title="Er Everdisk gratis?" closed="true" %}}
Ja, Everdisk er gratis å laste ned, og DLNA-medieserveren er inkludert. Et valgfritt engangskjøp av Premium Livstid legger til ekstrafunksjoner som konvertering av bilder og video for eldre TV-er, egendefinerte porter og mer. Du kan sette opp og bruke DLNA-streaming uten å betale.
{{% /details %}}

Klar til å prøve? [Last ned Everdisk fra App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) og stream ditt første album til TV-en på et par minutter. Spørsmål eller tilbakemeldinger? Send oss e-post på **support@everappz.com**.
