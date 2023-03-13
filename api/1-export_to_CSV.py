#!/usr/bin/python3
"""gather data mechni lil waynbe
azsakzaklhzazamlkjzaz api"""

import csv
import requests
import sys

if __name__ == "__main__":
    """gather data from an api"""
    user_id = sys.argv[1]
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    username = response.json().get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = todos.json()

    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for task in tasks:
            if task.get('userId') == int(user_id):
                task_completed = str(task.get('completed'))
                task_title = task.get('title')
                writer.writerow([user_id, username, task_completed, task_title])
