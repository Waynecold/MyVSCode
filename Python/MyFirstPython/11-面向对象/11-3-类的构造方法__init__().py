# 构造方法的名称：__init__

class Student:
    def __init__(self, name, age, tel) -> None: # 既有定义也有赋值的功能
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")

stu = Student("周杰轮", 31, "18500006666")
print(stu.name)
print(stu.age)
print(stu.tel)