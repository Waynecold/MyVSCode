# 函数b
def func_b():
    print("---2---")

# 函数a
def func_a():
    print("---1---")
    func_b()
    print("---3---")

# 调用函数a
func_a()