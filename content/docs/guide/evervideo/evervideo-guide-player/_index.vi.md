---
title: "Trình phát phương tiện"
date: 2020-02-01
lastmod: 2026-06-01
description: "Tìm hiểu cách sử dụng trình phát phương tiện Evervideo trên iPhone, iPad và Mac. Picture-in-Picture, giải mã phần cứng H.264 / HEVC, bộ chỉnh âm thanh và video, phụ đề chính và phụ, chọn track âm thanh và video, tỷ lệ và xoay video, tốc độ phát lại, hẹn giờ ngủ, AirPlay 2, Google Chromecast, luồng RTSP và trình phát nhỏ gọn luôn hiển thị trên màn hình."
keywords: [
  "hướng dẫn trình phát Evervideo", "cài đặt trình phát video", "bộ chỉnh Evervideo",
  "Picture-in-Picture iPhone", "PiP video iPad", "PiP video Mac",
  "AirPlay 2 video", "Google Chromecast video",
  "phụ đề video iPhone", "phụ đề SRT bên ngoài",
  "trình phát phụ đề ASS SSA", "libass iOS",
  "phụ đề kép học ngôn ngữ",
  "bộ chỉnh video độ sáng độ tương phản", "bộ chỉnh âm thanh trình phát video",
  "khóa xoay trình phát video", "chế độ tỷ lệ video iOS",
  "bộ giải mã H.264 phần cứng iPhone", "bộ giải mã HEVC phần cứng iPad",
  "tốc độ phát lại video", "trình phát video FFmpeg iOS",
  "trình phát RTSP iPhone", "trình phát video nhỏ gọn",
  "trình phát video VR 360 iPhone"
]
tags: ["hướng dẫn", "evervideo", "trình phát", "PiP", "phụ đề", "bộ chỉnh video"]
readingTime: 14
---


Trình phát phương tiện là màn hình chính của ứng dụng nơi bạn điều khiển phát lại và hầu hết các tính năng của Evervideo. Nó phát cả tệp video và âm thanh và được xây dựng trên công cụ phát tùy chỉnh dựa trên FFmpeg với giải mã phần cứng H.264 và HEVC thực hiện công việc nặng nhọc. Hãy khám phá cách sử dụng nó.

## Truy cập trình phát phương tiện

Bạn có thể đến trình phát toàn màn hình từ thanh trình phát nhỏ gọn. Trên iPhone, trình phát nhỏ gọn nằm ở đầu màn hình chính. Trên iPad và Mac, nó ở phía bên trái (hoặc đầu của bảng điều khiển chính). Để thu gọn trình phát toàn màn hình về chế độ xem nhỏ gọn, nhấn nút đóng ở góc dưới bên phải hoặc vuốt xuống. Để hoàn toàn ẩn trình phát nhỏ gọn, nhấn và vuốt xuống một lần nữa.

Trình phát nhỏ gọn vẫn hiển thị trong khi bạn duyệt thư viện, trình quản lý tệp hoặc cài đặt, vì vậy bạn không bao giờ mất video trong khi tìm kiếm video tiếp theo.

