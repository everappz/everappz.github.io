---
title: "Cách kết nối Synology NAS và nghe nhạc trên iPhone hoặc Mac của bạn"
date: 2024-09-19
description: "Tìm hiểu cách kết nối Synology NAS bằng API gốc hoặc QuickConnect và phát nhạc chất lượng cao trên iPhone hoặc Mac với Evermusic và Flacbox."
keywords: ["synology nas", "phát nhạc trực tuyến", "quickconnect", "evermusic synology", "flacbox synology", "trình phát nhạc nas", "nhạc nas iphone"]
tags: ["nhạc", "phát trực tuyến", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Tóm tắt:** Kết nối Synology NAS của bạn với Evermusic hoặc Flacbox bằng API gốc của Synology -- thủ công qua địa chỉ IP hoặc tự động qua QuickConnect ID. QuickConnect cho phép bạn phát nhạc từ xa mà không cần chuyển tiếp cổng. Cả hai ứng dụng đều hỗ trợ FLAC, MP3, WAV và các định dạng hi-res khác.

Nếu bạn đang tìm kiếm cách liền mạch để kết nối Synology NAS và thưởng thức thư viện nhạc trên iPhone hoặc Mac, ứng dụng Evermusic và Flacbox là giải pháp hoàn hảo. Các ứng dụng này hỗ trợ nhiều định dạng âm thanh, bao gồm FLAC, MP3 và WAV, giúp dễ dàng phát trực tuyến và nghe nhạc chất lượng cao trực tiếp từ Synology NAS.

Trong hướng dẫn này, chúng tôi sẽ chỉ cho bạn cách kết nối Synology NAS với ứng dụng Evermusic hoặc Flacbox bằng API gốc của Synology và tính năng QuickConnect. Bằng cách tận dụng API trực tiếp của Synology, bạn có thể truy cập an toàn thư viện nhạc bên ngoài mạng gia đình mà không cần cấu hình phức tạp như WebDAV, SMB, DLNA. Với QuickConnect, bạn có thể phát trực tuyến và quản lý nhạc từ bất kỳ đâu bằng iPhone hoặc Mac.

## Bước 1: Cấu hình quyền thư mục chia sẻ (tùy chọn)

1. Mở **Bảng điều khiển** và đi đến phần **Thư mục chia sẻ**.

![Thư mục chia sẻ](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Chọn thư mục **Music** và nhấp **Chỉnh sửa**.

3. Trong tab **Quyền**, cấu hình các quyền. Bật quyền truy cập khách với Chỉ đọc nếu bạn chỉ cần nghe nhạc, hoặc Đọc/Ghi nếu bạn cần sửa đổi tệp. Lưu các thay đổi.

![Quyền](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Bước 2: Tìm địa chỉ IP của Synology NAS

1. Mở **Bảng điều khiển** và đi đến tab **Giao diện mạng**.

![Giao diện mạng](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Hoặc sử dụng trình duyệt web để truy cập [find.synology.com](http://find.synology.com).

![Tìm Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Ghi lại địa chỉ IP của Synology NAS (ví dụ: 192.168.18.137).

## Bước 3: Tìm cổng mạng của Synology NAS

Bạn có thể tìm tài liệu chính thức của Synology về các cổng mạng mặc định của DSM tại [bài viết Trung tâm kiến thức Synology](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services) này.

Synology DSM sử dụng các cổng mặc định sau:
- **HTTP (Truy cập web):** Cổng **5000**
- **HTTPS (Truy cập web bảo mật):** Cổng **5001**

Đây là các cổng mặc định để truy cập giao diện DSM.

![Cổng mạng](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Bước 4: Bật tính năng QuickConnect ID

Synology QuickConnect ID là mã định danh duy nhất cho phép bạn truy cập Synology NAS từ xa qua internet mà không cần cấu hình các cài đặt mạng phức tạp như chuyển tiếp cổng. QuickConnect đơn giản hóa truy cập từ xa bằng cách sử dụng máy chủ của Synology để thiết lập kết nối giữa NAS và thiết bị của bạn, như điện thoại thông minh hoặc máy tính, thông qua QuickConnect ID.

**Cách tìm hoặc thiết lập QuickConnect ID:**

1. **Đăng nhập vào DSM.**
2. Đi đến **Bảng điều khiển > Truy cập bên ngoài > QuickConnect**.
3. **Bật QuickConnect** và tạo hoặc xem QuickConnect ID duy nhất của bạn.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Bước 5: Kết nối với Synology NAS trên iPhone/Mac bằng Evermusic hoặc Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) và [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) đều là ứng dụng trình phát nhạc được thiết kế cho thiết bị iOS và macOS, mỗi ứng dụng cung cấp các tính năng và khả năng độc đáo để quản lý và thưởng thức thư viện nhạc của bạn.

1. Mở ứng dụng Evermusic hoặc Flacbox và đi đến tab **Kết nối**.

![Kết nối](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Chọn **Kết nối dịch vụ đám mây** và chọn **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Bạn có hai tùy chọn kết nối: **thủ công** sử dụng địa chỉ IP và cổng của máy chủ, hoặc **tự động** qua QuickConnect ID.

### Kết nối thủ công

Đối với phương pháp thủ công, bạn sẽ cần địa chỉ IP trực tiếp và số cổng đã lấy ở các bước trước.

1. Nhập URL máy chủ bạn đã lấy ở bước 2, sử dụng định dạng sau: GIAO_THỨC://ĐỊA_CHỈ_IP:SỐ_CỔNG
   - Sử dụng **cổng 5000** cho HTTP và **cổng 5001** cho kết nối HTTPS.

   Ví dụ:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Số cổng thực tế có thể được xác nhận ở bước 3 trong quá trình thiết lập.
3. Nhập **tên đăng nhập** và **mật khẩu** cho Synology NAS.
4. Nhấn **Đăng nhập** để thiết lập kết nối.

![Kết nối thủ công](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Kết nối tự động

Đối với kết nối tự động, bạn sẽ sử dụng **QuickConnect ID** từ bước 4. Thay vì nhập thủ công địa chỉ IP và số cổng cho Synology NAS, chỉ cần nhập **QuickConnect ID**. Ứng dụng sẽ tự động lấy thông tin kết nối cần thiết.

Phương pháp này cho phép bạn truy cập NAS từ xa, ngay cả bên ngoài mạng gia đình, để bạn có thể quản lý tệp từ internet mà không cần cấu hình chuyển tiếp cổng hoặc địa chỉ IP tĩnh.

![Kết nối tự động](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Xác thực hai yếu tố

Bắt đầu từ DSM 4.2, Synology đã giới thiệu **xác minh 2 bước** để tăng cường bảo mật. Tính năng này yêu cầu mã **mật khẩu dùng một lần (OTP)**, được tạo bởi ứng dụng xác thực, ngoài thông tin đăng nhập thông thường của bạn. Nếu bạn đã bật xác minh 2 bước, sau khi nhập tên người dùng và mật khẩu, bạn cũng cần nhập OTP để đăng nhập vào phiên DSM.

Xin lưu ý, khi phiên của bạn hết hạn, ứng dụng sẽ cần được cấp phép lại thủ công. Để cấp phép lại:

1. Đi đến tab **Kết nối** trong ứng dụng.
2. Nhấn nút **Thêm hành động** bên cạnh tên máy chủ.
3. Chọn **Cài đặt** từ menu để nhập mã xác thực mới và hoàn tất quá trình cấp phép lại.

Điều này đảm bảo rằng ngay cả khi bạn truy cập NAS từ mạng không đáng tin cậy, dữ liệu của bạn vẫn an toàn.

## Bước 6: Duyệt và phát nhạc

1. Khi đã kết nối, thiết bị sẽ xuất hiện trong danh sách **Thiết bị đã kết nối**.

![Thiết bị đã kết nối](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Duyệt đến thư mục **Music** và nhấn vào bất kỳ tệp âm thanh nào để bắt đầu phát.

![Phát nhạc](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Bước 7: Thêm thư mục đám mây đã kết nối vào thư viện nhạc

1. Mở phần **Thư viện nhạc** trong ứng dụng.
2. Chọn **Thêm nhạc** và chọn **Kết nối**.
3. Chọn máy chủ NAS đã kết nối và chọn thư mục **Music**. Nhấn **Hoàn tất**.
4. Ứng dụng sẽ quét thư mục nhạc và thêm các tệp âm thanh được hỗ trợ vào thư viện nhạc. Siêu dữ liệu sẽ được tải và các bài hát của bạn sẽ được nhóm theo album, nghệ sĩ và thể loại.

## Kết luận

Bằng cách làm theo các bước này, bạn có thể dễ dàng thiết lập kết nối trên Synology NAS và phát trực tuyến toàn bộ thư viện nhạc đến iPhone hoặc Mac bằng Evermusic hoặc Flacbox. Dù ở nhà hay đang di chuyển, hãy tận hưởng truy cập liền mạch, chất lượng cao đến các bài hát yêu thích từ bất kỳ đâu bằng QuickConnect. Tận dụng sự linh hoạt và tiện lợi mà các ứng dụng này mang lại, và bắt đầu quản lý bộ sưu tập nhạc của bạn dễ dàng trên tất cả các thiết bị.

Với truy cập từ xa an toàn thông qua QuickConnect và hỗ trợ nhiều định dạng âm thanh, bạn sẽ không bao giờ xa rời âm nhạc của mình. Bây giờ, các tệp được lưu trữ trên NAS chỉ cách bạn một cú chạm!

## FAQ

{{% details title="Sự khác biệt giữa kết nối thủ công và QuickConnect là gì?" closed="true" %}}
Kết nối thủ công sử dụng địa chỉ IP và cổng của NAS, hoạt động trên mạng cục bộ. QuickConnect sử dụng dịch vụ chuyển tiếp của Synology để thiết lập kết nối từ bất kỳ đâu qua internet, không cần chuyển tiếp cổng.
{{% /details %}}

{{% details title="Tôi có thể phát nhạc từ Synology NAS bên ngoài mạng gia đình không?" closed="true" %}}
Có. Bật QuickConnect trên Synology NAS và sử dụng QuickConnect ID trong Evermusic hoặc Flacbox để phát nhạc từ bất kỳ đâu có kết nối internet.
{{% /details %}}

{{% details title="Những định dạng âm thanh nào được hỗ trợ khi phát từ Synology NAS?" closed="true" %}}
Evermusic và Flacbox hỗ trợ FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD và nhiều định dạng khác. Tất cả các định dạng được hỗ trợ đều hoạt động khi phát từ Synology NAS.
{{% /details %}}

{{% details title="Tôi có cần xác thực hai yếu tố để kết nối không?" closed="true" %}}
Không, 2FA là tùy chọn. Tuy nhiên, nếu bạn đã bật xác minh 2 bước trên Synology DSM, ứng dụng sẽ yêu cầu mật khẩu dùng một lần khi đăng nhập. Bạn sẽ cần cấp phép lại khi phiên hết hạn.
{{% /details %}}

{{% details title="Tôi nên sử dụng API gốc Synology, WebDAV hay SMB để kết nối?" closed="true" %}}
API gốc Synology với QuickConnect là lựa chọn tốt nhất cho truy cập từ xa. Đối với sử dụng mạng cục bộ, SMB thường là tùy chọn nhanh nhất. WebDAV hoạt động tốt cho cả truy cập cục bộ và từ xa. Evermusic và Flacbox hỗ trợ cả ba giao thức.
{{% /details %}}
