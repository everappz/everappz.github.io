---
date: '2025-06-12T17:00:00+00:00'
draft: false
title: 'Často kladené otázky'
description: 'Nájdite odpovede na bežné otázky o Evermusic, Flacbox, Evervideo a Evertag. Preskúmajte funkcie ako streamovanie z cloudu, správu súborov, možnosti prehrávania, úpravu metadát a ďalšie.'
keywords: [
  "Evermusic FAQ", "podpora Flacbox", "pomoc Evervideo", "otázky Evertag",
  "ako používať Evermusic", "riešenie problémov cloudového hudobného prehrávača", "sprievodca offline prehrávaním",
  "podpora editora zvukových tagov", "problémy so streamovaním videa", "návod na prenos súborov"
]
tags: [
  "FAQ", "pomoc", "podpora", "evermusic", "flacbox", "evervideo", "evertag",
  "nastavenie cloudu", "problémy s prehrávaním", "správa súborov", "úprava metadát",
  "riešenie problémov", "offline režim", "hudobný prehrávač", "video prehrávač"
]
aliases:
  - /blog/categories/how-to/
---


{{< lottie src="/images/juicy-json/juicy-woman-focused-on-online-learning.json" width="85%" >}}

## Zistite, ako používať naše aplikácie

Hľadáte odpovede alebo pomoc pri používaní jednej z našich aplikácií? Ste na správnom mieste.

Naše stránky s FAQ vám pomôžu pripojiť cloudové úložisko, spravovať hudobné a video súbory, nastaviť offline prehrávanie, upraviť nastavenia ekvalizéra, opraviť metadáta a oveľa viac.

Preskúmajte FAQ pre vašu aplikáciu nižšie, aby ste mohli začať, alebo si prezrite bežné otázky a odpovede, ktoré sme dostali od používateľov e-mailom.

## Vyberte svoju aplikáciu

{{< cards cols="2">}}

{{< card 
  link="/docs/faq/evervideo" 
  title="Evervideo" 
  subtitle="Prehrávajte 360° videá, streamujte z iCloud, sledujte s titulkami, používajte video ekvalizér, organizujte obsah so zoznamami skladieb a sťahujte videá na offline sledovanie."
  image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< card 
  link="/docs/faq/evermusic"
  title="Evermusic" 
  subtitle="Cloudový hudobný prehrávač s offline režimom, audio ekvalizérom, crossfade, bezšvíkovým prehrávaním, správou zoznamov skladieb, plnou hudobnou knižnicou a vstavaným správcom súborov."
  image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/flacbox"
  title="Flacbox" 
  subtitle="Hi-res audio prehrávač pre iPhone a Mac. Počúvajte hudbu v bezstratových formátoch ako FLAC, ALAC, APE a DSD. Jemne dolaďte výstup pomocou pokročilých nastavení zvuku."
  image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/evertag"
  title="Evertag" 
  subtitle="Inteligentný editor hudobných tagov s dávkovým úpravám. Opravte chýbajúce metadáta, obaly albumov a ďalšie. Upravujte tagy ID3, FLAC, APE — podporovaných viac ako 120 polí." 
  image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< /cards >}}

## Bežné problémy a odpovede

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{% details title="Prečo sa nemôžem prihlásiť do pCloud na staršej verzii iOS (15.8.4)?" closed="true" %}}
Webová prihlasovacia stránka pCloud sa nemusí správne zobrazovať na starších verziách iOS, ako je 15.8.4, čo bráni zadaniu e-mailu a hesla na obrazovke cloudového pripojenia.<br><br>

Ako riešenie môžete použiť protokol **WebDAV**, ktorý pCloud podporuje a spoľahlivo funguje na všetkých verziách iOS.

**Nastavenie WebDAV:**<br>
- **Servery USA:** `https://webdav.pcloud.com`  
- **Európske servery:** `https://ewebdav.pcloud.com`  
- **Používateľské meno:** Vaša e-mailová adresa pCloud  
- **Heslo:** Heslo vášho účtu pCloud  

Otvorte aplikáciu → Pripojenia → Pripojiť sa k cloudovému úložisku → Vyberte **WebDAV** → Zadajte svoje prihlasovacie údaje a URL servera.

Táto metóda vám umožní pripojiť sa k vášmu úložisku pCloud a pristupovať k súborom bez problémov na starších zariadeniach.
{{% /details %}}

{{% details title="Ako prehrávať hudbu cez AirPlay z Mac (macOS)?" closed="true" %}}
Verzia aplikácie pre macOS neobsahuje vstavaté tlačidlá pripojenia AirPlay, Chromecast ani Bluetooth ako v iOS.<br><br>

