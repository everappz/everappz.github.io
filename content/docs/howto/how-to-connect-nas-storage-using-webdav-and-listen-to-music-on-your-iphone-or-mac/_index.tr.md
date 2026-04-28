---
title: "WebDAV Kullanarak NAS Depolamayı Bağlama ve iPhone veya Mac'te Müzik Dinleme"
date: 2024-07-28
description: "Synology NAS'ınızda WebDAV'ı nasıl yapılandıracağınızı ve Evermusic veya Flacbox kullanarak iPhone veya Mac'inize müzik aktaracağınızı öğrenin. Adım adım kılavuzumuzu takip edin."
keywords: ["nas bağla", "webdav synology", "müzik akışı nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["müzik", "akış", "depolama", "nas", "bağlantı", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Özet:** Synology NAS'ınıza WebDAV'ı kurun ve etkinleştirin, paylaşılan klasör izinlerini yapılandırın, ardından NAS IP adresi ve WebDAV portu (varsayılan 5005/5006) kullanarak Evermusic veya Flacbox'tan bağlanın. Dosyaları cihazınıza kopyalamadan tüm müzik kitaplığınızı yayınlayabilir ve yönetebilirsiniz.

NAS depolamanızı WebDAV kullanarak nasıl bağlayacağınızı ve müzik kitaplığınızı iPhone veya Mac'inize zahmetsizce nasıl aktaracağınızı keşfedin. WebDAV (Web-based Distributed Authoring and Versioning), Internet üzerinden dosyaları yönetmenizi ve paylaşmanızı sağlayan bir protokoldür. NAS'ınızda WebDAV kurarak müzik koleksiyonunuza erişebilir ve yayınlayabilir, favori şarkılarınızın her zaman parmaklarınızın ucunda olmasını sağlayabilirsiniz.

Bu kılavuzda, en popüler NAS sunucularından biri olan Synology NAS'ta WebDAV bağlantısının nasıl kurulacağını göstereceğiz. Synology NAS'ınızda WebDAV'ı yapılandırmak için basit adımlarımızı izleyin ve müzik kitaplığınızı doğrudan iPhone veya Mac'inizden göz atabilir, yayınlayabilir ve yönetebilirsiniz.

## Adım 1: Synology NAS'a WebDAV Kurulumu

1. Synology NAS'ınıza giriş yapın ve **Paket Merkezi**'ni açın.
2. "webdav" arayın ve henüz kurulmamışsa WebDAV paketini kurun. Yapılandırmak için WebDAV sunucusunu açın.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Synology'ye WebDAV Kurulumu" width="600" >}}

## Adım 2: WebDAV Sunucusunu Yapılandırma

1. WebDAV ayarları sayfasında **HTTP'yi Etkinleştir**, **HTTPS'yi Etkinleştir**, **Anonim WebDAV'ı Etkinleştir** ve **DavDepthInfinity'yi Etkinleştir** kutucuklarını işaretleyin.
2. Değişiklikleri kaydetmek için **Uygula**'ya tıklayın. HTTP ve HTTPS bağlantıları için port numaralarını not edin, varsayılan olarak 5005 ve 5006'dır.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="WebDAV ayarlarını yapılandırma" width="600" >}}

## Adım 3: Paylaşılan Klasör İzinlerini Yapılandırma

1. **Denetim Masası**'nı açın ve **Paylaşılan Klasör** bölümüne gidin.
2. **Müzik** klasörünü seçin ve **Düzenle**'ye tıklayın.
3. **İzinler** sekmesinde izinleri yapılandırın. Sadece müzik dinlemeniz gerekiyorsa Salt Okunur ile misafir erişimini etkinleştirin veya dosyaları değiştirmeniz gerekiyorsa Okuma/Yazma ile etkinleştirin. Değişiklikleri kaydedin.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Paylaşılan Klasör İzinleri" width="600" >}}

## Adım 4: Synology NAS IP Adresini Bulma

1. **Denetim Masası**'nı açın ve **Ağ Arayüzü** sekmesine gidin veya web tarayıcınızı kullanarak [find.synology.com](http://find.synology.com) adresini ziyaret edin.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="NAS IP Adresini Bulma" width="600" >}}

2. Synology NAS'ınızın IP adresini not edin (örn. 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Synology NAS IP Adresi" width="600" >}}

## Adım 5: Evermusic/Flacbox ile Synology NAS'a Bağlanma

