---
title: "Cách nhập danh sách phát M3U vào Evermusic và Flacbox"
date: 2024-01-31
description: "Tìm hiểu cách nhập tệp danh sách phát M3U, M3U8 và CUE từ đám mây, bộ nhớ cục bộ hoặc thiết bị vào Evermusic và Flacbox."
keywords: ["evermusic", "flacbox", "danh sách phát", "m3u", "m3u8", "cue", "nhập", "ứng dụng nhạc"]
tags: ["evermusic", "nhập", "danh sách phát", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Tóm tắt:** Evermusic và Flacbox hỗ trợ nhập tệp danh sách phát M3U, M3U8 và CUE từ bộ nhớ đám mây, tệp ứng dụng cục bộ hoặc thiết bị của bạn. Đi tới Danh sách phát > Thêm > Nhập danh sách phát, chọn nguồn, chọn tệp của bạn và ứng dụng sẽ tự động tạo danh sách phát.

M3U, viết tắt của MP3 URL hoặc Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, là định dạng tệp máy tính được sử dụng cho danh sách phát đa phương tiện. Một trong những công dụng chính của nó là tạo tệp danh sách phát một mục nhập trỏ đến các luồng trên internet. Các tệp này cung cấp quyền truy cập thuận tiện vào nội dung phát trực tuyến và thường được sử dụng để tải xuống, gửi email và nghe đài phát thanh Internet.

Mặc dù được sử dụng rộng rãi, không có đặc tả chính thức nào cho định dạng M3U; nó đã trở thành tiêu chuẩn thực tế. Tệp M3U về cơ bản là tệp văn bản thuần túy chỉ định vị trí của một hoặc nhiều tệp phương tiện. Tùy thuộc vào mã hóa, nó được lưu với phần mở rộng "m3u" hoặc "m3u8". Mỗi mục trong tệp chỉ định vị trí của tệp phương tiện, có thể là đường dẫn cục bộ tuyệt đối, đường dẫn cục bộ tương đối so với vị trí tệp M3U hoặc URL. Các mục được phân tách bằng ngắt dòng, với một số thiết bị yêu cầu ngắt dòng được biểu diễn là CR LF.

Ngoài ra, tệp M3U có thể bao gồm các bình luận có tiền tố ký tự "#". Trong M3U mở rộng, "#" giới thiệu các chỉ thị M3U mở rộng, có thể hỗ trợ các tham số kết thúc bằng dấu hai chấm ":".

Trong ứng dụng Evermusic và Flacbox, chúng tôi đã triển khai chức năng nhập tệp M3U, loại bỏ nhu cầu tạo danh sách phát thủ công. Hướng dẫn này sẽ đưa bạn qua quy trình nhập danh sách phát từ bộ nhớ đám mây, tệp cục bộ hoặc tệp trên thiết bị của bạn trực tiếp vào ứng dụng.

Đầu tiên, điều hướng đến phần 'Danh sách phát'. Tiếp theo, nhấn nút 'Thêm' ở góc trên bên phải. Từ menu xuất hiện, chọn tùy chọn 'Nhập danh sách phát'.

![thao tác nhập danh sách phát](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Trên màn hình tiếp theo, chọn vị trí tệp. Các tùy chọn được hỗ trợ bao gồm:

- Bộ nhớ đám mây đã kết nối;
- Tệp trong ứng dụng;
- Tệp trên thiết bị của bạn;

![chọn vị trí tệp](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Hãy chọn bộ nhớ đám mây đã kết nối và mở thư mục chứa tệp danh sách phát. Các phần mở rộng tệp danh sách phát được hỗ trợ bao gồm M3U, M3U8 và CUE. Chọn tệp danh sách phát và nhấn 'Hoàn tất' để xác nhận lựa chọn của bạn.

![chọn tệp M3U](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

Ứng dụng sẽ phân tích tệp danh sách phát và tạo danh sách bài hát. Sau đó, nó sẽ tìm các tệp đó trên bộ nhớ và biên soạn danh sách phát cuối cùng sẽ được nhập vào thư viện nhạc. Điều quan trọng là tệp M3U/CUE của bạn phải chứa đường dẫn chính xác cho các tệp phương tiện và các tệp phải nằm ở những đường dẫn đó trên bộ nhớ của bạn.

![danh sách phát đã nhập](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

Ứng dụng hỗ trợ cả đường dẫn tương đối và URL tệp tuyệt đối.

Ví dụ:

Danh sách phát với đường dẫn tương đối:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Danh sách phát với URL tuyệt đối:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Nếu bạn nhập tệp danh sách phát nằm trong ứng dụng (phần Tệp cục bộ), không cần thêm bước nào.

Tuy nhiên, nếu bạn muốn nhập danh sách phát nằm trên thiết bị bằng trình chọn tệp hệ thống, có một lưu ý quan trọng cần nhớ.

Do chính sách bảo mật, ứng dụng chỉ có thể truy cập tệp bạn chọn bằng trình chọn tệp hệ thống. Tuy nhiên, tệp danh sách phát có thể bao gồm liên kết đến các tệp phương tiện khác trên thiết bị của bạn. Để nhập danh sách phát từ thiết bị, bạn phải chọn một thư mục chứa cả tệp danh sách phát và tất cả tệp phương tiện được liên kết. Trong trường hợp này, ứng dụng sẽ quét thư mục đã chọn, tìm tệp danh sách phát, xây dựng danh sách bài hát và nhập vào thư viện nhạc.

Ngoài ra, bạn có thể nhập nhiều danh sách phát cùng lúc bằng cách nhấn nút "Thêm hành động" và chọn "Nhập danh sách phát từ thư mục". Ứng dụng sẽ quét nội dung thư mục, tìm các tệp danh sách phát được hỗ trợ và nhập chúng vào thư viện.

## Câu hỏi thường gặp

{{% details title="Evermusic và Flacbox hỗ trợ những định dạng danh sách phát nào?" closed="true" %}}
Cả hai ứng dụng đều hỗ trợ các định dạng tệp danh sách phát M3U, M3U8 và CUE. Đây là những tiêu chuẩn danh sách phát phổ biến nhất được sử dụng bởi trình phát nhạc và phần mềm đa phương tiện.
{{% /details %}}

{{% details title="Tôi có thể nhập danh sách phát từ bộ nhớ đám mây không?" closed="true" %}}
Có. Bạn có thể nhập tệp danh sách phát từ bất kỳ dịch vụ bộ nhớ đám mây nào đã kết nối bao gồm Google Drive, Dropbox, OneDrive và máy chủ WebDAV.
{{% /details %}}

{{% details title="Tại sao một số bài hát bị thiếu sau khi nhập?" closed="true" %}}
Tệp danh sách phát phải chứa đường dẫn chính xác đến các tệp phương tiện của bạn và các tệp đó phải tồn tại tại các vị trí được chỉ định trên bộ nhớ của bạn. Kiểm tra lại rằng đường dẫn tệp trong tệp M3U hoặc CUE của bạn khớp với vị trí tệp thực tế.
{{% /details %}}

{{% details title="Tôi có thể nhập nhiều danh sách phát cùng lúc không?" closed="true" %}}
Có. Sử dụng nút Thêm hành động và chọn "Nhập danh sách phát từ thư mục". Ứng dụng quét thư mục tìm tất cả tệp danh sách phát được hỗ trợ và nhập chúng trong một bước.
{{% /details %}}

{{% details title="Tôi có cần tạo danh sách phát thủ công không?" closed="true" %}}
Không. Tính năng nhập loại bỏ việc tạo danh sách phát thủ công. Chỉ cần trỏ ứng dụng đến tệp M3U, M3U8 hoặc CUE hiện có của bạn và nó sẽ tự động tạo danh sách phát.
{{% /details %}}
