---
title: "How to Use Audio Sound Effects and DSP in Flacbox: BASS Engine, Bass Boost, Equalizer, Compressor, Freeverb, Crossfeed, and Volume Normalization"
date: 2026-07-24
description: "A complete technical guide to Flacbox audio on iPhone, iPad, and Mac. How the BASS playback engine works, which formats it adds beyond the standard iOS codecs (including MOD and tracker music and DSD), and how to use every real-time effect, the 10-band equalizer, and the custom DSP signal chain, with all presets and parameters."
keywords: ["Flacbox audio effects", "Flacbox BASS engine", "BASS audio library iOS", "MOD music player iPhone", "tracker music player iOS", "play MOD XM IT S3M iPhone", "DSD player iOS", "FLAC player iPhone", "lossless music player iOS", "Flacbox equalizer", "10 band equalizer iPhone", "volume normalization iPhone", "EBU R128 iOS", "loudness normalization music player", "crossfeed headphones iOS", "bs2b crossfeed", "compressor music player iOS", "freeverb reverb iOS", "DSP chain music player", "bass boost iPhone", "how to add effects to music Flacbox"]
tags: ["Flacbox", "Audio Effects", "How To", "BASS", "Equalizer", "Bass Boost", "Compressor", "Freeverb", "Crossfeed", "Volume Normalization", "EBU R128", "MOD Music", "Tracker Music", "DSD", "FLAC", "DSP", "Headphones"]
readingTime: 14
aliases:
  - /post/how-to-use-audio-sound-effects-and-dsp-in-flacbox-bass-engine-equalizer-crossfeed-volume-normalization/
---

{{< author-byline >}}

**TL;DR:** Flacbox plays audio through the **BASS engine**, a high performance native audio library. On top of decoding **FLAC, DSD, WavPack, Monkey's Audio (APE), Musepack, TrueAudio, Opus** and, importantly, **MOD and tracker module music (MOD, XM, IT, S3M, MTM, UMX, MO3)** that the standard iOS players do not handle, BASS gives Flacbox a full real time effects rack. You get a **10-band equalizer**, **Volume Normalization (EBU R128 loudness)**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed**, and a reorderable **DSP "Signal processing" chain** with 14 building blocks (filters, bass boost shelves, bit crusher, ring modulator, tremolo, stereo width, and more). Open them from **Settings > Audio player > Audio effects / Audio equalizer / Signal processing**, or from the player's **⋯ (More) menu > Audio effects**. Every effect is independent, applies in real time to any source, and never modifies your files.

## What Makes Flacbox Different: the BASS Engine

Most iPhone and iPad music apps rely only on the system audio stack (AVFoundation and Core Audio). Flacbox adds a second, more capable playback path built on the **BASS audio library** from un4seen. This is what lets Flacbox play formats that the built in iOS decoders skip, and it is what powers the whole effects rack described below.

When you play a track through the BASS engine, Flacbox:

1. Opens the file as a decoded stream (`BASS_StreamCreateFile`), or, if the file is a music module, loads it through the dedicated **module engine** (`BASS_MusicLoad`).
2. Wraps the stream in a tempo and pitch processor so speed and pitch can change without artifacts.
3. Runs the signal through the effects and the custom DSP chain.
4. Levels the loudness, applies crossfeed for headphones, and sends the result to the output.

Because all of this happens in real time on the audio stream, nothing is ever written back to your files. Turn an effect off and the original sound returns instantly.

## Audio Formats: What BASS Adds (Including MOD and Tracker Music)

Flacbox's BASS engine supports the standard system codecs plus a large set of extra formats through BASS add on plugins. The single most distinctive addition is **module (tracker) music**, which is not ordinary sampled audio at all. A module file stores instrument samples plus a pattern score, and the BASS module engine plays it back by **synthesizing the song live** from those patterns, the way the format was originally designed to be played. General media decoders treat audio as a flat PCM stem and cannot reproduce this.

