---
title: "Evertag 4.2: Yeni bulut bağlantıları, etiket düzenleyici ayarları açıklandı"
date: 2026-05-09
description: "Evertag 4.2; Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP ve NFS bağlantıları ekler, Wi-Fi Drive'ı tazeler ve arayüzü Liquid Glass için günceller. Bu yazı ayrıca tüm etiket düzenleyici ayarlarını açıklar — ID3v2.4 ile ID3v2.3 karşılaştırması, albüm kapağı ölçeklendirme, etiket çoğaltma, bulut yükleme modları ve Spotify ile diğer akış servisleri için doğru seçenekler dahil."
keywords: ["Evertag 4.2", "Evertag güncellemesi", "ID3 etiket düzenleyici iPhone", "ID3v2.4 vs ID3v2.3", "FLAC etiket düzenleme iOS", "MP3 etiket düzenleme iPhone", "albüm kapağı düzenleme iOS", "Spotify için etiket düzenleyici", "Plex etiket düzenleyici", "Apple Music etiket düzenleyici", "Evertag bulut etiket düzenleyici", "Internxt etiket düzenleyici", "Proton Drive etiket düzenleyici", "QNAP etiket düzenleyici", "Nextcloud etiket düzenleyici", "Amazon S3 etiket düzenleyici", "SFTP etiket düzenleyici iPhone", "FTP ses etiket düzenleyici", "NFS etiket düzenleyici iPhone", "Wi-Fi Drive etiket düzenleyici", "ID3 etiket çoğaltma", "albüm kapağı ölçeklendirme", "Liquid Glass tasarım", "ses meta veri düzenleyici iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Etiket düzenleyici", "ID3", "ID3v2.4", "ID3v2.3", "FLAC etiketleri", "MP3 etiketleri", "Albüm kapağı", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Yenilikler"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Özet:** [Evertag 4.2](/products/evertag), iPhone, iPad ve Mac için ses etiket düzenleyicisinde büyük bir güncellemedir. Etiket düzenlemedeki temel hataları gidermek ve 6'dan fazla yeni bulut ve sunucu bağlantısı eklemek için çalıştık — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3** ile birlikte **FTP**, **SFTP** ve **NFS** protokolleri. Wi-Fi Drive yenilenmiş bir arayüz, çoklu seçim modu, daha akıllı yükleme kuyruğu ve daha hızlı aktarımlar kazandı. Tüm uygulama **Liquid Glass** tasarımı için ayarlandı. Bu yazı ayrıca Evertag'in etiket düzenleyici ayarlarına derinlemesine iniyor — **ID3v2.4 vs ID3v2.3**, **albüm kapağı ölçeklendirme**, **etiket çoğaltma**, **bulut yükleme modları**, **indirilen dosyayı silme** ve **Spotify**, **Apple Music**, **Plex**, **Jellyfin** veya başka bir akış hizmeti için ses hazırlıyorsanız tam olarak hangi seçenekleri seçeceğinizi açıklıyor.

---

## Herkese merhaba!

Evertag'de büyük bir güncelleme burada. Etiket düzenlemedeki kritik hataları gidererek **6'dan fazla yeni bulut ve sunucu bağlantısı** ekledik; ses meta verilerini yönetmeyi her zamankinden daha kolay hale getirmek için. Kütüphaneniz gizliliğe odaklı bir bulutta, ev NAS'ında ya da genel bir FTP/SFTP/NFS sunucusunda olabilir.

[Evertag 4.2'yi App Store'dan indirin](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) veya mevcut sürümünüzden güncelleyin.

## Genişletilmiş bulut ve sunucu desteği

Evertag artık daha geniş bir bulut ve kendi kendine barındırılan depolama seçeneğine yerel olarak bağlanır. Dosyalarınız nerede olursa olsun ID3, MP4, FLAC, OGG ve APE etiketlerini düzenleyebilirsiniz.

### Gizliliğe odaklı bulut depolama: Internxt ve Proton Drive

Uçtan uca şifreleme ve sıfır bilgi depolama sizin için önemliyse, gizlilik öncelikli bulutun en saygın iki ismi artık Evertag'de yerel olarak destekleniyor:

- **Internxt** — açık kaynak, kuantum sonrası şifrelemeli, GDPR uyumlu İspanyol bulutu. Ücretsiz katman mevcut.
- **Proton Drive** — Proton Mail ve Proton VPN'in arkasındaki ekipten, İsviçre merkezli, uçtan uca şifrelenmiş depolama. Ücretsiz katman mevcut, daha büyük kütüphaneler için ücretli planlar.

Artık her iki hizmette saklanan ses dosyalarındaki meta verileri doğrudan düzenleyebilirsiniz — dosya iletim sırasında şifreli kalır ve yalnızca yeni etiketler geri yazılır.

### Kendi kendine barındırılan çözümler: QNAP, Nextcloud, Amazon S3

Kendi altyapısını işleten kullanıcılar için:

- **QNAP** — QNAP NAS aygıtlarına yerel API bağlantısı. Yerel Wi-Fi veya uzaktan erişim üzerinden QNAP'taki dosyalarınızda etiketleri düzenleyin.
- **Nextcloud** — kendi kendine barındırılan veya yönetilen herhangi bir Nextcloud örneğine bağlanın.
- **Amazon S3** — Evertag'i herhangi bir S3 kovasına (veya Backblaze B2, Wasabi, MinIO, Cloudflare R2 gibi S3 uyumlu depolamaya) yönlendirin ve meta verileri yerinde düzenleyin.

### Yeni ağ protokolleri: FTP, SFTP, NFS

Özel sunucuları, ev laboratuvarları veya cilalı bir mobil uygulaması olmayan jenerik NAS aygıtları olan kullanıcılar için Evertag 4.2 üç klasik protokolü ekledi:

- **SFTP (SSH Dosya Aktarım Protokolü)** — **kendi sunucunuzdan güvenli uzaktan etiket düzenleme** için doğru cevap. SFTP, SSH üzerinde çalışır; bu nedenle tüm aktarım (kimlik doğrulama ve ses verisi) şifrelenir. SSH erişimi olan bir VPS'iniz, özel bir sunucunuz veya evde bir Linux makineniz varsa uzaktaki dosyaların etiketlerini başka hiçbir şeyi açığa çıkarmadan düzenleyebilirsiniz. Şifre ve anahtar tabanlı kimlik doğrulamayı destekler.
- **FTP** — uzun süredir yerleşik dosya aktarım standardı. FTP'yi açan ancak yerel API entegrasyonu olmayan eski ev NAS aygıtları için yararlıdır.
- **NFS (Ağ Dosya Sistemi)** — Linux'ta ve çoğu NAS'ta fiili paylaşım protokolü. Aynı donanımda SMB'ye göre daha az ek yük.

> **İpucu:** Açık internet üzerinden uzaktan düzenleme için tercih edeceğiniz protokol SFTP'dir. FTP ve NFS yerel ağda kullanılması en iyi olanlardır — bir VPN ile sarmalamadığınız sürece bunları internete açık bırakmayın.

## Wi-Fi Drive yükseltmeleri

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/), Evertag'in **bilgisayarınızla iPhone veya iPad arasında ses dosyalarını kablosuz aktarmak — iTunes, kablo veya bulut hesabı olmadan** — için yerleşik özelliğidir. Her iki cihaz da aynı Wi-Fi ağında olmalıdır.

