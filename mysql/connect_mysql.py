# coding=utf-8
import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Shouhuzhe@2018",
    database="pt_base"
)

cur = conn.cursor()

# 使用cursor进行数据库操作

sql = """
    create table t_student(
    sno int primary key auto_increment,
    name varchar(30) not null,
    age int(2),
    score float(3,1) 
    )
"""

sql2 = " select * from t_student "

cur.execute(sql2)

cur.close

try:
    #执行创建表的sql语句
    cur.execute(sql)
    print("创建成功")
except Exception as e:
    print(e)
    print("创建表失败")
finally:
    #关闭连接
    cur.close()