| Family | Formats and extensions | How Flacbox plays it |
|---|---|---|
| **Module / tracker music** | MOD, XM, IT, S3M, MTM, UMX, MO3 | BASS built in module engine (`BASS_MusicLoad`) with sensitive ramping and length pre scan |
| **Lossless (modern)** | FLAC (.flac, .fla) | bassflac plugin |
| **Lossless (other)** | WavPack (.wv), Monkey's Audio (.ape), TrueAudio (.tta), Musepack (.mpc) | basswv, bassape, bass_tta, bass_mpc |
| **High resolution DSD** | DSD (.dsf, .dff) | bassdsd plugin, with DSD over PCM (DoP) support |
| **Lossy** | MP3, MP2, MP1, Ogg Vorbis, Opus (.opus) | Core BASS and bassopus |
| **MIDI** | MIDI (.mid, .midi, .kar) | bassmidi with SoundFont synthesis |
| **Container and streaming** | WebM audio, HLS streams | basswebm, basshls |
| **System codecs** | AAC, ALAC, M4A, M4B, MP4 audio, CAF, AIFF, WAV, AC3 | Core Audio on iOS, iPadOS, and macOS |

Tracker formats load through `BASS_MusicLoad` with **sensitive ramping** (smooths abrupt sample transitions in old modules) and a **pre scan** that computes the true length before playback. DSD files can play through **DSD over PCM (DoP)** so they work on standard output hardware.

> Why this matters for you: if you keep a collection of demoscene modules, chiptunes, or Amiga era MOD and XM files, Flacbox plays them natively alongside your FLAC and DSD library, with the same effects and equalizer available on top.

## The Flacbox Signal Chain, in Order

Every enabled stage processes the audio in sequence. Each one is bypassed (zero cost) when it is switched off:

1. **Source decode** (file stream or module engine)
2. **Tempo and pitch** wrapper (independent speed and pitch, plus the reverse mode)
3. **10-band Equalizer** (parametric peaking bands)
4. **Compressor**
5. **Freeverb** (reverb / space)
6. **Auto Wah**
7. **Phaser**
8. **Flanger**
9. **Echo**
10. **Chorus**
11. **Distortion**
12. **Rotate**
13. **Custom DSP chain** ("Signal processing": your own ordered list of filters and effects)
14. **Volume Normalization** (EBU R128 loudness leveling)
15. **Crossfeed** (headphone imaging)
16. **Output** (with configurable sample rate, channel count, and IO buffer)

All of the effects and the equalizer run on the same live stream, so they apply to local files, cloud drives, media servers, network streams, and module music alike, and they keep working during CarPlay and background playback.

## Where to Find Everything (Menus)

Flacbox groups its audio tools into three screens, all under the audio player settings.

**Audio effects (the effects rack):**

- From the player: open **Now Playing**, tap the **⋯ (More)** button, tap **Audio effects**.
- From settings: **Settings > Audio player > Audio effects**.

**Audio equalizer (10 bands, presets, import/export):**

- **Settings > Audio player > Audio equalizer**.

**Signal processing (the custom DSP chain):**

- **Settings > Audio player > Signal processing**.

You can also change the audio **output sample rate**, **number of channels**, and **preferred IO buffer duration** from **Settings > Audio player**.

## How Each Effect Editor Works

Every effect in the Audio effects list follows the same pattern, so once you learn one you know them all:

- **On/Off switch.** Each effect has its own switch. There is no master switch, so you can run one, several, or all of them at once. Every effect is off by default, and its controls are dimmed until you turn it on.
- **Presets.** A row of one tap presets gives you a good starting sound immediately. The current preset name is shown next to the effect.
- **Advanced sliders.** Open the parameters to fine tune. As soon as you move any slider, the effect switches to a **Manual** state, so you always know when you have moved away from a preset. Each slider has a reset control to return it to its default.

Changes save automatically and take effect in real time.

## The 10-Band Equalizer

**What it does:** Shapes the overall tone, from deep sub bass to high treble "air". This is the tool to use for a clean **bass boost**, a treble lift, or a full genre curve.

**How it is built:** Ten parametric peaking bands centered at **32, 64, 125, 250, 500 Hz and 1, 2, 4, 8, 16 kHz**. Each band ranges from **-12 dB to +12 dB** in 0.1 dB steps, with a global **preamp from -24 dB to +24 dB** to compensate for large boosts.

**Built in presets (22):** Acoustic, Bass Booster, Bass Reducer, Classical, Dance, Deep, Electronic, Flat, Hip-Hop, Jazz, Latin, Loudness, Lounge, Piano, Pop, R&B, Rock, Small Speakers, Spoken Word, Treble Booster, Treble Reducer, and Vocal Booster.

