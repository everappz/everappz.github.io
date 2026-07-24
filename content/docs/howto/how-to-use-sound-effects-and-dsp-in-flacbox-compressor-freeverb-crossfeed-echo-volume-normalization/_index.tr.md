---
title: "Flacbox'ta Ses Efektleri ve DSP Nasıl Kullanılır: Compressor, Freeverb, Crossfeed, Echo, Ses Normalizasyonu ve daha fazlası"
date: 2026-07-24
description: "iPhone, iPad ve Mac'te Flacbox sesi için eksiksiz rehber. BASS motorunun nasıl çalıştığını, hangi ek formatları (MOD ve tracker müziği ile DSD dahil) çaldığını ve her efektin, her sürgünün ve her ön ayarın sesinize tam olarak ne yaptığını, ayrıca 10 bantlı ekolayzeri ve özel DSP zincirini öğrenin."
keywords: ["Flacbox ses efektleri", "Flacbox ön ayarları açıklaması", "Flacbox BASS motoru", "BASS ses kütüphanesi iOS", "MOD müzik çalar iPhone", "tracker müzik çalar iOS", "MOD XM IT S3M çal iPhone", "DSD çalar iOS", "FLAC çalar iPhone", "kayıpsız müzik çalar iOS", "Flacbox ekolayzer ön ayarları", "10 bantlı ekolayzer iPhone", "ses normalizasyonu iPhone", "EBU R128 iOS", "ses düzeyi normalizasyonu müzik çalar", "kulaklık crossfeed iOS", "bs2b crossfeed", "compressor ön ayarları müzik çalar", "freeverb reverb iOS", "echo gecikme müzik çalar", "DSP zinciri müzik çalar", "bas artırma iPhone", "Flacbox ile müziğe efekt ekleme", "en iyi ekolayzer ayarları iPhone"]
tags: ["Flacbox", "Ses Efektleri", "Nasıl Yapılır", "BASS", "Ekolayzer", "Bas Artırma", "Compressor", "Freeverb", "Crossfeed", "Echo", "Ses Normalizasyonu", "EBU R128", "MOD Müzik", "Tracker Müzik", "DSD", "FLAC", "DSP", "Kulaklık", "Ön Ayarlar"]
readingTime: 30
---

{{< author-byline >}}

**Kısa cevap:** Flacbox'ta **Ayarlar > Ses çalar** içinde bir **Oynatma motoru** seçersiniz: **Standard** (Apple'ın sistem motoru), **Universal** (FFmpeg motoru) veya **Sound FX** (**BASS™ motoru**). Seçtiğiniz motor hangi dosya formatlarının çalacağına karar verir, bu yüzden seçim önemlidir. **Sound FX** motoru, çoğu iPhone uygulamasının atladığı ek formatları çalar (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus ve MOD, XM, IT ve S3M gibi eski **MOD ve tracker müziği**) ve ses araçlarını çalıştıran tek motordur: **10 bantlı ekolayzer**, **Ses Normalizasyonu**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed** ve kendi kendinize kurduğunuz bir **DSP zinciri**. Yani bu rehberdeki efektleri kullanmak için önce Oynatma motorunuzu **Sound FX** olarak ayarlayın. Her aracın hazır **ön ayarları** vardır. Bunları **Ayarlar > Ses çalar** içinde açın (Ses efektleri, Ses ekolayzeri, Sinyal işleme) veya çalarda **⋯ (Daha fazla eylem)** düğmesine dokunup **Ses efektleri**'ni seçin. Burada yaptığınız hiçbir şey dosyalarınızı asla değiştirmez.

> Aşağıdaki sürgü ve ön ayar açıklamaları, Flacbox'ın uygulama içinde size gösterdiği kısa açıklamaların aynısıdır ve dokunmadan önce tam bir resim elde etmeniz için biraz ek arka plan bilgisiyle harmanlanmıştır.

## Bu Rehber Nasıl Okunur

Her araç aynı şekilde çalışır:

1. **Açın.** Her efektin kendi açma/kapama düğmesi vardır. Başlangıçta hepsi kapalıdır. Aynı anda istediğiniz kadar efekti açabilirsiniz.
2. **Bir ön ayar seçin.** Ön ayar, hazır bir ayardır. Birine dokunun ve ses hemen değişir. Bu rehber **her** ön ayarın ne yaptığını listeler.
3. **İnce ayar (isteğe bağlı).** Sürgüleri açıp elle ayarlayın. Bir sürgüyü hareket ettirdiğiniz an efekt **Manual** gösterir, böylece ön ayardan ayrıldığınızı bilirsiniz. Her sürgünün bir sıfırlama düğmesi vardır.

Dosyalarınıza hiçbir şey kaydedilmez. Bunlar canlı efektlerdir. Bir efekti kapatın ve orijinal sesiniz anında geri gelir.

## Oynatma Motorunuzu Seçin (Efektler Sound FX'te)

Flacbox motorları birbirine karıştırmaz. **Ayarlar > Ses çalar > Oynatma motoru** içinde **bir** tane seçersiniz ve seçtiğiniz motor hangi dosya formatlarını çalabileceğinize ve efektlerin kullanılabilir olup olmayacağına karar verir. Uygulamada tam olarak bu adlarla gösterilen üç seçenek vardır:

1. **Standard.** Apple'ın yerleşik sistem motoru. Daha düşük pil kullanımı için donanım kod çözme kullanır.
2. **Universal.** Çok geniş bir format yelpazesini açan FFmpeg motoru.
3. **Sound FX.** **BASS™ motoru**. Kayıpsız ve yüksek çözünürlüklü dosyaları tam doğrulukla çalar, modül (tracker) müziği ekler ve bu rehberdeki her efekti, 10 bantlı ekolayzeri ve DSP zincirini çalıştırır.

Her motor kendi format setini desteklediğinden, çalabileceğiniz dosyalar seçtiğiniz motorla değişir. Daha da önemlisi, efektler, ekolayzer ve DSP zinciri **yalnızca** **Sound FX** motoruyla çalışır, bu yüzden bunları kullanmak istiyorsanız önce onu seçin.

Sound FX, Un4seen Developments'ın profesyonel bir ses kütüphanesi olan **BASS™** üzerine kuruludur. Ana sayfasında daha fazla bilgiye ulaşabilirsiniz: [un4seen.com](https://www.un4seen.com/).

## Müzik Formatları: Sound FX (BASS™) Motorunun Eklediği Formatlar (MOD ve Tracker Müziği Dahil)

**Sound FX (BASS™)** motoru seçiliyken Flacbox, günlük formatların üstüne aşağıdaki özel formatları çalar. En özeli **modül müziği**dir, ayrıca **tracker müziği** olarak da adlandırılır. Bir modül dosyası normal bir kayıt değildir. Küçük enstrüman sesleri ile bunların nasıl çalınacağını söyleyen bir "partisyon" içerir ve Flacbox şarkıyı bu partisyondan, bu dosyaların çalınması gereken şekilde canlı olarak yeniden oluşturur. Normal çalarlar bunu yapamaz.

| Müzik türü | Formatlar | Bilmekte fayda var |
|---|---|---|
| **Modül / tracker müziği** | MOD, XM, IT, S3M, MTM, UMX, MO3 | BASS™ modül çalar tarafından canlı olarak yeniden oluşturulur. Chiptune ve eski demoscene veya Amiga şarkıları için harika. |
| **Modern kayıpsız** | FLAC | Tam kalite, WAV'dan daha küçük. |
| **Diğer kayıpsız** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Daha az yaygın kayıpsız türler, hepsi destekleniyor. |
| **Yüksek çözünürlüklü DSD** | DSF, DFF | DSD over PCM kullanarak normal donanımda çalar. |
| **Modern kayıplı** | Opus, Ogg Vorbis, MP3 | Her zamanki akış ve indirme türleri. |

Sound FX motoru ayrıca ana akım Apple formatlarını (AAC, ALAC, M4A, WAV, AIFF) ve canlı yayınları da çalar, böylece efektler ve ekolayzer bunlarda da çalışır.

**Bu size neden yardımcı olur:** FLAC albümleri, DSD yüksek çözünürlüklü dosyalar ve eski MOD veya XM tracker şarkılarından oluşan bir klasör karışımınız varsa, Flacbox hepsini çalar ve ekolayzer ile efektler her birinde çalışır.

## Kullanacağınız Üç Menü

Flacbox ses araçlarını hepsi ses çalar ayarlarının içinde olan üç yerde tutar. Önce **Oynatma motorunuzun** **Sound FX** olarak ayarlandığından emin olun (Ayarlar > Ses çalar > Oynatma motoru), çünkü efektler, ekolayzer ve DSP zinciri yalnızca o motorla kullanılabilir.

- **Ses efektleri** (efekt rafı): çaları açın, **⋯ (Daha fazla eylem)**'e dokunun, **Ses efektleri**'ne dokunun. Veya **Ayarlar > Ses çalar > Ses efektleri**'ne gidin.
- **Ses ekolayzeri** (10 bant ve ön ayarlar): **Ayarlar > Ses çalar > Ses ekolayzeri**.
- **Sinyal işleme** (kendi DSP zinciriniz): **Ayarlar > Ses çalar > Sinyal işleme**.

Ayrıca **Ayarlar > Ses çalar** altında **çıkış örnekleme hızını**, **kanalları** ve **arabellek boyutunu** da ayarlayabilirsiniz.

## 10 Bantlı Ekolayzer

