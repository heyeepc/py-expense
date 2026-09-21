import sys
import os
import json



file_path = "number.json"


initial = 0
Income = 0
expend = 0

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:

    with open('number.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    initial = data[0]["initial"]
    Income = data[1]["Income"]
    expend = data[2]["expend"]



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

data[0]["initial"] = initial
data[1]["Income"] = Income
data[2]["expend"] = expend

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


print(f"现在的总金额有{initial}")
print(f"现在的总支出有{expend}")
print(f"现在的总收入有{Income}")





