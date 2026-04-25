---
title: "Cum să transferați biblioteca muzicală între dispozitive în Evermusic: ghid pas cu pas"
description: "Transferați cu ușurință biblioteca muzicală Evermusic, listele de redare, copertele albumelor și setările de pe un iPhone, iPad sau Mac pe altul folosind Wi-Fi Drive și instrumente de backup."
date: 2024-12-29
tags: ["bibliotecamuzicala", "transfer", "wifi", "backup", "webdav", "restaurare"]
keywords: ["transfer bibliotecă muzicală Evermusic", "backup și restaurare liste de redare Evermusic", "Evermusic WiFi Drive", "sincronizare Evermusic între dispozitive", "mutare bază de date Evermusic", "transfer fișiere Evermusic", "restaurare setări player audio", "transfer muzică WebDAV iOS"]
readingTime: 3
---

{{< author-byline >}}


**Rezumat:** Pentru a transfera biblioteca Evermusic pe un dispozitiv nou, creați un backup pe dispozitivul sursă, porniți Wi-Fi Drive, conectați al doilea dispozitiv prin aceeași rețea, descărcați backup-ul și fișierele muzicale, apoi restaurați din backup. Întregul proces durează aproximativ 10 minute, în funcție de dimensiunea bibliotecii.

În acest ghid, vă vom ghida prin transferul întregii biblioteci muzicale — inclusiv baza de date, copertele albumelor și setările — de pe un dispozitiv (iPhone sau Mac) pe altul. Deși sincronizarea automată a bibliotecii muzicale și a listelor de redare este o funcție planificată pentru viitor, acest proces trebuie în prezent realizat manual.

## Pasul 1: Creați un backup pe primul dispozitiv

1. **Deschideți aplicația pe primul dispozitiv** (cel cu biblioteca muzicală, listele de redare și serviciile cloud conectate).
2. **Navigați la Setări** și selectați opțiunea **Backup și Restaurare**.

