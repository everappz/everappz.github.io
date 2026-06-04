---
title: "Trình phát Âm thanh"
date: 2020-02-01
description: "Tìm hiểu cách sử dụng trình phát âm thanh Flacbox trên iPhone, iPad và Mac. Điều khiển phát lại, quản lý hàng đợi, cấu hình bộ máy âm thanh FFmpeg / hệ thống, thay đổi tốc độ lấy mẫu, chỉnh sửa cao độ, thời gian đệm IO, bộ chỉnh âm, dấu trang âm thanh, AirPlay 2, Google Cast, CarPlay, widget và phím tắt bàn phím Mac."
keywords: [
  "hướng dẫn trình phát Flacbox", "cài đặt trình phát âm thanh", "bộ chỉnh âm Flacbox",
  "phát nhạc AirPlay", "nhạc Google Cast", "dấu trang âm thanh",
  "hàng đợi phát lại Flacbox", "lặp lại và ngẫu nhiên Flacbox", "điều chỉnh âm lượng Flacbox",
  "mini player macOS", "ứng dụng nhạc voiceover",
  "Flacbox FFmpeg", "chỉnh sửa cao độ Flacbox", "tốc độ lấy mẫu Flacbox",
  "DAC ngoài Flacbox", "âm thanh vòm Flacbox", "bộ đệm IO Flacbox",
  "tốc độ phát lại Flacbox", "hẹn giờ tắt Flacbox"
]
tags: ["hướng dẫn", "flacbox", "trình phát"]
readingTime: 14
---


Trình phát Âm thanh là màn hình chính của ứng dụng, nơi bạn điều khiển nhạc và hầu hết các tính năng phát lại. Đây cũng là nơi bộ máy âm thanh hi-res của Flacbox — được xây dựng trên các codec hệ thống cộng với thư viện **FFmpeg** đi kèm — hoạt động. Hãy cùng khám phá cách sử dụng nó.

## Truy cập Trình phát Âm thanh

Bạn có thể vào trình phát toàn màn hình từ thanh mini player. Trên iPhone, mini player nằm ở cuối màn hình chính. Trên iPad và Mac, nó ở bên trái. Để ẩn mini player trên iPhone, nhấn một lần vào nó rồi vuốt xuống. Để đóng hoàn toàn trình phát toàn màn hình, nhấn nút đóng ở góc dưới bên phải.

