---
title: "Hogyan kérjük le ingyen az App Store metaadatait, ikonjait és képernyőképeit"
date: 2026-06-13
description: "Lépésről lépésre útmutató bármely iOS alkalmazás metaadatainak, ikonjának, képernyőképeinek és lokalizált App Store adatainak lekéréséhez az AppLookup.pro segítségével, amely egy ingyenes böngészős eszköz, hivatalos iTunes Search API alapokon."
keywords: [
  "app store metaadatok", "app store adatok lekérése", "app store ikon letöltés",
  "app store képernyőképek letöltése", "app store kereső eszköz", "itunes search api",
  "app metaadat kinyerő", "iOS app metaadatok", "app store api ingyenes eszköz",
  "alkalmazás ikon letöltés nagy felbontásban", "app store versenytárs kutatás",
  "lokalizált app store adatok", "app store ország kereső", "ingyenes aso kutatási eszköz"
]
tags: [
  "App Store Metaadatok", "App Lookup", "iTunes Search API",
  "App Ikon Letöltés", "App Képernyőképek", "ASO Kutatás"
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

## App Store adatok másodpercek alatt

**Röviden:** Az [AppLookup.pro](https://applookup.pro) egy ingyenes eszköz, amely bármely iOS, iPadOS, macOS vagy tvOS alkalmazás nyilvános adatait lekéri. Megkapod a címet, a leírást, az újdonságokat, a verziót, az árat, az értékeléseket, az alkalmazásikont, a képernyőképeket, a támogatott eszközöket és a nyers iTunes API választ. Minden mezőhöz egyérintéses másoló gomb tartozik. Nyisd meg az oldalt, illessz be egy App Store linket vagy írd be az alkalmazás nevét, és máris a kezedben vannak az adatok.

Használd ezekre:

- **ASO kutatás.** Nézd meg, hogyan írják a top alkalmazások a címüket, alcímüket, leírásukat és kulcsszavaikat.
- **Versenytárs követés.** Ellenőrizd a verziófrissítéseket, értékeléseket és árakat különböző piacokon.
- **Anyagok letöltése.** Mentsd el a hivatalos alkalmazásikont és a teljes méretű képernyőképeket egy ZIP fájlban.
- **Lokalizáció ellenőrzése.** Hasonlíts össze leírást, újdonságokat és képernyőképeket több mint 40 App Store országban.
- **API tesztelés.** Másold be az iTunes Search API nyers JSON válaszát közvetlenül a kódodba vagy a Postmanbe.

## Mi az az AppLookup.pro?

Az [AppLookup.pro](https://applookup.pro) egy ingyenes, böngésző alapú App Store kereső eszköz. Teljesen az eszközödön fut. Minden eredmény közvetlenül az Apple hivatalos [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) felületéről érkezik. Nincs scraping. Nincs regisztráció. Nincs nyomon követés.

### Mit kapsz

- **Keresés alkalmazás név vagy App Store URL alapján.** Az automatikus kiegészítés élő eredményeket mutat gépelés közben.
- **Több mint 40 ország bolt.** Válthatsz az USA, Egyesült Királyság, Japán, Németország, Franciaország, Brazília és további boltok között.
- **Teljes metaadat.** Cím, alcím, fejlesztő, bundle ID, verzió, ár, fájlméret, értékelések, kiadási dátum, korhatár besorolás, nyelvek és támogatott eszközök.
- **Nagy felbontású anyagok.** Alkalmazás ikonok és képernyőképek iPhone, iPad, macOS és Apple TV készülékekhez.
- **Tömeges ZIP letöltés.** Töltsd le az összes ikont vagy képernyőképet egyetlen archívumba.
- **Nyers iTunes API JSON.** Az Apple pontos válasza, készen áll a másolásra.
- **Másoló gomb minden mezőn.** Egy érintéssel a vágólapra kerül az érték.

## Hogyan használd az AppLookup.pro-t lépésről lépésre

### 1. lépés. Add meg az alkalmazás nevét vagy illessz be egy App Store URL-t

Nyisd meg az [applookup.pro](https://applookup.pro) oldalt, és kezdd el gépelni az alkalmazás nevét. Az automatikus kiegészítés élő App Store eredményeket mutat gépelés közben.

Beilleszthetsz közvetlen App Store linket is, mint például `https://apps.apple.com/us/app/instagram/id389801252` vagy csak az alkalmazás ID-t. Az eszköz kivonja az ID-t neked. A Google átirányító URL-eket is kezeli.

![Alkalmazás név vagy App Store URL beírása az AppLookup.pro oldalon](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### 2. lépés. Kérd le az alkalmazás adatait és töltsd le az ikont

Kattints a **Lookup** gombra, vagy nyomj Enter-t. Az eszköz meghívja a hivatalos iTunes Search API-t, és egy másodpercen belül megjeleníti az alkalmazás ikonját, a fejlesztő nevét, az értékelést, a verziót és az árat.

Görgess az **App Icon** szekcióhoz. Minden Apple által visszaadott ikonméret kártyaként jelenik meg. Minden kártyán van:

- **Direct Link.** Megnyitja a teljes méretű képet új lapon.
- **Download.** Elmenti a fájlt a számítógépedre.

Használd a **Download All Icons (ZIP)** gombot, hogy az összes ikonméretet egyetlen archívumban szerezd meg. Ugyanez igaz a képernyőképekre is: minden platform szekcióban van saját **Download All (ZIP)** gomb.

![Alkalmazás ikonok és képernyőképek letöltése az AppLookup.pro oldalról](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### 3. lépés. Olvasd el az alkalmazás részleteit és másolj át bármilyen mezőt

Görgess az **App Details** részhez. Látni fogod a bundle ID-t, verziót, árat, fájlméretet, minimum OS-t, kiadási dátumot, utolsó frissítés dátumát, korhatár besorolást, kategóriákat, kategória ID-kat, nyelveket, eladót, művész ID-t és track ID-t.

Érintsd meg a **Copy** gombot bármelyik kártyán. Az érték a vágólapra kerül, és a gombon zöld 'Copied' pipa jelenik meg.

Ugyanez működik a **Description**, **What's New** és **Supported Devices** szekciókhoz. Ezek a részek görgethetők, így elolvashatod a teljes szöveget anélkül, hogy elveszítenéd a helyed, és a Copy gomb az egész mezőt a vágólapra teszi.

![Teljes App Store részletek megtekintése és bármely mező egyérintéses másolása](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### 4. lépés. Tekintsd meg a nyers App Store API választ

Szükséged van az Apple által visszaadott pontos JSON-ra? Görgess a **Raw API Response** részhez. A teljes iTunes Search API tartalom görgethető nézegetőben jelenik meg, a tetején **Copy** gombbal. Egy érintés átmásolja az egész JSON objektumot.

Az **iTunes Lookup URL** közvetlenül felette látható. Illeszd be a Postmanbe, curlbe vagy a böngésződbe, hogy ugyanazt a kérést újra lejátsszad.

![A nyers iTunes Search API JSON válasz megtekintése és másolása](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### 5. lépés. Változtasd meg az országot a lokalizált verzió megtekintéséhez

Az App Store metaadatok országonként változnak. Ugyanaz az alkalmazás gyakran eltérő címmel, alcímmel, leírással, képernyőképekkel és árral szerepel minden piacon.

Válassz országot a tetején lévő legördülő menüből. A bemeneti mezőben lévő URL automatikusan frissül. Kattints újra a **Lookup** gombra, hogy az alkalmazást újra lekérd az adott piacon.

Ez a leggyorsabb módja annak, hogy ellenőrizd, hogyan mutatja be egy versenytárs az alkalmazását Japánban, Németországban, Brazíliában vagy bármelyik a több mint 40 támogatott országban.

![Boltok váltása országonként a lokalizált App Store metaadatok megtekintéséhez](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### 6. lépés. Másold a lokalizált metaadatokat

Miután az ország eredménye betöltődött, minden mező ugyanúgy működik. Érintsd meg a **Copy** gombot a leíráson, az újdonságokon, az alkalmazás nevén, a fejlesztőn, a bundle ID-n vagy bármelyik részletkártyán, hogy elmentsd a lokalizált szöveget.

Ez megkönnyíti az egymás melletti összehasonlító táblázatok készítését, vagy a lokalizált szövegek átadását fordítási ellenőrzésre.

![Lokalizált App Store leírás és metaadatok egyérintéses másolása](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Kik használják az AppLookup.pro-t

- **Indie fejlesztők**, akik ASO kutatást végeznek egy bevezetés előtt.
- **ASO és marketing csapatok**, akik követik a versenytársak frissítéseit és árazását.
- **Tervezők**, akik a hivatalos nagy felbontású alkalmazás ikont és képernyőképeket veszik át sajtóanyagokhoz és esettanulmányokhoz.
- **Lokalizációs csapatok**, akik auditálják, mely piacok fedettek, és hol fut még az alapértelmezett angol szöveg.
- **Backend és QA mérnökök**, akik iTunes Search API integrációkat tesztelnek scraper írása nélkül.
- **Írók és bloggerek**, akiknek szükségük van a hivatalos alkalmazás ikonra és néhány képernyőképre egy bejegyzéshez.

## Adatvédelem és jogi nyilatkozat

Az AppLookup.pro a böngésződben fut. Nincs bejelentkezés. Nincs nyomon követés. Nincs szerveroldali naplózás arról, milyen alkalmazásokat keresel. A kérések közvetlenül a böngésződből az Apple [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) felületére mennek.

Ez az eszköz **kizárólag oktatási és kutatási célokat** szolgál. Minden adat az Apple hivatalos nyilvános API-jából származik, és az Apple Inc. valamint a felsorolt alkalmazás kiadók tulajdonát képezi. Az eszköz használata az [Apple Media Services Terms and Conditions](https://www.apple.com/legal/internet-services/terms/site.html) feltételeinek megfelelően történik. Tartsd tiszteletben az Apple sebességkorlátait, és ne terjeszd újra a szerzői jogi védelem alatt álló anyagokat.

## Próbáld ki most

Nincs szükséged API kulcsra, fejlesztői fiókra vagy fizetős csomagra ahhoz, hogy App Store adatokat vizsgálj. Nyisd meg az [applookup.pro](https://applookup.pro) oldalt, illessz be bármilyen App Store URL-t, és másodperceken belül a kezedben lesznek a metaadatok, ikonok és a nyers JSON.

## Nyílt forráskódú

Az AppLookup.pro nyílt forráskódú. Hibajelentések, országbővítések és pull requestek szívesen láttak.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro a GitHubon" icon="github" tag="nyílt forráskódú" >}}
{{< /cards >}}

---

## Gyakran ismételt kérdések

{{% details title="Tényleg ingyenes az AppLookup.pro?" closed="true" %}}
Igen. Az AppLookup.pro 100 százalékban ingyenes és nyílt forráskódú. A böngésződben fut. Nincs regisztráció, nincs fizetős csomag és nincs használati korlát az Apple saját iTunes Search API korlátain túl.
{{% /details %}}

{{% details title="Honnan jönnek az adatok?" closed="true" %}}
Minden eredmény valós időben érkezik az Apple hivatalos [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) felületéről. Az eszköz nem scrapel App Store oldalakat, és nem gyorsítótáraz válaszokat semmilyen szerveren.
{{% /details %}}

{{% details title="Letölthetem az alkalmazás ikont nagy felbontásban?" closed="true" %}}
Igen. Az **App Icon** szekció megjelenít minden ikon URL-t, amit az Apple visszaad. Minden kártyán van Direct Link és Download gomb, plusz egy Download All Icons ZIP gomb mindet egyetlen archívumba csomagolja.
{{% /details %}}

{{% details title="Letölthetem az összes App Store képernyőképet egyszerre?" closed="true" %}}
Igen. Minden képernyőkép szekció (iPhone, iPad, macOS és Apple TV) tartalmaz egy **Download All (ZIP)** gombot, amely minden képernyőképet teljes felbontásban összecsomagol.
{{% /details %}}

{{% details title="Hogyan látom, hogy néz ki egy alkalmazás másik országban?" closed="true" %}}
Válassz országot az oldal tetején lévő legördülő menüben. Több mint 40 bolt támogatott. Kattints újra a **Lookup** gombra, és az eszköz újra lekéri az alkalmazást abban az országban, megjelenítve a lokalizált címet, leírást, képernyőképeket, újdonságokat és árat.
{{% /details %}}

{{% details title="Másolhatok egyetlen mezőket, mint a bundle ID vagy a kiadási dátum?" closed="true" %}}
Igen. Az eredményben minden szöveges mezőnek saját Copy gombja van: alkalmazás név, fejlesztő, leírás, újdonságok, bundle ID, verzió, ár, fájlméret, minimum OS, kiadási dátum, korhatár besorolás, nyelvek, támogatott eszközök és nyers JSON.
{{% /details %}}

{{% details title="Működik az AppLookup.pro bármely iOS alkalmazáshoz?" closed="true" %}}
Bármely olyan alkalmazáshoz működik, amely legalább egy App Store országban nyilvánosan elérhető, és amelyet az iTunes Search API visszaad. Nem listázott, eltávolított vagy enterprise terjesztésű alkalmazások nem jelennek meg.
{{% /details %}}

{{% details title="Támogatja a macOS és Apple TV alkalmazásokat?" closed="true" %}}
Igen. Ha az alkalmazás macOS vagy Apple TV képernyőképekkel rendelkezik az iTunes Search API válaszában, az AppLookup.pro megjeleníti őket saját görgethető panelben, letöltő gombokkal.
{{% /details %}}

{{% details title="Felhasználhatom a nyers JSON-t a saját kódomban?" closed="true" %}}
Igen. A Raw API Response szekció megjeleníti az Apple által visszaadott pontos JSON-t. Másold át Postmanbe, egy unit tesztbe vagy egy backend pipeline-ba. Tartsd tiszteletben az Apple API feltételeit és az ésszerű sebességkorlátokat.
{{% /details %}}

{{% details title="Biztonságos App Store URL-eket beilleszteni az eszközbe?" closed="true" %}}
Igen. Az URL a böngésződben kerül feldolgozásra. Az egyetlen kimenő hálózati hívás az Apple iTunes Search API felé történő lekérés.
{{% /details %}}

{{% details title="Mi a különbség az AppLookup.pro és az AppKeywords.pro között?" closed="true" %}}
Az [AppLookup.pro](https://applookup.pro) bármely megjelent alkalmazás App Store metaadatainak olvasására szolgál: versenytárs kutatás, anyagok letöltése, lokalizáció ellenőrzése. Az [AppKeywords.pro](https://appkeywords.pro) a saját alkalmazásod App Store metaadatainak megírására szolgál: cím, alcím és kulcsszó optimalizálás Fastlane támogatással. A két eszköz jól kiegészíti egymást.
{{% /details %}}
