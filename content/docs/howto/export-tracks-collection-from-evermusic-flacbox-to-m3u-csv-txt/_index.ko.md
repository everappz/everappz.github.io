---
title: "Evermusic 및 Flacbox에서 트랙 컬렉션을 M3U, CSV, TXT로 내보내는 방법"
date: 2024-01-31
description: "Evermusic와 Flacbox에서 최근 항목, 즐겨찾기, 재생목록, 앨범을 M3U, CSV, TXT 형식으로 내보내는 방법을 알아보세요. Last.fm 스크로블링 및 다른 기기에서의 재생에 적합합니다."
keywords: ["evermusic 내보내기", "flacbox 내보내기", "m3u로 내보내기", "재생목록 csv로 내보내기", "m3u txt csv 재생목록", "음악 내보내기"]
tags: ["evermusic", "최근 항목", "즐겨찾기", "내보내기", "m3u", "재생목록", "csv", "txt", "앨범"]
---

{{< author-byline >}}


**요약:** Evermusic과 Flacbox를 사용하면 모든 트랙 컬렉션(최근 항목, 즐겨찾기, 재생목록, 앨범)을 CSV, TXT 또는 M3U 파일로 내보낼 수 있습니다. 이러한 내보내기를 사용하여 Last.fm에 스크로블하거나, 라이브러리를 백업하거나, 다른 기기에서 재생목록을 재생할 수 있습니다.

## 소개

