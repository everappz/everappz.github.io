---
title: "Kết nối"
date: 2020-02-01
description: "Tìm hiểu cách kết nối dịch vụ đám mây và thiết bị NAS với Flacbox. Phát trực tuyến nhạc độ phân giải cao từ iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk và nhiều hơn nữa. Sử dụng SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder File Sharing và USB flash drive."
keywords: [
  "thiết lập đám mây Flacbox", "kết nối Google Drive với Flacbox", "phát trực tuyến SMB",
  "WebDAV iOS player", "ứng dụng nhạc DLNA", "phát trực tuyến âm thanh NAS", "Wi-Fi Drive iPhone",
  "chuyển file sang iPhone", "iTunes File Sharing Flacbox", "kết nối NAS với iPhone",
  "ứng dụng nhạc Synology Drive", "ứng dụng nhạc QNAP", "ứng dụng nhạc Bluesound",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "ứng dụng nhạc scrobbling Last.fm",
  "nhạc iXpand Flash Drive", "USB DAC iPhone"
]
tags: ["hướng dẫn", "flacbox", "kết nối", "đám mây", "NAS"]
readingTime: 12
---


Trên màn hình này, bạn có thể kết nối với tất cả nguồn lưu trữ nhạc. Bạn có thể tích hợp các dịch vụ đám mây phổ biến như Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive và nhiều dịch vụ khác, cũng như Mac, PC hoặc NAS qua các giao thức chuẩn. Cho dù bộ sưu tập của bạn nằm trên dịch vụ Dropbox hay NAS cá nhân như Synology, QNAP, Buffalo, Apple Time Capsule hoặc WD My Cloud Home, Flacbox đều kết nối tất cả từ một màn hình duy nhất.

