## FastAPI & SQLAlchemy: MySQL Setup Project with Clean Architecture

### ขั้นตอนเริ่มต้นสำหรับผู้ที่ยังไม่ได้ติดตั้ง `virtualenv` ในระบบ  

```bash
$ python -m pip install virtualenv 
$ python -m venv env 
```

### การเปิดใช้งาน Virtual Environment

#### บน Linux และ macOS

```bash
source env/bin/activate  
```

## บน Windows

```bash
.\env\Scripts\activate 
```


### การติดตั้ง Dependencies ด้วย requirements.txt

```bash
pip install -r requirements.txt 
```


### เรียกใช้ docker-compose เพื่อสร้างและรัน MySQL

```bash
docker-compose up -d
```

### ตรวจสอบสถานะของ container

```bash
docker ps 
```

### หากต้องการหยุดการทำงาน

```bash
docker-compose down
```