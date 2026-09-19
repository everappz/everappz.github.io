---
title: "Povežite svoje uređaje"
date: 2026-08-20
description: "Upute korak po korak za povezivanje s vašim Everdisk bežičnim diskom: gledajte na pametnom TV-u putem DLNA, otvorite datoteke u bilo kojem web pregledniku, priključite uređaj kao mrežni disk u Finderu, Windowsu ili Linuxu putem WebDAV-a ili SMB-a (uz neobvezno SMB3/AES šifriranje), povežite aplikacije za datoteke putem FTP-a i prenosite putem USB kabela na Mac bez Wi-Fi mreže."
keywords: ["povezivanje s Everdiskom", "strujanje na TV DLNA", "otvaranje datoteka u pregledniku", "priključivanje mrežnog diska Finder", "WebDAV Windows Linux", "FTP aplikacija za datoteke", "prijenos USB kabelom Mac", "povezivanje iPhonea s računalom", "mrežni disk iPhone"]
tags: ["everdisk", "vodič", "povezivanje"]
readingTime: 11
---


Kad dodirnete **Start** na zaslonu [Dijeljenje](/docs/guide/everdisk/everdisk-guide-sharing), drugi se uređaji mogu povezati s vašim datotekama na pet različitih načina. Odaberite način koji odgovara uređaju koji želite koristiti. U svakom slučaju, točna **adresa** koja vam je potrebna prikazana je u odjeljku **Kako se povezati** na zaslonu Dijeljenje.

> Oba uređaja moraju biti na **istoj Wi-Fi mreži** - ili, za Mac, povezana **USB kabelom** (pogledajte posljednji odjeljak).

## Gledajte na TV-u (DLNA)

Ovo koristite za prikaz fotografija, videozapisa i glazbe na pametnom TV-u ili medijskom uređaju.

1. U **Postavke → Dijeljenje → Povezivanja** provjerite je li **TV i medijski centar** uključen (uključen je prema zadanim postavkama).
2. Na zaslonu Dijeljenje dodirnite **Start**.
3. Na TV-u otvorite njegov ugrađeni medijski reproduktor ili aplikaciju medijskog poslužitelja (može se zvati Media Player, SmartShare, AllShare ili slično).
4. Vaš se uređaj pojavljuje na popisu medijskih poslužitelja pod svojim nazivom (na primjer "Speedy-Hare"). Odaberite ga.
5. Pregledavajte svoje dijeljene fotografije, videozapise i glazbu te započnite reprodukciju. Sličice za pregled pojavljuju se automatski.

Napomene:

- DLNA se ne može zaštititi lozinkom, pa je ova veza otvorena svakome na istoj Wi-Fi mreži dok je uključena.
- Ako se video ne reproducira na starijem TV-u, smanjite kvalitetu videa u **Postavke → Dijeljenje → Videozapisi** kako bi ga Everdisk pretvorio u kompatibilniji format.

## Otvaranje u web pregledniku (HTTP)

Ovo koristite za predaju datoteka bilo kome tko ima web preglednik - bez aplikacije za instalaciju.

1. U **Postavke → Dijeljenje → Povezivanja** provjerite je li **Preglednik** uključen.
2. Dodirnite **Start**.
3. Na zaslonu Dijeljenje kopirajte adresu za **Preglednik** (ili prikažite njezin QR kod).
4. Na drugom telefonu, tabletu ili računalu otvorite bilo koji web preglednik (Safari, Chrome, Edge, Firefox) i upišite tu adresu.
5. Otvara se stranica s vašim dijeljenim datotekama.

U pregledniku druga osoba može:

- prebacivati se između prikaza **popisa** i **rešetke** te razvrstavati po nazivu, datumu ili veličini;
- vidjeti prave **sličice** za fotografije, videozapise, PDF-ove i naslovnice glazbe;
- otvoriti fotografiju u **galeriji** preko cijelog zaslona s prelaskom prstom, zumiranjem prstima i prezentacijom;
- reproducirati glazbu u ugrađenom **reproduktoru** s redom čekanja, nasumičnom reprodukcijom i ponavljanjem;
- **preuzeti** bilo koju datoteku ili preuzeti cijelu mapu (ili nekoliko odabranih stavki) kao jedinstveni **Archive.zip**;
- **prenijeti** datoteke natrag na vaš uređaj - samo ako ste uključili **Uređivanje datoteka** (pogledajte [Pristup i privatnost](/docs/guide/everdisk/everdisk-guide-access)).

## Koristite ga kao mrežni disk (WebDAV)

Ovo koristite da bi se vaš uređaj pojavio kao običan disk na Macu, Windows PC-u ili Linux računalu, kako biste mogli povlačiti datoteke u oba smjera.

**Na Macu (Finder)**

1. U **Postavke → Dijeljenje → Povezivanja** provjerite je li **Računalo** uključeno.
2. Dodirnite **Start** i zabilježite adresu za **Računalo (WebDAV)**.
3. U Finderu odaberite **Idi → Poveži se s poslužiteljem** (ili pritisnite **⌘K**).
4. Upišite WebDAV adresu točno kako je prikazana i kliknite **Poveži se**.
5. Unesite prijavu i lozinku ako ste ih postavili, u suprotnom se povežite kao gost.
6. Vaš se uređaj otvara kao bilo koji drugi mrežni disk. Povlačite datoteke unutra ili van.

**Na Windowsu**

1. Otvorite **File Explorer**, desnom tipkom miša kliknite **Ovo računalo** i odaberite **Dodaj mrežnu lokaciju** (ili mapiraj mrežni disk).
2. Unesite WebDAV adresu prikazanu u Everdisku.
3. Unesite prijavu i lozinku ako ste ih postavili.

