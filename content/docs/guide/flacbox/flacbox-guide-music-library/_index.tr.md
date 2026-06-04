---
title: "Müzik Kitaplığı"
date: 2020-02-01
description: "Flacbox'ta iPhone, iPad ve Mac'te müzik kitaplığınızı nasıl oluşturacağınızı, düzenleyeceğinizi ve eşitleyeceğinizi öğrenin. Parçaları manuel olarak ekleyin veya bulut hizmetlerinden eşitleyin; meta verileri, albüm kapaklarını, çalma listelerini, favorileri, son çalınanları ve yer imlerini yönetin. Hi-Res ses desteği, MusicBrainz etiket düzenleyici, çevrimiçi ve çevrimdışı eşitleme ve kişiselleştirme seçeneklerini içerir."
keywords: [
  "Flacbox müzik kitaplığı", "buluttan müzik eşitleme", "müzik meta verisini düzenleme",
  "Flacbox ses etiketleri düzenleme", "çevrimdışı müzik eşitleme", "yerel müzik aktarma",
  "Flacbox çalma listesi yönetimi", "Flacbox albüm kapağı arama",
  "iPhone müzik meta verisi", "Flacbox uygulama kılavuzu",
  "Flacbox MusicBrainz", "Flacbox etiketleri normalleştirme",
  "Flacbox hi-res müzik kitaplığı", "Flacbox FFmpeg kitaplığı",
  "Flacbox solo albümler", "Flacbox besteci görünümü"
]
tags: ["müzik", "kılavuz", "flacbox", "kitaplık"]
readingTime: 11
---


Flacbox ile müzik kitaplığınızı yönetmek son derece kolaydır; tüm parçalarınızı — yerel FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE ve düzinelerce başka format — tek, aranabilir bir koleksiyona zahmetsizce düzenleyebilirsiniz. Müzik kitaplığınızı oluşturmak için iki seçeneğiniz var: manuel ekleme (neyin ekleneceğine tam olarak siz karar verirsiniz) veya otomatik eşitleme (Flacbox belirlenen bulut klasörlerini tarar ve yeni dosyalar göründükçe otomatik olarak ekler).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Müzik Kitaplığı Albümler Görünümü" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Manuel Ekleme

Parçaları manuel olarak eklemek için sol üst köşedeki **Müzik Ekle** simgesine dokunun ve bağlı bir bulut depolama hizmetinden klasörler ya da dosyalar ya da cihazınızdaki dosyalar arasından seçin. Kitaplığa parça eklediğinizde, yalnızca bu parçalara bağlantılar oluşturulur — gerçek dosyalar, değerli disk alanını korumak için özgün konumlarında kalır. Parçaları çevrimdışı erişilebilir kılmak istiyorsanız, seçenekler menüsündeki İndir eylemini kullanabilir veya çalma listeleri ve parça koleksiyonları için Çevrimdışı Mod'u etkinleştirebilirsiniz.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Müzik Kitaplığına Şarkı Ekleme" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

Mac sürümünde dosyaları kitaplığa sürükleyip bırakabilirsiniz. iPhone ve iPad'de ise sistem dosya seçiciden **Dosyaları Aç…** / **Klasörü Aç…** seçeneklerini kullanabilirsiniz.

## Oynatmaya Devam Et

Bu özellik uygulama ayarlarında etkinleştirilmişse, ses çalar kuyruğunu son kaydedilen konumdan geri yükler. En iyi deneyim için Ayarlar → Ses Çalar → Genel bölümünde hem **Ses Çalar Durumunu Kaydet** hem de **Oynatma Konumunu Kaydet** seçeneklerini etkinleştirin. Etkinleştirildikten sonra her klasör, albüm, sanatçı, tür ve çalma listesi ekranının üstünde bir **Oynatmaya Devam Et** düğmesi görünür — tam olarak bıraktığınız parçaya ve konuma geri dönmek için bu düğmeye dokunun.

## Konumlar

Kitaplığınızdaki tüm parçalar kaynak türüne ve müzik etiketlerine göre düşünceli biçimde gruplandırılır. Sağ üst köşedeki **Daha Fazla Eylem** düğmesine dokunup **Filtrele** seçeneğini belirleyerek şarkıları konuma göre filtreleyebilirsiniz.

### Çevrimiçi Müzik

