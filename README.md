# claude-camp-w1--practice
Claude AI 训练营第一周 Python 练习
# Claude AI 训练营 Week 1 Python 练习

2026 年 5 月 4 日 - 5 月 9 日，我在小麦校长的 Claude AI 训练营完成的第一周作业。

## 学习内容

- 吴恩达 AI Python for Beginners — Course 1（已完成）
- 哈佛 CS50P Week 0（已完成）
- Python 环境搭建：VS Code、Python 3.12、Git、GitHub

## 练习清单

| 文件 | 题目 | 涉及知识点 |
|---|---|---|
| `01_temperature_converter.py` | 温度转换器 — 摄氏度与华氏度互换 | 函数、`input()`、`float()`、`if/else` |
| `02_greeting.py` | 个性化问候语 | `input()`、`int()`、f-string、简单算术 |
| `03_tip_calculator.py` | 小费计算器 | `float()` 嵌套调用、百分比计算、`:.2f` 格式化 |
| `04_password_generator.py` | 随机密码生成器 | `import random`、`random.choices`、`''.join` |
| `05_bmi_calculator.py` | BMI 计算器 | 幂运算 `**`、`if/elif/else` 多分支 |

## 怎么运行

```bash
python3 01_temperature_converter.py
```

把 `01_...` 换成想跑的文件即可。

## 一点心得

第一周最大的收获不是写多漂亮的代码，而是走通了 **写代码 → 终端运行 → git 提交 → 推到 GitHub** 整套流程。也踩了一些经典的坑：
- `print(...)` 调用 vs `print = ...` 赋值的区别
- `float(input("..."))` 的引号位置 — 引号只包提示文字
- 变量名不能带 `%`、`$` 等特殊字符
- shell commit message 必须用双引号包起来，否则 `&` 会被当成后台运行

—— Elong, 2026.05.06
