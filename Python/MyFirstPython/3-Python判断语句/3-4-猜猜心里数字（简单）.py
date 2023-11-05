# 这里修改心里想的数字
num = 10

# 发出提问
if int(input("请输入第一次猜想的数字：")) == num:
    print("恭喜你，第一次就猜对了！")
elif int(input("不对，再猜一次：")) == num:
    print("猜对了！")
elif int(input("不对，再猜最后一次：")) == num:
    print("恭喜，最后一次机会，你猜对了！")
else:
    print(f"Sorry，全部猜错啦，我想的是：{num}")