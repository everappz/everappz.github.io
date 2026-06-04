---
title: "Thư viện nhạc"
date: 2020-02-01
description: "Tìm hiểu cách xây dựng, tổ chức và đồng bộ thư viện nhạc của bạn trong Flacbox trên iPhone, iPad và Mac. Thêm bản nhạc thủ công hoặc đồng bộ từ các dịch vụ đám mây, quản lý siêu dữ liệu, ảnh bìa album, danh sách phát, yêu thích, gần đây và đánh dấu trang. Bao gồm hỗ trợ âm thanh Hi-Res, trình chỉnh sửa thẻ MusicBrainz, đồng bộ trực tuyến và ngoại tuyến, và các tùy chọn cá nhân hóa."
keywords: [
  "thư viện nhạc Flacbox", "đồng bộ nhạc từ đám mây", "tổ chức siêu dữ liệu nhạc",
  "chỉnh sửa thẻ âm thanh Flacbox", "đồng bộ nhạc ngoại tuyến", "nhập nhạc cục bộ",
  "quản lý danh sách phát Flacbox", "tìm kiếm ảnh bìa album Flacbox",
  "siêu dữ liệu nhạc iPhone", "hướng dẫn ứng dụng Flacbox",
  "Flacbox MusicBrainz", "chuẩn hóa thẻ Flacbox",
  "thư viện nhạc hi-res Flacbox", "thư viện FFmpeg Flacbox",
  "album độc lập Flacbox", "chế độ xem nhạc sĩ Flacbox"
]
tags: ["nhạc", "hướng dẫn", "flacbox", "thư viện"]
readingTime: 11
---


Quản lý thư viện nhạc trong Flacbox rất dễ dàng — bạn có thể tổ chức tất cả các bản nhạc ở định dạng FLAC, ALAC, DSD, MP3, M4A, OGG, WMA, APE và hàng chục định dạng khác vào một bộ sưu tập có thể tìm kiếm duy nhất. Bạn có hai lựa chọn để xây dựng thư viện nhạc: thêm thủ công (bạn chọn chính xác những gì được thêm) hoặc đồng bộ tự động (Flacbox quét các thư mục đám mây được chỉ định và tự động thêm file mới khi chúng xuất hiện).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Thư viện Nhạc Chế độ xem Album" image="/docs/guide/flacbox/img/media-library-albums.webp" >}}
{{< /cards >}}

## Thêm Thủ công

Để thêm bản nhạc thủ công, nhấn biểu tượng **Thêm Nhạc** ở góc trên bên trái và chọn thư mục hoặc file từ dịch vụ lưu trữ đám mây đã kết nối hoặc file trên thiết bị. Khi bạn thêm bản nhạc vào thư viện, chỉ có liên kết đến các bản nhạc đó được tạo — các file thực tế vẫn ở vị trí ban đầu để tiết kiệm dung lượng.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Thêm Bài hát vào Thư viện Nhạc" image="/docs/guide/flacbox/img/library-add-songs.webp" >}}
{{< /cards >}}

Bạn cũng có thể kéo và thả file vào thư viện trên phiên bản Mac, hoặc sử dụng **Mở File…** / **Mở Thư mục…** từ bộ chọn file hệ thống trên iPhone và iPad.

## Tiếp tục Phát

Khôi phục hàng đợi phát từ vị trí đã lưu cuối cùng nếu tính năng này được bật trong cài đặt. Bật cả **Lưu Trạng thái Trình phát Âm thanh** và **Lưu Vị trí Phát** trong Cài đặt → Trình phát Âm thanh → Chung để có trải nghiệm tốt nhất.

## Vị trí

Tất cả các bản nhạc trong thư viện được nhóm hợp lý theo loại nguồn và thẻ nhạc. Bạn có thể lọc bài hát theo vị trí bằng cách sử dụng nút **Thêm Hành động** ở góc trên bên phải và chọn **Lọc**.

### Nhạc Trực tuyến

Phần này hiển thị nhạc từ các dịch vụ lưu trữ đám mây đã kết nối. Các bản nhạc ở đây được phát trực tiếp theo yêu cầu.

### File trong Ứng dụng này

Tại đây bạn có thể tìm thấy nhạc có thể phát ngoại tuyến từ file cục bộ. Bao gồm các file trong thư mục Documents của ứng dụng.

