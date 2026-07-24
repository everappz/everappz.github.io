---
title: "Kako koristiti zvučne efekte i DSP u Flacboxu: kompresor, Freeverb, crossfeed, echo, normalizacija glasnoće i više"
date: 2026-07-24
description: "Potpuni vodič za Flacbox zvuk na iPhoneu, iPadu i Macu. Naučite kako radi BASS motor, koje dodatne formate reproducira (uključujući MOD i tracker glazbu te DSD) i točno što svaki efekt, svaki klizač i svaki preset čini vašem zvuku, uz 10-pojasni ekvalizator i prilagođeni DSP lanac."
keywords: ["Flacbox zvučni efekti", "Flacbox preseti objašnjeni", "Flacbox BASS motor", "BASS audio biblioteka iOS", "MOD glazbeni reproduktor iPhone", "tracker glazbeni reproduktor iOS", "reprodukcija MOD XM IT S3M iPhone", "DSD reproduktor iOS", "FLAC reproduktor iPhone", "lossless glazbeni reproduktor iOS", "Flacbox preseti ekvalizatora", "10-pojasni ekvalizator iPhone", "normalizacija glasnoće iPhone", "EBU R128 iOS", "normalizacija glasnoće glazbeni reproduktor", "crossfeed slušalice iOS", "bs2b crossfeed", "preseti kompresora glazbeni reproduktor", "freeverb reverb iOS", "echo delay glazbeni reproduktor", "DSP lanac glazbeni reproduktor", "pojačanje basa iPhone", "kako dodati efekte glazbi Flacbox", "najbolje postavke ekvalizatora iPhone"]
tags: ["Flacbox", "Zvučni efekti", "Upute", "BASS", "Ekvalizator", "Pojačanje basa", "Kompresor", "Freeverb", "Crossfeed", "Echo", "Normalizacija glasnoće", "EBU R128", "MOD glazba", "Tracker glazba", "DSD", "FLAC", "DSP", "Slušalice", "Preseti"]
readingTime: 30
---

{{< author-byline >}}

{{< full-width-tables >}}

**Kratki odgovor:** U Flacboxu odaberete jedan **Motor reprodukcije** u **Postavke > Audio player**: **Standard** (Appleov sustavski motor), **Universal** (FFmpeg motor) ili **Sound FX** (**BASS™ motor**). Motor koji odaberete određuje koji se formati datoteka reproduciraju, pa je izbor bitan. **Sound FX** motor reproducira dodatne formate koje većina iPhone aplikacija preskače (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus i staru **MOD i tracker glazbu** poput MOD, XM, IT i S3M), i to je jedini motor koji pokreće zvučne alate: **10-pojasni ekvalizator**, **Normalizaciju glasnoće**, **Kompresor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distorziju**, **Rotate**, **Crossfeed** i izgradite-svoj **DSP lanac**. Dakle, da biste koristili efekte u ovom vodiču, prvo postavite Motor reprodukcije na **Sound FX**. Svaki alat ima gotove **presete**. Otvorite ih u **Postavke > Audio player** (Audio efekti, Audio ekvalizator, Obrada signala) ili dodirnite gumb **⋯ (Više)** na reproduktoru i odaberite **Audio efekti**. Ništa što ovdje učinite nikada ne mijenja vaše datoteke.

> Objašnjenja klizača i preseta u nastavku iste su kratke opise koje vam Flacbox prikazuje unutar aplikacije, uz malo dodatne pozadine kako biste dobili potpunu sliku prije nego što dodirnete.

## Kako čitati ovaj vodič

Svaki alat radi na isti način:

1. **Uključite ga.** Svaki efekt ima svoj prekidač za uključivanje/isključivanje. Svi su isprva isključeni. Možete uključiti koliko god ih želite istovremeno.
2. **Odaberite preset.** Preset je gotova postavka. Dodirnite jedan i zvuk se odmah promijeni. Ovaj vodič navodi što **svaki** preset čini.
3. **Fino podesite (opcionalno).** Otvorite klizače da ručno prilagodite. U trenutku kad pomaknete klizač, efekt prikazuje **Manual**, tako da znate da ste napustili preset. Svaki klizač ima gumb za poništavanje.

Ništa se ne sprema u vaše datoteke. Ovo su efekti uživo. Isključite efekt i vaš izvorni zvuk odmah se vraća.

## Odaberite svoj Motor reprodukcije (Sound FX ima efekte)

Flacbox ne miješa motore zajedno. Odaberete **jedan** u **Postavke > Audio player > Motor reprodukcije**, a motor koji odaberete određuje koje formate datoteka možete reproducirati i jesu li efekti dostupni. Postoje tri izbora, prikazana u aplikaciji pod ovim točnim nazivima:

1. **Standard.** Appleov ugrađeni sustavski motor. Koristi hardversko dekodiranje za manju potrošnju baterije.
2. **Universal.** FFmpeg motor, koji otvara vrlo širok raspon formata.
3. **Sound FX.** **BASS™ motor**. Reproducira lossless i visokorezolucijske datoteke s punom točnošću, dodaje modul (tracker) glazbu i pokreće svaki efekt, 10-pojasni ekvalizator i DSP lanac iz ovog vodiča.

Budući da svaki motor podržava vlastiti skup formata, datoteke koje možete reproducirati mijenjaju se s motorom koji odaberete. Još važnije, efekti, ekvalizator i DSP lanac rade **samo** sa **Sound FX** motorom, pa ga odaberite prvo ako ih želite koristiti.

