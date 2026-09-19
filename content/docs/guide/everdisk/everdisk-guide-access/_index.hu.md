---
title: "Hozzáférés és adatvédelem"
date: 2026-08-20
description: "Tartsd biztonságban az Everdisk megosztásodat: védd a hozzáférést bejelentkezéssel és jelszóval, titkosítsd az SMB kapcsolatot SMB3-mal (AES), szabályozd a Fájlszerkesztéssel, hogy a csatlakozott eszközök feltölthetnek, átnevezhetnek és törölhetnek-e, blokkold az ismeretlen eszközöket, válassz a kuka és a végleges törlés között, és értsd meg, miért marad minden a helyi hálózatodon."
keywords: ["Everdisk jelszavas védelem", "SMB-titkosítás", "SMB3 AES titkosítás", "fájlszerkesztés kapcsoló", "eszköz blokkolása", "blokkolt eszközök", "fájlok végleges törlése", "csak helyi hálózat", "bizalmas fájlmegosztás", "DLNA jelszó nélkül", "hálózati biztonság"]
tags: ["everdisk", "guide", "access", "privacy", "security"]
readingTime: 8
---


Az Everdisk a saját hálózatodon tartja a fájljaidat, és egyszerű vezérlőket ad ahhoz, hogy ki érheti el őket és mit tehet velük. Ezeket a vezérlőket a **Beállítások → Megosztás → Hozzáférés** menüben találod, néhány kapcsolódó beállítás mellett a Fájlkezelőben.

## Védd a hozzáférést bejelentkezéssel és jelszóval

Alapértelmezés szerint az azonos hálózaton lévő bárki, akinek megvan a címed, megnyithatja a megosztott fájljaidat. Ha be szeretnél kényszeríteni egy bejelentkezést:

1. Menj a **Beállítások → Megosztás → Hozzáférés** menübe.
2. Adj meg egy **Bejelentkezési nevet** és egy **Jelszót**.
3. Ezután a **Böngésző (HTTP)**, a **Számítógép (WebDAV)**, a **Számítógép (speciális) (SMB)** és a **Más alkalmazások és eszközök (FTP)** kapcsolatok mind bekérik ezeket az adatokat, mielőtt megjelenítenék a fájljaidat.

Hagyd mindkét mezőt üresen a nyitott hozzáféréshez. A jelszavad biztonságosan tárolódik az eszköz Kulcskarikájában.

> **A DLNA mindig nyitva van.** A TV és médiaközpont (DLNA) kapcsolat nem védhető jelszóval, így ha egyszer be van kapcsolva, az azonos Wi-Fi-n lévő bármely eszköz böngészheti a megosztott médiádat. Kapcsold ki, ha csak védett kapcsolatokat szeretnél, és csak olyan hálózatokon ossz meg, amelyekben megbízol.

## Titkosítsd az SMB kapcsolatot (SMB3 / AES)

A bejelentkezési név és a jelszó azt szabályozza, hogy **ki** csatlakozhat, de maga az adat a legtöbb kapcsolaton továbbra is nyílt szövegként utazik. **Az SMB az egyetlen kapcsolat, amelyet az Everdisk titkosítani tud**, ami minden átvitelt összekever, így senki más az azonos hálózaton nem tudja elolvasni.

A bekapcsolásához:

1. Állíts be egy **Bejelentkezési nevet** és **Jelszót** a fentiek szerint - a titkosított kapcsolatok nem lehetnek névtelenek.
2. Menj a **Beállítások → Megosztás** menübe, és kapcsold be az **SMB-titkosítás megkövetelése** lehetőséget.
3. **Állítsd le, majd indítsd újra** a megosztást, hogy a változtatás életbe lépjen.

Ezután minden SMB-átvitelt **SMB3-titkosítás (AES)** véd. A csatlakozó eszköznek támogatnia kell az SMB3-at - a Finder egy modern Macen, vagy a **Windows 10 és újabb**. Ez remek választás olyan Wi-Fi-n, amelyben nem bízol meg teljesen. Az SMB-titkosítás Premium funkció.

