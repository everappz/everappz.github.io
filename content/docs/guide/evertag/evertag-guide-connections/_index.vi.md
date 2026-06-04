---
title: "Kết nối"
date: 2020-02-01
description: "Tìm hiểu cách kết nối bộ nhớ đám mây, NAS và máy tính với Evertag. Truy cập và chỉnh sửa tệp âm thanh trực tiếp từ bộ nhớ đám mây, NAS cá nhân hoặc Mac/PC."
keywords: [
  "thiết lập đám mây Evertag", "kết nối iCloud với Evertag", "truy cập tệp SMB iOS",
  "trình chỉnh sửa thẻ âm thanh WebDAV", "chỉnh sửa siêu dữ liệu NAS", "Wi-Fi Drive Evertag",
  "truyền tệp âm thanh lên iPhone", "Evertag iTunes File Sharing", "chỉnh sửa thẻ FLAC từ đám mây"
]
tags: ["hướng dẫn", "evertag", "kết nối"]
readingTime: 11
---


Trên màn hình này, bạn có thể kết nối các nguồn chứa tệp âm thanh của mình. Bạn có thể tích hợp các dịch vụ đám mây phổ biến như Google Drive, Dropbox, OneDrive, iCloud và nhiều dịch vụ khác, cũng như kết nối Mac hoặc PC. Ngoài ra, bạn có thể chỉnh sửa các tệp âm thanh trên Apple Time Capsule, WD Cloud Home hoặc bất kỳ NAS nào hỗ trợ SMB hoặc WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Connections Screen" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Truy cập nhanh

Ở đầu màn hình Kết nối, bạn sẽ thấy danh sách **Truy cập nhanh**. Bất kỳ thư mục đám mây nào bạn thêm vào yêu thích — dù nằm sâu nhiều cấp — đều xuất hiện ở đây để bạn có thể truy cập ngay mà không cần điều hướng qua các thư mục gốc.

## Kết nối với bộ nhớ đám mây

- Mở tab «Kết nối»  
- Chọn «Kết nối với bộ nhớ đám mây» từ menu  
- Chọn dịch vụ lưu trữ đám mây từ danh sách  
- Nhập thông tin đăng nhập và nhấn «Hoàn tất».

Nếu gặp sự cố, hãy kiểm tra kết nối internet và tên đăng nhập/mật khẩu.  
Trong phiên bản Premium, bạn có thể thêm số lượng dịch vụ không giới hạn.

## Các dịch vụ lưu trữ đám mây được hỗ trợ

Hiện tại, ứng dụng hỗ trợ các dịch vụ lưu trữ đám mây phổ biến nhất: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), cũng như bất kỳ máy chủ SMB hoặc WebDAV nào.

## Bảo mật và quyền riêng tư

Chúng tôi chỉ sử dụng SDK chính thức và kết nối bảo mật để tương tác với các dịch vụ đám mây được kết nối. Tên đăng nhập và mật khẩu của bạn không thể được ứng dụng truy cập. Tất cả các yêu cầu từ ứng dụng đến dịch vụ đám mây đều được mã hóa.

Khi bạn nhập thông tin đăng nhập, ứng dụng hiển thị trang ủy quyền chính thức do nhà cung cấp dịch vụ đám mây cung cấp, và toàn bộ quá trình ủy quyền diễn ra bên ngoài ứng dụng. Nhà cung cấp dịch vụ đám mây gửi token ủy quyền cho ứng dụng sau khi ủy quyền thành công, và token đó được dùng để thực hiện các lệnh gọi API.

Token ủy quyền là khóa kỹ thuật số cho phép các ứng dụng bên thứ ba tương tác với bộ nhớ đám mây. Token được lưu trữ trên thiết bị của bạn trong bộ lưu trữ hệ thống bảo mật gọi là Keychain. Bạn có thể tải tệp từ dịch vụ đám mây đã kết nối về thiết bị, và các tệp đó sẽ được đặt trong thư mục «Tài liệu» của ứng dụng. Bạn có thể xóa các tệp đó bất kỳ lúc nào bằng trình quản lý tệp tích hợp.

