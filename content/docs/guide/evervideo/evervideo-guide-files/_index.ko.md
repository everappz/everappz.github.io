---
title: "파일"
date: 2020-02-01
lastmod: 2026-06-01
description: "iPhone, iPad, Mac에서 Evervideo의 파일 탭 사용 방법을 알아보세요. 클라우드 서비스, NAS 장치, 미디어 서버 및 RTSP 스트림을 한 곳에서 연결하세요. 오프라인 비디오, 전송 대기열, 다운로드, Wi-Fi Drive, iTunes / Finder 파일 공유 및 USB 드라이브를 관리하세요. iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA 및 S3 호환 스토리지 포함."
keywords: [
  "Evervideo 파일", "Evervideo 연결하기", "Evervideo 로컬 파일",
  "클라우드 비디오 설정 iPhone", "Google Drive 비디오 연결", "SMB 비디오 스트리밍",
  "WebDAV 비디오 플레이어 iOS", "DLNA 비디오 iPhone", "NAS 비디오 스트리밍",
  "Wi-Fi Drive 비디오 전송", "Evervideo iTunes 파일 공유", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "Evervideo 오프라인 모드 비디오", "Evervideo 전송 대기열",
  "Evervideo 파일 관리자", "Evervideo Documents 폴더",
  "비디오 플레이어 Synology", "비디오 플레이어 QNAP",
  "비디오 플레이어 Apple Time Capsule", "USB DAC 비디오",
  "iXpand 비디오 플레이어", "S3 비디오 플레이어"
]
tags: ["가이드", "evervideo", "파일", "연결하기", "클라우드", "NAS", "Plex", "RTSP"]
readingTime: 14
---

파일 탭은 Evervideo의 올인원 파일 관리자입니다. 클라우드 스토리지와 로컬 파일을 서로 다른 탭으로 분리하는 대부분의 비디오 앱과 달리, Evervideo는 두 가지를 하나의 스크롤 가능한 화면으로 통합하여 탭을 왔다 갔다 하지 않고 Plex 서버에서 클라우드 폴더로, iPhone의 Documents 폴더로 이동할 수 있습니다.

파일 탭은 화면에 이 순서로 나타나는 명확한 섹션으로 나뉩니다:

- **빠른 접근** — 가장 최근에 열었던 파일과 폴더에 대한 최근 항목 및 즐겨찾기.
- **이 애플리케이션의 파일** — Evervideo의 샌드박스 Documents 폴더에 있는 것들.
- **이 iPhone / iPad / Mac의 파일** — 기기의 다른 곳에 있는 비디오로, 시스템 파일 선택기를 통해 표시됩니다.
- **클라우드 스토리지** — 연결된 모든 클라우드 계정, NAS 및 미디어 서버.
- **사용 가능한 장치** — 로컬 네트워크에서 Bonjour / mDNS로 자동 발견된 서버와 드라이브.

파일 화면의 오른쪽 상단 모서리에 전송 버튼 (회전하는 화살표 아이콘)이 있습니다. 탭하여 모든 소스의 모든 다운로드 및 업로드를 모니터링하는 전송 대기열을 열 수 있습니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="연결된 스토리지의 Evervideo 파일" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## 클라우드 스토리지에 연결

파일 탭의 클라우드 스토리지 섹션은 연결된 모든 계정, NAS, 미디어 서버 및 스트림이 나란히 하나의 스크롤 가능한 목록으로 있는 곳입니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="파일 탭의 Evervideo 클라우드 스토리지 섹션" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- **파일** 탭을 엽니다.
- **클라우드 스토리지** 섹션으로 스크롤합니다.
- 메뉴에서 **클라우드 스토리지에 연결하다**를 탭합니다.
- 목록에서 클라우드 스토리지 서비스를 선택합니다.
- 클라우드 제공업체가 제공한 공식 인증 페이지에 자격 증명을 입력한 다음 **완료됨**을 탭합니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 클라우드 스토리지 서비스 연결" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

문제가 발생하면 인터넷 연결과 로그인 / 비밀번호를 확인하세요. 앱의 Premium 버전에서는 무제한 서비스를 추가할 수 있습니다. 무료 버전은 최대 3개를 지원합니다.

## 지원되는 클라우드 스토리지 서비스, 미디어 서버 및 프로토콜

