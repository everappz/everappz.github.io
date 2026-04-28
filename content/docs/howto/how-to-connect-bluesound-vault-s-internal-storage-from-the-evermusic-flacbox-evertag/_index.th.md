---
title: "วิธีเชื่อมต่อที่เก็บข้อมูลภายในของ Bluesound VAULT จาก Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "เรียนรู้วิธีเข้าถึงฮาร์ดไดรฟ์ภายในของ Bluesound VAULT จาก Evermusic, Flacbox และ Evertag โดยใช้โปรโตคอล SMB เพื่อจัดการ แก้ไข และเล่นไฟล์เสียง"
keywords: ["bluesound vault", "เชื่อมต่อที่เก็บข้อมูล smb", "evermusic smb", "flacbox vault", "evertag smb", "ที่เก็บข้อมูล nas เพลง", "ไดรฟ์ภายใน vault"]
tags: ["evermusic", "เชื่อมต่อ", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**สรุป:** เชื่อมต่อกับที่เก็บข้อมูลภายในของ Bluesound VAULT ผ่าน SMB โดยใช้ Evermusic, Flacbox หรือ Evertag ค้นหาที่อยู่ IP ของ VAULT ในแอป BluOS ป้อนเป็นการเชื่อมต่อ SMB ด้วยการเข้าถึงแบบผู้เยี่ยมชม และเริ่มเล่นหรือจัดการไฟล์เพลงของคุณ

Bluesound VAULT มีฮาร์ดไดรฟ์ภายในและทำหน้าที่เป็นที่เก็บข้อมูลที่เชื่อมต่อกับเครือข่าย (NAS) การเข้าถึงฮาร์ดไดรฟ์ภายในของ VAULT ช่วยให้คุณสามารถเพิ่ม/ลบไฟล์ แก้ไขแท็กข้อมูลเมตาจากแอปของเรา Evermusic, Flacbox, Evertag

**ขั้นตอนในการเข้าถึงฮาร์ดไดรฟ์ภายในของ VAULT มีดังนี้:**

1. ในแอป BluOS เลือก **ช่วยเหลือ > การวินิจฉัย**

2. จากหน้า **การวินิจฉัย** รับ **ที่อยู่ IP** ของ VAULT **ที่อยู่ IP** นี้จะถูกใช้ในขั้นตอนถัดไป

3. เปิด Evermusic, Flacbox หรือ Evertag

   ![แอปพลิเคชัน Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. เปิดหน้าจอ "การเชื่อมต่อ" และเลือกรายการเมนู "เชื่อมต่อบริการคลาวด์"

   ![หน้าจอการเชื่อมต่อ Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. เลือกบริการคลาวด์ "SMB"

   ![หน้าจอเชื่อมต่อบริการคลาวด์ Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. บน "หน้าจอการกำหนดค่า SMB" ป้อน URL ในรูปแบบต่อไปนี้:

   ```
   SMB://<<VAULT-IP>>
   ```

   แทนที่ `<<VAULT-IP>>` ด้วย **ที่อยู่ IP** ที่ได้รับในขั้นตอนที่ 2

   **หมายเหตุ:** เว้นช่องเข้าสู่ระบบและรหัสผ่านว่างไว้เนื่องจากที่เก็บข้อมูล VAULT รองรับโหมดผู้เยี่ยมชม (GUEST)

   ![หน้าจอการเชื่อมต่อ SMB ของ Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. แตะปุ่ม "เข้าสู่ระบบ" เพื่อบันทึกการกำหนดค่า

8. เปิดที่เก็บข้อมูลคลาวด์ที่เชื่อมต่อ นำทางไปยังโฟลเดอร์ที่มีไฟล์เสียงและแตะไฟล์ใดก็ได้เพื่อเริ่มเครื่องเล่นเสียง

   ![หน้าจอเซิร์ฟเวอร์ SMB ที่เปิดของ Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. คุณยังสามารถแก้ไขไฟล์โดยใช้ตัวจัดการไฟล์ในตัว

   ![หน้าจอตัวจัดการไฟล์ Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

ด้วยขั้นตอนง่ายๆ เหล่านี้ คุณสามารถเข้าถึงฮาร์ดไดรฟ์ภายในของ Bluesound VAULT และควบคุมคลังเพลงของคุณโดยใช้ Evermusic, Flacbox หรือ Evertag ได้อย่างง่ายดาย

## คำถามที่พบบ่อย

{{% details title="ฉันต้องใช้ชื่อผู้ใช้และรหัสผ่านเพื่อเชื่อมต่อกับ Bluesound VAULT หรือไม่?" closed="true" %}}
ไม่ Bluesound VAULT รองรับการเข้าถึงแบบผู้เยี่ยมชม (ไม่ระบุตัวตน) ผ่าน SMB เว้นช่องเข้าสู่ระบบและรหัสผ่านว่างไว้เมื่อกำหนดค่าการเชื่อมต่อ
{{% /details %}}

{{% details title="ฉันสามารถแก้ไขแท็กเพลงบน Bluesound VAULT ได้หรือไม่?" closed="true" %}}
ได้ การใช้ Evertag ช่วยให้คุณสามารถแก้ไขแท็กข้อมูลเมตา (ชื่อเรื่อง ศิลปิน อัลบั้ม ฯลฯ) สำหรับไฟล์เสียงที่เก็บไว้โดยตรงบนฮาร์ดไดรฟ์ภายในของ VAULT
{{% /details %}}

{{% details title="Bluesound VAULT รองรับโปรโตคอลใดบ้าง?" closed="true" %}}
Bluesound VAULT เปิดเผยที่เก็บข้อมูลภายในผ่าน SMB (Server Message Block) Evermusic, Flacbox และ Evertag ทั้งหมดรองรับการเชื่อมต่อ SMB ทำให้การเชื่อมต่อเป็นเรื่องง่าย
{{% /details %}}

{{% details title="ฉันสามารถสตรีมเพลงจาก VAULT โดยไม่ต้องคัดลอกไฟล์ไปยัง iPhone ของฉันได้หรือไม่?" closed="true" %}}
ได้ เมื่อเชื่อมต่อผ่าน SMB แล้ว คุณสามารถสตรีมไฟล์เสียงโดยตรงจากไดรฟ์ภายในของ VAULT โดยไม่ต้องคัดลอกไปยังอุปกรณ์ของคุณ
{{% /details %}}
