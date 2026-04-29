---
title: "Evermusic ve Flacbox'ta Parça Koleksiyonunu M3U, CSV ve TXT Olarak Dışa Aktarma"
date: 2024-01-31
description: "Evermusic ve Flacbox'taki sonlar, favoriler, çalma listeleri ve albümlerinizi M3U, CSV veya TXT formatlarına nasıl dışa aktaracağınızı öğrenin. Last.fm scrobbling ve diğer cihazlarda çalma için idealdir."
keywords: ["evermusic dışa aktarma", "flacbox dışa aktarma", "m3u dışa aktarma", "çalma listesini csv olarak dışa aktarma", "m3u txt csv çalma listesi", "müzik dışa aktarma"]
tags: ["evermusic", "recents", "favorites", "export", "m3u", "playlist", "csv", "txt", "album"]
---

{{< author-byline >}}


**Özet:** Evermusic ve Flacbox, herhangi bir parça koleksiyonunu (sonlar, favoriler, çalma listeleri, albümler) CSV, TXT veya M3U dosyalarına dışa aktarmanıza olanak tanır. Bu dışa aktarmaları Last.fm'e scrobble yapmak, kütüphanenizi yedeklemek veya çalma listelerinizi diğer cihazlarda dinlemek için kullanabilirsiniz.

## Giriş

