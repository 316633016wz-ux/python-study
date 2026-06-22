def add_fruit(stock,name,count):
    if name in stock:
        stock[name]+=count
    else:
        stock[name]=count

stock={}

add_fruit(stock,"苹果",5)
add_fruit(stock,"香蕉",3)
add_fruit(stock,"橙子",8)

for key in stock:
    print(f"{key}库存{stock[key]}个")

print(f"共{len(stock)}种水果")
