---
title: "Evertag 4.2: kết nối đám mây mới, giải thích cài đặt trình chỉnh sửa thẻ"
date: 2026-05-09
description: "Evertag 4.2 thêm kết nối Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP và NFS, làm mới Wi-Fi Drive và cập nhật giao diện cho Liquid Glass. Bài viết này cũng giải thích mọi cài đặt của trình chỉnh sửa thẻ — bao gồm ID3v2.4 vs ID3v2.3, co giãn ảnh bìa album, sao chép thẻ, các chế độ tải lên đám mây và những tùy chọn đúng cho Spotify cùng các dịch vụ phát trực tuyến khác."
keywords: ["Evertag 4.2", "cập nhật Evertag", "trình chỉnh sửa thẻ ID3 iPhone", "ID3v2.4 vs ID3v2.3", "chỉnh sửa thẻ FLAC iOS", "chỉnh sửa thẻ MP3 iPhone", "chỉnh sửa ảnh bìa album iOS", "trình chỉnh sửa thẻ cho Spotify", "trình chỉnh sửa thẻ Plex", "trình chỉnh sửa thẻ Apple Music", "Evertag trình chỉnh sửa thẻ đám mây", "trình chỉnh sửa thẻ Internxt", "trình chỉnh sửa thẻ Proton Drive", "trình chỉnh sửa thẻ QNAP", "trình chỉnh sửa thẻ Nextcloud", "trình chỉnh sửa thẻ Amazon S3", "trình chỉnh sửa thẻ SFTP iPhone", "trình chỉnh sửa thẻ âm thanh FTP", "trình chỉnh sửa thẻ NFS iPhone", "Wi-Fi Drive trình chỉnh sửa thẻ", "sao chép thẻ ID3", "co giãn ảnh bìa", "thiết kế Liquid Glass", "trình chỉnh sửa metadata âm thanh iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Trình chỉnh sửa thẻ", "ID3", "ID3v2.4", "ID3v2.3", "Thẻ FLAC", "Thẻ MP3", "Ảnh bìa album", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Có gì mới"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Tóm tắt:** [Evertag 4.2](/products/evertag) là một bản cập nhật lớn cho trình chỉnh sửa thẻ âm thanh trên iPhone, iPad và Mac. Chúng tôi đã xử lý các lỗi quan trọng trong chỉnh sửa thẻ và bổ sung hơn 6 kết nối đám mây và máy chủ mới — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, cùng các giao thức **FTP**, **SFTP** và **NFS**. Wi-Fi Drive được làm mới giao diện, có chế độ chọn nhiều, hàng đợi tải lên thông minh hơn và truyền nhanh hơn. Toàn bộ ứng dụng được tinh chỉnh cho thiết kế **Liquid Glass**. Bài viết này cũng đi sâu vào các cài đặt của trình chỉnh sửa thẻ Evertag — giải thích **ID3v2.4 vs ID3v2.3**, **co giãn ảnh bìa album**, **sao chép thẻ**, **các chế độ tải lên đám mây**, **xóa tệp đã tải xuống** và chính xác những tùy chọn nào cần chọn nếu bạn đang chuẩn bị âm thanh cho **Spotify**, **Apple Music**, **Plex**, **Jellyfin** hay bất kỳ dịch vụ phát trực tuyến nào khác.

---

## Xin chào tất cả mọi người!

Một bản cập nhật lớn của Evertag đã có. Chúng tôi xử lý các lỗi quan trọng trong chỉnh sửa thẻ và thêm **hơn 6 kết nối đám mây và máy chủ mới** để việc quản lý metadata âm thanh dễ dàng hơn bao giờ hết — dù thư viện của bạn ở trên đám mây ưu tiên quyền riêng tư, NAS tự host hay máy chủ FTP/SFTP/NFS thông thường.

[Tải Evertag 4.2 trên App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) hoặc cập nhật từ phiên bản hiện tại của bạn.

## Hỗ trợ đám mây và máy chủ mở rộng

Evertag giờ đây kết nối nguyên bản tới một loạt các tùy chọn đám mây và lưu trữ tự host rộng hơn. Bạn có thể chỉnh sửa thẻ ID3, MP4, FLAC, OGG và APE trên các tệp ở bất cứ đâu.

### Lưu trữ đám mây tập trung vào quyền riêng tư: Internxt và Proton Drive

Nếu bạn quan tâm đến mã hóa đầu cuối và lưu trữ không có kiến thức (zero-knowledge), hai cái tên được kính trọng nhất trong nhóm đám mây ưu tiên quyền riêng tư đã được Evertag hỗ trợ gốc:

- **Internxt** — đám mây Tây Ban Nha mã nguồn mở, mã hóa hậu lượng tử, tuân thủ GDPR. Có gói miễn phí.
- **Proton Drive** — kho lưu trữ mã hóa đầu cuối từ nhà phát triển Proton Mail và Proton VPN, có trụ sở tại Thụy Sĩ. Có gói miễn phí, gói trả phí cho thư viện lớn hơn.

Bạn có thể chỉnh sửa metadata trực tiếp trên các tệp âm thanh được lưu trên một trong hai dịch vụ — tệp vẫn được mã hóa khi truyền và chỉ các thẻ mới được ghi lại.

### Giải pháp tự host: QNAP, Nextcloud, Amazon S3

Cho người dùng vận hành hạ tầng riêng:

- **QNAP** — kết nối API gốc tới các thiết bị QNAP NAS. Chỉnh sửa thẻ trên các tệp ở QNAP qua Wi-Fi cục bộ hoặc truy cập từ xa.
- **Nextcloud** — kết nối tới bất kỳ instance Nextcloud nào, dù tự host hay được quản lý.
- **Amazon S3** — trỏ Evertag đến bất kỳ bucket S3 nào (hoặc kho tương thích S3 như Backblaze B2, Wasabi, MinIO, Cloudflare R2) và chỉnh sửa metadata tại chỗ.

### Các giao thức mạng mới: FTP, SFTP, NFS

Đối với người dùng có máy chủ tùy chỉnh, homelab hay NAS chung không có ứng dụng di động trau chuốt, Evertag 4.2 thêm ba giao thức cổ điển:

- **SFTP (SSH File Transfer Protocol)** — câu trả lời đúng cho **chỉnh sửa thẻ từ xa an toàn từ máy chủ của bạn**. SFTP chạy trên SSH nên toàn bộ quá trình truyền (xác thực và dữ liệu âm thanh) đều được mã hóa. Nếu bạn có VPS, máy chủ riêng hoặc máy Linux ở nhà có truy cập SSH, bạn có thể chỉnh sửa thẻ trên các tệp từ xa mà không phải mở thêm thứ gì khác. Hỗ trợ xác thực bằng mật khẩu và bằng khóa.
- **FTP** — chuẩn truyền tệp được thiết lập từ lâu. Hữu ích cho NAS gia đình cũ có FTP nhưng không có tích hợp API gốc.
- **NFS (Network File System)** — giao thức chia sẻ trên thực tế của Linux và hầu hết các thiết bị NAS. Chi phí thấp hơn SMB trên cùng phần cứng.

> **Mẹo:** SFTP là giao thức bạn nên chọn để chỉnh sửa từ xa qua Internet mở. FTP và NFS dùng tốt nhất trong mạng cục bộ — đừng để chúng trên Internet trừ khi đã được bao bằng VPN.

## Nâng cấp Wi-Fi Drive

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) là tính năng tích hợp sẵn trong Evertag để **chuyển tệp âm thanh không dây giữa máy tính và iPhone hoặc iPad — không cần iTunes, không cần dây cáp, không cần tài khoản đám mây**. Cả hai thiết bị phải nằm trên cùng mạng Wi-Fi.

