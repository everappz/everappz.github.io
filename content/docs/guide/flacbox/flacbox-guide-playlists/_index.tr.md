---
title: "Çalma Listeleri"
date: 2020-02-01
description: "Flacbox'ta iPhone, iPad ve Mac'te çalma listelerini nasıl oluşturacağınızı, içe aktaracağınızı, yöneteceğinizi ve özelleştireceğinizi öğrenin. Buluttan ve yerel dosyalardan çalma listeleri oluşturun, M3U / M3U8 / CUE içe aktarın, şarkıları yeniden sıralayın, kapak resmini düzenleyin, ZIP olarak arşivleyin, M3U / CSV / TXT olarak dışa aktarın ve çevrimdışı modu kullanın."
keywords: [
  "Flacbox çalma listeleri", "M3U çalma listesi içe aktarma", "çalma listesi yöneticisi",
  "iPhone'da çalma listesi oluşturma", "ses çalma listeleri Flacbox",
  "özel çalma listesi resmi", "çalma listesinden şarkı silme",
  "Flacbox çalma listesi sıralama", "VoiceOver çalma listesi yeniden sıralama",
  "Flacbox M3U dışa aktarma", "Flacbox CSV dışa aktarma", "Flacbox çalma listesi arşivi",
  "Flacbox çalma listesi çevrimdışı mod", "Flacbox CUE içe aktarma", "Flacbox yinelenen şarkılar"
]
tags: ["kılavuz", "flacbox", "çalma listeleri"]
readingTime: 7
---


Çalma Listeleri bölümünde müzik koleksiyonlarınızı yönetmek için kullanışlı araçlar bulacaksınız. Bu alan tüm çalma listelerinizi tek bir yerde gösterir. Üst kısmında, farklı çalma listesi seçeneklerini içeren bir menü açan gezinme çubuğunda bir **"..."** düğmesi ve Arama, Tümünü Oynat ve Tümünü Karıştır gibi hızlı eylemlere sahip bir araç çubuğu bulunur. Her çalma listesinin de başlığının yanında yalnızca o çalma listesine özgü daha fazla seçenek sunan kendi **"..."** düğmesi vardır.

Flacbox'taki çalma listeleri; çevrimiçi bulut parçaları, çevrimdışı indirilmiş dosyalar ve cihazınızdaki yerel dosyaların bir karışımını — hepsi tek bir çalma listesinde — içerebilir ve sorunsuz biçimde birlikte oynatılır.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Çalma Listeleri Ana Ekranı" image="/docs/guide/flacbox/img/playlists-main.webp" >}}
{{< /cards >}}

## Çalma Listesi Oluşturma

Yeni bir çalma listesi oluşturmak oldukça basittir. İki seçeneğiniz var: **+** düğmesine dokunun veya gezinme çubuğunun sağ üst köşesindeki **"..."** düğmesine dokunup Yeni Çalma Listesi seçeneğini belirleyin. Çalma listenize anlamlı bir ad verin, ardından Kaydet seçeneğine dokunun.

Bu, yeni çalma listenize dahil etmek istediğiniz parçaları seçebileceğiniz Şarkı Ekle iletişim kutusunu tetikler. Parçalar kaynak türüne göre kategorize edilmiş şekilde görünür:

- **Kitaplık** — müzik kitaplığınızda zaten bulunan parçalar.
- **Bu Uygulamadaki Dosyalar** — uygulamanın Documents klasöründeki ses dosyaları (bulut depolama alanından indirilmiş, Wi-Fi Drive aracılığıyla aktarılmış veya Finder Dosya Paylaşımı ile eklenmiş).
- **Bu Cihazdaki Dosyalar** — bu uygulamada olmayan, cihazınızın başka yerlerinde bulunan ses dosyaları.
- **Bağlantılar** — bağlı bulut depolama hizmetlerinde bulunan çevrimiçi dosyalar.

Varsayılan olarak, bir çalma listesine tek bir parçayı yalnızca bir kez ekleyebilirsiniz. Yinelenenlere izin vermek istiyorsanız Ayarlar → Müzik Kitaplığı → Çalma Listeleri → Çalma Listesindeki Yinelenenleri → Etkinleştir bölümünden bu özelliği etkinleştirin.

## Çalma Listesi İçe Aktarma

