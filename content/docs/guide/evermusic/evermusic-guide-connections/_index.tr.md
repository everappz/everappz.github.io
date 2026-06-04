---
title: "Bağlantılar"
date: 2020-01-01
description: "Evermusic kullanarak bulut hizmetlerini, bilgisayarları, NAS cihazlarını nasıl bağlayacağınızı ve müzik dosyalarınızı nasıl yöneteceğinizi öğrenin. Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes Dosya Paylaşımı ve daha fazlası için adım adım kılavuz."
keywords: [
  "Evermusic", "bulut müzik çalar", "NAS akışı", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes Dosya Paylaşımı",
  "bulut depolama bağlantısı", "müzik transferi iPhone", "dosya yöneticisi iOS"
]
tags: ["evermusic", "rehber", "bağlantılar"]
readingTime: 11
---


Bağlantılar ekranında müziğinizi barındıran her kaynağı bağlayabilirsiniz — popüler bulut hizmetleri, kendi barındırılan medya sunucuları, Mac veya PC'niz, kişisel bir NAS, Apple Time Capsule, WD My Cloud Home, hatta bir USB flash sürücü — ve tümünü tek bir birleşik arayüzden kullanabilirsiniz. Bağlantılar ayrıca derin iç içe geçmiş bulut klasörlerine Hızlı Erişim ayarladığınız ve scrobbling için Last.fm kimlik doğrulaması yaptığınız yerdir.

Ekran, tek bir iCloud Drive hesabından birden fazla bulut ve NAS cihazına yayılmış bir kitaplığa kadar ölçeklenmesi için açıkça etiketlenmiş bölümlere ayrılmıştır: en üstte Hızlı Erişim (favori bulut klasörleriniz), Bulut depolama (eklediğiniz hesaplar), Yerel ağ (Bonjour ile keşfedilen cihazlar), Bilgisayar (Wi-Fi Drive, iTunes Dosya Paylaşımı, SMB), Harici aksesuarlar (bağlı USB flash sürücüler) ve Diğer hizmetler (Last.fm ve benzerleri).

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic Connections Screen" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Bulut depolamaya bağlan

- Bağlantılar sekmesini açın.
- Menüden Bulut depolamaya bağlan'ı seçin.
- Listeden bir bulut depolama hizmeti seçin.
- Sağlayıcının resmi yetkilendirme sayfasında oturum açın (Evermusic şifrenizi asla görmez).
- Tamamlandı'ya dokunun.

