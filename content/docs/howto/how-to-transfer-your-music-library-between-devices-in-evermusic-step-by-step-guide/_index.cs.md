---
title: "Jak přenést hudební knihovnu mezi zařízeními v Evermusic: průvodce krok za krokem"
description: "Snadno přeneste svou hudební knihovnu Evermusic, seznamy skladeb, obaly alb a nastavení z jednoho iPhonu, iPadu nebo Macu na jiný pomocí Wi-Fi Drive a nástrojů pro zálohování."
date: 2024-12-29
tags: ["hudební knihovna", "přenos", "wifi", "záloha", "webdav", "obnovení"]
keywords: ["přenos hudební knihovny Evermusic", "zálohování a obnovení seznamů skladeb Evermusic", "Evermusic WiFi Drive", "synchronizace Evermusic mezi zařízeními", "přesun databáze Evermusic", "přenos souborů Evermusic", "obnovení nastavení přehrávače", "přenos hudby WebDAV iOS"]
readingTime: 3
---

{{< author-byline >}}


**Shrnutí:** Chcete-li přenést knihovnu Evermusic na nové zařízení, vytvořte zálohu na zdrojovém zařízení, spusťte Wi-Fi Drive, připojte druhé zařízení přes stejnou síť, stáhněte zálohu a hudební soubory a poté obnovte ze zálohy. Celý proces trvá přibližně 10 minut v závislosti na velikosti knihovny.

V tomto průvodci vás provedeme přenosem celé vaší hudební knihovny — včetně databáze, obalů alb a nastavení — z jednoho zařízení (iPhone nebo Mac) na jiné. Zatímco automatická synchronizace hudební knihovny a seznamů skladeb je funkcí plánovanou do budoucna, tento proces je v současnosti nutné provést ručně.

## Krok 1: Vytvoření zálohy na prvním zařízení

1. **Otevřete aplikaci na prvním zařízení** (to, které obsahuje vaši hudební knihovnu, seznamy skladeb a připojené cloudové služby).
2. **Přejděte do Nastavení** a vyberte možnost **Zálohování a obnovení**.

