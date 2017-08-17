#Author:Huangf
import json
import sys
import os

def read_table():
    #读取数据
    filePath = sys.path[0]+ os.sep +"staff_table"
    f = open(filePath,"r",encoding="utf-8")
    employee_dict = {}
    for line in f:
        dict = {}
        arr = line.strip().split(",")
        dict["staff_Id"] = arr[0]
        dict["name"] = arr[1]
        dict["age"] = arr[2]
        dict["dept"] = arr[4]
        dict["enroll_date"] = arr[5]
        employee_dict[arr[3]] = dict
    f.close()
    return employee_dict

def write_table(dict):
    #数据写入文件
    filePath = sys.path[0] + os.sep + "staff_table"
    f = open(filePath, "w",encoding="utf-8")
    s_all = ''
    s_list = []
    for i in range(len(dict)):
        for k, v in dict.items():
            if len(s_list)+1 == int(v["staff_Id"]):
                v_list = [v["staff_Id"],v["name"],v["age"],k,v["dept"],v["enroll_date"]]
                s = ",".join(v_list)
                s_list.append(s)
    s_all = "\n".join(s_list)
    f.write(s_all)
    f.close()

def sql_manage(sql):
    #处理sql语句
    key_dict = {
        "where":"",
        "set":"",
        "values":"",
        "limit":""
    }
    # sql = sql.lower()
    # print(sql)
    sql_list = sql.split()
    action = sql_list[0]
    for i in sql_list[1:]:
        j = i.lower()
        if j in key_dict:
            # index = sql(i)
            key_dict[j] = sql[sql.index(i)+len(i)+1:]
    print(key_dict)
    return key_dict

#insert into staff_table values ("Mona","30","13535324567","IT","2017-02-17")Rain,25,13832353222,Sales,2016-04-22
def insert_action(string):
    #创建新员工
    data = read_table()
    dict = sql_manage(string)
    sql_list = string.split()
    if sql_list[2] == "staff_table":
        values = dict["values"]
        values = values[1:len(values)-1]
        values = values.replace("\"",'')
        v_list = values.split(",")
        print(v_list)
        if len(v_list)==5:
            v_dict = {}
            v_dict["staff_Id"] = str(len(data)+1)
            v_dict["name"] = v_list[0]
            v_dict["age"] = v_list[1]
            v_dict["dept"] = v_list[3]
            v_dict["enroll_date"] = v_list[4]
            data[v_list[2]] = v_dict
            print(data)
            write_table(data)
            return True
        return False
    else:
        return False

#select name,age from staff_table where age > 22
#select * from staff_table where age > 22
#select * from staff_table where dept = "IT"
#select * from staff_table where enroll_date like "2013"
def select_action(string):
    #查找员工
    data = read_table()
    dict = sql_manage(string)
    sql_list = string.split()
    if sql_list[3] == "staff_table":
        info = sql_list[1]
        if info == "*":
            w_list = dict["where"].split()
            if w_list[0] == "age":
                age = int(w_list[2])
                return print_select_age(age,w_list[1])
            elif w_list[0] == "dept":
                if w_list[1] == "=":
                    print("staff_Id".center(10, " "), "name".center(10, " "), "age".center(10, " "),
                          "phone".center(12, " "), "dept".center(10, " "), "enroll_date".center(12, " "))
                    print("".center(70, "-"))
                    for k, v in data.items():
                        if "\""+v["dept"]+"\""== w_list[2]:
                            print(v["staff_Id"].center(10, " "), v["name"].center(10, " "), v["age"].center(10, " "),
                                  k.center(12, " "), v["dept"].center(10, " "), v["enroll_date"].center(12, " "), )
                    print("".center(70, "-"))
                    return True
                return False
            elif w_list[0] == "enroll_date":
                if w_list[1] == "like":
                    print("staff_Id".center(10, " "), "name".center(10, " "), "age".center(10, " "),
                          "phone".center(12, " "), "dept".center(10, " "), "enroll_date".center(12, " "))
                    print("".center(70, "-"))
                    for k, v in data.items():
                        if w_list[2][1:len(w_list[2])-1] in v["enroll_date"] :
                            print(v["staff_Id"].center(10, " "), v["name"].center(10, " "), v["age"].center(10, " "),
                                  k.center(12, " "), v["dept"].center(10, " "), v["enroll_date"].center(12, " "), )
                    print("".center(70, "-"))
                    return True
                return False
            else:
                return False
        else:
            info_list = info.split(",")
            if len(info_list) > 0:
                # print(info_list)
                w_list = dict["where"].split()
                if w_list[0] == "age":
                    age = int(w_list[2])
                    if len(info_list) == 1:
                        return print_select_age(age, w_list[1], info_list[0])
                    elif len(info_list) == 2:
                        return print_select_age(age, w_list[1], info_list[0],info_list[1])
                    elif len(info_list) == 3:
                        return print_select_age(age, w_list[1], info_list[0],info_list[1],info_list[2])
                    elif len(info_list) == 4:
                        return print_select_age(age, w_list[1], info_list[0],info_list[1],info_list[2],info_list[3])
                    elif len(info_list) == 5:
                        return print_select_age(age, w_list[1], info_list[0],info_list[1],info_list[2],info_list[3],info_list[4])
                elif w_list[0] == "dept":
                    pass
                elif w_list[0] == "enroll_date":
                    pass
            return False
    else:
        return False

