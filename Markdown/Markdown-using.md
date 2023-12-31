# Markdown展示笔记文档
>
>作者：Waynecold

## 一、标题 - \#

- 语法：**单边**“#”号+“空格”+内容  
- 示例：

# 一级

## 二级

### 三级

#### 四级

##### 五级

###### 六级

- 说明：可以看到，只有一、二级有横线分隔，三到六级都没有下横线分隔，一般使用到三级就够了，五、六级的标题似乎比正文的字体大小还小。

## 二、换行 - “空格”-“空格”-“回车”

单纯的在编辑窗口里按Enter换行
是不会显示换行的。只会输出显示一个空格。要想真正换行，需要在句末输入两个空格再Enter，  
就会在同一段内换行。

**另起一段**的话，就按两次Enter。即是段落与段落之间空一行。

## 三、字体 - *

这是常规正文文本，使用不同级数的“*”星号来设置：*斜体*，**粗体** 和 ***斜粗体***。  
也可以使用“_”来设置：_斜体_，__粗体__，___斜粗体___  
（由于是英文的下横线，输入中文时不方便，建议统一使用星号）。

## 四、分割线 - ***

分割线可以使用三点***、三短横线（英文）---或三下划线（英文）___。  

- 示例：

***
---
___

## 五、删除线 - ~~

删除线使用两个波浪线来设置：  

- 示例（不同格式的内容）：  
正文（无格式）  
*斜体*（带*号）  
~~删除~~（带~号）  
**粗体**（带**号）

## 六、下划线 - \<u>

正文中<u>这里</u>带下划线。  

## 七、脚注 - \[^...]

脚注可以对文本作进一步的补充说明。

- 示例：  
VSCode是[^Microsoft]一款软件产品的名称。脚注的位置可以放在任何地方，当然最好是容易修改的地方。脚注还会自动编号。  
[^Microsoft]:美国微软公司

## 八、列表

### 1、无序列表 - *, +, -

使用*、+或-号都行，后面加一个空格：  

- gagddf  
- agdfafd
### 2、有序列表 - 1.
使用数字加点.号来表示：  
1.dfsdf  
2.dfadf

### 3、列表可以互相嵌套

在子列表前加Tab、两个或四个空格均可：  
+ sss  
  - aaa  
    - ccc 
+ bbb  
  - ddd

## 九、区块 - \>

- 语法：段落前使用**单边**“\>” + “空格”
- 示例：

>#include<stdio.h>  
int main(void){  
  printf("hello,world");
  return 0;  
}

区块也可以嵌套，如下：
  >最外层
  >>第一层
  >>>第二层  

区块可以包含如列表等其他元素，如下：
>区块中使用列表  
>1.第一项  
>2.第二项
>+ 第一项
>+ 第二项
>+ 第三项  

列表也可以嵌套区块，需要在\>前添加四个空格缩进，如下：
>* 第一项
>    >第一项  
>    >第二项
>* 第二项

### 十、代码 - `（反引号）

示例：  
1.函数或代码片段，如`printf()`函数。  
2.代码块，使用三连反引号```包起来并指定一种语言，如:

```C
#include<stdio.h>
int main(void){
  printf("Hello, world!");
}
```

### 十一、链接

- 语法  
1.[链接名称](链接地址)  
2.<链接地址>

- 高级链接  
[链接名称][设置变量]

### 十二、图片

- 语法：![alt 属性文本](图片地址 "可选标题")
- 示例：![alt 我的B站头像](https://i2.hdslb.com/bfs/face/fa2ddb1b0ab20a5d168ccf64523d5ea5882203d3.jpg@240w_240h_1c_1s_!web-avatar-nav.webp "蓝衣服小男孩")

### 十三、表格 - |和-

Markdown使用|来分隔单元格，使用-来分隔表头。  

- 示例：

|热带水果|蔬菜|温带肉类|
|:---|:---:|---:|
|香蕉|西红柿|猪肉|
|苹果|蕨菜|牛肉|

- 说明：如上所示，第二行分隔线使用三段---表示，冒号的位置可设置单元格内容的对齐方式。段前最好用空行分隔一下。

### 十四、其他

- Markdown还支持HTML的标签。
- 转义字符使用反斜杠\以显示。
- 支持KaTeX和MathJax数学表达式
- 示例：使用\$\*\*\*\$输入行内表达式，\$\$\*\*\*\$\$输入块内的表达式，如下：

$f(x)=sin(x) + 12$
$$\sum_{n=1}^{100}\frac{f(x)-N}{N-f(x)}$$

$$
\begin{Bmatrix}
   a & b \\
   c & d
\end{Bmatrix}
$$
$$
\begin{CD}
   A @>a>> B \\
@VbVV @AAcA \\
   C @= D
\end{CD}
$$

- 更多使用规范请参考[KaTeX官方文档](https://katex.org/docs/supported)。
