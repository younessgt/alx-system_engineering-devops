#!/usr/bin/python3
""" that, using given REST API, for a given employee ID
returns information about his/her TODO list progress"""

import requests
from sys import argv

response = requests.get("https://jsonplaceholder.typicode.com/users")
for emp in response.json():
    if emp.get("id") == int(argv[1]):
        employe_name = emp.get("name")

response2 = requests.get("https://jsonplaceholder.typicode.com/todos")
total_task = 0
num_of_task_done = 0
list_task_title = []
for todo in response2.json():
    if todo.get("userId") == int(argv[1]):
        total_task += 1
        if todo.get("completed") is True:
            num_of_task_done += 1
            list_task_title.append(todo.get("title"))
print(f"Employee {employe_name} is done with tasks("
      f"{num_of_task_done}/{total_task}):")
for title in list_task_title:
    print(f"\t {title}")
