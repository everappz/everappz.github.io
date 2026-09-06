---
title: "Sdílení"
date: 2026-08-20
description: "Zjistěte, jak funguje sdílení v Everdisku: klepnutím na Spustit proměníte svůj iPhone nebo iPad v bezdrátový disk, vyberete, co chcete sdílet (soubory, složky, fotky a hudbu), spustíte čtyři servery (DLNA, HTTP, WebDAV, FTP), přečtete si adresy pro připojení, uvidíte, kdo je připojen, a udržíte sdílení běžící přes Wi-Fi nebo kabel USB."
keywords: ["sdílení Everdisk", "bezdrátový disk iPhone", "spuštění sdílení", "sdílení souborů iPhone", "sdílení fotek po síti", "DLNA HTTP WebDAV FTP", "co sdílet", "jak se připojit", "nechat aplikaci otevřenou", "sdílení přes Wi-Fi nebo kabel USB"]
tags: ["everdisk", "guide", "sharing"]
readingTime: 9
---


Karta **Sdílení** je srdcem Everdisku. Právě tady proměníte svůj iPhone nebo iPad v bezdrátový disk, vyberete přesně to, co chcete sdílet, a získáte adresy, které ostatní zařízení použijí k připojení. Je to první karta, kterou uvidíte po otevření aplikace.

## Spuštění a zastavení sdílení

Uprostřed obrazovky Sdílení je velké kulaté tlačítko.

- Klepnutím na **Spustit** uvedete všechny povolené servery najednou do provozu. Tlačítko ukáže **Spouštění...** a jakmile sdílení běží, změní se na **Zastavit**.
- Klepnutím na **Zastavit** vše zase vypnete. Připojená zařízení se odpojí.

Dokud sdílení běží, jsou vámi vybrané soubory, fotky a hudba dostupné každému zařízení ve stejné síti, které se připojí jedním ze čtyř způsobů uvedených níže.

> Sdílení běží pouze tehdy, když je aplikace otevřená. Podívejte se na **Nechte aplikaci otevřenou** ke konci této stránky, kde se dozvíte proč a jak udržet velké přenosy v chodu.

## Vyberte, co chcete sdílet

Než začnete, klepněte na záhlaví **Co sdílet** a otevřete tři skupiny. Sdílet můžete libovolnou jejich kombinaci a před spuštěním sdílení musíte vybrat alespoň jednu věc.

**Soubory a složky**

- Vlastní složka **Dokumenty** aplikace se sdílí ve výchozím nastavení. Pokud chcete, můžete její sdílení vypnout.
- Klepnutím na **Přidat složku** nasdílíte složku odkudkoli ze svého zařízení, nebo klepnutím na **Přidat soubor** nasdílíte jednotlivé soubory.
- Každá sdílená položka má tlačítko **Info** a tlačítko **Zastavit sdílení**.

**Fotky a videa**

- Zapněte **Povolit přístup k celé knihovně Fotek** pro sdílení celé své knihovny fotek a videí, nebo
- klepněte na **Přidat fotky** a ručně vyberte jen ty fotky a videa, které chcete sdílet.

**Hudba**

- Zapněte **Povolit přístup k celé hudební knihovně** pro sdílení celé své hudební knihovny, nebo
- klepněte na **Přidat skladby** a nasdílejte jen vybrané písně.
- Skladby, které jsou chráněné (DRM) nebo uložené pouze v cloudu, sdílet nelze.

Pokud se pokusíte spustit sdílení bez jakéhokoli výběru, Everdisk zobrazí poznámku **Není co sdílet**. Pokud změníte, co se sdílí, zatímco sdílení běží, **zastavte a spusťte je znovu**, aby se změna projevila.

## Čtyři servery

Everdisk sdílí stejný obsah čtyřmi způsoby najednou. Každý z nich je určen pro jiný druh zařízení a každý lze zapnout nebo vypnout v **Nastavení → Sdílení → Připojení**. Ve výchozím nastavení jsou zapnuté všechny čtyři.

- **TV a mediální centrum (DLNA)** - pro chytré televize a mediální přehrávače. Vaše zařízení si samy najdou a zobrazí vaše fotky, videa a hudbu s náhledovými miniaturami.
- **Prohlížeč (HTTP)** - pro jakýkoli telefon, tablet nebo počítač. Druhá osoba otevře odkaz ve webovém prohlížeči a vaše soubory prochází i stahuje. Nic se neinstaluje.
- **Počítač (WebDAV)** - pro Mac, PC s Windows nebo počítač s Linuxem. Vaše zařízení se zobrazí jako běžný síťový disk, takže můžete soubory přetahovat oběma směry.
- **Ostatní aplikace a zařízení (FTP)** - pro souborové aplikace a pokročilé uživatele, kteří umí FTP.

