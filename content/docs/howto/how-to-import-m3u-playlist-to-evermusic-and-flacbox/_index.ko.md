---
title: "Evermusic 및 Flacbox에 M3U 재생 목록을 가져오는 방법"
date: 2024-01-31
description: "클라우드, 로컬 저장소 또는 기기에서 M3U, M3U8, CUE 재생 목록 파일을 Evermusic 및 Flacbox로 가져오는 방법을 알아보세요."
keywords: ["evermusic", "flacbox", "재생 목록", "m3u", "m3u8", "cue", "가져오기", "음악 앱"]
tags: ["evermusic", "가져오기", "재생 목록", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**요약:** Evermusic과 Flacbox는 클라우드 저장소, 로컬 앱 파일 또는 기기에서 M3U, M3U8, CUE 재생 목록 파일 가져오기를 지원합니다. 재생 목록 > 더보기 > 재생 목록 가져오기로 이동하여 소스를 선택하고 파일을 고른 후 앱이 자동으로 재생 목록을 생성합니다.

M3U는 MP3 URL 또는 Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator의 약자로, 멀티미디어 재생 목록에 사용되는 컴퓨터 파일 형식입니다. 주요 용도 중 하나는 인터넷 스트림을 가리키는 단일 항목 재생 목록 파일을 만드는 것입니다. 이러한 파일은 스트리밍 콘텐츠에 편리하게 접근할 수 있게 해주며 다운로드, 이메일 전송, 인터넷 라디오 청취에 일반적으로 사용됩니다.

광범위하게 사용됨에도 불구하고 M3U 형식에 대한 공식 사양은 없으며 사실상의 표준이 되었습니다. M3U 파일은 본질적으로 하나 이상의 미디어 파일 위치를 지정하는 일반 텍스트 파일입니다. 인코딩에 따라 "m3u" 또는 "m3u8" 파일 확장자로 저장됩니다. 파일의 각 항목은 미디어 파일의 위치를 지정하며, 이는 절대 로컬 경로명, M3U 파일 위치에 상대적인 로컬 경로명 또는 URL일 수 있습니다. 항목은 줄 바꿈으로 구분되며, 일부 기기에서는 CR LF로 표시되는 줄 바꿈이 필요합니다.

또한 M3U 파일에는 "#" 문자로 시작하는 주석을 포함할 수 있습니다. 확장 M3U에서 "#"은 확장 M3U 지시문을 도입하며, 콜론 ":"으로 끝나는 매개변수를 지원할 수 있습니다.

Evermusic과 Flacbox 앱에서는 M3U 파일 가져오기 기능을 구현하여 수동으로 재생 목록을 만들 필요가 없습니다. 이 가이드는 클라우드 저장소, 로컬 파일 또는 기기의 파일에서 재생 목록을 앱으로 직접 가져오는 방법을 안내합니다.

먼저 '재생 목록' 섹션으로 이동합니다. 다음으로 오른쪽 상단에 있는 '더보기' 버튼을 탭합니다. 나타나는 메뉴에서 '재생 목록 가져오기' 옵션을 선택합니다.

![재생 목록 가져오기 동작](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

다음 화면에서 파일 위치를 선택합니다. 지원되는 옵션은 다음과 같습니다:

- 연결된 클라우드 저장소;
- 앱 내 파일;
- 기기의 파일;

![파일 위치 선택](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

연결된 클라우드 저장소를 선택하고 재생 목록 파일이 포함된 폴더를 엽니다. 지원되는 재생 목록 파일 확장자에는 M3U, M3U8, CUE가 있습니다. 재생 목록 파일을 선택하고 '완료됨'을 탭하여 선택을 확인합니다.

![M3U 파일 선택](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

앱이 재생 목록 파일을 분석하고 트랙 목록을 생성합니다. 그런 다음 저장소에서 해당 파일을 찾아 음악 라이브러리로 가져올 최종 재생 목록을 컴파일합니다. M3U/CUE 파일에 미디어 파일의 올바른 경로가 포함되어 있어야 하며, 파일이 저장소의 해당 경로에 위치해야 합니다.

![가져온 재생 목록](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

앱은 상대 경로와 절대 파일 URL을 모두 지원합니다.

예시:

상대 경로를 사용한 재생 목록:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

절대 URL을 사용한 재생 목록:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

앱 내(로컬 파일 섹션)에 있는 재생 목록 파일을 가져오는 경우 추가 단계가 필요하지 않습니다.

그러나 시스템 파일 선택기를 사용하여 기기에 있는 재생 목록을 가져오려면 중요한 사항을 알아두어야 합니다.

보안 정책으로 인해 앱은 시스템 파일 선택기를 사용하여 선택한 파일에만 접근할 수 있습니다. 그러나 재생 목록 파일에는 기기의 다른 미디어 파일에 대한 링크가 포함될 수 있습니다. 기기에서 재생 목록을 가져오려면 재생 목록 파일과 연결된 모든 미디어 파일이 포함된 폴더를 선택해야 합니다. 이 경우 앱이 선택한 폴더를 스캔하고 재생 목록 파일을 찾아 트랙 목록을 구성하고 음악 라이브러리로 가져옵니다.

또한 "추가 작업" 버튼을 탭하고 "폴더에서 재생 목록 가져오기"를 선택하여 한 번에 여러 재생 목록을 가져올 수 있습니다. 앱이 폴더의 콘텐츠를 스캔하고 지원되는 재생 목록 파일을 찾아 라이브러리로 가져옵니다.

## 자주 묻는 질문

{{% details title="Evermusic과 Flacbox는 어떤 재생 목록 형식을 지원하나요?" closed="true" %}}
두 앱 모두 M3U, M3U8, CUE 재생 목록 파일 형식을 지원합니다. 이는 음악 플레이어와 미디어 소프트웨어에서 사용되는 가장 일반적인 재생 목록 표준을 포함합니다.
{{% /details %}}

{{% details title="클라우드 저장소에서 재생 목록을 가져올 수 있나요?" closed="true" %}}
네. Google Drive, Dropbox, OneDrive, WebDAV 서버를 포함한 모든 연결된 클라우드 저장소 서비스에서 재생 목록 파일을 가져올 수 있습니다.
{{% /details %}}

{{% details title="가져오기 후 일부 트랙이 누락되는 이유는 무엇인가요?" closed="true" %}}
재생 목록 파일에 미디어 파일의 올바른 경로가 포함되어 있어야 하며, 해당 파일이 저장소의 지정된 위치에 존재해야 합니다. M3U 또는 CUE 파일의 파일 경로가 실제 파일 위치와 일치하는지 다시 확인하세요.
{{% /details %}}

{{% details title="한 번에 여러 재생 목록을 가져올 수 있나요?" closed="true" %}}
네. 추가 작업 버튼을 사용하고 "폴더에서 재생 목록 가져오기"를 선택하세요. 앱이 폴더에서 지원되는 모든 재생 목록 파일을 스캔하고 한 번에 가져옵니다.
{{% /details %}}

{{% details title="재생 목록을 수동으로 만들어야 하나요?" closed="true" %}}
아니요. 가져오기 기능으로 수동 재생 목록 생성이 필요 없습니다. 기존 M3U, M3U8 또는 CUE 파일을 앱에 지정하기만 하면 자동으로 재생 목록이 생성됩니다.
{{% /details %}}
