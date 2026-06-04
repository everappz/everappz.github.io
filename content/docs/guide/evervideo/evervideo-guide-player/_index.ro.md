---
title: "Player Media"
date: 2020-02-01
lastmod: 2026-06-01
description: "Aflați cum să utilizați playerul media Evervideo pe iPhone, iPad și Mac. Picture-in-Picture, decodare H.264 / HEVC accelerată hardware, egalizatoare audio și video, subtitrări primare și secundare, selecția pistelor audio și video, scalare și rotire video, viteză de redare, temporizator de repaus, AirPlay 2, Google Chromecast, fluxuri RTSP și playerul compact mereu pe ecran."
keywords: [
  "ghid player Evervideo", "setări player video", "egalizator Evervideo",
  "picture-in-picture iPhone", "video PiP iPad", "video PiP Mac",
  "video AirPlay 2", "video Google Chromecast",
  "subtitrări video iPhone", "subtitrări SRT externe",
  "player subtitrări ASS SSA", "libass iOS",
  "subtitrări duble învățare limbi",
  "egalizator video luminozitate contrast", "egalizator audio player video",
  "blocare rotație player", "mod scalare video iOS",
  "decodor H.264 hardware iPhone", "decodor HEVC hardware iPad",
  "viteză redare video", "player video FFmpeg iOS",
  "player RTSP iPhone", "player video compact",
  "player video VR 360 iPhone"
]
tags: ["ghid", "evervideo", "player", "PiP", "subtitrări", "egalizator video"]
readingTime: 14
---


Playerul Media este ecranul principal al aplicației unde controlați redarea și majoritatea funcțiilor Evervideo. Redă atât fișiere video, cât și audio și este construit pe un player personalizat bazat pe FFmpeg cu decodare H.264 și HEVC accelerată hardware care face munca grea. Să explorăm cum să-l utilizăm.

## Accesarea Playerului Media

Puteți ajunge la playerul pe tot ecranul din bara playerului compact. Pe iPhone, playerul compact se află în partea de sus a ecranului principal. Pe iPad și Mac, se află pe partea stângă (sau în partea de sus a panoului principal). Pentru a restrânge playerul pe tot ecranul înapoi la vizualizarea compactă, atingeți butonul de închidere din colțul din dreapta jos sau glisați în jos. Pentru a ascunde complet playerul compact, atingeți și glisați în jos din nou.

Playerul compact rămâne vizibil în timp ce navigați în bibliotecă, managerul de fișiere sau setări, astfel niciodată nu pierdeți videoclipul în timp ce căutați pe următor.

