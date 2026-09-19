---
title: "Anslut dina enheter"
date: 2026-08-20
description: "Steg-för-steg-instruktioner för att ansluta till din trådlösa Everdisk-disk: titta på en smart-TV via DLNA, öppna dina filer i valfri webbläsare, montera din enhet som en nätverksdisk i Finder, Windows eller Linux via WebDAV eller SMB (med valfri SMB3/AES-kryptering), anslut filappar via FTP och överför via en USB-kabel till en Mac utan Wi-Fi."
keywords: ["ansluta till Everdisk", "streama till TV DLNA", "öppna filer i webbläsare", "montera nätverksdisk Finder", "WebDAV Windows Linux", "FTP filapp", "USB kabelöverföring Mac", "ansluta iPhone till dator", "nätverksdisk iPhone"]
tags: ["everdisk", "guide", "connect"]
readingTime: 11
---


När du har tryckt på **Start** på [Delning](/docs/guide/everdisk/everdisk-guide-sharing)-skärmen kan andra enheter ansluta till dina filer på fem olika sätt. Välj den metod som passar den enhet du vill använda. I samtliga fall visas den exakta **adressen** du behöver i sektionen **Så ansluter du** på delningsskärmen.

> Båda enheterna måste vara på **samma Wi-Fi-nätverk** - eller, för en Mac, anslutna med en **USB-kabel** (se sista avsnittet).

## Titta på en TV (DLNA)

Använd detta för att visa foton, videor och musik på en smart-TV eller mediaspelare.

1. I **Inställningar → Delning → Anslutningar**, se till att **TV och mediacenter** är på (det är på som standard).
2. På delningsskärmen, tryck på **Start**.
3. På din TV, öppna dess inbyggda mediaspelare eller mediaserverapp (den kan heta Media Player, SmartShare, AllShare eller liknande).
4. Din enhet visas i listan över mediaservrar med sitt namn (till exempel "Speedy-Hare"). Välj den.
5. Bläddra bland dina delade foton, videor och din musik och börja spela upp. Förhandsvisningsminiatyrer visas automatiskt.

Att tänka på:

- DLNA kan inte lösenordsskyddas, så den här anslutningen är öppen för alla på samma Wi-Fi medan den är påslagen.
- Om en video inte spelas upp på en äldre TV, sänk videokvaliteten i **Inställningar → Delning → Videor** så att Everdisk konverterar den till ett mer kompatibelt format.

## Öppna i en webbläsare (HTTP)

Använd detta för att ge filer till vem som helst med en webbläsare - ingen app att installera.

1. I **Inställningar → Delning → Anslutningar**, se till att **Webbläsare** är på.
2. Tryck på **Start**.
3. På delningsskärmen, kopiera **Webbläsare**-adressen (eller visa dess QR-kod).
4. På den andra telefonen, surfplattan eller datorn, öppna valfri webbläsare (Safari, Chrome, Edge, Firefox) och skriv in den adressen.
5. Sidan öppnas med dina delade filer.

I webbläsaren kan den andra personen:

- Växla mellan **list**- och **rutnätsvy** och sortera efter namn, datum eller storlek.
- Se riktiga **miniatyrer** för foton, videor, PDF-filer och musikomslag.
- Öppna ett foto till ett **galleri** i helskärm med svep, nyp för att zooma och ett bildspel.
- Spela musik i en inbyggd **spelare** med kö, blandning och upprepning.
- **Ladda ner** vilken fil som helst, eller ladda ner en hel mapp (eller flera valda objekt) som en enda **Archive.zip**.
- **Ladda upp** filer tillbaka till din enhet - endast om du har slagit på **Filredigering** (se [Åtkomst och integritet](/docs/guide/everdisk/everdisk-guide-access)).

## Använd den som en nätverksdisk (WebDAV)

Använd detta för att få din enhet att visas som en vanlig disk på en Mac, Windows-PC eller Linux-dator, så att du kan dra filer åt båda hållen.

**På en Mac (Finder)**

1. I **Inställningar → Delning → Anslutningar**, se till att **Dator** är på.
2. Tryck på **Start** och notera adressen för **Dator (WebDAV)**.
3. I Finder, välj **Gå → Anslut till server** (eller tryck på **⌘K**).
4. Skriv in WebDAV-adressen exakt som den visas och klicka på **Anslut**.
5. Ange inloggning och lösenord om du har angett något, annars anslut som gäst.
6. Din enhet öppnas som vilken annan nätverksdisk som helst. Dra filer in eller ut.

**På Windows**

1. Öppna **Utforskaren**, högerklicka på **Den här datorn** och välj **Lägg till en nätverksplats** (eller mappa en nätverksenhet).
2. Ange WebDAV-adressen som visas i Everdisk.
3. Ange inloggning och lösenord om du har angett något.

**På Linux**

