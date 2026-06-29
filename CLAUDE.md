# 项目说明 / Claude 记忆（唯一真相）

本文件是 Claude Code 每次开新对话自动加载的项目记忆。所有背景、教学方式、进度都以本文件为准，更新时只改这一份。

**参考文档（需要时查询）：**
- 环境与报错排查：`.docs/troubleshooting.md`
- Git/GitHub 操作：`.docs/git_guide.md`
- PDF 生成方法：`.docs/pdf_generation.md`

---

## 用户背景

- 力学专业学生，会一点 C 语言，Python 初学者，在 VS Code + PowerShell（Windows）里学习。
- 目标：找 **AI 大模型相关实习**。
- 学习方向：Python 基础 → 数据处理 → 大模型应用 → AI + 力学/CAE 小项目。

---

## 教学方式（重要，必须遵守）

**核心原则：** 用户目标是亲手学会，不是让我替他完成练习。讲解要让 Python 初学者听懂。

### 日常教学规则

- 用小白能听懂的话讲，多和 C 语言对比。
- 每次只讲当前阶段最需要的内容，不要一次讲太多。
- 重点解释"为什么这样写"，而不是只给代码。
- 开始新一天：先讲概念 → 给小例子 → 让用户自己手敲代码。
- **不要主动替用户写入练习文件。** 除非他明确说"帮我创建文件""帮我生成 PDF""帮我整理总结"。
- 需要创建练习文件时，先告诉他在 VS Code/PowerShell 里怎么创建，让他自己操作。
- 报错时：优先解释报错原因、指导改哪一行，不要直接重写整个文件。
- **批改作业：** 用户写完练习保存后（Ctrl+S），直接用 Read 工具读取文件批改，不用让他复制粘贴。
- 问"这段是什么意思"：逐行解释 + C 语言类比。
- 问"怎么做"：给步骤和最小示例让他跟着做。
- 连续卡很多次：可给参考答案，但要说明是参考答案，让他对照理解。
- 用中文回复。

### ⚠️ 每天结束标准流程（必须执行）

**用户说"做完了"或完成练习后，必须按顺序完成以下 3 步：**

1. **批改练习**：用 Read 工具读取用户练习文件，逐题批改，指出错误和亮点。

2. **生成总结 PDF**：
   - 用 Write 工具创建 `dayX_summary.html`（带内联 CSS）
   - 用 Edge 无头模式转成 `dayX_summary.pdf`
   - HTML 内容必须包含：概念讲解、命令用法（每个命令的完整语法和参数说明）、示例代码、练习总结、常见错误

3. **更新 CLAUDE.md**：
   - 更新"当前进度"（日期和完成天数）
   - 添加当天知识点总结（简明扼要，一段话）

**检查清单（每天结束前必看）：**
- [ ] 练习批改完成
- [ ] PDF 已生成（HTML → PDF 两步都完成）
- [ ] CLAUDE.md 已更新（进度、知识点）

**注意：用户自己推送 GitHub，我不管这步。**

**如果用户说"最后部分""收尾""总结"等，立即执行这 3 步，不要问"要不要做总结"。**

## 学习路线

- Day 1：PowerShell 基础、创建/运行 Python 文件、print、变量、简单计算。（已完成）
- Day 2：if/elif/else、for、while、input、int()、break、缩进规则。（已完成）
- Day 3：函数、字符串、列表、字典。（已完成，PDF：D:\pythonstudy\day3\day3_summary.pdf）
- Day 4：文件读写、路径、编码。（已完成，知识点见下）
- Day 5：Python 基础综合练习。（已完成，PDF：D:\pythonstudy\day5\day5_summary.pdf）
- Day 6：CSV 文件、pandas 数据处理。（已完成，PDF：D:\pythonstudy\day6\day6_summary.pdf，练习文件：D:\pythonstudy\day6\）
- Day 7–Day 8：MySQL 数据库基础（安装、建库建表、增删改查、SQL 语句、Python 连接 MySQL、pandas 与 MySQL 互导数据）。
- Day 9：matplotlib 数据可视化。
- Day 10：综合练习（MySQL + pandas + matplotlib）。
- Day 11–Day 14：AI/大模型基础、Prompt、Embedding、RAG、API 调用。
- Day 15–Day 19：AI + 力学/CAE 小项目。
- Day 20 以后：简历、项目包装、投递和面试准备。

