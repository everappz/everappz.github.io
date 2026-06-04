---
date: 2020-01-01
lastmod: 2026-06-01
title: 'Evervideo'
description: 'Evervideo 사용 방법을 알아보세요 — iPhone, iPad, Mac용 올인원 클라우드 비디오 플레이어. iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, NFS, FTP / SFTP, DLNA, S3 — 그리고 Plex, Jellyfin, Emby, Subsonic, Navidrome에서 동영상을 스트리밍하고 다운로드하세요. PiP(화면 속 화면), 기본 및 보조 자막, 오디오 및 비디오 이퀄라이저, RTSP IP 카메라 스트림, Chromecast, AirPlay 2, 하드웨어 H.264 / HEVC 디코딩, 사진 및 Apple Music 라이브러리 통합, 소형 항상 표시 플레이어를 지원합니다.'
keywords: [
  "Evervideo 가이드", "Evervideo 사용 방법", "클라우드 비디오 플레이어 iPhone", "비디오 플레이어 Mac",
  "MKV 플레이어 iOS", "FFmpeg 비디오 플레이어", "HEVC 비디오 플레이어 iPhone",
  "화면 속 화면 비디오 iPhone", "PiP 비디오 플레이어 iPad",
  "RTSP 플레이어 iPhone", "IP 카메라 뷰어", "DLNA 비디오 플레이어",
  "Plex 클라이언트 iPhone", "Jellyfin 클라이언트 iOS", "Emby 클라이언트 iPad",
  "자막 플레이어 iOS", "SRT VTT ASS 자막", "보조 자막 iPhone",
  "비디오 이퀄라이저 iOS", "오디오 이퀄라이저 비디오 플레이어", "외부 DAC 비디오",
  "Google Drive에서 비디오 스트리밍", "Dropbox에서 비디오 스트리밍",
  "OneDrive에서 비디오 스트리밍", "iCloud Drive에서 비디오 스트리밍",
  "MEGA에서 비디오 스트리밍", "NAS에서 비디오 스트리밍",
  "Chromecast 비디오 iPhone", "AirPlay 2 비디오", "iCloud 비디오 플레이어",
  "사진 라이브러리 비디오 플레이어", "Apple Music 비디오 플레이어",
  "Wi-Fi Drive 비디오 전송", "M3U 비디오 재생 목록",
  "Evervideo Premium", "Family Sharing 비디오 앱"
]
tags: ["evervideo", "가이드", "비디오 플레이어", "PiP", "자막", "RTSP", "클라우드", "FFmpeg"]
---


### Evervideo 가이드에 오신 것을 환영합니다

Evervideo는 iPhone, iPad, Mac용 완전한 기능을 갖춘 클라우드 미디어 플레이어로, 모든 클라우드 스토리지 계정, NAS 또는 미디어 서버를 개인 미디어 라이브러리로 변환합니다. 아무것도 다시 업로드할 필요 없이 파일을 완전히 제어할 수 있습니다.

하드웨어 가속 H.264 및 HEVC 디코딩을 갖춘 맞춤형 FFmpeg 기반 플레이어 엔진을 기반으로, Evervideo는 시스템이 인식하지 못하는 형식도 포함하여 거의 모든 최신 컨테이너 및 코덱을 완전한 화질로 재생합니다 — MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS 및 그 외 FFmpeg 형식들. Wi-Fi 또는 셀룰러 네트워크에서 스마트 버퍼링으로 부드러운 스트리밍을 제공합니다. PiP(화면 속 화면)는 다른 앱 위에서도 비디오를 유지하며, 소형 항상 표시 플레이어를 통해 라이브러리를 탐색하면서도 계속 시청할 수 있고, Chromecast 및 AirPlay 2로 한 번 탭하면 TV, HomePod 또는 스피커로 재생을 전송할 수 있습니다.

Evervideo는 하나의 앱에서 놀랍도록 다양한 소스에 연결합니다:

- **개인 클라우드 스토리지:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **자체 호스팅 미디어 서버:** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud (공유 API를 통한 ownCloud 포함) · Synology Drive · QNAP.
- **NAS 및 파일 공유 프로토콜:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (비밀번호 또는 공개 키 인증) · NFS · DLNA · UPnP.
- **라이브 및 IP 카메라 스트림:** RTSP — Evervideo를 임의의 RTSP URL(`rtsp://camera-ip/stream`)에 연결하면 바로 재생됩니다.
- **S3 호환 객체 스토리지:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces 및 기타 S3-API 엔드포인트.
- **온디바이스 소스:** 사진 라이브러리 (모든 비디오, 짧음 / 보통 / 긴 영상, 화면 녹화, 사진 앨범), 음악 앱 라이브러리 (앨범, 장르, 재생 목록), USB / SD 카드 드라이브, 로컬 파일.

### 모든 형식과 코덱을 위한 단일 플레이어

