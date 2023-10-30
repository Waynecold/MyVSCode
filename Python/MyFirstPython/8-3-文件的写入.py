# 打开文件，"w"模式，如果文件不存在会创建新文件
f = open("D:/Documents/MyVSCode/Python/MyFirstPython/8-3-0-test.txt", "w", encoding="UTF-8")

# write写入，此时内容只写入到内存
f.write("Hello, world")
# >>> (空内容)

# flush刷新，内存中积攒的内容，写入到硬盘中
f.flush()
# >>> Hello, world

# close关闭带有flush功能
f.close()

# 已经保存过的文件如果再次使用“w”模式打开，会覆盖原有的内容
f = open("D:/Documents/MyVSCode/Python/MyFirstPython/8-3-0-test.txt", "w", encoding="UTF-8")
f.write("你好世界")
f.close()

# 想要不破坏原有内容可以使用“a”追加模式
f = open("D:/Documents/MyVSCode/Python/MyFirstPython/8-3-0-test.txt", "a", encoding="UTF-8")
f.write("\nHello, world")
f.close()