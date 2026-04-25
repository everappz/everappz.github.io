---
title: "Cách chuyển thư viện nhạc giữa các thiết bị trong Evermusic: hướng dẫn từng bước"
description: "Dễ dàng chuyển thư viện nhạc Evermusic, danh sách phát, ảnh bìa album và cài đặt từ iPhone, iPad hoặc Mac này sang thiết bị khác bằng Wi-Fi Drive và công cụ sao lưu."
date: 2024-12-29
tags: ["thuviennhac", "chuyendoi", "wifi", "saoluu", "webdav", "khoiphuc"]
keywords: ["chuyển thư viện nhạc Evermusic", "sao lưu và khôi phục danh sách phát Evermusic", "Evermusic WiFi Drive", "đồng bộ Evermusic giữa các thiết bị", "di chuyển cơ sở dữ liệu Evermusic", "chuyển tệp Evermusic", "khôi phục cài đặt trình phát âm thanh", "chuyển nhạc WebDAV iOS"]
readingTime: 3
---

{{< author-byline >}}


**Tóm tắt:** Để chuyển thư viện Evermusic sang thiết bị mới, hãy tạo bản sao lưu trên thiết bị nguồn, khởi động Wi-Fi Drive, kết nối thiết bị thứ hai qua cùng mạng, tải xuống bản sao lưu và các tệp nhạc, sau đó khôi phục từ bản sao lưu. Toàn bộ quá trình mất khoảng 10 phút tùy thuộc vào kích thước thư viện.

Trong hướng dẫn này, chúng tôi sẽ hướng dẫn bạn chuyển toàn bộ thư viện nhạc — bao gồm cơ sở dữ liệu, ảnh bìa album và cài đặt — từ thiết bị này (iPhone hoặc Mac) sang thiết bị khác. Mặc dù đồng bộ tự động thư viện nhạc và danh sách phát là tính năng được lên kế hoạch cho tương lai, quy trình này hiện tại phải được thực hiện thủ công.

## Bước 1: Tạo bản sao lưu trên thiết bị đầu tiên

1. **Mở ứng dụng trên thiết bị đầu tiên** (thiết bị có thư viện nhạc, danh sách phát và dịch vụ đám mây đã kết nối).
2. **Điều hướng đến Cài đặt** và chọn tùy chọn **Sao lưu và Khôi phục**.

