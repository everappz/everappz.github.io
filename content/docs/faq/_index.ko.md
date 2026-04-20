---
date: '2025-06-12T17:00:00+00:00'
draft: false
title: '자주 묻는 질문'
description: 'Evermusic, Flacbox, Evervideo, Evertag에 관한 일반적인 질문에 대한 답변을 찾아보세요. 클라우드 스트리밍, 파일 관리, 재생 옵션, 메타데이터 편집 등의 기능을 살펴보세요.'
keywords: [
  "Evermusic FAQ", "Flacbox 지원", "Evervideo 도움말", "Evertag 질문",
  "Evermusic 사용 방법", "클라우드 음악 플레이어 문제 해결", "오프라인 재생 가이드",
  "오디오 태그 편집기 지원", "비디오 스트리밍 문제", "파일 전송 튜토리얼"
]
tags: [
  "FAQ", "도움말", "지원", "evermusic", "flacbox", "evervideo", "evertag",
  "클라우드 설정", "재생 문제", "파일 관리", "메타데이터 편집",
  "문제 해결", "오프라인 모드", "음악 플레이어", "비디오 플레이어"
]
aliases:
  - /blog/categories/how-to/
---


{{< lottie src="/images/juicy-json/juicy-woman-focused-on-online-learning.json" width="85%" >}}

## 앱 사용 방법 알아보기

앱 중 하나에 대한 답변이나 도움이 필요하신가요? 올바른 곳에 오셨습니다.

FAQ 페이지는 클라우드 스토리지 연결, 음악 및 비디오 파일 관리, 오프라인 재생 설정, 이퀄라이저 설정 조정, 메타데이터 수정 등을 도와드립니다.

아래에서 앱의 FAQ를 탐색하여 시작하거나, 사용자 이메일에서 받은 일반적인 질문과 답변을 찾아보세요.

## 앱 선택

{{< cards cols="2">}}

{{< card 
  link="/docs/faq/evervideo" 
  title="Evervideo" 
  subtitle="360° 동영상 재생, iCloud에서 스트리밍, 자막으로 시청, 비디오 이퀄라이저 적용, 재생목록으로 콘텐츠 구성, 오프라인 시청을 위한 동영상 다운로드."
  image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< card 
  link="/docs/faq/evermusic"
  title="Evermusic" 
  subtitle="오프라인 모드, 오디오 이퀄라이저, 크로스페이드, 갭리스 재생, 재생목록 관리, 전체 음악 라이브러리 및 내장 파일 관리자를 갖춘 클라우드 음악 플레이어."
  image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/flacbox"
  title="Flacbox" 
  subtitle="iPhone 및 Mac용 고해상도 오디오 플레이어. FLAC, ALAC, APE, DSD와 같은 무손실 형식으로 음악을 들어보세요. 고급 오디오 설정으로 출력을 세밀하게 조정하세요."
  image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/evertag"
  title="Evertag" 
  subtitle="일괄 편집 기능이 있는 스마트 음악 태그 편집기. 누락된 메타데이터, 앨범 커버 등을 수정하세요. ID3, FLAC, APE 태그 편집 — 120개 이상의 필드 지원." 
  image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< /cards >}}

## 일반적인 문제 및 답변

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{% details title="이전 iOS 버전(15.8.4)에서 pCloud에 로그인할 수 없는 이유는 무엇인가요?" closed="true" %}}
pCloud 웹 로그인 페이지가 15.8.4와 같은 이전 iOS 버전에서 올바르게 표시되지 않아 클라우드 연결 화면에서 이메일과 비밀번호를 입력할 수 없을 수 있습니다.<br><br>

해결 방법으로 pCloud에서 지원하며 모든 iOS 버전에서 안정적으로 작동하는 **WebDAV** 프로토콜을 사용할 수 있습니다.

**WebDAV 설정:**<br>
- **미국 서버:** `https://webdav.pcloud.com`  
- **유럽 서버:** `https://ewebdav.pcloud.com`  
- **사용자 이름:** pCloud 이메일 주소  
- **비밀번호:** pCloud 계정 비밀번호  

앱 열기 → 연결 → 클라우드 스토리지 연결 → **WebDAV** 선택 → 자격 증명 및 서버 URL 입력.

이 방법으로 이전 기기에서도 문제 없이 pCloud 스토리지에 연결하고 파일에 접근할 수 있습니다.
{{% /details %}}

{{% details title="Mac(macOS)에서 AirPlay로 음악을 재생하는 방법은?" closed="true" %}}
앱의 macOS 버전에는 iOS처럼 내장된 AirPlay, Chromecast 또는 Bluetooth 연결 버튼이 없습니다.<br><br>

