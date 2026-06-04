---
date: 2020-01-01
title: 'Flacbox'
description: 'Flacbox 사용 방법 알아보기 — iPhone, iPad, Mac용 고해상도 FLAC, DSD, ALAC 및 FFmpeg 기반 클라우드 음악 플레이어. iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, DLNA 연결. 고해상도 오디오 스트리밍 및 다운로드, 메타데이터 편집, 오디오북 청취, Last.fm 스크로블링, Apple CarPlay 및 홈 화면 위젯 사용, 10밴드 이퀄라이저 맞춤 설정.'
keywords: [
  "Flacbox 사용자 가이드", "Flacbox 사용법", "고해상도 음악 플레이어 iPhone", "FLAC 플레이어 iPhone",
  "DSD 플레이어 iOS", "ALAC 플레이어 Mac", "무손실 음악 앱", "클라우드 음악 플레이어 iPhone",
  "오프라인 FLAC 플레이어 Mac", "음악 라이브러리 관리자", "오디오 태그 편집기",
  "CarPlay FLAC 플레이어", "Chromecast 오디오 앱", "AirPlay 2 음악",
  "Flacbox 위젯", "Flacbox CarPlay", "FFmpeg 음악 플레이어 iOS",
  "오디오북 플레이어 iPhone", "오디오 북마크 iOS", "피치 보정 음악 앱",
  "오디오 출력 샘플률", "외부 DAC iPhone", "USB DAC Mac",
  "Synology 음악 앱", "QNAP 음악 앱", "NAS 음악 플레이어 iPhone",
  "WebDAV 음악 플레이어", "SMB 음악 스트리밍", "DLNA 음악 플레이어",
  "iCloud Drive 음악", "Google Drive FLAC", "Dropbox FLAC 플레이어",
  "Wi-Fi Drive 음악 전송", "M3U 재생 목록 가져오기", "Last.fm 스크로블링"
]
tags: ["flacbox", "가이드", "고해상도", "FLAC", "FFmpeg", "클라우드", "CarPlay", "위젯"]
---


### Flacbox 가이드에 오신 것을 환영합니다

Flacbox는 iPhone, iPad, Mac용 고해상도 음악 플레이어로, 즐겨 사용하는 클라우드 스토리지, NAS, 미디어 서버를 나만의 개인 스트리밍 서비스로 만들어 드립니다.

Flacbox는 하나의 앱에서 매우 다양한 소스에 연결됩니다:

- **개인 클라우드 스토리지:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **자체 호스팅 서버:** Plex · Jellyfin · Emby · Subsonic (및 모든 Subsonic 호환 서버 — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (및 공유 API를 통한 ownCloud) · Synology Drive · QNAP.
- **NAS 및 파일 공유 프로토콜:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (비밀번호 또는 공개키 인증) · NFS · DLNA / UPnP (재생 및 다운로드). Apple Time Capsule, Synology, QNAP, WD My Cloud, Linux Samba / NFS / SSH 호스트, Mac 또는 Windows PC의 공유 폴더와 호환됩니다.
- **S3 호환 오브젝트 스토리지:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces 및 기타 S3 API 엔드포인트.
- **로컬 네트워크 검색:** 사용 가능한 기기 섹션이 Wi-Fi의 모든 Bonjour / mDNS 서비스(Plex, Jellyfin, Emby 서버, Synology, QNAP, 드라이브가 연결된 AirPort 라우터, Time Capsule)를 자동으로 나열하므로 IP 주소를 입력하지 않고도 탭하여 연결할 수 있습니다.

대부분의 음악 앱이 Apple의 내장 오디오 엔진만 사용하는 반면, Flacbox는 **FFmpeg**를 시스템 코덱과 함께 번들로 제공하여 iOS에서 기본적으로 지원하지 않는 형식(WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV 및 일반 MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC)을 재생할 수 있습니다. 구성 가능한 오디오 출력 샘플률(44.1 / 48 / 64 / 88.2 / 96 kHz), 다채널 출력(Mono → 5.1 → SDDS → ITU BS.775-1), IO 버퍼 조정, 피치 보정을 통해 Flacbox는 대부분의 소비자 음악 앱이 제공하지 못하는 수준의 오디오파일 제어 기능을 제공합니다.

### 원활한 스트리밍과 오프라인 재생 즐기기

Flacbox는 원활한 스트리밍을 위한 스마트 버퍼링과 내장 다운로드 관리자를 갖추고 있어 전체 재생 목록, 아티스트, 앨범, 폴더 또는 개별 트랙을 기기에 다운로드하여 오프라인으로 사용할 수 있습니다. 저장 공간이 부족하면 캐시 파일을 한 번의 탭으로 지우고 클라우드에서 계속 스트리밍하세요. 폴더, 재생 목록, 앨범, 아티스트에 대한 오프라인 모드는 클라우드에 새 트랙이 나타나는 즉시 자동으로 동기화하므로 오프라인 컬렉션이 항상 최신 상태로 유지됩니다.

### 자동으로 구성된 음악 라이브러리

오디오 트랙을 가져오면 Flacbox가 메타데이터를 스캔하여 곡, 미재생 곡, 앨범, 앨범 아티스트, 아티스트, 장르, 작곡가로 그룹화된 깔끔한 음악 라이브러리로 구성합니다. 내장 검색을 사용하여 몇 초 안에 원하는 항목을 찾고, 소스(온라인 클라우드 / 오프라인 / 기기)별로 필터링하고, 일반 / 그룹 / 탭 라이브러리 레이아웃을 선택하세요. '다양한 아티스트' 컴필레이션이 혼합된 라이브러리의 경우 Flacbox는 전체 앨범 / 독점 앨범 / 솔로 앨범 보기를 제공하여 노이즈 없이 올바른 결과를 표시합니다.

### 메타데이터 수정 및 음악 태그 편집

손상된 태그나 엉킨 인코딩(립핑 또는 오래된 파일에서 흔히 발생하는 문제)을 발견하면 내장 ID3 태그 편집기로 수동 또는 자동 MusicBrainz 조회로 정리할 수 있습니다. 깨진 문자 인코딩을 정규화하고(Windows PC에서 가져온 키릴 문자, 일본어, 중국어 태그에 적합), 누락된 앨범 아트를 검색하고, 변경 사항을 클라우드의 원본 파일에 자동으로 저장할 수 있습니다. 더 깊은 일괄 편집을 위해 동반 앱 Evertag를 설치하세요.

### Mac, PC 또는 NAS에서 손쉬운 전송

SMB, WebDAV, DLNA, Wi-Fi Drive(모든 데스크톱 브라우저에서 드래그 앤 드롭), Lightning 또는 USB-C 케이블을 통한 iTunes / Finder 파일 공유, USB 플래시 드라이브, iXpand 플래시 드라이브 등의 도구를 사용하여 컴퓨터와 iPhone 또는 iPad 사이에서 음악을 이동하세요. Apple Time Capsule, WD My Cloud, Synology, QNAP 또는 SMB / WebDAV / DLNA / FTP / SFTP를 지원하는 기타 NAS가 있으신가요? 한 번 연결하면 기기 저장 공간을 전혀 사용하지 않고 전체 라이브러리를 스트리밍할 수 있습니다.

### 이퀄라이저로 사운드 맞춤 설정

Flacbox는 iPod 스타일 프리셋(Acoustic, Bass Booster, Classical, Dance, Rock, Pop, Jazz 등)이 있는 10밴드 이퀄라이저, 프리앰프, 나만의 프리셋 저장 기능을 포함합니다. 오디오파일 IEM, HomePod mini, 자동차 스테레오 어느 것을 위해 튜닝하든 원하는 대로 사운드를 조정할 수 있습니다.

### 오디오북 친화적

Flacbox는 훌륭한 오디오북 플레이어입니다 — 트랙당 여러 북마크, 세밀한 재생 속도(0.02× ~ 3.00×), 정확히 멈춘 곳에서 재개하는 계속 재생, 맞춤 설정 가능한 건너뛰기 버튼, 취침 시 부드럽게 페이드 아웃되는 수면 타이머. M4B 챕터 마커와 긴 파일을 완벽하게 지원합니다.

### 어디서든 스트리밍 — 자동차와 홈 화면 포함

AirPlay 2를 통해 Apple TV / HomePod로 음악을 스트리밍하고, Google Chromecast 스피커와 Cast 지원 TV로 전송하고, Apple CarPlay로 어디서든 즐길 수 있습니다. iPhone과 iPad의 홈 화면 위젯을 사용하여 현재 재생 중인 트랙을 한눈에 확인하고, Last.fm 스크로블링으로 앱 전체에서 청취 기록을 유지하세요.

### 개인 정보 보호 및 보안

Flacbox는 각 클라우드 제공업체의 공식 SDK와 OAuth 기반 로그인만 사용합니다 — 비밀번호는 앱에 전달되지 않습니다. 액세스 토큰은 iOS Keychain에 암호화되어 저장되고, 모든 전송은 TLS로 보호되며, 클라우드 계정에서 액세스를 취소하거나 기기에서 Flacbox를 제거하면 즉시 모든 것이 삭제됩니다. 추가적인 개인 정보 보호를 위해 선택적 비밀번호로 라이브러리를 보호하세요.

### Flacbox 시작하기

이 가이드는 iPhone, iPad, Mac에서 Flacbox의 모든 부분(클라우드 서비스 연결, 라이브러리 구성, 파일 전송, 재생 목록 관리부터 이퀄라이저 조정 및 오디오 엔진 구성까지)을 안내합니다. 아래 카드를 사용하여 필요한 섹션으로 바로 이동하세요.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="탐색" subtitle="iPhone의 탭 바, iPad 및 Mac의 왼쪽 메뉴, 미니 플레이어, 위젯, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="연결하기" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="음악 라이브러리" subtitle="곡, 앨범, 아티스트, 장르, 작곡가 — 동기화, 검색, 메타데이터 편집." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="재생 목록" subtitle="M3U / M3U8 / CUE 빌드 및 가져오기, 재정렬, M3U / CSV / TXT로 내보내기." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="로컬 파일" subtitle="오프라인 음악, USB 드라이브, Wi-Fi Drive, 파일 관리자, 오프라인 폴더." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="오디오 플레이어" subtitle="고해상도 출력, 이퀄라이저, 피치, 북마크, AirPlay, Chromecast, 속도, 수면 타이머." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="설정" subtitle="오디오 엔진, 라이브러리, 파일 관리자, CarPlay, 위젯, 개인화, 언어, 백업." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="FAQ" subtitle="Flacbox에 관한 50가지 가장 일반적인 질문에 대한 답변을 찾아보세요." >}}

{{< /cards >}}
