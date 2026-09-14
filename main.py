import sys
import os

file_path = "number.txt"

if os.path.getsize(file_path) == 0:
    Initial = 0
if os.path.getsize(file_path) > 0:
    if os.path.exists("number.txt"):
        with open("number.txt", "r") as f:
            Initial = int(f.read())

while True:

    user_input = input("输入增加或者减少的金额(输入空格停止循环)： ").strip()

    if not user_input:

        break

    user_input = int(user_input)

    Initial = user_input + Initial

    print(f"现在的金额有{Initial}")

with open("number.txt", "w") as f:
    f.write(str(Initial)) # 把数字转成字符串写入文件

print(f"现在的总金额有{Initial}")





