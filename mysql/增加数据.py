#coding=utf-8
import pymysql

con = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='Shouhuzhe@2018',
    db='pt_base',
)

cur = con.cursor()

sql = 'insert into pt_user(user_name) values("laoliu")'

try:
    cur.execute(sql)
    con.commit()
    print("数据插入成功")
except Exception as e:
    print(e)
    print("插入数据失败")
finally:
    cur.close()