Bu bölüm, bağlı bulut depolama hizmetlerinizdeki müzikleri gösterir. Buradaki parçalar isteğe bağlı olarak akışla oynatılır; açıkça indirmedikçe veya çevrimdışı modu etkinleştirmedikçe yerel depolama alanı kullanmaz.

### Bu Uygulamadaki Dosyalar

Burada yerel dosyalarınızdan çevrimdışı oynatma için kullanılabilen müzikleri bulabilirsiniz. Bu; uygulamanın Documents dizinindeki dosyaları kapsar — indirdiğiniz, Wi-Fi Drive aracılığıyla aktardığınız veya Finder Dosya Paylaşımı yoluyla aktardığınız her şey.

### Bu iPhone / iPad / Mac'teki Dosyalar

Bu kategori, cihazınızdan **Dosyaları Aç…** sistem iletişim kutusu aracılığıyla uygulamaya aktarılan müzikleri içerir. Özgün dosyalar kendi konumlarında kalır; Flacbox yalnızca onlara bir bağlantı tutar.

## Kategoriler

Müzik kitaplığınıza parça eklediğinizde, uygulama ses etiketlerini otomatik olarak okur ve bunları Şarkılar, Oynatılmamış Şarkılar, Albümler, Albüm Sanatçıları, Sanatçılar, Türler ve Besteciler gibi kategorilere göre düzenler.

## Etikete Göre Gruplama

Bu kategoriler, parçalarınızı müzik etiketlerine göre düzenlemenize yardımcı olur. Müzik kitaplığına parça eklediğinizde, uygulama meta verilerini okur ve bunları bu kategorilere göre gruplandırır. Tüm albümlerinizi göremiyorsanız, uygulamanın her parçayı taradığından emin olun. Tarama ilerlemesini Ayarlar → Müzik Kitaplığı → Meta Veri Okuma → Müzik Kitaplığında İşlenen Dosya Sayısı bölümünden kontrol edebilirsiniz. Yerel dosyalar için Ayarlar → Müzik Kitaplığı → Çevrimdışı Klasör Eşitleme → Yerel Klasör Taramasını Başlat seçeneğinden çevrimdışı klasörleri de yeniden tarayabilirsiniz. Meta veri okuyucu tüm işlemleri tamamladıktan sonra müzik kitaplığınızda aşağıdaki kategorileri göreceksiniz:

- **Şarkılar** — PARÇA_BAŞLIĞI etiketine göre gruplandırılmış tüm şarkılar. Sıralama düzenini sağ üst köşedeki Daha Fazla Eylem menüsünden kontrol edebilirsiniz.
- **Oynatılmamış Şarkılar** — hiç oynatılmamış tüm şarkılar.
- **Albümler** — ALBÜM_ADI etiketine göre gruplandırılmış şarkılar; sanatçı, albüm sanatçısı ve besteci etiketleri göz ardı edilir. Aynı adda ancak farklı sanatçılara ait birden fazla albümünüz varsa, aşağıda açıklanan Özel Albümler sıralamasını kullanmayı düşünün.
- **Albüm Sanatçıları** — yalnızca ALBÜM_SANATÇISI_ETİKETİ'ne göre gruplandırılmış şarkılar. Derlemeleri ve iş birliklerini solo çalışmalardan temiz biçimde ayrı tutmak için kullanışlıdır.
- **Sanatçılar** — yalnızca SANATÇI_ETİKETİ'ne göre gruplandırılmış şarkılar.
- **Türler** — TÜR etiketine göre gruplandırılmış şarkılar.
- **Besteciler** — BESTECİ etiketine göre gruplandırılmış şarkılar — "besteci"nin birincil gezinme ekseni olduğu klasik müzik kitaplıkları için vazgeçilmezdir.

## Favoriler

Ses çalar ekranından veya seçenekler menüsünden şarkıları favori olarak işaretleyebilirsiniz. Favoriler kendi bölümlerinde görünür; böylece tek dokunuşla bulabilirsiniz.

## Son Çalınanlar

Bu bölüm, son çalınan tüm parçaları gösterir. Son çalınanlar listesinin kaç öğe tutacağını Ayarlar → Kitaplık → Son Çalınanlar → Liste Boyutunu Değiştir bölümünden özelleştirebilir ve dinleme geçmişinizi yedeklemek için listeyi M3U / CSV / TXT olarak dışa aktarabilirsiniz.

## Yer İmleri

