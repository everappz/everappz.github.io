---
title: "วิธีเล่นเพลงจาก Mac / PC / Linux / NAS บน iPhone โดยใช้เซิร์ฟเวอร์ Kodi DLNA"
date: 2025-07-25
description: "สตรีมเพลงจากคอมพิวเตอร์หรือ NAS ไปยัง iPhone ผ่าน Wi-Fi โดยใช้ Kodi DLNA และแอป Evermusic"
keywords: ["เซิร์ฟเวอร์ kodi dlna", "สตรีมเพลงไปยัง iphone", "เล่นเพลงจาก nas", "evermusic dlna", "เพลงจาก mac ไปยัง iphone", "เพลงจาก windows ไปยัง iphone", "kodi dlna iphone", "สตรีมเสียง dlna"]
tags: ["dlna", "kodi", "evermusic", "iphone", "สตรีมเพลง", "mac", "nas", "linux", "เครือข่ายท้องถิ่น"]
readingTime: 5
---

{{< author-byline >}}

**TL;DR:** ติดตั้ง Kodi บน Mac, PC, Linux หรือ NAS เปิดใช้เซิร์ฟเวอร์ DLNA/UPnP และสตรีมคลังเพลงทั้งหมดไปยัง iPhone หรือ iPad โดยใช้แอปฟรี Evermusic หรือ Flacbox ผ่าน Wi-Fi ไม่ต้องสมัครสมาชิก

## บทนำ

