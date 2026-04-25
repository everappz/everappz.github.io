---
title: "Evermusic에서 기기 간 음악 라이브러리를 전송하는 방법: 단계별 가이드"
description: "Wi-Fi Drive 및 백업 도구를 사용하여 Evermusic 음악 라이브러리, 재생 목록, 앨범 아트워크 및 설정을 하나의 iPhone, iPad 또는 Mac에서 다른 기기로 쉽게 전송하세요."
date: 2024-12-29
tags: ["음악라이브러리", "전송", "wifi", "백업", "webdav", "복원"]
keywords: ["Evermusic 음악 라이브러리 전송", "Evermusic 재생 목록 백업 및 복원", "Evermusic WiFi Drive", "기기 간 Evermusic 동기화", "Evermusic 데이터베이스 이동", "Evermusic 파일 전송", "오디오 플레이어 설정 복원", "WebDAV 음악 전송 iOS"]
readingTime: 3
---

{{< author-byline >}}


**요약:** Evermusic 라이브러리를 새 기기로 전송하려면 원본 기기에서 백업을 생성하고, Wi-Fi Drive를 시작한 후, 같은 네트워크에서 두 번째 기기를 연결하고, 백업 및 음악 파일을 다운로드한 다음 백업에서 복원하세요. 전체 과정은 라이브러리 크기에 따라 약 10분 정도 소요됩니다.

이 가이드에서는 데이터베이스, 앨범 커버 및 설정을 포함한 전체 음악 라이브러리를 하나의 기기(iPhone 또는 Mac)에서 다른 기기로 전송하는 과정을 안내합니다. 자동 음악 라이브러리 및 재생 목록 동기화는 향후 계획된 기능이지만, 현재는 이 과정을 수동으로 수행해야 합니다.

## 1단계: 첫 번째 기기에서 백업 생성

1. **첫 번째 기기에서 앱을 엽니다** (음악 라이브러리, 재생 목록 및 연결된 클라우드 서비스가 있는 기기).
2. **설정**으로 이동하여 **백업 및 복원** 옵션을 선택합니다.

