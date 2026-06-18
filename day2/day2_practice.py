name=input("请输入你的名字：")
score=int(input("请输入你的成绩："))

print("你好",name)

if score>=90:
    print("优秀")
elif score>=80:
    print("良好")
elif score>=60:
    print("及格")
else:
    print("不及格")

print("下面输出1到5的数字：")

for i in range(1,6):
    print(i)

total=0
for i in range(1,101):
    total+=i
print("1到100的和为：",total)