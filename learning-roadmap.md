---
name: learning-roadmap
description: Python/AI/CAE 学习的每日路线计划与当前进度（截至 2026-06-22，Day 1–3 完成，下一步 Day 4）
metadata: 
  node_type: memory
  type: project
  originSessionId: bdaeac48-9351-47e8-8741-cac3a9827ec0
---

用户是力学专业学生（见 [[user-profile]]），按以下每日计划学习，要求遵守 [[teaching-style]] 的教学方式。

**学习路线：**
- Day 1：PowerShell 基础、创建/运行 Python 文件、print、变量、简单计算。（已完成）
- Day 2：if/elif/else、for、while、input、int()、break、缩进规则。（已完成）
- Day 3：函数、字符串、列表、字典。（已完成，总结 PDF 在 D:\pythonstudy\day3\day3_summary.pdf）
- Day 4：文件读写、路径、编码。
- Day 5：Python 基础综合练习。
- Day 6–Day 9：CSV、pandas、matplotlib、数据分析。
- Day 10–Day 13：AI/大模型基础、Prompt、Embedding、RAG、API 调用。
- Day 14–Day 18：AI + 力学/CAE 小项目。
- Day 19 以后：简历、项目包装、投递和面试准备。

**当前进度（截至 2026-06-22）：** Day 1–3 全部完成，下一步 Day 4（文件读写、路径、编码）。Git/GitHub 已学完并推送成功，相关 PDF 已生成。

**Git/GitHub 学习进度（已全部完成）：**
- git init / .gitignore / add / commit / remote / branch -M main 全部学过
- git push -u origin main 推送成功（Personal Access Token 认证；国内连不上时配代理：git config --global http.proxy http://127.0.0.1:7890）
- 仓库地址：https://github.com/316633016wz-ux/python-study.git
- 以后更新代码三步：git add . → git commit -m "说明" → git push（注意 add 和 . 之间有空格，git add. 是错的）
- 易混点：push 过 ≠ 以后新建文件自动上传；每次有新文件/改动都要重新走三步

**PDF 生成方法（重要）：** weasyprint / xhtml2pdf 在用户 Python 3.8 环境下都失败（缺 GTK / md5 参数不兼容）。改用 Windows 自带 Edge 无头模式，稳定可用：
`"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless --disable-gpu --print-to-pdf="输出.pdf" "输入.html"`
流程：先写带内联 CSS 的 HTML，再用上面命令转 PDF。用户要 PDF 时直接帮他生成，不让他自己装库。

**已生成的 PDF：**
- D:\pythonstudy\day3\day3_summary.pdf（Day 3 总结）
- D:\pythonstudy\github学习\github_summary.pdf（GitHub 学习总结）
- D:\pythonstudy\vscode技巧\vscode_tips.pdf（VS Code 技巧）

**上下文提醒（重要）：** 主动留意上下文使用情况。当对话变长、上下文快用满时，要主动提醒用户"上下文快满了，建议先保存进度到记忆文件再 /compact"，不要等用户自己发现或等到信息丢失。

**常见指令：** 用户可能直接说"开始 Day X""继续""帮我排查报错""帮我总结成 PDF"——看到这些按本计划和背景继续带学。每天开始前用户不用做任何准备，直接说"开始 Day X"即可，我会自动读记忆文件 + 当天的 .py 文件从上次停的地方继续。
