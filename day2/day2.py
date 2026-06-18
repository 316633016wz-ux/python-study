score=int(input("请输入成绩："))
print(score)

if score>=90:
    print("优秀")
elif score>=80:
    print("良好")
elif score>=60:
    print("及格")
else:
    print("不及格")


for i in range(5):
    print(i)
 
total= 0
for i in range(1,101):
    total+=i
print("1到100的和为：",total)

count=1

while count<=5:
    print(count)
    count+=1

while True:
    text=input("请输入内容,输入exit退出:")
    if text=="exit":
        break
    print("你输入的是:",text)    
print("程序结束")