Trong Evertag 4.2, Wi-Fi Drive nhận được:

- **Giao diện hiện đại được làm mới** — gọn gàng hơn và dễ đọc hơn ngay từ cái nhìn đầu, được cập nhật cho Liquid Glass.
- **Chế độ chọn nhiều** — chọn nhiều tệp hoặc thư mục và xử lý hàng loạt.
- **Hàng đợi tải lên thông minh hơn** — phản hồi tiến trình rõ ràng hơn và bền hơn trước trục trặc mạng.
- **Tốc độ và độ tin cậy chung được cải thiện** — chuyển dữ liệu nhanh hơn cho thư viện lớn.

Đây là cách nhanh nhất để chuyển một loạt tệp âm thanh từ máy tính sang điện thoại, chỉnh sửa thẻ và gửi về — mà không cần dịch vụ bên thứ ba nào.

## Cài đặt trình chỉnh sửa thẻ: đi sâu

Đây là phần mà hầu hết người dùng không bao giờ đọc — và là phần quyết định xem các thẻ của bạn có hoạt động ở mọi nơi hay chỉ trong một số ứng dụng. Mở Evertag rồi vào phần **cài đặt trình chỉnh sửa thẻ âm thanh**. Dưới đây là những gì mỗi tùy chọn thực sự làm và nên chọn tùy chọn nào tùy mục tiêu của bạn.

