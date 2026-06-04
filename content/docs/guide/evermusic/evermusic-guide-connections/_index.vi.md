---
title: "Kết nối"
date: 2020-01-01
description: "Tìm hiểu cách kết nối dịch vụ đám mây, máy tính, thiết bị NAS và quản lý tệp nhạc bằng Evermusic. Hướng dẫn từng bước về Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes File Sharing và nhiều hơn nữa."
keywords: [
  "Evermusic", "trình phát nhạc đám mây", "phát NAS", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes File Sharing",
  "kết nối lưu trữ đám mây", "truyền nhạc iPhone", "trình quản lý tệp iOS"
]
tags: ["evermusic", "hướng dẫn", "kết nối"]
readingTime: 11
---


Trên màn hình Kết nối bạn có thể kết nối mọi nguồn chứa nhạc của bạn — dịch vụ đám mây phổ biến, máy chủ đa phương tiện tự lưu trữ, Mac hoặc PC, NAS cá nhân, Apple Time Capsule, WD My Cloud Home, thậm chí USB flash drive — và sử dụng tất cả chúng từ một giao diện thống nhất. Kết nối cũng là nơi bạn thiết lập Truy cập nhanh đến các thư mục đám mây sâu và nơi bạn xác thực Last.fm để scrobbling.

Màn hình được chia thành các phần được đánh nhãn rõ ràng: Truy cập nhanh ở trên cùng (thư mục đám mây yêu thích của bạn), Lưu trữ đám mây (các tài khoản đã thêm), Mạng cục bộ (thiết bị được Bonjour phát hiện), Máy tính (Wi-Fi Drive, iTunes File Sharing, SMB), Phụ kiện ngoài (USB flash drive đã kết nối), và Dịch vụ khác (Last.fm và tương tự).