Evertag 4.2'de Wi-Fi Drive şunları kazanır:

- **Yenilenmiş, modern arayüz** — daha temiz, bir bakışta okunması kolay ve Liquid Glass için güncellendi.
- **Çoklu seçim modu** — birden çok dosya veya klasör seçin ve toplu işlem yapın.
- **Daha akıllı yükleme kuyruğu** — daha iyi ilerleme bilgisi ve ağ aksaklıklarına karşı dayanıklılık.
- **Hız ve genel güvenilirlik iyileştirildi** — büyük kütüphaneler için daha hızlı aktarımlar.

Üçüncü taraf hizmet kullanmadan bir grup ses dosyasını bilgisayardan telefona taşımanın, etiketlerini düzenlemenin ve geri göndermenin en hızlı yoludur.

## Etiket düzenleyici ayarları: derinlemesine inceleme

Çoğu kullanıcının asla okumadığı kısım — ve etiketlerinizin her yerde mi yoksa yalnızca bazı uygulamalarda mı çalışacağını belirleyen kısım. Evertag'i açın, sonra **ses etiketleri düzenleyici ayarları** bölümüne gidin. Her seçeneğin gerçekte ne yaptığı ve hedefinize göre hangi seçeneği seçeceğiniz aşağıda.

### Albüm kapağı ölçeklendirme