### Co giãn ảnh bìa album

Khi bạn lưu ảnh bìa album vào tệp âm thanh, Evertag có thể thu nhỏ hình ảnh trước khi nhúng. Các tùy chọn:

- **Nhỏ** — ảnh hưởng nhỏ nhất đến kích thước tệp, chất lượng hình ảnh thấp hơn.
- **Trung bình** — lựa chọn cân bằng cho hầu hết người dùng.
- **Lớn** — chất lượng cao, phù hợp với trình phát màn hình lớn và CarPlay.
- **Rất lớn** — chất lượng rất cao, kích thước tệp tăng đáng kể.
- **Gốc (Đã tắt)** — nhúng ảnh bìa ở độ phân giải gốc. **Không co giãn.**

**Vì sao điều này quan trọng:**

- **Chất lượng cao hơn = tệp lớn hơn.** Một ảnh bìa 3.000 × 3.000 pixel có thể thêm vài MB cho mỗi bản. Nhân với một album, dung lượng đĩa tăng nhanh.
- **Một số trình phát xử lý kém các hình ảnh nhúng rất lớn.** Thiết bị cũ, một số đầu phát ô tô và một số trình phát máy tính cũ có thể nghẹn với ảnh bìa trên ~1.500 px hoặc từ chối hiển thị.
- **Với hầu hết các quy trình đám mây và phát trực tuyến**, **Trung bình** hoặc **Lớn** là điểm hợp lý. Chỉ dùng **Gốc** khi bạn thật sự cần chất lượng lưu trữ hoặc đang chuẩn bị tệp cho một trình phát mà bạn tin tưởng.

> Tùy chọn kích thước **Gốc** thuộc bản nâng cấp tùy chỉnh cao cấp của Evertag. Các kích thước tiêu chuẩn (Nhỏ/Trung bình/Lớn/Rất lớn) đều miễn phí.

### Tùy chọn lưu thẻ: ID3v2.4 vs ID3v2.3

Đây là cài đặt quan trọng nhất cho khả năng tương thích. ID3v2 là định dạng metadata được dùng bên trong các tệp MP3. Có hai phiên bản được dùng rộng rãi và chúng khác nhau ở các điểm tinh tế nhưng quan trọng.

#### ID3v2.4

- Mới hơn, hỗ trợ **mã hóa văn bản UTF-8** — xử lý đúng các văn tự không phải Latin (Trung, Nga, Nhật, Ả Rập, Do Thái, v.v.).
- Nhiều loại frame hơn (volume tương đối, cài đặt trước EQ, v.v.).
- **Khuyến nghị cho các trình phát hiện đại** hỗ trợ nó.

