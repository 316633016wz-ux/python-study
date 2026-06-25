import pandas as pd

data={
    "姓名":["小王","小明","小李","小红","小龙"],
    "语文":[99,96,39,59,88],
    "数学":[100,50,69,85,99],
    "英语":[98,99,85,100,20]
}

df=pd.DataFrame(data)

df.to_csv("scores.csv",index=False,encoding="utf-8-sig")

df2=pd.read_csv("scores.csv",encoding="utf-8-sig")

print(f"数学大于85的同学：{df.loc[df['数学']>85,'姓名']}")

print(f"语文成绩平均分为：{df['语文'].mean():.2f}")

df_sorted=df.sort_values("数学",ascending=False)
print(df_sorted)

df["总分"]=df["数学"]+df["语文"]+df["英语"]
print(df)

print(df.describe())
