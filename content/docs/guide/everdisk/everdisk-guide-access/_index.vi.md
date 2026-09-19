---
title: "Truy cập & Quyền riêng tư"
date: 2026-08-20
description: "Giữ cho việc chia sẻ Everdisk của bạn an toàn: bảo vệ truy cập bằng tên đăng nhập và mật khẩu, mã hóa kết nối SMB bằng SMB3 (AES), kiểm soát việc các thiết bị đã kết nối có thể tải lên, đổi tên và xóa hay không với Chỉnh sửa tệp, chặn các thiết bị lạ, chọn thùng rác so với xóa vĩnh viễn, và hiểu vì sao mọi thứ đều nằm trong mạng nội bộ của bạn."
keywords: ["bảo vệ bằng mật khẩu Everdisk", "mã hóa SMB", "mã hóa SMB3 AES", "công tắc chỉnh sửa tệp", "chặn thiết bị", "thiết bị bị chặn", "xóa tệp vĩnh viễn", "chỉ mạng nội bộ", "chia sẻ tệp riêng tư", "DLNA không mật khẩu", "an toàn mạng"]
tags: ["everdisk", "guide", "access", "privacy", "security"]
readingTime: 8
---


Everdisk giữ tệp của bạn trên mạng của riêng bạn và cho bạn các quyền kiểm soát đơn giản về việc ai có thể truy cập chúng và họ được làm gì. Bạn tìm thấy những quyền kiểm soát này trong **Cài đặt → Chia sẻ → Truy cập**, cùng một vài cài đặt liên quan trong Trình quản lý tệp.

## Bảo vệ truy cập bằng tên đăng nhập và mật khẩu

Theo mặc định, bất kỳ ai trong cùng mạng và có địa chỉ của bạn đều có thể mở các tệp bạn chia sẻ. Để yêu cầu đăng nhập:

1. Vào **Cài đặt → Chia sẻ → Truy cập**.
2. Nhập một **Tên đăng nhập** và một **Mật khẩu**.
3. Giờ đây các kết nối **Trình duyệt (HTTP)**, **Máy tính (WebDAV)**, **Máy tính (Nâng cao) (SMB)** và **Ứng dụng & Thiết bị khác (FTP)** đều sẽ hỏi những thông tin đó trước khi hiển thị tệp của bạn.

Để trống cả hai ô nếu muốn truy cập mở. Mật khẩu của bạn được lưu an toàn trong Keychain của thiết bị.

> **DLNA luôn mở.** Kết nối TV & Trung tâm giải trí (DLNA) không thể được bảo vệ bằng mật khẩu, nên khi đã bật, bất kỳ thiết bị nào trong cùng mạng Wi-Fi đều có thể duyệt media bạn chia sẻ. Hãy tắt nó nếu bạn chỉ muốn các kết nối được bảo vệ, và chỉ chia sẻ trên những mạng bạn tin cậy.

## Mã hóa kết nối SMB (SMB3 / AES)

Tên đăng nhập và mật khẩu kiểm soát **ai** có thể kết nối, nhưng dữ liệu tự nó vẫn truyền dưới dạng không mã hóa trên hầu hết các kết nối. **SMB là kết nối duy nhất Everdisk có thể mã hóa**, nó xáo trộn mọi lần truyền để không ai khác trong cùng mạng đọc được.

Để bật nó:

1. Đặt **Tên đăng nhập** và **Mật khẩu** như ở trên - kết nối có mã hóa không thể ẩn danh.
2. Vào **Cài đặt → Chia sẻ** và bật **Yêu cầu mã hóa SMB**.
3. **Dừng rồi Bắt đầu** chia sẻ lại để thay đổi có hiệu lực.

Mọi lần truyền SMB khi đó được bảo vệ bằng **mã hóa SMB3 (AES)**. Thiết bị kết nối phải hỗ trợ SMB3 - Finder trên một chiếc Mac hiện đại, hoặc **Windows 10 trở lên**. Đây là lựa chọn tuyệt vời trên Wi-Fi bạn chưa hoàn toàn tin tưởng. Mã hóa SMB là một tính năng Premium.