#### ID3v2.3

- Cũ hơn nhưng **phiên bản ID3 được hỗ trợ phổ biến nhất**.
- Không hỗ trợ UTF-8 trực tiếp (sử dụng UTF-16 cho văn bản Unicode).
- **Khuyến nghị khi bạn cần khả năng tương thích tối đa** với trình phát cũ, dàn âm thanh ô tô và một số ứng dụng máy tính.

#### Khi nào bật ID3v2.4 trong Evertag

- Bạn dùng **trình phát âm thanh hiện đại** như Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (phiên bản hiện tại) hoặc các trình phát Android hiện đại. ✅ **Bật ID3v2.4.**
- Thư viện của bạn chứa **ký tự không phải Latin** (Trung, Hàn, Nhật, Nga, Ả Rập, Hy Lạp, Do Thái). ✅ **Bật ID3v2.4** — UTF-8 xử lý chúng sạch sẽ hơn nhiều.

#### Khi nào tắt ID3v2.4 trong Evertag (dùng ID3v2.3)

- Bạn đang chuẩn bị tệp cho **dàn âm thanh ô tô hoặc đầu phát trên xe cũ hơn** không đọc được thẻ v2.4.
- Sau khi chỉnh sửa, bạn thấy **văn bản bị lỗi hoặc thiếu thẻ** trong một số ứng dụng — đó là dấu hiệu mạnh cho thấy v2.4 không được hỗ trợ ở đó. Trở lại v2.3.
- Bạn nhắm tới **trình phát máy tính cũ** hoặc trình phát di động cũ hơn (iPod đời đầu, một số trình phát MP3 từ những năm 2000–2010).

> **Quy tắc kinh nghiệm:** nếu thẻ của bạn hiển thị đúng ở mọi nơi với v2.4, hãy bật. Nếu chỉ một trình phát quan trọng hiển thị ký tự sai, trống hoặc không đọc được thẻ, tắt v2.4 và lưu lại.

#### Sao chép thẻ

Khi bạn bật **Sao chép thẻ**, Evertag ghi các trường metadata chung (tiêu đề, nghệ sĩ, album, v.v.) vào **cả phần ID3v1 và ID3v2** của tệp. Điều này cải thiện khả năng tương thích với các trình phát rất cũ chỉ đọc ID3v1 (thẻ 128 byte gốc ở cuối tệp).

- **Hầu hết người dùng không cần.** Trình phát hiện đại đọc ID3v2 trước.
- **Chỉ bật nếu** bạn đang xử lý phần cứng cổ điển hoặc phần mềm cụ thể bỏ qua ID3v2.

### Cập nhật tệp trực tuyến: Evertag xử lý chỉnh sửa đám mây như thế nào

Khi bạn chỉnh sửa thẻ trên một tệp được lưu trên đám mây đã kết nối (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP, v.v.), Evertag phải tải tệp đã chỉnh sửa lên lại. Bạn kiểm soát cách thực hiện:

- **Hiển thị thông báo xác nhận** *(mặc định, khuyến nghị)* — Evertag hỏi trước khi tải lên. Tốt nhất cho người dùng cẩn thận và thư viện chia sẻ.
- **Tự động cập nhật metadata của tệp** — tải lên im lặng sau mỗi lần chỉnh sửa. Tốt nhất cho người dùng đơn lẻ với kết nối nhanh, tin cậy và chỉnh sửa nhiều.
- **Không cập nhật metadata của tệp** — Evertag chỉ chỉnh sửa bản sao cục bộ. Hữu ích để xem trước thay đổi mà không đẩy lên đám mây.

### Chỉnh sửa tệp trực tuyến: dọn dẹp tệp cục bộ

