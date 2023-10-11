# 取中间一段
# 对列表list序列进行切片，从1开始，4结束，步长1
list = [0, 1, 2, 3, 4, 5, 6]
result1 = list[1:4] # 步长默认是1，可以省略
print(f"原列表序列{list}被切片后得到的是：{result1}")

# 取完整序列
# 对元组tuple序列进行切片，从头开始，到最后结束，步长1
tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = tuple[:]
print(f"原元组序列{tuple}被切片后得到的是：{result2}")

# 隔一个取
# 对字符串str序列进行切片，从头开始，到最后结尾，步长2
str = "abcdefghijk"
result3 = str[::2]
print(f"原字符串序列{str}被切片后得到的是：{result3}")

# 取倒序
# 对字符串str序列进行切片，从头开始，到最后结尾，步长-1（即倒序）
str = "abcdefghijk"
result4 = str[::-1]
print(f"原字符串序列{str}被切片后得到的是：{result4}")

# 倒序且部分
# 对列表list序列进行切片，从3开始，1结束，步长-1
list = [0, 1, 2, 3, 4, 5, 6]
result5 = list[3:1:-1] # 步长默认是1，可以省略
print(f"原列表序列{list}被切片后得到的是：{result5}")

# 倒序且隔几个取
# 对元组tuple序列进行切片，从头开始，到最后结束，步长-2
tuple = (0, 1, 2, 3, 4, 5, 6)
result6 = tuple[::-2]
print(f"原元组序列{tuple}被切片后得到的是：{result6}")