Ứng dụng không chia sẻ bất kỳ thông tin nào từ tài khoản đám mây đã kết nối. Bạn có thể thu hồi quyền truy cập vào tài khoản đám mây của mình bất kỳ lúc nào bằng cách mở trang cài đặt tài khoản trong trình duyệt web.

## Thu hồi token ủy quyền

Đăng nhập vào tài khoản của bạn trong trình duyệt web và điều hướng đến trang cài đặt. Ở đó, bạn có thể tìm thấy tất cả các ứng dụng bên thứ ba được kết nối với tài khoản đám mây của mình và xóa bất kỳ ứng dụng nào nếu không muốn sử dụng nữa. Hướng dẫn chi tiết có sẵn [tại đây](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Bạn cũng có thể ngắt kết nối các tài khoản đám mây trong ứng dụng, và token ủy quyền cũng sẽ bị xóa khỏi thiết bị. Nếu bạn xóa ứng dụng khỏi thiết bị, tất cả dữ liệu đã tải xuống và token truy cập cũng sẽ bị xóa.

## Ngắt kết nối bộ nhớ đám mây hoặc thay đổi cấu hình

- Tìm bộ nhớ đám mây bạn muốn quản lý trong giao diện ứng dụng.  
- Nhấn nút «...» bên cạnh tiêu đề dịch vụ để truy cập các tùy chọn bổ sung.  
  - **Đổi tên**: thay đổi tên hiển thị của dịch vụ đám mây trong danh sách.  
  - **Cài đặt**: sửa đổi cấu hình hoặc dữ liệu xác thực cho dịch vụ đám mây. Đôi khi bạn có thể cần ủy quyền lại nếu token hết hạn.  
  - **Ngắt kết nối**: hoàn toàn ngắt kết nối giữa ứng dụng và dịch vụ đám mây. Lưu ý rằng thao tác này sẽ xóa tất cả bài hát liên quan đến dịch vụ này khỏi thư viện nhạc trong ứng dụng, nhưng chúng vẫn còn trên máy chủ.

## Kết nối với máy tính hoặc NAS

Bạn cũng có thể kết nối máy tính, NAS cá nhân hoặc các thiết bị mạng khác bằng giao thức SMB, DLNA hoặc WebDAV.

## Kết nối với máy tính qua SMB

- Nhấn «Kết nối với bộ nhớ đám mây» → SMB.  
- Nhập địa chỉ IP máy tính và tên thư mục chia sẻ vào trường URL theo định dạng smb://computer-ip-address/shared-folder-name  
- Chọn phiên bản giao thức: Auto, SMB1, SMB2  
- Nhập tên đăng nhập và mật khẩu (nếu cần)  
- Nhấn «Hoàn tất».

Nếu kết nối thành công, bộ nhớ đã kết nối sẽ xuất hiện trong phần «Bộ nhớ đám mây».  
Hướng dẫn đầy đủ về cách kết nối Mac hoặc PC qua SMB có sẵn [tại đây](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Kết nối với NAS qua WebDAV

Tất cả các bước đều giống nhau ngoại trừ trường URL.  
URL phải có định dạng http://server-name hoặc https://server-name nếu máy chủ hỗ trợ SSL.  
Hướng dẫn đầy đủ về cách kết nối NAS bằng giao thức WebDAV có sẵn [tại đây](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Thiết bị có sẵn

Phần này hiển thị tất cả các thiết bị trong mạng cục bộ của bạn mà bạn có thể kết nối thông qua ứng dụng.  
Để thiết lập kết nối với một thiết bị, hãy làm theo các bước sau:

- Mở ứng dụng và đi đến phần «Thiết bị có sẵn».  
- Nhấn vào thiết bị bạn muốn kết nối từ danh sách.  
- Nếu cần, nhập thông tin đăng nhập để hoàn tất kết nối.

## Wi-Fi Drive

Wi-Fi Drive là công nghệ tiện lợi cho phép truyền tệp không dây từ máy tính đến thiết bị iOS qua trình duyệt trên máy tính.  
Để sử dụng tính năng này hiệu quả, hãy đảm bảo thiết bị và máy tính được kết nối cùng một mạng Wi-Fi.  
Dưới đây là hướng dẫn từng bước về cách sử dụng Wi-Fi Drive.

## Bật Wi-Fi Drive

- Mở ứng dụng và đi đến tab «Kết nối».  
- Chọn «Kết nối qua Wi-Fi» để truy cập màn hình chính của Wi-Fi Drive.  
- Nhấn «Khởi động Wi-Fi Drive» để bật Wi-Fi Drive.

## Truy cập Wi-Fi Drive trên máy tính

- Trên máy tính (để bàn hoặc laptop), mở trình duyệt web (Chrome, Firefox hoặc Safari).  
- Trong thanh địa chỉ của trình duyệt, nhập URL do ứng dụng cung cấp.

## Truyền tệp không dây

Sau khi trang web tương ứng với thiết bị iOS của bạn mở trong trình duyệt, bạn có thể dễ dàng kéo và thả tệp từ máy tính lên trang web.  
Các tệp bạn kéo và thả sẽ bắt đầu truyền đến thiết bị iOS và có thể truy cập trong ứng dụng.

Hướng dẫn chi tiết về cách truyền tệp không dây bằng Wi-Fi Drive có sẵn [tại đây](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing là một công nghệ khác cho phép bạn truyền tệp từ máy tính đến thiết bị bằng ứng dụng Finder trên Mac và cáp Lightning.  
- Chỉ cần kết nối thiết bị với máy tính bằng cáp và chạy ứng dụng Finder trên Mac.  
- Mở «Vị trí» → «Thiết bị đã kết nối của bạn» → «Tệp» → và tìm ứng dụng hiện tại.  
- Nhấn vào biểu tượng ứng dụng để xem tất cả các thư mục chia sẻ.  
- Sao chép tệp từ máy tính vào thư mục chia sẻ trên thiết bị bằng cách kéo và thả.

Hướng dẫn chi tiết về cách sử dụng iTunes File Sharing có sẵn [tại đây](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Kết nối USB flash

Nếu bạn có thẻ SD hoặc USB flash, bạn có thể kết nối bằng đầu đọc thẻ Lightning hoặc USB-C trên iPhone/iPad, hoặc cắm trực tiếp vào Mac. Ứng dụng hiện hỗ trợ đầu đọc thẻ được Apple chứng nhận. Chúng tôi có hướng dẫn chi tiết về cách kết nối USB flash với iPhone hoặc iPad và quản lý tệp trên đó, có sẵn [tại đây](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Các ổ đĩa đã kết nối xuất hiện trong phần **Phụ kiện kết nối** của màn hình Kết nối.

## Trình quản lý tệp

Sau khi kết nối dịch vụ lưu trữ đám mây, nhấn vào biểu tượng của nó để xem tất cả các tệp và thư mục có sẵn. Bạn có thể sử dụng trình quản lý tệp tích hợp để làm việc với các tệp này — tải xuống, đổi tên, di chuyển và nhiều thao tác khác. Khi bắt đầu tải xuống, tệp sẽ xuất hiện trong hàng đợi chuyển. Để xem hàng đợi chuyển, đi đến tab «Tệp cục bộ» và nhấn vào biểu tượng mũi tên quay tròn ở góc trên bên trái. Tất cả các tệp và thư mục đã tải xuống đều có sẵn trong phần «Tệp cục bộ».

## Thanh công cụ trên cùng

Thanh công cụ trên cùng, nằm ngay dưới thanh điều hướng, cung cấp một số hành động hữu ích để truy cập nhanh. Bạn có thể hiển thị hoặc ẩn thanh công cụ này bằng cách vuốt xuống. Các hành động có sẵn:

- **Tìm kiếm**: tìm kiếm nhanh trong thư mục hiện tại để dễ dàng tìm các tệp hoặc thư mục cụ thể.  

## Tùy chọn thư mục

Khi bạn mở một thư mục trong ứng dụng, bạn sẽ thấy các hành động khi nhấn nút «...» ở góc trên bên phải màn hình.  
Các hành động có sẵn:

- **Chọn**: kích hoạt chế độ chọn tệp để chọn một hoặc nhiều tệp trong thư mục.  
- **Thư mục mới**: tạo thư mục mới trong thư mục hiện tại để tổ chức tệp.  
- **Tải lên tệp**: tải tệp từ thiết bị lên thư mục trực tuyến.  
- **Tìm kiếm**: tìm kiếm tệp cụ thể trong thư mục hiện tại.  
- **Sắp xếp**: sắp xếp tệp trong thư mục theo tên, kích thước hoặc ngày chỉnh sửa.  
- **Lưới/Danh sách**: chuyển đổi giữa hai chế độ xem: dạng bảng và dạng hình thu nhỏ.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Cloud Folder Sort" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Chỉnh sửa tệp trực tuyến

Khi cần quản lý nhiều tệp trong bộ nhớ đám mây, bạn có thể sử dụng chế độ chọn để đơn giản hóa các hành động. Các bước thực hiện:

- **Kích hoạt chế độ chọn**: mở ứng dụng và điều hướng đến phần chứa bộ nhớ đám mây. Nhấn nút «...» ở góc trên bên phải và chọn mục menu «Chọn».  
- **Chọn tệp**: hộp kiểm sẽ xuất hiện bên cạnh mỗi tệp hoặc thư mục. Chọn một hoặc nhiều tệp hoặc thư mục.  
- **Thực hiện các hành động**: sau khi chọn tệp hoặc thư mục, bạn sẽ có quyền truy cập vào nhiều hành động.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Select" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Hành động với tệp

Gần tiêu đề tệp, bạn sẽ thấy ký hiệu «...» (ba chấm) — đây là menu hành động.  
Nhấn vào để xem danh sách các hành động có sẵn:

- **Chỉnh sửa thẻ âm thanh**: truy cập trình chỉnh sửa thẻ tích hợp để chỉnh sửa thẻ âm thanh cho tệp đã chọn. Tệp sẽ được tải xuống tạm thời vào thư mục tạm và sau đó được tải lên bộ nhớ sau khi bạn xác nhận các thay đổi.  
- **Thêm vào yêu thích**: thêm tệp vào danh sách yêu thích để truy cập nhanh.  
- **Tải xuống**: tải tệp hoặc thư mục về thiết bị để sử dụng ngoại tuyến.  
- **Đổi tên**: đổi tên tệp trực tiếp trên bộ nhớ từ xa.  
- **Di chuyển**: di chuyển tệp đến thư mục khác trong bộ nhớ đám mây.  
- **Mở trong**: xuất tệp sang ứng dụng tương thích khác. Tệp sẽ được tải xuống thiết bị, sau đó hộp thoại Chia sẻ sẽ xuất hiện.  
- **Xóa**: thao tác này xóa vĩnh viễn tệp khỏi bộ nhớ đám mây. **Không thể hoàn tác thao tác xóa này**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Options" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Nếu danh sách hành động vượt quá không gian màn hình, hãy cuộn xuống trong menu hành động để xem thêm tùy chọn.

## Hành động với thư mục

Đối với mỗi thư mục trong bộ nhớ đám mây, bạn có nhiều hành động khác nhau. Nhấn biểu tượng «...» bên cạnh tiêu đề thư mục. Nếu không thấy tất cả hành động, hãy cuộn xuống. Các hành động có sẵn:

- **Thêm vào yêu thích**: thêm thư mục vào danh sách yêu thích để truy cập nhanh.  
- **Tải xuống**: tải xuống toàn bộ nội dung thư mục về thiết bị để truy cập ngoại tuyến.  
- **Đổi tên**: đổi tên thư mục trực tiếp trên bộ nhớ từ xa.  
- **Di chuyển**: di chuyển thư mục đến vị trí khác trong bộ nhớ đám mây.  
- **Xóa**: thao tác này xóa vĩnh viễn thư mục và nội dung của nó khỏi bộ nhớ đám mây. **Không thể hoàn tác thao tác này**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Folder Options" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