Để chỉnh sửa tệp ở xa, Evertag tải nó về thiết bị trước. Sau khi chỉnh sửa, bạn chọn điều gì xảy ra với bản sao cục bộ đó:

- **Luôn xóa tệp đã tải về** — Evertag xóa tệp tạm thời sau khi chỉnh sửa. **Khuyến nghị** nếu bạn thiếu dung lượng hoặc làm việc với tệp của người khác.
- **Không xóa tệp đã tải về** — giữ tệp đã chỉnh sửa trên thiết bị. Hữu ích khi bạn muốn cả bản sao ngoại tuyến lẫn bản sao đám mây đã cập nhật.

### Nút trên màn hình chính

Màn hình chính của trình chỉnh sửa thẻ Evertag có thể hiện hoặc ẩn các nút cho từng thao tác. Chỉ bật những nút bạn thực sự sử dụng để giao diện được tập trung:

- **Tự động tìm thẻ âm thanh** — tìm metadata còn thiếu trực tuyến dựa trên dấu vân tay âm thanh của tệp.
- **Tìm thẻ âm thanh thủ công** — tìm theo tiêu đề/nghệ sĩ khi tìm tự động sai.
- **Tìm ảnh bìa album** — tìm và nhúng ảnh bìa chất lượng cao.
- **Lưu ảnh bìa album** — xuất ảnh bìa được nhúng vào thư viện ảnh hoặc tệp của bạn.
- **Chuẩn hóa mã hóa** — sửa văn bản không phải Latin bị lỗi do mã hóa cũ (rất hữu ích cho các bản nhạc Cyrillic, Trung, Nhật được rip bởi phần mềm cũ).
- **Xóa thẻ âm thanh** — xóa toàn bộ thẻ khỏi tệp. Hữu ích trước khi gắn thẻ lại sạch sẽ.

### Hiển thị thẻ mở rộng

Bật cái này để hiển thị toàn bộ trường metadata ngoài tiêu đề/nghệ sĩ/album/năm cơ bản — bao gồm BPM, người chỉ huy, nghệ sĩ gốc, tâm trạng, bản quyền, bộ mã hóa, ghi chú, lời và nhiều hơn nữa. Tính năng cho người dùng nâng cao; phần lớn người dùng phổ thông không cần.

### Chỉnh sửa tệp đồng thời

Khi bật, Evertag cho phép bạn chỉnh sửa metadata trên **nhiều tệp được chọn cùng lúc** — đặt cùng một album artist, năm hay thể loại cho cả album trong một thao tác. Đây là cách nhanh nhất để dọn một thư viện lớn lộn xộn.

## Chỉnh sửa thẻ cho Spotify, Apple Music và các nền tảng phát trực tuyến

Một câu hỏi phổ biến: «tôi đã chỉnh sửa thẻ trong Evertag, tải tệp lên, nhưng dịch vụ phát trực tuyến hiển thị metadata sai. Vì sao vậy?»

Câu trả lời ngắn: **các dịch vụ phát trực tuyến không phải lúc nào cũng tôn trọng thẻ cục bộ của bạn.** Apple Music và Spotify có cơ sở dữ liệu nội bộ riêng — khi nhận diện một bản nhạc, họ ghi đè metadata hiển thị bằng dữ liệu của họ. Nhưng đối với **tệp đã tải lên**, các tệp cục bộ của bạn (tính năng «Library» của Apple Music, Spotify Local Files), và **các bản tải lên của nhà phân phối lên các nền tảng phát trực tuyến**, thẻ của bạn hoàn toàn quan trọng. Cách thiết lập Evertag cho từng tình huống:

### Chuẩn bị tệp cho Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music xử lý UTF-8 đúng đắn.
- **Ảnh bìa album: Lớn** — các ứng dụng của Apple hiển thị ảnh bìa lớn rất tốt; Gốc là quá mức.
- **Sao chép thẻ: OFF** — không cần.
- Đảm bảo **Album Artist** được điền đúng — Apple Music dùng để nhóm.

