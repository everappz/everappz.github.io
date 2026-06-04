---
title: "Bağlantılar"
date: 2020-02-01
description: "Evertag'a bulut depolama, NAS ve bilgisayarınızı nasıl bağlayacağınızı öğrenin. Bulut depolama, kişisel NAS veya Mac/PC'den doğrudan ses dosyalarına erişin ve düzenleyin."
keywords: [
  "Evertag bulut kurulumu", "iCloud'u Evertag'a bağla", "SMB dosya erişimi iOS",
  "WebDAV ses etiketi düzenleyicisi", "NAS meta veri düzenleme", "Wi-Fi Drive Evertag",
  "ses dosyalarını iPhone'a aktar", "Evertag iTunes File Sharing", "buluttan FLAC etiketlerini düzenle"
]
tags: ["kılavuz", "evertag", "bağlantılar"]
readingTime: 11
---


Bu ekranda ses dosyalarınızı içeren çeşitli kaynakları bağlayabilirsiniz. Google Drive, Dropbox, OneDrive, iCloud ve diğerleri gibi popüler bulut hizmetlerini entegre edebilir, ayrıca Mac veya PC'nizi bağlayabilirsiniz. Bunlara ek olarak, Apple Time Capsule, WD Cloud Home veya SMB ya da WebDAV destekleyen herhangi bir NAS'ta bulunan ses dosyalarını düzenleme seçeneğiniz de mevcuttur.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Bağlantılar Ekranı" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Hızlı erişim

Bağlantılar ekranının üst kısmında bir **Hızlı erişim** listesi bulacaksınız. Favorilere eklediğiniz her bulut klasörü — birkaç seviye derinde olsa bile — burada görünür, böylece her seferinde üst klasörlerde gezinmeden doğrudan erişebilirsiniz.

## Bulut depolamaya bağlan

- 'Bağlantılar' sekmesini açın
- Menüden 'Bulut depolamaya bağlan' seçeneğini seçin
- Listeden bir bulut depolama hizmeti seçin
- Kimlik bilgilerinizi girin ve 'Tamamlandı'ya dokunun.

Herhangi bir sorunla karşılaşırsanız internet bağlantınızı ve giriş bilgilerinizi/parolanızı kontrol edin.  
Uygulamanın Premium sürümünde sınırsız sayıda hizmet ekleyebilirsiniz.

## Desteklenen bulut depolama hizmetleri

Uygulama şu anda en popüler bulut depolama hizmetlerini desteklemektedir: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), ayrıca herhangi bir SMB veya WebDAV sunucusu.

## Güvenlik ve gizlilik

Bağlı bulut hizmetleriyle etkileşim kurmak için yalnızca resmi SDK'ler ve güvenli bağlantılar kullanıyoruz. Giriş adınız ve parolanız uygulamaya erişilemez. Uygulamadan bulut hizmetine yapılan tüm istekler şifrelenir.

Giriş adınızı ve parolanızı girdiğinizde, uygulama size bulut hizmeti sağlayıcısı tarafından sağlanan resmi yetkilendirme sayfasını gösterir ve tüm yetkilendirme süreci uygulamanın dışında gerçekleşir. Bulut hizmeti sağlayıcısı, başarılı yetkilendirmeden sonra uygulamaya bir auth token gönderir ve bu token API çağrıları yapmak için kullanılır.

Auth token, üçüncü taraf uygulamaların bulut depolamayla etkileşim kurmasına izin veren bir dijital anahtardır. Auth token, Keychain adı verilen güvenli bir sistem depolama alanında cihazınızda saklanır. Bağlı bulut hizmetinden dosyalarınızı cihaza indirebilirsiniz ve bu dosyalar uygulamanın "Belgeler" dizinine yerleştirilir. Bu dosyaları yerleşik dosya yöneticisini kullanarak istediğiniz zaman kaldırabilirsiniz.

Uygulama, bağlı bulut hesabından herhangi bir bilgiyi paylaşmaz. Web tarayıcınızda hesap ayarları sayfasını açarak bulut hesabınıza erişimi istediğiniz zaman iptal edebilirsiniz.

## Auth-token'ı reddet

Bir web tarayıcısında hesabınıza giriş yapın ve ayarlar sayfasına gidin. Orada, bulut hesabınıza bağlı tüm üçüncü taraf uygulamaları bulabilir ve artık kullanmak istemediğiniz uygulamaları kaldırabilirsiniz. Ayrıntılı talimatlar [burada](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account) mevcuttur.