![Backup and Restore](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. Trên màn hình **Sao lưu và Khôi phục**, chọn các mục để đưa vào tệp sao lưu:
   - **Cơ sở dữ liệu** (bao gồm thư viện nhạc và danh sách phát)
   - **Ảnh bìa album**
   - **Cài đặt**

Các tùy chọn này được bật theo mặc định.

![Backup Options](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Nhấn **Sao lưu dữ liệu ứng dụng** để bắt đầu quá trình.

![Backup Application Data](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Khi sao lưu hoàn tất, một thông báo thông tin sẽ xuất hiện.

![Backup Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Nhấn **Hiển thị tệp** để hiện tệp sao lưu trong thư mục **Tài liệu**. Các tệp sao lưu thường được lưu trong thư mục **Backup**.

![Show Backup File](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Bước 2: Khởi động máy chủ Wi-Fi Drive

1. Đi đến phần **Kết nối** trong ứng dụng.
2. Cuộn xuống **Kết nối qua Wi-Fi** và nhấn vào.

![Connect Using Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. Trên màn hình tiếp theo, nhấn **Khởi động Wi-Fi Drive**.

- Tùy chọn, bạn có thể đặt tên đăng nhập và mật khẩu để bảo mật, nhưng điều này không cần thiết cho mạng gia đình.

4. Khi đã khởi động, bạn sẽ thấy các địa chỉ máy chủ có sẵn. Điều này có thể được sử dụng cho trình duyệt máy tính hoặc ứng dụng WebDAV, nhưng trong hướng dẫn này, chúng ta sẽ tiến thẳng đến các bước tiếp theo.

![Wi-Fi Drive Started](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Bước 3: Kết nối thiết bị thứ hai với thiết bị đầu tiên

1. Mở ứng dụng trên thiết bị thứ hai (nơi bạn muốn chuyển thư viện).
2. Đảm bảo cả hai thiết bị đều kết nối cùng một mạng Wi-Fi.
3. Trên thiết bị thứ hai, mở tab **Kết nối** và chọn **Thiết bị có sẵn**.

![Available Devices](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Bạn sẽ thấy kết nối WebDAV có tên **Evermusic** (máy chủ chúng ta đã khởi động trên thiết bị đầu tiên). Nhấn vào để kết nối.

5. Khi đã kết nối, bạn sẽ thấy tất cả các thư mục từ thiết bị đầu tiên.

![Connected to First Device](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Bước 4: Chuẩn bị chuyển tệp

1. Trên thiết bị thứ hai, đi đến **Cài đặt > Trình quản lý tệp** và bật **Lưu tệp đã tải xuống vào - Hỏi mỗi lần**.

- Điều này đảm bảo bạn có thể chọn thư mục đích cho mỗi lần tải xuống.

2. Quay lại tab **Kết nối** và điều hướng đến máy chủ WebDAV đã kết nối.

![Prepare for File Transfers](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Bước 5: Chuyển bản sao lưu và tệp nhạc

1. Mở thư mục **Backup** trên máy chủ WebDAV đã kết nối.

![Backup Folder](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Nhấn nút **Thêm hành động** (ba chấm) bên cạnh tệp sao lưu và chọn **Tải xuống**.

3. Tạo thư mục **Backup** trên thiết bị thứ hai để lưu trữ các tệp đã tải xuống. Xác nhận lựa chọn bằng cách nhấn **Hoàn tất**.

![Download Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Chuyển các tệp nhạc bổ sung:
   - Kiểm tra thư mục **Tải xuống** hoặc các thư mục liên quan khác trên máy chủ WebDAV.

![Transfer Music Files](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Sử dụng tùy chọn **Chọn** để chọn tệp, sau đó nhấn **Thêm hành động > Tải xuống**. Lưu chúng vào thư mục tương ứng trên thiết bị thứ hai để duy trì cùng cấu trúc thư mục.

Mục tiêu là chuyển tất cả tệp từ thiết bị đầu tiên sang thiết bị hiện tại, đảm bảo cấu trúc thư mục giống hệt nhau. Bằng cách này, các liên kết trong thư viện nhạc và danh sách phát sẽ được giữ nguyên. Lưu ý rằng các tệp cục bộ được lưu trữ bên ngoài thư mục Tài liệu của ứng dụng trên thiết bị đầu tiên phải được chuyển riêng. Vì ứng dụng không thể truy cập các tệp này ở chế độ Wi-Fi Drive, bạn cần sử dụng ứng dụng Tệp Hệ thống để chuyển.

![Transfer Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Bước 6: Theo dõi tiến trình chuyển

1. Trên thiết bị thứ hai, đi đến phần **Tệp cục bộ** (hoặc tab **Tải xuống** trên iPad/Mac).

2. Nhấn nút **Hoạt động chuyển** ở góc trên bên trái để theo dõi hàng đợi chuyển.

![Monitor Transfer](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Bước 7: Khôi phục dữ liệu từ bản sao lưu

1. Khi tệp sao lưu và tất cả tệp âm thanh cần thiết đã được tải xuống thiết bị thứ hai, hãy mở thư mục **Backup**.

2. Nhấn vào tệp sao lưu, một thông báo xác nhận sẽ xuất hiện.

![Restore Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Lưu ý:** Khôi phục sẽ thay thế tất cả dữ liệu thư viện nhạc hiện tại, danh sách phát, cài đặt và ảnh bìa album bằng dữ liệu sao lưu.

3. Nhấn **Khôi phục** để bắt đầu quá trình.

![Restore Process](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Sau khi khôi phục hoàn tất, một thông báo sẽ xác nhận thành công.

![Restoration Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Kiểm tra các phần **Danh sách phát** hoặc **Thư viện nhạc** để xác minh việc khôi phục.

![Verify Restoration](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Bước 8: Lập chỉ mục lại thư viện nhạc

1. Để có kết quả tốt nhất, hãy lập chỉ mục lại thư viện để đảm bảo tất cả tệp được phát hiện thành công.

2. Đi đến **Cài đặt > Thư viện nhạc > Đồng bộ nhạc ngoại tuyến** và chọn **Bắt đầu quét thư mục cục bộ**.

Bằng cách làm theo các bước này, bạn sẽ chuyển thành công thư viện nhạc, danh sách phát và cài đặt sang thiết bị khác. Nếu gặp bất kỳ vấn đề nào, đừng ngần ngại liên hệ hỗ trợ.

## Câu hỏi thường gặp

{{% details title="Tôi có thể chuyển thư viện Evermusic mà không cần Wi-Fi không?" closed="true" %}}
Wi-Fi Drive yêu cầu cả hai thiết bị phải ở trên cùng một mạng Wi-Fi. Hiện tại không có tùy chọn chuyển qua Bluetooth hoặc mạng di động. Bạn có thể sử dụng AirDrop hoặc ứng dụng Tệp để di chuyển thủ công tệp sao lưu và thư mục nhạc giữa các thiết bị.
{{% /details %}}

{{% details title="Các kết nối dịch vụ đám mây có được chuyển cùng bản sao lưu không?" closed="true" %}}
Bản sao lưu bao gồm cơ sở dữ liệu, danh sách phát, ảnh bìa album và cài đặt. Thông tin đăng nhập dịch vụ đám mây không được bao gồm vì lý do bảo mật. Bạn sẽ cần kết nối lại tài khoản đám mây trên thiết bị mới sau khi khôi phục.
{{% /details %}}

{{% details title="Điều gì xảy ra với thư viện hiện có trên thiết bị thứ hai?" closed="true" %}}
Khôi phục bản sao lưu sẽ thay thế tất cả dữ liệu thư viện nhạc, danh sách phát, cài đặt và ảnh bìa album hiện có trên thiết bị thứ hai. Hãy tạo bản sao lưu riêng cho thiết bị thứ hai trước nếu bạn muốn giữ lại dữ liệu của nó.
{{% /details %}}

{{% details title="Quy trình này có hoạt động giữa iPhone và Mac không?" closed="true" %}}
Có. Evermusic hỗ trợ chuyển Wi-Fi Drive giữa bất kỳ sự kết hợp nào của iPhone, iPad và Mac. Cả hai thiết bị chỉ cần ở trên cùng một mạng Wi-Fi.
{{% /details %}}

{{% details title="Quá trình chuyển mất bao lâu?" closed="true" %}}
Thời gian chuyển phụ thuộc vào kích thước thư viện nhạc và tốc độ Wi-Fi của bạn. Một thư viện điển hình vài gigabyte được chuyển trong 5-15 phút qua mạng gia đình tiêu chuẩn.
{{% /details %}}
