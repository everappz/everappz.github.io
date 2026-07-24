---
title: "How to Use Sound Effects and DSP in Flacbox: Compressor, Freeverb, Crossfeed, Echo, Volume Normalization, and more"
date: 2026-07-24
description: "The complete guide to Flacbox audio on iPhone, iPad, and Mac. Learn how the BASS engine works, which extra formats it plays (including MOD and tracker music and DSD), and exactly what every effect, every slider, and every preset does to your sound, plus the 10-band equalizer and the custom DSP chain."
keywords: ["Flacbox audio effects", "Flacbox presets explained", "Flacbox BASS engine", "BASS audio library iOS", "MOD music player iPhone", "tracker music player iOS", "play MOD XM IT S3M iPhone", "DSD player iOS", "FLAC player iPhone", "lossless music player iOS", "Flacbox equalizer presets", "10 band equalizer iPhone", "volume normalization iPhone", "EBU R128 iOS", "loudness normalization music player", "crossfeed headphones iOS", "bs2b crossfeed", "compressor presets music player", "freeverb reverb iOS", "echo delay music player", "DSP chain music player", "bass boost iPhone", "how to add effects to music Flacbox", "best equalizer settings iPhone"]
tags: ["Flacbox", "Audio Effects", "How To", "BASS", "Equalizer", "Bass Boost", "Compressor", "Freeverb", "Crossfeed", "Echo", "Volume Normalization", "EBU R128", "MOD Music", "Tracker Music", "DSD", "FLAC", "DSP", "Headphones", "Presets"]
readingTime: 30
---

{{< author-byline >}}

