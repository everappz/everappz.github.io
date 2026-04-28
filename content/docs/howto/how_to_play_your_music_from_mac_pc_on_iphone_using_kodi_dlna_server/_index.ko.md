---
title: "Kodi DLNA 서버를 사용하여 Mac / PC / Linux / NAS의 음악을 iPhone에서 재생하는 방법"
date: 2025-07-25
description: "Kodi DLNA와 Evermusic 앱을 사용하여 Wi-Fi를 통해 컴퓨터 또는 NAS에서 iPhone으로 음악을 스트리밍합니다."
keywords: ["kodi dlna 서버", "iphone으로 음악 스트리밍", "nas에서 음악 재생", "evermusic dlna", "mac에서 iphone으로 음악", "windows에서 iphone으로 음악", "kodi dlna iphone", "dlna 오디오 스트리밍"]
tags: ["dlna", "kodi", "evermusic", "iphone", "음악 스트리밍", "mac", "nas", "linux", "로컬 네트워크"]
readingTime: 5
---

{{< author-byline >}}


**요약:** Mac, PC, Linux 또는 NAS에 Kodi를 설치하고 DLNA/UPnP 서버를 활성화한 다음, 무료 Evermusic 또는 Flacbox 앱을 사용하여 Wi-Fi를 통해 전체 음악 라이브러리를 iPhone 또는 iPad로 스트리밍하세요. 구독이 필요하지 않습니다.

## 소개

