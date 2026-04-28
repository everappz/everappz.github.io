---
title: "Exportujte kompletnú históriu počúvania z Evermusic a Flacbox do Last.fm"
date: 2024-01-30
description: "Naučte sa, ako exportovať hudobnú históriu z Evermusic a Flacbox a nahrať ju na Last.fm pomocou súborov CSV a nástroja Last.fm Scrubbler pre Windows."
keywords: ["evermusic", "flacbox", "lastfm", "hudobná história", "scrobbling", "export skladieb", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "nedávne", "lastfm", "export", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Zhrnutie:** Exportujte históriu počúvania z Evermusic alebo Flacbox ako súbor CSV a potom ho nahrajte na Last.fm pomocou bezplatného nástroja Last.fm-Scrubbler-WPF na Windows. Automatické scrobblovanie je tiež natívne dostupné v oboch aplikáciách.

**Aktualizácia:** Automatické scrobblovanie je teraz dostupné! Viac sa dozviete tu: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobblovanie je jednoduchý spôsob, ako automaticky uložiť základné údaje, ako je názov a interpret práve prehrávanej skladby, do online služby. Neskôr si môžete prezrieť svoju históriu počúvania.

[Last.fm](https://www.last.fm/home), poháňaný systémom odporúčania hudby s názvom Audioscrobbler, ponúka túto službu zadarmo. Vytvára podrobný profil vášho hudobného vkusu zaznamenávaním skladieb, ktoré počúvate, či už z internetových rádiostaníc, vášho počítača alebo rôznych prenosných hudobných zariadení. Webovú stránku môžete neskôr navštíviť a získať odporúčania nových interpretov alebo albumov, ktoré zodpovedajú vášmu hudobnému vkusu.

Históriu počúvania môžete nahrať na [Last.fm](http://Last.fm) z aplikácií Evermusic a Flacbox pomocou bezplatného nástroja a my vám ukážeme, ako na to.

Otvorte sekciu 'Hudobná knižnica' v aplikácii a prejdite na sekciu 'Rýchly prístup'. Ťuknite na položku menu 'Nedávne'.

![obrazovka hudobnej knižnice](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

Na obrazovke 'Nedávne' ťuknite na tlačidlo 'Viac' v pravom hornom rohu na aktiváciu ponuky 'Viac akcií'. Ťuknite na položku menu 'Exportovať zoznam skladieb'.

![obrazovka nedávnych](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

Na obrazovke 'Vyberte formát súboru' máte možnosť vybrať formát cieľového súboru. Dostupné možnosti - CSV, TXT, M3U.

![obrazovka výberu formátu súboru](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Toto znamená Comma-Separated Values, ideálne na organizovanie vašich údajov do prehľadného tabuľkového formátu. V cieľovom súbore nájdete parametre ako Meno interpreta, Názov albumu, Názov skladby, Časová pečiatka (čas, kedy ste počúvali skladby), Meno interpreta albumu a Trvanie skladby.

TXT: Tu hovoríme o jednoduchom textovom súbore. Je jednoduchý a priamočiary, s parametrami vrátane Mena interpreta, Názvu albumu, Názvu skladby a Trvania.

M3U: Tento formát je v podstate hlavnou voľbou na vytváranie zoznamov skladieb. Je skvelý, pretože môžete exportovať svoj zoznam skladieb a vychutnať si ich na akomkoľvek zariadení, aj keď nemáte originálne súbory (za predpokladu, že vyberiete možnosť absolútnej URL pre mediálne súbory). Vo výstupnom súbore nájdete parametre ako Trvanie, Meno interpreta, Názov skladby a Umiestnenie mediálneho súboru.

Pre našu úlohu je výber CSV tou správnou cestou. Budeme používať tento súbor s bezplatným softvérom Last.fm-Scrubbler-WPF na nahranie našej histórie počúvania do služby [Last.fm](http://Last.fm). Jednoducho vyberte CSV a stlačte tlačidlo 'Exportovať'.

![obrazovka dokončeného exportu](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Po dokončení exportu jednoducho ťuknite na tlačidlo 'Zobraziť súbor' a aplikácia zobrazí vytvorený súbor vo vašom priečinku dokumentov. Potom ťuknite na tlačidlo 'Viac akcií' vedľa názvu súboru a z ponuky vyberte možnosť 'Otvoriť v'. Naším ďalším krokom je skopírovať exportovaný súbor do vášho stolného počítača. Môžete to jednoducho urobiť výberom možnosti AirDrop z ponuky 'Otvoriť v'.

![viac akcií pre exportovaný súbor](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Ďalej budeme používať bezplatného klienta s otvoreným zdrojovým kódom [Last.FM](http://Last.FM), ktorý je dostupný iba na platforme Windows. Tento klient vám umožňuje efektívne aktualizovať históriu počúvania na [Last.FM](http://Last.FM) pomocou súboru CSV, ktorý sme práve exportovali.

Ak momentálne nepoužívate počítač s Windows, nebojte sa. Tento klient môžete stále používať inštaláciou VirtualBox na váš Mac a použitím oficiálneho obrazu vývojového prostredia Windows.

Tu je to, čo musíte urobiť:

- Nainštalujte VirtualBox z nasledujúceho odkazu: [Stiahnuť VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Stiahnite a nainštalujte vývojové prostredie Windows z tohto odkazu: [Vývojové prostredie Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Na vašom počítači s Windows (alebo v aplikácii VirtualBox s obrazom Windows Development) stiahnite a nainštalujte [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - bezplatný softvér s otvoreným zdrojovým kódom dostupný na GitHub. Testovali sme na verzii 1.28, ktorú si môžete stiahnuť tu: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Stránka na stiahnutie Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

V sekcii 'Assets' kliknite na [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) na stiahnutie inštalačného archívu. Rozbaľte stiahnutý súbor a otvorte rozbalený priečinok.

- DÔLEŽITÉ

Táto aplikácia je stále v beta verzii. Tvorcovia aplikácie nemali veľa testovania. Odporúčajú najprv skúsiť scrobblovať na testovací účet a zistiť, či sa veci, ktoré chcete scrobblovať, robía správne. Najmä ak scrobblujete veľa skladieb naraz. Buďte prosím opatrní so svojimi účtami.

Spustite Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Na hlavnej obrazovke aplikácie jednoducho kliknite na 'Neprihlásený' v ľavom dolnom rohu na aktiváciu obrazovky 'Pridať účet'.

![Obrazovka pridania účtu](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Zadajte svoje prihlasovacie údaje.

![obrazovka zadania prihlasovacích údajov](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Kliknite na tlačidlo 'Login' na pridanie vášho účtu.

![Kliknite na tlačidlo Login na pridanie vášho účtu.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Otvorte kartu 'File Parse Scrobbler' na začatie importu súboru CSV z aplikácie Evermusic.

![Otvorte kartu File Parse Scrobbler na začatie importu súboru CSV z aplikácie Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Vyberte 'Parser: CSV' a kliknite na tlačidlo 'Settings'.

Na ďalšej obrazovke môžete vybrať poradie parametrov vo vašom súbore CSV.

Jednotlivé polia môžu byť ohraničené úvodzovkami a MUSIA byť ohraničené úvodzovkami, ak pole obsahuje akýkoľvek z nastavených oddeľovačov. Napríklad:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Takže nechajte všetky nastavenia predvolené; jediné, čo musíte zmeniť, je zaškrtnúť políčko v poli 'Has Fields Enclosed In Quotes'.

Kliknite na 'Save & Close' na uplatnenie zmien.

![vyberte poradie parametrov vo vašom súbore CSV.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Scrobblovanie parsovaním súboru má dva režimy. Môžu byť zmenené pomocou ComboBoxu 'Scrobbling Mode'.

Normálny režim: V tomto režime budú skladby scrobblované s časovou pečiatkou z parsovaného scrobblu. Iba scrobble novšie ako 14 dní môžu byť scrobblované.

Importný režim: V tomto režime budú skladby scrobblované s časovou pečiatkou vypočítanou z 'Finish Time' a vybraného trvania medzi každou skladbou. To umožňuje scrobblovanie skladieb, aj keď je časová pečiatka parsovaného scrobblu staršia ako 14 dní. Preto bude prvá (najvrchnejšia) skladba v súbore CSV scrobblovaná s 'Finish Time'.

Vyberte predtým vygenerovaný súbor CSV z aplikácie Evermusic v poli 'File:' a kliknite na 'Parse'. V niektorých prípadoch sa môže zobraziť chybové hlásenie, že niektoré scrobble sa nepodarilo parsovať. Je to v poriadku, ak máte niektoré skladby bez úplných metadát, ako je Meno interpreta.

![niektoré scrobble sa nepodarilo parsovať](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Kliknite na tlačidlo 'Check All' na výber všetkých parsovaných skladieb.

![Kliknite na tlačidlo Check All na výber všetkých parsovaných skladieb.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Kliknite na tlačidlo 'Preview' na kontrolu všetkých zmien, ktoré budú odoslané na server.

![Kliknite na tlačidlo Preview na kontrolu všetkých zmien, ktoré budú odoslané na server.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Kliknite na tlačidlo 'Scrobble' na nahranie všetkých zmien na server.

![Kliknite na tlačidlo Scrobble na nahranie všetkých zmien na server.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Predtým Last.fm-Scrubbler-WPF nemal denný limit scrobblov. Toto sa teraz zmenilo, pretože niektorí ľudia používali Scrubbler na scrobblovanie toľkých skladieb, že to spôsobovalo problémy pre stránku Last.fm. Limit scrobblov je v súčasnosti 2800 scrobblov za deň. Keď sa pokúsite scrobblovať viac, dostanete chybovú správu. Plánuje sa pridanie 'fronty scrobblov', takže ak potrebujete scrobblovať viac ako 2800 skladieb, budú pridané do fronty a automaticky scrobblované po určitom čase. Koľko scrobblov vám zostáva, si môžete skontrolovať v zobrazení výberu používateľa.

Keď sú všetky záznamy úspešne nahrané na server, uvidíte správu v spodnej časti okna aplikácie potvrdzujúcu: 'Successfully scrobbled selected tracks.'

![Successfully scrobbled selected tracks.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Teraz môžete otvoriť svoj profil na stránke [Last.fm](http://Last.fm) a skontrolovať všetky zmeny.

![váš profil na stránke Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Často kladené otázky

{{% details title="Môžem scrobblovať automaticky bez exportovania súborov CSV?" closed="true" %}}
Áno. Evermusic aj Flacbox teraz podporujú automatické scrobblovanie na Last.fm. Pozrite si návod: [Ako scrobblovať na Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Čo ak môj CSV má skladby staršie ako 14 dní?" closed="true" %}}
Použite Importný režim v Last.fm-Scrubbler-WPF. Prepočíta časové pečiatky z Finish Time, čo vám umožní scrobblovať skladby bez ohľadu na ich pôvodný dátum.
{{% /details %}}

{{% details title="Nemám počítač s Windows. Môžem stále používať Last.fm-Scrubbler?" closed="true" %}}
Áno. Nainštalujte VirtualBox na váš Mac a stiahnite bezplatný obraz Vývojového prostredia Windows od Microsoft. Spustite Last.fm-Scrubbler-WPF vo virtuálnom stroji.
{{% /details %}}

{{% details title="Prečo niektoré scrobble neboli parsované?" closed="true" %}}
Skladby, ktorým chýbajú základné metadáta (ako meno interpreta), nemôžu byť parsované. Je to očakávané a neovplyvní to ostatné skladby v súbore.
{{% /details %}}

{{% details title="Existuje denný limit scrobblov?" closed="true" %}}
Áno. Last.fm-Scrubbler-WPF umožňuje až 2 800 scrobblov za deň. Ak potrebujete scrobblovať viac, rozdeľte proces na viac dní.
{{% /details %}}