1. Öppna din filhanterare och välj **Anslut till server** (eller använd `davs://` / `dav://`).
2. Ange WebDAV-adressen som visas i Everdisk.

Om anslutningen är skrivskyddad eller dubbelriktad beror på inställningen **Filredigering**. Med den på kan du kopiera filer till din enhet och byta namn på eller ta bort dem; med den av är disken skrivskyddad.

## Anslut via SMB (krypterad nätverksdisk)

SMB är en nätverksdisk för Mac, Windows och Linux, byggd på fildelningen som redan finns i de systemen, så din enhet dyker upp som en vanlig nätverksdisk - och det är den enda anslutningen du kan kryptera.

1. I **Inställningar → Delning → Anslutningar**, se till att **Dator (avancerat)** (SMB-anslutningen) är på.
2. Tryck på **Start** och notera **SMB**-adressen, som ser ut som `smb://192.168.1.20:4455/Share`.
3. Anslut från din dator:
   - **Mac:** din enhet dyker upp av sig själv i **Finders sidofält** under **Platser** (Nätverk) - klicka bara på den och logga in. För att ansluta för hand istället väljer du **Gå → Anslut till server** (**⌘K**) och anger adressen.
   - **Windows:** öppna **Utforskaren**, högerklicka på **Den här datorn** och välj **Anslut en nätverksdisk**, ange sedan `\\<address>\Share` med värddatorn och resursnamnet från delningsskärmen (eller skriv `smb://`-adressen i adressfältet).
   - **Linux:** i din filhanterare väljer du **Anslut till server** och anger adressen.
4. Ange inloggning och lösenord om du har angett något, annars anslut som gäst.
5. Resursen heter **Share**. Med **Filredigering** på kan du kopiera filer i båda riktningarna; med den av är den skrivskyddad.

**Slå på kryptering (rekommenderas på Wi-Fi du inte litar på)**

SMB är den enda Everdisk-anslutningen som kan krypteras. För att skydda varje överföring med **SMB3-kryptering (AES)**:

1. I **Inställningar → Delning → Åtkomst**, ange en **Inloggning** och ett **Lösenord** - krypterade anslutningar kan inte vara anonyma.
2. I **Inställningar → Delning**, slå på **Kräv SMB-kryptering**.
3. **Stoppa och starta** delningen igen så att ändringen träder i kraft.

Din klient måste stödja SMB3 - Finder på en modern Mac, eller **Windows 10 och senare**. SMB-kryptering är en Premium-funktion.

## Anslut en filapp (FTP)

Använd detta för filhanterings- och överföringsappar som talar FTP (till exempel FileZilla eller Cyberduck på en dator).

1. I **Inställningar → Delning → Anslutningar**, se till att **Andra appar och enheter** är på.
2. Tryck på **Start** och notera **FTP**-adressen.
3. I din FTP-app, lägg till en ny anslutning med den adressen.
4. Ange inloggning och lösenord om du har angett något, eller lämna dem tomma för anonym åtkomst.

## Överför via en USB-kabel (Mac, ingen Wi-Fi behövs)

Använd detta när det inte finns någon Wi-Fi, eller när du vill ha den snabbaste och mest privata överföringen. Det fungerar endast med en **Mac**.

1. Anslut din iPhone eller iPad till Mac-datorn med den vanliga laddkabeln.
2. Om du blir tillfrågad på enheten, tryck på **Lita på den här datorn**.
3. I Everdisk, tryck på **Start**. Meddelandet **Snabb anslutning tillgänglig** visas och delningsskärmen visar en extra adress med märkningen **Kabelanslutning** som slutar på `.local`.
4. På Mac-datorn, öppna Finder → **Gå → Anslut till server** (**⌘K**) och ange den `.local`-adressen (den fungerar för både Webbläsare- och Dator-anslutningarna).
5. Din enhet öppnas via kabeln - snabbare än Wi-Fi, och datan når aldrig routern eller internet.

Att tänka på:

- Använd **`.local`-namnet**, inte en IP-adress (IP-adresser fungerar bara över Wi-Fi), och aldrig `localhost`.
- Kabelvägen är **endast för Mac**. Windows-PC och Android-enheter måste använda Wi-Fi.
- Du kan även dra filer in i Everdisk-mappen med hjälp av Finder på en Mac, eller appen Apple-enheter (eller iTunes) på Windows, via standardfildelning i iOS.

## Nästa steg

- [Åtkomst och integritet](/docs/guide/everdisk/everdisk-guide-access) - lägg till ett lösenord, tillåt uppladdningar, blockera en enhet.
- [Foton, musik och video](/docs/guide/everdisk/everdisk-guide-media) - dela hela ditt bibliotek och ställ in kvaliteten.
- [Anslut till servrar](/docs/guide/everdisk/everdisk-guide-devices) - nå andra enheter från Everdisk.