Ayrıca uygulamada bağlı bulut hesaplarının bağlantısını kesebilirsiniz ve auth token cihazınızdan da kaldırılır. Uygulamayı cihazınızdan kaldırırsanız, tüm indirilen veriler ve erişim token'ları da kaldırılır.

## Bulut depolamayı bağlantısını kes veya yapılandırmayı değiştir

- Bulut Depolama Seçeneklerine Erişim: Önce uygulamanın arayüzünde yönetmek istediğiniz bulut depolamayı bulun.
- '...' Düğmesine Dokunun: Hizmet başlığının yanında bir '...' düğmesi göreceksiniz. Ek seçeneklere erişmek için dokunun.
  - **Yeniden Adlandır**: Listenizde göründüğü şekliyle bulut hizmetinin adını değiştirmek isterseniz 'Yeniden Adlandır'ı seçin.
  - **Ayarlar**: Bulut hizmeti için yapılandırmayı veya kimlik doğrulama verilerini değiştirmek için 'Ayarlar'ı seçin. Bazen yetkilendirme token'ı süresi dolmuşsa bağlı bulut hizmetini yeniden yetkilendirmeniz gerekebilir.
  - **Bağlantıyı Kes**: Uygulama ile bulut hizmeti arasındaki bağlantıyı tamamen kesmek isterseniz 'Bağlantıyı Kes'i seçin. Bu seçeneğin seçilmesinin, bu bulut hizmetiyle ilişkili tüm şarkıları uygulamanın müzik kütüphanesinden kaldıracağını, ancak bunların sunucuda kalacağını unutmayın.

## Bilgisayara veya NAS'a Bağlan

Bilgisayarınızı, kişisel NAS'ınızı veya diğer ağ cihazlarını SMB, DLNA veya WebDAV protokolünü kullanarak da bağlayabilirsiniz.

## SMB kullanarak bilgisayara bağlan

- "Bulut depolamaya bağlan" → SMB'ye dokunun.
- URL alanına bilgisayarın IP adresini ve paylaşılan klasör adını smb://bilgisayar-ip-adresi/paylaşılan-klasör-adı biçiminde girin
- Protokol sürümünü seçin: Otomatik, SMB1, SMB2
- Giriş adı ve parolayı girin (gerekiyorsa)
- "Tamamlandı"ya dokunun.

Bağlantınız başarılıysa "Bulut depolama" bölümünde bağlı depolamayı göreceksiniz.  
SMB kullanarak Mac veya PC'nizi nasıl bağlayacağınıza dair tam bir öğretici [burada](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/) mevcuttur.

## WebDAV kullanarak NAS'a bağlan

Tüm adımlar URL alanı hariç aynıdır.  
URL, http://sunucu-adı biçiminde veya sunucu SSL destekliyorsa https://sunucu-adı biçiminde olmalıdır.  
WebDAV protokolünü kullanarak NAS'a nasıl bağlanılacağına dair tam bir öğretici [burada](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac) mevcuttur.

## Mevcut cihazlar

Bu bölüm, uygulamanın aracılığıyla bağlanabileceğiniz yerel ağınızdaki tüm cihazları görüntüler.  
Bir cihazla bağlantı kurmak için şu adımları izleyin:

- Uygulamayı açın ve "Mevcut Cihazlar" bölümüne gidin.
- Listeden bağlanmak istediğiniz cihaza dokunun.
- Gerekirse bağlantıyı tamamlamak için giriş bilgilerinizi girin.

## Wi-Fi Drive

Wi-Fi Drive, masaüstü tarayıcı aracılığıyla bilgisayarınızdan iOS cihazınıza kablosuz dosya aktarımı sağlayan kullanışlı bir teknolojidir.  
Bu özelliği etkili biçimde kullanmak için cihazınızın ve bilgisayarınızın aynı Wi-Fi ağına bağlı olduğundan emin olun.  
Wi-Fi Drive'ın nasıl kullanılacağına dair adım adım bir kılavuz aşağıda verilmiştir.

## Wi-Fi Drive'ı Etkinleştir

- Uygulamayı açın ve "Bağlantılar" sekmesine gidin.
- Wi-Fi Drive ana ekranına erişmek için "Wi-Fi üzerinden bağlan"ı seçin.
- Wi-Fi Drive'ı etkinleştirmek için "Wi-Fi Drive'ı Başlat"a dokunun.

## Bilgisayarınızda Wi-Fi Drive'a Erişin

- Bilgisayarınızda (masaüstü veya dizüstü), bir web tarayıcısı açın (Chrome, Firefox veya Safari gibi).
- Tarayıcının adres çubuğuna, uygulama tarafından sağlanan URL'yi girin.