**Mac, Windows PC, Linux 머신 또는 NAS 장치**가 있다면 무료 오픈소스 미디어 플랫폼인 [Kodi](https://kodi.tv/)를 사용하여 쉽게 집에서 **개인 음악 서버**로 변환할 수 있습니다. Kodi의 내장 **DLNA/UPnP 서버**를 사용하면 전체 음악 라이브러리를 DLNA 호환 클라이언트(iPhone 또는 iPad 포함)로 스트리밍할 수 있습니다.

이 가이드에서는 다음 방법을 단계별로 보여드립니다:

- Mac 또는 PC에 Kodi 설치하기  
- 공유를 위한 음악 폴더 설정하기  
- DLNA 음악 서버 활성화하기  
- **Evermusic** 또는 **Flacbox** iOS 앱으로 음악 접근하기

이 설정은 100% 무료입니다 — 구독 없이 Wi-Fi 네트워크를 통해 자신의 음악만 스트리밍합니다. 대규모 MP3 컬렉션을 정리하든, Wi-Fi를 통해 FLAC를 듣든, iTunes 동기화 없이 로컬 음악을 즐기든, 이 설정은 완벽합니다.

## Mac / PC / Linux / NAS에 Kodi 다운로드 및 설치

먼저 Kodi 공식 웹사이트를 방문하세요:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Kodi 메인 페이지" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

**다운로드**를 클릭하고 스크롤하여 컴퓨터용 버전을 찾으세요. 운영 체제를 선택하세요. 이 예에서는 **macOS**를 사용합니다.

{{< cards cols="1">}}
{{< card subtitle="Kodi 다운로드 페이지" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Intel Mac이면 **Intel (x86/64)**을, M1, M2, M3 Mac이면 **Apple Silicon**을 클릭하여 다운로드를 시작하세요.

{{< cards cols="1">}}
{{< card subtitle="macOS 설치 프로그램 선택" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

설치 프로그램이 다운로드되는 동안 잠시 기다려 주세요.

{{< cards cols="1">}}
{{< card subtitle="Kodi 다운로드 완료" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

다운로드 후 **다운로드** 폴더에서 `.dmg` 파일을 찾으세요.

{{< cards cols="1">}}
{{< card subtitle="Kodi 설치" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

다운로드한 파일을 더블클릭하여 설치 프로그램을 실행합니다. Kodi를 **응용 프로그램** 폴더로 드래그하여 설치합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="Kodi를 응용 프로그램으로 드래그하여 설치" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Kodi를 실행합니다. **시스템 환경설정 → 보안 및 개인 정보 보호 → 확인 없이 열기**에서 허용해야 할 수 있습니다.

{{< cards cols="1">}}
{{< card subtitle="Kodi 메인 화면" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Kodi 라이브러리에 음악 추가

홈 화면에서 **톱니바퀴 아이콘**(설정)을 클릭합니다.

{{< cards cols="1">}}
{{< card subtitle="Kodi 설정" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

**미디어 설정 → 라이브러리**로 이동합니다. 자동 인덱싱을 위해 비디오 라이브러리와 음악 라이브러리에 대해 **시작 시 라이브러리 업데이트**를 활성화합니다.

{{< cards cols="1">}}
{{< card subtitle="라이브러리 설정" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

그런 다음 **음악** 섹션으로 이동하여 **음악 추가**를 클릭합니다.

{{< cards cols="1">}}
{{< card subtitle="음악 폴더 추가" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

음악이 저장된 폴더를 찾아 선택합니다.

{{< cards cols="1">}}
{{< card subtitle="음악 소스 선택" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Kodi에 음악 소스를 추가합니다.

{{< cards cols="1">}}
{{< card subtitle="음악 소스 추가" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

확인하고 Kodi가 음악 라이브러리를 스캔하도록 합니다.

{{< cards cols="1">}}
{{< card subtitle="음악 소스 확인" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

라이브러리가 스캔되고 완전히 구축될 때까지 잠시 기다리세요.

{{< cards cols="1">}}
{{< card subtitle="음악 라이브러리 스캔 중" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Kodi DLNA 서버 활성화

**설정 → 서비스 → UPnP/DLNA**로 이동합니다.

옵션을 활성화합니다: **내 라이브러리 공유**.

이제 Kodi가 로컬 Wi-Fi 네트워크에서 DLNA 서버로 작동합니다.

{{< cards cols="1">}}
{{< card subtitle="Kodi에서 DLNA 활성화" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Kodi 라이브러리 열기

오른쪽 클릭으로 설정 창을 닫고 Kodi 메인 라이브러리를 엽니다.

{{< cards cols="1">}}
{{< card title="" subtitle="오른쪽 클릭으로 Kodi 라이브러리 접근" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## iOS용 음악 스트리밍 앱 다운로드

다양한 클라우드 스토리지 서비스와 DLNA 서버에서 음악을 스트리밍할 수 있는 무료 iOS DLNA 클라이언트 앱을 받으세요.

- 컬렉션이 주로 MP3 및 기타 표준 오디오 형식인 경우 **Evermusic**를 사용하세요.
- FLAC, ALAC 또는 DSD와 같은 형식의 하이레즈 음악 라이브러리가 있는 경우 **Flacbox**를 선택하세요.

두 앱 모두 **iOS**와 **macOS**에서 사용 가능하며 무료입니다.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Evermusic 다운로드" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Flacbox 다운로드" icon="download" tag="Free" >}}
{{< /cards >}}

## DLNA 소스 추가

iOS 앱을 다운로드한 후 **모든 연결하기** 섹션을 엽니다.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic 앱 메인 사이드바" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

아래로 스크롤하여 **로컬 네트워크 - 사용 가능한 장치**를 탭하여 DLNA 서버를 검색합니다. 이 섹션에서 로컬 네트워크의 모든 사용 가능한 장치를 볼 수 있습니다. **Kodi DLNA 서버**가 여기에 표시되어야 합니다. Kodi 서버를 탭하여 연결합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic에서 사용 가능한 DLNA 장치" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic이 Kodi를 통해 공유된 라이브러리 폴더를 표시합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic의 Kodi 음악 라이브러리" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

**곡** 폴더로 이동하여 DLNA 서버의 모든 사용 가능한 오디오 파일을 확인합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="원격 폴더의 곡 목록" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

오디오 파일을 탭하여 즉시 스트리밍을 시작합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic에서 MP3 파일 재생" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

**연결하기** 섹션으로 돌아갑니다. 추가된 DLNA 서버가 이제 여기에 표시됩니다. 아이콘을 탭하여 언제든지 다시 연결할 수 있습니다. 같은 단계로 이 화면에서 다른 클라우드 서비스도 연결할 수 있습니다.

여기에서 **Last.fm 스크로블링**도 활성화할 수 있습니다. 재생 통계가 Last.fm 계정에 저장되어 나중에 개인화된 음악 추천을 제공합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic의 연결" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## 음악 라이브러리 구축

**Evermusic**과 **Flacbox** 모두 라이브러리에 음악을 추가하고 아티스트, 앨범, 장르, 작곡가와 같은 **메타데이터 태그**로 정리할 수 있습니다.

시작하려면 **음악 라이브러리** 섹션을 엽니다. **도구 및 환경설정**까지 아래로 스크롤하고 **음악 추가**를 탭합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic 음악 라이브러리" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

음악 소스를 선택합니다 — 이 경우 **연결하기**를 선택합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic에서 새 음악 추가" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

연결에서 **Kodi DLNA 서버**를 찾고 탭하여 폴더와 파일을 확인합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="음악 가져오기를 위한 DLNA 서버 선택" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

추가할 폴더 또는 파일을 선택하고 **완료됨**을 탭합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="추가할 음악 폴더 선택" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

앱이 선택한 파일을 스캔하고 메타데이터를 사용하여 아티스트, 앨범, 장르, 작곡가 등의 섹션으로 정리합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="카테고리가 있는 음악 라이브러리" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## 재생 목록 만들기

자신만의 재생 목록도 만들 수 있습니다.

먼저 **재생 목록** 탭을 엽니다.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic의 재생 목록 탭" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

**플러스(+)** 버튼을 탭하고 **새 재생 목록**을 선택합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="새 재생 목록 만들기" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

재생 목록 이름을 입력하고 **저장하다**를 탭합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="재생 목록 이름 입력" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

다음으로 곡을 추가할 소스를 선택합니다 — 여기서는 **라이브러리**를 선택합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="새 재생 목록에 곡 추가" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

원하는 곡을 선택하고 **완료됨**을 탭하여 추가합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="라이브러리에서 재생 목록에 음악 추가" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

선택한 트랙이 이제 생성된 재생 목록에 표시됩니다.

{{< cards cols="1">}}
{{< card title="" subtitle="생성된 재생 목록이 목록에 표시됨" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

기본적으로 곡은 스트리밍에 사용할 수 있습니다. 오프라인으로 듣려면 **오프라인 모드**를 활성화하세요 — 앱이 모든 재생 목록 트랙을 다운로드합니다.

{{< cards cols="1">}}
{{< card title="" subtitle="재생 목록에 오프라인 모드 활성화됨" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

**추가 작업** 버튼을 탭하여 추가 옵션을 살펴보세요. 다음을 할 수 있습니다:

- 재생 목록 보관  
- 앨범 커버 변경  
- 트랙 순서 변경  
- 기타 유용한 기능

{{< cards cols="1">}}
{{< card title="" subtitle="더 많은 재생 목록 작업 가능" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## 결론

**Evermusic**과 **Flacbox**로 iPhone, iPad 또는 Mac을 강력한 DLNA 음악 플레이어로 변환하는 것은 쉽습니다. 클라우드, NAS 또는 **Kodi**와 같은 홈 미디어 서버에 음악을 저장하든, 이 앱들로 제한 없이 컬렉션을 스트리밍, 정리, 즐길 수 있습니다.

- **Kodi DLNA 서버**에서 직접 MP3 또는 하이레즈 FLAC 스트리밍  
- 메타데이터(앨범, 장르, 작곡가)로 그룹화된 개인 음악 라이브러리 구축  
- **맞춤 재생 목록** 생성 및 관리  
- 이동 중 청취를 위한 **오프라인 모드** 활성화  
- **여러 클라우드 서비스** 및 **로컬 네트워크 장치** 연결  
- **Last.fm 통합**으로 청취 습관 추적

오디오파일이든 캐주얼 리스너이든, Evermusic과 Flacbox는 원활한 음악 스트리밍과 정리에 필요한 모든 것을 제공합니다.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Evermusic 다운로드" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Flacbox 다운로드" icon="download" tag="Free" >}}
{{< /cards >}}

오늘부터 개인 음악 경험을 만들어 보세요.

## FAQ

{{% details title="Kodi는 DLNA 서버로 무료인가요?" closed="true" %}}
네. Kodi는 완전히 무료이며 오픈소스입니다. macOS, Windows, Linux 및 많은 NAS 장치에서 실행됩니다.
{{% /details %}}

{{% details title="Evermusic과 Flacbox는 DLNA를 통한 FLAC 스트리밍을 지원하나요?" closed="true" %}}
네. Flacbox는 FLAC, ALAC, DSD와 같은 하이레즈 형식에 최적화되어 있습니다. Evermusic도 MP3 및 기타 표준 형식과 함께 FLAC 재생을 지원합니다.
{{% /details %}}

{{% details title="Kodi에서 스트리밍한 후 오프라인으로 들을 수 있나요?" closed="true" %}}
네. 재생 목록에서 오프라인 모드를 활성화하면 앱이 모든 트랙을 장치에 다운로드하여 네트워크 연결 없이 들을 수 있습니다.
{{% /details %}}

{{% details title="DLNA를 사용하려면 프리미엄 구독이 필요한가요?" closed="true" %}}
무료 버전은 최대 3개의 클라우드 또는 네트워크 연결을 지원합니다. 프리미엄은 이 제한을 제거하고 무제한 서비스 및 DLNA 서버 연결을 허용합니다.
{{% /details %}}

{{% details title="iPhone이 Kodi와 같은 Wi-Fi 네트워크에 있어야 하나요?" closed="true" %}}
네. DLNA 스트리밍은 로컬 네트워크를 통해 작동합니다. Kodi 서버와 iOS 장치 모두 같은 Wi-Fi 네트워크에 연결되어 있어야 합니다.
{{% /details %}}

{{% details title="Mac이나 PC 대신 NAS로 이 설정을 사용할 수 있나요?" closed="true" %}}
네. 많은 NAS 장치(Synology, QNAP 등)가 Kodi를 지원하거나 자체 내장 DLNA 서버를 가지고 있습니다. Evermusic과 Flacbox는 모든 표준 DLNA/UPnP 서버에 연결할 수 있습니다.
{{% /details %}}
