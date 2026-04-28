---
title: "Kodi DLNA sunucusu kullanarak Mac / PC / Linux / NAS'tan iPhone'da müzik nasıl çalınır"
date: 2025-07-25
description: "Kodi DLNA ve Evermusic uygulamasını kullanarak Wi-Fi üzerinden bilgisayarınızdan veya NAS'tan iPhone'a müzik yayınlayın."
keywords: ["kodi dlna sunucusu", "iphonea müzik yayınlama", "nastan müzik çalma", "evermusic dlna", "mactan iphonea müzik", "windowstan iphonea müzik", "kodi dlna iphone", "dlna ses yayını"]
tags: ["dlna", "kodi", "evermusic", "iphone", "müzik yayını", "mac", "nas", "linux", "yerel ağ"]
readingTime: 5
---

{{< author-byline >}}

**TL;DR:** Mac, PC, Linux veya NAS'ınıza Kodi yükleyin, DLNA/UPnP sunucusunu etkinleştirin ve ücretsiz Evermusic veya Flacbox uygulamasını kullanarak Wi-Fi üzerinden tüm müzik kitaplığınızı iPhone veya iPad'e yayınlayın. Abonelik gerekmez.

## Giriş

**Mac, Windows PC, Linux makinesi veya NAS cihazınız** varsa, ücretsiz ve açık kaynaklı bir medya platformu olan [Kodi](https://kodi.tv/) kullanarak evde kolayca **kişisel müzik sunucusuna** dönüştürebilirsiniz. Kodi'nin yerleşik **DLNA/UPnP sunucusu** ile tüm müzik kitaplığınızı herhangi bir DLNA uyumlu istemciye — iPhone veya iPad dahil — yayınlayabilirsiniz.

Bu kılavuzda adım adım şunları göstereceğiz:

- Mac veya PC'ye Kodi yükleme
- Paylaşım için müzik klasörlerini ayarlama
- DLNA müzik sunucusunu etkinleştirme
- **Evermusic** veya **Flacbox** iOS uygulamasıyla müziğe erişme

Bu kurulum %100 ücretsizdir — abonelik yok, sadece kendi müziğiniz Wi-Fi ağınız üzerinden yayınlanır.

## Mac / PC / Linux / NAS'ınıza Kodi'yi indirin ve kurun

Önce Kodi'nin resmi web sitesini ziyaret edin:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Kodi ana sayfası" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

**İndirmeler**'e tıklayın ve bilgisayarınız için sürümü bulmak üzere aşağı kaydırın.
İşletim sisteminizi seçin. Bu örnekte **macOS** kullanacağız.

{{< cards cols="1">}}
{{< card subtitle="Kodi indirme sayfası" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Intel Mac'iniz varsa **Intel (x86/64)**'e veya M1, M2, M3 Mac için **Apple Silicon**'a tıklayarak indirmeyi başlatın.

{{< cards cols="1">}}
{{< card subtitle="macOS yükleyicisini seçin" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Yükleyici indirilirken lütfen bir an bekleyin.

{{< cards cols="1">}}
{{< card subtitle="Kodi indirildi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

İndirdikten sonra **İndirilenler** klasöründe `.dmg` dosyasını bulun.

{{< cards cols="1">}}
{{< card subtitle="Kodi'yi yükleyin" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Yükleyiciyi başlatmak için indirilen dosyaya çift tıklayın.
Kodi'yi yüklemek için **Uygulamalar** klasörüne sürükleyin.

{{< cards cols="1">}}
{{< card title="" subtitle="Kodi'yi Uygulamalar'a sürükleyerek yükleyin" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Kodi'yi başlatın. **Sistem Tercihleri → Güvenlik ve Gizlilik → Yine de Aç** bölümünde izin vermeniz gerekebilir.

{{< cards cols="1">}}
{{< card subtitle="Kodi ana ekranı" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Kodi kitaplığına müzik ekleyin

Ana ekrandan **dişli simgesine** (Ayarlar) tıklayın.

{{< cards cols="1">}}
{{< card subtitle="Kodi ayarları" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

**Medya Ayarları → Kitaplık**'a gidin. Otomatik indeksleme için video ve müzik kitaplığı için **Başlangıçta kitaplığı güncelle**'yi etkinleştirin.

{{< cards cols="1">}}
{{< card subtitle="Kitaplık ayarları" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Ardından **Müzik** bölümüne gidin ve **Müzik Ekle**'ye tıklayın.

{{< cards cols="1">}}
{{< card subtitle="Müzik klasörü ekle" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Müziğinizin depolandığı klasörü bulun ve seçin.

{{< cards cols="1">}}
{{< card subtitle="Müzik kaynağı seçin" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Müzik kaynağını Kodi'ye ekleyin.

{{< cards cols="1">}}
{{< card subtitle="Müzik kaynağı ekle" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Onaylayın ve Kodi'nin müzik kitaplığınızı taramasına izin verin.

{{< cards cols="1">}}
{{< card subtitle="Müzik kaynaklarını onaylayın" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Kitaplığınız taranıp tamamen oluşturulurken bir an bekleyin.

{{< cards cols="1">}}
{{< card subtitle="Müzik kitaplığı taranıyor" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Kodi DLNA sunucusunu etkinleştirin

**Ayarlar → Hizmetler → UPnP/DLNA**'ya gidin.

Seçeneği etkinleştirin: **Kitaplıklarımı paylaş**.

Kodi artık yerel Wi-Fi ağınızda bir DLNA sunucusu olarak çalışıyor.

{{< cards cols="1">}}
{{< card subtitle="Kodi'de DLNA'yı etkinleştirin" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Kodi kitaplığını açın

Ayarlar penceresini kapatmak ve Kodi ana kitaplığını açmak için sağ tıklayın.

{{< cards cols="1">}}
{{< card title="" subtitle="Kodi kitaplığına erişmek için sağ tıklayın" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## iOS için müzik yayın uygulaması indirin

Çeşitli bulut depolama hizmetlerinden ve DLNA sunucularından müzik yayınlamanıza olanak tanıyan ücretsiz bir iOS DLNA istemci uygulaması edinin.

- Koleksiyonunuz ağırlıklı olarak MP3 ve diğer standart ses formatlarıysa **Evermusic** kullanın.
- FLAC, ALAC veya DSD gibi formatlarda hi-res müzik kitaplığınız varsa **Flacbox** seçin.

Her iki uygulama da **iOS** ve **macOS** için mevcuttur ve ücretsizdir.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Evermusic İndir" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Flacbox İndir" icon="download" tag="Free" >}}
{{< /cards >}}

## DLNA kaynağı ekleyin

iOS uygulamasını indirdikten sonra **Tüm Bağlantılar** bölümünü açın.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic uygulaması ana kenar çubuğu" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Aşağı kaydırın ve DLNA sunucularını keşfetmek için **Yerel Ağ - Mevcut cihazlar**'a dokunun.
Bu bölümde yerel ağınızdaki tüm mevcut cihazları göreceksiniz. **Kodi DLNA sunucunuz** burada görünmelidir. Bağlanmak için Kodi sunucusuna dokunun.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic'te mevcut DLNA cihazları" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic, Kodi aracılığıyla paylaşılan kitaplık klasörlerini görüntüler.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic'te Kodi müzik kitaplığı" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

DLNA sunucunuzdaki tüm mevcut ses dosyalarını görüntülemek için **Şarkılar** klasörüne gidin.

{{< cards cols="1">}}
{{< card title="" subtitle="Uzak klasörden listelenen şarkılar" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Anında yayın başlatmak için herhangi bir ses dosyasına dokunun.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic'te MP3 dosyası çalınıyor" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

**Bağlantılar** bölümüne geri dönün. Eklenen DLNA sunucusu artık burada görünecektir. İstediğiniz zaman yeniden bağlanmak için simgesine dokunun.

Burada **Last.fm takibi**'ni de etkinleştirebilirsiniz. Çalma istatistikleri Last.fm hesabınıza kaydedilir.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic'te bağlantılar" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Müzik kitaplığı oluşturun

Hem **Evermusic** hem de **Flacbox** kitaplığınıza müzik eklemenize ve sanatçılar, albümler, türler ve besteciler gibi **meta veri etiketleriyle** düzenlemenize olanak tanır.

Başlamak için **Müzik Kitaplığı** bölümünü açın. **Araçlar ve tercihler**'e kaydırın ve **Müzik Ekle**'ye dokunun.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic müzik kitaplığı" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Müzik kaynağını seçin — bu durumda **Bağlantılar**'ı seçin.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic'te yeni müzik ekle" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Bağlantılarda **Kodi DLNA sunucusunu** bulun ve klasörleri ve dosyaları görüntülemek için dokunun.

{{< cards cols="1">}}
{{< card title="" subtitle="Müzik içe aktarma için DLNA sunucusu seçin" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Eklemek istediğiniz klasörleri veya dosyaları seçin ve **Tamamlandı**'ya dokunun.

{{< cards cols="1">}}
{{< card title="" subtitle="Eklenecek müzik klasörünü seçin" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Uygulama seçilen dosyalarınızı tarayacak ve meta veriler kullanarak Sanatçılar, Albümler, Türler ve Besteciler gibi bölümlere ayıracaktır.

{{< cards cols="1">}}
{{< card title="" subtitle="Kategorili müzik kitaplığı" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Çalma listeleri oluşturun

Kendi çalma listelerinizi de oluşturabilirsiniz.

Önce **Çalma Listeleri** sekmesini açın.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic'te Çalma Listeleri sekmesi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

**Artı (+)** düğmesine dokunun ve **Yeni Çalma Listesi**'ni seçin.

{{< cards cols="1">}}
{{< card title="" subtitle="Yeni çalma listesi oluşturun" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Çalma listeniz için bir ad girin ve **Kaydet**'e dokunun.

{{< cards cols="1">}}
{{< card title="" subtitle="Çalma listesi adını girin" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Ardından şarkı eklemek için bir kaynak seçin — burada **Kitaplık**'ı seçiyoruz.

{{< cards cols="1">}}
{{< card title="" subtitle="Yeni çalma listesine şarkı ekleyin" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

İstediğiniz şarkıları seçin ve eklemek için **Tamamlandı**'ya dokunun.

{{< cards cols="1">}}
{{< card title="" subtitle="Kitaplıktan çalma listesine müzik ekleyin" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Seçilen parçalar artık oluşturulan çalma listesinde görünecektir.

{{< cards cols="1">}}
{{< card title="" subtitle="Oluşturulan çalma listesi listede gösterildi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Varsayılan olarak şarkılar yayın için mevcuttur. Çevrimdışı dinlemek için **Çevrimdışı modu** etkinleştirin — uygulama tüm çalma listesi parçalarını indirecektir.

{{< cards cols="1">}}
{{< card title="" subtitle="Çalma listesi için çevrimdışı mod etkin" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Ek seçenekleri keşfetmek için **Daha fazla eylem** düğmesine dokunun. Şunları yapabilirsiniz:

- Çalma listesini arşivleyin
- Albüm kapağını değiştirin
- Parçaları yeniden sıralayın
- Ve daha fazla yararlı özellik

{{< cards cols="1">}}
{{< card title="" subtitle="Daha fazla çalma listesi eylemi mevcut" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Sonuç

**Evermusic** ve **Flacbox** ile iPhone, iPad veya Mac'inizi güçlü bir DLNA müzik çalara dönüştürmek kolaydır.

- **Kodi DLNA sunucunuzdan** doğrudan MP3 veya hi-res FLAC yayınlayın
- Meta verilere göre gruplandırılmış kişisel müzik kitaplığı oluşturun (albümler, türler, besteciler)
- **Özel çalma listeleri** oluşturun ve yönetin
- Hareket halindeyken dinlemek için **çevrimdışı modu** etkinleştirin
- **Birden fazla bulut hizmetine** ve **yerel ağ cihazlarına** bağlanın
- Dinleme alışkanlıklarınızı **Last.fm entegrasyonu** ile takip edin

İster bir ses tutkunusu ister sıradan bir dinleyici olun, Evermusic ve Flacbox sorunsuz müzik yayını ve organizasyon için ihtiyacınız olan her şeyi sunar.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Evermusic İndir" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Flacbox İndir" icon="download" tag="Free" >}}
{{< /cards >}}

Kişisel müzik deneyiminizi bugün oluşturmaya başlayın.

## Sık sorulan sorular

{{% details title="Kodi, DLNA sunucusu olarak ücretsiz mi?" closed="true" %}}
Evet. Kodi tamamen ücretsiz ve açık kaynaklıdır. macOS, Windows, Linux ve birçok NAS cihazında çalışır.
{{% /details %}}

{{% details title="Evermusic ve Flacbox, DLNA üzerinden FLAC yayınını destekliyor mu?" closed="true" %}}
Evet. Flacbox, FLAC, ALAC ve DSD gibi hi-res formatlar için optimize edilmiştir. Evermusic ayrıca MP3 ve diğer standart formatlarla birlikte FLAC oynatmayı destekler.
{{% /details %}}

{{% details title="Kodi'den yayın yaptıktan sonra çevrimdışı dinleyebilir miyim?" closed="true" %}}
Evet. Herhangi bir çalma listesinde Çevrimdışı Modu etkinleştirin ve uygulama tüm parçaları cihazınıza indirir.
{{% /details %}}

{{% details title="DLNA kullanmak için premium aboneliğe ihtiyacım var mı?" closed="true" %}}
Ücretsiz sürüm en fazla 3 bulut veya ağ bağlantısını destekler. Premium bu sınırı kaldırır.
{{% /details %}}

{{% details title="iPhone'umun Kodi ile aynı Wi-Fi ağında olması gerekiyor mu?" closed="true" %}}
Evet. DLNA yayını yerel ağınız üzerinden çalışır. Hem Kodi sunucusu hem de iOS cihazınız aynı Wi-Fi ağına bağlı olmalıdır.
{{% /details %}}

{{% details title="Bu kurulumu Mac veya PC yerine NAS ile kullanabilir miyim?" closed="true" %}}
Evet. Birçok NAS cihazı (Synology, QNAP vb.) Kodi'yi destekler veya kendi yerleşik DLNA sunucusuna sahiptir. Evermusic ve Flacbox herhangi bir standart DLNA/UPnP sunucusuna bağlanabilir.
{{% /details %}}