앱에서 최근 항목, 즐겨찾기, 앨범, 재생목록을 외부 파일로 내보내는 것은 매우 유용합니다. 이러한 파일을 사용하여 [Last.fm](http://Last.fm)과 같은 스크로블러 서비스에서 청취 기록을 업데이트하거나 외부 기기에서 재생목록을 들을 수 있습니다. Evermusic과 Flacbox를 사용하면 이 과정이 간단합니다. 여기서는 최근 항목을 CSV/TXT로, 재생목록을 M3U로 내보내는 방법을 보여드립니다. 단, 이 기능은 앱 내 모든 트랙 컬렉션에서 사용할 수 있습니다.

## 형식 선택

최근 항목을 내보내려면 '음악 라이브러리' 섹션을 열고 '최근 항목' 메뉴 항목을 선택합니다.

![음악 라이브러리](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

다음 화면에서 오른쪽 상단의 '더 보기' 버튼을 탭하고 '곡 목록 내보내기'를 선택합니다.

![최근 항목 내보내기](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

'파일 형식 선택' 화면에서 CSV, TXT, M3U 옵션을 선택할 수 있습니다.

- CSV

쉼표로 구분된 값의 약자로, 데이터를 깔끔한 표 형식으로 정리하기에 적합합니다. 출력 파일에는 아티스트 이름, 앨범 이름, 트랙 이름, 타임스탬프(트랙을 들은 시간), 앨범 아티스트 이름, 트랙 재생 시간 등의 매개변수가 포함됩니다. 이 파일은 [여기](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/)에서 설명한 대로 [Last.fm](http://Last.fm) 등의 스크로블러 서비스에서 청취 기록을 업데이트하는 데 사용할 수 있습니다.

- TXT

일반 텍스트 파일입니다. 단순하고 직관적이며, 아티스트 이름, 앨범 이름, 트랙 이름, 재생 시간 등의 매개변수가 포함됩니다. 텍스트 형식으로 트랙 목록이 필요할 때 유용합니다.

- M3U

이 형식은 재생목록 생성의 표준 형식입니다. 곡 목록을 내보내고 원본 파일 없이도(미디어 파일의 절대 URL 옵션을 선택한 경우) 모든 기기에서 트랙을 즐길 수 있어 좋습니다. 출력 파일에는 재생 시간, 아티스트 이름, 트랙 이름, 미디어 파일 위치 등의 매개변수가 포함됩니다.

## CSV 형식

이제 CSV를 선택하고 결과를 확인해 봅시다. CSV를 선택하고 '내보내기' 버튼을 누르기만 하면 됩니다.

![파일 형식 선택](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

내보내기가 완료되면 두 가지 옵션이 있는 알림이 표시됩니다. '파일 표시'를 탭하면 문서 디렉토리에 생성된 파일이 표시됩니다.

![내보내기 완료](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

이제 해당 파일을 전송하거나, 외부 텍스트 편집기에서 열거나, [Last.fm](http://Last.fm)에서 청취 기록을 업데이트하는 데 사용할 수 있습니다.

![내보내기 결과 파일이 있는 폴더](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

출력 CSV 파일에는 다음 형식으로 필드가 포함됩니다:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

예시:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![내보낸 CSV 파일](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## TXT 형식

출력 TXT 파일에는 다음 형식으로 필드가 포함됩니다:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

예시:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![내보낸 TXT 파일](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## M3U 형식

다음으로 재생목록을 M3U 형식으로 내보내는 방법을 안내합니다. M3U는 재생목록 파일의 사실상 표준입니다. 재생목록 내보내기 성공의 주요 전제 조건은 재생목록의 모든 파일이 동일한 저장소에 있어야 한다는 것입니다. Google Drive와 같은 클라우드 서비스, 로컬 파일, 또는 기기의 파일이 될 수 있습니다. 내보내기 프로세스를 시작하려면 아무 재생목록이나 열고 오른쪽 상단의 '더 보기' 버튼을 탭한 다음 '곡 목록 내보내기' 메뉴 항목을 선택합니다.

![재생목록 화면](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

다음 화면에서 'M3U' 파일 형식을 선택하면 '미디어 파일 위치 유형'에 대한 두 가지 옵션이 나타납니다:

![내보내기 파일 형식 선택 화면](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. '상대 경로'를 선택하면 재생목록 파일 기준 상대 경로로 미디어 파일 위치가 기록됩니다. 예시:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   이 경우 내보내기 완료 후 M3U 파일 위치를 변경하지 마세요. 변경하면 미디어 파일 경로가 깨집니다. 재생목록 재생을 시작하려면 내보낸 재생목록 파일을 탭하기만 하면 앱이 자동으로 저장소에서 미디어 파일을 찾아 재생을 시작합니다. 또한 재생목록을 저장소로 내보낸 다음 새 기기에서 다시 가져올 수도 있습니다.

2. '절대 URL'을 선택하면 앱이 미디어 파일의 직접 URL을 생성합니다. 이를 통해 모든 미디어 파일이 재생목록 파일과 같은 저장소에 있을 필요 없이 모든 기기/애플리케이션에서 재생목록을 재생할 수 있습니다. 이 옵션은 직접 파일 URL을 생성할 수 있는 클라우드 저장소에서만 지원됩니다. 단, 생성된 URL의 유효 기간이 제한되어 일정 시간이 지나면 만료될 수 있습니다. 지원되는 클라우드 서비스 목록: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav(게스트 모드인 경우)  

출력 미디어 파일 URL은 다음과 같습니다:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

'미디어 파일 위치 유형'을 선택한 후 '내보내기'를 탭합니다. 앱에서 M3U 파일의 대상 폴더를 선택하라는 메시지가 표시됩니다. '완료됨'을 탭하여 선택을 확인합니다.

![폴더 선택](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

앱이 M3U 파일을 생성하고 대상 폴더에 업로드/이동합니다.

![M3U 파일 업로드 중](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

내보내기가 완료되면 '파일 표시' 옵션이 있는 시스템 알림이 나타납니다.

![내보내기 완료 알림](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

탭하면 앱에서 내보낸 파일이 표시됩니다.

![파일 목록의 내보낸 M3U 파일](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

이전 단계에서 '미디어 파일 위치 유형'으로 '상대 경로'를 선택한 경우 출력 파일은 다음 형식입니다:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![상대 경로의 M3U 예시](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

'절대 URL' 옵션의 경우 앱이 다음 형식으로 M3U 파일을 생성합니다:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![절대 파일 URL의 M3U 예시](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

M3U 재생목록을 지원하는 모든 기기/애플리케이션에서 해당 파일을 열 수 있습니다.

![외부 앱에서 열린 M3U 재생목록](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## 마무리

Evermusic과 Flacbox에서 트랙을 내보내면 음악 데이터를 완전히 제어할 수 있습니다. 청취 기록 백업, Last.fm 스크로블링, 외부 기기에서의 재생목록 재생 등 M3U, CSV, TXT 내보내기 옵션은 유연성과 호환성을 위한 강력한 도구입니다. 이러한 기능을 활용하여 플랫폼 간에 음악 컬렉션을 정리, 공유, 재방문하는 방식을 향상시키세요.

## FAQ

{{% details title="Last.fm 스크로블링에 어떤 내보내기 형식을 사용해야 하나요?" closed="true" %}}
CSV를 사용하세요. Last.fm-Scrubbler-WPF와 같은 스크로블링 도구에 필요한 타임스탬프와 전체 메타데이터가 포함되어 있습니다.
{{% /details %}}

{{% details title="재생목록뿐만 아니라 다른 트랙 컬렉션도 내보낼 수 있나요?" closed="true" %}}
네. 동일한 단계를 사용하여 최근 항목, 즐겨찾기, 앨범, 재생목록 및 앱 내 기타 모든 트랙 컬렉션을 내보낼 수 있습니다.
{{% /details %}}

{{% details title="M3U 재생목록이 다른 기기에서 작동하나요?" closed="true" %}}
내보내기 시 절대 URL 옵션을 선택하면 M3U 재생목록을 지원하는 모든 기기에서 M3U 파일을 재생할 수 있습니다. 단, 일부 클라우드 URL은 시간이 지나면 만료될 수 있습니다.
{{% /details %}}

{{% details title="내보내기 기능은 무료인가요?" closed="true" %}}
네. M3U, CSV, TXT로 트랙 컬렉션을 내보내는 기능은 Evermusic과 Flacbox의 무료 버전과 프리미엄 버전 모두에서 사용할 수 있습니다.
{{% /details %}}

{{% details title="절대 URL 내보내기를 지원하는 클라우드 서비스는 무엇인가요?" closed="true" %}}
절대 URL 내보내기는 iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive, WebDAV(게스트 모드)에서 지원됩니다.
{{% /details %}}
