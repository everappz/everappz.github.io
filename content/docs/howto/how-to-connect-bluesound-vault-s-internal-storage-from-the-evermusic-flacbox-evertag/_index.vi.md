---
title: "Cách kết nối bộ nhớ trong của Bluesound VAULT từ Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Tìm hiểu cách truy cập ổ cứng bên trong của Bluesound VAULT từ Evermusic, Flacbox và Evertag sử dụng giao thức SMB để quản lý, chỉnh sửa và phát các tệp âm thanh."
keywords: ["bluesound vault", "kết nối bộ nhớ smb", "evermusic smb", "flacbox vault", "evertag smb", "bộ nhớ nas nhạc", "ổ đĩa bên trong vault"]
tags: ["evermusic", "kết nối", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Tóm tắt:** Kết nối với bộ nhớ trong của Bluesound VAULT qua SMB sử dụng Evermusic, Flacbox hoặc Evertag. Tìm địa chỉ IP của VAULT trong ứng dụng BluOS, nhập nó làm kết nối SMB với quyền truy cập khách và bắt đầu phát hoặc quản lý các tệp nhạc của bạn.

Bluesound VAULT có ổ cứng bên trong và hoạt động như một thiết bị lưu trữ gắn mạng (NAS). Truy cập ổ cứng bên trong của VAULT cho phép bạn thêm/xóa tệp, chỉnh sửa thẻ siêu dữ liệu từ các ứng dụng của chúng tôi Evermusic, Flacbox, Evertag.

**Sau đây là các bước để truy cập ổ cứng bên trong của VAULT:**

1. Trong ứng dụng BluOS, chọn **Trợ giúp > Chẩn đoán**.

2. Từ trang **Chẩn đoán**, lấy **Địa chỉ IP** của VAULT. **Địa chỉ IP** này sẽ được sử dụng trong các bước tiếp theo.

3. Mở Evermusic, Flacbox hoặc Evertag.

   ![Ứng dụng Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Mở màn hình "Kết nối" và chọn mục menu "Kết nối dịch vụ đám mây".

   ![Màn hình Kết nối Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Chọn dịch vụ đám mây "SMB".

   ![Màn hình Kết nối Dịch vụ Đám mây Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Trên "Màn hình cấu hình SMB" nhập URL theo định dạng sau:

   ```
   SMB://<<VAULT-IP>>
   ```

   Thay thế `<<VAULT-IP>>` bằng **Địa chỉ IP** đã lấy ở Bước 2.

   **Lưu ý:** Để trống các trường Đăng nhập và Mật khẩu vì bộ nhớ VAULT hỗ trợ chế độ KHÁCH.

   ![Màn hình kết nối SMB Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Nhấn nút "Đăng nhập" để lưu cấu hình.

8. Mở bộ nhớ đám mây đã kết nối, điều hướng vào thư mục chứa tệp âm thanh và nhấn vào bất kỳ tệp nào để khởi động trình phát âm thanh.

   ![Màn hình Máy chủ SMB đã mở Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Bạn cũng có thể chỉnh sửa tệp bằng trình quản lý tệp tích hợp.

   ![Màn hình Trình quản lý Tệp Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Với các bước đơn giản này, bạn có thể dễ dàng truy cập ổ cứng bên trong của Bluesound VAULT và kiểm soát thư viện nhạc của mình bằng Evermusic, Flacbox hoặc Evertag.

## Câu hỏi thường gặp

{{% details title="Tôi có cần tên người dùng và mật khẩu để kết nối với Bluesound VAULT không?" closed="true" %}}
Không. Bluesound VAULT hỗ trợ truy cập khách (ẩn danh) qua SMB. Để trống các trường Đăng nhập và Mật khẩu khi cấu hình kết nối.
{{% /details %}}

{{% details title="Tôi có thể chỉnh sửa thẻ nhạc trên Bluesound VAULT không?" closed="true" %}}
Có. Sử dụng Evertag, bạn có thể chỉnh sửa thẻ siêu dữ liệu (tiêu đề, nghệ sĩ, album, v.v.) cho các tệp âm thanh được lưu trữ trực tiếp trên ổ cứng bên trong của VAULT.
{{% /details %}}

{{% details title="Bluesound VAULT hỗ trợ những giao thức nào?" closed="true" %}}
Bluesound VAULT cung cấp bộ nhớ trong của mình qua SMB (Server Message Block). Evermusic, Flacbox và Evertag đều hỗ trợ kết nối SMB, giúp việc kết nối trở nên đơn giản.
{{% /details %}}

{{% details title="Tôi có thể phát nhạc trực tuyến từ VAULT mà không cần sao chép tệp vào iPhone không?" closed="true" %}}
Có. Sau khi kết nối qua SMB, bạn có thể phát trực tuyến các tệp âm thanh trực tiếp từ ổ đĩa bên trong của VAULT mà không cần sao chép chúng vào thiết bị của bạn.
{{% /details %}}
