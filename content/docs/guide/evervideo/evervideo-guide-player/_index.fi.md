---
title: "Mediasoitin"
date: 2020-02-01
lastmod: 2026-06-01
description: "Opi käyttämään Evervideo-mediasoitinta iPhonella, iPadilla ja Macilla. Picture-in-Picture, laitteistokiihdytetty H.264/HEVC-dekoodaus, ääni- ja videotaajuuskorjaimet, ensisijaiset ja toissijaiset tekstitykset, ääni- ja videoraitojen valinta, videon skaalaus ja pyöritys, toistonopeus, uniajastin, AirPlay 2, Google Chromecast, RTSP-virrat ja kompakti aina näytöllä oleva soitin."
keywords: [
  "Evervideo soitin-opas", "videosoittimen asetukset", "Evervideo taajuuskorjain",
  "Picture-in-Picture iPhone", "PiP video iPad", "PiP video Mac",
  "AirPlay 2 video", "Google Chromecast video",
  "videotekstitykset iPhone", "ulkoiset SRT-tekstitykset",
  "ASS SSA tekstityssoitin", "libass iOS",
  "kaksoisTekstitykset kielenopiskelu",
  "videotaajuuskorjain kirkkaus kontrasti", "äänentaajuuskorjain videosoitin",
  "videosoittimen pyörityksen lukitus", "videon skaalausmoodi iOS",
  "laitteisto H.264 dekooderi iPhone", "laitteisto HEVC dekooderi iPad",
  "toistonopeus video", "FFmpeg videosoitin iOS",
  "RTSP iPhone soitin", "kompakti videosoitin",
  "VR 360 videosoitin iPhone"
]
tags: ["opas", "evervideo", "soitin", "PiP", "tekstitykset", "videotaajuuskorjain"]
readingTime: 14
---


Mediasoitin on sovelluksen päänäyttö, jossa hallitset toistoa ja useimpia Evervideo-ominaisuuksia. Se toistaa sekä video- että äänitiedostoja ja on rakennettu mukautettuun FFmpeg-pohjaiseen soittimeen laitteistokiihdytetyllä H.264- ja HEVC-dekoodauksella. Tutkitaan kuinka sitä käytetään.

## Mediasoittimen Käyttö

Pääset koko näytön soittimeen kompaktin soitinpalkin kautta. iPhonella kompakti soitin sijaitsee päänäytön yläosassa. iPadilla ja Macilla se on vasemmalla puolella (tai pääpaneelin yläosassa). Supistaaksesi koko näytön soittimen takaisin kompaktiin näkymään, napauta sulje-painiketta oikeassa alakulmassa tai pyyhkäise alas. Piilottaaksesi kompaktin soittimen kokonaan, napauta ja pyyhkäise alas vielä kerran.

Kompakti soitin pysyy näkyvissä samalla kun selaat kirjastoasi, tiedostohallintaasi tai asetuksiasi, joten et koskaan menetä videotasi seuraavaa etsiessäsi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo koko näytön mediasoitin" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Tuetut Video- ja Ääniformaatit

Evervideo toistaa käytännöllisesti katsoen jokaisen nykyaikaisen kontin ja codecin sisällytetyn FFmpeg-moottorin kautta, laitteistokiihdytetyllä H.264- ja HEVC-dekoodauksella tuetuilla laitteilla.

- **Videokonttit:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — ja paljon muuta.
- **Video-codecit:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — plus käytännöllisesti katsoen jokainen muu codec, jota FFmpeg tukee.
- **Ääni-codecit:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — ja paljon muuta.
- **Tekstitysformaatit:** SRT, VTT (WebVTT), ASS / SSA ja upotetut teksti- tai kuvatekstitysraidat.
- **Suoratoistoprotokolaat:** HTTP / HTTPS, HLS (m3u8), RTSP (IP-kamerat ja IPTV) ja suora tiedostojen suoratoisto SMB / WebDAV / FTP / SFTP / NFS / DLNA:n kautta.

Se kattaa käytännöllisesti katsoen jokaisen videotiedoston, jonka todennäköisesti kohtaat — mukaan lukien MKV-ripit, turvakameran RTSP-virrat ja AV1 webm -web-lataukset.

## Toistokontrollit

Soittimen näytön alareunassa näet Toista-, Tauko-, Seuraava- ja Edellinen-painikkeet. On myös valinnaisia painikkeita kuten Hyppää eteenpäin ja Hyppää taaksepäin (oletus 10 sekuntia), jotka voit ottaa käyttöön sovelluksen asetuksissa. Pidä Seuraava / Edellinen -painikkeita painettuna pikakelauksen tai pikakelaukseen taaksepäin. Vedä toiston liukusäädintä hypätäksesi mihin tahansa kohtaan.

