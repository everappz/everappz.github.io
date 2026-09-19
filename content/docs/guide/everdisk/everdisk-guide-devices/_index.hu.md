---
title: "Csatlakozás kiszolgálókhoz"
date: 2026-08-20
description: "Használd az Everdisk Eszközök fülét, hogy a hálózatodon lévő többi kiszolgálóhoz csatlakozz. Adj hozzá és böngéssz DLNA, WebDAV, FTP, SFTP és SMB kiszolgálókat és NAS-meghajtókat, streamelj hangot és videót, tölts le fájlokat, és hozz létre, tölts fel, nevezz át, mozgass vagy törölj azokon a kiszolgálókon, amelyek ezt engedélyezik."
keywords: ["Everdisk Eszközök fül", "csatlakozás NAS-hoz", "DLNA kliens iPhone", "WebDAV kliens iPhone", "FTP kliens iPhone", "SFTP kliens iPhone", "SMB kliens iPhone", "csatlakozás SMB megosztáshoz", "hálózati kiszolgáló böngészése", "streamelés NAS-ról", "letöltés kiszolgálóról", "csatlakozás felhő WebDAV"]
tags: ["everdisk", "guide", "devices", "connections"]
readingTime: 9
---


Az Everdisk nem csupán egy vezeték nélküli meghajtó - egyben kliens is a hálózatodon lévő többi eszközhöz. Az **Eszközök** fül lehetővé teszi, hogy **DLNA**, **WebDAV**, **FTP**, **SFTP** és **SMB** kiszolgálókhoz csatlakozz - beleértve a Maceket, Windows PC-ket, Linux gépeket, NAS-meghajtókat és médiakiszolgálókat is -, majd böngészd, streameld és letöltsd azok fájljait.

## Az Eszközök képernyő

Az Eszközök fül két részből áll:

- **Kapcsolatok** - a már elmentett kiszolgálóid.
- **Elérhető eszközök** - azok a kiszolgálók, amelyeket az Everdisk automatikusan megtalál a helyi hálózatodon.

Ha egy olyan dologhoz szeretnél csatlakozni, amelyet az Everdisk már megtalált, egyszerűen érintsd meg az **Elérhető eszközök** listájában. Ha kézzel szeretnél hozzáadni egy kiszolgálót, érintsd meg a **plusz (+)** gombot vagy az **Új kapcsolat** lehetőséget.

## Új kapcsolat hozzáadása

Érintsd meg az **Új kapcsolat** lehetőséget, és válaszd ki az elérni kívánt kiszolgáló típusát:

- **DLNA / UPnP** - a legjobb választás médiakiszolgálókhoz. Streamelj videót, zenét és fotókat médiakönyvtárakból, hálózati tárolómeghajtókról, valamint DLNA-képes TV-kről és számítógépekről. A DLNA csak olvasható: böngészhetsz, streamelhetsz és letölthetsz, de nem tölthetsz fel és nem módosíthatsz fájlokat.
- **WebDAV** - csatlakozz fájlkiszolgálókhoz, hálózati tárolómeghajtókhoz és WebDAV-ot támogató felhőmeghajtókhoz. Olvasás és írás, amikor a kiszolgáló engedélyezi.
- **FTP** - gyakori routereken, hálózati tárolómeghajtókon és webtárhelyeken. Az alapértelmezett port a 21 (990 a biztonságos FTPS esetén); egyéni portot is megadhatsz a címben, például `ftp://host:2121`. Hagyd üresen a bejelentkezési nevet és jelszót az anonim hozzáféréshez.
- **SFTP** - csatlakozz biztonságosan SSH-n keresztül. Az alapértelmezett port a 22; szükség esetén egyéni portot használhatsz a címben, például `sftp://host:2222`.
- **SMB** - csatlakozz Macekhez, Windows PC-khez, Linux kiszolgálókhoz és hálózati tárolókhoz (NAS), amelyek **SMB / CIFS** protokollon osztanak meg mappákat. Adj meg egy `smb://server-address/share-name/` formátumú címet (példák: `smb://local-server-name/share-name/folder-path`, `smb://192.168.1.105/share-name/folder-path`, `smb://remote-server.com`). Az SMB két opcionális mezőt ad hozzá: egy **Munkacsoport** nevet, és egy **Protokollverziót**, amelyet hagyhatsz **Automatikus** értéken, vagy kényszeríthetsz **SMB1**-re vagy **SMB2**-re. Ha a különleges karaktereket tartalmazó fájlok vagy mappák nem nyílnak meg, próbáld meg átváltani a verziót **SMB1**-re.