## Dosyaları Kablosuz Aktarın

iOS cihazınıza karşılık gelen web sayfası tarayıcıda açıldığında, bilgisayarınızdan dosyaları web sayfasına kolayca sürükleyip bırakabilirsiniz.  
Sürükleyip bıraktığınız dosyalar iOS cihazınıza aktarılmaya başlayacak ve uygulama içinde erişilebilir olacak.

Wi-Fi Drive kullanarak dosyaları kablosuz aktarmanın ayrıntılı talimatları [burada](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive) mevcuttur.

## iTunes File Sharing

iTunes File Sharing, Mac'inizdeki Finder uygulamasını ve bir Lightning kablosunu kullanarak bilgisayardan cihaza dosya aktarmanızı sağlayan başka bir teknolojidir.  
- Cihazı bir kablo kullanarak bilgisayara bağlayın ve Mac'inizde Finder uygulamasını çalıştırın.
- "Konumlar" → "Bağlı Cihazınız" → "Dosyalar" → bölümünü açın ve mevcut uygulamayı bulun.
- Tüm paylaşılan klasörleri görmek için uygulama simgesine dokunun.
- Sürükle-bırak kullanarak dosyaları bilgisayardan cihazdaki paylaşılan klasöre kopyalayın.

iTunes File Sharing'in nasıl kullanılacağına dair ayrıntılı talimatlar [burada](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/) mevcuttur.

## USB flash kart bağla

Bir SD kart veya USB belleğiniz varsa, iPhone/iPad'deki Lightning veya USB-C kart okuyucu ile bağlayabilir ya da doğrudan Mac'e takabilirsiniz. Uygulama şu anda Apple Sertifikalı kart okuyucuları desteklemektedir. iPhone veya iPad'e USB flash kart bağlama ve üzerindeki dosyaları yönetme hakkında ayrıntılı talimatlarımız [burada](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it) mevcuttur. Bağlı sürücüler Bağlantılar ekranının **Bağlı aksesuarlar** bölümünde görünür.

## Dosya Yöneticisi

Bir bulut depolama hizmetini bağladıktan sonra, mevcut tüm dosyaları ve klasörleri görmek için simgesine dokunun. Bu dosyalarla çalışmak için yerleşik dosya yöneticisini kullanabilirsiniz — indirme, yeniden adlandırma, taşıma ve daha fazlası. Bir indirme başlattığınızda, dosya aktarım kuyruğunda görünür. Aktarım kuyruğunu görüntülemek için "Yerel Dosyalar" sekmesine gidin ve sol üst köşedeki dönen oklara dokunun. İndirilen tüm dosyalar ve klasörler "Yerel Dosyalar" bölümünde mevcuttur.

## Üst Araç Çubuğu

Gezinme çubuğunun altında uygun şekilde konumlanmış üst araç çubuğu, kolay erişim için çeşitli kullanışlı eylemler sunar. Bu araç çubuğunu basit bir aşağı kaydırma hareketiyle gösterebilir veya gizleyebilirsiniz. Mevcut eylemler şunlardır:

- **Ara**: Bu seçenek, geçerli dizinde hızlı arama yapmanıza olanak tanıyarak belirli dosya veya klasörleri bulmayı kolaylaştırır.

## Klasör Seçenekleri

Uygulamada bir klasör açtığınızda, ekranın sağ üst köşesindeki "..." düğmesine dokunarak kullanılabilecek pratik eylemler bulacaksınız.  
Bu eylemlerin ayrıntıları şöyledir:

- **Seçmek**: Dosya seçim modunu etkinleştirin. Bu mod, klasördeki bir veya daha fazla dosyayı seçmenize olanak tanıyarak seçilen öğeler üzerinde eylem gerçekleştirmeyi kolaylaştırır.
- **Yeni Klasör**: Geçerli klasörde yeni bir klasör oluşturun. Bu özellik dosyalarınızı düzenlemenizi ve kütüphanenizi iyi yapılandırılmış tutmanızı sağlar.
- **Dosyaları Yükle**: Cihazınızdan çevrimiçi klasöre dosya yükleyin. Bu eylem, dosyaları buluta veya sunucuya aktarmanıza olanak tanıyarak her yerden erişilebilir kılar.
- **Ara**: Geçerli klasördeki belirli dosyaları arayın. Bu özellik özellikle büyük bir koleksiyondaki belirli öğeleri hızlıca bulmak için kullanışlıdır.
- **Sırala**: Klasördeki dosyaları ad, boyut veya düzenleme tarihi gibi ölçütlere göre sıralayın. Varsayılan sıralama modu genellikle sunucudaki sıralama düzenini yansıtır, ancak tercihlerinize göre değiştirebilirsiniz.
- **Izgara/Liste Görünümü**: İki görüntüleme modu arasında geçiş yapın: tablo görünümü ve küçük resim görünümü. Tablo görünümü dosyaları bir listede sunarken, küçük resim görünümü dosyaların görsel temsillerini göstererek içeriği tek bakışta tanımlamayı kolaylaştırır.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Bulut Klasörü Sıralaması" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Çevrimiçi Dosyaları Düzenle

