---
title: "Toegang en privacy"
date: 2026-08-20
description: "Houd je delen met Everdisk veilig: bescherm de toegang met een login en wachtwoord, bepaal met Bestanden bewerken of verbonden apparaten mogen uploaden, hernoemen en verwijderen, blokkeer onbekende apparaten, kies tussen prullenbak en definitief verwijderen en begrijp waarom alles op je lokale netwerk blijft."
keywords: ["Everdisk wachtwoordbeveiliging", "schakelaar bestanden bewerken", "apparaat blokkeren", "geblokkeerde apparaten", "bestanden definitief verwijderen", "alleen lokaal netwerk", "privé bestanden delen", "DLNA geen wachtwoord", "netwerkveiligheid"]
tags: ["everdisk", "handleiding", "toegang", "privacy", "beveiliging"]
readingTime: 8
---


Everdisk houdt je bestanden op je eigen netwerk en geeft je eenvoudige knoppen om te bepalen wie erbij kan en wat ze mogen doen. Je vindt deze knoppen in **Instellingen → Delen → Toegang**, plus een paar bijbehorende instellingen in de Bestandsbeheerder.

## Bescherm de toegang met een login en wachtwoord

Standaard kan iedereen op hetzelfde netwerk die je adres heeft je gedeelde bestanden openen. Om een aanmelding te vereisen:

1. Ga naar **Instellingen → Delen → Toegang**.
2. Voer een **Login** en een **Wachtwoord** in.
3. Nu vragen de verbindingen **Browser (HTTP)**, **Computer (WebDAV)** en **Andere apps en apparaten (FTP)** allemaal om die gegevens voordat ze je bestanden tonen.

Laat beide velden leeg voor open toegang. Je wachtwoord wordt veilig opgeslagen in de sleutelhanger van het apparaat.

> **DLNA is altijd open.** De verbinding Tv en mediacenter (DLNA) kan niet met een wachtwoord worden beveiligd, dus zodra die aan staat, kan elk apparaat op hetzelfde Wi-Fi je gedeelde media doorbladeren. Zet hem uit als je alleen beveiligde verbindingen wilt, en deel alleen op netwerken die je vertrouwt.

## Bewerken toestaan of blokkeren (Bestanden bewerken)

De schakelaar **Bestanden bewerken** bepaalt of verbonden apparaten je bestanden alleen mogen bekijken, of ze ook mogen wijzigen.

- **Aan** (de standaard): verbonden apparaten kunnen je gedeelde bestanden **uploaden, hernoemen en verwijderen** - zo werkt je apparaat als een echte tweerichtings-netwerkschijf.
- **Uit**: je gedeelde bestanden zijn **alleen-lezen**. Anderen kunnen bekijken en downloaden, maar niets toevoegen of wijzigen.

Als je hem aanzet, verschijnt er een korte waarschuwing, omdat anderen hierdoor je bestanden kunnen wijzigen. Zolang hij aan staat, draagt hij een badge **Belangrijk**.

## Een apparaat blokkeren

Als je een apparaat ziet dat je niet herkent:

1. Zoek het op het Delen-scherm onder **Wie is verbonden**.
2. Tik op de knop Meer acties en kies **Dit apparaat blokkeren**.

Geblokkeerde apparaten staan in **Instellingen → Delen → Toegang → Geblokkeerde apparaten**, waar je er een kunt **deblokkeren** of **Alles deblokkeren**. Het blokkeren volgt het apparaat, zelfs als zijn netwerkadres verandert (voor de verbindingen Browser, Computer en Tv).

## Prullenbak versus definitief verwijderen

Wanneer een bestand wordt verwijderd - door jou in de bestandsbeheerder, of door een verbonden apparaat - gaat het normaal gesproken naar een herstelbare **prullenbak**, zodat je het terug kunt halen.

Verwijder je bestanden liever meteen zonder herstel, zet dan **Bestanden definitief verwijderen** aan in **Instellingen → Bestandsbeheerder → Bestanden verwijderen**. Dit staat standaard uit. **Het geldt voor de bestandsbeheerder op het apparaat** en voor **verwijderingen via het netwerk**; het verandert niets aan hoe de systeem-fotobibliotheek of muziekbibliotheek met verwijderen omgaat.

## Alles blijft lokaal

Everdisk deelt alleen over je **lokale netwerk** - er wordt niets naar het internet geüpload en er zit geen cloudaccount tussen. Een paar dingen die goed zijn om te weten:

- Everdisk heeft de iOS-machtiging **Lokaal netwerk** nodig, zodat apparaten in de buurt het kunnen vinden. Staat die machtiging uit, dan legt een melding uit hoe je hem weer aanzet in de iOS-app Instellingen.
- Voor de meeste privacy deel je alleen terwijl je op een **thuis- of privé-Wi-Fi**-netwerk zit dat je vertrouwt, en wees voorzichtig op openbare Wi-Fi. Een login en wachtwoord helpen, maar zijn geen vervanging voor een vertrouwd netwerk.
- De **meest private optie van allemaal is een USB-kabel naar een Mac** - de gegevens gaan rechtstreeks over de kabel en raken nooit de router of het internet. Zie [Je apparaten verbinden](/docs/guide/everdisk/everdisk-guide-connect).

## Volgende stappen

- [Delen](/docs/guide/everdisk/everdisk-guide-sharing) - kies wat je deelt en start met delen.
- [Instellingen](/docs/guide/everdisk/everdisk-guide-settings) - alle instellingen voor Toegang en Bestandsbeheerder op één plek.
