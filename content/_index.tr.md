---
date: '2025-06-12T17:00:00+00:00'
draft: false
title: 'Ana Sayfa'
layout: hextra-home
description: "iPhone ve Mac için Everappz uygulamalarini kesfedin: FLAC, DSD, APE ve ALAC oynatın, bulut depolama veya NAS'tan akış yapın, müzik ve video indirin, etiketleri düzenleyin ve ekolayzır ile çalma listesi araçlarıyla kaydı özelleştirin."
keywords: [
  "FLAC oynatıcı iPhone", "DSD ses oynatıcı iOS", "ALAC oynatıcı Mac", "çevrimdışı müzik oynatıcı iPhone", 
  "yüksek çözünürlüklü ses uygulaması iOS", "kayıpsız müzik oynatıcı", "NAS'tan müzik akışı", "bulut müzik oynatıcı", 
  "iPhone için video oynatıcı", "MP4 MKV oynatıcı Mac", "ses ekolayzır iOS", "meta veri etiketi düzenleyici iPhone", 
  "çoklu bulut dosya oynatıcı", "iTunes Dosya Paylaşım uygulaması", "CarPlay müzik uygulaması", 
  "AirPlay ve Chromecast desteği", "Mac müzik düzenleyici", "çalma listesi yöneticisi iOS"
]
tags: [
  "ses oynatıcı", "video oynatıcı", "FLAC desteği", "çevrimdışı oynatma", "bulut akışı", 
  "yüksek çözünürlüklü ses", "DSD ses", "iPhone uygulamaları", "Mac uygulamaları", "ses etiketi düzenleyici", 
  "medya kütüphanesi düzenleyici", "ekolayzır", "dosya yöneticisi", "NAS akışı", 
  "Chromecast", "AirPlay", "CarPlay", "çalma listesi oluşturma"
]
headless: false
aliases:
  - /home/
  - /index.php/
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
  let speedMultiplier = 1; // base speed
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

      star.y += star.velocity * speedMultiplier;
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

<!-- force dark theme for this page -->
{{< force-dark >}}

{{< rawhtml >}}

<style>
  .rocket-anim {
    cursor: pointer;
    transition: transform 0.6s ease-in;
    will-change: transform;
  }

  .rocket-launch {
    transform: translateY(-150vh) scale(1.2) rotate(-10deg);
    transition: transform 0.6s cubic-bezier(0.55, 0, 0.8, 0.2);
  }

  .rocket-return {
    animation: rocket-return 1.2s ease-out forwards;
  }

  @keyframes rocket-return {
    0% {
      transform: translateY(150vh) scale(0.9) rotate(15deg);
      opacity: 0;
    }
    30% {
      opacity: 0.5;
    }
    100% {
      transform: translateY(0) scale(1) rotate(0deg);
      opacity: 1;
    }
  }
</style>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    // Supports both <img> and lottie <div> with id or class 'rocket-anim'
    const rocket = document.querySelector('.rocket-anim img, .rocket-anim div[id^="lottie"]');
    if (!rocket) return;

    rocket.style.cursor = 'pointer';

    rocket.addEventListener('click', () => {
      rocket.classList.add('rocket-launch');
      speedMultiplier = 20;

      setTimeout(() => {
        rocket.classList.remove('rocket-launch');
        rocket.classList.add('rocket-return');
      }, 700);

      rocket.addEventListener('animationend', () => {
        rocket.classList.remove('rocket-return');
        speedMultiplier = 1;
      }, { once: true });
    });
  });
</script>

{{< /rawhtml >}}

<div class="rocket-anim hx:w-full">

{{< hextra/hero-container 
  lottie="/images/juicy-json/juicy-rocket.json" 
  lottieWidth="35%"
>}}

<div class="hx:mt-12"></div>

<div class="hx:flex hx:flex-col hx:items-center hx:justify-center hx:text-center hx:sm:block">

{{< hextra/hero-badge >}}
  <div class="hx:w-2 hx:h-2 hx:rounded-full hx:bg-primary-400"></div>
  <span>14 Milyon İndirme</span>
  {{< icon name="arrow-circle-right" attributes="height=14" >}}
{{< /hextra/hero-badge >}}

<div class="hx:mt-6 hx:mb-6">
{{< hextra/hero-headline >}}
 EVERAPPZ
{{< /hextra/hero-headline >}}
</div>

<div>
{{< hextra/hero-subtitle >}}
<strong>Verimliliğinizi artıran,&nbsp;<br class="hx:sm:block hx:hidden" />günlük görevlerinizi kolaylaştıran ve daha keyifli hale getiren uygulamalarımızı keşfedin.</strong>
{{< /hextra/hero-subtitle >}}
</div>

</div>

{{< /hextra/hero-container >}}

</div>

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{< hextra/feature-grid >}}

  {{< hextra/feature-card
    title="Sizin İçin Yapıldı. Sizin Tarafınızdan Geliştirildi."
    subtitle=`Tüm yorumları okuyoruz ve her güncellemeyi iyileştirmek için geri bildirimlerinizi kullanıyoruz.`
    icon="code"
    style="background: radial-gradient(circle at 50% 80%, rgba(99,102,241,0.15), transparent);"
  >}}

  {{< hextra/feature-card
    title="Performans Amaca Hizmet Eder."
    subtitle=`Gereksiz şişkinlik yok. Sadece temiz, kararlı ve önemli özelliklere sahip uygulamalar.`
    icon="presentation-chart-line"
    style="background: radial-gradient(circle at 50% 80%, rgba(236,72,153,0.15), transparent);"
  >}}

  {{< hextra/feature-card
    title="Gizlilik. Erişilebilirlik. Sadelik."
    subtitle=`Kullanımı kolay, tamamen erişilebilir ve gizliliğiniz düşünülerek tasarlanmış.`
    icon="shield-check"
    style="background: radial-gradient(circle at 50% 80%, rgba(16,185,129,0.15), transparent);"
  >}}