## Cho phép hoặc chặn chỉnh sửa (Chỉnh sửa tệp)

Công tắc **Chỉnh sửa tệp** kiểm soát việc các thiết bị đã kết nối chỉ có thể xem tệp của bạn, hay còn có thể thay đổi chúng.

- **Bật** (mặc định): các thiết bị đã kết nối có thể **tải lên, đổi tên và xóa** các tệp bạn chia sẻ - nhờ đó thiết bị của bạn hoạt động như một ổ đĩa mạng hai chiều thực thụ.
- **Tắt**: các tệp bạn chia sẻ ở chế độ **chỉ đọc**. Người khác có thể xem và tải xuống, nhưng không thể thêm hay thay đổi bất cứ thứ gì.

Việc bật nó sẽ hiển thị một cảnh báo ngắn vì nó cho phép người khác chỉnh sửa tệp của bạn. Nó mang huy hiệu **Quan trọng** khi đang bật.

## Chặn một thiết bị

Nếu bạn thấy một thiết bị mà mình không nhận ra:

1. Trên màn hình Chia sẻ, tìm nó trong phần **Ai đang kết nối**.
2. Chạm nút thêm hành động của nó và chọn **Chặn thiết bị này**.

Các thiết bị bị chặn được liệt kê trong **Cài đặt → Chia sẻ → Truy cập → Thiết bị bị chặn**, nơi bạn có thể **bỏ chặn** một thiết bị hoặc **Bỏ chặn tất cả**. Việc chặn đi theo thiết bị ngay cả khi địa chỉ mạng của nó thay đổi (đối với các kết nối Trình duyệt, Máy tính và TV).

## Thùng rác so với xóa vĩnh viễn

Khi một tệp bị xóa - bởi bạn trong trình quản lý tệp, hoặc bởi một thiết bị đã kết nối - nó thường chuyển vào **thùng rác** có thể khôi phục để bạn có thể lấy lại.

Nếu bạn muốn tệp bị loại bỏ ngay lập tức mà không thể khôi phục, hãy bật **Xóa tệp vĩnh viễn** trong **Cài đặt → Trình quản lý tệp → Xóa tệp**. Tùy chọn này mặc định là tắt. **Nó ảnh hưởng đến trình quản lý tệp trên thiết bị** và **các lượt xóa thực hiện qua mạng**; nó không thay đổi cách thư viện Ảnh hay thư viện Nhạc của hệ thống xử lý việc xóa.

## Mọi thứ đều nằm trong mạng nội bộ

Everdisk chỉ chia sẻ qua **mạng nội bộ** của bạn - không có gì được tải lên internet và không có tài khoản đám mây nào ở giữa. Một vài điều đáng biết:

- Everdisk cần quyền **Mạng nội bộ** của iOS để các thiết bị lân cận có thể tìm thấy nó. Nếu quyền đó bị tắt, một ghi chú sẽ giải thích cách bật lại nó trong ứng dụng Cài đặt của iOS.
- Để riêng tư nhất, chỉ nên chia sẻ khi bạn đang ở trên một mạng **Wi-Fi gia đình hoặc riêng tư** mà bạn tin cậy, và hãy cẩn thận trên Wi-Fi công cộng. Tên đăng nhập và mật khẩu giúp ích, nhưng không thể thay thế cho một mạng đáng tin cậy.
- **Tùy chọn riêng tư nhất trong tất cả là cáp USB tới một máy Mac** - dữ liệu đi thẳng qua cáp và không bao giờ chạm tới bộ định tuyến hay internet. Xem [Kết nối các thiết bị của bạn](/docs/guide/everdisk/everdisk-guide-connect).

## Các bước tiếp theo

- [Chia sẻ](/docs/guide/everdisk/everdisk-guide-sharing) - chọn nội dung để chia sẻ và bắt đầu chia sẻ.
- [Cài đặt](/docs/guide/everdisk/everdisk-guide-settings) - tất cả cài đặt Truy cập và Trình quản lý tệp ở cùng một nơi.
