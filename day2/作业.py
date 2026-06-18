age = int(input("输入你的年龄："))
if age>=18:
    print("成年人")
else:
    print("未成年人")

n=int(input("输入一个数字n"))
total=0
for i in range(1,n+1):
    total+=i
print(total)

password="123456"
for i in range(3):
    user_input=input("请输入密码:")
    if user_input==password:
        print("登录成功")
        break
    else:
        print("登录失败")