Evervideo는 비디오를 위한 매우 다양한 소스를 지원합니다. 아래의 모든 것이 단일 클라우드 스토리지에 연결하다 흐름에서 작동합니다.

**개인 클라우드 스토리지:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**자체 호스팅 미디어 서버:** Plex · Jellyfin · Emby · Subsonic (및 모든 Subsonic 호환 서버 — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (공유 API를 통한 ownCloud 포함) · Synology Drive · QNAP.

**NAS 및 파일 공유 프로토콜:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH 파일 전송 프로토콜, 비밀번호 또는 공개 키 인증) · NFS · DLNA / UPnP (재생 및 다운로드).

**라이브 및 IP 카메라 스트림:** RTSP — Evervideo를 임의의 `rtsp://` URL에 연결하면 바로 재생됩니다. 보안 카메라, IPTV 스트림, 도어벨 카메라, 유아 모니터 및 유사한 라이브 소스에 적합합니다.

**S3 호환 객체 스토리지:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces 및 기타 S3-API 엔드포인트.

**온디바이스 라이브러리:** 사진 라이브러리 (모든 비디오, 화면 녹화, 사진 앨범) 및 음악 앱 라이브러리 (앨범, 장르, 재생 목록) — 모두 미디어 라이브러리 내에 표시되어 복사할 필요가 없습니다.

**로컬 네트워크 검색:** 사용 가능한 장치 섹션은 Wi-Fi 네트워크의 모든 Bonjour / mDNS 서비스를 자동으로 나열합니다 — Plex, Jellyfin, Emby 서버, Synology, QNAP, 연결된 드라이브가 있는 AirPort 라우터, Apple Time Capsule — IP 주소를 입력하지 않고도 탭하여 연결할 수 있습니다.

각 연결은 지원되는 경우 OAuth 기반 인증을 사용하여 서비스의 공식 SDK 또는 개방형 프로토콜을 사용합니다. 동일한 서비스의 여러 계정 (예: 두 개의 Google Drive 계정 또는 Plex와 Jellyfin 서버 모두)을 연결하고 클라우드 스토리지 섹션에서 나란히 탐색할 수 있습니다.

## 보안 및 개인정보 보호

Evervideo는 연결된 클라우드 서비스와 상호 작용하기 위해 공식 SDK와 보안 연결만 사용합니다. 로그인과 비밀번호는 애플리케이션에서 접근할 수 없으며 — 모든 전송은 TLS 암호화됩니다.

로그인과 비밀번호를 입력하면 애플리케이션은 클라우드 서비스 제공업체가 제공한 공식 인증 페이지를 표시하며 전체 인증 과정은 애플리케이션 외부에서 이루어집니다. 그런 다음 클라우드 서비스 제공업체는 성공적인 인증 후 애플리케이션에 인증 토큰을 전송하며, 해당 토큰은 API 호출에 사용됩니다.

인증 토큰은 타사 애플리케이션이 사용자를 대신하여 클라우드 스토리지와 상호 작용할 수 있도록 하는 디지털 키입니다. 토큰은 기기에 Apple의 보안 시스템 스토리지 (Keychain)에 저장되며, 이는 저장 시 암호화되고 기기 비밀번호 또는 생체 인식 잠금으로 보호됩니다. 연결된 클라우드 서비스에서 기기로 파일을 다운로드할 수 있으며, 해당 파일은 앱의 Documents 디렉토리에 저장되고 내장 파일 관리자를 사용하여 언제든지 제거할 수 있습니다.

애플리케이션은 연결된 클라우드 계정의 어떤 정보도 Everappz, 광고주 또는 제3자와 공유하지 않습니다. 웹 브라우저에서 계정 설정 페이지를 열어 언제든지 클라우드 계정에 대한 액세스를 취소할 수 있습니다.

## 인증 토큰 취소

인증 토큰을 취소하려면 웹 브라우저에서 클라우드 계정에 로그인하고 보안 또는 연결된 앱 페이지로 이동하세요. 거기서 클라우드 계정에 연결된 모든 타사 앱을 찾을 수 있으며, 더 이상 사용하고 싶지 않은 앱을 제거할 수 있습니다. Google 계정에 대한 자세한 지침은 [여기](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account)에서 확인할 수 있습니다.

