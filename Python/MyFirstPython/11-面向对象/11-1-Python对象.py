# 设计一个类
class Student:
    name = ""
    gender = ""
    nationality = ""
    native_place = ""
    age = 0

    # 带有成员方法，调用类的内部的属性时，默认都要带self关键字
    def say_hi(self):
        print(f"大家好啊，我是{self.name}, 欢迎大家多多关照。")

    def say_hi2(self, msg):
        print(f"大家好啊，我是{self.name}, {msg}。")
    

# 创建一个对象
stu_1 = Student()

# 向对象属性进行赋值，类名称.属性名称
stu_1.name = "林均节"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "山东省"
stu_1.age = 31

# 获取对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)

# 使用类对象里面的成员方法
stu_1.say_hi()
stu_1.say_hi2("哎哟不错哦")
stu_1.say_hi2("看好你哦")
