import pymysql
import pandas as pd
from sqlalchemy import create_engine

engine=create_engine("mysql+pymysql://root:Wuzhewuzhe123@localhost/bookstore?charset=utf8")

# data={
#     "title":["红楼梦","西游记"],
#     "author":["曹雪芹","吴承恩"],
#     "price":[52,45],
#     "year":[1791,1592]
# }
# df_new=pd.DataFrame(data)

# df_new.to_sql("books",engine,if_exists="append",index=False)
# print("写入成功")

df=pd.read_sql("SELECT * FROM books",engine)
print(df)

