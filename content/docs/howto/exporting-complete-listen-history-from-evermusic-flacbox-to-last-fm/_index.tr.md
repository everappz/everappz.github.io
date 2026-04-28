---
title: "Evermusic ve Flacbox'tan Last.fm'e Tam Dinleme Geçmişinizi Dışa Aktarın"
date: 2024-01-30
description: "Evermusic ve Flacbox'tan müzik geçmişinizi nasıl dışa aktaracağınızı ve CSV dosyaları ile Windows için Last.fm Scrubbler aracını kullanarak Last.fm'e nasıl yükleyeceğinizi öğrenin."
keywords: ["evermusic", "flacbox", "lastfm", "müzik geçmişi", "scrobbling", "parça dışa aktarma", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "sonlar", "lastfm", "dışa aktarma", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Özet:** Dinleme geçmişinizi Evermusic veya Flacbox'tan CSV dosyası olarak dışa aktarın, ardından Windows'taki ücretsiz Last.fm-Scrubbler-WPF aracını kullanarak Last.fm'e yükleyin. Otomatik scrobbling de her iki uygulamada yerel olarak mevcuttur.

**Güncelleme:** Otomatik scrobbling artık mevcut! Daha fazla bilgi için buraya bakın: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling, çalmakta olduğunuz şarkının başlığı ve sanatçısı gibi temel ayrıntıları otomatik olarak bir çevrimiçi hizmete kaydetmenin basit bir yoludur. Daha sonra dinleme geçmişinizi inceleyebilirsiniz.

[Last.fm](https://www.last.fm/home), Audioscrobbler adlı bir müzik öneri sistemi tarafından desteklenmektedir ve bu hizmeti ücretsiz olarak sunmaktadır. İnternet radyo istasyonlarından, bilgisayarınızdan veya çeşitli taşınabilir müzik cihazlarından dinlediğiniz parçaları kaydederek müzik zevkinizin ayrıntılı bir profilini oluşturur. Daha sonra web sitesini ziyaret ederek müzik zevkinize uyan yeni sanatçı veya albüm önerileri alabilirsiniz.

Dinleme geçmişinizi ücretsiz bir araç kullanarak Evermusic ve Flacbox uygulamalarından [Last.fm](http://Last.fm)'e yükleyebilirsiniz ve bunu nasıl yapacağınızı size göstereceğiz.

Uygulamanın 'Müzik Kütüphanesi' bölümünü açın ve 'Hızlı erişim' bölümüne kaydırın. 'Sonlar' menü öğesine dokunun.

![müzik kütüphanesi ekranı](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

'Sonlar' ekranında sağ üst köşedeki 'Daha fazla' düğmesine dokunarak 'Daha fazla eylem' menüsünü etkinleştirin. 'Şarkı listesini dışa aktar' menü öğesine dokunun.

![son çalınanlar ekranı](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

'Dosya formatını seçin' ekranında hedef dosyanın formatını seçme imkanınız vardır. Mevcut seçenekler - CSV, TXT, M3U.

![dosya formatı seçim ekranı](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Bu, Comma-Separated Values anlamına gelir ve verilerinizi düzenli bir tablo formatında organize etmek için mükemmeldir. Hedef dosyada Sanatçı Adı, Albüm Adı, Parça Adı, Zaman Damgası (parçaları dinlediğiniz zaman), Albüm Sanatçısı Adı ve Parça Süresi gibi parametreleri bulacaksınız.

TXT: Burada düz metin dosyasından bahsediyoruz. Basit ve anlaşılırdır; Sanatçı Adı, Albüm Adı, Parça Adı ve Süre gibi parametreleri içerir.

M3U: Bu format temelde çalma listeleri oluşturmak için birincil tercihtir. Harikadır çünkü şarkı listenizi dışa aktarabilir ve orijinal dosyalarınız olmasa bile herhangi bir cihazda parçalarınızın keyfini çıkarabilirsiniz (medya dosyaları için mutlak URL seçeneğini seçmeniz koşuluyla). Çıktı dosyasında Süre, Sanatçı Adı, Parça Adı ve Medya Dosyası Konumu gibi parametreleri bulacaksınız.

Görevimiz için CSV seçmek doğru yoldur. Bu dosyayı ücretsiz yazılım Last.fm-Scrubbler-WPF ile dinleme geçmişimizi [Last.fm](http://Last.fm) hizmetine yüklemek için kullanacağız. Basitçe CSV'yi seçin ve 'Dışa Aktar' düğmesine basın.

![dışa aktarma tamamlandı ekranı](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Dışa aktarma tamamlandıktan sonra 'Dosyayı göster' düğmesine dokunun, uygulama oluşturulan dosyayı belgeler klasörünüzde gösterecektir. Ardından dosya adının yanındaki 'Daha fazla eylem' düğmesine dokunun ve menüden 'Şurada aç' seçeneğini seçin. Bir sonraki adımımız dışa aktarılan dosyayı masaüstü bilgisayarınıza kopyalamaktır. 'Şurada aç' menüsünden AirDrop seçeneğini seçerek bunu kolayca yapabilirsiniz.

![dışa aktarılan dosya için daha fazla eylem](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Sırada, yalnızca Windows platformunda kullanılabilen ücretsiz açık kaynaklı bir [Last.FM](http://Last.FM) istemcisini kullanacağız. Bu istemci, az önce dışa aktardığımız CSV dosyasını kullanarak [Last.FM](http://Last.FM) üzerindeki dinleme geçmişinizi verimli bir şekilde güncellemenize olanak tanır.

Şu anda bir Windows bilgisayarı kullanmıyorsanız endişelenmeyin. Mac'inize VirtualBox yükleyerek ve resmi Windows geliştirme ortamı imaj dosyasını kullanarak bu istemciye erişebilirsiniz.

İşte yapmanız gerekenler:

- Aşağıdaki bağlantıdan VirtualBox'ı yükleyin: [VirtualBox İndir](https://www.virtualbox.org/wiki/Downloads)

- Bu bağlantıdan Windows geliştirme ortamını indirin ve yükleyin: [Windows Geliştirme Ortamı](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Windows bilgisayarınızda (veya Windows Development imajlı VirtualBox uygulamasında) [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF)'yi indirin ve yükleyin - GitHub'da mevcut olan ücretsiz açık kaynaklı yazılım. Sürüm 1.28 üzerinde test ettik, buradan indirebilirsiniz: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Last.fm-Scrubbler-WPF indirme sayfası](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

'Assets' bölümünde [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) dosyasına tıklayarak kurulum arşivini indirin. İndirilen dosyayı çıkartın ve çıkartılan klasörü açın.

- ÖNEMLİ

Bu uygulama hâlâ beta aşamasındadır. Uygulama geliştiricileri çok fazla test yapmamıştır. Önce bir test hesabına scrobble yapmayı denemenizi ve scrobble yapmak istediğiniz şeylerin doğru çalışıp çalışmadığını kontrol etmenizi önerirler. Özellikle bir seferde çok sayıda parça scrobble ediyorsanız. Lütfen hesaplarınız konusunda dikkatli olun.

Last.fm-Scrubbler-WPF.exe'yi çalıştırın

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Uygulamanın ana ekranında sol alt köşede bulunan 'Giriş yapılmadı' seçeneğine dokunarak 'Hesap ekle' ekranını etkinleştirin.

![Hesap ekle ekranı](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Giriş bilgilerinizi girin.

![giriş bilgileri ekranı](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Hesabınızı eklemek için 'Login' düğmesine dokunun.

![Hesabınızı eklemek için Login düğmesine dokunun.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Evermusic uygulamasından CSV dosyasını içe aktarmaya başlamak için 'File Parse Scrobbler' sekmesini açın.

![Evermusic uygulamasından CSV dosyasını içe aktarmaya başlamak için File Parse Scrobbler sekmesini açın.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

'Parser: CSV' seçin ve 'Settings' düğmesine dokunun.

Bir sonraki ekranda CSV dosyanızdaki parametrelerin sırasını seçebilirsiniz.

Bireysel alanlar tırnak işaretleriyle çevrelenebilir ve alan belirlenen ayırıcılardan herhangi birini içeriyorsa tırnak işaretleriyle çevrelenmesi GEREKİR. Örneğin:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Bu nedenle tüm ayarları varsayılan olarak bırakın; değiştirmeniz gereken tek şey 'Has Fields Enclosed In Quotes' alanındaki onay kutusunu etkinleştirmektir.

Değişiklikleri uygulamak için 'Save & Close' düğmesine dokunun.

![CSV dosyanızdaki parametrelerin sırasını seçin.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Dosya ayrıştırma scrobbling'in iki modu vardır. 'Scrobbling Mode' ComboBox'u ile değiştirilebilirler.

Normal Mod: Bu modda parçalar, ayrıştırılan scrobble'ın zaman damgasıyla scrobble edilir. Yalnızca 14 günden yeni scrobble'lar scrobble edilebilir.

İçe Aktarma Modu: Bu modda parçalar, 'Finish Time' ve her parça arasında seçilen süre kullanılarak hesaplanan zaman damgasıyla scrobble edilir. Bu, ayrıştırılan scrobble'ın zaman damgası 14 günden eski olsa bile parçaların scrobble edilmesini sağlar. Bu nedenle CSV dosyasındaki ilk (en üstteki) parça 'Finish Time' ile scrobble edilecektir.

Evermusic uygulamasından daha önce oluşturulan CSV dosyasını 'File:' alanında seçin ve 'Parse' düğmesine dokunun. Bazı durumlarda bazı scrobble'ların ayrıştırılamadığını bildiren bir hata uyarısı görebilirsiniz. Sanatçı Adı gibi tam meta verisi olmayan bazı parçalarınız varsa bu normaldir.

![bazı scrobble'lar ayrıştırılamadı](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Ayrıştırılan tüm parçaları seçmek için 'Check All' düğmesine dokunun.

![Ayrıştırılan tüm parçaları seçmek için Check All düğmesine dokunun.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Sunucuya gönderilecek tüm değişiklikleri kontrol etmek için 'Preview' düğmesine dokunun.

![Sunucuya gönderilecek tüm değişiklikleri kontrol etmek için Preview düğmesine dokunun.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Tüm değişiklikleri sunucuya yüklemek için 'Scrobble' düğmesine dokunun.

![Tüm değişiklikleri sunucuya yüklemek için Scrobble düğmesine dokunun.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Daha önce Last.fm-Scrubbler-WPF'nin günlük scrobble sınırı yoktu. Bu artık değişti çünkü bazı kişiler Scrubbler'ı o kadar çok parça scrobble etmek için kullandılar ki Last.fm sayfası için sorunlara neden oldu. Scrobble sınırı şu anda günde 2800 scrobble'dır. Bundan fazlasını scrobble etmeye çalıştığınızda bir hata mesajı alırsınız. Bir 'scrobble kuyruğu' ekleme planları vardır, bu sayede 2800'den fazla parça scrobble etmeniz gerekiyorsa bunlar kuyruğa eklenir ve bir süre sonra otomatik olarak scrobble edilir. Kullanıcı seçim görünümünde kaç scrobble'ınızın kaldığını kontrol edebilirsiniz.

Tüm kayıtlar sunucuya başarıyla yüklendikten sonra uygulama penceresinin altında şunu onaylayan bir mesaj göreceksiniz: 'Successfully scrobbled selected tracks.'

![Successfully scrobbled selected tracks.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Artık [Last.fm](http://Last.fm) sayfasında profilinizi açabilir ve tüm değişiklikleri kontrol edebilirsiniz.

![Last.fm sayfasındaki profiliniz](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Sıkça Sorulan Sorular

{{% details title="CSV dosyalarını dışa aktarmadan otomatik olarak scrobble yapabilir miyim?" closed="true" %}}
Evet. Hem Evermusic hem de Flacbox artık otomatik Last.fm scrobbling'i desteklemektedir. Kılavuza bakın: [Last.fm'e Nasıl Scrobble Yapılır](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="CSV'mde 14 günden eski parçalar varsa ne olur?" closed="true" %}}
Last.fm-Scrubbler-WPF'de İçe Aktarma Modunu kullanın. Finish Time'dan zaman damgalarını yeniden hesaplar ve orijinal tarihlerine bakılmaksızın parçaları scrobble etmenizi sağlar.
{{% /details %}}

{{% details title="Windows bilgisayarım yok. Yine de Last.fm-Scrubbler kullanabilir miyim?" closed="true" %}}
Evet. Mac'inize VirtualBox yükleyin ve Microsoft'tan ücretsiz Windows Geliştirme Ortamı imajını indirin. Last.fm-Scrubbler-WPF'yi sanal makine içinde çalıştırın.
{{% /details %}}

{{% details title="Neden bazı scrobble'lar ayrıştırılmadı?" closed="true" %}}
Temel meta verileri eksik olan parçalar (sanatçı adı gibi) ayrıştırılamaz. Bu beklenen bir durumdur ve dosyadaki diğer parçaları etkilemez.
{{% /details %}}

{{% details title="Günlük scrobble sınırı var mı?" closed="true" %}}
Evet. Last.fm-Scrubbler-WPF günde en fazla 2.800 scrobble'a izin verir. Daha fazla scrobble yapmanız gerekiyorsa işlemi birkaç güne yayın.
{{% /details %}}
