---
title: "Cách thiết lập máy chủ SMB trên iPhone và iPad để chia sẻ tập tin"
description: "Biến iPhone hoặc iPad thành máy chủ tập tin SMB với Everdisk và mở nó như một ổ đĩa mạng từ Mac, một iPhone khác, Linux hoặc Android qua Wi-Fi. Hướng dẫn thiết lập đầy đủ, địa chỉ smb và cổng, mã hóa SMB3 tùy chọn, cùng cách kết nối từng bước cho mọi thiết bị."
date: 2026-09-19
tags: ["everdisk", "smb", "chia sẻ tập tin", "ổ đĩa mạng", "iphone", "ipad", "mac", "finder", "mã hóa", "wifi"]
keywords: ["máy chủ SMB iPhone", "máy chủ SMB iPad", "cách thiết lập SMB trên iPhone", "chia sẻ SMB iPhone", "kết nối iPhone SMB Mac Finder", "smb iphone sang iphone", "ứng dụng Tệp iOS kết nối máy chủ SMB", "chia sẻ tập tin iPhone SMB", "ổ đĩa mạng iphone Finder", "mã hóa SMB3 iOS", "chia sẻ smb iPhone Android", "kết nối SMB từ Linux", "iphone làm ổ đĩa mạng", "chia sẻ tập tin giữa các iphone wifi", "ánh xạ iphone làm ổ đĩa mạng"]
readingTime: 10
---

{{< author-byline >}}

SMB là cơ chế chia sẻ tập tin tích hợp sẵn trong macOS, Windows và Linux, cùng gần như mọi ổ đĩa mạng (NAS). Khi bạn kết nối tới một thư mục chia sẻ trên một máy tính khác và nó mở ra như một ổ đĩa bình thường trong Finder hay File Explorer, đó chính là SMB đang làm việc. Với [Everdisk](/products/everdisk) bạn có thể đặt một thư mục chia sẻ SMB lên iPhone hoặc iPad, để chính chiếc điện thoại hiện ra như một ổ đĩa mạng mà các thiết bị khác duyệt, sao chép về và sao chép sang.

Đây là tùy chọn bạn nên chọn khi muốn iPhone hoạt động như một ổ đĩa thực thụ, chứ không phải một trang web. Nó nhanh, kéo thả được cả hai chiều, và là kiểu kết nối duy nhất trong Everdisk có thể mã hóa mọi lần truyền. Hướng dẫn này bao quát phần thiết lập cùng cách kết nối từ Mac, một iPhone hoặc iPad khác, Linux, Android và Windows.

## Bạn cần những gì

