---
title: "Delning"
date: 2026-08-20
description: "Lär dig hur delning fungerar i Everdisk: tryck på Start för att förvandla din iPhone eller iPad till en trådlös disk, välj vad du vill dela (filer, mappar, foton och musik), kör de fyra servrarna (DLNA, HTTP, WebDAV, FTP), läs anslutningsadresserna, se vem som är ansluten och håll delningen igång över Wi-Fi eller en USB-kabel."
keywords: ["Everdisk delning", "trådlös disk iPhone", "starta delning", "dela filer iPhone", "dela foton över nätverk", "DLNA HTTP WebDAV FTP", "vad du kan dela", "så ansluter du", "håll appen öppen", "delning över Wi-Fi eller USB"]
tags: ["everdisk", "guide", "sharing"]
readingTime: 9
---


Fliken **Delning** är hjärtat i Everdisk. Det är här du förvandlar din iPhone eller iPad till en trådlös disk, väljer exakt vad du vill dela och får adresserna som andra enheter använder för att ansluta. Det är den första fliken du ser när du öppnar appen.

## Starta och stoppa delning

I mitten av delningsskärmen finns en stor rund knapp.

- Tryck på **Start** för att ta alla dina aktiverade servrar online samtidigt. Knappen visar **Startar...** och sedan **Stopp** när delningen är igång.
- Tryck på **Stopp** för att ta allt offline igen. Anslutna enheter kopplas bort.

Medan delningen är igång är dina valda filer, foton och din musik tillgängliga för alla enheter i samma nätverk som ansluter med någon av de fyra metoderna nedan.

> Delning körs bara medan appen är öppen. Se **Håll appen öppen** längst ner på den här sidan för att förstå varför, och hur du håller stora överföringar igång.

## Välj vad du vill dela

Innan du startar, tryck på rubriken **Vad du vill dela** för att öppna tre grupper. Du kan dela vilken kombination av dem som helst, och du måste välja minst en sak innan delning kan starta.

**Filer och mappar**

- Appens egen **Dokument**-mapp delas som standard. Du kan sluta dela den om du föredrar det.
- Tryck på **Lägg till mapp** för att dela en mapp från valfri plats på din enhet, eller på **Lägg till fil** för att dela enskilda filer.
- Varje delat objekt har en **Info**-knapp och en **Sluta dela**-knapp.

**Foton och videor**

- Slå på **Tillåt åtkomst till hela fotobiblioteket** för att dela hela ditt foto- och videobibliotek, eller
- Tryck på **Lägg till foton** för att handplocka endast de foton och videor du vill dela.

**Musik**

- Slå på **Tillåt åtkomst till hela musikbiblioteket** för att dela hela ditt musikbibliotek, eller
- Tryck på **Lägg till spår** för att bara dela utvalda låtar.
- Spår som är skyddade (DRM) eller lagrade endast i molnet kan inte delas.

Om du försöker starta utan att ha valt något visar Everdisk meddelandet **Inget att dela**. Om du ändrar vad som delas medan delningen är igång, **stoppa och starta igen** för att verkställa ändringen.

## De fyra servrarna

Everdisk delar samma innehåll på fyra sätt samtidigt. Var och en är utformad för en viss typ av enhet, och var och en kan slås på eller av i **Inställningar → Delning → Anslutningar**. Som standard är alla fyra på.

- **TV och mediacenter (DLNA)** - för smarta TV-apparater och mediaspelare. De upptäcker din enhet på egen hand och visar dina foton, videor och din musik, med förhandsvisningsminiatyrer.
- **Webbläsare (HTTP)** - för vilken telefon, surfplatta eller dator som helst. Den andra personen öppnar en länk i en webbläsare för att bläddra och ladda ner dina filer. Inget att installera.
- **Dator (WebDAV)** - för en Mac, Windows-PC eller Linux-dator. Din enhet visas som en vanlig nätverksdisk så att du kan dra filer åt båda hållen.
- **Andra appar och enheter (FTP)** - för filappar och avancerade användare som talar FTP.

