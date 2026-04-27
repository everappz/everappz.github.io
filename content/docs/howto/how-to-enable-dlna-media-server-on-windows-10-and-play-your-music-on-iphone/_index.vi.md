---
title: "Cách bật DLNA Media Server trên Windows 10 và phát nhạc trên iPhone"
date: 2019-11-26
description: "Bật máy chủ DLNA trên Windows 10 và truyền phát nhạc đến iPhone với ứng dụng Evermusic. Hướng dẫn thiết lập từng bước được bao gồm."
keywords: ["evermusic", "dlna", "windows 10", "phát nhạc trực tuyến trên iphone", "máy chủ phương tiện", "mạng cục bộ", "upnp"]
tags: ["evermusic", "nhạc", "đám mây", "iphone", "lưu trữ", "cục bộ", "nas", "windows", "wifi", "nghe", "mạng", "từ xa", "nhà", "trực tuyến", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**Tóm tắt:** Windows 10 có máy chủ DLNA tích hợp. Bật nó trong cài đặt Mạng và Chia sẻ, sau đó sử dụng ứng dụng miễn phí **Evermusic** trên iPhone để truyền phát toàn bộ thư viện nhạc qua Wi-Fi. Không cần phần mềm máy chủ bên thứ ba.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Bìa trước" caption="Truyền phát nhạc DLNA đến iPhone sử dụng Windows 10 và Evermusic" width="800" >}}

DLNA (Digital Living Network Alliance) là một công cụ mạnh mẽ cho phép bạn dễ dàng truyền phát các nội dung đa phương tiện khác nhau, bao gồm nhạc, giữa các thiết bị hỗ trợ DLNA trên mạng của bạn. Tin tốt là Windows 10, và các phiên bản trước đó, đi kèm với tính năng DLNA tích hợp, loại bỏ nhu cầu sử dụng máy chủ phương tiện bên thứ ba. Đây là cách bật DLNA Media Server trên Windows 10 và thưởng thức truyền phát nhạc trên iPhone.

## Cách bật DLNA Media Server trên Windows 10

1. Nhấp vào nút 'Start'.  
2. Chọn biểu tượng 'Settings'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Cài đặt máy chủ" caption="Mở Cài đặt Windows" width="500" >}}

3. Trên màn hình 'Windows Settings', chọn 'Network & Internet'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Cài đặt Windows" caption="Chọn Network & Internet" width="500" >}}

4. Trong phần 'Network', chọn 'Network and Sharing Center'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Trung tâm chia sẻ" caption="Mở Network and Sharing Center" width="500" >}}

5. Trên màn hình 'Network and Sharing Center', nhấp 'Change advanced sharing settings' ở menu bên trái.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Cài đặt chia sẻ nâng cao" caption="Thay đổi cài đặt chia sẻ nâng cao" width="500" >}}

6. Trên màn hình 'Advanced sharing settings', cuộn xuống phần 'All Networks' và mở rộng bằng cách nhấp vào mũi tên.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Bật khám phá" caption="Mở rộng cài đặt tất cả mạng" width="500" >}}

7. Nhấp 'Turn on media streaming' để kích hoạt máy chủ DLNA.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Bật máy chủ" caption="Bật máy chủ truyền phát phương tiện" width="500" >}}

8. Đặt tên cho thư viện phương tiện và chọn các thiết bị được phép truy cập.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Tên thư viện phương tiện" caption="Đặt tên cho thư viện phương tiện DLNA" width="500" >}}

9. Nhấp 'OK' để xác nhận. Bây giờ, các thư mục cá nhân như Nhạc, Ảnh và Video sẽ hiển thị cho bất kỳ thiết bị truyền phát nào có hỗ trợ UPnP.

## Cách tắt DLNA Media Server trên Windows 10

1. Nhấp 'Start' và gõ 'services' vào ô tìm kiếm.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Dịch vụ Windows" caption="Mở Dịch vụ Windows" width="500" >}}

2. Trên màn hình 'Services', cuộn xuống để tìm 'Windows Media Player Network Sharing Service'.  
3. Nhấp đúp và đặt 'Startup type' thành 'Manual'.  
4. Dừng dịch vụ bằng cách nhấp nút 'Stop'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="Dừng dịch vụ DLNA" caption="Tắt dịch vụ chia sẻ mạng DLNA" width="500" >}}