- Một iPhone hoặc iPad đã cài [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Một thiết bị khác trong **cùng mạng Wi-Fi**.
- Tập tin bạn muốn chia sẻ, nằm trong thư mục Tài liệu của Everdisk hoặc trong các thư mục bạn thêm vào.

## Thiết lập máy chủ SMB trong Everdisk

### Bước 1: Chọn thứ cần chia sẻ và ai được ghi

Mở Everdisk, vào thẻ **Chia sẻ**, và chạm **Chia sẻ gì**. Thư mục Tài liệu được chia sẻ mặc định. Thêm nữa bằng **Thêm thư mục** và **Thêm tệp**, và bật thư viện Ảnh hoặc Nhạc nếu bạn cũng muốn chúng sẵn sàng.

Quyết định xem các thiết bị khác chỉ được đọc tập tin của bạn, hay còn được thay đổi chúng. Mở **Cài đặt**, rồi **Chia sẻ**, rồi **Truy cập**, và đặt **Chỉnh sửa tệp**. Khi bật, thiết bị đã kết nối có thể sao chép tập tin vào điện thoại của bạn cùng đổi tên hoặc xóa. Khi tắt, thư mục chia sẻ chỉ để đọc.

Nếu bạn muốn một phần đăng nhập, hãy đặt **Tên đăng nhập** và **Mật khẩu** trên cùng màn hình Truy cập đó. Để trống cả hai để cho phép truy cập khách.

### Bước 2: Bật máy chủ SMB

Vào **Cài đặt**, rồi **Chia sẻ**, rồi **Kết nối**, và bật **Máy tính (Nâng cao)**. Đó là máy chủ SMB (nó mang nhãn SMB).

### Bước 3: Bắt đầu chia sẻ và ghi lại địa chỉ

Trở lại thẻ **Chia sẻ** và chạm **Bắt đầu**. Phần **Cách kết nối** giờ hiển thị địa chỉ SMB. Nó trông như thế này:

```
smb://192.168.1.20:4455/Share
```

Ba điều cần biết về địa chỉ đó:

- Con số sau dấu hai chấm là **cổng**. Everdisk dùng **4455** theo mặc định.
- Thư mục chia sẻ có tên là **Share**.
- Phần đầu là địa chỉ của iPhone trên Wi-Fi, nên nó sẽ khác trên mạng của bạn.

Giữ Everdisk mở trong lúc các thiết bị đang kết nối, vì iOS tạm dừng các ứng dụng nằm ở nền quá lâu.

## Kết nối từ Mac

Đây là trường hợp mượt mà nhất, vì macOS nói SMB một cách tự nhiên.

Cách nhanh nhất: mở **Finder** và nhìn vào thanh bên dưới mục **Locations** hoặc **Network**. Everdisk tự thông báo mình trên Wi-Fi, nên iPhone của bạn thường tự hiện ra ở đó. Nhấp vào nó, rồi nhấp **Connect As** và chọn **Guest**, hoặc nhập tên đăng nhập của bạn.

Để kết nối bằng tay:

1. Trong Finder, chọn **Go**, rồi **Connect to Server** (hoặc nhấn **Command và K**).
2. Gõ địa chỉ SMB hiển thị trong Everdisk, ví dụ `smb://192.168.1.20:4455/Share`.
3. Nhấp **Connect**, rồi chọn **Guest** hoặc nhập **Tên đăng nhập** và **Mật khẩu** của bạn.

iPhone của bạn mở ra trong một cửa sổ Finder. Sao chép tập tin vào hoặc ra bằng cách kéo, giống hệt bất kỳ ổ đĩa nào khác (nếu Chỉnh sửa tệp đang bật).

## Kết nối từ một iPhone hoặc iPad khác

iOS và iPadOS có thể mở các thư mục chia sẻ SMB trong ứng dụng **Tệp** tích hợp, giúp việc truyền giữa hai điện thoại gọn gàng và nhanh chóng.

Trên thiết bị thứ hai:

1. Mở ứng dụng **Tệp**.
2. Chạm nút **thêm** (ba chấm, góc trên bên phải trên iPhone) và chọn **Kết nối tới Máy chủ**.
3. Nhập địa chỉ SMB từ Everdisk, ví dụ `smb://192.168.1.20:4455/Share`.
4. Chọn **Khách**, hoặc **Người dùng đã đăng ký** và nhập tên đăng nhập của bạn.
5. Thư mục chia sẻ hiện ra dưới mục Vị trí trong Tệp. Duyệt và sao chép theo cả hai chiều.

Bạn cũng có thể dùng chính thẻ **Thiết bị** của Everdisk trên thiết bị thứ hai, vốn có sẵn một máy khách SMB. Mở Everdisk, vào **Thiết bị**, chạm **Kết nối mới**, chọn **SMB**, và nhập địa chỉ.

## Kết nối từ Linux

1. Mở trình quản lý tập tin của bạn (Files/Nautilus trên GNOME, Dolphin trên KDE).
2. Chọn **Other Locations** hoặc **Connect to Server**.
3. Nhập địa chỉ, ví dụ `smb://192.168.1.20:4455/Share`.
4. Kết nối với tư cách khách, hoặc nhập tên đăng nhập của bạn.

Từ một terminal bạn cũng có thể chạy `smbclient //192.168.1.20/Share -p 4455` và nhập tên đăng nhập khi được hỏi.

## Kết nối từ Android

Android không có trình duyệt SMB hệ thống, nên hãy dùng một trình quản lý tập tin có hỗ trợ SMB:

1. Cài một ứng dụng như **CX File Explorer**, **Solid Explorer**, hoặc **X-plore File Manager**.
2. Thêm một kết nối **SMB** hoặc **LAN** mới.
3. Nhập máy chủ (địa chỉ Wi-Fi của iPhone), đặt **cổng thành 4455**, và tên thư mục chia sẻ **Share**.
4. Kết nối với tư cách khách hoặc bằng tên đăng nhập của bạn, rồi duyệt và sao chép.

## Kết nối từ Windows

Windows có thể đọc các thư mục chia sẻ SMB, với một điểm lưu ý đáng biết trước. File Explorer tích hợp chỉ nói SMB trên cổng chuẩn và không cho bạn gõ cổng tùy chỉnh vào đường dẫn, còn Everdisk dùng cổng 4455. Nên cách **Ánh xạ ổ đĩa mạng** thông thường thường sẽ không chạm tới được.

Bạn có hai lựa chọn tốt trên Windows:

- Dùng một trình quản lý tập tin hoặc máy khách SMB cho phép đặt cổng tùy chỉnh, và trỏ nó tới địa chỉ của iPhone với cổng **4455** và tên thư mục chia sẻ **Share**.
- Hoặc kết nối từ Windows bằng một trong các máy chủ khác của Everdisk thay thế. Cả [thiết lập WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) lẫn [thiết lập FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) đều hoạt động tốt từ Windows File Explorer, và liên kết trình duyệt chạy được trong mọi trình duyệt.

Nếu bạn vẫn muốn thử Ánh xạ ổ đĩa mạng: mở **File Explorer**, nhấp chuột phải vào **This PC**, chọn **Map network drive**, và nhập máy chủ cùng tên thư mục chia sẻ hiển thị trong Everdisk. Nếu nó không kết nối được, đó là giới hạn cổng nói ở trên, nên hãy chuyển sang WebDAV hoặc FTP.

## Bật mã hóa cho Wi-Fi không đáng tin

SMB là kết nối Everdisk duy nhất có thể mã hóa mọi lần truyền, điều quan trọng trên mạng Wi-Fi bạn không hoàn toàn kiểm soát, như một quán cà phê hay một mạng văn phòng.

1. Trong **Cài đặt**, **Chia sẻ**, **Truy cập**, đặt **Tên đăng nhập** và **Mật khẩu**. Kết nối có mã hóa không thể ẩn danh, nên bước này là bắt buộc.
2. Trong **Cài đặt**, **Chia sẻ**, bật **Yêu cầu mã hóa SMB**.
3. Dừng rồi bắt đầu chia sẻ lại để thay đổi có hiệu lực.

Mọi lần truyền SMB khi đó được bảo vệ bằng **mã hóa SMB3 (AES)**. Thiết bị kết nối cần hỗ trợ SMB3, điều mà Finder trên một chiếc Mac hiện đại và Windows 10 trở lên đều làm được. Mã hóa SMB là một phần của gói mua Premium một lần duy nhất.

## Chỉ đọc hoặc đọc và ghi

Công tắc **Chỉnh sửa tệp** trong Cài đặt, Chia sẻ, Truy cập kiểm soát điều này cho mọi máy chủ, bao gồm cả SMB. Bật nó và thiết bị đã kết nối có thể tải lên, đổi tên và xóa. Tắt nó và họ chỉ có thể duyệt và sao chép tập tin ra khỏi điện thoại của bạn. Hãy chọn chỉ đọc khi bạn trao tập tin cho ai đó mà bạn không muốn họ thay đổi bất cứ thứ gì.

## Những cách người ta dùng thực tế

- **Chuyển một thư mục lớn vào iPhone từ Mac** bằng cách kéo nó vào cửa sổ Finder, nhanh hơn tải lên qua web.
- **Lấy một ngày ảnh và video khỏi điện thoại** sang laptop mà không cần iTunes hay cáp.
- **Gửi tập tin giữa hai iPhone** qua ứng dụng Tệp, không cần ứng dụng thứ ba ở bên nào.
- **Làm việc với một tập tin tại chỗ**, mở một tài liệu thẳng từ điện thoại trong một ứng dụng trên Mac của bạn và lưu ngược lại.

## Một vài mẹo nhỏ

- Giữ Everdisk mở trong lúc một thiết bị đang kết nối. Khóa điện thoại quá lâu có thể tạm dừng ứng dụng và làm rớt kết nối.
- Nếu một chiếc Mac không thấy điện thoại trong thanh bên Finder, hãy kết nối bằng tay với Connect to Server và địa chỉ smb đầy đủ.
- Để có tốc độ tốt nhất khi truyền lớn, giữ chất lượng ảnh và video ở Bản gốc trong Cài đặt.
- Trên một mạng không đáng tin, hãy bật Yêu cầu mã hóa SMB và tắt các máy chủ khác trong lúc bạn làm việc.

## Câu hỏi thường gặp

{{% details title="Địa chỉ và cổng SMB cho iPhone của tôi là gì?" closed="true" %}}
Sau khi bạn bắt đầu chia sẻ, Everdisk hiển thị địa chỉ trên màn hình Chia sẻ. Nó trông như smb://192.168.1.20:4455/Share. Con số 4455 là cổng Everdisk dùng cho SMB, và Share là tên thư mục chia sẻ. Phần đầu là địa chỉ của iPhone trên Wi-Fi, nên của bạn sẽ khác.
{{% /details %}}

{{% details title="Tôi có thể kết nối tới thư mục chia sẻ SMB của iPhone từ Windows không?" closed="true" %}}
Windows File Explorer chỉ kết nối SMB trên cổng chuẩn và không chấp nhận cổng tùy chỉnh trong đường dẫn, trong khi Everdisk dùng cổng 4455. Nên cách Ánh xạ ổ đĩa mạng thông thường thường sẽ không chạm tới được. Hãy dùng một trình quản lý tập tin cho phép đặt cổng tùy chỉnh, hoặc kết nối từ Windows bằng WebDAV, FTP hay liên kết trình duyệt thay thế. Tất cả những cách đó đều hoạt động từ Windows mà không gặp rắc rối về cổng.
{{% /details %}}

{{% details title="Làm sao để chia sẻ tập tin giữa hai iPhone bằng SMB?" closed="true" %}}
Bắt đầu máy chủ SMB trên iPhone thứ nhất trong Everdisk. Trên iPhone thứ hai, mở ứng dụng Tệp, chạm nút thêm, chọn Kết nối tới Máy chủ, và nhập địa chỉ smb hiển thị trong Everdisk (ví dụ smb://192.168.1.20:4455/Share). Kết nối với tư cách Khách hoặc bằng tên đăng nhập của bạn, và thư mục chia sẻ hiện ra trong Tệp. Bạn cũng có thể dùng chính thẻ Thiết bị của Everdisk trên điện thoại thứ hai.
{{% /details %}}

{{% details title="iPhone của tôi có tự hiện trong thanh bên Finder của Mac không?" closed="true" %}}
Thường là có. Everdisk thông báo thư mục chia sẻ SMB trên Wi-Fi của bạn, nên iPhone của bạn thường hiện ra dưới mục Locations hoặc Network trong thanh bên Finder. Nhấp vào nó và chọn Connect As, rồi Guest hoặc tên đăng nhập của bạn. Nếu nó không hiện ra, hãy kết nối bằng tay với Go, Connect to Server và địa chỉ smb đầy đủ.
{{% /details %}}

{{% details title="Tôi có cần mật khẩu để dùng SMB không?" closed="true" %}}
Không, tên đăng nhập là tùy chọn. Để trống Tên đăng nhập và Mật khẩu trong Cài đặt, Chia sẻ, Truy cập để cho phép truy cập khách. Đặt chúng nếu bạn muốn các kết nối phải đăng nhập. Tên đăng nhập và mật khẩu chỉ bắt buộc nếu bạn bật Yêu cầu mã hóa SMB, vì kết nối có mã hóa không thể ẩn danh.
{{% /details %}}

{{% details title="Kết nối SMB có được mã hóa không?" closed="true" %}}
Có thể. SMB là kết nối Everdisk duy nhất hỗ trợ mã hóa. Đặt tên đăng nhập và mật khẩu, rồi bật Yêu cầu mã hóa SMB trong Cài đặt, Chia sẻ. Mọi lần truyền khi đó được bảo vệ bằng SMB3 (AES). Thiết bị kia cần hỗ trợ SMB3, điều mà các máy Mac hiện đại và Windows 10 trở lên đều làm được. Mã hóa là tính năng Premium.
{{% /details %}}

{{% details title="Người khác có thể thay đổi hoặc xóa tập tin của tôi qua SMB không?" closed="true" %}}
Chỉ khi bạn cho phép. Công tắc Chỉnh sửa tệp trong Cài đặt, Chia sẻ, Truy cập kiểm soát điều này. Khi bật, thiết bị đã kết nối có thể tải lên, đổi tên và xóa. Khi tắt, thư mục chia sẻ chỉ để đọc và người khác có thể duyệt cùng sao chép tập tin ra khỏi điện thoại của bạn nhưng không thể thay đổi gì.
{{% /details %}}

{{% details title="Vì sao kết nối SMB của tôi bị rớt?" closed="true" %}}
iPhone của bạn là máy chủ, và iOS tạm dừng các ứng dụng nằm ở nền quá lâu. Giữ Everdisk mở trên màn hình trong lúc một thiết bị đang kết nối, và cắm điện thoại vào nguồn điện trong những lần truyền dài. Cũng hãy đảm bảo cả hai thiết bị vẫn ở cùng mạng Wi-Fi.
{{% /details %}}

{{% details title="SMB, WebDAV hay FTP, tôi nên dùng cái nào?" closed="true" %}}
Dùng SMB khi bạn muốn điện thoại hoạt động như một ổ đĩa mạng thực thụ trên Mac, một iPhone khác, Linux hay một NAS, và khi bạn muốn mã hóa. Dùng WebDAV khi bạn muốn một ổ đĩa mạng cũng hoạt động tốt từ Windows. Dùng FTP để tương thích rộng nhất với các thiết bị và ứng dụng cũ. Everdisk có thể chạy tất cả cùng lúc, nên bạn không bị khóa vào một cái.
{{% /details %}}

{{% details title="Everdisk có miễn phí không?" closed="true" %}}
Có, Everdisk tải miễn phí và máy chủ SMB được bao gồm sẵn. Gói mua Premium một lần duy nhất tùy chọn thêm mã hóa SMB, cổng tùy chỉnh cùng vài tính năng bổ sung khác. Bạn có thể thiết lập SMB và chia sẻ tập tin mà không phải trả tiền.
{{% /details %}}

Sẵn sàng thử chưa? [Tải Everdisk từ App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) và mở iPhone của bạn trong Finder chỉ trong khoảng một phút. Có câu hỏi hay góp ý? Gửi email cho chúng tôi tại **support@everappz.com**.
