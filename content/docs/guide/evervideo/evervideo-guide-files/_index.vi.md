---
title: "Tệp"
date: 2020-02-01
lastmod: 2026-06-01
description: "Tìm hiểu cách sử dụng tab Tệp trong Evervideo trên iPhone, iPad và Mac. Kết nối dịch vụ đám mây, thiết bị NAS, máy chủ phương tiện và luồng RTSP ở một nơi. Quản lý video ngoại tuyến, hàng đợi truyền, tải xuống, Wi-Fi Drive, iTunes / Finder File Sharing và ổ USB. Hỗ trợ iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA và lưu trữ tương thích S3."
keywords: [
  "tệp Evervideo", "kết nối Evervideo", "tệp cục bộ Evervideo",
  "thiết lập video đám mây iPhone", "kết nối Google Drive video", "phát trực tuyến video SMB",
  "trình phát video WebDAV iOS", "video DLNA iPhone", "phát trực tuyến video NAS",
  "truyền video Wi-Fi Drive", "iTunes File Sharing Evervideo", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "chế độ ngoại tuyến video Evervideo", "hàng đợi truyền Evervideo",
  "trình quản lý tệp Evervideo", "thư mục Documents Evervideo",
  "trình phát video Synology", "trình phát video QNAP",
  "trình phát video Apple Time Capsule", "USB DAC video",
  "trình phát video iXpand", "trình phát video S3"
]
tags: ["hướng dẫn", "evervideo", "tệp", "kết nối", "đám mây", "NAS", "Plex", "RTSP"]
readingTime: 14
---

Tab Tệp là trình quản lý tệp tất cả trong một của Evervideo. Không giống hầu hết ứng dụng video tách biệt lưu trữ đám mây và tệp cục bộ vào các tab khác nhau, Evervideo hợp nhất cả hai vào một màn hình có thể cuộn để bạn có thể chuyển từ máy chủ Plex sang thư mục đám mây rồi đến thư mục Documents trên iPhone mà không cần chuyển đổi giữa các tab.

Tab Tệp được chia thành các phần rõ ràng xuất hiện theo thứ tự này trên màn hình:

- **Truy cập nhanh** — mục gần đây và yêu thích cho các tệp và thư mục bạn mở gần đây nhất.
- **Tệp trong ứng dụng này** — nội dung trong thư mục Documents được sandbox của Evervideo.
- **Tệp trên iPhone / iPad / Mac này** — video ở nơi khác trên thiết bị của bạn, được hiển thị qua trình chọn tệp hệ thống.
- **Lưu trữ đám mây** — mọi tài khoản đám mây, NAS và máy chủ phương tiện bạn đã kết nối.
- **Thiết bị có sẵn** — máy chủ và ổ đĩa được tự động phát hiện qua Bonjour / mDNS trên mạng cục bộ của bạn.

Ở góc trên bên phải màn hình Tệp có nút Truyền tải (biểu tượng mũi tên quay). Nhấn vào đó để mở Hàng đợi truyền tải nơi bạn theo dõi mọi lượt tải xuống và tải lên từ tất cả các nguồn của mình.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tệp Evervideo trên các bộ nhớ đã kết nối" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Kết nối với lưu trữ đám mây

Phần Lưu trữ đám mây của tab Tệp là nơi tồn tại mọi tài khoản đã kết nối, NAS, máy chủ phương tiện và luồng — cạnh nhau, trong một danh sách có thể cuộn.

