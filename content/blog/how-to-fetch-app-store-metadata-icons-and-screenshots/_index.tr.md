---
title: "App Store Meta Verileri, Simgeler ve Ekran Görüntüleri Ücretsiz Nasıl Alınır"
date: 2026-06-13
description: "Resmi iTunes Search API ile çalışan ücretsiz bir tarayıcı aracı olan AppLookup.pro kullanarak herhangi bir iOS uygulamasının meta verilerini, simgesini, ekran görüntülerini ve yerelleştirilmiş App Store bilgilerini almak için adım adım kılavuz."
keywords: [
  "app store meta verileri", "app store verisi alma", "app store simge indirme",
  "app store ekran görüntüleri indirme", "app store arama aracı", "itunes search api",
  "uygulama meta veri çıkarıcı", "iOS uygulama meta verileri", "ücretsiz app store api aracı",
  "yüksek çözünürlüklü uygulama simgesi indirme", "app store rakip araştırması",
  "yerelleştirilmiş app store verileri", "ülkeye göre app store arama", "ücretsiz aso araştırma aracı"
]
tags: [
  "App Store Meta Verileri", "App Lookup", "iTunes Search API",
  "Uygulama Simgesi İndirme", "Uygulama Ekran Görüntüleri", "ASO Araştırması"
]
sidebar:
  exclude: true
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Saniyeler İçinde App Store Verisi Alın