Sound FX izgrađen je na **BASS™**, profesionalnoj audio biblioteci tvrtke Un4seen Developments. Više o njoj možete pročitati na njezinoj početnoj stranici na [un4seen.com](https://www.un4seen.com/).

## Glazbeni formati: što Sound FX (BASS™) motor dodaje (uključujući MOD i tracker glazbu)

S odabranim **Sound FX (BASS™)** motorom, Flacbox reproducira specijalističke formate u nastavku, povrh svakodnevnih. Najposebnija je **modul glazba**, koja se naziva i **tracker glazba**. Modul datoteka nije normalna snimka. Sadrži male zvukove instrumenata plus «partituru» koja govori kako ih svirati, a Flacbox uživo ponovno gradi pjesmu iz te partiture, onako kako su ove datoteke bile zamišljene da se reproduciraju. Normalni reproduktori to ne mogu.

| Vrsta glazbe | Formati | Dobro je znati |
|---|---|---|
| **Modul / tracker glazba** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Uživo ponovno izgrađeno BASS™ modul reproduktorom. Odlično za chiptune i stare demoscene ili Amiga pjesme. |
| **Moderni lossless** | FLAC | Puna kvaliteta, manje od WAV-a. |
| **Ostali lossless** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Manje uobičajene lossless vrste, sve podržane. |
| **Visokorezolucijski DSD** | DSF, DFF | Reproducira na normalnom hardveru koristeći DSD preko PCM-a. |
| **Moderni lossy** | Opus, Ogg Vorbis, MP3 | Uobičajene vrste za streaming i preuzimanje. |

Sound FX motor također reproducira mainstream Apple formate (AAC, ALAC, M4A, WAV, AIFF) i streamove uživo, pa efekti i ekvalizator rade i na njima.

**Zašto vam ovo pomaže:** ako imate mješavinu FLAC albuma, DSD visokorezolucijskih datoteka i mape starih MOD ili XM tracker pjesama, Flacbox ih sve reproducira, a ekvalizator i efekti rade na svakoj od njih.

## Tri izbornika koje ćete koristiti

Flacbox drži svoje zvučne alate na tri mjesta, sva unutar postavki audio playera. Prvo provjerite je li vaš **Motor reprodukcije** postavljen na **Sound FX** (Postavke > Audio player > Motor reprodukcije), jer su efekti, ekvalizator i DSP lanac dostupni samo s tim motorom.

- **Audio efekti** (polica efekata): otvorite reproduktor, dodirnite **⋯ (Više)**, dodirnite **Audio efekti**. Ili idite na **Postavke > Audio player > Audio efekti**.
- **Audio ekvalizator** (10 pojasa i preseta): **Postavke > Audio player > Audio ekvalizator**.
- **Obrada signala** (vaš vlastiti DSP lanac): **Postavke > Audio player > Obrada signala**.

Također možete postaviti **izlaznu frekvenciju uzorkovanja**, **kanale** i **veličinu međuspremnika** pod **Postavke > Audio player**.

## 10-pojasni ekvalizator

**Što radi:** Mijenja ton glazbe, od dubokog basa do svijetlih visokih tonova. Ovo je najbolji alat za čisto **pojačanje basa** ili svjetliji, jasniji gornji kraj. Zamislite ga kao deset gumba za glasnoću, svaki za drugačiji dio zvuka. Podignite pojas da izbacite taj dio naprijed, spustite ga da ga povučete natrag. Male promjene od nekoliko dB obično zvuče najbolje, i radi na svemu što reproducirate.

**Kako radi:** Deset klizača na **32, 64, 125, 250, 500 Hz i 1, 2, 4, 8, 16 kHz**. Svaki ide od **-12 dB (rez)** do **+12 dB (pojačanje)**. Tu je i **Predpojačalo** od **-24 do +24 dB** za ukupnu razinu. Možete spremiti vlastite presete i **izvesti ili uvesti** ih između uređaja.

**Što svaki ugrađeni preset radi (22 preseta):**

| Preset | Što čini vašem zvuku |
|---|---|
| **Flat** | Bez promjene. Svi pojasevi na nuli. Čista polazna točka. |
| **Acoustic** | Topli bas i oštri, prisutni visoki tonovi. Čini akustične gitare i glasove prirodnima i živahnima. |
| **Bass Booster** | Snažno podizanje u niskom kraju, srednji i visoki tonovi netaknuti. Više udara i težine. |
| **Bass Reducer** | Reže niski kraj. Zgodno za prostorije s bučnim basom, jeftine slušalice ili teške pjesme. |
| **Treble Booster** | Podiže samo visoke tonove. Dodaje sjaj i zrak, više detalja. |
| **Treble Reducer** | Ublažava visoke tonove. Ukroćuje oštre ili prodorne snimke. |
| **Classical** | Puni niski tonovi i blagi visoki uz lagani pad srednjih. Glatko i prostrano za orkestralnu glazbu. |
| **Dance** | Veliki niski i svijetli visoki tonovi s uvučenim srednjima. Udarno i energično za klupske pjesme. |
| **Deep** | Topao, gust niski kraj s mekšim visokim tonovima. Ugodan, opušten zvuk. |
| **Electronic** | Snažan bas i svijetli visoki tonovi za sinteze i ritmove. Široko i moderno. |
| **Hip-Hop** | Težak bas i jasni visoki tonovi s kontroliranim srednjima. Težinsko i udarno. |
| **Jazz** | Toplo i glatko, s malim padom srednjih. Lagano i prirodno za akustični jazz. |
| **Latin** | Pojačani niski i visoki tonovi s čistim srednjima. Svijetlo i živahno. |
| **Loudness** | Snažno pojačava bas i visoke tonove («smile» krivulja). Zvuči punije pri niskoj glasnoći. |
| **Lounge** | Istaknuti srednji tonovi s mekim rubovima. Opušteno i pogodno za vokale. |
| **Piano** | Jasni srednji i visoki tonovi tako da note klavira čisto zvone. |
| **Pop** | Podignuti srednji tonovi za vokale, s povučenim niskim i visokim. Glasovi su naprijed. |
| **R&B** | Vrlo snažna nisko-srednja toplina i jasni visoki tonovi. Glatko i bogato. |
| **Rock** | Pojačani niski i visoki tonovi za gitare i bubnjeve. Energično i puno. |
| **Small Speakers** | Pojačava niske i reže visoke tonove kako bi maleni zvučnici zvučali punije. |
| **Spoken Word** | Podiže raspon glasa i reže duboki bas. Čini govor jasnim. |
| **Vocal Booster** | Gura sredinu gdje žive glasovi, reže oko njih. Vokali se ističu. |

**Savjet za bas:** Počnite s **Bass Booster**, zatim, ako zvuči mutno, spustite Predpojačalo za 1 do 2 dB kako ništa ne bi distorziralo.

## Normalizacija glasnoće (ujednačena glasnoća)

**Što radi:** Neke pjesme sviraju glasnije od drugih, pa stalno mijenjate glasnoću. Ovo čini da svaka pjesma svira otprilike jednako glasno sama od sebe, tako da vi ne morate. Savršeno je za nasumične popise pjesama koji miješaju stare i nove snimke, različite albume ili različite izvore, gdje jedna pjesma može biti mnogo glasnija od sljedeće.

**Kako radi:** Sluša stvarnu glasnoću svake pjesme koristeći **EBU R128** standard (mjeren u **LUFS**, isti princip koji koriste streaming usluge), zatim prilagođava svaku pjesmu prema vašem cilju. Ne treba nikakve oznake u vašim datotekama i nikada ne mijenja audio. EBU R128 mjeri glasnoću koju vaše uši zapravo osjećaju kroz cijelu pjesmu, ne samo najviši vrh, zbog čega odgovara koliko glasno pjesme stvarno djeluju na vas. Flacbox to izračunava uživo dok glazba svira (i provjerava glasnoću unaprijed kada može), zatim primjenjuje jednu, ustaljenu promjenu glasnoće na pjesmu. Granica **Max boost** sprječava da vrlo tihe snimke budu podignute toliko jako da distorziraju. Budući da čita sam zvuk, radi na bilo kojem izvoru, uključujući datoteke u oblaku, streamove uživo i modul glazbu, čak i kada datoteke uopće nemaju oznake glasnoće.

**Klizači:**

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Ciljna glasnoća** | Postavlja glasnoću prema kojoj se svaka pjesma niveliranja. Više vrijednosti čine sve glasnijim ukupno. | -30 do -6 LUFS (-16) |
| **Max boost** | Ograničava koliko se tihe pjesme mogu pojačati. Više vrijednosti približavaju meke snimke cilju. | 0 do 24 dB (12) |

**Preseti:**

| Preset | Što radi |
|---|---|
| **Light** | Blago niveliranje za ležerno slušanje. Izjednačuje očite skokove glasnoće bez snažnog guranja tihih pjesama. |
| **Standard** | Univerzalna zadana postavka. Cilj glasnoće u streaming stilu koji odgovara većini glazbe. Počnite ovdje. |
| **Strong** | Agresivno usklađivanje koje čvrsto gura tihe pjesme prema gore. Najbolje za mješovite biblioteke s velikim razlikama u razini. |
| **Night** | Tiši ukupni cilj koji i dalje podiže meke dijelove, tako da kasnonoćno slušanje ostaje dosljedno i tiho. |

## Kompresor (izjednačavanje glasnih i tihih dijelova)

**Što radi:** U jednoj pjesmi, tihi dijelovi mogu biti previše meki, a glasni dijelovi previše glasni. Ovo ih približava, tako da se cijela pjesma lako čuje, čak i u autu ili na bučnom mjestu. Nježno stišava najglasnije trenutke i podiže mekše, tako da prestanete posezati za glasnoćom tijekom jedne pjesme. Ovo se razlikuje od Normalizacije glasnoće: Kompresor izjednačuje stvari **unutar** jedne pjesme, dok Normalizacija glasnoće usklađuje glasnoću **između** pjesama. Njih dvoje dobro rade zajedno. Počnite s presetom i otvorite klizače samo ako želite više kontrole.

**Klizači:**

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Threshold** | Razina na kojoj kompresija počinje. Niže vrijednosti više stišću zvuk, držeći tihe i glasne dijelove bliže zajedno. | -60 do 0 dB (-20) |
| **Ratio** | Koliko se snažno glasni dijelovi zadržavaju nakon što prijeđu prag. Više vrijednosti komprimiraju jače, držeći zvuk ujednačenijim. | 1:1 do 30:1 (4:1) |
| **Attack** | Koliko brzo efekt reagira na iznenadni glasni vrh. Kratke vrijednosti hvataju tranzijente; duže ih propuštaju. | 0.1 do 1000 ms (10 ms) |
| **Release** | Koliko brzo efekt otpušta nakon što glasni dio prođe. Kratke vrijednosti mogu pumpati; duže zvuče glatkije. | 10 ms do 5 s (100 ms) |
| **Master gain** | Konačno pojačanje izlaza primijenjeno nakon obrade. Podignite ovo da povisite ukupnu glasnoću nakon što se dinamika izjednači. | -30 do +30 dB (0) |

**Preseti:**

| Preset | Što radi |
|---|---|
| **Transparent** | Jedva prisutna sigurnosna mreža. Gotovo u potpunosti čuva dinamiku i hvata samo najglasnije vrhove. |
| **Soft** | Lagano niveliranje za hi-fi slušanje kod kuće. Suptilno izglađivanje bez stiskanja glazbe. |
| **Standard** | Razumna zadana postavka za svakodnevnu reprodukciju glazbe. Prvi preset za isprobati. |
| **Heavy** | Agresivno izjednačavanje za bučna okruženja. Auto, prepuna prostorija, slušanje pri niskoj glasnoći. |
| **Voice / Podcast** | Podešeno za govor. Sporiji attack propušta sibilante, velikodušno makeup pojačanje podiže vokale. |
| **Old Recordings** | Vintage albumi i restaurirani vinil, gdje je prosječna razina ispod modernih izdanja. |
| **Late Night** | Teška kompresija plus veliko pojačanje za tiho slušanje kada su susjedi ili obitelj koja spava bitni. |
| **Movie Dialog** | Podiže govor u odnosu na glazbu i zvučne efekte u raznolikoj zvučnoj podlozi. |
| **Streaming Match** | Cilja otprilike normalizaciju glasnoće modernih streaming usluga oko -14 LUFS. |
| **Maximum Loudness** | Sve u. Pogađa limiter; očekujte stisnut, vrlo ujednačen signal. Doslovni preset maksimalne glasnoće. |

## Freeverb (reverb, osjećaj prostora)

**Što radi:** Dodaje osjećaj prostora glazbi, od male sobe do velike dvorane. Odaberite preset ili sami fino podesite suhi i mokri miks, veličinu sobe, prigušenje i širinu. Reverb je prirodni odjek koji čujete u bilo kojem stvarnom prostoru, a Freeverb ga ponovno stvara u softveru. Malo čini da ravne ili blisko snimljene snimke djeluju otvorenije i življe. Puno smješta glazbu u velik, udaljen prostor. To je kreativni efekt, pa držite mokri miks skromnim za prirodne rezultate.

**Klizači:**

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Dry mix** | Koliko se izvornog, netaknutog zvuka zadržava. Više vrijednosti ostavljaju više suhog signala u miksu. | 0 do 1 (0.0) |
| **Wet mix** | Koliko se reverberiranog zvuka dodaje. Više vrijednosti čine reverb glasnijim i očitijim. | 0 do 3 (1.0) |
| **Room size** | Veličina zamišljenog prostora. Više vrijednosti daju duži, veći rep reverba, od male sobe do katedrale. | 0 do 1 (0.5) |
| **Damp** | Koliko brzo visoke frekvencije nestaju u repu. Više vrijednosti čine reverb tamnijim i toplijim. | 0 do 1 (0.5) |
| **Width** | Stereo raspon reverba. Više vrijednosti čine prostor širim između lijevog i desnog kanala. | 0 do 1 (1.0) |

**Preseti:**

| Preset | Što radi |
|---|---|
| **Room** | Mali, tijesan prostor. Suptilna ambijentalnost koja dodaje osjećaj mjesta bez ispiranja zvuka. |
| **Studio** | Suha, kontrolirana snimateljska soba. Tek dovoljno refleksije da zvuči prirodno. |
| **Hall** | Velika koncertna dvorana. Dug, raskošan rep koji odgovara orkestralnoj i akustičnoj glazbi. |
| **Cathedral** | Ogroman, odjekujući kameni prostor. Najduži, najdramatičniji rep reverba. |
| **Plate** | Svijetli, gusti studijski plate reverb. Klasik za vokale i bubnjeve. |
| **Ambience** | Kratka, prozračna ambijentalnost. Dodaje lagani osjećaj prostora dok ostaje uglavnom suho. |

## Auto Wah (funky pomicanje filtera)

**Što radi:** Filter koji se sam pomiče gore-dolje za funky, vokalni wah zvuk. Odaberite preset ili sami postavite mokri miks, feedback, brzinu, raspon i frekvenciju. To je isto «wah» pomicanje koje pravi gitarski wah pedal, ali ovdje se pomiče sam u ritmu glazbe. Odlično zvuči na funk, disco i elektroničkim pjesmama. To je smion, očit efekt, pa malo ide daleko na svakodnevnom slušanju.

**Klizači:**

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Wet mix** | Koliko je jak wah efekt u miksu. Više vrijednosti čine pomicajući filter očitijim. | -2 do +2 (1.5) |
| **Feedback** | Koliko se izlaza vraća natrag u efekt. Više vrijednosti čine wah rezonantnijim i izraženijim. | -1 do +1 (0.5) |
| **Rate** | Koliko brzo se filter pomiče gore-dolje. Više vrijednosti daju brži, ritmičniji wah. | 0.1 do 9 Hz (2.0) |
| **Range** | Koliko daleko se filter pomiče, u oktavama. Više vrijednosti daju šire, dramatičnije pomicanje. | 0.1 do 9 oktava (4.3) |
| **Frequency** | Osnovna frekvencija oko koje se filter pomiče. Niže vrijednosti zvuče dublje; više vrijednosti zvuče svjetlije. | 1 do 1000 Hz (50) |

**Preseti:**

| Preset | Što radi |
|---|---|
| **Classic** | Uravnoteženo, klasično wah pomicanje. Dobra polazna točka za funk i rock. |
| **Slow** | Sporo, široko pomicanje koje se nježno kreće gore-dolje. Odlično za padove i duge note. |
| **Funky** | Brzo, udarno pomicanje s puno kretanja. Dodaje ritmički ugriz gitarama i sintezama. |
| **Deep** | Duboko, široko pomicanje koje počinje od niske frekvencije. Veliko i dramatično. |
| **Subtle** | Nježno, suzdržano kretanje. Dodaje karakter bez dominiranja zvukom. |
| **Resonant** | Oštar, rezonantan wah s visokim feedbackom. Vokalno i izražajno. |

## Phaser (vrtložni whoosh)

**Što radi:** Pomicajući filter koji dodaje vrtložno, huhćuće kretanje zvuku. Odaberite preset ili sami postavite feedback, brzinu, raspon i frekvenciju. Dodaje nježno kretanje i svjetlucanje bez mijenjanja nota. Suptilan je na vokalima i padovima, a dramatičan na sintezama i gitarama. Isprobajte Slow za sanjiv osjećaj ili Jet za snažan vrtlog.

**Klizači:**

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Feedback** | Koliko se izlaza vraća natrag u efekt. Više vrijednosti čine phaser rezonantnijim i izraženijim. | -1 do +1 (0.0) |
| **Rate** | Koliko brzo se filter pomiče gore-dolje. Više vrijednosti daju brže, ritmičnije phasiranje. | 0.1 do 9 Hz (1.0) |
| **Range** | Koliko daleko se filter pomiče, u oktavama. Više vrijednosti daju šire, dramatičnije pomicanje. | 0.1 do 9 oktava (4.0) |
| **Frequency** | Osnovna frekvencija oko koje se filter pomiče. Niže vrijednosti zvuče dublje; više vrijednosti zvuče svjetlije. | 1 do 1000 Hz (100) |

**Preseti:**

| Preset | Što radi |
|---|---|
| **Classic** | Uravnoteženo, klasično phaser pomicanje. Dobra polazna točka za gitare i klavijature. |
| **Slow** | Sporo, široko pomicanje koje se nježno kreće gore-dolje. Odlično za padove i duge note. |
| **Fast** | Brzo, svjetlucavo pomicanje s puno kretanja. Dodaje kretanje i energiju. |
| **Deep** | Duboko, široko pomicanje koje počinje od niske frekvencije. Veliko i dramatično. |
| **Subtle** | Nježno, suzdržano kretanje. Dodaje karakter bez dominiranja zvukom. |
| **Jet** | Intenzivno, rezonantno pomicanje s visokim feedbackom, klasični whoosh mlaznog aviona. |

## Flanger (pomicanje mlaznog aviona)

**Što radi:** Kratko, pomicajuće kašnjenje koje daje zvuku mlazni, pomicajući whoosh. Odaberite preset ili sami postavite dubinu, feedback, brzinu i kašnjenje. To je jači, metalniji rođak phasera, poznat po huhćućem pomicanju u klasičnom rocku i elektroničkoj glazbi. Suptilne postavke dodaju nježno kretanje, dok su duboke postavke dramatične i očite. Najbolje se koristi štedljivo, radi efekta.

**Klizači:**

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Depth** | Koliko je jak pomicajući efekt. Više vrijednosti čine flanging očitijim. | 0 do 100% (25) |
| **Feedback** | Koliko se izlaza vraća natrag u efekt. Više vrijednosti čine flanger rezonantnijim i metalnijim. | -99 do +99% (-50) |
| **Rate** | Koliko brzo se pomicanje kreće gore-dolje. Više vrijednosti daju brže, svjetlucavije kretanje. | 0 do 10 Hz (0.25) |
| **Delay** | Osnovno vrijeme kašnjenja na kojem se pomicanje gradi. Više vrijednosti daju dublji, šuplji karakter. | 0 do 4 ms (2.0) |

**Preseti:**

| Preset | Što radi |
|---|---|
| **Classic** | Uravnoteženi, klasični flanger. Dobra polazna točka za gitare i klavijature. |
| **Subtle** | Nježno, suzdržano pomicanje. Dodaje kretanje bez dominiranja zvukom. |
| **Deep** | Duboko, teško pomicanje s jakim feedbackom. Veliko i dramatično. |
| **Jet** | Intenzivno pomicanje s pozitivnim feedbackom, klasični whoosh mlaznog aviona. |
| **Fast** | Brzo, svjetlucavo pomicanje s puno kretanja i energije. |
| **Wide** | Sporo, široko pomicanje s dugim kašnjenjem. Raskošno i prostrano. |

## Echo (ponavljanja)

**Što radi:** Ponavlja zvuk kao nestajuće odjeke za osjećaj prostora i dubine. Odaberite preset ili sami postavite mokri miks, feedback i kašnjenje. To je poput dozivanja u kanjonu: zvuk se vraća jednom ili više puta nakon kratke pauze. Jedno kratko ponavljanje dodaje tijelo i retro osjećaj, dok duža ponavljanja s više feedbacka stvaraju prostrane, tragajuće repove. Preset Ping Pong odbija ponavljanja između vašeg lijevog i desnog uha, što je zabavno na slušalicama. Držite mokri miks skromnim tako da odjeci podupiru glazbu umjesto da je prekrivaju.

**Klizači:**

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Wet mix** | Koliko su glasni odjeci u usporedbi s izvornim zvukom. Više vrijednosti čine da se ponavljanja više ističu. | -2 do +2 (0.6) |
| **Feedback** | Koliko se puta odjek ponavlja. Više vrijednosti daju više ponavljanja koja duže nestaju. | -1 do +1 (0.5) |
| **Delay** | Vrijeme između odjeka. Kraće vrijednosti daju čvrst slap-back; duže vrijednosti daju razmaknuta ponavljanja. | 0.01 do 2 s (0.4) |

**Preseti:**

| Preset | Što radi |
|---|---|
| **Slapback** | Jedno, čvrsto ponavljanje odmah iza zvuka. Klasični rockabilly slap-back. |
| **Room** | Kratak, prirodan odjek, poput male sobe. Dodaje prostor bez razmazivanja zvuka. |
| **Tape** | Topla, srednja ponavljanja koja postupno nestaju, poput starog tape delaya. |
| **Dub** | Duga, teška ponavljanja s jakim feedbackom. Veliko, dubby i prostrano. |
| **Ping Pong** | Odjeci se odbijaju između lijevog i desnog zvučnika za širok stereo efekt. |
| **Long** | Spora, široko razmaknuta ponavljanja koja se pružaju daleko iza zvuka. |

## Chorus (deblji, širi zvuk)

**Što radi:** Zgušnjava i proširuje zvuk slaganjem pomicajuće kopije preko izvornika. Odaberite preset ili sami postavite mokri/suhi miks, dubinu, brzinu i feedback. Čini da jedan instrument ili glas zvuči kao nekoliko koji sviraju zajedno, dodavanjem blago raštimanih, pomicajućih kopija. Ovo dodaje bogatstvo i nježno svjetlucanje. Suptilne postavke zagriju stvari, dok jake postavke zvuče raskošno i sanjivo. Popularan je na gitarama, klavijaturama i vokalima.

**Klizači:**

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Wet/Dry** | Koliko chorusa čujete u usporedbi s izvornim zvukom. Više vrijednosti čine efekt očitijim. | 0 do 100% (50) |
| **Depth** | Koliko daleko visina titra gore-dolje. Više vrijednosti daju deblji, svjetlucaviji zvuk. | 0 do 100% (25) |
| **Rate** | Koliko brzo se svjetlucanje kreće. Sporije brzine zvuče nježno i raskošno; brže brzine zvuče više poput vibrata. | 0 do 10 Hz (1.1) |
| **Feedback** | Koliko se efekta vraća natrag u sebe. Više vrijednosti čine chorus rezonantnijim i intenzivnijim. | -99 do +99% (25) |

**Preseti:**

| Preset | Što radi |
|---|---|
| **Subtle** | Nježno zgušnjavanje koje dodaje toplinu bez privlačenja pozornosti na sebe. |
| **Lush** | Bogat, klasičan chorus. Odlična svestrana postavka za gitare i klavijature. |
| **Ensemble** | Puno, slojevito svjetlucanje koje čini da jedan instrument zvuči kao nekoliko. |
| **Vibrato** | Potpuno mokro s brzim ritmom, za titrajući vibrato umjesto suptilnog chorusa. |
| **Wide** | Sporo, široko svjetlucanje koje otvara stereo sliku. Prostrano i sanjivo. |
| **Twelve-String** | Svijetlo, rezonantno svjetlucanje koje podsjeća na dvanaeststrunu gitaru. |

## Distorzija (hrapavost i oštrina)

**Što radi:** Dodaje hrapavost i oštrinu preopterećivanjem zvuka. Odaberite preset ili sami postavite drive, izlaz i ton. Namjerno pogrubljuje zvuk, od tople, hrapave oštrine do slomljenog, mutnog tona. To je kreativni, zabavni efekt, a ne način poboljšanja kvalitete, pa ga koristite u malim količinama. Zabavan je na elektroničkim, rock i eksperimentalnim pjesmama. Spustite Output ako teški preset postane preglasan.

**Klizači:**

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Drive** | Koliko jako je zvuk distorziran. Više vrijednosti su hrapavije i agresivnije. | 0 do 100% (15) |
| **Output** | Izlazna razina nakon distorzije. Spustite je ako teška postavka postane preglasna. | -60 do 0 dB (-18) |
| **Tone** | Odsijeca visoke tonove prije distorzije. Niže vrijednosti zvuče tamnije i toplije. | 100 do 8000 Hz (8000) |
| **Center** | Oko koje se frekvencije distorzija fokusira. Pomiče karakter svjetlije ili tamnije. | 100 do 8000 Hz (2400) |
| **Width** | Koliko je širok taj fokus. Uski zvuči oštro i nazalno; širok zvuči puno i otvoreno. | 100 do 8000 Hz (2400) |

**Preseti:**

| Preset | Što radi |
|---|---|
| **Warm Drive** | Lagana, topla hrapavost koja dodaje oštrinu bez puno mijenjanja karaktera. |
| **Crunch** | Klasičan hrskavi overdrive, udaran i ritmičan. |
| **Overdrive** | Svijetli, pokretani ton s puno ugriza. Odlično za lead zvukove. |
| **Fuzz** | Debeo, zasićen fuzz. Težak i pun harmonika. |
| **Metal** | Čvrst, srednje-fokusiran ton visokog pojačanja za agresivne, teške zvukove. |
| **Screamer** | Overdrive s pojačanim srednjima koji se probija, poput tube screamera. |
| **LoFi** | Zdrobljena, uskopojasna distorzija za hrapav lo-fi karakter. |

## Rotate (rotirajući stereo)

**Što radi:** Rotira zvuk oko stereo polja za rotacijski, vrtložni efekt. Odaberite preset ili sami postavite brzinu. Polako pomiče zvuk oko vaših lijevog i desnog kanala, pomalo poput rotirajućeg zvučnika, što dodaje vrtložni, hipnotički osjećaj. Spore postavke su nježne i široke, dok su brze postavke vrtoglave i očite. To je stereo efekt, pa je najuočljiviji na slušalicama ili dobro postavljenim zvučnicima.

**Klizač:**

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Rate** | Koliko brzo se zvuk vrti oko stereo polja. Negativne vrijednosti vrte u drugom smjeru; nula ga drži mirnim. | -5 do +5 Hz (1.0) |

**Preseti:**

| Preset | Što radi |
|---|---|
| **Slow Pan** | Sporo, nježno kretanje s jedne strane na drugu. Suptilno i široko. |
| **Sway** | Ustaljeno lijevo-desno njihanje. Dodaje nježno kretanje stereo slici. |
| **Rotary** | Srednji vrtnja koji podsjeća na rotirajući zvučnik. |
| **Fast Spin** | Brza vrtnja oko stereo polja za vrtoglavi, vrtložni efekt. |
| **Reverse** | Srednja vrtnja u suprotnom smjeru. |
| **Whirl** | Vrlo brz vrtlog. Intenzivno i dezorijentirajuće. |

## Crossfeed (prirodan zvuk na slušalicama)

Na zvučnicima, svako vaše uho čuje i lijevi i desni zvučnik, samo u malo drugačijim vremenima i glasnoćama. Na slušalicama, to prirodno miješanje je nestalo: vaše lijevo uho čuje samo lijevi kanal, a desno uho samo desni. Ovaj «super stereo» može učiniti da glazba djeluje kao da je podijeljena unutar vaše glave, a snimke s tvrdim panoramiranjem, gdje instrument sjedi potpuno na jednoj strani, mogu djelovati neprirodno ili umarajuće na dugim slušanjima.

Crossfeed to popravlja miješanjem male, filtrirane količine svakog kanala u drugi, s malenim kašnjenjem i nježnim odsijecanjem visokih frekvencija. To je blizu načina na koji zvuk iz stvarnih zvučnika dopire do oba vaša uha, uključujući način na koji vaša glava blago zasjenjuje daljnje uho. Rezultat je prirodnija, zvučnicima nalik slika koja sjedi malo ispred vas umjesto unutar vaše glave, i smanjuje umor od slušanja na dugim sesijama. Flacbox koristi dobro poznatu **bs2b (Bauer stereophonic-to-binaural)** metodu, cijenjeni open-source crossfeed koji koriste mnogi audiofilski reproduktori. O algoritmu možete pročitati na [bs2b projektnoj stranici](https://bs2b.sourceforge.net/).

**Cutoff** kontrolira koliko toplo miješanje zvuči, a **Feed level** kontrolira koliko je jako. Preseti pokrivaju klasične bs2b razine, od jedva prisutnog dodira do čvrstog, zvučnicima nalik miješanja. Crossfeed je efekt za slušalice, pa ga ostavite isključenim kada slušate na zvučnicima.

**Klizači:**

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Cutoff** | Postavlja gdje prelijevanje između kanala počinje odsijecati. Niže vrijednosti daju topliji, izraženiji efekt. | 300 do 2000 Hz (700) |
| **Feed level** | Kontrolira koliko jednog kanala prelijeva u drugi. Više vrijednosti proizvode zvuk sličniji zvučnicima. | 1 do 15 dB (4.5) |

**Preseti:**

| Preset | Što radi |
|---|---|
| **Subtle** | Jedva prisutan crossfeed za ležerno slušanje. Ublažava tvrdo panoramiran stereo bez mijenjanja tonalne ravnoteže. |
| **Chu Moy** | Klasična univerzalna zadana postavka. Uravnotežena i lagano topla, radi na gotovo bilo kojem materijalu. Počnite ovdje. |
| **Strong** | Jače prelijevanje za mikseve s tvrđim panoramiranjem. Očitije stereo suženje. |
| **Jan Meier** | Popularan među entuzijastima slušalica. Šire prelijevanje, prezentacija sličnija zvučnicima, blago podizanje basa. |
| **Speaker-like** | Podešeno za najprirodniju reprodukciju u stilu zvučnika preko slušalica. |
| **Vintage Stereo** | Agresivan crossfeed podešen za mikseve iz 1960-ih i 1970-ih s tvrdo panoramiranima bubnjevima i vokalima. |

## Obrada signala: izgradite svoj vlastiti DSP lanac

Osim gotovih efekata, Flacbox vam omogućuje izgradnju vlastitog lanca u **Postavke > Audio player > Obrada signala**. Kao što aplikacija objašnjava kada je lanac prazan: *«Dodirnite + da dodate efekt. Uključite ili isključite svaki njegovim prekidačem, povucite za promjenu redoslijeda, dodirnite za uređivanje njegovih parametara i dugo pritisnite za dupliciranje ili brisanje.»*

**Redoslijed je bitan**: filter prije distorzije zvuči drugačije od istog filtera nakon nje. Također možete usmjeriti cijeli lanac na **Sve kanale**, **Lijevi kanal** ili **Desni kanal**.

U nastavku je svaki blok, s vlastitim tekstom aplikacije za svaki klizač i svaki preset.

### Gain (podešavanje razine)

Podiže ili spušta razinu na jednoj točki u lancu.

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Gain** | Pojačava ili reže razinu na ovoj točki u lancu. Koristite ga da nadoknadite razinu nakon drugih efekata, ili da pokrenete one koji slijede. | -24 do +24 dB (0) |

| Preset | Što radi |
|---|---|
| **Unity** | Bez promjene razine. Neutralna polazna točka. |
| **Cut** | Veliki rez. Ukroćuje glasan izvor, ili stvara prostor prije efekata koji slijede. |
| **Trim** | Nježan rez da malo povuče razinu natrag. |
| **Lift** | Skromno pojačanje da podigne tih izvor. |
| **Boost** | Snažno pojačanje za tih materijal, ili da jače pokrene sljedeće efekte. |
| **Max** | Maksimalno pojačanje. Glasno, pazite na clipping kasnije u lancu. |

### Low Pass (uklanja visoke tonove)

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Cutoff** | Postavlja gdje filter počinje odsijecati visoke tonove. Spustite ga da potamnite i omekšate zvuk; podignite ga prema vrhu da se potpuno otvori. | 20 Hz do 20 kHz (20 kHz) |
| **Resonance** | Naglašava frekvencije točno na cutoffu. Držite je niskom za čisto odsijecanje; podignite je za šiljast, zviždeći rub. | 0.1 do 10 (0.707) |

| Preset | Što radi |
|---|---|
| **Air** | Odsijeca samo sam vrh. Skida malo oštrine bez zatupljivanja zvuka. |
| **Warm** | Nježno odsijecanje visokih tonova za topliji, zaobljeniji ton. |
| **Mellow** | Primjetno omekšano. Povlači svjetlinu natrag za opušten osjećaj. |
| **Muffled** | Tamno i prigušeno, kao da se čuje kroz zid. |
| **Telephone** | Uzak, rezonantan vrh nisko u rasponu. Tanak, telefonu nalik glas. |

### High Pass (uklanja niske tonove)

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Cutoff** | Postavlja gdje filter počinje odsijecati niske tonove. Podignite ga da stanjite niski kraj i uklonite tutnjavu; spustite ga prema dnu da se potpuno otvori. | 20 Hz do 20 kHz (20 Hz) |
| **Resonance** | Naglašava frekvencije točno na cutoffu. Držite je niskom za čisto odsijecanje; podignite je za šiljast, zviždeći rub. | 0.1 do 10 (0.707) |

| Preset | Što radi |
|---|---|
| **Rumble Cut** | Uklanja subsonic tutnjavu i DC offset bez diranja čujnog niskog kraja. |
| **Tighten** | Odsijeca bučne niske frekvencije za čvršći, čišći bas. |
| **Thin** | Reže toplinu i tijelo, ostavljajući lakši, tanji zvuk. |
| **Radio** | Ostaju samo srednji i visoki tonovi, poput malog radijskog zvučnika. |
| **Telephone** | Uzak, rezonantan vrh visoko u rasponu. Tanak, telefonu nalik glas. |

### Band Pass (zadržava srednji pojas)

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Center** | Postavlja frekvenciju koju filter propušta. Sve iznad i ispod nje se odsijeca. Pomičite je da izdvojite bas, srednje tonove ili visoke tonove. | 20 Hz do 20 kHz (1 kHz) |
| **Resonance** | Kontrolira koliko je pojas širok. Niske vrijednosti propuštaju širok raspon; podignite je da suzite na centar za oštar, rezonantan ton. | 0.1 do 10 (0.707) |

| Preset | Što radi |
|---|---|
| **Voice** | Širok pojas oko srednjeg raspona gdje sjedi većina vokala. Neutralna polazna točka. |
| **Bass** | Izolira niski kraj, ostavljajući samo bas i kick. |
| **Body** | Fokusira se na niske-srednje za toplo, kutijasto tijelo. |
| **Presence** | Podiže gornje-srednje za jasnoću i prisutnost. |
| **Telephone** | Uzak srednji pojas. Tanak, telefonu nalik zvuk. |
| **Wah** | Vrlo uzak, rezonantan vrh. Pomičite centar za wah efekt. |

### Notch (uklanja jedan uzak pojas)

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Frequency** | Postavlja frekvenciju koju filter uklanja. Sve iznad i ispod nje prolazi. Podesite je na brujanje ili rezonanciju da je izrežete. | 20 Hz do 20 kHz (60 Hz) |
| **Resonance** | Kontrolira koliko je rez širok. Niske vrijednosti izvlače širok raspon; podignite je da uklonite samo točkasti pojas i ostavite ostatak netaknutim. | 0.1 do 10 (8.0) |

| Preset | Što radi |
|---|---|
| **Mains Hum 60** | Uklanja 60 Hz električno brujanje (sjevernoameričko napajanje). Neutralna polazna točka. |
| **Mains Hum 50** | Uklanja 50 Hz električno brujanje (europsko i drugo napajanje). |
| **Rumble** | Reže niskofrekventnu tutnjavu ili rezonanciju bez stanjivanja cijelog donjeg kraja. |
| **Mud** | Izvlači nisko-srednji mulj za čišći, jasniji zvuk. |
| **Boxy** | Uklanja kutijast srednji ton. |
| **Harsh** | Ukroćuje oštar, prodoran vrh u gornjim-srednjima. |

### Peaking (parametarski EQ pojas)

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Frequency** | Centar pojasa za pojačanje ili rezanje. Pomičite ga da nađete frekvenciju koju želite oblikovati. | 20 Hz do 20 kHz (1 kHz) |
| **Gain** | Koliko pojačati ili rezati na centru. Pozitivno podiže pojas; negativno ga izvlači. | -15 do +15 dB (0) |
| **Q factor** | Postavlja koliko je pojas širok. Niske vrijednosti oblikuju široko područje; visoke vrijednosti suzuju za kirurške, točkaste promjene. | 0.1 do 10 (1.0) |

| Preset | Što radi |
|---|---|
| **Presence** | Široko podizanje gornjih-srednjih za jasnoću i prisutnost. Neutralna polazna točka. |
| **Warmth** | Široko podizanje niskih-srednjih koje dodaje tijelo i toplinu. |
| **Vocal Boost** | Podiže srž vokalnog raspona da izbaci glasove naprijed. |
| **Cut Mud** | Izvlači kutijast nisko-srednji mulj za čišći zvuk. |
| **Tame Harsh** | Uzak rez da ukroti oštar, prodoran vrh. |
| **Punch** | Nisko pojačanje koje dodaje udar i utjecaj niskom kraju. |
| **Sub Boost** | Duboko pojačanje na samom dnu za dodatnu težinu sub-basa. |
| **Air** | Široko podizanje na vrhu za otvoren, prozračan sjaj. |
| **Clarity** | Podiže visoke-srednje da doda definiciju i oštrinu. |
| **De-Ess** | Uzak rez u rasponu sibilanata da ukroti oštre S zvukove. |
| **De-Boom** | Reže bučno niskofrekventno nakupljanje za čvršći niski kraj. |
| **Scoop** | Širok pad srednjeg raspona za izvučen, moderan ton. |

### Low Shelf (kontrola basa i pojačanje basa)

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Frequency** | Postavlja kut ispod kojeg shelf djeluje. Sve ispod njega se zajedno pojačava ili reže. | 20 do 2000 Hz (200) |
| **Gain** | Koliko podignuti ili spustiti niski kraj. Pozitivno dodaje težinu i toplinu; negativno ga stanjuje. | -15 do +15 dB (0) |

| Preset | Što radi |
|---|---|
| **Warmth** | Nježno podizanje niskog kraja za toplinu i tijelo. Neutralna polazna točka. |
| **Bass Boost** | Čvrsto pojačanje basa za težinu i udar. |
| **Fullness** | Ispunjava niske-srednje za puniji, zaobljeniji zvuk. |
| **Trim Bass** | Skroman rez da olakša miks bogat basom. |
| **Cut Lows** | Snažan rez da stanji ili de-boom-a niski kraj. |
| **Big Bottom** | Veliko pojačanje niskog kraja za maksimalnu težinu i tutnjavu. |

### High Shelf (kontrola visokih tonova)

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Frequency** | Postavlja kut iznad kojeg shelf djeluje. Sve iznad njega se zajedno pojačava ili reže. | 1 do 20 kHz (8 kHz) |
| **Gain** | Koliko podignuti ili spustiti visoki kraj. Pozitivno dodaje svjetlinu i zrak; negativno izglađuje i potamnjuje. | -15 do +15 dB (0) |

| Preset | Što radi |
|---|---|
| **Presence** | Nježno podizanje visokog kraja za jasnoću i detalj. Neutralna polazna točka. |
| **Air** | Otvara sam vrh za prozračan, otvoren zvuk. |
| **Bright** | Snažno pojačanje za oštar, svijetao, istaknut ton. |
| **Soften** | Skroman rez da skine oštrinu s prodornih visokih tonova. |
| **Tame Highs** | Snažan rez da potamni i izgladi previše svijetao zvuk. |
| **Sparkle** | Veliko pojačanje gornjeg kraja za maksimalno svjetlucanje i sjaj. |

### Soft Clip (topla saturacija)

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Drive** | Gura signal jače u waveshaper. Male količine dodaju nježnu toplinu; velike količine zaobljuju vrhove u gustu saturaciju i hrapavost. | 0 do 40 dB (0) |

| Preset | Što radi |
|---|---|
| **Warm** | Dodir drivea za nježnu, analognu toplinu. |
| **Drive** | Primjetna saturacija koja zgušnjava i boji zvuk. |
| **Crunch** | Teški drive s čujnim hrskavim rubom. |
| **Fuzz** | Debela, mutna distorzija. Vrhovi su jako stisnuti. |
| **Destroy** | Maksimalni drive. Agresivna, potpuno zasićena hrapavost. |

### Bit Crusher (retro lo-fi)

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Bit depth** | Postavlja koliko bitova opisuje svaki uzorak. Manje bitova znači grublje korake i više kvantizacijskog šuma, za hrskav, hrapav digitalni zvuk. | 1 do 16 bitova (16) |
| **Sample rate** | Podsempira audio. Na sto posto frekvencija je netaknuta; spustite je da svaki uzorak drži duže, zatupljujući visoke tonove i dodajući oštar, aliasiran rub. | 1% do 100% (100%) |

| Preset | Što radi |
|---|---|
| **Vintage** | Suptilan pad kvalitete, poput ranog digitalnog samplera. |
| **LoFi** | Klasičan 8-bitni, half-rate lo-fi. Zrnat i retro. |
| **Crunch** | Teže drobljenje s čujnim hrskavim rubom. |
| **Gritty** | Grubo i hrapavo. Koraci između razina su očiti. |
| **Destroy** | Ekstremna redukcija. Oštro, slomljeno, jedva prepoznatljivo. |

### Ring Modulator (metalni i robotski tonovi)

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Carrier** | Postavlja frekvenciju tona kojim se signal množi. Nekoliko herca daje tremolo titranje; više frekvencije dodaju metalne, zvonaste i robotske prizvuke. | 1 do 4000 Hz (440) |
| **Mix** | Miješa modulirani zvuk s izvornim. Na nula posto čujete samo suhi signal; na sto posto samo potpuno modulirani ton. | 0% do 100% (0%) |

| Preset | Što radi |
|---|---|
| **Tremolo** | Vrlo nizak carrier pretvara ga u amplitudni tremolo, titrajući glasnoću. |
| **Robot** | Srednji carrier dodaje zveckave prizvuke za klasičan efekt robotskog glasa. |
| **Metallic** | Gusti, neharmonijski prizvuci za oštar, metalni ton. |
| **Bell** | Viši carrier daje svijetlo, zvonasto zvonjenje. |
| **Alien** | Potpuno mokro s visokim carrierom. Ekstremno, izvanzemaljsko, jedva prepoznatljivo. |

### Tremolo (titranje glasnoće)

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Rate** | Postavlja koliko brzo glasnoća pulsira. Sporije brzine daju glatko njihanje; brže brzine daju brzo mucanje. | 0.1 do 20 Hz (5) |
| **Depth** | Postavlja koliko glasnoća pada na svakom pulsu. Na nula posto razina je ustaljena; na sto posto pada sve do tišine. | 0% do 100% (0%) |

| Preset | Što radi |
|---|---|
| **Gentle** | Sporo, plitko njihanje. Suptilno kretanje bez privlačenja pozornosti. |
| **Classic** | Klasičan tremolo pojačala: srednja brzina i umjerena dubina. |
| **Deep** | Snažan, dubok puls koji gotovo pada do tišine na svakom ciklusu. |
| **Fast** | Brzo treperenje za svjetlucav, nervozan osjećaj. |
| **Chop** | Brzo i pune dubine. Tvrd, mucav rez. |

### Delay (echo)

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Time** | Postavlja pauzu prije svakog odjeka. Kratka vremena daju čvrst slapback; duža vremena razmiču ponavljanja dalje. | 0.01 do 2 s (0.25) |
| **Feedback** | Postavlja koliko se svakog odjeka vraća natrag. Niske vrijednosti daju jedno ponavljanje; više vrijednosti grade dug, tragajući niz odjeka. | 0 do 0.95 (0.4) |
| **Mix** | Miješa odjeke s izvornim. Na nula posto čujete samo suhi signal; na sto posto samo odjeke. | 0% do 100% (0%) |

| Preset | Što radi |
|---|---|
| **Slapback** | Jedan kratak odjek, čvrsto uz izvornik. Rockabilly i udvajanje vokala. |
| **Echo** | Klasičan echo: jasno ponavljanje s nekoliko tragajućih repova. |
| **Ping** | Brzo, odbijajuće ponavljanje koje dodaje ritmičko kretanje. |
| **Ambient** | Duža, mekša ponavljanja koja se ispiru u prostran rep. |
| **Dub** | Visok feedback za duge, dubby kaskade odjeka. |
| **Cavern** | Duga, duboka ponavljanja, poput zvuka koji odjekuje kroz ogroman prostor. |

### Stereo Width (suzi ili proširi)

| Kontrola | Što radi | Raspon (zadano) |
|---|---|---|
| **Width** | Suzuje ili proširuje stereo sliku. Nula posto sabija u mono, sto posto ostavlja je netaknutu, a više vrijednosti guraju strane šire. Utječe samo na stereo pjesme na cilju Svi kanali. | 0% do 200% (100%) |

| Preset | Što radi |
|---|---|
| **Wide** | Nježno proširenje koje otvara stereo sliku. Neutralna polazna točka. |
| **Wider** | Jače širenje za veliko, impresivno stereo polje. |
| **Max** | Maksimalna širina. Vrlo široko, ali pazite na probleme s mono-kompatibilnošću. |
| **Narrow** | Povlači strane unutra za čvršću, više centriranu sliku. |
| **Focused** | Gotovo centrirano, s tek naznakom stereo. |
| **Mono** | Potpuno sabijeno u mono. Oba zvučnika sviraju isti signal. |

## Kako sve to radi ispod haube (jednostavna verzija)

- **Motori:** odaberete jedan u Postavke > Audio player > Motor reprodukcije: **Standard** (sustav), **Universal** (FFmpeg) ili **Sound FX** (**BASS™ motor** tvrtke [Un4seen Developments](https://www.un4seen.com/)). Motor koji odaberete određuje koji se formati reproduciraju, a efekti, ekvalizator i DSP lanac rade samo u Sound FX motoru.
- **Formati:** BASS™ motor dodaje FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus i modul (tracker) glazbu povrh sustavskih i FFmpeg formata.
- **Efekti:** ekvalizator, kompresor i većina efekata koriste BASS™ dodatke za efekte. Freeverb je Freeverb reverb. Chorus, Flanger i Distorzija koriste klasične DirectX efekte s vlastitim kontrolama.
- **Normalizacija glasnoće:** EBU R128 leveler glasnoće uživo (standard glasnoće koji se koristi u emitiranju i streamingu).
- **Crossfeed:** bs2b (Bauer) crossfeed, pokrenut unutar BASS™ motora.
- **DSP lanac:** vaši prilagođeni blokovi, primijenjeni točno onim redoslijedom koji postavite, na svim kanalima ili samo na jednoj strani.
- **Izlaz:** možete postaviti frekvenciju uzorkovanja, broj kanala i veličinu međuspremnika da odgovaraju vašoj opremi.

Budući da sve ovo radi uživo dok glazba svira, efekti:

- Rade u **stvarnom vremenu** na svemu, uključujući datoteke u oblaku, streamove i modul glazbu.
- **Nikada ne mijenjaju ni ponovno spremaju** vaše datoteke. Isključite efekt i izvornik se vraća.
- **Pamte vaše postavke** za svaki efekt.
- Mogu se **slobodno miješati i kombinirati**, jer je svaki zaseban.

## Jednostavni recepti za isprobati

**Svakodnevno slušanje**

- **Više basa, čisto:** Ekvalizator > Bass Booster, zatim spustite Predpojačalo za 1 do 2 dB. Ili dodajte DSP Low Shelf na Bass Boost.
- **Ujednačena glasnoća kroz mješoviti popis pjesama:** Normalizacija glasnoće > Standard, plus Kompresor > Soft.
- **Nježno ukupno poliranje:** Kompresor > Transparent, plus Normalizacija glasnoće > Light.
- **Jasniji vokali:** Ekvalizator > Vocal Booster, ili DSP Peaking blok na Vocal Boost.
- **Puniji zvuk na malim zvučnicima telefona:** Ekvalizator > Small Speakers.

**Slušalice**

- **Ljepše, manje umarajuće na slušalicama:** Crossfeed > Chu Moy ili Jan Meier.
- **Širi zvuk na slušalicama:** DSP Stereo Width > Wide, plus Crossfeed > Chu Moy.
- **Popravite tvrdo panoramirane ploče iz 1960-ih i 1970-ih:** Crossfeed > Vintage Stereo.
- **Malo zraka i prostora:** Freeverb > Ambience, držano nisko, plus Crossfeed > Subtle.

**Tihi trenuci i govorni audio**

- **Kasnonoćno tiho slušanje:** Normalizacija glasnoće > Night, plus Kompresor > Late Night.
- **Podcasti i audioknjige:** Kompresor > Voice / Podcast, plus Ekvalizator > Spoken Word.
- **Najglasniji, najujednačeniji zvuk u bučnom autu:** Normalizacija glasnoće > Strong, plus Kompresor > Heavy.

**Rješavanje problema**

- **Ukrotite oštru, svijetlu snimku:** Ekvalizator > Treble Reducer, ili DSP Peaking blok na Tame Harsh.
- **Uklonite električno brujanje:** DSP lanac > Notch > Mains Hum 60 (ili Mains Hum 50 u Europi).
- **Čvršći, čišći bas:** DSP High Pass > Tighten, da izrežete bučni niski kraj.
- **Manje boom-a u miksu bogatom basom:** DSP Low Shelf > Trim Bass, ili Peaking > De-Boom.

**Kreativno i zabavno**

- **Topao, prostoran osjećaj:** Freeverb > Hall, držano nisko.
- **Sanjive, prostrane gitare:** Chorus > Wide, plus Echo > Long.
- **Retro lo-fi:** DSP lanac > Bit Crusher (LoFi) u Soft Clip (Warm).
- **Funky kretanje na elektroničkim pjesmama:** Auto Wah > Funky, ili Phaser > Fast.
- **Klasično pomicanje mlaznog aviona:** Flanger > Jet.

## Česta pitanja

{{% details title="Koji zvučni motor Flacbox koristi?" closed="true" %}}
Odaberete jedan Motor reprodukcije u Postavke > Audio player: Standard (Appleov sustavski motor), Universal (FFmpeg motor) ili Sound FX (BASS™ motor tvrtke Un4seen Developments, un4seen.com). Motor koji odaberete određuje koji se formati datoteka reproduciraju. Sound FX je onaj koji reproducira dodatne formate poput FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus i MOD ili tracker glazbe, i to je jedini motor koji pruža efekte uživo, 10-pojasni ekvalizator i DSP lanac. Da biste koristili efekte, postavite Motor reprodukcije na Sound FX.
{{% /details %}}

{{% details title="Može li Flacbox reproducirati MOD, XM, IT i drugu tracker ili modul glazbu?" closed="true" %}}
Da. BASS™ motor ima ugrađen modul reproduktor koji učitava MOD, XM, IT, S3M, MTM, UMX i MO3 datoteke i uživo ponovno gradi pjesmu iz njezinih obrazaca i zvukova instrumenata, onako kako se tracker glazba treba reproducirati. Obični iPhone reproduktori to ne mogu. Efekti i ekvalizator rade i na modul glazbi.
{{% /details %}}

{{% details title="Podržava li Flacbox DSD i visokorezolucijske datoteke?" closed="true" %}}
Da. Flacbox reproducira DSD datoteke (DSF i DFF) kroz BASS™ motor koristeći DSD preko PCM-a tako da rade na normalnom izlaznom hardveru, plus FLAC, WavPack, Monkey's Audio (APE), Musepack i TrueAudio za lossless reprodukciju.
{{% /details %}}

{{% details title="Koje zvučne efekte Flacbox ima?" closed="true" %}}
10-pojasni ekvalizator, Normalizaciju glasnoće, Kompresor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distorziju, Rotate i Crossfeed, plus izgradite-svoj DSP lanac s filterima, shelfovima, gainom, soft clipom, bit crusherom, ring modulatorom, tremolom, delayem i stereo širinom. Svaki je zaseban i može se kombinirati s ostalima.
{{% /details %}}

{{% details title="Što je preset?" closed="true" %}}
Preset je gotova postavka za efekt. Umjesto da sami pomičete klizače, dodirnete preset i zvuk se promijeni da odgovara. Svaki efekt u Flacboxu ima nekoliko preseta, a ovaj vodič navodi što svaki od njih radi. Ako pomaknete klizač nakon odabira preseta, efekt prikazuje «Manual» da vam kaže da sada koristi vaše vlastite vrijednosti.
{{% /details %}}

{{% details title="Kako otvoriti audio efekte u Flacboxu?" closed="true" %}}
Otvorite Now Playing reproduktor, dodirnite gumb ⋯ (Više) i odaberite Audio efekti. Ili idite na Postavke > Audio player > Audio efekti. Dodirnite efekt, uključite njegov prekidač i odaberite preset, ili otvorite klizače da fino podesite.
{{% /details %}}

{{% details title="Gdje je ekvalizator i koje su najbolje postavke?" closed="true" %}}
Idite na Postavke > Audio player > Audio ekvalizator. Ima 10 pojasa od 32 Hz do 16 kHz, svaki od -12 do +12 dB, plus Predpojačalo od -24 do +24 dB i 22 preseta. Za više basa koristite Bass Booster. Za jasnije glasove koristite Vocal Booster ili Pop. Za svjetliji zvuk koristite Treble Booster. Zatim prilagodite pojedine pojaseve po ukusu.
{{% /details %}}

{{% details title="Kako pojačati bas u Flacboxu?" closed="true" %}}
Dva laka načina. U Audio ekvalizatoru odaberite Bass Booster (ili podignite pojaseve 32 Hz i 64 Hz za nekoliko dB). Ili, u Obradi signala, dodajte Low Shelf blok postavljen na Bass Boost. U oba slučaja, spustite Predpojačalo ili dodajte Gain blok za 1 do 2 dB kako bi bas ostao čist i ne distorzirao.
{{% /details %}}

{{% details title="Koji je preset ekvalizatora najbolji za moju glazbu?" closed="true" %}}
Rock i Electronic dodaju energiju sa snažnim niskim i visokim tonovima. Acoustic, Jazz i Classical ostaju topli i prirodni. Pop i Vocal Booster guraju glasove naprijed. Bass Booster i Hip-Hop dodaju težinu. Deep i Loudness zvuče punije pri niskoj glasnoći. Počnite s onim koji odgovara vašem žanru, zatim fino podesite.
{{% /details %}}

{{% details title="Što je Normalizacija glasnoće i kako se razlikuje od ReplayGaina?" closed="true" %}}
Čini da svaka pjesma svira otprilike jednako glasno. Mjeri stvarnu glasnoću koristeći EBU R128 standard (u LUFS, poput streaming usluga) i prilagođava svaku pjesmu prema vašem cilju, s granicom maksimalnog pojačanja. Za razliku od ReplayGaina, ne treba nikakve oznake u vašim datotekama i radi na bilo kojem izvoru, uživo, bez mijenjanja audija. Preseti: Light, Standard, Strong i Night.
{{% /details %}}

{{% details title="Što je Crossfeed i trebam li ga koristiti?" closed="true" %}}
Crossfeed miješa malo lijevog i desnog kanala zajedno tako da slušalice djeluju više poput stvarnih zvučnika i manje kao da je zvuk zaglavljen u vašoj glavi. Namijenjen je samo za slušalice, pa ga isključite za zvučnike. Flacbox koristi bs2b (Bauer) metodu, s presetima poput Chu Moy i Jan Meier.
{{% /details %}}

{{% details title="Koja je razlika između Kompresora i Normalizacije glasnoće?" closed="true" %}}
Normalizacija glasnoće usklađuje glasnoću između različitih pjesama. Kompresor izjednačuje glasne i tihe dijelove unutar jedne pjesme. Rješavaju različite probleme i dobro rade zajedno, osobito u autu ili na bučnom mjestu.
{{% /details %}}

{{% details title="Što je Obrada signala (DSP) lanac?" closed="true" %}}
To je izgradite-svoju polica u Postavke > Audio player > Obrada signala. Dodajte blokove poput filtera, shelfova, gaina, soft clipa, bit crushera, ring modulatora, tremola, delaya i stereo širine, poredajte ih bilo kojim redoslijedom, uključite ili isključite svaki i usmjerite lanac na sve kanale, lijevi ili desni. Budući da je redoslijed bitan, možete dizajnirati točno zvuk koji želite.
{{% /details %}}

{{% details title="Koja je razlika između Ekvalizatora, efekata i DSP lanca?" closed="true" %}}
Ekvalizator je jednostavna 10-pojasna kontrola tona. Audio efekti su gotovi alati (kompresor, reverb, echo itd.) s presetima. DSP lanac je gdje gradite vlastiti redoslijed efekata od pojedinačnih blokova. Možete pokrenuti sva tri istovremeno.
{{% /details %}}

{{% details title="Mijenjaju li efekti ili oštećuju moje glazbene datoteke?" closed="true" %}}
Ne. Sve se primjenjuje uživo dok glazba svira. Vaše datoteke nikada se ne mijenjaju ni ponovno spremaju. Isključite efekt i izvorni zvuk se odmah vraća.
{{% /details %}}

{{% details title="Mogu li koristiti više od jednog efekta istovremeno?" closed="true" %}}
Da. Svaki efekt ima svoj prekidač i nema glavnog prekidača, pa bilo koja kombinacija radi. Na primjer, Normalizacija glasnoće plus Kompresor za ujednačeno slušanje, ili Freeverb plus Crossfeed na slušalicama, s ekvalizatorom na vrhu.
{{% /details %}}

{{% details title="Zašto su kontrole efekta zasivljene?" closed="true" %}}
Efekt je isključen. Uključite njegov prekidač na vrhu uređivača da koristite kontrole. Svaki efekt je isključen prema zadanom.
{{% /details %}}

{{% details title="Što znači oznaka Manual?" closed="true" %}}
Znači da ste pomaknuli klizač dalje od preseta, pa efekt sada koristi vaše vlastite prilagođene vrijednosti umjesto imenovanog preseta. Svaki klizač ima gumb za poništavanje, a ponovni odabir preseta zamjenjuje vaše ručne vrijednosti.
{{% /details %}}

{{% details title="Mogu li spremiti i dijeliti svoje presete ekvalizatora?" closed="true" %}}
Da. Osim 22 ugrađena preseta, možete napraviti vlastite, promijeniti im redoslijed te ih izvesti ili uvesti da premjestite svoje postavke na drugi uređaj.
{{% /details %}}

{{% details title="Rade li efekti s CarPlayem, streamingom i pozadinskom reprodukcijom?" closed="true" %}}
Da. Efekti rade unutar BASS™ motora, pa se primjenjuju na lokalne datoteke, diskove u oblaku, medijske poslužitelje, streamove i modul glazbu, i nastavljaju raditi tijekom CarPlaya i pozadinske reprodukcije.
{{% /details %}}

{{% details title="Mogu li promijeniti kvalitetu audio izlaza?" closed="true" %}}
Da. U Postavke > Audio player možete postaviti izlaznu frekvenciju uzorkovanja, broj kanala i veličinu međuspremnika da odgovaraju vašim slušalicama, zvučnicima ili DAC-u.
{{% /details %}}

{{% details title="Kakva je dobra početna postavka za slušalice?" closed="true" %}}
Uključite Normalizaciju glasnoće (Standard), dodajte lagani Kompresor (Soft), odaberite preset ekvalizatora koji vam se sviđa i uključite Crossfeed (Chu Moy ili Jan Meier). Ostavite reverb, echo i distorziju isključenima osim ako želite kreativan zvuk.
{{% /details %}}

---

*BASS je zaštitni znak tvrtke Un4seen Developments Ltd. Pogledajte [un4seen.com](https://www.un4seen.com/). Crossfeed koristi bs2b (Bauer stereophonic-to-binaural) algoritam; pogledajte [bs2b projektnu stranicu](https://bs2b.sourceforge.net/).*
