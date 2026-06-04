---
title: "Medya Oynatıcı"
date: 2020-02-01
lastmod: 2026-06-01
description: "iPhone, iPad ve Mac'te Evervideo medya oynatıcısını nasıl kullanacağınızı öğrenin. Picture-in-Picture, donanım hızlandırmalı H.264 / HEVC kod çözme, ses ve video ekolayzerler, birincil ve ikincil altyazılar, ses ve video parça seçimi, video ölçekleme ve döndürme, oynatma hızı, uyku zamanlayıcısı, AirPlay 2, Google Chromecast, RTSP akışları ve kompakt her zaman görünür oynatıcı."
keywords: [
  "Evervideo oynatıcı rehberi", "video oynatıcı ayarları", "Evervideo ekolayzer",
  "Picture-in-Picture iPhone", "PiP video iPad", "PiP video Mac",
  "AirPlay 2 video", "Google Chromecast video",
  "video altyazı iPhone", "harici SRT altyazılar",
  "ASS SSA altyazı oynatıcı", "libass iOS",
  "dil öğrenmek için çift altyazı",
  "video ekolayzer parlaklık kontrast", "ses ekolayzer video oynatıcı",
  "video oynatıcı döndürme kilidi", "video ölçekleme modu iOS",
  "donanım H.264 kod çözücü iPhone", "donanım HEVC kod çözücü iPad",
  "oynatma hızı video", "FFmpeg video oynatıcı iOS",
  "RTSP iPhone oynatıcı", "kompakt video oynatıcı",
  "VR 360 video oynatıcı iPhone"
]
tags: ["rehber", "evervideo", "oynatıcı", "PiP", "altyazılar", "video ekolayzer"]
readingTime: 14
---


Medya Oynatıcı, oynatmayı kontrol ettiğiniz ve Evervideo'nun özelliklerinin çoğuna eriştiğiniz uygulamanın ana ekranıdır. Hem video hem de ses dosyalarını oynatır ve ağır işleri yapan donanım hızlandırmalı H.264 ve HEVC kod çözme ile özel FFmpeg tabanlı bir oynatıcı üzerine kurulmuştur. Nasıl kullanılacağını keşfedelim.

## Medya Oynatıcıya Erişim

Tam ekran oynatıcıya kompakt oynatıcı çubuğundan ulaşabilirsiniz. iPhone'da, kompakt oynatıcı ana ekranın üst kısmında bulunur. iPad ve Mac'te, sol taraftadır (veya ana panelinın üstünde). Tam ekran oynatıcıyı kompakt görünüme geri daraltmak için sağ alt köşedeki kapat düğmesine dokunun veya aşağı kaydırın. Kompakt oynatıcıyı tamamen gizlemek için bir kez daha dokunun ve aşağı kaydırın.

Kitaplığınıza, dosya yöneticinize veya ayarlarınıza göz atarken kompakt oynatıcı görünür kalır; böylece bir sonrakini ararken asla videonuzu kaybetmezsiniz.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo tam ekran medya oynatıcı" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Desteklenen Video ve Ses Formatları

Evervideo, desteklenen cihazlarda donanım hızlandırmalı H.264 ve HEVC kod çözme ile paketlenmiş FFmpeg motoru aracılığıyla pratik olarak her modern kap ve codec'i oynatır.

- **Video kaplar:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — ve çok daha fazlası.
- **Video kodekar:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — artı FFmpeg'in desteklediği pratik olarak her diğer kodek.
- **Ses kodekar:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — ve çok daha fazlası.
- **Altyazı formatları:** SRT, VTT (WebVTT), ASS / SSA ve gömülü metin veya görüntü altyazı parçaları.
- **Yayın protokolleri:** HTTP / HTTPS, HLS (m3u8), RTSP (IP kameraları ve IPTV) ve SMB / WebDAV / FTP / SFTP / NFS / DLNA üzerinden doğrudan dosya akışı.

Bu, MKV kopyalar, güvenlik kamerası RTSP akışları ve AV1 webm web indirmeleri dahil karşılaşabileceğiniz pratik olarak her video dosyasını kapsar.

## Oynatma Kontrolleri

Oynatıcı ekranının altında Oynat, Duraklat, Sonraki ve Önceki düğmeleri görürsünüz. Uygulama ayarlarından etkinleştirebileceğiniz İleri Atla ve Geri Atla (varsayılan 10 saniye) gibi isteğe bağlı düğmeler de vardır. Hızlı ilerleme veya geri sarma için Sonraki / Önceki düğmelerine basılı tutun. Herhangi bir konuma atlamak için oynatma kaydırıcısını sürükleyin.

## Tekrar ve Karıştır

Tekrar düğmesine dokunarak tekrar modları arasında geçiş yapın:

