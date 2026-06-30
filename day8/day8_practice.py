import pymysql
import pandas as pd

conn=pymysql.connect(
    host="localhost",
    user="root",
    password="Wuzhewuzhe123",
    database="student_system",
    charset="utf8"
)

cursor=conn.cursor()

# sql="INSERT INTO students (name,age,score) VALUES('王五',22,99),('张二',23,20),('李六',21,0);"
# cursor.execute(sql)
# conn.commit()
# print("插入成功")

df=pd.read_sql("SELECT * FROM students",conn)
print(df)

print(f"平均成绩：{df['score'].mean():.2f}")

print(f"最高分同学：{df.loc[df['score']==df['score'].max(),'name'].values[0]}")
conn.close()


