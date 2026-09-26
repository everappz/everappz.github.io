---
title: "Kako reproducirati FLAC (lossless) glazbu na svom iPhoneu"
date: 2024-01-29
lastmod: 2026-09-26
description: "Kako reproducirati FLAC na iPhoneu i iPadu u 2026. uz Flacbox, hi-res reproduktor s više od 120 formata, izlazom do 384 kHz, podrškom za USB DAC, 10-pojasnim ekvilizatorom, BASS audio pogonom, efektima u stvarnom vremenu poput reverba i delaya, DSP procesorom i glazbenim vizualizatorom s 500 presetova. Reproducirajte iz oblaka ili s NAS-a i slušajte izvan mreže."
keywords: ["kako reproducirati flac na iphoneu", "flac reproduktor iphone", "flac", "iphone", "lossless", "hi-res audio", "dsd reproduktor ios", "usb dac iphone", "384khz", "glazba", "flacbox", "streaming", "izvan mreže", "ekvilizator", "dsp", "glazbeni vizualizator", "bass pogon"]
tags: ["glazba", "oblak", "reproduktor", "preuzimatelj", "ekvilizator", "lossless", "hi-res", "izvan mreže", "FLAC", "DSD", "DAC", "streamer", "vizualizator", "DSP"]
readingTime: 8
---

{{< author-byline >}}


**Ukratko:** Za reprodukciju FLAC-a na iPhoneu potreban vam je reproduktor treće strane, jer Appleova aplikacija Glazba ne podržava FLAC. Instalirajte [Flacbox](/products/flacbox) (besplatan je), a zatim ili prenesite datoteke putem Wi-Fi Drivea ili USB-a, ili povežite svoju pohranu u oblaku ili NAS. Vaša FLAC biblioteka reproducira se u punoj kvaliteti, do 384 kHz i 32-bit putem USB DAC-a. Flacbox također reproducira više od 120 formata, uključujući FLAC, DSD, ALAC, APE, WAV, OGG i OPUS, a dodaje i 10-pojasni ekvilizator, profesionalni BASS audio pogon s efektima u stvarnom vremenu, DSP procesor i glazbeni vizualizator preko cijelog zaslona.

[{{< figure src="/docs/howto/how-to-play-flac-music-on-iphone/Flacbox_Icon-App-1024x1024.webp" alt="Flacbox Icon - FLAC music player and downloader" width="160" >}}](/products/flacbox)

## Zašto moj iPhone ne reproducira FLAC izvorno?

Apple ima vlastiti lossless format nazvan ALAC (Apple Lossless), a aplikacija Glazba izgrađena je oko njega umjesto oko FLAC-a. Od iOS 11, aplikacija Datoteke može prikazati pretpregled jedne FLAC datoteke, ali nema glazbenu biblioteku, popise pjesama, red čekanja, ekvilizator ni streaming iz oblaka. To je preglednik datoteka, a ne glazbeni reproduktor.

Dakle, imate dvije prave mogućnosti:

1. Reproducirajte FLAC pomoću aplikacije reproduktora, tako da vaše datoteke ostaju točno onakve kakve jesu. Ovu preporučujemo.
2. Pretvorite FLAC u ALAC, što je lossless u lossless, a zatim sinkronizirajte s aplikacijom Glazba.

Ako imate pravu FLAC zbirku, prva je mogućnost bolja. Izbjegavate dupliranu biblioteku, preskačete vrijeme pretvorbe, a vaše mape i hi-res kvaliteta ostaju netaknute. Flacbox je izgrađen upravo za to.

## Mogućnost 1: reproducirajte FLAC uz Flacbox

Flacbox je hi-res glazbeni reproduktor za iPhone, iPad i Mac. Pretvara vašu pohranu u oblaku, NAS ili računalo u vašu vlastitu privatnu glazbenu biblioteku, bez pretvorbe i bez pretplate.

### Korak 1. Instalirajte Flacbox

Flacbox je besplatan za preuzimanje i radi na iPhoneu, iPadu i Macu.

{{< app-details product="flacbox" >}}

### Korak 2. Unesite svoje FLAC datoteke

Odaberite način koji vam je najlakši:

- **Wi-Fi Drive** — otvorite Povezivanja, zatim Računalo, pa Poveži se putem Wi-Fija, i povucite datoteke iz bilo kojeg preglednika na računalu. Pogledajte [vodič za Wi-Fi Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).
- **Pohrana u oblaku** — povežite iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, pCloud, Proton Drive i još 20, a zatim reproducirajte streamingom izravno iz oblaka.
- **NAS ili računalo** — povežite se putem SMB, WebDAV, DLNA, FTP, SFTP ili NFS (Synology, QNAP, WD My Cloud, Time Capsule ili bilo koji Samba dijeljeni resurs). Cijeli popis nalazi se u [vodiču za Povezivanja](/docs/guide/flacbox/flacbox-guide-connections).
- **USB memorijski pogon** — priključite SanDisk iXpand ili bilo koji vanjski čitač i reproducirajte [izravno s pogona](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it), bez uvoza.
- **Dijeljenje datoteka putem iTunesa ili Findera** — preko Lightning ili USB-C kabela.

### Korak 3. Pritisnite reprodukciju

Vaše se pjesme pojavljuju u biblioteci s oznakama i omotima pročitanima iz samih datoteka, grupirane po Albumu, Izvođaču, Žanru i Skladatelju. Svaka pjesma prikazuje svoj točan kodek i rezoluciju, primjerice FLAC, 96 kHz, 24-bit.

## Hi-res izlaz, USB DAC i višekanalni zvuk

Flacbox je izgrađen za ljude kojima je stalo do kvalitete zvuka, a ne samo do povremenog slušanja:

- **Frekvencija uzorkovanja** — reproducira od 8 kHz do 384 kHz, s višekanalnim izlazom od 1 do 7 kanala (do 5.1 i ITU BS.775-1).
- **Podrška za USB DAC** — sve iznad 48 kHz reproducira se u svojoj pravoj rezoluciji putem USB DAC-a. Preko vlastitog izlaza iPhonea, iOS ponovno uzorkuje zvuk kao što to čini za svaku aplikaciju, pa je DAC način da dobijete bit-perfect hi-res.
- **Podesivi izlaz** — postavite frekvenciju uzorkovanja, broj kanala i trajanje IO međuspremnika (oko 5 ms za hi-res s niskom latencijom) u Postavke, zatim Audio reproduktor.
- **Visina i brzina** — fina korekcija visine tona, uz brzinu reprodukcije od 0.02× do 3.00×.

## Reproducira više od 120 formata, ne samo FLAC

Uz FLAC, Flacbox uključuje FFmpeg kako bi mogao reproducirati formate koje iOS ne može sam otvoriti. Ne morate prvo pretvarati ni čistiti mješovitu biblioteku:

- **Lossless i hi-res** — FLAC, ALAC, WAV, AIFF, APE, WV (WavPack) i DSD (DSF i DFF, uključujući DSD64, DSD128 i DSD256).
- **S gubicima** — MP3, AAC, M4A, OGG, OPUS, WMA, MPC i još mnogo toga.
- **Tracker i MOD glazba** — klasične chiptune i demoscene datoteke MOD, XM, IT, S3M, MTM, UMX i MO3 koje većina reproduktora ne može otvoriti.

To je ukupno više od 120 formata, što pokriva gotovo sve u modernoj glazbenoj zbirci.

## Tri audio pogona, uključujući BASS pogon

Pogon reprodukcije možete odabrati u Postavke, zatim Audio reproduktor, pa Audio kodek:

- **System Codec + FFmpeg** — maksimalna kompatibilnost i stabilnost.
- **FFmpeg** — prisiljava FFmpeg putanju, čime se otključava korekcija visine tona i prilagođena izlazna frekvencija uzorkovanja.
- **BASS™ pogon** — profesionalna jezgra reprodukcije dodana u [Flacbox 7.6](/blog/flacbox-7-6-bass-audio-engine-effects-dsp-music-visualizer). Otključava audio efekte u stvarnom vremenu, DSP procesor, glazbeni vizualizator, tracker i MOD reprodukciju te ponovno uzorkovanje visoke kvalitete. Dodaje i neovisnu kontrolu visine tona (±60 semitones) i kontrolu tempa (0.1× do 4×).

## 10-pojasni ekvilizator, pojačanje basa i pretpojačalo