Albüm kapağını bir ses dosyasına kaydederken Evertag, gömme öncesinde görüntüyü küçültebilir. Mevcut seçenekler:

- **Küçük** — dosya boyutuna en küçük etki, görüntü kalitesi düşük.
- **Orta** — çoğu kullanıcı için dengeli seçim.
- **Büyük** — yüksek kalite, büyük ekranlı oynatıcılar ve CarPlay için uygun.
- **Çok büyük** — çok yüksek kalite, dosya boyutunda gözle görülür artış.
- **Orijinal (Devre dışı)** — kapağı orijinal çözünürlüğünde gömer. **Hiç ölçeklendirme yok.**

**Bu neden önemli:**

- **Daha yüksek kalite = daha büyük dosya.** 3.000 × 3.000 piksellik bir kapak her parçaya birkaç MB ekleyebilir. Bunu bir albüme yayın, disk alanı yükü hızla birikir.
- **Bazı oynatıcılar çok büyük gömülü görüntülerle iyi başa çıkmaz.** Daha eski cihazlar, bazı araç headunit'leri ve bazı eski masaüstü oynatıcılar ~1.500 px üzerindeki kapaklarda boğulabilir veya göstermeyi reddedebilir.
- **Çoğu bulut ve akış iş akışı için**, **Orta** veya **Büyük** uygundur. **Orijinal**'i yalnızca arşiv kalitesine ihtiyacınız olduğunda veya büyüklüğü kaldıracağına güvendiğiniz bir oynatıcı için dosya hazırlarken kullanın.

> **Orijinal** boyut seçeneği Evertag premium kişiselleştirme yükseltmesinin parçasıdır. Standart boyutlar (Küçük/Orta/Büyük/Çok büyük) ücretsizdir.

### Etiket kaydetme seçenekleri: ID3v2.4 vs ID3v2.3

Bu, uyumluluk için en önemli tek ayardır. ID3v2, MP3 dosyalarının içinde kullanılan meta veri biçimidir. Yaygın olarak kullanılan iki sürüm vardır ve ince ama önemli farklılıklara sahiptir.

#### ID3v2.4

- Daha yeni, **UTF-8 metin kodlaması**nı destekler — Latin olmayan yazıları (Çince, Rusça, Japonca, Arapça, İbranice vb.) doğru şekilde işler.
- Daha fazla çerçeve türü (göreceli ses seviyesi, ekolayzır ön ayarları vb.).
- Bunu destekleyen **modern oynatıcılar için önerilir**.

#### ID3v2.3

- Daha eski ama **en evrensel olarak desteklenen** ID3 sürümüdür.
- UTF-8'i doğrudan desteklemez (Unicode metin için UTF-16 kullanır).
- Eski oynatıcılar, araç stereoları ve bazı masaüstü uygulamalarıyla **maksimum uyumluluk gerektiğinde önerilir**.

#### Evertag'de ID3v2.4 ne zaman etkinleştirilmeli

- Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (mevcut sürümler) veya modern Android oynatıcılar gibi **modern ses oynatıcıları** kullanıyorsanız. ✅ **ID3v2.4'ü AÇIN.**
- Kütüphaneniz **Latin olmayan karakterler** (Çince, Korece, Japonca, Rusça, Arapça, Yunanca, İbranice) içeriyorsa. ✅ **ID3v2.4'ü AÇIN** — UTF-8 bunları çok daha temiz işler.

#### Evertag'de ID3v2.4 ne zaman devre dışı bırakılmalı (yerine ID3v2.3 kullanın)

- v2.4 etiketlerini okumayan **eski araç stereosu veya gösterge tablosu birimi** için dosyalar hazırlıyorsunuz.
- Düzenlemeden sonra bazı uygulamalarda **bozuk metin veya eksik etiketler** görüyorsunuz — bu, orada v2.4'ün desteklenmediğine dair güçlü bir işarettir. v2.3'e geri dönün.
- **Eski masaüstü oynatıcıları** veya daha eski taşınabilir oynatıcıları (erken iPod'lar, 2000-2010'lardan bazı MP3 oynatıcıları) hedefliyorsunuz.