{{< cards cols="1">}}
  {{< card title="" subtitle="Màn hình Kết nối Evermusic" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Kết nối lưu trữ đám mây

- Mở tab Kết nối.
- Chọn Kết nối lưu trữ đám mây từ menu.
- Chọn dịch vụ lưu trữ đám mây từ danh sách.
- Đăng nhập trên trang ủy quyền chính thức của nhà cung cấp (Evermusic không bao giờ thấy mật khẩu của bạn).
- Nhấn Hoàn tất.

{{< cards cols="1">}}
  {{< card title="" subtitle="Bộ chọn nhà cung cấp lưu trữ đám mây" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Nếu gặp sự cố, hãy kiểm tra kết nối internet và thông tin đăng nhập, đồng thời đảm bảo xác thực hai yếu tố được cấu hình đúng cho dịch vụ đó.  
Trong phiên bản Premium của ứng dụng, bạn có thể thêm số lượng dịch vụ không giới hạn. Người dùng miễn phí chỉ có thể kết nối một tài khoản đám mây tại một thời điểm.

## Dịch vụ lưu trữ đám mây được hỗ trợ

Evermusic hỗ trợ đầy đủ các dịch vụ đám mây và tự lưu trữ phổ biến. Người dùng miễn phí có cùng danh mục nhà cung cấp nhưng với giới hạn một tài khoản; Premium mở khóa tài khoản không giới hạn và xóa hầu hết các giới hạn khác.

- **Tài khoản đám mây cá nhân:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Máy chủ tự lưu trữ và thư viện đa phương tiện:** Plex · Jellyfin · Emby · Subsonic (và mọi máy chủ tương thích Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (và Owncloud qua API chung) · Synology Drive · QNAP.
- **NAS và giao thức chia sẻ tệp:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (xác thực bằng mật khẩu hoặc khóa công khai), NFS và DLNA (chỉ đọc — phát và tải xuống).
- **Lưu trữ đối tượng tương thích S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage hoặc bất kỳ điểm cuối S3-API nào.
- **Khám phá mạng cục bộ:** phần «Thiết bị có sẵn» tự động liệt kê bất kỳ thiết bị nào trên Wi-Fi của bạn được quảng bá qua Bonjour / mDNS — máy chủ Plex, Jellyfin, Emby, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, bộ định tuyến AirPort có ổ đĩa gắn kèm, v.v.

## Bảo mật và quyền riêng tư

Chúng tôi chỉ sử dụng SDK chính thức và kết nối bảo mật để tương tác với các dịch vụ đám mây đã kết nối. Thông tin đăng nhập và mật khẩu của bạn không có sẵn cho ứng dụng. Tất cả các yêu cầu từ ứng dụng đến dịch vụ đám mây đều được mã hóa.

Khi bạn nhập thông tin đăng nhập và mật khẩu, ứng dụng hiển thị trang ủy quyền chính thức do nhà cung cấp dịch vụ đám mây cung cấp và toàn bộ quá trình ủy quyền diễn ra bên ngoài ứng dụng. Nhà cung cấp dịch vụ đám mây gửi auth token đến ứng dụng sau khi ủy quyền thành công và token đó được sử dụng để thực hiện các lệnh gọi API.

Auth token là khóa kỹ thuật số cho phép các ứng dụng bên thứ ba tương tác với lưu trữ đám mây. Auth token được lưu trữ trên thiết bị của bạn trong bộ lưu trữ hệ thống an toàn có tên là Keychain. Bạn có thể tải xuống các tệp từ dịch vụ đám mây đã kết nối đến thiết bị và các tệp đó sẽ được đặt trong thư mục «Documents» của ứng dụng. Bạn có thể xóa những tệp đó bất cứ lúc nào bằng trình quản lý tệp tích hợp.

Ứng dụng không chia sẻ bất kỳ thông tin nào từ tài khoản đám mây đã kết nối. Bạn có thể thu hồi quyền truy cập vào tài khoản đám mây của mình bất cứ lúc nào bằng cách mở trang cài đặt tài khoản trên trình duyệt web.

## Thu hồi auth token

Đăng nhập vào tài khoản của bạn trên trình duyệt web và điều hướng đến trang cài đặt. Ở đó bạn có thể tìm thấy tất cả các ứng dụng bên thứ ba được kết nối với tài khoản đám mây của bạn và xóa bất kỳ ứng dụng nào. Hướng dẫn chi tiết có tại [đây](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Bạn cũng có thể ngắt kết nối các tài khoản đám mây đã kết nối trong ứng dụng và auth token cũng sẽ bị xóa khỏi thiết bị của bạn. Nếu bạn xóa ứng dụng khỏi thiết bị, tất cả dữ liệu đã tải xuống và token truy cập cũng sẽ bị xóa.

## Ngắt kết nối lưu trữ đám mây hoặc thay đổi cấu hình

- Truy cập Tùy chọn lưu trữ đám mây: đầu tiên, tìm lưu trữ đám mây bạn muốn quản lý trong giao diện ứng dụng.
- Nhấn nút «...»: bên cạnh tiêu đề dịch vụ, bạn sẽ thấy nút «...». Nhấn vào đó để truy cập các tùy chọn bổ sung.
  - **Đổi tên**: nếu bạn muốn thay đổi tên dịch vụ đám mây trong danh sách của mình, chọn «Đổi tên».
  - **Cài đặt**: để sửa đổi cấu hình hoặc dữ liệu xác thực cho dịch vụ đám mây, chọn «Cài đặt». Đôi khi, bạn có thể cần ủy quyền lại dịch vụ đám mây đã kết nối nếu token ủy quyền đã hết hạn.
  - **Ngắt kết nối**: nếu bạn muốn ngắt hoàn toàn kết nối giữa ứng dụng và dịch vụ đám mây, chọn «Ngắt kết nối». Lưu ý rằng việc chọn tùy chọn này sẽ xóa tất cả bài hát liên quan đến dịch vụ đám mây này khỏi thư viện nhạc của ứng dụng, nhưng chúng sẽ vẫn còn trên máy chủ.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Thêm hành động cho lưu trữ đám mây đã kết nối" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Kết nối đến Máy tính hoặc NAS

Bạn cũng có thể kết nối máy tính, NAS cá nhân hoặc các thiết bị mạng khác bằng giao thức SMB, DLNA hoặc WebDAV.

## Kết nối đến máy tính bằng SMB

- Nhấn «Kết nối lưu trữ đám mây» → SMB.
- Nhập địa chỉ IP máy tính và tên thư mục chia sẻ trong trường URL theo định dạng smb://computer-ip-address/shared-folder-name
- Chọn phiên bản giao thức: Auto, SMB1, SMB2
- Nhập thông tin đăng nhập và mật khẩu (nếu cần)
- Nhấn «Hoàn tất».

Nếu kết nối thành công, bạn sẽ thấy lưu trữ đã kết nối trong phần «Lưu trữ đám mây».  
Hướng dẫn đầy đủ về cách kết nối Mac hoặc PC bằng SMB có tại [đây](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Cài đặt kết nối SMB" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Kết nối đến NAS bằng WebDAV

Tất cả các bước tương tự ngoại trừ trường URL.  
URL phải theo định dạng http://server-name hoặc https://server-name nếu máy chủ hỗ trợ SSL.
Hướng dẫn đầy đủ về cách kết nối NAS bằng giao thức WebDAV có tại [đây](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Cài đặt kết nối WebDAV" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Kết nối đến Máy tính hoặc NAS bằng DLNA

Bạn cũng có thể chia sẻ thư viện nhạc trên Windows PC hoặc NAS cá nhân bằng giao thức DLNA và truy cập thư viện đó trong ứng dụng như được mô tả [tại đây](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA là giao thức phổ biến và được sử dụng rộng rãi, nhưng nó chỉ cho phép bạn phát hoặc tải xuống nhạc. Bạn không thể tải tệp lên hoặc tạo thư mục mới trên máy chủ.

{{< cards cols="1">}}
  {{< card title="" subtitle="Cài đặt kết nối DLNA" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Thiết bị có sẵn

Phần này hiển thị tất cả các thiết bị trong mạng cục bộ của bạn mà bạn có thể kết nối qua ứng dụng.  
Để thiết lập kết nối với thiết bị, hãy làm theo các bước sau:

- Mở ứng dụng và vào phần «Thiết bị có sẵn».
- Nhấn vào thiết bị bạn muốn kết nối từ danh sách.
- Nếu cần, nhập thông tin đăng nhập để hoàn tất kết nối.

{{< cards cols="1">}}
  {{< card title="" subtitle="Thiết bị có sẵn trên mạng cục bộ" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive là công nghệ tiện lợi cho phép truyền tệp không dây từ máy tính sang thiết bị iOS của bạn qua trình duyệt máy tính.  
Để sử dụng tính năng này hiệu quả, hãy đảm bảo thiết bị và máy tính của bạn được kết nối cùng một mạng Wi-Fi.  
Dưới đây là hướng dẫn từng bước về cách sử dụng Wi-Fi Drive.

## Bật Wi-Fi Drive

- Mở ứng dụng và vào tab «Kết nối».
- Chọn «Kết nối qua Wi-Fi» để truy cập màn hình chính Wi-Fi Drive.
- Nhấn «Khởi động Wi-Fi Drive» để bật Wi-Fi Drive.

## Truy cập Wi-Fi Drive trên Máy tính

- Trên máy tính (để bàn hoặc laptop), mở trình duyệt web (như Chrome, Firefox hoặc Safari).
- Trong thanh địa chỉ của trình duyệt, nhập URL do ứng dụng cung cấp.

## Truyền tệp không dây

Sau khi trang web tương ứng với thiết bị iOS của bạn mở trong trình duyệt, bạn có thể dễ dàng kéo và thả tệp từ máy tính vào trang web.  
Các tệp bạn kéo và thả sẽ bắt đầu truyền sang thiết bị iOS của bạn và có thể truy cập trong ứng dụng.

{{< cards cols="1">}}
  {{< card title="" subtitle="Cài đặt máy chủ Wi-Fi Drive" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Hướng dẫn chi tiết về cách truyền tệp không dây bằng WiFi-Drive có tại [đây](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing là công nghệ khác cho phép bạn truyền tệp từ máy tính sang thiết bị bằng ứng dụng Finder trên Mac và cáp.  
- Chỉ cần kết nối thiết bị với máy tính bằng cáp và chạy ứng dụng Finder trên Mac. 
- Mở «Vị trí» → «Thiết bị đã kết nối của bạn» → «Tệp» → và tìm ứng dụng Evermusic. 
- Nhấn vào biểu tượng ứng dụng để xem tất cả thư mục chia sẻ. 
- Sao chép tệp từ máy tính sang thư mục chia sẻ trên thiết bị bằng kéo và thả.  

Hướng dẫn chi tiết về cách sử dụng iTunes file sharing có tại [đây](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder File Sharing trên Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Kết nối USB flash drive

Nếu bạn có thẻ SD, bạn có thể kết nối nó bằng đầu đọc thẻ lightning. Ứng dụng hiện hỗ trợ đầu đọc thẻ Apple Certified và iXpand Flash Drives. Nếu bạn có iXpand Flash Drive - hãy cắm vào cổng lightning và mở ứng dụng. Bạn sẽ thấy thông báo «Thiết bị ngoài đã kết nối» và thông tin thiết bị. Chỉ cần nhấn vào biểu tượng flash drive để truy cập thư mục nhạc và nhấn vào bất kỳ tệp âm thanh nào để bắt đầu phát. Hướng dẫn chi tiết về cách kết nối USB flash drive với iPhone và nghe nhạc hoặc quản lý tệp có tại [đây](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Trình quản lý tệp

Sau khi kết nối dịch vụ lưu trữ đám mây, nhấn vào biểu tượng của nó để xem tất cả tệp và thư mục có sẵn. Bạn có thể sử dụng trình quản lý tệp tích hợp để làm việc với các tệp này — tải xuống, đổi tên, di chuyển và nhiều hơn nữa. Khi bạn bắt đầu tải xuống, tệp sẽ xuất hiện trong hàng đợi truyền. Để xem hàng đợi truyền, vào tab «Tệp cục bộ» và nhấn vào biểu tượng mũi tên quay trong góc trên bên trái. Tất cả tệp và thư mục đã tải xuống đều có trong phần «Tệp cục bộ».

## Thanh công cụ trên cùng

Thanh công cụ trên cùng, nằm thuận tiện dưới thanh điều hướng, cung cấp một số hành động hữu ích để truy cập dễ dàng. Bạn có thể hiện hoặc ẩn thanh công cụ này bằng cử chỉ vuốt xuống. Đây là các hành động có sẵn:

- **Tìm kiếm**: tùy chọn này cho phép bạn thực hiện tìm kiếm nhanh trong thư mục hiện tại.
- **Tiếp tục phát**: nếu được bật trong cài đặt ứng dụng, tính năng này khôi phục hàng đợi trình phát âm thanh và vị trí phương tiện cuối cùng cho thư mục hiện tại.
- **Phát tất cả**: khi chọn hành động này, ứng dụng sẽ quét thư mục hiện tại và các thư mục con, thêm tất cả tệp âm thanh tìm thấy vào hàng đợi trình phát mới.
- **Phát ngẫu nhiên**: tương tự «Phát tất cả», nhưng trộn các tệp trước khi thêm vào hàng đợi trình phát âm thanh.

{{< cards cols="1">}}
  {{< card title="" subtitle="Thanh công cụ trên cùng bên trong thư mục đám mây" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Tùy chọn thư mục

Khi bạn mở thư mục trong ứng dụng, bạn sẽ tìm thấy một bộ hành động tiện dụng có thể truy cập bằng cách nhấn nút «...» ở góc trên bên phải màn hình.  
Dưới đây là mô tả các hành động này:

- **Chọn**: kích hoạt chế độ chọn tệp. Chế độ này cho phép bạn chọn một hoặc nhiều tệp trong thư mục.
- **Thư mục mới**: tạo thư mục mới trong thư mục hiện tại.
- **Bật chế độ ngoại tuyến**: bật chế độ ngoại tuyến cho thư mục hiện tại. Chế độ ngoại tuyến không chỉ tải xuống đơn giản; nó tích cực theo dõi thư mục để phát hiện thay đổi. Nếu bạn thêm tệp mới vào thư mục trực tuyến, ứng dụng sẽ tự động tải xuống các tệp này.
- **Tải tệp lên**: tải tệp từ thiết bị của bạn lên thư mục trực tuyến.
- **Tìm kiếm**: tìm kiếm tệp cụ thể trong thư mục hiện tại.
- **Sắp xếp**: sắp xếp tệp trong thư mục theo tiêu chí như tên, kích thước hoặc ngày chỉnh sửa.
- **Chế độ lưới/danh sách**: chuyển đổi giữa hai chế độ xem: dạng bảng và dạng hình thu nhỏ.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Thêm hành động cho thư mục hiện tại" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Chỉnh sửa tệp trực tuyến

Khi bạn cần quản lý nhiều tệp trong lưu trữ đám mây trên Evermusic, bạn có thể sử dụng chế độ chọn. Thực hiện các bước sau:

- **Kích hoạt chế độ chọn**: mở ứng dụng và điều hướng đến phần chứa lưu trữ đám mây của bạn. Tìm nút «...» (dấu chấm lửng) ở góc trên bên phải. Nhấn vào đó và chọn mục menu «Chọn» để kích hoạt chế độ chọn.
- **Chọn tệp**: bạn sẽ thấy hộp kiểm xuất hiện bên cạnh mỗi tệp hoặc thư mục. Chọn một hoặc nhiều tệp hoặc thư mục bằng cách nhấn vào hộp kiểm bên cạnh chúng.
- **Thực hiện các hành động khác nhau**: sau khi chọn tệp hoặc thư mục bạn muốn quản lý, bạn sẽ có quyền truy cập vào một số hành động.

{{< cards cols="1">}}
  {{< card title="" subtitle="Chế độ chọn cho tệp trực tuyến" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Hành động tệp

Gần tiêu đề tệp, bạn sẽ thấy ký hiệu dấu chấm lửng «...» (ba chấm) — đây là menu hành động.  
Nhấn vào đó để xem danh sách các hành động có sẵn:

- **Phát tiếp theo**: chèn tệp đã chọn lên đầu hàng đợi trình phát của bạn.
- **Phát sau**: thêm tệp vào cuối hàng đợi trình phát của bạn.
- **Thêm vào thư viện nhạc**: kết hợp tệp vào thư viện nhạc của bạn.
- **Thêm vào danh sách phát**: sử dụng hành động này để thêm tệp vào danh sách phát hiện có hoặc tạo danh sách phát mới.
- **Chỉnh sửa thẻ âm thanh**: truy cập trình chỉnh sửa thẻ tích hợp của Evermusic để sửa đổi thẻ âm thanh cho tệp đã chọn.
- **Thêm vào mục yêu thích**: thêm tệp vào danh sách tệp yêu thích của bạn.
- **Tải xuống**: tải xuống tệp hoặc thư mục về thiết bị để sử dụng ngoại tuyến.
- **Đổi tên**: đổi tên tệp trực tiếp trên lưu trữ từ xa.
- **Di chuyển**: di chuyển tệp đến thư mục khác trong lưu trữ đám mây của bạn.
- **Mở trong**: xuất tệp sang ứng dụng tương thích khác.
- **Xóa**: hành động này sẽ xóa vĩnh viễn tệp khỏi lưu trữ đám mây của bạn.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Thêm hành động cho một tệp đơn lẻ" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Nếu danh sách hành động vượt quá không gian màn hình hiện có, chỉ cần cuộn xuống trong menu hành động để truy cập các tùy chọn bổ sung.

## Hành động thư mục

Đối với mỗi thư mục trong lưu trữ đám mây của bạn, có nhiều hành động khác nhau. Để truy cập các tùy chọn này, chỉ cần nhấn biểu tượng dấu chấm lửng «...» bên cạnh tiêu đề thư mục. Dưới đây là các hành động có sẵn:

- **Phát tất cả**: thay thế hàng đợi trình phát hiện tại bằng tất cả các mục từ thư mục đã chọn.
- **Phát tiếp theo**: thêm toàn bộ thư mục lên đầu hàng đợi trình phát.
- **Phát sau**: thêm nội dung thư mục vào cuối hàng đợi trình phát.
- **Thêm vào thư viện nhạc**: kết hợp liền mạch nội dung thư mục vào thư viện nhạc của bạn.
- **Thêm vào danh sách phát**: bạn có thể đưa toàn bộ thư mục vào danh sách phát.
- **Thêm vào mục yêu thích**: sử dụng hành động này để thêm thư mục vào danh sách tệp yêu thích của bạn.
- **Bật chế độ ngoại tuyến**: bằng cách bật chế độ ngoại tuyến cho thư mục đã chọn, ứng dụng liên tục quét để phát hiện thay đổi và tự động tải xuống tệp mới.
- **Tải xuống**: tải xuống tất cả nội dung thư mục về thiết bị để truy cập ngoại tuyến.
- **Đổi tên**: đổi tên thư mục trực tiếp trên lưu trữ từ xa.
- **Di chuyển**: di chuyển thư mục đến vị trí khác trong lưu trữ đám mây của bạn.
- **Xóa**: hãy thận trọng với hành động này vì nó xóa vĩnh viễn thư mục và nội dung của nó khỏi lưu trữ đám mây.


## Truy cập nhanh

Phần Truy cập nhanh nằm ở đầu màn hình. Nó cung cấp quyền truy cập nhanh vào các tệp và thư mục yêu thích và gần đây đã mở từ các dịch vụ đám mây đã kết nối.
Bất cứ khi nào bạn mở tệp hoặc thư mục từ đám mây, nó được thêm vào danh sách «Gần đây». Để xóa danh sách này, mở «Gần đây», nhấn nút «Thêm hành động» và chọn «Xóa danh sách». Bạn cũng có thể đánh dấu các thư mục lồng sâu là Mục yêu thích để truy cập nhanh mà không cần điều hướng qua cấu trúc thư mục.

## Dịch vụ khác

Phần này hiển thị các tính năng bổ sung giúp nâng cao trải nghiệm của bạn. Hiện tại, ứng dụng hỗ trợ scrobbling Last.fm. Khi đã kết nối, số liệu thống kê phát nhạc của bạn được tự động gửi đến tài khoản Last.fm của bạn. Bạn có thể truy cập hồ sơ Last.fm của mình sau để xem phân tích nghe nhạc và nhận đề xuất nhạc được cá nhân hóa. Hướng dẫn cài đặt chi tiết có tại [đây](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
