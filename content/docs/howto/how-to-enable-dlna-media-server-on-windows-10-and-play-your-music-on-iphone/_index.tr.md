---
title: "Windows 10'da DLNA Medya Sunucusu Nasıl Etkinleştirilir ve iPhone'da Müziğinizi Nasıl Dinlersiniz"
date: 2019-11-26
description: "Windows 10'da DLNA sunucusunu etkinleştirin ve Evermusic uygulamasıyla müziğinizi iPhone'a aktarın. Adım adım kurulum kılavuzu dahil."
keywords: ["evermusic", "dlna", "windows 10", "iphone müzik akışı", "medya sunucusu", "yerel ağ", "upnp"]
tags: ["evermusic", "müzik", "bulut", "iphone", "depolama", "yerel", "nas", "windows", "wifi", "dinle", "ağ", "uzak", "ev", "çevrimiçi", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**Özet:** Windows 10'da yerleşik bir DLNA sunucusu bulunur. Ağ ve Paylaşım ayarlarında etkinleştirin, ardından iPhone'unuzdaki ücretsiz **Evermusic** uygulamasını kullanarak tüm müzik kitaplığınızı Wi-Fi üzerinden aktarın. Üçüncü taraf sunucu yazılımına gerek yok.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Ön Kapak" caption="Windows 10 ve Evermusic kullanarak iPhone'a DLNA müzik akışı" width="800" >}}

DLNA (Digital Living Network Alliance), ağınızdaki DLNA destekli cihazlar arasında müzik dahil çeşitli medya içeriklerini kolayca aktarmanızı sağlayan güçlü bir araçtır. İyi haber şu ki Windows 10 ve önceki sürümler yerleşik bir DLNA özelliğiyle gelir, bu da üçüncü taraf medya sunucularına olan ihtiyacı ortadan kaldırır. İşte Windows 10'da DLNA Medya Sunucusunu etkinleştirme ve iPhone'unuzda müzik akışının keyfini çıkarma yöntemi.

## Windows 10'da DLNA Medya Sunucusu Nasıl Etkinleştirilir

1. 'Başlat' düğmesine tıklayın.  
2. 'Ayarlar' simgesini seçin.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Sunucu Kurulumu" caption="Windows Ayarlarını açın" width="500" >}}

3. 'Windows Ayarları' ekranında 'Ağ ve İnternet'i seçin.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Windows Ayarları" caption="Ağ ve İnternet'i seçin" width="500" >}}

4. 'Ağ' altında 'Ağ ve Paylaşım Merkezi'ni seçin.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Paylaşım Merkezi" caption="Ağ ve Paylaşım Merkezi'ni açın" width="500" >}}

5. 'Ağ ve Paylaşım Merkezi' ekranında sol menüdeki 'Gelişmiş paylaşım ayarlarını değiştir'e tıklayın.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Gelişmiş Paylaşım Ayarları" caption="Gelişmiş paylaşım ayarlarını değiştir" width="500" >}}

6. 'Gelişmiş paylaşım ayarları' ekranında 'Tüm Ağlar' bölümüne kaydırın ve oku tıklayarak genişletin.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Keşfi Aç" caption="Tüm ağ ayarlarını genişlet" width="500" >}}

7. DLNA sunucusunu etkinleştirmek için 'Medya akışını aç'a tıklayın.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Sunucuyu Aç" caption="Medya akışı sunucusunu etkinleştir" width="500" >}}

8. Medya kitaplığınıza bir ad verin ve erişimine izin verilen cihazları seçin.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Medya Kitaplığı Adı" caption="DLNA medya kitaplığınızı adlandırın" width="500" >}}

9. Onaylamak için 'Tamam'a tıklayın. Artık Müzik, Resimler ve Videolar gibi kişisel klasörleriniz UPnP destekli tüm akış cihazlarına görünür olacak.

## Windows 10'da DLNA Medya Sunucusu Nasıl Devre Dışı Bırakılır

1. 'Başlat'a tıklayın ve arama alanına 'services' yazın.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Windows Hizmetleri" caption="Windows Hizmetlerini açın" width="500" >}}

2. 'Hizmetler' ekranında 'Windows Media Player Network Sharing Service'i bulmak için aşağı kaydırın.  
3. Üzerine çift tıklayın ve 'Başlangıç türü'nü 'El ile' olarak ayarlayın.  
4. 'Durdur' düğmesine tıklayarak hizmeti durdurun.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="DLNA Hizmetini Durdur" caption="DLNA ağ paylaşım hizmetini devre dışı bırak" width="500" >}}