![Backup and Restore](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. Pe ecranul **Backup și Restaurare**, alegeți elementele de inclus în fișierul de backup:
   - **Baza de date** (include biblioteca muzicală și listele de redare)
   - **Coperte album**
   - **Setări**

Aceste opțiuni sunt activate implicit.

![Backup Options](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Atingeți **Backup date aplicație** pentru a începe procesul.

![Backup Application Data](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Odată ce backup-ul este complet, va apărea o alertă informativă.

![Backup Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Atingeți **Afișare fișier** pentru a dezvălui fișierul de backup în directorul **Documente**. Fișierele de backup sunt de obicei salvate în folderul **Backup**.

![Show Backup File](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Pasul 2: Porniți serverul Wi-Fi Drive

1. Mergeți la secțiunea **Conexiuni** din aplicație.
2. Derulați în jos la **Conectare prin Wi-Fi** și atingeți.

![Connect Using Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. Pe ecranul următor, atingeți **Pornire Wi-Fi Drive**.

- Opțional, puteți seta un login și o parolă pentru securitate, dar acest lucru nu este necesar pentru rețelele de acasă.

4. Odată pornit, veți vedea adresele de server disponibile. Acestea pot fi utilizate pentru browsere desktop sau aplicații WebDAV, dar în acest ghid, vom continua direct la pașii următori.

![Wi-Fi Drive Started](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Pasul 3: Conectați al doilea dispozitiv la primul

1. Deschideți aplicația pe al doilea dispozitiv (unde doriți să transferați biblioteca).
2. Asigurați-vă că ambele dispozitive sunt conectate la aceeași rețea Wi-Fi.
3. Pe al doilea dispozitiv, deschideți fila **Conexiuni** și selectați **Dispozitive disponibile**.

![Available Devices](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Ar trebui să vedeți o conexiune WebDAV numită **Evermusic** (serverul pe care l-am pornit pe primul dispozitiv). Atingeți pentru a vă conecta.

5. Odată conectat, veți vedea toate folderele de pe primul dispozitiv.

![Connected to First Device](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Pasul 4: Pregătiți transferul fișierelor

1. Pe al doilea dispozitiv, mergeți la **Setări > Manager fișiere** și activați **Salvare fișiere descărcate în - Întreabă de fiecare dată**.

- Aceasta vă asigură că puteți selecta folderul de destinație pentru fiecare descărcare.

2. Reveniți la fila **Conexiuni** și navigați la serverul WebDAV conectat.

![Prepare for File Transfers](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Pasul 5: Transferați backup-ul și fișierele muzicale

1. Deschideți folderul **Backup** de pe serverul WebDAV conectat.

![Backup Folder](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Atingeți butonul **Mai multe acțiuni** (trei puncte) lângă fișierul de backup și selectați **Descărcați**.

3. Creați un folder **Backup** pe al doilea dispozitiv pentru a stoca fișierele descărcate. Confirmați selecția atingând **Finalizat**.

![Download Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Transferați orice fișiere muzicale suplimentare:
   - Verificați folderul **Descărcări** sau alte foldere relevante de pe serverul WebDAV.

![Transfer Music Files](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Folosiți opțiunea **Selectați** pentru a alege fișierele, apoi atingeți **Mai multe acțiuni > Descărcați**. Salvați-le în folderul corespunzător de pe al doilea dispozitiv pentru a menține aceeași structură de directoare.

Scopul este de a transfera toate fișierele de pe primul dispozitiv pe dispozitivul actual, asigurându-vă că structura de foldere rămâne identică. În acest fel, legăturile din biblioteca muzicală și listele de redare rămân intacte. Rețineți că fișierele locale stocate în afara directorului Documente al aplicației de pe primul dispozitiv trebuie transferate separat. Deoarece aplicația nu poate accesa aceste fișiere în modul Wi-Fi Drive, va trebui să folosiți aplicația Fișiere Sistem pentru transfer.

![Transfer Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Pasul 6: Monitorizați progresul transferului

1. Pe al doilea dispozitiv, mergeți la secțiunea **Fișiere locale** (sau fila **Descărcări** pe iPad/Mac).

2. Atingeți butonul **Activitate transfer** din colțul din stânga sus pentru a monitoriza coada de transfer.

![Monitor Transfer](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Pasul 7: Restaurați datele din backup

1. Odată ce fișierul de backup și toate fișierele audio necesare sunt descărcate pe al doilea dispozitiv, deschideți folderul **Backup**.

2. Atingeți fișierul de backup și va apărea un mesaj de confirmare.

![Restore Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Notă:** Restaurarea va înlocui toate datele actuale ale bibliotecii muzicale, listele de redare, setările și copertele albumelor cu datele din backup.

3. Atingeți **Restaurare** pentru a începe procesul.

![Restore Process](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. După finalizarea restaurării, o alertă va confirma succesul.

![Restoration Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Verificați secțiunile **Liste de redare** sau **Bibliotecă muzicală** pentru a confirma restaurarea.

![Verify Restoration](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Pasul 8: Reindexați biblioteca muzicală

1. Pentru cele mai bune rezultate, reindexați biblioteca pentru a vă asigura că toate fișierele sunt detectate cu succes.

2. Mergeți la **Setări > Bibliotecă muzicală > Sincronizare muzică offline** și selectați **Pornire scanare foldere locale**.

Urmând acești pași, veți transfera cu succes biblioteca muzicală, listele de redare și setările pe alt dispozitiv. Dacă întâmpinați probleme, nu ezitați să contactați suportul.

## Întrebări frecvente

{{% details title="Pot transfera biblioteca Evermusic fără Wi-Fi?" closed="true" %}}
Wi-Fi Drive necesită ca ambele dispozitive să fie pe aceeași rețea Wi-Fi. În prezent nu există opțiune de transfer prin Bluetooth sau celular. Ca alternativă, puteți utiliza AirDrop sau aplicația Fișiere pentru a muta manual fișierul de backup și folderele muzicale între dispozitive.
{{% /details %}}

{{% details title="Conexiunile serviciilor cloud se transferă cu backup-ul?" closed="true" %}}
Backup-ul include baza de date, listele de redare, copertele albumelor și setările. Credențialele de autentificare ale serviciilor cloud nu sunt incluse din motive de securitate. Va trebui să reconectați conturile cloud pe noul dispozitiv după restaurare.
{{% /details %}}

{{% details title="Ce se întâmplă cu biblioteca existentă de pe al doilea dispozitiv?" closed="true" %}}
Restaurarea unui backup înlocuiește toate datele existente ale bibliotecii muzicale, listele de redare, setările și copertele albumelor de pe al doilea dispozitiv. Faceți mai întâi un backup separat al celui de-al doilea dispozitiv dacă doriți să păstrați datele sale.
{{% /details %}}

{{% details title="Funcționează acest proces între iPhone și Mac?" closed="true" %}}
Da. Evermusic suportă transferul Wi-Fi Drive între orice combinație de iPhone, iPad și Mac. Ambele dispozitive trebuie doar să fie pe aceeași rețea Wi-Fi.
{{% /details %}}

{{% details title="Cât durează transferul?" closed="true" %}}
Timpul de transfer depinde de dimensiunea bibliotecii muzicale și de viteza Wi-Fi. O bibliotecă tipică de câțiva gigabytes se transferă în 5-15 minute printr-o rețea de acasă standard.
{{% /details %}}