## Toisto ja Sekoitus

Napauta toistopainiketta siirtyäksesi toistotilojen välillä:

- **Toista kaikki** — toistaa jokaisen videon jonossasi.
- **Toista yksi** — toistaa vain nykyisen videon.
- **Pysäytä lopussa** — keskeyttää nykyisen videon päättyessä.
- **Ei toistoa** — toistaa jonon kerran ilman toistoa.

Käytä **Sekoitus**-painiketta jonon videoiden järjestyksen satunnaistamiseen.

## Picture-in-Picture (PiP)

iPhonella ja iPadilla Evervideo tukee täysin Picture-in-Picture (PiP) -toimintoa. Napauta PiP-kuvaketta soittimen näytöllä tai yksinkertaisesti pyyhkäise Evervideo taustalle — video jatkaa toistamista kelluvassa ikkunassa kaikkien muiden sovellusten yläpuolella. Vedä kelluva ikkuna mihin tahansa kulmaan; nipistä muuttaaksesi kokoa; napauta kerran esittääksesi toisto- / tauko- / ohituskontrollit; napauta pientä laajennuspainiketta palataksesi koko Evervideo-sovellukseen.

PiP toimii kaikilla videoformaateilla, joita Evervideo toistaa, mukaan lukien pilvistä suoratoistettavat tiedostot ja RTSP-virrat. PiP jatkuu myös puhelimen ollessa lukittuna (Automaattinen lukitus -asetuksesta riippuen).

## Kompakti Soitin

Kompakti soitin on pysyvä mini-soitin, joka pysyy näkyvissä jokaisen sovelluksen näytön yläosassa samalla kun selaat kirjastoa, tiedostohallintaa tai asetuksia. Napauta sitä laajentaaksesi koko näytön soittimeksi; pyyhkäise alas supistaaksesi sen takaisin.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Videoasetukset kompaktista soittimesta päänäytöllä" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

AirPlay'ta varten napauta soittimen AirPlay-painiketta. Evervideo tukee AirPlay 2:ta, joten voit suoratoistaa videota Apple TV:lle, HomePodille tai mille tahansa AirPlay 2 -yhteensopivalle kaiuttimelle tai äly-TV:lle. Useita AirPlay-laitteita sisältävässä järjestelmässä voit reitittää äänen useille vastaanottimille samanaikaisesti.

## Google Chromecast

Google Cast -käyttäjille soittimessa näkyy Cast-kuvake. Napauta sitä valitaksesi laitteen ja aloittaaksesi suoratoiston. Varmista, että puhelimesi ja Cast-vastaanotin ovat samassa Wi-Fi-verkossa. Kaikkia codecia ei tueta Chromecast-laitteistossa — jotkin tiedostot saattavat tarvita transkoodausta.

## RTSP Live-Virrat

Evervideo voi toistaa RTSP-lähteitä suoraan — IP-kamerat, oven kamerat, IPTV-virrat, lähetysvirrat ja mikä tahansa muu `rtsp://`-osoite. Lisää virta RTSP-yhteytenä kohdassa Tiedostot → Online-linkit → Lisää linkki, napauta sitä sitten aloittaaksesi katselun. RTSP-virrat toimivat Picture-in-Picturessa, kompaktissa soittimessa ja ne lähetetään AirPlay 2:lla ja Chromecastilla aivan kuin tavallinen video.

## Ääniraitatun Valinta

Videoille, joissa on useita ääniraitoja (kommentaari, vaihtoehtoiset dubbaukset, ohjaajan raita), napauta soittimen Lisää toimintoja -painiketta ja valitse Ääniraita — valitse sitten haluamasi raita. Tämä on välttämätöntä vieraskielisille elokuville, BDMV / MKV -tiedostoille useilla dubbauksiolla ja ohjeelliselle sisällölle kommentaariraidoilla.

## Videoraitatun Valinta

Jotkin videotiedostot sisältävät useita videoströömejä (monikulmaiset Blu-rayt, vaihtoehtoiset leikkaukset). Valitse Videoraita Lisää toimintoja -valikosta vaihtaaksesi niiden välillä toiston aikana.

## Tekstitykset — Sisäiset ja Ulkoiset

Evervideo antaa sinulle tarkkarajaisen hallinnan tekstityksistä:

- **Tekstitysraita** — valitse tiedostoon upotettujen raitojen joukosta.
- **Ulkoiset tekstitystiedostot** — lataa `.srt`, `.vtt`, `.ass` tai `.ssa` -tiedostoja laitteeltasi, iCloud Drivesta tai mistä tahansa yhdistetystä pilvipalvelusta.
- **Libass-renderöinti** — edistynyt ASS / SSA -tyyli (fontit, värit, sijainnit, karaoke-efektit) renderöidään oikein sisällytetyn libass-kirjaston ansiosta.
- **Fontinvalinta** — valitse mukautettu fontti ensisijaisille tekstityksille ja erillinen fontti toisijaisille. Sisällytetyt fontit sekä kaikki laitteellesi asennetut fontit ovat käytettävissä.

