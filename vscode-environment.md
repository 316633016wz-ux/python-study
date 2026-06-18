---
name: vscode-environment
description: 用户的 VS Code/PowerShell 操作习惯提醒与常见 Python 报错排查清单
metadata: 
  node_type: memory
  type: reference
  originSessionId: bdaeac48-9351-47e8-8741-cac3a9827ec0
---

用户（见 [[user-profile]]）在 VS Code + PowerShell（Windows）里学 Python，教学中需照顾以下点。

**VS Code / 保存运行提醒：**
- 写完代码先 Ctrl + S 保存，再到终端运行。
- 文件名旁有小圆点 = 还没保存。
- Python 文件后缀必须 `.py`（如 day3.py）。
- 运行文件时，PowerShell 当前目录里必须有该文件。
- `dir` 查看当前文件夹文件；`pwd` 查看当前目录；`cd 路径` 进入文件夹。
- 右下角若显示 Spaces: 2，提醒改成 Spaces: 4；Python 统一用 4 个空格缩进。

**VS Code 快捷键：**
- Ctrl + ` 开关终端；Ctrl + S 保存；Ctrl + / 注释当前行。
- Ctrl + F 搜索；Ctrl + P 快速打开文件；Alt + Shift + F 格式化代码。

**常见报错优先排查方向：**
- `can't open file`：检查当前目录和文件名。
- `IndentationError`：检查缩进是否多了/少了/混用。
- `SyntaxError`：检查括号、冒号、引号有没有漏。
- `NameError`：检查变量名是否拼错，或前面没赋值。

排查时遵守 [[teaching-style]]：指导改哪一行，不直接重写整个文件。
