# 列表list的定义(元素内容不受限)，且用变量接收
name_list = [True, 666, 'python']
print(name_list)
print(type(name_list))

# 嵌套的列表
my_list = [[1,2],3 ]
print(my_list)
print(type(my_list))

# 空列表
empty_list = []
empty_list = list()

# 下标索引取出元素
my_list = ['Apple', 'Billy', 'Owen']
print(my_list[0])
print(my_list[1])
print(my_list[2])
# 索引超出范围程序会报错

# 倒序取值
my_list = ['Apple', 'Billy', 'Owen']
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

# 嵌套的情况
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[0][0]) # 1（第1个元素的第一个）
print(my_list[1][0]) # 4（第2个元素的第一个）
print(my_list[1][1]) # 5