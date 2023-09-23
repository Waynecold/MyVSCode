# 主动返回None的函数
def say_hi():
    print("你好呀")
    return None

result = say_hi()

# None的返回，和类型
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")

# None用于if判断
def check_age(age):
    if age > 18:
        return "通过"
    else:
        return None
    
result = check_age(16) # 结果是False

if not result: # 取反，if条件通过，执行代码
    print("未成年，禁止进入")

# None用于声明无初始值的变量
name = None