## iPhone'da DLNA Sunucusundan Müzik Nasıl Dinlenir

1. App Store'dan ücretsiz **Evermusic** uygulamasını yükleyin:  
   [Evermusic Uygulaması](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. 'Bağlantılar' sekmesini açın ve 'Yerel Ağ' bölümündeki 'Kullanılabilir cihazlar'a dokunun.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Evermusic Bağlantıları" caption="Evermusic: Bağlantılar ekranı" width="500" >}}

3. Cihaz listesi yüklenirken birkaç saniye bekleyin ve Windows Media Player DLNA sunucusuna dokunun (örn. 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Kullanılabilir Cihazlar" caption="Evermusic'te kullanılabilir DLNA sunucuları" width="500" >}}

4. Medya sunucusunda bulunan klasörlerin listesini göreceksiniz.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Evermusic Klasörleri" caption="DLNA sunucusundan paylaşılan klasörleri gözat" width="500" >}}

5. Ses dosyaları içeren herhangi bir klasörü açın.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Klasör İçeriği" caption="Paylaşılan DLNA klasörlerinin içeriğini görüntüle" width="500" >}}

6. Ses oynatıcıyı başlatmak için herhangi bir dosyaya dokunun.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Ses Oynatıcı" caption="Evermusic'te DLNA'dan ses dosyası oynat" width="500" >}}

7. Ses deneyiminizi geliştirmek için ekranın alt kısmındaki ses göstergesi yakınındaki 'Ekolayzır' simgesine dokunarak ön amplifikatörlü iPod tarzı ekolayzırı etkinleştirin.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Ekolayzır" caption="Gelişmiş çalma için yerleşik ekolayzırı kullanın" width="500" >}}

## Sonuç

Windows 10'daki DLNA Medya Sunucusu ve iPhone'unuzdaki Evermusic ile bilgisayarınızdan mobil cihazınıza kesintisiz müzik akışının keyfini çıkarabilirsiniz. Depolama sınırlamalarına elveda, istek üzerine müziğe merhaba deyin!

## Sık Sorulan Sorular

{{% details title="Windows 10'a sunucu yazılımı yüklemem gerekiyor mu?" closed="true" %}}
Hayır. Windows 10 yerleşik bir DLNA medya sunucusu içerir. Yalnızca Ağ ve Paylaşım Merkezi ayarlarında medya akışını etkinleştirmeniz gerekir. Üçüncü taraf yazılım gerekmez.
{{% /details %}}

{{% details title="iPhone'umun aynı Wi-Fi ağında olması gerekiyor mu?" closed="true" %}}
Evet. DLNA akışı yerel ağınız üzerinden çalışır. Evermusic'in DLNA sunucusunu keşfedebilmesi için hem Windows 10 bilgisayarınız hem de iPhone'unuz aynı Wi-Fi ağına bağlı olmalıdır.
{{% /details %}}

{{% details title="DLNA üzerinden hangi ses formatlarını aktarabilirim?" closed="true" %}}
Windows DLNA sunucusu, formattan bağımsız olarak Müzik klasörünüzdeki dosyaları paylaşır. Evermusic MP3, FLAC, AAC, WAV, OGG, AIFF ve birçok başka formatı destekler, böylece sunucudan neredeyse her ses dosyasını çalabilirsiniz.
{{% /details %}}

{{% details title="Evermusic yerine Flacbox kullanabilir miyim?" closed="true" %}}
Evet. Flacbox da DLNA/UPnP göz atma ve çalmayı destekler. Windows DLNA sunucunuzdan müzik keşfetmek ve çalmak için her iki uygulamadan birini kullanabilirsiniz.
{{% /details %}}

{{% details title="DLNA akışı mobil veri kullanır mı?" closed="true" %}}
Hayır. DLNA tamamen yerel Wi-Fi ağınızda çalışır. Hiçbir mobil veri kullanmaz. Ancak çalma sırasında her iki cihazın da aynı ağa bağlı kalması gerekir.
{{% /details %}}
