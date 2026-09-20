---
title: "Kako postaviti SMB poslužitelj na iPhoneu i iPadu za dijeljenje datoteka"
description: "Pretvorite iPhone ili iPad u SMB poslužitelj datoteka uz Everdisk i otvorite ga poput mrežnog diska s Maca, drugog iPhonea, Linuxa ili Androida putem Wi-Fi. Cjelovito postavljanje, smb adresa i port, neobvezno SMB3 šifriranje te povezivanje korak po korak za svaki uređaj."
date: 2026-09-19
tags: ["everdisk", "smb", "dijeljenje datoteka", "mrežni disk", "iphone", "ipad", "mac", "finder", "šifriranje", "wifi"]
keywords: ["SMB poslužitelj iPhone", "SMB poslužitelj iPad", "kako postaviti SMB na iPhoneu", "iPhone SMB dijeljenje", "povezivanje iPhone SMB Mac Finder", "smb iphone na iphone", "iOS aplikacija Datoteke povezivanje na poslužitelj SMB", "dijeljenje datoteka iPhone SMB", "iphone mrežni disk Finder", "SMB3 šifriranje iOS", "smb dijeljenje iPhone Android", "povezivanje na SMB s Linuxa", "iphone kao mrežni disk", "dijeljenje datoteka između iphonea wifi", "mapiranje iphonea kao mrežnog diska"]
readingTime: 10
---

{{< author-byline >}}

SMB je dijeljenje datoteka ugrađeno u macOS, Windows i Linux te u gotovo svaki mrežni disk (NAS). Kada se povežete na dijeljenu mapu na drugom računalu i ona se otvori poput običnog diska u Finderu ili File Exploreru, to SMB obavlja posao. Uz [Everdisk](/products/everdisk) možete postaviti SMB dijeljenje na svoj iPhone ili iPad, pa se sam telefon pojavljuje kao mrežni disk koji drugi uređaji pregledavaju, s kojeg kopiraju i na koji kopiraju.

Ovo je opcija za koju posegnuti kada želite da se vaš iPhone ponaša kao pravi disk, a ne web stranica. Brz je, povlači i ispušta u oba smjera i jedina je vrsta veze u Everdisku koja može šifrirati svaki prijenos. Ovaj vodič pokriva postavljanje i povezivanje s Maca, drugog iPhonea ili iPada, Linuxa, Androida i Windowsa.

## Što vam je potrebno

