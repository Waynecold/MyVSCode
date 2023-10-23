# 定义字典
dict1 = {"wang": 99, "zhou": 88, "lin": 77}

# 定义空字典
dict2 = {}
dict3 = dict()
print(f"字典1的内容是{dict1}，类型是{type(dict1)}")
print(f"字典2的内容是{dict2}，类型是{type(dict2)}")
print(f"字典3的内容是{dict3}，类型是{type(dict3)}")

# 定义重复Key的字典
dict4 = {"wang": 99, "wang": 88, "zhou": 88, "lin": 77}
print(f"字典1的内容是{dict4}，类型是{type(dict4)}") # 结果wang：88覆盖了99

# 从字典中基于Key获取Value
dict1 = {"wang": 99, "zhou": 88, "lin": 77}
score = dict1["wang"]
print(f"wang的分数是{score}")

# 字典的嵌套
stu_score_dict = {
    "wang": {
        "语文": 77,
        "数学": 66,
        "英语": 33
    }, "zhou": {
        "语文": 88,
        "数学": 86,
        "英语": 55
    }, "lin": {
        "语文": 99,
        "数学": 96,
        "英语": 66
    }
}
print(f"学生的考试信息是：{stu_score_dict}")

# 从嵌套字典中获取数据
# 看一下zhou的语文成绩，lin的英语成绩
score = stu_score_dict["zhou"]["语文"]
print(f"zhou的语文分数是：{score}")
score = stu_score_dict["lin"]["英语"]
print(f"lin的英语成绩是：{score}")