---
title: "Prijenos datoteka s računala na iPhone pomoću SMB protokola"
description: "Naučite kako prenijeti i pristupiti velikim datotekama s vašeg Maca ili Windows PC-a na vaš iPhone ili iPad koristeći Evermusic i SMB protokol. Vodič korak po korak za besprijekorno streamanje i upravljanje datotekama."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["prijenos datoteka na iPhone SMB", "streamanje glazbe s PC-a na iPhone", "povezivanje Maca s iPhoneom SMB", "postavljanje Evermusic SMB", "pristup datotekama računala iPhone", "dijeljenje glazbe Windows iOS", "SMB prijenos datoteka Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Sažetak:** Koristite Evermusic na svom iPhoneu ili iPadu za pristup datotekama pohranjenim na vašem Macu ili Windows PC-u putem lokalne mreže preko SMB-a. Bez kabela, bez iTunesa, bez potrebe za upload u oblak. Omogućite dijeljenje datoteka na računalu, povežite se u aplikaciji i pregledavajte ili reproducirajte datoteke bežično.

Imate li opsežnu kolekciju velikih datoteka na svom MAC-u ili PC-u i želite im pristupiti bez napora s iPhonea ili iPada? Naše aplikacije pružaju jednostavno rješenje.

Slijedite ove korake za omogućavanje besprijekornog pristupa između vašeg računala i iOS uređaja koristeći SMB protokol:

## Korak 1: Omogućite SMB protokol na svom računalu

**Za MAC:**

1. Otvorite "Postavke sustava" na svom MAC-u.
2. Kliknite na "Dijeljenje".
3. Omogućite uslugu "Dijeljenje datoteka".
4. Dodajte mapu s glazbom u odjeljak "Dijeljene mape". Dodajte korisnika i odaberite razinu dopuštenja (Čitanje i pisanje ili Samo čitanje). Možete odabrati "Svi: Samo čitanje" za dodanu mapu s glazbom.

   ![Zaslon postavki Maca](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Zapamtite URL računala (smb://192.168.xx.xx) jer ćete ga koristiti u sljedećim koracima.
6. Kliknite na "Opcije" i aktivirajte "Dijeljenje datoteka i mapa putem SMB-a".

   ![Zaslon dijeljenja datoteka Maca](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Omogućite "Dijeljenje Windows datoteka" za dostupne račune.

   ![Zaslon SMB dijeljenja Maca](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Za Windows PC:**

1. Desnom tipkom miša kliknite na mapu s glazbom.
2. Odaberite "Svojstva".
3. Idite na karticu "Dijeljenje".
4. Kliknite na "Dijeli..."
5. Odaberite osobe s kojima želite dijeliti mapu i odredite razinu dopuštenja. Možete odabrati "Svi: Čitanje" za odabranu mapu s glazbom.

   ![Zaslon SMB dijeljenja Windowsa](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Kliknite "Završeno".
7. Kliknite "Završeno" u prozoru "Dijeljenje datoteka" i zapamtite putanju mape.

   ![Dijeljena SMB mapa Windowsa](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Korak 2: Povežite svoj iOS uređaj

1. Otvorite aplikaciju na svom iPhoneu ili iPadu.
2. Idite na karticu "Povezivanja".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Zaslon Povezivanja u Evermusicu"
  caption="Zaslon Povezivanja u Evermusicu"
  width="400"
>}}

*Ako se vaše računalo pojavi u odjeljku "Dostupni uređaji":*

Ako je vaše računalo vidljivo u odjeljku "Dostupni uređaji" i odabrali ste "Svi: Samo čitanje" u prethodnom koraku, jednostavno dodirnite svoje računalo i automatski će se povezati.

*Ako se vaše računalo ne pojavi automatski:*

1. Dodirnite "Poveži se s uslugom u oblaku".
2. Odaberite "SMB" na zaslonu "Poveži se s uslugom u oblaku".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Zaslon Poveži se s uslugom u oblaku u Evermusicu"
  caption="Zaslon Poveži se s uslugom u oblaku u Evermusicu"
  width="400"
>}}

3. Na zaslonu "SMB povezivanje" unesite URL poslužitelja s putanjom dijeljene mape. Možete koristiti naziv poslužitelja ili IP poslužitelja:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Unesite svoje korisničko ime i lozinku ili ostavite ova polja prazna ako ste odabrali "Svi: Samo čitanje" u prethodnom koraku.
5. Polje "WORKGROUP" je neobavezno i trebalo bi se koristiti ako imate Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Zaslon SMB konektora u Evermusicu"
  caption="Zaslon SMB konektora u Evermusicu"
  width="400"
>}}

6. Nakon što povežete računalo putem SMB protokola, pojavit će se u odjeljku "Usluge u oblaku" na zaslonu "Povezivanja".
7. Otvorite povezanu uslugu i idite do željene mape.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Otvorena SMB mapa u Evermusicu"
  caption="Otvorena SMB mapa u Evermusicu"
  width="400"
>}}

