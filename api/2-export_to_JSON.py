#!/usr/bin/python3
"""Exporting to JSON"""

import json
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(
        api_url + "todos", params={"userId": sys.argv[1]}).json()

    tasks_dict = {user.get("id"): [{"task": task.get("title"),
                                    "completed": task.get("completed"),
                                    "username": user.get("username")}
                                   for task in todos]}

    json_file_name = sys.argv[1] + ".json"
    with open(json_file_name, "w") as json_file:
        json.dump(tasks_dict, json_file)
