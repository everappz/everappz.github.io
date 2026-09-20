---
title: "Kako postaviti WebDAV poslužitelj na iPhoneu i iPadu za pristup i dijeljenje datoteka"
description: "Pretvorite iPhone ili iPad u WebDAV poslužitelj uz Everdisk i povežite ga kao mrežni disk u Mac Finderu, Windows File Exploreru, Linuxu, Androidu ili na drugom iPhoneu putem Wi-Fi. Cjelovito postavljanje, WebDAV adresa i port te povezivanje korak po korak za svaki uređaj."
date: 2026-09-19
tags: ["everdisk", "webdav", "mrežni disk", "dijeljenje datoteka", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["WebDAV poslužitelj iPhone", "WebDAV poslužitelj iPad", "kako postaviti WebDAV na iPhoneu", "povezivanje iPhonea kao mrežnog diska", "povezivanje iPhone WebDAV Mac Finder", "WebDAV Windows File Explorer iPhone", "iphone mrežni disk Windows", "WebDAV Linux iPhone", "pristup datotekama iPhonea s računala", "webdav iphone na iphone", "dijeljenje datoteka iPhone WebDAV", "mapiranje mrežnog diska iphone", "prijenos datoteka iphone webdav", "webdav adresa port iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV pretvara mapu u mrežni disk koji računalo može otvoriti u svom uobičajenom upravitelju datoteka. Radi putem istog web protokola koji vaš preglednik koristi, zbog čega dobro putuje između Maca, Windowsa i Linuxa bez posebnih upravljačkih programa. Uz [Everdisk](/products/everdisk) možete pokrenuti WebDAV poslužitelj na svom iPhoneu ili iPadu, pa se telefon pojavljuje kao disk koji možete pregledavati, s kojeg možete kopirati i na koji možete kopirati s gotovo bilo kojeg računala.

WebDAV je najbolji izbor kada je Windows u igri jer se Windows File Explorer čisto povezuje s njim. Ovaj vodič pokriva postavljanje i povezivanje s Maca, Windowsa, Linuxa, Androida i drugog iPhonea.

## Što vam je potrebno

- iPhone ili iPad s instaliranim [Everdiskom](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Računalo ili drugi uređaj na **istoj Wi-Fi mreži**.
- Datoteke koje želite dijeliti, u Everdiskovoj mapi Dokumenti ili u mapama koje dodate.

## Postavite WebDAV poslužitelj u Everdisku

### Korak 1: Odaberite što dijeliti i postavite pristup

Otvorite Everdisk, idite na karticu **Dijeljenje** i dodirnite **Što dijeliti**. Mapa Dokumenti dijeli se prema zadanim postavkama. Dodajte još pomoću **Dodaj mapu** i **Dodaj datoteku**.

Otvorite **Postavke**, zatim **Dijeljenje**, pa **Pristup**. Uključite **Uređivanje datoteka** ako želite da povezana računala kopiraju datoteke na vaš telefon te ih preimenuju ili brišu, ili isključite za disk samo za čitanje. Postavite **Prijava** i **Lozinka** ovdje ako želite prijavu ili ih ostavite prazne za gostujući pristup.

### Korak 2: Uključite WebDAV poslužitelj

Idite na **Postavke**, zatim **Dijeljenje**, pa **Veze** i uključite **Računalo**. To je WebDAV poslužitelj (nosi oznaku WebDAV).

### Korak 3: Pokrenite dijeljenje i zabilježite adresu

Vratite se na karticu **Dijeljenje** i dodirnite **Start**. Odjeljak **Kako se povezati** prikazuje WebDAV adresu. Izgleda ovako:

```
http://192.168.1.20:8080
```

Broj iza dvotočke je **port**, koji je prema zadanim postavkama **8080**. Prvi dio je adresa vašeg iPhonea na Wi-Fi mreži, pa će se vaša razlikovati. Držite Everdisk otvorenim na zaslonu dok je uređaj povezan.

## Povezivanje s Maca

1. Otvorite **Finder**, odaberite **Go**, zatim **Connect to Server** (ili pritisnite **Command i K**).
2. Upišite WebDAV adresu prikazanu u Everdisku, na primjer `http://192.168.1.20:8080`.
3. Kliknite **Connect**, zatim odaberite **Guest** ili unesite svoju **Prijava** i **Lozinka**.

Vaš se iPhone otvara u prozoru Findera i ponaša se poput obične mape. Kopirajte datoteke u bilo kojem smjeru ako je Uređivanje datoteka uključeno.

## Povezivanje s Windowsa

Windows ima ugrađeni WebDAV klijent, pa ovo radi iz File Explorera.

1. Otvorite **File Explorer**, desnom tipkom kliknite **This PC** u bočnoj traci i odaberite **Add a network location** (možete koristiti i **Map network drive**).
2. Kad se zatraži adresa, upišite istu WebDAV adresu iz Everdiska, na primjer `http://192.168.1.20:8080`, zatim kliknite **Next**.
3. Unesite svoju **Prijava** i **Lozinka** ako ste ih postavili.

Uređaj se zatim pojavljuje pod This PC kao mrežna lokacija koju možete otvoriti i s koje možete kopirati datoteke. Ako se Windows prvi put odbije povezati, provjerite radi li servis **WebClient** (pretražite Services u izborniku Start, pronađite WebClient i postavite ga da se pokrene), zatim pokušajte ponovno.

## Povezivanje s Linuxa

1. Otvorite svoj upravitelj datoteka i odaberite **Connect to Server** ili **Other Locations**.
2. Unesite adresu s WebDAV prefiksom, na primjer `dav://192.168.1.20:8080` (koristite `davs://` samo ako ste postavili TLS).
3. Povežite se kao gost ili unesite svoju prijavu.

## Povezivanje s Androida

Android nema sistemski WebDAV preglednik, pa koristite upravitelj datoteka koji ga podržava:

1. Instalirajte aplikaciju poput **Solid Explorer** ili **CX File Explorer**.
2. Dodajte novu vezu **WebDAV**.
3. Unesite host i **port 8080**, odaberite shemu `http` i dodajte svoju prijavu ako ste je postavili.

## Povezivanje s drugog iPhonea ili iPada

iOS aplikacija Datoteke ne uključuje WebDAV klijent, pa koristite jedno od ovoga:

- **Everdiskovu vlastitu karticu Uređaji.** Na drugom uređaju otvorite Everdisk, idite na **Uređaji**, dodirnite **Nova veza**, odaberite **WebDAV** i unesite adresu, na primjer `http://192.168.1.20:8080`. Ovo je najjednostavniji put i ne treba ništa dodatno.
- **WebDAV aplikaciju** poput Documents by Readdle, koja može dodati WebDAV vezu s istom adresom i prijavom.

## Radije brzu poveznicu umjesto diska?

Ako samo trebate brzo dohvatiti datoteku i uopće ne želite povezivati disk, uključite vezu **Preglednik** u Postavke, Dijeljenje, Veze. Everdisk vam tada daje web adresu koju možete otvoriti u bilo kojem pregledniku na bilo kojem uređaju za pregledavanje i preuzimanje vaših datoteka. To je najbrži način da predate datoteku Windows PC-u, Chromebooku ili telefonu prijatelja.

## Samo za čitanje ili čitanje i pisanje

Preklopnik **Uređivanje datoteka** u Postavke, Dijeljenje, Pristup odlučuje o ovome. Uključeno znači da povezana računala mogu prenositi, preimenovati i brisati. Isključeno znači da je disk samo za čitanje, pa drugi mogu pregledavati i kopirati vaše datoteke, ali ih ne mogu mijenjati.

## Načini na koje ljudi ovo koriste u praksi

- **Kopirajte datoteke na svoj iPhone s Windows PC-a** mapiranjem kao mrežne lokacije i povlačenjem preko.
- **Prebacite fotografije i dokumente na laptop** pomoću upravitelja datoteka koji već poznajete, bez kabela i bez iTunesa.
- **Uredite dokument na mjestu** s Maca, otvarajući ga izravno s telefona i spremajući natrag.
- **Premjestite mapu između iPhonea i iPada** pomoću Everdiskove kartice Uređaji na uređaju koji prima.

## Nekoliko savjeta

- Dok je uređaj povezan, držite Everdisk otvorenim. Zaključavanje telefona na duže vrijeme može pauzirati aplikaciju.
- Na Windowsu, ako veza ne uspije, pokrenite servis WebClient i pokušajte adresu ponovno.
- WebDAV i SMB oba se povezuju kao mrežni diskovi. Koristite WebDAV kad je Windows uključen, a [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) kad želite brzinu Findera i šifriranje.
- Za najbrže prijenose držite kvalitetu fotografija i videa na Original u Postavkama.

## Često postavljana pitanja

{{% details title="Koja je WebDAV adresa i port za moj iPhone?" closed="true" %}}
Nakon što pokrenete dijeljenje, Everdisk prikazuje adresu na zaslonu Dijeljenje. Izgleda kao http://192.168.1.20:8080. Broj 8080 je port koji Everdisk koristi za WebDAV, a prvi dio je adresa vašeg iPhonea na Wi-Fi mreži, pa će vaša biti drugačija.
{{% /details %}}

{{% details title="Kako se povezati na WebDAV svog iPhonea s Windowsa?" closed="true" %}}
Otvorite File Explorer, desnom tipkom kliknite This PC i odaberite Add a network location ili Map network drive. Unesite WebDAV adresu iz Everdiska, na primjer http://192.168.1.20:8080, zatim unesite svoju prijavu ako ste je postavili. Ako se Windows neće povezati, provjerite radi li servis WebClient (pretražite Services, pronađite WebClient, pokrenite ga) i pokušajte ponovno.
{{% /details %}}

{{% details title="Mogu li koristiti WebDAV između dva iPhonea?" closed="true" %}}
Da, ali iOS aplikacija Datoteke nema WebDAV klijent, pa koristite Everdisk na drugom uređaju. Otvorite karticu Uređaji, dodirnite Nova veza, odaberite WebDAV i unesite adresu prikazanu na prvom telefonu. Radi i WebDAV aplikacija poput Documents by Readdle.
{{% /details %}}

{{% details title="Treba li WebDAV lozinku?" closed="true" %}}
Ne, prijava je neobvezna. Ostavite Prijava i Lozinka prazne u Postavke, Dijeljenje, Pristup za gostujući pristup ili ih postavite ako želite da se veze prijavljuju.
{{% /details %}}

{{% details title="Mogu li drugi ljudi mijenjati moje datoteke putem WebDAV-a?" closed="true" %}}
Samo ako to dopustite. Preklopnik Uređivanje datoteka u Postavke, Dijeljenje, Pristup kontrolira ovo. Uključeno omogućuje povezanim uređajima da prenose, preimenuju i brišu. Isključeno čini disk samo za čitanje, pa drugi mogu pregledavati i kopirati, ali ništa ne mogu mijenjati.
{{% /details %}}

{{% details title="WebDAV ili SMB, koja je razlika?" closed="true" %}}
Oba povezuju vaš iPhone kao mrežni disk. WebDAV radi putem web protokola i čisto se povezuje iz Windows File Explorera, što mu je glavna snaga. SMB je izvorno dijeljenje datoteka na Macu, Linuxu i NAS uređajima, obično je brži na Macu i jedina je Everdisk veza koja može šifrirati prijenose. Everdisk može pokretati oba odjednom.
{{% /details %}}

{{% details title="Zašto se moj WebDAV disk odspaja?" closed="true" %}}
Vaš je iPhone poslužitelj, a iOS pauzira aplikacije koje predugo ostaju u pozadini. Dok je uređaj povezan, držite Everdisk otvorenim na zaslonu i priključite na napajanje za duge prijenose. Potvrdite i jesu li oba uređaja i dalje na istoj Wi-Fi mreži.
{{% /details %}}

{{% details title="Mogu li se povezati putem WebDAV-a bez Wi-Fi?" closed="true" %}}
Da, ako priključite svoj iPhone na Mac kabelom. Everdisk tada prikazuje dodatnu adresu za kabelsku vezu koju povezani Mac može otvoriti u Finderu, što radi čak i bez ikakvog Wi-Fi. Preko kabela samo taj Mac može doći do uređaja.
{{% /details %}}

{{% details title="Je li Everdisk besplatan?" closed="true" %}}
Da, Everdisk je besplatan za preuzimanje, a WebDAV poslužitelj je uključen. Neobvezna jednokratna Premium kupnja dodaje dodatke poput prilagođenih portova te pretvorbe fotografija i videa. WebDAV možete postaviti i dijeliti datoteke bez plaćanja.
{{% /details %}}

Spremni za isprobati? [Preuzmite Everdisk s App Storea](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) i povežite svoj iPhone kao disk u nekoliko minuta. Pitanja ili povratne informacije? Pišite nam na **support@everappz.com**.
