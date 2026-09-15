import sys
import os

file_path = "number.txt"

initial = 0
Income = 0
expend = 0

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if content:  # 确保读出来的字符串不为空
            initial = int(content)
            expend = int(content)
            Income = int(content)

while True:

    user_input = input("输入增加或者减少的金额(输入空格停止循环)： ").strip()

    if not user_input:

        break

    try:
        amount = int(user_input)
    except ValueError:
        print("输入无效，请输入合法的整数数字！")
        continue


    if amount > 0:
        Income += amount

    if amount < 0:
        expend += amount
        expend = abs(expend)

    initial= amount+ initial

    print(f"现在的金额有{initial}")

with open("number.txt", "w") as f:
    f.write(str(initial))# 把数字转成字符串写入文件
    f.write(str(expend))
    f.write(str(Income))

print(f"现在的总金额有{initial}")
print(f"现在的总支出有{expend}")
print(f"现在的总收入有{Income}")





