# # import导入time模块，使用sleep功能（函数）
# import time # time是Python内置的模块，按住CTRL点击可打开该模块的文件time.pyi

# print("你好")
# time.sleep(5)
# print("我好")

# # import导入time的sleep功能（函数）
# from time import sleep

# print("你好")
# sleep(5)
# print("我好")

# # *表示导入time模块全部功能
# from time import * # wildcard通配符

# print("你好")
# sleep(5)
# print("我好")

# 使用as给特定功能加上别名
import time as t

print("你好")
t.sleep(5)
print("我好")