**Short answer:** In Flacbox you choose one **Playback engine** in **Settings > Audio player**: **Standard** (Apple's system engine), **Universal** (the FFmpeg engine), or **Sound FX** (the **BASS™ engine**). The engine you pick decides which file formats play, so the choice matters. The **Sound FX** engine plays extra formats that most iPhone apps skip (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, and old **MOD and tracker music** like MOD, XM, IT, and S3M), and it is the only engine that powers the sound tools: a **10-band equalizer**, **Volume Normalization**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed**, and a build-your-own **DSP chain**. So to use the effects in this guide, set your Playback engine to **Sound FX** first. Each tool has ready-made **presets**. Open them in **Settings > Audio player** (Audio effects, Audio equalizer, Signal processing), or tap the **⋯ (More)** button on the player and choose **Audio effects**. Nothing you do here ever changes your files.

> The slider and preset explanations below are the same short descriptions Flacbox shows you inside the app, blended with a little extra background so you get the full picture before you tap.

## How to Read This Guide

Every tool works the same way:

1. **Turn it on.** Each effect has its own on/off switch. They are all off at first. You can turn on as many as you like at the same time.
2. **Pick a preset.** A preset is a ready-made setting. Tap one and the sound changes right away. This guide lists what **every** preset does.
3. **Fine-tune (optional).** Open the sliders to adjust by hand. The moment you move a slider, the effect shows **Manual**, so you know you have left the preset. Every slider has a reset button.

Nothing is saved into your files. These are live effects. Turn an effect off and your original sound comes back at once.

## Choose Your Playback Engine (Sound FX Has the Effects)

Flacbox does not blend engines together. You pick **one** in **Settings > Audio player > Playback engine**, and the engine you choose decides which file formats you can play and whether the effects are available. There are three choices, shown in the app under these exact names:

1. **Standard.** Apple's built-in system engine. Uses hardware decoding for lower battery use.
2. **Universal.** The FFmpeg engine, which opens a very wide range of formats.
3. **Sound FX.** The **BASS™ engine**. It plays lossless and high-resolution files with full accuracy, adds module (tracker) music, and powers every effect, the 10-band equalizer, and the DSP chain in this guide.

Because each engine supports its own set of formats, the files you can play change with the engine you select. More importantly, the effects, equalizer, and DSP chain work **only** with the **Sound FX** engine, so choose it first if you want to use them.

Sound FX is built on **BASS™**, a professional audio library from Un4seen Developments. You can read more about it on its home page at [un4seen.com](https://www.un4seen.com/).

## Music Formats: What the Sound FX (BASS™) Engine Adds (Including MOD and Tracker Music)

With the **Sound FX (BASS™)** engine selected, Flacbox plays the specialist formats below, on top of the everyday ones. The most special is **module music**, also called **tracker music**. A module file is not a normal recording. It holds small instrument sounds plus a "score" that says how to play them, and Flacbox rebuilds the song live from that score, the way these files were meant to be played. Normal players cannot do this.

| Type of music | Formats | Good to know |
|---|---|---|
| **Module / tracker music** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Rebuilt live by the BASS™ module player. Great for chiptunes and old demoscene or Amiga songs. |
| **Modern lossless** | FLAC | Full quality, smaller than WAV. |
| **Other lossless** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Less common lossless types, all supported. |
| **High-resolution DSD** | DSF, DFF | Plays on normal hardware using DSD over PCM. |
| **Modern lossy** | Opus, Ogg Vorbis, MP3 | The usual streaming and download types. |

The Sound FX engine also plays the mainstream Apple formats (AAC, ALAC, M4A, WAV, AIFF) and live streams, so the effects and equalizer work on those too.

**Why this helps you:** if you have a mix of FLAC albums, DSD high-resolution files, and a folder of old MOD or XM tracker songs, Flacbox plays them all, and the equalizer and effects work on every one of them.

## The Three Menus You Will Use

Flacbox keeps its sound tools in three places, all inside the audio player settings. First make sure your **Playback engine** is set to **Sound FX** (Settings > Audio player > Playback engine), because the effects, equalizer, and DSP chain are available only with that engine.

- **Audio effects** (the effects rack): open the player, tap **⋯ (More)**, tap **Audio effects**. Or go to **Settings > Audio player > Audio effects**.
- **Audio equalizer** (10 bands and presets): **Settings > Audio player > Audio equalizer**.
- **Signal processing** (your own DSP chain): **Settings > Audio player > Signal processing**.

You can also set the **output sample rate**, **channels**, and **buffer size** under **Settings > Audio player**.

## The 10-Band Equalizer

**What it does:** Changes the tone of the music, from deep bass to bright treble. This is the best tool for a clean **bass boost** or a brighter, clearer top end. Think of it as ten volume knobs, each for a different slice of the sound. Raise a band to bring that part forward, lower it to pull it back. Small changes of a few dB usually sound best, and it works on everything you play.

**How it works:** Ten sliders at **32, 64, 125, 250, 500 Hz and 1, 2, 4, 8, 16 kHz**. Each goes from **-12 dB (cut)** to **+12 dB (boost)**. There is also a **Preamplifier** from **-24 to +24 dB** for overall level. You can save your own presets and **export or import** them between devices.

**What each built-in preset does (22 presets):**

| Preset | What it does to your sound |
|---|---|
| **Flat** | No change. All bands at zero. A clean starting point. |
| **Acoustic** | Warm bass and crisp, present highs. Makes acoustic guitars and voices feel natural and lively. |
| **Bass Booster** | Strong lift in the low end, mids and highs untouched. More punch and weight. |
| **Bass Reducer** | Cuts the low end. Handy for boomy rooms, cheap earbuds, or heavy tracks. |
| **Treble Booster** | Lifts only the highs. Adds sparkle and air, more detail. |
| **Treble Reducer** | Softens the highs. Tames harsh or sharp recordings. |
| **Classical** | Full lows and gentle highs with a slight mid dip. Smooth and roomy for orchestral music. |
| **Dance** | Big lows and bright highs with scooped mids. Punchy and energetic for club tracks. |
| **Deep** | Warm, thick low end with softer highs. A cozy, laid-back sound. |
| **Electronic** | Strong bass and bright highs for synths and beats. Wide and modern. |
| **Hip-Hop** | Heavy bass and clear highs with controlled mids. Weighty and punchy. |
| **Jazz** | Warm and smooth, with a small mid dip. Easy and natural for acoustic jazz. |
| **Latin** | Boosted lows and highs with clean mids. Bright and lively. |
| **Loudness** | Boosts bass and treble strongly (a "smile" curve). Sounds fuller at low volume. |
| **Lounge** | Forward mids with soft edges. Relaxed and vocal-friendly. |
| **Piano** | Clear mids and highs so piano notes ring out cleanly. |
| **Pop** | Lifted mids for vocals, with lows and highs pulled back. Voices sit up front. |
| **R&B** | Very strong low-mid warmth and clear highs. Smooth and rich. |
| **Rock** | Boosted lows and highs for guitars and drums. Energetic and full. |
| **Small Speakers** | Boosts lows and cuts highs to help tiny speakers sound fuller. |
| **Spoken Word** | Lifts the voice range and cuts the deep bass. Makes talking clear. |
| **Vocal Booster** | Pushes the middle where voices live, cuts around them. Vocals stand out. |

**Tip for bass:** Start with **Bass Booster**, then, if it sounds muddy, pull the Preamplifier down 1 to 2 dB so nothing distorts.

## Volume Normalization (Even Loudness)

**What it does:** Some songs play louder than others, so you keep changing the volume. This makes every song play at about the same volume by itself, so you do not have to. It is perfect for shuffled playlists that mix old and new recordings, different albums, or different sources, where one track can be much louder than the next.

**How it works:** It listens to the real loudness of each track using the **EBU R128** standard (measured in **LUFS**, the same idea streaming services use), then adjusts each track toward your target. It needs no tags in your files and never changes the audio. EBU R128 measures the loudness your ears actually feel across the whole song, not just the highest peak, which is why it matches how loud tracks really seem to you. Flacbox works this out live as the music plays (and checks the loudness ahead of time when it can), then applies a single, steady volume change to the track. The **Max boost** limit stops very quiet recordings from being pushed up so hard that they distort. Because it reads the sound itself, it works on any source, including cloud files, live streams, and module music, even when the files have no loudness tags at all.

**Sliders:**

| Control | What it does | Range (default) |
|---|---|---|
| **Target loudness** | Sets the loudness every track is leveled toward. Higher values make everything play louder overall. | -30 to -6 LUFS (-16) |
| **Max boost** | Limits how much quiet tracks can be amplified. Higher values bring soft recordings closer to the target. | 0 to 24 dB (12) |

**Presets:**

| Preset | What it does |
|---|---|
| **Light** | Gentle leveling for casual listening. Evens out obvious volume jumps without pushing quiet tracks hard. |
| **Standard** | The all-purpose default. A streaming-style loudness target that suits most music. Start here. |
| **Strong** | Aggressive matching that pushes quiet tracks up firmly. Best for mixed libraries with big level differences. |
| **Night** | A quieter overall target that still lifts soft passages, so late-night listening stays consistent and low. |

## Compressor (Even Out Loud and Quiet Parts)

**What it does:** In one song, the quiet parts can be too soft and the loud parts too loud. This brings them closer together, so the whole song is easy to hear, even in the car or a noisy place. It gently turns the loudest moments down and lifts the softer ones, so you stop reaching for the volume during a single track. This is different from Volume Normalization: the Compressor evens things out **inside** one song, while Volume Normalization matches loudness **between** songs. The two work well together. Start with a preset, and only open the sliders if you want more control.

**Sliders:**

| Control | What it does | Range (default) |
|---|---|---|
| **Threshold** | The level where compression starts. Lower values squash more of the sound, keeping quiet and loud parts closer together. | -60 to 0 dB (-20) |
| **Ratio** | How strongly the loud parts are held back once they pass the threshold. Higher values compress harder, keeping the sound more even. | 1:1 to 30:1 (4:1) |
| **Attack** | How fast the effect responds to a sudden loud peak. Short values catch transients; longer ones let them through. | 0.1 to 1000 ms (10 ms) |
| **Release** | How fast the effect lets go after the loud part passes. Short values can pump; longer ones sound smoother. | 10 ms to 5 s (100 ms) |
| **Master gain** | Final output boost applied after processing. Raise this to lift overall loudness once the dynamics are evened out. | -30 to +30 dB (0) |

**Presets:**

| Preset | What it does |
|---|---|
| **Transparent** | Barely-there safety net. Preserves dynamics almost entirely and only catches the loudest peaks. |
| **Soft** | Light leveling for hi-fi listening at home. Subtle smoothing without squashing the music. |
| **Standard** | Sensible default for everyday music playback. The first preset to try. |
| **Heavy** | Aggressive evening for noisy environments. Car, crowded room, low-volume listening. |
| **Voice / Podcast** | Speech-tuned. Slower attack lets sibilants through, generous makeup gain pulls vocals up. |
| **Old Recordings** | Vintage albums and restored vinyl, where average level is below modern releases. |
| **Late Night** | Heavy compression plus big boost for quiet listening when neighbours or sleeping family matter. |
| **Movie Dialog** | Brings spoken word up against music and sound effects in a varied soundtrack. |
| **Streaming Match** | Targets approximately the loudness normalization of modern streaming services around -14 LUFS. |
| **Maximum Loudness** | All-in. Hits the limiter; expect a squashed, very level signal. The literal max-volume preset. |

## Freeverb (Reverb, a Sense of Space)

**What it does:** Adds a sense of space to the music, from a small room up to a big hall. Pick a preset, or fine-tune the dry and wet mix, room size, damping and width yourself. Reverb is the natural echo you hear in any real space, and Freeverb recreates it in software. A little makes flat or close-mic'd recordings feel more open and alive. A lot places the music in a large, distant space. It is a creative effect, so keep the wet mix modest for natural results.

**Sliders:**

| Control | What it does | Range (default) |
|---|---|---|
| **Dry mix** | How much of the original, untouched sound is kept. Higher values leave more of the dry signal in the mix. | 0 to 1 (0.0) |
| **Wet mix** | How much of the reverberated sound is added. Higher values make the reverb louder and more obvious. | 0 to 3 (1.0) |
| **Room size** | The size of the imagined space. Higher values give a longer, bigger reverb tail, from a small room up to a cathedral. | 0 to 1 (0.5) |
| **Damp** | How quickly the high frequencies fade in the tail. Higher values make the reverb darker and warmer. | 0 to 1 (0.5) |
| **Width** | The stereo spread of the reverb. Higher values make the space feel wider between the left and right channels. | 0 to 1 (1.0) |

**Presets:**

| Preset | What it does |
|---|---|
| **Room** | A small, tight space. Subtle ambience that adds a sense of place without washing out the sound. |
| **Studio** | A dry, controlled recording room. Just enough reflection to sound natural. |
| **Hall** | A large concert hall. A long, lush tail that suits orchestral and acoustic music. |
| **Cathedral** | A huge, echoing stone space. The longest, most dramatic reverb tail. |
| **Plate** | A bright, dense studio plate reverb. Classic for vocals and drums. |
| **Ambience** | A short, airy ambience. Adds a light sense of space while staying mostly dry. |

## Auto Wah (Funky Filter Sweep)

**What it does:** A filter that sweeps up and down on its own for a funky, vocal-like wah sound. Pick a preset, or set the wet mix, feedback, rate, range and frequency yourself. It is the same "wah" sweep a guitar wah pedal makes, but here it moves by itself in time with the music. It sounds great on funk, disco, and electronic tracks. It is a bold, obvious effect, so a little goes a long way on everyday listening.

**Sliders:**

| Control | What it does | Range (default) |
|---|---|---|
| **Wet mix** | How strong the wah effect is in the mix. Higher values make the sweeping filter more obvious. | -2 to +2 (1.5) |
| **Feedback** | How much of the output is fed back into the effect. Higher values make the wah more resonant and pronounced. | -1 to +1 (0.5) |
| **Rate** | How fast the filter sweeps up and down. Higher values give a faster, more rhythmic wah. | 0.1 to 9 Hz (2.0) |
| **Range** | How far the filter sweeps, in octaves. Higher values give a wider, more dramatic sweep. | 0.1 to 9 octaves (4.3) |
| **Frequency** | The base frequency the filter sweeps around. Lower values sound deeper; higher values sound brighter. | 1 to 1000 Hz (50) |

**Presets:**

| Preset | What it does |
|---|---|
| **Classic** | A balanced, classic wah sweep. A good starting point for funk and rock. |
| **Slow** | A slow, wide sweep that drifts gently up and down. Great for pads and long notes. |
| **Funky** | A fast, punchy sweep with plenty of movement. Adds rhythmic bite to guitars and synths. |
| **Deep** | A deep, wide sweep starting from a low frequency. Big and dramatic. |
| **Subtle** | A gentle, understated movement. Adds character without dominating the sound. |
| **Resonant** | A sharp, resonant wah with high feedback. Vocal-like and expressive. |

## Phaser (Swirling Whoosh)

**What it does:** A sweeping filter that adds a swirling, whooshing motion to the sound. Pick a preset, or set the feedback, rate, range and frequency yourself. It adds gentle movement and shimmer without changing the notes. It is subtle on vocals and pads, and dramatic on synths and guitars. Try Slow for a dreamy feel or Jet for a strong swirl.

**Sliders:**

| Control | What it does | Range (default) |
|---|---|---|
| **Feedback** | How much of the output is fed back into the effect. Higher values make the phaser more resonant and pronounced. | -1 to +1 (0.0) |
| **Rate** | How fast the filter sweeps up and down. Higher values give a faster, more rhythmic phasing. | 0.1 to 9 Hz (1.0) |
| **Range** | How far the filter sweeps, in octaves. Higher values give a wider, more dramatic sweep. | 0.1 to 9 octaves (4.0) |
| **Frequency** | The base frequency the filter sweeps around. Lower values sound deeper; higher values sound brighter. | 1 to 1000 Hz (100) |

**Presets:**

| Preset | What it does |
|---|---|
| **Classic** | A balanced, classic phaser sweep. A good starting point for guitars and keys. |
| **Slow** | A slow, wide sweep that drifts gently up and down. Great for pads and long notes. |
| **Fast** | A fast, shimmering sweep with plenty of movement. Adds motion and energy. |
| **Deep** | A deep, wide sweep starting from a low frequency. Big and dramatic. |
| **Subtle** | A gentle, understated movement. Adds character without dominating the sound. |
| **Jet** | An intense, resonant sweep with high feedback, the classic jet-plane whoosh. |

## Flanger (Jet-Plane Sweep)

**What it does:** A short, moving delay that gives the sound a jet-like, sweeping whoosh. Pick a preset, or set the depth, feedback, rate and delay yourself. It is a stronger, more metallic cousin of the phaser, famous for the whooshing sweep in classic rock and electronic music. Subtle settings add gentle motion, while deep settings are dramatic and obvious. Best used sparingly, for effect.

**Sliders:**

| Control | What it does | Range (default) |
|---|---|---|
| **Depth** | How strong the sweeping effect is. Higher values make the flanging more obvious. | 0 to 100% (25) |
| **Feedback** | How much of the output is fed back into the effect. Higher values make the flanger more resonant and metallic. | -99 to +99% (-50) |
| **Rate** | How fast the sweep moves up and down. Higher values give a faster, more shimmering motion. | 0 to 10 Hz (0.25) |
| **Delay** | The base delay time the sweep is built on. Higher values give a deeper, more hollow character. | 0 to 4 ms (2.0) |

**Presets:**

| Preset | What it does |
|---|---|
| **Classic** | A balanced, classic flanger. A good starting point for guitars and keys. |
| **Subtle** | A gentle, understated sweep. Adds movement without dominating the sound. |
| **Deep** | A deep, heavy sweep with strong feedback. Big and dramatic. |
| **Jet** | An intense sweep with positive feedback, the classic jet-plane whoosh. |
| **Fast** | A fast, shimmering sweep with plenty of motion and energy. |
| **Wide** | A slow, wide sweep with a long delay. Lush and spacious. |

## Echo (Repeats)

**What it does:** Repeats the sound as fading echoes for a sense of space and depth. Pick a preset, or set the wet mix, feedback and delay yourself. It is like calling out in a canyon: the sound comes back one or more times after a short gap. A single short repeat adds body and a retro feel, while longer repeats with more feedback create spacious, trailing tails. The Ping Pong preset bounces the repeats between your left and right ears, which is fun on headphones. Keep the wet mix modest so the echoes support the music rather than cover it.

**Sliders:**

| Control | What it does | Range (default) |
|---|---|---|
| **Wet mix** | How loud the echoes are compared with the original sound. Higher values make the repeats stand out more. | -2 to +2 (0.6) |
| **Feedback** | How many times the echo repeats. Higher values give more repeats that take longer to fade away. | -1 to +1 (0.5) |
| **Delay** | The time between echoes. Shorter values give a tight slap-back; longer values give spaced-out repeats. | 0.01 to 2 s (0.4) |

**Presets:**

| Preset | What it does |
|---|---|
| **Slapback** | A single, tight repeat right behind the sound. Classic rockabilly slap-back. |
| **Room** | A short, natural echo, like a small room. Adds space without smearing the sound. |
| **Tape** | Warm, medium repeats that fade gradually, like an old tape delay. |
| **Dub** | Long, heavy repeats with strong feedback. Big, dubby and spacious. |
| **Ping Pong** | Echoes bounce between the left and right speakers for a wide stereo effect. |
| **Long** | Slow, widely spaced repeats that trail off far behind the sound. |

## Chorus (Thicker, Wider Sound)

**What it does:** Thickens and widens the sound by layering a shifting copy over the original. Pick a preset, or set the wet/dry mix, depth, rate and feedback yourself. It makes one instrument or voice sound like several playing together, by adding slightly detuned, moving copies. This adds richness and a gentle shimmer. Subtle settings warm things up, while strong settings sound lush and dreamy. It is popular on guitars, keyboards, and vocals.

**Sliders:**

| Control | What it does | Range (default) |
|---|---|---|
| **Wet/Dry** | How much of the chorus you hear compared with the original sound. Higher values make the effect more obvious. | 0 to 100% (50) |
| **Depth** | How far the pitch wavers up and down. Higher values give a thicker, more shimmering sound. | 0 to 100% (25) |
| **Rate** | How fast the shimmer moves. Slower rates sound gentle and lush; faster rates sound more like vibrato. | 0 to 10 Hz (1.1) |
| **Feedback** | How much of the effect is fed back into itself. Higher values make the chorus more resonant and intense. | -99 to +99% (25) |

**Presets:**

| Preset | What it does |
|---|---|
| **Subtle** | A gentle thickening that adds warmth without drawing attention to itself. |
| **Lush** | A rich, classic chorus. A great all-round setting for guitars and keys. |
| **Ensemble** | A full, layered shimmer that makes a single instrument sound like several. |
| **Vibrato** | Fully wet with a fast rate, for a wobbling vibrato instead of a subtle chorus. |
| **Wide** | A slow, wide shimmer that opens up the stereo image. Spacious and dreamy. |
| **Twelve-String** | A bright, resonant shimmer reminiscent of a twelve-string guitar. |

## Distortion (Grit and Edge)

**What it does:** Adds grit and edge by overdriving the sound. Pick a preset, or set the drive, output and tone yourself. It deliberately roughens the sound, from a warm, gritty edge to a broken, fuzzy tone. It is a creative, for-fun effect rather than a way to improve quality, so use it in small amounts. It is fun on electronic, rock, and experimental tracks. Lower the Output if a heavy preset gets too loud.

**Sliders:**

| Control | What it does | Range (default) |
|---|---|---|
| **Drive** | How hard the sound is distorted. Higher values are grittier and more aggressive. | 0 to 100% (15) |
| **Output** | The output level after distortion. Lower it if a heavy setting gets too loud. | -60 to 0 dB (-18) |
| **Tone** | Rolls off the highs before distortion. Lower values sound darker and warmer. | 100 to 8000 Hz (8000) |
| **Center** | Which frequency the distortion is focused around. Shifts the character brighter or darker. | 100 to 8000 Hz (2400) |
| **Width** | How wide that focus is. Narrow sounds sharp and nasal; wide sounds full and open. | 100 to 8000 Hz (2400) |

**Presets:**

| Preset | What it does |
|---|---|
| **Warm Drive** | A light, warm grit that adds edge without changing the character much. |
| **Crunch** | A classic crunchy overdrive, punchy and rhythmic. |
| **Overdrive** | A bright, driven tone with plenty of bite. Great for lead sounds. |
| **Fuzz** | A thick, saturated fuzz. Heavy and full of harmonics. |
| **Metal** | A tight, mid-focused high-gain tone for aggressive, heavy sounds. |
| **Screamer** | A mid-boosted overdrive that cuts through, like a tube screamer. |
| **LoFi** | A crushed, narrow-band distortion for a gritty lo-fi character. |

## Rotate (Spinning Stereo)

**What it does:** Spins the sound around the stereo field for a rotary, swirling effect. Pick a preset, or set the rate yourself. It slowly moves the sound around your left and right channels, a bit like a spinning speaker, which adds a swirling, hypnotic feel. Slow settings are gentle and wide, while fast settings are dizzy and obvious. It is a stereo effect, so it is most noticeable on headphones or well-placed speakers.

**Slider:**

| Control | What it does | Range (default) |
|---|---|---|
| **Rate** | How fast the sound spins around the stereo field. Negative values spin the other way; zero holds it still. | -5 to +5 Hz (1.0) |

**Presets:**

| Preset | What it does |
|---|---|
| **Slow Pan** | A slow, gentle drift from side to side. Subtle and wide. |
| **Sway** | A steady left-right sway. Adds gentle motion to the stereo image. |
| **Rotary** | A medium spin reminiscent of a rotary speaker. |
| **Fast Spin** | A fast spin around the stereo field for a dizzy, swirling effect. |
| **Reverse** | A medium spin in the opposite direction. |
| **Whirl** | A very fast whirl. Intense and disorienting. |

## Crossfeed (Natural Sound on Headphones)

On speakers, each of your ears hears both the left and the right speaker, just at slightly different times and volumes. On headphones, that natural blending is gone: your left ear hears only the left channel and your right ear only the right. This "super stereo" can make music feel like it is split inside your head, and hard-panned recordings, where an instrument sits fully on one side, can feel unnatural or tiring on long listens.

Crossfeed fixes this by blending a small, filtered amount of each channel into the other, with a tiny delay and a gentle roll-off of the high frequencies. That is close to how sound from real speakers reaches both of your ears, including the way your head slightly shadows the far ear. The result is a more natural, speaker-like image that sits a little in front of you instead of inside your head, and it reduces listening fatigue on long sessions. Flacbox uses the well-known **bs2b (Bauer stereophonic-to-binaural)** method, a respected open-source crossfeed used by many audiophile players. You can read about the algorithm on the [bs2b project page](https://bs2b.sourceforge.net/).

The **Cutoff** controls how warm the blend sounds, and the **Feed level** controls how strong it is. The presets cover the classic bs2b levels, from a barely-there touch up to a firm, speaker-like blend. Crossfeed is a headphones effect, so leave it off when you listen on speakers.

**Sliders:**

| Control | What it does | Range (default) |
|---|---|---|
| **Cutoff** | Sets where the bleed between channels begins to roll off. Lower values give a warmer, more pronounced effect. | 300 to 2000 Hz (700) |
| **Feed level** | Controls how much of one channel bleeds into the other. Higher values produce a more speaker-like sound. | 1 to 15 dB (4.5) |

**Presets:**

| Preset | What it does |
|---|---|
| **Subtle** | Barely-there crossfeed for casual listening. Softens hard-panned stereo without changing tonal balance. |
| **Chu Moy** | The classic all-purpose default. Balanced and lightly warm, it works on almost any material. Start here. |
| **Strong** | Stronger bleed for harder-panned mixes. More obvious stereo narrowing. |
| **Jan Meier** | Popular among headphone enthusiasts. Wider feed, more speaker-like presentation, slight bass lift. |
| **Speaker-like** | Tuned for the most natural speaker-style reproduction over headphones. |
| **Vintage Stereo** | Aggressive crossfeed tuned for 1960s and 1970s mixes with hard-panned drums and vocals. |

## Signal Processing: Build Your Own DSP Chain

Beyond the ready-made effects, Flacbox lets you build your own chain in **Settings > Audio player > Signal processing**. As the app explains when the chain is empty: *"Tap + to add an effect. Turn each one on or off with its switch, drag to reorder, tap to edit its parameters, and long-press to duplicate or delete."*

The **order matters**: a filter before a distortion sounds different from the same filter after it. You can also point the whole chain at **All channels**, **Left channel**, or **Right channel**.

Below is every block, with the app's own text for each slider and each preset.

### Gain (Level Trim)

Raises or lowers the level at one point in the chain.

| Control | What it does | Range (default) |
|---|---|---|
| **Gain** | Boosts or cuts the level at this point in the chain. Use it to make up level after other effects, or to drive the ones that follow. | -24 to +24 dB (0) |

| Preset | What it does |
|---|---|
| **Unity** | No change in level. A neutral starting point. |
| **Cut** | A big cut. Tames a loud source, or makes room before the effects that follow. |
| **Trim** | A gentle cut to pull the level back a little. |
| **Lift** | A modest boost to bring a quiet source up. |
| **Boost** | A strong boost for quiet material, or to drive the following effects harder. |
| **Max** | Maximum boost. Loud, watch for clipping later in the chain. |

### Low Pass (Removes Highs)

| Control | What it does | Range (default) |
|---|---|---|
| **Cutoff** | Sets where the filter starts rolling off the highs. Lower it to darken and soften the sound; raise it toward the top to open fully. | 20 Hz to 20 kHz (20 kHz) |
| **Resonance** | Emphasizes the frequencies right at the cutoff. Keep it low for a clean roll-off; raise it for a peaky, whistling edge. | 0.1 to 10 (0.707) |

| Preset | What it does |
|---|---|
| **Air** | Trims only the very top. Takes a little edge off without dulling the sound. |
| **Warm** | A gentle roll-off of the highs for a warmer, rounder tone. |
| **Mellow** | Noticeably softened. Pulls the brightness back for a laid-back feel. |
| **Muffled** | Dark and muffled, as if heard through a wall. |
| **Telephone** | A narrow, resonant peak low in the range. A thin, telephone-like voice. |

### High Pass (Removes Lows)

| Control | What it does | Range (default) |
|---|---|---|
| **Cutoff** | Sets where the filter starts rolling off the lows. Raise it to thin out the low end and remove rumble; lower it toward the bottom to open fully. | 20 Hz to 20 kHz (20 Hz) |
| **Resonance** | Emphasizes the frequencies right at the cutoff. Keep it low for a clean roll-off; raise it for a peaky, whistling edge. | 0.1 to 10 (0.707) |

| Preset | What it does |
|---|---|
| **Rumble Cut** | Removes subsonic rumble and DC offset without touching the audible low end. |
| **Tighten** | Trims boomy low frequencies for a tighter, cleaner bass. |
| **Thin** | Cuts the warmth and body, leaving a lighter, thinner sound. |
| **Radio** | Only the mids and highs remain, like a small radio speaker. |
| **Telephone** | A narrow, resonant peak high in the range. A thin, telephone-like voice. |

### Band Pass (Keeps a Middle Band)

| Control | What it does | Range (default) |
|---|---|---|
| **Center** | Sets the frequency the filter passes. Everything above and below it is rolled off. Sweep it to pick out bass, mids, or highs. | 20 Hz to 20 kHz (1 kHz) |
| **Resonance** | Controls how wide the band is. Low values let a broad range through; raise it to narrow in on the center for a sharp, resonant tone. | 0.1 to 10 (0.707) |

| Preset | What it does |
|---|---|
| **Voice** | A wide band around the mid-range where most vocals sit. A neutral starting point. |
| **Bass** | Isolates the low end, leaving just the bass and kick. |
| **Body** | Focuses on the low-mids for a warm, boxy body. |
| **Presence** | Lifts the upper-mids for clarity and presence. |
| **Telephone** | A narrow mid-range band. A thin, telephone-like sound. |
| **Wah** | A very narrow, resonant peak. Sweep the center for a wah effect. |

### Notch (Removes One Narrow Band)

| Control | What it does | Range (default) |
|---|---|---|
| **Frequency** | Sets the frequency the filter removes. Everything above and below it passes through. Tune it onto a hum or resonance to cut it out. | 20 Hz to 20 kHz (60 Hz) |
| **Resonance** | Controls how wide the cut is. Low values scoop out a broad range; raise it to remove just a pinpoint band and leave the rest untouched. | 0.1 to 10 (8.0) |

| Preset | What it does |
|---|---|
| **Mains Hum 60** | Removes 60 Hz electrical hum (North American mains). A neutral starting point. |
| **Mains Hum 50** | Removes 50 Hz electrical hum (European and other mains). |
| **Rumble** | Cuts a low-frequency rumble or resonance without thinning the whole bottom end. |
| **Mud** | Scoops out low-mid mud for a cleaner, clearer sound. |
| **Boxy** | Removes a boxy mid-range honk. |
| **Harsh** | Tames a harsh, piercing peak in the upper-mids. |

### Peaking (Parametric EQ Band)

| Control | What it does | Range (default) |
|---|---|---|
| **Frequency** | The center of the band to boost or cut. Sweep it to find the frequency you want to shape. | 20 Hz to 20 kHz (1 kHz) |
| **Gain** | How much to boost or cut at the center. Positive lifts the band; negative scoops it out. | -15 to +15 dB (0) |
| **Q factor** | Sets how wide the band is. Low values shape a broad area; high values narrow in for surgical, pinpoint changes. | 0.1 to 10 (1.0) |

| Preset | What it does |
|---|---|
| **Presence** | A broad upper-mid lift for clarity and presence. A neutral starting point. |
| **Warmth** | A wide low-mid boost that adds body and warmth. |
| **Vocal Boost** | Lifts the core vocal range to bring voices forward. |
| **Cut Mud** | Scoops out boxy low-mid mud for a cleaner sound. |
| **Tame Harsh** | A narrow cut to tame a harsh, piercing peak. |
| **Punch** | A low boost that adds punch and impact to the low end. |
| **Sub Boost** | A deep boost at the very bottom for extra sub-bass weight. |
| **Air** | A broad lift at the top for an open, airy sheen. |
| **Clarity** | Lifts the high-mids to add definition and edge. |
| **De-Ess** | A narrow cut in the sibilance range to tame harsh S sounds. |
| **De-Boom** | Cuts a boomy low-frequency buildup for a tighter low end. |
| **Scoop** | A wide mid-range dip for a scooped, modern tone. |

### Low Shelf (Bass Control and Bass Boost)

| Control | What it does | Range (default) |
|---|---|---|
| **Frequency** | Sets the corner below which the shelf takes effect. Everything under it is boosted or cut together. | 20 to 2000 Hz (200) |
| **Gain** | How much to lift or lower the low end. Positive adds weight and warmth; negative thins it out. | -15 to +15 dB (0) |

| Preset | What it does |
|---|---|
| **Warmth** | A gentle low-end lift for warmth and body. A neutral starting point. |
| **Bass Boost** | A solid boost to the bass for weight and punch. |
| **Fullness** | Fills out the lower-mids for a fuller, rounder sound. |
| **Trim Bass** | A modest cut to lighten a bass-heavy mix. |
| **Cut Lows** | A strong cut to thin out or de-boom the low end. |
| **Big Bottom** | A big low-end boost for maximum weight and rumble. |

### High Shelf (Treble Control)

| Control | What it does | Range (default) |
|---|---|---|
| **Frequency** | Sets the corner above which the shelf takes effect. Everything over it is boosted or cut together. | 1 to 20 kHz (8 kHz) |
| **Gain** | How much to lift or lower the high end. Positive adds brightness and air; negative smooths and darkens. | -15 to +15 dB (0) |

| Preset | What it does |
|---|---|
| **Presence** | A gentle high-end lift for clarity and detail. A neutral starting point. |
| **Air** | Opens up the very top for an airy, open sound. |
| **Bright** | A strong boost for a crisp, bright, forward tone. |
| **Soften** | A modest cut to take the edge off harsh highs. |
| **Tame Highs** | A strong cut to darken and smooth an overly bright sound. |
| **Sparkle** | A big top-end boost for maximum shimmer and sparkle. |

### Soft Clip (Warm Saturation)

| Control | What it does | Range (default) |
|---|---|---|
| **Drive** | Pushes the signal harder into the waveshaper. Low amounts add gentle warmth; high amounts round the peaks into thick saturation and grit. | 0 to 40 dB (0) |

| Preset | What it does |
|---|---|
| **Warm** | A touch of drive for gentle, analog-style warmth. |
| **Drive** | Noticeable saturation that thickens and colors the sound. |
| **Crunch** | Heavy drive with an audible crunchy edge. |
| **Fuzz** | Thick, fuzzy distortion. The peaks are squashed hard. |
| **Destroy** | Maximum drive. Aggressive, fully saturated grit. |

### Bit Crusher (Retro Lo-Fi)

| Control | What it does | Range (default) |
|---|---|---|
| **Bit depth** | Sets how many bits describe each sample. Fewer bits mean coarser steps and more quantization noise, for a crunchy, gritty digital sound. | 1 to 16 bits (16) |
| **Sample rate** | Downsamples the audio. At one hundred percent the rate is untouched; lower it to hold each sample longer, dulling the highs and adding a harsh, aliased edge. | 1% to 100% (100%) |

| Preset | What it does |
|---|---|
| **Vintage** | A subtle drop in quality, like an early digital sampler. |
| **LoFi** | Classic 8-bit, half-rate lo-fi. Grainy and retro. |
| **Crunch** | Heavier crushing with an audible crunchy edge. |
| **Gritty** | Coarse and gritty. The steps between levels are obvious. |
| **Destroy** | Extreme reduction. Harsh, broken, barely recognizable. |

### Ring Modulator (Metallic and Robotic Tones)

| Control | What it does | Range (default) |
|---|---|---|
| **Carrier** | Sets the frequency of the tone the signal is multiplied by. A few hertz gives a tremolo wobble; higher frequencies add metallic, bell-like, and robotic overtones. | 1 to 4000 Hz (440) |
| **Mix** | Blends the modulated sound in with the original. At zero percent you hear only the dry signal; at one hundred percent only the fully modulated tone. | 0% to 100% (0%) |

| Preset | What it does |
|---|---|
| **Tremolo** | A very low carrier turns it into an amplitude tremolo, wobbling the volume. |
| **Robot** | A mid carrier adds clangy overtones for a classic robot-voice effect. |
| **Metallic** | Dense, inharmonic overtones for a harsh, metallic tone. |
| **Bell** | A higher carrier gives bright, bell-like ringing. |
| **Alien** | Full wet with a high carrier. Extreme, alien, barely recognizable. |

### Tremolo (Volume Wobble)

| Control | What it does | Range (default) |
|---|---|---|
| **Rate** | Sets how fast the volume pulses. Slower rates give a smooth sway; faster rates give a rapid stutter. | 0.1 to 20 Hz (5) |
| **Depth** | Sets how much the volume drops on each pulse. At zero percent the level is steady; at one hundred percent it dips all the way to silence. | 0% to 100% (0%) |

| Preset | What it does |
|---|---|
| **Gentle** | A slow, shallow sway. Subtle movement without drawing attention. |
| **Classic** | The classic amp tremolo: a medium rate and moderate depth. |
| **Deep** | A strong, deep pulse that nearly drops to silence each cycle. |
| **Fast** | A quick flutter for a shimmering, nervous feel. |
| **Chop** | Fast and full depth. A hard, stuttering chop. |

### Delay (Echo)

| Control | What it does | Range (default) |
|---|---|---|
| **Time** | Sets the gap before each echo. Short times give a tight slapback; longer times space the repeats further apart. | 0.01 to 2 s (0.25) |
| **Feedback** | Sets how much of each echo is fed back in. Low values give a single repeat; higher values build a long, trailing series of echoes. | 0 to 0.95 (0.4) |
| **Mix** | Blends the echoes in with the original. At zero percent you hear only the dry signal; at one hundred percent only the echoes. | 0% to 100% (0%) |

| Preset | What it does |
|---|---|
| **Slapback** | A single short echo, tight against the original. Rockabilly and vocal doubling. |
| **Echo** | The classic echo: a clear repeat with a few trailing tails. |
| **Ping** | A quick, bouncing repeat that adds rhythmic movement. |
| **Ambient** | Longer, softer repeats that wash out into a spacious tail. |
| **Dub** | High feedback for long, dubby cascades of echo. |
| **Cavern** | Long, deep repeats, like sound echoing through a huge space. |

### Stereo Width (Narrow or Widen)

| Control | What it does | Range (default) |
|---|---|---|
| **Width** | Narrows or widens the stereo image. Zero percent collapses to mono, one hundred percent leaves it untouched, and higher values push the sides wider. Only affects stereo tracks on the All-channels target. | 0% to 200% (100%) |

| Preset | What it does |
|---|---|
| **Wide** | A gentle widening that opens up the stereo image. A neutral starting point. |
| **Wider** | A stronger spread for a big, immersive stereo field. |
| **Max** | Maximum width. Very wide, but watch for mono-compatibility issues. |
| **Narrow** | Pulls the sides in for a tighter, more centered image. |
| **Focused** | Nearly centered, with just a hint of stereo. |
| **Mono** | Fully collapsed to mono. Both speakers play the same signal. |

## How It All Works Under the Hood (Simple Version)

- **Engines:** you pick one in Settings > Audio player > Playback engine: **Standard** (system), **Universal** (FFmpeg), or **Sound FX** (the **BASS™ engine** from [Un4seen Developments](https://www.un4seen.com/)). The engine you choose decides which formats play, and the effects, equalizer, and DSP chain run only in the Sound FX engine.
- **Formats:** the BASS™ engine adds FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, and module (tracker) music on top of the system and FFmpeg formats.
- **Effects:** the equalizer, compressor, and most effects use the BASS™ effects add-ons. Freeverb is the Freeverb reverb. Chorus, Flanger, and Distortion use classic DirectX-style effects with their own controls.
- **Volume Normalization:** a live **EBU R128** loudness leveler (the loudness standard used in broadcast and streaming).
- **Crossfeed:** the **bs2b (Bauer)** crossfeed, run inside the BASS™ engine.
- **DSP chain:** your custom blocks, applied in the exact order you set, on all channels or just one side.
- **Output:** you can set the sample rate, channel count, and buffer size to match your gear.

Because all of this runs live while the music plays, the effects:

- Work in **real time** on everything, including cloud files, streams, and module music.
- **Never change or re-save** your files. Turn an effect off and the original returns.
- **Remember your settings** for each effect.
- Can be **mixed and matched** freely, since each one is separate.

## Simple Recipes to Try

**Everyday listening**

- **More bass, cleanly:** Equalizer > Bass Booster, then lower the Preamplifier 1 to 2 dB. Or add a DSP Low Shelf on Bass Boost.
- **Even volume across a mixed playlist:** Volume Normalization > Standard, plus Compressor > Soft.
- **Gentle overall polish:** Compressor > Transparent, plus Volume Normalization > Light.
- **Clearer vocals:** Equalizer > Vocal Booster, or a DSP Peaking block on Vocal Boost.
- **Fuller sound on small phone speakers:** Equalizer > Small Speakers.

**Headphones**

- **Nicer, less tiring on headphones:** Crossfeed > Chu Moy or Jan Meier.
- **Wider sound on headphones:** DSP Stereo Width > Wide, plus Crossfeed > Chu Moy.
- **Fix hard-panned 1960s and 1970s records:** Crossfeed > Vintage Stereo.
- **A little air and space:** Freeverb > Ambience, kept low, plus Crossfeed > Subtle.

**Quiet times and spoken audio**

- **Late-night quiet listening:** Volume Normalization > Night, plus Compressor > Late Night.
- **Podcasts and audiobooks:** Compressor > Voice / Podcast, plus Equalizer > Spoken Word.
- **Loudest, most even sound in a noisy car:** Volume Normalization > Strong, plus Compressor > Heavy.

**Fixing problems**

- **Tame a harsh, bright recording:** Equalizer > Treble Reducer, or a DSP Peaking block on Tame Harsh.
- **Remove electrical hum:** DSP chain > Notch > Mains Hum 60 (or Mains Hum 50 in Europe).
- **Tighter, cleaner bass:** DSP High Pass > Tighten, to cut the boomy low end.
- **Less boom in a bass-heavy mix:** DSP Low Shelf > Trim Bass, or Peaking > De-Boom.

**Creative and fun**

- **Warm, roomy feel:** Freeverb > Hall, kept low.
- **Dreamy, spacious guitars:** Chorus > Wide, plus Echo > Long.
- **Retro lo-fi:** DSP chain > Bit Crusher (LoFi) into Soft Clip (Warm).
- **Funky movement on electronic tracks:** Auto Wah > Funky, or Phaser > Fast.
- **Classic jet-plane sweep:** Flanger > Jet.

## FAQ

{{% details title="What sound engine does Flacbox use?" closed="true" %}}
You choose one Playback engine in Settings > Audio player: Standard (Apple's system engine), Universal (the FFmpeg engine), or Sound FX (the BASS™ engine from Un4seen Developments, un4seen.com). The engine you pick decides which file formats play. Sound FX is the one that plays extra formats like FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, and MOD or tracker music, and it is the only engine that provides the live effects, the 10-band equalizer, and the DSP chain. To use the effects, set the Playback engine to Sound FX.
{{% /details %}}

{{% details title="Can Flacbox play MOD, XM, IT, and other tracker or module music?" closed="true" %}}
Yes. The BASS™ engine has a built-in module player that loads MOD, XM, IT, S3M, MTM, UMX, and MO3 files and rebuilds the song live from its patterns and instrument sounds, the way tracker music is meant to play. Regular iPhone players cannot do this. Effects and the equalizer work on module music too.
{{% /details %}}

{{% details title="Does Flacbox support DSD and high-resolution files?" closed="true" %}}
Yes. Flacbox plays DSD files (DSF and DFF) through the BASS™ engine using DSD over PCM so they work on normal output hardware, plus FLAC, WavPack, Monkey's Audio (APE), Musepack, and TrueAudio for lossless playback.
{{% /details %}}

{{% details title="What sound effects does Flacbox have?" closed="true" %}}
A 10-band equalizer, Volume Normalization, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate, and Crossfeed, plus a build-your-own DSP chain with filters, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay, and stereo width. Each one is separate and can be combined with the others.
{{% /details %}}

{{% details title="What is a preset?" closed="true" %}}
A preset is a ready-made setting for an effect. Instead of moving sliders yourself, you tap a preset and the sound changes to match. Every effect in Flacbox has several presets, and this guide lists what each one does. If you move a slider after picking a preset, the effect shows "Manual" to tell you it is now using your own values.
{{% /details %}}

{{% details title="How do I open the audio effects in Flacbox?" closed="true" %}}
Open the Now Playing player, tap the ⋯ (More) button, and choose Audio effects. Or go to Settings > Audio player > Audio effects. Tap an effect, turn on its switch, and pick a preset, or open the sliders to fine-tune.
{{% /details %}}

{{% details title="Where is the equalizer, and what are the best settings?" closed="true" %}}
Go to Settings > Audio player > Audio equalizer. It has 10 bands from 32 Hz to 16 kHz, each from -12 to +12 dB, plus a -24 to +24 dB Preamplifier and 22 presets. For more bass, use Bass Booster. For clearer voices, use Vocal Booster or Pop. For a brighter sound, use Treble Booster. Then adjust single bands to taste.
{{% /details %}}

{{% details title="How do I boost the bass in Flacbox?" closed="true" %}}
Two easy ways. In the Audio equalizer, pick Bass Booster (or raise the 32 Hz and 64 Hz bands a few dB). Or, in Signal processing, add a Low Shelf block set to Bass Boost. In both cases, lower the Preamplifier or add a Gain block 1 to 2 dB so the bass stays clean and does not distort.
{{% /details %}}

{{% details title="Which equalizer preset is best for my music?" closed="true" %}}
Rock and Electronic add energy with strong lows and highs. Acoustic, Jazz, and Classical stay warm and natural. Pop and Vocal Booster push voices forward. Bass Booster and Hip-Hop add weight. Deep and Loudness sound fuller at low volume. Start with the one that matches your genre, then fine-tune.
{{% /details %}}

{{% details title="What is Volume Normalization, and how is it different from ReplayGain?" closed="true" %}}
It makes every track play at about the same loudness. It measures the real loudness using the EBU R128 standard (in LUFS, like streaming services) and adjusts each track toward your target, with a max-boost limit. Unlike ReplayGain, it needs no tags in your files and works on any source, live, without changing the audio. Presets: Light, Standard, Strong, and Night.
{{% /details %}}

{{% details title="What is Crossfeed, and should I use it?" closed="true" %}}
Crossfeed mixes a little of the left and right channels together so headphones feel more like real speakers and less like the sound is stuck in your head. It is only for headphones, so turn it off for speakers. Flacbox uses the bs2b (Bauer) method, with presets like Chu Moy and Jan Meier.
{{% /details %}}

{{% details title="What is the difference between the Compressor and Volume Normalization?" closed="true" %}}
Volume Normalization matches the loudness between different songs. The Compressor evens out the loud and quiet parts inside a single song. They solve different problems and work well together, especially in a car or a noisy place.
{{% /details %}}

{{% details title="What is the Signal processing (DSP) chain?" closed="true" %}}
It is a build-your-own rack in Settings > Audio player > Signal processing. Add blocks like filters, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay, and stereo width, put them in any order, turn each on or off, and point the chain at all channels, left, or right. Because order matters, you can design exactly the sound you want.
{{% /details %}}

{{% details title="What is the difference between the Equalizer, the effects, and the DSP chain?" closed="true" %}}
The Equalizer is a simple 10-band tone control. The Audio effects are ready-made tools (compressor, reverb, echo, and so on) with presets. The DSP chain is where you build your own effect order from individual blocks. You can run all three at the same time.
{{% /details %}}

{{% details title="Do the effects change or damage my music files?" closed="true" %}}
No. Everything is applied live while the music plays. Your files are never changed or re-saved. Turn an effect off and the original sound returns at once.
{{% /details %}}

{{% details title="Can I use more than one effect at the same time?" closed="true" %}}
Yes. Each effect has its own switch and there is no master switch, so any combination works. For example, Volume Normalization plus Compressor for even listening, or Freeverb plus Crossfeed on headphones, with the equalizer on top.
{{% /details %}}

{{% details title="Why are the effect controls greyed out?" closed="true" %}}
The effect is turned off. Turn on its switch at the top of the editor to use the controls. Every effect is off by default.
{{% /details %}}

{{% details title="What does the Manual label mean?" closed="true" %}}
It means you moved a slider away from a preset, so the effect is now using your own custom values instead of a named preset. Every slider has a reset button, and picking a preset again replaces your manual values.
{{% /details %}}

{{% details title="Can I save and share my equalizer presets?" closed="true" %}}
Yes. Besides the 22 built-in presets, you can make your own, reorder them, and export or import them to move your settings to another device.
{{% /details %}}

{{% details title="Do the effects work with CarPlay, streaming, and background play?" closed="true" %}}
Yes. The effects run inside the BASS™ engine, so they apply to local files, cloud drives, media servers, streams, and module music, and they keep working during CarPlay and background playback.
{{% /details %}}

{{% details title="Can I change the audio output quality?" closed="true" %}}
Yes. In Settings > Audio player you can set the output sample rate, the number of channels, and the buffer size to match your headphones, speakers, or DAC.
{{% /details %}}

{{% details title="What is a good starting setup for headphones?" closed="true" %}}
Turn on Volume Normalization (Standard), add a light Compressor (Soft), pick an equalizer preset you like, and turn on Crossfeed (Chu Moy or Jan Meier). Leave reverb, echo, and distortion off unless you want a creative sound.
{{% /details %}}

---

*BASS is a trademark of Un4seen Developments Ltd. See [un4seen.com](https://www.un4seen.com/). Crossfeed uses the bs2b (Bauer stereophonic-to-binaural) algorithm; see the [bs2b project page](https://bs2b.sourceforge.net/).*
