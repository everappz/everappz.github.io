---
title: "M3U Çalma Listesini Evermusic ve Flacbox'a Nasıl Aktarılır"
date: 2024-01-31
description: "Bulut, yerel depolama veya cihazdan M3U, M3U8 ve CUE çalma listesi dosyalarını Evermusic ve Flacbox'a nasıl aktaracağınızı öğrenin."
keywords: ["evermusic", "flacbox", "çalma listesi", "m3u", "m3u8", "cue", "içe aktarma", "müzik uygulaması"]
tags: ["evermusic", "içe aktarma", "çalma listeleri", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Özet:** Evermusic ve Flacbox, bulut depolama, yerel uygulama dosyaları veya cihazınızdan M3U, M3U8 ve CUE çalma listesi dosyalarının içe aktarılmasını destekler. Çalma Listeleri > Daha fazla > Çalma Listesi İçe Aktar'a gidin, bir kaynak seçin, dosyanızı seçin ve uygulama çalma listenizi otomatik olarak oluşturur.

M3U, MP3 URL veya Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator'ın kısaltması olup, multimedya çalma listeleri için kullanılan bir bilgisayar dosya biçimidir. Başlıca kullanımlarından biri, internetteki akışlara işaret eden tek girişli çalma listesi dosyaları oluşturmaktır. Bu dosyalar, akış içeriğine kolay erişim sağlar ve yaygın olarak indirmeler, e-posta ve internet radyosu dinlemek için kullanılır.

Yaygın kullanımına rağmen, M3U biçimi için resmi bir spesifikasyon yoktur; fiili bir standart haline gelmiştir. Bir M3U dosyası, özünde bir veya daha fazla medya dosyasının konumlarını belirten düz bir metin dosyasıdır. Kodlamaya bağlı olarak "m3u" veya "m3u8" dosya uzantısıyla kaydedilir. Dosyadaki her giriş, bir medya dosyasının konumunu belirtir; bu konum mutlak bir yerel yol adı, M3U dosya konumuna göre göreli bir yerel yol adı veya bir URL olabilir. Girişler satır sonlarıyla ayrılır ve bazı cihazlar CR LF olarak temsil edilen satır sonları gerektirir.

Ayrıca, M3U dosyaları "#" karakteriyle başlayan yorumlar içerebilir. Genişletilmiş M3U'da "#", iki nokta üst üste ":" ile sonlandırılan parametreleri destekleyebilen genişletilmiş M3U yönergelerini tanıtır.

Evermusic ve Flacbox uygulamalarımızda, M3U dosya içe aktarma işlevselliğini uyguladık ve manuel çalma listesi oluşturma ihtiyacını ortadan kaldırdık. Bu kılavuz, çalma listelerinizi bulut depolamadan, yerel dosyalardan veya cihazınızdaki dosyalardan doğrudan uygulamaya aktarma sürecinde size rehberlik edecektir.

Öncelikle 'Çalma Listeleri' bölümüne gidin. Ardından sağ üst köşedeki 'Daha fazla' düğmesine dokunun. Görünen menüden 'Çalma listesi içe aktar' seçeneğini seçin.

![çalma listesi içe aktarma işlemi](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Sonraki ekranda dosya konumunu seçin. Desteklenen seçenekler şunlardır:

- Bağlı bulut depolama;
- Uygulamadaki dosyalar;
- Cihazınızdaki dosyalar;

![dosya konumu seçin](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Bağlı bulut depolamayı seçelim ve çalma listesi dosyasını içeren klasörü açalım. Desteklenen çalma listesi dosya uzantıları M3U, M3U8 ve CUE'dir. Çalma listesi dosyasını seçin ve seçiminizi onaylamak için 'Tamamlandı' düğmesine dokunun.

![M3U dosyası seçin](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Uygulama çalma listesi dosyasını ayrıştıracak ve bir parça listesi oluşturacaktır. Ardından bu dosyaları depolamada bulacak ve müzik kitaplığına aktarılacak nihai bir çalma listesi derleyecektir. M3U/CUE dosyanızın medya dosyaları için doğru yolları içermesi ve dosyaların depolamanızdaki bu yollarda bulunması çok önemlidir.

![içe aktarılan çalma listesi](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Uygulama hem göreli yolları hem de mutlak dosya URL'lerini destekler.

Örneğin:

Göreli yollu çalma listesi:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Mutlak URL'li çalma listesi:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Uygulama içinde bulunan bir çalma listesi dosyasını içe aktarıyorsanız (Yerel dosyalar bölümü), ek adım gerekmez.

Ancak, sistem dosya seçicisini kullanarak cihazınızda bulunan bir çalma listesini içe aktarmak istiyorsanız, akılda tutulması gereken önemli bir husus vardır.

Güvenlik politikaları nedeniyle, uygulama yalnızca sistem dosya seçicisiyle seçtiğiniz dosyaya erişebilir. Ancak çalma listesi dosyası, cihazınızdaki diğer medya dosyalarına bağlantılar içerebilir. Cihazınızdan bir çalma listesini içe aktarmak için hem çalma listesi dosyasını hem de ona bağlı tüm medya dosyalarını içeren bir klasör seçmelisiniz. Bu durumda, uygulama seçilen klasörü tarayacak, çalma listesi dosyasını bulacak, parça listesini oluşturacak ve müzik kitaplığına aktaracaktır.

Ayrıca, "Daha fazla eylem" düğmesine dokunup "Bir Klasörden Çalma Listeleri İçe Aktar" seçeneğini seçerek birden fazla çalma listesini aynı anda içe aktarabilirsiniz. Uygulama daha sonra klasörün içeriğini tarayacak, desteklenen çalma listesi dosyalarını bulacak ve kitaplığa aktaracaktır.

## Sıkça Sorulan Sorular

{{% details title="Evermusic ve Flacbox hangi çalma listesi biçimlerini destekler?" closed="true" %}}
Her iki uygulama da M3U, M3U8 ve CUE çalma listesi dosya biçimlerini destekler. Bunlar, müzik çalarlar ve medya yazılımları tarafından kullanılan en yaygın çalma listesi standartlarını kapsar.
{{% /details %}}

{{% details title="Bulut depolamadan çalma listeleri içe aktarabilir miyim?" closed="true" %}}
Evet. Google Drive, Dropbox, OneDrive ve WebDAV sunucuları dahil olmak üzere bağlı herhangi bir bulut depolama hizmetinden çalma listesi dosyalarını içe aktarabilirsiniz.
{{% /details %}}

{{% details title="İçe aktarma sonrasında neden bazı parçalar eksik?" closed="true" %}}
Çalma listesi dosyası, medya dosyalarınıza doğru yollar içermelidir ve bu dosyalar depolamanızda belirtilen konumlarda bulunmalıdır. M3U veya CUE dosyanızdaki dosya yollarının gerçek dosya konumlarıyla eşleştiğini tekrar kontrol edin.
{{% /details %}}

{{% details title="Birden fazla çalma listesini aynı anda içe aktarabilir miyim?" closed="true" %}}
Evet. Daha fazla eylem düğmesini kullanın ve "Bir Klasörden Çalma Listeleri İçe Aktar" seçeneğini seçin. Uygulama, desteklenen tüm çalma listesi dosyaları için klasörü tarar ve tek adımda içe aktarır.
{{% /details %}}

{{% details title="Çalma listelerini manuel olarak oluşturmam gerekiyor mu?" closed="true" %}}
Hayır. İçe aktarma özelliği, manuel çalma listesi oluşturma ihtiyacını ortadan kaldırır. Uygulamayı mevcut M3U, M3U8 veya CUE dosyanıza yönlendirmeniz yeterlidir; çalma listesini otomatik olarak oluşturur.
{{% /details %}}