Ak chcete používať **AirPlay** na MacBook Pro, postupujte takto:

1. Prejdite do **pravého horného rohu** obrazovky a otvorte **Ovládacie centrum** (vedľa hodín).  
2. Kliknite na ikonu **Zvuk/Hlasitosť**.  
3. Na ďalšej obrazovke kliknite na **AirPlay**, aby ste zobrazili zoznam všetkých dostupných zariadení AirPlay.  
4. Vyberte požadované zariadenie a začnite streamovať hudbu.  

Tým sa všetok systémový zvuk (vrátane Evermusic alebo Flacbox) presmeruje na vybrané zariadenie AirPlay.
{{% /details %}}

{{% details title="Prečo sa môj nákup Premium neaktivoval na Mac, ak som ho kúpil na iPhone?" closed="true" %}}
Doživotné nákupy a predplatné sú synchronizované medzi iOS a Mac cez **iCloud**.<br><br>

Aktivácia Premium na Mac:<br>
- Uistite sa, že máte na oboch zariadeniach nainštalovanú najnovšiu verziu aplikácie<br>
- Aktivujte **iCloud** na oboch zariadeniach<br>
- Spustite aplikáciu na zariadení iOS a počkajte 1 minútu, kým sa informácie o nákupe nahrajú<br>
- Na Mac nainštalujte aplikáciu z App Store pomocou rovnakého **Apple ID**<br>
- Spustite aplikáciu a počkajte niekoľko sekúnd na synchronizáciu informácií<br>
- Prípadne klepnite na **Obnoviť nákupy** v nastaveniach aplikácie na oboch zariadeniach<br><br>

Funkcie Premium by sa potom mali automaticky aktivovať na Mac.
{{% /details %}}

{{% details title="Ako môžem automaticky synchronizovať zoznamy skladieb medzi zariadeniami?" closed="true" %}}
V súčasnosti neexistuje **automatická synchronizácia** zoznamov skladieb.<br><br>

Môžete použiť jednu z nasledujúcich možností:<br>
- **Zálohovanie a obnovenie** z nastavení aplikácie [Ako preniesť hudobnú knižnicu medzi zariadeniami v Evermusic: podrobný sprievodca](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/)<br>
- **Export zoznamu skladieb do M3U**, potom import na iné zariadenie:<br>
  - [Ako exportovať zoznamy skladieb](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/)<br>
  - [Ako importovať zoznamy skladieb](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/)<br>
- **Archivovať zoznam skladieb alebo albumy** a preniesť cez ZIP:<br>
  - [Sprievodca archivovaním zoznamov skladieb](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to/)
{{% /details %}}

{{% details title="Je bezpečné používať vaše aplikácie? Môžem zakázať analytiku?" closed="true" %}}
Áno, vaše súkromie je naša najvyššia priorita.<br><br>

- Všetky dáta — hudobné súbory, nastavenia, cloudové prihlásenia — zostávajú na vašom zariadení<br>
- Prihlasovacie údaje sú bezpečne uložené v **iOS Keychain**<br>
- Zbierame iba anonymné správy o zlyhaní a používaní<br>
- Môžete sa odhlásiť v **Nastaveniach aplikácie → Analytika**<br><br>

Ďalšie informácie:<br>
- [Zásady ochrany osobných údajov](/legal/privacy-policy/)<br>
- [Zabezpečenie Apple Keychain](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web)<br><br>

Pri používaní personalizovaných reklám vyžaduje Google Mobile Ads zobrazenie nastavení súhlasu.<br>
Prémiovi používatelia nevidia reklamy a reklamný SDK je úplne zakázaný.
{{% /details %}}

{{% details title="Podporujú vaše aplikácie Zdieľanie rodiny?" closed="true" %}}
Áno, Zdieľanie rodiny je podporované.<br><br>

Zdieľanie nákupov v aplikácii:<br>
- Uistite sa, že nákup je nastavený na zdieľanie s vašou rodinnou skupinou<br>
- Na zariadení člena rodiny prejdite na **Nastavenia > Nákupy > Obnoviť nákupy**<br>
- Tým sa požiadajú údaje o nákupe zo serverov Apple a aktivujú sa na ich zariadení
{{% /details %}}

{{% details title="Ako urýchliť metadáta a cloudovú synchronizáciu?" closed="true" %}}
Na zlepšenie rýchlosti synchronizácie aktivujte úlohy na pozadí:<br><br>

- **Nastavenia → Hudobná knižnica → Čítanie metadát → Čítanie metadát na pozadí**<br>
- **Nastavenia → Hudobná knižnica → Synchronizácia online hudby → Synchronizácia na pozadí**<br><br>