### File trên iPhone / iPad / Mac này

Danh mục này bao gồm nhạc được nhập vào ứng dụng từ thiết bị qua hộp thoại **Mở File…**. File gốc vẫn ở vị trí ban đầu; Flacbox chỉ lưu liên kết đến chúng.

## Danh mục

Khi bạn thêm bản nhạc vào thư viện nhạc, ứng dụng tự động đọc thẻ âm thanh và tổ chức chúng thành các danh mục: Bài hát, Bài chưa phát, Album, Nghệ sĩ Album, Nghệ sĩ, Thể loại và Nhạc sĩ.

## Nhóm theo Thẻ

Các danh mục này giúp tổ chức bản nhạc theo thẻ nhạc. Sau khi trình đọc siêu dữ liệu hoàn thành, bạn sẽ thấy các danh mục sau:

- **Bài hát** — tất cả bài hát được nhóm theo thẻ TRACK_TITLE.
- **Bài chưa phát** — tất cả bài hát chưa bao giờ được phát.
- **Album** — bài hát được nhóm theo thẻ ALBUM_NAME.
- **Nghệ sĩ Album** — bài hát được nhóm chỉ theo thẻ ALBUM_ARTIST_TAG.
- **Nghệ sĩ** — bài hát được nhóm chỉ theo thẻ ARTIST_TAG.
- **Thể loại** — bài hát được nhóm theo thẻ GENRE.
- **Nhạc sĩ** — bài hát được nhóm theo thẻ COMPOSER — rất có giá trị cho thư viện nhạc cổ điển.

## Yêu thích

Bạn có thể đánh dấu bài hát là yêu thích trên màn hình trình phát âm thanh hoặc sử dụng menu tùy chọn.

## Gần đây

Phần này hiển thị tất cả bài hát được phát gần đây. Bạn có thể tùy chỉnh số lượng mục trong danh sách trong Cài đặt → Thư viện → Gần đây → Thay đổi Kích thước Danh sách, và xuất danh sách sang M3U / CSV / TXT.

## Đánh dấu trang

Bạn có thể tạo đánh dấu âm thanh trong khi bài hát đang phát và quản lý chúng trên màn hình này — hoàn hảo cho sách nói, bài giảng dài, hoặc chỉ đánh dấu điệp khúc của bài hát yêu thích.

## Thanh Công cụ Trên cùng

Nằm ngay bên dưới thanh điều hướng, thanh công cụ trên cùng cung cấp một số hành động tiện lợi: Tìm kiếm, Phát tất cả, Phát ngẫu nhiên và Tiếp tục phát. Bạn có thể hiển thị hoặc ẩn thanh công cụ này bằng cử chỉ vuốt xuống.

## Tìm kiếm

Tính năng tìm kiếm cho phép tìm bản nhạc, nghệ sĩ, album hoặc thể loại cụ thể trong thư viện nhạc.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Tìm kiếm Thư viện Nhạc" image="/docs/guide/flacbox/img/media-library-search.webp" >}}
{{< /cards >}}

## Menu Tùy chọn

Mỗi bài hát trong thư viện nhạc có menu với nhiều hành động hơn, được truy cập bằng cách nhấn nút ba chấm bên cạnh tiêu đề bài hát.

### Đối với Bài hát Đơn lẻ

- **Phát tiếp** — thêm bài hát vào đầu hàng đợi phát.
- **Phát sau** — thêm bài hát vào cuối hàng đợi phát.
- **Thêm vào Danh sách phát** — thêm bài hát vào danh sách phát.
- **Thêm vào Yêu thích** — đánh dấu bài hát là yêu thích.
- **Tải xuống** — lưu bài hát vào file cục bộ.
- **Chỉnh sửa thẻ âm thanh** — mở trình chỉnh sửa thẻ tích hợp.
- **Hiện trong Thư mục** — hiển thị thư mục chứa file âm thanh.
- **Hiện trong Finder** — đối với file từ Mac, hiển thị thư mục trong Finder.
- **Mở bằng** — xuất file âm thanh sang ứng dụng khác.
- **Xóa khỏi Dịch vụ Đám mây** — xóa file khỏi cả thư viện nhạc và lưu trữ đám mây. **Không thể hoàn tác hành động này.**
- **Xóa khỏi Thư viện Nhạc** — xóa bài hát khỏi thư viện nhạc, nhưng file vẫn còn trong bộ lưu trữ.