Voit määrittää kaiken tämän kohdassa Asetukset → Tekstitykset ennen toistoa tai käyttää Lisää toimintoja → Tekstitykset soittimesta vaihtaaksesi lennosta.

## Äänentaajuuskorjain

Evervideo sisältää täyden äänentaajuuskorjaimen videon ääniraitojen virittämiseen kuulokkeille, kaiuttimille tai hi-fi-järjestelmällesi. Napauta taajuuskorjaimen kuvaketta äänenvoimakkuusnäkymässä (tai Äänentaajuuskorjain-toimintoa soittimen Lisää toimintoja -valikossa), ota taajuuskorjain käyttöön oikeassa yläkulmassa olevalla kytkimellä ja valitse joko esiasetus tai vedä kaistaliukusäätimiä luodaksesi oman esiasemuksen. Mukautettuja esiasemuksia voidaan viedä ja tuoda jakamiseksi eri laitteiden välillä tai varmuuskopiointiin.

## Videotaajuuskorjain

Kuvan virittämistä varten Evervideo tarjoaa erillisen videotaajuuskorjaimen — säädä kirkkautta, kontrastia, kylläisyyttä ja värisävyä reaaliajassa toiston aikana. Kuten äänentaajuuskorjain, mukautettuja videoesiasemuksia voidaan viedä ja tuoda jakamista tai varmuuskopiointia varten. Käytä sitä tumman kohtauksen kirkastamiseen aurinkoisena päivänä, kylläisyyden lisäämiseen haalistuneessa sisällössä tai kylmän värisävyn lämmittämiseen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo videotaajuuskorjain" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Videon Skaalausmoodi

Valitse kuinka video täyttää näytön:

- **Sovita** — säilytä alkuperäinen kuvasuhde; mustat palkit tarvittaessa.
- **Täytä** — täytä koko näyttö, leikata video tarvittaessa.
- **Venytä** — venytä video täyttämään näyttö, vääristäen tarvittaessa.
- **Alkuperäinen** — säilytä natiivi resoluutio 1:1.

## Videon Pyöritys

Väärällä suunnistuksella tallennetuille videoille valitse **Lisää toimintoja → Pyöritys** ja valitse **0°**, **90°**, **180°** tai **270°** kuvan kiertämiseen poistumatta soittimesta.

## Laitteistodekoodaus (H.264 ja HEVC)

Kohdassa Asetukset → Soitin → Video voit ottaa käyttöön / poistaa käytöstä Laitteistodekoodaus H.264 ja Laitteistodekoodaus H.265 (HEVC) itsenäisesti. Laitteistodekoodaus on nopeampaa, kuluttaa vähemmän akkua ja toimii viileämmin — mutta harvinaisissa tapauksissa (vioittuneet tiedostot, eksoottiset profiilit) saatat joutua poistamaan laitteistodekoodauksen käytöstä ja palaamaan ohjelmistopohjaisen FFmpeg-dekoodauksen käyttöön. Evervideo mahdollistaa sen tiedostokohtaisesti soittimen Lisää toimintoja -valikosta.

## VR 360° -näkymä

Evervideo sisältää VR / 360° -näkymän sfäärisiä videotiedostoja varten. Toistettaessa 360°-videota voit vetää katsoaksesi ympärillesi, nipistä zoomattaksesi, ja Evervideo vääristää renderöinnin reaaliajassa.

## Toistonopeus

Napauta Nopeus-säätöä soittimen työkalupalkissa muuttaaksesi toistonopeutta — hidasta analyysia varten (0,25× tai 0,5×) tai nopeuta opaskirjojen ja luentojen osalta (1,25×, 1,5×, 2× ja jopa 3×). Napauta asetuskuvaketta Nopeus-näytön oikeassa yläkulmassa siirtyäksesi tarkkaan tilaan hienommilla säädöillä. Myös raitakohtainen sävelkorjaus on saatavilla.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo toistonopeus päätyökalupalkissa" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Soittimen Jono

Nähdäksesi soittimen jonon, napauta jono-painiketta soittimessa. Jokaisella jonossa olevalla videolla on lisää toimintoja — napauta kolmea pistettä nähdäksesi ne. Videoa uudelleenjärjestääksesi jonossa käytä otsikon lähellä olevaa järjestämisohjainta ja vedä se uuteen sijaintiin.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo toistojono" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Uniajastin