- **Tümünü Tekrarla** — kuyruğunuzdaki her videoyu döngüye alır.
- **Birini Tekrarla** — yalnızca mevcut videoyu tekrarlar.
- **Tekrar Durdur** — mevcut video bittiğinde duraklar.
- **Tekrarsız** — kuyruğu tekrarlamadan bir kez oynatır.

Kuyruktaki videoların sırasını rastgele yapmak için **Karıştır** düğmesini kullanın.

## Picture-in-Picture (PiP)

iPhone ve iPad'de Evervideo, Picture-in-Picture'ı (PiP) tam olarak destekler. Oynatıcı ekranındaki PiP simgesine dokunun veya Evervideo'yu arka plana geçirin — video her uygulamanın üzerinde kayan bir pencerede oynatılmaya devam eder. Kayan pencereyi herhangi bir köşeye sürükleyin; yeniden boyutlandırmak için sıkıştırın; temel oynat / duraklat / atla kontrollerini görmek için bir kez dokunun; tam Evervideo'ya dönmek için küçük genişletme düğmesine dokunun.

PiP, Evervideo'nun oynadığı her video formatıyla çalışır; bulut akışlı dosyalar ve RTSP akışları dahil. PiP ayrıca telefonunuz kilitliyken de çalışmaya devam eder (Auto-Lock ayarınıza bağlı olarak).

## Kompakt Oynatıcı

Kompakt oynatıcı, kütüphaneye, dosya yöneticinize veya ayarlara göz atarken uygulamadaki her ekranın üst kısmında görünür kalan kalıcı bir mini oynatıcıdır. Tam ekran oynatıcıya genişletmek için dokunun; tekrar daraltmak için aşağı kaydırın.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo ana ekranda kompakt oynatıcı görünümünden video ayarları" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

AirPlay için oynatıcıdaki AirPlay düğmesine dokunun. Evervideo, AirPlay 2'yi destekler; böylece Apple TV, HomePod veya AirPlay 2 uyumlu herhangi bir hoparlöre veya akıllı TV'ye video akışı yapabilirsiniz. Birden fazla AirPlay cihazı olan bir kurulumda, sesi aynı anda birden fazla alıcıya yönlendirebilirsiniz.

## Google Chromecast

Google Cast kullanıcıları için Cast simgesi oynatıcıda görünür. Bir cihaz seçmek ve yayın başlatmak için dokunun. Telefonunuzun ve Cast alıcısının aynı Wi-Fi ağında olduğundan emin olun. Chromecast donanımı tarafından desteklenmeyen bazı codec'ler olabilir — bazı dosyaların kodlama dönüşümüne ihtiyacı olabilir.

## RTSP Canlı Akışları

Evervideo, RTSP kaynaklarını doğrudan oynatabilir — IP kameraları, zil kameraları, IPTV akışları, yayın beslemeleri ve herhangi bir `rtsp://` URL'si. Akışı Dosyalar → Çevrimiçi Bağlantılar → Bağlantı ekle seçeneğinden RTSP bağlantısı olarak ekleyin, ardından izlemeye başlamak için dokunun. RTSP akışları Picture-in-Picture'da, kompakt oynatıcıda çalışır ve düzenli bir video gibi AirPlay 2 ve Chromecast üzerinden yayın yapar.

## Ses Parçası Seçimi

Birden fazla ses parçası olan videolar için (yorum, alternatif dil dublajları, yönetmen parçaları), oynatıcıdaki Daha fazla eylem düğmesine dokunun ve Ses Parçası'nı seçin — ardından istediğiniz parçayı seçin. Bu, yabancı dil filmleri, birden fazla dublajlı BDMV / MKV dosyaları ve yorum parçalı öğretici içerikler için gereklidir.

## Video Parçası Seçimi