애플리케이션 자체에서 클라우드 계정의 연결을 끊을 수도 있습니다 — 그렇게 하면 인증 토큰이 기기에서 즉시 삭제됩니다. 기기에서 애플리케이션을 제거하면 모든 다운로드된 데이터와 액세스 토큰이 함께 자동으로 제거됩니다.

## 클라우드 스토리지 연결 끊기 또는 구성 변경

- **클라우드 스토리지 옵션 접근** — 파일 탭의 **클라우드 스토리지** 섹션에서 연결된 서비스를 찾으세요.
- **서비스 제목 옆의 "..." 버튼을 탭**하여 추가 옵션을 엽니다:
  - **이름 변경** — 목록에 표시되는 클라우드 서비스 이름을 변경합니다.
  - **설정** — 구성 또는 인증 데이터를 수정합니다. 인증 토큰이 만료된 경우 연결된 클라우드 서비스를 재인증해야 할 수 있습니다.
  - **연결 끊기** — 앱과 클라우드 서비스 간의 연결을 완전히 끊습니다. 해당 서비스와 연결된 모든 비디오가 미디어 라이브러리에서 제거되지만, 서버에서는 그대로 유지됩니다.

## 컴퓨터 또는 NAS에 연결

SMB, WebDAV, FTP / FTPS, SFTP, NFS 또는 DLNA 프로토콜을 사용하여 컴퓨터, 개인 NAS 또는 기타 네트워크 장치에 연결할 수 있습니다. 이것은 Mac, Windows PC, Synology, QNAP, Apple Time Capsule 또는 WD My Cloud Home에 있는 기존 홈 미디어 라이브러리를 아무것도 복사하지 않고 Evervideo에 가져오는 가장 쉬운 방법입니다.

### SMB를 사용하여 컴퓨터에 연결

- **클라우드 스토리지에 연결하다 → SMB**를 탭합니다.
- `smb://computer-ip-address/shared-folder-name` 형식을 사용하여 컴퓨터의 IP 주소와 공유 폴더 이름을 입력합니다.
- 프로토콜 버전을 선택합니다: **Auto**, **SMB1** 또는 **SMB2**.
- 로그인과 비밀번호를 입력합니다 (필요한 경우).
- **완료됨**을 탭합니다.

연결이 성공하면 공유가 클라우드 스토리지 섹션에 나타납니다. SMB를 사용하여 Mac 또는 PC를 연결하는 방법에 대한 전체 튜토리얼은 [여기](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/)에서 확인할 수 있습니다.

### WebDAV를 사용하여 NAS에 연결

모든 단계는 SMB와 동일하지만 URL 필드는 다릅니다. 서버가 SSL을 지원하는 경우 `http://server-name` 또는 `https://server-name`을 사용하세요. WebDAV는 Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home 및 WebDAV 엔드포인트가 있는 다른 서버에서 작동합니다.

WebDAV에 대한 전체 튜토리얼은 [여기](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac)에서 확인할 수 있습니다.

### DLNA / UPnP를 통해 연결

Windows PC 또는 NAS에 있는 미디어 라이브러리를 DLNA / UPnP 프로토콜을 사용하여 공유하고 [여기](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone)에 설명된 대로 Evervideo 내에서 접근하세요. DLNA는 널리 지원되지만 비디오를 재생하거나 다운로드하는 것만 허용합니다 — DLNA 서버에 파일을 업로드하거나 새 폴더를 만들 수 없습니다.

### FTP, FTPS 또는 SFTP를 사용하여 연결

Evervideo는 클래식 파일 전송 프로토콜도 지원합니다. FTP 또는 FTPS를 통해 서버를 연결하려면 클라우드 스토리지에 연결하다 → FTP를 탭하고 `ftp://server-name` 형식 (암호화된 연결의 경우 `ftps://server-name`)으로 호스트 URL을 입력하고 로그인과 비밀번호를 제공한 다음 완료됨을 탭합니다. SFTP (SSH 파일 전송 프로토콜)의 경우 SFTP를 선택하고 비밀번호 또는 SSH 키 쌍을 제공하세요.

### NFS 공유에 연결

