# 定义一个叫add的函数，实现功能：接受两个数字，得到相加的结果
def add(x, y):
    result = x + y
    print(f"{x} + {y}的计算结果是：{result}")

# 调用函数
add(1, 2)
add(2, 5)

# 带有说明文档的函数
def add_v2(x, y):
    """
    add函数接收2个参数，进行相加的功能
    :param x: 形参x表示相加的其中一个数字
    :param y: 形参y表示相加的另一个数字
    :return: 返回值是2个数相加的结果
    """
    result = x + y
    print(f"2数相加的结果是{result}")
    return result

add_v2(2, 2) # 鼠标放在函数上即可看到说明文档