{{< cards cols="1">}}
  {{< card title="" subtitle="Phần lưu trữ đám mây trong tab Tệp của Evervideo" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Mở tab **Tệp**.
- Cuộn đến phần **Lưu trữ đám mây**.
- Nhấn **Kết nối với lưu trữ đám mây** từ menu.
- Chọn dịch vụ lưu trữ đám mây từ danh sách.
- Nhập thông tin đăng nhập trên trang ủy quyền chính thức do nhà cung cấp đám mây cung cấp, sau đó nhấn **Hoàn tất**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Kết nối dịch vụ lưu trữ đám mây trong Evervideo" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Nếu gặp sự cố, hãy kiểm tra kết nối internet và thông tin đăng nhập / mật khẩu của bạn. Trong phiên bản Premium của ứng dụng, bạn có thể thêm số lượng dịch vụ không giới hạn; phiên bản miễn phí hỗ trợ tối đa ba dịch vụ.

## Dịch vụ lưu trữ đám mây, máy chủ phương tiện và giao thức được hỗ trợ

Evervideo hỗ trợ một phạm vi nguồn video cực kỳ rộng. Tất cả những gì dưới đây đều hoạt động từ một quy trình Kết nối với lưu trữ đám mây duy nhất.

**Lưu trữ đám mây cá nhân:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Máy chủ phương tiện tự lưu trữ:** Plex · Jellyfin · Emby · Subsonic (và mọi máy chủ tương thích Subsonic — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (và ownCloud qua API dùng chung) · Synology Drive · QNAP.

**Giao thức NAS và chia sẻ tệp:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, mật khẩu hoặc xác thực khóa công khai) · NFS · DLNA / UPnP (phát lại và tải xuống).

**Luồng trực tiếp và camera IP:** RTSP — trỏ Evervideo vào bất kỳ URL `rtsp://` nào và nó phát ngay. Tuyệt vời cho camera an ninh, luồng IPTV, camera chuông cửa, camera theo dõi trẻ và các nguồn trực tiếp tương tự.

**Lưu trữ đối tượng tương thích S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces và bất kỳ endpoint S3 API nào khác.

**Thư viện cục bộ trên thiết bị:** thư viện Photos (tất cả video, ghi màn hình, ảnh album) và thư viện ứng dụng Music (Album, Thể loại, Danh sách phát) — cả hai đều hiển thị bên trong Thư viện phương tiện để bạn không phải sao chép gì.

**Khám phá mạng cục bộ:** phần Thiết bị có sẵn tự động liệt kê mọi dịch vụ Bonjour / mDNS trên mạng Wi-Fi của bạn — máy chủ Plex, Jellyfin, Emby, Synology, QNAP, router AirPort với ổ đĩa gắn kèm, Apple Time Capsule — để bạn có thể nhấn để kết nối mà không cần nhập địa chỉ IP.

Mỗi kết nối sử dụng SDK chính thức hoặc giao thức mở của dịch vụ, với ủy quyền dựa trên OAuth khi được hỗ trợ. Bạn có thể kết nối nhiều tài khoản của cùng một dịch vụ (ví dụ: hai tài khoản Google Drive, hoặc cả máy chủ Plex và Jellyfin) và duyệt chúng cạnh nhau trong phần Lưu trữ đám mây.

## Bảo mật và quyền riêng tư

Evervideo chỉ sử dụng SDK chính thức và kết nối an toàn để tương tác với các dịch vụ đám mây đã kết nối. Thông tin đăng nhập và mật khẩu của bạn không thể truy cập được bởi ứng dụng — tất cả truyền tải đều được mã hóa TLS.

Khi bạn nhập thông tin đăng nhập và mật khẩu, ứng dụng hiển thị trang ủy quyền chính thức do nhà cung cấp dịch vụ đám mây cung cấp, và toàn bộ quá trình ủy quyền diễn ra bên ngoài ứng dụng. Sau khi ủy quyền thành công, nhà cung cấp dịch vụ đám mây gửi auth-token đến ứng dụng, và token đó được sử dụng để thực hiện các lệnh gọi API.

Auth-token là khóa kỹ thuật số cho phép ứng dụng bên thứ ba tương tác với lưu trữ đám mây thay mặt bạn. Token được lưu trữ trên thiết bị của bạn trong bộ nhớ hệ thống an toàn của Apple (Keychain), được mã hóa khi nghỉ và được bảo vệ bằng mã PIN thiết bị hoặc khóa sinh trắc học. Bạn có thể tải xuống tệp từ các dịch vụ đám mây đã kết nối về thiết bị; những tệp đó được đặt trong thư mục Documents của ứng dụng và có thể xóa bất kỳ lúc nào bằng trình quản lý tệp tích hợp.

Ứng dụng không chia sẻ bất kỳ thông tin nào từ tài khoản đám mây đã kết nối với Everappz, nhà quảng cáo hay bất kỳ bên thứ ba nào. Bạn có thể thu hồi quyền truy cập vào tài khoản đám mây của mình bất cứ lúc nào bằng cách mở trang cài đặt tài khoản trong trình duyệt web.

## Thu hồi Auth-Token

Để thu hồi auth-token, hãy đăng nhập vào tài khoản đám mây của bạn trong trình duyệt web và điều hướng đến trang bảo mật hoặc ứng dụng đã kết nối. Ở đó bạn có thể tìm thấy mọi ứng dụng bên thứ ba được kết nối với tài khoản đám mây và xóa bất kỳ ứng dụng nào nếu bạn không muốn sử dụng nó nữa. Hướng dẫn chi tiết cho tài khoản Google có sẵn [tại đây](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Bạn cũng có thể ngắt kết nối tài khoản đám mây ngay trong ứng dụng — khi làm vậy, auth-token sẽ bị xóa ngay lập tức khỏi thiết bị của bạn. Nếu bạn gỡ cài đặt ứng dụng khỏi thiết bị, tất cả dữ liệu đã tải xuống và token truy cập đều bị xóa tự động cùng với nó.

## Ngắt kết nối lưu trữ đám mây hoặc thay đổi cấu hình

- **Truy cập tùy chọn lưu trữ đám mây** — tìm dịch vụ đã kết nối trong phần **Lưu trữ đám mây** của tab Tệp.
- **Nhấn nút «...»** bên cạnh tiêu đề dịch vụ để mở thêm tùy chọn:
  - **Đổi tên** — thay đổi tên dịch vụ đám mây như nó xuất hiện trong danh sách của bạn.
  - **Cài đặt** — sửa đổi cấu hình hoặc dữ liệu xác thực. Đôi khi bạn cần ủy quyền lại dịch vụ đám mây đã kết nối nếu token ủy quyền đã hết hạn.
  - **Ngắt kết nối** — hoàn toàn cắt đứt kết nối giữa ứng dụng và dịch vụ đám mây. Thao tác này xóa tất cả video liên quan đến dịch vụ đó khỏi thư viện phương tiện, nhưng để chúng nguyên vẹn trên máy chủ.

## Kết nối với máy tính hoặc NAS

Bạn có thể kết nối máy tính, NAS cá nhân hoặc thiết bị mạng khác bằng giao thức SMB, WebDAV, FTP / FTPS, SFTP, NFS hoặc DLNA. Đây là cách dễ nhất để đưa thư viện phương tiện gia đình hiện có — dù nằm trên Mac, Windows PC, Synology, QNAP, Apple Time Capsule hay WD My Cloud Home — vào Evervideo mà không cần sao chép bất cứ thứ gì.

### Kết nối với máy tính bằng SMB

- Nhấn **Kết nối với lưu trữ đám mây → SMB**.
- Nhập địa chỉ IP của máy tính và tên thư mục chia sẻ theo định dạng `smb://computer-ip-address/shared-folder-name`.
- Chọn phiên bản giao thức: **Auto**, **SMB1** hoặc **SMB2**.
- Nhập thông tin đăng nhập và mật khẩu (nếu cần).
- Nhấn **Hoàn tất**.

Nếu kết nối thành công, chia sẻ xuất hiện trong phần Lưu trữ đám mây. Hướng dẫn đầy đủ về cách kết nối Mac hoặc PC bằng SMB có sẵn [tại đây](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Kết nối với NAS bằng WebDAV

Tất cả các bước giống như SMB, ngoại trừ trường URL. Sử dụng `http://server-name` hoặc `https://server-name` nếu máy chủ hỗ trợ SSL. WebDAV hoạt động với Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home và bất kỳ máy chủ nào có endpoint WebDAV.

Hướng dẫn đầy đủ về WebDAV có sẵn [tại đây](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Kết nối qua DLNA / UPnP

Chia sẻ thư viện phương tiện nằm trên Windows PC hoặc NAS của bạn bằng giao thức DLNA / UPnP và truy cập nó trong Evervideo như được mô tả [tại đây](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA được hỗ trợ rộng rãi, nhưng chỉ cho phép bạn phát hoặc tải xuống video — bạn không thể tải lên tệp hoặc tạo thư mục mới trên máy chủ DLNA.

### Kết nối bằng FTP, FTPS hoặc SFTP

Evervideo cũng hỗ trợ các giao thức truyền tệp cổ điển. Để kết nối máy chủ qua FTP hoặc FTPS, nhấn Kết nối với lưu trữ đám mây → FTP, nhập URL host dạng `ftp://server-name` (hoặc `ftps://server-name` cho kết nối được mã hóa), cung cấp thông tin đăng nhập và mật khẩu, sau đó nhấn Hoàn tất. Với SFTP (SSH File Transfer Protocol), chọn SFTP và cung cấp mật khẩu hoặc cặp khóa SSH.

### Kết nối với chia sẻ NFS

Evervideo bao gồm hỗ trợ NFS (Network File System) — tiện lợi cho các máy chủ Linux, máy chủ BSD và thiết bị NAS thích hiển thị thư viện video qua NFS thay vì SMB. Chọn NFS trong menu Kết nối với lưu trữ đám mây, nhập địa chỉ máy chủ và đường dẫn xuất, rồi nhấn Hoàn tất.

## Kết nối Plex Media Server

Evervideo có thể kết nối trực tiếp với Plex Media Server và duyệt thư viện Phim, Chương trình TV và Video gia đình của bạn. Nhấn Kết nối với lưu trữ đám mây → Plex, đăng nhập bằng tài khoản Plex, chọn máy chủ, và thư viện xuất hiện cạnh các dịch vụ đám mây của bạn. Các máy chủ Plex trên cùng mạng cục bộ cũng được phát hiện tự động trong phần Thiết bị có sẵn.

## Kết nối máy chủ Jellyfin hoặc Emby

Cả Jellyfin (mã nguồn mở) và Emby (thương mại) đều hoạt động natively trong Evervideo. Nhấn Kết nối với lưu trữ đám mây → Jellyfin hoặc Emby, nhập URL máy chủ (thường là `http://server-ip:8096`) và thông tin đăng nhập, và thư viện của bạn đã sẵn sàng để phát trực tuyến.

## Kết nối máy chủ Subsonic hoặc Navidrome

Evervideo hỗ trợ Subsonic API, nghĩa là nó hoạt động với Subsonic, Navidrome và mọi máy chủ tương thích Subsonic khác — bao gồm Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) và Ampache. Nhấn Kết nối với lưu trữ đám mây → Subsonic, nhập URL máy chủ và thông tin đăng nhập, và thư viện xuất hiện trong phần Lưu trữ đám mây.

## Kết nối luồng RTSP (Camera IP, TV trực tiếp, IPTV)

Evervideo có hỗ trợ RTSP native, vì vậy bạn có thể trỏ nó đến bất kỳ nguồn RTSP nào — camera an ninh, camera chuông cửa, nhà cung cấp IPTV, camera theo dõi trẻ, nguồn phát sóng — và Evervideo sẽ kéo và giải mã luồng trực tiếp. Nhấn Liên kết trực tuyến → Thêm liên kết, dán URL đầy đủ (`rtsp://camera-ip:port/stream-path`), cung cấp thông tin đăng nhập và mật khẩu nếu cần, rồi nhấn Hoàn tất.

## Kết nối với lưu trữ đối tượng tương thích S3

Đối với người tự lưu trữ và người dùng cao cấp sử dụng lưu trữ đối tượng đám mây, Evervideo bao gồm một connector tương thích S3. Nhấn Kết nối với lưu trữ đám mây → Lưu trữ S3, sau đó nhập URL endpoint, vùng, khóa truy cập, khóa bí mật và tên bucket. Điều này hoạt động với AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces và bất kỳ endpoint S3 API nào khác.

## Thiết bị có sẵn

Phần này hiển thị mọi thiết bị trên mạng cục bộ của bạn mà bạn có thể kết nối từ Evervideo qua khám phá Bonjour / mDNS — máy chủ Plex, Jellyfin, Emby, Synology, QNAP, router AirPort với ổ đĩa gắn kèm, Apple Time Capsule, v.v. Để thiết lập kết nối:

- Cuộn đến phần Thiết bị có sẵn trong tab Tệp.
- Nhấn vào thiết bị bạn muốn kết nối.
- Nếu cần, nhập thông tin đăng nhập để hoàn tất kết nối.

{{< cards cols="1">}}
  {{< card title="" subtitle="Thiết bị có sẵn Evervideo trên mạng cục bộ" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive cho phép bạn truyền tệp không dây từ máy tính sang thiết bị iOS qua bất kỳ trình duyệt máy tính để bàn, Finder hoặc File Explorer. Thiết bị và máy tính phải ở trên cùng mạng Wi-Fi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Bật Wi-Fi Drive

- Trong tab Tệp, cuộn đến Lưu trữ đám mây → Kết nối qua Wi-Fi để mở màn hình chính Wi-Fi Drive.
- (Tùy chọn) Đặt tên người dùng và mật khẩu cho máy chủ web nhúng.
- Nhấn Bắt đầu Wi-Fi Drive.

### Truy cập Wi-Fi Drive trên máy tính

- Mở trình duyệt web trên máy tính (Chrome, Firefox, Safari, v.v.).
- Nhập URL được ứng dụng hiển thị.
- Kéo và thả tệp từ máy tính vào trang web — chúng sẽ bắt đầu truyền sang thiết bị iOS.

Bạn cũng có thể gắn kết Wi-Fi Drive trực tiếp trong **Finder** trên macOS (Đi → Kết nối với máy chủ…) hoặc File Explorer trên Windows (Ánh xạ ổ đĩa mạng…) và coi iPhone hoặc iPad như ổ đĩa mạng thông thường.

Hướng dẫn chi tiết có sẵn [tại đây](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (nay là Finder File Sharing trên macOS Catalina và mới hơn) cho phép bạn truyền tệp bằng cáp Lightning hoặc USB-C. Kết nối thiết bị, mở Finder trên Mac (hoặc iTunes trên Windows), tìm Evervideo trong danh sách ứng dụng và sao chép tệp vào thư mục chia sẻ của nó.

## Kết nối ổ USB Flash hoặc thẻ SD

Cắm ổ USB hoặc thẻ SD vào iPhone, iPad hoặc Mac qua bộ chuyển đổi Lightning-to-USB / USB-C hoặc đầu đọc thẻ. Mở Tệp → Tệp trên iPhone này → Mở thư mục, điều hướng đến ổ đĩa và chọn tệp video hoặc thư mục. Evervideo phát tệp trực tiếp từ ổ đĩa mà không cần sao chép vào bộ nhớ trong — tiện lợi cho thư viện 4K rất lớn.

## Duyệt thư mục trong các bộ nhớ đã kết nối

Nhấn vào bất kỳ dịch vụ đám mây đã kết nối nào để mở trình duyệt tệp của nó. Các thư mục hiển thị hình thu nhỏ video khi có sẵn, và nhấn vào video sẽ bắt đầu phát lại ngay lập tức trong khi tiếp tục phát trực tuyến phần còn lại của tệp trong nền.

{{< cards cols="1">}}
  {{< card title="" subtitle="Duyệt thư mục trong các bộ nhớ đã kết nối của Evervideo" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Truy cập nhanh

Phần Truy cập nhanh nằm ở đầu tab Tệp. Nó cung cấp quyền truy cập nhanh vào các tệp và thư mục yêu thích và gần đây đã mở — cả từ dịch vụ đám mây và từ bộ nhớ trên thiết bị. Mỗi khi bạn mở tệp hoặc thư mục từ đám mây, nó được thêm vào danh sách Đã mở gần đây. Bạn có thể đánh dấu các thư mục lồng sâu là Yêu thích để truy cập nhanh mà không cần phải đào qua cấu trúc thư mục.

{{< cards cols="1">}}
  {{< card title="" subtitle="Liên kết trực tuyến và truy cập nhanh Evervideo" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Tệp trong ứng dụng này

Phần này hiển thị các tệp và thư mục được lưu trữ trong thư mục Documents sandbox của Evervideo — mọi thứ bạn đã tải xuống từ đám mây, truyền qua Wi-Fi Drive, sao chép qua Finder File Sharing hoặc nhập từ ứng dụng khác.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tệp trong ứng dụng Evervideo" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Thư mục Documents

Thư mục Documents là gốc của mọi thứ bên trong Tệp trong ứng dụng này. Bạn có thể tạo thư mục con, đổi tên tệp, di chuyển chúng và sắp xếp theo ý thích.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tệp cục bộ Evervideo — Thư mục Documents" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Tệp trên iPhone / iPad / Mac này

Phần này hiển thị các video nằm trên thiết bị của bạn nhưng trong các ứng dụng khác. Bạn có thể nhập chúng vào Evervideo bằng trình chọn tệp hệ thống:

- Nhấn Mở tệp… để chọn các tệp cụ thể.
- Nhấn Mở thư mục… để chọn toàn bộ thư mục.

Bạn cũng có thể sử dụng Kết nối thư mục để tạo liên kết đến thư mục trên thiết bị với quyền truy cập đọc / ghi — hoàn hảo để làm việc với thư mục trên iCloud Drive hoặc ổ USB gắn kèm mà không cần sao chép bất cứ thứ gì.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tệp trên thiết bị này trong Evervideo" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Thư mục đặc biệt

Trong tab Tệp bạn sẽ thấy một số thư mục đặc biệt mà Evervideo tạo và sử dụng tự động:

- **Tải xuống** — mọi tệp được tải xuống từ đám mây xuất hiện ở đây theo mặc định. Tùy chỉnh trong Cài đặt → Trình quản lý tệp → Lưu tệp đã tải xuống vào.
- **Bộ nhớ đệm trình phát** — bộ nhớ đệm trình phát phương tiện. Theo mặc định trình phát tải xuống các video sắp tới để phát lại mượt mà. Bạn có thể tắt bộ nhớ đệm trong cài đặt ứng dụng hoặc đơn giản là xóa thư mục này.
- **iCloud** — các tệp trong thư mục này đồng bộ trên tất cả các thiết bị kết nối với cùng tài khoản iCloud.
- **Thư mục ngoại tuyến** — khi bạn đánh dấu thư mục, danh sách phát, album hoặc thể loại là có sẵn ngoại tuyến, các tệp được tải xuống vào thư mục này.

## Thanh công cụ trên cùng

Thanh công cụ trên cùng, nằm dưới thanh điều hướng, cung cấp một số hành động bạn có thể hiển thị hoặc ẩn bằng cử chỉ vuốt xuống:

- **Tìm kiếm** — thực hiện tìm kiếm trong thư mục hoặc phần hiện tại.
- **Tiếp tục phát** — nếu được bật trong cài đặt, khôi phục hàng đợi trình phát và vị trí video cuối cùng cho thư mục hiện tại.
- **Phát tất cả** — quét thư mục hiện tại và các thư mục con và thêm tệp vào hàng đợi trình phát.
- **Phát ngẫu nhiên** — giống Phát tất cả, nhưng xáo trộn trước khi thêm.

## Tùy chọn thư mục

Khi bạn mở thư mục, nhấn nút **«...»** ở góc trên bên phải để xem các hành động này:

- **Chọn** — kích hoạt chế độ chọn tệp.
- **Thư mục mới** — tạo thư mục mới trong thư mục hiện tại.
- **Bật chế độ ngoại tuyến** — bật đồng bộ ngoại tuyến cho thư mục hiện tại. Các tệp mới được thêm trực tuyến sẽ tự động tải xuống.
- **Tải lên tệp** — tải tệp từ thiết bị của bạn lên thư mục trực tuyến.
- **Tìm kiếm** — tìm kiếm trong thư mục.
- **Sắp xếp** — sắp xếp tệp theo tên, kích thước, ngày sửa đổi hoặc siêu dữ liệu.
- **Chế độ xem lưới / danh sách** — chuyển đổi giữa chế độ xem bảng và chế độ xem hình thu nhỏ. Chế độ xem hình thu nhỏ hiển thị bản xem trước poster video lớn.

## Chế độ chọn

Nhấn **«...»** ở góc trên bên phải và chọn **Chọn** để vào chế độ chọn. Hộp kiểm xuất hiện bên cạnh mọi tệp và thư mục. Nhấn để chọn một hoặc nhiều mục, sau đó thực hiện các hành động hàng loạt: Phát tiếp theo, Phát sau, Thêm vào thư viện phương tiện, Thêm vào danh sách phát, Sao chép, Tải lên, Di chuyển, Đổi tên hoặc Xóa.

{{< cards cols="1">}}
  {{< card title="" subtitle="Chế độ chọn trong trình quản lý tệp Evervideo" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Nếu bạn muốn coi lưu trữ đám mây đã kết nối là chỉ đọc (để ngăn xóa nhầm), hãy bật Cài đặt → Trình quản lý tệp → Chỉnh sửa tệp trực tuyến → Tắt để ẩn tất cả các thao tác phá hủy khỏi giao diện.

## Hành động tệp

Nhấn biểu tượng **«...»** gần tiêu đề tệp để hiển thị menu hành động:

- **Phát tiếp theo** — chèn tệp vào đầu hàng đợi trình phát.
- **Phát sau** — thêm tệp vào cuối hàng đợi trình phát.
- **Thêm vào thư viện phương tiện** — kết hợp tệp vào thư viện phương tiện, được sắp xếp theo Album và Thể loại.
- **Thêm vào danh sách phát** — thêm tệp vào danh sách phát hiện có hoặc tạo danh sách phát mới.
- **Chỉnh sửa thẻ** — mở trình chỉnh sửa thẻ tích hợp để sửa đổi siêu dữ liệu. Đối với tệp trực tuyến, tệp được tải xuống tạm thời, chỉnh sửa rồi tải lên lại sau khi bạn xác nhận.
- **Thêm vào yêu thích** — thêm tệp vào danh sách yêu thích để truy cập nhanh.
- **Tải xuống** — tải tệp hoặc thư mục về thiết bị để sử dụng ngoại tuyến.
- **Đổi tên** — đổi tên tệp trực tiếp trên bộ nhớ từ xa.
- **Di chuyển** — di chuyển tệp đến thư mục khác trong lưu trữ đám mây.
- **Thêm vào kho lưu trữ** — đóng gói tệp vào một tệp ZIP duy nhất (tính năng Premium).
- **Mở bằng** — xuất tệp sang ứng dụng tương thích khác qua trang chia sẻ hệ thống.
- **Xóa** — xóa vĩnh viễn tệp. **Hành động này không thể hoàn tác.**

## Hành động thư mục

Đối với mỗi thư mục trong lưu trữ đám mây, bạn có nhiều hành động có sẵn bằng cách nhấn biểu tượng **«...»** bên cạnh tiêu đề thư mục.

- **Phát tất cả** — thay thế hàng đợi trình phát hiện tại bằng mọi video trong thư mục.
- **Phát tiếp theo / Phát sau** — thêm toàn bộ thư mục vào hàng đợi.
- **Thêm vào thư viện phương tiện** — kết hợp nội dung thư mục vào thư viện phương tiện.
- **Thêm vào danh sách phát** — thêm toàn bộ thư mục vào danh sách phát.
- **Thêm vào yêu thích** — thêm thư mục vào yêu thích.
- **Bật chế độ ngoại tuyến** — ngoài việc tải xuống đơn giản, tính năng này liên tục theo dõi thư mục để tìm tệp mới và tự động tải xuống khi chúng xuất hiện trực tuyến.
- **Tải xuống** — tải toàn bộ nội dung thư mục về thiết bị để truy cập ngoại tuyến.
- **Đổi tên / Di chuyển** — đổi tên hoặc di chuyển thư mục trên bộ nhớ từ xa.
- **Thêm vào kho lưu trữ** — đóng gói nội dung thư mục vào tệp ZIP (tính năng Premium).
- **Xóa** — xóa vĩnh viễn thư mục và nội dung của nó. **Hành động này không thể hoàn tác.**

## Hàng đợi truyền tải

Ở góc trên bên phải của tab Tệp có nút **Truyền tải** (biểu tượng mũi tên quay). Nhấn vào đó để mở Hàng đợi truyền tải — danh sách mọi lượt tải xuống và tải lên đang hoạt động từ tất cả các nguồn, với tiến độ thời gian thực, tốc độ và ETA cho từng tệp.

{{< cards cols="1">}}
  {{< card title="" subtitle="Hàng đợi truyền tệp Evervideo" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Bạn có thể tạm dừng, tiếp tục, thử lại các lần truyền thất bại, sắp xếp lại các mục để ưu tiên tải xuống cụ thể hoặc hủy chúng riêng lẻ. Bạn cũng có thể điều chỉnh tốc độ hàng đợi truyền (số tác vụ song song tối đa), loại mạng (chỉ Wi-Fi hoặc Wi-Fi + Mạng di động) và truyền tải nền trong Cài đặt → Trình quản lý tệp.

{{< cards cols="1">}}
  {{< card title="" subtitle="Hành động trên hàng đợi truyền tệp Evervideo" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Chế độ ngoại tuyến và thư mục ngoại tuyến đồng bộ hóa

Chế độ ngoại tuyến là tính năng tiện lợi cho phép bạn xem các video yêu thích ngay cả khi không kết nối internet. Khi bạn bật chế độ ngoại tuyến cho bất kỳ thư mục, danh sách phát, album hoặc thể loại nào, tất cả tệp trong bộ sưu tập đó sẽ tự động được tải xuống thiết bị để phát lại ngoại tuyến. Chúng xuất hiện trong phần Thư mục ngoại tuyến.

Khi bạn thêm tệp mới lên máy chủ từ xa, chúng cũng tự động được tải xuống — vì vậy bộ sưu tập ngoại tuyến của bạn luôn cập nhật mà không cần bạn làm gì. Để đồng bộ lại thủ công, nhấn ba chấm ở góc trên bên phải của thư mục ngoại tuyến và chọn Đồng bộ hóa.

Bạn có thể điều chỉnh thời gian chờ đồng bộ hóa trong Cài đặt → Trình quản lý tệp → Thư mục ngoại tuyến đồng bộ hóa → Khoảng thời gian.

Hướng dẫn chi tiết có sẵn [tại đây](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Cá nhân hóa

Trong Cài đặt → Cá nhân hóa bạn có thể cấu hình cách tab Tệp được trình bày:

- **Kiểu màn hình tệp** — Menu đơn giản (hiển thị danh sách thư mục trực tiếp) hoặc Menu theo nhóm (nhóm nội dung theo danh mục — Truy cập nhanh, Thư mục đặc biệt, Lưu trữ đám mây, v.v.).
