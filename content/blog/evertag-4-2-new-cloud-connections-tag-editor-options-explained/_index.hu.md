---
title: "Evertag 4.2: új felhőkapcsolatok, a tag-szerkesztő beállításai elmagyarázva"
date: 2026-05-09
description: "Az Evertag 4.2 hozzáadja az Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP és NFS kapcsolatokat, frissíti a Wi-Fi Drive-ot, és a felületet a Liquid Glasshez igazítja. Ez a bejegyzés minden tag-szerkesztő beállítást is elmagyaráz — beleértve az ID3v2.4 vs ID3v2.3, az albumborító skálázását, a tag-ek duplikálását, a felhő feltöltési módokat és a Spotify és más streamingszolgáltatások számára helyes opciókat."
keywords: ["Evertag 4.2", "Evertag frissítés", "ID3 tag-szerkesztő iPhone", "ID3v2.4 vs ID3v2.3", "FLAC tag szerkesztés iOS", "MP3 tag szerkesztés iPhone", "albumborító szerkesztés iOS", "tag-szerkesztő Spotifyhoz", "tag-szerkesztő Plexhez", "tag-szerkesztő Apple Musichoz", "Evertag felhő tag-szerkesztő", "Internxt tag-szerkesztő", "Proton Drive tag-szerkesztő", "QNAP tag-szerkesztő", "Nextcloud tag-szerkesztő", "Amazon S3 tag-szerkesztő", "SFTP tag-szerkesztő iPhone", "FTP audio tag-szerkesztő", "NFS tag-szerkesztő iPhone", "Wi-Fi Drive tag-szerkesztő", "ID3 tag duplikáció", "albumborító skálázás", "Liquid Glass dizájn", "audio metaadat-szerkesztő iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Tag-szerkesztő", "ID3", "ID3v2.4", "ID3v2.3", "FLAC tag-ek", "MP3 tag-ek", "Albumborító", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Mi újság"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-administrator-everappz.webp"
---

{{< author-byline >}}

**Röviden:** Az [Evertag 4.2](/products/evertag) jelentős frissítés iPhone-ra, iPadre és Macre az audió tag-szerkesztőhöz. Megoldottuk a tag-szerkesztés kulcsfontosságú hibáit, és több mint 6 új felhő- és szerverkapcsolatot adtunk hozzá — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, valamint **FTP**, **SFTP** és **NFS** protokollok. A Wi-Fi Drive frissített felületet, többszörös kiválasztási módot, okosabb feltöltési sort és gyorsabb átviteleket kapott. Az egész app a **Liquid Glass** dizájnhoz van hangolva. Ez a bejegyzés mélyebbre is megy az Evertag tag-szerkesztő beállításaiban — elmagyarázva az **ID3v2.4 vs ID3v2.3**, **albumborító skálázás**, **tag duplikáció**, **felhő feltöltési módok**, **letöltött fájl törlése** és pontosan, hogy mely opciókat válaszd, ha audiót készítesz a **Spotify**, **Apple Music**, **Plex**, **Jellyfin** vagy bármilyen más streamingszolgáltatás számára.

---

## Sziasztok!

Megérkezett az Evertag nagy frissítése. Megoldottuk a tag-szerkesztés kulcsfontosságú hibáit, és **több mint 6 új felhő- és szerverkapcsolatot** adtunk hozzá, hogy az audio metaadatok kezelése egyszerűbb legyen, mint valaha — akár adatvédelem-orientált felhőben, akár otthoni öntárhelyű NAS-on, akár általános FTP/SFTP/NFS szerveren él a könyvtárad.

[Töltsd le az Evertag 4.2-t az App Store-ból](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611), vagy frissíts a jelenlegi verziódról.

## Kibővített felhő- és szervertámogatás

Az Evertag most már nativan kapcsolódik a felhő- és önállóan futtatott tárolási opciók szélesebb választékához. Bárhol is legyenek a fájljaid, szerkesztheted az ID3, MP4, FLAC, OGG és APE tag-eket.

### Adatvédelem-orientált felhőtárhelyek: Internxt és Proton Drive

Ha fontos számodra a végpontok közötti titkosítás és a zero-knowledge tárolás, az adatvédelmi-elsődleges felhők közül a két legtekintélyesebb név mostantól natívan elérhető az Evertagben:

- **Internxt** — nyílt forráskódú, posztkvantum titkosítású, GDPR-kompatibilis spanyol felhő. Ingyenes szint elérhető.
- **Proton Drive** — végpontok közötti titkosítású tároló a Proton Mail és a Proton VPN készítőitől, svájci központtal. Ingyenes szint elérhető, fizetős csomagok nagyobb könyvtárakhoz.

Most már közvetlenül szerkesztheted a metaadatokat bármelyik szolgáltatásban tárolt audiofájlokon — a fájl titkosítva marad átvitel közben, és csak az új tag-ek íródnak vissza.

### Önállóan futtatott megoldások: QNAP, Nextcloud, Amazon S3

Saját infrastruktúrát üzemeltető felhasználóknak:

- **QNAP** — natív API-kapcsolat QNAP NAS-eszközökhöz. Szerkeszd a tag-eket a QNAP-on lévő fájlokon helyi Wi-Fin vagy távoli hozzáféréssel.
- **Nextcloud** — csatlakozz bármilyen Nextcloud-példányhoz, akár saját üzemeltetésű, akár felügyelt.
- **Amazon S3** — irányítsd az Evertaget bármely S3-tárolóra (vagy S3-kompatibilis tárolóra, mint a Backblaze B2, Wasabi, MinIO, Cloudflare R2), és helyben szerkeszd a metaadatokat.

### Új hálózati protokollok: FTP, SFTP, NFS

Az Evertag 4.2 három klasszikus protokollt ad hozzá az egyéni szerverekkel, otthoni laborokkal vagy általános NAS-szal rendelkező felhasználók számára:

- **SFTP (SSH File Transfer Protocol)** — a megfelelő válasz **biztonságos távoli tag-szerkesztéshez a saját szerveredről**. Az SFTP az SSH-n fut, így a teljes átvitel (hitelesítés és audioadat) titkosított. Ha SSH-hozzáféréssel rendelkező VPS-ed, dedikált szervered vagy otthoni Linux gépet, akkor egyéb dolgok felfedése nélkül szerkesztheted a tag-eket távoli fájlokon. Támogatja a jelszó és a kulcs alapú hitelesítést is.
- **FTP** — a fájlátvitel régóta bevált szabványa. Régebbi otthoni NAS-okhoz hasznos, amelyek FTP-t kínálnak, de nincs natív API-integrációjuk.
- **NFS (Network File System)** — a Linux és a legtöbb NAS-eszköz de facto megosztási protokollja. Kisebb többletköltség, mint az SMB-é ugyanazon hardveren.

> **Tipp:** Az SFTP az a protokoll, amelyet a nyílt interneten keresztüli távoli szerkesztéshez akarsz használni. Az FTP és az NFS a helyi hálózatban a legjobb — ne tedd ki őket az internetnek, hacsak nem csomagolod őket VPN-be.

## Wi-Fi Drive fejlesztések

A [**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) az Evertag beépített funkciója audiofájlok **vezeték nélküli átviteléhez a számítógép és az iPhone vagy iPad között — iTunes, kábel és felhőfiók nélkül**. Mindkét eszköznek ugyanazon a Wi-Fi-hálózaton kell lennie.

Az Evertag 4.2-ben a Wi-Fi Drive a következőket kapja:

- **Frissített, modern felület** — letisztultabb, könnyebben olvasható, és a Liquid Glashez igazítva.
- **Többszörös kiválasztási mód** — válassz több fájlt vagy mappát, és tömegesen műveleteket végezhetsz rajtuk.
- **Okosabb feltöltési sor** — jobb folyamatvisszajelzés és nagyobb ellenálló képesség a hálózati zavarokkal szemben.
- **Jobb sebesség és általános megbízhatóság** — gyorsabb átvitelek nagy könyvtáraknál.

Ez a leggyorsabb módja annak, hogy egy köteg audiofájlt áthelyezz a számítógépről a telefonra, szerkeszd a tag-eket, majd visszaküldd — mindezt harmadik féltől származó szolgáltatás nélkül.

## Tag-szerkesztő beállítások: mély merülés

Ez az a rész, amit a felhasználók többsége soha nem olvas — és ez a rész dönti el, hogy a tag-jeid mindenhol működnek-e, vagy csak egyes appokban. Nyisd meg az Evertaget, majd lépj az **audio tag-szerkesztő beállítások** részbe. Itt van, hogy mit tesz valójában minden opció, és melyiket válaszd a célodtól függően.

### Albumborító skálázás

Amikor mented az albumborítót egy audiofájlba, az Evertag beágyazás előtt méretezheti a képet. Az elérhető opciók:

- **Kicsi** — legkisebb hatás a fájlméretre, alacsonyabb képminőség.
- **Közepes** — kiegyensúlyozott választás a felhasználók többségének.
- **Nagy** — magas minőség, alkalmas nagy képernyős lejátszókhoz és CarPlay-hez.
- **Extra nagy** — nagyon magas minőség, észrevehető fájlméret-növekedés.
- **Eredeti (Letiltva)** — a borítót az eredeti felbontásban ágyazza be. **Skálázás nélkül.**

**Miért fontos ez:**

- **Nagyobb minőség = nagyobb fájl.** Egy 3 000 × 3 000 pixeles borító több MB-ot adhat hozzá minden számhoz. Egész album esetén a lemezterhelés gyorsan halmozódik.
- **Néhány lejátszó nem kezeli jól a nagyon nagy beágyazott képeket.** Régebbi eszközök, néhány autós fejegység és egyes legacy asztali lejátszók ~1500 px feletti borítóknál fennakadhatnak vagy elutasíthatják a megjelenítést.
- **A legtöbb felhő- és streamingmunkafolyamathoz** a **Közepes** vagy **Nagy** az ideális. Az **Eredetit** csak akkor használd, ha kifejezetten archív minőségre van szükséged, vagy egy megbízható lejátszóhoz készíted a fájlokat.

> Az **Eredeti** méret opció az Evertag prémium személyre szabás-frissítésének része. A standard méretek (Kicsi/Közepes/Nagy/Extra nagy) ingyenesek.

### Tag mentési opciók: ID3v2.4 vs ID3v2.3

Ez a legfontosabb egyetlen beállítás a kompatibilitás szempontjából. Az ID3v2 a metaadat-formátum az MP3 fájlokon belül. Két széles körben használt verzió létezik, és finom, de fontos részletekben különböznek.

#### ID3v2.4

- Újabb, támogatja az **UTF-8 szövegkódolást** — helyesen kezeli a nem latin írásokat (kínai, orosz, japán, arab, héber stb.).
- Több keret-típus (relatív hangerő, equalizer-előbeállítások stb.).
- **Modern lejátszókhoz ajánlott**, amelyek támogatják.

#### ID3v2.3

- Régebbi, de **a leguniverzálisabban támogatott** ID3 verzió.
- Nem támogatja közvetlenül az UTF-8-at (UTF-16-ot használ Unicode szöveghez).
- **Akkor ajánlott, ha maximális kompatibilitásra van szükséged** régebbi lejátszókkal, autórádiókkal és bizonyos asztali alkalmazásokkal.

#### Mikor engedélyezd az ID3v2.4-et az Evertagben

- **Modern audio lejátszókat** használsz, mint az Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (jelenlegi verziók) vagy modern Android lejátszók. ✅ **Kapcsold be az ID3v2.4-et.**
- A könyvtárad **nem latin karaktereket** tartalmaz (kínai, koreai, japán, orosz, arab, görög, héber). ✅ **Kapcsold be az ID3v2.4-et** — az UTF-8 sokkal tisztábban kezeli ezeket.

#### Mikor tiltsd le az ID3v2.4-et az Evertagben (használd helyette az ID3v2.3-at)

- **Régebbi autórádióhoz vagy műszerfal-egységhez** készítesz fájlokat, amely nem olvas v2.4 tag-eket.
- Szerkesztés után **összezavart szöveget vagy hiányzó tag-eket** látsz egyes appokban — ez erős jel arra, hogy a v2.4 ott nem támogatott. Válts vissza v2.3-ra.
- **Legacy asztali lejátszókat** vagy régebbi hordozható lejátszókat (korai iPodok, néhány MP3 lejátszó a 2000–2010-es évekből) céloznál meg.

> **Hüvelykujjszabály:** ha a tag-jeid mindenhol helyesen jelennek meg v2.4-gyel, hagyd bekapcsolva. Ha akár egy fontos lejátszó rossz karaktereket, üreseket mutat vagy nem olvassa a tag-eket, kapcsold ki a v2.4-et és mentsd újra.

#### Tag-ek duplikálása

Amikor engedélyezed a **Tag-ek duplikálását**, az Evertag a közös metaadatmezőket (cím, előadó, album stb.) **mindkét ID3v1 és ID3v2 szakaszába** írja a fájlnak. Ez javítja a kompatibilitást nagyon régi lejátszókkal, amelyek csak az ID3v1-et olvassák (a fájl végén lévő eredeti 128 bájtos tag).

- **A felhasználók többségének nincs erre szüksége.** A modern lejátszók először az ID3v2-t olvassák.
- **Csak akkor engedélyezd, ha** vintage hardverrel vagy az ID3v2-t figyelmen kívül hagyó specifikus szoftverrel foglalkozol.

### Online fájlok frissítése: hogyan kezeli az Evertag a felhőszerkesztéseket

Amikor egy csatlakoztatott felhőben (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP stb.) tárolt fájl tag-jeit szerkeszted, az Evertagnek vissza kell töltenie a módosított fájlt. Te ellenőrzöd, hogyan:

- **Megerősítő üzenet megjelenítése** *(alapértelmezett, ajánlott)* — Az Evertag feltöltés előtt megkérdez. Legjobb az óvatos felhasználóknak és megosztott könyvtáraknak.
- **A fájl metaadatainak automatikus frissítése** — minden szerkesztés után csendben feltölt. Legjobb az egyéni felhasználóknak gyors, megbízható kapcsolattal, akik sokat szerkesztenek.
- **Ne frissítse a fájl metaadatait** — Az Evertag csak a helyi másolatot szerkeszti. Hasznos a változtatások előnézetéhez anélkül, hogy a felhőbe küldenénk őket.

### Online fájlok szerkesztése: helyi fájl tisztítása

Egy távoli fájl szerkesztéséhez az Evertag először letölti azt az eszközödre. A szerkesztés után kiválasztod, mi történjen ezzel a helyi másolattal:

- **Mindig törölje a letöltött fájlt** — Az Evertag a szerkesztés után eltávolítja az ideiglenes fájlt. **Ajánlott**, ha kevés a tárhelyed, vagy mások fájlján dolgozol.
- **Ne törölje a letöltött fájlt** — a szerkesztett fájlt az eszközödön tartja. Hasznos, ha mind offline példányt, mind frissített felhőpéldányt szeretnél.

### Gombok a főképernyőn

Az Evertag tag-szerkesztő főképernyője megjelenítheti vagy elrejtheti az egyéni műveletek gombjait. Csak azokat aktiváld, amelyeket valóban használsz, hogy a felület fókuszált maradjon:

- **Audio tag-ek automatikus keresése** — online keresi a hiányzó metaadatokat a fájl audió ujjlenyomata alapján.
- **Audio tag-ek manuális keresése** — keresés cím/előadó alapján, ha az automatikus keresés sikertelen.
- **Albumborító keresése** — magas minőségű borítókat keres és ágyaz be.
- **Albumborító mentése** — exportálja a beágyazott borítót a fotótárba vagy fájlokba.
- **Kódolás normalizálása** — javítja a régi kódolások által okozott összezavart nem latin szöveget (nagyon hasznos legacy szoftverrel rippelt cirill, kínai és japán dalokhoz).
- **Audio tag-ek törlése** — minden tag-et eltávolít a fájlból. Hasznos tiszta újra-tagelés előtt.

### Bővített tag-ek megjelenítése

Kapcsold be ezt a teljes metaadat-mezőkészlet megjelenítéséhez az alapvető cím/előadó/album/év mezőkön túl — beleértve a BPM-et, karmestert, eredeti előadót, hangulatot, szerzői jogot, kódolót, megjegyzéseket, dalszövegeket és többet. Power user funkció; a legtöbb alkalmi felhasználónak nincs rá szüksége.

### Fájlok egyidejű szerkesztése

Bekapcsoláskor az Evertag lehetővé teszi a metaadatok szerkesztését **több kiválasztott fájlon egyszerre** — egyetlen művelettel állítsd be ugyanazt az album artist, év vagy műfaj értéket egy egész albumra. Ez a leggyorsabb módja a nagy, rendezetlen könyvtár rendbetételének.

## Tag-ek szerkesztése Spotify, Apple Music és streaming platformokhoz

Gyakori kérdés: «szerkesztettem a tag-eket az Evertagben, feltöltöttem a fájlokat, és a streaming szolgáltatás rossz metaadatokat mutat. Mi a baj?»

Rövid válasz: **a streaming szolgáltatások nem mindig tisztelik a helyi tag-jeidet.** Az Apple Music és a Spotify saját belső adatbázissal rendelkezik — amikor felismernek egy számot, felülírják a megjelenített metaadatokat a sajátjukkal. De a **feltöltött fájlokra**, a helyi fájlokra (Apple Music «Library» funkció, Spotify Local Files) és a **streaming platformokra történő terjesztői feltöltésekre** a tag-jeid abszolút számítanak. Így állítsd be az Evertaget minden forgatókönyvhöz:

### Fájlok előkészítése Apple Music-hoz (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Az Apple Music helyesen kezeli az UTF-8-at.
- **Albumborító: Nagy** — Az Apple alkalmazásai jól renderelik a nagy borítókat; az Eredeti túlzás.
- **Tag-ek duplikálása: OFF** — nem szükséges.
- Győződj meg arról, hogy az **Album Artist** helyesen van kitöltve — az Apple Music csoportosításhoz használja.

### Fájlok előkészítése Spotify Local Files-hoz

A Spotify Local Files csak a jól tagelt fájlokat jeleníti meg. A Spotify által olvasott tag-ek korlátozottak.

- **ID3v2.4: ON** a legtöbb esetben. Ha egy szám szerkesztés után nem jelenik meg helyesen a Spotifyban, **próbáld meg ID3v2.4: OFF beállítással menteni** (azaz ID3v2.3-ként) — a Spotify értelmezője történelmileg konzervatív volt a v2.4-gyel kapcsolatban.
- **Albumborító: Közepes vagy Nagy** — a Spotify amúgy is lekicsinyíti.
- Töltsd ki legalább a **Címet**, **Előadót**, **Albumot** és **Szám számát**.

### Fájlok előkészítése terjesztői feltöltéshez (DistroKid, TuneCore, CD Baby stb.)

Ha művészként saját munkáidat töltöd fel streaming platformokra, a terjesztő általában olvassa a tag-eket, de a felületén is metaadatokat kér. Bárhogy is:

- **ID3v2.3** gyakran a biztonságosabb alapérték — sok terjesztői pipeline évekkel ezelőtt épült, és a régebbi formátumot részesíti előnyben.
- Ágyazz be **Nagy** borítót (a legtöbb terjesztő ≥ 1400 × 1400 px borítót igényel — ellenőrizd az iránymutatásaikat).
- Ne támaszkodj a bővített tag-ekre — a terjesztők csak az alapmezőket olvassák.

### Fájlok előkészítése Plex, Jellyfin, Navidrome, Subsonic, Emby számára

Ezek az önállóan futtatott média-szerverek nagyon toleránsak. Mind a v2.3-at, mind a v2.4-et tisztán olvassák, és jól kezelik az UTF-8-at.

- **ID3v2.4: ON** rendben van.
- **Albumborító: Nagy** vagy **Extra nagy** — ezek a szerverek mobil klienseknek és CarPlay képernyőknek szolgáltatnak borítókat, így a minőség számít.
- **Album Artist** erősen ajánlott — ezt használják a Plex/Jellyfin az albumok előadó szerinti helyes csoportosításához.

### Fájlok előkészítése autórádiókhoz és régebbi hardverhez

- **ID3v2.4: OFF** (használd az ID3v2.3-at) — a régebbi fejegységek gyakran nem támogatják a v2.4-et.
- **Albumborító: Közepes** — sok autókijelző fennakad a nagy beágyazott borítókon.
- **Tag-ek duplikálása: ON** — a régebbi autórádiók néha csak az ID3v1 visszaesést olvassák.

## Egyéb fejlesztések

### Liquid Glass dizájn

Az Evertag 4.2 felülete az Apple új **Liquid Glass** anyagához igazodik az egész alkalmazásban — áttetsző felületek, simább animációk és finomított vezérlők, amelyek természetesen illeszkednek az iOS, iPadOS és macOS rendszerekhez.

### Frissített kapcsolati könyvtárak

Frissítettük a belső könyvtárakat, amelyeket az Evertag a **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** és más szolgáltatásokkal való kommunikációhoz használ. Az eredmény: kevesebb határeseti kapcsolódási hiba, jobb támogatás az újabb szerververziókhoz, és nagyobb megbízhatóság a tag-ek távoli fájlokon történő szerkesztésekor.

### Fordítási és lokalizációs javítások

Több nyelvi javítás a felületen a felhasználók közvetlen visszajelzései alapján. Jobb szövegelhelyezés a kis gombokon több nyelven.

### A visszajelzéseid által ihletett kisebb finomítások

Sok kisebb fejlesztés az App Store-értékelésekből és a support@everappz.com címre érkező e-mailekből. Minden üzenetet elolvasunk.

## Szerezd be az Evertag 4.2-t

[**Töltsd le az Evertaget az App Store-ból**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611), vagy frissíts az App Store-on belül. Az Evertag ingyenes letöltésű, opcionális alkalmazáson belüli fejlesztésekkel a haladó funkciókhoz. Az új felhőkapcsolatok, hálózati protokollok, Wi-Fi Drive fejlesztések és Liquid Glass UI az alapfrissítés részei.

Ha tetszik az alkalmazás, kérjük, hagyj értékelést az App Store-ban — ez sokat segít. Visszajelzés vagy probléma? Írj nekünk a **support@everappz.com** címre. Minden üzenetet elolvasunk.

## Gyakran ismételt kérdések

{{% details title="Mi újság az Evertag 4.2-ben?" closed="true" %}}
Az Evertag 4.2 több mint 6 új felhő- és szerverkapcsolatot ad hozzá (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), frissített Wi-Fi Drive-ot többszörös kiválasztással és okosabb feltöltési sorral, Liquid Glass UI frissítéseket, frissített kapcsolati könyvtárakat, kulcsfontosságú tag-szerkesztési hibajavításokat és fordítási fejlesztéseket.
{{% /details %}}

{{% details title="ID3v2.4-et vagy ID3v2.3-at használjak az Evertagben?" closed="true" %}}
Használj **ID3v2.4-et** modern lejátszókhoz (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, modern Android alkalmazások) és nem latin karaktereket tartalmazó könyvtárakhoz — az UTF-8 támogatás tisztább kínai, koreai, japán, orosz, arab és héber tag-eket jelent. Használj **ID3v2.3-at**, ha a tag-jeid helytelenül jelennek meg egyes appokban, ha régebbi autórádiókat célzol meg, vagy ha egy streaming terjesztői pipeline elutasítja a v2.4-et. Mindig válthatsz és újramenthetsz.
{{% /details %}}

{{% details title="Miért rosszak a tag-jeim a Spotifyban szerkesztés után?" closed="true" %}}
A Spotify többnyire saját katalógusából jelenít meg metaadatokat — a helyi tag-jeidet csak a «Local Files»-hez vagy az általad művészként feltöltött tartalomhoz használja. Ha Spotify Local Files-hoz tagelsz fájlokat, és nem jelennek meg helyesen, próbáld meg letiltani az ID3v2.4-et az Evertagben, és menteni ID3v2.3-ként — a Spotify értelmezője történelmileg konzervatív volt a v2.4-gyel.
{{% /details %}}

{{% details title="Melyik albumborító-méretet válasszam az Evertagben?" closed="true" %}}
A felhasználók többségének: **Nagy**. Telefonokon, iPadeken, Maceken és modern autókijelzőkön remekül néz ki anélkül, hogy túlságosan felfújná a fájlokat. Használd a **Közepest**, ha hatalmas könyvtárad van, és lemezt szeretnél spórolni. Csak archív masterekhez vagy ha tényleg maximális minőségre van szükséged, használd az **Eredetit** (skálázás nélkül) — de tudd, hogy néhány régebbi lejátszó küzd a nagyon nagy beágyazott borítókkal. Az **Eredeti** az Evertag prémium személyre szabás-frissítésének része.
{{% /details %}}

{{% details title="A nagyobb albumborítók nagyobbá teszik a fájlokat?" closed="true" %}}
Igen. Egy 3000 × 3000 px-es borító beágyazása több megabájttal növelheti egyetlen audiofájl méretét. 1000 számos könyvtár esetén ez gigabájtokra rúg. Ha szűkös a tárhely, használd a Közepest vagy Nagyot; ha NAS-ról streamelsz, ahol a méret nem számít, az Extra nagy vagy Eredeti is jó.
{{% /details %}}

{{% details title="Mik a tag-ek duplikálása, és engedélyezzem őket?" closed="true" %}}
A tag-ek duplikálása a fő metaadatokat a fájl ID3v1 (legacy 128 bájt) és ID3v2 (modern) szakaszaiba is beírja. Csak akkor engedélyezd, ha nagyon régi lejátszókat vagy ID3v1-et olvasó hardvert célzol meg. A modern dolgokhoz (okostelefonok, számítógépek, újabb autórádiók) hagyd kikapcsolva.
{{% /details %}}

{{% details title="Az Evertag közvetlenül szerkeszti a tag-eket a felhőfájlokon?" closed="true" %}}
Igen. Csatlakozz a felhődhöz (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3 stb.) vagy FTP/SFTP/NFS-en keresztül, nyiss meg egy fájlt, és szerkeszd a tag-eket úgy, mintha helyi lenne. Az Evertag letölti a fájlt, alkalmazza a szerkesztéseidet, és visszatölti a frissített verziót. A beállításokban választhatsz a «Mindig kérdezzen», «Automatikus feltöltés» vagy «Ne töltse fel» módok közül.
{{% /details %}}

{{% details title="Tudok FLAC tag-eket szerkeszteni iPhone-on az Evertaggel?" closed="true" %}}
Igen. Az Evertag támogatja a FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE és más fontos formátumokat teljes olvasási/írási tag támogatással, beleértve a beágyazott borítót.
{{% /details %}}

{{% details title="Hogyan szerkeszthetem biztonságosan a tag-eket az otthoni szerveremen SFTP-vel?" closed="true" %}}
Nyisd meg az Evertaget, lépj a Connections menüpontra, válaszd az SFTP-t, és add meg a szerver hostnevét vagy IP-jét, portját (általában 22), felhasználónevet, valamint jelszót vagy SSH magánkulcsot. Az Evertag böngészi a távoli mappáidat, és a tag-eket közvetlenül szerkeszti SSH-n keresztüli végpontok közötti titkosítással.
{{% /details %}}

{{% details title="Tudok tag-eket szerkeszteni több fájlon egyszerre?" closed="true" %}}
Igen. Engedélyezd a **Fájlok egyidejű szerkesztése** opciót a beállításokban. Válassz több fájlt, nyisd meg a tag-szerkesztőt, és bármilyen mezőt is változtatsz, az alkalmazódik az összes kiválasztott fájlra. Ez a leggyorsabb módja annak, hogy egy egész albumra ugyanazt az album artist, év vagy műfaj értéket állítsd be.
{{% /details %}}

{{% details title="Ingyenes az Evertag 4.2-re való frissítés?" closed="true" %}}
Igen. Az Evertag ingyenesen letölthető az App Store-ból, és a 4.2 ingyenes frissítés minden meglévő felhasználó számára. Az új felhőintegrációk, Wi-Fi Drive fejlesztések és Liquid Glass UI az alapfrissítés részei.
{{% /details %}}

{{% details title="Mely eszközökön érhető el az Evertag 4.2?" closed="true" %}}
Az Evertag 4.2 iPhone-on, iPaden és Macen fut. Az iCloud Drive szinkronizáció eszközök között konzisztensen tartja a tag-szerkesztő beállításaidat.
{{% /details %}}
