---
title: "Cách xuất bộ sưu tập bài hát sang M3U, CSV và TXT trong Evermusic & Flacbox"
date: 2024-01-31
description: "Tìm hiểu cách xuất gần đây, yêu thích, danh sách phát và album từ Evermusic và Flacbox sang định dạng M3U, CSV hoặc TXT. Hoàn hảo cho việc scrobble Last.fm và phát trên các thiết bị khác."
keywords: ["xuất evermusic", "xuất flacbox", "xuất sang m3u", "xuất danh sách phát sang csv", "m3u txt csv danh sách phát", "xuất nhạc"]
tags: ["evermusic", "recents", "favorites", "export", "m3u", "playlist", "csv", "txt", "album"]
---

{{< author-byline >}}


**Tóm tắt:** Evermusic và Flacbox cho phép bạn xuất bất kỳ bộ sưu tập bài hát nào (gần đây, yêu thích, danh sách phát, album) sang tệp CSV, TXT hoặc M3U. Sử dụng các bản xuất này để scrobble lên Last.fm, sao lưu thư viện hoặc phát danh sách phát trên các thiết bị khác.

## Giới thiệu

Việc xuất gần đây, yêu thích, album và danh sách phát từ ứng dụng sang tệp bên ngoài có thể vô cùng hữu ích. Bạn có thể sử dụng các tệp này để cập nhật lịch sử nghe trên các dịch vụ scrobbler như [Last.fm](http://Last.fm) hoặc nghe danh sách phát trên các thiết bị bên ngoài. Với Evermusic và Flacbox, quy trình này rất dễ dàng. Ở đây, chúng tôi sẽ hướng dẫn bạn cách xuất gần đây sang CSV/TXT và danh sách phát sang M3U. Tuy nhiên, chức năng này có sẵn cho bất kỳ bộ sưu tập bài hát nào trong ứng dụng.

## Chọn định dạng

Để xuất gần đây, hãy mở phần 'Thư viện nhạc' và chọn mục menu 'Gần đây'.

![thư viện nhạc](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Trên màn hình tiếp theo, nhấn nút 'Thêm' ở góc trên bên phải và chọn 'Xuất danh sách bài hát'.

![xuất gần đây](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

Trên màn hình 'Chọn định dạng tệp', bạn có một số tùy chọn - CSV, TXT, M3U.

- CSV

Đây là viết tắt của Comma-Separated Values (Giá trị phân cách bằng dấu phẩy), hoàn hảo để sắp xếp dữ liệu của bạn thành định dạng bảng gọn gàng. Trong tệp đích, bạn sẽ tìm thấy các thông số như Tên nghệ sĩ, Tên album, Tên bài hát, Dấu thời gian (thời điểm bạn nghe các bài hát), Tên nghệ sĩ album và Thời lượng bài hát. Bạn có thể sử dụng tệp đó sau này để cập nhật lịch sử nghe trên các dịch vụ scrobbler như [Last.fm](http://Last.fm) như được mô tả [tại đây](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Ở đây, chúng ta đang nói về tệp văn bản thuần túy. Nó đơn giản và dễ hiểu, với các thông số bao gồm Tên nghệ sĩ, Tên album, Tên bài hát và Thời lượng. Hữu ích nếu bạn chỉ cần danh sách bài hát dưới dạng văn bản.

- M3U

Định dạng này về cơ bản là tiêu chuẩn thực tế để tạo danh sách phát. Nó tuyệt vời vì bạn có thể xuất danh sách bài hát và thưởng thức các bài hát trên bất kỳ thiết bị nào, ngay cả khi bạn không có tệp gốc (nếu bạn chọn tùy chọn URL tuyệt đối cho tệp phương tiện khi xuất). Trong tệp đầu ra, bạn sẽ tìm thấy các thông số như Thời lượng, Tên nghệ sĩ, Tên bài hát và Vị trí tệp phương tiện.

## Định dạng CSV

Bây giờ, hãy chọn CSV và xem chúng ta sẽ nhận được gì. Chỉ cần chọn CSV và nhấn nút 'Xuất'.

![chọn định dạng tệp](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Sau khi xuất hoàn tất, bạn sẽ thấy một thông báo với hai tùy chọn. Nhấn 'Hiển thị tệp' sẽ hiển thị tệp kết quả trong thư mục tài liệu của bạn.

![xuất hoàn tất](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Bây giờ bạn có thể gửi tệp đó, mở nó trong trình soạn thảo văn bản bên ngoài hoặc sử dụng để cập nhật tiến trình nghe trên [Last.fm](http://Last.fm).

![thư mục xuất với các tệp kết quả](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

Tệp CSV đầu ra sẽ chứa các trường theo định dạng sau:

```
{TÊN_NGHỆ_SĨ},{TÊN_ALBUM},{TÊN_BÀI_HÁT},{DẤU_THỜI_GIAN yyyy-MM-dd HH:mm:ss},{TÊN_NGHỆ_SĨ_ALBUM},{THỜI_LƯỢNG_BÀI_HÁT HH:mm:ss}
```

Ví dụ:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![tệp csv đã xuất](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## Định dạng TXT

Tệp TXT đầu ra sẽ chứa các trường theo định dạng sau:

```
{SỐ_THỨ_TỰ}. {TÊN_NGHỆ_SĨ} - {TÊN_ALBUM} - {TÊN_BÀI_HÁT} (THỜI_LƯỢNG HH:mm:ss)
```

Ví dụ:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![tệp txt đã xuất](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## Định dạng M3U

Tiếp theo, chúng tôi sẽ hướng dẫn bạn xuất danh sách phát sang định dạng M3U, đây là tiêu chuẩn thực tế cho các tệp danh sách phát. Điều kiện tiên quyết chính để xuất danh sách phát thành công là tất cả các tệp trong danh sách phát phải nằm trên cùng một bộ nhớ, dù đó là dịch vụ đám mây như Google Drive, tệp cục bộ hay tệp trên thiết bị của bạn. Để bắt đầu quá trình xuất, mở bất kỳ danh sách phát nào và nhấn nút 'Thêm' ở góc trên bên phải, sau đó chọn mục menu 'Xuất danh sách bài hát'.

![màn hình danh sách phát](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Trên màn hình tiếp theo, chọn định dạng tệp 'M3U', nơi bạn sẽ gặp hai tùy chọn cho 'Loại vị trí tệp phương tiện':

![màn hình chọn định dạng tệp xuất](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Nếu bạn chọn 'Đường dẫn tương đối', danh sách phát sẽ được tạo với vị trí tệp phương tiện được ghi tương đối so với tệp danh sách phát. Ví dụ:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   Trong trường hợp này, tránh thay đổi vị trí tệp M3U sau khi xuất hoàn tất, vì làm vậy sẽ phá vỡ đường dẫn đến các tệp phương tiện. Để bắt đầu phát danh sách phát, chỉ cần nhấn vào tệp danh sách phát đã xuất, và ứng dụng sẽ tự động tìm các tệp phương tiện trên bộ nhớ của bạn và bắt đầu phát. Bạn thậm chí có thể xuất danh sách phát ra bộ nhớ rồi nhập lại trên thiết bị mới.

2. Nếu bạn chọn 'URL tuyệt đối', ứng dụng sẽ tạo các URL trực tiếp cho tệp phương tiện của bạn. Điều này cho phép bạn phát danh sách phát trên bất kỳ thiết bị/ứng dụng nào mà không cần tất cả tệp phương tiện nằm trên cùng bộ nhớ với tệp danh sách phát. Tùy chọn này chỉ được hỗ trợ cho các dịch vụ lưu trữ đám mây có khả năng tạo URL trực tiếp cho tệp. Tuy nhiên, hãy lưu ý rằng trong một số trường hợp, các URL được tạo có thể có thời hạn giới hạn và có thể hết hạn sau một thời gian. Đây là danh sách các dịch vụ đám mây được hỗ trợ: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (nếu ở chế độ khách)  

URL tệp phương tiện đầu ra sẽ có dạng như sau:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Sau khi chọn 'Loại vị trí tệp phương tiện', nhấn 'Xuất'. Ứng dụng sẽ yêu cầu bạn chọn thư mục đích để xuất tệp M3U. Nhấn 'Hoàn tất' để xác nhận lựa chọn.

![chọn thư mục](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Ứng dụng sẽ tạo tệp M3U và tải lên/di chuyển nó đến thư mục đích.

![đang tải tệp m3u](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Sau khi xuất hoàn tất, một thông báo hệ thống sẽ xuất hiện với tùy chọn 'Hiển thị tệp'.

![thông báo xuất hoàn tất](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Nhấn vào đây sẽ hiển thị tệp đã xuất trong ứng dụng.

![tệp m3u đã xuất trong danh sách tệp](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Nếu bạn chọn 'Đường dẫn tương đối' làm 'Loại vị trí tệp phương tiện' ở bước trước, tệp đầu ra sẽ có định dạng sau:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![ví dụ m3u với đường dẫn tương đối](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Với tùy chọn 'URL tuyệt đối', ứng dụng sẽ tạo tệp M3U theo định dạng:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![ví dụ m3u với URL tuyệt đối của tệp](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Bạn có thể mở tệp đó trên bất kỳ thiết bị/ứng dụng nào hỗ trợ danh sách phát M3U.

![danh sách phát m3u được mở trong ứng dụng bên ngoài](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Lời kết

Xuất bài hát từ Evermusic và Flacbox mang lại cho bạn quyền kiểm soát hoàn toàn đối với dữ liệu âm nhạc. Dù bạn đang sao lưu lịch sử nghe, scrobble lên Last.fm hay thưởng thức danh sách phát trên các thiết bị bên ngoài, các tùy chọn xuất M3U, CSV và TXT là những công cụ mạnh mẽ được thiết kế cho sự linh hoạt và tương thích. Hãy tận dụng các tính năng này để nâng cao cách bạn tổ chức, chia sẻ và xem lại bộ sưu tập âm nhạc trên nhiều nền tảng.

## Câu hỏi thường gặp

{{% details title="Tôi nên sử dụng định dạng xuất nào cho scrobbling Last.fm?" closed="true" %}}
Sử dụng CSV. Nó bao gồm dấu thời gian và siêu dữ liệu đầy đủ theo yêu cầu của các công cụ scrobbling như Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Tôi có thể xuất bất kỳ bộ sưu tập bài hát nào, không chỉ danh sách phát không?" closed="true" %}}
Có. Bạn có thể xuất gần đây, yêu thích, album, danh sách phát và bất kỳ bộ sưu tập bài hát nào khác trong ứng dụng bằng các bước tương tự.
{{% /details %}}

{{% details title="Danh sách phát M3U của tôi có hoạt động trên các thiết bị khác không?" closed="true" %}}
Nếu bạn chọn tùy chọn URL tuyệt đối khi xuất, tệp M3U có thể được phát trên bất kỳ thiết bị nào hỗ trợ danh sách phát M3U. Lưu ý rằng một số URL đám mây có thể hết hạn theo thời gian.
{{% /details %}}

{{% details title="Tính năng xuất có miễn phí không?" closed="true" %}}
Có. Xuất bộ sưu tập bài hát sang M3U, CSV và TXT có sẵn trong cả phiên bản miễn phí và cao cấp của Evermusic và Flacbox.
{{% /details %}}

{{% details title="Những dịch vụ đám mây nào hỗ trợ xuất URL tuyệt đối?" closed="true" %}}
Xuất URL tuyệt đối được hỗ trợ cho iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive và WebDAV (chế độ khách).
{{% /details %}}