För steg-för-steg-instruktioner om anslutning för varje typ, se [Anslut dina enheter](/docs/guide/everdisk/everdisk-guide-connect).

## Så ansluter du och anslutningsadresser

När du har tryckt på Start visar sektionen **Så ansluter du** ett kort för varje aktiv server med den exakta **adressen** att skriva in på den andra enheten. Varje adress är enkel att kopiera - tryck på den för att kopiera, använd knappen **Dela** för att skicka den, eller tryck på **info-knappen (ⓘ)** för detaljerade instruktioner per protokoll.

- DLNA-kortet visar en enhetsbeskrivningsadress som slutar på `/device-desc.xml` för spelare som frågar efter en sådan.
- När din enhet är ansluten till en Mac med en kabel visas en extra adress med märkningen **Kabelanslutning** som använder din enhets `.local`-namn.

Du kan också öppna adressen som en **QR-kod** så att en annan enhets kamera kan hoppa direkt till den.

## Vem som är ansluten

Sektionen **Vem som är ansluten** listar de enheter som är anslutna till dig just nu, i realtid. Tryck på knappen Fler åtgärder bredvid en enhet för att **Blockera den här enheten** om du inte känner igen den. Blockerade enheter hanteras i [Åtkomst och integritet](/docs/guide/everdisk/everdisk-guide-access).

## Ditt enhetsnamn och din avatar

Varje enhet har ett vänligt namn (som "Speedy-Hare") och en färgad avatar. Detta är namnet som en TV, dator eller annan app visar för din enhet i nätverket, så att den är lätt att känna igen. Du kan generera nytt namn och ny avatar gratis, eller ange ett eget namn, en egen ikon eller fotoavatar med Premium. Se [Inställningar](/docs/guide/everdisk/everdisk-guide-settings).

## Dela över Wi-Fi eller en USB-kabel

Delning kan köras i två situationer:

- **Över Wi-Fi** - din enhet och de andra enheterna är på samma Wi-Fi-nätverk.
- **Över en USB-kabel** - din enhet är ansluten till en **Mac** med en kabel, även när det inte finns någon Wi-Fi alls. Detta är snabbare än Wi-Fi och fungerar fortfarande på ett flygplan, på ett hotell eller i ett låst nätverk.

Om varken Wi-Fi eller en kabel är tillgänglig är knappen **Start** inaktiverad och meddelandet **Ingen Wi-Fi-anslutning** visas. Om anslutningen bryts under delning stoppar Everdisk delningen automatiskt och meddelar dig. Tryck på info-knappen på något av dessa meddelanden för en fullständig förklaring.

## Håll appen öppen

Eftersom din iPhone eller iPad fungerar som server, **fungerar delning bara medan Everdisk är öppen på skärmen**. Om du stänger appen eller låser enheten under en längre tid kan systemet pausa appen och delningen stoppas.

För stora överföringar:

- Håll Everdisk öppen och i förgrunden.
- Anslut din enhet till ström.
- Ställ in **Automatiskt lås** på **Aldrig** i iOS Inställningar-appen medan du överför.

Du kan slå på **Meddela innan frånkoppling** (i Inställningar → Delning) så att Everdisk påminner dig om att öppna appen igen innan systemet pausar den. Tryck på info-knappen på bannern **Håll appen öppen** för mer detaljer.

## Nästa steg

- [Anslut dina enheter](/docs/guide/everdisk/everdisk-guide-connect) - anslut en TV, dator, webbläsare, telefon eller USB-kabel.
- [Åtkomst och integritet](/docs/guide/everdisk/everdisk-guide-access) - lägg till ett lösenord och kontrollera redigering.
- [Inställningar](/docs/guide/everdisk/everdisk-guide-settings) - slå på eller av servrar och justera kvaliteten.