Evervideo는 NFS (네트워크 파일 시스템) 지원을 포함합니다 — Linux 호스트, BSD 서버 및 SMB 대신 NFS를 통해 비디오 라이브러리를 노출하는 NAS 장치에 유용합니다. 클라우드 스토리지에 연결하다 메뉴에서 NFS를 선택하고 서버 주소와 내보낸 경로를 입력한 다음 완료됨을 탭합니다.

## Plex Media Server에 연결

Evervideo는 Plex Media Server에 직접 연결하여 Movies, TV Shows 및 Home Videos 라이브러리를 탐색할 수 있습니다. 클라우드 스토리지에 연결하다 → Plex를 탭하고 Plex 계정으로 로그인하고 서버를 선택하면 라이브러리가 클라우드 서비스 옆에 나타납니다. 동일한 로컬 네트워크의 Plex 서버는 사용 가능한 장치 섹션에서도 자동으로 발견됩니다.

## Jellyfin 또는 Emby 서버에 연결

Jellyfin (오픈 소스)과 Emby (상용) 미디어 서버 모두 Evervideo에서 기본적으로 작동합니다. 클라우드 스토리지에 연결하다 → Jellyfin 또는 Emby를 탭하고 서버 URL (일반적으로 `http://server-ip:8096`과 같은 형식)과 자격 증명을 입력하면 라이브러리가 스트리밍 준비가 됩니다.

## Subsonic 또는 Navidrome 서버에 연결

Evervideo는 Subsonic API를 지원하므로 Subsonic 자체, Navidrome 및 모든 다른 Subsonic 호환 서버 — Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) 및 Ampache 포함 — 와 함께 작동합니다. 클라우드 스토리지에 연결하다 → Subsonic을 탭하고 서버 URL과 자격 증명을 입력하면 라이브러리가 클라우드 스토리지 섹션에 나타납니다.

## RTSP 스트림에 연결 (IP 카메라, 라이브 TV, IPTV)

Evervideo는 RTSP를 기본적으로 지원하므로 보안 카메라, 도어벨 카메라, IPTV 제공업체, 유아 모니터, 방송 피드 등 모든 RTSP 소스를 연결하면 Evervideo가 스트림을 당겨서 라이브로 디코딩합니다. 온라인 링크 → 링크 추가를 탭하고 전체 URL (`rtsp://camera-ip:port/stream-path`)을 붙여 넣고 필요한 경우 로그인과 비밀번호를 제공한 다음 완료됨을 탭합니다.

## S3 호환 객체 스토리지에 연결

셀프 호스터와 클라우드 객체 스토리지를 사용하는 파워 사용자를 위해 Evervideo에는 S3 호환 커넥터가 포함되어 있습니다. 클라우드 스토리지에 연결하다 → S3 스토리지를 탭하고 엔드포인트 URL, 리전, 액세스 키, 시크릿 키 및 버킷 이름을 입력합니다. AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces 및 기타 S3-API 엔드포인트에서 작동합니다.

## 사용 가능한 장치

이 섹션은 Bonjour / mDNS 검색을 통해 Evervideo에서 연결할 수 있는 로컬 네트워크의 모든 장치를 표시합니다 — Plex, Jellyfin, Emby 서버, Synology, QNAP, 연결된 드라이브가 있는 AirPort 라우터, Apple Time Capsule 등. 연결을 설정하려면:

- 파일 탭의 사용 가능한 장치 섹션으로 스크롤합니다.
- 연결할 장치를 탭합니다.
- 필요한 경우 로그인 정보를 입력하여 연결을 완료합니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="로컬 네트워크의 Evervideo 사용 가능한 장치" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive를 사용하면 컴퓨터에서 데스크탑 브라우저, Finder 또는 File Explorer를 통해 iOS 기기로 파일을 무선으로 전송할 수 있습니다. 기기와 컴퓨터가 동일한 Wi-Fi 네트워크에 있어야 합니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Wi-Fi Drive 활성화

- 파일 탭에서 클라우드 스토리지 → Wi-Fi로 연결로 스크롤하여 Wi-Fi Drive 메인 화면을 엽니다.
- (선택 사항) 내장 웹 서버의 사용자 이름과 비밀번호를 설정합니다.
- Wi-Fi Drive 시작을 탭합니다.

### 컴퓨터에서 Wi-Fi Drive 접근

