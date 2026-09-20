---
title: "iPhone과 iPad에서 파일 전송용 FTP 서버 설정하는 법"
description: "Everdisk로 iPhone이나 iPad를 FTP 서버로 바꿔 Wi-Fi로 Mac, Windows PC, Linux, Android, FileZilla 같은 FTP 앱 또는 다른 iPhone에서 파일을 전송하세요. 전체 설정, ftp 주소와 포트, 게스트 접근, 그리고 모든 기기의 단계별 연결 방법을 안내합니다."
date: 2026-09-19
tags: ["everdisk", "ftp", "파일 전송", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["iPhone FTP 서버", "iPad FTP 서버", "iPhone에서 FTP 설정하는 법", "iphone ftp 서버 앱", "FileZilla를 iPhone에 연결", "Cyberduck iPhone FTP", "iPhone FTP 파일 전송", "iphone에서 컴퓨터로 ftp", "iphone에서 iphone으로 ftp", "Windows에서 iPhone FTP 연결", "iphone ftp 주소 포트", "iphone 익명 ftp", "iphone ftp 파일 공유", "카메라 nas용 iphone ftp"]
readingTime: 9
---

{{< author-byline >}}

FTP는 파일 전송의 오래된 믿음직한 방법입니다. 수십 년 동안 존재해 왔고, 바로 그 점이 유용한 이유입니다. 서버와 대화할 수 있는 거의 모든 것이 FTP를 이해합니다. 카메라, 스마트 TV, 라우터, 네트워크 드라이브, 자동화 도구, 그리고 모든 데스크톱 FTP 앱이 FTP를 씁니다. [Everdisk](/products/everdisk)로 iPhone이나 iPad에서 FTP 서버를 실행하면, 휴대폰이 그런 기기와 앱이 연결해 파일을 옮길 수 있는 곳이 됩니다.

다른 선택지가 맞지 않을 때, 예를 들어 오래된 기기나 FTP로만 연결할 줄 아는 앱일 때 FTP를 선택하세요. 이 가이드는 설정 방법과 Mac, Windows, FTP 앱, Linux, Android, 그리고 두 번째 iPhone에서 연결하는 방법을 다룹니다.

## 필요한 것

- [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8)가 설치된 iPhone이나 iPad.
- **같은 Wi-Fi 네트워크**에 있는 컴퓨터, 앱 또는 기기.
- 공유하려는 파일이 Everdisk 문서 폴더나 추가한 폴더에 있어야 합니다.

## Everdisk에서 FTP 서버 설정하기

### 1단계: 공유할 항목 고르고 접근 설정하기

Everdisk를 열고 **공유** 탭으로 가서 **공유할 항목**을 탭하세요. 문서 폴더는 기본으로 공유됩니다. **폴더 추가**와 **파일 추가**로 더 추가하세요.

**설정**으로 가서 **공유**, 그다음 **접근 권한**으로 이동하세요. 사람들이 업로드하고, 이름을 바꾸고, 삭제하게 하려면 **파일 편집**을 켜고, 다운로드만 허용하려면 끄세요. 로그인을 원하면 **로그인**과 **비밀번호**를 설정하고, 누구나 게스트로 연결할 수 있게 하려면 비워 두세요.

### 2단계: FTP 서버 켜기

**설정**으로 가서 **공유**, 그다음 **연결**로 이동해 **다른 앱 및 기기**를 켜세요. 그것이 FTP 서버입니다(FTP 태그가 붙습니다).

### 3단계: 공유 시작하고 주소 확인하기

**공유** 탭으로 돌아가 **시작**을 탭하세요. **연결 방법** 섹션에 FTP 주소가 표시됩니다. 다음과 같이 생겼습니다.

```
ftp://192.168.1.20:2121
```

콜론 뒤의 숫자는 **포트**로, 기본은 **2121**입니다. 앞부분은 Wi-Fi에서 iPhone의 주소이므로 여러분의 것은 다릅니다. 기기가 연결되어 있는 동안에는 Everdisk를 화면에 열어 두세요.

## Mac에서 연결하기

1. **Finder**를 열고 **이동**을 선택한 뒤 **서버에 연결**(또는 **Command와 K**를 누르세요)을 선택하세요.
2. Everdisk에 표시된 FTP 주소를 입력하세요. 예: `ftp://192.168.1.20:2121`.
3. **연결**을 클릭한 뒤 **게스트**를 고르거나 **로그인**과 **비밀번호**를 입력하세요.

Finder가 FTP 공유를 마운트하므로 둘러보고 Mac으로 파일을 복사할 수 있습니다. Finder는 FTP를 읽기 전용으로 엽니다. Mac에서 업로드하려면 아래에 설명한 대로 FTP 앱을 사용하세요.

## Windows에서 연결하기

1. **파일 탐색기**를 열고 맨 위의 주소 표시줄을 클릭하세요.
2. Everdisk의 FTP 주소를 입력하고(예: `ftp://192.168.1.20:2121`) **Enter**를 누르세요.
3. 설정했다면 **로그인**과 **비밀번호**를 입력하거나, 게스트로 계속하세요.

공유된 파일이 창에 나타나며 PC로 복사할 수 있습니다.

## FTP 앱으로 연결하기(FileZilla, Cyberduck)

업로드와 완전한 제어에는 FTP 앱이 가장 좋은 도구입니다. **FileZilla**와 **Cyberduck**은 무료이고 Windows, Mac, Linux에서 실행됩니다.

1. 앱을 열고 새 연결을 만드세요.
2. **호스트(Host)**를 iPhone의 Wi-Fi 주소로, **포트(Port)**를 **2121**로 설정하세요.
3. 로그인에는 **로그인**과 **비밀번호**를 입력하거나, 설정하지 않았다면 **Anonymous**를 고르세요.
4. 연결한 뒤 양방향으로 파일을 끌어다 놓으세요(업로드에는 파일 편집이 켜져 있어야 합니다).

## Linux에서 연결하기

1. 파일 관리자를 열고 **Connect to Server** 또는 **Other Locations**를 선택하세요.
2. 주소를 입력하세요. 예: `ftp://192.168.1.20:2121`.
3. 게스트나 로그인으로 연결하세요.

터미널에서 어떤 Linux FTP 클라이언트든 사용해 같은 호스트와 포트 2121을 지정할 수도 있습니다.

## Android에서 연결하기

Android에는 시스템 FTP 브라우저가 없으므로 앱을 사용하세요.

1. **AndFTP**, **FTPCafe** 같은 FTP 클라이언트나 **Solid Explorer**처럼 FTP를 지원하는 파일 관리자를 설치하세요.
2. 호스트, **포트 2121**, 그리고 로그인이나 Anonymous로 연결을 추가하세요.
3. 둘러보고 전송하세요.

## 다른 iPhone이나 iPad에서 연결하기

iOS 파일 앱에는 FTP 클라이언트가 없으므로 두 번째 기기에서 다음 중 하나를 사용하세요.

- **Everdisk 자체의 기기 탭.** Everdisk를 열고 **기기**로 가서 **새 연결**을 탭하고 **FTP**를 고른 뒤 주소를 입력하세요. 예: `ftp://192.168.1.20:2121`. 가장 간단한 방법입니다.
- **iOS용 전용 FTP 앱.** 같은 호스트, 포트 2121, 로그인을 사용합니다.

## 다른 장비 연결하기: 카메라, TV, 라우터, NAS

FTP가 빛을 발하는 지점입니다. 많은 기기에는 파일을 보내거나 가져올 수 있는 FTP 클라이언트가 내장되어 있습니다.

- FTP로 사진을 업로드하는 **카메라**는 사진을 iPhone으로 바로 보낼 수 있습니다.
- FTP를 지원하는 **스마트 TV, 라우터, NAS 박스, 자동화 도구**도 같은 방식으로 연결할 수 있습니다.

Everdisk에 표시된 주소를 사용해 iPhone의 Wi-Fi 주소, 포트 **2121**, 그리고 로그인(또는 Anonymous)을 지정하세요.

## 읽기 전용 또는 읽기 및 쓰기

설정, 공유, 접근 권한의 **파일 편집** 스위치가 이를 제어합니다. 켜면 사람들이 업로드하고, 이름을 바꾸고, 삭제할 수 있습니다. 끄면 다운로드만 할 수 있습니다. 파일을 나눠 주면서 휴대폰의 것을 바꾸지 않기를 바랄 때는 읽기 전용을 고르세요.

## 사람들이 실제로 쓰는 방법

- **FileZilla를 iPhone에 연결하기.** 한 번에 여러 파일을 휴대폰에 밀어 넣으세요.
- **FTP로만 연결할 줄 아는 오래된 앱이나 기기가** 다른 방법으로는 연결되지 않을 때 파일에 닿게 하세요.
- **FTP로 업로드하는 카메라에서 사진 받기.**
- **iPhone과 iPad 사이에서 파일 옮기기.** 받는 기기에서 Everdisk의 기기 탭을 사용하세요.

## 몇 가지 팁

- 기기가 연결되어 있는 동안 Everdisk를 열어 두세요. iOS는 잠시 뒤 백그라운드 앱을 일시정지하기 때문입니다.
- Mac에서 업로드하려면 Finder 대신 FileZilla나 Cyberduck을 사용하세요. Finder는 FTP를 읽기 전용으로 엽니다.
- 가장 넓은 호환성을 위해 로그인을 비워 두고 Anonymous로 연결하세요. 대부분의 FTP 클라이언트가 이를 제공합니다.
- FTP는 트래픽을 암호화하지 않습니다. 신뢰하지 않는 네트워크에서는 [암호화된 SMB 서버](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)를 대신 사용하세요.

## 자주 묻는 질문

{{% details title="내 iPhone의 FTP 주소와 포트는 무엇인가요?" closed="true" %}}
공유를 시작하면 Everdisk가 공유 화면에 주소를 표시합니다. ftp://192.168.1.20:2121처럼 생겼습니다. 2121은 Everdisk가 FTP에 사용하는 포트이고, 앞부분은 Wi-Fi에서 iPhone의 주소이므로 여러분의 것은 다릅니다.
{{% /details %}}

{{% details title="FileZilla나 Cyberduck을 내 iPhone에 어떻게 연결하나요?" closed="true" %}}
앱을 열고 새 연결을 만드세요. 호스트를 iPhone의 Wi-Fi 주소로, 포트를 2121로 설정하세요. 로그인과 비밀번호를 입력하거나, Everdisk에서 설정하지 않았다면 Anonymous를 고르세요. 연결하면 파일 편집이 켜져 있을 때 양방향으로 파일을 끌어다 놓을 수 있습니다.
{{% /details %}}

{{% details title="Windows에서 내 iPhone FTP에 연결할 수 있나요?" closed="true" %}}
네. 파일 탐색기를 열고 주소 표시줄을 클릭한 뒤 Everdisk의 FTP 주소를 입력하고(예: ftp://192.168.1.20:2121) Enter를 누르세요. 설정했다면 로그인을 입력하거나 게스트로 계속하세요. 업로드와 더 많은 제어를 위해서는 FileZilla 같은 FTP 앱을 대신 사용하세요.
{{% /details %}}

{{% details title="FTP에 로그인이 필요한가요?" closed="true" %}}
아니요, 로그인은 선택 사항입니다. 설정, 공유, 접근 권한에서 로그인과 비밀번호를 비워 두고 Anonymous로 연결하세요. 대부분의 FTP 클라이언트가 이를 제공합니다. 연결 시 먼저 로그인하게 하려면 로그인을 설정하세요.
{{% /details %}}

{{% details title="FTP로 왜 다운로드만 되고 업로드는 안 되나요?" closed="true" %}}
흔한 이유가 두 가지입니다. 첫째, 업로드, 이름 바꾸기, 삭제를 허용하려면 설정, 공유, 접근 권한의 파일 편집 스위치가 켜져 있어야 합니다. 둘째, Mac Finder는 FTP를 읽기 전용으로 열므로, 업로드하려면 FileZilla나 Cyberduck 같은 FTP 앱을 사용하세요.
{{% /details %}}

{{% details title="두 iPhone 사이에서 FTP를 쓸 수 있나요?" closed="true" %}}
네. 첫 번째 iPhone에서 FTP 서버를 시작하세요. 두 번째에서 Everdisk를 열고 기기 탭으로 가서 새 연결을 탭하고 FTP를 고른 뒤 첫 번째 휴대폰에 표시된 주소를 입력하세요. iOS 파일 앱에는 FTP 클라이언트가 없으므로 iOS용 전용 FTP 앱도 됩니다.
{{% /details %}}

{{% details title="FTP는 안전한가요?" closed="true" %}}
일반 FTP는 트래픽을 암호화하지 않으므로 홈 Wi-Fi처럼 신뢰하는 네트워크를 위한 도구로 다루세요. 통제하지 못하는 네트워크에서는 SMB 암호화 요구를 켠 SMB 서버를 사용하세요. 모든 전송을 보호합니다.
{{% /details %}}

{{% details title="어떤 기기가 FTP로 연결할 수 있나요?" closed="true" %}}
FTP 클라이언트가 있는 거의 모든 것입니다. 여기에는 Mac, Windows, Linux 컴퓨터, FileZilla와 Cyberduck 같은 FTP 앱, Android 파일 관리자, 그리고 카메라, 스마트 TV, 라우터, NAS 박스, 자동화 도구 같은 하드웨어가 포함됩니다. 그 넓은 도달 범위가 FTP를 고르는 주된 이유입니다.
{{% /details %}}

{{% details title="FTP 연결이 왜 끊겼나요?" closed="true" %}}
iPhone이 서버이고, iOS는 백그라운드에 너무 오래 있는 앱을 일시정지합니다. 기기가 연결되어 있는 동안 Everdisk를 화면에 열어 두고, 긴 전송에는 전원에 연결하세요. 두 기기가 여전히 같은 Wi-Fi에 있는지도 확인하세요.
{{% /details %}}

{{% details title="Everdisk는 무료인가요?" closed="true" %}}
네, Everdisk는 무료로 내려받을 수 있으며 FTP 서버가 포함되어 있습니다. 선택 사항인 일회성 Premium 구매는 사용자 지정 포트와 사진, 동영상 변환 같은 추가 기능을 더합니다. 결제 없이 FTP를 설정하고 파일을 전송할 수 있습니다.
{{% /details %}}

한번 써 보시겠어요? [App Store에서 Everdisk를 다운로드](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8)하고 몇 분 만에 첫 FTP 클라이언트를 연결해 보세요. 궁금한 점이나 의견이 있으신가요? **support@everappz.com**으로 이메일을 보내 주세요.
