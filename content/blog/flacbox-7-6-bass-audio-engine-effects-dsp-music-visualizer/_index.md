---
title: "Flacbox 7.6: New BASS Audio Engine, Effects, DSP, and a Live Music Visualizer"
date: 2026-07-23T00:00:00+02:00
description: "Flacbox 7.6 for iPhone, iPad, and Mac adds a professional BASS audio engine for lossless and hi-res playback, automatic loudness-based volume leveling, an eleven-effect studio suite (reverb, delay, multi-tap echo, chorus, flanger, phaser, auto-wah, distortion, compressor, stereo rotation, crossfeed), a 14-filter DSP processor, a full-screen real-time music visualizer, tracker and MOD music playback (MOD, XM, IT, S3M, MTM, UMX, MO3), a refreshed effects and equalizer design, and CarPlay improvements."
keywords: ["Flacbox 7.6", "Flacbox update", "BASS audio engine iPhone", "lossless music player iOS", "hi-res audio player iPhone 2026", "FLAC player iPhone", "DSD player iOS", "ALAC player iPhone", "APE player iOS", "MOD player iPhone", "tracker music player iOS", "play XM IT S3M on iPhone", "real-time audio effects iOS", "reverb delay chorus flanger phaser iPhone", "auto-wah distortion compressor iOS", "crossfeed headphones iOS", "stereo rotation audio effect", "DSP processor music player iPhone", "parametric EQ filters iOS", "bit crusher ring modulator iOS", "music visualizer iPhone", "real-time audio visualizer iOS", "volume normalization iPhone", "loudness leveling music player", "pitch and tempo control iOS", "CarPlay hi-res audio player", "cloud music player iOS 2026"]
tags: ["Flacbox", "Flacbox 7.6", "BASS Audio Engine", "Audio Effects", "DSP", "Music Visualizer", "Volume Leveling", "Loudness Normalization", "Reverb", "Delay", "Chorus", "Flanger", "Phaser", "Auto-Wah", "Distortion", "Compressor", "Crossfeed", "Tracker Music", "MOD", "Equalizer", "FLAC", "DSD", "ALAC", "APE", "CarPlay", "Hi-Res Audio", "What's New"]
aliases:
  - /post/flacbox-7-6-bass-audio-engine-effects-dsp-music-visualizer/
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**TL;DR:** [Flacbox 7.6](/products/flacbox) is our biggest update yet for the iPhone, iPad, and Mac hi-res audio player, and it is built around a brand-new **BASS™ audio engine** for lossless and high-resolution listening. You can select the BASS™ engine as an alternative playback core to unlock a full chain of **real-time audio effects**, a **14-filter DSP processor**, a **live full-screen music visualizer**, and playback of classic **tracker and MOD music** (MOD, XM, IT, S3M, MTM, UMX, MO3). The update also adds **automatic loudness-based volume leveling**, an **eleven-effect studio suite** (reverb, delay, multi-tap echo, chorus, flanger, phaser, auto-wah, distortion, compressor, stereo rotation, and crossfeed), a **refreshed effects and equalizer design** with modern glass-style sliders, and **CarPlay improvements** including DSP settings in the car and more accurate lock-screen, watch, and car controls. Under the hood: a more reliable streaming foundation, better file-type handling, broader localization, and many stability and performance fixes.

---

## Hi everyone!

Flacbox 7.6 is available to download, and this is our biggest update yet. It is built around a brand-new **BASS™ audio engine** for lossless and high-resolution listening — a professional playback core you can choose as an alternative to the existing engine. Selecting it unlocks a full chain of real-time audio effects, DSP processing, and live visualization, and it even adds playback of classic tracker and MOD music. Your music now sounds great *and* looks great.

