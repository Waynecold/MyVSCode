# 定义函数
def user_info(name, age, gender):
    print(f"1、姓名是：{name}，年龄是：{age}，性别是：{gender}")

# 位置参数 - 默认形式
user_info("小明", 20, "男")

# 关键字参数
user_info(age=10, gender="女", name="潇潇")
## 位置参数和关键字参数混用（位置参数必须放在最前）
user_info("甜甜", gender="女", age=9)

# 缺省参数
def user_info_default(name, age, gender="男"):
    print(f"2、姓名是：{name}，年龄是：{age}，性别是：{gender}")

user_info_default("小天", 13)

# 不定长参数
## 位置不定长使用*号，默认叫*args
def user_info_uncertain_1(*args):
    print(f"3、args参数的类型是：{type(args)}，内容是：{args}")

user_info_uncertain_1(1, 2, 3, "小明", "男")

## 关键字不定长使用**号，默认规范写**kwargs
def user_info_uncertain_2(**kwargs):
    print(f"3、args参数的类型是：{type(kwargs)}，内容是：{kwargs}")

user_info_uncertain_2(name="小王", age=11, gender="男")