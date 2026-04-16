---
date: '2025-06-12T17:00:00+00:00'
draft: false
title: '首页'
layout: hextra-home
description: "探索适用于 iPhone 和 Mac 的 Everappz 应用：播放 FLAC、DSD、APE 和 ALAC，从云存储或 NAS 流式传输，下载音乐和视频，编辑标签，并使用均衡器和播放列表工具自定义播放。"
keywords: [
  "FLAC 播放器 iPhone", "DSD 音频播放器 iOS", "ALAC 播放器 Mac", "离线音乐播放器 iPhone", 
  "高解析音频应用 iOS", "无损音乐播放器", "从 NAS 串流音乐", "云音乐播放器", 
  "iPhone 视频播放器", "MP4 MKV 播放器 Mac", "音频均衡器 iOS", "元数据标签编辑器 iPhone", 
  "多云文件播放器", "iTunes 文件共享应用", "CarPlay 音乐应用", 
  "AirPlay 和 Chromecast 支持", "Mac 音乐管理器", "播放列表管理器 iOS"
]
tags: [
  "音频播放器", "视频播放器", "FLAC 支持", "离线播放", "云端串流", 
  "高解析音频", "DSD 音频", "iPhone 应用", "Mac 应用", "音频标签编辑器", 
  "媒体库管理器", "均衡器", "文件管理器", "NAS 串流", 
  "Chromecast", "AirPlay", "CarPlay", "创建播放列表"
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
  <span>全球 1400 万次下载</span>
  {{< icon name="arrow-circle-right" attributes="height=14" >}}
{{< /hextra/hero-badge >}}

<div class="hx:mt-6 hx:mb-6">
{{< hextra/hero-headline >}}
 EVERAPPZ
{{< /hextra/hero-headline >}}
</div>

<div>
{{< hextra/hero-subtitle >}}
<strong>探索我们提升生产力的应用，&nbsp;<br class="hx:sm:block hx:hidden" />让日常任务更轻松、更愉快。</strong>
{{< /hextra/hero-subtitle >}}
</div>

</div>

{{< /hextra/hero-container >}}

</div>

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{< hextra/feature-grid >}}

  {{< hextra/feature-card
    title="为你打造，因你改进。"
    subtitle=`我们阅读所有评论，并利用您的反馈来改进每次更新。`
    icon="code"
    style="background: radial-gradient(circle at 50% 80%, rgba(99,102,241,0.15), transparent);"
  >}}

  {{< hextra/feature-card
    title="性能服务于目标。"
    subtitle=`没有臃肿。只有干净、稳定且功能实用的应用。`
    icon="presentation-chart-line"
    style="background: radial-gradient(circle at 50% 80%, rgba(236,72,153,0.15), transparent);"
  >}}

  {{< hextra/feature-card
    title="隐私。无障碍。简洁。"
    subtitle=`易于使用，完全无障碍，并在设计中充分考虑您的隐私。`
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
我们的产品
{{< /hextra/section-headline >}}

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{< cards cols="8">}}

  {{< card 
    link="/products/evervideo" 
    title="Evervideo" 
    tag="新品"
    subtitle="播放 360° 视频，观看带字幕的视频，使用视频均衡器，通过播放列表管理媒体，下载视频以供离线使用，并从 iCloud 流式传输。" 
    image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
    method="Resize"
    options="200x q80 webp"
    imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"
  >}}

  {{< card 
    link="/products/evermusic"
    title="Evermusic" 
    tag="全球 1100 万次下载"
    subtitle="云音乐播放器，支持离线模式、音频均衡器、交叉淡入淡出、无缝播放、播放列表、音乐库、文件管理器。" 
    image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
    method="Resize"
    options="200x q80 webp"
    imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"
  >}}

  {{< card 
    link="/products/flacbox"
    title="Flacbox" 
    tag="全球 100 万次下载"
    subtitle="适用于 iPhone 和 Mac 的 Hi-Res 音频播放器。以无损音频格式收听音乐：flac、alac、ape、wv、dsd 等。启用高级音频输出设置。" 
    image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
    method="Resize"
    options="200x q80 webp"
    imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"
  >}}

  {{< card 
    link="/products/evertag"
    title="Evertag" 
    subtitle="音乐标签编辑器，支持自动更正和批量模式。查找缺失的元数据，编辑专辑封面。编辑 ID3 / FLAC / APE。支持超过 120 种标签。" 
    image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
    method="Resize"
    options="200x q80 webp"
    imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"
  >}}

{{< /cards >}}

</div>

<div class="hx:mt-6"></div>

{{< hextra/section-headline >}}
App Store 评论
{{< /hextra/section-headline >}}

<div class="hx:mt-6"></div>

<div class="hx:w-full">
{{< appstore-reviews apps="1097564256,1594027432,885367198,1564384601,1450763230,1594027661" stars="5,4" >}}
</div>

<div class="hx:mt-6"></div>

{{< hextra/section-headline >}}
订阅
{{< /hextra/section-headline >}}

<div class="hx:mt-6"></div>

<div class="hx:w-full hx:text-center">

{{< hextra/hero-paragraph >}}
加入获取 Everappz 团队最新消息和独家优惠的用户行列。  
别忘了在社交媒体上关注我们，获取应用的最新消息和更新。  
订阅即表示您同意我们的[隐私政策](/legal/privacy-policy)并接受[条款和条件](/legal/terms-and-conditions/)。
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
  placeholder="输入邮箱"
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
style="outline: none; box-shadow: none;">订阅</button>

{{< /rawhtml >}}

</div>

<div class="hx:mt-6"></div>
