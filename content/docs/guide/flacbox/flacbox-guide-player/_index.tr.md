---
title: "Ses Çalar"
date: 2020-02-01
description: "Flacbox ses çalarını iPhone, iPad ve Mac'te nasıl kullanacağınızı öğrenin. Oynatmayı kontrol edin, kuyrukları yönetin, FFmpeg / sistem ses motorunu yapılandırın, örnekleme hızını, ses tonu düzeltmeyi, IO tampon süresini, ekolayzerı, ses yer imlerini, AirPlay 2, Google Cast, CarPlay, widget'ları ve Mac klavye kısayollarını ayarlayın."
keywords: [
  "Flacbox çalar kılavuzu", "ses çalar ayarları", "Flacbox ekolayzer",
  "AirPlay müzik akışı", "Google Cast müzik", "ses yer imleri",
  "Flacbox oynatma kuyruğu", "Flacbox tekrar karıştır", "Flacbox ses kontrolü",
  "macOS mini oynatıcı", "voiceover müzik uygulaması",
  "Flacbox FFmpeg", "Flacbox ses tonu düzeltme", "Flacbox örnekleme hızı",
  "Flacbox harici DAC", "Flacbox surround ses", "Flacbox IO tamponu",
  "Flacbox oynatma hızı", "Flacbox uyku zamanlayıcısı"
]
tags: ["kılavuz", "flacbox", "çalar"]
readingTime: 14
---


Ses Çalar, müziği kontrol ettiğiniz ve oynatma özelliklerinin çoğunu yönettiğiniz uygulamanın ana ekranıdır. Aynı zamanda Flacbox'ın sistem kodekleri ve paketlenmiş **FFmpeg** kitaplığı üzerine inşa edilen hi-res ses motorunun ağır yükü taşıdığı yerdir. Nasıl kullanılacağını keşfedelim.

## Ses Çalara Erişim

Tam ekran oynatıcıya mini oynatıcı çubuğundan ulaşabilirsiniz. iPhone'da mini oynatıcı ana ekranın alt kısmında bulunur. iPad ve Mac'te sol taraftadır. iPhone'da mini oynatıcıyı gizlemek için bir kez dokunun ve aşağı kaydırın. Tam ekran oynatıcıyı tamamen kapatmak için sağ alt köşedeki kapat düğmesine dokunun.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Ses Çalar Ana Ekranı" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Desteklenen Ses Formatları

Flacbox, en popüler ses formatlarını oynatır — hem Apple'ın sistem kodekleri hem de paketlenmiş FFmpeg motoru tarafından işlenen pek çok ek format:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

Bu liste, kişisel bir müzik koleksiyonunda bulunması muhtemel neredeyse her modern kayıplı ve kayıpsız formatı kapsar.

## Oynatma Kontrolleri

Oynatıcı ekranının alt kısmında Oynat, Duraklat, Sonraki Parça ve Önceki Parça düğmelerini göreceksiniz. Ayrıca uygulama ayarlarından etkinleştirebileceğiniz İleri 30 sn ve Geri 30 sn gibi isteğe bağlı düğmeler de vardır (sesli kitaplar için kullanışlıdır). Sonraki / Önceki düğmelerine basılı tutarak hızlı ileri veya geri alabilirsiniz. Bir parçanın belirli bir bölümüne geçmek için oynatma kaydırıcısını sürükleyin.

## Tekrar ve Karıştır

Tekrar modları arasında geçiş yapmak için tekrar düğmesine dokunun:

- **Tümünü Tekrarla** — kuyruğunuzdaki tüm parçaları döngüye alır.
- **Birini Tekrarla** — yalnızca geçerli parçayı tekrarlar.
- **Tekrarda Dur** — geçerli parça bittiğinde duraklatır.
- **Tekrar Yok** — kuyruğu tekrarlamadan bir kez çalar.

Kuyruktaki parçaların sırasını rastgele yapmak için **Karıştır** düğmesini kullanın.

## Ses Kontrolü

Ses kaydırıcısına erişmek için oynatma kontrollerinin altındaki ses simgesine dokunarak Ses Ayarları ekranını açın. Burada, oynatmayı başka bir cihaza hızlıca geçirmek için **Google Cast** ve **AirPlay** düğmelerini de bulacaksınız.

## Google Cast (Chromecast)

