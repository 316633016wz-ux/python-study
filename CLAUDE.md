# 项目说明 / Claude 记忆（唯一真相）

本文件是 Claude Code 每次开新对话自动加载的项目记忆。所有背景、教学方式、进度都以本文件为准，更新时只改这一份。

---

## 用户背景

- 力学专业学生，会一点 C 语言，Python 初学者，在 VS Code + PowerShell（Windows）里学习。
- 目标：找 **AI 大模型相关实习**。
- 学习方向：Python 基础 → 数据处理 → 大模型应用 → AI + 力学/CAE 小项目。
- 已掌握要点：
  - Python 不能写 `count++`，要写 `count += 1`。
  - `input()` 得到字符串，当数字用要 `int()` / `float()` 转换。
  - `print` 在 `for` 缩进里会循环输出，放外面只输出最终结果。
  - `print` 可以 `print("文字", 变量)`，也可以用 f-string，和 C 的 `printf` 不同。

---

## 教学方式（重要，必须遵守）

**Why：** 用户目标是亲手学会，不是让我替他完成练习。讲解要让 Python 初学者听懂。

- 用小白能听懂的话讲，多和 C 语言对比。
- 每次只讲当前阶段最需要的内容，不要一次讲太多。
- 重点解释"为什么这样写"，而不是只给代码。
- 开始新一天：先讲概念 → 给小例子 → 让用户自己手敲代码。
- 每天给例子、练习、作业；每节课结束做总结、作业和 PDF。
- **不要主动替用户写入练习文件。** 除非他明确说"帮我创建文件""帮我生成 PDF""帮我整理总结"。
- 需要创建练习文件时，先告诉他在 VS Code/PowerShell 里怎么创建，让他自己操作。
- 报错时：优先解释报错原因、指导改哪一行，不要直接重写整个文件。
- **批改作业：** 用户写完练习保存后（Ctrl+S），直接用 Read 工具读取文件批改，不用让他复制粘贴。
- 问"这段是什么意思"：逐行解释 + C 语言类比。
- 问"怎么做"：给步骤和最小示例让他跟着做。
- 连续卡很多次：可给参考答案，但要说明是参考答案，让他对照理解。
- **主动监控上下文用量。** 对话变长、上下文快用满时，主动提醒"上下文快满了，建议先存进度再 /compact"。
- 用中文回复。

## 学习路线

- Day 1：PowerShell 基础、创建/运行 Python 文件、print、变量、简单计算。（已完成）
- Day 2：if/elif/else、for、while、input、int()、break、缩进规则。（已完成）
- Day 3：函数、字符串、列表、字典。（已完成，PDF：D:\pythonstudy\day3\day3_summary.pdf）
- Day 4：文件读写、路径、编码。（已完成，知识点见下）
- Day 5：Python 基础综合练习。（已完成，PDF：D:\pythonstudy\day5\day5_summary.pdf）
- Day 6：CSV 文件、pandas 数据处理。（已完成，练习文件：D:\pythonstudy\day6\）
- Day 7–Day 9：matplotlib 可视化、数据分析综合。
- Day 10–Day 13：AI/大模型基础、Prompt、Embedding、RAG、API 调用。
- Day 14–Day 18：AI + 力学/CAE 小项目。
- Day 19 以后：简历、项目包装、投递和面试准备。

**当前进度（截至 2026-06-25）：** Day 1–6 全部完成，下一步 **Day 7**（matplotlib 数据可视化）。

**Day 6 知识点：** CSV = 逗号分隔的纯文本表格；pandas 核心：DataFrame（表格）、Series（一列）；`pd.DataFrame(dict)` 创建表格；`df.to_csv()`保存、`pd.read_csv()`读取；`df["列名"]`取列、`df[条件]`筛行、`df.loc[条件,"列名"]`行列同时筛；布尔索引（条件返回 True/False，df[True/False] 只留 True 的行）；`df["列名"].mean()`均值；`df.sort_values("列名", ascending=False)`排序；`df["新列"]=表达式`新增列；`df.describe()`一行出全部统计；f-string 里嵌套引号要换成单引号；`encoding="utf-8-sig"` 防止 Excel 中文乱码。练习文件 D:\pythonstudy\day6\。

