# f=open("test.txt","r",encoding="utf-8")
# content=f.read()
# f.close()
# print(content)

# with open("test.txt","r",encoding="utf-8")as f:
#     content=f.read()
# print(content)

# with open("output.txt","w",encoding="utf-8")as f:
#     f.write("第一行\n")
#     f.write("第二行\n")

# with open("output.txt","a",encoding="utf-8")as f:
#     f.write("第三行\n")

with open("output.txt","r",encoding="utf-8")as f:
    lines=f.readlines()

for line in lines:
    print(line.strip())
