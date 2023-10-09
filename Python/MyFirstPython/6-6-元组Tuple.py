# 定义元组
t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)}，内容是{t1}")
print(f"t2的类型是：{type(t2)}，内容是{t2}")
print(f"t3的类型是：{type(t3)}，内容是{t3}")

# 定义单个元素的元组（缺少逗号将变成str类型）
t4 = ("hello", )
print(f"t4的类型是：{type(t4)}，内容是{t4}")

# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是：{type(t5)}，内容是{t5}")

# 下标取特定元素，如上面的元素`6`
num = t5[1][2]
print(f"取出嵌套元组中第二个（元组）元素中的第三个元素：{num}")

# 元组的操作
## index查找下标
t6 = ("Hello", 233, "World", 233)
index = t6.index("World")
print(f"在元组t6中查找\"World\"的下标是：{index}")

## count统计
num = t6.count(233)
print(f"元组t6中统计有\"233\"的个数为：{num}")

# 元组的遍历
## while
index = 0
while index < len(t6):
    print(f"元组t6的元素分别有：{t6[index]}")
    index += 1

## for
for element in t1:
    print(f"元组t1的元素有：{element}")

# 元组的内容是不可修改的
# t1[2] = "Bye"

# 特殊情况，元组内的元素是一个列表，修改列表内的元素是可以的
t7 = (1, 2, [5, 6])
print(f"修改前t7的内容是：{t7}")
t7[2][0] = 3
t7[2][1] = 4
print(f"修改后t7的内容是：{t7}")
