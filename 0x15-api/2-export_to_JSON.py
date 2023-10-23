#!/usr/bin/python3
""" extend the task 0 to export data in the json format"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    data = []
    file_name = f"{argv[1]}.json"
    res = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(argv[1]))
    emp_username = res.json().get("username")

    res2 = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(argv[1]))

    data = {}
    data[argv[1]] = []
    for task in res2.json():
        data2 = {
             "task": task.get('title'),
             "completed": task.get('completed'),
             "username": emp_username
                }
        data[argv[1]].append(data2)

    with open(file_name, mode="w") as f:
        json.dump(data, f)