- 컴퓨터에서 웹 브라우저를 엽니다 (Chrome, Firefox, Safari 등).
- 애플리케이션에 표시된 URL을 입력합니다.
- 컴퓨터에서 웹 페이지로 파일을 드래그 앤 드롭합니다 — iOS 기기로 전송이 시작됩니다.

macOS에서 Finder의 **서버에 연결…**(이동 → 서버에 연결…)를 통해 또는 Windows의 File Explorer (네트워크 드라이브 연결…)를 통해 Wi-Fi Drive를 직접 마운트하여 iPhone 또는 iPad를 일반 네트워크 드라이브로 취급할 수도 있습니다.

자세한 지침은 [여기](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)에서 확인할 수 있습니다.

## iTunes / Finder 파일 공유

iTunes 파일 공유 (macOS Catalina 이상에서는 Finder 파일 공유)를 사용하면 Lightning 또는 USB-C 케이블을 사용하여 파일을 전송할 수 있습니다. 기기를 연결하고 Mac에서 Finder (또는 Windows에서 iTunes)를 열고 앱 목록에서 Evervideo를 찾아 공유 폴더로 파일을 복사합니다.

## USB 플래시 드라이브 또는 SD 카드 연결

Lightning-to-USB / USB-C 어댑터 또는 카드 리더기를 통해 iPhone, iPad 또는 Mac에 USB 드라이브 또는 SD 카드를 연결합니다. 파일 → 이 iPhone의 파일 → 폴더 열기를 열고 드라이브로 이동하여 비디오 파일 또는 폴더를 선택합니다. Evervideo는 내부 스토리지로 복사하지 않고 드라이브에서 직접 파일을 재생합니다 — 매우 큰 4K 라이브러리에 유용합니다.

## 연결된 스토리지에서 폴더 탐색

연결된 클라우드 서비스를 탭하여 파일 브라우저를 엽니다. 폴더는 사용 가능한 경우 비디오 썸네일을 표시하고, 비디오를 탭하면 즉시 재생이 시작되면서 나머지 파일을 백그라운드에서 계속 스트리밍합니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="연결된 스토리지에서 Evervideo 폴더 탐색" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## 빠른 접근

빠른 접근 섹션은 파일 탭의 상단에 위치합니다. 클라우드 서비스 및 온디바이스 스토리지의 즐겨찾는 파일과 폴더 및 최근 열린 파일과 폴더에 빠르게 접근할 수 있습니다. 클라우드에서 파일이나 폴더를 열 때마다 최근 열린 목록에 추가됩니다. 깊이 중첩된 폴더를 즐겨찾기로 표시하면 디렉토리 구조를 탐색하지 않고도 빠르게 접근할 수 있습니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 온라인 링크 및 빠른 접근" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## 이 애플리케이션의 파일

이 섹션은 Evervideo의 샌드박스 Documents 디렉토리에 저장된 파일과 폴더를 표시합니다 — 클라우드에서 다운로드한 것, Wi-Fi Drive를 통해 전송한 것, Finder 파일 공유를 통해 복사한 것, 또는 다른 앱에서 가져온 것들.