1. Evermusic veya Flacbox uygulamasını açın ve **Bağlantılar** sekmesine gidin.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Evermusic'te Bağlantılar Sekmesi" width="600" >}}

2. Otomatik bağlantı için **Mevcut cihazlar** bölümünde Synology NAS'ınızı bulun ve bağlanmak için dokunun.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Mevcut Cihazlar Listesi" width="600" >}}

3. Manuel bağlantı için **Bulut hizmetine bağlan**'ı seçin ve **WebDAV**'ı seçin. Sunucu adresini şu formatta girin: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (örn. [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Manuel WebDAV Yapılandırması" width="600" >}}

4. Misafir erişimi için kullanıcı adı ve şifre alanlarını boş bırakın veya Synology kimlik bilgilerinizi girin. **Giriş Yap**'a dokunun.

## Adım 6: Gezinme ve Müzik Çalma

1. Bağlandıktan sonra cihaz **Bağlı aksesuarlar** listesinde görünecektir.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Evermusic'te Bağlı Cihazlar" width="600" >}}

2. **Müzik** klasörüne gidin ve çalmaya başlamak için herhangi bir ses dosyasına dokunun.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Müzik Klasörünü Göz Atma" width="600" >}}

## Adım 7: Bağlı Bulut Klasörünü Müzik Kitaplığına Ekleme

1. Uygulamada **Müzik Kitaplığı** bölümünü açın.
2. **Müzik Ekle**'yi seçin ve **Bağlantılar**'ı seçin.
3. Bağlı NAS sunucunuzu seçin ve **Müzik** klasörünü seçin. **Tamamlandı**'ya dokunun.
4. Uygulama müzik klasörünü tarayacak ve desteklenen ses dosyalarını müzik kitaplığına ekleyecektir. Meta veriler yüklenecek ve parçalarınız albüm, sanatçı ve türe göre gruplandırılacaktır.

## Sonuç

Bu adımları izleyerek Synology NAS'ınızda kolayca bir WebDAV bağlantısı kurabilir ve Evermusic veya Flacbox kullanarak müzik kitaplığınızı iPhone veya Mac'inize yayınlayabilirsiniz. Favori parçalarınıza her zaman sorunsuz erişimin keyfini çıkarın.

## SSS

{{% details title="Hangi NAS cihazları WebDAV'ı destekler?" closed="true" %}}
Synology, QNAP, TrueNAS ve Western Digital dahil olmak üzere en popüler NAS markaları WebDAV'ı destekler. WebDAV kurulum talimatları için NAS üreticinizin belgelerini kontrol edin.
{{% /details %}}

{{% details title="NAS müzik akışı için WebDAV ve SMB arasındaki fark nedir?" closed="true" %}}
WebDAV HTTP/HTTPS üzerinden çalışır ve internet üzerinden uzaktan erişim için daha uygundur. SMB genellikle yerel ağlarda daha hızlıdır. Evermusic ve Flacbox her iki protokolü de destekler, bu nedenle yerel veya uzak erişime ihtiyacınız olup olmadığına göre seçim yapın.
{{% /details %}}

{{% details title="Synology'de WebDAV için kullanıcı adı ve şifreye ihtiyacım var mı?" closed="true" %}}
Hayır, anonim WebDAV erişimini etkinleştirir ve paylaşılan klasörünüzde misafir izinlerini yapılandırırsanız gerekli değildir. Daha iyi güvenlik için Synology kimlik bilgilerinizi kullanabilirsiniz.
{{% /details %}}

{{% details title="WebDAV üzerinden NAS'tan FLAC ve diğer yüksek çözünürlüklü formatları yayınlayabilir miyim?" closed="true" %}}
Evet. Hem Evermusic hem de Flacbox, WebDAV üzerinden NAS depolamadan yayın yaparken FLAC, ALAC, WAV, DSD ve diğer yüksek çözünürlüklü formatları destekler.
{{% /details %}}

{{% details title="Uygulama neden NAS'ımı Mevcut cihazlarda bulamıyor?" closed="true" %}}
iPhone/Mac'inizin ve NAS'ın aynı Wi-Fi ağında olduğundan emin olun. Otomatik keşif çalışmıyorsa, manuel bağlantı seçeneğini kullanın ve NAS IP adresini ve WebDAV portunu doğrudan girin.
{{% /details %}}