8. Možete koristiti ugrađeni upravitelj datoteka za uređivanje datoteka prema potrebi.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Upravitelj datoteka Evermusic"
  caption="Upravitelj datoteka Evermusic"
  width="400"
>}}

## Korak 3: Zaobilaženje problema s SMB2 mapama s posebnim znakovima

Ponekad možete naići na probleme s mapama koje sadrže posebne znakove pri korištenju SMB2 protokola. Evo nekih koraka za rješavanje ovog problema:

1. **Omogućite SMB 1:**  
   • Kao privremeno rješenje, pokušajte omogućiti SMB 1 na svom poslužitelju i u postavkama aplikacije. To može pomoći u zaobilaženju problema povezanih s posebnim znakovima u nazivima mapa.

2. **Koristite sistemski izbornik za otvaranje datoteka:**  
   • Idite na "Lokalne datoteke".  
   • Pomaknite se prema dolje do odjeljka "Datoteke na ovom uređaju".  
   • Dodirnite "Otvori datoteke..." ili "Otvori mape...".  
   • Pronađite svoj poslužitelj i odaberite datoteke ili mape koje trebate.  
   • Dodirnite "Otvori" za potvrdu odabira.

3. **Alternativni protokoli:**  
   • Ako problem potraje, razmislite o povezivanju s NAS-om koristeći WebDAV ili DLNA protokole ako vaš NAS podržava te opcije. Ti protokoli mogu bolje upravljati posebnim znakovima.

Slijedeći ove korake, možete ublažiti probleme s posebnim znakovima u nazivima mapa pri korištenju SMB2 protokola.

## Zaključak

S ovim koracima možete bez napora pristupiti svojoj velikoj kolekciji datoteka s MAC-a ili PC-a na svom iPhoneu ili iPadu koristeći naše aplikacije.

## Često postavljana pitanja

{{% details title="Mogu li pristupiti datotekama na PC-u s iPhonea bez iTunesa?" closed="true" %}}
Da. Evermusic se povezuje s vašim računalom putem SMB-a na lokalnoj Wi-Fi mreži. Nije potrebna sinkronizacija iTunesom ili Finderom. Omogućite dijeljenje datoteka na PC-u i povežite se izravno iz aplikacije.
{{% /details %}}

{{% details title="Radi li SMB pristup datotekama putem interneta?" closed="true" %}}
Ne. SMB je protokol lokalne mreže. Vaš iPhone i računalo moraju biti na istoj Wi-Fi mreži. Za udaljeni pristup, prenesite datoteke na uslugu u oblaku poput Google Drivea ili Dropboxa i povežite se s njom u Evermusicu.
{{% /details %}}

{{% details title="Kojim vrstama datoteka mogu pristupiti putem SMB-a?" closed="true" %}}
Evermusic podržava MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC i druge audio formate. Također možete pregledavati i upravljati ne-audio datotekama koristeći ugrađeni upravitelj datoteka.
{{% /details %}}

{{% details title="Mogu li prenijeti datoteke s NAS-a na iPhone koristeći SMB?" closed="true" %}}
Da. Većina NAS uređaja (Synology, QNAP, WD My Cloud i drugi) podržava SMB. Povežite se sa svojim NAS-om koristeći iste korake u ovom vodiču.
{{% /details %}}

{{% details title="Trebam li kopirati datoteke na iPhone da bih ih reproducirao?" closed="true" %}}
Ne. Evermusic streama datoteke izravno s vašeg računala ili NAS-a putem mreže. Datoteke se ne kopiraju na iPhone osim ako ne odaberete preuzimanje za offline reprodukciju.
{{% /details %}}

{{% details title="Je li SMB dijeljenje datoteka sigurno?" closed="true" %}}
SMB dijeljenje datoteka radi samo na vašoj lokalnoj mreži. Drugi uređaji na različitim mrežama ne mogu pristupiti vašim dijeljenim mapama. Za dodatnu sigurnost koristite korisničko ime i lozinku umjesto anonimnog (Svi) pristupa.
{{% /details %}}
