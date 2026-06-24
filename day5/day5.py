scores={}

try:
    with open("scores.txt","r",encoding="utf-8")as f:
        for line in f:
            line=line.strip()
            if line:
                name,score=line.split(",")
                scores[name]=int(score)
except FileNotFoundError:
    pass

def add_student():
    name=input("输入学生姓名：")
    score=int(input("输入成绩："))
    scores[name]=score
    print(f"已添加{name}的成绩为{score}")

def query_student():
    name=input("请输入姓名：")
    if name in scores:
        print(f"{name}的成绩为：{scores[name]}")
    else:
        print("该考生不存在")

def show_all():
    if not scores:
        print("还没有学生")
    else:
        for name,score in scores.items():
            print(f"{name}:{score}")

def averages():
    if not scores:
        print("还没有学生")
    else:
        average_scores=sum(scores.values())/len(scores)
        print(f"平均分：{average_scores:.2f}")

while True:
    print("\n1.添加学生 2.查询成绩 3.显示所有 4.显示平均分 0.退出")
    choice=input("选择：")
    if choice=="1":
        add_student()
    elif choice=="2":
        query_student()
    elif choice=="3":
        show_all()
    elif choice=="4":
        averages()
    elif choice=="0":
        break
    else:
        print("输入错误")



with open("scores.txt","w",encoding="utf-8")as f:
    for name,score in scores.items():
        f.write(f"{name},{score}\n")



       



    
    

    


