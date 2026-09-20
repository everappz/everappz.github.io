---
title: "Sådan opsætter du en SMB-server på iPhone og iPad til fildeling"
description: "Gør din iPhone eller iPad til en SMB-filserver med Everdisk, og åbn den som et netværksdrev fra en Mac, en anden iPhone, Linux eller Android over Wi-Fi. Fuld opsætning, smb-adressen og porten, valgfri SMB3-kryptering og trinvis forbindelse for hver enhed."
date: 2026-09-19
tags: ["everdisk", "smb", "fildeling", "netværksdrev", "iphone", "ipad", "mac", "finder", "kryptering", "wifi"]
keywords: ["SMB-server iPhone", "SMB-server iPad", "sådan opsætter du SMB på iPhone", "iPhone SMB-deling", "forbind iPhone SMB Mac Finder", "smb iphone til iphone", "iOS Filer-app forbind til server SMB", "del filer iPhone SMB", "iphone netværksdrev Finder", "SMB3-kryptering iOS", "smb-deling iPhone Android", "forbind til SMB fra Linux", "iphone som netværksdrev", "del filer mellem iphones wifi", "tilslut iphone som netværksdrev"]
readingTime: 10
---

{{< author-byline >}}

SMB er den fildeling, der er indbygget i macOS, Windows og Linux og i næsten alle netværksdrev (NAS). Når du forbinder til en delt mappe på en anden computer, og den åbnes som en almindelig disk i Finder eller File Explorer, er det SMB, der gør arbejdet. Med [Everdisk](/products/everdisk) kan du lægge en SMB-deling på din iPhone eller iPad, så telefonen selv dukker op som et netværksdrev, som andre enheder gennemser, kopierer fra og kopierer til.

Dette er den mulighed, du skal gribe fat i, når du vil have din iPhone til at opføre sig som et rigtigt drev og ikke en webside. Det er hurtigt, det trækker og slipper begge veje, og det er den eneste forbindelsestype i Everdisk, der kan kryptere hver overførsel. Denne vejledning dækker opsætningen, og hvordan du forbinder fra en Mac, en anden iPhone eller iPad, Linux, Android og Windows.

## Det skal du bruge

