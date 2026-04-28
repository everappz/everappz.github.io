---
title: "Kako reproducirati glazbu s Mac / PC / Linux / NAS na iPhoneu koristeći Kodi DLNA poslužitelj"
date: 2025-07-25
description: "Streamajte glazbu s računala ili NAS-a na iPhone putem Wi-Fi koristeći Kodi DLNA i aplikaciju Evermusic."
keywords: ["kodi dlna poslužitelj", "streamanje glazbe na iphone", "reproduciranje glazbe s nas", "evermusic dlna", "glazba s mac na iphone", "glazba s windows na iphone", "kodi dlna iphone", "dlna audio streaming"]
tags: ["dlna", "kodi", "evermusic", "iphone", "streamanje glazbe", "mac", "nas", "linux", "lokalna mreža"]
readingTime: 5
---

{{< author-byline >}}


**Sažetak:** Instalirajte Kodi na Mac, PC, Linux ili NAS, omogućite DLNA/UPnP poslužitelj i streamajte cijelu glazbenu knjižnicu na iPhone ili iPad koristeći besplatnu aplikaciju Evermusic ili Flacbox putem Wi-Fi. Bez pretplata.

## Uvod

Ako imate **Mac, Windows PC, Linux stroj ili NAS uređaj**, možete ga lako pretvoriti u **osobni glazbeni poslužitelj** kod kuće koristeći [Kodi](https://kodi.tv/), besplatnu i open-source medijsku platformu. S ugrađenim **DLNA/UPnP poslužiteljem** Kodija, možete streamati cijelu glazbenu knjižnicu na bilo koji DLNA-kompatibilni klijent — uključujući vaš iPhone ili iPad.

U ovom vodiču pokazat ćemo vam korak po korak kako:

- Instalirati Kodi na Mac ili PC  
- Postaviti glazbene mape za dijeljenje  
- Omogućiti DLNA glazbeni poslužitelj  
- Pristupiti toj glazbi koristeći **Evermusic** ili **Flacbox** iOS aplikaciju

Ova postavka je 100% besplatna — bez pretplata, samo vaša vlastita glazba streamana putem vaše Wi-Fi mreže. Bilo da pokušavate organizirati veliku MP3 kolekciju, slušati FLAC putem Wi-Fi ili jednostavno uživati u lokalnoj glazbi bez sinkronizacije putem iTunes, ova postavka je savršena za vas.

## Preuzimanje i instalacija Kodija na Mac / PC / Linux / NAS

Prvo posjetite službenu Kodi web stranicu:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Kodi glavna stranica" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Kliknite na **Preuzimanja** i pomaknite se kako biste pronašli verziju za vaše računalo.
Odaberite svoj operativni sustav. U ovom primjeru koristit ćemo **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Kodi stranica za preuzimanje" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Kliknite **Intel (x86/64)** ako imate Intel Mac ili **Apple Silicon** za M1, M2, M3 Mac za početak preuzimanja.

{{< cards cols="1">}}
{{< card subtitle="Odaberite macOS instalacijski program" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Pričekajte trenutak dok se instalacijski program preuzima.

{{< cards cols="1">}}
{{< card subtitle="Kodi preuzet" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Nakon preuzimanja, pronađite `.dmg` datoteku u mapi **Preuzimanja**.

{{< cards cols="1">}}
{{< card subtitle="Instalacija Kodija" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Dvaput kliknite na preuzetu datoteku za pokretanje instalacijskog programa.
Povucite Kodi u mapu **Aplikacije** za instalaciju.

{{< cards cols="1">}}
{{< card title="" subtitle="Instalirajte Kodi povlačenjem u Aplikacije" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Pokrenite Kodi. Možda ćete ga trebati dopustiti u **Postavke sustava → Sigurnost i privatnost → Ipak otvori**.

{{< cards cols="1">}}
{{< card subtitle="Kodi glavni zaslon" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Dodajte glazbu u Kodi knjižnicu

Kliknite **ikonu zupčanika** (Postavke) s početnog zaslona.

{{< cards cols="1">}}
{{< card subtitle="Kodi postavke" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Navigirajte do **Postavke medija → Knjižnica**. Omogućite **Ažuriraj knjižnicu pri pokretanju** za video i glazbenu knjižnicu za automatsko indeksiranje.

{{< cards cols="1">}}
{{< card subtitle="Postavke knjižnice" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Zatim idite na odjeljak **Glazba** i kliknite **Dodaj glazbu**.

{{< cards cols="1">}}
{{< card subtitle="Dodaj glazbenu mapu" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Pregledajte i odaberite mapu u kojoj je pohranjena vaša glazba.

{{< cards cols="1">}}
{{< card subtitle="Odaberite izvor glazbe" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Dodajte izvor glazbe u Kodi.

{{< cards cols="1">}}
{{< card subtitle="Dodaj izvor glazbe" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Potvrdite i dopustite Kodiju da skenira vašu glazbenu knjižnicu.

{{< cards cols="1">}}
{{< card subtitle="Potvrdite izvore glazbe" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Pričekajte trenutak dok se vaša knjižnica skenira i potpuno izgradi.

{{< cards cols="1">}}
{{< card subtitle="Skeniranje glazbene knjižnice" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Omogućite Kodi DLNA poslužitelj

Idite na **Postavke → Usluge → UPnP/DLNA**.

Omogućite opciju: **Dijeli moje knjižnice**.

Kodi sada djeluje kao DLNA poslužitelj na vašoj lokalnoj Wi-Fi mreži.

{{< cards cols="1">}}
{{< card subtitle="Omogući DLNA u Kodiju" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Otvorite Kodi knjižnicu

Desnim klikom zatvorite prozor postavki i otvorite Kodi glavnu knjižnicu.

{{< cards cols="1">}}
{{< card title="" subtitle="Desni klik za pristup Kodi knjižnici" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Preuzmite aplikaciju za streamanje glazbe za iOS

Nabavite besplatnu iOS DLNA klijentsku aplikaciju koja vam omogućuje streamanje glazbe iz širokog spektra usluga pohrane u oblaku i DLNA poslužitelja.

- Koristite **Evermusic** ako je vaša kolekcija uglavnom MP3 i drugi standardni audio formati.
- Odaberite **Flacbox** ako imate hi-res glazbenu knjižnicu u formatima poput FLAC, ALAC ili DSD.

Obje aplikacije dostupne su za **iOS** i **macOS**, i besplatne su za korištenje.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Preuzmite Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Preuzmite Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Dodajte DLNA izvor

Nakon što ste preuzeli iOS aplikaciju, otvorite odjeljak **Sva Povezivanja**.

{{< cards cols="1">}}
{{< card title="" subtitle="Glavni izbornik aplikacije Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Pomaknite se prema dolje i dodirnite **Lokalna mreža - Dostupni uređaji** za otkrivanje DLNA poslužitelja.
U ovom odjeljku vidjet ćete sve dostupne uređaje na vašoj lokalnoj mreži. Vaš **Kodi DLNA poslužitelj** trebao bi se pojaviti ovdje. Dodirnite Kodi poslužitelj za povezivanje.

{{< cards cols="1">}}
{{< card title="" subtitle="Dostupni DLNA uređaji u Evermusicju" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic će prikazati mape knjižnice dijeljene putem Kodija.

{{< cards cols="1">}}
{{< card title="" subtitle="Kodi glazbena knjižnica u Evermusicju" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Navigirajte do mape **Pjesme** za prikaz svih dostupnih audio datoteka na vašem DLNA poslužitelju.

{{< cards cols="1">}}
{{< card title="" subtitle="Pjesme navedene iz udaljene mape" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Dodirnite bilo koju audio datoteku za trenutno pokretanje streamanja.

{{< cards cols="1">}}
{{< card title="" subtitle="MP3 datoteka se reproducira u Evermusicju" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Vratite se na odjeljak **Povezivanja**. Dodani DLNA poslužitelj sada će se pojaviti ovdje. Dodirnite njegovu ikonu za ponovno povezivanje u bilo kojem trenutku. Također možete povezati druge usluge u oblaku s ovog zaslona koristeći iste korake.

Također možete omogućiti **Last.fm praćenje** ovdje. Statistike reprodukcije bit će spremljene na vaš Last.fm račun, pružajući personalizirane glazbene preporuke kasnije.

{{< cards cols="1">}}
{{< card title="" subtitle="Povezivanja u Evermusicju" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Izgradite glazbenu knjižnicu

**Evermusic** i **Flacbox** omogućuju vam dodavanje glazbe u knjižnicu i organiziranje po **oznakama metapodataka** poput izvođača, albuma, žanrova i skladatelja.

Za početak otvorite odjeljak **Glazbena knjižnica**. Pomaknite se prema dolje do **Alati i postavke** i dodirnite **Dodaj glazbu**.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic glazbena knjižnica" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Odaberite izvor glazbe — u ovom slučaju odaberite **Povezivanja**.

{{< cards cols="1">}}
{{< card title="" subtitle="Dodaj novu glazbu u Evermusicju" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Pronađite **Kodi DLNA poslužitelj** u Povezivanjima i dodirnite za prikaz mapa i datoteka.

{{< cards cols="1">}}
{{< card title="" subtitle="Odaberite DLNA poslužitelj za uvoz glazbe" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Odaberite mape ili datoteke koje želite dodati i dodirnite **Završeno**.

{{< cards cols="1">}}
{{< card title="" subtitle="Odaberite glazbenu mapu za dodavanje" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Aplikacija će skenirati odabrane datoteke i organizirati ih pomoću metapodataka u odjeljke poput Izvođači, Albumi, Žanrovi i Skladatelji.

{{< cards cols="1">}}
{{< card title="" subtitle="Glazbena knjižnica s kategorijama" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Stvaranje popisa pjesama

Također možete stvoriti vlastite popise pjesama.

Prvo otvorite karticu **Popisi pjesama**.

{{< cards cols="1">}}
{{< card title="" subtitle="Kartica popisa pjesama u Evermusicju" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Dodirnite gumb **plus (+)** i odaberite **Novi popis pjesama**.

{{< cards cols="1">}}
{{< card title="" subtitle="Stvorite novi popis pjesama" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Unesite naziv za svoj popis pjesama i dodirnite **Spremiti**.

{{< cards cols="1">}}
{{< card title="" subtitle="Unesite naziv popisa pjesama" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Zatim odaberite izvor za dodavanje pjesama — ovdje odabiremo **Knjižnicu**.

{{< cards cols="1">}}
{{< card title="" subtitle="Dodajte pjesme u novi popis pjesama" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Odaberite željene pjesme i dodirnite **Završeno** za dodavanje.

{{< cards cols="1">}}
{{< card title="" subtitle="Dodaj glazbu iz knjižnice u popis pjesama" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Vaše odabrane pjesme sada će se pojaviti u stvorenom popisu pjesama.

{{< cards cols="1">}}
{{< card title="" subtitle="Stvoreni popis pjesama prikazan na popisu" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Prema zadanim postavkama, pjesme su dostupne za streamanje. Za slušanje offline, omogućite **Offline način rada** — aplikacija će preuzeti sve pjesme popisa.

{{< cards cols="1">}}
{{< card title="" subtitle="Offline način rada omogućen za popis pjesama" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Dodirnite gumb **Više radnji** za istraživanje dodatnih opcija. Možete:

- Arhivirati popis pjesama  
- Promijeniti naslovnicu albuma  
- Preurediti pjesme  
- I još korisnih značajki

{{< cards cols="1">}}
{{< card title="" subtitle="Više radnji za popis pjesama dostupno" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Zaključak

S **Evermusic** i **Flacbox**, pretvaranje vašeg iPhone, iPad ili Mac u moćan DLNA glazbeni player je jednostavno. Bilo da pohranjujete glazbu u oblaku, na NAS-u ili na kućnom medijskom poslužitelju poput **Kodi**, ove aplikacije vam omogućuju streamanje, organiziranje i uživanje u vašoj kolekciji bez ograničenja.

- Streamajte MP3 ili hi-res FLAC izravno s vašeg **Kodi DLNA poslužitelja**  
- Izgradite osobnu glazbenu knjižnicu grupiranu po metapodacima (albumi, žanrovi, skladatelji)  
- Stvorite i upravljajte **prilagođenim popisima pjesama**  
- Omogućite **offline način rada** za slušanje u pokretu  
- Povežite se s **više usluga u oblaku** i **uređajima lokalne mreže**  
- Pratite navike slušanja s **Last.fm integracijom**

Bilo da ste audiofil ili povremeni slušatelj, Evermusic i Flacbox nude sve što vam treba za besprijekorno streamanje i organiziranje glazbe.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Preuzmite Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Preuzmite Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Počnite graditi svoje osobno glazbeno iskustvo danas.

## Često postavljana pitanja

{{% details title="Je li Kodi besplatan za korištenje kao DLNA poslužitelj?" closed="true" %}}
Da. Kodi je potpuno besplatan i open-source. Radi na macOS, Windows, Linux i mnogim NAS uređajima.
{{% /details %}}

{{% details title="Podržavaju li Evermusic i Flacbox FLAC streamanje putem DLNA?" closed="true" %}}
Da. Flacbox je optimiziran za hi-res formate poput FLAC, ALAC i DSD. Evermusic također podržava FLAC reprodukciju uz MP3 i druge standardne formate.
{{% /details %}}

{{% details title="Mogu li slušati offline nakon streamanja s Kodija?" closed="true" %}}
Da. Omogućite Offline način rada na bilo kojem popisu pjesama, i aplikacija će preuzeti sve pjesme na vaš uređaj za slušanje bez mrežne veze.
{{% /details %}}

{{% details title="Trebam li premium pretplatu za korištenje DLNA?" closed="true" %}}
Besplatna verzija podržava do 3 veze u oblaku ili mreži. Premium uklanja ovo ograničenje i omogućuje neograničeno povezivanje usluga i DLNA poslužitelja.
{{% /details %}}

{{% details title="Mora li moj iPhone biti na istoj Wi-Fi mreži kao Kodi?" closed="true" %}}
Da. DLNA streamanje radi putem vaše lokalne mreže. I Kodi poslužitelj i vaš iOS uređaj moraju biti povezani na istu Wi-Fi mrežu.
{{% /details %}}

{{% details title="Mogu li koristiti ovu postavku s NAS-om umjesto Mac-a ili PC-ja?" closed="true" %}}
Da. Mnogi NAS uređaji (Synology, QNAP itd.) podržavaju Kodi ili imaju vlastiti ugrađeni DLNA poslužitelj. Evermusic i Flacbox mogu se povezati s bilo kojim standardnim DLNA/UPnP poslužiteljem.
{{% /details %}}