{{< cards cols="1">}}
  {{< card title="" subtitle="Trình phát phương tiện toàn màn hình Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Định dạng video và âm thanh được hỗ trợ

Evervideo phát hầu hết mọi container và codec hiện đại thông qua công cụ FFmpeg được tích hợp, với giải mã phần cứng H.264 và HEVC trên các thiết bị được hỗ trợ.

- **Container video:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — và nhiều hơn nữa.
- **Codec video:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — cộng với hầu hết mọi codec khác mà FFmpeg hỗ trợ.
- **Codec âm thanh:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — và nhiều hơn nữa.
- **Định dạng phụ đề:** SRT, VTT (WebVTT), ASS / SSA và track phụ đề văn bản hoặc hình ảnh nhúng.
- **Giao thức phát trực tuyến:** HTTP / HTTPS, HLS (m3u8), RTSP (camera IP và IPTV), và phát trực tiếp tệp qua SMB / WebDAV / FTP / SFTP / NFS / DLNA.

Điều đó bao gồm hầu hết mọi tệp video bạn có thể gặp — bao gồm rip MKV, luồng RTSP camera an ninh và tải xuống AV1 webm.

## Điều khiển phát lại

Ở cuối màn hình trình phát, bạn sẽ thấy các nút Phát, Dừng, Tiếp theo và Trước. Cũng có các nút tùy chọn như Bỏ qua tiến và Bỏ qua lùi (mặc định 10 giây) mà bạn có thể bật trong cài đặt ứng dụng. Giữ nút Tiếp theo / Trước để tua nhanh hoặc tua lùi. Kéo thanh trượt phát lại để chuyển đến bất kỳ vị trí nào.

## Lặp lại và phát ngẫu nhiên

Nhấn nút lặp lại để chuyển đổi giữa các chế độ:

- **Lặp lại tất cả** — phát vòng lặp mọi video trong hàng đợi.
- **Lặp lại một** — chỉ lặp lại video hiện tại.
- **Dừng lặp lại** — tạm dừng khi video hiện tại kết thúc.
- **Không lặp lại** — phát hàng đợi một lần mà không lặp lại.

Sử dụng nút **Phát ngẫu nhiên** để ngẫu nhiên hóa thứ tự video trong hàng đợi.

## Picture-in-Picture (PiP)

Trên iPhone và iPad, Evervideo hỗ trợ đầy đủ Picture-in-Picture (PiP). Nhấn biểu tượng PiP trên màn hình trình phát hoặc đơn giản chuyển Evervideo vào nền — video tiếp tục phát trong cửa sổ nổi phía trên tất cả các ứng dụng khác. Kéo cửa sổ nổi đến bất kỳ góc nào; chụm để thay đổi kích thước; nhấn một lần để hiển thị các điều khiển phát / dừng / bỏ qua cơ bản; nhấn nút mở rộng nhỏ để quay lại Evervideo đầy đủ.

PiP hoạt động với mọi định dạng video Evervideo phát, bao gồm các tệp phát trực tuyến từ đám mây và luồng RTSP. PiP cũng tiếp tục chạy khi điện thoại bị khóa (tùy thuộc vào cài đặt Tự động khóa).

## Trình phát nhỏ gọn

Trình phát nhỏ gọn là mini-player liên tục vẫn hiển thị ở đầu mọi màn hình trong ứng dụng khi bạn duyệt thư viện, trình quản lý tệp hoặc cài đặt. Nhấn vào đó để mở rộng thành trình phát toàn màn hình; vuốt xuống để thu gọn lại.

{{< cards cols="1">}}
  {{< card title="" subtitle="Cài đặt video Evervideo từ trình phát nhỏ gọn trên màn hình chính" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

Để dùng AirPlay, nhấn nút AirPlay trên trình phát. Evervideo hỗ trợ AirPlay 2, vì vậy bạn có thể phát trực tuyến video lên Apple TV, HomePod hoặc bất kỳ loa hoặc TV thông minh nào tương thích AirPlay 2. Trong cài đặt với nhiều thiết bị AirPlay, bạn có thể định tuyến âm thanh đến nhiều thiết bị nhận đồng thời.

## Google Chromecast

Đối với người dùng Google Cast, biểu tượng Cast xuất hiện trên trình phát. Nhấn vào đó để chọn thiết bị và bắt đầu truyền. Đảm bảo điện thoại và thiết bị nhận Cast đang cùng mạng Wi-Fi. Không phải mọi codec đều được phần cứng Chromecast hỗ trợ — một số tệp có thể cần chuyển mã.

## Luồng RTSP trực tiếp

Evervideo có thể phát các nguồn RTSP trực tiếp — camera IP, camera chuông cửa, luồng IPTV, nguồn phát sóng và bất kỳ URL `rtsp://` nào. Thêm luồng như kết nối RTSP trong Tệp → Liên kết trực tuyến → Thêm liên kết, sau đó nhấn vào để bắt đầu xem. Luồng RTSP hoạt động trong Picture-in-Picture, trình phát nhỏ gọn và truyền qua AirPlay 2 và Chromecast giống như video thông thường.

## Chọn track âm thanh

Đối với video có nhiều track âm thanh (bình luận, lồng tiếng ngôn ngữ thay thế, track của đạo diễn), nhấn nút Thêm hành động trên trình phát và chọn Track âm thanh — sau đó chọn track bạn muốn. Điều này rất cần thiết cho phim nước ngoài, tệp BDMV / MKV với nhiều bản lồng tiếng và nội dung giáo dục với track bình luận.

## Chọn track video

Một số tệp video bao gồm nhiều luồng video (Blu-ray đa góc, bản cắt thay thế). Chọn Track video từ menu Thêm hành động để chuyển đổi giữa chúng trong khi phát lại.

## Phụ đề — Nội bộ và Bên ngoài

Evervideo cung cấp cho bạn quyền kiểm soát chi tiết đối với phụ đề:

- **Track phụ đề** — chọn từ các track được nhúng trong tệp.
- **Tệp phụ đề bên ngoài** — tải tệp `.srt`, `.vtt`, `.ass` hoặc `.ssa` từ thiết bị, iCloud Drive hoặc bất kỳ dịch vụ đám mây đã kết nối nào.
- **Hiển thị Libass** — kiểu dáng ASS / SSA nâng cao (phông chữ, màu sắc, vị trí, hiệu ứng karaoke) được hiển thị chính xác nhờ libass được tích hợp.
- **Chọn phông chữ** — chọn phông chữ tùy chỉnh cho track phụ đề chính và phông chữ riêng biệt cho phụ đề phụ. Phông chữ được tích hợp cùng với bất kỳ phông chữ nào được cài đặt trên thiết bị đều có sẵn.

Bạn có thể cấu hình tất cả những điều này trong Cài đặt → Phụ đề trước khi phát lại, hoặc sử dụng Thêm hành động → Phụ đề từ trình phát để chuyển đổi trong khi phát.

## Bộ chỉnh âm thanh

Evervideo bao gồm bộ chỉnh âm thanh đầy đủ để điều chỉnh âm thanh video cho tai nghe, loa hoặc hệ thống hi-fi của bạn. Nhấn biểu tượng bộ chỉnh trên thanh âm lượng (hoặc hành động Bộ chỉnh âm thanh trong menu Thêm hành động của trình phát), bật bộ chỉnh với công tắc ở góc trên bên phải, và chọn preset hoặc kéo thanh trượt để tạo preset của riêng bạn. Các preset tùy chỉnh có thể được xuất và nhập để chia sẻ chúng trên các thiết bị hoặc sao lưu.

## Bộ chỉnh video

Để điều chỉnh hình ảnh, Evervideo cung cấp bộ chỉnh video chuyên dụng — điều chỉnh độ sáng, độ tương phản, độ bão hòa và sắc độ trong thời gian thực trong khi phát lại. Giống như bộ chỉnh âm thanh, các preset video tùy chỉnh có thể được xuất và nhập để chia sẻ hoặc sao lưu. Sử dụng nó để làm sáng cảnh tối trong ngày nắng, tăng độ bão hòa trên nội dung phai màu, hoặc làm ấm màu sắc lạnh.

{{< cards cols="1">}}
  {{< card title="" subtitle="Bộ chỉnh video Evervideo" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Chế độ tỷ lệ video

Chọn cách video lấp đầy màn hình:

- **Vừa vặn** — giữ nguyên tỷ lệ khung hình gốc; thanh đen nơi cần thiết.
- **Lấp đầy** — lấp đầy toàn bộ màn hình, cắt video nếu cần.
- **Kéo giãn** — kéo giãn video để lấp đầy màn hình, biến dạng nếu cần.
- **Gốc** — giữ độ phân giải gốc 1:1.

## Xoay video

Đối với video được quay sai hướng, chọn **Thêm hành động → Xoay** và chọn **0°**, **90°**, **180°** hoặc **270°** để xoay hình ảnh mà không cần rời trình phát.

## Giải mã phần cứng (H.264 và HEVC)

Trong Cài đặt → Trình phát → Video, bạn có thể bật / tắt Giải mã phần cứng H.264 và Giải mã phần cứng H.265 (HEVC) độc lập. Giải mã phần cứng nhanh hơn, tiêu thụ ít pin hơn và chạy mát hơn — nhưng trong những trường hợp hiếm hoi (tệp bị hỏng, hồ sơ kỳ lạ) bạn có thể cần tắt giải mã phần cứng và quay lại giải mã phần mềm FFmpeg. Evervideo cho phép bạn thực hiện điều đó từng tệp từ menu Thêm hành động của trình phát.

## Cổng nhìn VR 360°

Evervideo bao gồm cổng nhìn VR / 360° cho các tệp video cầu. Khi phát video 360°, bạn có thể kéo để nhìn xung quanh, chụm để thu phóng và Evervideo sẽ làm cong quá trình hiển thị trong thời gian thực.

## Tốc độ phát lại

Nhấn điều khiển Tốc độ trên thanh công cụ trình phát để thay đổi tốc độ phát lại — làm chậm để phân tích (0,25× hoặc 0,5×) hoặc tăng tốc cho hướng dẫn và bài giảng (1,25×, 1,5×, 2× và lên đến 3×). Nhấn biểu tượng cấu hình ở góc trên bên phải của màn hình Tốc độ để chuyển sang chế độ chính xác với các điều chỉnh tinh tế hơn. Cũng có sẵn hiệu chỉnh tông điệu theo từng track.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tốc độ phát lại Evervideo trên thanh công cụ chính" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Hàng đợi trình phát

Để xem hàng đợi trình phát, nhấn nút hàng đợi trên trình phát. Mỗi video trong hàng đợi có thêm hành động — nhấn ba chấm để xem chúng. Để sắp xếp lại video trong hàng đợi, sử dụng chỉ báo sắp xếp lại gần tiêu đề và kéo đến vị trí mới.

{{< cards cols="1">}}
  {{< card title="" subtitle="Hàng đợi phát lại Evervideo" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Hẹn giờ ngủ

Mở Cài đặt → Trình phát → Hẹn giờ ngủ, bật nó và chọn thời gian bạn muốn phát lại tiếp tục trước khi tự động dừng. Bạn cũng có thể thêm nút Hẹn giờ ngủ trực tiếp vào màn hình trình phát chính qua Cài đặt → Trình phát → Cá nhân hóa → Hành động màn hình chính.

## Dấu trang trình phát

Lưu vị trí của bạn trong các video dài — bài giảng, sách nói-trên-video, hướng dẫn, tải xuống YouTube dài hàng giờ — bằng cách nhấn Thêm dấu trang từ menu Thêm hành động. Dấu trang xuất hiện trong danh sách Thêm hành động → Dấu trang của video và tồn tại giữa các phiên.

## Menu Thêm hành động

Nhấn nút **Thêm hành động «...»** trên trình phát để truy cập các chức năng bổ sung.

- **Tiếp tục phát** — tiếp tục hàng đợi từ vị trí cuối cùng.
- **Tìm kiếm** — tìm video cụ thể trong hàng đợi.
- **Đánh dấu trang** — xem và chuyển đến các dấu trang.
- **Tốc độ** — điều chỉnh tốc độ phát lại.
- **Gần đây** — các video đã phát gần đây.
- **Yêu thích** — các video yêu thích.
- **Bộ chỉnh âm thanh** — kích hoạt bộ chỉnh âm thanh.
- **Bộ chỉnh video** — kích hoạt bộ chỉnh video.
- **Track âm thanh** — chọn luồng âm thanh.
- **Track video** — chọn luồng video.
- **Phụ đề** — track chính / phụ, tệp bên ngoài, phông chữ.
- **Xoay** — xoay hình ảnh 0° / 90° / 180° / 270°.
- **Chế độ tỷ lệ** — Vừa vặn / Lấp đầy / Kéo giãn / Gốc.
- **Picture-in-Picture** — vào chế độ PiP.
- **AirPlay** / **Chromecast** — gửi đến thiết bị.
- **Hẹn giờ ngủ** — đặt bộ hẹn giờ để dừng phát lại.
- **Lưu hàng đợi thành danh sách phát** — lưu hàng đợi hiện tại như danh sách phát mới.
- **Xóa hàng đợi** — xóa hàng đợi và dừng phát lại.
- **Cài đặt** — chuyển thẳng đến cài đặt trình phát.
- **Trợ giúp** — mở hướng dẫn.

{{< cards cols="1">}}
  {{< card title="" subtitle="Màn hình Thêm hành động trình phát Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Cài đặt trình phát

Cây cài đặt trình phát đầy đủ được ghi lại trong [hướng dẫn Cài đặt](/docs/guide/evervideo/evervideo-guide-settings/). Các phần được sử dụng nhiều nhất:

- **Chung chung** — Chế độ lặp lại, Chế độ phát ngẫu nhiên, Lưu trạng thái trình phát, Lưu vị trí phát lại, Khoảng thời gian bỏ qua.
- **Video** — Giải mã phần cứng H.264 / HEVC, bộ chỉnh video, chế độ tỷ lệ, xoay, chế độ hiển thị, FPS ưu tiên, định dạng pixel ưu tiên, cổng nhìn VR.
- **Âm thanh** — Bộ chỉnh âm thanh, tần số lấy mẫu, kênh, thời lượng bộ đệm IO, chế độ hỗn hợp.
- **Phụ đề** — Track chính / phụ, chọn tệp bên ngoài, phông chữ, phông chữ phụ.
- **Thiết bị** (iOS) — AirPlay / Chromecast.
- **Cá nhân hóa** — Kiểu bố cục trình phát (Tối giản / Dưới / Cổ điển / Cổ điển), hành động màn hình chính, điều khiển màn hình khóa.
- **Bộ nhớ đệm phát lại** — Bộ nhớ đệm đĩa để phát trực tuyến mượt hơn.
- **Hẹn giờ ngủ** — Dừng tự động.

## Khả năng tiếp cận

Evervideo hoàn toàn có thể tiếp cận với VoiceOver. Mọi thành phần đều có nhãn và mô tả được thiết kế tốt. Khi VoiceOver hoạt động, ứng dụng chuyển sang Chế độ văn bản để chỉ hiển thị các yếu tố có ý nghĩa — cải thiện tốc độ điều hướng và sự rõ ràng. Bạn cũng có thể kích hoạt Chế độ văn bản trong Cài đặt → Khả năng tiếp cận → Chế độ văn bản.

### Điều chỉnh thanh trượt với VoiceOver

1. **Chọn thanh trượt** — vuốt sang trái hoặc phải cho đến khi VoiceOver thông báo nó.
2. **Điều chỉnh giá trị** — nhấp đúp và giữ thanh trượt, sau đó kéo lên hoặc xuống để thay đổi giá trị nhanh chóng. VoiceOver thông báo giá trị mới khi bạn thay đổi.

Các thành phần khác hoạt động như mong đợi, sử dụng các mẫu VoiceOver do hệ thống cung cấp.
