#!/usr/bin/python3
"""
    Python script to export data in the CSV format
"""
import csv
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    Employee_id = sys.argv[1]
    user = '{}users/{}'.format(url, Employee_id)
    json_obj = requests.get(user).json()

    todo = '{}todos?userId={}'.format(url, Employee_id)
    tasks = requests.get(todo).json()

    filename = '{}.csv'.format(Employee_id)
    with open(filename, 'w', newline='') as file:
        task_writer = csv.writer(file, delimiter=',',
                                 quotechar='"', quoting=csv.QUOTE_ALL)

        for task in tasks:
            task_writer.writerow([int(Employee_id), json_obj.get('username'),
                                  task.get('completed'),
                                  task.get('title')])