Tiež na macOS zvýšte rýchlosť čítania metadát cez **Nastavenia → Hudobná knižnica**.<br>
Ak je prehrávač aktívny (prehráva sa zvuk), iOS nebude aplikáciu pozastavovať, čo umožní nepretržitú synchronizáciu.
{{% /details %}}

{{% details title="Ako môžem zrušiť predplatné?" closed="true" %}}
Predplatné môžete zrušiť podľa oficiálnych pokynov Apple:<br>
👉 [Ako zrušiť predplatné](https://support.apple.com/en-us/118428)
{{% /details %}}

{{% details title="Ako sa pripojiť a streamovať zvuk z WD MyCloud EX2 Ultra?" closed="true" %}}

Keď pridáte pripojenie v aplikácii cez **Pripojenia > Pripojiť sa k cloudovému úložisku > My Cloud Home**, je oficiálne navrhnuté na podporu zariadení **WD MyCloud Home**.<br>
WD MyCloud EX2 Ultra používa obmedzený prístup pre aplikácie.<br><br>

Ak ste sa však úspešne pripojili k **WD MyCloud EX2 Ultra**, **WD MyCloud Mirror** alebo inému modelu úložiska **WD MyCloud**, môžete ho stále používať s nasledujúcim riešením:<br><br>

1. Otvorte **Pripojenia → Pripojiť sa k cloudovému úložisku → My Cloud Home**<br>
2. Vytvorte priečinok pomocou vstavaného správcu súborov<br>
3. Nahrajte hudobné súbory do tohto priečinka<br>
4. Tieto sa uložia do „sandboxu" dostupného iba pre aplikáciu<br>
5. Teraz ich môžete priamo streamovať alebo sťahovať<br><br>

⚠️ Z NAS budú prístupné iba priečinky vytvorené cez aplikáciu.
{{% /details %}}

{{% details title="Ako sa pripojiť ku Koofr.eu?" closed="true" %}}
Koofr môžete pripojiť pomocou **WebDAV**.<br><br>

- Sprievodca nastavením Koofr WebDAV: [blog koofr.eu](https://koofr.eu/blog/posts/3-ways-to-map-koofr-as-a-network-drive-explained)<br>
- Sprievodca WebDAV pre Evermusic/Flacbox: [Ako pripojiť úložisko NAS pomocou WebDAV a počúvať hudbu na iPhone alebo Mac](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)
{{% /details %}}

{{% details title="Aké sú schémy URL aplikácie?" closed="true" %}}
Tu sú podporované schémy:<br><br>

**Evermusic**<br>
- iOS (modrá ikona): `lsevermusic://`<br>
- macOS: `lsevermusicmac://`<br>
- iOS (červená ikona): `lsevermusicpro://`<br><br>

**Flacbox**<br>
- iOS: `lsflap://`<br>
- macOS: `lsflapmac://`<br><br>

**Evertag**<br>
- iOS: `lsevertag://`<br>
- macOS: `lsevertagmac://`<br><br>

**Evervideo**<br>
- iOS: `lsevervideo://`<br>
- macOS: `lsevervideomac://`
{{% /details %}}

{{% details title="Hudba prestane hrať, keď je aplikácia na pozadí — ako to opraviť?" closed="true" %}}
Ak aplikácia zlyhá alebo sa zastaví na pozadí:<br>
- Prejdite na **Nastavenia > Hudobná knižnica > Synchronizácia online hudby > Synchronizácia na pozadí → Zakázať**<br>
- **Nastavenia > Hudobná knižnica > Čítanie metadát > Čítanie metadát na pozadí → Zakázať**<br>
- **Nastavenia > Správca súborov > Prenosy na pozadí → Zakázať**
{{% /details %}}

{{% details title="Bezšvíkové prehrávanie nefunguje — ako to opraviť?" closed="true" %}}
Bezšvíkové prehrávanie závisí od verzie iOS a zvukového enginu.<br>
Skúste prepnúť zvukový engine:<br>
- Prejdite na **Nastavenia → Audio prehrávač → Všeobecné → Audio procesor**<br>
- Vyberte **Core Audio** pre lepšiu podporu bezšvíkového prehrávania
{{% /details %}}

{{% details title="Prečo aplikácia zobrazuje v zozname iba 100 položiek?" closed="true" %}}
Aplikácia používa stránkovanie pre výkon.<br>
Zakázanie stránkovania:<br>
- Prejdite na **Nastavenia → Personalizácia → Limit načítania obsahu → Deaktivovaný**<br>
Teraz sa načítajú všetky položky naraz.
{{% /details %}}

{{% details title="Prečo sú v metadátach podivné znaky?" closed="true" %}}
Skúste zapnúť normalizáciu metadát:<br>
- **Nastavenia → Hudobná knižnica → Čítanie metadát → Normalizovať kódovanie metadát**
{{% /details %}}

{{% details title="Prečo aplikácia nemôže čítať názvy priečinkov so špeciálnymi znakmi?" closed="true" %}}
Ide o známy problém s **protokolom SMB2**.<br><br>

Vyskúšajte nasledujúce riešenia:<br>
- Aktivujte **SMB1** na serveri a v nastaveniach aplikácie<br>
- Použite **systémový výber súborov**:<br>
  - Prejdite na **Lokálne súbory > Súbory na tomto zariadení > Otvoriť súbory...**<br>
  - Vyberte priečinky/súbory pomocou natívneho menu Apple<br><br>

Alternatívne sa pripojte pomocou **WebDAV** alebo **DLNA**, ak ich váš NAS podporuje.
{{% /details %}}

{{% details title="Ako nahrávať hudbu do iCloud a spravovať ju?" closed="true" %}}
– **Ako nahrám hudbu do iCloud?**  <br>
Prejdite na [https://www.icloud.com](https://www.icloud.com) vo svojom prehliadači, vytvorte priečinok a nahrajte svoje hudobné súbory priamo z Mac alebo PC.<br>

– **Ako spravujem úložisko iCloud?**  <br>
Máte dve možnosti:  <br>
1. Použite [https://www.icloud.com](https://www.icloud.com) vo svojom prehliadači na organizovanie, nahrávanie alebo mazanie súborov.<br>  
2. V aplikácii, po pripojení k iCloud cez **Pripojenia → Pripojiť sa k cloudovému úložisku → iCloud Drive**, použite vstavaný správcu súborov na nahrávanie, sťahovanie, premenovanie priečinkov alebo mazanie súborov priamo vo vašom úložisku iCloud — bez uloženia na zariadenie.<br>

⚠️ Pri mazaní súborov buďte opatrní. Aplikácia ich maže natrvalo (nepôjdu do koša a nedajú sa obnoviť).<br>

Viac informácií tu: [Ako streamovať hudbu z iCloud Drive na iPhone alebo Mac](/docs/howto/how-to-listen-to-music-from-icloud-drive-on-your-iphone-or-mac/)

{{% /details %}}

{{% details title="Ako preniesť 10 GB hudobnú knižnicu z Windows 11 na iPhone pre offline prehrávanie?" closed="true" %}}

Máte niekoľko spoľahlivých možností na presunutie hudobnej knižnice z PC so systémom Windows 11 na iPhone a jej používanie offline v aplikácii. Vyberte si metódu, ktorá vám najlepšie vyhovuje:

1. **Použitie káblovho pripojenia (odporúčané pre veľké knižnice)**  <br>
   Použite aplikáciu **Apple Devices** v systéme Windows 11 na priamy prenos súborov do iPhone cez USB.  
   Postupujte podľa sprievodcu Apple tu:  
   https://support.apple.com/en-ph/120402 <br>

2. **Bezdrôtovo cez Wi-Fi Drive**  <br>
   Aktivujte funkciu **WiFi Drive** v aplikácii a nahrajte hudbu prostredníctvom prehliadača v počítači.  
   Podrobné pokyny tu:  
   [Ako preniesť hudobné súbory z počítača do iPhone bez iTunes pomocou WiFi-Drive](/docs/howto/how-to-transfer-music-from-computer-to-iphone-without-itunes/) <br>

3. **Bezdrôtovo pomocou DLNA servera**  <br>
   Zapnite mediálny server DLNA na počítači so systémom Windows a streamujte alebo preneste knižnicu priamo do aplikácie.  
   Sprievodca:  
   [Ako aktivovať mediálny server DLNA v systéme Windows 10 a prehrávať hudbu na iPhone](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/) <br>

4. **Bezdrôtovo pomocou zdieľania súborov SMB**  <br>
   Aktivujte **zdieľanie súborov SMB** na PC a pripojte sa k nemu v aplikácii na prehliadanie, sťahovanie alebo prenos súborov priečinok po priečinku.  
   Pokyny:  
   [Prenos súborov z počítača do iPhone pomocou protokolu SMB](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/) <br>

⚠️ Pri prenose veľkých knižníc (10 GB+) je káblový prenos USB zvyčajne najrýchlejšou a najstabilnejšou možnosťou.

{{% /details %}}

</div>