## Cách phát nhạc từ máy chủ DLNA trên iPhone

1. Cài đặt ứng dụng miễn phí **Evermusic** từ App Store:  
   [Ứng dụng Evermusic](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Mở tab 'Kết nối' và nhấn vào 'Thiết bị khả dụng' trong phần 'Mạng cục bộ'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Kết nối Evermusic" caption="Evermusic: màn hình Kết nối" width="500" >}}

3. Đợi vài giây khi danh sách thiết bị tải và nhấn vào máy chủ Windows Media Player DLNA (ví dụ: 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Thiết bị khả dụng" caption="Các máy chủ DLNA khả dụng trong Evermusic" width="500" >}}

4. Bạn sẽ thấy danh sách các thư mục có sẵn trên máy chủ phương tiện.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Thư mục Evermusic" caption="Duyệt các thư mục được chia sẻ từ máy chủ DLNA" width="500" >}}

5. Mở bất kỳ thư mục nào chứa tệp âm thanh.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Nội dung thư mục" caption="Xem nội dung các thư mục DLNA được chia sẻ" width="500" >}}

6. Nhấn vào bất kỳ tệp nào để khởi động trình phát âm thanh.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Trình phát âm thanh" caption="Phát tệp âm thanh từ DLNA trong Evermusic" width="500" >}}

7. Để nâng cao trải nghiệm âm thanh, nhấn biểu tượng 'Bộ cân bằng' gần chỉ báo âm lượng ở cuối màn hình để bật bộ cân bằng kiểu iPod với bộ tiền khuếch đại.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Bộ cân bằng" caption="Sử dụng bộ cân bằng tích hợp để phát tốt hơn" width="500" >}}

## Kết luận

Với DLNA Media Server trên Windows 10 và Evermusic trên iPhone, bạn có thể thưởng thức truyền phát nhạc liền mạch từ máy tính đến thiết bị di động. Tạm biệt giới hạn lưu trữ và chào đón nhạc theo yêu cầu!

## Câu hỏi thường gặp

{{% details title="Tôi có cần cài đặt phần mềm máy chủ trên Windows 10 không?" closed="true" %}}
Không. Windows 10 đã bao gồm máy chủ phương tiện DLNA tích hợp. Bạn chỉ cần bật truyền phát phương tiện trong cài đặt Network and Sharing Center. Không cần phần mềm bên thứ ba.
{{% /details %}}

{{% details title="iPhone của tôi có cần ở cùng mạng Wi-Fi không?" closed="true" %}}
Có. Truyền phát DLNA hoạt động qua mạng cục bộ của bạn. Cả PC Windows 10 và iPhone đều phải kết nối cùng một mạng Wi-Fi để Evermusic có thể phát hiện máy chủ DLNA.
{{% /details %}}

{{% details title="Tôi có thể truyền phát những định dạng âm thanh nào qua DLNA?" closed="true" %}}
Máy chủ Windows DLNA chia sẻ tệp từ thư mục Nhạc bất kể định dạng. Evermusic hỗ trợ MP3, FLAC, AAC, WAV, OGG, AIFF và nhiều định dạng khác, vì vậy bạn có thể phát hầu như bất kỳ tệp âm thanh nào từ máy chủ.
{{% /details %}}

{{% details title="Tôi có thể sử dụng Flacbox thay vì Evermusic không?" closed="true" %}}
Có. Flacbox cũng hỗ trợ duyệt và phát DLNA/UPnP. Bạn có thể sử dụng một trong hai ứng dụng để khám phá và phát nhạc từ máy chủ Windows DLNA.
{{% /details %}}

{{% details title="Truyền phát DLNA có sử dụng dữ liệu di động không?" closed="true" %}}
Không. DLNA hoạt động hoàn toàn trên mạng Wi-Fi cục bộ. Nó không sử dụng bất kỳ dữ liệu di động nào. Tuy nhiên, cả hai thiết bị phải duy trì kết nối cùng một mạng trong quá trình phát.
{{% /details %}}
