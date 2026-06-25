import pandas as pd

data={
    "商品名":["手机","电脑","平板"],
    "单价":[6000,15000,3000],
    "销量":[100,50,29]
}

df=pd.DataFrame(data)

df["总销售额"]=df["单价"]*df["销量"]

df.to_csv("sales.csv",index=False,encoding="utf-8-sig")

df2=pd.read_csv("sales.csv",encoding="utf-8-sig")

df_totalsalesmax=df['总销售额'].max()

print(f"总销售额最高的商品是：{df.loc[df['总销售额']==df_totalsalesmax,'商品名']}")

print(f"所有商品的平均单价是：{df['单价'].mean()}")

df_sorted=df.sort_values("总销售额",ascending=False)

print(df_sorted)

      

