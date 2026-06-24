import random

def game():
    number=random.randint(1,100)
    count=0
    print("\n我想了个1-100间的随机数，你来猜")
    while True:
        guess=int(input("请输入一个数字："))
        count+=1
        if guess==number:
            print(f"恭喜你猜对了，用了{count}次")
            break
        elif guess<number:
            print("太小了")
        else:
            print("太大了")


while True:
    game()
    choice=input("\n是否再玩一局（是/否):")
    if choice=="否":
        break