MacBook Pro에서 **AirPlay**를 사용하려면 다음 단계를 따르세요:

1. 화면 **오른쪽 상단 모서리**로 이동하여 **제어 센터**(시계 근처)를 엽니다.  
2. **사운드/볼륨** 아이콘을 클릭합니다.  
3. 다음 화면에서 **AirPlay**를 클릭하여 사용 가능한 모든 AirPlay 기기 목록을 봅니다.  
4. 원하는 기기를 선택하여 음악 스트리밍을 시작합니다.  

이렇게 하면 모든 시스템 오디오(Evermusic 또는 Flacbox 포함)가 선택한 AirPlay 기기로 전달됩니다.
{{% /details %}}

{{% details title="iPhone에서 구매한 프리미엄이 Mac에서 활성화되지 않는 이유는?" closed="true" %}}
평생 구매 및 구독은 **iCloud**를 통해 iOS와 Mac 간에 동기화됩니다.<br><br>

Mac에서 프리미엄을 활성화하려면:<br>
- 두 기기 모두에 최신 앱 버전이 설치되어 있는지 확인하세요<br>
- 두 기기 모두에서 **iCloud**를 활성화하세요<br>
- iOS 기기에서 앱을 실행하고 구매 정보가 업로드될 때까지 1분 기다리세요<br>
- Mac에서 **동일한 Apple ID**를 사용하여 App Store에서 앱을 설치하세요<br>
- 앱을 실행하고 정보가 동기화될 때까지 몇 초 기다리세요<br>
- 또는 두 기기 앱 설정에서 **구매 복원**을 탭하세요<br><br>

그러면 Mac에서 프리미엄 기능이 자동으로 활성화됩니다.
{{% /details %}}

{{% details title="기기 간에 재생목록을 자동으로 동기화할 수 있나요?" closed="true" %}}
현재 재생목록에 대한 **자동 동기화는 없습니다**.<br><br>

다음 옵션 중 하나를 사용할 수 있습니다:<br>
- 앱 설정에서 **백업 및 복원** [Evermusic에서 기기 간 음악 라이브러리 전송 방법: 단계별 가이드](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/)<br>
- **재생목록을 M3U로 내보내기**, 다른 기기에서 가져오기:<br>
  - [재생목록 내보내기 방법](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/)<br>
  - [재생목록 가져오기 방법](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/)<br>
- **재생목록 또는 앨범을 ZIP으로 아카이브**하여 전송:<br>
  - [재생목록 아카이브 가이드](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to/)
{{% /details %}}

{{% details title="앱을 사용해도 안전한가요? 분석을 비활성화할 수 있나요?" closed="true" %}}
네, 귀하의 개인 정보 보호가 최우선입니다.<br><br>

- 음악 파일, 설정, 클라우드 로그인 등 모든 데이터는 기기에 저장됩니다<br>
- 로그인 자격 증명은 **iOS Keychain**에 안전하게 저장됩니다<br>
- 익명 충돌 및 사용 보고서만 수집합니다<br>
- **앱 설정 → 분석**에서 옵트아웃할 수 있습니다<br><br>

추가 정보:<br>
- [개인 정보 처리 방침](/legal/privacy-policy/)<br>
- [Apple Keychain 보안](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web)<br><br>

개인화된 광고를 사용하는 경우 Google Mobile Ads는 동의 설정을 표시해야 합니다.<br>
프리미엄 사용자는 광고가 없으며 광고 SDK가 완전히 비활성화됩니다.
{{% /details %}}

{{% details title="앱이 가족 공유를 지원하나요?" closed="true" %}}
네, 가족 공유가 지원됩니다.<br><br>

앱 내 구매를 공유하려면:<br>
- 구매가 가족 그룹과 공유되도록 설정되어 있는지 확인하세요<br>
- 가족 구성원의 기기에서 **설정 > 구매 > 구매 복원**으로 이동하세요<br>
- Apple 서버에서 구매 데이터를 요청하여 해당 기기에서 활성화합니다
{{% /details %}}

{{% details title="메타데이터 및 클라우드 동기화 속도를 높이는 방법은?" closed="true" %}}
동기화 속도를 향상시키려면 백그라운드 작업을 활성화하세요:<br><br>

- **설정 → 음악 라이브러리 → 메타데이터 읽기 → 백그라운드에서 메타데이터 읽기**<br>
- **설정 → 음악 라이브러리 → 온라인 음악 동기화 → 백그라운드 동기화**<br><br>

