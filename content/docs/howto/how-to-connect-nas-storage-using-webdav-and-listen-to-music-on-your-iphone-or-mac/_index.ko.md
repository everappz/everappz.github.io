---
title: "WebDAV를 사용하여 NAS 스토리지를 연결하고 iPhone 또는 Mac에서 음악 듣는 방법"
date: 2024-07-28
description: "Synology NAS에서 WebDAV를 구성하고 Evermusic 또는 Flacbox를 사용하여 iPhone이나 Mac으로 음악을 스트리밍하는 방법을 알아보세요. 단계별 가이드를 따라해 보세요."
keywords: ["nas 연결", "webdav synology", "음악 스트리밍 nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["음악", "스트리밍", "스토리지", "nas", "연결", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**요약:** Synology NAS에 WebDAV를 설치하고 활성화하고, 공유 폴더 권한을 구성한 다음, NAS IP 주소와 WebDAV 포트(기본값 5005/5006)를 사용하여 Evermusic 또는 Flacbox에서 연결합니다. 기기에 파일을 복사하지 않고도 전체 음악 라이브러리를 스트리밍하고 관리할 수 있습니다.

WebDAV를 사용하여 NAS 스토리지를 연결하고 음악 라이브러리를 iPhone이나 Mac으로 손쉽게 스트리밍하는 방법을 알아보세요. WebDAV(Web-based Distributed Authoring and Versioning)는 인터넷을 통해 파일을 관리하고 공유할 수 있는 프로토콜입니다. NAS에 WebDAV를 설정하면 음악 컬렉션에 접근하고 스트리밍할 수 있어 좋아하는 곡을 항상 손끝에서 즐길 수 있습니다.

이 가이드에서는 가장 인기 있는 NAS 서버 중 하나인 Synology NAS에서 WebDAV 연결을 설정하는 방법을 보여드립니다. Synology NAS에서 WebDAV를 구성하는 간단한 단계를 따르면 iPhone이나 Mac에서 직접 음악 라이브러리를 탐색, 스트리밍 및 관리할 수 있습니다.

## 1단계: Synology NAS에 WebDAV 설치

1. Synology NAS에 로그인하고 **패키지 센터**를 엽니다.
2. "webdav"를 검색하고 아직 설치되지 않은 경우 WebDAV 패키지를 설치합니다. WebDAV 서버를 열어 구성합니다.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Synology에 WebDAV 설치" width="600" >}}

## 2단계: WebDAV 서버 구성

1. WebDAV 설정 페이지에서 **HTTP 활성화**, **HTTPS 활성화**, **익명 WebDAV 활성화**, **DavDepthInfinity 활성화** 확인란을 선택합니다.
2. **적용**을 클릭하여 변경 사항을 저장합니다. HTTP 및 HTTPS 연결의 포트 번호를 확인하세요. 기본값은 5005와 5006입니다.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="WebDAV 설정 구성" width="600" >}}

## 3단계: 공유 폴더 권한 구성

1. **제어판**을 열고 **공유 폴더** 섹션으로 이동합니다.
2. **음악** 폴더를 선택하고 **편집**을 클릭합니다.
3. **권한** 탭에서 권한을 구성합니다. 음악만 들으려면 읽기 전용으로 게스트 액세스를 활성화하고, 파일을 수정해야 하면 읽기/쓰기로 활성화합니다. 변경 사항을 저장합니다.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="공유 폴더 권한" width="600" >}}

## 4단계: Synology NAS IP 주소 찾기

1. **제어판**을 열고 **네트워크 인터페이스** 탭으로 이동하거나, 웹 브라우저를 사용하여 [find.synology.com](http://find.synology.com)을 방문합니다.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="NAS IP 주소 찾기" width="600" >}}

2. Synology NAS의 IP 주소를 메모합니다(예: 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Synology NAS IP 주소" width="600" >}}

## 5단계: Evermusic/Flacbox로 Synology NAS에 연결

1. Evermusic 또는 Flacbox 앱을 열고 **연결하기** 탭으로 이동합니다.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Evermusic의 연결하기 탭" width="600" >}}

2. 자동 연결의 경우, **사용 가능한 장치** 섹션에서 Synology NAS를 찾아 탭하여 연결합니다.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="사용 가능한 장치 목록" width="600" >}}

