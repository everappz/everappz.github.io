---
title: "Cách thiết lập máy chủ FTP trên iPhone và iPad để truyền tập tin"
description: "Biến iPhone hoặc iPad thành máy chủ FTP với Everdisk và truyền tập tin từ Mac, PC chạy Windows, Linux, Android, một ứng dụng FTP như FileZilla, hoặc một iPhone khác qua Wi-Fi. Hướng dẫn thiết lập đầy đủ, địa chỉ ftp và cổng, truy cập khách, cùng cách kết nối từng bước cho mọi thiết bị."
date: 2026-09-19
tags: ["everdisk", "ftp", "truyền tập tin", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["máy chủ FTP iPhone", "máy chủ FTP iPad", "cách thiết lập FTP trên iPhone", "ứng dụng máy chủ ftp iphone", "kết nối FileZilla tới iPhone", "Cyberduck iPhone FTP", "truyền tập tin iPhone FTP", "ftp iphone sang máy tính", "ftp iphone sang iphone", "kết nối tới FTP iPhone từ Windows", "địa chỉ cổng ftp iphone", "ftp ẩn danh iphone", "chia sẻ tập tin iphone ftp", "ftp iphone cho máy ảnh nas"]
readingTime: 9
---

{{< author-byline >}}

FTP là công cụ truyền tập tin cũ nhưng đáng tin cậy. Nó đã tồn tại hàng chục năm, và đó chính là lý do nó hữu ích đến vậy: gần như mọi thứ có thể nói chuyện với một máy chủ đều hiểu nó. Máy ảnh, smart TV, router, ổ đĩa mạng, công cụ tự động hóa và mọi ứng dụng FTP trên máy tính đều nói FTP. Với [Everdisk](/products/everdisk) bạn có thể chạy một máy chủ FTP trên iPhone hoặc iPad, để chiếc điện thoại trở thành một nơi mà những thiết bị và ứng dụng đó có thể kết nối tới và di chuyển tập tin.

Hãy chọn FTP khi các tùy chọn khác không vừa, ví dụ một thiết bị cũ hơn hoặc một ứng dụng chỉ biết cách kết nối qua FTP. Hướng dẫn này bao quát phần thiết lập cùng cách kết nối từ Mac, Windows, một ứng dụng FTP, Linux, Android và một chiếc iPhone thứ hai.

## Bạn cần những gì

- Một iPhone hoặc iPad đã cài [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Một máy tính, ứng dụng hoặc thiết bị trong **cùng mạng Wi-Fi**.
- Tập tin bạn muốn chia sẻ, nằm trong thư mục Tài liệu của Everdisk hoặc trong các thư mục bạn thêm vào.

## Thiết lập máy chủ FTP trong Everdisk

### Bước 1: Chọn thứ cần chia sẻ và đặt quyền truy cập

Mở Everdisk, vào thẻ **Chia sẻ**, và chạm **Chia sẻ gì**. Thư mục Tài liệu được chia sẻ mặc định. Thêm nữa bằng **Thêm thư mục** và **Thêm tệp**.

Mở **Cài đặt**, rồi **Chia sẻ**, rồi **Truy cập**. Bật **Chỉnh sửa tệp** nếu bạn muốn người khác tải lên, đổi tên và xóa, hoặc tắt để chỉ cho phép tải xuống. Đặt **Tên đăng nhập** và **Mật khẩu** nếu bạn muốn một phần đăng nhập, hoặc để trống để ai cũng kết nối được với tư cách khách.

### Bước 2: Bật máy chủ FTP

Vào **Cài đặt**, rồi **Chia sẻ**, rồi **Kết nối**, và bật **Ứng dụng và thiết bị khác**. Đó là máy chủ FTP (nó mang nhãn FTP).

### Bước 3: Bắt đầu chia sẻ và ghi lại địa chỉ

Trở lại thẻ **Chia sẻ** và chạm **Bắt đầu**. Phần **Cách kết nối** hiển thị địa chỉ FTP. Nó trông như thế này:

```
ftp://192.168.1.20:2121
```

Con số sau dấu hai chấm là **cổng**, mặc định là **2121**. Phần đầu là địa chỉ của iPhone trên Wi-Fi, nên của bạn sẽ khác. Giữ Everdisk mở trên màn hình trong lúc một thiết bị đang kết nối.

## Kết nối từ Mac

1. Mở **Finder**, chọn **Go**, rồi **Connect to Server** (hoặc nhấn **Command và K**).
2. Gõ địa chỉ FTP hiển thị trong Everdisk, ví dụ `ftp://192.168.1.20:2121`.
3. Nhấp **Connect**, rồi chọn **Guest** hoặc nhập **Tên đăng nhập** và **Mật khẩu** của bạn.

Finder gắn thư mục chia sẻ FTP để bạn duyệt và sao chép tập tin về Mac. Lưu ý rằng Finder mở FTP ở dạng chỉ đọc. Khi bạn muốn tải lên từ Mac, hãy dùng một ứng dụng FTP như mô tả bên dưới.

## Kết nối từ Windows

1. Mở **File Explorer** và nhấp vào thanh địa chỉ ở trên cùng.
2. Gõ địa chỉ FTP từ Everdisk, ví dụ `ftp://192.168.1.20:2121`, và nhấn **Enter**.
3. Nhập **Tên đăng nhập** và **Mật khẩu** nếu bạn đã đặt, hoặc tiếp tục với tư cách khách.

Các tập tin chia sẻ hiện ra trong cửa sổ và bạn có thể sao chép chúng về PC của mình.

## Kết nối bằng một ứng dụng FTP (FileZilla, Cyberduck)

Để tải lên và toàn quyền kiểm soát, một ứng dụng FTP là công cụ tốt nhất. **FileZilla** và **Cyberduck** đều miễn phí và chạy trên Windows, Mac và Linux.

1. Mở ứng dụng và tạo một kết nối mới.
2. Đặt **Host** là địa chỉ Wi-Fi của iPhone, và **Port** là **2121**.
3. Với phần đăng nhập, nhập **Tên đăng nhập** và **Mật khẩu** của bạn, hoặc chọn **Anonymous** nếu bạn không đặt.
4. Kết nối, và kéo tập tin theo cả hai chiều (tải lên cần bật Chỉnh sửa tệp).

## Kết nối từ Linux

1. Mở trình quản lý tập tin của bạn và chọn **Connect to Server** hoặc **Other Locations**.
2. Nhập địa chỉ, ví dụ `ftp://192.168.1.20:2121`.
3. Kết nối với tư cách khách hoặc bằng tên đăng nhập của bạn.

Bạn cũng có thể dùng bất kỳ máy khách FTP Linux nào từ terminal, trỏ nó tới cùng máy chủ và cổng 2121.

## Kết nối từ Android

Android không có trình duyệt FTP hệ thống, nên hãy dùng một ứng dụng:

1. Cài một máy khách FTP như **AndFTP**, **FTPCafe**, hoặc một trình quản lý tập tin có hỗ trợ FTP như **Solid Explorer**.
2. Thêm một kết nối với máy chủ, **cổng 2121**, và tên đăng nhập của bạn hoặc Anonymous.
3. Duyệt và truyền.

## Kết nối từ một iPhone hoặc iPad khác

Ứng dụng Tệp của iOS không có sẵn máy khách FTP, nên hãy dùng một trong những cách này trên thiết bị thứ hai:

- **Chính thẻ Thiết bị của Everdisk.** Mở Everdisk, vào **Thiết bị**, chạm **Kết nối mới**, chọn **FTP**, và nhập địa chỉ, ví dụ `ftp://192.168.1.20:2121`. Đây là cách đơn giản nhất.
- **Một ứng dụng FTP chuyên dụng** cho iOS, dùng cùng máy chủ, cổng 2121 và tên đăng nhập.

## Kết nối thiết bị khác: máy ảnh, TV, router và NAS

Đây là nơi FTP tỏa sáng. Nhiều thiết bị có sẵn một máy khách FTP tích hợp có thể gửi hoặc lấy tập tin:

- **Máy ảnh** tải ảnh lên qua FTP có thể gửi chúng thẳng vào iPhone của bạn.
- **Smart TV, router, hộp NAS và công cụ tự động hóa** có hỗ trợ FTP đều kết nối theo cùng cách.

Trỏ chúng tới địa chỉ Wi-Fi của iPhone, cổng **2121**, và tên đăng nhập của bạn (hoặc Anonymous), dùng địa chỉ hiển thị trong Everdisk.

## Chỉ đọc hoặc đọc và ghi

Công tắc **Chỉnh sửa tệp** trong Cài đặt, Chia sẻ, Truy cập kiểm soát điều này. Bật cho phép người khác tải lên, đổi tên và xóa. Tắt nghĩa là họ chỉ có thể tải xuống. Hãy chọn chỉ đọc khi bạn trao tập tin ra ngoài và không muốn có gì bị thay đổi trên điện thoại của mình.

## Những cách người ta dùng thực tế

- **Kết nối FileZilla tới iPhone** và đẩy một loạt tập tin lên điện thoại trong một lần.
- **Để một ứng dụng hay thiết bị cũ chỉ nói FTP** chạm tới tập tin của bạn khi không có gì khác kết nối được.
- **Nhận ảnh từ một chiếc máy ảnh** tải lên qua FTP.
- **Chuyển tập tin giữa iPhone và iPad** bằng thẻ Thiết bị của Everdisk trên thiết bị nhận.

## Một vài mẹo nhỏ

- Giữ Everdisk mở trong lúc một thiết bị đang kết nối, vì iOS tạm dừng các ứng dụng nền sau một lúc.
- Để tải lên từ Mac, hãy dùng FileZilla hoặc Cyberduck thay vì Finder, vì Finder mở FTP ở dạng chỉ đọc.
- Để trống phần đăng nhập để tương thích rộng nhất, rồi kết nối với tư cách Anonymous, điều mà hầu hết máy khách FTP đều hỗ trợ.
- FTP không mã hóa lưu lượng của nó. Trên một mạng bạn không tin tưởng, hãy dùng [máy chủ SMB có mã hóa](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) thay thế.

## Câu hỏi thường gặp

{{% details title="Địa chỉ và cổng FTP cho iPhone của tôi là gì?" closed="true" %}}
Sau khi bạn bắt đầu chia sẻ, Everdisk hiển thị địa chỉ trên màn hình Chia sẻ. Nó trông như ftp://192.168.1.20:2121. Con số 2121 là cổng Everdisk dùng cho FTP, và phần đầu là địa chỉ của iPhone trên Wi-Fi, nên của bạn sẽ khác.
{{% /details %}}

{{% details title="Làm sao để kết nối FileZilla hoặc Cyberduck tới iPhone?" closed="true" %}}
Mở ứng dụng và tạo một kết nối mới. Đặt Host là địa chỉ Wi-Fi của iPhone và Port là 2121. Nhập Tên đăng nhập và Mật khẩu của bạn, hoặc chọn Anonymous nếu bạn không đặt trong Everdisk. Kết nối, và bạn có thể kéo tập tin theo cả hai chiều khi Chỉnh sửa tệp đang bật.
{{% /details %}}

{{% details title="Tôi có thể kết nối tới FTP của iPhone từ Windows không?" closed="true" %}}
Được. Mở File Explorer, nhấp vào thanh địa chỉ, gõ địa chỉ FTP từ Everdisk (ví dụ ftp://192.168.1.20:2121), và nhấn Enter. Nhập tên đăng nhập nếu bạn đã đặt, hoặc tiếp tục với tư cách khách. Để tải lên và kiểm soát nhiều hơn, hãy dùng một ứng dụng FTP như FileZilla thay thế.
{{% /details %}}

{{% details title="Tôi có cần tên đăng nhập cho FTP không?" closed="true" %}}
Không, tên đăng nhập là tùy chọn. Để trống Tên đăng nhập và Mật khẩu trong Cài đặt, Chia sẻ, Truy cập, và kết nối với tư cách Anonymous, điều mà hầu hết máy khách FTP đều hỗ trợ. Đặt một tên đăng nhập nếu bạn muốn các kết nối phải đăng nhập trước.
{{% /details %}}

{{% details title="Vì sao tôi chỉ tải xuống được mà không tải lên được qua FTP?" closed="true" %}}
Hai lý do thường gặp. Thứ nhất, công tắc Chỉnh sửa tệp trong Cài đặt, Chia sẻ, Truy cập phải bật để cho phép tải lên, đổi tên và xóa. Thứ hai, Finder trên Mac mở FTP ở dạng chỉ đọc, nên hãy dùng một ứng dụng FTP như FileZilla hoặc Cyberduck khi bạn muốn tải lên.
{{% /details %}}

{{% details title="Tôi có thể dùng FTP giữa hai iPhone không?" closed="true" %}}
Được. Bắt đầu máy chủ FTP trên iPhone thứ nhất. Trên chiếc thứ hai, mở Everdisk, vào thẻ Thiết bị, chạm Kết nối mới, chọn FTP, và nhập địa chỉ hiển thị trên điện thoại thứ nhất. Một ứng dụng FTP chuyên dụng cho iOS cũng dùng được, vì ứng dụng Tệp của iOS không có sẵn máy khách FTP.
{{% /details %}}

{{% details title="FTP có an toàn không?" closed="true" %}}
FTP thuần không mã hóa lưu lượng của nó, nên hãy xem nó như một công cụ cho các mạng bạn tin tưởng, như Wi-Fi ở nhà. Trên một mạng bạn không kiểm soát, hãy dùng máy chủ SMB với Yêu cầu mã hóa SMB bật lên, vốn bảo vệ mọi lần truyền.
{{% /details %}}

{{% details title="Những thiết bị nào có thể kết nối qua FTP?" closed="true" %}}
Gần như bất cứ thứ gì có một máy khách FTP. Điều đó bao gồm máy tính Mac, Windows và Linux, các ứng dụng FTP như FileZilla và Cyberduck, các trình quản lý tập tin Android, cùng phần cứng như máy ảnh, smart TV, router, hộp NAS và công cụ tự động hóa. Khả năng chạm tới rộng khắp đó chính là lý do chính để chọn FTP.
{{% /details %}}

{{% details title="Vì sao kết nối FTP của tôi bị rớt?" closed="true" %}}
iPhone của bạn là máy chủ, và iOS tạm dừng các ứng dụng nằm ở nền quá lâu. Giữ Everdisk mở trên màn hình trong lúc một thiết bị đang kết nối, và cắm nguồn điện cho những lần truyền dài. Cũng hãy đảm bảo cả hai thiết bị vẫn ở cùng mạng Wi-Fi.
{{% /details %}}

{{% details title="Everdisk có miễn phí không?" closed="true" %}}
Có, Everdisk tải miễn phí và máy chủ FTP được bao gồm sẵn. Một gói mua Premium một lần duy nhất tùy chọn thêm các tính năng bổ sung như cổng tùy chỉnh cùng chuyển đổi ảnh và video. Bạn có thể thiết lập FTP và truyền tập tin mà không phải trả tiền.
{{% /details %}}

Sẵn sàng thử chưa? [Tải Everdisk từ App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) và kết nối máy khách FTP đầu tiên chỉ trong vài phút. Có câu hỏi hay góp ý? Gửi email cho chúng tôi tại **support@everappz.com**.