대부분의 iOS 앱이 MP4 / MOV 내의 H.264 / H.265에서 멈추는 반면, Evervideo는 Apple의 시스템 코덱과 함께 FFmpeg를 번들로 제공하여 시스템이 인식하지 못하는 형식도 재생할 수 있습니다 — MKV 컨테이너, VP9, AV1, MPEG-2, OGG, Vorbis 등 — 파일과 기기에 따라 하드웨어 H.264 / HEVC 디코딩과 소프트웨어 디코딩 사이에서 자동으로 전환합니다.

비디오 트랙 (멀티 스트림 블루레이 립), 오디오 트랙 (코멘터리 트랙, 더빙), 자막 트랙을 선택할 수 있습니다. 외부 SRT, VTT, ASS / SSA 자막 파일은 한 번 탭으로 불러올 수 있으며, 번들 libass 덕분에 고급 ASS / SSA 스타일링이 올바르게 렌더링됩니다.

### 스마트 자막

- **자막 트랙 선택** 언어 학습에 완벽합니다.
- **외부 자막 파일** (`.srt`, `.vtt`, `.ass`, `.ssa`) 기기 어디서나 또는 클라우드에서 불러올 수 있습니다.
- **libass** 완전히 스타일이 적용된 ASS / SSA 렌더링을 위해.
- **트랙별 및 전체 폰트 선택** 자막에 사용됩니다.
- **오디오 트랙 선택** 더빙, 코멘터리 또는 감독 트랙을 선택합니다.
- **비디오 트랙 선택** 다중 앵글 또는 다중 버전 파일에 사용됩니다.

### 화면과 음향 조정

두 개의 이퀄라이저가 나란히 있습니다: 베이스와 트레블 조정을 위한 오디오 이퀄라이저 (맞춤 프리셋 가져오기 / 내보내기 지원), 밝기, 대비, 채도, 색조 조정을 위한 비디오 이퀄라이저 (마찬가지로 가져오기 / 내보내기 지원). 두 엔진 모두 오디오파일 컨트롤도 제공합니다: 오디오 출력 샘플 레이트, 채널 수, IO 버퍼 지속 시간, 혼합 모드 — 외부 DAC 및 홈 씨어터 수신기 사용자를 위한 기능입니다.

### 캐스트, AirPlay 및 화면 속 화면

- **화면 속 화면 (PiP):** 다른 앱을 사용하면서도 계속 시청합니다.
- **AirPlay 2:** Apple TV, HomePod 또는 AirPlay 2 지원 스피커 / TV로 비디오를 전송합니다.
- **Google Chromecast:** Chromecast 또는 Cast 지원 TV로 직접 캐스트합니다.
- **소형 플레이어:** 모든 화면 위에 유지되는 지속적인 미니 플레이어로 비디오를 잃지 않고 라이브러리를 탐색할 수 있습니다.

### 개인정보 보호 및 보안

Evervideo는 모든 클라우드 제공업체의 공식 SDK와 OAuth 기반 로그인을 사용하므로 비밀번호가 앱에 도달하지 않습니다. 액세스 토큰은 iOS/MacOS Keychain에 암호화되어 저장되고, 모든 전송은 TLS로 보호되며, 클라우드 계정에서 액세스를 취소하거나 기기에서 Evervideo를 제거하면 즉시 모든 것이 삭제됩니다. 추가적인 개인정보 보호를 위해 선택적 4자리 비밀번호로 라이브러리를 보호하세요.

### Evervideo 시작하기

이 가이드는 iPhone, iPad, Mac에서 Evervideo의 모든 부분을 안내합니다 — 클라우드 서비스 연결, 라이브러리 탐색, 파일 다운로드 및 전송, 재생 목록 관리, 미디어 플레이어, 이퀄라이저, 자막, 화면 속 화면 세밀 조정까지. 아래 카드를 사용하여 필요한 섹션으로 바로 이동하세요.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="내비게이션" subtitle="iPhone의 탭 바, iPad 및 Mac의 왼쪽 메뉴, 소형 항상 표시 미디어 플레이어." >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="파일" subtitle="클라우드, NAS, RTSP 스트림, 로컬 파일, USB 드라이브 및 전송 대기열을 위한 통합 탭." >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="미디어 라이브러리" subtitle="앨범, 장르, 최근 항목, 즐겨찾기로 탐색 — iOS 사진 라이브러리 및 Apple Music 라이브러리 포함." >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="재생 목록" subtitle="클라우드, 로컬, 사진 또는 음악 라이브러리에서 재생 목록 만들기, M3U / M3U8 / CUE 가져오기." >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="미디어 플레이어" subtitle="화면 속 화면, 오디오 및 비디오 트랙, 자막, 오디오 + 비디오 이퀄라이저, AirPlay, Chromecast." >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="설정" subtitle="오디오 엔진, 비디오 디코더, 자막, 라이브러리, 파일 관리자, 위젯, 개인화, 언어, 백업." >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="자주 묻는 질문" subtitle="Evervideo에 관한 가장 일반적인 질문에 대한 답을 찾아보세요." >}}

{{< /cards >}}