Bazı video dosyaları birden fazla video akışı içerir (çok açılı Blu-ray'ler, alternatif kurgular). Oynatma sırasında aralarında geçiş yapmak için Daha fazla eylem menüsünden Video Parçası'nı seçin.

## Altyazılar — Dahili ve Harici

Evervideo size altyazılar üzerinde ince taneli kontrol verir:

- **Altyazı parçası** — dosyaya gömülü parçalardan seçin.
- **Harici altyazı dosyaları** — cihazınızdan, iCloud Drive'dan veya bağlı herhangi bir bulut hizmetinden `.srt`, `.vtt`, `.ass` veya `.ssa` dosyalarını yükleyin.
- **Libass rendering** — gelişmiş ASS / SSA stillendirme (yazı tipleri, renkler, konumlar, karaoke efektleri) paketlenmiş libass sayesinde doğru şekilde işlenir.
- **Yazı tipi seçimi** — birincil altyazılar için özel bir yazı tipi ve ikincil altyazılar için ayrı bir yazı tipi seçin. Paketlenmiş yazı tipleri artı cihazınıza yüklü herhangi bir yazı tipi mevcuttur.

Tüm bunları oynatmadan önce Ayarlar → Altyazılar'dan yapılandırabilir ya da anında değiştirmek için oynatıcıdan Daha fazla eylem → Altyazılar'ı kullanabilirsiniz.

## Ses Ekolayzer

Evervideo, video ses parçalarını kulaklıklarınız, hoparlörleriniz veya hi-fi kurulumunuz için ayarlamak amacıyla tam bir ses ekolayzer içerir. Ses görünümündeki ekolayzer simgesine dokunun (veya oynatıcı Daha fazla eylem menüsündeki Ses Ekolayzer eylemine), sağ üst köşedeki anahtarla ekolayzerı açın ve ya bir ön ayar seçin ya da kendi ön ayarınızı oluşturmak için bant kaydırıcıları sürükleyin. Özel ön ayarlar, cihazlar arasında paylaşmak veya yedeklemek için dışa ve içe aktarılabilir.

## Video Ekolayzer

Görüntüyü ayarlamak için Evervideo, özel bir video ekolayzer sağlar — oynatma sırasında gerçek zamanlı olarak parlaklık, kontrast, doygunluk ve tonu ayarlayın. Ses ekolayzerı gibi, özel video ön ayarları da paylaşım veya yedekleme için dışa ve içe aktarılabilir. Güneşli bir günde karanlık bir sahneyi aydınlatmak, soluk içerikteki doygunluğu artırmak veya soğuk renk kaymasını ısıtmak için kullanın.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo video ekolayzer" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Video Ölçekleme Modu

Videonun ekranı nasıl dolduracağını seçin:

- **Sığdır** — orijinal en boy oranını koru; gerektiğinde siyah çubuklar.
- **Doldur** — gerekirse videoyu kırparak tüm ekranı doldur.
- **Gererek genişlet** — gerekirse bozarak videoyu ekranı dolduracak şekilde gererek genişlet.
- **Orijinal** — yerel çözünürlüğü 1:1'de koru.

## Video Döndürme

Yanlış yönlendirmeyle kaydedilmiş videolar için **Daha fazla eylem → Döndürme** seçeneğini seçin ve oynatıcıdan ayrılmadan resmi döndürmek için **0°**, **90°**, **180°** veya **270°** seçin.

## Donanım Kod Çözme (H.264 ve HEVC)

Ayarlar → Oynatıcı → Video'da, Donanım Çöz H.264 ve Donanım Çöz H.265 (HEVC)'yi bağımsız olarak etkinleştirebilir / devre dışı bırakabilirsiniz. Donanım kod çözme daha hızlıdır, daha az batarya kullanır ve daha serin çalışır — ancak nadir durumlarda (bozuk dosyalar, egzotik profiller) donanım kod çözmeyi devre dışı bırakmanız ve yazılım FFmpeg kod çözmeye geçmeniz gerekebilir. Evervideo bunu oynatıcı Daha fazla eylem menüsünden dosya bazında yapmanıza izin verir.

## VR 360° Görüntü Alanı

Evervideo, küresel video dosyaları için bir VR / 360° görüntü alanı içerir. 360° video oynatırken etrafına bakmak için sürükleyebilir, yakınlaştırmak için sıkıştırabilirsiniz ve Evervideo işlemeyi gerçek zamanlı olarak bozar.

## Oynatma Hızı

Oynatma hızını değiştirmek için oynatıcı araç çubuğundaki Hız kontrolüne dokunun — analiz için yavaşlatın (0,25× veya 0,5×) veya öğreticiler ve dersler için hızlandırın (1,25×, 1,5×, 2× ve 3×'e kadar). Daha ince ayarlamalar için hassas moda geçmek üzere Hız ekranının sağ üst köşesindeki yapılandırma simgesine dokunun. Parça başına perde düzeltmesi de mevcuttur.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo ana araç çubuğundaki oynatma hızı" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Oynatıcı Kuyruğu

Oynatıcı kuyruğunuzu görmek için oynatıcıdaki kuyruk düğmesine dokunun. Kuyruktaki her videonun daha fazla eylemi vardır — bunları görüntülemek için üç noktaya dokunun. Kuyruktaki bir videoyu yeniden sıralamak için başlığın yanındaki yeniden sıralama göstergesini kullanın ve yeni bir konuma sürükleyin.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo oynatma kuyruğu" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Uyku Zamanlayıcısı

Ayarlar → Oynatıcı → Uyku Zamanlayıcısı'nı açın, açık konuma getirin ve oynatmanın otomatik olarak durmadan önce ne kadar süre devam etmesini istediğinizi seçin. Ayrıca Ayarlar → Oynatıcı → Kişiselleştirme → Ana Ekran Eylemleri aracılığıyla Uyku Zamanlayıcısı düğmesini doğrudan ana oynatıcı ekranına ekleyebilirsiniz.

## Oynatıcı Yer İmleri

Uzun videolarda yerinizi kaydedin — dersler, video üzerindeki sesli kitaplar, öğreticiler, saatlik YouTube indirmeleri — Daha fazla eylem menüsünden Yer İmi Ekle'ye dokunarak. Yer imleri videonun Daha fazla eylem → Yer İmleri listesinde görünür ve oturumlar arasında devam eder.

## Daha Fazla Eylem Menüsü

Ek işlevlere erişmek için oynatıcıdaki **Daha fazla eylem "..."** düğmesine dokunun.

- **Oynatmaya Devam Et** — kuyruğu son konumdan devam ettirin.
- **Ara** — kuyruğunuzda belirli bir videoyu bulun.
- **Yer İmleri** — yer imlerini görüntüleyin ve atlayın.
- **Hız** — oynatma hızını ayarlayın.
- **Sonlar** — son oynatılan videolar.
- **Favoriler** — favori olarak işaretlenmiş videolar.
- **Ses Ekolayzer** — ses ekolayzerı etkinleştirin.
- **Video Ekolayzer** — video ekolayzerı etkinleştirin.
- **Ses Parçası** — ses akışını seçin.
- **Video Parçası** — video akışını seçin.
- **Altyazılar** — birincil / ikincil parça, harici dosya, yazı tipi.
- **Döndürme** — resmi 0° / 90° / 180° / 270° döndürün.
- **Ölçekleme Modu** — Sığdır / Doldur / Gererek genişlet / Orijinal.
- **Picture-in-Picture** — PiP moduna girin.
- **AirPlay** / **Chromecast** — bir cihaza gönderin.
- **Uyku Zamanlayıcısı** — oynatmayı durdurmak için bir zamanlayıcı ayarlayın.
- **Kuyruğu Oynatma Listesine Kaydet** — mevcut kuyruğu yeni bir oynatma listesi olarak kaydedin.
- **Kuyruğu Sil** — kuyruğu temizleyin ve oynatmayı durdurun.
- **Ayarlar** — doğrudan oynatıcı ayarlarına atlayın.
- **Yardım** — rehberlik açın.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo oynatıcı Daha Fazla Eylem ekranı" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Oynatıcı Ayarları

Oynatıcının tam ayarlar ağacı [Ayarlar rehberinde](/docs/guide/evervideo/evervideo-guide-settings/) belgelenmiştir. En çok kullanılan bölümler:

- **Genel** — Tekrar modu, Karıştır modu, Oynatıcı Durumunu Kaydet, Oynatma Konumunu Kaydet, Atlama süresi aralıkları.
- **Video** — Donanım kod çöz H.264 / HEVC, video ekolayzer, ölçekleme modu, döndürme, görüntüleme modu, tercih edilen FPS, tercih edilen piksel formatı, VR görüntü alanı.
- **Ses** — Ses ekolayzer, örnekleme hızı, kanallar, IO tampon süresi, karma mod.
- **Altyazılar** — Birincil / ikincil parça, harici dosya seçimi, yazı tipi, ikincil yazı tipi.
- **Cihazlar** (iOS) — AirPlay / Chromecast.
- **Kişiselleştirme** — Oynatıcı düzen stili (Minimal / Alt / Antik / Klasik), ana ekran eylemleri, kilit ekranı kontrolleri.
- **Oynatma Önbelleği** — daha düzgün akış için disk önbelleği.
- **Uyku Zamanlayıcısı** — otomatik durdurma.

## Erişilebilirlik

Evervideo, VoiceOver ile tamamen erişilebilirdir. Her bileşenin iyi tasarlanmış bir etiketi ve açıklaması vardır. VoiceOver etkin olduğunda, uygulama Metin Moduna geçer; böylece yalnızca anlamlı öğeler gösterilir — bu da gezinme hızını ve netliği artırır. Metin Modunu Ayarlar → Erişilebilirlik → Metin Modu'ndan da etkinleştirebilirsiniz.

### VoiceOver ile Kaydırıcıları Ayarlama

1. **Kaydırıcıyı seçin** — VoiceOver onu ilan edene kadar sola veya sağa kaydırın.
2. **Değeri ayarlayın** — kaydırıcıya çift dokunun ve basılı tutun, ardından değeri hızlıca değiştirmek için yukarı veya aşağı sürükleyin. VoiceOver ilerledikçe yeni değeri ilan eder.

Diğer bileşenler, sistem tarafından sağlanan VoiceOver kalıplarını kullanarak beklendiği gibi çalışır.