- iPhone ili iPad s instaliranim [Everdiskom](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Drugi uređaj na **istoj Wi-Fi mreži**.
- Datoteke koje želite dijeliti, u Everdiskovoj mapi Dokumenti ili u mapama koje dodate.

## Postavite SMB poslužitelj u Everdisku

### Korak 1: Odaberite što dijeliti i tko može pisati

Otvorite Everdisk, idite na karticu **Dijeljenje** i dodirnite **Što dijeliti**. Mapa Dokumenti dijeli se prema zadanim postavkama. Dodajte još pomoću **Dodaj mapu** i **Dodaj datoteku** te uključite svoju biblioteku Fotografija ili Glazbe ako i njih želite učiniti dostupnima.

Odlučite mogu li drugi uređaji samo čitati vaše datoteke ili ih i mijenjati. Otvorite **Postavke**, zatim **Dijeljenje**, pa **Pristup** i postavite **Uređivanje datoteka**. Kad je uključeno, povezani uređaji mogu kopirati datoteke na vaš telefon te ih preimenovati ili brisati. Kad je isključeno, dijeljenje je samo za čitanje.

Ako želite prijavu, postavite **Prijava** i **Lozinka** na istom zaslonu Pristup. Ostavite oboje prazno kako biste dopustili gostujući pristup.

### Korak 2: Uključite SMB poslužitelj

Idite na **Postavke**, zatim **Dijeljenje**, pa **Veze** i uključite **Računalo (napredno)**. To je SMB poslužitelj (nosi oznaku SMB).

### Korak 3: Pokrenite dijeljenje i zabilježite adresu

Vratite se na karticu **Dijeljenje** i dodirnite **Start**. Odjeljak **Kako se povezati** sada prikazuje SMB adresu. Izgleda ovako:

```
smb://192.168.1.20:4455/Share
```

Tri stvari koje treba znati o toj adresi:

- Broj iza dvotočke je **port**. Everdisk prema zadanim postavkama koristi **4455**.
- Dijeljeni resurs zove se **Share**.
- Prvi dio je adresa vašeg iPhonea na Wi-Fi mreži, pa će na vašoj mreži biti drugačija.

Držite Everdisk otvorenim dok su uređaji povezani jer iOS pauzira aplikacije koje predugo stoje u pozadini.

## Povezivanje s Maca

Ovo je najlakši slučaj jer macOS govori SMB izvorno.

Najbrži način: otvorite **Finder** i pogledajte u bočnoj traci pod **Locations** ili **Network**. Everdisk se najavljuje na Wi-Fi mreži, pa se vaš iPhone ondje često pojavljuje sam. Kliknite na njega, zatim kliknite **Connect As** i odaberite **Guest** ili unesite svoju prijavu.

Za ručno povezivanje:

1. U Finderu odaberite **Go**, zatim **Connect to Server** (ili pritisnite **Command i K**).
2. Upišite SMB adresu prikazanu u Everdisku, na primjer `smb://192.168.1.20:4455/Share`.
3. Kliknite **Connect**, zatim odaberite **Guest** ili unesite svoju **Prijava** i **Lozinka**.

Vaš se iPhone otvara u prozoru Findera. Kopirajte datoteke unutra ili van povlačenjem, baš kao i bilo koji drugi disk (ako je Uređivanje datoteka uključeno).

## Povezivanje s drugog iPhonea ili iPada

iOS i iPadOS mogu otvarati SMB dijeljenja u ugrađenoj aplikaciji **Datoteke**, što prijenose s telefona na telefon čini čistima i brzima.

Na drugom uređaju:

1. Otvorite aplikaciju **Datoteke**.
2. Dodirnite gumb **više** (tri točkice, gore desno na iPhoneu) i odaberite **Connect to Server**.
3. Unesite SMB adresu iz Everdiska, na primjer `smb://192.168.1.20:4455/Share`.
4. Odaberite **Guest** ili **Registered User** i unesite svoju prijavu.
5. Dijeljeni resurs pojavljuje se pod Locations u aplikaciji Datoteke. Pregledavajte i kopirajte u bilo kojem smjeru.

Možete koristiti i Everdiskovu vlastitu karticu **Uređaji** na drugom uređaju, koja uključuje SMB klijent. Otvorite Everdisk, idite na **Uređaji**, dodirnite **Nova veza**, odaberite **SMB** i unesite adresu.

## Povezivanje s Linuxa

1. Otvorite svoj upravitelj datoteka (Files/Nautilus na GNOME-u, Dolphin na KDE-u).
2. Odaberite **Other Locations** ili **Connect to Server**.
3. Unesite adresu, na primjer `smb://192.168.1.20:4455/Share`.
4. Povežite se kao gost ili unesite svoju prijavu.

Iz terminala možete pokrenuti i `smbclient //192.168.1.20/Share -p 4455` i unijeti svoju prijavu kad se to zatraži.

## Povezivanje s Androida

Android nema sistemski SMB preglednik, pa koristite upravitelj datoteka koji podržava SMB:

1. Instalirajte aplikaciju poput **CX File Explorer**, **Solid Explorer** ili **X-plore File Manager**.
2. Dodajte novu vezu **SMB** ili **LAN**.
3. Unesite host (Wi-Fi adresu vašeg iPhonea), postavite **port na 4455** i naziv dijeljenog resursa **Share**.
4. Povežite se kao gost ili sa svojom prijavom, zatim pregledavajte i kopirajte.

## Povezivanje s Windowsa

Windows može čitati SMB dijeljenja, uz jednu kvaku koju vrijedi znati unaprijed. Ugrađeni File Explorer razgovara sa SMB-om samo na standardnom portu i ne dopušta upisivanje prilagođenog porta u putanju, a Everdisk koristi port 4455. Zbog toga obični put **Map network drive** često do njega neće doći.

Na Windowsu imate dvije dobre opcije:

- Koristite upravitelj datoteka ili SMB klijent koji dopušta postavljanje prilagođenog porta i usmjerite ga na adresu vašeg iPhonea s portom **4455** i nazivom dijeljenog resursa **Share**.
- Ili se s Windowsa povežite putem jednog od drugih Everdiskovih poslužitelja. [Postavljanje WebDAV-a](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) i [postavljanje FTP-a](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) oba dobro rade iz Windows File Explorera, a poveznica za preglednik radi u bilo kojem pregledniku.

Ako ipak želite isprobati Map network drive: otvorite **File Explorer**, desnom tipkom kliknite **This PC**, odaberite **Map network drive** i unesite host i naziv dijeljenog resursa prikazane u Everdisku. Ako se ne može povezati, to je gornje ograničenje porta, pa prijeđite na WebDAV ili FTP.

## Uključite šifriranje za nepouzdani Wi-Fi

SMB je jedina Everdisk veza koja može šifrirati svaki prijenos, što je važno na Wi-Fi mreži koju ne kontrolirate u potpunosti, poput kafića ili uredske mreže.

1. U **Postavke**, **Dijeljenje**, **Pristup** postavite **Prijava** i **Lozinka**. Šifrirane veze ne mogu biti anonimne, pa je ovaj korak obavezan.
2. U **Postavke**, **Dijeljenje** uključite **Zahtijevaj SMB šifriranje**.
3. Zaustavite i ponovno pokrenite dijeljenje kako bi promjena stupila na snagu.

Svaki je SMB prijenos tada zaštićen **SMB3 šifriranjem (AES)**. Uređaj koji se povezuje mora podržavati SMB3, što i Finder na modernom Macu i Windows 10 ili noviji podržavaju. SMB šifriranje dio je jednokratne Premium kupnje.

## Samo za čitanje ili čitanje i pisanje

Preklopnik **Uređivanje datoteka** u Postavke, Dijeljenje, Pristup kontrolira ovo za svaki poslužitelj, uključujući SMB. Uključite ga i povezani uređaji mogu prenositi, preimenovati i brisati. Isključite ga i mogu samo pregledavati i kopirati datoteke s vašeg telefona. Odaberite samo za čitanje kada nekome predajete datoteke, a ne želite da išta mijenja.

## Načini na koje ljudi ovo koriste u praksi

- **Premjestite veliku mapu na svoj iPhone s Maca** povlačenjem u prozor Findera, brže od web prijenosa.
- **Skinite dan fotografija i videozapisa s telefona** na laptop bez iTunesa ili kabela.
- **Šaljite datoteke između dva iPhonea** putem aplikacije Datoteke, bez treće aplikacije na obje strane.
- **Radite s datotekom na mjestu**, otvarajući dokument izravno s telefona u aplikaciji na Macu i spremajući ga natrag.

## Nekoliko savjeta

- Dok je uređaj povezan, držite Everdisk otvorenim. Zaključavanje telefona na duže vrijeme može pauzirati aplikaciju i prekinuti vezu.
- Ako Mac ne vidi telefon u bočnoj traci Findera, povežite se ručno pomoću Connect to Server i pune smb adrese.
- Za najbolju brzinu velikih prijenosa držite kvalitetu fotografija i videa na Original u Postavkama.
- Na nepouzdanoj mreži uključite Zahtijevaj SMB šifriranje i isključite ostale poslužitelje dok radite.

## Često postavljana pitanja

{{% details title="Koja je SMB adresa i port za moj iPhone?" closed="true" %}}
Nakon što pokrenete dijeljenje, Everdisk prikazuje adresu na zaslonu Dijeljenje. Izgleda kao smb://192.168.1.20:4455/Share. Broj 4455 je port koji Everdisk koristi za SMB, a Share je naziv dijeljene mape. Prvi dio je adresa vašeg iPhonea na Wi-Fi mreži, pa će vaša biti drugačija.
{{% /details %}}

{{% details title="Mogu li se povezati na SMB dijeljenje svog iPhonea s Windowsa?" closed="true" %}}
Windows File Explorer povezuje se sa SMB-om samo na standardnom portu i ne prihvaća prilagođeni port u putanji, dok Everdisk koristi port 4455. Zbog toga obični put Map network drive često do njega neće doći. Koristite upravitelj datoteka koji dopušta postavljanje prilagođenog porta ili se s Windowsa povežite putem WebDAV-a, FTP-a ili poveznice za preglednik. Sve to radi s Windowsa bez ikakvih problema s portom.
{{% /details %}}

{{% details title="Kako dijeliti datoteke između dva iPhonea putem SMB-a?" closed="true" %}}
Pokrenite SMB poslužitelj na prvom iPhoneu u Everdisku. Na drugom iPhoneu otvorite aplikaciju Datoteke, dodirnite gumb više, odaberite Connect to Server i unesite smb adresu prikazanu u Everdisku (na primjer smb://192.168.1.20:4455/Share). Povežite se kao Guest ili sa svojom prijavom i dijeljeni se resurs pojavljuje u aplikaciji Datoteke. Možete koristiti i Everdiskovu vlastitu karticu Uređaji na drugom telefonu.
{{% /details %}}

{{% details title="Pojavljuje li se moj iPhone u bočnoj traci Mac Findera automatski?" closed="true" %}}
Obično da. Everdisk najavljuje SMB dijeljenje na vašoj Wi-Fi mreži, pa se vaš iPhone često pojavljuje pod Locations ili Network u bočnoj traci Findera. Kliknite na njega i odaberite Connect As, zatim Guest ili svoju prijavu. Ako se ne pojavi, povežite se ručno pomoću Go, Connect to Server i pune smb adrese.
{{% /details %}}

{{% details title="Trebam li lozinku za korištenje SMB-a?" closed="true" %}}
Ne, prijava je neobvezna. Ostavite Prijava i Lozinka prazne u Postavke, Dijeljenje, Pristup kako biste dopustili gostujući pristup. Postavite ih ako želite da se veze prijavljuju. Prijava i lozinka obavezne su samo ako uključite Zahtijevaj SMB šifriranje jer šifrirane veze ne mogu biti anonimne.
{{% /details %}}

{{% details title="Je li SMB veza šifrirana?" closed="true" %}}
Može biti. SMB je jedina Everdisk veza koja podržava šifriranje. Postavite prijavu i lozinku, zatim uključite Zahtijevaj SMB šifriranje u Postavke, Dijeljenje. Svaki je prijenos tada zaštićen SMB3 (AES). Drugi uređaj mora podržavati SMB3, što moderni Macovi i Windows 10 ili noviji podržavaju. Šifriranje je Premium značajka.
{{% /details %}}

{{% details title="Mogu li ljudi mijenjati ili brisati moje datoteke putem SMB-a?" closed="true" %}}
Samo ako to dopustite. Preklopnik Uređivanje datoteka u Postavke, Dijeljenje, Pristup kontrolira ovo. Kad je uključeno, povezani uređaji mogu prenositi, preimenovati i brisati. Kad je isključeno, dijeljenje je samo za čitanje i drugi mogu pregledavati i kopirati datoteke s vašeg telefona, ali ništa ne mogu mijenjati.
{{% /details %}}

{{% details title="Zašto mi je SMB veza prekinuta?" closed="true" %}}
Vaš je iPhone poslužitelj, a iOS pauzira aplikacije koje predugo ostaju u pozadini. Dok je uređaj povezan, držite Everdisk otvorenim na zaslonu i priključite telefon na napajanje tijekom dugih prijenosa. Provjerite i jesu li oba uređaja ostala na istoj Wi-Fi mreži.
{{% /details %}}

{{% details title="SMB, WebDAV ili FTP, koji odabrati?" closed="true" %}}
Koristite SMB kad želite da se telefon ponaša kao pravi mrežni disk na Macu, drugom iPhoneu, Linuxu ili NAS-u te kad želite šifriranje. Koristite WebDAV kad želite mrežni disk koji dobro radi i s Windowsa. Koristite FTP za najširu kompatibilnost sa starijim uređajima i aplikacijama. Everdisk može pokretati sve njih odjednom, pa niste ograničeni na jedan.
{{% /details %}}

{{% details title="Je li Everdisk besplatan?" closed="true" %}}
Da, Everdisk je besplatan za preuzimanje, a SMB poslužitelj je uključen. Neobvezna jednokratna Premium kupnja dodaje SMB šifriranje, prilagođene portove i još nekoliko dodataka. SMB možete postaviti i dijeliti datoteke bez plaćanja.
{{% /details %}}

Spremni za isprobati? [Preuzmite Everdisk s App Storea](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) i otvorite svoj iPhone u Finderu za otprilike minutu. Pitanja ili povratne informacije? Pišite nam na **support@everappz.com**.