Flacbox'a M3U / M3U8 / CUE dosyası içe aktarma özelliği ekledik; böylece başka bir çalardan geçiş yaptıktan sonra çalma listelerini manuel olarak yeniden oluşturmanıza gerek kalmaz.

Önce Çalma Listeleri bölümüne gidin. Ardından sağ üst köşedeki Daha Fazla düğmesine dokunun. Menüden Çalma Listesi İçe Aktar seçeneğini belirleyin.

Sonraki ekranda dosya konumunu seçin. Desteklenen seçenekler şunlardır:

- Bağlı bulut depolama
- Uygulamadaki dosyalar
- Cihazınızdaki dosyalar

Bağlı bulut depolama seçeneğini belirleyin ve çalma listesi dosyasını içeren klasörü açın. Desteklenen çalma listesi dosya uzantıları M3U, M3U8 ve CUE'dur. Çalma listesi dosyasını seçin ve seçiminizi onaylamak için Tamamlandı seçeneğine dokunun.

Uygulama çalma listesi dosyasını ayrıştırır, parça listesi oluşturur ve müzik kitaplığına aktarılan son çalma listesini derlemek üzere bu dosyaları depolama alanında bulur. Önemli: M3U / CUE dosyası medya dosyalarına doğru yollar içermeli ve dosyaların depolama alanınızdaki bu yollarda gerçekten mevcut olması gerekir. Çalma listesi içe aktarma hakkında daha fazla bilgi için [buraya](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox) bakın.

## Çalma Listesi Ayrıntı Ekranı

Bir çalma listesini açtığınızda Çalma Listesi Ayrıntı ekranı görünür. Sağ üst köşede çalma listesi seçenekleri içeren bir **"..."** düğmesi ve kapak resminin altında üç düğme bulacaksınız: Arama, Oynatmaya Devam Et, Tümünü Oynat ve Tümünü Karıştır. Ayrıca tam çalma listesi çevrimdışı eşitlemesini açmak için bir Çevrimdışı Mod onay kutusu da mevcuttur.

- **Oynatmaya Devam Et** — bu çalma listesi için son kaydedilen oynatma konumunu geri yükler.
- **Arama** — geçerli çalma listesi içinde arama yapar.
- **Tümünü Oynat** — geçerli çalma listesindeki tüm parçaları çalar kuyruğuna ekler.
- **Tümünü Karıştır** — **Tümünü Oynat** gibi, ancak parçaları ses çalar kuyruğuna eklemeden önce karıştırır.
- **Çevrimdışı Mod** — bu çalma listesindeki tüm parçaları yerel dosyalara indirir. Çalma listesine eklenen yeni öğeler de otomatik olarak indirilir.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Çalma Listesi Ayrıntı Ekranı" image="/docs/guide/flacbox/img/playlist-details-screen.webp" >}}
{{< /cards >}}

## Çalma Listeleri Ekranındaki Çalma Listesi İçin Daha Fazla Eylem

Çalma listesi başlığının yakınındaki **"..."** düğmesine dokunarak çalma listesi eylemlerine erişebilirsiniz. Mevcut eylemler:

- **Tümünü Oynat** — çalma listesi parçalarını yeni bir çalar kuyruğuna ekler.
- **Sonra Oynat** — çalma listesi parçalarını mevcut çalar kuyruğunun başına ekler.
- **Daha Sonra Oynat** — çalma listesi parçalarını mevcut çalar kuyruğunun sonuna ekler.
- **Resmi Düzenle** — çalma listesinin kapak resmini değiştirir.
- **Çevrimdışı Modu Etkinleştir** — çalma listesi için çevrimdışı modu açar. Hem mevcut hem de yeni parçalar otomatik olarak indirilir. Çevrimdışı mod hakkında daha fazla bilgi için [buraya](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/) bakın.
- **Şarkı Listesini Dışa Aktar** — bu çalma listesini [burada](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/) açıklandığı gibi **M3U / M3U8 / CSV / TXT** olarak dışa aktarır.
- **Arşive Ekle** — bu çalma listesini (m3u dosyası, albüm kapağı ve tüm parçalar dahil) [burada](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to) açıklandığı gibi tek bir ZIP dosyasında arşivler. Premium özelliği.
- **Şarkı Ekle** — geçerli çalma listesine daha fazla şarkı ekler.
- **Yeniden Adlandır** — çalma listesini yeniden adlandırır.
- **Çalma Listesini Sil** — çalma listesini müzik kitaplığından siler. **Bu işlem geri alınamaz.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Çalma Listeleri Ana Ekranında Çalma Listesi İçin Daha Fazla Eylem" image="/docs/guide/flacbox/img/more-actions-for-playlist-in-playlists-main-screen.webp" >}}
{{< /cards >}}

