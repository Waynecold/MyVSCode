# 打开文件
f = open("D:/Documents/MyVSCode/Python/MyFirstPython/8-文件操作/8-0-Python的简介.txt", "r", encoding="UTF-8")
print(f"f的类型是{type(f)}")

# # 读取文件
# ## .read(num)读取指定字符数？的内容
# print(f"读取42个字符的结果：{f.read(42)}")
# print(f"读取全部字符的结果：{f.read()}") # 第二次调用read()时会接着上次结束的位置开始

## readlines()读取全部行，封装到列表中
# lines = f.readlines()
# print(f"lines对象的类型：{type(lines)}") 
# print(f"lines对象的内容是：{lines}")

# ## readline()读取一行的内容，以"\n"为标记
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# line4 = f.readline()
# print(f"第一行的数据是：{line1}")
# print(f"第二行的数据是：{line2}")
# print(f"第三行的数据是：{line3}")
# print(f"第四行的数据是：{line4}")

# ## for循环读取文件行
# for line in f:
#     print(f"每一行的数据是：{line}")

# 关闭文件
f.close()

## with open() as f语法实现自动close，避免遗忘
with open("D:/Documents/MyVSCode/Python/MyFirstPython/8-文件操作/8-0-Python的简介.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行的数据是：{line}")
