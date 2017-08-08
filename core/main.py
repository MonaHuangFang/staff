#Author:Huangf
import json
import sys

def read_table():
    filePath = sys.path[0]+"/"+"staff_table"
    f = open(filePath,"r")
    employee_list = {}
    for line in f:
        dict = {}
        arr = line.split(",")
        dict["staff_Id"] = arr[0]
        dict["name"] = arr[1]
        dict["age"] = arr[2]
        dict["dept"] = arr[4]
        dict["enroll_date"] = arr[5]
        employee_list[arr[3]] = dict
    f.close()
    return employee_list

def sql_manage(sql):
    key_dict = {
        "where":"",
        "set":"",
        "values":"",
        "limit":""
    }
    sql_list = sql.split()
    action = sql_list[0]
    for i in sql_list[1:]:
        if i in key_dict:
            key_dict[i] = sql_list[sql_list.index(i+1):]
    print(key_dict)

def insert_action(str):
    data = read_table()

def select_action(str):
    data = read_table()

def delete_action(str):
    data = read_table()

def update_action(str):
    data = read_table()

def run():
    action_dict = {
        "insert":insert_action,
        "select":select_action,
        "delete":delete_action,
        "update":update_action
    }

    sqlStr = raw_input("sql>")
    # sqlStr = sqlStr.strip()
    sql_manage(sqlStr)
    action = sqlStr.split()[0]
    action = action.lower()
    if action_dict.get(action):
        action_dict[action](sqlStr)
    else:
        print ("you sql command is not right!")