Podrobné pokyny k připojení jednotlivých typů krok za krokem najdete v [Připojte svá zařízení](/docs/guide/everdisk/everdisk-guide-connect).

## Jak se připojit a adresy pro připojení

Když klepnete na Spustit, sekce **Jak se připojit** zobrazí pro každý aktivní server kartu s přesnou **adresou**, kterou zadáte na druhém zařízení. Každou adresu snadno zkopírujete - klepnutím ji zkopírujete, tlačítkem **Sdílet** ji odešlete, nebo klepnutím na tlačítko **info (ⓘ)** zobrazíte podrobné pokyny pro každý protokol.

- Karta DLNA zobrazuje adresu s popisem zařízení, která končí na `/device-desc.xml` pro přehrávače, jež ji vyžadují.
- Když je vaše zařízení připojeno k Macu kabelem, objeví se další adresa s odznakem **Kabelové připojení**, která používá název vašeho zařízení `.local`.

Adresu můžete otevřít i jako **QR kód**, aby fotoaparát jiného zařízení mohl skočit rovnou na ni.

## Kdo je připojen

Sekce **Kdo je připojen** zobrazuje v reálném čase zařízení, která jsou k vám právě připojena. Klepnutím na tlačítko dalších akcí u libovolného zařízení jej můžete pomocí **Blokovat toto zařízení** zablokovat, pokud jej nepoznáváte. Blokovaná zařízení se spravují v [Přístup a soukromí](/docs/guide/everdisk/everdisk-guide-access).

## Název a avatar vašeho zařízení

Každé zařízení má přátelský název (třeba "Speedy-Hare") a barevný avatar. Pod tímto názvem vaše zařízení zobrazí televize, počítač nebo jiná aplikace v síti, takže je snadno rozeznatelné. Název a avatar můžete zdarma vygenerovat znovu, nebo si s Premium nastavit vlastní název, ikonu či fotoavatar. Viz [Nastavení](/docs/guide/everdisk/everdisk-guide-settings).

## Sdílení přes Wi-Fi nebo kabel USB

Sdílení může běžet ve dvou situacích:

- **Přes Wi-Fi** - vaše zařízení a ostatní zařízení jsou ve stejné síti Wi-Fi.
- **Přes kabel USB** - vaše zařízení je připojeno kabelem k **Macu**, a to i tehdy, když žádná Wi-Fi vůbec není. Je to rychlejší než Wi-Fi a funguje to i v letadle, v hotelu nebo v uzamčené síti.

Pokud není k dispozici Wi-Fi ani kabel, je tlačítko **Spustit** zakázané a objeví se poznámka **Žádné připojení Wi-Fi**. Pokud se připojení během sdílení přeruší, Everdisk sdílení automaticky zastaví a dá vám vědět. Klepnutím na tlačítko info u kterékoli z těchto poznámek získáte úplné vysvětlení.

## Nechte aplikaci otevřenou

Protože váš iPhone nebo iPad funguje jako server, **sdílení funguje pouze tehdy, když je Everdisk otevřený na obrazovce**. Pokud aplikaci zavřete nebo zařízení na delší dobu uzamknete, systém může aplikaci pozastavit a sdílení se zastaví.

Pro velké přenosy:

- Nechte Everdisk otevřený a v popředí.
- Připojte zařízení k napájení.
- Nastavte **Automatické uzamčení** na **Nikdy** v aplikaci Nastavení iOS po dobu přenosu.

Můžete zapnout **Upozornit před odpojením** (v Nastavení → Sdílení), aby vám Everdisk připomněl, ať aplikaci znovu otevřete dřív, než ji systém uspí. Klepnutím na tlačítko info na banneru **Nechte aplikaci otevřenou** získáte více podrobností.

## Další kroky

- [Připojte svá zařízení](/docs/guide/everdisk/everdisk-guide-connect) - připojte televizi, počítač, prohlížeč, telefon nebo kabel USB.
- [Přístup a soukromí](/docs/guide/everdisk/everdisk-guide-access) - přidejte heslo a ovládejte úpravy.
- [Nastavení](/docs/guide/everdisk/everdisk-guide-settings) - zapínejte a vypínejte servery a laďte kvalitu.
