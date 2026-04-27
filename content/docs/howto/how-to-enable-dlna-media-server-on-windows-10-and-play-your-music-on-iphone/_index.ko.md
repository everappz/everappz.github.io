---
title: "Windows 10에서 DLNA 미디어 서버를 활성화하고 iPhone에서 음악을 재생하는 방법"
date: 2019-11-26
description: "Windows 10에서 DLNA 서버를 활성화하고 Evermusic 앱으로 iPhone에 음악을 스트리밍하세요. 단계별 설정 가이드 포함."
keywords: ["evermusic", "dlna", "windows 10", "iphone 음악 스트리밍", "미디어 서버", "로컬 네트워크", "upnp"]
tags: ["evermusic", "음악", "클라우드", "iphone", "저장소", "로컬", "nas", "windows", "wifi", "듣기", "네트워크", "원격", "홈", "온라인", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**요약:** Windows 10에는 내장 DLNA 서버가 있습니다. 네트워크 및 공유 설정에서 활성화한 다음, iPhone에서 무료 **Evermusic** 앱을 사용하여 Wi-Fi를 통해 전체 음악 라이브러리를 스트리밍하세요. 타사 서버 소프트웨어가 필요 없습니다.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: 표지" caption="Windows 10과 Evermusic을 사용한 iPhone으로의 DLNA 음악 스트리밍" width="800" >}}

DLNA(Digital Living Network Alliance)는 네트워크에서 DLNA 지원 장치 간에 음악을 포함한 다양한 미디어 콘텐츠를 쉽게 스트리밍할 수 있게 해주는 강력한 도구입니다. 좋은 소식은 Windows 10과 이전 버전에 내장 DLNA 기능이 포함되어 있어 타사 미디어 서버가 필요 없다는 것입니다. Windows 10에서 DLNA 미디어 서버를 활성화하고 iPhone에서 음악 스트리밍을 즐기는 방법을 알아보세요.

## Windows 10에서 DLNA 미디어 서버를 활성화하는 방법

1. '시작' 버튼을 클릭합니다.  
2. '설정' 아이콘을 선택합니다.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="서버 설정" caption="Windows 설정 열기" width="500" >}}

3. 'Windows 설정' 화면에서 '네트워크 및 인터넷'을 선택합니다.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Windows 설정" caption="네트워크 및 인터넷 선택" width="500" >}}

4. '네트워크'에서 '네트워크 및 공유 센터'를 선택합니다.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="공유 센터" caption="네트워크 및 공유 센터 열기" width="500" >}}

5. '네트워크 및 공유 센터' 화면에서 왼쪽 메뉴의 '고급 공유 설정 변경'을 클릭합니다.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="고급 공유 설정" caption="고급 공유 설정 변경" width="500" >}}

6. '고급 공유 설정' 화면에서 '모든 네트워크' 섹션으로 스크롤하고 화살표를 클릭하여 확장합니다.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="검색 켜기" caption="모든 네트워크 설정 확장" width="500" >}}

7. '미디어 스트리밍 켜기'를 클릭하여 DLNA 서버를 활성화합니다.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="서버 켜기" caption="미디어 스트리밍 서버 활성화" width="500" >}}

8. 미디어 라이브러리에 이름을 지정하고 액세스할 수 있는 장치를 선택합니다.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="미디어 라이브러리 이름" caption="DLNA 미디어 라이브러리 이름 지정" width="500" >}}

9. '확인'을 클릭하여 확인합니다. 이제 음악, 사진, 비디오와 같은 개인 폴더가 UPnP를 지원하는 모든 스트리밍 장치에 표시됩니다.

## Windows 10에서 DLNA 미디어 서버를 비활성화하는 방법

1. '시작'을 클릭하고 검색 필드에 'services'를 입력합니다.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Windows 서비스" caption="Windows 서비스 열기" width="500" >}}

