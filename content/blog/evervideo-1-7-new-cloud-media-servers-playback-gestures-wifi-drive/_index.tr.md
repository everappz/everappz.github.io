---
title: "Evervideo 1.7: Yeni Plex, Jellyfin, Bulut Akışı, Oynatma Hareketleri"
date: 2026-05-18
description: "Evervideo 1.7, 10'dan fazla yeni bağlantı ekler — Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS — ayrıca yeni oynatma hareketleri (atlamak için çift dokunma, 2x hız için dokun ve tut), toplu yüklemeli yenilenmiş bir Wi-Fi Drive ve iPhone, iPad ve Mac için Liquid Glass UI güncellemeleri."
keywords: ["Evervideo 1.7", "Evervideo güncellemesi", "HD video oynatıcı iPhone", "Plex video oynatıcı iOS", "Jellyfin iPhone video", "Emby video oynatıcı iOS", "Subsonic video iOS", "Navidrome video iOS", "Internxt video akışı", "Proton Drive video oynatıcı", "QNAP video oynatıcı iPhone", "Nextcloud video oynatıcı iOS", "Amazon S3 video akışı", "SFTP video oynatıcı iPhone", "FTP video oynatıcı iOS", "NFS video akışı iPhone", "NAS'tan video akışı iPhone", "MKV oynatıcı iPhone", "video oynatıcı hareketleri iOS", "video atlamak için çift dokunma", "Wi-Fi Drive video aktarımı iPhone", "Liquid Glass tasarımı", "bulut video oynatıcı iOS 2026", "buluttan film akışı iPhone"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Oynatma Hareketleri", "Liquid Glass", "Yenilikler"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Özet:** [Evervideo 1.7](/products/evervideo), iPhone, iPad ve Mac HD video oynatıcısı için büyük bir güncellemedir. Bu sürüm 10'dan fazla yeni bulut, NAS ve medya sunucusu bağlantısı ekler — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3** ile en popüler medya sunucuları **Plex**, **Subsonic**, **Navidrome**, **Jellyfin** ve **Emby** ve üç ağ protokolü: **FTP**, **SFTP** ve **NFS**. Yeni **oynatma hareketleri**, ileri veya geri atlamak için çift dokunmanıza, 2x hızda çalıştırmak için dokunup tutmanıza ve kontrolleri açıp kapatmak için tek dokunmanıza olanak tanır — tüm bunlar tam ekrandan ayrılmadan. Wi-Fi Drive, seçim modu ve daha akıllı bir yükleme kuyruğuyla yenilenmiş bir arayüze sahip olur. Uygulamanın tamamı Apple'ın yeni **Liquid Glass** tasarımı için ayarlanmıştır.

---

## Herkese merhaba!

Büyük bir Evervideo güncellemesi burada. Bu, gönderdiğimiz en büyük sürümlerden biridir: **10'dan fazla yeni bulut, sunucu ve ağ bağlantısı**, tam ekranda daha hızlı kontrol için yepyeni **oynatma hareketleri**, yenilenmiş bir **Wi-Fi Drive** deneyimi ve iPhone, iPad ve Mac genelinde **Liquid Glass** için ayarlanmış bir UI.

[Evervideo 1.7'yi App Store'dan indirin](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) veya mevcut sürümünüzden güncelleyin. Mac kullanıcıları [masaüstü sürümünü buradan](https://apps.apple.com/app/evervideo/id6743504109) alabilirler.

## 10'dan Fazla Yeni Bulut, NAS ve Medya Sunucusu Bağlantısı

Evervideo 1.7, «video kitaplığınız» olarak kabul edilenleri genişletir. Filmleriniz, dizileriniz veya kayıtlarınız güvendiğiniz bir bulutta, evdeki bir NAS'ta veya kendi barındırdığınız bir medya sunucusunda yaşıyorsa, Evervideo artık doğrudan oradan akış yapabilir — indirme yok, dönüştürme yok, yeniden kodlama yok.

### Gizlilik Odaklı Bulut Depolama: Internxt ve Proton Drive

Uçtan uca şifrelemeyi ve sıfır bilgi depolamayı önemsiyorsanız, en saygın gizlilik öncelikli bulutlardan ikisi artık Evervideo'da yerel olarak desteklenmektedir:

- **Internxt** — açık kaynaklı, kuantum sonrası şifrelenmiş, GDPR uyumlu İspanyol bulutu. Ücretsiz katman mevcut.
- **Proton Drive** — Proton Mail ve Proton VPN'in yaratıcılarından İsviçre merkezli uçtan uca şifrelenmiş depolama. Daha büyük kitaplıklar için ücretli planlarla birlikte ücretsiz katman mevcut.

Bir kez bağlanın ve videolarınız şifreli tünel üzerinden akar — Evervideo verilerinizi asla açık olarak görmez, sağlayıcının sunucusu da görmez.

### Kendi Barındırdığınız Depolama: QNAP, Nextcloud, Amazon S3

Kendi altyapısını çalıştıran kullanıcılar için:

- **QNAP** — QNAP NAS cihazlarına yerel Wi-Fi veya uzaktan erişim üzerinden hızlı ve güvenilir video oynatma için yerel API bağlantısı. 4K MKV dosyalarını yeniden kodlama olmadan doğrudan akıtın.
- **Nextcloud** — kendi barındırılan veya yönetilen herhangi bir Nextcloud örneğine bağlanın. Gizlilik nedeniyle Google Drive veya Dropbox'tan zaten geçtiyseniz harika.
- **Amazon S3** — Evervideo'yu herhangi bir S3 paketine (veya Backblaze B2, Wasabi, MinIO, Cloudflare R2 gibi S3 uyumlu depolamaya) yönlendirin ve koleksiyonunuzu doğrudan akıtın.

### <a id="media-servers"></a>Medya Sunucuları: Plex, Subsonic, Navidrome, Jellyfin, Emby

Bu, kendi barındıran video severler için büyük olay. Evervideo 1.7, iPhone, iPad veya Mac'inizi en popüler açık kaynak ve freemium medya sunucuları için birinci sınıf bir istemciye dönüştürür:

- **Plex** — Plex Media Server indirmek ve çalıştırmak için **ücretsizdir**, mobil senkronizasyon, donanım transkodlama ve canlı TV gibi özellikler için isteğe bağlı **Plex Pass** aboneliği vardır. Evervideo hem ücretsiz hem de Plex Pass kitaplıklarıyla çalışır — tam film ve TV koleksiyonunuzu akıtın.
- **Subsonic** — orijinal kendi barındıran akış sunucusu. Resmi Subsonic sunucusu **ücretlidir** (30 günlük denemeden sonra aylık 1 $) ve Evervideo ayrıca uyumlu video sunucularına Subsonic API'sini konuşur.
- **Navidrome** — modern, hafif, **tamamen ücretsiz ve açık kaynaklı** sunucu. Subsonic API'sini uygular. Raspberry Pi, NAS veya herhangi bir Linux kutusunda çalışır.
- **Jellyfin** — **tamamen ücretsiz ve açık kaynaklı** medya sunucusu (Emby'nin topluluk çatalı). Filmleri, TV'yi, müziği, kitapları ve ev videolarını işler. Hesap yok, telemetri yok, abonelik yok. Ticari koşullar olmadan kendi barındırma akışı isteyen kullanıcılar için tercih edilen seçenek.
- **Emby** — **freemium** medya sunucusu. Çekirdek sunucu ücretsizdir; **Emby Premiere**, mobil uygulamaları, çevrimdışı senkronizasyonu, Sinema Modu ve daha fazlasını açan tek seferlik veya yıllık bir satın alımdır. Evervideo hem ücretsiz hem de Premiere kitaplıklarına bağlanır.

Hangi sunucuyu çalıştırırsanız çalıştırın, Evervideo tüm kitaplığınızı — filmler, diziler, ev videoları ve gömülü altyazı parçaları — video ekolayzeri, 360° desteği, Resim İçinde Resim, AirPlay ve Chromecast ile akıtır.

### Yeni Ağ Protokolleri: FTP, SFTP, NFS

Özel sunucuları, ev laboratuvarları veya cilalı bir mobil uygulamayla gelmeyen genel NAS kutuları olan kullanıcılar için Evervideo 1.7 üç klasik protokol ekler:

- **SFTP (SSH Dosya Aktarım Protokolü)** — **kendi sunucunuzdan güvenli uzaktan video akışı** için doğru cevap. SFTP, SSH üzerinde çalışır, böylece tüm aktarım (kimlik doğrulama ve video verileri) şifrelenir. SSH erişimi olan bir VPS, özel sunucu veya evde bir Linux kutunuz varsa, üzerine bir video klasörü bırakabilir ve başka hiçbir şeyi ifşa etmeden açık internet üzerinden akış yapabilirsiniz. Parola ve anahtar tabanlı kimlik doğrulamayı destekler.
- **FTP** — dosya aktarımı için uzun süredir devam eden standart. **Ev NAS'ınız** (daha eski Synology, ASUS, D-Link, TerraMaster veya genel kutular) bir FTP sunucusunu açığa çıkarıyor ancak yerel bir API entegrasyonu yoksa kullanışlıdır. En iyi yerel ağınızın içinde kullanılır.
- **NFS (Ağ Dosya Sistemi)** — Linux ve çoğu NAS cihazında fiili paylaşım protokolü. NFS paylaşımları ev laboratuvarlarında ve küçük işletme ağlarında yaygındır; Evervideo artık bunları bağlar ve düşük yükle 4K ve HD video akıtır.

> **İpucu:** SFTP, açık internet üzerinden akış yapmak için istediğiniz protokoldür. FTP ve NFS en iyi yerel ağınızın içinde kullanılır — bir VPN'e sarmadıkça herkese açık internete açmayın.

## Yeni Oynatma Hareketleri

Tam ekranda video izlemek zahmetsiz hissettirmelidir. Evervideo 1.7, ekran üzerindeki kontrolleri ortaya çıkarmadan oynatmayı kontrol etmenizi sağlayan temiz bir dokunma hareketleri seti sunar — filmler, dersler veya kesintisiz izlemek istediğiniz her şey için mükemmel.

### Çift Dokunma — İleri veya Geri Atla

Yapılandırılabilir saniye sayısı kadar **ileri atlamak** için ekranın **sağ tarafına** çift dokunun. **Geri atlamak** için **sol tarafa** çift dokunun. Aralığı **Ayarlar → Oynatma → Hareket Atlama Aralığı** bölümünde değiştirebilirsiniz (varsayılan: 10 saniye) — 5 saniyeden (ince arama için) 60 saniyeye (intro atlamak için) kadar herhangi bir değer seçin.

Bu, YouTube ve Netflix kullanıcılarının anında tanıyacağı harekettir ve artık herhangi bir kaynaktan herhangi bir video için Evervideo'da yerel olarak desteklenmektedir.

### Dokun ve Tut — Geçici 2x Hız

**Oynatma hızını geçici olarak 2x'e yükseltmek** için ekranın herhangi bir yerine basılı tutun. Normal hıza dönmek için bırakın. Şunlar için mükemmel:

- Kalıcı bir hız değişikliğine bağlanmadan yavaş sahneleri atlamak.
- İlgili bölümü bulmak için derslerden, eğitimlerden veya podcast'lerden hızlıca geçmek.
- Tam sürümü izlemeye karar vermeden önce filmleri örneklemek.

Tutma hareketi kayıtlı oynatma hızınızı değiştirmez — bırakın ve başladığınız yere geri dönün.

### Tek Dokunma — Kontrolleri Göster/Gizle

Ekran üzerine tek bir dokunma, oynatma kontrollerini (oynat, duraklat, arama çubuğu, altyazılar, ekolayzer) açar veya kapatır. Onları getirmek için bir kez dokunun, gizlemek için tekrar dokunun. Çift dokunma ve tutmayla birleştirildiğinde, bu, neredeyse tüm bir filmi temiz tam ekran modunda geçirebileceğiniz ve yine de ne zaman ihtiyaç duyarsanız atlayabileceğiniz, duraklatabileceğiniz ve hızlı tarama yapabileceğiniz anlamına gelir.

## Wi-Fi Drive: Yeni UI ve Daha Hızlı Yüklemeler

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/), Evervideo'nun **bilgisayarınızdan iPhone'unuza veya iPad'inize kablosuz olarak video aktarmak için yerleşik özelliğidir — iTunes yok, kablo yok, bulut hesabı gerekmez**. Her iki cihazın da aynı Wi-Fi ağında olması gerekir. iOS uygulamasında sunucuyu başlatırsınız ve şunlardan birini yaparsınız:

- URL'yi herhangi bir masaüstü tarayıcıda (Safari, Chrome, Firefox, Edge) açın, video dosyalarınızı sayfaya sürükleyin ve doğrudan cihaza yüklensin, veya
- WebDAV kullanarak cihazı **Mac Finder** («Sunucuya Bağlan…») veya **Windows Dosya Gezgini** (Ağ Sürücüsünü Eşle) ile bir ağ paylaşımı olarak bağlayın.

Büyük yerel bir video koleksiyonunu herhangi bir üçüncü taraf hizmeti olmadan telefonunuza veya tabletinize taşımanın en hızlı yoludur. [Adım adım kılavuzu burada görün](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).

Evervideo 1.7'de Wi-Fi Drive şunları kazanır:

- **Yeniden tasarlanmış kullanıcı arayüzü** — daha temiz, bir bakışta daha okunabilir ve Liquid Glass için güncellenmiş.
- **Toplu eylemler için yeni seçim modu** — birden fazla dosya veya klasör seçin ve toplu olarak işlem yapın (sil, taşı, kopyala).
- **Geliştirilmiş dosya yükleme kuyruğu** — daha iyi ilerleme geri bildirimi ve ağ hıçkırıklarına karşı dayanıklılık, böylece dengesiz bir Wi-Fi bağlantısı artık 30 GB'lık bir aktarımı bozmaz.
- **Daha iyi genel aktarım performansı** — büyük kitaplıklar için ölçülebilir şekilde daha hızlı yüklemeler, özellikle 4K MKV dosyaları ve film koleksiyonları için.

## Diğer İyileştirmeler

### Liquid Glass Tasarım Güncellemeleri

Evervideo 1.7'nin arayüzü, uygulamanın tamamında Apple'ın yeni **Liquid Glass** malzemesi için güncellenmiştir — yarı saydam yüzeyler, daha akıcı animasyonlar ve iOS 26, iPadOS 26 ve macOS 26'ya doğal olarak uyan iyileştirilmiş kontroller. Şimdi Oynatılıyor, dosya tarayıcısı ve ayarlar ekranları yeni sistem estetiğine uyacak şekilde yeniden ayarlanmıştır.

### Güncellenmiş Bağlantı Kütüphaneleri

Evervideo'nun **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, **iCloud Drive**, **MEGA** ve diğer hizmetlerle iletişim kurmak için kullandığı temel kütüphaneleri yeniledik. Sonuç: daha az köşe durumu bağlantı arızası, yeni sunucu sürümleri için daha iyi destek ve daha yavaş veya coğrafi olarak uzak bağlantılarda video akışında daha iyi güvenilirlik.

### Oynatma Hata Düzeltmeleri

- Büyük MKV dosyalarında aramadan sonra akışların donduğu belirli kendi barındırılan sunucularda oynatma sorunları düzeltildi.
- Ağ oynatma sırasında kısa süreliğine düştüğünde daha iyi devam ettirme davranışı.
- Uzun formattaki içerikte daha düzgün altyazı senkronizasyonu.

### Yerelleştirme Düzeltmeleri

Doğrudan kullanıcı geri bildirimine dayalı olarak birden fazla dilde çeviri düzeltmeleri. Daha küçük düğmelerde ve daha uzun Avrupa dillerinde (Almanca, Felemenkçe, Fransızca) daha iyi metin yerleşimi.

### Geri Bildiriminizden İlham Alan Küçük İyileştirmeler

App Store yorumlarına ve support@everappz.com adresine gönderilen e-postalara dayalı pek çok küçük iyileştirme. Her mesajı okuyoruz.

## Bu Güncelleme Neden Önemli

Evervideo 1.7, üç fikir etrafında inşa edilmiştir:

1. **Videolarınız, onları nerede saklarsanız saklayın.** Kitaplığınız ister iCloud Drive'da, ister Proton Drive veya Internxt gibi gizlilik öncelikli bir bulutta, ister Plex veya Jellyfin gibi bir medya sunucusunda, ister evdeki bir NAS'ta, ister Navidrome çalıştıran bir Raspberry Pi'da yaşasın — Evervideo artık ona yerel olarak bağlanır ve her yerde aynı oynatma deneyimini sunar.
2. **Zahmetsiz hissettiren tam ekran video.** Yeni dokunma hareketleri (çift dokunma, dokun ve tut, tek dokunma), YouTube ve Netflix gibi akış uygulamalarının kullanıcıları beklemeye eğittiği akıcı kontrol türünü *sizin* video koleksiyonunuza uygular.
3. **Bilgisayarınızdan daha hızlı aktarımlar.** Toplu seçim ve daha akıllı bir yükleme kuyruğu olan yenilenmiş bir Wi-Fi Drive, büyük 4K film koleksiyonlarını iPhone veya iPad'inize taşımayı gerçekten hızlı hale getirir — kablo yok, iTunes yok, sıkıştırma yok.

## Evervideo 1.7'yi Edinin

[**Evervideo'yu App Store'dan indirin**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) veya App Store içinden güncelleyin. [Mac sürümü](https://apps.apple.com/app/evervideo/id6743504109), evrensel bir Mac uygulaması olarak ayrı olarak mevcuttur. Evervideo, gelişmiş özellikler için isteğe bağlı uygulama içi yükseltmelerle ücretsiz bir indirmedir. Yeni bulut bağlantıları, medya sunucusu desteği, oynatma hareketleri, Wi-Fi Drive iyileştirmeleri ve Liquid Glass UI temel güncellemenin bir parçasıdır.

Uygulamayı beğeniyorsanız, lütfen App Store'a bir değerlendirme bırakın — gerçekten yardımcı olur. Geri bildiriminiz var mı veya bir sorunla mı karşılaştınız? **support@everappz.com** adresinden bize e-posta gönderin. Her mesajı okuyoruz.

## Sıkça Sorulan Sorular

{{% details title="Evervideo 1.7'de yenilikler nelerdir?" closed="true" %}}
Evervideo 1.7, 10'dan fazla yeni bağlantı (Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), yeni oynatma hareketleri (atlamak için çift dokunma, 2x hız için dokun ve tut, kontrolleri açıp kapatmak için tek dokunma), seçim modu ve daha akıllı yükleme kuyruğuyla yeniden tasarlanmış bir Wi-Fi Drive, Liquid Glass tasarım güncellemeleri, güncellenmiş bağlantı kütüphaneleri ve birçok hata düzeltmesi için destek sunar.
{{% /details %}}

{{% details title="Evervideo, Plex ile çalışır mı?" closed="true" %}}
Evet. Evervideo 1.7'den itibaren bir Plex Media Server'a bağlanabilir ve tam video kitaplığınızı — filmler, TV şovları ve ev videoları — akıtabilirsiniz. Plex Media Server çalıştırmak ücretsizdir; Plex Pass isteğe bağlıdır. Evervideo, MKV, MP4, AVI, MOV ve diğer formatların yeniden kodlamadan doğrudan oynatılması da dahil olmak üzere hem ücretsiz hem de Plex Pass kurulumlarını destekler.
{{% /details %}}

{{% details title="Evervideo'da Jellyfin veya Navidrome destekleniyor mu?" closed="true" %}}
Evet. Hem Jellyfin hem de Navidrome, Evervideo 1.7'de tam olarak desteklenir. Jellyfin, video ve sesi işleyen ücretsiz, açık kaynaklı bir medya sunucusudur. Navidrome, Subsonic API'sini uygulayan ücretsiz, açık kaynaklı bir sunucudur. Evervideo her ikisine de yerel olarak bağlanır.
{{% /details %}}

{{% details title="Plex, Jellyfin, Emby, Navidrome ve Subsonic ücretsiz mi?" closed="true" %}}
- **Plex** — sunucu ücretsizdir; Plex Pass isteğe bağlı ücretli bir yükseltmedir.
- **Jellyfin** — tamamen ücretsiz ve açık kaynaklı.
- **Emby** — sunucu ücretsizdir; Emby Premiere ücretlidir ve mobil senkronizasyon ile çevrimdışı modu açar.
- **Navidrome** — tamamen ücretsiz ve açık kaynaklı.
- **Subsonic** — resmi sunucu 30 günlük denemeden sonra aylık 1 $ tutar, ancak API'si açıktır ve birçok ücretsiz sunucu (Navidrome dahil) bunu uygular.
{{% /details %}}

{{% details title="Ev NAS'ımdan SFTP, FTP veya NFS üzerinden akış yapabilir miyim?" closed="true" %}}
Evet. Evervideo 1.7, SFTP, FTP ve NFS'yi yerel bağlantı türleri olarak ekler. SFTP, tüm trafik SSH üzerinden şifrelendiği için herkese açık internet üzerinden kendi sunucunuzdan akış yapmak için önerilen seçimdir. FTP ve NFS, en iyi yerel ağınızın içinde veya bir VPN'in arkasında kullanılır.
{{% /details %}}

{{% details title="Evervideo'yu SFTP kullanarak özel bir sunucuya nasıl bağlarım?" closed="true" %}}
Evervideo'yu açın, Bağlantılar sekmesine gidin, SFTP'yi seçin ve sunucunuzun ana bilgisayar adını veya IP'sini, bağlantı noktasını (genellikle 22), kullanıcı adını ve ya bir parolayı ya da bir SSH özel anahtarını girin. Evervideo, uzak klasörlerinize göz atacak ve video dosyalarını uçtan uca şifreleme ile doğrudan akıtacaktır.
{{% /details %}}

{{% details title="Evervideo, Internxt ve Proton Drive'ı destekliyor mu?" closed="true" %}}
Evet. Her iki gizlilik odaklı bulut da Evervideo 1.7 itibarıyla desteklenmektedir. Uygulamada zaten bulunan MEGA ve diğer gizlilik öncelikli hizmetlere katılırlar.
{{% /details %}}

{{% details title="Yeni oynatma hareketleri nasıl çalışır?" closed="true" %}}
Tam ekran video oynatmada, yapılandırılabilir bir aralıkta (varsayılan 10 saniye — Ayarlar'da değiştirebilirsiniz) ileri atlamak için **sağ tarafa çift dokunun** ve geri atlamak için **sol tarafa çift dokunun**. Geçici olarak 2x'e hızlandırmak için ekranın herhangi bir yerinde **dokunup tutun**; normale dönmek için bırakın. Oynatma kontrollerini açmak veya kapatmak için herhangi bir yere **tek dokunun** (göster veya gizle).
{{% /details %}}

{{% details title="Çift dokunma atlama aralığını değiştirebilir miyim?" closed="true" %}}
Evet. **Ayarlar → Oynatma → Hareket Atlama Aralığı** bölümüne gidin ve 5 ile 60 saniye arasında bir değer seçin. Çoğu kullanıcı bunu 10 veya 15 saniyede tutar.
{{% /details %}}

{{% details title="Evervideo'daki Wi-Fi Drive nedir?" closed="true" %}}
Wi-Fi Drive, Evervideo'nun yerleşik kablosuz dosya aktarım özelliğidir. Videoları yerel Wi-Fi ağınız üzerinden bilgisayarınızdan iPhone'unuza veya iPad'inize yüklemenize olanak tanır — iTunes yok, kablo yok, bulut hesabı yok. Herhangi bir masaüstü tarayıcıyı veya Mac Finder veya Windows Dosya Gezgini gibi bir WebDAV istemcisini kullanabilirsiniz. [Tam Wi-Fi Drive kılavuzuna](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) bakın.
{{% /details %}}

{{% details title="Evervideo, Plex veya Jellyfin'den MKV, AVI ve diğer formatları oynatır mı?" closed="true" %}}
Evet. Evervideo neredeyse her video formatını oynatır — MKV, AVI, MP4, MOV, FLV, WMV, WEBM, M4V, TS, 3GP — ve bunları çoğu codec için transkodlama gerektirmeden doğrudan Plex, Jellyfin, Emby ve diğer medya sunucularından akıtır. Bu, sunucunuzda daha düşük CPU yükü ve daha hızlı başlatma süreleri anlamına gelir.
{{% /details %}}

{{% details title="Evervideo 1.7'ye güncelleme ücretsiz mi?" closed="true" %}}
Evet. Evervideo, App Store'dan ücretsiz bir indirmedir ve 1.7, tüm mevcut kullanıcılar için ücretsiz bir güncellemedir. Yeni bulut entegrasyonları, medya sunucusu desteği, oynatma hareketleri, Wi-Fi Drive iyileştirmeleri ve Liquid Glass UI, temel güncellemenin bir parçasıdır.
{{% /details %}}

{{% details title="Evervideo 1.7 hangi cihazlarda mevcut?" closed="true" %}}
Evervideo 1.7, iPhone, iPad ve Mac'te çalışır. AirPlay ve Chromecast, oynatmayı daha büyük bir ekrana yayınlamanıza olanak tanır. iCloud Drive senkronizasyonu, kitaplığınızı ve ayarlarınızı cihazlar arasında tutarlı tutar.
{{% /details %}}
