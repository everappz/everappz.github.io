---
title: "App Store Metadaten, Icons und Screenshots kostenlos abrufen: So geht's"
date: 2026-06-13
description: "Schritt für Schritt Anleitung zum Abrufen der Metadaten, des Icons, der Screenshots und der lokalisierten App Store Details jeder iOS App mit AppLookup.pro, einem kostenlosen Browser Tool auf Basis der offiziellen iTunes Search API."
keywords: [
  "app store metadaten", "app store daten abrufen", "app store icon herunterladen",
  "app store screenshots herunterladen", "app store lookup tool", "itunes search api",
  "app metadaten extraktor", "iOS app metadaten", "kostenloses app store api tool",
  "app icon hochauflösend herunterladen", "app store wettbewerbsanalyse",
  "lokalisierte app store daten", "app store länder suche", "kostenloses aso tool"
]
tags: [
  "App Store Metadaten", "App Lookup", "iTunes Search API",
  "App Icon Download", "App Screenshots", "ASO Recherche"
]
sidebar:
  exclude: true
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## App Store Daten in Sekunden abrufen

**Kurzfassung:** [AppLookup.pro](https://applookup.pro) ist ein kostenloses Tool, das öffentliche Daten jeder iOS, iPadOS, macOS oder tvOS App abruft. Sie erhalten den Titel, die Beschreibung, die Neuerungen, die Version, den Preis, die Bewertungen, das App Icon, die Screenshots, die unterstützten Geräte und die Rohantwort der iTunes API. Jedes Feld hat eine Ein Tipp Kopierschaltfläche. Öffnen Sie die Seite, fügen Sie einen App Store Link ein oder tippen Sie den App Namen, und Sie haben die Daten.

Nutzen Sie es für:

- **ASO Recherche.** Sehen Sie, wie Top Apps ihre Titel, Untertitel, Beschreibungen und Keywords formulieren.
- **Wettbewerbsbeobachtung.** Prüfen Sie Versions Updates, Bewertungen und Preise in allen Märkten.
- **Asset Download.** Sichern Sie das offizielle App Icon und Screenshots in voller Größe in einem ZIP.
- **Lokalisierungsprüfungen.** Vergleichen Sie Beschreibung, Neuerungen und Screenshots in über 40 App Store Ländern.
- **API Tests.** Kopieren Sie das rohe iTunes Search API JSON direkt in Ihren Code oder in Postman.

## Was ist AppLookup.pro?

[AppLookup.pro](https://applookup.pro) ist ein kostenloses, browserbasiertes App Store Lookup Tool. Es läuft komplett auf Ihrem Gerät. Jedes Ergebnis kommt direkt aus Apples offizieller [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html). Kein Scraping. Keine Anmeldung. Kein Tracking.

### Was Sie bekommen

- **Suche nach App Name oder App Store URL.** Die Autovervollständigung zeigt Live Ergebnisse während Sie tippen.
- **Über 40 Länder Storefronts.** Wechseln Sie zwischen US, UK, JP, DE, FR, BR und mehr.
- **Vollständige Metadaten.** Titel, Untertitel, Entwickler, Bundle ID, Version, Preis, Dateigröße, Bewertungen, Veröffentlichungsdatum, Altersfreigabe, Sprachen und unterstützte Geräte.
- **Hochauflösende Assets.** App Icons und Screenshots für iPhone, iPad, macOS und Apple TV.
- **Bulk ZIP Download.** Holen Sie sich alle Icons oder alle Screenshots in einem Archiv.
- **Rohes iTunes API JSON.** Die exakte Antwort von Apple, fertig zum Kopieren.
- **Kopierschaltflächen an jedem Feld.** Ein Tipp legt den Wert in die Zwischenablage.

## So nutzen Sie AppLookup.pro Schritt für Schritt

### Schritt 1. App Namen eingeben oder App Store URL einfügen

Öffnen Sie [applookup.pro](https://applookup.pro) und beginnen Sie, den App Namen einzutippen. Die Autovervollständigung zeigt Live Ergebnisse aus dem App Store während Sie tippen.

Sie können auch einen direkten App Store Link wie `https://apps.apple.com/us/app/instagram/id389801252` oder nur die App ID einfügen. Das Tool extrahiert die ID für Sie. Es verarbeitet auch Google Redirect URLs.

![App Namen oder App Store URL in AppLookup.pro eingeben](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Schritt 2. App Infos abrufen und das Icon herunterladen

Klicken Sie auf **Lookup** oder drücken Sie Enter. Das Tool ruft die offizielle iTunes Search API auf und zeigt das App Icon, den Entwicklernamen, die Bewertung, die Version und den Preis in weniger als einer Sekunde.

Scrollen Sie zum Abschnitt **App Icon**. Jede von Apple zurückgegebene Icon Größe erscheint als Karte. Jede Karte hat:

- **Direct Link.** Öffnet das Bild in voller Größe in einem neuen Tab.
- **Download.** Speichert die Datei auf Ihrem Computer.

Nutzen Sie **Download All Icons (ZIP)**, um alle Icon Größen in einem Archiv zu erhalten. Genauso bei Screenshots: jeder Plattformabschnitt hat seine eigene **Download All (ZIP)** Schaltfläche.

![App Icons und Screenshots von AppLookup.pro herunterladen](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Schritt 3. App Details lesen und beliebige Felder kopieren

Scrollen Sie zu **App Details**. Sie sehen Bundle ID, Version, Preis, Dateigröße, Mindest OS, Veröffentlichungsdatum, letztes Aktualisierungsdatum, Altersfreigabe, Genres, Genre IDs, Sprachen, Verkäufer, Artist ID und Track ID.

Tippen Sie die **Copy** Schaltfläche auf einer beliebigen Karte. Der Wert wandert in Ihre Zwischenablage und die Schaltfläche zeigt ein grünes 'Copied' Häkchen.

Das funktioniert genauso bei **Description**, **What's New** und **Supported Devices**. Diese Abschnitte sind scrollbar, sodass Sie den gesamten Text lesen können, ohne die Stelle zu verlieren, und die Copy Schaltfläche legt das gesamte Feld in Ihre Zwischenablage.

![Vollständige App Store Details ansehen und jedes Feld mit einem Tipp kopieren](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Schritt 4. Die rohe App Store API Antwort ansehen

Brauchen Sie das exakte JSON, das Apple zurückgibt? Scrollen Sie zu **Raw API Response**. Die vollständige Payload der iTunes Search API wird in einem scrollbaren Viewer mit einer **Copy** Schaltfläche oben angezeigt. Ein Tipp kopiert das gesamte JSON Objekt.

Die **iTunes Lookup URL** wird direkt darüber gezeigt. Fügen Sie sie in Postman, curl oder Ihren Browser ein, um dieselbe Anfrage zu wiederholen.

![Die rohe iTunes Search API JSON Antwort ansehen und kopieren](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Schritt 5. Das Land wechseln, um die lokalisierte Version zu sehen

App Store Metadaten ändern sich je nach Land. Dieselbe App hat oft einen anderen Titel, Untertitel, Beschreibung, Screenshots und Preis in jedem Markt.

Wählen Sie ein Land aus dem Dropdown oben. Die URL im Eingabefeld wird automatisch aktualisiert. Klicken Sie erneut auf **Lookup**, um die App in diesem Markt erneut abzurufen.

Das ist der schnellste Weg zu prüfen, wie ein Wettbewerber seine App in Japan, Deutschland, Brasilien oder in einem der über 40 unterstützten Länder präsentiert.

![Länder Storefronts wechseln, um lokalisierte App Store Metadaten zu sehen](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Schritt 6. Die lokalisierten Metadaten kopieren

Sobald das Länderergebnis geladen ist, funktioniert jedes Feld gleich. Tippen Sie **Copy** bei Beschreibung, Neuerungen, App Name, Entwickler, Bundle ID oder einer beliebigen Detailkarte, um den lokalisierten Text zu erfassen.

So lassen sich leicht Vergleichstabellen Seite an Seite erstellen oder lokalisierte Texte in ein Übersetzungs Review einspeisen.

![Lokalisierte App Store Beschreibung und Metadaten mit einem Tipp kopieren](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Wer AppLookup.pro nutzt

- **Indie Entwickler**, die vor einem Launch ASO Recherche machen.
- **ASO und Marketing Teams**, die Updates und Preise der Wettbewerber verfolgen.
- **Designer**, die das offizielle hochauflösende App Icon und Screenshots für Pressekits und Fallstudien holen.
- **Lokalisierungsteams**, die prüfen, welche Märkte abgedeckt sind und wo noch der englische Standardtext ausgeliefert wird.
- **Backend und QA Ingenieure**, die iTunes Search API Integrationen testen, ohne einen Scraper zu schreiben.
- **Autoren und Blogger**, die das offizielle App Icon und ein paar Screenshots für einen Beitrag brauchen.

## Datenschutz und Haftungsausschluss

AppLookup.pro läuft in Ihrem Browser. Es gibt keinen Login. Es gibt kein Tracking. Es gibt keine serverseitige Protokollierung der Apps, die Sie nachschlagen. Anfragen gehen direkt von Ihrem Browser an Apples [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html).

Dieses Tool dient **ausschließlich Bildungs und Recherchezwecken**. Alle Daten werden über Apples offizielle öffentliche API abgerufen und bleiben Eigentum von Apple Inc. und der aufgeführten App Anbieter. Die Nutzung des Tools unterliegt den [Apple Media Services Geschäftsbedingungen](https://www.apple.com/legal/internet-services/terms/site.html). Bitte respektieren Sie Apples Rate Limits und verteilen Sie keine urheberrechtlich geschützten Assets weiter.

## Jetzt ausprobieren

Sie brauchen keinen API Schlüssel, kein Entwicklerkonto und keinen Bezahltarif, um App Store Daten zu prüfen. Öffnen Sie [applookup.pro](https://applookup.pro), fügen Sie eine beliebige App Store URL ein, und Sie haben die Metadaten, Icons und das rohe JSON in Sekunden.

## Open Source

AppLookup.pro ist Open Source. Bug Reports, Länder Ergänzungen und Pull Requests sind willkommen.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro auf GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Häufig gestellte Fragen

{{% details title="Ist AppLookup.pro wirklich kostenlos?" closed="true" %}}
Ja. AppLookup.pro ist zu 100 Prozent kostenlos und Open Source. Es läuft in Ihrem Browser. Es gibt keine Anmeldung, keine kostenpflichtige Stufe und keine Nutzungsgrenze über Apples eigene iTunes Search API Limits hinaus.
{{% /details %}}

{{% details title="Woher kommen die Daten?" closed="true" %}}
Jedes Ergebnis wird in Echtzeit von Apples offizieller [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) abgerufen. Das Tool scrapt keine App Store Seiten und cacht keine Antworten auf einem Server.
{{% /details %}}

{{% details title="Kann ich das App Icon in hoher Auflösung herunterladen?" closed="true" %}}
Ja. Der Abschnitt **App Icon** zeigt jede Icon URL, die Apple zurückgibt. Jede Karte hat einen Direct Link und eine Download Schaltfläche, und eine Download All Icons ZIP Schaltfläche packt sie alle in ein Archiv.
{{% /details %}}

{{% details title="Kann ich alle App Store Screenshots auf einmal herunterladen?" closed="true" %}}
Ja. Jeder Screenshot Abschnitt (iPhone, iPad, macOS und Apple TV) hat eine **Download All (ZIP)** Schaltfläche, die alle Screenshots in voller Auflösung bündelt.
{{% /details %}}

{{% details title="Wie sehe ich, wie eine App in einem anderen Land aussieht?" closed="true" %}}
Wählen Sie ein Land im Dropdown oben auf der Seite. Über 40 Storefronts werden unterstützt. Klicken Sie erneut auf **Lookup**, und das Tool ruft die App für dieses Land erneut ab und zeigt den lokalisierten Titel, die Beschreibung, die Screenshots, die Neuerungen und den Preis.
{{% /details %}}

{{% details title="Kann ich einzelne Felder wie Bundle ID oder Veröffentlichungsdatum kopieren?" closed="true" %}}
Ja. Jedes Textfeld im Ergebnis hat seine eigene Copy Schaltfläche: App Name, Entwickler, Beschreibung, Neuerungen, Bundle ID, Version, Preis, Dateigröße, Mindest OS, Veröffentlichungsdatum, Altersfreigabe, Sprachen, unterstützte Geräte und rohes JSON.
{{% /details %}}

{{% details title="Funktioniert AppLookup.pro für jede iOS App?" closed="true" %}}
Es funktioniert für jede App, die in mindestens einem App Store Land öffentlich gelistet ist und von der iTunes Search API zurückgegeben wird. Nicht gelistete, entfernte oder per Enterprise verteilte Apps erscheinen nicht.
{{% /details %}}

{{% details title="Unterstützt es macOS und Apple TV Apps?" closed="true" %}}
Ja. Wenn die App macOS oder Apple TV Screenshots in der Antwort der iTunes Search API hat, zeigt AppLookup.pro sie in einem eigenen scrollbaren Panel mit Download Schaltflächen an.
{{% /details %}}

{{% details title="Kann ich das rohe JSON in meinem eigenen Code verwenden?" closed="true" %}}
Ja. Der Abschnitt Raw API Response zeigt das exakte JSON, das Apple zurückgibt. Kopieren Sie es in Postman, einen Unit Test oder eine Backend Pipeline. Bitte respektieren Sie die API Bedingungen von Apple und vernünftige Rate Limits.
{{% /details %}}

{{% details title="Ist es sicher, App Store URLs in das Tool einzufügen?" closed="true" %}}
Ja. Die URL wird in Ihrem Browser geparst. Der einzige ausgehende Netzwerkaufruf ist die Lookup Anfrage an Apples iTunes Search API.
{{% /details %}}

{{% details title="Was ist der Unterschied zwischen AppLookup.pro und AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) ist zum Lesen von App Store Metadaten jeder veröffentlichten App: Wettbewerbsrecherche, Asset Download, Lokalisierungsprüfungen. [AppKeywords.pro](https://appkeywords.pro) ist zum Schreiben von App Store Metadaten für Ihre eigene App: Titel, Untertitel und Keyword Optimierung mit Fastlane Unterstützung. Die beiden Tools ergänzen sich gut.
{{% /details %}}
