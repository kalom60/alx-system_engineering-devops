#!/usr/bin/python3
"""
    Python script to export data in the JSON format
    Records all tasks from all employees
"""
import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/'.format(url)
    json_obj = requests.get(user).json()

    user_task = {}
    for obj in json_obj:
        Employee_id = obj.get('id')
        Employee_name = obj.get('username')
        user_task[Employee_id] = []

        todo = '{}todos?userId={}'.format(url, Employee_id)
        tasks = requests.get(todo).json()

        for obj in tasks:
            task_obj = {
                'username': Employee_name,
                'task': obj.get('title'),
                'completed': obj.get('completed')
            }
            user_task[Employee_id].append(task_obj)

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as file:
        json.dump(user_task, file)
