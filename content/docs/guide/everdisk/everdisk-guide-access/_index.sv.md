---
title: "Åtkomst och integritet"
date: 2026-08-20
description: "Håll din Everdisk-delning säker: skydda åtkomsten med en inloggning och ett lösenord, styr om anslutna enheter kan ladda upp, byta namn och ta bort med Filredigering, blockera okända enheter, välj papperskorg kontra permanent borttagning och förstå varför allt stannar på ditt lokala nätverk."
keywords: ["Everdisk lösenordsskydd", "filredigering reglage", "blockera enhet", "blockerade enheter", "ta bort filer permanent", "endast lokalt nätverk", "privat fildelning", "DLNA inget lösenord", "nätverkssäkerhet"]
tags: ["everdisk", "guide", "access", "privacy", "security"]
readingTime: 8
---


Everdisk håller dina filer på ditt eget nätverk och ger dig enkla kontroller över vem som kan nå dem och vad de kan göra. Du hittar dessa kontroller i **Inställningar → Delning → Åtkomst**, plus några relaterade inställningar i Filhanteraren.

## Skydda åtkomsten med en inloggning och ett lösenord

Som standard kan vem som helst på samma nätverk som har din adress öppna dina delade filer. För att kräva en inloggning:

1. Gå till **Inställningar → Delning → Åtkomst**.
2. Ange en **Inloggning** och ett **Lösenord**.
3. Nu ber anslutningarna **Webbläsare (HTTP)**, **Dator (WebDAV)** och **Andra appar och enheter (FTP)** alla om dessa uppgifter innan de visar dina filer.

Lämna båda fälten tomma för öppen åtkomst. Ditt lösenord lagras säkert i enhetens Keychain.

> **DLNA är alltid öppet.** Anslutningen TV och mediacenter (DLNA) kan inte lösenordsskyddas, så när den väl är på kan alla enheter på samma Wi-Fi bläddra bland dina delade media. Stäng av den om du bara vill ha skyddade anslutningar, och dela endast på nätverk du litar på.

## Tillåt eller blockera redigering (Filredigering)

Reglaget **Filredigering** styr om anslutna enheter bara kan titta på dina filer, eller även ändra dem.

- **På** (standard): anslutna enheter kan **ladda upp, byta namn och ta bort** dina delade filer - så din enhet fungerar som en riktig dubbelriktad nätverksdisk.
- **Av**: dina delade filer är **skrivskyddade**. Andra kan visa och ladda ner, men kan inte lägga till eller ändra något.

Att slå på det visar en kort varning eftersom det låter andra personer ändra dina filer. Det har ett **Viktigt**-märke medan det är på.

## Blockera en enhet

Om du ser en enhet du inte känner igen:

1. På delningsskärmen, hitta den under **Vem som är ansluten**.
2. Tryck på dess knapp Fler åtgärder och välj **Blockera den här enheten**.

Blockerade enheter listas i **Inställningar → Delning → Åtkomst → Blockerade enheter**, där du kan **avblockera** en eller **Avblockera alla**. Blockering följer enheten även om dess nätverksadress ändras (för anslutningarna Webbläsare, Dator och TV).

## Papperskorg kontra permanent borttagning

När en fil tas bort - av dig i filhanteraren eller av en ansluten enhet - hamnar den normalt i en återställningsbar **papperskorg** så att du kan få tillbaka den.

Om du föredrar att filer tas bort omedelbart utan möjlighet till återställning, slå på **Ta bort filer permanent** i **Inställningar → Filhanterare → Ta bort filer**. Detta är av som standard. **Det påverkar filhanteraren på enheten** och **borttagningar som görs över nätverket**; det ändrar inte hur systemets fotobibliotek eller musikbibliotek hanterar borttagning.

## Allt stannar lokalt

Everdisk delar endast över ditt **lokala nätverk** - inget laddas upp till internet och det finns inget molnkonto emellan. Några saker värda att veta:

- Everdisk behöver iOS-behörigheten **Lokalt nätverk** så att närliggande enheter kan hitta det. Om den behörigheten är av förklarar ett meddelande hur du slår på den igen i iOS Inställningar-appen.
- För bästa integritet, dela endast medan du är på ett **hem- eller privat Wi-Fi**-nätverk du litar på, och var försiktig på offentligt Wi-Fi. En inloggning och ett lösenord hjälper, men det är ingen ersättning för ett betrott nätverk.
- Det **absolut mest privata alternativet är en USB-kabel till en Mac** - datan går direkt över kabeln och når aldrig routern eller internet. Se [Anslut dina enheter](/docs/guide/everdisk/everdisk-guide-connect).

## Nästa steg

- [Delning](/docs/guide/everdisk/everdisk-guide-sharing) - välj vad du vill dela och starta delning.
- [Inställningar](/docs/guide/everdisk/everdisk-guide-settings) - alla inställningar för Åtkomst och Filhanterare på ett ställe.