![Zálohování a obnovení](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. Na obrazovce **Zálohování a obnovení** vyberte položky, které chcete zahrnout do zálohovacího souboru:
   - **Databáze** (zahrnuje vaši hudební knihovnu a seznamy skladeb)
   - **Obaly alb**
   - **Nastavení**

Tyto možnosti jsou ve výchozím nastavení povoleny.

![Možnosti zálohování](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Klepněte na **Zálohovat data aplikace** pro zahájení procesu.

![Zálohovat data aplikace](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Po dokončení zálohy se zobrazí informační upozornění.

![Záloha dokončena](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Klepněte na **Zobrazit soubor** pro zobrazení zálohovacího souboru v adresáři **Dokumenty**. Zálohovací soubory jsou obvykle uloženy ve složce **Backup**.

![Zobrazit zálohovací soubor](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Krok 2: Spuštění serveru Wi-Fi Drive

1. Přejděte do sekce **Připojení** v aplikaci.
2. Posuňte se dolů na **Připojit přes Wi-Fi** a klepněte na něj.

![Připojit přes Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. Na další obrazovce klepněte na **Spustit Wi-Fi Drive**.

- Volitelně můžete nastavit přihlašovací jméno a heslo pro zabezpečení, ale pro domácí sítě to není nutné.

4. Po spuštění uvidíte dostupné adresy serveru. To lze použít pro desktopové prohlížeče nebo aplikace WebDAV, ale v tomto průvodci přejdeme přímo k dalším krokům.

![Wi-Fi Drive spuštěn](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Krok 3: Připojení druhého zařízení k prvnímu

1. Otevřete aplikaci na druhém zařízení (kam chcete přenést knihovnu).
2. Ujistěte se, že obě zařízení jsou připojena ke stejné Wi-Fi síti.
3. Na druhém zařízení otevřete záložku **Připojení** a vyberte **Dostupná zařízení**.

![Dostupná zařízení](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Měli byste vidět WebDAV připojení s názvem **Evermusic** (server, který jsme spustili na prvním zařízení). Klepněte na něj pro připojení.

5. Po připojení uvidíte všechny složky z prvního zařízení.

![Připojeno k prvnímu zařízení](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Krok 4: Příprava na přenos souborů

1. Na druhém zařízení přejděte do **Nastavení > Správce souborů** a povolte **Ukládat stažené soubory do - Ptát se pokaždé**.

- To zajistí, že můžete vybrat cílovou složku pro každé stažení.

2. Vraťte se na záložku **Připojení** a přejděte na připojený WebDAV server.

![Příprava na přenos souborů](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Krok 5: Přenos zálohy a hudebních souborů

1. Otevřete složku **Backup** na připojeném WebDAV serveru.

![Složka zálohy](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Klepněte na tlačítko **Další akce** (tři tečky) u zálohovacího souboru a vyberte **Stáhnout**.

3. Vytvořte složku **Backup** na druhém zařízení pro uložení stažených souborů. Potvrďte svůj výběr klepnutím na **Hotovo**.

![Stáhnout zálohu](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Přeneste další hudební soubory:
   - Zkontrolujte složku **Stáhnout** nebo jiné relevantní složky na WebDAV serveru.

![Přenos hudebních souborů](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Použijte možnost **Vybrat** pro výběr souborů, poté klepněte na **Další akce > Stáhnout**. Uložte je do odpovídající složky na druhém zařízení pro zachování stejné adresářové struktury.

Cílem je přenést všechny soubory z vašeho prvního zařízení na vaše aktuální zařízení a zajistit, aby struktura složek zůstala identická. Tímto způsobem zůstanou odkazy ve vaší hudební knihovně a seznamech skladeb neporušené. Mějte na paměti, že lokální soubory uložené mimo adresář Dokumenty aplikace na vašem prvním zařízení musí být přeneseny zvlášť. Protože aplikace nemůže přistupovat k těmto souborům v režimu Wi-Fi Drive, budete muset použít systémovou aplikaci Soubory pro jejich přenos.

![Přenos dokončen](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Krok 6: Sledování průběhu přenosu

1. Na druhém zařízení přejděte do sekce **Lokální soubory** (nebo záložka **Stáhnout** na iPadu/Macu).

2. Klepněte na tlačítko **Aktivita přenosu** v levém horním rohu pro sledování fronty přenosů.

![Sledování přenosu](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Krok 7: Obnovení dat ze zálohy

1. Jakmile je zálohovací soubor a všechny potřebné audio soubory staženy na druhé zařízení, otevřete složku **Backup**.

2. Klepněte na zálohovací soubor a zobrazí se potvrzovací zpráva.

![Obnovit zálohu](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Poznámka:** Obnovení nahradí všechna aktuální data hudební knihovny, seznamy skladeb, nastavení a obaly alb daty ze zálohy.

3. Klepněte na **Obnovit** pro zahájení procesu.

![Proces obnovení](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Po dokončení obnovení se zobrazí upozornění potvrzující úspěch.

![Obnovení dokončeno](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Zkontrolujte sekce **Seznamy skladeb** nebo **Hudební knihovna** pro ověření obnovení.

![Ověření obnovení](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Krok 8: Přeindexování hudební knihovny

1. Pro nejlepší výsledky přeindexujte svou knihovnu, abyste zajistili úspěšné rozpoznání všech souborů.

2. Přejděte do **Nastavení > Hudební knihovna > Synchronizace offline hudby** a vyberte **Spustit skenování lokálních složek**.

Dodržením těchto kroků úspěšně přenesete svou hudební knihovnu, seznamy skladeb a nastavení na jiné zařízení. Pokud narazíte na jakékoli problémy, neváhejte se obrátit na podporu.

## Často kladené otázky

{{% details title="Mohu přenést svou knihovnu Evermusic bez Wi-Fi?" closed="true" %}}
Wi-Fi Drive vyžaduje, aby obě zařízení byla na stejné Wi-Fi síti. V současnosti neexistuje možnost přenosu přes Bluetooth nebo mobilní data. Alternativně můžete použít AirDrop nebo aplikaci Soubory pro ruční přesun zálohovacího souboru a složek s hudbou mezi zařízeními.
{{% /details %}}

{{% details title="Přenesou se připojení ke cloudovým službám se zálohou?" closed="true" %}}
Záloha zahrnuje vaši databázi, seznamy skladeb, obaly alb a nastavení. Přihlašovací údaje ke cloudovým službám nejsou z bezpečnostních důvodů zahrnuty. Po obnovení budete muset znovu připojit své cloudové účty na novém zařízení.
{{% /details %}}

{{% details title="Co se stane s mou stávající knihovnou na druhém zařízení?" closed="true" %}}
Obnovení zálohy nahradí všechna stávající data hudební knihovny, seznamy skladeb, nastavení a obaly alb na druhém zařízení. Pokud chcete zachovat jeho data, vytvořte nejprve samostatnou zálohu druhého zařízení.
{{% /details %}}

{{% details title="Funguje tento proces mezi iPhonem a Macem?" closed="true" %}}
Ano. Evermusic podporuje přenos Wi-Fi Drive mezi libovolnou kombinací iPhonu, iPadu a Macu. Obě zařízení stačí mít na stejné Wi-Fi síti.
{{% /details %}}

{{% details title="Jak dlouho přenos trvá?" closed="true" %}}
Doba přenosu závisí na velikosti vaší hudební knihovny a rychlosti Wi-Fi. Typická knihovna o několika gigabajtech se přenese za 5-15 minut přes standardní domácí síť.
{{% /details %}}
