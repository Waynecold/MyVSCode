"""

要求：
1、显示主菜单，启动前要求输入用户姓名
2、查询余额，之后返回主菜单
3、实现存、取效果，显示余额，后返回主菜单

提示：
name记录用户姓名
money记录余额（默认5000000）

实现功能的函数：
查询余额函数
存款函数
取款函数
主菜单函数

用户选择推出或输入错误，否则程序一直循环运行

"""

"""

自己版本(修改后)：此程序bug，输入存入或取出的金额时不能是数字以外的字符。

"""

# 全局变量
name = "wayne"
money = 5000000

# 查询余额函数
def query(show_header):

    # 添加参数show_header，若为真，输出标题
    if show_header:
        print("---------------余额查询---------------")

    print(f"{name}，你好，你的余额剩余：{money}")
    # 原来如果调用的是函数外的实参，是不用放在函数头的

# 存款函数
def deposit(user_deposit):
    global money  # 局部变量转为全局变量的money
    money += user_deposit
    print("----------------存款-----------------")
    print(f"{name}，你好，你存款{user_deposit}成功")

    # 调用查询函数
    query(False)

# 取款函数
def withdraw(user_withdraw):
    global money
    money -= user_withdraw
    print("----------------取款-----------------")
    print(f"{name}，你好，你取款{user_withdraw}成功")
    query(False)

# 主菜单函数
def menu():
    print()
    print("---------------主菜单----------------")
    print(f"{name}，你好，欢迎使用ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款     \t[输入2]")
    print("取款     \t[输入3]")
    print("退出     \t[输入4]")
    return input("请出入您的选择：")

# 主程序
def main():
    while True:
        choice = menu()
        if choice == "1":
            query(True)
            continue
        elif choice == "2":
            user_deposit = input("请输入你要存入的金额：")
            deposit(user_deposit)
            continue
        elif choice == "3":
            user_withdraw = float(input("请输入你要取出的金额："))

            # 判断余额是否足够
            if money >= user_withdraw:
                withdraw(user_withdraw)
                continue
            else:
                print(f"余额不足以取出{user_withdraw}，请返回主菜单重新输入。")
        elif choice == "4":
            print("欢迎下次使用。")
            break
        else:
            print("输入错误。请重新选择。")

# 验证姓名，错误循环验证，或q退出
keyboard_input = input("欢迎使用ATM，请输入名字（q退出）：")
while keyboard_input != "q":
    if keyboard_input == name:
        print("正确")
        main()
        break
    else:
        keyboard_input = input("姓名输入错误，请重新输入名字（q退出）：")    
print("感谢使用")


"""

教程版本

"""

# # 定义全局变量
# money = 5000000
# name = None

# # 要求输入姓名
# name = input("请输入姓名：")

# # 查询函数
# def query(show_header): #添加参数show_header，若为真，输出标题
#     if show_header:
#         print("---------------余额查询---------------")
#     print(f"{name}，你好，你的余额剩余：{money}")

# # 存款函数
# def saving(num):
#     global money #局部变量定义为全局
#     money += num
#     print("----------------存款-----------------")
#     print(f"{name}，你好，你存款{num}成功")

#     # 调用查询函数
#     query(False)

# # 取款函数
# def get_money(num):
#     global money #局部变量定义为全局
#     money -= num
#     print("----------------取款-----------------")
#     print(f"{name}，你好，你取款{num}成功")

#     # 调用查询函数
#     query(False)

# # 主菜单函数
# def main():
#     print("---------------主菜单----------------")
#     print(f"{name}，你好，欢迎使用ATM。请选择操作：")
#     print("查询余额\t[输入1]")
#     print("存款\t\t[输入2]")
#     print("取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     return input("请出入您的选择：")

# # 设置无限循环
# while True:
#     keyboard_input = main()
#     if keyboard_input == "1":
#         query(True) # True即是输出标题头
#         continue # 通过continue继续下一次循环
#     elif keyboard_input == "2":
#         num = int(input("请输入你要存入的金额："))
#         saving(num)
#         continue
#     elif keyboard_input == "3":
#         num = int(input("请输入你要取出的金额："))
#         get_money(num)
#         continue
#     else:
#         print("程序退出了")
#         break