Bir şarkı çalarken sesli yer imleri oluşturabilir ve bunları bu ekranda yönetebilirsiniz — sesli kitaplar, uzun miksler, dersler veya sevdiğiniz bir parçanın nakaratını işaretlemek için mükemmeldir. Sesli yer imleriyle çalışmaya ilişkin ayrıntılı talimatlar [burada](/docs/guide/evermusic/evermusic-guide-music-library) mevcuttur.

## Üst Araç Çubuğu

Gezinme çubuğunun hemen altında bulunan üst araç çubuğu birkaç kullanışlı eylem sunar: Arama, Tümünü Oynat, Tümünü Karıştır ve Oynatmaya Devam Et. Bu araç çubuğunu basit bir aşağı kaydırma hareketiyle gösterebilir veya gizleyebilirsiniz.

## Arama

Arama özelliği, müzik kitaplığınızda belirli bir parçayı, sanatçıyı, albümü veya türü bulmanıza olanak tanır. Arama ekranında Sırala, Filtrele ve Izgara / Liste görünümü eylemlerine erişebilirsiniz. Arama, müzik kitaplığı veritabanına karşı yerel olarak çalışır; dolayısıyla tamamen çevrimdışı çalışır ve siz yazdıkça sonuçları getirir.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Müzik Kitaplığı Arama" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Seçenekler Menüsü

Müzik kitaplığınızdaki her şarkının, şarkı başlığının yakınındaki üç nokta düğmesine dokunularak erişilen daha fazla eylem içeren bir menüsü vardır. Bu eylemler, tek bir şarkı mı yoksa bir koleksiyonun parçası mı olduğuna bağlı olarak değişir.

### Bireysel Şarkılar İçin

- **Sonra Oynat** — şarkıyı çalar kuyruğunun başına ekler.
- **Daha Sonra Oynat** — şarkıyı çalar kuyruğunun sonuna ekler.
- **Çalma Listesine Ekle** — şarkıyı bir çalma listesine ekler.
- **Favorilere Ekle** — şarkıyı hızlı erişim için favori olarak işaretler.
- **İndir** — şarkıyı yerel dosyalara kaydeder. **Yerel Dosyalar** sekmesinde ve **Çevrimdışı Müzik** bölümünde görünür.
- **Ses Etiketlerini Düzenle** — eksik meta verileri düzeltmek için yerleşik ses etiketi düzenleyicisini açar; bu işlemin depolama alanınızdaki şarkıyı değiştireceğini unutmayın.
- **Klasörde Göster** — ses dosyasının depolandığı klasörü ortaya çıkarır.
- **Finder'da Göster** — Mac'inizden aktarılan dosyalar için bu eylem, ses dosyasının Mac'inizdeki konumunu açar.
- **Şurada Aç** — ses dosyasını başka bir uygulamaya aktarır.
- **Bulut Hizmetinden Sil** — dosyayı hem müzik kitaplığından hem de bulut depolama alanından kaldırır. **Bu işlem geri alınamaz.**
- **Müzik Kitaplığından Sil** — şarkıyı müzik kitaplığınızdan siler, ancak dosya depolama alanında kalır. Otomatik eşitleme etkinleştirilmişse ve dosya uzak depolama alanında mevcutsa, bir eşitleme işleminin ardından kitaplığınızda yeniden görünür.

### Şarkı Koleksiyonları İçin

Albümler, Sanatçılar, Türler veya Besteciler gibi şarkı koleksiyonları için seçenekler menüsü aşağıdaki eylemleri içerir.

- **Tümünü Oynat** — çalar kuyruğunu seçili koleksiyondaki şarkılarla değiştirir.
- **Sonra Oynat** — bu koleksiyondaki şarkıları çalar kuyruğunun başına ekler.
- **Daha Sonra Oynat** — bu koleksiyondaki şarkıları çalar kuyruğunun sonuna ekler.
- **Çalma Listesine Ekle** — bu koleksiyondaki şarkıları, yeni bir tane oluşturma seçeneğiyle birlikte bir çalma listesine dahil eder.
- **Çevrimdışı Modu Etkinleştir** — bu koleksiyondaki şarkıları yerel dosyalara indirir. Dosyalar **Yerel Dosyalar** sekmesinde ve **Çevrimdışı Müzik** bölümünde görünür. Koleksiyona sunucuda yeni öğeler eklendikçe otomatik olarak indirilir.
- **Resmi Düzenle** — şarkı koleksiyonunun albüm kapağını değiştirir.
- **Arşive Ekle** — koleksiyonun tamamını kolay yedekleme veya aktarım için tek bir ZIP dosyasında paketler (Premium özelliği).
- **Şarkı Listesini Dışa Aktar** — koleksiyonu diğer çalarlarda kullanmak veya arşivlemek amacıyla M3U, CSV veya TXT olarak dışa aktarır.
- **Müzik Kitaplığından Sil** — şarkı koleksiyonunu müzik kitaplığınızdan kaldırır. Bu eylem, gerçek dosyaları depolama alanından silmez. Otomatik eşitleme etkinleştirilmişse ve dosyalar uzak depolama alanında mevcutsa, bir eşitleme işleminin ardından kitaplığınızda yeniden görünürler.

