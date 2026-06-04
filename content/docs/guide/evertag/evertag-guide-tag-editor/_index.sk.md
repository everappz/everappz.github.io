---
title: "Editor tagov"
date: 2020-02-01
description: "Naučte sa, ako používať Editor tagov Evertag na aktualizáciu hudobných metadát, úpravu obalov albumov, hromadnú úpravu viacerých súborov a správu tagov z MusicBrainz. Ideálne pre organizáciu hudobnej knižnice na iOS a Mac."
keywords: [
  "editor tagov Evertag", "editor audio metadát", "editor hudobných tagov",
  "úprava audio tagov iPhone", "editor obalov albumov", "hromadná úprava audio tagov",
  "metadáta MusicBrainz", "aplikácia na organizáciu hudby", "návod Evertag", "editor ID3 tagov"
]
tags: ["návod", "evertag", "editor tagov"]
readingTime: 5
---


**Editor tagov** je hlavná obrazovka aplikácie Evertag, kde môžete prezerať a upravovať metadáta audio súborov. Otvorte túto obrazovku klepnutím na súbor v sekcii **Lokálne súbory** alebo z akéhokoľvek pripojeného účtu **cloudového úložiska**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Obrazovka Editora tagov Evertag" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Režimy úpravy

Evertag ponúka dva režimy úpravy:

- **Režim jedného súboru**
  - Navigácia medzi súbormi potiahnutím doľava alebo doprava v karuseli s obrázkami.

- **Hromadný režim**
  - Upravujte viacero súborov naraz a aplikujte zdieľané metadáta.
  - Na aktiváciu posuňte sa na koniec a klepnite na **Upravovať súbory súčasne**.

## Režim jedného súboru

Aplikácia štandardne otvára editor tagov v režime jedného súboru s povolením len hlavných možností úpravy. V tomto režime môžete upravovať najbežnejšie metadátové polia, ako sú:

**Názov skladby, Podtitul, Interpret albumu, Album, Interpret, Skladateľ, Performer, Žáner, Komentár, Počet taktov za minútu, Podcast, Kompilácia, Číslo disku, Číslo skladby, Celkový počet skladieb, Hodnotenie, Rok**

Pre prístup ku všetkým dostupným tagom posuňte sa na koniec obrazovky a klepnite na možnosť **Zobraziť rozšírené tagy**. Tým sa editor prepne do rozšíreného režimu, čo vám umožňuje upravovať viac ako **120 metadátových polí**, vrátane **MusicBrainz tagov**, **Textov piesní**, **Poradenských hodnotení**, hodnôt replay-gain, poradí zoradenia, metadát podcastov a ďalšie. Použite **Nastavenia → Editor audio tagov → Tlačidlá na hlavnej obrazovke** na trvalé prepnutie možnosti Zobraziť rozšírené tagy, aby bola vždy zapnutá.

