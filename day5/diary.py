from datetime import datetime

def write_diary():
    content=input("写日记：")
    now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt","a",encoding="utf-8")as f:
        f.write(f"{now}\n{content}\n\n")
    print("日记已保存")

def show_diary():
    try:
        with open("diary.txt","r",encoding="utf-8")as f:
            print("\n=====我的日记=====")
            for line in f:
                print(line,end="")
    except FileNotFoundError:
         print("还没有日记")

while True:
    print("\n1.写日记 2.查看日记 0.退出")
    choice=input("选择:")
    if choice=="1":
        write_diary()
    elif choice=="2":
        show_diary()
    elif choice=="0":
        break
    else:
        print("输入错误")