{{< cards cols="1">}}
  {{< card title="" subtitle="Playerul Media pe Tot Ecranul Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Formate Video și Audio Suportate

Evervideo redă practic orice container și codec modern prin motorul FFmpeg inclus, cu decodare H.264 și HEVC accelerată hardware pe dispozitivele suportate.

- **Containere video:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — și multe altele.
- **Codecuri video:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — plus practic orice alt codec pe care FFmpeg îl suportă.
- **Codecuri audio:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — și multe altele.
- **Formate subtitrări:** SRT, VTT (WebVTT), ASS / SSA și piste de subtitrări text sau imagine încorporate.
- **Protocoale de streaming:** HTTP / HTTPS, HLS (m3u8), RTSP (camere IP și IPTV) și streaming direct de fișiere prin SMB / WebDAV / FTP / SFTP / NFS / DLNA.

Aceasta acoperă practic orice fișier video pe care este probabil să-l întâlniți — inclusiv rip-uri MKV, fluxuri RTSP de camere de securitate și descărcări webm AV1.

## Controale de Redare

În partea de jos a ecranului playerului, veți vedea butoane pentru Redare, Pauză, Următor și Anterior. Există și butoane opționale precum Avans Rapid și Retrocedare Rapidă (10 secunde implicit) pe care le puteți activa în setările aplicației. Mențineți apăsate butoanele Următor / Anterior pentru a avansa sau a retroceda rapid. Trageți cursorul de redare pentru a sări la orice poziție.

## Repetare și Amestecare

Atingeți butonul de repetare pentru a parcurge modurile de repetare:

- **Repetare Toate** — repetă fiecare videoclip din coadă.
- **Repetare Unul** — repetă doar videoclipul curent.
- **Oprire la Final** — face pauză când videoclipul curent se termină.
- **Fără Repetare** — redă coada o singură dată fără a repeta.

Folosiți butonul **Amestecare** pentru a randomiza ordinea videoclipurilor din coadă.

## Picture-in-Picture (PiP)

Pe iPhone și iPad, Evervideo suportă complet Picture-in-Picture (PiP). Atingeți pictograma PiP pe ecranul playerului sau pur și simplu trimiteți Evervideo în fundal — videoclipul continuă să se redea într-o fereastră flotantă deasupra tuturor celorlalte aplicații. Glisați fereastra flotantă în orice colț; ciupiți pentru a redimensiona; atingeți o dată pentru a afișa controalele de bază redare / pauză / omitere; atingeți butonul mic de extindere pentru a reveni la Evervideo complet.

PiP funcționează cu fiecare format video pe care îl redă Evervideo, inclusiv fișierele transmise în cloud și fluxurile RTSP. PiP continuă să funcționeze și când telefonul este blocat (în funcție de setarea Auto-Lock).

## Player Compact

Playerul compact este un mini-player persistent care rămâne vizibil în partea de sus a fiecărui ecran din aplicație în timp ce navigați în bibliotecă, managerul de fișiere sau setări. Atingeți-l pentru a extinde la playerul pe tot ecranul; glisați în jos pentru a-l restrânge din nou.

{{< cards cols="1">}}
  {{< card title="" subtitle="Setări Video din Vizualizarea Playerului Compact pe Ecranul Principal Evervideo" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

Pentru AirPlay, atingeți butonul AirPlay pe player. Evervideo suportă AirPlay 2, astfel puteți transmite video la Apple TV, HomePod sau orice difuzor sau smart TV compatibil AirPlay 2. Într-o configurație cu mai multe dispozitive AirPlay, puteți direcționa audio la mai mulți receptori simultan.

## Google Chromecast

Pentru utilizatorii Google Cast, pictograma Cast apare pe player. Atingeți-o pentru a alege un dispozitiv și a începe transmiterea. Asigurați-vă că telefonul și receptorul Cast sunt în aceeași rețea Wi-Fi. Nu fiecare codec este suportat de hardware-ul Chromecast — unele fișiere pot necesita transcodare.

## Fluxuri RTSP Live

Evervideo poate reda surse RTSP direct — camere IP, camere sonerie, fluxuri IPTV, fluxuri de difuzare și orice URL `rtsp://`. Adăugați fluxul ca o conexiune RTSP în Fișiere → Linkuri Online → Adăugare link, apoi atingeți pentru a începe vizionarea. Fluxurile RTSP funcționează în Picture-in-Picture, playerul compact și se transmit prin AirPlay 2 și Chromecast la fel ca un videoclip normal.

## Selectarea Pistei Audio

Pentru videoclipuri cu mai multe piste audio (comentariu, dublaje în limbi alternative, piste ale regizorului), atingeți butonul Mai Multe Acțiuni pe player și alegeți Pistă Audio — apoi selectați pista dorită. Aceasta este esențială pentru filmele în limbi străine, fișierele BDMV / MKV cu mai multe dublaje și conținut instrucțional cu piste de comentarii.

## Selectarea Pistei Video

Unele fișiere video includ mai multe fluxuri video (Blu-ray-uri multi-unghi, variante alternative). Alegeți Pistă Video din meniul Mai Multe Acțiuni pentru a comuta între ele în timpul redării.

## Subtitrări — Interne și Externe

Evervideo vă oferă control precis asupra subtitrărilor:

- **Pistă de subtitrări** — alegeți dintre pistele încorporate în fișier.
- **Fișiere de subtitrări externe** — încărcați fișiere `.srt`, `.vtt`, `.ass` sau `.ssa` de pe dispozitiv, iCloud Drive sau orice serviciu cloud conectat.
- **Randare Libass** — stilizarea avansată ASS / SSA (fonturi, culori, poziții, efecte karaoke) este redată corect datorită bibliotecii libass incluse.
- **Selectarea fontului** — alegeți un font personalizat pentru subtitrările primare și un font separat pentru subtitrările secundare. Fonturile incluse plus orice font instalat pe dispozitiv sunt disponibile.

Puteți configura toate acestea în Setări → Subtitrări înainte de redare, sau folosiți Mai Multe Acțiuni → Subtitrări din player pentru a schimba din mers.

## Egalizator Audio

Evervideo include un egalizator audio complet pentru a acorda benzile sonore video pentru căști, difuzoare sau sistem hi-fi. Atingeți pictograma egalizator pe controlul volumului (sau acțiunea Egalizator Audio în meniul Mai Multe Acțiuni al playerului), activați egalizatorul cu comutatorul din colțul din dreapta sus și fie alegeți un preset, fie trageți cursorii de bandă pentru a crea propriul preset. Preset-urile personalizate pot fi exportate și importate pentru a le partaja între dispozitive sau pentru backup.

## Egalizator Video

Pentru reglarea imaginii, Evervideo oferă un egalizator video dedicat — reglați luminozitatea, contrastul, saturația și nuanța în timp real în timpul redării. Ca și egalizatorul audio, preset-urile video personalizate pot fi exportate și importate pentru partajare sau backup. Folosiți-l pentru a lumina o scenă întunecată într-o zi însorită, a crește saturația conținutului decolorat sau a încălzi o nuanță de culoare rece.

{{< cards cols="1">}}
  {{< card title="" subtitle="Egalizatorul Video Evervideo" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Mod Scalare Video

Alegeți cum videoclipul umple ecranul:

- **Ajustare** — păstrați proporțiile originale; bare negre acolo unde este necesar.
- **Umplere** — umpleți tot ecranul, tăind videoclipul dacă este necesar.
- **Întindere** — întindeți videoclipul pentru a umple ecranul, distorsionând dacă este necesar.
- **Original** — păstrați rezoluția nativă la 1:1.

## Rotire Video

Pentru videoclipuri înregistrate cu orientarea greșită, alegeți **Mai Multe Acțiuni → Rotire** și selectați **0°**, **90°**, **180°** sau **270°** pentru a roti imaginea fără a ieși din player.

## Decodare Hardware (H.264 și HEVC)

În Setări → Player → Video, puteți activa / dezactiva Decodare Hardware H.264 și Decodare Hardware H.265 (HEVC) independent. Decodarea hardware este mai rapidă, folosește mai puțină baterie și funcționează mai rece — dar în cazuri rare (fișiere corupte, profiluri exotice) poate fi necesar să dezactivați decodarea hardware și să reveniți la decodarea software FFmpeg. Evervideo vă permite să faceți asta fișier cu fișier din meniul Mai Multe Acțiuni al playerului.

## Viewport VR 360°

Evervideo include un viewport VR / 360° pentru fișiere video sferice. Când redați un videoclip 360°, puteți trage pentru a privi în jur, ciupi pentru a mări, și Evervideo va deforma randarea în timp real.

## Viteză de Redare

Atingeți controlul Viteză pe bara de instrumente a playerului pentru a schimba viteza de redare — încetiniți pentru analiză (0,25× sau 0,5×) sau accelerați pentru tutoriale și prelegeri (1,25×, 1,5×, 2× și până la 3×). Atingeți pictograma de configurare din colțul din dreapta sus al ecranului Viteză pentru a comuta la modul precis cu ajustări mai fine. Corecția de tonalitate per pistă este de asemenea disponibilă.

{{< cards cols="1">}}
  {{< card title="" subtitle="Viteza de Redare pe Bara Principală de Instrumente Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Coada Playerului

Pentru a vedea coada playerului, atingeți butonul de coadă pe player. Fiecare videoclip din coadă are mai multe acțiuni — atingeți cele trei puncte pentru a le vedea. Pentru a reordona un videoclip în coadă, folosiți indicatorul de reordonare lângă titlu și trageți-l într-o nouă poziție.

{{< cards cols="1">}}
  {{< card title="" subtitle="Coada de Redare Evervideo" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Temporizator de Repaus

Deschideți Setări → Player → Temporizator de Repaus, activați-l și alegeți cât timp doriți să continue redarea înainte de oprire automată. Puteți adăuga și butonul Temporizator de Repaus direct pe ecranul principal al playerului prin Setări → Player → Personalizare → Acțiuni Ecran Principal.

## Marcaje Player

Salvați-vă locul în videoclipuri lungi — prelegeri, audiobook-uri video, tutoriale, descărcări lungi YouTube — atingând Adăugare Marcaj din meniul Mai Multe Acțiuni. Marcajele apar în lista Mai Multe Acțiuni → Marcaje a videoclipului și persistă între sesiuni.

## Meniu Mai Multe Acțiuni

Atingeți butonul **Mai Multe Acțiuni "..."** pe player pentru a accesa funcții suplimentare.

- **Continuare Redare** — reluați coada de la ultima poziție.
- **Căutare** — găsiți un videoclip specific în coadă.
- **Marcaje** — vizualizați și săriți la marcaje.
- **Viteză** — ajustați viteza de redare.
- **Recente** — videoclipuri redare recent.
- **Preferințe** — videoclipuri marcate ca favorite.
- **Egalizator Audio** — activați egalizatorul audio.
- **Egalizator Video** — activați egalizatorul video.
- **Pistă Audio** — alegeți fluxul audio.
- **Pistă Video** — alegeți fluxul video.
- **Subtitrări** — pistă primară / secundară, fișier extern, font.
- **Rotire** — rotiți imaginea 0° / 90° / 180° / 270°.
- **Mod Scalare** — Ajustare / Umplere / Întindere / Original.
- **Picture-in-Picture** — intrați în modul PiP.
- **AirPlay** / **Chromecast** — trimiteți la un dispozitiv.
- **Temporizator de Repaus** — setați un temporizator pentru oprirea redării.
- **Salvare Coadă ca Listă de Redare** — salvați coada curentă ca o nouă listă de redare.
- **Ștergere Coadă** — curățați coada și opriți redarea.
- **Setări** — mergeți direct la setările playerului.
- **Ajutor** — deschideți ghidul.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ecranul Mai Multe Acțiuni al Playerului Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Setările Playerului

Arborele complet de setări al Playerului este documentat în [ghidul Setări](/docs/guide/evervideo/evervideo-guide-settings/). Secțiunile cel mai frecvent utilizate:

- **General** — mod repetare, mod amestecare, Salvare Stare Player, Salvare Poziție Redare, intervale de omitere.
- **Video** — decodare hardware H.264 / HEVC, egalizator video, mod scalare, rotire, mod afișare, FPS preferat, format pixeli preferat, viewport VR.
- **Audio** — egalizator audio, rată eșantionare, canale, durată buffer IO, mod mixt.
- **Subtitrări** — pistă primară / secundară, selectare fișier extern, font, font secundar.
- **Dispozitive** (iOS) — AirPlay / Chromecast.
- **Personalizare** — stil layout player (Minimal / Jos / Antic / Clasic), acțiuni ecran principal, controale ecran de blocare.
- **Cache Redare** — cache pe disc pentru streaming mai fluid.
- **Temporizator de Repaus** — oprire automată.

## Accesibilitate

Evervideo este complet accesibil cu VoiceOver. Fiecare componentă are o etichetă și descriere bine concepute. Când VoiceOver este activ, aplicația comută la Modul Text pentru ca numai elementele semnificative să fie afișate — îmbunătățind viteza de navigare și claritatea. Puteți activa și Modul Text în Setări → Accesibilitate → Mod Text.

### Ajustarea Glisierelor cu VoiceOver

1. **Selectați glisiera** — glisați stânga sau dreapta până când VoiceOver o anunță.
2. **Ajustați valoarea** — atingeți de două ori și mențineți apăsată glisiera, apoi trageți în sus sau în jos pentru a schimba rapid valoarea. VoiceOver anunță noua valoare pe măsură ce avansați.

Celelalte componente funcționează ca de așteptat, folosind modelele VoiceOver furnizate de sistem.
