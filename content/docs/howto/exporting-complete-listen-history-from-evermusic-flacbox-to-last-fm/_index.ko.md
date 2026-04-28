---
title: "Evermusic & Flacbox에서 Last.fm으로 전체 청취 기록 내보내기"
date: 2024-01-30
description: "CSV 파일과 Windows용 Last.fm Scrubbler 도구를 사용하여 Evermusic과 Flacbox에서 음악 기록을 내보내고 Last.fm에 업로드하는 방법을 알아보세요."
keywords: ["evermusic", "flacbox", "lastfm", "음악 기록", "스크로블링", "트랙 내보내기", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "최근 항목", "lastfm", "내보내기", "scrobbler"]
readingTime: 5
---


{{< author-byline >}}


**요약:** Evermusic 또는 Flacbox에서 청취 기록을 CSV 파일로 내보낸 다음 Windows에서 무료 Last.fm-Scrubbler-WPF 도구를 사용하여 Last.fm에 업로드하세요. 자동 스크로블링도 두 앱에서 기본적으로 사용할 수 있습니다.

**업데이트:** 자동 스크로블링이 이제 사용 가능합니다! 자세한 내용은 여기에서 확인하세요: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

스크로블링은 현재 재생 중인 노래의 제목과 아티스트와 같은 기본 세부 정보를 온라인 서비스에 자동으로 저장하는 간단한 방법입니다. 나중에 청취 기록을 검토할 수 있습니다.

