---
title: "Kết nối các thiết bị của bạn"
date: 2026-08-20
description: "Hướng dẫn từng bước để kết nối tới ổ đĩa không dây Everdisk của bạn: xem trên TV thông minh qua DLNA, mở tệp của bạn trong mọi trình duyệt web, gắn thiết bị của bạn như một ổ đĩa mạng trong Finder, Windows hay Linux qua WebDAV hoặc SMB (với mã hóa SMB3/AES tùy chọn), kết nối các ứng dụng quản lý tệp qua FTP, và truyền tệp qua cáp USB tới máy Mac ngay cả khi không có Wi-Fi."
keywords: ["kết nối tới Everdisk", "phát lên TV DLNA", "mở tệp trong trình duyệt", "gắn ổ đĩa mạng Finder", "WebDAV Windows Linux", "ứng dụng tệp FTP", "truyền tệp qua cáp USB Mac", "kết nối iPhone với máy tính", "ổ đĩa mạng iPhone"]
tags: ["everdisk", "guide", "connect"]
readingTime: 11
---


Sau khi bạn chạm **Bắt đầu** trên màn hình [Chia sẻ](/docs/guide/everdisk/everdisk-guide-sharing), những thiết bị khác có thể kết nối tới tệp của bạn theo năm cách khác nhau. Hãy chọn phương thức phù hợp với thiết bị bạn muốn dùng. Trong mọi trường hợp, **địa chỉ** chính xác mà bạn cần đều được hiển thị trong phần **Cách kết nối** của màn hình Chia sẻ.

> Cả hai thiết bị phải nằm trên **cùng một mạng Wi-Fi** - hoặc, đối với máy Mac, được kết nối bằng **cáp USB** (xem phần cuối).

## Xem trên TV (DLNA)

Dùng cách này để hiển thị ảnh, video và nhạc trên một TV thông minh hay trình phát media.

1. Trong **Cài đặt → Chia sẻ → Kết nối**, đảm bảo **TV & Trung tâm giải trí** đang bật (mặc định là bật).
2. Trên màn hình Chia sẻ, chạm **Bắt đầu**.
3. Trên TV, mở trình phát media tích hợp hoặc ứng dụng máy chủ media của nó (có thể được gọi là Media Player, SmartShare, AllShare, hay tương tự).
4. Thiết bị của bạn sẽ xuất hiện trong danh sách các máy chủ media theo tên của nó (ví dụ "Speedy-Hare"). Hãy chọn nó.
5. Duyệt ảnh, video và nhạc đã chia sẻ của bạn rồi bắt đầu phát. Hình thu nhỏ xem trước sẽ tự động hiện ra.

Lưu ý:

- DLNA không thể được bảo vệ bằng mật khẩu, nên khi đang bật, kết nối này mở cho bất kỳ ai trong cùng mạng Wi-Fi.
- Nếu một video không phát được trên TV đời cũ, hãy giảm chất lượng video trong **Cài đặt → Chia sẻ → Video** để Everdisk chuyển đổi nó sang định dạng tương thích hơn.

## Mở trong trình duyệt web (HTTP)

Dùng cách này để chuyển tệp cho bất cứ ai có trình duyệt web - không cần cài ứng dụng nào.

1. Trong **Cài đặt → Chia sẻ → Kết nối**, đảm bảo **Trình duyệt** đang bật.
2. Chạm **Bắt đầu**.
3. Trên màn hình Chia sẻ, sao chép địa chỉ **Trình duyệt** (hoặc hiển thị mã QR của nó).
4. Trên điện thoại, máy tính bảng hay máy tính bên kia, mở bất kỳ trình duyệt web nào (Safari, Chrome, Edge, Firefox) và nhập địa chỉ đó.
5. Trang sẽ mở ra cùng các tệp bạn đã chia sẻ.

Trong trình duyệt, người kia có thể:

- Chuyển giữa chế độ xem **danh sách** và **lưới**, và sắp xếp theo tên, ngày hay kích thước.
- Xem **hình thu nhỏ** thật cho ảnh, video, PDF và ảnh bìa nhạc.
- Mở một tấm ảnh thành **thư viện** toàn màn hình với thao tác vuốt, chụm để thu phóng và trình chiếu.
- Nghe nhạc trong **trình phát** tích hợp với hàng đợi, phát ngẫu nhiên và lặp lại.
- **Tải** bất kỳ tệp nào, hoặc tải cả một thư mục (hay nhiều mục đã chọn) thành một tệp **Archive.zip** duy nhất.
- **Tải lên** tệp trở lại thiết bị của bạn - chỉ khi bạn đã bật **Chỉnh sửa tệp** (xem [Truy cập & Quyền riêng tư](/docs/guide/everdisk/everdisk-guide-access)).

## Dùng như một ổ đĩa mạng (WebDAV)

Dùng cách này để làm cho thiết bị của bạn hiện ra như một ổ đĩa thông thường trên máy Mac, PC Windows hay máy Linux, để bạn có thể kéo tệp theo cả hai chiều.

**Trên máy Mac (Finder)**

1. Trong **Cài đặt → Chia sẻ → Kết nối**, đảm bảo **Máy tính** đang bật.
2. Chạm **Bắt đầu** và ghi lại địa chỉ **Máy tính (WebDAV)**.
3. Trong Finder, chọn **Đi → Kết nối tới máy chủ** (hoặc nhấn **⌘K**).
4. Nhập địa chỉ WebDAV đúng như hiển thị rồi nhấp **Kết nối**.
5. Nhập tên đăng nhập và mật khẩu nếu bạn đã đặt, nếu không thì kết nối với tư cách khách.
6. Thiết bị của bạn sẽ mở ra như bất kỳ ổ đĩa mạng nào khác. Hãy kéo tệp vào hoặc ra.

**Trên Windows**

1. Mở **File Explorer**, nhấp chuột phải vào **This PC**, rồi chọn **Add a network location** (hoặc ánh xạ một ổ đĩa mạng).
2. Nhập địa chỉ WebDAV hiển thị trong Everdisk.
3. Nhập tên đăng nhập và mật khẩu nếu bạn đã đặt.

**Trên Linux**

1. Mở trình quản lý tệp và chọn **Kết nối tới máy chủ** (hoặc dùng `davs://` / `dav://`).
2. Nhập địa chỉ WebDAV hiển thị trong Everdisk.

Kết nối chỉ đọc hay hai chiều tùy thuộc vào cài đặt **Chỉnh sửa tệp**. Khi bật, bạn có thể sao chép tệp vào thiết bị và đổi tên hoặc xóa chúng; khi tắt, ổ đĩa ở chế độ chỉ đọc.

## Kết nối qua SMB (ổ đĩa mạng có mã hóa)

SMB là một ổ đĩa mạng cho Mac, Windows và Linux, dựa trên tính năng chia sẻ tệp sẵn có trong các hệ thống đó, nên thiết bị của bạn hiện ra như một ổ đĩa mạng thông thường - và đây là kết nối duy nhất bạn có thể mã hóa.

1. Trong **Cài đặt → Chia sẻ → Kết nối**, đảm bảo **Máy tính (Nâng cao)** (kết nối SMB) đang bật.
2. Chạm **Bắt đầu** và ghi lại địa chỉ **SMB**, trông giống `smb://192.168.1.20:4455/Share`.
3. Kết nối từ máy tính của bạn:
   - **Mac:** thiết bị của bạn tự hiện lên trong **thanh bên Finder** dưới mục **Vị trí** (Mạng) - chỉ cần bấm vào nó rồi đăng nhập. Để kết nối bằng tay, chọn **Đi → Kết nối tới máy chủ** (**⌘K**) và nhập địa chỉ.
   - **Windows:** mở **File Explorer**, nhấp chuột phải vào **This PC** và chọn **Ánh xạ ổ đĩa mạng**, rồi nhập `\\<address>\Share` dùng tên máy chủ và tên thư mục chia sẻ từ màn hình Chia sẻ (hoặc gõ địa chỉ `smb://` vào thanh địa chỉ).
   - **Linux:** trong trình quản lý tệp chọn **Kết nối tới máy chủ** và nhập địa chỉ.