### Đối với Bộ sưu tập Bài hát

Đối với các bộ sưu tập như Album, Nghệ sĩ, Thể loại hoặc Nhạc sĩ:

- **Phát tất cả** — thay thế hàng đợi phát bằng bài hát từ bộ sưu tập đã chọn.
- **Phát tiếp** — thêm bài hát từ bộ sưu tập vào đầu hàng đợi.
- **Phát sau** — thêm bài hát từ bộ sưu tập vào cuối hàng đợi.
- **Thêm vào Danh sách phát** — bao gồm bài hát từ bộ sưu tập vào danh sách phát.
- **Bật chế độ ngoại tuyến** — tải bài hát từ bộ sưu tập xuống file cục bộ.
- **Chỉnh sửa Hình ảnh** — thay đổi ảnh bìa album cho bộ sưu tập.
- **Thêm vào Kho lưu trữ** — đóng gói toàn bộ bộ sưu tập thành một file ZIP (tính năng Premium).
- **Xuất Danh sách Bài hát** — xuất bộ sưu tập sang M3U, CSV hoặc TXT.
- **Xóa khỏi Thư viện Nhạc** — xóa bộ sưu tập khỏi thư viện nhạc. File trong bộ lưu trữ không bị ảnh hưởng.

## Chế độ Chọn

Bạn có thể kích hoạt chế độ chọn bằng cách sử dụng nút Thêm Hành động ở góc trên bên phải.

## Chi tiết Album

Khi bạn mở phần Nghệ sĩ, Nghệ sĩ Album hoặc Nhạc sĩ, bạn có thể thấy nút chuyển đổi cho Bài hát / Tất cả Album / Album Độc quyền / Album Độc lập.

- **Bài hát** — hiển thị tất cả bài hát nơi Nghệ sĩ / Nghệ sĩ Album / Nhạc sĩ này xuất hiện trong thẻ âm thanh.
- **Tất cả Album** — hiển thị album tổng hợp và tất cả album nơi nghệ sĩ xuất hiện.
- **Album Độc quyền** — hiển thị album nơi nghệ sĩ được chỉ định là nghệ sĩ duy nhất với tên album đó.
- **Album Độc lập** — hiển thị album chỉ có bản nhạc của nghệ sĩ được chỉ định.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Màn hình Chi tiết Album" image="/docs/guide/flacbox/img/media-library-album-details-screen.webp" >}}
{{< /cards >}}

## Cài đặt

Nhấn Thêm Hành động → Cài đặt để cấu hình tùy chọn thư viện nhạc.

### Đọc Siêu dữ liệu

Khi bạn thêm bản nhạc vào thư viện, trình đọc siêu dữ liệu bắt đầu làm việc. Quá trình nền này đọc tất cả siêu dữ liệu từ bản nhạc và tổ chức chúng theo Nghệ sĩ, Album, Thể loại và Nhạc sĩ.

Trình đọc siêu dữ liệu **chỉ cập nhật siêu dữ liệu trong thư viện nhạc** và không thay đổi file trong tài khoản đám mây hoặc bộ lưu trữ cục bộ.

Khi **Đọc Siêu dữ liệu trong Nền** được bật, trình đọc tiếp tục làm việc ở chế độ nền.

Khi **Chuẩn hóa Mã hóa Siêu dữ liệu** được bật, ứng dụng tự động chuẩn hóa mã hóa siêu dữ liệu cho tất cả bài hát. Điều này sửa mã hóa thẻ bị hỏng và ngăn các ký tự không chính xác xuất hiện.

**Tải lại siêu dữ liệu** đánh dấu mọi file trong thư viện nhạc là có siêu dữ liệu bị thiếu, kích hoạt trình đọc làm mới mọi bản ghi.

Nhấn **Bắt đầu Đọc Siêu dữ liệu** để kích hoạt trình đọc thủ công.

### Đồng bộ Trực tuyến

Đồng bộ nhạc trực tuyến tự động cho phép thêm bản nhạc từ các dịch vụ đám mây đã kết nối vào thư viện nhạc tự động. Để kích hoạt, mở cài đặt thư viện nhạc và chọn thư mục đồng bộ.

