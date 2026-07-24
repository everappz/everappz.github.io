---
title: "Cách sử dụng Hiệu ứng âm thanh và DSP trong Flacbox: Compressor, Freeverb, Crossfeed, Echo, Chuẩn hóa âm lượng và nhiều hơn nữa"
date: 2026-07-24
description: "Hướng dẫn đầy đủ về âm thanh Flacbox trên iPhone, iPad và Mac. Tìm hiểu cách hoạt động của công cụ BASS, nó phát thêm những định dạng nào (bao gồm nhạc MOD, nhạc tracker và DSD), và chính xác từng hiệu ứng, từng thanh trượt và từng cài đặt sẵn làm gì với âm thanh của bạn, cùng bộ chỉnh âm 10 dải và chuỗi DSP tùy chỉnh."
keywords: ["hiệu ứng âm thanh Flacbox", "giải thích cài đặt sẵn Flacbox", "công cụ BASS Flacbox", "thư viện âm thanh BASS iOS", "trình phát nhạc MOD iPhone", "trình phát nhạc tracker iOS", "phát MOD XM IT S3M iPhone", "trình phát DSD iOS", "trình phát FLAC iPhone", "trình phát nhạc lossless iOS", "cài đặt sẵn bộ chỉnh âm Flacbox", "bộ chỉnh âm 10 dải iPhone", "chuẩn hóa âm lượng iPhone", "EBU R128 iOS", "chuẩn hóa độ ồn trình phát nhạc", "crossfeed tai nghe iOS", "bs2b crossfeed", "cài đặt sẵn compressor trình phát nhạc", "freeverb reverb iOS", "echo delay trình phát nhạc", "chuỗi DSP trình phát nhạc", "tăng bass iPhone", "cách thêm hiệu ứng vào nhạc Flacbox", "cài đặt bộ chỉnh âm tốt nhất iPhone"]
tags: ["Flacbox", "Hiệu ứng âm thanh", "Hướng dẫn", "BASS", "Bộ chỉnh âm", "Tăng Bass", "Compressor", "Freeverb", "Crossfeed", "Echo", "Chuẩn hóa âm lượng", "EBU R128", "Nhạc MOD", "Nhạc Tracker", "DSD", "FLAC", "DSP", "Tai nghe", "Cài đặt sẵn"]
readingTime: 30
---

{{< author-byline >}}

{{< full-width-tables >}}

**Câu trả lời ngắn gọn:** Trong Flacbox bạn chọn một **Công cụ phát** trong **Cài đặt > Trình phát âm thanh**: **Standard** (công cụ hệ thống của Apple), **Universal** (công cụ FFmpeg), hoặc **Sound FX** (**công cụ BASS™**). Công cụ bạn chọn quyết định định dạng tệp nào phát được, nên lựa chọn này rất quan trọng. Công cụ **Sound FX** phát thêm những định dạng mà hầu hết ứng dụng iPhone bỏ qua (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, và nhạc **MOD và tracker** cũ như MOD, XM, IT và S3M), và đây là công cụ duy nhất cung cấp các công cụ âm thanh: **bộ chỉnh âm 10 dải**, **Chuẩn hóa âm lượng**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distortion**, **Rotate**, **Crossfeed**, và một **chuỗi DSP** tự dựng. Vậy nên để dùng các hiệu ứng trong hướng dẫn này, hãy đặt Công cụ phát của bạn thành **Sound FX** trước. Mỗi công cụ đều có sẵn các **cài đặt sẵn**. Mở chúng trong **Cài đặt > Trình phát âm thanh** (Hiệu ứng âm thanh, Bộ chỉnh âm, Xử lý tín hiệu), hoặc chạm nút **⋯ (Thêm)** trên trình phát và chọn **Hiệu ứng âm thanh**. Không có thao tác nào ở đây làm thay đổi tệp của bạn.

> Phần giải thích thanh trượt và cài đặt sẵn dưới đây chính là những mô tả ngắn mà Flacbox hiển thị cho bạn trong ứng dụng, kết hợp thêm một chút bối cảnh để bạn có bức tranh đầy đủ trước khi chạm.

## Cách đọc hướng dẫn này

Mọi công cụ đều hoạt động theo cùng một cách:

1. **Bật nó lên.** Mỗi hiệu ứng có công tắc bật/tắt riêng. Ban đầu tất cả đều tắt. Bạn có thể bật bao nhiêu tùy thích cùng lúc.
2. **Chọn một cài đặt sẵn.** Cài đặt sẵn là một thiết lập có sẵn. Chạm vào một cái và âm thanh thay đổi ngay lập tức. Hướng dẫn này liệt kê **mọi** cài đặt sẵn làm gì.
3. **Tinh chỉnh (tùy chọn).** Mở các thanh trượt để điều chỉnh bằng tay. Ngay khi bạn di chuyển một thanh trượt, hiệu ứng hiển thị **Manual**, để bạn biết mình đã rời khỏi cài đặt sẵn. Mỗi thanh trượt đều có nút đặt lại.

Không có gì được lưu vào tệp của bạn. Đây là các hiệu ứng trực tiếp. Tắt một hiệu ứng và âm thanh gốc của bạn trở lại ngay lập tức.

## Chọn Công cụ phát của bạn (Sound FX có các hiệu ứng)

Flacbox không trộn lẫn các công cụ với nhau. Bạn chọn **một** trong **Cài đặt > Trình phát âm thanh > Công cụ phát**, và công cụ bạn chọn quyết định định dạng tệp nào bạn phát được và liệu các hiệu ứng có khả dụng hay không. Có ba lựa chọn, hiển thị trong ứng dụng với những tên chính xác sau:

1. **Standard.** Công cụ hệ thống tích hợp của Apple. Dùng giải mã phần cứng để tiết kiệm pin hơn.
2. **Universal.** Công cụ FFmpeg, mở được một loạt định dạng rất rộng.
3. **Sound FX.** **Công cụ BASS™**. Nó phát các tệp lossless và độ phân giải cao với độ chính xác đầy đủ, thêm nhạc module (tracker), và cung cấp mọi hiệu ứng, bộ chỉnh âm 10 dải và chuỗi DSP trong hướng dẫn này.

Vì mỗi công cụ hỗ trợ một tập định dạng riêng, những tệp bạn phát được sẽ thay đổi theo công cụ bạn chọn. Quan trọng hơn, các hiệu ứng, bộ chỉnh âm và chuỗi DSP chỉ hoạt động **với** công cụ **Sound FX**, nên hãy chọn nó trước nếu bạn muốn dùng chúng.

