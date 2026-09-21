---
title: 'App Details Shortcode Demo'
date: '2026-01-01T00:00:00+00:00'
build:
  list: never
  render: always
  publishResources: false
sitemap:
  disable: true
---

# App Details Shortcode

The `app-details` shortcode fetches live App Store data via the public iTunes
Lookup API and renders each app in a single row: the app icon, title, and a
download button on the left, with the full detail sheet on the right.

## Usage

```
{{</* app-details ids="885367198, 1097564256" */>}}
```

Pass a comma-separated list of App Store numeric IDs to the `ids` param
(positional args and an optional `country="us"` param are also supported).

## Showcase — all Everappz apps

Evermusic, Flacbox, EverVideo, Evertag and Everdisk — iOS and Mac editions.

{{< app-details ids="885367198, 905746421, 1564384601, 1097564256, 1594027432, 6602897336, 6743504109, 1450763230, 1594027661, 6751851132" >}}
