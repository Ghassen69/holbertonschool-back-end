#!/usr/bin/python3
"""gather data from an api"""

import requests
from sys import argv

if __name__ == "__main__":
    employee_id = int(argv[1])
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ).json()
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id)
    ).json()
    completed_tasks = []
    for task in tasks:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task))
