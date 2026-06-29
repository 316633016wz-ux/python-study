# PDF 生成方法

## 背景

weasyprint / xhtml2pdf 在用户 Python 3.8 环境下都失败。改用 Windows 自带 Edge 无头模式。

## 生成方法

### 步骤1：创建 HTML 文件

用 Write 工具创建带内联 CSS 的 HTML 文件，例如 `day7_summary.html`。

**要求：**
- 所有 CSS 必须内联在 `<style>` 标签里（不能用外部 CSS 文件）
- 使用中文字体：`font-family: 'Microsoft YaHei', Arial, sans-serif;`
- 内容包含：概念讲解、命令用法（完整语法和参数说明）、示例代码、练习总结、常见错误

### 步骤2：转换为 PDF

使用 Edge 无头模式：

```bash
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless --disable-gpu --print-to-pdf="d:\pythonstudy\dayX\dayX_summary.pdf" "d:\pythonstudy\dayX\dayX_summary.html"
```

**参数说明：**
- `--headless`：无窗口模式
- `--disable-gpu`：禁用 GPU 加速
- `--print-to-pdf="路径"`：输出 PDF 的完整路径
- 最后一个参数：HTML 文件的完整路径

## 已生成的 PDF

- day3_summary.pdf
- day5_summary.pdf
- day6_summary.pdf
- day7_summary.pdf
- github学习/github_summary.pdf
- vscode技巧/vscode_tips.pdf

## 注意事项

- 用户要 PDF 时直接生成，不要让用户自己装库
- HTML 和 PDF 都放在对应的 `dayX` 文件夹里
- 文件命名规范：`dayX_summary.html` 和 `dayX_summary.pdf`
