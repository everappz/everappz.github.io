---
title: "Cách lấy metadata, biểu tượng và ảnh chụp màn hình App Store miễn phí"
date: 2026-06-13
description: "Hướng dẫn từng bước để lấy metadata, biểu tượng, ảnh chụp màn hình và thông tin App Store đã bản địa hoá của bất kỳ ứng dụng iOS nào bằng AppLookup.pro, công cụ trình duyệt miễn phí dựa trên iTunes Search API chính thức."
keywords: [
  "metadata App Store", "lấy dữ liệu App Store", "tải biểu tượng App Store",
  "tải ảnh chụp màn hình App Store", "công cụ tra cứu App Store", "iTunes Search API",
  "trích xuất metadata ứng dụng", "metadata ứng dụng iOS", "công cụ App Store API miễn phí",
  "tải biểu tượng ứng dụng độ phân giải cao", "nghiên cứu đối thủ App Store",
  "dữ liệu App Store bản địa hoá", "tra cứu App Store theo quốc gia", "công cụ nghiên cứu ASO miễn phí"
]
tags: [
  "Metadata App Store", "App Lookup", "iTunes Search API",
  "Tải biểu tượng ứng dụng", "Ảnh chụp màn hình ứng dụng", "Nghiên cứu ASO"
]
sidebar:
  exclude: true
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-cofounder-everappz.webp"
---

{{< author-byline >}}

## Lấy dữ liệu App Store trong vài giây

