---
date: 2020-01-01
lastmod: 2026-06-01
title: "Evervideo"
description: "Tìm hiểu cách sử dụng Evervideo — trình phát video đám mây tất cả trong một cho iPhone, iPad và Mac. Phát trực tuyến và tải xuống video từ iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, NFS, FTP / SFTP, DLNA và S3 — cùng với Plex, Jellyfin, Emby, Subsonic và Navidrome. Picture-in-Picture, phụ đề chính và phụ, bộ chỉnh âm thanh và video, luồng camera IP qua RTSP, Chromecast, AirPlay 2, giải mã phần cứng H.264 / HEVC, tích hợp thư viện Photos và Apple Music, và trình phát nhỏ gọn luôn hiển thị trên màn hình."
keywords: [
  "hướng dẫn Evervideo", "cách dùng Evervideo", "trình phát video đám mây iPhone", "trình phát video Mac",
  "trình phát MKV iOS", "trình phát video FFmpeg", "trình phát video HEVC iPhone",
  "video Picture-in-Picture iPhone", "trình phát video PiP iPad",
  "trình phát RTSP iPhone", "xem camera IP", "trình phát video DLNA",
  "Plex client iPhone", "Jellyfin client iOS", "Emby client iPad",
  "trình phát phụ đề iOS", "phụ đề SRT VTT ASS", "phụ đề phụ iPhone",
  "bộ chỉnh video iOS", "bộ chỉnh âm thanh trình phát video", "DAC ngoài video",
  "phát video từ Google Drive", "phát video từ Dropbox",
  "phát video từ OneDrive", "phát video từ iCloud Drive",
  "phát video từ MEGA", "phát video từ NAS",
  "Chromecast video iPhone", "AirPlay 2 video", "trình phát video iCloud",
  "trình phát video thư viện Photos", "trình phát video Apple Music",
  "truyền video Wi-Fi Drive", "danh sách phát video M3U",
  "Evervideo Premium", "ứng dụng video chia sẻ gia đình"
]
tags: ["evervideo", "hướng dẫn", "trình phát video", "PiP", "phụ đề", "RTSP", "đám mây", "FFmpeg"]
---


### Chào mừng đến với Hướng dẫn Evervideo

Evervideo là trình phát phương tiện đám mây đầy đủ tính năng cho iPhone, iPad và Mac, biến mọi tài khoản lưu trữ đám mây, NAS hoặc máy chủ phương tiện thành thư viện phương tiện cá nhân của bạn — không cần tải lên lại và vẫn giữ toàn quyền kiểm soát tệp của bạn.

Được xây dựng trên công cụ phát tùy chỉnh dựa trên FFmpeg với giải mã phần cứng H.264 và HEVC, Evervideo phát hầu hết mọi container và codec hiện đại — MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS và nhiều định dạng FFmpeg khác — ở chất lượng đầy đủ với bộ đệm thông minh để phát trực tuyến mượt mà qua Wi-Fi hoặc mạng di động. Picture-in-Picture giữ video của bạn hiển thị trên tất cả các ứng dụng khác, trình phát nhỏ gọn luôn hiển thị trên màn hình cho phép bạn tiếp tục xem trong khi duyệt thư viện, và Chromecast cùng AirPlay 2 phát lên TV, HomePod hoặc loa chỉ với một chạm.

Evervideo kết nối với danh sách nguồn rộng rãi, tất cả từ một ứng dụng:

- **Lưu trữ đám mây cá nhân:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Máy chủ phương tiện tự lưu trữ:** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud (và ownCloud qua API dùng chung) · Synology Drive · QNAP.
- **Giao thức NAS và chia sẻ tệp:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (mật khẩu hoặc xác thực khóa công khai) · NFS · DLNA · UPnP.
- **Luồng trực tiếp và camera IP:** RTSP — trỏ Evervideo vào bất kỳ URL RTSP nào (`rtsp://camera-ip/stream`) và nó phát ngay.
- **Lưu trữ đối tượng tương thích S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces và bất kỳ endpoint S3 API nào khác.
- **Nguồn trên thiết bị:** thư viện Photos (Tất cả video, Ngắn / Trung bình / Dài, Ghi màn hình, cùng Ảnh Album của bạn), thư viện ứng dụng Music (Album, Thể loại, Danh sách phát), ổ USB / SD và Tệp cục bộ.

### Một trình phát cho mọi định dạng và codec

Trong khi hầu hết ứng dụng iOS dừng lại ở H.264 / H.265 trong MP4 / MOV, Evervideo tích hợp FFmpeg cùng với các codec hệ thống của Apple để bạn có thể phát các định dạng mà hệ thống không nhận ra — container MKV, VP9, AV1, MPEG-2, OGG, Vorbis và nhiều hơn nữa — và tự động chuyển đổi giữa giải mã phần cứng H.264 / HEVC và giải mã phần mềm dựa trên tệp và thiết bị.