- En iPhone eller iPad med [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installeret.
- En anden enhed på **det samme Wi-Fi-netværk**.
- De filer, du vil dele, i Everdisks Dokumenter-mappe eller i mapper, du tilføjer.

## Opsæt SMB-serveren i Everdisk

### Trin 1: Vælg, hvad der skal deles, og hvem der kan skrive

Åbn Everdisk, gå til fanen **Deling**, og tryk på **Hvad skal deles**. Dokumenter-mappen deles som standard. Tilføj mere med **Tilføj mappe** og **Tilføj fil**, og slå dit billed- eller musikbibliotek til, hvis du også vil have dem tilgængelige.

Beslut, om andre enheder kun kan læse dine filer eller også ændre dem. Åbn **Indstillinger**, derefter **Deling**, derefter **Adgang**, og indstil **Filredigering**. Med den slået til kan tilsluttede enheder kopiere filer over på din telefon og omdøbe eller slette dem. Med den slået fra er delingen skrivebeskyttet.

Hvis du vil have et login, indstiller du et **Login** og en **Adgangskode** på den samme Adgang-skærm. Lad begge stå tomme for at tillade gæsteadgang.

### Trin 2: Slå SMB-serveren til

Gå til **Indstillinger**, derefter **Deling**, derefter **Forbindelser**, og slå **Computer (avanceret)** til. Det er SMB-serveren (den bærer SMB-mærket).

### Trin 3: Start deling, og notér adressen

Gå tilbage til fanen **Deling**, og tryk på **Start**. Afsnittet **Sådan opretter du forbindelse** viser nu SMB-adressen. Den ser sådan ud:

```
smb://192.168.1.20:4455/Share
```

Tre ting at vide om den adresse:

- Tallet efter kolon er **porten**. Everdisk bruger **4455** som standard.
- Delingen hedder **Share**.
- Den første del er din iPhones adresse på Wi-Fi, så den vil være anderledes på dit netværk.

Hold Everdisk åben, mens enheder er forbundet, fordi iOS sætter apps på pause, der ligger for længe i baggrunden.

## Forbind fra en Mac

Dette er det mest gnidningsfrie tilfælde, fordi macOS taler SMB indbygget.

Den hurtigste måde: åbn **Finder**, og kig i sidebjælken under **Placeringer** eller **Netværk**. Everdisk annoncerer sig selv på Wi-Fi, så din iPhone dukker ofte op der af sig selv. Klik på den, klik derefter på **Opret forbindelse som**, og vælg **Gæst**, eller indtast dit login.

Sådan forbinder du manuelt:

1. I Finder vælger du **Gå**, derefter **Opret forbindelse til server** (eller tryk på **Command og K**).
2. Indtast den SMB-adresse, der vises i Everdisk, for eksempel `smb://192.168.1.20:4455/Share`.
3. Klik på **Opret forbindelse**, og vælg derefter **Gæst**, eller indtast dit **Login** og din **Adgangskode**.

Din iPhone åbnes i et Finder-vindue. Kopier filer ind eller ud ved at trække, præcis som ethvert andet drev (hvis Filredigering er slået til).

## Forbind fra en anden iPhone eller iPad

iOS og iPadOS kan åbne SMB-delinger i den indbyggede **Filer**-app, hvilket gør overførsler fra telefon til telefon rene og hurtige.

På den anden enhed:

1. Åbn **Filer**-appen.
2. Tryk på **mere**-knappen (de tre prikker, øverst til højre på iPhone), og vælg **Opret forbindelse til server**.
3. Indtast SMB-adressen fra Everdisk, for eksempel `smb://192.168.1.20:4455/Share`.
4. Vælg **Gæst**, eller **Registreret bruger**, og indtast dit login.
5. Delingen vises under Placeringer i Filer. Gennemse og kopier i begge retninger.

Du kan også bruge Everdisks egen fane **Enheder** på den anden enhed, som indeholder en SMB-klient. Åbn Everdisk, gå til **Enheder**, tryk på **Ny forbindelse**, vælg **SMB**, og indtast adressen.

## Forbind fra Linux

1. Åbn din filhåndtering (Files/Nautilus på GNOME, Dolphin på KDE).
2. Vælg **Other Locations** eller **Connect to Server**.
3. Indtast adressen, for eksempel `smb://192.168.1.20:4455/Share`.
4. Forbind som gæst, eller indtast dit login.

Fra en terminal kan du også køre `smbclient //192.168.1.20/Share -p 4455` og indtaste dit login, når du bliver bedt om det.

## Forbind fra Android

Android har ikke en system-SMB-browser, så brug en filhåndtering, der understøtter SMB:

1. Installer en app såsom **CX File Explorer**, **Solid Explorer** eller **X-plore File Manager**.
2. Tilføj en ny **SMB**- eller **LAN**-forbindelse.
3. Indtast værten (din iPhones Wi-Fi-adresse), sæt **porten til 4455**, og delingsnavnet **Share**.
4. Forbind som gæst eller med dit login, og gennemse og kopier derefter.

## Forbind fra Windows

Windows kan læse SMB-delinger, med en enkelt hage værd at kende på forhånd. Den indbyggede File Explorer taler kun med SMB på standardporten og lader dig ikke skrive en brugerdefineret port i stien, og Everdisk bruger port 4455. Så den almindelige rute **Tilslut netværksdrev** når ofte ikke frem til den.

Du har to gode muligheder på Windows:

- Brug en filhåndtering eller SMB-klient, der lader dig indstille en brugerdefineret port, og peg den mod din iPhones adresse med port **4455** og delingsnavnet **Share**.
- Eller forbind fra Windows med en af Everdisks andre servere i stedet. [WebDAV-opsætningen](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) og [FTP-opsætningen](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) virker begge godt fra Windows File Explorer, og browserlinket virker i enhver browser.

Hvis du gerne vil prøve Tilslut netværksdrev: åbn **File Explorer**, højreklik på **Denne pc**, vælg **Tilslut netværksdrev**, og indtast værten og delingsnavnet, der vises i Everdisk. Hvis den ikke kan forbinde, er det portbegrænsningen ovenfor, så skift til WebDAV eller FTP.

## Slå kryptering til for Wi-Fi, du ikke har tillid til

SMB er den eneste Everdisk-forbindelse, der kan kryptere hver overførsel, hvilket har betydning på Wi-Fi, du ikke fuldt ud kontrollerer, som en café eller et kontornetværk.

1. I **Indstillinger**, **Deling**, **Adgang** indstiller du et **Login** og en **Adgangskode**. Krypterede forbindelser kan ikke være anonyme, så dette trin er påkrævet.
2. I **Indstillinger**, **Deling** slår du **Kræv SMB-kryptering** til.
3. Stop og start deling igen, så ændringen træder i kraft.

Hver SMB-overførsel er derefter beskyttet med **SMB3-kryptering (AES)**. Den enhed, der forbinder, skal understøtte SMB3, hvilket Finder på en moderne Mac og Windows 10 eller nyere begge gør. SMB-kryptering er en del af engangskøbet af Premium.

## Skrivebeskyttet eller læse og skrive

Kontakten **Filredigering** i Indstillinger, Deling, Adgang styrer dette for hver server, herunder SMB. Slå den til, så kan tilsluttede enheder uploade, omdøbe og slette. Slå den fra, så kan de kun gennemse og kopiere filer fra din telefon. Vælg skrivebeskyttet, når du rækker filer til nogen, du ikke vil have til at ændre noget.

## Sådan bruger folk det i praksis

- **Flyt en stor mappe over på din iPhone fra en Mac** ved at trække den ind i Finder-vinduet, hurtigere end en web-upload.
- **Hent en dags billeder og videoer af din telefon** over på en bærbar uden iTunes eller et kabel.
- **Send filer mellem to iPhones** gennem Filer-appen, uden en tredje app i nogen af enderne.
- **Arbejd med en fil på stedet**, ved at åbne et dokument direkte fra telefonen i en app på din Mac og gemme det tilbage.

## Et par tips

- Hold Everdisk åben, mens en enhed er forbundet. Hvis telefonen låses i lang tid, kan appen sættes på pause og forbindelsen falde.
- Hvis en Mac ikke kan se telefonen i Finder-sidebjælken, så forbind manuelt med Opret forbindelse til server og den fulde smb-adresse.
- For den bedste hastighed ved store overførsler holder du billed- og videokvaliteten på Original i Indstillinger.
- På et netværk, du ikke har tillid til, slår du Kræv SMB-kryptering til og slår de andre servere fra, mens du arbejder.

## Ofte stillede spørgsmål

{{% details title="Hvad er SMB-adressen og porten til min iPhone?" closed="true" %}}
Efter du starter deling, viser Everdisk adressen på Deling-skærmen. Den ser ud som smb://192.168.1.20:4455/Share. 4455 er den port, Everdisk bruger til SMB, og Share er navnet på den delte mappe. Den første del er din iPhones adresse på Wi-Fi, så din vil være anderledes.
{{% /details %}}

{{% details title="Kan jeg forbinde til min iPhones SMB-deling fra Windows?" closed="true" %}}
Windows File Explorer forbinder kun til SMB på standardporten og accepterer ikke en brugerdefineret port i stien, mens Everdisk bruger port 4455. Så den almindelige rute Tilslut netværksdrev når ofte ikke frem til den. Brug en filhåndtering, der lader dig indstille en brugerdefineret port, eller forbind fra Windows med WebDAV, FTP eller browserlinket i stedet. Alle disse virker fra Windows uden portproblemer.
{{% /details %}}

{{% details title="Hvordan deler jeg filer mellem to iPhones med SMB?" closed="true" %}}
Start SMB-serveren på den første iPhone i Everdisk. På den anden iPhone åbner du Filer-appen, trykker på mere-knappen, vælger Opret forbindelse til server og indtaster den smb-adresse, der vises i Everdisk (for eksempel smb://192.168.1.20:4455/Share). Forbind som Gæst eller med dit login, og delingen vises i Filer. Du kan også bruge Everdisks egen fane Enheder på den anden telefon.
{{% /details %}}

{{% details title="Dukker min iPhone op i Mac Finder-sidebjælken automatisk?" closed="true" %}}
Som regel ja. Everdisk annoncerer SMB-delingen på dit Wi-Fi, så din iPhone dukker ofte op under Placeringer eller Netværk i Finder-sidebjælken. Klik på den, og vælg Opret forbindelse som, derefter Gæst eller dit login. Hvis den ikke dukker op, så forbind manuelt med Gå, Opret forbindelse til server og den fulde smb-adresse.
{{% /details %}}

{{% details title="Skal jeg bruge en adgangskode for at bruge SMB?" closed="true" %}}
Nej, et login er valgfrit. Lad Login og Adgangskode stå tomme i Indstillinger, Deling, Adgang for at tillade gæsteadgang. Indstil dem, hvis du vil have forbindelser til at logge ind. Et login og en adgangskode er kun påkrævet, hvis du slår Kræv SMB-kryptering til, fordi krypterede forbindelser ikke kan være anonyme.
{{% /details %}}

{{% details title="Er SMB-forbindelsen krypteret?" closed="true" %}}
Det kan den være. SMB er den eneste Everdisk-forbindelse, der understøtter kryptering. Indstil et login og en adgangskode, og slå derefter Kræv SMB-kryptering til i Indstillinger, Deling. Hver overførsel er derefter beskyttet med SMB3 (AES). Den anden enhed skal understøtte SMB3, hvilket moderne Mac-computere og Windows 10 eller nyere gør. Kryptering er en Premium-funktion.
{{% /details %}}

{{% details title="Kan folk ændre eller slette mine filer over SMB?" closed="true" %}}
Kun hvis du tillader det. Kontakten Filredigering i Indstillinger, Deling, Adgang styrer dette. Med den slået til kan tilsluttede enheder uploade, omdøbe og slette. Med den slået fra er delingen skrivebeskyttet, og andre kan gennemse og kopiere filer fra din telefon, men kan ikke ændre noget.
{{% /details %}}

{{% details title="Hvorfor faldt min SMB-forbindelse?" closed="true" %}}
Din iPhone er serveren, og iOS sætter apps på pause, der ligger for længe i baggrunden. Hold Everdisk åben på skærmen, mens en enhed er forbundet, og sæt telefonen til strøm ved lange overførsler. Sørg også for, at begge enheder blev på det samme Wi-Fi.
{{% /details %}}

{{% details title="SMB, WebDAV eller FTP, hvilken skal jeg bruge?" closed="true" %}}
Brug SMB, når du vil have telefonen til at opføre sig som et rigtigt netværksdrev på en Mac, en anden iPhone, Linux eller et NAS, og når du vil have kryptering. Brug WebDAV, når du vil have et netværksdrev, der også virker godt fra Windows. Brug FTP for den bredeste kompatibilitet med ældre enheder og apps. Everdisk kan køre dem alle på én gang, så du er ikke låst fast til én.
{{% /details %}}

{{% details title="Er Everdisk gratis?" closed="true" %}}
Ja, Everdisk er gratis at downloade, og SMB-serveren er inkluderet. Det valgfrie engangskøb af Premium tilføjer SMB-kryptering, brugerdefinerede porte og et par andre ekstra funktioner. Du kan opsætte SMB og dele filer uden at betale.
{{% /details %}}

Klar til at prøve det? [Download Everdisk fra App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8), og åbn din iPhone i Finder på cirka et minut. Spørgsmål eller feedback? Skriv til os på **support@everappz.com**.