> Az Everdisk csak ezekhez a helyi hálózati és közvetlenül címzett protokollokhoz csatlakozik. Nem jelentkezik be felhőfiókokba, mint a Google Drive vagy a Dropbox. Egy felhőmeghajtó csak akkor érhető el, ha az adott szolgáltatás kínál egy **WebDAV**-címet, amelyet be tudsz írni.

## Add meg a címet és jelentkezz be

A kapcsolatszerkesztőben töltsd ki a következőket:

- **Cím (Title)** - egy barátságos név a kapcsolatnak.
- **URL / cím** - a kiszolgáló címe (minden típushoz példák jelennek meg).
- **Bejelentkezési név** és **Jelszó** - hagyd mindkettőt üresen, ha a kiszolgáló engedélyezi az anonim hozzáférést.

WebDAV esetén engedélyezheted az érvénytelen tanúsítványokat, ha a kiszolgálód önaláírt tanúsítványt használ. Ha egy biztonságos kiszolgáló azonossága nem ellenőrizhető, az Everdisk megerősítést kér, mielőtt megbíznál benne.

Az ingyenes felhasználók legfeljebb **10** kapcsolatot menthetnek. A Premium eltávolítja a korlátot.

## Böngészés, streamelés és letöltés

Ha csatlakoztál, érintsd meg a kiszolgálót a megnyitásához:

- **Böngészd** a mappákat listában vagy rácsban, rendezd őket, és nézd meg a bélyegképeket. A DLNA-kiszolgálók zenei részleteket és borítókat is megjelenítenek.
- **Streamelj** hangot és videót. A hang a minilejátszó lejátszási sorába kerül; a videó teljes képernyőn játszódik le. A tekerés streamelés közben is működik.
- **Tölts le** fájlokat az eszközödre. Válassz ki többet egyszerre a kötegelt letöltéshez. A letöltések a **Fájlátvitelek** között jelennek meg, és a **Dokumentumok** mappádba kerülnek.
- Az **Info** bármelyik elemnél megmutatja annak típusát, méretét, dátumát, elérési útját és médiarészleteit.

## Fájlok módosítása egy kiszolgálón

Azokon a kiszolgálókon, amelyek engedélyezik az írást - **WebDAV, FTP, SFTP és SMB** -, fájlokat is kezelhetsz:

- **Új mappa**
- **Fájlok feltöltése** az eszközödről
- **Átnevezés**, **Áthelyezés** és **Törlés** (egy vagy több elem egyszerre)

A **DLNA**-kiszolgálók csak olvashatók, így ezek a műveletek ott nem érhetők el.

## Kövesd nyomon az átviteleidet

A letöltések és feltöltések a háttérben futnak, és a **Fájlátvitelek** között jelennek meg, amelyet a **Dokumentumok** fül bal felső részéből nyithatsz meg. Ott figyelheted a folyamatot, valamint szüneteltetheted, folytathatod, újrapróbálhatod, megszakíthatod vagy törölheted a feladatokat. Az átviteleket a [Beállítások → Hálózat](/docs/guide/everdisk/everdisk-guide-settings) menüben is finomhangolhatod (csak Wi-Fi vagy Wi-Fi és mobiladat, egyszerre hány fusson, és folytatódjanak-e a háttérben).

## Következő lépések

- [Fájlok és dokumentumok](/docs/guide/everdisk/everdisk-guide-files) - kezeld mindazt, amit letöltöttél.
- [Fotók, zene és videó](/docs/guide/everdisk/everdisk-guide-media) - játszd le, amit streamelsz.
- [Beállítások](/docs/guide/everdisk/everdisk-guide-settings) - kapcsolati korlátok és átviteli beállítások.
