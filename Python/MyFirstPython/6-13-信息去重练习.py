# 定义一个列表
my_list = ['蒸汽平台', 'V社', '蒸汽平台', 'V社', 'Dota', 'CSGO', 'Dota', 'CSGO', 'best']

# 定义一个空集合
my_set = set()

# 通过for循环遍历列表
for element in my_list:
    print(f"1、列表\"my_list\"中的元素有\'{element}\'")

    # 在for循环中将列表的元素添加到空集合中
    my_set.add(element)

# 最终得到元素去重的集合对象，并打印输出
print(f"2、my_list原内容为{my_list}")
print(f"3、去重后之后的结果为{my_set}")