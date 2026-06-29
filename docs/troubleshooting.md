# 环境与报错排查

## VS Code / 运行提醒

- 写完代码先 Ctrl+S 保存，再到终端运行；文件名旁有小圆点 = 没保存。
- Python 文件后缀必须 .py；运行时 PowerShell 当前目录里必须有该文件。
- `dir` 看文件、`pwd` 看目录、`cd 路径` 进文件夹。
- 右下角若显示 Spaces: 2，改成 Spaces: 4；Python 统一 4 空格缩进。

## 快捷键

- Ctrl+` 开关终端
- Ctrl+S 保存
- Ctrl+/ 注释
- Ctrl+F 搜索
- Ctrl+P 打开文件
- Alt+Shift+F 格式化

## 常见报错

### can't open file
**原因：** 当前目录没有该文件，或文件名拼错
**解决：** `pwd` 看当前目录，`dir` 看文件列表，`cd` 切换到正确目录

### IndentationError
**原因：** 缩进多了/少了/混用了 Tab 和空格
**解决：** Python 统一 4 空格缩进，检查 `if`/`for`/`def` 下一行是否缩进

### SyntaxError
**原因：** 括号、冒号、引号漏了或不匹配
**解决：** 检查 `if`/`for`/`def` 后有没有冒号，括号/引号是否成对

### NameError
**原因：** 变量名拼错或没赋值就使用
**解决：** 检查变量名拼写，确保使用前已赋值

### KeyError
**原因：** 字典访问了不存在的键
**解决：** 用 `for key in d` 遍历字典，或先 `if "键" in d` 检查

### TypeError: write() argument must be str
**原因：** `readlines()` 返回列表，`write()` 只能写字符串
**解决：** 用 `for line in lines: f.write(line)` 逐行写，或 `f.write("".join(lines))`

## MySQL 常见错误

### 中文标点符号
**错误：** `VALUES('张三'，20)` 用了中文逗号
**正确：** `VALUES('张三', 20)` 必须用英文逗号

### 最后一个字段多了逗号
**错误：**
```sql
CREATE TABLE books(
    title VARCHAR(100),
    price FLOAT,    ← 多了逗号
);
```
**正确：**
```sql
CREATE TABLE books(
    title VARCHAR(100),
    price FLOAT     ← 没有逗号
);
```

### 忘记 WHERE 条件
**危险：**
```sql
UPDATE students SET score = 90;  -- 所有学生成绩都变90
DELETE FROM students;            -- 删除所有数据
```
**正确：**
```sql
UPDATE students SET score = 90 WHERE name = '张三';
DELETE FROM students WHERE score < 60;
```
