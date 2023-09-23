'''
1、len()是Python内置的函数，用于计算字符串的长度
'''
name = "wayne"
length = len(name)
print(length)

'''
2、创建计算字符串的长度的自定义函数
'''
# 创建函数
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度为{count}。")

# 重复调用函数
name2 = "waynecold"
my_len(name)
my_len(name2)
