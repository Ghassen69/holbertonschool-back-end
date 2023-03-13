#!/usr/bin/python3
"""gather data api."""

import requests
import sys

if __name__ == '__main__':
    completed = 0
    totalTasks = 0
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        employee_id = int(sys.argv[1])
        user_response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(employee_id))
        name = user_response.json().get('name')
        todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')

        if user_response.ok and todos_response.ok:
            user_data = user_response.json()
            todos_data = todos_response.json()

    for task in todos_data.json():
        if task.get('userId') == int(employee_id):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos_data.json()
          if task.get('userId') == int(employee_id) and task.get('completed')]))