3. 수동 연결의 경우, **클라우드 서비스 연결**을 선택하고 **WebDAV**를 선택합니다. 서버 주소를 다음 형식으로 입력합니다: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER(예: [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="수동 WebDAV 구성" width="600" >}}

4. 게스트 액세스의 경우 로그인과 비밀번호 필드를 비워두거나, Synology 자격 증명을 입력합니다. **로그인**을 탭합니다.

## 6단계: 음악 탐색 및 재생

1. 연결되면 장치가 **연결된 액세서리** 목록에 나타납니다.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Evermusic의 연결된 장치" width="600" >}}

2. **음악** 폴더로 이동하고 오디오 파일을 탭하여 재생을 시작합니다.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="음악 폴더 탐색" width="600" >}}

## 7단계: 연결된 클라우드 폴더를 음악 라이브러리에 추가

1. 앱에서 **음악 라이브러리** 섹션을 엽니다.
2. **음악 추가**를 선택하고 **연결하기**를 선택합니다.
3. 연결된 NAS 서버를 선택하고 **음악** 폴더를 선택합니다. **완료됨**을 탭합니다.
4. 앱이 음악 폴더를 스캔하고 지원되는 오디오 파일을 음악 라이브러리에 추가합니다. 메타데이터가 로드되고 트랙이 앨범, 아티스트, 장르별로 그룹화됩니다.

## 결론

이 단계를 따르면 Synology NAS에 WebDAV 연결을 쉽게 설정하고 Evermusic 또는 Flacbox를 사용하여 iPhone이나 Mac으로 음악 라이브러리를 스트리밍할 수 있습니다. 언제든지 좋아하는 트랙에 원활하게 접근하세요.

## FAQ

{{% details title="어떤 NAS 장치가 WebDAV를 지원하나요?" closed="true" %}}
Synology, QNAP, TrueNAS, Western Digital을 포함한 대부분의 인기 NAS 브랜드가 WebDAV를 지원합니다. WebDAV 설정 지침은 NAS 제조업체의 문서를 확인하세요.
{{% /details %}}

{{% details title="NAS 음악 스트리밍에서 WebDAV와 SMB의 차이점은 무엇인가요?" closed="true" %}}
WebDAV는 HTTP/HTTPS를 통해 작동하며 인터넷을 통한 원격 액세스에 더 적합합니다. SMB는 일반적으로 로컬 네트워크에서 더 빠릅니다. Evermusic과 Flacbox는 두 프로토콜을 모두 지원하므로, 로컬 또는 원격 액세스 필요에 따라 선택하세요.
{{% /details %}}

{{% details title="Synology에서 WebDAV에 사용자 이름과 비밀번호가 필요한가요?" closed="true" %}}
익명 WebDAV 액세스를 활성화하고 공유 폴더에 게스트 권한을 구성하면 필요하지 않습니다. 보안을 강화하려면 Synology 자격 증명을 대신 사용할 수 있습니다.
{{% /details %}}

{{% details title="WebDAV를 통해 NAS에서 FLAC 및 기타 고해상도 포맷을 스트리밍할 수 있나요?" closed="true" %}}
네. Evermusic과 Flacbox 모두 WebDAV를 통해 NAS 스토리지에서 스트리밍할 때 FLAC, ALAC, WAV, DSD 및 기타 고해상도 포맷을 지원합니다.
{{% /details %}}

{{% details title="사용 가능한 장치에서 내 NAS를 찾을 수 없는 이유는 무엇인가요?" closed="true" %}}
iPhone/Mac과 NAS가 같은 Wi-Fi 네트워크에 있는지 확인하세요. 자동 검색이 작동하지 않으면 수동 연결 옵션을 사용하여 NAS IP 주소와 WebDAV 포트를 직접 입력하세요.
{{% /details %}}