**Ne yapar:** Müziğin tonunu, derin bastan parlak tizlere kadar değiştirir. Temiz bir **bas artırma** veya daha parlak, daha net bir üst uç için en iyi araçtır. Bunu her biri sesin farklı bir dilimi için olan on ses düğmesi gibi düşünün. O kısmı öne getirmek için bir bandı yükseltin, geri çekmek için düşürün. Genellikle birkaç dB'lik küçük değişiklikler en iyi ses verir ve çaldığınız her şeyde çalışır.

**Nasıl çalışır:** **32, 64, 125, 250, 500 Hz ve 1, 2, 4, 8, 16 kHz**'de on sürgü. Her biri **-12 dB (kesme)** ile **+12 dB (artırma)** arasında gider. Ayrıca genel seviye için **-24 ile +24 dB** arasında bir **Preamplifier** vardır. Kendi ön ayarlarınızı kaydedebilir ve bunları cihazlar arasında **dışa veya içe aktarabilirsiniz**.

**Her yerleşik ön ayarın ne yaptığı (22 ön ayar):**

| Ön ayar | Sesinize ne yapar |
|---|---|
| **Flat** | Değişiklik yok. Tüm bantlar sıfırda. Temiz bir başlangıç noktası. |
| **Acoustic** | Sıcak bas ve net, mevcut tizler. Akustik gitarları ve sesleri doğal ve canlı hissettirir. |
| **Bass Booster** | Alt uçta güçlü bir yükseltme, orta ve tizlere dokunulmaz. Daha fazla vuruş ve ağırlık. |
| **Bass Reducer** | Alt ucu keser. Yankılı odalar, ucuz kulaklıklar veya ağır parçalar için kullanışlı. |
| **Treble Booster** | Yalnızca tizleri yükseltir. Parıltı ve hava, daha fazla ayrıntı ekler. |
| **Treble Reducer** | Tizleri yumuşatır. Sert veya keskin kayıtları evcilleştirir. |
| **Classical** | Hafif bir orta düşüşle dolu baslar ve nazik tizler. Orkestral müzik için yumuşak ve ferah. |
| **Dance** | Oyulmuş ortalarla büyük baslar ve parlak tizler. Kulüp parçaları için vurucu ve enerjik. |
| **Deep** | Daha yumuşak tizlerle sıcak, kalın alt uç. Rahat, keyifli bir ses. |
| **Electronic** | Synth'ler ve ritimler için güçlü bas ve parlak tizler. Geniş ve modern. |
| **Hip-Hop** | Kontrollü ortalarla ağır bas ve net tizler. Ağır ve vurucu. |
| **Jazz** | Küçük bir orta düşüşle sıcak ve yumuşak. Akustik caz için rahat ve doğal. |
| **Latin** | Temiz ortalarla artırılmış baslar ve tizler. Parlak ve canlı. |
| **Loudness** | Bas ve tizleri güçlü şekilde artırır (bir "gülümseme" eğrisi). Düşük ses seviyesinde daha dolu duyulur. |
| **Lounge** | Yumuşak kenarlarla öne çıkan ortalar. Rahat ve vokal dostu. |
| **Piano** | Piyano notalarının temiz şekilde çınlaması için net ortalar ve tizler. |
| **Pop** | Vokaller için yükseltilmiş ortalar, baslar ve tizler geri çekilir. Sesler önde durur. |
| **R&B** | Çok güçlü alt-orta sıcaklık ve net tizler. Yumuşak ve zengin. |
| **Rock** | Gitarlar ve davullar için artırılmış baslar ve tizler. Enerjik ve dolu. |
| **Small Speakers** | Küçük hoparlörlerin daha dolu duyulmasına yardımcı olmak için basları artırır ve tizleri keser. |
| **Spoken Word** | Ses aralığını yükseltir ve derin bası keser. Konuşmayı net hale getirir. |
| **Vocal Booster** | Seslerin bulunduğu ortayı öne iter, çevresini keser. Vokaller öne çıkar. |

**Bas için ipucu:** **Bass Booster** ile başlayın, sonra bulanık geliyorsa hiçbir şeyin bozulmaması için Preamplifier'ı 1 ila 2 dB düşürün.

## Ses Normalizasyonu (Eşit Ses Düzeyi)

**Ne yapar:** Bazı şarkılar diğerlerinden daha yüksek çalar, bu yüzden sürekli ses seviyesini değiştirirsiniz. Bu, her şarkıyı kendiliğinden yaklaşık aynı ses seviyesinde çaldırır, böylece bunu yapmanıza gerek kalmaz. Eski ve yeni kayıtları, farklı albümleri veya farklı kaynakları karıştıran ve bir parçanın diğerinden çok daha yüksek olabildiği karışık çalma listeleri için mükemmeldir.

**Nasıl çalışır:** Her parçanın gerçek ses düzeyini **EBU R128** standardını (akış hizmetlerinin kullandığı aynı fikir olan **LUFS** cinsinden ölçülür) kullanarak dinler, ardından her parçayı hedefinize doğru ayarlar. Dosyalarınızda etikete ihtiyaç duymaz ve sesi asla değiştirmez. EBU R128, yalnızca en yüksek zirveyi değil, kulaklarınızın şarkının tamamında gerçekten hissettiği ses düzeyini ölçer, bu yüzden parçaların size gerçekte ne kadar yüksek geldiğiyle eşleşir. Flacbox bunu müzik çalarken canlı olarak hesaplar (ve yapabildiğinde ses düzeyini önceden kontrol eder), ardından parçaya tek, sabit bir ses değişikliği uygular. **Max boost** sınırı, çok sessiz kayıtların bozulacak kadar yükseğe itilmesini önler. Sesin kendisini okuduğu için, dosyaların hiç ses düzeyi etiketi olmadığında bile bulut dosyaları, canlı yayınlar ve modül müziği dahil herhangi bir kaynakta çalışır.

**Sürgüler:**

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Target loudness** | Her parçanın seviyelendirildiği ses düzeyini belirler. Daha yüksek değerler her şeyi genel olarak daha yüksek çaldırır. | -30 ila -6 LUFS (-16) |
| **Max boost** | Sessiz parçaların ne kadar yükseltilebileceğini sınırlar. Daha yüksek değerler yumuşak kayıtları hedefe daha da yaklaştırır. | 0 ila 24 dB (12) |

**Ön ayarlar:**

| Ön ayar | Ne yapar |
|---|---|
| **Light** | Gündelik dinleme için nazik seviyelendirme. Sessiz parçaları sertçe zorlamadan bariz ses sıçramalarını düzeltir. |
| **Standard** | Her amaca uygun varsayılan. Çoğu müziğe uyan akış tarzı bir ses düzeyi hedefi. Buradan başlayın. |
| **Strong** | Sessiz parçaları sıkıca yukarı iten agresif eşleştirme. Büyük seviye farkları olan karışık kütüphaneler için en iyisi. |
| **Night** | Yumuşak pasajları hâlâ yükselten daha sessiz bir genel hedef, böylece gece geç saat dinlemesi tutarlı ve düşük kalır. |

## Compressor (Yüksek ve Sessiz Kısımları Dengeleyin)

**Ne yapar:** Bir şarkıda sessiz kısımlar çok yumuşak, yüksek kısımlar çok yüksek olabilir. Bu, onları birbirine yaklaştırır, böylece tüm şarkı arabada veya gürültülü bir yerde bile kolayca duyulur. En yüksek anları nazikçe kısar ve daha yumuşak olanları yükseltir, böylece tek bir parça sırasında ses seviyesine uzanmayı bırakırsınız. Bu, Ses Normalizasyonu'ndan farklıdır: Compressor işleri tek bir şarkının **içinde** dengelerken, Ses Normalizasyonu ses düzeyini şarkılar **arasında** eşleştirir. İkisi birlikte iyi çalışır. Bir ön ayarla başlayın ve yalnızca daha fazla denetim istiyorsanız sürgüleri açın.

**Sürgüler:**

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Threshold** | Sıkıştırmanın başladığı seviye. Daha düşük değerler sesin daha fazlasını ezerek sessiz ve yüksek kısımları birbirine yakın tutar. | -60 ila 0 dB (-20) |
| **Ratio** | Yüksek kısımlar eşiği geçtiğinde ne kadar güçlü tutulacağı. Daha yüksek değerler daha sert sıkıştırır ve sesi daha eşit tutar. | 1:1 ila 30:1 (4:1) |
| **Attack** | Efektin ani bir yüksek zirveye ne kadar hızlı tepki vereceği. Kısa değerler geçişleri yakalar; daha uzun olanlar bunların geçmesine izin verir. | 0.1 ila 1000 ms (10 ms) |
| **Release** | Yüksek kısım geçtikten sonra efektin ne kadar hızlı bıraktığı. Kısa değerler zonklayabilir; daha uzun olanlar daha yumuşak duyulur. | 10 ms ila 5 s (100 ms) |
| **Master gain** | İşlemeden sonra uygulanan son çıkış artışı. Dinamikler dengelendikten sonra genel ses düzeyini yükseltmek için bunu artırın. | -30 ila +30 dB (0) |

**Ön ayarlar:**