**Tóm tắt:** [AppLookup.pro](https://applookup.pro) là công cụ miễn phí cho phép lấy dữ liệu công khai của bất kỳ ứng dụng iOS, iPadOS, macOS hoặc tvOS nào. Bạn nhận được tiêu đề, mô tả, có gì mới, phiên bản, giá, đánh giá, biểu tượng ứng dụng, ảnh chụp màn hình, thiết bị được hỗ trợ và phản hồi gốc của iTunes API. Mỗi trường đều có nút sao chép một chạm. Mở trang web, dán liên kết App Store hoặc nhập tên ứng dụng là bạn có dữ liệu.

Dùng để:

- **Nghiên cứu ASO.** Xem cách các ứng dụng hàng đầu viết tiêu đề, phụ đề, mô tả và từ khoá.
- **Theo dõi đối thủ.** Kiểm tra cập nhật phiên bản, đánh giá và giá ở các thị trường.
- **Tải tài nguyên.** Lưu biểu tượng ứng dụng chính thức và ảnh chụp màn hình kích thước đầy đủ trong một file ZIP.
- **Kiểm tra bản địa hoá.** So sánh mô tả, có gì mới và ảnh chụp màn hình trên hơn 40 quốc gia App Store.
- **Kiểm tra API.** Sao chép JSON gốc của iTunes Search API thẳng vào code hoặc Postman.

## AppLookup.pro là gì?

[AppLookup.pro](https://applookup.pro) là công cụ tra cứu App Store miễn phí, chạy trên trình duyệt. Nó chạy hoàn toàn trên thiết bị của bạn. Mọi kết quả đều đến trực tiếp từ [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) chính thức của Apple. Không scrape. Không đăng ký. Không theo dõi.

### Những gì bạn nhận được

- **Tìm kiếm theo tên ứng dụng hoặc URL App Store.** Tính năng tự động hoàn thành hiển thị kết quả trực tiếp khi bạn nhập.
- **Hơn 40 cửa hàng quốc gia.** Chuyển đổi giữa Mỹ, Anh, Nhật, Đức, Pháp, Brazil và nhiều quốc gia khác.
- **Đầy đủ metadata.** Tiêu đề, phụ đề, nhà phát triển, Bundle ID, phiên bản, giá, dung lượng tệp, đánh giá, ngày phát hành, phân loại nội dung, ngôn ngữ và thiết bị được hỗ trợ.
- **Tài nguyên độ phân giải cao.** Biểu tượng và ảnh chụp màn hình ứng dụng cho iPhone, iPad, macOS và Apple TV.
- **Tải xuống ZIP hàng loạt.** Lấy mọi biểu tượng hoặc mọi ảnh chụp màn hình trong một file lưu trữ.
- **JSON gốc của iTunes API.** Phản hồi chính xác từ Apple, sẵn sàng để sao chép.
- **Nút sao chép trên mọi trường.** Một chạm sẽ đưa giá trị vào clipboard.

## Cách dùng AppLookup.pro từng bước

### Bước 1. Nhập tên ứng dụng hoặc dán URL App Store

Mở [applookup.pro](https://applookup.pro) và bắt đầu nhập tên ứng dụng. Tính năng tự động hoàn thành sẽ hiển thị kết quả App Store trực tiếp khi bạn nhập.

Bạn cũng có thể dán liên kết App Store trực tiếp như `https://apps.apple.com/us/app/instagram/id389801252` hoặc chỉ ID ứng dụng. Công cụ sẽ trích xuất ID giúp bạn. Nó cũng xử lý cả URL chuyển hướng của Google.

![Nhập tên ứng dụng hoặc URL App Store vào AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/1-app-store-lookup-enter-app-name.webp)

### Bước 2. Lấy thông tin ứng dụng và tải biểu tượng

Nhấn **Lookup** hoặc nhấn Enter. Công cụ sẽ gọi iTunes Search API chính thức và hiển thị biểu tượng ứng dụng, tên nhà phát triển, đánh giá, phiên bản và giá trong chưa đến một giây.

Cuộn đến phần **App Icon**. Mỗi kích thước biểu tượng mà Apple trả về sẽ xuất hiện dưới dạng một thẻ. Mỗi thẻ có:

- **Direct Link.** Mở ảnh kích thước đầy đủ trong tab mới.
- **Download.** Lưu tệp vào máy tính của bạn.

Dùng **Download All Icons (ZIP)** để lấy mọi kích thước biểu tượng trong một file lưu trữ. Tương tự với ảnh chụp màn hình: mỗi phần nền tảng đều có nút **Download All (ZIP)** riêng.

![Tải biểu tượng và ảnh chụp màn hình ứng dụng từ AppLookup.pro](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/2-app-store-lookup-view-app-details-icons.webp)

### Bước 3. Đọc thông tin chi tiết ứng dụng và sao chép bất kỳ trường nào

Cuộn đến **App Details**. Bạn sẽ thấy Bundle ID, phiên bản, giá, dung lượng tệp, OS tối thiểu, ngày phát hành, ngày cập nhật cuối, phân loại nội dung, thể loại, ID thể loại, ngôn ngữ, người bán, ID nghệ sĩ và ID track.

Chạm vào nút **Copy** trên bất kỳ thẻ nào. Giá trị sẽ vào clipboard và nút sẽ hiển thị dấu tích «Copied» màu xanh.

Tương tự với **Description**, **What's New** và **Supported Devices**. Các phần này có thể cuộn được, vì vậy bạn có thể đọc toàn bộ văn bản mà không mất vị trí, và nút Copy sẽ đưa toàn bộ trường vào clipboard.

![Xem thông tin App Store đầy đủ và sao chép bất kỳ trường nào chỉ với một chạm](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/3-app-store-lookup-view-app-details.webp)

### Bước 4. Xem phản hồi gốc của App Store API

Cần đúng JSON mà Apple trả về? Cuộn đến **Raw API Response**. Toàn bộ payload của iTunes Search API được hiển thị trong trình xem có thể cuộn với nút **Copy** ở trên cùng. Một chạm sẽ sao chép toàn bộ đối tượng JSON.

**iTunes Lookup URL** được hiển thị ngay phía trên. Dán nó vào Postman, curl hoặc trình duyệt của bạn để phát lại cùng một yêu cầu.

![Xem và sao chép phản hồi JSON gốc của iTunes Search API](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/4-app-store-lookup-view-app-raw-api-response.webp)

### Bước 5. Đổi quốc gia để xem phiên bản bản địa hoá

Metadata App Store thay đổi theo từng quốc gia. Cùng một ứng dụng thường có tiêu đề, phụ đề, mô tả, ảnh chụp màn hình và giá khác nhau ở mỗi thị trường.

Chọn quốc gia từ menu thả xuống ở trên cùng. URL trong ô nhập sẽ tự động cập nhật. Nhấn **Lookup** lần nữa để lấy lại ứng dụng ở thị trường đó.

Đây là cách nhanh nhất để xem đối thủ cạnh tranh giới thiệu ứng dụng của họ ở Nhật, Đức, Brazil hoặc bất kỳ trong số hơn 40 quốc gia được hỗ trợ như thế nào.

![Chuyển cửa hàng quốc gia để xem metadata App Store đã bản địa hoá](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/5-app-store-lookup-change-app-country.webp)

### Bước 6. Sao chép metadata bản địa hoá

Sau khi kết quả của quốc gia được tải, mọi trường đều hoạt động theo cùng cách. Chạm **Copy** trên mô tả, có gì mới, tên ứng dụng, nhà phát triển, Bundle ID hoặc bất kỳ thẻ chi tiết nào để chụp lại văn bản đã bản địa hoá.

Điều này giúp dễ dàng tạo bảng tính so sánh song song hoặc đưa nội dung đã bản địa hoá vào quy trình đánh giá bản dịch.

![Sao chép mô tả và metadata App Store đã bản địa hoá chỉ với một chạm](/blog/how-to-fetch-app-store-metadata-icons-and-screenshots/6-app-store-lookup-copy-localized-app-description.webp)

## Ai sử dụng AppLookup.pro

- **Nhà phát triển indie** làm nghiên cứu ASO trước khi ra mắt.
- **Đội ASO và marketing** theo dõi cập nhật và giá của đối thủ.
- **Nhà thiết kế** lấy biểu tượng ứng dụng và ảnh chụp màn hình chính thức độ phân giải cao cho bộ press kit và case study.
- **Đội bản địa hoá** kiểm tra những thị trường nào đã được phủ và nơi nào vẫn còn dùng nội dung tiếng Anh mặc định.
- **Kỹ sư backend và QA** kiểm thử tích hợp iTunes Search API mà không cần viết scraper.
- **Người viết và blogger** cần biểu tượng ứng dụng chính thức và vài ảnh chụp màn hình cho bài đăng.

## Quyền riêng tư và miễn trừ trách nhiệm

AppLookup.pro chạy trong trình duyệt của bạn. Không đăng nhập. Không theo dõi. Không có ghi log máy chủ về các ứng dụng bạn tra cứu. Các yêu cầu được gửi trực tiếp từ trình duyệt của bạn đến [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) của Apple.

Công cụ này chỉ dành cho **mục đích giáo dục và nghiên cứu**. Mọi dữ liệu được lấy từ API công khai chính thức của Apple và vẫn thuộc sở hữu của Apple Inc. và các nhà phát hành ứng dụng được liệt kê. Việc sử dụng công cụ này tuân theo [Điều khoản và Điều kiện Dịch vụ Truyền thông của Apple](https://www.apple.com/legal/internet-services/terms/site.html). Vui lòng tôn trọng giới hạn tốc độ của Apple và không phân phối lại các tài nguyên có bản quyền.

## Dùng thử ngay

Bạn không cần khoá API, tài khoản nhà phát triển hay gói trả phí để kiểm tra dữ liệu App Store. Mở [applookup.pro](https://applookup.pro), dán bất kỳ URL App Store nào, và bạn sẽ có metadata, biểu tượng và JSON gốc trong vài giây.

## Mã nguồn mở

AppLookup.pro là mã nguồn mở. Hoan nghênh báo cáo lỗi, bổ sung quốc gia và pull request.

{{< cards cols="1" >}}
  {{< card link="https://github.com/everappz/AppStoreLookup" title="AppLookup.pro trên GitHub" icon="github" tag="mã nguồn mở" >}}
{{< /cards >}}

---

## Câu hỏi thường gặp

{{% details title="AppLookup.pro thực sự miễn phí?" closed="true" %}}
Đúng vậy. AppLookup.pro là 100% miễn phí và mã nguồn mở. Nó chạy trong trình duyệt của bạn. Không đăng ký, không gói trả phí và không có giới hạn sử dụng nào khác ngoài giới hạn của chính iTunes Search API của Apple.
{{% /details %}}

{{% details title="Dữ liệu đến từ đâu?" closed="true" %}}
Mọi kết quả được lấy theo thời gian thực từ [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html) chính thức của Apple. Công cụ không scrape các trang App Store và không cache phản hồi trên bất kỳ máy chủ nào.
{{% /details %}}

{{% details title="Tôi có thể tải biểu tượng ứng dụng ở độ phân giải cao không?" closed="true" %}}
Có. Phần **App Icon** hiển thị mọi URL biểu tượng mà Apple trả về. Mỗi thẻ có nút Direct Link và Download, và nút Download All Icons ZIP đóng gói chúng trong một file lưu trữ.
{{% /details %}}

{{% details title="Tôi có thể tải tất cả ảnh chụp màn hình App Store cùng lúc không?" closed="true" %}}
Có. Mỗi phần ảnh chụp màn hình (iPhone, iPad, macOS và Apple TV) đều có nút **Download All (ZIP)** đóng gói mọi ảnh chụp màn hình ở độ phân giải đầy đủ.
{{% /details %}}

{{% details title="Làm thế nào để xem ứng dụng trông như thế nào ở quốc gia khác?" closed="true" %}}
Chọn một quốc gia trong menu thả xuống ở đầu trang. Hơn 40 cửa hàng quốc gia được hỗ trợ. Nhấn **Lookup** lần nữa và công cụ sẽ lấy lại ứng dụng cho quốc gia đó, hiển thị tiêu đề, mô tả, ảnh chụp màn hình, có gì mới và giá đã được bản địa hoá.
{{% /details %}}

{{% details title="Tôi có thể sao chép từng trường riêng lẻ như Bundle ID hoặc ngày phát hành không?" closed="true" %}}
Có. Mọi trường văn bản trong kết quả đều có nút Copy riêng: tên ứng dụng, nhà phát triển, mô tả, có gì mới, Bundle ID, phiên bản, giá, dung lượng tệp, OS tối thiểu, ngày phát hành, phân loại nội dung, ngôn ngữ, thiết bị được hỗ trợ và JSON gốc.
{{% /details %}}

{{% details title="AppLookup.pro có hoạt động với mọi ứng dụng iOS không?" closed="true" %}}
Nó hoạt động với bất kỳ ứng dụng nào được niêm yết công khai ở ít nhất một quốc gia App Store và được iTunes Search API trả về. Các ứng dụng chưa niêm yết, đã gỡ hoặc phân phối doanh nghiệp sẽ không xuất hiện.
{{% /details %}}

{{% details title="Có hỗ trợ ứng dụng macOS và Apple TV không?" closed="true" %}}
Có. Nếu ứng dụng có ảnh chụp màn hình macOS hoặc Apple TV trong phản hồi của iTunes Search API, AppLookup.pro sẽ hiển thị chúng trong bảng có thể cuộn riêng với các nút tải xuống.
{{% /details %}}

{{% details title="Tôi có thể dùng JSON gốc trong code của mình không?" closed="true" %}}
Có. Phần Raw API Response hiển thị đúng JSON mà Apple trả về. Sao chép nó vào Postman, unit test hoặc pipeline backend. Vui lòng tôn trọng điều khoản API của Apple và giới hạn tốc độ hợp lý.
{{% /details %}}

{{% details title="Có an toàn khi dán URL App Store vào công cụ không?" closed="true" %}}
Có. URL được phân tích trong trình duyệt của bạn. Cuộc gọi mạng đi duy nhất là truy vấn đến iTunes Search API của Apple.
{{% /details %}}

{{% details title="Sự khác biệt giữa AppLookup.pro và AppKeywords.pro là gì?" closed="true" %}}
[AppLookup.pro](https://applookup.pro) dùng để đọc metadata App Store của bất kỳ ứng dụng đã phát hành nào: nghiên cứu đối thủ, tải tài nguyên, kiểm tra bản địa hoá. [AppKeywords.pro](https://appkeywords.pro) dùng để viết metadata App Store cho ứng dụng của riêng bạn: tối ưu tiêu đề, phụ đề và từ khoá với hỗ trợ Fastlane. Hai công cụ này phối hợp rất tốt với nhau.
{{% /details %}}
