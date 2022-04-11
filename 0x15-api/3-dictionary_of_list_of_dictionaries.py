#!/usr/bin/python3
"""
    Python script to export data in the JSON format
    Records all tasks from all employees
"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(url)
    res = requests.get(user)
    json_obj = res.json()
    record = {}

    for user in json_obj:
        name = user.get('username')
        Employee_id = user.get('id')

        todos = '{}todos?userId={}'.format(url, Employee_id)
        res = requests.get(todos)
        tasks = res.json()
        all_task = []

        for task in tasks:
            task_obj = {"username": name,
                        "task": task.get('title'),
                        "completed": task.get('completed')}
            all_task.append(task_obj)

        record[str(Employee_id)] = all_task

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as file:
        json.dump(record, file)