| Ön ayar | Ne yapar |
|---|---|
| **Transparent** | Neredeyse fark edilmeyen bir güvenlik ağı. Dinamikleri neredeyse tamamen korur ve yalnızca en yüksek zirveleri yakalar. |
| **Soft** | Evde hi-fi dinleme için hafif seviyelendirme. Müziği ezmeden ince yumuşatma. |
| **Standard** | Günlük müzik oynatımı için makul varsayılan. Denenecek ilk ön ayar. |
| **Heavy** | Gürültülü ortamlar için agresif dengeleme. Araba, kalabalık oda, düşük ses seviyesinde dinleme. |
| **Voice / Podcast** | Konuşma için ayarlanmış. Daha yavaş atak sibilantların geçmesine izin verir, cömert makyaj kazancı vokalleri yukarı çeker. |
| **Old Recordings** | Ortalama seviyenin modern sürümlerin altında olduğu eski albümler ve restore edilmiş plaklar. |
| **Late Night** | Komşuların veya uyuyan ailenin önem taşıdığı sessiz dinleme için ağır sıkıştırma artı büyük artış. |
| **Movie Dialog** | Çeşitli bir film müziğinde konuşmayı müzik ve ses efektlerine karşı öne çıkarır. |
| **Streaming Match** | Modern akış hizmetlerinin yaklaşık -14 LUFS civarındaki ses düzeyi normalizasyonunu hedefler. |
| **Maximum Loudness** | Tam güç. Sınırlayıcıya vurur; ezilmiş, çok eşit bir sinyal bekleyin. Kelimenin tam anlamıyla maksimum ses ön ayarı. |

## Freeverb (Reverb, Bir Mekân Hissi)

**Ne yapar:** Müziğe küçük bir odadan büyük bir salona kadar bir mekân hissi ekler. Bir ön ayar seçin veya kuru ve ıslak karışımı, oda boyutunu, sönümlemeyi ve genişliği kendiniz ince ayarlayın. Reverb, herhangi bir gerçek mekânda duyduğunuz doğal yankıdır ve Freeverb bunu yazılımda yeniden yaratır. Az miktarı, düz veya yakın mikrofonlu kayıtları daha açık ve canlı hissettirir. Fazlası, müziği büyük, uzak bir mekâna yerleştirir. Yaratıcı bir efekttir, bu yüzden doğal sonuçlar için ıslak karışımı mütevazı tutun.

**Sürgüler:**

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Dry mix** | Orijinal, dokunulmamış sesin ne kadarının korunacağı. Daha yüksek değerler karışımda daha fazla kuru sinyal bırakır. | 0 ila 1 (0.0) |
| **Wet mix** | Yankılı sesin ne kadar eklendiği. Daha yüksek değerler reverb'i daha yüksek ve daha belirgin yapar. | 0 ila 3 (1.0) |
| **Room size** | Hayal edilen mekânın boyutu. Daha yüksek değerler, küçük bir odadan katedrale kadar daha uzun, daha büyük bir reverb kuyruğu verir. | 0 ila 1 (0.5) |
| **Damp** | Kuyrukta yüksek frekansların ne kadar hızlı söndüğü. Daha yüksek değerler reverb'i daha karanlık ve sıcak yapar. | 0 ila 1 (0.5) |
| **Width** | Reverb'in stereo yayılımı. Daha yüksek değerler mekânı sol ve sağ kanallar arasında daha geniş hissettirir. | 0 ila 1 (1.0) |

**Ön ayarlar:**

| Ön ayar | Ne yapar |
|---|---|
| **Room** | Küçük, sıkı bir mekân. Sesi boğmadan bir yer hissi ekleyen ince atmosfer. |
| **Studio** | Kuru, kontrollü bir kayıt odası. Doğal duyulmaya yetecek kadar yansıma. |
| **Hall** | Büyük bir konser salonu. Orkestral ve akustik müziğe uyan uzun, zengin bir kuyruk. |
| **Cathedral** | Devasa, yankılanan bir taş mekân. En uzun, en dramatik reverb kuyruğu. |
| **Plate** | Parlak, yoğun bir stüdyo plate reverb'i. Vokaller ve davullar için klasik. |
| **Ambience** | Kısa, havadar bir atmosfer. Çoğunlukla kuru kalırken hafif bir mekân hissi ekler. |

## Auto Wah (Funky Filtre Süpürmesi)

**Ne yapar:** Funky, vokal benzeri bir wah sesi için kendi kendine yukarı ve aşağı süpüren bir filtre. Bir ön ayar seçin veya ıslak karışımı, geri beslemeyi, hızı, aralığı ve frekansı kendiniz ayarlayın. Bir gitar wah pedalının yaptığı aynı "wah" süpürmesidir, ancak burada müzikle uyumlu olarak kendi kendine hareket eder. Funk, disko ve elektronik parçalarda harika duyulur. Cesur, bariz bir efekttir, bu yüzden günlük dinlemede azıcık bile çok işe yarar.

**Sürgüler:**

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Wet mix** | Karışımdaki wah efektinin ne kadar güçlü olduğu. Daha yüksek değerler süpüren filtreyi daha belirgin yapar. | -2 ila +2 (1.5) |
| **Feedback** | Çıkışın ne kadarının efekte geri beslendiği. Daha yüksek değerler wah'ı daha rezonanslı ve belirgin yapar. | -1 ila +1 (0.5) |
| **Rate** | Filtrenin ne kadar hızlı yukarı ve aşağı süpürdüğü. Daha yüksek değerler daha hızlı, daha ritmik bir wah verir. | 0.1 ila 9 Hz (2.0) |
| **Range** | Filtrenin oktav cinsinden ne kadar süpürdüğü. Daha yüksek değerler daha geniş, daha dramatik bir süpürme verir. | 0.1 ila 9 oktav (4.3) |
| **Frequency** | Filtrenin etrafında süpürdüğü temel frekans. Daha düşük değerler daha derin, daha yüksek değerler daha parlak duyulur. | 1 ila 1000 Hz (50) |

**Ön ayarlar:**

| Ön ayar | Ne yapar |
|---|---|
| **Classic** | Dengeli, klasik bir wah süpürmesi. Funk ve rock için iyi bir başlangıç noktası. |
| **Slow** | Nazikçe yukarı ve aşağı sürüklenen yavaş, geniş bir süpürme. Pad'ler ve uzun notalar için harika. |
| **Funky** | Bol hareketli, hızlı, vurucu bir süpürme. Gitarlara ve synth'lere ritmik ısırık ekler. |
| **Deep** | Düşük bir frekanstan başlayan derin, geniş bir süpürme. Büyük ve dramatik. |
| **Subtle** | Nazik, gösterişsiz bir hareket. Sese hakim olmadan karakter ekler. |
| **Resonant** | Yüksek geri beslemeli keskin, rezonanslı bir wah. Vokal benzeri ve ifadeli. |

## Phaser (Girdaplı Uğultu)

**Ne yapar:** Sese girdaplı, uğuldayan bir hareket ekleyen süpüren bir filtre. Bir ön ayar seçin veya geri beslemeyi, hızı, aralığı ve frekansı kendiniz ayarlayın. Notaları değiştirmeden nazik hareket ve parıltı ekler. Vokaller ve pad'lerde ince, synth'ler ve gitarlarda dramatiktir. Rüya gibi bir his için Slow'u veya güçlü bir girdap için Jet'i deneyin.

**Sürgüler:**

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Feedback** | Çıkışın ne kadarının efekte geri beslendiği. Daha yüksek değerler phaser'ı daha rezonanslı ve belirgin yapar. | -1 ila +1 (0.0) |
| **Rate** | Filtrenin ne kadar hızlı yukarı ve aşağı süpürdüğü. Daha yüksek değerler daha hızlı, daha ritmik bir phasing verir. | 0.1 ila 9 Hz (1.0) |
| **Range** | Filtrenin oktav cinsinden ne kadar süpürdüğü. Daha yüksek değerler daha geniş, daha dramatik bir süpürme verir. | 0.1 ila 9 oktav (4.0) |
| **Frequency** | Filtrenin etrafında süpürdüğü temel frekans. Daha düşük değerler daha derin, daha yüksek değerler daha parlak duyulur. | 1 ila 1000 Hz (100) |

**Ön ayarlar:**

| Ön ayar | Ne yapar |
|---|---|
| **Classic** | Dengeli, klasik bir phaser süpürmesi. Gitarlar ve klavyeler için iyi bir başlangıç noktası. |
| **Slow** | Nazikçe yukarı ve aşağı sürüklenen yavaş, geniş bir süpürme. Pad'ler ve uzun notalar için harika. |
| **Fast** | Bol hareketli, hızlı, parıldayan bir süpürme. Hareket ve enerji ekler. |
| **Deep** | Düşük bir frekanstan başlayan derin, geniş bir süpürme. Büyük ve dramatik. |
| **Subtle** | Nazik, gösterişsiz bir hareket. Sese hakim olmadan karakter ekler. |
| **Jet** | Yüksek geri beslemeli yoğun, rezonanslı bir süpürme, klasik jet uçağı uğultusu. |

## Flanger (Jet Uçağı Süpürmesi)

**Ne yapar:** Sese jet benzeri, süpüren bir uğultu veren kısa, hareketli bir gecikme. Bir ön ayar seçin veya derinliği, geri beslemeyi, hızı ve gecikmeyi kendiniz ayarlayın. Phaser'ın daha güçlü, daha metalik kuzenidir ve klasik rock ile elektronik müzikteki uğuldayan süpürmesiyle ünlüdür. İnce ayarlar nazik hareket ekler, derin ayarlar ise dramatik ve barizdir. Efekt için idareli kullanılması en iyisidir.