> **Pratik kural:** Etiketleriniz v2.4 ile her yerde doğru görüntüleniyorsa açık bırakın. Önemli bir oynatıcı bile yanlış karakter, boş veya etiketleri okumada başarısız olursa v2.4'ü kapatıp yeniden kaydedin.

#### Etiket çoğaltma

**Etiket çoğaltma**'yı etkinleştirdiğinizde Evertag, ortak meta veri alanlarını (başlık, sanatçı, albüm vb.) dosyanın **hem ID3v1 hem de ID3v2 bölümlerine** yazar. Bu, yalnızca ID3v1'i okuyan çok eski oynatıcılarla (dosyanın sonundaki orijinal 128 baytlık etiket) uyumluluğu artırır.

- **Çoğu kullanıcının buna ihtiyacı yoktur.** Modern oynatıcılar önce ID3v2'yi okur.
- **Yalnızca** vintage donanım veya ID3v2'yi yok sayan belirli yazılımlarla uğraşıyorsanız etkinleştirin.

### Çevrimiçi dosyaları güncelle: Evertag bulut düzenlemelerini nasıl ele alır

Bağlı bir bulutta (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP vb.) saklanan bir dosyanın etiketlerini düzenlerken Evertag, değiştirilmiş dosyayı geri yüklemek zorundadır. Bunu nasıl olacağını siz kontrol edersiniz:

- **Onay mesajı göster** *(varsayılan, önerilir)* — Evertag yüklemeden önce sorar. Temkinli kullanıcılar ve paylaşılan kütüphaneler için en iyisi.
- **Dosya meta verilerini otomatik güncelle** — her düzenlemeden sonra sessizce yükler. Hızlı, güvenilir bağlantıları olan ve çok düzenleme yapan tek kullanıcılar için en iyisi.
- **Dosya meta verilerini güncelleme** — Evertag yalnızca yerel kopyayı düzenler. Buluta göndermeden önce değişiklikleri önizlemek için yararlı.

### Çevrimiçi dosyaları düzenle: yerel dosya temizliği

Uzak bir dosyayı düzenlemek için Evertag önce dosyayı cihazınıza indirir. Düzenlemeden sonra o yerel kopyayla ne olacağını siz seçersiniz:

- **İndirilen dosyayı her zaman sil** — Evertag, düzenleme sonrası geçici dosyayı kaldırır. Depolama sıkışıksa veya başkasının dosyalarında çalışıyorsanız **önerilir**.
- **İndirilen dosyayı silme** — düzenlenmiş dosyayı cihazınızda tutar. Hem çevrimdışı kopya hem de güncellenmiş bulut kopyası istediğinizde yararlıdır.

### Ana ekrandaki düğmeler

Evertag'in etiket düzenleyici ana ekranı, bireysel işlemlerin düğmelerini gösterebilir veya gizleyebilir. Arayüzü odaklı tutmak için yalnızca gerçekten kullandıklarınızı etkinleştirin:

- **Otomatik ses etiketi arama** — dosyanın ses parmak izine göre çevrimiçi eksik meta verileri bulur.
- **Manuel ses etiketi arama** — otomatik arama yetersiz kaldığında başlığa/sanatçıya göre arayın.
- **Albüm kapağı ara** — yüksek kaliteli kapakları bulup gömer.
- **Albüm kapağını kaydet** — gömülü kapağı fotoğraf kütüphanenize veya dosyalarınıza dışa aktarır.
- **Kodlamayı normalleştir** — eski kodlamaların neden olduğu Latin olmayan bozuk metni düzeltir (eski yazılımla rip edilmiş Kiril, Çince ve Japonca parçalar için çok yararlıdır).
- **Ses etiketlerini sil** — bir dosyadan tüm etiketleri çıkarır. Temiz yeni etiketleme öncesinde yararlıdır.

### Genişletilmiş etiketleri göster

Bunu temel başlık/sanatçı/albüm/yıl ötesindeki tam meta veri alan setini görüntülemek için açın — BPM, şef, orijinal sanatçı, ruh hali, telif hakkı, kodlayıcı, yorumlar, sözler ve daha fazlası dahil. Üst düzey kullanıcı özelliği; çoğu sıradan kullanıcının buna ihtiyacı yoktur.