4. Nhập tên đăng nhập và mật khẩu nếu bạn đã đặt, nếu không thì kết nối với tư cách khách.
5. Thư mục chia sẻ được đặt tên là **Share**. Khi bật **Chỉnh sửa tệp**, bạn có thể sao chép tệp theo cả hai chiều; khi tắt, nó ở chế độ chỉ đọc.

**Bật mã hóa (khuyến nghị trên Wi-Fi không tin cậy)**

SMB là kết nối Everdisk duy nhất có thể mã hóa. Để bảo vệ mọi lần truyền bằng **mã hóa SMB3 (AES)**:

1. Trong **Cài đặt → Chia sẻ → Truy cập**, đặt **Tên đăng nhập** và **Mật khẩu** - kết nối có mã hóa không thể ẩn danh.
2. Trong **Cài đặt → Chia sẻ**, bật **Yêu cầu mã hóa SMB**.
3. **Dừng rồi Bắt đầu** chia sẻ lại để thay đổi có hiệu lực.

Máy khách của bạn phải hỗ trợ SMB3 - Finder trên một chiếc Mac hiện đại, hoặc **Windows 10 trở lên**. Mã hóa SMB là một tính năng Premium.

## Kết nối một ứng dụng quản lý tệp (FTP)

Dùng cách này cho các ứng dụng quản lý và truyền tệp quen dùng FTP (ví dụ FileZilla hay Cyberduck trên máy tính).

1. Trong **Cài đặt → Chia sẻ → Kết nối**, đảm bảo **Ứng dụng & Thiết bị khác** đang bật.
2. Chạm **Bắt đầu** và ghi lại địa chỉ **FTP**.
3. Trong ứng dụng FTP của bạn, thêm một kết nối mới bằng địa chỉ đó.
4. Nhập tên đăng nhập và mật khẩu nếu bạn đã đặt, hoặc để trống chúng để truy cập ẩn danh.

## Truyền tệp qua cáp USB (Mac, không cần Wi-Fi)

Dùng cách này khi không có Wi-Fi, hoặc khi bạn muốn truyền tệp nhanh nhất và riêng tư nhất. Cách này chỉ hoạt động với một máy **Mac**.

1. Cắm iPhone hoặc iPad của bạn vào máy Mac bằng cáp sạc thông thường.
2. Nếu được hỏi trên thiết bị, hãy chạm **Tin cậy máy tính này**.
3. Trong Everdisk, chạm **Bắt đầu**. Một ghi chú **Có sẵn kết nối nhanh** sẽ xuất hiện và màn hình Chia sẻ hiển thị một địa chỉ bổ sung với huy hiệu **Kết nối bằng cáp** kết thúc bằng `.local`.
4. Trên máy Mac, mở Finder → **Đi → Kết nối tới máy chủ** (**⌘K**) và nhập địa chỉ `.local` đó (nó hoạt động cho cả kết nối Trình duyệt lẫn Máy tính).
5. Thiết bị của bạn sẽ mở ra qua cáp - nhanh hơn Wi-Fi, và dữ liệu không bao giờ chạm tới bộ định tuyến hay internet.

Lưu ý:

- Dùng **tên `.local`**, không dùng địa chỉ IP (địa chỉ IP chỉ hoạt động qua Wi-Fi), và không bao giờ dùng `localhost`.
- Đường truyền bằng cáp **chỉ dành cho Mac**. Các PC Windows và thiết bị Android buộc phải dùng Wi-Fi.
- Bạn cũng có thể kéo tệp vào thư mục Everdisk bằng Finder trên máy Mac, hoặc bằng ứng dụng Apple Devices (hay iTunes) trên Windows, thông qua tính năng chia sẻ tệp tiêu chuẩn của iOS.

## Các bước tiếp theo

- [Truy cập & Quyền riêng tư](/docs/guide/everdisk/everdisk-guide-access) - thêm mật khẩu, cho phép tải lên, chặn một thiết bị.
- [Ảnh, Nhạc & Video](/docs/guide/everdisk/everdisk-guide-media) - chia sẻ toàn bộ thư viện của bạn và đặt chất lượng.
- [Kết nối tới máy chủ](/docs/guide/everdisk/everdisk-guide-devices) - truy cập các thiết bị khác từ Everdisk.