You can also create and save your own presets, reorder them, and **export or import** them to move your settings between devices.

**How to use it:** Pick a preset close to your taste, then nudge individual bands. For a bass boost without muddiness, lift **32 and 64 Hz** a few dB and pull the preamp down 1 to 2 dB so nothing clips.

## Volume Normalization (EBU R128 Loudness)

**What it does:** Some tracks are mastered much louder than others, so you keep reaching for the volume. Volume Normalization measures each track's real perceived loudness and gently levels it toward a consistent target, so a shuffled playlist that mixes decades and sources plays at about the same volume.

**How it is built:** It uses the broadcast grade **EBU R128** loudness model (measured in **LUFS**, the same standard streaming services use), not simple peak levels and not file tags. Flacbox measures integrated loudness in real time (and pre scans the track loudness when it can), then applies a gain correction toward your target, capped by a maximum boost so quiet recordings are not over amplified. Because it reads the actual audio, it works on any source and needs no loudness tags in your files.

**Parameters:**

| Parameter | Range | Default | Meaning |
|---|---|---|---|
| Target loudness | -30 to -6 LUFS | -16 LUFS | The loudness every track is leveled toward. Higher is louder overall. |
| Max boost | 0 to 24 dB | 12 dB | Limit on how much a quiet track can be amplified. |

**Presets:**

| Preset | Target | Max boost | Best for |
|---|---|---|---|
| Light | -20 LUFS | 6 dB | Gentle leveling, conservative |
| Standard | -16 LUFS | 12 dB | Streaming style loudness (default) |
| Strong | -14 LUFS | 18 dB | Aggressive matching for very mixed libraries |
| Night | -23 LUFS | 15 dB | Quieter, consistent late night listening |

**How to use it:** Turn it on and choose **Standard** for everyday listening, or **Night** for quiet, even late evening playback. It pairs especially well with the Compressor for in car and noisy environments.

## Compressor

**What it does:** Within a single song, quiet parts can be too soft and loud parts too loud. The Compressor pulls them closer together so the whole track stays easy to hear.

**How it is built:** A dB based dynamics processor (BASS `COMPRESSOR2`). It exposes the classic controls below.

**Parameters:**

| Parameter | Range | Default | Meaning |
|---|---|---|---|
| Threshold | -60 to 0 dB | -20 dB | The level where compression starts. Lower squashes more. |
| Ratio | 1:1 to 30:1 | 4:1 | How hard levels above the threshold are reduced. |
| Attack | 0.1 to 1000 ms | 10 ms | How fast it reacts to a loud peak. |
| Release | 10 ms to 5 s | 100 ms | How fast it lets go after the loud part passes. |
| Master gain | -30 to +30 dB | 0 dB | Makeup gain applied after compression. |

**Presets (10):** Transparent, Soft, Standard, Heavy, Voice / Podcast, Old Recordings, Late Night, Movie Dialog, Streaming Match, and Maximum Loudness.

**How to use it:** For most listening, turn it on and pick **Standard**. Use **Voice / Podcast** or **Movie Dialog** for spoken content, **Late Night** for quiet rooms, or **Maximum Loudness** for the loudest, most even result.

## Freeverb (Reverb)

**What it does:** Adds a sense of real space, from a small room up to a large hall or cathedral.

**How it is built:** The well known **Freeverb** algorithm (BASS `FREEVERB`), which sounds noticeably cleaner than legacy reverbs and exposes true reverb controls.

**Parameters:**

| Parameter | Range | Default | Meaning |
|---|---|---|---|
| Dry mix | 0 to 1 | 0.0 | Level of the original (dry) sound. |
| Wet mix | 0 to 3 | 1.0 | Level of the reverb (wet) sound. |
| Room size | 0 to 1 | 0.5 | Length of the reverb tail. |
| Damp | 0 to 1 | 0.5 | High frequency damping of the tail. |
| Width | 0 to 1 | 1.0 | Stereo width of the reverb. |

**Presets (6):** Room, Studio, Hall, Cathedral, Plate, and Ambience.

**How to use it:** Pick a space and keep the wet mix modest. A little adds air to close mic'd or dry recordings; a lot places the music far away.

