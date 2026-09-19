---
title: "Dijeljenje"
date: 2026-08-20
description: "Naučite kako funkcionira dijeljenje u Everdisku: dodirnite Start da biste iPhone ili iPad pretvorili u bežični disk, odaberite što dijelite (datoteke, mape, fotografije i glazbu), pokrenite pet poslužitelja (DLNA, HTTP, WebDAV, SMB, FTP), šifrirajte SMB vezu pomoću SMB3 (AES), pročitajte adrese za povezivanje, provjerite tko je povezan i zadržite dijeljenje aktivnim putem Wi-Fi mreže ili USB kabela."
keywords: ["Everdisk dijeljenje", "bežični disk iPhone", "pokretanje dijeljenja", "dijeljenje datoteka iPhone", "dijeljenje fotografija preko mreže", "DLNA HTTP WebDAV FTP", "što dijeliti", "kako se povezati", "zadržati aplikaciju otvorenom", "dijeljenje preko Wi-Fi ili USB kabela"]
tags: ["everdisk", "vodič", "dijeljenje"]
readingTime: 9
---


Kartica **Dijeljenje** srce je Everdiska. Na njoj svoj iPhone ili iPad pretvarate u bežični disk, odabirete točno ono što želite dijeliti i dobivate adrese koje drugi uređaji koriste za povezivanje. To je prva kartica koju vidite kad otvorite aplikaciju.

## Pokretanje i zaustavljanje dijeljenja

U sredini zaslona Dijeljenje nalazi se veliki okrugli gumb.

- Dodirnite **Start** da biste sve omogućene poslužitelje istovremeno prebacili u rad. Gumb prikazuje **Pokretanje...**, a zatim **Stop** kad dijeljenje postane aktivno.
- Dodirnite **Stop** da biste sve ponovno isključili. Povezani uređaji se odspajaju.

Dok je dijeljenje aktivno, odabrane datoteke, fotografije i glazba dostupne su svakom uređaju na istoj mreži koji se poveže jednim od pet načina navedenih u nastavku.

> Dijeljenje radi samo dok je aplikacija otvorena. Pogledajte **Zadržite aplikaciju otvorenom** pri kraju ove stranice da biste saznali zašto je tako i kako održati velike prijenose u tijeku.

## Odaberite što dijelite

Prije nego što započnete, dodirnite zaglavlje **Što dijeliti** kako biste otvorili tri skupine. Možete dijeliti bilo koju njihovu kombinaciju, a prije početka dijeljenja morate odabrati barem jednu stavku.

**Datoteke i mape**

- Vlastita mapa **Dokumenti** vaše aplikacije dijeli se prema zadanim postavkama. Možete prestati dijeliti tu mapu ako želite.
- Dodirnite **Dodaj mapu** da biste podijelili mapu s bilo kojeg mjesta na uređaju ili **Dodaj datoteku** za dijeljenje pojedinačnih datoteka.
- Svaka dijeljena stavka ima gumb **Info** i gumb **Zaustavi dijeljenje**.

**Fotografije i videozapisi**

- Uključite **Dopusti pristup cijeloj biblioteci fotografija** da biste podijelili cijelu biblioteku fotografija i videozapisa ili
- dodirnite **Dodaj fotografije** da biste ručno odabrali samo fotografije i videozapise koje želite dijeliti.

**Glazba**

- Uključite **Dopusti pristup cijeloj glazbenoj biblioteci** da biste podijelili cijelu glazbenu biblioteku ili
- dodirnite **Dodaj pjesme** da biste podijelili samo odabrane pjesme.
- Pjesme koje su zaštićene (DRM) ili pohranjene samo u oblaku ne mogu se dijeliti.

Ako pokušate započeti bez ijedne odabrane stavke, Everdisk prikazuje napomenu **Nema ničega za dijeljenje**. Ako promijenite što se dijeli dok je dijeljenje aktivno, **zaustavite ga i ponovno pokrenite** kako biste primijenili promjenu.

## Pet poslužitelja

Everdisk dijeli isti sadržaj na pet načina istovremeno. Svaki je osmišljen za drugu vrstu uređaja i svaki se može uključiti ili isključiti u **Postavke → Dijeljenje → Povezivanja**. Prema zadanim postavkama svih je pet uključeno.