Sound FX được xây dựng trên **BASS™**, một thư viện âm thanh chuyên nghiệp từ Un4seen Developments. Bạn có thể đọc thêm về nó trên trang chủ tại [un4seen.com](https://www.un4seen.com/).

## Định dạng nhạc: Công cụ Sound FX (BASS™) thêm những gì (Bao gồm nhạc MOD và Tracker)

Khi chọn công cụ **Sound FX (BASS™)**, Flacbox phát các định dạng chuyên biệt dưới đây, bên cạnh những định dạng thường ngày. Đặc biệt nhất là **nhạc module**, còn gọi là **nhạc tracker**. Một tệp module không phải là bản ghi âm thông thường. Nó chứa những âm nhạc cụ nhỏ cùng một «bản nhạc» chỉ dẫn cách phát chúng, và Flacbox dựng lại bài hát trực tiếp từ bản nhạc đó, đúng theo cách các tệp này được thiết kế để phát. Trình phát thông thường không làm được điều này.

| Loại nhạc | Định dạng | Nên biết |
|---|---|---|
| **Nhạc module / tracker** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Được dựng lại trực tiếp bởi trình phát module BASS™. Tuyệt vời cho chiptune và các bài demoscene hoặc Amiga cũ. |
| **Lossless hiện đại** | FLAC | Chất lượng đầy đủ, nhỏ hơn WAV. |
| **Lossless khác** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Các loại lossless ít phổ biến hơn, đều được hỗ trợ. |
| **DSD độ phân giải cao** | DSF, DFF | Phát trên phần cứng thông thường bằng DSD over PCM. |
| **Lossy hiện đại** | Opus, Ogg Vorbis, MP3 | Các loại phát trực tuyến và tải xuống thông thường. |

Công cụ Sound FX cũng phát các định dạng Apple phổ biến (AAC, ALAC, M4A, WAV, AIFF) và luồng trực tiếp, nên các hiệu ứng và bộ chỉnh âm cũng hoạt động trên những định dạng đó.

**Vì sao điều này hữu ích cho bạn:** nếu bạn có một tập hợp các album FLAC, các tệp DSD độ phân giải cao và một thư mục các bài tracker MOD hoặc XM cũ, Flacbox phát được tất cả, và bộ chỉnh âm cùng các hiệu ứng hoạt động trên mọi tệp trong số đó.

## Ba menu bạn sẽ dùng

Flacbox giữ các công cụ âm thanh của nó ở ba nơi, tất cả nằm trong cài đặt trình phát âm thanh. Trước tiên hãy đảm bảo **Công cụ phát** của bạn được đặt thành **Sound FX** (Cài đặt > Trình phát âm thanh > Công cụ phát), vì các hiệu ứng, bộ chỉnh âm và chuỗi DSP chỉ khả dụng với công cụ đó.

- **Hiệu ứng âm thanh** (giá hiệu ứng): mở trình phát, chạm **⋯ (Thêm)**, chạm **Hiệu ứng âm thanh**. Hoặc vào **Cài đặt > Trình phát âm thanh > Hiệu ứng âm thanh**.
- **Bộ chỉnh âm** (10 dải và các cài đặt sẵn): **Cài đặt > Trình phát âm thanh > Bộ chỉnh âm**.
- **Xử lý tín hiệu** (chuỗi DSP của riêng bạn): **Cài đặt > Trình phát âm thanh > Xử lý tín hiệu**.

Bạn cũng có thể đặt **tần số lấy mẫu đầu ra**, **kênh**, và **kích thước bộ đệm** trong **Cài đặt > Trình phát âm thanh**.

## Bộ chỉnh âm 10 dải

**Nó làm gì:** Thay đổi âm sắc của nhạc, từ bass sâu đến treble sáng. Đây là công cụ tốt nhất để **tăng bass** sạch sẽ hoặc làm phần cao sáng hơn, trong trẻo hơn. Hãy nghĩ về nó như mười núm âm lượng, mỗi núm cho một lát khác nhau của âm thanh. Nâng một dải để đưa phần đó ra trước, hạ nó xuống để kéo lùi lại. Những thay đổi nhỏ vài dB thường nghe hay nhất, và nó hoạt động trên mọi thứ bạn phát.

**Cách hoạt động:** Mười thanh trượt ở **32, 64, 125, 250, 500 Hz và 1, 2, 4, 8, 16 kHz**. Mỗi thanh chạy từ **-12 dB (cắt)** đến **+12 dB (tăng)**. Ngoài ra còn có **Preamplifier** từ **-24 đến +24 dB** cho mức tổng thể. Bạn có thể lưu các cài đặt sẵn của riêng mình và **xuất hoặc nhập** chúng giữa các thiết bị.

**Mỗi cài đặt sẵn tích hợp làm gì (22 cài đặt sẵn):**

| Cài đặt sẵn | Nó làm gì với âm thanh của bạn |
|---|---|
| **Flat** | Không thay đổi. Tất cả các dải ở mức không. Một điểm khởi đầu sạch sẽ. |
| **Acoustic** | Bass ấm và phần cao rõ ràng, hiện diện. Làm guitar acoustic và giọng hát cảm thấy tự nhiên và sống động. |
| **Bass Booster** | Nâng mạnh phần thấp, giữ nguyên phần trung và cao. Nhiều lực và sức nặng hơn. |
| **Bass Reducer** | Cắt phần thấp. Tiện cho phòng ù, tai nghe rẻ tiền, hoặc các bản nhạc nặng. |
| **Treble Booster** | Chỉ nâng phần cao. Thêm lấp lánh và độ thoáng, nhiều chi tiết hơn. |
| **Treble Reducer** | Làm mềm phần cao. Thuần hóa các bản ghi chói hoặc gắt. |
| **Classical** | Phần thấp đầy đặn và phần cao dịu với một chút hụt ở trung. Mượt mà và rộng rãi cho nhạc giao hưởng. |
| **Dance** | Phần thấp lớn và phần cao sáng với phần trung được múc lõm. Đầy lực và tràn năng lượng cho nhạc club. |
| **Deep** | Phần thấp ấm, dày với phần cao mềm hơn. Một âm thanh ấm cúng, thư thái. |
| **Electronic** | Bass mạnh và phần cao sáng cho synth và beat. Rộng và hiện đại. |
| **Hip-Hop** | Bass nặng và phần cao rõ với phần trung được kiểm soát. Nặng và đầy lực. |
| **Jazz** | Ấm và mượt, với một chút hụt ở trung. Nhẹ nhàng và tự nhiên cho nhạc jazz acoustic. |
| **Latin** | Phần thấp và cao được tăng với phần trung sạch. Sáng và sống động. |
| **Loudness** | Tăng mạnh bass và treble (đường cong «nụ cười»). Nghe đầy đặn hơn ở âm lượng thấp. |
| **Lounge** | Phần trung đưa ra trước với các cạnh mềm. Thư giãn và thân thiện với giọng hát. |
| **Piano** | Phần trung và cao rõ để các nốt piano vang lên trong trẻo. |
| **Pop** | Nâng phần trung cho giọng hát, kéo lùi phần thấp và cao. Giọng hát nổi lên phía trước. |
| **R&B** | Độ ấm phần thấp-trung rất mạnh và phần cao rõ. Mượt mà và phong phú. |
| **Rock** | Tăng phần thấp và cao cho guitar và trống. Tràn năng lượng và đầy đặn. |
| **Small Speakers** | Tăng phần thấp và cắt phần cao để giúp loa nhỏ nghe đầy đặn hơn. |
| **Spoken Word** | Nâng dải giọng nói và cắt bass sâu. Làm cho lời nói rõ ràng. |
| **Vocal Booster** | Đẩy phần giữa nơi giọng hát nằm, cắt xung quanh chúng. Giọng hát nổi bật. |

**Mẹo cho bass:** Bắt đầu với **Bass Booster**, sau đó, nếu nghe đục, hạ Preamplifier xuống 1 đến 2 dB để không có gì bị méo.

## Chuẩn hóa âm lượng (Độ ồn đồng đều)

**Nó làm gì:** Một số bài hát phát to hơn bài khác, nên bạn cứ phải chỉnh âm lượng liên tục. Tính năng này làm mọi bài phát ở khoảng cùng một mức âm lượng một cách tự động, nên bạn không phải làm. Nó hoàn hảo cho các danh sách phát ngẫu nhiên trộn lẫn bản ghi cũ và mới, các album khác nhau, hoặc các nguồn khác nhau, nơi một bản có thể to hơn nhiều so với bản kế tiếp.

**Cách hoạt động:** Nó lắng nghe độ ồn thực tế của mỗi bản bằng chuẩn **EBU R128** (đo bằng **LUFS**, cùng ý tưởng mà các dịch vụ phát trực tuyến sử dụng), sau đó điều chỉnh mỗi bản hướng về mục tiêu của bạn. Nó không cần thẻ nào trong tệp của bạn và không bao giờ thay đổi âm thanh. EBU R128 đo độ ồn mà tai bạn thực sự cảm nhận trên toàn bộ bài hát, không chỉ đỉnh cao nhất, đó là lý do nó khớp với mức độ to mà các bản nhạc thực sự nghe như thế nào với bạn. Flacbox tính toán điều này trực tiếp khi nhạc phát (và kiểm tra độ ồn trước khi có thể), rồi áp dụng một thay đổi âm lượng duy nhất, ổn định cho bản nhạc. Giới hạn **Max boost** ngăn các bản ghi rất nhỏ bị đẩy lên quá mạnh đến mức méo tiếng. Vì nó đọc chính âm thanh, nó hoạt động trên mọi nguồn, bao gồm tệp đám mây, luồng trực tiếp, và nhạc module, ngay cả khi các tệp hoàn toàn không có thẻ độ ồn.

**Thanh trượt:**

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Target loudness** | Đặt độ ồn mà mọi bản được cân bằng hướng tới. Giá trị cao hơn làm mọi thứ phát to hơn tổng thể. | -30 đến -6 LUFS (-16) |
| **Max boost** | Giới hạn mức khuếch đại của các bản nhỏ. Giá trị cao hơn đưa các bản ghi nhẹ gần mục tiêu hơn. | 0 đến 24 dB (12) |

**Cài đặt sẵn:**

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Light** | Cân bằng nhẹ nhàng cho nghe thông thường. Làm đều các bước nhảy âm lượng rõ ràng mà không đẩy các bản nhỏ mạnh. |
| **Standard** | Mặc định đa dụng. Một mục tiêu độ ồn kiểu phát trực tuyến phù hợp với hầu hết nhạc. Bắt đầu ở đây. |
| **Strong** | Khớp mạnh mẽ đẩy các bản nhỏ lên chắc chắn. Tốt nhất cho thư viện hỗn hợp có chênh lệch mức lớn. |
| **Night** | Một mục tiêu tổng thể yên tĩnh hơn nhưng vẫn nâng các đoạn nhẹ, để nghe khuya luôn nhất quán và nhỏ. |

## Compressor (Làm đều phần to và nhỏ)

**Nó làm gì:** Trong một bài hát, các phần nhỏ có thể quá khẽ và các phần to có thể quá to. Tính năng này đưa chúng lại gần nhau hơn, để cả bài dễ nghe, ngay cả trong xe hay nơi ồn ào. Nó nhẹ nhàng hạ những khoảnh khắc to nhất xuống và nâng những phần nhẹ hơn lên, để bạn thôi phải với tay chỉnh âm lượng trong một bản duy nhất. Điều này khác với Chuẩn hóa âm lượng: Compressor làm đều mọi thứ **bên trong** một bài hát, còn Chuẩn hóa âm lượng khớp độ ồn **giữa** các bài hát. Hai cái phối hợp tốt với nhau. Bắt đầu với một cài đặt sẵn, và chỉ mở các thanh trượt nếu bạn muốn kiểm soát nhiều hơn.

**Thanh trượt:**

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Threshold** | Mức mà quá trình nén bắt đầu. Giá trị thấp hơn ép nhiều âm thanh hơn, giữ phần nhỏ và to gần nhau hơn. | -60 đến 0 dB (-20) |
| **Ratio** | Mức độ mạnh mà phần to bị kìm lại khi vượt ngưỡng. Giá trị cao hơn nén mạnh hơn, giữ âm thanh đều hơn. | 1:1 đến 30:1 (4:1) |
| **Attack** | Hiệu ứng phản ứng nhanh thế nào với một đỉnh to đột ngột. Giá trị ngắn bắt được các transient; giá trị dài hơn để chúng lọt qua. | 0.1 đến 1000 ms (10 ms) |
| **Release** | Hiệu ứng buông ra nhanh thế nào sau khi phần to đi qua. Giá trị ngắn có thể gây bơm; giá trị dài hơn nghe mượt hơn. | 10 ms đến 5 s (100 ms) |
| **Master gain** | Tăng đầu ra cuối cùng áp dụng sau khi xử lý. Nâng cái này để tăng độ ồn tổng thể sau khi dải động đã được làm đều. | -30 đến +30 dB (0) |

**Cài đặt sẵn:**

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Transparent** | Lưới an toàn gần như vô hình. Giữ gần trọn dải động và chỉ bắt những đỉnh to nhất. |
| **Soft** | Cân bằng nhẹ cho nghe hi-fi tại nhà. Làm mượt tinh tế mà không ép nhạc. |
| **Standard** | Mặc định hợp lý cho phát nhạc thường ngày. Cài đặt sẵn đầu tiên nên thử. |
| **Heavy** | Làm đều mạnh mẽ cho môi trường ồn ào. Xe hơi, phòng đông người, nghe âm lượng thấp. |
| **Voice / Podcast** | Chỉnh cho giọng nói. Attack chậm hơn để các âm xì lọt qua, makeup gain rộng rãi kéo giọng lên. |
| **Old Recordings** | Album cổ và vinyl phục chế, nơi mức trung bình thấp hơn các bản phát hành hiện đại. |
| **Late Night** | Nén mạnh cộng với tăng lớn cho nghe yên tĩnh khi hàng xóm hay người nhà đang ngủ. |
| **Movie Dialog** | Đưa lời nói lên so với nhạc và hiệu ứng âm thanh trong một bản nhạc phim đa dạng. |
| **Streaming Match** | Nhắm tới khoảng chuẩn hóa độ ồn của các dịch vụ phát trực tuyến hiện đại quanh mức -14 LUFS. |
| **Maximum Loudness** | Tất tay. Chạm bộ giới hạn; hãy đợi một tín hiệu bị ép, rất đều. Cài đặt sẵn âm lượng tối đa theo đúng nghĩa đen. |

## Freeverb (Reverb, cảm giác về không gian)

**Nó làm gì:** Thêm cảm giác về không gian cho nhạc, từ một phòng nhỏ đến một sảnh lớn. Chọn một cài đặt sẵn, hoặc tự tinh chỉnh hỗn hợp khô và ướt, kích thước phòng, độ tắt dần và độ rộng. Reverb là tiếng vọng tự nhiên bạn nghe trong bất kỳ không gian thực nào, và Freeverb tái tạo nó bằng phần mềm. Một chút làm các bản ghi phẳng hoặc thu gần cảm thấy thoáng hơn và sống động hơn. Nhiều thì đặt nhạc vào một không gian lớn, xa xăm. Đây là hiệu ứng sáng tạo, nên giữ hỗn hợp ướt vừa phải để có kết quả tự nhiên.

**Thanh trượt:**

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Dry mix** | Giữ lại bao nhiêu âm thanh gốc, chưa xử lý. Giá trị cao hơn để lại nhiều tín hiệu khô hơn trong hỗn hợp. | 0 đến 1 (0.0) |
| **Wet mix** | Thêm bao nhiêu âm thanh có reverb. Giá trị cao hơn làm reverb to hơn và rõ hơn. | 0 đến 3 (1.0) |
| **Room size** | Kích thước của không gian tưởng tượng. Giá trị cao hơn cho đuôi reverb dài hơn, lớn hơn, từ phòng nhỏ đến nhà thờ lớn. | 0 đến 1 (0.5) |
| **Damp** | Các tần số cao tắt dần nhanh thế nào trong đuôi. Giá trị cao hơn làm reverb tối hơn và ấm hơn. | 0 đến 1 (0.5) |
| **Width** | Độ trải stereo của reverb. Giá trị cao hơn làm không gian cảm thấy rộng hơn giữa kênh trái và phải. | 0 đến 1 (1.0) |

**Cài đặt sẵn:**

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Room** | Một không gian nhỏ, chật. Không khí tinh tế thêm cảm giác về nơi chốn mà không làm nhòe âm thanh. |
| **Studio** | Một phòng thu khô, được kiểm soát. Vừa đủ phản xạ để nghe tự nhiên. |
| **Hall** | Một sảnh hòa nhạc lớn. Một đuôi dài, đầy đặn phù hợp với nhạc giao hưởng và acoustic. |
| **Cathedral** | Một không gian đá khổng lồ, vang vọng. Đuôi reverb dài nhất, kịch tính nhất. |
| **Plate** | Reverb bản kim loại studio sáng, dày. Kinh điển cho giọng hát và trống. |
| **Ambience** | Một không khí ngắn, thoáng. Thêm cảm giác không gian nhẹ trong khi vẫn chủ yếu khô. |

## Auto Wah (Quét bộ lọc funky)

**Nó làm gì:** Một bộ lọc tự quét lên xuống để tạo âm wah funky, giống giọng nói. Chọn một cài đặt sẵn, hoặc tự đặt hỗn hợp ướt, feedback, tốc độ, phạm vi và tần số. Nó là cùng tiếng «wah» quét mà một pedal wah guitar tạo ra, nhưng ở đây nó tự di chuyển theo nhịp nhạc. Nó nghe tuyệt trên các bản funk, disco và electronic. Đây là hiệu ứng táo bạo, rõ ràng, nên một chút cũng đủ dùng cho nghe thường ngày.

**Thanh trượt:**

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Wet mix** | Hiệu ứng wah mạnh thế nào trong hỗn hợp. Giá trị cao hơn làm bộ lọc quét rõ hơn. | -2 đến +2 (1.5) |
| **Feedback** | Bao nhiêu đầu ra được đưa trở lại vào hiệu ứng. Giá trị cao hơn làm wah cộng hưởng và rõ nét hơn. | -1 đến +1 (0.5) |
| **Rate** | Bộ lọc quét lên xuống nhanh thế nào. Giá trị cao hơn cho wah nhanh hơn, nhịp nhàng hơn. | 0.1 đến 9 Hz (2.0) |
| **Range** | Bộ lọc quét xa thế nào, tính bằng quãng tám. Giá trị cao hơn cho một cú quét rộng hơn, kịch tính hơn. | 0.1 đến 9 quãng tám (4.3) |
| **Frequency** | Tần số cơ sở mà bộ lọc quét quanh đó. Giá trị thấp hơn nghe sâu hơn; giá trị cao hơn nghe sáng hơn. | 1 đến 1000 Hz (50) |

**Cài đặt sẵn:**

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Classic** | Một cú quét wah cân bằng, kinh điển. Điểm khởi đầu tốt cho funk và rock. |
| **Slow** | Một cú quét chậm, rộng trôi nhẹ lên xuống. Tuyệt cho pad và các nốt dài. |
| **Funky** | Một cú quét nhanh, đầy lực với nhiều chuyển động. Thêm chất nhịp điệu cho guitar và synth. |
| **Deep** | Một cú quét sâu, rộng bắt đầu từ tần số thấp. Lớn và kịch tính. |
| **Subtle** | Một chuyển động nhẹ nhàng, kín đáo. Thêm cá tính mà không lấn át âm thanh. |
| **Resonant** | Một wah sắc nét, cộng hưởng với feedback cao. Giống giọng nói và biểu cảm. |

## Phaser (Xoáy vù vù)

**Nó làm gì:** Một bộ lọc quét thêm chuyển động xoáy, vù vù cho âm thanh. Chọn một cài đặt sẵn, hoặc tự đặt feedback, tốc độ, phạm vi và tần số. Nó thêm chuyển động nhẹ và lấp lánh mà không thay đổi các nốt. Nó tinh tế trên giọng hát và pad, và kịch tính trên synth và guitar. Thử Slow cho cảm giác mơ màng hoặc Jet cho một cú xoáy mạnh.

**Thanh trượt:**

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Feedback** | Bao nhiêu đầu ra được đưa trở lại vào hiệu ứng. Giá trị cao hơn làm phaser cộng hưởng và rõ nét hơn. | -1 đến +1 (0.0) |
| **Rate** | Bộ lọc quét lên xuống nhanh thế nào. Giá trị cao hơn cho phasing nhanh hơn, nhịp nhàng hơn. | 0.1 đến 9 Hz (1.0) |
| **Range** | Bộ lọc quét xa thế nào, tính bằng quãng tám. Giá trị cao hơn cho một cú quét rộng hơn, kịch tính hơn. | 0.1 đến 9 quãng tám (4.0) |
| **Frequency** | Tần số cơ sở mà bộ lọc quét quanh đó. Giá trị thấp hơn nghe sâu hơn; giá trị cao hơn nghe sáng hơn. | 1 đến 1000 Hz (100) |

**Cài đặt sẵn:**

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Classic** | Một cú quét phaser cân bằng, kinh điển. Điểm khởi đầu tốt cho guitar và phím. |
| **Slow** | Một cú quét chậm, rộng trôi nhẹ lên xuống. Tuyệt cho pad và các nốt dài. |
| **Fast** | Một cú quét nhanh, lấp lánh với nhiều chuyển động. Thêm chuyển động và năng lượng. |
| **Deep** | Một cú quét sâu, rộng bắt đầu từ tần số thấp. Lớn và kịch tính. |
| **Subtle** | Một chuyển động nhẹ nhàng, kín đáo. Thêm cá tính mà không lấn át âm thanh. |
| **Jet** | Một cú quét dữ dội, cộng hưởng với feedback cao, tiếng vù vù máy bay phản lực kinh điển. |

## Flanger (Quét kiểu máy bay phản lực)

**Nó làm gì:** Một độ trễ ngắn, di chuyển tạo cho âm thanh một cú quét vù vù kiểu máy bay phản lực. Chọn một cài đặt sẵn, hoặc tự đặt độ sâu, feedback, tốc độ và độ trễ. Nó là người anh em mạnh hơn, kim loại hơn của phaser, nổi tiếng với cú quét vù vù trong nhạc rock cổ điển và electronic. Cài đặt tinh tế thêm chuyển động nhẹ, còn cài đặt sâu thì kịch tính và rõ ràng. Tốt nhất dùng dè dặt, để tạo hiệu ứng.

**Thanh trượt:**

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Depth** | Hiệu ứng quét mạnh thế nào. Giá trị cao hơn làm flanging rõ hơn. | 0 đến 100% (25) |
| **Feedback** | Bao nhiêu đầu ra được đưa trở lại vào hiệu ứng. Giá trị cao hơn làm flanger cộng hưởng và kim loại hơn. | -99 đến +99% (-50) |
| **Rate** | Cú quét di chuyển lên xuống nhanh thế nào. Giá trị cao hơn cho chuyển động nhanh hơn, lấp lánh hơn. | 0 đến 10 Hz (0.25) |
| **Delay** | Thời gian trễ cơ sở mà cú quét được dựng trên đó. Giá trị cao hơn cho một cá tính sâu hơn, rỗng hơn. | 0 đến 4 ms (2.0) |

**Cài đặt sẵn:**

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Classic** | Một flanger cân bằng, kinh điển. Điểm khởi đầu tốt cho guitar và phím. |
| **Subtle** | Một cú quét nhẹ nhàng, kín đáo. Thêm chuyển động mà không lấn át âm thanh. |
| **Deep** | Một cú quét sâu, nặng với feedback mạnh. Lớn và kịch tính. |
| **Jet** | Một cú quét dữ dội với feedback dương, tiếng vù vù máy bay phản lực kinh điển. |
| **Fast** | Một cú quét nhanh, lấp lánh với nhiều chuyển động và năng lượng. |
| **Wide** | Một cú quét chậm, rộng với độ trễ dài. Đầy đặn và rộng rãi. |

## Echo (Lặp lại)

**Nó làm gì:** Lặp lại âm thanh thành các tiếng vọng nhạt dần để tạo cảm giác về không gian và chiều sâu. Chọn một cài đặt sẵn, hoặc tự đặt hỗn hợp ướt, feedback và độ trễ. Nó giống như gọi vọng trong một hẻm núi: âm thanh trở lại một hoặc nhiều lần sau một khoảng ngắn. Một lần lặp ngắn duy nhất thêm thân âm và cảm giác hoài cổ, còn các lần lặp dài hơn với nhiều feedback tạo ra những đuôi âm rộng rãi, kéo dài. Cài đặt sẵn Ping Pong nảy các lần lặp giữa tai trái và tai phải của bạn, thú vị trên tai nghe. Giữ hỗn hợp ướt vừa phải để các tiếng vọng hỗ trợ nhạc chứ không che lấp nó.

**Thanh trượt:**

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Wet mix** | Các tiếng vọng to thế nào so với âm thanh gốc. Giá trị cao hơn làm các lần lặp nổi bật hơn. | -2 đến +2 (0.6) |
| **Feedback** | Echo lặp lại bao nhiêu lần. Giá trị cao hơn cho nhiều lần lặp hơn, mất nhiều thời gian hơn để tắt dần. | -1 đến +1 (0.5) |
| **Delay** | Thời gian giữa các tiếng vọng. Giá trị ngắn hơn cho một slap-back chặt; giá trị dài hơn cho các lần lặp giãn cách. | 0.01 đến 2 s (0.4) |

**Cài đặt sẵn:**

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Slapback** | Một lần lặp duy nhất, chặt ngay sau âm thanh. Slap-back rockabilly kinh điển. |
| **Room** | Một tiếng vọng ngắn, tự nhiên, như một phòng nhỏ. Thêm không gian mà không làm nhòe âm thanh. |
| **Tape** | Các lần lặp ấm, vừa phải nhạt dần từ từ, như một tape delay cũ. |
| **Dub** | Các lần lặp dài, nặng với feedback mạnh. Lớn, kiểu dub và rộng rãi. |
| **Ping Pong** | Các tiếng vọng nảy giữa loa trái và phải để tạo hiệu ứng stereo rộng. |
| **Long** | Các lần lặp chậm, giãn cách rộng kéo dài xa phía sau âm thanh. |

## Chorus (Âm thanh dày hơn, rộng hơn)

**Nó làm gì:** Làm dày và mở rộng âm thanh bằng cách xếp một bản sao dịch chuyển lên trên bản gốc. Chọn một cài đặt sẵn, hoặc tự đặt hỗn hợp ướt/khô, độ sâu, tốc độ và feedback. Nó làm một nhạc cụ hoặc giọng hát nghe như nhiều cái cùng chơi, bằng cách thêm những bản sao hơi lệch tông, đang di chuyển. Điều này thêm sự phong phú và một chút lấp lánh nhẹ. Cài đặt tinh tế làm ấm mọi thứ lên, còn cài đặt mạnh nghe đầy đặn và mơ màng. Nó phổ biến trên guitar, keyboard và giọng hát.

**Thanh trượt:**

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Wet/Dry** | Bạn nghe bao nhiêu chorus so với âm thanh gốc. Giá trị cao hơn làm hiệu ứng rõ hơn. | 0 đến 100% (50) |
| **Depth** | Cao độ dao động lên xuống xa thế nào. Giá trị cao hơn cho âm thanh dày hơn, lấp lánh hơn. | 0 đến 100% (25) |
| **Rate** | Độ lấp lánh di chuyển nhanh thế nào. Tốc độ chậm hơn nghe nhẹ nhàng và đầy đặn; tốc độ nhanh hơn nghe giống vibrato hơn. | 0 đến 10 Hz (1.1) |
| **Feedback** | Bao nhiêu hiệu ứng được đưa trở lại vào chính nó. Giá trị cao hơn làm chorus cộng hưởng và mạnh hơn. | -99 đến +99% (25) |

**Cài đặt sẵn:**

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Subtle** | Một sự làm dày nhẹ nhàng thêm độ ấm mà không thu hút chú ý vào bản thân nó. |
| **Lush** | Một chorus phong phú, kinh điển. Một cài đặt đa dụng tuyệt cho guitar và phím. |
| **Ensemble** | Một sự lấp lánh đầy đặn, nhiều lớp làm một nhạc cụ đơn nghe như nhiều cái. |
| **Vibrato** | Hoàn toàn ướt với tốc độ nhanh, cho một vibrato rung thay vì một chorus tinh tế. |
| **Wide** | Một sự lấp lánh chậm, rộng mở ra hình ảnh stereo. Rộng rãi và mơ màng. |
| **Twelve-String** | Một sự lấp lánh sáng, cộng hưởng gợi nhớ một cây guitar mười hai dây. |

## Distortion (Sạn và cạnh gắt)

**Nó làm gì:** Thêm sạn và cạnh gắt bằng cách overdrive âm thanh. Chọn một cài đặt sẵn, hoặc tự đặt drive, output và tone. Nó cố ý làm ráp âm thanh, từ một cạnh ấm, sạn đến một âm vỡ, fuzzy. Nó là một hiệu ứng sáng tạo, để cho vui chứ không phải cách cải thiện chất lượng, nên dùng với lượng nhỏ. Nó thú vị trên các bản electronic, rock và thử nghiệm. Hạ Output xuống nếu một cài đặt sẵn nặng trở nên quá to.

**Thanh trượt:**

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Drive** | Âm thanh bị méo mạnh thế nào. Giá trị cao hơn sạn hơn và hung hãn hơn. | 0 đến 100% (15) |
| **Output** | Mức đầu ra sau distortion. Hạ xuống nếu một cài đặt nặng trở nên quá to. | -60 đến 0 dB (-18) |
| **Tone** | Giảm dần phần cao trước khi distortion. Giá trị thấp hơn nghe tối hơn và ấm hơn. | 100 đến 8000 Hz (8000) |
| **Center** | Tần số mà distortion tập trung quanh đó. Dịch cá tính sáng hơn hoặc tối hơn. | 100 đến 8000 Hz (2400) |
| **Width** | Tiêu điểm đó rộng thế nào. Hẹp nghe sắc và mũi; rộng nghe đầy đặn và thoáng. | 100 đến 8000 Hz (2400) |

**Cài đặt sẵn:**

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Warm Drive** | Một sạn nhẹ, ấm thêm cạnh gắt mà không thay đổi cá tính nhiều. |
| **Crunch** | Một overdrive giòn kinh điển, đầy lực và nhịp nhàng. |
| **Overdrive** | Một âm sáng, được drive với nhiều chất. Tuyệt cho các âm lead. |
| **Fuzz** | Một fuzz dày, bão hòa. Nặng và đầy hài âm. |
| **Metal** | Một âm high-gain chặt, tập trung phần trung cho các âm hung hãn, nặng. |
| **Screamer** | Một overdrive tăng phần trung xuyên qua, như một tube screamer. |
| **LoFi** | Một distortion băng hẹp, nghiền nát cho một cá tính lo-fi sạn. |

## Rotate (Stereo xoay)

**Nó làm gì:** Xoay âm thanh quanh trường stereo để tạo hiệu ứng xoay, xoáy. Chọn một cài đặt sẵn, hoặc tự đặt tốc độ. Nó từ từ di chuyển âm thanh quanh kênh trái và phải của bạn, hơi giống một loa đang quay, điều này thêm một cảm giác xoáy, thôi miên. Cài đặt chậm thì nhẹ nhàng và rộng, còn cài đặt nhanh thì chóng mặt và rõ ràng. Nó là một hiệu ứng stereo, nên dễ nhận thấy nhất trên tai nghe hoặc loa được đặt tốt.

**Thanh trượt:**

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Rate** | Âm thanh xoay quanh trường stereo nhanh thế nào. Giá trị âm xoay theo hướng ngược lại; số không giữ nó đứng yên. | -5 đến +5 Hz (1.0) |

**Cài đặt sẵn:**

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Slow Pan** | Một sự trôi chậm, nhẹ nhàng từ bên này sang bên kia. Tinh tế và rộng. |
| **Sway** | Một sự đung đưa trái-phải đều đặn. Thêm chuyển động nhẹ cho hình ảnh stereo. |
| **Rotary** | Một cú xoay vừa phải gợi nhớ một loa xoay. |
| **Fast Spin** | Một cú xoay nhanh quanh trường stereo để tạo hiệu ứng chóng mặt, xoáy. |
| **Reverse** | Một cú xoay vừa phải theo hướng ngược lại. |
| **Whirl** | Một cú xoáy rất nhanh. Dữ dội và gây mất phương hướng. |

## Crossfeed (Âm thanh tự nhiên trên tai nghe)

Trên loa, mỗi tai của bạn nghe cả loa trái và loa phải, chỉ khác nhau đôi chút về thời điểm và âm lượng. Trên tai nghe, sự hòa trộn tự nhiên đó biến mất: tai trái của bạn chỉ nghe kênh trái và tai phải chỉ nghe kênh phải. Kiểu «siêu stereo» này có thể làm nhạc cảm thấy như bị chia tách bên trong đầu bạn, và các bản ghi được pan cứng, nơi một nhạc cụ nằm hoàn toàn ở một bên, có thể cảm thấy không tự nhiên hoặc mệt mỏi khi nghe lâu.

Crossfeed sửa điều này bằng cách trộn một lượng nhỏ, đã lọc của mỗi kênh vào kênh kia, với một độ trễ nhỏ và một sự giảm dần nhẹ các tần số cao. Điều đó gần với cách âm thanh từ loa thật đến cả hai tai của bạn, bao gồm cả cách đầu bạn hơi che tai xa. Kết quả là một hình ảnh tự nhiên hơn, giống loa hơn nằm hơi phía trước bạn thay vì bên trong đầu, và nó giảm mệt mỏi khi nghe trong các buổi dài. Flacbox dùng phương pháp **bs2b (Bauer stereophonic-to-binaural)** nổi tiếng, một crossfeed mã nguồn mở được nhiều trình phát audiophile tôn trọng sử dụng. Bạn có thể đọc về thuật toán trên [trang dự án bs2b](https://bs2b.sourceforge.net/).

**Cutoff** kiểm soát độ ấm của sự hòa trộn, và **Feed level** kiểm soát độ mạnh của nó. Các cài đặt sẵn bao phủ các mức bs2b kinh điển, từ một chút gần như vô hình đến một sự hòa trộn chắc chắn, giống loa. Crossfeed là một hiệu ứng tai nghe, nên hãy tắt nó khi bạn nghe trên loa.

**Thanh trượt:**

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Cutoff** | Đặt nơi mà sự rò rỉ giữa các kênh bắt đầu giảm dần. Giá trị thấp hơn cho một hiệu ứng ấm hơn, rõ nét hơn. | 300 đến 2000 Hz (700) |
| **Feed level** | Kiểm soát bao nhiêu của một kênh rò rỉ sang kênh kia. Giá trị cao hơn tạo ra âm thanh giống loa hơn. | 1 đến 15 dB (4.5) |

**Cài đặt sẵn:**

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Subtle** | Crossfeed gần như vô hình cho nghe thông thường. Làm mềm stereo pan cứng mà không thay đổi cân bằng âm sắc. |
| **Chu Moy** | Mặc định đa dụng kinh điển. Cân bằng và hơi ấm, nó hoạt động trên gần như mọi chất liệu. Bắt đầu ở đây. |
| **Strong** | Rò rỉ mạnh hơn cho các bản mix pan cứng hơn. Thu hẹp stereo rõ ràng hơn. |
| **Jan Meier** | Phổ biến trong giới đam mê tai nghe. Feed rộng hơn, trình bày giống loa hơn, nâng bass nhẹ. |
| **Speaker-like** | Được chỉnh cho sự tái tạo kiểu loa tự nhiên nhất qua tai nghe. |
| **Vintage Stereo** | Crossfeed mạnh được chỉnh cho các bản mix thập niên 1960 và 1970 với trống và giọng hát pan cứng. |

## Xử lý tín hiệu: Tự dựng chuỗi DSP của bạn

Ngoài các hiệu ứng có sẵn, Flacbox cho phép bạn tự dựng chuỗi của mình trong **Cài đặt > Trình phát âm thanh > Xử lý tín hiệu**. Như ứng dụng giải thích khi chuỗi trống: *«Chạm + để thêm một hiệu ứng. Bật hoặc tắt từng cái bằng công tắc của nó, kéo để sắp xếp lại, chạm để chỉnh các tham số của nó, và nhấn giữ để nhân đôi hoặc xóa.»*

**Thứ tự quan trọng**: một bộ lọc trước một distortion nghe khác với cùng bộ lọc đó sau nó. Bạn cũng có thể hướng toàn bộ chuỗi vào **Tất cả các kênh**, **Kênh trái**, hoặc **Kênh phải**.

Dưới đây là mọi khối, cùng văn bản của chính ứng dụng cho từng thanh trượt và từng cài đặt sẵn.

### Gain (Điều chỉnh mức)

Nâng hoặc hạ mức tại một điểm trong chuỗi.

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Gain** | Tăng hoặc cắt mức tại điểm này trong chuỗi. Dùng nó để bù mức sau các hiệu ứng khác, hoặc để drive những cái theo sau. | -24 đến +24 dB (0) |

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Unity** | Không thay đổi mức. Một điểm khởi đầu trung tính. |
| **Cut** | Một cú cắt lớn. Thuần hóa một nguồn to, hoặc tạo chỗ trước các hiệu ứng theo sau. |
| **Trim** | Một cú cắt nhẹ để kéo mức lùi lại một chút. |
| **Lift** | Một sự tăng vừa phải để nâng một nguồn nhỏ lên. |
| **Boost** | Một sự tăng mạnh cho chất liệu nhỏ, hoặc để drive các hiệu ứng theo sau mạnh hơn. |
| **Max** | Tăng tối đa. To, coi chừng clipping ở phần sau của chuỗi. |

### Low Pass (Loại bỏ phần cao)

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Cutoff** | Đặt nơi bộ lọc bắt đầu giảm dần phần cao. Hạ nó xuống để làm tối và mềm âm thanh; nâng nó lên tối đa để mở hoàn toàn. | 20 Hz đến 20 kHz (20 kHz) |
| **Resonance** | Nhấn mạnh các tần số ngay tại cutoff. Giữ nó thấp để giảm dần sạch; nâng nó lên để có một cạnh nhọn, réo rắt. | 0.1 đến 10 (0.707) |

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Air** | Chỉ cắt phần đỉnh cao nhất. Bớt một chút cạnh gắt mà không làm mờ âm thanh. |
| **Warm** | Một sự giảm dần nhẹ nhàng của phần cao cho một âm ấm hơn, tròn hơn. |
| **Mellow** | Được làm mềm rõ rệt. Kéo độ sáng lùi lại cho một cảm giác thư thái. |
| **Muffled** | Tối và bị bịt, như nghe qua một bức tường. |
| **Telephone** | Một đỉnh hẹp, cộng hưởng ở phần thấp của dải. Một giọng mỏng, giống điện thoại. |

### High Pass (Loại bỏ phần thấp)

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Cutoff** | Đặt nơi bộ lọc bắt đầu giảm dần phần thấp. Nâng nó lên để làm mỏng phần thấp và loại bỏ tiếng ù; hạ nó xuống đáy để mở hoàn toàn. | 20 Hz đến 20 kHz (20 Hz) |
| **Resonance** | Nhấn mạnh các tần số ngay tại cutoff. Giữ nó thấp để giảm dần sạch; nâng nó lên để có một cạnh nhọn, réo rắt. | 0.1 đến 10 (0.707) |

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Rumble Cut** | Loại bỏ tiếng ù hạ âm và DC offset mà không chạm vào phần thấp nghe được. |
| **Tighten** | Cắt các tần số thấp ù để có một bass chặt hơn, sạch hơn. |
| **Thin** | Cắt độ ấm và thân âm, để lại một âm thanh nhẹ hơn, mỏng hơn. |
| **Radio** | Chỉ còn phần trung và cao, như một loa radio nhỏ. |
| **Telephone** | Một đỉnh hẹp, cộng hưởng ở phần cao của dải. Một giọng mỏng, giống điện thoại. |

### Band Pass (Giữ một dải giữa)

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Center** | Đặt tần số mà bộ lọc cho đi qua. Mọi thứ trên và dưới nó đều bị giảm dần. Quét nó để chọn ra bass, trung, hoặc cao. | 20 Hz đến 20 kHz (1 kHz) |
| **Resonance** | Kiểm soát dải rộng thế nào. Giá trị thấp cho một phạm vi rộng đi qua; nâng nó lên để thu hẹp vào tâm cho một âm sắc nhọn, cộng hưởng. | 0.1 đến 10 (0.707) |

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Voice** | Một dải rộng quanh phần trung nơi hầu hết giọng hát nằm. Một điểm khởi đầu trung tính. |
| **Bass** | Cô lập phần thấp, chỉ để lại bass và kick. |
| **Body** | Tập trung vào phần thấp-trung cho một thân âm ấm, hộp. |
| **Presence** | Nâng phần trên-trung cho độ rõ và sự hiện diện. |
| **Telephone** | Một dải trung hẹp. Một âm thanh mỏng, giống điện thoại. |
| **Wah** | Một đỉnh rất hẹp, cộng hưởng. Quét tâm để tạo hiệu ứng wah. |

### Notch (Loại bỏ một dải hẹp)

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Frequency** | Đặt tần số mà bộ lọc loại bỏ. Mọi thứ trên và dưới nó đều đi qua. Chỉnh nó vào một tiếng ù hoặc cộng hưởng để cắt nó ra. | 20 Hz đến 20 kHz (60 Hz) |
| **Resonance** | Kiểm soát cú cắt rộng thế nào. Giá trị thấp múc ra một phạm vi rộng; nâng nó lên để chỉ loại bỏ một dải điểm nhỏ và để lại phần còn lại nguyên vẹn. | 0.1 đến 10 (8.0) |

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Mains Hum 60** | Loại bỏ tiếng ù điện 60 Hz (điện lưới Bắc Mỹ). Một điểm khởi đầu trung tính. |
| **Mains Hum 50** | Loại bỏ tiếng ù điện 50 Hz (điện lưới châu Âu và khác). |
| **Rumble** | Cắt một tiếng ù hoặc cộng hưởng tần số thấp mà không làm mỏng toàn bộ phần đáy. |
| **Mud** | Múc ra bùn phần thấp-trung cho một âm thanh sạch hơn, rõ hơn. |
| **Boxy** | Loại bỏ một tiếng vang hộp ở phần trung. |
| **Harsh** | Thuần hóa một đỉnh chói, xuyên thấu ở phần trên-trung. |

### Peaking (Dải EQ tham số)

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Frequency** | Tâm của dải cần tăng hoặc cắt. Quét nó để tìm tần số bạn muốn định hình. | 20 Hz đến 20 kHz (1 kHz) |
| **Gain** | Tăng hoặc cắt bao nhiêu tại tâm. Dương nâng dải; âm múc nó ra. | -15 đến +15 dB (0) |
| **Q factor** | Đặt dải rộng thế nào. Giá trị thấp định hình một vùng rộng; giá trị cao thu hẹp vào cho các thay đổi phẫu thuật, điểm nhỏ. | 0.1 đến 10 (1.0) |

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Presence** | Một sự nâng phần trên-trung rộng cho độ rõ và sự hiện diện. Một điểm khởi đầu trung tính. |
| **Warmth** | Một sự tăng phần thấp-trung rộng thêm thân âm và độ ấm. |
| **Vocal Boost** | Nâng dải giọng hát cốt lõi để đưa giọng ra trước. |
| **Cut Mud** | Múc ra bùn phần thấp-trung hộp cho một âm thanh sạch hơn. |
| **Tame Harsh** | Một cú cắt hẹp để thuần hóa một đỉnh chói, xuyên thấu. |
| **Punch** | Một sự tăng phần thấp thêm lực và tác động cho phần thấp. |
| **Sub Boost** | Một sự tăng sâu ở phần đáy nhất cho thêm sức nặng sub-bass. |
| **Air** | Một sự nâng rộng ở phần đỉnh cho một độ thoáng mở, thoáng đãng. |
| **Clarity** | Nâng phần cao-trung để thêm độ rõ nét và cạnh. |
| **De-Ess** | Một cú cắt hẹp trong dải âm xì để thuần hóa các âm S chói. |
| **De-Boom** | Cắt một sự tích tụ tần số thấp ù cho một phần thấp chặt hơn. |
| **Scoop** | Một cú lõm phần trung rộng cho một âm được múc lõm, hiện đại. |

### Low Shelf (Kiểm soát Bass và Tăng Bass)

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Frequency** | Đặt góc mà bên dưới nó thềm có hiệu lực. Mọi thứ dưới nó được tăng hoặc cắt cùng nhau. | 20 đến 2000 Hz (200) |
| **Gain** | Nâng hoặc hạ phần thấp bao nhiêu. Dương thêm sức nặng và độ ấm; âm làm mỏng nó. | -15 đến +15 dB (0) |

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Warmth** | Một sự nâng phần thấp nhẹ nhàng cho độ ấm và thân âm. Một điểm khởi đầu trung tính. |
| **Bass Boost** | Một sự tăng chắc chắn cho bass để có sức nặng và lực. |
| **Fullness** | Lấp đầy phần thấp-trung cho một âm đầy đặn hơn, tròn hơn. |
| **Trim Bass** | Một cú cắt vừa phải để làm nhẹ một bản mix nặng bass. |
| **Cut Lows** | Một cú cắt mạnh để làm mỏng hoặc de-boom phần thấp. |
| **Big Bottom** | Một sự tăng phần thấp lớn cho sức nặng và tiếng ù tối đa. |

### High Shelf (Kiểm soát Treble)

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Frequency** | Đặt góc mà bên trên nó thềm có hiệu lực. Mọi thứ trên nó được tăng hoặc cắt cùng nhau. | 1 đến 20 kHz (8 kHz) |
| **Gain** | Nâng hoặc hạ phần cao bao nhiêu. Dương thêm độ sáng và độ thoáng; âm làm mượt và tối. | -15 đến +15 dB (0) |

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Presence** | Một sự nâng phần cao nhẹ nhàng cho độ rõ và chi tiết. Một điểm khởi đầu trung tính. |
| **Air** | Mở ra phần đỉnh nhất cho một âm thoáng, mở. |
| **Bright** | Một sự tăng mạnh cho một âm sắc trong trẻo, sáng, đưa ra trước. |
| **Soften** | Một cú cắt vừa phải để bớt cạnh gắt của phần cao chói. |
| **Tame Highs** | Một cú cắt mạnh để làm tối và mượt một âm thanh quá sáng. |
| **Sparkle** | Một sự tăng phần đỉnh lớn cho độ lấp lánh và sáng lóng lánh tối đa. |

### Soft Clip (Bão hòa ấm)

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Drive** | Đẩy tín hiệu mạnh hơn vào bộ tạo hình sóng. Lượng thấp thêm độ ấm nhẹ nhàng; lượng cao làm tròn các đỉnh thành bão hòa dày và sạn. | 0 đến 40 dB (0) |

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Warm** | Một chút drive cho độ ấm nhẹ nhàng, kiểu analog. |
| **Drive** | Bão hòa rõ rệt làm dày và tô màu âm thanh. |
| **Crunch** | Drive nặng với một cạnh giòn nghe được. |
| **Fuzz** | Distortion dày, fuzzy. Các đỉnh bị ép mạnh. |
| **Destroy** | Drive tối đa. Sạn hung hãn, bão hòa hoàn toàn. |

### Bit Crusher (Lo-Fi hoài cổ)

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Bit depth** | Đặt bao nhiêu bit mô tả mỗi mẫu. Ít bit hơn nghĩa là các bước thô hơn và nhiều nhiễu lượng tử hóa hơn, cho một âm số giòn, sạn. | 1 đến 16 bit (16) |
| **Sample rate** | Giảm lấy mẫu âm thanh. Ở một trăm phần trăm tần số không bị đụng tới; hạ nó xuống để giữ mỗi mẫu lâu hơn, làm mờ phần cao và thêm một cạnh chói, có aliasing. | 1% đến 100% (100%) |

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Vintage** | Một sự sụt chất lượng tinh tế, như một máy lấy mẫu số thời kỳ đầu. |
| **LoFi** | Lo-fi 8-bit, nửa tần số kinh điển. Hạt và hoài cổ. |
| **Crunch** | Nghiền nặng hơn với một cạnh giòn nghe được. |
| **Gritty** | Thô và sạn. Các bước giữa các mức rõ ràng. |
| **Destroy** | Giảm cực đoan. Chói, vỡ, hầu như không nhận ra. |

### Ring Modulator (Âm kim loại và robot)

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Carrier** | Đặt tần số của âm mà tín hiệu được nhân với. Vài hertz cho một dao động tremolo; tần số cao hơn thêm hài âm kim loại, giống chuông và robot. | 1 đến 4000 Hz (440) |
| **Mix** | Trộn âm được điều biến vào với bản gốc. Ở không phần trăm bạn chỉ nghe tín hiệu khô; ở một trăm phần trăm chỉ nghe âm được điều biến hoàn toàn. | 0% đến 100% (0%) |

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Tremolo** | Một carrier rất thấp biến nó thành một tremolo biên độ, làm dao động âm lượng. |
| **Robot** | Một carrier trung thêm hài âm loảng xoảng cho một hiệu ứng giọng robot kinh điển. |
| **Metallic** | Hài âm dày, không điều hòa cho một âm chói, kim loại. |
| **Bell** | Một carrier cao hơn cho tiếng ngân sáng, giống chuông. |
| **Alien** | Hoàn toàn ướt với một carrier cao. Cực đoan, ngoài hành tinh, hầu như không nhận ra. |

### Tremolo (Dao động âm lượng)

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Rate** | Đặt âm lượng đập nhanh thế nào. Tốc độ chậm hơn cho một sự đung đưa mượt; tốc độ nhanh hơn cho một sự ngắt quãng nhanh. | 0.1 đến 20 Hz (5) |
| **Depth** | Đặt âm lượng giảm bao nhiêu ở mỗi nhịp đập. Ở không phần trăm mức ổn định; ở một trăm phần trăm nó tụt hẳn xuống im lặng. | 0% đến 100% (0%) |

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Gentle** | Một sự đung đưa chậm, nông. Chuyển động tinh tế mà không thu hút chú ý. |
| **Classic** | Tremolo amp kinh điển: một tốc độ trung và độ sâu vừa phải. |
| **Deep** | Một nhịp đập mạnh, sâu gần như tụt xuống im lặng mỗi chu kỳ. |
| **Fast** | Một sự rung nhanh cho một cảm giác lấp lánh, bồn chồn. |
| **Chop** | Nhanh và độ sâu tối đa. Một cú ngắt cứng, lắp bắp. |

### Delay (Echo)

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Time** | Đặt khoảng cách trước mỗi tiếng vọng. Thời gian ngắn cho một slapback chặt; thời gian dài hơn giãn cách các lần lặp xa hơn. | 0.01 đến 2 s (0.25) |
| **Feedback** | Đặt bao nhiêu của mỗi tiếng vọng được đưa trở lại. Giá trị thấp cho một lần lặp duy nhất; giá trị cao hơn dựng một chuỗi tiếng vọng dài, kéo dài. | 0 đến 0.95 (0.4) |
| **Mix** | Trộn các tiếng vọng vào với bản gốc. Ở không phần trăm bạn chỉ nghe tín hiệu khô; ở một trăm phần trăm chỉ nghe các tiếng vọng. | 0% đến 100% (0%) |

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Slapback** | Một tiếng vọng ngắn duy nhất, chặt sát bản gốc. Nhân đôi rockabilly và giọng hát. |
| **Echo** | Echo kinh điển: một lần lặp rõ với một vài đuôi kéo theo. |
| **Ping** | Một lần lặp nhanh, nảy thêm chuyển động nhịp nhàng. |
| **Ambient** | Các lần lặp dài hơn, mềm hơn tràn ra thành một đuôi rộng rãi. |
| **Dub** | Feedback cao cho các thác tiếng vọng dài, kiểu dub. |
| **Cavern** | Các lần lặp dài, sâu, như âm thanh vọng qua một không gian khổng lồ. |

### Stereo Width (Thu hẹp hoặc mở rộng)

| Điều khiển | Nó làm gì | Phạm vi (mặc định) |
|---|---|---|
| **Width** | Thu hẹp hoặc mở rộng hình ảnh stereo. Không phần trăm gộp thành mono, một trăm phần trăm để nó nguyên vẹn, và giá trị cao hơn đẩy các bên rộng hơn. Chỉ ảnh hưởng đến các bản stereo trên mục tiêu Tất cả các kênh. | 0% đến 200% (100%) |

| Cài đặt sẵn | Nó làm gì |
|---|---|
| **Wide** | Một sự mở rộng nhẹ nhàng mở ra hình ảnh stereo. Một điểm khởi đầu trung tính. |
| **Wider** | Một sự trải mạnh hơn cho một trường stereo lớn, đắm chìm. |
| **Max** | Độ rộng tối đa. Rất rộng, nhưng coi chừng vấn đề tương thích mono. |
| **Narrow** | Kéo các bên vào cho một hình ảnh chặt hơn, trung tâm hơn. |
| **Focused** | Gần như trung tâm, chỉ với một chút stereo. |
| **Mono** | Gộp hoàn toàn thành mono. Cả hai loa phát cùng một tín hiệu. |

## Mọi thứ hoạt động thế nào bên trong (Phiên bản đơn giản)

- **Công cụ:** bạn chọn một trong Cài đặt > Trình phát âm thanh > Công cụ phát: **Standard** (hệ thống), **Universal** (FFmpeg), hoặc **Sound FX** (**công cụ BASS™** từ [Un4seen Developments](https://www.un4seen.com/)). Công cụ bạn chọn quyết định định dạng nào phát được, và các hiệu ứng, bộ chỉnh âm và chuỗi DSP chỉ chạy trong công cụ Sound FX.
- **Định dạng:** công cụ BASS™ thêm FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, và nhạc module (tracker) bên trên các định dạng hệ thống và FFmpeg.
- **Hiệu ứng:** bộ chỉnh âm, compressor, và hầu hết các hiệu ứng dùng các add-on hiệu ứng BASS™. Freeverb là reverb Freeverb. Chorus, Flanger, và Distortion dùng các hiệu ứng kiểu DirectX kinh điển với điều khiển riêng của chúng.
- **Chuẩn hóa âm lượng:** một bộ cân bằng độ ồn **EBU R128** trực tiếp (chuẩn độ ồn dùng trong phát sóng và phát trực tuyến).
- **Crossfeed:** crossfeed **bs2b (Bauer)**, chạy bên trong công cụ BASS™.
- **Chuỗi DSP:** các khối tùy chỉnh của bạn, áp dụng theo đúng thứ tự bạn đặt, trên tất cả các kênh hoặc chỉ một bên.
- **Đầu ra:** bạn có thể đặt tần số lấy mẫu, số kênh, và kích thước bộ đệm để khớp với thiết bị của bạn.

Vì tất cả những điều này chạy trực tiếp khi nhạc phát, các hiệu ứng:

- Hoạt động **theo thời gian thực** trên mọi thứ, bao gồm tệp đám mây, luồng, và nhạc module.
- **Không bao giờ thay đổi hoặc lưu lại** tệp của bạn. Tắt một hiệu ứng và bản gốc trở lại.
- **Ghi nhớ cài đặt của bạn** cho mỗi hiệu ứng.
- Có thể được **trộn và kết hợp** tự do, vì mỗi cái là riêng biệt.

## Các công thức đơn giản để thử

**Nghe thường ngày**

- **Nhiều bass hơn, sạch sẽ:** Bộ chỉnh âm > Bass Booster, rồi hạ Preamplifier 1 đến 2 dB. Hoặc thêm một DSP Low Shelf ở Bass Boost.
- **Âm lượng đều trên một danh sách phát hỗn hợp:** Chuẩn hóa âm lượng > Standard, cộng với Compressor > Soft.
- **Đánh bóng tổng thể nhẹ nhàng:** Compressor > Transparent, cộng với Chuẩn hóa âm lượng > Light.
- **Giọng hát rõ hơn:** Bộ chỉnh âm > Vocal Booster, hoặc một khối DSP Peaking ở Vocal Boost.
- **Âm đầy đặn hơn trên loa điện thoại nhỏ:** Bộ chỉnh âm > Small Speakers.

**Tai nghe**

- **Dễ chịu hơn, ít mệt hơn trên tai nghe:** Crossfeed > Chu Moy hoặc Jan Meier.
- **Âm rộng hơn trên tai nghe:** DSP Stereo Width > Wide, cộng với Crossfeed > Chu Moy.
- **Sửa các đĩa thập niên 1960 và 1970 pan cứng:** Crossfeed > Vintage Stereo.
- **Một chút thoáng và không gian:** Freeverb > Ambience, giữ thấp, cộng với Crossfeed > Subtle.

**Thời gian yên tĩnh và âm thanh nói**

- **Nghe yên tĩnh khuya:** Chuẩn hóa âm lượng > Night, cộng với Compressor > Late Night.
- **Podcast và sách nói:** Compressor > Voice / Podcast, cộng với Bộ chỉnh âm > Spoken Word.
- **Âm to nhất, đều nhất trong một chiếc xe ồn ào:** Chuẩn hóa âm lượng > Strong, cộng với Compressor > Heavy.

**Sửa vấn đề**

- **Thuần hóa một bản ghi chói, sáng:** Bộ chỉnh âm > Treble Reducer, hoặc một khối DSP Peaking ở Tame Harsh.
- **Loại bỏ tiếng ù điện:** chuỗi DSP > Notch > Mains Hum 60 (hoặc Mains Hum 50 ở châu Âu).
- **Bass chặt hơn, sạch hơn:** DSP High Pass > Tighten, để cắt phần thấp ù.
- **Ít ù hơn trong một bản mix nặng bass:** DSP Low Shelf > Trim Bass, hoặc Peaking > De-Boom.

**Sáng tạo và vui**

- **Cảm giác ấm, rộng rãi:** Freeverb > Hall, giữ thấp.
- **Guitar mơ màng, rộng rãi:** Chorus > Wide, cộng với Echo > Long.
- **Lo-fi hoài cổ:** chuỗi DSP > Bit Crusher (LoFi) vào Soft Clip (Warm).
- **Chuyển động funky trên các bản electronic:** Auto Wah > Funky, hoặc Phaser > Fast.
- **Cú quét máy bay phản lực kinh điển:** Flanger > Jet.

## Câu hỏi thường gặp

{{% details title="Flacbox dùng công cụ âm thanh nào?" closed="true" %}}
Bạn chọn một Công cụ phát trong Cài đặt > Trình phát âm thanh: Standard (công cụ hệ thống của Apple), Universal (công cụ FFmpeg), hoặc Sound FX (công cụ BASS™ từ Un4seen Developments, un4seen.com). Công cụ bạn chọn quyết định định dạng tệp nào phát được. Sound FX là công cụ phát các định dạng bổ sung như FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus, và nhạc MOD hoặc tracker, và đây là công cụ duy nhất cung cấp các hiệu ứng trực tiếp, bộ chỉnh âm 10 dải, và chuỗi DSP. Để dùng các hiệu ứng, hãy đặt Công cụ phát thành Sound FX.
{{% /details %}}

{{% details title="Flacbox có phát được MOD, XM, IT, và nhạc tracker hoặc module khác không?" closed="true" %}}
Có. Công cụ BASS™ có một trình phát module tích hợp tải các tệp MOD, XM, IT, S3M, MTM, UMX, và MO3 và dựng lại bài hát trực tiếp từ các pattern và âm nhạc cụ của nó, đúng theo cách nhạc tracker được thiết kế để phát. Các trình phát iPhone thông thường không làm được điều này. Các hiệu ứng và bộ chỉnh âm cũng hoạt động trên nhạc module.
{{% /details %}}

{{% details title="Flacbox có hỗ trợ DSD và các tệp độ phân giải cao không?" closed="true" %}}
Có. Flacbox phát các tệp DSD (DSF và DFF) qua công cụ BASS™ bằng DSD over PCM để chúng hoạt động trên phần cứng đầu ra thông thường, cùng với FLAC, WavPack, Monkey's Audio (APE), Musepack, và TrueAudio cho phát lossless.
{{% /details %}}

{{% details title="Flacbox có những hiệu ứng âm thanh nào?" closed="true" %}}
Một bộ chỉnh âm 10 dải, Chuẩn hóa âm lượng, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distortion, Rotate, và Crossfeed, cùng một chuỗi DSP tự dựng với các bộ lọc, thềm, gain, soft clip, bit crusher, ring modulator, tremolo, delay, và stereo width. Mỗi cái là riêng biệt và có thể kết hợp với những cái khác.
{{% /details %}}

{{% details title="Cài đặt sẵn là gì?" closed="true" %}}
Cài đặt sẵn là một thiết lập có sẵn cho một hiệu ứng. Thay vì tự di chuyển các thanh trượt, bạn chạm một cài đặt sẵn và âm thanh thay đổi để khớp. Mọi hiệu ứng trong Flacbox đều có vài cài đặt sẵn, và hướng dẫn này liệt kê từng cái làm gì. Nếu bạn di chuyển một thanh trượt sau khi chọn một cài đặt sẵn, hiệu ứng hiển thị «Manual» để báo cho bạn biết nó giờ đang dùng các giá trị của riêng bạn.
{{% /details %}}

{{% details title="Làm thế nào để mở các hiệu ứng âm thanh trong Flacbox?" closed="true" %}}
Mở trình phát Now Playing, chạm nút ⋯ (Thêm), và chọn Hiệu ứng âm thanh. Hoặc vào Cài đặt > Trình phát âm thanh > Hiệu ứng âm thanh. Chạm một hiệu ứng, bật công tắc của nó, và chọn một cài đặt sẵn, hoặc mở các thanh trượt để tinh chỉnh.
{{% /details %}}

{{% details title="Bộ chỉnh âm ở đâu, và cài đặt tốt nhất là gì?" closed="true" %}}
Vào Cài đặt > Trình phát âm thanh > Bộ chỉnh âm. Nó có 10 dải từ 32 Hz đến 16 kHz, mỗi dải từ -12 đến +12 dB, cùng một Preamplifier từ -24 đến +24 dB và 22 cài đặt sẵn. Để nhiều bass hơn, dùng Bass Booster. Để giọng rõ hơn, dùng Vocal Booster hoặc Pop. Để âm sáng hơn, dùng Treble Booster. Rồi điều chỉnh từng dải theo ý thích.
{{% /details %}}

{{% details title="Làm thế nào để tăng bass trong Flacbox?" closed="true" %}}
Hai cách dễ. Trong Bộ chỉnh âm, chọn Bass Booster (hoặc nâng các dải 32 Hz và 64 Hz vài dB). Hoặc, trong Xử lý tín hiệu, thêm một khối Low Shelf đặt ở Bass Boost. Trong cả hai trường hợp, hạ Preamplifier hoặc thêm một khối Gain 1 đến 2 dB để bass giữ sạch và không bị méo.
{{% /details %}}

{{% details title="Cài đặt sẵn bộ chỉnh âm nào tốt nhất cho nhạc của tôi?" closed="true" %}}
Rock và Electronic thêm năng lượng với phần thấp và cao mạnh. Acoustic, Jazz, và Classical giữ ấm và tự nhiên. Pop và Vocal Booster đẩy giọng ra trước. Bass Booster và Hip-Hop thêm sức nặng. Deep và Loudness nghe đầy đặn hơn ở âm lượng thấp. Bắt đầu với cái khớp với thể loại của bạn, rồi tinh chỉnh.
{{% /details %}}

{{% details title="Chuẩn hóa âm lượng là gì, và nó khác ReplayGain thế nào?" closed="true" %}}
Nó làm mọi bản phát ở khoảng cùng một độ ồn. Nó đo độ ồn thực bằng chuẩn EBU R128 (theo LUFS, như các dịch vụ phát trực tuyến) và điều chỉnh mỗi bản hướng về mục tiêu của bạn, với một giới hạn max-boost. Không như ReplayGain, nó không cần thẻ nào trong tệp của bạn và hoạt động trên mọi nguồn, trực tiếp, mà không thay đổi âm thanh. Cài đặt sẵn: Light, Standard, Strong, và Night.
{{% /details %}}

{{% details title="Crossfeed là gì, và tôi có nên dùng nó không?" closed="true" %}}
Crossfeed trộn một chút kênh trái và phải với nhau để tai nghe cảm thấy giống loa thật hơn và ít giống như âm thanh bị kẹt trong đầu bạn hơn. Nó chỉ dành cho tai nghe, nên hãy tắt nó cho loa. Flacbox dùng phương pháp bs2b (Bauer), với các cài đặt sẵn như Chu Moy và Jan Meier.
{{% /details %}}

{{% details title="Sự khác biệt giữa Compressor và Chuẩn hóa âm lượng là gì?" closed="true" %}}
Chuẩn hóa âm lượng khớp độ ồn giữa các bài hát khác nhau. Compressor làm đều các phần to và nhỏ bên trong một bài hát duy nhất. Chúng giải quyết các vấn đề khác nhau và phối hợp tốt với nhau, đặc biệt trong xe hơi hay nơi ồn ào.
{{% /details %}}

{{% details title="Chuỗi Xử lý tín hiệu (DSP) là gì?" closed="true" %}}
Nó là một giá tự dựng trong Cài đặt > Trình phát âm thanh > Xử lý tín hiệu. Thêm các khối như bộ lọc, thềm, gain, soft clip, bit crusher, ring modulator, tremolo, delay, và stereo width, đặt chúng theo thứ tự bất kỳ, bật hoặc tắt từng cái, và hướng chuỗi vào tất cả các kênh, trái, hoặc phải. Vì thứ tự quan trọng, bạn có thể thiết kế chính xác âm thanh bạn muốn.
{{% /details %}}

{{% details title="Sự khác biệt giữa Bộ chỉnh âm, các hiệu ứng, và chuỗi DSP là gì?" closed="true" %}}
Bộ chỉnh âm là một điều khiển âm sắc 10 dải đơn giản. Các Hiệu ứng âm thanh là các công cụ có sẵn (compressor, reverb, echo, và cứ thế) với các cài đặt sẵn. Chuỗi DSP là nơi bạn tự dựng thứ tự hiệu ứng của mình từ các khối riêng lẻ. Bạn có thể chạy cả ba cùng lúc.
{{% /details %}}

{{% details title="Các hiệu ứng có thay đổi hoặc làm hỏng các tệp nhạc của tôi không?" closed="true" %}}
Không. Mọi thứ được áp dụng trực tiếp khi nhạc phát. Các tệp của bạn không bao giờ bị thay đổi hoặc lưu lại. Tắt một hiệu ứng và âm thanh gốc trở lại ngay lập tức.
{{% /details %}}

{{% details title="Tôi có thể dùng nhiều hơn một hiệu ứng cùng lúc không?" closed="true" %}}
Có. Mỗi hiệu ứng có công tắc riêng và không có công tắc chính, nên bất kỳ tổ hợp nào cũng hoạt động. Ví dụ, Chuẩn hóa âm lượng cộng với Compressor cho nghe đều, hoặc Freeverb cộng với Crossfeed trên tai nghe, với bộ chỉnh âm ở trên cùng.
{{% /details %}}

{{% details title="Tại sao các điều khiển hiệu ứng bị làm mờ?" closed="true" %}}
Hiệu ứng đang tắt. Bật công tắc của nó ở phần trên của trình chỉnh sửa để dùng các điều khiển. Mọi hiệu ứng đều tắt theo mặc định.
{{% /details %}}

{{% details title="Nhãn Manual nghĩa là gì?" closed="true" %}}
Nó nghĩa là bạn đã di chuyển một thanh trượt ra khỏi một cài đặt sẵn, nên hiệu ứng giờ đang dùng các giá trị tùy chỉnh của riêng bạn thay vì một cài đặt sẵn có tên. Mỗi thanh trượt đều có nút đặt lại, và chọn lại một cài đặt sẵn sẽ thay thế các giá trị thủ công của bạn.
{{% /details %}}

{{% details title="Tôi có thể lưu và chia sẻ các cài đặt sẵn bộ chỉnh âm của mình không?" closed="true" %}}
Có. Bên cạnh 22 cài đặt sẵn tích hợp, bạn có thể tạo cái của riêng mình, sắp xếp lại chúng, và xuất hoặc nhập chúng để chuyển cài đặt của bạn sang thiết bị khác.
{{% /details %}}

{{% details title="Các hiệu ứng có hoạt động với CarPlay, phát trực tuyến, và phát nền không?" closed="true" %}}
Có. Các hiệu ứng chạy bên trong công cụ BASS™, nên chúng áp dụng cho tệp cục bộ, ổ đám mây, máy chủ phương tiện, luồng, và nhạc module, và chúng vẫn hoạt động trong CarPlay và phát nền.
{{% /details %}}

{{% details title="Tôi có thể thay đổi chất lượng đầu ra âm thanh không?" closed="true" %}}
Có. Trong Cài đặt > Trình phát âm thanh bạn có thể đặt tần số lấy mẫu đầu ra, số kênh, và kích thước bộ đệm để khớp với tai nghe, loa, hoặc DAC của bạn.
{{% /details %}}

{{% details title="Thiết lập khởi đầu tốt cho tai nghe là gì?" closed="true" %}}
Bật Chuẩn hóa âm lượng (Standard), thêm một Compressor nhẹ (Soft), chọn một cài đặt sẵn bộ chỉnh âm bạn thích, và bật Crossfeed (Chu Moy hoặc Jan Meier). Để reverb, echo, và distortion tắt trừ khi bạn muốn một âm thanh sáng tạo.
{{% /details %}}

---

*BASS là thương hiệu của Un4seen Developments Ltd. Xem [un4seen.com](https://www.un4seen.com/). Crossfeed dùng thuật toán bs2b (Bauer stereophonic-to-binaural); xem [trang dự án bs2b](https://bs2b.sourceforge.net/).*
