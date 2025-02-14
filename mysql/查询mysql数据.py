#coding=utf-8
import pymysql


con = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Shouhuzhe@2018",
    database="pt_base"
)

cur=con.cursor()

sql = " select nice_name,user_name,sex,age,mobile from pt_user"

try:
    cur.execute(sql)
    student=cur.fetchall()
    for item in student:
        print(item)
except Exception as e:
    print(e)
    print("查询失败")
finally:
    #关闭链接
    con.close()
