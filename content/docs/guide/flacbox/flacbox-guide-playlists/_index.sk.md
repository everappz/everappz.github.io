---
title: "Prehrávače"
date: 2020-02-01
description: "Naučte sa, ako vytvárať, importovať, spravovať a prispôsobovať prehrávače vo Flacbox na iPhone, iPad a Mac. Vytvárajte prehrávače z cloudových a lokálnych súborov, importujte M3U / M3U8 / CUE, preusporiadavajte skladby, upravujte obaly, archivujte do ZIP, exportujte do M3U / CSV / TXT a používajte offline režim."
keywords: [
  "Flacbox prehrávače", "import M3U prehrávača", "správca prehrávačov",
  "vytvoriť prehrávač iPhone", "audio prehrávače Flacbox",
  "vlastný obrázok prehrávača", "vymazanie skladieb z prehrávača",
  "zoradenie prehrávača Flacbox", "preusporiadanie prehrávača VoiceOver",
  "Flacbox export M3U", "Flacbox export CSV", "archív prehrávača Flacbox",
  "offline režim prehrávača Flacbox", "import CUE Flacbox", "duplicitné skladby Flacbox"
]
tags: ["príručka", "flacbox", "prehrávače"]
readingTime: 7
---


V sekcii Prehrávače nájdete užitočné nástroje na správu hudobných zbierok. Táto oblasť zobrazuje všetky prehrávače na jednom mieste. Navrchu je tlačidlo **„..."** v navigačnej lište, ktoré otvára ponuku s rôznymi možnosťami prehrávača, plus lišta nástrojov s rýchlymi akciami ako Hľadať, Prehrať všetko a Zamiešať všetko. Každý prehrávač má tiež vlastné tlačidlo **„..."** vedľa názvu, ktoré ponúka ďalšie možnosti práve pre daný prehrávač.

Prehrávače vo Flacbox môžu obsahovať zmesou online cloudových skladieb, stiahnutých offline súborov a lokálnych súborov zo zariadenia — všetko v jednom prehrávači — a prehrávajú sa bez problémov spolu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — hlavná obrazovka prehrávačov" image="/docs/guide/flacbox/img/playlists-main.webp" >}}
{{< /cards >}}

## Vytvorenie prehrávača

Vytvorenie nového prehrávača je jednoduché. Máte dve možnosti: klepnite na tlačidlo **+**, alebo klepnite na tlačidlo **„..."** v pravom hornom rohu navigačnej lišty a vyberte Nový prehrávač. Zadajte zmysluplný názov prehrávača a klepnite na Uložiť.

Tým sa otvorí dialóg Pridať skladby, kde si môžete ručne vybrať skladby, ktoré chcete zaradiť do nového prehrávača. Skladby sú pohodlne kategorizované podľa typu zdroja:

- **Knižnica** — skladby, ktoré sú už vo vašej hudobnej knižnici.
- **Súbory v tejto aplikácii** — zvukové súbory v priečinku Dokumenty aplikácie (stiahnuté z cloudového úložiska, importované cez Wi-Fi Drive alebo pridané cez Finder File Sharing).
- **Súbory na tomto zariadení** — zvukové súbory nachádzajúce sa inde na zariadení, nie v tejto aplikácii.
- **Pripojenia** — online súbory nachádzajúce sa v rámci pripojených cloudových úložných služieb.

Predvolene môžete každú skladbu pridať do prehrávača iba raz. Ak chcete povoliť duplicity, aktivujte túto funkciu v Nastavenia → Hudobná knižnica → Prehrávače → Duplicity v prehrávači → Povoliť.

## Import prehrávača

Vo Flacbox sme pridali import súborov M3U / M3U8 / CUE, takže nemusíte prehrávače manuálne znovu vytvárať po prechode z iného prehrávača.

Najprv prejdite do sekcie Prehrávače. Potom klepnite na tlačidlo Viac v pravom hornom rohu. Z ponuky vyberte Importovať prehrávač.

Na ďalšej obrazovke vyberte umiestnenie súboru. Podporované možnosti zahŕňajú:

- Pripojené cloudové úložisko
- Súbory v aplikácii
- Súbory na zariadení

Vyberte pripojené cloudové úložisko a otvorte priečinok obsahujúci súbor prehrávača. Podporované prípony súborov prehrávača zahŕňajú M3U, M3U8 a CUE. Vyberte súbor prehrávača a klepnutím na Hotovo potvrďte výber.

Aplikácia analyzuje súbor prehrávača, vytvorí zoznam skladieb a nájde tieto súbory v úložisku, aby zostavila finálny prehrávač, ktorý sa potom importuje do hudobnej knižnice. Dôležité: súbor M3U / CUE musí obsahovať správne cesty k mediálnym súborom a tieto súbory by mali skutočne existovať na týchto cestách v úložisku. Prečítajte si viac o importe prehrávača [tu](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox).

## Obrazovka detailu prehrávača