Đồng bộ trực tuyến chỉ chạy khi ứng dụng ở tiền cảnh. Để tăng tốc, hãy giữ Flacbox mở, cắm sạc thiết bị và bật **Cài đặt → Màn hình → Luôn Hoạt động**.

### Đồng bộ Ngoại tuyến

Cấu hình đồng bộ nhạc ngoại tuyến tại đây.

#### Thư mục Ngoại tuyến Đồng bộ

Khi bạn đánh dấu thư mục trực tuyến là có thể dùng ngoại tuyến, nó xuất hiện ở đây. Nội dung thư mục được tải xuống File Cục bộ → Thư mục Ngoại tuyến.

#### Khoảng thời gian

Đặt khoảng thời gian kiểm tra thư mục ngoại tuyến có thay đổi không.

#### Bắt đầu Quét Thư mục Cục bộ

Tùy chọn này quét tất cả thư mục cục bộ trong thư mục Documents của ứng dụng để tìm file âm thanh được hỗ trợ.

#### Quan trọng

Nên định kỳ khởi tạo đồng bộ nhạc ngoại tuyến để giữ thư viện nhạc được cập nhật.

### Cá nhân hóa

Trong phần này, bạn có thể cấu hình kiểu màn hình thư viện nhạc. Ba tùy chọn có sẵn: Menu Đơn giản, Menu Nhóm, Menu Dạng Tab.

### Ảnh bìa Album

Tại đây, bạn có thể cấu hình cách ứng dụng tải và lưu trữ ảnh bìa album.

- **Loại Mạng** — chọn Wi-Fi hoặc Wi-Fi & Dữ liệu Di động để tải ảnh bìa.
- **Tải Ảnh bìa Album cho File Trực tuyến** — khi bật, ảnh bìa nhúng được tải cho các file trong lưu trữ đám mây.
- **Tìm kiếm trong Thư mục** — khi bật, nếu bản nhạc không có ảnh bìa nhúng, ứng dụng tìm kiếm ảnh JPEG hoặc PNG trong cùng thư mục.
- **Chất lượng Ảnh bìa** — chọn chất lượng ảnh bìa album được lưu trữ trên thiết bị.
- **Hiện trong Thư mục** — mở thư mục nơi ảnh bìa album được lưu vào bộ nhớ đệm.
- **Xóa tất cả** — xóa ảnh bìa album được lưu vào bộ nhớ đệm để giải phóng dung lượng.

### Danh sách phát

Bạn có thể bật tùy chọn để thêm cùng một bài hát vào danh sách phát hai lần. Theo mặc định, tùy chọn này bị tắt.

### Gần đây

Bạn có thể quản lý danh sách bài hát gần đây đã phát.

- **Xóa Danh sách** — xóa toàn bộ danh sách bài hát gần đây.
- **Thay đổi Kích thước Danh sách** — đặt số lượng mục xuất hiện trong danh sách.
- **Xuất Danh sách Bài hát** — xuất danh sách gần đây sang M3U, CSV hoặc TXT. Hướng dẫn chi tiết có sẵn [tại đây](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Yêu thích

Bạn có thể quản lý danh sách bài hát yêu thích.

- **Chỉnh sửa Đồng thời** — khi bật, thêm bài hát vào yêu thích sẽ thêm nó vào cả thư viện nhạc và phần file cùng một lúc.
- **Xóa Danh sách** — xóa toàn bộ danh sách bài hát yêu thích.
- **Xuất Danh sách Bài hát** — tương tự Gần đây, xuất danh sách yêu thích sang M3U, CSV hoặc TXT.

### Xóa Thư viện

Hành động này sẽ xóa cơ sở dữ liệu thư viện nhạc, nhưng sẽ để nguyên các file nhạc trong bộ lưu trữ.

### Giới hạn Tải Nội dung

Theo mặc định, ứng dụng sử dụng phân trang để giảm thời gian tải nội dung và giữ thư viện lớn phản hồi nhanh. Tuy nhiên, bạn có thể tắt tùy chọn này và cho phép ứng dụng tải tất cả dữ liệu có sẵn cùng một lúc. Để làm điều này, mở cài đặt ứng dụng, cuộn xuống đến Cá nhân hóa → Giới hạn Tải Nội dung, và chọn Đã tắt.
