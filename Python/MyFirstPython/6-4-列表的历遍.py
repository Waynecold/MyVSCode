# 分别使用while和for循环，实现列表的历遍

## while循环
def list_while_func():
    my_list = ["hello", "world", "Wayne"]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f"列表的第{index + 1}个元素：{element}")
        index += 1

list_while_func()

## for循环
def list_for_func():
    my_list = ["stapler", "letter", "book"]
    for element in my_list:
        print(f"列表中的元素有：{element}")

list_for_func()