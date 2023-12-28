"""
字符串方法__str__
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__字符串魔术方法
    def __str__(self):
        return(f"Student类对象，name：{self.name}，age：{self.age}")
    
    # __lt__小于魔术方法
    def __lt__(self, other):
        return self.age < other.age
    
    # __le__小于等于魔术方法
    def __le__(self, other):
        return self.age <= other.age
    
    # __eq__等于魔术方法
    def __eq__(self, other):
        return self.age == other.age
    

stu1 = Student("周杰轮", 31)
print(stu1)          # 直接打印类对象只会输出内存地址（区别于print(stu.name)）
print(str(stu1))     # 即使转换了str类型也是，加了__str__方法就可以正确输出字符串内容了

stu2 = Student("林均节", 36)
print(stu1 < stu2)  # >> Ture
print(stu1 > stu2)  # >> False

stu3 = Student("张雪有", 31)
print(stu1 <= stu2) # >> Ture

print(stu1 == stu3) # >> False 不用__eq__方法的话，默认是对比数据的内存地址
print(stu1 == stu3) # >> Ture 加上__eq__方法后才是比较数据的值的大小
