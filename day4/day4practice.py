with open("output.txt","r",encoding="utf-8")as f:
    lines=f.readlines()
        
with open("result.txt","w",encoding="utf-8")as f:
    f.write("文件内容：\n")
    for line in lines:
        f.write(line)
    f.write(f"\n总行数为：{len(lines)}\n")