Bu uygulamada bulut depolamadaki birden fazla dosyayı yönetmeniz gerektiğinde, eylemlerinizi kolaylaştırmak için seçim modunu kullanabilirsiniz. Etkili dosya yönetimi için şu adımları izleyin:

- **Seçim Modunu Etkinleştir**: Cihazınızda uygulamayı açın ve bulut depolamanızı içeren bölüme gidin. Sağ üst köşedeki "..." (üç nokta) düğmesini arayın. Seçim modunu etkinleştirmek için dokunun ve "Seçmek" menü öğesini seçin.
- **Dosya Seçin**: Listelenen her dosya veya klasörün yanında onay kutuları göreceksiniz. Yanlarındaki onay kutularına dokunarak bir veya birden fazla dosya veya klasör seçin.
- **Çeşitli Eylemleri Gerçekleştirin**: Yönetmek istediğiniz dosyaları veya klasörleri seçtikten sonra, ihtiyaçlarınıza göre uyarlanmış çeşitli eylemlere erişebileceksiniz:

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Dosya Seçimi" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Dosya eylemleri

Dosyanın başlığının yanında üç nokta "..." sembolü göreceksiniz — bu eylemler menüsüdür.  
Kullanılabilir eylemlerin listesini görüntülemek için dokunun:

- **Ses Etiketlerini Düzenle**: Bu seçeneği seçerek, seçilen dosya için ses etiketlerini değiştirmenize olanak tanıyan yerleşik etiket düzenleyicisine erişebilirsiniz. Dosya geçici bir dizine geçici olarak indirilir ve değişiklikleri onayladıktan sonra depolamaya yüklenir.
- **Favorilere Ekle**: Bu eylem, hızlı ve kolay erişim için dosyayı favori dosyalar listenize ekler.
- **İndirmek**: Dosyayı veya klasörü cihazınıza indirmek ve çevrimdışı kullanım için erişilebilir kılmak için bu eylemi seçin.
- **Yeniden Adlandır**: Bu seçenek, dosyayı doğrudan uzak depolamada yeniden adlandırmanıza olanak tanır.
- **Taşı**: Dosyayı bulut depolamanızdaki farklı bir klasöre taşımak için bu eylemi seçin.
- **Farklı Aç**: Dosyayı başka uyumlu bir uygulamaya aktarmak için bu eylemi kullanın. Dosya cihazınıza indirilir ve ardından daha fazla paylaşım veya etkileşim için Paylaş iletişim kutusu görünür.
- **Silmek**: Bu eylemde dikkatli olun, zira dosyayı bulut depolamanızdan kalıcı olarak kaldırır. **Bu silme işlemi geri alınamaz**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Dosya Seçenekleri" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Eylemler listesi mevcut ekran alanını aşarsa, ek seçeneklere erişmek için eylemler menüsünde aşağı kaydırın.

## Klasör eylemleri

Bulut depolamanızdaki her klasör için çeşitli eylemler mevcuttur. Bu seçeneklere erişmek için klasör başlığının yanındaki "..." elips simgesine dokunun. Tüm eylemleri görmüyorsanız, daha fazla seçenek görmek için aşağı kaydırın. Mevcut eylemler şunlardır:

- **Favorilere Ekle**: Hızlı ve kolay erişim için klasörü favori dosyalar listenize eklemek için bu eylemi kullanın.
- **İndir**: Çevrimdışı erişim için klasörün tüm içeriğini cihazınıza indirin.
- **Yeniden Adlandır**: Klasörü doğrudan uzak depolamada yeniden adlandırın.
- **Taşı**: Klasörü bulut depolamanızdaki farklı bir konuma taşıyın.
- **Silmek**: Bu eylemde dikkatli olun, zira klasörü ve içeriğini bulut depolamanızdan kalıcı olarak kaldırır. **Bu eylem geri alınamaz**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Klasör Seçenekleri" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
