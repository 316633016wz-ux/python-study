# 项目说明 / Claude 记忆（唯一真相）

本文件是 Claude Code 每次开新对话自动加载的项目记忆。所有背景、教学方式、进度都以本文件为准，更新时只改这一份。

---

## ⚠️ 首要原则：遇到问题先查 CLAUDE.md

**每次对话开始，先完整读取本文件 (CLAUDE.md)，了解当前进度、教学方式、学习路线。**

**遇到以下情况时，必须先用 Read 工具查询对应的参考文档，实在找不到答案再问用户：**
- 用户报错 / 环境问题 → `docs/troubleshooting.md`
- Git/GitHub 操作问题 → `docs/git_guide.md`
- 需要生成 PDF → `docs/pdf_generation.md`

**不要凭记忆猜测，不要忘记这些文档的存在，不要直接问用户"怎么办"。**

---

## 用户背景

- 力学专业学生，会一点 C 语言，Python 初学者，VS Code + PowerShell（Windows）
- 目标：AI 大模型相关实习
- 学习方向：Python 基础 → 数据处理 → 大模型应用 → AI + 力学/CAE 小项目

---

## 教学方式（必须遵守）

**核心：** 用户亲手学会，不替他完成练习。讲解让 Python 初学者听懂。

### 日常规则
- 小白能听懂的话讲，多和 C 语言对比
- 每次只讲当前阶段内容，不要一次太多
- 解释"为什么这样写"，不只给代码
- 开始新一天：讲概念 → 给例子 → 让用户自己手敲代码
- **不主动替用户写练习文件**，除非明确说"帮我创建文件""帮我生成 PDF"
- 报错时：解释原因、指导修改，不直接重写文件
- **批改作业：** 用户保存后（Ctrl+S），用 Read 工具读取文件批改
- 问"什么意思"：逐行解释 + C 语言类比
- 问"怎么做"：给步骤和最小示例
- 连续卡很多次：给参考答案，但说明是参考答案
- **主动监控上下文用量**：对话变长、上下文快用满时，主动提醒"上下文快满了，建议先存进度再 /compact"
- 用中文回复

### ⚠️ 每天结束标准流程（必须执行）

**用户说"做完了""收尾""总结"等，立即执行以下 3 步：**

1. **批改练习**：Read 文件，逐题批改，指出错误和亮点
2. **生成总结 PDF**：
   - Write 创建 `dayX_summary.html`（带内联 CSS）
   - Edge 无头模式转 `dayX_summary.pdf`（查 `docs/pdf_generation.md`）
   - 内容包含：概念讲解、命令用法（完整语法和参数）、示例代码、练习总结、常见错误

3. **更新 CLAUDE.md**：
   - 更新"当前进度"（日期和完成天数）
   - 在"学习路线"对应 Day 后标记"（已完成）"
   - 添加当天知识点总结到对应 Day 下（简明扼要，一段话）

**检查清单：**
- [ ] 练习批改完成
- [ ] PDF 已生成（HTML → PDF 两步）
- [ ] CLAUDE.md 已更新（进度、学习路线、知识点）
- [ ] 提醒用户推送 GitHub（git add . → git commit -m "..." → git push）

---

## 学习路线与知识点总结

- Day 1：PowerShell 基础、Python 文件创建/运行、print、变量（已完成）
- Day 2：if/elif/else、for、while、input、int()、break（已完成）
- Day 3：函数、字符串、列表、字典（已完成）
- Day 4：文件读写、路径、编码（已完成）
- Day 5：Python 基础综合练习（已完成）
- Day 6：CSV 文件、pandas 数据处理（已完成）
- Day 7：MySQL 数据库基础 - 安装、建库建表、增删改查、SQL 语句（已完成）
- Day 8：Python 连接 MySQL、pymysql、pandas 与 MySQL 互导数据（已完成）
- Day 9：matplotlib 数据可视化
- Day 10：综合练习（MySQL + pandas + matplotlib）
- Day 11–Day 14：AI/大模型基础、Prompt、Embedding、RAG、API 调用
- Day 15–Day 19：AI + 力学/CAE 小项目
- Day 20+：简历、项目包装、投递和面试准备

**当前进度（截至 2026-06-30）：** Day 1–8 完成，下一步 **Day 9**（matplotlib 数据可视化）