Google Cast kullanıcıları için, oynatıcının alt kısmında **Cast** simgesi görünür. Cihaz seçip akışı başlatmak için bu simgeye dokunun. Cihazınızın ve Google Cast alıcısının aynı Wi-Fi ağında olduğundan emin olun. Not: Her ses formatı Google Cast ile uyumlu değildir — bazı hi-res formatların dönüştürülmesi gerekebilir.

## AirPlay

AirPlay için oynatıcının alt kısmındaki **AirPlay** düğmesini arayın. Akış için bir cihaz seçmek üzere bu düğmeye dokunun. Flacbox, **AirPlay 2**'yi destekler; dolayısıyla aynı anda birden fazla HomePod, Apple TV veya AirPlay 2 uyumlu hoparlöre oynatabilirsiniz.

## Ses Ekolayzerı

Flacbox, iPod tarzı ön ayarlara sahip **10 bantlı bir ekolayzer** içerir. Ses görünümünde Ekolayzer seçeneğine dokunun, ardından sağ üst köşeden açın. Acoustic ve Bass Booster gibi ön ayarları kullanabilir veya her frekans bandını kaydırıcılarla ayarlayabilirsiniz. Kendi ön ayarlarınızı oluşturun, herhangi bir ad altında kaydedin ve ön yükselteç ile genel sesi artırın. Ekolayzerı nasıl kullanacağınıza ilişkin daha ayrıntılı talimatlar [burada](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox) mevcuttur.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Ses Çalar Ekolayzerı" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Oynatıcı Modu Araç Çubuğu

Bazı oynatıcı stilleri için, tam ekran oynatıcının üst kısmında özel bir araç çubuğu bulunur. Bu araç çubuğunda üç kullanışlı düğme yer alır:

- **Arama** — çalar kuyruğunuzdaki belirli bir parçayı hızlıca bulun.
- **Oynatma Hızı Kontrolü** — oynatma hızını 0,02× ile 3,00× arasında ayarlayın. Sesli kitaplar, podcast'ler ve dersler için mükemmeldir. Varsayılan hıza geri dönmek için Normal'e dokunun.
- **Ses Yer İmleri** — parça başına birden fazla yer imi oluşturun. Yer imlerini nasıl kullanacağınıza ilişkin tam talimatlar [burada](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic) mevcuttur.

## Oynatıcı Kuyruğu

Oynatıcı kuyruğunuzu görmek için geçerli şarkının sağ tarafındaki kuyruk düğmesine dokunun. Kuyruktaki her şarkının daha fazla eylemi vardır — bunları görüntülemek için üç noktaya dokunun. Kuyruktaki bir şarkıyı yeniden sıralamak için başlığın yakınındaki yeniden sıralama göstergesini kullanın ve yeni bir konuma sürükleyin.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Oynatma Kuyruğu" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Yorumlar / Şarkı Sözleri

Parça yorumlarını ve gömülü şarkı sözlerini ve LRC dosyalarını görüntülemek için şu adımları izleyin:

1. **Ayarlar**'ı açın.
2. **Ses Çalar**'a gidin.
3. **Kişiselleştirme**'yi seçin.
4. **Ana ekrandaki düğmeler**'e dokunun.
5. **Yorumlar**'ı etkinleştirin.

Bundan sonra, kapak resmi / kuyruk görünümünden yorumlar görünümüne geçmek için ekranın alt kısmındaki oynatıcı kuyruğu düğmesine birkaç kez dokunun. Yorumlar ekranında **Yorumlar**, **Gömülü Şarkı Sözleri** ve **LRC Dosyası** arasında geçiş yapmak için sağa kaydırın. Tam talimatlar [burada](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox) mevcuttur.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Şarkı Sözleri ve Yorumlar Ekranı" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Seçenekler Menüsü

Ses çalar kuyruğundaki her şarkının, şarkı başlığının yakınındaki üç nokta düğmesine dokunularak erişilen daha fazla eylem içeren bir menüsü vardır.

