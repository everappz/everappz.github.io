---
title: "Exportați istoricul complet de ascultare din Evermusic și Flacbox pe Last.fm"
date: 2024-01-30
description: "Aflați cum să exportați istoricul muzical din Evermusic și Flacbox și să îl încărcați pe Last.fm folosind fișiere CSV și instrumentul Last.fm Scrubbler pentru Windows."
keywords: ["evermusic", "flacbox", "lastfm", "istoric muzical", "scrobbling", "export piese", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "recente", "lastfm", "export", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Rezumat:** Exportați istoricul de ascultare din Evermusic sau Flacbox ca fișier CSV, apoi încărcați-l pe Last.fm folosind instrumentul gratuit Last.fm-Scrubbler-WPF pe Windows. Scrobbling-ul automat este disponibil nativ și în ambele aplicații.

**Actualizare:** Scrobbling-ul automat este acum disponibil! Aflați mai multe aici: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling-ul este o modalitate simplă de a salva automat detalii de bază precum titlul și artistul melodiei pe care o ascultați într-un serviciu online. Mai târziu, puteți revizui istoricul de ascultare.

[Last.fm](https://www.last.fm/home), alimentat de un sistem de recomandare muzicală numit Audioscrobbler, oferă acest serviciu gratuit. Creează un profil detaliat al gusturilor dvs. muzicale prin înregistrarea pieselor pe care le ascultați, fie de la posturi de radio pe internet, de pe computer sau de pe diverse dispozitive muzicale portabile. Puteți vizita site-ul mai târziu pentru a primi recomandări de artiști sau albume noi care se potrivesc gusturilor dvs. muzicale.

Puteți încărca istoricul de ascultare pe [Last.fm](http://Last.fm) din aplicațiile Evermusic și Flacbox folosind un instrument gratuit, iar noi vă vom arăta cum să faceți acest lucru.

Deschideți secțiunea 'Biblioteca muzicală' a aplicației și derulați până la secțiunea 'Acces rapid'. Atingeți elementul de meniu 'Recente'.

![ecranul bibliotecii muzicale](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

Pe ecranul 'Recente', atingeți butonul 'Mai multe' din colțul din dreapta sus pentru a activa meniul 'Mai multe acțiuni'. Atingeți elementul de meniu 'Exportați lista de melodii'.

![ecranul recente](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

Pe ecranul 'Selectați formatul fișierului' aveți posibilitatea de a selecta formatul fișierului de destinație. Opțiuni disponibile - CSV, TXT, M3U.

![ecranul de selectare a formatului fișierului](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Aceasta înseamnă Comma-Separated Values, perfect pentru organizarea datelor într-un format de tabel ordonat. În fișierul de destinație, veți găsi parametri precum Numele Artistului, Numele Albumului, Numele Piesei, Marca temporală (momentul în care ați ascultat piesele), Numele Artistului Albumului și Durata Piesei.

TXT: Aici vorbim despre un fișier text simplu. Este simplu și direct, cu parametri care includ Numele Artistului, Numele Albumului, Numele Piesei și Durata.

M3U: Acest format este în esență alegerea principală pentru crearea listelor de redare. Este excelent deoarece puteți exporta lista de melodii și vă puteți bucura de piesele pe orice dispozitiv, chiar dacă nu aveți fișierele originale (cu condiția să selectați opțiunea URL absolut pentru fișierele media). În fișierul de ieșire, veți găsi parametri precum Durata, Numele Artistului, Numele Piesei și Locația Fișierului Media.

Pentru sarcina noastră, selectarea CSV este alegerea potrivită. Vom folosi acest fișier cu software-ul gratuit Last.fm-Scrubbler-WPF pentru a încărca istoricul nostru de ascultare pe serviciul [Last.fm](http://Last.fm). Pur și simplu alegeți CSV și apăsați butonul 'Export'.

![ecranul export finalizat](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

După ce exportul este finalizat, atingeți pur și simplu butonul 'Afișare fișier', iar aplicația va dezvălui fișierul creat în folderul dvs. de documente. Apoi, atingeți butonul 'Mai multe acțiuni' de lângă numele fișierului și selectați opțiunea 'Deschide în' din meniu. Următorul nostru pas este să copiem fișierul exportat pe computerul dvs. desktop. Puteți face acest lucru cu ușurință selectând opțiunea AirDrop din meniul 'Deschide în'.

![mai multe acțiuni pentru fișierul exportat](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

În continuare, vom folosi un client gratuit open-source [Last.FM](http://Last.FM) care este disponibil doar pe platforma Windows. Acest client vă permite să actualizați eficient istoricul de ascultare pe [Last.FM](http://Last.FM) folosind fișierul CSV pe care tocmai l-am exportat.

Acum, dacă nu utilizați în prezent un computer Windows, nu vă faceți griji. Puteți accesa în continuare acest client instalând VirtualBox pe Mac-ul dvs. și folosind fișierul oficial de imagine al mediului de dezvoltare Windows.

Iată ce trebuie să faceți:

- Instalați VirtualBox de la următorul link: [Descărcați VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Descărcați și instalați mediul de dezvoltare Windows de la acest link: [Mediu de Dezvoltare Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Pe computerul dvs. Windows (sau aplicația VirtualBox cu imaginea Windows Development) descărcați și instalați [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - software gratuit open-source disponibil pe GitHub. Am testat pe versiunea 1.28 pe care o puteți descărca aici: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Pagina de descărcare Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

În secțiunea 'Assets', faceți clic pe [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) pentru a descărca arhiva de instalare. Dezarhivați fișierul descărcat și deschideți folderul dezarhivat.

- IMPORTANT

Această aplicație este încă în versiune beta. Creatorii aplicației nu au efectuat multe teste. Aceștia recomandă să încercați mai întâi să faceți scrobble pe un cont de test și să vedeți dacă lucrurile pe care doriți să le scrobblați funcționează corect. Mai ales dacă faceți scrobble la multe piese deodată. Vă rugăm să fiți atenți cu conturile dvs.

Rulați Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Pe ecranul principal al aplicației, pur și simplu atingeți 'Neconectat', situat în colțul din stânga jos, pentru a activa ecranul 'Adăugare cont'.

![Ecranul de adăugare cont](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Introduceți datele dvs. de autentificare.

![ecranul de introducere a datelor de autentificare](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Atingeți butonul 'Login' pentru a adăuga contul dvs.

![Atingeți butonul Login pentru a adăuga contul dvs.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Deschideți fila 'File Parse Scrobbler' pentru a începe importul fișierului CSV din aplicația Evermusic.

![Deschideți fila File Parse Scrobbler pentru a începe importul fișierului CSV din aplicația Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Alegeți 'Parser: CSV' și atingeți butonul 'Settings'.

Pe ecranul următor, puteți alege ordinea parametrilor din fișierul dvs. CSV.

Câmpurile individuale pot fi incluse între ghilimele și TREBUIE să fie incluse între ghilimele dacă câmpul conține oricare dintre delimitatorii setați. De exemplu:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Așadar, lăsați toate setările implicite; singurul lucru pe care trebuie să-l schimbați este să activați caseta de selectare din câmpul 'Has Fields Enclosed In Quotes'.

Atingeți 'Save & Close' pentru a aplica modificările.

![alegeți ordinea parametrilor din fișierul dvs. CSV.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Scrobbling-ul prin parsarea fișierului are două moduri. Acestea pot fi schimbate cu ComboBox-ul 'Scrobbling Mode'.

Modul Normal: În acest mod, piesele vor fi scrobblate cu marca temporală din scrobble-ul parsat. Doar scrobble-urile mai noi de 14 zile pot fi scrobblate.

Modul Import: În acest mod, piesele vor fi scrobblate cu marca temporală calculată din 'Finish Time' și durata selectată între fiecare piesă. Aceasta permite scrobbling-ul pieselor chiar dacă marca temporală a scrobble-ului parsat este mai veche de 14 zile. Prin urmare, prima piesă (cea mai de sus) din fișierul CSV va fi scrobblată cu 'Finish Time'.

Alegeți un fișier CSV generat anterior din aplicația Evermusic în câmpul 'File:' și atingeți 'Parse'. În unele cazuri, este posibil să vedeți o alertă de eroare care spune că unele scrobble-uri nu au putut fi parsate. Este în regulă dacă aveți unele piese fără metadate complete, cum ar fi Numele Artistului.

![unele scrobble-uri nu au putut fi parsate](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Atingeți butonul 'Check All' pentru a selecta toate piesele parsate.

![Atingeți butonul Check All pentru a selecta toate piesele parsate.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Atingeți butonul 'Preview' pentru a verifica toate modificările care vor fi trimise la server.

![Atingeți butonul Preview pentru a verifica toate modificările care vor fi trimise la server.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Atingeți butonul 'Scrobble' pentru a încărca toate modificările pe server.

![Atingeți butonul Scrobble pentru a încărca toate modificările pe server.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Anterior, Last.fm-Scrubbler-WPF nu avea o limită de scrobble-uri pe zi. Acest lucru s-a schimbat acum, deoarece unele persoane au folosit Scrubbler-ul pentru a scrobbla atât de multe piese încât a cauzat probleme pentru pagina Last.fm. Limita de scrobble-uri este în prezent de 2800 de scrobble-uri pe zi. Când încercați să scrobblați mai mult decât atât, veți primi un mesaj de eroare. Există planuri de a adăuga o 'coadă de scrobble-uri', astfel încât dacă trebuie să scrobblați mai mult de 2800 de piese, acestea sunt adăugate la o coadă și sunt scrobblate automat după ceva timp. Puteți verifica câte scrobble-uri v-au mai rămas în vizualizarea de selecție a utilizatorului.

Odată ce toate înregistrările sunt încărcate cu succes pe server, veți vedea un mesaj în partea de jos a ferestrei aplicației care confirmă: 'Successfully scrobbled selected tracks.'

![Successfully scrobbled selected tracks.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Acum puteți deschide profilul dvs. pe pagina [Last.fm](http://Last.fm) și verifica toate modificările.

![profilul dvs. pe pagina Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Întrebări frecvente

{{% details title="Pot face scrobble automat fără a exporta fișiere CSV?" closed="true" %}}
Da. Atât Evermusic, cât și Flacbox acceptă acum scrobbling-ul automat pe Last.fm. Consultați ghidul: [Cum să faceți scrobble pe Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Ce se întâmplă dacă CSV-ul meu are piese mai vechi de 14 zile?" closed="true" %}}
Folosiți Modul Import în Last.fm-Scrubbler-WPF. Acesta recalculează mărcile temporale din Finish Time, permițându-vă să scrobblați piese indiferent de data lor originală.
{{% /details %}}

{{% details title="Nu am un computer Windows. Pot folosi totuși Last.fm-Scrubbler?" closed="true" %}}
Da. Instalați VirtualBox pe Mac-ul dvs. și descărcați imaginea gratuită a Mediului de Dezvoltare Windows de la Microsoft. Rulați Last.fm-Scrubbler-WPF în mașina virtuală.
{{% /details %}}

{{% details title="De ce nu sunt parsate unele scrobble-uri?" closed="true" %}}
Piesele cărora le lipsesc metadate esențiale (cum ar fi numele artistului) nu pot fi parsate. Acest lucru este așteptat și nu afectează alte piese din fișier.
{{% /details %}}

{{% details title="Există o limită zilnică de scrobble-uri?" closed="true" %}}
Da. Last.fm-Scrubbler-WPF permite până la 2.800 de scrobble-uri pe zi. Dacă trebuie să scrobblați mai multe, împărțiți procesul pe mai multe zile.
{{% /details %}}
