# Python 学习笔记1-基础部分

作者：Waynecold

## 1 - 运行Python

两种方法：

1. 在“命令提示符”（CMD）中输入`python`以打开Python，出现`>>>`后，输入代码，回车即可运行代码。
   > 例如：`print("Hello, world!")`  

   `print()`语句可以一次输出多份内容，内容之间使用`,`分隔。
   > 例如：`print("内容1", "内容2")`

2. 还可以把代码写在一个`.py`结尾的文件中，再在CMD中使用命令去运行该文件。
    > 命令格式：`python 空格 盘符:\地址\文件名`  
    > 例如：`python d:\code\test.py`

## 2 - Python基础语法

### 字面量

被写在代码中固定的值，称为字面量。整数、浮点数以及字符串等等都是字面量。

Python中有6种值（数据）类型：

- `数字Number`
  - `整数int`
  - `浮点数float`
  - `复数complex`
  - `布尔整数bool`
- `字符串String`
- `列表List`
- `元组Tuple`
- `集合Set`
- `字典Dictionary`

### 注释

注释只是提高代码的可读性，并不会被程序执行。

- 单行注释：使用`#`+空格+注释内容

- 多行注释：使用一对三个双引号包裹注释内容，`"""`注释内容`"""`

### 变量

变量用来记录数据，以便重复使用储存的数据。Python中的变量**不需要声明**。变量在使用前须要赋值，赋值后变量才会被创建。
> 定义格式：`变量名 = 变量值`  
> （`=`是赋值运算符，意思是右边的值赋予左边的变量）

### 数据类型（基础）

