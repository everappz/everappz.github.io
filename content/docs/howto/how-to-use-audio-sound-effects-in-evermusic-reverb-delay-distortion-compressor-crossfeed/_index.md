---
title: "How to Use the Audio Sound Effects in Evermusic: Reverb, Delay, Distortion, Compressor, Crossfeed, and Volume Normalization"
date: 2026-07-05
description: "A complete guide to Evermusic's real-time audio effects on iPhone, iPad, and Mac. Learn what Reverb, Delay, Distortion, Compressor, Crossfeed, and Volume Normalization do, how they are built, and how to enable, preset, and fine-tune each one."
keywords: ["Evermusic audio effects", "music player sound effects iPhone", "reverb music player iOS", "delay echo effect iPhone", "distortion audio effect iOS", "compressor music player iPhone", "crossfeed headphones iOS", "volume normalization iPhone", "loudness normalization music player", "EBU R128 iOS", "how to add reverb to music iPhone", "audio effects music player iOS 2026", "DSP effects music player iPhone"]
tags: ["Evermusic", "Audio Effects", "How To", "Reverb", "Delay", "Distortion", "Compressor", "Crossfeed", "Volume Normalization", "EBU R128", "Equalizer", "Headphones"]
readingTime: 8
aliases:
  - /post/how-to-use-audio-sound-effects-in-evermusic-reverb-delay-distortion-compressor-crossfeed/
---

{{< author-byline >}}

**TL;DR:** Evermusic includes six real-time audio effects — **Volume Normalization, Compressor, Reverb, Crossfeed, Delay, and Distortion**. Open them from the player's **⋯ (More) menu > Audio effects**, or from **Settings > Audio player > Audio effects**. Tap an effect, turn its switch **ON** (top-right), pick a **preset**, and optionally open **Advanced mode** to fine-tune the sliders. Each effect works independently and applies in real time to everything you play — local files, cloud streams, and internet radio — with no re-encoding.

## What Are the Evermusic Audio Effects?

Audio effects change the character of your sound as it plays. Evermusic runs them as **native, real-time processing nodes** inside its playback engine, so they apply to every source — local files, cloud drives, media servers, and internet radio — without ever modifying or re-encoding your files. Turn an effect off and your original sound returns instantly.

There are six effects, and each one is **independent** — there is no single master switch, so you can run one, several, or all of them at once:

1. **Volume Normalization** — keeps every track at a consistent loudness.
2. **Compressor** — evens out the loud and quiet parts within a track.
3. **Reverb** — adds a sense of space, from a small room to a cathedral.
4. **Crossfeed** — makes headphones sound more like real speakers.
5. **Delay** — adds an echo, from a tight slap to a long ambient tail.
6. **Distortion** — adds grit and lo-fi character, for fun.

Volume Normalization and Compressor are about **consistency and clarity**. Reverb, Delay, and Distortion are **creative effects**. Crossfeed is a **headphone comfort** tool. Together they turn Evermusic into a small studio in your pocket.

## How to Open the Audio Effects

There are two ways to reach the Audio effects screen.

**From the player (fastest):**

1. Open the **Now Playing / player** screen.
2. Tap the **⋯ (More)** button.
3. Tap **Audio effects**.

**From Settings:**

1. Go to the **Settings** tab.
2. Tap **Audio player**.
3. Tap **Audio effects**.

Either way, you land on the **Audio effects** list, which shows all six effects in this order: **Volume normalization, Compressor, Reverb, Crossfeed, Delay, Distortion**. Tap any one to open its editor.

## How Each Effect Editor Works

Every effect editor follows the same simple pattern, so once you learn one you know them all:

- **Enable switch (top-right).** Turn the effect **ON** or **OFF**. Every effect is off by default. When it is off, the controls are dimmed.
- **Simple / Advanced toggle (top-right).** *Simple* mode shows just a list of presets with plain-language descriptions — the easiest way to get a good sound in one tap. *Advanced* mode adds fine-tuning sliders.
- **Preset picker.** A row of preset "bubbles" in portrait, or a preset column in landscape. Pick a starting point, then adjust if you like.
- **Sliders (Advanced mode).** Each slider shows its current value and has a small **reset** button (a circular arrow) to return it to the default. Adjusting any slider switches the effect to a **Manual** state, so you always know when you have moved away from a preset.

Changes save automatically. Below is what each effect does and how to set it up.

## Volume Normalization

**What it does:** Some songs are mastered louder than others, so you keep reaching for the volume. Volume Normalization measures each track's real perceived loudness and gently levels it toward a consistent target, so everything plays at about the same volume. It uses the broadcast-grade **EBU R128** loudness standard (ITU-R BS.1770), works in real time on any source, and — unlike ReplayGain — needs **no loudness tags in your files** and never alters the audio.