- **Sonra Oynat** — şarkıyı çalar kuyruğunun başına ekler.
- **Çalma Listesine Ekle** — şarkıyı, yeni bir tane oluşturma seçeneğiyle birlikte bir çalma listesine dahil eder.
- **Favorilere Ekle** — şarkıyı hızlı erişim için favori olarak işaretler.
- **İndir** — şarkıyı yerel dosyalara kaydeder; **Yerel Dosyalar** sekmesinde ve **Çevrimdışı Müzik** bölümünde görünür.
- **Ses Etiketlerini Düzenle** — eksik meta verileri düzeltmek için yerleşik ses etiketleri düzenleyicisini açar; bu işlem depolama alanınızdaki şarkıyı değiştirir.
- **Klasörde Göster** — ses dosyasının depolandığı klasörü ortaya çıkarır.
- **Finder'da Göster** — Mac'inizden aktarılan dosyalar için bu eylem, ses dosyasının Mac'inizdeki konumunu açar.
- **Şurada Aç** — ses dosyasını başka bir uygulamaya aktarır.
- **Kuyruktan Sil** — seçili şarkıyı ses çalar kuyruğundan kaldırır.
- **Bulut Hizmetinden Sil** — şarkıyı hem müzik kitaplığından hem de bulut depolama alanından siler. **Bu işlem geri alınamaz.**
- **Yerel Dosyalardan Sil** — şarkıyı hem müzik kitaplığından hem de yerel depolama alanından siler. **Bu işlem geri alınamaz.**
- **Müzik Kitaplığından Sil** — şarkıyı müzik kitaplığınızdan siler; dosya depolama alanında kalır.

Aynı seçenekler, ses çalar kuyruğundaki şu an çalan öğe için de mevcuttur; parça başlığının yakınındaki **Daha Fazla Eylem** simgesine dokunarak erişebilirsiniz.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Oynatma Kuyruğundaki Öğe İçin Seçenekler" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Ek Oynatıcı Eylemleri

Ek eylemleri görmek için şu anda çalan şarkı başlığının sol tarafındaki **Daha Fazla Eylem** "..." düğmesine dokunun.