## Çalma Listesi Ayrıntı Ekranındaki Çalma Listesi İçin Daha Fazla Eylem

Sağ üst köşedeki **"..."** düğmesine dokunarak çalma listesi eylemlerine erişebilirsiniz. Mevcut eylemler:

- **Seç** — parça seçim modunu etkinleştirir; çalma listesinden birden fazla parçayı silmek veya sıralarını değiştirmek için kullanışlıdır.
- **Sonra Oynat** — çalma listesi parçalarını mevcut çalar kuyruğunun başına ekler.
- **Daha Sonra Oynat** — çalma listesi parçalarını mevcut çalar kuyruğunun sonuna ekler.
- **Şarkı Ekle** — çalma listesine yeni şarkılar ekler.
- **Şarkıları Yeniden Düzenle** — çalma listesindeki şarkıların sırasını sürükle ve bırak kullanarak manuel olarak değiştirir.
- **Yeniden Adlandır** — geçerli çalma listesini yeniden adlandırır.
- **Resmi Düzenle** — geçerli çalma listesinin albüm kapak resmini değiştirir.
- **Şarkı Listesini Dışa Aktar** — bu çalma listesini **M3U / M3U8 / CSV / TXT** olarak dışa aktarır. Daha fazla bilgi için [buraya](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/) bakın.
- **Arşive Ekle** — geçerli çalma listesini tüm parçalar ve m3u dosyası dahil ZIP'ler. Daha fazla bilgi için [buraya](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to) bakın.
- **Sırala** — çalma listesindeki parçaların sırasını değiştirir. Sıralama seçenekleri şunlardır: **Şarkı Başlığı, Şarkı Numarası, Albüm, Sanatçı, Albüm Sanatçısı, Tür, Besteci, Derecelendirme, Yıl, Dakika Başına Vuruş, Süre, Dosya Adı, Dosya Değiştirme Tarihi, Dosya Oluşturma Tarihi** ve **Manuel**. **Manuel** sıralama seçeneği, sürükle ve bırak kullanarak şarkıların manuel olarak yeniden sıralanmasına olanak tanır.
- **Arama** — geçerli çalma listesi içinde belirli bir şarkıyı arar.
- **Izgara / Liste** — ekran düzeni sunumunu değiştirir.
- **Çalma Listesini Sil** — çalma listesini müzik kitaplığından siler. Bu eylem parçaları depolama alanınızdan silmez, ancak **geri alınamaz**.

## Çalma Listesindeki Şarkı Sırasını Değiştirme

Çalma listesindeki şarkıların sırasını değiştirmek için sağ üst köşedeki **"..."** düğmesine dokunun ve seçim moduna girmek için **Seç** seçeneğini belirleyin. Her parçanın yanındaki yeniden sıralama kontrolünü ve sürükle ve bırak hareketlerini kullanarak parçaları yukarı veya aşağı taşıyın. Yeniden sıralama kontrolüne dokunmak parçayı listenin en üstüne taşır. Seçim modundan çıkmak ve değişiklikleri uygulamak için **Tamamlandı** seçeneğine dokunun.

Uzun çalma listelerinde daha basit bir iş akışı için Daha Fazla Eylem → Şarkıları Yeniden Düzenle seçeneğini belirleyerek özel sürükle ve bırak yeniden sıralama moduna girin.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Çalma Listesinde Şarkıları Yeniden Düzenleme" image="/docs/guide/flacbox/img/playlist-details-rearange-songs.webp" >}}
{{< /cards >}}

## Çalma Listesi Kapak Resmini Değiştirme

Bir çalma listesinin kapak resmini değiştirmek için sağ üst köşedeki **"..."** düğmesine dokunun ve **Resmi Düzenle** seçeneğini belirleyin. Mevcut kaynaklardan (Fotoğraflar, Dosyalar, bulut depolama veya çalma listesindeki bir parçadan oluşturulan kapak resmi) bir görüntü seçin, ardından **Tamamlandı** seçeneğine dokunarak onaylayın.

