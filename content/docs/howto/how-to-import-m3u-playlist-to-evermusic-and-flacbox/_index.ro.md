---
title: "Cum să importați o listă de redare M3U în Evermusic și Flacbox"
date: 2024-01-31
description: "Aflați cum să importați fișiere de liste de redare M3U, M3U8 și CUE din cloud, stocare locală sau dispozitiv în Evermusic și Flacbox."
keywords: ["evermusic", "flacbox", "listă de redare", "m3u", "m3u8", "cue", "import", "aplicație muzică"]
tags: ["evermusic", "import", "liste de redare", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Rezumat:** Evermusic și Flacbox acceptă importul fișierelor de liste de redare M3U, M3U8 și CUE din stocarea cloud, fișierele locale ale aplicației sau dispozitivul dvs. Accesați Liste de redare > Mai multe > Importare listă de redare, selectați o sursă, alegeți fișierul și aplicația creează automat lista de redare.

M3U, care înseamnă MP3 URL sau Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, este un format de fișier de computer utilizat pentru liste de redare multimedia. Una dintre utilizările sale principale este crearea fișierelor de liste de redare cu o singură intrare care indică fluxuri pe internet. Aceste fișiere oferă acces convenabil la conținut streaming și sunt utilizate în mod obișnuit pentru descărcări, e-mail și ascultarea radioului pe Internet.

În ciuda utilizării sale pe scară largă, nu există o specificație formală pentru formatul M3U; a devenit un standard de facto. Un fișier M3U este în esență un fișier text simplu care specifică locațiile unuia sau mai multor fișiere media. În funcție de codificare, este salvat cu extensia "m3u" sau "m3u8". Fiecare intrare din fișier specifică locația unui fișier media, care poate fi o cale locală absolută, o cale locală relativă la locația fișierului M3U sau un URL. Intrările sunt separate prin întreruperi de linie, unele dispozitive necesitând întreruperi de linie reprezentate ca CR LF.

În plus, fișierele M3U pot include comentarii prefixate cu caracterul "#". În M3U extins, "#" introduce directive M3U extinse, care pot accepta parametri terminați cu două puncte ":".

În aplicațiile noastre Evermusic și Flacbox, am implementat funcționalitatea de import a fișierelor M3U, eliminând necesitatea creării manuale a listelor de redare. Acest ghid vă va ghida prin importul listelor de redare din stocarea cloud, fișiere locale sau fișiere de pe dispozitivul dvs. direct în aplicație.

Mai întâi, navigați la secțiunea 'Liste de redare'. Apoi, atingeți butonul 'Mai multe' situat în colțul din dreapta sus. Din meniul care apare, selectați opțiunea 'Importare listă de redare'.

![acțiune de import listă de redare](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Pe ecranul următor, alegeți locația fișierului. Opțiunile acceptate includ:

- Stocare cloud conectată;
- Fișiere în aplicație;
- Fișiere pe dispozitivul dvs.;

![selectare locație fișier](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Să selectăm stocarea cloud conectată și să deschidem folderul care conține fișierul listei de redare. Extensiile de fișier acceptate pentru liste de redare includ M3U, M3U8 și CUE. Selectați fișierul listei de redare și atingeți 'Finalizat' pentru a confirma selecția.

![selectare fișier M3U](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Aplicația va analiza fișierul listei de redare și va crea o listă de piese. Apoi va localiza aceste fișiere în stocare și va compila o listă de redare finală care va fi importată în biblioteca muzicală. Este esențial ca fișierul dvs. M3U/CUE să conțină căile corecte pentru fișierele media, iar fișierele trebuie să fie localizate la aceste căi în stocarea dvs.

![listă de redare importată](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Aplicația acceptă atât căi relative, cât și URL-uri absolute de fișiere.

De exemplu:

Listă de redare cu căi relative:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Listă de redare cu URL-uri absolute:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Dacă importați un fișier de listă de redare situat în aplicație (secțiunea Fișiere locale), nu sunt necesari pași suplimentari.

Cu toate acestea, dacă doriți să importați o listă de redare situată pe dispozitivul dvs. folosind selectorul de fișiere al sistemului, există o considerație importantă de reținut.

Din cauza politicilor de securitate, aplicația poate accesa doar fișierul pe care îl selectați folosind selectorul de fișiere al sistemului. Cu toate acestea, fișierul listei de redare poate include link-uri către alte fișiere media de pe dispozitivul dvs. Pentru a importa o listă de redare de pe dispozitiv, trebuie să selectați un folder care conține atât fișierul listei de redare, cât și toate fișierele media asociate. În acest caz, aplicația va scana folderul selectat, va găsi fișierul listei de redare, va construi lista de piese și o va importa în biblioteca muzicală.

În plus, puteți importa mai multe liste de redare simultan atingând butonul "Mai multe acțiuni" și selectând "Importare liste de redare dintr-un folder". Aplicația va scana conținutul folderului, va găsi fișierele de liste de redare acceptate și le va importa în bibliotecă.

## Întrebări frecvente

{{% details title="Ce formate de liste de redare acceptă Evermusic și Flacbox?" closed="true" %}}
Ambele aplicații acceptă formatele de fișiere de liste de redare M3U, M3U8 și CUE. Acestea acoperă cele mai comune standarde de liste de redare utilizate de playerele muzicale și software-ul media.
{{% /details %}}

{{% details title="Pot importa liste de redare din stocarea cloud?" closed="true" %}}
Da. Puteți importa fișiere de liste de redare din orice serviciu de stocare cloud conectat, inclusiv Google Drive, Dropbox, OneDrive și servere WebDAV.
{{% /details %}}

{{% details title="De ce lipsesc unele piese după import?" closed="true" %}}
Fișierul listei de redare trebuie să conțină căi corecte către fișierele dvs. media, iar acele fișiere trebuie să existe la locațiile specificate în stocarea dvs. Verificați dacă căile fișierelor din fișierul M3U sau CUE corespund locațiilor reale ale fișierelor.
{{% /details %}}

{{% details title="Pot importa mai multe liste de redare simultan?" closed="true" %}}
Da. Folosiți butonul Mai multe acțiuni și selectați "Importare liste de redare dintr-un folder". Aplicația scanează folderul pentru toate fișierele de liste de redare acceptate și le importă într-un singur pas.
{{% /details %}}

{{% details title="Trebuie să creez listele de redare manual?" closed="true" %}}
Nu. Funcția de import elimină crearea manuală a listelor de redare. Pur și simplu îndreptați aplicația către fișierul M3U, M3U8 sau CUE existent și aceasta creează automat lista de redare.
{{% /details %}}
