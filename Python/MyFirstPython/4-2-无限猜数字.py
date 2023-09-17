# 获取范围在1-100的随机数
import random
num = random.randint(1, 100)
# print(f"{num}") # 此句显示随机数的确切数字

# 猜测次数的计数器
count = 0

# 设置布尔类型来标志循环是否继续
flag = True

while flag:
    guess_num = int(input("请输入你猜的数字"))
    if guess_num == num:
        print("猜中了")
        flag = False # 把标志设置为False就终止循环
    else:
        if guess_num > num: # 提示猜大了还是小了
            print("大了")
        else:
            print("小了")
    count += 1
print(f"你一共猜了{count}次") # 最后显示猜了多少次