### Dosyaları aynı anda düzenle

Etkinleştirildiğinde Evertag, **birden fazla seçili dosyada** aynı anda meta veri düzenlemenize olanak tanır — tek bir işlemde tüm albüm için aynı album artist, yıl veya türü ayarlayın. Büyük, düzensiz bir kütüphaneyi temizlemenin en hızlı yoludur.

## Spotify, Apple Music ve akış platformları için etiketleri düzenleme

Sık sorulan soru: «Evertag'de etiketlerimi düzenledim, dosyaları yükledim ve akış servisi yanlış meta veriler gösteriyor. Ne oluyor?»

Kısa cevap: **Akış servisleri yerel etiketlerinizi her zaman dikkate almaz.** Apple Music ve Spotify'ın kendi iç veritabanları vardır — bir parçayı tanıdıklarında, görüntülenen meta verileri kendi verileriyle üzerine yazarlar. Ancak **yüklenmiş dosyalar**, yerel dosyalarınız (Apple Music'in «Kütüphane» özelliği, Spotify Local Files) ve **dağıtımcı yüklemeleri akış platformlarına** için etiketleriniz kesinlikle önemlidir. Her senaryoda Evertag'i nasıl ayarlamanız gerektiği:

### Apple Music için dosya hazırlığı (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music UTF-8'i doğru şekilde işler.
- **Albüm kapağı: Büyük** — Apple uygulamaları büyük kapakları iyi gösterir; Orijinal abartılı.
- **Etiket çoğaltma: OFF** — gerekli değil.
- **Album Artist**'in doğru doldurulduğundan emin olun — Apple Music gruplama için kullanır.

### Spotify Local Files için dosya hazırlığı

Spotify Local Files yalnızca iyi etiketlenmiş dosyaları görüntüler. Spotify'ın okuduğu etiketler sınırlıdır.

- Çoğu durumda **ID3v2.4: ON**. Düzenlemeden sonra bir parça Spotify'da doğru görünmüyorsa **ID3v2.4: OFF ile kaydetmeyi deneyin** (yani ID3v2.3 olarak) — Spotify'ın ayrıştırıcısı tarihsel olarak v2.4 konusunda muhafazakar olmuştur.
- **Albüm kapağı: Orta veya Büyük** — Spotify zaten kapağı küçültür.
- En azından **Başlık**, **Sanatçı**, **Albüm** ve **Parça Numarası** doldurun.

### Dağıtımcı yüklemesi için dosya hazırlığı (DistroKid, TuneCore, CD Baby vb.)

Kendi eserlerini akış platformlarına yükleyen bir sanatçıysanız, dağıtımcınız genellikle etiketleri okur ancak meta verileri kendi UI'sinde de ister. Her halükarda:

- **ID3v2.3** çoğu zaman daha güvenli varsayılandır — birçok dağıtımcı boru hattı yıllar önce kurulmuştur ve eski formatı tercih eder.
- **Büyük** kapak gömün (çoğu dağıtımcı ≥ 1.400 × 1.400 px kapak ister — yönergelerini kontrol edin).
- Genişletilmiş etiketlere güvenmeyin — dağıtımcılar yalnızca temel alanları okur.

### Plex, Jellyfin, Navidrome, Subsonic, Emby için dosya hazırlığı

Bu kendi kendine barındırılan medya sunucuları çok hoşgörülüdür. Hem v2.3 hem de v2.4'ü temiz okurlar ve UTF-8'i iyi işlerler.

- **ID3v2.4: ON** uygundur.
- **Albüm kapağı: Büyük** veya **Çok büyük** — bu sunucular kapakları mobil istemcilere ve CarPlay ekranlarına sunar, kalite önemli.
- **Album Artist** kuvvetle önerilir — Plex/Jellyfin albümleri sanatçıya göre doğru gruplandırmak için bunu kullanır.

### Araç stereoları ve eski donanım için dosya hazırlığı

- **ID3v2.4: OFF** (ID3v2.3 kullanın) — eski headunit'ler genellikle v2.4'ü desteklemez.
- **Albüm kapağı: Orta** — birçok araç ekranı büyük gömülü sanatlarda boğulur.
- **Etiket çoğaltma: ON** — eski araç stereoları bazen yalnızca ID3v1 yedeğini okur.