**Na Linuxu**

1. Otvorite svoj upravitelj datoteka i odaberite **Poveži se s poslužiteljem** (ili upotrijebite `davs://` / `dav://`).
2. Unesite WebDAV adresu prikazanu u Everdisku.

Hoće li veza biti samo za čitanje ili dvosmjerna, ovisi o postavci **Uređivanje datoteka**. Kad je uključena, možete kopirati datoteke na svoj uređaj te ih preimenovati ili izbrisati; kad je isključena, disk je samo za čitanje.

## Povezivanje putem SMB-a (šifrirani mrežni disk)

SMB je mrežni disk za Mac, Windows i Linux, izgrađen na dijeljenju datoteka koje već postoji u tim sustavima, pa se vaš uređaj pojavljuje kao običan mrežni disk - i to je jedina veza koju možete šifrirati.

1. U **Postavke → Dijeljenje → Povezivanja** provjerite je li **Računalo (napredno)** (SMB veza) uključeno.
2. Dodirnite **Start** i zabilježite adresu za **SMB**, koja izgleda ovako `smb://192.168.1.20:4455/Share`.
3. Povežite se sa svog računala:
   - **Mac:** vaš se uređaj sam pojavljuje u **bočnoj traci Findera** pod **Lokacije** (Mreža) - samo ga kliknite i prijavite se. Za ručno povezivanje odaberite **Idi → Poveži se s poslužiteljem** (**⌘K**) i unesite adresu.
   - **Windows:** otvorite **File Explorer**, desnom tipkom miša kliknite **Ovo računalo** i odaberite **Mapiraj mrežni disk**, a zatim unesite `\\<address>\Share` koristeći naziv računala i naziv dijeljenja sa zaslona Dijeljenje (ili upišite `smb://` adresu u adresnu traku).
   - **Linux:** u svom upravitelju datoteka odaberite **Poveži se s poslužiteljem** i unesite adresu.
4. Unesite prijavu i lozinku ako ste ih postavili, u suprotnom se povežite kao gost.
5. Dijeljenje se zove **Share**. Uz uključeno **Uređivanje datoteka** možete kopirati datoteke u oba smjera; uz isključeno je samo za čitanje.

**Uključivanje šifriranja (preporučeno na Wi-Fi mreži kojoj ne vjerujete)**

SMB je jedina Everdisk veza koju se može šifrirati. Da biste svaki prijenos zaštitili **SMB3 šifriranjem (AES)**:

1. U **Postavke → Dijeljenje → Pristup** postavite **Prijavu** i **Lozinku** - šifrirane veze ne mogu biti anonimne.
2. U **Postavke → Dijeljenje** uključite **Zahtijevaj SMB šifriranje**.
3. **Zaustavite i ponovno pokrenite** dijeljenje kako bi promjena stupila na snagu.

Vaš klijent mora podržavati SMB3 - Finder na modernom Macu ili **Windows 10 i noviji**. SMB šifriranje je Premium značajka.

## Povezivanje aplikacije za datoteke (FTP)

Ovo koristite za aplikacije za upravljanje datotekama i prijenos koje koriste FTP (na primjer FileZilla ili Cyberduck na računalu).

1. U **Postavke → Dijeljenje → Povezivanja** provjerite je li **Ostale aplikacije i uređaji** uključeno.
2. Dodirnite **Start** i zabilježite **FTP** adresu.
3. U svojoj FTP aplikaciji dodajte novu vezu koristeći tu adresu.
4. Unesite prijavu i lozinku ako ste ih postavili ili ih ostavite prazne za anonimni pristup.

## Prijenos putem USB kabela (Mac, Wi-Fi nije potreban)

Ovo koristite kada nema Wi-Fi mreže ili kada želite najbrži i najprivatniji prijenos. Radi isključivo s **Macom**.

1. Priključite iPhone ili iPad na Mac uobičajenim kabelom za punjenje.
2. Ako se na uređaju to od vas zatraži, dodirnite **Vjeruj ovom računalu**.
3. U Everdisku dodirnite **Start**. Pojavljuje se napomena **Dostupna brza veza**, a zaslon Dijeljenje prikazuje dodatnu adresu s oznakom **Kabelska veza** koja završava na `.local`.
4. Na Macu otvorite Finder → **Idi → Poveži se s poslužiteljem** (**⌘K**) i unesite tu `.local` adresu (radi i za vezu Preglednik i za vezu Računalo).
5. Vaš se uređaj otvara preko kabela - brže od Wi-Fi mreže, a podaci nikad ne dolaze do usmjerivača ni interneta.

Napomene:

- Koristite **`.local` naziv**, ne IP adresu (IP adrese rade samo preko Wi-Fi mreže), i nikad `localhost`.
- Kabelski put je **samo za Mac**. Windows PC-ovi i Android uređaji moraju koristiti Wi-Fi.
- Datoteke možete povući i u mapu Everdisk pomoću Findera na Macu ili aplikacije Apple Devices (ili iTunesa) na Windowsu, putem standardnog dijeljenja datoteka na iOS-u.

## Sljedeći koraci

- [Pristup i privatnost](/docs/guide/everdisk/everdisk-guide-access) - dodajte lozinku, dopustite prijenose, blokirajte uređaj.
- [Fotografije, glazba i video](/docs/guide/everdisk/everdisk-guide-media) - podijelite cijelu biblioteku i postavite kvalitetu.
- [Povezivanje s poslužiteljima](/docs/guide/everdisk/everdisk-guide-devices) - dosegnite druge uređaje iz Everdiska.
