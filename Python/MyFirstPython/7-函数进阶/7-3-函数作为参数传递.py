# 定义函数，接收另一个函数作为传入参数
def test_func_1(compute):
    result = compute(1, 2) # compute是函数
    print(f"1、compute参数的类型是：{type(compute)}")
    print(f"计算结果是：{result}")

# 定义一个函数，准备作为参数传入到另一个函数
def compute(x, y):
    return x + y

# 调用，并传入函数
test_func_1(compute)

# 使用lambda定义使用匿名函数
def test_func_2(compute):
    result = compute(1, 2)
    print(f"2、结果是：{result}")

test_func_2(lambda x, y: x + y)