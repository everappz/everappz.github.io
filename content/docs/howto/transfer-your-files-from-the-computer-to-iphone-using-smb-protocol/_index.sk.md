---
title: "Prenos súborov z počítača do iPhone pomocou protokolu SMB"
description: "Naučte sa prenášať a pristupovať k veľkým súborom z vášho Macu alebo Windows PC do iPhonu alebo iPadu pomocou Evermusic a protokolu SMB. Podrobný sprievodca pre bezproblémové streamovanie a správu súborov."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["prenos súborov do iPhone SMB", "streamovanie hudby z PC na iPhone", "pripojenie Macu k iPhone SMB", "nastavenie Evermusic SMB", "prístup k súborom počítača iPhone", "zdieľanie hudby Windows iOS", "prenos súborov SMB Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Zhrnutie:** Použite Evermusic na svojom iPhone alebo iPade na prístup k súborom uloženým na Macu alebo Windows PC cez lokálnu sieť pomocou SMB. Bez káblov, bez iTunes, bez nahrávania do cloudu. Povoľte zdieľanie súborov na počítači, pripojte sa v aplikácii a prehliadajte alebo prehrávajte súbory bezdrôtovo.

Máte rozsiahlu zbierku veľkých súborov na vašom MAC alebo PC a chcete k nim jednoducho pristupovať z iPhonu alebo iPadu? Naše aplikácie poskytujú jednoduché riešenie.

Postupujte podľa týchto krokov na povolenie bezproblémového prístupu medzi počítačom a zariadením iOS pomocou protokolu SMB:

## Krok 1: Povolenie protokolu SMB na vašom počítači

**Pre MAC:**

1. Otvorte "Systémové nastavenia" na vašom MAC.
2. Kliknite na "Zdieľanie".
3. Povoľte službu "Zdieľanie súborov".
4. Pridajte svoju hudobnú zložku do sekcie "Zdieľané priečinky". Pridajte používateľa a vyberte úroveň oprávnení (Čítanie a zápis alebo Len čítanie). Môžete zvoliť "Všetci: Len čítanie" pre pridanú hudobnú zložku.

   ![Obrazovka nastavení Macu](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Zapamätajte si URL počítača (smb://192.168.xx.xx), pretože ho budete potrebovať v ďalších krokoch.
6. Kliknite na "Možnosti" a aktivujte "Zdieľať súbory a priečinky pomocou SMB".

   ![Obrazovka zdieľania súborov Macu](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Povoľte "Zdieľanie súborov Windows" pre dostupné účty.

   ![Obrazovka zdieľania SMB Macu](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Pre Windows PC:**

1. Kliknite pravým tlačidlom myši na hudobnú zložku.
2. Vyberte "Vlastnosti".
3. Prejdite na kartu "Zdieľanie".
4. Kliknite na "Zdieľať..."
5. Vyberte osoby, s ktorými chcete zdieľať priečinok, a určte úroveň oprávnení. Môžete vybrať "Všetci: Čítanie" pre vybranú hudobnú zložku.

   ![Obrazovka zdieľania SMB Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Kliknite na "Hotovo".
7. Kliknite na "Hotovo" v okne "Zdieľanie súborov" a zapamätajte si cestu k priečinku.

   ![Zdieľaný priečinok SMB Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Krok 2: Pripojenie zariadenia iOS

1. Otvorte aplikáciu na iPhone alebo iPade.
2. Prejdite na kartu "Pripojenia".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Obrazovka Pripojenia v Evermusic"
  caption="Obrazovka Pripojenia v Evermusic"
  width="400"
>}}

*Ak sa váš počítač zobrazí v sekcii "Dostupné zariadenia":*

Ak je váš počítač viditeľný v sekcii "Dostupné zariadenia" a v predchádzajúcom kroku ste vybrali "Všetci: Len čítanie", jednoducho klepnite na svoj počítač a pripojí sa automaticky.

*Ak sa váš počítač nezobrazí automaticky:*

1. Klepnite na "Pripojiť cloudovú službu".
2. Vyberte "SMB" na obrazovke "Pripojiť cloudovú službu".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Obrazovka Pripojiť cloudovú službu v Evermusic"
  caption="Obrazovka Pripojiť cloudovú službu v Evermusic"
  width="400"
>}}

3. Na obrazovke "Pripojenie SMB" zadajte URL servera s cestou k zdieľanému priečinku. Môžete použiť názov servera alebo IP adresu servera:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Zadajte svoje prihlasovacie meno a heslo alebo ponechajte tieto polia prázdne, ak ste v predchádzajúcom kroku vybrali "Všetci: Len čítanie".
5. Pole "WORKGROUP" je voliteľné a malo by sa použiť, ak máte Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Obrazovka SMB konektora v Evermusic"
  caption="Obrazovka SMB konektora v Evermusic"
  width="400"
>}}

6. Po pripojení počítača pomocou protokolu SMB sa zobrazí v sekcii "Cloudové služby" na obrazovke "Pripojenia".
7. Otvorte pripojenú službu a prejdite do požadovaného priečinku.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Otvorený priečinok SMB v Evermusic"
  caption="Otvorený priečinok SMB v Evermusic"
  width="400"
>}}