[Last.fm](https://www.last.fm/home)는 Audioscrobbler라는 음악 추천 시스템을 기반으로 이 서비스를 무료로 제공합니다. 인터넷 라디오 방송국, 컴퓨터 또는 다양한 휴대용 음악 장치에서 듣는 트랙을 기록하여 음악 취향의 상세한 프로필을 만듭니다. 나중에 웹사이트를 방문하여 음악 취향에 맞는 새로운 아티스트나 앨범에 대한 추천을 받을 수 있습니다.

다음에서 청취 기록을 업로드할 수 있습니다: [Last.fm](http://Last.fm) Evermusic과 Flacbox 앱에서 무료 도구를 사용하여, 이 방법을 안내해 드리겠습니다.

앱의 '음악 라이브러리' 섹션을 열고 '빠른 액세스' 섹션으로 스크롤합니다. '최근 항목' 메뉴 항목을 탭합니다.

![음악 라이브러리 화면](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

'최근 항목' 화면에서 오른쪽 상단의 '더보기' 버튼을 탭하여 '추가 작업' 메뉴를 활성화합니다. '노래 목록 내보내기' 메뉴 항목을 탭합니다.

![최근 항목 화면](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

'파일 형식 선택' 화면에서 대상 파일의 형식을 선택할 수 있습니다. 사용 가능한 옵션 - CSV, TXT, M3U.

![파일 형식 선택 화면](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: 쉼표로 구분된 값을 의미하며, 데이터를 깔끔한 표 형식으로 정리하는 데 완벽합니다. 대상 파일에는 아티스트 이름, 앨범 이름, 트랙 이름, 타임스탬프(트랙을 들은 시간), 앨범 아티스트 이름, 트랙 재생 시간과 같은 매개변수가 있습니다.

TXT: 여기서는 일반 텍스트 파일을 말합니다. 간단하고 직관적이며, 아티스트 이름, 앨범 이름, 트랙 이름, 재생 시간을 포함합니다.

M3U: 이 형식은 재생 목록 생성의 표준입니다. 원본 파일이 없어도(미디어 파일의 절대 URL 옵션을 선택한 경우) 노래 목록을 내보내고 모든 장치에서 트랙을 즐길 수 있어 유용합니다. 출력 파일에는 재생 시간, 아티스트 이름, 트랙 이름, 미디어 파일 위치와 같은 매개변수가 있습니다.

우리의 작업에는 CSV를 선택하는 것이 올바른 방법입니다. 이 파일을 무료 소프트웨어 Last.fm-Scrubbler-WPF와 함께 사용하여 청취 기록을 [Last.fm](http://Last.fm) 서비스에 업로드합니다. CSV를 선택하고 '내보내기' 버튼을 누르세요.

![내보내기 완료 화면](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

내보내기가 완료되면 '파일 표시' 버튼을 탭하면 앱이 문서 폴더에 생성된 파일을 표시합니다. 그런 다음 파일 이름 옆의 '추가 작업' 버튼을 탭하고 메뉴에서 '다음에서 열기' 옵션을 선택합니다. 다음 단계는 내보낸 파일을 데스크톱 컴퓨터로 복사하는 것입니다. '다음에서 열기' 메뉴에서 AirDrop 옵션을 선택하면 쉽게 할 수 있습니다.

![내보낸 파일에 대한 추가 작업](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

다음으로 Windows 플랫폼에서만 사용 가능한 무료 오픈소스 [Last.FM](http://Last.FM) 클라이언트를 사용합니다. 이 클라이언트를 사용하면 방금 내보낸 CSV 파일을 사용하여 [Last.FM](http://Last.FM) 에서 청취 기록을 효율적으로 업데이트할 수 있습니다.

현재 Windows 컴퓨터를 사용하고 있지 않더라도 걱정하지 마세요. Mac에 VirtualBox를 설치하고 공식 Windows 개발 환경 이미지 파일을 사용하여 이 클라이언트에 액세스할 수 있습니다.

다음은 수행해야 할 작업입니다:

- 다음 링크에서 VirtualBox를 설치하세요: [VirtualBox 다운로드](https://www.virtualbox.org/wiki/Downloads)

- 이 링크에서 Windows 개발 환경을 다운로드하고 설치하세요: [Windows 개발 환경](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Windows 컴퓨터(또는 Windows Development 이미지가 있는 VirtualBox 앱)에서 다운로드 및 설치하세요: [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - GitHub에서 사용 가능한 무료 오픈소스 소프트웨어입니다. 버전 1.28에서 테스트했으며 여기에서 다운로드할 수 있습니다: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Last.fm-Scrubbler-WPF 다운로드 페이지](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

'Assets' 섹션에서 [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) 을 탭하여 설치 아카이브를 다운로드합니다. 다운로드한 파일의 압축을 풀고 압축 해제된 폴더를 엽니다.

- 중요

이 앱은 아직 베타 버전입니다. 앱 제작자들은 많은 테스트를 하지 않았습니다. 먼저 테스트 계정에 스크로블을 시도하고 스크로블하려는 항목이 올바르게 작동하는지 확인하는 것을 권장합니다. 특히 한 번에 많은 트랙을 스크로블하는 경우에는 더욱 주의하세요. 계정에 주의하세요.

Last.fm-Scrubbler-WPF.exe를 실행합니다

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

앱의 메인 화면에서 왼쪽 하단에 있는 '로그인하지 않음'을 탭하여 '계정 추가' 화면을 활성화합니다.

![계정 추가 화면](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

로그인 자격 증명을 입력합니다.

![로그인 자격 증명 입력 화면](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

'로그인' 버튼을 탭하여 계정을 추가합니다.

!['로그인' 버튼을 탭하여 계정을 추가합니다.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

'File Parse Scrobbler' 탭을 열어 Evermusic 앱에서 CSV 파일 가져오기를 시작합니다.

!['File Parse Scrobbler' 탭을 열어 Evermusic 앱에서 CSV 파일 가져오기를 시작합니다.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

'Parser: CSV'를 선택하고 '설정' 버튼을 탭합니다.

다음 화면에서 CSV 파일의 매개변수 순서를 선택할 수 있습니다.

개별 필드는 따옴표로 묶을 수 있으며 필드에 설정된 구분 기호가 포함된 경우 따옴표로 묶어야 합니다. 예:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

모든 설정을 기본값으로 두고 변경해야 할 유일한 것은 'Has Fields Enclosed In Quotes' 필드의 체크박스를 활성화하는 것입니다.

'저장 및 닫기'를 탭하여 변경사항을 적용합니다.

![CSV 파일의 매개변수 순서를 선택합니다.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

파일 구문 분석 스크로블링에는 두 가지 모드가 있습니다. 'Scrobbling Mode' 콤보박스로 변경할 수 있습니다.

일반 모드: 이 모드에서는 구문 분석된 스크로블의 타임스탬프로 트랙이 스크로블됩니다. 14일 이내의 스크로블만 스크로블할 수 있습니다.

가져오기 모드: 이 모드에서는 '종료 시간'과 각 트랙 사이의 선택된 재생 시간에서 계산된 타임스탬프로 트랙이 스크로블됩니다. 이를 통해 구문 분석된 스크로블의 타임스탬프가 14일 이상이 되어도 트랙을 스크로블할 수 있습니다. 따라서 CSV 파일의 첫 번째(최상위) 트랙이 '종료 시간'으로 스크로블됩니다.

Evermusic 앱에서 이전에 생성된 CSV 파일을 'File:' 필드에서 선택하고 'Parse'를 탭합니다. 경우에 따라 일부 스크로블을 구문 분석할 수 없다는 오류 알림이 표시될 수 있습니다. 아티스트 이름과 같은 완전한 메타데이터가 없는 트랙이 있으면 괜찮습니다.

![일부 스크로블을 구문 분석할 수 없습니다](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

'모두 선택' 버튼을 탭하여 구문 분석된 모든 트랙을 선택합니다.

!['모두 선택' 버튼을 탭하여 구문 분석된 모든 트랙을 선택합니다.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

'미리보기' 버튼을 탭하여 서버에 게시될 모든 변경사항을 확인합니다.

!['미리보기' 버튼을 탭하여 서버에 게시될 모든 변경사항을 확인합니다.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

'Scrobble' 버튼을 탭하여 모든 변경사항을 서버에 업로드합니다.

!['Scrobble' 버튼을 탭하여 모든 변경사항을 서버에 업로드합니다.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

이전에는 Last.fm-Scrubbler-WPF에 일일 스크로블 제한이 없었습니다. 일부 사용자가 Scrubbler를 사용하여 너무 많은 트랙을 스크로블하여 Last.fm 페이지에 문제를 일으켰기 때문에 이제 변경되었습니다. 스크로블 제한은 현재 하루 2800 스크로블입니다. 그 이상 스크로블하려고 하면 오류 메시지가 표시됩니다. '스크로블 대기열'을 추가할 계획이 있으므로 2800개 이상의 트랙을 스크로블해야 하는 경우 대기열에 추가되어 일정 시간 후 자동으로 스크로블됩니다. 사용자 선택 보기에서 남은 스크로블 수를 확인할 수 있습니다.

모든 기록이 서버에 성공적으로 업로드되면 앱 창 하단에 '선택한 트랙이 성공적으로 스크로블되었습니다'라는 확인 메시지가 표시됩니다.

![선택한 트랙이 성공적으로 스크로블되었습니다.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

이제 [Last.fm](http://Last.fm) 페이지에서 프로필을 열고 모든 변경사항을 확인할 수 있습니다.

![Last.fm 페이지의 프로필](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## 자주 묻는 질문

{{% details title="CSV 파일을 내보내지 않고 자동으로 스크로블할 수 있나요?" closed="true" %}}
네. Evermusic과 Flacbox 모두 이제 자동 Last.fm 스크로블링을 지원합니다. 가이드를 참조하세요: [Last.fm에 스크로블하는 방법](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="CSV에 14일 이상 된 트랙이 있으면 어떻게 하나요?" closed="true" %}}
Last.fm-Scrubbler-WPF에서 가져오기 모드를 사용하세요. 종료 시간에서 타임스탬프를 재계산하여 원래 날짜에 관계없이 트랙을 스크로블할 수 있습니다.
{{% /details %}}

{{% details title="Windows 컴퓨터가 없습니다. Last.fm-Scrubbler를 사용할 수 있나요?" closed="true" %}}
네. Mac에 VirtualBox를 설치하고 Microsoft에서 무료 Windows 개발 환경 이미지를 다운로드하세요. 가상 머신 내에서 Last.fm-Scrubbler-WPF를 실행하세요.
{{% /details %}}

{{% details title="일부 스크로블이 구문 분석되지 않는 이유는 무엇인가요?" closed="true" %}}
필수 메타데이터(예: 아티스트 이름)가 누락된 트랙은 구문 분석할 수 없습니다. 이는 예상된 것이며 파일의 다른 트랙에는 영향을 미치지 않습니다.
{{% /details %}}

{{% details title="일일 스크로블 제한이 있나요?" closed="true" %}}
네. Last.fm-Scrubbler-WPF는 하루 최대 2,800 스크로블을 허용합니다. 더 많이 스크로블해야 하는 경우 프로세스를 여러 날에 나누세요.
{{% /details %}}