## Seçim Modu

Sağ üst köşedeki Daha Fazla Eylem düğmesini kullanarak seçim modunu etkinleştirebilirsiniz. Bu modda, birden fazla parçayı aynı anda seçebilir ve toplu işlemler gerçekleştirebilirsiniz — çalma listesine ekleme, favori olarak işaretleme, kitaplıktan silme, indirme ve daha fazlası.

## Albüm Ayrıntısı

Sanatçı, Albüm Sanatçısı veya Besteci bölümlerini açtığınızda Şarkılar / Tüm Albümler / Özel Albümler / Solo Albümler için bir değiştirici görebilirsiniz.

- **Şarkılar** — ses etiketlerinde bu Sanatçı / Albüm Sanatçısı / Bestecinin göründüğü tüm şarkıları görüntüler.
- **Tüm Albümler** — derleme albümlerini ve sanatçının hiç bulunduğu tüm albümleri gösterir.
- **Özel Albümler** — belirtilen sanatçının söz konusu albüm adına sahip tek sanatçı olduğu albümleri gösterir.
- **Solo Albümler** — diğer sanatçıların aynı adda albümleri olsa bile yalnızca belirtilen sanatçının parçalarının yer aldığı albümleri gösterir.

Bu, büyük kitaplıklardaki dağınık "Çeşitli Sanatçılar" derlemelerini temizlemek için özellikle kullanışlıdır.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Albüm Ayrıntı Ekranı" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Ayarlar

Müzik kitaplığı tercihlerinizi yapılandırmak için Daha Fazla Eylem → Ayarlar seçeneğine dokunun.

### Meta Veri Okuma

Kitaplığa parça eklediğinizde, meta veri okuyucu çalışmaya başlar. Bu arka plan işlemi, parçalarınızdaki tüm meta verileri okur ve bunları Sanatçı, Albüm, Tür ve Besteciye göre düzenler. Veriyi daha hızlı yüklemek için meta veri okuma hızını artırabilirsiniz — daha hızlı okumanın daha fazla enerji tükettiğini unutmayın. Meta veri okuyucuyu tamamen devre dışı bırakıp etiket bilgileri yerine dosya adlarını da görüntüleyebilirsiniz.

Önemle belirtmek gerekir ki meta veri okuyucu yalnızca müzik kitaplığınızdaki meta verileri günceller; bulut hesabınızdaki veya yerel depolama alanınızdaki dosyaları değiştirmez. Ses dosyalarının meta verilerini düzenlemek istiyorsanız, seçenekler menüsündeki ilgili eylemden etkinleştirebileceğiniz yerleşik etiket düzenleyicisini kullanın.

### Meta Veri Okuyucu İçin Mevcut Modlar

- **Devre Dışı** — meta veri okuyucu kapalıdır ve ses etiketi verisi yerine dosya adları gösterilir.
- **Geçerli Şarkı** — uygulama yalnızca şu anda çalan şarkının meta verilerini okur. Meta veri okuyucunun bulut sunucusuna çok sayıda istek göndermesini önlemek ve oynatma kesintilerine yol açmamak için yavaş bir ağ bağlantınız varsa bu seçeneği kullanın.
- **Oynatma Kuyruğu** — uygulama, ses çalar kuyruğundaki tüm şarkıların meta verilerini okur.
- **Kitaplık** — uygulama, müzik kitaplığındaki tüm şarkıların meta verilerini okur.

**Arka Planda Meta Veri Okuma** anahtarı açıkken, meta veri okuyucu arka plan modunda çalışmaya devam eder. Uygulamanın ses oynatma sırasında çok fazla enerji tüketmesi durumunda iOS işletim sistemi onu askıya alabilir.

