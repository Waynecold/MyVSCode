#　浮点数转整数（会丢失精度）
num_int = int(3.14)
print(type(num_int), num_int)

# 整数转浮点数
num_float = float(10)
print(type(num_float), num_float)

# 数字转字符串
int_str = str(88)
print(type(int_str), int_str)

float_str = str(3.14)
print(type(float_str), float_str)

# 字符串转数字（仅全是数字的字符串）
num1 = int("11")
print(type(num1), num1)

num2 = float("123.456")
print(type(num2), num2)

# 对于非数字字符，不能转换成数字