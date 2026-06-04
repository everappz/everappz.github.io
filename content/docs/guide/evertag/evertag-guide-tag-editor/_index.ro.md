---
title: "Editor de Etichete"
date: 2020-02-01
description: "Aflați cum să utilizați Editorul de Etichete Evertag pentru a actualiza metadatele muzicale, a edita coperțile de albume, a edita în lot mai multe fișiere și a gestiona etichetele din MusicBrainz. Ideal pentru organizarea bibliotecii dvs. muzicale pe iOS și Mac."
keywords: [
  "Evertag editor etichete", "editor metadate audio", "editor etichete muzicale",
  "editare etichete audio iPhone", "editor copertă album", "editare în lot etichete audio",
  "metadate MusicBrainz", "aplicație organizare muzică", "ghid Evertag", "editor etichete ID3"
]
tags: ["ghid", "evertag", "editor etichete"]
readingTime: 5
---


**Editorul de Etichete** este ecranul principal al aplicației Evertag unde puteți vizualiza și edita metadatele fișierelor audio. Deschideți acest ecran apăsând pe un fișier din secțiunea **Fișiere Locale** sau din orice cont de **stocare în cloud** conectat.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Tag Editor Screen" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Moduri de Editare

Evertag oferă două moduri de editare:

- **Modul fișier unic**  
  - Navigați între fișiere prin glisare la stânga sau la dreapta pe caruselul de coperți.  

- **Modul lot**  
  - Editați mai multe fișiere simultan și aplicați metadate comune.  
  - Pentru activare, derulați în jos și apăsați **Editați mai multe fișiere simultan**.

## Modul Fișier Unic

În mod implicit, aplicația deschide editorul de etichete în modul fișier unic cu doar opțiunile principale de editare activate. În acest mod, puteți edita cele mai comune câmpuri de metadate, cum ar fi:

**Titlu Piesă, Subtitlu, Artist Album, Album, Artist, Compozitor, Interpret, Gen, Comentariu, Bătăi Pe Minut, Podcast, Compilație, Număr Disc, Număr Piesă, Total Piese, Clasificare, An**

Pentru a accesa toate etichetele disponibile, derulați în jos pe ecran și apăsați opțiunea **Afișați Etichete Extinse**. Aceasta va comuta editorul în modul extins, permițându-vă să editați peste **120 de câmpuri de metadate**, inclusiv **Etichete MusicBrainz**, **Versuri**, **Clasificări de Avertisment**, valori replay-gain, ordini de sortare, metadate podcast și altele. Utilizați **Setări → Editor etichete audio → Butoane pe ecranul principal** pentru a activa permanent Afișați Etichete Extinse astfel încât să fie întotdeauna activat.

