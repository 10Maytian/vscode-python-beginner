print("=== Step 2：判断系统 ===")

name = input("请输入你的名字：")
age = int(input("请输入你的年龄："))

print("----- 分析中 -----")

if age >= 18:
    print("你好", name)
    print("你是成年人")
else:
    print("你好", name)
    print("你还是未成年")

print("系统运行结束 ✅")