**Sürgüler:**

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Depth** | Süpürme efektinin ne kadar güçlü olduğu. Daha yüksek değerler flanging'i daha belirgin yapar. | %0 ila %100 (25) |
| **Feedback** | Çıkışın ne kadarının efekte geri beslendiği. Daha yüksek değerler flanger'ı daha rezonanslı ve metalik yapar. | %-99 ila %+99 (-50) |
| **Rate** | Süpürmenin ne kadar hızlı yukarı ve aşağı hareket ettiği. Daha yüksek değerler daha hızlı, daha parıldayan bir hareket verir. | 0 ila 10 Hz (0.25) |
| **Delay** | Süpürmenin üzerine kurulduğu temel gecikme süresi. Daha yüksek değerler daha derin, daha boş bir karakter verir. | 0 ila 4 ms (2.0) |

**Ön ayarlar:**

| Ön ayar | Ne yapar |
|---|---|
| **Classic** | Dengeli, klasik bir flanger. Gitarlar ve klavyeler için iyi bir başlangıç noktası. |
| **Subtle** | Nazik, gösterişsiz bir süpürme. Sese hakim olmadan hareket ekler. |
| **Deep** | Güçlü geri beslemeli derin, ağır bir süpürme. Büyük ve dramatik. |
| **Jet** | Pozitif geri beslemeli yoğun bir süpürme, klasik jet uçağı uğultusu. |
| **Fast** | Bol hareket ve enerjili hızlı, parıldayan bir süpürme. |
| **Wide** | Uzun gecikmeli yavaş, geniş bir süpürme. Zengin ve ferah. |

## Echo (Tekrarlar)

**Ne yapar:** Bir mekân ve derinlik hissi için sesi solan yankılar olarak tekrarlar. Bir ön ayar seçin veya ıslak karışımı, geri beslemeyi ve gecikmeyi kendiniz ayarlayın. Bir kanyonda seslenmek gibidir: ses kısa bir aradan sonra bir veya daha fazla kez geri gelir. Tek bir kısa tekrar gövde ve retro bir his ekler, daha fazla geri beslemeli daha uzun tekrarlar ise ferah, arkasında iz bırakan kuyruklar oluşturur. Ping Pong ön ayarı tekrarları sol ve sağ kulaklarınız arasında sektirir, bu da kulaklıkta eğlencelidir. Yankıların müziği örtmek yerine desteklemesi için ıslak karışımı mütevazı tutun.

**Sürgüler:**

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Wet mix** | Yankıların orijinal sese kıyasla ne kadar yüksek olduğu. Daha yüksek değerler tekrarları daha belirgin yapar. | -2 ila +2 (0.6) |
| **Feedback** | Yankının kaç kez tekrarlandığı. Daha yüksek değerler solması daha uzun süren daha fazla tekrar verir. | -1 ila +1 (0.5) |
| **Delay** | Yankılar arasındaki süre. Daha kısa değerler sıkı bir slap-back verir; daha uzun değerler aralıklı tekrarlar verir. | 0.01 ila 2 s (0.4) |

**Ön ayarlar:**

| Ön ayar | Ne yapar |
|---|---|
| **Slapback** | Sesin hemen arkasında tek, sıkı bir tekrar. Klasik rockabilly slap-back. |
| **Room** | Küçük bir oda gibi kısa, doğal bir yankı. Sesi bulanıklaştırmadan mekân ekler. |
| **Tape** | Eski bir teyp gecikmesi gibi kademeli olarak solan sıcak, orta tekrarlar. |
| **Dub** | Güçlü geri beslemeli uzun, ağır tekrarlar. Büyük, dub tarzı ve ferah. |
| **Ping Pong** | Geniş bir stereo efekti için yankılar sol ve sağ hoparlörler arasında sekiyor. |
| **Long** | Sesin çok arkasında iz bırakan yavaş, geniş aralıklı tekrarlar. |

## Chorus (Daha Kalın, Daha Geniş Ses)

**Ne yapar:** Orijinalin üzerine kayan bir kopya katmanlayarak sesi kalınlaştırır ve genişletir. Bir ön ayar seçin veya ıslak/kuru karışımı, derinliği, hızı ve geri beslemeyi kendiniz ayarlayın. Hafifçe akort bozuk, hareketli kopyalar ekleyerek tek bir enstrümanı veya sesi birlikte çalan birkaç tanesi gibi duyurur. Bu, zenginlik ve nazik bir parıltı ekler. İnce ayarlar işleri ısıtır, güçlü ayarlar ise zengin ve rüya gibi duyulur. Gitarlarda, klavyelerde ve vokallerde popülerdir.

**Sürgüler:**

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Wet/Dry** | Orijinal sese kıyasla chorus'un ne kadarını duyduğunuz. Daha yüksek değerler efekti daha belirgin yapar. | %0 ila %100 (50) |
| **Depth** | Perdenin ne kadar yukarı ve aşağı dalgalandığı. Daha yüksek değerler daha kalın, daha parıldayan bir ses verir. | %0 ila %100 (25) |
| **Rate** | Parıltının ne kadar hızlı hareket ettiği. Daha yavaş hızlar nazik ve zengin, daha hızlı hızlar ise daha çok vibratoya benzer duyulur. | 0 ila 10 Hz (1.1) |
| **Feedback** | Efektin ne kadarının kendine geri beslendiği. Daha yüksek değerler chorus'u daha rezonanslı ve yoğun yapar. | %-99 ila %+99 (25) |

**Ön ayarlar:**

| Ön ayar | Ne yapar |
|---|---|
| **Subtle** | Kendine dikkat çekmeden sıcaklık ekleyen nazik bir kalınlaştırma. |
| **Lush** | Zengin, klasik bir chorus. Gitarlar ve klavyeler için harika bir çok yönlü ayar. |
| **Ensemble** | Tek bir enstrümanı birkaç tanesi gibi duyuran dolu, katmanlı bir parıltı. |
| **Vibrato** | İnce bir chorus yerine sallanan bir vibrato için tamamen ıslak ve hızlı bir oran. |
| **Wide** | Stereo görüntüyü açan yavaş, geniş bir parıltı. Ferah ve rüya gibi. |
| **Twelve-String** | On iki telli bir gitarı andıran parlak, rezonanslı bir parıltı. |

## Distortion (Pürüz ve Kenar)

**Ne yapar:** Sesi aşırı yükleyerek pürüz ve kenar ekler. Bir ön ayar seçin veya sürüşü, çıkışı ve tonu kendiniz ayarlayın. Sesi kasıtlı olarak, sıcak, pürüzlü bir kenardan bozuk, fuzzy bir tona kadar kabalaştırır. Kaliteyi artırmanın bir yolu değil, yaratıcı, eğlence amaçlı bir efekttir, bu yüzden küçük miktarlarda kullanın. Elektronik, rock ve deneysel parçalarda eğlencelidir. Ağır bir ön ayar çok yükselirse Output'u düşürün.

**Sürgüler:**

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Drive** | Sesin ne kadar sert bozulduğu. Daha yüksek değerler daha pürüzlü ve daha agresiftir. | %0 ila %100 (15) |
| **Output** | Distortion sonrası çıkış seviyesi. Ağır bir ayar çok yükselirse düşürün. | -60 ila 0 dB (-18) |
| **Tone** | Distortion'dan önce tizleri keser. Daha düşük değerler daha karanlık ve sıcak duyulur. | 100 ila 8000 Hz (8000) |
| **Center** | Distortion'ın hangi frekans etrafında odaklandığı. Karakteri daha parlak veya daha karanlık kaydırır. | 100 ila 8000 Hz (2400) |
| **Width** | O odağın ne kadar geniş olduğu. Dar keskin ve genizden, geniş ise dolu ve açık duyulur. | 100 ila 8000 Hz (2400) |

**Ön ayarlar:**

| Ön ayar | Ne yapar |
|---|---|
| **Warm Drive** | Karakteri fazla değiştirmeden kenar ekleyen hafif, sıcak bir pürüz. |
| **Crunch** | Klasik, vurucu ve ritmik bir crunchy overdrive. |
| **Overdrive** | Bol ısırıklı parlak, sürüşlü bir ton. Lead sesler için harika. |
| **Fuzz** | Kalın, doymuş bir fuzz. Ağır ve harmoniklerle dolu. |
| **Metal** | Agresif, ağır sesler için sıkı, orta odaklı bir yüksek kazançlı ton. |
| **Screamer** | Bir tube screamer gibi öne çıkan orta artırılmış bir overdrive. |
| **LoFi** | Pürüzlü bir lo-fi karakteri için ezilmiş, dar bantlı bir distortion. |

## Rotate (Dönen Stereo)

**Ne yapar:** Döner, girdaplı bir efekt için sesi stereo alanın etrafında döndürür. Bir ön ayar seçin veya hızı kendiniz ayarlayın. Sesi, dönen bir hoparlör gibi sol ve sağ kanallarınız etrafında yavaşça hareket ettirir, bu da girdaplı, hipnotik bir his ekler. Yavaş ayarlar nazik ve geniş, hızlı ayarlar ise baş döndürücü ve barizdir. Bir stereo efektidir, bu yüzden en çok kulaklıkta veya iyi yerleştirilmiş hoparlörlerde fark edilir.

**Sürgü:**

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Rate** | Sesin stereo alan etrafında ne kadar hızlı döndüğü. Negatif değerler ters yönde döndürür; sıfır onu sabit tutar. | -5 ila +5 Hz (1.0) |

**Ön ayarlar:**

