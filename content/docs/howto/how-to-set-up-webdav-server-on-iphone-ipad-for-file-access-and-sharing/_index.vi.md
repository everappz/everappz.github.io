---
title: "Cách thiết lập máy chủ WebDAV trên iPhone và iPad để truy cập và chia sẻ tập tin"
description: "Biến iPhone hoặc iPad thành máy chủ WebDAV với Everdisk và gắn nó như một ổ đĩa mạng trên Mac Finder, Windows File Explorer, Linux, Android hoặc một iPhone khác qua Wi-Fi. Hướng dẫn thiết lập đầy đủ, địa chỉ WebDAV và cổng, cùng cách kết nối từng bước cho mọi thiết bị."
date: 2026-09-19
tags: ["everdisk", "webdav", "ổ đĩa mạng", "chia sẻ tập tin", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["máy chủ WebDAV iPhone", "máy chủ WebDAV iPad", "cách thiết lập WebDAV trên iPhone", "gắn iPhone làm ổ đĩa mạng", "kết nối iPhone WebDAV Mac Finder", "WebDAV Windows File Explorer iPhone", "ổ đĩa mạng iphone Windows", "WebDAV Linux iPhone", "truy cập tập tin iPhone từ máy tính", "webdav iphone sang iphone", "chia sẻ tập tin iPhone WebDAV", "ánh xạ ổ đĩa mạng iphone", "truyền tập tin iphone webdav", "địa chỉ cổng webdav iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV biến một thư mục thành một ổ đĩa mạng mà máy tính có thể mở trong trình quản lý tập tin bình thường của nó. Nó chạy trên cùng giao thức web mà trình duyệt của bạn dùng, đó là lý do nó đi lại tốt qua Mac, Windows và Linux mà không cần driver đặc biệt. Với [Everdisk](/products/everdisk) bạn có thể chạy một máy chủ WebDAV trên iPhone hoặc iPad, để chiếc điện thoại hiện ra như một ổ đĩa mà bạn có thể duyệt, sao chép về và sao chép sang từ gần như bất kỳ máy tính nào.

WebDAV là lựa chọn tốt nhất khi có Windows trong cuộc, vì Windows File Explorer kết nối với nó một cách gọn gàng. Hướng dẫn này bao quát phần thiết lập cùng cách kết nối từ Mac, Windows, Linux, Android và một chiếc iPhone thứ hai.

## Bạn cần những gì

- Một iPhone hoặc iPad đã cài [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Một máy tính hoặc thiết bị khác trong **cùng mạng Wi-Fi**.
- Tập tin bạn muốn chia sẻ, nằm trong thư mục Tài liệu của Everdisk hoặc trong các thư mục bạn thêm vào.

## Thiết lập máy chủ WebDAV trong Everdisk

### Bước 1: Chọn thứ cần chia sẻ và đặt quyền truy cập

Mở Everdisk, vào thẻ **Chia sẻ**, và chạm **Chia sẻ gì**. Thư mục Tài liệu được chia sẻ mặc định. Thêm nữa bằng **Thêm thư mục** và **Thêm tệp**.

Mở **Cài đặt**, rồi **Chia sẻ**, rồi **Truy cập**. Bật **Chỉnh sửa tệp** nếu bạn muốn các máy tính đã kết nối sao chép tập tin vào điện thoại cùng đổi tên hoặc xóa, hoặc tắt để có một ổ đĩa chỉ đọc. Đặt **Tên đăng nhập** và **Mật khẩu** tại đây nếu bạn muốn một phần đăng nhập, hoặc để trống để truy cập khách.

### Bước 2: Bật máy chủ WebDAV

Vào **Cài đặt**, rồi **Chia sẻ**, rồi **Kết nối**, và bật **Máy tính**. Đó là máy chủ WebDAV (nó mang nhãn WebDAV).

### Bước 3: Bắt đầu chia sẻ và ghi lại địa chỉ

Trở lại thẻ **Chia sẻ** và chạm **Bắt đầu**. Phần **Cách kết nối** hiển thị địa chỉ WebDAV. Nó trông như thế này:

```
http://192.168.1.20:8080
```

Con số sau dấu hai chấm là **cổng**, mặc định là **8080**. Phần đầu là địa chỉ của iPhone trên Wi-Fi, nên của bạn sẽ khác. Giữ Everdisk mở trên màn hình trong lúc một thiết bị đang kết nối.

## Kết nối từ Mac

1. Mở **Finder**, chọn **Go**, rồi **Connect to Server** (hoặc nhấn **Command và K**).
2. Gõ địa chỉ WebDAV hiển thị trong Everdisk, ví dụ `http://192.168.1.20:8080`.
3. Nhấp **Connect**, rồi chọn **Guest** hoặc nhập **Tên đăng nhập** và **Mật khẩu** của bạn.

iPhone của bạn mở ra trong một cửa sổ Finder và hoạt động như một thư mục bình thường. Sao chép tập tin theo cả hai chiều nếu Chỉnh sửa tệp đang bật.

## Kết nối từ Windows

Windows có sẵn một máy khách WebDAV tích hợp, nên cách này hoạt động từ File Explorer.

1. Mở **File Explorer**, nhấp chuột phải vào **This PC** trong thanh bên, và chọn **Add a network location** (bạn cũng có thể dùng **Map network drive**).
2. Khi được hỏi địa chỉ, gõ cùng địa chỉ WebDAV từ Everdisk, ví dụ `http://192.168.1.20:8080`, rồi nhấp **Next**.
3. Nhập **Tên đăng nhập** và **Mật khẩu** nếu bạn đã đặt.

Thiết bị khi đó hiện ra dưới This PC như một vị trí mạng bạn có thể mở và sao chép tập tin từ đó. Nếu Windows từ chối kết nối lần đầu, hãy chắc chắn dịch vụ **WebClient** đang chạy (tìm Services trong menu Start, tìm WebClient, và đặt nó khởi động), rồi thử lại.

## Kết nối từ Linux

1. Mở trình quản lý tập tin của bạn và chọn **Connect to Server** hoặc **Other Locations**.
2. Nhập địa chỉ với tiền tố WebDAV, ví dụ `dav://192.168.1.20:8080` (chỉ dùng `davs://` nếu bạn đã thiết lập TLS).
3. Kết nối với tư cách khách hoặc nhập tên đăng nhập của bạn.

## Kết nối từ Android

Android không có trình duyệt WebDAV hệ thống, nên hãy dùng một trình quản lý tập tin có hỗ trợ nó:

1. Cài một ứng dụng như **Solid Explorer** hoặc **CX File Explorer**.
2. Thêm một kết nối **WebDAV** mới.
3. Nhập máy chủ và **cổng 8080**, chọn giao thức `http`, và thêm tên đăng nhập của bạn nếu bạn đã đặt.

## Kết nối từ một iPhone hoặc iPad khác

Ứng dụng Tệp của iOS không có sẵn máy khách WebDAV, nên hãy dùng một trong những cách này:

- **Chính thẻ Thiết bị của Everdisk.** Trên thiết bị thứ hai, mở Everdisk, vào **Thiết bị**, chạm **Kết nối mới**, chọn **WebDAV**, và nhập địa chỉ, ví dụ `http://192.168.1.20:8080`. Đây là cách đơn giản nhất và không cần gì thêm.
- **Một ứng dụng WebDAV** như Documents by Readdle, vốn có thể thêm một kết nối WebDAV với cùng địa chỉ và tên đăng nhập.

## Thích một liên kết nhanh hơn là một ổ đĩa?

Nếu bạn chỉ cần lấy nhanh một tập tin và không muốn gắn ổ đĩa gì cả, hãy bật kết nối **Trình duyệt** trong Cài đặt, Chia sẻ, Kết nối. Everdisk khi đó cho bạn một địa chỉ web bạn có thể mở trong bất kỳ trình duyệt nào trên bất kỳ thiết bị nào để duyệt và tải tập tin của bạn. Đây là cách nhanh nhất để trao một tập tin cho một PC chạy Windows, một Chromebook hay điện thoại của bạn bè.

## Chỉ đọc hoặc đọc và ghi

Công tắc **Chỉnh sửa tệp** trong Cài đặt, Chia sẻ, Truy cập quyết định điều này. Bật nghĩa là các máy tính đã kết nối có thể tải lên, đổi tên và xóa. Tắt nghĩa là ổ đĩa chỉ đọc, nên người khác có thể xem và sao chép tập tin của bạn nhưng không thể thay đổi chúng.

## Những cách người ta dùng thực tế

- **Sao chép tập tin vào iPhone từ một PC chạy Windows** bằng cách ánh xạ nó như một vị trí mạng và kéo chúng qua.
- **Chuyển ảnh và tài liệu sang laptop** bằng trình quản lý tập tin bạn đã quen, không cần cáp và không cần iTunes.
- **Chỉnh sửa một tài liệu tại chỗ** từ Mac của bạn, mở nó thẳng từ điện thoại và lưu ngược lại.
- **Chuyển một thư mục giữa iPhone và iPad** bằng thẻ Thiết bị của Everdisk trên thiết bị nhận.

## Một vài mẹo nhỏ

- Giữ Everdisk mở trong lúc một thiết bị đang kết nối. Khóa điện thoại quá lâu có thể tạm dừng ứng dụng.
- Trên Windows, nếu kết nối thất bại, hãy khởi động dịch vụ WebClient và thử lại địa chỉ.
- WebDAV và SMB đều gắn như ổ đĩa mạng. Dùng WebDAV khi có Windows tham gia, và [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) khi bạn muốn tốc độ Finder và mã hóa.
- Để truyền nhanh nhất, giữ chất lượng ảnh và video ở Bản gốc trong Cài đặt.

## Câu hỏi thường gặp

{{% details title="Địa chỉ và cổng WebDAV cho iPhone của tôi là gì?" closed="true" %}}
Sau khi bạn bắt đầu chia sẻ, Everdisk hiển thị địa chỉ trên màn hình Chia sẻ. Nó trông như http://192.168.1.20:8080. Con số 8080 là cổng Everdisk dùng cho WebDAV, và phần đầu là địa chỉ của iPhone trên Wi-Fi, nên của bạn sẽ khác.
{{% /details %}}

{{% details title="Làm sao để kết nối tới WebDAV của iPhone từ Windows?" closed="true" %}}
Mở File Explorer, nhấp chuột phải vào This PC, và chọn Add a network location hoặc Map network drive. Nhập địa chỉ WebDAV từ Everdisk, ví dụ http://192.168.1.20:8080, rồi nhập tên đăng nhập nếu bạn đã đặt. Nếu Windows không kết nối được, hãy chắc chắn dịch vụ WebClient đang chạy (tìm Services, tìm WebClient, khởi động nó) và thử lại.
{{% /details %}}

{{% details title="Tôi có thể dùng WebDAV giữa hai iPhone không?" closed="true" %}}
Được, nhưng ứng dụng Tệp của iOS không có máy khách WebDAV, nên hãy dùng Everdisk trên thiết bị thứ hai. Mở thẻ Thiết bị, chạm Kết nối mới, chọn WebDAV, và nhập địa chỉ hiển thị trên điện thoại thứ nhất. Một ứng dụng WebDAV như Documents by Readdle cũng dùng được.
{{% /details %}}

{{% details title="WebDAV có cần mật khẩu không?" closed="true" %}}
Không, tên đăng nhập là tùy chọn. Để trống Tên đăng nhập và Mật khẩu trong Cài đặt, Chia sẻ, Truy cập để truy cập khách, hoặc đặt chúng nếu bạn muốn các kết nối phải đăng nhập.
{{% /details %}}

{{% details title="Người khác có thể thay đổi tập tin của tôi qua WebDAV không?" closed="true" %}}
Chỉ khi bạn cho phép. Công tắc Chỉnh sửa tệp trong Cài đặt, Chia sẻ, Truy cập kiểm soát điều này. Bật cho phép thiết bị đã kết nối tải lên, đổi tên và xóa. Tắt làm ổ đĩa chỉ đọc, nên người khác có thể xem và sao chép nhưng không thay đổi được gì.
{{% /details %}}

{{% details title="WebDAV hay SMB, khác nhau thế nào?" closed="true" %}}
Cả hai đều gắn iPhone của bạn như một ổ đĩa mạng. WebDAV chạy trên giao thức web và kết nối gọn gàng từ Windows File Explorer, đó là thế mạnh chính của nó. SMB là cơ chế chia sẻ tập tin gốc trên Mac, Linux và các thiết bị NAS, thường nhanh hơn trên Mac, và là kết nối Everdisk duy nhất có thể mã hóa các lần truyền. Everdisk có thể chạy cả hai cùng lúc.
{{% /details %}}

{{% details title="Vì sao ổ đĩa WebDAV của tôi bị ngắt kết nối?" closed="true" %}}
iPhone của bạn là máy chủ, và iOS tạm dừng các ứng dụng nằm ở nền quá lâu. Giữ Everdisk mở trên màn hình trong lúc một thiết bị đang kết nối, và cắm nguồn điện cho những lần truyền dài. Cũng hãy xác nhận cả hai thiết bị vẫn ở cùng mạng Wi-Fi.
{{% /details %}}

{{% details title="Tôi có thể kết nối qua WebDAV mà không có Wi-Fi không?" closed="true" %}}
Được, nếu bạn cắm iPhone vào Mac bằng cáp. Everdisk khi đó hiển thị thêm một địa chỉ kết nối bằng cáp mà chiếc Mac đã nối có thể mở trong Finder, cách này hoạt động ngay cả khi hoàn toàn không có Wi-Fi. Trên cáp, chỉ chiếc Mac đó mới chạm tới được thiết bị.
{{% /details %}}

{{% details title="Everdisk có miễn phí không?" closed="true" %}}
Có, Everdisk tải miễn phí và máy chủ WebDAV được bao gồm sẵn. Một gói mua Premium một lần duy nhất tùy chọn thêm các tính năng bổ sung như cổng tùy chỉnh cùng chuyển đổi ảnh và video. Bạn có thể thiết lập WebDAV và chia sẻ tập tin mà không phải trả tiền.
{{% /details %}}

Sẵn sàng thử chưa? [Tải Everdisk từ App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) và gắn iPhone của bạn như một ổ đĩa chỉ trong vài phút. Có câu hỏi hay góp ý? Gửi email cho chúng tôi tại **support@everappz.com**.
