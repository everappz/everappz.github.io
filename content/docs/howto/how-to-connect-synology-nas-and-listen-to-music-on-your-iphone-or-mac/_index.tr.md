---
title: "Synology NAS Nasıl Bağlanır ve iPhone veya Mac'inizde Müzik Nasıl Dinlenir"
date: 2024-09-19
description: "Synology NAS'ınızı yerel API veya QuickConnect kullanarak nasıl bağlayacağınızı ve Evermusic ve Flacbox ile iPhone veya Mac'inizde yüksek kaliteli müzik nasıl yayınlayacağınızı öğrenin."
keywords: ["synology nas", "müzik yayınlama", "quickconnect", "evermusic synology", "flacbox synology", "nas müzik çalar", "iphone nas müzik"]
tags: ["müzik", "yayın", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Özet:** Synology NAS'ınızı Synology'nin yerel API'si ile Evermusic veya Flacbox'a bağlayın -- IP adresi ile manuel olarak veya QuickConnect ID ile otomatik olarak. QuickConnect, port yönlendirme olmadan uzaktan müzik yayınlamanıza olanak tanır. Her iki uygulama da FLAC, MP3, WAV ve diğer yüksek çözünürlüklü formatları destekler.

Synology NAS'ınızı bağlamak ve iPhone veya Mac'inizde müzik kitaplığınızın keyfini çıkarmak için sorunsuz bir yol arıyorsanız, Evermusic ve Flacbox uygulamaları mükemmel çözümlerdir. Bu uygulamalar FLAC, MP3 ve WAV dahil geniş bir ses formatı yelpazesini destekleyerek Synology NAS'ınızdan doğrudan yüksek kaliteli müzik yayınlamayı ve dinlemeyi kolaylaştırır.

Bu kılavuzda, Synology'nin yerel API'si ve QuickConnect özelliğini kullanarak Synology NAS'ınızı Evermusic veya Flacbox uygulamasına nasıl bağlayacağınızı göstereceğiz. Synology'nin doğrudan API'sini kullanarak, WebDAV, SMB, DLNA gibi karmaşık yapılandırmalara ihtiyaç duymadan ev ağınızın dışında müzik kitaplığınıza güvenli bir şekilde erişebilirsiniz. QuickConnect ile iPhone veya Mac'inizi kullanarak her yerden müziğinizi yayınlayabilir ve yönetebilirsiniz.

## Adım 1: Paylaşılan Klasör İzinlerini Yapılandırın (İsteğe Bağlı)

1. **Denetim Masası**'nı açın ve **Paylaşılan Klasör** bölümüne gidin.

![Paylaşılan Klasör](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. **Music** klasörünü seçin ve **Düzenle**'ye tıklayın.

3. **İzinler** sekmesinde izinleri yapılandırın. Sadece müzik dinlemeniz gerekiyorsa Salt Okunur ile misafir erişimini etkinleştirin veya dosyaları değiştirmeniz gerekiyorsa Okuma/Yazma'yı etkinleştirin. Değişiklikleri kaydedin.

![İzinler](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Adım 2: Synology NAS IP Adresini Bulun

1. **Denetim Masası**'nı açın ve **Ağ Arayüzü** sekmesine gidin.

![Ağ Arayüzü](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Veya web tarayıcınızı kullanarak [find.synology.com](http://find.synology.com) adresini ziyaret edin.

![Synology Bul](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Synology NAS'ınızın IP adresini not edin (ör. 192.168.18.137).

## Adım 3: Synology NAS Ağ Portlarını Bulun

Varsayılan DSM ağ portları için resmi Synology belgelerini bu [Synology Bilgi Merkezi makalesinde](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services) bulabilirsiniz.

Synology DSM aşağıdaki varsayılan portları kullanır:
- **HTTP (Web Erişimi):** Port **5000**
- **HTTPS (Güvenli Web Erişimi):** Port **5001**

Bunlar DSM arayüzüne erişim için varsayılan portlardır.

![Ağ Portları](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Adım 4: QuickConnect ID Özelliğini Etkinleştirin

Synology QuickConnect ID, port yönlendirme gibi karmaşık ağ ayarlarını yapılandırmanıza gerek kalmadan internet üzerinden Synology NAS'ınıza uzaktan erişmenizi sağlayan benzersiz bir tanımlayıcıdır. QuickConnect, Synology'nin sunucularını kullanarak QuickConnect ID aracılığıyla NAS'ınız ile akıllı telefonunuz veya bilgisayarınız gibi cihazınız arasında bir bağlantı kurarak uzaktan erişimi basitleştirir.

**QuickConnect ID'nizi Nasıl Bulur veya Kurarsınız:**

1. **DSM'e giriş yapın.**
2. **Denetim Masası > Harici Erişim > QuickConnect**'e gidin.
3. **QuickConnect'i etkinleştirin** ve benzersiz QuickConnect ID'nizi oluşturun veya görüntüleyin.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Adım 5: Evermusic veya Flacbox Kullanarak iPhone/Mac'inizde Synology NAS'a Bağlanın

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) ve [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256), her biri müzik kitaplığınızı yönetmek ve keyfini çıkarmak için benzersiz özellikler ve yetenekler sunan iOS ve macOS cihazları için tasarlanmış müzik çalar uygulamalarıdır.

1. Evermusic veya Flacbox uygulamasını açın ve **Bağlantılar** sekmesine gidin.

![Bağlantılar](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. **Bulut hizmeti bağla**'yı seçin ve **Synology Drive**'ı seçin.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

İki bağlantı seçeneğiniz var: sunucunun IP adresi ve portunu kullanarak **manuel** veya QuickConnect ID ile **otomatik**.

### Manuel Bağlantı

Manuel yöntem için önceki adımlarda elde ettiğiniz doğrudan IP adresi ve port numarasına ihtiyacınız olacak.

1. Adım 2'de elde ettiğiniz sunucu URL'sini şu formatta girin: PROTOKOL://IP_ADRESİ:PORT_NUMARASI
   - HTTP için **port 5000** ve HTTPS bağlantıları için **port 5001** kullanın.

   Örneğin:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Gerçek port numarası kurulumunuzun 3. adımında doğrulanabilir.
3. Synology NAS için **kullanıcı adı** ve **şifrenizi** girin.
4. Bağlantıyı kurmak için **Giriş Yap**'a dokunun.

![Manuel Bağlantı](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Otomatik Bağlantı

Otomatik bağlantı için adım 4'teki **QuickConnect ID**'yi kullanacaksınız. Synology NAS'ınız için IP adresini ve port numarasını manuel olarak girmek yerine, sadece **QuickConnect ID**'yi girin. Uygulama gerekli bağlantı bilgilerini otomatik olarak alacaktır.

Bu yöntem, ev ağınızın dışında bile NAS'ınıza uzaktan erişmenize olanak tanır, böylece port yönlendirme veya statik IP adresleri yapılandırmanıza gerek kalmadan dosyalarınızı internetten yönetebilirsiniz.

![Otomatik Bağlantı](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## İki Faktörlü Kimlik Doğrulama

DSM 4.2'den itibaren Synology, güvenliği artırmak için **2 adımlı doğrulama** özelliğini tanıttı. Bu özellik, normal giriş bilgilerinize ek olarak bir doğrulama uygulaması tarafından oluşturulan **tek kullanımlık şifre (OTP)** kodunu gerektirir. 2 adımlı doğrulamayı etkinleştirdiyseniz, kullanıcı adı ve şifrenizi girdikten sonra DSM oturumunuza giriş yapmak için OTP'yi de girmeniz gerekir.

Lütfen dikkat edin, oturumunuz sona erdiğinde uygulamanın manuel olarak yeniden yetkilendirilmesi gerekecektir. Yeniden yetkilendirmek için:

1. Uygulamada **Bağlantılar** sekmesine gidin.
2. Sunucu adının yanındaki **Daha fazla eylem** düğmesine dokunun.
3. Yeni kimlik doğrulama kodunu girmek ve yeniden yetkilendirme işlemini tamamlamak için menüden **Ayarlar**'ı seçin.

Bu, güvenilmeyen bir ağdan NAS'ınıza erişseniz bile verilerinizin güvende kalmasını sağlar.

## Adım 6: Müzikte Gezinin ve Çalın

1. Bağlandıktan sonra cihaz **Bağlı Cihazlar** listesinde görünecektir.

![Bağlı Cihazlar](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. **Music** klasörüne gidin ve çalmaya başlamak için herhangi bir ses dosyasına dokunun.

![Müzik Çal](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Adım 7: Bağlı Bulut Klasörünü Müzik Kitaplığına Ekleyin

1. Uygulamada **Müzik Kitaplığı** bölümünü açın.
2. **Müzik Ekle**'yi seçin ve **Bağlantılar**'ı seçin.
3. Bağlı NAS sunucunuzu seçin ve **Music** klasörünü seçin. **Tamamlandı**'ya dokunun.
4. Uygulama müzik klasörünü tarayacak ve desteklenen ses dosyalarını müzik kitaplığına ekleyecektir. Meta veriler yüklenecek ve parçalarınız albüm, sanatçı ve türe göre gruplanacaktır.

## Sonuç

Bu adımları izleyerek Synology NAS'ınızda kolayca bir bağlantı kurabilir ve Evermusic veya Flacbox kullanarak tüm müzik kitaplığınızı iPhone veya Mac'inize yayınlayabilirsiniz. Evde veya hareket halinde olun, QuickConnect kullanarak her yerden en sevdiğiniz parçalara sorunsuz, yüksek kaliteli erişimin keyfini çıkarın. Bu uygulamaların sunduğu esneklik ve kolaylıktan yararlanın ve tüm cihazlarınızda müzik koleksiyonunuzu kolayca yönetmeye başlayın.

QuickConnect aracılığıyla güvenli uzaktan erişim ve geniş ses formatı desteği ile müziğinizden asla uzak olmayacaksınız. Artık NAS'ta depolanan dosyalarınız sadece bir dokunuş uzağınızda!

## FAQ

{{% details title="Manuel bağlantı ile QuickConnect arasındaki fark nedir?" closed="true" %}}
Manuel bağlantı, yerel ağınızda çalışan NAS IP adresi ve portunu kullanır. QuickConnect, port yönlendirme olmadan internet üzerinden her yerden bağlantı kurmak için Synology'nin aktarma hizmetini kullanır.
{{% /details %}}

{{% details title="Ev ağımın dışında Synology NAS'tan müzik yayınlayabilir miyim?" closed="true" %}}
Evet. Synology NAS'ınızda QuickConnect'i etkinleştirin ve internet bağlantısı olan her yerden müzik yayınlamak için Evermusic veya Flacbox'ta QuickConnect ID'yi kullanın.
{{% /details %}}

{{% details title="Synology NAS'tan yayın yaparken hangi ses formatları desteklenir?" closed="true" %}}
Evermusic ve Flacbox, FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD ve diğer birçok formatı destekler. Synology NAS'tan yayın yaparken tüm desteklenen formatlar çalışır.
{{% /details %}}

{{% details title="Bağlanmak için iki faktörlü kimlik doğrulama gerekiyor mu?" closed="true" %}}
Hayır, 2FA isteğe bağlıdır. Ancak Synology DSM'nizde 2 adımlı doğrulamayı etkinleştirdiyseniz, uygulama giriş sırasında tek kullanımlık şifre isteyecektir. Oturum sona erdiğinde yeniden yetkilendirmeniz gerekecektir.
{{% /details %}}

{{% details title="Bağlanmak için Synology yerel API, WebDAV veya SMB mi kullanmalıyım?" closed="true" %}}
QuickConnect ile Synology yerel API, uzaktan erişim için en iyi seçimdir. Yerel ağ kullanımı için SMB genellikle en hızlı seçenektir. WebDAV hem yerel hem de uzaktan erişim için iyi çalışır. Evermusic ve Flacbox üç protokolü de destekler.
{{% /details %}}
