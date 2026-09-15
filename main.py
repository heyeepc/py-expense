import sys
import os

file_path = "number.txt"

initial = 0
Income = 0
expend = 0

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if len(lines) >= 3:
            initial = int(lines[0].strip())
            expend = int(lines[1].strip())
            Income = int(lines[2].strip())

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
        expend += abs(amount)

    initial= amount+ initial

    print(f"现在的金额有{initial}")

with open("number.txt", "w") as f:
    f.write(f"{initial}\n")
    f.write(f"{expend}\n")
    f.write(f"{Income}\n")

print(f"现在的总金额有{initial}")
print(f"现在的总支出有{expend}")
print(f"现在的总收入有{Income}")





