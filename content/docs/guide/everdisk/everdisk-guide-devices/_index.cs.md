---
title: "Připojení k serverům"
date: 2026-08-20
description: "Pomocí karty Zařízení v Everdisku se připojíte k dalším serverům ve vaší síti. Přidávejte a procházejte servery DLNA, WebDAV, FTP, SFTP a SMB a disky NAS, streamujte zvuk i video, stahujte soubory a na serverech, které to umožňují, vytvářejte, nahrávejte, přejmenovávejte, přesouvejte i mažte."
keywords: ["karta Zařízení Everdisk", "připojení k NAS", "klient DLNA iPhone", "klient WebDAV iPhone", "klient FTP iPhone", "klient SFTP iPhone", "SMB klient iPhone", "připojení ke sdílené složce SMB", "procházení síťového serveru", "streamování z NAS", "stahování ze serveru", "připojení cloud WebDAV"]
tags: ["everdisk", "guide", "devices", "connections"]
readingTime: 9
---


Everdisk není jen bezdrátový disk - je také klientem pro ostatní zařízení ve vaší síti. Karta **Zařízení** vám umožní připojit se k serverům **DLNA**, **WebDAV**, **FTP**, **SFTP** a **SMB** včetně Maců, PC s Windows, počítačů s Linuxem, disků NAS a mediálních serverů a poté procházet, streamovat a stahovat jejich soubory.

## Obrazovka Zařízení

Karta Zařízení má dvě části:

- **Připojení** - servery, které jste si už uložili.
- **Dostupná zařízení** - servery, které Everdisk automaticky najde ve vaší místní síti.

Pro připojení k něčemu, co Everdisk už našel, stačí na to klepnout v **Dostupná zařízení**. Pro ruční přidání serveru klepněte na tlačítko **plus (+)** nebo na **Nové připojení**.

## Přidání nového připojení

Klepněte na **Nové připojení** a zvolte typ serveru, ke kterému se chcete dostat:

- **DLNA / UPnP** - nejlepší pro mediální servery. Streamujte video, hudbu a fotky z mediálních knihoven, síťových úložných disků a televizí i počítačů s podporou DLNA. DLNA je pouze ke čtení: můžete procházet, streamovat a stahovat, ale nemůžete nahrávat ani měnit soubory.
- **WebDAV** - připojte se k souborovým serverům, síťovým úložným diskům a cloudovým diskům, které podporují WebDAV. Čtení i zápis, pokud to server umožňuje.
- **FTP** - běžné na routerech, síťových úložných discích a webhostingu. Výchozí port je 21 (990 pro zabezpečené FTPS); v adrese můžete nastavit vlastní port, například `ftp://host:2121`. Pro anonymní přístup nechte přihlašovací jméno a heslo prázdné.
- **SFTP** - připojte se bezpečně přes SSH. Výchozí port je 22; v případě potřeby použijte v adrese vlastní port, například `sftp://host:2222`.
- **SMB** - připojte se k Macům, PC s Windows, serverům Linux a síťovým úložištím (NAS), která sdílejí složky přes **SMB / CIFS**. Zadejte adresu jako `smb://server-address/share-name/` (příklady: `smb://local-server-name/share-name/folder-path`, `smb://192.168.1.105/share-name/folder-path`, `smb://remote-server.com`). SMB přidává dvě volitelná pole: název **Pracovní skupiny** a **Verzi protokolu**, kterou můžete nechat na **Automatické** nebo vynutit na **SMB1** či **SMB2**. Pokud se soubory nebo složky se speciálními znaky nedaří otevřít, zkuste přepnout verzi na **SMB1**.

> Everdisk se připojuje pouze k těmto protokolům v místní síti a k přímo adresovaným protokolům. Nepřihlašuje se k cloudovým účtům jako Google Drive nebo Dropbox. Cloudový disk je dosažitelný pouze tehdy, když daná služba nabízí adresu **WebDAV**, kterou můžete zadat.

## Zadání adresy a přihlášení

V editoru připojení vyplňte:

- **Název** - přátelský název pro připojení.
- **URL / adresa** - adresa serveru (příklady jsou zobrazeny pro každý typ).
- **Přihlašovací jméno** a **Heslo** - obojí nechte prázdné, pokud server umožňuje anonymní přístup.

U WebDAV můžete povolit neplatné certifikáty, pokud váš server používá certifikát podepsaný sám sebou. Pokud nelze ověřit identitu zabezpečeného serveru, Everdisk vás před navázáním důvěry požádá o potvrzení.

Uživatelé zdarma mohou uložit až **10** připojení. Premium tento limit odstraní.

## Procházení, streamování a stahování

Po připojení klepněte na server a otevřete jej:

- **Procházejte** složky v seznamu nebo mřížce, řaďte je a prohlížejte si miniatury. Servery DLNA navíc zobrazují podrobnosti o hudbě a obaly.
- **Streamujte** zvuk a video. Zvuk jde do fronty mini přehrávače; video se přehrává na celou obrazovku. Během streamování souboru funguje převíjení.
- **Stahujte** soubory do svého zařízení. Vyberte jich několik naráz pro dávkové stažení. Stahování se objeví ve **Přenosech souborů** a přistane ve vaší složce **Dokumenty**.
- **Info** u kterékoli položky zobrazí její druh, velikost, datum, cestu a podrobnosti o médiu.

## Změny souborů na serveru

Na serverech, které umožňují zápis - **WebDAV, FTP, SFTP a SMB** - můžete soubory také spravovat:

- **Nová složka**
- **Nahrát soubory** ze svého zařízení
- **Přejmenovat**, **Přesunout** a **Smazat** (jednu položku nebo několik naráz)

Servery **DLNA** jsou pouze ke čtení, takže tyto akce tam nejsou k dispozici.

## Sledování přenosů

Stahování a nahrávání běží na pozadí a objeví se ve **Přenosech souborů**, které otevřete vlevo nahoře na kartě **Dokumenty**. Tam můžete sledovat průběh a úlohy pozastavovat, obnovovat, opakovat, rušit nebo mazat. Přenosy můžete také doladit v [Nastavení → Síť](/docs/guide/everdisk/everdisk-guide-settings) (pouze Wi-Fi vs. Wi-Fi a mobilní data, kolik jich běží najednou a zda pokračují na pozadí).

## Další kroky

- [Soubory a dokumenty](/docs/guide/everdisk/everdisk-guide-files) - spravujte všechno, co stáhnete.
- [Fotky, hudba a video](/docs/guide/everdisk/everdisk-guide-media) - přehrávejte to, co streamujete.
- [Nastavení](/docs/guide/everdisk/everdisk-guide-settings) - limity připojení a možnosti přenosu.
