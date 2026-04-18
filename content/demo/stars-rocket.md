---
title: 'Stars Background & Rocket Animation Demo'
date: '2026-04-18T00:00:00+00:00'
draft: false
layout: hextra-home
build:
  list: never
  render: always
  publishResources: true
sitemap:
  disable: true
---

{{< stars-background >}}

{{< force-dark >}}

{{< rocket-animation >}}

<div class="rocket-anim hx:w-full">

{{< hextra/hero-container 
  lottie="/images/juicy-json/juicy-rocket.json" 
  lottieWidth="35%"
>}}

<div class="hx:mt-12"></div>

<div class="hx:flex hx:flex-col hx:items-center hx:justify-center hx:text-center hx:sm:block">

{{< hextra/hero-badge >}}
  <div class="hx:w-2 hx:h-2 hx:rounded-full hx:bg-primary-400"></div>
  <span>Stars & Rocket Demo</span>
  {{< icon name="arrow-circle-right" attributes="height=14" >}}
{{< /hextra/hero-badge >}}

<div class="hx:mt-6 hx:mb-6">
{{< hextra/hero-headline >}}
 Tap the Rocket
{{< /hextra/hero-headline >}}
</div>

<div>
{{< hextra/hero-subtitle >}}
<strong>Click the rocket to launch it and watch the stars accelerate.</strong>
{{< /hextra/hero-subtitle >}}
</div>

</div>

{{< /hextra/hero-container >}}

</div>