또한 macOS에서는 **설정 → 음악 라이브러리**를 통해 메타데이터 읽기 속도를 높이세요.<br>
플레이어가 활성 상태(오디오 재생 중)이면 iOS가 앱을 일시 중단하지 않아 지속적인 동기화가 가능합니다.
{{% /details %}}

{{% details title="구독을 취소하는 방법은?" closed="true" %}}
Apple의 공식 안내에서 구독을 취소할 수 있습니다:<br>
👉 [구독 취소 방법](https://support.apple.com/en-us/118428)
{{% /details %}}

{{% details title="WD MyCloud EX2 Ultra에서 오디오를 연결하고 스트리밍하는 방법은?" closed="true" %}}

앱에서 **연결 > 클라우드 스토리지 연결 > My Cloud Home**을 통해 연결을 추가하면 공식적으로 **WD MyCloud Home** 기기를 지원하도록 설계되어 있습니다.<br>
WD MyCloud EX2 Ultra는 앱의 접근을 제한합니다.<br><br>

하지만 **WD MyCloud EX2 Ultra**, **WD MyCloud Mirror** 또는 다른 **WD MyCloud** 스토리지 모델에 성공적으로 연결한 경우 다음 해결 방법으로 사용할 수 있습니다:<br><br>

1. **연결 → 클라우드 스토리지 연결 → My Cloud Home** 열기<br>
2. 내장 파일 관리자를 사용하여 폴더 만들기<br>
3. 이 폴더에 음악 파일 업로드<br>
4. 이 파일들은 앱만 접근할 수 있는 "샌드박스"에 저장됩니다<br>
5. 이제 직접 스트리밍하거나 다운로드할 수 있습니다<br><br>

⚠️ 앱을 통해 만든 폴더만 NAS에서 접근할 수 있습니다.
{{% /details %}}

{{% details title="Koofr.eu에 연결하는 방법은?" closed="true" %}}
**WebDAV**를 사용하여 Koofr에 연결할 수 있습니다.<br><br>

- Koofr WebDAV 설정 가이드: [koofr.eu 블로그](https://koofr.eu/blog/posts/3-ways-to-map-koofr-as-a-network-drive-explained)<br>
- Evermusic/Flacbox WebDAV 가이드: [WebDAV를 사용하여 NAS 스토리지에 연결하고 iPhone 또는 Mac에서 음악 듣는 방법](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)
{{% /details %}}

{{% details title="앱 URL 스킴은 무엇인가요?" closed="true" %}}
지원되는 스킴은 다음과 같습니다:<br><br>

**Evermusic**<br>
- iOS (파란 아이콘): `lsevermusic://`<br>
- macOS: `lsevermusicmac://`<br>
- iOS (빨간 아이콘): `lsevermusicpro://`<br><br>

**Flacbox**<br>
- iOS: `lsflap://`<br>
- macOS: `lsflapmac://`<br><br>

**Evertag**<br>
- iOS: `lsevertag://`<br>
- macOS: `lsevertagmac://`<br><br>

**Evervideo**<br>
- iOS: `lsevervideo://`<br>
- macOS: `lsevervideomac://`
{{% /details %}}

{{% details title="앱이 백그라운드에서 음악 재생을 멈추는 경우 해결 방법은?" closed="true" %}}
앱이 백그라운드에서 충돌하거나 일시 중지되는 경우:<br>
- **설정 > 음악 라이브러리 > 온라인 음악 동기화 > 백그라운드 동기화 → 비활성화**로 이동하세요<br>
- **설정 > 음악 라이브러리 > 메타데이터 읽기 > 백그라운드에서 메타데이터 읽기 → 비활성화**<br>
- **설정 > 파일 관리자 > 백그라운드 전송 → 비활성화**
{{% /details %}}

{{% details title="갭리스 재생이 작동하지 않는 경우 해결 방법은?" closed="true" %}}
갭리스 재생은 iOS 버전 및 오디오 엔진에 따라 다릅니다.<br>
오디오 엔진을 변경해 보세요:<br>
- **설정 → 오디오 플레이어 → 일반 → 오디오 프로세서**로 이동하세요<br>
- 더 나은 갭리스 지원을 위해 **Core Audio**를 선택하세요
{{% /details %}}

{{% details title="앱에서 목록에 100개 항목만 표시되는 이유는?" closed="true" %}}
앱은 성능을 위해 페이지네이션을 사용합니다.<br>
비활성화하려면:<br>
- **설정 → 개인화 → 콘텐츠 로딩 제한 → 비활성화됨**으로 이동하세요<br>
이제 모든 항목이 한 번에 로드됩니다.
{{% /details %}}

{{% details title="메타데이터에 이상한 문자가 나타나는 이유는?" closed="true" %}}
메타데이터 정규화를 활성화해 보세요:<br>
- **설정 → 음악 라이브러리 → 메타데이터 읽기 → 메타데이터 인코딩 정규화**
{{% /details %}}

{{% details title="앱이 특수 문자가 포함된 폴더 이름을 읽을 수 없는 이유는?" closed="true" %}}
이것은 **SMB2 프로토콜**의 알려진 문제입니다.<br><br>

다음 해결 방법을 시도해 보세요:<br>
- 서버 및 앱 설정에서 **SMB1**을 활성화하세요<br>
- **시스템 파일 선택기**를 사용하세요:<br>
  - **로컬 파일 > 이 기기의 파일 > 파일 열기...**로 이동하세요<br>
  - Apple의 기본 메뉴를 사용하여 폴더/파일을 선택하세요<br><br>

또는 NAS가 지원하는 경우 **WebDAV** 또는 **DLNA**를 사용하여 연결하세요.
{{% /details %}}

{{% details title="iCloud에서 음악을 업로드하고 관리하는 방법은?" closed="true" %}}
– **iCloud에 음악을 업로드하는 방법은?**  <br>
브라우저에서 [https://www.icloud.com](https://www.icloud.com)으로 이동하여 폴더를 만들고 Mac 또는 PC에서 직접 음악 파일을 업로드하세요.<br>

– **iCloud 저장 공간을 관리하는 방법은?**  <br>
두 가지 옵션이 있습니다:  <br>
1. 브라우저에서 [https://www.icloud.com](https://www.icloud.com)을 사용하여 파일을 정리, 업로드 또는 삭제하세요.<br>  
2. 앱에서 **연결 → 클라우드 스토리지 연결 → iCloud Drive**를 통해 iCloud에 연결한 후 내장 파일 관리자를 사용하여 기기에 저장하지 않고 iCloud 저장 공간에서 직접 파일을 업로드, 다운로드, 폴더 이름 변경 또는 삭제하세요.<br>

⚠️ 파일 삭제 시 주의하세요. 앱은 파일을 영구적으로 삭제합니다(휴지통으로 이동하지 않으며 복구할 수 없습니다).<br>

자세한 내용은 여기에서 확인하세요: [iPhone 또는 Mac에서 iCloud Drive의 음악을 스트리밍하는 방법](/docs/howto/how-to-listen-to-music-from-icloud-drive-on-your-iphone-or-mac/)

{{% /details %}}

{{% details title="Windows 11에서 10GB 음악 라이브러리를 iPhone으로 전송하여 오프라인으로 재생하는 방법은?" closed="true" %}}

Windows 11 PC에서 iPhone으로 음악 라이브러리를 이동하고 앱에서 오프라인으로 사용할 수 있는 여러 가지 방법이 있습니다. 가장 적합한 방법을 선택하세요:

1. **케이블 연결 사용(대용량 라이브러리에 권장)**  <br>
   Windows 11에서 **Apple Devices** 앱을 사용하여 USB를 통해 iPhone으로 직접 파일을 전송하세요.  
   Apple 가이드를 따르세요:  
   https://support.apple.com/en-ph/120402 <br>

2. **Wi-Fi Drive를 통한 무선 전송**  <br>
   앱 내에서 **WiFi Drive** 기능을 활성화하고 컴퓨터의 브라우저를 통해 음악을 업로드하세요.  
   단계별 안내:  
   [iTunes 없이 WiFi-Drive를 사용하여 컴퓨터에서 iPhone으로 음악 파일을 전송하는 방법](/docs/howto/how-to-transfer-music-from-computer-to-iphone-without-itunes/) <br>

3. **DLNA 서버를 사용한 무선 전송**  <br>
   Windows 컴퓨터에서 DLNA 미디어 서버를 켜고 앱으로 직접 라이브러리를 스트리밍하거나 전송하세요.  
   가이드:  
   [Windows 10에서 DLNA 미디어 서버를 활성화하고 iPhone에서 음악을 재생하는 방법](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/) <br>

4. **SMB 파일 공유를 사용한 무선 전송**  <br>
   PC에서 **SMB 파일 공유**를 활성화하고 앱에서 연결하여 폴더별로 파일을 탐색, 다운로드 또는 전송하세요.  
   안내:  
   [SMB 프로토콜을 사용하여 컴퓨터에서 iPhone으로 파일 전송](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/) <br>

⚠️ 대용량 라이브러리(10GB+)를 전송할 때는 유선 USB 전송이 일반적으로 가장 빠르고 안정적인 옵션입니다.

{{% /details %}}

</div>
