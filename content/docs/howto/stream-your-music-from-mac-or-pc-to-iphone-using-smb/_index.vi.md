---
title: "Phát nhạc trực tuyến từ Mac hoặc PC sang iPhone bằng SMB"
description: "Tìm hiểu cách phát trực tuyến bộ sưu tập nhạc từ Mac hoặc Windows PC sang iPhone hoặc iPad bằng Evermusic và giao thức SMB. Hướng dẫn từng bước đơn giản để kết nối và thưởng thức âm thanh mà không cần đồng bộ."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["phát nhạc từ Mac sang iPhone", "SMB phát âm thanh iOS", "thiết lập Evermusic SMB", "kết nối nhạc PC iPhone", "chia sẻ nhạc Mac iOS", "SMB Windows phát tệp", "truy cập thư mục PC Evermusic"]
aliases:
  - /post/stream-your-music-from-mac-or-pc-to-iphone-using-smb/
  - /single-post/Stream-your-music-from-MAC-or-PC-to-iPhone-using-SMB/
---

{{< author-byline >}}


**Tóm tắt:** Sử dụng ứng dụng Evermusic cho iPhone hoặc iPad để phát nhạc trực tuyến từ Mac hoặc Windows PC qua mạng cục bộ bằng SMB. Không cần đồng bộ, không cần sao chép -- chỉ cần bật chia sẻ tệp trên máy tính, kết nối trong ứng dụng và phát. Thiết lập mất chưa đến 5 phút.

Bạn đang chìm trong biển nhạc trên MAC hoặc PC và muốn thưởng thức nó dễ dàng trên iPhone hoặc iPad? Không cần tìm đâu xa ngoài Evermusic. Với Evermusic, việc kết nối máy tính bằng giao thức SMB và phát trực tuyến các bản nhạc yêu thích cực kỳ đơn giản, không cần lo lắng về dung lượng thiết bị hay các rắc rối đồng bộ. Đây là hướng dẫn từng bước để bắt đầu:

## Bước 1: Bật giao thức SMB trên máy tính