หากคุณมี **Mac, Windows PC, เครื่อง Linux หรืออุปกรณ์ NAS** คุณสามารถเปลี่ยนมันเป็น **เซิร์ฟเวอร์เพลงส่วนตัว** ที่บ้านได้อย่างง่ายดายโดยใช้ [Kodi](https://kodi.tv/) แพลตฟอร์มมีเดียฟรีและโอเพ่นซอร์ส ด้วยเซิร์ฟเวอร์ **DLNA/UPnP** ในตัวของ Kodi คุณสามารถสตรีมคลังเพลงทั้งหมดไปยังไคลเอนต์ที่รองรับ DLNA — รวมถึง iPhone หรือ iPad ของคุณ

ในคู่มือนี้ เราจะแสดงให้คุณเห็นทีละขั้นตอนวิธี:

- ติดตั้ง Kodi บน Mac หรือ PC
- ตั้งค่าโฟลเดอร์เพลงสำหรับการแชร์
- เปิดใช้เซิร์ฟเวอร์เพลง DLNA
- เข้าถึงเพลงนั้นโดยใช้แอป **Evermusic** หรือ **Flacbox** สำหรับ iOS

การตั้งค่านี้ฟรี 100% — ไม่มีการสมัครสมาชิก แค่เพลงของคุณเองที่สตรีมผ่านเครือข่าย Wi-Fi

## ดาวน์โหลดและติดตั้ง Kodi บน Mac / PC / Linux / NAS

ก่อนอื่น เยี่ยมชมเว็บไซต์ทางการของ Kodi:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="หน้าหลัก Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

คลิก **ดาวน์โหลด** และเลื่อนเพื่อค้นหาเวอร์ชันสำหรับคอมพิวเตอร์ของคุณ
เลือกระบบปฏิบัติการของคุณ ในตัวอย่างนี้เราจะใช้ **macOS**

{{< cards cols="1">}}
{{< card subtitle="หน้าดาวน์โหลด Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

คลิก **Intel (x86/64)** หากคุณมี Intel Mac หรือ **Apple Silicon** สำหรับ M1, M2, M3 Mac เพื่อเริ่มดาวน์โหลด

{{< cards cols="1">}}
{{< card subtitle="เลือกตัวติดตั้ง macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

กรุณารอสักครู่ขณะตัวติดตั้งกำลังดาวน์โหลด

{{< cards cols="1">}}
{{< card subtitle="ดาวน์โหลด Kodi แล้ว" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

หลังจากดาวน์โหลด ค้นหาไฟล์ `.dmg` ในโฟลเดอร์ **ดาวน์โหลด**

{{< cards cols="1">}}
{{< card subtitle="ติดตั้ง Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

ดับเบิลคลิกไฟล์ที่ดาวน์โหลดเพื่อเรียกใช้ตัวติดตั้ง
ลาก Kodi ไปยังโฟลเดอร์ **แอปพลิเคชัน** เพื่อติดตั้ง

{{< cards cols="1">}}
{{< card title="" subtitle="ติดตั้ง Kodi โดยลากไปยังแอปพลิเคชัน" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

เปิด Kodi คุณอาจต้องอนุญาตใน **การตั้งค่าระบบ → ความปลอดภัยและความเป็นส่วนตัว → เปิดต่อไป**

{{< cards cols="1">}}
{{< card subtitle="หน้าจอหลัก Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## เพิ่มเพลงในคลัง Kodi

คลิก **ไอคอนเกียร์** (การตั้งค่า) จากหน้าจอหลัก

{{< cards cols="1">}}
{{< card subtitle="การตั้งค่า Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

ไปที่ **การตั้งค่ามีเดีย → คลัง** เปิดใช้ **อัปเดตคลังเมื่อเริ่มต้น** สำหรับคลังวิดีโอและเพลงสำหรับการสร้างดัชนีอัตโนมัติ

{{< cards cols="1">}}
{{< card subtitle="การตั้งค่าคลัง" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

จากนั้นไปที่ส่วน **เพลง** และคลิก **เพิ่มเพลง**

{{< cards cols="1">}}
{{< card subtitle="เพิ่มโฟลเดอร์เพลง" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

เรียกดูและเลือกโฟลเดอร์ที่เก็บเพลงของคุณ

{{< cards cols="1">}}
{{< card subtitle="เลือกแหล่งเพลง" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

เพิ่มแหล่งเพลงใน Kodi

{{< cards cols="1">}}
{{< card subtitle="เพิ่มแหล่งเพลง" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

ยืนยันและปล่อยให้ Kodi สแกนคลังเพลงของคุณ

{{< cards cols="1">}}
{{< card subtitle="ยืนยันแหล่งเพลง" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

รอสักครู่ขณะสแกนและสร้างคลังของคุณ

{{< cards cols="1">}}
{{< card subtitle="กำลังสแกนคลังเพลง" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## เปิดใช้เซิร์ฟเวอร์ DLNA ของ Kodi

ไปที่ **การตั้งค่า → บริการ → UPnP/DLNA**

เปิดใช้ตัวเลือก: **แชร์คลังของฉัน**

Kodi ตอนนี้ทำงานเป็นเซิร์ฟเวอร์ DLNA บนเครือข่าย Wi-Fi ท้องถิ่นของคุณ

{{< cards cols="1">}}
{{< card subtitle="เปิดใช้ DLNA ใน Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## เปิดคลัง Kodi

คลิกขวาเพื่อปิดหน้าต่างการตั้งค่าและเปิดคลังหลักของ Kodi

{{< cards cols="1">}}
{{< card title="" subtitle="คลิกขวาเพื่อเข้าถึงคลัง Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## ดาวน์โหลดแอปสตรีมเพลงสำหรับ iOS

รับแอปไคลเอนต์ DLNA ฟรีสำหรับ iOS ที่ให้คุณสตรีมเพลงจากบริการจัดเก็บข้อมูลบนคลาวด์และเซิร์ฟเวอร์ DLNA

- ใช้ **Evermusic** หากคอลเลกชันของคุณส่วนใหญ่เป็น MP3 และรูปแบบเสียงมาตรฐานอื่นๆ
- เลือก **Flacbox** หากคุณมีคลังเพลงคุณภาพสูงในรูปแบบเช่น FLAC, ALAC หรือ DSD

ทั้งสองแอปมีให้สำหรับ **iOS** และ **macOS** และใช้ได้ฟรี

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="ดาวน์โหลด Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="ดาวน์โหลด Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## เพิ่มแหล่ง DLNA

หลังจากดาวน์โหลดแอป iOS ให้เปิดส่วน **การเชื่อมต่อ ทั้งหมด**

{{< cards cols="1">}}
{{< card title="" subtitle="แถบด้านข้างหลักของแอป Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

เลื่อนลงและแตะ **เครือข่ายท้องถิ่น - อุปกรณ์ที่มีให้บริการ** เพื่อค้นหาเซิร์ฟเวอร์ DLNA
ในส่วนนี้ คุณจะเห็นอุปกรณ์ทั้งหมดที่มีในเครือข่ายท้องถิ่นของคุณ **เซิร์ฟเวอร์ Kodi DLNA** ของคุณควรปรากฏที่นี่ แตะเซิร์ฟเวอร์ Kodi เพื่อเชื่อมต่อ

{{< cards cols="1">}}
{{< card title="" subtitle="อุปกรณ์ DLNA ที่มีใน Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic จะแสดงโฟลเดอร์คลังที่แชร์ผ่าน Kodi

{{< cards cols="1">}}
{{< card title="" subtitle="คลังเพลง Kodi ใน Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

ไปที่โฟลเดอร์ **เพลง** เพื่อดูไฟล์เสียงทั้งหมดที่มีบนเซิร์ฟเวอร์ DLNA

{{< cards cols="1">}}
{{< card title="" subtitle="เพลงจากโฟลเดอร์ระยะไกล" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

แตะไฟล์เสียงใดๆ เพื่อเริ่มสตรีมทันที

{{< cards cols="1">}}
{{< card title="" subtitle="ไฟล์ MP3 กำลังเล่นใน Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

กลับไปที่ส่วน **การเชื่อมต่อ** เซิร์ฟเวอร์ DLNA ที่เพิ่มจะปรากฏที่นี่ แตะไอคอนเพื่อเชื่อมต่อใหม่ได้ทุกเมื่อ

คุณยังสามารถเปิดใช้ **การติดตาม Last.fm** ที่นี่ สถิติการเล่นจะถูกบันทึกในบัญชี Last.fm ของคุณ

{{< cards cols="1">}}
{{< card title="" subtitle="การเชื่อมต่อใน Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## สร้างคลังเพลง

ทั้ง **Evermusic** และ **Flacbox** ให้คุณเพิ่มเพลงในคลังและจัดระเบียบตาม **แท็กข้อมูลเมตา** เช่น ศิลปิน อัลบั้ม แนวเพลง และนักแต่งเพลง

เริ่มต้นโดยเปิดส่วน **คลังเพลง** เลื่อนลงไปที่ **เครื่องมือและการตั้งค่า** และแตะ **เพิ่มเพลง**

{{< cards cols="1">}}
{{< card title="" subtitle="คลังเพลง Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

เลือกแหล่งเพลง — ในกรณีนี้ เลือก **การเชื่อมต่อ**

{{< cards cols="1">}}
{{< card title="" subtitle="เพิ่มเพลงใหม่ใน Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

ค้นหา **เซิร์ฟเวอร์ Kodi DLNA** ในการเชื่อมต่อและแตะเพื่อดูโฟลเดอร์และไฟล์

{{< cards cols="1">}}
{{< card title="" subtitle="เลือกเซิร์ฟเวอร์ DLNA สำหรับนำเข้าเพลง" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

เลือกโฟลเดอร์หรือไฟล์ที่ต้องการเพิ่มและแตะ **เสร็จสิ้น**

{{< cards cols="1">}}
{{< card title="" subtitle="เลือกโฟลเดอร์เพลงที่จะเพิ่ม" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

แอปจะสแกนไฟล์ที่เลือกและจัดระเบียบโดยใช้ข้อมูลเมตาเป็นส่วนต่างๆ เช่น ศิลปิน อัลบั้ม แนวเพลง และนักแต่งเพลง

{{< cards cols="1">}}
{{< card title="" subtitle="คลังเพลงพร้อมหมวดหมู่" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## สร้างเพลย์ลิสต์

คุณยังสามารถสร้างเพลย์ลิสต์ของคุณเองได้

ก่อนอื่น เปิดแท็บ **เพลย์ลิสต์**

{{< cards cols="1">}}
{{< card title="" subtitle="แท็บเพลย์ลิสต์ใน Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

แตะปุ่ม **บวก (+)** และเลือก **เพลย์ลิสต์ใหม่**

{{< cards cols="1">}}
{{< card title="" subtitle="สร้างเพลย์ลิสต์ใหม่" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

ป้อนชื่อเพลย์ลิสต์และแตะ **บันทึก**

{{< cards cols="1">}}
{{< card title="" subtitle="ป้อนชื่อเพลย์ลิสต์" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

จากนั้นเลือกแหล่งที่มาเพื่อเพิ่มเพลง — ที่นี่เราเลือก **คลัง**

{{< cards cols="1">}}
{{< card title="" subtitle="เพิ่มเพลงในเพลย์ลิสต์ใหม่" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

เลือกเพลงที่ต้องการและแตะ **เสร็จสิ้น** เพื่อเพิ่ม

{{< cards cols="1">}}
{{< card title="" subtitle="เพิ่มเพลงจากคลังในเพลย์ลิสต์" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

แทร็กที่เลือกจะปรากฏในเพลย์ลิสต์ที่สร้าง

{{< cards cols="1">}}
{{< card title="" subtitle="เพลย์ลิสต์ที่สร้างแสดงในรายการ" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

ตามค่าเริ่มต้น เพลงพร้อมสำหรับสตรีม หากต้องการฟังออฟไลน์ เปิดใช้ **โหมดออฟไลน์** — แอปจะดาวน์โหลดแทร็กทั้งหมด

{{< cards cols="1">}}
{{< card title="" subtitle="โหมดออฟไลน์เปิดใช้สำหรับเพลย์ลิสต์" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

แตะปุ่ม **ดำเนินการเพิ่มเติม** เพื่อสำรวจตัวเลือกเพิ่มเติม คุณสามารถ:

- เก็บเพลย์ลิสต์
- เปลี่ยนปกอัลบั้ม
- จัดเรียงแทร็กใหม่
- และฟีเจอร์ที่เป็นประโยชน์อื่นๆ

{{< cards cols="1">}}
{{< card title="" subtitle="ดำเนินการเพลย์ลิสต์เพิ่มเติมที่มี" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## สรุป

ด้วย **Evermusic** และ **Flacbox** การเปลี่ยน iPhone, iPad หรือ Mac ของคุณเป็นเครื่องเล่นเพลง DLNA ที่ทรงพลังนั้นง่ายดาย

- สตรีม MP3 หรือ FLAC คุณภาพสูงโดยตรงจาก **เซิร์ฟเวอร์ Kodi DLNA** ของคุณ
- สร้างคลังเพลงส่วนตัวจัดกลุ่มตามข้อมูลเมตา (อัลบั้ม แนวเพลง นักแต่งเพลง)
- สร้างและจัดการ **เพลย์ลิสต์ที่กำหนดเอง**
- เปิดใช้ **โหมดออฟไลน์** สำหรับฟังขณะเดินทาง
- เชื่อมต่อกับ **บริการคลาวด์หลายแห่ง** และ **อุปกรณ์เครือข่ายท้องถิ่น**
- ติดตามนิสัยการฟังด้วย **การรวม Last.fm**

ไม่ว่าคุณจะเป็นนักฟังเสียงหรือผู้ฟังทั่วไป Evermusic และ Flacbox มอบทุกสิ่งที่คุณต้องการสำหรับการสตรีมและจัดระเบียบเพลงอย่างราบรื่น

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="ดาวน์โหลด Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="ดาวน์โหลด Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

เริ่มสร้างประสบการณ์เพลงส่วนตัวของคุณวันนี้

## คำถามที่พบบ่อย

{{% details title="Kodi ใช้เป็นเซิร์ฟเวอร์ DLNA ฟรีหรือไม่?" closed="true" %}}
ใช่ Kodi ฟรีทั้งหมดและเป็นโอเพ่นซอร์ส ทำงานบน macOS, Windows, Linux และอุปกรณ์ NAS หลายรุ่น
{{% /details %}}

{{% details title="Evermusic และ Flacbox รองรับการสตรีม FLAC ผ่าน DLNA หรือไม่?" closed="true" %}}
ใช่ Flacbox ได้รับการปรับให้เหมาะกับรูปแบบคุณภาพสูงเช่น FLAC, ALAC และ DSD Evermusic ยังรองรับการเล่น FLAC ร่วมกับ MP3 และรูปแบบมาตรฐานอื่นๆ
{{% /details %}}

{{% details title="ฉันสามารถฟังออฟไลน์หลังจากสตรีมจาก Kodi ได้หรือไม่?" closed="true" %}}
ได้ เปิดใช้โหมดออฟไลน์บนเพลย์ลิสต์ใดก็ได้ แอปจะดาวน์โหลดแทร็กทั้งหมดไปยังอุปกรณ์ของคุณ
{{% /details %}}

{{% details title="ฉันต้องสมัครสมาชิกพรีเมียมเพื่อใช้ DLNA หรือไม่?" closed="true" %}}
เวอร์ชันฟรีรองรับการเชื่อมต่อคลาวด์หรือเครือข่ายสูงสุด 3 รายการ พรีเมียมจะลบข้อจำกัดนี้
{{% /details %}}

{{% details title="iPhone ของฉันต้องอยู่ในเครือข่าย Wi-Fi เดียวกันกับ Kodi หรือไม่?" closed="true" %}}
ใช่ การสตรีม DLNA ทำงานผ่านเครือข่ายท้องถิ่น ทั้งเซิร์ฟเวอร์ Kodi และอุปกรณ์ iOS ต้องเชื่อมต่อกับเครือข่าย Wi-Fi เดียวกัน
{{% /details %}}

{{% details title="ฉันสามารถใช้การตั้งค่านี้กับ NAS แทน Mac หรือ PC ได้หรือไม่?" closed="true" %}}
ได้ อุปกรณ์ NAS หลายรุ่น (Synology, QNAP ฯลฯ) รองรับ Kodi หรือมีเซิร์ฟเวอร์ DLNA ในตัว Evermusic และ Flacbox สามารถเชื่อมต่อกับเซิร์ฟเวอร์ DLNA/UPnP มาตรฐานใดก็ได้
{{% /details %}}
