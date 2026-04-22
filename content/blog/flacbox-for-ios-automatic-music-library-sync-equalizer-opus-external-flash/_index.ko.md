---
title: "Flacbox 1.6: 자동 동기화, 이퀄라이저, OPUS 지원"
date: 2017-01-25
description: "Flacbox 1.6 iOS용은 자동 클라우드 동기화, 10밴드 이퀄라이저, OPUS 형식 지원, iPhone 및 iPad용 외장 플래시 드라이브 재생을 추가합니다."
keywords: ["Flacbox 업데이트", "FLAC 플레이어 iOS", "10밴드 이퀄라이저 iPhone", "자동 음악 동기화", "iPhone에서 OPUS 재생", "외장 플래시 드라이브 음악", "FLAC 스트리밍 iOS", "hi-res 음악 앱 iPhone", "Flacbox 이퀄라이저", "SD 카드 음악 플레이어 iOS"]
tags: ["Flacbox", "이퀄라이저", "음악 라이브러리", "OPUS", "FLAC", "외부 저장소", "동기화", "오디오 플레이어", "iOS 앱", "업데이트"]
draft: false
aliases:
  - /post/flacbox-for-ios-automatic-music-library-sync-equalizer-opus-external-flash/
  - /amp/flacbox-for-ios-automatic-music-library-sync-equalizer-opus-external-flash/
  - /single-post/Flacbox-for-iOS-Automatic-Music-Library-Sync-Equalizer-OPUS-External-Flash/
  - /index.php/2017/01/25/flacbox-1-6-for-ios-automatic-music-library-sync-10-band-equalizer-opus-file-format-external-flash-support/
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-cofounder-everappz.webp"
---

{{< author-byline >}}

**Flacbox 1.6**은 iPhone과 iPad용 FLAC 음악 플레이어에 주요 새 기능을 제공합니다.

**요약:** 이 업데이트는 자동 클라우드 라이브러리 동기화, 커스텀 프리셋이 있는 10밴드 이퀄라이저, OPUS 형식 지원, 외부 SD 카드에서 음악 재생 기능을 추가합니다. FLAC 재생 버그도 수정되었습니다.

## Flacbox 1.6의 새로운 기능

### 자동 클라우드 음악 라이브러리 동기화

더 이상 수동으로 라이브러리를 새로고침할 필요가 없습니다. 새로운 동기화 엔진이 선택한 클라우드 폴더를 자동으로 스캔하고 실시간으로 음악 라이브러리를 업데이트합니다.

- 활성화: **Settings → Music Library → Automatic Sync**
- **Sync Folder → Change Settings**에서 폴더 선택
- 동기화 모드 선택: Wi-Fi 전용 또는 Wi-Fi + 셀룰러
- 플레이어 활성 시 자동 업데이트를 위한 **Background Sync** 활성화 (배터리 사용량 증가)

수동 개입 없이 클라우드 음악 컬렉션이 최신 상태로 유지됩니다.

### 커스텀 사운드를 위한 10밴드 이퀄라이저

내장 **10밴드 이퀄라이저**로 오디오를 조정하세요. 플레이어 화면이나 설정에서 접근할 수 있습니다.

- **-12 dB**에서 **+12 dB** 사이의 주파수 조정
- 내장 프리셋 사용 또는 나만의 프리셋 생성
- 프리앰프 파워 미세 조정 (청력 보호를 위해 주의)

iPhone이나 iPad에서 스튜디오 수준의 오디오 제어가 가능합니다.

### OPUS 파일 형식 지원

Flacbox는 이제 FLAC, ALAC, MP3 및 기타 형식과 함께 **OPUS** 파일을 재생합니다. OPUS는 음성과 음악에 널리 사용되는 고효율 코덱입니다. OPUS 재생에도 전체 이퀄라이저 지원이 포함됩니다.

### 외부 SD 카드에서 음악 재생

iPhone이나 iPad에 연결된 SD 또는 microSD 카드에서 직접 음악을 재생하세요:

- **Lightning to SD Card Camera Reader Adapter** 사용
- 카드를 삽입하고 장치에 연결
- Flacbox를 열면 카드가 자동 인식
- **Services → PowerDrive** 섹션에서 파일 탐색 및 재생

장치 저장소를 사용하지 않고 음악 라이브러리를 확장하기에 이상적입니다.

### FLAC 재생 버그 수정

FLAC 파일 끝에서 **2초가 건너뛰는** 문제가 완전히 해결되었습니다. 이제 처음부터 끝까지 원활하게 재생됩니다.

## Flacbox 다운로드

Flacbox 1.6은 현재 App Store에서 이용 가능합니다. [Flacbox 다운로드](https://itunes.apple.com/us/app/flacbox-flac-player-music/id1097564256?mt=8)하고 오늘 이 기능들을 체험하세요.

피드백이나 기능 요청이 있으시면 연락주세요 -- 사용자가 필요한 것을 기반으로 Flacbox를 만듭니다.

## 자주 묻는 질문

{{% details title="Flacbox는 어떤 오디오 형식을 지원하나요?" closed="true" %}}
Flacbox는 FLAC, ALAC, MP3, AAC, OGG, OPUS, WAV, AIFF, DSD 및 기타 인기 오디오 형식을 지원합니다. 모든 형식이 내장 이퀄라이저와 함께 작동합니다.
{{% /details %}}

{{% details title="iPhone에서 SD 카드의 음악을 재생할 수 있나요?" closed="true" %}}
네. Lightning to SD Card Camera Reader Adapter를 사용하여 SD 또는 microSD 카드를 연결하세요. Flacbox가 자동으로 카드를 감지하고 외부 저장소에서 직접 파일을 탐색하고 재생할 수 있습니다.
{{% /details %}}

{{% details title="Flacbox는 클라우드 저장소와 자동으로 동기화하나요?" closed="true" %}}
네. 버전 1.6부터 Flacbox는 클라우드 폴더에서 음악 라이브러리를 자동으로 동기화할 수 있습니다. 설정에서 Automatic Sync를 활성화하고 모니터링할 폴더를 선택하세요.
{{% /details %}}

{{% details title="Flacbox 이퀄라이저는 사용자 정의 가능한가요?" closed="true" %}}
네. 10밴드 이퀄라이저를 사용하면 -12 dB에서 +12 dB 사이에서 개별 주파수 레벨을 조정할 수 있습니다. 내장 프리셋을 사용하거나 나만의 커스텀 설정을 저장할 수 있습니다.
{{% /details %}}
