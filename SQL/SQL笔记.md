# 1 - SQL入门

SQL(Structured Query Language)是一种用于在数据库中存储、操作和检索数据的标准语言。

## SQL基础语法

三个层级：库 > 表 > 数据

这里的SQL语言使用MySQL，图像化界面使用DBeaver。

命令行操作：

```cmd
>> mysql -uroot -p                          # 以密码登入根数据库
>> show databases;                          # 查看数据库
>> use 数据库名;                             # 使用数据库
>> create database 数据库名 [carset utf8];   # 字符集utf8创建新库
>> show tables;                             # 查看数据库中的表
>> drop table 表名;                          # 删除表
>> exit                                     # 退出MySQL，特别地，exit不用【;】，其他操作都要加上分号
```

SQL语言根据功能分成4类操作：

1. `DDL`（Data Definition Language）数据定义：库和表的创建和删除
2. `DML`（Data Manipulation Language）数据操纵：数据的新增、删除和修改
3. `DCL`（Data Control Language）数据控制：用户的密码，权限等操作
4. `DQL`（Data Query Language）数据查询：数据的查询和计算

SQL语法特征：

- 大小写不敏感
- 可以跨行书写，以【;】分号结束
- 支持注释
  - 单行：`-- 注释内容`或`# 注释内容`
  - 多行：`/* 注释内容*/`

### DDL操作

```SQL
use 数据库名;                             # 选定库

show tables;                             # 显示选定库的所有表

create table student(
    id int,                              # 列名称 + 列类型 + ,
    w8t float,                           # int是整数，float浮点数
    n4me varchar(10),                    # 文本，括号内是最大长度限制  
);

drop table student;                      # 删除表
```

### DML操作

```SQL
-- 创建表
create table student(
 id int,                                ## 定义3个列属性（名字+类型），表现为表头
 name varchar(10),
 age int
);

-- 新增数据
insert into student (id) values(1), (2), (3);   # id列新增3个值

insert into student (id, name, age) values(4, '周杰轮', 31), (5, '林均节', 29);     # 分别给3个列新增2组值

-- 删除数据
-- delete from 表名称 [where 条件判断];
delete from student where id = 1;               # 删掉id=1的数据，不写条件表示整个表

-- 修改数据
-- update 表名称 set 列 = 值 [where 条件判断];
update student set name = '张雪有' where id = 4; # 符合id=4条件的修改为name='张雪有'
```

注意：

- 字符串只用`'`单括号包裹。
- 条件判断的操作符可以是`=`，`<`，`>`，`<=`，`>=`，`!=`等

### DQL操作

```SQL
-- 基础查询
-- select 字段列表|* from 表 [where 条件判断];
select gender, avg(age) from student;

-- 聚合分组查询
-- select 字段列表|聚合函数 from 表 [where 条件判断] group by 列;
select gender, avg(age) from student group by gender;

-- 结果排序 + 分页展示
/*
select 字段列表|聚合函数 from 表 [where 条件判断] 
group by 列 
order by 列 [asc|desc];                           # 默认asc升序，desc降序
limit [n,]m                                       # 【跳过第n个】取m个显示
*/
select gender, avg(age) from student group by gender;
```

常用分组聚合函数：

- sum(列) 求和
- avg(列) 求平均值
- min(列) 求最小值
- max(列) 求最大值
- count(列|*) 求数量
