### 作者：黄方
### 程序介绍：
'''
员工信息表程序，实现增删改查操作：
1、可进行模糊查询，语法至少支持下面3种:
    select name,age from staff_table where age > 22
　  select * from staff_table where dept = "IT"
    select * from staff_table where enroll_date like "2013"
2、查到的信息，打印后，最后面还要显示查到的条数
3、可创建新员工纪录，以phone做唯一键，staff_id需自增，语法如下：
    insert into staff_table values ("Mona","30","13535324567","IT",> "2017-02-17")
4、可删除指定员工信息纪录，输入员工id，即可删除，语法如下：
    delete from staff_table where staff_Id = 3
5、可修改员工信息，语法如下:
　　 UPDATE staff_table SET dept="Market" where dept = "IT"
注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码
'''

### 程序结构：
```
staff/
|——readme
|——bin #staff 执行文件 目录
|  |—— __init__.py
|  |—— staff.py #staff 执行程序
|  |—— staff_table 数据存储文件
|——conf #配置文件
|  |—— __init__.py
|  |—— setting.py
|——core #主要程序逻辑目录
|  |—— __init__.py
|  |—— main.py
|  |   |—— read_table
|  |   |—— write_table
|  |   |—— sql_manage
|  |   |—— insert_action
|  |   |—— select_action
|  |   |—— print_select_age
|  |   |—— delete_action
|  |   |—— update_action
|  |   |—— run
```