2. '서비스' 화면에서 'Windows Media Player Network Sharing Service'를 찾아 스크롤합니다.  
3. 더블 클릭하고 '시작 유형'을 '수동'으로 설정합니다.  
4. '중지' 버튼을 클릭하여 서비스를 중지합니다.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="DLNA 서비스 중지" caption="DLNA 네트워크 공유 서비스 비활성화" width="500" >}}

## iPhone에서 DLNA 서버의 음악을 재생하는 방법

1. App Store에서 무료 **Evermusic** 앱을 설치합니다:  
   [Evermusic 앱](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. '연결' 탭을 열고 '로컬 네트워크' 섹션에서 '사용 가능한 장치'를 탭합니다.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Evermusic 연결" caption="Evermusic: 연결 화면" width="500" >}}

3. 장치 목록이 로드될 때까지 몇 초 기다린 다음 Windows Media Player DLNA 서버를 탭합니다(예: 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="사용 가능한 장치" caption="Evermusic에서 사용 가능한 DLNA 서버" width="500" >}}

4. 미디어 서버에서 사용 가능한 폴더 목록이 표시됩니다.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Evermusic 폴더" caption="DLNA 서버의 공유 폴더 탐색" width="500" >}}

5. 오디오 파일이 포함된 폴더를 엽니다.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="폴더 내용" caption="공유 DLNA 폴더의 내용 보기" width="500" >}}

6. 오디오 플레이어를 시작하려면 파일을 탭합니다.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="오디오 플레이어" caption="Evermusic에서 DLNA의 오디오 파일 재생" width="500" >}}

7. 오디오 경험을 향상시키려면 화면 하단의 볼륨 표시기 근처에 있는 '이퀄라이저' 아이콘을 탭하여 프리앰프가 있는 iPod 스타일 이퀄라이저를 활성화합니다.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="이퀄라이저" caption="내장 이퀄라이저로 향상된 재생" width="500" >}}

## 결론

Windows 10의 DLNA 미디어 서버와 iPhone의 Evermusic을 사용하면 컴퓨터에서 모바일 장치로의 원활한 음악 스트리밍을 즐길 수 있습니다. 저장 공간 제한에 작별을 고하고 온디맨드 음악을 환영하세요!

## 자주 묻는 질문

{{% details title="Windows 10에 서버 소프트웨어를 설치해야 하나요?" closed="true" %}}
아니요. Windows 10에는 내장 DLNA 미디어 서버가 포함되어 있습니다. 네트워크 및 공유 센터 설정에서 미디어 스트리밍만 활성화하면 됩니다. 타사 소프트웨어는 필요 없습니다.
{{% /details %}}

{{% details title="iPhone이 같은 Wi-Fi 네트워크에 있어야 하나요?" closed="true" %}}
예. DLNA 스트리밍은 로컬 네트워크에서 작동합니다. Evermusic이 DLNA 서버를 검색하려면 Windows 10 PC와 iPhone 모두 같은 Wi-Fi 네트워크에 연결되어 있어야 합니다.
{{% /details %}}

{{% details title="DLNA를 통해 어떤 오디오 형식을 스트리밍할 수 있나요?" closed="true" %}}
Windows DLNA 서버는 형식에 관계없이 음악 폴더의 파일을 공유합니다. Evermusic은 MP3, FLAC, AAC, WAV, OGG, AIFF 및 기타 많은 형식을 지원하므로 서버에서 거의 모든 오디오 파일을 재생할 수 있습니다.
{{% /details %}}

{{% details title="Evermusic 대신 Flacbox를 사용할 수 있나요?" closed="true" %}}
예. Flacbox도 DLNA/UPnP 탐색 및 재생을 지원합니다. 두 앱 중 하나를 사용하여 Windows DLNA 서버에서 음악을 검색하고 재생할 수 있습니다.
{{% /details %}}

{{% details title="DLNA 스트리밍이 모바일 데이터를 사용하나요?" closed="true" %}}
아니요. DLNA는 로컬 Wi-Fi 네트워크에서만 작동합니다. 모바일 데이터를 사용하지 않습니다. 단, 재생 중에는 두 장치 모두 같은 네트워크에 연결되어 있어야 합니다.
{{% /details %}}