Bu nedenle, büyük bir müzik koleksiyonunuz varsa meta veri eşitlemesi için uygulamanın masaüstü sürümünü kullanmanız önerilir. Ardından eşitlenmiş kitaplığı masaüstünden mobil cihaza aktarmak için uygulama ayarlarındaki Veri Yedekleme ve Geri Yükleme özelliğini kullanabilirsiniz.

**Meta Veri Kodlamasını Normalleştir** seçeneği etkinleştirildiğinde, uygulama müzik kitaplığındaki tüm şarkıların meta veri kodlamasını otomatik olarak normalleştirir. Bu, ses etiketi kodlamasının bozulduğu durumlarda (örneğin Windows PC'de dosya düzenlendikten sonra) yaşanan sorunları giderir ve parça bilgilerinde yanlış karakterlerin görünmesini önler.

**Meta Veriyi Yenile** eylemi, müzik kitaplığınızdaki her dosyayı eksik meta verisi olarak işaretler; bu da meta veri okuyucunun her kaydı yenilemesini tetikler.

Okuyucuyu manuel olarak tetiklemek için **Meta Veri Okumayı Başlat** seçeneğine dokunun. İşlemin ilerlemesi aşağıda gösterilir.

### Çevrimiçi Eşitleme

Otomatik çevrimiçi müzik eşitleme, bağlı bulut hizmetlerinden parçaları müzik kitaplığına otomatik olarak eklemenizi sağlar. Bu özelliği etkinleştirmek için Müzik Kitaplığı Ayarları'na gidin ve eşitleme klasörlerini seçin.

Bu seçenek etkinleştirildiğinde, uygulama seçilen tüm klasörleri tarar, desteklenen ses dosyalarını belirler ve bunları kitaplığınıza sorunsuz biçimde entegre eder. İlgili menü eylemini kullanarak eşitlemeyi başlatabilir veya durdurabilirsiniz.

Çevrimiçi müzik eşitlemesi yalnızca uygulama ön planda olduğunda çalışır; bu da büyük bir kitaplığı eşitlemenin biraz zaman alabileceği anlamına gelir. Süreci hızlandırmak için uygulamayı açık bırakın, cihazınızı bir güç kaynağına bağlayın ve uygulama ayarlarında Ekran → Her Zaman Aktif seçeneğini etkinleştirin.

Alternatif olarak, çevrimiçi müzik eşitlemesini uygulamanın masaüstü sürümünde gerçekleştirebilir ve müzik kitaplığını Yedekleme ve Geri Yükleme özelliğini kullanarak iOS sürümüne aktarabilirsiniz.

Çevrimiçi müzik kitaplığınızı ne sıklıkla eşitlemek istediğinizi de ayarlayabilirsiniz. Aralığı Hemen olarak ayarlarsanız, uygulamayı her açtığınızda çevrimiçi eşitleme başlar.

### Çevrimdışı Eşitleme

Burada çevrimdışı müzik eşitlemesini yapılandırabilirsiniz.

#### Eşitlenen Çevrimdışı Klasörler

Bir bulut klasörünü çevrimdışı kullanıma hazır hale getirdiğinizde (Daha Fazla Eylem menüsü aracılığıyla), Yerel Dosyalar → Çevrimdışı Klasörler bölümünde görünür. Uygulama içeriğini cihazınıza indirir. Klasörde değişiklik yaparsanız — dosya ekleme, kaldırma veya güncelleme gibi — uygulama bu değişiklikleri algılar ve yerel kopyayı otomatik olarak günceller.

Bu ekranda çevrimdışı klasör eşitlemesini manuel olarak başlatabilir, çevrimdışı klasörü kapsayan klasörde ortaya çıkarabilir ve klasör için çevrimdışı modu devre dışı bırakabilirsiniz. Çevrimdışı modun devre dışı bırakılması, tüm yerel dosya kopyalarını cihazınızdan kaldırır.

#### Zaman Aralığı

Uygulamanın çevrimdışı klasörlerdeki değişiklikleri ne sıklıkla kontrol edeceğini ayarlayabilirsiniz.

#### Yerel Klasör Taramasını Başlat

Bu seçenek, desteklenen ses dosyalarını bulmak için uygulamanın Documents dizinindeki tüm yerel klasörleri tarar. Bu yerel dosyaların tamamı müzik kitaplığınıza sorunsuz biçimde eklenir. Cihazınızda ancak bu uygulamanın dışında bulunan yerel dosyalar, iOS / macOS güvenlik kısıtlamaları nedeniyle uygulama Documents dizini dışındaki dosyalara erişilememesi nedeniyle müzik kitaplığına manuel olarak eklenmelidir.

#### Önemli

Müzik kitaplığınızı yerel dosyalarınızla güncel tutmak için çevrimdışı müzik eşitlemesini periyodik olarak başlatmanız önerilir.

### Kişiselleştirme

Bu bölümde, müzik kitaplığı ekranının stilini tercihlerinize göre yapılandırabilirsiniz. Üç seçenek mevcuttur: Düz Menü, Gruplandırılmış Menü, Sekmeli Menü. Ayrıca albüm ayrıntı ekranlarında albüm kapaklarının gösterilmesini etkinleştirebilir veya devre dışı bırakabilirsiniz.

### Albüm Kapaları

Burada uygulamanın albüm kapak resimlerini nasıl yüklediğini ve sakladığını yapılandırabilirsiniz.

- **Ağ Türü** — kapak indirmeleri için Wi-Fi veya Wi-Fi & Hücresel Veri seçin.
- **Çevrimiçi Dosyalar İçin Albüm Kapaklarını Yükle** — etkinleştirildiğinde, bulut depolama alanında depolanan dosyalar için gömülü albüm kapaklarını yükler. Bu, ek ağ verisi kullanabilir.
- **Klasörde Ara** — etkinleştirildiğinde, bir parçanın gömülü kapağı yoksa uygulama aynı klasörde JPEG veya PNG görüntülerini arar ve bunları albüm kapak resmi olarak kullanır.
- **Kapak Kalitesi** — cihazınızda depolanan albüm kapak resimlerinin kalitesini seçin.
- **Klasörde Göster** — albüm kapaklarının önbelleğe alındığı klasörü açın; böylece yönetebilir veya yedekleyebilirsiniz.
- **Tümünü Sil** — önbelleğe alınmış albüm kapaklarını silerek depolama alanını boşaltın ve uygulamayı isteğe bağlı olarak yeniden yüklemeye zorlayın.

Varsayılan olarak, uygulama parçalarınızdaki gömülü albüm kapaklarını kontrol eder ve mevcutsa bunları görüntüler. Gömülü albüm kapak resmi yoksa ve **Klasörde Ara** seçeneği etkinleştirilmişse, uygulama kapsayan klasörde JPEG veya PNG görüntülerini kontrol eder ve o klasördeki tüm parçalar için albüm kapak resmi olarak kullanır.

### Çalma Listeleri

Aynı şarkıyı bir çalma listesine iki kez ekleme seçeneğini etkinleştirebilirsiniz. Bu seçenek varsayılan olarak devre dışıdır.

### Son Çalınanlar

Son çalınan şarkılar listenizi yönetebilirsiniz.

- **Listeyi Sil** — son çalınan şarkıların listesinin tamamını siler.
- **Liste Boyutunu Değiştir** — listede görünen öğe sayısını ayarlar.
- **Şarkı Listesini Dışa Aktar** — son çalınan şarkılar listenizi M3U, CSV veya TXT olarak dışa aktarır. Ayrıntılı talimatlar [burada](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/) mevcuttur.

### Favoriler

Favori şarkılar listenizi yönetebilirsiniz.

- **Eş Zamanlı Düzenleme** — etkinleştirildiğinde, bir şarkıyı favorilere eklemek hem müzik kitaplığında hem de dosyalar bölümünde aynı anda eklenmesini sağlar.
- **Listeyi Sil** — favori şarkıların listesinin tamamını siler.
- **Şarkı Listesini Dışa Aktar** — Son Çalınanlar'a benzer şekilde, favoriler listesini M3U, CSV veya TXT olarak dışa aktarır.

### Kitaplığı Sil

Bu eylem müzik kitaplığı veritabanını siler, ancak müzik dosyalarınıza depolama alanında dokunmaz.

### İçerik Yükleme Sınırı

Varsayılan olarak uygulama, içerik yükleme süresini azaltmak ve büyük kitaplıkları duyarlı tutmak için sayfalama kullanır. Ancak bu seçeneği devre dışı bırakıp uygulamanın tüm mevcut verileri aynı anda yüklemesine de izin verebilirsiniz. Bunu yapmak için uygulama ayarlarını açın, Kişiselleştirme → İçerik Yükleme Sınırı bölümüne inin ve Devre Dışı seçeneğini belirleyin.
