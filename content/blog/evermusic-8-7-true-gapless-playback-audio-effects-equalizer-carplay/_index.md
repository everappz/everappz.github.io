---
title: "Evermusic 8.7: True Gapless Playback, Audio Effects, Volume Normalization, Redesigned Equalizer"
date: 2026-07-05
description: "Evermusic 8.7 for iPhone, iPad, and Mac adds true gapless playback, five studio audio effects (Reverb, Delay, Distortion, Compressor, Crossfeed), EBU R128 volume normalization, a redesigned 10-band equalizer with import/export presets, a rebuilt AVAudioEngine streaming engine with FLAC and Ogg Vorbis support, and faster, more accurate CarPlay and Now Playing."
keywords: ["Evermusic 8.7", "Evermusic update", "true gapless playback iPhone", "gapless music player iOS", "gapless playback CarPlay", "music player audio effects iPhone", "reverb delay distortion compressor crossfeed iOS", "crossfeed headphones iOS", "volume normalization iPhone", "loudness normalization music player", "EBU R128 normalization iOS", "replay gain alternative iPhone", "10-band equalizer iPhone", "graphic equalizer iOS app", "equalizer presets import export", "FLAC player iPhone", "Ogg Vorbis player iOS", "lossless music player iPhone 2026", "AVAudioEngine music player", "CarPlay music player iPhone", "Now Playing lock screen accuracy", "cloud music player iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Gapless Playback", "Audio Effects", "Reverb", "Delay", "Distortion", "Compressor", "Crossfeed", "Volume Normalization", "EBU R128", "Equalizer", "FLAC", "Ogg Vorbis", "CarPlay", "Now Playing", "Liquid Glass", "What's New"]
aliases:
  - /post/evermusic-8-7-true-gapless-playback-audio-effects-equalizer-carplay/
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**TL;DR:** [Evermusic 8.7](/products/evermusic) is a sound-quality release for iPhone, iPad, and Mac. It ships **true gapless playback** (no pauses, clicks, or ticks between tracks), a full set of **studio audio effects** — Reverb, Delay, Distortion, Compressor, and Crossfeed — and **EBU R128 volume normalization** that keeps loudness consistent from song to song without ReplayGain tags. The **10-band equalizer** is redesigned with new sliders, faster preset switching, custom presets you can import and export, and a better landscape and iPad layout. Under the hood, a **rebuilt AVAudioEngine streaming engine** improves reliability and format support, including **FLAC** and **Ogg Vorbis**. **CarPlay** and **Now Playing** are faster and more accurate on the Lock Screen, in the car, and from headphone remotes.

---

## Hello everyone!

Evermusic 8.7 is available to download. This update is all about how your music *sounds*. We rebuilt the playback engine for true gapless playback, added a suite of studio-grade audio effects, introduced loudness normalization, and redesigned the equalizer from the sliders up. Everything is wrapped in Apple's new **Liquid Glass** design.

[Download Evermusic 8.7 from the App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) or update from your existing version. Evermusic is a free download with optional in-app upgrades.

## True Gapless Playback

Gapless playback means the silence between two tracks is gone. No pause, no click, no tick — the current song flows straight into the next one. It matters most for the music that was designed to be heard as a whole: **live recordings, DJ mixes, classical works, and concept albums** where one track fades directly into another.

Here is what changed technically. Evermusic's audio engine keeps two tracks in play at once: the one you are hearing and the next one in the queue. While the current track plays, the next track is already being **fetched, decoded, and pre-buffered** in the background. When the current track reaches its end, the engine hands off to the next track **inside the player, not inside the audio stream**. The output render loop keeps pulling audio samples from a continuous ring buffer without ever stopping, so the listener never hears a boundary. The switch happens between samples, which is exactly why there is no audible gap.

This works the same whether the file is on your device, in the cloud, or on a media server — the pre-buffering just starts a little earlier for remote sources.

## Studio Audio Effects

Evermusic 8.7 adds five real-time audio effects you can stack on top of your music. Each one runs as a native audio-processing node in the playback engine, so it applies to everything you play — local files, cloud streams, and internet radio alike — with no re-encoding.