| Ön ayar | Ne yapar |
|---|---|
| **Slow Pan** | Yandan yana yavaş, nazik bir sürüklenme. İnce ve geniş. |
| **Sway** | Sabit bir sol-sağ salınım. Stereo görüntüye nazik hareket ekler. |
| **Rotary** | Döner bir hoparlörü andıran orta bir dönüş. |
| **Fast Spin** | Baş döndürücü, girdaplı bir efekt için stereo alan etrafında hızlı bir dönüş. |
| **Reverse** | Ters yönde orta bir dönüş. |
| **Whirl** | Çok hızlı bir girdap. Yoğun ve şaşırtıcı. |

## Crossfeed (Kulaklıkta Doğal Ses)

Hoparlörlerde, her iki kulağınız da hem sol hem de sağ hoparlörü, yalnızca biraz farklı zaman ve seviyelerde duyar. Kulaklıkta bu doğal harmanlanma yoktur: sol kulağınız yalnızca sol kanalı, sağ kulağınız yalnızca sağ kanalı duyar. Bu "süper stereo", müziğin kafanızın içinde bölünmüş gibi hissettirebilir ve bir enstrümanın tamamen bir tarafta oturduğu sert pan yapılmış kayıtlar uzun dinlemelerde doğal olmayan veya yorucu hissedebilir.

