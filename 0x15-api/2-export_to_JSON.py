#!/usr/bin/python3
"""
    Python script to export data in the JSON format
"""
import json
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    Employee_id = sys.argv[1]
    user = '{}users/{}'.format(url, Employee_id)
    json_obj = requests.get(user).json()
    name = json_obj.get('username')

    todo = '{}todos?userId={}'.format(url, Employee_id)
    tasks = requests.get(todo).json()

    user_task = []
    for task in tasks:
        task_obj = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': name
        }

        user_task.append(task_obj)
    to_json = {str(Employee_id): user_task}

    filename = '{}.json'.format(Employee_id)
    with open(filename, 'w') as file:
        json.dump(to_json, file)