### Chuẩn bị tệp cho Spotify Local Files

Spotify Local Files chỉ hiển thị các tệp được gắn thẻ tốt. Các thẻ Spotify đọc bị giới hạn.

- Phần lớn trường hợp **ID3v2.4: ON**. Nếu một bản nhạc không xuất hiện đúng trong Spotify sau khi chỉnh sửa, **hãy thử lưu với ID3v2.4: OFF** (tức là ID3v2.3) — bộ phân tích cú pháp của Spotify trong lịch sử khá thận trọng với v2.4.
- **Ảnh bìa album: Trung bình hoặc Lớn** — Spotify dù sao cũng thu nhỏ ảnh bìa.
- Điền tối thiểu **Tiêu đề**, **Nghệ sĩ**, **Album** và **Số bản nhạc**.

### Chuẩn bị tệp cho việc tải lên qua nhà phân phối (DistroKid, TuneCore, CD Baby, v.v.)

Nếu bạn là nghệ sĩ tải tác phẩm của mình lên các nền tảng phát trực tuyến, nhà phân phối thường đọc thẻ nhưng cũng yêu cầu metadata trong giao diện của họ. Bằng cách nào đi nữa:

- **ID3v2.3** thường là mặc định an toàn hơn — nhiều quy trình của nhà phân phối được xây dựng nhiều năm trước và ưu tiên định dạng cũ.
- Nhúng ảnh bìa **Lớn** (hầu hết nhà phân phối yêu cầu ảnh bìa ≥ 1.400 × 1.400 px — kiểm tra hướng dẫn của họ).
- Đừng dựa vào thẻ mở rộng — nhà phân phối chỉ đọc các trường cốt lõi.

### Chuẩn bị tệp cho Plex, Jellyfin, Navidrome, Subsonic, Emby

Các máy chủ media tự host này rất khoan dung. Chúng đọc cả v2.3 và v2.4 sạch sẽ và xử lý UTF-8 tốt.

- **ID3v2.4: ON** đều ổn.
- **Ảnh bìa album: Lớn** hoặc **Rất lớn** — các máy chủ này phục vụ ảnh bìa cho các client di động và màn hình CarPlay, nên chất lượng quan trọng.
- **Album Artist** được khuyến nghị mạnh — đó là điều Plex/Jellyfin dùng để nhóm album theo nghệ sĩ chính xác.

### Chuẩn bị tệp cho dàn âm thanh ô tô và phần cứng cũ hơn

- **ID3v2.4: OFF** (dùng ID3v2.3) — đầu phát cũ thường không hỗ trợ v2.4.
- **Ảnh bìa album: Trung bình** — nhiều màn hình ô tô bị nghẹn với ảnh bìa nhúng lớn.
- **Sao chép thẻ: ON** — dàn âm thanh ô tô cũ đôi khi chỉ đọc dự phòng ID3v1.

## Cải tiến khác

### Thiết kế Liquid Glass

Giao diện của Evertag 4.2 được tinh chỉnh cho vật liệu **Liquid Glass** mới của Apple trên toàn ứng dụng — bề mặt bán trong, hoạt ảnh mượt mà hơn và các điều khiển tinh tế hòa hợp tự nhiên với iOS, iPadOS và macOS.

### Thư viện kết nối được cập nhật

Chúng tôi đã làm mới các thư viện nội bộ mà Evertag dùng để giao tiếp với **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** và các dịch vụ khác. Tóm lại: ít lỗi kết nối ở các trường hợp hiếm, hỗ trợ tốt hơn cho các phiên bản máy chủ mới, và độ tin cậy cao hơn khi chỉnh sửa thẻ trên các tệp từ xa.

### Sửa lỗi dịch và bản địa hóa

