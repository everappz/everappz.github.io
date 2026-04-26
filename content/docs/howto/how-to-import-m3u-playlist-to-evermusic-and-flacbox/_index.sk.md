---
title: "Ako importovať zoznam skladieb M3U do Evermusic a Flacbox"
date: 2024-01-31
description: "Zistite, ako importovať súbory zoznamov skladieb M3U, M3U8 a CUE z cloudu, lokálneho úložiska alebo zariadenia do Evermusic a Flacbox."
keywords: ["evermusic", "flacbox", "zoznam skladieb", "m3u", "m3u8", "cue", "import", "hudobná aplikácia"]
tags: ["evermusic", "import", "zoznamy skladieb", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Zhrnutie:** Evermusic a Flacbox podporujú import súborov zoznamov skladieb M3U, M3U8 a CUE z cloudového úložiska, lokálnych súborov aplikácie alebo vášho zariadenia. Prejdite na Prehrávače > Viac > Importovať zoznam skladieb, vyberte zdroj, zvoľte súbor a aplikácia automaticky vytvorí váš zoznam skladieb.

M3U, čo znamená MP3 URL alebo Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, je formát počítačového súboru používaný pre multimediálne zoznamy skladieb. Jedným z jeho hlavných použití je vytváranie súborov zoznamov skladieb s jedným záznamom, ktoré odkazujú na streamy na internete. Tieto súbory ponúkajú pohodlný prístup k streamovanému obsahu a bežne sa používajú na sťahovanie, e-maily a počúvanie internetového rádia.

Napriek širokému použitiu neexistuje formálna špecifikácia formátu M3U; stal sa de facto štandardom. Súbor M3U je v podstate obyčajný textový súbor, ktorý určuje umiestnenia jedného alebo viacerých mediálnych súborov. V závislosti od kódovania sa ukladá s príponou "m3u" alebo "m3u8". Každý záznam v súbore určuje umiestnenie mediálneho súboru, čo môže byť absolútna lokálna cesta, lokálna cesta relatívna k umiestneniu súboru M3U alebo URL. Záznamy sú oddelené koncami riadkov, pričom niektoré zariadenia vyžadujú konce riadkov reprezentované ako CR LF.

Okrem toho môžu súbory M3U obsahovať komentáre s predponou znaku "#". V rozšírenom M3U "#" zavádza rozšírené direktívy M3U, ktoré môžu podporovať parametre ukončené dvojbodkou ":".

V našich aplikáciách Evermusic a Flacbox sme implementovali funkciu importu súborov M3U, čím sa eliminuje potreba manuálneho vytvárania zoznamov skladieb. Tento sprievodca vás prevedie importom vašich zoznamov skladieb z cloudového úložiska, lokálnych súborov alebo súborov na vašom zariadení priamo do aplikácie.

Najprv prejdite do sekcie 'Prehrávače'. Potom ťuknite na tlačidlo 'Viac' v pravom hornom rohu. Z ponuky, ktorá sa zobrazí, vyberte možnosť 'Importovať zoznam skladieb'.

![akcia importu zoznamu skladieb](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Na ďalšej obrazovke zvoľte umiestnenie súboru. Podporované možnosti zahŕňajú:

- Pripojené cloudové úložisko;
- Súbory v aplikácii;
- Súbory na vašom zariadení;

![výber umiestnenia súboru](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Vyberme pripojené cloudové úložisko a otvorte priečinok obsahujúci súbor zoznamu skladieb. Podporované prípony súborov zoznamov skladieb zahŕňajú M3U, M3U8 a CUE. Vyberte súbor zoznamu skladieb a ťuknite na 'Hotovo' na potvrdenie výberu.

![výber súboru M3U](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Aplikácia analyzuje súbor zoznamu skladieb a vytvorí zoznam skladieb. Potom nájde tieto súbory v úložisku a zostaví konečný zoznam skladieb, ktorý bude importovaný do hudobnej knižnice. Je kľúčové, aby váš súbor M3U/CUE obsahoval správne cesty k mediálnym súborom a súbory sa nachádzali na týchto cestách vo vašom úložisku.

![importovaný zoznam skladieb](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Aplikácia podporuje relatívne cesty aj absolútne URL súborov.

Napríklad:

Zoznam skladieb s relatívnymi cestami:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Zoznam skladieb s absolútnymi URL:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Ak importujete súbor zoznamu skladieb umiestnený v aplikácii (sekcia Lokálne súbory), nie sú potrebné žiadne ďalšie kroky.

Ak však chcete importovať zoznam skladieb umiestnený na vašom zariadení pomocou systémového výberu súborov, je tu dôležitá skutočnosť, ktorú treba mať na pamäti.

Kvôli bezpečnostným zásadám môže aplikácia pristupovať iba k súboru, ktorý vyberiete pomocou systémového výberu súborov. Súbor zoznamu skladieb však môže obsahovať odkazy na ďalšie mediálne súbory na vašom zariadení. Na import zoznamu skladieb z vášho zariadenia musíte vybrať priečinok obsahujúci súbor zoznamu skladieb aj všetky prepojené mediálne súbory. V tomto prípade aplikácia prehľadá vybraný priečinok, nájde súbor zoznamu skladieb, zostaví zoznam skladieb a importuje ho do hudobnej knižnice.

Okrem toho môžete importovať viacero zoznamov skladieb naraz ťuknutím na tlačidlo "Viac akcií" a výberom "Importovať zoznamy skladieb z priečinka". Aplikácia potom prehľadá obsah priečinka, nájde podporované súbory zoznamov skladieb a importuje ich do knižnice.

## Často kladené otázky

{{% details title="Aké formáty zoznamov skladieb podporujú Evermusic a Flacbox?" closed="true" %}}
Obe aplikácie podporujú formáty súborov zoznamov skladieb M3U, M3U8 a CUE. Tieto pokrývajú najbežnejšie štandardy zoznamov skladieb používané hudobnými prehrávačmi a multimediálnym softvérom.
{{% /details %}}

{{% details title="Môžem importovať zoznamy skladieb z cloudového úložiska?" closed="true" %}}
Áno. Môžete importovať súbory zoznamov skladieb z akejkoľvek pripojenej cloudovej úložnej služby vrátane Google Drive, Dropbox, OneDrive a serverov WebDAV.
{{% /details %}}

{{% details title="Prečo po importe chýbajú niektoré skladby?" closed="true" %}}
Súbor zoznamu skladieb musí obsahovať správne cesty k vašim mediálnym súborom a tieto súbory musia existovať na uvedených umiestneniach vo vašom úložisku. Skontrolujte, či cesty k súborom vo vašom súbore M3U alebo CUE zodpovedajú skutočným umiestneniam súborov.
{{% /details %}}

{{% details title="Môžem importovať viacero zoznamov skladieb naraz?" closed="true" %}}
Áno. Použite tlačidlo Viac akcií a vyberte "Importovať zoznamy skladieb z priečinka". Aplikácia prehľadá priečinok a nájde všetky podporované súbory zoznamov skladieb a importuje ich v jednom kroku.
{{% /details %}}

{{% details title="Musím vytvárať zoznamy skladieb manuálne?" closed="true" %}}
Nie. Funkcia importu eliminuje manuálne vytváranie zoznamov skladieb. Stačí nasmerovať aplikáciu na váš existujúci súbor M3U, M3U8 alebo CUE a automaticky vytvorí zoznam skladieb.
{{% /details %}}