Every effect ships with a **curated library of presets** to get you a great sound in one tap, and Evermusic **remembers your exact settings** between sessions. Adjust any control and the effect switches to a **Manual** state so you always know when you have moved away from a preset.

### Reverb

Adds a sense of space, from a tight room to a cathedral. Built on Apple's `AVAudioUnitReverb`, it offers **13 room presets** (Small Room, Medium Hall, Plate, Cathedral, and more) plus a **wet/dry mix** control from 0 to 100% so you decide how much space to add.

### Delay (Echo)

A classic echo with **10 presets** — Slapback, Tape Echo, Dub, Ambient, and others. You can dial in the **delay time** (up to 2 seconds), **feedback** (how many repeats), a **low-pass cutoff** to warm up the repeats, and the **wet/dry mix**.

### Distortion

From subtle grit to full lo-fi destruction, driven by `AVAudioUnitDistortion` with **22 character presets** (Bit Brush, Cellphone Concert, Radio Tower, and more), a **pre-gain** drive control, and a wet/dry mix so you can blend the effect back into the clean signal.

### Compressor

A dynamics processor (Apple's `AUDynamicsProcessor`) that evens out loud and quiet passages. It exposes the full professional control set — **threshold, ratio/headroom, attack, release, expansion, and makeup gain** — with **10 presets** tuned for real situations: Voice / Podcast, Late Night, Movie Dialog, Streaming Match, and Maximum Loudness among them.

### Crossfeed

Crossfeed makes headphone listening sound more natural by mixing a little of the left channel into the right and vice versa, the way your ears hear real speakers. It is built on the well-known **Bauer stereophonic-to-binaural (bs2b)** algorithm, with control over the **crossfeed level** and **cutoff frequency**, and **6 presets** including the audiophile-favorite *Chu Moy* and *Jan Meier* settings. It is especially good on older, hard-panned 1960s and 1970s stereo mixes.

## Volume Normalization

Ever built a playlist where one track blasts and the next is a whisper? Volume normalization fixes that. Evermusic 8.7 uses **EBU R128 loudness measurement** (the same ITU-R BS.1770 standard used in broadcast and by streaming services) to measure each track's real perceived loudness and gently steer it toward a consistent target.

Unlike ReplayGain, it does **not** require any tags in your files and it does **not** modify your audio. It works in real time on anything you play, including cloud streams and live radio, and it resets cleanly when you seek or change tracks.

Four presets cover the common cases:

- **Light** — gentle leveling (target −20 LUFS).
- **Standard** — the default, streaming-style loudness (target −16 LUFS, up to +12 dB of lift for quiet tracks).
- **Strong** — aggressive matching for very mixed libraries (target −14 LUFS).
- **Night** — quieter and consistent for low-volume evening listening (target −23 LUFS).

You no longer need to reach for the volume between songs.

## Redesigned Equalizer

Evermusic's **10-band graphic equalizer** got a full redesign. The bands cover **32 Hz to 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), each adjustable from **−12 dB to +12 dB** in fine 0.1 dB steps, with a **preamp** from −24 dB to +24 dB to prevent clipping when you boost.

What is new in 8.7:

- **New sliders** — precise, responsive controls that adopt the native iOS 26 system slider look and the **Liquid Glass** material.
- **Faster, smoother preset switching** — jump between presets instantly, with a redesigned horizontal preset bar in portrait and a vertical preset column in landscape.
- **Better layout in landscape and on iPad** — the sliders and preset picker rearrange to use the extra width instead of cramming into a phone-sized column.
- **Custom presets** — create and save your own curves, reorder them, and **import and export** presets as `.eqp` files to move them between devices or share them.

The equalizer runs natively in the engine (`AVAudioUnitEQ`), so it applies to every source, and it also works over AirPlay, Chromecast, and CarPlay where supported.

## Rebuilt Playback Engine

Under the hood, Evermusic 8.7 runs on a **rebuilt streaming engine** built on Apple's `AVAudioEngine` with a custom render pipeline. This is what makes the gapless handoff, the effects chain, and the equalizer possible, and it also makes everyday playback more reliable.

- **Improved format support** — including **FLAC** (via Core Audio) and **Ogg Vorbis** (via `libvorbisfile`), alongside MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF, and more.
- **Smarter buffering** — an adaptive pre-buffer scales with your connection, with a continuous ring buffer feeding the output so brief network hiccups do not turn into dropouts.
- **Automatic recovery** — a rebuffering state machine and retry logic with backoff resume playback cleanly after a weak-signal moment instead of stopping the track.
- **Fewer interruptions** — the same engine drives local files, cloud streams, media servers, and internet radio, so behavior is consistent everywhere.

## Now Playing and CarPlay

The screens you actually look at while listening — the **Lock Screen**, **CarPlay**, and your car's or headphones' remote buttons — are more accurate and faster in 8.7.

- **More accurate Now Playing info.** Evermusic captures the player's state under a lock before publishing it, so the title, elapsed time, duration, and play/pause state can never disagree with each other on the Lock Screen or in the car. Buffering and loading states are now reported correctly instead of showing "playing" while a track is still fetching.
- **Reliable remote controls.** Play, pause, next, previous, seek, skip, shuffle, repeat, and playback rate all respond consistently from headphone buttons, car controls, and the Lock Screen, driven by `MPRemoteCommandCenter`.
- **Faster CarPlay artwork.** Album art now loads several times faster on long lists (batch pacing cut from 1.0s to 0.25s, with the first visible screen loading immediately), and it now appears in the compact iOS 26 CarPlay list rows that previously showed no artwork.
- **CarPlay sorting and stability fixes.** Faster sorting on large libraries and hardening against edge-case crashes when scrolling long lists.
- **Throttled metadata updates.** Now Playing and remote-command updates are throttled so rapid changes no longer flood the system, which keeps lock-screen and CarPlay controls responsive.

## Other Improvements

- **Liquid Glass design** refinements across the app — translucent surfaces, smoother animations, and refined controls on iOS, iPadOS, and macOS.
- **New Home Screen widgets** with improved update logic that keeps them in sync without draining extra battery.
- Fixes for recent iOS releases.
- Localization fixes across multiple languages.
- Many smaller improvements based on your emails and App Store reviews.

## Why This Update Matters

Evermusic 8.7 is built around one idea: **your music should sound its best, on any source.**

1. **Whole albums, as intended.** True gapless playback means live sets, DJ mixes, and concept albums finally play the way the artist mastered them.
2. **A studio in your pocket.** Reverb, Delay, Distortion, Compressor, Crossfeed, a redesigned equalizer, and loudness normalization give you real control over your sound, not just an on/off switch.
3. **The same experience everywhere.** Local files, cloud drives, media servers, and internet radio all run through the same rebuilt engine, with accurate Now Playing and a faster CarPlay on top.

## Get Evermusic 8.7

[**Download Evermusic from the App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) or update from inside the App Store. Evermusic is a free download with optional in-app upgrades for advanced features.

If you enjoy the app, please leave a rating on the App Store — it genuinely helps. Have feedback or run into an issue? Email us at **support@everappz.com**. We read every message.

## Frequently Asked Questions

{{% details title="What's new in Evermusic 8.7?" closed="true" %}}
Evermusic 8.7 adds true gapless playback, five studio audio effects (Reverb, Delay, Distortion, Compressor, and Crossfeed), EBU R128 volume normalization, a redesigned 10-band equalizer with custom presets and import/export, a rebuilt AVAudioEngine streaming engine with improved format support (including FLAC and Ogg Vorbis), faster and more accurate CarPlay and Now Playing, Liquid Glass design updates, refreshed Home Screen widgets, and bug and localization fixes.
{{% /details %}}

{{% details title="Does Evermusic have true gapless playback?" closed="true" %}}
Yes. Starting with Evermusic 8.7, playback is truly gapless: there is no pause, click, or tick between tracks. The engine pre-buffers and decodes the next track while the current one plays and hands off between audio samples on a continuous ring buffer, so the transition is inaudible. It works for local files, cloud streams, and media servers, and it is ideal for live albums, DJ mixes, and concept albums.
{{% /details %}}

{{% details title="What audio effects does Evermusic 8.7 include?" closed="true" %}}
Five real-time effects: **Reverb** (13 room presets, wet/dry mix), **Delay/Echo** (10 presets with delay time, feedback, low-pass, and mix), **Distortion** (22 character presets with pre-gain and mix), **Compressor** (a full dynamics processor with threshold, ratio, attack, release, expansion, and makeup gain, plus 10 presets), and **Crossfeed** (Bauer bs2b headphone crossfeed with level and cutoff controls and 6 presets). Each effect ships with curated presets, and your custom settings are remembered between sessions.
{{% /details %}}

{{% details title="What is Crossfeed and why would I use it?" closed="true" %}}
Crossfeed mixes a small, filtered amount of each stereo channel into the other, the way your ears naturally hear real loudspeakers in a room. On headphones this reduces the exaggerated, "in-your-head" separation of hard-panned recordings and makes long listening more comfortable. Evermusic uses the well-known Bauer stereophonic-to-binaural (bs2b) algorithm and includes presets such as Chu Moy and Jan Meier. It is especially effective on older 1960s and 1970s stereo mixes.
{{% /details %}}

{{% details title="How does volume normalization work in Evermusic?" closed="true" %}}
Evermusic 8.7 measures each track's perceived loudness using the EBU R128 standard (ITU-R BS.1770) in real time and gently adjusts the level toward a consistent target so tracks do not jump in volume. It does not require ReplayGain tags and does not alter your files. Four presets are available — Light (−20 LUFS), Standard (−16 LUFS), Strong (−14 LUFS), and Night (−23 LUFS) — and normalization resets cleanly when you seek or change tracks.
{{% /details %}}

{{% details title="Is Evermusic's volume normalization the same as ReplayGain?" closed="true" %}}
It achieves the same goal — consistent loudness between tracks — but works differently. ReplayGain relies on loudness tags stored inside your files. Evermusic's normalizer measures loudness live using EBU R128, so it works on any source, including cloud streams and internet radio, even when the files have no tags at all.
{{% /details %}}

{{% details title="How many bands does the Evermusic equalizer have, and can I make my own presets?" closed="true" %}}
The Evermusic equalizer is a 10-band graphic equalizer covering 32 Hz to 16 kHz, with each band adjustable from −12 dB to +12 dB in 0.1 dB steps and a preamp from −24 dB to +24 dB. It includes built-in presets, lets you create and save custom presets, and supports importing and exporting presets as .eqp files so you can move or share them between devices.
{{% /details %}}

{{% details title="What changed in the Evermusic 8.7 equalizer?" closed="true" %}}
The equalizer was redesigned with new, more precise sliders that adopt the iOS 26 system slider and Liquid Glass look, faster and smoother preset switching, and a better layout in landscape and on iPad (a horizontal preset bar in portrait and a vertical preset column in landscape). Custom presets and .eqp import/export are supported.
{{% /details %}}

{{% details title="Does Evermusic 8.7 support FLAC and Ogg Vorbis?" closed="true" %}}
Yes. The rebuilt engine plays FLAC (via Core Audio) and Ogg Vorbis (via libvorbisfile), along with MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF, and more, from local files, cloud drives, and media servers.
{{% /details %}}

{{% details title="What improved in CarPlay and on the Lock Screen?" closed="true" %}}
CarPlay album artwork loads several times faster on long lists and now appears in the compact iOS 26 list rows that previously showed none. Now Playing information on the Lock Screen and in CarPlay is more accurate — the title, elapsed time, duration, and play/pause state are captured together so they can't disagree, and buffering states are reported correctly. Remote controls (play, pause, next, previous, seek, shuffle, repeat, rate) respond reliably from headphones and the car, and CarPlay sorting on large libraries is faster.
{{% /details %}}

{{% details title="Do the audio effects and equalizer work with cloud streaming and CarPlay?" closed="true" %}}
Yes. The effects, equalizer, and volume normalization run natively inside the playback engine, so they apply to everything Evermusic plays — local files, cloud drives, media servers, and internet radio — and they continue to work during CarPlay playback and, where supported, over AirPlay and Chromecast.
{{% /details %}}

{{% details title="Is Evermusic 8.7 free to update, and which devices does it support?" closed="true" %}}
Yes. Evermusic is a free download from the App Store, and 8.7 is a free update for existing users, with optional in-app upgrades for advanced features. It runs on iPhone, iPad, and Mac. CarPlay requires a CarPlay-compatible vehicle or head unit.
{{% /details %}}