![Evermusic - Hỗ trợ SMB - Màn hình chia sẻ Mac](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Nếu bạn sử dụng MAC

- Mở System Preferences -> Sharing.
- Bật dịch vụ File Sharing.
- Trong phần "Shared Folders", thêm thư mục nhạc của bạn, chọn người dùng và đặt mức quyền (Read & Write hoặc Read Only).
- Để thuận tiện hơn, bạn có thể chọn "Everyone: Read Only" cho thư mục nhạc, giúp dễ dàng truy cập trong Evermusic.
- Đừng quên ghi nhớ URL máy tính (smb://192.168.xx.xx) cho các bước tiếp theo.

![Evermusic - Hỗ trợ SMB - Màn hình chia sẻ tệp](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Nhấn "Options" và bật "Share files and folders using SMB."
- Bật "Windows File Sharing" cho các tài khoản khả dụng.

![Evermusic - Hỗ trợ SMB - Màn hình chia sẻ tệp và thư mục](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Nếu bạn sử dụng Windows PC

![Evermusic - Hỗ trợ SMB - Chia sẻ tệp trên Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Nhấp chuột phải vào thư mục nhạc.
- Chọn "Properties."
- Mở tab "Sharing."
- Nhấp "Share..."
- Chọn người để chia sẻ và đặt mức quyền của họ.
- Giống như MAC, bạn có thể chọn "Everyone: Read" cho thư mục nhạc đã chọn.
- Nhấp "Hoàn tất" để lưu cài đặt.

![Evermusic - Hỗ trợ SMB - Thư mục được chia sẻ trên Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Bước 2: Thêm máy tính tự động

- Bây giờ, mở Evermusic và đi đến tab "Kết nối" ("Mạng" nếu bạn sử dụng phiên bản ứng dụng cũ).
- Nếu bạn thấy máy tính trong phần "Thiết bị có sẵn" ("Chia sẻ có sẵn" nếu bạn sử dụng phiên bản ứng dụng cũ) và đã chọn "Everyone: Read Only" ở bước trước, chỉ cần nhấn vào máy tính và nó sẽ kết nối tự động.
- Nếu điều này không xảy ra, bạn có thể thêm máy tính thủ công.

![Evermusic - Hỗ trợ SMB - Màn hình kết nối tài khoản](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Bước 3: Thêm máy tính thủ công

- Nhấn "Kết nối dịch vụ đám mây" ("Thêm tài khoản" nếu bạn sử dụng phiên bản ứng dụng cũ)
- Chọn "SMB" từ danh sách máy chủ khả dụng trên màn hình tiếp theo.
- Trên màn hình cài đặt "SMB":
  - Nhập URL máy chủ với đường dẫn thư mục chia sẻ. Bạn có thể nhập tên máy chủ hoặc IP máy chủ. Ví dụ:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Nhập tên đăng nhập và mật khẩu hoặc để trống nếu bạn đã chọn "Everyone: Read Only" ở bước trước.
  - Trường "WORKGROUP" là tùy chọn và nên sử dụng nếu bạn có miền Active Directory.

![Evermusic - Hỗ trợ SMB - Màn hình nhập thông tin đăng nhập](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Sau khi kết nối tài khoản SMB, nó sẽ xuất hiện trong phần "Dịch vụ đám mây" ("Tài khoản"). Mở tài khoản đã kết nối bằng cách nhấn vào, điều hướng đến thư mục nhạc và nhấn vào bất kỳ tệp âm thanh nào để khởi động trình phát.

![Evermusic - Hỗ trợ SMB - Màn hình mở thư mục đã kết nối](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Thưởng thức bộ sưu tập nhạc mượt mà trên iPhone hoặc iPad với Evermusic.

![Evermusic - Hỗ trợ SMB - Màn hình trình phát âm thanh](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Bước 4: Giải pháp tạm thời SMB2

Nếu bạn gặp sự cố khi duyệt thư mục hoặc phát tệp chứa ký tự đặc biệt (như ü, ö, é), điều này có thể liên quan đến giao thức SMB2. Chúng tôi đang tích cực làm việc để giải quyết vấn đề này.

Như một giải pháp tạm thời, hãy thử bật SMB 1 trên máy chủ và trong cài đặt ứng dụng. Ngoài ra, bạn có thể kết nối với máy chủ SMB bằng menu mở tệp hệ thống. Đây là cách:

1. Điều hướng đến "Tệp cục bộ."
2. Cuộn xuống phần "Tệp trên thiết bị này" và nhấn "Mở tệp..." hoặc "Mở thư mục..."
3. Tìm máy chủ và chọn tệp hoặc thư mục bạn cần.
4. Nhấn "Mở" để xác nhận lựa chọn.

## Bước 5: Giải pháp tạm thời WebDAV

Ngoài ra, bạn có thể thử kết nối với NAS bằng giao thức WebDAV hoặc DLNA nếu được hỗ trợ.

Bằng cách làm theo các bước này, bạn có thể vượt qua các vấn đề liên quan đến ký tự đặc biệt trong tên tệp và tiếp tục thưởng thức các tệp phương tiện.

P.S. Bạn cũng có thể chuyển tệp âm thanh từ MAC/PC sang iPhone bằng iTunes File Sharing và phát tệp âm thanh cục bộ. Tìm hiểu thêm về tính năng này trong hướng dẫn của chúng tôi: [Cách phát tệp iTunes trên iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Câu hỏi thường gặp

{{% details title="Tôi có thể phát nhạc từ PC sang iPhone mà không cần iTunes không?" closed="true" %}}
Có. Evermusic kết nối với PC qua SMB trên mạng Wi-Fi cục bộ. Không cần iTunes. Chỉ cần bật chia sẻ tệp trên PC và kết nối trong ứng dụng.
{{% /details %}}

{{% details title="Phát trực tuyến SMB có sử dụng dữ liệu di động không?" closed="true" %}}
Không. SMB hoạt động qua mạng Wi-Fi cục bộ. Không cần kết nối internet hoặc dữ liệu di động.
{{% /details %}}

{{% details title="Evermusic hỗ trợ định dạng âm thanh nào qua SMB?" closed="true" %}}
Evermusic hỗ trợ MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC và các định dạng âm thanh phổ biến khác. Tệp được phát trực tiếp từ chia sẻ SMB.
{{% /details %}}

{{% details title="Tôi có thể phát nhạc từ NAS sang iPhone không?" closed="true" %}}
Có. Nếu NAS hỗ trợ SMB (hầu hết đều hỗ trợ, bao gồm Synology, QNAP và WD My Cloud), bạn có thể kết nối bằng các bước tương tự trong hướng dẫn này.
{{% /details %}}

{{% details title="Tôi có cần để máy tính bật khi phát trực tuyến không?" closed="true" %}}
Có. Vì Evermusic phát tệp trực tiếp từ máy tính, nên máy tính phải được bật và kết nối cùng mạng với iPhone.
{{% /details %}}

{{% details title="Có giới hạn kích thước tệp cho phát trực tuyến SMB không?" closed="true" %}}
Không. Evermusic phát tệp bất kỳ kích thước nào qua SMB. Các tệp lossless lớn (FLAC, WAV) hoạt động bình thường.
{{% /details %}}