Avaa Asetukset → Soitin → Uniajastin, ota se käyttöön ja valitse kuinka kauan haluat toiston jatkuvan ennen automaattista pysähtymistä. Voit myös lisätä Uniajastin-painikkeen suoraan soittimen päänäyttöön kohdassa Asetukset → Soitin → Personointi → Päänäytön toiminnot.

## Soittimen Kirjanmerkit

Tallenna paikkasi pitkissä videoissa — luennot, äänikirjat videoina, opaskirjat, tunnin mittaiset YouTube-lataukset — napauttamalla Lisää kirjanmerkki Lisää toimintoja -valikosta. Kirjanmerkit näkyvät videon Lisää toimintoja → Kirjanmerkit-listassa ja säilyvät istuntojen välillä.

## Lisää Toimintoja -Valikko

Napauta soittimen Lisää toimintoja "..." -painiketta päästäksesi lisätoimintoihin.

- **Jatka toistoa** — jatka jonoa viimeisestä sijainnista.
- **Haku** — etsi tiettyä videota jonosta.
- **Kirjanmerkit** — katso ja hyppää kirjanmerkkeihin.
- **Nopeus** — säädä toistonopeutta.
- **Äskettäin** — äskettäin toistetut videot.
- **Suosikit** — suosikki-videot.
- **Äänentaajuuskorjain** — aktivoi äänentaajuuskorjain.
- **Videotaajuuskorjain** — aktivoi videotaajuuskorjain.
- **Ääniraita** — valitse äänivirta.
- **Videoraita** — valitse videovirta.
- **Tekstitykset** — ensisijainen / toissijainen raita, ulkoinen tiedosto, fontti.
- **Pyöritys** — pyöritä kuvaa 0° / 90° / 180° / 270°.
- **Skaalausmoodi** — Sovita / Täytä / Venytä / Alkuperäinen.
- **Picture-in-Picture** — siirry PiP-tilaan.
- **AirPlay** / **Chromecast** — lähetä laitteelle.
- **Uniajastin** — aseta ajastin toiston pysäyttämiseksi.
- **Tallenna jono soittolistana** — tallenna nykyinen jono uutena soittolistana.
- **Poista jono** — tyhjennä jono ja pysäytä toisto.
- **Asetukset** — siirry suoraan soittimen asetuksiin.
- **Ohje** — avaa opaskirja.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo soittimen lisää toimintoja -näyttö" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Soittimen Asetukset

Koko soittimen asetuspuu on dokumentoitu [Asetukset-oppaassa](/docs/guide/evervideo/evervideo-guide-settings/). Eniten käytetyt osiot:

- **Yleinen** — Toistotila, sekoitustila, tallenna soittimen tila, tallenna toistosijainti, hypyn aikavälit.
- **Video** — Laitteistodekoodaus H.264 / HEVC, videotaajuuskorjain, skaalausmoodi, pyöritys, näyttötila, suositellut FPS, suositeltu pikselimuoto, VR-näkymä.
- **Ääni** — Äänentaajuuskorjain, näytteenottotaajuus, kanavat, IO-puskurin kesto, sekamoodi.
- **Tekstitykset** — Ensisijainen / toissijainen raita, ulkoisen tiedoston valinta, fontti, toissijainen fontti.
- **Laitteet** (iOS) — AirPlay / Chromecast.
- **Personointi** — Soittimen asettelun tyyli (Minimal / Alareuna / Antique / Classical), päänäytön toiminnot, lukitusnäytön kontrollit.
- **Toistovälimuisti** — levyvälimuisti sujuvampaa suoratoistoa varten.
- **Uniajastin** — automaattinen pysäytys.

## Esteettömyys

Evervideo on täysin käytettävissä VoiceOverin kanssa. Jokaisella komponentilla on hyvin suunniteltu tunniste ja kuvaus. Kun VoiceOver on aktiivinen, sovellus vaihtaa Tekstitilaan, jotta vain merkitykselliset elementit näkyvät — parantaen navigointinopeutta ja selkeyttä. Voit myös ottaa Tekstitilan käyttöön kohdassa Asetukset → Esteettömyys → Tekstimoodi.

### Liukusäätimien Säätäminen VoiceOverin Kanssa

1. **Valitse liukusäädin** — pyyhkäise vasemmalle tai oikealle, kunnes VoiceOver ilmoittaa siitä.
2. **Säädä arvoa** — kaksoisnapauta ja pidä liukusäädintä painettuna, vedä sitten ylös tai alas muuttaaksesi arvoa nopeasti. VoiceOver ilmoittaa uuden arvon edetessäsi.

Muut komponentit toimivat odotetusti käyttäen järjestelmän tarjoamia VoiceOver-malleja.
