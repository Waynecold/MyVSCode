def print_file_info(file_name):
    """
    接收传入文件的路径，打印文件的全部内容。
    :param file_name: 传入路径
    :return: None
    """
    fr = None
    try:
        fr = open(file_name, "r", encoding= "utf-8")
        content = fr.read()
        print(content)
        fr.close()
    except Exception as e:
        print(f"程序出现异常了，原因是：{e}。请联系程序管理员。")
    finally:
        if fr:  # 如果变量是None，表示False，如果有任何内容，表示True
           fr.close()


def append_to_file(file_name, data):
    """
    接收文件路径以及传入数据，将数据追加写入到文件中。
    :param file_name: 传入数据的路径
    :param data: 传入数据
    :return: None
    """
    # 追加操作
    fw = open(file_name, "a", encoding="utf-8")
    fw.write(data)
    fw.write("\n")
    fw.close()

    # 打印显示
    with open(file_name, "r", encoding="utf-8") as fr:
        content = fr.read()
        print(content)



# 示例
if __name__ == "__main__":
    ## 传入正确路径
    print("1")
    f = "D:/Documents/MyVSCode/Python/MyFirstPython/8-文件操作/8-0-Python的简介.txt"
    print_file_info(f)

    ## 传入错误路径
    print("2")
    f = "D:/Documents/MyVSCode/Python/MyFirstPython/8-0-Python的简介.txt"
    print_file_info(f)

    ## 追加数据
    print("3")
    f = "D:/Documents/MyVSCode/Python/MyFirstPython/8-文件操作/8-0-Python的简介.txt"
    data_append = "hello world"
    append_to_file(f, data_append)