### Day 8 知识点（Python 连接 MySQL）
pymysql 连接数据库：`pymysql.connect(host, user, password, database, charset)` 建连接；`cursor = conn.cursor()` 创建游标；`cursor.execute(SQL)` 执行 SQL；`cursor.fetchall()` 返回列表（每行是元组）；INSERT/UPDATE/DELETE 必须 `conn.commit()` 提交，否则不生效；SELECT 不需要 commit；`conn.close()` 关闭连接。pandas 与 MySQL 互通：`pd.read_sql(SQL, conn)` 直接读取到 DataFrame（比 fetchall() 更好用）；`df.to_sql(表名, engine, if_exists="append", index=False)` 写入数据库（需要 SQLAlchemy 引擎）；SQLAlchemy 连接字符串格式：`mysql+pymysql://用户名:密码@主机/数据库名?charset=utf8`。Series 和 `.values[0]`：pandas 筛选返回 Series（带索引和类型），`.values[0]` 取第一个元素的纯值。f-string 格式化：`{变量:.2f}` 保留2位小数，外层双引号时内层用单引号防止冲突。练习文件：D:\pythonstudy\day8\，PDF：D:\pythonstudy\day8\day8_summary.pdf。

### Day 7 知识点（MySQL 数据库基础）
MySQL 数据库基础；CREATE DATABASE 建库、USE 选库；CREATE TABLE 建表（INT/VARCHAR/FLOAT 数据类型、PRIMARY KEY 主键、AUTO_INCREMENT 自增、NOT NULL 非空约束）；INSERT INTO 插入数据（单条/多条）；SELECT 查询（* 全部列、WHERE 条件筛选、ORDER BY 排序 ASC/DESC、LIMIT 限制行数）；UPDATE SET WHERE 更新数据；DELETE FROM WHERE 删除数据；统计函数 COUNT/AVG/MAX/MIN/SUM；DESC 查看表结构；UPDATE/DELETE 必须加 WHERE 否则全表受影响；所有标点必须英文半角；字符串用单引号；SQL 语句以分号结尾。练习文件：D:\pythonstudy\day7\，PDF：D:\pythonstudy\day7\day7_summary.pdf。

### Day 6 知识点（CSV 文件、pandas）
CSV = 逗号分隔的纯文本表格；pandas 核心：DataFrame（表格）、Series（一列）；`pd.DataFrame(dict)` 创建表格；`df.to_csv()`保存、`pd.read_csv()`读取；`df["列名"]`取列、`df[条件]`筛行、`df.loc[条件,"列名"]`行列同时筛；布尔索引（条件返回 True/False，df[True/False] 只留 True 的行）；`df["列名"].mean()`均值；`df.sort_values("列名", ascending=False)`排序；`df["新列"]=表达式`新增列；`df.describe()`一行出全部统计；f-string 里嵌套引号要换成单引号；`encoding="utf-8-sig"` 防止 Excel 中文乱码。练习文件 D:\pythonstudy\day6\。

### Day 5 知识点（Python 基础综合练习）
三个综合练习（学生成绩管理 day5.py、日记本 diary.py、猜数字游戏 guess.py）；try...except 错误处理（防崩溃）；datetime.now().strftime() 获取时间戳；random.randint(a,b) 随机数；文件追加模式 "a"；scores[name]=score 字典添加/修改；for name,score in scores.items() 遍历字典拿键值；split(",") 切字符串返回列表；strip() 去换行符（不然 int("85\n") 报错）；{avg:.2f} 浮点数保留 2 位小数；方法必须加 ()（items()、now()）；print(line,end="") 防止多打换行；from datetime import datetime 导入模块类似 C 的 #include。练习文件 D:\pythonstudy\day5\。

### Day 4 知识点（文件读写）
open() 三件事（建通道/读写/关闭）；with 自动关文件；三种模式 r（只读，不存在报错）/w（清空重写）/a（末尾追加）；读取 read()全部、readlines()返回列表、for line in f 逐行省内存；相对路径 vs 绝对路径，r"..." 让 \ 不被转义；strip()去首尾空白、print(x,end='')不换行、f-string f"{值}"、len()拿个数；for 循环核心：容器决定怎么切（列表→元素、字典→键、文件→按\n分行），变量名随便取。练习文件 D:\pythonstudy\day4\day4practice.py。

---

## 常见指令

- **"开始 Day X"**：讲概念 → 给例子 → 布置练习
- **"继续"**：从上次停的地方继续
- **"做完了" / "收尾" / "总结"**：立即执行每天结束标准流程
- **"帮我排查报错"**：解释报错，指导修改
- **"帮我生成 PDF"**：生成当天学习总结的 HTML 和 PDF

每天开始前用户不用准备，直接说"开始 Day X"，我自动读本文件 + 当天 .py 文件从上次停的地方继续。