Uygulamadan sonlar, favoriler, albümler ve çalma listelerinizi harici bir dosyaya dışa aktarmak son derece faydalı olabilir. Bu dosyaları [Last.fm](http://Last.fm) gibi scrobbler hizmetlerinde dinleme geçmişinizi güncellemek veya çalma listelerinizi harici cihazlarda dinlemek için kullanabilirsiniz. Evermusic ve Flacbox ile bu işlem çok kolaydır. Burada, sonlarınızı CSV/TXT formatına ve çalma listelerinizi M3U formatına nasıl dışa aktaracağınızı göstereceğiz. Ancak bu işlevsellik uygulama içindeki herhangi bir parça koleksiyonu için kullanılabilir.

## Format Seçin

Sonlarınızı dışa aktarmak için 'Müzik kütüphanesi' bölümünü açın ve 'Sonlar' menü öğesini seçin.

![müzik kütüphanesi](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Sonraki ekranda sağ üst köşedeki 'Daha Fazla' düğmesine dokunun ve 'Şarkı listesini dışa aktar' seçeneğini seçin.

![sonları dışa aktar](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

'Dosya formatı seçin' ekranında birkaç seçeneğiniz var - CSV, TXT, M3U.

- CSV

Bu, Virgülle Ayrılmış Değerler anlamına gelir ve verilerinizi düzenli bir tablo formatına organize etmek için mükemmeldir. Hedef dosyada Sanatçı Adı, Albüm Adı, Parça Adı, Zaman Damgası (parçaları dinlediğiniz zaman), Albüm Sanatçısı Adı ve Parça Süresi gibi parametreleri bulacaksınız. Bu dosyayı daha sonra [burada](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/) açıklandığı gibi [Last.fm](http://Last.fm) gibi scrobbler hizmetlerinde dinleme geçmişinizi güncellemek için kullanabilirsiniz.

- TXT

Burada düz bir metin dosyasından bahsediyoruz. Basit ve anlaşılırdır, Sanatçı Adı, Albüm Adı, Parça Adı ve Süre parametrelerini içerir. Sadece metin sunumunda bir parça listesine ihtiyacınız varsa kullanışlıdır.

- M3U

Bu format, çalma listeleri oluşturmak için varsayılan standarttır. Harikadır çünkü şarkı listenizi dışa aktarabilir ve orijinal dosyalara sahip olmasanız bile (mutlak URL medya dosyaları seçeneğini seçerseniz) parçalarınızı herhangi bir cihazda dinleyebilirsiniz. Çıktı dosyasında Süre, Sanatçı Adı, Parça Adı ve Medya Dosyası Konumu gibi parametreleri bulacaksınız.

## CSV Formatı

Şimdi CSV'yi seçelim ve ne alacağımızı görelim. CSV'yi seçip 'Dışa Aktar' düğmesine basmanız yeterlidir.

![dosya formatı seçin](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Dışa aktarma tamamlandığında, iki seçenekli bir uyarı göreceksiniz. 'Dosyayı göster' seçeneğine dokunmak, sonuç dosyasını belgeler dizininizde gösterecektir.

![dışa aktarma tamamlandı](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Artık bu dosyayı gönderebilir, harici bir metin düzenleyicide açabilir veya [Last.fm](http://Last.fm) üzerindeki dinleme ilerlemenizi güncellemek için kullanabilirsiniz.

![sonuç dosyalarının bulunduğu dışa aktarma klasörü](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

Çıktı CSV dosyası aşağıdaki formatta alanlar içerecektir:

```
{SANATCI_ADI},{ALBUM_ADI},{PARCA_ADI},{ZAMAN_DAMGASI yyyy-MM-dd HH:mm:ss},{ALBUM_SANATCISI_ADI},{PARCA_SURESI HH:mm:ss}
```

Örneğin:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![dışa aktarılmış csv dosyası](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## TXT Formatı

Çıktı TXT dosyası aşağıdaki formatta alanlar içerecektir:

```
{SIRA_NUMARASI}. {SANATCI_ADI} - {ALBUM_ADI} - {PARCA_ADI} (SURE HH:mm:ss)
```

Örneğin:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![dışa aktarılmış txt dosyası](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## M3U Formatı

Şimdi, çalma listesi dosyaları için fiili standart olan M3U formatına çalma listenizi dışa aktarma konusunda size rehberlik edeceğiz. Başarılı çalma listesi dışa aktarımının ana ön koşulu, çalma listesindeki tüm dosyaların aynı depolama alanında bulunması gerektiğidir; ister Google Drive gibi bir bulut hizmetinde, ister yerel dosyalarda veya cihazınızdaki dosyalarda olsun. Dışa aktarma işlemini başlatmak için herhangi bir çalma listesini açın ve sağ üst köşedeki 'Daha Fazla' düğmesine dokunun, ardından 'Şarkı listesini dışa aktar' menü öğesini seçin.

![çalma listesi ekranı](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Sonraki ekranda, 'Medya dosyası konum türü' için iki seçenekle karşılaşacağınız 'M3U' dosya formatını seçin:

![dışa aktarma dosya formatı seçim ekranı](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. 'Göreceli yol' seçerseniz, çalma listesi medya dosyası konumları çalma listesi dosyasına göre göreceli olarak yazılır. Örneğin:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   Bu durumda, dışa aktarma tamamlandıktan sonra M3U dosyasının konumunu değiştirmekten kaçının, aksi takdirde medya dosyalarının yolları bozulur. Çalma listenizin çalınmasına başlamak için dışa aktarılan çalma listesi dosyasına dokunmanız yeterlidir; uygulama depolama alanınızdaki medya dosyalarını otomatik olarak bulacak ve çalmaya başlayacaktır. Hatta çalma listelerinizi depolama alanına dışa aktarabilir ve ardından yeni cihazınıza tekrar içe aktarabilirsiniz.

2. 'Mutlak URL' seçerseniz, uygulama medya dosyalarınız için doğrudan URL'ler oluşturacaktır. Bu, çalma listesini herhangi bir cihazda/uygulamada tüm medya dosyalarının çalma listesi dosyasıyla aynı depolama alanında bulunmasına gerek kalmadan çalmanıza olanak tanır. Bu seçenek yalnızca doğrudan dosya URL'leri oluşturabilen bulut depolama hizmetleri için desteklenir. Ancak bazı durumlarda, oluşturulan URL'lerin sınırlı bir ömrü olabileceğini ve bir süre sonra geçerliliğini yitirebileceğini unutmayın. Desteklenen bulut hizmetlerinin listesi: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (konuk modunda)  

Çıktı medya dosyası URL'si şöyle bir şey olacaktır:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

'Medya dosyası konum türü'nü seçtikten sonra 'Dışa Aktar' düğmesine dokunun. Uygulama, M3U dosyasını dışa aktarmak için bir hedef klasör seçmenizi isteyecektir. Seçiminizi onaylamak için 'Tamamlandı' düğmesine dokunun.

![klasör seçin](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Uygulama bir M3U dosyası oluşturacak ve hedef klasöre yükleyecek/taşıyacaktır.

![m3u dosyası yükleniyor](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Dışa aktarma tamamlandığında, 'Dosyayı göster' seçeneğiyle bir sistem uyarısı görünecektir.

![dışa aktarma tamamlandı uyarısı](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Buna dokunmak, dışa aktarılan dosyayı uygulamada gösterecektir.

![dosya listesinde dışa aktarılmış m3u dosyası](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Önceki adımda 'Medya dosyası konum türü' olarak 'Göreceli yol' seçtiyseniz, çıktı dosyası aşağıdaki formatta olacaktır:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![göreceli yollu m3u örneği](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

'Mutlak URL' seçeneği için uygulama şu formatta bir M3U dosyası oluşturacaktır:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![mutlak dosya url'li m3u örneği](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Bu dosyayı M3U çalma listelerini destekleyen herhangi bir cihazda/uygulamada açabilirsiniz.

![harici uygulamada açılan m3u çalma listesi](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Son Düşünceler

Parçalarınızı Evermusic ve Flacbox'tan dışa aktarmak, müzik verileriniz üzerinde tam kontrol sağlar. İster dinleme geçmişinizi yedekleyin, ister Last.fm'e scrobble yapın, ister çalma listelerinizi harici cihazlarda dinleyin; M3U, CSV ve TXT dışa aktarma seçenekleri esneklik ve uyumluluk için tasarlanmış güçlü araçlardır. Müzik koleksiyonunuzu platformlar arasında düzenleme, paylaşma ve yeniden ziyaret etme şeklinizi geliştirmek için bu özelliklerden yararlanın.

## SSS

{{% details title="Last.fm scrobbling için hangi dışa aktarma formatını kullanmalıyım?" closed="true" %}}
CSV kullanın. Last.fm-Scrubbler-WPF gibi scrobbling araçlarının gerektirdiği zaman damgalarını ve tam meta verileri içerir.
{{% /details %}}

{{% details title="Sadece çalma listeleri değil, herhangi bir parça koleksiyonunu dışa aktarabilir miyim?" closed="true" %}}
Evet. Aynı adımları kullanarak uygulamadaki sonları, favorileri, albümleri, çalma listelerini ve diğer herhangi bir parça koleksiyonunu dışa aktarabilirsiniz.
{{% /details %}}

{{% details title="M3U çalma listem diğer cihazlarda çalışır mı?" closed="true" %}}
Dışa aktarma sırasında Mutlak URL seçeneğini seçerseniz, M3U dosyası M3U çalma listelerini destekleyen herhangi bir cihazda çalınabilir. Bazı bulut URL'lerinin zamanla süresinin dolabileceğini unutmayın.
{{% /details %}}

{{% details title="Dışa aktarma özelliği ücretsiz mi?" closed="true" %}}
Evet. Parça koleksiyonlarını M3U, CSV ve TXT olarak dışa aktarma, Evermusic ve Flacbox'ın hem ücretsiz hem de premium sürümlerinde mevcuttur.
{{% /details %}}

{{% details title="Hangi bulut hizmetleri Mutlak URL dışa aktarmayı destekler?" closed="true" %}}
Mutlak URL dışa aktarma; iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive ve WebDAV (konuk modu) için desteklenir.
{{% /details %}}
