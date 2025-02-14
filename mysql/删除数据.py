# coding=utf-8
import pymysql
con = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='Shouhuzhe@2018',
    db='pt_base'
)

cur = con.cursor()

sql = 'delete from pt_user where user_name=%s'

try:
    cur.execute(sql,('lisi01'))
    con.commit()
    print("删除成功")
except Exception as e:
    print(e)
    print("删除失败")
finally:
    con.close()
