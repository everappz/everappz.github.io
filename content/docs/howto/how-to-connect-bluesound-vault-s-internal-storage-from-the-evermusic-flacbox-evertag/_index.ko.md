---
title: "Evermusic, Flacbox, Evertag에서 Bluesound VAULT의 내부 저장소를 연결하는 방법"
date: 2022-03-10
description: "SMB 프로토콜을 사용하여 Evermusic, Flacbox, Evertag에서 Bluesound VAULT의 내장 하드 드라이브에 접근하여 오디오 파일을 관리, 편집, 재생하는 방법을 알아보세요."
keywords: ["bluesound vault", "smb 저장소 연결", "evermusic smb", "flacbox vault", "evertag smb", "nas 저장소 음악", "vault 내장 드라이브"]
tags: ["evermusic", "연결", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**요약:** Evermusic, Flacbox 또는 Evertag를 사용하여 SMB를 통해 Bluesound VAULT의 내부 저장소에 연결하세요. BluOS 앱에서 VAULT의 IP 주소를 찾고, 게스트 접근으로 SMB 연결로 입력한 후 음악 파일을 재생하거나 관리하기 시작하세요.

Bluesound VAULT에는 내장 하드 드라이브가 있으며 네트워크 연결 저장소(NAS)로 작동합니다. VAULT의 내장 하드 드라이브에 접근하면 Evermusic, Flacbox, Evertag 앱에서 파일을 추가/삭제하고 메타데이터 태그를 편집할 수 있습니다.

**VAULT의 내장 하드 드라이브에 접근하는 단계는 다음과 같습니다:**

1. BluOS 앱에서 **도움말 > 진단**을 선택합니다.

2. **진단** 페이지에서 VAULT의 **IP 주소**를 확인합니다. 이 **IP 주소**는 다음 단계에서 사용됩니다.

3. Evermusic, Flacbox 또는 Evertag를 엽니다.

   ![Everappz 애플리케이션](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. "연결하기" 화면을 열고 "클라우드 서비스 연결" 메뉴 항목을 선택합니다.

   ![Evermusic 연결하기 화면](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. "SMB" 클라우드 서비스를 선택합니다.

   ![Evermusic 클라우드 서비스 연결 화면](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. "SMB 구성 화면"에서 다음 형식으로 URL을 입력합니다:

   ```
   SMB://<<VAULT-IP>>
   ```

   `<<VAULT-IP>>`를 2단계에서 확인한 **IP 주소**로 바꿉니다.

   **참고:** VAULT 저장소가 게스트(GUEST) 모드를 지원하므로 로그인 및 비밀번호 필드를 비워두세요.

   ![Evermusic SMB 연결 화면](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. "로그인" 버튼을 탭하여 구성을 저장합니다.

8. 연결된 클라우드 저장소를 열고 오디오 파일이 있는 폴더로 이동하여 아무 파일이나 탭하여 오디오 플레이어를 시작합니다.

   ![Evermusic 열린 SMB 서버 화면](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. 내장 파일 관리자를 사용하여 파일을 편집할 수도 있습니다.

   ![Evermusic 파일 관리자 화면](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

이러한 간단한 단계를 통해 Bluesound VAULT의 내장 하드 드라이브에 쉽게 접근하고 Evermusic, Flacbox 또는 Evertag를 사용하여 음악 라이브러리를 관리할 수 있습니다.

## FAQ

{{% details title="Bluesound VAULT에 연결하려면 사용자 이름과 비밀번호가 필요합니까?" closed="true" %}}
아니요. Bluesound VAULT는 SMB를 통한 게스트(익명) 접근을 지원합니다. 연결을 구성할 때 로그인 및 비밀번호 필드를 비워두세요.
{{% /details %}}

{{% details title="Bluesound VAULT에서 음악 태그를 편집할 수 있습니까?" closed="true" %}}
예. Evertag를 사용하면 VAULT의 내장 하드 드라이브에 직접 저장된 오디오 파일의 메타데이터 태그(제목, 아티스트, 앨범 등)를 편집할 수 있습니다.
{{% /details %}}

{{% details title="Bluesound VAULT는 어떤 프로토콜을 지원합니까?" closed="true" %}}
Bluesound VAULT는 SMB(Server Message Block)를 통해 내부 저장소를 공개합니다. Evermusic, Flacbox, Evertag 모두 SMB 연결을 지원하므로 쉽게 연결할 수 있습니다.
{{% /details %}}

{{% details title="iPhone에 파일을 복사하지 않고 VAULT에서 음악을 스트리밍할 수 있습니까?" closed="true" %}}
예. SMB를 통해 연결하면 VAULT의 내장 드라이브에서 장치로 복사하지 않고 직접 오디오 파일을 스트리밍할 수 있습니다.
{{% /details %}}
