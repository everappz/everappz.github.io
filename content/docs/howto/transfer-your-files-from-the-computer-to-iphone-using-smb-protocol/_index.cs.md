---
title: "Přenos souborů z počítače do iPhone pomocí protokolu SMB"
description: "Naučte se přenášet a přistupovat k velkým souborům z vašeho Macu nebo Windows PC do iPhonu nebo iPadu pomocí Evermusic a protokolu SMB. Podrobný průvodce pro bezproblémový streaming a správu souborů."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["přenos souborů do iPhone SMB", "streamování hudby z PC na iPhone", "připojení Macu k iPhone SMB", "nastavení Evermusic SMB", "přístup k souborům počítače iPhone", "sdílení hudby z Windows na iOS", "přenos souborů SMB Evermusic"]
---

{{< author-byline >}}


**Shrnutí:** Použijte Evermusic na svém iPhonu nebo iPadu pro přístup k souborům uloženým na Macu nebo Windows PC přes místní síť pomocí SMB. Bez kabelů, bez iTunes, bez nahrávání do cloudu. Povolte sdílení souborů na počítači, připojte se v aplikaci a procházejte nebo přehrávejte soubory bezdrátově.

Máte rozsáhlou sbírku velkých souborů na vašem MAC nebo PC a chcete k nim snadno přistupovat z iPhonu nebo iPadu? Naše aplikace poskytují jednoduché řešení.

Postupujte podle těchto kroků pro povolení bezproblémového přístupu mezi počítačem a iOS zařízením pomocí protokolu SMB:

## Krok 1: Povolení protokolu SMB na vašem počítači

**Pro MAC:**

1. Otevřete "Předvolby systému" na vašem MAC.
2. Klikněte na "Sdílení".
3. Povolte službu "Sdílení souborů".
4. Přidejte složku s hudbou do sekce "Sdílené složky". Přidejte uživatele a zvolte úroveň oprávnění (Čtení a zápis nebo Pouze čtení). Můžete zvolit "Všichni: Pouze čtení" pro přidanou složku s hudbou.

   ![Obrazovka nastavení Macu](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Zapamatujte si URL počítače (smb://192.168.xx.xx), protože ji budete potřebovat v dalších krocích.
6. Klikněte na "Volby" a aktivujte "Sdílení souborů a složek pomocí SMB".

   ![Obrazovka sdílení souborů Macu](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Povolte "Sdílení souborů Windows" pro dostupné účty.

   ![Obrazovka sdílení SMB na Macu](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Pro Windows PC:**

1. Klikněte pravým tlačítkem na složku s hudbou.
2. Vyberte "Vlastnosti".
3. Přejděte na kartu "Sdílení".
4. Klikněte na "Sdílet..."
5. Zvolte osoby, se kterými chcete složku sdílet, a určete úroveň oprávnění. Můžete vybrat "Všichni: Čtení" pro zvolenou složku s hudbou.

   ![Obrazovka sdílení SMB na Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Klikněte na "Hotovo".
7. Klikněte na "Hotovo" v okně "Sdílení souborů" a zapamatujte si cestu ke složce.

   ![Sdílená složka SMB na Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Krok 2: Připojení iOS zařízení

1. Otevřete aplikaci na svém iPhonu nebo iPadu.
2. Přejděte na kartu "Připojení".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Obrazovka Připojení v Evermusic"
  caption="Obrazovka Připojení v Evermusic"
  width="400"
>}}

*Pokud se váš počítač zobrazí v sekci "Dostupná zařízení":*

Pokud je váš počítač viditelný v sekci "Dostupná zařízení" a v předchozím kroku jste vybrali "Všichni: Pouze čtení", jednoduše klepněte na svůj počítač a připojí se automaticky.

*Pokud se váš počítač nezobrazí automaticky:*

1. Klepněte na "Připojit cloudovou službu".
2. Vyberte "SMB" na obrazovce "Připojit cloudovou službu".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Obrazovka Připojit cloudovou službu v Evermusic"
  caption="Obrazovka Připojit cloudovou službu v Evermusic"
  width="400"
>}}

3. Na obrazovce "Připojení SMB" zadejte URL serveru s cestou ke sdílené složce. Můžete použít název serveru nebo IP adresu serveru:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Zadejte své přihlašovací jméno a heslo nebo tato pole ponechte prázdná, pokud jste v předchozím kroku vybrali "Všichni: Pouze čtení".
5. Pole "WORKGROUP" je volitelné a mělo by se použít, pokud máte Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Obrazovka SMB konektoru v Evermusic"
  caption="Obrazovka SMB konektoru v Evermusic"
  width="400"
>}}