**Presets:** Light, Standard, Strong, and Night.

**Advanced controls:**

- **Target loudness** — the loudness every track is leveled toward, shown in LUFS. Higher (for example, −14 LUFS) makes everything play louder overall; lower (−23 LUFS) is quieter and calmer.
- **Max boost** — limits how much a quiet track can be amplified, in dB. Higher values bring soft recordings closer to the target.

**How to use it:** Turn it on and choose **Standard** for streaming-style loudness, or **Night** for consistent, quiet late-evening listening. Great for shuffled playlists that mix old and new recordings.

## Compressor

**What it does:** Within a single song, quiet parts can be too soft and loud parts too loud. The Compressor pulls them closer together so the whole track is easy to hear — in the car, on a run, or anywhere noisy. It is a full dynamics processor built on Apple's `AUDynamicsProcessor`.

**Presets:** Transparent, Soft, Standard, Heavy, Voice / Podcast, Old Recordings, Late Night, Movie Dialog, Streaming Match, and Maximum Loudness.

**Advanced controls (seven sliders):**

- **Threshold** — the level where compression starts. Lower squashes more.
- **Headroom** — space above the threshold before hard limiting engages.
- **Expansion ratio** — how strongly very quiet sounds (like background noise) are pulled down.
- **Expansion threshold** — the level below which that gating begins.
- **Attack** — how fast the effect reacts to a sudden loud peak.
- **Release** — how fast it lets go after the loud part passes.
- **Master gain** — final makeup boost applied after processing.

**How to use it:** For most listening, turn it on and pick **Standard**. Choose **Voice / Podcast** or **Movie Dialog** for spoken content, **Late Night** for quiet listening, or **Maximum Loudness** for the loudest, most even result.

## Reverb

**What it does:** Makes music sound like it is playing in a real space, with a natural tail of echo — from an intimate room to a grand hall or cathedral. Built on Apple's `AVAudioUnitReverb`.

**Presets (13):** Small Room, Medium Room, Large Room, Medium Hall, Large Hall, Plate, Medium Chamber, Large Chamber, Cathedral, and several hall and room variations.

**Advanced control:**

- **Mix** — how much reverb to blend in, from 0% (dry, original sound) to 100% (fully into the chosen space).

**How to use it:** Turn it on, pick a space (for example, **Medium Hall** for a warm, roomy feel), and keep the **Mix** modest — a little goes a long way. Use it to add air to close-mic'd or "dry" recordings.

## Crossfeed

**What it does:** On headphones, the left and right channels stay completely separate, which can make music feel stuck inside your head — especially on hard-panned older stereo mixes. Crossfeed blends a small, filtered amount of each channel into the other, the way your ears naturally hear speakers in a room, so the sound feels more natural and less tiring on long listens. It is built on the well-known **Bauer stereophonic-to-binaural (bs2b)** algorithm.

**Presets (6):** Subtle, Chu Moy, Strong, Jan Meier, Speaker-like, and Vintage Stereo.

**Advanced controls:**

- **Cutoff** — where the bleed between channels begins to roll off. Lower values give a warmer, more pronounced effect.
- **Feed level** — how much of one channel bleeds into the other. Higher values sound more speaker-like.

**How to use it:** This is a **headphones** effect — leave it off for speakers. Turn it on and try **Chu Moy** or **Jan Meier** (both audiophile favorites), or **Vintage Stereo** for hard-panned 1960s and 1970s recordings.

## Delay (Echo)

**What it does:** Repeats the sound like an echo in the mountains. A little makes music feel fuller; more leaves a clear, rhythmic echo after each note. Built on Apple's `AVAudioUnitDelay`.

**Presets (10):** Slapback, Doubler, Short Echo, Standard, Tape Echo, Bright Echo, Long Echo, Dub, Spacious, and Ambient.

**Advanced controls:**

- **Delay time** — the pause between the original sound and its echo. Short is a tight slap; long is a clear repeat.
- **Feedback** — how many times the echo repeats before fading.
- **Tone** — filters brightness out of the echo for a warmer, tape-like sound.
- **Mix** — how much echo to blend in.

**How to use it:** Turn it on and start with **Slapback** or **Tape Echo** for subtle depth, or **Ambient** and **Dub** for long, spacious tails.

## Distortion

**What it does:** Makes music sound rough and gritty, like a broken speaker or a lo-fi transmission. It is a creative, for-fun effect rather than a fidelity tool, so use it sparingly. Built on Apple's `AVAudioUnitDistortion`.

**Presets (22):** including Bit Brush, Broken Speaker, Cellphone Concert, Radio Tower, Alien Chatter, Cosmic Interference, and many more.

