---
title: "Cum să preiei gratuit metadatele, pictogramele și capturile de ecran din App Store"
date: 2026-06-13
description: "Ghid pas cu pas pentru preluarea metadatelor, pictogramei, capturilor de ecran și detaliilor localizate din App Store pentru orice aplicație iOS folosind AppLookup.pro, un instrument gratuit de browser bazat pe API-ul oficial iTunes Search."
keywords: [
  "metadate app store", "preluare date app store", "descărcare pictogramă app store",
  "descărcare capturi de ecran app store", "instrument căutare app store", "itunes search api",
  "extractor metadate aplicație", "metadate aplicație iOS", "instrument gratuit api app store",
  "descărcare pictogramă aplicație în rezoluție înaltă", "analiză concurență app store",
  "date localizate app store", "căutare țară app store", "instrument gratuit aso"
]
tags: [
  "Metadate App Store", "Căutare aplicații", "iTunes Search API",
  "Descărcare pictogramă aplicație", "Capturi de ecran aplicații", "Analiză ASO"
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

## Obține date App Store în câteva secunde

**Versiunea scurtă:** [AppLookup.pro](https://applookup.pro) este un instrument gratuit care obține date publice pentru orice aplicație iOS, iPadOS, macOS sau tvOS. Obții titlul, descrierea, noutățile, versiunea, prețul, evaluările, pictograma aplicației, capturile de ecran, dispozitivele acceptate și răspunsul brut iTunes API. Fiecare câmp are un buton de copiere cu o atingere. Deschide site-ul, lipește un link App Store sau tastează numele aplicației și ai datele.

Folosește-l pentru:

- **Cercetare ASO.** Vezi cum scriu aplicațiile de top titlurile, subtitlurile, descrierile și cuvintele cheie.
- **Urmărirea concurenților.** Verifică actualizările de versiuni, evaluările și prețurile pe diferite piețe.
- **Descărcare resurse.** Salvează pictograma oficială a aplicației și capturile de ecran la dimensiune completă într-un singur ZIP.
- **Verificări de localizare.** Compară descrierea, noutățile și capturile de ecran pe peste 40 de țări App Store.
- **Testare API.** Copiază JSON-ul brut iTunes Search API direct în codul tău sau în Postman.

## Ce este AppLookup.pro?

[AppLookup.pro](https://applookup.pro) este un instrument gratuit de căutare în App Store bazat pe browser. Rulează în întregime pe dispozitivul tău. Fiecare rezultat vine direct din [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) oficial de la Apple. Fără scraping. Fără înregistrare. Fără urmărire.

### Ce obții

- **Căutare după numele aplicației sau URL App Store.** Completarea automată afișează rezultate live pe măsură ce tastezi.
- **Peste 40 de magazine pe țări.** Comută între US, UK, JP, DE, FR, BR și altele.
- **Metadate complete.** Titlu, subtitlu, dezvoltator, bundle ID, versiune, preț, dimensiune fișier, evaluări, dată lansare, rating de conținut, limbi și dispozitive acceptate.
- **Resurse în rezoluție înaltă.** Pictograme de aplicație și capturi de ecran pentru iPhone, iPad, macOS și Apple TV.
- **Descărcare ZIP în bloc.** Obține toate pictogramele sau toate capturile de ecran într-o singură arhivă.
- **JSON brut iTunes API.** Răspunsul exact de la Apple, gata de copiat.
- **Butoane de copiere pe fiecare câmp.** O atingere pune valoarea în clipboard.

## Cum să folosești AppLookup.pro pas cu pas

### Pasul 1. Introdu numele aplicației sau lipește un URL App Store

Deschide [applookup.pro](https://applookup.pro) și începe să tastezi numele aplicației. Completarea automată afișează rezultate live App Store pe măsură ce tastezi.

Poți de asemenea să lipești un link direct App Store, precum `https://apps.apple.com/us/app/instagram/id389801252`, sau doar ID-ul aplicației. Instrumentul extrage ID-ul pentru tine. Gestionează și URL-urile de redirecționare Google.

![Introdu un nume de aplicație sau URL App Store în AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Pasul 2. Preia informațiile aplicației și descarcă pictograma

Apasă **Lookup** sau apasă Enter. Instrumentul apelează iTunes Search API oficial și afișează pictograma aplicației, numele dezvoltatorului, evaluarea, versiunea și prețul în mai puțin de o secundă.

Derulează la secțiunea **App Icon**. Fiecare dimensiune de pictogramă pe care o returnează Apple apare ca un card. Fiecare card are:

- **Direct Link.** Deschide imaginea la dimensiune completă într-o filă nouă.
- **Download.** Salvează fișierul pe computerul tău.

Folosește **Download All Icons (ZIP)** pentru a obține fiecare dimensiune de pictogramă într-o singură arhivă. Același lucru este valabil pentru capturile de ecran: fiecare secțiune de platformă are propriul buton **Download All (ZIP)**.

![Descarcă pictograme de aplicație și capturi de ecran din AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Pasul 3. Citește detaliile aplicației și copiază orice câmp

Derulează la **App Details**. Vei vedea bundle ID, versiune, preț, dimensiune fișier, OS minim, dată lansare, dată ultimei actualizări, rating de conținut, genuri, ID-uri de gen, limbi, vânzător, ID artist și ID melodie.

Atinge butonul **Copy** pe orice card. Valoarea merge în clipboard-ul tău și butonul afișează o bifă verde «Copied».

Același lucru funcționează pentru **Description**, **What's New** și **Supported Devices**. Aceste secțiuni sunt derulabile, astfel încât poți citi textul complet fără să-ți pierzi locul, iar butonul Copy pune întregul câmp în clipboard.

![Vizualizează detaliile complete App Store și copiază orice câmp cu o atingere](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Pasul 4. Vizualizează răspunsul API brut App Store

Ai nevoie de JSON-ul exact pe care îl returnează Apple? Derulează la **Raw API Response**. Întreaga încărcătură utilă iTunes Search API este afișată într-un vizualizator derulabil cu un buton **Copy** în partea de sus. O atingere copiază întregul obiect JSON.

**iTunes Lookup URL** este afișat chiar deasupra acestuia. Lipește-l în Postman, curl sau în browserul tău pentru a relua aceeași cerere.

![Vizualizează și copiază răspunsul JSON brut iTunes Search API](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Pasul 5. Schimbă țara pentru a vedea versiunea localizată

Metadatele App Store se schimbă în funcție de țară. Aceeași aplicație are adesea un titlu, subtitlu, descriere, capturi de ecran și preț diferite în fiecare piață.

Alege o țară din meniul derulant din partea de sus. URL-ul din caseta de introducere se actualizează automat. Apasă **Lookup** din nou pentru a relua preluarea aplicației pe acea piață.

Acesta este cel mai rapid mod de a verifica cum își prezintă un concurent aplicația în Japonia, Germania, Brazilia sau în oricare dintre cele peste 40 de țări acceptate.

![Comută magazinele pe țări pentru a vedea metadatele localizate App Store](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Pasul 6. Copiază metadatele localizate

Odată ce rezultatul țării se încarcă, fiecare câmp funcționează în același mod. Atinge **Copy** pe descriere, noutăți, numele aplicației, dezvoltator, bundle ID sau orice card de detalii pentru a captura textul localizat.

Acest lucru face ușoară construirea de foi de calcul de comparație una lângă alta sau alimentarea textului localizat în revizuirea traducerii.

![Copiază descrierea și metadatele localizate App Store cu o atingere](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Cine folosește AppLookup.pro

- **Dezvoltatori independenți** care fac cercetare ASO înainte de o lansare.
- **Echipe ASO și de marketing** care urmăresc actualizările și prețurile concurenței.
- **Designeri** care obțin pictograma oficială a aplicației în rezoluție înaltă și capturi de ecran pentru kituri de presă și studii de caz.
- **Echipe de localizare** care auditează care piețe sunt acoperite și unde textul implicit în engleză este încă livrat.
- **Ingineri backend și QA** care testează integrările iTunes Search API fără a scrie un scraper.
- **Scriitori și bloggeri** care au nevoie de pictograma oficială a aplicației și de câteva capturi de ecran pentru o postare.

## Confidențialitate și declinare a responsabilității

AppLookup.pro rulează în browserul tău. Nu există autentificare. Nu există urmărire. Nu există jurnalizare pe server a aplicațiilor pe care le cauți. Cererile merg direct din browserul tău către [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) de la Apple.

Acest instrument este destinat doar **scopurilor educaționale și de cercetare**. Toate datele sunt preluate din API-ul public oficial Apple și rămân proprietatea Apple Inc. și a editorilor de aplicații listați. Utilizarea instrumentului este supusă [Apple Media Services Terms and Conditions](https://www.apple.com/legal/internet-services/terms/site.html). Te rugăm să respecți limitele de rată Apple și să nu redistribui resurse protejate de drepturi de autor.

## Încearcă acum

Nu ai nevoie de o cheie API, un cont de dezvoltator sau un plan plătit pentru a inspecta datele App Store. Deschide [applookup.pro](https://applookup.pro), lipește orice URL App Store și vei avea metadatele, pictogramele și JSON-ul brut în câteva secunde.

## Open Source

AppLookup.pro este open source. Rapoartele de erori, adăugările de țări și pull request-urile sunt binevenite.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro pe GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Întrebări frecvente

{{% details title="AppLookup.pro este cu adevărat gratuit?" closed="true" %}}
Da. AppLookup.pro este 100 la sută gratuit și open source. Rulează în browserul tău. Nu există înregistrare, nivel plătit sau plafon de utilizare dincolo de propriile limite iTunes Search API ale Apple.
{{% /details %}}

{{% details title="De unde provin datele?" closed="true" %}}
Fiecare rezultat este preluat în timp real din [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) oficial de la Apple. Instrumentul nu face scraping pe paginile App Store și nu memorează răspunsurile în cache pe niciun server.
{{% /details %}}

{{% details title="Pot descărca pictograma aplicației în rezoluție înaltă?" closed="true" %}}
Da. Secțiunea **App Icon** afișează fiecare URL de pictogramă pe care Apple îl returnează. Fiecare card are un Direct Link și un buton Download, iar un buton Download All Icons ZIP le împachetează într-o singură arhivă.
{{% /details %}}

{{% details title="Pot descărca toate capturile de ecran App Store deodată?" closed="true" %}}
Da. Fiecare secțiune de capturi de ecran (iPhone, iPad, macOS și Apple TV) are un buton **Download All (ZIP)** care grupează fiecare captură de ecran la rezoluție completă.
{{% /details %}}

{{% details title="Cum văd cum arată o aplicație într-o altă țară?" closed="true" %}}
Alege o țară din meniul derulant din partea de sus a paginii. Sunt acceptate peste 40 de magazine. Apasă **Lookup** din nou și instrumentul va relua preluarea aplicației pentru acea țară, afișând titlul, descrierea, capturile de ecran, noutățile și prețul localizate.
{{% /details %}}

{{% details title="Pot copia câmpuri individuale precum bundle ID sau data lansării?" closed="true" %}}
Da. Fiecare câmp de text din rezultat are propriul buton Copy: numele aplicației, dezvoltator, descriere, noutăți, bundle ID, versiune, preț, dimensiune fișier, OS minim, dată lansare, rating de conținut, limbi, dispozitive acceptate și JSON brut.
{{% /details %}}

{{% details title="AppLookup.pro funcționează pentru orice aplicație iOS?" closed="true" %}}
Funcționează pentru orice aplicație care este listată public în cel puțin o țară App Store și returnată de iTunes Search API. Aplicațiile nelistate, eliminate sau distribuite în întreprindere nu vor apărea.
{{% /details %}}

{{% details title="Acceptă aplicații macOS și Apple TV?" closed="true" %}}
Da. Dacă aplicația are capturi de ecran macOS sau Apple TV în răspunsul iTunes Search API, AppLookup.pro le afișează în propriul panou derulabil cu butoane de descărcare.
{{% /details %}}

{{% details title="Pot folosi JSON-ul brut în propriul cod?" closed="true" %}}
Da. Secțiunea Raw API Response afișează JSON-ul exact pe care îl returnează Apple. Copiază-l în Postman, un test unitar sau un pipeline backend. Te rugăm să respecți termenii API Apple și limitele de rată rezonabile.
{{% /details %}}

{{% details title="Este sigur să lipești URL-uri App Store în instrument?" closed="true" %}}
Da. URL-ul este analizat în browserul tău. Singurul apel de rețea de ieșire este căutarea către iTunes Search API de la Apple.
{{% /details %}}

{{% details title="Care este diferența dintre AppLookup.pro și AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) este pentru citirea metadatelor App Store din orice aplicație publicată: cercetarea concurenței, descărcarea resurselor, verificările de localizare. [AppKeywords.pro](https://appkeywords.pro) este pentru scrierea metadatelor App Store pentru propria ta aplicație: optimizarea titlului, subtitlului și cuvintelor cheie cu suport Fastlane. Cele două instrumente funcționează bine împreună.
{{% /details %}}