- **TV i medijski centar (DLNA)** - za pametne televizore i medijske uređaje. Oni sami otkrivaju vaš uređaj i prikazuju vaše fotografije, videozapise i glazbu, s pregledom u obliku sličica.
- **Preglednik (HTTP)** - za bilo koji telefon, tablet ili računalo. Druga osoba otvori poveznicu u web pregledniku kako bi pregledala i preuzela vaše datoteke. Ništa se ne instalira.
- **Računalo (WebDAV)** - za Mac, Windows PC ili Linux računalo. Vaš se uređaj pojavljuje kao običan mrežni disk pa možete povlačiti datoteke u oba smjera.
- **Računalo (napredno) (SMB)** - mrežni disk za Mac, Windows i Linux. Na Macu se sam pojavljuje u bočnoj traci Findera; na Windowsu ga otvorite u File Exploreru pomoću `smb://` adrese. To je jedina veza koju možete **šifrirati**, uz SMB3 šifriranje (AES).
- **Ostale aplikacije i uređaji (FTP)** - za aplikacije za datoteke i napredne korisnike koji koriste FTP.

Upute za povezivanje korak po korak za svaku vrstu potražite u [Povežite svoje uređaje](/docs/guide/everdisk/everdisk-guide-connect).

## Kako se povezati i adrese za povezivanje

Nakon što dodirnete Start, odjeljak **Kako se povezati** prikazuje karticu za svaki aktivni poslužitelj s točnom **adresom** koju upisujete na drugom uređaju. Svaku adresu lako je kopirati - dodirnite je za kopiranje, upotrijebite gumb **Podijeli** za slanje ili dodirnite gumb **info (ⓘ)** za detaljne upute za svaki protokol.

- DLNA kartica prikazuje adresu opisa uređaja koja završava na `/device-desc.xml` za uređaje koji je traže.
- Kad je vaš uređaj priključen na Mac kabelom, pojavljuje se dodatna adresa s oznakom **Kabelska veza** koja koristi `.local` naziv vašeg uređaja.

Adresu možete otvoriti i kao **QR kod** kako bi kamera drugog uređaja mogla izravno skočiti na nju.

## Tko je povezan

Odjeljak **Tko je povezan** u stvarnom vremenu navodi uređaje koji su trenutno povezani s vama. Dodirnite gumb za više radnji pokraj bilo kojeg uređaja da biste ga **blokirali** ako ga ne prepoznajete. Blokiranim uređajima upravlja se u [Pristup i privatnost](/docs/guide/everdisk/everdisk-guide-access).

## Naziv i avatar vašeg uređaja

Svaki uređaj ima prijateljski naziv (poput "Speedy-Hare") i avatar u boji. To je naziv koji TV, računalo ili druga aplikacija prikazuju za vaš uređaj na mreži, pa ga je lako prepoznati. Naziv i avatar možete besplatno ponovno generirati ili uz Premium postaviti prilagođeni naziv, ikonu ili avatar s fotografijom. Pogledajte [Postavke](/docs/guide/everdisk/everdisk-guide-settings).

## Dijeljenje preko Wi-Fi mreže ili USB kabela

Dijeljenje može raditi u dvije situacije:

- **Preko Wi-Fi mreže** - vaš uređaj i drugi uređaji nalaze se na istoj Wi-Fi mreži.
- **Preko USB kabela** - vaš je uređaj kabelom priključen na **Mac**, čak i kad Wi-Fi uopće nema. To je brže od Wi-Fi mreže i nastavlja raditi u avionu, u hotelu ili na zaključanoj mreži.

Ako nema ni Wi-Fi mreže ni kabela, gumb **Start** je onemogućen i pojavljuje se napomena **Nema Wi-Fi veze**. Ako veza prekine tijekom dijeljenja, Everdisk automatski zaustavlja dijeljenje i obavještava vas. Dodirnite gumb info na bilo kojoj od tih napomena za potpuno objašnjenje.

## Zadržite aplikaciju otvorenom

Budući da vaš iPhone ili iPad djeluje kao poslužitelj, **dijeljenje radi samo dok je Everdisk otvoren na zaslonu**. Ako zatvorite aplikaciju ili dulje vrijeme zaključate uređaj, sustav može pauzirati aplikaciju i dijeljenje se zaustavlja.

Za velike prijenose:

- Držite Everdisk otvorenim i u prvom planu.
- Priključite uređaj na napajanje.
- U aplikaciji iOS Postavke postavite **Automatsko zaključavanje** na **Nikad** dok traje prijenos.

Možete uključiti **Obavijesti prije odspajanja** (u Postavke → Dijeljenje) kako bi vas Everdisk podsjetio da ponovno otvorite aplikaciju prije nego što je sustav obustavi. Dodirnite gumb info na natpisu **Zadržite aplikaciju otvorenom** za više detalja.

## Sljedeći koraci

- [Povežite svoje uređaje](/docs/guide/everdisk/everdisk-guide-connect) - povežite TV, računalo, preglednik, telefon ili USB kabel.
- [Pristup i privatnost](/docs/guide/everdisk/everdisk-guide-access) - dodajte lozinku i upravljajte uređivanjem.
- [Postavke](/docs/guide/everdisk/everdisk-guide-settings) - uključite ili isključite poslužitelje i podesite kvalitetu.