**Advanced controls:**

- **Pre-gain** — how hard the signal drives the distortion. Higher is more aggressive.
- **Mix** — how much distortion to blend with the clean sound.

**How to use it:** Turn it on, pick a character preset, and keep the **Mix** low unless you want a heavily broken sound. Fun on electronic and experimental tracks.

## How the Effects Are Built

Evermusic's effects run inside a modern **AVAudioEngine** processing chain. Each effect is a native audio node placed in the signal path, and it is only active when you switch it on — otherwise it is bypassed with zero cost. Reverb, Delay, and Distortion use Apple's built-in audio units (`AVAudioUnitReverb`, `AVAudioUnitDelay`, `AVAudioUnitDistortion`); the Compressor uses Apple's `AUDynamicsProcessor`; Crossfeed is a custom node based on the open-source **bs2b** algorithm; and Volume Normalization is a real-time **EBU R128** loudness node.

Because the effects are part of the playback engine itself, they:

- Apply in **real time** to everything you play, including cloud streams and live radio.
- **Never modify or re-encode** your files — turn an effect off and the original sound returns.
- **Remember your settings** between sessions, per effect.
- Can be combined freely, since each one is independent.

They also work alongside Evermusic's **10-band graphic equalizer** and its **gapless playback**, so you can shape the tone, level the loudness, and keep transitions seamless all at once.

## Tips

- **Start in Simple mode.** Pick a preset first; only open Advanced mode when you want to fine-tune.
- **Less is more** for Reverb, Delay, and Distortion — keep the Mix modest for musical results.
- **Crossfeed is for headphones**, not speakers.
- **Volume Normalization + Compressor** together give the most consistent, easy-to-hear result for mixed playlists and in-car listening.
- Every slider has a **reset** button if you want to return to its default.

## FAQ

{{% details title="How do I add reverb, delay, or other effects to my music in Evermusic?" closed="true" %}}
Open the player, tap the ⋯ (More) button, and choose Audio effects (or go to Settings > Audio player > Audio effects). Tap the effect you want, turn its switch ON at the top-right, and pick a preset. Open Advanced mode to fine-tune the sliders. The effect applies immediately to whatever is playing.
{{% /details %}}

{{% details title="What audio effects does Evermusic have?" closed="true" %}}
Six real-time effects: Volume Normalization (EBU R128 loudness leveling), Compressor (dynamics), Reverb (space and echo tail), Crossfeed (natural headphone imaging), Delay (echo), and Distortion (lo-fi grit). Each is independent and can be used alone or combined.
{{% /details %}}

{{% details title="Do the effects change or damage my audio files?" closed="true" %}}
No. All effects are applied in real time during playback only. They never modify or re-encode your files. Turn an effect off and your original sound returns instantly.
{{% /details %}}

{{% details title="Can I use more than one effect at the same time?" closed="true" %}}
Yes. Every effect is independent — there is no master switch — so you can enable any combination. For example, Volume Normalization plus Compressor for consistent, easy listening, or Reverb plus Crossfeed on headphones.
{{% /details %}}

{{% details title="What is Crossfeed and should I use it?" closed="true" %}}
Crossfeed blends a small, filtered amount of each stereo channel into the other so headphones sound more like real speakers, reducing the "in-your-head" feeling of hard-panned mixes. It is a headphone effect (leave it off for speakers). It is built on the Bauer stereophonic-to-binaural (bs2b) algorithm and includes presets like Chu Moy and Jan Meier.
{{% /details %}}

{{% details title="What is Volume Normalization and how is it different from ReplayGain?" closed="true" %}}
Volume Normalization keeps every track at a consistent loudness by measuring perceived loudness with the EBU R128 standard and leveling toward a target. Unlike ReplayGain, it does not need loudness tags in your files and does not alter the audio — it works live on any source, including cloud streams and internet radio. Presets: Light, Standard, Strong, and Night.
{{% /details %}}

{{% details title="What is the difference between Simple and Advanced mode?" closed="true" %}}
Simple mode shows a list of presets with plain descriptions, so you can get a good sound in one tap. Advanced mode adds the parameter sliders (for example, Mix for Reverb, or the seven Compressor controls) for precise fine-tuning. Toggle between them with the mode button at the top-right of each effect editor.
{{% /details %}}

{{% details title="Why are the effect controls greyed out?" closed="true" %}}
The effect is turned off. Turn on the effect's switch at the top-right of its editor to activate the controls. Every effect is off by default.
{{% /details %}}

{{% details title="Do the effects work with streaming and CarPlay?" closed="true" %}}
Yes. The effects run inside the playback engine, so they apply to local files, cloud drives, media servers, and internet radio, and they keep working during CarPlay playback.
{{% /details %}}
