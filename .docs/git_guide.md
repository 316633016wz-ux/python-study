# Git / GitHub 操作指南

## 仓库信息

- 仓库地址：https://github.com/316633016wz-ux/python-study.git
- 用户名：316633016wz-ux

## 基本操作三步走

每次有改动都要走这三步：

```bash
git add .                           # 添加所有更改到暂存区（注意 add 和 . 之间有空格）
git commit -m "完成DayX学习：简要说明"   # 提交更改并写说明
git push                            # 推送到 GitHub
```

**重要：** push 过一次 ≠ 新文件自动上传；每次有改动都要重新走三步。

## 国内网络问题

如果 `git push` 连不上 GitHub，配置代理：

```bash
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
```

## 常用命令

```bash
git status              # 查看当前状态（哪些文件改了、暂存了）
git log                 # 查看提交历史
git diff                # 查看未暂存的改动
git pull                # 从远程拉取最新代码
```

## commit message 规范

建议格式：`完成DayX学习：简要说明`

示例：
- `完成Day7学习：MySQL数据库基础，掌握增删改查和统计函数`
- `更新CLAUDE.md：添加Day7知识点总结和进度`
- `优化CLAUDE.md：明确每天结束标准流程和检查清单`
