# AIPrototype2023
 Thanapat Sopon
 ID : 633020444-1 : SIDS

# คาบ 1
การใช้ Clound ทำ Web
ข้อดี
- ราคาที่ดีประหยัด ใช้แค่ไหนจ่ายแค่นั้น
- ทุกอย่างเร็วขึ้น ไม่ต้องมาเสียเวลาหาจ้างคนค่อยดูแลระบบและไม่รู้ว่าใครเก่งไม่เก่ง เพราะ Cloud มีคนที่เก่งค่อยดูแลให้
- เข้ากับข้อตกลงของบริษัทได้ เนื่องจากมีความปลอดภัยครบ
- ใช้แค่ Browser ที่รันได้
ข้อเสีย
- มีการเปลี่ยนแปลงอยู่เรื่อยๆ
- จำเป็นต้องใช้ Internet
- ทุกอย่างเป็น service จำเป็นต้องมีความรู้นิดหน่อยเพื่อให้รันได้ และจะได้ไม่ต้องเสียเงินซื้อทุกอย่าง
- ทุกอย่างอยู่บน Internet ถ้าสาย Internet เสีย ทุกอย่างจบ งานอาจจะทำต่อไม่ได้

# คาบ 2
- Ssh ไว้เชื่อมต่อบน cloud 
- Scp 
- Exit ออก
- Pwd เราอยู่ไหน
- Ssh ชื่อ ACC @ IP
- Htop เพื่อดูเครื่องเรา
- scp -r testfolder1/ thanapat_window@13.67.90.233:/home/thanapat_window/. = ย้ายโฟลเดอร์เข้าไดฟ์ scp -r ชื่อโฟลเดอร์/ชื่อ cloud@IP:/home/ชื่อเครื่อง/.
- R = 4
- W = 2
- X = 1
- Cat อ่านเฉยๆแบบไม่ต้องเปิด cat ชื่อไฟล์
- Sudo chmod 755 ชื่อคน
- เจ้า 7=ทำได้ทุกอย่าง เพื่อน 5=อ่านกับรันได้ คนดู 5=อ่านกับรันได้
- Exit() = ใน python
- scp thanapat_window@13.67.90.233:/home/thanapat_window/print.py ~/. = ย้ายจากไดฟ์ลงเครื่อง scp ชื่อ cloud@IP:/home/ชื่อเครื่อง/ชื่อไฟล์ ~/.
- เข้ากับเพื่อน : ssh ชื่อที่เพื่อนตั้ง@IP เพื่อน ตัวอย่าง ssh thanapat_window@4.216.171.68
- Ctrl+C  = ยกเลิกคำสั่ง

# คาบ 3
- สร้างใหม่ = conda create -n mypy38(ชื่อที่เราต้องการตั้ง) python=3.8(เวอร์ชั่นเลือกเองได้)
- $ conda activate mypy38 เริ่มใช้
- $ conda deactivate เลิกใช้
- Manls เอาไว้ดูคำสั่งที่ใช้ได้
- sudo apt-get install ffmpeg = ใช้ดาวร์โหลด พก ของ Linux
- sudo snap install ffmpeg
- conda ใช้ใน Linux แทน pip
- conda install notebook ใช้ดาวร์โหลด jupyter
- screen -S sc1 ใช้สร้าง screen ใหม่ sc1 คือ ชื่อ อะไรก็ได้
- Ctrl+A ยกนิ้วขึ้นกด D เพื่อออกจาก screen
- screen -R sc1 เพื่อเข้า screen ใหม่
- ctel + A แล้วกด K จากนั้นเลือก Y = เพื่อ Kill screen
- screen -ls เพื่อดูว่ายังเหลือ screen อยู่มั้ย

# คาบ 4
- git pull ใช้ก่อนอัปลง Github
- git status เช็คไฟล์ว่าถูกแก้มั้ย
- git add (filename)
- git commit -m "..."
- git push พอไป github ให้ใช้คำสั่งนี้
- Import package : argparse : รับ input ข้างนอก
- Create function parse_input รับตัวแปรตอนเรารัน python
main function (flow follow after this)
- เริ่มจาก รับค่าตัวแปร input_V = parse_input() {function}
- print(the input xx i (ค่าตัวแปร x ไม่มีก็=7)
- print("we are in the main function")
- function การคูณ 9*ตัวแปร x
- print(”hello”) function

# คาบ 5
- การบ้าน

# คาบ 6
วิธีรันพวก python จะใช้ python ชื่อโฟลเดอร์    ตัวอย่าง python python_subprocess.py คือชื่อ
code python_subprocess.py  = การสร้าง VScode Python

# คาบ 7
- from flask : import libary ดาวร์โหลด libary
- app = Flask(name)
- def helloworld():
- route(”/”) = ในเว็บ ถ้าเปิดแบบนี้ www.flask.com/
- / มีกี่อันก็ได้ตามที่เราสร้าง

# คาบ 8
- fw เอาไว้ใช้เก็บไลบรารี่ต่าง ๆ ที่เราได้ทำการติดตั้งผ่าน pip
- templates เอาไว้ใช้เก็บไฟล์ HTML
- app.py เอาไว้ใช้เขียนและเอาไว้รัน flask
- static เอาไว้ใช้เก็บไฟล์ static(ไฟล์ที่ไม่มีการเปลี่ยนแปลงของคอนเทนต์) ต่าง ๆ เช่น JavaScript(js), CSS และไฟล์รูปภาพนามสกุลต่าง ๆ เช่น jpg, png เป็นต้น ซึ่งเราจะต้องเก็บไฟล์เหล่านี้ ไว้ที่โฟลเดอร์ static

# คาบ 9
![Screenshot 2024-02-27 043334](https://github.com/TungSoPon/AIPrototype2023/assets/108257588/897c67e4-e6cf-40a2-ac5c-f8f36a578806)

- Input Node ขึ้นอยู่กับ feature = n
- Input Node → layer 1 → layer 2 → output

![6](https://github.com/TungSoPon/AIPrototype2023/assets/108257588/1428f5c0-ed5b-4049-ab81-5566aa1ea010)

- max pooling = สรุปเฉพาะจุดเด่น
- activation function = กำหนดค่าที่ไปคูณให้อยู่ใน range ต้องการ

![7](https://github.com/TungSoPon/AIPrototype2023/assets/108257588/ee66874a-b542-4269-8825-e74967dde060)

- ช่องสีเหลืองจำคำนวณรอบๆแล้วเอาใส่ตรงกลางแบบนี้

-ค่า Loss สามารถหาได้จาก
![image](https://github.com/TungSoPon/AIPrototype2023/assets/108257588/488586bc-f6ff-48e9-bbd1-1c9b2bec9b1f)