上面已经提过，[基本类型](#字面量)有6种常见类型。值得注意的是Python不同于C，**变量是没有类型的，只是数据本身才有数据类型。**

使用`type()`语句来查看数据的类型。
> 例如：

```py
print(type("你好世界。"))
print(type(666))
print(type(3.1415926))
```

> 输出显示：

```md
<class 'str'>
<class 'int'>
<class 'float'>
```

### 数据类型的转换（基础）

- `int(x)`将x转换成整数
- `float(x)`将x转换成浮点数
- `str(x)`将x转换成字符串

### 标识符

一些自定义的变量，方法，类的名字，是内容的标识。

规则如下：

- 只允许英文，~~中文~~（不推荐），数字，下划线
- 数字不允许开头
- 不可使用关键字（系统保留）
- 大小写敏感

建议规范：

- 全小写英文
- 下划线命名法

### 运算符

|算术运算符|赋值运算符|复合赋值运算符|
|---|---|---|
|`+`加|`=`赋值|`+=`|
|`-`减||`-=`|
|`*`乘||`*=`|
|`/`除||`/=`|
|`//`取整除||`//=`|
|`%`取余||`%=`|
|`**`指数||`**=`|

> 复合赋值是指变量和右边结果进行运算后再赋值给左边变量

### 字符串扩展

#### 字符串的定义

1. 单引号：`name = 'wayne'`
2. 双引号：`name = "wayne"`（推荐使用）
3. 三引号：`name = """wayne"""`

上面学[注释](#注释)时提过，三引号原是**多行注释**的用法，但只要把三引号包裹的内容赋值给一个变量，即可接收成**字符串**使用。这样，其中包裹的字符串内容也是可以换行的。

当字符串包含单引号或双引号，可以互相嵌套解决。另外，只包含一边的引号的情况，可使用`\`转义。

#### 字符串的拼接

**字符串**字面量和**字符串**变量之间可以使用`+`拼接。（前面刚开始学[print()语句](#1---运行python)提到，用逗号`,`隔开多个输出内容的话，每个内容都将以空格分开。）

注意，字符串不能和非字符串类型（如数字）进行拼接。

#### 字符串格式化

使用占位符`%s`占位（C中称转换说明），后面接对应的变量，多个变量占位，用括号包裹起来，且按顺序填入。

语法：`"%占位符" % 变量`

> 示例：

```py
name = "Wayne"
message = "你好，%s" % name
print(message)
```

> 多个变量：

```py
weather = "小到中雨"
date = 14
month = 9
#原本是数字类型，%s转换成字符串类型
message = "今天是%s月%s日，今天的天气是%s。" % (month, date, weather)
print(message)
```

基本数据类型的占位符：

- `%s`字符串
- `%d`整数
- `%f`浮点数

### 格式化的精度控制

使用辅助符号`m.n`来控制数据的宽度和精度：

- `m`：控制宽度（很少使用），小于数字自身则不生效
- `n`：控制小数点精度，小数部分自动四舍五入

> 示例：

```py
# 3 数字的修饰符m.n
num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11宽度限制不限制，小数精度2，结果是：%.2f" % num2)
```

> 输出结果：

```py
数字11设置宽度限制5，结果是：   11
数字11设置宽度限制1，结果是：11
数字11设置宽度限制7，小数精度2，结果是：  11.35   
数字11设置宽度限制不限制，小数精度2，结果是：11.35
```

### 字符串格式化方式 2

上面的方法还是C老一代的写法，现代的Python还能更优雅地使用：
> `f“内容{变量}”`

来快速格式化。（不理会类型但也不做精度控制）

> 示例：

```py
weather = "小到中雨"
date = 14
month = 9
print(f"今天是{month}月{date}日，今天的天气{weather}。")
```

### 表达式格式化

表达式：一条具有明确执行结果的代码语句。

> - `f"(表达式)"`
> - `"%s%d%f" % (表达式, 表达式, 表达式)`

### 数据输入

使用`input()`语句获取键盘输入，再使用一个变量来接收获取的数据即可。

- `input()`数据输入
- `print()`数据输出

> 示例：

```py
print("请告诉我你是谁？")
name = input()
print("我知道了，你是%s。" % name)

# 进一步优雅
name = input("请告诉我你是谁？")
print("我知道了，你是%s。" % name)
```

第2种提示语言直接写进`input()`括号内，效果是等同的，但更简洁优雅。

输入类型始终是**字符串**类型。注意做数据类型转换。

## 3 - Python判断语句

### 布尔类型

布尔类型是6种[基本数据类型](#字面量)中的其中一种，布尔`bool`和整数`int`，浮点数`float`，复数`complex`都属于**数字**`Number`的一类。
> 布尔类型的字面量（**注意：Python大小写敏感**）：

- 真`True` `1`
- 假`False` `0`

### 比较运算符

|运算符|描述|
|---|---|
|`==`|相等|
|`!=`|不相等|
|`>`|大于|
|`<`|小于|
|`>=`|大于等于|
|`<=`|小于等于|

使用比较运算符时会得到布尔类型的结果。

### if语句的基本格式

满足条件时，执行语句，否则跳过。

> 语法：

```py
if 条件:  
    语句1
    语句2
    ...
```

注意：

- 条件后接冒号`:`
- Python对缩进敏感，判断后执行的子代码需要**缩进4个空格**

### if...else语句

> 语法：

```py
if 判断条件:  
    成立时执行的语句1
    语句2
    语句3
    ...
else:
    不成立时执行的语句1
    语句2
    语句3
    ...
```

注意：

- `else`搭配`if`的判断条件，自身不需要判断条件
- `else`后面接冒号`:`
- `else`的代码块也要缩进4个空格

### if...elif...else复合语句

可以完成多条件的判断。

> 语法：

```py
if 条件1:  
    语句1
    语句2
    ...
elif 条件2:
    语句1
    语句2
    ...
elif 条件3:
    语句1
    语句2
    ...
else:
    语句1
    语句2
    ...
```

注意：

- `elif`可以写多个
- 多个判断是互斥且有序的，上一个判断满足了就不会判断了
- 可以把`input()`语句写到判断条件内，节省代码量

### 判断语句的嵌套

Python通过缩进来决定层次的关系。

> 语法：

```py
if 条件1:  
    语句1
    语句2
    ...
    if 条件2:
        语句1
        语句2
        ...
```

注意：设计层级时应注意每个判断条件的优先级。优先级高的在外层，优先级低的在内层，同等优先级的使用`elif`。

## 4 - Python循环语句

### while循环语句

只要条件满足，无限循环执行。

> 语法：

```py
while 条件:
    语句1
    语句2
    ...
```

注意：

- 条件应该要可以得到一个布尔类型的结果，`True`继续，`False`停止
- 设置好终止循环的条件，否则会无限循环
- 缩进

> 示例：无限猜数字

```py
# 获取范围在1-100的随机数
import random
num = random.randint(1, 100)
# print(f"{num}") # 此句显示随机数的确切数字

# 猜测次数的计数器
count = 0

# 设置布尔类型来标志循环是否继续
flag = True

while flag:
    guess_num = int(input("请输入你猜的数字"))
    if guess_num == num:
        print("猜中了")
        flag = False # 把标志设置为False就终止循环
    else:
        if guess_num > num: # 提示猜大了还是小了
            print("大了")
        else:
            print("小了")
    count += 1
print(f"你一共猜了{count}次") # 最后显示猜了多少次
```

### 嵌套while循环

> 示例：准备表白100天，每天送10支玫瑰，然后表白一次，100天后表白成功

```py
i = 1
while i <= 100:
    print(f"今天是第{i}天表白，准备表白……")
    j = 1
    while j <= 10:
        print(f"送给小美{j}支玫瑰花")
        j += 1
    print("小美，我喜欢你")
    i += 1
print(f"第{i - 1}天，表白成功")
```

注意：

- 通过缩进区分多层的循环
- 注意条件的控制，避免无限循环

### 补充知识

#### 1. `print()`不换行输出

多个`print()`语句之间，会自动换行打印输出，但想要输出而不换行，可以在`print()`中加入`end=''`。

> 例如：  
> `print("语句1", end='')`  
> `print("语句2")`

#### 2. `\t`制表符

使用`\t`令多行输出的单词可以对齐。

> 例如：  
> `print("Hello\tworld")`  
> `print("itheimat\tbest")`

#### 3. 换行

不同于C的`\n`换行符，Python中`print()`空内容就是换行。

### for循环语句

`for`循环是“轮询”机制，对一批内容进行逐个处理。

> 语法：（遍历字符串`name`）

```py
name = "wayne"
for x in name:
    语句1
    语句2
    ...
```

- `x`是临时变量。
- `x`属于`for`循环内的**作用域**，虽然没有在开头就定义，但也能在作用域外引用（不建议），想要在**作用域外**引用，正确做法应预先定义它
- `name`待处理的数据集（序列），如字符串

### range 语句

序列类型：

- 字符串
- 列表
- 元组

上面已提及了字符串的序列，列表和元组都是关于数字的序列。使用`range`语句，获得一个简单的**数字序列**。

- 语法1：  
  `range(num)`  
  获取从0开始到num（不含num自身）结束的数字数列，如：`range(5)`获取到`[0, 1, 2, 3, 4]`
- 语法2：  
  `range(num1, num2)`  
  获取从num1到num2（不含num2自身）结束的数字序列，如：`range(5, 10)`获取到`[5, 6, 7, 8, 9]`
- 语法3：`range(num1, num2, step)`  
  获取从num1到num2(不含自身)的，**步长**为step的序列，如：`range(5, 10, 2)`获取到`[5, 7, 9]`

### for循环的嵌套

> 语法：

```py
# 作用域外引用该变量的话需提前定义
# i = 0
# y = 0
for x in seq1 :
    语句1
    语句2
    ...
        for y in seq2 :
        语句1
        语句2
        ...
```

### 循环中断：continue和break

对自身所在的`while`循环或`for`循环都生效。无法对上层循环作用。

- `continue`语句：临时中断**本次**循环，直接进入**下一次循环**，语句后面的语句均不会执行
- `break`语句：直接**结束**循环，剩余循环均不会执行，跳到循环外的语句

## 5 - 函数

### 函数的介绍

组织好的可重复使用，实现特定功能的代码段。

> 示例：计算字符串的长度

```py
# 创建函数
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度为{count}。")

# 重复调用函数
name = "wayne"
name2 = "waynecold"
my_len(name)
my_len(name2)

# 其实，Python自带计算字符串函数len()
len(name)
len(name2)
```

> 定义语法：

```py
def 函数名（传入函数）:
    函数体
    return 返回值
```

- 先定义，后调用
- 不需要参数，可以省略，但括号不可省略
- 不需要返回值，可以省略

### 函数的传入参数

调用函数进行计算的时候，接受外部提供的数据。

> 示例：

```py
# 定义一个叫add的函数，实现功能：接受两个数字，得到相加的结果
def add(x, y):
    result = x + y
    print(f"{x} + {y}的计算结果是：{result}")

# 调用函数
add(1, 2)
add(2, 5)
```

- 函数定义中，`x`和`y`是形式参数，参数之间使用`,`逗号分隔
- 调用函数时，`a`和`b`是实际参数，传入参数时要一一对应

### 函数的返回值

- 函数执行完成后，可以使用`return`关键字返回想要的结果
- 变量可以接收函数的返回值
- 注意，函数体遇到`return`就结束了，后面的所有代码都不执行了

### None类型

类似`C`里，空值是`void`。在`Python`中使用`None`字面量，类型为`<class'NoneType'>`，来表示：空的，无意义的。

使用场景：

- 函数返回值
- 在`if`判断上，`None`相当于`False`
- 定义无初始值的变量

### 函数说明文档

函数都是纯代码语言，对于人类阅读效率较低，可以添加说明文档，辅助理解函数的作用。

> 示例：多行注释的说明文档

```py
def add(x, y):
    """
    add函数接收2个参数，进行相加的功能
    :param x: 形参x表示相加的其中一个数字
    :param y: 形参y表示相加的另一个数字
    :return: 返回值是2个数相加的结果
    """
    result = x + y
    print(f"2数相加的结果是{result}")
    return result
```

- 在调用函数时，键入函数名，鼠标放在上面即可弹出文档提示

### 函数的嵌套调用

`函数a`执行到调用`函数b`的语句，先把`函数b`全部执行完，再继续执行`a`的剩余内容。

### 变量的作用域

作用域：变量的作用范围。

- 局部变量：只在函数体内临时使用，完成后立即销毁，函数外不可再调用
- 全局变量：将变量定义在函数体外，即可使用全局变量

在局部变量前添加哎`global`关键字，可以将局部变量变为全局变量。如：`global 变量名`。

### ATM综合案例

详见文件[ATM综合案例.py](https://)

## 6 - 数据容器

一种可以容纳多份数据的数据类型。每一份数据称为元素，每一个元素可以是任意类型的数据。

- 列表`list`
- 元组`tuple`
- 字符串`str`
- 集合`set`
- 字典`dictionary`

### 列表list

> 定义语法：

```py
# 字面量定义
[元素1, 元素2, ...]

# 变量定义
变量名 = [元素1, 元素2, ...]

# 定义空列表
变量名 = []
变量名 = list[]
```

列表可以一次存储多个元素，且可以是**不同类型**的数据（数字，字符串，布尔等），**嵌套**也行。

使用**下标索引**取出特定数据。正序从0开始递增，倒序从-1开始递减。

> 取出元素：

```py
变量名 = [1, 2, [3，4]]
列表[0] # 1（第一个元素）
列表[-1] # 4（倒数第一个元素）
列表[3][0] # 3（第三个元素中的第一个）
```

`列表`除了定义，下标取值，还提供了一系列的功能（**方法**）：

|方法|语法|
|---|---|
|查询元素下标|`index = 列表名.index(元素)`|
|修改元素下标|`列表[下标] = 值`|
|插入元素|`列表.insert(下标, 元素)`|
|追加元素|1、单个`列表.append(元素)`<br>2、多个`列表.extend(元素)`|
|删除元素|1、`del列表[下标]`<br>2、`列表.pop(下标)`（返回值可接收）<br>3、`列表.remove(元素)`（删除第一个匹配值）|
|清空列表|`列表.clear()`|
|统计元素个数|1、指定元素`列表.count(元素)`<br>2、全部元素`len(列表)`|

---

补充：前面已经学过函数，如果将函数定义为 **class（类）** 的成员，那么函数称为 **方法**。

> 例如：

```py
# 函数
def add(x, y):
    return x + y

# 方法
class Student:
    def add(self, x, y):
        return x + y

# 函数的调用
num = add(1, 2)

# 方法的调用
student = Student()
num = student.add(1, 2)
```

---

#### 列表的遍历

将列表容器中的元素依次取出处理的行为，称之为：**遍历、迭代**。

> while循环语法：

```py
index = 0
while index < len(列表):
    元素 = 列表[index]
    对元素进行处理
    index += 1
```

> for循环语法：

```py
for 临时变量 in 列表:
    对临时变量进行处理
```

### 元组tuple

`列表`的元素可以**被修改**，`元组`一旦定义完成就**不可修改**。  
只有元组的元素是`列表`，修改`列表中的内容`才是允许的。

> 定义语法：

```py
# 字面量定义
(元素1, 元素2, ...)

# 变量定义
变量名 = (元素1, 元素2, ...)

# 定义空元组
变量名 = ()
变量名 = tuple()
```

和`列表`一样，`元组`的元素也是内容不受限。
其他基本的属性和操作都和列表相同。

### 字符串str

`字符串`其实也是数据容器，是`字符`的容器，不同于`C`，`Python`中单个`字符`也算`字符串`。

`已定义的字符串`是无法修改的。

|操作方法|语法|
|---|---|
|下标取值|`字符串[下标]`|
|查询下标|`index = 字符串.index(字符串)`|
|元素替换|`字符串.replace(字符串1, 字符串2)`<br>不会修改原字符串，得到另一个新的|
|字符串拆分|`list = 字符串.split(字符串)`<br>拆分后得到一个新的列表|
|移除首尾|`字符串.strip()` 去除空格<br>`字符串.strip(字符串)` 去除指定字符串|
|统计字符出现次数|`字符串.count(字符串)`|
|统计字符串长度|`len(字符串)`|

#### 补充：序列的切片操作

`列表`、`元组`、`字符串`都是**内容连续、有序**的数据容器，可视为`序列`。序列的下标索引可以正序从0开始从前往后，也可以倒序从-1开始从后往前。

|元素1|元素2|元素3|元素...|元素n|
|---|---|---|---|---|
|0|1|2|>>|n-1|

|元素1|元素2|元素...|元素n-1|元素n|
|---|---|---|---|---|
|-n|-(n-1)|<<|-2|-1|

切片：从一个序列中取出一个子序列

> 语法：`序列[起始下标:结束下标:步长]`

- 起始可以省略，从头开始
- 结束可以省略，到尾结束，得到的结果是**结束下标-1**的元素结束
- 步长可以省略，默认为1
- 步长是负数，表示倒序执行
- 切片后不会影响原序列，而得到新的序列

### 集合set

上面已经学了：

- `列表`：可修改，可重复，有序元素
- `元组`和`字符串`：不可修改，可重复，有序元素

`集合`主要特点：不支持重复元素（去重），无序存储（不支持下标索引），可修改，仅支持for循环。

> 定义语法：

```py
# 字面量定义
{元素1, 元素2, ...}

# 变量定义
变量名 = {元素1, 元素2, ...}

# 定义空列表
变量名 = set()
```

- 使用大括号`{}`包裹
- 空集合使用圆括号`()`
- `集合`是无序的，所以不支持下标索引访问
- 允许修改

|操作方法|语法|
|---|---|
|新增元素|`集合.add(元素)`|
|移除元素|`集合.remove(元素)`|
|随机取出一个元素|`集合.pop()`|
|清空集合|`集合.clear()`|
|取出差集|`集合1.difference(集合2)`|
|删除差集|`集合1.difference_update(集合2)`|
|合并集合|`集合1.union(集合2)`|
|统计元素个数|`len(集合)`|

### 字典dict

`字典`可以通过`Key`检索`Value`，`Key: Value`称为`键值对`。

`字典`的特点和集合类似，`Key`不允许重复，会覆盖原先的数据。`字典`可以嵌套，嵌套时`Value`是`字典`，`Key`不能是`字典`。可修改，仅支持for循环。

> 定义语法：

```py
# 字面量定义
{key: value, key: value, ...}

# 变量定义
变量名 = {key: value, key: value, ...}

# 定义空字典
变量名 = {}
变量名 = dict()
```

|操作方法|语法|
|---|---|
|获取指定值|`字典[key]`|
|新增元素|`字典[key] = value`|
|取出并删除元素|`字典.pop(key)`|
|清空字典|`字典.clear()`|
|获取全部的Key|`字典.keys()`|
|统计元素个数|`len(字典)`|

#### 数据容器整理分类

下标索引、重复类型：

- 支持（序列类型）：`列表`、`元组`、`字符串`
- 不支持（非序列类型）：`集合`、`字典`

修改元素：

- 支持：`列表`、`集合`、`字典`
- 不支持：`元组`、`字符串`

通用操作：

- 5种都支持`for循环`的遍历
  - 序列类型还支持`while循环`的遍历
- `len()`函数统计元素个数
  - `max()`统计获取最大元素
  - `min()`统计获取最小元素
- 类型转换
  - `list()`转换为列表
  - `str()`转换为字符串
  - `tuple()`转换为元组
  - `set()`转换为集合
- 排序功能
  - 升序：`sorted(容器)`
  - 降序：`sorted(容器, reverse = True)`

#### 字符串的比较大小

通过`ASCII码`进行比较大小。字符从左到右按位比较，只要有一位大整体就大。

## 7 - 函数进阶

### 函数多返回值

> 示例：

```py
def test_return():
    return 1, "hello", True

x, y, z = test_return()
print(x)
print(y)
print(z)
```

### 函数参数种类

常见4种类型：

- `位置参数`：传递的参数和定义的参数的**个数和顺序**必须一致
- `关键字参数`：通过`键值对`的形式传递参数，传入可以**不考虑顺序**  
  `关键字参数`和`位置参数`可以混用，但位置参数必须放在前面（顺序要求）
- `缺省参数`：定义函数时就把某个参数设定了默认值，传入时忽略将使用默认值，如果传入其他值将覆盖默认值，混用时默认值必须写在最后
- `不定长参数`：不确定会使用参数个数时使用
  - 位置不定长使用`*`号，规范命名为`*args`，以元组类型接收多个不定参数，有顺序要求
  - 关键字不定长使用`**`号，规范命名为`**kwargs`，以字典类型接收多个`键值对`的不定参数，没有顺序要求

### 匿名函数

前面学习的参数都是以基本数据类型作为传入参数，函数也可以作为参数传递到另一个函数。这是一种计算逻辑的传递，非数据的传递。

函数在调用另一函数作为参数时，不必考虑传入函数的内部是如何处理数据的，所以传入的函数就是黑箱。

### lambda匿名函数的语法

函数的定义：

- `def`关键字：可以定义带有名称的函数，可重复使用
- `lambda`关键字：可定义匿名函数，无名称，临时使用一次

语法和def基本一样，但函数体只能写一行代码：

> `lambda 传入函数：函数体`（一行）

## 8 - Python的文件操作

### 文件的编码

编码记录了内容和二进制之间互相转换的逻辑。最常用的是`UTF-8`编码，其他还有`GBK`等。内存中的数据会在计算机关机后消失，想要长久保存数据，就要把数据保存为文件。

### 文件的打开

在`Python`中，使用对象`f`接收`open()`函数，可以打开一个已经存在的文件，或者创建一个新文件。

> `f = open(file, mode, encoding)`

- `file`：文件名的（包括路径）
- `mode`：访问模式
  - `r`：只读（默认访问模式）
  - `w`：写入（覆盖原内容）
  - `a`：追加（写入到已有内容之后）
- `encoding`：编码格式

### 文件的读取

操作：

- `f.read(num)`操作，读取num个字符，缺省就是全部
- `f.readlines()`，读取全部行，并封装到列表中
- `f.readline()`，读取单行
- `for`循环，自动按换行符分隔每一行，进行循环操作

注意：每次读取完后，下次再次使用函数读取将从上次结束的位置继续开始。

### 文件的关闭

- `f.close()`操作，关闭文件对象
- `with open() as f:`打开文件，可自动关闭

### 文件的写入

> 示例：

```py
# 打开文件
f = open("python.txt", "w")
# 内容写入
f.write("hello world")
# 内容刷新
f.flush
```

- 打开文件使用`open()`函数的`"w"`模式，如果文件不存在会创建新文件
- 文件已有内容，则会覆盖原来的内容
- `write`写入，此时内容只写入到内存
- `flush`刷新，内存中积攒的内容，写入到硬盘中
- `close()`方法，带有`flush()`功能

### 文件的追加

通过`open()`函数的`"a"`模式，其他特性和`"w"`模式相同。

## 9 - Python异常、模块与包

### Python异常

程序错误和异常称为`bug`。对`bug`提前`捕获`以减少`异常`。

> 捕获异常：

```py
# 捕获常规异常
try:
    可能发生错误的代码
except[异常 as 别名]:
    如果出现异常执行补救的代码
[else:]
    没有异常时执行的代码
[finally:]
    有无异常都执行，如关闭文件

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print("name变量名称未定义错误")

# 捕获多个异常
try:
    print(name)
except(NameError, ZeroDivisionError) as e:
    print("出现了变量未定义 或者 除以0的异常错误")

# 捕获所有异常 - Exception
try:
    print(name)
except Exception as e:
    print("出现异常了")
```

异常具有传递性，在多个嵌套函数内传递

### 模块Module

`模块`也是一个`Python`文件，储存`类`、`函数`、`变量`等。通过导入进行使用。

> 导入模块的语法：

```py
[from 模块名] import [模块|类|变量|函数|*][as 别名]
```

- `from`可以省略，`as`别名也可以省略
- `*`表示导入模块全部功能
- 通过`.`来确定层级关系
- 模块导入通常写在代码的开头位置

> 示例：

```py
# time是Python内置的模块，按住CTRL点击可打开该模块的文件time.pyi
import time 
print("你好")
time.sleep(5)
print("我好")
```

#### 自定义模块

模块也是`Python`文件，通过`import`、`from`关键字导入即可。

通过`if __main__ == "__main__`"限制仅有当直接执行程序才进入`if`内部，如果是导入的，则不进入`if`内部。用于模块的内部测试，调用时不会执行。

不同模块，同名的功能都被导入的话，后导入的会覆盖先前导入的。

`__all__ = [函数1, 函数2...]`变量功能：引入一个列表，用于控制`import *`对哪些功能可以被导入。

### Python包

`Python包`就是文件夹，里面存放多个`Python模块`文件，但包含一个`__init__.py`文件。文件内也使用`__all__`变量来控制`import *`的导入范围。
`包`的导入和`模块`的类似，只是多一层级的写法。

常用的第三方包：

- 科学计算：`numpy`
- 数据分析：`pandas`
- 大数据计算：`pyspark`、`apache-flink`
- 图形可视化：`matplotlib`、`pyecharts`
- 人工智能：`tensorflow`

`Python`内置了`pip程序`用于导入第三方包。

> 示例：（在命令提示符中通过网络安装第三方包）

```cmd
pip install -i url地址 包名称
```

## 10 - Python综合案例

### json数据格式

`JSON`是以一种轻量级数据交互格式，本质是一个特定格式的`字符串`。主要功能是在不同编程语言中数据的**传递和交互**。`JSON`的格式正好和`Python`中的`字典`或一个`内部元素全是字典的列表`。

> Python数据和Json数据的互相转化：

- 在Python中，需要先`import json`，再使用`dumps`和`loads`方法，如：`data = json.dumps(data)`
- 如果字符串内容包含中文，可以使用`ensure_ascii = False`参数来确保中文正确转换

### pyecharts模块

开发可视化图表使用的技术栈是Echart框架的Python版本：pyecharts包<https://pyecharts.org/#/zh-cn/>

> 需要在cmd安装：`pip install pyecharts`

pyecharts常用配置选项:

- 全局配置选项
  - 配置图标的标题
  - 配置图例
  - 配置鼠标移动的效果
  - 配置工具栏
  - 等等整体的配置项
- 系列配置选项

### 数据处理

本章缺少数据。

结合`jsonviewer`来分析`json`的结构层次，主要使用`.replace`和`切片`的方法来处理原始数据。

### 构建折线图

```py
import json
from pyecharts.charts import Line # 导包，导入折线图功能
from pyecharts.options import TitleOpts, LabelOpts # 导入标题设置
...
## 构建折线图对象
line = Line()
...
# 调用render方法，生成图表
line.render()
```

详见：`Python\MyFirstPython\10-Python综合案例\10-3-折线图开发（缺少数据不能运行只作展示）.py`

### 构建可视化地图

```py
from pyecharts.charts import Map # 导入地图功能
from pyecharts.options import VisualMaOpts #地图相关设置
...
# 创建地图对象
map = Map()

# 添加数据
map.add("各省份确诊人数", data_list, "china")
...
# 绘图
map.render("全国疫情地图.html") # 创建并命名目标文件
```

详见：`Python\MyFirstPython\10-Python综合案例\10-4-地图可视化基本使用.py` 和`Python\MyFirstPython\10-Python综合案例\10-5-全国疫情可视化地图（缺数据）.py`

### 构建柱状图

```py
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

# 创建柱状图
bar = Bar()

# 添加x轴数据
bar.add_xaxis(["中国","美国","英国"])

# 添加y轴数据
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right")) # 设置数值标签在右侧

# 反转x轴和y轴
bar.reversal_axis()

# 绘图
bar.render("基础柱状图.html")
```

### 构建时间线柱状图

详见：`Python\MyFirstPython\10-Python综合案例\10-7-带有时间线的柱状图.py`