{{< cards cols="1">}}
  {{< card title="" subtitle="Màn hình Kết nối Flacbox" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Kết nối với Lưu trữ Đám mây

- Mở tab **Kết nối**.
- Chọn **Kết nối tới bộ nhớ đám mây** từ menu.
- Chọn dịch vụ đám mây từ danh sách.
- Nhập thông tin đăng nhập trên trang ủy quyền chính thức của nhà cung cấp, sau đó nhấn **Hoàn tất**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Thêm Dịch vụ Lưu trữ Đám mây" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Nếu gặp sự cố, hãy kiểm tra kết nối internet và thông tin đăng nhập. Phiên bản Premium của ứng dụng cho phép thêm không giới hạn dịch vụ; phiên bản miễn phí hỗ trợ tối đa ba dịch vụ.

## Dịch vụ Đám mây, Máy chủ Phương tiện và Giao thức được Hỗ trợ

Flacbox hỗ trợ danh sách nguồn nhạc đặc biệt phong phú. Tất cả bên dưới đều có thể truy cập từ một màn hình **Kết nối tới bộ nhớ đám mây**.

**Lưu trữ đám mây cá nhân:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Máy chủ tự host:** Plex · Jellyfin · Emby · Subsonic (và mọi máy chủ tương thích Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (và ownCloud qua API chia sẻ) · Synology Drive · QNAP.

**NAS và giao thức chia sẻ file:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, mật khẩu hoặc xác thực khóa công khai) · NFS · DLNA / UPnP (phát và tải xuống).

**Lưu trữ đối tượng tương thích S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces và bất kỳ endpoint S3-API nào khác.

**Khám phá mạng nội bộ:** phần Thiết bị có sẵn tự động liệt kê mọi dịch vụ Bonjour / mDNS trên Wi-Fi — chỉ cần chạm để kết nối mà không cần nhập địa chỉ IP.

Mỗi kết nối sử dụng **SDK chính thức hoặc giao thức mở** của dịch vụ với ủy quyền OAuth khi được hỗ trợ. Bạn có thể kết nối nhiều tài khoản của cùng một dịch vụ và duyệt chúng song song.

## Bảo mật và Quyền riêng tư

Chúng tôi chỉ sử dụng SDK chính thức và kết nối bảo mật để tương tác với các dịch vụ đám mây được kết nối. Thông tin đăng nhập và mật khẩu của bạn không thể truy cập được bởi ứng dụng — tất cả truyền tải được mã hóa TLS.

Khi bạn nhập thông tin đăng nhập, ứng dụng hiển thị trang ủy quyền chính thức của nhà cung cấp đám mây và toàn bộ quá trình ủy quyền diễn ra bên ngoài ứng dụng. Token xác thực được lưu trữ trên thiết bị trong bộ nhớ hệ thống bảo mật của Apple (Keychain), được mã hóa và bảo vệ bằng mã khóa thiết bị hoặc khóa sinh trắc học.

Ứng dụng không chia sẻ bất kỳ thông tin nào từ các tài khoản đám mây được kết nối của bạn với Everappz, nhà quảng cáo hoặc bất kỳ bên thứ ba nào. Bạn có thể thu hồi quyền truy cập vào tài khoản đám mây bất kỳ lúc nào bằng cách mở trang cài đặt tài khoản trong trình duyệt web.

## Thu hồi Auth-Token

Để thu hồi auth-token, đăng nhập vào tài khoản đám mây trong trình duyệt web và điều hướng đến trang bảo mật hoặc ứng dụng đã kết nối. Tại đó bạn có thể tìm thấy mọi ứng dụng bên thứ ba được kết nối với tài khoản đám mây của bạn và xóa bất kỳ ứng dụng nào. Hướng dẫn chi tiết cho tài khoản Google có sẵn [tại đây](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Bạn cũng có thể ngắt kết nối tài khoản đám mây bên trong ứng dụng — khi đó, auth-token sẽ bị xóa ngay lập tức khỏi thiết bị. Nếu bạn gỡ cài đặt ứng dụng, tất cả dữ liệu đã tải xuống và token truy cập sẽ tự động bị xóa.

## Ngắt kết nối Lưu trữ Đám mây hoặc Thay đổi Cấu hình

- **Truy cập tùy chọn lưu trữ đám mây** — tìm dịch vụ đã kết nối trong màn hình **Kết nối**.
- **Nhấn nút «...»** bên cạnh tiêu đề dịch vụ để mở các tùy chọn bổ sung:
  - **Đổi tên** — thay đổi tên của dịch vụ đám mây trong danh sách.
  - **Cài đặt** — chỉnh sửa cấu hình hoặc dữ liệu xác thực. Đôi khi bạn có thể cần ủy quyền lại nếu token đã hết hạn.
  - **Ngắt kết nối** — hoàn toàn hủy kết nối giữa ứng dụng và dịch vụ đám mây. Điều này xóa tất cả bài hát liên quan khỏi thư viện nhạc của ứng dụng, nhưng chúng vẫn nguyên vẹn trên máy chủ.

## Kết nối với Máy tính hoặc NAS

Bạn cũng có thể kết nối máy tính, NAS cá nhân hoặc các thiết bị mạng khác bằng giao thức SMB, DLNA hoặc WebDAV. Đây là cách dễ nhất để đưa thư viện nhạc gia đình hiện có vào Flacbox mà không cần sao chép.

## Kết nối với Máy tính qua SMB

- Nhấn **Kết nối tới bộ nhớ đám mây → SMB**.
- Nhập địa chỉ IP của máy tính và tên thư mục chia sẻ theo định dạng `smb://computer-ip-address/shared-folder-name`.
- Chọn phiên bản giao thức: **Auto**, **SMB1** hoặc **SMB2**.
- Nhập thông tin đăng nhập và mật khẩu (nếu cần).
- Nhấn **Hoàn tất**.

Nếu kết nối thành công, bạn sẽ thấy bộ nhớ đã kết nối trong phần **Lưu trữ Đám mây**. Hướng dẫn đầy đủ về cách kết nối Mac hoặc PC qua SMB có sẵn [tại đây](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Kết nối với NAS qua WebDAV

Tất cả các bước giống với SMB, ngoại trừ trường URL. URL phải có định dạng `http://server-name` hoặc `https://server-name` nếu máy chủ hỗ trợ SSL. WebDAV hoạt động với **Synology, QNAP, Nextcloud, ownCloud** và nhiều máy chủ khác.

Hướng dẫn đầy đủ về cách kết nối NAS qua WebDAV có sẵn [tại đây](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Kết nối với Máy tính hoặc NAS qua DLNA

Bạn cũng có thể chia sẻ thư viện nhạc trên Windows PC hoặc NAS cá nhân qua giao thức DLNA / UPnP như mô tả [tại đây](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA chỉ cho phép phát hoặc tải nhạc xuống — bạn không thể tải lên file hoặc tạo thư mục mới trên máy chủ DLNA.

## Kết nối với NAS hoặc Máy chủ qua FTP, FTPS hoặc SFTP

Flacbox cũng hỗ trợ các giao thức chuyển file cổ điển. Để kết nối qua FTP hoặc FTPS, nhấn **Kết nối tới bộ nhớ đám mây → FTP**, nhập URL máy chủ theo định dạng `ftp://server-name` (hoặc `ftps://server-name` cho kết nối mã hóa), nhập thông tin đăng nhập, rồi nhấn **Hoàn tất**. Đối với **SFTP**, chọn **SFTP** và cung cấp mật khẩu hoặc cặp khóa SSH.

## Kết nối với NFS Share

Flacbox hỗ trợ **NFS** (Network File System). Chọn **NFS** trong menu **Kết nối tới bộ nhớ đám mây**, nhập địa chỉ máy chủ và đường dẫn xuất khẩu, rồi nhấn **Hoàn tất**.

## Kết nối Plex Media Server

Flacbox có thể kết nối trực tiếp với Plex Media Server và duyệt thư viện nhạc theo Nghệ sĩ, Album, Thể loại và Danh sách phát. Nhấn **Kết nối tới bộ nhớ đám mây → Plex**, đăng nhập bằng tài khoản Plex, chọn máy chủ — thư viện xuất hiện cùng với các dịch vụ đám mây của bạn.

## Kết nối Máy chủ Jellyfin hoặc Emby

Cả **Jellyfin** (mã nguồn mở) và **Emby** (thương mại) đều hoạt động tự nhiên trong Flacbox. Nhấn **Kết nối tới bộ nhớ đám mây → Jellyfin** hoặc **Emby**, nhập URL máy chủ và thông tin đăng nhập.

## Kết nối Máy chủ Subsonic hoặc Navidrome

Flacbox hỗ trợ Subsonic API, có nghĩa là hoạt động với **Subsonic**, **Navidrome** và mọi máy chủ tương thích Subsonic. Nhấn **Kết nối tới bộ nhớ đám mây → Subsonic**, nhập URL máy chủ và thông tin đăng nhập.

## Kết nối với Lưu trữ Đối tượng Tương thích S3

Nhấn **Kết nối tới bộ nhớ đám mây → S3 storage**, sau đó nhập URL endpoint, khu vực, khóa truy cập, khóa bí mật và tên bucket. Hoạt động với AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces và bất kỳ dịch vụ S3-API nào khác.

## Thiết bị có sẵn

Phần này hiển thị mọi thiết bị trên mạng nội bộ mà bạn có thể kết nối qua khám phá Bonjour.

- Mở ứng dụng và đi đến phần **Thiết bị có sẵn** trong Kết nối.
- Nhấn vào thiết bị bạn muốn kết nối.
- Nếu cần, nhập thông tin đăng nhập để hoàn tất kết nối.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Thiết bị có sẵn trên Mạng nội bộ" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive là công nghệ tiện lợi cho phép truyền file không dây từ máy tính sang thiết bị iOS qua bất kỳ trình duyệt máy tính nào. Đảm bảo thiết bị và máy tính kết nối cùng một mạng Wi-Fi.

### Bật Wi-Fi Drive

- Mở ứng dụng và đi đến tab **Kết nối**.
- Chọn **Kết nối qua Wi-Fi** để truy cập màn hình Wi-Fi Drive chính.
- (Tùy chọn) Đặt tên người dùng và mật khẩu cho máy chủ web nhúng.
- Nhấn **Khởi động Wi-Fi Drive** để bật Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Truy cập Wi-Fi Drive trên Máy tính

- Trên máy tính, mở trình duyệt web (Chrome, Firefox hoặc Safari).
- Trong thanh địa chỉ, nhập URL do ứng dụng cung cấp.

### Truyền File Không dây

Khi trang web tương ứng với thiết bị iOS mở ra trong trình duyệt, bạn có thể dễ dàng kéo và thả file từ máy tính lên trang web. File sẽ bắt đầu truyền đến thiết bị iOS và có thể truy cập bên trong Flacbox.

Bạn cũng có thể gắn Wi-Fi Drive trực tiếp trong Finder trên macOS (Đi → Kết nối với Máy chủ…) hoặc File Explorer trên Windows (Ánh xạ Ổ đĩa Mạng…).

Hướng dẫn chi tiết về cách truyền file không dây qua Wi-Fi Drive có sẵn [tại đây](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (nay là Finder File Sharing trên macOS Catalina trở lên) là cách khác để truyền file qua cáp Lightning hoặc USB-C.

- Kết nối thiết bị với máy tính bằng cáp và chạy **Finder** trên Mac (hoặc **iTunes** trên Windows).
- Mở **Vị trí → Thiết bị đã kết nối → Tệp** và tìm ứng dụng Flacbox.
- Nhấn vào biểu tượng ứng dụng để xem tất cả thư mục chia sẻ.
- Sao chép file từ máy tính vào thư mục chia sẻ bằng kéo thả.

Hướng dẫn chi tiết về cách sử dụng Finder File Sharing có sẵn [tại đây](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Kết nối USB Flash Drive

Nếu bạn có thẻ SD hoặc USB drive, hãy kết nối qua bộ chuyển đổi Lightning to USB / SD Card Reader hoặc USB-C drive (trên iPad và iPhone 15 / 16 / 17 / Pro). Ứng dụng hỗ trợ đầu đọc thẻ được Apple chứng nhận và iXpand Flash Drive.

Hướng dẫn chi tiết về cách kết nối USB flash drive với iPhone có sẵn [tại đây](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Trình quản lý File

Sau khi kết nối dịch vụ đám mây, nhấn vào biểu tượng để xem tất cả file và thư mục. Trình quản lý file tích hợp cho phép tải xuống, đổi tên, di chuyển, tải lên, xóa và nhiều thao tác khác.

## Thanh Công cụ Trên cùng

Thanh công cụ trên cùng, nằm bên dưới thanh điều hướng, cung cấp một số hành động hữu ích. Bạn có thể hiển thị hoặc ẩn nó bằng cử chỉ vuốt xuống.

- **Tìm kiếm** — thực hiện tìm kiếm nhanh trong thư mục hiện tại.
- **Tiếp tục phát** — nếu được bật trong cài đặt, tính năng này khôi phục hàng đợi phát và vị trí phát cuối cùng.
- **Phát tất cả** — quét thư mục hiện tại và thư mục con, thêm tất cả file âm thanh vào hàng đợi phát mới.
- **Phát ngẫu nhiên** — như Phát tất cả nhưng xáo trộn file trước khi thêm vào hàng đợi.

## Tùy chọn Thư mục

Khi mở thư mục, nhấn nút **«...»** ở góc trên bên phải để truy cập các hành động:

- **Chọn** — kích hoạt chế độ chọn file.
- **Thư mục mới** — tạo thư mục mới.
- **Bật chế độ ngoại tuyến** — bật chế độ ngoại tuyến cho thư mục hiện tại với theo dõi thay đổi tự động.
- **Tải lên file** — tải file từ thiết bị lên thư mục trực tuyến.
- **Tìm kiếm** — tìm kiếm file trong thư mục hiện tại.
- **Sắp xếp** — sắp xếp file theo tên, kích thước, ngày sửa đổi hoặc siêu dữ liệu.
- **Lưới / Danh sách** — chuyển đổi giữa chế độ xem bảng và hình thu nhỏ.

## Chỉnh sửa File Trực tuyến

Để quản lý nhiều file trong lưu trữ đám mây, sử dụng **Chế độ Chọn**:

- **Kích hoạt Chế độ Chọn** — nhấn nút **«...»** ở góc trên bên phải và chọn **Chọn**.
- **Chọn File** — hộp kiểm xuất hiện bên cạnh mỗi file và thư mục.
- **Thực hiện Hành động** — sau khi chọn, có thể thực hiện: Phát tiếp, Phát sau, Thêm vào Thư viện Nhạc, Thêm vào Danh sách phát, Sao chép, Tải lên, Di chuyển, Đổi tên, Xóa.

## Hành động File

Nhấn biểu tượng **«...»** bên cạnh tiêu đề file để hiển thị menu hành động:

- **Phát tiếp** — chèn file vào đầu hàng đợi phát.
- **Phát sau** — thêm file vào cuối hàng đợi phát.
- **Thêm vào Thư viện Nhạc** — đưa file vào thư viện nhạc.
- **Thêm vào Danh sách phát** — thêm file vào danh sách phát hiện có hoặc tạo mới.
- **Chỉnh sửa thẻ âm thanh** — mở trình chỉnh sửa thẻ tích hợp.
- **Thêm vào Yêu thích** — thêm file vào yêu thích để truy cập nhanh.
- **Tải xuống** — tải file hoặc thư mục về thiết bị để dùng ngoại tuyến.
- **Đổi tên** — đổi tên file trực tiếp trên bộ nhớ từ xa.
- **Di chuyển** — chuyển file sang thư mục khác trong lưu trữ đám mây.
- **Mở bằng** — xuất file sang ứng dụng tương thích khác.
- **Xóa** — xóa vĩnh viễn file khỏi lưu trữ đám mây. **Không thể hoàn tác hành động này.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Thêm Hành động cho File trong Lưu trữ Đám mây Đã kết nối" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

## Hành động Thư mục

Đối với mỗi thư mục trong lưu trữ đám mây, nhấn biểu tượng **«...»** bên cạnh tiêu đề thư mục để xem các hành động:

- **Phát tất cả** — thay thế hàng đợi phát hiện tại bằng mọi mục trong thư mục đã chọn.
- **Phát tiếp** — thêm toàn bộ thư mục vào đầu hàng đợi.
- **Phát sau** — thêm nội dung thư mục vào cuối hàng đợi.
- **Thêm vào Thư viện Nhạc** — đưa nội dung thư mục vào thư viện nhạc.
- **Thêm vào Danh sách phát** — thêm toàn bộ thư mục vào danh sách phát.
- **Thêm vào Yêu thích** — thêm thư mục vào yêu thích.
- **Bật chế độ ngoại tuyến** — liên tục theo dõi thư mục và tự động tải xuống các file mới.
- **Tải xuống** — tải xuống tất cả nội dung thư mục để truy cập ngoại tuyến.
- **Đổi tên** — đổi tên thư mục trực tiếp trên bộ nhớ từ xa.
- **Di chuyển** — chuyển thư mục đến vị trí khác trong lưu trữ đám mây.
- **Lưu trữ (ZIP)** — đóng gói nội dung thư mục thành một file ZIP duy nhất (tính năng Premium).
- **Xóa** — xóa vĩnh viễn thư mục và nội dung của nó. **Không thể hoàn tác hành động này.**

## Truy cập Nhanh

Phần Truy cập Nhanh nằm ở đầu màn hình. Nó cung cấp truy cập nhanh đến các file và thư mục yêu thích và mới mở từ các dịch vụ đám mây đã kết nối.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Liên kết Trực tuyến và Truy cập Nhanh" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Dịch vụ Khác

Phần này hiển thị các tính năng bổ sung. Hiện tại, ứng dụng hỗ trợ scrobbling **Last.fm** — khi được kết nối, thống kê phát nhạc của bạn tự động được gửi đến tài khoản Last.fm. Hướng dẫn thiết lập chi tiết có sẵn [tại đây](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Kết nối Last.fm" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