{{< cards cols="1">}}
  {{< card title="" subtitle="Màn hình chính Trình phát Âm thanh Flacbox" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Định dạng Âm thanh Được hỗ trợ

Flacbox phát các định dạng âm thanh phổ biến nhất — cả codec hệ thống của Apple và nhiều định dạng bổ sung được xử lý bởi bộ máy FFmpeg đi kèm:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

Điều đó bao gồm hầu hết mọi định dạng lossy và lossless hiện đại bạn có thể có trong bộ sưu tập nhạc cá nhân.

## Điều khiển Phát lại

Ở cuối màn hình trình phát, bạn sẽ thấy các nút Phát, Tạm dừng, Bài tiếp theo và Bài trước. Cũng có các nút tùy chọn như Tiếp 30 giây và Lùi 30 giây mà bạn có thể bật trong cài đặt ứng dụng (tiện cho sách nói). Bạn có thể tua nhanh hoặc tua lại bằng cách nhấn giữ nút Tiếp / Trước. Để chuyển đến một phần cụ thể của bài nhạc, kéo thanh trượt phát lại.

## Lặp lại và Ngẫu nhiên

Nhấn nút lặp lại để chuyển đổi giữa các chế độ lặp lại:

- **Lặp lại Tất cả** — lặp lại tất cả các bài nhạc trong hàng đợi.
- **Lặp lại Một** — chỉ lặp lại bài nhạc hiện tại.
- **Dừng Lặp lại** — tạm dừng khi bài nhạc hiện tại kết thúc.
- **Không Lặp lại** — phát hàng đợi một lần mà không lặp lại.

Sử dụng nút **Ngẫu nhiên** để xáo trộn thứ tự bài nhạc trong hàng đợi.

## Điều chỉnh Âm lượng

Mở màn hình Cài đặt Âm thanh bằng cách nhấn biểu tượng âm thanh bên dưới các điều khiển phát lại để truy cập thanh trượt âm lượng. Bạn cũng sẽ tìm thấy các nút **Google Cast** và **AirPlay** ở đây để nhanh chóng chuyển phát lại sang thiết bị khác.

## Google Cast (Chromecast)

Đối với người dùng Google Cast, biểu tượng **Cast** xuất hiện ở cuối trình phát. Nhấn nó để chọn thiết bị và bắt đầu phát trực tuyến. Đảm bảo thiết bị của bạn và bộ thu Google Cast đang ở cùng mạng Wi-Fi. Lưu ý: không phải mọi định dạng âm thanh đều tương thích với Google Cast — một số định dạng hi-res có thể cần được chuyển mã.

## AirPlay

Đối với AirPlay, hãy tìm nút **AirPlay** ở cuối trình phát. Nhấn nó và chọn thiết bị để phát trực tuyến. Flacbox hỗ trợ **AirPlay 2**, vì vậy bạn có thể phát đến nhiều HomePod, Apple TV hoặc loa tương thích AirPlay 2 cùng lúc.

## Bộ Chỉnh Âm

Flacbox bao gồm **bộ chỉnh âm 10 dải** với các preset theo phong cách iPod. Nhấn Bộ chỉnh âm trên chế độ xem âm lượng, sau đó bật nó ở góc trên bên phải. Bạn có thể sử dụng các preset như Acoustic và Bass Booster, hoặc điều chỉnh từng dải tần số bằng thanh trượt. Tạo preset của riêng bạn, lưu chúng với bất kỳ tên nào, và tăng âm lượng tổng thể bằng bộ khuếch đại. Chúng tôi có hướng dẫn chi tiết hơn về cách sử dụng bộ chỉnh âm [tại đây](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Bộ Chỉnh Âm Trình phát Âm thanh Flacbox" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Thanh Công cụ Chế độ Trình phát

Đối với một số kiểu trình phát, có một thanh công cụ chuyên dụng ở đầu trình phát toàn màn hình. Thanh công cụ này chứa ba nút hữu ích:

- **Tìm kiếm** — nhanh chóng tìm một bài nhạc cụ thể trong hàng đợi trình phát.
- **Điều khiển Tốc độ Phát lại** — điều chỉnh tốc độ phát lại từ 0,02× đến 3,00×. Hoàn hảo cho sách nói, podcast và bài giảng. Nhấn Bình thường để trở về tốc độ mặc định.
- **Dấu trang Âm thanh** — tạo nhiều dấu trang cho mỗi bài nhạc. Chúng tôi có hướng dẫn đầy đủ về cách sử dụng dấu trang [tại đây](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Hàng đợi Trình phát

Để xem hàng đợi trình phát, nhấn nút hàng đợi ở bên phải của bài nhạc hiện tại. Mỗi bài nhạc trong hàng đợi có thêm hành động — nhấn ba chấm để xem chúng. Để sắp xếp lại bài nhạc trong hàng đợi, sử dụng chỉ báo sắp xếp lại gần tiêu đề và kéo nó đến vị trí mới.

{{< cards cols="1">}}
  {{< card title="" subtitle="Hàng đợi Phát lại Flacbox" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Bình luận / Lời bài hát

Để xem bình luận bài nhạc và lời bài hát nhúng, cũng như file LRC, hãy làm theo các bước sau:

1. Mở **Cài đặt**.
2. Vào **Trình phát Âm thanh**.
3. Chọn **Cá nhân hóa**.
4. Nhấn **Các nút trên màn hình chính**.
5. Bật **Bình luận**.

Sau đó, nhấn nút hàng đợi trình phát ở cuối màn hình nhiều lần để chuyển từ chế độ xem artwork / hàng đợi sang chế độ xem bình luận. Trên màn hình Bình luận, vuốt phải để chuyển đổi giữa **Bình luận**, **Lời bài hát Nhúng** và **File LRC**. Hướng dẫn đầy đủ có sẵn [tại đây](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Màn hình Lời bài hát và Bình luận Flacbox" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Menu Tùy chọn

Mỗi bài nhạc trong hàng đợi trình phát âm thanh có menu với nhiều hành động hơn, truy cập bằng cách nhấn nút ba chấm gần tiêu đề bài nhạc.

- **Phát Tiếp theo** — thêm bài nhạc vào đầu hàng đợi trình phát.
- **Thêm vào Danh sách phát** — đưa bài nhạc vào danh sách phát, với tùy chọn tạo mới.
- **Thêm vào Yêu thích** — đánh dấu bài nhạc là yêu thích để truy cập nhanh.
- **Tải xuống** — lưu bài nhạc vào file cục bộ, xuất hiện trong tab **File cục bộ** và phần **Nhạc Ngoại tuyến**.
- **Chỉnh sửa Thẻ Âm thanh** — mở trình chỉnh sửa thẻ âm thanh tích hợp để sửa siêu dữ liệu còn thiếu, sửa đổi bài nhạc trên bộ nhớ của bạn.
- **Hiển thị trong Thư mục** — hiển thị thư mục nơi file âm thanh được lưu.
- **Hiển thị trong Finder** — đối với các file được nhập từ Mac, điều này hiển thị thư mục nơi file âm thanh nằm trên Mac của bạn.
- **Mở Trong** — xuất file âm thanh sang ứng dụng khác.
- **Xóa khỏi Hàng đợi** — xóa bài nhạc đã chọn khỏi hàng đợi trình phát âm thanh.
- **Xóa khỏi Dịch vụ Đám mây** — xóa bài nhạc khỏi cả thư viện nhạc và lưu trữ đám mây. **Hành động này không thể hoàn tác.**
- **Xóa khỏi File Cục bộ** — xóa bài nhạc khỏi cả thư viện nhạc và lưu trữ cục bộ. **Hành động này không thể hoàn tác.**
- **Xóa khỏi Thư viện Nhạc** — xóa bài nhạc khỏi thư viện nhạc, trong khi giữ file trong bộ nhớ.

Các tùy chọn tương tự có sẵn cho mục đang phát trong hàng đợi trình phát âm thanh, mà bạn có thể truy cập bằng cách nhấn biểu tượng **Thêm Hành động** gần tiêu đề bài nhạc.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tùy chọn Flacbox cho Mục trong Hàng đợi Phát lại" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Hành động Trình phát Bổ sung

Nhấn nút **Thêm Hành động** "..." ở bên trái tiêu đề bài nhạc đang phát để xem các hành động bổ sung.

- **Tiếp tục Phát** — tiếp tục từ nơi bạn dừng lại, bao gồm hàng đợi và vị trí phát lại. Đặc biệt hữu ích cho sách nói. Được kích hoạt trong cài đặt ứng dụng.
- **Tìm kiếm** — nhanh chóng tìm một bài nhạc cụ thể trong hàng đợi trình phát âm thanh.
- **Dấu trang** — xem danh sách các dấu trang âm thanh đã tạo.
- **Bình luận** — xem bình luận bài nhạc và lời bài hát nhúng, cũng như file LRC. Hướng dẫn đầy đủ [tại đây](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Tốc độ** — điều chỉnh tốc độ phát lại theo ý thích.
- **Gần đây** — truy cập danh sách các bài nhạc đã phát gần đây.
- **Yêu thích** — xem bộ sưu tập các bài nhạc yêu thích.
- **Bộ Chỉnh Âm** — kích hoạt bộ chỉnh âm.
- **Hẹn giờ Tắt** — đặt hẹn giờ để dừng phát lại sau một khoảng thời gian nhất định. Tuyệt vời cho những lúc bạn muốn chìm vào giấc ngủ với nhạc.
- **Lưu Hàng đợi vào Danh sách phát** — lưu hàng đợi trình phát âm thanh hiện tại dưới dạng danh sách phát mới.
- **Xóa Hàng đợi** — xóa hàng đợi trình phát và dừng phát lại.
- **Cài đặt** — truy cập cài đặt trình phát âm thanh.
- **Trợ giúp** — tìm hỗ trợ và hướng dẫn.

{{< cards cols="1">}}
  {{< card title="" subtitle="Màn hình Thêm Hành động Trình phát Âm thanh Flacbox" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Dấu trang Âm thanh

Tính năng này cho phép bạn tạo nhiều dấu trang cho các bài nhạc trong thư viện nhạc — hoàn hảo cho sách nói, bài giảng, DJ mix dài, hoặc đánh dấu điệp khúc của bài nhạc yêu thích.

Để tạo dấu trang mới:

- Bắt đầu phát bài nhạc mong muốn.
- Mở màn hình trình phát.
- Nhấn nút **Dấu trang** trên thanh công cụ chế độ trình phát.
- Chọn **Thêm Dấu trang**.
- Chọn thời gian dấu trang và nhấn **Xong** ở góc trên bên phải.

Chỉnh sửa dấu trang cho bài nhạc hiện tại rất dễ: nhấn Chỉnh sửa ở góc trên bên phải để vào chế độ chỉnh sửa. Trong chế độ này, bạn có thể sắp xếp lại dấu trang, xóa chúng, điều chỉnh thời gian dấu trang và thay đổi tiêu đề dấu trang. Hướng dẫn chi tiết hơn về dấu trang âm thanh có sẵn [tại đây](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Màn hình Dấu trang Âm thanh Flacbox" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Gần đây và Yêu thích

Trên màn hình trình phát, nhấn ba chấm để truy cập Gần đây và Yêu thích. Trong cả hai phần, bạn có thể tìm kiếm bài nhạc, phát tất cả, phát ngẫu nhiên tất cả, xuất danh sách và xóa danh sách. Chúng tôi có hướng dẫn chi tiết về cách xuất danh sách bài nhạc [tại đây](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Kết nối iPhone với xe qua USB hoặc Apple CarPlay không dây và Flacbox xuất hiện trên màn hình chính CarPlay, sẵn sàng phát nhạc an toàn khi lái xe. Giao diện CarPlay bao gồm các tab riêng cho Thư viện, Kết nối, File cục bộ và Cài đặt, với các điều khiển phát lại, ngẫu nhiên, lặp lại, quản lý hàng đợi và bộ chỉnh âm đều có sẵn mà không cần cầm điện thoại. Cấu hình thêm trải nghiệm CarPlay trong Cài đặt → CarPlay — tùy chọn sắp xếp, phân trang, màu gradient biểu tượng menu, có tải hình ảnh không, và tùy chọn tự động tạm dừng khi CarPlay kết nối.

[Đọc hướng dẫn CarPlay đầy đủ](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox trên Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Widget Màn hình chính (iPhone & iPad)

Flacbox hỗ trợ widget Màn hình chính và Màn hình khóa iOS để bạn có thể xem và điều khiển phát lại ngay. Đảm bảo Widget được bật trong Cài đặt → Widget → Bật Widget, sau đó nhấn giữ Màn hình chính hoặc Màn hình khóa, nhấn **+**, tìm kiếm **Flacbox** và thêm widget. Widget tự động cập nhật trong quá trình phát để hiển thị artwork, tiêu đề và nghệ sĩ của bài đang phát.

## Cửa sổ Mini Player (Chỉ dành cho Mac)

Người dùng Mac có thể sử dụng mini player nhỏ gọn luôn hiển thị trên cùng. Di chuyển con trỏ đến cạnh dưới bên phải của cửa sổ Flacbox, thu nhỏ xuống kích thước nhỏ nhất, và nhấn nút thu gọn. Giữ nó trên cùng của mọi cửa sổ khác bằng cách chọn Cửa sổ → Hiển thị Cửa sổ Luôn trên Cùng trong thanh menu — hoàn hảo để giữ điều khiển nhạc luôn hiển thị khi bạn làm việc trong ứng dụng khác.

## Phím tắt Bàn phím (Chỉ dành cho Mac)

Đối với người dùng Mac, menu phát lại hệ thống có sẵn trong thanh trạng thái với các phím tắt. Ví dụ: nhấn phím cách để Phát / Tạm dừng. Phím tắt cho Dừng, Bài tiếp theo, Bài trước, Bỏ qua Thời gian, Lặp lại, Ngẫu nhiên và Tốc độ Phát lại cũng có sẵn.

## Cài đặt Trình phát Âm thanh

Để truy cập cài đặt, nhấn nút Thêm trên màn hình trình phát và chọn Cài đặt. Tại đây, bạn sẽ tìm thấy một số phần, được liệt kê dưới đây.

### Chung

Những cài đặt này bao gồm các khía cạnh cơ bản của trình phát âm thanh, bao gồm hàng đợi phát lại, đầu ra âm thanh và lưu trạng thái trình phát.

- **Chế độ Lặp lại** — chọn cách trình phát âm thanh hoạt động khi bài nhạc kết thúc:
  - **Lặp lại Tất cả** — phát lại tất cả bài nhạc trong hàng đợi.
  - **Lặp lại Một** — chỉ lặp lại bài nhạc hiện tại.
  - **Dừng Lặp lại** — tạm dừng phát lại khi bài nhạc hiện tại kết thúc.
  - **Không Lặp lại** — cho phép hàng đợi phát qua mà không lặp lại.
- **Chế độ Ngẫu nhiên** — xáo trộn thứ tự bài nhạc trong hàng đợi. Bạn có thể tắt hoặc bật **Ngẫu nhiên**.
- **Codec Âm thanh** — chọn bộ máy âm thanh dùng cho phát lại:
  - **Codec Hệ thống + FFmpeg** — ưu tiên codec âm thanh của hệ thống khi có thể, tăng cường khả năng tương thích và ổn định. Chỉnh sửa cao độ và điều chỉnh tốc độ lấy mẫu đầu ra âm thanh có thể bị giới hạn trong chế độ này.
  - **FFmpeg** — buộc dùng codec FFmpeg cho tất cả file âm thanh, cho phép bạn tinh chỉnh chỉnh sửa cao độ và tốc độ lấy mẫu đầu ra âm thanh.
- **Tốc độ Lấy mẫu Đầu ra Âm thanh** — điều chỉnh tốc độ lấy mẫu đầu ra âm thanh để tối ưu hóa chất lượng âm thanh, đặc biệt hữu ích với DAC ngoài. Các giá trị có sẵn: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** và **96 kHz**.
- **Số Kênh Đầu ra Âm thanh** — đối với hệ thống âm thanh đa kênh với DAC ngoài, chỉ định số kênh: **Mono, Stereo, Center / Left / Right, Center / Left / Right / Surround, ITU BS.775-1, 5.1 Surround** và **SDDS**.
- **Thời gian Đệm IO Đầu ra Âm thanh** — cấu hình thời gian đệm đầu vào / đầu ra cho phát lại âm thanh. Giá trị điển hình để giảm thiểu độ trễ khi phát âm thanh độ phân giải cao là khoảng **5 mili giây (0,005 giây)**. Kích thước đệm chấp nhận được phụ thuộc vào phần cứng và phần mềm của bạn, vì vậy hãy thử các khoảng thời gian khác nhau trên thiết bị mục tiêu và chọn cái cân bằng tốt nhất giữa độ trễ thấp và phát lại không bị ngắt.
- **Chế độ Đầu ra Âm thanh (chỉ iOS)** — cấu hình chế độ đầu ra âm thanh hỗn hợp để âm thanh từ Flacbox kết hợp với các ứng dụng khác. Hướng dẫn chi tiết [tại đây](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Lưu Vị trí Phát lại** — đảm bảo ứng dụng lưu và khôi phục vị trí phát lại cho các bài nhạc trong thư viện nhạc.
- **Lưu Trạng thái Trình phát Âm thanh** — lưu trạng thái trình phát âm thanh trước khi bạn đóng ứng dụng. Để tiếp tục phát lại, nhấn **Tiếp tục Phát** ở đầu bất kỳ thư mục, album, nghệ sĩ hoặc thể loại nào khi bạn mở lại ứng dụng. Bạn cũng có thể khôi phục phát lại cho các file riêng lẻ bằng cách nhấn vào bài nhạc cụ thể.

Sau khi bật cả **Lưu Vị trí Phát lại** và **Lưu Trạng thái Trình phát Âm thanh**, mở bất kỳ thư mục, album, nghệ sĩ hoặc thể loại nào và bạn sẽ thấy nút **Tiếp tục Phát** ở đầu màn hình cùng với bài nhạc và vị trí được lưu cuối cùng. Nhấn nó để tiếp tục ngay nơi bạn dừng lại.

### Cá nhân hóa

Cá nhân hóa cho phép bạn tùy chỉnh giao diện màn hình trình phát âm thanh, thay đổi các điều khiển có sẵn trên màn hình chính, màn hình khóa và thanh trạng thái, và cấu hình điều khiển bỏ qua thời gian.

- **Kiểu Màn hình Trình phát Âm thanh** — cấu hình vị trí các phần tử trên màn hình trình phát âm thanh.
- **Kiểu Cuộn Ảnh bìa Album** — cấu hình kiểu cuộn ưa thích cho ảnh bìa album.
- **Phần tử Bổ sung** — bật thêm các phần tử trên màn hình trình phát âm thanh. **Thông tin Định dạng Âm thanh** hiển thị thông tin âm thanh của bài đang phát phía trên artwork; **Thanh trượt Âm lượng** hiển thị thanh trượt đầu ra âm thanh bên dưới các điều khiển phát lại.
- **Hành động Màn hình Chính** — cấu hình nút nào sẽ hiển thị trên màn hình trình phát âm thanh chính theo mặc định: **Chế độ Lặp lại và Ngẫu nhiên, Bài tiếp theo và Bài trước, Bỏ qua Thời gian, Hẹn giờ Tắt, Google Chromecast, AirPlay và Bluetooth, Bộ Chỉnh Âm, Tìm kiếm, Dấu trang, Tốc độ, Thêm Dấu trang, Thêm vào Yêu thích, Bình luận** và nhiều hơn nữa.
- **Điều khiển Phát lại trên Màn hình Khóa** — chọn điều khiển nào xuất hiện trên màn hình khóa. Các giá trị có thể: **Bỏ qua Thời gian, Thêm Dấu trang, Thêm vào Yêu thích**.
- **Nút Bỏ qua Thời gian** — chọn khoảng thời gian cho các nút **Bỏ qua Thời gian**.

### Tải File

Trong quá trình tải file, bạn có thể thay đổi loại mạng dùng để tải bài nhạc. Các tùy chọn có sẵn: **Wi-Fi**, **Wi-Fi & Dữ liệu Di động**.

- **Thời gian Tải trước** — đặt khoảng thời gian đệm. Tăng nếu bạn có kết nối mạng kém.
- **Sử dụng URL Trực tiếp** — khi được bật, URL trực tiếp được dùng để tải bài nhạc nếu máy chủ hỗ trợ. Điều này có thể tăng tốc tải bài nhạc nhưng có thể ảnh hưởng đến độ ổn định phát lại.

### Bộ Chỉnh Âm

Tùy chỉnh cài đặt bộ chỉnh âm. Bạn có thể đọc thêm về cấu hình bộ chỉnh âm [tại đây](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Tốc độ Phát lại

Điều chỉnh tốc độ phát lại của trình phát âm thanh từ **0,02× đến 3,00×**. Nhấn biểu tượng cấu hình ở góc trên bên phải để chuyển sang **chế độ chính xác** để điều chỉnh tinh tế hơn.

{{< cards cols="1">}}
  {{< card title="" subtitle="Màn hình Tốc độ Phát lại Flacbox" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Chỉnh sửa Cao độ

Thay đổi cài đặt chỉnh sửa cao độ bằng các giá trị được xác định trước. Bạn cũng có thể chuyển đổi giữa các giá trị được xác định trước và chế độ chính xác bằng cách nhấn nút ở góc trên bên phải. Chỉnh sửa cao độ có sẵn trong đường dẫn codec FFmpeg, với phạm vi từ **-1000 đến +1000**.

### Bộ nhớ đệm Phát lại

Các bài nhạc trong hàng đợi trình phát âm thanh được tự động tải xuống để đảm bảo phát lại mượt mà. Nếu bạn tải file âm thanh thủ công, bạn có thể tắt tùy chọn này để tránh trùng lặp. Bạn cũng có thể cấu hình kích thước bộ nhớ đệm trình phát âm thanh tại đây.

### Hẹn giờ Tắt

Kích hoạt hẹn giờ để tự động dừng phát lại sau một khoảng thời gian nhất định — tiện khi bạn muốn đi vào giấc ngủ cùng nhạc. Nhấn biểu tượng cấu hình ở góc trên bên phải để có **chế độ chính xác** với độ chi tiết từng phút.

## Khả năng Tiếp cận

Flacbox hoàn toàn tiếp cận được với **VoiceOver**. Mọi thành phần đều có nhãn và mô tả được thiết kế tốt. Khi VoiceOver hoạt động, ứng dụng chuyển sang **Chế độ Văn bản** để chỉ hiển thị các phần tử có ý nghĩa — cải thiện tốc độ điều hướng và sự rõ ràng. Bạn cũng có thể kích hoạt Chế độ Văn bản trong **Cài đặt → Khả năng tiếp cận → Chế độ Văn bản**.

### Điều chỉnh Thanh trượt với VoiceOver

1. **Chọn thanh trượt** — vuốt sang trái hoặc phải cho đến khi VoiceOver thông báo nó.
2. **Điều chỉnh giá trị** — nhấn đúp và giữ thanh trượt, sau đó kéo lên hoặc xuống để thay đổi giá trị nhanh chóng. VoiceOver thông báo giá trị mới khi bạn điều chỉnh.

### Điều chỉnh Vị trí Bài nhạc trong Danh sách với VoiceOver

1. Nhấn biểu tượng chỉ báo sắp xếp lại gần tiêu đề bài nhạc để cho nó trọng tâm.
2. Nhấn đúp chỉ báo sắp xếp lại nhanh chóng. Ở lần nhấn thứ hai, đừng nhả ngón tay — giữ cho đến khi bạn nghe thấy âm thanh cho biết ô sẵn sàng để di chuyển.
3. Di chuyển ô đến vị trí mới.

Các thành phần khác hoạt động như mong đợi, sử dụng các mẫu VoiceOver do hệ thống cung cấp.