Keď otvoríte prehrávač, zobrazí sa obrazovka Detailu prehrávača. Nájdete tu tlačidlo **„..."** v pravom hornom rohu s možnosťami prehrávača a tri tlačidlá pod obalon: Hľadať, Pokračovať v prehrávaní, Prehrať všetko a Zamiešať všetko. Je tu tiež zaškrtávacie políčko Offline režim na prepnutie úplnej offline synchronizácie prehrávača.

- **Pokračovať v prehrávaní** — obnoví poslednú uloženú pozíciu prehrávania pre tento prehrávač.
- **Hľadať** — vyhľadávanie v aktuálnom prehrávači.
- **Prehrať všetko** — pridá všetky skladby z aktuálneho prehrávača do fronty prehrávača.
- **Zamiešať všetko** — podobne ako **Prehrať všetko**, ale zamiešal skladby pred pridaním do fronty audio prehrávača.
- **Offline režim** — stiahne všetky skladby z tohto prehrávača do lokálnych súborov. Všetky nové položky pridané do prehrávača sa tiež automaticky stiahnu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — obrazovka detailu prehrávača" image="/docs/guide/flacbox/img/playlist-details-screen.webp" >}}
{{< /cards >}}

## Ďalšie akcie pre prehrávač na hlavnej obrazovke prehrávačov

K akciám prehrávača môžete pristupovať klepnutím na tlačidlo **„..."** vedľa názvu prehrávača. Dostupné akcie:

- **Prehrať všetko** — pridá skladby prehrávača do novej fronty prehrávača.
- **Prehrať ďalej** — pridá skladby prehrávača na začiatok existujúcej fronty prehrávača.
- **Prehrať neskôr** — pridá skladby prehrávača na koniec existujúcej fronty prehrávača.
- **Upraviť obrázok** — zmeňte obal prehrávača.
- **Povoliť offline režim** — zapnite offline režim pre prehrávač. Existujúce aj nové skladby sa automaticky stiahnu. Prečítajte si viac o offline režime [tu](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).
- **Exportovať zoznam skladieb** — exportujte tento prehrávač do **M3U / M3U8 / CSV / TXT**, ako je opísané [tu](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Pridať do archívu** — archivujte tento prehrávač (vrátane súboru m3u, obalu a všetkých skladieb) do jedného ZIP, ako je opísané [tu](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to). Funkcia Premium.
- **Pridať skladby** — pridajte ďalšie skladby do aktuálneho prehrávača.
- **Premenovať** — premenujte prehrávač.
- **Vymazať prehrávač** — vymaže prehrávač z hudobnej knižnice. **Túto akciu nie je možné vrátiť späť.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — ďalšie akcie pre prehrávač na hlavnej obrazovke prehrávačov" image="/docs/guide/flacbox/img/more-actions-for-playlist-in-playlists-main-screen.webp" >}}
{{< /cards >}}

## Ďalšie akcie pre prehrávač na obrazovke detailu prehrávača

K akciám prehrávača môžete pristupovať klepnutím na tlačidlo **„..."** v pravom hornom rohu. Dostupné akcie:

- **Vybrať** — aktivuje režim výberu skladieb, užitočné na vymazanie viacerých skladieb z prehrávača alebo zmenu ich poradia.
- **Prehrať ďalej** — pridá skladby prehrávača na začiatok existujúcej fronty prehrávača.
- **Prehrať neskôr** — pridá skladby prehrávača na koniec existujúcej fronty prehrávača.
- **Pridať skladby** — pridajte nové skladby do prehrávača.
- **Preusporiadať skladby** — manuálne zmeňte poradie skladieb v prehrávači pomocou drag-and-drop.
- **Premenovať** — premenujte aktuálny prehrávač.
- **Upraviť obrázok** — zmeňte obal aktuálneho prehrávača.
- **Exportovať zoznam skladieb** — exportujte tento prehrávač do **M3U / M3U8 / CSV / TXT**. Prečítajte si viac [tu](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Pridať do archívu** — zazipujte aktuálny prehrávač vrátane všetkých skladieb a súboru m3u. Prečítajte si viac [tu](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Zoradiť** — zmeňte poradie skladieb v prehrávači. Možnosti zoradenia zahŕňajú **Názov skladby, Číslo skladby, Album, Interpret, Albumový interpret, Žáner, Skladateľ, Hodnotenie, Rok, Údery za minútu, Trvanie, Názov súboru, Dátum úpravy súboru, Dátum vytvorenia súboru** a **Manuálne**. Možnosť zoradenia **Manuálne** umožňuje manuálne preusporiadanie skladieb pomocou drag-and-drop.
- **Hľadať** — vyhľadajte konkrétnu skladbu v aktuálnom prehrávači.
- **Mriežka / Zoznam** — zmeňte prezentáciu rozloženia obrazovky.
- **Vymazať prehrávač** — vymaže prehrávač z hudobnej knižnice. Táto akcia nesmaže skladby z úložiska, ale **nie je možné ju vrátiť späť**.

## Zmena poradia skladieb v prehrávači

Ak chcete zmeniť poradie skladieb v prehrávači, klepnite na tlačidlo **„..."** v pravom hornom rohu a výberom **Vybrať** vstúpte do režimu výberu. Použite ovládací prvok preusporiadania a gestá drag-and-drop pri každej skladbe na jej presúvanie nahor alebo nadol. Klepnutím na ovládací prvok preusporiadania sa skladba presunie na začiatok zoznamu. Ak chcete ukončiť režim výberu a uplatniť zmeny, klepnite na **Hotovo**.

Pre ešte jednoduchší pracovný postup pri dlhých prehrávačoch vyberte Viac akcií → Preusporiadať skladby a vstúpte do vyhradeného režimu drag-and-drop preusporiadania.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — preusporiadanie skladieb v prehrávači" image="/docs/guide/flacbox/img/playlist-details-rearange-songs.webp" >}}
{{< /cards >}}

## Zmena obrázka obalu prehrávača

Ak chcete zmeniť obrázok obalu prehrávača, klepnite na tlačidlo **„..."** v pravom hornom rohu a vyberte **Upraviť obrázok**. Vyberte obrázok z dostupných zdrojov (Fotky, Súbory, cloudové úložisko alebo generovaný obal zo skladby v prehrávači), potom potvrďte klepnutím na **Hotovo**.

## Pridanie skladieb do prehrávača

Otvorte prehrávač a klepnite na tlačidlo **„..."** v pravom hornom rohu, potom výberom **Pridať skladby** otvorte dialóg. Vyberte skladby, ktoré chcete pridať, a potvrďte klepnutím na **Hotovo**.

## Vymazanie viacerých skladieb z prehrávača

Otvorte prehrávač, klepnite na tlačidlo **„..."** v pravom hornom rohu a výberom **Vybrať** vstúpte do režimu výberu. Vyberte skladby, ktoré chcete vymazať, a klepnite na **Vymazať z prehrávača** v dolnej časti obrazovky. Potvrďte klepnutím na **Hotovo**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — režim výberu na obrazovke detailu prehrávača" image="/docs/guide/flacbox/img/selection-mode-playlist-details-screen.webp" >}}
{{< /cards >}}

## Možnosti skladby

Každá skladba v prehrávači má zoznam akcií, dostupný klepnutím na tlačidlo **„..."**. Ak nevidíte všetky akcie, posuňte nadol. Môžete vymazať skladbu z prehrávača, stiahnuť ju, upraviť audio tagy a ďalšie.

- **Prehrať ďalej** — pridá skladbu na začiatok fronty prehrávača.
- **Prehrať neskôr** — pridá skladbu na koniec fronty prehrávača.
- **Pridať do prehrávača** — pridá skladbu do iného prehrávača.
- **Pridať k obľúbeným** — označí skladbu ako obľúbenú pre rýchly prístup.
- **Stiahnuť** — sprístupní skladbu offline. Zobrazí sa vo fronte prenosov a na karte **Lokálne súbory** v sekcii **Stiahnutá hudba** hudobnej knižnice.
- **Upraviť audio tagy** — otvorí zabudovaný editor tagov na zmenu metadát skladby.
- **Otvoriť v** — exportuje skladbu a otvorí ju v inej aplikácii.
- **Zobraziť v priečinku** — odhalí priečinok, kde sa nachádza zvukový súbor.
- **Zobraziť vo Finderi** — pre súbory importované z Mac odhalí priečinok, kde sa nachádza zvukový súbor na Mac.
- **Vymazať z prehrávača** — vymaže skladbu z prehrávača.
- **Vymazať z cloudovej služby** — vymaže skladbu z prehrávača a priradené cloudovej služby. **Túto akciu nie je možné vrátiť späť.**
- **Vymazať z hudobnej knižnice** — vymaže skladbu z hudobnej knižnice, pričom súbor v úložisku zostáva nedotknutý.

## Dostupnosť

Flacbox je plne prístupný s technológiou **VoiceOver**, pričom zabezpečuje, že každá komponenta má dobre navrhnutý štítok a popis. Keď je aktívny VoiceOver, aplikácia prekladá používateľské rozhranie do **Textového režimu**, zobrazuje iba prístupné a užitočné prvky na zlepšenie rýchlosti navigácie a pohodlia. Textový režim môžete tiež aktivovať v Nastavenia → Dostupnosť → Textový režim.

### Nastavenie pozície skladby v prehrávači pomocou VoiceOver

1. Otvorte prehrávač a klepnite na tlačidlo **Viac**.
2. Vyberte **Zmeniť poradie skladieb**. Zobrazenie sa prepne do režimu úprav.
3. Klepnite na ikonu indikátora preusporiadania pri názve skladby, aby ste na ňu zamerali pozornosť.
4. Rýchlo **dvakrát klepnite** na ikonu indikátora preusporiadania. Pri druhom klepnutí neuvoľnite prst — podržte ho, kým nezačujete zvuk signalizujúci, že bunka je pripravená na presunutie.
5. Teraz môžete presunúť bunku na nové miesto.

Ostatné komponenty fungujú podľa očakávania, pričom používajú vzory VoiceOver poskytované systémom.