Crossfeed bunu, her kanalın küçük, filtrelenmiş bir miktarını diğerine, minik bir gecikme ve yüksek frekansların nazik bir azaltmasıyla harmanlayarak düzeltir. Bu, gerçek hoparlörlerden gelen sesin her iki kulağınıza ulaşma şekline, kafanızın uzak kulağı hafifçe gölgeleme biçimi dahil, yakındır. Sonuç, kafanızın içi yerine biraz önünüzde oturan daha doğal, hoparlör benzeri bir görüntüdür ve uzun oturumlarda dinleme yorgunluğunu azaltır. Flacbox, birçok audiophile çalar tarafından kullanılan saygın bir açık kaynaklı crossfeed olan iyi bilinen **bs2b (Bauer stereophonic-to-binaural)** yöntemini kullanır. Algoritma hakkında [bs2b proje sayfasında](https://bs2b.sourceforge.net/) bilgi edinebilirsiniz.

**Cutoff** harmanlamanın ne kadar sıcak duyulacağını, **Feed level** ise ne kadar güçlü olduğunu denetler. Ön ayarlar, neredeyse fark edilmeyen bir dokunuştan sağlam, hoparlör benzeri bir harmanlamaya kadar klasik bs2b seviyelerini kapsar. Crossfeed bir kulaklık efektidir, bu yüzden hoparlörlerde dinlerken kapalı bırakın.

**Sürgüler:**

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Cutoff** | Kanallar arasındaki sızmanın azalmaya başladığı yeri belirler. Daha düşük değerler daha sıcak, daha belirgin bir efekt verir. | 300 ila 2000 Hz (700) |
| **Feed level** | Bir kanalın diğerine ne kadar sızdığını denetler. Daha yüksek değerler daha hoparlör benzeri bir ses üretir. | 1 ila 15 dB (4.5) |

**Ön ayarlar:**

| Ön ayar | Ne yapar |
|---|---|
| **Subtle** | Gündelik dinleme için neredeyse fark edilmeyen crossfeed. Tonal dengeyi değiştirmeden sert pan yapılmış stereoyu yumuşatır. |
| **Chu Moy** | Klasik her amaca uygun varsayılan. Dengeli ve hafif sıcak, neredeyse her malzemede çalışır. Buradan başlayın. |
| **Strong** | Daha sert pan yapılmış mikslere daha güçlü sızma. Daha belirgin stereo daralma. |
| **Jan Meier** | Kulaklık meraklıları arasında popüler. Daha geniş besleme, daha hoparlör benzeri sunum, hafif bas yükseltmesi. |
| **Speaker-like** | Kulaklıkta en doğal hoparlör tarzı üretim için ayarlanmış. |
| **Vintage Stereo** | Sert pan yapılmış davullar ve vokallerle 1960'lar ve 1970'ler miksleri için ayarlanmış agresif crossfeed. |

## Sinyal İşleme: Kendi DSP Zincirinizi Kurun

Hazır efektlerin ötesinde, Flacbox **Ayarlar > Ses çalar > Sinyal işleme** içinde kendi zincirinizi kurmanıza olanak tanır. Zincir boşken uygulamanın açıkladığı gibi: *"Bir efekt eklemek için + öğesine dokunun. Her birini anahtarıyla açın veya kapatın, yeniden sıralamak için sürükleyin, parametrelerini düzenlemek için dokunun ve çoğaltmak veya silmek için uzun basın."*

**Sıra önemlidir**: distortion'dan önceki bir filtre, aynı filtrenin sonrasından farklı duyulur. Ayrıca tüm zinciri **Tüm kanallara**, **Sol kanala** veya **Sağ kanala** yönlendirebilirsiniz.

Aşağıda, her sürgü ve her ön ayar için uygulamanın kendi metniyle birlikte her blok yer alır.

### Gain (Seviye Ayarı)

Zincirdeki bir noktada seviyeyi yükseltir veya düşürür.

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Gain** | Zincirdeki bu noktada seviyeyi artırır veya keser. Diğer efektlerden sonra seviyeyi telafi etmek veya sonraki efektleri sürmek için kullanın. | -24 ila +24 dB (0) |

| Ön ayar | Ne yapar |
|---|---|
| **Unity** | Seviyede değişiklik yok. Nötr bir başlangıç noktası. |
| **Cut** | Büyük bir kesme. Yüksek bir kaynağı evcilleştirir veya sonraki efektlerden önce yer açar. |
| **Trim** | Seviyeyi biraz geri çekmek için nazik bir kesme. |
| **Lift** | Sessiz bir kaynağı yukarı getirmek için mütevazı bir artış. |
| **Boost** | Sessiz malzeme için veya sonraki efektleri daha sert sürmek için güçlü bir artış. |
| **Max** | Maksimum artış. Yüksek, zincirin ilerisinde kırpılmaya dikkat edin. |

### Low Pass (Tizleri Kaldırır)

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Cutoff** | Filtrenin tizleri azaltmaya başladığı yeri belirler. Sesi karartmak ve yumuşatmak için düşürün; tamamen açmak için üste doğru yükseltin. | 20 Hz ila 20 kHz (20 kHz) |
| **Resonance** | Kesme frekansındaki frekansları vurgular. Temiz bir azalma için düşük tutun; tepeli, ıslık gibi bir kenar için yükseltin. | 0.1 ila 10 (0.707) |

| Ön ayar | Ne yapar |
|---|---|
| **Air** | Yalnızca en üstü keser. Sesi köreltmeden biraz kenarını alır. |
| **Warm** | Daha sıcak, daha yuvarlak bir ton için tizlerin nazik bir azalması. |
| **Mellow** | Belirgin şekilde yumuşatılmış. Rahat bir his için parlaklığı geri çeker. |
| **Muffled** | Bir duvarın arkasından duyulmuş gibi karanlık ve boğuk. |
| **Telephone** | Aralığın altında dar, rezonanslı bir tepe. İnce, telefon benzeri bir ses. |

### High Pass (Basları Kaldırır)

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Cutoff** | Filtrenin basları azaltmaya başladığı yeri belirler. Alt ucu inceltmek ve gürültüyü kaldırmak için yükseltin; tamamen açmak için alta doğru düşürün. | 20 Hz ila 20 kHz (20 Hz) |
| **Resonance** | Kesme frekansındaki frekansları vurgular. Temiz bir azalma için düşük tutun; tepeli, ıslık gibi bir kenar için yükseltin. | 0.1 ila 10 (0.707) |

| Ön ayar | Ne yapar |
|---|---|
| **Rumble Cut** | Duyulabilir alt uca dokunmadan subsonik gürültüyü ve DC ofsetini kaldırır. |
| **Tighten** | Daha sıkı, daha temiz bir bas için yankılı düşük frekansları keser. |
| **Thin** | Sıcaklığı ve gövdeyi keserek daha hafif, daha ince bir ses bırakır. |
| **Radio** | Yalnızca ortalar ve tizler kalır, küçük bir radyo hoparlörü gibi. |
| **Telephone** | Aralığın üstünde dar, rezonanslı bir tepe. İnce, telefon benzeri bir ses. |

### Band Pass (Ortada Bir Bant Tutar)

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Center** | Filtrenin geçirdiği frekansı belirler. Üstündeki ve altındaki her şey azaltılır. Bası, ortaları veya tizleri seçmek için süpürün. | 20 Hz ila 20 kHz (1 kHz) |
| **Resonance** | Bandın ne kadar geniş olduğunu denetler. Düşük değerler geniş bir aralığı geçirir; keskin, rezonanslı bir ton için merkeze doğru daraltmak için yükseltin. | 0.1 ila 10 (0.707) |

| Ön ayar | Ne yapar |
|---|---|
| **Voice** | Çoğu vokalin bulunduğu orta aralık çevresinde geniş bir bant. Nötr bir başlangıç noktası. |
| **Bass** | Alt ucu yalıtır, yalnızca bası ve kick'i bırakır. |
| **Body** | Sıcak, kutu gibi bir gövde için alt-ortalara odaklanır. |
| **Presence** | Netlik ve mevcudiyet için üst-ortaları yükseltir. |
| **Telephone** | Dar bir orta aralık bandı. İnce, telefon benzeri bir ses. |
| **Wah** | Çok dar, rezonanslı bir tepe. Bir wah efekti için merkezi süpürün. |

### Notch (Bir Dar Bandı Kaldırır)

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Frequency** | Filtrenin kaldırdığı frekansı belirler. Üstündeki ve altındaki her şey geçer. Kesmek için bir uğultuya veya rezonansa ayarlayın. | 20 Hz ila 20 kHz (60 Hz) |
| **Resonance** | Kesmenin ne kadar geniş olduğunu denetler. Düşük değerler geniş bir aralığı oyar; yalnızca bir nokta bandı kaldırıp gerisini dokunulmamış bırakmak için yükseltin. | 0.1 ila 10 (8.0) |

| Ön ayar | Ne yapar |
|---|---|
| **Mains Hum 60** | 60 Hz elektriksel uğultuyu kaldırır (Kuzey Amerika şebekesi). Nötr bir başlangıç noktası. |
| **Mains Hum 50** | 50 Hz elektriksel uğultuyu kaldırır (Avrupa ve diğer şebekeler). |
| **Rumble** | Tüm alt ucu inceltmeden düşük frekanslı bir gürültüyü veya rezonansı keser. |
| **Mud** | Daha temiz, daha net bir ses için alt-orta bulanıklığı oyar. |
| **Boxy** | Kutu gibi bir orta aralık homurtusunu kaldırır. |
| **Harsh** | Üst-ortalarda sert, delici bir tepeyi evcilleştirir. |

### Peaking (Parametrik EQ Bandı)

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Frequency** | Artırılacak veya kesilecek bandın merkezi. Şekillendirmek istediğiniz frekansı bulmak için süpürün. | 20 Hz ila 20 kHz (1 kHz) |
| **Gain** | Merkezde ne kadar artırılacağı veya kesileceği. Pozitif bandı yükseltir; negatif onu oyar. | -15 ila +15 dB (0) |
| **Q factor** | Bandın ne kadar geniş olduğunu belirler. Düşük değerler geniş bir alanı şekillendirir; yüksek değerler cerrahi, nokta değişiklikler için daraltır. | 0.1 ila 10 (1.0) |

| Ön ayar | Ne yapar |
|---|---|
| **Presence** | Netlik ve mevcudiyet için geniş bir üst-orta yükseltme. Nötr bir başlangıç noktası. |
| **Warmth** | Gövde ve sıcaklık ekleyen geniş bir alt-orta artış. |
| **Vocal Boost** | Sesleri öne getirmek için çekirdek vokal aralığını yükseltir. |
| **Cut Mud** | Daha temiz bir ses için kutu gibi alt-orta bulanıklığı oyar. |
| **Tame Harsh** | Sert, delici bir tepeyi evcilleştirmek için dar bir kesme. |
| **Punch** | Alt uca vuruş ve etki ekleyen düşük bir artış. |
| **Sub Boost** | Ekstra sub-bas ağırlığı için en alttaki derin bir artış. |
| **Air** | Açık, havadar bir parlaklık için en üstte geniş bir yükseltme. |
| **Clarity** | Tanım ve kenar eklemek için yüksek-ortaları yükseltir. |
| **De-Ess** | Sert S seslerini evcilleştirmek için sibilans aralığında dar bir kesme. |
| **De-Boom** | Daha sıkı bir alt uç için yankılı düşük frekanslı bir birikimi keser. |
| **Scoop** | Oyulmuş, modern bir ton için geniş bir orta aralık düşüşü. |

### Low Shelf (Bas Denetimi ve Bas Artırma)

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Frequency** | Shelf'in etkili olduğu köşenin altını belirler. Altındaki her şey birlikte artırılır veya kesilir. | 20 ila 2000 Hz (200) |
| **Gain** | Alt ucun ne kadar yükseltileceği veya düşürüleceği. Pozitif ağırlık ve sıcaklık ekler; negatif onu inceltir. | -15 ila +15 dB (0) |

| Ön ayar | Ne yapar |
|---|---|
| **Warmth** | Sıcaklık ve gövde için nazik bir alt uç yükseltmesi. Nötr bir başlangıç noktası. |
| **Bass Boost** | Ağırlık ve vuruş için basa sağlam bir artış. |
| **Fullness** | Daha dolu, daha yuvarlak bir ses için alt-ortaları doldurur. |
| **Trim Bass** | Bas ağırlıklı bir miksi hafifletmek için mütevazı bir kesme. |
| **Cut Lows** | Alt ucu inceltmek veya de-boom yapmak için güçlü bir kesme. |
| **Big Bottom** | Maksimum ağırlık ve gürültü için büyük bir alt uç artışı. |

### High Shelf (Tiz Denetimi)

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Frequency** | Shelf'in etkili olduğu köşenin üstünü belirler. Üstündeki her şey birlikte artırılır veya kesilir. | 1 ila 20 kHz (8 kHz) |
| **Gain** | Üst ucun ne kadar yükseltileceği veya düşürüleceği. Pozitif parlaklık ve hava ekler; negatif yumuşatır ve karartır. | -15 ila +15 dB (0) |

| Ön ayar | Ne yapar |
|---|---|
| **Presence** | Netlik ve ayrıntı için nazik bir üst uç yükseltmesi. Nötr bir başlangıç noktası. |
| **Air** | Havadar, açık bir ses için en üstü açar. |
| **Bright** | Net, parlak, öne çıkan bir ton için güçlü bir artış. |
| **Soften** | Sert tizlerin kenarını almak için mütevazı bir kesme. |
| **Tame Highs** | Aşırı parlak bir sesi karartmak ve yumuşatmak için güçlü bir kesme. |
| **Sparkle** | Maksimum parıltı için büyük bir üst uç artışı. |

### Soft Clip (Sıcak Doygunluk)

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Drive** | Sinyali dalga şekillendiriciye daha sert iter. Düşük miktarlar nazik sıcaklık ekler; yüksek miktarlar zirveleri kalın doygunluk ve pürüze yuvarlar. | 0 ila 40 dB (0) |

| Ön ayar | Ne yapar |
|---|---|
| **Warm** | Nazik, analog tarzı sıcaklık için bir tutam sürüş. |
| **Drive** | Sesi kalınlaştıran ve renklendiren belirgin doygunluk. |
| **Crunch** | Duyulabilir crunchy bir kenarla ağır sürüş. |
| **Fuzz** | Kalın, fuzzy distortion. Zirveler sertçe ezilir. |
| **Destroy** | Maksimum sürüş. Agresif, tamamen doymuş pürüz. |

### Bit Crusher (Retro Lo-Fi)

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Bit depth** | Her örneği kaç bitin tanımladığını belirler. Daha az bit, crunchy, pürüzlü bir dijital ses için daha kaba adımlar ve daha fazla kuantizasyon gürültüsü demektir. | 1 ila 16 bit (16) |
| **Sample rate** | Sesi alt örnekler. Yüzde yüzde hız dokunulmamıştır; her örneği daha uzun tutmak için düşürün, tizleri köreltir ve sert, aliased bir kenar ekler. | %1 ila %100 (%100) |

| Ön ayar | Ne yapar |
|---|---|
| **Vintage** | Erken bir dijital örnekleyici gibi kalitede ince bir düşüş. |
| **LoFi** | Klasik 8-bit, yarı hızlı lo-fi. Grenli ve retro. |
| **Crunch** | Duyulabilir crunchy bir kenarla daha ağır ezme. |
| **Gritty** | Kaba ve pürüzlü. Seviyeler arasındaki adımlar bariz. |
| **Destroy** | Aşırı azaltma. Sert, bozuk, zar zor tanınabilir. |

### Ring Modulator (Metalik ve Robotik Tonlar)

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Carrier** | Sinyalin çarpıldığı tonun frekansını belirler. Birkaç hertz bir tremolo dalgalanması verir; daha yüksek frekanslar metalik, çan benzeri ve robotik üst tonlar ekler. | 1 ila 4000 Hz (440) |
| **Mix** | Modüle edilmiş sesi orijinalle harmanlar. Yüzde sıfırda yalnızca kuru sinyali duyarsınız; yüzde yüzde yalnızca tamamen modüle edilmiş tonu. | %0 ila %100 (%0) |

| Ön ayar | Ne yapar |
|---|---|
| **Tremolo** | Çok düşük bir taşıyıcı, onu ses seviyesini dalgalandıran bir genlik tremolosuna dönüştürür. |
| **Robot** | Orta bir taşıyıcı, klasik bir robot sesi efekti için tıngırdayan üst tonlar ekler. |
| **Metallic** | Sert, metalik bir ton için yoğun, uyumsuz üst tonlar. |
| **Bell** | Daha yüksek bir taşıyıcı parlak, çan benzeri bir çınlama verir. |
| **Alien** | Yüksek bir taşıyıcıyla tamamen ıslak. Aşırı, uzaylı, zar zor tanınabilir. |

### Tremolo (Ses Dalgalanması)

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Rate** | Ses seviyesinin ne kadar hızlı nabız attığını belirler. Daha yavaş hızlar yumuşak bir salınım verir; daha hızlı hızlar hızlı bir kekeleme verir. | 0.1 ila 20 Hz (5) |
| **Depth** | Her nabızda ses seviyesinin ne kadar düştüğünü belirler. Yüzde sıfırda seviye sabittir; yüzde yüzde tamamen sessizliğe düşer. | %0 ila %100 (%0) |

| Ön ayar | Ne yapar |
|---|---|
| **Gentle** | Yavaş, sığ bir salınım. Dikkat çekmeden ince hareket. |
| **Classic** | Klasik amp tremolosu: orta bir hız ve ılımlı bir derinlik. |
| **Deep** | Her döngüde neredeyse sessizliğe düşen güçlü, derin bir nabız. |
| **Fast** | Parıldayan, gergin bir his için hızlı bir titreme. |
| **Chop** | Hızlı ve tam derinlik. Sert, kekeleyen bir kesme. |

### Delay (Echo)

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Time** | Her yankıdan önceki boşluğu belirler. Kısa süreler sıkı bir slapback verir; daha uzun süreler tekrarları daha da aralar. | 0.01 ila 2 s (0.25) |
| **Feedback** | Her yankının ne kadarının geri beslendiğini belirler. Düşük değerler tek bir tekrar verir; daha yüksek değerler uzun, iz bırakan bir yankı serisi oluşturur. | 0 ila 0.95 (0.4) |
| **Mix** | Yankıları orijinalle harmanlar. Yüzde sıfırda yalnızca kuru sinyali duyarsınız; yüzde yüzde yalnızca yankıları. | %0 ila %100 (%0) |

| Ön ayar | Ne yapar |
|---|---|
| **Slapback** | Orijinale sıkıca yaslanmış tek, kısa bir yankı. Rockabilly ve vokal ikileme. |
| **Echo** | Klasik echo: birkaç iz bırakan kuyruklu net bir tekrar. |
| **Ping** | Ritmik hareket ekleyen hızlı, sekiyor bir tekrar. |
| **Ambient** | Ferah bir kuyruğa yayılan daha uzun, daha yumuşak tekrarlar. |
| **Dub** | Uzun, dub tarzı yankı çağlayanları için yüksek geri besleme. |
| **Cavern** | Devasa bir mekânda yankılanan ses gibi uzun, derin tekrarlar. |

### Stereo Width (Daralt veya Genişlet)

| Denetim | Ne yapar | Aralık (varsayılan) |
|---|---|---|
| **Width** | Stereo görüntüyü daraltır veya genişletir. Yüzde sıfır mono'ya çöker, yüzde yüz onu dokunulmamış bırakır ve daha yüksek değerler kenarları daha geniş iter. Yalnızca Tüm kanallar hedefindeki stereo parçaları etkiler. | %0 ila %200 (%100) |

| Ön ayar | Ne yapar |
|---|---|
| **Wide** | Stereo görüntüyü açan nazik bir genişletme. Nötr bir başlangıç noktası. |
| **Wider** | Büyük, sürükleyici bir stereo alan için daha güçlü bir yayılma. |
| **Max** | Maksimum genişlik. Çok geniş, ancak mono uyumluluğu sorunlarına dikkat edin. |
| **Narrow** | Daha sıkı, daha merkezi bir görüntü için kenarları içeri çeker. |
| **Focused** | Yalnızca bir tutam stereoyla neredeyse merkezi. |
| **Mono** | Tamamen mono'ya çökmüş. Her iki hoparlör de aynı sinyali çalar. |

## Tüm Bunlar Kaputun Altında Nasıl Çalışır (Basit Sürüm)

- **Motorlar:** Ayarlar > Ses çalar > Oynatma motoru içinde bir tane seçersiniz: **Standard** (sistem), **Universal** (FFmpeg) veya **Sound FX** ([Un4seen Developments](https://www.un4seen.com/)'ten **BASS™ motoru**). Seçtiğiniz motor hangi formatların çalacağına karar verir ve efektler, ekolayzer ve DSP zinciri yalnızca Sound FX motorunda çalışır.
- **Formatlar:** BASS™ motoru, sistem ve FFmpeg formatlarının üstüne FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus ve modül (tracker) müziği ekler.
- **Efektler:** ekolayzer, compressor ve çoğu efekt BASS™ efekt eklentilerini kullanır. Freeverb, Freeverb reverb'idir. Chorus, Flanger ve Distortion kendi denetimleriyle klasik DirectX tarzı efektleri kullanır.
- **Ses Normalizasyonu:** canlı bir **EBU R128** ses düzeyi seviyeleyici (yayın ve akışta kullanılan ses düzeyi standardı).
- **Crossfeed:** BASS™ motorunun içinde çalışan **bs2b (Bauer)** crossfeed'i.
- **DSP zinciri:** özel bloklarınız, belirlediğiniz tam sırada, tüm kanallarda veya yalnızca bir tarafta uygulanır.
- **Çıkış:** örnekleme hızını, kanal sayısını ve arabellek boyutunu ekipmanınıza uyacak şekilde ayarlayabilirsiniz.

Tüm bunlar müzik çalarken canlı olarak çalıştığından, efektler:

- Bulut dosyaları, yayınlar ve modül müziği dahil her şeyde **gerçek zamanlı** çalışır.
- Dosyalarınızı **asla değiştirmez veya yeniden kaydetmez**. Bir efekti kapatın ve orijinal geri döner.
- Her efekt için **ayarlarınızı hatırlar**.
- Her biri ayrı olduğu için serbestçe **karıştırılıp eşleştirilebilir**.

## Denemek İçin Basit Tarifler

**Günlük dinleme**

- **Daha fazla bas, temizce:** Ekolayzer > Bass Booster, sonra Preamplifier'ı 1 ila 2 dB düşürün. Veya Bass Boost'ta bir DSP Low Shelf ekleyin.
- **Karışık bir çalma listesinde eşit ses düzeyi:** Ses Normalizasyonu > Standard, artı Compressor > Soft.
- **Nazik genel cila:** Compressor > Transparent, artı Ses Normalizasyonu > Light.
- **Daha net vokaller:** Ekolayzer > Vocal Booster veya Vocal Boost'ta bir DSP Peaking bloğu.
- **Küçük telefon hoparlörlerinde daha dolu ses:** Ekolayzer > Small Speakers.

**Kulaklıklar**

- **Kulaklıkta daha hoş, daha az yorucu:** Crossfeed > Chu Moy veya Jan Meier.
- **Kulaklıkta daha geniş ses:** DSP Stereo Width > Wide, artı Crossfeed > Chu Moy.
- **Sert pan yapılmış 1960'lar ve 1970'ler plaklarını düzeltin:** Crossfeed > Vintage Stereo.
- **Biraz hava ve mekân:** Freeverb > Ambience, düşük tutulmuş, artı Crossfeed > Subtle.

**Sessiz zamanlar ve konuşma sesi**

- **Gece geç saat sessiz dinleme:** Ses Normalizasyonu > Night, artı Compressor > Late Night.
- **Podcast'ler ve sesli kitaplar:** Compressor > Voice / Podcast, artı Ekolayzer > Spoken Word.
- **Gürültülü bir arabada en yüksek, en eşit ses:** Ses Normalizasyonu > Strong, artı Compressor > Heavy.

**Sorunları düzeltme**

- **Sert, parlak bir kaydı evcilleştirin:** Ekolayzer > Treble Reducer veya Tame Harsh'ta bir DSP Peaking bloğu.
- **Elektriksel uğultuyu kaldırın:** DSP zinciri > Notch > Mains Hum 60 (veya Avrupa'da Mains Hum 50).
- **Daha sıkı, daha temiz bas:** Yankılı alt ucu kesmek için DSP High Pass > Tighten.
- **Bas ağırlıklı bir mikste daha az yankı:** DSP Low Shelf > Trim Bass veya Peaking > De-Boom.

**Yaratıcı ve eğlenceli**

- **Sıcak, ferah his:** Freeverb > Hall, düşük tutulmuş.
- **Rüya gibi, ferah gitarlar:** Chorus > Wide, artı Echo > Long.
- **Retro lo-fi:** DSP zinciri > Bit Crusher (LoFi) içine Soft Clip (Warm).
- **Elektronik parçalarda funky hareket:** Auto Wah > Funky veya Phaser > Fast.
- **Klasik jet uçağı süpürmesi:** Flanger > Jet.

## SSS

{{% details title="Flacbox hangi ses motorunu kullanır?" closed="true" %}}
Ayarlar > Ses çalar içinde bir Oynatma motoru seçersiniz: Standard (Apple'ın sistem motoru), Universal (FFmpeg motoru) veya Sound FX (Un4seen Developments'ten BASS™ motoru, un4seen.com). Seçtiğiniz motor hangi dosya formatlarının çalacağına karar verir. Sound FX, FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus ve MOD veya tracker müziği gibi ek formatları çalan tek motordur ve canlı efektleri, 10 bantlı ekolayzeri ve DSP zincirini sağlayan tek motordur. Efektleri kullanmak için Oynatma motorunu Sound FX olarak ayarlayın.
{{% /details %}}

{{% details title="Flacbox MOD, XM, IT ve diğer tracker veya modül müziğini çalabilir mi?" closed="true" %}}
Evet. BASS™ motorunun, MOD, XM, IT, S3M, MTM, UMX ve MO3 dosyalarını yükleyen ve şarkıyı desenlerinden ve enstrüman seslerinden, tracker müziğinin çalınması gerektiği şekilde canlı olarak yeniden oluşturan yerleşik bir modül çalar vardır. Sıradan iPhone çalarlar bunu yapamaz. Efektler ve ekolayzer modül müziğinde de çalışır.
{{% /details %}}

{{% details title="Flacbox DSD ve yüksek çözünürlüklü dosyaları destekler mi?" closed="true" %}}
Evet. Flacbox, DSD dosyalarını (DSF ve DFF) normal çıkış donanımında çalışmaları için DSD over PCM kullanarak BASS™ motoru aracılığıyla çalar, ayrıca kayıpsız oynatma için FLAC, WavPack, Monkey's Audio (APE), Musepack ve TrueAudio çalar.
{{% /details %}}

{{% details title="Flacbox'ta hangi ses efektleri var?" closed="true" %}}
10 bantlı bir ekolayzer, Ses Normalizasyonu, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate ve Crossfeed, ayrıca filtreler, shelf'ler, gain, soft clip, bit crusher, ring modulator, tremolo, delay ve stereo width ile kendi kendinize kurduğunuz bir DSP zinciri. Her biri ayrıdır ve diğerleriyle birleştirilebilir.
{{% /details %}}

{{% details title="Ön ayar nedir?" closed="true" %}}
Ön ayar, bir efekt için hazır bir ayardır. Sürgüleri kendiniz hareket ettirmek yerine bir ön ayara dokunursunuz ve ses ona uyacak şekilde değişir. Flacbox'taki her efektin birkaç ön ayarı vardır ve bu rehber her birinin ne yaptığını listeler. Bir ön ayar seçtikten sonra bir sürgüyü hareket ettirirseniz, efekt artık kendi değerlerinizi kullandığını söylemek için «Manual» gösterir.
{{% /details %}}

{{% details title="Flacbox'ta ses efektlerini nasıl açarım?" closed="true" %}}
Şimdi Çalınıyor çalarını açın, ⋯ (Daha fazla eylem) düğmesine dokunun ve Ses efektleri'ni seçin. Veya Ayarlar > Ses çalar > Ses efektleri'ne gidin. Bir efekte dokunun, anahtarını açın ve bir ön ayar seçin veya ince ayar yapmak için sürgüleri açın.
{{% /details %}}

{{% details title="Ekolayzer nerede ve en iyi ayarlar nelerdir?" closed="true" %}}
Ayarlar > Ses çalar > Ses ekolayzeri'ne gidin. 32 Hz'den 16 kHz'e her biri -12 ila +12 dB olan 10 bant, ayrıca -24 ila +24 dB'lik bir Preamplifier ve 22 ön ayar vardır. Daha fazla bas için Bass Booster kullanın. Daha net sesler için Vocal Booster veya Pop kullanın. Daha parlak bir ses için Treble Booster kullanın. Sonra tek bantları zevkinize göre ayarlayın.
{{% /details %}}

{{% details title="Flacbox'ta bası nasıl artırırım?" closed="true" %}}
İki kolay yol. Ses ekolayzerinde Bass Booster'ı seçin (veya 32 Hz ve 64 Hz bantlarını birkaç dB yükseltin). Veya Sinyal işleme içinde Bass Boost olarak ayarlanmış bir Low Shelf bloğu ekleyin. Her iki durumda da, basın temiz kalması ve bozulmaması için Preamplifier'ı düşürün veya 1 ila 2 dB'lik bir Gain bloğu ekleyin.
{{% /details %}}

{{% details title="Müziğim için hangi ekolayzer ön ayarı en iyisi?" closed="true" %}}
Rock ve Electronic, güçlü baslar ve tizlerle enerji ekler. Acoustic, Jazz ve Classical sıcak ve doğal kalır. Pop ve Vocal Booster sesleri öne iter. Bass Booster ve Hip-Hop ağırlık ekler. Deep ve Loudness düşük ses seviyesinde daha dolu duyulur. Türünüze uyanla başlayın, sonra ince ayar yapın.
{{% /details %}}

{{% details title="Ses Normalizasyonu nedir ve ReplayGain'den nasıl farklıdır?" closed="true" %}}
Her parçayı yaklaşık aynı ses düzeyinde çaldırır. Gerçek ses düzeyini EBU R128 standardını (akış hizmetleri gibi LUFS cinsinden) kullanarak ölçer ve her parçayı bir max-boost sınırıyla hedefinize doğru ayarlar. ReplayGain'in aksine, dosyalarınızda etikete ihtiyaç duymaz ve sesi değiştirmeden herhangi bir kaynakta canlı olarak çalışır. Ön ayarlar: Light, Standard, Strong ve Night.
{{% /details %}}

{{% details title="Crossfeed nedir ve kullanmalı mıyım?" closed="true" %}}
Crossfeed, sol ve sağ kanallardan biraz karıştırır, böylece kulaklıklar gerçek hoparlörlere daha çok benzer ve ses kafanızda takılı kalmış gibi olmaz. Yalnızca kulaklıklar içindir, bu yüzden hoparlörler için kapatın. Flacbox, Chu Moy ve Jan Meier gibi ön ayarlarla bs2b (Bauer) yöntemini kullanır.
{{% /details %}}

{{% details title="Compressor ile Ses Normalizasyonu arasındaki fark nedir?" closed="true" %}}
Ses Normalizasyonu, farklı şarkılar arasındaki ses düzeyini eşleştirir. Compressor, tek bir şarkının içindeki yüksek ve sessiz kısımları dengeler. Farklı sorunları çözerler ve özellikle bir arabada veya gürültülü bir yerde birlikte iyi çalışırlar.
{{% /details %}}

{{% details title="Sinyal işleme (DSP) zinciri nedir?" closed="true" %}}
Ayarlar > Ses çalar > Sinyal işleme içinde kendi kendinize kurduğunuz bir raftır. Filtreler, shelf'ler, gain, soft clip, bit crusher, ring modulator, tremolo, delay ve stereo width gibi bloklar ekleyin, herhangi bir sıraya koyun, her birini açın veya kapatın ve zinciri tüm kanallara, sola veya sağa yönlendirin. Sıra önemli olduğundan, tam olarak istediğiniz sesi tasarlayabilirsiniz.
{{% /details %}}

{{% details title="Ekolayzer, efektler ve DSP zinciri arasındaki fark nedir?" closed="true" %}}
Ekolayzer, basit bir 10 bantlı ton denetimidir. Ses efektleri, ön ayarları olan hazır araçlardır (compressor, reverb, echo vb.). DSP zinciri, kendi efekt sıranızı bireysel bloklardan kurduğunuz yerdir. Üçünü de aynı anda çalıştırabilirsiniz.
{{% /details %}}

{{% details title="Efektler müzik dosyalarımı değiştirir veya bozar mı?" closed="true" %}}
Hayır. Her şey müzik çalarken canlı olarak uygulanır. Dosyalarınız asla değiştirilmez veya yeniden kaydedilmez. Bir efekti kapatın ve orijinal ses anında geri döner.
{{% /details %}}

{{% details title="Aynı anda birden fazla efekt kullanabilir miyim?" closed="true" %}}
Evet. Her efektin kendi anahtarı vardır ve ana anahtar yoktur, bu yüzden herhangi bir kombinasyon çalışır. Örneğin, eşit dinleme için Ses Normalizasyonu artı Compressor veya kulaklıkta Freeverb artı Crossfeed, üstünde ekolayzer ile.
{{% /details %}}

{{% details title="Efekt denetimleri neden gri görünüyor?" closed="true" %}}
Efekt kapalıdır. Denetimleri kullanmak için düzenleyicinin üstündeki anahtarını açın. Her efekt varsayılan olarak kapalıdır.
{{% /details %}}

{{% details title="Manual etiketi ne anlama gelir?" closed="true" %}}
Bir sürgüyü bir ön ayardan uzaklaştırdığınız anlamına gelir, yani efekt artık adlandırılmış bir ön ayar yerine kendi özel değerlerinizi kullanıyor. Her sürgünün bir sıfırlama düğmesi vardır ve bir ön ayarı tekrar seçmek manuel değerlerinizin yerini alır.
{{% /details %}}

{{% details title="Ekolayzer ön ayarlarımı kaydedip paylaşabilir miyim?" closed="true" %}}
Evet. 22 yerleşik ön ayarın yanı sıra, kendinizinkileri oluşturabilir, yeniden sıralayabilir ve ayarlarınızı başka bir cihaza taşımak için dışa veya içe aktarabilirsiniz.
{{% /details %}}

{{% details title="Efektler CarPlay, akış ve arka plan oynatımıyla çalışır mı?" closed="true" %}}
Evet. Efektler BASS™ motorunun içinde çalışır, bu yüzden yerel dosyalara, bulut sürücülerine, medya sunucularına, yayınlara ve modül müziğine uygulanır ve CarPlay ile arka plan oynatımı sırasında çalışmaya devam ederler.
{{% /details %}}

{{% details title="Ses çıkış kalitesini değiştirebilir miyim?" closed="true" %}}
Evet. Ayarlar > Ses çalar içinde çıkış örnekleme hızını, kanal sayısını ve arabellek boyutunu kulaklıklarınıza, hoparlörlerinize veya DAC'nize uyacak şekilde ayarlayabilirsiniz.
{{% /details %}}

{{% details title="Kulaklıklar için iyi bir başlangıç kurulumu nedir?" closed="true" %}}
Ses Normalizasyonu'nu (Standard) açın, hafif bir Compressor (Soft) ekleyin, beğendiğiniz bir ekolayzer ön ayarı seçin ve Crossfeed'i (Chu Moy veya Jan Meier) açın. Yaratıcı bir ses istemiyorsanız reverb, echo ve distortion'ı kapalı bırakın.
{{% /details %}}

---

*BASS, Un4seen Developments Ltd'nin ticari markasıdır. Bkz. [un4seen.com](https://www.un4seen.com/). Crossfeed, bs2b (Bauer stereophonic-to-binaural) algoritmasını kullanır; bkz. [bs2b proje sayfası](https://bs2b.sourceforge.net/).*
