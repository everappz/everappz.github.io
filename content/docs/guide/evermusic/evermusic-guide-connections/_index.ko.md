---
title: "연결하기"
date: 2020-01-01
description: "Evermusic를 사용하여 클라우드 서비스, 컴퓨터, NAS 장치를 연결하고 음악 파일을 관리하는 방법을 알아보세요. Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes File Sharing 등에 대한 단계별 가이드."
keywords: [
  "Evermusic", "클라우드 음악 플레이어", "NAS 스트리밍", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes File Sharing",
  "클라우드 스토리지 연결", "iPhone 음악 전송", "iOS 파일 관리자"
]
tags: ["evermusic", "가이드", "연결"]
readingTime: 11
---


연결하기 화면에서 음악이 저장된 모든 소스를 연결할 수 있습니다 — 인기 클라우드 서비스, 자체 호스팅 미디어 서버, Mac 또는 PC, 개인 NAS, Apple Time Capsule, WD My Cloud Home, USB 플래시 드라이브까지 — 모두 하나의 통합된 인터페이스에서 사용할 수 있습니다. 연결하기는 깊이 중첩된 클라우드 폴더에 대한 빠른 접근을 설정하고 스크로블링을 위해 Last.fm을 인증하는 곳이기도 합니다.

화면은 명확하게 레이블이 붙은 섹션으로 나뉘어 있어 단일 iCloud Drive 계정부터 여러 클라우드와 NAS 장치에 걸친 라이브러리까지 확장됩니다: 상단의 빠른 접근(즐겨찾는 클라우드 폴더), 클라우드 스토리지(추가한 계정), 로컬 네트워크(Bonjour로 검색된 장치), 컴퓨터(Wi-Fi Drive, iTunes File Sharing, SMB), 외부 액세서리(연결된 USB 플래시 드라이브), 기타 서비스(Last.fm 등).

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic 연결하기 화면" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## 클라우드 스토리지에 연결

- 연결하기 탭을 엽니다.
- 메뉴에서 클라우드 스토리지에 연결을 선택합니다.
- 목록에서 클라우드 스토리지 서비스를 선택합니다.
- 공급자의 공식 인증 페이지에서 로그인합니다(Evermusic는 비밀번호를 절대 볼 수 없습니다).
- 완료됨을 탭합니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="클라우드 스토리지 공급자 선택기 연결" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

문제가 발생하면 인터넷 연결과 로그인 자격 증명을 다시 확인하고, 해당 서비스에 대한 이중 인증이 올바르게 구성되어 있는지 확인하세요.  
앱의 프리미엄 버전에서는 무제한 수의 서비스를 추가할 수 있습니다. 무료 사용자는 한 번에 단일 클라우드 계정만 연결할 수 있습니다.

## 지원되는 클라우드 스토리지 서비스

Evermusic는 인기 있는 클라우드 및 자체 호스팅 서비스의 전체 라인업을 지원합니다. 무료 사용자는 동일한 공급자 카탈로그를 사용하지만 하나의 계정 제한이 있습니다; 프리미엄은 무제한 계정을 잠금 해제하고 대부분의 다른 제한을 제거합니다.

