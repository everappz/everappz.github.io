---
title: "Anslut till servrar"
date: 2026-08-20
description: "Använd fliken Enheter i Everdisk för att ansluta till andra servrar i ditt nätverk. Lägg till och bläddra bland DLNA-, WebDAV-, FTP- och SFTP-servrar och NAS-diskar, streama ljud och video, ladda ner filer och skapa, ladda upp, byt namn, flytta eller ta bort på servrar som tillåter det."
keywords: ["Everdisk fliken Enheter", "ansluta till NAS", "DLNA-klient iPhone", "WebDAV-klient iPhone", "FTP-klient iPhone", "SFTP-klient iPhone", "bläddra nätverksserver", "streama från NAS", "ladda ner från server", "ansluta moln WebDAV"]
tags: ["everdisk", "guide", "devices", "connections"]
readingTime: 9
---


Everdisk är inte bara en trådlös disk - det är också en klient för de andra enheterna i ditt nätverk. Fliken **Enheter** låter dig ansluta till **DLNA**-, **WebDAV**-, **FTP**- och **SFTP**-servrar, inklusive NAS-diskar och mediaservrar, för att sedan bläddra, streama och ladda ner deras filer.

## Enheter-skärmen

Fliken Enheter har två delar:

- **Anslutningar** - de servrar du redan har sparat.
- **Tillgängliga enheter** - servrar som Everdisk hittar automatiskt på ditt lokala nätverk.

För att ansluta till något Everdisk redan har hittat, tryck bara på det under **Tillgängliga enheter**. För att lägga till en server manuellt, tryck på **plus-knappen (+)** eller på **Ny anslutning**.

## Lägg till en ny anslutning

Tryck på **Ny anslutning** och välj den typ av server du vill nå:

- **DLNA / UPnP** - bäst för mediaservrar. Streama video, musik och foton från mediabibliotek, nätverkslagringsenheter och DLNA-aktiverade TV-apparater och datorer. DLNA är skrivskyddat: du kan bläddra, streama och ladda ner, men du kan inte ladda upp eller ändra filer.
- **WebDAV** - anslut till filservrar, nätverkslagringsenheter och molndiskar som stöder WebDAV. Läs och skriv när servern tillåter det.
- **FTP** - vanligt på routrar, nätverkslagringsenheter och webbhotell. Standardporten är 21 (990 för säker FTPS); du kan ange en anpassad port i adressen, till exempel `ftp://host:2121`. Lämna inloggning och lösenord tomma för anonym åtkomst.
- **SFTP** - anslut säkert via SSH. Standardporten är 22; använd en anpassad port i adressen vid behov, till exempel `sftp://host:2222`.

> Everdisk ansluter endast till dessa protokoll för lokala nätverk och direkt adresserade anslutningar. Appen loggar inte in på molnkonton som Google Drive eller Dropbox. En molndisk går bara att nå om den tjänsten erbjuder en **WebDAV**-adress du kan skriva in.

## Ange adressen och logga in

I anslutningsredigeraren fyller du i:

- **Titel** - ett vänligt namn för anslutningen.
- **URL / adress** - serveradressen (exempel visas för varje typ).
- **Inloggning** och **Lösenord** - lämna båda tomma om servern tillåter anonym åtkomst.

För WebDAV kan du tillåta ogiltiga certifikat om din server använder ett självsignerat certifikat. Om en säker servers identitet inte kan verifieras ber Everdisk dig att bekräfta innan den litar på den.

Gratisanvändare kan spara upp till **10** anslutningar. Premium tar bort gränsen.

## Bläddra, streama och ladda ner

När du är ansluten, tryck på servern för att öppna den:

- **Bläddra** bland mapparna i list- eller rutnätsvy, sortera dem och se miniatyrer. DLNA-servrar visar även musikdetaljer och omslag.
- **Streama** ljud och video. Ljud går till minispelarens kö; video spelas upp i helskärm. Du kan spola medan en fil streamas.
- **Ladda ner** filer till din enhet. Välj flera samtidigt för en batchnedladdning. Nedladdningar visas i **Filöverföringar** och hamnar i din **Dokument**-mapp.
- **Info** på ett objekt visar dess typ, storlek, datum, sökväg och mediadetaljer.

## Ändra filer på en server

På servrar som tillåter skrivning - **WebDAV, FTP och SFTP** - kan du även hantera filer:

- **Ny mapp**
- **Ladda upp filer** från din enhet
- **Byt namn**, **Flytta** och **Ta bort** (ett objekt eller flera samtidigt)

**DLNA**-servrar är skrivskyddade, så dessa åtgärder är inte tillgängliga där.

## Följ dina överföringar

Nedladdningar och uppladdningar körs i bakgrunden och visas i **Filöverföringar**, som du öppnar från övre vänstra hörnet på fliken **Dokument**. Där kan du se förloppet och pausa, återuppta, göra om, avbryta eller rensa uppgifter. Du kan också justera överföringar i [Inställningar → Nätverk](/docs/guide/everdisk/everdisk-guide-settings) (endast Wi-Fi kontra Wi-Fi och mobildata, hur många som körs samtidigt och om de fortsätter i bakgrunden).

## Nästa steg

- [Filer och dokument](/docs/guide/everdisk/everdisk-guide-files) - hantera allt du laddar ner.
- [Foton, musik och video](/docs/guide/everdisk/everdisk-guide-media) - spela upp det du streamar.
- [Inställningar](/docs/guide/everdisk/everdisk-guide-settings) - anslutningsgränser och överföringsalternativ.
