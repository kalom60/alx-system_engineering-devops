#!/usr/bin/python3
"""This script will extract information and save it in json file"""
import json
import requests

if __name__ == "__main__":
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    user = requests.get("https://jsonplaceholder.typicode.com/users")
    json_todo = todo.json()
    json_user = user.json()
    todo_list = json_todo[:]
    user_list = json_user[:]
    id_list = []
    for i in todo_list:
        id_list.append(i)
    user_name = []
    for i in user_list:
        user_name.append(i)
    for i in user_name:
        for j in id_list:
            if j['userId'] == i['id']:
                del j['id']
                j['task'] = j['title']
                del j['title']
                j['username'] = j['userId']
                j['username'] = i['username']
    for i in id_list:
        del i['userId']
    i = 0
    list_of_list = []
    while (i < len(id_list)):
        list_of_list.append(id_list[i:i+20])
        i += 20
    file_name = "todo_all_employees.json"
    with open(file_name, "w", encoding='utf-8') as f:
        dic = {}
        for i in list_of_list:
            for j in i:
                for k in user_name:
                    if j['username'] == k['username']:
                        dic[str(k['id'])] = i
        f.write(json.dumps(dic))
