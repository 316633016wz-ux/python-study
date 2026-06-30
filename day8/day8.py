import pymysql
import pandas as pd 

conn=pymysql.connect(
    host="localhost",
    user="root",
    password="Wuzhewuzhe123",
    database="bookstore",
    charset="utf8"
)

cursor=conn.cursor()

# cursor.execute("SHOW TABLES;")

# cursor.execute("SELECT * FROM books;")

# sql="INSERT INTO books (title,author,price,year) VALUES('平凡的世界','路遥',48,1986);"
# cursor.execute(sql)
# conn.commit()
# print('插入成功')

# sql = "DELETE FROM books WHERE id = 7;"
# cursor.execute(sql)
# conn.commit()

# print("删除成功！")

# sql="UPDATE books SET price=55 WHERE title='三体';"
# cursor.execute(sql)
# conn.commit()
# print('更新成功')

# cursor.execute("SELECT * FROM books;")

# result=cursor.fetchall()

# for row in result:
#     print(row)

# cursor.close()

df=pd.read_sql("SELECT * FROM books",conn)
print(df)
print()
print("平均价格:",df["price"].mean())

conn.close()