---
title: "การตั้งค่า"
date: 2026-08-20
description: "ทัวร์การตั้งค่า Everdisk แบบครบถ้วน ตั้งแต่โปรไฟล์อุปกรณ์ (ชื่อและรูปประจำตัว) เซิร์ฟเวอร์การเชื่อมต่อทั้งสี่ตัว การควบคุมการเข้าถึง คุณภาพรูปภาพและวิดีโอ พอร์ตแบบกำหนดเอง ภาพตัวอย่างขนาดย่อ DLNA ตัวเลือกเครือข่ายและการถ่ายโอน ตัวเลือกตัวจัดการไฟล์ และ Premium"
keywords: ["การตั้งค่า Everdisk", "ชื่อและรูปประจำตัวอุปกรณ์", "เซิร์ฟเวอร์การเชื่อมต่อ", "คุณภาพรูปภาพวิดีโอ", "พอร์ตกำหนดเอง HTTP WebDAV FTP", "ภาพตัวอย่างขนาดย่อ DLNA", "การถ่ายโอนพร้อมกัน", "ลบไฟล์ถาวร", "แคชภาพตัวอย่างขนาดย่อ", "Everdisk Premium"]
tags: ["everdisk", "guide", "settings"]
readingTime: 12
---


แท็บ **การตั้งค่า** จัดกลุ่มทุกอย่างออกเป็นสามส่วนหลัก ได้แก่ **Sharing**, **Network** และ **File Manager** พร้อมกับ Premium ข้อเสนอแนะ และลิงก์ทางกฎหมาย หน้านี้อธิบายทุกการตั้งค่าและค่าเริ่มต้นของมัน

## Premium

