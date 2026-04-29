---
title: "Xuất toàn bộ lịch sử nghe nhạc từ Evermusic & Flacbox sang Last.fm"
date: 2024-01-30
description: "Tìm hiểu cách xuất lịch sử nghe nhạc từ Evermusic và Flacbox và tải lên Last.fm bằng tệp CSV và công cụ Last.fm Scrubbler cho Windows."
keywords: ["evermusic", "flacbox", "lastfm", "lịch sử nghe nhạc", "scrobbling", "xuất bài hát", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "gần đây", "lastfm", "xuất", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Tóm tắt:** Xuất lịch sử nghe nhạc từ Evermusic hoặc Flacbox dưới dạng tệp CSV, sau đó tải lên Last.fm bằng công cụ miễn phí Last.fm-Scrubbler-WPF trên Windows. Scrobble tự động cũng có sẵn trong cả hai ứng dụng.

**Cập nhật:** Scrobble tự động hiện đã có sẵn! Tìm hiểu thêm tại đây: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling là cách đơn giản để tự động lưu các thông tin cơ bản như tiêu đề và nghệ sĩ của bài hát bạn đang phát vào một dịch vụ trực tuyến. Sau đó, bạn có thể xem lại lịch sử nghe nhạc của mình.

[Last.fm](https://www.last.fm/home), được hỗ trợ bởi hệ thống gợi ý âm nhạc có tên Audioscrobbler, cung cấp dịch vụ này miễn phí. Nó tạo ra một hồ sơ chi tiết về sở thích âm nhạc của bạn bằng cách ghi lại các bản nhạc bạn nghe, dù là từ các đài phát thanh internet, máy tính hay các thiết bị nghe nhạc di động khác nhau. Bạn có thể truy cập trang web sau đó để nhận các gợi ý nghệ sĩ hoặc album mới phù hợp với sở thích âm nhạc của bạn.

Bạn có thể tải lịch sử nghe nhạc lên [Last.fm](http://Last.fm) từ ứng dụng Evermusic và Flacbox bằng công cụ miễn phí, và chúng tôi sẽ hướng dẫn bạn cách thực hiện.

Mở phần 'Thư viện nhạc' của ứng dụng và cuộn đến phần 'Truy cập nhanh'. Nhấn vào mục menu 'Gần đây'.

![màn hình thư viện nhạc](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

Trên màn hình 'Gần đây', nhấn nút 'Thêm' ở góc trên bên phải để kích hoạt menu 'Thêm hành động'. Nhấn vào mục menu 'Xuất danh sách bài hát'.

![màn hình gần đây](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

Trên màn hình 'Chọn định dạng tệp', bạn có thể chọn định dạng của tệp đích. Các tùy chọn có sẵn - CSV, TXT, M3U.

![màn hình chọn định dạng tệp](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Viết tắt của Comma-Separated Values, hoàn hảo để sắp xếp dữ liệu của bạn thành định dạng bảng gọn gàng. Trong tệp đích, bạn sẽ tìm thấy các tham số như Tên nghệ sĩ, Tên album, Tên bản nhạc, Dấu thời gian (thời điểm bạn nghe các bản nhạc), Tên nghệ sĩ album và Thời lượng bản nhạc.

TXT: Ở đây chúng ta nói về tệp văn bản thuần túy. Đơn giản và dễ hiểu, với các tham số bao gồm Tên nghệ sĩ, Tên album, Tên bản nhạc và Thời lượng.

M3U: Định dạng này là lựa chọn hàng đầu để tạo danh sách phát. Rất tuyệt vì bạn có thể xuất danh sách bài hát và thưởng thức các bản nhạc trên bất kỳ thiết bị nào, ngay cả khi bạn không có tệp gốc (miễn là bạn chọn tùy chọn URL tuyệt đối cho tệp phương tiện). Trong tệp đầu ra, bạn sẽ tìm thấy các tham số như Thời lượng, Tên nghệ sĩ, Tên bản nhạc và Vị trí tệp phương tiện.

Đối với nhiệm vụ của chúng ta, chọn CSV là lựa chọn đúng đắn. Chúng ta sẽ sử dụng tệp này với phần mềm miễn phí Last.fm-Scrubbler-WPF để tải lịch sử nghe nhạc lên dịch vụ [Last.fm](http://Last.fm). Chỉ cần chọn CSV và nhấn nút 'Xuất'.

![màn hình xuất hoàn tất](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Sau khi xuất hoàn tất, chỉ cần nhấn nút 'Hiển thị tệp', ứng dụng sẽ hiển thị tệp đã tạo trong thư mục tài liệu của bạn. Sau đó, nhấn nút 'Thêm hành động' bên cạnh tên tệp và chọn tùy chọn 'Mở trong' từ menu. Bước tiếp theo là sao chép tệp đã xuất sang máy tính để bàn của bạn. Bạn có thể dễ dàng thực hiện bằng cách chọn tùy chọn AirDrop từ menu 'Mở trong'.

![thêm hành động cho tệp đã xuất](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Tiếp theo, chúng ta sẽ sử dụng một ứng dụng khách mã nguồn mở miễn phí của [Last.FM](http://Last.FM) chỉ có trên nền tảng Windows. Ứng dụng khách này cho phép bạn cập nhật hiệu quả lịch sử nghe nhạc trên [Last.FM](http://Last.FM) bằng tệp CSV mà chúng ta vừa xuất.

Nếu bạn hiện không sử dụng máy tính Windows, đừng lo lắng. Bạn vẫn có thể truy cập ứng dụng khách này bằng cách cài đặt VirtualBox trên Mac và sử dụng tệp hình ảnh môi trường phát triển Windows chính thức.

Đây là những gì bạn cần làm:

- Cài đặt VirtualBox từ liên kết sau: [Tải VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Tải và cài đặt môi trường phát triển Windows từ liên kết này: [Môi trường phát triển Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Trên máy tính Windows của bạn (hoặc ứng dụng VirtualBox với hình ảnh Windows Development) tải và cài đặt [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - phần mềm mã nguồn mở miễn phí có trên GitHub. Chúng tôi đã thử nghiệm trên phiên bản 1.28 mà bạn có thể tải tại đây: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Trang tải Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

Trong phần 'Assets', nhấn vào [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) để tải tệp cài đặt nén. Giải nén tệp đã tải và mở thư mục đã giải nén.

- QUAN TRỌNG

Ứng dụng này vẫn đang trong giai đoạn beta. Các nhà phát triển ứng dụng chưa thực hiện nhiều thử nghiệm. Họ khuyến nghị thử scrobble vào tài khoản thử nghiệm trước và xem những thứ bạn muốn scrobble có hoạt động chính xác không. Đặc biệt nếu bạn scrobble nhiều bản nhạc cùng lúc. Vui lòng cẩn thận với tài khoản của bạn.

Chạy Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Trên màn hình chính của ứng dụng, chỉ cần nhấn vào 'Chưa đăng nhập' ở góc dưới bên trái để kích hoạt màn hình 'Thêm tài khoản'.

![Màn hình thêm tài khoản](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Nhập thông tin đăng nhập của bạn.

![màn hình nhập thông tin đăng nhập](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Nhấn nút 'Login' để thêm tài khoản của bạn.

![Nhấn nút Login để thêm tài khoản của bạn.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Mở tab 'File Parse Scrobbler' để bắt đầu nhập tệp CSV từ ứng dụng Evermusic.

![Mở tab File Parse Scrobbler để bắt đầu nhập tệp CSV từ ứng dụng Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Chọn 'Parser: CSV' và nhấn nút 'Settings'.

Trên màn hình tiếp theo, bạn có thể chọn thứ tự các tham số trong tệp CSV của bạn.

Các trường riêng lẻ có thể được bao quanh bằng dấu ngoặc kép và CẦN được bao quanh bằng dấu ngoặc kép nếu trường chứa bất kỳ ký tự phân cách nào đã đặt. Ví dụ:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Vì vậy, giữ nguyên tất cả cài đặt mặc định; điều duy nhất bạn cần thay đổi là bật hộp kiểm trong trường 'Has Fields Enclosed In Quotes'.

Nhấn 'Save & Close' để áp dụng thay đổi.

![chọn thứ tự các tham số trong tệp CSV của bạn.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Scrobble phân tích tệp có hai chế độ. Chúng có thể được thay đổi bằng ComboBox 'Scrobbling Mode'.

Chế độ Bình thường: Trong chế độ này, các bản nhạc sẽ được scrobble với dấu thời gian từ scrobble đã phân tích. Chỉ các scrobble mới hơn 14 ngày mới có thể được scrobble.

Chế độ Nhập: Trong chế độ này, các bản nhạc sẽ được scrobble với dấu thời gian được tính từ 'Finish Time' và thời lượng đã chọn giữa mỗi bản nhạc. Điều này cho phép scrobble các bản nhạc ngay cả khi dấu thời gian của scrobble đã phân tích cũ hơn 14 ngày. Do đó, bản nhạc đầu tiên (trên cùng) trong tệp CSV sẽ được scrobble với 'Finish Time'.

Chọn tệp CSV đã tạo trước đó từ ứng dụng Evermusic trong trường 'File:' và nhấn 'Parse'. Trong một số trường hợp, bạn có thể thấy cảnh báo lỗi nói rằng một số scrobble không thể phân tích được. Không sao nếu bạn có một số bản nhạc thiếu dữ liệu đầy đủ như Tên nghệ sĩ.

![một số scrobble không thể phân tích được](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Nhấn nút 'Check All' để chọn tất cả các bản nhạc đã phân tích.

![Nhấn nút Check All để chọn tất cả các bản nhạc đã phân tích.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Nhấn nút 'Preview' để kiểm tra tất cả thay đổi sẽ được gửi đến máy chủ.

![Nhấn nút Preview để kiểm tra tất cả thay đổi sẽ được gửi đến máy chủ.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Nhấn nút 'Scrobble' để tải tất cả thay đổi lên máy chủ.

![Nhấn nút Scrobble để tải tất cả thay đổi lên máy chủ.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Trước đây Last.fm-Scrubbler-WPF không có giới hạn scrobble mỗi ngày. Điều này đã thay đổi vì một số người đã sử dụng Scrubbler để scrobble quá nhiều bản nhạc, gây ra sự cố cho trang Last.fm. Giới hạn scrobble hiện tại là 2800 scrobble mỗi ngày. Khi bạn cố scrobble nhiều hơn, bạn sẽ nhận được thông báo lỗi. Có kế hoạch thêm 'hàng đợi scrobble', vì vậy nếu bạn cần scrobble hơn 2800 bản nhạc, chúng sẽ được thêm vào hàng đợi và tự động scrobble sau một thời gian. Bạn có thể kiểm tra còn bao nhiêu scrobble trong chế độ xem chọn người dùng.

Khi tất cả bản ghi được tải lên máy chủ thành công, bạn sẽ thấy thông báo ở cuối cửa sổ ứng dụng xác nhận: 'Successfully scrobbled selected tracks.'

![Successfully scrobbled selected tracks.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Bây giờ bạn có thể mở hồ sơ của mình trên trang [Last.fm](http://Last.fm) và kiểm tra tất cả thay đổi.

![hồ sơ của bạn trên trang Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Câu hỏi thường gặp

{{% details title="Tôi có thể scrobble tự động mà không cần xuất tệp CSV không?" closed="true" %}}
Có. Cả Evermusic và Flacbox đều hỗ trợ scrobble tự động sang Last.fm. Xem hướng dẫn: [Cách Scrobble sang Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Nếu CSV của tôi có bản nhạc cũ hơn 14 ngày thì sao?" closed="true" %}}
Sử dụng Chế độ Nhập trong Last.fm-Scrubbler-WPF. Nó tính lại dấu thời gian từ Finish Time, cho phép bạn scrobble bản nhạc bất kể ngày gốc.
{{% /details %}}

{{% details title="Tôi không có máy tính Windows. Tôi vẫn có thể sử dụng Last.fm-Scrubbler không?" closed="true" %}}
Có. Cài đặt VirtualBox trên Mac của bạn và tải hình ảnh Môi trường Phát triển Windows miễn phí từ Microsoft. Chạy Last.fm-Scrubbler-WPF bên trong máy ảo.
{{% /details %}}

{{% details title="Tại sao một số scrobble không được phân tích?" closed="true" %}}
Các bản nhạc thiếu siêu dữ liệu cần thiết (như tên nghệ sĩ) không thể được phân tích. Điều này là bình thường và không ảnh hưởng đến các bản nhạc khác trong tệp.
{{% /details %}}

{{% details title="Có giới hạn scrobble hàng ngày không?" closed="true" %}}
Có. Last.fm-Scrubbler-WPF cho phép tối đa 2.800 scrobble mỗi ngày. Nếu bạn cần scrobble nhiều hơn, hãy chia quy trình thành nhiều ngày.
{{% /details %}}
