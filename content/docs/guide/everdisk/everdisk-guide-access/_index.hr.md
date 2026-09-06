---
title: "Pristup i privatnost"
date: 2026-08-20
description: "Zadržite dijeljenje u Everdisku sigurnim: zaštitite pristup prijavom i lozinkom, upravljajte time mogu li povezani uređaji prenositi, preimenovati i brisati pomoću Uređivanja datoteka, blokirajte nepoznate uređaje, odaberite smeće ili trajno brisanje i shvatite zašto sve ostaje na vašoj lokalnoj mreži."
keywords: ["Everdisk zaštita lozinkom", "prekidač za uređivanje datoteka", "blokiranje uređaja", "blokirani uređaji", "trajno brisanje datoteka", "samo lokalna mreža", "privatno dijeljenje datoteka", "DLNA bez lozinke", "sigurnost mreže"]
tags: ["everdisk", "vodič", "pristup", "privatnost", "sigurnost"]
readingTime: 8
---


Everdisk čuva vaše datoteke na vlastitoj mreži i daje vam jednostavne kontrole nad time tko im može pristupiti i što može činiti. Te kontrole pronaći ćete u **Postavke → Dijeljenje → Pristup**, uz nekoliko srodnih postavki u Upravitelju datoteka.

## Zaštitite pristup prijavom i lozinkom

Prema zadanim postavkama svatko na istoj mreži tko ima vašu adresu može otvoriti vaše dijeljene datoteke. Da biste zahtijevali prijavu:

1. Idite na **Postavke → Dijeljenje → Pristup**.
2. Unesite **Prijavu** i **Lozinku**.
3. Sada veze **Preglednik (HTTP)**, **Računalo (WebDAV)** i **Ostale aplikacije i uređaji (FTP)** sve traže te podatke prije nego što prikažu vaše datoteke.

Ostavite oba polja prazna za otvoreni pristup. Vaša se lozinka sigurno pohranjuje u Keychain uređaja.

> **DLNA je uvijek otvoren.** Veza TV i medijski centar (DLNA) ne može se zaštititi lozinkom, pa svaki uređaj na istoj Wi-Fi mreži može pregledavati vaše dijeljene medije čim je uključena. Isključite je ako želite samo zaštićene veze i dijelite samo na mrežama kojima vjerujete.

## Dopustite ili blokirajte uređivanje (Uređivanje datoteka)

Prekidač **Uređivanje datoteka** upravlja time mogu li povezani uređaji samo gledati vaše datoteke ili ih i mijenjati.

- **Uključeno** (zadano): povezani uređaji mogu **prenositi, preimenovati i brisati** vaše dijeljene datoteke - pa vaš uređaj radi kao pravi dvosmjerni mrežni disk.
- **Isključeno**: vaše dijeljene datoteke su **samo za čitanje**. Drugi mogu pregledavati i preuzimati, ali ne mogu ništa dodati ni promijeniti.

Uključivanje prikazuje kratko upozorenje jer omogućuje drugim ljudima izmjenu vaših datoteka. Dok je uključeno, nosi oznaku **Važno**.

## Blokiranje uređaja

Ako vidite uređaj koji ne prepoznajete:

1. Na zaslonu Dijeljenje pronađite ga pod **Tko je povezan**.
2. Dodirnite njegov gumb za više radnji i odaberite **Blokiraj ovaj uređaj**.

Blokirani uređaji navedeni su u **Postavke → Dijeljenje → Pristup → Blokirani uređaji**, gdje jedan možete **odblokirati** ili **Odblokirati sve**. Blokiranje prati uređaj čak i ako se njegova mrežna adresa promijeni (za veze Preglednik, Računalo i TV).

## Smeće u odnosu na trajno brisanje

Kad se datoteka izbriše - vi u upravitelju datoteka ili povezani uređaj - obično odlazi u **smeće** iz kojeg se može vratiti kako biste je mogli povratiti.

Ako želite da se datoteke uklone odmah bez mogućnosti vraćanja, uključite **Trajno izbriši datoteke** u **Postavke → Upravitelj datoteka → Brisanje datoteka**. Ovo je prema zadanim postavkama isključeno. **Utječe na upravitelj datoteka na uređaju** i na **brisanja izvršena preko mreže**; ne mijenja način na koji sustavna biblioteka Fotografije ili glazbena biblioteka postupaju s brisanjem.

## Sve ostaje lokalno

Everdisk dijeli samo preko vaše **lokalne mreže** - ništa se ne prenosi na internet i nema računa u oblaku u sredini. Vrijedi znati nekoliko stvari:

- Everdisku je potrebno dopuštenje iOS-a **Lokalna mreža** kako bi ga obližnji uređaji mogli pronaći. Ako je to dopuštenje isključeno, napomena objašnjava kako ga ponovno uključiti u aplikaciji iOS Postavke.
- Za najveću privatnost dijelite samo dok ste na **kućnoj ili privatnoj Wi-Fi** mreži kojoj vjerujete i budite oprezni na javnom Wi-Fi-ju. Prijava i lozinka pomažu, ali nisu zamjena za pouzdanu mrežu.
- **Najprivatnija opcija od svih jest USB kabel prema Macu** - podaci idu izravno preko kabela i nikad ne dolaze do usmjerivača ni interneta. Pogledajte [Povežite svoje uređaje](/docs/guide/everdisk/everdisk-guide-connect).

## Sljedeći koraci

- [Dijeljenje](/docs/guide/everdisk/everdisk-guide-sharing) - odaberite što dijelite i pokrenite dijeljenje.
- [Postavke](/docs/guide/everdisk/everdisk-guide-settings) - sve postavke Pristupa i Upravitelja datoteka na jednom mjestu.