{{< cards cols="1">}}
{{< card title="" subtitle="Spodný panel akcií" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Hromadný režim

Do hromadnej úpravy môžete vstúpiť dvoma spôsobmi:

1. **Zo správcu súborov**
   - Klepnite na **Viac akcií** (•••) v pravom hornom rohu.
   - Klepnite na **Vybrať**, vyberte viacero súborov a potom klepnite na **Upraviť audio tagy**.

2. **Z Editora tagov**
   - Otvorte ľubovoľný súbor, posuňte sa na koniec a klepnite na **Upravovať súbory súčasne** na načítanie všetkých súborov z rovnakého priečinka.

{{< cards cols="1">}}
{{< card title="" subtitle="Režim hromadnej úpravy" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Po úprave klepnite na **Uložiť** na použitie zmien.

## Úprava textov piesní

Rozšírený editor zobrazuje pole **Texty piesní**. Klepnutím naň otvoríte zoznam textov piesní — každý záznam textov má vlastný jazyk a popis, takže jeden track môže ukladať niekoľko prekladov.

Texty piesní nemusíte písať od začiatku. Editor obsahuje skratky pre rýchle vyhľadávanie do najpopulárnejších databáz textov piesní na webe, vopred vyplnené aktuálnym interpretom a názvom skladby:

- **Lrclib** — vhodná verejná databáza pre **časovo synchronizované (LRC-štýl) texty piesní**. Použite ju, keď chcete synchronizované texty, ktoré sa riadkujú v prehrávačoch, ktoré ich podporujú.
- **Genius** — rozsiahly katalóg s anotáciami a presnými textami piesní v prostom texte.
- **Lyricsify** — komunitná databáza s prostými a časovo synchronizovanými textami piesní.
- **Google** — všeobecné webové vyhľadávanie ako záloha, keď špecializované databázy nemajú zhodu.

Každá skratka sa zobrazí len vtedy, keď je príslušná služba dostupná z vášho zariadenia. Klepnite na službu, skopírujte texty piesní (alebo LRC časové značky), ktoré chcete, vráťte sa do Evertag a vložte ich do textového poľa — potom **Uložte** na zápis textov piesní späť do tagov audio súboru.

{{< cards cols="1">}}
  {{< card title="" subtitle="Stránky textov piesní" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Vyberte jazyk z výberového poľa:

{{< cards cols="1">}}
  {{< card title="" subtitle="Výber jazyka textov piesní" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Potom vložte alebo napíšte text piesne. Evertag podporuje prostý text aj časovo synchronizované texty piesní — zástupný text zobrazuje príklad formátu LRC-štýl, čo je presne to, čo Lrclib a Lyricsify vracia pre synchronizované výsledky.

{{< cards cols="1">}}
  {{< card title="" subtitle="Editor textu piesní" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Nastavenie hodnotenia a poradenského hodnotenia

Rozšírený editor ponúka hviezdicový ovládací prvok **Hodnotenie** spolu so segmentovým ovládacím prvkom **Poradenské hodnotenie**.

### Hviezdicové hodnotenie

Použite pole **Hodnotenie** na pridelenie osobného skóre od jednej do piatich hviezd. Hodnota sa zapíše do štandardného tagu hodnotenia súboru (POPM pre ID3, `rate` pre MP4, `RATING` pre Vorbis/APE atď.), takže iné aplikácie, ktoré čítajú tento tag — vrátane aplikácie Hudba, Plex, Roon a väčšiny desktopových editorov tagov — okamžite zobrazia vaše hodnotenia.

{{< cards cols="1">}}
  {{< card title="" subtitle="Hodnotenie" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Poradenské hodnotenie

**Poradenské hodnotenie** označuje obsah skladby pomocou jednej z hodnôt z Parental Advisory štandardu, ktorý iTunes Store a väčšina hudobných platforiem používa:

- **Neofenzívne** — predvolené pre skladby bez informácií o rodičovskom poradenstve. Súbor sa považuje za vhodný pre všetkých poslucháčov a v prehrávačoch, ktoré rešpektujú tag, nezobrazí žiadny poradenský štítok.
- **Explicitné** — skladba obsahuje explicitný jazyk alebo obsah. Prehrávače, ktoré rešpektujú rodičovské kontroly (aplikácia Hudba, aplikácia Apple TV, exporty Spotify, Plex atď.) zobrazí vedľa názvu odznak **E** a keď sú na zariadení alebo účte povolené obmedzenia, môžu skryť skladbu z detských profilov alebo odmietnuť jej prehrávanie.
- **Čisté** — cenzurovaná alebo upravená verzia inak explicitnej skladby. Prehrávače zobrazujú odznak **C**, aby poslucháči mohli rozlíšiť čistú verziu od pôvodnej explicitnej verzie, čo je užitočné, keď obe verzie žijú v rovnakej knižnici.

Toto pole budete chcieť nastaviť alebo opraviť, keď:

- Súbor má nesprávny štítok (napríklad čistá rádiová verzia, ktorá bola nesprávne označená ako Explicitná, alebo naopak).
- Skladby boli rippované alebo stiahnuté bez tagu a teraz sa zobrazujú ako Neofenzívne aj napriek tomu, že obsahujú explicitný obsah — potrebné, aby rodičovské kontroly a rodinne zdieľané knižnice fungovali správne.
- Pripravujete album na odovzdanie alebo zdieľanie a potrebujete, aby každá skladba niesla konzistentné metadáta.
- Chcete, aby CarPlay, Zamykacia obrazovka, prehrávače v štýle Apple Music alebo DJ softvér zobrazoval správny odznak **E** / **C** vedľa názvu skladby.

Hodnota je uložená v štandardnom poli poradenského hodnotenia pre formát súboru (`rtng` pre MP4, `TXXX:ITUNESADVISORY` pre ID3, `ITUNESADVISORY` pre Vorbis), takže každý prehrávač, ktorý číta metadáta rodičovského poradenstva, uvidí vaše aktualizácie.

{{< cards cols="1">}}
  {{< card title="" subtitle="Poradenské hodnotenie textov piesní" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Úprava obalu albumu

Na zmenu obalu albumu:

1. Klepnite na ikonu **Fotoaparátu** v karuseli s obrázkami.
2. Vyberte umiestnenie obrázka: Lokálne súbory, Cloud, Stiahnuté alebo Knižnica fotiek.
3. Vyberte obrázok na použitie ako obal.

{{< cards cols="1">}}
  {{< card title="" subtitle="Vybrať obrázok" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Ďalšie akcie v Editore tagov

Extra možnosti úpravy sú dostupné cez panel nástrojov pod zobrazením obrázkov.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ponuka Viac akcií" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Automatické vyhľadávanie audio tagov

Táto akcia aktivuje inteligentný vyhľadávač tagov, ktorý na základe existujúcich informácií nájde a vyplní kompletné metadáta pre váš audio súbor.  
Aplikácia používa databázu MusicBrainz — jednu z najkomplexnejších databáz tagov — s viac ako **50 miliónmi** skladieb.

### Vyhľadávanie obalu albumu

Pomocou metadát vyhľadajte na webe správny obal albumu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Vyhľadávanie obalu albumu" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Po nájdení uložte obrázok do **Fotiek** pomocou systémovej kontextovej ponuky.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pridať obrázok do Fotiek" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Potom sa vráťte do editora tagov, klepnite na ikonu Fotoaparátu, prejdite do **Knižnice fotiek** a vyberte uložený obrázok. Aplikácia ho nastaví ako obal vášho audio súboru.

Môžete upraviť, ako sa obrázky obalov škálujú v nastaveniach aplikácie.

### Uloženie obalu albumu

Táto akcia uloží aktuálny obal albumu do priečinka **Dokumenty**, aby ste ho mohli neskôr znova použiť.

### Normalizácia kódovania

Táto akcia normalizuje kódovanie textu všetkých tagov v metadátach audio súboru. Je obzvlášť užitočná, ak prechádzate z PC so systémom Windows, kde súbory môžu používať rôzne kódovania, ktoré sa na Mac zobrazujú ako nečitateľné alebo poškodené znaky.

### Manuálne vyhľadávanie tagov

Manuálne vyhľadávajte metadáta albumov pomocou databázy MusicBrainz.

- Vyberte album

{{< cards cols="1">}}
  {{< card title="" subtitle="Vybrať album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Vyberte správnu pieseň

{{< cards cols="1">}}
  {{< card title="" subtitle="Vybrať pieseň" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Vyberte, ktoré tagy sa majú použiť

{{< cards cols="1">}}
  {{< card title="" subtitle="Vybrať audio tagy" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Klepnite na **Hotovo** na použitie vybraných metadát na vašu skladbu.

### Vymazanie audio tagov

Vymažte všetky metadátové polia pre súbor. Užitočné, keď začínate odznova. Klepnite na **Uložiť** na potvrdenie.

## Nastavenia Editora tagov

Prejdite do **Nastavenia → Editor audio tagov** na prispôsobenie správania.

### Škálovanie obalu albumu

Vyberte, ako sa majú obaly albumov škálovať pri ukladaní do audio súborov. Môžete zakázať škálovanie na zachovanie pôvodnej veľkosti obrázka, ale uvedomte si, že niektoré prehrávače nemusia podporovať veľké súbory s obrázkami. Možnosť "pôvodná veľkosť" je súčasťou prémiových funkcií personalizácie.

### Možnosti ukladania tagov

- **ID3v2.4** — Keď je povolené, aplikácia ukladá tagy vo formáte ID3v2.4 pokiaľ je to možné. Zakážte, ak vaše audio tagy nie sú správne zobrazené na starších prehrávačoch alebo zariadeniach, čím prejdete na širšie podporovaný ID3v2.3.
- **Duplicitné tagy** — Keď je povolené, bežné metadátové polia sú duplikované do oboch sekcií tagov súboru. Toto zlepšuje kompatibilitu so staršími audio prehrávačmi, ale vo väčšine prípadov nie je potrebné.

### Možnosti aktualizácie metadát cloudových súborov

Môžete kontrolovať, ako aplikácia aktualizuje metadáta pre audio súbory uložené v cloudových službách:

- **Zobraziť potvrdzovaciu správu**  
  Pýtajte sa pred použitím zmien metadát na cloudové súbory.

- **Automaticky aktualizovať metadáta súboru**  
  Uložte zmeny metadát do cloudového súboru automaticky po úprave.

- **Neaktualizovať metadáta súboru**  
  Preskočte aktualizáciu cloudových súborov — zmeny sa uplatnia iba lokálne.

### Upravovať online súbory

Vyberte, čo sa stane s lokálne stiahnutými kópiami cloudových súborov po úprave:

- **Vždy vymazať stiahnutý súbor**  
  Odstráňte lokálnu kópiu po uložení zmien.

- **Nevymazávať stiahnutý súbor**  
  Ponechajte stiahnutý súbor na zariadení po úprave.

### Tlačidlá na hlavnej obrazovke

Prispôsobte, ktoré akcie sa zobrazujú na hlavnej obrazovke editora tagov (Automaticky hľadať audio tagy, Manuálne hľadať audio tagy, Hľadať obálku albumu, Uložiť obálku albumu, Normalizovať kódovanie, Vymazať audio tagy). Môžete tiež prepnúť **Zobraziť rozšírené tagy** a **Upravovať súbory súčasne**, aby sa editor vždy otváralo v preferovanom režime.
