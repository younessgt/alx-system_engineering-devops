#!/usr/bin/python3
""" extend the task 0 to export data in the json format"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    data = {}
    file_name = "todo_all_employees.json"
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    for user in res.json():
        userid = user.get("id")
        username = user.get("username")
        data[userid] = []
        res2 = requests.get(
                "https://jsonplaceholder.typicode.com/todos?userId={}"
                .format(userid))
        for todo_task in res2.json():
            data2 = {
                "username": username,
                "task": todo_task.get('title'),
                "completed": todo_task.get('completed')
                }
            data[userid].append(data2)

    with open(file_name, mode="w") as f:
        json.dump(data, f)
