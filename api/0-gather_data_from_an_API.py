#!/usr/bin/python3
"""gather data from an api"""

import requests
from sys import argv

if __name__ == "__main__":
    completed_tasks = 0
    total_tasks = 0

    user_id = argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    )
    user_name = user.json().get('name')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')

    for task in tasks.json():
        if task.get('userId') == int(user_id):
            total_tasks += 1
            if task.get('completed'):
                completed_tasks += 1

    print('Employee {} is done with tasks({}/{}):'.format(
        user_name, completed_tasks, total_tasks
    ))

    formatted_titles = [
        "\t " + task.get('title')
        for task in tasks.json()
        if task.get('userId') == int(user_id) and task.get('completed')
    ]
    formatted_output = '\n'.join(formatted_titles)
    print(formatted_output)