- **Oynatmaya Devam Et** — kuyruk ve medya konumu dahil olmak üzere kaldığınız yerden devam edin. Sesli kitaplar için özellikle kullanışlıdır. Uygulama ayarlarında etkinleştirilir.
- **Arama** — ses çalar kuyruğunuzda belirli bir parçayı hızlıca bulun.
- **Yer İmleri** — oluşturulan ses yer imlerinin listesini görüntüleyin.
- **Yorumlar** — parça yorumlarını ve gömülü şarkı sözlerini ve LRC dosyalarını görüntüleyin. Tam talimatlar [burada](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Hız** — oynatma hızını tercihinize göre ayarlayın.
- **Son Çalınanlar** — son çalınan şarkıların listesine erişin.
- **Favoriler** — favorilere eklenen şarkılar koleksiyonunuzu görüntüleyin.
- **Ses Ekolayzerı** — ses ekolayzerını etkinleştirin.
- **Uyku Zamanlayıcısı** — belirli bir süre sonra oynatmayı durdurmak için bir zamanlayıcı ayarlayın. Müzikle uyuyakalmak istediğiniz anlar için harikadır.
- **Kuyruğu Çalma Listesi Olarak Kaydet** — geçerli ses çalar kuyruğunu yeni bir çalma listesi olarak kaydedin.
- **Kuyruğu Sil** — çalar kuyruğunu temizleyin ve oynatmayı durdurun.
- **Ayarlar** — ses çalar ayarlarına erişin.
- **Yardım** — yardım ve rehberlik bulun.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Ses Çalar Daha Fazla Eylem Ekranı" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Ses Yer İmleri

Bu özellik, müzik kitaplığınızdaki parçalar için birden fazla yer imi oluşturmanızı sağlar — sesli kitaplar, dersler, uzun DJ miksleri veya sevdiğiniz bir parçanın nakaratını işaretlemek için mükemmeldir.

Yeni bir yer imi oluşturmak için:

- İstediğiniz şarkıyı çalmaya başlayın.
- Oynatıcı ekranını açın.
- Oynatıcı modu araç çubuğundaki **Yer İmleri** düğmesine dokunun.
- **Yer İmi Ekle**'yi seçin.
- Yer imi zamanını seçin ve sağ üst köşedeki **Tamamlandı**'ya dokunun.

Geçerli parça için yer imlerini düzenlemek kolaydır: düzenleme moduna girmek için sağ üst köşedeki Düzenle seçeneğine dokunun. Bu modda yer imlerini yeniden düzenleyebilir, silebilir, yer imi zamanını ayarlayabilir ve yer imi başlıklarını değiştirebilirsiniz. Ses yer imleri hakkında daha ayrıntılı talimatlar [burada](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic) mevcuttur.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Ses Yer İmleri Ekranı" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Son Çalınanlar ve Favoriler

Oynatıcı ekranında Son Çalınanlar ve Favoriler'e erişmek için üç noktaya dokunun. Her iki bölümde de şarkı arayabilir, tümünü oynatabilir, tümünü karıştırabilir, listeyi dışa aktarabilir ve listeyi temizleyebilirsiniz. Şarkı listelerini nasıl dışa aktaracağınıza ilişkin ayrıntılı talimatlar [burada](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/) mevcuttur.

## Apple CarPlay (iPhone)

iPhone'unuzu USB veya kablosuz Apple CarPlay ile arabanıza bağlayın; Flacbox CarPlay ana ekranınızda görünür ve sürüş sırasında güvenli biçimde müzik çalmaya hazır olur. CarPlay arayüzü; Kitaplık, Bağlantılar, Yerel Dosyalar ve Ayarlar için özel sekmeler içerir; oynatma kontrolleri, karıştırma, tekrarlama, kuyruk yönetimi ve ses ekolayzerı telefonunuzu elinize almadan kullanılabilir. Ayarlar → CarPlay bölümünden CarPlay deneyimini daha da yapılandırın — sıralama seçenekleri, sayfalama, menü simgeleri gradyan rengi, görüntülerin yüklenip yüklenmeyeceği ve CarPlay bağlandığında oynatmayı otomatik duraklatma seçeneği.

[CarPlay kılavuzunun tamamını okuyun](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Apple CarPlay'de" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Ana Ekran Widget'ları (iPhone ve iPad)

Flacbox, oynatmayı bir bakışta görmek ve kontrol etmek için iOS Ana Ekran ve Kilit Ekranı widget'larını destekler. Ayarlar → Widget'lar → Widget'ları Etkinleştir bölümünde Widget'ların etkinleştirildiğinden emin olun, ardından Ana Ekran'ınıza veya Kilit Ekranı'nıza uzun basın, **+** simgesine dokunun, **Flacbox**'ı arayın ve bir widget ekleyin. Widget, oynatma sırasında şu an çalan parçanın kapak resmini, başlığını ve sanatçısını gösterecek şekilde yenilenir.

## Mini Oynatıcı Penceresi (Yalnızca Mac)

Mac kullanıcıları, kompakt, her zaman üstte mini oynatıcı kullanabilir. İmlecinizi Flacbox penceresinin sağ alt köşesine getirin, en küçük boyutuna küçültün ve daralt düğmesine dokunun. Menü çubuğunda Pencere → Pencereyi Her Zaman Üstte Göster seçeneğini belirleyerek her zaman diğer pencerelerin üstünde tutun — başka bir uygulamada çalışırken müzik kontrollerini görünür tutmak için mükemmeldir.

## Klavye Kısayolları (Yalnızca Mac)

Mac kullanıcıları için, durum çubuğunda klavye kısayollarına sahip bir sistem oynatma menüsü mevcuttur. Örneğin, Oynat / Duraklat için boşluk çubuğuna basın. Durdur, Sonraki Şarkı, Önceki Şarkı, Zaman Atla, Tekrar, Karıştır ve Oynatma Hızı için kısayollar da mevcuttur.

## Ses Çalar Ayarları

Ayarlara erişmek için oynatıcı ekranındaki Daha Fazla düğmesine dokunun ve Ayarlar'ı seçin. Burada aşağıda listelenen birkaç bölüm bulacaksınız.

### Genel

Bu ayarlar, oynatma kuyruğu, ses çıkışı ve oynatıcının durumunu kaydetme dahil olmak üzere ses çaların temel yönlerini kapsar.

- **Tekrar Modu** — bir parça bittiğinde ses çaların nasıl davranacağını seçin:
  - **Tümünü Tekrarla** — kuyruğunuzdaki tüm parçaları yeniden çalar.
  - **Birini Tekrarla** — yalnızca geçerli parçayı tekrarlar.
  - **Tekrarda Dur** — geçerli parça bittiğinde oynatmayı duraklatır.
  - **Tekrar Yok** — kuyruğunuzun tekrarlamadan çalınmasına izin verir.
- **Karıştır Modu** — kuyruğunuzdaki parçaların sırasını rastgele yapın. **Karıştırmayı Kapat** veya **Karıştırmayı Aç** seçeneklerinden birini belirleyebilirsiniz.
- **Ses Kodeki** — oynatma için kullanılan ses motorunu seçin:
  - **Sistem Kodeki + FFmpeg** — uyumluluk ve kararlılığı artırmak için mümkün olan durumlarda sistem ses kodekini önceliklendirir. Bu modda ses tonu düzeltme ve ses çıkışı örnekleme hızı ayarlamaları sınırlı olabilir.
  - **FFmpeg** — tüm ses dosyaları için FFmpeg kodekini zorlar; ses tonu düzeltme ve ses çıkışı örnekleme hızını ayarlamanıza olanak tanır.
- **Ses Çıkışı Örnekleme Hızı** — özellikle harici DAC ile ses kalitesini optimize etmek için ses çıkışı örnekleme hızını ayarlayın. Mevcut değerler: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** ve **96 kHz**.
- **Ses Çıkışı Kanal Sayısı** — harici DAC'lı çok kanallı ses sistemleri için kanal sayısını belirtin: **Mono, Stereo, Merkez / Sol / Sağ, Merkez / Sol / Sağ / Surround, ITU BS.775-1, 5.1 Surround** ve **SDDS**.
- **Ses Çıkışı Tercih Edilen IO Tampon Süresi** — ses oynatma için giriş / çıkış tamponu süresini yapılandırın. Yüksek çözünürlüklü ses oynatırken gecikmeyi en aza indirmek için tipik bir değer yaklaşık **5 milisaniye (0,005 saniye)**'dir. Kabul edilebilir tampon boyutu donanım ve yazılım ortamınıza bağlıdır; dolayısıyla hedef cihazınızda farklı süreleri test edin ve düşük gecikme ile sorunsuz oynatmayı en iyi dengeleyen seçeneği belirleyin.
- **Ses Çıkışı Modu (Yalnızca iOS)** — Flacbox'ın sesinin diğer uygulamalarla harmanlanmasını sağlamak için karışık ses çıkışı modunu yapılandırın. Ayrıntılı talimatlar [burada](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Oynatma Konumunu Kaydet** — uygulamanın müzik kitaplığınızdaki şarkıların oynatma konumunu kaydedip geri yüklemesini sağlar.
- **Ses Çalar Durumunu Kaydet** — uygulamayı kapatmadan önce ses çalarınızın durumunu korur. Oynatmaya devam etmek için uygulamayı yeniden açtığınızda herhangi bir klasör, albüm, sanatçı veya tür ekranının üst kısmındaki **Oynatmaya Devam Et** seçeneğine dokunun. Belirli dosyalar için oynatmayı, o parçaya dokunarak da geri yükleyebilirsiniz.

**Oynatma Konumunu Kaydet** ve **Ses Çalar Durumunu Kaydet** seçeneklerinin her ikisini de etkinleştirdikten sonra herhangi bir klasör, albüm, sanatçı veya türü açın; ekranın üst kısmında son kaydedilen parça ve konum ile birlikte bir **Oynatmaya Devam Et** düğmesi göreceksiniz. Kaldığınız yerden devam etmek için bu düğmeye dokunun.

### Kişiselleştirme

Kişiselleştirme, ses çalar ekranının görünümünü özelleştirmenize, ana ekranda, kilit ekranında ve durum çubuğunda kullanılabilen kontrolleri değiştirmenize ve zaman atlama kontrollerini yapılandırmanıza olanak tanır.

- **Ses Çalar Ekranı Stili** — ses çalar ekranındaki öğelerin konumlandırmasını yapılandırın.
- **Albüm Kapakları Kaydırma Stili** — albüm kapakları için tercih edilen kaydırma stilini yapılandırın.
- **Ek Öğeler** — ses çalar ekranında ekstra öğeleri etkinleştirin. **Ses Formatı Bilgisi**, kapak resminin üzerinde şu an çalan parçanın ses bilgilerini gösterir; **Ses Seviyesi Kaydırıcısı**, oynatma kontrollerinin altında ses çıkış kaydırıcısını gösterir.
- **Ana Ekran Eylemleri** — varsayılan olarak ana ses çalar ekranında hangi düğmelerin görünmesi gerektiğini yapılandırın: **Tekrar ve Karıştır Modu, Sonraki ve Önceki Şarkı, Zaman Atla, Uyku Zamanlayıcısı, Google Chromecast, AirPlay ve Bluetooth, Ses Ekolayzerı, Arama, Yer İmleri, Hız, Yer İmi Ekle, Favorilere Ekle, Yorumlar** ve daha fazlası.
- **Kilit Ekranındaki Oynatma Kontrolleri** — kilit ekranında hangi kontrollerin görüneceğini seçin. Olası değerler: **Zaman Atla, Yer İmi Ekle, Favorilere Ekle**.
- **Zaman Atlama Düğmeleri** — **Zaman Atla** düğmeleri için zaman aralığını seçin.

### Dosya Yükleme

Dosya yükleme işlemi sırasında şarkıları yüklemek için kullanılan ağ türünü değiştirebilirsiniz. Mevcut seçenekler: **Wi-Fi**, **Wi-Fi & Hücresel Veri**.

- **Ön Yükleme Süresi** — tamponlama zaman aralığını ayarlayın. Zayıf ağ bağlantınız varsa bu değeri artırın.
- **Doğrudan URL Kullan** — etkinleştirildiğinde, sunucu destekliyorsa şarkıyı yüklemek için doğrudan URL kullanılır. Bu, şarkı yüklemeyi hızlandırabilir ancak oynatma kararlılığını etkileyebilir.

### Ses Ekolayzerı

Ses ekolayzerı ayarlarını özelleştirin. Ses ekolayzerını yapılandırma hakkında daha fazla bilgi için [buraya](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox) bakın.

### Oynatma Hızı

Ses çaların oynatma hızını **0,02× ile 3,00×** arasında ayarlayın. Daha ince ayarlar için **hassas moda** geçmek üzere sağ üst köşedeki yapılandırma simgesine dokunun.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Oynatma Hızı Ekranı" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Ses Tonu Düzeltme

Önceden tanımlanmış değerleri kullanarak ses tonu düzeltme ayarlarını değiştirin. Sağ üst köşedeki düğmeye dokunarak önceden tanımlanmış değerler ve hassas mod arasında geçiş yapabilirsiniz. Ses tonu düzeltme FFmpeg kodek yolunda mevcuttur; aralık **-1000 ile +1000** arasındadır.

### Oynatma Önbelleği

Ses çalar kuyruğundaki şarkılar, sorunsuz oynatmayı sağlamak için otomatik olarak indirilir. Ses dosyalarını manuel olarak indirirseniz, kopyaları önlemek için bu seçeneği devre dışı bırakabilirsiniz. Ses çalar önbellek boyutunu da burada yapılandırabilirsiniz.

### Uyku Zamanlayıcısı

Belirli bir süre sonra oynatmayı otomatik olarak durdurmak için bir zamanlayıcı etkinleştirin — müzikle uyuyakalmak istediğinizde kullanışlıdır. Dakika dakika hassasiyet için **hassas mod** kullanmak üzere sağ üst köşedeki yapılandırma simgesine dokunun.

## Erişilebilirlik

Flacbox, **VoiceOver** ile tamamen erişilebilirdir. Her bileşenin iyi tasarlanmış bir etiketi ve açıklaması vardır. VoiceOver etkin olduğunda, uygulama **Metin Moduna** geçerek yalnızca anlamlı öğelerin yüzeye çıkarılmasını sağlar — gezinme hızını ve netliğini artırır. Ayrıca **Ayarlar → Erişilebilirlik → Metin Modu** bölümünden Metin Modunu etkinleştirebilirsiniz.

### VoiceOver ile Kaydırıcıları Ayarlama

1. **Kaydırıcıyı seçin** — VoiceOver duyurulana kadar sola veya sağa kaydırın.
2. **Değeri ayarlayın** — kaydırıcıya çift dokunun ve basılı tutun, ardından değeri hızlıca değiştirmek için yukarı veya aşağı sürükleyin. VoiceOver, ilerledikçe yeni değeri duyurur.

### VoiceOver ile Listede Parça Konumunu Ayarlama

1. Parça başlığının yakınındaki yeniden sıralama göstergesi simgesine odak vermek için dokunun.
2. Yeniden sıralama göstergesine hızlıca çift dokunun. İkinci dokunuşta parmağınızı bırakmayın — hücrenin taşınmaya hazır olduğunu belirten bir ses duyulana kadar basılı tutun.
3. Hücreyi yeni konumuna taşıyın.

Diğer bileşenler, sistem tarafından sağlanan VoiceOver kalıplarını kullanarak beklendiği gibi çalışır.