Nhiều sửa đổi ngôn ngữ trong UI dựa trên phản hồi trực tiếp từ người dùng. Đặt văn bản trên các nút nhỏ tốt hơn ở một số ngôn ngữ.

### Những điều chỉnh nhỏ được truyền cảm hứng từ phản hồi của bạn

Nhiều cải tiến nhỏ dựa trên các đánh giá App Store và email gửi đến support@everappz.com. Chúng tôi đọc mọi tin nhắn.

## Tải Evertag 4.2

[**Tải Evertag từ App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) hoặc cập nhật từ App Store. Evertag là bản tải miễn phí với các nâng cấp trong ứng dụng tùy chọn cho các tính năng nâng cao. Các kết nối đám mây mới, giao thức mạng, cải tiến Wi-Fi Drive và giao diện Liquid Glass đều thuộc bản cập nhật cơ sở.

Nếu bạn yêu thích ứng dụng, vui lòng để lại đánh giá trên App Store — điều đó thực sự giúp ích. Có phản hồi hay gặp sự cố? Email cho chúng tôi tại **support@everappz.com**. Chúng tôi đọc mọi tin nhắn.

## Câu hỏi thường gặp

{{% details title="Có gì mới trong Evertag 4.2?" closed="true" %}}
Evertag 4.2 thêm hơn 6 kết nối đám mây và máy chủ mới (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), Wi-Fi Drive được làm mới với chế độ chọn nhiều và hàng đợi tải lên thông minh hơn, các cập nhật giao diện Liquid Glass, các thư viện kết nối được cập nhật, các bản sửa lỗi quan trọng trong chỉnh sửa thẻ và các cải tiến về bản dịch.
{{% /details %}}

{{% details title="Trong Evertag nên dùng ID3v2.4 hay ID3v2.3?" closed="true" %}}
Dùng **ID3v2.4** cho các trình phát hiện đại (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, các ứng dụng Android hiện đại) và cho các thư viện chứa ký tự không phải Latin — hỗ trợ UTF-8 đồng nghĩa thẻ tiếng Trung, Hàn, Nhật, Nga, Ả Rập và Do Thái sạch sẽ hơn. Dùng **ID3v2.3** nếu thẻ của bạn hiển thị sai trong một số ứng dụng, nếu bạn nhắm tới dàn âm thanh ô tô cũ hơn, hoặc nếu một quy trình của nhà phân phối phát trực tuyến từ chối v2.4. Bạn luôn có thể chuyển và lưu lại.
{{% /details %}}

{{% details title="Vì sao thẻ của tôi sai trong Spotify sau khi chỉnh sửa?" closed="true" %}}
Spotify chủ yếu hiển thị metadata từ danh mục riêng của họ — thẻ cục bộ của bạn chỉ được dùng cho «Local Files» hoặc nội dung bạn đã tải lên với tư cách nghệ sĩ. Nếu bạn gắn thẻ tệp cho Spotify Local Files mà chúng không hiển thị đúng, hãy thử tắt ID3v2.4 trong Evertag và lưu dưới dạng ID3v2.3 — bộ phân tích cú pháp của Spotify trong lịch sử thận trọng với v2.4.
{{% /details %}}

{{% details title="Trong Evertag nên chọn kích thước ảnh bìa album nào?" closed="true" %}}
Với hầu hết người dùng: **Lớn**. Trông tuyệt trên điện thoại, iPad, Mac và màn hình ô tô hiện đại mà không làm phình các tệp quá nhiều. Dùng **Trung bình** nếu thư viện rất lớn và bạn muốn tiết kiệm dung lượng. Chỉ dùng **Gốc** (không co giãn) cho master lưu trữ hoặc khi bạn thật sự cần chất lượng tối đa — nhưng lưu ý rằng một số trình phát cũ có thể gặp khó khăn với ảnh bìa nhúng rất lớn. **Gốc** thuộc bản nâng cấp tùy chỉnh cao cấp của Evertag.
{{% /details %}}