6. Po připojení počítače pomocí protokolu SMB se zobrazí v sekci "Cloudové služby" na obrazovce "Připojení".
7. Otevřete připojenou službu a přejděte do požadované složky.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Otevřená složka SMB v Evermusic"
  caption="Otevřená složka SMB v Evermusic"
  width="400"
>}}

8. Můžete využít vestavěný správce souborů k úpravě souborů podle potřeby.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Správce souborů Evermusic"
  caption="Správce souborů Evermusic"
  width="400"
>}}

## Krok 3: Řešení problémů se složkami SMB2 se speciálními znaky

Někdy můžete narazit na problémy se složkami obsahujícími speciální znaky při použití protokolu SMB2. Zde jsou kroky k vyřešení tohoto problému:

1. **Povolení SMB 1:**  
   • Jako dočasné řešení zkuste povolit SMB 1 na vašem serveru a v nastavení aplikace. To může pomoci obejít problémy související se speciálními znaky v názvech složek.

2. **Použití systémového menu pro otevření souborů:**  
   • Přejděte na "Místní soubory".  
   • Přejděte dolů do sekce "Soubory na tomto zařízení".  
   • Klepněte na "Otevřít soubory..." nebo "Otevřít složky...".  
   • Najděte svůj server a vyberte soubory nebo složky, které potřebujete.  
   • Klepněte na "Otevřít" pro potvrzení výběru.

3. **Alternativní protokoly:**  
   • Pokud problém přetrvává, zvažte připojení k NAS pomocí protokolů WebDAV nebo DLNA, pokud váš NAS tyto možnosti podporuje. Tyto protokoly mohou lépe zpracovávat speciální znaky.

Dodržováním těchto kroků můžete zmírnit problémy se speciálními znaky v názvech složek při použití protokolu SMB2.

## Závěr

S těmito kroky můžete snadno přistupovat k rozsáhlé sbírce souborů z vašeho MAC nebo PC na iPhonu nebo iPadu pomocí našich aplikací.

## Často kladené otázky

{{% details title="Mohu přistupovat k souborům na PC z iPhonu bez iTunes?" closed="true" %}}
Ano. Evermusic se připojí k vašemu počítači přes SMB na místní Wi-Fi síti. Není potřeba synchronizace přes iTunes nebo Finder. Povolte sdílení souborů na PC a připojte se přímo z aplikace.
{{% /details %}}

{{% details title="Funguje přístup k souborům přes SMB přes internet?" closed="true" %}}
Ne. SMB je protokol místní sítě. Váš iPhone a počítač musí být na stejné Wi-Fi síti. Pro vzdálený přístup nahrajte soubory do cloudové služby jako Google Drive nebo Dropbox a připojte se k ní v Evermusic.
{{% /details %}}

{{% details title="Jaké typy souborů mohu přistupovat přes SMB?" closed="true" %}}
Evermusic podporuje MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC a další audio formáty. Můžete také procházet a spravovat neaudio soubory pomocí vestavěného správce souborů.
{{% /details %}}

{{% details title="Mohu přenášet soubory z NAS do iPhonu pomocí SMB?" closed="true" %}}
Ano. Většina NAS zařízení (Synology, QNAP, WD My Cloud a další) podporuje SMB. Připojte se k NAS pomocí stejných kroků v tomto průvodci.
{{% /details %}}

{{% details title="Musím kopírovat soubory do iPhonu, abych je mohl přehrávat?" closed="true" %}}
Ne. Evermusic streamuje soubory přímo z vašeho počítače nebo NAS přes síť. Soubory nejsou kopírovány do iPhonu, pokud si je nezvolíte stáhnout pro offline přehrávání.
{{% /details %}}

{{% details title="Je sdílení souborů přes SMB bezpečné?" closed="true" %}}
Sdílení souborů přes SMB funguje pouze na vaší místní síti. Ostatní zařízení na jiných sítích nemohou přistupovat k vašim sdíleným složkám. Pro dodatečnou bezpečnost použijte přihlašovací jméno a heslo místo anonymního přístupu (Všichni).
{{% /details %}}