## Auto Wah

**What it does:** A resonant filter that sweeps up and down on its own for a funky, vocal like "wah" motion.

**How it is built:** BASS `AUTOWAH`, an LFO swept resonant filter.

**Parameters:** Wet mix (-2 to +2, default 1.5), Feedback (-1 to +1, default 0.5), Rate (0.1 to 9 Hz, default 2.0), Range (0.1 to 9 octaves, default 4.3), Frequency (1 to 1000 Hz, default 50).

**Presets (6):** Classic Wah, Slow Sweep, Funky, Deep, Subtle, and Resonant.

## Phaser

**What it does:** A sweeping filter that adds a swirling, whooshing motion to the sound.

**How it is built:** BASS `PHASER`, a swept notch and comb filter.

**Parameters:** Feedback (-1 to +1, default 0.0), Rate (0.1 to 9 Hz, default 1.0), Range (0.1 to 9 octaves, default 4.0), Frequency (1 to 1000 Hz, default 100).

**Presets (6):** Classic, Slow, Fast, Deep, Subtle, and Jet.

## Flanger

**What it does:** A short, moving delay that gives a jet like sweeping whoosh.

**How it is built:** BASS DX8 `FLANGER`, a modulated comb filter.

**Parameters:** Depth (0 to 100%, default 25), Feedback (-99 to +99%, default -50), Rate (0 to 10 Hz, default 0.25), Delay (0 to 4 ms, default 2.0).

**Presets (6):** Classic, Subtle, Deep, Jet, Fast, and Wide.

## Echo

**What it does:** Repeats the sound as fading echoes for a sense of space and depth, from a tight slapback to a long, spacious tail.

**How it is built:** BASS `ECHO4`, a modern echo with signed feedback and an optional ping pong (stereo) mode.

**Parameters:** Wet mix (-2 to +2, default 0.6), Feedback (-1 to +1, default 0.5), Delay (0.01 to 2 s, default 0.4), plus a stereo/ping pong option carried by the preset.

**Presets (6):** Slapback, Room, Tape, Dub, Ping-Pong, and Long.

## Chorus

**What it does:** Thickens and widens the sound by layering a shifting copy over the original.

**How it is built:** BASS DX8 `CHORUS`, a modulated short delay.

**Parameters:** Wet/dry mix (0 to 100%, default 50), Depth (0 to 100%, default 25), Feedback (-99 to +99%, default 25), Rate (0 to 10 Hz, default 1.1).

**Presets (6):** Subtle, Lush, Ensemble, Vibrato, Wide, and 12-String.

## Distortion

**What it does:** Adds grit and edge by overdriving the sound, from a warm drive to full fuzz.

**How it is built:** BASS DX8 `DISTORTION`, a waveshaper with a built in post EQ, so you shape both the drive and its tone.

**Parameters:** Drive/Edge (0 to 100%, default 15), Output gain (-60 to 0 dB, default -18), EQ Center (100 to 8000 Hz, default 2400), EQ Width (100 to 8000 Hz, default 2400), Tone / pre low pass (100 to 8000 Hz, default 8000).

**Presets (7):** Warm Drive, Crunch, Overdrive, Fuzz, Metal, Screamer, and Lo-Fi.

**How to use it:** This is a creative, for fun effect. Keep the output modest and drive to taste.

## Rotate

**What it does:** Spins the sound around the stereo field for a rotary, swirling auto pan.

**How it is built:** BASS `ROTATE`, a rotary auto panner.

**Parameters:** Rate (-5 to +5 Hz, default 1.0). Negative values reverse the spin direction.

**Presets (6):** Slow Pan, Sway, Rotary, Fast Spin, Reverse, and Whirl.

## Crossfeed (for Headphones)

**What it does:** On headphones, the left and right channels stay completely separate, which can make music feel stuck inside your head, especially on hard panned older stereo mixes. Crossfeed blends a small, filtered amount of each channel into the other, the way your ears naturally hear speakers in a room, so the sound feels more natural and less tiring on long listens.

**How it is built:** The well known **Bauer stereophonic-to-binaural (bs2b)** algorithm, the same implementation the standard engine uses, run here as a BASS DSP stage. It exposes the two classic bs2b controls.

**Parameters:**

