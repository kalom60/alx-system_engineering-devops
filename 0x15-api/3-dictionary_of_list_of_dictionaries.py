#!/usr/bin/python3
"""
    Python script to export data in the JSON format
    Records all tasks from all employees
"""
import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    users = requests.get('{}users'.format(url)).json()
    records = {}
    name = {}

    for user in users:
        Employee_id = user.get("id")
        records[Employee_id] = []
        name[Employee_id] = user.get("username")

    todos = requests.get('{}todos'.format(url)).json()
    for todo in todos:
        Employee_id = todo.get("userId")
        todo_obj = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": name.get(Employee_id)
        }
        records.get(Employee_id).append(todo_obj)

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as file:
        json.dump(records, file)