## Diğer iyileştirmeler

### Liquid Glass tasarımı

Evertag 4.2'nin arayüzü, tüm uygulamada Apple'ın yeni **Liquid Glass** materyaline göre ayarlandı — yarı saydam yüzeyler, daha akıcı animasyonlar ve iOS, iPadOS ve macOS'a doğal olarak uyan rafine kontroller.

### Güncellenmiş bağlantı kütüphaneleri

Evertag'in **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** ve diğer hizmetlerle iletişim kurmak için kullandığı dahili kütüphaneleri yeniledik. Sonuç: kenar durumlarda daha az bağlantı hatası, daha yeni sunucu sürümleri için daha iyi destek ve uzak dosyalarda etiket düzenlemede daha iyi güvenilirlik.

### Çeviri ve yerelleştirme düzeltmeleri

Kullanıcılardan gelen doğrudan geri bildirimlere dayanarak UI'da birden fazla dil düzeltmesi. Birçok dilde küçük düğmelerde daha iyi metin yerleşimi.

### Geri bildiriminizden ilham alınan küçük iyileştirmeler

App Store yorumları ve support@everappz.com adresine gelen e-postalardan gelen birçok küçük iyileştirme. Her mesajı okuyoruz.

## Evertag 4.2'yi edinin

[**Evertag'i App Store'dan indirin**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) veya App Store'dan güncelleyin. Evertag ücretsiz indirilir ve gelişmiş özellikler için isteğe bağlı uygulama içi yükseltmeler sunar. Yeni bulut bağlantıları, ağ protokolleri, Wi-Fi Drive iyileştirmeleri ve Liquid Glass UI temel güncellemenin parçasıdır.

Uygulamayı beğeniyorsanız, lütfen App Store'da bir puan bırakın — bu gerçekten yardımcı oluyor. Geri bildiriminiz var mı veya bir sorunla karşılaştınız mı? Bize **support@everappz.com** adresinden e-posta gönderin. Her mesajı okuyoruz.

## Sıkça Sorulan Sorular

{{% details title="Evertag 4.2'nin yenilikleri neler?" closed="true" %}}
Evertag 4.2, 6'dan fazla yeni bulut ve sunucu bağlantısı (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), çoklu seçim ve daha akıllı yükleme kuyruğu ile yenilenmiş bir Wi-Fi Drive, Liquid Glass UI güncellemeleri, güncellenmiş bağlantı kütüphaneleri, kritik etiket düzenleme hata düzeltmeleri ve çeviri iyileştirmeleri ekler.
{{% /details %}}

{{% details title="Evertag'de ID3v2.4 mü ID3v2.3 mü kullanmalıyım?" closed="true" %}}
Modern oynatıcılar (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, modern Android uygulamaları) ve Latin olmayan karakterler içeren kütüphaneler için **ID3v2.4** kullanın — UTF-8 desteği Çince, Korece, Japonca, Rusça, Arapça ve İbranice etiketleri daha temiz hale getirir. Etiketleriniz bazı uygulamalarda yanlış görüntüleniyorsa, eski araç stereolarını hedefliyorsanız veya bir akış dağıtımcı boru hattı v2.4'ü reddediyorsa **ID3v2.3** kullanın. Her zaman geçiş yapıp yeniden kaydedebilirsiniz.
{{% /details %}}

{{% details title="Düzenlemeden sonra Spotify'da etiketlerim neden yanlış?" closed="true" %}}
Spotify çoğunlukla kendi kataloğundan meta veri görüntüler — yerel etiketleriniz yalnızca «Local Files» için veya sanatçı olarak yüklediğiniz içerik için kullanılır. Spotify Local Files için dosya etiketlemiyor ve doğru görüntülenmiyorsa, Evertag'de ID3v2.4'ü devre dışı bırakıp ID3v2.3 olarak kaydetmeyi deneyin — Spotify'ın ayrıştırıcısı tarihsel olarak v2.4 konusunda muhafazakar olmuştur.
{{% /details %}}