## Çalma Listesine Şarkı Ekleme

Çalma listesini açın ve sağ üst köşedeki **"..."** düğmesine dokunun, ardından bir iletişim kutusu açmak için **Şarkı Ekle**'yi seçin. Eklemek istediğiniz parçaları seçin ve **Tamamlandı** seçeneğine dokunarak onaylayın.

## Çalma Listesinden Birden Fazla Şarkıyı Silme

Çalma listesini açın, sağ üst köşedeki **"..."** düğmesine dokunun ve seçim moduna girmek için **Seç** seçeneğini belirleyin. Silmek istediğiniz parçaları seçin ve ekranın alt kısmındaki **Çalma Listesinden Sil** seçeneğine dokunun. **Tamamlandı** seçeneğine dokunarak onaylayın.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Çalma Listesi Ayrıntı Ekranında Seçim Modu" image="/docs/guide/flacbox/img/selection-mode-playlist-details-screen.webp" >}}
{{< /cards >}}

## Parça Seçenekleri

Çalma listesindeki her parçanın **"..."** düğmesine dokunularak erişilebilen eylemler listesi vardır. Tüm eylemleri göremiyorsanız görüntülemek için aşağı kaydırın. Parçayı çalma listesinden silebilir, indirebilir, ses etiketlerini düzenleyebilir ve daha fazlasını yapabilirsiniz.

- **Sonra Oynat** — parçayı çalar kuyruğunun başına ekler.
- **Daha Sonra Oynat** — parçayı çalar kuyruğunun sonuna ekler.
- **Çalma Listesine Ekle** — parçayı başka bir çalma listesine ekler.
- **Favorilere Ekle** — parçayı hızlı erişim için favori olarak işaretler.
- **İndir** — parçayı çevrimdışı erişilebilir kılar. Aktarım kuyruğunda ve müzik kitaplığının **İndirilen Müzik** bölümündeki **Yerel Dosyalar** sekmesinde görünür.
- **Ses Etiketlerini Düzenle** — parça meta verilerini değiştirmek için yerleşik etiket düzenleyicisini açar.
- **Şurada Aç** — parçayı dışa aktarır ve başka bir uygulamada açar.
- **Klasörde Göster** — ses dosyasının bulunduğu klasörü ortaya çıkarır.
- **Finder'da Göster** — Mac'inizden aktarılan dosyalar için bu eylem, ses dosyasının Mac'inizdeki konumunu açar.
- **Çalma Listesinden Sil** — parçayı çalma listesinden siler.
- **Bulut Hizmetinden Sil** — parçayı çalma listesinden ve ilgili bulut hizmetinden siler. **Bu işlem geri alınamaz.**
- **Müzik Kitaplığından Sil** — parçayı müzik kitaplığından siler; dosya depolama alanında kalır.

## Erişilebilirlik

Flacbox, her bileşenin iyi tasarlanmış bir etiketi ve açıklamasının bulunduğu **VoiceOver** teknolojisiyle tamamen erişilebilirdir. VoiceOver etkin olduğunda, uygulama kullanıcı arayüzünü **Metin Moduna** çevirerek gezinme hızını ve rahatlığını artırmak için yalnızca erişilebilir ve kullanışlı öğeleri görüntüler. Ayrıca Ayarlar → Erişilebilirlik → Metin Modu bölümünden Metin Modunu etkinleştirebilirsiniz.

### VoiceOver ile Çalma Listesindeki Parça Konumunu Ayarlama

1. Bir çalma listesi açın ve **Daha Fazla** düğmesine dokunun.
2. **Şarkı Sırasını Değiştir**'i seçin. Görünüm düzenleme moduna geçer.
3. Parça başlığının yakınındaki yeniden sıralama göstergesi simgesine odak vermek için dokunun.
4. Yeniden sıralama göstergesi simgesine hızlıca **çift dokunun**. İkinci dokunuşta parmağınızı bırakmayın — hücrenin taşınmaya hazır olduğunu belirten bir ses duyulana kadar basılı tutun.
5. Artık hücreyi yeni bir konuma taşıyabilirsiniz.

Diğer bileşenler, sistem tarafından sağlanan VoiceOver kalıplarını kullanarak beklendiği gibi çalışır.
