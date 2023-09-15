# 定义变量储存布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}，类型是：{type(bool_1)}")
print(f"bool_1变量的内容是：{bool_2}，类型是：{type(bool_2)}")

# 比较运算符的结果
# ==，!=，>，<，>=，<=
num1 = 10
num2 = 10
num3 = 15
name1 = "wayne"
name2 = "wade"
print(f"10 == 10的结果是：{num1 == num2}")
print(f"10 != 15的结果是：{num1 != num3}")
# ==运算符还可以比较字符串
print(f"wayne == wade的结果是：{name1 == name2}")
print(f"10 > 15的结果是：{num1 > num3}")
print(f"10 < 15的结果是：{num1 < num3}")
print(f"10 >= 10的结果是：{num2 > num1}")
print(f"10 <= 15的结果是：{num2 < num3}")
