---
title: "Kết nối tới máy chủ"
date: 2026-08-20
description: "Dùng tab Thiết bị trong Everdisk để kết nối tới các máy chủ khác trong mạng của bạn. Thêm và duyệt các máy chủ DLNA, WebDAV, FTP và SFTP cũng như ổ NAS, phát âm thanh và video, tải tệp, và tạo, tải lên, đổi tên, di chuyển hay xóa trên những máy chủ cho phép."
keywords: ["tab Thiết bị Everdisk", "kết nối tới NAS", "ứng dụng DLNA iPhone", "ứng dụng WebDAV iPhone", "ứng dụng FTP iPhone", "ứng dụng SFTP iPhone", "duyệt máy chủ mạng", "phát từ NAS", "tải từ máy chủ", "kết nối đám mây WebDAV"]
tags: ["everdisk", "guide", "devices", "connections"]
readingTime: 9
---


Everdisk không chỉ là một ổ đĩa không dây - nó còn là một ứng dụng khách cho các thiết bị khác trong mạng của bạn. Tab **Thiết bị** cho phép bạn kết nối tới các máy chủ **DLNA**, **WebDAV**, **FTP** và **SFTP**, bao gồm ổ NAS và máy chủ media, rồi duyệt, phát và tải tệp của chúng.

## Màn hình Thiết bị

Tab Thiết bị có hai phần:

- **Kết nối** - những máy chủ bạn đã lưu.
- **Thiết bị có sẵn** - những máy chủ mà Everdisk tự tìm thấy trong mạng nội bộ của bạn.

Để kết nối tới thứ mà Everdisk đã tìm thấy, chỉ cần chạm vào nó trong **Thiết bị có sẵn**. Để thêm một máy chủ thủ công, chạm nút **cộng (+)** hoặc **Kết nối mới**.

## Thêm một kết nối mới

Chạm **Kết nối mới** và chọn loại máy chủ bạn muốn truy cập:

- **DLNA / UPnP** - phù hợp nhất cho máy chủ media. Phát video, nhạc và ảnh từ các thư viện media, ổ lưu trữ mạng cũng như các TV và máy tính hỗ trợ DLNA. DLNA chỉ đọc: bạn có thể duyệt, phát và tải, nhưng không thể tải lên hay thay đổi tệp.
- **WebDAV** - kết nối tới các máy chủ tệp, ổ lưu trữ mạng và ổ đám mây hỗ trợ WebDAV. Đọc và ghi khi máy chủ cho phép.
- **FTP** - phổ biến trên bộ định tuyến, ổ lưu trữ mạng và dịch vụ lưu trữ web. Cổng mặc định là 21 (990 cho FTPS bảo mật); bạn có thể đặt một cổng tùy chỉnh trong địa chỉ, ví dụ `ftp://host:2121`. Để trống tên đăng nhập và mật khẩu để truy cập ẩn danh.
- **SFTP** - kết nối bảo mật qua SSH. Cổng mặc định là 22; dùng một cổng tùy chỉnh trong địa chỉ nếu cần, ví dụ `sftp://host:2222`.

> Everdisk chỉ kết nối tới những giao thức trong mạng nội bộ và được định địa chỉ trực tiếp này. Nó không đăng nhập vào các tài khoản đám mây như Google Drive hay Dropbox. Một ổ đám mây chỉ truy cập được nếu dịch vụ đó cung cấp một địa chỉ **WebDAV** để bạn nhập vào.

## Nhập địa chỉ và đăng nhập

Trong trình chỉnh sửa kết nối, hãy điền:

- **Tiêu đề** - một cái tên thân thiện cho kết nối.
- **URL / địa chỉ** - địa chỉ máy chủ (mỗi loại đều có ví dụ minh họa).
- **Tên đăng nhập** và **Mật khẩu** - để trống cả hai nếu máy chủ cho phép truy cập ẩn danh.

Đối với WebDAV, bạn có thể cho phép chứng chỉ không hợp lệ nếu máy chủ của bạn dùng chứng chỉ tự ký. Nếu không thể xác minh danh tính của một máy chủ bảo mật, Everdisk sẽ hỏi bạn xác nhận trước khi tin cậy nó.

Người dùng miễn phí có thể lưu tối đa **10** kết nối. Premium gỡ bỏ giới hạn này.

## Duyệt, phát và tải

Sau khi kết nối, chạm vào máy chủ để mở nó:

- **Duyệt** các thư mục ở dạng danh sách hoặc lưới, sắp xếp chúng, và xem hình thu nhỏ. Các máy chủ DLNA còn hiển thị thông tin chi tiết bài nhạc và ảnh bìa.
- **Phát** âm thanh và video. Âm thanh được đưa vào hàng đợi của trình phát thu nhỏ; video phát toàn màn hình. Bạn có thể tua trong khi tệp đang được phát trực tuyến.
- **Tải** tệp về thiết bị của bạn. Chọn nhiều tệp cùng lúc để tải hàng loạt. Các lượt tải xuất hiện trong **Truyền tệp** và được lưu vào thư mục **Tài liệu** của bạn.
- **Thông tin** trên bất kỳ mục nào sẽ hiển thị loại, kích thước, ngày, đường dẫn và thông tin chi tiết về media của nó.

## Thay đổi tệp trên máy chủ

Trên những máy chủ cho phép ghi - **WebDAV, FTP và SFTP** - bạn cũng có thể quản lý tệp:

- **Thư mục mới**
- **Tải tệp lên** từ thiết bị của bạn
- **Đổi tên**, **Di chuyển** và **Xóa** (một mục hoặc nhiều mục cùng lúc)

Các máy chủ **DLNA** ở chế độ chỉ đọc, nên những thao tác này không khả dụng ở đó.

## Theo dõi các lượt truyền tệp của bạn

Các lượt tải xuống và tải lên chạy ở chế độ nền và hiển thị trong **Truyền tệp**, mà bạn mở từ góc trên bên trái của tab **Tài liệu**. Ở đó bạn có thể theo dõi tiến trình, và tạm dừng, tiếp tục, thử lại, hủy hay xóa các tác vụ. Bạn cũng có thể tinh chỉnh việc truyền tệp trong [Cài đặt → Mạng](/docs/guide/everdisk/everdisk-guide-settings) (chỉ Wi-Fi so với Wi-Fi và di động, số lượng chạy cùng lúc, và liệu chúng có tiếp tục ở chế độ nền hay không).

## Các bước tiếp theo

- [Tệp & Tài liệu](/docs/guide/everdisk/everdisk-guide-files) - quản lý mọi thứ bạn tải về.
- [Ảnh, Nhạc & Video](/docs/guide/everdisk/everdisk-guide-media) - phát những gì bạn phát trực tuyến.
- [Cài đặt](/docs/guide/everdisk/everdisk-guide-settings) - giới hạn kết nối và các tùy chọn truyền tệp.
