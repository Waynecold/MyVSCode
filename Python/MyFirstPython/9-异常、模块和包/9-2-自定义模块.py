__all__ = ['add'] # 控制当import *时，只导入add函数

def add(a, b):
    print(a + b)

def min(a, b):
    print(a - b)

# 用于内部测试，调用时不会执行
if __name__ == '__main__':
    add(1, 2)
