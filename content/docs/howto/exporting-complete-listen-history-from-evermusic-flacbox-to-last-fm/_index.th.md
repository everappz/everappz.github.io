---
title: "ส่งออกประวัติการฟังทั้งหมดจาก Evermusic และ Flacbox ไปยัง Last.fm"
date: 2024-01-30
description: "เรียนรู้วิธีส่งออกประวัติเพลงจาก Evermusic และ Flacbox และอัปโหลดไปยัง Last.fm โดยใช้ไฟล์ CSV และเครื่องมือ Last.fm Scrubbler สำหรับ Windows"
keywords: ["evermusic", "flacbox", "lastfm", "ประวัติเพลง", "สครอบบลิง", "ส่งออกเพลง", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "ล่าสุด", "lastfm", "ส่งออก", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**สรุป:** ส่งออกประวัติการฟังของคุณจาก Evermusic หรือ Flacbox เป็นไฟล์ CSV จากนั้นอัปโหลดไปยัง Last.fm โดยใช้เครื่องมือฟรี Last.fm-Scrubbler-WPF บน Windows การ scrobble อัตโนมัติยังมีให้ใช้งานในทั้งสองแอปด้วย

**อัปเดต:** การ scrobble อัตโนมัติพร้อมใช้งานแล้ว! เรียนรู้เพิ่มเติมที่นี่: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling เป็นวิธีง่ายๆ ในการบันทึกรายละเอียดพื้นฐานโดยอัตโนมัติ เช่น ชื่อเพลงและศิลปินของเพลงที่คุณกำลังเล่นไปยังบริการออนไลน์ ในภายหลังคุณสามารถตรวจสอบประวัติการฟังของคุณได้

[Last.fm](https://www.last.fm/home) ขับเคลื่อนโดยระบบแนะนำเพลงที่เรียกว่า Audioscrobbler ให้บริการนี้ฟรี มันสร้างโปรไฟล์รายละเอียดของรสนิยมทางดนตรีของคุณโดยการบันทึกแทร็กที่คุณฟัง ไม่ว่าจะเป็นจากสถานีวิทยุอินเทอร์เน็ต คอมพิวเตอร์ของคุณ หรืออุปกรณ์เล่นเพลงพกพาต่างๆ คุณสามารถเยี่ยมชมเว็บไซต์ในภายหลังเพื่อรับคำแนะนำศิลปินหรืออัลบั้มใหม่ที่ตรงกับรสนิยมทางดนตรีของคุณ

คุณสามารถอัปโหลดประวัติการฟังไปยัง [Last.fm](http://Last.fm) จากแอป Evermusic และ Flacbox โดยใช้เครื่องมือฟรี และเราจะแนะนำวิธีการทำ

เปิดส่วน 'คลังเพลง' ของแอปพลิเคชันและเลื่อนไปที่ส่วน 'เข้าถึงด่วน' แตะรายการเมนู 'ล่าสุด'

![หน้าจอคลังเพลง](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

บนหน้าจอ 'ล่าสุด' แตะปุ่ม 'เพิ่มเติม' ที่มุมขวาบนเพื่อเปิดเมนู 'ดำเนินการเพิ่มเติม' แตะรายการเมนู 'ส่งออกรายการเพลง'

![หน้าจอล่าสุด](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

บนหน้าจอ 'เลือกรูปแบบไฟล์' คุณสามารถเลือกรูปแบบของไฟล์ปลายทาง ตัวเลือกที่มี - CSV, TXT, M3U

![หน้าจอเลือกรูปแบบไฟล์](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: ย่อมาจาก Comma-Separated Values เหมาะสำหรับจัดระเบียบข้อมูลของคุณในรูปแบบตาราง ในไฟล์ปลายทาง คุณจะพบพารามิเตอร์ เช่น ชื่อศิลปิน ชื่ออัลบั้ม ชื่อแทร็ก เวลาประทับ (เวลาที่คุณฟังแทร็ก) ชื่อศิลปินอัลบั้ม และความยาวแทร็ก

TXT: นี่คือไฟล์ข้อความธรรมดา เรียบง่ายและตรงไปตรงมา มีพารามิเตอร์รวมถึงชื่อศิลปิน ชื่ออัลบั้ม ชื่อแทร็ก และความยาว

M3U: รูปแบบนี้เป็นตัวเลือกหลักสำหรับการสร้างเพลย์ลิสต์ มันดีมากเพราะคุณสามารถส่งออกรายการเพลงและเพลิดเพลินกับแทร็กของคุณบนอุปกรณ์ใดก็ได้ แม้ว่าคุณจะไม่มีไฟล์ต้นฉบับ (หากคุณเลือกตัวเลือก URL แบบสมบูรณ์สำหรับไฟล์มีเดีย) ในไฟล์เอาต์พุต คุณจะพบพารามิเตอร์ เช่น ความยาว ชื่อศิลปิน ชื่อแทร็ก และตำแหน่งไฟล์มีเดีย

สำหรับงานของเรา การเลือก CSV เป็นทางเลือกที่ถูกต้อง เราจะใช้ไฟล์นี้กับซอฟต์แวร์ฟรี Last.fm-Scrubbler-WPF เพื่ออัปโหลดประวัติการฟังของเราไปยังบริการ [Last.fm](http://Last.fm) เพียงเลือก CSV แล้วกดปุ่ม 'ส่งออก'

![หน้าจอส่งออกเสร็จสมบูรณ์](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

หลังจากการส่งออกเสร็จสมบูรณ์ เพียงแตะปุ่ม 'แสดงไฟล์' แล้วแอปจะแสดงไฟล์ที่สร้างขึ้นในโฟลเดอร์เอกสารของคุณ จากนั้นแตะปุ่ม 'ดำเนินการเพิ่มเติม' ข้างชื่อไฟล์และเลือกตัวเลือก 'เปิดใน' จากเมนู ขั้นตอนต่อไปคือการคัดลอกไฟล์ที่ส่งออกไปยังคอมพิวเตอร์เดสก์ท็อปของคุณ คุณสามารถทำได้ง่ายๆ โดยเลือกตัวเลือก AirDrop จากเมนู 'เปิดใน'

![การดำเนินการเพิ่มเติมสำหรับไฟล์ที่ส่งออก](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

ต่อไปเราจะใช้ไคลเอนต์โอเพนซอร์สฟรีของ [Last.FM](http://Last.FM) ซึ่งมีให้ใช้งานบนแพลตฟอร์ม Windows เท่านั้น ไคลเอนต์นี้ช่วยให้คุณอัปเดตประวัติการฟังบน [Last.FM](http://Last.FM) ได้อย่างมีประสิทธิภาพโดยใช้ไฟล์ CSV ที่เราเพิ่งส่งออก

ตอนนี้ หากคุณไม่ได้ใช้คอมพิวเตอร์ Windows ไม่ต้องกังวล คุณยังสามารถเข้าถึงไคลเอนต์นี้ได้โดยการติดตั้ง VirtualBox บน Mac ของคุณและใช้ไฟล์อิมเมจสภาพแวดล้อมการพัฒนา Windows อย่างเป็นทางการ

นี่คือสิ่งที่คุณต้องทำ:

- ติดตั้ง VirtualBox จากลิงก์ต่อไปนี้: [ดาวน์โหลด VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- ดาวน์โหลดและติดตั้งสภาพแวดล้อมการพัฒนา Windows จากลิงก์นี้: [สภาพแวดล้อมการพัฒนา Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

บนคอมพิวเตอร์ Windows ของคุณ (หรือแอป VirtualBox ที่มีอิมเมจ Windows Development) ดาวน์โหลดและติดตั้ง [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - ซอฟต์แวร์โอเพนซอร์สฟรีที่มีบน GitHub เราทดสอบบนเวอร์ชัน 1.28 ซึ่งคุณสามารถดาวน์โหลดได้ที่นี่: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![หน้าดาวน์โหลด Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

ในส่วน 'Assets' แตะที่ [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) เพื่อดาวน์โหลดไฟล์เก็บถาวรการติดตั้ง แตกไฟล์ที่ดาวน์โหลดมาและเปิดโฟลเดอร์ที่แตกออกมา

- สำคัญ

แอปนี้ยังอยู่ในเวอร์ชันเบต้า ผู้สร้างแอปไม่ได้ทำการทดสอบมากนัก พวกเขาแนะนำให้ลอง scrobble ไปยังบัญชีทดสอบก่อนและดูว่าสิ่งที่คุณต้องการ scrobble ทำงานอย่างถูกต้องหรือไม่ โดยเฉพาะถ้าคุณ scrobble แทร็กจำนวนมากในครั้งเดียว โปรดระมัดระวังกับบัญชีของคุณ

เรียกใช้ Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

บนหน้าจอหลักของแอปพลิเคชัน เพียงแตะที่ 'ยังไม่ได้เข้าสู่ระบบ' ที่มุมซ้ายล่างเพื่อเปิดหน้าจอ 'เพิ่มบัญชี'

![หน้าจอเพิ่มบัญชี](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

กรอกข้อมูลประจำตัวสำหรับเข้าสู่ระบบของคุณ

![หน้าจอกรอกข้อมูลเข้าสู่ระบบ](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

แตะปุ่ม 'Login' เพื่อเพิ่มบัญชีของคุณ

![แตะปุ่ม Login เพื่อเพิ่มบัญชีของคุณ](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

เปิดแท็บ 'File Parse Scrobbler' เพื่อเริ่มนำเข้าไฟล์ CSV จากแอป Evermusic

![เปิดแท็บ File Parse Scrobbler เพื่อเริ่มนำเข้าไฟล์ CSV จากแอป Evermusic](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

เลือก 'Parser: CSV' แล้วแตะปุ่ม 'Settings'

บนหน้าจอถัดไป คุณสามารถเลือกลำดับของพารามิเตอร์ในไฟล์ CSV ของคุณ

ฟิลด์แต่ละรายการสามารถล้อมรอบด้วยเครื่องหมายคำพูดและจำเป็นต้องล้อมรอบด้วยเครื่องหมายคำพูดหากฟิลด์มีตัวคั่นที่ตั้งค่าไว้ ตัวอย่างเช่น:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

ดังนั้นให้ปล่อยการตั้งค่าทั้งหมดเป็นค่าเริ่มต้น สิ่งเดียวที่คุณต้องเปลี่ยนคือเปิดใช้งานช่องทำเครื่องหมายในฟิลด์ 'Has Fields Enclosed In Quotes'

แตะ 'Save & Close' เพื่อใช้การเปลี่ยนแปลง

![เลือกลำดับของพารามิเตอร์ในไฟล์ CSV ของคุณ](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

การ scrobble โดยการแยกวิเคราะห์ไฟล์มีสองโหมด สามารถเปลี่ยนได้ด้วย ComboBox 'Scrobbling Mode'

โหมดปกติ: ในโหมดนี้ แทร็กจะถูก scrobble ด้วยเวลาประทับจาก scrobble ที่แยกวิเคราะห์แล้ว เฉพาะ scrobble ที่ใหม่กว่า 14 วันเท่านั้นที่สามารถ scrobble ได้

โหมดนำเข้า: ในโหมดนี้ แทร็กจะถูก scrobble ด้วยเวลาประทับที่คำนวณจาก 'Finish Time' และระยะเวลาที่เลือกระหว่างแต่ละแทร็ก สิ่งนี้ช่วยให้สามารถ scrobble แทร็กได้แม้ว่าเวลาประทับของ scrobble ที่แยกวิเคราะห์จะเก่ากว่า 14 วัน ดังนั้น แทร็กแรก (บนสุด) ในไฟล์ CSV จะถูก scrobble ด้วย 'Finish Time'

เลือกไฟล์ CSV ที่สร้างไว้ก่อนหน้านี้จากแอป Evermusic ในฟิลด์ 'File:' แล้วแตะ 'Parse' ในบางกรณี คุณอาจเห็นการแจ้งเตือนข้อผิดพลาดว่า scrobble บางรายการไม่สามารถแยกวิเคราะห์ได้ ไม่เป็นไรหากคุณมีแทร็กบางรายการที่ไม่มีข้อมูลเมตาครบถ้วน เช่น ชื่อศิลปิน

![scrobble บางรายการไม่สามารถแยกวิเคราะห์ได้](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

แตะปุ่ม 'Check All' เพื่อเลือกแทร็กที่แยกวิเคราะห์ทั้งหมด

![แตะปุ่ม Check All เพื่อเลือกแทร็กที่แยกวิเคราะห์ทั้งหมด](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

แตะปุ่ม 'Preview' เพื่อตรวจสอบการเปลี่ยนแปลงทั้งหมดที่จะถูกส่งไปยังเซิร์ฟเวอร์

![แตะปุ่ม Preview เพื่อตรวจสอบการเปลี่ยนแปลงทั้งหมดที่จะถูกส่งไปยังเซิร์ฟเวอร์](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

แตะปุ่ม 'Scrobble' เพื่ออัปโหลดการเปลี่ยนแปลงทั้งหมดไปยังเซิร์ฟเวอร์

![แตะปุ่ม Scrobble เพื่ออัปโหลดการเปลี่ยนแปลงทั้งหมดไปยังเซิร์ฟเวอร์](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

ก่อนหน้านี้ Last.fm-Scrubbler-WPF ไม่มีขีดจำกัด scrobble ต่อวัน ตอนนี้เปลี่ยนแล้วเพราะบางคนใช้ Scrubbler เพื่อ scrobble แทร็กจำนวนมากจนทำให้เกิดปัญหาสำหรับหน้า Last.fm ขีดจำกัด scrobble ปัจจุบันคือ 2800 scrobble ต่อวัน เมื่อคุณพยายาม scrobble มากกว่านั้น คุณจะได้รับข้อความแสดงข้อผิดพลาด มีแผนที่จะเพิ่ม 'คิว scrobble' ดังนั้นหากคุณต้อง scrobble มากกว่า 2800 แทร็ก จะถูกเพิ่มไปยังคิวและ scrobble โดยอัตโนมัติหลังจากผ่านไประยะหนึ่ง คุณสามารถตรวจสอบจำนวน scrobble ที่เหลือได้ในมุมมองการเลือกผู้ใช้

เมื่อระเบียนทั้งหมดถูกอัปโหลดไปยังเซิร์ฟเวอร์สำเร็จ คุณจะเห็นข้อความที่ด้านล่างของหน้าต่างแอปยืนยันว่า: 'Successfully scrobbled selected tracks.'

![Successfully scrobbled selected tracks.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

ตอนนี้คุณสามารถเปิดโปรไฟล์ของคุณบนหน้า [Last.fm](http://Last.fm) และตรวจสอบการเปลี่ยนแปลงทั้งหมด

![โปรไฟล์ของคุณบนหน้า Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## คำถามที่พบบ่อย

{{% details title="ฉันสามารถ scrobble โดยอัตโนมัติโดยไม่ต้องส่งออกไฟล์ CSV ได้หรือไม่?" closed="true" %}}
ได้ ทั้ง Evermusic และ Flacbox รองรับการ scrobble อัตโนมัติไปยัง Last.fm แล้ว ดูคู่มือ: [วิธี Scrobble ไปยัง Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)
{{% /details %}}

{{% details title="จะทำอย่างไรถ้า CSV ของฉันมีแทร็กที่เก่ากว่า 14 วัน?" closed="true" %}}
ใช้โหมดนำเข้าใน Last.fm-Scrubbler-WPF มันคำนวณเวลาประทับใหม่จาก Finish Time ทำให้คุณสามารถ scrobble แทร็กได้โดยไม่คำนึงถึงวันที่ดั้งเดิม
{{% /details %}}

{{% details title="ฉันไม่มีคอมพิวเตอร์ Windows ฉันยังสามารถใช้ Last.fm-Scrubbler ได้หรือไม่?" closed="true" %}}
ได้ ติดตั้ง VirtualBox บน Mac ของคุณและดาวน์โหลดอิมเมจสภาพแวดล้อมการพัฒนา Windows ฟรีจาก Microsoft เรียกใช้ Last.fm-Scrubbler-WPF ภายในเครื่องเสมือน
{{% /details %}}

{{% details title="ทำไม scrobble บางรายการไม่ถูกแยกวิเคราะห์?" closed="true" %}}
แทร็กที่ขาดข้อมูลเมตาที่จำเป็น (เช่น ชื่อศิลปิน) ไม่สามารถแยกวิเคราะห์ได้ นี่เป็นสิ่งที่คาดหวังได้และไม่กระทบแทร็กอื่นในไฟล์
{{% /details %}}

{{% details title="มีขีดจำกัด scrobble ต่อวันหรือไม่?" closed="true" %}}
มี Last.fm-Scrubbler-WPF อนุญาตได้สูงสุด 2,800 scrobble ต่อวัน หากคุณต้อง scrobble มากกว่านั้น ให้แบ่งกระบวนการออกเป็นหลายวัน
{{% /details %}}