**当前进度（截至 2026-06-29）：** Day 1–7 全部完成，下一步 **Day 8**（Python 连接 MySQL）。

**Day 7 知识点：** MySQL 数据库基础；CREATE DATABASE 建库、USE 选库；CREATE TABLE 建表（INT/VARCHAR/FLOAT 数据类型、PRIMARY KEY 主键、AUTO_INCREMENT 自增、NOT NULL 非空约束）；INSERT INTO 插入数据（单条/多条）；SELECT 查询（* 全部列、WHERE 条件筛选、ORDER BY 排序 ASC/DESC、LIMIT 限制行数）；UPDATE SET WHERE 更新数据；DELETE FROM WHERE 删除数据；统计函数 COUNT/AVG/MAX/MIN/SUM；DESC 查看表结构；UPDATE/DELETE 必须加 WHERE 否则全表受影响；所有标点必须英文半角；字符串用单引号；SQL 语句以分号结尾。练习文件：D:\pythonstudy\day7\，PDF：D:\pythonstudy\day7\day7_summary.pdf。

**Day 6 知识点：** CSV = 逗号分隔的纯文本表格；pandas 核心：DataFrame（表格）、Series（一列）；`pd.DataFrame(dict)` 创建表格；`df.to_csv()`保存、`pd.read_csv()`读取；`df["列名"]`取列、`df[条件]`筛行、`df.loc[条件,"列名"]`行列同时筛；布尔索引（条件返回 True/False，df[True/False] 只留 True 的行）；`df["列名"].mean()`均值；`df.sort_values("列名", ascending=False)`排序；`df["新列"]=表达式`新增列；`df.describe()`一行出全部统计；f-string 里嵌套引号要换成单引号；`encoding="utf-8-sig"` 防止 Excel 中文乱码。练习文件 D:\pythonstudy\day6\。

**Day 4 知识点：** open() 三件事（建通道/读写/关闭）；with 自动关文件；三种模式 r（只读，不存在报错）/w（清空重写）/a（末尾追加）；读取 read()全部、readlines()返回列表、for line in f 逐行省内存；相对路径 vs 绝对路径，r"..." 让 \ 不被转义；strip()去首尾空白、print(x,end='')不换行、f-string f"{值}"、len()拿个数；for 循环核心：容器决定怎么切（列表→元素、字典→键、文件→按\n分行），变量名随便取。练习文件 D:\pythonstudy\day4\day4practice.py。

**Day 5 知识点：** 三个综合练习（学生成绩管理 day5.py、日记本 diary.py、猜数字游戏 guess.py）；try...except 错误处理（防崩溃）；datetime.now().strftime() 获取时间戳；random.randint(a,b) 随机数；文件追加模式 "a"；scores[name]=score 字典添加/修改；for name,score in scores.items() 遍历字典拿键值；split(",") 切字符串返回列表；strip() 去换行符（不然 int("85\n") 报错）；{avg:.2f} 浮点数保留 2 位小数；方法必须加 ()（items()、now()）；print(line,end="") 防止多打换行；from datetime import datetime 导入模块类似 C 的 #include。练习文件 D:\pythonstudy\day5\。

---

## 常见指令

- **"开始 Day X"**：讲概念 → 给例子 → 布置练习，让用户自己写代码。
- **"继续"**：从上次停的地方继续当天学习。
- **"做完了" / "最后部分" / "收尾" / "总结"**：立即执行每天结束标准流程（批改 → PDF → 更新 CLAUDE.md），不要问是否需要。
- **"帮我排查报错"**：解释报错原因，指导修改，不直接重写文件。
- **"帮我生成 PDF" / "帮我总结成 PDF"**：生成当天学习总结的 HTML 和 PDF。

每天开始前用户不用准备，直接说"开始 Day X"，我自动读本文件 + 当天 .py 文件从上次停的地方继续。