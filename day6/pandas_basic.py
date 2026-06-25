import pandas as pd

data={
    "姓名":["小明","小红","小刚"],
    "语文":[85,92,78],
    "数学":[90,88,85]
}

df=pd.DataFrame(data)
print(df)

print(df["语文"])

print(df["语文"].mean())

print(df["数学"] > 88)

print(df[df["数学"]>88])

print(df.loc[df["数学"]>88,"姓名"])

df.to_csv("student.csv",index=False,encoding="utf-8-sig")
print("CSV已保存")

df2=pd.read_csv("student.csv",encoding="utf-8-sig")
print(df2)

df_sorted=df.sort_values("数学",ascending=False)
print(df_sorted)

df["总分"]=df["数学"]+df["语文"]
print(df)

print(df.describe())