{{< /hextra/feature-grid >}}

</div>

<div class="hx:mt-12"></div>

<div class="hx:w-full">
{{< press-carousel >}}
</div>

<div class="hx:mt-12"></div>

{{< hextra/section-headline >}}
Ürünlerimiz
{{< /hextra/section-headline >}}

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{< cards cols="8">}}

  {{< card 
    link="/products/evervideo" 
    title="Evervideo" 
    tag="Yeni"
    subtitle="360° videolar oynatın, altyazılı izleyin, video ekolayzır kullanın, medyanızı çalma listeleriyle düzenleyin, çevrimdışı kullanım için video indirin ve iCloud'dan akış yapın." 
    image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
    method="Resize"
    options="200x q80 webp"
    imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"
  >}}

  {{< card 
    link="/products/evermusic"
    title="Evermusic" 
    tag="11 Milyon İndirme"
    subtitle="Çevrimdışı mod, ses ekolayzırı, crossfade, kesintisiz çalma, çalma listeleri, müzik kütüphanesi ve dosya yöneticisi ile bulut müzik çalar." 
    image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
    method="Resize"
    options="200x q80 webp"
    imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"
  >}}

  {{< card 
    link="/products/flacbox"
    title="Flacbox" 
    tag="1 Milyon İndirme"
    subtitle="iPhone ve Mac için Hi-Res ses oynatıcı. Müziğinizi kayıpsız ses formatlarında dinleyin: flac, alac, ape, wv, dsd ve daha fazlası. Gelişmiş ses çıkış ayarlarını etkinleştirin." 
    image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
    method="Resize"
    options="200x q80 webp"
    imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"
  >}}

  {{< card 
    link="/products/evertag"
    title="Evertag" 
    subtitle="Otomatik düzeltme ve toplu iş modu ile müzik etiket düzenleyici. Eksik meta verileri bulun, albüm kapaklarını düzenleyin. ID3 / FLAC / APE düzenleyin. 120'den fazla etiket desteklenir." 
    image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
    method="Resize"
    options="200x q80 webp"
    imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"
  >}}

{{< /cards >}}

</div>

<div class="hx:mt-6"></div>

{{< hextra/section-headline >}}
App Store Yorumları
{{< /hextra/section-headline >}}

<div class="hx:mt-6"></div>

<div class="hx:w-full">
{{< appstore-reviews apps="1097564256,1594027432,885367198,1564384601,1450763230,1594027661" stars="5,4" >}}
</div>

<div class="hx:mt-6"></div>

{{< hextra/section-headline >}}
Abone Ol
{{< /hextra/section-headline >}}

<div class="hx:mt-6"></div>

<div class="hx:w-full hx:text-center">

{{< hextra/hero-paragraph >}}
Everappz ekibinden en son haberleri ve özel fırsatları alan kişilere katılın.  
En son haberler ve uygulama güncellemeleri için bizi sosyal medyada takip etmeyi unutmayın.  
Abone olarak [Gizlilik Politikamızı](/legal/privacy-policy) kabul eder ve [Şartlar ve Koşulları](/legal/terms-and-conditions/) onaylarsınız.
{{< /hextra/hero-paragraph >}}

</div>

<div class="hx:mt-6"></div>

<div class="hx:w-full hx:text-center">

{{< rawhtml >}}

<form action="https://everappz.us10.list-manage.com/subscribe/post?u=f758cdf6a38df2a75513ac5f1&amp;id=2373740226" 
method="post" 
id="mc-embedded-subscribe-form" 
name="mc-embedded-subscribe-form" 
class="validate" 
target="_blank" 
novalidate
>

<!-- style from shortcodes/card -->
<input
  type="email"
  placeholder="E-posta Girin"
  value=""
  name="EMAIL"
  id="mce-EMAIL"
  required
  class="email
    hx:rounded-full
    hx:border hx:border-gray-200 hx:dark:border-neutral-800
    hx:hover:border-gray-300 hx:dark:hover:border-neutral-700
    hx:bg-transparent
    hx:font-normal
    hx:text-gray-700 hx:dark:text-neutral-200
    hx:px-4 hx:py-3"
style="height: 50px; width: 300px; margin-bottom:1rem; margin-right:1rem; outline: none; box-shadow: none;"
id="mce-EMAIL" 
required
>

<div 
style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_f758cdf6a38df2a75513ac5f1_2373740226" tabindex="-1" value=""></div>

<!-- style from hextra/hero-button -->
<button type="submit"
class="not-prose hx:font-bold hx:cursor-pointer hx:px-6 hx:py-3 hx:rounded-full hx:text-center hx:text-white hx:inline-flex hx:items-center hx:gap-2 hx:bg-primary-600 hx:hover:bg-primary-700 hx:focus:outline-hidden hx:focus:ring-4 hx:focus:ring-primary-300 hx:dark:bg-primary-600 hx:dark:hover:bg-primary-700 hx:dark:focus:ring-primary-800 hx:transition-all hx:ease-in hx:duration-200" 
style="outline: none; box-shadow: none;">Abone Ol</button>

{{< /rawhtml >}}

</div>

<div class="hx:mt-6"></div>
