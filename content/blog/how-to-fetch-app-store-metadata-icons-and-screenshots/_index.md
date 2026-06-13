---
title: "Fetch App Store Metadata, Icons & Screenshots — Free Tool"
date: 2026-06-13
description: "Step-by-step guide to fetching any iOS app's metadata, icon, screenshots, and localized App Store details using AppLookup.pro — a free, browser-based tool powered by the official iTunes Search API."
keywords: [
  "app store metadata", "fetch app store data", "app store icon download",
  "app store screenshots download", "app store lookup tool", "itunes search api",
  "app metadata extractor", "iOS app metadata", "app store api free tool",
  "download app icon high resolution", "app store competitor research",
  "localized app store data", "app store country lookup", "free aso research tool"
]
tags: [
  "App Store Metadata", "App Lookup", "iTunes Search API",
  "App Icon Download", "App Screenshots", "ASO Research"
]
aliases:
  - /post/how-to-fetch-app-store-metadata-icons-and-screenshots/
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

## Why You Need Fast Access to App Store Metadata

**TL;DR:** Whether you are researching competitors, building an ASO report, mirroring an app icon at 1024×1024, or pulling localized release notes, you need a fast way to query the App Store. [AppLookup.pro](https://applookup.pro) is a free, browser-based tool that returns every public field for any iOS app — name, description, version, ratings, icon, screenshots, supported devices, and the raw iTunes API response — and lets you copy each field to the clipboard with one tap.

Reliable App Store data is the foundation of:

- **ASO research** — analyze how top-ranking apps write their titles, subtitles, descriptions, and keywords.
- **Competitor benchmarking** — track version cadence, rating volume, and pricing across markets.
- **Asset extraction** — download the official 1024×1024 icon and full-resolution screenshots in one ZIP.
- **Localization audits** — compare description, release notes, and screenshots across 40+ App Store storefronts.
- **API integration** — copy the raw iTunes Search API JSON to test your own backend pipelines.

## What Is AppLookup.pro?

[AppLookup.pro](https://applookup.pro) is a free, lightweight App Store lookup tool that runs entirely in your browser. It uses Apple's official [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html), so every result is fetched directly from Apple — no scraping, no third-party caching, no signup, no tracking.

### Key Features

- **Search by app name or paste any App Store URL** — autocomplete suggests apps as you type.
- **40+ country storefronts** — switch between US, UK, JP, DE, FR, BR and more.
- **Full metadata** — title, subtitle, developer, bundle ID, version, price, file size, ratings, release date, content rating, languages, supported devices.
- **High-resolution assets** — icons at 60, 100, 256, 512, and 1024 px; iPhone, iPad, and Apple TV screenshots.
- **Bulk ZIP download** — grab every icon size or every screenshot in a single archive.
- **Raw iTunes API JSON** — the exact response from Apple, ready to copy into your code.
- **Copy buttons on every field** — one tap, value lands in your clipboard.

## How to Use AppLookup.pro (Step by Step)

### Step 1 — Enter an App Name or Paste an App Store URL

Open [applookup.pro](https://applookup.pro) and start typing the app name. The autocomplete pulls live results from Apple as you type. You can also paste a direct App Store link such as `https://apps.apple.com/us/app/instagram/id389801252` or a bare app ID — the tool extracts the ID automatically and even handles Google redirect URLs.

![Enter an app name or App Store URL into AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Step 2 — Fetch App Info and Download Artworks

Click **Lookup** (or press Enter). The tool calls the official iTunes Search API and renders the app icon, developer name, rating, version, and price within a second. Scroll to the **App Icon — All Sizes** section to grab the icon at 60, 100, 256, 512, or 1024 px. Each card has a direct CDN link and a **Download** button. Use **Download All Icons (ZIP)** to grab every size as a single archive, or use the equivalent button under each screenshot section for iPhone, iPad, and Apple TV assets.

![Download app icons and screenshots in all sizes from AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Step 3 — Read App Details and Copy Any Field with One Tap

Below the artwork you will find the **App Details** grid: bundle ID, version, price, file size, minimum OS, release date, last updated date, content rating, genres, genre IDs, languages, seller, artist ID, and track ID. Every card has a **Copy** button — tap it and the value lands in your clipboard with a green "Copied" confirmation. The same applies to the **Description**, **What's New**, and **Supported Devices** sections, which are all scrollable and individually copyable.

![View full App Store details and copy any field with one tap](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Step 4 — View the Raw App Store API Response

Need the exact JSON Apple returns? Scroll to the **Raw API Response** section. The complete iTunes Search API payload is rendered in a scrollable, syntax-friendly viewer, with a **Copy** button in the header that copies the entire JSON object to your clipboard. The iTunes Lookup URL is also shown so you can replay the request in any HTTP client.

![View and copy the raw iTunes Search API JSON response](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Step 5 — Change the Country to See the Localized Version

App Store metadata is localized. The same app can have a different title, subtitle, description, screenshots, and even pricing across storefronts. Select a new country from the dropdown at the top — the URL in the input box rewrites automatically, and clicking **Lookup** re-fetches the app in that market. This is the fastest way to audit how a competitor presents their app in Japan, Germany, Brazil, or any of the 40+ supported countries.

![Switch country storefronts to see localized App Store metadata](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Step 6 — Copy Localized Metadata Field by Field

Once the localized version is loaded, every text field works exactly the same way: tap the **Copy** button beside the description, what's new, app name, developer, bundle ID, or any detail item to capture the localized string. This makes it trivial to build side-by-side comparison spreadsheets or to feed localized copy into translation QA workflows.

![Copy localized App Store description and metadata with one tap](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Practical Use Cases

- **Competitor ASO teardown.** Compare the title, subtitle, description structure, screenshot order, and update frequency of top-ranking competitors.
- **Icon and screenshot benchmarking.** Download every competitor asset in full resolution and review them side by side.
- **Localization gap analysis.** Switch countries to see which markets a competitor actually localizes — and where they ship the default English copy.
- **Pricing and tier research.** Confirm price, currency, and in-app purchase availability across storefronts.
- **API and integration testing.** Copy the raw iTunes Search API JSON straight into Postman or a unit test.
- **Press kits and case studies.** Grab the official 1024×1024 icon and high-resolution screenshots for blog posts and slide decks.

## Privacy & Disclaimer

AppLookup.pro runs entirely in your browser. There is no login, no tracking, and no server-side logging of the apps you look up. All requests go directly from your browser to Apple's [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html).

This tool is provided for **educational and research purposes only**. All data is fetched from Apple's official public API and remains the property of Apple Inc. and the respective app publishers. Usage is subject to the [Apple Media Services Terms and Conditions](https://www.apple.com/legal/internet-services/terms/site.html). Do not use the tool to violate rate limits, redistribute copyrighted assets, or build commercial scraping pipelines.

## Get Started

You do not need an API key, a developer account, or any paid subscription to inspect App Store data. Open [applookup.pro](https://applookup.pro), paste any App Store URL, and you will have the full metadata, icons, and raw JSON in seconds.

## Contribute to the Project

AppLookup.pro is open source. Bug reports, new country support, and pull requests are welcome.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro on GitHub" icon="github" tag="open source" >}}
{{< /cards >}}

---

## Frequently Asked Questions

{{% details title="Is AppLookup.pro really free?" closed="true" %}}
Yes. AppLookup.pro is 100% free, open source, and runs entirely in your browser. There is no signup, no paid tier, and no usage cap beyond Apple's own iTunes Search API limits.
{{% /details %}}

{{% details title="Where does the data come from?" closed="true" %}}
Every result is fetched in real time from Apple's official [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html). The tool does not scrape App Store pages and does not cache responses on any server.
{{% /details %}}

{{% details title="Can I download the 1024×1024 app icon?" closed="true" %}}
Yes. The **App Icon — All Sizes** section exposes the icon at 60, 100, 256, 512, and 1024 pixels with direct CDN links and a one-click download. You can also grab every size in a single ZIP archive.
{{% /details %}}

{{% details title="Can I download all App Store screenshots at once?" closed="true" %}}
Yes. Each screenshot section (iPhone, iPad, Apple TV) has a **Download All (ZIP)** button that packages every screenshot at full resolution into one archive.
{{% /details %}}

{{% details title="How do I see how an app is localized in another country?" closed="true" %}}
Use the country dropdown at the top of the page. Select the target storefront (40+ countries are supported) and click **Lookup** again — the tool re-queries the iTunes API for that market and shows the localized title, description, screenshots, release notes, and pricing.
{{% /details %}}

{{% details title="Can I copy individual fields like bundle ID or release date?" closed="true" %}}
Yes. Every text field in the result — app name, developer, description, what's new, bundle ID, version, price, file size, minimum OS, release date, content rating, languages, supported devices, and raw JSON — has its own **Copy** button.
{{% /details %}}

{{% details title="Does AppLookup.pro work for any iOS app?" closed="true" %}}
It works for any app that is publicly listed in at least one App Store storefront and returned by the iTunes Search API. Unlisted, removed, or enterprise-distributed apps will not return results.
{{% /details %}}

{{% details title="Can I use the raw JSON output in my own code?" closed="true" %}}
Yes. The **Raw API Response** section shows the exact JSON returned by Apple. Copy it directly into Postman, a unit test, or your backend pipeline. Remember to respect Apple's API terms and reasonable rate limits.
{{% /details %}}

{{% details title="Is it safe to paste App Store URLs into the tool?" closed="true" %}}
Yes. URL parsing happens entirely in your browser. The only outbound network call is the lookup to Apple's iTunes Search API.
{{% /details %}}

{{% details title="What is the difference between AppLookup.pro and AppKeywords.pro?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) is for **reading** App Store metadata from any published app — competitor research, asset extraction, localization audits. [AppKeywords.pro](https://appkeywords.pro) is for **writing** App Store metadata for your own app — title, subtitle, and keyword optimization with Fastlane integration. The two tools complement each other.
{{% /details %}}
