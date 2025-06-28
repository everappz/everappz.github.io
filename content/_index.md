---
date: '2025-06-12T17:00:00+00:00'
draft: false
title: 'Home'
seo:
  title: 'Home | Everappz Home Page'
layout: hextra-home
date: 2025-06-12
description: "Explore Everappz apps for iPhone and Mac: play FLAC, DSD, APE, and ALAC, stream from cloud storage or NAS, download music and videos, edit tags, and customize playback with equalizer and playlist tools."
keywords: [
  "FLAC player iPhone", "DSD audio player iOS", "ALAC player Mac", "offline music player iPhone", 
  "hi-res audio app iOS", "lossless music player", "stream music from NAS", "cloud music player", 
  "video player for iPhone", "MP4 MKV player Mac", "audio equalizer iOS", "metadata tag editor iPhone", 
  "multi-cloud file player", "iTunes File Sharing app", "CarPlay music app", 
  "AirPlay and Chromecast support", "Mac music organizer", "playlist manager iOS"
]
tags: [
  "audio player", "video player", "FLAC support", "offline playback", "cloud streaming", 
  "hi-res audio", "DSD audio", "iPhone apps", "Mac apps", "audio tag editor", 
  "media library organizer", "equalizer", "file manager", "NAS streaming", 
  "Chromecast", "AirPlay", "CarPlay", "playlist creation"
]
---

{{< rawhtml >}}

<style>
  html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    overflow-x: hidden;
  }

  html.dark body {
    background: black;
  }

  html:not(.dark) body {
    background: white;
  }

  #stars {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    pointer-events: none;
  }
</style>

<canvas id="stars"></canvas>

<script>
  const canvas = document.getElementById("stars");
  const ctx = canvas.getContext("2d");

  let w = window.innerWidth;
  let h = window.innerHeight;
  canvas.width = w;
  canvas.height = h;

  const stars = Array.from({ length: 200 }, () => ({
    x: Math.random() * w,
    y: Math.random() * h,
    radius: Math.random() * 1.5,
    // velocity: Math.random() * 0.5 + 0.2
    velocity: Math.random() * 0.2 + 0.05
  }));

  function getStarColor() {
    return document.documentElement.classList.contains("dark")
      ? "rgba(255,255,255,0.3)"  // white-ish in dark
      : "rgba(0,0,0,0.2)";       // faint black in light
  }

  function animate() {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = getStarColor();
    for (const star of stars) {
      ctx.beginPath();
      ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
      ctx.fill();

      star.y += star.velocity;
      if (star.y > h) {
        star.y = 0;
        star.x = Math.random() * w;
      }
    }
    requestAnimationFrame(animate);
  }

  animate();

  window.addEventListener("resize", () => {
    w = window.innerWidth;
    h = window.innerHeight;
    canvas.width = w;
    canvas.height = h;
  });

  // Rerun animation when theme changes
  const observer = new MutationObserver(() => {
    // reset star color
    animate();
  });

  observer.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["class"]
  });
</script>

{{< /rawhtml >}}




<!-- {{< rawhtml >}}

<style>
  body {
    background: black;
    margin: 0;
    padding: 0;
  }

  .star-background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('/gif/urban-line-stars-line.gif');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
    z-index: -1;
    pointer-events: none; /* allows clicking/scrolling through */
  }
</style>

<div class="star-background"></div>

{{< /rawhtml >}} -->

<!-- force dark theme for this page -->
{{< force-dark >}}

{{< hextra/hero-container
  image="/gif/juicy-rocket.gif"
  imageWidth="200"
>}}

<div class="hx:flex hx:flex-col hx:items-center hx:justify-center hx:sm:block">

{{< hextra/hero-badge >}}
  <div class="hx:w-2 hx:h-2 hx:rounded-full hx:bg-primary-400"></div>
  <span>14 Million Downloads Worldwide</span>
  {{< icon name="arrow-circle-right" attributes="height=14" >}}
{{< /hextra/hero-badge >}}

<div class="hx:mt-6 hx:mb-6">
{{< hextra/hero-headline >}}
 EVERAPPZ
{{< /hextra/hero-headline >}}
</div>

<div class="hx:mb-12">
{{< hextra/hero-subtitle >}}
<strong>Discover our apps that boost productivity,&nbsp;<br class="hx:sm:block hx:hidden" />and make daily tasks easier and more enjoyable.</strong>
{{< /hextra/hero-subtitle >}}
</div>

<div class="hx:mb-6">
{{< hextra/hero-paragraph >}}
<strong>• Built for You. Improved by You.</strong><br>
We read all reviews and use your feedback to improve every update.<br><br>
<strong>• Performance Meets Purpose.</strong><br>
No bloat. Just clean, stable apps with features that matter.<br><br>
<strong>• Privacy. Accessibility. Simplicity.</strong><br>
Easy to use, fully accessible, and built with your privacy in mind.<br>
{{< /hextra/hero-paragraph >}}
</div>

</div>

{{< /hextra/hero-container >}}

<div class="hx:mt-6"></div>

{{< hextra/section-headline >}}
Our Products
{{< /hextra/section-headline >}}

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{< cards cols="8">}}

  {{< card 
    link="/products/evervideo"
    image="/app_icons/Evervideo_Icon-App-1024x1024.png"   
    title="Evervideo" 
    method="Crop"
    options="1024x1024"
    subtitle="HD Video Player & Media Library Organizer" 
  >}}

  {{< card 
    link="/products/evermusic"
    image="/app_icons/Evermusic_Icon-App-1024x1024.png"  
    title="Evermusic" 
    method="Crop"
    options="1024x1024"
    subtitle="Cloud Streamer & Offline Music Player" 
  >}}

  {{< card 
    link="/products/flacbox"
    image="/app_icons/Flacbox_Icon-App-1024x1024.png"   
    title="Flacbox" 
    method="Crop"
    options="1024x1024"
    subtitle="Hi-Res Audio Player & Playlists Manager" 
  >}}

  {{< card 
    link="/products/evertag"
    image="/app_icons/Evertag_Icon-App-1024x1024.png"  
    title="Evertag" 
    method="Crop"
    options="1024x1024"
    subtitle="Music Metadata Editor & Album Art Organizer" 
  >}}

{{< /cards >}}

</div>

<div class="hx:mt-6"></div>

{{< hextra/section-headline >}}
App Store Reviews
{{< /hextra/section-headline >}}

<div class="hx:mt-6"></div>

<div class="hx:w-full">
{{< appstore-reviews apps="1097564256,1594027432,885367198,1564384601,1450763230,1594027661" stars="5,4" >}}
</div>
