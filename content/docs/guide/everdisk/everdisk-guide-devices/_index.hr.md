---
title: "Povezivanje s poslužiteljima"
date: 2026-08-20
description: "Upotrijebite karticu Uređaji u Everdisku za povezivanje s drugim poslužiteljima na svojoj mreži. Dodajte i pregledavajte DLNA, WebDAV, FTP i SFTP poslužitelje te NAS diskove, strujite zvuk i video, preuzimajte datoteke te stvarajte, prenosite, preimenujte, premještajte ili brišite na poslužiteljima koji to dopuštaju."
keywords: ["Everdisk kartica Uređaji", "povezivanje s NAS", "DLNA klijent iPhone", "WebDAV klijent iPhone", "FTP klijent iPhone", "SFTP klijent iPhone", "pregledavanje mrežnog poslužitelja", "strujanje s NAS", "preuzimanje s poslužitelja", "povezivanje oblak WebDAV"]
tags: ["everdisk", "vodič", "uređaji", "povezivanja"]
readingTime: 9
---


Everdisk nije samo bežični disk - ujedno je i klijent za druge uređaje na vašoj mreži. Kartica **Uređaji** omogućuje vam povezivanje s **DLNA**, **WebDAV**, **FTP** i **SFTP** poslužiteljima, uključujući NAS diskove i medijske poslužitelje, a zatim pregledavanje, strujanje i preuzimanje njihovih datoteka.

## Zaslon Uređaji

Kartica Uređaji ima dva dijela:

- **Povezivanja** - poslužitelji koje ste već spremili.
- **Dostupni uređaji** - poslužitelji koje Everdisk automatski pronalazi na vašoj lokalnoj mreži.

Da biste se povezali s nečim što je Everdisk već pronašao, samo to dodirnite u odjeljku **Dostupni uređaji**. Da biste poslužitelj dodali ručno, dodirnite gumb **plus (+)** ili **Nova veza**.

## Dodavanje nove veze

Dodirnite **Nova veza** i odaberite vrstu poslužitelja koji želite dosegnuti:

- **DLNA / UPnP** - najbolje za medijske poslužitelje. Strujite video, glazbu i fotografije iz medijskih biblioteka, mrežnih diskova te DLNA televizora i računala. DLNA je samo za čitanje: možete pregledavati, strujati i preuzimati, ali ne možete prenositi ni mijenjati datoteke.
- **WebDAV** - povežite se s poslužiteljima datoteka, mrežnim diskovima i diskovima u oblaku koji podržavaju WebDAV. Čitanje i pisanje kad poslužitelj to dopušta.
- **FTP** - uobičajeno na usmjerivačima, mrežnim diskovima i web hostingu. Zadani port je 21 (990 za sigurni FTPS); možete postaviti prilagođeni port u adresi, na primjer `ftp://host:2121`. Ostavite prijavu i lozinku prazne za anonimni pristup.
- **SFTP** - povežite se sigurno putem SSH-a. Zadani port je 22; upotrijebite prilagođeni port u adresi ako je potrebno, na primjer `sftp://host:2222`.

> Everdisk se povezuje samo s tim protokolima na lokalnoj mreži i onima s izravnom adresom. Ne prijavljuje se u račune u oblaku poput Google Drivea ili Dropboxa. Disk u oblaku dostupan je samo ako ta usluga nudi **WebDAV** adresu koju možete upisati.

## Unesite adresu i prijavite se

U uređivaču veze ispunite:

- **Naziv** - prijateljski naziv za vezu.
- **URL / adresa** - adresa poslužitelja (primjeri su prikazani za svaku vrstu).
- **Prijava** i **Lozinka** - ostavite oboje prazno ako poslužitelj dopušta anonimni pristup.

Za WebDAV možete dopustiti nevaljane certifikate ako vaš poslužitelj koristi samopotpisani. Ako se identitet sigurnog poslužitelja ne može provjeriti, Everdisk vas traži potvrdu prije nego što mu povjeri.

Besplatni korisnici mogu spremiti do **10** veza. Premium uklanja ograničenje.

## Pregledavanje, strujanje i preuzimanje

Kad se povežete, dodirnite poslužitelj da biste ga otvorili:

- **Pregledavajte** mape u obliku popisa ili rešetke, razvrstajte ih i pogledajte sličice. DLNA poslužitelji prikazuju i pojedinosti o glazbi te naslovnice.
- **Strujite** zvuk i video. Zvuk odlazi u red čekanja mini reproduktora; video se reproducira preko cijelog zaslona. Premotavanje radi dok se datoteka struji.
- **Preuzimajte** datoteke na svoj uređaj. Odaberite nekoliko odjednom za skupno preuzimanje. Preuzimanja se pojavljuju u **Prijenosi datoteka** i završavaju u mapi **Dokumenti**.
- **Info** za bilo koju stavku prikazuje njezinu vrstu, veličinu, datum, putanju i pojedinosti o mediju.

## Mijenjanje datoteka na poslužitelju

Na poslužiteljima koji dopuštaju pisanje - **WebDAV, FTP i SFTP** - možete i upravljati datotekama:

- **Nova mapa**
- **Prijenos datoteka** s vašeg uređaja
- **Preimenovanje**, **Premještanje** i **Brisanje** (jedne stavke ili nekoliko njih odjednom)

**DLNA** poslužitelji su samo za čitanje, pa te radnje ondje nisu dostupne.

## Praćenje prijenosa

Preuzimanja i prijenosi odvijaju se u pozadini i pojavljuju se u odjeljku **Prijenosi datoteka**, koji otvarate iz gornjeg lijevog kuta kartice **Dokumenti**. Ondje možete pratiti napredak te pauzirati, nastaviti, ponoviti, otkazati ili obrisati zadatke. Prijenose možete i podesiti u [Postavke → Mreža](/docs/guide/everdisk/everdisk-guide-settings) (samo Wi-Fi ili Wi-Fi i mobilni podaci, koliko ih se izvodi odjednom te nastavljaju li se u pozadini).

## Sljedeći koraci

- [Datoteke i dokumenti](/docs/guide/everdisk/everdisk-guide-files) - upravljajte svime što preuzmete.
- [Fotografije, glazba i video](/docs/guide/everdisk/everdisk-guide-media) - reproducirajte ono što strujite.
- [Postavke](/docs/guide/everdisk/everdisk-guide-settings) - ograničenja veza i opcije prijenosa.