{{% details title="Evertag'de hangi albüm kapağı boyutunu seçmeliyim?" closed="true" %}}
Çoğu kullanıcı için: **Büyük**. Telefonlar, iPad'ler, Mac'ler ve modern araç ekranlarında harika görünür ve dosyaları çok şişirmez. Büyük bir kütüphaneniz varsa ve disk tasarrufu istiyorsanız **Orta** kullanın. Yalnızca arşiv master'ları için veya gerçekten maksimum kalite gerektiğinde **Orijinal** (ölçeklendirme yok) kullanın — ancak bazı eski oynatıcıların çok büyük gömülü sanatlarla zorlandığını unutmayın. **Orijinal** Evertag premium kişiselleştirme yükseltmesinin parçasıdır.
{{% /details %}}

{{% details title="Daha büyük albüm kapakları dosyalarımı büyütür mü?" closed="true" %}}
Evet. 3.000 × 3.000 px sanat eseri gömmek tek bir ses dosyasına birkaç megabayt ekleyebilir. 1.000 parçalık bir kütüphanede gigabaytlara ulaşır. Depolama dar ise Orta veya Büyük kullanın; boyutun önemli olmadığı bir NAS'tan yayın yapıyorsanız Çok büyük veya Orijinal uygundur.
{{% /details %}}

{{% details title="Etiket çoğaltma nedir ve etkinleştirmeli miyim?" closed="true" %}}
Etiket çoğaltma, temel meta verileri dosyanın hem ID3v1 (eski 128 bayt) hem de ID3v2 (modern) bölümlerine yazar. Yalnızca çok eski oynatıcıları veya ID3v1'i okuyan donanımı hedefliyorsanız etkinleştirin. Modern her şey (akıllı telefonlar, bilgisayarlar, son araç stereoları) için kapalı bırakın.
{{% /details %}}

{{% details title="Evertag bulut dosyalarındaki etiketleri doğrudan düzenler mi?" closed="true" %}}
Evet. Bulutunuza (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3 vb.) veya FTP/SFTP/NFS aracılığıyla bağlanın, bir dosya açın ve yerelmiş gibi etiketleri düzenleyin. Evertag dosyayı indirir, düzenlemelerinizi uygular ve güncellenmiş sürümü geri yükler. Ayarlarda «Her zaman sor», «Otomatik yükle» veya «Yükleme» modları arasında seçim yapabilirsiniz.
{{% /details %}}

{{% details title="iPhone'da Evertag ile FLAC etiketlerini düzenleyebilir miyim?" closed="true" %}}
Evet. Evertag, gömülü sanat dahil tam okuma/yazma etiket desteği ile FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE ve diğer önemli formatları destekler.
{{% /details %}}

{{% details title="Ev sunucumda SFTP ile etiketleri nasıl güvenli düzenlerim?" closed="true" %}}
Evertag'i açın, Bağlantılar'a gidin, SFTP'yi seçin ve sunucunuzun ana bilgisayar adı veya IP'sini, bağlantı noktasını (genellikle 22), kullanıcı adınızı ve bir parolayı veya bir SSH özel anahtarını girin. Evertag uzaktaki klasörlerinize göz atacak ve SSH üzerinden uçtan uca şifrelemeyle etiketleri doğrudan düzenleyecektir.
{{% /details %}}

{{% details title="Aynı anda birden fazla dosyanın etiketlerini düzenleyebilir miyim?" closed="true" %}}
Evet. Ayarlarda **Dosyaları aynı anda düzenle**'yi etkinleştirin. Birden fazla dosya seçin, etiket düzenleyiciyi açın ve değiştirdiğiniz herhangi bir alan tüm seçili dosyalara uygulanır. Tüm bir albüm için aynı album artist, yıl veya tür ayarlamanın en hızlı yolu.
{{% /details %}}

{{% details title="Evertag 4.2 güncellemesi ücretsiz mi?" closed="true" %}}
Evet. Evertag App Store'da ücretsiz indirilebilir ve 4.2 mevcut tüm kullanıcılar için ücretsiz bir güncellemedir. Yeni bulut entegrasyonları, Wi-Fi Drive iyileştirmeleri ve Liquid Glass UI temel güncellemenin parçasıdır.
{{% /details %}}

{{% details title="Evertag 4.2 hangi cihazlarda mevcut?" closed="true" %}}
Evertag 4.2 iPhone, iPad ve Mac'te çalışır. iCloud Drive senkronizasyonu, etiket düzenleyici ayarlarınızı cihazlar arasında tutarlı tutar.
{{% /details %}}
