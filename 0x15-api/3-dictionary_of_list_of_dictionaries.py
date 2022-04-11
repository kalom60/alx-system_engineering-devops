#!/usr/bin/python3
"""
    Python script to export data in the JSON format
    Records all tasks from all employees
"""
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users".format(url)).json()

    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump({
            user.get("id"): [{
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            } for task in requests.get("{}todos".format(url),
                                       params={
                                           "userId": user.get("id")
            }).json()]
            for user in users}, file)
