---
title: "Cách phát nhạc từ Mac / PC / Linux / NAS trên iPhone bằng máy chủ Kodi DLNA"
date: 2025-07-25
description: "Phát nhạc từ máy tính hoặc NAS đến iPhone qua Wi-Fi bằng Kodi DLNA và ứng dụng Evermusic."
keywords: ["máy chủ kodi dlna", "phát nhạc đến iphone", "phát nhạc từ nas", "evermusic dlna", "nhạc từ mac đến iphone", "nhạc từ windows đến iphone", "kodi dlna iphone", "phát âm thanh dlna"]
tags: ["dlna", "kodi", "evermusic", "iphone", "phát nhạc trực tuyến", "mac", "nas", "linux", "mạng cục bộ"]
readingTime: 5
---

{{< author-byline >}}

**TL;DR:** Cài đặt Kodi trên Mac, PC, Linux hoặc NAS, bật máy chủ DLNA/UPnP và phát toàn bộ thư viện nhạc đến iPhone hoặc iPad bằng ứng dụng miễn phí Evermusic hoặc Flacbox qua Wi-Fi. Không cần đăng ký.

## Giới thiệu

Nếu bạn có **Mac, PC Windows, máy Linux hoặc thiết bị NAS**, bạn có thể dễ dàng biến nó thành **máy chủ nhạc cá nhân** tại nhà bằng [Kodi](https://kodi.tv/), nền tảng đa phương tiện miễn phí và mã nguồn mở. Với máy chủ **DLNA/UPnP** tích hợp của Kodi, bạn có thể phát toàn bộ thư viện nhạc đến bất kỳ thiết bị khách tương thích DLNA nào — bao gồm iPhone hoặc iPad của bạn.

Trong hướng dẫn này, chúng tôi sẽ chỉ cho bạn từng bước cách:

- Cài đặt Kodi trên Mac hoặc PC
- Thiết lập thư mục nhạc để chia sẻ
- Bật máy chủ nhạc DLNA
- Truy cập nhạc bằng ứng dụng **Evermusic** hoặc **Flacbox** cho iOS

Thiết lập này hoàn toàn miễn phí — không cần đăng ký, chỉ nhạc của bạn được phát qua mạng Wi-Fi.

## Tải xuống và cài đặt Kodi trên Mac / PC / Linux / NAS

Đầu tiên, truy cập trang web chính thức của Kodi:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Trang chủ Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Nhấp vào **Tải xuống** và cuộn để tìm phiên bản cho máy tính của bạn.
Chọn hệ điều hành của bạn. Trong ví dụ này, chúng tôi sẽ sử dụng **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Trang tải xuống Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Nhấp **Intel (x86/64)** nếu bạn có Mac Intel hoặc **Apple Silicon** cho M1, M2, M3 Mac để bắt đầu tải xuống.

{{< cards cols="1">}}
{{< card subtitle="Chọn trình cài đặt macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Vui lòng đợi một chút trong khi trình cài đặt tải xuống.

{{< cards cols="1">}}
{{< card subtitle="Đã tải xuống Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Sau khi tải xuống, tìm tệp `.dmg` trong thư mục **Tải xuống**.

{{< cards cols="1">}}
{{< card subtitle="Cài đặt Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Nhấp đúp vào tệp đã tải xuống để khởi chạy trình cài đặt.
Kéo Kodi vào thư mục **Ứng dụng** để cài đặt.

{{< cards cols="1">}}
{{< card title="" subtitle="Cài đặt Kodi bằng cách kéo vào Ứng dụng" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Khởi chạy Kodi. Bạn có thể cần cho phép nó trong **Tùy chọn Hệ thống → Bảo mật & Quyền riêng tư → Mở dù sao**.

{{< cards cols="1">}}
{{< card subtitle="Màn hình chính Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Thêm nhạc vào thư viện Kodi

Nhấp vào **biểu tượng bánh răng** (Cài đặt) từ màn hình chính.

{{< cards cols="1">}}
{{< card subtitle="Cài đặt Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Điều hướng đến **Cài đặt Phương tiện → Thư viện**. Bật **Cập nhật thư viện khi khởi động** cho thư viện video và nhạc để lập chỉ mục tự động.

{{< cards cols="1">}}
{{< card subtitle="Cài đặt thư viện" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Sau đó đi đến phần **Nhạc** và nhấp **Thêm Nhạc**.

{{< cards cols="1">}}
{{< card subtitle="Thêm thư mục nhạc" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Duyệt và chọn thư mục nơi lưu trữ nhạc của bạn.

{{< cards cols="1">}}
{{< card subtitle="Chọn nguồn nhạc" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Thêm nguồn nhạc vào Kodi.

{{< cards cols="1">}}
{{< card subtitle="Thêm nguồn nhạc" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Xác nhận và để Kodi quét thư viện nhạc của bạn.

{{< cards cols="1">}}
{{< card subtitle="Xác nhận nguồn nhạc" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Đợi một chút trong khi thư viện được quét và xây dựng hoàn chỉnh.

{{< cards cols="1">}}
{{< card subtitle="Đang quét thư viện nhạc" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Bật máy chủ DLNA của Kodi

Đi đến **Cài đặt → Dịch vụ → UPnP/DLNA**.

Bật tùy chọn: **Chia sẻ thư viện của tôi**.

Kodi giờ đây hoạt động như máy chủ DLNA trên mạng Wi-Fi cục bộ của bạn.

{{< cards cols="1">}}
{{< card subtitle="Bật DLNA trong Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Mở thư viện Kodi

Nhấp chuột phải để đóng cửa sổ cài đặt và mở thư viện chính Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Nhấp chuột phải để truy cập thư viện Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Tải xuống ứng dụng phát nhạc cho iOS

Tải ứng dụng DLNA miễn phí cho iOS cho phép bạn phát nhạc từ nhiều dịch vụ lưu trữ đám mây và máy chủ DLNA.

- Sử dụng **Evermusic** nếu bộ sưu tập của bạn chủ yếu là MP3 và các định dạng âm thanh tiêu chuẩn khác.
- Chọn **Flacbox** nếu bạn có thư viện nhạc hi-res ở các định dạng như FLAC, ALAC hoặc DSD.

Cả hai ứng dụng đều có sẵn cho **iOS** và **macOS**, và miễn phí.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Tải xuống Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Tải xuống Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Thêm nguồn DLNA

Sau khi tải xuống ứng dụng iOS, mở phần **Tất cả Kết nối**.

{{< cards cols="1">}}
{{< card title="" subtitle="Thanh bên chính của ứng dụng Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Cuộn xuống và nhấn **Mạng cục bộ - Thiết bị có sẵn** để khám phá máy chủ DLNA.
Trong phần này, bạn sẽ thấy tất cả các thiết bị có sẵn trên mạng cục bộ. **Máy chủ Kodi DLNA** của bạn sẽ xuất hiện ở đây. Nhấn vào máy chủ Kodi để kết nối.

{{< cards cols="1">}}
{{< card title="" subtitle="Thiết bị DLNA có sẵn trong Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic sẽ hiển thị các thư mục thư viện được chia sẻ qua Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Thư viện nhạc Kodi trong Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Điều hướng đến thư mục **Bài hát** để xem tất cả các tệp âm thanh có sẵn trên máy chủ DLNA.

{{< cards cols="1">}}
{{< card title="" subtitle="Bài hát từ thư mục từ xa" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Nhấn vào bất kỳ tệp âm thanh nào để bắt đầu phát ngay lập tức.

{{< cards cols="1">}}
{{< card title="" subtitle="Tệp MP3 đang phát trong Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Quay lại phần **Kết nối**. Máy chủ DLNA đã thêm sẽ xuất hiện ở đây. Nhấn biểu tượng để kết nối lại bất cứ lúc nào.

Bạn cũng có thể bật **theo dõi Last.fm** ở đây. Thống kê phát sẽ được lưu vào tài khoản Last.fm của bạn.

{{< cards cols="1">}}
{{< card title="" subtitle="Kết nối trong Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Xây dựng thư viện nhạc

Cả **Evermusic** và **Flacbox** đều cho phép bạn thêm nhạc vào thư viện và sắp xếp theo **thẻ siêu dữ liệu** như nghệ sĩ, album, thể loại và nhà soạn nhạc.

Để bắt đầu, mở phần **Thư viện Nhạc**. Cuộn xuống **Công cụ và tùy chọn** và nhấn **Thêm Nhạc**.

{{< cards cols="1">}}
{{< card title="" subtitle="Thư viện nhạc Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Chọn nguồn nhạc — trong trường hợp này, chọn **Kết nối**.

{{< cards cols="1">}}
{{< card title="" subtitle="Thêm nhạc mới trong Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Tìm **máy chủ Kodi DLNA** trong Kết nối và nhấn để xem thư mục và tệp.

{{< cards cols="1">}}
{{< card title="" subtitle="Chọn máy chủ DLNA để nhập nhạc" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Chọn thư mục hoặc tệp bạn muốn thêm và nhấn **Hoàn tất**.

{{< cards cols="1">}}
{{< card title="" subtitle="Chọn thư mục nhạc để thêm" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Ứng dụng sẽ quét các tệp đã chọn và sắp xếp bằng siêu dữ liệu thành các phần như Nghệ sĩ, Album, Thể loại và Nhà soạn nhạc.

{{< cards cols="1">}}
{{< card title="" subtitle="Thư viện nhạc với danh mục" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Tạo danh sách phát

Bạn cũng có thể tạo danh sách phát của riêng mình.

Đầu tiên, mở tab **Danh sách phát**.

{{< cards cols="1">}}
{{< card title="" subtitle="Tab Danh sách phát trong Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Nhấn nút **cộng (+)** và chọn **Danh sách phát mới**.

{{< cards cols="1">}}
{{< card title="" subtitle="Tạo danh sách phát mới" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Nhập tên cho danh sách phát và nhấn **Lưu**.

{{< cards cols="1">}}
{{< card title="" subtitle="Nhập tên danh sách phát" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Tiếp theo, chọn nguồn để thêm bài hát — ở đây, chúng tôi chọn **Thư viện**.

{{< cards cols="1">}}
{{< card title="" subtitle="Thêm bài hát vào danh sách phát mới" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Chọn bài hát bạn muốn và nhấn **Hoàn tất** để thêm.

{{< cards cols="1">}}
{{< card title="" subtitle="Thêm nhạc từ thư viện vào danh sách phát" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Các bản nhạc đã chọn sẽ xuất hiện trong danh sách phát đã tạo.

{{< cards cols="1">}}
{{< card title="" subtitle="Danh sách phát đã tạo hiển thị trong danh sách" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Theo mặc định, bài hát có sẵn để phát trực tuyến. Để nghe ngoại tuyến, bật **Chế độ ngoại tuyến** — ứng dụng sẽ tải xuống tất cả bản nhạc.

{{< cards cols="1">}}
{{< card title="" subtitle="Chế độ ngoại tuyến được bật cho danh sách phát" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Nhấn nút **Thêm hành động** để khám phá các tùy chọn bổ sung. Bạn có thể:

- Lưu trữ danh sách phát
- Thay đổi ảnh bìa album
- Sắp xếp lại bản nhạc
- Và nhiều tính năng hữu ích khác

{{< cards cols="1">}}
{{< card title="" subtitle="Thêm hành động danh sách phát có sẵn" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Kết luận

Với **Evermusic** và **Flacbox**, biến iPhone, iPad hoặc Mac thành trình phát nhạc DLNA mạnh mẽ thật dễ dàng.

- Phát MP3 hoặc FLAC hi-res trực tiếp từ **máy chủ Kodi DLNA**
- Xây dựng thư viện nhạc cá nhân được nhóm theo siêu dữ liệu (album, thể loại, nhà soạn nhạc)
- Tạo và quản lý **danh sách phát tùy chỉnh**
- Bật **chế độ ngoại tuyến** để nghe khi di chuyển
- Kết nối với **nhiều dịch vụ đám mây** và **thiết bị mạng cục bộ**
- Theo dõi thói quen nghe nhạc với **tích hợp Last.fm**

Dù bạn là người yêu âm thanh hay người nghe bình thường, Evermusic và Flacbox cung cấp mọi thứ bạn cần cho phát nhạc và tổ chức mượt mà.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Tải xuống Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Tải xuống Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Bắt đầu xây dựng trải nghiệm âm nhạc cá nhân của bạn ngay hôm nay.

## Câu hỏi thường gặp

{{% details title="Kodi có miễn phí khi dùng làm máy chủ DLNA không?" closed="true" %}}
Có. Kodi hoàn toàn miễn phí và mã nguồn mở. Chạy trên macOS, Windows, Linux và nhiều thiết bị NAS.
{{% /details %}}

{{% details title="Evermusic và Flacbox có hỗ trợ phát FLAC qua DLNA không?" closed="true" %}}
Có. Flacbox được tối ưu hóa cho các định dạng hi-res như FLAC, ALAC và DSD. Evermusic cũng hỗ trợ phát FLAC cùng với MP3 và các định dạng tiêu chuẩn khác.
{{% /details %}}

{{% details title="Tôi có thể nghe ngoại tuyến sau khi phát từ Kodi không?" closed="true" %}}
Có. Bật Chế độ ngoại tuyến trên bất kỳ danh sách phát nào và ứng dụng sẽ tải xuống tất cả bản nhạc vào thiết bị.
{{% /details %}}

{{% details title="Tôi có cần đăng ký premium để sử dụng DLNA không?" closed="true" %}}
Phiên bản miễn phí hỗ trợ tối đa 3 kết nối đám mây hoặc mạng. Premium loại bỏ giới hạn này.
{{% /details %}}

{{% details title="iPhone của tôi có cần ở cùng mạng Wi-Fi với Kodi không?" closed="true" %}}
Có. Phát DLNA hoạt động qua mạng cục bộ. Cả máy chủ Kodi và thiết bị iOS phải kết nối cùng mạng Wi-Fi.
{{% /details %}}

{{% details title="Tôi có thể sử dụng thiết lập này với NAS thay vì Mac hoặc PC không?" closed="true" %}}
Có. Nhiều thiết bị NAS (Synology, QNAP v.v.) hỗ trợ Kodi hoặc có máy chủ DLNA tích hợp. Evermusic và Flacbox có thể kết nối với bất kỳ máy chủ DLNA/UPnP tiêu chuẩn nào.
{{% /details %}}