[Download Flacbox 7.6 from the App Store](https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8) or update from your existing version. Mac users can grab the [desktop version here](https://apps.apple.com/app/apple-store/id1594027432?pt=95781850&ct=everappzcom&mt=8). Flacbox is a free download with optional in-app upgrades for advanced features.

## New BASS™ Audio Engine

The headline of Flacbox 7.6 is a **new [BASS™](https://www.un4seen.com) audio engine** — a professional playback core, built on the acclaimed **BASS™** audio library from [un4seen Developments](https://www.un4seen.com), that you can select as an alternative to the existing engine. Keep the classic engine when you want it, or switch to BASS™ when you want the full audiophile toolkit. The choice is yours, per your preference, and switching is a single setting.

Choosing the BASS™ engine unlocks everything this release is about:

- **A full chain of real-time audio effects** — stack studio-style processors and hear the change instantly (see the [effects suite](#new-audio-effects-suite) below).
- **A real-time DSP processor** — build your own signal chain from [14 filters](#new-dsp-processor).
- **Live visualization** — full-screen animated visuals that react to your music in real time.
- **Tracker and MOD music playback** — play classic module formats: **MOD, XM, IT, S3M, MTM, UMX, and MO3**. These are the chiptune and demoscene formats that store patterns and samples instead of a rendered waveform, and Flacbox now plays them natively.
- **High-quality resampling** — your existing lossless library is played back with clean, high-quality sample-rate conversion.
- **Precise, independent pitch and tempo control** — shift the key by up to **±60 semitones** *or* change the speed from **0.1× to 4×** without affecting the other, ideal for practice, transcription, and DJ-style listening.

Because Flacbox is a **hi-res and lossless player**, the BASS™ engine plays your **FLAC, DSD, ALAC, APE, WAV, AIFF, MP3, AAC, and Opus** files with the same fidelity you expect — and now with a real-time processing chain sitting on top of it.

## Automatic Volume Leveling

Ever built a playlist where one album blasts and the next is a whisper? Flacbox 7.6 fixes that with **automatic volume leveling**. It uses **loudness-based normalization** built on the **EBU R128** standard (the same ITU-R BS.1770 loudness measurement used in broadcast and by streaming services) to measure each track's real perceived loudness in **LUFS** and gently steer it toward a consistent target — so you are not constantly reaching for the volume control between songs.

For your **local files, Flacbox pre-scans your library** so playback opens already leveled — there is no waiting for the app to "catch up" to the right loudness after a track starts. The result is a smooth, even listening level across mixed libraries, compilations, and shuffle sessions.

Four presets cover the common cases:

- **Light** — gentle leveling (target −20 LUFS, up to +6 dB of lift).
- **Standard** — the default, streaming-style loudness (target −16 LUFS, up to +12 dB of lift for quiet tracks).
- **Strong** — aggressive matching for very mixed libraries (target −14 LUFS, up to +18 dB).
- **Night** — quieter and consistent for low-volume evening listening (target −23 LUFS).

## <a id="new-audio-effects-suite"></a>New Audio Effects Suite

Flacbox 7.6 adds a suite of **eleven real-time audio effects** that you can stack and tune while the music plays. Each effect runs live inside the BASS™ engine, so it applies to everything you listen to without re-encoding your files. Every effect has **its own dedicated screen, a library of presets, and an instant on/off toggle**, so you can audition a sound in one tap and switch it off just as fast.

- **Reverb** — add a sense of space, from a tight room to a large hall.
- **Delay** — a classic echo with adjustable time and feedback.
- **Multi-tap echo** — layered, rhythmic repeats for a richer echo than a single delay line.
- **Chorus** — thickens and widens a sound by blending slightly detuned copies.
- **Flanger** — the sweeping, jet-plane "whoosh" made by a modulated short delay.
- **Phaser** — a smooth, swirling movement across the frequency spectrum.
- **Auto-wah** — an envelope-driven filter sweep that reacts to the music's dynamics.
- **Distortion** — from subtle warmth and grit to full lo-fi character.
- **Compressor** — evens out loud and quiet passages for a more controlled, upfront sound.
- **Stereo rotation** — moves the sound around the stereo field for a spacious, moving image.
- **Crossfeed** — mixes a little of each channel into the other so hard-panned recordings sound **more natural on headphones**, closer to how you hear real speakers in a room.

Adjust any control and Flacbox remembers your settings, so your sound comes back exactly as you left it.

## <a id="new-dsp-processor"></a>New DSP Processor

For listeners who want to go deeper, Flacbox 7.6 introduces a **real-time DSP processor** that lets you **build your own signal chain from 14 filters**. Combine them in any order to correct a room, tame harsh recordings, or sculpt a completely custom tone. As with the effects, each filter has **presets and an instant on/off toggle**.

The 14 real-time DSP filters are:

1. **Gain** — level trim for the chain.
2. **Low-pass filter** — cuts the highs above a chosen frequency.
3. **High-pass filter** — cuts the lows below a chosen frequency.
4. **Band-pass filter** — keeps a band and removes the rest.
5. **Notch filter** — surgically removes a narrow problem frequency.
6. **Peaking EQ** — boost or cut a bell-shaped band.
7. **Low-shelf EQ** — shape everything below a frequency (bass control).
8. **High-shelf EQ** — shape everything above a frequency (treble control).
9. **Soft-clip saturation** — gentle, musical warmth and loudness.
10. **Bit crusher** — deliberate lo-fi, retro digital character.
11. **Tremolo** — rhythmic volume modulation.
12. **Delay** — a DSP-level echo you can place anywhere in the chain.
13. **Ring modulator** — metallic, bell-like, experimental textures.
14. **Stereo width** — narrow or widen the stereo image.

Together with the [10-band equalizer](#refreshed-design) and the [effects suite](#new-audio-effects-suite), the DSP processor turns Flacbox into a genuine **mobile audio workstation** for your lossless library.

## Real-Time Music Visualizer

Flacbox 7.6 adds a **real-time music visualizer**: full-screen animated visuals that react live to your music. Choose from a **large library of presets**, or let them cycle automatically for an ever-changing show. It is available **across the playback engines on all your devices**, and a built-in **screen-sleep preventer** keeps the display awake so the visuals never cut out mid-song.

It is a great fit for a phone or iPad propped up at a party, an iPad on a desk, or a Mac on a big screen — your music now looks as good as it sounds.

## <a id="refreshed-design"></a>Refreshed Design

The parts of Flacbox you touch most while shaping your sound have been redesigned:

- **Redesigned audio effects and equalizer screens** with **modern sliders** and **glass-style visuals** that feel right at home on today's iOS, iPadOS, and macOS.
- **A simplified presets mode** so you can get a great sound fast, without digging through every control.
- **Clearer organization of engines, effects, and DSP** — it is now easier to see which playback engine you are on and which processors are active.

## CarPlay Improvements

Listening on the road gets better in 7.6:

- **DSP settings on CarPlay** — reach your DSP configuration safely from the car's display.
- **Fixed artwork and Now Playing** — album art and the Now Playing screen render correctly.
- **More accurate lock-screen, watch, and car controls** — title, artwork, and playback state stay in sync across the Lock Screen, Apple Watch, and your car controls.

## Other Improvements

- **A more reliable streaming foundation** — steadier playback from cloud drives, media servers, and network shares.
- **Better file-type handling** — smoother recognition and playback across your mixed-format library.
- **Broader localization** — more of the app, in more languages.
- **Many stability and performance fixes** — based on your emails and App Store reviews.

## Why This Update Matters

Flacbox 7.6 is built around one idea: **your lossless library deserves a professional-grade playback experience — and it should look as good as it sounds.**

1. **A pro engine you can choose.** The new BASS™ audio engine sits alongside the classic one, so you can switch to a full audiophile toolkit whenever you want it and keep things simple when you don't.
2. **A studio in your pocket.** Eleven real-time effects, a 14-filter DSP processor, a redesigned equalizer, and automatic volume leveling give you real control over your sound — not just an on/off switch.
3. **New music to explore.** Native **tracker and MOD** playback opens up decades of chiptune and demoscene music that most iPhone players simply cannot play.
4. **See your music, everywhere.** The real-time visualizer works across engines and devices, with the screen kept awake so the show goes on.

## Get Flacbox 7.6

[**Download Flacbox from the App Store**](https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8) or update from inside the App Store. Mac users can get the [desktop version here](https://apps.apple.com/app/apple-store/id1594027432?pt=95781850&ct=everappzcom&mt=8). Flacbox is a free download with optional in-app upgrades for advanced features.

Thank you for using Flacbox. Your music now sounds great and looks great, with a professional-grade engine, a full suite of effects and DSP filters, and a live visualizer to match. If you enjoy the app, please leave a rating on the App Store — it genuinely helps. Have feedback or run into an issue? Email us at **support@everappz.com**. We read every message.

## Frequently Asked Questions

{{% details title="What's new in Flacbox 7.6?" closed="true" %}}
Flacbox 7.6 adds a new professional **BASS™ audio engine** you can select as an alternative playback core, **automatic loudness-based volume leveling**, an **eleven-effect studio suite** (reverb, delay, multi-tap echo, chorus, flanger, phaser, auto-wah, distortion, compressor, stereo rotation, and crossfeed), a **14-filter real-time DSP processor**, a **full-screen real-time music visualizer**, native **tracker and MOD** playback (MOD, XM, IT, S3M, MTM, UMX, MO3), a **refreshed effects and equalizer design**, and **CarPlay improvements**. It also includes a more reliable streaming foundation, better file-type handling, broader localization, and many stability and performance fixes.
{{% /details %}}

{{% details title="What is the new BASS™ audio engine in Flacbox?" closed="true" %}}
The [BASS™](https://www.un4seen.com) audio engine, built on the BASS™ audio library from un4seen Developments, is a professional playback core you can choose as an **alternative to Flacbox's existing engine**. Selecting it unlocks a full chain of real-time audio effects, a DSP processor, and live visualization, and it adds playback of classic tracker and MOD music. It plays your existing lossless and hi-res library (FLAC, DSD, ALAC, APE, and more) with **high-quality resampling** and **precise pitch and tempo control**. You can switch back to the classic engine at any time.
{{% /details %}}

{{% details title="Which audio formats and tracker/MOD types does Flacbox 7.6 play?" closed="true" %}}
Flacbox remains a hi-res and lossless player, handling **FLAC, DSD, APE, ALAC, WAV, AIFF, MP3, AAC, Opus**, and more. New in 7.6, the BASS™ engine also plays classic **tracker and module music**: **MOD, XM, IT, S3M, MTM, UMX, and MO3** — the pattern-and-sample formats used in chiptune and demoscene music that most iPhone players can't open.
{{% /details %}}

{{% details title="How does automatic volume leveling work in Flacbox?" closed="true" %}}
Flacbox 7.6 uses **EBU R128 loudness measurement** (the ITU-R BS.1770 standard) to keep tracks from different albums at a consistent perceived volume, so you don't have to adjust the volume between songs. For **local files, your library is pre-scanned** so playback opens already leveled — there's no delay while the app measures loudness after a track starts. Four presets are available — **Light** (−20 LUFS), **Standard** (−16 LUFS), **Strong** (−14 LUFS), and **Night** (−23 LUFS) — and it works across mixed libraries, compilations, and shuffle sessions.
{{% /details %}}

{{% details title="What audio effects are in Flacbox 7.6?" closed="true" %}}
Eleven real-time effects you can stack and tune while the music plays: **reverb, delay, multi-tap echo, chorus, flanger, phaser, auto-wah, distortion, compressor, stereo rotation, and crossfeed**. Each effect has its **own screen, a library of presets, and an instant on/off toggle**, and Flacbox remembers your settings between sessions. Crossfeed in particular makes hard-panned recordings sound more natural on headphones.
{{% /details %}}

{{% details title="What is the DSP processor and which filters does it include?" closed="true" %}}
The DSP processor lets you **build your own real-time signal chain from 14 filters**: gain, low-pass, high-pass, band-pass and notch filters, peaking EQ, low-shelf and high-shelf EQ, soft-clip saturation, bit crusher, tremolo, delay, ring modulator, and stereo width. Each filter has **presets and an instant on/off toggle**, so you can correct a room, tame harsh recordings, or design a completely custom tone.
{{% /details %}}

{{% details title="What is crossfeed and why would I use it on headphones?" closed="true" %}}
Crossfeed mixes a small, filtered amount of each stereo channel into the other, the way your ears naturally hear real loudspeakers in a room. On headphones this reduces the exaggerated, "in-your-head" separation of hard-panned recordings and makes long listening more comfortable. It's especially effective on older 1960s and 1970s stereo mixes.
{{% /details %}}

{{% details title="Does the Flacbox music visualizer work on all devices?" closed="true" %}}
Yes. The **real-time music visualizer** shows full-screen animated visuals that react live to your music, with a large library of presets you can pick from or let cycle automatically. It's **available across the playback engines on all your devices**, and a built-in **screen-sleep preventer** keeps the display awake so the visuals don't cut out during a song.
{{% /details %}}

{{% details title="Can I change pitch and tempo without affecting the other?" closed="true" %}}
Yes. When you use the new BASS™ engine, Flacbox 7.6 offers **precise, independent pitch and tempo control** — change a track's speed without changing its key, or shift the key without changing the speed. It's useful for practice, transcription, and DJ-style listening.
{{% /details %}}

{{% details title="What improved in CarPlay in Flacbox 7.6?" closed="true" %}}
CarPlay now includes **DSP settings** so you can reach your configuration from the car, **fixed album artwork and Now Playing** rendering, and **more accurate lock-screen, Apple Watch, and car controls** that stay in sync with playback. Combined with the more reliable streaming foundation, listening to your lossless library on the road is smoother.
{{% /details %}}

{{% details title="Do the effects, DSP, and equalizer work with cloud streaming?" closed="true" %}}
Yes. The effects, DSP filters, equalizer, and volume leveling run in real time inside the BASS™ playback engine, so they apply to everything Flacbox plays — **local files, cloud drives (iCloud Drive, Google Drive, Dropbox, OneDrive, and more), media servers, and network shares** — with no re-encoding of your files.
{{% /details %}}

{{% details title="Is Flacbox 7.6 a free update, and which devices does it support?" closed="true" %}}
Yes. Flacbox is a **free download** from the App Store, and 7.6 is a **free update** for existing users, with optional in-app upgrades for advanced features. It runs on **iPhone, iPad, and Mac**. CarPlay requires a CarPlay-compatible vehicle or head unit.
{{% /details %}}