{{< cards cols="1">}}
{{< card title="" subtitle="Bottom Actions Panel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Modul Lot

Puteți intra în editarea în lot în două moduri:

1. **Din Managerul de Fișiere**  
   - Apăsați **Mai multe acțiuni** (•••) în colțul din dreapta sus.  
   - Apăsați **Selectați**, alegeți mai multe fișiere și apoi apăsați **Editați etichetele audio**.

2. **Din Editorul de Etichete**  
   - Deschideți orice fișier, derulați în jos și apăsați **Editați fișierele simultan** pentru a încărca toate fișierele din același folder.

{{< cards cols="1">}}
{{< card title="" subtitle="Batch Editing Mode" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

După editare, apăsați **Salvați** pentru a aplica modificările.

## Editați Versuri

Editorul extins expune câmpul **Versuri**. Apăsați pe el pentru a deschide lista de versuri — fiecare intrare de versuri are propriul limbă și descriere, astfel încât o singură piesă poate stoca mai multe traduceri.

Nu trebuie să tastați versurile de la zero. Editorul include comenzi rapide de căutare cu o singură atingere la cele mai populare baze de date de versuri de pe web, pre-completate cu artistul și titlul piesei curente:

- **Lrclib** — baza de date publică preferată pentru **versuri sincronizate (stil LRC)**. Folosiți-o când doriți versuri sincronizate care defilează linie cu linie în playerele care le suportă.
- **Genius** — catalog mare cu adnotații și versuri text simplu precise.
- **Lyricsify** — bază de date bazată pe comunitate cu versuri simple și cu marcaje temporale.
- **Google** — o căutare web generală ca alternativă când bazele de date dedicate nu au o potrivire.

Fiecare comandă rapidă apare doar când serviciul corespunzător este accesibil de pe dispozitivul dvs. Apăsați un serviciu, copiați versurile (sau marcajele temporale LRC) pe care le doriți, reveniți la Evertag și lipiți-le în câmpul de text — apoi **Salvați** pentru a scrie versurile înapoi în etichetele fișierului audio.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Pages" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Alegeți o limbă din selector:

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Language Selector" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Apoi lipiți sau tastați textul versurilor. Evertag suportă atât text simplu cât și versuri sincronizate — placeholder-ul arată un exemplu al formatului LRC, care este exact ceea ce Lrclib și Lyricsify returnează pentru rezultate sincronizate.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Text Editor" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Setați o Clasificare și Clasificare de Avertisment

Editorul extins oferă un control de stele **Clasificare** alături de un control segmentat **Clasificare de Avertisment**.

### Clasificare cu Stele

Utilizați câmpul **Clasificare** pentru a da unei piese un scor personal de la una la cinci stele. Valoarea este scrisă în câmpul standard de clasificare al fișierului (POPM pentru ID3, `rate` pentru MP4, `RATING` pentru Vorbis/APE, etc.), astfel că alte aplicații care citesc această etichetă — inclusiv aplicația Music, Plex, Roon și majoritatea editorelor de etichete de desktop — vor prelua imediat scorurile dvs.

{{< cards cols="1">}}
  {{< card title="" subtitle="Rating" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Clasificare de Avertisment

**Clasificarea de Avertisment** marchează conținutul unei piese folosind una din valorile standardului Parental Advisory pe care iTunes Store și majoritatea platformelor muzicale îl folosesc:

- **Fără restricții** — valoarea implicită pentru piesele fără informații de aviz parental. Fișierul este tratat ca potrivit pentru toți ascultătorii și nu va afișa nicio etichetă de avertisment în playerele care respectă eticheta.
- **Explicit** — piesa conține limbaj sau conținut explicit. Playerele care respectă controalele parentale (aplicația Music, aplicația Apple TV, exporturi Spotify, Plex, etc.) vor afișa un insignă **E** lângă titlu și, când restricțiile sunt activate pe dispozitiv sau cont, pot ascunde piesa din profilurile copiilor sau pot refuza să o redea.
- **Curat** — o versiune cenzurată sau editată a unei piese altfel explicite. Playerele afișează o insignă **C** pentru ca ascultătorii să poată distinge o editare curată de masterul explicit original, ceea ce este util când ambele versiuni trăiesc în aceeași bibliotecă.

Va trebui să setați sau să corectați acest câmp când:

- Un fișier are eticheta greșită (de exemplu, o editare radio curată care a fost etichetată greșit ca Explicit, sau invers).
- Piesele au fost extrase sau descărcate fără etichetă și acum sunt afișate ca Fără restricții chiar dacă conțin conținut explicit — necesar pentru ca controalele parentale și bibliotecile partajate în familie să funcționeze corect.
- Pregătiți un album pentru depunere sau partajare și trebuie ca fiecare piesă să aibă metadate consecvente.
- Doriți ca CarPlay, Ecranul de Blocare, playere în stil Apple Music sau software DJ să afișeze insigna **E** / **C** corectă lângă titlul piesei.

Valoarea este stocată în câmpul standard de clasificare de avertisment pentru formatul fișierului (`rtng` pentru MP4, `TXXX:ITUNESADVISORY` pentru ID3, `ITUNESADVISORY` pentru Vorbis), astfel că orice player care citește metadate de aviz parental va vedea actualizarea dvs.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Advisory Rating" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Editați Coperta Albumului

Pentru a schimba o copertă de album:

1. Apăsați pictograma **Cameră** în caruselul de coperți.  
2. Alegeți locația imaginii: Fișiere Locale, Cloud, Descărcări sau Biblioteca de Fotografii.  
3. Selectați o imagine pentru a aplica ca artă de copertă.

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Image" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Mai Multe Acțiuni în Editorul de Etichete

Opțiuni de editare suplimentare sunt disponibile prin bara de instrumente de sub vizualizarea coperților.

{{< cards cols="1">}}
  {{< card title="" subtitle="More Actions Menu" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Căutare Automată Etichete Audio

Această acțiune activează motorul de căutare inteligent de etichete, care găsește și completează metadate complete pentru fișierul dvs. audio pe baza informațiilor existente.  
Aplicația folosește baza de date MusicBrainz — una dintre cele mai cuprinzătoare baze de date de etichete — cu peste **50 de milioane** de piese.

### Căutare Copertă Album

Folosiți metadate pentru a căuta pe web arta corectă a albumului.  

{{< cards cols="1">}}
  {{< card title="" subtitle="Search Album Cover" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Odată găsită, salvați imaginea în **Fotografii** folosind meniul contextual al sistemului.

{{< cards cols="1">}}
  {{< card title="" subtitle="Add Image to Photos" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

După aceea, reveniți la editorul de etichete, apăsați pictograma Cameră, mergeți la **Biblioteca de Fotografii** și selectați imaginea salvată. Aplicația o va seta ca coperta fișierului dvs. audio.

Puteți ajusta modul în care imaginile de copertă sunt scalate în setările aplicației.

### Salvare Artă Album

Această acțiune salvează arta curentă a albumului în folderul **Documente**, astfel încât să o puteți reutiliza mai târziu.

### Normalizare Codificare

Această acțiune va normaliza codificarea textului tuturor etichetelor din metadatele fișierului audio. Este deosebit de utilă dacă faceți tranziția de la un PC cu Windows, unde fișierele pot folosi codificări diferite care apar ca caractere ilizibile sau corupte pe un Mac.

### Căutare Manuală Etichete

Căutați manual metadate de album folosind baza de date MusicBrainz.  

- Selectați albumul  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Alegeți piesa corectă  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Song" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Alegeți ce etichete să aplicați  

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Audio Tags" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Apăsați **Finalizat** pentru a aplica metadatele selectate piesei dvs.

### Ștergere Etichete Audio

Ștergeți toate câmpurile de metadate pentru un fișier. Util când se pornește de la zero. Apăsați **Salvați** pentru a confirma.

## Setări Editor de Etichete

Navigați la **Setări → Editor etichete audio** pentru a personaliza comportamentul.

### Scalarea Copertei Albumului

Selectați modul în care coperțile de album ar trebui scalate când sunt salvate în fișiere audio. Puteți dezactiva scalarea pentru a păstra dimensiunea originală a imaginii, dar rețineți că unele playere s-ar putea să nu suporte fișiere de copertă mari. Opțiunea "dimensiunea originală" face parte din funcțiile de personalizare Premium.

### Opțiuni de Salvare Etichete

- **ID3v2.4** — când este activat, aplicația salvează etichetele în format ID3v2.4 când este posibil. Dezactivați pentru a reveni la ID3v2.3 mai larg suportat dacă etichetele audio nu sunt afișate corect pe playere sau dispozitive mai vechi.
- **Etichete duplicate** — când este activat, câmpurile de metadate comune sunt duplicate în ambele secțiuni de etichete ale fișierului. Aceasta îmbunătățește compatibilitatea cu playerele audio mai vechi, dar în majoritatea cazurilor nu este necesară.

### Opțiuni de Actualizare Metadate Fișier Cloud

Puteți controla modul în care aplicația actualizează metadatele pentru fișierele audio stocate în servicii cloud:

- **Afișare mesaj de confirmare**  
  Cereți confirmare înainte de a aplica modificări de metadate la fișierele cloud.

- **Actualizare automată a metadatelor fișierului**  
  Salvați modificările de metadate în fișierul cloud automat după editare.

- **Nu actualizați metadatele fișierului**  
  Ignorați actualizarea fișierelor cloud — modificările se vor aplica doar local.

### Editare Fișiere Online

Alegeți ce se întâmplă cu copiile local descărcate ale fișierelor cloud după editare:

- **Ștergeți întotdeauna fișierul descărcat**  
  Eliminați copia locală după salvarea modificărilor.

- **Nu ștergeți fișierul descărcat**  
  Păstrați fișierul descărcat pe dispozitivul dvs. după editare.

### Butoanele Ecranului Principal

Personalizați ce acțiuni apar pe ecranul principal al editorului de etichete (Căutare automată etichete, Căutare manuală etichete, Căutare copertă album, Salvare artă album, Normalizare codificare, Ștergere etichete audio). Puteți, de asemenea, activa/dezactiva **Afișați etichete extinse** și **Editați fișierele simultan** astfel încât editorul să se deschidă întotdeauna în modul dvs. preferat.