8. Môžete využiť vstavaný správca súborov na úpravu súborov podľa potreby.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Správca súborov Evermusic"
  caption="Správca súborov Evermusic"
  width="400"
>}}

## Krok 3: Riešenie problémov s priečinkami SMB2 so špeciálnymi znakmi

Niekedy môžete naraziť na problémy s priečinkami obsahujúcimi špeciálne znaky pri používaní protokolu SMB2. Tu sú kroky na vyriešenie tohto problému:

1. **Povolenie SMB 1:**  
   • Ako dočasné riešenie skúste povoliť SMB 1 na vašom serveri a v nastaveniach aplikácie. To môže pomôcť obísť problémy súvisiace so špeciálnymi znakmi v názvoch priečinkov.

2. **Použitie systémového menu na otváranie súborov:**  
   • Prejdite na "Lokálne súbory".  
   • Prejdite nadol do sekcie "Súbory na tomto zariadení".  
   • Klepnite na "Otvoriť súbory..." alebo "Otvoriť priečinky...".  
   • Nájdite svoj server a vyberte súbory alebo priečinky, ktoré potrebujete.  
   • Klepnite na "Otvoriť" na potvrdenie výberu.

3. **Alternatívne protokoly:**  
   • Ak problém pretrváva, zvážte pripojenie k NAS pomocou protokolov WebDAV alebo DLNA, ak váš NAS podporuje tieto možnosti. Tieto protokoly môžu lepšie spracovávať špeciálne znaky.

Dodržiavaním týchto krokov môžete zmierniť problémy so špeciálnymi znakmi v názvoch priečinkov pri používaní protokolu SMB2.

## Záver

S týmito krokmi môžete jednoducho pristupovať k rozsiahlej zbierke súborov z vášho MAC alebo PC na iPhone alebo iPade pomocou našich aplikácií.

## Často kladené otázky

{{% details title="Môžem pristupovať k súborom na PC z iPhonu bez iTunes?" closed="true" %}}
Áno. Evermusic sa pripojí k vášmu počítaču cez SMB na lokálnej Wi-Fi sieti. Synchronizácia cez iTunes alebo Finder nie je potrebná. Povoľte zdieľanie súborov na PC a pripojte sa priamo z aplikácie.
{{% /details %}}

{{% details title="Funguje prístup k súborom cez SMB cez internet?" closed="true" %}}
Nie. SMB je protokol lokálnej siete. Váš iPhone a počítač musia byť na rovnakej Wi-Fi sieti. Pre vzdialený prístup nahrajte súbory do cloudovej služby ako Google Drive alebo Dropbox a pripojte sa k nej v Evermusic.
{{% /details %}}

{{% details title="Aké typy súborov môžem pristupovať cez SMB?" closed="true" %}}
Evermusic podporuje MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC a ďalšie audio formáty. Môžete tiež prehliadať a spravovať neaudio súbory pomocou vstavaného správcu súborov.
{{% /details %}}

{{% details title="Môžem prenášať súbory z NAS do iPhonu pomocou SMB?" closed="true" %}}
Áno. Väčšina NAS zariadení (Synology, QNAP, WD My Cloud a ďalšie) podporuje SMB. Pripojte sa k NAS pomocou rovnakých krokov v tomto sprievodcovi.
{{% /details %}}

{{% details title="Musím kopírovať súbory do iPhonu, aby som ich mohol prehrávať?" closed="true" %}}
Nie. Evermusic streamuje súbory priamo z vášho počítača alebo NAS cez sieť. Súbory sa nekopírujú do iPhonu, pokiaľ si ich nezvolíte stiahnuť pre offline prehrávanie.
{{% /details %}}

{{% details title="Je zdieľanie súborov cez SMB bezpečné?" closed="true" %}}
Zdieľanie súborov cez SMB funguje iba na vašej lokálnej sieti. Ostatné zariadenia na iných sieťach nemôžu pristupovať k vašim zdieľaným priečinkom. Pre dodatočnú bezpečnosť použite prihlasovacie meno a heslo namiesto anonymného (Všetci) prístupu.
{{% /details %}}