Bạn có thể chọn track video (rip Blu-ray đa luồng), track âm thanh (track bình luận, lồng tiếng thay thế) và track phụ đề. Tệp phụ đề SRT, VTT và ASS / SSA bên ngoài được tải với một chạm; kiểu dáng ASS / SSA nâng cao được hiển thị chính xác nhờ libass được tích hợp.

### Phụ đề thông minh

- **Chọn track phụ đề** — hoàn hảo để học ngôn ngữ.
- **Tệp phụ đề bên ngoài** (`.srt`, `.vtt`, `.ass`, `.ssa`) được tải từ bất cứ đâu trên thiết bị hoặc từ đám mây.
- **libass** để hiển thị ASS / SSA đầy đủ kiểu dáng.
- **Chọn phông chữ theo track và toàn cục** cho phụ đề.
- **Chọn track âm thanh** — chọn lồng tiếng, bình luận hoặc track của đạo diễn.
- **Chọn track video** cho tệp đa góc hoặc đa phiên bản.

### Tinh chỉnh hình ảnh và âm thanh

Hai bộ chỉnh song song: bộ chỉnh âm thanh để điều chỉnh âm trầm và âm bổng (với nhập / xuất preset tùy chỉnh), và bộ chỉnh video để điều chỉnh độ sáng, độ tương phản, độ bão hòa và sắc độ (cũng với nhập / xuất). Cả hai công cụ còn cung cấp các điều khiển audiophile: tần số lấy mẫu đầu ra âm thanh, số kênh, thời lượng bộ đệm IO và chế độ hỗn hợp — dành cho người dùng có DAC ngoài và bộ thu nhà hát gia đình.

### Truyền, AirPlay và Picture-in-Picture

- **Picture-in-Picture (PiP):** tiếp tục xem trong khi sử dụng các ứng dụng khác.
- **AirPlay 2:** phát video lên Apple TV, HomePod hoặc bất kỳ loa / TV hỗ trợ AirPlay 2 nào.
- **Google Chromecast:** truyền trực tiếp đến Chromecast hoặc TV hỗ trợ Cast.
- **Trình phát nhỏ gọn:** mini player liên tục hiển thị trên mọi màn hình để bạn duyệt thư viện mà không mất video.

### Quyền riêng tư và bảo mật

Evervideo sử dụng SDK chính thức và đăng nhập OAuth từ mọi nhà cung cấp đám mây để mật khẩu của bạn không bao giờ đến ứng dụng. Token truy cập được lưu trữ mã hóa trong Keychain iOS/macOS, mọi truyền tải đều được bảo vệ TLS, và việc thu hồi quyền truy cập từ tài khoản đám mây (hoặc xóa Evervideo khỏi thiết bị) sẽ xóa tất cả ngay lập tức. Bảo vệ thư viện của bạn bằng mã PIN 4 chữ số tùy chọn để tăng thêm lớp bảo mật.

### Bắt đầu với Evervideo

Hướng dẫn này sẽ dẫn bạn qua từng phần của Evervideo trên iPhone, iPad và Mac — từ kết nối dịch vụ đám mây, duyệt thư viện, tải xuống và truyền tệp, quản lý danh sách phát, đến tinh chỉnh trình phát phương tiện, bộ chỉnh, phụ đề và Picture-in-Picture. Sử dụng các thẻ bên dưới để chuyển thẳng đến phần bạn cần.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="Điều hướng" subtitle="Thanh tab trên iPhone, Menu trái trên iPad và Mac, trình phát phương tiện nhỏ gọn luôn hiển thị trên màn hình." >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="Tệp" subtitle="Một tab thống nhất cho đám mây, NAS, luồng RTSP, tệp cục bộ, ổ USB và hàng đợi truyền." >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="Thư viện phương tiện" subtitle="Duyệt theo Album, Thể loại, Gần đây, Yêu thích — cùng thư viện iOS Photos và thư viện Apple Music." >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="Danh sách phát" subtitle="Tạo danh sách phát từ đám mây, cục bộ, Photos hoặc thư viện Music, nhập M3U / M3U8 / CUE." >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="Trình phát phương tiện" subtitle="Picture-in-Picture, track âm thanh và video, phụ đề, bộ chỉnh âm thanh và video, AirPlay, Chromecast." >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="Cài đặt" subtitle="Công cụ âm thanh, bộ giải mã video, phụ đề, thư viện, trình quản lý tệp, widget, cá nhân hóa, ngôn ngữ, sao lưu." >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="FAQ" subtitle="Tìm câu trả lời cho các câu hỏi phổ biến nhất về Evervideo." >}}

{{< /cards >}}
