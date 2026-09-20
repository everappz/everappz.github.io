---
title: "iPhone과 iPad에서 파일 접근 및 공유용 WebDAV 서버 설정하는 법"
description: "Everdisk로 iPhone이나 iPad를 WebDAV 서버로 바꿔 Wi-Fi로 Mac Finder, Windows 파일 탐색기, Linux, Android 또는 다른 iPhone에서 네트워크 드라이브로 마운트하세요. 전체 설정, WebDAV 주소와 포트, 그리고 모든 기기의 단계별 연결 방법을 안내합니다."
date: 2026-09-19
tags: ["everdisk", "webdav", "네트워크 드라이브", "파일 공유", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["iPhone WebDAV 서버", "iPad WebDAV 서버", "iPhone에서 WebDAV 설정하는 법", "iPhone을 네트워크 드라이브로 마운트", "iPhone WebDAV Mac Finder 연결", "WebDAV Windows 파일 탐색기 iPhone", "iphone 네트워크 드라이브 Windows", "WebDAV Linux iPhone", "컴퓨터에서 iPhone 파일 접근", "iphone에서 iphone으로 webdav", "iPhone WebDAV 파일 공유", "iphone 네트워크 드라이브 매핑", "iphone webdav 파일 전송", "iphone webdav 주소 포트"]
readingTime: 9
---

{{< author-byline >}}

WebDAV는 폴더를 컴퓨터가 일반 파일 관리자에서 열 수 있는 네트워크 드라이브로 바꿔 줍니다. 브라우저가 쓰는 것과 같은 웹 프로토콜로 실행되며, 그래서 특별한 드라이버 없이 Mac, Windows, Linux를 잘 넘나듭니다. [Everdisk](/products/everdisk)로 iPhone이나 iPad에서 WebDAV 서버를 실행하면, 휴대폰이 거의 모든 컴퓨터에서 둘러보고, 복사해 오고, 복사해 넣을 수 있는 드라이브로 나타납니다.

WebDAV는 Windows가 관련될 때 가장 좋은 선택입니다. Windows 파일 탐색기가 깔끔하게 연결되기 때문입니다. 이 가이드는 설정 방법과 Mac, Windows, Linux, Android, 그리고 두 번째 iPhone에서 연결하는 방법을 다룹니다.

## 필요한 것

- [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8)가 설치된 iPhone이나 iPad.
- **같은 Wi-Fi 네트워크**에 있는 컴퓨터나 다른 기기.
- 공유하려는 파일이 Everdisk 문서 폴더나 추가한 폴더에 있어야 합니다.

## Everdisk에서 WebDAV 서버 설정하기

### 1단계: 공유할 항목 고르고 접근 설정하기

Everdisk를 열고 **공유** 탭으로 가서 **공유할 항목**을 탭하세요. 문서 폴더는 기본으로 공유됩니다. **폴더 추가**와 **파일 추가**로 더 추가하세요.

**설정**으로 가서 **공유**, 그다음 **접근 권한**으로 이동하세요. 연결된 컴퓨터가 휴대폰에 파일을 복사하고 이름을 바꾸거나 삭제하게 하려면 **파일 편집**을 켜고, 읽기 전용 드라이브로 두려면 끄세요. 로그인을 원하면 여기서 **로그인**과 **비밀번호**를 설정하고, 게스트 접근을 위해서는 비워 두세요.

### 2단계: WebDAV 서버 켜기

**설정**으로 가서 **공유**, 그다음 **연결**로 이동해 **컴퓨터**를 켜세요. 그것이 WebDAV 서버입니다(WebDAV 태그가 붙습니다).

### 3단계: 공유 시작하고 주소 확인하기

**공유** 탭으로 돌아가 **시작**을 탭하세요. **연결 방법** 섹션에 WebDAV 주소가 표시됩니다. 다음과 같이 생겼습니다.

```
http://192.168.1.20:8080
```

콜론 뒤의 숫자는 **포트**로, 기본은 **8080**입니다. 앞부분은 Wi-Fi에서 iPhone의 주소이므로 여러분의 것은 다릅니다. 기기가 연결되어 있는 동안에는 Everdisk를 화면에 열어 두세요.

## Mac에서 연결하기

1. **Finder**를 열고 **이동**을 선택한 뒤 **서버에 연결**(또는 **Command와 K**를 누르세요)을 선택하세요.
2. Everdisk에 표시된 WebDAV 주소를 입력하세요. 예: `http://192.168.1.20:8080`.
3. **연결**을 클릭한 뒤 **게스트**를 고르거나 **로그인**과 **비밀번호**를 입력하세요.

iPhone이 Finder 창에 열리며 일반 폴더처럼 동작합니다. 파일 편집이 켜져 있으면 양방향으로 파일을 복사하세요.

## Windows에서 연결하기

Windows에는 WebDAV 클라이언트가 내장되어 있어 파일 탐색기에서 됩니다.

1. **파일 탐색기**를 열고 사이드바에서 **내 PC**를 마우스 오른쪽 버튼으로 클릭한 뒤 **네트워크 위치 추가**를 선택하세요(**네트워크 드라이브 연결**을 사용해도 됩니다).
2. 주소를 물으면 Everdisk의 같은 WebDAV 주소를 입력하세요. 예: `http://192.168.1.20:8080`. 그다음 **다음**을 클릭하세요.
3. 설정했다면 **로그인**과 **비밀번호**를 입력하세요.

그러면 기기가 내 PC 아래에 열어서 파일을 복사할 수 있는 네트워크 위치로 나타납니다. Windows가 처음에 연결을 거부하면 **WebClient** 서비스가 실행 중인지 확인하세요(시작 메뉴에서 서비스를 검색하고 WebClient를 찾아 시작으로 설정). 그다음 다시 시도하세요.

## Linux에서 연결하기

1. 파일 관리자를 열고 **Connect to Server** 또는 **Other Locations**를 선택하세요.
2. WebDAV 접두어를 붙여 주소를 입력하세요. 예: `dav://192.168.1.20:8080`(TLS를 설정한 경우에만 `davs://`를 사용하세요).
3. 게스트로 연결하거나 로그인을 입력하세요.

## Android에서 연결하기

Android에는 시스템 WebDAV 브라우저가 없으므로 이를 지원하는 파일 관리자를 사용하세요.

1. **Solid Explorer**나 **CX File Explorer** 같은 앱을 설치하세요.
2. 새 **WebDAV** 연결을 추가하세요.
3. 호스트와 **포트 8080**을 입력하고 `http` 방식을 고른 뒤, 설정했다면 로그인을 추가하세요.

## 다른 iPhone이나 iPad에서 연결하기

iOS 파일 앱에는 WebDAV 클라이언트가 없으므로 다음 중 하나를 사용하세요.

- **Everdisk 자체의 기기 탭.** 두 번째 기기에서 Everdisk를 열고 **기기**로 가서 **새 연결**을 탭하고 **WebDAV**를 고른 뒤 주소를 입력하세요. 예: `http://192.168.1.20:8080`. 가장 간단한 방법이며 추가로 필요한 것이 없습니다.
- **WebDAV 앱**(예: Documents by Readdle). 같은 주소와 로그인으로 WebDAV 연결을 추가할 수 있습니다.

## 드라이브 대신 빠른 링크를 원하시나요?

파일 하나만 빠르게 가져오면 되고 드라이브를 마운트하고 싶지 않다면, 설정, 공유, 연결에서 **브라우저** 연결을 켜세요. 그러면 Everdisk가 어떤 기기의 어떤 브라우저에서든 열어 파일을 둘러보고 내려받을 수 있는 웹 주소를 줍니다. Windows PC, Chromebook, 친구의 휴대폰에 파일을 건네는 가장 빠른 방법입니다.

## 읽기 전용 또는 읽기 및 쓰기

설정, 공유, 접근 권한의 **파일 편집** 스위치가 이를 결정합니다. 켜면 연결된 컴퓨터가 업로드하고, 이름을 바꾸고, 삭제할 수 있습니다. 끄면 드라이브가 읽기 전용이 되어 다른 사람이 파일을 보고 복사할 수는 있어도 바꿀 수는 없습니다.

## 사람들이 실제로 쓰는 방법

- **Windows PC에서 iPhone으로 파일 복사하기.** 네트워크 위치로 매핑한 뒤 끌어다 놓으세요.
- **사진과 문서를 노트북으로 옮기기.** 이미 익숙한 파일 관리자로, 케이블도 iTunes도 없이 됩니다.
- **문서를 제자리에서 편집하기.** Mac에서 휴대폰의 문서를 바로 열어 다시 저장하세요.
- **iPhone과 iPad 사이에서 폴더 옮기기.** 받는 기기에서 Everdisk의 기기 탭을 사용하세요.

## 몇 가지 팁

- 기기가 연결되어 있는 동안 Everdisk를 열어 두세요. 휴대폰을 오래 잠가 두면 앱이 일시정지될 수 있습니다.
- Windows에서 연결이 실패하면 WebClient 서비스를 시작하고 주소를 다시 시도하세요.
- WebDAV와 SMB는 둘 다 네트워크 드라이브로 마운트됩니다. Windows가 관련되면 WebDAV를, Finder 속도와 암호화를 원하면 [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)를 사용하세요.
- 가장 빠른 전송을 위해 설정에서 사진과 동영상 품질을 원본으로 유지하세요.

## 자주 묻는 질문

{{% details title="내 iPhone의 WebDAV 주소와 포트는 무엇인가요?" closed="true" %}}
공유를 시작하면 Everdisk가 공유 화면에 주소를 표시합니다. http://192.168.1.20:8080처럼 생겼습니다. 8080은 Everdisk가 WebDAV에 사용하는 포트이고, 앞부분은 Wi-Fi에서 iPhone의 주소이므로 여러분의 것은 다릅니다.
{{% /details %}}

{{% details title="Windows에서 내 iPhone WebDAV에 어떻게 연결하나요?" closed="true" %}}
파일 탐색기를 열고 내 PC를 마우스 오른쪽 버튼으로 클릭한 뒤 네트워크 위치 추가나 네트워크 드라이브 연결을 선택하세요. Everdisk의 WebDAV 주소를 입력하고(예: http://192.168.1.20:8080), 설정했다면 로그인을 입력하세요. Windows가 연결하지 못하면 WebClient 서비스가 실행 중인지 확인한 뒤(서비스를 검색해 WebClient를 찾아 시작) 다시 시도하세요.
{{% /details %}}

{{% details title="두 iPhone 사이에서 WebDAV를 쓸 수 있나요?" closed="true" %}}
네, 하지만 iOS 파일 앱에는 WebDAV 클라이언트가 없으므로 두 번째 기기에서 Everdisk를 사용하세요. 기기 탭을 열고 새 연결을 탭한 뒤 WebDAV를 고르고 첫 번째 휴대폰에 표시된 주소를 입력하세요. Documents by Readdle 같은 WebDAV 앱도 됩니다.
{{% /details %}}

{{% details title="WebDAV에 비밀번호가 필요한가요?" closed="true" %}}
아니요, 로그인은 선택 사항입니다. 게스트 접근을 위해 설정, 공유, 접근 권한에서 로그인과 비밀번호를 비워 두거나, 연결 시 로그인하게 하려면 설정하세요.
{{% /details %}}

{{% details title="다른 사람이 WebDAV로 내 파일을 바꿀 수 있나요?" closed="true" %}}
허용할 때만 그렇습니다. 설정, 공유, 접근 권한의 파일 편집 스위치가 이를 제어합니다. 켜면 연결된 기기가 업로드하고, 이름을 바꾸고, 삭제할 수 있습니다. 끄면 드라이브가 읽기 전용이 되어 다른 사람이 보고 복사할 수는 있어도 아무것도 바꿀 수 없습니다.
{{% /details %}}

{{% details title="WebDAV와 SMB, 차이가 무엇인가요?" closed="true" %}}
둘 다 iPhone을 네트워크 드라이브로 마운트합니다. WebDAV는 웹 프로토콜로 실행되어 Windows 파일 탐색기에서 깔끔하게 연결되는 것이 주된 강점입니다. SMB는 Mac, Linux, NAS 기기의 기본 파일 공유 방식이며, 보통 Mac에서 더 빠르고, 전송을 암호화할 수 있는 유일한 Everdisk 연결입니다. Everdisk는 둘을 동시에 실행할 수 있습니다.
{{% /details %}}

{{% details title="WebDAV 드라이브가 왜 연결이 끊기나요?" closed="true" %}}
iPhone이 서버이고, iOS는 백그라운드에 너무 오래 있는 앱을 일시정지합니다. 기기가 연결되어 있는 동안 Everdisk를 화면에 열어 두고, 긴 전송에는 전원에 연결하세요. 두 기기가 여전히 같은 Wi-Fi에 있는지도 확인하세요.
{{% /details %}}

{{% details title="Wi-Fi 없이 WebDAV로 연결할 수 있나요?" closed="true" %}}
네, iPhone을 케이블로 Mac에 연결하면 됩니다. 그러면 Everdisk가 연결된 Mac이 Finder에서 열 수 있는 추가 케이블 연결 주소를 표시하며, Wi-Fi가 전혀 없어도 됩니다. 케이블에서는 그 Mac만 기기에 닿을 수 있습니다.
{{% /details %}}

{{% details title="Everdisk는 무료인가요?" closed="true" %}}
네, Everdisk는 무료로 내려받을 수 있으며 WebDAV 서버가 포함되어 있습니다. 선택 사항인 일회성 Premium 구매는 사용자 지정 포트와 사진, 동영상 변환 같은 추가 기능을 더합니다. 결제 없이 WebDAV를 설정하고 파일을 공유할 수 있습니다.
{{% /details %}}

한번 써 보시겠어요? [App Store에서 Everdisk를 다운로드](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8)하고 몇 분 만에 iPhone을 드라이브로 마운트해 보세요. 궁금한 점이나 의견이 있으신가요? **support@everappz.com**으로 이메일을 보내 주세요.
