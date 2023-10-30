'''
已有bill.txt文件，读取内容
将文件写到bill.txt.bak备份
进行判断，将标记为测试的数据行丢弃
'''
# 我的写法
f1 = open("D:/Documents/MyVSCode/Python/MyFirstPython/8-4-0-bill.txt", "r", encoding="utf-8")
content = f1.readlines()
f2 = open("D:/Documents/MyVSCode/Python/MyFirstPython/8-4-0-bill.txt.bak", "w", encoding="utf-8")
for line in content:
    if "测试" in line:
        continue
    f2.write(line)
f2.close()
f1.close()

# # 示例
# # 打开文件得到对象，准备读取
# fr = open("D:/Documents/MyVSCode/Python/MyFirstPython/8-4-0-bill.txt", "r", encoding="utf-8")
# # 打开问价得到文件对象，准备写入
# fw = open("D:/Documents/MyVSCode/Python/MyFirstPython/8-4-0-bill.txt.bak", "w", encoding="utf-8")
# # for循环读取文件
# for line in fr:
#     line = line.strip()
#     # 判断内容，将满足的内容写出
#     if line.split(",")[4] == "测试":
#         continue # 符合条件，跳过循环到下一个
#     # 将内容写出去
#     fw.write(line)
#     # 前面进行了strip()操作，所以要补上换行符
#     fw.write("\n")
# # close掉2个文件对象
# fr.close()
# fw.close() # 这里打开fw文件使用"w"模式，是因为，在close之前的操作都依次写入到了文件内