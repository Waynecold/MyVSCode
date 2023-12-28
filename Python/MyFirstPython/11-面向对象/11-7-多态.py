# 父类
class Animal:
    def speak(self):            # 这里的speak是没有实际的操作的，是一个抽象方法
        pass                    # 含有抽象方法的类（出现pass）称为抽象类，也称接口，顶层设计

# 多个子类
class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

# 发声函数
def make_noise(animal: Animal):  # 要求传入一个Animal类型的参数
    animal.speak()

# 使用make_noise功能
dog = Dog()                     # 创建对象
cat = Cat()

make_noise(dog)                 # 不同对象，经过相同函数（同一动作）会返回不同的结果
make_noise(cat)