![Backup and Restore](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. **백업 및 복원** 화면에서 백업 파일에 포함할 항목을 선택합니다:
   - **데이터베이스** (음악 라이브러리 및 재생 목록 포함)
   - **앨범 커버**
   - **설정**

이 옵션들은 기본적으로 활성화되어 있습니다.

![Backup Options](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. **애플리케이션 데이터 백업**을 탭하여 프로세스를 시작합니다.

![Backup Application Data](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. 백업이 완료되면 정보 알림이 나타납니다.

![Backup Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

**파일 표시**를 탭하여 **문서** 디렉토리에서 백업 파일을 확인합니다. 백업 파일은 일반적으로 **Backup** 폴더에 저장됩니다.

![Show Backup File](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## 2단계: Wi-Fi Drive 서버 시작

1. 앱에서 **연결하기** 섹션으로 이동합니다.
2. **Wi-Fi를 사용하여 연결**로 스크롤하여 탭합니다.

![Connect Using Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. 다음 화면에서 **Wi-Fi Drive 시작**을 탭합니다.

- 선택적으로 보안을 위해 로그인 및 비밀번호를 설정할 수 있지만, 가정용 네트워크에서는 불필요합니다.

4. 시작되면 사용 가능한 서버 주소가 표시됩니다. 이는 데스크톱 브라우저나 WebDAV 앱에 사용할 수 있지만, 이 가이드에서는 다음 단계로 바로 진행합니다.

![Wi-Fi Drive Started](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## 3단계: 두 번째 기기를 첫 번째 기기에 연결

1. 두 번째 기기에서 앱을 엽니다(라이브러리를 전송하려는 기기).
2. 두 기기가 동일한 Wi-Fi 네트워크에 연결되어 있는지 확인합니다.
3. 두 번째 기기에서 **연결하기** 탭을 열고 **사용 가능한 장치**를 선택합니다.

![Available Devices](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. **Evermusic**이라는 이름의 WebDAV 연결이 표시됩니다(첫 번째 기기에서 시작한 서버). 탭하여 연결합니다.

5. 연결되면 첫 번째 기기의 모든 폴더가 표시됩니다.

![Connected to First Device](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## 4단계: 파일 전송 준비

1. 두 번째 기기에서 **설정 > 파일 관리자**로 이동하여 **다운로드한 파일 저장 위치 - 매번 묻기**를 활성화합니다.

- 이렇게 하면 각 다운로드에 대한 대상 폴더를 선택할 수 있습니다.

2. **연결하기** 탭으로 돌아가서 연결된 WebDAV 서버로 이동합니다.

![Prepare for File Transfers](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## 5단계: 백업 및 음악 파일 전송

1. 연결된 WebDAV 서버에서 **Backup** 폴더를 엽니다.

![Backup Folder](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. 백업 파일 옆의 **추가 작업** 버튼(점 세 개)을 탭하고 **다운로드**를 선택합니다.

3. 두 번째 기기에 다운로드한 파일을 저장할 **Backup** 폴더를 만듭니다. **완료됨**을 탭하여 선택을 확인합니다.

![Download Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. 추가 음악 파일을 전송합니다:
   - WebDAV 서버의 **다운로드** 폴더 또는 기타 관련 폴더를 확인합니다.

![Transfer Music Files](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- **선택하다** 옵션을 사용하여 파일을 선택한 다음 **추가 작업 > 다운로드**를 탭합니다. 동일한 디렉토리 구조를 유지하기 위해 두 번째 기기의 해당 폴더에 저장합니다.

목표는 첫 번째 기기의 모든 파일을 현재 기기로 전송하여 폴더 구조가 동일하게 유지되도록 하는 것입니다. 이렇게 하면 음악 라이브러리와 재생 목록의 링크가 그대로 유지됩니다. 첫 번째 기기의 앱 문서 디렉토리 외부에 저장된 로컬 파일은 별도로 전송해야 합니다. Wi-Fi Drive 모드에서는 앱이 이러한 파일에 접근할 수 없으므로 시스템 파일 앱을 사용하여 전송해야 합니다.

![Transfer Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## 6단계: 전송 진행 상황 모니터링

1. 두 번째 기기에서 **로컬 파일** 섹션(또는 iPad/Mac의 **다운로드** 탭)으로 이동합니다.

2. 왼쪽 상단의 **전송 활동** 버튼을 탭하여 전송 대기열을 모니터링합니다.

![Monitor Transfer](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## 7단계: 백업에서 데이터 복원

1. 백업 파일과 필요한 모든 오디오 파일이 두 번째 기기에 다운로드되면 **Backup** 폴더를 엽니다.

2. 백업 파일을 탭하면 확인 메시지가 나타납니다.

![Restore Backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **참고:** 복원하면 현재 음악 라이브러리 데이터, 재생 목록, 설정 및 앨범 아트워크가 모두 백업 데이터로 대체됩니다.

3. **복원**을 탭하여 프로세스를 시작합니다.

![Restore Process](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. 복원이 완료되면 성공 알림이 표시됩니다.

![Restoration Complete](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

**재생 목록** 또는 **음악 라이브러리** 섹션을 확인하여 복원을 검증합니다.

![Verify Restoration](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## 8단계: 음악 라이브러리 재인덱싱

1. 최상의 결과를 위해 모든 파일이 성공적으로 감지되었는지 확인하기 위해 라이브러리를 재인덱싱합니다.

2. **설정 > 음악 라이브러리 > 오프라인 음악 동기화**로 이동하여 **로컬 폴더 스캔 시작**을 선택합니다.

이 단계를 따르면 음악 라이브러리, 재생 목록 및 설정을 다른 기기로 성공적으로 전송할 수 있습니다. 문제가 발생하면 언제든지 지원팀에 문의하세요.

## 자주 묻는 질문

{{% details title="Wi-Fi 없이 Evermusic 라이브러리를 전송할 수 있나요?" closed="true" %}}
Wi-Fi Drive는 두 기기가 동일한 Wi-Fi 네트워크에 있어야 합니다. 현재 블루투스 또는 셀룰러 전송 옵션은 없습니다. 대안으로 AirDrop 또는 파일 앱을 사용하여 백업 파일과 음악 폴더를 기기 간에 수동으로 이동할 수 있습니다.
{{% /details %}}

{{% details title="클라우드 서비스 연결이 백업과 함께 전송되나요?" closed="true" %}}
백업에는 데이터베이스, 재생 목록, 앨범 커버 및 설정이 포함됩니다. 보안상의 이유로 클라우드 서비스 로그인 자격 증명은 포함되지 않습니다. 복원 후 새 기기에서 클라우드 계정을 다시 연결해야 합니다.
{{% /details %}}

{{% details title="두 번째 기기의 기존 라이브러리는 어떻게 되나요?" closed="true" %}}
백업을 복원하면 두 번째 기기의 기존 음악 라이브러리 데이터, 재생 목록, 설정 및 앨범 아트워크가 모두 대체됩니다. 데이터를 보존하려면 먼저 두 번째 기기의 별도 백업을 만드세요.
{{% /details %}}

{{% details title="이 과정이 iPhone과 Mac 간에도 작동하나요?" closed="true" %}}
네. Evermusic은 iPhone, iPad 및 Mac의 모든 조합 간에 Wi-Fi Drive 전송을 지원합니다. 두 기기가 동일한 Wi-Fi 네트워크에 있기만 하면 됩니다.
{{% /details %}}

{{% details title="전송에 얼마나 걸리나요?" closed="true" %}}
전송 시간은 음악 라이브러리의 크기와 Wi-Fi 속도에 따라 달라집니다. 일반적인 몇 기가바이트의 라이브러리는 표준 가정용 네트워크에서 5~15분 내에 전송됩니다.
{{% /details %}}
