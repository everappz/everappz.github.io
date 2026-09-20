---
title: "Kako postaviti FTP poslužitelj na iPhoneu i iPadu za prijenos datoteka"
description: "Pretvorite iPhone ili iPad u FTP poslužitelj uz Everdisk i prenosite datoteke s Maca, Windows PC-a, Linuxa, Androida, FTP aplikacije poput FileZille ili drugog iPhonea putem Wi-Fi. Cjelovito postavljanje, ftp adresa i port, gostujući pristup te povezivanje korak po korak za svaki uređaj."
date: 2026-09-19
tags: ["everdisk", "ftp", "prijenos datoteka", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["FTP poslužitelj iPhone", "FTP poslužitelj iPad", "kako postaviti FTP na iPhoneu", "aplikacija ftp poslužitelj iphone", "povezivanje FileZille s iPhoneom", "Cyberduck iPhone FTP", "prijenos datoteka iPhone FTP", "ftp iphone na računalo", "ftp iphone na iphone", "povezivanje na iPhone FTP s Windowsa", "ftp adresa port iphone", "anonimni ftp iphone", "dijeljenje datoteka iphone ftp", "iphone ftp za kameru nas"]
readingTime: 9
---

{{< author-byline >}}

FTP je stari pouzdanik prijenosa datoteka. Postoji desetljećima, što je upravo razlog zašto je toliko koristan: gotovo sve što može razgovarati s poslužiteljem razumije ga. Kamere, pametni TV-i, usmjerivači, mrežni diskovi, alati za automatizaciju i svaka stolna FTP aplikacija govore FTP. Uz [Everdisk](/products/everdisk) možete pokrenuti FTP poslužitelj na svom iPhoneu ili iPadu, pa telefon postaje mjesto na koje se ti uređaji i aplikacije mogu povezati i premještati datoteke.

Posegnite za FTP-om kada druge opcije ne odgovaraju, na primjer stariji uređaj ili aplikacija koja se zna povezati samo putem FTP-a. Ovaj vodič pokriva postavljanje i povezivanje s Maca, Windowsa, FTP aplikacije, Linuxa, Androida i drugog iPhonea.

## Što vam je potrebno

- iPhone ili iPad s instaliranim [Everdiskom](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Računalo, aplikacija ili uređaj na **istoj Wi-Fi mreži**.
- Datoteke koje želite dijeliti, u Everdiskovoj mapi Dokumenti ili u mapama koje dodate.

## Postavite FTP poslužitelj u Everdisku

### Korak 1: Odaberite što dijeliti i postavite pristup

Otvorite Everdisk, idite na karticu **Dijeljenje** i dodirnite **Što dijeliti**. Mapa Dokumenti dijeli se prema zadanim postavkama. Dodajte još pomoću **Dodaj mapu** i **Dodaj datoteku**.

Otvorite **Postavke**, zatim **Dijeljenje**, pa **Pristup**. Uključite **Uređivanje datoteka** ako želite da ljudi prenose, preimenuju i brišu, ili isključite da dopustite samo preuzimanja. Postavite **Prijava** i **Lozinka** ako želite prijavu ili ih ostavite prazne kako bi se svatko mogao povezati kao gost.

### Korak 2: Uključite FTP poslužitelj

Idite na **Postavke**, zatim **Dijeljenje**, pa **Veze** i uključite **Druge aplikacije i uređaji**. To je FTP poslužitelj (nosi oznaku FTP).

### Korak 3: Pokrenite dijeljenje i zabilježite adresu

Vratite se na karticu **Dijeljenje** i dodirnite **Start**. Odjeljak **Kako se povezati** prikazuje FTP adresu. Izgleda ovako:

```
ftp://192.168.1.20:2121
```

Broj iza dvotočke je **port**, koji je prema zadanim postavkama **2121**. Prvi dio je adresa vašeg iPhonea na Wi-Fi mreži, pa će vaša biti drugačija. Držite Everdisk otvorenim na zaslonu dok je uređaj povezan.

## Povezivanje s Maca

1. Otvorite **Finder**, odaberite **Go**, zatim **Connect to Server** (ili pritisnite **Command i K**).
2. Upišite FTP adresu prikazanu u Everdisku, na primjer `ftp://192.168.1.20:2121`.
3. Kliknite **Connect**, zatim odaberite **Guest** ili unesite svoju **Prijava** i **Lozinka**.

Finder povezuje FTP dijeljenje pa možete pregledavati i kopirati datoteke na svoj Mac. Imajte na umu da Finder otvara FTP samo za čitanje. Kad želite prenositi s Maca, koristite FTP aplikaciju kako je opisano u nastavku.

## Povezivanje s Windowsa

1. Otvorite **File Explorer** i kliknite adresnu traku na vrhu.
2. Upišite FTP adresu iz Everdiska, na primjer `ftp://192.168.1.20:2121`, i pritisnite **Enter**.
3. Unesite svoju **Prijava** i **Lozinka** ako ste ih postavili ili nastavite kao gost.

Dijeljene datoteke pojavljuju se u prozoru i možete ih kopirati na svoj PC.

## Povezivanje FTP aplikacijom (FileZilla, Cyberduck)

Za prijenose i punu kontrolu FTP aplikacija je najbolji alat. **FileZilla** i **Cyberduck** besplatni su i rade na Windowsu, Macu i Linuxu.

1. Otvorite aplikaciju i stvorite novu vezu.
2. Postavite **Host** na Wi-Fi adresu vašeg iPhonea, a **Port** na **2121**.
3. Za prijavu unesite svoju **Prijava** i **Lozinka** ili odaberite **Anonymous** ako je niste postavili.
4. Povežite se i povlačite datoteke u oba smjera (za prijenose treba uključeno Uređivanje datoteka).

## Povezivanje s Linuxa

1. Otvorite svoj upravitelj datoteka i odaberite **Connect to Server** ili **Other Locations**.
2. Unesite adresu, na primjer `ftp://192.168.1.20:2121`.
3. Povežite se kao gost ili sa svojom prijavom.

Iz terminala možete koristiti i bilo koji Linux FTP klijent, usmjeravajući ga na isti host i port 2121.

## Povezivanje s Androida

Android nema sistemski FTP preglednik, pa koristite aplikaciju:

1. Instalirajte FTP klijent poput **AndFTP**, **FTPCafe** ili upravitelj datoteka s podrškom za FTP poput **Solid Explorer**.
2. Dodajte vezu s hostom, **portom 2121** i svojom prijavom ili Anonymous.
3. Pregledavajte i prenosite.

## Povezivanje s drugog iPhonea ili iPada

iOS aplikacija Datoteke ne uključuje FTP klijent, pa na drugom uređaju koristite jedno od ovoga:

- **Everdiskovu vlastitu karticu Uređaji.** Otvorite Everdisk, idite na **Uređaji**, dodirnite **Nova veza**, odaberite **FTP** i unesite adresu, na primjer `ftp://192.168.1.20:2121`. Ovo je najjednostavniji put.
- **Namjensku FTP aplikaciju** za iOS, koristeći isti host, port 2121 i prijavu.

## Povežite drugu opremu: kamere, TV-e, usmjerivače i NAS

Ovdje FTP zablista. Mnogi uređaji imaju ugrađeni FTP klijent koji može slati ili dohvaćati datoteke:

- **Kamere** koje prenose fotografije putem FTP-a mogu ih slati izravno na vaš iPhone.
- **Pametni TV-i, usmjerivači, NAS kutije i alati za automatizaciju** koji podržavaju FTP mogu se povezati na isti način.

Usmjerite ih na Wi-Fi adresu vašeg iPhonea, port **2121** i svoju prijavu (ili Anonymous), koristeći adresu prikazanu u Everdisku.

## Samo za čitanje ili čitanje i pisanje

Preklopnik **Uređivanje datoteka** u Postavke, Dijeljenje, Pristup kontrolira ovo. Uključeno omogućuje ljudima da prenose, preimenuju i brišu. Isključeno znači da mogu samo preuzimati. Odaberite samo za čitanje kada predajete datoteke i ne želite da se išta mijenja na vašem telefonu.

## Načini na koje ljudi ovo koriste u praksi

- **Povežite FileZillu sa svojim iPhoneom** i gurnite hrpu datoteka na telefon odjednom.
- **Pustite staru aplikaciju ili uređaj koji govori samo FTP** da dođe do vaših datoteka kad se ništa drugo neće povezati.
- **Primite fotografije s kamere** koja prenosi putem FTP-a.
- **Premjestite datoteke između iPhonea i iPada** pomoću Everdiskove kartice Uređaji na uređaju koji prima.

## Nekoliko savjeta

- Dok je uređaj povezan, držite Everdisk otvorenim jer iOS nakon nekog vremena pauzira pozadinske aplikacije.
- Za prijenos s Maca koristite FileZillu ili Cyberduck umjesto Findera jer Finder otvara FTP samo za čitanje.
- Ostavite prijavu praznom za najširu kompatibilnost, zatim se povežite kao Anonymous, što većina FTP klijenata nudi.
- FTP ne šifrira svoj promet. Na mreži kojoj ne vjerujete umjesto toga koristite [SMB poslužitelj sa šifriranjem](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/).

## Često postavljana pitanja

{{% details title="Koja je FTP adresa i port za moj iPhone?" closed="true" %}}
Nakon što pokrenete dijeljenje, Everdisk prikazuje adresu na zaslonu Dijeljenje. Izgleda kao ftp://192.168.1.20:2121. Broj 2121 je port koji Everdisk koristi za FTP, a prvi dio je adresa vašeg iPhonea na Wi-Fi mreži, pa će vaša biti drugačija.
{{% /details %}}

{{% details title="Kako povezati FileZillu ili Cyberduck sa svojim iPhoneom?" closed="true" %}}
Otvorite aplikaciju i stvorite novu vezu. Postavite Host na Wi-Fi adresu vašeg iPhonea, a Port na 2121. Unesite svoju Prijava i Lozinka ili odaberite Anonymous ako je niste postavili u Everdisku. Povežite se i možete povlačiti datoteke u oba smjera kad je Uređivanje datoteka uključeno.
{{% /details %}}

{{% details title="Mogu li se povezati na FTP svog iPhonea s Windowsa?" closed="true" %}}
Da. Otvorite File Explorer, kliknite adresnu traku, upišite FTP adresu iz Everdiska (na primjer ftp://192.168.1.20:2121) i pritisnite Enter. Unesite svoju prijavu ako ste je postavili ili nastavite kao gost. Za prijenose i veću kontrolu umjesto toga koristite FTP aplikaciju poput FileZille.
{{% /details %}}

{{% details title="Trebam li prijavu za FTP?" closed="true" %}}
Ne, prijava je neobvezna. Ostavite Prijava i Lozinka prazne u Postavke, Dijeljenje, Pristup i povežite se kao Anonymous, što većina FTP klijenata nudi. Postavite prijavu ako želite da se veze prvo prijave.
{{% /details %}}

{{% details title="Zašto mogu samo preuzimati, a ne i prenositi putem FTP-a?" closed="true" %}}
Dva su razloga uobičajena. Prvo, preklopnik Uređivanje datoteka u Postavke, Dijeljenje, Pristup mora biti uključen da bi se dopustili prijenosi, preimenovanja i brisanja. Drugo, Mac Finder otvara FTP samo za čitanje, pa koristite FTP aplikaciju poput FileZille ili Cyberduck kad želite prenositi.
{{% /details %}}

{{% details title="Mogu li koristiti FTP između dva iPhonea?" closed="true" %}}
Da. Pokrenite FTP poslužitelj na prvom iPhoneu. Na drugom otvorite Everdisk, idite na karticu Uređaji, dodirnite Nova veza, odaberite FTP i unesite adresu prikazanu na prvom telefonu. Radi i namjenska FTP aplikacija za iOS jer iOS aplikacija Datoteke ne uključuje FTP klijent.
{{% /details %}}

{{% details title="Je li FTP siguran?" closed="true" %}}
Obični FTP ne šifrira svoj promet, pa ga tretirajte kao alat za mreže kojima vjerujete, poput svoje kućne Wi-Fi mreže. Na mreži koju ne kontrolirate koristite SMB poslužitelj s uključenim Zahtijevaj SMB šifriranje, koji štiti svaki prijenos.
{{% /details %}}

{{% details title="Koji se uređaji mogu povezati putem FTP-a?" closed="true" %}}
Gotovo sve s FTP klijentom. To uključuje računala s Macom, Windowsom i Linuxom, FTP aplikacije poput FileZille i Cyberducka, Android upravitelje datoteka te hardver poput kamera, pametnih TV-a, usmjerivača, NAS kutija i alata za automatizaciju. Taj širok domet glavni je razlog da odaberete FTP.
{{% /details %}}

{{% details title="Zašto mi je FTP veza prekinuta?" closed="true" %}}
Vaš je iPhone poslužitelj, a iOS pauzira aplikacije koje predugo ostaju u pozadini. Dok je uređaj povezan, držite Everdisk otvorenim na zaslonu i priključite na napajanje za duge prijenose. Provjerite i jesu li oba uređaja i dalje na istoj Wi-Fi mreži.
{{% /details %}}

{{% details title="Je li Everdisk besplatan?" closed="true" %}}
Da, Everdisk je besplatan za preuzimanje, a FTP poslužitelj je uključen. Neobvezna jednokratna Premium kupnja dodaje dodatke poput prilagođenih portova te pretvorbe fotografija i videa. FTP možete postaviti i prenositi datoteke bez plaćanja.
{{% /details %}}

Spremni za isprobati? [Preuzmite Everdisk s App Storea](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) i povežite svoj prvi FTP klijent u nekoliko minuta. Pitanja ili povratne informacije? Pišite nam na **support@everappz.com**.
