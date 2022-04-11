#!/usr/bin/python3
"""
    Python script to export data in the JSON format
    Records all tasks from all employees
"""
import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    users = requests.get("{}users".format(url)).json()
    tasks = requests.get("{}todos".format(url)).json()
    records = {}

    for user in users:
        Employee_id = user.get("id")
        name = user.get("username")

        for task in tasks:
            if (task.get("userId") == int(Employee_id)):
                user_dict = {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": name
                }
                tasks.append(user_dict)

        records[Employee_id] = tasks

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as file:
        json.dump(records, file)