| Parameter | Range | Default | Meaning |
|---|---|---|---|
| Cutoff | 300 to 2000 Hz | 700 Hz | Where the bleed between channels rolls off. Lower is warmer and more pronounced. |
| Feed level | 1 to 15 dB | 4.5 dB | How much of one channel bleeds into the other. Higher is more speaker like. |

**Presets (6):** Subtle, Chu Moy, Strong, Jan Meier, Speaker-like, and Vintage Stereo.

**How to use it:** This is a headphones effect, so leave it off for speakers. Try **Chu Moy** or **Jan Meier** (both audiophile favorites), or **Vintage Stereo** for hard panned 1960s and 1970s recordings.

## Signal Processing: the Custom DSP Chain

Beyond the fixed effects rack, Flacbox includes a fully **reorderable DSP chain** under **Settings > Audio player > Signal processing**. This is a studio style rack: add the blocks you want, in any order, duplicate them, enable or disable each one, and target **all channels, left only, or right only**. The chain processes the audio as raw floating point samples, so each block is applied in the exact order you place it, front to back.

Add effects with the **+** button, drag to reorder, and use the **⋯** on each block to duplicate or delete it.

**Filters and tone (biquad based):**

| Block | Key parameters (range, default) | Built in presets |
|---|---|---|
| **Low Pass** | Cutoff 20 Hz to 20 kHz (20 kHz), Q 0.1 to 10 (0.707) | Air, Warm, Mellow, Muffled, Telephone |
| **High Pass** | Cutoff 20 Hz to 20 kHz (20 Hz), Q 0.1 to 10 (0.707) | Rumble cut, Tighten, Thin, Radio, Telephone |
| **Band Pass** | Center 20 Hz to 20 kHz (1 kHz), Q 0.1 to 10 (0.707) | Voice, Bass, Body, Presence, Telephone, Wah |
| **Notch** | Frequency 20 Hz to 20 kHz (60 Hz), Q 0.1 to 10 (8.0) | Hum 60 Hz, Hum 50 Hz, Rumble, Mud, Boxy, Harsh |
| **Peaking (parametric EQ)** | Frequency 20 Hz to 20 kHz (1 kHz), Gain -15 to +15 dB, Q 0.1 to 10 (1.0) | Presence, Warmth, Vocal boost, Cut mud, Tame harsh, Punch, Sub boost, Air, Clarity, De-ess, De-boom, Scoop |
| **Low Shelf (bass control / bass boost)** | Frequency 20 to 2000 Hz (200 Hz), Gain -15 to +15 dB | Warmth, Bass boost, Fullness, Trim bass, Cut lows, Big bottom |
| **High Shelf (treble control)** | Frequency 1 to 20 kHz (8 kHz), Gain -15 to +15 dB | Presence, Air, Bright, Soften, Tame highs, Sparkle |

**Level, drive, and creative blocks:**

| Block | Key parameters (range, default) | Built in presets |
|---|---|---|
| **Gain** | -24 to +24 dB (0) | Cut, Trim, Unity, Lift, Boost, Max |
| **Soft Clip** | Drive 0 to 40 dB (0), tanh saturation | Warm, Drive, Crunch, Fuzz, Destroy |
| **Bit Crusher** | Bit depth 1 to 16 bits (16), Sample rate ratio 0.01 to 1.0 (1.0) | Vintage, Lo-Fi, Crunch, Gritty, Destroy |
| **Ring Modulator** | Carrier 1 to 4000 Hz (440), Mix 0 to 1 (0) | Tremolo, Robot, Metallic, Bell, Alien |
| **Tremolo** | Rate 0.1 to 20 Hz (5), Depth 0 to 1 (0) | Gentle, Classic, Deep, Fast, Chop |
| **Delay** | Time 0.01 to 2 s (0.25), Feedback 0 to 0.95 (0.4), Mix 0 to 1 (0) | Slapback, Echo, Ping, Ambient, Dub, Cavern |
| **Stereo Width** | Width 0 to 2 (1.0): 0 is mono, 1 is normal, 2 is extra wide | Wide, Wider, Max, Narrow, Focused, Mono |

