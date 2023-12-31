# 数据的封装
import json

from data_define import Record

# 文件读取相关功能
## 先定义一个抽象类((父类)
class FileReader:
    """
    功能：读取不同格式的数据，并封装到list列表中
    """
    def read_data(self) -> list[Record]: # type: ignore
        pass        # 因为将会有两种格式的数据传入，这里先pass掉，具体实现功能由子类进行操作

## 子类:记录文件的路径
### 本例子有两种数据的格式，先是txt格式的数据预处理
class TextFileReader(FileReader):
    def __init__(self, path):               # 定义成员变量-读取文件路径
        self.path = path
    
    # 复写父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()             # 消除每一行的\n
            data_list = line.split(",")     # 以【,】分割字符串，并装到列表data_list中
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
                                            # 注意下标[2]想得到的是金额是数字，转换称int
            record_list.append(record)      # append追加，使record_list成为一个嵌套的list
        
        f.close()
        return record_list                  # 返回这个数据经过预处理的list

### json格式的数据预处理
class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    # 复写父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)                # 使用json.loads()要导包才不会报错
            record = Record(data_dict["date"], data_dict["order_id"], data_dict["money"], data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list

if __name__ == '__main__':                              # 这种写法只在模块内执行
    text_file_reader = TextFileReader("/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for l in list1:
        print(l)
    
    for l in list2:
        print(l)