Flacbox uključuje 10-pojasni grafički ekvilizator s presetovima u stilu iPoda poput Acoustic, Bass Booster, Rock, Pop, Jazz, Classical i Dance. Postoji pretpojačalo za podizanje tihih pjesama bez izobličenja, a možete spremiti i vlastite presetove. Podesite ga za slušalice u uhu, HomePod ili automobilski stereo. Za potpuni vodič pogledajte [vodič za ekvilizator](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Ekvilizator Flacbox audio reproduktora" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Audio efekti u stvarnom vremenu

Kada je BASS pogon uključen, dobivate jedanaest efekata u stvarnom vremenu koje možete slagati i podešavati dok glazba svira. Ništa se ne kodira ponovno, a isključivanje efekta odmah vraća izvorni zvuk:

- **Reverb** — od male sobe do katedrale.
- **Delay i multi-tap echo** — od kratkog slapbacka do dugog ambijentalnog repa.
- **Crossfeed** — miješa stereo kanale tako da slušalice zvuče više poput pravih zvučnika na oštro paniranim miksevima.
- **Kompresor** — izjednačava glasne i tihe dijelove, što je odlično za auto ili teretanu.
- **Chorus, Flanger, Phaser, Auto-Wah, Distortion i stereo rotacija** — kreativni modulacijski i karakterni efekti.

Flacbox ima i automatsko izjednačavanje glasnoće na temelju broadcast standarda glasnoće EBU R128. Albumi i nasumično promiješani popisi pjesama sviraju na ujednačenoj razini, pa ne morate stalno posezati za glasnoćom. Dolazi s presetovima Light, Standard, Strong i Night.

## Izgradite vlastiti DSP procesor

Osim efekata, Flacbox vam daje DSP procesor s 14 filtara u stvarnom vremenu koji sami postavljate. Možete dodati profesionalne filtre i parametarske EQ pojaseve, saturaciju i bit crusher te kreativne procesore poput tremola, ring modulatora i stereo širine. Sve to radi uživo na svemu što reproducirate, od lokalnog FLAC-a do streama iz oblaka, a DSP postavke dostupne su čak i u CarPlayu.

## Glazbeni vizualizator preko cijelog zaslona

Flacbox ima ugrađeni glazbeni vizualizator koji slika pokretne, šarene vizuale u ritmu vaše glazbe. Koristi poznati Milkdrop pogon (projectM) s 500 presetova, iscrtane pomoću OpenGL na iPhoneu, iPadu i Macu. Otvorite ga iz reproduktora dodirom na gumb Više radnji, a zatim Vizualizacija. Odaberite preset ili upotrijebite Auto način rada da ih promiješate svakih 30 sekundi uz glatki crossfade. Za pomoć korak po korak pogledajte vodič o tome [kako uključiti glazbeni vizualizator](/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox glazbeni vizualizator (Milkdrop i projectM)" image="/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac/music-visualizer-starfield-sectors-preset.webp" >}}
{{< /cards >}}

## Oblak, NAS i reprodukcija izvan mreže

Reproducirajte streamingom izravno iz više od 30 usluga u oblaku, uključujući iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, pCloud, Proton Drive i Internxt. Možete povezati i samostalno hostirane poslužitelje poput Plex, Jellyfin, Emby, Subsonic i Navidrome, te bilo koji NAS putem SMB, WebDAV, DLNA, FTP, SFTP ili NFS.

Kada želite glazbu sa sobom, ugrađeni upravitelj preuzimanja sprema cijele popise pjesama, izvođače, albume ili mape za slušanje izvan mreže. Način izvan mreže zatim automatski sinkronizira nove pjesme čim se pojave u oblaku. Ponestaje vam prostora? Očistite predmemoriju jednim dodirom i nastavite reproducirati streamingom.

## Sve ostalo što ozbiljni slušatelji žele

- **Organizirana biblioteka** — grupirana po Pjesmama, Albumima, Izvođačima albuma, Izvođačima, Žanrovima i Skladateljima, uz brzo pretraživanje koje radi izvan mreže.
- **Uređivač ID3 oznaka** — popravite neuredne metapodatke i pokvarena kodiranja (ćirilica, japanski, kineski) i upišite promjene natrag u datoteku.
- **Popisi pjesama** — izradite, presložite, uvezite i izvezite M3U, M3U8 i CUE te ih učinite dostupnima izvan mreže.
- **Apple CarPlay** — namjenski zaslon u automobilu za biblioteku, oblak, lokalnu i glazbu izvan mreže, s ekvilizatorom na raspolaganju.
- **AirPlay 2 i Chromecast** — emitirajte na HomePod, Apple TV i zvučnike s podrškom za Cast.
- **Alati za audioknjige** — više zabilješki, podesiva brzina, mjerač vremena za spavanje i nastavak od mjesta na kojem ste stali.
- **Widgeti i još mnogo toga** — widgeti za početni zaslon i zaključani zaslon, Last.fm scrobbling, vremenski usklađeni tekstovi i LRC, te potpuna VoiceOver pristupačnost.

Flacbox je besplatan za preuzimanje. Premium uklanja ograničenja besplatne verzije na račune u oblaku, popise pjesama i mape izvan mreže, a dostupan je kao jednokratna doživotna kupnja ili kao mjesečna ili godišnja pretplata, uz Obiteljsko dijeljenje.

{{< app-details product="flacbox" >}}

## Mogućnost 2: pretvorite FLAC u ALAC za aplikaciju Glazba

Ako doista želite svoje ripove unutar Appleove aplikacije Glazba, možete ih pretvoriti. FLAC u ALAC je lossless u lossless, pa ne gubite nikakvu kvalitetu:

1. Na svom računalu skupno pretvorite besplatnim alatom poput XLD na Macu ili foobar2000 na Windowsu. Oba zadržavaju vaše oznake.
2. Dodajte ALAC datoteke u svoju biblioteku Glazba ili iTunes.
3. Sinkronizirajte na iPhone pomoću Findera na Macu ili aplikacije Apple Devices na Windowsu.

Kompromisi su stvarni. Sada čuvate dvije kopije svoje biblioteke, svaka izmjena metapodataka znači još jednu sinkronizaciju, a raspored aplikacije Glazba ostaje fiksan, bez popisa pjesama temeljenih na pravilima, bez ekvilizatora, bez DSP-a i bez streaminga iz oblaka ili s NAS-a na uređaju. Zato većina ljudi s ozbiljnim FLAC zbirkama bira prvu mogućnost.

## Česta pitanja

{{% details title="Može li iPhone izvorno reproducirati FLAC datoteke?" closed="true" %}}
Samo na ograničen način. Aplikacija Datoteke može prikazati pretpregled jedne FLAC datoteke od iOS 11, ali nema biblioteke, popisa pjesama, reda čekanja, ekvilizatora ni streaminga iz oblaka. Za pravo slušanje upotrijebite aplikaciju reproduktora poput Flacboxa.
{{% /details %}}

{{% details title="Mogu li reproducirati 24-bit ili 96kHz (ili više) FLAC na iPhoneu?" closed="true" %}}
Da. Flacbox podržava hi-res izlaz do 384 kHz. Za reprodukciju iznad 48 kHz u pravoj rezoluciji povežite vanjski USB DAC, jer ugrađeni izlaz iPhonea ponovno uzorkuje zvuk za svaku aplikaciju.
{{% /details %}}

{{% details title="Pretvara li Flacbox FLAC u drugi format?" closed="true" %}}
Ne. Flacbox reproducira FLAC u njegovoj izvornoj lossless kvaliteti bez pretvorbe. Efekti i DSP primjenjuju se uživo samo tijekom reprodukcije i nikada ne mijenjaju vaše datoteke.
{{% /details %}}

{{% details title="Gubim li kvalitetu pretvaranjem FLAC-a u ALAC?" closed="true" %}}
Ne. FLAC i ALAC oba su lossless, pa je pretvorba bit-perfect. Samo trošite vrijeme i odričete se praktičnosti, jer završite s dvjema bibliotekama za održavanje i morate ponovno sinkronizirati nakon izmjena.
{{% /details %}}

{{% details title="Koje audio formate Flacbox podržava?" closed="true" %}}
Više od 120 formata, uključujući FLAC, DSD (DSF i DFF), ALAC, APE, WAV, AIFF, WV, OGG, OPUS, MP3, AAC, M4A, WMA, pa čak i tracker i MOD glazbu poput MOD, XM, IT i S3M.
{{% /details %}}

{{% details title="Ima li Flacbox ekvilizator, efekte i vizualizator?" closed="true" %}}
Da. Ima 10-pojasni ekvilizator s presetovima i pretpojačalom. Ima i profesionalni BASS pogon s jedanaest efekata u stvarnom vremenu (reverb, delay, multi-tap echo, crossfeed, kompresor, chorus, flanger, phaser, auto-wah, distortion i stereo rotacija), uz EBU R128 izjednačavanje glasnoće, DSP procesor s 14 filtara i Milkdrop vizualizator preko cijelog zaslona s 500 presetova.
{{% /details %}}

{{% details title="Mogu li reproducirati FLAC streamingom sa svog NAS-a ili iz oblaka?" closed="true" %}}
Da. Flacbox se povezuje s više od 30 usluga u oblaku te s NAS-om ili računalom putem SMB, WebDAV, DLNA, FTP, SFTP i NFS. Cijela vaša biblioteka dostupna je bez kopiranja datoteka na iPhone, a pjesme možete preuzeti za reprodukciju izvan mreže bilo kada.
{{% /details %}}

{{% details title="Je li Flacbox doista besplatan?" closed="true" %}}
Flacbox je besplatan za preuzimanje, s osnovnim značajkama poput ekvilizatora, streaminga iz oblaka i reprodukcije izvan mreže. Premium uklanja ograničenja besplatne verzije na račune u oblaku, popise pjesama i mape izvan mreže, a dolazi kao jednokratna doživotna kupnja ili kao mjesečna ili godišnja pretplata, uz Obiteljsko dijeljenje.
{{% /details %}}
