---
title: "Synology NAS를 연결하고 iPhone 또는 Mac에서 음악을 듣는 방법"
date: 2024-09-19
description: "Synology NAS를 네이티브 API 또는 QuickConnect로 연결하고 Evermusic 및 Flacbox를 사용하여 iPhone 또는 Mac에서 고품질 음악을 스트리밍하는 방법을 알아보세요."
keywords: ["synology nas", "음악 스트리밍", "quickconnect", "evermusic synology", "flacbox synology", "nas 음악 플레이어", "iphone nas 음악"]
tags: ["음악", "스트리밍", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**요약:** Synology의 네이티브 API를 사용하여 Synology NAS를 Evermusic 또는 Flacbox에 연결하세요 -- IP 주소를 통한 수동 연결 또는 QuickConnect ID를 통한 자동 연결이 가능합니다. QuickConnect를 사용하면 포트 포워딩 없이 원격으로 음악을 스트리밍할 수 있습니다. 두 앱 모두 FLAC, MP3, WAV 및 기타 고해상도 형식을 지원합니다.

Synology NAS를 연결하고 iPhone 또는 Mac에서 음악 라이브러리를 즐길 수 있는 원활한 방법을 찾고 계신다면, Evermusic 및 Flacbox 앱이 완벽한 솔루션입니다. 이 앱들은 FLAC, MP3, WAV를 포함한 다양한 오디오 형식을 지원하여 Synology NAS에서 고품질 음악을 쉽게 스트리밍하고 들을 수 있습니다.

이 가이드에서는 Synology의 네이티브 API 및 QuickConnect 기능을 사용하여 Synology NAS를 Evermusic 또는 Flacbox 앱에 연결하는 방법을 보여드리겠습니다. Synology의 직접 API를 활용하면 WebDAV, SMB, DLNA와 같은 복잡한 구성 없이도 홈 네트워크 외부에서 안전하게 음악 라이브러리에 액세스할 수 있습니다. QuickConnect를 사용하면 iPhone 또는 Mac을 사용하여 어디서든 음악을 스트리밍하고 관리할 수 있습니다.

## 1단계: 공유 폴더 권한 구성 (선택 사항)

1. **제어판**을 열고 **공유 폴더** 섹션으로 이동합니다.

![공유 폴더](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. **Music** 폴더를 선택하고 **편집**을 클릭합니다.

3. **권한** 탭에서 권한을 구성합니다. 음악을 듣기만 하면 되는 경우 읽기 전용으로 게스트 액세스를 활성화하고, 파일을 수정해야 하는 경우 읽기/쓰기를 활성화합니다. 변경 사항을 저장합니다.

![권한](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## 2단계: Synology NAS IP 주소 찾기

1. **제어판**을 열고 **네트워크 인터페이스** 탭으로 이동합니다.

![네트워크 인터페이스](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. 또는 웹 브라우저를 사용하여 [find.synology.com](http://find.synology.com)을 방문합니다.

![Synology 찾기](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Synology NAS의 IP 주소를 메모합니다 (예: 192.168.18.137).

## 3단계: Synology NAS 네트워크 포트 찾기

Synology DSM 기본 네트워크 포트에 대한 공식 Synology 문서는 이 [Synology 지식 센터 문서](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services)에서 찾을 수 있습니다.

Synology DSM은 다음 기본 포트를 사용합니다:
- **HTTP (웹 액세스):** 포트 **5000**
- **HTTPS (보안 웹 액세스):** 포트 **5001**

이것은 DSM 인터페이스에 액세스하기 위한 기본 포트입니다.

![네트워크 포트](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## 4단계: QuickConnect ID 기능 활성화

Synology QuickConnect ID는 포트 포워딩과 같은 복잡한 네트워크 설정을 구성할 필요 없이 인터넷을 통해 Synology NAS에 원격으로 액세스할 수 있게 해주는 고유 식별자입니다. QuickConnect는 Synology의 서버를 사용하여 QuickConnect ID를 통해 NAS와 스마트폰이나 컴퓨터와 같은 장치 간의 연결을 설정하여 원격 액세스를 간소화합니다.

**QuickConnect ID를 찾거나 설정하는 방법:**

1. **DSM에 로그인합니다.**
2. **제어판 > 외부 액세스 > QuickConnect**로 이동합니다.
3. **QuickConnect를 활성화**하고 고유한 QuickConnect ID를 생성하거나 확인합니다.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## 5단계: Evermusic 또는 Flacbox를 사용하여 iPhone/Mac에서 Synology NAS에 연결

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) 및 [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256)는 iOS 및 macOS 장치용으로 설계된 음악 플레이어 앱으로, 각각 음악 라이브러리를 관리하고 즐기기 위한 고유한 기능과 성능을 제공합니다.

1. Evermusic 또는 Flacbox 앱을 열고 **연결하기** 탭으로 이동합니다.

![연결하기](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. **클라우드 서비스 연결**을 선택하고 **Synology Drive**를 선택합니다.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

두 가지 연결 옵션이 있습니다: 서버의 IP 주소와 포트를 사용한 **수동** 연결 또는 QuickConnect ID를 통한 **자동** 연결.

### 수동 연결

수동 방법의 경우 이전 단계에서 확인한 직접 IP 주소와 포트 번호가 필요합니다.

1. 2단계에서 얻은 서버 URL을 다음 형식으로 입력합니다: PROTOCOL://IP_ADDRESS:PORT_NUMBER
   - HTTP 연결에는 **포트 5000**을, HTTPS 연결에는 **포트 5001**을 사용합니다.

   예:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. 실제 포트 번호는 설정의 3단계에서 확인할 수 있습니다.
3. Synology NAS의 **로그인**과 **비밀번호**를 입력합니다.
4. **로그인**을 탭하여 연결을 설정합니다.

![수동 연결](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### 자동 연결

자동 연결의 경우 4단계의 **QuickConnect ID**를 사용합니다. Synology NAS의 IP 주소와 포트 번호를 수동으로 입력하는 대신 **QuickConnect ID**만 입력하면 됩니다. 앱이 자동으로 필요한 연결 정보를 검색합니다.

이 방법을 사용하면 홈 네트워크 외부에서도 NAS에 원격으로 액세스할 수 있으므로 포트 포워딩이나 고정 IP 주소를 구성할 필요 없이 인터넷에서 파일을 관리할 수 있습니다.

![자동 연결](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## 2단계 인증

DSM 4.2부터 Synology는 보안을 강화하기 위해 **2단계 인증**을 도입했습니다. 이 기능은 일반 로그인 자격 증명 외에 인증 앱에서 생성된 **일회용 비밀번호 (OTP)** 코드가 필요합니다. 2단계 인증을 활성화한 경우, 사용자 이름과 비밀번호를 입력한 후 OTP를 입력하여 DSM 세션에 로그인해야 합니다.

세션이 만료되면 앱을 수동으로 다시 인증해야 합니다. 재인증하려면:

1. 앱에서 **연결하기** 탭으로 이동합니다.
2. 서버 이름 옆의 **추가 작업** 버튼을 탭합니다.
3. 메뉴에서 **설정**을 선택하여 새 인증 코드를 입력하고 재인증 프로세스를 완료합니다.

이렇게 하면 신뢰할 수 없는 네트워크에서 NAS에 액세스하더라도 데이터가 안전하게 유지됩니다.

## 6단계: 음악 탐색 및 재생

1. 연결되면 장치가 **연결된 장치** 목록에 표시됩니다.

![연결된 장치](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. **Music** 폴더로 이동하여 오디오 파일을 탭하면 재생이 시작됩니다.

![음악 재생](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## 7단계: 연결된 클라우드 폴더를 음악 라이브러리에 추가

1. 앱에서 **음악 라이브러리** 섹션을 엽니다.
2. **음악 추가**를 선택하고 **연결하기**를 선택합니다.
3. 연결된 NAS 서버를 선택하고 **Music** 폴더를 선택합니다. **완료됨**을 탭합니다.
4. 앱이 음악 폴더를 스캔하고 지원되는 오디오 파일을 음악 라이브러리에 추가합니다. 메타데이터가 로드되고 트랙이 앨범, 아티스트 및 장르별로 그룹화됩니다.

## 결론

이 단계를 따르면 Synology NAS에서 쉽게 연결을 설정하고 Evermusic 또는 Flacbox를 사용하여 전체 음악 라이브러리를 iPhone 또는 Mac으로 스트리밍할 수 있습니다. 집에 있든 이동 중이든 QuickConnect를 사용하여 어디서든 좋아하는 트랙에 원활하고 고품질로 액세스하세요. 이 앱들이 제공하는 유연성과 편의성을 활용하여 모든 장치에서 음악 컬렉션을 쉽게 관리하세요.

QuickConnect를 통한 안전한 원격 액세스와 다양한 오디오 형식 지원으로 음악에서 멀리 떨어질 일이 없습니다. 이제 NAS에 저장된 파일이 탭 한 번이면 됩니다!

## FAQ

{{% details title="수동 연결과 QuickConnect의 차이점은 무엇인가요?" closed="true" %}}
수동 연결은 NAS IP 주소와 포트를 사용하며 로컬 네트워크에서 작동합니다. QuickConnect는 Synology의 릴레이 서비스를 사용하여 포트 포워딩 없이 인터넷을 통해 어디서든 연결을 설정합니다.
{{% /details %}}

{{% details title="홈 네트워크 외부에서 Synology NAS의 음악을 스트리밍할 수 있나요?" closed="true" %}}
예. Synology NAS에서 QuickConnect를 활성화하고 Evermusic 또는 Flacbox에서 QuickConnect ID를 사용하면 인터넷 연결이 있는 곳이면 어디서든 음악을 스트리밍할 수 있습니다.
{{% /details %}}

{{% details title="Synology NAS에서 스트리밍할 때 어떤 오디오 형식이 지원되나요?" closed="true" %}}
Evermusic 및 Flacbox는 FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD 및 기타 많은 형식을 지원합니다. Synology NAS에서 스트리밍할 때 모든 지원 형식이 작동합니다.
{{% /details %}}

{{% details title="연결하려면 2단계 인증이 필요한가요?" closed="true" %}}
아니요, 2단계 인증은 선택 사항입니다. 그러나 Synology DSM에서 2단계 인증을 활성화한 경우 앱에서 로그인 시 일회용 비밀번호를 요청합니다. 세션이 만료되면 재인증이 필요합니다.
{{% /details %}}

{{% details title="연결에 Synology 네이티브 API, WebDAV 또는 SMB 중 무엇을 사용해야 하나요?" closed="true" %}}
QuickConnect가 포함된 Synology 네이티브 API가 원격 액세스에 가장 좋은 선택입니다. 로컬 네트워크 사용의 경우 SMB가 일반적으로 가장 빠른 옵션입니다. WebDAV는 로컬 및 원격 액세스 모두에 잘 작동합니다. Evermusic 및 Flacbox는 세 가지 프로토콜을 모두 지원합니다.
{{% /details %}}
