#!/usr/bin/python3
"""gather data api."""

import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(employee_id))

    employee_name = employee.json().get('name')

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    completed_count = 0
    total_tasks_count = 0
    for task in tasks.json():
        if task.get('userId') == int(employee_id):
            total_tasks_count += 1
            if task.get('completed'):
                completed_count += 1

    print('Employee {} has completed ({}/{}) tasks:'
          .format(employee_name, completed_count, total_tasks_count))

    filtered_tasks = [
        task for task in tasks.json()
        if task.get('userId') == int(employee_id) and task.get('completed')
    ]
    formatted_titles = [
        "\t " + task.get('title')
        for task in filtered_tasks
    ]
    formatted_output = '\n'.join(formatted_titles)
    print(formatted_output)
