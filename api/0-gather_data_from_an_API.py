#!/usr/bin/python3
"""Returns a list of completed tasks for a given employee ID"""

import requests
from sys import argv

if __name__ == "__main__":
    e_id = int(argv[1])
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(e_id)
    ).json()
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(e_id)
    ).json()
    completed_tasks = []
    for task in tasks:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completed_tasks), len(tasks)
        )
    )
    for task in completed_tasks:
        print("\t {}".format(task))
