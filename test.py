# 지문 등록
# 지문인식센서로부터 지문데이터를 가져온 후 지문의 특징을 Byte형으로 다운로드 가능
# 이 Byte자료형을 문자열형으로 변환하여 DB에 저장
from pyfingerprint.pyfingerprint import PyFingerprint
import pymysql
import mysql.connector
import datetime

person = mysql.connector.connect(
  host="database.cv7tztt1jtpd.ap-northeast-2.rds.amazonaws.com",
  user="admin",
  password="1q2w3e4r",
  database="person"
)

now = datetime.now()
# PyFingerprint 라이브러리는 PyFingerprint클래스 입니다 /dev/ttyAMA0), 
# verifyPassword()클래스의 메서드 입니다. 
try:
    # PyFingerprint 클래스로 초기화된 지문 인식 센서 객체
    f = PyFingerprint('/dev/ttyAMAO', 57600, 0xFFFFFFFF, 0x00000000) 
    if (f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
# PyFingerprint. 암호가 올바르지 않으면 예외가 발생합니다
except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: '+ str(e))
    exit (1)
    
try:
    print('Waiting for finger...')
    ##지문이 읽힐때까지 기다림
    while (f.readlmage() == False ):
        pass
    ## Converts read image to characteristics and stores it in charbuffer 1
    f.convertlmage(0x01)
    
    # 지문의 특성을 문자열 형태로 변환
    # 지문이 감지되면 코드는 downloadCharacteristics()클래스의 메서드를 호출하여 
    # PyFingerprint센서에서 지문 특성을 다운로드하여 버퍼에 저장합니다.
    # 특성은 문자열로 변환되고 및 메소드를 사용하여 UTF-8로 인코딩 됩니다. 
    Fingerprint = str(f.downloadCharacteristics(0x01)).encode('utf-8')
    cur = person.cursor
        
    # 지문을 DB에 저장
    sql="insert into FingerPrint values (%s)"

    cur.execute(sql)
    person.commit()
except Exception as e:
    print('Operation failed!')
    print('Exception message: '+ str(e))
    exit (1)
finally:
    person.close()