ด้านบนของการตั้งค่า คุณจะเห็นสถานะ Premium ของคุณ หรือปุ่ม **Unlock all features** Everdisk ใช้งานได้ฟรีโดยมีข้อจำกัดเล็กน้อย การซื้อ **Premium Lifetime** แบบครั้งเดียวจะยกเลิกข้อจำกัดเหล่านั้น ดู [Premium](#premium-lifetime) ที่ท้ายหน้านี้

## การตั้งค่าการแชร์

### General

- **Start device sharing automatically** - เริ่มการแชร์ทันทีที่คุณเปิดแอป *(Premium)*
- **Share Documents Folder** - แชร์โฟลเดอร์ Documents ของแอป เปิดโดยค่าเริ่มต้น
- **Notify before disconnecting** - เตือนให้คุณเปิดแอปอีกครั้งก่อนที่ระบบจะหยุดแอปชั่วคราวในเบื้องหลัง ปิดโดยค่าเริ่มต้น จะขอสิทธิ์การแจ้งเตือนในครั้งแรก

### Device Profile

- **Device Name** - ชื่อที่อุปกรณ์อื่นเห็นสำหรับคุณบนเครือข่าย แตะเพื่อแก้ไข *(Premium)*
- **Device Avatar** - ไอคอนและสีพื้นหลังสำหรับอุปกรณ์ของคุณ คุณเลือกไอคอน ไล่เฉดสีพื้นหลัง หรือ **เลือกรูปประจำตัวจาก Photos** ได้ *(Premium)*
- **Regenerate Name & Avatar** และ **Regenerate Avatar** - สุ่มชื่อและ/หรือรูปประจำตัวใหม่ *(ฟรี)*

### Access

- **Login** และ **Password** - บังคับให้ลงชื่อเข้าใช้สำหรับการเชื่อมต่อ Browser, Computer และ Other Apps
- **Files Editing** - อนุญาตให้อุปกรณ์ที่เชื่อมต่ออยู่อัปโหลด เปลี่ยนชื่อ และลบได้ เปิดโดยค่าเริ่มต้น
- **Blocked Devices** - จัดการอุปกรณ์ที่คุณบล็อกไว้

ดูรายละเอียดได้ที่ [การเข้าถึงและความเป็นส่วนตัว](/docs/guide/everdisk/everdisk-guide-access)

### Connections

เปิดหรือปิดเซิร์ฟเวอร์แต่ละตัว ทั้งสี่ตัวเปิดโดยค่าเริ่มต้น และแต่ละตัวมีปุ่ม info (ⓘ) พร้อมคำแนะนำการเชื่อมต่อ

- **TV & Media Center** (DLNA)
- **Browser** (HTTP)
- **Computer** (WebDAV)
- **Other Apps & Devices** (FTP)

### Photos

- **Format** - Original หรือ Most Compatible (JPEG)
- **Quality** - Original, High, Medium หรือ Low

การตั้งค่าอื่นใดนอกจาก Original จะแปลงรูปภาพขณะที่แชร์ ซึ่งช้ากว่า การแปลงเป็นฟีเจอร์ Premium

### Videos

- **Format** - Original หรือ Most Compatible (H.264 MP4)
- **Quality** - Original, High, Medium หรือ Low

แนวคิดเดียวกับ Photos: Original เร็วที่สุด และการแปลงเป็น Premium ลดคุณภาพลงหากทีวีรุ่นเก่าเล่นวิดีโอไม่ได้

### Advanced

- **HTTP Port** (ค่าเริ่มต้น 80), **WebDAV Port** (ค่าเริ่มต้น 8080), **FTP Port** (ค่าเริ่มต้น 2121) DLNA เลือกพอร์ตของมันเองโดยอัตโนมัติ *(การเปลี่ยนพอร์ตเป็น Premium ผู้ใช้ฟรีดูค่าได้)*

### DLNA Thumbnails

- **Show Thumbnails** - เผยแพร่ภาพตัวอย่างสำหรับทีวี เปิดโดยค่าเริ่มต้น (ฟรี)
- เลือกขนาดที่จะเผยแพร่: **Small (160px)**, **Medium (640px)**, **Large (1024px)**, **Extra Large (4096px)**

## การตั้งค่าเครือข่าย

- **File Transfers** - ใช้ **Wi-Fi** อย่างเดียว หรือ **Wi-Fi & Cellular Data** สำหรับการดาวน์โหลดและอัปโหลด ค่าเริ่มต้นคือ Wi-Fi
- **Parallel Transfer Limit** - จำนวนการถ่ายโอนที่ทำงานพร้อมกัน ค่าเริ่มต้นคือ 5
- **Background Transfers** - ให้การถ่ายโอนทำงานต่อขณะที่คุณใช้หน้าจออื่น เปิดโดยค่าเริ่มต้น
- **Thumbnails for Files** - ว่าจะดึงภาพตัวอย่างขนาดย่อของไฟล์บนอุปกรณ์อื่นผ่าน Wi-Fi อย่างเดียว หรือเซลลูลาร์ด้วย ค่าเริ่มต้นคือ Wi-Fi

## การตั้งค่าตัวจัดการไฟล์

- **Permanently Delete Files** - ลบทันทีโดยไม่มีถังขยะ ปิดโดยค่าเริ่มต้น ดู [การเข้าถึงและความเป็นส่วนตัว](/docs/guide/everdisk/everdisk-guide-access)
- **Reset All Notice Messages** - นำแบนเนอร์เคล็ดลับที่คุณปิดไปกลับมา
- **Thumbnail Cache** - ดูว่าภาพตัวอย่างขนาดย่อที่แคชไว้ใช้พื้นที่เท่าไหร่ และ **Clear Thumbnail Cache**

## ข้อเสนอแนะและกฎหมาย

ด้านล่างสุด คุณ **Rate this App**, **Send Feedback**, **Get More Apps** และเปิด **Terms and Conditions** และ **Privacy Policy** ได้

## Premium Lifetime

Everdisk ใช้งานได้ฟรี การซื้อ **Premium Lifetime** เพียงครั้งเดียว เป็นการจ่ายครั้งเดียว ไม่ใช่การสมัครสมาชิก จะปลดล็อก

- **Unlimited Folders** - แชร์ได้มากกว่า 5 โฟลเดอร์
- **Unlimited Connections** - บันทึกเซิร์ฟเวอร์บนแท็บ Devices ได้มากกว่า 10 รายการ
- **Photo & Video Conversion** - แชร์ในคุณภาพใด ๆ ก็ได้นอกจาก Original
- **Custom Ports** - ตั้งพอร์ต HTTP, WebDAV และ FTP ของคุณเอง
- **Auto-Start Sharing** - เริ่มการแชร์โดยอัตโนมัติเมื่อคุณเปิดแอป
- **Device Customization** - ชื่ออุปกรณ์แบบกำหนดเอง ไอคอนรูปประจำตัว ไล่เฉดสีพื้นหลัง หรือรูปประจำตัวจากรูปถ่าย

Premium ผูกกับ Apple ID ของคุณ ใช้ **Restore Purchases** เพื่อปลดล็อกบนอุปกรณ์อื่นของคุณที่ลงชื่อเข้าใช้ด้วย Apple ID เดียวกัน

## ขั้นตอนต่อไป

- [การแชร์](/docs/guide/everdisk/everdisk-guide-sharing) - หน้าจอการแชร์โดยละเอียด
- [การเข้าถึงและความเป็นส่วนตัว](/docs/guide/everdisk/everdisk-guide-access) - รหัสผ่าน การแก้ไข และการบล็อก
- [คำถามที่พบบ่อย](/docs/faq/everdisk) - คำตอบด่วนสำหรับคำถามที่พบบ่อย