def print_select_age(age,type,*args):
    #打印查找员工
    data = read_table()
    if args:
        string = "staff_Id".center(12, " ")
        if "name" in args:
            string = string + "name".center(12, " ")
        if "age" in args:
            string = string + "age".center(12, " ")
        if "phone" in args:
            string = string + "phone".center(12, " ")
        if "dept" in args:
            string = string + "dept".center(12, " ")
        if "enroll_date" in args:
            string = string + "enroll_date".center(12, " ")
        print(string)
        print("".center(len(args)*12+20, "-"))
        if type == ">":
            for k, v in data.items():
                if int(v["age"]) > age:
                    p_str = v["staff_Id"].center(12, " ")
                    if "name" in args:
                        p_str = p_str +  v["name"].center(12, " ")
                    if "age" in args:
                        p_str = p_str + v["age"].center(12, " ")
                    if "phone" in args:
                        p_str = p_str + k.center(12, " ")
                    if "dept" in args:
                        p_str = p_str + v["dept"].center(12, " ")
                    if "enroll_date" in args:
                        p_str = p_str +  v["enroll_date"].center(12, " ")
                    print(p_str)
        elif type == "=":
            for k, v in data.items():
                if int(v["age"]) == age:
                    p_str = v["staff_Id"].center(12, " ")
                    if "name" in args:
                        p_str = p_str + v["name"].center(12, " ")
                    if "age" in args:
                        p_str = p_str + v["age"].center(12, " ")
                    if "phone" in args:
                        p_str = p_str + k.center(12, " ")
                    if "dept" in args:
                        p_str = p_str + v["dept"].center(12, " ")
                    if "enroll_date" in args:
                        p_str = p_str + v["enroll_date"].center(12, " ")
                    print(p_str)
        elif type == "<":
            for k, v in data.items():
                if int(v["age"]) < age:
                    p_str = v["staff_Id"].center(12, " ")
                    if "name" in args:
                        p_str = p_str + v["name"].center(12, " ")
                    if "age" in args:
                        p_str = p_str + v["age"].center(12, " ")
                    if "phone" in args:
                        p_str = p_str + k.center(12, " ")
                    if "dept" in args:
                        p_str = p_str + v["dept"].center(12, " ")
                    if "enroll_date" in args:
                        p_str = p_str + v["enroll_date"].center(12, " ")
                    print(p_str)
        else:
            return False
        print("".center(len(args)*12+20, "-"))
        return True
    else:
        print("staff_Id".center(12, " "), "name".center(12, " "), "age".center(12, " "), "phone".center(12, " "),
              "dept".center(12, " "), "enroll_date".center(12, " "))
        print("".center(80, "-"))
        if type == ">":
            for k, v in data.items():
                if int(v["age"]) > age:
                    print(v["staff_Id"].center(12, " "), v["name"].center(12, " "), v["age"].center(12, " "),
                          k.center(12, " "), v["dept"].center(12, " "), v["enroll_date"].center(12, " "))
        elif type == "=":
            for k, v in data.items():
                if int(v["age"]) == age:
                    print(v["staff_Id"].center(12, " "), v["name"].center(12, " "), v["age"].center(12, " "),
                          k.center(12, " "), v["dept"].center(12, " "), v["enroll_date"].center(12, " "))
        elif type == "<":
            for k, v in data.items():
                if int(v["age"]) < age:
                    print(v["staff_Id"].center(12, " "), v["name"].center(12, " "), v["age"].center(12, " "),
                          k.center(12, " "), v["dept"].center(12, " "), v["enroll_date"].center(12, " "))
        else:
            return False
        print("".center(80, "-"))
        return True

#delete from staff_table where staff_Id = 3
def delete_action(string):
    #删除员工
    data = read_table()
    dict = sql_manage(string)
    sql_list = string.split()
    if sql_list[2] == "staff_table":
        w_list = dict["where"].split()
        if len(w_list)==3:
            if w_list[0] == "staff_Id" and w_list[1] == "=":
                for k,v in data.items():
                    if v["staff_Id"] == w_list[2]:
                        data.pop(k)
                        for k2, v2 in data.items():
                            if int(v2["staff_Id"])>int(w_list[2]):
                                v2["staff_Id"] = str(int(v2["staff_Id"])-1)
                        write_table(data)
                        return True
    return False

#update staff_table set dept = "Market" where dept = "IT"
def update_action(string):
    #修改员工数据
    data = read_table()
    dict = sql_manage(string)
    sql_list = string.split()
    if sql_list[1] == "staff_table":
        s_list = dict["set"]
        s_list = s_list.replace("\"","").split()
        w_list = dict["where"]
        w_list = w_list.replace("\"", "").split()
        for k,v in data.items():
            if w_list[0] in v:
                if w_list[0] == s_list[0] and w_list[0] is not "name":
                    if v[w_list[0]] == w_list[2]:
                        v[w_list[0]] = s_list[2]
                else:
                    return False
            else:
                return False
        write_table(data)
        return True

    return False




def run():
    action_dict = {
        "insert":insert_action,
        "select":select_action,
        "delete":delete_action,
        "update":update_action
    }

    while True:
        sqlStr = input("sql>").strip()
        # sqlStr = sqlStr.strip()
        action = sqlStr.split()[0]
        action = action.lower()
        if action_dict.get(action):
            result = action_dict[action](sqlStr)
            if result == False:
                print("you sql command is not right!")
        elif sqlStr == "q":
            break
        else:
            print("you sql command is not right!")





