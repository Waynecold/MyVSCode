def str_reverse(s):
    """
    接收传入字符串，将字符串反转返回。
    :param s: 传入的字符串
    :return: 反转后的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    按照下标x和y，对字符串进行切片。
    :param s: 传入的字符串
    :param x: 起始字符的下标
    :param y: 结束字符的下标（不含）
    :return: 切片完成后的字符串
    """
    return s[x:y]

# 示例
if __name__ == '__main__':
    str_reverse("abc")
    # >>> cba

    substr("abcdefghijk", 3, 5)
    # >>> de