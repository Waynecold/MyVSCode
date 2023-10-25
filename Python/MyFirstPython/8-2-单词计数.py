"""
创建txt文件，内容如下，通过读取文件的操作，统计itheima单词出现的次数

itheima itcast python
itheima python itcast
beijing shanghai itheima
shenzhen guangzhou itheima
wuhan hangzhou itheima
zhengzhou bigdata itheima

"""

# 我的写法
with open("D:/Documents/MyVSCode/Python/MyFirstPython/8-2-0-word.txt", "r", encoding="UTF-8") as f:
    count = 0
    for line in f.readlines(): # 这里的readlines可以省略
        list = line.split() # 这里的list其实是list类型，list里面的元素是str类型
        for str in list:
            if "itheima" in str: # 这里没有strip也算了进去，这里不是字符串的对比，而是指定字符顺序作为对比
                count +=1
    print(f"1、itheima出现的次数：{count}")

# 示例

# 打开文件
f = open("D:/Documents/MyVSCode/Python/MyFirstPython/8-2-0-word.txt", "r", encoding="UTF-8")

# 方法1，读取全部内容，通过字符串count方法统计itheima的单词数量
content = f.read() # 此处read得到的结果是一整串str类型
count = content.count("itheima")
print(f"2、itheima在文件中出现了{count}次。")

# 打开文件
f = open("D:/Documents/MyVSCode/Python/MyFirstPython/8-2-0-word.txt", "r", encoding="UTF-8")

# 方法2，读取内容，一行一行读取
count = 0
for line in f:
    line = line.strip() # 去除开头和结尾的空格和换行符
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            count += 1
print(f"3、itheima出现的次数是{count}")
f.close()

# 方法1最优