{{< cards cols="1">}}
  {{< card title="" subtitle="Connect Cloud Storage Provider Picker" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Herhangi bir sorunla karşılaşırsanız, internet bağlantınızı ve oturum açma kimlik bilgilerinizi iki kez kontrol edin ve o hizmet için iki faktörlü kimlik doğrulamanın doğru şekilde yapılandırıldığından emin olun.  
Uygulamanın Premium sürümünde sınırsız sayıda hizmet ekleyebilirsiniz. Ücretsiz kullanıcılar aynı anda tek bir bulut hesabı bağlayabilir.

## Desteklenen bulut depolama hizmetleri

Evermusic, popüler bulut ve kendi barındırılan hizmetlerin tüm yelpazesini destekler. Ücretsiz kullanıcılar aynı sağlayıcı kataloğunu alır ancak tek hesap sınırıyla; Premium sınırsız hesabın kilidini açar ve diğer sınırların çoğunu kaldırır.

- **Kişisel bulut hesapları:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘)
- **Kendi barındırılan sunucular ve medya kitaplıkları:** Plex · Jellyfin · Emby · Subsonic (ve her Subsonic uyumlu sunucu — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (ve Owncloud, paylaşılan API aracılığıyla) · Synology Drive · QNAP
- **NAS ve dosya paylaşım protokolleri:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (şifre veya public-key kimlik doğrulaması), NFS ve DLNA (salt okunur — oynatma ve indirme)
- **S3 uyumlu nesne depolama:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage veya herhangi bir S3-API uç noktası
- **Yerel ağ keşfi:** Mevcut cihazlar bölümü, Wi-Fi'nızda kendisini Bonjour / mDNS aracılığıyla tanıtan tüm cihazları otomatik olarak listeler — Plex, Jellyfin, Emby sunucuları, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, sürücü takılı AirPort yönlendiricileri vb.

## Güvenlik ve gizlilik

Bağlı bulut hizmetleriyle etkileşim kurmak için yalnızca resmi SDK ve güvenli bağlantı kullanıyoruz. Giriş bilgileriniz ve şifreniz uygulama tarafından erişilemez. Uygulamadan bulut hizmetine yapılan tüm istekler şifrelenir.

Giriş bilgilerinizi ve şifrenizi girdiğinizde, uygulama size bulut hizmeti sağlayıcısı tarafından sağlanan resmi yetkilendirme sayfasını gösterir ve tüm yetkilendirme işlemi uygulama dışında gerçekleşir. Bulut hizmeti sağlayıcısı, başarılı yetkilendirmeden sonra uygulamaya bir auth token gönderir ve bu token API çağrıları yapmak için kullanılır.

Auth-token, üçüncü taraf uygulamaların bulut depolamayla etkileşime girmesine izin veren dijital bir anahtardır. Auth-token, Keychain adı verilen güvenli bir sistem deposunda cihazınızda saklanır. Bağlı bulut hizmetinden dosyaları cihaza indirebilirsiniz ve bu dosyalar uygulamanın "Documents" dizinine yerleştirilir. Bu dosyaları yerleşik dosya yöneticisini kullanarak istediğiniz zaman kaldırabilirsiniz.

Uygulama, bağlı bulut hesabından herhangi bir bilgi paylaşmaz. Web tarayıcınızda hesap ayarları sayfasını açarak bulut hesabınıza erişimi istediğiniz zaman iptal edebilirsiniz.

## Auth-token'ı reddet

Web tarayıcısında hesabınıza giriş yapın ve ayarlar sayfasına gidin. Orada bulut hesabınıza bağlı tüm üçüncü taraf uygulamaları bulabilir ve artık kullanmak istemiyorsanız bunlardan herhangi birini kaldırabilirsiniz. Ayrıntılı talimatlar [burada](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account) mevcuttur.

Bağlı bulut hesaplarını uygulamada da bağlantısını kesebilirsiniz ve auth token de cihazınızdan kaldırılır. Uygulamayı cihazınızdan kaldırırsanız indirilen tüm veriler ve erişim tokenları da kaldırılır.

## Bulut depolamayı bağlantısını kes veya yapılandırmayı değiştir

- Bulut Depolama Seçeneklerine Erişin: İlk olarak, uygulamanın arayüzünde yönetmek istediğiniz bulut depolamayı bulun.
- '...' Düğmesine Dokunun: Hizmet başlığının yanında '...' düğmesi göreceksiniz. Ek seçeneklere erişmek için ona dokunun.
  - **Yeniden Adlandır**: Listedeki bulut hizmetinin adını değiştirmek istiyorsanız 'Yeniden Adlandır'ı seçin.
  - **Ayarlar**: Bulut hizmetinin yapılandırmasını veya kimlik doğrulama verilerini değiştirmek için 'Ayarlar'ı seçin. Bazen, yetkilendirme token'ının süresi dolmuşsa bağlı bulut hizmetini yeniden yetkilendirmeniz gerekebilir.
  - **Bağlantıyı Kes**: Uygulama ile bulut hizmeti arasındaki bağlantıyı tamamen kesmek istiyorsanız 'Bağlantıyı Kes'i seçin. Bu seçeneğin uygulamanın müzik kitaplığından bu bulut hizmetiyle ilişkili tüm şarkıları kaldıracağını, ancak sunucuda kalacağını unutmayın.

{{< cards cols="1">}}
  {{< card title="" subtitle="Connected Cloud Storage More Actions Menu" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Bilgisayara veya NAS'a bağlan

Bilgisayarınızı, kişisel NAS'ınızı veya diğer ağ cihazlarını SMB, DLNA veya WebDAV protokolünü kullanarak da bağlayabilirsiniz.

## SMB kullanarak bilgisayara bağlan

- "Bulut depolamaya bağlan" → SMB'ye dokunun.
- URL alanına smb://computer-ip-address/shared-folder-name formatını kullanarak bilgisayar IP adresini ve paylaşılan klasör adını girin
- Protokol sürümünü seçin: Auto, SMB1, SMB2
- Giriş adı ve şifreyi girin (gerekiyorsa)
- "Tamamlandı"ya dokunun.

Bağlantınız başarılıysa "Bulut depolama" bölümünde bağlı depolamayı göreceksiniz.  
SMB kullanarak MAC veya PC'nizi nasıl bağlayacağınıza dair tam öğretici [burada](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/) mevcuttur.

{{< cards cols="1">}}
  {{< card title="" subtitle="SMB Connection Settings" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## WebDAV kullanarak NAS'a bağlan

URL alanı dışında tüm adımlar aynıdır.  
URL, http://server-name formatında veya sunucu SSL destekliyorsa https://server-name formatında olmalıdır.
WebDAV protokolünü kullanarak NAS'ı nasıl bağlayacağınıza dair tam öğretici [burada](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac) mevcuttur.

{{< cards cols="1">}}
  {{< card title="" subtitle="WebDAV Connection Settings" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## DLNA kullanarak Bilgisayara veya NAS'a bağlan

DLNA protokolünü kullanarak Windows PC'nizde veya kişisel NAS'ınızda bulunan bir müzik kitaplığını paylaşabilir ve bu kitaplığa [burada](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone) açıklandığı gibi uygulamada erişebilirsiniz. DLNA popüler ve yaygın olarak kullanılan bir protokoldür, ancak yalnızca müzik çalmanıza veya indirmenize izin verir. Sunucuya dosya yükleyemez veya yeni klasörler oluşturamazsınız.

{{< cards cols="1">}}
  {{< card title="" subtitle="DLNA Connection Settings" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Mevcut cihazlar

Bu bölüm, uygulama aracılığıyla bağlanabileceğiniz yerel ağınızdaki tüm cihazları gösterir.  
Bir cihazla bağlantı kurmak için şu adımları izleyin:

- Uygulamayı açın ve "Mevcut Cihazlar" bölümüne gidin.
- Listeden bağlanmak istediğiniz cihaza dokunun.
- Gerekirse bağlantıyı tamamlamak için giriş bilgilerinizi girin.

{{< cards cols="1">}}
  {{< card title="" subtitle="Available Devices on the Local Network" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive, bir masaüstü tarayıcısı aracılığıyla bilgisayarınızdan iOS cihazınıza kablosuz dosya aktarımı sağlayan kullanışlı bir teknolojidir.  
Bu özelliği etkili bir şekilde kullanmak için cihazınızın ve bilgisayarınızın aynı Wi-Fi ağına bağlı olduğundan emin olun.  
Wi-Fi Drive'ın nasıl kullanılacağına dair adım adım bir kılavuz aşağıdadır.

## Wi-Fi Drive'ı Etkinleştir

- Uygulamayı açın ve "Bağlantılar" sekmesine gidin.
- Wi-Fi Drive ana ekranına erişmek için "Wi-Fi Üzerinden Bağlan"ı seçin.
- Wi-Fi Drive'ı etkinleştirmek için "Wi-Fi Drive'ı Başlat"a dokunun.

## Bilgisayarınızda Wi-Fi Drive'a Erişin

- Bilgisayarınızda (masaüstü veya dizüstü), bir web tarayıcısı açın (Chrome, Firefox veya Safari gibi).
- Tarayıcının adres çubuğuna uygulama tarafından sağlanan URL'yi girin.

## Dosyaları Kablosuz Aktarın

iOS cihazınıza karşılık gelen web sayfası tarayıcıda açıldığında, bilgisayarınızdan dosyaları web sayfasına kolayca sürükleyip bırakabilirsiniz.  
Sürükleyip bıraktığınız dosyalar iOS cihazınıza aktarılmaya başlar ve uygulama içinde erişilebilir olur.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive Server Settings" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

WiFi-Drive kullanarak dosyaların kablosuz olarak nasıl aktarılacağına dair ayrıntılı talimatlar [burada](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) mevcuttur.

## iTunes Dosya Paylaşımı

iTunes Dosya Paylaşımı, Mac'inizdeki Finder uygulamasını ve lightning kablosunu kullanarak bilgisayardan cihaza dosya aktarmanızı sağlayan başka bir teknolojidir.  
- Sadece bir kablo kullanarak cihazı bilgisayara bağlayın ve Mac'inizde Finder uygulamasını çalıştırın.
- "Konumlar" → "Bağlı Cihazınız" → "Dosyalar" → bölümünü açın ve Evermusic uygulamasını bulun.
- Tüm paylaşılan klasörleri görmek için uygulama simgesine dokunun.
- Sürükle-bırak kullanarak bilgisayardan cihazın paylaşılan klasörüne dosyaları kopyalayın.

iTunes dosya paylaşımının nasıl kullanılacağına dair ayrıntılı talimatlar [burada](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/) mevcuttur.

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder File Sharing on Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## USB flash kart bağla

Bir SD kartınız varsa, lightning kart okuyucu kullanarak bağlayabilirsiniz. Uygulama şu anda Apple Certified kart okuyucuları ve iXpand Flash Drive'ları desteklemektedir. iXpand Flash Drive'ınız varsa — lightning bağlantı noktasına takın ve uygulamayı açın. 'Harici cihaz bağlandı' mesajı ve cihaz bilgilerini göreceksiniz. Müzik klasörüne erişmek için flash sürücü simgesine dokunun ve çalmaya başlamak için herhangi bir ses dosyasına dokunun. iPhone'a USB flash kart bağlama ve üzerindeki müziği dinleme veya dosyaları yönetme hakkında ayrıntılı talimatlarımız [burada](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it) mevcuttur.

## Dosya Yöneticisi

Bir bulut depolama hizmeti bağladıktan sonra, mevcut tüm dosya ve klasörleri görüntülemek için simgesine dokunun. Bu dosyalarla çalışmak için yerleşik dosya yöneticisini kullanabilirsiniz — indirme, yeniden adlandırma, taşıma ve daha fazlası. Bir indirme başlattığınızda, dosya aktarım kuyruğunda görünür. Aktarım kuyruğunu görüntülemek için "Yerel Dosyalar" sekmesine gidin ve sol üst köşedeki dönen okları dokunun. İndirilen tüm dosyalar ve klasörler "Yerel Dosyalar" bölümünde mevcuttur.

## Üst Araç Çubuğu

Gezinme çubuğunun altında uygun biçimde bulunan üst araç çubuğu, kolay erişim için birkaç kullanışlı eylem sunar. Bu araç çubuğunu basit bir aşağı kaydırma hareketiyle gösterebilir veya gizleyebilirsiniz. İşte mevcut eylemler:

- **Ara**: Bu seçenek, belirli dosyaları veya klasörleri bulmayı kolaylaştırarak mevcut dizinde hızlı arama yapmanıza olanak tanır.
- **Çalmayı Sürdür**: Uygulama ayarlarında etkinleştirilmişse, bu özellik mevcut klasör için ses oynatıcı kuyruğunu ve son medya konumunu geri yükler. Müzik kitaplığınızda kaldığınız yerden devam etmenin kullanışlı bir yoludur.
- **Tümünü Oynat**: Bu eylemi seçerek uygulama mevcut klasörü ve alt klasörlerini tarar, bulunan tüm ses dosyalarını yeni bir oynatıcı kuyruğuna ekler. Belirli bir dizindeki tüm müziği çalmak istediğinizde kullanışlıdır.
- **Tümünü Karıştır**: "Tümünü Oynat"a benzer, ancak bu eylem mevcut klasörü ve alt klasörlerini tarar ancak dosyaları ses oynatıcı kuyruğuna eklemeden önce karıştırır. Müziğinizi biraz çeşitlilik için rastgele sırayla keyifle dinlemenin harika bir yoludur.

{{< cards cols="1">}}
  {{< card title="" subtitle="Top Toolbar Inside a Cloud Folder" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Klasör Seçenekleri

Uygulamada bir klasör açtığınızda, ekranın sağ üst köşesindeki "..." düğmesine dokunarak mevcut kullanışlı bir eylem seti bulacaksınız.  
Bu eylemlerin dökümü şöyledir:

- **Seçmek**: Dosya seçim modunu etkinleştirin. Bu mod, klasör içindeki bir veya daha fazla dosyayı seçmenizi sağlar, seçilen öğeler üzerinde eylem gerçekleştirmeyi kolaylaştırır.
- **Yeni Klasör**: Mevcut klasör içinde yeni bir klasör oluşturun. Bu özellik dosyalarınızı düzenlemenize ve kitaplığınızı iyi yapılandırılmış tutmanıza olanak tanır.
- **Çevrimdışı modu etkinleştirmek**: Mevcut klasör için çevrimdışı modu açın. Çevrimdışı mod basit indirmenin ötesine geçer; klasörü değişiklikler için aktif olarak izler. Klasöre çevrimiçi yeni dosyalar eklerseniz, uygulama bu dosyaları otomatik olarak cihazınıza indirir. Bu, yerel kitaplığınızın sunucudaki değişikliklerle güncel kalmasını sağlar.
- **Dosya Yükle**: Cihazınızdaki dosyaları çevrimiçi klasöre yükleyin. Bu eylem dosyaları buluta veya sunucuya aktarmanıza olanak tanır, her yerden erişilebilir yapar.
- **Ara**: Mevcut klasörde belirli dosyaları arayın. Bu özellikle büyük bir koleksiyonda belirli öğeleri hızla bulmak için kullanışlıdır.
- **Sırala**: Klasördeki dosyaları ad, boyut veya düzenleme tarihi gibi ölçütlere göre sıralayın. Varsayılan sıralama modu genellikle sunucudaki sıralama düzenini yansıtır, ancak tercihlerinize göre değiştirebilirsiniz.
- **Izgara/Liste Görünümü**: İki görüntüleme modu arasında geçiş yapın: tablo görünümü ve küçük resim görünümü. Tablo görünümü dosyaları bir listede sunarken, küçük resim görünümü dosyaların görsel temsillerini gösterir, bakışta içeriği tanımlamayı kolaylaştırır.

{{< cards cols="1">}}
  {{< card title="" subtitle="Current Folder More Actions Menu" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Çevrimiçi Dosyaları Düzenle

Evermusic'te bulut depolamada birden fazla dosyayı yönetmeniz gerektiğinde, eylemlerinizi kolaylaştırmak için seçim modunu kullanabilirsiniz. Etkili dosya yönetimi için şu adımları izleyin:

- **Seçim Modunu Etkinleştir**: Uygulamayı cihazınızda açın ve bulut depolamanızı içeren bölüme gidin. Sağ üst köşede "..." (üç nokta) düğmesini bulun. Seçim modunu etkinleştirmek için üzerine dokunun ve "Seçmek" menü öğesini seçin.
- **Dosyaları Seçin**: Listede her dosya veya klasörün yanında onay kutuları görünecektir. Yanlarındaki onay kutularına dokunarak bir veya birden fazla dosya veya klasör seçin.
- **Çeşitli Eylemler Gerçekleştirin**: Yönetmek istediğiniz dosya veya klasörleri seçtikten sonra, ihtiyaçlarınıza göre özelleştirilmiş çeşitli eylemlere erişebileceksiniz:

{{< cards cols="1">}}
  {{< card title="" subtitle="Selection Mode for Online Files" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Dosya eylemleri

Dosyanın başlığının yanında "..." sembolünü (üç nokta) göreceksiniz — bu eylemler menüsüdür.  
Mevcut eylemlerin listesini ortaya çıkarmak için ona dokunun:

- **Sıradaki Çal**: Seçilen dosyayı oynatıcı kuyruğunuzun en üstüne eklemek için bu eylemi seçin, o anda çalan öğenin hemen ardından çalınmasını sağlar.
- **Sonra Çal**: Bu seçeneği seçmek dosyayı oynatıcı kuyruğunuzun en altına ekler, mevcut kuyruktan sonra çalınmasını sağlar.
- **Müzik Kitaplığına Ekle**: Bu eylem, dosyayı müzik kitaplığınıza dahil etmenize olanak tanır, sanatçı, albüm, tür veya besteciye göre kolayca erişilebilir ve düzenli hale getirir.
- **Oynatma Listesine Ekle**: Dosyayı mevcut bir oynatma listesine eklemek veya yeni bir tane oluşturmak için bu eylemi kullanın.
- **Ses etiketlerini düzenlemek**: Bu seçeneği seçerek Evermusic'in yerleşik etiket düzenleyicisine erişebilir, seçilen dosya için ses etiketlerini değiştirmenize olanak tanır. Dosya geçici olarak bir geçici dizine indirilir ve ardından değişiklikleri onayladıktan sonra depolama alanına yüklenir.
- **Favorilere Ekle**: Bu eylem dosyayı hızlı ve kolay erişim için favori dosyalar listenize ekler.
- **İndirmek**: Dosyayı veya klasörü cihazınıza indirmek, çevrimdışı kullanım için erişilebilir kılmak için bu eylemi seçin.
- **Yeniden Adlandır**: Bu seçenek uzak depolamada doğrudan dosyayı yeniden adlandırmanıza olanak tanır, özelleştirilmiş dosya adlandırmasına izin verir.
- **Taşı**: Dosyayı bulut depolamada farklı bir klasöre taşımak için bu eylemi seçin, düzenli bir dosya yapısını korumaya yardımcı olur.
- **Şurada Aç**: Dosyayı başka bir uyumlu uygulamaya dışa aktarmak için bu eylemi kullanın. Dosya cihazınıza indirilir ve ardından daha fazla paylaşım veya etkileşim için Paylaş iletişim kutusu görünür.
- **Silmek**: Dosyayı bulut depolamanızdan kalıcı olarak kaldırdığı için bu eylemle dikkatli olun. Bu silme işlemi geri alınamaz.

{{< cards cols="1">}}
  {{< card title="" subtitle="More Actions Menu for a Single File" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Eylemler listesi mevcut ekran alanını aşarsa, ek seçeneklere erişmek için eylemler menüsünde aşağı kaydırın.

## Klasör eylemleri

Bulut depolamada her klasör için çeşitli eylemler mevcuttur. Bu seçeneklere erişmek için klasör başlığının yanında bulunan üç nokta "..." simgesine dokunun. Tüm eylemleri göremiyorsanız daha fazla seçenek ortaya çıkarmak için aşağı kaydırın. İşte mevcut eylemler:

- **Tümünü Oynat**: Mevcut oynatıcı kuyruğunu seçilen klasördeki tüm öğelerle değiştirin.
- **Sıradaki Çal**: Tüm klasörü oynatıcı kuyruğunun en üstüne, o anda çalan öğenin hemen ardından ekleyin.
- **Sonra Çal**: Klasör içeriğini oynatıcı kuyruğunun en altına ekleyin.
- **Müzik Kitaplığına Ekle**: Bu eylem, klasörün içeriğini müzik kitaplığınıza sorunsuz bir şekilde dahil eder, sanatçı, albüm, tür veya besteciye göre kolayca erişilebilir ve düzenli hale getirir.
- **Oynatma Listesine Ekle**: Tüm klasörü bir oynatma listesine dahil edebilirsiniz. Ayrıca yeni bir oynatma listesi oluşturma seçeneğiniz de var ve klasörün adı otomatik olarak atanacak.
- **Favorilere Ekle**: Klasörü hızlı ve kolay erişim için favori dosyalar listenize eklemek için bu eylemi kullanın.
- **Çevrimdışı modu etkinleştirmek**: Seçilen klasör için çevrimdışı modu etkinleştirerek, uygulama basit indirmenin ötesine geçer. Değişiklikleri sürekli tarar ve çevrimiçi klasöre yeni dosyalar eklenirse bunlar otomatik olarak uygulamaya indirilir.
- **İndirmek**: Çevrimdışı erişim için klasörün tüm içeriğini cihazınıza indirin.
- **Yeniden Adlandır**: Klasörü doğrudan uzak depolamada yeniden adlandırın.
- **Taşı**: Klasörü bulut depolamada farklı bir konuma taşıyın.
- **Silmek**: Klasörü ve içeriğini bulut depolamanızdan kalıcı olarak kaldırdığı için bu eylemle dikkatli olun. Bu eylem geri alınamaz.


## Hızlı Erişim

Hızlı Erişim bölümü ekranın en üstünde bulunur. Bağlı bulut hizmetlerinden favori ve son açılan dosyalarınıza hızlı erişim sağlar.
Buluttan bir dosya veya klasör her açtığınızda "Son Açılanlar" listesine eklenir. Bu listeyi temizlemek için "Sonlar"ı açın, "Daha fazla eylem" düğmesine dokunun ve "Listeyi Sil"i seçin. Ayrıca dizin yapısını kazımadan onlara hızlıca erişmek için derin iç içe geçmiş klasörleri Favoriler olarak işaretleyebilirsiniz.

## Diğer Hizmetler

Bu bölüm deneyiminizi geliştiren ekstra özellikleri gösterir. Şu anda uygulama Last.fm scrobbling desteklemektedir. Bağlandığında, oynatma istatistikleriniz otomatik olarak Last.fm hesabınıza gönderilir. Dinleme analitiğini görüntülemek ve kişiselleştirilmiş müzik önerileri almak için daha sonra Last.fm profilinizi ziyaret edebilirsiniz. Ayrıntılı kurulum talimatları [burada](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm) mevcuttur.