**Kısaca:** [AppLookup.pro](https://applookup.pro), herhangi bir iOS, iPadOS, macOS veya tvOS uygulamasının herkese açık verilerini çeken ücretsiz bir araçtır. Başlık, açıklama, sürüm yenilikleri, sürüm, fiyat, derecelendirmeler, uygulama simgesi, ekran görüntüleri, desteklenen cihazlar ve ham iTunes API yanıtını alırsınız. Her alanın tek dokunuşla kopyalama düğmesi vardır. Siteyi açın, bir App Store bağlantısı yapıştırın veya uygulama adını yazın, verilere ulaşırsınız.

Şunlar için kullanın:

- **ASO araştırması.** En iyi uygulamaların başlıklarını, alt başlıklarını, açıklamalarını ve anahtar kelimelerini nasıl yazdığını görün.
- **Rakip takibi.** Pazarlar arasında sürüm güncellemelerini, derecelendirmeleri ve fiyatları kontrol edin.
- **Materyal indirme.** Resmi uygulama simgesini ve tam boyutlu ekran görüntülerini tek bir ZIP içinde kaydedin.
- **Yerelleştirme kontrolleri.** Açıklama, sürüm yenilikleri ve ekran görüntülerini 40'tan fazla App Store ülkesinde karşılaştırın.
- **API testi.** Ham iTunes Search API JSON yanıtını doğrudan kodunuza veya Postman'e kopyalayın.

## AppLookup.pro Nedir?

[AppLookup.pro](https://applookup.pro), ücretsiz, tarayıcı tabanlı bir App Store arama aracıdır. Tamamen cihazınızda çalışır. Her sonuç doğrudan Apple'ın resmi [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) sayfasından gelir. Scraping yok. Kayıt yok. İzleme yok.

### Ne Elde Edersiniz

- **Uygulama adı veya App Store URL'si ile arama.** Yazdıkça otomatik tamamlama canlı sonuçlar gösterir.
- **40'tan fazla ülke mağazası.** ABD, Birleşik Krallık, Japonya, Almanya, Fransa, Brezilya ve daha fazlası arasında geçiş yapın.
- **Tam meta veri.** Başlık, alt başlık, geliştirici, bundle ID, sürüm, fiyat, dosya boyutu, derecelendirmeler, yayın tarihi, içerik derecelendirmesi, diller ve desteklenen cihazlar.
- **Yüksek çözünürlüklü materyaller.** iPhone, iPad, macOS ve Apple TV için uygulama simgeleri ve ekran görüntüleri.
- **Toplu ZIP indirme.** Her simgeyi veya her ekran görüntüsünü tek bir arşivde alın.
- **Ham iTunes API JSON'u.** Apple'dan gelen tam yanıt, kopyalamaya hazır.
- **Her alanda kopyalama düğmeleri.** Tek dokunuşla değer panoya gider.

## AppLookup.pro Adım Adım Nasıl Kullanılır

### Adım 1. Uygulama Adını Girin veya App Store URL'sini Yapıştırın

[applookup.pro](https://applookup.pro) sayfasını açın ve uygulama adını yazmaya başlayın. Otomatik tamamlama, yazdıkça canlı App Store sonuçlarını gösterir.

`https://apps.apple.com/us/app/instagram/id389801252` gibi doğrudan bir App Store bağlantısı veya sadece uygulama ID'sini de yapıştırabilirsiniz. Araç ID'yi sizin için çıkarır. Google yönlendirme URL'lerini de işler.

![AppLookup.pro'ya uygulama adı veya App Store URL'si girin](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Adım 2. Uygulama Bilgilerini Alın ve Simgeyi İndirin

**Lookup** düğmesine tıklayın veya Enter tuşuna basın. Araç resmi iTunes Search API'yi çağırır ve bir saniyeden kısa sürede uygulama simgesini, geliştirici adını, derecelendirmeyi, sürümü ve fiyatı gösterir.

**App Icon** bölümüne kaydırın. Apple'ın döndürdüğü her simge boyutu bir kart olarak görünür. Her kartta:

- **Direct Link.** Tam boyutlu görüntüyü yeni sekmede açar.
- **Download.** Dosyayı bilgisayarınıza kaydeder.

Her simge boyutunu tek bir arşivde almak için **Download All Icons (ZIP)** kullanın. Ekran görüntüleri için de aynısı geçerlidir: her platform bölümünün kendi **Download All (ZIP)** düğmesi vardır.

![AppLookup.pro'dan uygulama simgelerini ve ekran görüntülerini indirin](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Adım 3. Uygulama Ayrıntılarını Okuyun ve İstediğiniz Alanı Kopyalayın

**App Details** bölümüne kaydırın. Bundle ID, sürüm, fiyat, dosya boyutu, minimum işletim sistemi, yayın tarihi, son güncelleme tarihi, içerik derecelendirmesi, türler, tür ID'leri, diller, satıcı, sanatçı ID'si ve track ID'sini göreceksiniz.

Herhangi bir karttaki **Copy** düğmesine dokunun. Değer panonuza gider ve düğme yeşil bir 'Copied' işareti gösterir.

Aynısı **Description**, **What's New** ve **Supported Devices** için de geçerlidir. Bu bölümler kaydırılabilir, böylece yerinizi kaybetmeden tam metni okuyabilirsiniz ve Copy düğmesi tüm alanı panonuza koyar.

![Tam App Store ayrıntılarını görüntüleyin ve istediğiniz alanı tek dokunuşla kopyalayın](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Adım 4. Ham App Store API Yanıtını Görüntüleyin

Apple'ın döndürdüğü tam JSON gerekiyor mu? **Raw API Response** bölümüne kaydırın. Tam iTunes Search API yükü, üstte **Copy** düğmesi olan kaydırılabilir bir görüntüleyicide gösterilir. Tek dokunuşla tüm JSON nesnesi kopyalanır.

**iTunes Lookup URL** hemen üstte gösterilir. Aynı isteği tekrarlamak için Postman'e, curl'e veya tarayıcınıza yapıştırın.

![Ham iTunes Search API JSON yanıtını görüntüleyin ve kopyalayın](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Adım 5. Yerelleştirilmiş Sürümü Görmek İçin Ülkeyi Değiştirin

App Store meta verileri ülkeye göre değişir. Aynı uygulama genellikle her pazarda farklı başlık, alt başlık, açıklama, ekran görüntüsü ve fiyata sahiptir.

Üstteki açılır menüden bir ülke seçin. Giriş kutusundaki URL otomatik olarak güncellenir. Uygulamayı o pazarda yeniden almak için tekrar **Lookup** tıklayın.

Bu, bir rakibin uygulamasını Japonya, Almanya, Brezilya veya 40'tan fazla desteklenen ülkenin herhangi birinde nasıl sunduğunu kontrol etmenin en hızlı yoludur.

![Yerelleştirilmiş App Store meta verilerini görmek için ülke mağazalarını değiştirin](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Adım 6. Yerelleştirilmiş Meta Verileri Kopyalayın

Ülke sonucu yüklendiğinde, her alan aynı şekilde çalışır. Yerelleştirilmiş metni yakalamak için açıklama, sürüm yenilikleri, uygulama adı, geliştirici, bundle ID veya herhangi bir ayrıntı kartında **Copy** düğmesine dokunun.

Bu, yan yana karşılaştırma elektronik tabloları oluşturmayı veya yerelleştirilmiş metni çeviri incelemesine aktarmayı kolaylaştırır.

![Yerelleştirilmiş App Store açıklamasını ve meta verilerini tek dokunuşla kopyalayın](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## AppLookup.pro'yu Kimler Kullanır

- **Bağımsız geliştiriciler** lansman öncesi ASO araştırması yapanlar.
- **ASO ve pazarlama ekipleri** rakip güncellemelerini ve fiyatlandırmayı takip edenler.
- **Tasarımcılar** basın kitleri ve vaka çalışmaları için resmi yüksek çözünürlüklü uygulama simgesini ve ekran görüntülerini alanlar.
- **Yerelleştirme ekipleri** hangi pazarların kapsandığını ve varsayılan İngilizce metnin nerede hala gönderildiğini denetleyenler.
- **Backend ve QA mühendisleri** scraper yazmadan iTunes Search API entegrasyonlarını test edenler.
- **Yazarlar ve blog yazarları** bir gönderi için resmi uygulama simgesine ve birkaç ekran görüntüsüne ihtiyaç duyanlar.

## Gizlilik ve Sorumluluk Reddi

AppLookup.pro tarayıcınızda çalışır. Giriş yok. İzleme yok. Aradığınız uygulamaların sunucu tarafında kaydı yok. İstekler doğrudan tarayıcınızdan Apple'ın [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) sayfasına gider.

Bu araç **yalnızca eğitim ve araştırma amaçlıdır**. Tüm veriler Apple'ın resmi genel API'sinden alınır ve Apple Inc. ile listelenen uygulama yayıncılarının mülkü olarak kalır. Aracın kullanımı [Apple Media Services Şartlar ve Koşullarına](https://www.apple.com/legal/internet-services/terms/site.html) tabidir. Lütfen Apple'ın hız sınırlarına saygı gösterin ve telif hakkıyla korunan materyalleri yeniden dağıtmayın.

## Şimdi Deneyin

App Store verilerini incelemek için API anahtarına, geliştirici hesabına veya ücretli plana ihtiyacınız yok. [applookup.pro](https://applookup.pro) sayfasını açın, herhangi bir App Store URL'sini yapıştırın ve saniyeler içinde meta verilere, simgelere ve ham JSON'a sahip olacaksınız.

## Açık Kaynak

AppLookup.pro açık kaynaktır. Hata raporları, ülke eklemeleri ve pull request'ler memnuniyetle karşılanır.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="GitHub'da AppLookup.pro" icon="github" tag="açık kaynak" >}}
{{< /cards >}}

---

## Sıkça Sorulan Sorular

{{% details title="AppLookup.pro gerçekten ücretsiz mi?" closed="true" %}}
Evet. AppLookup.pro yüzde 100 ücretsiz ve açık kaynaktır. Tarayıcınızda çalışır. Kayıt yoktur, ücretli katman yoktur ve Apple'ın kendi iTunes Search API sınırlarının ötesinde kullanım sınırı yoktur.
{{% /details %}}

{{% details title="Veriler nereden geliyor?" closed="true" %}}
Her sonuç, Apple'ın resmi [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) sayfasından gerçek zamanlı olarak alınır. Araç App Store sayfalarını scrape etmez ve yanıtları herhangi bir sunucuda önbelleğe almaz.
{{% /details %}}

{{% details title="Uygulama simgesini yüksek çözünürlükte indirebilir miyim?" closed="true" %}}
Evet. **App Icon** bölümü, Apple'ın döndürdüğü her simge URL'sini gösterir. Her kartta bir Direct Link ve bir Download düğmesi vardır ve bir Download All Icons ZIP düğmesi onları tek bir arşivde paketler.
{{% /details %}}

{{% details title="Tüm App Store ekran görüntülerini bir kerede indirebilir miyim?" closed="true" %}}
Evet. Her ekran görüntüsü bölümünde (iPhone, iPad, macOS ve Apple TV) her ekran görüntüsünü tam çözünürlükte paketleyen bir **Download All (ZIP)** düğmesi vardır.
{{% /details %}}

{{% details title="Bir uygulamanın başka bir ülkede nasıl göründüğünü nasıl görürüm?" closed="true" %}}
Sayfanın üstündeki açılır menüden bir ülke seçin. 40'tan fazla mağaza desteklenmektedir. Tekrar **Lookup** tıklayın ve araç o ülke için uygulamayı yeniden alır, yerelleştirilmiş başlığı, açıklamayı, ekran görüntülerini, sürüm yeniliklerini ve fiyatı gösterir.
{{% /details %}}

{{% details title="Bundle ID veya yayın tarihi gibi tek alanları kopyalayabilir miyim?" closed="true" %}}
Evet. Sonuçtaki her metin alanının kendi Copy düğmesi vardır: uygulama adı, geliştirici, açıklama, sürüm yenilikleri, bundle ID, sürüm, fiyat, dosya boyutu, minimum işletim sistemi, yayın tarihi, içerik derecelendirmesi, diller, desteklenen cihazlar ve ham JSON.
{{% /details %}}

{{% details title="AppLookup.pro herhangi bir iOS uygulaması için çalışır mı?" closed="true" %}}
En az bir App Store ülkesinde herkese açık olarak listelenen ve iTunes Search API tarafından döndürülen herhangi bir uygulama için çalışır. Listelenmemiş, kaldırılmış veya kurumsal olarak dağıtılan uygulamalar görünmez.
{{% /details %}}

{{% details title="macOS ve Apple TV uygulamalarını destekliyor mu?" closed="true" %}}
Evet. Uygulamanın iTunes Search API yanıtında macOS veya Apple TV ekran görüntüleri varsa, AppLookup.pro bunları kendi kaydırılabilir panelinde indirme düğmeleriyle gösterir.
{{% /details %}}

{{% details title="Ham JSON'u kendi kodumda kullanabilir miyim?" closed="true" %}}
Evet. Raw API Response bölümü, Apple'ın döndürdüğü tam JSON'u gösterir. Postman'e, bir birim testine veya bir backend pipeline'a kopyalayın. Lütfen Apple'ın API şartlarına ve makul hız sınırlarına saygı gösterin.
{{% /details %}}

{{% details title="App Store URL'lerini araca yapıştırmak güvenli mi?" closed="true" %}}
Evet. URL tarayıcınızda ayrıştırılır. Tek giden ağ çağrısı Apple'ın iTunes Search API'sine yapılan aramadır.
{{% /details %}}

{{% details title="AppLookup.pro ile AppKeywords.pro arasındaki fark nedir?" closed="true" %}}
[AppLookup.pro](https://applookup.pro), yayınlanmış herhangi bir uygulamanın App Store meta verilerini okumak içindir: rakip araştırması, materyal indirme, yerelleştirme kontrolleri. [AppKeywords.pro](https://appkeywords.pro), kendi uygulamanız için App Store meta verilerini yazmak içindir: Fastlane desteğiyle başlık, alt başlık ve anahtar kelime optimizasyonu. İki araç birlikte iyi çalışır.
{{% /details %}}