**Day 4 知识点：** open() 三件事（建通道/读写/关闭）；with 自动关文件；三种模式 r（只读，不存在报错）/w（清空重写）/a（末尾追加）；读取 read()全部、readlines()返回列表、for line in f 逐行省内存；相对路径 vs 绝对路径，r"..." 让 \ 不被转义；strip()去首尾空白、print(x,end='')不换行、f-string f"{值}"、len()拿个数；for 循环核心：容器决定怎么切（列表→元素、字典→键、文件→按\n分行），变量名随便取。练习文件 D:\pythonstudy\day4\day4practice.py。

**Day 5 知识点：** 三个综合练习（学生成绩管理 day5.py、日记本 diary.py、猜数字游戏 guess.py）；try...except 错误处理（防崩溃）；datetime.now().strftime() 获取时间戳；random.randint(a,b) 随机数；文件追加模式 "a"；scores[name]=score 字典添加/修改；for name,score in scores.items() 遍历字典拿键值；split(",") 切字符串返回列表；strip() 去换行符（不然 int("85\n") 报错）；{avg:.2f} 浮点数保留 2 位小数；方法必须加 ()（items()、now()）；print(line,end="") 防止多打换行；from datetime import datetime 导入模块类似 C 的 #include。练习文件 D:\pythonstudy\day5\。

---

## 环境与报错排查

**VS Code / 运行提醒：**
- 写完代码先 Ctrl+S 保存，再到终端运行；文件名旁有小圆点 = 没保存。
- Python 文件后缀必须 .py；运行时 PowerShell 当前目录里必须有该文件。
- `dir` 看文件、`pwd` 看目录、`cd 路径` 进文件夹。
- 右下角若显示 Spaces: 2，改成 Spaces: 4；Python 统一 4 空格缩进。

**快捷键：** Ctrl+` 开关终端、Ctrl+S 保存、Ctrl+/ 注释、Ctrl+F 搜索、Ctrl+P 打开文件、Alt+Shift+F 格式化。

**常见报错：**
- `can't open file`：检查当前目录和文件名。
- `IndentationError`：缩进多了/少了/混用。
- `SyntaxError`：括号、冒号、引号漏了。
- `NameError`：变量名拼错或没赋值。
- `KeyError`：字典必须用键访问（`d["苹果"]` 对，`d[0]` 错），遍历用 `for key in d`。
- `TypeError: write() argument must be str`：readlines() 返回列表，write() 只收字符串，要 for 循环逐行写或 "".join()。

**VS Code 技巧 PDF：** D:\pythonstudy\vscode技巧\vscode_tips.pdf

---

## Git / GitHub（已学完）

- 仓库：https://github.com/316633016wz-ux/python-study.git
- 更新代码三步：`git add .` → `git commit -m "说明"` → `git push`（注意 add 和 . 之间有空格）。
- push 过 ≠ 新文件自动上传；每次有改动都要重新走三步。
- 国内连不上配代理：`git config --global http.proxy http://127.0.0.1:7890`

---

## PDF 生成方法（重要）

weasyprint / xhtml2pdf 在用户 Python 3.8 环境下都失败。改用 Windows 自带 Edge 无头模式：

```
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless --disable-gpu --print-to-pdf="输出.pdf" "输入.html"
```

流程：先写带内联 CSS 的 HTML，再用上面命令转 PDF。用户要 PDF 时直接帮他生成，不让他装库。

**已生成的 PDF：** day3_summary.pdf、github学习/github_summary.pdf、vscode技巧/vscode_tips.pdf

---

## 常见指令

用户可能直接说"开始 Day X""继续""帮我排查报错""帮我总结成 PDF"——按本文件计划继续带学。每天开始前用户不用准备，直接说"开始 Day X"，我自动读本文件 + 当天 .py 文件从上次停的地方继续。