---
title: "Kako besplatno dohvatiti metapodatke, ikone i snimke zaslona iz App Storea"
date: 2026-06-13
description: "Vodič korak po korak za dohvaćanje metapodataka, ikone, snimaka zaslona i lokaliziranih App Store podataka bilo koje iOS aplikacije pomoću AppLookup.pro, besplatnog alata u pregledniku koji se temelji na službenom iTunes Search API-ju."
keywords: [
  "metapodaci app store", "dohvati podatke app store", "preuzimanje ikone app store",
  "preuzimanje snimaka zaslona app store", "alat za pretraživanje app store", "itunes search api",
  "izvlačenje metapodataka aplikacije", "metapodaci iOS aplikacije", "besplatni alat app store api",
  "preuzmi ikonu aplikacije visoke rezolucije", "istraživanje konkurencije app store",
  "lokalizirani podaci app store", "pretraga app store po državi", "besplatni alat za aso istraživanje"
]
tags: [
  "Metapodaci App Store", "App Lookup", "iTunes Search API",
  "Preuzimanje Ikone Aplikacije", "Snimke Zaslona Aplikacije", "ASO Istraživanje"
]
sidebar:
  exclude: true
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

## Podaci App Storea u nekoliko sekundi

**Ukratko:** [AppLookup.pro](https://applookup.pro) je besplatan alat koji povlači javne podatke za bilo koju iOS, iPadOS, macOS ili tvOS aplikaciju. Dobivaš naslov, opis, novosti u verziji, verziju, cijenu, ocjene, ikonu aplikacije, snimke zaslona, podržane uređaje i sirovi odgovor iTunes API-ja. Svako polje ima gumb za kopiranje jednim dodirom. Otvori stranicu, zalijepi App Store poveznicu ili upiši ime aplikacije, i podaci su tu.

Koristi ga za:

- **ASO istraživanje.** Pogledaj kako vodeće aplikacije pišu naslove, podnaslove, opise i ključne riječi.
- **Praćenje konkurencije.** Provjeri ažuriranja verzija, ocjene i cijene na različitim tržištima.
- **Preuzimanje materijala.** Spremi službenu ikonu aplikacije i snimke zaslona u punoj veličini u jedan ZIP.
- **Provjere lokalizacije.** Usporedi opis, novosti u verziji i snimke zaslona u više od 40 zemalja App Storea.
- **Testiranje API-ja.** Kopiraj sirovi JSON iTunes Search API-ja izravno u svoj kôd ili Postman.

## Što je AppLookup.pro?

[AppLookup.pro](https://applookup.pro) je besplatan alat za pretraživanje App Storea, koji se izvršava u pregledniku. U cijelosti radi na tvom uređaju. Svaki rezultat dolazi izravno iz Appleovog službenog [iTunes Search API-ja](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html). Bez scrapinga. Bez registracije. Bez praćenja.

### Što dobivaš

- **Pretraga po nazivu aplikacije ili App Store URL-u.** Automatsko dovršavanje prikazuje rezultate uživo dok tipkaš.
- **Više od 40 trgovina po državama.** Prebacuj se između SAD-a, UK-a, Japana, Njemačke, Francuske, Brazila i drugih.
- **Potpuni metapodaci.** Naslov, podnaslov, programer, bundle ID, verzija, cijena, veličina datoteke, ocjene, datum izdanja, dobna oznaka, jezici i podržani uređaji.
- **Materijali visoke rezolucije.** Ikone aplikacija i snimke zaslona za iPhone, iPad, macOS i Apple TV.
- **Skupno preuzimanje ZIP-a.** Zgrabi svaku ikonu ili svaku snimku zaslona u jednoj arhivi.
- **Sirovi JSON iTunes API-ja.** Točan odgovor od Applea, spreman za kopiranje.
- **Gumbi za kopiranje na svakom polju.** Jedan dodir stavlja vrijednost u međuspremnik.

## Kako koristiti AppLookup.pro korak po korak

### Korak 1. Unesi ime aplikacije ili zalijepi App Store URL

Otvori [applookup.pro](https://applookup.pro) i počni tipkati ime aplikacije. Automatsko dovršavanje prikazuje rezultate App Storea uživo dok tipkaš.

Možeš zalijepiti i izravnu App Store poveznicu poput `https://apps.apple.com/us/app/instagram/id389801252` ili samo ID aplikacije. Alat izvlači ID umjesto tebe. Podržava i Googleove redirect URL-ove.

![Unesi ime aplikacije ili App Store URL u AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Korak 2. Dohvati informacije o aplikaciji i preuzmi ikonu

Klikni **Lookup** ili pritisni Enter. Alat poziva službeni iTunes Search API i u manje od sekunde prikazuje ikonu aplikacije, ime programera, ocjenu, verziju i cijenu.

Skrolaj do sekcije **App Icon**. Svaka veličina ikone koju Apple vraća prikazana je kao kartica. Svaka kartica ima:

- **Direct Link.** Otvara sliku pune veličine u novoj kartici.
- **Download.** Sprema datoteku na tvoje računalo.

Koristi **Download All Icons (ZIP)** da uzmeš svaku veličinu ikone u jednoj arhivi. Isto vrijedi i za snimke zaslona: svaka sekcija platforme ima vlastiti gumb **Download All (ZIP)**.

![Preuzmi ikone aplikacije i snimke zaslona s AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Korak 3. Pročitaj detalje o aplikaciji i kopiraj bilo koje polje

Skrolaj do **App Details**. Vidjet ćeš bundle ID, verziju, cijenu, veličinu datoteke, minimalni OS, datum izdanja, datum posljednjeg ažuriranja, dobnu oznaku, žanrove, ID-ove žanrova, jezike, prodavača, ID izvođača i ID pjesme.

Dodirni gumb **Copy** na bilo kojoj kartici. Vrijednost ide u međuspremnik i gumb prikazuje zelenu kvačicu 'Copied'.

Isto funkcionira za **Description**, **What's New** i **Supported Devices**. Te sekcije imaju klizač pa možeš pročitati cijeli tekst bez gubljenja mjesta, a gumb Copy stavlja cijelo polje u međuspremnik.

![Pregledaj pune detalje App Storea i kopiraj bilo koje polje jednim dodirom](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Korak 4. Pogledaj sirovi odgovor App Store API-ja

Treba ti točan JSON koji Apple vraća? Skrolaj do **Raw API Response**. Cjeloviti sadržaj iTunes Search API-ja prikazan je u prikazu s klizačem, a na vrhu je gumb **Copy**. Jedan dodir kopira cijeli JSON objekt.

**iTunes Lookup URL** prikazan je odmah iznad. Zalijepi ga u Postman, curl ili svoj preglednik da ponoviš isti zahtjev.

![Pregledaj i kopiraj sirovi JSON odgovor iTunes Search API-ja](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Korak 5. Promijeni državu da vidiš lokaliziranu verziju

Metapodaci App Storea mijenjaju se po državama. Ista aplikacija često ima drugačiji naslov, podnaslov, opis, snimke zaslona i cijenu na svakom tržištu.

Odaberi državu iz padajućeg izbornika na vrhu. URL u polju za unos ažurira se automatski. Klikni ponovno **Lookup** da ponovno dohvatiš aplikaciju za to tržište.

Ovo je najbrži način da provjeriš kako konkurent predstavlja svoju aplikaciju u Japanu, Njemačkoj, Brazilu ili bilo kojoj od više od 40 podržanih zemalja.

![Promijeni trgovinu po državi da vidiš lokalizirane App Store metapodatke](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Korak 6. Kopiraj lokalizirane metapodatke

Kada se rezultat za državu učita, svako polje radi na isti način. Dodirni **Copy** na opisu, novostima u verziji, nazivu aplikacije, programeru, bundle ID-u ili bilo kojoj kartici detalja da zabilježiš lokalizirani tekst.

To olakšava izradu tablica usporedbe rame uz rame ili slanje lokaliziranog teksta u pregled prijevoda.

![Kopiraj lokalizirani opis i metapodatke App Storea jednim dodirom](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Tko koristi AppLookup.pro

- **Indie programeri** koji rade ASO istraživanje prije lansiranja.
- **ASO i marketinški timovi** koji prate ažuriranja i cijene konkurencije.
- **Dizajneri** koji uzimaju službenu ikonu aplikacije visoke rezolucije i snimke zaslona za press kitove i studije slučaja.
- **Lokalizacijski timovi** koji provjeravaju koja su tržišta pokrivena i gdje se još uvijek isporučuje engleski tekst.
- **Backend i QA inženjeri** koji testiraju integracije iTunes Search API-ja bez pisanja scrapera.
- **Pisci i blogeri** kojima treba službena ikona aplikacije i nekoliko snimaka zaslona za objavu.

## Privatnost i odricanje od odgovornosti

AppLookup.pro radi u tvom pregledniku. Nema prijave. Nema praćenja. Nema serverskog bilježenja aplikacija koje tražiš. Zahtjevi idu izravno iz tvog preglednika u Appleov [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html).

Ovaj alat je **samo u edukativne i istraživačke svrhe**. Svi podaci dohvaćeni su iz Appleovog službenog javnog API-ja i ostaju vlasništvo tvrtke Apple Inc. i navedenih izdavača aplikacija. Korištenje alata podliježe [Apple Media Services uvjetima](https://www.apple.com/legal/internet-services/terms/site.html). Molimo poštuj Appleova ograničenja stope i nemoj distribuirati materijale zaštićene autorskim pravima.

## Isprobaj odmah

Ne treba ti API ključ, programerski račun ni plaćeni plan da bi pregledao podatke App Storea. Otvori [applookup.pro](https://applookup.pro), zalijepi bilo koji App Store URL i u nekoliko sekundi imat ćeš metapodatke, ikone i sirovi JSON.

## Otvoreni kôd

AppLookup.pro je otvorenog koda. Prijave bugova, dodavanje zemalja i pull requestovi su dobrodošli.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro na GitHubu" icon="github" tag="otvoreni kôd" >}}
{{< /cards >}}

---

## Često postavljana pitanja

{{% details title="Je li AppLookup.pro stvarno besplatan?" closed="true" %}}
Da. AppLookup.pro je 100 posto besplatan i otvorenog koda. Radi u tvom pregledniku. Nema registracije, plaćenih razina ni ograničenja korištenja, izvan vlastitih ograničenja iTunes Search API-ja Applea.
{{% /details %}}

{{% details title="Odakle dolaze podaci?" closed="true" %}}
Svaki rezultat dohvaća se u stvarnom vremenu iz Appleovog službenog [iTunes Search API-ja](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html). Alat ne scrape-a App Store stranice i ne sprema odgovore na nijednom poslužitelju.
{{% /details %}}

{{% details title="Mogu li preuzeti ikonu aplikacije u visokoj rezoluciji?" closed="true" %}}
Da. Sekcija **App Icon** prikazuje svaki URL ikone koji Apple vraća. Svaka kartica ima Direct Link i gumb Download, a gumb Download All Icons ZIP pakira ih sve u jednu arhivu.
{{% /details %}}

{{% details title="Mogu li preuzeti sve snimke zaslona App Storea odjednom?" closed="true" %}}
Da. Svaka sekcija snimaka zaslona (iPhone, iPad, macOS i Apple TV) ima gumb **Download All (ZIP)** koji pakira svaku snimku zaslona u punoj rezoluciji.
{{% /details %}}

{{% details title="Kako mogu vidjeti kako aplikacija izgleda u drugoj državi?" closed="true" %}}
Odaberi državu u padajućem izborniku na vrhu stranice. Podržano je više od 40 trgovina. Klikni ponovno **Lookup** i alat ponovno dohvaća aplikaciju za tu državu, prikazujući lokalizirani naslov, opis, snimke zaslona, novosti u verziji i cijenu.
{{% /details %}}

{{% details title="Mogu li kopirati pojedinačna polja poput bundle ID-a ili datuma izdanja?" closed="true" %}}
Da. Svako tekstualno polje u rezultatu ima vlastiti gumb Copy: naziv aplikacije, programer, opis, novosti u verziji, bundle ID, verzija, cijena, veličina datoteke, minimalni OS, datum izdanja, dobna oznaka, jezici, podržani uređaji i sirovi JSON.
{{% /details %}}

{{% details title="Radi li AppLookup.pro za bilo koju iOS aplikaciju?" closed="true" %}}
Radi za bilo koju aplikaciju koja je javno navedena u najmanje jednoj državi App Storea i koju vraća iTunes Search API. Aplikacije koje nisu navedene, koje su uklonjene ili distribuirane putem enterprise kanala neće se pojaviti.
{{% /details %}}

{{% details title="Podržava li macOS i Apple TV aplikacije?" closed="true" %}}
Da. Ako aplikacija ima snimke zaslona za macOS ili Apple TV u odgovoru iTunes Search API-ja, AppLookup.pro ih prikazuje u zasebnom panelu s klizačem i gumbima za preuzimanje.
{{% /details %}}

{{% details title="Mogu li koristiti sirovi JSON u vlastitom kodu?" closed="true" %}}
Da. Sekcija Raw API Response prikazuje točan JSON koji Apple vraća. Kopiraj ga u Postman, jedinični test ili backend pipeline. Molimo poštuj Appleove API uvjete i razumna ograničenja stope.
{{% /details %}}

{{% details title="Je li sigurno lijepiti App Store URL-ove u alat?" closed="true" %}}
Da. URL se analizira u tvom pregledniku. Jedini izlazni mrežni poziv je pretraživanje Appleovog iTunes Search API-ja.
{{% /details %}}

{{% details title="Koja je razlika između AppLookup.pro i AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) služi za čitanje metapodataka App Storea bilo koje objavljene aplikacije: istraživanje konkurencije, preuzimanje materijala, provjere lokalizacije. [AppKeywords.pro](https://appkeywords.pro) služi za pisanje metapodataka App Storea za tvoju aplikaciju: optimizacija naslova, podnaslova i ključnih riječi uz Fastlane podršku. Ta dva alata dobro rade zajedno.
{{% /details %}}
