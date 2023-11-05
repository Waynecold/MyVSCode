"""
要求：
创建一个自定义包，名称为：my_utils
包内提供2个模块：
1、str_util.py(字符串相关)：
    1、str_reverse(s)函数，
        接收传入字符串，将字符串反转返回。
    2、substr(s, x, y)函数，
        按照下标x和y，对字符串进行切片。
2、file_util.py（文件处理相关）：
    1、print_file_info(file_name)函数，
        接收传入文件的路径，打印文件的全部内容，
        如文件不存在则捕获异常，输出提示信息，
        通过finally关闭文件对象。
    2、append_to_file(file_name, data)函数，
        接收文件路径以及传入数据，将数据追加写入到文件中。
3、构建好包之后，尝试用一用。
"""

# 1
import my_utils_9_3_0.str_util
from my_utils_9_3_0 import file_util

str_input = "abcdefg"
print(my_utils_9_3_0.str_util.str_reverse(str_input))
print(my_utils_9_3_0.str_util.substr(str_input, 0, 4))

path = "D:/Documents/MyVSCode/Python/MyFirstPython/9-异常、模块和包/9-3-1-示例文件.txt"
test = "栖息于热带和亚热带海中。乌翅真鲨通常独居，偶尔成群结队地猎食。"
file_util.print_file_info(path)
file_util.append_to_file(path, test)