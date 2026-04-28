---
title: "Cách kết nối bộ lưu trữ NAS bằng WebDAV và nghe nhạc trên iPhone hoặc Mac"
date: 2024-07-28
description: "Tìm hiểu cách cấu hình WebDAV trên Synology NAS và phát nhạc trực tuyến đến iPhone hoặc Mac bằng Evermusic hoặc Flacbox. Làm theo hướng dẫn từng bước của chúng tôi."
keywords: ["kết nối nas", "webdav synology", "phát nhạc nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["nhạc", "phát trực tuyến", "lưu trữ", "nas", "kết nối", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Tóm tắt:** Cài đặt và bật WebDAV trên Synology NAS, cấu hình quyền thư mục chia sẻ, sau đó kết nối từ Evermusic hoặc Flacbox bằng địa chỉ IP của NAS và cổng WebDAV (mặc định 5005/5006). Bạn có thể phát trực tuyến và quản lý toàn bộ thư viện nhạc mà không cần sao chép tệp vào thiết bị.

Khám phá cách kết nối bộ lưu trữ NAS bằng WebDAV và dễ dàng phát trực tuyến thư viện nhạc đến iPhone hoặc Mac. WebDAV (Web-based Distributed Authoring and Versioning) là một giao thức cho phép bạn quản lý và chia sẻ tệp qua Internet. Bằng cách thiết lập WebDAV trên NAS, bạn có thể truy cập và phát trực tuyến bộ sưu tập nhạc, đảm bảo các bài hát yêu thích luôn trong tầm tay.

Trong hướng dẫn này, chúng tôi sẽ chỉ cho bạn cách thiết lập kết nối WebDAV trên một trong những máy chủ NAS phổ biến nhất, Synology NAS. Làm theo các bước đơn giản của chúng tôi để cấu hình WebDAV trên Synology NAS, và bạn sẽ có thể duyệt, phát trực tuyến và quản lý thư viện nhạc trực tiếp từ iPhone hoặc Mac.

## Bước 1: Cài đặt WebDAV trên Synology NAS

1. Đăng nhập vào Synology NAS và mở **Trung tâm gói**.
2. Tìm "webdav" và cài đặt gói WebDAV nếu chưa được cài đặt. Mở máy chủ WebDAV để cấu hình.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Cài đặt WebDAV trên Synology" width="600" >}}

## Bước 2: Cấu hình máy chủ WebDAV

1. Trên trang cài đặt WebDAV, đánh dấu các ô **Bật HTTP**, **Bật HTTPS**, **Bật WebDAV ẩn danh** và **Bật DavDepthInfinity**.
2. Nhấp **Áp dụng** để lưu thay đổi. Ghi lại số cổng cho kết nối HTTP và HTTPS, mặc định là 5005 và 5006.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Cấu hình cài đặt WebDAV" width="600" >}}

## Bước 3: Cấu hình quyền thư mục chia sẻ

1. Mở **Bảng điều khiển** và đi đến phần **Thư mục chia sẻ**.
2. Chọn thư mục **Nhạc** và nhấp **Chỉnh sửa**.
3. Trong tab **Quyền**, cấu hình các quyền. Bật quyền truy cập khách với Chỉ đọc nếu bạn chỉ cần nghe nhạc, hoặc Đọc/Ghi nếu bạn cần sửa đổi tệp. Lưu thay đổi.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Quyền thư mục chia sẻ" width="600" >}}

## Bước 4: Tìm địa chỉ IP của Synology NAS

1. Mở **Bảng điều khiển** và đi đến tab **Giao diện mạng**, hoặc sử dụng trình duyệt web để truy cập [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Tìm địa chỉ IP của NAS" width="600" >}}

2. Ghi lại địa chỉ IP của Synology NAS (ví dụ: 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Địa chỉ IP Synology NAS" width="600" >}}

## Bước 5: Kết nối với Synology NAS bằng Evermusic/Flacbox

1. Mở ứng dụng Evermusic hoặc Flacbox và đi đến tab **Kết nối**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Tab Kết nối trong Evermusic" width="600" >}}

2. Để kết nối tự động, tìm Synology NAS trong phần **Thiết bị có sẵn** và chạm để kết nối.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Danh sách thiết bị có sẵn" width="600" >}}

3. Để kết nối thủ công, chọn **Kết nối dịch vụ đám mây** và chọn **WebDAV**. Nhập địa chỉ máy chủ theo định dạng: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (ví dụ: [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Cấu hình WebDAV thủ công" width="600" >}}

4. Để trống các trường đăng nhập và mật khẩu cho quyền truy cập khách, hoặc nhập thông tin đăng nhập Synology. Chạm **Đăng nhập**.

## Bước 6: Duyệt và phát nhạc

1. Sau khi kết nối, thiết bị sẽ xuất hiện trong danh sách **Phụ kiện kết nối**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Thiết bị đã kết nối trong Evermusic" width="600" >}}

2. Điều hướng đến thư mục **Nhạc** và chạm vào bất kỳ tệp âm thanh nào để bắt đầu phát.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Duyệt thư mục nhạc" width="600" >}}

## Bước 7: Thêm thư mục đám mây đã kết nối vào thư viện nhạc

1. Mở phần **Thư viện nhạc** trong ứng dụng.
2. Chọn **Thêm nhạc** và chọn **Kết nối**.
3. Chọn máy chủ NAS đã kết nối và chọn thư mục **Nhạc**. Chạm **Hoàn tất**.
4. Ứng dụng sẽ quét thư mục nhạc và thêm các tệp âm thanh được hỗ trợ vào thư viện nhạc. Siêu dữ liệu sẽ được tải và các bài hát sẽ được nhóm theo album, nghệ sĩ và thể loại.

## Kết luận

Bằng cách làm theo các bước này, bạn có thể dễ dàng thiết lập kết nối WebDAV trên Synology NAS và phát trực tuyến thư viện nhạc đến iPhone hoặc Mac bằng Evermusic hoặc Flacbox. Tận hưởng quyền truy cập liền mạch vào các bài hát yêu thích bất cứ lúc nào.

## Câu hỏi thường gặp

{{% details title="Thiết bị NAS nào hỗ trợ WebDAV?" closed="true" %}}
Hầu hết các thương hiệu NAS phổ biến đều hỗ trợ WebDAV, bao gồm Synology, QNAP, TrueNAS và Western Digital. Kiểm tra tài liệu của nhà sản xuất NAS để biết hướng dẫn thiết lập WebDAV.
{{% /details %}}

{{% details title="Sự khác biệt giữa WebDAV và SMB cho phát nhạc trực tuyến từ NAS là gì?" closed="true" %}}
WebDAV hoạt động qua HTTP/HTTPS và phù hợp hơn cho truy cập từ xa qua Internet. SMB thường nhanh hơn trên mạng cục bộ. Evermusic và Flacbox hỗ trợ cả hai giao thức, vì vậy hãy chọn dựa trên nhu cầu truy cập cục bộ hay từ xa.
{{% /details %}}

{{% details title="Tôi có cần tên người dùng và mật khẩu cho WebDAV trên Synology không?" closed="true" %}}
Không, nếu bạn bật quyền truy cập WebDAV ẩn danh và cấu hình quyền khách trên thư mục chia sẻ. Để bảo mật tốt hơn, bạn có thể sử dụng thông tin đăng nhập Synology.
{{% /details %}}

{{% details title="Tôi có thể phát trực tuyến FLAC và các định dạng hi-res khác từ NAS qua WebDAV không?" closed="true" %}}
Có. Cả Evermusic và Flacbox đều hỗ trợ FLAC, ALAC, WAV, DSD và các định dạng độ phân giải cao khác khi phát trực tuyến từ bộ lưu trữ NAS qua WebDAV.
{{% /details %}}

{{% details title="Tại sao ứng dụng không tìm thấy NAS trong Thiết bị có sẵn?" closed="true" %}}
Đảm bảo iPhone/Mac và NAS đang ở trên cùng một mạng Wi-Fi. Nếu tính năng tự động phát hiện không hoạt động, sử dụng tùy chọn kết nối thủ công và nhập trực tiếp địa chỉ IP của NAS và cổng WebDAV.
{{% /details %}}