## Engedélyezd vagy tiltsd a szerkesztést (Fájlszerkesztés)

A **Fájlszerkesztés** kapcsoló szabályozza, hogy a csatlakozott eszközök csak megnézhetik a fájljaidat, vagy módosíthatják is azokat.

- **Bekapcsolva** (alapértelmezett): a csatlakozott eszközök **feltölthetnek, átnevezhetnek és törölhetnek** a megosztott fájljaidból - így az eszközöd valódi kétirányú hálózati meghajtóként működik.
- **Kikapcsolva**: a megosztott fájljaid **csak olvashatók**. Mások megtekinthetik és letölthetik őket, de semmit sem adhatnak hozzá és nem módosíthatnak.

A bekapcsolása egy rövid figyelmeztetést jelenít meg, mert lehetővé teszi, hogy mások módosítsák a fájljaidat. Amíg be van kapcsolva, egy **Fontos** jelzést visel.

## Egy eszköz blokkolása

Ha egy olyan eszközt látsz, amelyet nem ismersz fel:

1. A Megosztás képernyőn keresd meg a **Ki csatlakozott** alatt.
2. Érintsd meg a további műveletek gombját, és válaszd a **Blokkold ezt az eszközt** lehetőséget.

A blokkolt eszközök a **Beállítások → Megosztás → Hozzáférés → Blokkolt eszközök** menüben vannak felsorolva, ahol **feloldhatod** egy eszköz blokkolását vagy **Az összes feloldása** lehetőséggel az összesét. A blokkolás az eszközt akkor is követi, ha annak hálózati címe megváltozik (a Böngésző, a Számítógép és a TV kapcsolatoknál).

## Kuka vs. végleges törlés

Amikor egy fájl törlődik - akár te törlöd a fájlkezelőben, akár egy csatlakozott eszköz -, az általában egy helyreállítható **kukába** kerül, hogy visszaszerezhesd.

Ha azt szeretnéd, hogy a fájlok azonnal, helyreállítás nélkül törlődjenek, kapcsold be a **Fájlok végleges törlése** lehetőséget a **Beállítások → Fájlkezelő → Fájlok törlése** menüben. Ez alapértelmezés szerint ki van kapcsolva. **Az eszközön lévő fájlkezelőt** és a **hálózaton keresztül végrehajtott törléseket** is érinti; nem változtatja meg azt, ahogyan a rendszer Fotók könyvtára vagy Zene könyvtára kezeli a törlést.

## Minden helyben marad

Az Everdisk csak a **helyi hálózatodon** oszt meg - semmi sem kerül fel az internetre, és nincs felhőfiók sem közben. Néhány dolgot érdemes tudni:

- Az Everdisknek szüksége van az iOS **Helyi hálózat** engedélyére, hogy a közeli eszközök megtalálhassák. Ha ez az engedély ki van kapcsolva, egy üzenet elmagyarázza, hogyan kapcsolhatod vissza az iOS Beállítások alkalmazásában.
- A legnagyobb adatvédelem érdekében csak akkor ossz meg, amikor egy megbízható **otthoni vagy privát Wi-Fi** hálózaton vagy, és légy óvatos a nyilvános Wi-Fi-n. A bejelentkezés és a jelszó segít, de nem helyettesíti a megbízható hálózatot.
- **A legbizalmasabb lehetőség mind közül egy USB-kábel egy Machez** - az adat egyenesen a kábelen keresztül megy, és soha nem érinti a routert vagy az internetet. Lásd [Eszközeid csatlakoztatása](/docs/guide/everdisk/everdisk-guide-connect).

## Következő lépések

- [Megosztás](/docs/guide/everdisk/everdisk-guide-sharing) - válaszd ki, mit osztasz meg, és indítsd el a megosztást.
- [Beállítások](/docs/guide/everdisk/everdisk-guide-settings) - az összes Hozzáférés és Fájlkezelő beállítás egy helyen.