**How to use it:** For a clean **bass boost**, add a **Low Shelf** set around 80 to 120 Hz with a few dB of gain, then add a **Gain** block trimmed 1 to 2 dB to keep headroom. For a lo-fi character, chain **Bit Crusher** into **Soft Clip**. For a wider mix on headphones, add **Stereo Width** and pair it with Crossfeed.

## How It Is All Built (Implementation Notes)

- **Engine:** the un4seen **BASS** library, with format add ons (bassflac, bassdsd, basswv, bassape, bass_mpc, bass_tta, bassopus, bassmidi, basswebm, basshls) loaded at startup, plus the **bass_fx** effects library for the tempo, pitch, and DSP effects.
- **Effects:** the equalizer uses BASS parametric peaking bands. The Compressor, Auto Wah, Phaser, Echo, and Rotate use the modern bass_fx effects; Freeverb uses the Freeverb algorithm; Chorus, Flanger, and Distortion use the DX8 effect set with their native parameter ranges.
- **Volume Normalization** is a real time **EBU R128 (LUFS)** loudness leveler, the broadcast and streaming loudness standard, with a per track loudness pre scan feeding a gain stage.
- **Crossfeed** is the vendored **libbs2b** (Bauer) crossfeed, attached as a BASS DSP stage.
- **Custom DSP chain** processes interleaved floating point audio through your ordered list of nodes, with per node enable and a left / right / all channel target.
- **Output** is configurable: sample rate, channel count, and preferred IO buffer duration.

Because every stage runs live on the playback stream, the effects:

- Apply in **real time** to everything you play, including module music, cloud streams, and network sources.
- **Never modify or re-encode** your files. Turn an effect off and the original returns.
- **Remember your settings** between sessions, per effect.
- Can be **combined freely**, since each one is independent.

## Tips

- **Start with a preset**, then fine tune only if you want to.
- For a **bass boost**, prefer the equalizer's low bands or a DSP **Low Shelf**, and pull the preamp or a Gain block down slightly so nothing clips.
- **Crossfeed is for headphones**, not speakers.
- **Volume Normalization plus Compressor** gives the most consistent, easy to hear result for mixed playlists and in car listening.
- Keep **Reverb, Echo, and Distortion** mixes modest for musical results.
- The **DSP chain order matters**. A filter before a distortion sounds different from the same filter after it.

## FAQ

{{% details title="What audio engine does Flacbox use?" closed="true" %}}
Flacbox plays audio through the BASS engine from un4seen, a high performance native audio library, alongside the system audio stack. BASS is what lets Flacbox decode extra formats (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, and MOD or tracker music) and run its full real time effects rack, equalizer, and DSP chain.
{{% /details %}}

{{% details title="Can Flacbox play MOD, XM, IT, and other tracker or module music?" closed="true" %}}
Yes. The BASS engine includes a built in module player that loads MOD, XM, IT, S3M, MTM, UMX, and MO3 files and synthesizes them live from their patterns and instrument samples, the way tracker music is meant to be played. Standard iOS players cannot do this. Effects and the equalizer work on module music too.
{{% /details %}}

{{% details title="Does Flacbox support DSD and high resolution files?" closed="true" %}}
Yes. Flacbox plays DSD files (.dsf and .dff) through the BASS DSD plugin, including DSD over PCM (DoP) for standard output hardware, plus FLAC, WavPack, Monkey's Audio (APE), Musepack, and TrueAudio for lossless playback.
{{% /details %}}

{{% details title="Which audio effects does Flacbox have?" closed="true" %}}
A 10-band equalizer, Volume Normalization (EBU R128 loudness), Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate, and Crossfeed, plus a reorderable DSP "Signal processing" chain with filters, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay, and stereo width. Each effect is independent and can be combined with the others.
{{% /details %}}

{{% details title="How do I open the audio effects in Flacbox?" closed="true" %}}
Open the Now Playing player, tap the ⋯ (More) button, and choose Audio effects. You can also go to Settings > Audio player > Audio effects. Tap an effect, turn its switch on, and pick a preset, or open the sliders to fine tune.
{{% /details %}}

{{% details title="Where is the equalizer?" closed="true" %}}
Go to Settings > Audio player > Audio equalizer. It is a 10-band equalizer (32 Hz to 16 kHz), each band adjustable from -12 to +12 dB, with a -24 to +24 dB preamp and 22 built in presets. You can create, save, reorder, and export or import your own presets.
{{% /details %}}