{{% details title="Ảnh bìa lớn hơn có làm tệp của tôi to hơn không?" closed="true" %}}
Có. Nhúng ảnh bìa 3.000 × 3.000 px có thể thêm vài megabyte cho một tệp âm thanh duy nhất. Trên thư viện 1.000 bản, con số đó lên tới gigabyte. Nếu hạn chế dung lượng, dùng Trung bình hoặc Lớn; nếu bạn phát từ NAS không quan tâm kích thước, Rất lớn hoặc Gốc cũng được.
{{% /details %}}

{{% details title="Sao chép thẻ là gì và có nên bật không?" closed="true" %}}
Sao chép thẻ ghi metadata cốt lõi vào cả ID3v1 (di sản 128 byte) và ID3v2 (hiện đại) của tệp. Chỉ bật nếu bạn nhắm tới các trình phát rất cũ hoặc phần cứng đọc ID3v1. Với mọi thiết bị hiện đại (smartphone, máy tính, dàn âm thanh ô tô đời mới), hãy để tắt.
{{% /details %}}

{{% details title="Evertag có chỉnh sửa thẻ trực tiếp trên tệp đám mây không?" closed="true" %}}
Có. Kết nối tới đám mây của bạn (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, v.v.) hoặc qua FTP/SFTP/NFS, mở một tệp và chỉnh sửa thẻ như thể nó là cục bộ. Evertag tải tệp về, áp dụng các chỉnh sửa của bạn, rồi tải bản đã cập nhật lên lại. Bạn có thể chọn giữa các chế độ «Luôn hỏi», «Tự động tải lên» hoặc «Không tải lên» trong cài đặt.
{{% /details %}}

{{% details title="Có thể chỉnh sửa thẻ FLAC trên iPhone bằng Evertag không?" closed="true" %}}
Có. Evertag hỗ trợ FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE và các định dạng quan trọng khác với hỗ trợ đầy đủ đọc/ghi thẻ, bao gồm ảnh bìa nhúng.
{{% /details %}}

{{% details title="Làm thế nào để chỉnh sửa thẻ an toàn trên máy chủ tại nhà bằng SFTP?" closed="true" %}}
Mở Evertag, vào Connections, chọn SFTP và nhập tên máy chủ hoặc IP, cổng (thường là 22), tên người dùng và mật khẩu hoặc khóa SSH riêng. Evertag sẽ duyệt các thư mục từ xa của bạn và chỉnh sửa thẻ trực tiếp với mã hóa đầu cuối qua SSH.
{{% /details %}}

{{% details title="Có thể chỉnh sửa thẻ cùng lúc trên nhiều tệp không?" closed="true" %}}
Có. Bật **Chỉnh sửa tệp đồng thời** trong cài đặt. Chọn nhiều tệp, mở trình chỉnh sửa thẻ và bất kỳ trường nào bạn thay đổi sẽ áp dụng cho tất cả các tệp đã chọn. Đây là cách nhanh nhất để đặt cùng một album artist, năm hoặc thể loại cho toàn bộ album.
{{% /details %}}

{{% details title="Cập nhật lên Evertag 4.2 có miễn phí không?" closed="true" %}}
Có. Evertag là bản tải miễn phí từ App Store, và 4.2 là bản cập nhật miễn phí cho mọi người dùng hiện có. Các tích hợp đám mây mới, cải tiến Wi-Fi Drive và giao diện Liquid Glass đều thuộc bản cập nhật cơ sở.
{{% /details %}}

{{% details title="Evertag 4.2 có sẵn trên thiết bị nào?" closed="true" %}}
Evertag 4.2 chạy trên iPhone, iPad và Mac. Đồng bộ iCloud Drive giữ cho cài đặt trình chỉnh sửa thẻ của bạn nhất quán giữa các thiết bị.
{{% /details %}}