- **개인 클라우드 계정:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **자체 호스팅 서버 및 미디어 라이브러리:** Plex · Jellyfin · Emby · Subsonic(모든 Subsonic 호환 서버 포함 — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud(공유 API를 통한 Owncloud 포함) · Synology Drive · QNAP.
- **NAS 및 파일 공유 프로토콜:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (비밀번호 또는 공개키 인증), NFS, DLNA (읽기 전용 — 재생 및 다운로드).
- **S3 호환 오브젝트 스토리지:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage, 또는 모든 S3 API 엔드포인트.
- **로컬 네트워크 검색:** 사용 가능한 장치 섹션은 Bonjour / mDNS를 통해 자신을 광고하는 Wi-Fi의 모든 장치를 자동으로 나열합니다 — Plex, Jellyfin, Emby 서버, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, 드라이브가 연결된 AirPort 라우터 등.

## 보안 및 개인 정보 보호

연결된 클라우드 서비스와 상호 작용하기 위해 공식 SDK와 보안 연결만 사용합니다. 로그인 및 비밀번호는 응용 프로그램에서 사용할 수 없습니다. 응용 프로그램에서 클라우드 서비스로의 모든 요청은 암호화됩니다.

로그인 및 비밀번호를 입력하면 응용 프로그램은 클라우드 서비스 공급자가 제공하는 공식 인증 페이지를 표시하며, 모든 인증 프로세스는 응용 프로그램 외부에서 이루어집니다. 클라우드 서비스 공급자는 성공적인 인증 후 응용 프로그램에 인증 토큰을 보내고 해당 토큰은 API 호출을 하는 데 사용됩니다.

인증 토큰은 타사 응용 프로그램이 클라우드 스토리지와 상호 작용할 수 있도록 하는 디지털 키입니다. 인증 토큰은 Keychain이라는 보안 시스템 스토리지의 장치에 저장됩니다. 연결된 클라우드 서비스에서 장치로 파일을 다운로드할 수 있으며, 이러한 파일은 앱의 '문서' 디렉토리에 배치됩니다. 내장된 파일 관리자를 사용하여 언제든지 해당 파일을 제거할 수 있습니다.

응용 프로그램은 연결된 클라우드 계정의 정보를 공유하지 않습니다. 웹 브라우저에서 계정 설정 페이지를 열어 언제든지 클라우드 계정에 대한 액세스를 취소할 수 있습니다.

## 인증 토큰 거부

웹 브라우저에서 계정에 로그인하고 설정 페이지로 이동합니다. 거기에서 클라우드 계정에 연결된 모든 타사 앱을 찾고 더 이상 해당 응용 프로그램을 사용하고 싶지 않으면 제거할 수 있습니다. 자세한 지침은 [여기](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account)에서 확인할 수 있습니다.

응용 프로그램에서 연결된 클라우드 계정을 연결 끊기할 수도 있으며, 인증 토큰도 장치에서 제거됩니다. 장치에서 응용 프로그램을 제거하면 다운로드된 모든 데이터와 액세스 토큰도 제거됩니다.

## 클라우드 스토리지 연결 끊기 또는 구성 변경

- 클라우드 스토리지 옵션에 접근: 먼저 앱의 인터페이스에서 관리하려는 클라우드 스토리지를 찾습니다.
- '...' 버튼 탭: 서비스 제목 옆에 '...' 버튼이 있습니다. 추가 옵션에 액세스하려면 탭합니다.
  - **이름 바꾸기**: 목록에 표시되는 클라우드 서비스 이름을 변경하려면 '이름 바꾸기'를 선택합니다.
  - **설정**: 클라우드 서비스의 구성 또는 인증 데이터를 수정하려면 '설정'을 선택합니다. 인증 토큰이 만료된 경우 연결된 클라우드 서비스를 재인증해야 할 수도 있습니다.
  - **연결 끊기**: 앱과 클라우드 서비스 간의 연결을 완전히 끊으려면 '연결 끊기'를 선택합니다. 이 옵션을 선택하면 해당 클라우드 서비스와 관련된 모든 노래가 앱의 음악 라이브러리에서 제거되지만, 서버에는 그대로 남아 있습니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="연결된 클라우드 스토리지 추가 작업 메뉴" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## 컴퓨터 또는 NAS에 연결

SMB, DLNA, 또는 WebDAV 프로토콜을 사용하여 컴퓨터, 개인 NAS, 또는 기타 네트워크 장치에 연결할 수도 있습니다.

## SMB를 사용하여 컴퓨터에 연결

- "클라우드 스토리지에 연결" → SMB를 탭합니다.
- smb://computer-ip-address/shared-folder-name 형식을 사용하여 URL 필드에 컴퓨터 IP 주소와 공유 폴더 이름을 입력합니다.
- 프로토콜 버전 선택: Auto, SMB1, SMB2
- 로그인 및 비밀번호 입력(필요한 경우)
- "완료됨"을 탭합니다.

연결이 성공하면 "클라우드 스토리지" 섹션에 연결된 스토리지가 표시됩니다.  
SMB를 사용하여 MAC 또는 PC를 연결하는 방법에 대한 전체 튜토리얼은 [여기](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/)에서 확인할 수 있습니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="SMB 연결 설정" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## WebDAV를 사용하여 NAS에 연결

URL 필드를 제외하고 모든 단계가 동일합니다.  
URL은 http://server-name 형식이어야 하며, 서버가 SSL을 지원하는 경우 https://server-name 형식이어야 합니다.
WebDAV 프로토콜을 사용하여 NAS를 연결하는 방법에 대한 전체 튜토리얼은 [여기](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac)에서 확인할 수 있습니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="WebDAV 연결 설정" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## DLNA를 사용하여 컴퓨터 또는 NAS에 연결

DLNA 프로토콜을 사용하여 Windows PC 또는 개인 NAS에 있는 음악 라이브러리를 공유하고 [여기](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone)에 설명된 대로 앱에서 해당 라이브러리에 액세스할 수 있습니다. DLNA는 인기 있고 널리 사용되는 프로토콜이지만, 음악을 재생하거나 다운로드하는 것만 허용합니다. 서버에 파일을 업로드하거나 새 폴더를 만들 수 없습니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="DLNA 연결 설정" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## 사용 가능한 장치

이 섹션은 응용 프로그램을 통해 연결할 수 있는 로컬 네트워크 내의 모든 장치를 표시합니다.  
장치와 연결을 설정하려면 다음 단계를 따르세요:

- 앱을 열고 "사용 가능한 장치" 섹션으로 이동합니다.
- 목록에서 연결하려는 장치를 탭합니다.
- 필요한 경우 로그인 세부 정보를 입력하여 연결을 완료합니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="로컬 네트워크의 사용 가능한 장치" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive는 데스크톱 브라우저를 통해 컴퓨터에서 iOS 기기로 무선 파일 전송을 가능하게 하는 편리한 기술입니다.  
이 기능을 효과적으로 사용하려면 기기와 컴퓨터가 동일한 Wi-Fi 네트워크에 연결되어 있는지 확인하세요.  
Wi-Fi Drive 사용 방법에 대한 단계별 가이드입니다.

## Wi-Fi Drive 활성화

- 응용 프로그램을 열고 "연결하기" 탭으로 이동합니다.
- "Wi-Fi로 연결"을 선택하여 Wi-Fi Drive 메인 화면에 접근합니다.
- "Wi-Fi Drive 시작"을 탭하여 Wi-Fi Drive를 활성화합니다.

## 컴퓨터에서 Wi-Fi Drive에 접근

- 컴퓨터(데스크톱 또는 노트북)에서 웹 브라우저(Chrome, Firefox, 또는 Safari 등)를 엽니다.
- 브라우저의 주소 표시줄에 응용 프로그램이 제공하는 URL을 입력합니다.

## 무선으로 파일 전송

브라우저에서 iOS 기기에 해당하는 웹 페이지가 열리면 컴퓨터에서 웹 페이지로 파일을 쉽게 드래그 앤 드롭할 수 있습니다.  
드래그 앤 드롭한 파일이 iOS 기기로 전송되기 시작하며 응용 프로그램 내에서 접근할 수 있게 됩니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive 서버 설정" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

WiFi-Drive를 사용하여 무선으로 파일을 전송하는 방법에 대한 자세한 지침은 [여기](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)에서 확인할 수 있습니다.

## iTunes File Sharing

iTunes File Sharing은 Mac의 Finder 앱과 Lightning 케이블을 사용하여 컴퓨터에서 기기로 파일을 전송할 수 있는 또 다른 기술입니다.  
- 케이블을 사용하여 기기를 컴퓨터에 연결하고 Mac에서 Finder 앱을 실행합니다.
- "위치" → "연결된 기기" → "파일"을 열고 Evermusic 앱을 찾습니다.
- 앱 아이콘을 탭하여 모든 공유 폴더를 봅니다.
- 드래그 앤 드롭을 사용하여 컴퓨터에서 기기의 공유 폴더로 파일을 복사합니다.  

iTunes File Sharing 사용 방법에 대한 자세한 지침은 [여기](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/)에서 확인할 수 있습니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="Mac에서 iTunes / Finder File Sharing" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## USB 플래시 카드 연결

SD 카드가 있는 경우 Lightning 카드 리더를 사용하여 연결할 수 있습니다. 현재 앱은 Apple 인증 카드 리더와 iXpand Flash Drive를 지원합니다. iXpand Flash Drive가 있는 경우 Lightning 포트에 삽입하고 응용 프로그램을 엽니다. '외부 장치 연결됨' 메시지와 장치 정보가 표시됩니다. 플래시 드라이브 아이콘을 탭하여 음악 폴더에 접근하고 오디오 파일을 탭하여 재생을 시작하면 됩니다. iPhone에 USB 플래시 카드를 연결하고 음악을 듣거나 파일을 관리하는 방법에 대한 자세한 지침은 [여기](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it)에서 확인할 수 있습니다.

## 파일 관리자

클라우드 스토리지 서비스를 연결한 후, 아이콘을 탭하여 사용 가능한 모든 파일과 폴더를 봅니다. 내장된 파일 관리자를 사용하여 이러한 파일로 작업할 수 있습니다 — 다운로드, 이름 바꾸기, 이동 등. 다운로드를 시작하면 파일이 전송 대기열에 나타납니다. 전송 대기열을 보려면 "로컬 파일" 탭으로 이동하여 왼쪽 상단 모서리의 회전 화살표를 탭합니다. 다운로드된 모든 파일과 폴더는 "로컬 파일" 섹션에서 사용할 수 있습니다.

## 상단 도구 모음

탐색 바 바로 아래에 편리하게 위치한 상단 도구 모음은 쉬운 접근을 위한 몇 가지 유용한 작업을 제공합니다. 아래로 스와이프하는 제스처를 사용하여 이 도구 모음을 표시하거나 숨길 수 있습니다. 사용 가능한 작업은 다음과 같습니다:

- **검색**: 이 옵션을 사용하면 현재 디렉토리 내에서 빠른 검색을 수행하여 특정 파일이나 폴더를 손쉽게 찾을 수 있습니다.
- **재생 계속**: 응용 프로그램 설정에서 활성화된 경우, 이 기능은 현재 폴더의 오디오 플레이어 대기열과 마지막 미디어 위치를 복원합니다. 음악 라이브러리에서 중단한 곳을 이어서 재생하는 데 편리한 방법입니다.
- **모두 재생**: 이 작업을 선택하면 앱이 현재 폴더와 하위 폴더를 스캔하여 찾은 모든 오디오 파일을 새 플레이어 대기열에 추가합니다. 특정 디렉토리 내의 모든 음악을 재생하려는 경우 유용합니다.
- **모두 셔플**: "모두 재생"과 유사하지만, 오디오 플레이어 대기열에 추가하기 전에 파일을 셔플합니다. 다양한 순서로 음악을 즐기기 위한 좋은 방법입니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="클라우드 폴더 내 상단 도구 모음" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## 폴더 옵션

앱에서 폴더를 열면 화면 오른쪽 상단 모서리의 "..." 버튼을 탭하여 사용 가능한 편리한 작업 세트를 찾을 수 있습니다.  
이러한 작업에 대한 설명은 다음과 같습니다:

- **선택하다**: 파일 선택 모드를 활성화합니다. 이 모드를 사용하면 폴더 내에서 하나 이상의 파일을 선택하여 선택한 항목에 대한 작업을 수행할 수 있습니다.
- **새 폴더**: 현재 폴더 내에 새 폴더를 만듭니다. 이 기능을 사용하면 파일을 구성하고 라이브러리를 잘 구조화할 수 있습니다.
- **오프라인 모드 활성화**: 현재 폴더에 대한 오프라인 모드를 켭니다. 오프라인 모드는 단순한 다운로드를 넘어 폴더의 변경 사항을 적극적으로 모니터링합니다. 온라인 폴더에 새 파일을 추가하면 앱이 자동으로 기기에 다운로드합니다. 이렇게 하면 로컬 라이브러리가 서버의 변경 사항과 최신 상태를 유지합니다.
- **파일 업로드**: 기기에서 온라인 폴더로 파일을 업로드합니다. 이 작업을 통해 파일을 클라우드 또는 서버로 전송하여 어디서나 접근할 수 있게 됩니다.
- **검색**: 현재 폴더 내에서 특정 파일을 검색합니다. 큰 컬렉션에서 특정 항목을 빠르게 찾는 데 특히 유용합니다.
- **정렬**: 이름, 크기, 또는 편집 날짜와 같은 기준으로 폴더 내의 파일을 정렬합니다. 기본 정렬 모드는 일반적으로 서버의 정렬 순서를 반영하지만 원하는 대로 변경할 수 있습니다.
- **격자/목록 보기**: 두 가지 보기 모드 전환: 테이블 보기와 썸네일 보기. 테이블 보기는 목록에 파일을 표시하고, 썸네일 보기는 파일의 시각적 표현을 표시하여 콘텐츠를 한눈에 더 쉽게 식별할 수 있습니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="현재 폴더 추가 작업 메뉴" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## 온라인 파일 편집

Evermusic에서 클라우드 스토리지 내의 여러 파일을 관리해야 할 경우, 선택 모드를 사용하여 작업을 간소화할 수 있습니다. 효과적인 파일 관리를 위해 다음 단계를 따르세요:

- **선택 모드 활성화**: 기기에서 앱을 열고 클라우드 스토리지가 있는 섹션으로 이동합니다. "..." (말줄임표) 버튼이 있는 오른쪽 상단 모서리를 찾습니다. 탭하고 "선택하다" 메뉴 항목을 선택하여 선택 모드를 활성화합니다.
- **파일 선택**: 나열된 모든 파일이나 폴더 옆에 체크박스가 나타납니다. 체크박스를 탭하여 하나 또는 여러 파일이나 폴더를 선택합니다.
- **다양한 작업 수행**: 관리하려는 파일이나 폴더를 선택한 후에는 필요에 맞게 조정된 여러 작업에 접근할 수 있습니다:

{{< cards cols="1">}}
  {{< card title="" subtitle="온라인 파일에 대한 선택 모드" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## 파일 작업

파일 제목 옆에 말줄임표 기호 "..."(세 점)가 있는데, 이것이 작업 메뉴입니다.  
탭하여 사용 가능한 작업 목록을 표시합니다:

- **다음에 재생**: 선택한 파일을 플레이어 대기열 상단에 삽입하여 현재 재생 중인 항목 바로 다음에 재생되도록 합니다.
- **나중에 재생**: 이 옵션을 선택하면 파일이 플레이어 대기열의 하단에 추가되어 기존 대기열 이후에 재생됩니다.
- **음악 라이브러리에 추가**: 이 작업을 통해 파일을 음악 라이브러리에 통합하여 아티스트, 앨범, 장르, 또는 작곡가별로 쉽게 접근하고 정리할 수 있습니다.
- **플레이리스트에 추가**: 이 작업을 사용하여 파일을 기존 플레이리스트에 추가하거나 새로 만듭니다.
- **오디오 태그 편집**: 이 옵션을 선택하면 Evermusic의 내장 태그 편집기에 접근하여 선택한 파일의 오디오 태그를 수정할 수 있습니다. 파일은 임시 디렉토리로 임시 다운로드되었다가 변경 사항을 확인한 후 스토리지에 업로드됩니다.
- **즐겨찾기에 추가**: 이 작업은 파일을 즐겨찾기 파일 목록에 추가하여 빠르고 편리하게 접근할 수 있습니다.
- **다운로드**: 이 작업을 선택하여 파일 또는 폴더를 기기에 다운로드하여 오프라인 사용 가능하게 만듭니다.
- **이름 바꾸기**: 이 옵션을 사용하면 원격 스토리지에서 직접 파일 이름을 바꿀 수 있습니다.
- **이동**: 이 작업을 선택하여 클라우드 스토리지 내에서 파일을 다른 폴더로 이동하여 정돈된 파일 구조를 유지합니다.
- **다음에서 열기**: 이 작업을 사용하여 파일을 다른 호환 앱으로 내보냅니다. 파일이 기기에 다운로드되고 추가 공유 또는 상호 작용을 위한 공유 대화 상자가 나타납니다.
- **삭제하기**: 이 작업에 주의하세요. 파일이 클라우드 스토리지에서 영구적으로 제거됩니다. 이 삭제는 취소할 수 없습니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="단일 파일에 대한 추가 작업 메뉴" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

작업 목록이 사용 가능한 화면 공간을 초과하면 작업 메뉴 내에서 아래로 스크롤하여 추가 옵션에 접근하면 됩니다.

## 폴더 작업

클라우드 스토리지의 각 폴더에 대해 다양한 작업을 사용할 수 있습니다. 이러한 옵션에 접근하려면 폴더 제목 옆의 말줄임표 아이콘 "..."을 탭하면 됩니다. 모든 작업이 표시되지 않으면 아래로 스크롤하여 더 많은 선택 항목을 확인하세요. 사용 가능한 작업은 다음과 같습니다:

- **모두 재생**: 현재 플레이어 대기열을 선택한 폴더의 모든 항목으로 교체합니다.
- **다음에 재생**: 현재 재생 중인 항목 바로 다음에 전체 폴더를 플레이어 대기열의 상단에 추가합니다.
- **나중에 재생**: 폴더 내용을 플레이어 대기열의 하단에 추가합니다.
- **음악 라이브러리에 추가**: 이 작업은 폴더의 내용을 음악 라이브러리에 원활하게 통합하여 아티스트, 앨범, 장르, 또는 작곡가별로 쉽게 접근하고 정리할 수 있습니다.
- **플레이리스트에 추가**: 전체 폴더를 플레이리스트에 포함할 수 있습니다. 새 플레이리스트를 만들 수도 있으며, 폴더 이름이 자동으로 할당됩니다.
- **즐겨찾기에 추가**: 이 작업을 사용하여 폴더를 즐겨찾기 파일 목록에 추가하여 빠르고 편리하게 접근할 수 있습니다.
- **오프라인 모드 활성화**: 선택한 폴더에 대해 오프라인 모드를 활성화하면 응용 프로그램이 단순한 다운로드를 넘어섭니다. 변경 사항을 지속적으로 스캔하고, 온라인 폴더에 새 파일이 추가되면 자동으로 앱에 다운로드됩니다.
- **다운로드**: 오프라인 접근을 위해 폴더의 모든 내용을 기기에 다운로드합니다.
- **이름 바꾸기**: 원격 스토리지에서 직접 폴더 이름을 바꿉니다.
- **이동**: 클라우드 스토리지 내에서 폴더를 다른 위치로 이동합니다.
- **삭제하기**: 이 작업에 주의하세요. 폴더와 그 내용이 클라우드 스토리지에서 영구적으로 제거됩니다. 이 작업은 취소할 수 없습니다.


## 빠른 접근

빠른 접근 섹션은 화면 상단에 있습니다. 연결된 클라우드 서비스에서 즐겨찾는 파일과 최근에 연 파일에 빠르게 접근할 수 있습니다.
클라우드에서 파일이나 폴더를 열 때마다 "최근 열린 파일" 목록에 추가됩니다. 이 목록을 지우려면 "최근 항목"을 열고 "추가 작업" 버튼을 탭한 다음 "목록 삭제"를 선택합니다. 디렉토리 구조를 탐색하지 않고도 빠르게 접근하기 위해 깊이 중첩된 폴더를 즐겨찾기로 표시할 수도 있습니다.

## 기타 서비스

이 섹션은 사용 경험을 향상시키는 추가 기능을 표시합니다. 현재 앱은 Last.fm 스크로블링을 지원합니다. 연결되면 재생 통계가 자동으로 Last.fm 계정으로 전송됩니다. 나중에 Last.fm 프로필을 방문하여 청취 분석을 보고 맞춤형 음악 추천을 받을 수 있습니다. 자세한 설정 지침은 [여기](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)에서 확인할 수 있습니다.
