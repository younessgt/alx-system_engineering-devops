#!/usr/bin/python3
""" extend the task 0 to export data in the CSV format"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    data = []
    file_name = f"{argv[1]}.csv"
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
            data.append(
                    [int(argv[1]),
                     employe_name,
                     todo.get("completed"),
                     todo.get("title")])

            total_task += 1
            if todo.get("completed") is True:
                num_of_task_done += 1
                list_task_title.append(todo.get("title"))

    with open(file_name, mode="w", newline="") as f:
        writer = csv.writer(f)

        for row in data:
            writer.writerow(row)
