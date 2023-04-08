# 등록된 지문인지 여부 확인 프로그램
from pyfingerprint.pyfingerprint import PyFingerprint
import pymysql
import mysql.connector

person = mysql.connector.connect(
  host="database.cv7tztt1jtpd.ap-northeast-2.rds.amazonaws.com",
  user="admin",
  password="1q2w3e4r",
  database="person"
)
try:
    f=PyFingerprint('/dev/ttyAMAO', 57600, 0xFFFFFFFF, 0x00000000) 
    if (f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
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
    cur = person.cursor
    sql="select * from FingerPrint" 
    cur.execute(sql)
    for row in cur. fetchall:
        print(f.uploadCharacteristics(0x02, eval(row[0])))
        score=f.compareCharacteristics()
        print(score)
except Exception as e:
    print('Operation failed!')
    print ('Exception message: '+ str(e))
    exit(1)
finally:
    person.close()