{{% details title="How do I boost the bass in Flacbox?" closed="true" %}}
Two good options. In the Audio equalizer, raise the 32 Hz and 64 Hz bands a few dB and choose the Bass Booster preset as a starting point. Or, in Signal processing, add a Low Shelf block around 80 to 120 Hz with a few dB of gain. In both cases, trim the preamp or add a Gain block 1 to 2 dB lower so the low end does not clip.
{{% /details %}}

{{% details title="What is Volume Normalization and how is it different from ReplayGain?" closed="true" %}}
Volume Normalization measures each track's real perceived loudness using the EBU R128 standard (in LUFS, the same measure streaming services use) and levels it toward a target, capped by a maximum boost. Unlike ReplayGain, it does not need loudness tags in your files and reads the actual audio in real time, so it works on any source. Presets: Light, Standard, Strong, and Night.
{{% /details %}}

{{% details title="What is Crossfeed and should I use it?" closed="true" %}}
Crossfeed blends a small, filtered amount of each stereo channel into the other so headphones sound more like real speakers, reducing the in your head feeling of hard panned mixes. It is a headphones effect, so leave it off for speakers. Flacbox uses the Bauer stereophonic-to-binaural (bs2b) algorithm, with presets like Chu Moy and Jan Meier.
{{% /details %}}

{{% details title="What is the Signal processing (DSP) chain?" closed="true" %}}
It is a reorderable rack of DSP building blocks under Settings > Audio player > Signal processing. Add filters (low/high/band pass, notch, peaking, low/high shelf), gain, soft clip, bit crusher, ring modulator, tremolo, delay, and stereo width in any order, duplicate or disable each one, and target all channels, left, or right. Because order matters, you can design exactly the processing you want.
{{% /details %}}

{{% details title="What is the difference between the Equalizer, the effects, and the DSP chain?" closed="true" %}}
The Equalizer is a fixed 10-band tone control. The Audio effects are ready made processors (compressor, reverb, echo, and so on) with presets. The Signal processing DSP chain is a build your own rack where you place and order individual blocks yourself. They can all run at the same time.
{{% /details %}}

{{% details title="Do the effects change or damage my audio files?" closed="true" %}}
No. All effects, the equalizer, and the DSP chain are applied in real time during playback only. They never modify or re-encode your files. Turn an effect off and your original sound returns instantly.
{{% /details %}}

{{% details title="Can I use more than one effect at the same time?" closed="true" %}}
Yes. Every effect has its own on/off switch and there is no master switch, so you can enable any combination. For example, Volume Normalization plus Compressor for consistent listening, or Freeverb plus Crossfeed on headphones, with the equalizer and a DSP chain on top.
{{% /details %}}

{{% details title="Why are the effect controls greyed out?" closed="true" %}}
The effect is turned off. Turn on the effect's switch at the top of its editor to activate the controls. Every effect is off by default.
{{% /details %}}

{{% details title="What does the Manual label mean on an effect?" closed="true" %}}
It means you have moved a slider away from a preset, so the effect is now using your custom values instead of a named preset. Every slider has a reset control to return it to its default, and picking a preset again replaces your manual values.
{{% /details %}}

{{% details title="Does the equalizer let me save and share presets?" closed="true" %}}
Yes. Besides the 22 built in presets, you can create your own, reorder them, and export or import presets to move your settings between devices.
{{% /details %}}

{{% details title="Do the effects work with CarPlay, background playback, and streaming?" closed="true" %}}
Yes. The effects run inside the BASS playback engine, so they apply to local files, cloud drives, media servers, network streams, and module music, and they keep working during CarPlay and background playback.
{{% /details %}}

{{% details title="Can I change the audio output quality?" closed="true" %}}
Yes. Under Settings > Audio player you can set the output sample rate, the number of output channels, and the preferred IO buffer duration to match your hardware and latency needs.
{{% /details %}}

{{% details title="What is the best starting setup for everyday listening on headphones?" closed="true" %}}
Turn on Volume Normalization (Standard), add a light Compressor (Standard or Soft), pick an equalizer preset you like, and enable Crossfeed (Chu Moy or Jan Meier). Keep reverb, echo, and distortion off unless you want a creative sound.
{{% /details %}}