{{< cards cols="1">}}
  {{< card title="" subtitle="이 애플리케이션의 Evervideo 파일" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Documents 폴더

Documents 폴더는 이 애플리케이션의 파일 내의 모든 것의 루트입니다. 하위 폴더를 만들고, 파일 이름을 변경하고, 이동하고, 원하는 대로 그룹화할 수 있습니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 로컬 파일 — Documents 폴더" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## 이 iPhone / iPad / Mac의 파일

이 섹션은 기기에 있지만 다른 애플리케이션에 있는 비디오를 표시합니다. 시스템 파일 선택기를 사용하여 Evervideo로 가져올 수 있습니다:

- 특정 파일을 선택하려면 파일 열기…를 탭합니다.
- 전체 폴더를 선택하려면 폴더 열기…를 탭합니다.

아무것도 복사하지 않고 iCloud Drive 또는 연결된 USB 드라이브의 폴더로 작업하기 위해 폴더 연결을 사용하여 기기의 폴더에 읽기 / 쓰기 접근 링크를 만들 수도 있습니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="이 기기의 Evervideo 파일" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## 특수 폴더

파일 탭에는 Evervideo가 자동으로 만들고 사용하는 여러 특수 폴더가 있습니다:

- **다운로드** — 클라우드에서 다운로드된 모든 파일이 기본적으로 여기에 나타납니다. 설정 → 파일 관리자 → 다운로드한 파일 저장 위치에서 사용자 정의할 수 있습니다.
- **플레이어 캐시** — 미디어 플레이어 캐시. 기본적으로 플레이어는 부드러운 재생을 위해 다가오는 비디오를 미리 다운로드합니다. 앱 설정에서 캐시를 비활성화하거나 이 폴더를 삭제할 수 있습니다.
- **iCloud** — 이 폴더의 파일은 동일한 iCloud 계정에 연결된 모든 기기에서 동기화됩니다.
- **오프라인 폴더** — 폴더, 재생 목록, 앨범 또는 장르를 오프라인으로 사용 가능하게 표시하면 파일이 이 폴더로 다운로드됩니다.

## 상단 툴바

내비게이션 바 아래에 위치한 상단 툴바는 아래로 스와이프 제스처로 표시하거나 숨길 수 있는 여러 작업을 제공합니다:

- **검색** — 현재 폴더 또는 섹션 내에서 검색을 수행합니다.
- **계속 재생** — 설정에서 활성화된 경우 현재 폴더의 플레이어 대기열과 마지막 비디오 위치를 복원합니다.
- **모두 재생** — 현재 폴더와 하위 폴더를 스캔하고 플레이어 대기열에 파일을 추가합니다.
- **모두 셔플** — 모두 재생과 같지만 추가하기 전에 셔플합니다.

## 폴더 옵션

폴더를 열 때 오른쪽 상단 모서리의 **"..."** 버튼을 탭하여 다음 작업을 수행합니다:

- **선택하다** — 파일 선택 모드를 활성화합니다.
- **새 폴더** — 현재 폴더 내에 새 폴더를 만듭니다.
- **오프라인 모드 활성화** — 현재 폴더의 오프라인 동기화를 켭니다. 온라인에서 추가된 새 파일이 자동으로 다운로드됩니다.
- **파일 업로드** — 기기에서 온라인 폴더로 파일을 업로드합니다.
- **검색** — 폴더 내에서 검색합니다.
- **정렬** — 이름, 크기, 수정 날짜 또는 메타데이터별로 파일을 정렬합니다.
- **그리드 / 목록 보기** — 테이블 보기와 썸네일 보기 사이를 전환합니다. 썸네일 보기는 큰 비디오 포스터 미리 보기를 표시합니다.

## 선택 모드

오른쪽 상단 모서리의 **"..."**를 탭하고 **선택하다**를 선택하여 선택 모드로 들어갑니다. 모든 파일과 폴더 옆에 확인란이 나타납니다. 하나 또는 여러 항목을 선택한 다음 배치 작업을 수행합니다: 다음에 재생, 나중에 재생, 미디어 라이브러리에 추가, 재생 목록에 추가, 복사, 업로드, 이동, 이름 변경 또는 삭제.

{{< cards cols="1">}}
  {{< card title="" subtitle="파일 관리자에서 Evervideo 선택 모드" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

연결된 클라우드 스토리지를 읽기 전용으로 처리하려면 (실수로 삭제하는 것을 방지하기 위해) 설정 → 파일 관리자 → 온라인 파일 편집 → 꺼짐을 활성화하여 UI에서 모든 파괴적인 작업을 숨기세요.

## 파일 작업

파일 제목 근처의 **"..."** 아이콘을 탭하여 작업 메뉴를 표시합니다:

- **다음에 재생** — 플레이어 대기열의 상단에 파일을 삽입합니다.
- **나중에 재생** — 플레이어 대기열의 하단에 파일을 추가합니다.
- **미디어 라이브러리에 추가** — 앨범과 장르로 정리된 미디어 라이브러리에 파일을 통합합니다.
- **재생 목록에 추가** — 기존 재생 목록에 파일을 추가하거나 새로 만듭니다.
- **태그 편집** — 내장 태그 편집기를 열어 메타데이터를 수정합니다. 온라인 파일의 경우 파일이 임시로 다운로드되고 편집된 다음 확인 후 다시 업로드됩니다.
- **즐겨찾기에 추가** — 빠른 접근을 위해 즐겨찾기 목록에 파일을 추가합니다.
- **다운로드** — 오프라인 사용을 위해 기기에 파일 또는 폴더를 다운로드합니다.
- **이름 변경** — 원격 스토리지에서 파일 이름을 직접 변경합니다.
- **이동** — 클라우드 스토리지 내의 다른 폴더로 파일을 이동합니다.
- **아카이브에 추가** — 파일을 단일 ZIP 파일로 묶습니다 (Premium 기능).
- **다른 앱에서 열기** — 시스템 공유 시트를 통해 다른 호환 앱으로 파일을 내보냅니다.
- **삭제하기** — 파일을 영구적으로 제거합니다. **이 작업은 취소할 수 없습니다.**

## 폴더 작업

클라우드 스토리지의 각 폴더에 대해 폴더 제목 옆의 **"..."** 아이콘을 탭하면 다양한 작업을 수행할 수 있습니다.

- **모두 재생** — 현재 플레이어 대기열을 폴더의 모든 비디오로 교체합니다.
- **다음에 재생 / 나중에 재생** — 전체 폴더를 대기열에 추가합니다.
- **미디어 라이브러리에 추가** — 폴더의 내용을 미디어 라이브러리에 통합합니다.
- **재생 목록에 추가** — 전체 폴더를 재생 목록에 추가합니다.
- **즐겨찾기에 추가** — 즐겨찾기에 폴더를 추가합니다.
- **오프라인 모드 활성화** — 단순한 다운로드를 넘어 새 파일을 지속적으로 모니터링하고 온라인에 나타나면 자동으로 다운로드합니다.
- **다운로드** — 오프라인 접근을 위해 폴더의 모든 내용을 기기에 다운로드합니다.
- **이름 변경 / 이동** — 원격 스토리지에서 폴더 이름을 변경하거나 이동합니다.
- **아카이브에 추가** — 폴더 내용을 ZIP 파일로 묶습니다 (Premium 기능).
- **삭제하기** — 폴더와 그 내용을 영구적으로 제거합니다. **이 작업은 취소할 수 없습니다.**

## 전송 대기열

파일 탭의 오른쪽 상단 모서리에는 **전송** 버튼 (회전하는 화살표 아이콘)이 있습니다. 탭하여 전송 대기열을 엽니다 — 모든 소스의 모든 활성 다운로드 및 업로드 목록으로, 파일별 실시간 진행 상황, 속도 및 ETA가 표시됩니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo 파일 전송 대기열" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

전송을 일시 중지, 재개, 실패한 전송 재시도, 항목을 재정렬하여 특정 다운로드를 우선시하거나 개별적으로 취소할 수 있습니다. 또한 설정 → 파일 관리자에서 전송 대기열 속도 (최대 병렬 작업), 네트워크 유형 (Wi-Fi만 또는 Wi-Fi + 셀룰러) 및 백그라운드 전송을 조정할 수 있습니다.

{{< cards cols="1">}}
  {{< card title="" subtitle="파일 전송 대기열에서 Evervideo 작업" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## 오프라인 모드 및 동기화된 오프라인 폴더

오프라인 모드는 인터넷에 연결되어 있지 않을 때도 즐겨찾는 비디오를 볼 수 있는 편리한 기능입니다. 폴더, 재생 목록, 앨범 또는 장르에 오프라인 모드를 활성화하면 해당 컬렉션의 모든 파일이 오프라인 재생을 위해 자동으로 기기에 다운로드됩니다. 오프라인 폴더 섹션에 나타납니다.

원격 서버에 새 파일을 추가하면 자동으로 다운로드됩니다 — 따라서 오프라인 컬렉션은 아무것도 하지 않아도 최신 상태를 유지합니다. 수동으로 재동기화하려면 오프라인 폴더의 오른쪽 상단 모서리에 있는 세 점을 탭하고 동기화하다를 선택합니다.

설정 → 파일 관리자 → 동기화된 오프라인 폴더 → 시간 간격에서 동기화 타임아웃을 조정할 수 있습니다.

자세한 지침은 [여기](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/)에서 확인할 수 있습니다.

## 개인화

설정 → 개인화에서 파일 탭이 표시되는 방식을 구성할 수 있습니다:

- **파일 화면 스타일** — 일반 메뉴 (폴더 목록을 직접 표시) 또는 그룹화된 메뉴 (내용을 카테고리별로 그룹화 — 빠른 접근, 특수 폴더, 클라우드 스토리지 등).
